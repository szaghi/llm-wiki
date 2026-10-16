---
type: Definition
title: "Covariant and contravariant bases"
description: "The two natural, generally non-unit and non-orthogonal bases of a curvilinear system — tangents a_i = ∂x/∂ξ^i to the coordinate curves and normals a^i = ∇ξ^i to the coordinate surfaces — which are reciprocal (a_i·a^j = δ_i^j) and define the contravariant and covariant components of a vector."
status: established
aliases: [tangent basis, normal basis, reciprocal basis, covariant base vectors, contravariant base vectors, contravariant components, covariant components, physical components]
tags: [curvilinear-coordinates, tensor-calculus, metric]
timestamp: 2026-10-16T00:00:00Z
---

# Covariant and contravariant bases

At every point of a system of
[general curvilinear coordinates](/definitions/curvilinear-coordinates.md)
there are two natural sets of basis vectors
([Riley et al. (2006)](/sources/riley-2006.md), §10.10, pp. 364–367;
§26.14, eqs. (26.52)–(26.55), pp. 955–956; [Arfken et al. (2013)](/sources/arfken-2013.md),
§4.3, eqs. (4.37), (4.44), pp. 218–220, who call them the covariant and
contravariant basis vectors):

$$\mathbf a_i=\frac{\partial\mathbf x}{\partial\xi^i}\quad\text{(covariant base vectors)},\qquad \mathbf a^i=\nabla\xi^i\quad\text{(contravariant base vectors)}.$$

* $\mathbf a_i$ is tangent to the $\xi^i$ coordinate curve, in the direction
  of increasing $\xi^i$; $\mathbf a^i$ is normal to the coordinate surface
  $\xi^i=$ const (§10.10, pp. 364, 366).
* In general neither set is of unit length nor orthogonal (§26.14, p. 955).
* The two sets are **reciprocal**:
  $$\mathbf a_i\cdot\mathbf a^j=\delta^j_i,$$
  proved by the chain rule, $\mathbf a_i\cdot\nabla\xi^j=\sum_k(\partial x^k/\partial\xi^i)(\partial\xi^j/\partial x^k)=\partial\xi^j/\partial\xi^i$
  (§10.10, worked example, pp. 366–367; eq. (26.54); Arfken et al.,
  eq. (4.45), p. 220, by the same chain rule). Equivalently, the
  matrix of metric coefficients $[\partial\xi^i/\partial x^j]$ is the inverse
  of the Jacobian matrix $[\partial x^i/\partial\xi^j]$.
* Each basis follows from the other by cross products: for $(i,j,k)$ a cyclic
  permutation of $(1,2,3)$,
  $$\mathbf a^i=\frac{\mathbf a_j\times\mathbf a_k}{\mathbf a_i\cdot(\mathbf a_j\times\mathbf a_k)}=\frac{\mathbf a_j\times\mathbf a_k}{J},$$
  with a similar expression for $\mathbf a_i$ in terms of the $\mathbf a^i$
  (§26.15, p. 959; Arfken et al., exercise 4.3.1, p. 226, for a right-handed
  but not necessarily orthogonal triad, noting that the $\mathbf a^i$ are the
  reciprocal lattice of Example 3.2.1, eqs. (3.15)–(3.17), pp. 129–130). The
  second equality uses
  $J=\mathbf a_1\cdot(\mathbf a_2\times\mathbf a_3)$, the
  [Jacobian](/definitions/jacobian.md) (cyclic invariance of the triple
  product).
* Each basis is obtained from the other with the
  [metric tensor](/definitions/metric-tensor.md):
  $\mathbf a^i=g^{ij}\mathbf a_j$, $\mathbf a_i=g_{ij}\mathbf a^j$ (§26.15,
  p. 959; Arfken et al., pp. 219–220, proving $g^{ij}=\mathbf a^i\cdot\mathbf a^j$,
  eq. (4.47)).
