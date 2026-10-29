---
type: Source
title: "Sandberg & Zhao (2022) — Machine-learning for turbulence and heat-flux model development: A review of challenges associated with distinct physical phenomena and progress to date"
description: "Review of machine-learned RANS stress and turbulent heat-flux closures organised by the physics that defeats standard models — anisotropy, stress–strain misalignment, non-constant turbulent Prandtl number, coupled buoyancy, unsteadiness with or without a spectral gap — and of model-consistent, CFD-driven and multi-objective training."
resource: "doi:10.1016/j.ijheatfluidflow.2022.108983"
source_kind: paper
authors: [Sandberg R.D., Zhao Y.]
year: 2022
venue: "Int. J. Heat Fluid Flow 95:108983"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_International_Journal_of_Heat_and_Fluid_Flow_Sandberg_Machine-learning_for_turbulence_and_heat-flux_model_developm.pdf"
tags: [review, data-driven, rans, heat-flux, symbolic-regression, earsm]
timestamp: 2026-10-29T10:04:00Z
---

# Summary

Sandberg & Zhao (2022) review machine-learned RANS closures for the
Reynolds stress and the turbulent heat flux, organised by the physical
phenomenon that defeats standard closures. The challenges are: stress
anisotropy in wall-bounded flows (near-wall anisotropy, separation on the
[periodic hill](/benchmarks/periodic-hill.md), secondary flow in square
ducts, junction flows, transition paths), the stress–strain misalignment
that invalidates the [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)
in free shear flows and blade-passage wakes, non-constant turbulent
Prandtl number and counter-gradient heat transport in cooling flows (with
a DNS against [$k$-$\omega$ SST](/methods/k-omega-sst-model.md) comparison
of a jet in crossflow), coupled momentum and temperature in natural
convection, and statistically unsteady flows, where the presence or
absence of a [spectral gap](/definitions/spectral-gap.md) decides whether
URANS is legitimate.

The methods section sets out the workflow and the
[a priori and a posteriori](/definitions/a-priori-and-a-posteriori-testing.md)
distinction, the Boussinesq closure and its extension on Pope's ten-tensor
[integrity basis](/methods/tensor-basis-neural-network.md) as an
[explicit algebraic stress model](/methods/explicit-algebraic-reynolds-stress-model.md),
the tensor-diffusivity expansion of the heat flux (GDH, GGDH and HoGGDH as
special cases), the frozen extraction of the turbulence time scale, and
[model-consistent](/methods/model-consistent-training.md) frameworks:
[field inversion](/methods/field-inversion-machine-learning.md),
closed-loop feature consistency, implicit stress treatment, ML-in-the-loop
RANS, CFD-driven training and SpaRTA. The applications cover TBNN and
gene-expression-programming ([symbolic regression](/methods/symbolic-regression-closure.md))
anisotropy models for ducts, hills (trained on the
[backward-facing step](/benchmarks/backward-facing-step.md)),
[turbine](/benchmarks/turbine-cascade.md) wakes and jets in crossflow;
learned heat-flux models; ML corrections of
[correlation-based](/methods/local-correlation-based-transition-model.md) and
[laminar-kinetic-energy](/methods/laminar-kinetic-energy-transition-model.md)
transition models; phase-locked and triple-decomposition URANS closures;
and multi-objective training of coupled stress and heat-flux closures.
[PINNs](/methods/physics-informed-neural-network.md) are judged not to
yield predictive closures, [Reynolds-stress models](/methods/reynolds-stress-model.md)
too costly for wide use, and [$k$-$\varepsilon$](/methods/k-epsilon-model.md)
coefficient variability is cited as a source of
[model-form uncertainty](/definitions/model-form-uncertainty.md). The
authors conclude that a priori gains are common, a posteriori gains need
model consistency, generalizability is the most pressing issue, and
classes of models blended by ML classifiers are more plausible than
universal models. Evidence is that of the cited works.

# Version read

