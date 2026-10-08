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

# Citations

1. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §§6.3, 6.7.
2. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.2.
