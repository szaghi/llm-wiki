---
type: Method
title: "Hole cutting"
description: "Hole cutting removes from an overset grid the points that lie inside bodies or are made redundant by a finer overlapping grid; the page compares the surface-based tests of the Chimera papers, Cartesian hole maps, analytic shapes and object X-rays, tree, auxiliary-grid and GPU collision-detection cutters with flood fills, priority-driven classification, cut-cell clipping, and Chimera without holes."
status: established
aliases: [hole generation, blanking, hole-point identification, explicit hole cutting, Chimera hole cutting, cutting, hole profiling, object X-rays]
tags: [hole-cutting, domain-connectivity, overset-grid, chimera]
timestamp: 2026-11-02T15:27:00Z
---

# Hole cutting

Hole cutting is the step of [domain connectivity](/definitions/domain-connectivity.md)
that decides, on each component grid $G_k$ of an [overset grid](/definitions/overset-grid.md),
which points are **hole points** $\mathcal H_k$ ($\iota_k(\mathbf i)=0$ in the
[point classification](/definitions/point-classification.md)): points that fall inside a
solid body carried by another grid, outside the physical domain, or in a region that a
finer overlapping grid already resolves. The points of $G_k$ next to the hole then become
receptors $\mathcal R_k$ (the hole [fringe](/definitions/fringe-point.md)) and take their
values from the grid that cut the hole. Benek et al. (1983) introduced the operation with the
[Chimera](/definitions/overset-grid.md) scheme
([Benek et al. (1983)](/sources/benek-1983.md), "Holes"); the methods below differ in what
defines the hole boundary $\mathcal C$ (a grid surface, a closed body surface, an
approximation of it, a priority rule, or no surface at all) and in how a point is tested
against it. [Implicit hole cutting](/methods/implicit-hole-cutting.md), where holes are a
by-product of donor selection, has its own page.
[Sharma et al. (2021)](/sources/sharma-2021.md), §1, sort the explicit methods
by what the user supplies: analytic cutter shapes, a hole map with ray casting,
or meshes built with holes; implicit methods instead use a cell-wise criterion
or primitive volumes, and explicit cutting needs user input that becomes
impractical with many moving meshes.

## Why holes are cut

