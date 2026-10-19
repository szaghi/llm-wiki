---
type: Method
title: "DIRK schemes with high weak stage order"
description: "Diagonally implicit Runge–Kutta schemes designed to have weak stage order above their stage order: the $(2,2,3)$ and $(3,3,3)$ families, the eigenvector-criterion schemes up to weak stage order 3, and the stiffly accurate L-stable DIRK-(7,4,4), DIRK-(12,5,4) and DIRK-(12,5,5) found by constrained polynomial optimization, which recover full order on linear stiff problems."
status: established
aliases: [high-WSO DIRK, DIRK-(7,4,4), DIRK-(12,5,4), DIRK-(12,5,5)]
tags: [runge-kutta, implicit, order-reduction, stiff, order-conditions]
timestamp: 2026-10-19T12:00:00Z
---

# DIRK schemes with high weak stage order

[DIRK methods](/methods/diagonally-implicit-runge-kutta.md) cannot have stage order
above 2, but they can have high [weak stage order](/definitions/weak-stage-order.md)
$q_{\mathrm w}$, the condition $b^\top A^j\tau^{(k)}=0$ ($j<s$, $k\le q_{\mathrm w}$)
that removes [order reduction](/definitions/order-reduction.md) on linear stiff
problems. Schemes are labelled $(s,p,q_{\mathrm w})$: stages, classical order, weak
stage order. Before 2022 such schemes reached $q_{\mathrm w}=3$ through the
eigenvector criterion; [Biswas et al. (2023)](/sources/biswas-2023.md) construct the
first DIRK schemes with $q_{\mathrm w}=4$ and 5, using the algebraic theory of
[Biswas et al. (2024)](/sources/biswas-2024.md).

## From the eigenvector criterion to the minimal polynomial

Earlier constructions (Rosales et al.; Ketcheson, Seibold, Shirokoff and Zhou 2020)
required each residual $\tau^{(k)}$ to be an eigenvector of $A$, with $b$ orthogonal
to those eigenvectors; this gave DIRK schemes up to order 4 and $q_{\mathrm w}=3$
(Biswas et al. 2024, §1.2; Biswas et al. 2023, §3). In the language of the
[barriers](/results/weak-stage-order-barriers.md), the criterion means that the
minimal polynomial $\mu_{\mathcal K}$ (page-local) of the residual space
$\mathcal K_{q_{\mathrm w}}$ (registry symbol) has degree at most 1, and with invertible $A$
this caps $q_{\mathrm w}\le3$. Going beyond needs $\deg\mu_{\mathcal K}\ge2$, and
for an irreducible DIRK with invertible $A$, $q_{\mathrm w}>3$ and
$\deg\mu_{\mathcal K}=2$ force $\mu_{\mathcal K}(x)=(x-a_{11})(x-a_{22})$ (Biswas et
al. 2023, Thms. 4.1, 4.3; Biswas et al. 2024, Lemma 6.5).

Biswas et al. (2024, Remark 7.5) turn this into a construction guide for
$q_{\mathrm w}=p$: take $r=\lfloor q_{\mathrm w}/2\rfloor$, impose
$\mu_{\mathcal K}(x)=(x-a_{11})\cdots(x-a_{rr})$, solve
$\mu_{\mathcal K}(A)\tau^{(k)}=0$ as a sufficient condition, and size $s$ with the
DIRK barrier.

## Small exact families

- **$(2,2,3)$.** Exactly two schemes,
  $A=\begin{pmatrix}1\mp\frac{\sqrt2}2&0\\\frac12\pm\frac{\sqrt2}2&\frac12\end{pmatrix}$,
  $b=(\frac12\pm\frac{\sqrt2}4,\ \frac12\mp\frac{\sqrt2}4)^\top$, with $b^\top A=\frac12b^\top$
  and $R(z)=(1+z/2)/(1-z/2)$ (Biswas et al. 2024, Ex. 7.1).
