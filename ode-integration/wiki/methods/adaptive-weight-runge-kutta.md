---
type: Method
title: "Adaptive-weight (positivity-preserving) Runge–Kutta methods"
description: "After the stages of a Runge–Kutta step are computed, a linear program replaces the weights by the nearest weights that keep the update nonnegative and satisfy the order conditions up to a possibly reduced order; every step remains a Runge–Kutta step, so linear invariants are kept, and convex adaptation inherits A-stability."
status: established
aliases: [positivity-preserving adaptive Runge–Kutta, adaptive weights, weight adaptation, free adaptation, convex adaptation, bound-preserving adaptive Runge–Kutta]
tags: [runge-kutta, positivity, structure-preserving, step-size-control, stiff]
timestamp: 2026-10-20T03:57:00Z
---

# Adaptive-weight (positivity-preserving) Runge–Kutta methods

[Nüßlein et al. (2021)](/sources/nusslein-2021.md) keep the stages of a Runge–Kutta step
$(A,b,c)$ and change only its weights when the update has negative entries. With
$\mathsf F_n=[f(t_n+c_1h,Y_1),\dots,f(t_n+c_sh,Y_s)]\in\mathbb R^{d\times s}$ (page-local)
the update is $y_{n+1}=y_n+h\mathsf F_nb$, which is **linear in the weights** once the
stages are known (§2, Eqs. (2.1)–(2.4)). Nonnegativity
$y_n+h\mathsf F_n\tilde b\ge0$ is then a set of linear inequalities in new weights
$\tilde b$ (Eq. (2.7)), and the [Runge–Kutta order conditions](/results/runge-kutta-order-conditions.md)
for fixed $(A,c)$ are linear equalities $G_{\tilde p}\tilde b=r_{\tilde p}$ up to an order
$\tilde p\le p$ (page-local $G_{\tilde p}$, $r_{\tilde p}$, as on
[embedded pairs](/methods/embedded-runge-kutta-pair.md)). Choosing $\tilde b$ is therefore a
linear program. Each step is a Runge–Kutta step $(A,\tilde b_n)$, so every linear invariant
of the ODE (total mass, element counts) is preserved exactly, unlike clipping or orthogonal
projection onto the nonnegative orthant (§1–2).

## Free and convex adaptation

**Free adaptation** (§3, LP (3.1)):

$$\min_{\tilde b}\ \lVert\tilde b-b\rVert_1\quad\text{subject to}\quad y_n+h\mathsf F_n\tilde b\ge0,\qquad G_{\tilde p}\tilde b=r_{\tilde p}.$$

The $\ell^1$ objective is linearized with slack variables, returns $\tilde b=b$ when the
update is already nonnegative, and penalizes large weights (§3.2). Two-sided bounds
$\alpha\le\cdot\le\beta$ replace the positivity constraint in the same way (Eq. (2.6)).

**Convex adaptation** (§3.2, LP (3.2)): $\tilde b=\sum_k\omega_kb^{(k)}$ with
$\omega_k\in[0,1]$, $\sum_k\omega_k=1$ (page-local), a convex combination of known weight
vectors $b^{(k)}$ sharing $A$, such as embedded methods, or the forward Euler
$(1,0,\dots,0)$ for explicit and a backward Euler weight vector for implicit bases. No order
conditions are imposed; the adapted method has the lowest order among its components.

**Active set** (§3.3, Eq. (3.3)). Positivity is imposed only on the components that are
negative, $\mathcal H_0=\{i:y^{n+1}_i<0\}$, enlarged by the components that become negative
after adaptation, until all are nonnegative (page-local $\mathcal H$). In the authors'
examples this took at most two iterations.

