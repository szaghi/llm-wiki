---
type: Source
title: "Zangeneh (2021) — Data-driven model for improving wall-modeled large-eddy simulation of supersonic turbulent flows with separation"
description: "Corrects the wall shear stress and wall heat flux of an SST-IDDES wall-modelled LES with a random-forest regression on seven-point-stencil features, feeding corrected eddy viscosity and turbulent Prandtl number back into the solver; a posteriori on a supersonic flat plate and a Mach 2.9 expansion–compression corner."
resource: "doi:10.1063/5.0072550"
source_kind: paper
authors: [Zangeneh R.]
year: 2021
venue: "Phys. Fluids 33:126103"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2021_Crossref_Physics_of_Fluids_Zangeneh_Data-driven_model_for_improving_wall-modeled_large-eddy_simu.pdf"
tags: [wmles, wall-model, data-driven, log-layer-mismatch, compressible, separated-flow]
timestamp: 2026-10-29T07:40:00Z
---

# Summary

Zangeneh (2021) targets [log-layer mismatch](/definitions/log-layer-mismatch.md)
and the skin-friction and heat-flux errors it causes in
[wall-modelled LES](/methods/wall-modelled-les.md) of supersonic flows. The
baseline is an SST-based IDDES ([detached-eddy simulation](/methods/detached-eddy-simulation.md)
on the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)), run as a
WMLES with a fully coupled RANS inner layer on an auxiliary wall grid
whose $\tau_w$ and $q_w$ are Neumann conditions for the LES, a branch of
[hybrid RANS/LES](/definitions/hybrid-rans-les.md). The author attributes
the discrepancy at the matching location to the different eddy
viscosities and turbulent Prandtl numbers of the LES and the RANS layer.

The [machine-learning wall model](/methods/machine-learning-wall-model.md)
is a random-forest regression of 300 trees mapping local mean-flow
features of the baseline WMLES to the discrepancy of $\tau_w$ and $q_w$
against experiment or DNS; among its precedents the paper cites
discrepancy-modelling works of the
[model-form uncertainty](/definitions/model-form-uncertainty.md)
literature (Xiao et al. 2016; Wang et al. 2017) and works of
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)
(Parish & Duraisamy 2016; Singh et al. 2017). The inputs come from the seven-point stencil of
Lozano-Durán & Bae centred at the second off-wall point: relative
velocities, symmetric and antisymmetric velocity-difference tensors, a
wall-stress and a pressure/temperature-gradient velocity scale. The
predicted wall values correct $\mu_t$ and $Pr_t$, which are fed back into
the solver ("a corrective approach and not 'standard' turbulence model").
All tests are [a posteriori](/definitions/a-priori-and-a-posteriori-testing.md):
a supersonic zero-pressure-gradient [turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md),
trained at $Re_\delta=57\,300$, $M=2.28$ and predicted at
$Re_\delta=617\,000$, $M=1.69$, where the corrected profile in
[Van Driest scaling](/definitions/compressible-velocity-transformation.md)
loses the mismatch; and a Mach 2.9 expansion–compression corner
([shock–boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md))
trained and predicted at two Reynolds numbers against the DNS of Fang et
al. (2015), where $C_f$, separation length, reattachment and the Stanton
peak improve. A model trained on both flows improves the corner less; the
author concludes that the training set is far from representative. The
solver switches a skew-symmetric low-dissipation scheme to a
shock-capturing one with the Ducros [sensor](/definitions/shock-sensor.md).
The evidence is comparison of plotted curves; no error norms are tabulated.

# Version read

Version of record (AIP; submitted 23 September 2021, accepted
12 November 2021, online 3 December 2021): 14 PDF pages, an AIP cover page
plus article pp. 126103-1 to -13, all read, the equation and reference
pages visually. Page 1 matches the metadata (single author, Lawrence
Technological University); no identity issue. Equation, table and figure
numbers are those of this version.

# Key claims