Version of record (Elsevier; received 25 October 2021, accepted 21 April
2022), 18 pages, all read (equation pages 7, 8, 10–14 also visually).
Page 1 matches the metadata; no identity issue. A review: its claims are
those of the cited works as the authors state them, except the
jet-in-crossflow comparison of §2.3. Equation numbers are those of this
version.

# Key claims

Page-local symbols: $\mathsf S_{ij}$, $\mathsf W_{ij}$ the mean strain and
rotation scaled by a turbulence time scale $t_{\mathrm{turb}}$ (the
source's $s_{ij}$, $w_{ij}$, $\tau$; they are the registry's $\mathsf S_{ij}$,
$\mathsf W_{ij}$ when $t_{\mathrm{turb}}=k/\varepsilon$); $I_1,\dots,I_5$ their invariants;
$\langle u_i'T'\rangle$ the turbulent heat flux; $\nabla\vartheta=(\beta^*k^{3/2}/\varepsilon)\nabla\langle T\rangle$
the non-dimensional temperature gradient; $a^{\mathrm h}_n$,
$\Gamma^{(n)}_{ij}$, $J^{\mathrm h}_n$ the heat-flux basis coefficients,
tensors and invariants; $\alpha_{\mathrm{th},t}=\nu_t/Pr_t$ the turbulent
diffusivity; $J$, $J_1$, $J_2$ cost functions (not the invariants
$J^{\mathrm h}_n$); $\eta_{\mathrm{aw}}$ the adiabatic wall effectiveness; BR the
blowing ratio; GEP gene-expression programming.

