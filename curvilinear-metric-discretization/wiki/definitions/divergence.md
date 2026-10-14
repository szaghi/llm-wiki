---
type: Definition
title: "Divergence"
description: "The scalar field ∇·v, the net outflux per unit volume: ∂v^k/∂x^k in Cartesians, (1/h1h2h3)Σ∂(h_j h_k v̂_i)/∂ξ^i in orthogonal coordinates, and v^i_;i = (1/√g)∂(√g v^j)/∂ξ^j in any coordinates."
status: established
aliases: [div, Voss-Weyl formula, conservative form of the divergence, solenoidal]
tags: [vector-calculus, operators, curvilinear-coordinates, conservation-form]
timestamp: 2026-10-13T00:00:00Z
---

# Divergence

**Cartesian** (eq. (10.33), p. 352): $\nabla\cdot\mathbf v=\partial v_k/\partial x_k$,
a scalar under rotations (worked example, p. 935). A field with
$\nabla\cdot\mathbf v=0$ is **solenoidal**. For a fluid velocity $\nabla\cdot\mathbf u$
is "the net rate of outflow of fluid per unit volume" at a point (p. 352);
the coordinate-free statement is
$\nabla\cdot\mathbf v=\lim_{V\to0}\frac1V\oint_S\mathbf v\cdot d\mathbf S$
(eq. (11.15), p. 398; [integral definitions](/results/integral-definitions-of-grad-div-curl.md)).
All from [Riley et al. (2006)](/sources/riley-2006.md).

**Orthogonal curvilinear**, physical components
$\mathbf v=\sum_i\hat v_i\hat{\mathbf a}_i$ (eq. (10.61), p. 367):

$$\nabla\cdot\mathbf v=\frac{1}{h_1h_2h_3}\left[\frac{\partial}{\partial\xi^1}(h_2h_3\hat v_1)+\frac{\partial}{\partial\xi^2}(h_3h_1\hat v_2)+\frac{\partial}{\partial\xi^3}(h_1h_2\hat v_3)\right].$$

Two proofs are given: (i) writing $\hat{\mathbf a}_1=h_2h_3\nabla\xi^2\times\nabla\xi^3$
and using $\nabla\cdot(\nabla\xi^2\times\nabla\xi^3)=0$ (eq. (10.43),
[vector operator identities](/results/vector-operator-identities.md)) (p. 368);
(ii) the flux through the six faces of the element
$h_1h_2h_3\Delta\xi^1\Delta\xi^2\Delta\xi^3$ (§11.7, p. 399). Cylindrical:
$\frac1R\partial_R(R\hat v_R)+\frac1R\partial_\varphi\hat v_\varphi+\partial_z\hat v_z$
(Table 10.2); spherical: Table 10.3.

**General coordinates** (§26.20, eqs. (26.92)–(26.97), pp. 972–973): replacing
partial by [covariant derivatives](/definitions/covariant-derivative.md),
$\nabla\cdot\mathbf v=v^i{}_{;i}=\partial_iv^i+\Gamma^i_{ki}v^k$, and the
contracted [Christoffel symbol](/definitions/christoffel-symbols.md)
$\Gamma^i_{ki}=\partial_k\sqrt g/\sqrt g$ gives

$$\nabla\cdot\mathbf v=\frac{1}{\sqrt g}\frac{\partial}{\partial\xi^j}\left(\sqrt g\,v^j\right),$$

valid for non-orthogonal systems, with $v^j$ the contravariant components
(not the physical ones; $v^j=\hat v_j/h_j$ in orthogonal systems, which
recovers eq. (10.61)). The book checks the cylindrical case,
$v^i{}_{;i}=\frac1R\partial_R(Rv^R)+\partial_\varphi v^\varphi+\partial_zv^z$
(p. 970). The left form ($\partial_iv^i+\Gamma^i_{ki}v^k$) and the right form
($\sqrt g$ inside the derivative) are equal in the continuum; the second is
the "conservative" arrangement, in which the divergence is a derivative of a
flux-like quantity $\sqrt g\,v^j$.

*Compiler's derivation (hypothesis-grade; not in the source).* With
$v^j=\mathbf v\cdot\mathbf a^j$ and $\sqrt g=\lvert J\rvert$, the general
form reads $\nabla\cdot\mathbf v=\frac{1}{\sqrt g}\partial_j(\sqrt g\,\mathbf a^j\cdot\mathbf v)$.
For a constant field $\mathbf c$, $\nabla\cdot\mathbf c=0$, so
$\partial_j(\sqrt g\,\mathbf a^j)=\mathbf 0$ identically — the continuum
identity on which the conservative form rests; the same follows from
$\sqrt g\,\mathbf a^1=\pm\mathbf a_2\times\mathbf a_3$ by symmetry of second
derivatives. No source of the bundle yet states it or discusses its
discrete counterpart.

Integrated form: the [divergence theorem](/results/divergence-theorem.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §10.7.2, p. 352; §10.9, p. 360; §10.10, pp. 367–369; §11.7, pp. 398–399; §26.4, p. 935; §§26.19–26.20, pp. 969–973.
