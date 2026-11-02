---
type: Method
title: "Implicit hole cutting"
description: "Implicit hole cutting (Lee and Baeder 2003) replaces cutting by body surfaces with cell selection: every point is tested against all overlapping grids and the smallest enclosing cell wins; the page gives the rule, its algorithm and cost, its unstructured partitioned form in PUNDIT and TIOGA, the shrinking fringe gap it causes, and its relation to CMPGRD and PEGASUS 5."
status: established
aliases: [IHC, implicit hole-cutting, cell-selection connectivity, smallest-cell donor selection]
tags: [hole-cutting, domain-connectivity, overset-grid, unstructured, rotorcraft]
timestamp: 2026-11-02T15:26:00Z
---

# Implicit hole cutting

**Implicit hole cutting** (IHC) is the [domain-connectivity](/definitions/domain-connectivity.md)
method of Lee & Baeder (2003), first reported in 2-D (Lee & Baeder 2002, as they cite it) and
extended to 3-D in the source ingested here
([Lee & Baeder (2003)](/sources/lee-2003.md), Abstract and "Implicit Hole Cutting",
pp. 3–4). It replaces the usual two steps of overset assembly, explicit
[hole cutting](/methods/hole-cutting.md) with walls as cutters followed by a
[donor search](/methods/donor-search.md) for the fringe list, with a single
**cell-selection process**: every point of every grid $G_k$, boundary and interior, is tested
against all overlapping grids $G_{k'}$; among all cells that enclose it, the one with the
smallest volume $J^{-1}$ is the optimum donor; the point keeps its own value when its own
cell is already the smallest. Holes appear as a by-product, because grids are built with
cells that shrink towards the walls, so near a body the body grid wins and the background
grid's points there become receptors. The authors' summary: IHC is "a cell-selection process,
not a wall-cutting process".

## Selection rule

For a point $(\mathbf i,k)$ at $\mathbf x^k_{\mathbf i}$, let the candidate donor cells be the
cells of the grids $G_{k'}$, $k'\ne k$, that contain $\mathbf x^k_{\mathbf i}$, and let
$J^{-1}_{\min}$ be the smallest volume among them, attained in grid $k'_{\min}$. The
receptor's own volume is $J^{-1}$ at $(\mathbf i,k)$ for an interior point and $+\infty$ for a
point on an overlap (interpolated) outer boundary, i.e. a boundary point with no physical
boundary condition. Then (sub-item 1, p. 5)

$$\iota_k(\mathbf i)=\begin{cases}-k'_{\min} & \text{if } J^{-1}_{\min}<J^{-1}(\mathbf i,k),\ \text{or a donor is forced},\\ 1 & \text{otherwise.}\end{cases}$$

Overlap outer-boundary points therefore always receive, and interior points receive only when
a smaller cell exists. The volume $J^{-1}$ is already a solver quantity, so the criterion
costs nothing extra (p. 3). Other quality measures (aspect ratio, orientation, the
cell-difference parameter of PEGASUS 5, which the authors cite from its 2002 conference
version) are not used (p. 5). The walls act through the cell sizes, or through a grid
topology with a fixed wall index; the first usually suffices.

Lee & Baeder describe the outcome as keeping "only the best" cells in a multiply overlapped
region, with the rest becoming hole points (p. 3). Points inside a body that find a donor are
interpolated harmlessly; points with no valid donor are left in place and insulated by the
fringe layers that receive from valid donors (sub-item 4, pp. 7–9).

## Claims made for the method

Lee & Baeder (2003) state (p. 3):

- holes are "both automatically optimum and not affected by any imperfection on the wall
  surface": thin bodies, surface mismatch and openings cannot make the cut fail, and orphans
  caused by such failures disappear; [orphans](/definitions/orphan-point.md) from
  insufficient overlap must still be checked;
- the match in cell size between the first fringe layer and its donors is always the best
  available, so no separate [overlap optimization](/methods/overlap-optimization.md), no user
  parameter (offset, wall distance, donor quality) and no grid priority or
  [hierarchy](/definitions/grid-hierarchy.md) is needed;
- holes are cut simultaneously around bodies and around flow-feature grids (vortex, shock and
  refinement grids) (Figs. 1, 15);
- the same structured flow solver runs in overset mode with only an extra array dimension
  for the grid number.

**Hole points need not be blanked.** The authors argue that the solver can update hole points
like any other point: by hyperbolicity, invalid values cannot reach the field region within
one time step $\Delta t$ if the distance information travels in $\Delta t$ is smaller than the
thickness of the thinnest fringe, which must also enclose the body completely (Abstract;
pp. 3, 7–9). Fringe thickness, propagation speed and $\Delta t$ decide the condition; "first
order checks of many cases" put common $\Delta t$ well within it. They extend the argument to
implicit methods, which they say "mimic" global parabolic behaviour, especially with Newton
subiterations, provided the values at invalid points are not very large. The mask is then
needed only for contour plots, for blanking hole points in the residual of steady
convergence checks and in the residual of implicit Newton subiterations; unsteady explicit
computations need it only for plots (p. 3). Beyond those checks the paper gives no proof
and no measurement.
[Benek et al. (1983)](/sources/benek-1983.md) and
[Benek et al. (1985)](/sources/benek-1985.md) instead multiply the rows of the implicit
operator by the 0/1 IBLANK and reset the diagonal of a zeroed row to unity, and
[Meakin & Suhs (1989)](/sources/meakin-1989.md) multiply the time step and dissipation terms
of their factored scheme by $i_b$, so that hole points are frozen
([point classification](/definitions/point-classification.md)). The two positions concern
different settings, recorded under Qualifications.

## Algorithm

The driver loops over receptor grids and calls `BoundaryConnect` (overlap-boundary points)
and `InteriorConnect` (interior points), either grid by grid or all boundary calls first; both
call `FindDonor` for each candidate donor grid (pp. 4–5). Only a serial, single-level version
is outlined; the code runs inside the flow solver or standalone.

**Boundary points first; non-overlapping pairs.** For a grid pair (receptor $G_k$, partner
$G_{k'}$) the boundary points of $G_k$ are tested first. If none finds a donor in $G_{k'}$
and $G_{k'}$ is not wholly embedded in $G_k$ (checked with one point near the middle of
$G_{k'}$), the pair does not overlap and the interior points of $G_k$ are not tested against
$G_{k'}$. The result is stored in a symmetric pair matrix with three values: overlapping,
not overlapping, and overlapping without mutual cutting. The third value marks grids that
share part of a solid wall (O-H, C-H or one-wall topologies), which must not cut each other
yet must still interpolate their boundaries; storing "not overlapping" for them would make
the partner skip even its boundary interpolation. Shared walls are detected from the donor
grids of boundary test points just above the wall. The authors state that this keeps the
cost of interior points flat as $n_g$ grows (sub-item 2, pp. 5–6; Figs. 3–4).

**Search continuity.** Each stencil walk starts from the donor of the previously tested
point, stored per ordered grid pair; the interior loops alternate between forward and
backward sweeps in each direction with the time-step counter, so consecutive test points
stay neighbours. No tree structure is used; details on
[donor search](/methods/donor-search.md) (sub-item 3, pp. 6–7; Fig. 5).

**Near-wall protection.** A user parameter (`jHoleImmune`) makes the cells within a given
wall-normal index layer donors regardless of their volume and keeps the points there from
being receptors. It handles the unusual case where the smallest wall cell is larger than all
receptor cells (Fig. 7, value 5), and saves test points on viscous grids. Lee & Baeder state
that it is not the OFFSET hole enlargement of PEGASUS 5, and that hole expansion is
irrelevant to IHC. For untrimmed near-body grids that pass through a body (collar grids,
secondary surface features, surface refinement grids) it is set to 1 when their interior
points are tested; such grids are identified by hand (p. 8; Figs. 7–9).

**Interpolation.** The solution is interpolated with a Hermite cubic monotone formula on a
6-point stencil per direction, the coordinates with a Hermite tricubic interpolant; the first
two cells next to each grid boundary therefore cannot be donors, and 4- or 2-point formulas
are accepted near walls. All grid-boundary points are interpolated before the hole-fringe
points, which removes the coupling between them (pp. 4, 10–11; see
[inter-grid interpolation](/methods/inter-grid-interpolation.md)).

## Cost

The single 3-D demonstration is a half-span quad tilt rotor-like model with 39 grids and about
2.5 million points (blades, nacelles, nested vortex-tracking grids, wings, fuselage,
background). Connectivity took about 45 s of CPU on an Alpha 21264 at 667 MHz; linear instead
of cubic interpolation cut the time by about 20–25 % (Example, p. 12; Figs. 14–15). No flow
solution, accuracy or convergence study is reported; the 2-D results are in the earlier paper.

## Resolution-based selection on partitioned unstructured meshes

[Roget & Sitaraman (2014)](/sources/roget-2014.md), §2.1 and §3.5, use the same
criterion on unstructured meshes without naming it implicit hole cutting: the
donor of a query point is its candidate donor cell of *finest resolution*
(nominally the cell volume $\lvert V_c\rvert$; for a node, the average volume
of the cells sharing it), and a non-hole point is a field point when its own
resolution is the finest among itself and its candidates, a receptor of the
finest candidate otherwise (Fig. 12). Field points are thereby chosen so that
the overlap is minimal (Fig. 2). Three things differ from Lee & Baeder's
version:

- **holes are cut, not inferred.** A point is a hole point only if it lies in a
  hole sub-block of another body's auxiliary grid and finds no donor in that
  body's mesh ([hole cutting](/methods/hole-cutting.md)); the resolution rule
  decides only between field and receptor;
- **mandatory receptors.** Points within a stencil-dependent number of cells of
  an outer boundary or a hole point always receive, which plays the role of
  Lee & Baeder's infinite volume for overlap-boundary points *(compiler check,
  not in the sources)*;
- **donor quality.** A donor cell may not contain receptor vertices; conflicts
  are resolved by turning points into field points, and a pathological
  conflict produces an [orphan](/definitions/orphan-point.md) (§3.5).

Candidate donors are searched only in meshes of a *different body* (§3.2), so
two meshes of the same body never interpolate from each other.

## Fringe gap under implicit hole cutting

TIOGA, which [Sharma et al. (2021)](/sources/sharma-2021.md) cite to Roget &
Sitaraman and to Brazell et al., applies (§1 and Fig. 4) implicit
hole cutting in the ExaWind wind-farm stack: the nodes of a preset number of
cells inward from each outer boundary are mandatory fringe, and a preset number
of nodes beyond them are kept as field points on both meshes so that the
fringe gap $d$ is nonzero (a zero gap gives a singular system). Since both
counts are in cells, $d$ shrinks with the mesh size, $d\propto h$; keeping $d$
fixed in physical distance is called impractical on unstructured meshes. Sharma
et al. draw the consequence from Chesshire & Henshaw's rule: with $d\propto h$,
linear interpolation ($q=2$) no longer preserves second-order accuracy for the
elliptic pressure equation, and they measure the degradation (§3.1, §4.1.1;
[interpolation-order requirement](/results/interpolation-order-requirement.md)).
Lee & Baeder's version has the same property, since its fringe is defined by
cell layers too *(compiler check, not in the sources)*.

[Horne & Mahesh (2021)](/sources/horne-2021.md), §1, recall an earlier GPU
assembly of Chandar et al. with implicit cutting based on axis-aligned bounding
boxes, for one static overset mesh on a single GPU.

## Relation to other assembly methods

- **CMPGRD.** The composite-grid algorithm of Chesshire & Henshaw (1990) also uses no cutting
  surfaces: exterior points are seeded next to physical boundaries and grow during an
  iterative classification. The choice among overlapping grids is made by grid order (each
  point first tries to interpolate from the highest-numbered grid), not by cell size, and the
  authors advise roughly equal spacings where grids overlap
  ([Chesshire & Henshaw (1990)](/sources/chesshire-1990.md), §3.1 p. 11, §3.2 pp. 16–21;
  see [hole cutting](/methods/hole-cutting.md)).
- **PEGASUS 5.** Rogers et al. (2003) also search donors for every point of every grid,
  because their overlap optimization may turn interior points into receptors, and they keep
  the same principle, finest points kept and coarser ones interpolated. The difference is the
  order: PEGASUS 5 first cuts holes explicitly with a Cartesian hole map, then optimizes the
  overlap, and selects among donors by its cell-difference parameter
  ([Rogers et al. (2003)](/sources/rogers-2003.md), pp. 1039–1041; see
  [overlap optimization](/methods/overlap-optimization.md)).
- **Over-sized holes.** Noack (2005) reaches a similar end by cutting holes larger than the
  body, so that coarse background fringes do not interpolate near a resolved boundary layer
  ([Noack (2005)](/sources/noack-2005.md), §II).

## Later uses and cost judgements

[Li & Wang (2022)](/sources/li-2022.md) take Roget & Sitaraman's implicit hole cutting into a multiple-solver framework and add a supplementary implicit hole cutting during conflict resolution (§3, Appendix A). [Hedayat et al. (2022)](/sources/hedayat-2022.md) judge it about an order of magnitude more expensive than explicit cutting for grids re-assembled every step, without a measurement (§2.2.2). [Chandar & Sitaraman (2022)](/sources/chandar-2022.md) run on overset meshes assembled in this way and note that donor stencils of RBF interpolation (at least 9 donors in 2-D) widen the search (§3.7.1).

## Wall distance as the criterion

Wall distance as the selection criterion, and its cost, are developed on [wall-distance hole cutting](/methods/wall-distance-hole-cutting.md): [Xiao et al. (2023)](/sources/xiao-2023.md) compute it with a parallel advancing-front algorithm, [Oh et al. (2024)](/sources/oh-2024.md) exactly and before the donor search.

## Qualifications

- **Must hole points be excluded from the solution update?** (Recorded as a qualification at
  the first deep lint, in agreement with
  [point classification](/definitions/point-classification.md): a difference of setting and
  of mechanism, not a conflict between sources.) Benek et al. (1983), p. 374, and Benek et al.
  (1985), p. 323, require hole points to be excluded because they lie outside the
  computational domain, and they and Meakin & Suhs (1989), §II, build the exclusion into an
  implicit approximate-factorization operator with a single fringe layer (Benek et al. 1985,
  p. 324, Fig. 4). Lee & Baeder (2003), pp. 3, 7–9, also keep invalid values away from the
  field points, but by insulation instead of blanking: hole points may be updated provided
  the hole fringe completely encloses the body, is thicker than the distance information
  travels in one $\Delta t$, and the values at invalid points are not very large; they extend
  the argument to implicit methods with Newton subiterations and still blank hole points in
  residuals. The positions rest on different hypotheses (a one-layer fringe without a
  thickness condition; a thick fringe), and no source ingested here tests an unblanked update under
  the Chimera papers' hypotheses or a blanked one under Lee & Baeder's. Meakin & Suhs's rule
  that a hole point must not become a field point without first being interpolated (§II,
  Fig. 3) concerns hole motion, not the update, and Lee & Baeder do not address it.
- The "automatically optimum" claim refers to the volume criterion. In the paper's own Fig. 7
  case the smallest wall cell is larger than all receptor cells, so the volume criterion alone
  would make the wall layer receive, and the authors add the `jHoleImmune` parameter (p. 8).
- The resolution criterion of Lee & Baeder and Roget & Sitaraman is the cell volume
  alone; neither source discusses anisotropic cells (stretched boundary-layer cells of
  small volume but large extent), and Roget & Sitaraman state no minimum overlap beyond
  the mandatory-receptor depth, which they do not quantify.
- Lee & Baeder print the face test of `FindDonor` in a form that is identically zero (p. 10);
  the test of their Fig. 10 is given on [donor search](/methods/donor-search.md).

# Citations

- [Lee & Baeder (2003)](/sources/lee-2003.md) — Abstract; "Implicit Hole Cutting", pp. 3–4; `BoundaryConnect`/`InteriorConnect` sub-items 1–4, pp. 4–9, Figs. 3–9; `FindDonor`, pp. 9–11; Example, p. 12, Figs. 14–15.
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §3.1, p. 11; §3.2, pp. 14–21.
- [Rogers et al. (2003)](/sources/rogers-2003.md) — "Boundary Point Interpolation", p. 1039; "Cell Difference Parameter" and "Overlap Optimization", pp. 1040–1041.
- [Noack (2005)](/sources/noack-2005.md) — §II.
- [Roget & Sitaraman (2014)](/sources/roget-2014.md) — §2.1, Fig. 2 (resolution-based types); §3.2 (other-body query points); §3.5, Fig. 12 (decision logic, donor quality).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — §1, Fig. 4 (TIOGA fringe, $d\propto h$); §3.1, §4.1.1.
- [Horne & Mahesh (2021)](/sources/horne-2021.md) — §1 (Chandar et al., as recalled).
- [Benek et al. (1983)](/sources/benek-1983.md) — p. 374 (holes must be excluded); p. 375, Eqs. (2)–(3) (IBLANK in the implicit operator).
- [Benek et al. (1985)](/sources/benek-1985.md) — p. 323 (holes must be excluded); p. 324, Fig. 4 (single fringe layer); p. 325 (IBLANK in the "standard tri-diagonal algorithm").
- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §II, Eq. (2) (IBLANK in the factored operator); §II, Fig. 3 (hole-motion rule).
- [Li & Wang (2022)](/sources/li-2022.md) — §3, Appendix A.
- [Hedayat et al. (2022)](/sources/hedayat-2022.md) — §2.2.2.
- [Chandar & Sitaraman (2022)](/sources/chandar-2022.md) — §3.7.1.
- [Xiao et al. (2023)](/sources/xiao-2023.md) — §2.
- [Oh et al. (2024)](/sources/oh-2024.md) — Abstract.