1. Even in channel, pipe and boundary-layer flows the Boussinesq hypothesis is invalid near the wall because of stress anisotropy, yet the mean flow is usually obtainable with traditional models on a fine enough near-wall grid (§2.1). **Stated**
2. Square-duct secondary flow is stress-induced and needs the imbalance of the normal stresses, "clearly beyond the scope of linear eddy-viscosity models"; quadratic models do not generally ensure it (Modesti 2020), although some gave adequate results (Speziale et al. 1992) (§2.1). **Stated**
3. Jet in crossflow, DNS against steady $k$-$\omega$ SST RANS with eddy-diffusivity heat flux and $Pr_t=0.9$ (simplified Sakai & Takahashi 2011 configuration: jet Reynolds number 12 500 on the jet diameter, incoming boundary layer at $Re_\tau=500$ one diameter upstream, blowing ratio 0.5, temperature ratio about 1.1174): RANS gives a much reduced spanwise spread of wall temperature, wrong $R_{13}$ and $R_{23}$, an underpredicted horseshoe vortex, a spanwise velocity of the wrong sign off-axis, and a strongly underpredicted heat-flux magnitude, worst near the wall (§2.3, Fig. 5). **Shown**
4. In URANS of trailing-edge cooling flows the shedding scales are accounted twice (resolved and modelled), giving excessive turbulent diffusion; constant-$Pr_t$ gradient diffusion overpredicts the wall temperature (§2.3, citing Medic & Durbin 2005; Sandberg et al. 2018). **Stated**
5. "To the authors' knowledge, no existing RANS models have taken into account the strong coupling of heat flux and turbulence modeling during model development" (§2.4). **Stated**
6. When the frequencies of deterministic unsteadiness overlap the turbulence spectrum (no spectral gap), Reynolds averaging fails because it cannot account for the stochastic–deterministic interaction and energy transfer (§2.5, Fig. 8). **Stated**
7. Training on DNS Reynolds stresses cannot guarantee accurate RANS mean flows (Wu et al. 2019; Brener et al. 2021); costs built on predicted mean quantities (CFD-driven) alleviate this (§3.1). **Stated**
8. PINNs "do not yield closures that can be utilized in predictive RANS-based CFD of new configurations" (§3.2). **Stated**
9. The turbulence time scale of RANS $\varepsilon$ or $\omega$ can differ substantially from that of high-fidelity data; the frozen approach of Parneix et al. (1998) solves the $\omega$ or $\varepsilon$ equation with frozen reference mean velocity and stresses to obtain a consistent time scale (§3.2). **Stated**
10. Including temperature gradients in the heat-flux invariants $J^{\mathrm h}_n$ violates the linearity principle for passive scalars (Pope 1983; Seki et al. 2003), but is retained because temperature in compressible turbulence is not strictly passive (§3.3). **Stated**
11. CFD-driven training needs much less data (select profiles, usable with experiments beyond DNS/LES reach), excludes non-converging candidates, and tests the model a posteriori during training; its drawback is a dramatically higher development cost, currently intractable for complex 3D flows (§3.4, §4.1). **Stated**
12. The TBNN of Ling et al. (2016), trained on duct, channel, jets in crossflow, square cylinder and converging–diverging channel, improved anisotropy a priori and duct corner vortices a posteriori on a duct at another Reynolds number and a wavy wall (§4.1). **Stated**
13. GEP trained on a backward-facing step gave excellent a posteriori periodic-hill predictions with the first four basis tensors and two invariants; some individuals had very large coefficients, non-realizable stresses and unstable runs, removable thanks to symbolic transparency but not robustly automatically (§4.1). **Stated**
14. CFD-driven GEP for high- and low-pressure-turbine wake mixing produced simpler models than frozen training and improved wake profiles in all a posteriori tests on other geometries, predominantly through increased diffusion (§4.1). **Stated**
15. GEP and TBNN on jets in crossflow (trained inline, tested a priori skewed) both greatly improved on the linear baseline but failed where the streamwise vorticity is strongest (§4.1). **Stated**
16. Junction flow (Weatheritt & Sandberg 2019): recursive feature elimination reduced the basis; the cost included the divergence of the stress; the a priori error fell strongly but the a posteriori velocity improved only marginally (§4.1). **Stated**
17. SpaRTA (Schmelzer et al. 2020) adds a production correction $R$ to the $k$ and $\omega$ equations and is tractable in 3D; Huijing et al. (2021) obtained much better mean flow and good generalization on a wall-mounted cube, "indicating that both a non-linear anisotropy model and a production correction in the transport equations is needed for such flows" (§4.1, Eq. 8). **Stated**
18. Milani et al. (2019): adding $Re_d$ and $\nu_t/\nu$ as inputs improved turbulent-diffusivity predictions, the invariants carrying about 55% of model importance (§4.2.1). **Stated**
19. Milani et al. (2021, ICHMT): a TBNN trained on one flow class and tested on another performed like the baseline, "suggesting that such models might not perform as poorly as believed when extrapolation to other flow classes is attempted" (§4.2.1). **Stated**
20. Haghiri & Sandberg (2020): GEP models of a spatially varying $1/Pr_t$ gave average $Pr_t$ between 0.42 and 0.6 for trailing-edge slots, well below the "typical" 0.85–0.9; $\eta_{\mathrm{aw}}$ improved for medium and small lip thickness but not for large (vortex shedding) (§4.2.1). **Stated**
21. Lav et al. (2021), the first CFD-driven heat-flux training: wall temperature in the cost function worked best; a model trained at BR 1.26 had mean $Pr_t=0.32$ and performed well at two other blowing ratios; training on several blowing ratios at once generalized better (§4.2.1, Eq. 11). **Stated**
22. Weatheritt et al. (2020): recursive feature elimination on jet-in-crossflow data ranked $\Gamma^{(4)}$ first, then $\Gamma^{(9)},\Gamma^{(2)},\Gamma^{(5)}$, "the GDH was not the appropriate basis while the GGDH and HoGGDH featured prominently"; the GEP model Eq. 14 beat eddy-diffusivity models a posteriori (scalar transport on high-fidelity velocity) (§4.2.2). **Stated**
23. Akolekar et al. (2019), low-pressure turbine with incoming wakes, 20 phases per cycle: models trained on one phase work on the same phase; trained on phase 13 they work on phase 5, trained on phase 10 they fail on phase 18; the trend of $g^{(1)}$ and of the nonlinear part tracks wake–wake interaction, so two models trained on two representative phases suffice (§4.4.1, Fig. 10). **Shown** (reproduced figure)
24. Lav et al. (2019) triple decomposition into mean, periodic and stochastic parts: the stochastic anisotropy was insensitive to Fourier, POD or DMD extraction; the GEP closure of the stochastic anisotropy sharply reduces the modelled diffusion ($g^{(1)}$), its nonlinear coefficients being small; URANS then resolves more scales and improves the near and far wake (§4.4.2). **Stated**
25. Lav & Sandberg (2020): GEP closures of stochastic stress and heat flux in URANS of a trailing-edge slot, trained at BR 1.26 with lip thickness 1.14, average $Pr_t=0.471$; the nearly perfect $\eta_{\mathrm{aw}}$ at BR 1.26 "might be fortuitous" since velocity profiles do not match closely; at BR 0.86 improvement up to $x/s=20$, weaker downstream, attributed to frozen (non-model-consistent) training (§4.4.2, Fig. 11). **Shown** (reproduced figure)
26. Coupled closures (anisotropy plus heat flux) "has to date not been considered with field inversion"; multi-expression CFD-driven training (Waschkowski et al. 2022) with Pareto-based optimisation of the velocity and temperature errors $J_1$, $J_2$ (Eq. 17) improved both over the baseline and over separately trained models in vertical natural convection (§4.5, Figs 12–13). **Shown** (reproduced figure)
27. A plain sum of $J_1$ and $J_2$ is not useful when the errors differ in magnitude, and weighting is "at best an ad hoc process"; Pareto fronts allow model selection after training (§4.5). **Stated**
28. Most work is on statistically steady RANS; generalizability is the most pressing issue; open data sets with agreed formats are needed; universal models are unlikely, classes of models for flow topologies blended by ML classification more likely (§5). **Stated**