**Algorithm** (§3.4, Algorithm 1). Compute the stages and $y_{n+1}$; if it is nonnegative,
proceed to the error estimate. Otherwise solve the LP for $\tilde p=p_{\mathrm{start}}$,
decreasing $\tilde p$ down to $p_{\min}$ until it is feasible and the weight perturbation
$\delta=\lVert h\mathsf F_n(\tilde b-b)\rVert$ is below a tolerance; if no order succeeds,
reduce $h$ and repeat. Then estimate the local error by
$E_T+\delta$ (page-local $E_T$, the usual embedded estimate) and accept or reject as in
[step-size control](/methods/step-size-control.md) (§4.2, Eqs. (4.1)–(4.2)).

## Degrees of freedom

Feasibility needs $\operatorname{rank}G_{\tilde p}<s$; since the quadrature conditions
alone give $\operatorname{rank}G_{\tilde p}\ge\tilde p$, the reduced order must satisfy
$\tilde p<s$ (§3.1, §4.1). Tables 1–2 list the free directions $s-\operatorname{rank}G_{\tilde p}$
(entries for $\tilde p=1,2,\dots$):

| base method | free directions |
|---|---|
| classical RK4 | 3, 2, 0, 0 |
| SSPRK(10,4) | 9, 8, 6, 4 |
| Cash–Karp 5(4) | 5, 4, 2, 1, 0 |
| Dormand–Prince 5(4) | 6, 5, 3, 1, 0 |
| backward Euler | 0 |
| Lobatto IIIC4 | 3, 2, 1, 0, … |
| Radau IIA3 | 2, 1, 0, … |
| SDIRK(5,4) | 4, 3, 1, 0 |
| TR-BDF2 | 2, 1 |
| backward-Euler extrapolation of orders 2, 3, 4 ($s=3,6,10$) | 2, 1 / 5, 4, 2 / 9, 8, 6, 3 |

Fully implicit methods therefore need a drastic order reduction, SDIRK(5,4) one order, and
TR-BDF2 and the [backward-Euler extrapolation methods](/methods/extrapolation-methods.md)
allow adaptation at full order. For a DIRK whose first stage is a scaled backward Euler
step, $\tilde p=1$ is always feasible because backward Euler is unconditionally positive;
for explicit bases $\tilde p=1$ is feasible only for small enough $h$ (§4.1). Among the
explicit bases only the many-stage
[SSP method](/methods/strong-stability-preserving-runge-kutta.md) SSPRK(10,4) keeps free
directions (four) at full order.

## Stability

The [stability function](/definitions/stability-function.md)
$R_{\tilde b}(z)=1+z\tilde b^\top(I-zA)^{-1}\mathbf 1$ is affine in the weights (§4.3,
Eq. (4.3)), which gives two results.

- **Theorem 4.1 (convex adaptation).** If $\tilde b=\sum_k\omega_kb^{(k)}$ is a convex
  combination, the stability region of $(A,\tilde b)$ contains the intersection of the
  regions of the $(A,b^{(k)})$, since $\lvert R_{\tilde b}\rvert\le\sum_k\omega_k\lvert R_{b^{(k)}}\rvert$.
  Convex adaptation of [A-stable](/properties/a-stability.md) components is A-stable.
- **Lemma 4.2 (free adaptation).**
  $\lvert R_{\tilde b}(z)\rvert\le\lvert R_b(z)\rvert+\lVert\tilde b-b\rVert_1\,\lVert z(I-zA)^{-1}\mathbf 1\rVert_\infty$,
  which justifies minimizing $\lVert\tilde b-b\rVert_1$ as a control of the change of the
  stability region; for explicit methods the second factor is bounded by a polynomial in
  $\lvert z\rvert$.

Because the method changes from step to step, no convergence or stability proof for the
whole sequence is given; the authors call it "very challenging" (§4.2).

## Results

