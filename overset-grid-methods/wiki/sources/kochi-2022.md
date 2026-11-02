---
type: Source
title: "Kochi & Ramakrishna (2022) — A discontinuous Galerkin overset scheme using WENO reconstruction and subcells for two-dimensional problems"
description: "Couples discontinuous Galerkin solutions on two-dimensional overset quadrilateral grids by reconstructing the higher modes of each artificial-boundary cell with a compact subcell WENO procedure fed by donor-polynomial values in a ghost cell, giving order N+1 on smooth problems and acting as a limiter when shocks cross the overset boundary."
resource: "doi:10.1007/s10915-022-01991-9"
source_kind: paper
authors: [Kochi S.R.S.P., Ramakrishna M.]
year: 2022
venue: "J. Sci. Comput. 93:35"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2022_Crossref_Journal_of_Scientific_Computing_Kochi_A_Discontinuous_Galerkin_Overset_Scheme_Using_WENO_Reconstru.pdf"
tags: [dg, high-order, interpolation, shock-capturing, overset-grid]
timestamp: 2026-11-02T15:04:00Z
---

# Summary

For the discontinuous Galerkin method on overset quadrilateral grids, Kochi & Ramakrishna follow the element-based coupling (the degrees of freedom of the artificial-boundary cells of one grid are rebuilt from the other grid) rather than the face-based one (donor values imposed weakly through the numerical flux). The cell average of an artificial-boundary cell is kept; its higher modes are recomputed by their compact subcell WENO reconstruction from the immediate neighbours, the missing neighbour being a ghost cell across the artificial boundary whose point values are evaluated from the donor grid's DG polynomial (k-d tree search and Newton inversion of the donor map). The nonlinear reconstruction doubles as a limiter when a discontinuity crosses the overset boundary. Smooth tests ([isentropic vortex](/benchmarks/isentropic-vortex.md), entropy wave) give order $N+1$; shock tubes and 2-D Riemann problems pass the artificial boundary without oscillation. See [discontinuous Galerkin methods on overlapping grids](/methods/discontinuous-galerkin-on-overset-grids.md) and [shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md).

# Version read

arXiv preprint 2106.06285v1 (11 June 2021), 20 pages, all read; locators are those of the preprint. Title and authors match the Crossref record.

# Key claims

1. Element-based coupling (artificial-boundary cell degrees of freedom rebuilt from the overlapping grid, after Nastase, Mavriplis & Sitaraman) is chosen over face-based coupling (donor values at artificial-boundary flux points imposed through the numerical flux, after Galbraith et al.) (§1, §3). **Stated**
2. The cell average of the artificial-boundary cell is kept and its higher modes are rebuilt by compact subcell WENO reconstruction (WENO3 for $N=1$, WENO5 on half-cells for $N=2$, subcells for $N=2,3$) in $x$ and $y$, projected and averaged (§3, Eqs. 8–14). **Derived**
3. The ghost cell extends the grid line across the artificial boundary with the size of the boundary face; its point values come from the donor DG polynomial, the donor found by a k-d tree and Newton inversion (tolerance $10^{-10}$, at most 20 iterations) (§3.1). **Stated**
4. Entropy wave and isentropic vortex on an embedded square and the same square rotated by $45^\circ$: $L_2$ density orders about $N+1$ for $N=1$–3, errors no larger than on the single grid (§4.1–4.2, Tables 1–2). **Shown**
5. Sod and Lax shock tubes (overset patch $h=1/200$ on an $h=1/100$ background) and three 2-D Riemann configurations: shocks cross the artificial boundary without oscillations (§4.3–4.4). **Shown**
6. No stability or conservation analysis is given. **Stated**

# Printed slips

- Eq. 12 prints the nonlinear weights as $\bar\omega_i=\gamma_i/\sum_i(\epsilon+\beta_i)^2$; with the sum in the denominator the weights reduce to $\gamma_i$ and the reconstruction is linear, contrary to its use as a limiter; the cited Jiang–Shu form has $(\epsilon+\beta_i)^2$ per stencil *(compiler check, not in the sources)*.
- Example 2: $40\times40$ elements on $[0,10]\times[-5,5]$ give an element size $1/4$, not the printed "1/20" *(compiler check, not in the sources)*.
- The Riemann tests give a background $h=1/400$ in the text and $1/200$ in the captions of Figs. 13–17; the Fig. 17 caption gives the configuration-16 patch as $[0.395,0.605]$, the text and Fig. 14 $[0.295,0.705]$; Example 1 writes the exact solution as $\rho(x,y,0)$; $x_b(1,s_k)$ in Eq. 4 is undefined.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| artificial boundary cell | receptor cell of the DG grid | its average is kept, its higher modes rebuilt |
| $P^N$ | polynomial degree $N$ | registry §8 |
| $\gamma_i$, $\beta_i$, $\bar\omega_i$ | WENO linear weights, smoothness indicators, nonlinear weights | registry §8 ($\omega_r$, $\beta_r$) |

# Reference list

18 printed references, numbered, merged complete into the [bibliography](/bibliography.md) with `citedby` kochi-2022. No printed duplicates.

# Pages created or updated

Chunk 3 (2026-11-02). This source is cited on:

- [Isentropic vortex convection](/benchmarks/isentropic-vortex.md)
- [Composite overlapping grid](/definitions/composite-overlapping-grid.md)
- [Fringe (receptor) points and overlap width](/definitions/fringe-point.md)
- [Discontinuous Galerkin methods on overlapping grids](/methods/discontinuous-galerkin-on-overset-grids.md)
- [Donor search](/methods/donor-search.md)
- [High-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Moving overset grids](/methods/moving-overset-grid.md)
- [Shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md)
