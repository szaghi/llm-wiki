---
type: Operator
title: "Summation-by-parts operator"
description: "A first-derivative matrix D with a symmetric positive-definite norm M is summation-by-parts when MD + DᵀM equals the boundary operator; LGL collocation (DGSEM) has this property with diagonal norm, which yields the strong–weak equivalence, the skew-symmetric flux-differencing operator, the flux form of nodal DG and its entropy proofs, and sparse low-order SBP operators on quadrilaterals and triangles."
status: established
symbol: "$Q+Q^\\top=B$"
aliases: [SBP operator, SBP property, diagonal-norm SBP, generalized SBP, hybridized SBP operator, discrete integration by parts]
tags: [dg, entropy-stable, kinetic-energy-preserving, finite-difference]
timestamp: 2026-10-23T19:58:00Z
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
  (Eq. (4)). [Pazner (2021)](/sources/pazner-2021.md) calls $Q$ the
  *weighted* differentiation matrix, on the reference interval $[0,1]$, and
  states its two defining sums as Prop. 1:
  - (P1) every row sums to zero, $\sum_jQ_{ij}=0$, because
    $\sum_j\ell_j\equiv1$; this is conservation;
  - (P2) the column sums are $-1$ for the first node, $+1$ for the last and
    $0$ otherwise, because LGL quadrature is exact for degree $2N-1$; this
    is the SBP property.

  [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) list the
  same identities, $\sum_kQ_{jk}=0$ and $\sum_jQ_{jk}=\delta_{kN}-\delta_{k0}$,
  next to $Q+Q^\top=B$ (Eqs. (107)–(110)). In several dimensions the
  operators are Kronecker products, e.g. $M\otimes Q$ and $Q\otimes M$ in
  2D (Pazner (2021), Eq. (9)).
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
- **Diagonal-norm finite-difference SBP.** On a grid of points the
  derivative is $D=M^{-1}Q$ with a diagonal positive norm $M$ that is a
  quadrature, $\mathbf 1^\top M\mathbf x^k\approx(x_R^{k+1}-x_L^{k+1})/(k+1)$,
  and a boundary operator $B$ with $\mathbf 1^\top B\mathbf x^k=x_R^k-x_L^k$;
  multi-dimensional operators are tensor products
  ([Edoh (2022)](/sources/edoh-2022.md), §2, Eqs. (1)–(2)). Because a
  diagonal norm commutes with diagonal data matrices $A=\mathrm{diag}(\mathbf a)$,
  the SBP property gives the integrated discrete product rule
  $$\mathbf 1^\top M\big(\mathrm{diag}(\mathbf a)D\mathbf b+\mathrm{diag}(\mathbf b)D\mathbf a\big)=\mathbf a^\top B\mathbf b=a_Rb_R-a_Lb_L,$$
  the identity behind every kinetic-energy proof of split forms (Eq. (2)). Edoh
  leaves out boundary and interface simultaneous-approximation terms.
  [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) run a
  sixth-order SBP finite-difference scheme on the periodic 2D Taylor–Green
  vortex (App. A.3) and write nodal DG in the general element-wise form
  above, $MD_j+D_j^\top M=\mathcal R^\top B_\partial N_j\mathcal R$ (§2.2,
  Eq. (20)); they note that a single-block finite-difference or Fourier
  collocation scheme is a one-element DG scheme in this sense (Example 2.12).
- **Stiffness operator with dense norms.**
  [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md)
  use the stiffness matrix $Q_{ij}=\int\chi_i\,\partial_\xi\chi_j$ of a
  modal or nodal basis $\{\chi_i\}$ (page-local) evaluated by a quadrature
  exact to degree at least $2N-1$. It satisfies
  $Q+Q^\top=\sum_{\text{faces}}V_f^\top W_f\,n_f\,V_f$, with page-local face
  interpolation $V_f$, face weights $W_f$ and reference normal $n_f$,
  whatever the collocation of solution and quadrature nodes and with a
  dense mass matrix (Eq. (24)). Earlier nonlinear-stability proofs for
  split forms relied on a diagonal norm, which commutes with the diagonal
  solution matrix; splitting with respect to $Q$ instead of $D$ is what
  lets them prove energy stability of an uncollocated, overintegrated or
  modal flux-reconstruction split form (§3;
  [flux reconstruction](/methods/flux-reconstruction.md)).
