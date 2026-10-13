---
type: Definition
title: "Block-structured AMR"
description: "Adaptive refinement by a hierarchy of properly nested rectangular patches aligned to coarse grid lines, refined in space and time by a fixed ratio."
status: established
aliases: [SAMR, patch-based AMR, Berger-Colella AMR]
tags: [amr, block-structured, hierarchy, subcycling]
timestamp: 2026-10-13T00:00:00Z
---

# Block-structured AMR

Adaptive mesh refinement in which the refined region is a **hierarchy of
rectangular grid patches**: level $l{+}1$ patches have mesh spacing
$\Delta x_l / r$ for a fixed (even) refinement ratio $r$, with $r=2$ giving
the 2:1 interface. Defined by
[Berger & Colella (1989)](/sources/berger-colella-1989.md), refining the
earlier rotated-grid approach into grid-aligned patches specifically to make
conservation maintainable.

## Defining discipline (Berger–Colella formulation)

* **Alignment and proper nesting**: every patch starts and ends on corners
  of cells of the next coarser level; a level-$l$ cell is separated from any
  level-$l{-}2$ cell by at least one level-$l{-}1$ cell in each coordinate
  direction (a patch may span several parent patches).
* **Space–time refinement (subcycling)**: $\Delta t_l / \Delta x_l$ is
  constant across levels, so one coarse step corresponds to $r$ fine steps
  and the same explicit integrator runs unmodified on every level.
* **Finest-wins solution**: the solution at a point is the value on the
  finest patch containing it; covered coarse cells are overwritten by the
  conservative average (restriction $R$, [notation](/notation.md)) of their
  fine children.
* **Coupling operators**: patch boundary (ghost) values come from sibling
  patches or from the ghost-fill $\Gamma$ — bilinear interpolation in space,
  linear in time, from the parent level; interface conservation is restored
  by [refluxing](/methods/refluxing.md).
* **Automatic regridding**: error estimation flags cells, buffer zones of
  unflagged cells absorb feature motion between regriddings (finite
  propagation speed), and clustering heuristics emit new patches; nesting is
  enforced by construction.

**Variant: block-oriented SAMR.** Non-overlapping blocks of equal point
count, refined whole-block (possibly anisotropically), adjoining blocks
within a factor 2 per direction — less grid-management overhead and
simpler parallel data dependencies than patch hierarchies; the topology
preferred by the SBP-SAT community
([Nissen et al. (2014)](/sources/nissen-2014.md)).

**Variant: tree-based (octree) AMR.** The other major structured-AMR
flavor refines cell-by-cell on a tree — e.g. RAMSES's fully threaded tree
of "octs" (8-cell sibling groups)
([Fromang et al. (2006)](/sources/fromang-2006.md)) — rather than by
rectangular patches. Where 2:1 balance is enforced, the 2:1 coarse–fine
interface and its transfer operators are the same mathematical object in
both flavors (Knapp et al. enforce no 2:1 balance, and Hoppe et al. state
arbitrary resolution jumps, below); what changes
is granularity, data structure, and where interfaces occur (everywhere, at
single-cell granularity, in the tree case).

Within this corpus, this hierarchy — and specifically its $r=2$ coarse–fine
interface with $\Gamma$, $R$, and prolongation $P$ as the transfer
operators — is the structure on which every AMR divergence-constraint
question is posed. [Evans & Hawley (1988)](/sources/evans-hawley-1988.md)'s
claim that CT admits adaptive meshes naturally predates this framework and
concerns smoothly moving zones, not patch hierarchies.

**Frameworks and codes (added 2026-10-12).**
* *Patch hierarchies without parent–child links.* CASTRO, on BoxLib,
  needs only that the union of level-$(l+1)$ grids lie inside the union of
  level-$l$ grids. The proper-nesting buffer is two level-$l$ cells for
  $r = 2$ and one for $r = 4$, because the PPM stencil needs four ghost
  cells; $r$ is always 2 or 4, and every grid has an even cell count per
  direction. The level-0 step is the minimum over levels of each level's
  stable step times $h_0/h_l$ (§6.2). The paper sorts codes by these
  choices: FLASH (equal patches, one time step), RAGE (cell by cell, one
  step), ENZO and CASTRO (arbitrary patches, subcycling), with ENZO and
  FLASH imposing strict parent–child nesting ([Almgren et al. (2010)](/sources/almgren-2010.md), §§1, 6.1–6.2).
  **The PPM ghost-cell count is CASTRO's.** The PPM paper states no
  ghost-cell requirement. Its stencils are consistent with the count: an
  interface value uses two zones on each side, and flattening reaches
  further ([Colella & Woodward (1984)](/sources/colella-woodward-1984.md),
  eqs. 1.9, A.2, A.6; [PPM](/methods/ppm.md)).
