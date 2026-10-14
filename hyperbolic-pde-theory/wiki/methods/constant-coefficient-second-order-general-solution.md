---
type: Method
title: "General solution of constant-coefficient second-order PDEs"
description: "For a11 u_xx + 2 a12 u_xy + a22 u_yy = 0 with constant coefficients, u = F(x + beta1 y) + G(x + beta2 y) where the beta are the roots of a22 beta^2 + 2 a12 beta + a11 = 0, or F + x G in the repeated-root parabolic case; in characteristic coordinates the equation reduces to u_xi_eta = 0, or u_eta_eta = 0 when parabolic."
status: established
aliases: [characteristic coordinates, canonical form, reduction to u_xi_eta = 0]
tags: [second-order, characteristics, general-solution, canonical-form]
timestamp: 2026-10-13T00:00:00Z
---

# General solution of constant-coefficient second-order PDEs

The equation is the principal part alone with constant coefficients,
$$a_{11}\,\partial_x^2 u + 2a_{12}\,\partial_x\partial_y u + a_{22}\,\partial_y^2 u = 0$$
([Riley et al. (2006)](/sources/riley-2006.md), eq. 20.20, p. 688). The
method needs every term to have the same total number of derivatives, so
there are no lower-order terms and no forcing (p. 688). The
[diffusion equation](/definitions/diffusion-equation.md) is therefore
excluded.

## Arbitrary functions of linear combinations

A solution $u = F(\xi(x,y))$ yields only $F''$ only if $\xi$ is linear,
$\xi = x + \beta y$ (pp. 688–689). Substituting gives
$(a_{11} + 2a_{12}\beta + a_{22}\beta^2)F'' = 0$ (eq. 20.21), so $F$ is
arbitrary when
$$a_{22}\beta^2 + 2a_{12}\beta + a_{11} = 0, \qquad \beta_{1,2} = \frac{-a_{12} \pm \sqrt D}{a_{22}}$$
(p. 689; dividing by $a_{22}$ assumes it is non-zero). With $D \ne 0$ the
general solution is
$$u(x,y) = F(x + \beta_1y) + G(x + \beta_2y)$$
(eq. 20.22). The alternative $F'' = 0$ gives only the trivial linear
solution (p. 689). The roots are real in the
[hyperbolic](/definitions/second-order-pde-classification.md) case and
complex conjugate in the elliptic case (p. 690).

**Parabolic case** ($D = 0$). There is a single root
$\beta = -a_{12}/a_{22}$. Trying $u = v(x,y)G(x + \beta y)$ requires $v$ to
solve the equation, and $v = x$ gives
$$u = F(x + \beta y) + x\,G(x + \beta y)$$
(eq. 20.25, p. 690). The choice $v = y$ gives nothing new (p. 691).

## Characteristic coordinates

With $\xi = x + \beta_1y$, $\eta = x + \beta_2y$ the equation becomes
$$\left[2a_{11} + 2a_{12}(\beta_1 + \beta_2) + 2a_{22}\beta_1\beta_2\right]\partial_\xi\partial_\eta u = 0,$$
and the bracket is non-zero iff $D \ne 0$. Then $\partial_\xi\partial_\eta u = 0$,
whose two integrations give $u = F(\xi) + G(\eta)$ (pp. 691–692). In the
parabolic case $\xi = x + \beta y$, $\eta = x$ reduce it to
$a_{11}\partial_\eta^2u = 0$, so $u = \eta G(\xi) + F(\xi)$ (p. 692). The
coordinate lines are the [characteristics](/definitions/characteristic-curve.md)
of the operator (p. 703).

## Worked cases

* [Wave equation](/definitions/wave-equation.md), with $t$ for $y$:
  $\beta^2 = c^2$ and $u = F(x - ct) + G(x + ct)$ (eq. 20.23, pp. 689–690).
* [Laplace equation](/definitions/laplace-and-poisson-equations.md):
  $\beta = \pm i$ and $u = F(x + iy) + G(x - iy)$ (eq. 20.24, p. 690).
* $\partial_x^2u + 2\partial_x\partial_yu + \partial_y^2u = 0$ (parabolic,
  $\beta = -1$) with $u(0,y) = 0$, $u(x,1) = x^2$: $u = x(x - y + 1)$
  (p. 691).
* Forcing: particular integrals by inspection, e.g. $x^3 + y^3$ for
  $\nabla^2u = 6(x + y)$ (p. 692).

## A misstatement in the source (compiler's check)

The book says (p. 690) that hyperbolic and elliptic equations have
solutions whose arguments have the forms $x + \alpha y$ and $x + i\beta y$
respectively, with $\alpha$, $\beta$ real. From the roots above, the
elliptic arguments are $x + (\Re\beta_j \pm i\,\Im\beta_j)y$ with
$\Re\beta_j = -a_{12}/a_{22}$. They are purely imaginary multiples of $y$
only when $a_{12} = 0$. The statement holds as printed only for equations
without a mixed derivative. This is the compiler's derivation.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.3.3 (pp. 687–692),
  §20.6.2 (p. 703).
