---
type: Method
title: "Subcell finite-volume limiting for DG"
description: "Subcell finite-volume limiting makes a nodal DGSEM robust by convexly blending it, per element or per subcell interface, with a compatible low-order finite-volume scheme on the LGL subcells; the page gives the flux-differencing form, the four mix-and-match ingredients, the entropy-stable blending lemma, semi-discrete monolithic convex limiting, switching on equidistant or Gauss-weight subcells, Gauss-node blending, and measured effects."
status: established
aliases: [subcell limiting, subcell FV shock capturing, hybrid DG/FV blending, element-wise blending, subcell-wise blending, native LGL finite volumes, FV subcell switching]
tags: [dg, limiting, finite-volume, positivity, entropy-stable]
timestamp: 2026-10-24T06:38:53Z
---

# Subcell finite-volume limiting for DG

A nodal [DGSEM](/methods/dgsem.md) of degree $N$ on Legendre–Gauss–Lobatto
(LGL) nodes can be rewritten exactly as a finite-volume-like scheme on
$N+1$ subcells per direction, whose widths (in reference space) are the LGL
weights $\mathsf w_i$. A low-order finite-volume scheme on the same subcells
then shares the degrees of freedom with the DG scheme, and the two can be
blended convexly with a coefficient $\alpha\in[0,1]$ ($\alpha=0$ pure DG,
$\alpha=1$ pure finite volume). [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)
cast this as a framework of four ingredients that can be mixed and matched,
recover existing methods as members of it, and test new combinations. Two
earlier members are ingested as well:
[Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md), who extend
Hennemann et al.'s element-wise blending to systems with non-conservative
terms (resistive GLM-MHD) and prove that it keeps entropy stability, and
[Pazner (2021)](/sources/pazner-2021.md), whose sparse invariant-domain
preserving DG limits antidiffusive fluxes subcell face by subcell face.

## Ingredient I: the high-order DGSEM in subcell-flux form

In 2D, on a curvilinear quadrilateral with tensor LGL nodes, the DGSEM in
standard or split ([flux-differencing](/methods/flux-differencing.md)) form
uses the SBP matrices $Q_{ij}=\mathsf w_i\ell_j'(\xi_i)$ and
$B=\mathrm{diag}(-1,0,\dots,0,1)$ of the
[summation-by-parts operator](/operators/summation-by-parts-operator.md)
page, with volume matrix $Q-B$ (standard) or $2Q-B$ (split) and a symmetric,
consistent two-point volume flux $f^{\mathrm{vol}}$ evaluated with averaged
metric terms (Rueda-Ramírez et al. 2022, Eqs. (2)–(7)). The choice of
$f^{\mathrm{vol}}$ gives kinetic-energy preservation, entropy conservation
(Ismail–Roe, Chandrashekar) or pressure-equilibrium preservation (Shima et
al.) ([entropy-conservative flux](/methods/entropy-conservative-flux.md)).

Because DGSEM on LGL nodes is a diagonal-norm SBP discretization, it can be
written in **flux-differencing (subcell) form** (Eqs. (8)–(11), after Fisher
& Carpenter, with surface terms transformed as well):
$$J_{ij}\,\dot u^{\mathrm{DG}}_{ij}=\frac{1}{\mathsf w_i}\Big(\hat f^{\mathrm{DG}}_{(i-1,i)j}-\hat f^{\mathrm{DG}}_{(i,i+1)j}\Big)+\frac{1}{\mathsf w_j}\Big(\hat f^{\mathrm{DG}}_{i(j-1,j)}-\hat f^{\mathrm{DG}}_{i(j,j+1)}\Big),$$
with the element surface fluxes at the outer subcell faces and the inner
fluxes $\hat f^{\mathrm{DG}}_{(i,i+1)j}=-\sum_{l=0}^{i}F^{\mathrm{vol}(1)}_{lj}$,
computed recursively, $F^{\mathrm{vol}(1)}$ the volume term of direction 1
(page-local). The form shows local subcell conservation, so the
[Lax–Wendroff theorem](/results/lax-wendroff-theorem.md) applies at the
subcell level (§2.1).

**Non-conservative terms.** For GLM-MHD with the Powell and GLM terms,
[Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) (Eqs. (31)–(37),
after Bohm et al.) add to the 1D split form a volume term
$-\sum_kQ_{jk}\Phi^*_{(j,k)}$ and a surface term $\Phi^\diamond$ at the element
boundary, with $\Phi^*_{(j,k)}=2\Phi^\diamond_{(j,k)}-\Phi_j$ and
$\Phi^\diamond_{(j,j+1)}$ built from the arithmetic means of $B_1$ and
$\psi_{\mathrm{GLM}}$ at the interface ($\Phi$, $\Phi^*$, $\Phi^\diamond$
page-local; the Powell vector is that of the
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
page). The non-conservative two-point terms need consistency but not
symmetry. Entropy stability requires an entropy-conservative volume flux
and an entropy-stable surface flux: an entropy-stable (dissipative) flux
used as volume flux gives an "unpredictable" entropy balance, because $Q$
has entries of both signs (§3.3.2; [entropy stability](/properties/entropy-stability.md)).

## Ingredient II: a compatible subcell finite-volume scheme

The LGL nodal values are read as subcell values (the nodes are not at the
subcell centres), and the same subcell form holds with
$\hat f^{\mathrm{FV}}_{(i,m)j}=\lVert n_{(i,m)j}\rVert\,h\big(u_{ij},u_{mj};n_{(i,m)j}/\lVert n_{(i,m)j}\rVert\big)$
for a two-point Riemann solver $h$ (Rueda-Ramírez et al. 2022, Eqs.
(12)–(13)). The subcell normals of Hennemann et al., derived from the
flux-differencing form,
$n_{(i,i+1)j}=Ja^{(1)}_{0j}+\sum_{l=0}^{i}\sum_{m=0}^{N}Q_{lm}(Ja^{(1)})_{mj}$
(Eq. (14); the same metrics in 3D in Rueda-Ramírez et al. 2021, App. C,
Eq. (150)), make the scheme watertight on high-order curvilinear meshes,
[free-stream preserving](/properties/free-stream-preservation.md), and
satisfy discrete subcell metric identities (Eq. (15)). With non-conservative
terms, the "native LGL" finite-volume scheme of Rueda-Ramírez et al. (2021)
is, in 1D,
$$J\mathsf w_j\,\dot u^{\mathrm{FV}}_j=h_{(j-1,j)}-h_{(j,j+1)}+\Phi^\diamond_{(j,j-1)}-\Phi^\diamond_{(j,j+1)},$$
the non-conservative term being a central difference of interface means
(Eqs. (41)–(46), after Chandrashekar–Klingenberg and Derigs et al.);
it is written with the same boundary/interior split as the DG operator,
and its interior flux may differ from the element-boundary flux (Eq. (47)).
Options for the scheme:

