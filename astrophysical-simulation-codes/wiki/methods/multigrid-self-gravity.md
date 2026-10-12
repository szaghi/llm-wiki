---
type: Method
title: "Poisson solvers for self-gravity on adaptive meshes"
description: "Solving the gravitational Poisson equation on AMR hierarchies: Enzo's root FFT plus grid-by-grid multigrid with interpolated Dirichlet data, Castro's level and composite multigrid solves with a post-subcycling correction solve, and Athena++'s globally consistent FAS multigrid V-cycle over the whole octree with conservative level-boundary ghost cells."
status: established
aliases: [multigrid self-gravity, AMR Poisson solver, FAS multigrid, full multigrid, FMG, level-by-level gravity solve, composite Poisson solve]
tags: [self-gravity, multigrid, amr, performance, conservation]
timestamp: 2026-10-12T00:00:00Z
---

# Poisson solvers for self-gravity on adaptive meshes

Self-gravity requires the potential $\Phi$ from
$$\nabla^2\Phi = 4\pi G\rho,\qquad \mathbf g = -\nabla\Phi,$$
at every hydrodynamic step. On a uniform grid the cell-centred 7-point
discretization reads
$$\sum_{\mathrm{nb}}\Phi - 6\,\Phi_{i,j,k} = 4\pi G\rho_{i,j,k}\,h^2,$$
the sum running over the six face neighbours
([Tomida & Stone (2023)](/sources/tomida-2023.md), §2.1, eq. 3; Enzo
uses the same 7-point second-order stencil on subgrids,
[Bryan et al. (2014)](/sources/bryan-2014.md), §5.1; Castro uses
"standard finite differences",
[Almgren et al. (2010)](/sources/almgren-2010.md), §4). In comoving
coordinates Enzo solves $\nabla^2\Phi = (4\pi G/a)$ times the total
density minus its mean ([Bryan et al. (2014)](/sources/bryan-2014.md),
§2.1, eq. 8). On an AMR hierarchy the question is how the levels are
coupled. The three codes ingested here take three different answers.

## Geometric multigrid building blocks

[Tomida & Stone (2023)](/sources/tomida-2023.md), §2, give the most
complete statement; the parts shared with Castro are noted.
* **Smoother.** Red–black Gauss–Seidel with over-relaxation, red cells
  ($i+j+k$ even) first:
  $$\Phi_{i,j,k}\leftarrow\Phi_{i,j,k} + \omega_{\mathrm{SOR}}\left[\frac16\Big(\sum_{\mathrm{nb}}\Phi - 6\Phi_{i,j,k}\Big) - \frac{4\pi G\rho_{i,j,k}h^2}{6}\right],$$
  with $\omega_{\mathrm{SOR}} = 1.15$, chosen to damp high frequencies,
  not the SOR-optimal value (§§2.2, 2.3.2, eqs. 14–16). Castro also uses
  red–black Gauss–Seidel in geometric multigrid V-cycles
  ([Almgren et al. (2010)](/sources/almgren-2010.md), §4).
* **Transfer operators.** Restriction is the volume-weighted average over
  the $2\times2\times2$ children; prolongation is trilinear, with 1D
  weights $\tfrac14, \tfrac34$ from the two nearest coarse cells. The
  full-multigrid (FMG) prolongation uses the 3-point weights
  $\tfrac{5}{32}, \tfrac{30}{32}, -\tfrac{3}{32}$, which the paper calls
  "third-order tricubic"; they are quadratic Lagrange weights with
  third-order accuracy (§2.3.1, eqs. 17–18; see the Source page).
* **Cycles.** Only the V-cycle is implemented, typically V(1,1). FMG
  restricts the source to all levels, solves the coarsest and then
  alternates FMG prolongation and one V-cycle per level; it needs no
  initial guess and costs about two V-cycles. Multigrid iteration (MGI)
  starts from a guess. On the coarsest level a single cell is solved
  exactly; otherwise red–black sweeps are repeated (§§2.3.2–2.3.4,
  4.1.1, Algorithms 1–2).
* **Full Approximation Scheme.** The defect-correction scheme is
  ill-defined across AMR levels, because defects at different resolutions
  cannot be combined. FAS (Brandt 1977) restricts the potential as well
  and solves the full equation on every level; it is equivalent to the
  correction scheme for linear problems on uniform grids, and Athena++
  always uses it with refinement (§2.3.5, Algorithm 3).
* **Stopping test.** The volume-weighted RMS defect on the finest level
  against a user threshold, or a fixed iteration count (§2.3.7,
  eqs. 20–21).

## Coupling the levels

### Enzo: root FFT, then grid by grid

