---
type: Software
title: "IDEFIX (performance-portable Godunov code for astrophysical flows)"
description: "Kokkos C++ finite-volume Godunov code for non-relativistic HD and MHD, PLUTO-compatible in its inputs, with primitive reconstruction up to PPM, five Riemann solvers, face-centred constrained transport with an optional vector-potential form, method-of-lines RK integrators, RKL2 super-time-stepping, non-ideal MHD and conservative orbital advection on Cartesian, cylindrical and spherical non-AMR grids, run fully on the device."
status: established
aliases: [IDEFIX, Idefix]
tags: [software, mhd, hydro, constrained-transport, riemann-solver, time-integration, gpu, kokkos, performance-portability, performance, scaling, verification]
timestamp: 2026-10-12T00:00:00Z
---

# IDEFIX

IDEFIX is a C++ finite-volume Godunov code for non-relativistic
hydrodynamics and MHD, written from scratch on the Kokkos
performance-portability library rather than by porting
[PLUTO](/software/pluto.md), so that one source compiles for CPUs and for
NVIDIA and AMD GPUs ([Lesur et al. (2023)](/sources/lesur-2023.md), §1,
§3.1). It keeps PLUTO's user interface but not all of its algorithmic
choices.

## Code

* C++ with Kokkos, bundled as a git submodule and compiled with the code
  (§3.1). Public repository `https://github.com/idefix-code/idefix`,
  forked from a private development repository; CeCILL licence; no version
  number printed (footnote 7). Python readers are bundled; yt support via
  the `yt_idefix` extension (footnote 4).
* **PLUTO compatibility** (§3.2–§3.3): the same input-file format and
  keywords, variable names, several preprocessor macros and VTK output
  conventions as PLUTO; restart dumps are not compatible.
* **I/O** (§3.3): restart dumps and single-precision VTK files of cell
  averages (with $\mathbf B$ reconstructed from the faces), each written to
  one file through MPI-IO, with no external I/O library.
* **Software process** (§6): public and private master branches are
  validated daily on CPU and GPU targets with a test suite that includes
  the paper's tests; merge requests are accepted only if the pipeline
  passes.

## Design for GPUs

From [Lesur et al. (2023)](/sources/lesur-2023.md), §3; see
[porting compressible-flow codes to GPUs](/methods/gpu-porting.md).
* **Two constructs**: `IdefixArrayND`, aliases of `Kokkos::View` after
  K-Athena (Grete et al. 2021), allocated in device memory, and
  `idefix_for` parallel loops with `KOKKOS_LAMBDA`; host mirrors
  `IdefixHostArrayND` serve I/O and complex initial conditions (§3.1).
* **Device-resident execution**: "The algorithm described in §2 is running
  exclusively on the device"; the host does I/O, initial conditions and
  exception handling. Host and device memories are always assumed
  separate; without an accelerator, device code compiles as host code
  "with very little overhead" (§3.1). Data layout, memory pools and unified
  memory are not discussed.
* **MPI** (§3.4): one MPI process per device; packing and unpacking on the
  device; persistent communications; CUDA-aware MPI, so no host–device
  copy with direct device links (NVLink). Ghost cells are exchanged
  **sequentially, dimension by dimension** (x, then y, then z) rather than
  with all 26 neighbours at once as in
  [Athena++](/software/athena-plus-plus.md), because direct timings showed
  the sequential exchange "generally faster, especially on NVidia GPUs".
  The authors state that this exchange would not suit a future AMR version.

## Equations

Dimensionless non-relativistic MHD with a viscous stress, Ohmic, Hall and
ambipolar terms, thermal diffusion and an external gravitational potential
(§2.1, eqs. 1–4), with $P^* = p + \tfrac12\vert\mathbf B\vert^2$,
$E = \rho e + \tfrac12\rho\vert\mathbf v\vert^2 + \tfrac12\vert\mathbf B\vert^2$ and
$\mathbf J = \nabla\times\mathbf B$ (no $4\pi$). The induction equation
(eq. 3) carries, besides $-\mathbf v\times\mathbf B$, an Ohmic term
proportional to $\mathbf J$, a Hall term proportional to
$\mathbf J\times\mathbf B$ and an ambipolar term proportional to
$(\mathbf J\times\mathbf B)\times\mathbf B$.
* **Pressure in the flux** (§2.3): unlike PLUTO, which treats pressure
  gradients as a momentum source term, IDEFIX puts the pressure in the
  momentum flux, solved by the Riemann solver. In curvilinear geometry this
  creates extra pressure source terms absent from PLUTO, so the two codes'
  results "are expected to differ, even if the same algorithm combination
  is chosen".

