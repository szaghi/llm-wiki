---
type: Definition
title: "General tensor"
description: "A set of quantities whose contravariant (upper) and covariant (lower) indices transform under an arbitrary invertible change of curvilinear coordinates with the factors ∂ξ̄^i/∂ξ^a and ∂ξ^d/∂ξ̄^l respectively; the components on different tensor bases represent one coordinate-free object."
status: established
aliases: [tensor, absolute tensor, contravariant tensor, covariant tensor, mixed tensor, tensor transformation law]
tags: [tensor-calculus, coordinate-transformation]
timestamp: 2026-10-13T00:00:00Z
---

# General tensor

Let $\bar\xi^i=\bar\xi^i(\xi^1,\xi^2,\xi^3)$ be an arbitrary invertible change
of [curvilinear coordinates](/definitions/curvilinear-coordinates.md), not
necessarily linear. The [covariant and contravariant base vectors](/definitions/covariant-and-contravariant-bases.md)
transform as ([Riley et al. (2006)](/sources/riley-2006.md), §26.16,
eqs. (26.66)–(26.70), pp. 960–961)

$$\mathbf a_j=\frac{\partial\bar\xi^i}{\partial\xi^j}\,\bar{\mathbf a}_i,\qquad \mathbf a^j=\frac{\partial\xi^j}{\partial\bar\xi^i}\,\bar{\mathbf a}^i,$$

so the components of a vector must transform as

$$\bar v^i=\frac{\partial\bar\xi^i}{\partial\xi^j}v^j\quad\text{(contravariant)},\qquad \bar v_i=\frac{\partial\xi^j}{\partial\bar\xi^i}v_j\quad\text{(covariant)}.$$

The book takes these two laws as the *defining* properties of contravariant
and covariant vector components (p. 961). A **general tensor** with upper
indices $i,j,\dots,k$ and lower indices $l,m,\dots,n$ is a set of components
transforming as (eq. (26.71), p. 962)

$$\bar T^{ij\cdots k}{}_{lm\cdots n}=\frac{\partial\bar\xi^i}{\partial\xi^a}\frac{\partial\bar\xi^j}{\partial\xi^b}\cdots\frac{\partial\bar\xi^k}{\partial\xi^c}\,\frac{\partial\xi^d}{\partial\bar\xi^l}\frac{\partial\xi^e}{\partial\bar\xi^m}\cdots\frac{\partial\xi^f}{\partial\bar\xi^n}\;T^{ab\cdots c}{}_{de\cdots f}.$$

* For second order the three variants are contravariant $T^{ij}$, mixed
  $T^i{}_j$ and covariant $T_{ij}$, all components of one tensor
  $\mathbf T=T^{ij}\mathbf a_i\otimes\mathbf a_j=T^i{}_j\,\mathbf a_i\otimes\mathbf a^j=T_{ij}\,\mathbf a^i\otimes\mathbf a^j$
  on different tensor bases (§26.14, p. 957; §26.16, p. 962). Indices are
  moved between positions with the [metric tensor](/definitions/metric-tensor.md).
* The mixed Kronecker delta $\delta^i_j$ is a tensor (and isotropic); it is
  the mixed form of the metric (p. 962).
* The algebra (sums, outer products, contraction, the
  [quotient law](/results/quotient-law.md)) carries over from the
  [Cartesian tensor](/definitions/cartesian-tensor.md) case, with
  contraction always between one upper and one lower index (p. 962).
* **Partial derivatives of tensor components are not tensors** in
  non-Cartesian coordinates, because the transformation matrix varies with
  position: $\partial v^i/\partial\xi^j$ picks up a term
  $(\partial\xi^k/\partial\bar\xi^j)(\partial^2\bar\xi^i/\partial\xi^k\partial\xi^l)v^l$
  (eq. (26.84), p. 968). The exception is a scalar, whose gradient
  $\partial\phi/\partial\xi^i$ is a covariant vector. The tensorial
  replacement is the [covariant derivative](/definitions/covariant-derivative.md).
* A tensor whose transformation carries an extra power of the Jacobian is a
  [relative tensor](/definitions/relative-tensor.md); a general tensor is a
  relative tensor of weight 0 ("absolute").
* If all components of a tensor vanish in one coordinate system they vanish
  in all (hint to exercise 26.27, p. 983) — the basis for proving a tensor
  identity in Cartesian coordinates and asserting it in general ones.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §26.14, pp. 955–957; §26.16, pp. 960–963; §26.19, p. 968; exercise 26.27 and hint, pp. 981, 983.
