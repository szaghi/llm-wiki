---
type: Definition
title: "Spurious force and pressure oscillations"
description: "Non-physical high-frequency oscillations of the pressure and of the hydrodynamic force on a body moving across a fixed grid in immersed boundary and cut-cell methods, caused by the discontinuous change of the cells and forcing points the boundary condition acts on; their sources (local mass-conservation errors, fresh and dead cells, abrupt switching of stencils) and the remedies the sources report."
status: established
aliases: [spurious pressure oscillations, SPO, spurious force oscillations, SFO, force oscillations of moving bodies]
tags: [moving-boundary, sharp-interface, cut-cell, conservation, pressure]
timestamp: 2026-11-08T18:22:00Z
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
| cut cells for continuity, immersed boundary for momentum (Seo and Mittal) | cited by Xie et al. (2022) and Raj et al. (2023) |
| conservative and consistent implicit cut-cell fluxes with a solid-volume source computed consistently with the piecewise-linear boundary | [Xie et al. (2022)](/sources/xie-2022.md) |
| field extension of the forcing to near-boundary solid points, reducing the divergence error | [Raj et al. (2023)](/sources/raj-2023.md) |

Raj et al. (2023, §4) measure decay rates of the oscillation amplitude above 2
under grid refinement and above 0.5 under time-step refinement, against 1.8
and 0.5 reported by Seo and Mittal.

# Citations

- [Kim et al. (2001)](/sources/kim-2001.md) — §2.3.
- [Uhlmann (2005)](/sources/uhlmann-2005.md) — §1, §5.
- [Xie et al. (2022)](/sources/xie-2022.md) — §1, §2, §4.
- [Raj et al. (2023)](/sources/raj-2023.md) — §1, §2, §4.
