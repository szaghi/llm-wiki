---
type: Source
title: "Dallerit & Tokman (2025) — Stiffness resilient exponential integrators and φ-order conditions"
description: "Derives a φ-series expansion of the exact solution and the φ-order conditions, solves them in closed form for any order, proves that the resulting methods cancel every error term J^k F(τ) of low-order trees, and builds stiffness-resilient exponential Runge–Kutta, multistep and multivalue methods of orders 3–6."
resource: "doi:10.1007/s10543-025-01062-z"
source_kind: paper
authors: [Dallerit V., Tokman M.]
year: 2025
venue: "BIT Numer. Math. 65:23"
local_file: "/home/stefano/papers/mosaic/ode-integration/2025_Crossref_BIT_Numerical_Mathematics_Dallerit_Stiffness_resilient_exponential_integrators_and_varphi_-orde.pdf"
tags: [exponential, stiff, order-conditions, b-series, order-reduction]
timestamp: 2026-10-20T05:00:00Z
---

# Summary

[Exponential integrators](/methods/exponential-integrators.md) for a stiff
autonomous system $y'=f(y)$ are usually built from one of two sets of
conditions. **Classical** conditions match Taylor or
[B-series](/definitions/b-series.md) with all $\phi_k$ expanded. They leave
terms $J^kF(\tau)$ in the leading error and cause
[order reduction](/definitions/order-reduction.md) when the Jacobian is
unbounded. **Stiff** order conditions write the error with bounded
operators $\phi_k(hJ)$. They exclude order reduction under analytic-semigroup
assumptions but are hard to solve: exponential Runge–Kutta methods of this
kind exist only up to order five. The paper proposes an intermediate set,
the **φ-order conditions**
([stiff order conditions and φ-order conditions](/results/exponential-runge-kutta-stiff-order-conditions.md)).
They come from a new φ-series of the exact solution (Thm 5),
$y(t_n+h)=y_n+\phi_1(hJ_n)hf(y_n)+\sum_{k\ge3}\phi_k(hJ_n)G_k$, where
$G_k$ is a B-series supported on trees of order $k$ with at least two
branches at the root. A method $y_{n+1}=y_n+\phi_1(hJ_n)hf(y_n)+\sum_{k=3}^p\phi_k(hJ_n)v_k$
has φ-order $p$ if each $v_k$ matches $G_k$ on all trees of order
$\le p$.

With $v_k=\sum_j\kappa_{k,j}hr_n(Y_j)$, where $r_n$ is the nonlinear remainder
of $f$ about $y_n$, the conditions are solved in closed form (Thm 6). The
$Y_j$ must be classical order-$(p-2)$ approximations at distinct nonzero
nodes $c_j$, and $\kappa_{k,j}$ follows from a Vandermonde inverse. Such
methods also cancel every error term $J^kF(\tau)$ with $\lvert\tau\rvert\le p$
(Thm 7, "stiffness resilience"). They are equivalent to polynomial
interpolation of the remainder (Thm 8). They have embedded methods by
truncation (Thm 9; [embedded pairs](/methods/embedded-runge-kutta-pair.md)),
a full-order [dense output](/methods/dense-output.md) (Thm 10), and need one
Krylov projection per step
([evaluating φ-functions](/methods/phi-function-evaluation.md)). Nodes in
$(0,1]$ give exponential Runge–Kutta methods SREXP_RK3–6. Negative integer
nodes reproduce the exponential Adams methods of Hochbruck–Ostermann
([linear multistep methods](/methods/linear-multistep-method.md)), and nodes
in $(-1,0)$ give multivalue methods. Tests on two semilinear parabolic
problems and a 2D advection–diffusion–reaction PDE show the design orders
without order reduction. At order 5, at least two stiffness-resilient schemes
beat the exponential Rosenbrock EXPRB_5s4 in CPU time against error. The
paper's "stiffly accurate" means "satisfies the stiff order conditions",
not the Runge–Kutta [stiff accuracy](/properties/stiff-accuracy.md) property.

# Version read

