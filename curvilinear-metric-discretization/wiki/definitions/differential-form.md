---
type: Definition
title: "Differential form"
description: "A p-form is a sum of coefficient functions times wedge products of p basis 1-forms dx^i, an object built to be the oriented integrand of a p-dimensional integral; in three dimensions 0-, 1-, 2- and 3-forms carry scalars, line, surface and volume integrands, and no p-form with p > D survives."
status: established
aliases: [p-form, 1-form, 2-form, 3-form, 0-form, exterior differential form, Cartan calculus, closed form, exact form]
tags: [differential-forms, exterior-calculus, integration]
timestamp: 2026-10-14T00:00:00Z
---

# Differential form

In the calculus of differential forms (Cartan's calculus) the differentials
$dx^i$ are not infinitesimal numbers but objects with prescribed operational
rules; combined with the [wedge product](/definitions/wedge-product.md) they
generate the $p$-forms ([Arfken et al. (2013)](/sources/arfken-2013.md),
§4.5, eqs. (4.77)–(4.79), pp. 232–233). In three-dimensional space, with
$\phi$, $\psi$, $v_k$ and $b_k$ ordinary functions of position:

$$\begin{aligned}
\text{0-form:}\quad&\phi,\\
\text{1-form:}\quad&\alpha=v_1\,dx^1+v_2\,dx^2+v_3\,dx^3,\\
\text{2-form:}\quad&\beta=b_1\,dx^2\wedge dx^3+b_2\,dx^3\wedge dx^1+b_3\,dx^1\wedge dx^2,\\
\text{3-form:}\quad&\psi\,dx^1\wedge dx^2\wedge dx^3.
\end{aligned}$$

* A $p$-form contains $p$ factors $dx^i$ in each term; ordinary functions are
  0-forms (p. 233). The definition presupposes neither the dimension $D$ of
  the space nor its metric: forms are defined on differentiable manifolds,
  sets of points labelled by locally smooth coordinates (p. 233, with the
  remark that a coordinate on a circle or sphere cannot be globally smooth).
* **Integrands.** 1-forms are designed to be the integrands of line
  integrals, 2-forms of surface integrals, 3-forms of volume integrals
  (pp. 233, 235): "1-forms can be associated with elements of length,
  2-forms with area, and 3-forms with volume", and these elements are
  **oriented**, with signs fixed by the order in which the differentials
  are written (p. 235).
* **Dimension bound.** A wedge product containing a repeated or linearly
  dependent differential vanishes, so in a space of dimension $D$ only
  $p\le D$ occurs: up to 3-forms in three dimensions, 4-forms in Minkowski
  space (p. 234).
* **Coefficients.** In $\alpha=v_k\,dx^k$ the coefficients transform under a
  change of coordinates like vector components; the older literature called
  the differentials and the coefficients contravariant and covariant
  components, since they transform in mutually inverse ways (p. 233). This
  is the dictionary by which every relation between forms translates into a
  relation of vector analysis.
* **Complementary forms.** With a metric and an orientation, each $p$-form
  has a dual $(D-p)$-form, given by the [Hodge star](/definitions/hodge-star.md)
  (p. 235).

## Integration

The integral of a 1-form along a curve is a line integral evaluated through
any monotone parametrisation; the integral of a 2-form $\psi\,dx\wedge dy$ over a
plane region is $\int\psi\,(\pm dx\,dy)$, the sign being the **orientation** of
the area, and the opposite sign must be used for $dy\wedge dx$ in the same
computation (§4.7, eqs. (4.102)–(4.105), pp. 243–245). Under a change of
variables the wedge product produces the signed
[Jacobian](/definitions/jacobian.md) by itself, without inserting it by hand
([wedge product](/definitions/wedge-product.md), eq. (4.103)). The general
integral theorem is [Stokes' theorem for differential forms](/results/generalized-stokes-theorem.md),
$\int_\Omega d\alpha=\int_{\partial\Omega}\alpha$.

The book insists that orientation choices (counterclockwise traversal,
right-handed axes, $dy\wedge dz\mapsto d\mathbf S$ components) are not
dictated by the calculus but by the user, who "has the responsibility to make
definitions corresponding to the situation for which the results are claimed
to be relevant" (pp. 247–248).

## Closed and exact forms

A 1-form $\alpha$ is **exact** on a region if $\alpha=d\phi$ there for some
function $\phi$; then $\int_P^Q\alpha=\phi(Q)-\phi(P)$, independent of the
path, in any dimension (eqs. (4.100)–(4.101), p. 244). In two dimensions,
$v_x\,dx+v_y\,dy$ is called **closed** if $\partial v_x/\partial y=\partial v_y/\partial x$
(exercise 4.7.3, p. 248), i.e. if its [exterior derivative](/definitions/exterior-derivative.md)
vanishes; every exact form is closed because $d(d\phi)=0$. The exercise asks
which of several 1-forms are closed or exact, including
$(-y\,dx+x\,dy)/(x^2+y^2)$, which is closed away from the origin; the
book does not state in Ch. 4 under what condition a closed form is exact. For
1-forms in three dimensions the vector-calculus version is the
[conservative vector field](/definitions/conservative-vector-field.md):
on a simply connected region, irrotational fields are gradients.

*Compiler's remark.* For a body-fitted grid the forms viewpoint assigns each
field a natural geometric home (point values, edge integrals, face fluxes,
cell integrals for 0-, 1-, 2-, 3-forms); the source states the integrand
correspondence only, not its discrete use, and no source of this bundle yet
treats discrete forms.

# Citations

* [Arfken et al. (2013)](/sources/arfken-2013.md), §4.5, pp. 232–235; §4.7, pp. 243–248; exercise 4.7.3, p. 248.
