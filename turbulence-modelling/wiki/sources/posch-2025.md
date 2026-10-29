---
type: Source
title: "Posch et al. (2025) — Turbulent combustion modeling for internal combustion engine CFD: A review"
description: "Reviews turbulent combustion models for RANS and LES of internal combustion engines (regime diagrams, eddy break-up and partially stirred reactor, coherent flame, G-equation, thickened flame, PDF methods, conditional moment closure, flamelet and FGM tables), tabulates their engine applications and assesses calibration, turbulence–chemistry interaction, future fuels and machine learning."
resource: "doi:10.1016/j.pecs.2024.101200"
source_kind: paper
authors: [Posch S., Gößnitzer C., Lang M., Novella R., Steiner H., Wimmer A.]
year: 2025
venue: "Prog. Energy Combust. Sci. 106:101200"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Progress_in_Energy_and_Combustion_Science_Posch_Turbulent_combustion_modeling_for_internal_combustion_engine.pdf"
tags: [combustion, review, rans, les, tabulated-chemistry, data-driven]
timestamp: 2026-10-29T05:13:00Z
---

# Summary

Posch et al. (2025) review the turbulent combustion models used in
three-dimensional CFD of internal combustion engines. After a
classification of engine concepts by ignition mode (homogeneous and
direct-injection spark ignition, prechamber jet ignition, diesel
compression ignition, low-temperature and dual-fuel concepts), they state
the reacting-flow equations and summarise the turbulence treatment:
[DNS](/definitions/direct-numerical-simulation.md) cost and its few engine
uses, RANS with Favre averaging, the
[Boussinesq closure](/definitions/boussinesq-hypothesis.md) and turbulent
Schmidt and [Prandtl numbers](/definitions/turbulent-prandtl-number.md),
and [LES](/definitions/large-eddy-simulation.md) with implicit filtering by
finite-volume averaging, Favre filtering, the
[Smagorinsky](/methods/smagorinsky-model.md) and dynamic structure
([one-equation](/methods/subgrid-kinetic-energy-equation-model.md)) models,
and commutation errors of the moving engine mesh. The Borghi–Peters premixed
and the Peters non-premixed regime diagrams follow.

The model section states eddy break-up, eddy dissipation and
partially-stirred-reactor closures, the coherent flame model and its ECFM
and ECFM3Z forms, the G-equation, the
[thickened flame model](/methods/thickened-flame-model.md) with its
dynamic sensor, presumed and transported PDF methods,
[conditional moment closure](/methods/conditional-moment-closure.md)
(with the [CSE](/methods/conditional-source-term-estimation.md) variant of
a cited LES), and [flamelet-based tables](/methods/flamelet-tabulated-chemistry.md)
(steady flamelets, FGM, ILDM, flamelet/progress variable, interactive
flamelets). Ten tables list engine applications by model. Recurring
judgements: tuned model constants compromise predictive capability;
direct chemistry integration (SAGE, multi-zone, with
[mesh adaptation](/methods/mesh-adaptation.md)) neglects
turbulence–chemistry interaction; a general justification for neglecting
that interaction in compression-ignition engines cannot be derived; models
built on unity Lewis number miss the differential diffusion of hydrogen.
The outlook covers a validation pyramid from engine to DNS that combines
[a priori and a posteriori](/definitions/a-priori-and-a-posteriori-testing.md)
evaluation, future fuels, early-flame and multi-regime models, and machine
learning for chemistry (including
[physics-informed networks](/methods/physics-informed-neural-network.md)
for kinetics) and for subgrid closures
([CNN closures](/methods/neural-network-sgs-model.md),
[GAN super-resolution](/methods/super-resolution-sgs-model.md)), which so
far are tested on benchmark flames only. No new model or computation is
presented.

# Version read

Version of record (Elsevier, open access CC BY; received 8 March 2022,
revised 18 October 2024, accepted 21 October 2024, online 6 November 2024),
48 pages (text pp. 1–38, references and biographies pp. 39–48), all read.
Page 1 matches the Crossref metadata; no identity issue. Equation, table,
figure and section numbers are those of this version.

# Key claims

