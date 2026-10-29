---
type: Method
title: "Thickened flame model"
description: "The thickened flame model of LES combustion widens the flame front over the grid by scaling diffusion and reaction while keeping the flame speed; this page gives the premixed and dynamically thickened forms, flame sensors and the minor-species correction in stratified flames, the counterflow analysis of diffusion flames, the grid-correction factor, and the partially stirred reactor contrast."
status: established
aliases: [TF model, TFLES, thickened-flame LES, dynamically thickened flame, DTF, DTFLES, artificially thickened flame, thickening factor, non-premixed thickened flame, flame sensor, minor-species correction, wrinkling factor]
tags: [combustion, les, numerical-dissipation, thickened-flame]
timestamp: 2026-10-29T05:13:00Z
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

The bundle's sources hold three developments: the **dynamically thickened**
form used in a wall-resolved LES of a swirl combustor
([Agostinelli et al. (2021)](/sources/agostinelli-2021.md)); the same form
in a stratified **multi-regime** flame, with a new flame sensor and a
correction of the minor species that thickening distorts
([Zhang et al. (2023)](/sources/zhang-2023-c.md)); and the
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

## Dynamic thickening of a stratified flame: sensor and minor species

Zhang et al. (2023) run the dynamically thickened flame (DTF) in an
[OpenFOAM](/software/openfoam.md) LES of the Darmstadt multi-regime burner
flame MRB26b (stratified methane–air: rich central jet at equivalence
ratio 2.6, air slot, lean slot at 0.8, air coflow), with
[flamelet-generated manifold](/methods/flamelet-tabulated-chemistry.md)
chemistry built from freely propagating premixed flamelets and a dynamic
[Smagorinsky](/methods/smagorinsky-model.md) eddy viscosity (§2–3). They
compare it with a presumed-PDF closure of the same table, run without
thickening. Page-local symbols in this section: $Y_c=Y_{\mathrm{CO_2}}+Y_{\mathrm{H_2O}}$
the (non-normalized) progress variable, $\bar D_{\mathrm{th}}$ the
unity-Lewis-number diffusivity (printed without a density factor and
called a "thermal diffusion rate"), $Sc_t=0.7$ the turbulent Schmidt
number, $\Xi_\Delta$ the subgrid wrinkling factor, $\Omega_{\mathrm{fs}}$
the flame sensor (not the registry's rotation tensor), $l^0_{\mathrm F}$ and
$s_{\mathrm L}$ the laminar thermal thickness and flame speed (registry §11
for $\Xi_\Delta$, $\Omega_{\mathrm{fs}}$ and $s_{\mathrm L}$), $\Delta$ the cube root of the cell volume. The thickened
progress-variable equation is (Eq. 9)
$$\partial_t(\bar\rho\tilde Y_c)+\nabla\cdot(\bar\rho\tilde{\boldsymbol u}\tilde Y_c)=\nabla\cdot\Big[\Big(F\,\Xi_\Delta\bar D_{\mathrm{th}}+(1-\Omega_{\mathrm{fs}})\frac{\mu_t}{Sc_t}\Big)\nabla\tilde Y_c\Big]+\frac{\Xi_\Delta}{F}\,\bar{\dot\omega}_{Y_c},$$
and the mixture fraction and the additionally transported CO and H$_2$
are thickened in the same way, because, as Zhang et al. (§3.3) cite from
Kuenne et al., thickening both the progress variable and the mixture
fraction is needed to reproduce the structure of a stratified flame. The
thickening factor follows Proch & Kempf as cited there (Eqs. 10–11),
$$F=1+\Omega_{\mathrm{fs}}(F_{\max}-1),\qquad F_{\max}=\max\Big(\frac{n\Delta}{l^0_{\mathrm F}},1\Big),\qquad n=5,$$
so that five cells span the thickened flamelet, with $l^0_{\mathrm F}(Z)$,
$s_{\mathrm L}(Z)$ and the sensor tabulated from the one-dimensional
flamelets. The wrinkling factor is the power-law form of Wang et al.
(Charlette type) with exponent $\beta_{\mathrm{Ch}}=0.5$ (Eq. 12), with the
efficiency function and the subgrid velocity $u'_\Delta$ (registry §11)
given in Appendix A. The DTF is used only with the premixed database, for
which it was derived (§3.3).

**A piecewise flame sensor** (contribution, §3.3, Eqs. 13–16, Fig. 5). On a
one-dimensional premixed flame at equivalence ratio 0.8 the authors
compare three sensors (page-local $\Omega_1$–$\Omega_3$), $\Omega_1=16\,[Y_c(1-Y_c)]^2$, the normalized
progress-variable gradient $\Omega_2$ and the normalized source term
$\Omega_3$, and state that $\Omega_1$ and $\Omega_2$ cover the reaction
region only partly while $\Omega_2$ thickens strongly near the unburned
side. Their sensor takes $\Omega_1$ up to the position $x_1$ of its
maximum, the value 1 between $x_1$ and the position $x_2$ of the maximum
of $\Omega_3$, and $\Omega_3$ beyond $x_2$, so as to cover both the
preheat zone and the heat-release zone; they call it "more stringent" than
a sensor of Popp et al. with the same aim, without a quantitative
comparison.

**Minor species under thickening** (contribution, §4.2, Eqs. 17–19,
Figs. 12–17). The DTF over-predicts CO and H$_2$ near the outer (lean
premixed) reaction zone, as Popp et al. also observed for this flame
(as cited there), and with the premixed table it over-consumes reactants
around the outer zone at $x=30$ and 60 mm, which the authors attribute to
an over-predicted turbulent flame speed (§4.1.1). Means and fluctuations
of the mixture fraction and the mean progress variable agree between DTF
and the presumed-PDF closure, but the RMS of $\tilde Y_c$ is lower with
DTF, much lower upstream, and the resolved reaction layers are less
wrinkled; the authors read this as **loss of resolved wrinkling** caused
by the thickening, and note that downstream, where the two RMS values
approach, the CO and H$_2$ deviations shrink. They state that the error is
a combined effect of thickening and wrinkling loss, where earlier work
(as cited there) addressed one or the other. Conserving species mass
between the thickened resolved front (thickness $Fl^0_{\mathrm F}$,
area $A_{\mathrm{res}}$) and the thin wrinkled laminar front (thickness
$l^0_{\mathrm F}$, area $\Xi_\Delta A_{\mathrm{res}}$), with a front-mean
mass fraction $Y^*_{\mathrm{CO}}$ that is the same in both (page-local
symbols), gives
$$Y^*_{\mathrm{CO}}\,l^0_{\mathrm F}\,\Xi_\Delta A_{\mathrm{res}}=\Big(Y^*_{\mathrm{CO}}\frac{\Xi_\Delta}{F}\Big)Fl^0_{\mathrm F}A_{\mathrm{res}}\quad\Rightarrow\quad Y^{\mathrm c}_{\mathrm{CO}}=Y_{\mathrm{CO}}\,\frac{\Xi_\Delta}{F},$$
and likewise for H$_2$ (Eqs. 18–19). The authors identify it with the
correction $Y^{\mathrm c}_{\mathrm{CO}}=Y_{\mathrm{CO}}(a\,\Xi_\Delta+b)/F$ of
Gruhlke et al., which they cite, taken with $a=1$, $b=0$ where Gruhlke
et al. obtain $a$, $b$ from a filtered wrinkled flamelet model. Applied to
the DTF results, the correction brings CO and H$_2$ in the outer premixed
zone close to the presumed-PDF closure; in the inner multi-regime
zone the gain is slight, the correction being premixed-based (Fig. 17).
The major species are not corrected; the authors cite Gruhlke et al. for
the correction affecting them little and do not test it. The DTF also
under-predicts the temperature and major-species RMS at $x=6$ mm in the
outer zone while their means are unaffected (Fig. 15).

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

## The model in engine LES

The review of combustion models for internal-combustion-engine CFD by
[Posch et al. (2025)](/sources/posch-2025.md), §4.5, states the model
after Butler & O'Rourke and Colin et al., as cited: the flame is thickened
from $\delta_u$ to $F\delta_u$ ($\delta_u$ the
laminar flame thickness, page-local, as in the Fureby & Nilsson paragraph below) and an efficiency function, which
plays the role of the wrinkling factor $\Xi_\Delta$ of the previous
sections (the source's $E$), accounts for the wrinkling by eddies smaller
than $F\delta_u$. The Favre-filtered species equation becomes
(Eq. 43; $\tilde Y_k$ the Favre-filtered mass fraction, $D_k$ the molecular
diffusivity of species $k$, $\bar{\dot\omega}_k$ its filtered rate,
page-local)
$$\frac{\partial\bar\rho\tilde Y_k}{\partial t}+\frac{\partial}{\partial x_i}\big(\bar\rho\tilde u_i\tilde Y_k\big)=\frac{\partial}{\partial x_i}\Big(\bar\rho\,\Xi_\Delta FD_k\frac{\partial\tilde Y_k}{\partial x_i}\Big)+\frac{\Xi_\Delta}{F}\bar{\dot\omega}_k-\frac{\partial}{\partial x_i}\Big[\bar\rho\big(\widetilde{u_iY_k}-\tilde u_i\tilde Y_k\big)\Big],$$
the same form as Zhang et al.'s progress-variable equation above. The
filtered rate comes from the Arrhenius laws "as in DNS", which the authors
call a major advantage, since ignition and flame–wall interaction then
need no submodel. The dynamic form of Légier et al. uses the sensor
$$\Omega_{\mathrm{fs}}=\tilde Y_{\mathrm F}^{\nu_{\mathrm F}}\tilde Y_{\mathrm O}^{\nu_{\mathrm O}}\exp\!\Big(-\Gamma_{\mathrm a}\frac{T_{\mathrm a}}{\tilde T}\Big),\qquad F=1+(F_{\max}-1)\tanh\!\Big(b_{\mathrm{tf}}\frac{\Omega_{\mathrm{fs}}}{\Omega_{\mathrm{fs},\max}}\Big)$$
(Eqs. 44–45; fuel and oxidizer mass fractions with their reaction orders,
$T_{\mathrm a}$ the activation temperature, $\Gamma_{\mathrm a}<1$ a factor
that lowers it artificially, $b_{\mathrm{tf}}$ the transition parameter and
$\Omega_{\mathrm{fs},\max}$ the maximum of the sensor, analytic for a
stoichiometric premixed flame; all page-local, the source's $\Gamma$,
$\xi$, $\Omega_{TF}$, $\Omega_{max}$); its non-premixed application is
DTFLES. On coarser grids, where $F$ and the efficiency both grow, the
diffusion number can exceed the Courant number and restrict the time step,
as the authors cite (§4.5). They cite the non-premixed TFM of Cuenot et
al. as tested only on laminar steady strained flames (§4.5), which is the
scope recorded in the sections above.

The review's assessment of the model (§5.1.4, Table 6): because the
formulation assumes no flamelets, it "can be considered as a
regime-independent combustion model for LES"; the original form with
global $F$ and static efficiency, calibrated against experiments, is
limited to low-dynamics flows, and the dynamic form avoids altering mixing
and diffusion away from the front; for highly stretched flames the burning
velocity of the thickened flame is not conserved, and the stretch-aware
variants with different thickening factors for mass and thermal diffusion
and modified source terms are "still not widely applied" in engine
simulation. Among the engine applications of Table 6, Granet et al.
simulated 75 cycles (50 unstable, 25 stable) of a premixed propane
research engine with the efficiency set to 2.0, reporting thickening
factors below 8 for the unstable and close to 50 for the stable operating
condition; other entries use the Charlette efficiency function, a dynamic
exponent, adaptive mesh refinement, FGM chemistry, a stratified dynamic
TFM with a fifth-order polynomial laminar flame speed and a wall treatment
with $F$ and the efficiency set to 1 at walls (§5.1.4, Table 6, as
cited). A thermodiffusive extension of the efficiency function derived from
two-dimensional laminar simulations (Schuh et al.) is cited for hydrogen
(§6.2.1).

## Finite-rate alternatives and the flame resolution of LES

Thickening is one of several finite-rate closures of the filtered reaction
rate. [Fureby & Nilsson (2023)](/sources/fureby-2023.md), §3.3, list the
thickened flame model with the eddy dissipation concept, the partially
stirred reactor (PaSR), the fractal model, Eulerian stochastic fields and
the linear-eddy model, all as cited there, and choose the LES PaSR of
Sabelnikov & Fureby for an LES of a cavity-stabilized hydrogen ramjet
combustor (Eq. 4): each reaction rate is evaluated at the filtered state
and multiplied by a reacting volume fraction
$$\gamma^*_{\mathrm{PaSR}}=\frac{\tau_{\mathrm{ch}}}{\tau_{\mathrm{mix}}+\tau_{\mathrm{ch}}},\qquad \tau_{\mathrm{ch}}\approx\frac{\delta_u}{s_{\mathrm L}},\qquad \tau_{\mathrm{mix}}\approx\sqrt{\tau_\eta\,\tau_\Delta},\qquad \tau_\Delta=\frac{\Delta}{u'_\Delta},$$
with $\delta_u$, $s_{\mathrm L}$ the laminar flame thickness and speed,
$\tau_\eta$ the Kolmogorov time and $u'_\Delta$ a subgrid velocity scale;
$\gamma^*_{\mathrm{PaSR}}$, $\tau_{\mathrm{ch}}$, $\tau_{\mathrm{mix}}$,
$u'_\Delta$ and $s_{\mathrm L}$ as in registry §11, $\delta_u$ and
$\tau_\Delta$ page-local (the source's $\gamma^*$, $\tau_c$, $\tau_m$,
$\tau_\Delta$, $v'$, $s_u$; $s_{\mathrm L}$ is not the registry's Lundquist
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

**The partially stirred reactor in RANS.** Posch et al. (2025), §4.2,
state the RANS form of the same reactor model: the cell is split into
reacting fine structures and non-reacting surroundings, mixed and then
reacted in sequence, with the rate
$\gamma^*_{\mathrm{PaSR}}\,\bar\rho\,(Y^*_k-Y^0_k)/\tau^*$ (Eq. 28; $Y^*_k$,
$Y^0_k$ the fine-structure and surrounding compositions and $\tau^*$ the
residence time in the fine structures, page-local), the reacting fraction
$\gamma^*_{\mathrm{PaSR}}=\tau_{\mathrm{ch}}/(\tau_{\mathrm{ch}}+\tau_{\mathrm{mix}})$
(Eq. 29, the form of Fureby & Nilsson's), the chemical time taken as the
slowest, $\tau_{\mathrm{ch}}=\max\big(Y^*_k/\lvert\mathrm dY^*_k/\mathrm dt\rvert\big)$
(Eq. 30), and the mixing time $\tau_{\mathrm{mix}}=C_{\mathrm{mix}}k/\varepsilon$
(Eq. 31; $C_{\mathrm{mix}}$ page-local) with $C_{\mathrm{mix}}$ between 0.001
and 0.3; the engine applications they review use 0.01–0.1, 0.005 and 0.1
(§5.1.1, §5.2.1, Table 8). For LES they cite a phenomenological mixing
time built from the subgrid dissipation rate and the fractal dimension of
the turbulent field, where Fureby & Nilsson write
$\tau_{\mathrm{mix}}\approx\sqrt{\tau_\eta\tau_\Delta}$. Posch et al. also
state the eddy break-up rate $C_{\mathrm{EBU}}\bar\rho(\varepsilon/k)\tilde c(1-\tilde c)$
(Eq. 27; $\tilde c$ the Favre progress variable, $C_{\mathrm{EBU}}$
page-local), valid for high Reynolds and Damköhler numbers, which
overestimates the rate where $\varepsilon/k$ is large and predicts
non-physical burning near walls (§4.2).

**Where conditional closures place the model.** The review of
[conditional source-term estimation](/methods/conditional-source-term-estimation.md)
by [Salehi et al. (2024)](/sources/salehi-2024.md), §1, lists the
"artificially thickened flamelet model" it cites among the
topology-based approaches of the laminar-flamelet family, with the
flame-surface-density and G-equation models (the same family holds the
steady and unsteady flamelet models coupled through a presumed PDF),
beside algebraic (eddy break-up), reactor-type (eddy dissipation
concept, partially stirred reactor), conditional-moment and
transported-PDF closures. It names the thickened flamelet model as an
exception among closures first developed in RANS: it was "originally
proposed for LES", as CSE was. Its motivation for a closure of the
filtered rate is a resolution argument: in premixed combustion
"it is common for the thickness of the flame to be thinner than the
Kolmogorov length", and it is "very unlikely for the flame ever to be so
thick as to be well-resolved on an LES mesh"; even a non-premixed flame
resolved by a very fine LES mesh would, at an extinction and reignition
event, produce a premixed front that the mesh "would likely not" resolve
(§1). The review does not discuss thickening further.

**Thickening with a high-order discontinuous Galerkin solver.** In their
review of high-order discontinuous schemes,
[Lv & Ekaterinaris (2023)](/sources/lv-2023.md), §6.3, Fig. 14, show a
discontinuous Galerkin LES of the Volvo bluff-body premixed flame
(propane/air at equivalence ratio 0.65 and 288 K, bulk velocity 17.3 m/s,
equilateral-triangle V-gutter of side $L=0.04$ m; taken from the first
author's earlier work) with a five-species two-step mechanism and the
thickened flame model of Colin et al. that they cite, on 10,000 hexahedra
with polynomial degree $N=3$ (64 degrees of freedom per element). They
report that "the reaction zone is captured by only one or two elements
thanks to the high-order representation", against "more than ten cells"
usually needed by second-order schemes, and mean streamwise velocities at
$x/L=0.375$, 0.95, 1.53 and 3.75 that "compare well" with the
experiment. The thickening factor and the efficiency function used are
not printed; the comparison with second-order schemes is stated, not run
in the paper. See the [discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md) for the element discretization.

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
- **Zhang et al. (2023).** The constants $C_k$ and $b$ of the efficiency
  function (Eqs. A.1–A.4) are given no values in the paper. The DTF is
  run only with the premixed table: Table 1 lists four cases, the FP,
  CF-Diff and CF-PaPre databases with the presumed PDF and the FP
  database with the DTF. The correction factor is
  derived for the front-mean $Y^*_{\mathrm{CO}}$ (Eq. 18) and written for the
  local $Y_{\mathrm{CO}}$ (Eq. 19); the paper does not say whether it is
  applied to instantaneous fields before averaging or to the averaged
  fields. The over-consumption attributed to the turbulent flame speed is
  not tested separately; the authors mention a dynamic wrinkling exponent,
  which they cite, as an alternative to the fixed $\beta_{\mathrm{Ch}}=0.5$.
- **Printed count in Salehi et al. (2024).** §1 announces that the closures "can be classified into the following four categories" and then numbers five (algebraic, reactor-type, laminar flamelet, conditional moment closure, transported PDF); the five are recorded above as printed.
- **Posch et al. (2025).** §4.5 states that "the model constant $\beta$
  has to be adjusted to the numerical scheme", while no $\beta$ appears in
  the printed formulation (Eqs. 43–45). The review calls the model
  "regime-independent" for LES (§5.1.4) and in §4.5 restricts it to cases
  where emissions and strain effects are not essential, because thickened
  flames still carry considerable unresolved content. All its evidence is
  cited from the reviewed studies.
- Agostinelli et al. and Cuenot et al. do not overlap in configuration:
  Agostinelli et al. apply the premixed dynamic form to a technically premixed swirl flame
  without studying it, and Cuenot et al. analyse non-premixed flames
  without an LES.

# Citations

- [Cuenot et al. (2022)](/sources/cuenot-2022.md) — §1 (premixed TF, efficiency function, DTF, earlier non-premixed uses); §2, Eqs. (1)–(4) (counterflow diffusion flame, mixture-fraction space); §2.1–2.2, Eqs. (5)–(11) (consumption speed, thickness, thickening rule); §3–4, Eqs. (12)–(14), Tables 1–2, Figs. 2–7 (two-step grid tests, correction factor); §5, Table 3, Figs. 9–11 (reduced chemistry at 54 bar, inner structure); §6, Eq. (15) (proposed LES model); §7.
- [Fureby & Nilsson (2023)](/sources/fureby-2023.md) — §3.2 (one-equation subgrid model, gradient-diffusion fluxes); §3.3, Eqs. (2)–(4) (finite-rate LES models listed, LES PaSR, choice against flamelets); §6 (model combination).
- [Coulon et al. (2023)](/sources/coulon-2023.md) — §1 (flame-thickness scales out of reach of LES meshes); §3.3, footnote 9 (five points per thermal thickness of an LES).
- [Zhang et al. (2023)](/sources/zhang-2023-c.md) — §2–3.4, Table 1 (MRB26b, LES-FGM in OpenFOAM, cases); §3.3, Eqs. (9)–(16), Fig. 5, App. A (thickened equations, thickening and wrinkling factors, piecewise flame sensor); §4.1.1, Fig. 6 (outer-zone over-consumption); §4.2.1, Figs. 12–15 (minor-species over-prediction, wrinkling loss); §4.2.2, Eqs. (17)–(19), Figs. 16–17 (minor-species correction, Gruhlke et al. with $a=1$, $b=0$).
- [Agostinelli et al. (2021)](/sources/agostinelli-2021.md) — §2 (DTFLES with Charlette efficiency function, $\beta_{\mathrm{Ch}}=0.5$, ARC chemistry, mesh); §3.1–3.3 (thermoacoustic outcome under two thermal wall treatments).
- [Lv & Ekaterinaris (2023)](/sources/lv-2023.md) — §6.3, Fig. 14 (DG LES with $N=3$ of the Volvo bluff-body flame with the thickened flame model; one or two elements across the reaction zone).
- [Salehi et al. (2024)](/sources/salehi-2024.md) — §1 (closure families, thickened flamelet model among topology-based approaches originally proposed for LES; flame resolution on LES meshes).
- [Posch et al. (2025)](/sources/posch-2025.md) — §4.2, Eqs. (27)–(31) (eddy break-up and partially stirred reactor in RANS); §4.5, Eqs. (43)–(45) (thickened species equation, Légier sensor, time-step restriction); §5.1.1, §5.2.1, Table 8 ($C_{\mathrm{mix}}$ values); §5.1.4, Table 6 (engine applications, regime independence, stretch); §6.2.1 (thermodiffusive efficiency function; review).
