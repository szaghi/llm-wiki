---
type: Method
title: "Self-adaptive turbulence eddy simulation (SATES)"
description: "SATES, the unified URANS–LES–DNS model of Han and coworkers formerly called VLES, multiplies the k-omega eddy viscosity (BSL or SST host, as each source prints it) by a resolution control function of three length scales; the SATES-SM, SATES-σ and two-layer SATES-II cut-off coefficients, their WCNS numerics in PHengLEI, and high-lift, cylinder and supersonic base-flow results."
status: established
aliases: [SATES, very-large eddy simulation, VLES (Han et al.), SATES-SM, SATES-σ, SATES-sigma, SATES-II, self-adaptive turbulence eddy simulation, adaptive filter-length coefficient]
tags: [hybrid-rans-les, rans, eddy-viscosity, separated-flow, numerical-dissipation]
timestamp: 2026-10-29T10:04:00Z
---

# Self-adaptive turbulence eddy simulation (SATES)

Self-adaptive turbulence eddy simulation (SATES) is a
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) closure that keeps the
transport equations of Menter's BSL $k$-$\omega$ model unchanged and only
multiplies its eddy viscosity by a *resolution control function* $F_r\in[0,1]$
built from an integral length $L_i$, a grid cut-off length $L_c$ and a
Kolmogorov length $L_k$, so that the same equations act as URANS, LES or
DNS according to the local ratio of grid to turbulence scales
([Wu et al. (2023)](/sources/wu-2023-b.md), §2.1.1;
[Wu et al. (2024)](/sources/wu-2024.md), §2.1). The model is that of Han and
coworkers, earlier called very-large eddy simulation (VLES); both papers
use the new name. Two variants are documented: SATES-SM, whose cut-off
coefficient $C_x$ is a constant calibrated against the
[Smagorinsky model](/methods/smagorinsky-model.md), and SATES-σ, whose $C_x$
is made local by a factor built from the [sigma model](/methods/sigma-model.md)
(Wu et al. 2024, §2.2). A third variant, SATES-II of
[Wu et al. (2026)](/sources/wu-2026-b.md), blends a WALE-type near-wall
coefficient with a σ-model coefficient in the outer flow, and the same
coefficient is carried over into IDDES (§2.2–§2.3). The symbols $F_r$, $L_i$, $L_c$, $L_k$, $C_x$,
$\beta_F$, $n_F$ are those of the registry (§11); $F_\sigma$ and
$C_{x,\mathrm{base}}$ are page-local, defined below, and so are the
SATES-II symbols $F_{\mathrm{cor}}$, $C_x^\sigma$, $C_x^{\mathrm{EWT}}$,
$C_{x,\mathrm{II}}$, $f_{\mathrm{bl}}$, $C_{\mathrm{bl}}$, $C_{\mathrm{WT}}$,
$C_m$, $\mathcal D_m$, $T_{\mathrm{RANS}}$, $T_{\mathrm{SGS}}$, $L_{\mathrm{SGS}}$
and $R$ (base radius).

## Formulation

Wu et al. (2023) and Wu et al. (2024) print the BSL $k$-$\omega$ equations as the host model (Wu et
al. 2023, Eqs. 1–3; Wu et al. 2024, Eqs. 1–3), with $F_1$ blending the Wilcox
$k$-$\omega$ and the $k$-$\varepsilon$ constant sets (see
[$k$-$\omega$ SST](/methods/k-omega-sst-model.md)). The modification is

$$\mu_t=F_r\frac{\rho k}{\omega},\qquad
F_r=\min\Big\{1,\Big[\frac{1-\exp(-\beta_FL_c/L_k)}{1-\exp(-\beta_FL_i/L_k)}\Big]^{n_F}\Big\},$$

$$L_i=\frac{k^{3/2}}{\beta^*k\omega},\qquad L_c=C_x\Delta,\qquad L_k=\frac{\nu^{3/4}}{(\beta^*k\omega)^{1/4}},\qquad \Delta=(\Delta_x\Delta_y\Delta_z)^{1/3}$$

