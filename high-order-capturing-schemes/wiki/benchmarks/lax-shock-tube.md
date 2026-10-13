---
type: Benchmark
title: "Lax shock tube"
description: "The 1D Riemann problem (0.445, 0.698, 3.528 | 0.5, 0, 0.571), with a strong contact and an intermediate state that must be built up; a hard test for component-wise high-order schemes."
status: established
aliases: [Lax problem, Lax's problem]
tags: [benchmark, euler, riemann-problem, 1d]
timestamp: 2026-10-13T00:00:00Z
---

# Lax shock tube

**Set-up** (Lax 1954): $(\rho, v, p)_L = (0.445, 0.698, 3.528)$,
$(\rho, v, p)_R = (0.5, 0, 0.571)$, $\gamma = 1.4$
([Liu, Osher & Chan (1994)](/sources/liu-1994.md);
[Jiang & Shu (1996)](/sources/jiang-1996.md)).

**Why it is hard.** Component-wise fourth-order ENO is much noisier here
than on [Sod's problem](/benchmarks/sod-shock-tube.md); characteristic
reconstruction removes most of the noise; even at shocks the
reconstruction's jumps carry only about 35 % of the shock, the smooth
polynomial part the rest ([Harten et al. (1987)](/sources/harten-1987.md),
Figs. 12–16; [characteristic decomposition](/methods/characteristic-decomposition.md)).
Jiang and Shu call it, with Sod's, a tough case for non-characteristic
schemes of order three or more, where oscillations easily appear.

**Uses.** [Shu & Osher (1989)](/sources/shu-1989.md) (Example 6,
contact sharpening); [Liu, Osher & Chan (1994)](/sources/liu-1994.md)
(WENO $r = 3$); [Jiang & Shu (1996)](/sources/jiang-1996.md) (WENO-LF-5-PS
performs well here); [Suresh & Huynh (1997)](/sources/suresh-1997.md)
(MP5); [Levy, Puppo & Russo (1999)](/sources/levy-1999.md) (Test 6:
wiggles at the contact decay under refinement; global and density
indicators clearly better than component-wise ones).

**Later uses (batch 2).** [Henrick et al. (2005)](/sources/henrick-2005.md)
(WENO5M sharper, ENO property kept); [Borges et al. (2008)](/sources/borges-2008.md)
(with Sod and the 123 problem); [Castro et al. (2011)](/sources/castro-2011.md)
(ninth order: WENO-M needs the largest $q$ to be non-oscillatory);
[Hu, Wang & Adams (2010)](/sources/hu-2010.md); [Fu, Hu & Adams (2016)](/sources/fu-2016.md)
(WENO-CU6-M overshoots at the contact); [Zhu & Qiu (2016)](/sources/zhu-2016.md);
[Balsara, Garain & Shu (2016)](/sources/balsara-2016.md) (no overshoots
with AO(5,3) and AO(9,5,3)); [Rathan & Naga Raju (2017)](/sources/rathan-2017.md).

**Later uses (batch 3).** Compact-reconstruction WENO on 200 points is
sharper than WENO-JS and WENO-Z. With 60 points (0.57 s) it matches
WENO-JS with 100 (0.55 s) ([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 2).
Seventh-order AFD-WENO captures the rarefaction, contact and shock
([Balsara et al. (2025)](/sources/balsara-2025.md), §VII.a).

**Later uses (batch 4).**
* RKDG with WENO limiters, 200 cells, $t = 1.3$. Contact resolution
  improves as the TVB constant $M$ grows and fewer cells are flagged
  ([Qiu & Shu (2005)](/sources/qiu-2005.md), Example 3.6).
* ADER-DG with $K = 9$ and subcell limiting on $20\times5$ cells to
  $t = 0.14$, alone ([Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.1) and with AMR ([Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.2). The
  shock stays within one main cell and the contact stays unlimited
  ([a posteriori subcell limiting](/methods/a-posteriori-subcell-limiting.md)).

**Later uses (batch 5).**
* Fifth-order alternative FD with MP5 on a 1D refined grid and on a
  refined polar grid, $t = 1.3$. The density oscillates more on the refined
  grid because a resolution change sits just behind the contact. Finer
  runs converge, and in 2D the shock front stays straight across the
  refined box ([Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), §5.5).
* With regridding every 10 steps, non-conservative WENO inter-level
  interpolation oscillates behind the contact and gets the shock speed
  wrong; the hybrid conservative interpolation matches the reference
  ([Wang et al. (2025)](/sources/wang-2025.md), §6.3.2, preprint;
  [high-order AMR](/methods/high-order-amr.md)).

**Later uses (batch 7).**
* DG of degree 2–7 on 200 cells with only the positivity limiter is
  oscillatory for Euler; the Navier–Stokes version ($\mathrm{Re} = 100$, 1000)
  is compared with a 64000-point reference ([Zhang (2017)](/sources/zhang-2017.md), Example 2).

**Later uses (batch 11, merged at the 2026-10-13 deep lint).**
* Lax's states on 100 cells at second order (MUSCL), end time not
  printed: the rarefaction and the shock are "almost identical" with HLL,
  HLLC and HLL-BVD, and HLL-BVD smears the contact "slightly" less
  ([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §III C, Fig. 4).
* The same paper's "strong Lax problem" is not Lax's problem despite the
  name: $(\rho, v_x, p) = (1, -19.59745, 1000)$ for $x \le 0.8$ and
  $(1, -19.59745, 0.01)$ otherwise, to $t = 0.012$, a strong shock with a
  stationary contact. HLLC resolves the contact best but "produces the
  largest overshoot values across the shock"; HLL-BVD is much sharper
  than HLL without overshoot (§III C 1, Figs. 5–6).

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §7.
2. [Shu & Osher (1989)](/sources/shu-1989.md), Example 6.
3. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), Example 4.
4. [Jiang & Shu (1996)](/sources/jiang-1996.md), §8.2 Example 1.
5. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §4.2 Example 2.
6. [Levy, Puppo & Russo (1999)](/sources/levy-1999.md), Test 6.
7. [Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md), §5.6.
8. [Borges et al. (2008)](/sources/borges-2008.md), §5.2.1.
9. [Castro, Costa & Don (2011)](/sources/castro-2011.md), §5.3.
10. [Hu, Wang & Adams (2010)](/sources/hu-2010.md), §3.2.
11. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §5.2.
12. [Zhu & Qiu (2016)](/sources/zhu-2016.md), Example 3.5.
13. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §5.2.
14. [Rathan & Naga Raju (2017)](/sources/rathan-2017.md), Example 6.
15. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 2.
16. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §VII.a.
17. [Qiu & Shu (2005)](/sources/qiu-2005.md), Example 3.6.
18. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.1.
19. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.2.
20. [Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), §5.5 (accepted manuscript).
21. [Wang et al. (2025)](/sources/wang-2025.md), §6.3.2 (arXiv preprint).
22. [Zhang (2017)](/sources/zhang-2017.md), Example 2.
23. [Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §III C, Figs. 4–6.
