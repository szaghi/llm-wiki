---
type: Property
title: "Accuracy at critical points"
description: "Whether a nonlinear capturing scheme keeps its design order where derivatives of the solution vanish (smooth extrema, flat extrema, sonic points); limiters, stencil switches and smoothness indicators can each cost order there."
status: established
aliases: [order at extrema, critical-point accuracy, degeneracy at extrema]
tags: [accuracy, weno, eno, limiter, critical-points]
timestamp: 2026-10-08T00:00:00Z
---

# Accuracy at critical points

A *critical point* is where $f'(u(x))$ or $u'$ (and possibly higher
derivatives) vanishes: smooth extrema, flat extrema such as those of
$\sin^4(\pi x)$ (first three derivatives zero), and sonic points
$f'(u) = 0$. Nonlinear stabilization is most likely to act there, since
data at an extremum look locally like data at a jump over a short
stencil ([Suresh & Huynh (1997)](/sources/suresh-1997.md), Fig. 2.1).

## Mechanisms and claims, by family

* **TVD limiters**: first order at extrema, always
  ([total variation diminishing](/properties/total-variation-diminishing.md)).
  PPM's extremum reset is of this kind ([PPM](/methods/ppm.md)).
* **ENO**: the leading error coefficient jumps where the stencil turns,
  which can happen at critical points; one order is lost in the maximum
  norm ([Harten et al. (1987)](/sources/harten-1987.md), Remarks 1.2, 3.1).
  Round-off-level stencil switching near zeros of derivatives can cost
  accuracy on $\sin^4$-type data (Rogerson & Meiburg, cited by
  [Jiang & Shu (1996)](/sources/jiang-1996.md),
  [Shu (1998)](/sources/shu-1998.md) and
  [Balsara & Shu (2000)](/sources/balsara-2000.md)); biasing toward a
  preferred stencil repairs it.
* **Flux building blocks**: E-fluxes that are only Lipschitz at sonic
  points cost accuracy there; Lax–Friedrichs-type or entropy-fixed Roe
  fluxes keep it ([Shu & Osher (1988)](/sources/shu-1988.md),
  [(1989)](/sources/shu-1989.md); [Liu, Osher & Chan (1994)](/sources/liu-1994.md)
  obtain order $r+1$ "except near sonic points").
* **WENO, undivided-difference indicator**: for $r = 3$, third order at
  critical points ([Jiang & Shu (1996)](/sources/jiang-1996.md), §2).
* **WENO-JS**: Jiang and Shu state that with their indicator the
  weights are also fifth-order accurate at critical points, from the
  expansion $\beta_k = \tfrac{13}{12}(f''h^2)^2(1 + O(h^2))$ when
  $f' = 0$ (eq. 3.9). [Shu (1998)](/sources/shu-1998.md) repeats that the
  accuracy condition holds "even near smooth extrema".
  [Balsara & Shu (2000)](/sources/balsara-2000.md) report that Jiang and
  Shu proved uniform third and fifth order for $r = 2, 3$ "at all points
  in the flow including at critical points such as smooth extrema and
  sonic points", and that a Mathematica analysis (omitted from the paper)
  extends uniform $(2r-1)$-th order to $r = 4$–$7$.
  This claim is refuted; see `Contradictions` below.
* **WENO-JS, corrected** ([Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md)):
  at $f' = 0$, $f''' \neq 0$ the indicators $\beta_0$, $\beta_2$ carry
  $O(h^5)$ terms $\mp\tfrac{13}{6}f''f'''h^5$ that differ between stencils,
  so $\beta_k = \tfrac{13}{12}(f''h^2)^2(1 + O(h))$, $\omega_k = d_k + O(h)$,
  and WENO5 is third order. The test functions $\sin$ and $\sin^4$ have
  $f' = f''' = 0$ together at their critical points, and ε $= 10^{-6}$
  dominates the indicators on fine grids, which is why the earlier
  tests missed it. For $r \le 6$ and $\varepsilon = 0$ the rate near a
  critical point of order $n_{\mathrm{cp}}$ is
  $$r_c = \max(2r - 2 - n_{\mathrm{cp}},\ n_{\mathrm{cp}}),$$
  two orders below design at $n_{\mathrm{cp}} = 1$ and down to $r - 1$
  (eq. 60). The fix: [mapped WENO](/methods/mapped-weno.md).