(Wu et al. 2023, Eqs. 4–6; Wu et al. 2024, Eqs. 4–6), with
$\varepsilon=\beta^*k\omega$, $\beta^*=0.09$ (both papers' $\beta_1^*$),
$\beta_F=0.002$ (both papers' $\beta^*$) and $n_F=2$ (Wu et al. 2023, Table
1; Wu et al. 2024 prints the square in Eq. 5 and $\beta_F$ in Table 1).

**The host as printed by Wu et al. (2026).** Wu et al. (2026) state that
SATES "is developed based on the SST k-ω turbulence model" and that,
compared with it, SATES "only modifies the formulation of turbulent
viscosity" (§2.1–§2.2). Their eddy viscosity keeps the SST limiter,

$$\mu_t=F_r\,\rho\frac{k}{\omega}F_{\mathrm{cor}},\qquad F_{\mathrm{cor}}=\frac{\omega}{\max(\omega,\lvert S\rvert F_2/a_1)},\qquad F_2=\tanh\Big[\max\Big(\frac{2\sqrt k}{\beta^*\omega d},\frac{500\mu}{\rho\omega d^2}\Big)^2\Big]$$

(Eqs. 1–6), with the same $F_r$, $L_i$, $L_k$, $\beta_F=0.002$, $n_F=2$ and
$\beta^*=0.09$ as above; they call $F_{\mathrm{cor}}$ "the correction
function in SST model", print no value of $a_1$ and no normalization of
$\lvert S\rvert$, and do not print the transport equations. Wu et al.
(2023), Wu et al. (2024) and Wu et al. (2024b) print the BSL equations and
$\mu_t=F_r\rho k/\omega$ without a limiter (above).

Wu et al. (2023) and Wu et al. (2024) read $F_r$ as the ratio of modelled to total turbulent kinetic
energy, the integral of the energy spectrum between $L_k$ and $L_c$ over the
integral between $L_k$ and $L_i$; Wu et al. (2024) say $F_r$ "roughly
resembles" that ratio (§2.1, Eq. 5). Three operating modes follow (Wu et al.
2023, Fig. 1; Wu et al. 2024, Fig. 1):

| Grid relative to turbulence | $F_r$ | Mode |
|---|---|---|
| $L_c\gtrsim L_i$ | $1$ | URANS (the BSL model) |
| $L_k<L_c<L_i$ | $0<F_r<1$ | LES |
| $L_c\to0$ | $\to0$ | DNS |

Wu et al. (2024) note that Han et al.'s formulation has three length scales,
against two in Speziale's VLES (§2.1). Wu et al. (2024b) print Speziale's
form, $\tau^{\mathrm{VLES}}_{ij}=[1-\exp(-\beta_F\Delta/L_k)]^{n_F}\tau^{\mathrm{RANS}}_{ij}$
(Eq. 40, their notation for the modelled stress), and state that it
"would over-damp the Reynolds stress", can hardly return to URANS unless the
mesh is "unreasonably coarse", and tends to RANS behaviour as $Re\to\infty$
($L_k\to0$); SATES instead "tends to the adaptive equilibrium state",
because damping the modelled stress lowers $L_i$, which raises $F_r$ and
counteracts the damping (§III.B).

### SATES-SM: constant cut-off coefficient

In the original model the cut-off coefficient is tied to the Smagorinsky
constant,

$$C_x=\frac{\sqrt{0.3}\,C_s}{\beta^*},\qquad C_s=0.1\ \Rightarrow\ C_x=0.61,$$

calibrated so that the model is "identical to the Smagorinsky-type LES model
when $L_c=L_i$" (Wu et al. 2024, §2.2, Eq. 7; Wu et al. 2023, Eq. 7, Table 1;
$\sqrt{0.3}\times0.1/0.09=0.609$ *(compiler check, not in the sources)*). Wu
et al. (2024) call this version SATES-SM.

[Wu et al. (2024b)](/sources/wu-2024-b.md) print the derivation behind this
calibration (§III.A, Eqs. 28–38). With a Kolmogorov spectrum above the cut-off
$k_c=\pi/\Delta$ they write a filtered eddy viscosity
$\mu_{t,\Delta}$ (page-local) as the product of the subfilter velocity and
length, and define the filtered ratio

$$F_{r,\Delta}=\frac{L_c}{L_i}=\frac{C_x\Delta\,\varepsilon}{k^{3/2}},\qquad \mu_{t,\Delta}=F_{r,\Delta}\,\mu_{\mathrm{RANS}}=\rho C_\mu C_x\Delta\sqrt k$$

(Eqs. 33–34; $\mu_{\mathrm{RANS}}=\rho k/\omega$ the BSL eddy viscosity). Under
production–dissipation equilibrium, $\mu_{t,\Delta}\lvert S\rvert^2=\rho\varepsilon$,
and a shear-flow relation between $k$, $\lvert S\rvert$ and $\varepsilon$
with the constant 0.3, the model equals the Smagorinsky form
$\mu_{t,\Delta}=\rho(C_s\Delta)^2\lvert S\rvert$ with
$C_x=\sqrt{0.3}\,C_s/C_\mu$ (Eqs. 35–38); the relation above prints
$\beta^*$ in the place of $C_\mu$; $C_s=0.1$ is chosen from the typical range 0.08–0.22
(as cited). Expanding the exponentials of $F_r$ for fine grids gives
$F_r\to(L_c/L_i)^{n_F}$ (Eq. 43), from which the authors conclude that "the
SATES guarantees correct LES mode whereas the VLES fails" (§III.B).

