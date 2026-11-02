---
type: Method
title: "Implicit–explicit time stepping on overlapping grids"
description: "Implicit–explicit time integration on overset grids: split by terms (implicit viscous terms in semi-implicit IMEX Runge–Kutta finite volumes for incompressible flow on moving Chimera meshes) or split by component grid (implicit on grids with small cells, explicit on the background) for geometrically stiff wave problems."
status: established
aliases: [IMEX on Chimera meshes, spatially partitioned implicit-explicit scheme]
tags: [imex, stability, moving-grid, wave-equation]
timestamp: 2026-11-02T15:26:00Z
---

# Implicit–explicit time stepping on overlapping grids

Overset grids raise two kinds of stiffness: physical (viscous or acoustic scales faster than the convective one) and geometric (small cells on a few component grids, needed to resolve fine features, limiting the explicit step of the whole system). The sources split the time integration accordingly.

## Splitting by terms

[Carlino & Boscheri (2024)](/sources/carlino-2024.md) integrate the incompressible Navier–Stokes equations on evolving Chimera meshes with semi-implicit IMEX Runge–Kutta schemes: a flux splitting separates explicit (convective) and implicit (viscous, pressure) terms, the mesh velocity is encoded in the nonlinear flux by integration on moving cells, and an incremental projection enforces the divergence-free constraint. With implicit viscous terms the time step is limited only by the fluid velocity relative to the moving frame, not by the viscous eigenvalues ([incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md), [moving overset grids](/methods/moving-overset-grid.md)).

## Splitting by component grid

[Carson et al. (2025)](/sources/carson-2025.md) derive implicit modified-equation schemes (single step, three time levels, second and fourth order, with conditions for unconditional stability) for wave equations in second-order form and combine them in a spatially partitioned implicit–explicit (SPIE) scheme: component grids with small cells are integrated implicitly, the others — such as background Cartesian grids — explicitly. For geometrically stiff problems this is reported many times faster, and more accurate, than the explicit scheme everywhere; the implicit coefficient matrix is definite and suited to Krylov or multigrid solvers ([upwind schemes for wave equations](/methods/upwind-wave-equation-overset.md)).

## Qualifications

- The two splittings are complementary: Carlino & Boscheri's is the same on every grid; Carson et al.'s couples an implicit and an explicit grid through the overset interpolation, whose stability the authors study by analysis and computation.

# Citations

- [Carlino & Boscheri (2024)](/sources/carlino-2024.md) — Abstract, Conclusions.
- [Carson et al. (2025)](/sources/carson-2025.md) — Abstract, Conclusions.
