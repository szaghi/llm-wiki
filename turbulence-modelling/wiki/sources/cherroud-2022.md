---
type: Source
title: "Cherroud et al. (2022) — Sparse Bayesian Learning of Explicit Algebraic Reynolds-Stress models for turbulent separated flows"
description: "Introduces SBL-SpaRTA, a sparse Bayesian (demi-Bayesian LASSO) regression of integrity-basis corrections to k-omega SST that selects terms and returns posterior coefficient distributions; cross-validated a posteriori on periodic hill, converging-diverging channel and curved step, it favours a single stochastic production correction."
resource: "doi:10.1016/j.ijheatfluidflow.2022.109047"
source_kind: paper
authors: [Cherroud S., Merle X., Cinnella P., Gloerfelt X.]
year: 2022
venue: "Int. J. Heat Fluid Flow 98:109047"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_International_Journal_of_Heat_and_Fluid_Flow_Cherroud_Sparse_Bayesian_Learning_of_Explicit_Algebraic_Reynolds-Stre.pdf"
tags: [data-driven, symbolic-regression, earsm, uncertainty-quantification, separated-flow, rans]
timestamp: 2026-10-27T15:46:00Z
---

# Summary

Cherroud et al. (2022) introduce SBL-SpaRTA, a stochastic counterpart of
the deterministic SpaRTA [sparse regression](/methods/symbolic-regression-closure.md)
of Schmelzer et al. (2020a). Corrections of the
[$k$-$\omega$ SST](/methods/k-omega-sst-model.md) linear eddy-viscosity
model are sought in two places: an additive anisotropy $b^\Delta_{ij}$ in
the constitutive relation (beyond the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)) and a
production residual $R=2k\,b^R_{ij}\partial_j\langle u_i\rangle$ in the $k$
and $\omega$ equations. Both are expanded on Pope's
[integrity basis](/methods/tensor-basis-neural-network.md), restricted in 2D
to $T^{(1)}$–$T^{(3)}$ and two invariants, with a dictionary of 25
monomials per tensor; the targets come from the $k$-corrective-frozen
solve. The learned models are framed as data-driven
[explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md).

The regression is Tipping's sparse Bayesian learning with an ARD Gaussian
prior on the weights and a demi-Bayesian LASSO hyper-prior on the
precisions, governed by one sparsity parameter $\lambda_{\mathrm{SBL}}$; the
evidence procedure selects terms and gives Gaussian posteriors at once.
$\lambda_{\mathrm{SBL}}$ is chosen by [a posteriori](/definitions/a-priori-and-a-posteriori-testing.md)
cross-validation: the MAP models are run in [OpenFOAM](/software/openfoam.md)
and scored on velocity, $k$, shear stress and $C_f$ in leave-one-out
scenarios over the [periodic hill](/benchmarks/periodic-hill.md), a
converging–diverging channel and the curved
[backward-facing step](/benchmarks/backward-facing-step.md). The selected
models have $b^\Delta_{ij}=0$ and a single stochastic $T^{(1)}$
production term; posteriors are propagated by second-order Hermite
polynomial chaos (three CFD runs per model) into $\pm3\sigma$ bands that
widen where the prediction departs from LES, a handle on
[model-form uncertainty](/definitions/model-form-uncertainty.md). Velocity
and $C_f$ improve over SST, $k$ is overpredicted in separated regions,
and the converging–diverging bubble is not located. A Sobol analysis
shows the production term dominant near walls. The learned models beat
the BSL-EARSM of Menter et al. (2012), a
[Reynolds-stress](/methods/reynolds-stress-model.md)-derived closure. The
introduction places the method against
[field inversion](/methods/field-inversion-machine-learning.md),
[model aggregation](/methods/turbulence-model-aggregation.md) and
[model-consistent training](/methods/model-consistent-training.md).

# Version read

Version of record (Elsevier; received 28 February 2022, accepted 7
September 2022), 19 pages, all read; equations on pp. 4–7, 16, 17 checked
visually. Page 1 matches the metadata; no identity issue. The paper links
the general-EARSM OpenFOAM implementation (github shmlzr/general_earsm).
Equation numbers are those of this version.

