---
type: Definition
title: "Hybrid RANS/LES"
description: "Scale-resolving approaches that model all turbulence with RANS in some regions or limits and resolve part of it as in LES elsewhere; the distinction from wall-modelled LES, operating modes, continuous eddy simulation, self-adaptive turbulence eddy simulation, hybrid temporal LES and sequential RANS-to-LES coupling, the deficiencies the sources identify, and applications."
status: established
aliases: [HRL, hybrid RANS-LES, RANS/LES hybrid, bridging model, hybrid turbulence model, scale-resolving simulation, SRS, continuous eddy simulation, CES, sequential RANS-LES, stress-blended eddy simulation, SBES, self-adaptive turbulence eddy simulation, SATES, very-large eddy simulation, VLES, scale-resolving hybrid model, SRH, hybrid temporal LES, HTLES]
tags: [hybrid-rans-les, rans, les, des, pans]
timestamp: 2026-10-28T17:00:00Z
---

# Hybrid RANS/LES

A hybrid RANS/LES (HRL) method lets a simulation carry all of the turbulent
stress with a RANS model where the RANS model is adequate or the grid is too
coarse, and resolve part of the turbulence, as in
[large-eddy simulation](/definitions/large-eddy-simulation.md), where the
grid allows and RANS fails (separation, reattachment, mean
three-dimensionality). Haering et al. (2022) state the goal as "employing
LES only where RANS is deficient"
([Haering et al. (2022)](/sources/haering-2022.md), §I). Dzanic et al. (2022)
place hybrid ("bridging") models within scale-resolving simulation, which
relaxes the resolution requirements of LES while resolving the dominant
flow physics, with the intent "to resolve only the coherent flow structures
while modeling the stochastic portion of the flow"
([Dzanic et al. (2022)](/sources/dzanic-2022.md), §1).
Carlsson et al. (2023) describe hybrid RANS-LES modelling as "more accurate
than RANS and computationally more affordable than LES for the aeronautical
industry", its key feature being RANS-type behaviour near solid walls and
LES far from them; the common methods stem from DES, of which delayed DES
is "considered to be the most mature for industrial use", next to IDDES,
HYB0, PANS and zonal DES
([Carlsson et al. (2023)](/sources/carlsson-2023.md), §1). Cai et al. (2022)
group hybrid RANS-LES with wall-modelled LES as the routes that relax the
near-wall grid requirement of LES around ground vehicles
([Cai et al. (2022)](/sources/cai-2022.md), §I), and Placco et al. (2023)
call DES "a hybrid solution of Navier-Stokes equations using both
turbulence modelling and filtering"
([Placco et al. (2023)](/sources/placco-2023.md), §1).

## Hybrid RANS/LES and wall-modelled LES

Haering et al. (2022, §I) cite the taxonomy of Larsson et al.:

- in [wall-modelled LES](/methods/wall-modelled-les.md), LES is active in
  the whole domain, the grid does not resolve the near-wall layer, and a wall
  model supplies the wall stress from the LES velocity;
- in HRL, RANS and LES are active in distinct regions; the near-wall layer
  is generally RANS, so the wall-normal grid must resolve the viscous layer
  and the wall stress is computed directly, but there is no wall-parallel
  resolution requirement there beyond resolving the geometry and the mean
  flow.

An HRL whose RANS model is active only near the wall can therefore be read as
a wall-modelled LES. The authors expect HRL to remain preferable where RANS
represents the boundary layers over most of a body, as in most external
aerodynamics, and wall-modelled LES to be more efficient where RANS fails
almost everywhere outside the viscous layer. Lozano-Durán et al. (2022)
quote the NASA CFD Vision 2030 study as naming hybrid RANS/LES and
wall-modelled LES the most viable approaches for realistic high-Reynolds
external aerodynamics, and note that most simulations of the NASA Juncture
Flow so far used RANS or hybrid RANS solvers
([Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), §I; see
[NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md)). In the Third
High-Lift Prediction Workshop delayed detached-eddy simulation was among the
few unsteady techniques submitted next to the dominant steady RANS
([Goc et al. (2021)](/sources/goc-2021.md), §1).

Delassaux et al. (2023) give a finer automotive taxonomy: wall-resolved
LES; wall-modelled LES, which "uses a RANS model only in the innermost part
of the wall boundary layer and then switch[es] to a LES model";
wall-function LES, which resolves the boundary layer with a number of cells
independent of the Reynolds number and a first node at $y^+>30$; zonal and
embedded LES with RANS and LES regions fixed a priori; and hybrid RANS/LES
proper ([Delassaux et al. (2023)](/sources/delassaux-2023.md), §4.1; HAL
author manuscript). They cite a GPU wall-function LES of the
notchback DrivAer car whose drag error falls from 24 counts with
stress-blended eddy simulation to 10 and 2 counts with LES on 250 and 500
million cells (Menter et al., cited; §1).

Luckring & Rizzi (2024), surveying vortex aerodynamics, draw the line by
what each method resolves: wall-stress WMLES resolves the energetic motions
of the outer boundary layer and the detached shear layers, with "approximately
80% of the boundary layer" in LES, while hybrid RANS/LES of the DES97 kind
resolves only the detached shear layers, so "WMLES has the potential to be
significantly more accurate than hybrid RANS/LES in non-equilibrium flows"
([Luckring & Rizzi (2024)](/sources/luckring-2024.md), §2.4.1.5). Alberti et
al. (2025) find that, on fine grids, SA-based DDES and IDDES in a
high-order DG solver behave "more like a wall-modeled ILES rather than a
simple WMLES", the model's eddy viscosity adapting to the resolution
([Alberti et al. (2025)](/sources/alberti-2025-b.md), §4; details on the
[DES page](/methods/detached-eddy-simulation.md) and
[implicit LES](/definitions/implicit-les.md)).

Bae & Koumoutsakos (2022) draw the line differently: they list hybrid
LES/RANS, with RANS near the wall, LES outside and the interface set
implicitly by the change of model, as one of two families of wall-modelled
LES, the other being wall-flux models that replace the no-slip condition by
a modelled wall stress ([Bae & Koumoutsakos (2022)](/sources/bae-2022.md),
p. 2). Bose & Park (2018) draw it the other way and exclude hybrids from
their review of wall-modelled LES: there the LES equations with a formal
subgrid model are solved everywhere and only the wall (or a virtual-wall)
boundary condition changes, whereas hybrid RANS/LES and DES solve RANS
near the wall, either with an explicit RANS/LES delineation (zonal) or
implicitly through the closure (DES); they add that the
[log-layer mismatch](/definitions/log-layer-mismatch.md) appears in hybrid
formulations (Nikitin et al. 2000) as well as in wall-modelled LES
([Bose & Park (2018)](/sources/bose-2018.md), §1, §2.1). Zangeneh (2021),
after Shur et al., separates DES and DDES, which keep the attached boundary
layer in RANS, from the wall-modelled-LES branch of hybrids, which keeps
RANS only in a thin near-wall layer, and runs an SST-based IDDES in the
second role, with the RANS inner layer solved on an auxiliary wall grid
embedded in the coarse LES mesh and feeding the LES with wall shear stress
and heat flux ([Zangeneh (2021)](/sources/zangeneh-2021.md), §I, §II.A–B;
see [wall-modelled LES](/methods/wall-modelled-les.md)). Heinz (2020) goes
furthest and counts wall-modelled LES as the first of four groups of
hybrids (below). Mani & Dorgan (2023) take the same inclusive view from
industry: wall-modelled LES "is a hybrid approach in its own right (LES is
coupled with a wall model, similar to the well-known wall-function
treatment used in some RANS codes) and pushes the LES region into the
boundary layer" ([Mani & Dorgan (2023)](/sources/mani-2023.md), §4.5.2).
Huang et al. (2022c) cite Larsson et al.'s review for two sub-categories of
wall models, wall-stress-modelled LES and hybrid LES/RANS, and Zhu et al.'s
hybrid RANS–implicit-LES on a high-order flux-reconstruction method as a
precedent for wall modelling of implicit LES; their own wall model belongs
to the first category ([Huang et al. (2022c)](/sources/huang-2022-c.md), §I;
see [implicit LES](/definitions/implicit-les.md)).
Maeyama & Kawai (2023) take the narrow reading: near-wall modelling falls
into LES/RANS hybrids that blend RANS and subgrid eddy viscosities, DES
among them, with the switching location set explicitly or implicitly, and
wall-stress models that run the LES down to the wall, and they call only
the second "wall-modelled LES"
([Maeyama & Kawai (2023)](/sources/maeyama-2023.md), §1). The
summary of the wall-modelled-LES and lattice-Boltzmann group of the Fourth
High-Lift Prediction Workshop groups by grid instead: the very-large-eddy
simulation of the lattice Boltzmann code PowerFLOW, a $k$-$\varepsilon$-based
closure that switches to an LES-type closure through an indicator function,
follows "a hybrid RANS/LES philosophy" but is grouped with the wall-modelled
LES submissions because it runs on $y^+\gg1$ grids
([Kiris et al. (2023)](/sources/kiris-2023.md), §II.4; see
[NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md)). Thawait et al.
(2023) motivate their choice of DES by the two failures it avoids: RANS
models "not suitable" for unsteady shocks, separation and
shock/boundary-layer interaction, and the near-wall cost that restricts LES
to moderate Reynolds numbers
([Thawait et al. (2023)](/sources/thawait-2023.md), §I).

Where the whole boundary layer stays in RANS, the grid need only resolve
the free shear regions. François et al. (2022) use this argument for a
zonal detached-eddy simulation of a turbofan fan stage at a Reynolds number
of about one million, whose cost they call "much less dependent on the
Reynolds number" than that of wall-resolved or wall-modelled LES (§1); they
assert, without a cost comparison, that their 0.5 mm free-shear cells would
need more cells with wall-modelled LES ([François et al. (2022)](/sources/francois-2022.md),
§4.1). Hoy & Bermejo-Moreno (2022) recall, for shock/boundary-layer
interaction, that RANS cannot predict strong separation and its
low-frequency dynamics while DNS and wall-resolved LES are too expensive
for the long integration times needed, and that the experiment they compute
had been simulated with a dynamic hybrid RANS/LES by Zope et al.
([Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md), §1).

Elzaabalawy et al. (2023) argue from the same cost picture that RANS cannot
be dropped: thin attached boundary layers at Reynolds numbers up to $10^9$
(ships, submarines) and Spalart's estimate, which they cite, that wall-modelled
LES of a full wing will not be possible before 2045 make RANS and hybrid
RANS/LES indispensable, with RANS kept in attached layers and a seamless
RANS/LES hybridization for separation; "it is unrealistic to discard RANS
equations if one wishes to extend high-order accurate schemes to industrial
applications" ([Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md),
§1, Fig. 1). Yang & Ma (2022) give the same motivation for a
turbomachinery passage: RANS in attached boundary layers, LES away from them,
and grid savings at high Reynolds number
([Yang & Ma (2022)](/sources/yang-2022-b.md), §1).
Husson et al. (2024) put the same distinction from the lattice Boltzmann
side: in a hybrid RANS/LES the outer part of the attached boundary layer is
also RANS, so no resolved fluctuations have to be generated there, whereas
wall-modelled LES models only about the first 10% of the layer and needs
[inflow turbulence generation](/methods/inflow-turbulence-generation.md);
they present their lattice-Boltzmann zonal DES as a "fair alternative" to
both Navier–Stokes hybrids and lattice-Boltzmann wall-modelled LES,
especially for aeroacoustics ([Husson et al. (2024)](/sources/husson-2024.md),
§1, §5). Batther & Lee (2022) take up the question that Visbal & Garmann
left open after their wall-resolved LES of dynamic-stall onset, whether
"Reynolds-averaged or hybrid LES/Reynolds-averaged Navier–Stokes
approaches can be calibrated to reproduce the abrupt nature" of
laminar-separation-bubble bursting, and answer it positively for delayed
DES with transition models at about 22% of the LES grid points
([Batther & Lee (2022)](/sources/batther-2022.md), §1, §4.5; see
[dynamic stall](/definitions/dynamic-stall.md)).