- **Sparsified first-order operator.** Pazner (2021), Eq. (23), replaces
  $Q$ by the weighted differentiation matrix $\widehat Q$ of the
  piecewise-linear hat functions on the LGL subgrid. It is tridiagonal with
  entries $\pm\tfrac12$: first row $(-\tfrac12,\tfrac12,0,\dots)$, interior
  rows $(\dots,-\tfrac12,0,\tfrac12,\dots)$, last row $(\dots,0,-\tfrac12,\tfrac12)$
  (the last row is implied, not printed). It is first-order accurate, and
  Pazner states that it satisfies (P1) and (P2). Hence
  $\widehat Q+\widehat Q^\top=B$ holds exactly, with the same $B$, so
  $\widehat D=M^{-1}\widehat Q$ is itself a first-order SBP operator for
  the LGL norm *(compiler check, not in the sources: add the tridiagonal
  matrix to its transpose)*. Its stencil has $O(1)$ width for every $N$,
  which is what keeps Pazner's graph-viscosity low-order scheme from
  growing more diffusive with $N$ (§3, Fig. 1;
  [convex limiting](/methods/convex-limiting.md)). On curved elements it
  needs corrected metric terms
  ([free-stream preservation](/properties/free-stream-preservation.md)).

- **Multidimensional diagonal-norm SBP on triangles and a sparse
  low-order companion.** [Lin, Chan & Tomas (2023)](/sources/lin-2023.md)
  use nodal SBP operators on quadrilaterals and triangles whose volume
  quadrature, with positive weights and exact for degree $2N-1$, contains
  an $(N+1)$-point Gauss–Lobatto face quadrature exact for degree $2N$;
  with the 0/1 face-extraction matrix $E$ and $B_r=\mathrm{diag}(\text{face weights}\times\hat n_r)$
  (page-local $E$, $B_r$ for reference direction $r$), the property reads
  $Q_r+Q_r^\top=E^\top B_rE$ (§3.1, Eq. (5); arXiv v2). For their
  positivity-preserving low-order scheme they need a sparse operator
  $Q^{\mathrm L}_r$ with the same SBP property and $Q^{\mathrm L}_r\mathbf 1=0$
  (Eqs. (7)–(8)):
  - on tensor-product elements, Pazner's piecewise-linear operator above,
    $I\otimes\widehat Q$ and $\widehat Q\otimes I$;
  - on simplices, a new construction. A diagonal-norm SBP operator is fixed
    by its skew-symmetric part, $Q_r=\tfrac12(Q_r-Q_r^\top)+\tfrac12E^\top B_rE$
    (Eqs. (9)–(10)), so they prescribe the sparsity of the skew part from an
    adjacency graph of the nodes (two nodes adjacent when closer than a
    multiple of a power of their quadrature weights, Eq. (11)) and write its
    entries as differences of a page-local potential vector $\mathsf p$,
    $(Q^{\mathrm L}_r-Q^{\mathrm L\top}_r)_{jk}/2=\mathsf p_k-\mathsf p_j$ on
    edges, after Wu, Trask & Chan. The conservation condition then becomes
    the graph-Laplacian system $\mathsf L\mathsf p=\tfrac12E^\top B_rE\,\mathbf 1$
    with zero-mean $\mathsf p$, which has a unique solution (§3.2) *(compiler
    check, not in the sources: the row sum of the skew part at node $j$ is
    $-(\mathsf L\mathsf p)_j$)*.

  The adjacency parameters are "not optimal" and the results "not
  sensitive" to them (§8). Sparsifying keeps the low-order scheme from
  becoming more diffusive as $N$ grows: at 600 degrees of freedom its
  Leblanc solutions at $N=2$ and $N=5$ nearly coincide (§5, Table 1a,
  Fig. 3), the multi-dimensional, simplex counterpart of Pazner's
  observation. On curved meshes both operators stay SBP and conservative if
  the geometric terms satisfy a discrete GCL (App. A;
  [free-stream preservation](/properties/free-stream-preservation.md)).

