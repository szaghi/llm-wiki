---
type: Definition
title: "Fringe (receptor) points and overlap width"
description: "Receptor points — the hole-fringe and outer-boundary points that take interpolated values — how many layers of them a discretization needs, the overlap they require (Benek's heuristic, Chesshire's overlap d, the fringe gap of implicit assembly, Yin–Yang buffer), the fringe rules of SUGGAR, TIOGA and PUNDIT, and the fringe-thickness condition of implicit hole cutting."
status: established
aliases: [receptor point, fringe point, interpolation point, intergrid boundary point, IGBP, hole-boundary point, hole-fringe point, outer-boundary point, interpolated boundary point, recipient point, receiver, fringe level, overlap width, acceptor, acceptor cell, ghost cell, reconstruction cell, mandatory receptor, fringe gap]
tags: [domain-connectivity, interpolation, overset-grid]
timestamp: 2026-11-02T15:07:00Z
---

# Fringe (receptor) points and overlap width

A **receptor point** $(\mathbf i,k)\in\mathcal R_k$ is a point of grid $G_k$
that the solver does not update but sets by
[inter-grid interpolation](/methods/inter-grid-interpolation.md) from a donor
stencil $\mathcal S_{\mathbf i}$ of an overlapping grid $G_{k'}$; receptors are
the artificial boundaries through which the components of an
[overset grid](/definitions/overset-grid.md) communicate. Two kinds are
distinguished by every founding source: **hole-fringe points**, the layers of
non-hole points that surround a hole, and **outer-boundary points**, points on
a grid boundary that carries no physical boundary condition
([Benek et al. (1983)](/sources/benek-1983.md), p. 375, Fig. 7;
[Rogers et al. (2003)](/sources/rogers-2003.md), Fig. 1;
[Noack (2005)](/sources/noack-2005.md), §I, §IV). The number of receptor layers
is the **fringe level** $n_f$, and the room the receptors and their donor
stencils need is the **overlap**. "Fringe", "receptor", "interpolation point",
"intergrid boundary point" and "recipient" are synonyms across the sources
(see the vocabulary table on [point
classification](/definitions/point-classification.md)).

## Definitions in the sources

- Benek et al. (1983), p. 375: after the hole points inside the cutting curve
  $\mathcal C$ are found, the nearest neighbours of hole points lying outside
  $\mathcal C$ constitute the boundary of the embedded grid inside its parent and
  are interpolated from the embedded grid; the outer boundary of the embedded grid is
  interpolated from its parent.
- [Benek et al. (1985)](/sources/benek-1985.md), p. 324, Fig. 4: a point with
  IBLANK $=1$ whose nearest-neighbour search stencil (a $3\times3$ block in the 2-D
  figure) contains a hole point is a **fringe point**; its index joins the list of
  boundary points to be interpolated, and it is also set to IBLANK $=0$. One
  layer results ($n_f=1$).
- [Meakin & Suhs (1989)](/sources/meakin-1989.md), §I: **interpolated (hole)
  boundary points** form the border between field and hole points and are
  treated as inter-subdomain boundaries.
- Rogers et al. (2003), "Automation…": a hole-fringe point is any point that has a
  hole point as a neighbour; outer-boundary points are min/max index surfaces not
  specified as flow-solver boundary conditions, found automatically from the
  OVERFLOW boundary-condition input.
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md), §3.2: an
  **interpolation point** is any point that is not a valid discretization point
  but can be interpolated to the required order; receptors arise both at
  physical-boundary-induced holes and at the "interior boundaries" of components.
- [Kageyama & Sato (2004)](/sources/kageyama-2004.md), §II: the border points of
  each Yin–Yang component (e.g. the first index line) receive interpolated
  values, the "horizontal" or "internal" boundary condition; there are no holes
  in the basic grid, only outer-boundary receptors.