- **Explicit bases** (§2.2, §5.1). Cash–Karp 5(4) at $h=0.005$ on the four-species
  Kopecz–Meister reaction system first produces a negative component at $t=1.905$ and then
  diverges; with weights adapted at fourth order the solution stays positive and
  qualitatively correct, with adaptation active only for $1.905\le t\le2.63$ (Fig. 1). On an
  upwind advection–decay problem with Dormand–Prince 5(4) adaptation is needed for
  $h>0.0082$ and the base method is unstable for $h>0.016$, so it acts in a narrow window
  only (Figs. 4–5); for such cheap explicit problems a smaller step is "generally more
  efficient" (§5.1, no timings printed).
- **Implicit and extrapolation bases** (§5.2–5.4). On a heat equation with a discrete delta
  as initial data, third-order backward-Euler extrapolation with free adaptation stays third
  order and positive but shows a nonphysical dip after the first step; convex adaptation
  with a first-order embedded method gives a physical solution at first order in the adapted
  step (Figs. 6–7). On an advection–diffusion–production–destruction problem with PI control,
  72 of 264 steps were adapted, all still at third order, with perturbation $\delta$ of the
  size of the truncation estimate and mass conserved to roundoff (Figs. 8–9). On the
  [stratospheric reaction problem](/benchmarks/stratospheric-reaction-problem.md), 249 steps
  with two rejections; 25 steps had negative values, the smallest being
  $-1.59\times10^{-11}$, and both linear invariants were kept to roundoff (§5.4, Figs.
  10–11).
- **Recommendation** (§6). The approach pays off mainly with diagonally implicit and
  extrapolation bases, where the LP is cheap against the stage solves and the step is not
  stability-limited.

## Qualifications

- **A different "unconditional".** Positivity here is per problem and per step, by a
  method that changes every step; it is not unconditional positivity of a fixed scheme as for
  [modified Patankar methods](/methods/modified-patankar-methods.md), and it does not
  contradict the Bolley–Crouzeix barrier recalled on
  [positivity preservation](/properties/positivity-preservation.md) (§1).
- **Asymptotic order** is empirical: as $h\to0$ with a positive exact solution adaptation
  eventually stops and the base order is observed, but this is not proved (§4.2).
- **Stages may be negative.** With explicit bases the right-hand side is evaluated at
  possibly negative stage values; the authors suggest `sqrt(max(u,0))`-type guards. On
  problems whose solution is positive but which violate the sufficient condition
  $y_i=0\Rightarrow f_i\ge0$, tests "did not show promising results" (§5).
- **Related ideas.** Relaxation Runge–Kutta methods also modify the weights at the end of a
  step, by a scalar, to conserve or dissipate a functional
  ([relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md); Nüßlein et al. 2021, §2).
  The weight-space objective is claimed "computationally much more efficient" than the
  solution-space projections of Sandu and Shampine for large systems (§2.1), not timed.
- **Printed slips** *(compiler checks of the PDF, pp. 4–7)*. In the SSP(3,3) example
  (Eq. (2.13)) the update is printed as $(-\tfrac19,\tfrac{10}9)^\top+\alpha(5,-5)^\top$,
  dropping the factor $h=\tfrac13$; the correct perturbation is $\tfrac{5\alpha}3(1,-1)^\top$,
  so the admissible parameter interval would be $[\tfrac1{15},\tfrac23]$ rather than the
  printed $[\tfrac1{45},\tfrac29]$, which matches the printed (2.13). §3.1 deduces
  "$\tilde p\le s$" where the argument gives $\tilde p<s$, as §4.1 and §6 state. Eq. (3.3)
  sums from $j=0$ with the original weights $b_j$ where $j\ge1$ and $\tilde b_j$ are meant.

# Citations

- [Nüßlein et al. (2021)](/sources/nusslein-2021.md) — §1, §2 (Eqs. (2.1)–(2.7), (2.13)), §2.2 (Fig. 1), §3 (LPs (3.1)–(3.2), Eq. (3.3), Algorithm 1), §4.1 (Tables 1–2), §4.2 (Eqs. (4.1)–(4.2)), §4.3 (Thm. 4.1, Lemma 4.2), §5.1–5.4 (Figs. 4–11), §6; arXiv v2.
