---
type: Method
title: "Aggregation and blending of data-driven turbulence models"
description: "Several RANS models, each trained for one flow class, are combined with space-dependent convex weights learned from local flow features: externally, by mixing the solutions of separate runs, or internally, by blending the experts' corrections inside one RANS solve; tested on separated flows, a jet, a hump and an airfoil."
status: established
aliases: [model aggregation, space-dependent model aggregation, XMA, mixture of experts, model blending, internal model blending, M_blend, expert models]
tags: [rans, data-driven, symbolic-regression, uncertainty-quantification, separated-flow]
timestamp: 2026-10-27T15:47:00Z
---

# Aggregation and blending of data-driven turbulence models

Data-driven RANS corrections trained on one class of flows tend not to
carry over to others. **Model aggregation** keeps several "expert" models,
each trained for its own class, and combines them with weights
$w_M(\boldsymbol x)\ge0$, $\sum_Mw_M=1$ (page-local: $M$ an expert of the
set $\mathcal M$), that vary in space and are predicted from local flow
features $\boldsymbol\zeta$ by a regressor.
[Oulghelou et al. (2025)](/sources/oulghelou-2025.md) (§1, Fig. 1)
describe, citing Zordo-Banliat et al. (2024) and Cherroud et al. (2025),
the earlier **external** form (space-dependent model aggregation, XMA): it runs every expert to
convergence and mixes their *solutions*; it is inspired by Bayesian model
averaging, reads the weights as local model probabilities, and estimates
[model-form uncertainty](/definitions/model-form-uncertainty.md) from the
spread of the expert solutions. Oulghelou et al. propose the **internal**
form: the experts' *corrections* are mixed inside the transport equations
and the blended model is solved once.

## Internal versus external aggregation

Oulghelou et al. (2025, §1, §3) state the trade-off:

| | External (XMA) | Internal blending |
|---|---|---|
| What is mixed | quantities of interest of $N_M$ converged runs | model corrections, inside one run |
| Cost | $N_M$ simulations | one corrected run plus one baseline run for the features |
| Governing equations | the aggregated fields "are in general not a solution" of them | the blended solution satisfies the RANS equations |
| Uncertainty | variance across expert solutions estimates model-form uncertainty | "no longer an uncertainty quantification method" |

Oulghelou et al. (§1) cite other internal approaches that choose models by
classifiers trained alongside data-driven models (Matai & Durbin;
[Lozano-Durán & Bae 2023](/sources/lozanoduran-2023.md), whose
[building-block-flow wall model](/methods/building-block-flow-wall-model.md)
classifies the local flow by its similarity to training flows), or weight
them by Gaussian-process posterior variances (Ho et al.). The authors also
note that the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md) is
itself a heuristic blend of $k$-$\varepsilon$ and $k$-$\omega$ (§1). They
argue against two alternatives without testing them: training one model
on many flows "may lead to a soft compromise solution", and progressive
augmentation may still need thresholding functions (§1).

[Cherroud et al. (2022)](/sources/cherroud-2022.md) (§1) recall the
Bayesian model-scenario averaging of Edeling et al. (2014a) and state its
limit: an average over a set of models cannot be more accurate than the
best model in the set. They learn new corrections instead, by sparse
Bayesian regression on three separated flows (see
[symbolic-regression closures](/methods/symbolic-regression-closure.md)).
Oulghelou et al. take the SBL-SpaRTA regression from Cherroud et al.
(2022) and their experts from Cherroud et al. (2025). Their
separated-flow expert, $(5.21\pm0.0173)\,T^{(2)}$ in the anisotropy and
$(0.681\pm0.02)\,T^{(1)}$ in the production, is trained on all three
flows together (Table 1), whereas each selected model of Cherroud et al.
(2022) is trained on two of them and has no anisotropy correction
(production coefficients 0.8433, 0.382 and 0.197, Eqs. A.13–A.15).

## The experts and what is blended (Oulghelou et al. 2025)

