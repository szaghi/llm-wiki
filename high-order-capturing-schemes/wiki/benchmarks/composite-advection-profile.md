---
type: Benchmark
title: "Composite-profile linear advection (Jiang–Shu test)"
description: "Linear advection on a periodic domain of a combination of narrow Gaussians, a square wave, a sharp triangle and a half-ellipse: separates smooth-but-sharp peaks from true discontinuities, and exposes extremum clipping and phase error over long times."
status: established
aliases: [Jiang-Shu linear test, Shu's linear test, four-wave advection]
tags: [benchmark, linear-advection, dispersion, critical-points]
timestamp: 2026-10-13T00:00:00Z
---

# Composite-profile linear advection (Jiang–Shu test)

**Set-up.** $u_t + u_x = 0$ on $[-1, 1]$, periodic, with initial data
made of a smooth but narrow combination of Gaussians, a square wave, a
sharp triangle and a half-ellipse, left to right
([Jiang & Shu (1996)](/sources/jiang-1996.md), §8.1 Example 1;
constants as printed by [Levy, Puppo & Russo (1999)](/sources/levy-1999.md),
written in words because their paper symbols collide with the registry:
the Gaussians are centred at $-0.7$ and $-0.7 \pm 0.005$ with exponent
coefficient $\log 2/(36\times 0.005^2)$, and the half-ellipses centred at
$0.5$ and $0.5 \pm 0.005$ with inverse half-width 10).

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
* After ten traversals of the 200-zone grid (the profile advected over
  2000 mesh points), $r = 5$ MPWENO keeps peak
  heights, the inflection that distinguishes the Gaussians from the
  triangle, symmetric profiles and about seven points across the square
  wave's edges; PPM flattens every peak and its steepener squares and
  skews them ([Balsara & Shu (2000)](/sources/balsara-2000.md), §VI.a,
  Fig. 1; [PPM](/methods/ppm.md)).

**Later uses (batch 2).** WENO-Z behaves like WENO-M, both better than
WENO-JS, at $t = 8$ with 200 and 400 points ([Borges et al. (2008)](/sources/borges-2008.md));
at eleventh order with 200 points, $q = 1$ oscillates for all of JS, Z, M,
$q = 2$ only for WENO-M, $q = r - 1$ for none ([Castro et al. (2011)](/sources/castro-2011.md));
WENO-AO(7,5,3) over 4000 points improves on AO(5,3) and on WENO-ZQ, which
shows overshoots as published and flattening once modified
([Balsara, Garain & Shu (2016)](/sources/balsara-2016.md);
`Contradictions` on [adaptive-order WENO](/methods/weno-ao.md)); a
seventh-order $L^1$-indicator scheme against WENO-BS7 and WENO-Z7
([Rathan & Naga Raju (2017)](/sources/rathan-2017.md)).

**Later uses (batch 4).** The same profile in the density of the
linearized Euler equations, run for ten periods ($t = 20$) on 3D
tetrahedral meshes stretched 1:20 into thin plates ($L = 0.3$) or
needles ($L = 0.00075$). ADER-FV with
[polynomial WENO](/methods/polynomial-weno.md) of second to fourth order
improves with order and stays essentially non-oscillatory. The reason
is that the stencils are regular in the reference coordinates
([Dumbser & Käser (2007)](/sources/dumbser-2007.md), §5.3.2).

**Later uses (batch 7).**
* On 400 zones to $t = 10$ at CFL 0.6: MC with RK2 degrades badly; classical
  PPM with RK3 keeps the Gaussian, triangle and ellipse distinguishable,
  with an upwind bias on the ellipse; third- and fourth-order CWENO show no
  over- or undershoots. The resolution and run length differ from the
  200-zone, ten-traversal comparison above, so the better showing of PPM is
  not a contradiction ([Balsara (2017)](/sources/balsara-2017-d.md), §§II–III).

# Citations

1. [Jiang & Shu (1996)](/sources/jiang-1996.md), §8.1.
2. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §4.1 Example 2.
3. [Levy, Puppo & Russo (1999)](/sources/levy-1999.md), Test 4.
4. [Balsara & Shu (2000)](/sources/balsara-2000.md), §VI.a.
5. [Borges et al. (2008)](/sources/borges-2008.md), §5.1.
6. [Castro, Costa & Don (2011)](/sources/castro-2011.md), §5.2.
7. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §5.1.
8. [Rathan & Naga Raju (2017)](/sources/rathan-2017.md), Example 3.
9. [Dumbser & Käser (2007)](/sources/dumbser-2007.md), §5.3.2.
10. [Balsara (2017)](/sources/balsara-2017-d.md), §§II–III.
