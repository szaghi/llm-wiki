---
type: Software
title: "AthenaK (performance-portable Kokkos version of the Athena++ AMR framework)"
description: "From-scratch Kokkos C++ reimplementation of the Athena++ block-based AMR framework that keeps all field data device-resident, packs every MeshBlock of a device into one MeshBlockPack, runs on CPUs and NVIDIA, AMD and ARM hardware, and carries Newtonian, special- and general-relativistic (M)HD, two-fluid ion–neutral MHD, discrete-angle GR radiation and particles."
status: established
aliases: [AthenaK, Athena-K]
tags: [software, mhd, hydro, amr, constrained-transport, riemann-solver, time-integration, relativity, gpu, kokkos, performance-portability, performance, scaling, verification]
timestamp: 2026-10-12T00:00:00Z
---

# AthenaK

AthenaK is a reimplementation of the [Athena++](/software/athena-plus-plus.md)
block-based AMR framework with the Kokkos C++ performance-portability
library, so that one source runs on CPUs and on NVIDIA, AMD and ARM
hardware ([Stone et al. (2026)](/sources/stone-2026.md), abstract, §1–§2).
It was rewritten from scratch rather than ported, but "very little of the
overall design was changed"; many of its ideas come from the Parthenon
collaboration (§2). The authors call it "a much smaller and simpler
project" than Parthenon and state that "most of the features of Athena++
will not be implemented in AthenaK anytime soon" (§1, §6).

## Code

* C++ on Kokkos (Trott et al. 2022), which abstracts memory spaces,
  execution spaces and execution policies through templates; at build
  time the instructions are "effectively translated into the native
  programming environment of the target architecture" (§1). The Kokkos
  version is not printed.
* Repository `https://github.com/IAS-Astrophysics/athenak`, BSD-3 licence;
  "there are no private development versions" (§2, footnote 3). No code
  version or commit is printed.
* Build with CMake (Kokkos built as an external dependency). The whole
  source is always compiled; physics and algorithm options and problem
  generators are chosen at run time from the input file, unlike the
  configure script of Athena++ (§2).
* Output data are copied device→host, which "enables asynchronous
  outputs"; MPI-IO writes a custom binary format with no external library,
  and Python scripts convert it, e.g. to HDF5 (§2).

## Design for GPUs

All from [Stone et al. (2026)](/sources/stone-2026.md), §2; see
[porting compressible-flow codes to GPUs](/methods/gpu-porting.md).
* **MeshBlockPack.** All MeshBlocks on one device form one aggregate, so
  one kernel launch covers them all; this "reduces the number of kernel
  launches and greatly enhances performance when there are a large number
  of small MeshBlocks on the same device."
* **Device-resident data.** Each physics module stores its variables as
  Kokkos Views with one more dimension than the mesh, the extra index
  being the MeshBlock. Data are "always stored on the device, and is never
  moved to the host except for outputs." Physics operations always run on
  the device.
* **Host-side tree.** The mesh tree is created, stored and refined on the
  host, which also runs the task lists; data needed on both sides are
  Kokkos DualViews.
* **Boundary communication.** Ghost cells are loaded "within parallel
  kernels on the device", as memory copies or into a boundary buffer in
  device memory sent by point-to-point MPI; prolongation and restriction
  are also done "all at once inside parallel kernels". The number of MPI
  messages is proportional to the MeshBlocks in the rank's pack. The
  communication infrastructure "has been largely re-designed" from
  Athena++. Whether the MPI library is GPU-aware is not stated.
* **Templating against register spilling.** "Since the number of registers
  is extremely limited on many GPUs, we have found that the use of
  templating for some algorithmic options (e.g., Riemann solvers) reduces
  register spillage and can greatly improve performance."
* **Cartesian coordinates only.** Reasons given: exascale targets suit
  Cartesian grids; coordinate differences are at the level of truncation
  error; higher-order schemes are simpler; and virtual functions and
  polymorphism "are not supported by the compilers currently available on
  many GPUs". Consequence: 2D axisymmetric calculations are not possible.
* **Task lists** for multistage integrators, operator-split sources and
  each physics module, chained or interleaved; the physics is selected at
  run time by which task lists execute.

## Mesh and AMR

