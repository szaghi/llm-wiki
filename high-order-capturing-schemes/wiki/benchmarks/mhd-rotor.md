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

# Citations

1. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.4.
2. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.2.
