---
type: Method
title: "Explicit Runge–Kutta methods with high weak stage order"
description: "Explicit Runge–Kutta methods whose weights are orthogonal to the residual space up to weak stage order $q_{\\mathrm w}\\ge2$, which alleviates order reduction on hyperbolic problems with time-dependent boundary data; stage bound $p+q_{\\mathrm w}\\le s+1$, Sylvester-equation characterization, optimized schemes up to $(9,5,5)$, parallel-iterated $(p^2,p,p)$ schemes, and zero SSP coefficient."
status: established
aliases: [high-WSO ERK, explicit RK alleviating order reduction, ERK312, ERK313]
tags: [runge-kutta, explicit, order-reduction, order-conditions, ssp]
timestamp: 2026-10-19T07:44:00Z
---

# Explicit Runge–Kutta methods with high weak stage order

Explicit [Runge–Kutta methods](/definitions/runge-kutta-method.md) have stage order
at most 1, and on initial-boundary-value problems with time-dependent boundary data
they suffer [order reduction](/definitions/order-reduction.md), typically to second
order. [Biswas et al. (2025)](/sources/biswas-2025.md) remove most of it by
imposing [weak stage order](/definitions/weak-stage-order.md) $q_{\mathrm w}\ge2$,
i.e. $b^\top A^j\tau^{(k)}=0$ for all $j\ge0$ and $2\le k\le q_{\mathrm w}$, which is
compatible with explicit structure; they give a general theory, optimized schemes
up to order 5 and $q_{\mathrm w}=5$, and a family reaching any $q_{\mathrm w}$. The
remedy changes only the coefficients, unlike the boundary-modification remedies
(Carpenter et al., Abarbanel et al., Pathria, Alonso-Mallo), which need derivatives
of the boundary data, extra parameters, intrusive changes, and have been studied
only in one dimension (§1). Schemes are labelled $(s,p,q_{\mathrm w})$.

## Structure theory

Registry symbols, as on [weak-stage-order barriers](/results/weak-stage-order-barriers.md):
$\mathcal K_m$ the Krylov space of the residuals $\tau^{(k)}$, $k\le m$, $\mathcal Y$ the
smallest $A^\top$-invariant subspace containing $b$, $n_c$ the number of distinct abscissae
(Biswas et al. write $K_q$, $Y$).

- $p\le\deg P\le\dim\mathcal Y\le s-\dim\mathcal K_{q_{\mathrm w}}$ (Lemma 2.1). A
  method with $p>1$ and $q_{\mathrm w}>1$ has $\deg P<s$, hence a zero on the first
  subdiagonal of $A$.
- $p+q_{\mathrm w}\le s+1$ for $p\ge2$ (Thm. 2.3), with equality only if
  $\dim\mathcal K_{q_{\mathrm w}}=q_{\mathrm w}-1$ and $\dim\mathcal Y=p$.
- **Necessary conditions (Thm. 2.4).** Write $A$ in blocks of sizes
  $1,\ q_{\mathrm w}-1,\ s-q_{\mathrm w}$, with diagonal blocks $0$, $A_{22}$, $A_{33}$,
  subdiagonal blocks $A_{21}$, $A_{31}$, $A_{32}$, and $c=(0,c_U,c_L)$; let
  $V_U=[c_U\ c_U^2\cdots c_U^{q_{\mathrm w}-1}]$,
  $W_U=[\frac12c_U^2\ \frac13c_U^3\cdots\frac1{q_{\mathrm w}}c_U^{q_{\mathrm w}}]$ and
  $V_L$, $W_L$ likewise (all page-local). An irreducible explicit method with weak
  stage order $q_{\mathrm w}$ and $\dim\mathcal K_{q_{\mathrm w}}=q_{\mathrm w}-1$ has
  $c_1,\dots,c_{q_{\mathrm w}+1}$ distinct, $a_{q_{\mathrm w}+1,q_{\mathrm w}}=0$, a
  unique matrix $X$ (page-local) with
  $$A_{33}X-XW_UV_U^{-1}=(A_{33}V_L-W_L)V_U^{-1},\qquad XA_{22}-A_{33}X=A_{32},$$
  and weights of the form $b=\begin{pmatrix}1&0\\0&-X^\top\\0&I\end{pmatrix}\beta$
  for some $\beta\in\mathbb R^{s-q_{\mathrm w}+1}$. Then
  $\mathcal K_{q_{\mathrm w}}$ is the column space of $(0;I;X)$. The Sylvester
  equations are uniquely solvable because $A_{33}$ is nilpotent and $W_UV_U^{-1}$
  has non-zero eigenvalues.
- **Sufficiency (Thm. 2.5)** and **minimality (Thm. 2.6).** Any $(A,b)$ admitting
  such $(X,\beta)$ has $q_{\mathrm w}\ge q$; a method with $p\ge2$ has
  $q_{\mathrm w}=s+1-p$ iff it satisfies these conditions, and then
  $R(z)=\sum_{j=0}^pz^j/j!$, the Taylor polynomial: stage-optimal methods have the
  linear stability of a $p$-stage order-$p$ method.
