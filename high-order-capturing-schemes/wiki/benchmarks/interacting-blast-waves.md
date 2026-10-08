---
type: Benchmark
title: "Woodward–Colella interacting blast waves"
description: "Two strong blast waves between reflecting walls that collide (pressures 1000, 0.01, 100; t = 0.038): tests robustness, positivity and contact resolution in a confined, strongly interacting flow."
status: established
aliases: [two interacting blast waves, Woodward-Colella blast wave, double blast wave]
tags: [benchmark, euler, strong-shocks, positivity]
timestamp: 2026-10-08T00:00:00Z
---

# Woodward–Colella interacting blast waves

**Set-up** (Woodward & Colella, cited by all sources below). On
$[0, 1]$ with reflecting walls, $\rho = 1$, $v = 0$, and pressure
$1000$ for $x < 0.1$, $0.01$ in the middle, $100$ for $x > 0.9$
([Jiang & Shu (1996)](/sources/jiang-1996.md), printed values;
[Levy, Puppo & Russo (1999)](/sources/levy-1999.md)); $\gamma = 1.4$,
final time $t = 0.038$.

**Observations.**
* Fourth-order ENO with 800 cells shows all the interactions and serves
  as the converged solution; at 400 cells velocity and pressure are
  converged but density is not, the contacts being smeared. Second-order
  ENO is much worse at 200. Just before the collision the low-pressure
  region shrinks to one or two cells, where polynomial reconstruction can
  go negative; a positivity condition lowers the order locally, needed
  only during two time steps
  ([Harten et al. (1987)](/sources/harten-1987.md), §7;
  [ENO](/methods/eno-reconstruction.md)).
* With subcell resolution or artificial compression, 200 points give a
  better density than plain ENO-RF-3 with 400
  ([Shu & Osher (1989)](/sources/shu-1989.md), Example 7).
* WENO4 and WENO5 are far better than WENO3 and comparable to ENO-RF-4;
  WENO4 is slightly better on the medium grid, WENO5 on the fine one
  ([Jiang & Shu (1996)](/sources/jiang-1996.md), Example 3).
* Central WENO resolves both density peaks with no Riemann solver; the
  global indicator is less dissipative but shows small ENO-type wiggles
  ([Levy, Puppo & Russo (1999)](/sources/levy-1999.md), Test 8).
* MPWENO with artificial compression at 400 zones nearly matches a
  1000-zone result, the left-going contact well captured
  ([Balsara & Shu (2000)](/sources/balsara-2000.md), §VI.b; the text
  names $r = 5$, the figure caption $r = 6$).

**Later uses (batch 2).** WENO5M resolves the three contacts near
$x = 0.595, 0.765, 0.799$ better than WENO5 ([Henrick et al. (2005)](/sources/henrick-2005.md));
WENO-Z sharper than WENO-M at $x \approx 0.78$ and $0.86$
([Borges et al. (2008)](/sources/borges-2008.md)); WENO-CU6 improves the
valley at $0.75$ and the peak at $0.78$ with a slight overshoot at 400
points ([Hu, Wang & Adams (2010)](/sources/hu-2010.md)); TENO5/6 free of
the velocity overshoots of WENO-JS, WENO-Z and WENO-CU6, and WENO-CU6-M
fails ([Fu, Hu & Adams (2016)](/sources/fu-2016.md)); WENO-ZQ at 800
points ([Zhu & Qiu (2016)](/sources/zhu-2016.md)); WENO-AO(5,3) at 400
zones close to a 1000-zone result ([Balsara, Garain & Shu (2016)](/sources/balsara-2016.md)).

**Later uses (batch 3).** WENO-CU6-M1 cannot compute it without
limiting; with the cut-off positivity limiter at $h = 2.5\times10^{-3}$ it
is comparable to WENO-CU6-M2 ([Hu, Adams & Shu (2013)](/sources/hu-2013.md), §3.3).
Compact-reconstruction WENO with 200 cells resolves the smooth region
better than WENO-JS and WENO-Z ([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 5).
AFD-WENO on 1000 zones, with flattening, matches a 4000-zone reference
([Balsara et al. (2025)](/sources/balsara-2025.md), §VII.a).

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §7, Figs. 17–19.
2. [Shu & Osher (1989)](/sources/shu-1989.md), Example 7.
3. [Jiang & Shu (1996)](/sources/jiang-1996.md), §8.2 Example 3.
4. [Levy, Puppo & Russo (1999)](/sources/levy-1999.md), Test 8.
5. [Balsara & Shu (2000)](/sources/balsara-2000.md), §VI.b, Fig. 2.
6. [Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md), §5.5.
7. [Borges et al. (2008)](/sources/borges-2008.md), §5.2.3.
8. [Hu, Wang & Adams (2010)](/sources/hu-2010.md), §3.3.
9. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §5.3.
10. [Zhu & Qiu (2016)](/sources/zhu-2016.md), Example 3.7.
11. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §5.3.
12. [Hu, Adams & Shu (2013)](/sources/hu-2013.md), §3.3.
13. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 5.
14. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §VII.a.
