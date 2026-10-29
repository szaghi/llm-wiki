---
type: Definition
title: "Shock sensors and troubled-cell indicators"
description: "A shock sensor or troubled-cell indicator is the switch that decides where a scheme adds shock-capturing dissipation or changes its discretization; this page defines the pressure, dilatation–vorticity, modal-decay, density-gradient and TENO-type indicators of the sources, and what each flags wrongly in turbulence."
status: established
aliases: [shock sensor, shock indicator, troubled-cell indicator, troubled-cell detector, discontinuity indicator, Ducros sensor, Jameson pressure sensor, Persson–Peraire indicator, KXRCF indicator, TVB minmod indicator, TENO troubled-cell indicator, filtered shock indicator, extremum-property sensor, EP sensor, Ren discontinuity indicator]
tags: [shock-capturing, numerical-dissipation, compressible, dg, implicit-les, boundary-layer]
timestamp: 2026-10-29T10:03:00Z
---

# Shock sensors and troubled-cell indicators

A **shock sensor** (in DG language a **troubled-cell indicator**) is a
pointwise or element-wise function of the discrete solution that marks
where a discontinuity is present, so that the scheme can act there and
only there: switch on an [artificial viscosity](/methods/artificial-viscosity-shock-capturing.md),
replace a DG element by [finite-volume subcells](/methods/subcell-finite-volume-shock-capturing.md),
apply a limiter, or move from a central or linear scheme to a
[WENO or TENO](/methods/weno-scheme.md) reconstruction. In scale-resolving
simulation of compressible turbulence the sensor decides how much
shock-capturing [numerical dissipation](/properties/numerical-dissipation.md)
reaches the resolved turbulence: a sensor that fires on vortical or
under-resolved turbulent structures turns a low-dissipation scheme into a
dissipative one there, a sensor that misses a shock lets the scheme
oscillate. The sources differ on which quantity separates shocks from
turbulence.

Symbols: $\Psi_i$ the Jameson pressure sensor and $\Phi_i$ the Ducros
factor of registry §11; $s_e$ the Persson–Peraire indicator of an element
and $s_0$ its threshold (as on the subcell page);
$\mathrm{IS}_k$ the Jiang–Shu-type smoothness indicator of stencil or
polynomial $k$ (registry §11). Also registry §11, shared with the
[WENO](/methods/weno-scheme.md) page: $\gamma^{\mathrm T}_k$ the
scale-separated smoothness measure of TENO and
$\chi^{\mathrm T}_k=\gamma^{\mathrm T}_k/\sum_l\gamma^{\mathrm T}_l$ its
normalized form (the sources' $\gamma_k$, $\chi_k$, marked because
$\gamma$ is the ratio of specific heats and $\chi$ the Spalart–Allmaras
ratio), $C_T$ the cut-off threshold. Page-local: $q$ an exponent, $\epsilon$ a small
regularizer; $U_\infty$ and $\delta_0$ the free-stream velocity and inflow
boundary-layer thickness.

## Pressure-jump sensors

**Jameson–Schmidt–Turkel sensor.** The normalized second difference of
pressure,
$$\Psi_i=\frac{\big|\sum_k(p_i-p_k)\big|}{\sum_k(p_i+p_k)}$$
over the neighbours $k$ of node $i$, switches the second-difference
dissipation of JST-type schemes; in the unstructured LD2C scheme its cap
makes the scheme first-order upwind at shocks
([Carlsson et al. 2023](/sources/carlsson-2023.md), §2.2.3, Eqs. 12–13; see
[low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md)).
OpenCFD-SCU sums a one-dimensional form,
$|{-p_{i-1}}+2p_i-p_{i+1}|/(p_{i-1}+2p_i+p_{i+1})$, over the three grid
directions and selects by two thresholds (0.02 and 0.1) a linear
seventh-order upwind, a seventh-order WENO or a fifth-order WENO flux
([Dang et al. 2022](/sources/dang-2022.md), §2.2.3, Eqs. 41–43; see
[WENO](/methods/weno-scheme.md)). In the Mach 6 swept-ramp DNS of
[Zhang et al. (2022c)](/sources/zhang-2022-g.md), §II A, the same code
runs a two-member hybrid instead, a sixth-order monotonicity-preserving
optimized scheme (OMP6) where the pressure gradient is low and a
seventh-order WENO where it is high: "the pressure gradient is used as the
shock recognizer"; neither the sensor formula nor its threshold is printed.
Two later DNS with the code family return to the three-member hybrid:
[Zhang et al. (2024b)](/sources/zhang-2024-b.md), §2.1, in OpenCFD-SCU for
Mach 6 compression ramps at three wall temperatures, and
[Tang et al. (2024)](/sources/tang-2024.md), §2.1, in the CPU parent code
OpenCFD-SC for a Mach 5, 30° ramp. Both describe a modified
Jameson–Schmidt–Turkel pressure-gradient sensor with two thresholds that
selects the seventh-order linear upwind scheme in smooth regions, the
seventh-order WENO in non-smooth and the fifth-order WENO in "extremely
non-smooth" ones, and print neither the formula nor the thresholds
(Zhang et al. refer to Dang et al. 2022 for them). Zhang et al. state that
the linear seventh-order scheme and the seventh-order WENO each "lack
robustness" in the reattachment region of their interaction and cannot
keep it stable, while the fifth-order WENO alone is "significantly more
dissipative"; the three-way switch is their answer (stated from their
runs, no comparison shown).

**The same sensor in a DG element.** [Gao et al. (2022)](/sources/gao-2022.md),
§3.2, Eqs. (12)–(13), adapt it to the DGSEM: at each node, with
$p_{\min}$ and $p_{\max}$ the smallest and largest neighbouring nodal
pressures,
$$\Psi_{ijk}=\frac{|p_{\min}-2p_{ijk}+p_{\max}|}{|p_{\min}+2p_{ijk}+p_{\max}|},$$
averaged over the element with the volumes of the $(N+1)^3$ finite-volume
subcells as weights; an element above the threshold (value not printed)
becomes finite volume. The JST-type indicator is also one of the a priori
indicators of the FLEXI switching scheme of
[Krais et al. (2021)](/sources/krais-2021.md), §4.3, §7.2.

**Flux switch in a detonation DNS.** In the code FK3 of
[Iwata et al. (2023)](/sources/iwata-2023.md), §II B, a pressure sensor
(Quirk and Kim et al. cited) selects the convective flux of a fifth-order
WENO finite-volume scheme: HLLC away from shocks, for its lower numerical
diffusion, and Lax–Friedrichs around them, for robustness; the formula and
threshold are not printed. The run is a detonation propagating into
isotropic turbulence.

**Gradient sensor plus a bound sensor in a detonation LES.** The
unstructured finite-volume LES of a rotating detonation rocket engine of
[Vignat et al. (2024)](/sources/vignat-2024.md), §3.5, runs two sensors
that drop the reconstruction to first order: one built from pressure and
density gradients, for detonations, shocks and flames, with thresholds
set by a sensitivity study "for minimum activation with stability"
(values not printed), and one that fires where a mass fraction leaves
$[0,1]$ or the temperature falls below 260 K. Away from both the
reconstruction is fourth order on uniform and third order on non-uniform
meshes.