Mani & Dorgan (2023, §4.5.2) report that hybrid RANS/LES is "still a
workhorse for most unsteady simulations in industry", where DES and then
delayed DES have carried unsteady simulation at Boeing, but that it is too
expensive for the many flight conditions of a database, "despite efforts to
reduce dissipation levels and thus minimize grid requirements", and "has
also struggled at times" to predict separation and reattachment in
smooth-body separation, the regime for which they see wall-modelled LES as
promising. Idelsohn et al. (2024) call the hybridization of RANS and LES "a
promising way" for separated flows, listing DES, scale-adaptive simulation
and PANS as global hybrids and DDES, shear-layer-adapted DDES and IDDES as
advanced versions, yet hold universally applicable hybrids "unaffordable"
to develop because the two approaches are incompatible where they
interact: LES models handle only subgrid fluctuations while RANS provides
a statistical average of all scales, "a challenge that is still
unresolved" ([Idelsohn et al. (2024)](/sources/idelsohn-2024.md), §1.2).
Their own route, a two-scale method whose sub-mesh stress comes from a
database of small direct simulations, is on the
[pseudo-direct numerical simulation](/methods/pseudo-direct-numerical-simulation.md)
page.

## How hybrids operate

Haering et al. (2022, §I) sort HRL methods into three modes:

1. reduce the RANS stress with a specified function so that resolved
   fluctuations can develop (e.g. the flow-simulation methodology);
2. carry distinct RANS and LES models and blend their modelled stresses;
3. carry a single model that switches internally between RANS-like and
   LES-like operation, as [detached-eddy simulation](/methods/detached-eddy-simulation.md)
   (DES), "the most ubiquitous HRL approach", does.

The switch between modes is either *unified*, responding to local model or
flow parameters and a grid measure, or *interfaced*, prescribed ab initio.
Unified switches rely on ad hoc functions tuned per flow, such as the
model-reduction factor of the flow-simulation methodology or the delaying
function of delayed DES, so the methods "may not be predictive, in general".
Dzanic et al. (2022, §1) note that most earlier high-order work on such
models concerned RANS or zonal methods such as DES.

[Partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
is a single-model unified hybrid: one parameter, the unresolved fraction
$f_k$ of the kinetic energy, moves the same transport equations between RANS
($f_k=1$) and DNS. The [active model split](/methods/active-model-split.md)
method of Haering et al. is a two-model method with no blending function at
all.

Abe's anisotropy-resolving hybrid (HLR) is a two-model blend of the second
kind: a one-equation nonlinear eddy-viscosity RANS model and the stabilized
mixed subgrid model are combined as
$\phi=(1-f_{hb})\phi_{\mathrm{RANS}}+f_{hb}\phi_{\mathrm{LES}}$, with
$f_{hb}=1-\exp\{-(C_{hb}l_{KL}/\Delta)^3\}$ and $l_{KL}$ a RANS length built from
$k^{3/2}/\varepsilon$ with near-wall damping (page-local symbols), so that
$f_{hb}\to1$, pure LES, as the grid is refined; on the backward-facing-step
grids of Abe (2021) it runs essentially as LES
([Abe (2021)](/sources/abe-2021.md), §III, App. A, Eqs. A1–A4; see
[scale-similarity and mixed models](/methods/scale-similarity-model.md)).
Zonal DES lets the user prescribe the RANS and DES zones or, in its mode 2,
detects them with a shielding function (see the
[DES page](/methods/detached-eddy-simulation.md)); Basile et al. (2023), with
mode 0+1, force RANS inside a jet nozzle and François et al. (2022) in the
core flow of a fan stage
([Basile et al. (2023)](/sources/basile-2023.md), §2.2).

Alberti et al. (2025) leave zonal approaches aside because they
need a priori knowledge of the flow, name the gray area, modelled-stress
depletion and log-layer mismatch as the main DES deficiencies, and list
X-LES, scale-adaptive simulation and stress-blended eddy simulation as
other non-zonal hybrids (§1). Guo & Wang (2025) frame DES, zonal LES and
embedded LES as the hybrid families, with modelled-stress depletion and the
grey area as the problems of the RANS-to-LES transition, and sort the DES
improvements into three groups: the LES length scale, the delay
(shielding) function and a reformulated eddy viscosity; their own model
changes the first and the third
([Guo & Wang (2025)](/sources/guo-2025.md), §1, §2.1; see the
[DES page](/methods/detached-eddy-simulation.md)).

**Wall-distance blending of one transported viscosity.** Tang et al. (2022)
blend two models in a single transport equation: the [Spalart–Allmaras](/methods/spalart-allmaras-model.md) equation
near the wall and the one-equation Yoshizawa subgrid-energy model, rewritten
as a transport equation for the eddy viscosity by substituting
$k_{\mathrm{sgs}}=\nu_t^2/(C_\mu^2\Delta^2)$, are blended term by term into
one equation for $\tilde\nu$ with a function $F$ of the wall distance alone
($F=1$ below $y_{\mathrm{RANS}}$, $F=0$ above $y_{\mathrm{LES}}$, a
hyperbolic-tangent ramp between, constants $C_{f1}=2.0$, $C_{f2}=0.2$),
after Wang et al. and Sánchez-Rocha & Menon, whom they cite
([Tang et al. (2022)](/sources/tang-2022.md), §2.1, Eqs. 1–9; page-local
$F$, $y_{\mathrm{RANS}}$, $y_{\mathrm{LES}}$). The RANS layer is "quite
thin", $y_{\mathrm{RANS}}$ about 10–20% of the boundary-layer thickness; the
SA damping $f_{v1}$ is switched off in the LES region through
$\chi^3/(\chi^3+F^{20}c_{v1}^3)$, "for the sake of fast transition"; the
subgrid constants are $C_\mu=0.02075$, $C_d=1.0$, $Pr_t=0.9$, and the scalar
fluxes use the blended viscosity
$\mu_t^{\mathrm{bl}}=F\mu_t^{\mathrm{RANS}}+(1-F)\mu_t^{\mathrm{LES}}$ (Eqs. 9, 14;
$\mu_t^{\mathrm{bl}}$ registry §11, $\mu_t^{\mathrm{RANS}}$, $\mu_t^{\mathrm{LES}}$ page-local, a
wall-distance blend, not the constrained-LES $\nu_t^{\mathrm{hyb}}$ of registry
§11 below). The Yoshizawa part also carries terms from a spatially varying
filter width (Eq. 4). The interface height is prescribed by the wall
distance.

**Bridging in the dissipation term.** Wang et al. (2021) give a general
construction of DES-type hybrids for any RANS model with a length-scale
equation: only the dissipation of the modelled kinetic energy is modified,
$\varepsilon=k^{3/2}/l$ with $l$ the RANS length in the RANS region and
$C_{DES}\Delta$ in the LES region, which returns the RANS model in the RANS
region and the [Smagorinsky model](/methods/smagorinsky-model.md) in the LES
region under local equilibrium; the construction yields a theoretical value
of $C_{DES}$ from the coefficients of the length-scale equation
([Wang et al. (2021)](/sources/wang-2021-l.md), §2.3, Eqs. 11–16; details on
the [DES page](/methods/detached-eddy-simulation.md)). They list PANS, PITM,
DES and zonal DES as the main hybrid strategies (§1). Li et al. (2022) make
the LES branch of the same construction dynamic: with
$C_{DES}=C_kC_s$ ($C_k$ the registry §11 factor of the length-scale-equation coefficients) and $C_s$ from the dynamic procedure, the hybrid needs no
calibration of $C_{DES}$ on decaying turbulence, and on the same
Reynolds-stress host it improves resolved stresses and pressure
fluctuations while leaving mean quantities nearly unchanged
([Li et al. (2022)](/sources/li-2022-k.md), §II C, §IV; details on the
DES page).

### Self-adaptive turbulence eddy simulation

Wu et al. (2023) assess the unified RANS–LES–DNS approach of Han and
coworkers, earlier called very-large eddy simulation (VLES), which they
rename *self-adaptive turbulence eddy simulation* (SATES)
([Wu et al. (2023)](/sources/wu-2023-b.md), §1, §2.1.1). The transport
equations of Menter's BSL $k$-$\omega$ model are kept unchanged (see the
[SST page](/methods/k-omega-sst-model.md)) and only the eddy viscosity is
multiplied by a resolution control function $F_r$ (registry §11 symbols
throughout this subsection):

$$\mu_t=F_r\frac{\rho k}{\omega},\qquad
F_r=\min\Big\{1,\Big[\frac{1-\exp(-\beta_FL_c/L_k)}{1-\exp(-\beta_FL_i/L_k)}\Big]^{n_F}\Big\},$$

$$L_i=\frac{k^{3/2}}{\beta^*k\omega},\qquad L_c=C_x(\Delta x\Delta y\Delta z)^{1/3},\qquad L_k=\frac{\nu^{3/4}}{(\beta^*k\omega)^{1/4}},\qquad C_x=\frac{\sqrt{0.3}\,C_s}{\beta^*}$$