- **Hybridized operators for nodes without the boundary.** On
  Legendre–Gauss nodes the volume nodes exclude the faces, and Schwarz et
  al. extend entropy-stable collocation to them through a generalized SBP
  property (§3.4). They recall that the diagonal mass matrix needed for the LGL operator is
  exact on Gauss nodes but a lumping on LGL nodes, because Gauss quadrature
  integrates degree $2N+1$ exactly and LGL only $2N-1$
  ([Schwarz et al. (2025)](/sources/schwarz-2025.md), §3.1, §3.3). They
  print the LGL property as $Q+Q^\top=V_f^\top B$ with the face
  interpolation $V_f$; the square, conforming form is
  $Q+Q^\top=V_f^\top BV_f$, which is the registry's $B$ on LGL nodes, where
  $V_f$ is the 0/1 extraction *(compiler check, not in the sources)*. Entropy-stable Gauss collocation therefore
  uses Chan's hybridized (generalized) SBP operator coupling volume and face
  nodes,
  $Q_{\mathrm h}=\begin{pmatrix}2MD-V_f^\top BV_f&V_f^\top B\\-BV_f&B\end{pmatrix}$
  in one direction (Eq. (23); page-local $Q_{\mathrm h}$, $V_f$, and
  $B=\mathrm{diag}(-1,1)$ on the two faces), together with an
  [entropy projection](/methods/entropy-projection.md) of the face states
  (Eqs. (24)–(25); see [flux differencing](/methods/flux-differencing.md)).
  [Cicchino & Nadarajah (2025)](/sources/cicchino-2025.md) use the modal
  counterpart for flux reconstruction on curvilinear hexahedra: their
  discrete integration by parts holds for any quadrature exact to degree
  $2N-1$ (Eq. (22)), and the hybridized skew-symmetric operator
  $\tilde Q-\tilde Q^\top$ on volume and surface quadrature nodes satisfies
  $\tilde Q+\tilde Q^\top=\mathrm{blockdiag}\big(0,\ \mathsf W_f\,\mathrm{diag}(n_f)\big)$,
  page-local $\mathsf W_f$ the surface weights and $n_f$ the reference
  normals (Eqs. (38)–(39)). This SBP-like property cancels the surface
  terms in their free-stream proof and gives local conservation through
  skew-symmetry (Thms. 6.1–6.2;
  [flux reconstruction](/methods/flux-reconstruction.md)).
- **Over-integrated LGL nodes with a modal projection.**
  [Liu et al. (2025b)](/sources/liu-2025-b.md) (§3.1, Eqs. (3.4)–(3.8))
  use, after Chen & Shu, $k_q+1\ge k+1$ LGL nodes for degree-$k$
  polynomials, with $k_q=k+2$ in their tests. In page-local notation,
  $\mathsf V$ is the $(k_q+1)\times(k+1)$ Legendre Vandermonde matrix at the
  nodes, $\mathsf P=\hat M^{-1}\mathsf V^\top M$ the discrete $L^2$ projection
  with $\hat M=\mathsf V^\top M\mathsf V$, and $\hat D$ the modal
  differentiation matrix. The modal matrices satisfy
  $\hat M\hat D+\hat D^\top\hat M=\mathsf V^\top B\mathsf V$, and the nodal
  difference matrix
  $$D=\tfrac12M^{-1}(I+\mathsf V\mathsf P)^\top B(I-\mathsf V\mathsf P)+\mathsf V\hat D\mathsf P$$
  has $Q=MD$ with $Q+Q^\top=B$, $M=\mathrm{diag}(\mathsf w_j)$. Because the
  LGL nodes contain the endpoints, plain restriction serves as the
  extrapolation. [Liu et al. (2025c)](/sources/liu-2025-c.md) (§3.1,
  Lemmas 1–2) use the collocated case, $k+2$ LGL nodes for tensor degree
  $k+1$. They use the row sums $\sum_lD_{jl}=\sum_lQ_{jl}=0$ and the column
  sums $\sum_lQ_{lj}=\tau_j$, the $j$th diagonal entry of $B$, in their
  entropy proof for conservative MHD.

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
   diagonal boundary operators, after their Eq. (2.5). Pazner (2021) uses
   (P1) and the Kronecker structure in the same way for the antidiffusive
   corrections of Pazner's limiter: their nodal residuals sum to zero along
   every line of nodes, so they can be rewritten as differences of
   subcell-face fluxes and limited face by face (Props. 8–9,
   Eqs. (53)–(54)).
