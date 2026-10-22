---
type: Property
title: "Free-stream preservation"
description: "A discretization on curvilinear grids is free-stream preserving when a uniform state stays an exact discrete steady solution, which requires discrete metric identities; the page records the DGSEM metric treatment, the subcell metric identities of Hennemann et al. and their reformulation as Pazner's conservation condition, and the untested free-stream claim made for interpolation-based TENO."
status: established
aliases: [freestream preservation, free-stream preserving, discrete metric identities, geometric conservation law, GCL, watertight subcell discretization]
tags: [dg, finite-difference, limiting]
timestamp: 2026-10-21T00:00:00Z
---

# Free-stream preservation

On a curvilinear grid the physical fluxes enter the scheme combined with
the metric terms, the Jacobian $J$ and the contravariant metric terms
$Ja^{(n)}$. A scheme is **free-stream preserving** when every constant state
remains an exact discrete steady solution, so that the metric discretization
creates no spurious residual. In the sources the property is secured by
discrete *metric identities*, algebraic conditions on the discrete metric
terms that make the residual of a constant state vanish.

## Nodal DG

In the [DGSEM](/methods/dgsem.md), the metric terms are computed at the LGL
nodes by applying the derivative matrix to the node coordinates
([Ranocha et al. (2023)](/sources/ranocha-2023.md), Eqs. (2.12)–(2.13)).
They enter the curvilinear SBP operator
$D_{d,x}=\tfrac12J^{-1}\sum_n\big(Ja^{(n)}_dD_{n,\xi}+D_{n,\xi}Ja^{(n)}_d\big)$
(Eq. (2.14)). In [flux differencing](/methods/flux-differencing.md) they are
averaged between node pairs in the two-point flux, as
$\{\!\{Ja^{(n)}\}\!\}_{(i,m)}$ (Eq. (2.17);
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md),
Eq. (6)). Ranocha et al. reorder the sums into directional volume fluxes.
They note that free-stream preservation "still requires the usual care"
with the metric terms and cite the literature for it rather than proving it
(§2.3).

## Subcell metric identities

The [subcell finite-volume](/methods/subcell-finite-volume-limiting.md)
scheme that is blended with the DGSEM needs its own normals. Without them,
it would neither be watertight nor preserve free streams on high-order
curved elements. Rueda-Ramírez et al. (2022) recall the normals of Hennemann
et al., derived from the subcell flux form of the DGSEM (§2.2, Eq. (14)). In
the first direction, on grid line $j$, they read

$$n_{(i,i+1)j}=(Ja^{(1)})_{0j}+\sum_{l=0}^{i}\sum_{m=0}^{N}Q_{lm}(Ja^{(1)})_{mj},$$

with $Q=MD$ the SBP matrix, and similarly in the second direction. These
unnormalized subcell-interface normals (page-local symbol $n_{(a,b)}$) give
free-stream preservation and satisfy the discrete subcell metric identities

$$\frac{n_{(i-1,i)j}-n_{(i,i+1)j}}{\mathsf w_i}+\frac{n_{i(j-1,j)}-n_{i(j,j+1)}}{\mathsf w_j}=0 .$$

The source obtains these identities by evaluating a constant state in the
subcell scheme (Eq. (15)). The proof is in Hennemann et al., as recalled.
The finite-volume flux through each subcell face is
$\lVert n_{(a,b)}\rVert\,h\big(u_a,u_b;n_{(a,b)}/\lVert n_{(a,b)}\rVert\big)$
(Eq. (13)). For a constant state, consistency of $h$ reduces the residual
to $f(u)$ dotted into the left-hand side of the identity. The residual
therefore vanishes exactly when the identity holds *(compiler check, not in
the sources)*.

**Proposition 2** (Rueda-Ramírez et al. (2022), §3, Eqs. (35)–(36)). In
Pazner's sparse invariant-domain-preserving DG method, the modified metric
terms must satisfy a conservation condition, $\sum_{j\in N(i)}\hat c_{ij}=0$
over the low-order stencil (page-local graph coefficients $\hat c$). With
$\hat c$ built from the Hennemann et al. normals, that sum is
$\tfrac12\mathsf w_i\mathsf w_j$ times the left-hand side of the subcell metric
identity. The Hennemann et al. normals are therefore exact analytic
solutions of Pazner's condition, and the singular-value-decomposition
minimisation Pazner used to find the modified metrics is unnecessary.
The authors present this as a simplification of Pazner's construction, not
a correction.

## Finite-difference reconstruction schemes

[Ye et al. (2022)](/sources/ye-2022.md) argue that [AFTENO](/methods/afteno.md)
has an advantage over flux-splitting TENO. Because it interpolates states
and evaluates a two-point flux plus derivative corrections, they claim it
keeps free streams better (§1, §4.2, §5). They also say the extra cost of
the interpolation-based flux, about three times TENO5, buys this property.
The paper contains no curvilinear-grid test, so the claim is untested in
the source.

## Qualifications

- None of the three sources proves free-stream preservation itself. Ranocha
  et al. (2023) and Rueda-Ramírez et al. (2022) cite it from the literature
  for the DGSEM and the subcell normals. Ye et al. (2022) assert it without
  a test. The page records the conditions and their algebraic relations,
  which are stated or proved in the sources.

# Citations

- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1 Eq. (6), §2.2 Eqs. (13)–(15), §3 Prop. 2 Eqs. (35)–(36).
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §2.3 Eqs. (2.12)–(2.19).
- [Ye et al. (2022)](/sources/ye-2022.md) — §1, §4.2, §5.
