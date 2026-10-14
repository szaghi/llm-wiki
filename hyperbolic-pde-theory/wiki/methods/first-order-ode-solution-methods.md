---
type: Method
title: "Solution methods for first-order ODEs"
description: "Closed-form methods for first-order ODEs of the kind the characteristic equations of first-order PDEs produce: separation of variables, exact equations and integrating factors (in particular exp of the integral of the coefficient for linear equations), homogeneous and isobaric substitutions, Bernoulli and Riccati equations, and for higher degree the factorisation and Clairaut forms with their singular solutions."
status: established
aliases: [integrating factor, separable ODE, exact ODE, Bernoulli equation, Riccati equation, Clairaut equation, singular solution]
tags: [ode, first-order, characteristics]
timestamp: 2026-10-14T00:00:00Z
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

[Arfken et al. (2013)](/sources/arfken-2013.md) cover the same first-degree
methods (§7.2, pp. 331–339): separable equations, exact equations with the
criterion $\partial_yM = \partial_xN$ and the solution as a line integral
(eqs. 7.6–7.10), equations homogeneous in $x$ and $y$, isobaric equations,
and the linear equation with $\mu = \exp\int a_0\,\mathrm dx$ (eqs.
7.11–7.17). They agree that an integrating factor always exists but that a
systematic construction "is known only when a first-order ODE is linear"
(p. 334). They add that every separable equation is exact, but not
conversely (p. 333), and two theorems for the linear equation: its
solution is unique up to an added multiple of the homogeneous solution, and
the homogeneous equation has only one linearly independent solution
(p. 337). Bernoulli's equation is linearised by the same substitution
(eqs. 7.101–7.102, p. 378).

**Riccati's equation** (Arfken et al., eqs. 7.103–7.104, p. 378),
$y' = \chi_2(x)y^2 + \chi_1(x)y + \chi_0(x)$ with $\chi_2, \chi_0 \ne 0$,
has no general method. If one solution $y_1$ is known, $y = y_1 + v$ turns
it into the Bernoulli equation $v' = \chi_2v^2 + (2\chi_2y_1 + \chi_1)v$.

**Nonlinear equations: movable singularities** (Arfken et al., §7.8,
pp. 378–379). The solutions of a nonlinear ODE can have singularities whose
position depends on the data. $y' = y^2$ with $y(0) = 1$ and $y(0) = 2$
blows up at $x = 1$ and $x = 1/2$; the linear equation
$y' + y/(x - 1) = 0$ is singular at $x = 1$ whatever the data. A nonlinear
equation may also have special solutions outside its general solution
(Example 7.8.2). For characteristic equations this means a solution
carried along a characteristic can cease to exist at a finite distance
fixed by the data (compiler's remark; neither book draws the conclusion).

## Higher degree

For $F(x,y,y') = 0$ polynomial in $y'$ (eq. 14.27): factorise into
first-degree equations and multiply their solutions (eqs. 14.28–14.29).
Otherwise solve for $x$ or $y$ and differentiate (§14.3.2–14.3.3).
**Clairaut's equation** $y = xy' + F(y')$ has the general solution
$y = c_1x + F(c_1)$, and a **singular solution**, with no arbitrary
constant and not obtainable from the general one, from $F'(y') + x = 0$
(eqs. 14.39–14.43, pp. 483–484). Arfken et al. set the same equation as an
exercise and note that "the singular solution is the envelope of the
general solutions" (Exercise 7.8.4, pp. 379–380). Higher-degree equations "do not occur
often in the description of physical systems" (p. 480).

## Scope

The book's general framing is that an $n$th-order ODE has $n$ arbitrary
constants. The book assumes this, saying that "a totally general proof is
difficult" (§14.1, p. 470). There is no existence or uniqueness theorem
for initial-value problems (e.g. a Lipschitz condition) in the chapters
read. Uniqueness along characteristics therefore rests on nothing stated
here. Arfken et al. do not change this for nonlinear first-order equations:
"there is no systematic way to solve the most general first-order ODE"
(p. 331), and their only uniqueness statements concern linear equations
(p. 337; Exercise 7.5.1).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §14.1–14.3 (pp. 468–484),
  §20.3.1 (pp. 682–684).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §7.2 (pp. 331–339),
  §7.8 (pp. 377–380).