- Riemann solver: Rusanov / local [Lax–Friedrichs](/methods/lax-friedrichs-flux.md),
  or [HLLE, HLLEM](/methods/hll-riemann-solvers.md), which preserve positivity
  of $\rho$ and $p$; for MHD, an entropy-stable Rusanov flux whose
  dissipation acts on jumps of the entropy variables, which the
  authors motivate by stating that "Lax–Friedrichs type" dissipation on
  $[\![u]\!]$ with their Roe-type matrix is not entropy stable for MHD (Rueda-Ramírez et al. 2021,
  §3.3.1, Eqs. (52)–(60); compare the compiler check on the
  [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) page).
- Reconstruction: first order (piecewise constant), second-order minmod on
  primitive variables (keeps positivity; slopes in reference space; falls
  back to first order in the element-boundary subcells, where the
  collocated interface nodes leave minmod undefined), or minmod on scaled
  entropy variables (Fjordholm–Mishra–Tadmor), which gives an entropy-stable
  higher-order finite-volume scheme (Rueda-Ramírez et al. 2022, §2.2,
  §4 item (4)).

**The entropy-stable reconstruction (TVD-ES).** The last option is the
second contribution of [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md)
(§4, Eqs. (72)–(81)). A first-order scheme on the non-uniform LGL subcells
imprints the mesh on the solution (Fig. 6). Their interior subcell flux is
an entropy-conservative flux on the subcell means minus a Roe-type
dissipation $\tfrac12R\lvert\Lambda\rvert\mathsf ZR^\top$ acting on the jump
of minmod-reconstructed scaled entropy variables $\tilde w=R^\top w$, with
$\mathsf Z$ Barth's diagonal scaling (page-local $\tilde w$, $\mathsf Z$).
It is entropy stable if the reconstructed jumps have the sign of the
cell-mean jumps, componentwise (the sign property), and the authors recall
that minmod is the only symmetric TVD limiter with that property. The
reconstruction is done in reference space; of three treatments of the
element-boundary subcells, none at all (piecewise constant there) gives the
best Orszag–Tang results and is used throughout. Matching the finite-volume
boundary values to the DG ones keeps the boundary terms of the two schemes
identical, the hypothesis of the blending lemma below; the scheme needs the
connectivity of the DGSEM only, so it replaces the volume integral
"without any additional MPI communication". The scheme is the
[TeCNO](/methods/tecno-scheme.md) construction on LGL subcells.

With first-order reconstruction and the Rusanov flux the subcell scheme
**is** Pazner's low-order sparse invariant-domain-preserving scheme
(Rueda-Ramírez et al. 2022, Prop. 1; see
[convex limiting](/methods/convex-limiting.md)). Pazner reads the
nodes as "subcell-centred values" and limits fluxes through subcell faces
(§4.1.3, Fig. 2), but does not state the equivalence.

## Ingredient III: element-wise or subcell-wise blending

- **Element-wise** (Rueda-Ramírez et al. 2022, Eq. (16)):
  $\dot u_{ij}=(1-\alpha)\,\dot u^{\mathrm{DG}}_{ij}+\alpha\,\dot u^{\mathrm{FV}}_{ij}$,
  one $\alpha$ per element. Rueda-Ramírez et al. (2021) blend only the
  advective and non-conservative parts,
  $J\mathsf w_j\dot u_j=(1-\alpha)F^{a,\mathrm{DG}}_j+\alpha F^{a,\mathrm{FV}}_j-F^{\nu,\mathrm{DG}}_j$,
  and keep the visco-resistive terms pure DGSEM with BR1 gradients of the
  entropy variables, on the argument that physical diffusion adds
  dissipation at the large gradients near a shock (§3, Eq. (28);
  $F^{a}$, $F^{\nu}$ page-local).
- **Subcell-wise** (Rueda-Ramírez et al. 2022, Eqs. (17)–(18)): one
  coefficient per subcell interface,
  $\hat f_{(a,b)}=(1-\alpha_{(a,b)})\hat f^{\mathrm{DG}}_{(a,b)}+\alpha_{(a,b)}\hat f^{\mathrm{FV}}_{(a,b)}$,
  inserted in the subcell form; the update stays conservative.
  [Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md) (Remark 6,
  arXiv v1) note that with LGL nodes the DG and finite-volume fluxes at
  the element boundary coincide when the two schemes use the same surface
  flux, so the blended flux there does not depend on the coefficient and
  subcell-wise limiting is purely element-local, the point Lin, Chan &
  Tomas make for their sparse scheme ([convex limiting](/methods/convex-limiting.md)).
  [Pazner (2021)](/sources/pazner-2021.md) reaches the same structure from
  the nodal side (§4.1.3, §4.2.2, Props. 8–11): the antidiffusive residuals
  of the DGSEM minus the low-order scheme sum to zero over each element and
  along each line of nodes in each direction (Props. 8–9, from the
  Kronecker structure), so the nodal antidiffusive flux is a difference of
  subcell-face fluxes, each face is limited with one coefficient computed
  from its two nodes, and the result is conservative (Prop. 10) and, for
  convex constraints, invariant-domain preserving (Prop. 11). This
  replaces the minimization problem of Lohmann et al.'s multidimensional
  subcell limiter by a dimension-by-dimension procedure.

