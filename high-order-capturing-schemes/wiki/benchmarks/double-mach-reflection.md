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

**Later uses (batch 2).** WENO-Z of orders 5, 9, 11 at up to
$1600 \times 400$ (higher order compensates resolution; $q \le 2$
unstable for WENO-M at $r > 3$ and WENO-Z at $r > 4$)
([Castro et al. (2011)](/sources/castro-2011.md)); WENO-CU6 at
$480 \times 120$ resolves vortical structure comparable to WENO5 at
twice the resolution ([Hu, Wang & Adams (2010)](/sources/hu-2010.md));
TENO6 at an effective $1024 \times 256$ comparable to ninth-order WENO-JS
at $1/960$, WENO-CU6-M fails ([Fu, Hu & Adams (2016)](/sources/fu-2016.md));
WENO-ZQ at $1600 \times 400$ ([Zhu & Qiu (2016)](/sources/zhu-2016.md));
WENO-AO(7,5,3) at $1600 \times 400$ resolves the Kelvin–Helmholtz
roll-up of the Mach-stem slip line ([Balsara, Garain & Shu (2016)](/sources/balsara-2016.md)).

**Later uses (batch 3).** FV-WENO ($r = 3$) with HLLC or MUSTA at
$480\times120$, $960\times240$ and $1920\times480$ gives the accepted
pattern on all meshes. HLLC rolls up the slip surfaces more than MUSTA,
a sign of less numerical diffusion. Since slip surfaces are physically
unstable, Euler computations have no converged limit, and their
roll-up measures only the scheme's effective viscosity
([Titarev & Toro (2004)](/sources/titarev-2004.md), §5.3). WENO-CU6-M1
with the cut-off positivity limiter at $240\times60$ predicts a strong
near-wall jet, as WENO-CU6-M2 does, where earlier computations at this
resolution smear it ([Hu, Adams & Shu (2013)](/sources/hu-2013.md), §3.4).
AFD-WENO at $1920\times480$, with a flattening algorithm, captures the
instabilities around the Mach stem
([Balsara et al. (2025)](/sources/balsara-2025.md), §VIII.a).

# Citations

1. [Jiang & Shu (1996)](/sources/jiang-1996.md), §8.3 Example 3.
2. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §4.3 Example 2.
3. [Balsara & Shu (2000)](/sources/balsara-2000.md), §VII.b.
4. [Castro, Costa & Don (2011)](/sources/castro-2011.md), §5.5.
5. [Hu, Wang & Adams (2010)](/sources/hu-2010.md), §3.7.
6. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §5.5.
7. [Zhu & Qiu (2016)](/sources/zhu-2016.md), Example 3.8.
8. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §5.5.
9. [Titarev & Toro (2004)](/sources/titarev-2004.md), §5.3.
10. [Hu, Adams & Shu (2013)](/sources/hu-2013.md), §3.4.
11. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §VIII.a.
