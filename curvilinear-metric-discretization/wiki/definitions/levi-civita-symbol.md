---
type: Definition
title: "Levi-Civita symbol"
description: "The totally antisymmetric permutation symbol ε_ijk (+1, −1, 0 for even, odd, repeated index permutations of 1,2,3), which writes determinants, cross products and curls in index form and satisfies the contraction identity ε_ijk ε_klm = δ_il δ_jm − δ_im δ_jl."
status: established
aliases: [permutation symbol, alternating tensor, epsilon tensor, epsilon-delta identity, Kronecker delta]
symbol: "$\\varepsilon_{ijk}$"
tags: [tensor-calculus, cartesian-tensors, identities]
timestamp: 2026-10-13T00:00:00Z
---

# Levi-Civita symbol

$$\varepsilon_{ijk}=\begin{cases}+1 & (i,j,k)\ \text{an even permutation of }(1,2,3),\\ -1 & \text{an odd permutation},\\ 0 & \text{otherwise.}\end{cases}$$

It is totally antisymmetric, and any totally antisymmetric three-index
quantity is a scalar multiple of it ([Riley et al. (2006)](/sources/riley-2006.md),
§26.8, p. 941). Together with the Kronecker delta $\delta_{ij}$ it is an
isotropic [Cartesian tensor](/definitions/cartesian-tensor.md) under proper
rotations; strictly it is a pseudotensor, and in general coordinates a
[relative tensor](/definitions/relative-tensor.md) of weight $-1$
($\varepsilon^{ijk}$: $+1$) (§§26.8, 26.10, 26.17).

## Identities stated in the source

* **Determinant** (eq. (26.29), p. 942): $\lvert A\rvert\,\varepsilon_{lmn}=A_{li}A_{mj}A_{nk}\varepsilon_{ijk}$,
  extended in a footnote to $N\times N$ matrices.
* **Contraction identity** (eq. (26.30), proved by cases, p. 943):
  $$\varepsilon_{ijk}\varepsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl},$$
  a special case of the determinant form (eq. (26.34))
  $\varepsilon_{ijk}\varepsilon_{pqr}=\det\begin{bmatrix}\delta_{ip}&\delta_{iq}&\delta_{ir}\\ \delta_{jp}&\delta_{jq}&\delta_{jr}\\ \delta_{kp}&\delta_{kq}&\delta_{kr}\end{bmatrix}$,
  with the further contractions $\varepsilon_{ijk}\varepsilon_{ilm}=\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl}$,
  $\varepsilon_{ijk}\varepsilon_{ijm}=2\delta_{km}$ and $\varepsilon_{ijk}\varepsilon_{ijk}=6$
  (eqs. (26.35)–(26.36), p. 944).
* **Vector operations in index form** (Cartesian, right-handed axes; p. 943):
  $(\mathbf b\times\mathbf c)_i=\varepsilon_{ijk}b_jc_k$,
  $(\nabla\times\mathbf v)_i=\varepsilon_{ijk}\,\partial v_k/\partial x_j$,
  $(\mathbf v\times\mathbf w)\cdot\mathbf c=\varepsilon_{ikl}c_iv_kw_l$,
  $\nabla^2\phi=\delta_{ij}\,\partial^2\phi/\partial x_i\partial x_j$.
* **Double curl** (worked example, p. 944): with the contraction identity,
  $[\nabla\times(\nabla\times\mathbf v)]_i=\partial_i(\partial_j v_j)-\nabla^2v_i$,
  i.e. eq. (10.41) in Cartesian components.

The book recommends these identities as "a quick method" of proving the
[vector operator identities](/results/vector-operator-identities.md) (§10.8,
p. 354; exercise 26.6). The tensor forms of the Stokes and divergence
theorems also use it ([Stokes' theorem](/results/stokes-theorem.md)).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §26.8, pp. 941–944; §26.10, pp. 947–948; §26.17, p. 964; exercise 26.6, p. 978.