The Athena++ design is kept: MeshBlocks in a binary tree, quadtree or
octree, Z-ordering, flux correction at level boundaries and one global
time step (§1–§2). See
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md). On the
GPU, MeshBlock size matters strongly: on one A100, with the same total
grid, throughput falls from 614 to 413, 242 and 126 Mzone-cycles/s as
$N_{\mathrm b}$ goes from 128 to 64, 32 and 16; "Running small problems on
GPUs is not an effective use of resources" (§5.1).

## Equations and solvers

All from [Stone et al. (2026)](/sources/stone-2026.md), §3.
* **Form.** $\partial_t u + \nabla\cdot\mathbf f(u) = s(u)$, with the flux
  evaluated from the primitive variables (eq. 1), and
  $\partial_t\mathbf B + \nabla\times\boldsymbol{\mathcal E} = 0$ (eq. 2).
* **Reconstruction** of primitive variables only: PLM, PPM4 (Colella &
  Woodward 1984), PPMX (extremum-preserving, McCorquodale et al. 2015) and
  WENOZ (Acker et al. 2016). Characteristic reconstruction "has not yet
  been implemented in AthenaK".
* **Riemann solvers**: LLF, HLLE, HLLC, HLLD, Roe. See
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
* **Time integration**: method of lines with the low-storage SSP
  Runge–Kutta methods of Ketcheson (2010), RK1 to RK4, and IMEX
  Runge–Kutta for stiff sources (§3, §3.4). The step is
  $\Delta t \le \nu\min h/\max_p\vert\lambda^{(p)}\vert$, the minimum taken
  over all cells and all directions (eq. 3); "Generally we use CFL ≤
  1/Ndim", i.e. $\nu \le 1/d$. CTU is not implemented because it "does not
  extend easily to the relativistic equations of motion". See
  [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md).
* **Constrained transport**: face-area-averaged $\mathbf B$ and the Evans &
  Hawley (1988) scheme with the upwind EMFs of Gardiner & Stone (2005,
  2008); "the staggered mesh version of CT is critical for some problems."
  See [constrained transport](/methods/constrained-transport.md).
* **First-order flux correction (FOFC)** after Lemaster & Stone (2009): in
  each Runge–Kutta stage, if $\rho$ or $p$ would become negative in a cell,
  the fluxes on all its faces are recomputed with piecewise-constant
  reconstruction and LLF, before the AMR level-boundary flux correction.
  The authors attribute the loss of positivity to truncation error, not
  round-off; in GRMHD accretion "it significantly reduces the need for
  floors".
* **Equations of state** (§3.1–§3.2): ideal gas $p = (\gamma-1)\rho e$ and
  isothermal ($p$ proportional to $\rho$ with the isothermal sound speed
  squared); MHD total energy
  $E = \frac{p}{\gamma-1} + \frac12\rho\vert\mathbf v\vert^2 + \frac12\vert\mathbf B\vert^2$.
* **Explicit diffusion** (§3.3, eqs. 6–10): viscous, conductive and Ohmic
  fluxes added to $\mathbf f$ in every Runge–Kutta stage (not operator
  split), with a stability limit of the square of the cell width over
  $2d$ times the diffusion coefficient, times a diffusive Courant number
  (eq. 10). Super-time-stepping and implicit solvers "have not been ported
  from Athena++" (see [super-time-stepping](/methods/super-time-stepping.md)).
* **Two-fluid ion–neutral MHD** (§3.4, eq. 11): an MHD ion fluid and a
  hydrodynamic neutral fluid coupled by a drag proportional to the product
  of the two densities and the velocity difference, integrated by the
  second- and third-order IMEX schemes of Pareschi & Russo (2005) or the
  positivity-preserving scheme of Krapp et al. (2024).
* **Special-relativistic (M)HD** (§3.5, eqs. 12–18): conserved $D$, $S_i$
  and $\tau$ (the energy minus $D$, HARM-style); primitives are $\rho$, the
  spatial four-velocity and the internal energy. "In a departure from
  Athena++", conserved-to-primitive inversion uses the scheme of
  [Kastaun, Kalinani & Ciolfi (2021)](/sources/kastaun-2021.md); see
  [primitive-variable recovery](/methods/primitive-variable-recovery.md).
* **General-relativistic (M)HD** (§3.6, eqs. 19–26): Cartesian
  Kerr–Schild or Minkowski coordinates only, with the free index lowered,
  normal-frame velocity primitives and the same inversion plus frame
  transformations. Because the grid is Cartesian, "our algorithm does not
  conserve angular momentum to machine precision as HARM". Inside the
  horizon, floors act within half the sum of the outer and inner horizon
  radii (excision).
