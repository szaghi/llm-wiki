---
type: Method
title: "Adaptive mesh refinement in astrophysical codes"
description: "Structured AMR as built into astrophysical codes: cell-based, patch-based and block-based hierarchies, subcycled versus global time stepping, refluxing and EMF correction, conservative restriction and limited prolongation, nesting rules, refinement criteria and load balancing, compared across Athena++, AthenaK, GAMER, PLUTO, Castro, Enzo, FLASH, RAMSES, Quokka, GRaM-X and ADAM, with the GPU codes' block-size and host-side bookkeeping findings."
status: established
aliases: [AMR, SAMR, block-structured AMR, patch-based AMR, octree AMR, Berger–Oliger AMR, Berger–Colella AMR, subcycling, refluxing, flux correction]
tags: [amr, conservation, performance, gpu]
timestamp: 2026-10-13T00:00:00Z
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

## Later uses (batch 3)

### GPU codes with AMR

Four batch-3 codes refine their meshes. The three that state a ratio use
$r_{\mathrm{ref}} = 2$; AthenaK keeps the Athena++ design.

| Code | Unit of refinement | $r_{\mathrm{ref}}$ | Nesting rule | Time stepping |
|---|---|---|---|---|
| [Quokka](/software/quokka.md) (AMReX `AMRCore`) | block-structured grids sized by `blocking_factor` and `max_grid_size` | 2 only | not stated | subcycled, $\Delta t_l = \Delta t_0/2^l$ |
| [AthenaK](/software/athenak.md) | MeshBlocks in a binary tree, quadtree or octree, as Athena++ | not restated | not restated | single global $\Delta t$ |
| [GRaM-X](/software/gram-x.md) (CarpetX on AMReX) | blocks of runtime size, "typical" $8^3$ | 2 | proper nesting | single global $\Delta t$ |
| [ADAM](/software/adam.md) | identical blocks in an octree, $2^3$ children | 2 | 2:1 between contiguous blocks | single global $\Delta t$ |

Sources for the table:
[Wibking & Krumholz (2022)](/sources/wibking-2022.md), §§2.2, 2.2.4, 4;
[Stone et al. (2026)](/sources/stone-2026.md), §2;
[Shankar et al. (2023)](/sources/shankar-2023.md), §III A;
[Zaghi et al. (2023)](/sources/zaghi-2023.md), §§2.2, 3.1.

**Quokka** ([Wibking & Krumholz (2022)](/sources/wibking-2022.md)).
* Berger–Oliger / Berger–Colella AMR on Cartesian grids through AMReX's
  lower-level `AMRCore` interface, which supplies grid generation,
  coarse–fine interpolation, domain decomposition and communication;
  Quokka does the time stepping and the refinement criteria (§2.2).
* $r_{\mathrm{ref}} = 2$ only, "to minimize numerical glitches" at
  coarse–fine boundaries; linear conservative interpolation on
  refinement, conservative averaging on derefinement; a flux-register
  synchronization "at the end of every two time steps on level $l>0$"
  keeps conservation to machine precision (§2.2).
* **Radiation across levels** (§2.2.4). After discussing the options of
  [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), Quokka subcycles
  the explicit radiation within each level: the coarse step is chosen so
  that each level advance takes at most a set number of radiation
  substeps (default 10, used in all tests), and the coarse–fine radiation
  flux mismatch is added to the adjacent coarse cells at the end of each
  level advance. A maximum of one reproduces RAMSES's flux
  synchronization. Too large a maximum can break positivity of
  $E_{\mathrm r}$ or flux causality on the coarse level. This is a working
  design for what RAMSES-RT calls "not possible (or at least nontrivial)"
  (Where subcycling bites, above), with the stated risk as its price; see
  [M1 radiation transport](/methods/m1-radiation-transport.md).
* **Criteria.** Relative density gradient above 0.2 (Kelvin–Helmholtz,
  §3.1.8); relative $E_{\mathrm r}$ gradient above 0.1 (shadow and beam
  tests, §§3.2.4–3.2.5); relative density gradient (AMR scaling run, §4.2).
  The authors advocate refining on the gradient of the optical depth per
  cell where the optically thick Riemann correction fails (§2.2.2).
