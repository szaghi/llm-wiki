---
type: Source
title: "Oulghelou et al. (2025) — Machine-Learning-Assisted Blending of Data-Driven Turbulence Models"
description: "Blends sparse symbolic corrections of the k-ω SST model inside the RANS equations, with space-dependent weights predicted by a random forest from baseline-flow features, and tests the blend against its expert models on training flows and on a flat plate, the NASA hump and the NACA 0012."
resource: "doi:10.1007/s10494-025-00661-8"
source_kind: paper
authors: [Oulghelou M., Cherroud S., Merle X., Cinnella P.]
year: 2025
venue: "Flow Turbul. Combust. 115:1095-1132"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Flow_Turbulence_and_Combustion_Oulghelou_Machine-Learning-Assisted_Blending_of_Data-Driven_Turbulence.pdf"
tags: [rans, data-driven, symbolic-regression, separated-flow, uncertainty-quantification]
timestamp: 2026-10-26T15:38:00Z
---

# Summary

Oulghelou et al. (2025) propose an internal blending of data-driven
corrections of the [k-ω SST model](/methods/k-omega-sst-model.md)
([aggregation of turbulence models](/methods/turbulence-model-aggregation.md)).
Each "expert" is a sparse
[symbolic-regression correction](/methods/symbolic-regression-closure.md)
trained with SBL-SpaRTA on one flow class. Each correction is written on the
[integrity basis](/methods/tensor-basis-neural-network.md) and added to the
[Boussinesq](/definitions/boussinesq-hypothesis.md) anisotropy. The experts'
anisotropy corrections and their $k$-equation corrections are combined as
convex sums inside the RANS equations, with space-dependent weights
$w_M(\boldsymbol x)$. The resulting field is a RANS solution and needs one
corrected run. By contrast, the authors' earlier external aggregation (XMA)
mixes the solutions of $N_M$ runs. The internal version gives up XMA's natural
uncertainty estimate ([model-form uncertainty](/definitions/model-form-uncertainty.md)).

There are three experts:
- the baseline SST, for attached wall flows;
- a separated-flow expert, trained on the [periodic hill](/benchmarks/periodic-hill.md),
  a converging–diverging channel and the curved
  [backward-facing step](/benchmarks/backward-facing-step.md);
- a jet expert, trained on PIV of an axisymmetric near-sonic jet.

The weights are fitted in two steps. Target weights on the training data are
Gaussian kernels of each expert's streamwise-velocity error. A random forest
then maps eleven features of the baseline SST solution to those weights. The
experts' targets come from frozen RANS, and the blend is assessed inside the
solver ([a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md);
the corrections family is that of
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)).

On the training flows the blend selects the right expert locally. On the
[channel](/benchmarks/turbulent-channel-flow.md) it reproduces SST, where the
other experts break the [law of the wall](/definitions/law-of-the-wall.md). On
the separated cases its errors are lowest or close to lowest. Three unseen
cases were also run:
- the zero-pressure-gradient [boundary layer](/benchmarks/turbulent-boundary-layer.md):
  the blend is worse than SST but better than the other experts;
- the [NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md): the
  predicted bubble is within 0.01 of the experimental length;
- the [NACA 0012](/benchmarks/naca-0012-airfoil.md): lift and drag are close to
  SST, shown only in plots.

All runs are 2D and steady, in a modified [OpenFOAM](/software/openfoam.md).
Lozano-Durán & Bae's classifier-based
[building-block-flow wall model](/methods/building-block-flow-wall-model.md) is
cited as a related internal approach.

# Version read

arXiv:2410.14431v2 [physics.flu-dyn] (3 March 2025), 43 pages in the arXiv
layout, all read. Pages 6, 7, 9, 10, 35 and 36 were checked visually. It is not
the journal's version of record, which runs to 38 pages (1095–1132). Page 1
prints "Machine-learning-assisted Blending", which differs from the published
title only in capitalization. The authors match, with Oulghelou and Cherroud
marked as equal contributors, and there is no identity problem. Section,
equation, table and figure numbers on this page are those of arXiv v2.

# Key claims

