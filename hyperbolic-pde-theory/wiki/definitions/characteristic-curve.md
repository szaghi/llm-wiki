---
type: Definition
title: "Characteristic curves"
description: "Curves along which data on a curve cannot determine the derivatives of the solution: for a first-order linear PDE the curves dy/dx = b2/b1 along which the solution's invariant is constant, for a second-order PDE the real roots of the characteristic ODE; they carry information, and data on a characteristic, or on a curve crossing one twice, leave the solution undetermined or overdetermined."
status: established
aliases: [characteristics, characteristic lines, characteristic directions]
tags: [characteristics, well-posedness, first-order, second-order]
timestamp: 2026-10-14T00:00:00Z
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

**Arfken et al.'s version.** [Arfken et al. (2013)](/sources/arfken-2013.md)
make the same determinant argument for constant coefficients: $u$ given
along a curve parametrised by $\sigma$, the derivative along the curve and
the PDE form a linear system for $\partial_x u$, $\partial_y u$, and the
Taylor expansion about a point of the curve then extends $u$ off it,
"tacitly assuming that there are no singularities" (§9.2, eqs. 9.5–9.7,
pp. 405–406). The determinant vanishes on the characteristics
$\mathrm dy/\mathrm dx = b_2/b_1$ (eq. 9.4). They draw four conclusions
(p. 406). Data on a curve fix $u$ along every characteristic that meets
it. Data on a curve that meets a characteristic twice usually lead to an
inconsistency. Only a non-characteristic curve can fix $u$ off itself.
Data along a characteristic "will ordinarily lead to inconsistency", so
that the PDE has no solution unless the data are redundant, and in any case
give no information off that characteristic. They agree with Riley et al.
on the overdetermined case.

*Qualification.* For data on a characteristic, Riley et al. stress only
that the solution stays unspecified off it; Arfken et al. add that
arbitrary data on a characteristic are incompatible with the PDE, which
already fixes how $u$ varies along it. The statements are complementary:
data on a characteristic must satisfy a compatibility condition, and if
they do they still leave $u$ undetermined elsewhere. Neither book states
the compatibility condition in general (compiler's synthesis).

**More than two variables** (Arfken et al., pp. 407–408). For
$\mathbf b\cdot\nabla u = 0$ with constant $\mathbf b$, the characteristics are
the straight lines parallel to $\mathbf b$. Data on a surface determine the
three first derivatives only if two independent directions in the surface
and $\mathbf b$ are linearly independent. If a characteristic lies in the
data surface the determinant vanishes. "A boundary condition is effective
in determining a unique solution to a first-order PDE only if the boundary
does not include a characteristic, and inconsistencies may arise if a
characteristic intersects a boundary more than once" (p. 408).

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
$x - ct = \text{const}$ and $x + ct = \text{const}$ (p. 704). Arfken et al.
reach the same lines by another route. They factor the hyperbolic operator
into two first-order operators and take the characteristics of each factor
(eqs. 9.12–9.14, p. 409; eq. 9.89, p. 435). For elliptic equations the
factors, and so the characteristics, are complex and "do not have an obvious
relevance to boundary conditions" (p. 410; see
[classification](/definitions/second-order-pde-classification.md)). Arfken
et al. add that for some hyperbolic equations "it will also be practical to
propagate solutions along the characteristics" (pp. 409–410).

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

Riley et al. do not write the equation that $u$ obeys along a first-order
characteristic. It follows from the chain rule: on a curve with
$\mathrm dx/\mathrm d\sigma = b_1$, $\mathrm dy/\mathrm d\sigma = b_2$,
$$\frac{\mathrm du}{\mathrm d\sigma} = b_1\,\partial_x u + b_2\,\partial_y u = \psi(x,y,u),$$
so the PDE becomes a system of ODEs along each characteristic. This was the
compiler's derivation at the founding ingestion.

**Partly supported since arfken-2013.** For constant $b_1$, $b_2$, Arfken et
al. state it: in the coordinates $\sigma = b_1x + b_2y$ (along the
characteristics) and $\xi = b_2x - b_1y$ (constant on them), the equation
$b_1\partial_x u + b_2\partial_y u + c_0u = \psi$ becomes
$(b_1^2 + b_2^2)\,\partial_\sigma u + c_0u = \psi$, "really an ODE in
$\sigma$" with $\xi$ as a parameter (eqs. 9.8–9.9, pp. 406–407). They
generalise in words: "more general PDEs can be solved using ODE methods on
characteristic lines, a feature that causes it to be said that PDE
solutions propagate along the characteristics" (p. 405). The
variable-coefficient form above and its extension to $\psi(x,y,u)$ remain
the compiler's derivation; Arfken et al. leave variable coefficients to
Exercises 9.2.5–9.2.6.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.6 (pp. 699–705),
  Figs. 20.2–20.5.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §9.2 (pp. 403–408),
  §9.3 (pp. 409–410), §9.6 (p. 435).