* Unit versions: $\hat{\mathbf a}_i=\mathbf a_i/h_i$ (tangent) and
  $\hat{\mathbf a}^i=\nabla\xi^i/\lvert\nabla\xi^i\rvert$ (normal). The two
  unit bases coincide when the system is orthogonal; then
  $\nabla\xi^i=\hat{\mathbf a}_i/h_i$ (§10.10, pp. 366–367). The book
  states the "if" direction ("it may be shown that the two bases become
  identical if the coordinate system is orthogonal") and proves it through
  $\nabla\xi^i=\hat{\mathbf a}_i/h_i$. Arfken et al. define the orthogonal-system
  unit vectors as the normals to the coordinate surfaces (p. 183) and then
  use $\partial\mathbf x/\partial\xi^i=h_i\hat{\mathbf a}_i$ (eq. (3.132),
  p. 184), which presupposes the same coincidence; for an orthogonal set
  $\lvert\mathbf a^i\rvert=1/\lvert\mathbf a_i\rvert$ (exercise 4.3.2).
* In Cartesian coordinates the two bases coincide with $\mathbf e_k$, which is
  why the covariant/contravariant distinction is invisible there (§26.14,
  p. 956; Arfken et al., pp. 206–207: the two transformation laws coincide
  only in Cartesian systems).

## Components of a vector

A vector $\mathbf v$ has **contravariant components** $v^i$ and **covariant
components** $v_i$ (§10.10, p. 366; §26.14, p. 956):

$$\mathbf v=v^i\mathbf a_i=v_i\mathbf a^i,\qquad v^i=\mathbf v\cdot\mathbf a^i,\qquad v_i=\mathbf v\cdot\mathbf a_i.$$

Arfken et al. (eqs. (4.38), (4.43), pp. 218–219) stress that $\mathbf v$ is
a fixed object while its components and the basis change "in mutually
inverse ways" under a change of coordinates, and that calling the set $v^i$
"a vector" is a linguistic shortcut.

The **physical components** $\hat v_i$ on a unit basis differ from both; for
an orthogonal system $v^i=\hat v_i/h_i$ (no sum) (§26.20, p. 972). The tensor
forms of the vector operators ([divergence](/definitions/divergence.md),
[curl](/definitions/curl.md)) are written in $v^i$ or $v_i$, the orthogonal
tables in $\hat v_i$; mixing them is the commonest error when comparing the
two (Riley makes the distinction explicit at §26.20, p. 972; Arfken et al.
at p. 225: the covariant components "are coefficients of the possibly
nonunit" contravariant base vectors "and are therefore not components" of
the vector "in the orthonormal basis"; and $\hat v_k=h_kv^k$ (no sum)).

## Change of basis under a coordinate shift

When one coordinate is shifted by a function of the others, both bases
change in the reciprocal pattern. For
[field-aligned coordinates](/definitions/field-aligned-coordinates.md)
$\xi^3=\varphi-\chi(\Psi,\vartheta)$ built on
[flux coordinates](/definitions/magnetic-flux-coordinates.md), the
contravariant vector $\mathbf a^3=\nabla\varphi-I\nabla\Psi-q_{\mathrm{loc}}\nabla\vartheta$
gains terms while $\mathbf a^1,\mathbf a^2$ do not, and the covariant vectors
$\mathbf a_1=\mathbf a_\Psi+I\mathbf a_\varphi$, $\mathbf a_2=\mathbf a_\vartheta+q_{\mathrm{loc}}\mathbf a_\varphi$
gain terms while $\mathbf a_3$ does not
([Jiang et al. (2024)](/sources/jiang-2024.md), eqs. (16)–(22), p. 3;
[Seto et al. (2023)](/sources/seto-2023.md), eq. (7), p. 3). Seto et al.'s
quasi-ballooning representation mixes the two systems, taking
$(\mathbf a_\Psi,\mathbf a_2,\mathbf a_3)$ as covariant and
$(\nabla\Psi,\nabla\vartheta,\nabla\varphi-q_{\mathrm{loc}}\nabla\vartheta)$
as contravariant basis, which are again reciprocal (eqs. (12)–(13), p. 3;
[shifted metric](/methods/shifted-metric.md)). The angle between two
contravariant vectors follows from the metric,
$\cos\alpha_{12}=g^{12}/\sqrt{g^{11}g^{22}}$, which
[Liu et al. (2024)](/sources/liu-2024.md) use to place gyro-average points
in the non-orthogonal grid (eq. (14), p. 4; $\alpha_{12}$ local to this
sentence).

The derivatives of the base vectors along the coordinates define the
[Christoffel symbols](/definitions/christoffel-symbols.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §10.10, pp. 364–367; §§26.14–26.15, pp. 955–960; §26.20, p. 972.
* [Arfken et al. (2013)](/sources/arfken-2013.md), Example 3.2.1, pp. 129–130; §3.10, pp. 183–184; §4.1, pp. 206–207; §4.3, pp. 218–220, 225; exercises 4.3.1–4.3.3, p. 226.
* [Jiang et al. (2024)](/sources/jiang-2024.md), §III A, p. 3.
* [Liu et al. (2024)](/sources/liu-2024.md), §II C, p. 4.
* [Seto et al. (2023)](/sources/seto-2023.md), §2, p. 3.