- [Chan (2009)](/sources/chan-2009.md), §7, Fig. 1: fringe points are "one or
  more layers of grid points that are located at a grid boundary where no
  boundary conditions are specified, or at a hole boundary"; Fig. 1 separates
  hole-boundary from outer-boundary fringe points.
- [Roget & Sitaraman (2014)](/sources/roget-2014.md), §2.1, §3.5: a **mandatory
  receptor** is a point within a number of cells, set by the breadth of the
  discretization stencil, of an outer-boundary node of a near-body mesh or of a
  hole point; other receptors arise where a finer donor exists (the depth is
  not quantified in the paper).
- [Picard et al. (2021)](/sources/picard-2021.md), §3.2.1: the receptors are
  **ghost cells**, not integrated, set every step from the other grid and used
  only for the fluxes at the faces of the adjacent integrated ("sending")
  cells; the exchange is symmetric between patch and substrate.
- [Horne & Mahesh (2021)](/sources/horne-2021.md), §2, call them
  *reconstruction* cells (cells bordering cut cells or on the outer edges of
  overset meshes) and their donors reconstruction partners;
  [Wang et al. (2021)](/sources/wang-2021.md), §III A, *acceptor* cells, in a
  layer of a few cells on the outer surface of the rotating grid and around the
  hole in the background (widths not stated).

## How many layers

The fringe level follows the solver's stencil. Chesshire & Henshaw (1990),
§3.2, p. 14: a centred three-point discretization ($q_{\mathrm d}=3$) needs one
line of interpolation points, a five-point one ($q_{\mathrm d}=5$) two lines,
i.e. $n_f=(q_{\mathrm d}-1)/2$ for these centred stencils *(compiler check, not in
the sources)*; [Henshaw (1994)](/sources/henshaw-1994.md)
uses two lines for the fourth-order scheme (§4.1, §5.1). The later sources
agree on two layers for wider stencils: [Sherer & Scott (2005)](/sources/sherer-2005.md),
§4.2, use a **two-point fringe** at all interpolation boundaries of their
sixth-order compact scheme; Picard et al. (2021), §3.2.3, Fig. 3, set
$n_f=2$ ghost layers because a second-order MUSCL flux at a face needs two
cells on each side, which makes the flux at the first integrated cell
independent of the patch boundary. Rogers et al. (2003),
"Outer-Boundary Specification": PEGASUS 5 sets one fringe level for holes and
outer boundaries jointly or separately; a fringe level of two "has certain
advantages within the flow solver and can produce more accurate solutions"
(stated, not shown); not all solvers accept mixed levels. The abstract also
describes PEGASUS 5's hole-size optimization as "adding additional layers of
fringe points" ([overlap optimization](/methods/overlap-optimization.md)).

[Lee & Baeder (2003)](/sources/lee-2003.md), p. 12, recommend the opposite at
outer boundaries: interpolate a **single** layer of outer-boundary points
instead of the usual two, because high-order interpolation is expensive in 3-D
(the cost per interpolated point grows roughly $q$-fold from 2-D to 3-D, against
50% for an interior point); with a 5-point interior stencil this needs biased
stencils at the first interior points, with a fourth-order compact scheme it
does not. At hole fringes they recommend "as many layers as possible", since
the fringe insulates invalid hole values (next section).

Noack (2005), §IV, Fig. 5, ties the fringe depth to the solver's
reconstruction: for a cell C next to the first fringe cell F1, a first-order
scheme needs C and F1; a least-squares gradient (Cobalt, HYB3D) needs C, F1 and
the second layer F2; a Taylor-series reconstruction from node values (USM3D)
needs the node values of F1, each averaged from all cells around the node,
hence a wider fringe.

