---
type: Method
title: "Discontinuous Galerkin methods on overlapping grids"
description: "How discontinuous Galerkin solutions on overlapping grids are coupled: element-based coupling rebuilds the degrees of freedom of artificial-boundary cells from the donor grid, face-based coupling imposes donor values through the numerical flux; WENO reconstruction can make the element-based coupling a limiter, and penalty coupling has an energy theory."
status: established
aliases: [DG overset, element-based overset coupling, face-based overset coupling]
tags: [dg, high-order, interpolation, stability]
timestamp: 2026-11-02T15:27:00Z
---

# Discontinuous Galerkin methods on overlapping grids

A discontinuous Galerkin (DG) solution of degree $N$ is a polynomial per element, so an overset coupling can transfer either point values at flux points or whole element polynomials.

## Two coupling families

[Kochi & Ramakrishna (2022)](/sources/kochi-2022.md) distinguish (§1, §3):

- **face-based coupling** (credited to Galbraith et al.): the donor solution is evaluated at the flux points of the artificial boundary and imposed weakly through the numerical flux;
- **element-based coupling** (credited to Nastase, Mavriplis & Sitaraman): the degrees of freedom of the artificial-boundary cells, the receptor cells adjacent to a grid's overset boundary, are rebuilt from the overlapping grid.

## WENO reconstruction of the artificial-boundary cells

Kochi & Ramakrishna (2022) take the element-based route. The cell average of an artificial-boundary cell is kept; its higher modes are rebuilt by a compact subcell WENO reconstruction from the immediate neighbours (WENO3 for $N=1$, WENO5 on half-cells for $N=2$), the missing neighbour across the artificial boundary being a ghost cell whose point values are evaluated from the donor element's polynomial; the donor is found by a k-d tree and Newton inversion of the donor element's map ([donor search](/methods/donor-search.md)) (§3). The reconstructions in $x$ and $y$ are projected and averaged. Because the reconstruction is nonlinear, the same step limits the solution when a discontinuity crosses the overset boundary ([shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md)).

Evidence (§4): $L_2$ density orders about $N+1$ for $N=1$–3 on an entropy wave and an [isentropic vortex](/benchmarks/isentropic-vortex.md), on an embedded square and the same square rotated by $45^\circ$, with errors no larger than on a single grid; Sod and Lax shock tubes and three 2-D Riemann configurations cross the artificial boundary without oscillation. No stability or conservation analysis is given.

## Penalty coupling and its energy theory

[Kopriva et al. (2022)](/sources/kopriva-2022.md) analyse the continuous overset problem coupled by penalty (lifting) terms with matrices $\Sigma_u$, $\Sigma_v$ at both overlap boundaries, the form a DG or summation-by-parts discretization inherits: it is energy bounded and conservative if $\beta A+\Sigma_u=\Sigma_v$ and $2\Sigma_v-\beta A\ge0$ ([well-posedness and energy stability of overset problems](/results/overset-well-posedness.md)). The authors present the analysis as the foundation for provably stable overset discretizations (§1, §4).

## Shock-aligned DG overset grids and staggered LDG meshes

[Kochi & Ramakrishna (2023)](/sources/kochi-2023.md) use their DG overset coupling to place a shock-aligned refined grid where troubled cells were flagged ([shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md)). [Tian et al. (2024)](/sources/tian-2024.md) use "overlapping meshes" in a different sense: the vorticity, velocity and potential of the incompressible Euler equations are approximated on different staggered meshes, so the velocity is continuous on primitive-mesh interfaces and upwind fluxes apply in a local DG scheme; a divergence-free velocity and positive vorticity averages (time-step restriction plus slope limiter) give a maximum principle for the vorticity (Abstract).

## Qualifications

- Kochi & Ramakrishna (2022) print the nonlinear weights with the sum over stencils in the denominator, which as printed makes them equal to the linear weights; the cited Jiang–Shu form applies the denominator per stencil (Eq. 12) *(compiler check, not in the sources)*.

# Citations

- [Kochi & Ramakrishna (2022)](/sources/kochi-2022.md) — §1, §3, §4, Tables 1–2.
- [Kopriva et al. (2022)](/sources/kopriva-2022.md) — §1, Thm 5, §4.
- [Kochi & Ramakrishna (2023)](/sources/kochi-2023.md) — Abstract.
- [Tian et al. (2024)](/sources/tian-2024.md) — Abstract, §3–§4.
