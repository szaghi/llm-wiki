---
type: Benchmark
title: "Orszag–Tang vortex (2D MHD)"
description: "Smooth periodic MHD data that steepen into interacting shocks and current sheets; the standard 2D test of shock capturing and divergence control in ideal MHD."
status: established
aliases: [Orszag-Tang problem, Orszag-Tang vortex]
tags: [benchmark, mhd, 2d, divergence-free]
timestamp: 2026-10-08T00:00:00Z
---

# Orszag–Tang vortex

**Set-up.** Doubly periodic; in the normalization of Christlieb et al.
$\rho = \gamma^2$, $\mathbf v = (-\sin y, \sin x, 0)$,
$\mathbf B = (-\sin y, \sin 2x, 0)$, $A_z(0) = \frac12\cos 2x + \cos y$ on
$[0, 2\pi]^2$, $\gamma = 5/3$
([Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.3).

**Results.**
* PIF-WENO with unstaggered [constrained transport](/methods/constrained-transport.md)
  agrees with the literature at $t = 0.5, 2, 3, 4$ on $192^2$. Without CT
  non-physical features appear by $t = 1.5$ and the run crashes at
  $t = 1.67$. The positivity limiter, not needed here, changes little
  ([Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.3, Figs. 4–6).
  Run to $t = 30$, the energy error from the limiter's correction stays
  small and decreases with refinement (§6.7).
* Divergence-preserving AFD-WENO with a Yee-staggered field performs
  well at third to ninth order
  ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.2).

**Later uses (batch 4).** In the $4\pi$-scaled normalization
($\rho = \gamma^2$, $p = \gamma$,
$\mathbf B = \sqrt{4\pi}(-\sin y, \sin 2x)$, $\gamma = 5/3$) with GLM
divergence cleaning:
* third-order ADER-WENO with AMR (equivalent $800^2$) to $t = 5$
  matches the uniform fine grid, Jiang and Wu's fifth-order FD-WENO and
  an unstructured WENO solution, at 1.8 times less CPU ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4);
* ADER-DG with $K = 5$, subcell limiting and AMR (equivalent $270^2$)
  agrees with the uniform grid and the same references ([Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.2.2).

# Citations

1. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §§6.3, 6.7.
2. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.2.
3. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4, Table 5.
4. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.2.2.