**Smooth pressure-ratio switch of a central/WENO hybrid.** In the
compressible LES code with curvilinear immersed boundaries of
[Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md), §2.2,
Eqs. (13)–(16), the interface flux blends a fourth-order skew-symmetric
central flux and a third-order WENO flux,
$\hat F_{i+1/2}=(1-\sigma_b)F^{\mathrm{cen}}_{i+1/2}+\sigma_bF^{\mathrm{WENO}}_{i+1/2}$
($\sigma_b$ the upwind fraction, registry §11; the source writes the
central fraction $1-\sigma_b$), with the smooth tanh switch of Xiaoshuai &
Yuxin as cited,
$$\sigma_b=\frac12-\frac12\,\frac{\tanh\!\big(3(r_{i+1/2}-r_{\mathrm{th}})/\max(r_{\mathrm{th}},|r_{i+1/2}-r_{\mathrm{th}}|)\big)}{\tanh 3},\qquad r_i=\frac{|2\Delta p_{i+1/2}\Delta p_{i-1/2}|+\epsilon}{(\Delta p_{i+1/2})^2+(\Delta p_{i-1/2})^2+\epsilon},$$
$r_{i+1/2}=\min(r_i,r_{i+1})$, $\Delta p_{i+1/2}=p_{i+1}-p_i$,
$\epsilon<10^{-10}$ (page-local $r_i$ and threshold $r_{\mathrm{th}}$, the
source's $r_d$). Where adjacent pressure differences are equal $r_i=1$,
and the flux is central if $r_{\mathrm{th}}\le\tfrac12$; where one of them
vanishes $r_i\to0$ and $\sigma_b=1$, the WENO flux, for any threshold; the
ratio never exceeds one, since $2|ab|\le a^2+b^2$ *(compiler check, not in
the sources)*. The threshold
$r_{\mathrm{th}}$ is neither defined nor given a value in the paper. The
same ratio, applied to undivided differences of the solution, is the
discontinuity measure of Ren et al. below.

**Pressure ratio of a Riemann solver.** In a real-gas hybrid,
[Xu et al. (2026)](/sources/xu-2026.md), Eq. (18), flag a compressive jump
when the interface pressure ratio given by the primitive-variable Riemann
solver exceeds 0.05 with a compressive wave speed; flagged cells take the
conservative WENO update (see
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).

## Dilatation–vorticity sensors (Ducros type)

**The Ducros factor.** The ratio of squared dilatation to squared
dilatation plus squared vorticity,
$$\Phi_i=\frac{(\nabla\cdot\boldsymbol u)^2}{(\nabla\cdot\boldsymbol u)^2+|\nabla\times\boldsymbol u|^2+\epsilon},$$
is near 0 where vorticity dominates (turbulence away from shocks) and near
1 at inviscid shocks (Carlsson et al. 2023, Eq. 14; Gao et al. 2022,
Eqs. 14–15, with the element value again a volume-weighted mean). Its
uses in the sources:

- as the switch between energy-preserving central schemes and WENO in
  [STREAmS](/software/streams.md) ([Cogo et al. 2022](/sources/cogo-2022.md), §2);
- as the homotopy parameter that blends an eighth-order kinetic-energy-
  and entropy-preserving central scheme with a third-order upwind flux in
  SPADE, and as a multiplier of the Persson–Peraire-driven artificial
  diffusivity in the modal DG code CODA
  ([Chapelier et al. 2024](/sources/chapelier-2024.md), §III.B.a–b, h);
- as the switch of a KGP/HLLC hybrid for real-gas flow, where it is
  "mostly activated by the oscillations" of the central scheme rather than
  by a physical jump ([Bernades et al. 2023](/sources/bernades-2023.md),
  §4.1.1);
- multiplied with the pressure sensor, $\Psi_i\Phi_i$, in LD2C, because
  $\Phi_i$ alone "cannot separate shocks from small dilatations" and fires
  wherever vorticity is negligible; the authors state that the product
  distinguishes shocks from compressible turbulence (Carlsson et al. 2023,
  §2.2.3, Eqs. 14–15);
- in the modified Jameson dissipation of the EDGE solver used for implicit
  LES of supersonic twin jets, where the second-difference coefficient is
  $1.5\,\Phi$ times a pressure-jump ratio and the fourth-difference
  coefficient carries the factor
  $\tfrac12+\tfrac12\min(\max\Phi,\max\Theta)$, with
  $\Theta=|\nabla\times\boldsymbol u|^2/((\nabla\cdot\boldsymbol u)^2+|\nabla\times\boldsymbol u|^2)$
  the vortical complement (page-local)
  ([Ahn et al. 2023](/sources/ahn-2023.md), §III, Eqs. 1–6; formulas on
  [artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md));
- as the switch from the adaptive-local-deconvolution reconstruction and
  flux to WENO5-JS in the compressible ALDM against which
  [Bezgin et al. (2025)](/sources/bezgin-2025.md), §1, §5, compare their
  machine-learned implicit LES; in their outlook they note that
  three-dimensional flow information enters dimension-by-dimension
  finite-volume schemes today only through such sensors (§1, §6; see
  [implicit LES](/definitions/implicit-les.md)).
- as one factor of the coefficient that scales the upwind term of the Roe
  flux in the sixth-order WCNS of PHengLEI-HyOrder: for each primitive
  variable $U$,
  $$\phi_{\mathrm R}=\phi_1+\phi_2-\phi_1\phi_2,\qquad \phi_1=\Big|\frac{U^{\mathrm R}-U^{\mathrm L}}{\min(U^{\mathrm R},U^{\mathrm L})}\Big|+\epsilon_1,\qquad \phi_2=\frac{(\nabla\cdot\boldsymbol u)^2}{(\nabla\cdot\boldsymbol u)^2+\nabla\times\boldsymbol u+\epsilon_2},$$
  a total-variation (relative-jump) indicator of the interface states
  combined with the Ducros ratio as printed, $\epsilon_1$, $\epsilon_2$
  without values (page-local $\phi_{\mathrm R}$, $\phi_1$, $\phi_2$,
  $\epsilon_1$, $\epsilon_2$); on the two-dimensional Riemann problem
  (configuration 3 of Lax & Liu) the coefficient stays close to one in most
  regions and decreases near shear layers, which the authors read as shock
  capturing kept and dissipation lowered in the shear layers
  ([Wu et al. 2026](/sources/wu-2026-b.md), §3.3, Eqs. 27–28, Fig. 4;
  scheme on [weighted compact nonlinear schemes](/methods/weighted-compact-nonlinear-scheme.md)).
  The combination $\phi_1+\phi_2-\phi_1\phi_2$ is one minus the product of
  $1-\phi_1$ and $1-\phi_2$, so it equals one when either factor does
  *(compiler check, not in the sources)*.

The same switch between an energy-preserving central flux and WENO runs
two further STREAmS DNS: [Yu et al. (2022)](/sources/yu-2022-e.md),
§2.1, switch a sixth-order kinetic-energy-preserving scheme to fifth-order
WENO near strong compressions detected by the Ducros criterion in an
oblique shock/boundary-layer interaction at $M_\infty=2.28$ (threshold not
printed), and [Yu et al. (2023)](/sources/yu-2023.md), §2, restate the
same solver set-up for the same database; [Zhang et al. (2022)](/sources/zhang-2022-b.md), §2, use a
modified Ducros sensor with threshold 0.15 between an eighth-order
energy-preserving flux and seventh-order WENO only in their $M_\infty=8$
boundary layers, and apply the energy-preserving flux throughout at
$M_\infty=0.5$ and 2, where no shocklets are expected.
[Yu et al. (2023b)](/sources/yu-2023-b.md), §II, Eq. (6), print the
modified Ducros sensor of their STREAmS DNS of Mach 5 oblique
shock/boundary-layer interactions (14°, 10° and 6° wedges),
$$s=\frac{-\nabla\cdot\boldsymbol u}{\sqrt{(\nabla\cdot\boldsymbol u)^2+|\nabla\times\boldsymbol u|^2+(U_\infty/\delta_0)^2}}$$
($s$ page-local; $\delta_0$ their inflow boundary-layer thickness,
the source's $\delta_{\mathrm{in}}$): the sixth-order
kinetic-energy-preserving scheme gives way to fifth-order WENO where
$s\ge0.1$. It is the signed, unsquared form, with Pirozzoli's
regularization written inside the root.

The Ducros sensor also switches the scheme in the in-house finite-volume
code of [Zangeneh (2021)](/sources/zangeneh-2021.md), §II.D, for
wall-modelled LES of supersonic boundary layers and a compression corner:
a skew-symmetric collocated second-order low-dissipation scheme in the
turbulent regions, a "semi-discrete, central difference scheme to capture
discontinuities" where the sensor flags (formula and threshold not
printed).

A dilatation–vorticity sensor of Fernandez et al., with time and space
relaxation factors 0.7, selects the elements of the DG/FV blend of
[Klose et al. (2025)](/sources/klose-2025.md), §2 (formula not printed).

**Regularized and signed variants.** Gao et al. (2022, §3.2) cite
Pirozzoli's choice $\epsilon=(U_\infty/\delta_0)^2$, which filters
small-amplitude dilatation outside the boundary layer, and write two
variants that flag compressions only (Eqs. 16–17, idea credited to Larsson
et al. and Lusher & Sandham):
$$\Phi^{\mathrm s}=\frac{-\nabla\cdot\boldsymbol u}{|\nabla\cdot\boldsymbol u|+|\nabla\times\boldsymbol u|+U_\infty/\delta_0},\qquad
\Phi^{\mathrm s}_{a}=\frac{-\nabla\cdot\boldsymbol u}{|\nabla\cdot\boldsymbol u|+a_\omega|\nabla\times\boldsymbol u|+U_\infty/\delta_0},$$
($\Phi^{\mathrm s}$, $\Phi^{\mathrm s}_a$, $a_\omega$ page-local; $a_\omega$
the source's case-dependent vorticity scaling $\alpha$). The positive
dilatation of an expansion fan then gives negative values, whereas the
squared form flags expansion fans as it flags weak shocks; the scaled
variant is "not easy to be generalized for different cases". Neither is
used in their final runs. The same group's later DG simulation of the
interaction over an elastic panel uses instead the "improved Ducros
indicator" of Gao et al. (2022a), with the parameter value 10.0, to
confine an adaptive filter to troubled elements, and keeps the filter
always active above $y=2\delta_r$ ([Gao et al. 2023](/sources/gao-2023.md),
§3.1.3, §5.1; the other two indicators of that paper are in the next
section).

[De Vanna et al. (2022)](/sources/devanna-2022.md), §3.1.2, Eq. (8), run a
compression-only form in the hybrid energy-preserving/WENO-Z solver URANOS
for wall-modelled LES of an oblique shock/boundary-layer interaction at
$M_\infty=2.28$:
$$\Phi^{\mathrm c}=\max\left(-\frac{\nabla\cdot\boldsymbol u}{\sqrt{(\nabla\cdot\boldsymbol u)^2+|\nabla\times\boldsymbol u|^2+\epsilon}},\,0\right),\qquad \epsilon=\Big(\frac{U_\infty}{\delta_0}\Big)^2,$$
($\Phi^{\mathrm c}$ page-local, the source's $\theta$) evaluated at cell
interfaces; above $0.1$ the cell is "shocked" and WENO-Z replaces the
energy-preserving flux in it and in its neighbours. The square root makes
it the unsquared form, and the maximum discards expansions as Gao et al.'s
signed variants do.
The same form, with threshold $0.05$ and $\delta_0$ the boundary-layer
thickness of the case, switches on the AUSM-type numerical diffusion of
the split energy-preserving finite-volume flux of the OpenFOAM-based
solver scramjetFoam, in the wall-resolved LES of supersonic film cooling
of [Wei et al. (2023)](/sources/wei-2023.md), §II C, Eq. (19); no
artificial diffusion is added to the species equations (flux on
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).

**Switching a filter instead of a flux.** In the sixth-order compact
finite-difference DNS of a Mach 2.9, 24° compression ramp of
[Kang & Lee (2024)](/sources/kang-2024.md), §II.B, "a modified version of
the Ducros-type sensor" (formula and threshold not printed) drops the
eighth-order compact low-pass filter applied at every final Runge–Kutta
stage to a second-order one at shocks, with the filter parameter raised
from 0.47 to 0.49 (the source's $\alpha_f$); a localized artificial
diffusivity acts in addition (on
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)).

[van Noordt et al. (2022)](/sources/vannoordt-2022.md), §2.3, Eq. (9), blend
a fourth-order kinetic-energy- and entropy-preserving central flux with a
third-order WENO flux, $\hat f=(1-\alpha_{\mathrm b})\hat f_{\mathrm{cent}}+\alpha_{\mathrm b}\hat f_{\mathrm{diss}}$
($\alpha_{\mathrm b}$ page-local, the source's $\alpha$, renamed because
$\alpha$ is the DG/FV blending factor of the registry), with a sensor
printed "following Ducros et al." as
$$\alpha_{\mathrm b}\big|_{\mathrm{volume}}=\frac{(\nabla\cdot\boldsymbol u)^2+|\nabla\times\boldsymbol u|^2}{(\nabla\cdot\boldsymbol u)^2+(U_\infty/\delta_0)^2},$$
whose $U_\infty/\delta_0$ term, they state, "shields the boundary layer"
from artificial dissipation near the wall; in the first three irregular
cells next to their immersed boundary $\alpha_{\mathrm b}$ is prescribed by
hand, independent of the solution. Their results are reported with
constant interior values ($\alpha_{\mathrm b}=0.0125$ in a channel,
$0.02$ in hypersonic cases) and irregular-cell triplets (§3.1–3.2); see
the qualification below.

**Modal sensor multiplied by a compression factor.**
[Tonicello et al. (2022)](/sources/tonicello-2022.md), §2.2, Eq. (2.10),
App. B, switch the bulk artificial viscosity of their spectral-difference
DNS of a compression–expansion ramp with the Persson–Peraire-type modal
sensor $s_{\mathrm{modal}}$ (truncation to degree $N-1$, characteristic
variables after Lodato; thresholds self-calibrated on a manufactured
solution) multiplied by a Ducros-type factor built from element averages
$\{\cdot\}_e$ (registry §11):
$$s_e^{\mathrm D}=s_{\mathrm{modal}}\times\frac{\big[\tfrac12\big(|\{\nabla\cdot\boldsymbol u\}_e|-\{\nabla\cdot\boldsymbol u\}_e\big)\big]^2}{\{\nabla\cdot\boldsymbol u\}_e^2+\{\omega_k\omega_k\}_e+\epsilon},$$
with $\epsilon$ "of order machine epsilon squared". The numerator is
non-zero only in compression; the authors state that the factor keeps the
viscosity off at walls and in strongly vortical regions with negligible
compression, and the mean viscosity is non-zero only near the shock
(§3.2, Fig. 12; scheme on
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)).

## Modal-decay and gradient sensors in element methods

**Persson–Peraire.** The share of the element's solution norm carried by
its highest modes,
$s_e=\log_{10}\big[(\rho-\rho_{N-1},\rho-\rho_{N-1})_e/(\rho,\rho)_e\big]$
with $\rho_{N-1}$ the truncation of the density to degree $N-1$, gates a
local modal filter in the flux-reconstruction code ATHOS, with recommended
$s_0\in[-3.7,-2.7]$ at $N=2$ and $[-5.3,-4.3]$ at $N=3$
([Wang 2024](/sources/wang-2024-b.md), §2.3, Eq. 19, Table 2b; values and
results on [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)).
The same sensor, with the calibration of Glaubitz et al., drives the
Laplacian artificial viscosity of CODA (Chapelier et al. 2024, §III.B.a;
[Schotte et al. 2026](/sources/schotte-2026.md), §2.2). FLEXI's subcell
switching in the code comparison of Chapelier et al. (§III.B.f) uses
instead the exponential decay rate of the modal coefficients of the
**pressure**. [Jiang et al. (2025)](/sources/jiang-2025.md), §3.1, flag
oscillating cells of the turbulent kinetic energy $k$ at the
under-resolved edge of a boundary layer with an element-resolution
indicator (Persson–Peraire cited) and replace their polynomial by a
Hermite-WENO reconstruction: the indicator here targets a turbulence
variable, not a shock.
[An et al. (2025)](/sources/an-2025.md), App. A, Eq. (A.1), do the same
for the Spalart–Allmaras variable in their third-order modal DG RANS
solver: the troubled-cell detector is the modal-decay ratio of the
conserved $\rho\tilde\nu$,
$$S_e=\log_{10}\frac{\langle\rho\tilde\nu^{N}_e,\rho\tilde\nu^{N-1}_e\rangle}{\langle\rho\tilde\nu^{N}_e,\rho\tilde\nu^{N}_e\rangle}$$
($S_e$ page-local; the source's $S_k$, with $\rho\tilde\nu^{N}_e$ the
modal expansion over all $M(N)$ modes of element $e$ and
$\rho\tilde\nu^{N-1}_e$ the expansion over the first $M(N-1)$ modes, $N$
the source's $p$, which it calls the discrete order;
$\langle\cdot,\cdot\rangle$ the element inner product), and a
cell is troubled above a case-dependent threshold; troubled cells take a
Hermite-WENO reconstruction extended to the SA equation, with linear
weights modified for anisotropic meshes, plus a positivity-preserving
limiter on $\tilde\nu$. The authors' reason: the weak solution of
$\tilde\nu$ has discontinuous first derivatives at the turbulent/laminar
edge, oscillating high-order solutions give negative $\tilde\nu$, and the
solver diverges (§2, App. A; background of their solver, cited). The
threshold values are not printed.

**Confining an adaptive filter.** [Gao et al. (2023)](/sources/gao-2023.md),
§3.1.3, apply the positivity-preserving, minimum-entropy adaptive modal
filter of Dzanic & Witherden only in elements that an indicator flags
(method on [explicit modal filtering](/methods/explicit-modal-filtering.md)
and [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)).
They change the indicator with the case: a Jameson indicator above 0.0008
for supersonic panel flutter, a Persson–Peraire indicator with threshold
$-4.5$ for a shock hitting a cantilever panel, and the improved Ducros
indicator for the turbulent interaction (§4.1–4.2, §5.1). They report
that the confined filter introduces "much less dissipation in smooth flow
areas, especially in those complex vortical structures", than the
unconfined one, from a qualitative Schlieren comparison (§4.2, Figs. 14,
16).

**Modal energy of $\rho p$ and a logistic blender.** In the subcell
blending of [Potluri et al. (2023)](/sources/potluri-2023.md), §3.1.1,
Eqs. (11)–(12), the indicator variable is the product $\rho p$, expanded
in Legendre modes with coefficients $m_j$. Two modal-energy ratios are
used: the Persson–Peraire form $\mathbb E_{\mathrm P}=m_N^2/\sum_{i=0}^Nm_i^2$
and the form of Hennemann et al.,
$\mathbb E_{\mathrm H}=\max\{m_N^2/\sum_{i=0}^Nm_i^2,\ m_{N-1}^2/\sum_{i=0}^{N-1}m_i^2\}$
($m_j$, $\mathbb E_{\mathrm P}$, $\mathbb E_{\mathrm H}$ page-local). The
ratio is mapped to the blending factor $\alpha$ by a logistic function of
$\mathbb E/\mathbb T(N)-1$ with sharpness $9.21024$ and threshold
$\mathbb T(N)=0.5\times10^{-1.8(N+1)^{0.25}}$, clipped to
$[\alpha_{\min},\alpha_{\max}]$ with $\alpha_{\min}=10^{-3}$, and smoothed
over neighbours. $\mathbb E_{\mathrm P}$ is used for $N\le2$ and, for
$N>2$, in supersonic cases; $\mathbb E_{\mathrm H}$ in hypersonic cases
with $N>2$. Their cases are laminar; they report a limitation: shock detectors "cannot be expected to detect the high
gradients which show-up in the initial transient of hypersonic boundary
layers", where the blending factor is non-zero at first but "diminishes
very quickly", so they impose it at the wall instead (§3.3; the wall
modification is on the subcell page).

**Three detectors compared in under-resolved compressible turbulence.**
[Bilocq et al. (2025)](/sources/bilocq-2025.md), §3.5, Eqs. (29)–(30),
use the same logistic map with the Hennemann calibration (sharpness
$9.21024$, threshold $0.5\times10^{-1.8(N+1)^{1/4}}$, cut-off
$\alpha_{\min}=0.001$) on the single-ratio modal-energy indicator of the
density, $\mathbb E_{\mathrm P}=(\rho-\rho_{N-1},\rho-\rho_{N-1})_e/(\rho,\rho)_e$
(their $\mathcal E$, Eq. 30; the Persson–Peraire ratio without the
logarithm), to switch both a Laplacian
artificial viscosity (DG-AV) and their selective entropy-stable DG (DG-ES,
which uses the entropy-stable discretization only in flagged cells). In
decaying compressible isotropic turbulence with eddy shocklets
($M_{t,0}=0.6$, $Re_{\lambda,0}=100$, $N=5$) they compare three detectors
(§4.1.5, Figs. 3–4, Table 4):

- the original Persson–Peraire calibration flags close to 100% of the
  cells and over-dissipates;
- the Hennemann calibration flags at most about 10% of the elements, and
  DG-AV and DG-ES then behave like the unstabilized DG;
- the dilatation–vorticity shock sensor of Fernandez et al., which gives a
  subcell-varying viscosity, fires in more cells than the Hennemann
  calibration because the shocklets persist, damps the dilatation
  fluctuations strongly, and fails on five of the coarse meshes on which
  the Hennemann calibration is stable.

DG-AV is strongly sensitive to the detector, DG-ES much less, and in the
worst case it matches the fully entropy-stable scheme. In the supersonic
Taylor–Green vortex ($M_0=1.25$, $Re=1600$, $N=3$) the flagged fraction
falls from about 37% at $64^3$ degrees of freedom to about 6.5% at
$128^3$ and below 1% at $512^3$ (§4.2.2, Table 6). For the strong
vortex/shock interaction the plain Hennemann sensor keeps neither DG-AV nor
DG-ES stable, and they widen it by one diffusion sweep over face
neighbours, $\alpha\leftarrow\max_{\mathcal K}(\alpha,0.5\alpha_{\mathcal K})$,
at the cost of a larger stabilized region (§4.3.2, Eq. 39). The sensor
never fires inside the vortex, so the authors attribute the vortex damping
of DG-AV to dissipation during the earlier passage through the shock
(§4.3.3). See [artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
and [entropy conservation](/properties/entropy-conservation.md).

**The smoothness indicator as a refinement indicator.**
[Ims & Wang (2023)](/sources/ims-2023.md), §3.2, Eqs. (15)–(17), reuse the
Persson–Peraire smoothness ratio, averaged over density, momentum and total
energy, over the cell and in time, as one of three indicators for
h-refinement of implicit LES with flux reconstruction. On two turbine
cascades it concentrates refinement in the boundary layers and converges
the wake statistics more slowly than the two alternatives; on the T106a
cascade it is no better than random refinement (§5.1–5.3, visual
comparisons; see [mesh adaptation](/methods/mesh-adaptation.md)).
For steady RANS and laminar flow,
[Bulgarini et al. (2025b)](/sources/bulgarini-2025-b.md), §4.2–4.3,
Eqs. (39)–(43), compare a "spectral decay" indicator (cited to Persson &
Peraire and printed as the ratio of norms
$\|(\rho\boldsymbol u)_N-(\rho\boldsymbol u)_{N-1}\|_{L^2(e)}/\|(\rho\boldsymbol u)_N\|_{L^2(e)}$,
without the logarithm and on the momentum) with a small-scale-energy
indicator and two interface non-conformity indicators for anisotropic
$h$-adaptation of their isogeometric DG: on a laminar cylinder at $Re=40$
all four give a speed-up of about 2 against a uniformly fine mesh, the
spectral-decay indicator is "the most effective overall" and the
small-scale-energy indicator over-refines the separation region (§4.3,
Figs. 9–10). Side by side: Ims & Wang (2023) find, for adaptive implicit
LES of turbine cascades, the small-scale-energy and residual indicators
converge faster than the Persson–Peraire ratio, which on the T106a is no
better than random; Bulgarini et al. (2025b) rank the spectral-decay ratio
first and the small-scale-energy indicator last for steady laminar and
RANS flow, with a normalization of the latter by the element size
(Eq. 40). The two studies differ in flow regime (unsteady implicit LES
against steady solutions), in the printed form of the indicators and in
the quantity converged.

**Density gradient.** The entropy-stable artificial viscosity of
[HORSES3D](/software/horses3d.md) is switched by an element-wise
density-gradient sensor, $\int_{\mathrm{el}}\mathcal J|\nabla_\xi\rho|^2$
([Ferrer et al. 2023](/sources/ferrer-2023.md), §4.4, Eq. 19;
[Mateo-Gabín et al. 2022](/sources/mateogabin-2022.md), §6.2–6.3,
Eqs. 127–128, where the Shu–Osher run sets the SVV exponent to zero where
the sensor exceeds 10).

**Hysteresis.** Krais et al. (2021, §4.3) switch an element to finite
volumes above an upper threshold and back below a lower one, which they
state prevents back-and-forth switching and reduces the sensitivity to the
user value (no data shown).

## Troubled-cell indicators of modal RKDG

[Huang & Fu (2024)](/sources/huang-2024.md) and
[Huang et al. (2025)](/sources/huang-2025.md) work with third-order modal
(Legendre) Runge–Kutta DG on uniform Cartesian grids ($N=2$; the sources
write $k$), inviscid Euler tests only. They recall two classical
indicators (Huang & Fu 2024, §4.1–4.2, Eqs. 27–31):

- **TVB minmod.** The cell's interface deviations from its mean are
  compared with the neighbouring mean differences through the modified
  minmod function, which returns its first argument if that is below
  $M_{\mathrm{TVB}}\Delta x^2$ ($M_{\mathrm{TVB}}$ page-local, the source's
  $M$) and the minmod otherwise; the cell is troubled if the modification
  changes anything. A larger $M_{\mathrm{TVB}}$ flags fewer cells, too large
  a value misses genuine troubled cells.
- **KXRCF** (Krivodonova et al.), the normalized jump across the inflow
  boundary $\partial I_i^-$ towards the neighbour $I_l$,
  $$I^{\mathrm{KXRCF}}_i=\frac{\big|\int_{\partial I_i^-}(u^h|_{I_i}-u^h|_{I_l})\,ds\big|}{h^{(N+1)/2}\,|\partial I_i^-|\,\big\|u^h|_{I_i}\big\|},$$
  troubled above 1 ($h$ the radius of the circumscribed circle, the norm
  the maximum over the cell).

They state that both need a critical parameter tied to the solution and
tuned case by case (§1).

**KXRCF in flux reconstruction.** Two flux-reconstruction sources change
the normalization of KXRCF:

- [Shi & Yan (2023)](/sources/shi-2023.md), §II.B.1, Eqs. (6)–(7), drop
  the factor $h^{(N+1)/2}$ "based on the non-dimensionalization analysis",
  so that the indicator measures the inflow-face jump of density as a
  fraction of the cell's own maximum, and flag a cell above $C_{\mathrm{KX}}=0.01$
  (page-local, the source's $C_k$; the original threshold is 1). On the double Mach
  reflection the sensor marks the shocks and also parts of the shear layer
  and the vortex, and density contours keep "wrinkles", which they read as
  oscillations the sensor–limiter pair does not remove (§III.B, Fig. 3).
  The sensor then drives a WENO limiter in an implicit LES of a Mach 2.9
  compression-ramp interaction (see [WENO schemes](/methods/weno-scheme.md)).
- [Liu & Yuan (2023)](/sources/liu-2023-b.md), §3.3, Eqs. (30)–(32), use
  the larger of the two interface jumps of the cell,
  $I_i=\max(|u_{i,L}-u_{i-1,R}|,|u_{i,R}-u_{i+1,L}|)$, which is
  $O(h^{N+1})$ in smooth regions and $O(1)$ at a discontinuity, and its
  normalized form $I^{\mathrm{KXRCF}}_i=I_i/(h^{(N+1)/2}\{u\}_i)$ with the cell mean
  $\{u\}_i$ ($I_i$ page-local; the source's $I^*_i$). A cell with
  $I^{\mathrm{KXRCF}}_i<c_{\mathrm{sm}}=10^{-3}$ is accepted, one with
  $I^{\mathrm{KXRCF}}_i>c_{\mathrm{dc}}=1$ is troubled ($c_{\mathrm{sm}}$,
  $c_{\mathrm{dc}}$ page-local, the source's $C_S$, $C_D$), and only the cells in
  between go to a relaxed discrete maximum principle on the cell means
  ($N=2,3$) or on subcell means ($N\ge4$), with relaxation
  $\max(10^{-4},10^{-3}\times\text{local range})$ (Eqs. 26–29); a cell whose
  density or pressure becomes non-positive, or NaN, is troubled in any
  case, and the two neighbours of a troubled cell are marked too (§3.2,
  §3.4). This is an *a posteriori* test of the unlimited candidate
  solution (the route of the subcell page), with pressure as the detection
  variable. Without the KXRCF pre-detection the shock cell of a steady
  detonation switches between the high-order and the subcell scheme every
  few steps, which they attribute to Runge-type perturbations of the
  transfer between the two representations, and with first-order subcells
  the peak-pressure history does not converge to $10^{-4}$; with it the
  time-averaged number of troubled cells per step falls from 14–85 to
  5–7 (Table 2; one-dimensional inviscid tests only).

**TENO-based troubled-cell indicator.** Huang & Fu (2024, §4.3, Eqs. 32–35)
transfer the stencil selection of TENO to the DG polynomials $p_{i-1}$,
$p_i$, $p_{i+1}$ of a cell and its two neighbours, $k\in\{i-1,i,i+1\}$:
$$\mathrm{IS}_k=\sum_{l=1}^{2}\int\Delta x^{2l-1}\Big(\frac{\partial^lp_k}{\partial x^l}\Big)^2dx,\qquad
\gamma^{\mathrm T}_k=\frac{1}{(\mathrm{IS}_k+\epsilon)^q},\qquad
\chi^{\mathrm T}_k=\frac{\gamma^{\mathrm T}_k}{\sum_{l=i-1}^{i+1}\gamma^{\mathrm T}_l},$$
and cell $i$ is troubled iff its own $\chi^{\mathrm T}_i<C_T$, with
$\epsilon=10^{-3}$, $q=6$, $C_T=10^{-4}$ for every case, without tuning.
In two dimensions the one-dimensional test is applied in $x$ and $y$ and
a cell flagged in either direction is troubled (§5.1). The idea comes from
Fu's TENO discontinuity indicator for hybrid finite differences, which
needs four candidate stencils and six points; the novelty is the compact
three-cell form. Huang et al. (2025, §3.1, §4.1, Eqs. 11–14) reuse it with
the same parameters in their TENO-THINC limiter, applied to each
characteristic variable, and in two dimensions limit a cell troubled
along $x$ only along $x$.

Reported behaviour, all on inviscid Euler problems:

- on smooth one- and two-dimensional advection the indicator never fires,
  so the limited and unlimited schemes give identical third-order errors
  (Huang & Fu 2024, §6.1, Tables 1, 3; Huang et al. 2025, §5.1, Tables 1, 3),
  whereas the TVB indicator "may activate limiters" at smooth extrema and
  is therefore used to force limiting in the accuracy test (Huang & Fu
  2024, §6.1.1);
- KXRCF misses the under-resolved high-wavenumber part of the Shu–Osher
  problem ($x\approx5.6$ to 7.2), which the TENO indicator flags, and
  marks more than 50% of the cells of the two-dimensional Riemann problem
  (configuration 3), while the TENO indicator places troubled cells "much
  more precisely" with "less noise" on the shock tubes and the double Mach
  reflection (Huang & Fu 2024, §6.2–6.6, Figs. 4–15; visual evidence only);
- in the double Mach reflection at $1200\times300$ the indicator flags 34681
  cells, 9.63% of the domain, of which the boundary-variation selector of
  the TENO-THINC limiter sends 6476 (1.8% of the domain) to the jump
  reconstruction (Huang et al. 2025, §5.5, Fig. 6).

**Troubled-cell detection for DG limiting in multi-material flow.** In
their review of diffuse-interface methods,
[Maltsev et al. (2022)](/sources/maltsev-2022.md), §III D, §IV C, cite
these ways of localizing DG limiting: the TVB troubled-cell detection of Qiu & Shu
followed by a WENO or Hermite-WENO reconstruction of the higher moments, the
monotonicity-preserving troubled-zone indicator of Balsara et al., a
troubled-cell detector with minmod limiting of the Legendre slopes in the
local DG solver of Gryngarten & Menon, a minmod detector with a WENO limiter
in the DG solver of Saleem et al., and a TVB minmod detector selecting the
cells whose second moments are WENO-reconstructed in the reconstructed DG
of Pandare et al. (the
[subcell finite-volume](/methods/subcell-finite-volume-shock-capturing.md)
a posteriori route is on its page). They also note that a contact
discontinuity such as a material interface, unlike a shock, has parallel
characteristics that do not counteract numerical diffusion, so that
interface smearing is unavoidable without corrections to the governing
equations (§IV A).

**The review of Lv & Ekaterinaris.** In their review of high-order
discontinuous schemes for multiphase and multicomponent flows,
[Lv & Ekaterinaris (2023)](/sources/lv-2023.md), §4.2, list the
indicators that localize DG artificial viscosity after Persson & Peraire:
inter-element jumps, entropy residuals, intra-element pressure jumps,
pressure gradients and a neural network (all cited); the minmod limiter
of TVB Runge–Kutta DG carries its own built-in detector. They add two
cautions for LES: under-resolved turbulence can be mistaken for shocks,
so the sensor must confine the dissipation, and even with a good sensor
limiting stays "too intrusive" for high-order solutions; as an instance
of confinement they cite a limiter-assisted flux-reconstruction LES of
the NASA CRM in which "only 0.3% of elements have the limiter
activated". The a posteriori subcell correction removes the ad hoc choice
of what to do in a troubled element but keeps troubled-cell detection,
with its problem-dependent parameters (§4.2; see
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)).

## Switches inside WENO reconstructions (finite differences and volumes)

**Relative total-variation limiter.** The bandwidth-optimized WENO schemes
that [Kumar & Ghosh (2022)](/sources/kumar-2022-b.md), §2.2.1,
Eqs. (24)–(26), use for DNS of shock trains carry the limiter of Taylor et
al.: on the $r+1$ candidate stencils of $r$ points the stencil total
variations $TV_k=\sum_l|f_{i+k+l-r+1}-f_{i+k+l-r}|$ (page-local, with $f$
the split flux) give
$$R_{TV}=\frac{\max_kTV_k}{\epsilon+\min_kTV_k},$$
and when $R_{TV}$ does not exceed a threshold $P_{\mathrm{TV}}$
(page-local; the source's $\alpha^{RL}_{TV}$ or 'P', which they call "an
arbitrary constant") every smoothness indicator $\mathrm{IS}_k$ is set to
zero; otherwise the nonlinear WENO weights act. With all $\mathrm{IS}_k$
zero the weights of their Eq. (19) reduce to the optimized linear ones
*(compiler check, not in the sources)*. The threshold is the sensor's only parameter
and decides the resolution: raising it from 3 to 10 resolves more small
scales on the Shu–Osher, two-dimensional Riemann, double-Mach and
Rayleigh–Taylor tests, but the three-point scheme is unstable in the double
Mach reflection at threshold 7 and the four-point one at 5, and very large
values give Gibbs oscillations at shocks; the authors take 5 for their DNS
(§3.1, §3.2.1). Their conclusion that thresholds of 7 to 10 "may also show
better performance" than WENO-CU6 is stated, not shown (§4).

**Extremum-property sensor of a hybrid interpolation WENO.**
[Wang et al. (2024b)](/sources/wang-2024-i.md), §II.D, Eqs. (21)–(23),
decide per point whether the fifth-order interpolation-based WENO of
their HAUS-WENO scheme may use its linear weights. Write the quartic
interpolant of the five-point stencil as
$q_1(x)=\sum_{\ell=0}^4c_\ell\,\varphi_\ell(x)$,
$\varphi_\ell=((x-x_i)/h)^\ell$ (page-local $q_1$, $c_\ell$,
$\varphi_\ell$), whose derivative has the sign of
$4c_4\varphi_3+3c_3\varphi_2+2c_2\varphi_1+c_1$. On each half-interval,
$[x_{i-3/2},x_i]$ and $[x_i,x_{i+3/2}]$, the authors bound this derivative
term by term, taking for each term the larger (or smaller) of its values
at the two ends and summing; call the sums $B^{\max}_{\mathrm L}$,
$B^{\min}_{\mathrm L}$, $B^{\max}_{\mathrm R}$, $B^{\min}_{\mathrm R}$
(page-local; the source's MAX1, MIN1, MAX2, MIN2). The point is smooth if
$(B^{\max}_{\mathrm L}\pm h)(B^{\min}_{\mathrm L}\pm h)>0$ and
$(B^{\max}_{\mathrm R}\pm h)(B^{\min}_{\mathrm R}\pm h)>0$, the test that
the paper names after the extremum property of the interpolant
(§II.D); then the linear interpolation $q_1(x_{i+1/2})$ replaces
the nonlinear weights and the characteristic projection. The shift
"$\pm h$" is printed without further explanation. The idea of testing for
roots of $q_1'$, earlier needing the roots explicitly, and the sign test
on reconstruction-based unequal-sized WENO are attributed to earlier work
of the group (as cited). For the supersonic Taylor–Green vortex the
sensed variable is the density, and the authors state that the sensor
"does not contain empirical parameters" (Abstract, §I). It makes HAUS-WENO
the cheapest of the four schemes compared, 0.74 of the WENO-JS run time
as printed in their Table III (0.723 from the printed run times, see the
Source page) (scheme results on [WENO](/methods/weno-scheme.md)).

**Comfort-zone indicator of WENO-K.** In the Gauss–Kriging WENO of
[Han et al. (2022)](/sources/han-2022-c.md), §3.2.2, Table 4, every cell
starts as troubled ($\theta_{\mathrm K}=0$, plain WENO-JS) and becomes smooth when the
ratio $a_{\mathrm{cz}}=(\bar q_{i-1}-\bar q_{i+2})/(\bar q_{i+1}-\bar q_i)$ of cell
averages lies in the "comfort zone" $-6.5<a_{\mathrm{cz}}<5$, a range "determined by a
large number of tests"; there the Kriging hyper-parameter is
$\theta_{\mathrm K}=\tfrac65\big(1-\tfrac{12}{15+a_{\mathrm{cz}}}\big)$ ($a_{\mathrm{cz}}$,
$\theta_{\mathrm K}$ page-local, the source's $a$, $\theta$;
see [WENO](/methods/weno-scheme.md)).

**Central weight of CWENOZ as a reset switch.** In the ADDA algorithm of
[Tsoutsanis & Nogueira (2025)](/sources/tsoutsanis-2025.md), §4.3,
Remark 5, Fig. 3, a cell-wise energy-ratio sensor (the energy of the
reconstructed momentum removed by a weak and by a strong modal filter;
on [numerical dissipation](/properties/numerical-dissipation.md)) lowers
or raises the dissipation of an unstructured CWENOZ finite-volume implicit
LES, and the nonlinear weight $\mathsf w_1$ of the central stencil,
computed for density and pressure, acts as the discontinuity detector:
when it falls below a threshold $C$ the flux-dissipation multiplier is
reset to its full value at once. The threshold is printed as
"$C<0.999$" and the flowchart writes $\mathsf w_1\le C$; with the
non-normalized central weight $1000$ of ADDA's low-dissipation setting,
the normalized linear central weight is $1-1/1000=0.999$ *(compiler check,
not in the sources)*. The authors state that the energy-ratio sensor
responds to under-resolved turbulence and to discontinuities alike
(Remark 3), and that the density-based reset prevents very-low-dissipation
settings in cells whose stencils cross strong density gradients (§5.3,
Fig. 24). Scheme on [WENO](/methods/weno-scheme.md).

## Indicators built from TENO stencil flags (finite differences)

**Eight-point TENO-S indicator.** [Liang & Fu (2024)](/sources/liang-2024.md),
§3.1, Eqs. (31)–(34), cover the points $x_{i-3},\dots,x_{i+4}$ with six
**equal-sized** three-point stencils, compute their Jiang–Shu indicators
(the three not used by TENO given in Eq. 31), and set
$\gamma^{\mathrm T}_k=1/(\mathrm{IS}_k+\epsilon)^6$, $k=0,\dots,5$, with
$\epsilon=10^{-4}$ in one dimension and $10^{-2}$ in several (it also acts as
a cut-off of the smoothness measurement). A cell is smooth if
$\chi^{\mathrm T}_k>C_{T2}$ for every $k$, with the built-in $C_{T2}=10^{-6}$,
troubled otherwise; it is evaluated on conserved variables in physical
space (density and total energy in one dimension, density only in
several), dimension by dimension. Smooth cells take a non-dissipative
skew-symmetric flux, troubled ones an eight-point TENO flux (see
[WENO](/methods/weno-scheme.md) and
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).
Equal stencils keep the indicator cheap, and the authors state that it
separates smooth from non-smooth scales "in the wavenumber space", hence
"more universal for general conservation laws" than physical-variable
sensors such as the Ducros sensor (§3.1). In the double Mach reflection
more than 90% of the cells use the skew-symmetric flux (§4.6, no count
printed).

**Discontinuity-strength measure.** Liang & Fu (2024, §3.3.2,
Eqs. 47–49) and [Li & Fu (2024)](/sources/li-2024-c.md), §3.2.1,
Eqs. (44)–(47), grade rather than flag: a first-order measure $m\in[0,1]$
built from neighbouring undivided differences (after Ren et al.) is near 1
at a discontinuity and near 0 for high-wavenumber fluctuations, and maps
the TENO cut-off between about $10^{-7}$ (Liang & Fu; $10^{-5}$ for Li &
Fu) and $10^{-10}$; formulas on [WENO](/methods/weno-scheme.md).
[Wu et al. (2024b)](/sources/wu-2024-b.md), §II.D, Eqs. (20)–(22),
print the measure in full for their weighted compact nonlinear scheme:
$m_{\mathrm R}=1-\min(1,\eta_{i+1/2}/C_{\mathrm r})$ with
$$\eta_i=\frac{|2\Delta f_{i+1/2}\Delta f_{i-1/2}|+\epsilon}{(\Delta f_{i+1/2})^2+(\Delta f_{i-1/2})^2+\epsilon},\qquad \epsilon=\frac{0.9C_{\mathrm r}}{1-0.9C_{\mathrm r}}\,\xi^2,$$
$\eta_{i+1/2}=\min(\eta_{i-1},\eta_i,\eta_{i+1})$, $\xi=10^{-3}$ and
$C_{\mathrm r}=0.24$ for five-point interpolation (page-local
$m_{\mathrm R}$, $\eta_i$, $C_{\mathrm r}$, $\xi$; $\Delta f$ undivided
differences of the interpolated variable). It sets the TENO cut-off
$C_T=10^{-\lfloor\beta_{\mathrm A}\rfloor}$,
$\beta_{\mathrm A}=10-5(1-g)$, $g=(1-m_{\mathrm R})^4(1+4m_{\mathrm R})$,
between $10^{-5}$ at discontinuities and $10^{-10}$ in smooth regions, on
a smooth (tanh) rather than step cut-off (scheme and results on
[weighted compact nonlinear schemes](/methods/weighted-compact-nonlinear-scheme.md)).

**Pattern of TENO flags.** [Takagi et al. (2022)](/sources/takagi-2022.md),
§3.1–3.2, Eqs. (19)–(20), read the 0/1 flags that fifth-order TENO already
computes for its two biased stencils, classify each cell by which of them
is non-smooth, and declare a discontinuity in cell $i$ when a cell on its
left has a non-smooth right stencil, a cell on its right a non-smooth left
stencil (within three cells), and cell $i$ itself neither; the pattern
comes from TENO's flags on a one-cell step (Table 1). It adds no parameter
to TENO and sends the flagged cells to a THINC jump reconstruction; under-
resolved smooth fluctuations, which also turn flags off, do not show the
pattern and stay with TENO. Li & Fu (2024, §3.2.3, Eqs. 59–61) reuse the
same pattern for five- to seven-point adaptive TENO in compressible
multiphase flow.

## Schemes that replace the sensor

**Boundary-variation selection.** [Deng et al. (2022)](/sources/deng-2022.md),
§1, state that the performance of hybrid central/upwind schemes "relies on"
the shock indicator and, citing a comparison of indicators, that none is
universally best; their $P_nT_m$-BVD-AD finite-volume schemes need no
explicit sensor: a cell takes a THINC jump reconstruction instead of its
polynomial when that lowers its total boundary variation (the sum of the
face jumps), and the dissipation-adjusting stage acts only on faces where
neither neighbour has switched (§3.2, Eqs. 17–25; scheme on
[WENO](/methods/weno-scheme.md)).

**Nonlinear weights as the detector.** In the weighted compact nonlinear
scheme WCNS-T of [Ma et al. (2022)](/sources/ma-2022.md), §2.2, Eqs.
(21)–(29), the discontinuity detection is carried by the Z-type nonlinear
weights of four compact sub-interpolations, with the global indicator
$|\mathrm{IS}_0+3\mathrm{IS}_1-3\mathrm{IS}_2-\mathrm{IS}_3|$ and
third-derivative-including smoothness indicators on four-point stencils;
with idealized weights (zero on stencils that cross the jump) the
tri-diagonal interpolation system splits into two independent systems on
the two sides of a discontinuity, which the authors call the
shock-capturing mechanism, so no switch between compact and explicit
interpolation families is needed (the paper does not call this a sensor).
The scheme is on
[weighted compact nonlinear schemes](/methods/weighted-compact-nonlinear-scheme.md).

**A sensor-free artificial viscosity.** The Brescia/Bergamo DG solvers
used by [Bulgarini et al. (2025)](/sources/bulgarini-2025.md), §2, Eq. (9),
and [Bulgarini et al. (2025b)](/sources/bulgarini-2025-b.md), §3.4,
Eqs. (27)–(31), add the pressure-gradient-directed artificial viscosity of
Bassi et al. in every element "without the use of any shock sensor": its
coefficient is proportional to a jump residual, the lifted difference
between the numerical and the physical inviscid flux on the element
boundary, so it is "always and everywhere active, but introduces a
numerical viscosity only where nonphysical oscillations occur"; formulas on
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md).
Both papers are steady RANS computations (transonic RAE 2822, NACA 0012).

By contrast, the OpenFOAM implicit-LES solver of
[Cheng et al. (2023)](/sources/cheng-2023-b.md), §2.2, uses no sensor: one
bounded (TVD) reconstruction, ROUND, acts at shocks and in turbulence
(scheme on [WENO](/methods/weno-scheme.md)).

## Filtering the field before sensing

[Gao et al. (2022)](/sources/gao-2022.md), §3.2, a FLEXI implicit LES of
an oblique shock reflecting on a Mach 2 turbulent boundary layer, report
the failure of both families in that configuration:

- the Jameson indicator evaluated on the instantaneous pressure marks large
  parts of the under-resolved turbulent boundary layer as troubled (Fig. 2),
  so it "cannot be used" for this interaction unmodified;
- the Ducros indicator, because dilatation and vorticity have similar
  magnitudes in the interaction region, either detects almost no shock
  inside the boundary layer (large threshold) or marks too many cells
  (small threshold); most authors, they state, take the large threshold
  and refine the mesh (§1, §3.2, citing Fang et al., Jammalamadaka et al.;
  stated, not run).

Their remedy is to evaluate a jump-detecting indicator on a **filtered**
field from which the turbulent structures are removed while shock jumps
remain. They reject temporal filters (no real-time update; a moving
average made sharp shocks and stability hard to reconcile) and use the
Jameson indicator on the **spanwise-averaged pressure**, the mean over all
spanwise nodes, which confines the subcells to the shocks, including
inside the boundary layer, with "a negligible number" of finite-volume
subcells near the interaction (Fig. 7 against Fig. 2). The global average
needs a quasi-two-dimensional configuration (oblique reflections,
compression ramps); an element-local spanwise average serves some
three-dimensional cases; complex geometries are left open. The authors
state that the filtering applies to any jump-detecting indicator, e.g.
Persson's, and that its parallel cost fits within the 15–20% overhead of
the hybrid scheme (§3.2, §5.3.1). The resulting interaction is on
[shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

## The sensor and the subgrid model

In their review of the canonical shock–turbulence interaction,
[Cuadra et al. (2025)](/sources/cuadra-2025.md), §III A 1, state that the
overall dissipation of hybrid central/WENO (or TENO) schemes "depends
strongly on the shock sensor", which motivates refined sensors (cited),
and, §III A 3, that switching the subgrid fluxes off in the cells where
the shock-capturing scheme is active improves LES (Bermejo-Moreno et al.
2010, cited); their list of three elements for predictive LES of
supersonic shock–turbulence interaction ends with "SGS fluxes only where
the hybrid scheme is central" (§IV A 3). See [shock-generated turbulence](/results/shock-generated-turbulence.md).

## Qualifications

- **The Wu et al. (2026) sensor as printed.** In $\phi_2$ the vorticity
  enters the denominator as the vector $\nabla\times\boldsymbol u$ added to
  scalars, where the Ducros factor above uses $|\nabla\times\boldsymbol u|^2$;
  and $\phi_1$, a relative jump plus $\epsilon_1$, is not bounded by one as
  printed, so $\phi_{\mathrm R}$ can exceed one *(compiler check, not in the
  sources)*. The paper calls the coefficient $\phi$ in Eq. (27) and
  $\phi_k$, "of kth's variable", in the text.

- **What separates a shock from turbulence.** Carlsson et al. (2023) state
  that the product $\Psi_i\Phi_i$ separates shocks from compressible
  turbulence and support it with channel and base-flow runs in which the
  dissipation coefficient and face extrapolation also change (see the LD2
  page); Gao et al. (2022) state that Ducros-type sensors fail for shocks
  that penetrate a turbulent boundary layer, citing others, and test the
  Jameson indicator alone; Liang & Fu (2024) call their indicator more
  universal than the Ducros sensor without running the Ducros sensor.
  None of the three compares the sensors on one case.
- **"Parameter-free" indicators.** Huang & Fu (2024) and Huang et al.
  (2025) use one parameter set ($\epsilon=10^{-3}$, $q=6$, $C_T=10^{-4}$)
  for eight and nine Euler tests on uniform grids at $N=2$; the limiters
  they drive keep their own cut-offs and constants. Liang & Fu (2024)
  print "no case-by-case tuning" (abstract) while using
  $\epsilon=10^{-4}$ in one dimension and $10^{-2}$ in several, different
  indicator variables in one and several dimensions, and a Roe instead of
  a Rusanov splitting "to obtain a stable result" in the blast-wave case
  (§4.4). Takagi et al. (2022) call their pattern indicator parameter-free;
  it inherits TENO's $C_T$, whose value changes their blast-wave
  convergence (§4.5, Fig. 9). No source tests these indicators on a
  turbulent flow with shocks.
- **Two printed forms of the TENO indicator.** Huang & Fu (2024, Eq. 32)
  integrate each neighbour polynomial over its own cell $I_k$; Huang et al.
  (2025, Eq. 11), restating the same indicator, integrate all three over
  the target cell $I_i$. For a neighbour quadratic the first-derivative
  term differs in general between the two (the second-derivative term,
  a constant integrand, does not) *(compiler check, not in the sources)*.
- **Printed form in EDGE.** Ahn et al. (2023, Eq. 6) print the pressure
  ratio of the second-difference coefficient as
  $|\sum_kp_k-p_0|/(\sum_kp_k+p_0)$ and write the vortical factor with the
  subscript $j$ and the dilatation of node 0. For more than one neighbour
  the printed ratio is not the normalized sum of differences
  $|\sum_k(p_k-p_0)|/\sum_k(p_k+p_0)$ of the JST sensor above
  *(compiler check, not in the sources)*.
- **Indicators that miss or overreach.** Potluri et al. (2023) find that
  modal shock detectors miss the transient wall gradients of laminar
  hypersonic boundary layers (§3.3); Shi & Yan (2023) find that their
  KXRCF variant also flags shear layers and vortices (§III.B); Ims & Wang
  (2023) find the Persson–Peraire ratio biased towards boundary layers when
  it ranks cells for refinement (§5.1). The three findings come from
  different uses (blending, limiting, refinement); none of the three
  papers compares indicators on one turbulent case.
- **Printed forms in Liu & Yuan (2023) and Potluri et al. (2023).** Liu &
  Yuan (Eq. 30) write the interface jumps at time level $n$, while their
  Algorithm 1 applies the pre-detection together with the test of the
  candidate solution at $n+1$; Eq. (32) divides by the cell mean as
  printed, without an absolute value (the detection variable of all their
  tests is pressure).
  Potluri et al. (§3.1.1) print the modal expansion as $\sum_{i=0}^Nm_jP_j$,
  with mismatched indices.
- The Jameson threshold of Gao et al. (2022) is not printed, nor is
  Fernandez et al.'s sensor formula in Klose et al. (2025). Neither the
  formula nor the thresholds of the OpenCFD-SC/SCU sensor are printed by
  Zhang et al. (2024b) or Tang et al. (2024), nor the modified Ducros
  sensor of Kang & Lee (2024), nor the threshold values of Vignat et al.
  (2024); the forms above for these sources are the descriptions they
  print.
- **Printed form of van Noordt et al. (2022), Eq. (9).** As printed, the
  vorticity sits in the numerator together with the dilatation and the
  shielding term $(U_\infty/\delta_0)^2$ in the denominator. Where
  $\nabla\cdot\boldsymbol u\approx0$ the expression reduces to
  $|\nabla\times\boldsymbol u|^2/(U_\infty/\delta_0)^2$, which is not
  bounded by 1 and is not small where the vorticity is of order
  $U_\infty/\delta_0$ or larger, as in near-wall shear *(compiler check,
  not in the sources)*; the paper does not state a clipping or how the
  sensor combines with the constant values $\alpha_{\mathrm b}$ it reports.
  The form differs from the Ducros factor $\Phi_i$ above, in which the
  vorticity enters the denominator.
- **Evidence for detector sensitivity (Bilocq et al. 2025).** The
  ranking of the three detectors rests on one decaying-turbulence case at
  $N=5$, with "standard values of the parameters" that "have not been
  fine-tuned for this problem" (§4.1.5); the selective
  scheme DG-ES has no printed entropy-stability proof at the interfaces
  between flagged and unflagged cells (§3.6).
- **Printed forms in Tsoutsanis & Nogueira (2025).** Besides the threshold
  "$C<0.999$" (above), §4.3 says a cell tagged for more dissipation
  increases the central linear weight, while §4.2 and §5.1 obtain more dissipation by
  reducing the central linear weight to 2.
- Deng et al.'s (2022) statement that no indicator is universally best is
  a citation, not a comparison run in the paper; Ma et al.'s (2022)
  decoupling at discontinuities is derived under idealized weights
  (exactly zero on stencils that cross the jump, proportional to the
  linear weights otherwise), which the authors call "a theoretical
  analysis".

# Citations

- [Gao et al. (2022)](/sources/gao-2022.md) — §1; §3.2, Eqs. (12)–(17), Figs. 2, 5–7 (Jameson and Ducros indicators in DGSEM, signed variants, filtered-field indicator); §5.3.1 (cost of the filtering).
- [Liang & Fu (2024)](/sources/liang-2024.md) — §3.1, Eqs. (31)–(34), Fig. 2 (eight-point indicator); §3.2, Eq. (35); §3.3.2, Eqs. (47)–(49) (discontinuity strength); §4.4, §4.6.
- [Huang & Fu (2024)](/sources/huang-2024.md) — §1; §4.1–4.3, Eqs. (27)–(35) (TVB, KXRCF, TENO indicator); §5.1; §6.1–6.6, Tables 1–4, Figs. 4–15.
- [Huang et al. (2025)](/sources/huang-2025.md) — §3.1, §3.3, §4.1, Eqs. (11)–(14) (TENO indicator restated, characteristic and directional use); §5.1, Tables 1, 3; §5.5, Fig. 6 (troubled-cell and BVD fractions).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §3.1–3.2, Eqs. (19)–(20), Table 1 (TENO-flag pattern indicator); §4.5, Fig. 9.
- [Li & Fu (2024)](/sources/li-2024-c.md) — §3.2.1, Eqs. (44)–(47) (discontinuity strength $m$); §3.2.3, Eqs. (59)–(61) (pattern indicator for TENOA).
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §2.2.3, Eqs. (12)–(15) (Jameson sensor, Ducros factor, product).
- [Dang et al. (2022)](/sources/dang-2022.md) — §2.2.3, Eqs. (41)–(43) (modified Jameson sensor, thresholds).
- [Ahn et al. (2023)](/sources/ahn-2023.md) — §III, Eqs. (1)–(6) (Ducros-weighted Jameson dissipation in EDGE).
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §2 (Ducros-switched WENO in STREAmS).
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL hal-04582857v1: §III.B.a, b, f, h (Persson–Peraire with Ducros weighting, Ducros homotopy, pressure modal-decay indicator).
- [Bernades et al. (2023)](/sources/bernades-2023.md) — §4.1.1, Fig. 1 (Ducros sensor activated by oscillations).
- [Krais et al. (2021)](/sources/krais-2021.md) — §4.3 (indicators, hysteresis); §7.2 (JST-type indicator).
- [Klose et al. (2025)](/sources/klose-2025.md) — ASME accepted manuscript: §2 (dilatation–vorticity sensor of Fernandez et al.).
- [Wang (2024)](/sources/wang-2024-b.md) — arXiv v2: §2.3, Eq. (19), Table 2 (Persson–Peraire indicator and thresholds).
- [Schotte et al. (2026)](/sources/schotte-2026.md) — §2.2 (Persson–Peraire sensor with Glaubitz calibration).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.4, Eq. (19) (density-gradient sensor).
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §6.2–6.3, Eqs. (127)–(128) (density-gradient sensors).
- [Jiang et al. (2025)](/sources/jiang-2025.md) — §3.1 (element-resolution indicator for HWENO limiting of $k$).
- [Xu et al. (2026)](/sources/xu-2026.md) — arXiv 2508.21599v1: §3, Eq. (18) (pressure-ratio sensor).
- [Zangeneh (2021)](/sources/zangeneh-2021.md) — §II.D (Ducros-switched skew-symmetric and shock-capturing schemes).
- [Maltsev et al. (2022)](/sources/maltsev-2022.md) — §III D, §IV C–D (troubled-cell detectors of DG limiting, cited); §IV A (contact discontinuities).
- [Kumar & Ghosh (2022)](/sources/kumar-2022-b.md) — §2.2.1, Eqs. (24)–(26) (relative total-variation limiter); §3.1, §3.2.1 (threshold and stability); §4.
- [Han et al. (2022)](/sources/han-2022-c.md) — §3.2.2, Table 4 (comfort-zone indicator of WENO-K).
- [De Vanna et al. (2022)](/sources/devanna-2022.md) — §3.1.1–3.1.2, Eq. (8) (compression-only modified Ducros sensor, threshold 0.1, WENO-Z in the cell and its neighbours).
- [van Noordt et al. (2022)](/sources/vannoordt-2022.md) — §2.3, Eqs. (8)–(9) (Ducros-type blending sensor with boundary-layer shielding, prescribed irregular-cell values); §3.1–3.2 (constant dissipation factors).
- [Tonicello et al. (2022)](/sources/tonicello-2022.md) — §2.2, Eq. (2.10), App. B, Eq. (B3) (modal sensor times compression-only Ducros factor); §3.2, Fig. 12.
- [Yu et al. (2022)](/sources/yu-2022-e.md) — §2.1 (Ducros criterion switching KEP to WENO5 in STREAmS).
- [Zhang et al. (2022)](/sources/zhang-2022-b.md) — §2 (modified Ducros sensor, threshold 0.15, at $M_\infty=8$ only).
- [Deng et al. (2022)](/sources/deng-2022.md) — §1 (dependence of hybrid schemes on the indicator); §3.2, Eqs. (17)–(25) (BVD selection instead of a sensor).
- [Ma et al. (2022)](/sources/ma-2022.md) — §2.2, Eqs. (21)–(29) (nonlinear weights and decoupling of the compact system at a discontinuity).
- [Zhang et al. (2022c)](/sources/zhang-2022-g.md) — §II A (pressure-gradient recognizer of the OMP6/WENO7 hybrid in OpenCFD-SCU).
- [Gao et al. (2023)](/sources/gao-2023.md) — §3.1.3 (Jameson, Persson–Peraire and improved Ducros indicators confining the adaptive filter, values 0.0008, $-4.5$, 10.0); §4.1–4.2, Figs. 14, 16; §5.1.
- [Potluri et al. (2023)](/sources/potluri-2023.md) — §3.1.1, Eqs. (11)–(12) (modal energy of $\rho p$, threshold, logistic blender); §3.3 (detectors miss transient wall gradients).
- [Ims & Wang (2023)](/sources/ims-2023.md) — §3.2, Eqs. (15)–(17) (Persson–Peraire ratio as refinement indicator); §5.1–5.3.
- [Shi & Yan (2023)](/sources/shi-2023.md) — §II.B.1, Eqs. (6)–(7) (KXRCF without grid scaling, $C_{\mathrm{KX}}=0.01$, density); §III.B, Fig. 3 (double Mach reflection).
- [Liu & Yuan (2023)](/sources/liu-2023-b.md) — §3.2–3.5, Eqs. (26)–(32), Algorithm 1 (physical and relaxed maximum-principle detection, KXRCF pre-detection, neighbour marking); §5.5, Table 2, Figs. 6–7, 10.
- [Iwata et al. (2023)](/sources/iwata-2023.md) — §II B (pressure sensor switching HLLC and Lax–Friedrichs fluxes).
- [Yu et al. (2023)](/sources/yu-2023.md) — §2 (Ducros switch in STREAmS, same database as Yu et al. 2022).
- [Cheng et al. (2023)](/sources/cheng-2023-b.md) — §2.2 (ROUND reconstruction, no sensor; passing).
- [Zhang et al. (2024b)](/sources/zhang-2024-b.md) — §2.1 (two-threshold modified Jameson sensor selecting UDL7/WENO7/WENO5 in OpenCFD-SCU; robustness statement).
- [Tang et al. (2024)](/sources/tang-2024.md) — §2.1 (the same hybrid and sensor in OpenCFD-SC; passing).
- [Yu et al. (2023b)](/sources/yu-2023-b.md) — §II, Eq. (6) (signed modified Ducros sensor, threshold 0.1, KEP to WENO5 in STREAmS).
- [Wei et al. (2023)](/sources/wei-2023.md) — §II C, Eq. (19) (compression-only Ducros sensor, threshold 0.05, switching AUSM-type diffusion).
- [Kang & Lee (2024)](/sources/kang-2024.md) — §II.B (modified Ducros sensor switching the compact filter from eighth to second order).
- [Vignat et al. (2024)](/sources/vignat-2024.md) — §3.5 (pressure/density-gradient sensor and scalar-bound sensor, first-order reconstruction).
- [Lv & Ekaterinaris (2023)](/sources/lv-2023.md) — §4.2 (indicators for DG artificial viscosity, cautions for LES, troubled-cell detection in subcell correction; review).
- [Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md) — §2.2, Eqs. (13)–(16) (pressure-ratio indicator and tanh switch of a central/WENO hybrid; threshold not given).
- [An et al. (2025)](/sources/an-2025.md) — §2; App. A, Eqs. (A.1)–(A.2) (modal-decay detector on $\rho\tilde\nu$ driving HWENO and positivity limiting).
- [Wang et al. (2024b)](/sources/wang-2024-i.md) — Abstract, §I; §II.D, Eqs. (21)–(23) (extremum-property sensor); §III.E, Table III (cost).
- [Wu et al. (2024b)](/sources/wu-2024-b.md) — §II.D, Eqs. (20)–(22) (Ren-type discontinuity measure setting an adaptive TENO cut-off).
- [Bilocq et al. (2025)](/sources/bilocq-2025.md) — §3.5, Eqs. (29)–(31) (Hennemann-calibrated modal-energy sensor); §3.6 (sensor-selected entropy-stable cells); §4.1.5, Figs. 3–4, Table 4 (Persson–Peraire, Hennemann and Fernandez detectors compared); §4.2.2, Table 6 (troubled-cell fractions); §4.3.2–4.3.3, Eq. (39) (sensor widening).
- [Wu et al. (2026)](/sources/wu-2026-b.md) — §3.3, Eqs. (27)–(28), Fig. 4 (total-variation and Ducros factors scaling the Roe dissipation of a sixth-order WCNS; Riemann problem).
- [Bezgin et al. (2025)](/sources/bezgin-2025.md) — §1, §5, §6 (Ducros sensor of compressible ALDM; sensors as the only 3-D information of dimension-by-dimension schemes).
- [Bulgarini et al. (2025)](/sources/bulgarini-2025.md) — §2, Eq. (9) (artificial viscosity without a shock sensor).
- [Bulgarini et al. (2025b)](/sources/bulgarini-2025-b.md) — §3.4, Eqs. (27)–(31) (jump-residual artificial viscosity); §4.2–4.3, Eqs. (39)–(43), Figs. 9–10 (spectral-decay and other refinement indicators).
- [Cuadra et al. (2025)](/sources/cuadra-2025.md) — §III A 1 (dissipation of hybrid schemes set by the sensor); §III A 3, §IV A 3 (subgrid fluxes switched off where shock capturing acts; review).
- [Tsoutsanis & Nogueira (2025)](/sources/tsoutsanis-2025.md) — §4.3, Remarks 3, 5, Fig. 3 (CWENOZ central weight as discontinuity reset of ADDA); §5.3, Fig. 24.