# Key claims

Page-local symbols: $\mathsf S^\omega_{ij}=\langle S_{ij}\rangle/\omega$,
$\mathsf W^\omega_{ij}=\langle\Omega_{ij}\rangle/\omega$ the mean strain
and rotation scaled by $1/\omega$ (not the registry's $k/\varepsilon$
scaling of $\mathsf S_{ij}$); $I_1=\mathsf S^\omega_{mn}\mathsf S^\omega_{mn}$,
$I_2=\mathsf W^\omega_{mn}\mathsf W^\omega_{mn}$; $g^{\Delta(n)}$,
$g^{R(n)}$ the coefficient functions of $b^\Delta_{ij}$ and $b^R_{ij}$;
$\alpha^{\mathrm{ARD}}_i$ the prior precisions; $\lambda_{\mathrm{SBL}}$
the sparsity hyper-parameter; $\mathbf M^{(s)}$ the model of scenario $s$;
$m^G$ the averaged relative improvement (Eq. 31); CD, PH, CBFS the
converging–diverging channel, periodic hill and curved backward-facing
step.

1. SBL-SpaRTA simultaneously selects a sparse set of terms from a redundant dictionary and estimates posterior distributions of their coefficients, unlike SpaRTA, which needs separate model-identification and parameter-estimation steps (§1, §3). **Stated**
2. For 2D flows only $T^{(1)},T^{(2)},T^{(3)}$ are linearly independent and only $I_1,I_2$ are nonzero, so $b^\Delta_{ij}=\sum_{n=1}^3T^{(n)}_{ij}g^{\Delta(n)}(I_1,I_2)$ (Eq. 7, after Pope 1975). **Stated**
3. The dictionary $\{I_1^l,I_2^m,I_1^pI_2^q\,\|\,0\le l,m\le9,\ 2\le p+q\le4\}$ gives 25 candidate terms per coefficient function, 75 per target, 150 in total (Eq. 14, §2.2). **Stated** *(compiler check, not in the sources: 10 powers of $I_1$ with the constant, 9 non-constant powers of $I_2$ and 6 mixed products give 25 only if $p,q\ge1$, which Eq. 14 does not state.)*
4. The learning target is $2k\,b^\Delta_{ij}$, not $b^\Delta_{ij}$, because $b^\Delta_{ij}=(2k\,b^\Delta_{ij})/2k$ is $0/0$ at the wall (§2.2). **Derived**
5. Correcting the eddy viscosity and time scale indirectly through the transport equations ($k$-corrective-frozen, Schmelzer et al. 2020a,b) favours models consistent with the RANS solver and reduces error propagation from ill-conditioning (§2.1). **Stated**
6. With demi-Bayesian LASSO priors, larger $\lambda_{\mathrm{SBL}}$ gives a sparser $b^\Delta_{ij}$ model; the $b^R_{ij}$ model reduces to one term ($T^{(1)}$) for every $\lambda_{\mathrm{SBL}}$, its magnitude decreasing as $\lambda_{\mathrm{SBL}}$ grows; for $\lambda_{\mathrm{SBL}}>2\times10^5$ both vanish and SST is unchanged (§4.2, App. A). **Shown**
7. All learned models have much lower streamwise-velocity mean-square error than the baseline; models with non-null $b^\Delta_{ij}$ are somewhat better on the training flows, the sparser models generalize better (§4.2, Fig. 1). **Shown**
8. $\mathbf M^{(1)}$ at $\lambda_{\mathrm{SBL}}=2\times10^5$ gives the most accurate velocity for CD and PH; $\mathbf M^{(3)}$ at $10^4$ the most accurate for CBFS (§4.2, Fig. 1). **Shown**
9. The best models for $C_f$, $k$ and the shear stress have $b^\Delta_{ij}=0$ and only the production correction, which raises the eddy viscosity in the separated region to reattach the boundary layer; no learned model improves all quantities on all flows (§4.2, Figs 2–4). **Shown**
10. Cross-validated on velocity, $k$, shear stress and $C_f$ together, $\lambda^*_{\mathrm{SBL}}=2\times10^5$ for all three scenarios, with $m^G$ = 6.0%, 28.% and 31.% for $\mathbf M^{(1)}$, $\mathbf M^{(2)}$, $\mathbf M^{(3)}$ (Table 2). **Shown**
11. Cross-validated on velocity alone, $\lambda^*_{\mathrm{SBL}}=2\times10^5$ (74.0%), $10^4$ (68.0%), $10^4$ (77.0%); models with non-null $b^\Delta_{ij}$ then outperform production-only models, a limitation attributed to expressing the stress through the mean velocity gradient only (Table 2, §4.2). **Shown**
12. $\mathbf M^{(1)}$ fails to beat the baseline when cross-validated on $k$, $C_f$, $(k,C_f)$, $(\tau_{xy},C_f)$ and $(k,\tau_{xy},C_f)$ ("–" in Table 2), "which suggests that $\mathbf M^{(1)}$ needs probably to be further regularized" (§4.2). **Shown**
13. The selected models $\mathbf M^{(1)}$, $\mathbf M^{(2)}$, $\mathbf M^{(3)}$ ($\lambda^*_{\mathrm{SBL}}=2\times10^5$) have $b^R_{ij}=g^{R(1)}T^{(1)}_{ij}$ with $g^{R(1)}=0.8433\pm0.0142$, $0.382\pm0.0184$, $0.197\pm0.0156$ (Eqs. A.13–A.15). **Shown**
14. Gaussian posteriors are propagated by Hermite polynomial chaos truncated at second order; with one stochastic coefficient, three CFD runs per model suffice (§4.2). **Stated**
15. The three models clearly outperform SST in velocity profiles, especially in the CBFS and PH recirculations; the $\mathbf M^{(3)}$ intervals are too narrow to cover the LES everywhere, the $\mathbf M^{(1)}$ bands cover it (Fig. 5). **Shown**
16. The uncertainty intervals grow where the prediction departs from LES, warning about reliability (Figs 5–7, Conclusions). **Shown**
17. The authors write that "it is however likely" that the solution posterior is asymmetric although the parameter posterior is symmetric, because the Navier–Stokes equations are nonlinear; the intervals are drawn symmetric ($\pm3\sigma$) (§4.2). **Stated**
18. $C_f$ predictions improve the separation and reattachment points, and the intervals encompass the LES separation and reattachment (Fig. 6). **Shown**
19. For CD no model locates the small LES separation bubble: it is much smaller than SST's but shifted downstream and larger than LES; the raised eddy viscosity increases upstream skin friction and delays separation (§4.2, Fig. 6). **Shown**
20. For CBFS the predicted $C_f$ in attached regions is slightly worse than the baseline, most visibly for $\mathbf M^{(1)}$ (largest $g^{R(1)}$), but the high-fidelity values stay within the intervals (§4.2). **Shown**
21. All three models overpredict $k$ in separated regions, with large intervals for $k$ in all cases (Fig. 7). **Shown**
22. The single-term learned models are almost as robust and cheap as SST and perform significantly better than the BSL-EARSM of Menter et al. (2012) in OpenFOAM (§4.2, App. C, Figs C.9–C.11). **Shown**
23. Sobol analysis of $\mathbf M^{(3)}$ at $\lambda_{\mathrm{SBL}}=10^4$ (non-null $b^\Delta_{ij}$, four stochastic parameters): the shear anisotropy is mostly sensitive to the $b^R_{ij}$ parameter near walls, especially near separation and reattachment; sensitivity to $b^\Delta_{ij}$ lies mostly outside the boundary layer, in the recirculation, dominated by the linear $T^{(1)}$ term; interactions above second order are negligible (§4.3, Fig. 8a). **Shown**
24. "LEVM are overall sufficient for such 2D separated flows, provided that the eddy viscosity coefficient is properly tuned" (§4.3). **Shown** (interpretation of Fig. 8)
25. Correcting the production of $k$ is generally sufficient for these 2D separated flows, consistent with Schmelzer et al. (2020a) and Ben Hassan Saïdi et al. (2022); not for 3D flows (Huijing et al. 2021), where nonlinear terms become important (Conclusions). **Stated**
26. Without uncertainty intervals, propagating only the MAP estimates costs a single CFD run (Conclusions). **Stated**
27. Bayesian inference is more robust to overfitting than deterministic regression on sparse data, thanks to the regularizing priors (§1). **Stated**