Version of record: Springer typeset PDF, open access (CC BY 4.0, U.S.
Government work), 34 pages, BIT Numer. Math. 65, article 23. Received 28
April 2024, accepted 4 March 2025, published online 6 May 2025;
communicated by M. Thalhammer. The DOI is printed on page 1. The printed
title carries the Greek letter φ; the PDF's embedded title drops it.

# Key claims

Registry notation: $J_n=f'(y_n)$ (source $J$), $\phi_k$ (source $\varphi_k$,
same normalisation), $r_n(y)=f(y)-f(y_n)-J_n(y-y_n)$ the page-local
remainder (source $r$), $Y_j=B(z_j,y_n)$ the stages (source $Z_j$), trees
$\tau$ (source $t$), $a(\tau)$ the B-series coefficients of the method
(source $\phi(t)$). Page-local: $e_\theta(\tau)=\theta^{\lvert\tau\rvert}/\gamma(\tau)$
the exact-solution coefficients; $G_k=B(g_k,y_n)$ the φ-series
vectors (source $\Gamma_k$, $\lambda_k$); $v_k=B(\hat g_k,y_n)$ their
approximations (source $\nu_k$); $T_S$ the trees with one root branch and
$T_M$ the rest ($\bullet$ and trees with $\ge2$ root branches); $[\tau]_k$ the
$k$-fold rooting of $\tau$; $E_k$ the elementary symmetric
polynomials (source $e_k$).

1. The exact solution satisfies
   $y(t_n+h)=y_n+\phi_1(hJ_n)hf(y_n)+\sum_{k=3}^\infty\phi_k(hJ_n)G_k$,
   with $g_k(\tau)=k!/\gamma(\tau)$ for $\tau\in T_M$, $\lvert\tau\rvert=k$, and 0
   otherwise; there is no $k=2$ term (Thm 5, Eqs. 11–12). **Proved**
2. For any $Y=B(z,y_n)$ with $z(\varnothing)=1$, the B-series of $hr_n(Y)$ is
   zero on $\varnothing$, $\bullet$ and every tree in $T_S$; on
   $\tau=[\tau_1,\dots,\tau_m]\in T_M\setminus\{\bullet\}$ its coefficient is
   $\prod_iz(\tau_i)$ (Thm 4, Eq. 10). **Proved**
3. φ-order conditions are stronger than classical order conditions and, in
   the authors' words, weaker or easier than stiff order conditions; the
   resulting methods have no powers of $J_n$ in the leading error term
   (§3, p. 8). **Stated** (the "stronger than classical" half is made precise
   by Thm 7)
4. Under the ansatz (14) the φ-order-$p$ conditions reduce to
   $\hat g_k(\tau)=k!/\gamma(\tau)$ if $k=\lvert\tau\rvert$ and 0 otherwise, for
   $\tau\in T_M$, $\lvert\tau\rvert\le p$, $3\le k\le p$ (Eq. 16). φ-order 4
   leaves six conditions (p. 11). **Derived**
5. The $v_k$ must be linearly independent, so at least $p-2$ remainder
   evaluations $hr_n(Y_j)$ are needed. With exactly $p-2$ the $\kappa_{k,j}$
   are unique; with more they are not (§3, p. 11). **Derived**
6. **Theorem 6.** A method of form (18) with $p-2$ distinct nonzero nodes has
   φ-order $p$ iff each $Y_j$ is a classical order-$(p-2)$ approximation of
   $y(t_n+c_jh)$ and
   $\kappa_{k,j}=(-1)^{p-k}(k-1)!\,E_{p-k}(\{c_1,\dots,c_{p-2}\}\setminus\{c_j\})\big/\big(c_j^2\prod_{l\ne j}(c_j-c_l)\big)$
   (Eq. 19; proof pp. 13–17). **Proved**. The reader checked Eq. 19
   numerically against Eqs. 40–41 and Tables 1–3.
7. **Theorem 7.** A method of form (17) has φ-order $p$ iff
   $a(\tau)=e_1(\tau)$ and $a([\tau]_k)=e_1([\tau]_k)$ for all $k>1$ and all
   $\lvert\tau\rvert\le p$. It matches the exact B-series on every tree of
   order $\le p$ and on every tree $[\tau]_k$ (elementary differential
   $J_n^kF(\tau)$) with $\lvert\tau\rvert\le p$, whatever its order (pp. 17–19).
   **Proved**