* **Grid sizes.** `blocking_factor` = `max_grid_size` = 128 in the uniform
  runs; `blocking_factor` 32 and `max_grid_size` 128 in the AMR run (§4).

**AthenaK** ([Stone et al. (2026)](/sources/stone-2026.md), §2).
The Athena++ design is kept (MeshBlocks in a binary, quad- or octree,
Z-ordering, flux correction at level boundaries, one global time step),
and "very little of the overall design was changed". On the GPU:
* All MeshBlocks of a device form one MeshBlockPack, so one kernel launch
  covers them; this "greatly enhances performance when there are a large
  number of small MeshBlocks on the same device".
* Field data stay on the device and are moved to the host only for
  output; the tree is created, stored and refined on the host.
* Ghost cells are packed inside device kernels and sent by point-to-point
  MPI, one message per MeshBlock of the pack; prolongation and
  restriction are done "all at once inside parallel kernels".
* The first-order flux correction fallback must run before the
  level-boundary flux corrections (§3).

**GRaM-X** ([Shankar et al. (2023)](/sources/shankar-2023.md)).
* The Cactus driver CarpetX implements Berger–Oliger block-structured AMR
  on AMReX: $r_{\mathrm{ref}} = 2$ ("Each level has half the spacing"),
  proper nesting, ghost zones filled by prolongation from the coarser
  level, restriction of overlaid coarse data, blocks of runtime-chosen size
  (§III A). AMReX's inter-mesh operators were extended to higher-order
  templated stencils for vertex-centred (spacetime) and conservative
  cell-centred (fluid) data (§III).
* **No subcycling**: one $\Delta t$ on all levels, "for simplicity" and
  because it "increases parallel scalability ... since all refinement
  levels can be evolved simultaneously. Subcycling in time necessarily
  serializes evolving different refinement levels." (§III A). This is a
  reason for the global step not in the Athena++ list above.
* Fine face fluxes are restricted (averaged) to coarse faces so that
  integrated fluxes agree on all levels; "As we are using a global time
  step, so-called refluxing is not necessary." (§III C 3).
* Edge-centred vector potential keeps $\nabla\cdot\mathbf B$ zero to
  round-off "in particular near mesh refinement interfaces" (§III B); the
  algorithm is not described.
* "All of CarpetX's basic operations are fully GPU enabled", and all data
  stay in device memory, moved to the host only for I/O (§§III, III C). The paper reports no AMR performance numbers (all
  benchmarks are unigrid, §V).

**ADAM** ([Zaghi et al. (2023)](/sources/zaghi-2023.md), §2.2).
* Block-based octree: one root block, each block splits into 8 identical
  children and 8 siblings can rejoin. The tree is a hash map keyed by a
  64-bit linearization of level and block coordinates, replicated on all
  processes and updated "essentially" serially (a stated limitation).
* AMR update in three steps: marking by a back-end (GPU) routine, e.g. on
  a gradient criterion, then a CPU pass that
  enforces the 2:1 rule, sibling-complete recomposition and the maximum
  level; refinement and coarsening on the CPU "by interpolation" (order
  and conservation not stated) after copying the field from the GPU; load
  balancing along Morton space-filling curves, then copy back.
* Ghost cells across level jumps use second-order interpolation;
  inter-process exchange uses CUDA-aware MPI.
* **Criteria.** Density-gradient modulus with target coarse and fine
  cell sizes (shock test, §3.2); enthalpy gradient (vortex test, App.).
  To avoid "flip-flop", blocks split above one threshold and recompose
  below a smaller one, leaving a persistence band.
* One global $\Delta t$ from the minimum over cells (§3.1, eq. 9); no
  subcycling is described. The paper does not discuss conservation across
  level jumps (refluxing); NASTO is a finite-difference scheme.