# Printed slips

- **Eq. (2):** the viscous term is printed $\partial_j(\nu\,\partial U_j/\partial x_j)$.
- **Eq. (11), sign of the production.** *(Compiler check, not in the sources: with $\tau_{ij}=\langle u_i'u_j'\rangle$ entering the momentum equation (2) as $-\partial_j\tau_{ij}$, the production is $-\tau_{ij}\partial_jU_i=2k(\frac{\nu_t}{k}S_{ij}-b^\Delta_{ij})\partial_jU_i$; Eq. (11) prints $2k(-\frac{\nu_t}{k}S_{ij}+b^{\Delta,hf}_{ij})\partial_jU_i$, the opposite overall sign. Eq. (12), $R=2kb^R_{ij}\partial U_i/\partial x_j$, follows the printed convention, so the sign of the $b^R_{ij}$ coefficients relative to $\nu_t$ depends on it.)*
- **Eq. (10):** the destruction of the $\omega$ equation is printed $-\beta^*\omega^2$ (the constant of the $k$ equation) and the diffusion coefficient $\sigma_w$, while the text says $\sigma_\omega$.
- **Eq. (26).** *(Compiler check, not in the sources: the Gaussian marginal likelihood of Eqs. (17) and (19) has the quadratic term $\mathbf t^T(\sigma^2\mathbf I+\mathbf C\mathbf A^{-1}\mathbf C^T)^{-1}\mathbf t$; Eq. (26) prints it without the inverse.)* The prior sum runs $\sum_{i=0}^M$ although the precisions are indexed $1,\dots,M$ (Eqs. 19–20).
- **Eq. (27):** $\gamma_i$ is never defined; the same symbol is the quantity weight of Eq. (30), and $\gamma$ the $\omega$-equation coefficient of Eq. (10).
- **p. 5, noise prior:** "uniform hyper-prior on $\frac1{\sigma^2}$ (over a logarithmic scale)" and later "a uniform prior for $\sigma^2$".
- **§2.2, p. 4:** "75 = M function candidates for $b^\Delta_{ij}$, and the same number for $b^\Delta_{ij}$ too" (the second is $b^R_{ij}$); the design matrices are named $\mathbf C_{b^\Delta}$ and $\mathbf C_{b^R}$ in the text and $\mathbf C_R$ in Eq. (15).
- **§4.1, CD case:** bump height printed "$h\simeq\frac{2}{3H}$", dimensionally inconsistent.
- **Eq. (A.9):** $\mathbf M^{(3)}_{b^R}=[(0.737\pm0.0296)]\mathbf T^{(1)}\pm0.358$, while the noise standard deviation of $\mathbf M^{(3)}_{b^R}$ is printed 0.0358, 0.0358, 0.0361 and 0.0364 in Eqs. (A.3), (A.6), (A.12), (A.15).
- **Eqs. (A.10), (A.11):** "$\mathbf T^{(2)}+\pm0.0042$", "$+\pm0.00417$".
- **SpaRTA citation:** §4.2 "the three models of Schmelzer et al. (2020b)" and §2.2 "as in Schmelzer et al. (2020b)", while the captions of Figs 1–4 and Appendix B cite 2020a.
- **Table 1** column header "Model idle"; **Table 2** "28.%", "31. %"; p. 1 "MSC: 0000 1111" template field; abstract "probabilistic chaos collocation".
- **§4.3:** the four-parameter model of the Sobol analysis needs more than the three collocation runs stated in §4.2 for one-parameter models; the number used is not printed.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U_i$, $P$, $u_i'$ | $\langle u_i\rangle$, $\langle p\rangle$, $u_i'$ | |
| $\tau_{ij}=\langle u_i'u_j'\rangle$ | $R_{ij}$ | positive convention; **collision:** the registry's $\tau_{ij}$ is the SGS stress |
| $a_{ij}=\tau_{ij}-\frac23k\delta_{ij}$ | $R_{ij}-\frac23k\delta_{ij}=2kb_{ij}$ | |
| $b^0_{ij}=-\nu_tS_{ij}/k$ | $-\nu_t\langle S_{ij}\rangle/k$ | Boussinesq anisotropy |
| $b^\Delta_{ij}$, $a^\Delta_{ij}=2kb^\Delta_{ij}$ | $b^\Delta_{ij}$, $2kb^\Delta_{ij}$ | |
| $R^{hf}$, $R$, $b^R_{ij}$ | $R$, $b^R_{ij}$ | production residual and its tensor |
| $S_{ij}$ | $\langle S_{ij}\rangle$ | |
| $S^*_{ij}$, $\Omega^*_{ij}$ | $\mathsf S^\omega_{ij}$, $\mathsf W^\omega_{ij}$ (page-local) | scaled by $1/\omega$, not $k/\varepsilon$ |
| $T^{(n)}_{ij}$, $I_1$, $I_2$ | $T^{(n)}_{ij}$, $I_1$, $I_2$ (page-local invariants) | $I_2$ without minus sign |
| $\alpha^\Delta_n$, $\alpha^R_n$ | $g^{\Delta(n)}$, $g^{R(n)}$ | **collision:** the source's $\alpha_i$ are also the SBL precisions |
| $\alpha_i$, $\mathbf A$ | $\alpha^{\mathrm{ARD}}_i$ (page-local) | |
| $\lambda$ | $\lambda_{\mathrm{SBL}}$ (page-local) | **collision** with the Taylor microscale |
| $\gamma$ ($\omega$ equation), $\beta^*$, $\sigma_k$, $\sigma_\omega$ | $\gamma_\omega$, $\beta^*$, $\sigma_k$, $\sigma_\omega$ | values not printed |
| $P_k$ (Eq. 11) | $P_k$ | limited by $10\beta^*\omega k$; sign as printed (see slips) |
| $\mathbf w$, $\mathbf C$, $\mathbf t$ | $\boldsymbol\theta$, (design matrix), (target vector) | |
| $\sigma^2$, $\boldsymbol\mu$, $\boldsymbol\Sigma$ | (noise variance, posterior mean and covariance, page-local) | |
| $M$ | (number of candidate functions, 75) | |
| $h$, $H$ | (hill/step/bump height; channel half-height) | **collision:** not the cell size $h$ |
| $Re$ | $Re_h$ (PH, CBFS), $Re$ on the half-height (CD) | |
| $C_f$, $\tau_{xy}$ | $C_f$, $R_{12}$ | |

