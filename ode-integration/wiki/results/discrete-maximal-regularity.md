---
type: Result
title: "Discrete maximal regularity of variable-step Galerkin and Runge–Kutta time stepping"
description: "Discrete maximal parabolic L2 regularity holds for arbitrary step sequences for continuous and discontinuous Galerkin time stepping, Gauss, Radau IIA and Lobatto IIIA collocation and every algebraically stable Runge–Kutta method, proved by an energy argument on the pointwise form of the scheme in Hilbert space."
status: established
aliases: [discrete maximal L2 regularity, maximal parabolic regularity of time discretizations, discrete MR estimate]
tags: [stability, runge-kutta, implicit, parabolic, structure-preserving]
timestamp: 2026-10-20T06:18:00Z
---

# Discrete maximal regularity of variable-step Galerkin and Runge–Kutta time stepping

**Maximal $L^2$ regularity** of a linear parabolic problem bounds both $y'$ and the
operator term in $L^2$ in time by the data alone. A time discretization has **discrete
maximal regularity** when the same bound holds for the numerical solution with constants
independent of the steps. [Akrivis, Makridakis & Smaragdakis (2025)](/sources/akrivis-2025.md)
(§4) prove it, by an energy argument and for **arbitrary (variable) step sequences**, for
continuous and discontinuous Galerkin time stepping, for Gauss, Radau IIA and Lobatto IIIA
collocation, and for every algebraically stable Runge–Kutta method. They prove it to obtain the
stability of [Runge–Kutta physics-informed networks](/methods/learned-time-integrators.md), but
the section is a self-contained result on time integration.

Setting and page-local symbols: a Hilbert space with inner product $\langle\cdot,\cdot\rangle$
and norm $\lVert\cdot\rVert$; $\mathcal A=-L$ a coercive, self-adjoint, densely defined operator
(the registry $L$ of $y'=Ly$ with the sign reversed; the source writes $A$, which here would
clash with the Butcher matrix); the problem $y'+\mathcal Ay=g$, $y(0)=y_0\in D(\mathcal A^{1/2})$,
$g\in L^2(0,T)$; $L^2(0,t)$ norms are $L^2$ in time of the Hilbert norm; $h_n=t_{n+1}-t_n$ the
steps, arbitrary; $s$ the number of stages or collocation nodes $c_1<\dots<c_s$, and
$t_{ni}=t_n+c_ih_n$. The source writes $k_n$ for the step and $q$ for the stage count.

## Continuous estimate

Taking the inner product of the equation with itself and using
$2\langle y',\mathcal Ay\rangle=\frac d{dt}\lVert\mathcal A^{1/2}y\rVert^2$ gives the identity

$$\lVert\mathcal A^{1/2}y(t)\rVert^2+\lVert y'\rVert^2_{L^2(0,t)}+\lVert\mathcal Ay\rVert^2_{L^2(0,t)}=\lVert\mathcal A^{1/2}y_0\rVert^2+\lVert g\rVert^2_{L^2(0,t)}$$

(Eq. (65), as recalled with references to Kunstmann–Weis and Denk–Hieber–Prüss). The discrete
estimates below are copies of this identity, with equality or with $\le$.

## The abstract theorem

Write a scheme in **pointwise form**: find a continuous piecewise polynomial $\hat Y$ of degree
$s$ in time with $\hat Y(0)=y_0$ and

$$\hat Y'(t)+\Pi_{s-1}\mathcal A\hat Y(t)=\tilde\Pi_{s-1}g(t),\qquad t\in(t_n,t_{n+1}],$$

where $\Pi_{s-1}$, $\tilde\Pi_{s-1}$ are projections or interpolations onto discontinuous
piecewise polynomials of degree $s-1$ (Eq. (66); $\hat Y$, $\Pi_{s-1}$, $\tilde\Pi_{s-1}$
page-local). The framework is that of Akrivis–Makridakis–Nochetto, as recalled.

**Theorem 8.** If on every step

$$\int_{t_n}^{t_{n+1}}\langle\hat Y',\Pi_{s-1}\mathcal A\hat Y\rangle\,dt\ \ge\ \int_{t_n}^{t_{n+1}}\langle\hat Y',\mathcal A\hat Y\rangle\,dt=\tfrac12\bigl(\lVert\mathcal A^{1/2}\hat Y(t_{n+1})\rVert^2-\lVert\mathcal A^{1/2}\hat Y(t_n)\rVert^2\bigr)\qquad(67)$$

then for $m=1,\dots,N$ and any partition

