---
type: Source
title: "De Vanna et al. (2022) — Wall-modeled LES of shock-wave/boundary layer interaction"
description: "Assesses a wall-modelled LES that keeps the no-slip condition and imposes the equilibrium-wall-model stress through an effective wall viscosity, reverting to wall-resolved LES where the grid resolves the wall, on an oblique shock/boundary-layer interaction at Mach 2.28; separation is captured but the bubble is oversized."
resource: "doi:10.1016/j.ijheatfluidflow.2022.109071"
source_kind: paper
authors: [De Vanna F., Bernardini M., Picano F., Benini E.]
year: 2022
venue: "Int. J. Heat Fluid Flow 98:109071"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_International_Journal_of_Heat_and_Fluid_Flow_De_Wall-modeled_LES_of_shock-waveboundary_layer_interaction.pdf"
tags: [wmles, shock-boundary-layer-interaction, compressible, wall-model, les]
timestamp: 2026-10-29T07:37:00Z
---

# Summary

De Vanna et al. (2022) assess, in a flow out of equilibrium, the
[wall-modelled LES](/methods/wall-modelled-les.md) strategy the group
introduced in De Vanna et al. (2021b): the oblique
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
at $M_\infty=2.28$, shock-generator deflection $8°$, inflow $Re_\tau=700$
($Re_\theta\approx5000$), the IUSTI experiment of Dupont et al. An
[equilibrium wall model](/methods/equilibrium-wall-model.md) (ODEs for the
wall-parallel velocity and temperature, mixing-length eddy viscosity with
van Driest damping in [semi-local scaling](/definitions/compressible-velocity-transformation.md))
is coupled to the LES without replacing the no-slip and thermal wall
conditions: the modelled wall stress and heat flux are imposed by adding a
wall subgrid contribution to the wall viscosity and conductivity. A
resolution detector compares the wall spacings in inner units, computed
from the resolved wall stress, with thresholds; where the wall is
resolved the wall model is off and the method reverts to wall-resolved
LES. The exchange point is chosen dynamically.