# Reference list

68 printed references, author-year (Elsevier Harvard), alphabetical. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Same-author same-year works are keyed in printed
order (Edeling 2014a/b and 2018, De Zordo-Banliat 2020a/b, Ling 2016a/b,
Schmelzer 2020a/b, Wu 2019a/b). The ingested Sources
[duraisamy-2019](/sources/duraisamy-2019.md), [duraisamy-2021](/sources/duraisamy-2021.md)
and [li-2021](/sources/li-2021.md) are the same works as the entries
cited. De Zordo-Banliat et al. 2020b prints no volume; Menter 1992 is
recorded as a technical report; only one DOI is printed (Beetham et al.
2021). No printed duplicate; no item is unparseable.

# Pages created or updated

Chunk 10 (2026-10-27). This source is cited on:

- [Backward-facing step](/benchmarks/backward-facing-step.md)
- [Periodic hill](/benchmarks/periodic-hill.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Model-consistent (a posteriori) training of learned closures](/methods/model-consistent-training.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
- [Symbolic-regression turbulence closures](/methods/symbolic-regression-closure.md)
- [Tensor-basis neural network and the integrity basis](/methods/tensor-basis-neural-network.md)
- [Aggregation and blending of data-driven turbulence models](/methods/turbulence-model-aggregation.md)
- [OpenFOAM](/software/openfoam.md)
