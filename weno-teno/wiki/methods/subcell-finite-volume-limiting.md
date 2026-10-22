---
type: Method
title: "Subcell finite-volume limiting for DG"
description: "Subcell finite-volume limiting makes a nodal DGSEM robust by convexly blending it, per element or per subcell interface, with a compatible low-order finite-volume scheme on the LGL subcells; the page gives the flux-differencing form, the four mix-and-match ingredients, the entropy-stable blending lemma with non-conservative terms, element switching on finer equidistant subcells, and the measured effect of each choice."
status: established
aliases: [subcell limiting, subcell FV shock capturing, hybrid DG/FV blending, element-wise blending, subcell-wise blending, native LGL finite volumes, FV subcell switching]
tags: [dg, limiting, finite-volume, positivity, entropy-stable]
timestamp: 2026-10-23T10:00:00Z
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
  dissipation acts on jumps of the entropy variables, since plain
  Lax–Friedrichs dissipation on $[\![u]\!]$ is not entropy stable for MHD
  (Rueda-Ramírez et al. 2021, §3.3.1, Eqs. (52)–(60)).
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
[convex limiting](/methods/convex-limiting.md)). Pazner himself reads the
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
(Rueda-Ramírez et al. 2022, §4 item (2)).

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
  fraction of the finite-volume solution. In Pazner's method the a priori
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
indicator with clipping and relaxation.

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
| [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md) | $N=7$, $64^2$ elements, $t=10$, bounds $\rho\ge0.1\rho^{\mathrm{FV}}$, $p\ge0.1p^{\mathrm{FV}}$ | subcell-wise blending adds about $10^3$ times less low-order method ($\bar\alpha\approx10^{-9}$–$10^{-8}$ vs $10^{-6}$–$10^{-5}$, read from Fig. 4b) at a similar peak $\alpha\approx0.025$ |
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

## Other limiter classes

[Du, Shu & Zhong (2022)](/sources/du-2022.md) (§1) cite the a posteriori
subcell finite-volume limiters of Dumbser, Zanotti, Loubère and Diot as a
separate class of DG limiters, next to the WENO and Hermite WENO limiters
that replace the polynomial of a troubled cell, and develop the latter
([WENO limiters for DG](/methods/weno-limiter-dg.md)); the blending of this page instead mixes a
low-order update into the DG one, by an amount set a priori or by target
bounds.

## Qualifications

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
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §1; §3.3, Eq. (18); §4.1–4.3, Eqs. (19)–(31), Fig. 2; §7.2; §8.1, §8.6–§8.9, Tables 1, 3, 6, Figs. 13, 16; §9.
