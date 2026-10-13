---
type: Benchmark
title: "Shu–Osher shock/entropy-wave interaction"
description: "A Mach 3 shock running into a sinusoidal density (entropy) field: smooth structure behind a shock, where high-order capturing schemes show their largest advantage over TVD schemes."
status: established
aliases: [Shu-Osher problem, shock-entropy wave interaction, Shu's problem]
tags: [benchmark, euler, turbulence, high-order]
timestamp: 2026-10-13T00:00:00Z
---

# Shu–Osher shock/entropy-wave interaction

**Set-up** ([Shu & Osher (1989)](/sources/shu-1989.md), Example 8). The
1D Euler equations with a right-moving Mach 3 shock entering a state
whose density carries a sine perturbation of amplitude 0.2 (amplitude
0 is a pure shock; written in words, since $\varepsilon$ is the weight
regularization). The post-shock
state printed in later uses is
$(\rho, v, p) = (3.857143,\ 2.629369,\ 10.3333)$
([Jiang & Shu (1996)](/sources/jiang-1996.md);
[Suresh & Huynh (1997)](/sources/suresh-1997.md)). The interaction
generates a band of fine density oscillations behind the shock.

**What it measures.** Accuracy of smooth structure behind a shock: the
whole difficulty is resolving the oscillations without shock-generated
noise. Results in this corpus:
* third-order ENO-RF with 200 points matches a second-order MUSCL TVD
  scheme with 800 in density; velocity and pressure, lacking structure,
  gain less ([Shu & Osher (1989)](/sources/shu-1989.md));
* $r = 5$ MPWENO with 200 zones converges to an 800-zone reference, every
  extremum matched with no more than 11 points between extrema; $r = 3$
  WENO needs 400 ([Balsara & Shu (2000)](/sources/balsara-2000.md), §VI.d);
* MP5 and WENO5 compared by [Suresh & Huynh (1997)](/sources/suresh-1997.md).

**Weak-wave variant** ([Jiang & Shu (1996)](/sources/jiang-1996.md),
§8.2 Example 2). Amplitude 0.01, wave number $k = 13$ on
$[0, 5]$; the shock is run to $x = 4.5$ and shuffled back to remove the
start-up transient. The amplified entropy wave is compared with the
linear-theory amplitude 0.08690716. At 800 points (about 20 per
wavelength) the fourth-order Liu–Osher–Chan WENO is best and WENO5
second; at 1200 they are equal, and WENO5 wins on finer grids. A
second-order TVD scheme with 2000 points is clearly worse.

**2D variant** (Example 4 of §8.3): a normal Mach 3 shock and an oblique
weak entropy wave; linear-theory amplitude 0.08744786. ENO-LF-4/5 lose
accuracy unless biased; WENO works without modification, and the biased
"WENO2" variants are better still; the pressure–entropy weights fail.

**Later uses (batch 2).** Standard set-up on $[-5,5]$ to $t = 1.8$:
* WENO5M resolves the post-shock waves better than WENO5 at 400 points,
  "particularly … where the solution's first derivative vanishes"
  ([Henrick et al. (2005)](/sources/henrick-2005.md));
* WENO-M and WENO-Z at 200–300 points capture much more of the
  high-frequency field than WENO-JS, also at $k = 10$
  ([Borges et al. (2008)](/sources/borges-2008.md)); at orders 5–11 the
  dissipation ranks JS > Z > M for each $q$
  ([Castro et al. (2011)](/sources/castro-2011.md));
* WENO-SYM resolves the extrema WENO-JS damps; a weak Mach 1.1 variant
  and oblique versions at 22° and 45° ([Martín et al. (2006)](/sources/martin-2006.md));
* WENO-CU6 beats WENO5, WENO-M and WENO-SYM
  ([Hu, Wang & Adams (2010)](/sources/hu-2010.md)); TENO6 and TENO5-opt
  keep the entropy-wave amplitude best ([Fu, Hu & Adams (2016)](/sources/fu-2016.md));
* WENO-ZQ better than WENO-JS at 400 points ([Zhu & Qiu (2016)](/sources/zhu-2016.md));
  WENO-AO closer to the reference at higher order
  ([Balsara, Garain & Shu (2016)](/sources/balsara-2016.md));
* hybrid compact-WENO H7 best at 200 points, H5 better than WENO5 and WENO7
  ([Pirozzoli (2002)](/sources/pirozzoli-2002.md));
* the seventh-order $L^1$-indicator scheme against WENO-BS7 and WENO-Z7
  ([Rathan & Naga Raju (2017)](/sources/rathan-2017.md)).

**Later uses (batch 3).**
* A modified version — a Mach 1.1 shock into a $1 + 0.1\sin 20\pi x$
  density field, run to $t = 5$, more than ten times the usual time —
  on 2000 cells: the Rusanov-based FV-WENO severely damps the acoustic
  wave spreading upstream, while WENO-HLLC and WENO-MUSTA are about
  twice as accurate ([Titarev & Toro (2004)](/sources/titarev-2004.md), §5.1).
* Compact-reconstruction WENO captures the post-shock structures better
  than WENO-JS and WENO-Z at 200 and 400 points
  ([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 4).
* GP-WENO on 200 cells: GP-R3 is least diffusive; GP-R2 has slightly
  better amplitudes than WENO-JS. With $\ell/h = 3$, about half the
  post-shock wavelength, it is much more accurate; for large $\ell$ it
  approaches WENO-JS ([Reyes et al. (2018)](/sources/reyes-2018.md), §5.3;
  [GP-WENO](/methods/gp-weno.md)).

**Later uses (batch 4).**
* RKDG with WENO limiters, 200 cells. Raising the TVB constant flags
  fewer cells and resolves the post-shock waves better, but at
  $M = 300$ the weak shocks go unflagged and small oscillations appear
  ([Qiu & Shu (2005)](/sources/qiu-2005.md), Example 3.7).
* Fourth-order ADER-WENO on 200 zones has almost converged to an
  800-zone reference and shows all its extrema, with no more than 11
  points between extrema. Third order is close, and a TVD MC-limiter
  scheme misses the reference by a wide margin ([Balsara et al. (2009)](/sources/balsara-2009.md), §6.2).
* ADER-DG with $K = 9$ and subcell limiting on $40\times5$ cells. The
  shock is kept as a jump over one or two subcells, and the leftmost
  steepening waves, contained within single cells, are flagged before
  they become shocks. The paper prints the pre-shock density as
  $1 + 0.2\sin(5\pi x)$ and the final time as $0.18$. These differ from the
  $\sin(5x)$ and $t = 1.8$ printed by Qiu and Shu (2005) and recorded
  here as printed ([Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.3).

**Later uses (batch 5).** On $[0, 10]$ with the shock at $x = 1$ and
density $1 + 0.2\sin(5x)$, two AMR levels on a base of 128 points against a
2048-point reference: hybrid and WENO inter-level interpolation are less
dissipative than Berger–Colella second-order interpolation. The caption
gives $t = 0.2$, and no error numbers are reported
([Wang et al. (2025)](/sources/wang-2025.md), §6.3.3, preprint).

**Later uses (batch 9).** The Titarev–Toro variant ($[-5, 5]$,
$1 + 0.1\sin 20\pi x$, $t = 5$) with degree-3 SBP DG on 256 elements and
no shock capturing gives indistinguishable results with and without
relaxation ([Ranocha et al. (2020)](/sources/ranocha-2020.md), §4.4, Fig. 10). The printed left-state
velocity lacks its decimal point ("0523346").

**Later uses (batch 15).** *The baseline interpolation of the batch-5
comparison.* The 1989 algorithm fills fine ghost cells from coarser data
by bilinear interpolation in space and linear interpolation in time,
which is second order; it states no limiter and no conservation
constraint, and does not specify the interpolation that initializes new
fine grids ([Berger & Colella (1989)](/sources/berger-1989.md), §4;
[high-order AMR](/methods/high-order-amr.md)). The batch-5 line agrees
with it on the order; the 1989 paper has no Shu–Osher run.

# Citations

1. [Shu & Osher (1989)](/sources/shu-1989.md), §V Example 8.
2. [Jiang & Shu (1996)](/sources/jiang-1996.md), §§8.2–8.3.
3. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §4.2 Example 3.
4. [Balsara & Shu (2000)](/sources/balsara-2000.md), §VI.d.
5. [Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md), §5.4.
6. [Borges et al. (2008)](/sources/borges-2008.md), §5.2.2.
7. [Castro, Costa & Don (2011)](/sources/castro-2011.md), §5.4.
8. [Martín et al. (2006)](/sources/martin-2006.md), §§5.3–5.5.
9. [Hu, Wang & Adams (2010)](/sources/hu-2010.md), §3.4.
10. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §5.4.
11. [Zhu & Qiu (2016)](/sources/zhu-2016.md), Example 3.6.
12. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §5.4.
13. [Pirozzoli (2002)](/sources/pirozzoli-2002.md), §5.2.
14. [Rathan & Naga Raju (2017)](/sources/rathan-2017.md), Example 7.
15. [Titarev & Toro (2004)](/sources/titarev-2004.md), §5.1.
16. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 4.
17. [Reyes et al. (2018)](/sources/reyes-2018.md), §5.3.
18. [Qiu & Shu (2005)](/sources/qiu-2005.md), Example 3.7.
19. [Balsara et al. (2009)](/sources/balsara-2009.md), §6.2.
20. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.3.
21. [Wang et al. (2025)](/sources/wang-2025.md), §6.3.3 (arXiv preprint).
22. [Ranocha et al. (2020)](/sources/ranocha-2020.md), §4.4 (arXiv v4).
23. [Berger & Colella (1989)](/sources/berger-1989.md), §4.