### SATES-σ: sigma-model weighting of the cut-off

Wu et al. (2024) argue that a Smagorinsky-type LES mode is "questionable for
near-wall treatment because too much sub-grid-scale (SGS) eddy viscosity is
introduced into the boundary layer" (§1). Their variant SATES-σ multiplies
the base coefficient $C_{x,\mathrm{base}}=0.61$ (page-local) by an
"enhancing factor" $F_\sigma$ (page-local), the ratio of the σ-model to the
Smagorinsky eddy viscosity at the same $\Delta$, and floors the product:

$$C_x=\max\big(C_{x,\mathrm{base}}F_\sigma,\,0.15\big),\qquad
F_\sigma=\Big(\frac{C_\sigma}{C_s}\Big)^2\frac{\mathcal D_\sigma}{\lvert S\rvert},\qquad
\mathcal D_\sigma=\frac{\varsigma_3(\varsigma_1-\varsigma_2)(\varsigma_2-\varsigma_3)}{\varsigma_1^2}$$

(§2.2, Eqs. 8–11, Table 1), with $C_\sigma=3.0$, $C_s=0.1$, $\lvert S\rvert$
with the factor two and $\varsigma_1\ge\varsigma_2\ge\varsigma_3$ the
singular values of the velocity gradient. Because $\mathcal D_\sigma$
vanishes for two-dimensional or two-component fields, including pure shear
and solid rotation, $F_\sigma$ lowers the eddy viscosity in laminar and
initial-shear regions; the authors credit this with capturing
laminar–turbulent transition, stating that the model "can improve the rapid
transition from RANS to LES by using the local structure parameter of
σ-model to identify the laminar region" (§2.2, §4). The floor 0.15 guards
coarse grids, on which unresolved turbulent boundary layers "would be
identified as pure shear flows with vanished turbulent viscosity" (§2.2).
On the supercritical cylinder $C_x$ rises from the floor at the leading edge
to values above 1.0 in the boundary layer before separation (§3.2, Figs. 8,
11). The constant $C_\sigma=3.0$ enters only through $(C_\sigma/C_s)^2$
together with $C_{x,\mathrm{base}}$ and the floor; it is not the stand-alone
σ-model constant tabulated on the [sigma model](/methods/sigma-model.md) page.

### SATES-II: a two-layer coefficient read as a ratio of time scales

