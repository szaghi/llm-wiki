---
type: Software
title: "AthenaK"
description: "AthenaK is the Kokkos performance-portable rewrite of the Athena++ block-based adaptive-mesh-refinement framework, with Godunov finite-volume hydrodynamics, MHD, two-fluid, relativistic, radiation and particle modules; this page records its design, numerics, first-order flux correction, turbulence demonstration runs up to 10,240^3 cells, and GPU performance and scaling."
status: established
aliases: [Athena K, Athena++ Kokkos version, AthenaK AMR framework]
tags: [software, astrophysics, mhd, gpu, mesh-adaptation, compressible]
timestamp: 2026-10-29T10:10:00Z
---

# AthenaK

**AthenaK** is a from-scratch reimplementation of the block-based
adaptive-mesh-refinement (AMR) framework of Athena++ (Stone et al. 2020,
as cited) in the Kokkos performance-portability model, whose C++ templates
map one source onto CUDA, HIP/ROCm and OpenMP back ends. It is described by
[Stone et al. (2026)](/sources/stone-2026.md), who release it under the
BSD-3 licence. The paper is an astrophysical code paper: turbulence enters
only through demonstration runs (driven MHD turbulence, a turbulent
interstellar medium, two-fluid turbulence and particle transport in
turbulence), none analysed as a turbulence result. Its bearing on this
bundle is as a GPU code for [compressible MHD turbulence](/results/compressible-mhd-turbulence.md)
with [mesh adaptation](/methods/mesh-adaptation.md) and
[WENO-type](/methods/weno-scheme.md) reconstruction. Its predecessor Athena++ is the code of
the guide-field MHD boxes of [Gan et al. (2022)](/sources/gan-2022.md).

## Framework design

What AthenaK keeps from Athena++ (§2): an octree of fixed-size
**MeshBlocks** ordered along a Z-order curve, communication between
refinement levels only at block boundaries, flux correction at level
boundaries, one time step for all levels, and execution through task
lists. What changes (§2):

- **MeshBlockPacks.** All MeshBlocks on a device form one pack, so that one
  kernel launch covers every block; the authors state that this "greatly
  enhances performance when there are a large number of small MeshBlocks
  on the same device". Each physics module is a C++ object stored in the
  pack, with its own memory and task list, which allows several fluids at
  once; the idea comes partly from the Parthenon collaboration, as cited.
- **Data residence.** All dependent variables live on the device as
  Kokkos views with one more index than the dimension (the MeshBlock
  index) and move to the host only for output; the mesh tree is built,
  stored and refined on the host. Boundary buffers are packed in device
  kernels and exchanged by point-to-point MPI, so the number of messages
  grows with the number of MeshBlocks per rank; prolongation and
  restriction run in parallel kernels.
- **Kernels.** Limiting the number of temporaries in a kernel and
  templating algorithmic options such as the Riemann solver reduce
  register spilling significantly, as the authors state; only a few 1-D
  arrays fit in scratch-pad memory. Devices with 80 GB or more hold grids
  up to $512^3$ cells each.
- **Restrictions.** Only uniform Cartesian coordinates are supported; the
  authors argue that coordinate effects are at truncation-error level for
  resolved calculations, the main loss being 2-D axisymmetric runs. Physics
  is selected at run time, output uses MPI-IO in a custom binary format.
- **Load balance.** Each MeshBlock carries a cost proportional to its cells
  and physics modules, and blocks are distributed to equalize the cost per
  rank while keeping the Z-order (§5.2).

## Numerics

All fluid solvers are higher-order Godunov finite-volume schemes for
$\partial_t\boldsymbol U+\nabla\cdot\boldsymbol F(\boldsymbol W)=\boldsymbol S$
($\boldsymbol U$, $\boldsymbol W$ conserved and primitive variables,
page-local), with the induction equation in Faraday form (§3, Eqs. 1–2):

- **Reconstruction** of primitive variables only: piecewise linear (PLM),
  PPM with the original Colella–Woodward limiters (PPM4), PPM with
  extremum-preserving limiters (PPMX), and WENO-Z after Borges et al.
  (2008); characteristic reconstruction is not implemented.
- **Riemann solvers**: local Lax–Friedrichs (LLF), HLLE, HLLC, HLLD and
  Roe; only LLF and HLLE in general relativity.
