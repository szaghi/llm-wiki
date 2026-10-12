---
type: Software
title: "Athena++ (block-based AMR framework for astrophysical MHD)"
description: "C++ rewrite of Athena around a physics-agnostic block-based tree AMR mesh with a single global time step and task-list execution, carrying finite-volume upwind-CT MHD (Newtonian, special and general relativistic) with method-of-lines integrators, a multigrid self-gravity solver and a fully conservative self-gravity coupling."
status: established
aliases: [Athena++, athena++, Athena++ AMR framework]
tags: [software, mhd, hydro, amr, constrained-transport, unsplit, riemann-solver, time-integration, self-gravity, multigrid, conservation, performance, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Athena++

Athena++ is a from-scratch C++ rewrite of the C code
[Athena](/software/athena.md). Its central design decision is to abstract the
mesh from the physics: mesh, AMR, boundary conditions and MPI domain
decomposition are written for discrete variables "without specific references
to any particular physics" ([Stone et al. (2020)](/sources/stone-2020.md), §1,
§2). The nonrelativistic MHD module reimplements Athena's finite-volume and
upwind-CT algorithms but replaces CTU with method-of-lines integrators (§3).

## Code

* C++ (strict C++11, migration to C++14 under way); public repository
  `https://github.com/PrincetonUniversity/athena-public-version`, development
  on a private GitHub repository; three-clause BSD licence. Dependencies: a C++
  compiler and Python (2.7+ / 3.4+); optional MPI, OpenMP, FFTW3, HDF5. A
  Python regression suite of more than 60 tests runs under Jenkins and Travis
  CI; gcov/lcov coverage is about 65% of C++ lines. No numbered version is
  printed ([Stone et al. (2020)](/sources/stone-2020.md), §2.6).
* The project's position: open source but not open development;
  reproducibility requires independent implementations (§2.6).
* The later multigrid paper cites the repository
  `https://github.com/PrincetonUniversity/athena`, a BSD licence, the website
  `https://www.athena-astro.app/`, and Athena++ v21.0 as
  doi:10.5281/zenodo.4455880; the multigrid solver needs no external library
  except MPI ([Tomida & Stone (2023)](/sources/tomida-2023.md), §3.2, §5).

## Mesh and AMR

See [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md); all
items from [Stone et al. (2020)](/sources/stone-2020.md), §2.1–§2.2.
* **Blocks.** The mesh is a set of `MeshBlock`s, all with the same cell count,
  stored in a binary tree, quadtree or octree (1D/2D/3D). Refinement ratio
  $r_{\mathrm{ref}}=2$ in all directions at once; $N_{\mathrm b}$ must be even;
  $n_{\mathrm g}$ must be even with AMR; neighbours differ by at most one level
  (2:1 balance). Blocks are ordered along a Z-order curve to assign them to
  processes (§2.1, §2.1.2).
* **Ghost cells.** $n_{\mathrm g}=2$ for second-order MHD on a uniform mesh;
  $n_{\mathrm g}=3$ (hydro) and $4$ (MHD) for spatial orders up to four. Each
  neighbour has its own message buffer: up to 8 (2D) or 26 (3D) neighbours on
  uniform grids, up to 12 or 56 with AMR. Inter-level data go through "coarse
  buffers" holding restricted copies (§2.1.1, §2.1.3).
* **Single coverage.** Each position is covered by "one and only one mesh
  level", which removes level-dependent derived quantities that afflict
  patch-based AMR (§1).
* **Refluxing and EMF correction.** A coarse-face flux is replaced by the
  area-weighted sum of the 4 (3D) or 2 (2D) fine-face fluxes. On a coarse/fine
  face, the coarse EMF times its edge length is replaced by the sum of fine EMF
  times fine edge length (eq. 1); on shared edges, fine EMFs are averaged
  first. Even without refinement, EMFs on edges shared by `MeshBlock`s are
  replaced by their arithmetic average, because round-off, nondeterministic MPI
  ordering or non-ANSI optimizations otherwise create divergence errors that
  CT never removes (§2.1.4).
