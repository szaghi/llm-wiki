---
type: Definition
title: "Fresh-cell problem"
description: "In sharp-interface immersed boundary methods with moving bodies, a grid cell that was inside the body at the previous time step and is in the fluid at the new one has no valid time history, so its momentum equation cannot be advanced; remedies are merging with neighbours for one step or interpolating its value, and diffuse methods do not meet the problem."
status: established
aliases: [freshly cleared cells, fresh cells, emerging cells]
tags: [moving-boundary, sharp-interface, ghost-cell, cut-cell]
timestamp: 2026-11-13T05:47:00Z
---

# Fresh-cell problem

When $\Gamma$ moves across a fixed grid, some cells that lay inside $\Omega_s$ at
time $t^n$ lie in the fluid at $t^{n+1}$. For a sharp-interface method these
**fresh** ("freshly cleared") cells have no valid flow history, so the
spatial discontinuity of the boundary becomes a temporal discontinuity and the
time derivative cannot be discretized there
([Mittal & Iaccarino 2005](/sources/mittal-2005.md), moving-boundary section;
[Mittal et al. 2008](/sources/mittal-2008.md), §2.2). Because the
boundary moves at most about one cell per step, fresh cells form at most a
single layer.

## Remedies

- **Merging** the fresh cell with a neighbouring fluid cell for the first
  step after it emerges, as in body-conformal Lagrangian methods, without loss
  of spatial accuracy (Udaykumar et al. 1999, cited by Mittal & Iaccarino 2005).
- **Interpolation** of the fresh-cell value from neighbours (Udaykumar et al.
  2001, cited ibid.). [Mittal et al. (2008)](/sources/mittal-2008.md),
  §2.2, take the intermediate velocity of a fresh cell from a trilinear
  interpolation over the seven non-fresh nodes surrounding its image point
  plus the boundary intercept, then solve the pressure equation as usual; the
  stencil is consistent with the one the cell had as a
  [ghost cell](/methods/ghost-cell-method.md) at the previous step.

Methods with continuous forcing do not meet the problem: spreading the
boundary over a few cells on both sides gives a smooth transition between
solid and fluid (Mittal & Iaccarino 2005, moving-boundary section).

## In moving embedded boundaries

[Natarajan et al. (2022)](/sources/natarajan-2022.md), §2, initialize the
conserved state of a freshly cleared cut cell with a volume-weighted average of
the valid cells around it, and show that a uniform flow with a body moving at
the flow velocity is then preserved exactly.

## Fresh and dead cells in cut-cell methods

[Xie et al. (2022)](/sources/xie-2022.md), §3, need no special treatment
beyond setting the previous velocity of a fresh cell to the body velocity and
the new velocity of a dead cell (zero fluid volume) to the body velocity, once
the solid-volume change enters the continuity equation consistently.
[Raj et al. (2023)](/sources/raj-2023.md) relate the changing status of
intercepted cells to violations of the geometric conservation law and to
[spurious force oscillations](/definitions/spurious-force-oscillations.md).

## Vanishing and newborn cells in moving cut cells

[Bayyuk, Powell & van Leer (1993)](/sources/bayyuk-1993.md) name the two
cases for a body crossing a stationary Cartesian grid: a **vanishing** cell
swept over by the body, whose final conserved state is not guaranteed to
vanish (mass or energy would enter through the body, or become negative), and
a **newborn** cell uncovered by the body, across whose new face no flux can be
computed for lack of a state. Splitting the step at the exact covering and
exposure times would need exceptional handling of each such cell and its
neighbours; they instead [merge cells](/methods/cell-merging.md) so that no
combined cell changes its intersection status during a step.
[Murman, Aftosmis & Berger (2003)](/sources/murman-2003.md), §4, follow the
same cells in space-time: the flux a vanishing cell receives before its
vertex is crossed is passed to the next cell ahead of the front, and a cell
emerging behind the front is integrated from the time it appears, its
discretization kept through the step, so that no merged state has to be
reconstructed.

## Smooth and conservative entry and exit

- [Seo & Mittal (2011)](/sources/seo-2011.md), §2, show that dead cells
  (fluid becoming solid) produce pressure peaks as large as fresh cells, and
  that both act as spurious mass sources violating the
  [geometric conservation law](/definitions/geometric-conservation-law.md).
- [Meinke et al. (2013)](/sources/meinke-2013.md), §3.1, and
  [Schneiders et al. (2013)](/sources/schneiders-2013.md), §4.2, give an
  emerging cell a least-squares weight that grows smoothly from zero as it
  leaves the body, over about ten time steps, so that it enters the
  reconstruction stencils of its neighbours gradually.
- [Schneiders et al. (2016)](/sources/schneiders-2016.md), §3.8, give the
  contents of a submerging cell to its fluid neighbours by fixed fractions and
  link an emerging cell to a neighbour for one step, the combined volume being
  stabilized by redistribution however small it is.
- [Bennett, Nikiforakis & Klein (2018)](/sources/bennett-2018.md) fill a newly
  uncovered cell by volume-weighted averaging of its neighbours and give the
  contents of a newly covered cell to its neighbours; in their dimensionally
  split scheme global conservation is kept only approximately
  ([discrete conservation](/properties/discrete-conservation.md)).

# Citations

- [Mittal & Iaccarino (2005)](/sources/mittal-2005.md) — moving-boundary section.
- [Mittal et al. (2008)](/sources/mittal-2008.md) — §2.2.
- [Natarajan et al. (2022)](/sources/natarajan-2022.md) — §2.
- [Xie et al. (2022)](/sources/xie-2022.md) — §3.
- [Raj et al. (2023)](/sources/raj-2023.md) — §1–§2.
- [Bayyuk, Powell & van Leer (1993)](/sources/bayyuk-1993.md) — moving-body and merging sections.
- [Murman, Aftosmis & Berger (2003)](/sources/murman-2003.md) — §4.
- [Seo & Mittal (2011)](/sources/seo-2011.md) — §2.
- [Meinke et al. (2013)](/sources/meinke-2013.md) — §3.1.
- [Schneiders et al. (2013)](/sources/schneiders-2013.md) — §4.2.
- [Schneiders et al. (2016)](/sources/schneiders-2016.md) — §3.8.
- [Bennett, Nikiforakis & Klein (2018)](/sources/bennett-2018.md) — §1, §4.