The stress expansion of Eq. (2), in registry notation and with the
positive convention for which Eq. (1) is traceless (see Printed slips):
$\langle\rho u_i''u_j''\rangle-\tfrac23\langle\rho\rangle k\delta_{ij}=-2\mu_t\langle S^d_{ij}\rangle+2\langle\rho\rangle k\,g^{(1)}T^{(1)}_{ij}+2\langle\rho\rangle k\sum_{n=2}^{10}g^{(n)}(I_1,\dots,I_5)T^{(n)}_{ij}$,
labelled linear Boussinesq, additional linear and additional nonlinear
terms; for statistically 2D flows only $T^{(1)}$–$T^{(4)}$ and $I_1$,
$I_2$ are used. The heat-flux expansion (Eq. 6, after Younis et al. 2005)
is $-\langle u_i'T'\rangle=\sqrt k\,[a^{\mathrm h}_1\partial_i\vartheta+\sum_{n=2}^{10}a^{\mathrm h}_n\Gamma^{(n)}_{ij}\partial_j\vartheta]$,
with GDH ($a^{\mathrm h}_1=1/Pr_t$ only, Eq. 9), GGDH (Daly & Harlow,
only $a^{\mathrm h}_2$, Eq. 12) and HoGGDH (Abe & Suga, only
$a^{\mathrm h}_4$, Eq. 13) as special cases.

# Printed slips