**Host model (§2, Eqs. 2–6, App. B).** Steady incompressible
[$k$-$\omega$ SST](/methods/k-omega-sst-model.md) with two additive
corrections, extracted from high-fidelity data by the $k$-corrective
frozen-RANS method (of Schmelzer et al. 2020, as cited there) and
regressed as symbolic models (see
[symbolic-regression closures](/methods/symbolic-regression-closure.md)).
In registry notation, with page-local $b^\Delta_{ij}$ (extra anisotropy)
and $\mathcal R_k$ (residual of the $k$ equation):

$$b_{ij}=-\frac{\nu_t}{k}\langle S_{ij}\rangle+b^\Delta_{ij},\qquad \mathcal R_k=2k\,b^R_{ij}\,\partial_j\langle u_i\rangle,$$

$\mathcal R_k$ added to the $k$ equation and, multiplied by the
$\omega$-production coefficient, to the $\omega$ equation; the production
becomes $\min\{2(\nu_t\langle S_{ij}\rangle-kb^\Delta_{ij})\partial_j\langle u_i\rangle,\ c_1\beta^*k\omega\}$
($c_1=10$). Keeping the linear Boussinesq term and adding the correction
"has the benefit of enhanced numerical stability" (§2, citing earlier work; see
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)). Both
corrections use the 2-D form of Pope's basis with three tensors and two
invariants, built from $S_{ij}/\omega$ and $\Omega_{ij}/\omega$ (Eqs. 7–10;
see [tensor-basis neural network](/methods/tensor-basis-neural-network.md)).
Since $\omega=\varepsilon/(\beta^*k)$, $S_{ij}/\omega=\beta^*\mathsf S_{ij}$
with the registry-style $\mathsf S_{ij}=\tfrac{k}{\varepsilon}\langle S_{ij}\rangle$
*(compiler check, not in the sources)*.

**Experts (Table 1).** Coefficients from SBL-SpaRTA, sparse Bayesian
regression over a dictionary of monomials of the two invariants (§2.1),
with posterior standard deviations small enough that the coefficients are
treated as deterministic (§3):

| Expert | $b^\Delta_{ij}$ | $b^R_{ij}$ | Trained on | Stated effect |
|---|---|---|---|---|
| $M_{\mathrm{SST}}$ | 0 | 0 | — (baseline) | expert for attached wall flows |
| $M_{\mathrm{SEP}}$ | $5.21\,T^{(2)}_{ij}$ | $0.681\,T^{(1)}_{ij}$ | LES of the [periodic hill](/benchmarks/periodic-hill.md) ($Re=10\,595$), DNS of a converging–diverging channel, LES of a curved [backward-facing step](/benchmarks/backward-facing-step.md) ($Re=13\,700$) | raises the eddy viscosity in separated flow |
| $M_{\mathrm{ANSJ}}$ | $0.25\,T^{(1)}_{ij}$ | 0 | PIV of an axisymmetric near-sonic jet ($M_{\mathrm{jet}}=0.985$) | "strongly" lowers the eddy viscosity, compensating the jet anomaly of two-equation models |

**Blended corrections (Eq. 11).**

$$b^\Delta_{ij}=\sum_{M\in\mathcal M}w_M(\boldsymbol x)\,b^{\Delta,M}_{ij},\qquad b^R_{ij}=\sum_{M\in\mathcal M}w_M(\boldsymbol x)\,b^{R,M}_{ij},\qquad \sum_{M\in\mathcal M}w_M=1.$$

**Target weights (§3, Eq. 12).** On the training flows each expert's
streamwise velocity $q_M$ is compared pointwise with the high-fidelity
value $q_{\mathrm{ref}}$ (page-local), and the "exact" weights are Gaussian
kernels of that error:

$$w_M=\frac{\exp\!\big(-\lVert q_M-q_{\mathrm{ref}}\rVert^2/2\sigma_w^2\big)}{\sum_{M'\in\mathcal M}\exp\!\big(-\lVert q_{M'}-q_{\mathrm{ref}}\rVert^2/2\sigma_w^2\big)},$$

with the bandwidth $\sigma_w$ (page-local) chosen from $\{1,10^{-1},\dots,10^{-4}\}$
to minimize the error of the weighted velocity.

