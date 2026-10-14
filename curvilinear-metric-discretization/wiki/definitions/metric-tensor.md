---
type: Definition
title: "Metric tensor"
description: "The symmetric second-order tensor g_ij = a_i·a_j (with inverse g^ij = a^i·a^j and determinant g) that completely characterises a curvilinear coordinate system at each point: it gives arc length, volume element, scalar products, and raises and lowers indices."
status: established
aliases: [metric, fundamental tensor, covariant metric tensor, contravariant metric tensor, metric coefficients g_ij]
symbol: "$g_{ij}$"
tags: [metric, tensor-calculus, curvilinear-coordinates]
timestamp: 2026-10-13T00:00:00Z
---

# Metric tensor

"Any particular curvilinear coordinate system is completely characterised at
each point in space by the nine quantities" ([Riley et al. (2006)](/sources/riley-2006.md),
§26.15, eq. (26.56), p. 957)

$$g_{ij}=\mathbf a_i\cdot\mathbf a_j,$$

the covariant components of the symmetric second-order **metric tensor**
$\mathbf g$, where $\mathbf a_i$ are the
[covariant base vectors](/definitions/covariant-and-contravariant-bases.md).

## Properties stated in the source

1. **Arc length** (eq. (26.57)): $(ds)^2=d\mathbf x\cdot d\mathbf x=g_{ij}\,d\xi^i d\xi^j$.
2. **Volume element** (eq. (26.58)): $dV=\sqrt g\,d\xi^1d\xi^2d\xi^3$ with
   $g=\det[g_{ij}]$; equivalently $\lvert\mathbf a_1\cdot(\mathbf a_2\times\mathbf a_3)\rvert=\sqrt g$
   (p. 959, "it may be shown"; exercise 26.25). See [Jacobian](/definitions/jacobian.md).
3. **Contravariant components** $g^{ij}=\mathbf a^i\cdot\mathbf a^j$, and
   $[g^{ij}]=[g_{ij}]^{-1}$, i.e. $g^{ik}g_{kj}=\delta^i_j$ (eq. (26.65),
   proved from index raising and lowering on an arbitrary vector, pp. 958–959).
   The mixed components are $\delta^i_j$ (p. 960).
4. **Scalar product** (eqs. (26.61)–(26.64)):
   $\mathbf v\cdot\mathbf w=g_{ij}v^iw^j=g^{ij}v_iw_j=v^iw_i=v_iw^i$.
5. **Raising and lowering**: $v_i=g_{ij}v^j$, $v^i=g^{ij}v_j$, and for any
   tensor, e.g. $T_{ij}=g_{ik}g_{jl}T^{kl}$, $T^{ij}=g^{ik}g^{jl}T_{kl}$
   (pp. 959, 963, eqs. (26.72)–(26.73)).
6. **Tensor character**: $g_{ij}$ transforms covariantly,
   $\bar g_{ij}=\dfrac{\partial\xi^k}{\partial\bar\xi^i}\dfrac{\partial\xi^l}{\partial\bar\xi^j}g_{kl}$,
   and $g^{ij}$ contravariantly (worked example, p. 963). Its determinant is
   a relative scalar of weight 2, $\bar g=\lvert\partial\xi/\partial\bar\xi\rvert^2g$
   (p. 964; see [relative tensor](/definitions/relative-tensor.md)).
7. **Orthogonal systems**: $g_{ij}=h_i^2\delta_{ij}$ (no sum), $g=h_1^2h_2^2h_3^2$
   ([scale factors](/definitions/scale-factors.md); p. 957).
8. **Metric compatibility**: the [covariant derivative](/definitions/covariant-derivative.md)
   of the metric vanishes identically, $g_{ij;k}=0$ in every coordinate system
   (exercise 26.29, p. 982, stated as an exercise with a hint, p. 983).
9. Its derivatives determine the [Christoffel symbols](/definitions/christoffel-symbols.md),
   eq. (26.82).

## Example

Cylindrical polars $(R,\varphi,z)$: $[g_{ij}]=\operatorname{diag}(1,R^2,1)$,
$[g^{ij}]=\operatorname{diag}(1,R^{-2},1)$, $(ds)^2=(dR)^2+R^2(d\varphi)^2+(dz)^2$,
$dV=R\,dR\,d\varphi\,dz$ (eqs. (26.59)–(26.60), pp. 958–960). Spherical polars
are exercise 26.26.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §26.15, pp. 957–960; §26.16, p. 963; §26.17, p. 964; exercises 26.25, 26.26, 26.29, pp. 981–982.
