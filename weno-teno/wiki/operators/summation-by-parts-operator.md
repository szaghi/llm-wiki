---
type: Operator
title: "Summation-by-parts operator"
description: "A first-derivative matrix D with a symmetric positive-definite norm M is summation-by-parts when MD + DᵀM equals the boundary operator; LGL collocation (DGSEM) has this property with diagonal norm, which yields the strong–weak equivalence, the skew-symmetric flux-differencing operator and the flux form of nodal DG."
status: established
symbol: "$Q+Q^\\top=B$"
aliases: [SBP operator, SBP property, diagonal-norm SBP, generalized SBP, discrete integration by parts]
tags: [dg, entropy-stable, kinetic-energy-preserving, finite-difference]
timestamp: 2026-10-21T00:00:00Z
---

# Summation-by-parts operator

A summation-by-parts (SBP) operator is a discrete first-derivative matrix
whose algebra mimics integration by parts exactly. That property is what lets
nodal DG and finite-difference schemes carry the continuous energy, entropy
and kinetic-energy estimates over to the discrete level. In
one dimension, on the reference element $[-1,1]$ with nodes $\xi_0,\dots,\xi_N$,
let $D$ be the nodal differentiation matrix and $M$ a symmetric
positive-definite norm (mass) matrix. The pair is SBP when $Q=MD$ satisfies

$$Q+Q^\top=B,\qquad B=\mathrm{diag}(-1,0,\dots,0,1).$$

## General definition

[Ranocha et al. (2023)](/sources/ranocha-2023.md) give the multi-dimensional
element-wise definition (Def. 2.2, after Kreiss–Scherer). On an element,
for each direction $d$, the ingredients are:

- a consistent derivative matrix $D_d$;
- a symmetric positive-definite $M$ approximating the $L^2$ inner product of
  the element;
- a restriction $\mathcal R$ from volume to boundary nodes (page-local
  symbol, since $R$ is the eigenvector matrix in this bundle);
- a symmetric positive-definite boundary quadrature $B_\partial$;
- the multiplication $N_d$ by the $d$th component of the outward unit normal.

The pair is SBP when

$$MD_d+D_d^\top M=\mathcal R^\top B_\partial N_d\,\mathcal R .$$

The derivative matrix is *$N$th-order accurate* if it differentiates
monomials of degree $\le N$ exactly, $D\,\boldsymbol\xi^k=k\,\boldsymbol\xi^{k-1}$ for
$k\le N$, and it is *consistent* if $N\ge0$, i.e. $D\mathbf 1=\mathbf 0$ (Def. 2.1).

The following special cases appear in the sources:

- **Diagonal norm, LGL nodes.** Tensor-product Lagrange bases at the
  Legendre–Gauss–Lobatto nodes, with collocated LGL quadrature, are SBP with
  $M=\mathrm{diag}(\mathsf w_j)$, and the nodes include the boundary (Ranocha
  et al. (2023), Ex. 2.3). $\mathcal R$ then selects the boundary nodes, and
  $\mathcal R^\top B_\partial N_d\mathcal R$ is diagonal. In 1D it is exactly
  the matrix $B$ above. This is the [DGSEM](/methods/dgsem.md).
  [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)
  write the same operator as $Q_{ij}=\mathsf w_i\ell_j'(\xi_i)$ with Lagrange
  polynomials $\ell_j$ (page-local), and $B=\mathrm{diag}(-1,0,\dots,0,1)$
  (Eq. (4)).
- **Generalized SBP, Gauss nodes.** Lagrange collocation at Legendre–Gauss
  nodes is also SBP, but the volume nodes exclude the boundary, so
  $\mathcal R$ is a dense interpolation (Ranocha et al. (2023), §6).
  Entropy-stable schemes on these nodes use the *hybridized* SBP operator

  $$Q_{h,d}=\frac12\begin{bmatrix}MD_d-(MD_d)^\top & \mathcal R^\top B_\partial N_d\\ -B_\partial N_d\mathcal R & 0\end{bmatrix},$$

  which acts on volume and surface values together (Eq. (6.2)).
