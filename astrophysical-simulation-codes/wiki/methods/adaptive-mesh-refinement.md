---
type: Method
title: "Adaptive mesh refinement in astrophysical codes"
description: "Structured AMR as built into astrophysical codes: cell-based, patch-based and block-based hierarchies, subcycled versus global time stepping, refluxing and EMF correction, conservative restriction and limited prolongation, nesting rules, refinement criteria and load balancing, compared across Athena++, GAMER, PLUTO, Castro, Enzo and RAMSES."
status: established
aliases: [AMR, SAMR, block-structured AMR, patch-based AMR, octree AMR, Berger–Oliger AMR, Berger–Colella AMR, subcycling, refluxing, flux correction]
tags: [amr, conservation, performance]
timestamp: 2026-10-12T00:00:00Z
---

# Adaptive mesh refinement in astrophysical codes

Every framework in this bundle refines a Cartesian (or logically
rectangular) mesh by factors $r_{\mathrm{ref}}$ between levels $l$, with
$h_{l+1} = h_l/r_{\mathrm{ref}}$, and keeps the finite-volume update
conservative across level interfaces. They differ in the unit of
refinement, in whether levels take their own time step, and in how
levels are synchronized. This page compares those choices as the
sources state them.

## Taxonomy: cell, patch, block

[Stone et al. (2020)](/sources/stone-2020.md), §2.2, sort AMR codes into
three families:
* **Cell-based** (cell-by-cell) refinement: RAMSES, ART.
* **Patch-based** Berger–Oliger / Berger–Colella refinement: Enzo, PLUTO,
  AMRVAC, and the libraries Chombo and AMReX.
* **Block-based** refinement: FLASH/PARAMESH, NIRVANA, DISPATCH, Athena++.

[Bryan et al. (2014)](/sources/bryan-2014.md), §1, draw the same lines
for Enzo's variable-size patches against FLASH's fixed blocks and
RAMSES/ART cell refinement. The codes ingested here realize each family
as follows.

| Code | Unit of refinement | $r_{\mathrm{ref}}$ | Nesting rule | Time stepping |
|---|---|---|---|---|
| [Athena++](/software/athena-plus-plus.md) | fixed-size MeshBlock in a binary tree / quadtree / octree | 2 | 2:1 between neighbours | single global $\Delta t$ |
| [GAMER](/software/gamer.md) | octree of patches of $N_{\mathrm b}^3$ cells ($8^3$ in the figures) | 2 | not stated | subcycled |
| [PLUTO](/software/pluto.md) (with Chombo) | disjoint patches, Berger–Rigoutsos clustering | 2 or 4, mixed per level | proper nesting | subcycled |
| [Castro](/software/castro.md) (BoxLib) | union of non-overlapping grids of arbitrary size | 2 or 4 | proper nesting, no parent–child relation | subcycled |
| [Enzo](/software/enzo.md) | variable-size patches, Berger–Rigoutsos clustering | 2 or 4, "generally" 2 | contained in one parent | subcycled, $\Delta t_l$ free |
| RAMSES ([RAMSES-RT](/software/ramses-rt.md)) | oct of $2\times2\times2$ cells in a recursive tree | 2 | 2:1 grading | subcycled, time ratio 2 |

