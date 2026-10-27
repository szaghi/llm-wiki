---
type: Definition
title: "Hybrid RANS/LES"
description: "Scale-resolving approaches that model all turbulence with RANS in some regions or limits and resolve part of it as in LES elsewhere; the distinction from wall-modelled LES, operating modes, continuous eddy simulation and sequential RANS-to-LES coupling, the deficiencies the sources identify, and applications."
status: established
aliases: [HRL, hybrid RANS-LES, RANS/LES hybrid, bridging model, hybrid turbulence model, scale-resolving simulation, SRS, continuous eddy simulation, CES, sequential RANS-LES, stress-blended eddy simulation, SBES]
tags: [hybrid-rans-les, rans, les, des, pans]
timestamp: 2026-10-26T20:48:00Z
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

Following the taxonomy of Larsson et al., as recalled by Haering et al.
(2022, §I):

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
author manuscript). They report, as recalled, a GPU wall-function LES of the
notchback DrivAer car whose drag error falls from 24 counts with
stress-blended eddy simulation to 10 and 2 counts with LES on 250 and 500
million cells (Menter et al., cited; §1).

Bae & Koumoutsakos (2022) draw the line differently: they list hybrid
LES/RANS, with RANS near the wall, LES outside and the interface set
implicitly by the change of model, as one of two families of wall-modelled
LES, the other being wall-flux models that replace the no-slip condition by
a modelled wall stress ([Bae & Koumoutsakos (2022)](/sources/bae-2022.md),
p. 2).

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
(ships, submarines) and Spalart's estimate, as recalled, that wall-modelled
LES of a full wing will not be possible before 2045 make RANS and hybrid
RANS/LES indispensable, with RANS kept in attached layers and a seamless
RANS/LES hybridization for separation; "it is unrealistic to discard RANS
equations if one wishes to extend high-order accurate schemes to industrial
applications" ([Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md),
§1, Fig. 1). Yang & Ma (2022) give the same motivation for a
turbomachinery passage: RANS in attached boundary layers, LES away from them,
and grid savings at high Reynolds number
([Yang & Ma (2022)](/sources/yang-2022-b.md), §1).

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
In Haering et al.'s terms, zonal DES is interfaced where the user prescribes
the zones (modes 1 and 3, as Basile et al. recall) and unified where a
shielding function detects them (mode 2) *(compiler check, not in the
sources)*; Basile et al. (2023) force RANS inside a jet nozzle
and François et al. (2022) in the core flow of a fan stage
([Basile et al. (2023)](/sources/basile-2023.md), §2.2).

**Wall-distance blending of one transported viscosity.** Tang et al. (2022)
use an interfaced two-model hybrid of the second kind in a single transport
equation: the [Spalart–Allmaras](/methods/spalart-allmaras-model.md) equation
near the wall and the one-equation Yoshizawa subgrid-energy model, rewritten
as a transport equation for the eddy viscosity by substituting
$k_{\mathrm{sgs}}=\nu_t^2/(C_\mu^2\Delta^2)$, are blended term by term into
one equation for $\tilde\nu$ with a function $F$ of the wall distance alone
($F=1$ below $y_{\mathrm{RANS}}$, $F=0$ above $y_{\mathrm{LES}}$, a
hyperbolic-tangent ramp between, constants $C_{f1}=2.0$, $C_{f2}=0.2$),
after Wang et al. and Sánchez-Rocha & Menon as recalled
([Tang et al. (2022)](/sources/tang-2022.md), §2.1, Eqs. 1–9; page-local
$F$, $y_{\mathrm{RANS}}$, $y_{\mathrm{LES}}$). The RANS layer is "quite
thin", $y_{\mathrm{RANS}}$ about 10–20% of the boundary-layer thickness; the
SA damping $f_{v1}$ is switched off in the LES region through
$\chi^3/(\chi^3+F^{20}c_{v1}^3)$, "for the sake of fast transition"; the
subgrid constants are $C_\mu=0.02075$, $C_d=1.0$, $Pr_t=0.9$, and the scalar
fluxes use the blended viscosity
$\mu_t^{\mathrm{bl}}=F\mu_t^{\mathrm{RANS}}+(1-F)\mu_t^{\mathrm{LES}}$ (Eqs. 9, 14;
page-local $\mu_t^{\mathrm{bl}}$, $\mu_t^{\mathrm{RANS}}$, $\mu_t^{\mathrm{LES}}$, a
wall-distance blend, not the constrained-LES $\nu_t^{\mathrm{hyb}}$ of registry
§11 below). The Yoshizawa part also carries terms from a spatially varying
filter width (Eq. 4). The interface height is prescribed by the wall
distance, so in Haering et al.'s terms the switch is interfaced, not
unified *(compiler check, not in the sources)*.

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
DES and zonal DES as the main hybrid strategies (§1).

