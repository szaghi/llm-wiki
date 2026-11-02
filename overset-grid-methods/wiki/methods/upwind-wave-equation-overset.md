---
type: Method
title: "Upwind schemes for wave equations on overlapping grids"
description: "Upwind dissipation for finite-difference schemes of wave equations in second-order form on overset grids, where centred schemes are generally unstable near thin boundary-fitted grids: added as a modular corrector stage that acts as a special artificial dissipation, also in implicit modified-equation time stepping."
status: established
aliases: [upwind predictor-corrector, upwind dissipation for second-order wave equations]
tags: [wave-equation, finite-difference, stability, high-order]
timestamp: 2026-11-02T15:26:00Z
---

# Upwind schemes for wave equations on overlapping grids

Wave equations have no natural dissipation, so the interpolation at overset boundaries can drive centred, dissipation-free schemes unstable; the difficult case is an overset grid with thin boundary-fitted component grids. The sources here solve the wave equation in second-order form (and Maxwell's equations written that way) and add upwind dissipation for stability.

## Upwinding as a corrector stage

[Angel et al. (2023)](/sources/angel-2023.md) add upwinding to an existing centred discretization as a modular corrector stage that takes the form of a special artificial dissipation. The predictor–corrector scheme keeps the robustness of the authors' earlier upwind formulation — theory and computations show stability on overset grids with thin boundary-fitted grids, where nondissipative schemes are generally unstable — and runs typically ten or more times faster; Maxwell's equations in second-order form are solved to second and fourth order ([Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md)).

## Upwinding in implicit time stepping

[Carson et al. (2025)](/sources/carson-2025.md) build implicit modified-equation schemes (second and fourth order) for the same equations and discuss several ways of incorporating upwind dissipation; adding it in a separate explicit predictor–corrector step, as above, is the one they find useful ([IMEX time stepping on overlapping grids](/methods/imex-time-stepping-on-overset-grids.md)).

## Relation to other stabilizations

[Henshaw (2006)](/sources/henshaw-2006-b.md) stabilizes a centred high-order Maxwell solver on composite grids with added high-order dissipation ([high-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md)); the upwind schemes replace that tuned dissipation by one built from the characteristic structure of the equations.

# Citations

- [Angel et al. (2023)](/sources/angel-2023.md) — Abstract, §2–§3, numerical section.
- [Carson et al. (2025)](/sources/carson-2025.md) — Abstract, Conclusions.
- [Henshaw (2006)](/sources/henshaw-2006-b.md) — §9, Eq. (9.9).