- **$(3,3,3)$.** A one-parameter family in the scale $a$ of the leading block,
  $a_{11}=(1\mp\frac{\sqrt2}2)a$, $a_{22}=\frac a2$, $a_{33}=\frac{3a-2}{6(a-1)}$;
  three branches for $(a_{31},a_{32})$, two of them S-reducible; no member reaches
  $p=4$ or $q_{\mathrm w}=4$; $0<a<\frac23$ or $a>1$ is needed for positive
  eigenvalues of $A$ and right-half-plane poles of $R$ (Biswas et al. 2024, Ex. 7.2).
- **Stiffly accurate $(4,3,3)$** schemes of Ketcheson et al. (2020) are sharp for
  the DIRK barrier (Biswas et al. 2024, Ex. 7.3).

## The reduced system with $\dim\mathcal K_{q_{\mathrm w}}=2$

Biswas et al. (2023, §4) choose a two-dimensional residual space spanned by
page-local vectors $w_1,w_2$ with $(A-a_{11}I)(A-a_{22}I)w_j=0$, in one of two
branches:

$$\begin{aligned}
&a_{11}\neq a_{22}:&&Aw_1=a_{11}w_1,\quad Aw_2=a_{22}w_2,\\
&a_{11}=a_{22}:&&Aw_1=a_{11}w_1,\quad Aw_2=a_{11}w_2+w_1,
\end{aligned}$$

together with $\tau^{(k)}\in\operatorname{span}\{w_1,w_2\}$ for $2\le k\le q_{\mathrm w}$
and $b^\top w_1=b^\top w_2=0$ (Eqs. (22)–(26)). This choice caps $q_{\mathrm w}\le5$
and needs $s\ge p+1+\delta_{\mathrm{SA}}$ ($\delta_{\mathrm{SA}}=1$ for stiffly
accurate schemes, page-local). Confluent schemes, $c_1=\dots=c_r$ with $r\ge2$,
satisfy the equations but are S-reducible to a smaller scheme and are excluded
(Lemma 4.4). The weak-stage-order conditions also make $(p-1)(p-2)/2$ order
conditions redundant (Table 2). For $p=4$ the last row of the construction
solves only the quadrature conditions $b^\top c^{k-1}=1/k$, $k\le4$, and
$b^\top\mathrm{diag}(c)Ac=\frac18$, besides $b^\top w_1=b^\top w_2=0$ (Eq. (28));
for $p=5$ six more conditions are added (§5.1).

## Construction by optimization

Biswas et al. (2023, §5) pose a constrained polynomial optimization: minimize the
squared $\ell_2$ norm of the order-$(p+1)$ residuals subject to lower-triangular
$A$, order $p$, the reduced weak-stage-order system, stiff accuracy $a_{sj}=b_j$,
$c_j\ge0$, $a_{ii}\ge0$ and $|R(iy)|\le1$ on a finite sample of the imaginary axis.
Non-negative diagonal plus $|R(iy)|\le1$ gives A-stability, and with stiff accuracy
L-stability (see [A-stability](/properties/a-stability.md),
[stiff accuracy](/properties/stiff-accuracy.md)). Feasible points come from a
hybrid analytic–numerical row-by-row solve of the branch $a_{11}\neq a_{22}$
(rejecting $|a_{ij}|>20$ or residuals above $10^{-10}$) refined by Gauss–Newton;
then more than $10^5$ local SQP solves pick, per class, a scheme near-optimal in the
objective and Pareto-optimal in $(\text{objective},\max|a_{ij}|)$. A-stability is
checked a posteriori (Fig. 1).

## The three schemes

