---
type: Definition
title: "Grid hierarchy and priority"
description: "The rules that decide which component grid may cut holes in, or supply donors to, which other: Benek's embedding hierarchy of levels, its relaxation in later PEGASUS versions, CMPGRD's priority ordering, SUGGAR's body hierarchy in which siblings cut each other, and the donor-quality criteria that replace any ordering."
status: established
aliases: [embedding hierarchy, grid embedding hierarchy, hierarchical structure of grids, grid priority, grid ordering, body hierarchy, primary and subordinate grids]
tags: [domain-connectivity, hole-cutting, overset-grid]
timestamp: 2026-11-02T11:29:00Z
---

# Grid hierarchy and priority

Where several component grids of an [overset grid](/definitions/overset-grid.md)
cover the same region, an assembly needs a rule that decides which grid
**cuts holes** in which, and which grid **serves as donor** for which receptor.
The founding sources give four kinds of rule: a strict **embedding hierarchy**
of levels $\ell(k)$ (Benek et al.), a total **priority ordering** of the grids
by their index $k$ (Chesshire & Henshaw), a **body hierarchy** of geometric
components (Noack), and **no ordering at all**, the choice being made point by
point by a donor-quality measure (Rogers et al., Lee & Baeder). The rule shapes
both [hole cutting](/methods/hole-cutting.md) and the
[donor search](/methods/donor-search.md).

## Benek's embedding hierarchy

[Benek et al. (1983)](/sources/benek-1983.md), p. 374, Figs. 2–3, impose a
hierarchical structure "following naturally from the embedding process": every
grid sits at a level $\ell(k)$, the background grid at $\ell=1$, embedded grids
at larger $\ell$. The general form (Fig. 2) is a graph in which a grid may be
linked to several grids of the previous level; the paper restricts itself to a
tree:

1. every grid $G_k$ with $\ell(k)>1$ lies entirely inside a **single** grid
   $G_{k'}$ with $\ell(k')=\ell(k)-1$, its precursor, $\Omega_k\subset\Omega_{k'}$;
2. grids on the same level are **disjoint**: $\Omega_k\cap\Omega_{k''}=\emptyset$
   for $\ell(k)=\ell(k'')$, $k\neq k''$.

The edges of the tree are the communication lines: an embedded grid takes its
outer-boundary values from its precursor and cuts a hole in it, whose boundary
receives values from the embedded grid (p. 375, Fig. 7). The authors call the
general graph "an important generalization" for future extensions. The
hierarchy is also the data structure: each grid node stores its level,
precursor, descendants, and the locations of its interpolation points,
coefficients, interpolated data and flagged points, connected by linked lists
in one large array (pp. 375–376). [Benek et al. (1985)](/sources/benek-1985.md),
p. 323, Fig. 1, keep the same rules in 3-D and name their purpose: the
hierarchy "limits the search" for donor points to parent–child pairs. Their
applications use outer → fuselage → {wing, tail} and large ellipsoid → {two
small ellipsoids} (Fig. 5). [Meakin & Suhs (1989)](/sources/meakin-1989.md),
§I, speak of a **primary** grid that completely overlaps a **subordinate**
grid; their Space Shuttle case has the external-tank grid as primary and six
hole boundaries among three grids that all cut one another (§III).

## Relaxation in PEGASUS

[Rogers et al. (2003)](/sources/rogers-2003.md), pp. 1037–1038, recall the
history: PEGASUS 1 (Benek et al. 1985) imposed the hierarchy — a grid could cut
a hole only in a larger grid and connect only to it — with topology-specific
hole cutters; version 2 (Benek, Donegan & Suhs 1987, as recalled) removed the
restrictions on interconnectivity, so a grid could cut holes in any number of
grids and overlap any number of grids; version 3 generalized the cutters,
version 4 allowed surfaces from several grids to form one hole. Donor choice
among several candidate grids was then governed by a user-supplied
**prioritized link list** per grid, which PEGASUS 5 replaces by the
cell-difference parameter because the lists "unnecessarily constrained the
choices for the donor interpolation cells" (Cell Difference Parameter).

## CMPGRD's priority ordering

[Chesshire & Henshaw (1990)](/sources/chesshire-1990.md), §3.2, pp. 14–20,
order the component grids so that **higher-numbered grids cover parts of
lower-numbered ones**: a higher $k$ means a higher priority. In Step 3 of their
algorithm each point first tries to be interpolated from the highest grid
$k'>k$ that can serve it, then to be a valid discretization point, then to be
interpolated from the highest $k'<k$, and otherwise becomes exterior; Step 5
then works from the lowest grid to the highest, deleting unneeded interpolation
points and converting interpolation points that can be discretized. Points
removed from a grid generally lie under a higher grid, but every grid, even the
top one, can lose points, and changing the order changes the composite grid
(Fig. 9). No containment or disjointness is required: grids of any priority may
overlap one another arbitrarily. The authors conjecture that if a valid
composite grid exists for some ordering, one results for all orderings, and say
this is not proved (p. 16).

## SUGGAR's body hierarchy

[Noack (2005)](/sources/noack-2005.md), §II, Figs. 3–4, organizes the
*geometry*, not the grids, as a tree of bodies — e.g. Aircraft → {Wing+Pylon →
{Wing, Pylon}, Store → {Bomb, Fin 1–4}} — with grids attached to the leaves and
container bodies that hold no grids. The cutting rule is **siblings cut each
other**: when a body cuts a sibling, the sibling's subtree is searched and all
grids of its descendants are cut (Wing cuts the Pylon grids; Wing+Pylon cuts
every Store grid). The same tree carries the motion: each body's transform is
given relative to its parent, so a fin can move relative to a store that moves
relative to the aircraft (§VII; [moving overset
grids](/methods/moving-overset-grid.md)).

## No ordering: quality-based choice

[Lee & Baeder (2003)](/sources/lee-2003.md), p. 3, list "no grid priority or
hierarchy" among the advantages of [implicit hole
cutting](/methods/implicit-hole-cutting.md): every point is tested against all
overlapping grids, and the candidate donor cell of smallest volume wins, the
point's own cell included; holes follow from the cell sizes. Grids sharing part
of a solid wall (O-H, C-H, one-wall topologies) are exempted from cutting each
other by an overlap-matrix entry of $-1$ (pp. 5–6). Rogers et al. (2003)
combine a hierarchy-free exhaustive search with the cell-difference parameter
and an [overlap optimization](/methods/overlap-optimization.md) that keeps the
finest points. In both, the role of the ordering is taken by a measure of donor
and receptor cell size.

