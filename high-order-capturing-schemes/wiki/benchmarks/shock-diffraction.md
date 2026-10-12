---
type: Benchmark
title: "Shock diffraction at a backward-facing corner"
description: "A Mach 5.09 shock diffracting around a 90° corner: the strong expansion behind the corner drives density and pressure towards zero, so unlimited high-order schemes need ad hoc fixes, and the diffracted normal shock exposes the shock instability of low-dissipation Riemann solvers."
status: established
aliases: [shock diffraction, backward-facing step diffraction]
tags: [benchmark, euler, positivity, 2d, shock-instability]
timestamp: 2026-10-12T00:00:00Z
---

# Shock diffraction at a backward-facing corner

**Set-up.** Domain $[0,1]\times[6,11]\cup[1,13]\times[0,11]$. A
right-moving Mach 5.09 shock starts at $x = 0.5$, $6 \le y \le 11$, into
gas with $\rho = 1.4$, $p = 1$, $\gamma = 1.4$. Inflow at $x = 0$, outflow
on the far boundaries, reflecting walls along the step; $t = 2.3$
([Zhang & Shu (2010)](/sources/zhang-2010.md), §4.5;
[Zhang & Shu (2012)](/sources/zhang-2012.md), Example 5.3).

**Results.** Negative density or pressure arises below and to the right
of the corner. Cockburn and Shu's DG needed an ad hoc positivity
correction. With the [scaling limiter](/methods/positivity-preserving-scaling-limiter.md),
RKDG (TVB $M = 100$) and FD WENO5 ($h = 1/80$) never produce negative
values, and their results match the published ones. A reactive variant —
detonation diffraction at a 90° corner — is run with the same limiter
([Zhang & Shu (2012)](/sources/zhang-2012.md), Example 5.5).

**Later uses (batch 7).**
* *DG with only the positivity limiter* at $h = 1/64$, degree 2–3 on
  rectangles: the Euler run is highly oscillatory and at degree 3 the
  oscillations shift the shock; the Navier–Stokes run at $\mathrm{Re} = 200$
  is clean ([Zhang (2017)](/sources/zhang-2017.md), Example 7).

**Later uses (batch 8).**
* *A 90° corner in the unit square, as a shock-instability test.* A Mach
  5.09 shock on $[0,1]^2$ with $400\times400$ cells and the corner at
  $(0.05, 0.45)$, run to $t = 0.1561$ at second order. HLLC and HLLEM
  partly distort the diffracted normal shock. Selective wave modification
  and anti-diffusion control keep it, the latter most cleanly
  ([Simon & Mandal (2019)](/sources/simon-2019.md), §9.6; [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.4).
* With the corner at the middle of the left boundary, $t = 0.15$, second
  order: Godunov, Roe, HLLEM and HLLC all show post-shock oscillations,
  which the entropy-control term removes ([Xie et al. (2021)](/sources/xie-2021.md), §6.2).
* The failure in both is [numerical shock instability](/definitions/numerical-shock-instability.md),
  not positivity.

# Citations

1. [Zhang & Shu (2010)](/sources/zhang-2010.md), §4.5.
2. [Zhang & Shu (2012)](/sources/zhang-2012.md), Examples 5.3, 5.5.
3. [Zhang (2017)](/sources/zhang-2017.md), Example 7.
4. [Simon & Mandal (2019)](/sources/simon-2019.md), §9.6.
5. [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.4.
6. [Xie et al. (2021)](/sources/xie-2021.md), §6.2.