Wu et al. (2026) summarize the earlier variants in their Table 1: SATES-SM
is "Simple, but lacks local adaptivity" and weak in free shear layers,
SATES-σ is good in free shear flows but has "weak modeling capability in
wall boundary layers" (§1, Table 1). They also cite a dynamic coefficient
of Lu et al. (2025, as cited), obtained by equating the SATES length with a
Boussinesq subgrid viscosity $\mu_t^{\mathrm{SGS}}=\rho(C_m\Delta)^2\mathcal D_m$
($C_m$ a model constant, $\mathcal D_m$ a differential operator "with units
of frequency"; Lu et al. used the [WALE model](/methods/wale-model.md)),
printed as $C_x=C_m^2\mathcal D_m\Delta/\sqrt k$ (Eqs. 8–9). Because this
coefficient grows with $\Delta$, the authors call it an "undesirable
grid-dependence" (Table 1, §2.2).

**Time-scale reading of $C_x$.** Wu et al. (2026, §2.2) cite Johansen et
al. (2004) for the statement that the URANS eddy viscosity equals a
subgrid viscosity when $L_c=L_i$; on that basis they equate the SATES eddy viscosity with a
RANS viscosity $L_i^2/T_{\mathrm{RANS}}$ and with a subgrid viscosity
$L_{\mathrm{SGS}}^2/T_{\mathrm{SGS}}$ and print the result

$$L_c=L_{\mathrm{SGS}}\sqrt{\frac{T_{\mathrm{SGS}}}{T_{\mathrm{RANS}}}},\qquad C_x=C_m\sqrt{\frac{T_{\mathrm{SGS}}}{T_{\mathrm{RANS}}}}$$

(Eq. 10), where $T_{\mathrm{RANS}}$, $T_{\mathrm{SGS}}$ and $L_{\mathrm{SGS}}$
(page-local) are time and length scales the paper does not define further.
They read $C_x$ as "a blending of the RANS and LES time scales", which
"should be independent of numerical discretization", so that in SATES-II
"the grid effect is confined solely in the filter length scale,
$L_c=C_x\Delta$" (§2.2).

**Outer coefficient from the σ model.** With the
[sigma model](/methods/sigma-model.md) as the subgrid model they print

$$C_x^\sigma=\frac{C_\sigma}{\beta^*}\sqrt{\frac{\mathcal D_\sigma}{\omega}}\,\frac{1}{\sqrt{F_{\mathrm{cor}}}},\qquad C_\sigma=1.5,$$

with $\mathcal D_\sigma$ the operator of the σ model built from the singular
values $\varsigma_1\ge\varsigma_2\ge\varsigma_3$ of the velocity gradient
and the floor $C_x^\sigma=\max(C_x^\sigma,0.15)$ "in the previous SATES-σ
model" (Eqs. 11–12). This is a different expression from the SATES-σ
coefficient of Wu et al. (2024) above ($C_\sigma=3.0$, through
$F_\sigma$), which Wu et al. (2026) reprint in their Table 1 as the
"SATES-σ" row.

**Inner coefficient from WALE ("enhanced wall treatment").** With
$\mathcal S_{ij}$ the traceless symmetric part of the squared velocity
gradient, as on the [WALE page](/methods/wale-model.md),

$$C_x^{\mathrm{EWT}}=C_{x,\mathrm{base}}\Big(\frac{C_{\mathrm{WT}}}{C_s}\Big)^2\frac{(\mathcal S_{ij}\mathcal S_{ij})^{3/2}}{\big[(\mathcal S_{ij}\mathcal S_{ij})^{5/4}+(S_{ij}S_{ij})^{5/2}\big]\lvert S\rvert},$$

with $C_{x,\mathrm{base}}=0.61$, $C_s=0.1$ and $C_{\mathrm{WT}}=0.325$, a
constant that "has a value between 0.325 and 0.5" (Eqs. 13–14). The
form is that of the SATES-σ factor, the base coefficient times the ratio of
the WALE to the Smagorinsky subgrid viscosity at equal $\Delta$ *(compiler
check, not in the sources)*.

**Blending.** The two are combined by a modified SST $F_2$:

$$C_{x,\mathrm{II}}=C_x^\sigma(1-f_{\mathrm{bl}})+C_x^{\mathrm{EWT}}f_{\mathrm{bl}},\qquad f_{\mathrm{bl}}=\tanh\Big[\Big(C_{\mathrm{bl}}\max\Big(\frac{2\sqrt k}{\beta^*\omega d},\frac{500\nu}{\omega d^2}\Big)\Big)^4\Big],\qquad C_{\mathrm{bl}}=0.67$$

(Eqs. 15–16; the source's $f_{\mathrm{blend}}$ and $C_1$), so that
$f_{\mathrm{bl}}=1$ applies the wall treatment in the inner boundary layer
and $f_{\mathrm{bl}}=0$ recovers the σ-model coefficient in the outer flow.
Table 1 describes SATES-II as "Dynamic blending of RANS/LES time scales and
providing enhanced wall treatment". The authors present the adaptive
coefficient as "a general improvement strategy" for hybrid RANS/LES
methods and transplant it into IDDES (AIDDES, on the
[DES page](/methods/detached-eddy-simulation.md)); extension to PANS and
PITM, to other host models (which "requires reinterpreting time scales")
and to strongly non-equilibrium flows such as strong shock/boundary-layer
interaction, "where the time-scale separation may become less
well-defined", is left open (§1, §2.3, §5).

## Relation to VLES and to DES

Wu et al. (2023) and Wu et al. (2024) justify the renaming by Pope's definition of very-large eddy
simulation as LES whose filter and grid "are too coarse to resolve 80% of
the energy": Wu et al. (2023) state that the method resolves "larger than
90%" of the kinetic energy even on coarse grids and so performs like Pope's
traditional LES (§2.1.1), and Wu et al. (2024) that it "behaves
significantly different from the original VLES method defined by Pope"
regarding the resolved fraction (§2.1). Wu et al. (2023) contrast SATES with
[DES-type methods](/methods/detached-eddy-simulation.md), "which typically
treat the entire attached boundary layer with a RANS approach" (§1), and
list DES, DDES and IDDES as suffering from grid-induced separation and "a
slow 'transition' from RANS to LES" (§1). Wu et al. (2024) cite RANS and
transitional and turbulent DDES that "did not show an appropriate drop in
lift after stall", attributing it to the thick RANS layer of DDES (§1,
§3.3). Wu et al. (2023) list [PANS](/methods/partially-averaged-navier-stokes.md)
beside DES and VLES among bridging methods (§1).

Wu et al. (2026) bring the two families together. Their AIDDES replaces
the LES length of SST-IDDES by $C_{x,\mathrm{II}}(\Delta_x\Delta_y\Delta_z)^{1/3}$,
and they define for IDDES a SATES-like indicator, the ratio of the IDDES
hybrid length to $L_i$, which "approximates the weight of the integral
length scale in the hybrid length scale" (§2.3, Eqs. 17–21; formulas on
the [DES page](/methods/detached-eddy-simulation.md)). In their runs IDDES
keeps this indicator near 1 in the attached boundary layer (shielding) but
lets it decay slowly in separated shear layers, which they read as a
delayed RANS-to-LES transition; SATES-SM gives $F_r$ of "about 0.2 − 0.4"
in the attached boundary layer upstream of the base flow's separation,
i.e. insufficient near-wall modelling, while SATES-II gives
$F_r\approx0.9$–1.0 in the inner layer and low values in the separated shear
layer and recirculation region (§4.1.2, Fig. 8).

