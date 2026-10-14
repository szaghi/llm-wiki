---
type: Definition
title: "Classification of second-order linear PDEs"
description: "A second-order linear PDE in two variables is hyperbolic, parabolic or elliptic as the discriminant of its principal part is positive, zero or negative; the type can change across the plane, a change of variables preserves it, and it fixes the number of real characteristic families."
status: established
aliases: [hyperbolic equation, parabolic equation, elliptic equation, equation type]
tags: [classification, second-order, characteristics]
timestamp: 2026-10-13T00:00:00Z
---

# Classification of second-order linear PDEs

The general second-order linear PDE in two independent variables is
$$a_{11}\,\partial_x^2 u + 2a_{12}\,\partial_x\partial_y u + a_{22}\,\partial_y^2 u + b_1\,\partial_x u + b_2\,\partial_y u + c_0 u = \psi(x,y),$$
with coefficients given functions of $(x,y)$
([Riley et al. (2006)](/sources/riley-2006.md), eq. 20.19, p. 687). With
the discriminant $D = a_{12}^2 - a_{11}a_{22}$ the equation is

* **hyperbolic** if $D > 0$,
* **parabolic** if $D = 0$,
* **elliptic** if $D < 0$

(§20.3.3, p. 687; the book writes the mixed coefficient without the factor
2, so its criterion $B^2 \gtrless 4AC$ is $4D \gtrless 0$). Only the
principal (second-order) part enters. When the coefficients depend on
$(x,y)$ the equation can be of different types in different parts of the
plane (p. 687).

## Model equations

* The [wave equation](/definitions/wave-equation.md)
  $\partial_x^2 u - c^{-2}\partial_t^2 u = 0$ has $a_{11} = 1$,
  $a_{12} = 0$, $a_{22} = -1/c^2$, so $D = 1/c^2 > 0$: hyperbolic (p. 704).
* The [diffusion equation](/definitions/diffusion-equation.md)
  $\kappa\,\partial_x^2 u - \partial_t u = 0$ has $a_{12} = a_{22} = 0$:
  parabolic.
* The [Laplace equation](/definitions/laplace-and-poisson-equations.md)
  $\partial_x^2 u + \partial_y^2 u = 0$ has $D = -1$: elliptic (p. 706).

## What the type decides

* **Characteristics.** The characteristic directions solve
  $a_{11}(\mathrm dy/\mathrm dx)^2 - 2a_{12}\,\mathrm dy/\mathrm dx + a_{22} = 0$,
  i.e. $\mathrm dy/\mathrm dx = (a_{12} \pm \sqrt D)/a_{11}$ for
  $a_{11} \ne 0$: two real families when hyperbolic, one when parabolic,
  two complex families when elliptic (eqs. 20.44–20.45, p. 703). See
  [characteristic curves](/definitions/characteristic-curve.md).
* **Form of the general solution** of a constant-coefficient equation
  without lower-order terms: real, repeated or complex characteristic
  coordinates ([general solution of constant-coefficient second-order
  equations](/methods/constant-coefficient-second-order-general-solution.md)).
* **Which boundary data are appropriate**: Cauchy data on an open boundary
  (hyperbolic), Dirichlet or Neumann data on an open (parabolic) or closed
  (elliptic) boundary ([boundary data by equation type](/results/boundary-data-by-equation-type.md)).

## Invariance under a change of variables

Under a change of independent variables $\xi = \xi(x,y)$,
$\eta = \eta(x,y)$ the transformed coefficients satisfy
$$D' = D\left[\frac{\partial(\xi,\eta)}{\partial(x,y)}\right]^2,$$
so a non-singular change of variables cannot change the type
(Exercise 20.24, p. 710). The book poses this as an exercise ("the algebra
is somewhat lengthy, but straightforward"), with no worked proof in the
text.

## Scope

The book classifies only equations in two independent variables; it gives
no classification for more variables or for first-order systems, and no
definition of a hyperbolic system. Those wait for their sources.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.3.3 (p. 687), §20.6.2
  (pp. 701–705), Exercise 20.24 (p. 710).
