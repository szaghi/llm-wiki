---
type: Source
title: "Sandberg & Michelassi (2022) — Fluid Dynamics of Axial Turbomachinery: Blade- and Stage-Level Simulations and Models"
description: "Review of the blade- and stage-level fluid dynamics of axial compressors and turbines as revealed by DNS and LES, of what free shear flows, transition, separation and shock interaction demand of RANS, transition and hybrid models, and of data-driven closures trained on high-fidelity turbomachinery data."
resource: "doi:10.1146/annurev-fluid-031221-105530"
source_kind: paper
authors: [Sandberg R.D., Michelassi V.]
year: 2022
venue: "Annu. Rev. Fluid Mech. 54:255-285"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Annual_Review_of_Fluid_Mechanics_Sandberg_Fluid_Dynamics_of_Axial_Turbomachinery_Blade-_and_Stage-Leve.pdf"
tags: [turbomachinery, review, rans, transition, les, data-driven]
timestamp: 2026-10-27T10:58:00Z
---

# Summary

Sandberg & Michelassi (2022) review how [DNS](/definitions/direct-numerical-simulation.md),
[LES](/definitions/large-eddy-simulation.md), [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
and RANS/URANS have advanced the understanding of loss-generating flow in
the blade rows of axial [turbines](/benchmarks/turbine-cascade.md) and
[compressors](/benchmarks/compressor-cascade.md), and what that flow
demands of models. The review is organised by phenomenon:
blade-to-blade and row-to-row interaction, with deterministic unsteadiness
at the reduced frequency coexisting with stochastic turbulence;
free-stream turbulence (with [synthetic inflow](/methods/inflow-turbulence-generation.md)
of prescribed intensity and length scale), wakes, wake distortion and
trailing-edge shedding; boundary layers under strong pressure gradients,
[separation bubbles](/definitions/laminar-separation-bubble.md), natural,
bypass, separated-flow and wake-induced transition, and
[shock–boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).
The modelling verdicts are three. Reynolds averaging needs a spectral gap
between deterministic and turbulent frequencies, which vanishes at modern
rotation speeds and with trailing-edge shedding. Stress–strain
misalignment in distorted wakes invalidates the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md). The
$\gamma$–$Re_\theta$ [correlation-based model](/methods/local-correlation-based-transition-model.md)
suppresses wake-induced transition, which [laminar kinetic energy](/methods/laminar-kinetic-energy-transition-model.md)
models address. The [$k$-$\varepsilon$](/methods/k-epsilon-model.md),
[$k$-$\omega$](/methods/k-omega-model.md), [Spalart–Allmaras](/methods/spalart-allmaras-model.md),
[Reynolds-stress](/methods/reynolds-stress-model.md) and
[scale-adaptive](/methods/scale-adaptive-simulation.md) models are placed
in this frame, and [wall-modelled LES](/methods/wall-modelled-les.md) and
[grid requirements](/results/les-grid-point-requirements.md) set the cost
of scale resolution.

The exploitation section covers design correlations from DNS/LES sweeps,
loss analyses (POD, mechanical work potential, a Favre-averaged entropy
analysis that places the RANS error in near-wake turbulence production),
and data-driven closures: [field inversion and machine learning](/methods/field-inversion-machine-learning.md),
gene-expression programming of explicit algebraic stress models
([symbolic regression](/methods/symbolic-regression-closure.md)) trained on
time-averaged, phase-locked or triple-decomposed data, CFD-driven
([model-consistent](/methods/model-consistent-training.md)) training, the
[a priori and a posteriori](/definitions/a-priori-and-a-posteriori-testing.md)
distinction, the [tensor-basis network](/methods/tensor-basis-neural-network.md),
and brief mentions of [neural-network SGS models](/methods/neural-network-sgs-model.md)
and [PINN](/methods/physics-informed-neural-network.md)
[wall models](/methods/machine-learning-wall-model.md). The authors expect
machine learning to patch specific weaknesses, not to be "our savior".
Evidence is a curated summary of published simulations.

# Version read

Version of record (Annual Reviews; Review in Advance 13 October 2021):
31 pages (pp. 255–285), all read, pp. 258, 259, 263, 268, 269, 277 and
278 also visually. Page 1 matches the metadata; no identity issue. A
review: its claims are those of the cited works as the authors state
them. Equation and figure numbers are those of this version.

# Key claims

Page-local symbols: $\mathcal R_{\theta t}$ the transported
transition-onset momentum-thickness Reynolds number (as on the
[correlation-based model](/methods/local-correlation-based-transition-model.md)
page); $F_{\mathrm{red}}=fC/V_{2,is}$ the reduced frequency; $Zw$ the
Zweifel coefficient; $K_{\mathrm{acc}}$ the acceleration parameter;
$M_{is}$, $Re_{is}$ isentropic Mach and Reynolds numbers; TI, LS
free-stream turbulence intensity and length scale; GEP gene-expression
programming.

