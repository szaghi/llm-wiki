---
type: Source
title: "Biswas et al. (2025) — Explicit Runge–Kutta Methods that Alleviate Order Reduction"
description: "Extends weak stage order to explicit Runge–Kutta methods: proves the stage bound p+q_w ≤ s+1, characterizes stage-optimal schemes by Sylvester equations, shows that high weak stage order is incompatible with nonzero SSP coefficient, and gives optimized schemes up to (9,5,5) that remove order reduction on linear hyperbolic problems with time-dependent boundary data."
resource: "doi:10.1137/23m1606812"
source_kind: paper
authors: [Biswas A., Ketcheson D.I., Roberts S., Seibold B., Shirokoff D.]
year: 2025
venue: "SIAM J. Numer. Anal. 63:1398-1426"
local_file: "/home/stefano/papers/mosaic/ode-integration/2025_Crossref_SIAM_Journal_on_Numerical_Analysis_Biswas_Explicit_RungeKutta_Methods_that_Alleviate_Order_Reduction.pdf"
tags: [runge-kutta, explicit, order-reduction, order-conditions, ssp]
timestamp: 2026-10-19T12:00:00Z
---

# Summary

Explicit Runge–Kutta (ERK) methods applied to initial-boundary-value
problems with time-dependent boundary data suffer
[order reduction](/definitions/order-reduction.md). The observed rate drops
to about [stage order](/definitions/stage-order.md) + 1, and an explicit
method has $q\le1$. Earlier remedies modify the boundary conditions. Those
remedies need derivatives of the boundary data, introduce parameters, are
intrusive and have been studied only in 1D. The paper instead imposes the
[weak stage order](/definitions/weak-stage-order.md) conditions, developed
for implicit methods ([Biswas et al. 2023](/sources/biswas-2023.md),
[Biswas et al. 2024](/sources/biswas-2024.md)), on explicit tableaux.

The [barriers](/results/weak-stage-order-barriers.md) proved are
$p\le\deg P\le\dim\mathcal Y\le s-\dim\mathcal K_{q_{\mathrm w}}$,
$\dim\mathcal K_{q_{\mathrm w}}\ge q_{\mathrm w}-1$, and hence the stage
bound $p+q_{\mathrm w}\le s+1$. So any ERK with $p>1$ and $q_{\mathrm w}>1$
has a vanishing first-subdiagonal entry and a stability polynomial of
degree below $s$. Two Sylvester equations characterize the schemes with
$\dim\mathcal K_{q_{\mathrm w}}=q_{\mathrm w}-1$. For stage-optimal schemes
this characterization is an equivalence, and the stability polynomial is
the degree-$p$ Taylor polynomial of $e^z$. Non-negative coefficients are
incompatible with $q_{\mathrm w}\ge2$ when $p\ge2$, so such schemes have
[SSP](/methods/strong-stability-preserving-runge-kutta.md) coefficient
zero. Parallel-iterated methods of type $(p^2,p,p)$ reach arbitrarily
high weak stage order. For $y'=Ly+g(t)$ the scheme is equivalent to a
[GARK method](/methods/generalized-additive-runge-kutta.md) that applies
$L$ only $\dim\mathcal Y$ times.

Algorithm 1 parameterizes the stage-optimal schemes. The
[explicit Runge–Kutta methods with high weak stage order](/methods/explicit-runge-kutta-high-weak-stage-order.md)
(3,2,2), (4,3,2), (5,3,3), (6,4,3), (7,4,4), (8,5,4) and (9,5,5) are given
with exact rational coefficients, optimized for the principal error norm
of the [order conditions](/results/runge-kutta-order-conditions.md). The
tests use Clawpack/SharpClaw finite volumes: advection, inviscid Burgers,
1D shallow water, 2D acoustics and the Thacker flood wave. On linear
problems the new schemes reach full order. On nonlinear problems they
reach order 3, against order 2 for SSPRK3, RK4 and Dormand–Prince. The
paper also cites Rodas5P ([Rodas5P](/methods/rodas5p.md),
[Steinebach 2023](/sources/steinebach-2023.md)) as a Rosenbrock method
that avoids order reduction for DAEs up to order 5.

