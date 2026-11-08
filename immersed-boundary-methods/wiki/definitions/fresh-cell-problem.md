---
type: Definition
title: "Fresh-cell problem"
description: "In sharp-interface immersed boundary methods with moving bodies, a grid cell that was inside the body at the previous time step and is in the fluid at the new one has no valid time history, so its momentum equation cannot be advanced; remedies are merging with neighbours for one step or interpolating its value, and diffuse methods do not meet the problem."
status: established
aliases: [freshly cleared cells, fresh cells, emerging cells]
tags: [moving-boundary, sharp-interface, ghost-cell, cut-cell]
timestamp: 2026-11-08T18:10:00Z
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

# Citations

- [Mittal & Iaccarino (2005)](/sources/mittal-2005.md) — moving-boundary section.
- [Mittal et al. (2008)](/sources/mittal-2008.md) — §2.2.
- [Natarajan et al. (2022)](/sources/natarajan-2022.md) — §2.