- **Time integration**: method of lines with low-storage SSP Runge–Kutta
  of first to fourth order, time step limited by
  $\Delta t\le\mathrm{CFL}\min_i(\Delta x_i/\lambda_{\max,i})$ with,
  "generally", $\mathrm{CFL}\le1/N_{\mathrm{dim}}$ (Eq. 3); IMEX
  Runge–Kutta for stiff sources (Pareschi & Russo, printed "Pareshi",
  and the positivity-preserving scheme of Krapp et al., as cited).
- **Magnetic field**: face-centred, area-averaged, advanced by constrained
  transport with upwinded electric fields (Gardiner & Stone, as cited).
- **Explicit diffusion**: viscosity, thermal conduction and Ohmic
  resistivity by second-order differences, added at every Runge–Kutta
  stage without operator splitting, under a diffusive time-step limit
  (§3.3, Eqs. 6–10); a viscous Gaussian test converges at second order
  (Fig. 5). Super-time-stepping, implicit diffusion and the ambipolar and
  Hall terms exist in Athena++ only.

**First-order flux correction (FOFC).** If, in any Runge–Kutta stage,
density or pressure in a cell would become negative, the fluxes on all
faces of that cell are recomputed with first-order reconstruction and the
LLF solver, before the flux correction at refinement-level boundaries
(§3). The authors motivate it by truncation errors, not round-off, that
become comparable to derived quantities such as the pressure where the
kinetic or magnetic energy dominates; citing Lemaster & Stone (2009), they
state that in supersonic turbulence it acted about once per $10^{10}$ cell
updates, and that in GRMHD it "significantly reduces the need for floors".
With it, the Komissarov cylindrical explosions of special-relativistic MHD
run at field strengths 0.1 and 1 without the flooring, background
modification or artificial viscosity that other codes need, as they state
(§3.5, Fig. 10). The paper calls the LLF solver of the fallback
"diffusive" (§3); see [numerical dissipation](/properties/numerical-dissipation.md).

**Verification** (§3.1–3.2, Figs. 1, 3): linear hydrodynamic waves converge
at fourth order with PPMX and WENO-Z until nonlinear or round-off effects
dominate, at second order with PPM4 and PLM; MHD slow and Alfvén waves
converge at fourth order with third-order Runge–Kutta and PPMX or WENO-Z,
the fast wave "only converges at second order, even in one dimension";
on the Shu–Osher problem with 200 cells WENO-Z with third-order Runge–Kutta
captures the small scales better than PLM with second order.

**Further modules** (§3.4–4): two-fluid ion–neutral MHD coupled by a stiff
drag integrated by IMEX; special- and general-relativistic hydrodynamics
and MHD (Cartesian Kerr–Schild coordinates; angular momentum not conserved
to machine precision, as the authors state); gray relativistic radiation
transport on a geodesic angular grid; Lagrangian Monte Carlo tracers and
charged test particles without feedback on the fluid. The tracers follow
the mass flow better than velocity-interpolated ones but are more
diffusive than the fluid, and more particles do not mitigate this (§4.1).

## Turbulence runs

- **Driven isothermal MHD turbulence** (§3.2, Fig. 4): $10{,}240^3$ cells
  in $256^3$-cell MeshBlocks on 65,536 Frontier GPUs (graphics compute
  dies), WENO-Z with second-order Runge–Kutta and HLLD, rms Mach number 0.5,
  a mean field of Alfvén Mach number 2, solenoidal real-space driving with
  a parabolic spectrum over $1\le2\pi k/L_{\mathrm{box}}\le3$ as printed
  (no FFT, hence no global communication), saturating at
  $\delta B/\bar B\approx3$ over four turnover times. No explicit viscosity
  or resistivity is stated for this run.
- **Supernova blast in a turbulent multiphase interstellar medium** (§3.1,
  Fig. 2): $(32\ \mathrm{pc})^3$ on $2048^3$ cells, third-order Runge–Kutta
  with PPM4, HLLC and FOFC, $2.4\times10^3$ GPU hours.
