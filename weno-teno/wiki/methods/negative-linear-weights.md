---
type: Method
title: "Negative linear weights"
description: "When accuracy on the full stencil fixes the linear weights of a WENO combination, some can be negative or fail to exist, and the combination stops being convex; the page records where this happens (integration, Gauss points, unstructured and semi-Lagrangian stencils, spectral optimisation) and the remedies the sources use or cite."
status: established
aliases: [negative weights, negative ideal weights, negative optimal weights, non-existent linear weights, Shi–Hu–Shu technique, treating negative weights in WENO]
tags: [weno, reconstruction, teno, cweno, finite-volume]
timestamp: 2026-10-30T08:41:00Z
---

# Negative linear weights

A WENO approximation combines the candidate approximations $\hat f^{(k)}$ of the stencils $S_k$ with
linear weights $d_k$, $\sum_kd_k=1$, chosen so that the combination reaches the order of the full
stencil, and then replaces $d_k$ by nonlinear weights $\omega_k$
([WENO-JS reconstruction](/methods/weno-js-reconstruction.md)). [Shu (2009a)](/sources/shu-2009.md)
(§2.3.3) stresses that the $d_k$ "are determined uniquely by the accuracy requirement", so nothing
prevents some of them from being negative; the linear combination is then "no longer a convex
combination", and "if the usual WENO procedure is used without modification, oscillations and
instability may appear. This is because a sum of monotone approximations with negative linear
weights may become nonmonotone, even though the linear weights sum to one." Later sources add the
case in which no set of linear weights reaches the full-stencil order.

## Where they appear

- **WENO integration.** Shu (2009a, §2.3.4, Eqs. (2.18)–(2.22)) approximates
  $\int_{I_i}u\,dx$ from point values on the five-point stencil: each three-point stencil gives a
  fourth-order rule, e.g. $\Delta x\big(\tfrac1{24}u_{i-2}-\tfrac1{12}u_{i-1}+\tfrac{25}{24}u_i\big)$ on $S_0$,
  and the five-point rule
  $\Delta x\big(-\tfrac{17}{5760}u_{i-2}+\tfrac{77}{1440}u_{i-1}+\tfrac{863}{960}u_i+\tfrac{77}{1440}u_{i+1}-\tfrac{17}{5760}u_{i+2}\big)$
  is sixth order. The linear weights are
  $$d_0=-\frac{17}{240},\qquad d_1=\frac{137}{120},\qquad d_2=-\frac{17}{240},$$
  two of them negative, so "we would need to use the technique in [Shi, Hu & Shu] to handle the
  negative linear weights"; the procedure enters the residual-distribution finite-difference WENO
  schemes of Chou & Shu, as Shu cites them. The combination with these weights reproduces every
  coefficient of the five-point rule *(compiler check, not in the sources: exact rational
  arithmetic)*. The interpolation weights $(\tfrac1{16},\tfrac58,\tfrac5{16})$ and reconstruction weights
  $(\tfrac1{10},\tfrac35,\tfrac3{10})$ of the same review (§2.1–§2.2) are all positive.
- **Gauss points of multidimensional finite volumes.** [Ding & Wu (2024a)](/sources/ding-2024.md)
  (§2.2.2) note that with the three-point Gauss rule on each cell edge, "negative linear weights
  would appear in the WENO reconstruction for the midpoint", and that they "must be dealt with care",
  "otherwise numerical oscillations and instability may occur"; their fifth-order
  dimension-by-dimension scheme uses the four-point Gauss–Lobatto rule instead.
- **Unstructured meshes.** [Fu (2023)](/sources/fu-2023.md) (§3.9) states that for unstructured WENO
  "the optimal linear weights may become negative or even do not exist for the meshes with low
  quality", and [Ji, Liang & Fu (2022)](/sources/ji-2022.md) (§1) that "for some mesh topologies, the
  optimal linear weights may become negative inducing numerical instabilities or even do not exist".
  [Zhang & Zhu (2024)](/sources/zhang-2024-c.md) (§1) write in general that the linear weights of
  classical WENO "may be negative or non-existent", which makes the reconstruction "unstable or unable
  to improve the order of accuracy".
- **Semi-Lagrangian schemes.** Fu (2023, §3.2) cites conservative high-order semi-Lagrangian
  finite-difference WENO as a case where "the linear weights may not exist".
- **Spectrally optimised weights.** When linear weights are tuned for dispersion and dissipation
  rather than for maximum order, positivity becomes a design constraint: [Li, Chen & Ren (2022a)](/sources/li-2022.md)
  bound their dissipation parameter by $0\le c_{\mathrm{diss}}\le\min(c_{\mathrm{disp}},\tfrac19-\tfrac13c_{\mathrm{disp}})$,
  which "guarantees" non-negative $d_k$ of their four candidates and a convex combination (§2.3,
  §3.1, Table 1; [MDCD schemes](/methods/mdcd-scheme.md)).

