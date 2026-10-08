---
type: Benchmark
title: "Composite-profile linear advection (Jiang–Shu test)"
description: "Linear advection on a periodic domain of a combination of narrow Gaussians, a square wave, a sharp triangle and a half-ellipse: separates smooth-but-sharp peaks from true discontinuities, and exposes extremum clipping and phase error over long times."
status: established
aliases: [Jiang-Shu linear test, Shu's linear test, four-wave advection]
tags: [benchmark, linear-advection, dispersion, extrema]
timestamp: 2026-10-08T00:00:00Z
---

# Composite-profile linear advection (Jiang–Shu test)

**Set-up.** $u_t + u_x = 0$ on $[-1, 1]$, periodic, with initial data
made of a smooth but narrow combination of Gaussians, a square wave, a
sharp triangle and a half-ellipse, left to right
([Jiang & Shu (1996)](/sources/jiang-1996.md), §8.1 Example 1;
constants $a = 0.5$, $z = -0.7$, $\delta = 0.005$, $\alpha = 10$,
$\beta = \log 2/(36\delta^2)$ as printed by
[Levy, Puppo & Russo (1999)](/sources/levy-1999.md)).

**What it shows.**
* WENO4 and WENO5 beat ENO4 on all four waves; WENO4 is better at the
  spike-like peaks, WENO5 at the square wave and obtuse turns; with Yang's
  compression (CFL lowered to 0.2) WENO5 is best everywhere
  ([Jiang & Shu (1996)](/sources/jiang-1996.md); 200 points, $t = 8$).
* MP5 compares favourably with WENO5 and ENO3 after one and ten periods,
  200 cells, CFL 0.4 ([Suresh & Huynh (1997)](/sources/suresh-1997.md),
  Figs. 4.1–4.2).
* Third-order central WENO shows no spurious oscillation, sharper contacts
  in the square wave than WENO/ENO with Roe flux, and an unexplained
  asymmetry in the right hump at 400 cells
  ([Levy, Puppo & Russo (1999)](/sources/levy-1999.md), Fig. 5.2).
* After ten traversals (2000 mesh points), $r = 5$ MPWENO keeps peak
  heights, the inflection that distinguishes the Gaussians from the
  triangle, symmetric profiles and about seven points across the square
  wave's edges; PPM flattens every peak and its steepener squares and
  skews them ([Balsara & Shu (2000)](/sources/balsara-2000.md), §VI.a,
  Fig. 1; [PPM](/methods/ppm.md)).

# Citations

1. [Jiang & Shu (1996)](/sources/jiang-1996.md), §8.1.
2. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §4.1 Example 2.
3. [Levy, Puppo & Russo (1999)](/sources/levy-1999.md), Test 4.
4. [Balsara & Shu (2000)](/sources/balsara-2000.md), §VI.a.