5. **Entropy and kinetic-energy estimates.** Combined with symmetric
   two-point volume fluxes, the SBP property makes the DG scheme
   entropy-conservative or entropy-dissipative when the volume flux is
   [entropy-conservative](/methods/entropy-conservative-flux.md) and the
   surface flux is entropy-conservative or dissipative (Ranocha et al.
   (2023), §2, citing Fisher, Carpenter, Gassner and co-workers). See
   [entropy stability](/properties/entropy-stability.md).
   Rueda-Ramírez et al. (2021) carry the argument out for GLM-MHD with
   non-conservative terms. With the identities (107)–(110) the element
   entropy balance reduces to the boundary terms plus
   $\sum_{j,k}Q_{jk}\,r_{(j,k)}$, where page-local $r_{(j,k)}$ is the entropy
   production of the volume flux between nodes $j$ and $k$ (Lemma 2,
   Eq. (61)). Because $Q$ has entries of both signs, this sum has no sign
   unless every $r_{(j,k)}$ vanishes, so the volume flux must be
   entropy-conservative; a dissipative volume flux gives an
   "unpredictable" entropy balance (§3.3.2).
   [Renac (2021)](/sources/renac-2021.md) uses the same diagonal-norm SBP
   framework for the author's entropy-stable DGSEM on unstructured quadrilaterals
   (§1.2, §5).
6. **Boundary weight and positivity.** The first and last LGL weights on
   $[-1,1]$ are $\mathsf w_0=\mathsf w_N=2/(N(N+1))$. Renac (2021) shows that
   this weight fixes the CFL factor $1/(2N(N+1))$ of Renac's
   positivity-preserving DGSEM (Remark 6.1, Theorem 6.1;
   [optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)).

7. **Kinetic-energy proofs.** Edoh (2022) proves kinetic-energy
   preservation of split forms entirely in this algebra: the contribution
   of the convective term to $\mathbf v_i^\top M\frac{d}{dt}\mathbf v_i$
   collapses to the boundary term
   $\tfrac12\mathbf v_i^\top B\,\mathrm{diag}(\mathbf v_j)\,\mathbf v_i$, the discrete
   $\tfrac12\big[v_j\lvert v\rvert^2\big]$ at the boundary, using $Q+Q^\top=B$, the commuting diagonal norm and, for
   the rotational form, index relabelling under the double sum (Eqs.
   (11)–(12), (15), (22)–(24)). The same algebra shows that the strain-based
   EMAC form is not kinetic-energy preserving, because the discrete
   product rule fails pointwise (Eq. (16);
   [split convective forms](/methods/split-convective-forms.md),
   [kinetic energy preservation](/properties/kinetic-energy-preservation.md)).
8. **Element-wise constraints.** With a diagonal-norm SBP element, local
   conservation and the element entropy balance are linear constraints
   on the time derivative, $\mathbf 1^\top M\frac{d}{dt}u_m$ and
   $\sum_mw_m^\top M\frac{d}{dt}u_m$ equal to boundary fluxes; Abgrall et al.
   (2022) enforce both with the smallest correction in the $M$-norm (§2.2,
   Eqs. (23)–(26); [entropy correction term](/methods/entropy-correction-term.md)).

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
- [Pazner (2021)](/sources/pazner-2021.md) — §2 Prop. 1 Eqs. (8)–(9), §3 Eq. (23) Fig. 1, Props. 8–9 Eqs. (53)–(54) (arXiv v1).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §3.3.2 Lemma 2 Eq. (61), App. B Eqs. (107)–(110) (arXiv v1).
- [Renac (2021)](/sources/renac-2021.md) — §1.2, §5, Theorem 6.1, Remark 6.1 (arXiv v3).
- [Edoh (2022)](/sources/edoh-2022.md) — §2 Eqs. (1)–(2), §3 Eqs. (11)–(16), (22)–(24).
- [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md) — Eq. (19), §3 Eq. (24) (arXiv v1).
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — §2.2 Eqs. (20)–(26), Example 2.12, App. A.3 (arXiv v4).
- [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) — §3.1 Eq. (5), §3.2 Eqs. (7)–(11), §5 Table 1a Fig. 3, §8, App. A (arXiv v2).
- [Schwarz et al. (2025)](/sources/schwarz-2025.md) — §3.1, §3.3–3.4 Eqs. (20)–(25) (arXiv v1).
- [Cicchino & Nadarajah (2025)](/sources/cicchino-2025.md) — §2 Eq. (22), §3.3 Eqs. (38)–(39), §6 Thms. 6.1–6.2.
- [Liu et al. (2025b)](/sources/liu-2025-b.md) — §3.1 Eqs. (3.4)–(3.8).
- [Liu et al. (2025c)](/sources/liu-2025-c.md) — §3.1 Lemmas 1–2, App. B.