## Remedies

**1. Modify the WENO procedure (Shi, Hu & Shu).** Shu (2009a, §2.3.3) points to "a procedure to
systematically modify the WENO procedure so that it is still stable and nonoscillatory in the
presence of negative weights" by Shi, Hu & Shu, used, as Shu cites them, for high-order central WENO
schemes, staggered finite-difference WENO, WENO schemes for nonconservative hyperbolic systems and
well-balanced WENO schemes for balance laws including the shallow-water equations. Zhang & Zhu (2024,
§1), Ji, Liang & Fu (2022, §1), Ding & Wu (2024a, §2.2.2) and
[Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) (§1.1) cite the same technique. No ingested source
prints its formulas.

**2. Lower the accuracy demanded of the combination.** Shu (2009a, §2.3.3): asking only fourth
instead of fifth order of the five-point combination frees one parameter, which can be used to make
all weights positive; asking only third order, the order of each candidate, allows any $d_k$ with
$\sum_kd_k=1$, e.g. equal weights or the largest weight on the most symmetric stencil. The cost is "a
lower order accuracy than the 'authentic' WENO schemes" on the same stencil; Shu cites central WENO
(Levy, Puppo & Russo) and unstructured finite-volume WENO schemes built this way. Fu (2023, §3.9) and
Ji, Liang & Fu (2022, §1, §2.3) describe the same remedy for unstructured meshes, and the latter's
unstructured WENO baseline uses candidates of the target order with free linear weights.

**3. Avoid the evaluation point.** Ding & Wu (2024a, §2.2.2) move the quadrature to Gauss–Lobatto
points, where the weights of their fifth-order scheme do not turn negative.

**4. Combine stencils of unequal size.** In [CWENO](/methods/cweno.md)-type reconstructions the
high-order polynomial on the large stencil is written as a combination with lower-degree polynomials,
so that "the choice of the linear weights can be arbitrary" (Ji, Liang & Fu 2022, §1). Zhang & Zhu
(2024, §1) list the central WENO of Levy et al., the unequal-sized WENO of Zhu & Qiu, which in their
words "completely" solves the difficulty, and WENO-AO among the answers, and their own ghost
multi-resolution scheme takes any positive linear weights. The same freedom is claimed for
[multi-resolution WENO](/methods/multi-resolution-weno.md) by
[Wang et al. (2021)](/sources/wang-2021.md) and for WENO-ZQ by
[Zheng et al. (2022)](/sources/zheng-2022.md); see the CWENO page for the evidence on which positive
weights keep the design order.

**5. Drop the convex combination (TENO).** Fu (2023) argues from Kang & Li's necessary and sufficient
condition for WENO-like linear combinations that the TENO combination "will always work" for the first
derivative on uniform Cartesian meshes and extends to nonuniform Cartesian meshes, because every
candidate contains the evaluation point (§2.5); that TENO-N, which applies a predefined optimal linear
scheme on the largest stencil not crossed by a discontinuity, avoids negative or non-existent linear
weights by construction (§3.2); and that its unstructured finite-volume TENO schemes (its ref. [210], up to sixth order) avoid
the drawback (§3.9; [targeted ENO](/methods/targeted-eno.md)).

## Qualifications

- The claims that negative weights cause oscillations and instability are stated, with citations,
  in every source above; none of them shows a computation with unmodified negative weights.
- Fan, Zhang & Qiu (2022, §1.1) add, citing three works, that avoiding negative linear weights makes
  WENO approximations of diffusion operators much more robust, but that such schemes still do not
  preserve positivity of density and pressure on demanding tests
  ([bound preservation](/properties/bound-preservation.md)).
- "Non-existent" weights (no combination reaches the full-stencil order) and negative weights are
  different failures; remedies 2, 4 and 5 address both, remedies 1 and 3 only negative ones.

# Citations

- [Shu (2009a)](/sources/shu-2009.md) — §2.1–§2.2 (linear weights), §2.3.3, §2.3.4 (Eqs. (2.18)–(2.22)).
- [Ding & Wu (2024a)](/sources/ding-2024.md) — §2.2.2 (arXiv v1).
- [Fu (2023)](/sources/fu-2023.md) — §2.5, §3.2, §3.9.
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §1, §2.3 (preprint).
- [Zhang & Zhu (2024)](/sources/zhang-2024-c.md) — §1.
- [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) — §1.1.
- [Li, Chen & Ren (2022a)](/sources/li-2022.md) — §2.3, §3.1, Table 1.
- [Wang et al. (2021)](/sources/wang-2021.md) — §3.1.1.
- [Zheng et al. (2022)](/sources/zheng-2022.md) — §1, §2.2.