- **Two-dimensional magnetorotational instability** (§3.3, Fig. 6): zero
  net vertical flux, $8192^2$ cells on eight GPUs, explicit viscosity and
  resistivity, $Re=Rm=10^6$ (the source's $Re_M$), $Pm=1$, many plasmoids
  after ten orbits; the authors state that a 3-D repetition is under way
  to study reconnection and MRI-driven turbulence.
- **Two-fluid driven turbulence** (§3.4, Fig. 8): $1200^3$, IMEX with PPM4,
  sonic Mach about 10, Alfvén Mach about 1, drag coefficient $10^6$; the
  ionization fraction fluctuates little at this strong coupling, while
  Hu et al. (2024, MNRAS 527:3945, as cited; not the ingested
  [Hu et al. (2024)](/sources/hu-2024.md)) find strong fluctuations in
  general.
- **Test particles in MHD turbulence** (§4.2, Fig. 19): $1280^3$,
  $Re=5\times10^4$, $Pm=1$, HLLD, about seven turnover times,
  $3.6\times10^7$ trajectories at two charge-to-mass ratios.

See [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
for these boxes among the bundle's periodic-box runs.

## Performance

Single-device throughput in millions of cell updates per second (Mzcps),
hydrodynamics / MHD, for a linear-wave test with PLM, second-order
Runge–Kutta and HLLE (§5.1, Table 1):

| Device | Hydro | MHD |
|---|---|---|
| Apple M1 Pro (CPU) | 34 | 11 |
| Xeon Gold 6326 (CPU) | 63 | 33 |
| NVIDIA V100 | 298 | 158 |
| NVIDIA A100 | 614 | 298 |
| AMD MI250 | 405 | 190 |
| NVIDIA H100 | 677 | 290 |
| NVIDIA Grace Hopper | 1077 | 565 |

- MHD runs about half as fast as hydrodynamics; on Xeon / A100 / Grace
  Hopper the relativistic solvers range from 16/378/653 (special-relativistic
  hydro) to 6.2/109/211 (radiation GR hydro) (Table 2).
- On an A100, shrinking MeshBlocks from $128^3$ to $64^3$, $32^3$, $16^3$
  lowers 614 Mzcps to 413, 242 and 126 (§5.1).
- On a Grace Hopper the code runs at 8% of the theoretical peak FLOP rate
  (individual kernels up to 22%); a consumer RTX 3070 Ti gives 74.9 (40.2)
  Mzcps for hydro (MHD) in double precision, about four times slower than
  a V100, which the authors explain by bandwidth-bound kernels (§5.1).
- **AMR against a uniform grid** (§5.1, Fig. 20): a 2-D MHD blast on one
  A100 runs at 181 Mzcps on a uniform $4096^2$ grid and at 141 Mzcps with
  a $1024^2$ root and two levels, "roughly 20%" overhead, yet the AMR run
  needs 18% of the wall-clock time (the caption: 5.4 times faster) with
  essentially the same density field.
- **Weak scaling** (§5.2, Figs. 21–22): about 80% efficiency on 65,536
  Frontier GCDs for the non-relativistic solvers (stated in the text, no
  figure); above 97% on 512 Polaris nodes (2048 A100) for GRMHD and
  radiation GRMHD; above 90% on 128 Crusher nodes with a drop beyond eight
  nodes attributed to "networking issues"; with dynamic refinement of a
  diagonal sound wave up to 4096 GCDs, super-linear when the MeshBlock
  size grows from $16^3$ to $128^3$ and nearly perfect at fixed $32^3$,
  with over five million MeshBlocks migrated for load balance.

## Qualifications

- Stone et al. (2026) refer in §4.2 to "the $4096^3$ turbulence simulation
  described in Section 3.2", which §3.2 and the Fig. 4 caption give as
  $10{,}240^3$; the Fig. 6 caption calls the magnetorotational run "a 2D
  (axisymmetric) simulation", while §2 states that 2-D axisymmetric runs
  are not possible with AthenaK; §3.3 swaps the left and right panels of
  Fig. 5 relative to the caption; §3.5 calls the test of Fig. 9 a blast
  wave and the caption a shock tube; the text cites Zhu et al. and Fields
  et al. as 2024, the reference list as 2025; one §3.4 paragraph is
  printed twice.
- The 65,536-GPU efficiency counts "65,536 GPUs (in this case, single
  GCDs)", as §5.2 prints.
- $1-141/181=0.22$ and $1/0.18=5.6$ *(compiler check, not in the
  sources)*: consistent with the printed "roughly 20%" and "5.4×" to
  rounding.

# Citations

- [Stone et al. (2026)](/sources/stone-2026.md) — §1; §2; §3, Eqs. (1)–(3); §3.1, Figs. 1–2; §3.2, Fig. 4; §3.3, Eqs. (6)–(10), Figs. 5–6; §3.4, Figs. 7–8; §3.5, Figs. 9–10; §3.6; §4.1–4.2, Figs. 18–19; §5.1, Tables 1–2, Fig. 20; §5.2, Figs. 21–22; §6.
- [Gan et al. (2022)](/sources/gan-2022.md) — §2 (Athena++ guide-field MHD runs).
