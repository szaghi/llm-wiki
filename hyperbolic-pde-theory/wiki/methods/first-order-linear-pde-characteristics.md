---
type: Method
title: "First-order linear PDEs: general solution along characteristics"
description: "The general solution of b1 u_x + b2 u_y = 0 is an arbitrary function of an invariant constant along the characteristics dx/b1 = dy/b2; a zeroth-order term is absorbed by a particular solution factor, a forcing by a particular integral, and data on a non-characteristic curve then fix the arbitrary function where its characteristics reach."
status: established
aliases: [method of characteristics, first-order linear PDE, general solution in arbitrary functions]
tags: [first-order, characteristics, general-solution]
timestamp: 2026-10-14T00:00:00Z
---

# First-order linear PDEs: general solution along characteristics

The equation is
$$b_1(x,y)\,\partial_x u + b_2(x,y)\,\partial_y u + c_0(x,y)\,u = \psi(x,y)$$
([Riley et al. (2006)](/sources/riley-2006.md), eq. 20.9, p. 682).

## Steps

1. **One derivative missing.** If $b_1 = 0$ or $b_2 = 0$ the equation is a
   first-order linear ODE in the other variable, and its integration
   "constant" is an arbitrary function of the variable not integrated. For
   example $x\,\partial_x u + 3u = x^2$, multiplied by the integrating
   factor $x^3$, gives $u = x^2/5 + F(y)/x^3$ (p. 682; [first-order ODE
   methods](/methods/first-order-ode-solution-methods.md)).
2. **Principal part only** ($c_0 = \psi = 0$). Seek $u = F(\xi)$ with
   $\xi(x,y)$ unknown. Substituting removes $F$ and leaves
   $b_1\partial_x\xi + b_2\partial_y\xi = 0$ (eq. 20.10). Since $F$ is
   constant where $\xi$ is, comparing with
   $\mathrm d\xi = \partial_x\xi\,\mathrm dx + \partial_y\xi\,\mathrm dy = 0$
   shows that $\xi$ is constant along
   $$\frac{\mathrm dx}{b_1(x,y)} = \frac{\mathrm dy}{b_2(x,y)}$$
   (eqs. 20.11–20.12, p. 683). Integrating this ODE gives $\xi$, and
   $u = F(\xi)$ with $F$ arbitrary. These curves are the
   [characteristics](/definitions/characteristic-curve.md) (p. 700).
3. **Zeroth-order term** ($c_0 \ne 0$). Seek $u = v(x,y)F(\xi)$ with $v$
   any solution of the equation, however simple. The terms in $F$ vanish
   and $\xi$ obeys the same equation as in step 2 (pp. 684–685).
4. **Forcing** ($\psi \ne 0$). Add a particular integral, found by
   inspection or by adapting ODE methods, to the general solution of the
   homogeneous equation (p. 686; [homogeneous linear problems](/definitions/homogeneous-linear-problem.md)).
5. **Fit the data.** Choose $F$ so that $u$ takes the prescribed values on
   the data curve.

## Constant coefficients: rotated coordinates (Arfken et al.)

[Arfken et al. (2013)](/sources/arfken-2013.md) solve the constant-coefficient
case by a change of variables instead of the ansatz $u = F(\xi)$ (§9.2,
pp. 404–407). With $\sigma = b_1x + b_2y$ along the characteristics and
$\xi = b_2x - b_1y$ constant on them,
$$b_1\partial_x u + b_2\partial_y u = (b_1^2 + b_2^2)\,\partial_\sigma u ,$$
so $b_1\partial_x u + b_2\partial_y u = 0$ has the general solution
$u = F(b_2x - b_1y)$ with $F$ arbitrary (eqs. 9.1–9.3, p. 404), and with a
zeroth-order term and a forcing the equation becomes an ODE in $\sigma$
with $\xi$ as a parameter (eqs. 9.8–9.9, pp. 406–407). This agrees with
steps 2–4 above. Example 9.2.1: $\partial_x u + \partial_y u + (x + y)u = 0$
gives $u = e^{-xy}F(x - y)$ (p. 407; checked by substitution by the
compiler). Variable coefficients are left to Exercises 9.2.5–9.2.6
($y\,\partial_x u + x\,\partial_y u = 0$, $x\,\partial_x u - y\,\partial_y u = 0$, p. 409).

