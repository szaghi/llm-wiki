---
type: Method
title: "Cell merging for cut cells"
description: "Stabilization of cut-cell discretizations that combines a small cut cell with one or more neighbours into a single control volume large enough for the full-cell time step; Bayyuk et al.'s merging criteria for moving bodies, the space-time view that equates it with flux telescoping, virtual merging of the mass balance, and the oscillations its on-off switching causes."
status: established
aliases: [cell merging, cell linking, cell combination, virtual cell merging]
tags: [cut-cell, small-cell, moving-boundary, conservation, stability]
timestamp: 2026-11-13T05:47:00Z
---

# Cell merging for cut cells

Cell merging removes the [small-cell problem](/definitions/small-cell-problem.md)
of a [cut-cell method](/methods/cut-cell-method.md) by changing the control
volumes rather than the update: a cut cell whose volume $\kappa_{\mathbf i}h^d$
is small is combined with one or more neighbours, the faces between them are
ignored in the discretization, and the combined cell is advanced with a time
step set by the full cells. The state of the combined cell is the
volume-weighted average of its members, so merging is conservative; after the
step the members are separated again, their states recovered from the
combined state (and a gradient) under a conservation constraint
([Bayyuk, Powell & van Leer 1993](/sources/bayyuk-1993.md); Hartmann et al.,
as described by [Schneiders et al. 2013](/sources/schneiders-2013.md), §4.1).
Ye et al. absorb a cut piece whose centre lies in the body into its neighbours
([Ye et al. 1999](/sources/ye-1999.md), §2).

## Merging criteria for moving bodies (Bayyuk et al. 1993)

For bodies that move across a stationary quadtree grid,
[Bayyuk, Powell & van Leer (1993)](/sources/bayyuk-1993.md) merge every cell
the surface intersects with cells in an envelope around it so that three
criteria hold over each motion step:

1. the initial and the final area of each combined cell are no smaller than
   the smallest uncut cell of the grid (or a fixed fraction of it), which
   removes the time-step limit of small cells for moving and stationary
   boundaries alike;
2. no corner vertex of a combined cell is crossed by the surface during the
   step, so the combined cell keeps its intersection topology: cut cells stay
   cut, interior cells interior, exterior cells exterior. The cells the body
   sweeps over (vanishing cells) and the cells it uncovers (newborn cells, see
   [fresh-cell problem](/definitions/fresh-cell-problem.md)) are thereby
   absorbed into combined cells and need no special handling; the authors
   state that length-averaged fluxes of cells of varying area then keep
   second-order time accuracy;
3. a combined cell holds a bounded number of cells (up to eight in their
   algorithm).

Cells are unmerged after every step, since the topological invariance holds
for one step only, and cells inside the body receive a zero state. The second
criterion ties the motion step to the smallest uncut cell, so the admissible
motion step decreases with the smallest radius of curvature of the body.

## Equivalence with flux telescoping (Murman et al. 2003)

[Murman, Aftosmis & Berger (2003)](/sources/murman-2003.md), §4, treat the
same swept cells by a space-time analysis of the moving cut cell: the flux into
a cell that vanishes ahead of the front, up to the time its vertex is crossed,
is passed on to the next cell. Ahead of the front this flux telescoping is
mathematically equivalent to merging; behind the front it is not, because the
discretization is kept through the step and no reconstruction of the merged
states is needed — a reconstruction they call problematic for large motions.

## Virtual merging (Seo & Mittal 2011)

[Seo & Mittal (2011)](/sources/seo-2011.md), §3, avoid the geometric
complexity of merging in three dimensions by merging only the mass balance:
the source of the pressure Poisson equation of a cut cell with volume fraction
below $0.5$ is transferred to the adjacent cells, after which that small cell
is treated as a [ghost cell](/methods/ghost-cell-method.md). The idea follows
the momentum-exchange method of Meyer et al.

## Merging switches on and off

When the boundary moves, a cell crosses the merging threshold from one step
to the next and is suddenly merged with, or separated from, a neighbour.
[Schneiders et al. (2013)](/sources/schneiders-2013.md), §4–§5, show that this
abrupt change of the discrete operator acts like a source term: a displacement
of a cylinder so small that the expected drag change is $O(10^{-7})$ makes a
single cut cell cross the threshold, and the merged scheme answers with a
visible jump in drag, while their smooth interpolation and
[redistribution](/methods/redistribution.md) scheme does not. Over a
transversely oscillating cylinder the drag fluctuations of merging are up to
two orders of magnitude larger (§6); see
[spurious force oscillations](/definitions/spurious-force-oscillations.md).
[Schneiders et al. (2016)](/sources/schneiders-2016.md), §3.8, still link a
cell that emerges from the body to a neighbour for a single step, which only
delays its appearance by one step.

## Aggregation in unfitted finite elements

The finite-element counterpart aggregates badly cut elements onto an interior
element: the degrees of freedom of the ill-posed elements are constrained by
those of a well-posed root element through a discrete extension operator,
which keeps the condition number bounded independently of the cut
([Badia, Dilip & Verdugo 2023](/sources/badia-2023.md), §1–§2; see
[CutFEM](/methods/cutfem.md) for the ghost-penalty alternative).

# Citations

- [Bayyuk, Powell & van Leer (1993)](/sources/bayyuk-1993.md) — merging section.
- [Ye et al. (1999)](/sources/ye-1999.md) — §2.
- [Murman, Aftosmis & Berger (2003)](/sources/murman-2003.md) — §4.
- [Seo & Mittal (2011)](/sources/seo-2011.md) — §3.
- [Schneiders et al. (2013)](/sources/schneiders-2013.md) — §4–§6.
- [Schneiders et al. (2016)](/sources/schneiders-2016.md) — §3.8.
- [Badia, Dilip & Verdugo (2023)](/sources/badia-2023.md) — §1–§2.