Page-local symbols: $q_w$ wall heat flux; $\tau_w^e$, $q_w^e$ the
discrepancies of the baseline wall values against the reference, the
regression targets; $\tau_w^{\mathrm{rfr}}=\tau_w^{\mathrm{wmles}}+\tau_w^e$
the corrected value; $\upsilon_1,L_1$ and $\upsilon_2,L_2$ the two
characteristic velocity and length scales; $\Delta$ the stencil spacing,
$h_s=2\Delta$ the stencil-centre wall distance; $K_{\mathrm{rf}}$ the
number of trees; $C_h$ the Stanton number (registry §11; the source's
$St$; the registry's $St$ is the Strouhal number).

1. Log-layer mismatch in hybrid RANS/LES and DES-type wall modelling gives skin friction "on the order of 15% too low" (citing Nikitin et al. 2000); Gieseking et al. reported about 25% under-prediction with IDDES in supersonic boundary layers (§I). **Stated**
2. IDDES does not remove the mismatch: Peterson & Candler attributed it in supersonic boundary layers to IDDES calibration on low-speed channels, Mockett et al. found it in low-speed channel IDDES too and suggested numerical sensitivity; "a concrete explanation for the problem of the IDDES model has remained elusive" (§I). **Stated**
3. "To date, no modification for WMLES has been tested on supersonic flows with separation and reattachment" (§I). **Stated**
4. Since velocity, density and temperature at the matching location are passed from the LES to the RANS layer, the resolved part is the same in both, and the discrepancy in total shear stress and heat flux there "arises due to the discrepancies between $\mu_{t,LES}$ and $\mu_{t,RANS}$ and also $Pr_{t,LES}$ and $Pr_{t,RANS}$" (§II C). **Stated** (argued, not derived)
5. Because the wall model takes the under-resolved instantaneous LES solution at the matching location as input, "even a perfect wall model would not be able to accurately predict skin friction" (§II C). **Stated**
6. Inputs and outputs must be non-dimensional and Galilean invariant; velocities relative to the wall and velocity differences (Eqs. 8–10) satisfy Galilean invariance (§II E). **Stated**
7. The seven-point stencil (from Lozano-Durán & Bae) lets the model "differentiate between different types of flow, such as separation zones and mean flow three-dimensionality" (§II E). **Stated**
8. Random-forest regression "has robust performances with only a small set of training parameters", unlike neural networks (§II F). **Stated**
9. The out-of-bag error stabilised at 300 trees, and $K_{\mathrm{rf}}=300$ is used (§II G). **Shown** (not plotted)
10. Flat plate: the corrected mean velocity profile is "almost identical to the experimental result", with a log region in $30<y^+<3000$ "without showing LLM"; the baseline IDDES has the right log slope but a higher intercept, hence a lower skin friction (§III A 1, Fig. 6). **Shown**
11. Flat plate: baseline Reynolds stresses normalized by $\tau_w$ are too high, "primarily because of the lower wall shear stress given by the IDDES model"; the correction captures the near-wall peak at $y/\delta\le0.1$ and nearly overlaps experiment for $y/\delta\le0.5$; the shear-stress peak improves but stays under-predicted (§III A 1, Fig. 7). **Shown**
12. Flat plate: mean temperature and temperature fluctuations improve "significantly" (Fig. 8). **Shown**
13. Flat plate barycentric map: the experiment is two-component near the wall, tends to isotropy outward and approaches one-component near the edge; the baseline captures this "to some extent" but turns isotropic outside the edge; the corrected anisotropy is "significantly improved" (Fig. 9). **Shown**
14. Corner: the baseline under-predicts $C_f$ on plate and ramp and the separation plateau; the correction improves the separation length, and the mean reattachment point "compares favorably" with DNS (§III B 1, Fig. 10). **Shown**
15. Corner: $C_h$ turns negative through the expansion, peaks just downstream of reattachment and recovers more slowly than $C_f$; baseline–DNS differences lie mainly downstream of the compression corner; the correction improves the peak and the ramp heat flux (Fig. 11). **Shown**
16. Corner: a λ-shock forms at the compression corner; the recirculation size is "more correctly predicted" with the correction (Fig. 12), and so is the spanwise spacing of Görtler-type convergence lines near reattachment (Figs. 13–14). **Shown**
17. Corner: mean velocity and temperature on eight sampling lines agree better with DNS after correction, especially in the separation region; the baseline recovers temperature faster in the bubble with a larger $|C_h|$; "The RFR model improves the heat flux by correcting the turbulent Prandtl number in the separation region" (§III B 2, Figs. 15–17). **Shown**
18. Corner: Reynolds normal and shear stresses are suppressed by the expansion and amplified downstream of the compression corner, with maxima near reattachment in mid-boundary layer; corrected fields agree better with DNS near separation and reattachment (Fig. 18). **Shown**
19. A model trained on both flows still reduces the $C_f$ under-prediction and corrects reattachment on the corner, but less than the corner-only model; the $C_h$ peak is not well predicted, though better than the baseline (§III C, Fig. 19). **Shown**
20. The training set "is far from being representative of the rich flow physics"; a generalizable model needs a broader set of supersonic flows (Abstract, §III C, §IV). **Stated**
21. The in-house finite-volume solver uses a skew-symmetric collocated second-order low-dissipation scheme in turbulent regions, switched by the Ducros sensor to a "semi-discrete, central difference scheme" at discontinuities, with "the original implicit Euler scheme" in time (§II D). **Stated**

# Printed slips

- **§I:** "Peterson and Candler$^7$ reported…" and "Peterson and Candler$^7$ concluded…" cite ref. 7, which is Mockett, Fuchs & Thiele (2012); Peterson & Candler is ref. 9.
- **§II B:** "the shear stress tensor (SST)-based IDDES model", while the cited ref. 36 is titled "…the k-ω shear stress transport model".
- **Eq. (6):** the advection term of the $\rho k$ equation is printed $\nabla\cdot(\rho\vec U\omega)$, with $\omega$.
- **Eq. (5):** the cross-diffusion term is printed $2(1-F_1)\rho\sigma_\omega\times2\frac{\nabla k\cdot\nabla\omega}{\omega}$, with a factor 2 on each side of a line break.
- **Eq. (4):** the convective term is printed $(\bar\rho\tilde e+\bar p)\frac{\partial\tilde u_j}{\partial x_j}$. *(Compiler check, not in the sources: with the conservative time derivative $\partial(\bar\rho\tilde e)/\partial t$ the term in conservation form is $\partial[(\bar\rho\tilde e+\bar p)\tilde u_j]/\partial x_j$; the printed term omits $\tilde u_j\,\partial(\bar\rho\tilde e+\bar p)/\partial x_j$.)*
- **Eqs. (3)–(4):** the molecular stress is printed $\mu\tilde S_{ij}$ while the SGS closure is $\tau_{ij}=-2\mu_t\tilde S_{ij}$ with the same $\tilde S_{ij}$.
- **§II C:** $q_w=-C_p\big(\frac{\mu_t}{Pr_t}+\frac{\mu}{Pr}\big)\times\frac{\partial T}{\partial x_j}$, a wall quantity with a free index $j$.
- **Eqs. (8)–(10):** $\delta_iu_j$ is typeset as $\frac{(u_i^{e_i}-u_i^{-e_i})}{2\Delta}$, index $i$ on $u$ where the left side carries $j$; Eq. (11) writes $\tilde S_i^0$, $\tilde\Omega_i^0$ with one index for the two-index tensors of Eqs. (9)–(10).
- **Eq. (12):** the target is the error $\tau_w^e$, but the split criterion squares $\tau_{wj}^{dns}-\overline\tau^e_{w1;f^j}$, the reference wall stress minus the region-mean error; the second sum drops the subscript $w$.
- **§II F against §II G:** the forest prediction is "the unweighted average over the collection" in §II F and "the weighted vote from each individual tree" in §II G; §II G also speaks of class weights penalizing "misclassifying the minority class" for a regression model.
- **§II E:** the canonical building blocks are "turbulent channel flows and turbulent boundary layers (TBL) with separation", but no channel flow is used.
- **Case 1 Reynolds number:** $Re_\delta=617\,000$ in §III and Table I, "617 300" twice in §III A 1; §III B 1 prints "Re = 19 983.8" and "Re = 40 934.2" without subscript.
- **Case 1 grid:** "a uniformly spaced grid $y^+=1.7$ from $y=1.4$ to $3\delta$", as printed.
- **Figs. 10–11 legends:** "DNS (Fang et al. [50])", but Fang et al. is ref. 52 (ref. 50 is Bylander 2002).
- **Fig. 9 caption:** "Barycentric map of Reynolds stress of." (truncated).
- **Training Reynolds numbers:** "low Reynolds numbers" (§IV) against "both at medium Reynolds number" (§I).
- **Reference list:** ref. 5 prints "K. Soshi and L. Johan" (cited in the text as "Kawai et al."); ref. 16 "K. Lyea, S. Mishraa, and D. Rayb"; ref. 24 "J. Wu, J. Xiao, and E. Paterso"; ref. 44 the single author "J. T. J. Ling"; ref. 54 "D. Graaff"; the title of ref. 47 (Aldrich, Minerals 2020) begins with the title of ref. 18, and ref. 47 is the citation for "Developed in the 1990s, random forest".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar{(\cdot)}$, $\tilde{(\cdot)}$ | $\bar\phi$, $\tilde\phi$ | LES filter, Favre filter; in §II E $\bar p$, $\bar T$ are mean values, in §III B 2 $\langle u\rangle$ time means |
| $\tau_{ij}=\bar\rho\widetilde{u_iu_j}-\bar\rho\tilde u_i\tilde u_j$ | $\tau_{ij}$ (compressible form) | positive trace; agrees |
| $\tilde S_{ij}$ (Eq. 4) | $\tilde S^d_{ij}$ | printed deviatoric |
| $\tilde S_{i,j}$, $\tilde\Omega_{i,j}$ (Eqs. 9–10) | (stencil velocity-difference tensors, page-local) | **collision:** same letters as the strain and rotation tensors |
| $\tilde u_i^0$, $\delta_iu_j$ | (page-local) | velocity relative to the wall at the stencil centre; central difference over $2\Delta$ |
| $\Delta$, $h$ | $\Delta$ (stencil spacing), $h_s$ (page-local) | **collision:** the registry's $h$ is the cell size |
| $q_j$ | (SGS heat flux, page-local) | |
| $\lambda$ (Eq. 4), $\kappa$ (§II E) | (thermal conductivity) | **collision:** not the Taylor microscale, not the von Kármán constant |
| $k$, $\omega$, $F_1$, $F_2$, $\sigma_k$, $\sigma_\omega$, $a_1$ | same | SST; values not printed |
| $\alpha$, $\beta$ (Eq. 5) | $\gamma_\omega$, $\beta_\omega$ | **collision:** not the DG blending factor or the field-inversion multiplier |
| $\beta$ (§III B) | (ramp angle, 25°) | **collision** |
| $S$ (Eq. 7) | $\lvert S\rvert$ | definition not printed |
| $l_{IDDES}$, $l_{RANS}$, $l_{LES}$, $f_B$, $f_e$ | (IDDES length scales and functions, page-local) | Eq. (1) |
| $\tau_w^e$, $q_w^e$, $\tau_w^{rfr}$, $\tau_w^{wmles}$ | same (page-local) | |
| $\upsilon_1,L_1$, $\upsilon_2,L_2$ | same (page-local) | **collision:** $L$ is not the integral scale |
| $h(\mathbf x,\theta_k)$, $K$, $\Omega_m$, $M$ | (tree predictor), $K_{\mathrm{rf}}$, (feature-space regions) | **collision:** $\Omega_m$ is not the rotation tensor, $M$ not the Mach number |
| $Re_\delta$, $Re_\theta$, $\delta$, $\delta_{ref}$ | $Re$ on $\delta$, $Re_\theta$, $\delta$, $\delta_r$ | |
| $x^+$, $y^+$, $z^+$ (spacings) | $\Delta x^+$, $\Delta y^+$, $\Delta z^+$ | |
| $C_f=\tau_w/(\frac12\rho_\infty u_\infty^2)$, $St=q_w/(\rho_\infty u_\infty C_p(T_w-T_r))$, $T_r$ | $C_f$, $C_h$ (Stanton number, registry §11), recovery temperature | **collision:** the source's $St$ is the Stanton number; the registry's $St$ is the Strouhal number |

# Reference list

59 printed references, numbered (superscript) AIP style with titles. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Refs. 1 and 32 print the same work (Lozano-Durán &
Bae 2020, CTR brief) and both map to the bibliography's `lozanoduran-2020-e` (the CTR brief; `lozanoduran-2020-b` is its arXiv preprint). Ref. 39 (Zangeneh, J. Fluids Eng. 143:024504, 2021)
is a different work printed under this Source's key and is keyed `zangeneh-2021-b`, and ref. 42 (Zangeneh, AIAA J. 59, 2021) `zangeneh-2021-c`. The garbled author
names of refs. 5, 16, 24, 44 and 54 are listed under Printed slips; ref. 5
is keyed from the in-text "Kawai et al.". No item is unparseable.

# Pages created or updated

Chunk 9 (2026-10-27), cited further in chunk 12. This source is cited on:

- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Barycentric anisotropy map](/definitions/barycentric-anisotropy-map.md)
- [Compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Machine-learning wall models](/methods/machine-learning-wall-model.md)
- [Non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
