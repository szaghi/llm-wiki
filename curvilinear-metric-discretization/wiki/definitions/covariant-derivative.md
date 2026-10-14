---
type: Definition
title: "Covariant derivative"
description: "The tensorial derivative of tensor components in general coordinates, v^i_;j = ∂_j v^i + Γ^i_kj v^k and v_i;j = ∂_j v_i − Γ^k_ij v_k, which accounts for the variation of the base vectors (∂_j v = v^i_;j a_i), reduces to the partial derivative in Cartesians and annihilates the metric."
status: established
aliases: [semicolon derivative, absolute derivative, intrinsic derivative, covariant differentiation, nabla v]
tags: [tensor-calculus, operators, christoffel]
timestamp: 2026-10-13T00:00:00Z
---

# Covariant derivative

Partial derivatives of tensor components are not tensors in general
coordinates ([general tensor](/definitions/general-tensor.md), eq. (26.84)).
Differentiating $\mathbf v=v^i\mathbf a_i$ and expanding $\partial_j\mathbf a_i$
with the [Christoffel symbols](/definitions/christoffel-symbols.md) gives
([Riley et al. (2006)](/sources/riley-2006.md), §26.19, eqs. (26.85)–(26.88),
pp. 968–970)

$$\frac{\partial\mathbf v}{\partial\xi^j}=v^i{}_{;j}\,\mathbf a_i,\qquad v^i{}_{;j}=\frac{\partial v^i}{\partial\xi^j}+\Gamma^i_{kj}v^k,\qquad v_{i;j}=\frac{\partial v_i}{\partial\xi^j}-\Gamma^k_{ij}v_k.$$

The $v^i{}_{;j}$ are the mixed components of a second-order tensor
$\nabla\mathbf v$ (by the [quotient law](/results/quotient-law.md), or
directly from eqs. (26.84) and (26.78)); in Cartesians they reduce to
$\partial v^i/\partial x^j$. Comma notation: $v^i{}_{,j}=\partial v^i/\partial\xi^j$.

**Second-order tensors** (p. 971): one Christoffel term per index, with $+$
for each upper and $-$ for each lower index,

$$T^{ij}{}_{;k}=T^{ij}{}_{,k}+\Gamma^i_{lk}T^{lj}+\Gamma^j_{lk}T^{il},\quad T^i{}_{j;k}=T^i{}_{j,k}+\Gamma^i_{lk}T^l{}_j-\Gamma^l_{jk}T^i{}_l,\quad T_{ij;k}=T_{ij,k}-\Gamma^l_{ik}T_{lj}-\Gamma^l_{jk}T_{il},$$

the components of one third-order tensor $\nabla\mathbf T$. **Scalars**:
$\phi_{;j}=\phi_{,j}$ (eq. (26.90)).

## Properties

* **Metric compatibility**: $g_{ij;k}=0$ in every coordinate system
  (exercise 26.29, p. 982; hint p. 983).
* **Commutation in Euclidean space**: the commutator defines the Riemann
  tensor, $v_{i;jk}-v_{i;kj}=R^l{}_{ijk}v_l$ with
  $R^l{}_{ijk}=\partial_j\Gamma^l_{ik}-\partial_k\Gamma^l_{ij}+\Gamma^m_{ik}\Gamma^l_{mj}-\Gamma^m_{ij}\Gamma^l_{mk}$;
  it vanishes in Cartesians and therefore in every coordinate system of
  three-dimensional Euclidean space, so covariant derivatives commute there
  (exercise 26.27, p. 981).
* **Vector operators**: the contraction $v^i{}_{;i}$ is the
  [divergence](/definitions/divergence.md), the antisymmetrised $v_{i;j}-v_{j;i}$
  the [curl](/definitions/curl.md) (§26.20).

## Absolute derivative along a curve

Along a curve $\xi^i(t)$ (§26.21, eq. (26.99), pp. 975–976):

$$\frac{d\mathbf v}{dt}=\frac{\delta v^i}{\delta t}\mathbf a_i,\qquad \frac{\delta v^i}{\delta t}=\frac{dv^i}{dt}+\Gamma^i_{jk}v^j\frac{d\xi^k}{dt}=v^i{}_{;k}\frac{d\xi^k}{dt},$$

and analogously for covariant and higher-order components. Setting the
absolute derivative of the unit tangent to zero gives the geodesic equation
$d^2\xi^i/ds^2+\Gamma^i_{jk}(d\xi^j/ds)(d\xi^k/ds)=0$ (eq. (26.101),
p. 977), straight lines in Euclidean space; with a non-affine parameter $t$
the right side becomes $(\ddot s/\dot s)\,d\xi^i/dt$ (exercise 26.28).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§26.19–26.22, pp. 968–977; exercises 26.27–26.29, pp. 981–982.
