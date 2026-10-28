---
type: Source
title: "Diez Sanhueza et al. (2023) — Machine learning for RANS turbulence modeling of variable property flows"
description: "Field inversion and machine learning for the semi-locally damped Myong–Kasagi k-ε model in channels with strong property variations: multipliers on the dissipation terms, a momentum bold-drive optimizer, a logarithmic-neuron network and a weighted relaxation filter cut held-out velocity errors over thirty DNS cases."
resource: "doi:10.1016/j.compfluid.2023.105835"
source_kind: paper
authors: [Diez Sanhueza R., Smit S.H.H.J., Peeters J.W.R., Pecnik R.]
year: 2023
venue: "Comput. Fluids 255:105835"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Computers_amp_Fluids_Sanhueza_Machine_learning_for_RANS_turbulence_modeling_of_variable_pr.pdf"
tags: [rans, data-driven, field-inversion, neural-network, compressible, channel-flow]
timestamp: 2026-10-28T02:16:00Z
---

# Summary

Diez Sanhueza et al. (2023) apply [field inversion and machine learning](/methods/field-inversion-machine-learning.md)
to the low-Reynolds Myong–Kasagi [$k$-$\varepsilon$ model](/methods/k-epsilon-model.md)
in the form of Otero Rodriguez et al., whose damping functions use the
semi-local wall distance $y^*$ instead of $y^+$, for fully developed
[channel flows](/benchmarks/turbulent-channel-flow.md) with strong
variations of density and viscosity. The truth data are 30
[DNS](/definitions/direct-numerical-simulation.md) cases: 16 low-Mach
heated channels with prescribed property laws, nine supersonic
ideal-gas channels of Trettel & Larsson (Mach 0.7–4) and five
incompressible channels ($Re_\tau=180$–4200). The mean equations use the
[Boussinesq closure](/definitions/boussinesq-hypothesis.md), the strong
Reynolds analogy and $Pr_t=1$, and the authors state that
[Morkovin's hypothesis](/definitions/morkovin-hypothesis.md) holds for
all variable-property cases; the semi-local scaling of
[compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
is the frame of the features.

The inversion multiplies the **dissipation** terms of the $k$ and
$\varepsilon$ equations (not the production, as in Parish & Duraisamy),
and its cost regularizes the additive corrections
$\delta_k=D_k(\beta_k-1)$, $\delta_\varepsilon=D_\varepsilon(\beta_\varepsilon-1)$
normalized by the largest budget term. A bold-drive gradient descent with
momentum ran over 450 inversions; the gradients come from a discrete
adjoint with SymPy-generated Jacobians. A 77-parameter network with three
logarithmic neurons in its first layer predicts $\delta_k$ from 14
features, and a "weighted relaxation factor" filters the prediction by a
regularized least-squares fit to the production term before it is
injected into the solver, which re-evaluates $\rho$ and $\mu$ from an
equation of state ([a posteriori](/definitions/a-priori-and-a-posteriori-testing.md)
use). In ten K-fold trials the $L^\infty$ error of the mean velocity
drops in almost all held-out cases, from 23.4% to 4.0% in the hardest;
the worst case is the extrapolation to $Re_\tau=4200$ (2.3% to 14.0%).
The max–min envelope over the trials is presented as an uncertainty
estimate ([model-form uncertainty](/definitions/model-form-uncertainty.md)).
Integrated gradients rank the eddy viscosity as the most important
feature.

# Version read

Version of record (Comput. Fluids 255:105835, Elsevier, open access CC
BY; received 29 Apr 2022, accepted 15 Feb 2023, online 17 Feb 2023), 13
pages, all read; Tables 1–2, Eqs. (23)–(29) and Figs. 4, 8–10 checked
visually. Page 1 prints the first author "Rafael Diez Sanhueza"; the
running head prints "R.D. Sanhueza et al." and Crossref gives
"Sanhueza R.D.". The authors are recorded as page 1 prints them; the slug
keeps the Crossref form. Title, venue and DOI match the metadata.
Numbering on this page is that of this version.

# Key claims

The source's channel half-width $h$ is the registry's $\delta$; its star
denotes semi-local scaling, $Re_\tau^*=\sqrt{\langle\rho\rangle/\rho_w}\,(\mu_w/\langle\mu\rangle)\,Re_\tau$
(Eq. 1) and $y^*=y^+\sqrt{\rho/\rho_w}\,\mu_w/\mu$ (Eq. 8), as in the
registry; its $u^*$ is the DNS velocity, written $u_{\mathrm{DNS}}$. Its
budget terms are $P_k=\mu_t(\partial_yu)^2$, $D_k=\rho\varepsilon$, $T_k$
(diffusion), and likewise for $\varepsilon$; $\mu_t$ is the dynamic eddy
viscosity.

1. Turbulence models developed for isothermal incompressible fluids can be inaccurate for flows with strong property variations (supercritical fluids, hypersonic flows) (§1.1). **Stated** (cited)
2. Under small property fluctuations the turbulence changes are governed by wall-normal gradients of $Re_\tau^*$ (citing Patel et al.); the Patel et al. velocity transformation is "equivalent to the one proposed by Trettel and Larsson" (§1.1). **Stated**
3. Morkovin's hypothesis applies to all variable-property DNS cases of the database (§2.1). **Stated** (cited)
4. The baseline model with DNS density and viscosity profiles deviates strongly in variable-property flows, most in JFM.CRe$^*_\tau$, where "the maximum error margin reaches a magnitude of 22.8% at the channel center" (§2.2, Fig. 1). **Shown** (see Printed slips)
5. $Pr_t=1$ in all cases; a detailed analysis showed $Pr_t\approx1$ in the buffer layer of the supersonic cases, and Patel found the same for the low-Mach cases (§2.2). **Stated**
6. The multipliers act on the dissipation terms, $P_k-\beta_kD_k+T_k=0$ and $P_\varepsilon-\beta_\varepsilon D_\varepsilon+T_\varepsilon=0$ (Eqs. 9–10), "in order to adhere to energy conservation" (production appears with opposite sign in the mean kinetic-energy equation) and because production is active in a smaller region of the boundary layer (§3.1). **Stated**
7. A $\beta_k$ in the $k$ equation can unbalance production and dissipation in the log layer, so results with $\beta_\varepsilon$ alone are also given (§3.1). **Stated**
8. The Hessian of the inversion is non-invertible at the channel centre (vanishing gradients near the symmetry plane), so gradient descent is used, which leaves $\beta$ near the centre at its initial value 1 (§3.1.1). **Stated**
9. The bold-drive optimizer with momentum (Algorithm 1; expansion and contraction ratios 1.2 and 0.5, momentum 0.9) "decreased the running times by a factor three with respect to the original bold drive method" and ran over 450 inversions automatically (§3.1.1, §6). **Shown** (no timings printed)
10. The discrete adjoint (Eqs. 17–18) avoids the sensitivity matrix of the state with respect to $\beta$; explicit SymPy formulas make the Jacobian assembly sparse-efficient (§3.1.2). **Stated**
11. Hyper-parameters, the weight-regularization coefficient of the loss (Eq. 19) included, are set by the elbow method on training data only, so the cases outside the training set are "purely held-back test cases" (§3.2, §3.2.1). **Stated**
12. $L^2$ regularization of the weights makes feature-importance rankings "more consistent" (§3.2). **Stated**
13. The weighted relaxation factor (Eqs. 20–29: $\delta_{\mathrm{ML}}=\beta_PP$ fitted to the raw prediction with a penalty $\lambda_\delta\beta_P^2$, $\lambda_\delta$ fixed by $\|\delta_{\mathrm{ML}}\|=\alpha_r\|\delta_{\mathrm{ini}}\|$ through Newton–Raphson, giving $\delta_{\mathrm{ML}}=\delta_{\mathrm{ini}}P^2/(\lambda_\delta+P^2)$) filters a synthetic perturbation $0.6\,y^3\sin(8\pi y)$ added to the inverted correction of JFM.CRe$^*_\tau$ and recovers a distribution resembling the hidden one (§3.2.2, Fig. 2). **Shown**
14. The final network has three logarithmic neurons in the first layer and 77 trainable parameters, the smallest able to fit the training data of trial K-1 (§3.2.1, §3.3, Fig. 4). **Stated**
15. The elbow method gives clear inflection points of the velocity error against the velocity weight; a common weight of 100 is chosen for all cases (§4, Fig. 5). **Shown**
16. Different weights of the $\delta_k$ and $\delta_\varepsilon$ penalties, and even inversions with only $\delta_k$ or only $\delta_\varepsilon$, give corrections of similar shape with different peaks, in all cases (§4, Fig. 6). **Shown**
17. Maximum corrections of the low-Mach cases are up to 4.5 times those of the incompressible cases; for some low-Mach cases $\delta_k$ is almost entirely positive (§4, Fig. 7). **Shown**
18. $\delta_\varepsilon/S_\varepsilon$ has gradients up to 83.5% higher than the maximum gradients of $\delta_k/S_k$ ($S$ the largest budget term), so the learned system predicts $\delta_k/S_k$ only (§4). **Shown**
19. The relaxation factor $\alpha_r=0.95$ gave stable predictions in all cases "without modifying the $\delta$ corrections significantly" (§5). **Shown**
20. The learned correction reduces the $L^\infty$ velocity error in almost all held-out cases (Table 3); best, JFM.CRe$^*_\tau$ in K-1, 23.4% to 4.0% (abstract, §5). **Shown**
21. The worst prediction is IC.Re4200 in K-8, 2.3% to 14.0%, explained as extrapolation (highest $Re_\tau=4200$, nearest training case 2000, "2.1 times lower"); JFM.LL in K-3 (4.8% to 5.8%) and IC.Re2000 in K-6 (2.4% to 2.5%) are also slightly worse (§5, Table 3). **Shown**
22. In the six trials holding out JFM.CRe$^*_\tau$ (K-1, K-2, K-3, K-4, K-7, K-10) all predictions beat the baseline (Fig. 9); the conclusions state a baseline 23.4% against "an average error of only 6.2%" (§5, §6). **Shown** (see Printed slips)
23. Integrated gradients (Eq. 31) rank $\mu_t/\mu_w$ as the most important feature; $\rho/\rho_w$ and $\mu/\mu_w$ rank low because their variation is carried by $y^*$, "in agreement with" Otero Rodriguez et al. (§5, Fig. 10). **Shown**
24. The learned system "acts as an excellent non-linear interpolator" between well-represented cases, and the coupled solver "remained stable during all the cases tested" (abstract, §6). **Shown**
25. The methodology improves RANS models in variable-property flows "without introducing prior modeling assumptions into the system" (abstract). **Stated**

# Printed slips

- **§2.2 against Table 3:** the baseline error of JFM.CRe$^*_\tau$ is printed "22.8% at the channel center ($y=H$)" in §2.2 and 23.4% in Table 3, the abstract and §6; the channel half-width is $h$ elsewhere.
- **§4 against Fig. 6:** the text discusses Fig. 6 "for the DNS case CRe$^*_\tau$, which corresponds to the case with the highest modeling errors", while the caption says "considering the DNS case JFM.CRe$^*_\tau$", the case §2.2 and §5 name as the highest-error one.
- **§6:** "an average error of only 6.2%". *(compiler check, not in the sources)* The Table 3 errors of JFM.CRe$^*_\tau$ in the six trials listed in the Fig. 9 caption (4.0, 6.3, 5.2, 10.2, 4.2, 8.6) average $38.5/6\approx6.42\%$; the paper does not say how its average was formed.
- **Eqs. (9), (12) against §3.3:** *(compiler check, not in the sources)* from Eqs. (9) and (12), $P_k-\beta_kD_k+T_k=P_k-D_k-\delta_k+T_k$, so the inverted $\delta_k$ enters the $k$ equation with a minus sign, while §3.3 says the corrections are inserted "as an explicit source term ($+\delta_{ML}(y)$)".
- **Eq. (11):** the sum $\sum_{i=1}^N$ precedes all three terms, but $\delta_k$ and $\delta_\varepsilon$ carry no index $i$.

# Notation map

| Diez Sanhueza et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| bar (Eq. 1) | $\langle\cdot\rangle$ | Reynolds average; dropped elsewhere |
| $u$ | $\langle u\rangle_\rho$ | Favre-averaged streamwise velocity |
| $u^*$ | $u_{\mathrm{DNS}}$ (page-local) | **collision:** the star is the DNS value here, semi-local scaling elsewhere |
| $h$, $y=H$ | $\delta$ | channel half-width |
| $Re_{\tau,w}$ | $Re_\tau$ | wall-based friction Reynolds number |
| $Re^\star_\tau$, $y^\star$ ($Y^\star$) | $Re_\tau^*$, $y^*$ | semi-local scaling, agree |
| $u_{\tau,w}$ | $u_\tau$ | |
| $\rho,\mu,c_p$, subscript $w$ | $\rho,\mu,c_p$, wall values | non-dimensionalized by wall values |
| $\lambda$ (conductivity) | $\lambda_{\mathrm{th}}$ (page-local) | **collision** with the Taylor microscale $\lambda$ |
| $\lambda$ (Eq. 19), $\lambda$ (Eq. 23) | $\lambda_{\mathrm{reg}}$, $\lambda_\delta$ (page-local) | two different regularization weights under one symbol in the source: of the network weights, and of the relaxation fit (as on the field-inversion page) |
| $Pr_w$, $Pr_t$, $Ec_{\tau,w}$, $Ma_{\tau,w}$ | $Pr$ at the wall, $Pr_t$, (friction Eckert number), $M_\tau$ | page-local |
| $\phi$ | (volumetric heat source) | page-local |
| $k$, $\varepsilon$, $\mu_t$ | $k$, $\varepsilon$, $\mu_t$ | agree; $\mu_t=C_\mu f_\mu\rho k^2/\varepsilon$ |
| $P_k$, $D_k$, $T_k$ | (production $\mu_t(\partial_yu)^2$, destruction $\rho\varepsilon$, diffusion) | density-weighted form of the registry $P_k$ |
| $C_{\varepsilon1}$, $C_{\varepsilon2}$, $C_\mu$, $\sigma_k$, $\sigma_\varepsilon$, $f_\varepsilon$, $f_\mu$, $Re_t$ | as printed | Myong–Kasagi constants 1.4, 1.8, 0.09, 1.4, 1.3 |
| $\beta_k$, $\beta_\varepsilon$ | $\beta(\boldsymbol x)$ with subscripts | field-inversion multipliers, on the dissipation terms |
| $\beta$ (Eqs. 22–26) | $\beta_P$ (page-local) | multiplier of production in the relaxation filter; **collision** with the inversion $\beta$ |
| $\delta_k$, $\delta_\varepsilon$, $\delta_{FI}$, $\delta_{NN}$, $\delta_{ini}$, $\delta_{ML}$ | $\boldsymbol\delta$ components (inverted, network, raw, relaxed) | **collision** with the boundary-layer thickness $\delta$ |
| $S_U$, $S_k$, $S_\varepsilon$, $M_k$, $M_\varepsilon$ | (normalization scales) | page-local |
| $I_U$, $I_k$, $I_\varepsilon$, $\mathcal J$ | (cost weights, inversion cost) | page-local |
| $\mathcal R$, $W$, $\Psi$ | (residual, discrete state, adjoint vector $\boldsymbol\Psi_{\mathrm{adj}}$) | **collision** with the Jameson sensor $\Psi_i$ |
| $\alpha$ | $\alpha_r$ (relaxation factor, page-local) | also the learning rate and the integrated-gradients path variable; **collision** with the DG blending factor $\alpha$ |
| $k^+$, $k^-$, $c$, $m$ | (bold-drive ratios, momentum constant and vector) | **collision** with wall units and the TKE |
| $X_f$, $X_i$, $w_j$ | $\boldsymbol\zeta$, $\zeta_i$, $\boldsymbol\theta$ | features; network weights |
| $\mathcal L_{train}$ | $\mathcal L$ | loss |

# Reference list

41 printed references, numbered style ([1]–[41]); abbreviated page
ranges are expanded. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ref. [1] prints
its authors "Rodriguez GJO … S. RD" and is the Otero Rodriguez et al.
(2018) work already in the bibliography under the Otero Rodriguez key;
ref. [27] (the RANS channel code) prints the same author forms. Cited works
sharing a first-author-year key with different works already in the
bibliography (He 2008, Chang 2018, Jiménez 2008, Singh 2017) are keyed
apart at the merge. Ref. [9] (Morkovin 1961) is printed without a book
title. No printed duplicate, no unparseable item.

# Pages created or updated

Chunk 12 (2026-10-28). This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Morkovin's hypothesis and Reynolds analogies](/definitions/morkovin-hypothesis.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [k-ε models](/methods/k-epsilon-model.md)
