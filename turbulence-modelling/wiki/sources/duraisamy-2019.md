---
type: Source
title: "Duraisamy et al. (2019) — Turbulence Modeling in the Age of Data"
description: "Review of how experimental and DNS data are used to quantify and reduce the model-form uncertainty of RANS closures: a four-layer taxonomy of modelling assumptions, realizability-constrained perturbations, Bayesian calibration, field inversion, machine-learned discrepancies and the field-inversion-and-machine-learning paradigm."
resource: "doi:10.1146/annurev-fluid-010518-040547"
source_kind: paper
authors: [Duraisamy K., Iaccarino G., Xiao H.]
year: 2019
venue: "Annu. Rev. Fluid Mech. 51:357–377"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2019_Crossref_Annual_Review_of_Fluid_Mechanics_Duraisamy_Turbulence_Modeling_in_the_Age_of_Data.pdf"
tags: [rans, data-driven, uncertainty-quantification, field-inversion, review]
timestamp: 2026-10-25T13:42:00Z
---

# Summary

Duraisamy et al. (2019) review the use of data (experiments and DNS) to
quantify and reduce the uncertainty of single-point RANS closures. The
organising device is a four-layer taxonomy of RANS modelling assumptions:
L1, the information lost by Reynolds averaging, called irrecoverable; L2,
the representation of the Reynolds stress $R_{ij}$ in terms of averaged
variables (the [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)
is an L2 choice); L3, the functional form of the model operators; L4, the
coefficient values. Each class of method is then written as one form of a
calibrated model built from the model, the data, the discrepancy
$\boldsymbol\delta$ and the features $\boldsymbol\zeta$ (Eqs. 7, 8, 9, 13);
this framing anchors the page on
[model-form uncertainty](/definitions/model-form-uncertainty.md).

