---
type: Benchmark
title: "Lax shock tube"
description: "The 1D Riemann problem (0.445, 0.698, 3.528 | 0.5, 0, 0.571), with a strong contact and an intermediate state that must be built up; a hard test for component-wise high-order schemes."
status: established
aliases: [Lax problem, Lax's problem]
tags: [benchmark, euler, riemann-problem, 1d]
timestamp: 2026-10-08T00:00:00Z
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