**Fringe gap and the singular limit.** [Sharma et al. (2021)](/sources/sharma-2021.md),
Fig. 4, describe the fringe built by TIOGA's implicit hole cutting: the nodes
of a preset number of cells counted inward from each outer boundary are
mandatory fringe, and a preset number of nodes beyond the innermost mandatory
fringe are kept as field points on both meshes, so that the **fringe gap** $d$
between the receptors of the two meshes stays nonzero, "which would otherwise
result in a singular system of equations". Because both counts are in cells,
$d$ shrinks with $h$ unless the user intervenes. Their $d$ is Chesshire's
overlap below, and the $d\propto h$ case is the one that needs wider
interpolation for second-order PDEs
([interpolation-order requirement](/results/interpolation-order-requirement.md)).

## SUGGAR's fringe rules

Noack (2005), §IV, marks **INNER** fringes (between holes and field) and
**OUTER** fringes (on boundaries flagged as overlap; any boundary not
associated with a boundary surface becomes overlap automatically), each at
levels 1 and 2:

- *node-centred*: a cell with an OUT node makes its other nodes INNER FRINGE 1;
  a cell with an INNER FRINGE 1 node makes its other nodes INNER FRINGE 2;
  outer-boundary points are OUTER FRINGE 1, and the other nodes of their cells
  OUTER FRINGE 2;
- *cell-centred, neighbour based* (for least-squares gradients, Fig. 6): a cell
  with an OUT face neighbour is INNER FRINGE 1, a cell with an INNER FRINGE 1
  neighbour INNER FRINGE 2; cells touching an outer-boundary node are OUTER
  FRINGE 1, their neighbours OUTER FRINGE 2;
- *cell-centred, node based* (for Taylor-series reconstruction, Fig. 7): OUT
  and OUTER FRINGE 1 are propagated from nodes to cells and back to all nodes of
  those cells before the second level is marked; this assembly needs more
  overlap than the neighbour-based one.

## Overlap

**Heuristic statements.** Benek et al. (1983), p. 375, Fig. 7a: the points in
the difference approximation used by the interpolation must be defined on the
donor grid, the overlap must be wide enough for such points to exist, and,
heuristically, wide enough that the boundaries forming it have little influence
on the solution where it is interpolated. Benek et al. (1985), p. 323, require
"sufficient overlap ... to support an interpolation for the outer boundary" of
the embedded grid. Their grids are generous: the cylinder overlap spans radial
points 6 to 30 (1983, p. 376), the SKF 1.1 grids overlap by 5 points, the 1985
fuselage grid overlaps the outer grid by 2.5 radii and the ellipsoid grids by
5 points (1985, pp. 326, 330).

**Chesshire's overlap $d$.** Chesshire & Henshaw (1990), §5.3, define the
overlap as the distance between the innermost interpolation points of the two
grids (for two 1-D grids, $d=x_p-x_{2p}$ in their indexing), not the geometric
overlap of the grids; $d>0$ is necessary, the interpolation system becoming
singular when a receptor of one grid coincides with one of the other. The width
$q$ needed for accuracy depends on how $d$ scales: for a PDE of order $2s$
discretized to order $p$, $q=sp+1$ when $d\propto h$ and $q=sp/2+1$ when
$d=O(1)$, with $sp/2$ receptor layers on each grid and a total overlap
$d+\tfrac{sp}{2}(h_1+h_2)$. Chesshire & Henshaw print the rule as $q=2pr+1$ /
$q=pr+1$ with $pr$ layers, their $2p$ being the PDE order and $2r$ the
discretization order, so that their $p$ is the registry's $s$ and their $2r$
the registry's $p$. Lemmas I–II (§5.3, pp. 33–34) prove it for second-order
discretizations ($q\ge2s+1$ and $q\ge s+1$), assuming a well-posedness property
proved only for $s=1$; the extension to higher-order discretizations rests on
their Remark 1 (see the
[interpolation-order requirement](/results/interpolation-order-requirement.md)).
Explicit interpolation needs more overlap than implicit interpolation
([explicit and implicit
interpolation](/definitions/explicit-and-implicit-interpolation.md)); the
minimum allowable overlap is an input of CMPGRD (§3.2).