# Version read

arXiv:2310.02817v2 [math.NA], 5 October 2023, 23 pages (main text
pp. 1–20, references pp. 20–21, Appendix A pp. 21–23); page 1 carries the
footnote "Submitted to the editors DATE". This is not the SINUM version of
record (pp. 1398–1426, 29 pages). Title and authors match the published
version. Section, equation, theorem and table numbers are those of arXiv
v2. Refs. [6] ([Biswas et al. 2024](/sources/biswas-2024.md)) and [28]
are printed "In Press", reflecting the 2023 state.

# Key claims

Registry notation: $h$ step, $q_{\mathrm w}$ weak stage order (the
source's $q$), $\mathcal Y$ and $\mathcal K_m$ the source's $Y$ and $K_m$,
$\mathsf L$ the source's Sylvester unknown $L$, $n_c$ the number of
distinct abscissae, $P(z)$ the stability polynomial (the source's $R(z)$). Labels $(s,p,q_{\mathrm w})$.

1. Any explicit method with $c=A\mathbf 1$ has $\tau^{(1)}=0$, so
   $\dim\mathcal K_1=0$. Explicit Euler ($A=0$) has $q_{\mathrm w}=\infty$.
   Any explicit scheme with $p>1$ has $\tau^{(2)}\ne0$, so
   $\dim\mathcal K_2\ge1$ (§1.3, §2.1). **Proved** (elementary)
2. For an ERK of order $p$ and weak stage order $q_{\mathrm w}$:
   $p\le\deg P\le\dim\mathcal Y\le s-\dim\mathcal K_{q_{\mathrm w}}$
   (Lemma 2.1, Eq. (2.1)). Nearly all practical ERKs ($\deg P=s$) therefore
   have $q_{\mathrm w}=1$. Any method with $p>1$, $q_{\mathrm w}>1$ has
   $\deg P<s$, which requires a zero on the first subdiagonal of $A$.
   **Proved**
3. If $p>1$ then $q_{\mathrm w}<n_c$. If $q_{\mathrm w}<n_c$ then
   $\dim\mathcal K_{q_{\mathrm w}}\ge q_{\mathrm w}-1$ (Lemma 2.2, proof
   §6.1). **Proved**
4. Stage bound: an ERK with $p\ge2$ satisfies $p+q_{\mathrm w}\le s+1$
   (Thm 2.3, Eq. (2.2)). Equality implies
   $\dim\mathcal K_{q_{\mathrm w}}=q_{\mathrm w}-1$ and $\dim\mathcal Y=p$.
   The bound holds also when $p$ is only the linear (tall-tree) order
   (Remark 1). **Proved**
5. Necessary conditions for an irreducible ERK with weak stage order
   $q_{\mathrm w}$ and $\dim\mathcal K_{q_{\mathrm w}}=q_{\mathrm w}-1$
   (Thm 2.4): (a) $c_1,\dots,c_{q_{\mathrm w}+1}$ are distinct; (b) a unique
   $\mathsf L$ solves the Sylvester equations (2.4)–(2.5); (c) $b$ has the
   form (2.6); (d) $a_{q_{\mathrm w}+1,q_{\mathrm w}}=0$. Sufficient
   condition (Thm 2.5): any $(A,b)$ with a pair $(\mathsf L,\beta)$
   satisfying (a)–(d) has weak stage order at least $q_{\mathrm w}$.
   **Proved**
6. An $s$-stage scheme with $p\ge2$ has $q_{\mathrm w}=s+1-p$ iff
   Thm 2.4(a)–(d) hold with $q_{\mathrm w}=s-p+1$. Such schemes are
   irreducible and $P(z)=\sum_{j=0}^pz^j/j!$ (Thm 2.6). **Proved**
7. An ERK with $A\ge0$, $b\ge0$ has either $q_{\mathrm w}=1$, or $p\le1$
   and $q_{\mathrm w}=\infty$ (Thm 2.7). Hence every ERK with $p\ge2$ and
   $q_{\mathrm w}\ge2$ has SSP coefficient $\mathcal C=0$ (Cor. 2.8, via
   Kraaijevanger's Thm 4.2). The linear SSP coefficient, which depends only
   on $P$, can be positive. **Proved**
8. A method with $q_{\mathrm w}\ge p-1$ that satisfies the order-$p$
   quadrature conditions also satisfies all "palm tree" conditions
   $b^\top A^kc^j=1/((k+j+1)\cdots(j+1))$, $0\le j+k\le p-1$ (Eq. (3.2)). For
   $p\le3$ every classical order condition is a palm-tree condition, so the
   output of Algorithm 1 already has order $p$. **Stated** (no proof
   printed)
9. Table 3.1, minimum stages for given $(p,q_{\mathrm w})$, $p=2,\dots,5$:
   $q_{\mathrm w}=1$: 2, 3, 4, 6; $q_{\mathrm w}=2$: 3, 4, 5, 6;
   $q_{\mathrm w}=3$: 4, 5, 6, 7; $q_{\mathrm w}=4$: 5, 6, 7, 8;
   $q_{\mathrm w}=5$: 6, 7, 8, 9. The rows $q_{\mathrm w}\ge2$ attain
   $s=p+q_{\mathrm w}-1$; the only miss is $(p,q_{\mathrm w})=(5,1)$, where
   the classical barrier gives 6. **Shown** (by construction)
10. The (3,2,2) schemes form a two-parameter family, all with
    $P(z)=1+z+z^2/2$, linear SSP coefficient 1 and the same principal error,
    since $b^\top c^2=b^\top Ac=0$. The coefficient size is minimal at
    $c=(0,\frac12,1)$, $b=(-\frac12,2,-\frac12)$ (§3.1.2, Eq. (3.4)).
    **Derived**
11. All (4,3,2) and (5,3,3) schemes have $P(z)=1+z+z^2/2+z^3/6$ and linear SSP
    coefficient 1 (§3.1.3–3.1.4). **Derived**
12. Table 3.2 (principal error norm $\mathcal A^{(p+1)}$, coefficient size
    $\mathcal D$): (3,2,2) 2.357E-1, 2; SSPRK3 7.217E-2, 1; (4,3,2)
    5.893E-2, 1.003; ERK312 7.217E-2, 2; (5,3,3) 7.217E-2, 1.858; ERK313
    1.443E-1, 3.75; RK4 1.450E-2, 1; (6,4,3) 1.443E-2, 1.144; (7,4,4)
    1.667E-2, 6.187; DP5 3.991E-4, 11.60; (8,5,4) 1.217E-2, 25.33; (9,5,5)
    3.316E-2, 44.42. **Shown** (computed)
13. L-shaped schemes (nonzero entries only in the first column and last
    row of $A$, like ERK313) cannot have $p=q_{\mathrm w}=4$ or higher
    (Remark 2). **Stated**
14. For every $p\ge2$ there are ERKs of type $(p^2,p,p)$. They are
    parallel-iterated Runge–Kutta methods built on a $(p+1)$-stage basic
    method in V-transformed form (Thm 3.1). Parallel iteration does not in
    general raise weak stage order; the special basic method does. On an
    ideal parallel machine the cost is about that of a serial $p$-stage ERK
    (§3.2). **Proved** (constructive)
15. Applied to $y'=Ly+g(t)$, an ERK with $p\ge1$ and $d=\dim\mathcal Y$ is
    equivalent to a 2-additive GARK method with $d$ applications of $L$
    and $s$ evaluations of $g$ per step (Thm 4.1, Eq. (4.2)). **Proved**
16. With order $p$ and stage order $q$, PDE order reduction typically gives
    rate $\min(p,q+1)$. The paper observes the same with weak stage order
    for linear problems with time-dependent boundary data, which motivates
    $q_{\mathrm w}=p-1$ (§1.3). **Stated** + **Shown** (§5)
17. High-weak-stage-order ERKs "typically achieve an error of
    $\min(p,q_{\mathrm w}+1)$ in (linear) PDE problems or
    $\min(p,q_{\mathrm w})$ in ODE problems" (§3). **Stated**
18. Linear advection (5.1), CFL 0.9, $t=0.7$: the weak-stage-order-1
    methods reduce to order 2 in $y$ and 1 in $y_x$. All high-weak-stage-order
    methods reach full order in $y$. Those with $q_{\mathrm w}=p-1$ lose one
    order in $y_x$ through $O(h)$ boundary layers (Fig. 5.1). **Shown**
19. Inviscid Burgers (5.2), CFL 0.9, $t=0.8$: weak-stage-order-1 methods
    give order 2 in $y$ and 1 in $y_x$. All high-weak-stage-order methods
    give order at least 3 in $y$ and 2 in $y_x$ (Fig. 5.2). **Shown**
20. 1D shallow water (5.3), CFL 0.8, $t=0.5$: classical methods order 2,
    high-weak-stage-order methods order 3, with much smaller errors
    (Fig. 5.3). **Shown**
21. 2D linear acoustics (5.4), CFL 0.45, $t=1$: classical methods reduce.
    High-weak-stage-order methods reach full order with much smaller errors
    (Fig. 5.4). **Shown**
22. 2D Thacker parabolic flood wave (5.5), $t=0.5$: high-weak-stage-order
    methods order 3 or slightly better, classical order 2, with much smaller
    errors (Fig. 5.5). **Shown**
23. Comparison of $q_{\mathrm w}=3$ methods (§5.7, Fig. 5.6): (5,3,3),
    Skvortsov's ERK313 and the parallel-iterated (9,3,3) all reach order 3
    on advection and Burgers. Errors are nearly identical on advection, and
    (5,3,3) has the smallest errors on Burgers. **Shown**
24. Requiring weak stage order $q_{\mathrm w}$ sets the highest
    $q_{\mathrm w}-1$ coefficients of the stability polynomial to zero, dual
    to order $p$ fixing the first $p+1$ (§7). **Derived**
25. Weak stage order guarantees the absence of order reduction only for
    linear problems. On nonlinear problems $q_{\mathrm w}\ge3$ gives order 3
    against order 2 for $q_{\mathrm w}=1$ (§7). **Shown** (numerically only)

# Printed slips

- Algorithm 1, Outputs: "$(A_{32},A_{21},A_{32},b)$" — $A_{32}$ is listed
  twice; the third item should be $A_{31}$.
- Lemma 2.2 proof (§6.1): "implies $\dim K_q\ge m-1$" should read $q-1$.
- Conclusions (§7): the stage bound is attributed to "Theorem 2.4" (it is
  Theorem 2.3). The Sylvester characterization is placed in "Theorems
  2.5–2.6", but the Sylvester equations are in Theorem 2.4.
- Table 3.2 caption refers to "B.x" sections; the appendix sections are
  A.1–A.4.
- §5.5: "$(u(x,y,t),v(x,y,y))$" for $v(x,y,t)$.
- Typos: "principle error" (§3.1.4), "the the conditions" (§3.1), "achieve
  3rd-order convergence both problems" (§5.7), "substituing", "involing"
  (§6.2), "as show herein" (§1.3).
- Reference list: ref. [9] title "Numberical Methods…"; ref. [15] prints
  Hundsdorfer twice among the authors; refs. [13] and [14] are the same
  book (Hairer & Wanner 1996); ref. [28] is printed both "In Press (2023)"
  and as arXiv:1712.00897.

# Notation map

| Biswas et al. (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$ | $h$ | |
| $A$, $b$, $c$, $e$ | $A$, $b$, $c$, $\mathbf 1$ | $c=A\mathbf 1$ assumed |
| $\tau^{(k)}$ | $\tau^{(k)}$ | agrees |
| **$q$** | $q_{\mathrm w}$ | **collision: weak stage order; §1.3 also uses $q$ once for stage order** |
| $R(z)=1+\sum_j z^jb^\top A^{j-1}e$ | $P(z)$ for explicit methods | stability polynomial |
| **$Y$** | $\mathcal Y$ | **collision with stage values $Y_i$** |
| **$K_m$** | $\mathcal K_m$ | **collision with $K$ (correction iterations)** |
| **$L$ (§2, Sylvester unknown)** | $\mathsf L$ | **collision with the linear operator $L$; the source itself reuses $L$ for the operator in §4** |
| $L$ (§4), $g(t)$ | $L$, $g(t)$ | linear operator and forcing of $y'=Ly+g(t)$ |
| $\beta$ | — | free weight parameters of (2.6); collides with Shu–Osher $\beta_{ij}$ only nominally |
| $\mathcal A^{(p+1)}$ | — | principal error norm, built from $\sigma(\tau)$, $\gamma(\tau)$, $\Phi(\tau)$ (agree) |
| $\mathcal D$ | — | $\max\{\lvert a_{ij}\rvert,\lvert b_i\rvert,\lvert c_i\rvert\}$ |
| SSP coefficient | $\mathcal C$ | agrees |
| **$\hat A$, $\hat b$ (§4)** | $A^{\{q,r\}}$, $b^{\{q\}}$ | **collision with embedded $\hat b$**; GARK coefficients |
| $\hat A$, $\hat s$ (§6) | — | leading block of $A$; a second meaning of $\hat A$ inside the source |
| $\tilde A$, $\tilde b$, $\tilde c$, $\tilde V$, $\tilde S$ | — | basic method of the parallel-iterated construction |
| $Y_i$ (§4) | $Y_i$ | stage values; agrees |

# Reference list

The paper prints 38 references in numbered style, alphabetical. All are
merged complete into the [bibliography](/bibliography.md) with `citedby`
biswas-2025. Refs. [5] and [26] are software repositories. Refs. [6] and
[28] are "In Press" (2023), and ref. [27] is an arXiv preprint; all are
their own entries. The printed duplicate [13]=[14] (Hairer & Wanner 1996)
is folded into one entry (`hairer-1996`), so the list gives 37 entries. The doubled author in
ref. [15] is kept as printed. DOIs are printed for [8], [11], [18], [29]
and [37]. The three Biswas items take the suffixes `biswas-2023`,
`biswas-2023-b`, `biswas-2023-c` in printed order.

# Pages created or updated

Chunk 1 (2026-10-19); updated in later chunks. This source is cited on:

* [Boundary conditions for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md)
* [Dormand–Prince 5(4) pair](/methods/dormand-prince-5-4.md)
* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Explicit Runge–Kutta methods with high weak stage order](/methods/explicit-runge-kutta-high-weak-stage-order.md)
* [Generalized additive Runge–Kutta (GARK) methods and internal consistency](/methods/generalized-additive-runge-kutta.md)
* [Linear advection equation](/benchmarks/linear-advection-equation.md)
* [Optimal stability polynomials for explicit Runge–Kutta methods](/methods/optimal-stability-polynomial.md)
* [Order reduction](/definitions/order-reduction.md)
* [Rodas5P](/methods/rodas5p.md)
* [Rosenbrock–Wanner (ROW) and W-methods](/methods/rosenbrock-wanner-method.md)
* [Runge–Kutta method](/definitions/runge-kutta-method.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Stage order](/definitions/stage-order.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
* [Weak stage order](/definitions/weak-stage-order.md)
* [Weak-stage-order barriers](/results/weak-stage-order-barriers.md)