* **GR radiation** (§3.7, eqs. 29–30): gray transport of the specific
  intensity (White et al. 2023) on a geodesic angular grid of hexagons and
  pentagons (ten times the square of the grid level plus two angles; 42 at
  level 2); spatial PLM and angular donor-cell upwind fluxes; gray
  Kirchhoff absorption and isotropic elastic scattering in an
  operator-split, locally implicit backward-Euler source step, with the
  fluid four-momentum updated conservatively. This is a discrete-angle
  method, not a moment closure (contrast
  [M1 radiation transport](/methods/m1-radiation-transport.md)).
* **Particles** (§4): per-particle data in 2D Views; inter-rank migration by
  a gather–scatter of the departing list plus non-blocking point-to-point
  sends (a "significant design difference" from Athena++, with fewer
  messages). Lagrangian Monte Carlo tracers (Genel et al. 2013) and charged
  test particles (Boris pusher; GR orbits after Bacchini et al. 2019;
  linear or TSC interpolation).
* **Planned** (§6): the fourth-order integrator of Felker & Stone (2018),
  multigrid self-gravity on AMR (after
  [Tomida & Stone (2023)](/sources/tomida-2023.md)), and non-relativistic
  radiation and neutrino transport.

## Performance and scaling

From [Stone et al. (2026)](/sources/stone-2026.md), §5. The metric is
cell updates per device-second, in millions (Mzone-cycles/s); see
[cell-update throughput](/definitions/cell-updates-per-second.md) and
[parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).
**Precision (single or double) is not stated anywhere in the paper.**
* **Single device** (Table 1). 3D linear wave on a uniform mesh; CPUs run
  one $128^3$ MeshBlock on all cores, GPUs a $512\times256\times256$ grid of
  $128^3$ MeshBlocks. The reconstruction, integrator, Riemann solver and
  Courant number are not stated. Normalization: per device (a CPU socket
  or a GPU), no cost or power normalization.

  | Device | Hydro | MHD |
  |---|---|---|
  | Apple M1 pro (8 cores) | 34 | 11 |
  | Intel Xeon Gold 6326 (32 cores) | 63 | 33 |
  | NVIDIA V100 | 298 | 158 |
  | NVIDIA A100 | 614 | 298 |
  | AMD MI250 | 405 | 190 |
  | NVIDIA H100 | 677 | 290 |
  | NVIDIA Grace Hopper | 1077 | 565 |

  Whether the MI250 entry is one GCD or the two-GCD module is not stated.
  CPU builds use Kokkos's CMake vectorization options rather than the
  hand-placed directives of Athena++, and the authors say CPU optimization
  is likely incomplete. They state that CPU performance is "comparable to
  that reported for Athena++" and GPU performance "comparable to, or better
  than" [Cholla](/software/cholla.md)-MHD and AthenaPK (§5.1).
* **Solver cost** (Table 2, Mzone-cycles/s per device; non-relativistic
  rows on the same linear wave, relativistic rows on a 3D shock tube):

  | Device | Hydro | MHD | SR hydro | SR MHD | GR hydro | GR MHD | GR radiation hydro |
  |---|---|---|---|---|---|---|---|
  | Intel Xeon Gold 6326 | 63 | 33 | 16 | 20 | 13 | 12 | 6.2 |
  | NVIDIA A100 | 614 | 298 | 378 | 178 | 281 | 120 | 109 |
  | NVIDIA Grace Hopper | 1077 | 565 | 653 | 297 | 445 | 227 | 211 |

  MHD costs about 2× hydro (Riemann solver and CT). On the CPU, SR hydro is
  slower than SR MHD, attributed to the inversion root-finder:
  "Likely this algorithm requires further tuning on CPUs". The 120
  Mzone-cycles/s GRMHD figure on an A100 is called "comparable to" H-AMR,
  with no H-AMR number printed. The radiation angular resolution is not
  stated.
* **AMR on one GPU** (Fig. 20): a 2D MHD blast on one A100 runs at 181
  Mzone-cycles/s uniform and 141 with AMR, "roughly 20% overhead"; the AMR
  run takes 18% of the uniform wall time (caption: "5.4× faster"). The
  authors say the overhead is "likely amplified" by 2D. This agrees with
  the ≈20% AMR overhead measured on CPUs for Athena++
  ([Stone et al. (2020)](/sources/stone-2020.md), §3.4.1).
