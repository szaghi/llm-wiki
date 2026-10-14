---
type: Definition
title: "Classification of second-order linear PDEs"
description: "A second-order linear PDE in two variables is hyperbolic, parabolic or elliptic as the discriminant of its principal part is positive, zero or negative; the type can change across the plane, a change of variables preserves it, and it fixes the number of real characteristic families."
status: established
aliases: [hyperbolic equation, parabolic equation, elliptic equation, equation type]
tags: [classification, second-order, characteristics]
timestamp: 2026-10-14T00:00:00Z
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

[Arfken et al. (2013)](/sources/arfken-2013.md) state the same criterion
(§9.3, eqs. 9.17–9.22, pp. 410–411). They write the principal part with the
factor 2, so their discriminant $b^2 - ac$ is exactly $D$. They add that the
classification of an equation with variable coefficients "is only local; the
class may change as the coordinates vary" (p. 411). The two books agree.
The names come from the analogy with quadratic forms: ellipse, hyperbola,
parabola (pp. 410–411).

**Arfken's route: factorisation.** The prototype
$\partial_x^2u - c^2\partial_y^2u$ (with $c$ real) factors into two
commuting first-order operators, $(\partial_x + c\,\partial_y)(\partial_x - c\,\partial_y)u = 0$, each with its own
real characteristics. The elliptic prototype
$\partial_x^2u + c^2\partial_y^2u$ factors only with $\pm ic$, which
gives complex characteristics "which do not have an obvious relevance to
boundary conditions" (eqs. 9.11–9.16, pp. 409–410; Arfken's $a$ is set to 1 here). In general, for
$a_{22} \ne 0$,
$$a_{11}\partial_x^2 + 2a_{12}\partial_x\partial_y + a_{22}\partial_y^2 = \left(\frac{a_{12} + \sqrt D}{a_{22}^{1/2}}\,\partial_x + a_{22}^{1/2}\partial_y\right)\left(\frac{a_{12} - \sqrt D}{a_{22}^{1/2}}\,\partial_x + a_{22}^{1/2}\partial_y\right)$$
(eq. 9.18, p. 410). The characteristics are real if and only if $D \ge 0$:
two independent families for $D > 0$, exactly one for $D = 0$, a complex
conjugate pair for $D < 0$ (p. 410).

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
  [characteristic curves](/definitions/characteristic-curve.md). Arfken et
  al. give the slopes as $\mathrm dy/\mathrm dx = a_{22}/(a_{12} \pm \sqrt D)$
  (eq. 9.22, p. 411). The two forms give the same pair of slopes when
  $a_{11}a_{22} \ne 0$: multiplying numerator and denominator by
  $a_{12} \mp \sqrt D$ turns Arfken's form into Riley's, with the two signs
  exchanged (compiler's check).
* **Form of the general solution** of a constant-coefficient equation
  without lower-order terms: real, repeated or complex characteristic
  coordinates ([general solution of constant-coefficient second-order
  equations](/methods/constant-coefficient-second-order-general-solution.md)).
* **Which boundary data are appropriate**: Cauchy data on an open boundary
  (hyperbolic), Dirichlet or Neumann data on an open (parabolic) or closed
  (elliptic) boundary ([boundary data by equation type](/results/boundary-data-by-equation-type.md)).
  Arfken et al. state the same dependence: "the boundary conditions needed
  to specify (in a consistent way) a unique solution will depend on the
  equation class" (§9.3, p. 412).

## Canonical forms

Arfken et al. reduce a constant-coefficient principal part with
$a_{22} > 0$ to a diagonal form by the non-characteristic change of
variables $\hat\xi = a_{22}^{1/2}x - a_{22}^{-1/2}a_{12}y$,
$\hat\eta = a_{22}^{-1/2}y$:
$$a_{11}\partial_x^2 + 2a_{12}\partial_x\partial_y + a_{22}\partial_y^2 = -D\,\partial_{\hat\xi}^2 + \partial_{\hat\eta}^2$$
(eqs. 9.20–9.21, p. 411; verification set as Exercise 9.3.1; the identity
was re-derived by the compiler). Rescaling $\hat\xi$ then gives the wave
operator for $D > 0$ and the Laplacian for $D < 0$. For $D = 0$ only
$\partial_{\hat\eta}^2$ survives, and the canonical parabolic equation
is taken as $\partial_x u = \text{const}\times\partial_y^2u$, the
[diffusion equation](/definitions/diffusion-equation.md) (eq. 9.19, p. 410).
Without the first-derivative term the parabolic equation is in effect an
ODE in $y$ with $x$ as a parameter (p. 410). This diagonal form differs from
Riley et al.'s reduction to $\partial_\xi\partial_\eta u = 0$ in
characteristic coordinates ([general solution of constant-coefficient
second-order equations](/methods/constant-coefficient-second-order-general-solution.md)).
Both are valid reductions; they use different coordinates.

## Invariance under a change of variables

Under a change of independent variables $\xi = \xi(x,y)$,
$\eta = \eta(x,y)$ the transformed coefficients satisfy
$$D' = D\left[\frac{\partial(\xi,\eta)}{\partial(x,y)}\right]^2,$$
so a non-singular change of variables cannot change the type
(Exercise 20.24, p. 710). The book poses this as an exercise ("the algebra
is somewhat lengthy, but straightforward"), with no worked proof in the
text.

**Qualification (Arfken et al.).** Arfken et al. conclude from eq. 9.21
that "the classification of our PDE remains invariant under
transformation" (p. 411). Their argument covers one linear change of
variables, constant coefficients and $a_{22} > 0$. Riley et al.'s
Exercise 20.24 states the invariance for every non-singular change of
variables, with the Jacobian factor. The two statements agree where both
apply; Riley's is the general one.

## Scope

Riley et al. classify only equations in two independent variables; they give
no classification for more variables or for first-order systems, and no
definition of a hyperbolic system.

Arfken et al. extend the names to more variables without a definition: "we
apply the terms hyperbolic, elliptic, and parabolic in a way that relates
the spatial to the time derivatives". The Laplace and Poisson equations are
elliptic, the wave equation hyperbolic, the diffusion equation parabolic,
and "we will not carry out a full analysis" (§9.3, p. 411). This is a usage
convention for the model equations, not a classification criterion (for
instance, by the signature of the coefficient matrix). The general
classification in more variables, and of first-order systems, still waits
for its sources.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.3.3 (p. 687), §20.6.2
  (pp. 701–705), Exercise 20.24 (p. 710).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §9.3 (pp. 409–412),
  eqs. 9.11–9.22, Exercise 9.3.1.