[Bryan et al. (2014)](/sources/bryan-2014.md), §5.1:
* The root grid is solved by FFT, periodic (with the continuous or the
  finite-difference Green's function) or isolated by the James (1977)
  method.
* Each subgrid is solved separately by multigrid, with Dirichlet data
  interpolated (trilinear by default, or spline) from its parent and a
  buffer of 3 parent zones (6 fine zones for $r_{\mathrm{ref}} = 2$);
  sibling boundaries can be iterated (4 iterations by default). The
  gravity solver needs 6 ghost zones (§3).
* This is not a coherent level-wide solve, an inconsistency the paper
  admits; a HYPRE-based AMR gravity solver is announced as future work
  (§§5.1, 14). The effective force resolution is about twice the cell
  size; in a point-mass test the force rolls over at about 1.6 fine cell
  widths, consistent with CIC deposition (§11.2.6).
* The subgrid multigrid (`SolveForPotential`) is one of the limiters of
  AMR strong scaling (§12.2.3).

### Castro: level solves, composite solves and a correction solve

[Almgren et al. (2010)](/sources/almgren-2010.md), §§4, 6.2.2–6.2.3:
* Boundary data are inhomogeneous Dirichlet values from the
  coarsest-level monopole approximation. Constant, monopole and full
  Poisson gravity are options.
* A **composite** solve over all levels runs at the start and after each
  regrid. Within the subcycled step each level does its own **level**
  solve at the start and end of its step, adding a lagged correction equal
  to the difference between the composite and the level potentials
  (after Miniati & Colella 2007).
* After the fine levels have subcycled to the coarse time, a two-level
  composite **correction solve** is driven by the density change from
  refluxing and by a flux register of the mismatch between coarse and
  fine normal potential gradients (eqs. 36–38). The resulting correction
  of $\mathbf g$ gives momentum and energy "sync sources", applied with a
  factor $\frac12\Delta t$ on both levels; the register propagates to
  the next coarser level (eqs. 39–40). Its tolerance equals the final
  residual of the level solve.
* Weak scaling: Poisson gravity scales "relatively good ... up to only
  13,824 processors", against 64,000 without gravity or with the
  monopole; hybrid MPI+OpenMP gives "at least a factor of 3" lower
  linear-solver time on a $768^3$ case at large processor counts (§7.4).

### Athena++: one globally consistent V-cycle

[Tomida & Stone (2023)](/sources/tomida-2023.md), §3:
* The solver lives on the hydro MeshBlocks of the
  [block-based octree](/methods/adaptive-mesh-refinement.md), with
  $n_{\mathrm g} = 1$. Each MeshBlock is coarsened to one cell inside its
  own `Multigrid` object; refined blocks then become cells of "Octet"
  objects ($2^3$ cells plus ghosts), which are smoothed and restricted,
  and the result passes to "RootGrid" levels below the root
  (§§3.2.1, 3.3.1, Fig. 3). This order keeps the number of `Multigrid`
  objects constant down to the Octet levels, which keeps load balance; it
  differs from Trottenberg et al. (2001), which removes locally refined
  grids first.
* The whole hierarchy is solved in one FAS V-cycle, not level by level.
* **Level boundaries** use a "mass-conservation" ghost formula (the Π
  stencil of Feng et al. 2018): the coarse face gradient must equal the
  area average of the four fine face gradients across the interface
  (eq. 23), which makes the truncation error of the gradient
  divergence-free with no "fake" mass. The first fine layer is
  area-averaged and sent to the coarse side; the coarse value is
  interpolated to four fine-aligned points with transverse gradients
  (eqs. 24–25); the fine ghost is $\tfrac13$ of the adjacent fine value
  plus $\tfrac23$ of the interpolated coarse value (eq. 26), and the coarse
  ghost is $\tfrac43$ of the area-averaged fine value minus $\tfrac13$ of
  the adjacent coarse value (eq. 27). One set of independent
  communications suffices and **no flux-correction step** is needed;
  SFUMATO (Matsumoto 2007) instead uses flux correction (§3.3.2). Eq. 24
  as printed carries a possible factor-2 inconsistency (see the Source
  page). Ghosts are refreshed after every sweep, and the red–black pattern
  cannot be kept across level boundaries. Before prolongation, ghosts are
  filled by restriction and trilinear prolongation instead (Fig. 4b).
* **Boundary conditions:** periodic, zero-gradient, zero-fixed,
  user-defined, and isolated by multipole expansion to hexadecapole order
  (App. A); with FAS they are applied consistently on every level
  (§2.3.6).
* **Parallelization:** MPI + OpenMP over MeshBlocks; at the transition
  level all data are gathered with `MPI_Allgather` and every rank solves
  the RootGrid levels redundantly. The RootGrid and Octet levels are not
  parallelized (§§3.2.5, 3.4).
* Athena++ uses one global time step, so all levels sit at the same time;
  the authors argue this suits non-local physics such as gravity (§§3.1,
  5).

### Level-by-level against global

[Tomida & Stone (2023)](/sources/tomida-2023.md) (§3.3.1, App. B,
Fig. 13) call level-by-level ("one-way coupled") solvers, among them
Enzo's, not self-consistent, because coarse solutions miss fine-scale
mass. In a binary test with $h = 1/64$, the error in the root region
outside the refined blocks is "a few $\times10^{-4}$" with the full AMR
multigrid and about 1 % with a root-only solution. They infer that
level-by-level is less accurate "by more than one order of magnitude", but
call this a "rough estimate": no level-by-level solver was implemented, so
the factor is a hypothesis, not a measurement.
Enzo's paper concedes the inconsistency itself
([Bryan et al. (2014)](/sources/bryan-2014.md), §5.1). The two sources
agree on the qualitative point; the size of the effect rests on an
indirect experiment.

## Coupling to the hydrodynamic step

* **Athena++** runs the multigrid solve as a separate TaskList on every
  substep of the integrator (VL2, RK2 or RK3), twice per step for a
  second-order integrator; the source terms follow the curl-free
  cell-centred scheme of Mullen et al. (2021) without its exact energy
  conservation
  ([Tomida & Stone (2023)](/sources/tomida-2023.md), §3.2.3, eq. 22;
  see [conservative self-gravity](/methods/conservative-self-gravity.md)).
* **Castro** uses a predictor–corrector: the hydro step uses the source at
  the old time, the Poisson equation is re-solved with the new density,
  and $\frac{\Delta t}{2}$ times the difference between the new and old
  $\rho\mathbf g$ (and the energy analogue) is added. The paper contrasts this with FLASH and
  Enzo, which extrapolate $\mathbf g$ at the half step from the two
  previous times ([Almgren et al. (2010)](/sources/almgren-2010.md),
  §5.1, eqs. 15–20).
* **Enzo**'s PPM update time-centres the gravity source as
  $\frac{\Delta t}{2}\,\mathbf g^{n+1/2}(\rho^n + \rho^{n+1})$
  ([Bryan et al. (2014)](/sources/bryan-2014.md), §4.1, eq. 38).

## Measured behaviour

All from [Tomida & Stone (2023)](/sources/tomida-2023.md), §4, except
where noted.
* **Uniform grid, sinusoidal density** (§4.1.1, Fig. 5): each V-cycle
  reduces the error by a factor of about 0.125; 10–15 iterations converge
  fully; FMG and MGI are second order; the first FMG sweep already reaches
  truncation-level error but carries smoother noise, so a few V-cycles are
  recommended. FMG almost always beats MGI.
* **AMR, binary potential** (§4.2.1, Figs. 7–8): second order; the
  convergence factor is about 0.2 at first, then about 0.5, attributed to
  persistent errors at level boundaries.
* **Weak scaling, uniform grid** (§4.1.2, Fig. 6): from 2 to 200 nodes,
  89.6 %, 73.2 % and 45.7 % for one FMG sweep with $128^3$, $64^3$ and
  $32^3$ MeshBlocks, and 92.9 %, 78.8 % and 56.3 % for FMG plus 10
  V-cycles. Multigrid outperforms the FFT solver at scale. With $64^3$
  blocks one FMG sweep costs about 15 % of an MHD step, FMG plus 10
  V-cycles about 70 %.
* **AMR scaling** (§4.2.2, Fig. 9): 18,432 MeshBlocks on 36 to 2,304
  processes; at 2,304 processes multigrid is about 2–6× slower than MHD
  and less scalable, attributed to the unparallelized RootGrid and Octet
  levels; $16^3$ MeshBlocks are recommended first.
* **[Jeans wave](/benchmarks/jeans-wave.md)** (§4.3, Figs. 10–11): about
  second order; with an unconverged potential (one FMG sweep) the error
  is "precisely second order" and gravity-dominated; in the unstable case
  an unconverged potential breaks symmetry and fragments early.
* **Protostellar collapse demonstration** (§4.4): gravity takes about
  85–90 % of the run time.
* **Castro, hydrostatic white dwarf** with full Poisson or monopole
  gravity: spurious velocities below 1 % of the central sound speed and
  "clear second order convergence in the max norm" of the velocity
  ([Almgren et al. (2010)](/sources/almgren-2010.md), §8.4, Fig. 11).

## Contradictions

**Are level-by-level Poisson solvers adequate?** *Open.*
* [Tomida & Stone (2023)](/sources/tomida-2023.md), §3.3.1, App. B: solving
  each refined level with coarse-level Dirichlet data (Enzo, RAMSES, ART)
  is "not self-consistent", because coarse solutions miss fine-scale mass,
  and is less accurate "by more than one order of magnitude" — a rough
  estimate from a root-only solve, not from an implemented level-by-level
  solver.
* [Bryan et al. (2014)](/sources/bryan-2014.md), §5.1: Enzo's grid-by-grid
  subgrid solve is the production method; the paper concedes it is not a
  coherent level-wide solve and announces a HYPRE-based AMR solver as future
  work, without quantifying the error.
* The two agree that the method is inconsistent; they differ on how much it
  matters, and no source measures it on an implemented level-by-level
  solver.

# Citations

1. [Tomida & Stone (2023)](/sources/tomida-2023.md), §§2–5, Apps. A–B (arXiv v1).
2. [Almgren et al. (2010)](/sources/almgren-2010.md), §§4, 5.1, 6.2.2–6.2.3, 7.4, 8.4 (arXiv v1 numbering).
3. [Bryan et al. (2014)](/sources/bryan-2014.md), §§2.1, 3, 4.1, 5.1, 11.2.6, 12.2.3, 14 (arXiv v1).