**Codes without AMR.** [IDEFIX](/software/idefix.md) uses stretched
rectilinear grids instead, and its sequential dimension-by-dimension
ghost exchange is stated to be unsuited to a future AMR version
([Lesur et al. (2023)](/sources/lesur-2023.md), §§2.6, 3.4).
[Cholla](/software/cholla.md) is static-mesh only with one time step; on
Frontier it reaches $19{,}278^3 \approx 7.2\times10^{12}$ cells without
AMR ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §1).
[gPLUTO](/software/gpluto.md) as described is uniform-mesh; PLUTO's
Chombo AMR is not part of the GPU rewrite
([Rossazza et al. (2026)](/sources/rossazza-2026.md), §2.2).
[STREAmS](/software/streams.md) has one Cartesian mesh, uniform in the
streamwise and spanwise directions and stretched in the wall-normal one
(error-function or sinh mapping) ([Bernardini et al. (2021)](/sources/bernardini-2021.md),
§§3.1–3.2).

### Cost and overhead on GPUs

* **Block size.** On one A100 at fixed total grid, AthenaK throughput
  falls from 614 to 413, 242 and 126 million cell updates per second as
  MeshBlocks shrink from $128^3$ to $64^3$, $32^3$ and $16^3$; "Running
  small problems on GPUs is not an effective use of resources"
  ([Stone et al. (2026)](/sources/stone-2026.md), §5.1). ADAM on V100s
  finds blocks of $16^3$ cheaper per cell than $8^3$ (grind time 0.25 →
  0.16 at equal GPU count, runs 4 and 7 on 8 GPUs; labelled seconds, the printed values are seconds per million
  cells per GPU per iteration), while $32^3$ on 64 GPUs
  raises the MPI ghost time ([Zaghi et al. (2023)](/sources/zaghi-2023.md),
  §3.2, Fig. 6, Table 1 runs 1, 7, 8). Quokka recommends at least $256^3$
  cells per GPU per level ([Wibking & Krumholz (2022)](/sources/wibking-2022.md),
  §4.2). These GPU findings qualify, for GPUs, the CPU recommendation of
  $8^3$–$16^3$ blocks with AMR in Athena++ (Cost and overhead, above);
  the hardware differs, so they do not contradict it.
* **AMR overhead.** AthenaK's 2D MHD blast on one A100 runs at 181
  million cell updates per second on a uniform $4096^2$ grid and 141 with
  AMR, "roughly 20%" overhead (22 % from the printed numbers), the same
  fraction Athena++ reported on CPUs (above); the authors expect 2D to
  amplify the overhead ([Stone et al. (2026)](/sources/stone-2026.md),
  §5.1, Fig. 20). Quokka's single-node per-GPU AMR throughput is about
  50 % below the uniform grid, attributed to fewer than $256^3$ cells per
  GPU per level and to sequential level-by-level stepping
  ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §4.2).
* **Regridding.** ADAM's serial octree update costs 4.25 s on 1 GPU and
  still 1.84 s on 32 (7008 blocks), and grows from 0.74 s at 1562 blocks
  to 527.97 s at 684,258 blocks, "dramatically high when the number of
  blocks increases" ([Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.2,
  Table 1).
* **Scaling with AMR.** Quokka's AMR strong scaling ($256^3$ root plus 2
  levels, V100s) gives 100 %, 86.70 %, 65.83 % and 52.69 % efficiency on
  4, 8, 16 and 32 GPUs ([Wibking & Krumholz (2022)](/sources/wibking-2022.md),
  §4.2, Table 5). AthenaK's AMR weak scaling on Frontier is "nearly
  perfect" to 4096 GCDs with MeshBlocks fixed at $32^3$, migrating over 5
  million MeshBlocks for load balance
  ([Stone et al. (2026)](/sources/stone-2026.md), §5.2, Fig. 22).

### Observed effects of refinement (GPU codes)

* AthenaK's 2D MHD blast with a $1024^2$ root and two levels gives density
  "essentially identical" to the uniform $4096^2$ run in 18 % of the wall
  time; the caption says "5.4× faster", while $1/0.18$ is 5.6
  ([Stone et al. (2026)](/sources/stone-2026.md), §5.1, Fig. 20).
* Quokka's Kelvin–Helmholtz run with 4 levels on a $2048^2$ base (peak
  $32{,}768^2$, $128^2$ local grids) took about 4.5 h on one GPU and shows
  no visible artefacts at level boundaries (qualitative)
  ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.1.8, Fig. 7).