* **Restriction** is volume-weighted for cell-centred (conserved) variables
  and area-weighted for face-centred fields (eqs. 2–3).
* **Prolongation** of cell-centred data is multidimensional linear
  reconstruction limited with minmod, less aggressive than the hydro limiter
  because sharper limiters produce unphysical structures at level interfaces
  (eqs. 4–5). Ghost-zone prolongation uses primitive variables; new blocks are
  filled from conserved variables with a pressure floor, which breaks energy
  but not mass or momentum conservation. Face fields use the Tóth & Roe (2002)
  divergence-preserving prolongation, extended to nonuniform and curvilinear
  meshes; existing fine faces are not overwritten (§2.1.5).
* **Load balancing** by a per-block cost (user-set or measured), redistributed
  periodically and on refinement; at least one block per process is needed and
  the block order cannot be shuffled (§2.1.6).
* **No subcycling.** A single global $\Delta t$ for all levels. Reasons given:
  the maximum signal speed is often largest on the root level; temporal
  interpolation adds error, especially with self-gravity; complexity hurts
  optimization and load balance; the saving is only about half the number of
  levels when each level holds the same number of cells. The paper concedes lower efficiency for more
  than 10 levels covering at most 1% of the volume (§2.1.7, §2.2). The
  multigrid paper adds that a global step suits non-local physics such as
  gravity and implicit radiation ([Tomida & Stone (2023)](/sources/tomida-2023.md), §3.1, §5).
* **Taxonomy** (§2.2): cell-by-cell (RAMSES, ART); patch-based
  Berger–Oliger/Berger–Colella (Enzo, PLUTO, AMRVAC; Chombo, AMReX);
  block-based (FLASH/PARAMESH, NIRVANA, DISPATCH, Athena++). Smaller blocks
  give more flexibility at higher ghost-cell overhead (§2.1.2).
* **Coordinates** (§2.3): logically rectangular grids with uniform,
  logarithmic or user-defined spacing; Cartesian, cylindrical and
  spherical-polar (Newtonian and special relativistic); in general relativity
  Minkowski, Schwarzschild, spherical Kerr–Schild or a user stationary metric.
  A "polar" boundary copies ghosts across the pole and averages EMFs on radial
  edges touching it.

## Execution model and parallelism

* **TaskList** (§2.5): each task has a unique bit identifier, a bit-field of
  dependencies and a function pointer; each `MeshBlock` tracks its task state;
  nonblocking MPI receives are posted before the list runs. The design hides
  communication, composes physics at run time, and allows different task lists
  on different blocks (Figs. 9–10).
* **Hybrid MPI+OpenMP** (§2.4): coarse-grained, one thread per `MeshBlock`,
  requiring `MPI_THREAD_MULTIPLE`; fine-grained loop-level OpenMP was found
  inefficient. GPU: the Kokkos port K-Athena, with a Kokkos version of the
  whole framework under development (§1, §3.6.2, §6).

## Equations

Nonideal MHD in conservative form with magnetic permeability 1 (§3.1,
eqs. 6–9): the ideal-MHD system for $\rho$, $\rho\mathbf v$, $E$, $\mathbf B$
with total pressure $P^*$, plus a viscous stress, Ohmic resistivity, ambipolar
diffusion (strong coupling) and thermal conduction, with
$\mathbf J = \nabla\times\mathbf B$. Equation of state: any analytic or
tabulated pressure as a function of density and internal energy. Recorded as printed: in the viscous stress (eq. 7) the second
velocity-gradient term repeats the differentiated index where the transposed
gradient is presumably meant, and the heat flux (eq. 9) enters with a positive sign.

## Solvers

* **Discretization**: finite volume, cell averages at volume centres;
  induction by the upwind CT of Gardiner & Stone with face-area-averaged
  $\mathbf B$; the EMF construction is not restated (§3.1). See
  [constrained transport](/methods/constrained-transport.md).