(Eqs. 4–7), with the integral, cut-off and Kolmogorov lengths built from
$\varepsilon=\beta^*k\omega$, $\beta^*=0.09$ (the source's $\beta_1^*$),
$\beta_F=0.002$ and $n_F=2$ (the source's $\beta^*$ and $n$), and $C_s=0.1$,
the Smagorinsky constant of their LES comparator, giving $C_x=0.61$
(Table 1; $\sqrt{0.3}\times0.1/0.09=0.609$ *(compiler check, not in the
sources)*). $L_i$ equals $\sqrt k/(\beta^*\omega)$, the RANS length
$\sqrt k/(C_\mu\omega)$ of IDDES printed by Li et al. (2022, Eq. 5) when
$C_\mu=\beta^*=0.09$ *(compiler check, not in the sources)*. The authors
read $F_r$, defined as the ratio of the spectral integral of $E$ between
$L_k$ and $L_c$ to that between $L_k$ and $L_i$, as the fraction of
modelled kinetic energy, and the model as operating in three modes:
$L_c\gtrsim L_i$ gives $F_r=1$ (URANS), $L_k<L_c<L_i$ gives $0<F_r<1$
(LES) and $L_c\to0$ gives $F_r\to0$ (DNS) (Fig. 1). Wu et al. list
[PANS](/methods/partially-averaged-navier-stokes.md) beside DES and VLES
among the bridging methods (§1). The
renaming rests on Pope's definition, which Wu et al. quote: very-large eddy
simulation is LES whose filter and grid "are too coarse to resolve 80% of
the energy", whereas the method, they state, resolves "larger than 90%" of
the kinetic energy even on coarse grids and so performs like Pope's
traditional LES (§2.1.1). They contrast it with DES-type methods, "which
typically treat the entire attached boundary layer with a RANS approach"
(§1). In their 30P30N comparison the resolved share is shown as scatter
plots of resolved against modelled kinetic energy in the mid-span plane,
dominant even on the coarse grid, with modelled energy significant near
walls where $F_r\approx1$ (§3.2, Eq. 16, Figs. 9–10); no integrated fraction
is reported.

Wu et al. (2024) name this constant-coefficient version SATES-SM and make
the cut-off coefficient local in a variant SATES-σ, $C_x=\max(C_{x,\mathrm{base}}F_\sigma,0.15)$, $C_{x,\mathrm{base}}=0.61$,
with $F_\sigma$ (page-local, as on the SATES page) the ratio of the [sigma-model](/methods/sigma-model.md) to the
Smagorinsky eddy viscosity ($C_\sigma=3.0$, $C_s=0.1$), so that the model
lowers the eddy viscosity in pure-shear and laminar regions and captures
transition without a transition model ([Wu et al. (2024)](/sources/wu-2024.md),
§2.2, Eqs. 8–11). Both variants, their numerics and their results (channel,
square and supercritical cylinders, a stall sweep of the MD-30P30N) are on
the [SATES page](/methods/self-adaptive-turbulence-eddy-simulation.md).
Wu et al. (2024b) frame SATES again as a unified URANS–LES–DNS model
against the modelled-stress depletion, grid-induced separation and
log-layer mismatch of DES-type methods, derive its Smagorinsky limit, argue
that its fine-grid limit is LES where Speziale's VLES tends to RANS at high
Reynolds number, and couple it to a fifth-order WCNS
([Wu et al. (2024b)](/sources/wu-2024-b.md), §I, §III; on the SATES page).

**Zonal and unified, in turbomachinery usage.** Sandberg & Michelassi
(2022) divide hybrids into *zonal* approaches with predetermined RANS and
LES regions, "like in detached eddy simulations", and *unified* approaches
that blend on flow, geometry and grid properties, such as
[scale-adaptive simulation](/methods/scale-adaptive-simulation.md); they
state that the difficulty of defining a robust URANS/LES blend has so far
limited hybrids in industrial design
([Sandberg & Michelassi (2022)](/sources/sandberg-2022.md), §2.2.2.2). The
placement of DES differs from that of Haering et al. above and of Bose &
Park, see Qualifications. Li et al. (2024b) use the opposite labels for
the DES family: DES, DDES and IDDES are "seamless" hybrids, and for the
geometric complexity of high-lift transport configurations a zonal method
is "intractable to use" ([Li et al. (2024b)](/sources/li-2024-f.md), §I),
whereas the zonal DES applications on the
[DES page](/methods/detached-eddy-simulation.md) include a fan–outlet-guide-vane
stage and a subsonic jet.

### Hybrid temporal LES: the scale-resolving hybrid model

Mays et al. (2023) assess the scale-resolving hybrid (SRH) model of Duffal
et al., a hybrid temporal-LES approach derived by formally applying a
temporal filter to the Navier–Stokes equations, so that the temporal filter
width moves the model from LES to RANS, "a theoretically unified model
smoothly transitioning from RANS to LES"
([Mays et al. (2023)](/sources/mays-2023.md), §1, §2.1.2, Eqs. 9–13). The
host RANS model, the Lag elliptic-blending $k$-$\varepsilon$ model, is kept
in subfilter form and only the dissipation of the modelled kinetic energy is
multiplied, in registry symbols (subfilter quantities $k_{\mathrm{sgs}}$,
$\varepsilon_{\mathrm{sgs}}$; time-mean total $k_{\mathrm{tot}}$, the sum of the
time-mean modelled and resolved parts):

$$\varepsilon_{\mathrm{sgs}}\to\psi_H\,\varepsilon_{\mathrm{sgs}},\qquad
\psi_H=1-f_s+\frac{f_s}{r_K}\Big(\frac43-\frac13r_K^{3/4}\Big)\frac{k_{\mathrm{sgs}}}{k_{\mathrm{tot}}},$$

$$r_K=1-\max\big(0,\;1-\beta_\psi\mathrm{CFL}_H^{2/3}\big),\qquad
\mathrm{CFL}_H=\frac{\varepsilon}{k_{\mathrm{tot}}^{3/2}}\max(\Delta t\,U_s,\Delta),\qquad U_s=|\langle\boldsymbol u\rangle|+\sqrt{k_{\mathrm{tot}}},$$

with $\psi_H\ge1$ the SRH factor, $r_K$ the "SRH energy ratio", the
theoretical modelled-to-total energy ratio attainable with the given cell
size and time step, $\beta_\psi=0.69$ calibrated on decaying isotropic
turbulence and assumed constant, $\mathrm{CFL}_H$ a filtered CFL number,
$U_s$ a sweeping velocity, $\Delta$ the cube root of the cell volume and
$f_s$ the shielding function of the
[DES page](/methods/detached-eddy-simulation.md) ($\psi_H$ registry §11, the others page-local; the
printed $\varepsilon$ in $\mathrm{CFL}_H$ is not further specified). The form gives
$r_K=\min(1,\beta_\psi\mathrm{CFL}_H^{2/3})$, and $\psi_H=1$ where $f_s=0$
*(compiler check, not in the sources)*. The time means use exponential
weighting over 300 time steps, fixed by STAR-CCM+; the $r_K$ derivation
assumes an inertial-range spectrum (§2.1.2, §3.2.2). Because $\psi_H$
contains the time-mean resolved energy through $k_{\mathrm{tot}}$, the model
responds to the resolved content; the authors, after Heinz, call this a
"major difference from DES formulations" and test the model against
Heinz's two questions: under refinement the resolved fraction rises while
the total kinetic energy stays roughly constant, and in turbulent regions
the realised modelled-to-total ratio approximately matches $r_K$, diverging
in weakly turbulent or irrotational regions where the spectral assumption
fails (§3.1.1, §3.2.2, Figs. 4, 10c). The realised ratio flags
under-resolved regions a posteriori (a patch with about 40% modelled energy
at $Re_D=7.2\times10^5$), and $r_K$ from a RANS initialization gives a simple
a priori measure (§3.2.2, Fig. 13). The convective flux blends second-order
upwind and bounded central differencing with the shielding function as the
blending weight, described as upwind in the enforced RANS zones and
centred in LES-like zones (§2.2, Eqs. 14–15; see Qualifications). The
introduction cites Spalart et al. (1997) and Girimaji (2006), the
[PANS](/methods/partially-averaged-navier-stokes.md) paper, for the hybrid
approach (§1).

### A four-group classification and the mode relations

Heinz (2020) organizes a review of hybrids around one question: how a
method controls the balance of modelled and resolved motion under changes
of grid and Reynolds number ([Heinz (2020)](/sources/heinz-2020.md), §1,
§4.1). The premise is that RANS and LES equations have the same structure
and differ only in the length or time scale they are supplied with, RANS
scales being much larger (§1, §2.3). Ensemble-averaging the LES equations
gives the mode relations

$$R_{ij}=R^{\mathrm{res}}_{ij}+\langle\tau_{ij}\rangle,\qquad k_{\mathrm{tot}}=k_{\mathrm{res}}+k_{\mathrm{sgs}},\qquad \varepsilon_{\mathrm{tot}}=\varepsilon_{\mathrm{res}}+\varepsilon_{\mathrm{sgs}},$$

with $R^{\mathrm{res}}_{ij}$ the mean resolved stress (registry §11),
$\langle\tau_{ij}\rangle$ the mean modelled stress, $\varepsilon_{\mathrm{res}}$
and $\varepsilon_{\mathrm{sgs}}$ the resolved and modelled dissipation
(page-local); the dissipation split neglects a term that reaches at most
about 2%, as cited (§2.4, Eqs. 13–18). With the total scales
$L_{\mathrm{tot}}=k_{\mathrm{tot}}^{3/2}/\varepsilon_{\mathrm{tot}}$ and the
registry's modelled-to-total ratios $k_+$, $\varepsilon_+$, $L_+$, the review
sorts existing hybrids into four groups and names a weakness of each (§3):

1. **Wall-modelled LES**, algebraic or with the thin-boundary-layer
   equations between the wall and a matching height, including the
   correction $\nu_t=\nu_{t,\mathrm{tot}}-\nu_{t,\mathrm{res}}$ of Park & Moin
   (page-local subscripts: prescribed total and resolved viscosities). Its
   results depend on three design parameters, the exchange location as a
   fraction of an unknown boundary-layer thickness, the mesh distribution
   and the prescribed total viscosity, and resolving the boundary layer
   adequately makes it "orders of magnitude more expensive than original
   DES", as cited (§3.1; see [wall-modelled LES](/methods/wall-modelled-les.md)).
2. **Source-term methods**: Germano's hybrid filter, the consistent
   dual-mesh method of Xiao & Jenny with relaxation forcing, Woodruff's
   model-invariant hybrid. Their formulation is mathematically correct, but
   reconstructing LES variables is an ill-posed deconvolution and their cost
   exceeds that of LES (§3.2).
3. **RANS-bound methods**: DES, which switches only the dissipation of the
   $k$ equation, $\varepsilon\to\max\big(1,k^{3/2}/(C_{\mathrm{DES}}\Delta\varepsilon)\big)\varepsilon$
   with $C_{\mathrm{DES}}=0.65$; the author's group's unified RANS-LES
   (UNI-LES), which replaces the time scale $k/\varepsilon$ by
   $\min(\Delta k^{-1/2},k/\varepsilon)$ in all terms of the $k$ and momentum
   equations, with no $C_{\mathrm{DES}}$, and which Heinz calls "highly
   beneficial" for fluctuations in transition regions; and
   Reynolds-stress-constrained LES, which models only the fluctuation of the
   modelled stress around $\langle\tau_{ij}\rangle=R_{ij}-R^{\mathrm{res}}_{ij}$
   and can produce an unphysical mean modelled stress when the anisotropies
   of $R_{ij}$ and $R^{\mathrm{res}}_{ij}$ disagree (§3.3, Eqs. 22–23; see the
   mean-and-fluctuation splitting below).
4. **RANS-coefficient methods**: [PANS](/methods/partially-averaged-navier-stokes.md),
   PITM and SAS. PANS and PITM neglect the transport difference
   $\partial_j\big[(1-\varepsilon_+/k_+^2)\nu_t\partial_jk\big]$, which is non-zero
   in general, so that they hold strictly only for homogeneous turbulence;
   PITM is "basically equal" to PANS with $\varepsilon_+=1$, the
   maximum-transport Prandtl number and $k_+=L_+^{2/3}$ (§3.4, Eqs. 24–30).

Speziale's continuous model, $\langle\tau_{ij}\rangle=[1-\exp(-\eta_S\Delta/\eta)]^nR_{ij}$
with $\eta$ the Kolmogorov length, $n=1$ and $\eta_S=0.001$ (page-local), is
criticized for imposing the model's response without reference to the
actual resolution and for its Reynolds-number dependence through
$L_{\mathrm{tot}}/\eta$ (§3). From these weaknesses Heinz sets three
requirements for an optimal hybrid: it works from moderate to extreme
Reynolds numbers on reasonable grids with a continuous modelled/resolved
partition; it applies to many turbulence models with comparable resolution
on one grid; and the relation between grid and resolution is known and
matches the actual resolution (§4.1). The
[continuous eddy simulation](/methods/continuous-eddy-simulation.md)
derived to meet them follows. Heinz also treats lattice Boltzmann solvers
as a solver choice, not a modelling alternative: the BGK relaxation time
fixes $\nu+\nu_t$, so the same solver acts as RANS, LES or hybrid depending
on how that time is supplied (App. A; see
[lattice Boltzmann methods](/methods/lattice-boltzmann-method.md)).

### Continuous eddy simulation

The method has its own page,
[continuous eddy simulation](/methods/continuous-eddy-simulation.md). Heinz
(2022) frames the design problem of every hybrid as the "communication"
between modelled and resolved motion: the modelled viscosity must be small
enough not to extinguish resolved motion on coarse grids, yet grow for
coarser grids and higher Reynolds numbers, and "most hybrid methods" do not
address it; CES and the partially integrated transport model (PITM) are the
two the author names that do
([Heinz (2022)](/sources/heinz-2022.md), §1, Table 1). The earlier review
derives the CES destruction coefficient $1+L_+^2(\cdot-1)$ by a variational
analysis of the $k$-$\varepsilon$ and $k$-$\omega$ models, names four
variants (CES-KES, CES-KEK, CES-KOS, CES-KOK, hybridizing either the scale
equation or the $k$ equation), and from a CES–DES equivalence obtains
$C_{\mathrm{DES}}=0.75$ ($k$-$\varepsilon$) and 0.61 ($k$-$\omega$), close to
0.65 (Heinz 2020, §4.2–§4.4, Eqs. 38–55; details on the CES page). From a variational
analysis of the $\varepsilon$ equation Heinz derives three ways of making its
destruction coefficient depend on resolution: through the ratio of modelled
to total length scale (the CES choice) or through the ratio of time scales
(the PITM-type choice), and argues that the second is consistent only for
homogeneous flow unless the turbulent transport terms carry the total
viscosity (§2–§3, Table 2).

Mozaffari et al. (2024) implement in an SST host Heinz's continuous eddy
simulation (CES), which adjusts the modelled viscosity to the actual degree
of resolution so that modelled and resolved motion stay balanced under grid
and Reynolds-number changes, a construction they call "theory-based"
([Mozaffari et al. (2024)](/sources/mozaffari-2024.md), §2.3, Eqs. 33–34; HAL
accepted manuscript). The $k$-destruction is multiplied by a factor,

$$\beta^*\omega k\;\to\;\beta^*\omega k\,\psi_\beta,\qquad \psi_\beta=\beta_{\mathrm{CES}}+R(1-\beta_{\mathrm{CES}}),\qquad R=L_+^2,\qquad
L_+=\frac{\Delta_{C+}}{(1+\Delta_{C+}^3)^{1/3}},\quad \Delta_{C+}=C_+\frac{\Delta}{L_{\mathrm{tot}}},$$

with $L_+$ the ratio of the modelled to the total length scale,
$L_{\mathrm{tot}}=\sqrt k/(C_\mu\omega)$ the RANS length of SST, and
$\psi_\beta$, $L_+$, $\beta_{\mathrm{CES}}$ as in registry §11, $R$,
$\Delta_{C+}$, $C_+$, $L_{\mathrm{tot}}$ page-local. The source writes $\beta_{\mathrm{CES}}$ as $\beta$, the symbol of the SST
destruction coefficient, without defining it, and gives no value of $C_+$
nor the definition of $\Delta$. For $\Delta_{C+}\to\infty$, $L_+\to1$ and
$\psi_\beta\to1$ (the RANS dissipation); for $\Delta_{C+}\to0$,
$\psi_\beta\to\beta_{\mathrm{CES}}$ *(compiler check, not in the sources)*. Unlike the
thin transition of IDDES, the CES transition from RANS near the wall to LES
away from it is smooth (§3.2, Fig. 11). On the NACA 0012 at $45^\circ$ CES and
IDDES perform "almost the same without any superiority" ($C_L=1.192$ and
1.231, $C_D=0.993$ and 1.038, reference 1.097 and 1.180; Table 2); on the
$35^\circ$ Ahmed body with a no-slip body surface CES separates already on the
roof and over-predicts the drag (0.3779), where IDDES matches the wake
(0.2819) (§3.3, Table 3). See
[detached-eddy simulation](/methods/detached-eddy-simulation.md).

### Sequential RANS-to-LES coupling

Bouhafid et al. (2024) couple the two models in time rather than in space
to compute an aircraft wake from the jet regime to the vortex-dissipation
regime with one solver
([Bouhafid et al. (2024)](/sources/bouhafid-2024.md), §1, §2.1, Fig. 1). A
steady RANS of the whole aircraft in the aircraft frame (a
[Reynolds-stress model](/methods/reynolds-stress-model.md) on adapted meshes
for the NASA CRM, [SST](/methods/k-omega-sst-model.md) for a wing with jet)
is sliced normal to the flight direction where streamwise gradients are
negligible against transverse ones; the slice is extruded over one Crow
wavelength ($\approx8.6b_0$, $b_0$ the vortex spacing, page-local) into a
periodic box in the ground frame, where a compressible temporal LES with
the [Smagorinsky model](/methods/smagorinsky-model.md) continues. The RANS
turbulence passes to the LES as an initial synthetic field (Fourier modes
on a Pao spectrum, rescaled cell by cell to the RANS Reynolds stresses, in
the jet region only), which is no longer divergence-free after rescaling,
judged acceptable for an initial condition (§2.1; see
[inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
Without the synthetic field the LES misses the jet roll-up of a wind-tunnel
wing–jet case; with it the 22.5-million-cell temporal LES resembles an
89-million-cell zonal DES at much lower cost, no timings being given (§3.2,
Figs. 4–6). The authors contrast it with the hybrid RANS/LES near field of
Misaka et al., which captures vortex meandering better but must be at least
one Crow wavelength long (§2.1).

### Mean-and-fluctuation splitting

A family of methods builds on the decomposition of Schumann (1975), which
Haering et al. (2022, §I) cite, in which different eddy-viscosity
models act on the mean and on the fluctuating strain; the authors say it
"may actually be considered the first hybrid method". They cite:

- **two-velocity HRL** (Uribe et al.): RANS viscosity on the mean strain,
  Smagorinsky on the resolved fluctuating strain, with a hyperbolic-tangent
  length-scale blending that can cause "drastic model shifts";
- **RSC-SGS** (Chen et al.): the mean-strain RANS stress (Spalart–Allmaras
  or van Driest) reduced by the averaged resolved stress, dynamic
  Smagorinsky on the fluctuations; in expectation it returns the unaltered
  RANS stress, and its prescribed switch location makes it zonal;
- **dynamic HRL** (Bhushan & Walters): RANS on the mean blended with an
  implicit subgrid model through a ratio of productions, both active
  everywhere;
- **dual-mesh HRL**: separate RANS and LES simulations on two grids coupled
  by forcing terms that enforce consistency in expectation.

Brenner et al. (2022, §1) open their data-assimilation paper with hybrid
LES/RANS methods, among them the same dual-mesh framework of Xiao & Jenny,
as one answer to the near-wall cost of scale resolution; they cite Xiao &
Jenny for that cost, which scales "with $Re^3$ and $Re^{1.8}$ for DNS and
LES, respectively" in wall-bounded flows; their own route is the opposite, a RANS model corrected by data
([Brenner et al. (2022)](/sources/brenner-2022.md), §1; see
[grid-point requirements](/results/les-grid-point-requirements.md) and
[field inversion](/methods/field-inversion-machine-learning.md)). Ghidoni et
al. (2022) quote a RANS–implicit-LES hybrid (Islam & Thornber) and the
SA-DES of Travin et al. among the reference results for their
two-dimensional URANS of the cylinder at $Re=1.4\times10^5$, and name
hybrid RANS/LES among the targets of adaptive time integration for stiff
turbulence-model equations ([Ghidoni et al. (2022)](/sources/ghidoni-2022.md),
§1, §6.2, Table 12, §7; see [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)).

**Constrained LES near an immersed boundary.** Cai et al. (2022) use a
Reynolds-stress-constrained ("constrained LES", CLES) eddy viscosity near
the wall, after Chen et al. (2012) and Verma et al. (2013) and the authors'
own submitted work; the Chen et al. paper is the same Reynolds-stress-constrained
LES work that Haering et al. cite for RSC-SGS: both reference lists resolve
to one bibliography entry *(compiler check, not in the sources)*. In registry notation, with
$\langle\cdot\rangle$ a time average, $\tilde u_i$ the Favre-filtered velocity
and the resolved Reynolds stress (registry §11)
$R^{\mathrm{res}}_{ij}=\langle\tilde u_i\tilde u_j\rangle-\langle\tilde u_i\rangle\langle\tilde u_j\rangle$,

$$\nu_t^{\mathrm{hyb}}=\frac{2\nu_t^{\mathrm{RANS}}\langle\tilde S_{ij}\rangle\langle\tilde S_{ij}\rangle+R^{\mathrm{res}}_{ij}\langle\tilde S_{ij}\rangle}{2\langle\tilde S_{ij}\rangle\langle\tilde S_{ij}\rangle},\qquad
\frac{\nu_t^{\mathrm{RANS}}}{\nu}=\kappa y^+\big(1-e^{-y^+/19}\big)^2,$$

([Cai et al. (2022)](/sources/cai-2022.md), §II C 1, Eq. 27; $\nu_t^{\mathrm{hyb}}$,
$\nu_t^{\mathrm{RANS}}$ registry §11, the latter a mixing-length viscosity, $\kappa$
not given a value). Contracting the condition
$-2\nu_t^{\mathrm{hyb}}\langle\tilde S_{ij}\rangle+R^{\mathrm{res}}_{ij}=-2\nu_t^{\mathrm{RANS}}\langle\tilde S_{ij}\rangle$
with $\langle\tilde S_{ij}\rangle$ gives the formula: modelled plus resolved
stress, projected on the mean strain, equals the RANS stress *(compiler
check, not in the sources)*. The modelled stress is enforced up to "several
grid points from wall", because the non-conservative
[immersed boundary](/methods/immersed-boundary-method.md) otherwise loses
near-wall Reynolds stress and delays turbulence development. The authors
state that $\nu_t^{\mathrm{hyb}}$ "approaches the RANS eddy viscosity for
attached boundary layers and reduces to the LES viscosity for separated
boundary layers automatically"; the printed formula contains no subgrid
viscosity, and how the return to the Vreman subgrid viscosity is enforced is
not printed (§II C 1). They also state that "without this enhancement, the
flow stays attached even by refining the grid", with no run without it in
the paper (§IV; see [wall-modelled LES](/methods/wall-modelled-les.md)).

## Deficiencies identified by the sources

Haering et al. (2022, §II) name four deficiencies common to most HRL
formulations.

1. **Modelled-stress depletion (MSD).** If resolved turbulence is generated
   passively, by lowering the modelled stress and waiting for instabilities,
   the total stress must first be depleted: such methods "must exhibit
   regions of modeled-stress-depletion", with log-layer mismatch, reduced
   body forces, premature separation and delayed reattachment as
   consequences (see [log-layer mismatch](/definitions/log-layer-mismatch.md)).
   The authors judge explicitly introducing resolved fluctuations, at a rate
   consistent with the reduction of the modelled stress, to be "the only way
   to prevent regions of MSD", and view body forcing formally as a model of
   the commutator between the implicit filter and the substantial
   derivative (§II A). They cite Piomelli et al. for stochastic forcing at
   the RANS/LES interface, which removed log-layer mismatch in channel flow
   but is problem dependent, and Menter et al. for the forced scale-adaptive
   simulation SAS-F, which still showed log-layer mismatch.
2. **One scalar eddy viscosity for two jobs.** A hybrid model must carry a
   non-negligible share of the mean stress and the energy transfer to the
   unresolved scales; a scalar eddy viscosity cannot do both (§II B; see
   the [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)).
3. **Ad hoc blending and scalar grid measures.** The cube root of the cell
   volume tends to the smallest cell size as the aspect ratio grows and so
   overestimates the resolution; cell-diagonal measures are preferable, and
   resolution indicators should account for the anisotropy of both the grid
   and the resolved turbulence (§II C).
   Abe (2021) supplies LES evidence for the first half: on a shear layer
   resolved by cells with $\Delta x/\Delta y\sim100$, subgrid models using the
   cube root are "clearly suppressed" and lengthen the separation bubble,
   while $\max(\Delta x,\Delta y,\Delta z)$ gives reasonable eddy viscosities
   (§IV C–D, Figs. 9–11). In detached-eddy simulation the grid length differs
   by variant (see the table on the DES page); Basile et al. (2023) divide
   the cube root by $N+1$ on a high-order DG discretization (§2.2).
4. **RANS transport equations fed with fluctuating quantities.** Nonlinear
   sources calibrated on mean quantities, such as the $\varepsilon$
   destruction $C_{\varepsilon2}\varepsilon^2/k$, acquire spurious correlations
   when evaluated on fluctuating fields; a Taylor expansion shows that the
   mean of the destruction then depends on the amount of resolved
   turbulence. The rule: "what goes in to, and what comes out of,
   RANS-based transport models must be expected values". The problem
   concerns single-model unified methods, DES, PANS and PITM among them,
   and its symptoms are masked by numerical dissipation, coefficient tuning
   or averaging (§II D, Eqs. 1–2).

**An empirical interface and lost high frequencies.** In their review of
one-dimensional turbulence, Chen et al. (2024b) call hybrid RANS/LES a
trade of accuracy for cost whose RANS–LES interface is "considerably
empirical" and which loses high-frequency information under Reynolds
averaging near walls; they offer stochastic one-dimensional near-wall
closures instead ([Chen et al. (2024b)](/sources/chen-2024-c.md), §4.1; see
[one-dimensional turbulence](/methods/one-dimensional-turbulence.md)). The
review runs no hybrid simulation.

**No feedback from the resolved motion.** Heinz (2020) concludes that the
classical hybrids, wall-modelled LES and DES, feed no information about the
resolved motion back to the model, and that only PANS and PITM try, with the
shortcomings listed above (§6). In DES, adjusting the grid ratio
$\Delta/L_{\mathrm{tot}}$ to the length ratio $L_+$ is called "absurd", and
DES is said to be unstable under grid variation, citing Spalart's grid
guide (§4.4); the statements follow the CES–DES equivalence, and the review
runs no simulations (§5). Heinz also requires a hybrid's stress
model to be realizable, citing work in which dynamic LES that does not honour
realizability (the dynamic Smagorinsky model) is often unstable while
"fully realizable dynamic LES" is stable without averaging or clipping, as
cited (§2.1; see the [Boussinesq page](/definitions/boussinesq-hypothesis.md)).

**Grid changes perturb the turbulence.** Because the grid sets the split
between modelled and resolved turbulence, Mozaffari et al. (2022) show
with a DES of decaying turbulence crossing a fine-to-coarse interface that
the drop of resolved energy is never compensated by the slower decay of
modelled energy, so "a single change in mesh size causes a lasting
perturbation of the turbulence"; from "a mesh designer's perspective" they
conclude that mesh-size changes should be avoided, and adapt meshes on
time-averaged criteria so that the mesh converges to a static one
([Mozaffari et al. (2022)](/sources/mozaffari-2022.md), §1, Fig. 1, §3; see
[mesh adaptation](/methods/mesh-adaptation.md)).

Dzanic et al. (2022) stress the numerical side: the excessive dissipation of
low-order schemes harms the modelled physics of hybrid simulations more than
RANS, and they find that raising the order of a flux-reconstruction
discretization at fixed degrees of freedom benefits PANS proportionally more
than [implicit LES](/definitions/implicit-les.md) (§1, §4; see
[numerical dissipation](/properties/numerical-dissipation.md)).

**The grey area.** Carlsson et al. (2023) name the "grey-area" problem, the
delayed development of resolved turbulence in the initial LES region next
to a RANS–LES interface in free shear layers, which "may significantly
degrade" the scale-resolving result; grey-area-mitigation methods modify
the LES length scale (§1; the shear-layer-adapted length is on the
[DES page](/methods/detached-eddy-simulation.md)). With that length scale,
they find the onset of resolved turbulence in a separated shear layer
"mainly governed by the amount of numerical dissipation introduced by the
numerical scheme and the resolution of the grid" (§4.4).

**Two issues and their names.** Husson et al. (2024, §2.2, Fig. 1, after
Deck & Renard) define the vocabulary the DES-type literature uses:

- the *grey area* is the RANS-to-LES transition zone, where the modelling
  is "neither one nor the other";
- *modelled-stress depletion* ("Issue I") is a grey area inside an
  attached boundary layer, where the RANS eddy viscosity is lost before
  resolved content is sufficient, weakening the Reynolds stresses and
  giving a wrong skin friction or even *grid-induced separation*;
- the *delay in the formation of instabilities* ("Issue II") is the late
  appearance of resolved turbulence in a free shear layer, caused partly by
  RANS eddy viscosity advected from upstream into the mixing layer; "the
  smaller the grey area for mixing layer the better".

Both issues are typical of fine meshes on which the cell size falls below
$\delta$; isotropic lattice Boltzmann grids, very fine along the wall, make
DES-type models trigger them "almost systematically" (§1). The ideal
shielding keeps the whole attached layer in RANS and switches quickly to
LES in separation; its realization in zonal DES mode 2 (2020) is on the
[DES page](/methods/detached-eddy-simulation.md). Pan & Zhang (2023)
motivate DDES by the same grid-induced separation, a "nonphysical separation
phenomenon induced by Reynolds stress loss" when DES switches to LES on
grids that do not meet LES requirements
([Pan & Zhang (2023)](/sources/pan-2023.md), §II.C). Wu et al. (2023, §1),
citing Menter, list grid-induced separation and "a slow 'transition' from
RANS to LES" as the limitations of DES, DDES and IDDES that motivate
SATES. Mani & Dorgan (2023, §4.5.2) describe modelled-stress depletion as
too little modelled stress where the RANS-to-LES switch falls very near the
wall on a grid that cannot resolve the eddies there, manifest as
grid-induced premature separation, still triggered under DDES by certain
grid topologies and nearly isotropic surface meshes, and expected to worsen
with unsteady mesh adaptation; Menter's robust shielding for two-equation
hybrids is proprietary, and they ask for a public-domain one (details on the
[DES page](/methods/detached-eddy-simulation.md)).

**Numerical dissipation as a source of log-layer mismatch.** In SST-IDDES
of channel flow at $M_b=0.15$, the same model with a second-order central
scheme carrying RANS-level fourth-difference dissipation shows a
significant [log-layer mismatch](/definitions/log-layer-mismatch.md) at
$Re_\tau=395$, 2400 and 18 000: correct where IDDES runs in RANS mode,
failing "as soon as the model switches to LES due to adding to much
numerical dissipation"; the low-dissipation low-dispersion schemes leave
only a small mismatch at the interface ($y^+\approx200$ at $Re_\tau=2400$,
$\approx2000$ at $18\,000$) (Carlsson et al. 2023, §4.3, Fig. 4; see
[low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md)).

**Transition blurs the modes.** Möller et al. (2024) couple SST-based DDES
to a one-equation intermittency transition model and argue that in a
laminar or transitional boundary layer the RANS/LES distinction loses its
meaning: with $\gamma=0$ the production of the modelled $k$ is switched off
and its destruction cut to 10%, so $k$ and the RANS length stay near zero and
the length-scale test declares "RANS mode" where the model is "more a
laminar mode"; there the model "acts more like an implicit LES model", its
subgrid viscosity minimal, which explains the demand for finer meshes
([Möller et al. (2024)](/sources/moller-2024.md), §II.D, Fig. 1, p. 10;
accepted manuscript). The dynamic central/upwind flux blending of DDES,
designed for the fully turbulent RANS/LES distinction, then runs fully
upwind in the boundary layers and damps resolved inflow turbulence, and the
authors obtain their best transition predictions on a compressor cascade
only with a constant 5% upwind fraction and synthetic inflow turbulence,
noting that bypass transition is then carried by resolved scales and that
the model may act "more like an LES model" (§III.B.3, pp. 25–26). They add
that assessing transition by surface values such as the skin friction
$C_f$ alone "may lead to wrong conclusions" (§III.B.2, p. 21). Details on the
[DES page](/methods/detached-eddy-simulation.md) and the
[transition-model page](/methods/local-correlation-based-transition-model.md).

**Grey area and shielding in a temporal hybrid.** In the SRH runs of Mays
et al. (2023, §3.1.1, Fig. 5) the grey area, bounded by the isolines
$r_K=0.99$ and 0.2 (taking 80% resolution as LES), is about $0.05D$ wide on
the coarsest grid and intersects the free shear layer; its inner edge is
set by the shielding and does not move with the grid, its outer edge moves
closer to the wall and narrows on the finest grid. The factor $\psi_H$ grows
rapidly away from the wall, which the authors credit with mitigating
grey-area effects (§3.2.2, Fig. 9). The thin shielding needed for the
breakdown of the separated shear layers costs log-layer mismatch in channel
flow, which the original authors of the model reported, and the interaction
of SRH with the Lag elliptic-blending host spuriously reduces the reduced
stress function in the free stream, giving "very poor results" in
high-Reynolds channel flow (§3.2.2; see
[log-layer mismatch](/definitions/log-layer-mismatch.md)). The authors
argue that "it is likely that there is no ideal universal shielding
function" (§3.2.2).

**Where the interface should sit.** Wang et al. (2024c) require a
RANS/LES interface that is grid independent and able to distinguish
stable from unstable flow states (§III.F, as cited), and evaluate the
interfaces of SA-based DES, DDES and scale-adaptive lengths on
three wall-resolved LES fields of a Mach 2 flat-plate boundary layer: all
move toward the wall as the grid is refined ([Wang et al. (2024c)](/sources/wang-2024-j.md),
§III.F, Fig. 15). From the joint distributions of the velocity-gradient
invariants, which change little with the grid in the viscous sublayer but
markedly in the log and wake layers, they infer that the change of flow
topology happens in the buffer layer and that the "feasible region of
switching interface" from RANS to LES-like modelling lies at
$7<y^+<15$ (§III.D, Figs. 10–11). From the TKE peak (near $y^+\approx15$ on
the finest grid) and the onset of the rapid fall of the resolved
dissipation above $y^+\approx14$ on every grid, with a $k$-$\varepsilon$
eddy-viscosity argument, they propose $y^+\approx14$ as the interface of
a scale-adaptive hybrid in supersonic boundary layers (§III.E, Figs.
12–14); evaluated on the three LES fields, their shielded length places
it there on all three grids (Fig. 16; see
[scale-adaptive simulation](/methods/scale-adaptive-simulation.md)). The
flow is one Mach 2 boundary layer, and their run of the modified model is
on the coarse grid ($209\times161\times81$) only (§II, §III.B).

**Time step and dissipation in a workshop.** Kiris et al. (2023, §VI 1c)
cite a hybrid RANS/LES time-step study of the Fourth High-Lift Prediction
Workshop that attributes large inaccuracies in the wing-root separation of
the NASA CRM high-lift model at $21.47^\circ$ from the dissipation of the
large time steps that A-stable BDF2 allows; see
[numerical dissipation](/properties/numerical-dissipation.md).

## Evidence from applications

- **Four separated flows, compiled.** Heinz (2020) runs no simulation and
  compiles published results to argue that existing hybrids show
  prediction variability through their design parameters, resolution
  deficiencies and inconsistent improvements (§5):
  - on the [periodic hill](/benchmarks/periodic-hill.md) ($Re$ from 5600
    to $10^5$ on the hill height), with the measured reattachment following
    $x_R/h=0.49(Re/10^4)^{-1.4}+3.71$ (after Kähler et al.), PANS, PITM,
    wall-modelled LES, DES and Reynolds-stress-constrained LES vary widely
    with their design parameters, while SAS, source-term methods and
    UNI-LES "apparently reduce the RANS error significantly"; two PANS
    studies of the same flow recommend $f_k=0.4$ (Ma et al.) and $f_k=0.15$
    (Razi et al.) and give different reattachment trends with $f_k$, and
    PITM's modelled energy fraction does not follow the expected grid trend
    near the wall on four grids (§5.1, Figs. 6–8);
  - on the [NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md)
    ($Re_c\approx936\,000$, $M=0.1$, measured $x_R/c=1.10$) the compiled
    reattachment lies at 1.188–1.305 for RANS (errors 8–18.6%),
    1.114–1.152 for DES, 1.035–1.105 for wall-modelled LES and 1.08–1.19
    for source-term methods, and wall-modelled LES and DES miss the double
    peak of $C_f$ (§5.2, Table 3, Figs. 10–11);
  - on the Bachalo–Johnson transonic axisymmetric bump
    ($M_\infty=0.875$, $Re_c=2.763\times10^6$, measured $x_R/c=1.10$),
    wall-modelled LES cannot match both the shock and the reattachment
    maxima of $C_f$ by any choice of exchange location (§5.3, Table 5,
    Fig. 14);
  - on the [NACA 4412 airfoil](/benchmarks/naca-4412-airfoil.md) no
    methodology predicts both lift and drag accurately; DES under-predicts
    drag by more than 34%, and Reynolds-stress-based PITM hybrids reduce the
    RANS lift and drag errors from $+14\%$ and $-54\%$ to $+7\%$ and $-39\%$
    (§5.4).
- **Hovering rotor on moving Cartesian grids.** Sugaya & Imamura (2021) run
  DDES-p, an SA-based DDES with a shielding function modified for small
  streamwise grid sizes on Cartesian grids, for the
  [Caradonna–Tung rotor](/benchmarks/caradonna-tung-rotor.md) on 75 and 149
  million cells, with immersed-boundary wall functions; thrust and figure of
  merit barely change with grid and scheme, and the high-order scheme
  resolves finer wake vortices than MUSCL
  ([Sugaya & Imamura (2021)](/sources/sugaya-2021.md), §2.1, §4.5,
  Table 7, Fig. 19; details on the [DES page](/methods/detached-eddy-simulation.md)).
- **Data-driven correction of an IDDES wall model.** Zangeneh (2021)
  corrects the wall shear stress and heat flux of SST-IDDES used as a
  wall-modelled LES of supersonic flows with a random forest, and reports
  the [log-layer mismatch](/definitions/log-layer-mismatch.md) removed on a
  flat plate at $Re_\theta=50\,000$ and better separation and reattachment
  on an expansion–compression corner at $M=2.9$ (§III; details on the
  [machine-learning wall-model page](/methods/machine-learning-wall-model.md)).

- **Transitional Rayleigh–Taylor mixing.** With variable-density PANS
  (BHR closure), RANS ($f_k=1$) overpredicts mixing, with a growth rate
  $\alpha_b=0.043$ against 0.025 of the unmodelled reference, and even
  disturbs the laminar linear regime; with $f_k\le0.35$ and a suitable choice
  of the other resolution parameters PANS reproduces the reference
  ($\alpha_b=0.024$ at $f_k=0.25$); the minimum resolution is set by the need
  to resolve the bubbles and spikes that trigger turbulence ([Pereira et al. (2021)](/sources/pereira-2021.md),
  §IV.2, Table II, §V; see [PANS](/methods/partially-averaged-navier-stokes.md)
  and [Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md)).
- **Turbomachinery and jets.** Zonal DES of a fan stage matches hot-wire
  mean and RMS profiles where RANS fails in the tip gap (François et al.
  2022, §5.3–5.4); zonal DES on $hp$-adaptive DG reproduces a subsonic jet
  with fewer degrees of freedom than finite-volume references (Basile et al.
  2023, §4.2.3). Details on the
  [DES page](/methods/detached-eddy-simulation.md).
- **Separated and vortical flows.** IDDES of a backward-facing step and
  DDES-SST of a ship hull and a delta wing on adapted meshes (Mozaffari et
  al. 2022, §4–§5).
- **Full-scale car.** Delassaux et al. (2023) compare the realizable
  [$k$-$\varepsilon$](/methods/k-epsilon-model.md) and
  [SST](/methods/k-omega-sst-model.md) RANS models with SST-based delayed
  DES on a simplified estate car (Peugeot 308 SW, $Re_L=1.3\times10^7$,
  115 million cells, wind-tunnel data). The hybrid model reproduces the
  measured wake topology, a single recirculation bubble fed by the rising
  underbody flow and capped by the roof shear layer, the base pressure and
  the underbody exit flow, which both RANS models miss; its drag (0.255) is
  further from the measurement (0.244) than RANS (0.242), and the authors
  show with a cumulative drag along the car that the RANS agreement comes
  from compensating errors (§6–§7, Table 3, Fig. 13). They call it "well
  known" that hybrid RANS/LES does not improve integrated loads over RANS on
  cars, citing DDES, LES and [PANS](/methods/partially-averaged-navier-stokes.md)
  studies (§6). The hybrid run costs 18 times the wall-clock time of RANS
  on three times as many cores (§7.6). Details on the
  [DES page](/methods/detached-eddy-simulation.md).
- **Ahmed body.** Cai et al. (2022) recall body-fitted RANS and hybrid
  results for the 35° and 25° slants (DES, IDDES, PANS, embedded LES,
  scale-adaptive and stress-blended eddy simulation; §I) and run a
  lattice-Boltzmann wall-modelled LES with the CLES viscosity above at
  $Re_H=7.68\times10^5$ ($H$ the body height): on the fine grid ($4.03\times10^7$
  cells) the wall-law case separates massively on the slant, on the coarse
  one ($1.36\times10^7$) it stays attached. Drag coefficients (near-field):
  wall law 0.2347 (fine) and 0.2742 (coarse), no-slip on slant and base
  0.2553 and 0.2548, against 0.279 measured by Meile et al. at the same
  $Re_H$ and the body-fitted results of Guilmineau et al. listed in their
  Table III (SST 0.2999, EARSM 0.2603, DES 0.3156, IDDES 0.3452) (§IV,
  Table III; DES details on the
  [DES page](/methods/detached-eddy-simulation.md)).
- **Supersonic base flow and channel flow.** SA-DDES of the Herrin–Dutton
  base flow ($M_\infty=2.46$) and SST-IDDES of channels at $M_b=0.15$ and 1.5
  with low-dissipation schemes (Carlsson et al. 2023, §4.3–§4.4; on the
  DES page).
- **Lattice Boltzmann solvers.** Mozaffari et al. (2024) present SST-based
  IDDES and CES in the lattice Boltzmann code
  [ProLB](/software/prolb.md), on immersed-boundary Cartesian grids with an
  algebraic equilibrium wall model, as "an alternative for the wall-modeled
  LES in the LBM framework" that behaves as wall-modelled LES only where
  the flow separates (§3.2, lines 413–418). On the Ahmed body the
  equilibrium wall model, which has no pressure-gradient term, suppresses
  the slant separation for both hybrids at $25^\circ$ and $35^\circ$, and a
  zero-velocity wall condition at $y^+\gg1$ restores it; IDDES with that
  condition is said to recover the wall-modelled LES solution of Cai et
  al. at lower cost, with no cost figure (§3.3, lines 510–515; see
  [Ahmed body](/benchmarks/ahmed-body.md) and
  [equilibrium wall model](/methods/equilibrium-wall-model.md)).
- **Transonic buffet.** SST-PANS with a dynamic resolution parameter
  predicts the OAT15A shock buffet on grids where SST URANS converges to a
  steady state, at about 3% more cost per time step; the authors argue that
  PANS works on RANS-like grids while DES-family methods in LES mode bring
  back LES grid and time-step requirements
  ([Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md), §1, §4.5–4.6;
  see [PANS](/methods/partially-averaged-navier-stokes.md)).
- **Aircraft wakes.** The sequential coupling above gives, on the NASA CRM,
  vortex lifespans between 4 and 5 descent times for non-zero atmospheric
  turbulence, in agreement with the Crow–Bate and Sarpkaya models for weak
  and medium turbulence, and a secondary wake much more turbulent and a
  plume about three times less diluted than an analytic Lamb–Oseen
  initialization with uncorrelated noise (Bouhafid et al. 2024, §4.3,
  Figs. 18, 23).
- **Turbomachinery design.** Liu et al. (2024) list DES, scale-adaptive
  simulation and related hybrids as too expensive for routine
  turbomachinery design, and pursue a transition-coupled Reynolds-stress
  RANS instead ([Liu et al. (2024)](/sources/liu-2024.md), Introduction).
  Constant et al. (2024) name the transposition of their immersed-boundary
  RANS method to hybrid RANS/LES, which their solver already runs in DDES
  and zonal DES form, as future work
  ([Constant et al. (2024)](/sources/constant-2024.md), §7; HAL author
  manuscript).
- **Planetary-entry capsule wakes.** Placco et al. (2023) recall that DES
  studies of capsule wakes showed the importance of the turbulence model and
  the limits of RANS in separated flow, but were "restricted to the
  near-body region of the wake due to some shortcomings of the hybrid
  solution approach", with disagreements in the backshell area attributed to
  the model's prediction of transition after shoulder separation; they use
  [implicit LES](/definitions/implicit-les.md) instead (§1, §2).
- **Dynamic stall.** Baldan & Guardone (2025) compare a wall-resolved LES of
  a NACA 0012 pitching sinusoidally between $-5^\circ$ and $25^\circ$
  ($Re_c=1.35\times10^5$, reduced frequency 0.1, span $1.2c$, WALE) with
  their earlier two-dimensional URANS and three-dimensional stress-blended
  eddy simulation (SBES), both on SST coupled to an intermittency transport
  equation ([Baldan & Guardone (2025)](/sources/baldan-2025.md), §2.2,
  Fig. 9; arXiv v2). The three agree within 0.1 in $C_L$ in attached flow,
  all place peak lift at $22^\circ$ against $24^\circ$ in the experiment,
  diverge somewhat in the early stalled downstroke ($24^\circ$–$18^\circ$)
  and reconverge later, with a $C_L$ offset of 0.2 from the experiment
  persisting. The authors infer that the experiment–simulation differences
  are "not primarily due to turbulence models, as commonly reported" but
  to wind-tunnel effects or surface roughness (§3); they compute one cycle,
  without phase averaging (§2.2); see [model-form uncertainty](/definitions/model-form-uncertainty.md)
  and [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md). They cite
  the DES best practice of Shur et al. that the span must be at least one
  chord to reproduce the dynamic-stall vortex (Introduction), and find the
  same requirement for their LES in the downstroke (§2.1).
- **Reynolds-stress host.** IDDES built on the SSG/LRR-$\omega$
  [Reynolds-stress model](/methods/reynolds-stress-model.md) shortens the
  separated shear layer and advances its Kelvin–Helmholtz instability
  against SST-IDDES on the tandem cylinders ($Re_D=1.6\times10^5$) and the
  transonic buffet of a hammerhead launch vehicle ($M=0.81$), with a primary
  shedding frequency of 176 Hz against 172 Hz (SST-IDDES) and 179–180 Hz
  measured (Wang et al. 2021, §3.2–§3.3, Table 1; see
  [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md) and the
  [DES page](/methods/detached-eddy-simulation.md)).
- **Turbine tip-leakage vortex.** An SST-based DES with $F_2$ shielding
  (ANSYS CFX) on one passage of a transonic high-pressure turbine cascade
  with a tip gap of $0.07c$ resolves the wandering and breakdown of the tip
  leakage vortex that the authors say URANS erases (Yang & Ma 2022, §3–§4;
  see [turbine cascades](/benchmarks/turbine-cascade.md)). They argue that
  mesh adequacy of a DES-type method "cannot be conducted by just comparing
  flow parameters among different mesh amounts", and instead show, on one
  grid of about 13 million cells, that the central/upwind blending factor of
  the convective flux is near zero (LES mode) in the vortex and wake and
  that velocity spectra follow a $-5/3$ range (§3.1, Figs. 4–5).
- **Supersonic combustion.** The SA/Yoshizawa wall-distance hybrid above,
  with WENO-5 fluxes, carries flamelet/progress-variable combustion in the
  DLR strut scramjet and a cavity-stabilized combustor at Mach 2.52 (Tang et
  al. 2022, §3; see
  [flamelet tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)).
- **Lattice Boltzmann zonal DES.** ZDES mode 2 (2020) in a lattice
  Boltzmann solver shields a flat-plate boundary layer exactly like RANS
  on a grid with $\Delta x\approx0.01\delta$, where DDES suffers severe
  modelled-stress depletion, and reproduces a finite-volume zonal DES of a
  backward-facing step and the attached layers of a three-element high-lift
  airfoil (Husson et al. 2024, §4; details on the
  [DES page](/methods/detached-eddy-simulation.md)).
- **Centrifugal pump.** SA-based DES and DDES of a stalled centrifugal
  impeller, compared with a same-grid LES, show no universal winner: DDES
  closer in vortex patterns, DES in RMS fluctuations and leading-edge
  pressure (Pan & Zhang 2023, §IV–§V; details on the DES page).
- **Dynamic-stall onset.** Delayed DES with four RANS and transition
  closures reproduces the stages of dynamic-stall onset seen in a
  wall-resolved LES of a pitching NACA 0012 at $Re=2\times10^5$, with
  slightly earlier stall and lower peak lift (Batther & Lee 2022, §4; see
  [dynamic stall](/definitions/dynamic-stall.md)). Batther & Lee use a span
  of $0.1c$, citing Visbal & Garmann's finding that spans of 10% to 120% of
  the chord do not change the overall features of this ramp-up case
  (§2.1), whereas Baldan & Guardone find a span above one chord necessary
  in the stalled downstroke of a sinusoidal cycle (above); Batther & Lee's
  case is a constant-rate ramp-up to stall onset.
- **Transitional compressor cascade.** Transitional DDES of the V103
  cascade at $Re=138\,500$ (Möller et al. 2024, §III; see
  [compressor cascades](/benchmarks/compressor-cascade.md) and the
  [DES page](/methods/detached-eddy-simulation.md)).
- **Three-element high-lift airfoil, three approaches.** Wu et al. (2023)
  compare Smagorinsky LES ($C_s=0.1$), SST-IDDES and SATES on the
  [30P30N airfoil](/benchmarks/30p30n-high-lift-airfoil.md)
  ($Re=1.71\times10^6$, $M=0.17$, $\alpha=5.5^\circ$) in the structured
  finite-difference code PHengLEI with a fourth-order
  [weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md)
  (§2–§3). On the 27-million-cell grid with linear weights the lift is 2.82
  (SATES), 2.64 (LES) and 2.27 (IDDES) against the experimental mean 2.83,
  errors of $-0.4\%$, $-6.7\%$ and $-19.8\%$ (Table 2). SATES and LES
  develop the slat shear-layer instability faster than IDDES, SATES places
  the reattachment inside the slat cove closest to the PIV, IDDES separates
  early on the flap and carries large eddy viscosity in the attached layers
  and the slat cove, and the resolved energy is highest for LES, then
  SATES, then IDDES; the authors conclude that SATES makes "a faster
  'transition' from RANS to LES than IDDES" and gives "more accurate
  wall-modeled behaviors" than LES (§3.4, §4, Figs. 17–25). With SATES the
  lift stays within 3% of 2.83 on 7.2, 19 and 27 million cells (0.7%,
  $-2.8\%$, $-0.4\%$), and replacing the linear weights by WENO-Z-type
  nonlinear weights or the scheme by a second-order blended scheme lowers
  it by 6.7% and 11.0% (§3.1–§3.3, Table 2; see
  [numerical dissipation](/properties/numerical-dissipation.md)).
- **Stall of a three-element airfoil and a supercritical cylinder.** Wu et
  al. (2024) compare SATES-SM, SATES-σ and SST-IDDES on the MD-30P30N at
  $Re_C=9\times10^6$, $M=0.2$, $\alpha=8$–$24^\circ$, where SATES-σ keeps the total
  lift error "always less than 6.5%, even at post-stall conditions", and on a
  cylinder at $Re_D=3\times10^6$, where SATES-SM predicts a subcritical
  topology ($C_D=1.39$), SATES-σ a supercritical one ($C_D=0.55$) and IDDES
  $C_D=0.62$ (§3.2–§3.3, Table 3; details on the
  [SATES page](/methods/self-adaptive-turbulence-eddy-simulation.md)).
- **High-lift aircraft vortex system.** SA-IDDES of the NASA CRM high-lift
  configuration resolves vortex structures that SA-RANS does not and gives
  $C_D=0.1843$ against 0.1868 measured (SA-RANS 0.1867) on one
  276-million-cell grid (Li et al. 2024b, §III.D; on the [DES page](/methods/detached-eddy-simulation.md)
  and [NASA CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md)).
- **Compressor tip-leakage flow.** Zhang et al. (2024) choose SA-DDES for the
  tip flow of a compressor tandem cascade because RANS has "inherent defects
  in predicting the strong anisotropic and unsteady characteristics", its
  models being "based on the isotropic hypothesis" (as cited from Tucker)
  ([Zhang et al. (2024)](/sources/zhang-2024.md), §1,
  §2.3; on the [DES page](/methods/detached-eddy-simulation.md) and
  [compressor cascades](/benchmarks/compressor-cascade.md)).
- **Supersonic combustors.** In passing, Wang & Xu (2024) list LES and
  hybrid LES/RANS studies of the Burrows–Kurkov hydrogen combustor as the
  motivation of their DNS of a reacting supersonic boundary layer
  ([Wang & Xu (2024)](/sources/wang-2024-h.md), §1).
- **Dynamic Reynolds-stress IDDES.** On the periodic hill and the
  [hammerhead launch-vehicle buffet](/benchmarks/hammerhead-launch-vehicle-buffet.md),
  the dynamic RSM-IDDES of Li et al. (2022) keeps the mean results of
  RSM-IDDES and improves resolved stresses and the high-frequency pressure
  fluctuations, its $C_p$-RMS at the experimental maximum being 0.0554
  against 0.0719 (RSM-IDDES), 0.0897 (SST-IDDES) and 0.0454 measured (§III
  B–C, Fig. 18; details on the [DES page](/methods/detached-eddy-simulation.md)).
- **Drag crisis of a circular cylinder.** The SRH model above, on
  unstructured meshes of 7.65–16.64 million cells with $y^+<1$, about five
  times fewer than the reference wall-resolved LES (38.4–89.4 million),
  gives $C_D=0.743$, 0.456, 0.252 and 0.276 at $Re_D=2.5$, 3.8, 5.3 and
  $7.2\times10^5$ on its representative grids (0.292 on the finer grid at
  $5.3\times10^5$) against 0.833, 0.481, 0.296 and
  0.213 from the reference LES, where URANS with the same host gives 0.436,
  0.354, 0.204 and 0.156; Strouhal numbers are 0.24/0.28/0.35/0.43 against
  0.25/0.23/0.38/0.45 (Mays et al. 2023, §3.2, Tables 4–5). Force
  fluctuations are damped by the near-wall URANS layer ($C_{L,\mathrm{rms}}$
  0.238–0.339 against 0.486 at $Re_D=2.5\times10^5$). On the coarsest grid
  WALE LES gives $C_D=1.247$ where SRH gives 0.743; SRH on that grid costs
  about 39% of WALE on the finest grid and 51% of WALE on the intermediate one
  (4695 against 12 150 and 9270 CPU hours; §3.1, Tables 2–3). The authors
  claim "near-LES quality results" on meshes five times coarser than the
  reference LES, which they argue "most likely could have achieved similar
  quantitative results" on a smaller mesh, since it deliberately resolved the
  far wake (§3.2.2, §4). See
  [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md) and
  [laminar separation bubble](/definitions/laminar-separation-bubble.md).
- **High-lift aircraft, wall-modelled LES against hybrids.** In the Fourth
  High-Lift Prediction Workshop the scale-resolving submissions, both
  wall-modelled LES and hybrid RANS/LES, underpredict the outboard flap
  suction peak relative to steady RANS at $21.47^\circ$, which explains the
  excessive nose-up pitching moment of all wall-modelled LES above
  $17^\circ$; the cause is unclear (Kiris et al. 2023, §VI 1e, Fig. 37). The
  authors recommend unsteady surface-pressure measurements, because
  wall-modelled LES gives reasonably accurate second-order surface-pressure
  correlations, an advantage over hybrid RANS/LES they cite (§VI 5). See
  [NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md) and
  [wall-modelled LES](/methods/wall-modelled-les.md).
- **High-speed fin.** An SST-DDES in ANSYS Fluent carries the flow side of a
  coupled aerothermoelastic analysis of a deployable fin at Mach 3–6, with no
  assessment of the hybrid behaviour (Thawait et al. 2023, §II B, §VI;
  details on the [DES page](/methods/detached-eddy-simulation.md)).
- **Concentrated vortex flows, surveyed.** Luckring & Rizzi (2024) report
  from the studies they review that on the F-15E at $65^\circ$ angle of
  attack ($M=0.3$, $Re_c=13.6\times10^6$) URANS shows no significant
  unsteadiness and virtually no vorticity over the wing while hybrid
  RANS/LES resolves it, so that "the hybrid RANS/LES formulation appears to
  be necessary for simulating flows with significant unsteady separated
  flow" (Forsythe et al., §2.4.1.4); that the most promising vortex-breakdown
  predictions of the AVT-080 70° delta wing came from hybrid RANS/LES, such
  as Morton's SA-based DES with adaptive refinement (§3.1.2.1, §4.1.2);
  that on blunt-leading-edge delta and diamond wings hybrids "appear to have
  done better than RANS methods" (§3.1.1.2); that on the AVT-316 triple
  delta wing hybrid RANS/LES was more reliable than URANS (§3.2.3.5); and
  that in CAWAPI-3 the one-standard-deviation pressure bands of the hybrid
  solutions bracket the F-16XL flight data (§3.2.3.3). They ask that the
  RANS/LES switch of hybrids be assessed against the scale of the secondary
  vortex (§2.4.2). Details on
  [delta-wing vortex flow](/benchmarks/delta-wing-vortex-flow.md) and
  [mesh adaptation](/methods/mesh-adaptation.md).

## Qualifications

- Haering et al.'s statement that explicit forcing is the only remedy for
  MSD is hedged in the source ("It appears that …", §II A) and rests on the
  cited forcing studies; no proof is given.
- Delassaux et al. recall from the DrivAer estate study of Ashton et al.
  that hybrid RANS/LES predicted drag and lift better than RANS, and state
  that hybrid RANS/LES is required for the estate wake and loads (§1); their
  own drag is better with RANS, which they attribute to error cancellation
  (§6), without discussing the difference from that study. The
  cost ratio of 18 is a wall-clock ratio: in core-hours (384 cores for
  2 hours against 1152 cores for 36 hours) it is 54 *(compiler check, not
  in the sources)*.
- Haering et al. (2022, §V B) cite successful simulations of the periodic
  hill at about one million cells with second-order delayed DES, PANS and
  PITM; see [periodic hill](/benchmarks/periodic-hill.md).
  Prieto Saavedra et al. (2024) list, for the hill at $Re_b=37\,000$, PITM
  hybrid results of Chaouat & Schiestel with reattachment at 4.30, 4.26,
  3.54 and 3.68 hill heights and a DLUM result of Mokhtarpoor et al. at
  3.8, beside LES and implicit-LES values between 3.2 and 3.8
  ([Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md),
  Table 3).
- Mozaffari et al. (2024) conclude that their averaged solutions "are
  largely consistent with the reference data, even for states where the
  flow is not in equilibrium and under large adverse pressure gradients"
  (Conclusions, lines 544–546), while §3.3 calls the slant attachment with
  the wall model "nonphysical" (line 502) and the $25^\circ$ no-slip IDDES "a
  wrong representation of the flow structures in the wake" (line 526). That
  $25^\circ$ IDDES drag (0.2970) is close to the 0.2990 measured by Meile et
  al. (Table 3).
- Husson et al. (2024) call zonal DES mode 2 (2020) "the only
  fully-detailed «automatic» formulation in the open literature" that
  shields the whole attached boundary layer, on the ground that the
  shielding of ANSYS's SBES/SDES and the switch of the PowerFLOW
  lattice-Boltzmann VLES are undisclosed (§1); the claim concerns open
  documentation, not a comparison of performance.
- Bouhafid et al. (2024) state in the abstract that atmospheric turbulence
  and stratification "both accelerate the vortex decay", and in §4.3.1 that
  atmospheric turbulence intensity "does not seem to significantly impact
  the vortex pair lifespan", while the lifespan decreases with the
  normalized dissipation; the emphasis differs within the paper.
- **Where DES sits.** Sandberg & Michelassi (2022, §2.2.2.2) class DES
  as zonal, with "predetermined regions for RANS and LES"; Haering et al.
  (2022, §I) make it the prototype of a single model that switches
  internally, with a unified switch responding to model, flow and grid
  parameters, and Bose & Park (2018, §1) contrast the explicit RANS/LES
  delineation of zonal methods with DES, where it is implicit in the
  closure. The DES page holds the switch itself. The sources state their
  taxonomies without arguing for them, and the page records the
  difference without a verdict.
- **Which hybrids count.** Heinz (2020) counts wall-modelled LES as a
  hybrid group, Bose & Park (2018) exclude hybrids from wall-modelled LES,
  and Bae & Koumoutsakos (2022) count hybrid LES/RANS as a family of
  wall-modelled LES; these are different scopes of the same words.
- **Strong evaluative claims.** Heinz's statements that DES is unstable
  under grid variation and that its framework is "too narrow" (§4.4), and
  that "RANS equations can generate resolved motions if $L_+\le1$" (§4.3,
  offered while §4.1 grants that an "exact mathematical proof … is
  currently missing"), are made in a review that runs no simulations
  (§5); the CES derivation assumes no dependence on the
  material derivatives of $k$ and $\varepsilon$ and spatially constant
  relative variations of both (§4.2). Heinz's claim that PANS and PITM need
  a "much finer grid" than CES for the same resolution (§4.4) compares PANS
  with CES; Petrocchi & Barakos's statement that PANS works on RANS-like
  grids compares it with DES in LES mode.
- Heinz prints the Kolmogorov-constant mapping
  $C_+=(3C_K/2)^{3/2}/\pi$ ($C_K$ the Kolmogorov constant) with $C_K=(1.3,1.43,1.5)$ giving
  $C_+=(0.876,1.0,1.074)$ (§2.3, App. C); the formula gives 0.867 for
  $C_K=1.3$ *(compiler check, not in the sources)*. Its Table 5 error of
  5.3% for a reattachment at 1.157 against 1.10 evaluates to 5.2%
  *(compiler check, not in the sources)*.
- Wu et al. (2023) write that "$\beta$ and $n$ are the model constants" of
  $F_r$ while Eq. 5 and Table 1 use $\beta^*$ (here $\beta_F$); their Fig. 1
  writes the integrals of $F_r$ as $\int E(L)\,dL$ and Eq. 5 as
  $\int E(k)\,dk$ with length-scale limits. In §3.4 they assign grid
  resolution to group B and schemes to group C, where Table 2 labels them A
  and B, and call SATES the best "in both turbulence models" for three
  approaches. Their errors in Table 2 reproduce from the printed lifts
  against 2.83 *(compiler check, not in the sources)*; the statement that
  cases A1–A3 differ "by less than 3%" holds for each against 2.83, while
  A1 and A2 differ by 3.6% from each other *(compiler check, not in the
  sources)*. The SATES "LES mode" is the eddy viscosity $F_r\rho k/\omega$,
  linked to the Smagorinsky model only through $C_x$.
- Idelsohn et al.'s statements on RANS ("unsuitable in general for modeling
  turbulent flows") and on hybrids stand in their introduction (§1.2); the
  paper's only RANS computation is a URANS $k$-$\varepsilon$ run of a
  particle-laden channel (§3.2.2), and it runs no hybrid.
- Mays et al. (2023) set the blending weight of their hybrid upwind/central
  flux equal to the shielding function $f_s$ (§2.2), which by their Eq. 13
  vanishes at the wall; with the printed Eq. 14 this gives the bounded
  central reconstruction in the shielded RANS zone and second-order upwind
  in LES-like zones, the reverse of the stated intent *(compiler check, not
  in the sources)*. The bounded branch (Eq. 15) weights the central
  reconstruction by $\sigma=0.01$, while the text says $\sigma$ introduces
  "some upwinding". They state that the grid-A time step is "half" that of
  grid C, while Table 1 prints $\Delta t\,U_\infty/D=1.0\times10^{-3}$ and
  $7.5\times10^{-4}$; and Table 6 heads the fourth case $Re=7.8\times10^5$,
  elsewhere $7.2\times10^5$. Their reference LES has a mean lift of $-0.903$
  at $Re_D=2.5\times10^5$ against $+0.822$ and $+0.857$ from SRH (Table 4);
  the paper discusses the sign only as "a positive value for the lift
  coefficient".

# Citations

- [Haering et al. (2022)](/sources/haering-2022.md) — §I, §II A–D Eqs. 1–2, §V B.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §1, §4.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §I.
- [Goc et al. (2021)](/sources/goc-2021.md) — §1.
- [Abe (2021)](/sources/abe-2021.md) — §III, App. A Eqs. A1–A4, §IV C–D Figs. 9–11.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — p. 2.
- [Basile et al. (2023)](/sources/basile-2023.md) — §2.2, §4.2.3.
- [François et al. (2022)](/sources/francois-2022.md) — §1, §4.1, §5.3–5.4.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) — §1.
- [Mozaffari et al. (2022)](/sources/mozaffari-2022.md) — §1 Fig. 1, §3, §4–§5.
- [Pereira et al. (2021)](/sources/pereira-2021.md) — §IV.2 Table II, §V.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §1, §4.3 Fig. 4, §4.4.
- [Cai et al. (2022)](/sources/cai-2022.md) — §I, §II C 1 Eq. 27, §IV Table III (HAL v1).
- [Placco et al. (2023)](/sources/placco-2023.md) — §1, §2.
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — §1, §4.1, §6 Table 3 Fig. 13, §7, §7.6 (HAL author manuscript).
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §2.3 Eqs. 33–34, §3.2 Table 2 Fig. 11, §3.3 Table 3, Conclusions (HAL accepted manuscript).
- [Bouhafid et al. (2024)](/sources/bouhafid-2024.md) — Abstract, §1, §2.1 Fig. 1, §3.2 Figs. 4–6, §4.3 Figs. 18, 23.
- [Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md) — §1, §4.5–4.6.
- [Liu et al. (2024)](/sources/liu-2024.md) — Introduction.
- [Constant et al. (2024)](/sources/constant-2024.md) — §7 (HAL author manuscript).
- [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) — Table 3.
- [Möller et al. (2024)](/sources/moller-2024.md) — §II.D Fig. 1, §III, §III.B.2–3 (accepted manuscript).
- [Baldan & Guardone (2025)](/sources/baldan-2025.md) — Introduction, §2.1, §2.2 Fig. 9, §3 (arXiv v2).
- [Heinz (2022)](/sources/heinz-2022.md) — §1 Table 1, §2–§3 Table 2.
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §1 Fig. 1.
- [Wang et al. (2021)](/sources/wang-2021-l.md) — §1, §2.3 Eqs. 11–16, §3.2–§3.3 Table 1.
- [Yang & Ma (2022)](/sources/yang-2022-b.md) — §1, §3.1 Figs. 4–5, §3–§4.
- [Tang et al. (2022)](/sources/tang-2022.md) — §2.1 Eqs. 1–9, 14, §3.
- [Husson et al. (2024)](/sources/husson-2024.md) — §1, §2.2 Fig. 1, §4, §5.
- [Batther & Lee (2022)](/sources/batther-2022.md) — §1, §2.1, §4, §4.5.
- [Pan & Zhang (2023)](/sources/pan-2023.md) — §II.C, §IV–§V.
- [Heinz (2020)](/sources/heinz-2020.md) — §1, §2.1, §2.3–§2.4 Eqs. 13–18, §3.1–§3.4 Eqs. 21–30, §4.1–§4.4 Eqs. 38–55, §5.1–§5.4 Tables 3, 5 Figs. 6–8, 10–11, 14, §6, App. A, App. C.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §2.2.2.2.
- [Bose & Park (2018)](/sources/bose-2018.md) — §1, §2.1.
- [Zangeneh (2021)](/sources/zangeneh-2021.md) — §I, §II.A–B, §III.
- [Sugaya & Imamura (2021)](/sources/sugaya-2021.md) — §2.1, §4.5 Table 7, Fig. 19.
- [Brenner et al. (2022)](/sources/brenner-2022.md) — §1.
- [Ghidoni et al. (2022)](/sources/ghidoni-2022.md) — §1, §6.2, Table 12, §7.
- [Wu et al. (2023)](/sources/wu-2023-b.md) — §1, §2.1.1 Eqs. 4–7 Table 1 Fig. 1, §3.1–§3.4 Eq. 16 Table 2 Figs. 9–10, 17–25, §4.
- [Li et al. (2022)](/sources/li-2022-k.md) — §II B Eq. 5, §II C, §III B–C Fig. 18, §IV.
- [Mani & Dorgan (2023)](/sources/mani-2023.md) — §4.5.2.
- [Huang et al. (2022c)](/sources/huang-2022-c.md) — §I.
- [Idelsohn et al. (2024)](/sources/idelsohn-2024.md) — §1.2.
- [Mays et al. (2023)](/sources/mays-2023.md) — §1, §2.1.2 Eqs. 9–13, §2.2 Eqs. 14–15, §3.1–§3.1.1 Tables 1–3 Figs. 4–5, §3.2–§3.2.2 Tables 4–6 Figs. 9–10, 13, §4.
- [Kiris et al. (2023)](/sources/kiris-2023.md) — §II.4, §VI 1c, §VI 1e Fig. 37, §VI 5.
- [Maeyama & Kawai (2023)](/sources/maeyama-2023.md) — §1.
- [Thawait et al. (2023)](/sources/thawait-2023.md) — §I, §II B, §VI.
- [Wu et al. (2024)](/sources/wu-2024.md) — §2.2, Eqs. (8)–(11) (SATES-SM and SATES-σ); §3.2–§3.3, Table 3 (cylinder and MD-30P30N comparisons).
- [Li et al. (2024b)](/sources/li-2024-f.md) — §I (seamless and zonal hybrids); §III.D (CRM-HL with SA-IDDES).
- [Chen et al. (2024b)](/sources/chen-2024-c.md) — §4.1 (critique of hybrid RANS/LES).
- [Zhang et al. (2024)](/sources/zhang-2024.md) — §1, §2.3 (DDES chosen over RANS for tip-leakage flow).
- [Wang & Xu (2024)](/sources/wang-2024-h.md) — §1 (LES and hybrid literature of the Burrows–Kurkov combustor; passing).
- [Luckring & Rizzi (2024)](/sources/luckring-2024.md) — §2.4.1.4–§2.4.1.5 (WMLES against hybrid RANS/LES; F-15E, as cited); §2.4.2 (switch to be assessed against the secondary-vortex scale); §3.1.1.2, §3.1.2.1, §3.2.3.3, §3.2.3.5, §4.1.2 (vortex-flow evidence, as cited).
- [Alberti et al. (2025)](/sources/alberti-2025-b.md) — §1 (non-zonal hybrids, DES deficiencies); §4 ("wall-modeled ILES" behaviour on fine DG grids).
- [Guo & Wang (2025)](/sources/guo-2025.md) — §1, §2.1 (hybrid families, transition problems, three groups of DES improvements).
- [Wu et al. (2024b)](/sources/wu-2024-b.md) — §I, §III (SATES as a unified model, against Speziale's VLES).
- [Wang et al. (2024c)](/sources/wang-2024-j.md) — §III.D–F, Figs. 10–16 (grid dependence of hybrid interfaces, feasible switching region $7<y^+<15$, interface at $y^+\approx14$).