Page-local symbols: $Re_{\mathrm t}=u'L/\nu$ the turbulence Reynolds
number; $Da$ the Damköhler number; $Ka=(\delta_{\mathrm L}/\eta)^2$ and
$Ka_\delta=(\delta_{\mathrm r}/\eta)^2$ the Karlovitz numbers on the laminar
flame thickness $\delta_{\mathrm L}$ and reaction-zone thickness
$\delta_{\mathrm r}$; $s_{\mathrm L}$, $s_{\mathrm T}$ the laminar and
turbulent flame speeds; $Z$ the mixture fraction, $\xi$ its sample-space
value, $\chi$ the scalar dissipation rate, $c$ the progress variable, $Y_k$
the species mass fractions, $\dot\omega_k$ their production rates;
$\Sigma_{\mathrm f}$, $\alpha_\Sigma$, $\beta_\Sigma$ the flame surface density and the strain
and consumption constants of the coherent flame model; $F$, $\Xi_\Delta$
the thickening factor and efficiency function of the thickened flame;
$\gamma^*_{\mathrm{PaSR}}$, $\tau_{\mathrm{ch}}$, $\tau_{\mathrm{mix}}$,
$C_{\mathrm{mix}}$ the reacting fraction, chemical and mixing times and
mixing constant of the partially stirred reactor; $Q_i(\xi)$ the
conditional Favre mean of CMC; $C_\Phi$ the mixing constant of transported
PDF methods.

