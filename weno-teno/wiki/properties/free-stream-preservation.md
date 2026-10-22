---
type: Property
title: "Free-stream preservation"
description: "A discretization on curvilinear or moving grids is free-stream preserving when a uniform state stays an exact discrete steady solution, which requires discrete metric identities; the page covers the DGSEM identity, corrected and subcell metrics, warped-mesh tests, geometric conservation laws on moving meshes with the Duan–Tang proof, and an untested TENO claim."
status: established
aliases: [freestream preservation, free-stream preserving, discrete metric identities, geometric conservation law, GCL, watertight subcell discretization]
tags: [dg, finite-difference, limiting, entropy-stable]
timestamp: 2026-10-22T20:00:00Z
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
They note that "the usual care must be taken to ensure free-stream
preservation" when the contravariant vectors are computed, and cite the
literature for it rather than proving it (§2.3).

[Pazner (2021)](/sources/pazner-2021.md) states the condition and proves
its effect. With $G$ the diagonal matrix of nodal Jacobians and $GJ^{-1}$
the nodal metric terms (his notation, page-local), the discrete metric
identity of Kopriva, as he recalls it, is
$\sum_iD_{i}\,(GJ^{-1})_{ij}=0$ for every $j$, with $D_i$ the
tensor-product weighted derivative in direction $i$ (Eq. (22)).

- **Strong form.** Under the identity, the strong-form DGSEM gives
  $\frac{d}{dt}u=0$ for every spatially constant flux (Prop. 3).
- **Weak form.** The weak form is in general not free-stream preserving,
  for example on curved meshes. Pazner therefore takes the strong form as
  the high-order target of his limiter (§2.4.2).

[Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) show where the
identity enters the entropy analysis on 3D curvilinear hexahedra. The
element entropy balance of the split-form DGSEM contains a residual equal
to the entropy flux potential contracted with the discrete divergence of
the metric terms. It vanishes when the discrete metric identities hold,
e.g. for metrics computed as a discrete curl (App. C.1, Lemma 4,
Eq. (145)). Free-stream preservation is therefore a prerequisite of their
entropy conservation and stability proofs, as they state after Hennemann
et al. (§6.1).

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
subcell scheme (Eq. (15)). Rueda-Ramírez et al. (2021) give the 3D form of
the same normals and use them for the non-conservative GLM-MHD terms as
well (App. C.2, Eq. (150)). The normals are symmetric. On element
boundaries they reduce to the surface-scaled normals, pointing along the
reference coordinates rather than outward. They make the subcell
finite-volume scheme watertight, and its entropy-balance residual vanishes
under the DG metric identities (Lemma 5): inserting (150) turns the
residual into the discrete divergence of the metric terms, Eq. (145). The
normals and their watertightness are taken from Hennemann et al.
The finite-volume flux through each subcell face is
$\lVert n_{(a,b)}\rVert\,h\big(u_a,u_b;n_{(a,b)}/\lVert n_{(a,b)}\rVert\big)$
(Eq. (13)). For a constant state, consistency of $h$ reduces the residual
to $f(u)$ dotted into the left-hand side of the identity. The residual
therefore vanishes exactly when the identity holds *(compiler check, not in
the sources)*.

**Pazner's corrected metrics.** Pazner (2021) builds his low-order
scheme from the sparse first-order operator $\widehat Q$
([summation-by-parts operator](/operators/summation-by-parts-operator.md)).
That operator cannot differentiate the metric terms exactly, so the metric
identities fail for it, and with them free-stream preservation (§3). He
perturbs the metric terms, $\widehat{GJ^{-1}}=GJ^{-1}+C$ with page-local
correction $C$, so that the sparse weak form reproduces the boundary normals
for a constant state (Eq. (25)). This is an underdetermined linear system,
Eqs. (26)–(27). Its operator has the constants as null space, so it is
solvable when the right-hand side sums to zero. The sum vanishes by (P1),
the SBP column sums and the metric identity (22) (Eq. (28)). Pazner takes
the minimum-norm solution from a singular-value decomposition precomputed
on the reference element, and the perturbation is $O(h)$ entrywise. The
corrected low-order scheme is conservative and constant-preserving
(Prop. 4). For variable-velocity advection the same correction must also
enforce a discrete divergence-free condition on the velocity,
$\sum_j\hat c_{ij}\cdot\beta_j=0$ (page-local velocity $\beta_j$ at node
$j$); the procedure for this is not given (§3.3).

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

## Evidence on warped meshes