The solver (URANOS, finite differences) hybridizes a sixth-order
[kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
split convective scheme with fifth-order WENO-Z
([WENO](/methods/weno-scheme.md)) through a modified Ducros
[shock sensor](/definitions/shock-sensor.md), and closes the
[LES](/definitions/large-eddy-simulation.md) with the
[WALE model](/methods/wale-model.md); the inflow is a digital filter
([inflow generation](/methods/inflow-turbulence-generation.md)). The
[grid-point cost](/results/les-grid-point-requirements.md) of
wall-resolved LES motivates the approach, and the authors judge
[non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)
complex and "frequently invasive at the implementation level" (§1). Three wall-modelled grids are compared with a
wall-resolved LES, DNS of the incoming [boundary layer](/benchmarks/turbulent-boundary-layer.md)
and PIV. Because no-slip is kept, the wall-modelled runs show negative
friction in the separated region; but the bubble is oversized, which the
authors attribute to the wall model and to the subgrid and shock-capturing
[numerical dissipation](/properties/numerical-dissipation.md) that
"laminarize" it at low resolution. Once rescaled by the interaction
length, bubble shape and second-order statistics agree with PIV.
Evidence is numerical, one configuration on three grids.

# Version read

Version of record (Elsevier; received 18 July 2022, accepted 17 October
2022), 13 pages, all read (pp. 2–8 also visually). Page 1 matches the
metadata; no identity issue. Equation and figure numbers are those of
this version.

# Key claims

Page-local symbols: $\mu^w_{\mathrm{sgs}}$, $\lambda^w_{\mathrm{sgs}}$ the
wall subgrid viscosity and conductivity (registry §11); $\mu_{\mathrm{eff}}$,
$\lambda_{\mathrm{eff}}$ the effective wall viscosity and conductivity;
$\lambda_{\mathrm{th}}$ the thermal conductivity; $\theta_{\mathrm{WM}}$
the wall-model activation flag (1 modelled, 0 resolved);
$\mu_r=|\tau_w^{\mathrm{WM}}/\tau_w^{\mathrm{WR}}|$ the effective viscosity
ratio; $\theta_{\mathrm D}$ the modified Ducros sensor; $L_{\mathrm{int}}$
the interaction length (registry §11; nominal impingement to reflected-shock foot);
$x^*=(x-x_{\mathrm{sh}})/\delta_r$ with $\delta_r$ the inflow 99%
thickness; WMLES and WRLES wall-modelled and wall-resolved LES.

1. The wall-resolved LES point count scales as $N_{\mathrm{WR}}\sim Re_L^{13/7}$ (citing Choi & Moin 2012), "mostly quadratically", which motivates WMLES (§1). **Stated**
2. Most wall models assume equilibrium, "the instantaneous balance between nonlinear convective terms and the pressure gradient", which makes separated or incipiently separated flows challenging; "non-equilibrium wall-modeling in a LES framework is still an open problem" (§1). **Stated**
3. The WMLES blends wall-resolved and wall-modelled approaches by setting the wall viscosity to $\mu_w+\mu^w_{\mathrm{sgs}}$ and the wall conductivity to $\lambda_{\mathrm{th},w}+\lambda^w_{\mathrm{sgs}}$, so that $\tau_w^{\mathrm{LES}}=\mu_{\mathrm{eff}}\,\partial u_\parallel/\partial y$ and $q_w^{\mathrm{LES}}=\lambda_{\mathrm{eff}}\,\partial T/\partial y$ reproduce the wall-model stress and heat flux with the resolved gradients, while no-slip, no-penetration and isothermal or adiabatic conditions remain active (§2.2, Eqs 7a–b; method of De Vanna et al. 2021b). **Derived**
4. When the wall is resolved, $\mu_{\mathrm{eff}}\to\mu_w$ and $\lambda_{\mathrm{eff}}\to\lambda_{\mathrm{th},w}$, so $\mu^w_{\mathrm{sgs}}=\lambda^w_{\mathrm{sgs}}=0$ and the method "falls back to a standard WRLES" (§2.2). **Derived**
5. The wall model is switched on only where at least one of $\Delta x^+<40$, $\Delta y^+_w<3$, $\Delta z^+<15$ fails, the inner units being those of the resolved wall stress; thresholds from Piomelli (2008) and Georgiadis et al. (2010) (§3.2, Eq. 9). **Stated** (design choice)
6. The LES/wall-model exchange point is computed dynamically from the local wall resolution, always "sufficiently far from the wall and in an adequately resolved flow zone", which improves the wall-model inputs, "particularly when adequately resolved parts of the wall are encountered, or the shear stress approaches zero" (§3.2; details in De Vanna et al. 2021b). **Stated**
7. Convective terms: the sixth-order energy-preserving split scheme of Pirozzoli (2010) in smooth regions, fifth-order WENO-Z (Castro et al. 2011) near shocks, switched by a modified Ducros sensor (Eq. 8) with threshold 0.1, WENO being used in the flagged cell and its neighbours (§3.1.1–3.1.2). **Stated**
8. Viscous terms are discretized semi-conservatively with sixth-order formulae, equal to central differences for uniform properties and giving "strong preservation and proper telescoping" for variable viscosity (§3.1.3, from De Vanna et al. 2021a). **Stated**
9. Time integration: low-storage TVD Runge–Kutta (Gottlieb & Shu 1998) with the step set by CFL 0.5 and Fourier number 0.1, the smaller step taken (§3.1.4). **Stated**
10. Incoming boundary layer ($x^*=-14$, $Re_\tau=840$): the WMLES $C_f$ matches WRLES "mostly regardless of the resolution", with "just a slight underestimation"; the WMLES mean velocity agrees with experiment and DNS and in the resolved region shows "a higher level of accuracy even than the wall-resolved arrangement", which overstates the log-region profile (§4.3, Fig. 3). **Shown**
11. WRLES velocity fluctuations agree with experiment and DNS (the $u_{\mathrm{rms}}$ peak slightly overestimated, the others underestimated); the WMLES fluctuation peaks lie in the modelled region and cannot be predicted; the WMLES $u_{\mathrm{rms}}$ is "quite well aligned with DNS", grid-independent, with mild near-wall overestimation; the other components are grid-sensitive and the medium grid fits DNS and WRLES best (§4.3, Figs 4c–d). **Shown**
12. The medium-beats-fine result is attributed to the grid moving the dynamic interface ("not always optimized") and to the nonlinear interaction of WENO numerical viscosity with the wall model; further analysis is deferred to De Vanna et al. (2022, Comput. Fluids) (§4.3). **Stated**
13. Streamwise $C_f$ and $C_p$: WMLES describes friction and pressure well outside the recirculation with mild grid dependence; in the bubble WRLES predicts "an important separation while a gentle reverse flow is found in wall-modeled computations" (§4.4, Fig. 5a). **Shown**
14. WMLES "properly detects the partial flow separation with negative friction values", attributed to keeping no-slip and regulating the local wall subgrid contribution, a feature "mainly ruled out in classical equilibrium wall-modeling formulations" (§1, §4.4, §5). **Shown**
15. WMLES spreads the pressure rise over a broader region than WRLES, consistent with the larger bubble; the fine WMLES $C_p$ is reasonably accurate (§4.4, Fig. 5b). **Shown**
16. The effective viscosity ratio $\mu_r$ (Eq. 12; one for a fully resolved wall) decreases with grid refinement; it decreases along the incoming boundary layer ($x^*<-10$), peaks in the bubble region $x^*\in[-10,5]$ (augmented subgrid stress, near-zero resolved wall stress) and grows in the recovery ($x^*>5$) (§4.4, Fig. 6a). **Shown**
17. The ensemble average of $\theta_{\mathrm{WM}}$ exceeds 0.95 in the incoming and outgoing boundary layers and drops to about 0.65 in the bubble: the recirculation, with small wall gradients, is more often treated as wall-resolved (§4.4, Fig. 6b). **Shown**
18. WMLES predicts a wider bubble that collapses towards WRLES with refinement; the oversizing is attributed to the wall model and to subgrid plus shock-capturing artificial viscosity that "tends to laminarize the bubble, increasing its size" at low resolution (§4.5, Fig. 7). **Shown** (attribution **Stated**)
19. WMLES captures the velocity spike at the top of the recirculation; the reflected-shock fluctuations are "decidedly less marked" than in WRLES, attributed to artificial viscosity smearing the shocks (§4.5, Fig. 7). **Shown**
20. Away from the wall the WMLES mean velocity profiles collapse on WRLES (bubble thickness adequately predicted); near the wall they agree less, connected with the overestimated $C_f$ in the bubble and its streamwise misalignment (§4.5, Fig. 8). **Shown**
21. Interaction length: $L_{\mathrm{int}}/\delta_r\sim\{7.0,5.2,5.0\}$ for the coarse, medium and fine WMLES, 3.3 for WRLES, 4.18 in the experiment (§4.6). **Shown**
22. With coordinates scaled by $L_{\mathrm{int}}$, the fine WMLES mean $u$ fits the PIV bubble shape and peak location; the mean $v$ peaks are slightly shifted in WMLES while WRLES "perfectly overlap PIV"; $v_{\mathrm{rms}}$ and the shear-stress component are "impressively accurate in shape", reproducing the turbulence amplification of vortex shedding in the separation-shock shear layer (§4.6, Figs 9–13). **Shown**
23. Recovery boundary layer ($x^*=11$): the WMLES mean profiles are consistent with WRLES; all fluctuation components are overestimated relative to WRLES, attributed to more intense low-frequency fluctuations; the overestimate drops markedly from coarse to medium, medium ≈ fine (§4.7, Figs 14–15). **Shown**
24. The bubble is "systematically overestimated in size but consistently described in shape and morphology"; the method can be used at high Reynolds number "in both equilibrium and incipient separated configurations"; future work: non-equilibrium improvements and coupling with a sharp-interface immersed boundary method (§5). **Stated**

# Printed slips

- **Eq. (1b):** the pressure term is printed $-\partial\bar p_i\delta_{ij}/\partial x_j$, with a spurious index on $\bar p$.
- **§4.2:** "compared to the wall-resolved setup (Fig. 2(c))"; the wall-resolved panel is Fig. 2(d) ("(d) WRLES").
- **§3.1.2:** "employed in the actual cell and all three surrenders".
- **§4.3, Fig. 3:** the streamwise mean-velocity profiles are called "wall-normal velocity profiles".
- **Symbols:** $\mu^w_{tot}$, $\lambda^w_{tot}$ (§2.2 text) and $\mu_{eff}$, $\lambda_{eff}$ (Eq. 7) for the same quantities; $y^*$ is the semi-local wall distance in §2.2 and $y/\delta$ in §4.3.
- **Typos:** "strongly under-predict" (§1), "blu tones" (§4.1), "dumping function" (§2.2).
- **Reference list:** Balin et al. (2020), "p. 3012", is printed with DOI 10.2514/6.2020-3002, the DOI also printed for Goc et al. (2020), "p. 3002"; Suga et al. (2019) is printed without a volume.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar\phi$, $\tilde\phi$, $\phi''$ | $\bar\phi$, $\tilde\phi$, $\phi''$ | filter, Favre filter; the statistics of §4 are averages, written $\langle\cdot\rangle$ on concept pages |
| $T^{SGS}_{ij}=\overline{\rho u_iu_j}-\bar\rho\tilde u_i\tilde u_j$ | $\tau_{ij}$ (compressible form) | positive convention; isotropic part neglected |
| $\mu_{SGS}$ | $\mu_t$ | WALE subgrid viscosity |
| $C_w=0.325$, $S^d_{ij}$ (WALE) | $C_w$, $\mathcal S_{ij}$ (page-local, as on the [WALE](/methods/wale-model.md) page) | **collision:** the WALE $S^d_{ij}$ is not the registry's deviatoric strain |
| $\Delta=(\Delta x_1\Delta x_2\Delta x_3)^{1/3}$ | $\Delta$ | |
| $\bar\tau_{ij}$ | $\sigma_{ij}$ | filtered viscous stress; **collision** with the SGS stress |
| $\tilde g_{ij}$, $\tilde S_{ij}$ | $\partial_j\tilde u_i$, $\tilde S_{ij}$ | |
| $\lambda$, $\lambda_{SGS}$, $\lambda_w$ | $\lambda_{\mathrm{th}}$, $\lambda_{\mathrm{th},t}$, $\lambda_{\mathrm{th},w}$ (page-local) | **collision** with the Taylor microscale |
| $\mu^w_{SGS}$, $\lambda^w_{SGS}$, $\mu_{eff}$, $\lambda_{eff}$ | $\mu^w_{\mathrm{sgs}}$, $\lambda^w_{\mathrm{sgs}}$ (registry §11), $\mu_{\mathrm{eff}}$, $\lambda_{\mathrm{eff}}$ (page-local) | |
| $h_{wall}$ | $h_{\mathrm{wm}}$ | dynamic matching height |
| $u_{/\!/LES}$ | $U_{\mathrm{LES}}$ | |
| $\mu_{t,wm}=\kappa\rho_{wm}u_\tau yD$, $A^+=17$, $\kappa=0.41$ | (wall-model eddy viscosity), $A^+$, $\kappa$ | |
| $y^*$ (§2.2) | $y^*$ | semi-local wall distance |
| $\theta$, $\bar\theta=0.1$, $\varepsilon=(u_\infty/\delta_0)^2$ | $\theta_{\mathrm D}$, (threshold), $\epsilon_{\mathrm D}$ (page-local) | **collision:** $\varepsilon$ is not the dissipation rate |
| $\theta_{WM}$, $\mu^{SGS}_r$ | $\theta_{\mathrm{WM}}$, $\mu_r$ (page-local) | |
| $\delta_0$, $Re_{\tau,0}$ | $\delta_r$, $Re_\tau$ at the inflow | |
| $l^*$ | $L_{\mathrm{int}}$ (registry §11) | not the scaled $L_{\mathrm{sc}}$ of the registry |
| $\phi=8°$ | (shock-generator deflection) | |
| $c_f$, $c_p$ | $C_f$, $C_p$ | **collision:** $c_p$ is also the specific heat |
| $\Delta x^+_w$, $\Delta y^+_w$, $\Delta z^+_w$ | $\Delta x^+$, $\Delta y^+$, $\Delta z^+$ | from the resolved wall stress |

# Reference list

53 printed references, author-year (Elsevier Harvard), alphabetical. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. The four De Vanna et al. 2021 works (a–d) are matched
to existing entries by identity, not by printed suffix; the cited De Vanna
et al. (2022), Comput. Fluids, is a different work from this source and is
keyed `devanna-2022-b`. The ingested Sources [bose-2018](/sources/bose-2018.md)
and [lozanoduran-2022](/sources/lozanoduran-2022.md) are the same works as
the entries cited. Incomplete items: Cheng et al. 2022, Mettu &
Subbareddy 2022 and De Vanna et al. 2022 (no pages or volume), Suga et
al. 2019 (no volume), De Vanna et al. 2021c (no title); the Balin et al.
2020 DOI is withheld (see Printed slips). No printed duplicate.

# Pages created or updated

Chunk 10 (2026-10-27). This source is cited on:

- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)
- [Slip-wall models](/methods/slip-wall-model.md)
- [WALE model](/methods/wale-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