1. The DNS cost of evolving flat-plate boundary layers scales as $Re_{L_x}^{37/14}$ (Choi & Moin 2012), and blade-row domains must also include passages and inter-row gaps (§2.1). **Stated**
2. Inaccurate turbulence prediction in gas turbines can cost 0.5% of cycle efficiency; a 2% error in metal temperature can halve blade life; 1% less cooling air raises cycle efficiency by 0.4% (§1). **Stated**
3. RANS closure errors weigh far more than LES closure errors because RANS models carry all turbulent scales, LES only the high-wavenumber part (§2.2.2.1). **Stated**
4. The cost and lack of robustness of full Reynolds-stress models have precluded their widespread turbomachinery use (§2.2.2.1). **Stated**
5. Hybrid RANS/LES is classified into zonal approaches with predetermined RANS and LES regions, "like in detached eddy simulations", and unified approaches blending on flow, geometry and grid properties, such as scale-adaptive simulation; defining a robust blend has limited industrial use (§2.2.2.2). **Stated**
6. No transition models based on first principles exist; $e^N$ methods have no reason to be accurate in the high-disturbance turbomachinery environment; low-Reynolds-number wall damping has "no obvious relation to the transition physics" (§2.2.3). **Stated**
7. A mixing plane filters out all streamwise vorticity, so end-wall boundary-layer growth and spanwise mixing are wrong and multistage prediction is inaccurate (§2.2.4). **Stated**
8. Reynolds averaging requires a spectral gap between deterministic frequencies (rotor–stator interaction, shedding) and the turbulence cascade; without it "any model based on Reynolds averaging will fail" and scale-resolving simulation is required; higher rotation speeds make the gap vanish (§3.1.2, §3.2.3, Fig. 1). **Stated**
9. Acceleration and turning in the passages misalign the Reynolds-stress and strain tensors in wake cores, invalidating the linear Boussinesq hypothesis; nonlinear closures or Reynolds-stress transport are a possible cure (§3.2.3). **Stated**
10. URANS misrepresents shedding frequency and wake decay because shedding is accounted twice, resolved and in the closure; a GEP closure trained on the stochastic part of a triple decomposition of wake LES (Lav et al. 2019) has a much smaller turbulent diffusion and improves near- and far-wake URANS prediction (§3.2.3). **Stated**
11. In a DNS of pulsating separated, thermally stratified flow (Wissink et al. 2004) the turbulent shear stress was rarely aligned with the velocity deformation, nor the heat flux with the temperature gradient, and $Pr_t$ ranged from 0.4 to 4 instead of a constant near 0.9 (§3.2.3, §3.3). **Stated**
12. In strong favourable pressure gradients a boundary layer is likely to relaminarize for $K_{\mathrm{acc}}=\nu U_e^{-2}\,dU_e/ds>3.5\times10^{-6}$ (§3.3.1, Eq. 1). **Stated**
13. Leading-edge changes that alter the separation bubble gave up to 30% difference in blade loss (Wheeler et al. 2009) (§3.3.2). **Stated**
14. In HPT-vane DNS/LES at $Re_{is}=570\,000$, low-TI inflow gives leading-edge streaks whose spacing follows the inflow integral scale, transient-growth-like amplification and breakdown by the sinuous mode in the favourable and the varicose mode in the adverse pressure gradient; high TI with large length scales gives earlier transition through breakdown of vortical structures (Zhao & Sandberg 2020a) (§3.3.3.2, Fig. 5). **Stated**
15. In HPT-nozzle LES with TI 6–20% and length scales 5–20% of chord, larger length scales give an earlier rise and higher heat transfer on both sides (Pichler et al. 2017b) (§3.2.1, Fig. 4a). **Stated**
16. Unsteady losses from wake distortion do not grow monotonically with $F_{\mathrm{red}}$; at high $F_{\mathrm{red}}$ wakes merge before entering the passage ("fogging") (§3.2.2). **Stated**
17. In a transonic HPT, the interaction of the shock with trailing-edge shedding, not the passage shock, adds loss through turbulence production in the wake (Zhao & Sandberg 2020b) (§3.2.2). **Stated**
18. In an LPT-stage LES at $Re_{is}=100\,000$, once the wake apex passes the separation point, separation and reattachment move downstream at about one half and one quarter of the local isentropic velocity, and the bubble vanishes for about 25% of the time (Pichler et al. 2017a) (§3.3.3.4, Fig. 6). **Stated**
19. In the $\gamma$–$Re_\theta$ model wake-induced transition is suppressed because the low $\mathcal R_{\theta t}$ of incoming wakes is not fed into the blade boundary layers; the Langtry–Menter separation term raises the intermittency "above unity" in transitional separated regions (§3.3.3.3–3.3.3.4). **Stated**
20. The laminar kinetic energy model of Pacciani et al. (2014) creates no laminar kinetic energy on the wake-induced path, transition there being triggered by the wake deficit and turbulence, and lets it grow between wakes; the $k$–$\overline{v^2}$–$\omega$ model adds a transport equation for the wall-normal fluctuation to model Klebanoff-distortion growth (§2.2.3, §3.3.3). **Stated**
21. Transonic-compressor low-frequency shock oscillation can move the shock by up to 10% of axial chord, and URANS cannot predict the amplitude (Hergt et al. 2019) (§3.3.4). **Stated**
22. Entropy analysis of LES and RANS of the VKI LS89 vane: mean-flow entropy generation is confined to the suction-side boundary layer, the largest contribution is near-wake turbulence production, and that is where RANS departs most from high fidelity (Zhao & Sandberg 2020c) (§4.2). **Stated**
23. A mechanical-work-potential loss coefficient, unlike the pressure-loss coefficient, accounts for the operating pressure of a stage in an engine (Leggett et al. 2020, 2021) (§4.2). **Stated**
24. Injecting the true DNS Reynolds stress into RANS does not guarantee the mean flow (Parneix et al. 1998) and can jeopardize robustness (Wu et al. 2019); field inversion plus machine learning (Parish & Duraisamy 2016) yields model-consistent closures at a significant inverse-problem cost (§4.3). **Stated**
25. Field inversion with a neural network correcting Spalart–Allmaras in a low-Reynolds-number LPT cascade matched a costlier two-equation model with $\gamma$–$Re_\theta$ transition (Ferrero et al. 2020) (§4.3). **Stated**
26. CFD-driven training (GEP with a RANS solve per candidate; Zhao et al. 2020) needs much less data, and models trained on HPT data predicted LPT wake-loss profiles for other geometries and Reynolds numbers (§4.3). **Stated**
27. The GEP explicit algebraic model of Eq. (2), $\langle\rho u_i''u_j''\rangle-\tfrac23\langle\rho\rangle k\delta_{ij}=-2\mu_t\langle S^d_{ij}\rangle_\rho+2\langle\rho\rangle k\,g^{(1)}T^{(1)}_{ij}+2\langle\rho\rangle k\sum_{n=2}^4g^{(n)}T^{(n)}_{ij}$ in registry notation (labelled linear Boussinesq, additional linear and additional nonlinear terms) (with the sign convention of the printed left side; see Printed slips), trained on single phases of phase-locked LPT data, performs well on its training phase and can perform poorly on others; the nonlinear terms matter more for phases with wake–wake interaction; two models suffice across all phases (Akolekar et al. 2019) (§4.3, Fig. 7). **Stated**
28. A posteriori testing is full CFD with the new model, accounting for its interplay with the transport equations; a priori testing checks whether a trained model reproduces training or test data, for example a stress closure fed with reference velocity gradients (§4.3). **Stated**
29. Machine-learning SGS models "have yet to be employed" in blade- or stage-level simulations (§4.3); machine learning will not produce models predicting all turbomachinery flow features, but will address specific mechanisms in multiexpression approaches (Future issue 5). **Stated** (opinion)