Page-local symbols: $b^\Delta_{ij}$ is the additive anisotropy correction.
$b^R_{ij}$ is the tensor of the $k$-equation correction $R_k=2k\,b^R_{ij}\partial_j\langle u_i\rangle$.
$\mathcal M=\{M_{SST},M_{SEP},M_{ANSJ}\}$ is the set of experts and $M_{blend}$
the blended model. $w_M$ is the weight of expert $M$, and $\sigma$ the
bandwidth of the Gaussian kernel. $L$ is the reference length of each case
(Tables 5, 8). Lengths in Tables 6 and 11 are in $x/L$.

1. Internal blending of expert corrections yields fields that are solutions of the RANS equations, unlike external aggregation, whose fields "are in general not a solution of the governing equations". It costs one simulation instead of $N_M$ (§1, pp. 3–4; §3, p. 9). **Stated**
2. Internal blending "does not deliver estimates of the predictive uncertainty as naturally as the external model aggregation" and is "no longer an uncertainty quantification method" (§1, p. 4; §3, p. 9). **Stated**
3. Data-driven corrections trained on narrow flow classes "do not generalize to radically different flows, and often deteriorate the representation of canonical flows". Multi-flow training "may lead to a soft compromise solution" [31] (§1, pp. 2–3). **Stated**
4. The separated-flow expert ($b^\Delta_{ij}=5.21\,T^{(2)}_{ij}$, $b^R_{ij}=0.681\,T^{(1)}_{ij}$) raises the eddy viscosity and deviates in the channel log layer (mean absolute error of $u^+$ 2.41, against 0.44 for SST). The jet expert ($b^\Delta_{ij}=0.25\,T^{(1)}_{ij}$) "tends to strongly reduce the eddy viscosity of the baseline model to compensate for the so-called jet anomaly" and overpredicts the channel velocity (error 8.97) (§4.2.1, Table 3). **Shown**
5. On the channel at $Re_\tau=1000$ the blend gives the baseline a weight "very close to one throughout the channel height" and matches SST accuracy (error of $u^+$ 0.44 for both) (§4.2.1, Table 3, Fig. 4). **Shown**
6. Near-sonic jet, mean absolute error of the normalized velocity: jet expert 0.04, SST 0.09, separated-flow expert 0.16, blend 0.07. The weights are roughly equal at the jet entrance, and the jet expert dominates downstream (§4.2.2, Table 4, Figs. 5–6). **Shown**
7. On the periodic hill, the converging–diverging channel and the curved step, the separated-flow expert receives the highest weight in separated regions and SST in attached regions. The jet expert always receives low weights (§4.2.3, Figs. 7d, 8d). **Shown**
8. Separation-bubble lengths (Table 6). Periodic hill: LES 4.49, SST 7.42, separated-flow expert 4.15, blend 4.555. Converging–diverging channel: DNS 0.85, SST 3.41, separated-flow expert 0.83, blend 2.05. Curved step: LES 3.55, SST 3.59, separated-flow expert 2.51, blend 3.44. The jet expert gives 7.98, 6.65 and 5.52. **Shown**
9. Mean absolute errors on the separated training cases (Table 7). The blend has the lowest $C_f$ error on the periodic hill ($2.07\cdot10^{-3}$) and on the converging–diverging channel ($2.15\cdot10^{-3}$). On the curved step SST has the lowest $C_f$ error ($4.83\cdot10^{-4}$, against $5.05\cdot10^{-4}$ for the blend). On the hill velocity the separated-flow expert is lowest (0.06, against 0.09). The authors summarize that "the blended model generally outperforms the specialized models" (§4.2.3, Table 7). **Shown**
10. The converging–diverging channel has "a small separation bubble in the divergent that cannot be captured by RANS model, even after data-driven correction" (§4.2.3, p. 19). **Shown**
11. The random forest reaches $R^2=0.991$ on the 80% training split and 0.99 on the held-out 20%, and the histograms of the weight errors peak at zero (§3.1, Fig. 3). **Shown**
12. The features of the test cases lie largely inside the 95% covariance ellipses of the training features in PCA, t-SNE and autoencoder latent spaces. The NACA 0012 has outliers, "especially at higher angles of attack" (§5.1, Fig. 10). **Shown**
13. Flat plate (unseen), mean absolute error of $C_f$: jet expert $1.1\times10^{-3}$, SST $8.4\times10^{-5}$, separated-flow expert $3.7\times10^{-4}$, blend $1.7\times10^{-4}$. Error of $u^+$: 6.27, 0.42, 1.45 and 0.7. The blend beats the two corrected experts but not SST (§5.1.1, Table 9). **Shown**
14. On the flat plate, "contrary to expectations", SST does not dominate along $y^+$. The jet expert gains significant weight in the log region, which the authors read as weight shifts there having "little impact on the overall accuracy" (§5.1.1, Fig. 11c). **Shown** (interpretation **Stated**)
15. The weights "exhibit small oscillations, probably due to irregularity in the random forest regressor", which "do not appear to translate into oscillations in the numerical solution". Smoother regressors such as Gaussian processes are suggested (§5.1.1, p. 27; §3, p. 11). **Shown**/**Stated**
16. Wall-mounted hump (unseen): the bubble runs from $x/L=0.62$ to 1.15 (length 0.53) in the experiment [73]. The predictions are 0.62–1.24 (0.62) for SST, 0.62–1.03 (0.41) for the separated-flow expert, 0.62–1.7 (1.08) for the jet expert and 0.62–1.14 (0.52) for the blend (§5.1.2, Table 11). **Shown**
17. Hump mean absolute errors (Table 10), in the order jet expert, SST, separated-flow expert, blend. Velocity: 0.24, 0.06, 0.06, 0.04. $C_f$: $2.17\cdot10^{-3}$, $7.53\cdot10^{-4}$, $4.21\cdot10^{-4}$, $3.86\cdot10^{-4}$. $C_p$: 0.09, 0.03, 0.05, 0.04. The blend is lowest on two of the three metrics (§5.1.2). **Shown**
18. In the core flow of the hump "all weights tend to converge towards a value of 1/3", which the authors read as insensitivity of that region to the turbulence model (§5.1.2, Fig. 12d). **Shown** (interpretation **Stated**)
19. NACA 0012 ($Re=6\times10^6$, 0°–18°): the jet expert has the largest lift and drag discrepancies. "The $M_{SST}$ performs better than $M_{SEP}$ for most of the present flows, the latter model being too dissipative", so the separated-flow expert "should be replaced or supplemented with another expert model". The blend reproduces the "lift-curve slope, drag behavior, and surface-pressure profiles". No error table is printed for this case (§5.1.3, Figs. 15–16). **Shown** (plots only)
20. On the airfoil surfaces the jet expert receives minimal weight. The separated-flow expert gains weight in moderately separated suction-side regions, and SST in attached zones (§5.1.3, Fig. 16). **Shown**
21. Conclusions: the blend "outperforms the baseline $M_{SST}$ model in flow configurations where the baseline model struggles, and that are sufficiently close to the training flows", and "in certain cases" it "surpasses the best-performing individual expert models" (§6). **Shown** (summarizing Tables 3–11)
22. The additive correction $b_{ij}=b^0_{ij}+b^\Delta_{ij}$, "leaving the linear term unaltered, has the benefit of enhanced numerical stability" [47] (§2, p. 6). **Stated**
23. The posterior standard deviations of the SBL-SpaRTA coefficients are small relative to their means, so the coefficients are treated as deterministic (§3, p. 9, Table 1). **Stated** (values printed)
24. The input features are "by construction, bounded within -1 and 1 to improve generalizability" (App. A, p. 35). **Stated** (see Printed slips)
25. The procedure is not restricted to the $k$-$\omega$ SST model and can be extended to $k$-$\varepsilon$ variants, with the experts retrained (§2, p. 7). **Stated**

The blending law is (Eq. 11)
$$b^\Delta_{ij}=\sum_{M\in\mathcal M}w_M\,b^{\Delta,M}_{ij},\qquad b^R_{ij}=\sum_{M\in\mathcal M}w_M\,b^{R,M}_{ij},\qquad\sum_{M\in\mathcal M}w_M=1,$$
and the target weights on training data are
$w_L=\mathcal G(\delta^L,\bar\delta)/\sum_M\mathcal G(\delta^M,\bar\delta)$,
with $\mathcal G=\exp\big(-\lVert\delta^L-\bar\delta\rVert_2^2/(2\sigma^2)\big)$
(Eq. 12). Here $\delta^M$ is the expert's streamwise velocity and $\bar\delta$
the high-fidelity one, and $\sigma$ is chosen by grid search in
$\{1,\dots,10^{-4}\}$.

# Printed slips

- **Converging–diverging channel Reynolds number:** Table 1 (p. 9) gives "Re = 13600", while §4.2.3 (p. 17) and Table 5 give 12600.
- **Periodic-hill reference length:** Table 5 gives $L$ = "Hill height", and the Fig. 9 caption has "hill crest for PH", but the Fig. 7 caption reads "with L the channel half-height (full channel height = 2L)".
- **OpenFOAM version:** §4.1 has "OpenFoam v23-06 [57]", while ref. [57] reads "OpenFOAM Foundation … (2023). Version 10".
- **Weight symbol:** the exact-weight formula (p. 10) writes $\omega_L$, the rest of the paper $w_M$, and $\omega$ is also the specific dissipation rate.
- **Expert notation:** Table 1 writes $b^\Delta_R$ for the text's $b^R_{ij}$.
- **Feature bounds:** App. A says the features are "bounded within -1 and 1", while $\eta_3=\min(\sqrt k\lambda/(50\nu),2)$ is capped at 2 as printed, and $\lambda$ in $\eta_3$ is never defined.
- **$D_{jet}$:** the captions of Figs. 5 and 6 call it "the nozzle radius", and §4.2.2 gives "a radius of 1 inch".
- **Channel data:** §3.1 lists "RANS data for a turbulent channel flow at $Re_\tau=1000$" among the training data, while Fig. 4 compares with the DNS [58].
- **Section map:** the introduction places the training and test results in Section 4 and the conclusions in Section 5. The tests are subsections 5.1.1–5.1.3 of "5.1 Assessing training features coverage in the latent space", and the conclusions are Section 6.
- **Duplicate reference:** refs. [66] and [69] are the same t-SNE paper (van der Maaten & Hinton 2008).
- **Typos:** "Kroenecker", "bellow", "ansatzs", "instead than", "where calibrated", "Inspired to".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U_i$, $P$ | $\langle u_i\rangle$, $\langle p\rangle$ | capitals for the Reynolds average |
| $\overline U_x$ | (high-fidelity streamwise velocity, page-local) | **collision:** the overbar is not the LES filter |
| $\tau_{ij}=2k(b_{ij}+\tfrac13\delta_{ij})$, $\overline{u_i'u_j'}$ | $R_{ij}$ | positive semi-definite, kinematic; **collision:** $\tau_{ij}$ is the SGS stress in the registry |
| $a_{ij}=2kb_{ij}$, $b_{ij}$ | $2kb_{ij}$, $b_{ij}$ | agree |
| $b^0_{ij}=-\frac{\nu_t}{k}S_{ij}$ | $b_{ij}=-\nu_t\langle S_{ij}\rangle/k$ | Boussinesq anisotropy; agrees |
| $b^\Delta_{ij}$, $R_k$, $b^R_{ij}$ ($b^\Delta_R$ in Table 1) | (page-local) | additive corrections |
| $\alpha^\Delta_n$, $\alpha^R_n$ | $g^{(n)}$ | basis coefficients |
| $T^{(n)}_{ij}(S^*,\Omega^*)$, $I_1$, $I_2$ | $T^{(n)}$, invariants | normalized by $\omega$ ($S^*=S/\omega$), not $k/\varepsilon$; three tensors and two invariants in 2D |
| $S_{ij}$, $\Omega_{ij}=\tfrac12(\partial_jU_i-\partial_iU_j)$ | $\langle S_{ij}\rangle$, $\langle\Omega_{ij}\rangle$ | agree |
| $S=2S_{ij}S_{ij}$ | $\lvert S\rvert^2$ | **collision:** the source's $S$ is the squared magnitude |
| $\alpha_k$, $\alpha_\omega$ | $\sigma_k$, $\sigma_\omega$ | SST diffusion coefficients, (0.85, 1) and (0.5, 0.856) |
| $\gamma$ | $\alpha$ (as on the SST page) | (5/9, 0.44); **collision:** $\gamma$ is the ratio of specific heats in the registry |
| $\beta$, $\beta^*$, $a_1$, $b_1$, $c_1$ | $\beta$, $\beta^*$, $a_1$, $b_1$, $c_1$ | SST constants: $\beta=(0.075,0.0828)$, $\beta^*=0.09$, $a_1=0.31$, $b_1=1$, $c_1=10$; **collision:** this $\beta$ is not the field-inversion $\beta(\boldsymbol x)$ |
| $F_1$, $F_2$, $F_3$, $F_{23}$, $CD_{k\omega}$ | $F_1$, $F_2$, (page-local) | $F_3$ optional |
| $y$ ("blending function distance") | $d$ | wall distance |
| $\varepsilon$, $\epsilon$ | $\varepsilon$ | not defined in terms of $k$, $\omega$ in the source |
| $\eta_1$–$\eta_{11}$ | $\boldsymbol\zeta=(\zeta_1,\dots,\zeta_{11})$ | **collision:** $\eta$ is the Kolmogorov length in the registry |
| $w_M$, $\omega_L$ | $w_M$, $w_L$ (page-local) | **collision:** $w_i$ are quadrature weights and $\omega$ the specific dissipation rate in the registry |
| $\mathcal W$ | $f(\boldsymbol\zeta;\boldsymbol\theta)$ | feature-to-weight map (random forest) |
| $\lambda_i$, $\Sigma$, $\zeta$ (§5.1) | (latent-space eigenvalues, covariance, latent variables; page-local) | **collision:** $\lambda$ is the Taylor microscale and $\boldsymbol\zeta$ the features in the registry |
| $\kappa=0.41$, $B=5.2$ | $\kappa$, $B$ | log law of Figs. 4, 11 |
| $Re_\tau$, $y^+$, $U^+$ | $Re_\tau$, $y^+$, $u^+$ | agree |

# Reference list

83 printed references, numbered [1]–[83]. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Refs. [66] and [69]
are the same t-SNE paper printed twice and are folded into one entry. Ref. [17]
is the ingested [duraisamy-2019](/sources/duraisamy-2019.md), ref. [18]
[duraisamy-2021](/sources/duraisamy-2021.md) and ref. [38]
[lozanoduran-2023](/sources/lozanoduran-2023.md), printed as "963, 35".
Ref. [80] (Liu Z. et al., "Kan: Kolmogorov-arnold networks", arXiv:2404.19756)
received the printed key `liu-2024`, which belongs to a different ingested
work, and is re-keyed `liu-2024-b`. Odd printings are recorded as printed:
- [46] Menter 1992 "Technical report, A";
- [74] has the author "Resource, N.T.M." (the NASA TMR website);
- [57] has the corporate author OpenFOAM Foundation;
- [37] and [39] give article numbers without volumes;
- [28] and [33] give Physics of Fluids 35 with an issue but no article number;
- [47] and [79] are ASME Turbo Expo papers with page strings "02–41015" and
  "12–32023";
- [52] pairs volume 24 with the year 2001;
- [54] reads "Journal of Turbulence (13), 4".

No unparseable references.

# Pages created or updated

Chunk 6 (2026-10-26). This source is cited on:

- [Backward-facing step](/benchmarks/backward-facing-step.md)
- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md)
- [Periodic hill](/benchmarks/periodic-hill.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Building-block-flow wall model](/methods/building-block-flow-wall-model.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Symbolic-regression turbulence closures](/methods/symbolic-regression-closure.md)
- [Tensor-basis neural network and the integrity basis](/methods/tensor-basis-neural-network.md)
- [Aggregation and blending of data-driven turbulence models](/methods/turbulence-model-aggregation.md)
- [OpenFOAM](/software/openfoam.md)