1. Since combustion-model development is often driven by low-pressure applications such as turbomachinery, using combustion models "off the rack" for engine CFD "should be treated with caution" (§1). **Stated**
2. DNS cost scales as $Re^3$ operations, with a minimum of $Re^{11/4}$ (citing Pope); the engine DNS studies cited either do not resolve combustion or are two-dimensional with highly reduced mechanisms, raising a cost–benefit issue (§3.2.1). **Stated**
3. In engine LES the filter width varies in time with the moving mesh and non-uniform widths cause commutation errors; Moureau et al. conclude the time commutation error can be ignored when flow and mesh motion are induced by the same boundary movement, but such errors can occur with adaptive mesh refinement (§3.2.3). **Stated**
4. Engine LES typically uses implicit filtering through finite-volume averaging and "usually requires at least second order central schemes to avoid artificial dissipation" (§3.2.3). **Stated**
5. RANS yields an ensemble-averaged cycle that "does not need to correlate with a real single engine cycle"; LES gives single cycles and is the main tool for cycle-to-cycle variation, needing a number of cycles for statistics; RANS keeps a role for many-run co-optimisation (§3.2.3). **Stated**
6. The premixed regimes are bounded by $Re_{\mathrm t}=1$, $Ka=1$, $u'/s_{\mathrm L}=1$ and $Ka_\delta=1$, with $Re_{\mathrm t}=Da^2Ka^2$ (Eq. 16) and $Ka_\delta=(\delta_{\mathrm r}/\delta_{\mathrm L})^2Ka$ (Eq. 17); $\delta_{\mathrm r}/\delta_{\mathrm L}$ lies between 0.1 at atmospheric and 0.03 at higher pressure; $Ka_\delta=1$ corresponds to $Ka=100$ for $\delta_{\mathrm r}/\delta_{\mathrm L}=0.1$ (§3.3.1, Fig. 2). **Stated** *(compiler check, not in the sources: Eq. 17 gives $0.1^2\times100=1$)*
7. Regime diagrams assume homogeneous isotropic turbulence, which the engine flow is "far from", so they give only a "fairly rough distinction" (§3.3.2). **Stated**
8. Low-Damköhler cases are excluded because chemical times in most technical applications and engines are shorter than transport times (§3.3). **Stated**
9. Lipatnikov et al. conclude from DNS at various $Ka$ that the domain of flamelet validity is wider than initially assumed; van Oijen et al. give a strong-stretch theory in the FGM formalism; Kheirkhah and Gülder propose a revised regime diagram (§4.1). **Stated**
10. Eddy break-up, $\bar{\dot\omega}=C_{\mathrm{EBU}}\bar\rho(\varepsilon/k)\tilde c(1-\tilde c)$ (Eq. 27), overestimates the reaction rate where $\varepsilon/k$ is large and predicts a nonphysical burning velocity near walls (§4.2). **Stated**
11. The partially stirred reactor uses $\gamma^*_{\mathrm{PaSR}}=\tau_{\mathrm{ch}}/(\tau_{\mathrm{ch}}+\tau_{\mathrm{mix}})$ and $\tau_{\mathrm{mix}}=C_{\mathrm{mix}}k/\varepsilon$ with $C_{\mathrm{mix}}$ in 0.001–0.3 (Eqs. 29, 31); applications use $C_{\mathrm{mix}}=0.01$–0.1, 0.005 and 0.1 (§4.2, §5.1.1, §5.2.1, Table 8). **Stated**
12. In the coherent flame model $\beta_\Sigma$ is generally set to unity and $\alpha_\Sigma$ in the range of unity, and settings far from unity "may significantly deteriorate the predictions"; for hydrogen engines the ECFM strain constant had to be adjusted with the air–fuel ratio because differential diffusion is absent from its turbulent flame speed (§4.3, §5.1.2, §6.2.1). **Stated**
13. Thickened flame: on coarser grids where $F$ and $\Xi_\Delta$ both increase the diffusion number may exceed the Courant number and restrict the time step; thickened flames carry considerable unresolved content, so the model suits cases where emissions and strain effects are not essential; since it does not assume flamelets it "can be considered as a regime-independent combustion model for LES" (§4.5, §5.1.4). **Stated**
14. A $\beta$-function presumed PDF cannot represent the burned-mixture probability of the premixed case and is "not suitable" there (§4.6). **Stated**
15. CMC transports $Q_i(\xi)=\overline{\rho Y_i|Z=\xi}/\overline{\rho|Z=\xi}$ with conditional convection, conditional scalar dissipation and conditional reaction terms (Eq. 53); its cost scales with the number of species times the number of conditioning values; collapsing the azimuthal direction to a two-dimensional CMC grid in a three-dimensional case reproduced full three-dimensional results (§4.7, §5.2.3, Table 10). **Stated**
16. "Limitations and application failures hardly are ever published"; the application review therefore focuses on in-cylinder pressure and heat release, because emission levels "do not allow any useful validation" (§5). **Stated**
17. Direct chemistry integration is a clear trend in engine RANS, but computing chemical sources from averaged values "completely" neglects turbulence–chemistry interaction, a significant limitation for propagating spark-ignition flames; mechanism multipliers are more sensitive calibration handles than interaction-model parameters (§5.1.5, §5.3). **Stated**
18. Ravindran et al.: during cold start detailed chemistry with energy deposition underestimated flame propagation while the G-equation matched the pressure (§5.1.5). **Stated**
19. Between Kokjohn and Reitz (small-scale turbulence–chemistry interaction not dominant in low-temperature diesel combustion) and Kung and Haworth (interaction relevant), the authors conclude "a general justification to neglect TCI in CI engines cannot be derived" (§5.2.4). **Stated**
20. Xu et al.: five-dimensional FGM matched an optical engine while four-dimensional FGM predicted very late ignition; FGM beat PaSR with roughly 90% less computational time (§5.2.5). **Stated**
21. Transported PDF needs calibration of $C_\Phi$ (2.0 in two cited works) and its cost makes it "impractical for industrial applications" even for RANS (§5.2.2). **Stated**
22. Lean or diluted spark ignition and jet ignition raise $Ka$ and move combustion to non-flamelet regimes; tuning model constants "often compromises the fundamental accuracy and predictive capability" (§5.3, §6.3.2). **Stated**
23. Prediction of cycle-to-cycle variation needs ignition and early-flame models (§5.3, §6.3.1). **Stated**
24. For hydrogen, Berger et al. found the consumption speed and the turbulent flame speed increased by a factor of three by thermodiffusive instabilities; Aspden et al. and Howarth et al. show classical premixed regime diagrams are inadequate for thermodiffusively unstable flames (§6.2.1). **Stated**
25. Models assuming unity Lewis number a priori, such as the coherent flame model, "are not able to account for differential diffusion effects and yield inaccurate turbulent flame speed and reaction rate determination", even if tuning still matches the in-cylinder pressure (§6.2.1). **Stated**
26. Gaucherand et al.: a high volumetric ammonia content (57%) can be modelled with unity-Lewis models while lower contents need preferential diffusion (§6.2.2). **Stated**
27. Vancoillie et al.: among common turbulent burning-velocity models only the coherent flame model failed to reproduce the correlation of turbulent burning velocity with $u'$ for methanol at 1 and 5 bar (§6.2.3). **Stated**
28. Multi-mode combustion models are "still on an academic level", tested on benchmark flames (§6.3.3). **Stated**
29. Ihme et al. report a memory reduction by a factor of 5000 for an ANN against tabulation; Chung et al. report a 20% cost saving over LES with direct chemistry using random-forest submodel assignment (§6.4). **Stated**
30. Machine-learned closures "have been mostly developed and tested on benchmark flame simulation cases" and their transfer to engines "is not straight forward"; data-driven models lack extrapolation, so training data must cover the engine's temperature and pressure range (§6.4.1–6.4.2). **Stated**

