---
type: Method
title: "Overlap optimization"
description: "Overlap optimization reduces the overlap of an assembled overset grid to what interpolation needs, keeping the better-suited points active and interpolating the rest; the page covers the CMPGRD deletion and conversion steps, PEGASUS 5's finest-points-kept algorithm with its cell-difference parameter, and the size criteria of implicit hole cutting."
status: established
aliases: [hole-size optimization, overlap minimization, overlap reduction, donor selection, donor quality]
tags: [domain-connectivity, hole-cutting, overset-grid, interpolation]
timestamp: 2026-11-02T11:26:00Z
---

# Overlap optimization

Once holes are cut and donors found, an [overset grid](/definitions/overset-grid.md) usually
overlaps far more than interpolation requires, and in the overlap a coarse grid may be kept
active where a finer one is available. **Overlap optimization** changes the
[point classification](/definitions/point-classification.md) so that the overlap shrinks
towards the minimum the interpolation stencils need, and so that, of two overlapping grids,
the better-suited one keeps the active points $\mathcal D_k$ while the other's points become
receptors $\mathcal R_k$ or hole points $\mathcal H_k$. It needs a rule for which points are
better suited, which is also the rule for choosing among several candidate donors. The
chunk-1 sources give three such rules: grid order (CMPGRD), relative cell size with a
cell-difference parameter (PEGASUS 5), and smallest cell volume
([implicit hole cutting](/methods/implicit-hole-cutting.md)).

## What the overlap must contain

Benek et al. (1983) state the constraint: the points of the difference approximation used in
the interpolation must be defined on the donor grid, so the overlap must contain them, and
heuristically it must be large enough that the boundaries forming it have little influence
on the solution where interpolation occurs
([Benek et al. (1983)](/sources/benek-1983.md), "Overlap", p. 375). Their examples overlap
generously (the cylinder grids from the sixth to the thirtieth radial point) or by 5 points
(the airfoil O-meshes). Benek et al. (1985) state only the requirement of enough overlap to
interpolate the outer boundary of the embedded grid from its parent
([Benek et al. (1985)](/sources/benek-1985.md), p. 323).

Chesshire & Henshaw (1990) make the requirement precise. A point is a valid interpolation
point if it can be interpolated to the required order, with a sufficiently centred stencil,
from discretization or interpolation points of another grid; the overlap $d$ is measured
between the innermost receptors of the two grids, not between the grid edges; and the
interpolation width $q$ needed for a given accuracy depends on whether $d$ shrinks with $h$
([Chesshire & Henshaw (1990)](/sources/chesshire-1990.md), §3.2 p. 16, §5.3; see
[interpolation order and overlap requirements](/results/interpolation-order-requirement.md)).
With [explicit interpolation](/definitions/explicit-and-implicit-interpolation.md), stencils
may contain discretization points only, which costs more overlap; implicit interpolation lets
stencils contain receptors and needs less overlap and fewer points (§5.2, p. 28). A centred
three-point discretization needs one line of receptors, a five-point one two lines (§3.2,
p. 14).

## CMPGRD: grid order, deletion and conversion

In CMPGRD the user orders the component grids so that higher-numbered grids cover parts of
lower-numbered ones. During classification each point first tries to be interpolated from the
highest grid above it, then to be a discretization point, then to be interpolated from a lower
grid (Step 3). The optimization proper follows (§3.2, Steps 4–5, pp. 19–20):

1. mark the donor-stencil points of every receptor that interpolates from a lower grid as
   needed (Step 4);
2. going from the lowest to the highest grid, **delete** receptors that are needed neither by
   a discretization point of their own grid nor by a receptor of another grid (they become
   exterior, $\iota=0$), **convert** receptors that can be interior points into discretization
   points, and mark the points of higher grids that this grid's receptors need (Step 5).

The algorithm seeks a composite grid with a minimum number of interpolation points. Its
parameters are the interpolation width, the discretization width, the minimum allowable
overlap and the grid order; changing the order changes the grid, and every grid, even the
top one, loses points (Fig. 9). The authors state that if a valid grid exists for one order,
one "should result for all orderings", and say explicitly that this is not proved (p. 16).
They also advise roughly equal grid spacings where grids overlap (§3.1, p. 11). The null grid,
all points unused, is formally valid and is avoided by enough overlap (p. 16).

## PEGASUS 5: finest points kept

Rogers et al. (2003) run an automatic overlap optimization after the automatic
[hole cutting](/methods/hole-cutting.md) and after the outer-boundary points and their donors
are known. The premise is that donor and receptor cells should be of similar size, so the
finest mesh points are kept and coarser ones interpolated from them
([Rogers et al. (2003)](/sources/rogers-2003.md), "Overlap Optimization", pp. 1040–1041,
Figs. 4–5):

1. for a pair of meshes, each interpolates all its points from the other; only the
   interpolations of the **coarser** points, those interpolated from finer regions of the
   other mesh, are kept;
2. an interpolated point that belongs to a donor cell is removed from the interpolated set;
3. after steps 1–2 for all mesh pairs, each interpolated point keeps a single donor, the one
   with the smallest cell-difference parameter where several remain; the remaining points are
   field points.

