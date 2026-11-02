---
type: Method
title: "Nonlinear and optimized inter-grid interpolation"
description: "Inter-grid interpolation that adapts to the solution or is tuned in wavenumber: WENO-type nonlinear interpolation and reconstruction keep high order in smooth regions and fall back to low order at discontinuities crossing overset boundaries, while optimized linear interpolation minimizes spectral error for waves crossing them."
status: established
aliases: [WENO inter-grid interpolation, multi-resolution weighted interpolation, optimized interpolation]
tags: [interpolation, shock-capturing, high-order]
timestamp: 2026-11-02T15:41:00Z
---

# Nonlinear and optimized inter-grid interpolation

Linear Lagrange [inter-grid interpolation](/methods/inter-grid-interpolation.md) of order $q$ oscillates when a discontinuity lies in its stencil, and its error for waves depends on the wavenumber. Two families of sources modify it.

## Nonlinear (WENO-type) interpolation and reconstruction

- [Ding et al. (2025)](/sources/ding-2025.md) extend multi-resolution WENO to interpolation at arbitrary receptor locations on unequal-size nested sub-stencils for curvilinear structured overset grids. Accuracy near discontinuities degrades progressively down to first order, so that several discontinuities can sit in one stencil (classical WENO tolerates one); the linear weights and smoothness indicators ($\omega_r$, $\beta_r$ in registry §8) are independent of the interpolation location. A freestream-preserving discretization is extended to the overset framework; tests with strong discontinuities and shock reflections show robustness at inter-grid boundaries.
- [Kochi & Ramakrishna (2022)](/sources/kochi-2022.md) rebuild the higher modes of DG receptor cells by compact subcell WENO reconstruction from a ghost cell evaluated on the donor polynomial; the nonlinear step doubles as a limiter when shocks cross the overset boundary ([DG on overlapping grids](/methods/discontinuous-galerkin-on-overset-grids.md)).
- [Picard et al. (2021)](/sources/picard-2021.md) limit their second-order intersection-weighted transfer with a limiter extended to overset patches ([shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md)).

## Optimized linear interpolation

- [Ding et al. (2026)](/sources/ding-2026.md) design an optimized high-order interpolation for inter-grid boundaries of a cell-centred finite-difference solver that minimizes spectral-property errors; for periodic problems crossing inter-grid boundaries often it is more accurate than classical Lagrange interpolation.
- [Sherer & Scott (2005)](/sources/sherer-2005.md) analyse interpolation formulas by Fourier error and report optimized and B-spline variants only marginally better than non-optimized explicit interpolation in their vortex case ([high-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md)).

## Qualifications

- Ding et al. (2025, 2026) were read in a targeted way (abstracts, structure, conclusions); their formulas are not reproduced here.

# Citations

- [Ding et al. (2025)](/sources/ding-2025.md) — Abstract.
- [Ding et al. (2026)](/sources/ding-2026.md) — Abstract.
- [Kochi & Ramakrishna (2022)](/sources/kochi-2022.md) — §3.
- [Picard et al. (2021)](/sources/picard-2021.md) — §3.2.5, Eq. 15.
- [Sherer & Scott (2005)](/sources/sherer-2005.md) — §2.1, §3.2, §5.1–5.2, App. A.
