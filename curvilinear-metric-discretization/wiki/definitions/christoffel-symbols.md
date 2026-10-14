---
type: Definition
title: "Christoffel symbols"
description: "The coefficients Γ^k_ij of the derivatives of the covariant base vectors, ∂_j a_i = Γ^k_ij a_k, symmetric in i and j, computable from the metric as Γ^m_ij = ½ g^mk(∂_i g_jk + ∂_j g_ki − ∂_k g_ij); they vanish in Cartesian coordinates and are not the components of a tensor."
status: established
aliases: [Christoffel symbol of the second kind, Christoffel symbol of the first kind, connection coefficients, affine connection]
symbol: "$\\Gamma^k_{ij}$"
tags: [tensor-calculus, metric, christoffel]
timestamp: 2026-10-14T00:00:00Z
---

# Christoffel symbols

In a general coordinate system the
[base vectors](/definitions/covariant-and-contravariant-bases.md) vary with
position. The **Christoffel symbol of the second kind** $\Gamma^k_{ij}$ is
defined by expanding the derivative of a covariant base vector on the
covariant basis ([Riley et al. (2006)](/sources/riley-2006.md), §26.18,
eqs. (26.75)–(26.77), p. 965):

$$\frac{\partial\mathbf a_i}{\partial\xi^j}=\Gamma^k_{ij}\,\mathbf a_k,\qquad \Gamma^k_{ij}=\mathbf a^k\cdot\frac{\partial\mathbf a_i}{\partial\xi^j},\qquad \frac{\partial\mathbf a^i}{\partial\xi^j}=-\Gamma^i_{kj}\,\mathbf a^k.$$

The third relation follows by differentiating $\mathbf a^i\cdot\mathbf a_j=\delta^i_j$.
[Arfken et al. (2013)](/sources/arfken-2013.md) define the symbols by the same expansion and
solve for them with the reciprocal basis (§4.3, eqs. (4.53)–(4.54),
p. 222), writing the differentiation index first in the lower pair; by the
symmetry below the two index orders give the same numbers (see the
[Arfken notation map](/sources/arfken-2013.md)).

## Properties stated in the source

1. **Cartesian coordinates**: $\Gamma^k_{ij}=0$ for all indices (p. 965).
2. **Symmetry**: $\Gamma^k_{ij}=\Gamma^k_{ji}$, because
   $\partial_j\mathbf a_i=\partial^2\mathbf x/\partial\xi^j\partial\xi^i=\partial_i\mathbf a_j$
   (p. 966; Arfken et al., p. 222 and exercise 4.3.4).
3. **Metric formula** (eq. (26.82), p. 967): from
   $\partial_k g_{ij}=\Gamma^l_{ik}g_{lj}+\Gamma^l_{jk}g_{il}$ (eq. (26.79)) and
   its two cyclic permutations,
   $$\Gamma^m_{ij}=\tfrac12 g^{mk}\left(\frac{\partial g_{jk}}{\partial\xi^i}+\frac{\partial g_{ki}}{\partial\xi^j}-\frac{\partial g_{ij}}{\partial\xi^k}\right).$$
   Arfken et al. reach the same formula through the symbol of the first kind
   (eqs. (4.59)–(4.63), pp. 223–224), recommending it as more convenient
   than the base-vector definition.
4. **Not a tensor**: under $\xi\mapsto\bar\xi$ (eq. (26.78), p. 966),
   $$\bar\Gamma^k_{ij}=\frac{\partial\bar\xi^k}{\partial\xi^l}\frac{\partial^2\xi^l}{\partial\bar\xi^j\partial\bar\xi^i}+\frac{\partial\bar\xi^k}{\partial\xi^n}\frac{\partial\xi^l}{\partial\bar\xi^i}\frac{\partial\xi^m}{\partial\bar\xi^j}\Gamma^n_{lm};$$
   the first, inhomogeneous term spoils the tensor law. Arfken et al. state
   that neither $\Gamma^k_{ij}$ nor $\partial v^k/\partial\xi^j$ is
   individually a tensor, only their combination in the
   [covariant derivative](/definitions/covariant-derivative.md) (p. 223), and
   that the first kind is "not a third-rank tensor" either (p. 223).
5. **Contracted symbol** (§26.20, eqs. (26.92)–(26.96), pp. 972–973): using
   $\partial_k g=g\,g^{ij}\partial_k g_{ij}$ (derivative of a determinant,
   eq. (26.96)),
   $$\Gamma^i_{ki}=\tfrac12 g^{il}\frac{\partial g_{il}}{\partial\xi^k}=\frac{1}{2g}\frac{\partial g}{\partial\xi^k}=\frac{1}{\sqrt g}\frac{\partial\sqrt g}{\partial\xi^k}.$$
   This identity turns the covariant divergence into the conservative form
   of the [divergence](/definitions/divergence.md). Arfken et al. derive it
   identically (eqs. (4.66)–(4.68), p. 225), noting that two of the three
   metric-derivative terms cancel by renaming dummy indices.
6. **First kind** (exercise 26.29, p. 982): $\Gamma_{kij}=g_{kl}\Gamma^l_{ij}=\tfrac12(\partial_j g_{ik}+\partial_i g_{jk}-\partial_k g_{ij})$,
   with $\partial_k g_{ij}=\Gamma_{ijk}+\Gamma_{jik}$. Arfken et al. define
   the first kind as $g_{mk}\Gamma^m_{ij}=\mathbf a_k\cdot\partial_j\mathbf a_i$,
   prove the same derivative relation and the same formula
   (eqs. (4.59)–(4.61), pp. 223–224); their bracket symbol is mapped to
   $\Gamma_{kij}$ in the notation map.

The symbols enter the [covariant derivative](/definitions/covariant-derivative.md),
the absolute derivative along a curve and the geodesic equation
$d^2\xi^i/ds^2+\Gamma^i_{jk}(d\xi^j/ds)(d\xi^k/ds)=0$ (eq. (26.101), p. 977),
which in Euclidean space describes straight lines.

## Example

Cylindrical polars $(\xi^1,\xi^2,\xi^3)=(R,\varphi,z)$: the only non-zero
symbols are $\Gamma^2_{12}=\Gamma^2_{21}=1/R$ and $\Gamma^1_{22}=-R$, obtained
both from the base-vector derivatives and from the metric formula
(eq. (26.83), p. 967). Arfken et al. set the cylindrical case as an exercise
with the note "there are only three nonvanishing $\Gamma$" (exercise 4.3.8,
p. 226), consistent with these three. Spherical polars are exercise 26.26.
"The apparatus ... becomes unnecessary in Cartesian coordinates, because the
basis vectors have vanishing derivatives" (Arfken et al., p. 224).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §26.18, pp. 965–967; §26.20, pp. 972–973; §26.22, p. 977; exercises 26.26, 26.29, pp. 981–982.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §4.3, pp. 222–225; exercises 4.3.4, 4.3.8, p. 226.