* **Reconstruction** (§3.2.1): donor cell, PLM or PPM, on primitive or
  characteristic variables (characteristic only for the nonrelativistic ideal
  EOS). PLM uses the van Leer (1974) limiter on uniform Cartesian-like
  directions and Mignone's (2014) modified limiter on nonuniform or curvilinear
  ones; PPM uses the Colella–Sekora / McCorquodale et al. smooth-extremum
  limiter on Cartesian meshes and Mignone's modification of the
  Colella–Woodward limiter on curvilinear grids. On a uniform grid the PPM
  face value is 7/12 of the sum of the two adjacent cell values minus 1/12 of
  the sum of the next two (eq. 10). The default CT is second order, so overall accuracy stays
  $O(h^2)$ even with PPM.
* **Riemann solvers** (§3.2.2): HLLE, HLLC, HLLD and Roe; no exact solver;
  HLLE/HLLC/HLLD extended to a general EOS; Athena's H-correction is not yet
  implemented (§3.4.2). See
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
* **Integrators** (§3.2.3): method of lines in the Ketcheson (2010)
  low-storage 2S form; CTU is not implemented because characteristic
  projection is too complex for relativity. Available: RK1, **VL2**
  (default; the predictor must use first-order donor-cell fluxes), RK2 =
  SSPRK(2,2), RK3 = SSPRK(3,3); the framework admits RK4()4[2S] and 3S*
  methods. Stability: RK2 and RK3 have SSP coefficient 1, so $\nu=1$, and
  in practice $\nu=1$ works with PLM and PPM for most problems; RK1 is stable
  only with donor-cell fluxes; VL2 allows $\nu=1$ in 1D and $\nu=1/2$ in 2D
  and 3D, and is positive-definite for $\nu\le1/3$ with first-order fluxes in
  both steps. Recommended pairs: RK1 + donor cell (testing), VL2 or RK2 with
  PLM or PPM, RK3 + PPM. See
  [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md).
* **Curvilinear geometric sources** (§3.2.4, eqs. 16–19): the cylindrical and
  spherical momentum source terms are built from face stresses of the Riemann
  fluxes so that they are algebraically identical to the conservative
  angular-momentum update, giving machine-precision angular-momentum
  conservation.
* **Diffusion** (§3.2.5): explicit, added as flux divergences inside each
  integrator stage, or operator-split RKL1/RKL2 super-time-stepping; a
  super step replaces a number of explicit diffusive steps that grows as the
  square of its stage count, so the speed-up is proportional to the stage count.
* **Other physics** (§3.2.6, §5): passive scalars; operator-split reactions;
  shearing box and orbital advection; FFT self-gravity (public); implicit
  radiation transport of Jiang et al. (2014a); flux-limited diffusion and
  variable Eddington tensor planned.
* **Relativistic MHD** (§4): special and general relativity (White et al.
  2016). Primitives are density, gas pressure, the normal-frame spatial
  four-velocity (guaranteeing subluminal states) and the lab-frame field; the
  same CT discretization with metric-weighted lengths, areas and volumes;
  reconstruction on primitives only. With the free index lowered, the source
  vanishes for ignorable coordinates, so energy and $z$-angular momentum are
  conserved to machine precision. Inversion uses the Newman & Hamlin (2014)
  one-dimensional root-find; floors act on density and gas pressure, never on
  the field. Relativistic solvers: HLLE, HLLC (hydro) and HLLD (MHD), usable in
  GR through local frame transformations (§4.2.2).

## Self-gravity

