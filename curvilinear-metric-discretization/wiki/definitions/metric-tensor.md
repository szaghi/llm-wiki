---
type: Definition
title: "Metric tensor"
description: "The symmetric second-order tensor g_ij = a_i·a_j (with inverse g^ij = a^i·a^j and determinant g) that completely characterises a curvilinear coordinate system at each point: it gives arc length, volume element, scalar products, and raises and lowers indices."
status: established
aliases: [metric, fundamental tensor, covariant metric tensor, contravariant metric tensor, metric coefficients g_ij]
symbol: "$g_{ij}$"
tags: [metric, tensor-calculus, curvilinear-coordinates]
timestamp: 2026-10-16T00:00:00Z
---

# Metric tensor

"Any particular curvilinear coordinate system is completely characterised at
each point in space by the nine quantities" ([Riley et al. (2006)](/sources/riley-2006.md),
§26.15, eq. (26.56), p. 957)

$$g_{ij}=\mathbf a_i\cdot\mathbf a_j,$$

the covariant components of the symmetric second-order **metric tensor**
$\mathbf g$, where $\mathbf a_i$ are the
[covariant base vectors](/definitions/covariant-and-contravariant-bases.md).
[Arfken et al. (2013)](/sources/arfken-2013.md) give the same definition twice: in Cartesian form,
$g_{ij}=\sum_k(\partial x^k/\partial\xi^i)(\partial x^k/\partial\xi^j)$ with
$(ds)^2=g_{ij}d\xi^id\xi^j$ (§3.10, eqs. (3.128)–(3.129), p. 184: "spaces
with a measure of distance given by Eq. (3.128) are called metric or
Riemannian"), and as $g_{ij}=\mathbf a_i\cdot\mathbf a_j$ (§4.3,
eqs. (4.39)–(4.40), p. 219), "called the covariant metric tensor".

## Properties stated in the source

1. **Arc length** (eq. (26.57); Arfken eqs. (3.128), (4.39)): $(ds)^2=d\mathbf x\cdot d\mathbf x=g_{ij}\,d\xi^i d\xi^j$.
2. **Volume element** (eq. (26.58)): $dV=\sqrt g\,d\xi^1d\xi^2d\xi^3$ with
   $g=\det[g_{ij}]$; equivalently $\lvert\mathbf a_1\cdot(\mathbf a_2\times\mathbf a_3)\rvert=\sqrt g$
   (p. 959, "it may be shown"; exercise 26.25). See [Jacobian](/definitions/jacobian.md).
3. **Contravariant components** $g^{ij}=\mathbf a^i\cdot\mathbf a^j$, and
   $[g^{ij}]=[g_{ij}]^{-1}$, i.e. $g^{ik}g_{kj}=\delta^i_j$ (eq. (26.65),
   proved from index raising and lowering on an arbitrary vector, pp. 958–959).
   Arfken et al. instead *define* $g^{ij}$ as the inverse (eq. (4.41)) and
   prove $g^{ij}=\mathbf a^i\cdot\mathbf a^j$ (eqs. (4.46)–(4.47), p. 220).
   The mixed components are $\delta^i_j$ (p. 960).
4. **Scalar product** (eqs. (26.61)–(26.64)):
   $\mathbf v\cdot\mathbf w=g_{ij}v^iw^j=g^{ij}v_iw_j=v^iw_i=v_iw^i$
   (Arfken eq. (4.48), p. 221).
5. **Raising and lowering**: $v_i=g_{ij}v^j$, $v^i=g^{ij}v_j$, and for any
   tensor, e.g. $T_{ij}=g_{ik}g_{jl}T^{kl}$, $T^{ij}=g^{ik}g^{jl}T_{kl}$
   (pp. 959, 963, eqs. (26.72)–(26.73); Arfken eqs. (4.42)–(4.43), p. 219).
6. **Tensor character**: $g_{ij}$ transforms covariantly,
   $\bar g_{ij}=\dfrac{\partial\xi^k}{\partial\bar\xi^i}\dfrac{\partial\xi^l}{\partial\bar\xi^j}g_{kl}$,
   and $g^{ij}$ contravariantly (worked example, p. 963). Arfken et al.
   obtain the tensor character from the invariance of $(ds)^2$ by the
   [quotient law](/results/quotient-law.md) (p. 219; exercise 4.1.10,
   p. 215). Its determinant is
   a relative scalar of weight 2, $\bar g=\lvert\partial\xi/\partial\bar\xi\rvert^2g$
   (p. 964; see [relative tensor](/definitions/relative-tensor.md)).
7. **Orthogonal systems**: $g_{ij}=h_i^2\delta_{ij}$ (no sum), $g=h_1^2h_2^2h_3^2$
   ([scale factors](/definitions/scale-factors.md); p. 957; Arfken
   eqs. (3.130), (3.131) and exercise 4.3.2).