## Numerics

Wu et al. (2023) and Wu et al. (2024) run SATES in the CARDC structured finite-difference solver
[PHengLEI](/software/phenglei.md), with the fourth-order
[weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md)
(explicit flux difference with coefficients $9/8$ and $-1/24$, Roe flux,
fifth-order interpolation) and fourth-order central viscous terms (Wu et al.
2023, §2.2.1, Eqs. 12–14; Wu et al. 2024, §2.3, Eqs. 13–15). Both find the
result sensitive to the scheme's [numerical dissipation](/properties/numerical-dissipation.md):

- Wu et al. (2023), 30P30N at $Re=1.71\times10^6$: SATES lift on the fine grid
  is 2.82 with linear-weight interpolation (WCNS-L), 2.64 with Z-type weights
  (WCNS-Z) and 2.52 with a second-order blended central/upwind scheme (2%
  upwind), against the experimental 2.83 (Table 2); the authors recommend
  linear weights for shock-free low-Mach flows (§3.3).
- Wu et al. (2024), supercritical cylinder at $Re_D=3\times10^6$: SATES-σ with
  a MUSCL scheme fails to delay separation, damps the Kelvin–Helmholtz
  instability, shortens the recirculation and gives $C_D=1.26$ against 0.55
  with WCNS (§3.2, Table 3, Figs. 13–17); they call WCNS "more accurate and
  necessary".

Time integration is second-order backward differentiation with implicit
LU-SGS sub-iterations, and the runs start from steady RANS fields (Wu et al.
2024, §2.4).

Wu et al. (2024b) move SATES to the fifth-order WCNS (sixth-order explicit
flux difference, three third-order interpolation candidates) and study the
nonlinear weights of its interpolation in the same PHengLEI dual-time setting
(§II, §IV.C). The TENO-type sharp cut-off of the weights, they argue, makes
the weights discontinuous for marginally resolved turbulence, which "would
lead to numerical instability or bad convergence in the SATES simulation"
(§I); they replace it by a smooth $\tanh$ cut-off (details on the
[WCNS page](/methods/weighted-compact-nonlinear-scheme.md)). In SATES runs of
the modified BANC-III 30P30N (about 27 M cells) and of the Herrin–Dutton
supersonic axisymmetric base flow ($M_\infty=2.46$, about 7 M and 42 M cells):

- Jiang–Shu weights are over-dissipative: they suppress the Kelvin–Helmholtz
  instability of the slat-cove and base shear layers and give the largest
  $C_p$ deviation, mostly on the flap (§IV.C, Figs. 7–8, 12);
- the sub-iteration residual of the base flow falls by about one order with
  the sharp TENO cut-off, three with the smooth one and two with its
  adaptive form (Fig. 13); the smooth form predicts the slat-cove vorticity
  and the base-flow TKE peaks better than the sharp one, which the authors
  attribute "largely" to the better sub-iteration convergence (Figs. 10, 14);
- on the coarse base-flow grid the adaptive smooth form gives the best TKE
  profiles against experiment, the fine-grid reference being Jiang–Shu
  weights on 42 M cells (Fig. 14);
- the TENO-type weights cost 1.51 to 1.68 times the CPU hours of Jiang–Shu
  weights, Z-type weights 1.02 to 1.03 times (Table I).