# Printed slips

- **Eq. (2) against p. 259:** $\tau^R_{ij}$ is defined as $-\overline{\rho u''_iu''_j}$, but Eq. (2) writes $\tau^R_{ij}-\frac23\bar\rho k\delta_{ij}=-2\mu_t[\tilde S_{ij}-\frac13\tilde S_{kk}\delta_{ij}]+\dots$. *(Compiler check, not in the sources: with the p. 259 definition the trace of $\tau^R_{ij}$ is $-2\bar\rho k$, so the printed left side has trace $-4\bar\rho k$, while the Boussinesq term $-2\mu_t[\tilde S_{ij}-\frac13\tilde S_{kk}\delta_{ij}]$ is traceless; with $\tau^R_{ij}=+\overline{\rho u''_iu''_j}$ the left side is traceless too.)*
- **Fig. 1:** the URANS equation prints "$\partial(\bar\rho\tilde u_i)/Dt$".
- **§3.3.3.3:** "Kelvin–Helmhotlz".
- **§4.3:** "Duraisamy 2020" in the text, "Duraisamy K. 2021" in the list.
- **§2.2.2.1:** "Wilcox et al. (1998)" twice, while the list has the single author "Wilcox DC. 1998".
- **Reference list:** "Ferreira C. 2001" is listed but not cited in the text; "Lechnerm" (Egorov et al.) and "turbomachichines" (Denton & Singh) as printed.
- **Symbols:** $\gamma$ is the intermittency in a margin note and the ratio of specific heats in Eq. (1); $\omega$ is both the turbulence frequency and the wake maturity; $\tau$ both the stresses and the work coefficient; the summation index $k$ of Eq. (2) is also the turbulent kinetic energy.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar{(\cdot)}$ | $\langle\phi\rangle$ | Reynolds (time) average; **collision:** the registry's overbar is the LES filter |
| $\tilde{(\cdot)}$, $u''_i$ | $\langle\phi\rangle_\rho$, $u''_i$ | Favre average and fluctuation; **collision:** the registry's tilde is the Favre filter |
| $\langle\cdot\rangle$ | $\bar\phi$ | spatial (LES) filter; **collision** |
| $\hat{(\cdot)}$ | $\tilde\phi$ | Favre filter; **collision:** not a test filter |
| $\tau^R_{ij}=-\overline{\rho u''_iu''_j}$ | $-\langle\rho u''_iu''_j\rangle$ | **negative convention** (p. 259); Eq. (2) uses the positive one |
| $\tau^{DET}_{ij}$, $\tau^{SGS}_{ij}$ | (deterministic stress, page-local), $\tau_{ij}$ | sign of $\tau^{SGS}_{ij}$ not stated |
| $\sigma_{ij}$ | $\sigma_{ij}$ | viscous stress |
| $\epsilon$, $L$ | $\varepsilon$, (turbulence length scale of $k$–$L$) | **collision:** $L$ is not the registry's integral scale definition |
| $\tilde S_{ij}-\frac13\tilde S_{kk}\delta_{ij}$ | $\langle S^d_{ij}\rangle_\rho$ | |
| $V^k_{ij}$, $\zeta_k$, $I_k$ | $T^{(n)}_{ij}$, $g^{(n)}$, (invariants, page-local) | Pope's integrity basis |
| $J$, $J^B$, $J^{GEP}$, $J^{\%}$ | (normalized mean-square errors, page-local) | Fig. 7 |
| $\gamma$ (margin), $Re_{\theta t}$ | $\gamma$, $\mathcal R_{\theta t}$ | transition pages |
| $\gamma$ (Eq. 1) | $\gamma$ | ratio of specific heats |
| $K$ | $K_{\mathrm{acc}}$ (page-local) | **collision:** not the spectral kinetic energy $K$ |
| $\omega$ (wake maturity) | $\omega_{\mathrm{wm}}$ (page-local) | **collision:** not the specific dissipation rate |
| $\tau=\Delta H_0/U^2$ | $\tau_{\mathrm{work}}$ (page-local) | **collision:** not a stress |
| $Zw$, $\Phi$, $F_{red}$ | $Zw$, $\Phi_{\mathrm{fl}}$, $F_{\mathrm{red}}$ (page-local) | **collision:** $\Phi$ is not the shared Ducros factor $\Phi_i$ |
| $C_x$, $C$, $S$ | $c_{ax}$, (chord), (pitch) | **collision:** $S$ is not the strain rate |
| $c_p$ (Fig. 3b) | $C_p$ | blade loading |
| $Re_{is}$, $M_{is}$, $Re_{L_x}$ | (isentropic numbers; Reynolds number on the development length, page-local) | |

