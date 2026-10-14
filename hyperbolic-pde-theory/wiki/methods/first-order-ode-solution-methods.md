---
type: Method
title: "Solution methods for first-order ODEs"
description: "Closed-form methods for first-order ODEs of the kind the characteristic equations of first-order PDEs produce: separation of variables, exact equations and integrating factors (in particular exp of the integral of the coefficient for linear equations), homogeneous and isobaric substitutions, Bernoulli's equation, and for higher degree the factorisation and Clairaut forms with their singular solutions."
status: established
aliases: [integrating factor, separable ODE, exact ODE, Bernoulli equation, Clairaut equation, singular solution]
tags: [ode, first-order, characteristics]
timestamp: 2026-10-13T00:00:00Z
---

# Solution methods for first-order ODEs

A first-degree first-order ODE has the form $y' = F(x,y)$, or equivalently
$M(x,y)\,\mathrm dx + N(x,y)\,\mathrm dy = 0$
([Riley et al. (2006)](/sources/riley-2006.md), §14.2, p. 470). The
characteristic equations $\mathrm dx/b_1 = \mathrm dy/b_2$ of a
[first-order linear PDE](/methods/first-order-linear-pde-characteristics.md)
are of this kind. The book integrates them by separation, and the
one-variable case by an integrating factor (§20.3.1, pp. 682–684).

## First degree

* **Separable**, $y' = X(x)Y(y)$: $\int\mathrm dy/Y = \int X\,\mathrm dx$
  (eq. 14.3, p. 471).
* **Exact**, $\partial_yM = \partial_xN$: then $M\,\mathrm dx + N\,\mathrm dy = \mathrm dU$
  and the solution is $U(x,y) = \text{const}$, with
  $U = \int M\,\mathrm dx + F(y)$ and $F$ fixed by $\partial_yU = N$
  (eqs. 14.4–14.8, p. 472).
* **Integrating factor.** If inexact, a factor $\mu$ with
  $\partial_y(\mu M) = \partial_x(\mu N)$ always exists, but there is no
  general way to find it. It depends on $x$ alone iff
  $(\partial_yM - \partial_xN)/N$ does, and then
  $\mu = \exp\int(\partial_yM - \partial_xN)/N\,\mathrm dx$; similarly for
  $y$ alone (eqs. 14.9–14.12, p. 473).
* **Linear**, $y' + a_0(x)y = \psi(x)$: always solvable, with
  $$\mu(x) = \exp\int a_0(x)\,\mathrm dx, \qquad \mu y = \int\mu\psi\,\mathrm dx$$
  (eqs. 14.14–14.17, pp. 474–475).
* **Homogeneous**, $y' = F(y/x)$, with numerator and denominator
  homogeneous of the same degree: $y = vx$ makes it separable (eqs.
  14.18–14.19, pp. 475–476). **Isobaric** equations, where $y$ carries a
  weight relative to $x$, use $y = vx^{\text{weight}}$ (p. 476).
* **Bernoulli**, $y' + a_0y = \psi y^\gamma$, $\gamma \ne 0, 1$:
  $v = y^{1-\gamma}$ gives a linear equation (eq. 14.21, p. 477).
* $y' = F(c_1x + c_2y + c_3)$ is separable in $v = c_1x + c_2y + c_3$. A
  ratio of linear functions is made homogeneous by shifting the origin to
  the intersection of the two lines (eqs. 14.22–14.26, pp. 478–480).

## Higher degree

For $F(x,y,y') = 0$ polynomial in $y'$ (eq. 14.27): factorise into
first-degree equations and multiply their solutions (eqs. 14.28–14.29).
Otherwise solve for $x$ or $y$ and differentiate (§14.3.2–14.3.3).
**Clairaut's equation** $y = xy' + F(y')$ has the general solution
$y = c_1x + F(c_1)$, and a **singular solution**, with no arbitrary
constant and not obtainable from the general one, from $F'(y') + x = 0$
(eqs. 14.39–14.43, pp. 483–484). Higher-degree equations "do not occur
often in the description of physical systems" (p. 480).

## Scope

The book's general framing is that an $n$th-order ODE has $n$ arbitrary
constants. The book assumes this, saying that "a totally general proof is
difficult" (§14.1, p. 470). There is no existence or uniqueness theorem
for initial-value problems (e.g. a Lipschitz condition) in the chapters
read. Uniqueness along characteristics therefore rests on nothing stated
here.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §14.1–14.3 (pp. 468–484),
  §20.3.1 (pp. 682–684).