- **Eq. (1) against §3.2:** $\tau_{ij}$ is defined as $-\overline\rho\,\overline{u''_iu''_j}$, but Eq. (1) writes $\tau_{ij}-\frac23\overline\rho k\delta_{ij}=-2\mu_t[S_{ij}-\frac13S_{kk}\delta_{ij}]$. with that definition $\tau_{kk}=-2\overline\rho k$, so the left side has trace $-4\overline\rho k$ while the right side is traceless; with $\tau_{ij}=+\overline\rho\,\overline{u''_iu''_j}$ both are traceless *(compiler check, not in the sources)*. §4.1 then writes $P_k=\tau_{ij}\partial u_i/\partial x_j$, which uses the negative convention.
- **Eqs. (12)–(13), dimensions.** with $\tau_{ij}=\overline{u'_iu'_j}/2k$, dimensionless as defined after Eq. 6, and $\alpha_2=C_{GGDH}/(\beta^*k)$, $\sqrt k\,\alpha_2\tau_{ij}\partial\vartheta/\partial x_j=C_{GGDH}(k/\epsilon)\tau_{ij}\partial\overline\Theta/\partial x_j$, which has units K·s/m, not those of a heat flux; the printed right side $C_{GGDH}\tau_{ij}\partial_j\overline\Theta/\omega$ has the same defect. Both are dimensionally consistent if $\tau_{ij}$ there is the dimensional $\overline{u'_iu'_j}$, and the middle and right expressions then agree only if $\omega=\epsilon/k$; with $\omega=\epsilon/(\beta^*k)$ a factor $\beta^*$ remains. Eq. (13) is likewise consistent only with dimensional $\tau$ *(compiler check, not in the sources)*.
- **Eq. (7):** $J_1$ and $J_4$ are printed with the same tensor, $\frac{\partial\vartheta}{\partial x_i}w_{ik}w_{kj}\frac{\partial\vartheta}{\partial x_j}$.
- **Eq. (16).** the kinematic flux $\overline{u''_iT''}$ is added to $\mu_t f\,\partial\overline T/\partial x_i$ with the dynamic eddy viscosity; the two terms differ by a density factor unless $f$ absorbs it *(compiler check, not in the sources)*.
- **After Eq. (12):** "$C_{GDDH}(I_m,J_n)$" for $C_{GGDH}$.
- **§4.2.1:** the Lav et al. (2021) cost function is called "Eqn. 9"; it is Eq. (11), Eq. (9) is the GDH.
- **§3.2:** "(Spalart and Allmaras, yyyy)", and the reference list entry has no year.
- **Citations against the list:** "Durbin, 1995, 2005" is cited but no Durbin 2005 is listed; "Weatheritt and Sandberg (2017, 2020)" is cited but no Weatheritt & Sandberg 2020 is listed, while an uncited "Wang, R., Kashinath, K., … 2020" is; Gatski & Speziale (1993) is printed twice; Sandberg & Michelassi is cited "2021" with the reference "Ann. Rev. Fluid Mech. 54, 2022".
- **Symbols:** $\tau_{ij}$ is the Reynolds stress $-\overline\rho\,\overline{u''_iu''_j}$ (§3.2), $\overline{u'_iu'_j}/2k$ (after Eq. 6) and, for dimensional consistency, $\overline{u'_iu'_j}$ in Eqs. (12)–(13); $\tau$ alone is the time scale.
- **Typos:** "A shown in Fig. 5" (§2.3), "have tacked" (§3.4), "The new models where then tested" (§4.2.1), "Despite of the success" (§4.3).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\overline{(\cdot)}$, $u''_i$, $u'_i$ | $\langle\cdot\rangle$, $u_i''$, $u_i'$ | Reynolds average; **collision:** the registry's overbar is the LES filter |
| $\tau_{ij}=-\overline\rho\,\overline{u''_iu''_j}$ | $-\langle\rho u_i''u_j''\rangle$ | **negative convention** (§3.2); Eq. (1) consistent only with the positive one |
| $\tau_{ij}=\overline{u'_iu'_j}/2k$ (after Eq. 6) | $b_{ij}+\tfrac13\delta_{ij}$ | **collision** |
| $\tau$ (time scale), $s_{ij}$, $w_{ij}$ | $t_{\mathrm{turb}}$, $\mathsf S_{ij}$, $\mathsf W_{ij}$ | **collision:** $\tau$ is not a stress |
| $S_{ij}-\frac13S_{kk}\delta_{ij}$ | $\langle S^d_{ij}\rangle$ | |
| $V^\gamma_{ij}$, $\zeta_\gamma$ | $T^{(n)}_{ij}$, $g^{(n)}$ | Pope's integrity basis |
| $I_1,\dots,I_5$ | $I_1,\dots,I_5$ (page-local) | |
| $a^R_{ij}$, $\xi_\gamma$, $R=ka^R_{ij}\partial_ju_i$ | $2b^R_{ij}$, (coefficients), $R$ | SpaRTA production correction |
| $\epsilon$, $\omega$, $\beta^*$ | $\varepsilon$, $\omega$, $\beta^*$ | |
| $\mu_t$, $\nu_t$ | $\mu_t$, $\nu_t$ | |
| $\overline\Theta$, $\Theta'$, $\theta'$, $T$ | $\langle T\rangle$, $T'$ | used interchangeably in the source |
| $\partial\vartheta/\partial x_i$ | $\partial_i\vartheta$ (page-local) | |
| $\alpha$, $\alpha_t$ | $\alpha_{\mathrm{th}}=\nu/Pr$, $\alpha_{\mathrm{th},t}$ (page-local) | **collision:** not the DG blending factor $\alpha$ |
| $\alpha_\gamma$, $\Gamma^\gamma_{ij}$, $J_n$ | $a^{\mathrm h}_n$, $\Gamma^{(n)}_{ij}$, $J^{\mathrm h}_n$ (page-local) | **collision:** $J$, $J_1$, $J_2$ are also costs |
| $C_{GGDH}$, $C_{HoGGDH}$ | (GGDH and HoGGDH coefficient functions) | |
| $Pr_t$, $Pr_T$ | $Pr_t$ | |
| $\eta$ | $\eta_{\mathrm{aw}}$ (page-local) | **collision** with the Kolmogorov length |
| $\phi=\overline\phi+\tilde\phi+\phi''$ | (mean, periodic and stochastic parts, page-local) | **collision:** tilde is not a Favre filter, double prime not a Favre fluctuation |
| $J^B$, $J^{EARSM}$, $J^{\%}$ | (baseline and model errors, relative reduction, page-local) | Fig. 10 |