# Reference list

133 printed references, author-year style ("Literature Cited"),
alphabetical, without DOIs. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Same-author
same-year works are keyed in printed order (the Michelassi, Pichler and
Zhao families, e.g. Zhao & Sandberg 2020a–c). The ingested Sources
[bose-2018](/sources/bose-2018.md), [duraisamy-2019](/sources/duraisamy-2019.md) and [duraisamy-2021](/sources/duraisamy-2021.md) are
the same works as the entries cited. Conference papers (Laskowski et al.
2016, Denton & Singh 1979, Spalart & Allmaras 1992) are recorded as
`@misc`. The text–list mismatches are listed under Printed slips. No item
is unparseable.

# Pages created or updated

Chunk 9 (2026-10-27), cited further in chunk 10. This source is cited on:

- [Compressor cascades](/benchmarks/compressor-cascade.md)
- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Turbine cascades (T106, T161, VKI LS89)](/benchmarks/turbine-cascade.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Spectral gap](/definitions/spectral-gap.md)
- [Explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [Wilcox k-ω model](/methods/k-omega-model.md)
- [Laminar kinetic energy transition models](/methods/laminar-kinetic-energy-transition-model.md)
- [Local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
- [Machine-learning wall models](/methods/machine-learning-wall-model.md)
- [Model-consistent (a posteriori) training of learned closures](/methods/model-consistent-training.md)
- [Neural-network subgrid-scale models](/methods/neural-network-sgs-model.md)
- [Physics-informed neural networks for RANS](/methods/physics-informed-neural-network.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
- [Scale-adaptive simulation](/methods/scale-adaptive-simulation.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Symbolic-regression turbulence closures](/methods/symbolic-regression-closure.md)
- [Tensor-basis neural network and the integrity basis](/methods/tensor-basis-neural-network.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