## Comparison

| Rule | Source | Who cuts whom | Who serves as donor |
|---|---|---|---|
| level tree | Benek et al. 1983, 1985 | child cuts its precursor | precursor ↔ child only |
| prioritized links | PEGASUS 2–4, as recalled by Rogers et al. 2003 | any grid, by hole-cutter input | user-ordered list per grid |
| index priority | Chesshire & Henshaw 1990 | emerges from the classification; lower grids yield to higher | highest admissible $k'$ first |
| body tree | Noack 2005 | siblings and their descendants | found by search |
| none | Lee & Baeder 2003; Rogers et al. 2003 | emerges from cell volumes / hole map + optimization | smallest cell volume; smallest cell-difference parameter |

## Qualifications

- Benek et al. (1985), p. 323, use "lower level" in both senses: embedded grids
  occupy "a lower level of the hierarchy" (larger $\ell$), while a level-$\ell$
  grid lies inside a grid on "the next lower level $\ell-1$". Their Fig. 1 is
  unambiguous, and the bundle writes only $\ell(k)$ with $\ell=1$ the background.
- Benek et al. (1983) print "G12" in the Fig. 13 legend for the airfoil grid
  that the text and the other figures call the level-2 grid "$G_{21}$".
- Chesshire & Henshaw's ordering-independence statement is a conjecture
  (status hypothesis within this established page).

# Citations

- [Benek et al. (1983)](/sources/benek-1983.md) — p. 374, Figs. 2–3 (hierarchy, general graph, restricted tree); pp. 375–376 (communication lines, data structure).
- [Benek et al. (1985)](/sources/benek-1985.md) — p. 323, Fig. 1 (hierarchy limits the donor search); p. 325, Fig. 5 (application hierarchies).
- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §I (primary and subordinate grids); §III (Shuttle inter-grid boundaries).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §3.2, pp. 14–20, Fig. 9 (ordering, Steps 3 and 5, conjecture).
- [Lee & Baeder (2003)](/sources/lee-2003.md) — p. 3 (no priority or hierarchy); pp. 5–6 (shared-wall grids).
- [Rogers et al. (2003)](/sources/rogers-2003.md) — pp. 1037–1038 (PEGASUS versions); Cell Difference Parameter (link lists replaced).
- [Noack (2005)](/sources/noack-2005.md) — §II, Figs. 3–4 (body hierarchy, siblings cut each other); §VII (hierarchical transforms).
