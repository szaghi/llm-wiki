---
type: Benchmark
title: "Shock–cloud interaction (MHD and relativistic MHD)"
description: "A strong magnetized shock overrunning a dense stationary cloud; tests resolution of the shocked cloud's fine structure and robustness, in 2D and 3D ideal MHD and in relativistic MHD."
status: established
aliases: [cloud-shock interaction, shock-cloud problem]
tags: [benchmark, mhd, 2d, 3d]
timestamp: 2026-10-08T00:00:00Z
---

# Shock–cloud interaction

**Set-up (MHD).** On $[0,1]^2$ (or $[0,1]^3$) a shock at $x = 0.05$
moves into a medium containing a stationary cloud of density 10 and
radius 0.15 centred at $(0.25, 0.5)$; uniform transverse field,
$t = 0.06$ ([Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.5).

**Results.**
* PIF-WENO with CT captures the shock-like structure near $x = 0.75$,
  as the authors' earlier SSP-RK solver did and some earlier results
  did not; $512^2$ resolves much more structure than $256^2$. In 3D at
  $256^3$ a very-low-pressure structure appears at $t = 0.0378$ and
  requires the positivity limiter; it is absent at $128^3$ and with the
  SSP-RK solver ([Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.5).
* A relativistic-MHD shock–cloud case is run at ninth order with
  divergence-preserving AFD-WENO
  ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.3, Fig. 20).

**Later uses (batch 6).**
* The original FD-WENO with unstaggered CT gives the full states: left
  $(3.86859, 11.2536, 0, 0, 167.345, 0, 2.1826182, -2.1826182)$ and right
  $(1, 0, 0, 0, 1, 0, 0.56418958, 0.56418958)$, cloud density 10, radius
  0.15, $256^2$, $t = 0.06$. The structure near $x = 0.75$ appears in a
  second-order FV code only at $512^2$, which the authors take as evidence
  that it is physical. A 2.5D version computes $B_z$ by CT, and a 3D run
  on $128^3$ has no positivity problem
  ([Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §7.4).
* A mirrored 3D version (shock at $x = 0.6$, cloud at $(0.8, 0.5, 0.5)$,
  upstream flow towards $-x$), MHD and relativistic, $256^3$. Order
  reduction with selective flux integration was "fundamental"
  ([Berta et al. (2024)](/sources/berta-2024.md), §5.8).

# Citations

1. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.5.
2. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.3.
3. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §7.4 (arXiv v2).
4. [Berta et al. (2024)](/sources/berta-2024.md), §5.8 (arXiv v4).
