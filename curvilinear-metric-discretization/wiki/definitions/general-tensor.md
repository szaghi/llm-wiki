---
type: Definition
title: "General tensor"
description: "A set of quantities whose contravariant (upper) and covariant (lower) indices transform under an arbitrary invertible change of curvilinear coordinates with the factors ∂ξ̄^i/∂ξ^a and ∂ξ^d/∂ξ̄^l respectively; the components on different tensor bases represent one coordinate-free object."
status: established
aliases: [tensor, absolute tensor, contravariant tensor, covariant tensor, mixed tensor, tensor transformation law]
tags: [tensor-calculus, coordinate-transformation]
timestamp: 2026-10-14T00:00:00Z
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

Riley takes these two laws as the *defining* properties of contravariant
and covariant vector components (p. 961), and so do [Arfken et al. (2013)](/sources/arfken-2013.md)
(§4.1, eqs. (4.4)–(4.5), pp. 206–207), who motivate them by a vector and a
gradient: in Cartesian frames the two coefficients $\partial\bar\xi^i/\partial\xi^j$
and $\partial\xi^j/\partial\bar\xi^i$ coincide, and they differ as soon as
non-Cartesian systems enter (p. 206). Arfken et al. call the number of
indices the **rank** (Riley: order). A **general tensor** with upper
indices $i,j,\dots,k$ and lower indices $l,m,\dots,n$ is a set of components
transforming as (eq. (26.71), p. 962)

$$\bar T^{ij\cdots k}{}_{lm\cdots n}=\frac{\partial\bar\xi^i}{\partial\xi^a}\frac{\partial\bar\xi^j}{\partial\xi^b}\cdots\frac{\partial\bar\xi^k}{\partial\xi^c}\,\frac{\partial\xi^d}{\partial\bar\xi^l}\frac{\partial\xi^e}{\partial\bar\xi^m}\cdots\frac{\partial\xi^f}{\partial\bar\xi^n}\;T^{ab\cdots c}{}_{de\cdots f}.$$

* For second order the three variants are contravariant $T^{ij}$, mixed
  $T^i{}_j$ and covariant $T_{ij}$, all components of one tensor
  $\mathbf T=T^{ij}\mathbf a_i\otimes\mathbf a_j=T^i{}_j\,\mathbf a_i\otimes\mathbf a^j=T_{ij}\,\mathbf a^i\otimes\mathbf a^j$
  on different tensor bases (§26.14, p. 957; §26.16, p. 962; Arfken et al.,
  eq. (4.6), p. 207). Indices are moved between positions with the
  [metric tensor](/definitions/metric-tensor.md).
* The mixed Kronecker delta $\delta^i_j$ is a tensor (and isotropic); it is
  the mixed form of the metric (p. 962). Arfken et al. prove its tensor law
  by the chain rule, "independent of the number of dimensions"
  (eqs. (4.14)–(4.15), p. 209).
* The algebra (sums, outer products, contraction, the
  [quotient law](/results/quotient-law.md)) carries over from the
  [Cartesian tensor](/definitions/cartesian-tensor.md) case, with
  contraction always between one upper and one lower index (p. 962).
  Arfken et al. prove that contracting a mixed second-rank tensor gives a
  scalar (eq. (4.16), p. 210), that a direct (outer) product is a tensor of
  summed rank and summed co/contravariant character (eq. (4.17), p. 210),
  and the inverse law $v^i=(\partial\xi^i/\partial\bar\xi^j)\bar v^j$, warning
  that $\partial\xi^i/\partial\bar\xi^j\neq(\partial\bar\xi^j/\partial\xi^i)^{-1}$
  because the derivatives hold different variables fixed; only the summed
  product cancels (eqs. (4.18)–(4.19), p. 211).
* **Partial derivatives of tensor components are not tensors** in
  non-Cartesian coordinates, because the transformation matrix varies with
  position: $\partial v^i/\partial\xi^j$ picks up a term
  $(\partial\xi^k/\partial\bar\xi^j)(\partial^2\bar\xi^i/\partial\xi^k\partial\xi^l)v^l$
  (eq. (26.84), p. 968). The exception is a scalar, whose gradient
  $\partial\phi/\partial\xi^i$ is a covariant vector. The tensorial
  replacement is the [covariant derivative](/definitions/covariant-derivative.md).
  Arfken et al. state the same (exercise 4.1.7 note, p. 214; p. 222) and
  caution that direct products involving $\nabla$, such as $\nabla\mathbf v$,
  have simple transformation rules only in Cartesian systems (pp. 210–211).
* A tensor whose transformation carries an extra power of the Jacobian is a
  [relative tensor](/definitions/relative-tensor.md); a general tensor is a
  relative tensor of weight 0 ("absolute").
* If all components of a tensor vanish in one coordinate system they vanish
  in all (hint to exercise 26.27, p. 983; Arfken et al., exercise 4.1.1,
  p. 213, and exercise 4.1.2: tensors equal in one system are equal in all)
  — the basis for proving a tensor identity in Cartesian coordinates and
  asserting it in general ones.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §26.14, pp. 955–957; §26.16, pp. 960–963; §26.19, p. 968; exercise 26.27 and hint, pp. 981, 983.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §4.1, pp. 205–214; §4.3, p. 222; exercises 4.1.1, 4.1.2, 4.1.7, pp. 213–214.