- **No SSP (Thm. 2.7, Cor. 2.8).** $A\ge0$, $b\ge0$ forces $q_{\mathrm w}=1$ (or
  $p\le1$); every method with $p,q_{\mathrm w}\ge2$ has
  [SSP coefficient](/methods/strong-stability-preserving-runge-kutta.md) zero. The
  (3,2,2), (4,3,2) and (5,3,3) methods below still have linear SSP coefficient 1.

## Construction (Algorithm 1)

Choose $A_{22}$, $A_{33}$ and $c$ with $c_1=0$, $c_2,\dots,c_{q_{\mathrm w}+1}$
distinct, $q_{\mathrm w}\ge p-1$ and $p+q_{\mathrm w}=s+1$; solve the first
Sylvester equation for $X$; set $A_{32}=XA_{22}-A_{33}X$, $A_{21}=c_U-A_{22}\mathbf 1$,
$A_{31}=c_L-A_{32}\mathbf 1-A_{33}\mathbf 1$; choose $\beta$ so that $b$ satisfies the
quadrature conditions $b^\top c^{j-1}=1/j$, $j\le p$. With $q_{\mathrm w}\ge p-1$
these imply the "palm-tree" conditions $b^\top A^kc^j=1/((k+j+1)\cdots(j+1))$,
$j+k\le p-1$ (Eq. (3.2), stated without proof), which are all the order conditions
for $p\le3$; for $p\ge4$ the remaining conditions are solved with the leftover
freedom (§3.1). Coefficients are then optimized for the principal error norm
$\mathcal A^{(p+1)}$ (the 2-norm of the order-$(p+1)$ residuals) and, secondarily,
for the coefficient size $\mathcal D=\max\{|a_{ij}|,|b_i|,|c_i|\}$, with
$0\le c_i\le1$; the authors used their Integreat library.

## Schemes

- **(3,2,2) family:** $c=(0,c_2,c_3)$, $a_{21}=c_2$, $a_{31}=c_3$, $a_{32}=0$,
  $b=\big(1-\frac1{2c_2}-\frac1{2c_3},\ \frac{c_3}{2c_2(c_3-c_2)},\ \frac{c_2}{2c_3(c_2-c_3)}\big)$.
  All members have $R=1+z+z^2/2$; the optimal one is $c=(0,\frac12,1)$,
  $b=(-\frac12,2,-\frac12)$ (Eq. (3.4)).
- **(4,3,2):** $c=(0,\frac3{10},\frac23,\frac34)$; $a_{21}=\frac3{10}$;
  $a_{31}=\frac23$, $a_{32}=0$; $a_{41}=-\frac{21}{320}$, $a_{42}=\frac{45}{44}$,
  $a_{43}=-\frac{729}{3520}$; $b=(\frac7{108},\frac{500}{891},-\frac{27}{44},\frac{80}{81})$
  (Eq. (3.5)).
- **(5,3,3):** $c=(0,\frac3{11},\frac{15}{19},\frac56,1)$, exact rational
  coefficients in Eq. (3.6); its $\mathcal A^{(4)}$ is minimal iff
  $b^\top\mathrm{diag}(c)Ac=\frac18$.
- **(6,4,3), (7,4,4), (8,5,4), (9,5,5):** exact rational coefficients in App. A; in
  (8,5,4) and (9,5,5) the abscissae are rational approximations of Gauss–Lobatto
  points and $A_{22}=0$, so stages $2,\dots,q_{\mathrm w}+1$ can be evaluated in
  parallel.
- **Skvortsov's ERK312 and ERK313** (background, compared with (4,3,2) and (5,3,3)
  in Table 3.2): ERK312 has $c=(0,\frac12,1,1)$, $b=(\frac16,\frac23,-\frac16,\frac13)$,
  and its first three stages are the optimal (3,2,2) scheme; ERK313 is L-shaped
  (non-zero entries of $A$ only in the first column and the last row),
  $c=(0,\frac13,\frac23,1,0)$, $b=(\frac14,-3,\frac{15}4,-1,1)$. L-shaped schemes
  cannot reach $p=q_{\mathrm w}=4$ (Remark 2, "it can be shown").

The minimum stage counts found (Table 3.1), for $p=2,\dots,5$:

| | $p=2$ | $p=3$ | $p=4$ | $p=5$ |
|---|---|---|---|---|
| $q_{\mathrm w}=1$ | 2 | 3 | 4 | 6 |
| $q_{\mathrm w}=2$ | 3 | 4 | 5 | 6 |
| $q_{\mathrm w}=3$ | 4 | 5 | 6 | 7 |
| $q_{\mathrm w}=4$ | 5 | 6 | 7 | 8 |
| $q_{\mathrm w}=5$ | 6 | 7 | 8 | 9 |

