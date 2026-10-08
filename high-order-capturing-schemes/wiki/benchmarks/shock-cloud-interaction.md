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

# Citations

1. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.5.
2. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.3.
