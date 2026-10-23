---
type: Method
title: "Flux differencing and split-form DG"
description: "Flux differencing replaces the DG volume term D f by symmetric two-point volume fluxes weighted by 2D; on diagonal-norm SBP elements and finite-difference grids it recovers split forms, inherits entropy or kinetic-energy properties from the volume flux, reaches high order through two-point flux combinations, and costs about N+1 times the strong form's flux evaluations."
status: established
aliases: [flux-differencing DG, split-form DG, split-form DGSEM, two-point flux volume integral, entropy-conservative DG volume term, LeFloch–Mercier–Rohde flux, Hadamard-product form]
tags: [dg, finite-difference, entropy-stable, kinetic-energy-preserving, numerical-flux, software]
timestamp: 2026-10-23T23:30:00Z
---

# Flux differencing and split-form DG

In a nodal DG element whose derivative matrix $D_d$ is a diagonal-norm
[summation-by-parts operator](/operators/summation-by-parts-operator.md),
**flux differencing** replaces the volume term $\sum_dD_d\mathbf f^{(d)}$ of the
strong form by

$$\mathrm{VOL}_i=\sum_d\sum_m2\,(D_d)_{im}\,f^{\mathrm{vol},(d)}(u_i,u_m).$$

Here $f^{\mathrm{vol},(d)}$ is a symmetric, consistent two-point *volume flux*
in direction $d$: $f^{\mathrm{vol},(d)}(u,u)=f^{(d)}(u)$ and
$f^{\mathrm{vol},(d)}(u_i,u_m)=f^{\mathrm{vol},(d)}(u_m,u_i)$. The scheme is then

$$\frac{d}{dt}\mathbf u+\mathrm{VOL}+M^{-1}\mathcal R^\top B_\partial\Big(\mathbf h-\sum_dN_d\mathcal R\,\mathbf f^{(d)}\Big)=0,$$

with $\mathbf h$ the surface numerical fluxes. This is the form of
[Ranocha et al. (2023)](/sources/ranocha-2023.md), Eq. (2.5), after Gassner,
Winters & Kopriva, with origins they trace to Tadmor, LeFloch–Mercier–Rohde,
Fisher et al., Carpenter et al. and Chen–Shu. The page-local boundary
symbols $\mathcal R$, $B_\partial$, $N_d$ are those of the SBP page.
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) call
the same construction the *split form* of the DGSEM (§2.1, Eqs. (2)–(7)).

## Consistency with the standard DGSEM

With the central volume flux $f^{\mathrm{vol}}=\{\!\{f\}\!\}$, flux differencing
reduces to the standard strong form. On a curvilinear element the central
flux is $\{\!\{f\cdot Ja\}\!\}$ (Rueda-Ramírez et al. (2022), Eq. (7)). The
check: $\sum_m2D_{im}\tfrac12(f_i+f_m)=f_i\sum_mD_{im}+(D\mathbf f)_i=(D\mathbf f)_i$,
because the rows of a consistent $D$ sum to zero *(compiler check, not in
the sources)*.

Other volume fluxes give the split forms of finite-difference methods
(Ranocha et al. (2023), §2, citing Gassner–Winters–Kopriva). Rueda-Ramírez
et al. (2022), §2.1, list the properties a suitable volume flux can give:

- kinetic-energy preservation;
- entropy conservation or dissipation (Ismail–Roe, Chandrashekar);
- pressure-equilibrium preservation (Shima et al.);
- several of these together.

The fluxes themselves are on
[entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md).
The finite-difference split forms they reproduce are on
[split convective forms](/methods/split-convective-forms.md).

## Finite-difference split forms as flux differencing

[Edoh (2022)](/sources/edoh-2022.md) uses the same identity in the other
direction, to analyse finite-difference split forms with diagonal-norm SBP
operators $D=M^{-1}Q$. For nodal vectors $\mathbf a,\mathbf b$ and their
diagonal matrices $A,B$ (page-local), a quadratic split term is a sum of
two-point fluxes (Eqs. (3)–(6)):

$$\big(AD\mathbf b+BD\mathbf a\big)_i=\sum_m2D_{im}\,(\!(a;b)\!)_{im},\qquad (\!(a;b)\!)_{im}=\tfrac12(a_ib_m+a_mb_i),$$

