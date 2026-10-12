---
type: Method
title: "Explicit Runge–Kutta methods"
description: "One-step methods that combine several evaluations of the semi-discrete operator within a step, written in Butcher form; origin in Runge (1895), order by Taylor matching, stability function, embedded pairs, and the methods that change the weights after the stages are known (relaxation, positivity adaptation)."
status: established
aliases: [Runge-Kutta, RK, Butcher tableau, classical Runge-Kutta, embedded Runge-Kutta pair]
tags: [time-discretization, method-of-lines, runge-kutta]
timestamp: 2026-10-12T00:00:00Z
---

# Explicit Runge–Kutta methods

For the semi-discretization $\frac{d}{dt}u = \mathcal L(u)$, an explicit
$s$-stage Runge–Kutta method in **Butcher form** computes
$$Y_i = u^n + \Delta t\sum_{j<i}\mathsf a_{ij}\,\mathcal L(Y_j),\quad i = 1,\dots,s,\qquad u^{n+1} = u^n + \Delta t\sum_{j=1}^{s}\mathsf b_j\,\mathcal L(Y_j),$$
with $Y_1 = u^n$ and stage times $t^n + \mathsf c_i\Delta t$. Order
$p_{\mathrm t}$ means agreement with the Taylor series of the exact
solution through $\Delta t^{p_{\mathrm t}}$ per step. The
[Shu–Osher form](/methods/ssp-runge-kutta.md) is a rewriting of the same
methods as convex combinations of forward-Euler steps; the SSP property
belongs to the method, not to one rewriting of it
([Higueras & Roldán (2019)](/sources/higueras-2019.md), §2, Defs. 1–2).

## Origin: Runge (1895)

Runge generalizes Simpson's rule from quadrature to $u' = \mathcal L(t, u)$
([Runge (1895)](/sources/runge-1895.md), pp. 167–170):
* the "tangent trapezoid", today's **midpoint method**,
  $u^{n+1} = u^n + \Delta t\,\mathcal L\!\left(t^n + \tfrac12\Delta t,\ u^n + \tfrac12\Delta t\,\mathcal L(t^n, u^n)\right)$ (eq. 2);
* the "chord trapezoid", today's **Heun (trapezoidal) method**, the
  second-order SSP method on the [SSP page](/methods/ssp-runge-kutta.md) (eq. 3);
* both match the Taylor series through $\Delta t^2$. Their Simpson-type
  combination, (2) plus one third of (3) − (2), is third order only when
  $\mathcal L$ does not depend on $u$. Runge repairs this with a modified
  chord step, giving a **third-order method with four evaluations** of
  $\mathcal L$ (eqs. 3a, 4). His proof is term-by-term matching of the
  Taylor expansion, for single equations and for two-equation systems.

The paper has no fourth-order method, no general $s$-stage form, no order
conditions and no stability analysis. The error is estimated from the
agreement of the two second-order variants and by halving the step; the
independent variable is switched to whichever coordinate changes faster
(pp. 172–178). These are the precursors of embedded error estimation and
step control, without an automatic rule.

## Stability function and the classical methods

For the test equation $u' = \lambda u$, with $z = \Delta t\lambda$, one step
multiplies by the **stability function**
$R_{\mathrm{st}}(z) = 1 + z\,\mathsf b^{\mathsf T}(\mathsf I - z\mathsf A)^{-1}\mathbf 1$,
a polynomial of degree $s$ for an explicit method
([Nüßlein, Ranocha & Ketcheson (2021)](/sources/nusslein-2021.md), eq. 4.3).
Linear stability does not imply a monotone or positive solution: SSP(3,3)
at $\Delta t = 1/3$ on a linear positive two-component system, inside its
linear stability interval, returns a negative component (§2.1, eqs. 2.8–2.11).
The classical four-stage fourth-order method (RK4) is not SSP and is used
throughout the corpus with WENO; see the batch-5 notes on the
[SSP page](/methods/ssp-runge-kutta.md).

## Embedded pairs

A **pair** adds weights $\hat{\mathsf b}$ of a lower order
$\hat p_{\mathrm t}$ on the same stages; the difference of the two updates
estimates the local error ([Ranocha et al. (2022)](/sources/ranocha-2022.md), §2, eqs. 2–4).
In a FSAL ("first same as last") pair the embedded method also uses
$\mathcal L(u^{n+1})$, which the next step needs anyway. Names give the main order, the embedded order in parentheses, then the
effective number of operator evaluations per step (one less than the
stage count for a FSAL pair), with a trailing F for FSAL: BS3(2)3F,
BS5(4)7F, DP5(4)6F. The estimate drives
[step-size control](/methods/runge-kutta-step-size-control.md).

## Methods that change the weights after the stages

Since $u^{n+1}$ is linear in $\mathsf b$ once the stages are known, two
lines of work re-choose the weights at the end of each step. Both keep all
linear invariants, because every modified step is still a Runge–Kutta
step:
* [relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md) scales
  all weights by one scalar $\gamma^n_{\mathrm R}$ so that a convex
  functional (an entropy) changes by exactly the right amount
  ([Ranocha et al. (2020)](/sources/ranocha-2020.md));
* [positivity-preserving adaptive Runge–Kutta](/methods/positivity-preserving-adaptive-runge-kutta.md)
  solves a linear program for new weights $\tilde{\mathsf b}$ that make
  $u^{n+1} \ge 0$ while satisfying the order conditions up to some
  order ([Nüßlein, Ranocha & Ketcheson (2021)](/sources/nusslein-2021.md)).

Storage-saving implementations are on
[low-storage Runge–Kutta](/methods/low-storage-runge-kutta.md).

# Citations

1. [Runge (1895)](/sources/runge-1895.md), pp. 167–178.
2. [Higueras & Roldán (2019)](/sources/higueras-2019.md), §2.
3. [Nüßlein, Ranocha & Ketcheson (2021)](/sources/nusslein-2021.md), §§2, 4.3.
4. [Ranocha et al. (2022)](/sources/ranocha-2022.md), §2.
5. [Ranocha et al. (2020)](/sources/ranocha-2020.md), §2.
