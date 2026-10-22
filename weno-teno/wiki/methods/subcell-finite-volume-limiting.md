---
type: Method
title: "Subcell finite-volume limiting for DG"
description: "Subcell finite-volume limiting makes a nodal DGSEM robust by convexly blending it, per element or per subcell interface, with a compatible low-order finite-volume scheme on the LGL subcells; the page gives the flux-differencing form that makes the two compatible, the four mix-and-match ingredients, and the measured effect of each choice."
status: established
aliases: [subcell limiting, subcell FV shock capturing, hybrid DG/FV blending, element-wise blending, subcell-wise blending]
tags: [dg, limiting, finite-volume, positivity, entropy-stable]
timestamp: 2026-10-21T00:00:00Z
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
recover existing methods as members of it, and test new combinations.

## Ingredient I: the high-order DGSEM in subcell-flux form

In 2D, on a curvilinear quadrilateral with tensor LGL nodes, the DGSEM in
standard or split ([flux-differencing](/methods/flux-differencing.md)) form
uses the SBP matrices $Q_{ij}=\mathsf w_i\ell_j'(\xi_i)$ and
$B=\mathrm{diag}(-1,0,\dots,0,1)$ of the
[summation-by-parts operator](/operators/summation-by-parts-operator.md)
page, with volume matrix $Q-B$ (standard) or $2Q-B$ (split) and a symmetric,
consistent two-point volume flux $f^{\mathrm{vol}}$ evaluated with averaged
metric terms (Eqs. (2)–(7)). The choice of $f^{\mathrm{vol}}$ gives
kinetic-energy preservation, entropy conservation (Ismail–Roe,
Chandrashekar) or pressure-equilibrium preservation (Shima et al.)
([entropy-conservative flux](/methods/entropy-conservative-flux.md)).

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

## Ingredient II: a compatible subcell finite-volume scheme

The LGL nodal values are read as subcell values (the nodes are not at the
subcell centres), and the same subcell form holds with
$\hat f^{\mathrm{FV}}_{(i,m)j}=\lVert n_{(i,m)j}\rVert\,h\big(u_{ij},u_{mj};n_{(i,m)j}/\lVert n_{(i,m)j}\rVert\big)$
for a two-point Riemann solver $h$ (Eqs. (12)–(13)). The subcell normals of
Hennemann et al., derived from the flux-differencing form,
$n_{(i,i+1)j}=Ja^{(1)}_{0j}+\sum_{l=0}^{i}\sum_{m=0}^{N}Q_{lm}(Ja^{(1)})_{mj}$
(Eq. (14)), make the scheme watertight on high-order curvilinear meshes,
[free-stream preserving](/properties/free-stream-preservation.md), and
satisfy discrete subcell metric identities (Eq. (15)). Options:

- Riemann solver: Rusanov / local [Lax–Friedrichs](/methods/lax-friedrichs-flux.md),
  or [HLLE, HLLEM](/methods/hll-riemann-solvers.md), which preserve positivity
  of $\rho$ and $p$.
- Reconstruction: first order (piecewise constant), second-order minmod on
  primitive variables (keeps positivity; slopes in reference space; falls
  back to first order in the element-boundary subcells, where the
  collocated interface nodes leave minmod undefined), or minmod on scaled
  entropy variables (Fjordholm–Mishra–Tadmor), which gives an entropy-stable
  higher-order finite-volume scheme (§2.2, §4 item (4)).

With first-order reconstruction and the Rusanov flux this subcell scheme
**is** Pazner's low-order sparse invariant-domain-preserving scheme (Prop. 1;
see [convex limiting](/methods/convex-limiting.md)).

## Ingredient III: element-wise or subcell-wise blending

- **Element-wise** (Eq. (16)): $\dot u_{ij}=(1-\alpha)\,\dot u^{\mathrm{DG}}_{ij}+\alpha\,\dot u^{\mathrm{FV}}_{ij}$,
  one $\alpha$ per element.
- **Subcell-wise** (Eqs. (17)–(18)): one coefficient per subcell interface,
  $\hat f_{(a,b)}=(1-\alpha_{(a,b)})\hat f^{\mathrm{DG}}_{(a,b)}+\alpha_{(a,b)}\hat f^{\mathrm{FV}}_{(a,b)}$,
  inserted in the subcell form; the update stays conservative.

Element-wise blending is simpler and admits a global entropy estimate of the
hybrid, provided the surface terms of the two schemes match (§2.2, §6,
proved in Hennemann et al. for Euler and in a follow-up for MHD); it is
typically more dissipative than subcell blending. The entropy proof for
subcell-wise blending is "still missing" (§4 item (2)).

## Ingredient IV: a priori or a posteriori coefficients

- **A priori**: a [troubled-cell indicator](/definitions/troubled-cell-indicator.md)
  evaluated on the previous step. The modal-energy indicator of Hennemann et
  al. (Eqs. (19)–(22)) maps the share of energy in the top Legendre modes
  through a logistic function to $\alpha$, capped by $\alpha_{\max}$. It is
  cheap (pure DG where $\alpha=0$, pure FV where $\alpha=1$) but heuristic
  and parameter-dependent.
- **A posteriori**: FCT / [convex limiting](/methods/convex-limiting.md)
  against target bounds — local min/max, Guermond–Popov bar states, or a
  fraction of the finite-volume solution.

Existing methods as members (§3–§4): Pazner's sparse IDP DG = standard
DGSEM + first-order Rusanov subcell FV + element- or subcell-wise blending
+ a posteriori Zalesak-type limiting for positivity of density and specific
entropy (with an a priori Persson–Peraire pre-check at high $N$, because the
bar-state bounds alone are very restrictive); Hennemann et al.'s
entropy-stable shock capturing = split-form entropy-stable DGSEM + subcell
FV + element-wise blending + a priori modal indicator.

## Limiting-amount diagnostics

Rueda-Ramírez et al. (Eq. (45)) measure the amount of low-order method by
the maximum of $\alpha$ over a time window and by its volume-weighted mean
over the domain and over the Runge–Kutta stages, $\bar\alpha$ ($\bar\alpha=1$
all finite volume, $\bar\alpha=0$ all DG).

## Measured effects

All tests use SSP-RK3 of Shu–Osher with CFL 0.5, coefficients recomputed at
every stage (§5); FLUXO for all but the KPP case, which uses Trixi.jl
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

## Qualifications

- No convergence-order study is reported; "high order" is the formal order
  of the DGSEM.
- The variants with HLLE or second-order subcell reconstruction do not
  guarantee the bar-state bounds (§5.2.3).
- The claim that the entropy-stable scheme "will converge to the unique
  entropic solution" (§5.1) rests on a semi-discrete entropy inequality and
  numerical evidence, not on a convergence theorem.
- The Kelvin–Helmholtz runs differ visibly between blendings by $t=6.7$;
  this is a statement about under-resolved chaotic flow, not about which
  blending is more accurate.

# Citations

- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — arXiv v2: §2.1 (Eqs. (2)–(11)); §2.2 (Eqs. (12)–(15)); §2.3 (Eqs. (16)–(18)); §2.4 (Eqs. (19)–(29)); §3 (Props. 1–2); §4; §5 (Eq. (45), Figs. 2–11); §6.