### Continuous eddy simulation

The method has its own page,
[continuous eddy simulation](/methods/continuous-eddy-simulation.md). Heinz
(2022) frames the design problem of every hybrid as the "communication"
between modelled and resolved motion: the modelled viscosity must be small
enough not to extinguish resolved motion on coarse grids, yet grow for
coarser grids and higher Reynolds numbers, and "most hybrid methods" do not
address it; CES and the partially integrated transport model (PITM) are the
two the author names that do
([Heinz (2022)](/sources/heinz-2022.md), §1, Table 1). From a variational
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
page-local symbols $\psi_\beta$, $R$, $L_+$, $\Delta_{C+}$, $C_+$, $L_{\mathrm{tot}}$,
$\beta_{\mathrm{CES}}$. The source writes $\beta_{\mathrm{CES}}$ as $\beta$, the symbol of the SST
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

A family of methods builds on the decomposition of Schumann (1975), as
recalled by Haering et al. (2022, §I), in which different eddy-viscosity
models act on the mean and on the fluctuating strain; the authors say it
"may actually be considered the first hybrid method". They recall:

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

**Constrained LES near an immersed boundary.** Cai et al. (2022) use a
Reynolds-stress-constrained ("constrained LES", CLES) eddy viscosity near
the wall, after Chen et al. (2012) and Verma et al. (2013) and the authors'
own submitted work; the Chen et al. paper is the same Reynolds-stress-constrained
LES work that Haering et al. cite for RSC-SGS: both reference lists resolve
to one bibliography entry *(compiler check, not in the sources)*. In registry notation, with
$\langle\cdot\rangle$ a time average, $\tilde u_i$ the Favre-filtered velocity
and the page-local resolved Reynolds stress
$R^{\mathrm{res}}_{ij}=\langle\tilde u_i\tilde u_j\rangle-\langle\tilde u_i\rangle\langle\tilde u_j\rangle$,

$$\nu_t^{\mathrm{hyb}}=\frac{2\nu_t^{\mathrm{RANS}}\langle\tilde S_{ij}\rangle\langle\tilde S_{ij}\rangle+R^{\mathrm{res}}_{ij}\langle\tilde S_{ij}\rangle}{2\langle\tilde S_{ij}\rangle\langle\tilde S_{ij}\rangle},\qquad
\frac{\nu_t^{\mathrm{RANS}}}{\nu}=\kappa y^+\big(1-e^{-y^+/19}\big)^2,$$

([Cai et al. (2022)](/sources/cai-2022.md), §II C 1, Eq. 27; $\nu_t^{\mathrm{hyb}}$,
$\nu_t^{\mathrm{RANS}}$ page-local, the latter a mixing-length viscosity, $\kappa$
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
   derivative (§II A). As they recall it, stochastic forcing at the RANS/LES
   interface removed log-layer mismatch in channel flow but is problem
   dependent (Piomelli et al.), and the forced scale-adaptive simulation
   SAS-F still showed log-layer mismatch (Menter et al.).
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

## Evidence from applications

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
  $Re_H$ and the body-fitted results of Guilmineau et al. recalled in their
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
- **Transitional compressor cascade.** Transitional DDES of the V103
  cascade at $Re=138\,500$ (Möller et al. 2024, §III; see
  [compressor cascades](/benchmarks/compressor-cascade.md) and the
  [DES page](/methods/detached-eddy-simulation.md)).

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
- The periodic hill has been simulated successfully at about one million
  cells with second-order delayed DES, PANS and PITM, as recalled by Haering
  et al. (2022, §V B); see [periodic hill](/benchmarks/periodic-hill.md).
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
- Bouhafid et al. (2024) state in the abstract that atmospheric turbulence
  and stratification "both accelerate the vortex decay", and in §4.3.1 that
  atmospheric turbulence intensity "does not seem to significantly impact
  the vortex pair lifespan", while the lifespan decreases with the
  normalized dissipation; the emphasis differs within the paper.

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