Wu et al. (2026) run SATES-SM, SATES-II, SST-IDDES and AIDDES in
PHengLEI-HyOrder, the group's high-order cell-centred finite-difference
branch of [PHengLEI](/software/phenglei.md) (§3.4): a sixth-order WCNS
whose interpolation combines one sixth-order and three third-order
candidates with multi-order-candidate weights and the smooth scale
separation of Wu et al. (2024b) (MOC6-STA, §3.1–§3.2, Eqs. 22–25), a Roe
flux whose dissipation is scaled by a sensor combining a total-variation
indicator and the Ducros factor (Eqs. 27–28; see
[shock sensors](/definitions/shock-sensor.md)), fourth-order central
viscous terms, a second-order upwind scheme for the turbulence equations,
and second-order backward differentiation with LU-SGS and Newton-like
sub-iterations; hybrid runs start from steady RANS fields. Details are on
the [WCNS page](/methods/weighted-compact-nonlinear-scheme.md).

## Results

**Validation cases of SATES-σ** (Wu et al. 2024, §3.1). In
[turbulent channel flow](/benchmarks/turbulent-channel-flow.md) at
$Re_\tau=395$ ($64\times96\times64$ and $128\times120\times64$, first $y^+$ of
0.6 and 0.3) the mean velocity agrees with the DNS of Moser et al., the small
shift on the coarse grid disappearing on the fine one; $F_r=1$ at the wall
(URANS mode) and decreases away from it, and the ordering
$R_{11}>R_{33}>R_{22}$ of the normal stresses is captured (Figs. 2–4). On the
[square cylinder](/benchmarks/square-cylinder-flow.md) at $Re_D=2.2\times10^4$
(0.66 M and 1.73 M cells) mean velocities and resolved normal stresses at
$x/D=0$–3 agree with DNS and LDV on both grids (Figs. 5–6).

**Supercritical circular cylinder** ($Re_D=3\times10^6$, $M=0.2$, about 6.7 M
cells, span $1D$; Wu et al. 2024, §3.2, Table 3; see
[circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)):

| Case | $St$ | $C_{pb}$ | $L_r/D$ | $C_D$ |
|---|---|---|---|---|
| SST-IDDES, WCNS | 0.29 | −0.68 | 0.63 | 0.62 |
| SATES-SM, WCNS | 0.20 | −1.69 | 0.33 | 1.39 |
| SATES-σ, WCNS | 0.24 | −0.34 | 0.79 | 0.55 |
| SATES-σ, MUSCL | 0.19 | −1.32 | 0.61 | 1.26 |
| Shih et al. experiment, $Re_D=1\times10^6$ (as listed) | 0.22 | −0.33 | — | 0.24 |

SATES-SM predicts "the incorrect flow topology of the subcritical regime",
with $F_r\approx1$ near the wall (fully turbulent boundary layer); SATES-σ
gives low eddy viscosity in the initial boundary layer, a low-TKE front half
followed by a sharp rise (transition), a turbulent separation that
suppresses alternate shedding, and the best mean $C_f$ against Achenbach's
experiment (Figs. 8–12). The authors caution that experiments and
simulations at supercritical $Re_D$ "do not have good convergence" and judge
the models by the tendency of the flow topology (§3.2).

**30P30N high-lift airfoil** (see the
[30P30N benchmark](/benchmarks/30p30n-high-lift-airfoil.md)). On the modified
BANC-III geometry at $Re=1.71\times10^6$, $M=0.17$, $\alpha=5.5^\circ$, SATES
with WCNS-L gives $C_L$ within 3% of the measured 2.83 on 7.2 M, 19 M and 27 M
cells (0.7%, −2.8%, −0.4%), against −6.7% for Smagorinsky LES ($C_s=0.1$) and
−19.8% for SST-IDDES on the fine grid; IDDES separates early on the flap,
"which may have been caused by the GIS", carries larger $\mu_t$ in attached
layers and the slat cove, and resolves less kinetic energy than SATES, which
the authors read as "a faster 'transition' from RANS to LES than IDDES" (Wu
et al. 2023, Table 2, §3.4, Figs. 17–25). On the MD-30P30N at
$Re_C=9\times10^6$, $M=0.2$, $\alpha=8$–$24^\circ$ (12.8 M and 26.4 M cells),
SATES-σ gives grid-converged $C_p$ at $21^\circ$ that agrees with experiment
better than SATES-SM and IDDES, especially at the suction peaks of the main
element and flap; a $C_p$ plunge at $x/c\approx0.15$ at $8^\circ$ indicates a
[laminar separation bubble](/definitions/laminar-separation-bubble.md); and
the total-lift error is "always less than 6.5%, even at post-stall
conditions", the maximum lift and the stall being captured (Wu et al. 2024,
§3.3, Figs. 22–26). The flap lift is over-predicted, which the authors
attribute to free-air simulation against wind-tunnel blockage (§3.3).

