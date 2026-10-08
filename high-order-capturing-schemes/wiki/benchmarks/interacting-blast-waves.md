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

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §7, Figs. 17–19.
2. [Shu & Osher (1989)](/sources/shu-1989.md), Example 7.
3. [Jiang & Shu (1996)](/sources/jiang-1996.md), §8.2 Example 3.
4. [Levy, Puppo & Russo (1999)](/sources/levy-1999.md), Test 8.
5. [Balsara & Shu (2000)](/sources/balsara-2000.md), §VI.b, Fig. 2.
