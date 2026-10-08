---
type: Benchmark
title: "MHD blast wave in a low-β medium"
description: "An over-pressured region expanding into a strongly magnetized, low-pressure background; strong anisotropic shocks against tiny thermal pressure make it the standard positivity stress test for MHD, also run in relativistic MHD."
status: established
aliases: [magnetized blast wave, MHD blast problem, RMHD blast wave]
tags: [benchmark, mhd, positivity, low-beta, 2d, 3d]
timestamp: 2026-10-08T00:00:00Z
---

# MHD blast wave in a low-β medium

**Set-up.** A piecewise-constant pressure — high inside a small
sphere, low outside — with constant density, zero velocity and a
uniform oblique field $B_x = B_y = 100/\sqrt{8\pi}$
([Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.6). Wu and
Shu's two variants, BLAST-I and BLAST-II, differ in field and pressure
strengths ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.2).
The relativistic version follows Komissarov and Mignone–Bodo: domain
$[-6,6]^2$, explosion density $10^{-2}$ and pressure 1 within radius
0.8, ambient $10^{-4}$ and $5\times10^{-4}$ beyond radius 1, field 0.1,
$\gamma = 4/3$, $t = 4$ (§7.3).

**Results.**
* PIF-WENO with CT: negative pressure appears at the first (2D, $256^2$)
  or second (3D, $150^3$) step without the positivity limiter. With it
  the results match the literature at $t = 0.01$, and the limiter's
  energy error stays below 1% except on the coarsest meshes
  ([Christlieb et al. (2016)](/sources/christlieb-2016.md), §§6.6–6.7).
* Divergence-preserving AFD-WENO needs its PCP variant for both
  variants (3D $300^3$; 2D $400^2$, fifth order, $t = 0.01$), and runs
  the RMHD blast at fifth order on $512^2$
  ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§7.2–7.3;
  [flux limiter](/methods/positivity-preserving-flux-limiter.md)).

# Citations

1. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §§6.6–6.7.
2. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§7.2–7.3.