* **Multigrid** ([Tomida & Stone (2023)](/sources/tomida-2023.md); see
  [Poisson solvers for self-gravity on adaptive meshes](/methods/multigrid-self-gravity.md)).
  Cell-centred, second-order geometric multigrid for $\nabla^2\Phi=4\pi G\rho$:
  7-point Laplacian, volume-weighted restriction, trilinear prolongation,
  red–black Gauss–Seidel with $\omega_{\mathrm{SOR}}=1.15$, V(1,1) cycles, in
  multigrid-iteration or full-multigrid mode (§2.3). On AMR the Full
  Approximation Scheme solves the whole hierarchy in one globally consistent
  V-cycle (§2.3.5, §3.3.1); fine/coarse boundaries use a "mass-conservation"
  ghost formula after Feng et al. (2018), so no flux-correction step is needed
  (§3.3.2). Each `MeshBlock` must be logically cubic with $N_{\mathrm b}$ a power of two,
  more restrictive than the AMR itself; $n_{\mathrm g}=1$ (§3.2.1). Below the
  `MeshBlock` levels, data are gathered to every rank with `MPI_Allgather` and
  the coarse "RootGrid" levels are solved redundantly; these and the "Octet"
  levels are not parallelized (§3.2.5, §3.4). Coupling to hydro (eq. 22) uses
  face accelerations from potential differences and the Riemann mass fluxes;
  it is curl-free, but neither momentum nor energy is conserved to round-off,
  because the potential carries a residual and the conservative energy scheme
  is not used (§3.2.3).
* **Fully conservative coupling** ([Mullen, Hanawa & Gammie (2021)](/sources/mullen-2021.md);
  see [conservative self-gravity](/methods/conservative-self-gravity.md)). On
  static uniform Cartesian meshes, the momentum and energy sources are
  discretized as exact divergences of the gravitational stress tensor
  $\mathsf T_{\mathbf g}$ and of a gravitational energy flux, so total momentum
  and energy are conserved to round-off with periodic boundaries (§2.2–2.3).
  The energy source pairs the Riemann mass flux with the time-averaged face
  gravity (eqs. 57–59). The scheme is given for VL2 (§3.1), RK2 and RK3
  (App. B), needs two Poisson solves per step with second-order integrators,
  and is formally second order. The paper finds that the stress tensor of
  Athena++ v19.0 does not give a curl-free gravity and causes anomalous
  accelerations near massive bodies with light atmospheres; its corrected
  $\mathsf T_{\mathbf g}$ differs only in the diagonal components (§2.3.1,
  §3.3). Round-off conservation needs a round-off-accurate Poisson solution
  (FFT); multigrid residuals break it (§3.2). Not implemented with AMR (§6).

## Performance and scaling

From [Stone et al. (2020)](/sources/stone-2020.md), §3.4.1, §3.6:
* Single Skylake 6148 core, 3D MHD, HLLD + PLM, VL2, $64^3$ block: 2.924
  million zone-cycles per second; PPM halves the throughput (Table 2). The
  paper claims the highest per-core performance among the public versions of
  FLASH, PLUTO and Enzo, "in some cases by as much as a factor of 10". About
  85% of the MHD code is vectorized. Full-node per-core throughput is about 2×
  lower than single-core, which the paper attributes to memory bandwidth and
  cache use (Table 3). K-Athena on an NVIDIA Volta is about 5× one 20-core
  Skylake.
* Weak scaling on a Cray XC50, $64^3$ per block, one block per process, up to
  250 nodes ($10^4$ cores): efficiency 8→250 nodes about 97% (hydro, HLLC) and
  95% (MHD, HLLD) (Fig. 33). On Oakforest-PACS (Xeon Phi KNL), 2048 nodes =
  524,288 threads: 86% (hydro) and 84% (MHD) relative to 8 nodes (Fig. 34).
* Strong scaling with AMR (Fig. 35): with $16^3$ blocks the AMR throughput is
  about half the uniform one but the time to solution is about 5× shorter.
* Block-size cost model (§3.6.5, eq. 30): cost per cell = compute + a
  communication term $\propto 1/N_{\mathrm b}$ + a per-block overhead
  $\propto 1/N_{\mathrm b}^3$. On a $128^3$ blast, cost rises about 10× from
  $128^3$ to $4^3$ blocks; recommendation $8^3$–$16^3$ for AMR, the largest
  possible for uniform grids.
* AMR overhead on a linear-wave run: 132.5 → 106.0 Mzone-cycles/s, about 20%
  (§3.4.1).
