---
type: Definition
title: "Laplacian"
description: "The scalar operator ∇²φ = ∇·∇φ: Σ∂²φ/∂x_k² in Cartesians, the scale-factor form in orthogonal coordinates and (1/√g)∂_j(√g g^jk ∂_kφ) in any coordinates; applied to a vector field it acts on basis vectors as well as components outside Cartesian coordinates."
status: established
aliases: [del squared, Laplace operator, vector Laplacian, Laplace-Beltrami operator, perpendicular Laplacian, parallel Laplacian]
tags: [vector-calculus, operators, curvilinear-coordinates]
timestamp: 2026-10-16T00:00:00Z
---

# Laplacian

**Definition** ([Riley et al. (2006)](/sources/riley-2006.md), eqs. (10.34),
(10.39), pp. 352, 356; [Arfken et al. (2013)](/sources/arfken-2013.md),
eq. (3.62), p. 154): $\nabla^2\phi=\nabla\cdot\nabla\phi$, in Cartesians
$\partial^2\phi/\partial x_k\partial x_k$. As a flux,
$\nabla^2\phi=\lim_{V\to0}\frac1V\oint_S\nabla\phi\cdot d\mathbf S$ (p. 400).

**Orthogonal curvilinear** (§10.10, p. 368; Table 10.4):

$$\nabla^2\phi=\frac{1}{h_1h_2h_3}\left[\partial_1\!\left(\frac{h_2h_3}{h_1}\partial_1\phi\right)+\partial_2\!\left(\frac{h_3h_1}{h_2}\partial_2\phi\right)+\partial_3\!\left(\frac{h_1h_2}{h_3}\partial_3\phi\right)\right],$$

obtained by inserting the orthogonal [gradient](/definitions/gradient.md) into
the orthogonal [divergence](/definitions/divergence.md); identically in Arfken
et al. (eq. (3.142), p. 186), who note that it "contains no cross
derivatives ... because the coordinate system is orthogonal". Cylindrical and
spherical forms: Tables 10.2–10.3; for spherical polars
$\frac{1}{r^2}\partial_r(r^2\partial_r\phi)=\frac1r\partial_r^2(r\phi)$ (p. 363).
Radial functions: $\nabla^2\phi(r)=\dfrac{d^2\phi}{dr^2}+\dfrac2r\dfrac{d\phi}{dr}$, and
$\nabla^2(1/r)=-4\pi\delta(\mathbf x)$ (p. 355); both also in Arfken et al.
(Example 3.6.1, eqs. (3.120), (3.163), exercise 3.10.34; pp. 154, 177,
192, 202), who stress that the delta-function form is "only meaningful when
inserted into an integral".

**General coordinates** (eq. (26.98), p. 974): with the contravariant
components $v^j=g^{jk}\partial_k\phi$ of $\nabla\phi$ in the general divergence,

$$\nabla^2\phi=\frac{1}{\sqrt g}\frac{\partial}{\partial\xi^j}\left(\sqrt g\,g^{jk}\frac{\partial\phi}{\partial\xi^k}\right),$$

which reduces to the orthogonal form with $\sqrt g=h_1h_2h_3$,
$g^{jj}=h_j^{-2}$ (worked example, p. 974). Arfken et al. derive the same
formula and the same reduction (eq. (4.70), p. 225). Off-diagonal $g^{jk}$ of a
non-orthogonal system produce mixed derivatives.

The same general form is used by the plasma codes of the bundle, with $J$
for $\sqrt g$: [Jiang et al. (2024)](/sources/jiang-2024.md) write
$\nabla\cdot(\phi\nabla_\perp\psi)\approx J^{-1}\partial_i(\phi Jg^{ij}\partial_j\psi)$
with the $\partial_2$ terms dropped (eq. (41), p. 4) and the vorticity as
$\nabla\cdot(v_A^{-2}\nabla_\perp\phi)=J^{-1}\partial_i(Jg^{ij}v_A^{-2}\partial_j\phi)$
(eq. (47), p. 6; $v_A$ the Alfvén speed, local to this formula);
[Seto et al. (2023)](/sources/seto-2023.md) derive it from the conservative
[divergence](/definitions/divergence.md) of the covariant-basis
[gradient](/definitions/gradient.md) (eqs. (A.2)–(A.3), p. 14).