**Explicit interpolation and circular interpolation.** Sherer & Scott (2005),
§5.3, size the overlap of their single-cylinder grid as "the minimum number of
points to prevent circular interpolation", i.e. donor points that are
themselves receivers fed by the grid they update, with a two-point fringe; a
larger overlap gives more centred donor stencils and lower interpolation error,
a minimal one more one-sided stencils (§3.2). Picard et al. (2021), §3.2.2,
Eq. 12, state the same explicit-interpolation condition for cell layers: the
substrate receptor cells are the closest $n_f$ layers that intersect the patch
but no patch receptor cell. They then *minimize* the gap between the two
receptor sets by adding patch receptor cells between them without violating
that condition, a step that "eventually improves the stability" at large patch
refinement (Eq. 13; no separate test shown). The gap they minimize is the least
distance between receptor-cell centres of the two grids, which plays the role
of Chesshire's $d$ *(compiler check, not in the sources)*; with coincident
interfaces it equals half the sum of the two cell sizes, so it stays positive
(§4.2, Eq. 23).

**Block overlaps.** Sherer & Scott (2005), §4.2, split grids into blocks for
MPI and connect blocks through coincident-point overlaps of five points, which
recover the interior differencing and filtering exactly; only the non-coincident
overset boundaries need interpolation.

**Yin–Yang buffer.** Kageyama & Sato (2004), §II, extend each component by a
buffer angle $\delta$ proportional to the grid spacing ($\Delta\theta=\Delta\phi=2\delta$
in their Fig. 1) "required for minimum overlap in the overset methodology"; even
for $\delta\to0$ the basic grid overlaps on about 6% of the sphere (§III;
[Yin–Yang grid](/definitions/yin-yang-grid.md)).

## Fringe thickness and time step

Lee & Baeder (2003), pp. 7–9, state a condition for leaving hole points
unblanked: contamination from invalid points is impossible if the distance
information travels from any invalid point in one $\Delta t$ is smaller than
the thinnest fringe thickness, provided the fringe completely encloses the
body; the distance of the first fringe layer from the surface is set by the
relative cell volumes. They report that "first order checks of many cases"
put common time steps well within this limit, and recommend frequent checks.
For moving bodies, Meakin & Suhs (1989), §II, Fig. 3, impose a related
one-layer rule on receptors: a hole point must never become a field point
without first having been an interpolated hole-boundary point, which limits a
hole's motion to one point per time step in their restricted search
([moving overset grids](/methods/moving-overset-grid.md)).

## Donor qualification near boundaries

Receptor and donor layers interact near grid boundaries. Lee & Baeder (2003),
p. 10, use a 6-point monotone Hermite cubic stencil per direction, so the first
two cells from each grid boundary cannot be donors; near walls they accept 4-
or 2-point stencils instead (p. 11). To avoid coupled (implicit) interpolation
between outer-boundary points of two minimally overlapping grids they
interpolate all outer-boundary points before the hole-fringe points (p. 11,
Fig. 12). Noack (2005), §VI, notes that cell-centred donor stencils (donor cell
plus face neighbours) occupy roughly twice the space of node-centred ones and
lose members at boundaries.

## Receptor layers in later methods

Later sources fix the receptor layers per method: two layers of acceptor cells on each mesh in [Zhao et al. (2022)](/sources/zhao-2022.md) (§II C); one layer of artificial-boundary elements whose higher modes are rebuilt in the DG coupling of [Kochi & Ramakrishna (2022)](/sources/kochi-2022.md) (§3); and, in [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md), fringe cells that are not interpolated at all, the grids being coupled by fluxes through a compact hybrid stencil ([ADER schemes on overlapping grids](/methods/ader-on-overset-grids.md)). [Wang & Stern (2022)](/sources/wang-2022.md) rebuild the volume fraction of fringe cells geometrically rather than interpolate it ([multiphase flow](/methods/multiphase-flow-on-overset-grids.md)). [Chandar & Sitaraman (2022)](/sources/chandar-2022.md) replace the interpolation row of one receptor, the flux-balance cell, by a global conservation constraint ([conservative overset interface](/methods/conservative-overset-interface.md)).

