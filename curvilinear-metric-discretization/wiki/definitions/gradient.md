---
type: Definition
title: "Gradient"
description: "The vector field ∇φ of a scalar field, with dφ = ∇φ·dx: ∂φ/∂x^k e_k in Cartesians, Σ(1/h_i)∂φ/∂ξ^i â_i in orthogonal coordinates and ∂φ/∂ξ^i a^i in any coordinates; normal to the level surfaces, and the limit of the closed-surface integral of φ dS per unit volume."
status: established
aliases: [grad, del, directional derivative, normal derivative]
tags: [vector-calculus, operators, curvilinear-coordinates]
timestamp: 2026-10-13T00:00:00Z
---

# Gradient

## Definition and geometry

In Cartesian coordinates $\nabla=\mathbf e_k\,\partial/\partial x^k$ and
$\nabla\phi=\mathbf e_k\,\partial\phi/\partial x^k$ (eqs. (10.25)–(10.26),
p. 348). For a displacement $d\mathbf x$, $d\phi=\nabla\phi\cdot d\mathbf x$
(eq. (10.27)), so along a curve $d\phi/du=\nabla\phi\cdot d\mathbf x/du$ and
the **directional derivative** in a unit direction $\hat{\mathbf s}$ is
$\nabla\phi\cdot\hat{\mathbf s}$ (eqs. (10.28)–(10.30), p. 349);
$\nabla\phi$ points along the fastest increase of $\phi$, is normal to the
level surfaces $\phi=$ const, and $\nabla\phi=(\partial\phi/\partial n)\hat{\mathbf n}$
with the **normal derivative** $\partial\phi/\partial n=\lvert\nabla\phi\rvert$
(eq. (10.32), p. 350). The scalar operator $\hat{\mathbf s}\cdot\nabla$ gives
the rate of change of a vector field in direction $\hat{\mathbf s}$
(eq. (10.31)). Chain rule: $\nabla[\phi(\psi)]=(\partial\phi/\partial\psi)\nabla\psi$
(p. 352). All from [Riley et al. (2006)](/sources/riley-2006.md), §10.7.1.

## In curvilinear coordinates

* **Orthogonal** (eq. (10.60), p. 367): matching $d\phi=\partial_i\phi\,d\xi^i$
  with $d\mathbf x=\sum_ih_i\,d\xi^i\hat{\mathbf a}_i$,
  $$\nabla\phi=\sum_i\frac{1}{h_i}\frac{\partial\phi}{\partial\xi^i}\hat{\mathbf a}_i,\qquad \nabla=\sum_i\frac{\hat{\mathbf a}_i}{h_i}\frac{\partial}{\partial\xi^i},$$
  and in particular $\nabla\xi^i=\hat{\mathbf a}_i/h_i$ ([scale factors](/definitions/scale-factors.md)).
  Cylindrical and spherical forms: Tables 10.2–10.3 (pp. 360, 363).
* **General** (eq. (26.91), p. 972): the covariant derivative of a scalar is
  its partial derivative, so
  $$\nabla\phi=\frac{\partial\phi}{\partial\xi^i}\,\mathbf a^i,$$
  i.e. the covariant components of $\nabla\phi$ are $\partial_i\phi$ (a
  covariant vector by the [quotient law](/results/quotient-law.md), p. 968);
  contravariant components follow by raising, $g^{ij}\partial_j\phi$
  ([metric tensor](/definitions/metric-tensor.md)).

## Integral (coordinate-free) form

$\nabla\phi=\lim_{V\to0}\frac1V\oint_S\phi\,d\mathbf S$ (eq. (11.14),
p. 398); proved in the source for Cartesian coordinates only — the
curvilinear proof "requires complicated manipulations of the derivatives of
the basis vectors ... and is not presented" (p. 398). See
[integral definitions of grad, div and curl](/results/integral-definitions-of-grad-div-curl.md).
Its integrated form is $\int_V\nabla\phi\,dV=\oint_S\phi\,d\mathbf S$
(eq. (11.21); [divergence theorem](/results/divergence-theorem.md)).

The gradient of a vector, $\partial v_i/\partial x_j$, is a second-order
tensor ([Cartesian tensor](/definitions/cartesian-tensor.md)); its
general-coordinate form is the [covariant derivative](/definitions/covariant-derivative.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §10.7.1, pp. 348–352; §§10.9–10.10, pp. 360–367; §11.7, p. 398; §26.19, p. 968; §26.20, p. 972.