The thickened-flame species equation is printed (Eq. 43) with diffusion
$\bar\rho\,\Xi_\Delta FD_k\partial_i\tilde Y_k$ and source
$(\Xi_\Delta/F)\bar{\dot\omega}_k$, the dynamic thickening
$F=1+(F_{\max}-1)\tanh(\xi_{\mathrm T}\Omega/\Omega_{\max})$ (Eq. 45) with
the Legier sensor (Eq. 44); the G-equation as
$\partial_tG+\boldsymbol u\cdot\nabla G=s_{\mathrm L}|\nabla G|$ (Eq. 40); the
coherent flame model as a transport equation for $\Sigma_{\mathrm f}$ with strain
source $\alpha_\Sigma(\varepsilon/k)\Sigma_{\mathrm f}$ and sink
$\beta_\Sigma\bar s_{\mathrm f}\Sigma_{\mathrm f}^2/(1-\tilde c)$ (Eq. 34); the unsteady flamelet as
$\partial_tY_k=(\chi/2)\partial^2_ZY_k+\dot\omega_k$ (Eq. 54).

# Printed slips

- **§5.2.5:** "Application examples of flamelet-based models for SI engines are listed in Table 12"; Table 12 is titled "Flamelet-based models CI engine application examples". **§5.2.6:** "Coherent flame model application examples of SI engines are listed in Table 13"; Table 13 is titled "Coherent flame model CI engine application examples".
- **§5.1.5 / Table 7:** the text cites "Salman et al. [202]", Table 7 "Givler et al. [202]"; ref. [202] has first author Salman N, with Givler SD third.
- **§5.1.3:** "Dekana and Peters [147]"; ref. [147] prints "Peters N, Dekena M.".
- **§5.2.3:** "Lueng et al. [253]"; ref. [253] prints "Leung K".
- **§6.2.2:** "the turbulent flame speed according to Peters [317]"; ref. [317] is "Temperature cross-over and non-thermal runaway at two-stage ignition of n-heptane", while Table 5 gives the turbulent flame speed of the same study "according to [57]".
- **Table 5, Distaso et al. [173]:** "$s_L$ according to [174], $s_L$ with detailed chemistry fit" ($s_L$ printed twice).
- **§4.7:** "the first moment CMC equations are identical to the flamelet equation (Eq. (55))"; the flamelet equation is Eq. (54), Eq. (55) the PDF mapping integral.
- **§4.4:** "The turbulent flame speed $s_L$ has to be modeled as well", while $s_L$ is the laminar flame speed elsewhere.
- **§3.3.2:** the reaction-zone thickness is written $(\nabla Z)_R$ in the text and $(\Delta Z)_R$ in Eq. (22) and the regime bullets.
- **§3.3:** "$Le=a_m/D=1$" with $a_m$ undefined.
- **§4.5:** "the model constant $\beta$ has to be adjusted to the numerical scheme"; no $\beta$ appears in Eqs. (43)–(45).
- **§6.2.1 (Chu et al. [351]):** "while the distortion of the kernel shape is mainly due to the tangential strain rate for the unity $Le$ case, production and destruction of the surface area by flame propagation are significantly increased for the unity $Le$ case" ("unity $Le$" printed in both clauses).
- **§6.3.3:** "Hartl et al. [440,441,441]".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar z$, $z'$ (RANS) | $\langle\phi\rangle$, $\phi'$ | **the overbar is a Reynolds average here** |
| $\tilde z$, $z''$ (RANS) | $\langle\phi\rangle_\rho$, $\phi''$ | Favre average |
| $\hat z$, $\mathcal F$ (LES) | $\bar\phi$, $G$ | **the hat is the LES filter, not a test filter** |
| $\langle z\rangle=\widehat{\rho z}/\hat\rho$ (LES) | $\tilde\phi$ | **angle brackets are a Favre filter, not a Reynolds average** |
| $\bar\rho\widetilde{u_i''u_j''}$ | $\langle\rho\rangle R_{ij}$ (Favre form) | positive convention |
| $\hat\rho(\langle u_iu_j\rangle-\langle u_i\rangle\langle u_j\rangle)$ | $\tau_{ij}$ (compressible form) | positive convention |
| $\tau_{ij}$ | $\sigma_{ij}$ | viscous stress; **collision** with the SGS stress |
| $\kappa_C$ | (page-local) thermal conductivity | **collision** with the von Kármán $\kappa$; $\kappa$ is also the flame curvature in Eq. (41) |
| $Re=u'l_t/\nu$ | $Re_{\mathrm t}$ (page-local) | $l_t$ = $L$ |
| $l_k$, $\delta_l$ ($\delta_L$), $\delta_r$ | $\eta$, $\delta_{\mathrm L}$, $\delta_{\mathrm r}$ (page-local) | **collision** of $\delta$ with the boundary-layer thickness |
| $s_L$, $s_T$ | $s_{\mathrm L}$, $s_{\mathrm T}$ | the registry's $S_L$ is the Lundquist number |
| $Z^*$, $c^*$ | $\xi$ (page-local) | sample-space value; **collision** with the reference coordinate $\xi$ of element methods |
| $\psi$ (also $\gamma$), $\tau_c$, $\tau_{mix}$, $C_{mix}$ | $\gamma^*_{\mathrm{PaSR}}$, $\tau_{\mathrm{ch}}$, $\tau_{\mathrm{mix}}$, $C_{\mathrm{mix}}$ | |
| $F$, $E$, $\Omega_{TF}$, $\xi$ (Eq. 45) | $F$, $\Xi_\Delta$, $\Omega_{\mathrm{fs}}$, $\xi_{\mathrm T}$ (page-local) | thickened flame |
| $\Sigma$, $\bar s_f$, $\alpha_f$, $\beta_f$ (Eq. 34) | $\Sigma_{\mathrm f}$, $\bar s_{\mathrm f}$, $\alpha_\Sigma$, $\beta_\Sigma$ (page-local, as on [flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)) | coherent flame model; $\alpha_f$ is the modal-filter strength of registry §11 |
| $\alpha$ (non-premixed regimes) | (page-local) strain rate | **collision** with the DG/FV blending factor |
| $\lambda$ | (page-local) air–fuel equivalence ratio | **collision** with the Taylor microscale |
| $\Gamma$ | gamma function; activation-temperature factor of Eq. (44) | reused in the source |
| $\mu_t$, $\nu_t$, $Sc_t$, $Pr_t$, $k$, $\varepsilon$ | $\mu_t$, $\nu_t$, $Sc_t$, $Pr_t$, $k$, $\varepsilon$ | |