**The blending lemma** ([Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md),
§3.3.3, Lemma 3, Eqs. (62)–(71); 3D curvilinear, Lemma 6, App. C). If two
schemes have identical element-boundary terms (same surface flux and same
surface non-conservative term) and arbitrary interior terms that depend
only on the element's states, the element-wise blend has the entropy
balance
$$\sum_jJ\mathsf w_j\,\dot\eta_j=\dot\eta_{\partial K}+(1-\alpha)\,\dot\eta^{\mathrm{DG}}_K+\alpha\,\dot\eta^{\mathrm{FV}}_K,$$
the convex combination of the interior entropy productions plus the common
boundary part ($\dot\eta$ terms page-local). The blend is entropy
conservative if both parts are, for any element-wise varying $\alpha$, and
entropy stable if one part is entropy stable and the other conservative or
stable. For the hybrid scheme the interior productions are
$\sum_{j,k}Q_{jk}r^{\mathrm{DG}}_{(j,k)}$ and
$\sum_{j=0}^{N-1}r^{\mathrm{FV}}_{(j,j+1)}$, so the DG volume flux, the
interior finite-volume flux and the surface flux control entropy
independently (Eq. (71); $r$ the interface entropy productions,
page-local). On 3D unstructured curvilinear meshes the result needs the
discrete metric identities and the subcell metrics above (Lemmas 4–6). The
lemma generalizes Hennemann et al. (Euler, first-order subcells) to
non-conservative systems and to higher-order subcell schemes.

Element-wise blending is simpler and therefore admits this global entropy
estimate; it is typically more dissipative than subcell blending. The
entropy proof for subcell-wise blending is "still missing"
(Rueda-Ramírez et al. 2022, §4 item (2)); Lin & Chan (2024) obtain one by
constraining the subcell coefficients (next section).

## Subcell coefficients that enforce the cell entropy inequality

[Lin & Chan (2024)](/sources/lin-2024.md) (§3, Thms 3.1–3.3, Algorithms
1–3) choose the subcell-wise coefficients so that the blended LGL-DGSEM
satisfies the **semi-discrete cell entropy inequality** of each element,
the property of entropy-stable DG, instead of a nodal entropy condition.
They write the high- and low-order schemes as algebraic subcell fluxes,
$\mathsf m_i\dot u_i=\hat f_i-\hat f_{i-1}$ with
$\hat f_i=l_i\hat f^{\mathrm H}_i+(1-l_i)\hat f^{\mathrm L}_i$ and
$l_i=1-\alpha_i\in[0,1]$ the weight of the high-order flux at the subcell
interface between nodes $i$ and $i+1$ ($\mathsf m_i$ the lumped LGL mass,
page-local $l_i$); the low-order scheme is the sparse graph-viscosity
subcell scheme of Lin, Chan & Tomas (2023), positivity-preserving and
semi-discretely entropy stable ([convex limiting](/methods/convex-limiting.md)).
Both schemes share the local Lax–Friedrichs interface flux, so their
element-boundary fluxes coincide and the surface part of the entropy
balance does not depend on the coefficients (Eqs. (17), (22)). The cell
entropy inequality then reduces to one linear inequality in the volume
coefficients, in 1D
$$\sum_{i=1}^{N}(w_i-w_{i+1})^\top\hat f_i(l_i)\le\psi(u_{N+1})-\psi(u_1),$$
with $w$ the entropy variables and $\psi$ the entropy flux potential of
registry §6, nodes numbered $1,\dots,N+1$ (Eq. (23)). The coefficients
solve the linear program
$$\max\sum_il_i\quad\text{subject to the inequality above and}\quad0\le l_i\le l^{\mathrm C}_i,$$
where $l^{\mathrm C}_i$ are the coefficients that any convex-constraint
limiter allows (Eq. (25); page-local $l^{\mathrm C}$). $l=0$ is feasible
because the low-order scheme is entropy stable, so the program is always
solvable, and its solution is conservative, entropy stable and keeps the
convex constraints (Thm 3.1). It is a continuous knapsack problem, solved
exactly by a greedy algorithm that releases the subcells in decreasing
order of their entropy production, at cost $O(m\log m)$ with
$m=N(N+1)$ per element and direction (Thm 3.2, Algorithm 2). In 2D the
inequality is imposed dimension by dimension, which reduces the unknowns
per direction from $(N+2)(N+1)$ to $N(N+1)$ (Eqs. (29)–(46), Thm 3.3). A
shock-capturing variant tightens the bound by the factor $1-\beta_{\mathrm e}\epsilon_K$,
with $\epsilon_K\in[0,1]$ the modal smoothness factor of Pazner's
[indicator](/definitions/troubled-cell-indicator.md) and a user parameter
$\beta_{\mathrm e}\in[0,1]$, which blends in that fraction of the
low-order entropy dissipation (Eqs. (49)–(51); $\beta_{\mathrm e}$,
$\epsilon_K$ registry §10).

**Evidence** (§4; Euler, SSPRK(3,3), Davis wave speeds;
[DGSEM](/methods/dgsem.md)):

| Test | Setup | Finding |
|---|---|---|
| modified Sod tube (sonic rarefaction) | $N=3$, 50 and 100 elements, $t=0.2$ | DGSEM alone shows an entropy-violating jump at the rarefaction; ESDG and DGSEM with the cell-entropy limiter give a smooth rarefaction (Fig. 2) |
| [KPP rotating wave](/benchmarks/kpp-rotating-wave.md) | $N=3$, $64^2$ and $128^2$ elements | DGSEM with Hennemann blending converges to a non-entropic solution, with the cell-entropy limiter to the entropic one (Fig. 3) |
| [isentropic vortex](/benchmarks/isentropic-vortex.md) | $N=1$–4, $2K_{\mathrm e}\times K_{\mathrm e}$ elements, $K_{\mathrm e}=5$–80 (page-local), no convex constraint | finest $L^2$ rates 1.84, 2.74 (printed), 4.28, 4.36; the local minimum entropy principle gives at most first order (0.86–0.95), its relaxed form at most second (1.21–1.52) (Tables 1–3) |
| [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md) | $N=3$, $80^2$, $t=10$, relaxed positivity | robust; applied to ESDG instead of DGSEM the turbulent structures differ visibly (Figs. 4–5) |
| [Mach 2000 jet](/benchmarks/high-mach-astrophysical-jet.md) | $N=3$, $150^2$, $t=10^{-3}$ | robust with TVD-like density bounds; with $\beta_{\mathrm e}=0.01$ and 0 carbuncles appear, also with the minimum entropy principle; the carbuncle effect, the authors write, "is not due only to a loss of entropy stability, but rather a lack of sufficient dissipation near shocks" (Figs. 6–7, A.8) |

