---
type: Software
title: "AthenaK"
description: "Stone et al.'s Kokkos rewrite of the Athena++ block-based adaptive-mesh-refinement framework: finite-volume PLM, PPM and WENO-Z reconstruction on primitive variables, HLL-family and Roe solvers, low-storage SSP and IMEX Runge–Kutta, constrained transport and a first-order flux-correction fallback, with Newtonian, relativistic and radiation modules running on CPUs and GPUs."
status: established
aliases: [AthenaK, Athena-K]
tags: [software, gpu, amr, mhd, relativistic, finite-volume]
timestamp: 2026-10-24T05:59:00Z
---

# AthenaK

AthenaK is a from-scratch reimplementation of the
[block-based adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
framework and the fluid solvers of Athena++ in the Kokkos C++
performance-portability library, so that one source runs on CPUs, NVIDIA
and AMD GPUs and ARM processors
([Stone et al. (2026)](/sources/stone-2026.md), §1–2). The authors state
that "very little of the overall design was changed, although the
implementation is completely new" (§2). It is an outgrowth of the
Parthenon collaboration and shares features with Parthenon and the codes
built on it, but is "a much smaller and simpler project" aimed at
astrophysical fluid dynamics (§1). The numerical methods are recalled from
the Athena lineage, not new; the paper's contribution is the software and
its performance data. It is open source (BSD-3) and built with cmake, with
physics chosen at run time in the input file (§2).

## Framework

- **AMR design inherited from Athena++** (§2): MeshBlocks in an octree
  (binary tree and quadtree in 1D and 2D) labelled by Z-ordering,
  communication between levels only at block boundaries, flux corrections
  at level boundaries for conservation, one time step on all levels, and
  execution through task lists.
- **MeshBlockPacks**: all MeshBlocks of a device form one aggregate, so one
  kernel launch covers them; the idea is credited to Parthenon. The authors
  state that this "greatly enhances performance when there are a large
  number of small MeshBlocks on the same device" (§2).
- **Data locality**: variables are Kokkos Views with one index more than
  the array of a single MeshBlock, the extra index being the MeshBlock, resident on the device and copied to the
  host only for output; the mesh tree is built and refined on the host;
  ghost-zone buffers go by point-to-point MPI, and prolongation and
  restriction of all blocks are done at once in parallel kernels (§2).
- **Kernels**: fewer temporaries per kernel and templating of algorithmic
  options such as the Riemann solver reduce register spill and "can
  greatly improve performance" (§2).
- **Geometry**: uniform Cartesian meshes only. The authors argue that the
  coordinate choice matters at the level of truncation error and that
  higher-order schemes are simpler in Cartesian coordinates; 2D
  axisymmetric calculations are therefore not possible (§2), and the
  Cartesian GRMHD module does not conserve angular momentum to machine
  precision, as HARM does (§3.6).
- **Load balancing** gives each MeshBlock a cost proportional to its cells
  and physics modules and redistributes blocks while keeping Z-ordering
  (§5.2). Most modules also run in single precision (§5.1).

## Numerical method

- **Finite-volume "reconstruct–solve–advance"** for
  $\partial_tu+\nabla\cdot f=S$, with the induction equation advanced
  separately (§3, Eqs. (1)–(2)).
- **Reconstruction**, always of primitive variables: piecewise linear
  (PLM), the [piecewise parabolic method](/methods/piecewise-parabolic-method.md)
  with the original Colella–Woodward limiters ("PPM4") or the
  extremum-preserving limiters of McCorquodale et al. ("PPMX"), and
  [WENO-Z](/methods/weno-z.md) of Borges et al.; no formulas are printed.
  [Characteristic reconstruction](/methods/characteristic-decomposition.md)
  is not implemented, "largely because of the complexity of the
  implementation for general relativistic flows" (§3).
- **Riemann solvers**: [local Lax–Friedrichs](/methods/lax-friedrichs-flux.md),
  [HLLE, HLLC, HLLD](/methods/hll-riemann-solvers.md) and
  [Roe](/methods/roe-riemann-solver.md); the GRMHD module has only the GR
  versions of LLF and HLLE (§3, §3.6).
- **Time integration** by the method of lines with low-storage
  [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) methods from first to
  fourth order (Ketcheson), at $\Delta t\le\nu\min_d\Delta x_d/a_d$ with
  $\nu\le1$ and generally $\nu\le1/N_{\mathrm{dim}}$ (Eq. (3); page-local
  $a_d$ the largest cell-centred signal speed in direction $d$,
  $N_{\mathrm{dim}}$ the number of dimensions), and
  [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) methods (Pareschi–Russo,
  printed "Pareshi", and the positivity-preserving scheme of Krapp et al.)
  for stiff ion–neutral drag (§3, §3.4). The unsplit CTU integrator is not
  implemented because it does not extend easily to relativistic equations
  (§3).
- **Magnetic field**: face-averaged field advanced by staggered
  [constrained transport](/methods/constrained-transport.md) (Evans–Hawley)
  with the upwind edge electric fields of Gardiner & Stone, which the
  authors call "critical for some problems" although it complicates the
  AMR ghost-zone and flux-conservation logic (§3.2;
  [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).
- **First-order flux correction (FOFC)**, after Lemaster & Stone: in each
  Runge–Kutta stage, if density or pressure in a cell would become
  negative, the fluxes on all its faces are recomputed with
  piecewise-constant states and the LLF flux, before the AMR flux
  correction. It fires about once per $10^{10}$ cell updates in the
  supersonic-turbulence application where it was introduced, but "greatly
  improves the stability of calculations in extreme regimes" and reduces
  the need for floors in GRMHD (§3). It is an a posteriori, cell-flagged
  fallback of the [MOOD](/methods/mood-a-posteriori-limiting.md) kind, with
  positivity as the only detector, and no positivity theorem is given
  ([bound preservation](/properties/bound-preservation.md)). The authors
  attribute positivity failures of multidimensional higher-order
  finite-volume schemes at high kinetic or magnetic energy to truncation
  error, not round-off (§3).
- **Physics modules**: Newtonian hydrodynamics and MHD with explicit
  viscosity, conduction and Ohmic resistivity (second-order differencing,
  unsplit at every stage); two-fluid ion–neutral MHD; special and general
  [relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)
  and MHD, with total energy minus rest mass as the energy variable and the
  conserved-to-primitive solver of Kastaun et al., a departure from
  Athena++; GR gray radiation transport on a geodesic angular grid; tracer
  and charged test particles (§3.3–4.2).

## Verification

As reported, on the following tests (§3–4):

- **Linear waves.** In 1D hydrodynamics PPMX and WENO-Z converge at fourth
  order in $L_1$ and PPM4 and PLM at second order (Fig. 1; one wave period;
  RK3 except PLM with RK2;
  [linear acoustics tests](/benchmarks/linear-acoustics-tests.md)). In 1D
  MHD PPMX and WENO-Z give fourth order for slow and Alfvén waves but only
  second order for the fast wave "even in one dimension", as in Athena++;
  no cause is given (Fig. 3).
- **Shocks.** With 200 cells WENO-Z with RK3 resolves the small scales of
  the [Shu–Osher problem](/benchmarks/shu-osher-problem.md) better than PLM
  with RK2 (Fig. 1). The [Brio–Wu tube](/benchmarks/brio-wu-shock-tube.md)
  shows small ringing near the compound wave, which characteristic
  reconstruction would reduce (Fig. 3). With FOFC the Komissarov
  cylindrical explosions run without the flooring, background modification
  or artificial viscosity other finite-volume SRMHD codes needed (Fig. 10;
  [MHD blast waves](/benchmarks/mhd-blast-wave.md)).
- **Diffusion and stiff sources.** Viscous diffusion of a Gaussian converges
  at second order; Pareschi–Russo IMEX2 overshoots with damped oscillations
  in a stiff drag relaxation where the Krapp et al. scheme converges
  smoothly (Figs. 5, 7).
- **Relativity and radiation.** GR Bondi accretion converges at second order
  with RK2, PLM and HLLE; the field rotation rate of the Blandford–Znajek
  monopole at the horizon is near the expected half of the hole's, compared
  with iharm3d, and a SANE torus is run in the EHT code-comparison setup; a
  radiation linear wave converges at better than first order (Figs. 12–15).

## Performance

- **One device** (PLM, RK2, HLLE linear wave; Table 1): hydro/MHD in
  millions of cell updates per second, 63/33 on a Xeon Gold 6326, 614/298
  on an A100, 677/290 on an H100 and 1077/565 on a Grace Hopper. MHD costs
  about twice hydro; relativistic and radiation modules cost more (Table 2).
  On an A100 shrinking MeshBlocks from $128^3$ to $16^3$ lowers the rate
  from 614 to 126 (§5.1). Nsight Compute measures 8 % of theoretical peak
  overall, up to 22 % for single kernels (§5.1).
- **AMR on one GPU.** A 2D MHD blast with AMR runs at 141 against 181 for
  the uniform $4096^2$ mesh, about 20 % overhead, and needs 18 % of its
  wall-clock time ("5.4× faster"), with identical density (§5.1, Fig. 20).
- **Scaling.** Weak-scaling efficiency above 97 % to 2048 A100 GPUs on
  Polaris, above 90 % to 1024 GPU dies on Crusher, and about 80 % to 65,536
  on Frontier; AMR weak scaling on Frontier is super-linear while MeshBlocks
  grow and nearly perfect at fixed $32^3$ MeshBlocks (§5.2, Figs. 21–22).
  The largest run shown is driven isothermal MHD
  [turbulence](/benchmarks/compressible-isotropic-turbulence.md) on
  $10{,}240^3$ cells with WENO-Z, RK2 and HLLD on 65,536 GPUs (§3.2, Fig. 4).

## Related codes

The authors place AthenaK among Kokkos and GPU codes: Parthenon and the
codes built on it (AthenaPK, KHARMA, Phoebus), [IDEFIX](/software/idefix.md),
the Kokkos implementation of [PLUTO](/software/pluto.md) by Lesur et al.,
and CUDA codes such as Cholla, H-AMR, GAMER-2 and a RAMSES port; AMReX is
named as a GPU-enabled AMR package (§1). Unlike IDEFIX, which has no AMR
and runs on curvilinear meshes, AthenaK has block-based AMR and Cartesian
meshes only (§2; IDEFIX page).

## Qualifications

- **"Order" is observed order.** The fourth order of PPMX and WENO-Z is the
  $L_1$ convergence rate on linear waves with an SSP-RK3 integrator; the
  paper does not state the formal order of the finite-volume scheme. IDEFIX
  is described by [Lesur et al. (2023)](/sources/lesur-2023.md) (§2.3) as at
  most globally second order whatever the reconstruction; the two codes are different implementations, and no
  source runs them on the same problem.
- **Printed slips** (version of record): §3.3 describes the left and right
  panels of Fig. 5 in the opposite order to the caption; the text calls
  Fig. 9 a relativistic MHD blast wave test while its caption calls it the
  SRMHD shock-tube test; §4.2 refers to "the $4096^3$ turbulence
  simulation described in Section 3.2", which describes a $10{,}240^3$ run;
  the Fig. 6 caption calls the MRI run "a 2D (axisymmetric) simulation"
  although §2 states that axisymmetric calculations are not possible; the
  text cites Zhu et al. and Fields et al. as 2024, the reference list as
  2025.
- **Bundle fit.** The paper is about software and performance; its
  discretizations are recalled from earlier Athena papers and enter this
  bundle as ingredients (primitive-variable WENO-Z and PPM, HLL-family
  fluxes, constrained transport, an a posteriori first-order fallback).

# Citations

- [Stone et al. (2026)](/sources/stone-2026.md) — §1; §2; §3, Eqs. (1)–(3); §3.1–3.7, Figs. 1, 3–5, 7, 9–10, 12–15; §4; §5.1–5.2, Tables 1–2, Figs. 20–22; §6.
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §2.3 (IDEFIX at most globally second order; for comparison).
