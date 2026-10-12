---
type: Benchmark
title: "Sedov point-blast wave (low-density positivity test)"
description: "A point release of energy into a cold gas of near-zero pressure; the strong shock and the near-vacuum interior make it the standard low-density test for positivity-preserving schemes, in a planar 1D and a 2D corner version."
status: established
aliases: [Sedov blast, planar Sedov problem, point-blast wave]
tags: [benchmark, euler, positivity, low-density, blast-wave]
timestamp: 2026-10-09T00:00:00Z
---

# Sedov point-blast wave

**Set-up.** Density 1, zero velocity, and a tiny background energy
everywhere, except one cell that carries the point energy. Zhang & Shu
use total energy $10^{-12}$ with $E_0/h$, $E_0 = 3.2\times10^6$, in the
centre cell, $\gamma = 1.4$, $t = 0.001$
([Zhang & Shu (2010)](/sources/zhang-2010.md), §4.2;
[Zhang & Shu (2012)](/sources/zhang-2012.md), Example 5.2). Hu et al. and
Guo et al. use $(\rho, v_x, p) = (1, 0, 4\times10^{-13})$ with
$p = 2.56\times10^{8}$ in the centre cell on $[0, 4]$, $h = 0.005$,
$t = 0.001$ ([Hu, Adams & Shu (2013)](/sources/hu-2013.md), §3.1;
[Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 9). The 2D
version puts the energy in the lower-left corner cell of a square with
reflecting (symmetry) left and bottom boundaries; the exact solution is
self-similar (Sedov; Korobeinikov).

**Results.**
* Third-order RKDG with the [scaling limiter](/methods/positivity-preserving-scaling-limiter.md)
  and a TVB limiter captures the shock in 1D ($N = 800$) and 2D
  ($160^2$, $t = 1$). Without the TVB limiter it blows up even with the
  positivity limiter ([Zhang & Shu (2010)](/sources/zhang-2010.md), §4.2).
* FD WENO5 with the limiter ($h = 1/200$ in 1D; $h = 1.1/320$ in 2D)
  matches the DG results ([Zhang & Shu (2012)](/sources/zhang-2012.md), Examples 5.2–5.3).
* The [cut-off flux limiter](/methods/positivity-preserving-flux-limiter.md)
  with WENO5 gives a slightly sharper blast than Zhang–Shu, attributed
  to Zhang–Shu's single global signal speed in the Lax–Friedrichs flux
  ([Hu, Adams & Shu (2013)](/sources/hu-2013.md), §§3.1–3.2).
* The positivity-preserving [compact-reconstruction WENO](/methods/compact-reconstruction-weno.md)
  with HLLC is also slightly sharper than Zhang–Shu; minimum density and
  internal energy $4.7\times10^{-3}$ and $10^{-12}$
  ([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 9).

**Later uses (batch 7).**
* *DG with only the positivity limiter.* On $160^2$ over $[0, 1.1]^2$ with
  background pressure $10^{-5}$ and corner-cell energy $0.244816/h^2$, Euler
  and Navier–Stokes ($\mathrm{Re} = 200$) DG of degree 2–4 run to completion
  with no TVB or WENO limiter ([Zhang (2017)](/sources/zhang-2017.md), Example 6). *Compiler's
  note, flagged for human review:* this sits uneasily with the statement
  above that RKDG "blows up" without the TVB limiter even with the
  positivity limiter. The set-ups differ (background state, a step rule
  with $\max\{\cdot, 2h^2\}$ and restarts), so the two may not be
  comparable, and neither paper addresses the other.

## Contradictions

* **Does positivity-limited DG survive the Sedov problem without a TVB or
  WENO limiter?** *Open* (recorded at the batch-8 deep lint, from the
  compiler's note above). The earlier statement on this page says RKDG
  "blows up" without the TVB limiter even with the positivity limiter;
  [Zhang (2017)](/sources/zhang-2017.md) (Example 6) runs DG of degree 2–4
  to completion with the positivity limiter alone. The set-ups differ in
  the background state and the step rule, so the claims may not conflict.

# Citations

1. [Zhang & Shu (2010)](/sources/zhang-2010.md), §4.2.
2. [Zhang & Shu (2012)](/sources/zhang-2012.md), Examples 5.2–5.3.
3. [Hu, Adams & Shu (2013)](/sources/hu-2013.md), §§3.1–3.2.
4. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 9.
5. [Zhang (2017)](/sources/zhang-2017.md), Example 6.