* An independent comparison on a 14-core Intel Xeon E5-2680 (double
  precision, VL + PLM + Roe) measured $7.7\times10^6$ cell updates per second
  for Athena++, 1.5× the CPU version of GAMER; it also quotes $5\times10^7$
  (single) and $3\times10^7$ (double precision) cells per second for Athena++
  on Intel KNL as a private communication
  ([Zhang, Schive & Chiueh (2018)](/sources/zhang-2018.md), §5.2).
* Multigrid ([Tomida & Stone (2023)](/sources/tomida-2023.md), §4): on a
  uniform grid one full-multigrid sweep costs about 15% of an MHD step with
  $64^3$ blocks (FMG + 10 V-cycles about 70%), and multigrid outperforms the
  FFT solver at scale. Weak-scaling efficiency from 2 to 200 nodes for one FMG
  sweep is 89.6%, 73.2% and 45.7% for $128^3$, $64^3$ and $32^3$ blocks. With
  AMR, at 2,304 processes multigrid is about 2–6× slower and less scalable
  than MHD on the same blocks, attributed to the unparallelized coarse levels.
  In a magnetized protostellar-collapse demonstration gravity takes about
  85–90% of the run time (§4.4).

## Verification

From [Stone et al. (2020)](/sources/stone-2020.md) unless stated:
* [Linear wave convergence](/benchmarks/linear-wave-convergence.md): strict
  second order whenever VL2 or PLM is used; RK3 + PPM errors at least 10×
  lower, near third order for some families (§3.3.1, Fig. 11); second order
  globally with AMR (§3.4.1, Fig. 19). Nonideal fast-wave decay converges to
  the analytic rates (§3.3.2).
* [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md): primitive
  reconstruction gives significant oscillations behind the right-moving fast
  rarefaction, so characteristic reconstruction is needed (§3.3.3, Fig. 15).
* [Double Mach reflection](/benchmarks/double-mach-reflection.md) with AMR:
  indistinguishable from uniform, CPU time 279 → 63.2 s with $6^2$ blocks
  (§3.4.2, Fig. 20).
* [Sedov–Taylor blast wave](/benchmarks/sedov-taylor-blast-wave.md), hydro and
  MHD, 3D, with AMR: visually identical to uniform $512^3$, excellent agreement
  with the analytic solution (§3.4.4); also in spherical-polar coordinates
  with AMR (§3.5.3).
* [Field-loop advection](/benchmarks/field-loop-advection.md) through the pole
  of a spherical-polar grid: structure well preserved through the singularity
  (§3.5.2, Fig. 29).
* [Jeans wave](/benchmarks/jeans-wave.md): about second order with the
  multigrid solver ([Tomida & Stone (2023)](/sources/tomida-2023.md), §4.3);
  strict second order for all six VL2/RK2/RK3 × PLM/PPM combinations with the
  conservative coupling, and total energy conserved to round-off in the
  unstable case ([Mullen, Hanawa & Gammie (2021)](/sources/mullen-2021.md),
  §4.2).
* Also: Shu–Osher, ambipolar C-shock, Liska–Wendroff implosion (symmetric to
  machine precision, given direction-unbiased stencils and value-safe
  floating point), Lecoanet et al. Kelvin–Helmholtz versus Dedalus,
  Kelvin–Helmholtz with AMR, curvilinear advection, relativistic shock tube,
  Kelvin–Helmholtz and magnetized blast with AMR, and a Fishbone–Moncrief torus
  (§3.3–§4.3).

## Limitations stated by the sources

* AMR damps sound waves in coarse regions, so it cannot be used where such
  waves matter ([Stone et al. (2020)](/sources/stone-2020.md), §3.4.3); in the
  relativistic Kelvin–Helmholtz run many small-scale features are artefacts of
  fine/coarse boundaries (§4.3.2).
* The multigrid solver's convergence factor degrades from about 0.2 to 0.5
  with AMR, attributed to errors at level boundaries
  ([Tomida & Stone (2023)](/sources/tomida-2023.md), §4.2.1).
