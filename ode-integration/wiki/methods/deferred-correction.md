---
type: Method
title: "Deferred correction (DeC)"
description: "Arbitrarily high-order one-step integrator that iterates a cheap low-order operator against a high-order collocation operator on subnodes of the step; in Abgrall's form K explicit corrections give order min(M+1, K), and linearly implicit variants handle stiff sources."
status: established
aliases: [DeC, deferred correction method, Abgrall's DeC, explicit DeC, IMDeC, implicit deferred correction]
tags: [deferred-correction, explicit, implicit, stiff, order-conditions]
timestamp: 2026-10-19T12:00:00Z
---

# Deferred correction (DeC)

Deferred correction computes the solution of a high-order implicit collocation problem
on subnodes of one step. It does so by a fixed number $K$ of corrections, each of which
solves only a cheap low-order problem. In the two-operator form of Abgrall, used by
[Han Veiga et al. (2021)](/sources/hanveiga-2021.md) (§3, after Dutt, Greengard &
Rokhlin), a low-order explicit operator $\mathcal L^1$ is iterated against a high-order
operator $\mathcal L^2$. The fixed point of the iteration is the collocation solution
$\mathcal L^2=0$, and each iteration gains one order of accuracy. The method reaches
arbitrary order without solving Runge–Kutta
[order conditions](/results/runge-kutta-order-conditions.md), which Han Veiga et al. give
as its motivation (§1, Remark 3.2). With $K$ fixed it is itself a
[Runge–Kutta method](/definitions/runge-kutta-method.md) (Remark 3.2, citing Christlieb,
Ong & Qiu).

**Page-local notation.** Problem $y'=f(y)$ (autonomous; the source writes
$\partial_t\alpha+F(\alpha)=0$, so $f=-F$). Subnodes $t_{n,m}=t_n+c_mh$,
$m=0,\dots,\mathsf M$, with $c_0=0$ and $c_{\mathsf M}=1$ when the nodes include the
endpoints. $Y_m^{(k)}$ is the subnode value after $k$ corrections, and
$\mathbf Y=(Y_0,\dots,Y_{\mathsf M})$. $\ell_r$ are the Lagrange polynomials on the nodes (a basis, unrelated to the registry's multirate micro-step index $\ell$)
$c_0,\dots,c_{\mathsf M}$. $\omega_{mr}=\int_0^{c_m}\ell_r(\vartheta)\,d\vartheta$ are the
integration weights (the source's $\theta^m_r$, normalized to the unit interval).

## The two operators and the iteration

The high-order operator is the collocation (Picard-integral) form on the subnodes, and the
low-order operator is forward Euler from $t_n$ (Han Veiga et al. 2021, eqs. (18)–(20);
signs translated):

$$\begin{aligned}
\mathcal L^2(\mathbf Y)_m&=Y_m-Y_0-h\sum_{r=0}^{\mathsf M}\omega_{mr}\,f(Y_r),\\
\mathcal L^1(\mathbf Y)_m&=Y_m-Y_0-c_m\,h\,f(Y_0),\qquad m=1,\dots,\mathsf M .
\end{aligned}$$

$\mathcal L^2(\mathbf Y)=0$ is an implicit collocation method. The DeC algorithm
(eq. (23)) sets $Y_0^{(k)}=y_n$ for all $k$ and $Y_m^{(0)}=y_n$, then iterates

$$\mathcal L^1(\mathbf Y^{(k)})=\mathcal L^1(\mathbf Y^{(k-1)})-\mathcal L^2(\mathbf Y^{(k-1)}),\qquad k=1,\dots,K,$$

and returns $y_{n+1}=Y^{(K)}_{\mathsf M}$. The unknown enters only through $\mathcal L^1$,
so each correction is explicit. With the forward-Euler $\mathcal L^1$ the correction
collapses to *(compiler algebra, not in the sources)*

$$Y_m^{(k)}=y_n+h\sum_{r=0}^{\mathsf M}\omega_{mr}\,f\big(Y_r^{(k-1)}\big),$$

a discrete Picard iteration on the collocation problem. One step therefore costs
$1+(K-1)\mathsf M$ evaluations of $f$ ($Y^{(0)}_r=y_n$ for all $r$, so the first
correction needs only $f(y_n)$) *(compiler count)*.

**Convergence** (Abgrall's proposition, Prop. 3.1, as recalled by Han Veiga et al.). Let
$\mathcal L^1$ be coercive,
$\kappa_1\lVert\mathbf Y-\mathbf Z\rVert\le\lVert\mathcal L^1(\mathbf Y)-\mathcal L^1(\mathbf Z)\rVert$.
Let $\mathcal L^1-\mathcal L^2$ be Lipschitz with constant $\kappa_2h$. Let
$\mathcal L^2=0$ have a unique solution $\mathbf Y^*$ ($\kappa_1$, $\kappa_2$ page-local).
If $\kappa_2h/\kappa_1<1$, the iteration converges and
$\lVert\mathbf Y^{(k)}-\mathbf Y^*\rVert\le(\kappa_2h/\kappa_1)^k\lVert\mathbf Y^{(0)}-\mathbf Y^*\rVert$.
Each correction therefore gains one power of $h$, and $K$ corrections give order
$\min(\mathsf M+1,K)$ (see [equivalence of DeC and ADER](/results/dec-ader-equivalence.md),
Thm. 4.5). Han Veiga et al. take $K=\mathsf M+1$, "as many iterations as the desired order
of accuracy" (§3).

**Choices** (Remark 3.2). A higher-order $\mathcal L^1$ speeds up convergence of the
iteration but can lower the final accuracy, because the error loses smoothness (citing
Christlieb et al.). Gauss–Legendre subnodes exclude the endpoint and need an extrapolation
to $t_{n+1}$. For continuous finite elements, mass lumping in $\mathcal L^1$ avoids inverting
the global mass matrix while $\mathcal L^2$ keeps the consistent one. This is Abgrall's
motivation, and it makes residual-distribution schemes high order in time (§3, §4.5.1).

## Linearly implicit DeC for stiff sources (IMDeC)

For $y'=f^{\mathrm E}(y)+f^{\mathrm I}(y)$ with stiff $f^{\mathrm I}$, the IMDeC of
Abgrall & Torlo (as recalled by Han Veiga et al. 2021, §4.4, eqs. (38)–(42)) puts the
stiff part into $\mathcal L^1$, linearized at $y_n$:

$$\mathcal L^1(\mathbf Y)_m=Y_m-Y_0-c_mh\Big(f^{\mathrm E}(Y_0)+J^{\mathrm I}_n\,Y_m\Big),\qquad J^{\mathrm I}_n=\frac{\partial f^{\mathrm I}}{\partial y}(y_n)$$

($J^{\mathrm I}_n$ page-local). Each correction then solves, at every subnode,

$$\big(I-c_mh\,J^{\mathrm I}_n\big)\big(Y_m^{(k)}-Y_m^{(k-1)}\big)=-\mathcal L^2\big(\mathbf Y^{(k-1)}\big)_m,$$

i.e. a $d\times d$ linear system per subnode, in which the Jacobian does not interact with
the subnode coupling. Han Veiga et al. compare it with the implicit ADER, which couples all
subnodes in one larger system (see [ADER](/methods/ader-time-integration.md)). On a stiff
linear three-species system ($h=1$, fourth order) and on the Robertson problem (third order,
30 steps with $h_n=2h_{n-1}$), both implicit variants follow the reference solution while the
explicit DeC and ADER fail. Implicit ADER is visibly more accurate than IMDeC (Figs. 9–10).
Their heuristic is that IMDeC treats the $\mathcal L^1$ terms "in a very simplified first
order manner", while implicit ADER "is closer to a pure implicit scheme" (§4.4, §5.3).
Abgrall & Torlo's scheme was designed as an AP IMEX scheme for kinetic models (see
[asymptotic-preserving scheme](/definitions/asymptotic-preserving-scheme.md)).

## Linear stability

For $y'=\lambda y$ the explicit DeC (orders 2 to 5) and explicit ADER have identical
stability regions, independent of the node family (equispaced, Gauss–Lobatto,
Gauss–Legendre), and the regions grow with the order (Han Veiga et al. 2021, §5.1, Fig. 2;
computed numerically). They call an analytic study "not feasible". Their reason is that it
"leads to solving polynomial inequalities of degree $p(p+1)$". The node independence has a
short explanation *(compiler check, not in the sources)*. Each correction raises the degree
in $z=h\lambda$ by one, so $R(z)$ is a polynomial of degree at most $K$. Order $K$ then
forces $R(z)=\sum_{j=0}^{K}z^j/j!$ for $K\le\mathsf M+1$, the Taylor polynomial. This is the
[stability polynomial](/definitions/stability-function.md) of every $K$-stage explicit
Runge–Kutta method of order $K\le4$.

## Accuracy observations

On the scalar test $y'=\lambda y$ ($\lambda=10$, $t\in[0,0.1]$), with orders up to 11, DeC
keeps its design order with equispaced nodes. ADER with equispaced nodes does not at the
highest orders. Han Veiga et al. attribute this to DeC not needing a mass matrix (§5.2.1),
and they note that equispaced quadrature weights turn negative from ninth order. On a
nonlinear scalar ODE, a linear three-species system, Lotka–Volterra (including $t\le100$
with $h=1$) and on spectral-difference semi-discretizations of linear advection and
Burgers (orders 3 to 9, $h=\frac{0.5}{\mathsf M+1}\frac{\Delta x}{\lvert v_{\max}\rvert}$),
DeC and ADER both reach their design orders (§5.2–5.3).

## Qualifications

- **Order of the collocation operator.** Han Veiga et al. state that $\mathcal L^2=0$ is of
  order $\mathsf M+1$, and they also say the order "depends on the used quadrature rule"
  (§2–3). For Gauss–Lobatto or Gauss–Legendre subnodes the underlying collocation method is
  of higher order ($2\mathsf M$ and $2\mathsf M+2$ respectively; see
  [fully implicit collocation methods](/methods/fully-implicit-runge-kutta.md)). The bound
  $\min(\mathsf M+1,K)$ is therefore a lower bound for such nodes, not the sharp order
  *(compiler note)*.
- **Robustness with equispaced nodes.** The explanation that DeC "does not require a mass
  matrix" is incomplete. DeC still uses the interpolation weights $\omega_{mr}$, which for
  equispaced nodes suffer the same negative-weight problem the paper reports *(compiler
  note, not in the sources)*.
- **Printed slips** (arXiv v3). The ODE is written $\alpha'+F(\alpha)=0$, but the DeC
  operators (eqs. (18)–(20)) carry $-hF$ (i.e. $\alpha'=+F$), and the stiff examples set the
  stiff term equal to the right-hand side. The spectral-difference DeC update (eq. (68))
  restarts from $u^{(k)}$ where the algorithm (23) restarts from $u(t_n)$, as in the formula
  above. Eq. (42) has $\mathcal L^2(\mathbf Y^{(k+1)})$ for $\mathcal L^2(\mathbf Y^{(k)})$.
- The claim that implicit ADER beats IMDeC rests on two plots without error tables.

# Citations

- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) — §1; §3 (eqs. (18)–(23), Prop. 3.1, Remark 3.2); §4.3 (Thm. 4.5); §4.4 (eqs. (37)–(47)); §4.5.1 (DeC–residual distribution); §5.1 (Fig. 2); §5.2–5.3 (Figs. 3–14).
