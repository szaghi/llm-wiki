---
type: Benchmark
title: "MHD rotor"
description: "A dense, rapidly spinning disc in a magnetized ambient medium launches torsional Alfvén waves; low-pressure regions make it a positivity test, especially in its very-low-β version."
status: established
aliases: [rotor problem, Balsara-Spicer rotor]
tags: [benchmark, mhd, 2d, positivity, low-beta]
timestamp: 2026-10-09T00:00:00Z
---

# MHD rotor

**Set-up** (Balsara and Spicer). On $[0,1]^2$ a disc of radius 0.1 with
density 10 rotates rigidly in a unit-density ambient. Density and
velocity taper linearly between radii 0.1 and 0.115 (Christlieb et al.,
the very-low-β version of Waagan, cited) or 0.13 (Balsara et al.)
([Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.4;
[Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.2).

**Results.**
* PIF-WENO with CT on $400^2$ to $t = 0.27$ matches the reference; the
  positivity-preserving [flux limiter](/methods/positivity-preserving-flux-limiter.md)
  is required, otherwise the code fails
  ([Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.4).
* Seventh-order divergence-preserving AFD-WENO on $256^2$ to $t = 0.29$
  ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.2, Fig. 13).

**Later uses (batch 4).** Variants differ in taper and $\gamma$.
* Balsara et al.: $[-0.5, 0.5]^2$, $200^2$, $\mathbf B = (2.5, 0)$,
  $p = 1$, taper 0.1–0.13 (six zones, to be kept under refinement),
  $\gamma = 5/3$. Fourth-order ADER-WENO with a linearized solver to
  $t = 0.29$ agrees with Balsara and Spicer ([Balsara et al. (2009)](/sources/balsara-2009.md), §7.3).
* Dumbser et al. and Zanotti et al.: $[-0.6, 0.6]^2$, taper only
  0.1–0.105, $\gamma = 1.4$, GLM cleaning, $t = 0.25$. Third-order
  ADER-WENO with AMR (equivalent $960^2$) uses more than five times
  fewer elements. Thanks to the cleaning, it shows no spurious
  oscillations in density or magnetic pressure ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4, Table 6).
  ADER-DG with $K = 5$ and subcell limiting on AMR (equivalent $800^2$)
  matches the uniform grid ([Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.2.1).

**Later uses (batch 6).**
* *Second order.* Unit square, $200^2$, $B = 2.5$, $p = 1$, taper 0.1–0.13,
  $\gamma = 5/3$, $t = 0.29$, with divergence-free reconstruction and HLLE:
  consistent with Balsara and Spicer ([Balsara (2004)](/sources/balsara-2004.md), §7.2).
  The RK-WENO fourth-order sibling of the ADER run gives the same picture
  ([Balsara (2009b)](/sources/balsara-2009-b.md), §5.2).
* *Tóth's first rotor.* $[-0.5, 0.5]^2$, angular velocity 20, taper width
  0.015, $\gamma = 1.4$, $\mathbf B = 5/\sqrt{4\pi}\,\hat x$, $400^2$, with
  no positivity treatment: symmetric, no spurious oscillations, and the
  order of the CT makes no visible difference. The output time is 0.15 in
  the text and 0.125 in the caption ([Seo & Ryu (2023)](/sources/seo-2023.md), §3.6).
* *Another normalization.* $[0, 1]^2$, $B_x = 2.5/\sqrt{4\pi}$, $p = 0.5$,
  taper 0.1–0.115, $\gamma = 5/3$, $400^2$, $t = 0.295$. Without the
  divergence projection the fifth-order Mach number shows instability and
  nonphysical structure ([Ding & Wu (2024)](/sources/ding-2024.md), Example 4.3).
* *Relativistic.* With a maximum Lorentz factor of 10 or 30, the usual $400^2$ mesh
  has no zone within 10% of the nominal Lorentz factor. The fraction levels
  off only from $1200^2$ (Lorentz factor 10) and $3500^2$ (30), a
  resolution caveat for this benchmark. Runs on $2500^2$ and $4700^2$ at
  third order ([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §6.1).

**Later uses (batch 7).**
* *GLM vs CT at second order* (Tóth's first rotor, $400^2$, $t = 0.15$):
  "extremely similar" Mach contours ([Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §4.6).
* *Entropy-stable GLM on block AMR* up to $512^2$: much smaller divergence
  artifacts than without cleaning, close to staggered CT; density and
  pressure minima that the CT run shows only at $2048^2$
  ([Derigs et al. (2018)](/sources/derigs-2018.md), §5.3).
* *Fourth-order ADER-WENO on $1000^2$* with a multidimensional Riemann
  solver, taper kept at six zones; and a relativistic rotor with Lorentz
  factor 30, which needs at least $3500^2$ and was run at $4700^2$
  ([Balsara (2017)](/sources/balsara-2017-d.md), §§IX.3, IX.6).

# Citations

1. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.4.
2. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.2.
3. [Balsara et al. (2009)](/sources/balsara-2009.md), §7.3.
4. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4.
5. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.2.1.
6. [Balsara (2004)](/sources/balsara-2004.md), §7.2.
7. [Balsara (2009b)](/sources/balsara-2009-b.md), §5.2 (author manuscript).
8. [Seo & Ryu (2023)](/sources/seo-2023.md), §3.6.
9. [Ding & Wu (2024)](/sources/ding-2024.md), Example 4.3 (arXiv v1).
10. [Balsara & Kim (2016)](/sources/balsara-2016-b.md), §6.1.
11. [Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §4.6.
12. [Derigs et al. (2018)](/sources/derigs-2018.md), §5.3.
13. [Balsara (2017)](/sources/balsara-2017-d.md), §§IX.3, IX.6.
