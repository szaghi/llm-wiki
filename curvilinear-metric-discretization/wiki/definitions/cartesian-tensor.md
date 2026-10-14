---
type: Definition
title: "Cartesian tensor"
description: "A set of 3^N quantities whose values transform under every rotation of Cartesian axes x'_i = L_ij x_j like products of N coordinates, T'_ij…k = L_ip L_jq … L_kr T_pq…r; scalars, vectors and second-order tensors are orders 0, 1, 2, closed under addition, outer product and contraction."
status: established
aliases: [Cartesian tensors, first-order tensor, second-order tensor, tensor of order N, rank, outer product, contraction]
tags: [tensor-calculus, cartesian-tensors]
timestamp: 2026-10-13T00:00:00Z
---

# Cartesian tensor

Restricting coordinate changes to rigid rotations of Cartesian axes, with
orthogonal matrix $L$ (components of $\mathbf x$ in the rotated frame
$x'_i=L_{ij}x_j$, $x_i=L_{ji}x'_j$, $L_{ik}L_{jk}=L_{ki}L_{kj}=\delta_{ij}$,
$L_{ij}=\mathbf e'_i\cdot\mathbf e_j$), a set of quantities $T_{ij\cdots k}$
with $N$ subscripts forms the components of an **$N$th-order Cartesian
tensor** if, for all rotations,
([Riley et al. (2006)](/sources/riley-2006.md), §§26.3–26.5,
eqs. (26.4)–(26.6), (26.18)–(26.19), pp. 930–935)

$$T'_{ij\cdots k}=L_{ip}L_{jq}\cdots L_{kr}T_{pq\cdots r},\qquad T_{ij\cdots k}=L_{pi}L_{qj}\cdots L_{rk}T'_{pq\cdots r}.$$

In three dimensions it has $3^N$ components. Order 0 is a scalar (invariant
under rotation, e.g. $\mathbf v\cdot\mathbf w=v_iw_i$, p. 934), order 1 a
vector ($v'_i=L_{ij}v_j$, eq. (26.9)). The tensor itself is basis-free:
$\mathbf v=v_i\mathbf e_i=v'_i\mathbf e'_i$ and
$\mathbf T=T_{ij}\,\mathbf e_i\otimes\mathbf e_j=T'_{ij}\,\mathbf e'_i\otimes\mathbf e'_j$
(eqs. (26.10), (26.23)). Under a rotation the matrix of a second-order tensor
transforms as $\mathbf T'=L\mathbf TL^{\mathsf T}$ like a linear operator, but
not every linear operator is a second-order tensor: both indices must refer
to the same coordinate system, so $L_{ij}$ itself is not one (p. 936).

## Algebra (§26.6, pp. 938–939)

* Sums and differences of tensors of equal order are tensors; so is a tensor
  with two indices interchanged. Any tensor splits into a part symmetric and
  a part antisymmetric in a chosen pair of indices.
* **Outer product**: an $N$th-order and an $M$th-order tensor give an
  $(N+M)$th-order tensor, e.g. $T_{ij}=v_iw_j$, $\mathbf T=\mathbf v\otimes\mathbf w$
  (eqs. (26.20)–(26.22)).
* **Contraction**: setting two indices equal and summing lowers the order by
  two (worked proof, p. 939); the trace $T_{ii}$ is a scalar.
* The **gradient of a vector**, $T_{ij}=\partial v_i/\partial x_j$, is a
  second-order tensor, $\mathbf T=\nabla\mathbf v$ (p. 937); the divergence
  $\partial v_i/\partial x_i$ is a scalar (worked example, p. 935).
* A set is shown to be a tensor most easily by the
  [quotient law](/results/quotient-law.md) or by recognising an outer
  product, rather than by direct substitution (p. 937).

## Special tensors

* $\delta_{ij}$ and $\varepsilon_{ijk}$ ([Levi-Civita symbol](/definitions/levi-civita-symbol.md))
  are **isotropic**: their components are the same in every rotated frame.
  To within a scalar multiple they are the only isotropic tensors of orders 2
  and 3, and the only isotropic first-order tensor is zero (§26.9, pp. 944–946,
  proved by two specific rotations). The general fourth-order isotropic
  tensor $\lambda\delta_{ij}\delta_{kl}+\eta\delta_{ik}\delta_{jl}+\nu\delta_{il}\delta_{jk}$
  is assumed, not proved (eq. (26.47), p. 953).
* Under improper rotations ($\det L=-1$) **pseudotensors** acquire an extra
  factor $\det L$ (eq. (26.39)); $\varepsilon_{ijk}$ is a pseudotensor and
  $\varepsilon_{ijk}b_jc_k$ a pseudovector (§26.10, pp. 946–948). The
  general-coordinate counterpart is the [relative tensor](/definitions/relative-tensor.md).

Cartesian tensors are the special case, for rigid rotations, of the
[general tensor](/definitions/general-tensor.md): for a rotation
$\partial x^j/\partial x'^i=\partial x'^i/\partial x^j=L_{ij}$ and the
contravariant and covariant laws coincide (pp. 961–962).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§26.1–26.10, pp. 928–948; §26.12, pp. 950–954; §26.16, pp. 961–962.