**Perpendicular and parallel Laplacians.** For a field with unit direction
$\hat{\mathbf b}$, Seto et al. (eq. (A.1), p. 14) define
$\nabla_\perp^2\phi=\nabla^2\phi-\nabla_\parallel^2\phi$ with
$\nabla_\parallel^2\phi=\nabla\cdot(\hat{\mathbf b}\,\hat{\mathbf b}\cdot\nabla\phi)$.
In [field-aligned coordinates](/definitions/field-aligned-coordinates.md),
where $\hat{\mathbf b}=\mathbf a_2/\sqrt{g_{22}}$, the parallel part involves
$\partial_2$ only (eq. (A.4), p. 15),

$$\nabla_\parallel^2\phi=\frac{1}{\sqrt g}\,\partial_2\!\left(\frac{\sqrt g}{g_{22}}\,\partial_2\phi\right),\qquad \nabla_\perp^2\phi=\frac{1}{\sqrt g}\,\partial_i\!\left(\sqrt g\,g^{ij}\partial_j\phi\right)-\frac{1}{\sqrt g}\,\partial_2\!\left(\frac{\sqrt g}{g_{22}}\,\partial_2\phi\right),$$

so that in $\nabla_\perp^2$ the coefficient of the $\partial_2\partial_2$ term
is $g^{22}-1/g_{22}$. Seto et al. write it in the quasi-ballooning system of
the [shifted metric](/methods/shifted-metric.md) and in orthogonal
[flux coordinates](/definitions/magnetic-flux-coordinates.md), where the
coefficients become explicit functions of $R$, $h_\vartheta$, $B_{\mathrm p}$,
$B_{\mathrm t}$ and $B$ (eqs. (A.5)–(A.12), (A.21)–(A.28), pp. 15–16); one
printed coefficient has a misprint, recorded on the
[Source page](/sources/seto-2023.md). Dropping the remaining $\partial_2$
terms of $\nabla_\perp^2$ is the flute-ordering approximation, whose error is
discussed on the field-aligned-coordinates page.

**Expanded form for discretization.** Both plasma codes difference the
operator after expanding the outer derivative by the product rule, i.e. as
first- and second-derivative terms with coefficients such as
$(1/\sqrt g)\,\partial_\Psi(\sqrt g\,g^{\Psi\Psi})$ precomputed from the
equilibrium (Seto et al., eqs. (A.5)–(A.6), p. 15; Jiang et al., eq. (52),
p. 8, for a weighted operator of the same structure; [GMEC](/software/gmec.md),
[BOUT++](/software/bout-plus-plus.md)), not in the conservative arrangement
with $\sqrt g\,g^{jk}\partial_k\phi$ differenced as a flux. Neither source
compares the two arrangements.

**Vector Laplacian.** $\nabla^2\mathbf v$ is defined through
$\nabla\times(\nabla\times\mathbf v)=\nabla(\nabla\cdot\mathbf v)-\nabla^2\mathbf v$
(eq. (10.41), p. 356). Only when the basis vectors are constant (Cartesian
coordinates) does it act component by component,
$(\nabla^2\mathbf v)_i=\nabla^2v_i$ (eq. (10.42)); in cylindrical or
spherical polars the derivatives of the basis vectors contribute, so
$(\nabla^2\mathbf v)_R\ne\nabla^2\hat v_R$ in general (p. 357; exercise 10.18).
Arfken et al. take the same identity as the definition (eq. (3.70), p. 155),
state the same restriction to Cartesians, and give the components
explicitly: in cylindrical polars
$(\nabla^2\mathbf v)_R=\nabla^2\hat v_R-\hat v_R/R^2-(2/R^2)\partial_\varphi\hat v_\varphi$,
$(\nabla^2\mathbf v)_\varphi=\nabla^2\hat v_\varphi-\hat v_\varphi/R^2+(2/R^2)\partial_\varphi\hat v_R$,
$(\nabla^2\mathbf v)_z=\nabla^2\hat v_z$ (eq. (3.151), p. 190), and the
spherical components in eq. (3.160) (p. 192).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§10.7.2, 10.8.2, pp. 352–357; §§10.9–10.10, pp. 360–369; §11.7, p. 400; §26.20, pp. 973–974; exercise 10.18, pp. 372–373.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §3.6, pp. 154–155; §3.9, p. 177; §3.10, pp. 186, 189–192; §4.3, p. 225; exercise 3.10.34, p. 202.
* [Jiang et al. (2024)](/sources/jiang-2024.md), §IV A, p. 4; §V A, p. 6; §VII A, p. 8.
* [Seto et al. (2023)](/sources/seto-2023.md), App. A, pp. 14–16.