Three strands are surveyed: bounding uncertainty from physical constraints
(realizability-constrained eigenspace perturbations of $R_{ij}$, random-matrix
sampling); statistical inference (Bayesian calibration of coefficients,
spatial discrepancy fields, field inversion of a multiplier on the production
term of the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md) in a
convex curved channel, compared with SARC); and machine learning of
discrepancies (Gaussian-process and random-forest models of the Reynolds-stress
discrepancy tested on the [periodic hill](/benchmarks/periodic-hill.md) and a
square duct, the [tensor-basis neural network](/methods/tensor-basis-neural-network.md)
and gene-expression programming on Pope's integrity basis). Bayesian
calibration on [channel-flow](/benchmarks/turbulent-channel-flow.md) DNS is
cited as L4-only work.

The review presents no new computations; every figure is reproduced from
the cited works. Its central argument is about data–model consistency:
learning directly from DNS creates a mismatch between the training and the
prediction environments, because latent RANS variables (the dissipation rate)
play an operational role. The remedy argued for is
[field inversion and machine learning](/methods/field-inversion-machine-learning.md):
inference precedes learning, and the learned correction is embedded in the
RANS solver. This prefigures the
[a priori against a posteriori](/definitions/a-priori-and-a-posteriori-testing.md)
question, although the paper does not use those terms in that sense. It
closes with five open challenges and a call for every prediction to carry an
explicit uncertainty estimate.

# Version read

arXiv preprint arXiv:1804.00183v3 [physics.flu-dyn], 29 September 2018,
typeset in the Annual Reviews template with preprint pagination 1–23 (header
"Annual Review of Fluid Mechanics 2019. 51:1–23"), not the version of record;
23 pages, all read. The metadata above are those of the published version
(Annu. Rev. Fluid Mech. 51:357–377). Page 1 matches the published identity
(title, three authors listed alphabetically by a footnote, DOI). Section,
equation and figure numbers on this page are those of the arXiv v3. The
embedded Fig. 3 (p. 11) is a cropped page of Ling & Templeton (2015) whose
hidden text layer (caption of that paper's Fig. 7, page header, download
stamp) leaks into text extraction; that text is not content of this review.

# Key claims

1. RANS modelling assumptions fall into four layers: L1 (averaging), L2
   (representation of $R_{ij}$ in terms of the averaged variables), L3
   (functional form of the model operators) and L4 (coefficients
   $\boldsymbol\theta$). The uncertainty introduced at L1 is "fundamentally
   irrecoverable regardless of the sophistication of the turbulence model"
   (§2, Eqs. 1–6). **Stated**
2. Under L1, infinitely many instantaneous realizations are compatible with
   one averaged field and can evolve differently, "leading to hysteresis-like
   phenomena and thus uncertainty" (§2, L1). **Stated**
3. Linear eddy-viscosity and algebraic stress models are L2-level assumptions;
   if $R_{ij}$ depends only on the local mean velocity gradient, the
   Cayley–Hamilton theorem yields an exact expansion basis (§2, L2). **Stated**
4. The choice of $C_\mu$ in two-equation linear eddy-viscosity models is "a
   classical L4 closure issue" (§2, L4). **Stated**
5. Naive calibration (Eq. 7) ignores measurement uncertainty and treats the
   coefficients as the dominant error source; it "has led to the proliferation
   of turbulence model variants" (§3.1). **Stated**
6. With Gaussian distributions the MAP estimate is the solution of a
   deterministic weighted least-squares problem, and the box states that
   regularized least squares coincides with MAP when the regularization weight
   equals the observation covariance times the inverse prior covariance (box
   "Statistical inversion", p. 7). **Stated** (the printed condition is
   discussed under Printed slips)
7. Kennedy–O'Hagan calibration adds a Gaussian-process discrepancy to the
   model output and treats the input-to-prediction map as a physics-agnostic
   black box; the review focuses instead on discrepancies embedded inside the
   model (§3.4). **Stated**
8. Formal bounds from the background-flow method exist for shear, channel,
   Rayleigh–Bénard and porous-medium flows, but it is "difficult to envision
   that formal bounds can be derived for flow problems of practical
   engineering interest" (§4.1). **Stated**
9. Realizability strongly constrains the eigenvalues of $R_{ij}$, only weakly
   constrains $k$ (pointwise non-negativity) and does not bound the
   eigenvectors (§4.1, Fig. 1). **Stated**
10. Bounding eigenvector uncertainty by the two alignments of maximum and
    minimum production of $k$ gives prediction intervals that "appear to
    provide a satisfactory representation" of model uncertainty for a
    turbulent jet (§4.1, Fig. 2, from Mishra & Iaccarino 2017). **Shown**
    (reproduced)
11. The random-matrix approach samples a maximum-entropy distribution of
    symmetric positive semi-definite matrices with mean $R_{ij}^{\mathrm{RANS}}$;
    it explores eigenvalue and eigenvector uncertainty jointly but lacks the
    clear limiting-state interpretation of the eigenspace approach; both
    guarantee realizability (§4.1). **Stated**
12. The discrepancy is spatially varying, $\boldsymbol\delta=\boldsymbol\delta(\boldsymbol x)$,
    because the RANS equations contain the divergence of $R_{ij}$ (§4.1).
    **Stated**
13. Model coefficients are not universal (flow-specific optimal values for the
    plane jet, round jet and wake), so default coefficients in complex flows
    cause L4 uncertainty (§4.2). **Stated**
14. Failure markers identify where RANS assumptions are violated, but "there
    is no straightforward way to use the results for improving predictions"
    (§4.3, Fig. 3). **Stated**
15. Oliver & Moser (2011) and Cheung et al. (2011) "were the first" to combine
    channel DNS and Bayesian inference to obtain posterior distributions of
    RANS model parameters (§5.1). **Stated**
16. Oliver & Moser (2009) modelled a Reynolds-stress discrepancy tensor as a
    random field governed by stochastic equations structurally similar to, but
    simpler than, Reynolds-stress transport; this "laid the foundation" of
    model-form uncertainty quantification (§5.1). **Stated**
17. Field inversion of a multiplier $\beta(\boldsymbol x)$ on the
    Spalart–Allmaras production term, from LES skin friction on the lower
    convex wall of a curved channel only, gives velocity and Reynolds stresses
    in good agreement with LES and better than SA and SARC; the inferred trend
    is consistent with convex curvature reducing turbulence and suggests that
    SARC needs improvement in the log layer (§5.1, Figs. 4–5). **Shown**
    (reproduced from Singh & Duraisamy 2016)
18. Inferred discrepancy fields are tied to one geometry and flow condition;
    mapping $\boldsymbol\delta$ to features $\boldsymbol\zeta$ is the route to
    generalization (§5.2). **Stated**
19. Random-forest models of the discrepancy in Reynolds-stress magnitude,
    anisotropy and orientation, trained on separated flows in other
    geometries, improve the predicted anisotropy and mean velocity on the
    periodic hill (§5.3, Figs. 6–7). **Shown** (reproduced)
20. Objectivity and rotational invariance of learned Reynolds-stress models are
    obtained from tensor invariants of the eigendecomposition; orientation has
    been represented by Euler angles and unit quaternions (§5.3). **Stated**
21. The tensor-basis neural network learns the coefficients
    $g^{(n)}(\boldsymbol\zeta)$ of the ten-tensor expansion but gives "no
    explicit expression for the resulting model"; gene-expression programming
    gives explicit algebraic models, but trained on low-Reynolds-number
    backward-facing-step DNS it shows "a high level of uncertainty" on the
    periodic hill (§5.3, Eqs. 11–12). Eq. 11 is printed as an expansion of the
    full stress, $R_{ij}=\sum_{n=1}^{10}g^{(n)}T^{(n)}_{ij}$, with no separate
    isotropic term. **Stated**
22. Existing feature sets are local; non-local, non-equilibrium features (e.g.
    streamline integration) could extend predictive capability (§5.3).
    **Stated**
23. Applying machine learning directly to high-fidelity data makes the
    training and the prediction environments inconsistent; latent RANS
    variables are operational (the RANS $\varepsilon$ only supplies scale
    information); inference before learning enforces consistency (§5.4, §6).
    **Stated**
24. Even replacing RANS terms by DNS-computed quantities leaves predictions
    unsatisfactory, partly because the RANS equations can be ill-conditioned
    (§6). **Stated**
25. In the field-inversion-and-machine-learning airfoil application, "even
    very limited experimental measurements, such as the lift coefficient" give
    considerable improvement over the baseline Spalart–Allmaras model (§5.4,
    Fig. 8). **Shown** (reproduced)
26. Equation discovery purely from data has so far rediscovered known
    equations; discovering unknown closures from finite data risks
    "problem-specific/spurious laws" (§6). **Stated**
27. The recommended approach (1) uses inference and learning, (2) assesses
    information content, (3) complies with physical and mathematical
    constraints, (4) acknowledges the closure assumptions and (5) quantifies
    uncertainty rigorously; every prediction should carry an explicit
    uncertainty estimate (§6, Eq. 13). **Stated**

# Printed slips

- **Production sign (§4.1).** Printed: "the turbulence kinetic energy (TKE)
  production $P=\tau_{ij}\partial U_i/\partial x_j$". Eq. 10 writes the stress
  as $\boldsymbol\tau=2k(\frac13\mathbf I+\mathbf V\boldsymbol\Lambda\mathbf V^\top)$,
  and the random-matrix approach places it among positive semi-definite
  matrices, so $\boldsymbol\tau$ is the kinematic, positive-trace stress. With
  that convention the production is $P_k=-R_{ij}\partial_j\langle u_i\rangle$,
  so the printed formula lacks a minus sign; the sign swaps which alignment
  is called maximum and which minimum, not the pair of extremal alignments
  *(compiler check, not in the sources)*.
- **Least squares against MAP (box, p. 7).** Printed:
  $\mathbf c_{\rm LS}=\arg\min\|\boldsymbol\theta-\mathbf o(\mathcal M(\mathbf c))\|_2^2+\gamma\|\mathbf c\|_2$,
  with an unsquared regularization norm and no prior mean, and the condition
  "$\gamma\equiv Q_\theta Q_c^{-1}$", which equates a scalar weight with a
  matrix product. With $Q_\theta=\sigma_\theta^2\mathbf I$,
  $Q_c=\sigma_c^2\mathbf I$ and $\mathbf c_{prior}=0$, twice the MAP objective
  times $\sigma_\theta^2$ is
  $\|\boldsymbol\theta-\mathbf o\|_2^2+(\sigma_\theta^2/\sigma_c^2)\|\mathbf c\|_2^2$:
  the equivalence holds for a squared norm, zero prior mean and isotropic
  covariances, with $\gamma=\sigma_\theta^2/\sigma_c^2$ *(compiler check, not
  in the sources)*.
- §3.2: "misfit between the model prediction δ and the data", whereas
  $\boldsymbol\delta$ is everywhere else the discrepancy (the misfit itself).
- §6, after Eq. 13: "$\tilde{\mathbf q}=\widetilde{\mathcal M}+\boldsymbol\epsilon_{\mathbf q}$"
  equates a quantity of interest with a model: the lexicon of p. 3 defines
  $\mathbf q$ as a quantity of interest and $\widetilde{\mathcal M}$ as the
  calibrated model.
- §5.2 credits "the scenario averaging (Edeling et al. 2014b)", but in the
  printed list 2014a is "Predictive RANS simulations via Bayesian
  model-scenario averaging" (J. Comput. Phys. 275) and 2014b is "Bayesian
  estimates of parameter variability in the k–ε turbulence model"
  (J. Comput. Phys. 258).
- §5.3 cites "(Wu et al. 2017)" for Euler angles and quaternions; the list has
  no 2017 Wu entry. The only Wu entry on the representation of Reynolds-stress
  perturbations is the unlettered Wu, Sun, Laizet & Xiao (2018),
  "Representation of Reynolds stress perturbations…", CMAME, printed with
  arXiv:1709.05683.
- §5.4: "even if the values assumed by are different from the true value": the
  symbol of the dissipation rate is missing (also on the rendered page).
- Typos: "reliazability" (§4.1, p. 9); "constrains such as symmetry
  properties" (p. 7); "the the entire mapping" (p. 7); "the mode of the the
  posterior" (p. 6); "statical inversion" (p. 12); "indicted in the insets"
  and "significant different geometries" (Fig. 6 caption).

# Notation map

| Duraisamy et al. (2019) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol\tau$, $\tau_{ij}$ | $R_{ij}=\langle u_i'u_j'\rangle$ | sign and density convention not stated; Eq. 10 and the positive semi-definite random matrix fix the kinematic, positive-trace convention |
| $\boldsymbol\tau^{\rm RANS}$, $\tilde{\boldsymbol\tau}$, $\boldsymbol\delta_\tau$ | $R_{ij}^{\mathrm{RANS}}$, perturbed or learned $R_{ij}$, discrepancy of $R_{ij}$ | tilde = perturbed or calibrated, **not** a Favre filter |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | time or ensemble average; agrees |
| $U_i$ | $\langle u_i\rangle$ | mean velocity |
| $k$, $\tilde k$ | $k$ | baseline and perturbed turbulent kinetic energy |
| $\boldsymbol\Lambda$, $\mathbf V$ | eigenvalues and eigenvectors of $b_{ij}$ | Eq. 10 places $\mathbf V\boldsymbol\Lambda\mathbf V^\top$ beside $\frac13\mathbf I$ |
| $P=\tau_{ij}\partial U_i/\partial x_j$ | $P_k=-R_{ij}\partial_j\langle u_i\rangle$ | printed without the minus sign (Printed slips) |
| $\mathbf c$ | $\boldsymbol\theta$ | model coefficients (L4) |
| $\boldsymbol\theta$ (data) | written "data" | **collision**: the registry $\boldsymbol\theta$ is the trainable parameters |
| $\boldsymbol\eta$ (features) | $\boldsymbol\zeta$ | **collision**: the registry $\eta$ is the Kolmogorov length |
| $\boldsymbol\delta$ | $\boldsymbol\delta$ | model discrepancy; agrees |
| $\delta$ (Fig. 4, SA production multiplier) | $\beta(\boldsymbol x)$ | field-inversion correction field |
| $c^{(n)}$, $\mathbf T^{(n)}$ | $g^{(n)}$, $T^{(n)}$ | Pope (1975) integrity basis, Eqs. 11–12 |
| $\mathbf T$ (random matrix) | random symmetric positive semi-definite matrix | same letter as the basis tensors in the source |
| $\mathbf W$, $\boldsymbol\beta$, $\boldsymbol\ell$, $\sigma$ | part of $\boldsymbol\theta$ (weights, biases), hidden layer, activation | **collision**: the bias $\boldsymbol\beta$ against the registry $\beta(\boldsymbol x)$ |
| $\gamma$ | regularization weight | **collision** with the registry $\gamma$ (ratio of specific heats) |
| $\mathcal M$, $\widetilde{\mathcal M}$, $\mathcal P$, $\mathbf w$, $\mathbf o$, $\mathbf q$ | model, calibrated model, model operators, averaged variables, model output, quantity of interest | paper-specific lexicon (box, p. 3); $\mathcal P$ is not the production |
| $\boldsymbol\epsilon_\theta$, $\boldsymbol\epsilon_{\mathbf q}$ | data and prediction uncertainty | not the dissipation $\varepsilon$ |
| $Q_\theta$, $Q_c$ | observation and prior covariance matrices | |
| $s$, $s_\perp$ | streamwise coordinate, wall-normal distance (curved channel) | $s_\perp$ is $y$ |
| $C_\mu$, $C_f$ | $C_\mu$, $C_f$ | agree |
| L1–L4 | layers of modelling assumptions | paper-specific taxonomy |

# Reference list

The arXiv v3 prints 84 references in author-year style (alphabetical
"Literature Cited"), with no DOIs. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` duraisamy-2019;
same-author-year works take key suffixes in printed order (Edeling et al.
2014a, 2014b; Ling et al. 2016a, 2016b; Singh et al. 2017a, 2017b; Wang et al.
2016a, 2016b; the unlettered Wu et al. 2018 CMAME entry and Wu et al. 2018a, b,
c). Pre-publication items are their own entries: Raissi et al. 2017 (arXiv),
Wu et al. 2018a (in preparation), Wu et al. 2018c (submitted,
arXiv:1803.05581), Wu et al. 2018 (CMAME, printed with an arXiv number), Pan &
Duraisamy 2018 and Xiao & Cinnella 2018 (printed with arXiv numbers). Giles et
al. (2003) prints the third author as "J.-D. M-uacute, ller" (a BibTeX
artefact for Müller); Eisfeld (2017) prints no venue; Durbin (2017) prints
"Annual Review of Fluid Mechanics, (0), 2017"; several entries print no
volume (Edeling et al. 2017, Ray et al. 2016, Singh et al. 2017b, Vollant et
al. 2017, Weatheritt & Sandberg 2017).

# Pages created or updated

Chunk 1 (2026-10-25), cited further in chunk 2 (2026-10-25). This source is cited on:

- [Backward-facing step](/benchmarks/backward-facing-step.md)
- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Periodic hill](/benchmarks/periodic-hill.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Tensor-basis neural network and the integrity basis](/methods/tensor-basis-neural-network.md)
