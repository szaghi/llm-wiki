---
type: Benchmark
title: "MHD rotor"
description: "A dense, rapidly spinning disc in a magnetized ambient medium launches torsional Alfvén waves; low-pressure regions make it a positivity test, especially in its very-low-β version."
status: established
aliases: [rotor problem, Balsara-Spicer rotor]
tags: [benchmark, mhd, 2d, positivity, low-beta]
timestamp: 2026-10-08T00:00:00Z
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

# Citations

1. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.4.
2. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.2.
3. [Balsara et al. (2009)](/sources/balsara-2009.md), §7.3.
4. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4.
5. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.2.1.
