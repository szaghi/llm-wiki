---
type: Benchmark
title: "Woodward–Colella interacting blast waves"
description: "Two strong blast waves between reflecting walls that collide (pressures 1000, 0.01, 100; t = 0.038): tests robustness, positivity and contact resolution in a confined, strongly interacting flow."
status: established
aliases: [two interacting blast waves, Woodward-Colella blast wave, double blast wave]
tags: [benchmark, euler, strong-shocks, positivity]
timestamp: 2026-10-13T00:00:00Z
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

**Later uses (batch 4).**
* RKDG with WENO limiters, $K = 1$–$3$, 400 cells, at $t = 0.038$.
  Resolution improves with the TVB constant up to $M = 10$, but $M = 300$
  is slightly worse. It improves from $K = 1$ to 2 and deteriorates
  slightly from 2 to 3 ([Qiu & Shu (2005)](/sources/qiu-2005.md), Example 3.8;
  [WENO limiters for DG](/methods/weno-limited-dg.md)).
* Fourth-order ADER-WENO with a linearized Riemann solver at CFL 0.8:
  400 zones capture the left-going contact and every structure of a
  1600-zone run ([Balsara et al. (2009)](/sources/balsara-2009.md), §6.1).
* Third-order ADER-WENO with two AMR levels on a $300\times10$ base
  grid, in 2D with periodic $y$ and reflecting $x$. It agrees with a
  3600-point TVD reference at the collision ($t = 0.028$) and at
  $t = 0.038$ ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4).
* Reflecting walls by weighted least-squares extrapolation (WLS-GAW)
  give satisfactory profiles against a $h = 1/16000$ reference
  ([Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §5.1.3; [weighted extrapolation](/methods/weighted-extrapolation.md)).

**Later uses (batch 5).** With the reflecting walls imposed by
inverse Lax–Wendroff ghost values instead of mirroring:
* Fifth-order SILW conserves mass and energy only to truncation level,
  with errors growing to about $2\times10^{-3}$ and $5\times10^{-3}$ by
  $t = 0.5$ at $N = 1600$. Exactly conservative boundary fluxes bring
  both to $10^{-15}$. In a long run ($t = 19$, $N = 800$) the
  non-conservative shock is visibly misplaced
  ([Ding, Shu & Zhang (2020)](/sources/ding-2020.md), Example 4, Tables 2.8–2.9, Fig. 2.5;
  [inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md)).
* The flux-based ILW with the wall imposed as zero mass flux agrees at
  $t = 0.038$ with a mirrored-wall reference on $h = 1/5120$
  ([Lu et al. (2021)](/sources/lu-2021.md), Example 3.4).

**Later uses (batch 9).** Run to $t = 0.04$, not $0.038$, with the TVD
MC scheme on $h = 1/512$, to show a variable-step SSP multistep method's
step following the largest wave speed: it grows as the shocks approach,
drops at the collision and grows again, with the Courant number near
$1/4$ (second order) and $1/6$ (third order) ([Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md), §6.6,
Fig. 1b; [SSP linear multistep methods](/methods/ssp-linear-multistep.md)).

**Later uses (batch 11).** *The Woodward–Colella paper.*
[Woodward & Colella (1984)](/sources/woodward-1984.md) (§IVa) print the
set-up above: gas at rest between reflecting walls 1 apart, $\rho = 1$,
$p = 1000$, 0.01 and 100 with interfaces at 0.1 and 0.9, $\gamma = 1.4$,
results displayed at $t = 0.038$ (§VIa prints "0.38", a typo). They
state that the problem "was introduced in" Woodward (1982, *Parallel
Computation*). This qualifies the set-up line above: the name
"Woodward–Colella" is the conventional one, the origin is Woodward (1982).
* *Reference solution.* A PPMLR run that tracks the two contacts as three
  fluids, is exact before the waves interact, and refines by 8 in space
  and time near each discontinuity and the walls: 3096 zones of width
  $1/2400$ to $1/9600$.
* *Flow.* The blast waves collide at $t \approx 0.028$, in agreement with
  the batch-4 remark above. The peak density stays below the limiting 36
  (accurate to about 1 %) and falls to about 24 by $t = 0.030$. At the end
  the left and middle contacts carry most of the error.
* *Quantitative comparison* (Table I, 200 to 1200 zones, CRAY-1). The
  error is the mean absolute deviation of cell-average density from the
  reference. At 200 and 1200 zones: PPMLR 0.0760 and 0.0133, PPMDE 0.0990
  and 0.0144, MUSCL 0.162 and 0.0401, ETBFCT 0.227 and 0.0606, BBC 0.196
  and 0.0717, MacCormack 0.261 and 0.0862, Godunov 0.330 and 0.182. Only
  [PPM](/methods/ppm.md) converges at first order; Godunov's error goes
  like $h^{0.15}$ to $h^{0.4}$. Matching 200-zone PPMLR costs more CPU
  time by 1.6 (PPMDE), 6.2 (MUSCL), 7.4 (BBC), 8.0 (MacCormack) and 13.5
  (ETBFCT); Godunov cannot match it with 12 times the zones.
* *Profiles* (Fig. 6). Godunov smears the three contacts "unacceptably";
  ETBFCT shows a spurious contact at a density-slope discontinuity; both
  PPM forms keep the outer contacts one zone wide at 200 zones and are
  "essentially converged" at 1200.

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
15. [Qiu & Shu (2005)](/sources/qiu-2005.md), Example 3.8.
16. [Balsara et al. (2009)](/sources/balsara-2009.md), §6.1.
17. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4.
18. [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §5.1.3.
19. [Ding, Shu & Zhang (2020)](/sources/ding-2020.md), Example 4.
20. [Lu et al. (2021)](/sources/lu-2021.md), Example 3.4.
21. [Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md), §6.6 (arXiv v2).
22. [Woodward & Colella (1984)](/sources/woodward-1984.md), §§IVa, VIa, Figs. 1, 2, 6, Table I.