## Solvers

From [Lesur et al. (2023)](/sources/lesur-2023.md), §2.
* **Reconstruction** (§2.3) of the primitive variables $\rho$, $\mathbf v$,
  $\mathbf B$, $p$, with no characteristic decomposition: flat (first
  order), PLM with the van Leer limiter, LimO3 of Čada & Torrilhon (2009)
  ("up to 4th order accurate") and PPM with an extremum-preserving limiter
  (Colella & Woodward 1984; Colella & Sekora 2008; "4th order accurate on
  regularly spaced grids"). The code remains "at most globally second
  order" (footnote 1). The ghost-cell count follows the reconstruction.
* **Riemann solvers** (§2.3), from most to least diffusive: Rusanov (LF),
  HLL (Einfeldt et al. 1991), HLLC (Toro et al. 1994; replaced by HLLD of
  Miyoshi & Kusano 2005 in MHD) and Roe (Cargo & Gallice 1997), chosen at
  run time. See [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
* **Constrained transport** (§2.4, eqs. 6–8): face-averaged $\mathbf B$
  evolved by Evans & Hawley (1988) CT from edge EMFs
  $\boldsymbol{\mathcal E}$. Optionally the induction equation is evolved
  through an edge-centred vector potential whose time derivative is
  $-\boldsymbol{\mathcal E}$ and whose curl is $\mathbf B$: "mathematically
  equivalent to the original CT algorithm", but it prevents round-off from
  accumulating in $\nabla\cdot\mathbf B$. Its costs are the memory for the
  potential, initial conditions written for the potential, and a possible
  overflow of the potential under a large-scale constant EMF, removed by a
  periodic gauge transformation. See
  [constrained transport](/methods/constrained-transport.md).
* **EMF reconstruction** (§2.4): from the Riemann face fluxes
  (Gardiner & Stone 2005: arithmetic average and the
  $\boldsymbol{\mathcal E}^0$ and $\boldsymbol{\mathcal E}^c$ variants) or
  from 2D Riemann solvers at edges (Londrillo & Del Zanna 2004; 2D HLL and
  HLLD after Mignone & Del Zanna 2021). The default is
  $\boldsymbol{\mathcal E}^c$, "similar to Athena".
* **Parabolic terms** (§2.5): viscosity, thermal diffusion, Ohmic and
  ambipolar diffusion enter as fluxes (conservatively); the Ohmic and
  ambipolar EMFs are centred finite differences added to
  $\boldsymbol{\mathcal E}$.
* **Hall effect** (§2.5, §4.3): the whistler speed is added to the HLL
  Riemann fan for the magnetic-field fluxes only (Lesur et al. 2014;
  Marchand et al. 2019), and the Hall EMF is the arithmetic average of the
  face fluxes; putting Hall in $\boldsymbol{\mathcal E}^c$ "led to numerical
  instabilities". The scheme is "known to be diffusive" but stable; HLL is
  "our only solver compatible with the Hall effect".
* **Time integration** (§2.7, eq. 9, Table 1): method of lines. Each stage
  takes a full Euler step $u + \Delta t\,\mathcal L(u)$ (including the CT
  update) from the previous stage and averages it with the state at the
  start of the cycle: Euler; RK2 with weights $(1/2, 1/2)$; RK3 with
  $(1/4, 3/4)$ and $(2/3, 1/3)$, the TVD Runge–Kutta of Gottlieb & Shu
  (1998). The paper does not call the scheme unsplit in words, but every
  direction is evaluated from the same stage state. See
  [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md).
* **Time step** (§2.7, eq. 10): the inverse of the cell-wise maximum of a
  sum over directions of the maximum signal speed over the cell width plus
  twice the maximum diffusion coefficient over the squared cell width,
  times a Courant number $\nu < 1$; hyperbolic and parabolic limits are
  combined point-wise, generalizing Beckers (1992). There is no dimension
  prefactor; IDEFIX's $\nu$ equals the number of dimensions times PLUTO's
  Courant number, and PLUTO computes global hyperbolic and parabolic steps
  separately, so IDEFIX's step "can be somewhat larger".
* **Super-time-stepping** (§2.8): second-order Runge–Kutta–Legendre (RKL2)
  for viscosity, thermal, ambipolar and Ohmic diffusion (not Hall), RKL1
  for debugging; see [super-time-stepping](/methods/super-time-stepping.md).
* **Orbital advection** (§2.9): FARGO-type advection by a prescribed
  orbital velocity (Masset 2000) in the conservative form of Mignone et
  al. (2012, A&A 545:152), conserving mass, angular momentum and magnetic
  flux; fully parallel in 3D including decomposition along the azimuth;
  the CFL limit uses the velocity residual.
* **Grids** (§2.6): Cartesian, polar/cylindrical and spherical; rectilinear
  grids with piecewise-parameterized stretching; **no AMR**. The azimuthal
  conserved variable is the vertical angular momentum, so angular momentum
  is conserved to machine precision; an "axis" boundary for spherical
  domains follows Zhu & Stone (2018). Shearing-box boundaries exist for HD
  and MHD (§4.3).

## Performance and scaling

From [Lesur et al. (2023)](/sources/lesur-2023.md), §5, Tables 3–4,
Fig. 18. Workload: a 3D Orszag–Tang extension, HLLD, PLM,
$\boldsymbol{\mathcal E}^c$, RK2, **double precision**, to $t = 1.0$. See
[cell-update throughput](/definitions/cell-updates-per-second.md) and
[parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).
* **Single node** (Table 4; $32^3$ cells per MPI process on CPUs, $256^3$
  per GPU):

  | Node | Cell updates/s | Cells per kWh (TDP proxy) |
  |---|---|---|
  | Irene Rome, 2×AMD EPYC 7H12 (128 cores) | 41.3 M | $2.7\times10^{10}$ |
  | Jean Zay CSL, 2×Intel Cascade Lake 6248 (40 cores) | 25.0 M | $3.0\times10^{10}$ |
  | Jean Zay, 4×NVIDIA V100 | 484 M | $11.3\times10^{10}$ |
  | Adastra, 4×AMD MI250X | 1240 M | $18.2\times10^{10}$ |

  Speed-ups against the two-socket Cascade Lake node are 19.3 (V100 node)
  and 49.6 (MI250X node): node against node, with different sub-domain
  sizes per worker and no cost normalization. The abstract's "more than
  $10^8$ cell/s in MHD on a single NVidia V100 GPU" corresponds to the
  484 M per 4-GPU node. The CPU rates (>10 M per 20-core Intel CPU, 20 M per
  64-core AMD CPU) are called "similar to other CPU codes"; Intel VTune
  reports more than 86% of the integration loops auto-vectorized with
  AVX2, on a build not specified.
* **Energy** (§5): a proxy from component TDPs (GPU plus host CPU; storage,
  network and cooling excluded) gives about $3\times10^{10}$ cells per kWh
  on CPUs and up to $1.8\times10^{11}$ on MI250X, "up to 6 times more
  energy efficient". The gain holds at $256^3$ cells per GPU only; at
  $32^3$ per GPU CPU and GPU efficiencies are similar, and GPUs are
  worthwhile "only for subdomains larger than $64^3$".
* **Weak scaling** (Fig. 18; efficiency relative to one node): above 80% to
  1024 Rome nodes (131 072 cores), "very close to Pluto's" (PLUTO 4.4,
  MPI), IDEFIX slightly better beyond 10 000 cores, attributed "probably"
  to device-side packing; above 80% to 512 V100 GPUs (128 nodes) with
  $256^3$ per GPU; above 95% to 1024 MI250X GPUs (256 nodes), "probably
  thanks to the AMD Slingshot interconnect" (as printed). One "GPU" is
  one two-GCD MI250X module: the abstract counts 1024 GPUs on 256 nodes,
  and Table 3 lists four MI250X per node. Performance
  drops substantially below $64^3$ per GPU. Peak about $3\times10^{11}$
  cell updates/s on 1024 GPUs. No strong scaling is shown.
* **Related Kokkos codes** (§6): K-Athena (Cartesian ideal MHD only) is
  "quantitatively similar" in performance and Parthenon's hydro performance
  "similar to Idefix"; no numbers are given.

## Verification

From [Lesur et al. (2023)](/sources/lesur-2023.md), §4. Most tests are
visual; error norms are reported for the linear waves, the ambipolar
C-shock and the Hall shock.
* [Sod shock tube](/benchmarks/sod-shock-tube.md) (§4.1, Fig. 2): Roe,
  PLM, RK2, 500 points, $t = 0.2$, against the analytic solution. The text
  prints a left pressure of 0.1; the figure shows the standard 1.0.
* [Double Mach reflection](/benchmarks/double-mach-reflection.md) (§4.1,
  Fig. 3): $1920\times480$, $t = 0.2$; LimO3 and PPM give a more vigorous
  jet and the onset of Kelvin–Helmholtz rolls.
* [Sedov–Taylor blast wave](/benchmarks/sedov-taylor-blast-wave.md) (§4.1,
  Figs. 4–5): Cartesian $512^3$, and spherical $256\times256\times512$ with
  the blast placed near the polar axis (axis regularization).
* [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md) (§4.2, Fig. 6):
  run with $\gamma = 5/3$, "initial condition identical to Mignone et al.
  (2007)", Roe, PLM, 500 points, against PLUTO 4.3 with 8000 points;
  "excellent agreement" with a "small amplitude oscillation of the
  post-shock velocity that is typical of the primitive variable
  reconstruction".
* [Linear wave convergence](/benchmarks/linear-wave-convergence.md) (§4.2,
  eq. 14, Figs. 7–8): oblique Gardiner–Stone set-up, $2N\times N\times N$,
  amplitude $10^{-6}$. With PLM+RK2, Lax–Friedrichs, HLL, HLLD and Roe all
  converge at second order. With HLLD, PPM+RK3 **stops converging at high
  resolution**, worst for the slow mode, also with HLL and in Athena++
  with primitive reconstruction; LimO3 converges and is recommended. The
  text says LimO3 shows "proper second order convergence", the Fig. 8
  caption "slightly larger than second order".
* Magnetized rotor (§4.2, Fig. 9), Cartesian $512^2$ and polar
  $256\times1024$: iso-contours agree between geometries.
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) (§4.2, Figs.
  10–11): $t = 0.5$; RK3+PPM+Roe "most accurate";
  $\vert\nabla\cdot\mathbf B\vert \ll 10^{-12}$ in all runs.
* Planet–disc interaction with orbital advection (§4.3, Figs. 12–13): 2D
  polar $256\times256$, "excellent" agreement with FARGO3D.
* Ambipolar isothermal C-shock (§4.3, Fig. 14), after Mac Low et al.
  (1995): error "less than 2% when using 2 points per L" (the ambipolar
  length); RKL2 time to solution about 10% of the explicit scheme at high
  resolution.
* Hall-dominated shock (§4.3, Table 2, Fig. 15), after González-Morales et
  al. (2018) with mass-conserving states: relative error falls by 3–4 per
  doubling ("slightly less than second order"), attributed to grid-scale
  whistler diffusion.
* Shearing waves in a shearing box, hydro and MHD (§4.3, Figs. 16–17):
  agreement with the linear solution until the orbital frequency times
  the time reaches about 10, where the hydro vertical velocity diverges at about 17
  points per wavelength, as reported for Athena PPM by Balbus & Hawley
  (2006).

Not tested: field-loop advection; the vector-potential formulation and the
$\nabla\cdot\mathbf B$ round-off growth law are asserted, not shown;
curvilinear convergence; strong scaling.

## Limitations stated by the source

* No AMR; the sequential ghost exchange would not suit an AMR version
  (§2.6, §3.4); Parthenon offers Kokkos AMR (§6).
* At most globally second order whatever the reconstruction (footnote 1).
* PPM stalls on high-resolution linear waves (§4.2).
* GPUs pay off only above about $64^3$ cells per GPU (§5).
* Planned: self-gravity in several geometries, particle-in-cell (§6).

# Citations

1. [Lesur et al. (2023)](/sources/lesur-2023.md), §§1–6, Tables 1–4, Figs. 1–18 (arXiv v1).
