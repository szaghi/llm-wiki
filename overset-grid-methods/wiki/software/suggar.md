---
type: Software
title: "SUGGAR"
description: "Noack's stand-alone overset grid assembler for moving-body simulation (2005): structured, unstructured and general polyhedral grids for node- and cell-centred solvers, binary-tree Cartesian hole cutting, a body hierarchy in which siblings cut each other, cell-centred fringe and donor-weight options, and per-step assembly coupled to solver and motion code through FIFOs, with timings."
status: established
aliases: ["Structured, Unstructured, and Generalized overset Grid AssembleR"]
tags: [software, domain-connectivity, hole-cutting, unstructured, moving-grid]
timestamp: 2026-11-02T11:28:00Z
---

# SUGGAR

SUGGAR (Structured, Unstructured, and Generalized overset Grid AssembleR) is
an overset grid assembly program, separate from the flow solver, built for
moving-body simulations ([Noack 2005](/sources/noack-2005.md), §I). It
produces the [domain connectivity](/definitions/domain-connectivity.md)
information of a composite grid made of structured, unstructured
(triangle/tetrahedron, prism) and general polyhedral component grids, for
node-centred and for cell-centred flow solvers: the receptor points
$\mathcal R_k$ with their donor members and weights, and the hole points
$\mathcal H_k$. Assembly proceeds in four phases: hole cutting, fringe
identification, donor search, donor stencil and weights (§§II–VI). The
companion library DiRTlib (Donor interpolation Receptor Transaction library,
Noack's ref. 20, a separate paper) performs the solver-side operations; this
page covers the assembler.

Noack (2005, §I) places SUGGAR among existing tools: the
[PEGASUS family](/software/pegasus.md) as the structured mainstay, used for
moving bodies through scripts, with [PEGASUS 5](/software/pegasus-5.md) "not
applied to moving body problems"; Beggar and [DCF3D](/software/dcf3d.md)
with assembly integral to the solver; the Overture library with static and
dynamic overset grids; a Tohoku University tetrahedral solver with integral
overset assembly. Earlier papers documented SUGGAR's octree hole cutting and
its node-centred assembly of structured and simplex grids (Noack's refs. 18,
19); the 2005 paper adds the items below.

## Contributions of the 2005 paper

**Binary-tree hole cutting (§§II–III).** Each body's faceted hole-cutting
surface $\mathcal C$ is approximated by a recursive Cartesian subdivision,
against which points of other grids are tested (procedure of refs. 18–19, as
for an octree). An octree refines every box into eight, so it over-refines in
some directions; the binary tree splits a box in one direction only. The
refinement rule: a node intersecting the bounding box of a facet is a
candidate; each facet's bounding-box spans are enlarged by one thousandth of
the box diagonal (so that facets aligned with a Cartesian direction do not
trigger excessive refinement); a direction needs refinement if the node's
span exceeds the enlarged facet span; the split direction cycles
$x\to y\to z$, starting after the parent's direction, and the first direction
needing refinement is split. Without cycling, an early facet drives excessive
refinement in one direction. Table 1 counts nodes needed to resolve a plane:

| Surface in the unit square/cube | binary tree | quadtree | octree |
|---|---|---|---|
| $x=0.8$ | 13 | 253 | 10921 |
| $x+y=1$ | 835 | 709 | 31753 |
| $x+y+z=1$ | 27265 | — | 21793 |

Noack summarizes: a significant memory saving where surfaces align with the
Cartesian axes and "a small penalty otherwise". Hole cutting may use coarse
resolution in some places and fine resolution in small gaps (§VIII). Cutting
a hole larger than the body is called "often advisable", to keep coarse
background receptors away from a resolved boundary layer (§II). See
[hole cutting](/methods/hole-cutting.md).

**Body hierarchy (§II, Figs. 3–4).** The geometry is a tree of bodies
(container bodies without grids allowed), with grids attached to the leaves.
The rule is that **siblings cut each other**; when a body cuts a sibling, it
cuts every grid in the sibling's subtree. Example: Wing cuts Pylon grids;
Wing+Pylon cuts all Store grids. This differs from the containment
[hierarchy](/definitions/grid-hierarchy.md) of the 1983–1985 Chimera papers,
which governs which grid receives from which; Noack's tree governs which
body cuts which grids.

**Fringe marking (§IV, Figs. 5–7).** Receptors are INNER fringe (next to
holes) or OUTER fringe (at grid boundaries flagged as overlap boundaries;
any boundary without a boundary condition is set as overlap automatically),
each at levels 1 and 2 ($n_f=2$).
- Node-centred (as in ref. 19): nodes of a cell having a hole node become
  INNER 1, then nodes of cells having an INNER 1 node become INNER 2;
  OUTER 1/2 likewise from the outer boundary nodes.
- Cell-centred, neighbour based (for least-squares gradient reconstruction,
  as in Cobalt and HYB3D): face neighbours of hole cells become INNER 1, their
  neighbours INNER 2.
- Cell-centred, node based (for the Taylor-series reconstruction of USM3D,
  which needs node values averaged from all surrounding cells): marks
  through nodes, giving a wider fringe and "more overlap" than the neighbour
  based rule.
Fringe depth is thus solver dependent. See
[fringe points](/definitions/fringe-point.md).

**Donor search on general polyhedra (§V).** Parametric or barycentric
coordinates do not exist for arbitrary polyhedra, so SUGGAR walks from a
start cell, taken from a separate octree refined to the size of the
solid-boundary faces, toward the query point. Each face (a possibly
non-planar polygon) gets an averaged normal, a reference point behind all
face vertices and a "thickness" (the largest normal offset of its vertices);
a point is behind, within or above the face accordingly, and lies in the
cell if it is within or on the inner side of every face. Otherwise the
segment from the cell centre to the point is intersected with the cell's
faces, each triangulated from its edges to its centroid, and the walk
continues into the neighbour across the intersected face. Face geometry is
computed lazily and cached. See [donor search](/methods/donor-search.md).

**Cell-centred donor stencils and weights (§VI).** The donor stencil is the
donor cell plus its face neighbours (about twice the extent of a
node-centred stencil, Fig. 8; fewer members at boundaries, worst case a
corner tetrahedron with all but one face on boundaries). Weights are linear
and normalized to sum 1, with options: zeroth order (weight 1 on the donor
cell); the Laplacian weights of USM3D, optionally clipped to $[0,2]$ before
normalization, falling back to zeroth order when all vanish; the unweighted
least squares of HYB3D, which degenerates when member centres are coplanar
or collinear (Fig. 9) and must then be reduced in dimension; and, under
development, barycentric weights on the Delaunay tetrahedron of cell centres
(donor cell and its node neighbours) containing the receptor. Results with
HYB3D and USM3D showed least-squares weights can be non-monotone with respect
to donor values, to be handled by the solver or DiRTlib (no data shown). See
[inter-grid interpolation](/methods/inter-grid-interpolation.md).

**Moving-body support (§VII, Fig. 10).** Hole-cutting and donor-search trees
are built once, in each body's untransformed frame; grids are never moved.
Per-body transforms are absolute in time and hierarchical (child relative to
parent), so a fin can move relative to a store that moves relative to the
aircraft; a query point is mapped local → global → target-body frame.
SUGGAR runs as its own process: a motion controller (e.g. a six-degree-of-
freedom code) writes transforms to a FIFO, SUGGAR assembles and signals, the
solver reads the new connectivity, advances one step and writes time, forces
and moments for the controller. Blocking FIFOs synchronize the processes;
all must share one shared-memory machine and only one parallel solver
process can talk to a FIFO. See
[moving overset grids](/methods/moving-overset-grid.md).

SUGGAR can also write a structured-plus-unstructured system as one general
polyhedral composite grid (§VIII).

## Demonstrations and timings

No flow solutions or accuracy measurements are given; the demonstrations
show cut geometry, cut planes, times and memory (§VIII).

| Case | Grids | Points | Setup | Per step | Memory |
|---|---|---|---|---|---|
| Wing/pylon/finned store, prescribed store motion | structured; 25 listed, "26" in the totals | 3,639,804 (printed total) | 283 s: 6 s read, 261 s binary trees, 16 s donor octree | 15 s hole cutting + 39 s donor search + 10 s output | ≈1.0 GB |
| C130 with parachute and cargo box, prescribed motion of chute and cargo | 2 unstructured (prism/tet) + 15 structured | 4,846,230 points, 10,687,568 cells | 256 s reading and orienting cells + 14 s binary tree + 79 s donor octree (printed total 335 s) | 81 s hole cutting + 53 s donor search + 71 s ASCII output | ≈1.8 GB |

Both cases ran on a 2.6 GHz Pentium 4 desktop with 3 GB of memory
(§VIII). A parallel option for hole cutting and donor search exists but
was not used. The wing/pylon/store case is on
[store separation](/benchmarks/store-separation.md).

## Qualifications

- Table 2's 25 rows sum to 3,108,363 points and 2,899,400 cells, while the
  totals row prints "26 structured, 3639804, 3411400"; the differences are
  exactly $81^3$ points and $80^3$ cells, i.e. one $81\times81\times81$ grid
  missing from the listed rows *(compiler check, not in the sources)*.
- The C130 setup components print as 256, 14 and 79 s with "a total setup
  time of 335 seconds"; they sum to 349 s *(compiler check, not in the
  sources)*.
- The printed node-based cell-centred fringe procedure (§IV, steps 1–5)
  uses INNER FRINGE 1 in step 5 but no step assigns it; the omission is in
  the print.
- The over-cutting advice (holes larger than the body) is a stated design
  choice; it runs opposite to the minimum-overlap aim of
  [implicit hole cutting](/methods/implicit-hole-cutting.md) and
  [overlap optimization](/methods/overlap-optimization.md), but no source
  compares the two on the same case.

# Citations

- [Noack (2005)](/sources/noack-2005.md) — §I (purpose, other tools, PEGASUS 5 not applied to moving bodies, DiRTlib); §II and Figs. 1–4 (binary tree, body hierarchy, over-cutting); §III and Table 1 (refinement criterion, node counts); §IV and Figs. 5–7 (fringe marking); §V (polyhedral donor search); §VI and Figs. 8–9 (donor stencils and weights, non-monotonicity); §VII and Fig. 10 (moving-body support, FIFOs); §VIII, Tables 2–3, Figs. 11–15 (demonstrations, timings, memory).