* The fully conservative gravity coupling is not available with AMR
  ([Mullen, Hanawa & Gammie (2021)](/sources/mullen-2021.md), §6).

## Later uses (batch 2)

### General equations of state

[Coleman (2020)](/sources/coleman-2020.md) documents how the
nonrelativistic (M)HD of the public Athena++ was extended to an arbitrary
equation of state; see
[general equations of state in Godunov codes](/methods/general-equation-of-state.md).
* **Interface** (§3.1, eqs. 13–15). The EOS supplies three functions:
  $p(\rho,\rho e)$, $\rho e(\rho,p)$ and $c_s^2(\rho,p)$, the last being the
  derivative of $p$ with respect to $\rho$ at constant entropy. Athena++
  evolves $E$ and takes $p$ as the primitive, so $\rho e$ is obtained by
  subtracting the kinetic and magnetic parts of $E$ before $p(\rho,\rho e)$
  is called. The sound speed feeds the CFL condition and the Riemann
  solvers. The EOS must have positive derivatives of $p$ with respect to
  $\rho$ at fixed internal energy and with respect to internal energy at
  fixed $\rho$ (eqs. 4–5), conditions the paper calls "sufficient, but not
  necessary" for a unique Riemann solution, citing Chen et al. (2019).
  Recorded as printed: the text says the first two functions convert
  primitives to conservatives "and the inverse, respectively", the reverse
  of their roles.
* **Recipe** (§3.1, eqs. 16–18). Every ideal-gas relation
  ($p=(\gamma-1)\rho e$, $\rho e = p/(\gamma-1)$, $c_s^2=\gamma p/\rho$) was
  replaced by the corresponding general function: "we found all instances
  of $\gamma$ and replaced them", with one caveat, the HLLC wave-speed
  estimate (below). Characteristic reconstruction "does not support general
  EOS" (footnote 3), which agrees with the restriction of characteristic
  reconstruction to the ideal EOS stated above. Every run of the paper uses
  PLM on primitives with VL2.
* **Tabular EOS** (§3.2, eqs. 19–28). A utility tabulates the logarithms of
  $p/(\rho e)$, $\rho e/p$ and the first adiabatic index on a grid regular in
  $\log\rho$ and in the logarithm of the internal energy or pressure scaled
  by a power of $\rho$, interpolates bilinearly, which "guarantees the
  preservation of monotonicity", and extrapolates linearly off the table
  (floors on $p$, $\rho e$ and $\rho$ are recommended). For an ideal gas the
  tabulated quantities are constants, so a $2\times2$ table reproduces the
  ideal EOS "exactly (to machine precision)"; asserted, no data shown.
* **Analytic EOSs in the tests** (§4, §4.4): a Saha-ionization hydrogen EOS
  evaluated through a Brent–Dekker temperature root-find to one part in
  $10^{12}$, preferred to a table so that table resolution does not
  contaminate convergence, and the Helmholtz EOS evaluated as a function of
  $(\rho,T)$ with a bisection/secant/Newton–Raphson temperature solve.
* **Riemann solvers** (§3.3, §5.1.4, §5.2, App. A). HLLC's extremal wave
  speeds were previously estimated from a Roe-average state, which needs a
  fourth EOS function; the default is now a generalized PVRS estimate that
  needs only the three functions and markedly improves the asymmetric
  double-shock tests without degrading ideal-gas results. HLLD keeps the
  Miyoshi & Kusano (2005) estimate. HLLE did not converge on the two
  double-shock tests with any estimator tried, while running on the other
  hydrogen-EOS tests with errors "a few tens of per cent worse than HLLC"
  (§5.1.4, §6). This qualifies the §3.2.2 statement that HLLE is extended
  to a general EOS: it runs, but fails to converge on general-EOS double
  shocks (see [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)).