The authors present the method as an alternative to the local minimum
principle on $\rho^{1-\gamma}e$ of Pazner and Rueda-Ramírez et al., which
they find limited to compressible flow and to at most second order, and
to Tadmor's entropy condition on each subcell flux, which by private
communication also does not keep high order for DGSEM (§1, footnotes 1,
9). High order with the new limiter is shown, not proved (§4.2).

## Ingredient IV: a priori or a posteriori coefficients

- **A priori**: a [troubled-cell indicator](/definitions/troubled-cell-indicator.md)
  evaluated on the previous step. The modal-energy indicator of Hennemann et
  al. maps the share of energy in the top Legendre modes through a logistic
  function to $\alpha$ (Rueda-Ramírez et al. 2022, Eqs. (19)–(22);
  Rueda-Ramírez et al. 2021, Eqs. (82)–(85)). Rueda-Ramírez et al. (2022)
  cap it by $\alpha_{\max}$; Rueda-Ramírez et al. (2021) clip it to 0 below
  $\alpha_{\min}=0.01$, relax it in time with factor 0.7 and propagate it to
  neighbours in two sweeps (Eqs. (86)–(88)). It is cheap (pure DG where
  $\alpha=0$, pure FV where $\alpha=1$) but heuristic and
  parameter-dependent.
- **A posteriori**: FCT / [convex limiting](/methods/convex-limiting.md)
  against target bounds — local min/max, Guermond–Popov bar states, or a
  fraction of the finite-volume solution.
- **Semi-discrete, on the bar states**: monolithic convex limiting
  (Rueda-Ramírez et al. 2024, §2.2) limits each subcell antidiffusive
  flux in closed form so that the two bar states of the interface stay in
  their bounds, before any time step; the limited operator then depends on
  the state, not on $\Delta t$, unlike FCT/IDP, whose antidiffusive
  correction and bounds depend on the step ([convex limiting](/methods/convex-limiting.md)). In Pazner's method the a priori
  modal indicator serves a different purpose: it relaxes the a posteriori
  bounds toward global ones in smooth elements, which recovers the design
  order (§4.4, §5.1).

Existing methods as members (Rueda-Ramírez et al. 2022, §3–§4): Pazner's
sparse IDP DG = standard DGSEM + first-order Rusanov subcell FV + element-
or subcell-wise blending + a posteriori Zalesak-type limiting for positivity
of density and specific entropy (with an a priori Persson–Peraire pre-check
at high $N$, because the bar-state bounds alone are very restrictive);
Hennemann et al.'s entropy-stable shock capturing = split-form
entropy-stable DGSEM + subcell FV + element-wise blending + a priori modal
indicator. Rueda-Ramírez et al. (2021) add a third: split-form
entropy-stable DGSEM with non-conservative terms + first-order or TVD-ES
subcell FV + element-wise blending of the advective part + a priori modal
indicator with clipping and relaxation. Rueda-Ramírez et al. (2024) a
fourth: split-form DGSEM (Ranocha's or Chandrashekar's volume flux) +
first-order Rusanov subcell FV + subcell-wise blending + semi-discrete
monolithic convex limiting of density, ratio quantities, pressure and
entropy on the bar states.

## Limiting-amount diagnostics

Rueda-Ramírez et al. (2022, Eq. (45)) measure the amount of low-order
method by the maximum of $\alpha$ over a time window and by its
volume-weighted mean over the domain and over the Runge–Kutta stages,
$\bar\alpha$ ($\bar\alpha=1$ all finite volume, $\bar\alpha=0$ all DG).

## Measured effects

**Rueda-Ramírez, Pazner & Gassner (2022).** All tests use SSP-RK3 of
Shu–Osher with CFL 0.5, coefficients recomputed at every stage (§5); FLUXO
for all but the KPP case, which uses Trixi.jl
([FLUXO](/software/fluxo.md), [Trixi.jl](/software/trixi-jl.md)).

| Test | Setup | Finding |
|---|---|---|
| [KPP rotating wave](/benchmarks/kpp-rotating-wave.md) | $N=3$, $32^2$–$256^2$ elements, $t=1$, element-wise a priori, $\alpha_{\max}=0.5$ | standard DGSEM converges to a clean but **non-entropic** solution; entropy-stable split-form DGSEM converges to the entropy solution (Figs. 2–3) |
| [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md) | $N=7$, $64^2$ elements, $t=10$, bounds $\rho\ge0.1\rho^{\mathrm{FV}}$, $p\ge0.1p^{\mathrm{FV}}$ | subcell-wise blending needs about three orders of magnitude less low-order method ($\bar\alpha$) at a similar peak $\alpha$ (§5.2.1, Fig. 4) |
| Mach 4 bow shock | $N=5$, curved third-order mesh, subcell IDP bounds (bar states + entropy), first-order Rusanov FV | bounds met to machine precision; shock sharp inside elements; $\bar\alpha=11.03\%$ (864 elements) and $9.50\%$ (1536) |
| [Mach 2000 jet](/benchmarks/high-mach-astrophysical-jet.md) | $N=3$, $256^2$ elements, $\gamma=5/3$, $t=10^{-3}$ | robust with both blendings; resolution improves from FV-Rusanov to FV-HLLE to second-order FV-HLLE; subcell-wise sharper than element-wise |
| [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) (GLM-MHD) | $N=3$, $256^2$ elements, $t=1$, subcell-wise TVD-like density bounds | second-order subcell FV limits less and develops more turbulent structure than first-order FV |

On the KPP problem the decisive ingredient is the entropy stability of the
high-order scheme, not the shock capturing (§5.1); see
[entropy stability](/properties/entropy-stability.md).

**Rueda-Ramírez et al. (2021)** (§6; FLUXO, SSPRK(5,4) of Spiteri–Ruuth,
CFL 0.5, $\gamma=5/3$).