in Hadamard-product notation $AD\mathbf b+BD\mathbf a=[D\circ(\!(a;b)\!)]\mathbf 1$;
$(\!(a;b)\!)$ is the product mean of
[entropy-conservative two-point fluxes](/methods/entropy-conservative-flux.md),
with $(\!(1;a)\!)$ the arithmetic mean. Hence a quadratic split form is
locally conservative with respect to that special average and obeys a
precise discrete product rule; the identity
$(\!(a;b)\!)=2(\!(1;a)\!)(\!(1;b)\!)-(\!(1;ab)\!)$ shows the two-point flux
"extrapolates" between a non-split and a split flux (Eq. (6)). Edoh's
page-local *splitting error operator*
$\mathcal S_D(a,b)=AD\mathbf b+BD\mathbf a-DA\mathbf b=[D\circ((\!(a;b)\!)-(\!(1;ab)\!))]\mathbf 1$
is telescoping, $\mathbf 1^\top M\mathcal S_D(a,b)=0$ in the periodic
case, and locally of the order of the operator; it encodes the
zero-consistent corrections of Edoh's kinetic-energy-preserving splittings
(Eq. (7); [split convective forms](/methods/split-convective-forms.md)).

## High-order finite-difference fluxes from two-point fluxes

On a uniform finite-difference grid, the LeFloch–Mercier–Rohde
construction raises a symmetric, consistent two-point flux $\tilde f$ to
order $2n_{\mathrm o}$ (page-local $n_{\mathrm o}\ge1$, coefficients
$c_n$):

$$\hat f_{i+1/2}=\sum_{n=1}^{n_{\mathrm o}}c_n\sum_{s=0}^{n-1}\tilde f\big(u_{i-s},u_{i-s+n}\big),\qquad \sum_nn\,c_n=1,\quad \sum_nn^{2s-1}c_n=0\ \ (s=2,\dots,n_{\mathrm o}).$$

[Duan & Tang (2022)](/sources/duan-2022.md) prove that
$\frac1{\Delta\xi}(\hat f_{i+1/2}-\hat f_{i-1/2})$ approximates
$\partial_\xi f$ to order $2n_{\mathrm o}$ also on moving curvilinear
meshes, with the metric terms evaluated at the same two nodes, and that
the same combination discretizes the geometric conservation laws and a
non-conservative source term consistently (Prop. 3.1, Eqs.
(3.6)–(3.12)). The key step is their Lemma 3.1: for a consistent
symmetric two-point function,
$2\,\partial_{\zeta_r}\tilde f(u(\zeta_l),u(\zeta_r))\vert_{\zeta_r=\zeta_l}=\partial_\zeta f(u(\zeta))\vert_{\zeta_l}$,
an identity they credit to Chan. With an entropy-conservative $\tilde f$
the flux is entropy conservative (Thm. 3.2). For $n_{\mathrm o}=2$ the
constraints give $c_1=4/3$, $c_2=-1/6$, the fourth-order central weights
*(compiler check, not in the sources: the paper prints no values of the
coefficients)*. This is the finite-difference counterpart of DG flux
differencing: a central difference whose products are replaced by
two-point fluxes. Duan & Tang (sixth order, $n_{\mathrm o}=3$) and Li, Duan
& Tang build their moving-mesh TeCNO schemes on it
([adaptive moving mesh](/methods/adaptive-moving-mesh.md),
[TeCNO schemes](/methods/tecno-scheme.md)).

[De Michele & Coppola (2023b)](/sources/demichele-2023-b.md) state the same
construction from a central derivative formula (App. A, Eqs. (16)–(18),
after Theorem 3.1 of Ranocha and after Pirozzoli; arXiv v2). If
$\partial_x\phi_i\approx\sum_{k=-L_{\mathrm s}}^{L_{\mathrm s}}\mathsf a_k\phi_{i+k}$ with central weights
$\mathsf a_k=-\mathsf a_{-k}$ (page-local $\mathsf a_k$ and half-width $L_{\mathrm s}$), then
$\partial_xf\approx\sum_k2\mathsf a_k\tilde f(u_i,u_{i+k})$ with the same order, and
the central sum is the difference of

$$\hat f_{i+1/2}=2\sum_{k=1}^{L_{\mathrm s}}\mathsf a_k\sum_{m=0}^{k-1}\tilde f\big(u_{i-m},u_{i-m+k}\big).$$

