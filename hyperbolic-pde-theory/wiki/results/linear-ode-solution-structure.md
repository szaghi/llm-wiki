---
type: Result
title: "Structure of linear ODE solutions"
description: "The general solution of an nth-order linear ODE is the complementary function, a superposition of n linearly independent homogeneous solutions with n arbitrary constants, plus any particular integral; with constant coefficients the homogeneous solutions come from the roots of the auxiliary polynomial (x^k e^{nu x} for a repeated root), and Euler, Legendre and canonical-form substitutions reduce some variable-coefficient cases."
status: established
aliases: [complementary function, particular integral, auxiliary equation, Euler equation, reduction of order, undetermined coefficients]
tags: [ode, linearity, superposition]
timestamp: 2026-10-13T00:00:00Z
---

# Structure of linear ODE solutions

**Statement.** For
$$a_n(x)y^{(n)} + a_{n-1}(x)y^{(n-1)} + \dots + a_1(x)y' + a_0(x)y = \psi(x)$$
(homogeneous iff $\psi = 0$), the general solution is
$$y = y_c + y_p, \qquad y_c = c_1y_1 + \dots + c_ny_n,$$
where $y_1, \dots, y_n$ are linearly independent solutions of the
homogeneous equation and $y_p$ is any solution of the full equation
([Riley et al. (2006)](/sources/riley-2006.md), eqs. 15.1–15.7,
pp. 490–492). Independence is tested with the
[Wronskian](/definitions/wronskian.md). Any $y_p$ is "equally valid, no
matter how simple (or complicated)" (p. 492). The superposition argument
"assumes crucially that the ODE is linear" (p. 492).

**Status.** That the general solution of an $n$th-order ODE has $n$
arbitrary constants is assumed: "a totally general proof is difficult"
(§14.1, p. 470). No existence theorem is given.

## Constant coefficients

Trying $y = e^{\nu x}$ in the homogeneous equation gives the auxiliary
equation $a_n\nu^n + \dots + a_1\nu + a_0 = 0$ (eq. 15.10, p. 492), with
roots $\nu_j$:

* distinct real roots: $y_c = \sum_jc_je^{\nu_jx}$ (eq. 15.11);
* a complex pair $\Re\nu \pm i\,\Im\nu$ (real coefficients):
  $e^{\Re\nu\,x}(c_1\cos(\Im\nu\,x) + c_2\sin(\Im\nu\,x))$ (eq. 15.12);
* a $k$-fold root $\nu$: $(c_1 + c_2x + \dots + c_kx^{k-1})e^{\nu x}$
  (eqs. 15.13–15.14, pp. 493).

**Particular integrals by undetermined coefficients:** for a forcing that
is exponential, sinusoidal, polynomial, or a sum or product of these, try
the same form with unknown coefficients. If a term of the trial function
lies in $y_c$, multiply by the lowest power of $x$ that removes the overlap
(pp. 494–496). Otherwise use [variation of
parameters](/methods/variation-of-parameters.md), [Green's
functions](/methods/greens-functions-for-linear-odes.md) or the [Laplace
transform](/methods/integral-transform-methods.md) (pp. 495, 501).

## Variable coefficients (special cases)

* **Euler and Legendre linear equations**, with coefficients
  $\propto (c_1x + c_2)^k$ on $y^{(k)}$: the substitution
  $c_1x + c_2 = e^t$ gives constant coefficients. For the homogeneous Euler
  equation try $y = x^\nu$, and a $k$-fold root gives
  $x^\nu, x^\nu\ln x, \dots, x^\nu(\ln x)^{k-1}$ (eqs. 15.36–15.38,
  pp. 503–505). The radial equations of [separation in polar
  coordinates](/methods/separation-of-variables.md) are of this type.
* **Exact equations:** the left-hand side is a derivative iff
  $a_0 - a_1' + a_2'' - \dots + (-1)^na_n^{(n)} = 0$, and one integration
  lowers the order (eq. 15.43, p. 505).
* **Reduction of order:** with one homogeneous solution $y_1$ known,
  $y = y_1v$ gives an equation of order $n - 1$ in $v'$. For second order
  this yields both the second solution and a particular integral
  (§15.2.3, pp. 506–507).
* **Canonical form:** for $y'' + a_1y' + a_0y = \psi$,
  $y = v\exp(-\tfrac12\int a_1\,\mathrm dx)$ removes the first-derivative
  term, leaving $v'' + (a_0 - \tfrac14a_1^2 - \tfrac12a_1')v = \psi\exp(\tfrac12\int a_1\,\mathrm dx)$
  (eqs. 15.70–15.73, pp. 516–517).

**Discrete analogue.** Linear recurrence relations with constant
coefficients have the same complementary-plus-particular structure and a
characteristic polynomial (§15.1.4, pp. 496–501). This bundle does not
compile them further (discrete theory is out of scope).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §14.1 (p. 470), §15
  introduction and §15.1–15.2 (pp. 490–517).
