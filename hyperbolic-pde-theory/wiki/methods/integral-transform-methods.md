---
type: Method
title: "Integral transform methods"
description: "Transform a linear PDE (or ODE) in one variable, Laplace in time for initial-value problems, Fourier in space on infinite ranges, to remove that variable's derivatives, solve the resulting ODE (or algebraic equation) with the data built in, and invert, using convolution to obtain Green's-function integrals such as the Gaussian heat-kernel solution."
status: established
aliases: [Laplace transform method, Fourier transform method, transform methods]
tags: [transform-methods, diffusion, ode, greens-function]
timestamp: 2026-10-13T00:00:00Z
---

# Integral transform methods

A transform with respect to one independent variable removes that
variable from the derivatives. A PDE in two variables becomes an ODE, and a
constant-coefficient ODE becomes an algebraic equation. Initial or
boundary data enter through the transforms of the derivatives. The
solution is then inverted ([Riley et al. (2006)](/sources/riley-2006.md),
§21.4, p. 747; §15.1.5, p. 501). Which transform, in which variable, "is a
matter of experience" (p. 747). Laplace and Fourier transform theory is in
Ch. 13, which this bundle has not read.

## Laplace transform in time

$\bar u(x,p) = \int_0^\infty u(x,t)e^{-pt}\,\mathrm dt$, and the transform
of $\partial_t u$ is $p\bar u - u(x,0)$ (p. 747). For the
[diffusion equation](/definitions/diffusion-equation.md) on $x > 0$ with
$u(x,0) = 0$ and $u(0,t) = g$:
$$\kappa\,\partial_x^2\bar u = p\bar u \quad\Rightarrow\quad \bar u(x,p) = \frac{g}{p}\exp\left(-\sqrt{p/\kappa}\,x\right)$$
(eq. 21.72, p. 748). The growing exponential is excluded by $u \to 0$ as
$x \to \infty$. The inverse, $u = g[1 - \operatorname{erf}(x/\sqrt{4\kappa t})]$,
needs a contour integration (deferred to Ch. 24, not read). Transforming
the total amount $\int_0^\infty u\,\mathrm dx$ instead gives a simpler
inversion, $2g\sqrt{\kappa t/\pi}$ (pp. 748). The book's verdict: the
easy elimination of derivatives "is usually paid for by the introduction
of a difficult inverse transformation", a problem less severe for Fourier
transforms (p. 748).

**ODEs.** For a constant-coefficient linear ODE the transform of
$y^{(n)}$ is $p^n\bar y - p^{n-1}y(0) - \dots - y^{(n-1)}(0)$ (eq. 15.32),
so the solution with one-point data comes out in one step, after partial
fractions and a table inversion. Systems of linear ODEs are handled the
same way (§15.1.5, pp. 501–503).

## Fourier transform in space

$\tilde u(k,t) = (2\pi)^{-1/2}\int u(x,t)e^{-ikx}\,\mathrm dx$, assuming
$u, \partial_x u \to 0$ as $|x| \to \infty$. For the diffusion equation on
the line, $\partial_t\tilde u = -\kappa k^2\tilde u$, so
$\tilde u = \tilde u_0(k)e^{-\kappa k^2t}$ (eq. 21.73, p. 749). The
convolution theorem then gives
$$u(x,t) = \frac{1}{\sqrt{4\pi\kappa t}}\int_{-\infty}^{\infty}\exp\left[-\frac{(x - x')^2}{4\kappa t}\right]u_0(x')\,\mathrm dx'$$
(eq. 21.74, p. 750), a superposition of the heat kernel ([fundamental
solution](/definitions/fundamental-solution.md)). The Gaussian integral is
evaluated by completing the square; the shift of the integration path off
the real axis is justified in Ch. 24 (p. 750).

## Relation to separation of variables

The closed forms (integrals rather than series) come from the infinite
range of $x$, not from the transform. [Separation of
variables](/methods/separation-of-variables.md) with an unrestricted real
separation constant gives an integral over that constant, which is an
inverse Fourier transform, and the same solution (eq. 21.75,
pp. 750–751).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §15.1.5 (pp. 501–503),
  §21.4 (pp. 747–751).