8. Stiffness amplifies $J_n^kF(\tau)$, so removing these terms from the error
   "can alleviate" loss of accuracy and of the convergence region on stiff
   problems. The authors call this **stiffness resilience** (§5.1, p. 19).
   **Stated** (no bound for unbounded $J_n$ is proved)
9. A φ-order-$p$ method (17) equals replacing
   $R(\theta)=hr_n(y(t_n+\theta h))$ in the variation-of-constants formula by
   the unique polynomial $P$ of degree $p-1$ with $P(0)=P'(0)=0$ and
   $P(c_i)=hr_n(Y_i)=R(c_i)+O(h^p)$ (Thm 8). **Proved**
10. The whole update $\phi_1(hJ_n)hf(y_n)+\sum_k\phi_k(hJ_n)v_k$ is one linear
    combination and needs a single Krylov projection (KIOPS) (§5.3).
    **Stated**
11. Truncating the sum at $k=q<p$ gives an embedded method of φ-order $q$.
    Adaptive error control then needs two KIOPS calls, and the
    $\kappa_{k,j}$ are cheap enough to recompute every step (Thm 9, §5.4).
    **Proved** (Thm 9); **Stated** (cost)
12. Dense output:
    $y(t_n+\theta h)=y_n+\sum_{k\ge1}\phi_k(\theta hJ_n)\theta^kG_k$
    (Thm 10, Eq. 38), so
    $y_n+\phi_1(\theta hJ_n)\theta hf(y_n)+\sum_{k=3}^p\phi_k(\theta hJ_n)\theta^kv_k$
    has φ-order $p$ at $t_n+\theta h$ (§5.5). **Proved**
13. Order-3 exponential Runge–Kutta: $\kappa_{3,1}=2/c_1^2$ with $Y_1$ from
    exponential Euler. Every $0<c_1\le1$ gives φ-order 3, and $c_1=3/4$ raises
    the classical order to 4 ($\kappa_{3,1}=32/9$) (§6.1, p. 23). **Stated**
    (observed in Fig. 3)
14. The nodes $c_1=1/2$, $c_2=2/3$ and $c_1=1/8$, $c_2=1/9$ in the φ-order-4
    family re-derive the methods of Rainwater & Tokman (§6.1). **Stated**
15. Order-4 exponential Runge–Kutta with nodes $c_{1,2}=(10\mp\sqrt{10})/15$,
    the roots of $6-20x+15x^2$, and closed-form $\kappa$ (Eq. 40) (§6.1).
    **Derived**
16. For $p>4$ the stages cannot come from exponential Euler. The dense output
    of a φ-order-$(p-2)$ method supplies them. Order-6 example with nodes
    $(10-\sqrt{10})/15$, $(10+\sqrt{10})/15$, $1/4$, $1/2$, $3/4$, $1$ (Eq. 41)
    (§6.1, p. 24). **Derived**
17. Nodes at the roots of the Jacobi polynomial $P^{(0,2)}_{p-2}(2x-1)$, $p$
    the φ-order, cancel more error terms and "in some cases" raise the
    classical order. Stiffness-resilient methods "of order up to 8" were built
    this way; the explanation is left to future work (§6.1, p. 24).
    **Stated** (observed for RK3 and RK5, Fig. 3)
18. Negative integer nodes $c_j=-j$ give exponential multistep methods
    identical to the exponential Adams methods of Hochbruck & Ostermann. At
    order 3: $y_{n+1}=y_n+\phi_1(hJ_n)hf(y_n)+\phi_3(hJ_n)\,2hr_n(y_{n-1})$
    (§6.2, Table 2). **Stated** (identity asserted, not shown)
19. Multistep variants need $p-2$ past values, which makes starting hard,
    and lose accuracy with distant nodes. Nodes $c_j=-j/(p-2)\in[-1,0)$
    (multivalue methods) avoid this; the past values come "for little to no
    extra cost" from the adaptive Krylov dense output (§6.3, Table 3).
    **Stated**