**Feature-to-weight map (§3.1, Eq. 13, App. A).** A random-forest regressor
(scikit-learn, 100 trees) maps eleven local features, evaluated on the
*baseline* SST solution, to the weights. Ten are the features of Ling &
Templeton (normalized Q criterion, turbulence intensity, turbulent Reynolds
number, streamwise pressure gradient, time-scale ratio, viscosity ratio,
and others); the eleventh is $P_k/(P_k+\varepsilon)$, which tends to 0 in
decaying turbulence and $\tfrac12$ in equilibrium (Table 12). $R^2$ is 0.991 on
the training 80% of the points and 0.99 on the held-out 20%.
Algorithm 2 (prediction): run baseline SST, compute the features, predict
the weights, assemble Eq. 11, solve the blended model to convergence.

## Results (Oulghelou et al. 2025)

All runs are 2-D, steady, in a modified OpenFOAM, on the grids of the
earlier SpaRTA work; the grids are stated, not shown, to make discretization
error negligible (§4.1).

**Training flows.**

- *Channel, $Re_\tau=1000$ (§4.2.1, Table 3, Fig. 4).* The blend gives
  $M_{\mathrm{SST}}$ a weight "very close to one" across the channel and
  its accuracy: mean absolute error of $u^+$ 0.44 for both, against 2.41
  for $M_{\mathrm{SEP}}$ (log-layer deviation) and 8.97 for
  $M_{\mathrm{ANSJ}}$.
- *Near-sonic jet (§4.2.2, Table 4).* Mean absolute velocity error 0.04
  ($M_{\mathrm{ANSJ}}$), 0.09 (SST), 0.16 ($M_{\mathrm{SEP}}$), 0.07
  (blend); the jet expert dominates downstream.
- *Separated flows (§4.2.3, Tables 6–7, Figs. 7–9).* $M_{\mathrm{SEP}}$ takes
  the largest weight in separated regions, SST in attached ones, the jet
  expert always little. Separation-bubble lengths (in units of the case's
  reference length):

  | Flow | Reference | SST | $M_{\mathrm{SEP}}$ | $M_{\mathrm{ANSJ}}$ | Blend |
  |---|---|---|---|---|---|
  | periodic hill | 4.49 (LES) | 7.42 | 4.15 | 7.98 | 4.555 |
  | converging–diverging channel | 0.85 (DNS) | 3.41 | 0.83 | 6.65 | 2.05 |
  | curved backward-facing step | 3.55 (LES) | 3.59 | 2.51 | 5.52 | 3.44 |

  The blend has the lowest $C_f$ error on the hill and the channel; SST
  has the lowest on the curved step, $M_{\mathrm{SEP}}$ the lowest hill
  velocity error (0.06 against 0.09). A small bubble in the divergent part
  of the channel "cannot be captured by RANS model, even after data-driven
  correction" (p. 19).

**Unseen flows (§5).**

- *Zero-pressure-gradient flat plate (Table 9).* Mean absolute errors of
  $C_f$: SST $8.4\times10^{-5}$, blend $1.7\times10^{-4}$, $M_{\mathrm{SEP}}$
  $3.7\times10^{-4}$, $M_{\mathrm{ANSJ}}$ $1.1\times10^{-3}$; of $u^+$: 0.42,
  0.7, 1.45, 6.27. The blend beats the two specialized experts but not
  SST. "Contrary to expectations", the jet expert gains weight in the log
  region, which the authors read as weight shifts there having "little
  impact" (Fig. 11c).
- *[NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md),
  $Re=9.36\times10^5$ on the chord (Tables 10–11).* Experimental bubble
  from $x/c=0.62$ to 1.15 (length 0.53); SST 0.62, $M_{\mathrm{SEP}}$ 0.41,
  $M_{\mathrm{ANSJ}}$ 1.08, blend 0.52. The blend has the lowest velocity
  (0.04) and $C_f$ ($3.86\times10^{-4}$) errors, SST the lowest $C_p$ error
  (0.03 against 0.04). In the core flow all weights tend to $\tfrac13$,
  which the authors read as insensitivity of that region to the model (Fig. 12d).
- *[NACA 0012](/benchmarks/naca-0012-airfoil.md), $Re=6\times10^6$,
  $0^\circ$–$18^\circ$ (§5.1.3, Figs. 15–16).* The blend reproduces the
  lift slope, drag and surface pressure close to SST; $M_{\mathrm{SEP}}$ is
  "too dissipative" and "should be replaced or supplemented"; the jet
  expert is worst. No error table is printed.
