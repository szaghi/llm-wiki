---
type: Definition
title: "Curl"
description: "The vector field ∇×v, the circulation per unit area about the normal: ε_ijk ∂v_k/∂x_j in Cartesians, a scale-factor determinant in orthogonal coordinates, and (∇×v)^i = (1/√g) ε^ijk ∂v_k/∂ξ^j in any coordinates, where the Christoffel terms cancel."
status: established
aliases: [rot, rotation, vorticity operator, irrotational]
tags: [vector-calculus, operators, curvilinear-coordinates]
timestamp: 2026-10-14T00:00:00Z
---

# Curl

**Cartesian** (eq. (10.35), p. 353): the determinant with rows
$(\mathbf e_1,\mathbf e_2,\mathbf e_3)$, $(\partial_x,\partial_y,\partial_z)$,
$(v_1,v_2,v_3)$; in index form $(\nabla\times\mathbf v)_i=\varepsilon_{ijk}\partial v_k/\partial x_j$
([Levi-Civita symbol](/definitions/levi-civita-symbol.md), p. 943). A field
with $\nabla\times\mathbf v=\mathbf 0$ is **irrotational**. For rigid rotation
$\mathbf u=\boldsymbol\omega\times\mathbf x$, $\nabla\times\mathbf u=2\boldsymbol\omega$
(eq. (10.36), p. 353). Coordinate-free forms: $\nabla\times\mathbf v=\lim_{V\to0}\frac1V\oint_S d\mathbf S\times\mathbf v$
and $(\nabla\times\mathbf v)\cdot\hat{\mathbf n}=\lim_{A\to0}\frac1A\oint_C\mathbf v\cdot d\mathbf x$
(eqs. (11.16)–(11.17), p. 398; [integral definitions](/results/integral-definitions-of-grad-div-curl.md)).
All from [Riley et al. (2006)](/sources/riley-2006.md).
[Arfken et al. (2013)](/sources/arfken-2013.md) (§3.5, eqs. (3.58)–(3.61), pp. 149–152)
give the same determinant and the circulation picture, computing
$\oint\mathbf v\cdot d\mathbf x\approx(\partial_xv_y-\partial_yv_x)\,\Delta x\,\Delta y$
round a small rectangle (eq. (3.60)): the line integral per unit area is
the circulation (vorticity), and a field with zero curl everywhere is
**irrotational** (eq. (3.61)); a central field $\phi(r)\hat{\mathbf x}$ has
zero curl (eq. (3.59)).

**Orthogonal curvilinear** (eq. (10.62), p. 368; physical components):

$$\nabla\times\mathbf v=\frac{1}{h_1h_2h_3}\det\begin{bmatrix}h_1\hat{\mathbf a}_1 & h_2\hat{\mathbf a}_2 & h_3\hat{\mathbf a}_3\\ \partial_1 & \partial_2 & \partial_3\\ h_1\hat v_1 & h_2\hat v_2 & h_3\hat v_3\end{bmatrix},\qquad (\nabla\times\mathbf v)_1=\frac{1}{h_2h_3}\left[\partial_2(h_3\hat v_3)-\partial_3(h_2\hat v_2)\right],$$

proved from $\hat{\mathbf a}_1=h_1\nabla\xi^1$ and $\nabla\times\nabla\xi^1=\mathbf 0$
(pp. 368–369), and again by circulation round a face element (§11.7,
p. 400). Arfken et al. derive the same determinant from the circulation
round a curvilinear face element $h_1h_2\,d\xi^1d\xi^2$, with the $h_i$
again evaluated on the displaced edges (eq. (3.143), pp. 186–187, fig. 3.22).
Cylindrical and spherical forms: Tables 10.2–10.3; Arfken eqs. (3.150),
(3.159). In the orthogonal tables the unit vector $\hat{\mathbf a}_1$ itself
has non-zero divergence and curl, e.g.
$\nabla\cdot\hat{\mathbf a}_1=\partial_1(h_2h_3)/(h_1h_2h_3)$ (Arfken et al.,
exercise 3.10.4, p. 197).

**General coordinates** (§26.20, p. 974). The curl is first defined as the
antisymmetric covariant tensor $(\operatorname{curl}\mathbf v)_{ij}=v_{i;j}-v_{j;i}$,
valid in any dimension; the symmetric Christoffel terms cancel, so
$(\operatorname{curl}\mathbf v)_{ij}=\partial_jv_i-\partial_iv_j$ needs no
[Christoffel symbols](/definitions/christoffel-symbols.md). In three
dimensions the associated vector has contravariant components

$$(\nabla\times\mathbf v)^i=-\frac{1}{2\sqrt g}\varepsilon^{ijk}(\operatorname{curl}\mathbf v)_{jk}=\frac{1}{\sqrt g}\varepsilon^{ijk}\frac{\partial v_k}{\partial\xi^j},$$

with $v_k$ the covariant components; $\varepsilon^{ijk}/\sqrt g$ is an
absolute tensor ([relative tensor](/definitions/relative-tensor.md)).
Arfken et al. give the antisymmetric covariant form only,
$\partial_jv_i-\partial_iv_j=v_{i;j}-v_{j;i}$, with the same cancellation of
the symmetric Christoffel terms (eq. (4.71), p. 225) and the warning that
the $v_i$ are not components on an orthonormal basis; they do not write the
contravariant vector with $\varepsilon^{ijk}/\sqrt g$.

**As a form** (Arfken et al., eqs. (4.87)–(4.88), p. 240): the exterior
derivative of the 1-form $v_k\,dx^k$ is the 2-form with coefficients
$(\nabla\times\mathbf v)_k$ on $dx^2\wedge dx^3$, $dx^3\wedge dx^1$,
$dx^1\wedge dx^2$; its [Hodge star](/definitions/hodge-star.md) is the 1-form
$(\nabla\times\mathbf v)_k\,dx^k$ ([exterior derivative](/definitions/exterior-derivative.md)).

The curl of a gradient vanishes and the divergence of a curl vanishes;
$\nabla\times(\nabla\times\mathbf v)=\nabla(\nabla\cdot\mathbf v)-\nabla^2\mathbf v$
([vector operator identities](/results/vector-operator-identities.md)).
Integrated form: [Stokes' theorem](/results/stokes-theorem.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §10.7.3, p. 353; §10.10, pp. 368–369; §11.7, pp. 398–400; §26.8, p. 943; §26.20, p. 974.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §3.5, pp. 149–152; §3.10, pp. 186–189, 192; §4.3, p. 225; §4.6, p. 240; exercise 3.10.4, p. 197.