| Test | Setup | Finding |
|---|---|---|
| free-stream preservation | heavily warped 3D mesh, $10^3$ elements, $N=4$, random element-wise $\alpha$ redrawn every stage | $\lVert\partial_tu\rVert\sim10^{-13}$–$10^{-12}$ at $t=0$, deviations $\sim10^{-13}$ (EC) and $10^{-14}$–$10^{-15}$ (ES, TVD-ES) at $t=1$ (Table 1) |
| weak magnetic blast | same mesh, $N=4,6$, CFL 0.4 to 0.025 | the entropy error of the EC blend goes to zero at fourth order in the time step, the order of the time integrator; ES and TVD-ES dissipate entropy (Fig. 5) |
| [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) | pure FV ($\alpha=1$), $N=7$, $256^2$ DOFs; blended, $N=3,7$, up to $1024^2$ DOFs, $t=1$ | TVD-ES resolves more and imprints less than first-order FV (Fig. 6); the blended scheme approaches Athena's constrained-transport solution as the resolution grows; $N=7$ needs smaller $\alpha$ than $N=3$ (Figs. 7–10) |
| GEM reconnection | resistive GLM-MHD, $N=3,7$, up to $1024\times512$ DOFs, $t=100$ | the entropy-stable DGSEM alone crashes from loss of positivity; with small amounts of blending the runs complete; at equal DOFs $N=3$ reconnects faster than $N=7$ (Fig. 14) |
| Io–plasma torus | 165 888 curved hexahedra, $N=4$ (20.7 M DOFs), TVD-ES, $t=10$ | little blending, mostly in Io's atmosphere; some features of the Galileo I31 magnetometer data reproduced after offsets in $B_1$, $B_2$ (Figs. 17–19) |

**Pazner (2021)** (§4.1.4, §5; MFEM, SSP-RK3, half the IDP time-step
bound). At fixed 320 degrees of freedom on two square waves, element-wise
limiting does not improve beyond $N=1$, while subcell limiting improves
with $N$ (Fig. 3); on [solid-body rotation](/benchmarks/solid-body-rotation.md)
subcell limiting is less diffusive than element-wise limiting ($25^2$,
$N=3$, Fig. 4), and on $64^2$ elements with $N=3$ the subcell FCT solution
has range $[0,1]$ and $L^1$ error $1.1\times10^{-2}$, against
$[-0.21,1.16]$ and $1.0\times10^{-2}$ unlimited and $[0,0.66]$ and
$8.5\times10^{-2}$ for the low-order scheme (§5.4, Fig. 10). At equal
degrees of freedom higher $N$ resolves the
[Sod](/benchmarks/sod-and-lax-shock-tubes.md) contact and the
[Shu–Osher](/benchmarks/shu-osher-problem.md) smooth structure better, and
$N=3$ on $64^2$ elements beats $N=1$ on $128^2$ on
[Riemann configuration 12](/benchmarks/two-dimensional-riemann-problems.md);
the [double Mach reflection](/benchmarks/double-mach-reflection.md) at
$2400\times600$ elements, $N=3$, shows Kelvin–Helmholtz roll-ups near the
triple point (§5.2–§5.7).

**Peyvan et al. (2023).** [Peyvan, Shukla, Chan & Karniadakis (2023)](/sources/peyvan-2023.md)
use the element-wise blending of Hennemann et al., "identical" to it, in
an entropy-stable DGSEM for one-dimensional strong-shock and reacting
problems: $\alpha$ is constant per element, set from the decay of the
modal energy and capped at a user-defined $\alpha_{\max}=0.5$, and the
subcell fluxes are HLLC (§2.3.1, Eqs. 55–56). Against spectral
difference and flux reconstruction stabilized by the adaptive entropy
filter, Zhang–Shu positivity-preserving modal DG and positivity-preserving
fifth-order finite-difference WENO (§4.1–4.3):

| Test | Setup | Finding |
|---|---|---|
| [Leblanc shock tube](/benchmarks/leblanc-shock-tube.md), pressure ratio $10^9$ | 1000 elements, $N=3$, Chandrashekar volume flux | smallest oscillations; discontinuities smeared more than by FR and SD, which the authors attribute to the per-element shock detection; FR and SD overshoot, SD the most (Fig. 1) |
| Mach-10 variant of the [Shu–Osher problem](/benchmarks/shu-osher-problem.md) | 170 elements, $N=3$, reference on 3000 | resolves the dip at $x=2.82$, which SD and FR miss, and the valley at $x=3.265$, which FR misses (Fig. 2) |
| three-species reacting Sod | 800 elements, $N=3$ | correct solution, no oscillations, comparable with WENO; modal DG gives non-physical species densities (Fig. 3) |

They conclude that the blended scheme is the most robust, with the
fewest tuning parameters, and extend it to five-species air in
thermochemical non-equilibrium with new entropy-conservative fluxes
([entropy-conservative fluxes](/methods/entropy-conservative-flux.md)).

**Rueda-Ramírez et al. (2024)** (§3, Trixi.jl). With monolithic convex
limiting the LGL-DGSEM keeps its design order under positivity bounds
only (mean orders 4.16 for $N=3$, 4.75 for $N=4$ on a density wave) and
drops to 1.82 and 1.61 under tight local bar-state bounds (Tables 1–4).
On a Mach-2000 jet ($N=3$, $256^2$ elements) its number of time steps
is inversely proportional to the CFL number, while that of the FCT/IDP
subcell limiter of Rueda-Ramírez, Pazner & Gassner is not, and the
FCT/IDP solution changes markedly with the CFL number (Table 5, Fig. 8).
Details are on the [convex limiting](/methods/convex-limiting.md) page.

**Lin et al. (2023).** [Lin, Chan & Tomas (2023)](/sources/lin-2023.md)
read their sparse low-order DG scheme as a subcell finite-volume scheme
with Lax–Friedrichs-type fluxes on the node graph (§6.2, Eqs. 47–48),
which is how they prove its semi-discrete entropy stability, and state
that their approach most closely resembles those of Hennemann et al. and
Rueda-Ramírez & Gassner; the blending is element-wise, with a
coefficient from positivity constraints ([convex limiting](/methods/convex-limiting.md)).

## Element switching on finer, equidistant subcells

[Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) extend FLEXI's
a priori subcell scheme (Sonntag and Munz, as recalled), which differs
from the framework above in all four ingredients. The DG scheme is a
Legendre–Gauss collocation DGSEM, not LGL. A troubled element is
switched as a whole ($\alpha\in\{0,1\}$) to a second-order
finite-volume scheme with piecewise-linear minmod reconstruction on
$N_{\mathrm{FV}}^d$ subcells that are **equidistant in reference space**
(page-local $N_{\mathrm{FV}}$ per direction), not the LGL subcells
(§4.1–4.2). Because the subcells do not share the DG degrees of freedom,
two transfer operators are needed (§4.3, Eqs. (27)–(30)):

