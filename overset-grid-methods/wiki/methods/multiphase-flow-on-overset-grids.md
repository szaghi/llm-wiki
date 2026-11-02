---
type: Method
title: "Multiphase flow on overlapping grids"
description: "How interface-capturing and multi-component models cross overset boundaries: a discontinuous volume fraction cannot be interpolated like a smooth field, so it is rebuilt in fringe cells from an interpolated distance function and normal, while a diffuse-interface five-equation model is transferred like the other variables."
status: established
aliases: [two-phase flow on overset grids, VOF overset interpolation]
tags: [multiphase, interpolation, finite-volume, marine]
timestamp: 2026-11-02T15:06:00Z
---

# Multiphase flow on overlapping grids

Interface-capturing variables are discontinuous across the interface; the [inter-grid interpolation](/methods/inter-grid-interpolation.md) used for velocity and pressure smears or violates them at [fringe points](/definitions/fringe-point.md).

## Volume of fluid with geometric reconstruction

[Wang & Stern (2022)](/sources/wang-2022.md) show that trilinear interpolation of the fluid volume fraction $F$ (page-local; not the registry's immersed-body $\chi$) from a coarse donor gives fully wet fringe cells $F<1$ (§1, Fig. 1). They interpolate instead the smooth signed distance $\varphi$ and the interface normal $\mathbf n$ to each fringe cell, rebuild the interface there as the plane $\mathbf n\cdot\mathbf x=\alpha$, and compute $F$ as the water volume of sub-cells on the water side over the cell volume (§2.2, Eqs. (5)–(9)); $\varphi$ is first extended from its four-cell band to the whole domain, because donors outside the band feed fringe cells. A volume-of-fluid ghost fluid method, with ghost-pressure coefficients that use only cell densities, treats gravity and surface tension (§2.3). On advection tests the overset grid raises mass and position errors by at most 0.8 percentage points against a single block (§3), and the method runs on static and dynamic overset grids assembled by [SUGGAR](/software/suggar.md) in ship applications (§4).

## Diffuse-interface multi-component flow

[Picard et al. (2021)](/sources/picard-2021.md) solve the five-equation two-component Euler model (recalled from Allaire, Clerc & Kokh) on a finite-volume Chimera patch, transferring all variables by their intersection-weighted second-order transfer; a Mach 1.22 shock on a helium bubble with a $30^\circ$-rotated patch agrees with the single grid for equal cell sizes (§4.4). The model is written in non-conservative form, and the transfer is not conservative ([shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md)).

## Qualifications

- Wang & Stern (2022) state that interpolating the normal directly is "one order more accurate" than computing it from the interpolated distance function, without showing it (§2.2).
- Level-set mass loss makes the zero level set mismatch across overset grids of different resolution, which Wang & Stern (2022) report as a source of pressure-equation convergence problems in a level-set ghost fluid method (§2.3).

# Citations

- [Wang & Stern (2022)](/sources/wang-2022.md) — §1, §2.2–2.3, §3, §4.
- [Picard et al. (2021)](/sources/picard-2021.md) — §2, §4.4.
