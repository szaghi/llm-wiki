---
type: Result
title: "A-stability barriers for decoupled and internally consistent multirate methods"
description: "Two impossibility theorems for multirate and GARK methods: no consistent decoupled GARK method is A-stable on the real 2D test problem, and an internally consistent multirate GARK method of order exactly one is scalar A-stable for only finitely many multirate ratios."
status: established
aliases: [decoupled multirate A-stability barrier, internally consistent multirate barrier]
tags: [multirate, stability, stiff, implicit]
timestamp: 2026-10-19T12:00:00Z
---

# A-stability barriers for decoupled and internally consistent multirate methods

[Roberts et al. (2021)](/sources/roberts-2021.md) prove two barriers on the
linear stability of [GARK](/methods/generalized-additive-runge-kutta.md) and
[multirate GARK](/methods/multirate-gark.md) methods for
$y'=f^{\{\mathrm f\}}(y)+f^{\{\mathrm s\}}(y)$. The first rules out unconditional
2D stability for every **decoupled** method. The second rules out scalar
A-stability, for all but finitely many multirate ratios $m$, for **internally
consistent** methods of order one. Together they explain why the internally
inconsistent multirate backward Euler methods and the coupled compound-fast
methods are the stable members of the family. The stability notions are defined
on [linear stability of multirate methods](/definitions/multirate-linear-stability.md).

## Barrier 1: decoupled methods (Roberts et al. 2021, Lemma 3.1, Thm. 3.4)

A GARK method is **decoupled** when its coupling blocks introduce no implicitness
between partitions.

**Lemma 3.1.** For a decoupled GARK method the coupling matrix
$\begin{bmatrix}0&A^{\{\mathrm f,\mathrm s\}}\\A^{\{\mathrm s,\mathrm f\}}&0\end{bmatrix}$
is nilpotent (graph argument).

**Theorem 3.4.** No decoupled GARK method consistent with the additive problem
(first-order accurate) is A-stable for the real 2D test problem.

*Proof idea.* On the skew test matrix $\begin{bmatrix}0&\eta\\-\eta&0\end{bmatrix}$,
with $w=H\eta$ (page-local), the 2D stability matrix depends only on the coupling
blocks (eq. 3.10). Nilpotency makes its determinant a polynomial,
$\det\mathbf R_2(w)=1+w^2+\mathcal O(w^4)$, which grows without bound, so
$\mathbf R_2$ cannot stay power bounded for all $w$.

Consequence: the decoupled multirate backward Euler and decoupled multirate
midpoint methods of the same paper, which are scalar L-stable (backward Euler) and
algebraically stable, are **not** unconditionally stable on the real 2D test; the
statements are consistent only because scalar and algebraic stability do not
imply 2D stability. Chinomona & Reynolds (2021, §4.1), citing the preprint of
Roberts et al. (2021) among others, likewise
report that solve-decoupled multirate-infinitesimal methods are easier to
implement but less stable than solve-coupled ones
([IMEX-MRI-GARK](/methods/imex-mri-gark.md)).

## Barrier 2: internally consistent first-order methods (Roberts et al. 2021, Thm. 5.1)

**Theorem 5.1.** An internally consistent MrGARK method of order exactly one is
scalar A-stable for only a finite number of multirate ratios $m$.

*Proof idea.* Expand along the imaginary axes with fixed direction,
$\lvert R_{\mathrm{mr}}(i\omega^{\{\mathrm f\}}\rho,i\omega^{\{\mathrm s\}}\rho)\rvert^2=1+\rho^2\kappa+\mathcal O(\rho^4)$
(page-local: direction $\omega^{\{\cdot\}}$, real amplitude $\rho$, and $\kappa$ a
quadratic form in the direction; the source writes $y$ and $p$), and show that the
Hessian of $\kappa$ has $\det=-4(r^{\{\mathrm f\}}-r^{\{\mathrm s\}})^2$, where
$r^{\{\mathrm f\}}=(b^{\{\mathrm f\}})^\top c^{\{\mathrm f\}}-\tfrac12$ and
$r^{\{\mathrm s\}}=(b^{\{\mathrm s\}})^\top c^{\{\mathrm s\}}-\tfrac12$ are the second-order
residuals of the two partitions' GARK weights and abscissae (page-local). Unless the residuals agree the form is a saddle, so some
direction leaves the unit disc. Remark 5.1: the proof needs only that the fast
error tends to zero as $m$ grows, so it applies to any multirate strategy, not
only MrGARK.

## Evidence that internal consistency costs stability

- The internally **inconsistent** coupled and decoupled multirate backward Euler
  methods are scalar L- and algebraically stable for all $m$ (stated without
  proof; Roberts et al. 2021, §5.1).
- The two internally consistent SDIRK2-based MrGARK methods, (5.5) and the
  Kværnø–Rentrop-type (5.6), share one scalar stability function, which is only
  L(69.2°) at $m=2$ and not even L(0°) by $m=6$ (§5.2, computed angles). The
  authors conclude that "it appears that internal consistency negatively affects
  the stability".
- The compound-fast methods escape both barriers: they are coupled in the
  compound step and use a damping condition on their coupling, and keep L($\alpha$)
  angles of about 81°–89° for every $m$ tested
  ([Multirate GARK](/methods/multirate-gark.md), Table 5.1).
- Forgoing internal consistency, however, raises the number of order conditions
  and limits the stage order to zero (§7); see
  [stage order](/definitions/stage-order.md).

## Qualifications

- Barrier 1 concerns the **real** 2D test problem; the scalar test cannot detect
  it. Barrier 2 is a scalar result for order exactly one; it says nothing about
  higher-order internally consistent methods, for which the paper reports only a
  failed search (the Kværnø–Rentrop order-3 attempt gave coefficients unbounded in
  $m$ and no A(0°)-stable solution; §5.3).
- Roberts et al. position these general GARK statements against method-specific
  multirate stability analyses (Kværnø, Savcenco, Hundsdorfer & Savcenco), and
  note that Theorem 5.1 could conflict with claims of unconditional stability for
  internally consistent multirate backward Euler schemes in earlier work,
  depending on the test problem used there; those works are not ingested.

# Citations

- [Roberts et al. (2021)](/sources/roberts-2021.md) — §3.3 (eq. 3.10, Lemma 3.1, Thm. 3.4), §5.1–5.3 (Thm. 5.1, Remark 5.1), §7.
- [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) — §4.1 (solve-decoupled versus solve-coupled stability, cited).