* **Later weights.** [WENO-Z](/methods/weno-z.md): fourth order at
  $n_{\mathrm{cp}} = 1$ with $q = 1$, fifth with $q = 2$; higher $q$ (up to
  $r - 1$) restores order at higher $n_{\mathrm{cp}}$, and ε $\sim h^2$
  acts as a flat-versus-rough switch ([Borges et al. (2008)](/sources/borges-2008.md);
  [Castro et al. (2011)](/sources/castro-2011.md)). WENO-CU6 degenerates
  like WENO5 and its authors decline the fix as too dissipative
  ([Hu, Wang & Adams (2010)](/sources/hu-2010.md)). WENO-ZQ keeps
  $\omega - d = O(h^4)$ at $f' = 0$ ([Zhu & Qiu (2016)](/sources/zhu-2016.md));
  TENO's condition is weaker and is stated to hold near critical points
  ([Fu, Hu & Adams (2016)](/sources/fu-2016.md)); a seventh-order
  $L^1$-indicator scheme keeps order at $n_{\mathrm{cp}} \le 2$
  ([Rathan & Naga Raju (2017)](/sources/rathan-2017.md)). Conditions are
  collected on [weight accuracy conditions](/results/weno-weight-accuracy-conditions.md).
* **Does it matter with shocks?** Every scheme converges at about first
  order with captured shocks (5/6 in $L_1$ for contacts on Sod), so the
  gain from critical-point accuracy there is "proportional rather than
  geometric" ([Henrick et al. (2005)](/sources/henrick-2005.md));
  [Borges et al. (2008)](/sources/borges-2008.md) attribute the sharper
  shock results of WENO-M and WENO-Z to larger weights on discontinuous
  stencils, not to critical-point order, and
  [Castro et al. (2011)](/sources/castro-2011.md) note that no
  meaningful shock example yet shows a substantial gain from critical
  points.
* **Monotonicity-preserving bounds**: designed to leave smooth extrema
  untouched; they do degrade order on the flat extrema of $\sin^4$
  ([monotonicity-preserving limiting](/methods/monotonicity-preserving-limiter.md),
  where the disagreement is recorded).