Rueda-Ramírez et al. (2021) test the blended DGSEM–subcell scheme on a
heavily warped 3D mesh of $10^3$ elements, geometry degree 4, with a
uniform GLM-MHD state ($\rho=1$, $v=(0.1,-0.2,0.3)$, $p=1$, $B=(1,1,1)$).
The blending coefficient $\alpha$ is drawn at random per element and per
Runge–Kutta stage; $N=4$, CFL 0.1, $t=1$ (§6.1, Eqs. (91)–(94)). The
$L^2$ norm of $\partial_tu$ is $10^{-13}$–$10^{-12}$ at $t=0$. At $t=1$ the
deviation is about $10^{-13}$ with the entropy-conservative surface flux
and $10^{-14}$–$10^{-15}$ with the entropy-stable and TVD-ES fluxes
(Table 1; [TeCNO schemes](/methods/tecno-scheme.md)). Free streams are
kept for random element-wise blends; the subcell metrics (150) and the
discrete metric identities are the ingredients of the proofs in App. C.

## Moving meshes: geometric conservation laws

On a mesh that moves in time, a uniform state must also survive the mesh
motion. [Duan & Tang (2022)](/sources/duan-2022.md) and
[Li, Duan & Tang (2022)](/sources/li-2022-c.md) write the law in
time-dependent curvilinear coordinates together with the volume
conservation law (VCL), $\partial_\tau J+\sum_k\partial_{\xi_k}(J\partial_t\xi_k)=0$,
and the surface conservation laws (SCLs),
$\sum_k\partial_{\xi_k}(J\partial_{x_j}\xi_k)=0$ (Duan & Tang, Eq. (2.9); Li,
Duan & Tang, Eq. (2.3); [adaptive moving mesh](/methods/adaptive-moving-mesh.md)).
As Duan & Tang recall, these identities make constant states exact
solutions of the transformed equations (§2). Discretely, in both papers:

- the SCL metric terms are written in conservative cross-product form with
  the same central difference, of order $2n_{\mathrm o}$ (page-local, as
  on [flux differencing](/methods/flux-differencing.md)), as the
  entropy-conservative flux, which gives the discrete SCLs (Li, Duan &
  Tang, Eq. (3.9); Duan & Tang, Eq. (3.17));
- the time metric is computed from the mesh velocity as
  $J\partial_t\xi_k=-\sum_j\dot x_j\,J\partial_{x_j}\xi_k$, which gives the
  semi-discrete VCL (Li, Duan & Tang, Eq. (3.10); Duan & Tang, Eq. (3.18)),
  page-local computational coordinates $\xi_k$ and computational time
  $\tau$.

Li, Duan & Tang state that the fully discrete scheme with SSP-RK3 then
preserves free streams, proved by Duan & Tang (Remark 3.1). As recalled
from Visbal & Gaitonde, violating free-stream preservation "causes large
errors and instabilities" for high-order schemes (§3.2).

**The proof** (Duan & Tang (2022), §3.3, Prop. 3.2). The proof for the
high-order finite-difference case, which Li, Duan & Tang defer to "Duan &
Tang", is in this paper:

1. *Discrete SCLs.* The metrics are written in divergence
   (cross-product) form, e.g.
   $J\partial_{x_1}\xi_1=\partial_{\xi_3}(x_3\,\partial_{\xi_2}x_2)-\partial_{\xi_2}(x_3\,\partial_{\xi_3}x_2)$,
   and every derivative is replaced by the same central operator
   $\delta_k a_i=\tfrac12\sum_nc_n(a_{i+n\mathbf e_k}-a_{i-n\mathbf e_k})$
   (page-local coefficients $c_n$, those of the entropy-conservative flux
   combination; [flux differencing](/methods/flux-differencing.md)). The
   discrete SCLs then hold exactly, because the directional operators
   commute, $\delta_j\delta_k=\delta_k\delta_j$ (Eqs. (3.15)–(3.17), after the
   conservative metric method of Thomas & Lombard). In 2D the metrics
   reduce to central differences of the node coordinates (App. B); in 1D
   the SCL holds automatically (App. A).
2. *Discrete VCL.* The temporal metrics are
   $J\partial_t\xi_k=-\sum_j\dot x_j\,J\partial_{x_j}\xi_k$ at the nodes, and
   $J$ is advanced by the same flux combination applied to the averaged
   temporal metrics (Eqs. (3.5), (3.8), (3.18)).
