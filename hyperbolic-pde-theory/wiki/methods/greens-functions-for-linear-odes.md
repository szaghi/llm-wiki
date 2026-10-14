---
type: Method
title: "Green's functions for linear ODEs"
description: "The solution of an nth-order linear ODE L y = psi with homogeneous boundary conditions is the integral of G(x, x') psi(x') where L G = delta(x - x'), G obeys the boundary conditions in x, its first n-2 derivatives are continuous at x = x' and the (n-1)th jumps by 1/a_n(x'); G depends on the boundary conditions, and one-point conditions give a causal kernel."
status: established
aliases: [ODE Green's function, impulse response, jump conditions]
tags: [greens-function, ode, boundary-conditions]
timestamp: 2026-10-13T00:00:00Z
---

# Green's functions for linear ODEs

For $\mathcal Ly \equiv a_n(x)y^{(n)} + \dots + a_1(x)y' + a_0(x)y = \psi(x)$
on $x_a \le x \le x_b$, suppose
$$y(x) = \int_{x_a}^{x_b} G(x,x')\,\psi(x')\,\mathrm dx'$$
for every $\psi$ ([Riley et al. (2006)](/sources/riley-2006.md), eqs.
15.58–15.60, p. 511). Applying $\mathcal L$ and comparing with the sifting
property of $\delta$ gives $\mathcal LG(x,x') = \delta(x - x')$ (eq. 15.62,
p. 511). $G$ is the response to a unit impulse at $x = x'$ (p. 512).

**Defining properties** (p. 512–513):

1. $\mathcal LG = \delta(x - x')$.
2. As a function of $x$, $G$ obeys the specified homogeneous boundary
   conditions on $y$.
3. $\partial_x^kG$ for $k \le n - 2$ is continuous at $x = x'$, and
   $\partial_x^{n-1}G$ jumps by $1/a_n(x')$ (eqs. 15.63–15.65,
   integrating across $x'$).

**Construction.** On each side of $x'$, $G$ is a combination of
complementary-function solutions with coefficients depending on $x'$.
Properties 2 and 3 fix these coefficients (p. 513).

## Worked cases

* $y'' + y = \psi$, $y(0) = y(\pi/2) = 0$: $G = -\cos x'\sin x$ for
  $x < x'$, $-\sin x'\cos x$ for $x > x'$. So
  $y = -\cos x\int_0^x\sin x'\,\psi\,\mathrm dx' - \sin x\int_x^{\pi/2}\cos x'\,\psi\,\mathrm dx'$
  (eqs. 15.66–15.68, pp. 513–514).
* Same operator, one-point conditions $y(0) = y'(0) = 0$:
  $G = H(x - x')\sin(x - x')$, so $y = \int_0^x\sin(x - x')\psi(x')\,\mathrm dx'$.
  Only the past of $\psi$ contributes (p. 515).

The two cases show that "a particular $G(x,x')$ applies to a given LHS of
an ODE and the imposed boundary conditions" (p. 514). Dropping the constant
limits of integration gives a particular integral (p. 514).
Inhomogeneous conditions are first removed by $v = y - y_b(x)$, with $y_b$ a
polynomial of degree $n - 1$ satisfying them (pp. 515–516; [homogeneous
linear problems](/definitions/homogeneous-linear-problem.md)). For a
second-order two-point problem, $G$ is a product of solutions divided by
their [Wronskian](/definitions/wronskian.md) (Exercise 15.27, p. 527, set
as an exercise).

## Relations

The construction parallels [variation of
parameters](/methods/variation-of-parameters.md): both replace the
constants of the complementary function by functions (p. 513). Both need
the whole complementary function (p. 511). The eigenfunction approach is
deferred to Ch. 17 (not read). The PDE extension is [Green's functions for
linear PDEs](/methods/greens-functions-for-pdes.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §15.2.5 (pp. 511–516),
  Exercise 15.27 (p. 527).
