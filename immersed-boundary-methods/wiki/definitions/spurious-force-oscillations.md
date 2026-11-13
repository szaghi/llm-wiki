---
type: Definition
title: "Spurious force and pressure oscillations"
description: "Non-physical high-frequency oscillations of the pressure and of the hydrodynamic force on a body moving across a fixed grid in immersed boundary and cut-cell methods, caused by the discontinuous change of the cells and forcing points the boundary condition acts on; their sources (local mass-conservation errors, fresh and dead cells, abrupt switching of stencils) and the remedies the sources report."
status: established
aliases: [spurious pressure oscillations, SPO, spurious force oscillations, SFO, force oscillations of moving bodies]
tags: [moving-boundary, sharp-interface, cut-cell, conservation, pressure]
timestamp: 2026-11-13T05:47:00Z
---

# Spurious force and pressure oscillations

When a body moves across a fixed Cartesian grid, the set of cells and forcing
points that carry its boundary condition changes discontinuously: cells cross
from solid to fluid ([fresh cells](/definitions/fresh-cell-problem.md)) and
from fluid to solid (dead cells), and reconstruction stencils switch. Sharp
methods then show non-physical oscillations of the pressure and of the
computed force at the frequency with which the boundary crosses grid lines;
they shrink with refinement but can dominate the force signal
([Xie et al. 2022](/sources/xie-2022.md), §1; [Raj et al. 2023](/sources/raj-2023.md), §1).

## Sources identified

- **Local mass-conservation errors.** [Xie et al. (2022)](/sources/xie-2022.md),
  §2 and §4.2, attribute the oscillations in cut-cell methods to the
  temporal discontinuity of the solid volume in cut cells: with a mass source
  equal to the rate of change of a cut cell's solid volume and consistent
  mass and momentum fluxes, they compare no conservation, mass-only and full
  conservation and find the oscillations greatly reduced only with both; the
  non-smooth volume change of cut cells is "the major resource" of the
  oscillations.
- **Violation of the geometric conservation law** by the changing status of
  intercepted cells ([Raj et al. 2023](/sources/raj-2023.md), §1–§2, citing
  Lee et al.).
- **Insufficient smoothing of the transfer** between grid and moving boundary
  in reconstruction-based direct forcing ([Uhlmann 2005](/sources/uhlmann-2005.md),
  §1), and mesh-scale oscillations with volume-fraction weighting.

## Remedies reported

| remedy | source |
|---|---|
| regularized-delta transfer of the direct force at Lagrangian points | [Uhlmann (2005)](/sources/uhlmann-2005.md) |
| mass source/sink in cells containing the boundary | [Kim et al. (2001)](/sources/kim-2001.md), cited by Xie et al. (2022) |
| cut cells for continuity, immersed boundary for momentum | [Seo & Mittal (2011)](/sources/seo-2011.md), cited also by Xie et al. (2022) and Raj et al. (2023) |
| conservative and consistent implicit cut-cell fluxes with a solid-volume source computed consistently with the piecewise-linear boundary | [Xie et al. (2022)](/sources/xie-2022.md) |
| field extension of the forcing to near-boundary solid points, reducing the divergence error | [Raj et al. (2023)](/sources/raj-2023.md) |

Raj et al. (2023, §4) measure decay rates of the oscillation amplitude above 2
under grid refinement and above 0.5 under time-step refinement, against 1.8
and 0.5 reported by Seo and Mittal.

## The moving-boundary papers of 2011–2018

- **Geometric conservation, quantified.** [Seo & Mittal (2011)](/sources/seo-2011.md),
  §2, split the mass-conservation error of a ghost-cell method with a moving
  body into a volume term from fresh and dead cells and transpiration terms of
  the stair-step boundary ([geometric conservation law](/definitions/geometric-conservation-law.md)).
  For a cylinder oscillating at $Re=31$ on a coarse grid the volume term is
  about 40 times the transpiration terms, and every peak of the pressure drag
  falls on a step where a fresh or a dead cell appears; dead cells matter as
  much as fresh ones. The oscillation amplitude scales as $h^{1.9}\Delta t^{-0.8}$.
  Applying cut-cell volume and face fractions to the pressure equation only,
  with the mass balance of cells of volume fraction below $0.5$ moved to
  their neighbours ([cell merging](/methods/cell-merging.md), virtual form),
  lowers the oscillations by about an order of magnitude (root mean square
  about seven times) and keeps second-order accuracy; the residual scales as
  $h^{1.8}\Delta t^{-0.5}$ (§3–§4). Diffuse-interface methods smooth the
  error in time without removing it (§2).
- **Abrupt change of the discrete operator.** [Meinke et al. (2013)](/sources/meinke-2013.md),
  §3.1, and [Schneiders et al. (2013)](/sources/schneiders-2013.md), §4, trace
  the oscillations of compressible cut-cell methods to the sudden change of the
  discretization when a cell emerges, submerges, becomes cut or becomes small:
  the changed truncation error acts like an unphysical source term. They make
  the change smooth: the least-squares weight of a cell entering or leaving a
  reconstruction stencil ramps over about ten time steps, and the blending
  between the regular update and the stable interpolated update of a small
  cell is a continuously differentiable function of the cell volume instead of
  a switch at volume fraction $0.5$. Drag fluctuations of a transversely
  oscillating cylinder fall by up to two orders of magnitude compared with
  [cell merging](/methods/cell-merging.md) (Schneiders et al. 2013, §6).
  [Schneiders et al. (2016)](/sources/schneiders-2016.md) keep this scheme,
  strictly conservative, for freely moving particles and report forces free of
  the oscillations.

## Contradictions

- **Is conservation enough? (open, opened 2026-11-13).**
  [Seo & Mittal (2011)](/sources/seo-2011.md), §2–§4, identify the violation of
  the [geometric conservation law](/definitions/geometric-conservation-law.md)
  — the spurious mass sources of fresh and dead cells — as "the primary cause"
  of the oscillations and remove most of them by restoring local mass
  conservation, without smoothing the stencils; [Xie et al. (2022)](/sources/xie-2022.md)
  likewise find mass and momentum conservation sufficient to remove most of
  them. [Schneiders et al. (2013)](/sources/schneiders-2013.md), §1 and §4–§5,
  state that the oscillations "are caused by abrupt changes of the spatial
  discretization operator" and show them in a conservative cut-cell scheme
  with cell merging, which they remove only by making the discrete operator
  vary smoothly in time. The two attributions overlap — Seo and Mittal list
  the abrupt change of near-wall velocities and stencils among the residual
  sources (§4), and Schneiders et al. keep strict conservation — but they
  disagree on which mechanism is primary and on whether a conservative scheme
  can still oscillate. No source in the bundle settles it.

# Citations

- [Kim et al. (2001)](/sources/kim-2001.md) — §2.3.
- [Uhlmann (2005)](/sources/uhlmann-2005.md) — §1, §5.
- [Xie et al. (2022)](/sources/xie-2022.md) — §1, §2, §4.
- [Raj et al. (2023)](/sources/raj-2023.md) — §1, §2, §4.
- [Seo & Mittal (2011)](/sources/seo-2011.md) — §2–§4.
- [Meinke et al. (2013)](/sources/meinke-2013.md) — §3.1, §4.
- [Schneiders et al. (2013)](/sources/schneiders-2013.md) — §1, §4–§6.
- [Schneiders et al. (2016)](/sources/schneiders-2016.md) — §1, §6.
