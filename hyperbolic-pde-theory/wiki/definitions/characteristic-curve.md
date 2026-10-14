---
type: Definition
title: "Characteristic curves"
description: "Curves along which data on a curve cannot determine the derivatives of the solution: for a first-order linear PDE the curves dy/dx = b2/b1 along which the solution's invariant is constant, for a second-order PDE the real roots of the characteristic ODE; they carry information, and data on a characteristic, or on a curve crossing one twice, leave the solution undetermined or overdetermined."
status: established
aliases: [characteristics, characteristic lines, characteristic directions]
tags: [characteristics, well-posedness, first-order, second-order]
timestamp: 2026-10-13T00:00:00Z
---

# Characteristic curves

## First-order equations

Take $b_1(x,y)\,\partial_x u + b_2(x,y)\,\partial_y u = \psi(x,y,u)$ and
prescribe $u = g(\sigma)$ along a curve $\Gamma$: $x = x(\sigma)$,
$y = y(\sigma)$, $\sigma$ arc length
([Riley et al. (2006)](/sources/riley-2006.md), eq. 20.39, p. 699). Along
$\Gamma$,
$$\frac{\mathrm dg}{\mathrm d\sigma} = \partial_x u\,\frac{\mathrm dx}{\mathrm d\sigma} + \partial_y u\,\frac{\mathrm dy}{\mathrm d\sigma}$$
(eq. 20.40). With the PDE this is a linear system for $\partial_x u$ and
$\partial_y u$. It fails to have a unique solution exactly where
$$\begin{vmatrix} \mathrm dx/\mathrm d\sigma & \mathrm dy/\mathrm d\sigma \\ b_1 & b_2 \end{vmatrix} = 0
\quad\Longleftrightarrow\quad \frac{\mathrm dy}{\mathrm dx} = \frac{b_2(x,y)}{b_1(x,y)},$$
and the curves with this slope are the **characteristics** (eq. 20.41,
p. 699). They are the curves along which the invariant $\xi$ of the
general solution $u = F(\xi)$ is constant (eq. 20.12; see
[first-order linear PDEs](/methods/first-order-linear-pde-characteristics.md)).

If $\Gamma$ is nowhere characteristic, the data and the PDE give all
derivatives on $\Gamma$, and the book argues that the solution is then
fixed near $\Gamma$ by a Taylor expansion about it. Characteristics are
therefore "the curves along which information about the solution
'propagates'" (p. 700). This is a heuristic: no existence theorem is
stated.

Two failures (p. 700, Fig. 20.3):

* $\Gamma$ is itself a characteristic, or a single point: information
  cannot leave $\Gamma$, and the solution stays unspecified off it.
* $\Gamma$ crosses some characteristic more than once: the data on one
  arc already fix the solution on those characteristics, so data on a
  second arc "can overdetermine the problem solution and generally results
  in there being no solution".

Worked case (pp. 700–701): for $x\,\partial_x u - 2y\,\partial_y u = 0$
the characteristics are $x^2y = \text{const}$. With $u = 2y + 1$ given on
$x = 1$ only for $0 \le y \le 1$, the solution $u = 2x^2y + 1$ holds
only where $0 \le x^2y \le 1$, the region swept by the characteristics
that meet the data segment. Elsewhere any $2x^2y + 1 + G(x^2y)$ with
$G = 0$ on $[0,1]$ fits.

## Second-order equations

Take $a_{11}\,\partial_x^2 u + 2a_{12}\,\partial_x\partial_y u + a_{22}\,\partial_y^2 u = \psi(x,y,u,\partial_x u,\partial_y u)$
with Cauchy data $u = g$, $\partial_n u = h$ on $\Gamma$ (eq. 20.43,
p. 701). The tangential and normal derivatives give $\partial_x u$ and
$\partial_y u$ on $\Gamma$. Differentiating these along $\Gamma$ gives
two more linear equations for the three second derivatives, and with the
PDE the system is singular when
$$\begin{vmatrix} a_{11} & 2a_{12} & a_{22} \\ \mathrm dx/\mathrm d\sigma & \mathrm dy/\mathrm d\sigma & 0 \\ 0 & \mathrm dx/\mathrm d\sigma & \mathrm dy/\mathrm d\sigma \end{vmatrix} = 0
\quad\Longleftrightarrow\quad a_{11}\left(\frac{\mathrm dy}{\mathrm dx}\right)^2 - 2a_{12}\frac{\mathrm dy}{\mathrm dx} + a_{22} = 0$$
(p. 703, eq. 20.44). The roots
$\mathrm dy/\mathrm dx = (a_{12} \pm \sqrt D)/a_{11}$ (eq. 20.45) give two
real families when the equation is hyperbolic, one when parabolic and two
complex families when elliptic (see
[classification](/definitions/second-order-pde-classification.md)). With
constant coefficients they are straight lines $x + \beta_j y = \text{const}$
(p. 703), the arguments of the
[general solution](/methods/constant-coefficient-second-order-general-solution.md).

For the [wave equation](/definitions/wave-equation.md),
$(\mathrm dx/\mathrm dt)^2 = c^2$, and the characteristics are the lines
$x - ct = \text{const}$ and $x + ct = \text{const}$ (p. 704).

**Propagation.** At a point, the solution is determined only if both
characteristics through it meet the curve that carries the data
(p. 704). Cauchy data $u$, $\partial_t u$ on $t = 0$, $0 \le x \le L$,
for the wave equation therefore fix the solution only in the region
bounded by the characteristics from the ends of the segment, the points
with $0 \le x - ct$ and $x + ct \le L$ for $t \ge 0$ (Fig. 20.5). If a
hyperbolic equation's data curve meets a characteristic more than once,
Cauchy data can overdetermine the problem; the curve must be changed, or
the data on the offending parts relaxed to Dirichlet or Neumann
conditions (p. 705).

## Remark (compiler's derivation)

The book does not write the equation that $u$ obeys along a first-order
characteristic. It follows from the chain rule: on a curve with
$\mathrm dx/\mathrm d\sigma = b_1$, $\mathrm dy/\mathrm d\sigma = b_2$,
$$\frac{\mathrm du}{\mathrm d\sigma} = b_1\,\partial_x u + b_2\,\partial_y u = \psi(x,y,u),$$
so the PDE becomes a system of ODEs along each characteristic. This is the
compiler's derivation, not a claim of the source.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.6 (pp. 699–705),
  Figs. 20.2–20.5.