**SATES-II and AIDDES** (Wu et al. 2026, §2.4, §4). On the NASA
zero-pressure-gradient [flat plate](/benchmarks/turbulent-boundary-layer.md)
($M=0.2$, $Re=5\times10^6$ per unit length, $137\times97\times97$ points)
SATES-SM under-predicts the skin friction against the SST results of CFL3D
and FUN3D, while the wall treatment of SATES-II restores it and AIDDES
leaves the wall behaviour of IDDES unchanged (Fig. 1). On the Herrin–Dutton
[supersonic axisymmetric base flow](/benchmarks/supersonic-axisymmetric-base-flow.md)
($M_\infty=2.46$, grid of $9.5\times10^6$ cells, 640 cores; Table 3):

| Model | $L_r/R$ | error | wall time (h) |
|---|---|---|---|
| SATES-SM | 3.17 | +20.5% | 50.28 |
| SATES-II | 2.81 | +6.8% | 51.59 |
| SST-IDDES | 3.58 | +36.1% | 45.30 |
| AIDDES | 2.81 | +6.8% | 46.54 |
| experiment | 2.63 | | |

($L_r$ the recirculation length, registry §11; $R$ the base radius.) The
four models "roughly consume comparable computing resources" (§4.1.3);
the resolved kinetic energy of the shear layer deviates most with IDDES,
less with SATES-SM, and is most accurate with SATES-II, AIDDES being
comparable (Fig. 11). On the [30P30N airfoil](/benchmarks/30p30n-high-lift-airfoil.md)
at $Re_C=9\times10^6$, $M=0.2$, $\alpha=21^\circ$ (page-local angle of
attack), SATES-SM separates prematurely on the slat upper surface, which
the authors attribute to the lack of wall modelling, SATES-II gives
$F_r\to1$ near the walls and improves the boundary-layer profiles at
$x/C=0.85$–0.975 and on the flap, IDDES gives a "relatively stable
quasi-two-dimensional" slat wake, and AIDDES stronger three-dimensional
fluctuations than IDDES (§4.2, Figs. 12–14).

## Qualifications

- All evidence is numerical comparison with experiment and other
  simulations; neither Wu et al. (2023) nor Wu et al. (2024) analyses the model. The SATES "LES mode" is
  the eddy viscosity $F_r\rho k/\omega$, linked to the Smagorinsky model only
  through $C_x$.
- Wu et al. (2024) state the limit of SATES-σ themselves: because it works
  close to its LES mode, transition "may not be captured accurately if the
  computational grid resolution is insufficient", unlike DDES, which is
  closer to URANS (§4). Transition is captured here without a transition
  model.
- In Wu et al. (2024) Table 3, titled "at $Re_D=3\times10^6$", the reference
  LES of Catalano et al. and the experiment of Shih et al. are listed at
  $Re_D=1\times10^6$.
- Printed slips of Wu et al. (2024): Eq. 12 prints
  $\partial U/\partial t+\partial E/\partial t=0$ while Eqs. 13–14
  discretize a spatial derivative of $E$; time steps are printed as
  $\Delta tD/U_\infty$ for the cylinders and for the airfoil, beside
  flow-through times printed as $tU_\infty/C$ for the cylinders (§3.1b,
  §3.2, §3.3); §3.3 prints 12.8 M and 26.4 M cells for the 30P30N grids
  while §4 says "approximately 24 million"; the MUSCL scheme is called third
  order in §2.4 and in one sentence of §3.2, second order elsewhere in §3.2
  and in §4.
- Wu et al. (2023) write that "$\beta$ and $n$ are the model constants" of
  $F_r$ while Eq. 5 and Table 1 use their $\beta^*$ (here $\beta_F$); their
  Fig. 1 writes the integrals as $\int E(L)\,dL$ and Eq. 5 as
  $\int E(k)\,dk$ with length-scale limits (details on the
  [hybrid RANS/LES](/definitions/hybrid-rans-les.md) page).