20. All SREXP_MS, SREXP_MV and SREXP_RK methods of orders 3–6 converge at
    their design order or better on the three test problems, with no order
    reduction (Figs. 1–3). **Shown**
21. SREXP_RK3 and SREXP_RK5 (Jacobi nodes) converge at orders 4 and 6
    (Fig. 3, p. 29). **Shown**
22. Higher order pays on the semilinear problems, where $f$ and $J_n$ are
    cheap, while lower-order methods "can perform better for certain
    parameter regimes" on the advection–diffusion PDE (§7, Figs. 1–3).
    **Shown**
23. At order 5 all stiffness-resilient methods (SREXP_RK5, SREXP_MS5,
    SREXP_MV5) show order 5, while the stiffly accurate exponential
    Rosenbrock EXPRB_5s4 of Luan & Ostermann shows "a slight order reduction"
    on the advection–diffusion PDE (Fig. 4e). At least two stiffness-resilient
    schemes beat EXPRB_5s4 in CPU time against error on all test problems
    (Fig. 4b,d,f). **Shown** (no hardware or implementation details)
24. The framework re-derives known methods (Hochbruck–Ostermann, Rainwater–
    Tokman) as well as new ones (§8). **Stated**

# Printed slips

- p. 12, worked $p=4$ example: "$w_1([[\bullet],\bullet])=c_1/2$,
  $w_2(\dots)=c_2/2$". By Thm 4 and Eq. 34 the value is $c_j^3/2$, the only
  one consistent with Eqs. 21–22.
- Eqs. 19 and 33: the product is printed $\prod_{l=1,\,l\ne i}^L(c_j-c_l)$;
  the index should be $l\ne j$.
- Proof of Thm 6, p. 14: the exponent is printed $(-1)^{L-k}$ against
  $(-1)^{p-k}$ in Eqs. 19/33 (same parity, harmless); "$\delta_{k-2.m}$".
- Eq. 36: the product $\prod_{i=0}^m$ should start at $i=1$.
- Eq. 31: "$x_j=z_j(\tau)$" where the equation uses $z_j(t)$.
- Proof of Thm 7: "for all $1\le k\le q$" with $q$ undefined (should be
  $p$); "$\nu_2(t)=0\ \forall T\in T^\#$".
- Thm 7 states "$\forall k>1$", while the proof and the discussion use
  $k\ge1$, which the term $J_nF(\tau)$ needs.
- §5.3: the sum is printed $\sum_{k=3}^q$ (should be $p$). Thm 9: "has order
  $q$" means φ-order $q$.
- §6.2: "we can choose $c_j=-j$ for $i\in\{1,\dots,p-2\}$".
- Table 1: nodes are truncated, not rounded, to 4 decimals (e.g. 0.8774 for
  0.877485, 0.2949 for 0.294998); the $\kappa$ values match Eq. 19 at the
  exact roots.
- §7, pp. 28–29: the text names "SRERK_6", "SRERK_3", "SRERK_5" where Table 1
  and the figures use SREXP_RK*, and cites "Fig. 1c" for an RK method,
  whereas Fig. 1 shows multistep methods.
- Fig. 1(d) caption repeats "Semilinear parabolic problem 1" for problem 2.
- Typos: "Figs. 1, 2, 3 and 4 p are designed", "findinings", "perform have
  the accuracy", "a method as ϕ-order 3", "controler".
- Reference list: ref. [14] "Constructing new timet integrators"; ref. [20]
  pages "22–12219"; ref. [3] (Hochbruck & Ostermann, SIAM J. Numer. Anal. 43)
  printed with year 2006 (published 2005).

# Notation map