Sources for the table:
[Stone et al. (2020)](/sources/stone-2020.md), §§2.1, 2.1.2, 2.1.7;
[Zhang et al. (2018)](/sources/zhang-2018.md), §3.3;
[Mignone et al. (2012)](/sources/mignone-2012.md), §4;
[Almgren et al. (2010)](/sources/almgren-2010.md), §6.1;
[Bryan et al. (2014)](/sources/bryan-2014.md), §3;
[Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §§5, 5.1.

Details per family:
* **Block-based.** Athena++ MeshBlocks all have the same cell count;
  each refines into $2^d$ children; cells per block per direction must be
  even, and $n_{\mathrm g}$ must be even with AMR. Neighbours differ by
  at most one level. Smaller blocks give more flexibility but a larger
  ghost-cell overhead ([Stone et al. (2020)](/sources/stone-2020.md),
  §§2.1, 2.1.2). The [multigrid gravity solver](/methods/multigrid-self-gravity.md)
  is stricter: it needs logically cubic MeshBlocks with a power of 2
  cells per side ([Tomida & Stone (2023)](/sources/tomida-2023.md), §3.2.1).
  Because each point is covered by "one and only one mesh level", no
  level-dependent derived quantity (such as a cooling temperature)
  arises, which [Stone et al. (2020)](/sources/stone-2020.md), §1, name
  as a defect of patch-based AMR. GAMER groups 8 neighbouring patches into
  a "patch group" of $(2N_{\mathrm b})^3$ cells as the unit of GPU work,
  which lowers the ghost-zone overhead
  ([Zhang et al. (2018)](/sources/zhang-2018.md), §4).
* **Patch-based.** PLUTO-Chombo uses levels $l = 0,\dots,l_{\max}$ with
  integer ratios 2 and 4, mixed as e.g. 2:4:4 or 4:2:2:2:2; patches are
  disjoint and properly nested: a level-$(l+1)$ cell is separated from
  level $l-1$ by at least one row of level-$l$ cells
  ([Mignone et al. (2012)](/sources/mignone-2012.md), §4). Castro grids
  have an even number of cells per direction and a proper-nesting buffer
  of 2 coarse cells for $r_{\mathrm{ref}} = 2$ and 1 for
  $r_{\mathrm{ref}} = 4$, "since four ghost cells are needed for the PPM
  algorithm"; no parent–child relation is required
  ([Almgren et al. (2010)](/sources/almgren-2010.md), §6.1, Fig. 1). Enzo
  subgrids start and end on coarse-cell boundaries and lie wholly inside
  one parent; no proper-nesting or 2:1 rule is stated beyond that
  ([Bryan et al. (2014)](/sources/bryan-2014.md), §3). Enzo's authors
  report that $r_{\mathrm{ref}} = 2$ "typically provides the best
  performance" (§3).
* **Cell-based.** RAMSES starts from one oct, refines uniformly to
  $l_{\min}$ and adaptively to $l_{\max}$; "the resolution must never
  change by more than one level across cell boundaries"
  ([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §5; the paper
  counts the root oct as level 1).

## Time stepping: subcycling or one global step

**Subcycling** (Berger–Oliger). PLUTO-Chombo sets
$\Delta t_{l} = \Delta t_{l-1}/r_{\mathrm{ref}}$, with optional extra
substeps, and advances levels recursively, filling coarse–fine ghost cells
by linear time interpolation of coarse data
([Mignone et al. (2012)](/sources/mignone-2012.md), §4, eq. 46, Fig. 4).
Castro advances recursively with $\Delta t_{l+1} = \Delta t_l/r_{\mathrm{ref}}$
and sets the level-0 step from the most restrictive level, scaled by the
cell-size ratio ([Almgren et al. (2010)](/sources/almgren-2010.md),
§6.2.1). RAMSES takes two substeps on level $l+1$ per step on level $l$
([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §5.1, Listing 1).
GAMER updates level $l$, evolves $l+1$ until synchronized, then corrects
$l$ and (de)refines $l+1$ ([Zhang et al. (2018)](/sources/zhang-2018.md),
§3.3). Enzo's recursive `EvolveLevel` ("W-cycle") lets each level take its
own $\Delta t_l$ until it catches up; the finer steps are not
restricted to the coarse step divided by a power of 2
([Bryan et al. (2014)](/sources/bryan-2014.md), §3, Fig. 2 caption).

**Global step.** Athena++ advances all levels with one $\Delta t$
([Stone et al. (2020)](/sources/stone-2020.md), §2.1.7). The stated
reasons (§2.2): the largest signal speed $\vert\mathbf v\vert + c_f$ is
often on the root level; temporal interpolation adds error, especially
with self-gravity; subcycling complicates optimization and load
balancing; and with equal cell counts per level the saving is only about
half the number of levels. The authors concede that the global step is less
efficient when more than 10 levels cover 1 % or less of the volume.
[Tomida & Stone (2023)](/sources/tomida-2023.md), §§3.1, 5, add that a
single time level suits non-local physics (gravity, implicit radiation).

**Where subcycling bites.** Physics coupled across levels inherits the
subcycling structure:
* Under subcycling, a coarse–fine flux partially updates the coarse
  neighbour, whose state stays ill-defined until the coarse step ends.
  RAMSES-RT therefore does not subcycle radiation inside the hydro step;
  it argues that conservative RT subcycling is "not possible (or at least
  nontrivial)" and runs RT on each level's hydro step instead, which
  keeps photon conservation across levels
  ([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §5.2, App. D).
* Under subcycling, a time step limited by a point-local stiff source
  (cooling, chemistry) forces every finer level to a step $2^l$ smaller
  than needed when the source time scale does not depend on the mesh.
  PLUTO evaluates the source-limited step on leaf cells only, since
  covered cells are overwritten by restriction; the expected speed-up is
  about $2^l$ ([Mignone et al. (2012)](/sources/mignone-2012.md), §4.2,
  eqs. 52–53).
* Castro needs a multilevel Poisson synchronization after subcycled
  levels ([Poisson solvers on adaptive meshes](/methods/multigrid-self-gravity.md);
  [Almgren et al. (2010)](/sources/almgren-2010.md), §§6.2.2–6.2.3).

## Synchronization: refluxing and EMF correction

Fine and coarse fluxes through a shared face differ, so the coarse cell
next to (and not covered by) a fine region is corrected with the fine
fluxes (Berger & Colella 1989):
* Athena++ replaces the coarse face flux with the area-weighted sum of
  the 4 (3D) or 2 (2D) fine face fluxes
  ([Stone et al. (2020)](/sources/stone-2020.md), §2.1.4, Fig. 6).
* With subcycling the replacement is the space–time average of the fine
  fluxes (PLUTO: [Mignone et al. (2012)](/sources/mignone-2012.md), §4,
  eqs. 48–49). Enzo corrects the coarse cell by $\Delta t$ times the
  difference between the coarse flux and the sum over the
  $r_{\mathrm{ref}}^{d-1}$ fine faces
  ([Bryan et al. (2014)](/sources/bryan-2014.md), §3.4, eq. 27), which
  requires a flux-conservative solver "or at least ... an accurate
  estimate of the flux" (§3.2). Castro applies explicit refluxing to the
  coarse cells adjacent to, not covered by, the fine union
  ([Almgren et al. (2010)](/sources/almgren-2010.md), §6.2.1). GAMER does
  the same at leaf coarse cells
  ([Zhang et al. (2018)](/sources/zhang-2018.md), §3.3).

For [constrained transport](/methods/constrained-transport.md) the
face-centred $\mathbf B$ needs the same treatment for the edge EMF
$\boldsymbol{\mathcal E}$:
* Athena++ sets the coarse EMF times the coarse edge length equal to the
  sum of the fine EMFs times the fine edge lengths (eq. 1); on shared
  edges the fine EMFs are averaged first. Even without refinement, EMFs
  on edges shared by MeshBlocks are replaced by their arithmetic mean,
  because round-off, nondeterministic MPI ordering or non-ANSI
  optimization otherwise leave divergence errors that CT never removes
  ([Stone et al. (2020)](/sources/stone-2020.md), §§2.1.1, 2.1.4,
  Figs. 7–8).
* GAMER corrects coarse face $\mathbf B$ with EMF differences on
  coarse–fine "interedges" ([Zhang et al. (2018)](/sources/zhang-2018.md),
  §3.3). Enzo projects the electric field, not $\mathbf B$, from fine to
  coarse and re-updates the parent field
  ([Bryan et al. (2014)](/sources/bryan-2014.md), §4.3).
* PLUTO's AMR avoids the issue by using
  [GLM cleaning](/methods/glm-divergence-cleaning.md) instead of CT
  ([Mignone et al. (2012)](/sources/mignone-2012.md), §§1, 3, 7).

For radiation, RAMSES-RT inter-level fluxes partially update coarse
cells. Across static refinement from level 6 to 8, total photon flux is
constant to "about 1 in $10^4$" for an oblique beam after two crossing
times and "to the number precision, which here is 7 decimals" for a
horizontal beam with HLL; with on-the-fly refinement the discrepancy is
within 0.03 % ([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §5.3,
Figs. 7–8).

## Restriction

Coarse cells covered by fine cells take averages of the fine data:
* Cell-centred conserved variables: volume-weighted average (Athena++:
  [Stone et al. (2020)](/sources/stone-2020.md), §2.1.5, eq. 2; PLUTO:
  [Mignone et al. (2012)](/sources/mignone-2012.md), eq. 47; Castro:
  [Almgren et al. (2010)](/sources/almgren-2010.md), §6.2.1; GAMER:
  [Zhang et al. (2018)](/sources/zhang-2018.md), §3.3).
* Face-centred $\mathbf B$: area-weighted average (Athena++, eq. 3;
  GAMER, §3.3).
* Enzo writes all three cases as one formula,
  $u^{\mathrm{coarse}} = r_{\mathrm{ref}}^{-d}\sum u^{\mathrm{fine}}$,
  with the exponent $d$ for cell-centred, $d-1$ for face-centred and 1
  for edge-centred data
  ([Bryan et al. (2014)](/sources/bryan-2014.md), §3.3, eq. 26).

## Prolongation

Ghost cells at a coarse–fine boundary and newly created fine cells are
interpolated from coarse data.
* **Athena++** uses multidimensional slope-limited linear reconstruction
  with the minmod limiter, chosen as less aggressive than the hydro
  limiter because "sharper limiters produce unphysical structures at
  level interfaces". Ghost zones are prolongated in primitive variables,
  because conserved variables can give negative pressure. New blocks are
  prolongated in conserved variables with a pressure floor, which breaks
  energy conservation but not mass or momentum conservation. Face
  $\mathbf B$ uses the divergence-preserving prolongation of Tóth & Roe
  (2002), extended to nonuniform and curvilinear meshes, and existing fine
  faces are not overwritten
  ([Stone et al. (2020)](/sources/stone-2020.md), §2.1.5, eqs. 4–5).
* **PLUTO** prolongates conservatively, piecewise linear in volume
  coordinates with MC-limited central slopes
  ([Mignone et al. (2012)](/sources/mignone-2012.md), §4, eq. 45,
  Table 1).
* **Enzo** requires conservative and monotone interpolators. Its
  second-order multidimensional linear interpolators limit along cell
  diagonals: exact in 2D (3 constraints for 3 parameters),
  over-constrained in 3D (5 against 4) and fixed heuristically. Options
  are SecondOrderA (minmod diagonal slopes), SecondOrderB (unlimited
  slopes with a positivity limiter), SecondOrderC (CIC, monotone but not
  conservative), ThirdOrderA (TSC, conservative only after a correction
  that may break monotonicity) and FirstOrderA (piecewise constant).
  Ghost cells are filled from the parent first, then from siblings where
  available ([Bryan et al. (2014)](/sources/bryan-2014.md), §3.1,
  App.). CT runs use the divergence-free prolongation of Balsara (2001)
  (§4.3).
* **GAMER** uses conservative interpolation of unspecified order for the
  conserved variables and Balsara (2001) divergence-free prolongation for
  $\mathbf B$ ([Zhang et al. (2018)](/sources/zhang-2018.md), §3.3,
  eq. 17).
* **Castro** does not specify the order of its coarse–fine ghost or
  regrid interpolation ([Almgren et al. (2010)](/sources/almgren-2010.md),
  §§6.1, 6.2.1).
* **RAMSES-RT** fills newly refined radiation cells by straight injection
  or linear interpolation
  ([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §5.2).

## Ghost layers

Athena++ needs $n_{\mathrm g} = 2$ for second-order MHD on a uniform
mesh, and $n_{\mathrm g} = 3$ (hydro) or 4 (MHD) for spatial orders up to
four; it keeps independent message buffers per neighbour, up to 26 in 3D
on uniform grids and 56 with AMR, and exchanges inter-level data through
"coarse buffers" of restricted copies
([Stone et al. (2020)](/sources/stone-2020.md), §§2.1.1, 2.1.3). Enzo
uses 3 ghost zones for PPM and ZEUS and 6 for the gravity solver
([Bryan et al. (2014)](/sources/bryan-2014.md), §3). GAMER's ghost width
is one cell larger in MHD than in hydro because of the staggered field
([Zhang et al. (2018)](/sources/zhang-2018.md), §3.1).

## Refinement criteria

* **Second-derivative (Löhner 1987) estimator.** PLUTO tags a cell when a
  normalized second difference of a chosen variable exceeds a threshold,
  with a default noise-filter parameter of 0.01
  ([Mignone et al. (2012)](/sources/mignone-2012.md), §4.1, eqs. 50–51).
  Enzo lists the same estimator with the parameter $10^{-2}$ by default
  ([Bryan et al. (2014)](/sources/bryan-2014.md), §3.6, eq. 33).
* **Curvature, shear and pressure-gradient indicators** in Athena++,
  with refine and derefine thresholds, e.g. 0.01 and 0.005 for the
  curvature indicator in the double Mach reflection
  ([Stone et al. (2020)](/sources/stone-2020.md), §§3.4.2–3.4.4,
  eqs. 25, 27, 28).
* **Enzo's catalogue** of 13 criteria (§3.6): normalized slope (typically
  0.3), baryon and particle mass (super- or sub-Lagrangian), shocks,
  Jeans length (4 cells per Jeans length by default, after Truelove et
  al.), cooling time, must-refine particles and regions, shear, H I
  optical depth, resistive length, metallicity and the Löhner estimator,
  plus static refined regions.
* **Physics-specific ones:** GAMER refines on the current-to-field ratio
  $\vert\mathbf J\vert/\vert\mathbf B\vert$ against a threshold scaled by
  $1/h_l$ ([Zhang et al. (2018)](/sources/zhang-2018.md), §5.1);
  RAMSES-RT on photon density, ion fractions and their gradients
  ([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §5.2, eq. 43).
  Castro uses user-supplied error estimators
  ([Almgren et al. (2010)](/sources/almgren-2010.md), §6.1).

## Grid generation and regridding

Patch codes cluster tagged cells into rectangles with the
Berger–Rigoutsos algorithm: PLUTO-Chombo
([Mignone et al. (2012)](/sources/mignone-2012.md), §4), Castro, which
regrids at a user-set interval of level-$l$ steps
([Almgren et al. (2010)](/sources/almgren-2010.md), §6.1), and Enzo,
which accepts a proto-subgrid when its fraction of flagged cells is
"typically over 30%" or it is small, and otherwise splits it at the
maximum second derivative of the signature along the longest axis
([Bryan et al. (2014)](/sources/bryan-2014.md), §3.5). Block and oct
codes refine whole blocks or octs into $2^d$ children
([Stone et al. (2020)](/sources/stone-2020.md), §2.1;
[Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §5).

## Load balancing and parallel layout

* **Athena++**: Z-ordering of MeshBlocks from the tree assigns blocks to
  processes; each block carries a "cost" (user-set or timed); blocks are
  redistributed periodically and on refinement. It needs at least one
  block per process and cannot shuffle the block order
  ([Stone et al. (2020)](/sources/stone-2020.md), §§2.1.1, 2.1.6).
* **Castro**: a knapsack heuristic or a Morton space-filling curve,
  switched automatically on grids per level against processors
  ([Almgren et al. (2010)](/sources/almgren-2010.md), §7.1).
* **PLUTO-Chombo**: each level is distributed by boxes, with load equal
  to grid points per box and a Kernighan–Lin knapsack solver; there is no
  parallelism inside a box. Performance deteriorates when the blocks per
  level approach the number of processors, or when the ideal workload per
  processor approaches the maximum box size
  ([Mignone et al. (2012)](/sources/mignone-2012.md), §4.3); the tests
  show scaling degrading below about 3–4 blocks per processor (§6.6).
* **Enzo**: the grid is the unit of distribution; refined grids start on
  the parent's process and are balanced per level by greedy transfer
  (until max/min load < 1.05) or a Hilbert curve; grids are split to
  about 10 per processor; the full hierarchy metadata is replicated on
  every rank ([Bryan et al. (2014)](/sources/bryan-2014.md), §12.1).
  In the AMR strong-scaling run the refined levels scale well to 2,048
  cores, while the root level degrades beyond 1,024 because root tiles are
  not repartitioned on restart (§12.2.3).
* **GAMER**: Hilbert-curve decomposition computed independently per
  level ([Zhang et al. (2018)](/sources/zhang-2018.md), §4).

## Cost and overhead

* Athena++ models the cost per cell of a block with $N_{\mathrm b}$ cells
  per side as a compute term, plus a communication term $\propto
  1/N_{\mathrm b}$, plus a per-block overhead $\propto 1/N_{\mathrm b}^3$.
  On a $128^3$ blast the cost rises about 10× from $128^3$ to $4^3$
  blocks; communication exceeds compute near $16^3$. The recommendation
  is $8^3$–$16^3$ blocks with AMR and the largest possible blocks on
  uniform grids ([Stone et al. (2020)](/sources/stone-2020.md),
  §§3.6.4–3.6.5, eq. 30). The AMR overhead on a linear-wave run was about
  20 % (132.5 → 106.0 Mzone-cycles/s, §3.4.1).
* Castro's two-level AMR overhead (monopole gravity) is about 5 % on 8
  processes and 19 % on 64,000, relative to the ideal factor 3
  ([Almgren et al. (2010)](/sources/almgren-2010.md), §7.4).
* Enzo's cost model for $r_{\mathrm{ref}} = 2$ makes the cost of level
  $l$ grow with $l$ unless the refined volume fraction drops by more than
  a factor 16 per level; cosmological runs hover near that critical
  ratio ([Bryan et al. (2014)](/sources/bryan-2014.md), §12.2.4,
  eqs. 113–115; the text writes the ratio both ways round, see the
  Source page).

## Observed effects of refinement

* Coarse regions damp sound waves: in Athena++'s Kelvin–Helmholtz runs
  AMR "cannot be used" where such waves matter
  ([Stone et al. (2020)](/sources/stone-2020.md), §3.4.3). In the
  relativistic Kelvin–Helmholtz test many small-scale features are
  artefacts of fine/coarse boundaries (§4.3.2).
* Enzo's "wave pool" and "shock pool" tests send a sound wave and a
  Mach 2 shock through a static refined region: PPM shows no significant
  reflection at refinement boundaries; ZEUS puts the shock in the wrong
  place ([Bryan et al. (2014)](/sources/bryan-2014.md), §§11.2.2–11.2.3,
  qualitative).
* Speed-ups against uniform grids at equal finest resolution are
  reported per test: 4.4× on the
  [double Mach reflection](/benchmarks/double-mach-reflection.md) in
  Athena++ ([Stone et al. (2020)](/sources/stone-2020.md), §3.4.2); up to
  1977.8 in a 1D 10-level shock tube in PLUTO, where the static time is
  inferred from ideal scaling
  ([Mignone et al. (2012)](/sources/mignone-2012.md), §5.1.1, Table 2).
* Athena++ keeps the 3D [Sedov–Taylor blast](/benchmarks/sedov-taylor-blast-wave.md)
  spherically symmetric with AMR; the Liska–Wendroff implosion is
  symmetric to machine precision, and the symmetry is "also preserved
  with AMR"
  ([Stone et al. (2020)](/sources/stone-2020.md), §§3.3.5, 3.4.4).

## Later uses (batch 2)

### Refinement for self-gravitating collapse and sink particles

* **Jeans refinement.** [Federrath et al. (2010)](/sources/federrath-2010.md)
  run the block-AMR code FLASH with the Truelove condition of at least 4
  cells per Jeans length (§2.2.1), and note the claim of Heitsch et al.
  (2001) that MHD needs more than four. In practice they refine to keep at
  least 12 cells per Jeans length on every level below the finest and
  resolve it with 5 cells on the finest, where the
  [sink-particle](/methods/sink-particles.md) accretion radius is about
  2.5 cells (§4.2.1); their gas–sink gravity test refines at 6 and
  derefines above 12 cells per Jeans length (§3.2), and the cluster run adds
  shock refinement (§4.2). See the
  [Jeans resolution criterion](/definitions/jeans-resolution-criterion.md).
* **Why sinks are needed.** The Truelove and Heitsch criteria "are only
  meaningful in regions that are undergoing self-gravitational collapse".
  Pure AMR satisfies them only for the first object to collapse, because
  the Courant step of the finest level then stalls the whole run; sink
  particles cut the runaway off "in a controlled fashion"
  ([Federrath et al. (2010)](/sources/federrath-2010.md), §2.2.1). The
  refinement criterion drives collapsing gas to the finest level, and sinks
  may form only there; an extra criterion keeps every cell within a sink's
  accretion radius at the finest level (§2.2.2).
* **Sink-centred refinement.**
  [Krumholz, McKee & Klein (2004)](/sources/krumholz-2004.md) use a
  Berger–Oliger code with subcycled levels and a synchronization step for
  conservation across levels, and refine so that a sink's accretion zone
  is always on the finest level; every cell size and time step they quote
  is the finest level's (§2.1). In their shock–accretor application,
  refinement keeps the distance to the sink at no less than 32 cells, down
  to a finest cell of 1/512 of the Bondi radius (§4). They assert that the
  sink algorithm "is not dependent on any of the details of the AMR
  framework" and applies equally to fixed grids (§2.1).
* **Gravity near Cartesian boundaries.** In FLASH's gas–sink gravity test
  on a static singular isothermal sphere ($32^3$ root grid plus 2 levels,
  isolated boundaries), test-particle orbits broaden after about 100 inner
  orbits because the multigrid potential loses spherical symmetry near the
  Cartesian boundaries; the authors find it "hard to maintain perfect
  spherical symmetry for more than 10-100 sink particle orbits"
  ([Federrath et al. (2010)](/sources/federrath-2010.md), §3.2, Figs. 5–6).

### Castro in 2016

[Katz et al. (2016)](/sources/katz-2016.md) add, for
[Castro](/software/castro.md): subcycling with as many substeps as the
refinement jump (two jumps of 4 give 16 finest steps per root step);
refined grids may not reach the domain boundary; the final multilevel
gravity synchronization is optional and disabled for their merger runs
(§2.1, §2.3); boxes a multiple of 16 zones per side for multigrid
efficiency, maximum grid size 32–64 (§5); tagging by distance from each
star (twice the Roche radius) on the root level and by density on finer
levels (§3.2). The default box distribution is a Morton space-filling
curve, while a knapsack algorithm proved most efficient for their problem
(§5); the 2010 description of an automatic switch between the two (Load
balancing, above) and this statement of the default differ, and neither
paper dates the change.

## Contradictions

**Is time subcycling worth its cost?** *Open.*
* [Stone et al. (2020)](/sources/stone-2020.md), §§2.1.7, 2.2: the
  temporal interpolation that subcycling needs "adds error, especially with
  self-gravity", its saving is only about half the number of levels when
  the levels hold equal numbers of cells, and its complexity hurts
  optimization and load balance; Athena++ therefore uses one global step.
* [Almgren et al. (2010)](/sources/almgren-2010.md), §6.2;
  [Bryan et al. (2014)](/sources/bryan-2014.md), §3;
  [Mignone et al. (2012)](/sources/mignone-2012.md), §4;
  [Zhang et al. (2018)](/sources/zhang-2018.md), §3.3;
  [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §5.1: subcycle by
  design (Castro adds a multilevel gravity correction solve for it).
* No source measures the interpolation error or the cost trade-off on a
  common problem; the entry closes when one does.

**Do patch-based hierarchies suffer level-dependent derived quantities?**
*Open.* [Stone et al. (2020)](/sources/stone-2020.md), §1, argue that
covering each point by one level only avoids level-dependent derived
quantities (e.g. a temperature used by cooling) that afflict patch-based
AMR; the patch-based sources (Castro, Enzo, PLUTO-Chombo) do not discuss
the issue, and none quantifies it.

# Citations

1. [Stone et al. (2020)](/sources/stone-2020.md), §§1, 2.1–2.2, 3.4, 3.6, 4.3.
2. [Mignone et al. (2012)](/sources/mignone-2012.md), §§4, 4.1–4.3, 5.1.1, 6.6.
3. [Almgren et al. (2010)](/sources/almgren-2010.md), §§6.1–6.2, 7.1, 7.4 (arXiv v1 numbering).
4. [Bryan et al. (2014)](/sources/bryan-2014.md), §§1, 3, 3.1–3.6, 4.3, 11.2, 12.1–12.2, App. (arXiv v1).
5. [Zhang et al. (2018)](/sources/zhang-2018.md), §§3.1, 3.3, 4, 5.1 (arXiv v4).
6. [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §§5–5.3, App. D (arXiv v2).
7. [Tomida & Stone (2023)](/sources/tomida-2023.md), §§3.1, 3.2.1, 5 (arXiv v1).
8. [Federrath et al. (2010)](/sources/federrath-2010.md), §§2.2.1–2.2.2, 3.2, 4.2 (arXiv v2).
9. [Krumholz, McKee & Klein (2004)](/sources/krumholz-2004.md), §§2.1, 4 (arXiv v1).
10. [Katz et al. (2016)](/sources/katz-2016.md), §§2.1, 2.3, 3.2, 5 (arXiv v2).