- DG to FV: the subcell integral means of the DG polynomial, computed
  with the DGSEM quadrature on each subinterval;
- FV to DG: for $N_{\mathrm{FV}}>N+1$ an overdetermined problem, solved by
  least squares constrained by conservation of the element integral (a
  discrete projection, after Dumbser and Zanotti), with
  $V^{\mathrm{FV2DG}}\circ V^{\mathrm{DG2FV}}=I$ (page-local operator
  names).

Subcell metric terms are the subcell means of the DG metrics (Eqs.
(19)–(21)); DG/FV faces are evaluated on the subcell face distribution
and transformed back (Fig. 2). The novelty is the subcell count. FLEXI
used $N_{\mathrm{FV}}=N+1$; Mossier et al. take $N_{\mathrm{FV}}=2N+1$
from Dumbser et al.'s a posteriori subcell limiter, the largest count
that does not shorten the explicit step, since the DG step scales with
$\Delta x/(2N+1)$ and the subcell step with $\Delta x/N_{\mathrm{FV}}$
(Eqs. (18), (31)); in a $p$-adaptive run one global
$N_{\mathrm{FV}}=2N_{\max}+1$ is used. Equality of the two limits gives
$N_{\mathrm{FV}}=2N+1$ only up to the Runge–Kutta factors, which depend
on $N$ *(compiler check, not in the sources)*. The step counts confirm
it: 4695, 4726 and 4765 steps on the double Mach reflection, 235, 241
and 248 on a 3D explosion, for the static, $p$-adaptive and finer-subcell
setups (Tables 3, 6). The switch is a priori, by a modal-decay
[indicator](/definitions/troubled-cell-indicator.md) checked before the
step and after each stage for DG-to-FV, which they call "a priori", as
against the "a posteriori FV sub-cell limiting" of Dumbser et al. (§1;
[MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md)).

Measured effects (§8): free-stream preservation on a curved hybrid mesh
with $N_{\mathrm{FV}}=15$ to $10^{-13}$–$10^{-16}$ (Table 1); DG/FV
interfaces emit acoustic waves, strongest for $N_{\mathrm{FV}}=N+1$,
which $N_{\mathrm{FV}}=2N+1$ "almost completely avoids" (schlieren
images, Figs. 13, 16); the finer subcells sharpen shocks on Sod, the
[double Mach reflection](/benchmarks/double-mach-reflection.md) and the
[forward-facing step](/benchmarks/forward-facing-step.md), and improve
the wake of a transonic airfoil where only about three elements are
limited. With $p$-adaptation the authors call the result "hp-adaptive";
see [h- and hp-adaptation](/methods/hp-adaptation.md). They do not use
split-form DG, to isolate the stabilizing effect of the subcells (§9).

## Subcells on Legendre–Gauss nodes

Two sources build the subcells on Legendre–Gauss nodes, which exclude the
element boundary, and size them by the Gauss weights.

**Hard switching with a compact subcell reconstruction.**
[Deng et al. (2025)](/sources/deng-2025.md) couple a modal Legendre DG
scheme of degree $N$ (Gauss quadrature, SSP-RK3, BR2 viscous terms;
[Bassi–Rebay](/methods/bassi-rebay-viscous-discretization.md)) to a
finite-volume scheme on non-uniform subcells (§3.1–3.2, Fig. 2):

- the subcell values are the DG values at the Gauss points, the subcell
  widths the Gauss weights ($\mathsf w_i\times\mathsf w_j$ in 2D), and the
  point value is *treated as* the subcell average, without exact
  averaging; the way back to modal coefficients solves the mass-matrix
  system with the Gauss-weighted point values on the right (Eq. (3.6));
- the subcell reconstruction is their non-uniform-grid
  [ROUND](/methods/round-scheme.md) scheme, third order away from
  $\tilde u_i\approx0,1$ and free of smoothness indicators; viscous terms on
  the subcells use second-order central differences;
- the subcell face fluxes at element boundaries coincide with the DG
  surface Gauss points, are stored, and are used directly by the DG
  neighbour on DG–FV interfaces;
- a troubled element is switched as a whole, at every Runge–Kutta stage,
  by a relaxed [BVD](/definitions/boundary-variation-diminishing.md)
  criterion: a subcell is discontinuous if the total boundary variation
  of the third-order linear reconstruction exceeds that of the first-order
  one by more than $\max\big(10^{-6},10^{-4}(\lvert\bar u_{i-1}\rvert+\lvert\bar u_i\rvert+\lvert\bar u_{i+1}\rvert)\big)$;
  an element is troubled if any subcell (1D) or more than half of them
  (2D) are (Eqs. (3.7)–(3.9);
  [troubled-cell indicator](/definitions/troubled-cell-indicator.md));
- an a posteriori positivity fix recomputes the subcells with a
  first-order Godunov scheme where negative density or pressure appears at
  Gauss points; on the viscous shock tube at $\mathrm{Re}=1000$ it was needed,
  and triggered only, at the start (§4.6;
  [viscous shock tube](/benchmarks/viscous-shock-tube.md)).

They classify subcell methods as hard switching, a priori or a posteriori
(MOOD), against seamless convex blending, and as equidistant subcells
reached by projection against quadrature-sized subcells; they side with
Hennemann et al. that projecting onto equidistant subcells gives a
non-conservative blended form, and add that equidistant subcells change
the data structure, break compactness and add cost and load imbalance
(§1, §3.2). Mass, momentum and energy are conserved to $O(10^{-16})$ over a
vortex run on
$40\times40$ elements (Table 3). Comparisons at matched degrees of freedom
(§4): on the [Woodward–Colella blast wave](/benchmarks/woodward-colella-blast-wave.md)
third order with 130 elements (390 DOFs) is competitive with Vilar's
ninth-order DG with first-order subcell correction at 540 DOFs (Fig. 9); on
the [Shu–Osher problem](/benchmarks/shu-osher-problem.md) third order with
300 DOFs is comparable to or better than Hennemann et al.'s fifth-order DG
with first-order subcells at 320 and 640 DOFs (Fig. 10); and on the
[double Mach reflection](/benchmarks/double-mach-reflection.md) at fourth
order on $480\times120$ elements the resolution is better than Hennemann et
al. at similar DOFs, with small acoustic waves the authors attribute to
excessive DG/FV switching (Figs. 16–17). A third-order isentropic-vortex
study gives $L^2$ density orders 2.69, 3.40, 3.41, 2.65 with the indicator
and 2.60, 2.42, 2.47, 2.13 when 5 % of the elements are forced troubled
(Tables 1–2). On curvilinear grids the subcell metrics are taken from the
DG mapping, which "may lead to the violation of the free-stream
preservation", and is not fixed (§4.7;
[free-stream preservation](/properties/free-stream-preservation.md)).