| Dallerit & Tokman (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $y'=f(y)$, $h$, $t_n$, $y_n$ | $y'=f(y)$, $h$, $t_n$, $y_n$ | agree; autonomous only |
| $J$ | $J_n$ | full Jacobian at $y_n$, recomputed each step |
| $\varphi_k$ | $\phi_k$ | same normalisation |
| $r(y)$ | $r_n(y)$ | page-local remainder about $y_n$ |
| $R(\theta)$ | — | $hr_n(y(t_n+\theta h))$; **collides with the stability function $R(z)$** |
| $T$, $T^\#$, $t$, $\emptyset$ | $T$, $T\cup\{\varnothing\}$, $\tau$, $\varnothing$ | trees |
| $T_S$, $T_M$, $[\tau]_k$ | $T_S$, $T_M$, $[\tau]_k$ | the paper's tree partition and repeated rooting; $F([\tau]_k)=J_n^kF(\tau)$ (Lemma 1) |
| $\lvert t\rvert$, $\gamma(t)$, $\sigma(t)$, $F(t)$, $B(a,y_n)$ | $\lvert\tau\rvert$, $\gamma(\tau)$, $\sigma(\tau)$, $F(\tau)$, $B(a,y_n)$ | agree (Butcher normalisation $h^{\lvert\tau\rvert}/\sigma(\tau)$) |
| **$\phi(t)$** | $a(\tau)$ | **collision with the φ-functions $\phi_k$**; method coefficients |
| $e_\theta$, $e$ | $e_\theta$, $e_1$ | exact-solution coefficients; **$e$ also names the elementary symmetric polynomials in the source** |
| **$e_k(S)$** | $E_k(S)$ | elementary symmetric polynomial |
| **$\Gamma_k$**, **$\lambda_k$** | $G_k$, $g_k$ | **collisions with the MRI coupling matrices $\Gamma^{(k)}$ and the eigenvalue** |
| $v_k$, **$\nu_k$** | $v_k$, $\hat g_k$ | **$\nu$ collides with the Courant number** |
| $Z_j=B(z_j,y_n)$, $c_j=z_j(\bullet)$ | $Y_j$, $c_j$ | stage values; nodes may be negative |
| $W_j=hr(Z_j)=B(w_j,y_n)$ | $hr_n(Y_j)$ | remainder evaluations |
| **$\alpha_{k,j}$** | $\kappa_{k,j}$ | page-local, as on the [stiff order conditions](/results/exponential-runge-kutta-stiff-order-conditions.md) page; coefficient of $hr_n(Y_j)$ in $v_k$; **$\alpha$ collides with the Shu–Osher $\alpha_{ij}$** |
| **$L$** | $p-2$ | **collision with the linear operator**; number of nodes |
| $A$, $B$, $C$, $V$ | — | proof-local matrices; **$A$ collides with the Butcher matrix** |
| order $p$ | $p$ | classical order |
| ϕ-order $p$ | — | Def. 4; strictly stronger than classical order (Thm 7), not Hochbruck–Ostermann stiff order |
| "stiffly accurate" | — | **satisfies the stiff order conditions; not [stiff accuracy](/properties/stiff-accuracy.md)** |

# Reference list

The paper prints 24 references in numbered style. All are merged complete
into the [bibliography](/bibliography.md) with `citedby` dallerit-2025, and
all parse. Ref. [20] has a garbled page field ("22–12219") and ref. [14] the
typo "timet"; both are kept as printed. Ref. [3] (Hochbruck & Ostermann, SIAM J. Numer.
Anal. 43) is printed with the year 2006 and merged into `hochbruck-2005`,
the year of its published issue; ref. [12] (Butcher, IMA J. Numer. Anal. 30),
printed 2010, is likewise `butcher-2009-b` (same DOI). Luan & Ostermann 2014
(EXPRB_5s4) is `luan-2014-b`.

# Pages created or updated

Chunk 4 (2026-10-20). This source is cited on:

* [B-series, composition and substitution laws](/definitions/b-series.md)
* [Dense output](/methods/dense-output.md)
* [Evaluating φ-functions: Leja interpolation, Krylov and related methods](/methods/phi-function-evaluation.md)
* [Exponential integrators and φ-functions](/methods/exponential-integrators.md)
* [Order reduction](/definitions/order-reduction.md)
* [Stiff accuracy](/properties/stiff-accuracy.md)
* [Stiff order conditions of exponential Runge–Kutta methods and φ-order conditions](/results/exponential-runge-kutta-stiff-order-conditions.md)