# Reference list

484 printed references, numbered Vancouver style; no reference prints a
DOI. The list is merged complete into the [bibliography](/bibliography.md)
with `citedby` this slug. Refs. [12] and [387] are the same work (Westlye et
al., Fuel 2013), printed twice. Ref. [481] (Nista et al., printed "Proc
Combust Inst 2022" without volume) is the ingested
[nista-2023](/sources/nista-2023.md); refs. [99], [355], [364] and [484] are
the ingested [cuenot-2022](/sources/cuenot-2022.md),
[domingo-2023](/sources/domingo-2023.md),
[berger-2022](/sources/berger-2022.md) and [ihme-2022](/sources/ihme-2022.md).
Ref. [328] prints a garbled author string ("J. CH, P. G, J. PW, K. WC") and
no year; ref. [119] (GRI-Mech 3.0) is undated; refs. [76] and [299] print
"Oijen Jv", ref. [250] "Paola GD"; ref. [370] is an arXiv preprint, kept as
its own entry. The cited works whose printed keys equal those of different
works already in the bibliography (`li-2022`, `liu-2022`, `wang-2023`,
`xu-2023`, `yu-2023`, `zhang-2024`) are keyed `li-2022-u`, `liu-2022-q` (with the further printed `liu-2022-b`, `liu-2022-c` as `liu-2022-r`, `liu-2022-s`), `wang-2023-p`, `xu-2023-g`, `yu-2023-g` and `zhang-2024-h`.

# Pages created or updated

Chunk 15 (2026-10-28). This source is cited on:

- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Turbulent Prandtl number and turbulent heat-flux models](/definitions/turbulent-prandtl-number.md)
- [Conditional moment closure](/methods/conditional-moment-closure.md)
- [Conditional source-term estimation](/methods/conditional-source-term-estimation.md)
- [Flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Neural-network subgrid-scale models](/methods/neural-network-sgs-model.md)
- [Physics-informed neural networks for RANS](/methods/physics-informed-neural-network.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [One-equation subgrid kinetic-energy models](/methods/subgrid-kinetic-energy-equation-model.md)
- [Super-resolution subgrid-scale models](/methods/super-resolution-sgs-model.md)
- [Thickened flame model](/methods/thickened-flame-model.md)