**Convex blending on Gauss and LGL nodes.**
[Schwarz et al. (2025)](/sources/schwarz-2025.md) blend the entropy-stable
collocation DGSEM in [FLEXI](/software/flexi.md), on LGL or on Gauss
nodes, with a second-order TVD finite-volume scheme on the nodal subcells,
$(Jq)_t=\alpha\,(Jq)_t^{\mathrm{FV}}+(1-\alpha)\,(Jq)_t^{\mathrm{DG}}$, with
the nodal values read as subcell means, piecewise-linear reconstruction
with a generalized minmod limiter, $\alpha$ from Hennemann et al.'s
modified Persson–Peraire modal indicator on $\rho p$ with minimum and
maximum blending 0.01 and 0.04 at every resolution, and $\alpha_f=\max(\alpha^-,\alpha^+)$
at interfaces after Rueda-Ramírez et al. (§3.5, Eq. (26)). Only the volume
term needs blending if both schemes have the same interface solution. This
is trivially true for first-order FV on LGL nodes; for second-order FV,
or on Gauss nodes, it must be enforced by blending the surface term as
well or, on LGL nodes, by zero slopes in the outer subcells (§3.5). They
use the blend only on the compressible
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $M_0=1.25$,
$N=3$, where the Gauss-node scheme gives sharper and less oscillatory
shocks than the LGL one; oscillations of the dilatational dissipation at
$256^3$ and $512^3$ DOF are attributed to Gibbs oscillations under the
minimal blending (§4.2.2, Figs. 5–8). The paper does not claim the blend
is entropy stable on Gauss nodes.

## Other limiter classes

**Local correction of subcell fluxes.**
[Vilar & Abgrall (2024)](/sources/vilar-2024.md) write a modal DG cell on
2D unstructured or polygonal grids exactly as a subcell finite-volume
scheme with reconstructed fluxes
([DG–subcell finite-volume equivalence](/results/dg-subcell-finite-volume-equivalence.md))
and, a posteriori, replace those fluxes by first-order ones only on the
faces of troubled subcells, so that the DG solution is kept in the
admissible subcells of the same cell; they contrast this with the subcell
limiters above, which change or discard the whole DG polynomial of a
troubled cell, "a waste of information" (§1, §3; see
[MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md)).

**A posteriori recomputation on subcells.** In ADER-DG,
[Gaburro et al. (2024)](/sources/gaburro-2024.md) (§3.4) and
[Ciallella et al. (2024)](/sources/ciallella-2024.md) (§3.4) use the a
posteriori limiter of Dumbser and coworkers: the unlimited candidate is
checked for positivity and a relaxed maximum principle, troubled cells
are recomputed with a second-order MUSCL–Hancock finite-volume scheme on
triangular subcells, and a DG polynomial is rebuilt from the subcell
averages. Nothing is blended; the troubled cell's DG update is replaced.
The subcells are $N^2$ sub-triangles of each barycentric triangle of a
polygon (Gaburro et al.) or $(2N+1)^d$ sub-triangles of a triangle
(Ciallella et al.), not LGL subcells, and the subcell scheme does not
share the DG degrees of freedom; see
[MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md).
[Cernetic et al. (2023)](/sources/cernetic-2023.md) (§1) cite subcell
finite-volume treatments (Zanotti et al. 2015; Markert et al. 2021) as the
"recent advanced treatments" of shocks in DG and use a time-evolved
[artificial viscosity](/methods/artificial-viscosity.md) instead.

[Du, Shu & Zhong (2022)](/sources/du-2022.md) (§1) cite the a posteriori
subcell finite-volume limiters of Dumbser, Zanotti, Loubère and Diot as a
separate class of DG limiters, next to the WENO and Hermite WENO limiters
that replace the polynomial of a troubled cell, and develop the latter
([WENO limiters for DG](/methods/weno-limiter-dg.md)); the blending of this page instead mixes a
low-order update into the DG one, by an amount set a priori or by target
bounds.
[Maltsev et al. (2023)](/sources/maltsev-2023.md) (§2.4) find subcell
limiters attractive on uniform meshes but "not as straightforward" on
unstructured meshes of arbitrary elements with transition layers and
poor-quality cells, and possibly restrictive on the time step, while
acknowledging their extension to Voronoi meshes; they replace the higher
DG modes of troubled cells by a same-order CWENOZ reconstruction instead
([WENO limiters for DG](/methods/weno-limiter-dg.md)).

## Qualifications

- **Lin & Chan (2024): rates and printings.** The stated band
  "between $O(h^{N+1/2})$ and $O(h^{N+1})$" (§4.2) is not met by every
  last rate of Table 1 (4.28 for $N=3$ exceeds $N+1$, 4.36 for $N=4$ is
  below $N+1/2$). Two $N=2$ rates are misprinted: from the printed errors
  $\log_2(1.785\times10^{-1}/4.126\times10^{-2})=2.11$ (printed 1.11) and
  $\log_2(6.714\times10^{-3}/1.210\times10^{-3})=2.47$ (printed 2.74). The
  smoothness factor (Eq. 50; the source's symbols $s$, $s_0$, $\kappa$,
  page-local here) prints the upper case as "$1$ if
  $s<s_0+\kappa$" and a ramp $\tfrac12\big(1-\sin(\pi(s-s_0)/(2\kappa))\big)$
  that equals $\tfrac12-\tfrac12\sin(-\pi/2)=1$ at $s_0-\kappa$ and 0 at
  $s_0+\kappa$, the reverse of the outer cases (0 below, 1 above), so a
  continuous ramp needs $+\sin$; Pazner prints the same middle case, as
  recorded for Pazner's indicator on the
  [troubled-cell indicator](/definitions/troubled-cell-indicator.md) page
  *(compiler check, not in the sources)*. Their
  substate decomposition (Eq. 63) carries $\Delta t/\mathsf m_i$ in each half
  where $2\Delta t/\mathsf m_i$ reproduces the forward-Euler update
  *(compiler check, not in the sources)*. With the Davis estimate, which
  is not always an upper bound of the wave speed, the low-order scheme is
  not provably positive or entropy stable, so Theorems 3.1 and 3.3 hold
  under a true wave-speed bound (footnote 8).
