---
type: Definition
title: "Gradient"
description: "The vector field ∇φ of a scalar field, with dφ = ∇φ·dx: ∂φ/∂x^k e_k in Cartesians, Σ(1/h_i)∂φ/∂ξ^i â_i in orthogonal coordinates and ∂φ/∂ξ^i a^i in any coordinates; normal to the level surfaces, and the limit of the closed-surface integral of φ dS per unit volume."
status: established
aliases: [grad, del, directional derivative, normal derivative]
tags: [vector-calculus, operators, curvilinear-coordinates]
timestamp: 2026-10-16T00:00:00Z
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

[Arfken et al. (2013)](/sources/arfken-2013.md) (§3.5, eqs. (3.38)–(3.45), pp. 143–145)
state the same definition and geometry: $d\phi=\nabla\phi\cdot d\mathbf x$
(eq. (3.41)), the direction of fastest increase, $\nabla r=\hat{\mathbf x}$
and $\nabla\phi(r)=(d\phi/dr)\hat{\mathbf x}$ (eqs. (3.49), (3.51)). They also
prove that $\nabla\phi$ *is* a vector, i.e. that its components transform
under rotations like those of $d\mathbf x$, by recognising each transformed
component as a chain-rule expression for $\partial\phi/\partial x'_i$
(eqs. (3.42)–(3.43), p. 144), and observe that the gradient's law
differs from that of a vector once frames are not Cartesian, which is where
the covariant/contravariant distinction starts (§4.1, eq. (4.3), p. 206).

## In curvilinear coordinates

* **Orthogonal** (eq. (10.60), p. 367): matching $d\phi=\partial_i\phi\,d\xi^i$
  with $d\mathbf x=\sum_ih_i\,d\xi^i\hat{\mathbf a}_i$,
  $$\nabla\phi=\sum_i\frac{1}{h_i}\frac{\partial\phi}{\partial\xi^i}\hat{\mathbf a}_i,\qquad \nabla=\sum_i\frac{\hat{\mathbf a}_i}{h_i}\frac{\partial}{\partial\xi^i},$$
  and in particular $\nabla\xi^i=\hat{\mathbf a}_i/h_i$ ([scale factors](/definitions/scale-factors.md)).
  Arfken et al. give the same formula (eqs. (3.138)–(3.139), p. 185), noting
  that orthogonality lets the Cartesian form carry over with the
  displacements $h_i\,d\xi^i$.
  Cylindrical and spherical forms: Tables 10.2–10.3 (pp. 360, 363).
* **General** (eq. (26.91), p. 972): the covariant derivative of a scalar is
  its partial derivative, so
  $$\nabla\phi=\frac{\partial\phi}{\partial\xi^i}\,\mathbf a^i,$$
  i.e. the covariant components of $\nabla\phi$ are $\partial_i\phi$ (a
  covariant vector by the [quotient law](/results/quotient-law.md), p. 968);
  contravariant components follow by raising, $g^{ij}\partial_j\phi$
  ([metric tensor](/definitions/metric-tensor.md)). Arfken et al. obtain the
  same from the Cartesian components $(\nabla\phi)_j=(\partial\phi/\partial\xi^i)(\partial\xi^i/\partial x^j)$
  (eqs. (4.49)–(4.50), (4.64), pp. 221, 224), "showing that the covariant
  representation of $\nabla\psi$ is the set of derivatives".
  [Seto et al. (2023)](/sources/seto-2023.md) write the gradient on the
  covariant basis of field-aligned coordinates,
  $\nabla\phi=g^{ij}\partial_j\phi\,\mathbf a_i$ (eq. (A.2), p. 14), as the
  first step of the perpendicular Laplacian, and the perpendicular gradient
  as $\nabla_\perp\phi=\nabla\phi-g_{22}^{-1}\partial_2\phi\,g_{2i}\mathbf a^i$
  (eq. (A.13), p. 15), since $\hat{\mathbf b}=\mathbf a_2/\sqrt{g_{22}}$
  there ([field-aligned coordinates](/definitions/field-aligned-coordinates.md)).

## Integral (coordinate-free) form

$\nabla\phi=\lim_{V\to0}\frac1V\oint_S\phi\,d\mathbf S$ (eq. (11.14),
p. 398); proved in the source for Cartesian coordinates only — the
curvilinear proof "requires complicated manipulations of the derivatives of
the basis vectors ... and is not presented" (p. 398). See
[integral definitions of grad, div and curl](/results/integral-definitions-of-grad-div-curl.md).
Its integrated form is $\int_V\nabla\phi\,dV=\oint_S\phi\,d\mathbf S$
(eq. (11.21); [divergence theorem](/results/divergence-theorem.md)).

**As a form.** The differential of a function is the 1-form
$d\phi=(\nabla\phi)_k\,dx^k$ (Arfken et al., eq. (4.86), p. 240;
[exterior derivative](/definitions/exterior-derivative.md)); its integral
along any curve is $\phi(\text{end})-\phi(\text{start})$ (eq. (4.101)).

The gradient of a vector, $\partial v_i/\partial x_j$, is a second-order
tensor ([Cartesian tensor](/definitions/cartesian-tensor.md)); its
general-coordinate form is the [covariant derivative](/definitions/covariant-derivative.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §10.7.1, pp. 348–352; §§10.9–10.10, pp. 360–367; §11.7, p. 398; §26.19, p. 968; §26.20, p. 972.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §3.5, pp. 143–146; §3.10, pp. 185, 189, 192; §4.1, p. 206; §4.3, pp. 221, 224; §4.6, p. 240; §4.7, p. 244.
* [Seto et al. (2023)](/sources/seto-2023.md), App. A.1, pp. 14–15.