8. **Metric compatibility**: the [covariant derivative](/definitions/covariant-derivative.md)
   of the metric vanishes identically, $g_{ij;k}=0$ in every coordinate system
   (exercise 26.29, p. 982, stated as an exercise with a hint, p. 983;
   also $g^{ij}{}_{;k}=0$, Arfken exercise 4.3.10, p. 226).
9. Its derivatives determine the [Christoffel symbols](/definitions/christoffel-symbols.md),
   eq. (26.82) (Arfken eq. (4.63)).

## Example

Cylindrical polars $(R,\varphi,z)$: $[g_{ij}]=\operatorname{diag}(1,R^2,1)$,
$[g^{ij}]=\operatorname{diag}(1,R^{-2},1)$, $(ds)^2=(dR)^2+R^2(d\varphi)^2+(dz)^2$,
$dV=R\,dR\,d\varphi\,dz$ (eqs. (26.59)–(26.60), pp. 958–960). Spherical polars
are exercise 26.26 in Riley; Arfken et al. work them out,
$[g_{ij}]=\operatorname{diag}(1,r^2,r^2\sin^2\theta)$ and
$[g^{ij}]=\operatorname{diag}(1,r^{-2},(r\sin\theta)^{-2})$ from the
explicit $\mathbf a_i$ and $\mathbf a^i$ (Example 4.3.1, pp. 220–221);
cylindrical is their exercise 4.3.5.

## Inverse by cofactors

In a code that stores one metric and needs the other, the inverse is
computed from cofactors. [Liu et al. (2024)](/sources/liu-2024.md)
(eq. (27), p. 5) obtain the covariant field-aligned metric from the
contravariant one this way, with $J^2=g=1/\det[g^{ij}]$. With unrestricted
sums over the indices the formula reads

$$g_{il}=\tfrac12\,J^2\,\varepsilon_{ijk}\,\varepsilon_{lmn}\,g^{jm}g^{kn},$$

the adjugate of $[g^{ij}]$ divided by its determinant (compiler's statement
of the normalisation, hypothesis-grade). Liu et al. print
$J^2\sum\varepsilon_{ijk}\varepsilon_{lmn}(g^{jm}g^{kn}-g^{jn}g^{km})$, which
equals this only if the sums run over $j<k$ and $m<n$; with unrestricted sums
it is four times larger (see the [Source page](/sources/liu-2024.md)).

## Non-orthogonal example: field-aligned coordinates

In [field-aligned coordinates](/definitions/field-aligned-coordinates.md)
the metric is non-orthogonal even when the parent
[flux coordinates](/definitions/magnetic-flux-coordinates.md) are
orthogonal: $g^{13}=\nabla\Psi\cdot\nabla\varphi-I\lvert\nabla\Psi\rvert^2-q_{\mathrm{loc}}\nabla\Psi\cdot\nabla\vartheta$
([Jiang et al. (2024)](/sources/jiang-2024.md), eq. (27), p. 3), and the
components carrying the integrated shear $I$ grow along the field and jump
across the twist-shift boundary, which the [shifted metric](/methods/shifted-metric.md)
is designed to remove. The orthogonal flux-surface metric of
[Seto et al. (2023)](/sources/seto-2023.md) (eqs. (1)–(3), p. 2) is
diagonal, $g_{\Psi\Psi}=1/g^{\Psi\Psi}$ and so on, the case of property 7.

## Qualification: sign of the diagonal elements

Arfken et al. write that $g_{ij}$, "though manifestly symmetric, is not
required to be diagonal, and its elements (including those on the diagonal)
may be of either sign" (p. 219), and give the Minkowski metric
$\operatorname{diag}(1,-1,-1,-1)$, for which $(ds)^2$ need not be positive
(Example 4.3.1, p. 221). The remark concerns general metric (pseudo-Riemannian)
spaces. In the Euclidean setting of this bundle, where $g_{ij}=\mathbf a_i\cdot\mathbf a_j$
as both books define it, $g_{ii}=\lvert\mathbf a_i\rvert^2=h_i^2>0$ (no sum)
and $[g_{ij}]$ is positive definite (compiler's remark, immediate from the
definition). A difference of scope, not a contradiction.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §26.15, pp. 957–960; §26.16, p. 963; §26.17, p. 964; exercises 26.25, 26.26, 26.29, pp. 981–982.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §3.10, p. 184; §4.3, pp. 218–221, 224; exercises 4.1.10, 4.3.2, 4.3.5, 4.3.10, pp. 215, 226.
* [Jiang et al. (2024)](/sources/jiang-2024.md), §III A–B, p. 3.
* [Liu et al. (2024)](/sources/liu-2024.md), §II C–D, pp. 3, 5.
* [Seto et al. (2023)](/sources/seto-2023.md), §2, p. 2.
