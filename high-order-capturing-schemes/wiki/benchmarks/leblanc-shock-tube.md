---
type: Benchmark
title: "Leblanc shock tube (extreme pressure and density ratio)"
description: "A shock tube with jumps of about a billion in pressure and a thousand in density; the shock position and the contact are hard to get right and the low-density side tests positivity."
status: established
aliases: [Le Blanc problem, LeBlanc shock tube]
tags: [benchmark, euler, positivity, strong-shocks, riemann-problem]
timestamp: 2026-10-08T00:00:00Z
---

# Leblanc shock tube

**Set-up.** Two versions appear.
* $\rho_L = 2$, $\rho_R = 0.001$, $u = 0$, $p_L = 10^9$, $p_R = 1$,
  $\gamma = 1.4$, $t = 10^{-4}$ ([Zhang & Shu (2010)](/sources/zhang-2010.md), §4.3).
* Domain $[0, 9]$, $\gamma = 5/3$, a jump of $10^6$ in internal energy
  and $10^3$ in density, right state $(\rho, u, p) = (10^{-3}, 0, 10^{-7})$,
  $t = 6$ ([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 10;
  [Hu, Adams & Shu (2013)](/sources/hu-2013.md), §3.3, $h = 9/800$).
The solution is a strong rarefaction, a contact and a shock.

**Results.**
* RKDG with the positivity limiter works with TVB constants
  $(M_1, M_2, M_3) = (10^{10}, 10, 10^{10})$ at $N = 800$ and
  $(10^{20}, 100, 10^{20})$ at $N = 6400$. The second field is the
  contact. Without the limiter such constants make the scheme unstable,
  and small constants give much worse results
  ([Zhang & Shu (2010)](/sources/zhang-2010.md), §4.3).
* WENO-CU6-M1 cannot compute it unlimited. With the cut-off flux limiter
  it runs, with small shock-position errors that decrease under
  refinement; WENO-CU6-M2, stabilized otherwise, still fails
  ([Hu, Adams & Shu (2013)](/sources/hu-2013.md), §3.3).
* Compact WENO stays positive but overshoots in internal energy, as do
  other published schemes; the solution improves with refinement
  ([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 10).

# Citations

1. [Zhang & Shu (2010)](/sources/zhang-2010.md), §4.3.
2. [Hu, Adams & Shu (2013)](/sources/hu-2013.md), §3.3.
3. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 10.