# Reference list

128 printed references, author-year style, in order of first citation
(not alphabetical), without DOIs. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug; the twice
printed Gatski & Speziale (1993) is one entry. Same-author same-year works
are keyed in printed order (Weatheritt 2017a–d, Milani 2021, Akolekar
2019 and 2021, Lav 2020, Zhao 2020). The cited Sandberg & Michelassi
("2021") is the ingested [sandberg-2022](/sources/sandberg-2022.md);
the undated Spalart & Allmaras paper is mapped to the bundle's existing
entry by title; the cited Wang & Yeung (2013), on visual tracking, is a
different work from the ingested [wang-2013](/sources/wang-2013.md) and is keyed `wang-2013-h`; the Spalart & Allmaras paper is `spalart-1992`. The
ingested Sources [duraisamy-2019](/sources/duraisamy-2019.md) and
[duraisamy-2021](/sources/duraisamy-2021.md) are the same works as the
entries cited. Several J. Fluid Mech. and ASME J. Turbomach. entries
print no pages. No item is unparseable.

# Pages created or updated

Chunk 10 (2026-10-27), cited further in chunks 12–13. This source is cited on:

- [Backward-facing step](/benchmarks/backward-facing-step.md)
- [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md)
- [Periodic hill](/benchmarks/periodic-hill.md)
- [Turbine cascades (T106, T161, VKI LS89)](/benchmarks/turbine-cascade.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Barycentric anisotropy map](/definitions/barycentric-anisotropy-map.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Spectral gap](/definitions/spectral-gap.md)
- [Turbulent Prandtl number and turbulent heat-flux models](/definitions/turbulent-prandtl-number.md)
- [Explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Laminar kinetic energy transition models](/methods/laminar-kinetic-energy-transition-model.md)
- [Local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
- [Model-consistent (a posteriori) training of learned closures](/methods/model-consistent-training.md)
- [Physics-informed neural networks for RANS](/methods/physics-informed-neural-network.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
- [Symbolic-regression turbulence closures](/methods/symbolic-regression-closure.md)
- [Tensor-basis neural network and the integrity basis](/methods/tensor-basis-neural-network.md)
