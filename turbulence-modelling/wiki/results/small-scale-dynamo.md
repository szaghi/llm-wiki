---
type: Result
title: "Small-scale turbulent dynamo"
description: "The small-scale (fluctuation) dynamo amplifies magnetic fields by turbulent stretching without a mean field; the page gathers its kinematic and saturated stages, Schekochihin's (2022) tearing-limited saturation theory, and simulation evidence on growth rates, saturation levels, resolution, multiphase gas, and the stretching, winding and compression split of the growth rate under explicit bulk viscosity."
status: hypothesis
aliases: [fluctuation dynamo, turbulent dynamo, saturated dynamo, tearing-limited dynamo, reconnection-limited dynamo]
tags: [dynamo, mhd, astrophysics, reconnection, dns, compressible]
timestamp: 2026-10-26T15:53:00Z
---

# Small-scale turbulent dynamo

The **small-scale (fluctuation) dynamo** is the exponential amplification of
a weak magnetic field by a turbulent flow without a mean field, at scales
smaller than the outer scale of the flow, followed by a nonlinear stage and a
saturated state of statistically steady MHD turbulence. [Schekochihin
(2022)](/sources/schekochihin-2022.md) (§13) reviews the classical picture
(as recalled from Batchelor 1950, Biermann & Schlüter 1951, Kazantsev 1968,
and the author's own earlier work, Schekochihin et al. 2002, 2004) and
proposes a **tearing-limited** theory of the saturated state: the folded
fields are disrupted by tearing, which sets their reversal scale and seeds a
local cascade that resembles the [tearing-mediated
turbulence](/results/tearing-mediated-mhd-turbulence.md) of the
strong-mean-field case. The page carries `status: hypothesis`: the author
presents the theory as new, supported by "tentative evidence", and leaves
open the central question of the saturated state (§13.3.4).

Four simulation studies of astrophysical gas add measured growth rates and
saturation levels: [Seta & Federrath (2022)](/sources/seta-2022.md) run the
dynamo in a driven, thermally bistable two-phase medium with explicit
viscosity and resistivity; [Martin-Alvarez et al.
(2022)](/sources/martinalvarez-2022.md) measure how the resolved dynamo in a
cosmological galaxy simulation depends on resolution and refinement
strategy; [Liu et al. (2022)](/sources/liu-2022.md) model the part of the
dynamo the grid cannot resolve; [Beattie et al. (2025)](/sources/beattie-2025.md)
control the dissipation of the compressive velocity modes with an explicit
[bulk viscosity](/definitions/bulk-viscosity.md) and split the growth rate
into stretching, winding and compression. None of them tests the
tearing-limited theory (see Qualifications).

Page-local notation: $\ell$ is the scale of the stretching motions, $L$ the
outer scale, $\delta u_\ell$ the velocity increment at $\ell$,
$Rm_\ell=\delta u_\ell\ell/\eta_m$ and $Rm_L$ the magnetic Reynolds numbers
at $\ell$ and $L$, $Re_{\mathrm{eff},\ell}=\delta u_\ell\ell/(\nu+\eta_m)$,
$b_\lambda$ the amplitude (velocity units) of a field reversing across a
fold of width $\lambda$, $\varepsilon$ the energy flux of the turbulence.
In the simulation sections, $E_{\mathrm{mag}}$ and $E_{\mathrm{kin}}$ are
magnetic and turbulent kinetic energies, $\Gamma_E$ an exponential growth
rate of magnetic energy (the quantity it refers to is stated per source),
$R_{\mathrm{sat}}=E_{\mathrm{mag}}/E_{\mathrm{kin}}$ in the saturated state,
$E_B(k)$ the magnetic energy spectrum, $h_{\min}$ the finest cell size,
$c_s$ the sound speed and $t_0$ the eddy-turnover time at the driving scale;
the turbulent Mach number is $M_t=u_{\mathrm{rms}}/c_s$. In the
bulk-viscosity section, $\nu_b$, $Re_{\mathrm{bulk}}$, $P_\nu=\nu/\nu_b$,
$\boldsymbol u_{\mathrm c}$, $\boldsymbol u_{\mathrm s}$, $E_{\mathrm c}$,
$E_{\mathrm s}$ are the bulk viscosity, bulk Reynolds number, viscous Prandtl
number and the compressive and solenoidal velocity parts and their kinetic
energies, as defined on [bulk viscosity](/definitions/bulk-viscosity.md),
$\ell_0$ the driving scale, and $\gamma_B$ (page-local) the instantaneous
growth rate of $\langle\boldsymbol B^2\rangle$ divided by two, so that
$\Gamma_E=2\gamma_B$ in the kinematic stage.

## Kinematic stage and the onset of tearing

In the kinematic regime the field is organized in folds — long in the
direction of the field, reversing across a resistive width
$\lambda\sim\ell\,Rm_\ell^{-1/2}$ (Eq. 13.2, as recalled). Treating a fold
as a current sheet, the review (§13.3.1) applies the tearing growth rate of a
reversing field,

$$\gamma_{\mathrm t}\sim b_\lambda^{1/2}\lambda^{-3/2}\eta_m^{1/2}(1+Pm)^{-1/4}$$

(Eq. 13.3; page-local $\gamma_{\mathrm t}$), and finds that tearing outpaces
the resistive evolution of the fold once
$b_\lambda\sim\delta u_\ell\,Re_{\mathrm{eff},\ell}^{-1/2}$ (Eq. 13.4), i.e.
already when the field is far weaker than the flow. Hence the review's
statement that "a nonlinear dynamo is also a reconnecting dynamo".

## Self-similar nonlinear stage

Recalled from Schekochihin et al. (2002), Cho et al. (2009) and Beresnyak
(2012) (§13.3.2): once the field is strong enough to suppress the stretching
motions at scale $\ell$, the dynamo proceeds at the scale where
$\delta u_{\ell(t)}\sim b_\lambda(t)$ (Eq. 13.5), so

$$b_\lambda\sim(\varepsilon t)^{1/2},\qquad \ell(t)\sim\varepsilon^{1/2}t^{3/2}$$

(Eq. 13.6): magnetic energy grows linearly in time. The fraction of the
energy flux going into the field is quoted as 0.04–0.07 (Cho et al. 2009;
Beresnyak 2012), with $3/38$ from Xu & Lazarian (2016), all as recalled.

## Saturation: tearing-limited folds

When $\ell$ reaches the outer scale, the fold-reversal scale is set by
tearing (Eq. 13.7, condition 13.8) and not by Ohmic diffusion
(§13.3.3):

$$\lambda_R\sim L\,Rm_L^{-1/3}(1+Pm)^{-1/6}$$

(Eq. 13.9; $\lambda_R$ page-local), instead of the $L\,Rm_L^{-1/2}$ of the
author's earlier view. A torn fold of length $L$ yields
$N\sim Rm_L^{1/6}(1+Pm)^{1/3}$ islands (Eq. 13.10; page-local $N$). The flux
ropes so produced have amplitude given by Eq. (13.11) and a critically
balanced parallel length
$l_\parallel\sim L\,Rm_L^{-2/9}(1+Pm)^{-1/9}$ (Eq. 13.12), with the
outer-scale velocity playing the role of the Alfvén speed and the fold field
the role of a local mean field. The resulting cascade is a [critically
balanced](/properties/critical-balance.md) [RMHD](/definitions/reduced-mhd.md)
cascade with $\lambda_R$ in the role of the critical-balance scale and the
small ordering parameter

$$\frac{\delta u_{\lambda_R}}{\delta u_L}\sim\frac{\lambda_R}{l_\parallel}\sim Rm_L^{-1/9}(1+Pm)^{-1/18}\ll1$$

(Eq. 13.13). This cascade is [aligned](/properties/dynamic-alignment.md),
then disrupted by tearing at (Eq. 13.15)

$$\lambda_D\sim L\,Rm_L^{-41/63}(1+Pm)^{-41/126},$$

below which it has the $k^{-11/5}$ envelope of the tearing-mediated range,
and it ends at the Kolmogorov scale $\sim L\,Re_{\mathrm{eff},L}^{-3/4}$
(Eq. 13.16; $\lambda_D$ page-local). The review's conclusion is that
"universality is regained at small scales": even without a mean field, MHD
turbulence "manages to turn itself into RMHD (Alfvénic) turbulence, at least
in local patches", with statistics isotropic overall because the local mean
field fluctuates (§13.3.3, citing Beresnyak & Lazarian 2009 and St-Onge et
al. 2020 for the latter).

## Numerical evidence cited

- **Folds become current sheets.** The review cites its own unpublished
  simulations (Iskakov & Schekochihin 2008: $512^3$, $Pm=1$, $Re=1360$ with
  $Re=u_{\mathrm{rms}}/(\nu k_0)$, $k_0=2\pi$, Fig. 31) showing inflow–outflow
  patterns around field reversals and corrugated folds with plasmoid-like
  structures, and Beresnyak (2012, unpublished: $1024^3$, $Pm=10$,
  $Re\approx500$, Fig. 32) with the same features; none of these appear in
  the "Stokes" regime $Re\sim1$, $Pm\gg1$, where the saturated field stays
  smoothly folded at the resistive scale (§13.2, footnote 74).
- **Spectra.** In saturated-dynamo simulations the kinetic-energy spectrum
  steepens at large scales (an empirical $k^{-7/3}$) and becomes shallower,
  $\approx k^{-4/3}$, at small scales (Grete et al. 2021, as recalled), with
  magnetic-to-kinetic transfer via tension at small scales — consistent with
  reconnection in folds driving flows (§13.2, Fig. 33).
- **Tests of the tearing-limited theory.** Galishnikova et al. (2022, up to
  $2240^3$), designed to test the fold-tearing scenario, "appear to offer some
  tentative evidence" for the disruption of folds by tearing, for the scaling
  of the reversal scale with $Rm^{-1/3}$, and for a steeper-than-Kolmogorov
  spectrum ($\propto k^{-2}$ "or thereabouts") below $\lambda_R$ (§13.3.4).

## Saturation scenarios above $\lambda_R$

The theory does not say whether magnetic energy stays at $\lambda_R$ or moves
to the outer scale — "the central question of small-scale-dynamo theory"
(§13.3.4). Section 13.4 catalogues speculations, "not necessarily all
mutually exclusive":

- multiscale folds with $b_\lambda\propto\lambda^{3/5}$, i.e. a $k^{-11/5}$
  magnetic spectrum (Eq. 13.17, §13.4.1);
- a $k^{-1}$ magnetic spectrum above $\lambda_R$ (Eq. 13.18, after Yousef et
  al. 2007) and a velocity cascade depleted by dynamo losses,
  $E\propto k^{-(5+2\sigma_d)/3}$ when the rate of transfer into the folds
  times the cascade time is a constant $\sigma_d$ (Eqs. 13.19–13.20,
  page-local $\sigma_d$; §13.4.2);
- **magnetoelastic turbulence**: a tangled field acts as an elastic medium
  with isotropic waves $\omega_f^2=k^2v_A^2$, $v_A^2=\langle b^2\rangle/3$
  (page-local $\omega_f$), and a weak, isotropic
  Iroshnikov–Kraichnan-like cascade $E(k)\sim(\varepsilon v_A)^{1/2}k^{-3/2}$
  (Eqs. 13.21–13.26, §13.4.3), with a polymer analogy;
- a fast-reconnection-limited dynamo with reversal scale
  $\sim\epsilon_{\mathrm{rec}}\ell$ if $Rm_\ell\gtrsim10^6(1+Pm)$
  (Eqs. 13.27–13.29, §13.4.4);
- the Xu & Lazarian (2016) scheme, which the review critiques: its spectral
  "overturning" at constant energy is not seen in $Pm\gg1$, $Re\sim1$ runs
  (§13.4.5);
- Subramanian's (1999) model with an effective resistivity
  $\eta_m+\tau\langle b^2\rangle$ and a reversal scale $L\,Rm_c^{-1/2}$,
  $Rm_c\sim10$–$100$ (Eqs. 13.30–13.32, §13.4.6; $\tau$, $Rm_c$ page-local);
- inverse magnetic-energy transfer via sporadic decay (Eqs. 13.33–13.35,
  §13.4.7) and a local shear dynamo (§13.4.8).

The decay of the saturated state, once forcing stops, is the subject of
[decaying MHD turbulence](/results/decaying-mhd-turbulence.md).

## Measuring growth and saturation in simulations

The simulation sources define the stages operationally and measure
different quantities; their rates are not directly comparable.

- **Seta & Federrath (2022, §4.1)**: kinematic stage = exponential growth of
  the ratio $E_{\mathrm{mag}}/E_{\mathrm{kin}}$, with $\Gamma_E$ in units of
  $t_0^{-1}$; saturated stage = statistically steady ratio, its level
  $R_{\mathrm{sat}}$.
- **Martin-Alvarez et al. (2022, §3.2)**: $\Gamma_E$ is the rate of a fit
  $\propto\exp[\Gamma_E(t-t_0)]$ to the magnetic energy per unit gas mass of
  the galactic region, in Gyr$^{-1}$, over an accretion phase
  ($t\in[0.3,1.4]$ Gyr) and a feedback phase ($t\in[1.7,3.3]$ Gyr); the seed
  ($3\times10^{-20}$ G comoving) never becomes dynamically important, so
  their runs stay kinematic.
- **Liu et al. (2022, §5.1.1)** give the e-folding time of their subgrid
  amplification, $h/\sigma_{\mathrm{sgs}}$ (see [subgrid turbulent dynamo
  model](/methods/subgrid-turbulent-dynamo-model.md)).
- **Beattie et al. (2025, §1, §4.5)**: kinematic, nonlinear and saturated
  stages are exponential, linear and zero growth of the volume-averaged
  magnetic energy; $\Gamma_E$ is fitted by log-linear regression over
  $10\le t/t_0\le30$ in units of $t_0^{-1}$, with $t_0=\ell_0/u_{\mathrm{rms}}$
  and $\ell_0$ half the box, and the saturated ratio $R_{\mathrm{sat}}$ is
  averaged over $t/t_0\ge75$.

## Reynolds number, resolution and numerical dissipation

- **A critical Reynolds number.** As recalled by Liu et al. (2022, §1, from
  Brandenburg & Subramanian 2005), the dynamo needs a dissipation scale at
  least about 30 times below the injection scale, a critical Reynolds number
  of about 30–60. When dissipation is numerical this is a resolution
  requirement: about 30 pc for a 1 kpc galactic disc, about 3 pc for a
  100 pc thin disc. Liu et al. respond with a subgrid model; Martin-Alvarez
  et al. (2022, §4) name that model as the alternative to resolving the
  amplification.
- **Growth rate against $Re$.** Martin-Alvarez et al. (2022, §3.2) recall
  $\Gamma_E\propto Re^{1/2}$ for incompressible (Kolmogorov) and
  $\Gamma_E\propto Re^{0.3}$ for compressible (Burgers) turbulence (Schober
  et al. 2012). With $\eta_m=0$ and all dissipation numerical (numerical
  $Pm\sim2$, §3.3.5), $Re$ is a function of the cell size only. Their
  quasi-Eulerian runs, which refine the whole galaxy to $h_{\min}$, follow
  $\Gamma_E\propto Re^{1/2}\propto h_{\min}^{-1/2}$ ("Kolmogorov turbulence
  + viscosity $\nu\propto\Delta x_{\max}$") in the accretion phase; their
  quasi-Lagrangian runs follow $\Gamma_E\propto h_{\min}^{-0.3}$ for
  $h_{\min}<80$ pc, the compressible value of Federrath et al. (2011), which
  the authors attribute to the refinement strategy rather than to
  compressibility, since the same solver gives the $1/2$ exponent with
  quasi-Eulerian refinement (§3.2, Fig. 7: the paper draws both scalings
  as reference lines and reports no fitted exponent). The refinement strategies are described on
  [RAMSES](/software/ramses.md).
- **Magnitudes.** At $h_{\min}=20$ pc the quasi-Eulerian galaxy has about
  1 dex more magnetic energy per unit mass than the quasi-Lagrangian one, and
  more than the quasi-Lagrangian runs at 10 pc (§3.2, §4, Fig. 6).
  Extrapolated to the 0.7 pc of turbulent-box simulations of the
  interstellar medium (Balsara et al. 2004, as recalled), the accretion-phase
  rates reach about 60 Gyr$^{-1}$ (quasi-Eulerian) against about
  10 Gyr$^{-1}$ (quasi-Lagrangian); the authors extrapolate that with
  realistic diffusivities the dynamo would saturate at $z\gg6$ (§3.2). In
  the feedback phase the lowest resolutions give negative rates (§3.2). The
  feedback strength matters less than the refinement strategy (§3.1, §3.2).
- **Explicit diffusion above the numerical one.** Seta & Federrath (2022,
  §2.4) run $Re=Rm=2000$ ($Pm=1$; $Re=u_{\mathrm{rms}}L_{\mathrm{box}}/(2\nu)$
  at the driving scale $L_{\mathrm{box}}/2$, page-local $L_{\mathrm{box}}$ the
  box size) on $512^3$ cells, below the numerical Reynolds number
  $\approx2N_x^{4/3}\approx8000$ that they recall from McKee et al. (2020),
  so that explicit diffusion dominates and acts at larger scales than the
  numerical one (a [DNS](/definitions/direct-numerical-simulation.md)-type
  criterion for a finite-volume code). The two galaxy studies instead run
  ideal MHD and rely on [numerical
  dissipation](/properties/numerical-dissipation.md), in the manner of
  [implicit LES](/definitions/implicit-les.md).

## Compressibility, driving and multiphase gas

Seta & Federrath (2022) drive turbulence in a periodic 200 pc box
([forced turbulence](/benchmarks/homogeneous-isotropic-turbulence.md) at
$1\le kL_{\mathrm{box}}/2\pi\le3$, $u_{\mathrm{rms}}\approx10$ km s$^{-1}$,
$t_0\approx10$ Myr) with a constant heating rate and the Koyama–Inutsuka
cooling function, so that thermal instability splits the gas into a cold
phase ($T<10^3$ K, about 3–4% of the volume, $M_t\approx5$) and a warm phase
($T\ge10^3$ K, about 96%, $M_t\approx1$) (§2, §3.2). Forcing is purely
solenoidal (Sol) or purely compressive (Comp); the seed has $10^{-10}$ G rms
and a $k^{3/2}$ spectrum. Results (§4.1, Table 1):

| Driving | Phase | $M_t$ | $\Gamma_E$ [$t_0^{-1}$] | $R_{\mathrm{sat}}$ |
|---|---|---|---|---|
| Sol | cold | $4.8\pm0.3$ | $0.37\pm0.02$ | $0.019\pm0.002$ |
| Sol | warm | $1.2\pm0.1$ | $0.37\pm0.02$ | $0.13\pm0.02$ |
| Comp | cold | $5.4\pm0.4$ | $0.18\pm0.01$ | $0.0024\pm0.0007$ |
| Comp | warm | $1.1\pm0.1$ | $0.18\pm0.01$ | $0.021\pm0.005$ |

- **Equal growth in both phases.** The growth rate is the same in the
  supersonic cold and the transsonic warm phase, which the authors state
  "clearly does not agree with the isothermal models" (Federrath et al. 2011,
  as recalled), where $\Gamma_E$ decreases with $M_t$ for $M_t\gtrsim1$.
  Solenoidal forcing grows the field about twice as fast as compressive.
- **Lower saturation in the cold phase**, the same trend with $M_t$ as in
  isothermal runs; attributed to a stronger rms Lorentz force there, which
  stops growth earlier (§4.2, Fig. 12).
- **Below the isothermal model.** Both $\Gamma_E$ and $R_{\mathrm{sat}}$ lie
  below the isothermal empirical model of Federrath et al. (2011) at
  matching $M_t$ (relative differences 0.33–1.11 in $\Gamma_E$ and
  0.43–1.50 in $R_{\mathrm{sat}}$), which the authors attribute, "probably",
  to continuous energy exchange between the phases (§4.1, §5).
- **Vorticity budget.** Projecting the compressible, magnetized vorticity
  equation (Eq. 9; as recalled from Shukurov & Subramanian 2021)

  $$\frac{\partial\boldsymbol\omega}{\partial t}=\nabla\times(\boldsymbol u\times\boldsymbol\omega)+\nu\nabla^2\boldsymbol\omega+\nabla\times\frac{(\nabla\times\boldsymbol B)\times\boldsymbol B}{4\pi\rho}+\frac{\nabla\rho\times\nabla p}{\rho^2}+2\nu\nabla\times\big(\boldsymbol S^d\nabla\ln\rho\big)+\nabla\times\boldsymbol f$$

  on $\boldsymbol\omega$ (the source writes the Lorentz term with the current
  density and the deviatoric strain as $\boldsymbol\tau$; $\boldsymbol S^d$ is
  the matrix of $S^d_{ij}$), the authors find that the turbulent term always
  amplifies vorticity, the baroclinic term amplifies it in the warm phase,
  and the viscous log-density-gradient term destroys it in the cold phase;
  the rms vorticity ends up about equal in both phases, which they offer as
  the "probable" reason for the equal growth rates (§4.2, Figs. 9–10,
  Table 2). Splitting the turbulent term, vortex stretching dominates in the
  warm phase and compression in the cold one (Eq. 10, Fig. 11, Table 3; see
  Qualifications). With compressive forcing the seed vorticity comes from
  the baroclinic and log-density-gradient terms, not from the forcing.
- **Field statistics.** The field is spatially intermittent in both phases
  and its kurtosis drops at saturation, as in earlier isothermal work cited
  by the authors; field-line curvature is higher in the cold phase (§3.1,
  Fig. 6; App. C).

Martin-Alvarez et al. (2022, §3.3.4) find in their galaxy that the warm
phase carries more small-scale turbulent energy with quasi-Eulerian
refinement and state that "the majority of the turbulent amplification in
galaxy simulations takes place in the warm phase of the ISM"; their kinetic
spectra are Kolmogorov-like ($k^{-5/3}$) for the strongly fed runs and
between Kolmogorov and Burgers ($k^{-2}$) for the weak-feedback run
(§3.3.5).

## Stretching against compression

The three galaxy and multiphase sources separate amplification by field-line
stretching from the frozen-in compression scaling
$|\boldsymbol B|\propto\rho^{2/3}$ (magnetic energy density
$\propto\rho^{4/3}$); Beattie et al. (2025) split the growth rate itself
(next section):

- Martin-Alvarez et al. (2022, §3.3.1, Eq. 5, Fig. 8) build an
  adiabatic-compression estimate of the magnetic energy from the density
  field; at $z=2$ and $h_{\min}=20$ pc the measured magnetic energy exceeds
  it about 20-fold in the weak-feedback quasi-Lagrangian run and almost
  $10^3$-fold in the quasi-Eulerian run, so the extra growth is "produced
  through stretching of magnetic field lines" (§4); at the coarsest
  resolutions the field falls below the compression estimate.
- Liu et al. (2022, §5.1.1) find that the halo field, carried there by
  outflows, follows the compression scaling normalized to the equipartition
  field of the dense interstellar medium.
- Seta & Federrath (2022, §3.1, Fig. 5) find that the field–density
  relation follows none of the simple compression laws
  ($|\boldsymbol B|\propto\rho^0,\rho^{1/2},\rho^{2/3},\rho$), with fitted
  slopes between $\rho^{0.22}$ and $\rho^{0.71}$ and a large spread: "the
  magnetic field strength is not only controlled by the density".

## Growth-rate decomposition and bulk viscosity in a trans-sonic dynamo

[Beattie et al. (2025)](/sources/beattie-2025.md) (read in arXiv v4) run
the dynamo in forced, isothermal, visco-resistive MHD at $M_t\approx0.90$–$0.96$
(kinematic stage) with a modified FLASH finite-volume code, $Re=Rm=1000$,
$Pm=1$, Ornstein–Uhlenbeck forcing at $\ell_0=L/2$ with a 2:1
solenoidal-to-compressive energy ratio, a seed magnetic energy of
$10^{-10}\rho_0c_s^2$ ($\rho_0$ the mean density), grids $128^3$–$1024^3$, and an explicit
[bulk viscosity](/definitions/bulk-viscosity.md) with
$P_\nu=\nu/\nu_b\in\{\infty,1,0.1,0.01,0.001\}$ (§4, Table 1). Their
Reynolds numbers are real-space, $u_{\mathrm{rms}}\ell_0/\nu$ (footnote 3).

**Decomposition of the growth rate** (§3.2, Eqs. 33–40, App. C). From the
induction equation with uniform resistivity in a periodic box,
$d\langle B^2\rangle/dt=2\gamma_B\langle B^2\rangle-2\eta_m\langle\partial_jB_i\partial_jB_i\rangle$,
with

$$\gamma_B=\underbrace{\frac{\langle B_iB_jS^d_{ij}\rangle}{\langle B^2\rangle}}_{\text{stretching}}+\underbrace{\frac{\langle B_iB_j\Omega_{ij}\rangle}{\langle B^2\rangle}}_{\text{winding}}-\underbrace{\frac{\langle B^2\,\nabla\cdot\boldsymbol u\rangle}{6\langle B^2\rangle}}_{\text{compression}},$$

the velocity-gradient tensor being split orthogonally into expansion
$\tfrac13(\nabla\cdot\boldsymbol u)\delta_{ij}$, deviatoric strain $S^d_{ij}$
and rotation $\Omega_{ij}$. The winding term vanishes identically because
$B_iB_j$ is symmetric and $\Omega_{ij}$ antisymmetric (Eq. 39), and the
simulations confirm it. The factor $\tfrac16$ comes from the
$-\tfrac12B^2\nabla\cdot\boldsymbol u$ of the induction equation and the
$+\tfrac13B^2\nabla\cdot\boldsymbol u$ of the expansion part; the identity
$B_i\,[\nabla\times(\boldsymbol u\times\boldsymbol B)]_i=B_iB_j\partial_ju_i-\tfrac12B^2\nabla\cdot\boldsymbol u-\tfrac12\nabla\cdot(\boldsymbol uB^2)$
(their Eqs. C7–C8, with $\nabla\cdot\boldsymbol B=0$) reproduces it *(compiler
check, not in the sources)*. Compressions ($\nabla\cdot\boldsymbol u<0$) raise
the local growth rate by $\tfrac16|\nabla\cdot\boldsymbol u|$, rarefactions
lower it by as much; for compression along the field the compression term
cancels the stretching contribution (§3.2, footnote 6). The saturation
balance of stretching plus compression against Ohmic dissipation (Eq. 42)
is, the authors state, the one Yousef et al. (2007) derived for
incompressible turbulence.

**Results** (§5–§8, Table 1, Figs. 5–13):

| $P_\nu$ | grid | $\Gamma_E$ [$t_0^{-1}$] | $R_{\mathrm{sat}}$ |
|---|---|---|---|
| $\infty$ | $512^3$ | $1.48\pm0.03$ | $0.17\pm0.03$ |
| 1 | $1024^3$ | $1.42\pm0.01$ | $0.15\pm0.04$ |
| 1 | $512^3$ | $1.42\pm0.02$ | $0.14\pm0.03$ |
| 0.1 | $512^3$ | $1.47\pm0.05$ | $0.20\pm0.03$ |
| 0.01 | $256^3$ | $1.46\pm0.03$ | $0.19\pm0.07$ |
| 0.001 | $256^3$ | $1.28\pm0.02$ | not run to saturation |

- **Integral quantities barely depend on $\nu_b$.** The saturated ratio
  $\approx0.15$ (Alfvén Mach number $\approx2.5$) is consistent within
  $1\sigma$ with the Stokes-hypothesis results of Federrath et al. (2011),
  which the authors cite; the growth rate drops only when the bulk-viscous decay time
  reaches $t_0$ (§5.1–5.2). The solenoidal modes saturate at
  $\langle E_{\mathrm{mag}}\rangle/\langle E_{\mathrm s}\rangle\approx0.1$ for
  every $P_\nu$, the compressive ones at ratios between 1 and 10 (Fig. 6).
- **Stretching dominates**, in the kinematic and the saturated stage, even in
  this compressible dynamo; it grows the field "for all quantiles above the
  16th percentile", and its median moves towards zero by a factor of about
  two at saturation, as, according to the authors, Sur & Subramanian
  (2023) found at Mach 3 (§5.2, Figs. 7–8).
- **Compression plays a "dual role"**: its term is nearly symmetric about
  zero, growing and decaying the field in about equal amounts at
  $M_t\approx1$; lowering $P_\nu$ narrows its fluctuations while keeping its
  mean near zero, which the authors call "a key result" (§5.2).
- **A larger-scale field.** Low $P_\nu$ suppresses high-wavenumber modes and
  makes the field larger-scale in both stages; the saturated correlation
  wavenumber settles at $k_{\mathrm{cor}}\ell_0\approx2.5$ ($k_{\mathrm{cor}}$
  page-local). The mechanism offered, that the bulk dissipation wavenumber
  "drags" the shear one, and with it the resistive one through
  $\ell_\nu/\ell_\eta\sim Pm^{1/2}$, is a hypothesis (§7, Eq. 58,
  Figs. 10–12).
- **Spectral ratios.** In the kinematic stage
  $E_B(k)\sim k^2E_{\mathrm s}(k)$ up to the ratio peak, flattening to
  about $kE_{\mathrm s}(k)$ at saturation, with the equipartition wavenumber
  moving from about 100 to about 10 at $P_\nu=\infty$ (§8, Fig. 13).
- **Resolution.** Growth rates and integral statistics converge by $256^3$
  (App. D). The compressive-mode spectra and the claim that dynamo
  simulations without bulk viscosity are implicit LES for those modes are on
  [bulk viscosity](/definitions/bulk-viscosity.md) and
  [compressible MHD turbulence](/results/compressible-mhd-turbulence.md).

The authors read the dominance of stretching as the reason why
$\ell_\nu/\ell_\eta\sim Pm^{1/2}$ also holds in compressible flow, citing
Kriel et al. (2025) (§9.2). They state (footnote 4) that the growth-rate
decompositions of Seta & Federrath (2021) and Sur & Subramanian (2023)
neglected the expansion part of the velocity gradient and overestimated the
effect of compression by factors of 3 and 6; those works are not ingested,
and the vorticity-budget analysis of the ingested
[Seta & Federrath (2022)](/sources/seta-2022.md) above is a different
decomposition.

Seta & Federrath (2022) and Beattie et al. (2025) both give $\Gamma_E$ in
units of a driving-scale time, but with different time units, Reynolds-number
definitions, driving and thermodynamics; their rates are not compared by
either source.

## Spectral signatures

Martin-Alvarez et al. (2022, §3.3.5) recall the Kazantsev (1968) magnetic
spectrum $E_B(k)\propto k^{3/2}$ of the kinematic dynamo driven by
Kolmogorov turbulence, with amplification below the viscous and above the
resistive scale; Seta & Federrath (2022, §2.5) use the same $k^{3/2}$ form
for their seed. Martin-Alvarez et al. observe what they call an "inverse
cascade", the migration of the magnetic-spectrum peak to larger scales with
time: at $z=2$ the peak lies slightly below the disc thickness for
$h_{\min}\le80$ pc, more prominently with quasi-Eulerian refinement, and in
the quasi-Eulerian 20 pc run the magnetic power at kpc scales grows by more
than 6 dex between $z=12$ and $z=2$ (Figs. 12–14). The quasi-Lagrangian runs
show bumps in the spectra at the transitions between refinement levels
(Fig. 13). They add that zero-padding of the FFT box changes the
large-scale shape and can mask the peak migration (App. B).

## Qualifications

- **Printed sign, §13.3.4, p. 111 of arXiv v3** (checked on the rendered
  page). The text reports Galishnikova et al. (2022) as supporting "the
  $\lambda_R\propto\mathrm{Rm}^{1/3}$ scaling of the field-reversal scale",
  and footnote 79 gives their version as
  "$\lambda_R\propto\mathrm{Rm}^{3/10}\mathrm{Pm}^{1/5}$", both with positive
  exponents; Eq. (13.9), p. 109, prints
  $\lambda_R\sim L\,Rm_L^{-1/3}(1+Pm)^{-1/6}$, a scale that decreases with
  $Rm$. The review does not say why the signs differ. Footnote 79 adds that
  Galishnikova et al. compare with tearing of a sinusoidal profile ($n=2$ in
  App. D.1.5) rather than the Harris-like $n=1$ of the main text.
  *(Compiler check, not in the sources: repeating the balance of Eq. 13.7,
  $\gamma_{\mathrm t}\sim\delta u_L/L$ with $b_\lambda\sim\delta u_L$, with the
  general-$n$ growth rate of Eq. D40 at $n=2$,
  $\gamma_{\mathrm t}\lambda/b_\lambda\sim S_{L,\lambda}^{-3/7}(1+Pm)^{-2/7}$,
  gives $\lambda_R\sim L\,Rm_L^{-3/10}(1+Pm)^{-1/5}$: the magnitudes of the
  footnote's exponents with negative signs, as in Eq. 13.9.)*
- The review records the competing view (Haugen et al. 2003, 2004; Beresnyak
  2012; Xu & Lazarian 2016, as recalled) that the saturated state is
  non-asymptotic and would become Kolmogorov-like with scale-by-scale
  equipartition at higher resolution (§13.2); Grete et al. (2021) and Bian &
  Aluie (2019) disagree on magnetic control of the small-scale cascade, as
  recalled. These are disagreements among un-ingested works reported by the
  review, not a bundle contradiction.
- The theory revises the author's earlier result (Schekochihin et al. 2002,
  2004) that the reversal scale is resistive, $L\,Rm^{-1/2}$.
- **Regime of the simulations.** The four simulation sources run
  compressible MHD at $Re=Rm=2000$, $Pm=1$ (Seta & Federrath 2022), or
  ideal MHD with numerical dissipation and an estimated numerical $Pm\sim2$
  (Martin-Alvarez et al. 2022); the galaxy runs stay kinematic or saturate
  through a tuned subgrid model (Liu et al. 2022); Beattie et al. (2025) run
  isothermal MHD at $Re=Rm=1000$, $Pm=1$, $M_t\approx1$. None addresses fold
  tearing or the $Rm$ scaling of the saturated reversal scale, so they
  neither support nor contradict the tearing-limited theory above.
- **Printed slips, Beattie et al. (2025).** §5.2 reads a growth rate
  $\Gamma_E t_0\approx1.4$ as an e-folding "every $1.4t_0$"; the magnetic
  energy then e-folds every $t_0/1.4\approx0.71t_0$ *(compiler check, not in
  the sources)*. §5.2 also says the growth rate is "significantly affected"
  for $P_\nu\le0.01$, while Table 1 gives $1.46\pm0.03$ at $P_\nu=0.01$,
  within the range of the larger $P_\nu$; only $P_\nu=0.001$ is clearly
  lower. §4.2 gives a 2:1 solenoidal-to-compressive forcing energy, §5.1
  "the same amount of energy". §7 writes the kinematic-stage field as
  small-scale with $k_{\mathrm{cor}}\ell_0<1$, the Fig. 11 caption with
  $k_{\mathrm{cor}}\ell_0>1$.
- **Printed exponents, Martin-Alvarez et al. (2022, §3.2, pp. 3334–3335).** The
  text pairs $Re\propto\Delta x_{\max}^{-4/3}$ (ideal Kolmogorov, Kritsuk et
  al. 2011) and $Re\propto\Delta x_{\max}^{-1/3}$ (linear scaling of the
  viscosity with resolution) with "$\Gamma_\varepsilon\propto\Delta
  x_{\max}^{-2/3}$ and $\Gamma_\varepsilon\propto\Delta x_{\max}^{-1/3}$,
  respectively". *(Compiler check, not in the sources: with
  $\Gamma_E\propto Re^{1/2}$ the first pairing gives $h_{\min}^{-2/3}$ as
  printed, the second gives $h_{\min}^{-1/6}$, not $h_{\min}^{-1/3}$; and the
  fiducial $\Gamma_E\propto Re^{1/2}\propto h_{\min}^{-1/2}$ with
  $\nu\propto h_{\min}$ implies $Re\propto h_{\min}^{-1}$, not
  $h_{\min}^{-1/3}$.)* The measured scalings above do not depend on this
  sentence.
- **Sign of the compression term, Seta & Federrath (2022, §4.2, Fig. 11,
  Table 3).** The paper states that the sign of each projected term
  indicates growth (positive) or decay (negative), and then that the
  compression term, "though it is negative", amplifies vorticity in the cold
  phase. Eq. (10) prints $\nabla\times(\boldsymbol u\times\boldsymbol\omega)=
  (\boldsymbol\omega\cdot\nabla)\boldsymbol u-(\boldsymbol u\cdot\nabla)\boldsymbol\omega-\boldsymbol\omega(\nabla\cdot\boldsymbol u)$
  with the labels under the unsigned terms, and does not say which sign the
  plotted compression term carries. *(Compiler check, not in the sources:
  $\boldsymbol\omega\cdot[-\boldsymbol\omega(\nabla\cdot\boldsymbol u)]=-|\boldsymbol\omega|^2\nabla\cdot\boldsymbol u$
  is negative where the flow expands, i.e. where it reduces $|\boldsymbol\omega|$;
  the stated interpretation holds only if the plotted quantity is
  $+\boldsymbol\omega(\nabla\cdot\boldsymbol u)$. Also, the printed parts do
  not add up to the whole: for solenoidal forcing, cold phase, kinematic
  stage, Table 3 gives stretching, advection and compression
  $0.08$, $-0.07$, $-0.42$, while Table 2 gives the turbulent term $1.9$
  (units $10^{-27}$ s$^{-2}$); no sign combination of the three reproduces
  it.)* The paper does not explain either point; the stretching-versus-compression
  attribution above is the authors'.

# Citations

- [Schekochihin (2022)](/sources/schekochihin-2022.md) — §13 (Eqs. 13.2–13.35): §13.1, §13.2, §13.3.1–§13.3.4, §13.4.1–§13.4.8; footnotes 74, 79.
- [Seta & Federrath (2022)](/sources/seta-2022.md) — §2.3–§2.5; §3.1, Figs. 5–6; §3.2; §4.1, Table 1; §4.2, Eqs. (9)–(10), Figs. 9–12, Tables 2–3; §5; App. C.
- [Martin-Alvarez et al. (2022)](/sources/martinalvarez-2022.md) — §1; §2; §3.1–§3.2, Figs. 6–7; §3.3.1, Eq. (5), Fig. 8; §3.3.4; §3.3.5, Figs. 12–14; §4; App. B.
- [Liu et al. (2022)](/sources/liu-2022.md) — §1; §5.1.1; (subgrid model: §2.2, Eq. 14).
- [Beattie et al. (2025)](/sources/beattie-2025.md) — §1, Eqs. (1)–(3), footnotes 3–4, 6; §3.2, Eqs. (33)–(42); §4, Table 1; §5.1–5.2, Figs. 5–8; §7, Eq. (58), Figs. 10–12; §8, Fig. 13; §9.2; App. C, Eqs. (C1)–(C16); App. D.
