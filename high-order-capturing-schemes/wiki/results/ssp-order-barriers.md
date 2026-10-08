---
type: Result
title: "Order barriers and optimal coefficients of SSP time discretizations"
description: "What strong-stability-preserving Runge–Kutta and multistep methods can and cannot reach: SSP coefficient at most 1 for m-stage order-m methods, no four-stage fourth-order method without the downwind operator, multistep step-count barriers, and no implicit SSP method above first order."
status: established
aliases: [SSP barriers, SSP order barrier, optimal SSP methods]
tags: [time-discretization, ssp, impossibility]
timestamp: 2026-10-08T00:00:00Z
---

# Order barriers and optimal coefficients of SSP time discretizations

The setting is the [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)
framework: forward Euler is strongly stable in some norm or convex
functional for $\Delta t \le \Delta t_{\mathrm{FE}}$, and a higher-order
method in Shu–Osher form inherits the property for
$\Delta t \le \mathcal{C}\,\Delta t_{\mathrm{FE}}$ with
$\mathcal{C} = \min a_{ik}/\vert b_{ik}\vert$ (using $\tilde{\mathcal{L}}$
where $b_{ik} < 0$). "SSP" replaces the earlier name "TVD time
discretization", because nothing in the argument is specific to total
variation ([Gottlieb, Shu & Tadmor (2001)](/sources/gottlieb-2001.md), §1).
The results below are all from Gottlieb, Shu & Tadmor unless stated.

## Runge–Kutta

* **$\mathcal{C} \le 1$ for $m$ stages and order $m$** (Proposition 3.1):
  with nonnegative coefficients, no $m$-stage method of order $m$ beats
  forward Euler's step, already for linear $\mathcal{L}$. Dropping the
  order requirement lifts the bound: an $m$-stage first-order method
  reaches $\mathcal{C} = m$ (suitable for steady states).
* **Linear problems, any order** (Proposition 3.2): for linear
  $\mathcal{L}$ the unique $m$-stage order-$m$ method is SSP with
  $\mathcal{C} = 1$. It is built as $m-1$ forward-Euler stages followed by
  $$u^{(m)} = \sum_{k=0}^{m-2} a_{m,k}\,u^{(k)} + a_{m,m-1}\left(u^{(m-1)} + \Delta t\,\mathcal{L}u^{(m-1)}\right),$$
  with $a_{m,k} = a_{m-1,k-1}/k$, $a_{m,m-1} = 1/m!$,
  $a_{m,0} = 1 - \sum_{k\ge1} a_{m,k}$, all nonnegative. Examples are the
  convex decompositions
  $\sum_{k=0}^{3}\frac{(\Delta t\mathcal{L})^k}{k!} = \frac13 + \frac12(I+\Delta t\mathcal{L}) + \frac16(I+\Delta t\mathcal{L})^3$
  and
  $\sum_{k=0}^{4}\frac{(\Delta t\mathcal{L})^k}{k!} = \frac38 + \frac13(I+\Delta t\mathcal{L}) + \frac14(I+\Delta t\mathcal{L})^2 + \frac1{24}(I+\Delta t\mathcal{L})^4$.
  For nonlinear $\mathcal{L}$ the same schemes stay SSP but lose order $m$.
* **Fourth order needs $\tilde{\mathcal{L}}$** (Proposition 4.2; proved
  in Gottlieb & Shu 1998): every four-stage fourth-order method with
  $\mathcal{C} > 0$ has a negative $b_{ik}$. The best method found has
  $\mathcal{C} = 0.936$ with two $\tilde{\mathcal{L}}$ evaluations, an
  effective $0.936 \times 4/6 = 0.624$; its optimality is not claimed.
  This agrees with [Shu (1998)](/sources/shu-1998.md), §4.2.2, and with
  [Shu & Osher (1988)](/sources/shu-1988.md), whose search for fourth
  order could not avoid negative $b_{ik}$.
* **Low storage**: the best two-register third-order method found has
  $\mathcal{C} = 0.32$; no SSP five-stage fourth-order member of the
  Carpenter–Kennedy low-storage class with positive coefficients was
  found, and a low-storage method with a negative $b_{ik}$ cannot use
  $\tilde{\mathcal{L}}$ and so cannot be made SSP.
* **Two-step two-stage hybrids**: third order reaches $\mathcal{C} \approx 0.473$;
  fourth order with nonnegative coefficients is impossible (Proposition 4.3).

## Multistep

For $u^{n+1} = \sum_{i=1}^{m}\left(a_i u^{n+1-i} + \Delta t\, b_i\,\mathcal{L}(u^{n+1-i})\right)$:

* no $m$-step method of order $m$ ($m \ge 2$) has all $b_i \ge 0$, and no
  $m$-step SSP method has order $m+1$ (Proposition 5.1);
* optimal $\mathcal{C}$: two-step second order $1/2$; three-step second
  order with $b_i \ge 0$, $1/2$; four-step third order with $b_i \ge 0$,
  $1/3$ (Propositions 5.2–5.4). With one evaluation per step these match
  the efficiency of the optimal two- and three-stage Runge–Kutta
  methods, at higher storage;
* more steps help: four-step second order $2/3$; five- and six-step
  third order $1/2$ and $0.567$; four-step fourth order $\approx 0.159$
  ($0.245$ with six steps); five-step fifth order $\approx 0.085$
  ($0.130$ with six steps);
* a five-step fourth-order method with all $b_i \ge 0$ exists
  ($\mathcal{C} = 0.021$), which disproves the belief that SSP order four
  forces negative coefficients — though the coefficient is too small to
  be useful.

## Implicit methods

Backward Euler is unconditionally TVD (Harten's lemma for implicit
schemes), but no implicit Runge–Kutta (Proposition 6.2) or multistep
(Proposition 6.3) method of the form with only implicit $\mathcal{L}$
terms is SSP above first order. A non-SSP second-order implicit
Runge–Kutta method destroys the monotonicity of a first-order upwind
solution at CFL 1.4 (Fig. 6.1).

## Linear coercive operators

For a linear, coercive, Lipschitz-in-time $\mathcal{L}(t)$, forward
Euler is strongly stable iff $\Delta t \le 2\eta$, and classical RK4 is
then stable under the same condition, with growth $\vert u^n\vert \le e^{3K_{\mathrm{L}}t^n}\vert u^0\vert$
for a Lipschitz constant $K_{\mathrm{L}}$ of $\mathcal{L}(t)$ (Proposition 3.3), improving the Levy–Tadmor bound
$\Delta t \le \eta/31$ to $\Delta t \le 2\eta$.

# Citations

1. [Gottlieb, Shu & Tadmor (2001)](/sources/gottlieb-2001.md), §§2–6 (Propositions 3.1–6.3, Table 3.1).
2. [Shu (1998)](/sources/shu-1998.md), §4.2.
3. [Shu & Osher (1988)](/sources/shu-1988.md), §II.