3. *Forward Euler.* With $u^n_i=u_0$ everywhere, the update gives
   $J^{n+1}_i=J^n_i-\sum_k\frac{\Delta t}{\Delta\xi_k}\,\delta_k[J\partial_t\xi_k]$
   and $(Ju)^{n+1}_i=J^{n+1}_iu_0$, so the state stays $u_0$; explicit
   SSP Runge–Kutta methods are convex combinations of forward-Euler steps,
   which extends the result (Prop. 3.2).
4. *Entropy-stable dissipation.* The dissipation of their TeCNO-type flux
   acts on jumps of reconstructed entropy variables and vanishes for a
   constant state, so the entropy-stable scheme preserves free streams too
   (Remark 4.1; [TeCNO schemes](/methods/tecno-scheme.md)).

Discrete GCLs are also needed for the discrete entropy conservation of the
moving-mesh scheme (Duan & Tang, Remark 2.1, Thm. 3.2;
[entropy stability](/properties/entropy-stability.md)). Neither paper
prints a free-stream test; the property is proved, and the accuracy tests
on moving meshes reach the design orders (Duan & Tang, Exs. 6.1, 6.7).

## Finite-difference reconstruction schemes

[Ye et al. (2022)](/sources/ye-2022.md) argue that [AFTENO](/methods/afteno.md)
has an advantage over flux-splitting TENO. Because it interpolates states
and evaluates a two-point flux plus derivative corrections, they claim it
keeps free streams better (§1, §4.2, §5). They also say the extra cost of
the interpolation-based flux, about three times TENO5, buys this property.
The paper contains no curvilinear-grid test, so the claim is untested in
the source.

## Qualifications

- **Who proves what.** Ranocha et al. (2023) and Rueda-Ramírez et al.
  (2022) cite free-stream preservation from the literature for the DGSEM
  and the subcell normals. Ye et al. (2022) assert it without a test.
  Pazner (2021) proves it for the strong-form DGSEM and for his corrected
  low-order scheme (Props. 3–4), and Rueda-Ramírez et al. (2021) prove
  that the curvilinear entropy-balance residuals vanish under the metric
  identities and show free-stream preservation numerically. Li, Duan &
  Tang (2022) cite the proof for moving meshes; Duan & Tang (2022) give it
  (Prop. 3.2).
- **Strong and weak forms.** Pazner's statement that the weak form (14)
  "will not in general" preserve constants ("e.g. curved meshes", §2.4.2)
  is not a conflict with the strong–weak equivalence of Ranocha et al.
  (2023), Eq. (2.6), but a difference in how the face normals enter. Ranocha
  et al. derive (2.6) from the SBP property (2.2), whose boundary operator
  $\mathcal R^\top B_\partial N_d\mathcal R$ already carries the normals.
  Pazner's strong form (15) carries the face normals separately, in
  $\hat F_e-F_e\cdot n$, next to the volume metric terms $GJ^{-1}$. *(Compiler
  check, not in the sources: by the SBP column sums the two discrete forms
  differ by the boundary values of the contravariant flux against
  $F_e\cdot n$; they coincide when the face normals equal the volume metric
  terms at the boundary nodes and differ when the normals are computed
  otherwise.)*
- **Numbering.** Rueda-Ramírez et al. (2022) cite Pazner's sparsified
  matrix as his Eq. (34) and the conservation condition as Eq. (35). In the
  arXiv v1 of Pazner (2021) read here they are Eq. (23) and the first item
  of Prop. 5. The difference is one of versions.

# Citations

- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1 Eq. (6), §2.2 Eqs. (13)–(15), §3 Prop. 2 Eqs. (35)–(36).
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §2.3 Eqs. (2.12)–(2.19).
- [Ye et al. (2022)](/sources/ye-2022.md) — §1, §4.2, §5.
- [Pazner (2021)](/sources/pazner-2021.md) — §2.4 Eq. (22) Prop. 3, §3.1 Eqs. (25)–(29) Props. 4–5, §3.3 (arXiv v1).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §6.1 Eqs. (91)–(94) Table 1, App. C Lemmas 4–5 Eqs. (145), (150) (arXiv v1).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §2 Eq. (2.3), §3.2 Eqs. (3.9)–(3.10), Remark 3.1 (arXiv v1).
- [Duan & Tang (2022)](/sources/duan-2022.md) — §2 Eq. (2.9), Remark 2.1, §3.3 Eqs. (3.5), (3.8), (3.15)–(3.18), Prop. 3.2, Thm. 3.2, Remark 4.1, App. A–B, Exs. 6.1, 6.7 (arXiv v1).
