---
type: Operator
title: "Five-point discrete Laplacian"
description: "Second-order central-difference approximation of the two-dimensional Laplacian on a rectangular grid with spacings Delta x and Delta y; with Dirichlet values on the perimeter it turns Laplace's equation into a linear system for the interior grid values, and a nine-point variant is posed as an exercise."
status: established
symbol: "$\\nabla_h^2$"
aliases: [five-point stencil, 5-point Laplacian, discrete Laplacian, nine-point stencil]
tags: [discretization, finite-difference, poisson]
timestamp: 2026-10-13T00:00:00Z
---

# Five-point discrete Laplacian

**Definition.** On a grid $x_i=x_0+i\Delta x$, $y_j=y_0+j\Delta y$ with
$u_{i,j}\approx u(x_i,y_j)$, second central differences give
$$\left(\nabla_h^2u\right)_{i,j}=\frac{u_{i+1,j}-2u_{i,j}+u_{i-1,j}}{(\Delta x)^2}+\frac{u_{i,j+1}-2u_{i,j}+u_{i,j-1}}{(\Delta y)^2}$$
([Riley et al. (2006)](/sources/riley-2006.md), §27.8, eq. 27.87,
p. 1031). Laplace's equation $\nabla^2u=0$ becomes
$\left(\nabla_h^2u\right)_{i,j}=0$ at every interior point.

**Identity.** With $\beta=(\Delta x/\Delta y)^2$, the discrete equation is
equivalently
$$u_{i+1,j}+u_{i-1,j}+\beta\left(u_{i,j+1}+u_{i,j-1}\right)=2(1+\beta)\,u_{i,j}\quad\text{(eq. 27.88)},$$
and for $\beta=1$ ($\Delta x=\Delta y=h$) each interior value is the mean of
its four neighbours.

**Boundary values.** On a rectangle the perimeter values $u_{0,j}$,
$u_{N,j}$, $u_{i,0}$, $u_{i,M}$ are prescribed (eq. 27.89; here $N$ and $M$
are the grid index ranges). Non-rectangular boundaries need "more complex
boundary-value prescriptions" or non-Cartesian coordinates (p. 1031). The
interior equations form a sparse linear system, which the book solves only
by [relaxation](/methods/laplace-relaxation.md).

**Order.** The book calls eq. 27.87 a "second central difference formula"
and gives no truncation-error statement for it in §27.8. Exercise 27.26
(statement read, solution not) has the reader show by Taylor expansion that
the nine-point weighted mean — weight $1/5$ on each of the four nearest and
$1/20$ on each of the four diagonal neighbours, $\Delta x=\Delta y=h$ — is
a relaxation scheme "good to the fifth order in $h$" for Laplace's
equation, using $\partial_x^4u+2\partial_x^2\partial_y^2u+\partial_y^4u=0$
(p. 1038).

Stability, accuracy and feasibility of PDE schemes are said to be "too
complicated to be discussed here" (p. 1031).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §27.8 (pp. 1030–1031),
  exercise 27.26 (p. 1038).