$$\lVert\mathcal A^{1/2}\hat Y(t_m)\rVert^2+\lVert\hat Y'\rVert^2_{L^2(0,t_m)}+\lVert\Pi_{s-1}\mathcal A\hat Y\rVert^2_{L^2(0,t_m)}\le\lVert\mathcal A^{1/2}y_0\rVert^2+\lVert\tilde\Pi_{s-1}g\rVert^2_{L^2(0,t_m)}\qquad(68).$$

The proof squares the pointwise equation, integrates over the step, uses (67) and sums; no
step-ratio condition enters. Condition (67) is a one-sided property of the projection, the
discrete counterpart of the energy identity.

## Instances

| Method | $\Pi_{s-1}$, $\tilde\Pi_{s-1}$ | Condition (67) | Estimate |
|---|---|---|---|
| continuous Galerkin cG($s$) | both the $L^2$ projection $P_{s-1}$, which on degree-$s$ polynomials equals interpolation at the $s$ Gauss points | equality | identity (74); bound (76) with $\lVert g\rVert$ (Prop. 9) |
| discontinuous Galerkin dG($s-1$), via the Radau reconstruction of Makridakis–Nochetto | interpolation at the Radau nodes, $P_{s-1}$ | inequality, by Radau quadrature exactness to degree $2s-2$ | (84)–(85) (Prop. 10) |
| Gauss collocation | interpolation $I_{s-1}$ at the nodes, both | equality | identity (91)–(92) (Props. 11–12) |
| Radau IIA collocation | $I_{s-1}$, both | inequality | (91)–(92) |
| Lobatto IIIA collocation | see below | — | identity (99), bound (100) (Prop. 13) |

For collocation methods the pointwise form is $\hat Y'+I_{s-1}\mathcal A\hat Y=I_{s-1}g$ with
$\hat Y$ the collocation polynomial (Eqs. (24), (87); see
[fully implicit Runge–Kutta methods](/methods/fully-implicit-runge-kutta.md)), and the
estimate reads in nodal and stage values $y_n$, $Y_{ni}$ (Prop. 12, Eq. (92)):

$$\lVert\mathcal A^{1/2}y_m\rVert^2+\sum_{n=0}^{m-1}h_n\sum_{i=1}^sb_i\lVert\hat Y'(t_{ni})\rVert^2+\sum_{n=0}^{m-1}h_n\sum_{i=1}^sb_i\lVert\mathcal AY_{ni}\rVert^2\le\lVert\mathcal A^{1/2}y_0\rVert^2+\sum_{n=0}^{m-1}h_n\sum_{i=1}^sb_i\lVert g(t_{ni})\rVert^2,$$

with equality for Gauss; for Radau IIA $\hat Y'(t_{ns})$ is the left derivative at $t_{n+1}$.

**Lobatto IIIA.** Its coefficient matrix is singular (first row zero) and the methods are
A-stable but not B-stable, so neither the collocation argument nor algebraic stability applies
directly. Akrivis et al. show that the degree-$(s-1)$ interpolant $\tilde Y=I_{s-1}\hat Y$ of the
Lobatto IIIA collocation solution, which is continuous because both endpoints are nodes, solves a
**modified cG($s-1$) method** with forcing $I_{s-1}g$ (Eq. (95), proved by integration by parts
and Lobatto quadrature exactness to degree $2s-3$), and deduce the identity (99) with the
interpolation at $s-1$ Gauss points in the operator term. They describe this as a new connection
and the estimates as "the first maximal regularity estimates in the literature" for Lobatto IIIA
(§1, §4.4.2); the priority claim is theirs. For the trapezoidal rule ($s=2$), Remark 14 gives the
exact identity

$$\lVert\mathcal A^{1/2}y_m\rVert^2+\sum_{n=0}^{m-1}h_n\Bigl\lVert\frac{y_{n+1}-y_n}{h_n}\Bigr\rVert^2+\sum_{n=0}^{m-1}h_n\Bigl\lVert\mathcal A\frac{y_{n+1}+y_n}2\Bigr\rVert^2=\lVert\mathcal A^{1/2}y_0\rVert^2+\sum_{n=0}^{m-1}h_n\Bigl\lVert\frac{g(t_{n+1})+g(t_n)}2\Bigr\rVert^2$$

for arbitrary partitions (Eq. (101)).

## Algebraically stable Runge–Kutta methods