In the 1-D illustration with three meshes, a stretched mesh A, a mesh B stretched the other
way and a uniform mesh C coarser than both, mesh C ends with no active field point in the
overlap. Which size measure decides "coarser" is not printed beyond the parameter below.
The optimization takes about 5 % of the PEGASUS 5 run ("Performance"). Rogers et al. call it
"unique" among automatic attempts to resize holes, citing Chiu & Meakin (1995) and Henshaw's
Ogen (1998) as the other attempts. On the 30P30N airfoil it enlarges the effective hole beyond
the hole the Cartesian map cut (Fig. 9; see
[multi-element airfoils](/benchmarks/multi-element-airfoil.md)). The OFFSET input, which
blanks every point within OFFSET cells of a hole point, adds a user-controlled enlargement
(pp. 1042–1043).

**Cell-difference parameter (CDP).** To choose among candidate donors, PEGASUS 5 replaces the
prioritized link lists of earlier versions with a "qualitative measure" of the difference in
size and orientation between the receptor's cell (the "boundary cell") and the donor cell (the
"interpolation cell"). In page-local symbols, $L^{\mathrm R}_m$ and $L^{\mathrm D}_m$ are the
largest $m$-components of the four diagonals of the receptor and donor cells, and
$B^{\mathrm R}$, $B^{\mathrm D}$ the volumes of the smallest Cartesian boxes enclosing them.
As printed (p. 1040),

$$\mathrm{CDP}=\sum_{m=1}^{3}\frac{L^{\mathrm R}_mB^{\mathrm R}-L^{\mathrm D}_mB^{\mathrm D}}{L^{\mathrm R}_mB^{\mathrm R}},$$

and the text says its values "vary from 0 (the best) to very large values"; the donor with
the smallest value is kept.

## Implicit hole cutting: smallest volume

Lee & Baeder (2003) select, among all cells enclosing a point, the one with the smallest
volume $J^{-1}$, and keep the point active when its own cell is the smallest; overlap
outer-boundary points take volume $+\infty$ and always receive. They state that the match in
size between the first fringe layer and its donors is then always the best available, so no
separate hole optimization or overlap minimization, no user parameter and no grid priority is
needed ([Lee & Baeder (2003)](/sources/lee-2003.md), p. 3, sub-item 1 p. 5). They consider
and set aside other quality measures (aspect ratio, orientation, PEGASUS 5's parameter, cited
from its 2002 conference version), and distinguish their near-wall parameter `jHoleImmune`,
which forces wall layers to be donors, from the OFFSET hole enlargement of PEGASUS 5 (p. 8).
They recommend interpolating a single layer of outer-boundary points, but as many layers as
possible at hole fringes (p. 12), and state that cubic interpolation tolerates a larger
spacing ratio between interpolating grids, usually about 2:1 (p. 4).

## Over-sized holes

Noack (2005) reaches the same end by cutting holes larger than the body: it removes part of
the overlap and keeps coarse background fringe points from interpolating near a resolved
boundary layer; in small gaps the cut must be fine to remove no more points than needed
([Noack (2005)](/sources/noack-2005.md), §II). Noack also notes that the node-based fringe
marking for cell-centred solvers needs more overlap than the neighbour-based one, and that a
zeroth-order donor stencil needs the least (§IV, §VI; see
[fringe points](/definitions/fringe-point.md)).

## Agreement across the sources

Three sources prefer similar donor and receptor sizes: Chesshire & Henshaw's
advice of about equal spacings in the overlap, Rogers et al.'s finest-points-kept rule and
CDP, and Lee & Baeder's smallest-volume rule with a tolerated ratio of about 2:1. None of them
gives an error analysis for the size rule; the accuracy requirement that is derived, the
interpolation width as a function of the overlap, is Chesshire & Henshaw's.

## Qualifications

- **CDP as printed.** Each term of the printed sum equals
  $1-L^{\mathrm D}_mB^{\mathrm D}/(L^{\mathrm R}_mB^{\mathrm R})$ with positive quantities,
  so each term is below 1 and the sum below 3, and it is negative whenever the donor cell is
  the larger. For a donor cell twice as large in every diagonal component, with 8 times the
  box volume, each term is $1-16=-15$ and the sum $-45$ *(compiler check, not in the
  sources)*. The printed formula therefore cannot range from 0 upwards as the text says, and
  "smallest CDP kept" would favour the largest donors, against the stated aim of similar
  cell sizes. The paper prints no other form; pages should not rely on the printed formula.
- Lee & Baeder's "automatically optimum" refers to the volume criterion; in their own Fig. 7
  case, where the volume criterion would make the wall layer receive, they add the
  forced-donor parameter `jHoleImmune` (p. 8).
- CMPGRD's order independence is an unproved conjecture of its authors.
- Rogers et al. state the similar-size premise from "experience" (p. 1040); the claim that
  fringe level 2 "can produce more accurate solutions" (p. 1039) is also given without
  evidence.

# Citations

- [Benek et al. (1983)](/sources/benek-1983.md) — "Overlap", p. 375, Fig. 7a; test-problem grids pp. 376–377.
- [Benek et al. (1985)](/sources/benek-1985.md) — "Hole Generation", p. 323.
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §3.1, p. 11; §3.2, pp. 14–20, Fig. 9; §5.2, p. 28; §5.3.
- [Lee & Baeder (2003)](/sources/lee-2003.md) — pp. 3–5, 8, 12; Fig. 7.
- [Rogers et al. (2003)](/sources/rogers-2003.md) — "Cell Difference Parameter", p. 1040; "Overlap Optimization", pp. 1040–1041, Figs. 4–5; pp. 1042–1043 (OFFSET, Fig. 9); "Performance".
- [Noack (2005)](/sources/noack-2005.md) — §II, §IV, §VI.