* In ADAM's shock–sphere runs, halving the finest target cell size
  multiplies the cell count by "between 4 and 5" instead of 8; the finest
  run has 350 million cells "instead of the 8 billions it would have with
  uniform refinement", a cell-count ratio rather than a measured time
  ([Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.2, Table 1 runs
  9–13). The moving-vortex appendix reports that refinement jumps "seem to
  not pollute the solution" (visual).

### Bearing on the open entries (batch 3)

* **Is time subcycling worth its cost?** Batch 3 adds one subcycled code
  (Quokka) and three with a global step (AthenaK, GRaM-X, ADAM). GRaM-X
  adds a reason, that subcycling serializes the levels and hurts parallel
  scalability, and Quokka attributes part of its AMR efficiency loss to
  sequential level-by-level stepping; neither measures the trade-off
  against the alternative on a common problem, so the entry stays open.
* **Level-dependent derived quantities.** No batch-3 source discusses the
  issue.

## Later uses (batch 4)

### FLASH in a 2021 production configuration

[Mathew & Federrath (2021)](/sources/mathew-2021.md) document the
refinement set-up of a [FLASH](/software/flash.md) ("flash4") application,
eleven years after the configuration of
[Federrath et al. (2010)](/sources/federrath-2010.md) in Later uses
(batch 2):

| Code | Unit of refinement | $r_{\mathrm{ref}}$ | Nesting rule | Time stepping |
|---|---|---|---|---|
| [FLASH](/software/flash.md) (PARAMESH) | block, after Berger & Colella (1989) | not stated | not stated | not stated |

* **Jeans refinement at 16 cells.** On all levels below the finest the
  Jeans length is resolved by $N_{\mathrm J} \ge 16$ cells "to prevent
  underestimation of the turbulent energy and to resolve the local
  collapse reasonably well" (citing Federrath et al. 2011), against at
  least 12 in Federrath et al. (2010), §4.2.1. The new reason concerns the
  turbulent energy, not artificial fragmentation. On the finest level the
  sink size $2r_{\mathrm{acc}} = 5h$ keeps 5 cells per Jeans length, the
  2010 value, which the authors say satisfies the Truelove criterion
  (§2.3). See the
  [Jeans resolution criterion](/definitions/jeans-resolution-criterion.md).
* **Grid.** A triple-periodic 2 pc box at effective $N = 4096$, finest
  $h = 100$ AU; the root grid size and the number of levels are not
  stated, and no criterion besides the Jeans one is named (§2.6,
  Table 1).
* **No resolution study.** All runs use one finest resolution; ten
  turbulence realizations per model replace a resolution sweep, and the
  authors name resolution as the main caveat (§§3, 6.1). The paper reports
  no AMR cost or overhead.

### Bearing on the open entries (batch 4)

Mathew & Federrath do not describe FLASH's time stepping across levels or
any level-dependent quantity. [Porth et al. (2019)](/sources/porth-2019.md),
§3, §4.1.5, describe H-AMR's locally adaptive time stepping, which decouples
temporal from spatial refinement levels and is called "superior to the
'standard' hierarchical timestepping", with 3–4 levels giving a further
factor 3–5 in speed; the factor is quoted from Chatterjee et al. (2019),
not measured against a global step, so the subcycling entry stays open.

## Later uses (batch 5)

* **Jeans refinement in the original.** [Truelove et al. (1997)](/sources/truelove-1997.md)
  refine with ratio 4 wherever the Jeans number (cell size over Jeans
  length) reaches a threshold, "immediately reducing [the Jeans number] there by a
  factor of 4", evaluated in every cell at every step, and estimate that
  a uniform grid covering 9 decades of collapse with 10 cells across the
  final cloud would need more than $10^{12}$ cells (§2, Fig. 1). They add
  an AMR-specific hazard: perturbations grow as they are advected into
  finer grids, and coarse-to-fine interpolation at regridding seeds
  errors (§2). The scope of the criterion is an open entry on the
  [Jeans resolution criterion](/definitions/jeans-resolution-criterion.md)
  page.

## Later uses (batch 6)

### The original patch-based AMR (Berger & Colella 1989)

[Berger & Colella (1989)](/sources/berger-1989.md) is the primary source
for the conservative patch-based AMR that the codes above cite. Its 2D
design, in the format of the table at the top:

| Code | Unit of refinement | $r_{\mathrm{ref}}$ | Nesting rule | Time stepping |
|---|---|---|---|---|
| Berger–Colella code (unnamed, 3000 lines of Fortran) | logically rectangular patches on coarse grid lines, clustered, possibly overlapping on one level | even only; 4 in the runs | proper nesting, conditions (i)–(ii) below | subcycled, $\Delta t_l/h_l$ equal on all levels |

Sources for the row: §§2, 5, 7, 8.

* **Hierarchy** (§2). Each level is a union of rectangles that are subsets
  of one discretization of the domain; rectangles of one level may
  overlap, but the solution must not depend on the decomposition, and the
  value at a point is that of the finest grid containing it. Patch
  boundaries lie on coarse grid lines, unlike the rotated patches of
  Berger & Oliger, which "greatly simplifies the maintenance of
  conservation" (§1).
* **Proper nesting** (§2): "(i) a fine grid starts and ends at the corner
  of a cell in the next coarser grid. (ii) There must be at least one
  level $l-1$ cell in some level $l-1$ grid separating a grid cell at level
  $l$ from a cell at level $l-2$", except at the physical boundary; this is
  "not as stringent as requiring a fine grid to be contained in only one
  coarser level grid" (Fig. 2.1).
* **Time refinement** (§2). The same ratio in space and time, so that one
  explicit scheme is stable on all levels; the stated reasons are that
  spatial and temporal truncation errors are often of the same order and
  that "the smaller time step of the fine grid is not imposed globally".
  Before a grid advances, all finer grids have reached its time (§3).
* **Restriction** (§3). After every coarse step a covered coarse cell takes
  the average of its $r_{\mathrm{ref}}^2$ fine cells, which is "equivalent
  (within roundoff error)" to redefining the coarse fluxes as time sums of
  fine fluxes but needs no flux storage.
* **Flux register** (§3, eqs. 2–3). For an uncovered coarse cell whose
  left face borders a fine grid, the net correction after the
  $r_{\mathrm{ref}}$ fine steps is
  $$u^{\mathrm{coarse}} \leftarrow u^{\mathrm{coarse}} + \frac{\Delta t_l}{h_l}\left(\frac{1}{r_{\mathrm{ref}}^{2}}\sum_{\text{fine steps}}\ \sum_{\text{fine faces}}\hat f^{\mathrm{fine}} - \hat f^{\mathrm{coarse}}_{i+1/2}\right),$$
  with the sign reversed for a right face (2D, $r_{\mathrm{ref}}$ fine faces
  and $r_{\mathrm{ref}}$ fine steps; the weight is $1/r_{\mathrm{ref}}$ for
  area times $1/r_{\mathrm{ref}}$ for the step ratio). It is accumulated in
  a register per coarse–fine face, initialized to minus the coarse flux and
  incremented after each fine step, stored per fine grid; with overlapping
  fine grids a marker array corrects each coarse edge once. Cost "approximately
  0.3% of a typical run time". This is the construction behind the
  refluxing formulas of Enzo, PLUTO, Castro and GAMER above.
* **Ghost values** (§4). From same-level neighbours where possible,
  otherwise bilinear interpolation in space from coarser levels and, "if
  necessary", linear interpolation in time; filled per boundary patch, with
  same-level data overwriting interpolated data. Conservation or limiting
  of the interpolation is not stated. A first point-by-point version "took
  40% of the run time and had to be rewritten".
* **Regridding** (§5). Recursive from the finest level; at most one new
  level per regrid, except at $t = 0$; a buffer of flagged cells ("two
  cells in each direction is typical"), traded against regrid frequency;
  extra flags under grids two levels finer to keep the nesting.
* **Clustering** (§5). One patch around all flagged cells, bisected along
  its long side while its fraction of flagged cells is below a minimum
  (e.g. 60 %; 65 % in the runs), then pairs merged when the merged grid
  costs less, with a cost proportional to $mn + m + n$ for an $m\times n$
  grid (fluxes plus perimeter work); "approximately 1.7% of the CPU time".
* **Refinement criterion** (§6). Richardson extrapolation: two steps on a
  grid minus one double step on the grid coarsened by 2, divided by
  $2^3 - 2 = 6$ for a second-order scheme (the paper gives the general
  formula), estimates the local truncation error; all four fine cells are
  flagged where it exceeds a tolerance (0.02 on density in the runs). It
  is scheme-independent but always large at captured discontinuities. A
  captured shock between constant states need not be refined, because it
  spreads over a fixed number of zones; contacts and slip lines spread
  with time and usually must be.
* **Strong shocks across coarse–fine interfaces** (§6, Figs. 6.1–6.2).
  Captured fluxes near a shock differ by $O(1)$ from exact ones; on a
  uniform grid these errors cancel in time, but across an interface
  between two mesh sizes they do not, and they enter the post-shock state
  as spurious waves whose observed amplitude is proportional to the jump in
  the characteristic quantities. Above a threshold strength, shocks "must
  be refined everywhere, if they are to be refined anywhere".
* **Cost** (§7, Tables I–II; Cray X-MP, oblique shock reflection, three
  levels of ratio 4, effective $1600\times320$). Integration 78.29 % of
  5674 CPU s; interpolation 12.95 %, output 2.87 %, grid updates 2.78 %,
  grid generation 1.71 %, memory management 0.59 %; error estimation 3 %
  of the integration. Over 90 % of the integrated cells are on the finest
  level ($1.13\times10^8$ of about $1.2\times10^8$ cell updates). With the
  finest grids on about 10 % of the domain, "an equivalent uniform grid
  computation would require a factor of 8 more CPU time" and at least 2.2
  times the memory. The AMR overhead outside integration and output is
  about 18 % (sum of the printed rows, computed here). See
  [double Mach reflection](/benchmarks/double-mach-reflection.md) for the
  problem family.

### Attributions checked against the original

* **Refluxing and restriction** (Synchronization and Restriction, above):
  the attribution of the coarse-cell correction to Berger & Colella
  agrees with §3; the original adds the flux register, the
  once-per-edge rule and the equivalence of restriction to fine-flux
  sums.
* **"Berger–Oliger / Berger–Colella"** (Taxonomy, above). The two are one
  family, but the original distinguishes them: Berger & Colella align
  patches with the coarse grid and make global conservation explicit,
  where Berger & Oliger allowed rotated patches (§1).
* **Proper nesting.** PLUTO-Chombo's rule (a level-$(l+1)$ cell separated
  from level $l-1$ by a row of level-$l$ cells) is condition (ii) of the
  original; the original adds condition (i), patches starting and ending
  on coarse-cell corners. Castro's absence of a parent–child relation
  agrees with the original, which does not require a fine grid to lie in
  a single coarser grid.
* **Enzo** (table at the top). Enzo's subgrids lie wholly in one parent
  and its finer steps are not tied to the coarse step divided by a power
  of 2 ([Bryan et al. (2014)](/sources/bryan-2014.md), §3); the original
  does not require containment in one parent, and it fixes the time ratio
  at exactly $r_{\mathrm{ref}}$. These are Enzo's departures from the
  original, not contradictions of it.
* **Disjoint patches.** PLUTO's and Castro's grids are disjoint or
  non-overlapping; the original allows same-level overlap and handles it
  in the flux correction (§§2–3). The later codes are stricter.
* **Clustering** (Grid generation, above). The original does not use the
  Berger–Rigoutsos algorithm but bisection and merging under an efficiency
  threshold; Enzo's acceptance of proto-subgrids "typically over 30%"
  flagged is a different algorithm and parameter, not a disagreement.
* **FLASH** (batch-4 table). "Block, after Berger & Colella (1989)" is
  [Mathew & Federrath (2021)](/sources/mathew-2021.md)'s citation for
  FLASH's AMR; the original describes clustered patches of variable size,
  not the fixed-size blocks of PARAMESH.
* **Temporal interpolation.** The ghost filling of the original is linear
  in time (§4); this is the kind of temporal interpolation that
  [Stone et al. (2020)](/sources/stone-2020.md) name as a source of error
  under subcycling (Time stepping, above). The original does not measure
  its error.

### Bearing on the open entries (batch 6)

* **Is time subcycling worth its cost?** The original gives the accuracy
  rationale for subcycling (truncation errors of equal order in space and
  time; the fine step is not imposed globally) and a cost table in which
  the finest level dominates the cell updates; its factor-8 estimate
  compares with a uniform grid, not with a global step on the same
  hierarchy. The entry stays open.
* **Level-dependent derived quantities.** The original defines the
  solution at a point as the finest grid's value (§2) and does not discuss
  derived quantities; the question is unchanged.

## Later uses (batch 8)

### FLASH's first version from its code paper

[Fryxell et al. (2000)](/sources/fryxell-2000.md), §2, describe the
PARAMESH mesh of the first [FLASH](/software/flash.md) version. In the
format of the table at the top, replacing for that version the "not
stated" entries of the batch-4 row:

| Code | Unit of refinement | $r_{\mathrm{ref}}$ | Nesting rule | Time stepping |
|---|---|---|---|---|
| [FLASH](/software/flash.md) (first version, PARAMESH) | fixed-size blocks of $8^d$ cells in an oct- or quad-tree, each refining into $2^d$ children | 2 | at most one level jump across adjacent blocks | single global $\Delta t$ (PARAMESH could subcycle; FLASH does not) |

* **Family.** The authors class PARAMESH as block-structured AMR,
  "similar to" De Zeeuw & Powell (1993), and contrast it with Berger-style
  overlapping or rotated subgrids ("very complex and has proven to be very
  difficult to parallelize") and with Khokhlov's cell-based tree. This
  agrees with the Taxonomy above and with the batch-6 check of the
  Berger & Colella citation.
* **Refluxing** (Fig. 4). At a refinement jump the fine-face fluxes of
  mass, momentum, energy and composition are summed and replace the
  coarse-face flux, printed as the plain sum of the four fine fluxes in
  3D; area weighting is not stated. Without subcycling no time sum is needed. This
  agrees in kind with the Athena++ replacement (Synchronization, above).
* **Prolongation.** "The FLASH code employs quadratic interpolation for
  the guard cell filling operation"; conservation and limiting are not
  stated.
* **Ghost layers.** $n_{\mathrm g} = 4$, because PPM "requires four guard
  cells at each spatial boundary" (§§2, 3.2), against Enzo's 3 for PPM.
* **Refinement criterion** (eqs. 1–3). The Löhner estimator with the
  noise filter 0.01, as in PLUTO and Enzo; a block is refined when the
  estimator's maximum over its interior plus a halo two guard cells wide
  exceeds 0.8 and derefined below 0.2, on density, pressure and
  temperature, evaluated "defaulting to once every four time steps". The
  multidimensional form (eq. 3) is printed with an apparent misprint (see
  the Source page).
* **Load balancing.** A work-weighted Morton space-filling curve (after
  Warren & Salmon 1993): keys by bit-interleaving integer block
  coordinates, a parallel bitonic sort of the keys only, equal-work cuts,
  then the data move; run only when the refinement changes. Compare
  Athena++'s Z-ordering and Castro's Morton option (Load balancing, above).
* **Cost and overhead** (§§2, 8). Identical blocks cost "rarely more than
  about 30%" extra memory. At fixed total work AMR scales worse than a
  uniform grid, because the guard-cell communication grows relative to the
  computation. AMR is faster than the uniform grid "beyond a refinement
  level of six (corresponding to a uniform mesh with 512 cells per side)",
  and only while "at most 60% of the mesh in two dimensions, or 40% in
  three dimensions" is maximally refined (Figs. 45–48).
* **Observed effects of refinement** (§§7.6–7.7). On the Emery Mach 3
  step the default thresholds 0.8/0.2 leave the slip line near the Mach
  stem unrefined, which changes the Kelvin–Helmholtz result; 0.6 refines
  it: "refinement criterion and thresholds need to be carefully considered
  for any particular problem". A Sedov front crossing a static jump from 7
  to 6 levels is broader and lower on the coarse side and emits a
  **reflected shock**, stronger the smaller the angle between the shock
  direction and the jump, while head-on crossing errors "appear small and
  well behaved"; forced jumps "should only be used for regions ... not
  critical". Enzo's "shock pool" finds no significant reflection for PPM
  (above): that is a shock crossing a refined region of subcycled patches,
  qualitative, and agrees with FLASH's head-on case; the reflection FLASH
  reports is for oblique incidence. A qualification by geometry, not a
  contradiction. It is the kind of coarse–fine shock error Berger &
  Colella describe (§6 of their paper; batch 6 above).

### Bearing on the open entries (batch 8)

* **Is time subcycling worth its cost?** FLASH's first version takes the
  global-step side, with reasons: per-level steps need extra memory for
  temporary solution copies and force an ordering of block advances that
  "can have a damaging effect on load balance"; the authors also list the
  arguments for subcycling (less accumulated diffusion on coarse blocks,
  with a counter-argument, and saved work). Nothing is measured, so the
  entry stays open.
* **Level-dependent derived quantities.** Not discussed.

## Open question: level-dependent derived quantities

Recorded at deep lint #1 as a contradiction and moved here at deep lint #3,
because only one side is stated: [Stone et al. (2020)](/sources/stone-2020.md), §1, argue that
covering each point by one level only avoids level-dependent derived
quantities (e.g. a temperature used by cooling) that afflict patch-based
AMR; the patch-based sources (Castro, Enzo, PLUTO-Chombo) do not discuss
the issue, and none quantifies it.

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
  design (Castro adds a multilevel gravity correction solve for it);
  [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2 (Quokka), and
  [Porth et al. (2019)](/sources/porth-2019.md), §4.1.5 (H-AMR's locally
  adaptive time stepping, claimed to give a factor 3–5) also subcycle;
  [Berger & Colella (1989)](/sources/berger-1989.md), §2, pp. 67–68 (the origin: one ratio in space and time "so the same explicit difference scheme is stable on all grids"; truncation errors of equal order; "the smaller time step of the fine grid is not imposed globally").
* One global step, with reasons: [Stone et al. (2026)](/sources/stone-2026.md)
  (AthenaK), [Shankar et al. (2023)](/sources/shankar-2023.md) (GRaM-X:
  subcycling serializes the levels) and [Zaghi et al. (2023)](/sources/zaghi-2023.md)
  (ADAM); see the batch-3 notes above;
  [Fryxell et al. (2000)](/sources/fryxell-2000.md), §2 (FLASH: extra memory for temporary copies, a block ordering that "can have a damaging effect on load balance"; the arguments for subcycling listed, nothing measured).
* No source measures the interpolation error or the cost trade-off on a
  common problem; the entry closes when one does.

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
11. [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §§2.2, 2.2.2, 2.2.4, 3.1.8, 3.2.4–3.2.5, 4–4.2 (arXiv v2).
12. [Stone et al. (2026)](/sources/stone-2026.md), §§2, 3, 5.1–5.2 (arXiv v1).
13. [Shankar et al. (2023)](/sources/shankar-2023.md), §§III, III A–III C, V (arXiv v2).
14. [Zaghi et al. (2023)](/sources/zaghi-2023.md), §§2.2, 3.1–3.2, App.
15. [Lesur et al. (2023)](/sources/lesur-2023.md), §§2.6, 3.4.
16. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §1 (arXiv v2).
17. [Rossazza et al. (2026)](/sources/rossazza-2026.md), §2.2.
18. [Bernardini et al. (2021)](/sources/bernardini-2021.md), §§3.1–3.2.
19. [Mathew & Federrath (2021)](/sources/mathew-2021.md), §§2.1, 2.3, 2.6, 3, 6.1, Table 1 (arXiv v2).
20. [Porth et al. (2019)](/sources/porth-2019.md), §§3, 4.1.5 (arXiv v2).
21. [Truelove et al. (1997)](/sources/truelove-1997.md), §2, Fig. 1.
22. [Berger & Colella (1989)](/sources/berger-1989.md), §§1–8, eqs. 1–3, Tables I–II, Figs. 2.1, 6.1–6.2.
23. [Fryxell et al. (2000)](/sources/fryxell-2000.md), §§2, 3.2, 7.6–7.7, 8.2–8.4, eqs. 1–3, Figs. 1–4, 41, 45–48.
