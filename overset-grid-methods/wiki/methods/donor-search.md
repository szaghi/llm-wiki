---
type: Method
title: "Donor search"
description: "Donor search finds, for each receptor of an overset grid, the enclosing cell of another grid and the receptor's local coordinates in it; the page synthesizes pruning by hierarchy and bounding boxes, start-cell trees, stencil walking and jumping with Newton inversion, inside tests, the polyhedral neighbour walk, and measured costs."
status: established
aliases: [donor cell search, stencil walking, stencil jumping, gradient search, interpolation stencil search, nearest-neighbour search, neighbour walk]
tags: [donor-search, domain-connectivity, overset-grid, unstructured]
timestamp: 2026-11-02T11:26:00Z
---

# Donor search

**Donor search** is the step of [domain connectivity](/definitions/domain-connectivity.md)
that, for a receptor $(\mathbf i,k)$ at $\mathbf x^k_{\mathbf i}$, finds a donor grid $k'$, a
cell of $G_{k'}$ that encloses the point, and the receptor's position in it: either the
parameter coordinates $\mathbf r'=\mathbf d_{k'}^{-1}(\mathbf x^k_{\mathbf i})$ or the local
coordinates $\mathbf s\in[0,1]^{n_d}$ in the donor cell. From these the
[inter-grid interpolation](/methods/inter-grid-interpolation.md) weights
$\alpha_{\mathbf j}$ on the donor stencil $\mathcal S_{\mathbf i}$ follow. Lee & Baeder (2003)
split the task into three problems: whether a point is inside a given cell, the search path
from a start cell to the enclosing cell, and the local coordinates $\mathbf s$, and remark
that all three, including the search direction, can be solved from $\mathbf s$ alone when
$\mathbf s$ is not too large ([Lee & Baeder (2003)](/sources/lee-2003.md), "Existing
Connectivity Method", p. 2). Every method below is a combination of pruning, a start cell, a
walk and a local inversion.

## Which points and which grids are searched

- **Hierarchy.** Benek et al. (1985) give, as the main advantage of their embedding
  [hierarchy](/definitions/grid-hierarchy.md), that it restricts the search for donors to
  the parent and children of a grid
  ([Benek et al. (1985)](/sources/benek-1985.md), p. 323).
- **Receptors only, or every point.** The Chimera papers search only for the outer-boundary
  and hole-fringe points (Benek et al. 1983 and 1985). Rogers et al. (2003) search every point
  of every grid in all $n_g(n_g-1)$ ordered donor/receptor pairs, because the later
  [overlap optimization](/methods/overlap-optimization.md) may turn interior points into
  receptors; they note that the number of pairs grows as $n_g^2$, so search efficiency is at
  a premium ([Rogers et al. (2003)](/sources/rogers-2003.md), "Boundary Point
  Interpolation", p. 1039). [Implicit hole cutting](/methods/implicit-hole-cutting.md) also
  tests every point (Lee & Baeder 2003). In CMPGRD the classification iteration asks, for
  each point, whether it can be interpolated from a given grid, highest grid first
  ([Chesshire & Henshaw (1990)](/sources/chesshire-1990.md), §3.2, Step 3).
- **Bounding boxes.** CMPGRD first rejects points outside the bounding rectangle of $G_{k'}$
  (§3.2, p. 21). PEGASUS 5 tests whether two grids intersect through several Cartesian and
  rotated Cartesian boxes and skips disjoint pairs, then discards the receptor points that
  lie outside the donor grid's boxes (p. 1039).
- **Non-overlapping pairs.** Lee & Baeder test the boundary points of a grid first; if none
  finds a donor in the partner grid and the partner is not embedded, the interior points are
  not searched in that grid (sub-item 2, pp. 5–6).
- **Time coherence.** For moving bodies Meakin & Suhs (1989) limit the search at time level
  $n+1$ to a band around the hole and inter-grid boundaries of level $n$
  ([Meakin & Suhs (1989)](/sources/meakin-1989.md), §II DCF; see
  [moving overset grids](/methods/moving-overset-grid.md)).

## Start cell

- **Closest point, then neighbours.** Benek et al. (1983) find, for the first boundary point
  of an embedded grid, the closest point of the containing grid by search, and locate the
  following points by a "nearest neighbor" search procedure whose details they leave to the
  companion paper of Steger, Dougherty & Benek (1983)
  ([Benek et al. (1983)](/sources/benek-1983.md), "Interpolation Points", p. 375,
  Fig. 7b).
- **Nearest-point walk.** CMPGRD moves from an initial guess to any closer neighbouring grid
  point until it reaches a local minimum of the distance; if that minimum lies on the grid
  boundary, it searches all boundary points globally and repeats the local walk. This finds
  the nearest point "provided the transformation … is sufficiently smooth" (§3.2, p. 21).
- **Continuity.** Lee & Baeder start each walk from the donor of the previously tested point,
  or, after an unsuccessful search, from the last cell next to the boundary before the walk
  left the grid (stored with negative indices to flag the failure); the start cells are stored
  per ordered grid pair. The interior sweeps alternate forward and backward in each
  direction with the time-step counter, so successive test points are neighbours, and the
  boundary sweep is kept continuous on O-H, C-H and one-wall topologies. The first point of
  each grid starts at the corner cell; the authors judge an accelerated search for it "not
  really warranted" and use no tree structure (sub-item 3, pp. 6–7; Fig. 5). For a
  Cartesian donor grid the cell is direct: with $\mathbf x_0$ the lowest corner point and
  $\Delta x_m$ the spacings (page-local symbols),
  $$i_m=\left\lfloor\frac{x_m-x_{0,m}}{\Delta x_m}\right\rfloor+1,\qquad m=1,\dots,n_d$$
  (Eq. (1), printed with the Fortran `INT`).
- **Trees.** PEGASUS 5 builds an alternating digital tree (Bonet & Peraire 1991, as cited)
  for each mesh at start-up and queries it for a cell close to the receptor (p. 1039). SUGGAR
  starts its walks from a separate octree, refined to the size of the solid-boundary faces
  and filled with candidate start cells, distinct from the hole-cutting tree
  ([Noack (2005)](/sources/noack-2005.md), §V). Lee & Baeder list tree structures
  (polygonal mapping tree, alternating digital tree) as the usual accelerators of the
  search path and avoid them (p. 2).

## Walk and local inversion on structured grids

**Newton inversion.** CMPGRD obtains $\mathbf r'=\mathbf d_{k'}^{-1}(\mathbf x)$ by Newton
iteration on the mapping, started from the nearest grid point (§3.2, p. 21). PEGASUS 5 inverts
the trilinear map of the current cell by Newton iteration for the three local coordinates
$\mathbf s$; if all lie in $[0,1]$ the cell encloses the point, otherwise $\mathbf s$ gives
the direction and distance of a jump to another cell, and the process repeats. Newton
typically needs 3–5 inversions, and 2–3 jumps suffice when the start cell is close and the
grid smooth; a jump is limited to 5 cells per computational direction, and jumps across C-grid
cuts and periodic O-grid boundaries are detected, which matters because a tree start can be
close in physical space and far in index space (p. 1039). Rogers et al. call stencil jumping
and its variants "the most commonly used approaches for finding donor cells": stencil
walking (also "gradient search") moves one cell per step, jumping several. Benek et al.
(1985) require that the receptor lie inside the donor cell, $0<s_m<1$, for their trilinear
formula, but do not describe how the cell is found (p. 324).

**Inside test and walk without inversion.** Lee & Baeder first test, assuming planar faces,
whether the point lies on the inner side of all six faces of the current cell; the faces
that fail give the next search direction. The test needs right-handed index axes. Only for the
enclosing cell do they solve for $\mathbf s$, by Newton iteration on a Hermite tricubic
interpolant of the coordinates, started from the trilinear estimate (more efficient than
$s_m=0.5$ for high-order interpolation; 0.5 is kept on coarser multigrid levels with linear
interpolation). If a coordinate leaves $[0,1]$, the walk moves to the neighbour cell, but only
after the third Newton iteration, since Newton usually converges in about three
(`FindDonor`, pp. 9–11; Fig. 10).

**Safeguards.** Lee & Baeder's walk checks for a return to a previously tested cell (with
curved faces the planar test can cycle; after a preset number of steps the indices are stored
and the cell first repeated is accepted, the cubic coordinate interpolation then deciding;
Fig. 11), for a cut across a concave boundary (called one of the most difficult tasks, with
visual identification as the crude fallback), for crossing into a solid body, and for crossing
the periodic cut of O- and C-grids; a walk that leaves the grid returns a failure. Cells
within two cells of a grid boundary are rejected as donors for the 6-point stencil unless the
point is flagged for a low-order formula near a wall (pp. 9–11).

## Polyhedral and unstructured grids

For node-centred structured and simplex grids SUGGAR uses the parametric or barycentric
coordinates of the search (Noack 2003, as cited); for cell-centred solvers the receptor
location is the cell centre (§V–VI). For general polyhedral cells, whose faces are arbitrary,
possibly non-planar polygons, barycentric or parametric coordinates are not available and
Noack (2005) uses a **neighbour walk** (§V). Each face is given a plane with average normal
$\bar{\mathbf n}_f$ through a face point $\mathbf p_f$ chosen behind all other face points,
and a thickness $\epsilon_f=\max_i\bar{\mathbf n}_f\cdot(\mathbf x_i-\mathbf p_f)$ over the
face vertices $\mathbf x_i$ (page-local symbols). A point $\mathbf x$ is behind the face if
$\bar{\mathbf n}_f\cdot(\mathbf x-\mathbf p_f)<0$, above it if the value exceeds
$\epsilon_f$, and within it otherwise; it lies in the cell if it is within, or on the cell
centre's side of, every face. Otherwise the segment from the cell centre to $\mathbf x$ is
intersected with the cell's faces, each triangulated from its edges to its centroid, and the
walk moves into the neighbour across the intersected face. Face geometry is computed only for
the faces met and cached.

## Moving frames

SUGGAR builds its search trees once, in each body's untransformed frame, and transforms a query
point from its local frame to the global frame and then to the frame of the target body, so
the search always runs in the target's coordinates (§VII).

## Cost

| source | hardware | measured |
|---|---|---|
| Rogers et al. (2003), "Performance" | SGI R10K, 250 MHz | on average 2–3 donor cells found per grid point, about 10,000 donor cells per CPU second, about 5 % of the donors found kept; interpolation about 50 % of the PEGASUS 5 run |
| Noack (2005), §VIII, Tables 2–3 | Pentium 4, 2.6 GHz | donor-search octree 16 s once and donor search about 39 s per step (wing/pylon/store, 3.64 million points); 79 s once and about 53 s per step (C130 air drop, 4.85 million points) |
| Lee & Baeder (2003), Example | Alpha 21264, 667 MHz | whole implicit-hole-cutting connectivity, 39 grids, about 2.5 million points: about 45 s; linear instead of cubic interpolation saves 20–25 % |
| Chesshire & Henshaw (1990), §3.2 | — | whole composite-grid construction estimated at $O(n_g^2N_{\mathrm{pts}})$ operations |

The rows measure different things (search alone, search per time step, whole assembly) and
are not comparable across codes.

## Qualifications

- Lee & Baeder print the planar inside test as $\mathbf r_i\cdot(\mathbf n_i\times\mathbf
  r_i)>0$ for the six faces (p. 10), with $\mathbf n_i$ the inward face normal and
  $\mathbf r_i$ the vector from a face base point to the tested point. A scalar triple product
  with a repeated vector vanishes for every point, so the printed test can never pass
  *(compiler check, not in the sources)*. Their Fig. 10 shows the test as
  $(\mathbf p\times\mathbf q)\cdot\mathbf r>0$ with $\mathbf n=\mathbf p\times\mathbf q$
  formed from two edge vectors $\mathbf p$, $\mathbf q$ of the face, i.e.
  $\mathbf r_i\cdot\mathbf n_i>0$.
- Rogers et al.'s prevalence claim for stencil jumping is stated without a survey or
  citation of one.
- None of the sources proves convergence of the walks; CMPGRD's nearest-point walk assumes a
  smooth mapping, and Lee & Baeder give their safeguards without proof.

# Citations

- [Benek et al. (1983)](/sources/benek-1983.md) — "Interpolation Points", p. 375, Fig. 7b.
- [Benek et al. (1985)](/sources/benek-1985.md) — p. 323 (hierarchy restricts the search); p. 324 (receptor inside the trilinear cell).
- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §II DCF, Table 1.
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §3.2, Step 3 and p. 21.
- [Lee & Baeder (2003)](/sources/lee-2003.md) — p. 2, Eq. (1); sub-items 2–3, pp. 5–7, Fig. 5; `FindDonor`, pp. 9–11, Figs. 10–11; Example, p. 12.
- [Rogers et al. (2003)](/sources/rogers-2003.md) — "Boundary Point Interpolation", p. 1039; "Performance".
- [Noack (2005)](/sources/noack-2005.md) — §V–VII; §VIII, Tables 2–3.
