---
type: Method
title: "Thickened flame model"
description: "The thickened flame model of LES combustion widens the flame front over the grid by scaling diffusion and reaction while keeping the flame speed; this page gives the premixed and dynamically thickened forms, the counterflow analysis showing that diffusion flames need only diffusivity scaling, the grid-correction factor, the proposed LES model, and the partially stirred reactor as a finite-rate contrast."
status: established
aliases: [TF model, TFLES, thickened-flame LES, dynamically thickened flame, DTF, DTFLES, artificially thickened flame, thickening factor, non-premixed thickened flame]
tags: [combustion, les, numerical-dissipation, thickened-flame]
timestamp: 2026-10-27T21:11:00Z
---

# Thickened flame model

The **thickened flame (TF) model** of Colin et al., which
[Cuenot et al. (2022)](/sources/cuenot-2022.md), §1 and §2.2, cite, lets a
[large-eddy simulation](/definitions/large-eddy-simulation.md) of premixed
combustion resolve a flame front that is much thinner than the grid. The
laminar flame speed scales as $\sqrt{\dot\omega_{\mathrm r}D_{\mathrm m}}$ and the
thermal thickness as $\sqrt{D_{\mathrm m}/\dot\omega_{\mathrm r}}$, with $D_{\mathrm m}$ the
molecular diffusivity and $\dot\omega_{\mathrm r}$ a reaction-rate scale
($1/\dot\omega_{\mathrm r}$ a chemical time; $D_{\mathrm m}$ as in registry §11, $\dot\omega_{\mathrm r}$ page-local).
Multiplying $D_{\mathrm m}$ and dividing $\dot\omega_{\mathrm r}$ by the same
**thickening factor** $F$ (registry §11; not the SST blending
functions $F_1$, $F_2$) keeps the flame speed and thickens the front by
$F$, enough to place several grid points across it. Because
the thickened front responds less to the turbulent eddies, a subgrid
efficiency function accounts for the unresolved wrinkling of the filtered
front. The model is combined with direct chemistry, tabulated flamelets
or equilibrium chemistry, and is used for thermoacoustics,
ignition and extinction, and pollutants (works cited by Cuenot et al.
2022, §1); the authors call it "totally different from pdf-based or
viscosity-based (ILES) methods". The pre-tabulated alternative is
[flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md).

The bundle's sources hold two developments: the **dynamically thickened**
form used in a wall-resolved LES of a swirl combustor
([Agostinelli et al. (2021)](/sources/agostinelli-2021.md)), and the
analysis of what thickening means for **non-premixed** flames, where the
premixed transformation does not apply (Cuenot et al. 2022).

## Dynamically thickened flame and the efficiency function

Cuenot et al. (2022, §1) cite the dynamically thickened flame
(DTF) of Légier et al., which uses a flame sensor that confines the thickening to
the reaction zone, so that mixing ahead of the flame is not altered; the
earlier TF applications to non-premixed injection that the authors cite
all concern partially premixed flames. Agostinelli et al. (2021), §2, use
this dynamic formulation ("DTFLES") in the compressible LES solver AVBP,
coupled to the power-law efficiency function of Charlette et al. "with
the standard coefficient" $\beta_{\mathrm{Ch}}=0.5$ (page-local) for the
flame–turbulence interaction, with a 20-species analytically reduced
methane–air chemistry (166 reactions, 9 species in quasi-steady state),
the [sigma SGS model](/methods/sigma-model.md), the third-order TTGC scheme
and a 20.3-million-tetrahedron mesh of 300 µm cells in the flame zone,
wall-resolved ($y^+\approx1$ at the centerbody tip, about 3 elsewhere).
Their subject is the thermal wall boundary condition of the PRECCINSTA
swirl combustor (equivalence ratio 0.8, 10 kW): with a tuned thermal resistance per
surface the LES predicts a self-excited limit cycle at 224 Hz with about
800 Pa against an experimentally stable flame, and with conjugate heat
transfer it predicts a stable flame with correct length and angle
(§3.1–3.3). The combustion model is held fixed in all their runs; the
paper does not vary the thickening or the efficiency coefficient.

## Non-premixed flames: the counterflow analysis

