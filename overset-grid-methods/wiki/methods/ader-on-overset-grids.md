---
type: Method
title: "ADER schemes on overlapping grids"
description: "ADER-type space–time finite-volume schemes on moving overset grids: a local space–time predictor treats all cells alike and a corrector with a compact hybrid stencil carries information between grids through fluxes, so fringe cells need no interpolation; second order is shown for incompressible flow."
status: established
aliases: [space-time chimera, compact transmission condition]
tags: [ader, finite-volume, moving-grid, incompressible]
timestamp: 2026-11-02T15:06:00Z
---

# ADER schemes on overlapping grids

An ADER scheme predicts a local space–time solution in each cell and then corrects the cell averages with space–time fluxes. [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) use the second-order ADER-type scheme of their earlier advection–diffusion work on moving overset grids and extend it to the incompressible Navier–Stokes equations with a Chorin–Temam projection on collocated variables.

## Compact transmission condition

The coupling replaces fringe interpolation by stencils (§2.1, Algorithm 1):

- every cell, fringe cells included, builds a compact hybrid stencil from the first layer of surrounding cells, completed with cells of the other grid where its own grid has none;
- the predictor is local and treats all cells alike; the corrector's finite-volume fluxes then carry information between the grids;
- [inter-grid interpolation](/methods/inter-grid-interpolation.md) is needed only when a hole cell becomes active as the foreground grid moves (§4.4).

[Hole cutting](/methods/hole-cutting.md) inactivates background cells whose centres lie inside the surface of the foreground cells $n=5$ layers from the foreground's outer boundary (§2). In the no-shift configuration — coincident faces of the two grids at the overlap on uniform Cartesian grids (Definition 4.1) — the fringe pressure scheme reduces to the interior diamond formula, so the fluxes are conservative there; the paper states that this can be proved and prints no proof (§4.2.2). Because time is treated like space, the authors describe the overlapping grids as space–time chimera meshes (§1).

## Evidence

Second order in space and time for velocity and pressure ($L^2$ rates about 2) on the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) with a rotating, perturbed foreground grid; the $L^\infty$ error has no definite rate (§5.1). The [lid-driven cavity](/benchmarks/lid-driven-cavity.md), steady and impulsively started or stopped [cylinders](/benchmarks/flow-past-circular-cylinder.md) and a sedimenting cylinder ([immersed boundaries on overlapping grids](/methods/immersed-boundary-on-overset-grids.md)) agree with references using about $10^4$ cells (§5–§6).

## Qualifications

- The hybrid-stencil algorithm may fail for widely different spacings of the two grids; the remedies proposed are not tested (§2.1).
- For second order the relaxation parameter of the predictor must satisfy a bound of order $h_{\max}^2$ (Eq. 34), with $C_2=(1-2^{-1/2})/(2^{-3/2}-1)\approx-0.453$; with a positive $O(1)$ factor the printed bound would be negative, and the factor is left unspecified (§4.1.2) *(compiler check, not in the sources)*.
- The authors state that this is the first ADER-type incompressible Navier–Stokes solver (§7).

# Citations

- [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) — §1, §2.1, §4.1–4.4, §5–§7, Definition 4.1, Algorithm 1.