| scheme | abscissae $c$ (rounded) | $\max\lvert a_{ij}\rvert$ | first entries |
|---|---|---|---|
| DIRK-(7,4,4) | $0.129, 0.449, 0.010, 1.231, 2.979, 1.248, 1$ | $\approx2.46$ | $a_{11}=0.1290066345260422$, $b_7=a_{77}=0.3395048796261326$ |
| DIRK-(12,5,4) | $0.235, 0.743, 0.033, 0.738, 0.238, 1.750, 2.990, 2.882, 2.914, 2.574, 3.567, 1$ | $\approx2.86$ | $a_{11}=0.2345371908646273$ |
| DIRK-(12,5,5) | $0.041, 0.227, 0.622, 1.378, 1.260, 1.228, 1.270, 2.496, 2.784, 3.337, 4.173, 1$ | $\approx12.37$ | $a_{11}=0.04113473525867655$, $b_{12}=0.5454220210658036$ |

All three are stiffly accurate, A- and L-stable, have non-negative abscissae and
$a_{11}\neq a_{22}$ (so they are not SDIRK); the full 16-digit coefficients are in
Biswas et al. (2023), App. A, Table 3. They are the first DIRK schemes with weak
stage order above 3 (§8). The searches found no scheme with the same $(p,q_{\mathrm w})$
and fewer stages under the imposed constraints (§5.1). A preliminary search in the
branch $a_{11}=a_{22}$ with $\dim\mathcal K_{q_{\mathrm w}}>2$ found SDIRK schemes with high weak
stage order, none of which is given (Remark 5.1).

## Numerical behaviour

Against the $q_{\mathrm w}=1$ references DIRK-(5,4,1) and DIRK-(5,5,1), Biswas et
al. (2023, §6–7) report:

- **[Prothero–Robinson](/benchmarks/prothero-robinson-problem.md)**, $\lambda=-10^4$:
  DIRK-(7,4,4) and DIRK-(12,5,5) converge at order $p$ throughout, the references at
  about 1 in the stiff regime (Fig. 2).
- **Heat and Schrödinger equations** with time-dependent Dirichlet data:
  DIRK-(7,4,4) and DIRK-(12,5,5) reach full order in $u$ and $u_x$; DIRK-(12,5,4)
  full order in $u$ and 4.5 in $u_x$ (Figs. 3–4).
- **Linear advection:** DIRK-(12,5,4) order 5 in $u$, 4 in $u_x$ (Fig. 6).
- **Fourth-order PDE** $u_t=-u_{xxxx}+f$, variable-coefficient heat, 2D
  advection–diffusion with corners, advection–diffusion with a physical boundary
  layer: expected orders recovered (Figs. 5, 7–9).
- **Beyond the theory:** slowly time-varying coefficients practically remove the
  reduction, rapidly varying ones do not (errors still smaller); viscous Burgers
  converges at order 3; Van der Pol with $\mu=500$ keeps its reduction for
  $10^{-2}<h<10^{-1}$ (Figs. 10–12).

## Qualifications

- Several abscissae lie far outside $[0,1]$, up to $c\approx4.17$; the construction
  imposes only $c_j\ge0$ and the paper does not discuss stage times beyond the step,
  which matter when forcing or boundary data are evaluated at $t_n+c_ih$.
- Stage counts (7, 12, 12) are search results, well above the lower bounds of the
  [barriers](/results/weak-stage-order-barriers.md); fewer-stage schemes are not
  excluded.
- Biswas et al. (2023) read the arXiv companion of Biswas et al. (2024) for
  Theorems 4.1–4.3; statements on this page are attributed to whichever source
  states them.

# Citations

- [Biswas et al. (2023)](/sources/biswas-2023.md) — §3 Table 2; §4 Thms. 4.1–4.3, Eqs. (22)–(26), Lemma 4.4; §5, §5.1 Remark 5.1, Fig. 1; §6–7 Figs. 2–12; §8; App. A Table 3.
- [Biswas et al. (2024)](/sources/biswas-2024.md) — §1.2; Lemma 6.5; Exs. 7.1–7.3; Remark 7.5.