- Wu et al. (2024b) state that the fine-grid limit $(L_c/L_i)^{n_F}$ with
  $n_F=2$ "approaches the form in the filtered URANS computation as shown in
  Eq. (33)", where $F_{r,\Delta}=L_c/L_i$ carries the first power; and they
  define $L_c=\tfrac14\gamma_{\mathrm a}\Delta$ and
  $L_i=\mu_{\mathrm{RANS}}/(\rho\sqrt{2k/3})$ in Eq. 32 (with an anisotropy
  factor, here $\gamma_{\mathrm a}$, page-local) but $L_c=C_x\Delta$,
  $L_i=k^{3/2}/\varepsilon$ in Eq. 42, the constants being absorbed in $C_x$.
  Their printed shear-flow relation "$\langle uv\rangle\approx0.3k|S|=\varepsilon$"
  (Eq. 36) equates quantities of different dimensions (velocity squared,
  velocity squared per time) *(compiler check, not in the sources)*. Their
  heat flux multiplies the effective viscosity by a single $Pr$, with no
  turbulent Prandtl number stated (Eq. 4).
- Wu et al. (2026) test SATES-II on the flat plate (against the SST
  results of CFL3D and FUN3D), the base flow and the 30P30N airfoil; the
  base-flow errors of Table 3 are relative to the one experimental
  recirculation length $L_r/R=2.63$. Their remaining AIDDES deviations "may originate from
  the lack of a realistic turbulent boundary layer at inlet" (§4.1.3).
- In Wu et al. (2026), Eq. (11) carries the factors $1/\beta^*$ and
  $F_{\mathrm{cor}}^{-1/2}$, which Eq. (10) does not show, and Table 1
  prints the SATES-II coefficient as $(C_m/\beta^*)\sqrt{\mathcal D_m/\omega}$,
  without $F_{\mathrm{cor}}$. Substituting their Eq. (8) into the middle
  expression of their Eq. (9),
  $\Delta^{-1}\mu_t^{\mathrm{SGS}}/(C_\mu\sqrt k)$, gives
  $\rho C_m^2\mathcal D_m\Delta/(C_\mu\sqrt k)$, while the printed result is
  $C_m^2\mathcal D_m\Delta/\sqrt k$ *(compiler check, not in the sources)*.
  They define the squared gradient of Eq. (13) in words as
  "$g^2_{ij}=g_{ij}g_{ij}$", a scalar contraction, while the same equation
  uses it as a tensor with free indices and a trace $g^2_{kk}$; the WALE
  tensor written above is the one of the WALE page. The introduction
  prints $F_r$ without the $\min(1,\cdot)$ of Eq. (5).

# Citations

- [Wu et al. (2023)](/sources/wu-2023-b.md) — §1 (DES deficiencies, bridging methods); §2.1.1, Eqs. (1)–(7), Table 1, Fig. 1 (SATES formulation, renaming from VLES); §2.2 (WCNS, blended scheme); §3.2–§3.4, Table 2, Figs. 6–25 (30P30N grid, scheme and model comparisons); §4.
- [Wu et al. (2024)](/sources/wu-2024.md) — §1 (SGS viscosity in boundary layers, DDES after stall); §2.1, Eqs. (1)–(6), Fig. 1 (SATES, three modes, Pope's VLES); §2.2, Eqs. (7)–(11), Table 1 (SATES-SM and SATES-σ); §2.3–§2.4, Eqs. (12)–(17) (WCNS-E-4, MUSCL, time integration, PHengLEI); §3.1 (channel, square cylinder); §3.2, Table 3, Figs. 7–17 (supercritical cylinder); §3.3, Figs. 18–26 (MD-30P30N stall sweep); §4.
- [Wu et al. (2026)](/sources/wu-2026-b.md) — §1, Table 1 (earlier SATES variants, Lu et al.'s coefficient); §2.1–§2.2, Eqs. (1)–(16) (SST host with $F_{\mathrm{cor}}$, time-scale reading of $C_x$, $C_x^\sigma$, WALE-type wall treatment, SATES-II blending); §2.3, Eqs. (17)–(21) (AIDDES, IDDES resolution indicator); §2.4, Fig. 1 (flat plate); §3.1–§3.4, Eqs. (22)–(28) (MOC6-STA WCNS, adaptive Roe dissipation, PHengLEI-HyOrder); §4.1–§4.2, Tables 2–3, Figs. 5–14 (base flow and 30P30N); §5.
- [Wu et al. (2024b)](/sources/wu-2024-b.md) — §I (sharp TENO cut-off and SATES convergence); §III.A–B, Eqs. (24)–(45) (BSL host model, filtered eddy viscosity, Smagorinsky calibration of $C_x$, Speziale VLES against SATES, fine-grid limit, self-adaptivity); §IV.C, Figs. 7–14, Table I (30P30N and supersonic base flow with fifth-order WCNS weights, sub-iteration convergence, cost).
