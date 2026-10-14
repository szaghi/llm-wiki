---
type: Definition
title: "Laplacian"
description: "The scalar operator ∇²φ = ∇·∇φ: Σ∂²φ/∂x_k² in Cartesians, the scale-factor form in orthogonal coordinates and (1/√g)∂_j(√g g^jk ∂_kφ) in any coordinates; applied to a vector field it acts on basis vectors as well as components outside Cartesian coordinates."
status: established
aliases: [del squared, Laplace operator, vector Laplacian, Laplace-Beltrami operator]
tags: [vector-calculus, operators, curvilinear-coordinates]
timestamp: 2026-10-13T00:00:00Z
---

# Laplacian

**Definition** ([Riley et al. (2006)](/sources/riley-2006.md), eqs. (10.34),
(10.39), pp. 352, 356): $\nabla^2\phi=\nabla\cdot\nabla\phi$, in Cartesians
$\partial^2\phi/\partial x_k\partial x_k$. As a flux,
$\nabla^2\phi=\lim_{V\to0}\frac1V\oint_S\nabla\phi\cdot d\mathbf S$ (p. 400).

**Orthogonal curvilinear** (§10.10, p. 368; Table 10.4):

$$\nabla^2\phi=\frac{1}{h_1h_2h_3}\left[\partial_1\!\left(\frac{h_2h_3}{h_1}\partial_1\phi\right)+\partial_2\!\left(\frac{h_3h_1}{h_2}\partial_2\phi\right)+\partial_3\!\left(\frac{h_1h_2}{h_3}\partial_3\phi\right)\right],$$

obtained by inserting the orthogonal [gradient](/definitions/gradient.md) into
the orthogonal [divergence](/definitions/divergence.md). Cylindrical and
spherical forms: Tables 10.2–10.3; for spherical polars
$\frac{1}{r^2}\partial_r(r^2\partial_r\phi)=\frac1r\partial_r^2(r\phi)$ (p. 363).
Radial functions: $\nabla^2\phi(r)=\dfrac{d^2\phi}{dr^2}+\dfrac2r\dfrac{d\phi}{dr}$, and
$\nabla^2(1/r)=-4\pi\delta(\mathbf x)$ (p. 355).

**General coordinates** (eq. (26.98), p. 974): with the contravariant
components $v^j=g^{jk}\partial_k\phi$ of $\nabla\phi$ in the general divergence,

$$\nabla^2\phi=\frac{1}{\sqrt g}\frac{\partial}{\partial\xi^j}\left(\sqrt g\,g^{jk}\frac{\partial\phi}{\partial\xi^k}\right),$$

which reduces to the orthogonal form with $\sqrt g=h_1h_2h_3$,
$g^{jj}=h_j^{-2}$ (worked example, p. 974). Off-diagonal $g^{jk}$ of a
non-orthogonal system produce mixed derivatives.

**Vector Laplacian.** $\nabla^2\mathbf v$ is defined through
$\nabla\times(\nabla\times\mathbf v)=\nabla(\nabla\cdot\mathbf v)-\nabla^2\mathbf v$
(eq. (10.41), p. 356). Only when the basis vectors are constant (Cartesian
coordinates) does it act component by component,
$(\nabla^2\mathbf v)_i=\nabla^2v_i$ (eq. (10.42)); in cylindrical or
spherical polars the derivatives of the basis vectors contribute, so
$(\nabla^2\mathbf v)_R\ne\nabla^2\hat v_R$ in general (p. 357; exercise 10.18).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§10.7.2, 10.8.2, pp. 352–357; §§10.9–10.10, pp. 360–369; §11.7, p. 400; §26.20, pp. 973–974; exercise 10.18, pp. 372–373.