This is the formula above with $c_k=2\mathsf a_k$, and $\sum_kk\,c_k=1$ is the
consistency of the central derivative, $\sum_{k=-L_{\mathrm s}}^{L_{\mathrm s}}k\,\mathsf a_k=1$ *(compiler
check, not in the sources)*. The authors note that for fluxes built from
arithmetic and product means the formula reduces to a high-order finite
difference of a combination of advective and divergence forms, and that it
extends high order to nonlinear two-point fluxes, such as their
asymptotically entropy-conservative ones, for which no split-form
representation exists. They run it at fourth and sixth order on the
inviscid Taylor–Green vortex (§5;
[entropy-conservative fluxes](/methods/entropy-conservative-flux.md)).

The central weights need not be those of maximum order.
[Liang & Fu (2024b)](/sources/liang-2024-b.md) use the same formula with
four terms and the Kennedy–Gruber triple-average two-point flux, but fix
only the consistency and second- and fourth-order conditions on
$\mathsf a_1,\dots,\mathsf a_4$ and choose the remaining freedom by a
weighted spectral optimization, giving a sixth-order eight-point flux with
$\mathsf a_1=0.8441336457279522$, $\mathsf a_2=-0.2441336457279522$,
$\mathsf a_3=0.0570096576929319$, $\mathsf a_4=-0.006723831837710873$
(§2.3 Eqs. (27)–(28), §3.3.1 Eqs. (40)–(42)). Details are on
[split convective forms](/methods/split-convective-forms.md).

## Properties

- **Entropy.** The scheme is entropy-conservative if the volume flux is
  entropy-conservative and the surface flux is entropy-conservative. It is
  entropy-dissipative if the surface flux is entropy-dissipative instead
  (Ranocha et al. (2023), §2, citing Carpenter et al. and Gassner–Winters–Kopriva).
  See [entropy stability](/properties/entropy-stability.md).
  [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) explain why
  the dissipation belongs in the surface flux. The volume contribution to
  the element entropy balance is $\sum_{j,k}Q_{jk}r_{(j,k)}$, with
  page-local $r_{(j,k)}$ the entropy production of the volume flux between
  nodes $j$ and $k$, and $Q$ has entries of both signs. An
  entropy-dissipative volume flux therefore gives an "unpredictable"
  entropy balance; only an EC volume flux makes the volume part vanish
  (Lemma 2, Eq. (61), §3.3.2).
  [Renac (2021)](/sources/renac-2021.md) uses the construction on
  straight-sided unstructured quadrilaterals, with Renac's multicomponent EC
  flux in the volume and an entropy-stable relaxation flux at the
  interfaces. In 2D the volume term at node $(i,j)$ of element $K$ reads
  $$2\mathsf w_i\mathsf w_j\Big(\sum_kD_{ik}\,f^{\mathrm{ec}}\big(u^{ij},u^{kj},\{\!\{Ja^{(1)}\}\!\}_{(i,k)j}\big)+\sum_kD_{jk}\,f^{\mathrm{ec}}\big(u^{ij},u^{ik},\{\!\{Ja^{(2)}\}\!\}_{i(j,k)}\big)\Big),$$
  with the contravariant metric terms $Ja^{(1)}$, $Ja^{(2)}$ (Renac's
  $J\nabla\xi$ and its companion) averaged between the two nodes, as in
  the curvilinear form below. The
  scheme satisfies a cell entropy inequality (§5.2, Eqs. (62)–(64)).