Every row with $q_{\mathrm w}\ge2$ attains $s=p+q_{\mathrm w}-1$; the
$q_{\mathrm w}=1$ row is the classical count. Error norms $(\mathcal A^{(p+1)},\mathcal D)$
(Table 3.2): (3,2,2) $2.357\times10^{-1}$, 2; SSPRK3 $7.217\times10^{-2}$, 1; (4,3,2)
$5.893\times10^{-2}$, 1.003; ERK312 $7.217\times10^{-2}$, 2; (5,3,3)
$7.217\times10^{-2}$, 1.858; ERK313 $1.443\times10^{-1}$, 3.75; RK4
$1.450\times10^{-2}$, 1; (6,4,3) $1.443\times10^{-2}$, 1.144; (7,4,4)
$1.667\times10^{-2}$, 6.187; Dormand–Prince 5 $3.991\times10^{-4}$, 11.60; (8,5,4)
$1.217\times10^{-2}$, 25.33; (9,5,5) $3.316\times10^{-2}$, 44.42.

**Arbitrary weak stage order (Thm. 3.1).** For every $p\ge2$ a $(p^2,p,p)$ method
exists: a parallel-iterated Runge–Kutta method (Hairer–Nørsett–Wanner §II.11) built
on a $(p+1)$-stage basic method in Burrage's V-transformed form,
$\tilde A=\tilde V\tilde S\tilde V^{-1}$, $\tilde V=[\mathbf 1\,|\,\tilde c\,|\cdots|\,\tilde c^p]$,
$\tilde S$ with subdiagonal $1,\frac12,\dots,\frac1p$ (tilde quantities page-local).
Generic parallel iteration does not raise $q_{\mathrm w}$; this basic method does.
On an ideal parallel machine the cost is about that of a serial $p$-stage method.

**Cheaper linear evaluations (Thm. 4.1).** For $y'=Ly+g(t)$ an explicit method with
$d=\dim\mathcal Y$ is equivalent to a 2-partition
[GARK method](/methods/generalized-additive-runge-kutta.md) with only $d$ products
by $L$ and $s$ evaluations of $g$; stage-optimal methods have $d=p$.

## Numerical evidence

Clawpack/SharpClaw with centred fifth-order reconstruction, exact boundary cell
averages at every stage (§5):

- **Linear advection with forcing**, CFL 0.9: SSPRK3, RK4 and Dormand–Prince
  ($q_{\mathrm w}=1$) drop to order 2 in $u$ and 1 in $u_x$; all high-$q_{\mathrm w}$
  methods reach order $p$ in $u$, and those with $q_{\mathrm w}=p-1$ lose one order
  in $u_x$ through $\mathcal O(h)$ boundary layers (Fig. 5.1).
- **Inviscid Burgers**: order $\ge3$ in $u$, 2 in $u_x$, against 2 and 1 (Fig. 5.2).
- **1D shallow water** (manufactured), **2D Thacker parabolic flood wave**: order 3
  against 2, with much smaller errors (Figs. 5.3, 5.5).
- **2D linear acoustics**, CFL 0.45: full order for (5,3,3), (7,4,4), (9,5,5)
  (Fig. 5.4).
- **$q_{\mathrm w}=3$ comparison**: (5,3,3), ERK313 and the parallel-iterated (9,3,3)
  all reach order 3; (5,3,3) has the smallest Burgers error (Fig. 5.6).

## Qualifications

- The guarantee is for linear problems; the nonlinear improvements (order 3) are
  observations, consistent with the DIRK case of
  [Biswas et al. (2023)](/sources/biswas-2023.md).
- The authors' rates "$\min(p,q_{\mathrm w}+1)$ for linear PDEs, $\min(p,q_{\mathrm w})$
  for ODEs" (§3) are stated, not proved.
- Printed slips (arXiv v2): Algorithm 1 lists $A_{32}$ twice among its outputs
  (the second is $A_{31}$); the proof of Lemma 2.2 writes "$\dim K_q\ge m-1$" for
  $q-1$; §7 cites Theorem 2.4 for the stage bound, which is Theorem 2.3. The
  authors' own Sylvester unknown is named $L$; it is renamed $X$ here because
  $L$ denotes the linear operator.

# Citations

- [Biswas et al. (2025)](/sources/biswas-2025.md) — §1, §1.3; Lemmas 2.1–2.2; Thms. 2.3–2.7, Cor. 2.8, Remarks 1–2; §3.1 Algorithm 1, Eqs. (3.2)–(3.6), Tables 3.1–3.2; Thm. 3.1; Thm. 4.1; §5 Figs. 5.1–5.6; §7; App. A.
- [Biswas et al. (2023)](/sources/biswas-2023.md) — §7.2.