* *Subcycling is a choice, not part of the definition.* AMReX supports
  level-by-level advance "with or without subcycling in time", or
  full-hierarchy strategies ([Zhang et al. (2019)](/sources/zhang-2019.md)). ADAM's 2023 compressible
  solver takes one global time step from the smallest cell ([Zaghi et al. (2023)](/sources/zaghi-2023.md), eq. 9).
* *Subcycling without time interpolation.* A GPU lattice-Boltzmann AMR
  fills **two** fine ghost layers once per coarse step, by linear or cubic
  spatial interpolation. The band absorbs the two fine substeps, so no
  temporal interpolation of ghost data is needed ([Jaber, Essel & Sullivan (2025)](/sources/jaber-essel-sullivan-2025.md), §4.1).
* *More tree-based variants.*
  * A cell-based Cartesian cut-cell tree, ordered along a
    [space-filling curve](/definitions/space-filling-curve.md) for partitioning and multigrid coarsening ([Aftosmis, Berger & Murman (2004)](/sources/aftosmis-berger-murman-2004.md)).
  * A block octree of identical Cartesian blocks with 2:1 balance, whose
    tree sits in a CPU hash map keyed by a Morton-type index while the
    field lives on the GPU ([Zaghi et al. (2023)](/sources/zaghi-2023.md), §2.2;
    [ADAM](/software/adam.md)).
  * A GPU-resident forest of block quadtrees and octrees, stored as integer
    ID lists with explicit neighbor links rather than a curve, with 2:1
    balance enforced at all times ([Jaber, Essel & Sullivan (2025)](/sources/jaber-essel-sullivan-2025.md), §§3.1–3.3).
  * A forest of element trees on an unstructured hybrid coarse mesh
    (t8code), where a pyramid refines into 6 pyramids and 4 tetrahedra
    rather than $2^d$ children, and only face neighbors are encoded. The
    paper defines no transfer operators and no 2:1 balance ([Knapp et al. (2026)](/sources/knapp-2026.md), §§2–3).
* *Multiresolution-driven block tree with local time stepping.* ALPACA,
  a CPU-only MPI code for compressible multi-phase flow, refines a binary,
  quad or octree of fixed-size blocks ("e.g. $32^3$" cells) with $r = 2$.
  * Parent nodes are kept, not only the leaves; their storage counts in the
    paper's compression metric.
  * Refinement is decided by Harten-type multiresolution rather than by
    error-estimation flags. Wavelet details, the difference between the
    fine data and its prediction $P$ from the coarse level, are set to zero
    below a "level-dependent threshold"; zero details coarsen, non-zero
    details refine. The threshold value, its level dependence, and the
    stencil and order of $P$ are not given. Averaging stated to be
    consistent with prediction is the registry round-trip $R P = I$, on cell
    averages.
  * The halo concept is said to keep the graded-tree property "even for
    arbitrary resolution jumps between neighboring blocks". No 2:1 limit
    is stated.
  * Coarser levels take larger steps, with the step readjusted after every
    finest-level step. Halo cells at a resolution jump are filled by
    prediction from the coarser level, applied to the right-hand side as
    well as the solution, and are then advanced by the same Runge–Kutta
    operator as the interior. The paper describes no temporal
    interpolation of ghost data. This is a third answer to the
    subcycling ghost problem, next to linear-in-time interpolation and the
    two-layer band above.
  * Conservation at resolution jumps rests on a flux correction applied at
    the last Runge–Kutta stage and stated only by citation
    ([refluxing](/methods/refluxing.md)).
  * Weak scaling to 512 nodes (24 576 cores) at efficiency "above 75%"
    (Fig. 20b reads about 0.74–0.75 for the shuffle executable);
    strong scaling is shown graphically to about $3\cdot10^4$ cores
    ([Hoppe et al. (2022)](/sources/hoppe-2022.md), §§5, 7.1, 9; Algorithms 1–3).

# Citations

1. [Berger & Colella (1989)](/sources/berger-colella-1989.md), §2–6.
2. [Fromang et al. (2006)](/sources/fromang-2006.md), §2.5.
3. [Nissen et al. (2014)](/sources/nissen-2014.md), §2.
4. [Almgren et al. (2010)](/sources/almgren-2010.md), §§1, 6.1–6.2.
5. [Zhang et al. (2019)](/sources/zhang-2019.md).
6. [Zaghi et al. (2023)](/sources/zaghi-2023.md), §2.2, eq. 9.
7. [Jaber, Essel & Sullivan (2025)](/sources/jaber-essel-sullivan-2025.md), §§3–4.
8. [Aftosmis, Berger & Murman (2004)](/sources/aftosmis-berger-murman-2004.md), §§2–4.
9. [Knapp et al. (2026)](/sources/knapp-2026.md), §§2–3.
10. [Hoppe et al. (2022)](/sources/hoppe-2022.md), §§5, 7.1, 9; Algorithms 1–3.
11. [Colella & Woodward (1984)](/sources/colella-woodward-1984.md), eqs. 1.9, A.2, A.6.