- **Curvilinear SBP.** On a mapped element with Jacobian $J$ and
  contravariant metric terms $Ja^{(n)}_d$, both diagonal at the nodes, the
  physical derivative is
  $D_{d,x}=\tfrac12J^{-1}\sum_n\big(Ja^{(n)}_dD_{n,\xi}+D_{n,\xi}Ja^{(n)}_d\big)$
  (Ranocha et al. (2023), Eq. (2.14)). Here $D_{n,\xi}$ is the reference
  tensor-product operator in direction $n$, and $Ja^{(n)}_d$ is the $d$th
  Cartesian component of $Ja^{(n)}$.

## Consequences used by the sources

1. **Discrete integration by parts.** For nodal vectors $\mathbf u$,
   $\mathbf v$, the 1D identity gives
   $\mathbf u^\top Q\mathbf v+\mathbf v^\top Q\mathbf u=u_Nv_N-u_0v_0$, the
   discrete image of $\int_{-1}^1(uv'+u'v)\,d\xi=[uv]_{-1}^1$ *(compiler
   check, not in the sources: insert $Q+Q^\top=B$)*.
2. **Strong–weak equivalence.** The strong-form DG operator
   $D\mathbf f+M^{-1}B(\mathbf h-\mathbf f)$ equals the weak-form operator
   $-M^{-1}D^\top M\mathbf f+M^{-1}B\mathbf h$ (Ranocha et al. (2023),
   Eqs. (2.3), (2.6)). Here $\mathbf f$ is the vector of nodal fluxes and
   $\mathbf h$ carries the numerical fluxes at the boundary nodes. The
   equivalence is the SBP identity $MD=B-D^\top M$.
3. **Skew-symmetric flux-differencing operator.** With
   $\widetilde D_d=2D_d-M^{-1}\mathcal R^\top B_\partial N_d\mathcal R$, the SBP
   identity gives

   $$M\widetilde D_d=MD_d-D_d^\top M=-(M\widetilde D_d)^\top,$$

   so $(\widetilde D_d)_{ii}=0$ (Ranocha et al. (2023), Eqs. (2.7), (2.11)). In
   1D with LGL nodes, $M\widetilde D=2Q-B$, which is the split-form volume
   matrix $S$ of Rueda-Ramírez et al. (2022), Eq. (4) *(compiler check, not
   in the sources)*. See [flux differencing](/methods/flux-differencing.md).
4. **Flux form and local conservation.** As recalled by Rueda-Ramírez et al.
   (2022) (§2.1, after Fisher & Carpenter), every diagonal-norm SBP
   discretization can be rewritten as differences of inter-node fluxes. This
   is the subcell flux form of the DGSEM, which gives local conservation in
   the sense of the [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)
   and the hinge of
   [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md).
   Ranocha et al. (2023) state the same consequence, for diagonal $M$ and
   diagonal boundary operators, after their Eq. (2.5).
5. **Entropy and kinetic-energy estimates.** Combined with symmetric
   two-point volume fluxes, the SBP property makes the DG scheme
   entropy-conservative or entropy-dissipative when the volume flux is
   [entropy-conservative](/methods/entropy-conservative-flux.md) and the
   surface flux is entropy-conservative or dissipative (Ranocha et al.
   (2023), §2, citing Fisher, Carpenter, Gassner and co-workers). See
   [entropy stability](/properties/entropy-stability.md).

## Relation to periodic finite-difference operators

[Coppola & Veldman (2023)](/sources/coppola-2023.md) build their
conservation theory for periodic grids from banded matrices with vanishing
row and column sums ("double-centred" matrices, §3.2), and they remark in
passing that SBP matrices fit this class. Their equivalence
"global conservation $\Leftrightarrow$ flux form"
([local conservation and flux form](/results/local-conservation-flux-form.md))
is the periodic analogue of consequence 4. The authors point to SBP as the
route to non-periodic boundaries, which they do not treat.

# Citations

- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — Defs. 2.1–2.2, Ex. 2.3, Eqs. (2.3), (2.5)–(2.7), (2.11), (2.14), §6 Eq. (6.2).
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1, Eqs. (3)–(4), (8)–(11).
- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §3.2.