Cuenot et al. (2022, §2) analyse the steady strained counterflow
diffusion flame, a planar stagnation flow of strain rate
$a_{\mathrm{cf}}=\lvert u_{\mathrm O}-u_{\mathrm F}\rvert/L_{\mathrm{inj}}$ between
oxidizer and fuel injectors a distance $L_{\mathrm{inj}}$ apart, with one
diffusivity $D_{\mathrm m}$ for all species and temperature ($a_{\mathrm{cf}}$, $D_{\mathrm m}$, $\eta_Z$, $\zeta_Z$ as in registry §11; the other symbols page-local).
The mixture fraction (1 in fuel, 0 in oxidizer) is
$$Z(x)=\tfrac12\big(1-\operatorname{erf}\eta_Z(x)\big),\qquad \eta_Z=\frac{\zeta_Z}{\sqrt{2D_{\mathrm m}/a_{\mathrm{cf}}}},\qquad \zeta_Z=\int_0^x\frac{\rho}{\rho_0}\,dx,$$
with $x=0$ at the stagnation point and $\rho_0$ the density there
(Eqs. 2–3, taken from the authors' earlier work, their ref. [45]). The stoichiometric scalar
dissipation rate is $\chi_{Z,\mathrm{st}}=C_{\mathrm{st}}^2a_{\mathrm{cf}}/\pi$ with
$\chi_Z=2D_{\mathrm m}(\partial_xZ)^2$ and
$C_{\mathrm{st}}=\exp(-\eta_{Z,\mathrm{st}}^2)\rho_{\mathrm{st}}/\rho_0$. In
mixture-fraction space every species or temperature $\phi_k$ obeys
$-\chi_Z\,\partial^2\phi_k/\partial Z^2=\dot\omega_{\phi_k}$ (Eq. 4), a
solution insensitive to the diffusion coefficients. Integrating it across
the flame at high Damköhler number and mapping back to physical space with
$(\partial_xZ)_{\mathrm{st}}=C_{\mathrm{st}}\sqrt{a_{\mathrm{cf}}/(2\pi D_{\mathrm m})}$ gives the
consumption speed and thermal thickness (§2.1–2.2, Eqs. 5–11)
$$\dot\Omega_{\phi_k}=-\frac{1}{C_{\mathrm{st}}}\sqrt{\frac{2a_{\mathrm{cf}}D_{\mathrm m}}{\pi}}\left(\frac{\phi_{k,+\infty}-\phi_{k,\mathrm{st}}}{1-Z_{\mathrm{st}}}-\frac{\phi_{k,\mathrm{st}}-\phi_{k,-\infty}}{Z_{\mathrm{st}}}\right),\qquad l_{\mathrm F}=\frac{1}{C_{\mathrm{st}}}\sqrt{\frac{2\pi D_{\mathrm m}}{a_{\mathrm{cf}}}},$$
with subscripts $\pm\infty$ the two stream ends; the total heat release
rate $\dot Q_T$ (page-local) follows with $\phi_k=T$ (Eq. 10).

**The thickening rule.** The consumption speed scales as $\sqrt{a_{\mathrm{cf}}D_{\mathrm m}}$ and
the thickness as $\sqrt{D_{\mathrm m}/a_{\mathrm{cf}}}$, independently of chemistry: in the
high-Damköhler regime "modifying the reaction rate has no effect". The
premixed transformation (multiply $D_{\mathrm m}$, divide the reaction rate) therefore
"can not be applied to diffusion flames"; preserving the consumption speed
while thickening requires multiplying $D_{\mathrm m}$ and dividing the strain rate by
the same factor. With $a_{\mathrm{cf}}$ given by the resolved flow in an LES, only $D_{\mathrm m}$
can be acted upon (§2.2, abstract). A diffusion flame has no intrinsic
thickness: grid filtering lowers the resolved strain rate and numerical
diffusion adds to the physical one, so the flame thickens by itself on an
LES grid and, the authors conclude, "does not need any explicit artificial
thickening" for stability (§2.2, §7). They state that applying the
premixed model directly to non-premixed flames "may lead to a significant
modification of the turbulent flame consumption speed and finally
incorrect flame shape and behavior" (§1).

## Grid tests and the correction factor

The tests are one-dimensional steady laminar counterflow flames in
CANTERA with first-order upwind discretization, on uniform grids of
decreasing resolution ratio $RR=l_{\mathrm F}/h$ ($h$ the grid step); no
turbulent flame is computed (§3–5):

| Case | Chemistry | Conditions | Grids |
|---|---|---|---|
| methane–air (§3–4) | two-step BFER* (checked against GRI 3.0) | $a_{\mathrm{cf}}=100$ s⁻¹, $l_{\mathrm F}\approx4$ mm, $\dot Q_T=323$ kW | M1000 to M10 points, $RR=200$ to 2 |
| methane–oxygen at 54 bar (§5) | analytically reduced, 14 transported and 4 quasi-steady species, 136 reactions | $a_{\mathrm{cf}}=810$ s⁻¹, $l_{\mathrm F}=300$ µm, $\dot Q_T=2020$ kW | M1500 to M30 points, $RR=45$ to 0.9 |

Every grid gives a stable converged solution, even with one point in the
reaction zone. The total heat release rate rises as the grid coarsens,
already for $RR\le20$, which the authors interpret as numerical
over-diffusion consistent with $\dot Q_T\propto\sqrt{D_{\mathrm m}}$ (Fig. 5); they
state that the upwind scheme's dissipation error has the form
$\sin(k_wh)/(k_wh)$, $k_w$ the wavenumber (§4; see
[numerical dissipation](/properties/numerical-dissipation.md)). An
effective diffusivity $D_{\mathrm m}^*$ (page-local) is defined from the coarse-grid
heat release,
$$F=\frac{D_{\mathrm m}^*}{D_{\mathrm m}}=\left(\frac{\dot Q_{T,\mathrm{coarse}}}{\dot Q_{T,\mathrm{ref}}}\right)^2$$
(Eq. 14), with values 1.113, 1.27, 1.505 and 2.575 at $RR=20$, 10, 6 and 2
for the two-step case (Table 2) and from 1.01 at $RR=30$ to 1.46 at
$RR=0.9$ for the reduced chemistry, slightly above the two-step values at
equal $RR$ (Table 3). Multiplying all diffusivities by $F$ on
the fine grid reproduces the coarse solutions "exactly" (Fig. 6); dividing
them by $F$ on the coarse grid recovers the reference
consumption within 3% for two-step chemistry, even at $RR=2$ (Fig. 7), and
within 2% for the reduced chemistry except on the one grid with no point
near stoichiometry (Fig. 9). Two points in the reaction zone suffice for
the consumption rate if one lies near stoichiometry; about five are needed
for the inner structure: at $RR=6$ the heat-release profile keeps its
endothermic–exothermic double structure and intermediate species are
captured, at $RR=0.9$ it degenerates to a single peak and H, H$_2$,
HO$_2$, OH and O peaks are misplaced or mis-scaled, OH remaining
reasonable (§5, Figs. 10–11). The correction does not change the
Damköhler number, so the flamelet regime is preserved (§5).

## Proposed LES model

For LES of non-premixed combustion Cuenot et al. (2022, §6) propose to
divide all diffusion coefficients by
$$F_{\mathrm{LES}}=F_{\mathrm{num}}\,F_{\mathrm{sgs}},\qquad F_{\mathrm{num}}=\frac{C_{\mathrm{st}}^2a_{\mathrm{cf}}^{\mathrm{LES}}/\pi}{\chi^{\mathrm{LES}}_{Z,\mathrm{st}}}$$
(Eq. 15; $F_{\mathrm{num}}$, $F_{\mathrm{sgs}}$ as in registry §11), estimated from the resolved strain rate
$a_{\mathrm{cf}}^{\mathrm{LES}}$ and the resolved stoichiometric scalar dissipation
$\chi^{\mathrm{LES}}_{Z,\mathrm{st}}$, with $F_{\mathrm{num}}=1$ on a fine
grid, and with a subgrid factor $F_{\mathrm{sgs}}\le1$ for subgrid strain
and wrinkling that is "left for future work"; $F_{\mathrm{LES}}$ may lie
above or below 1. The dominant error is set by the Kolmogorov resolution
$RR_\eta=\eta/h$: modelling error dominates when $RR_\eta\le RR$ (strong
turbulence), numerical error when $RR_\eta\ge RR$ (weak turbulence).
$F_{\mathrm{LES}}\approx1$ means numerical diffusion compensates the
subgrid effects, which the authors offer as the reading of Breda et al.,
whose LES with and without a subgrid combustion model gave similar
results. The proposal is untested: there is no turbulent flame in the
paper, and the authors restrict the analysis to high Damköhler number.

## Finite-rate alternatives and the flame resolution of LES

Thickening is one of several finite-rate closures of the filtered reaction
rate. [Fureby & Nilsson (2023)](/sources/fureby-2023.md), §3.3, list the
thickened flame model with the eddy dissipation concept, the partially
stirred reactor (PaSR), the fractal model, Eulerian stochastic fields and
the linear-eddy model, all as cited there, and choose the LES PaSR of
Sabelnikov & Fureby for an LES of a cavity-stabilized hydrogen ramjet
combustor (Eq. 4): each reaction rate is evaluated at the filtered state
and multiplied by a reacting volume fraction
$$\gamma^*_{\mathrm{PaSR}}=\frac{\tau_{\mathrm{ch}}}{\tau_{\mathrm{mix}}+\tau_{\mathrm{ch}}},\qquad \tau_{\mathrm{ch}}\approx\frac{\delta_u}{s_u},\qquad \tau_{\mathrm{mix}}\approx\sqrt{\tau_\eta\,\tau_\Delta},\qquad \tau_\Delta=\frac{\Delta}{u'_\Delta},$$
with $\delta_u$, $s_u$ the laminar flame thickness and speed, $\tau_\eta$ the
Kolmogorov time, $u'_\Delta$ a subgrid velocity scale and
$\delta_u$, $s_u$, $\gamma^*_{\mathrm{PaSR}}$, $\tau_{\mathrm{ch}}$, $\tau_{\mathrm{mix}}$,
$\tau_\Delta$, $u'_\Delta$ page-local (the source's $\gamma^*$, $\tau_c$,
$\tau_m$, $\tau_\Delta$, $v'$; $s_u$ is not the registry's Lundquist
number $S_L$). The flow closure is a one-equation
[subgrid kinetic energy model](/methods/subgrid-kinetic-energy-equation-model.md)
with gradient-diffusion scalar fluxes ($Pr_t\approx0.7$, turbulent Schmidt
number about 0.85). They prefer a finite-rate model to
[flamelet tabulation](/methods/flamelet-tabulated-chemistry.md) because the
flame is highly fragmented and the flow and chemical time scales are
similar (§3.3), and call the combination of the one-equation model and PaSR
"a reliable combination, capable of matching the more advanced and
expensive models", citing their own earlier work (§6). The thickened flame
model is not run in the paper.

A DNS study that uses no thickening states the LES flame resolution it
assumes. [Coulon et al. (2023)](/sources/coulon-2023.md), §1, motivate
their DNS of premixed methane, ammonia–hydrogen and hydrogen flames in AVBP
by the diffusive phenomena at flame-thickness scales being "still out of
reach with current mesh sizes for most Large Eddy Simulations (LES)
calculations, especially at high pressures". To define a reference flame
surface for their local stretch statistics, they filter the DNS until the
thermal thickness spans five points of a grid six times coarser than the
DNS grid, five being "a typical number of points in the thermal thickness
of a LES calculation" (§3.3, footnote 9). Their stretch results are on
[flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md).

## Qualifications

- **Printed slips in Cuenot et al. (2022).** After Eq. (15) the text says
  that with numerical diffusion $\chi^{\mathrm{LES}}_{Z,\mathrm{st}}$
  decreases "and $F_{num}<1$"; with the printed formula a smaller
  denominator gives $F_{\mathrm{num}}>1$, which is also the direction of
  the $F\ge1$ of Tables 2–3 *(compiler check, not in the
  sources)*. The numerical error is printed as
  $\varepsilon_{\mathrm{num}}=(F_{\mathrm{num}}^2-1)\dot Q_{T,\mathrm{exact}}$,
  whereas Eq. (14) gives $\dot Q_{T,\mathrm{num}}=F^{1/2}\dot Q_{T,\mathrm{exact}}$
  and hence $(F^{1/2}-1)\dot Q_{T,\mathrm{exact}}$ *(compiler check, not in
  the sources)*. The "+65%" heat release quoted for $RR=2$ (§4) compares
  with $\sqrt{2.575}-1=60.5\%$ from Table 2, and in §5 the factors 1.46 and
  1.12 of Table 3 are quoted as heat-release ratios, which by Eq. (14)
  would be $\sqrt{1.46}=1.21$ and $\sqrt{1.12}=1.06$ *(compiler checks,
  not in the sources)*. Eq. (6) replaces $\chi_{Z,\mathrm{st}}$ by $a_{\mathrm{cf}}/\pi$
  without $C_{\mathrm{st}}^2$; carried through, the prefactor of the
  consumption speed would be $C_{\mathrm{st}}\sqrt{2a_{\mathrm{cf}}D_{\mathrm m}/\pi}$ rather than
  the printed $C_{\mathrm{st}}^{-1}\sqrt{2a_{\mathrm{cf}}D_{\mathrm m}/\pi}$ *(compiler check, not in
  the sources)*; the $\sqrt{a_{\mathrm{cf}}D_{\mathrm m}}$ scaling, which the argument uses, is
  unaffected. The reference grid is called M1000 in the text and in
  Eq. (14), while Fig. 6 and Table 2 use M500 with $F=1$; the Fig. 7
  caption refers to Table 2 for meshes defined in Table 1; §5 prints that the
  fuel-side profiles are less steep because of larger diffusion
  coefficients "compared to the fuel stream", a comparison of the fuel
  stream with itself.
- **Scope.** All evidence of Cuenot et al. is steady, laminar and
  one-dimensional with a first-order upwind solver; the claims that no
  explicit thickening is needed and that solutions are robust below
  $RR=1$ are not tested in unsteady or turbulent flames, and
  $F_{\mathrm{sgs}}\le1$ assumes that subgrid effects only increase
  consumption. The consumption-speed analysis assumes a single
  diffusivity; the extension to unequal diffusivities is referred to
  earlier work.
- **Printed wording in Fureby & Nilsson (2023).** §3.3 calls the mixing
  time "the harmonic mean" of the Kolmogorov and shear times, while the
  printed formula $\sqrt{\tau_\eta\tau_\Delta}$ is their geometric mean;
  the coefficients of the one-equation model are said to be "dynamically
  evaluated from scale similarity" with no further detail.
- Agostinelli et al. and Cuenot et al. do not overlap in configuration:
  Agostinelli et al. apply the premixed dynamic form to a technically premixed swirl flame
  without studying it, and Cuenot et al. analyse non-premixed flames
  without an LES.

# Citations

- [Cuenot et al. (2022)](/sources/cuenot-2022.md) — §1 (premixed TF, efficiency function, DTF, earlier non-premixed uses); §2, Eqs. (1)–(4) (counterflow diffusion flame, mixture-fraction space); §2.1–2.2, Eqs. (5)–(11) (consumption speed, thickness, thickening rule); §3–4, Eqs. (12)–(14), Tables 1–2, Figs. 2–7 (two-step grid tests, correction factor); §5, Table 3, Figs. 9–11 (reduced chemistry at 54 bar, inner structure); §6, Eq. (15) (proposed LES model); §7.
- [Fureby & Nilsson (2023)](/sources/fureby-2023.md) — §3.2 (one-equation subgrid model, gradient-diffusion fluxes); §3.3, Eqs. (2)–(4) (finite-rate LES models listed, LES PaSR, choice against flamelets); §6 (model combination).
- [Coulon et al. (2023)](/sources/coulon-2023.md) — §1 (flame-thickness scales out of reach of LES meshes); §3.3, footnote 9 (five points per thermal thickness of an LES).
- [Agostinelli et al. (2021)](/sources/agostinelli-2021.md) — §2 (DTFLES with Charlette efficiency function, $\beta_{\mathrm{Ch}}=0.5$, ARC chemistry, mesh); §3.1–3.3 (thermoacoustic outcome under two thermal wall treatments).