- **Robustness against correction terms.** [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md)
  compare flux differencing with central DG made entropy conservative or
  kinetic-energy preserving by an element-wise
  [entropy correction term](/methods/entropy-correction-term.md). On the
  inviscid 2D [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
  with nodal DG at $N=5$ on $16^2$ elements, the central scheme blows up at
  $t\approx3.8$ and the version with both corrections at $t\approx4.3$, while flux differencing with an
  entropy-conservative and kinetic-energy-preserving volume flux runs to
  $t\approx35$; on a sixth-order SBP finite-difference grid of $100^2$
  nodes the corrected schemes fail at $t\approx23.5$–$25.5$ and flux
  differencing with the Pirozzoli or Ranocha flux does not fail before
  $t=30$ (§4.2.2, App. A.3, Figs. 7, 11). The authors suggest that flux
  differencing gains from the local (inter-element and subcell) entropy
  balances it satisfies, which an element-wise correction does not (§6).
- **Chain-rule split forms.** For Burgers,
  [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md)
  split the volume term as $\tfrac23\partial_x(u^2/2)+\tfrac13u\,\partial_xu$
  with respect to the stiffness operator rather than through two-point
  fluxes; for DG their scheme coincides with Chan's flux-differencing form,
  and for collocated LGL DG with Gassner's split form (§3.1). They extend
  it to energy-stable flux reconstruction
  ([flux reconstruction](/methods/flux-reconstruction.md)).
- **Accuracy.** For general symmetric volume fluxes the scheme keeps the
  order of accuracy of the derivative operator (Ranocha et al. (2023), §2,
  citing Chen–Shu and Ranocha). This is the route to high order with
  kinetic-energy-preserving fluxes *(compiler check, not in the sources:
  neither source relates the two results)*. It sidesteps the second-order barrier
  that [Coppola & Veldman (2023)](/sources/coppola-2023.md) prove for
  single product-form face fluxes, since the volume term is a sum of
  two-point fluxes over the element
  ([kinetic energy preservation](/properties/kinetic-energy-preservation.md)).
- **Local conservation.** Rueda-Ramírez et al. (2022), Eqs. (8)–(11), write
  the whole DGSEM, surface terms included, as inter-node flux differences.
  In the first direction, with unit Jacobian for brevity, the scheme reads
  $\mathsf w_i\frac{d}{dt}u_i=\hat f^{\mathrm{DG}}_{(i-1,i)}-\hat f^{\mathrm{DG}}_{(i,i+1)}$.
  The outer fluxes $\hat f^{\mathrm{DG}}_{(-1,0)}$ and $\hat f^{\mathrm{DG}}_{(N,N+1)}$
  are the surface numerical fluxes. The inner ones follow recursively from
  the volume terms, $\hat f^{\mathrm{DG}}_{(0,1)}=-F^{\mathrm{vol}}_0$ and
  $\hat f^{\mathrm{DG}}_{(i,i+1)}=\hat f^{\mathrm{DG}}_{(i-1,i)}-F^{\mathrm{vol}}_i$
  for $i=1,\dots,N-1$, with page-local $F^{\mathrm{vol}}_i=-\sum_mS_{im}f^{\mathrm{vol}}(u_i,u_m)$ and
  $S=2Q-B$. The authors note that these fluxes differ slightly from Fisher &
  Carpenter's because the surface terms are transformed too (§2.1). The flux
  form gives subelement-wise conservation in the
  [Lax–Wendroff](/results/lax-wendroff-theorem.md) sense. It is what allows
  [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)
  to blend DG and finite-volume fluxes at each subcell interface.
  [Rueda-Ramírez, Bolm, Kuzmin & Gassner (2024)](/sources/ruedaramirez-2024.md)
  print the closed form,
  $\hat f^{\mathrm{DG}}_{(i,i+1)}=\sum_{l=0}^{i}\sum_{k=0}^{N}S_{lk}\,f^{\mathrm{vol}}(u_l,u_k)$,
  symmetric in its two indices, so that with the unit normals $\pm1$ the
  subcell fluxes are antisymmetric (§2.1, Eqs. (5)–(8), Remark 1; arXiv
  v1); summing the recursion above gives exactly this sum
  *(compiler check, not in the sources)*. They add that the form is free
  only for diagonal-norm SBP operators: DG with a dense mass matrix, such as
  a Bernstein basis of degree $N>1$, needs one sparse
  $(N+1)\times(N+1)$ linear solve per equation, element and Runge–Kutta
  stage to recover it (Remark 2), and Gauss-node DGSEM admits it with
  inter-element fluxes and projections still to be analysed (Remark 3).
  They limit these fluxes against a Rusanov subcell scheme by monolithic
  convex limiting ([DGSEM](/methods/dgsem.md),
  [convex limiting](/methods/convex-limiting.md)).

## Non-conservative terms

Rueda-Ramírez et al. (2021) extend the split form to GLM-MHD, whose
entropy analysis needs the non-conservative Powell and GLM terms (§2.2).
In 1D, with page-local $\Phi$ the nodal non-conservative "flux",
$\Phi^\diamond_{(j,k)}$ its surface two-point term and $\Phi^*_{(j,k)}$ its
volume two-point term, the advective and non-conservative part of the
nodal balance is (Eq. (32))

$$\begin{aligned}J\mathsf w_j\frac{d}{dt}u_j={}&-2\sum_kQ_{jk}f^{\mathrm{vol}}(u_j,u_k)-\sum_kQ_{jk}\Phi^*_{(j,k)}+\delta_{jN}(f_N+\Phi_N)-\delta_{j0}(f_0+\Phi_0)\\&-\delta_{jN}\big(h_{(N,R)}+\Phi^\diamond_{(N,R)}\big)+\delta_{j0}\big(h_{(0,L)}+\Phi^\diamond_{(0,L)}\big),\end{aligned}$$

with $L$ and $R$ the outer neighbour states. The two-point fluxes must be
symmetric and consistent. The non-conservative terms need only
consistency, $\Phi^\diamond_{(j,j)}=\Phi^*_{(j,j)}=\Phi_j$, and they are not
symmetric. The surface term multiplies the nodal coefficient vector by the
arithmetic mean of the field it differentiates, e.g. $\{\!\{B_1\}\!\}$ and
$\{\!\{\psi_{\mathrm{GLM}}\}\!\}$, and the volume term satisfies
$\Phi^*_{(j,k)}=2\Phi^\diamond_{(j,k)}-\Phi_j$ (Eqs. (35)–(37), (106)).
Together with the Derigs et al. EC flux, this split form is entropy
conservative in the generalized Tadmor sense
([entropy stability](/properties/entropy-stability.md)). On 3D curvilinear
meshes the non-conservative terms carry averaged metric terms as well
(App. C.1, Eqs. (133)–(139)).

## Efficient evaluation

Ranocha et al. (2023) collect the implementation identities and measure
each one in [Trixi.jl](/software/trixi-jl.md) and [FLUXO](/software/fluxo.md).

1. **Absorbing the surface correction.** With
   $\widetilde D_d=2D_d-M^{-1}\mathcal R^\top B_\partial N_d\mathcal R$ and
   diagonal $M$ and boundary operator, consistency of $f^{\mathrm{vol}}$
   cancels the $-N_d\mathcal R\mathbf f^{(d)}$ term. The scheme becomes
   $\frac{d}{dt}\mathbf u+\sum_d\sum_m(\widetilde D_d)_{im}f^{\mathrm{vol},(d)}(u_i,u_m)+M^{-1}\mathcal R^\top B_\partial\mathbf h=0$,
   the flux-differencing analogue of the weak form, with no pointwise flux
   evaluation at surface nodes (§2.1, Eqs. (2.7)–(2.10)).
2. **Skew-symmetry.** $M\widetilde D_d$ is skew-symmetric (Eq. (2.11)), so
   $(\widetilde D_d)_{ii}=0$. With symmetric fluxes only the pairs $i<m$ are
   evaluated, which "saves more than half" of the volume-flux evaluations
   (§2.2). In 1D, $M\widetilde D=2Q-B=S$, the split-form matrix of
   Rueda-Ramírez et al. (2022) *(compiler check, not in the sources)*.
3. **Curvilinear elements.** The curvilinear SBP operator gives
   $(D_d)_{im}=J_i^{-1}\sum_n\{\!\{Ja^{(n)}_d\}\!\}_{im}(D_{n,\xi})_{im}$, with the
   metric terms averaged between nodes $i$ and $m$ (Eq. (2.17)). Rueda-Ramírez
   et al. (2022), Eq. (6), use the same averaged metrics in the contravariant
   two-point flux. Reordering the sums turns the volume term into one
   *directional* volume flux per reference direction $n$, taken along the
   averaged contravariant vector $\{\!\{Ja^{(n)}\}\!\}_{im}$. This keeps the
   sparsity of the tensor-product operators, which the Cartesian-flux form
   (2.18) loses (§2.3, Eq. (2.19)).
4. **Directional fluxes.** Directional fluxes should be coded directly
   rather than through rotation to the first coordinate direction (§4.2,
   Table 2). Free-stream preservation on curved meshes still depends on how
   the contravariant vectors are computed, for which the authors cite the
   literature (§2.3;
   [free-stream preservation](/properties/free-stream-preservation.md)).

### Cost

On tensor-product LGL elements of degree $N$ in $d$ dimensions, the strong
form needs $d(N+1)^d$ flux evaluations per element, and flux differencing
needs $O(d(N+1)^{d+1})$. Both need $O(d(N+1)^{d+1})$ floating-point
operations without the fluxes (Ranocha et al. (2023), §2, Table 1).

The authors measure cost by the performance index PID, the wall-clock time
of one evaluation of the semi-discretization divided by the number of DG
nodes (Def. 4.1). It counts one node as one degree of freedom, not node
times variable. Their findings:

- **Against overintegration.** Overintegration interpolates to a higher
  degree, applies the weak form there and projects back. In 3D with the
  Shima et al. flux, flux differencing is cheaper than any overintegration
  for $3\le N\le5$. With the entropy-conservative flux it lies between
  overintegration to degree $N+1$ and $N+2$ for $N\in\{3,4\}$ (§5, Fig. 2).
  In 3D at $N\le3$, the most relevant case for CFD, flux differencing can be
  faster than overintegration with one extra node per direction (§5, §9).
- **Robustness.** Ranocha et al. state, citing earlier work, that flux
  differencing stays stable where overintegration fails, and that
  overintegration costs about a factor two in explicit time step (§5).
- **SIMD.** With an array-of-structures-of-arrays layout, precomputed
  primitive variables and logarithms, and explicit vectorization, the volume
  terms reach vectorization ratios of 98.36–99.26 % and 20.69–29.09 % of the
  FMA peak at $N=3$ on an Intel Core i7-8700K (§8, Table 3). The total
  speed-up is 20 % to 3× in 2D and 30 % to 3× in 3D (Figs. 10–11).
- **Best timings.** The best 3D PIDs at $N=3$ are
  $2.6\times10^{-8}$ s (Cartesian) and $4.3\times10^{-8}$ s (curved,
  unstructured) with the Shima et al. flux, and $4.2\times10^{-8}$ s and
  $6.5\times10^{-8}$ s with the Ranocha entropy-conservative flux (§9).

## Gauss-node variant

On Legendre–Gauss nodes the volume nodes exclude the boundary. Entropy
stability then requires the hybridized SBP operator and an *entropy
projection*: the surface states are computed from the interpolated entropy
variables, $\tilde u=u(\mathcal Rw(\mathbf u))$ (Ranocha et al. (2023), §6,
Eqs. (6.1)–(6.3)).

- **Run-time breakdown.** Flux differencing takes 66–91 % of the run time in
  2D and 65–89 % in 3D. The entropy projection takes 4–14 % (Fig. 3).
- **Cost relative to LGL.** The Gauss scheme is 1.5× to 5× more expensive
  than LGL-DGSEM, with the gap closing at high order in 3D (Fig. 4).
- **Self-correction.** An earlier estimate by Chan and co-workers, that a
  degree-$N$ Gauss scheme costs about as much as a degree-$(N+1)$ LGL
  scheme, "was optimistic" because it ignored the projection, face
  interpolation and lifting (§6, footnote 4). J. Chan is an author of both
  papers.

## Qualifications

- The cost figures are single-core CPU measurements on the compressible
  Euler equations. MPI and non-conservative terms are deferred to other work
  (Ranocha et al. (2023), §9).
- Ranocha et al.'s §4.2 prose ranges for the flux microbenchmarks do not
  match their Table 2 throughout *(compiler check, not in the sources:
  ratios computed from the printed timings)*. The text says the Cartesian flux is 5–20 %
  faster than the directional one, but the table gives +27 % for the Shima
  flux in 3D and a faster directional HLL flux in 3D. The text puts the
  precomputed rotated flux up to 2× slower, but the table's largest ratio is
  1.55. The table is the measurement.

# Citations

- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §2 Eq. (2.5) and Table 1, §2.1–2.3 Eqs. (2.7)–(2.19), §4.2 Table 2, §5 Fig. 2, §6 Eqs. (6.1)–(6.3) Figs. 3–4, §8 Table 3, §9.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1 Eqs. (2)–(11).
- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §6.1 Observation 9.
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §2.2, §3.1 Eqs. (32)–(37), §3.3.2 Lemma 2 Eq. (61), App. B Eq. (106), App. C.1 Eqs. (133)–(139) (arXiv v1).
- [Renac (2021)](/sources/renac-2021.md) — §5.2 Eqs. (62)–(64) (arXiv v3).
- [Edoh (2022)](/sources/edoh-2022.md) — §2 Eqs. (1)–(7).
- [Duan & Tang (2022)](/sources/duan-2022.md) — §3.2 Prop. 3.1, Lemma 3.1, Eqs. (3.6)–(3.12), Thm. 3.2 (arXiv v1).
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — §2.2 Ex. 2.4 Eq. (22), §4.2.2 Figs. 7–8, §6, App. A.3 Fig. 11 (arXiv v4).
- [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md) — §3.1 (arXiv v1).
- [De Michele & Coppola (2023b)](/sources/demichele-2023-b.md) — App. A Eqs. (16)–(18), §5 (arXiv v2).
- [Rueda-Ramírez, Bolm, Kuzmin & Gassner (2024)](/sources/ruedaramirez-2024.md) — §2.1 Eqs. (5)–(8), Remarks 1–3 (arXiv v1).
- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — §2.3 Eqs. (27)–(28), §3.3.1 Eqs. (40)–(42).