**Three variables** (pp. 407–408). For $\mathbf b\cdot\nabla u = 0$ with
constant $\mathbf b$, the characteristics are the lines parallel to
$\mathbf b$, and the general solution is an arbitrary function of two
independent combinations of $(x, y, z)$ that are constant along them (eq.
9.10). Riley et al. say the method "may be extended" to more variables but
do not show it (p. 681); Arfken et al. show the constant-coefficient case.

## Worked cases

* $x\,\partial_x u - 2y\,\partial_y u = 0$: $\mathrm dx/x = \mathrm dy/(-2y)$
  gives $\xi = x^2y$ and $u = F(x^2y)$. The data $u(1,y) = 2y + 1$ on the
  whole line give $u = 2x^2y + 1$. The single-point datum $u(1,1) = 4$
  gives the family $x^2y + 3 + G(x^2y)$ with $G(1) = 0$, so it is not
  unique (eqs. 20.13–20.14, pp. 683–684).
* $x\,\partial_x u + 2\,\partial_y u - 2u = 0$: $\xi = xe^{-y/2}$, and
  $u = e^{y}F(xe^{-y/2})$, equivalently $x^2G(xe^{-y/2})$ (eq. 20.15,
  pp. 684–685).
* $y\,\partial_x u - x\,\partial_y u = 3x$: $\xi = x^2 + y^2$, particular
  integral $-3y$, so $u = F(x^2 + y^2) - 3y$. The data $u(x,0) = x^2$ give
  $u = x^2 + y^2 - 3y$ (eq. 20.18, pp. 686–687).

## Uniqueness and existence

Data along a curve generally fix $u$; data at a point fix only a class of
solutions (p. 699). Data fix $u$ only on the characteristics that meet the
data curve. They fail if the curve is a characteristic, and generally
admit no solution if it crosses a characteristic twice
([characteristic curves](/definitions/characteristic-curve.md),
pp. 700–701).

## Scope

* Linear, two independent variables. The method "may be extended to
  equations containing several independent variables", but the book
  does not show it (p. 681).
* §20.6.1 allows $\psi(x,y,u)$ when analysing characteristics, but the
  solution method above is given only for the linear equation.
* **Nonlinear equations.** Neither book solves a nonlinear first-order
  PDE in the chapters read. Arfken et al. name
  $\partial_t u + c(u)\,\partial_x u = 0$ "the simplest nonlinear wave
  equation", in which the local propagation speed depends on the solution,
  and contrast it with the linear $\partial_t u + c\,\partial_x u = 0$
  (§9.3, eq. 9.23, p. 413). They do not analyse it; the scalar conservation
  law and its characteristics wait for their sources.
* Context (§20.2–20.3, pp. 680–681): a family of functions of one
  combination $\xi(x,y)$ satisfies a first-order PDE obtained by
  eliminating the function. The book notes that an $n$th-order PDE is not
  in general the result of eliminating $n$ arbitrary functions, but that
  one may "expect $n$ combinations to be involved in the solution".
* The ODE that $u$ obeys along a characteristic,
  $\mathrm du/\mathrm d\sigma = \psi - c_0u$ on
  $(\mathrm dx, \mathrm dy)/\mathrm d\sigma = (b_1, b_2)$, is not written
  by the book. It is the compiler's chain-rule derivation (see the remark on
  [characteristic curves](/definitions/characteristic-curve.md)).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.2–20.3.2
  (pp. 680–687), §20.6.1 (pp. 699–701).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §9.2 (pp. 403–409),
  §9.3 (p. 413).