* **Scope** (§1, §4.4). Nonrelativistic only: the general EOS does not
  apply to the relativistic modules. The EOS functions take no passive
  scalars, so composition-dependent tests were not attempted. The
  hydrogen-EOS tests use "publicly available version 19.0 of Athena++"
  (§4.1); the version for the other tests is not stated.
* **Verification** (§4–§5; PLM, VL2, CFL number 0.4, $N=64$ to 2048 cells):
  six hydrodynamic Riemann problems and one MHD Riemann problem (the Ryu &
  Jones 2a states, all seven waves discontinuities) with the hydrogen EOS,
  HD sound and MHD fast [linear waves](/benchmarks/linear-wave-convergence.md)
  with the hydrogen EOS, and two Helmholtz-EOS Riemann problems, among them a
  "Sod-like" one (see [Sod shock tube](/benchmarks/sod-shock-tube.md)). The
  paper calls the Riemann-problem convergence "close to linear" and the
  linear-wave convergence "near quadratic"; it prints errors, not orders.
  On the two hydrogen double-shock problems convergence stalls: the density
  L1 error is 3.64848e-08 at $N=512$ and 3.0004e-08 at $N=2048$ (test 3,
  Table 8). The paper offers, without demonstration, that cells straddling
  the shocks pass cell-averaged states to the EOS where the adiabatic index
  is non-monotonic, a limitation of finite-volume methods without front
  tracking (§5.1.2, §6). The Serna & Marquina (2014) van der Waals tests are
  reproduced by visual comparison only. Recorded as printed: the text calls
  the Helmholtz tests "tests 8 and 9" while the tables and figures number
  them 10 and 11, and eq. 3 omits $v_x$ from the energy flux.
* **Priority claim** (§1, asserted): Athena++ is called "the first
  publicly-available open-source MHD code whose general EOS capabilities
  have been explicitly verified with a suite of (M)HD tests utilizing a
  non-trivial EOS"; CASTRO is said to have run similar tests but to be
  hydro-only.

### The relativistic inversion

The Newman & Hamlin (2014) inversion that Athena++ uses (§4 above) is one
of five schemes compared stand-alone by
[Siegel et al. (2018)](/sources/siegel-2018.md); see
[primitive-variable recovery](/methods/primitive-variable-recovery.md).
In their Lorentz-factor–magnetization sweep it recovers the largest
fraction of points for every EOS tested (79.1 %, 77.1 % and 77.4 % for the
ideal gas, LS220 and Helmholtz, Table 2), and they recommend it for analytic
EOSs; on the tabulated LS220 EOS it costs 331 EOS calls on average against
11.3 for their 3D Newton–Raphson scheme (Table 1), because each iteration
needs an enthalpy-to-temperature inversion (§4.2, §5).
[Kastaun, Kalinani & Ciolfi (2021)](/sources/kastaun-2021.md) classify it as
iterating on the pressure with an EOS of the form $p(\rho,h_{\mathrm{rel}})$, without EOS
derivatives, with a bounded step count and no initial guess, and, citing
Siegel et al., as the only existing scheme that consistently needs fewer
than about 10 steps also at relativistic velocities (§IV D, Table I). The
two counts measure different things: EOS calls per inversion against
root-finder steps.

# Citations

1. [Stone et al. (2020)](/sources/stone-2020.md), §§1–4, §§3.6.1–3.6.5 (journal version).
2. [Tomida & Stone (2023)](/sources/tomida-2023.md), §§2–5 (arXiv v1).
3. [Mullen, Hanawa & Gammie (2021)](/sources/mullen-2021.md), §§2–6, App. B (arXiv v1).
4. [Zhang, Schive & Chiueh (2018)](/sources/zhang-2018.md), §5.2 (arXiv v4).
5. [Coleman (2020)](/sources/coleman-2020.md), §§1–6, App. A (arXiv v3).
6. [Siegel et al. (2018)](/sources/siegel-2018.md), §§4.2, 5, Tables 1–2 (arXiv v2).
7. [Kastaun, Kalinani & Ciolfi (2021)](/sources/kastaun-2021.md), §IV D, Table I (arXiv v2).