* **Extremum-preserving PPM limiting**: the Colella–Sekora limiter
  fires at smooth multi-D extrema, for example those of $x^3 - xy^2$
  along $x = \pm y/\sqrt3$, and costs fourth order in the max norm. A
  third-derivative test that spares small perturbations of a cubic
  restores it ([McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §2.4;
  [fourth-order finite volume](/methods/fourth-order-finite-volume.md)).
* **Adaptive meshes**: order can also be lost where nothing is
  singular. Ghost values at coarse–fine boundaries that do not match the
  fine Runge–Kutta stages trigger the limiter on smooth data, and the
  convergence rate falls to 1.39–1.59
  ([McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §4.3, Table 5;
  [high-order AMR](/methods/high-order-amr.md)).

## Numerical evidence in this corpus

On $u_t + u_x = 0$, $u_0 = \sin^4(\pi x)$:
* WENO5's observed order "settles down later" than for $\sin(\pi x)$,
  and the fourth-order Liu–Osher–Chan scheme is more accurate on the
  coarsest grid ([Jiang & Shu (1996)](/sources/jiang-1996.md), Table 4;
  [Shu (1998)](/sources/shu-1998.md), Table 2.3: $L_\infty$ orders 2.31,
  3.88, 4.80, 5.48 from 80 to 640 points);
* MP5 matches the unlimited quartic only at small CFL
  ([Suresh & Huynh (1997)](/sources/suresh-1997.md), Tables I–II);
* $r = 5$ WENO nearly reaches design order at about 80 points, while
  every MP-bounded variant converges markedly more slowly
  ([Balsara & Shu (2000)](/sources/balsara-2000.md), Table V).

**Batch 3.** Both WENO-Z-type devices recur in the new schemes:
compact-reconstruction WENO adopts WENO-Z weights "which can avoid
accuracy loss at critical points" ([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.2),
and WENO-AO interpolation uses $\tau$ built from indicator differences
for the same purpose, citing Borges et al.
([Balsara et al. (2025)](/sources/balsara-2025.md), §III). Neither paper
tests a critical-point problem directly.

**Batch 4.** The fourth-order central [energy-stable WENO](/methods/energy-stable-weno.md)
uses WENO-Z-form weights $d_k\left(1 + \tau/(\varepsilon + \beta_k)\right)$
with $\tau = (\Delta^3 f_{j-1})^2$. Its truncation analysis gives
design order for any number of vanishing derivatives if
$O(h^3) \le \varepsilon \le O(h^2)$. With only $\varepsilon > 0$ the
order can fall from four to two. The paper's implementation recipe,
however, sets $\varepsilon \propto h^4$, below that window, and no
critical-point test isolates the effect ([Fisher et al. (2011)](/sources/fisher-2011.md), §5.2 and eq. 75). Since
the upper end matches the $\varepsilon \sim h^2$ switch of WENO-Z, the
two families agree on the scaling's ceiling but not on its floor.

## Contradictions

**Is fifth-order WENO-JS fifth order at critical points?**
* [Jiang & Shu (1996)](/sources/jiang-1996.md), eq. 3.9: with their
  indicator the weights are "also 5th order accurate at critical points";
  repeated by [Shu (1998)](/sources/shu-1998.md); extended to
  $r = 4$–$7$ by [Balsara & Shu (2000)](/sources/balsara-2000.md).
* [Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md): the
  expansions (Table 1) differ from Jiang–Shu's eqs. 3.5, 3.7, 3.9; WENO5
  is third order where $f' = 0$, $f''' \neq 0$ (verified with
  $\varepsilon = 10^{-40}$ and 128-bit arithmetic), and all higher-order
  WENO schemes drop two orders at $n_{\mathrm{cp}} = 1$ (eq. 60); the
  published conditions are incomplete.
* **Closed (2026-10-08):** Henrick et al. explicitly supersede the
  earlier claim, identifying the error in the expansion and the reason
  the original tests could not detect it; confirmed independently by
  [Borges et al. (2008)](/sources/borges-2008.md) and
  [Castro et al. (2011)](/sources/castro-2011.md).

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), Remarks 1.2, 3.1.
2. [Shu & Osher (1988)](/sources/shu-1988.md), §III; [Shu & Osher (1989)](/sources/shu-1989.md), Remark 2.1.
3. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §3.4.
4. [Jiang & Shu (1996)](/sources/jiang-1996.md), §§2–3, Tables 3–4.
5. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §§2, 4.
6. [Shu (1998)](/sources/shu-1998.md), §§2.2.2, 2.3.2.
7. [Balsara & Shu (2000)](/sources/balsara-2000.md), §§I, IV.a.
8. [Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md), §§3–6 (Table 1 and eq. 60 read from the page images).
9. [Borges et al. (2008)](/sources/borges-2008.md), §4.
10. [Castro, Costa & Don (2011)](/sources/castro-2011.md), §4.
11. [Hu, Wang & Adams (2010)](/sources/hu-2010.md), §2.4.
12. [Zhu & Qiu (2016)](/sources/zhu-2016.md), §2.
13. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §3.1.5.
14. [Rathan & Naga Raju (2017)](/sources/rathan-2017.md), §3.
15. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.2.
16. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §III.
17. [Fisher et al. (2011)](/sources/fisher-2011.md), §5.2 and Appendix A (eqs. 42 and 75 read from the page images).
18. [McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §§2.4, 4.3.