Benek et al. (1983) give two reasons: points of the containing grid $G_k$ can fall inside a
solid boundary of an embedded grid $G_{k'}$, hence outside the domain, and points can fall
inside a mesh embedded within $G_{k'}$, which the hierarchy of the paper forbids
(p. 374). Benek et al. (1985) add the cost argument: updating every point common to the two
grids by interpolation would need many interpolations, whereas cutting a hole leaves the
grids communicating only through their boundaries, the outer boundary of $G_{k'}$ and the
hole boundary of $G_k$ ([Benek et al. (1985)](/sources/benek-1985.md), "Hole Generation",
p. 323). Meakin & Suhs (1989) present hole cutting as what distinguishes Chimera from other
Schwarz-type overlapping decompositions: a body cuts an artificial boundary into a grid that
has no natural boundary there, and this two-way link with a fully embedded grid is what makes
computations with several moving bodies possible
([Meakin & Suhs (1989)](/sources/meakin-1989.md), §I, Figs. 1–2).

## Surface-based tests of the Chimera papers

**Hole boundary as a grid surface.** In both Benek papers the hole boundary $\mathcal C$ in
the containing grid is a level curve (2-D) or level surface (3-D) of the embedded grid, a
constant-index line or surface around the body (Benek et al. 1983, p. 375, Fig. 4; Benek et
al. 1985, p. 324). In the special case of a single embedded grid and an O-mesh that wraps
around it, the hole reduces to dropping the points inside an azimuthal level line (Benek et
al. 1983, p. 374).

**Point-in-curve tests.** Benek et al. (1983) give two tests for a point $\mathbf x$ of
$G_k$ (p. 375, Figs. 5–6). In the page-local symbols below, $\mathbf x_o$ is the mean of the
points defining $\mathcal C$, $R_{\max}$ the largest distance from $\mathbf x_o$ to
$\mathcal C$, $\mathbf x_c$ the point of $\mathcal C$ closest to $\mathbf x$ and $\mathbf n$
the outward unit normal of $\mathcal C$ at $\mathbf x_c$.

1. *Radius test.* If $\lvert\mathbf x-\mathbf x_o\rvert>R_{\max}$ the point is outside.
   Otherwise its polar angle $\theta$ about $\mathbf x_o$ is bracketed by two points of
   $\mathcal C$ at angles $\theta^\pm$ and radii $r^\pm$, and the distance to $\mathcal C$
   along the ray is approximated by
   $$r_c=r^-+\frac{r^+-r^-}{\theta^+-\theta^-}\,(\theta-\theta^-);$$
   the point is inside when $\lvert\mathbf x-\mathbf x_o\rvert\le r_c$. The authors call
   it "not particularly efficient", but such searches take "a miniscule amount" of the total
   solution time. The bracketing assumes that every ray from $\mathbf x_o$ meets
   $\mathcal C$ once, i.e. that $\mathcal C$ is star-shaped about $\mathbf x_o$; the
   authors state no such hypothesis *(compiler check, not in the sources)*.
2. *Closest-point normal test.* With $d=\mathbf n\cdot(\mathbf x-\mathbf x_c)$, the point
   is outside if $d>0$ and inside if $d\le 0$. The authors judge it more promising for
   three dimensions.

Benek et al. (1985) combine the two into one 3-D procedure in six steps (p. 324, Fig. 3,
stated in 2-D): build outward normals at the points of $\mathcal C$; choose a temporary
origin inside $\mathcal C$; set $R_{\max}$; test $\lvert\mathbf x-\mathbf x_o\rvert$ for
every point of $G_k$; for $\lvert\mathbf x-\mathbf x_o\rvert<R_{\max}$ form $d$; set the
IBLANK of the point from 1 to 0 if $d<0$. The radius test is thus only a pre-filter in 1985,
and the boundary case $d=0$ is classed as inside in 1983 and outside in 1985 (a convention
difference, not a disagreement).

**Hierarchy.** In both Benek papers only an embedded grid cuts a hole in its parent: the
hierarchy places each grid of level $\ell(k)+1$ wholly inside one grid of level $\ell(k)$,
with same-level grids disjoint (Benek et al. 1983, p. 374; Benek et al. 1985, p. 323; see
[grid hierarchy](/definitions/grid-hierarchy.md)). Rogers et al. (2003) recall how
PEGASUS relaxed this: version 1 let a grid cut holes only in a larger grid, with cutters of
specific topologies; version 2 removed the restrictions on interconnection; version 3 let any
number of surfaces of one grid cut a hole; version 4 let surfaces from several grids form one
hole ([Rogers et al. (2003)](/sources/rogers-2003.md), pp. 1037–1038; see
[PEGSUS and PEGASUS 4](/software/pegasus.md)). Noack (2005) organizes cutting by a tree of
bodies, with the rule that **siblings cut each other**: a body cuts every grid of a sibling
and of the sibling's descendants, and container bodies without grids structure the tree
([Noack (2005)](/sources/noack-2005.md), §II, Figs. 3–4).

**Fringe after the hole.** Once the hole is known, the points of $G_k$ outside
$\mathcal C$ that are nearest neighbours of hole points are flagged as hole-boundary points
and interpolated from the cutting grid (Benek et al. 1983, p. 375, Fig. 7c). Benek et al.
(1985) build a single fringe layer this way from a nearest-neighbour stencil and, to simplify
the solver, also set the IBLANK of these fringe points to 0, so that IBLANK $=0$ marks both
hole and fringe points there (p. 324, Fig. 4). Rogers et al. (2003) define a hole-fringe
point as any point that has a hole point as neighbour and let the user choose the number of
fringe layers $n_f$ (p. 1039). The detailed rules, including Noack's node- and cell-centred
variants, are on the [fringe-point](/definitions/fringe-point.md) page.

## Cartesian hole map with line of sight (PEGASUS 5)

Rogers et al. (2003) cut holes automatically from the flow-solver boundary conditions: every
solid-wall surface is a cutting surface, and the surfaces must form an air-tight closed set
(extra boundary conditions can close gaps). The parts come from J. Steger (private
communication) and Chiu & Meakin (1995), as cited (pp. 1038–1039, Figs. 2–3):

1. build a Cartesian mesh enclosing the solid surfaces;
2. mark the Cartesian elements that intersect the surface as **fringe elements**;
3. assume the corner elements are **outside** and paint inwards: any non-fringe element
   adjacent to an outside element is outside, until nothing changes;
4. mark every remaining element **inside**;
5. locate each grid point in its element: outside gives a field point, inside a hole point;
6. for a point in a fringe element, test for a clear **line of sight** to a neighbouring
   non-fringe element (the segment does not cross the surface inside the fringe element);
   the point takes the status of the element it can see.

Because no surface normal is used, the method accepts surface discontinuities. Several hole
maps (cutters) can be defined, each from a subset of the closed surfaces and with its own
extent and resolution. An input **OFFSET** blanks, in addition, every point within OFFSET
cells of a hole point; it fixes most failures of the automatic cutter (pp. 1042–1043). The
two failure modes reported are holes not cut inside very thin bodies (a trailing edge finer
than the hole map; fixed by OFFSET or a finer map) and wrong holes at curved walls where
overlapping surface grids define the surface ambiguously and tiny gaps fool the line-of-sight
test (fixed by naming a grid subset where no hole may be cut) (Boeing 777 section;
Conclusions). On the Boeing 777-200 landing configuration (79 meshes, 22.4 million points)
the case needed eight cutters, OFFSET 1 or 2 on about half the meshes and manual unblanking
in two regions; on the 30P30N airfoil the hole near the slat trailing edge came out too close
to it because the hole map lacked resolution (Fig. 9; see
[multi-element airfoils](/benchmarks/multi-element-airfoil.md)). Measured on an SGI R10K at
250 MHz, a typical 3-D problem blanks 5–15 % of the points, at 100–200 blanked points per CPU
second, and hole cutting takes about 30 % of the PEGASUS 5 run, averaged over the paper's
two cases ("Performance").

Lee & Baeder (2003) list the earlier alternatives as summarized by Meakin (2001), as they
recall it: mark-and-fill, surface normal vectors, ray casting and the hole-map method, and
the object X-rays of Meakin that combine a hole map with ray casting
([Lee & Baeder (2003)](/sources/lee-2003.md), "Existing Connectivity Method", p. 2). In
that two-step procedure the hole array is also "expanded or resized" for optimum overlap
before the fringe list is extracted, which is the role of
[overlap optimization](/methods/overlap-optimization.md).

[Chan (2009)](/sources/chan-2009.md), §7, reviews the NASA line of cutters as
background. The early PEGASUS used an expensive inside/outside test, with the
user naming each hole cutter and the grids it cuts; PEGASUS 5 automated most
of it with uniform Cartesian maps, with two stated weaknesses: occasional
robustness problems at component junctions with fairings, and large memory for
uniform maps when feature sizes span a wide range. Two methods of Meakin, as
recalled there, trade generality for speed in moving-body runs:

- **Analytic shapes** (c. 1991): bodies approximated by analytic shapes, so the
  point-in-shape test is very fast, but fitting shapes to complex bodies is
  "prohibitively difficult".
- **Object X-rays** (2001): a fine 2-D Cartesian map is laid over the body in
  one coordinate plane; from each map vertex a ray is cast normal to the plane
  and its pierce points with the body surface are stored; a query point is
  located in its map cell at once and declared inside or outside by comparing
  its normal coordinate with the stored pierce points. X-rays are used
  routinely in OVERFLOW 2 moving-body computations, but are generated by hand
  and the user lists the grids each X-ray cuts.

## Auxiliary-grid hole profiling with a donor-search test (PUNDIT)

[Roget & Sitaraman (2014)](/sources/roget-2014.md), §3.1, cut holes in
partitioned unstructured meshes from the boundary-condition input alone. For
each near-body mesh an auxiliary Cartesian grid of equal box-shaped
*sub-blocks* encloses its wall faces with a 1% margin; the sub-block of a point
follows by the same floor formula as Lee & Baeder's Cartesian donor cell
([donor search](/methods/donor-search.md)). The global box of each body is
subdivided until no sub-block overlaps both a wall face and an outer-boundary
face (bounding-box tests only). Hole sub-blocks are those that may overlap a
wall face plus those inside the hole, found by an *external* scan-line flood
fill seeded from an added outer layer of "out" sub-blocks, which avoids
choosing interior seeds and handles disconnected holes (Fig. 4: even a singly
connected wall can give a multiply connected sub-block hole). Only bounding
boxes and integer tags are communicated. The hole test then uses the donor
search: a point of body $B$ lying in a hole sub-block of another body $B'$ is a
hole point if no partition of $B'$'s mesh finds a donor for it. The argument
("a trivial observation") is that a point with no donor in a near-body mesh is
inside its hole or outside its outer boundary, and the sub-block construction
excludes the second case; the authors call the cut exact, tagging all and only
the points inside walls, and state that ray tracing would need the whole body
surface on every process. Hole profiling costs a negligible share of the
assembly in their tests (§6.1).

## Collision-detection cutting on GPUs

[Horne & Mahesh (2021)](/sources/horne-2021.md), §2, cut unstructured meshes in
three stages (from their earlier CPU method, cutting being Meakin's term as they
cite it): explicit **cutting volumes** (spheres, cylinders, object-oriented
boxes and others) placed around bodies remove redundant cells; a
**fine-detail cut** removes the remaining cells that intersect solid
boundaries (K-D trees and signed distances on CPUs; on GPUs a bounding volume
hierarchy over the cells plus the exact GJK overlap test for convex
polyhedra); a **"Forest-Fire" flood fill**, seeded from the cells that overlap the
solid boundaries, removes the cells deep inside bodies. Cutting both removes cells
outside the flow domain and reduces overlap while keeping complete coverage.
On GPUs the cutting kernels run $O(10)$ to $O(100)$ times faster than the CPU
method (§4.1; [parallel and GPU overset grid
assembly](/methods/parallel-overset-grid-assembly.md)).

## Tree-based approximation of the cutting surface (SUGGAR)

Noack (2005) approximates each body's faceted cutting surface by a recursive Cartesian
subdivision and tests the points of other grids against it; the octree version was described
in earlier papers that the source cites (Noack & Kadanthot 2002; Noack 2003) and is not
repeated (§II, §VII). The new option is a **binary tree**: a node is split in one direction
only, so the refinement can be anisotropic where an octree (quadtree in 2-D) over-refines,
e.g. a slat gap that is narrow chordwise but long spanwise. The refinement rule (§III): a
node is a candidate when it intersects the bounding box of a facet; the facet's box extents
are enlarged by a margin equal to one-thousandth of the box diagonal, so that facets aligned
with a Cartesian direction do not force endless refinement; a direction needs splitting when
the node's extent in it exceeds the enlarged facet extent; the split direction is chosen
cyclically $x\to y\to z$, starting after the parent's split direction. Without the cycling,
the first facet would drive refinement in one preferred direction to the detriment of the
others. Table 1 counts the nodes needed to refine to a surface in the unit square or cube:

| surface | binary tree | quadtree | octree |
|---|---|---|---|
| $x=0.8$ | 13 | 253 | 10,921 |
| $x+y=1$ | 835 | 709 | 31,753 |
| $x+y+z=1$ | 27,265 | — | 21,793 |

The binary tree saves memory where the surface aligns with the axes and costs a little
otherwise (§II). The resolution can vary: coarse where the wing is far from the separating
store, fine in the small pylon–store gap (§VIII, Figs. 11–12).

Noack argues that an approximate geometry is acceptable because a hole larger than the body
is often advisable: it removes part of the overlap and keeps the coarse background fringe
from interpolating near a resolved boundary layer, while small gaps need fine resolution to
cut no more points than necessary (§II). On the wing/pylon/store case (Table 2 prints a total of 26
structured grids and 3.64 million points but lists 25 rows; 2.6 GHz Pentium 4) building the binary trees took 261 s once and hole
cutting about 15 s per time step; on the C130 air drop (2 unstructured and 15 structured
grids, 4.85 million points) the tree took 14 s and hole cutting about 81 s per step (§VIII,
Tables 2–3; see [store separation](/benchmarks/store-separation.md)).

## Classification without cutting surfaces (CMPGRD)

Chesshire & Henshaw (1990) do not cut holes with surfaces. In the CMPGRD algorithm every point
first gets the highest grid number; for each boundary point of a grid that lies inside the
subdomain of another grid, the closest point of that other grid is marked exterior
($\iota=0$); an
iteration to a fixed point then lets each point try, in turn, to be interpolated from the
highest-numbered grid above it, to be a valid discretization point, or to be interpolated
from a lower grid, and marks it exterior when all fail. The exterior set grows from the seeds
and fills the regions outside the domain
([Chesshire & Henshaw (1990)](/sources/chesshire-1990.md), §3.2, Steps 1–3, pp. 16–21;
Figs. 10–11 trace the flags of a two-grid example). The holes produced depend on the
ordering of the grids, on the interpolation and discretization widths $q$ and $q_{\mathrm d}$
and on the minimum overlap (Fig. 9). The authors call the algorithm "fundamentally different"
from those of B. Kreiss and of Benek et al. (p. 14). It is described further on
[CMPGRD](/software/cmpgrd.md) and [overlap optimization](/methods/overlap-optimization.md).
Its successor Ogen ([Overture](/software/overture.md)) works the same way:
the physical boundaries mark exterior points unused, then the remaining points
are classified as discretization or interpolation points
([Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md), §3.1;
[Banks et al. (2016)](/sources/banks-2016.md), §4.1, where an annular grid
around a disk "cuts a hole" in a Cartesian fluid grid and trims the solid
Cartesian grid, §5.2).

## Chimera without holes

[Picard et al. (2021)](/sources/picard-2021.md), §3.2.2, deliberately cut no
hole: the geometric detail (a cylinder, a ramp) is meshed only in the patch and
"does not explicitly appear" in the substrate (§4.3), whose covered cells keep
being integrated while the patch receives only through its receptor layers. The
authors present this as a difference from the hole-cutting Chimera methods they
cite: no cell is deactivated and no grid is modified, and the covered substrate
cells are stated to have "no impact on the solution inside the patch" (§3.2.3).
The substrate thus integrates a flow through the region the body occupies in the
patch *(compiler check, not in the sources)*.

## Holes inside implicit operators

Cutting a hole into a grid whose discretization is implicit along lines needs
more than a mask. [Sherer & Scott (2005)](/sources/sherer-2005.md), §4.4,
Fig. 10, take holes from a grid-assembly code and insert one-sided boundary
closures of their compact differences and filters at every hole boundary,
decoupling the hole points by $\{0,1,0\}$ rows; the details are on [point
classification](/definitions/point-classification.md).

## Exact clipping at a minor-grid boundary

Wang (1995) cuts the hole with the boundary $\Gamma_{k\mid k'}$ of the minor grid lying
inside the major grid and clips the major-grid cells exactly against it: cells crossed by
the boundary are **cut cells**, cells in the region covered by the minor grid are **hole
cells**, excluded from the computation, and the rest are normal cells
([Wang (1995)](/sources/wang-1995.md), §3.1, Fig. 3). The overlap is thereby turned into a
patched interface; the purpose is conservation, treated on
[conservative overset interface](/methods/conservative-overset-interface.md). The geometry
step costs about one flow-solver step in 2-D and is done once for grids that do not move
(§6).

## Hole cutting for moving bodies

When bodies move, holes move and must be recut every time step. Meakin & Suhs (1989) state
that in static PEGASUS applications hole definition is typically the most time-consuming
task, and restrict the search for the holes at time level $n+1$ to the points on either side
of the hole boundaries at level $n$; this imposes a one-cell-per-step limit on hole motion
(§II, Fig. 3; details on [moving overset grids](/methods/moving-overset-grid.md)). Noack
(2005) builds the cutting trees once, in each body's own frame, and transforms the query
points instead of the trees (§VII). Chan (2009), §7, gives per-step cutting as the
reason for Meakin's fast analytic-shape and X-ray cutters. Henshaw & Schwendeman (2006),
§3.1, recompute the Ogen classification every step from the previous one, and Horne &
Mahesh (2021), §2, keep the bounding volume hierarchy of each rigidly moving partition and
update only its boxes ([moving overset grids](/methods/moving-overset-grid.md)).

## Hole cutting in 2022 moving-body solvers

[Hedayat et al. (2022)](/sources/hedayat-2022.md) cut holes explicitly by ray tracing against user-defined surfaces and prefer it to implicit hole cutting for grids that move every step, stating without measurement that implicit hole cutting costs about an order of magnitude more (§2.2.2). [Zhao et al. (2022)](/sources/zhao-2022.md) make the background cells inside the immersed body inactive and surround them with two acceptor layers (§II C). [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) inactivate background cells whose centres lie inside the surface of the foreground cells five layers from the foreground's outer boundary (§2). [Li & Wang (2022)](/sources/li-2022.md) use implicit hole cutting with a supplementary pass during conflict resolution and report hole maps of $35^3$ against $115^3$ for their earlier code (§3, §6). [Delcour et al. (2022)](/sources/delcour-2022.md) give no hole-cutting details for their commercial-code Chimera mesh.

## Wall-distance criteria

Wall-distance-based implicit hole cutting on unstructured grids, with its parallel advancing-front and exact pre-classification variants ([Xiao et al. 2023](/sources/xiao-2023.md); [Oh et al. 2024](/sources/oh-2024.md)), is on [wall-distance hole cutting](/methods/wall-distance-hole-cutting.md).

## Qualifications

- The cost statements are not comparable. Benek et al. (1983) measure hole searches against
  the whole 2-D flow solution; Meakin & Suhs (1989) measure hole definition within static
  PEGASUS; Rogers et al. (2003) measure hole cutting (about 30 %) against the PEGASUS 5 run,
  where interpolation takes about 50 %.
- Roget & Sitaraman's test declares a point inside the wall when it finds no donor in the
  near-body mesh, so the exactness they claim is relative to the discrete near-body mesh
  and to the donor search near the wall *(compiler check, not in the sources)*; the paper
  supports it by a logical argument, not a proof.
- Horne & Mahesh's GJK test is exact for convex polyhedra; the authors state that "the
  majority" of cells and faces are convex and describe no treatment of the others.
- None of the sources ingested here proves that a point-in-surface test is correct for every
  geometry. Benek et al. state their tests without hypotheses; Rogers et al. require an
  air-tight surface and report the thin-body and ambiguous-surface failures above.
- Lee & Baeder (2003) argue that the explicit procedures are unnecessary: with
  [implicit hole cutting](/methods/implicit-hole-cutting.md) the holes come from cell
  selection and are, in their words, not affected by imperfections of the wall surface
  (Abstract).

# Citations

- [Benek et al. (1983)](/sources/benek-1983.md) — "Holes" and "Boundaries", pp. 374–375, Figs. 4–7: hole as a level curve, radius and normal tests, hole-boundary points.
- [Benek et al. (1985)](/sources/benek-1985.md) — "Hole Generation", pp. 323–324, Figs. 2–4: six-step 3-D procedure, IBLANK, single-layer fringe.
- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §I, Figs. 1–2 (holes as the Chimera distinction); §II DCF, Fig. 3 (moving holes).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §3.2, Steps 1–3, pp. 14–21, Figs. 9–11.
- [Wang (1995)](/sources/wang-1995.md) — §3.1, Fig. 3; §6.
- [Lee & Baeder (2003)](/sources/lee-2003.md) — "Existing Connectivity Method", pp. 2–3.
- [Rogers et al. (2003)](/sources/rogers-2003.md) — pp. 1037–1039 (history, hole map, line of sight, Figs. 2–3); pp. 1042–1044 (OFFSET, 777 case, performance, failure modes).
- [Noack (2005)](/sources/noack-2005.md) — §II–III (body hierarchy, binary tree, Table 1); §VII; §VIII, Tables 2–3.
- [Sherer & Scott (2005)](/sources/sherer-2005.md) — §4.4, Fig. 10 (holes in compact operators).
- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) — §3.1 (Ogen hole cutting, per-step update).
- [Chan (2009)](/sources/chan-2009.md) — §7 (PEGASUS cutters, analytic shapes, object X-rays).
- [Roget & Sitaraman (2014)](/sources/roget-2014.md) — §3.1, Fig. 4 (hole profiling, flood fill, exactness); §6.1.
- [Banks et al. (2016)](/sources/banks-2016.md) — §4.1, §5.2 (Ogen cutting each step).
- [Picard et al. (2021)](/sources/picard-2021.md) — §3.2.2, §4.3 (no hole cutting).
- [Horne & Mahesh (2021)](/sources/horne-2021.md) — §2 (cutting volumes, fine-detail cut, flood fill); §4.1.
- [Sharma et al. (2021)](/sources/sharma-2021.md) — §1 (explicit vs implicit hole cutting).
- [Hedayat et al. (2022)](/sources/hedayat-2022.md) — §2.2.2.
- [Zhao et al. (2022)](/sources/zhao-2022.md) — §II C.
- [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) — §2.
- [Li & Wang (2022)](/sources/li-2022.md) — §3, §6.
- [Delcour et al. (2022)](/sources/delcour-2022.md) — §3.3.
- [Xiao et al. (2023)](/sources/xiao-2023.md) — §2.
- [Oh et al. (2024)](/sources/oh-2024.md) — Abstract.