- Rueda-Ramírez et al. (2022) report no convergence-order study; "high
  order" is the formal order of the DGSEM there. Pazner (2021) does: with
  the bound relaxation the subcell IDP scheme reaches order $N+1$ for
  $N\ge3$, and without it about first order (§5.1, Table 1).
- The variants with HLLE or second-order subcell reconstruction do not
  guarantee the bar-state bounds (Rueda-Ramírez et al. 2022, §5.2.3).
- The element-wise blend of Rueda-Ramírez et al. (2021) guarantees entropy
  stability, not positivity: $\alpha$ comes from a heuristic indicator, and
  the robustness on GEM and Io is empirical. The TVD-ES flux carries no
  formal second-order guarantee on the irregular LGL subcells, because the
  entropy-conservative flux is second order only on regular meshes (as
  recalled from Winters–Gassner, §4).
- The claim that the entropy-stable scheme "will converge to the unique
  entropic solution" (Rueda-Ramírez et al. 2022, §5.1) rests on a
  semi-discrete entropy inequality and numerical evidence, not on a
  convergence theorem.
- The Kelvin–Helmholtz runs differ visibly between blendings by $t=6.7$;
  the source does not use this difference to rank the blendings by
  accuracy.
- Mossier et al. call the modal-truncation projection between degrees
  "conservative"; on curved elements truncating the Legendre modes of $u$
  keeps $\int u\,d\xi$, not $\int J u\,d\xi$, so element integrals are
  conserved only for constant $J$ *(compiler check, not in the sources)*.
  They print the overdetermination condition as $N_{\mathrm{FV}}+1>N$
  (§4.3), which also holds in the square and underdetermined cases; the
  least-squares problem is overdetermined for $N_{\mathrm{FV}}>N+1$. Their
  speedups are single-core and load balancing is "work in progress"
  (§8.3, §9).
- Peyvan et al. call the blending "not problem dependent" (§4.2), yet
  $\alpha_{\max}$ is user-defined and "usually kept at 0.5"; their claim
  of the "least computational effort" (Abstract) is not supported by any
  timing, and their preference over WENO for parallel scaling (§5) by
  no scaling data. All their tests are one-dimensional.
- Printed slips of Rueda-Ramírez et al. (2021, arXiv v1) that touch this
  page: the middle case of the clipping (86) reads
  "$\tilde\alpha_{\min}\le\alpha\le\alpha_{\max}$" for
  $\alpha_{\min}\le\tilde\alpha\le\alpha_{\max}$; the boundary slopes (79)
  and the first argument of $\Theta_N$ in (80) use the node $0$ of the own
  element where symmetry with $\Theta_0$ requires node $N$ *(compiler
  check, not in the sources)*; neither affects the variant used, which has no boundary
  reconstruction.

# Citations

- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — arXiv v2: §2.1 (Eqs. (2)–(11)); §2.2 (Eqs. (12)–(15)); §2.3 (Eqs. (16)–(18)); §2.4 (Eqs. (19)–(29)); §3 (Props. 1–2); §4; §5 (Eq. (45), Figs. 2–11); §6.
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — arXiv v1: §1; §3 (Eqs. (28), (31)–(37), (41)–(47)); §3.3 (Lemmas 1–3, Eqs. (52)–(71)); §4 (Eqs. (72)–(81)); §5 (Eqs. (82)–(88)); §6 (Tables 1, Figs. 5–19); App. C (Lemmas 4–6, Eq. (150)).
- [Pazner (2021)](/sources/pazner-2021.md) — arXiv v1: §4.1.3–§4.1.4 (Figs. 2–4); §4.2.2 (Props. 8–11); §4.4; §5 (Table 1, Figs. 7–13).
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — §1 (subcell finite-volume limiters named as a class).
- [Peyvan, Shukla, Chan & Karniadakis (2023)](/sources/peyvan-2023.md) — arXiv v1: Abstract; §2.3.1, Eqs. (47)–(56); §4.1–4.3, Figs. 1–3; §5.
- [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) — arXiv v2: §1; §6.2, Eqs. (47)–(48).
- [Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md) — arXiv v1: §2.1–2.2, Remarks 1, 6; §3.1, Tables 1–4; §3.5, Table 5, Fig. 8.
- [Gaburro et al. (2024)](/sources/gaburro-2024.md) — arXiv v1: §3.4 (a posteriori subcell limiter).
- [Ciallella et al. (2024)](/sources/ciallella-2024.md) — arXiv v1: §3.4, Remark 1.
- [Cernetic et al. (2023)](/sources/cernetic-2023.md) — accepted manuscript: §1.
- [Maltsev et al. (2023)](/sources/maltsev-2023.md) — §2.4.
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §1; §3.3, Eq. (18); §4.1–4.3, Eqs. (19)–(31), Fig. 2; §7.2; §8.1, §8.6–§8.9, Tables 1, 3, 6, Figs. 13, 16; §9.
- [Deng et al. (2025)](/sources/deng-2025.md) — §1; §3.1–3.3, Eqs. (3.6)–(3.9), Fig. 2; §4.2–4.7, Tables 1–3, Figs. 9–10, 16–17.
- [Schwarz et al. (2025)](/sources/schwarz-2025.md) — arXiv v1: §3.5, Eq. (26); §4.2.2, Figs. 5–8.
- [Vilar & Abgrall (2024)](/sources/vilar-2024.md) — HAL preprint v1: §1; §3.
- [Lin & Chan (2024)](/sources/lin-2024.md) — §1; §2.3; §3.1–3.4, Eqs. (15)–(51), Thms 3.1–3.3, Algorithms 1–3; §4.1–4.4, Tables 1–3, Figs. 2–7, A.8; footnotes 1, 8, 9.