- *Coverage check (§5.1, Fig. 10).* Projections of the features (PCA,
  t-SNE, autoencoder) show the test flows mostly inside the 95% ellipses of
  the training features, with outliers for the airfoil at high incidence.

**Conclusions as stated (§6).** The blend "outperforms the baseline
$M_{\mathrm{SST}}$ model in flow configurations where the baseline model
struggles, and that are sufficiently close to the training flows", and "in
certain cases" surpasses the best individual expert.

## Related ways of protecting attached flow

Aggregation keeps the baseline where the regressor detects attached flow.
[Wu et al. (2025)](/sources/wu-2025.md) reach the same goal with a fixed
mask instead of a learned weight: the field-inversion correction of the
SST $\omega$ equation is multiplied by the DDES shielding function, so it
vanishes inside attached boundary layers (see
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)).
Neither paper compares the two routes.

## Qualifications

- **"Generally outperforms" is stronger than the tables.** Oulghelou et
  al. (2025, p. 20) summarize that the blend "generally outperforms the
  specialized models". In their Tables 6–7 $M_{\mathrm{SEP}}$ is closer to
  the DNS bubble in the converging–diverging channel (0.83 against 2.05 for
  0.85) and has the lower hill velocity error, SST the lower curved-step
  $C_f$ error; on the flat plate SST is better on both metrics (Table 9);
  on the airfoil no errors are printed.
- **Weights follow one quantity.** The target weights are computed from the
  streamwise velocity only, pointwise (§3).
- **Smoothness.** The random-forest weights "exhibit small oscillations",
  which "do not appear to translate" into the solution; smoother
  regressors such as Gaussian processes are suggested (§5.1.1).
- **Scope.** Three experts, 2-D steady RANS, one host model; the authors
  state the procedure extends to $k$-$\varepsilon$ variants with retrained
  experts (§2). The near-sonic jet and the airfoil are compressible cases
  run with an incompressible formulation, and the paper does not say how
  compressibility is handled.
- **Printed slips (arXiv v2).** The converging–diverging channel is at
  $Re=13\,600$ in Table 1 and 12 600 in §4.2.3 and Table 5. The hill's
  reference length is the hill height in Table 5 and Fig. 9 but the
  channel half-height in the Fig. 7 caption. §4.1 names OpenFOAM v23-06
  while ref. [57] gives Version 10. The weight formula writes $\omega_L$
  for the $w_M$ used elsewhere. Appendix A calls all features bounded in
  $[-1,1]$, but the turbulent-Reynolds-number feature is capped at 2 and
  its length scale is not defined. The jet's "$D_{\mathrm{jet}}$" is
  called the nozzle radius in the captions of Figs. 5–6. §3.1 calls the
  channel training data "RANS data" while Fig. 4 compares with DNS. The
  t-SNE paper is printed twice (refs. [66], [69]).

# Citations

- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — arXiv v2: §1, Fig. 1 (external aggregation, internal blending, related approaches); §2, Eqs. 1–10 (augmented SST, tensor basis, frozen-RANS targets); §2.1, §3, Table 1 (SBL-SpaRTA experts); §3, Eqs. 11–13, Algorithms 1–2 (blending, Gaussian weights, random forest); §3.1, Fig. 3, Table 2; §4.1–4.2, Tables 3–7, Figs. 4–9 (training flows); §5, Tables 9–11, Figs. 10–16 (unseen flows, latent-space coverage); §6; App. A, Table 12 (features); App. B (SST constants).
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — classifier of flow similarity in the building-block-flow wall model, as cited by Oulghelou et al. (2025, §1).
- [Wu et al. (2025)](/sources/wu-2025.md) — author manuscript: §2.1, Eqs. 5–6 (shielding-function mask on the field-inversion correction).
- [Cherroud et al. (2022)](/sources/cherroud-2022.md) — §1 (Bayesian model-scenario averaging and its limit); App. A, Eqs. A.13–A.15 (single-scenario SBL-SpaRTA models).