For any $s$-stage Runge–Kutta method with distinct nodes that is
[algebraically stable](/properties/a-stability.md), i.e. $b_i\ge0$ and
$\mathcal M=(b_ia_{ij}+b_ja_{ji}-b_ib_j)$ positive semidefinite ($\mathcal M$ page-local; the
registry reserves $M$ for the mass matrix), Akrivis et al. (§4.4.3, Eqs. (105)–(111)) apply
$\mathcal A^{1/2}$ to the Runge–Kutta equations and expand, as in the classical proof that
algebraic stability implies B-stability:

$$\lVert\mathcal A^{1/2}y_{n+1}\rVert^2=\lVert\mathcal A^{1/2}y_n\rVert^2-\sum_{i,j}\mathcal M_{ij}\langle\mathcal A^{1/2}\varphi_i,\mathcal A^{1/2}\varphi_j\rangle+2\sum_ib_i\langle\varphi_i,\mathcal AY_{ni}\rangle,\qquad\varphi_i=h_n\bigl(g(t_{ni})-\mathcal AY_{ni}\bigr)$$

($\varphi_i$ page-local). Dropping the $\mathcal M$ term and using
$2\langle g,\mathcal AY\rangle=\lVert g\rVert^2+\lVert\mathcal AY\rVert^2-\lVert g-\mathcal AY\rVert^2$
gives, summed over steps, the estimate (111) of the same form as (92), with
$\lVert g(t_{ni})-\mathcal AY_{ni}\rVert$ in place of $\lVert\hat Y'(t_{ni})\rVert$, for every
algebraically stable method and variable steps. *(Compiler check, not in the source: the
per-step inequality
$\lVert\mathcal A^{1/2}y_{n+1}\rVert^2+h_n\sum_ib_i\bigl(\lVert g(t_{ni})-\mathcal AY_{ni}\rVert^2+\lVert\mathcal AY_{ni}\rVert^2\bigr)\le\lVert\mathcal A^{1/2}y_n\rVert^2+h_n\sum_ib_i\lVert g(t_{ni})\rVert^2$
follows from the identity above with $\mathcal M\succeq0$ alone.)* For Gauss and Radau IIA it
reduces to (92). The argument is the [Runge–Kutta energy method](/methods/runge-kutta-energy-method.md)
in the $\mathcal A^{1/2}$-norm.

## Relation to earlier results

Kovács, Li & Lubich (2016), as recalled by Akrivis et al. (§1, Remark 15), proved discrete
maximal $L^p$ regularity for A-stable time discretizations, for any $p\in(1,\infty)$ and in UMD
Banach spaces, with **constant** steps, which Akrivis et al. call "a key assumption"; their
Thm. 3.2 gives for the trapezoidal rule the inequality with a constant $C$, for $y_0=0$. The two
results extend each other: Kovács–Li–Lubich are more general in $p$ and in the space; Akrivis et
al. are restricted to $p=2$ in Hilbert space but allow arbitrary steps, give identities with
constant one for cG, Gauss and the trapezoidal rule, and include high-order Lobatto IIIA, which
Remark 15 says the Kovács–Li–Lubich analysis does not cover. This is a difference of scope, not
a contradiction.

## Qualifications

- The results are for **linear** problems with a self-adjoint coercive operator and
  time-dependent forcing; nonlinear and non-self-adjoint problems are not treated.
- Akrivis et al. state that, because the nodes are distinct, B-stability and algebraic
  stability are equivalent (§4.4.3). The estimate (111) uses only the direction algebraic
  stability $\Rightarrow$ estimate, so the equivalence is not needed for it; see
  [A-, L- and algebraic stability](/properties/a-stability.md).
- §4.4.3 writes the derivation with $\hat Y'(t_{ni})$, a collocation reading; for a
  non-collocation method the quantity is $g(t_{ni})-\mathcal AY_{ni}$, as above.
- **Printed slips (arXiv v2).** The text indexes the Lobatto nodes from $c_0=0$ in one place
  (§4.4.2) and from $c_1=0$ elsewhere; Eq. (109) writes $k$ for $k_n$; Remark 15 says "Lobatto
  IIA" for Lobatto IIIA; §4.2 lets the subinterval index run to $N$ instead of $N-1$.

# Citations

- [Akrivis, Makridakis & Smaragdakis (2025)](/sources/akrivis-2025.md) — §1, §4.1 (Eq. 65), §4.2 (Eqs. 66–70, Thm. 8), §4.3 (Props. 9–10, Eqs. 71–85), §4.4.1 (Props. 11–12, Eqs. 86–92), §4.4.2 (Eqs. 93–104, Prop. 13, Remarks 14–16), §4.4.3 (Eqs. 105–111).
