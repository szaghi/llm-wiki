---
type: Benchmark
title: "Double Mach reflection"
description: "A Mach 10 shock hitting a 30° wedge (posed as a 60° shock on a flat wall): two Mach stems, a wall jet and slip-line roll-up; the standard 2D robustness and resolution test."
status: established
aliases: [double Mach reflection, DMR]
tags: [benchmark, euler, 2d, strong-shocks]
timestamp: 2026-10-08T00:00:00Z
---

# Double Mach reflection

**Set-up** (Woodward & Colella). Domain $[0, 4]\times[0, 1]$; a
right-moving Mach 10 shock at $x = 1/6$ on the bottom, inclined at 60° to
the $x$-axis; reflecting wall for $x > 1/6$, exact post-shock data to the
left of it; the top boundary follows the exact shock motion; undisturbed
gas $\rho = 1.4$, $p = 1$; $t = 0.2$; usually only $[0, 3]\times[0,1]$
shown ([Jiang & Shu (1996)](/sources/jiang-1996.md), §8.3 Example 3;
[Suresh & Huynh (1997)](/sources/suresh-1997.md);
[Balsara & Shu (2000)](/sources/balsara-2000.md), §VII.b).

**Results.**
* WENO-LF-4, WENO-LF-5 and ENO-LF-4 on $240\times 59$ and
  $480\times 119$ resolve both Mach stems; WENO with pressure–entropy
  weights fails because of the strong reflected waves
  ([Jiang & Shu (1996)](/sources/jiang-1996.md);
  [characteristic decomposition](/methods/characteristic-decomposition.md)).
* MP5 and WENO5 on $240\times 60$ capture both stems and the wall jet;
  CPU 5553 s versus 6843 s, against 4122 s for constant reconstruction
  ([Suresh & Huynh (1997)](/sources/suresh-1997.md), Fig. 4.7).
* $r = 5$ MPWENO with LLF fluxes and artificial compression on
  $480\times 120$ captures the slip-line roll-up seen in much finer runs.
  With RF fluxes a mild carbuncle appears where the normal shock meets
  the wall; using LLF near shocks removes it without loss of order
  ([Balsara & Shu (2000)](/sources/balsara-2000.md)).

# Citations

1. [Jiang & Shu (1996)](/sources/jiang-1996.md), §8.3 Example 3.
2. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §4.3 Example 2.
3. [Balsara & Shu (2000)](/sources/balsara-2000.md), §VII.b.