* **Weak scaling, uniform mesh** (§5.2, Fig. 21; efficiency = per-device
  performance over single-device performance): about 70% on 4096 A100 GPUs
  of Perlmutter, after a large drop at small node counts that the authors
  attribute to production network load; 80% "on up to 65536 GPUs (in this
  case, single GCDs)" of MI250X on Frontier. The per-device problem size is
  not printed.
* **Weak scaling with AMR** (§5.2, Fig. 22): 3D sound wave along the grid
  diagonal, $128^3$ root cells per device, one level, continual
  (de)refinement and load balancing, on Frontier to 4096 GCDs. With
  MeshBlocks fixed at $32^3$ above 8 devices, "nearly perfect weak
  scaling", with more than 5 million MeshBlocks migrated for load balance
  at the largest size.
* **Production**: driven isothermal MHD turbulence at $4096^3$ on 4096
  Frontier GPUs with $256^3$ MeshBlocks (§3.2); a $2048^3$ supernova in a
  multiphase interstellar medium in "only $2.4\times10^3$ GPU hours", GPU
  type not stated (§3.1).

## Verification

From [Stone et al. (2026)](/sources/stone-2026.md); single CPU core unless
noted. Only plots are printed: no error values, orders or resolutions are
tabulated.
* [Linear wave convergence](/benchmarks/linear-wave-convergence.md), 1D
  hydro and MHD (§3.1–§3.2, Figs. 1, 3): RK3 with PPMX or WENOZ converges
  at fourth order "until either non-linear effects or round-off error
  becomes important"; PLM and PPM4 at second order. In MHD the slow and
  Alfvén waves reach fourth order with PPMX and WENOZ but "the fast wave
  only converges at second-order even in one-dimension", unexplained.
* Shu–Osher shock tube (§3.1, Fig. 1): 200 cells, WENOZ+RK3 resolves small
  scales "more accurately than PLM"; visual.
* [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md) (§3.2, Fig. 3):
  200 cells, RK2+PLM and RK3+PPM4, "small amplitude ringing near the
  compound wave", which characteristic reconstruction (not implemented)
  would reduce.
* Gaussian viscous diffusion (§3.3, Fig. 5): second-order L1 convergence
  against the analytic solution.
* Two-fluid relaxation and a steady ion–neutral C-shock (§3.4, Fig. 7):
  the Krapp et al. IMEX variant "smoothly converges" where the Pareschi–Russo
  scheme overshoots; the C-shock profile is kept after 10 flow times
  (visual).
* SR MHD shock tube with AMR, set-up "identical to" Athena++ (§3.5, Fig. 9);
  Komissarov (1999) cylindrical explosions with FOFC, run "robustly"
  without floors or artificial viscosity (§3.5, Fig. 10; a variant of the
  relativistic [MHD blast wave](/benchmarks/mhd-blast-wave.md) with an
  ambient pressure of $3\times10^{-5}$).
* GR: Bondi accretion in Cartesian Kerr–Schild, second-order L1
  convergence (§3.6, Fig. 12); Blandford–Znajek monopole with
  magnetization 100 (Fig. 13); an Event Horizon Telescope SANE torus
  overlaid on the Porth et al. (2019) $128^3$ comparison (Fig. 14).
* Radiation: radiation-modified linear wave, better than first order with
  a split first-order source (Fig. 15); a beam in Schwarzschild (Fig. 16).
* Tracers in a Lecoanet et al. Kelvin–Helmholtz run, "more diffusive"
  than a passive scalar (§4.1, Fig. 18).
* 2D [MHD blast wave](/benchmarks/mhd-blast-wave.md) on one A100, uniform
  $4096^2$ against AMR with a $1024^2$ root and two levels: "essentially
  identical" density (§5.1, Fig. 20).

## Limitations stated by the source

* Cartesian coordinates only; no 2D axisymmetric runs; GR angular momentum
  not conserved to machine precision (§2, §3.6).
* No characteristic reconstruction, no CTU, no super-time-stepping or
  implicit diffusion, no self-gravity yet (§3, §3.3, §6).
* CPU optimization likely incomplete; the relativistic inversion needs CPU
  tuning (§5.1).
* Small problems use GPUs inefficiently (§5.1).

# Citations

1. [Stone et al. (2026)](/sources/stone-2026.md), §§1–6, Tables 1–2, Figs. 1–22 (arXiv v1).
2. [Stone et al. (2020)](/sources/stone-2020.md), §3.4.1.