## Qualifications

- Benek et al. (1985) set fringe points to IBLANK $=0$ like hole points, for the
  convenience of XMER3D; their receptors are identified by the interpolation
  list, not by the mask.
- Noack (2005) prints a node-based cell-centred procedure (§IV, steps 1–5) whose
  step 5 uses INNER FRINGE 1 nodes, but no printed step assigns INNER FRINGE 1.
- Chesshire & Henshaw's 1-D grid formula $x^2_i=b-(i-1)h_2$ and cross-distance
  formula in §5.3 are printed inconsistently with their Fig. 14 (consistent
  forms: $x^2_i=b-(N_2-i)h_2$ and $d+(p-i)h_1+(2p-j)h_2$ in their indexing); the
  $O(h)$ versus $O(1)$ factor counting behind Lemmas I–II is unaffected
  *(compiler check, not in the sources)*.

# Citations

- [Benek et al. (1983)](/sources/benek-1983.md) — p. 375, Fig. 7 (hole-boundary and outer-boundary points, overlap requirement); p. 376 (overlaps used).
- [Benek et al. (1985)](/sources/benek-1985.md) — pp. 323–324, Fig. 4 (fringe definition, overlap requirement); pp. 326, 330 (overlaps used).
- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §I (interpolated boundary points); §II, Fig. 3 (hole-motion rule).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §3.2, p. 14 (lines of interpolation points); §5.3 (overlap $d$, Lemmas I–II, summary rule).
- [Henshaw (1994)](/sources/henshaw-1994.md) — §4.1, §5.1 (two lines, $q=5$).
- [Lee & Baeder (2003)](/sources/lee-2003.md) — pp. 7–9 (fringe thickness and contamination); pp. 10–12, Figs. 12–13 (stencils, single outer layer).
- [Rogers et al. (2003)](/sources/rogers-2003.md) — Abstract; Fig. 1; "Automation of the Oversetting Process"; "Outer-Boundary Specification" (fringe level).
- [Kageyama & Sato (2004)](/sources/kageyama-2004.md) — §II, Eq. (1), Fig. 1 (border points, buffer $\delta$); §III (6% overlap).
- [Noack (2005)](/sources/noack-2005.md) — §I; §IV, Figs. 5–7 (fringe rules); §VI (cell-centred stencils).
- [Sherer & Scott (2005)](/sources/sherer-2005.md) — §3.2 (centring and overlap); §4.2 (two-point fringe, five-point block overlaps); §5.3 (minimal overlap without circular interpolation).
- [Chan (2009)](/sources/chan-2009.md) — §7, Fig. 1 (fringe definition).
- [Roget & Sitaraman (2014)](/sources/roget-2014.md) — §2.1, §3.5 (mandatory receptors).
- [Picard et al. (2021)](/sources/picard-2021.md) — §3.2.1–3.2.3, Eqs. 12–13, Fig. 3 (ghost cells, two layers, gap minimization); §4.2, Eq. 23.
- [Horne & Mahesh (2021)](/sources/horne-2021.md) — §2 (reconstruction cells).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — Fig. 4 (TIOGA fringe, fringe gap).
- [Wang et al. (2021)](/sources/wang-2021.md) — §III A, Fig. 5 (acceptor cells).
- [Zhao et al. (2022)](/sources/zhao-2022.md) — §II C.
- [Kochi & Ramakrishna (2022)](/sources/kochi-2022.md) — §3.
- [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) — §2.1, §4.4.
- [Wang & Stern (2022)](/sources/wang-2022.md) — §2.2.
- [Chandar & Sitaraman (2022)](/sources/chandar-2022.md) — §3.1.
