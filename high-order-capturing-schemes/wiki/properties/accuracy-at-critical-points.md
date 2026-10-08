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
  *Compiler reading:* the expansion (3.9) shows the indicators agree to
  relative $O(h^2)$ at a first-order critical point, which meets the
  sufficient condition $O(h^{r-1})$ only for $r \le 3$; nothing in this
  batch tests points where higher derivatives also vanish. The claim is
  recorded as stated, pending later sources.
* **Monotonicity-preserving bounds**: designed to leave smooth extrema
  untouched; they do degrade order on the flat extrema of $\sin^4$
  ([monotonicity-preserving limiting](/methods/monotonicity-preserving-limiter.md),
  where the disagreement is recorded).

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

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), Remarks 1.2, 3.1.
2. [Shu & Osher (1988)](/sources/shu-1988.md), §III; [Shu & Osher (1989)](/sources/shu-1989.md), Remark 2.1.
3. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §3.4.
4. [Jiang & Shu (1996)](/sources/jiang-1996.md), §§2–3, Tables 3–4.
5. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §§2, 4.
6. [Shu (1998)](/sources/shu-1998.md), §§2.2.2, 2.3.2.
7. [Balsara & Shu (2000)](/sources/balsara-2000.md), §§I, IV.a.
