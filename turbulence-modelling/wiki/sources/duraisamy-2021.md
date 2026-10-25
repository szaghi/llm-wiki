---
type: Source
title: "Duraisamy (2021) — Perspectives on machine learning-augmented Reynolds-averaged and large eddy simulation models of turbulence"
description: "Single-author perspective on machine-learning augmentation of RANS and LES closures: representations of learned corrections, the distinction between a priori and model-consistent training (field inversion, FIML, integrated inference and learning), feature selection, constraints, and the open problems of identifiability, discretization error and generalization."
resource: "doi:10.1103/physrevfluids.6.050504"
source_kind: paper
authors: [Duraisamy K.]
year: 2021
venue: "Phys. Rev. Fluids 6:050504"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2021_Crossref_Physical_Review_Fluids_Duraisamy_Perspectives_on_machine_learning-augmented_Reynolds-averaged.pdf"
tags: [data-driven, model-consistent-training, field-inversion, rans, les, review]
timestamp: 2026-10-25T13:40:00Z
---

# Summary

Duraisamy (2021) is a review and perspective on machine-learning
augmentation of RANS and LES closures. The framing (§II) is abstract: the
governing equations are coarse-grained, by ensemble averaging for RANS or by
implicit or explicit low-pass filtering for [LES](/definitions/large-eddy-simulation.md),
into an exact but unclosed system; a model replaces the unclosed term by a
closure with secondary (scale-providing) variables; a learned correction
$\boldsymbol\delta(\boldsymbol\zeta;\boldsymbol\theta)$ with features
$\boldsymbol\zeta$ and parameters $\boldsymbol\theta$ augments it. The paper
calls this paradigm "data-enabled" rather than "data-driven".

§III surveys representations: eigenvalue perturbation of the Reynolds-stress
anisotropy, the [tensor-basis neural network](/methods/tensor-basis-neural-network.md)
on Pope's integrity basis (a nonlinear extension of the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)), random forests,
symbolic and sparse regression, neural-network SGS models, direct modelling of
the SGS force, neural-network deconvolution, super-resolution and GANs.

§IV is the core argument. **A priori training** (targets and features
extracted from coarse-grained DNS, Eq. 5) is consistent with the DNS field but
not with the RANS or LES environment: features differ when computed from model
variables, errors accumulate on-line, and model terms are rebalanced. This is
the [a priori against a posteriori](/definitions/a-priori-and-a-posteriori-testing.md)
question. **[Model-consistent training](/methods/model-consistent-training.md)**
is the remedy: field inversion (Eq. 7),
[field inversion followed by learning](/methods/field-inversion-machine-learning.md)
(Eq. 8), and integrated inference and learning in one optimization (Eq. 9), of
which the differentiable-physics LES closure of Sirignano et al. on decaying
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
is the cited example. Weakly coupled alternatives without adjoints are listed,
among them "closed loop training"; reinforcement learning is named only as a
flow-control application (§I).

§§V–VII give feature-selection guidelines (local non-dimensionalization,
invariance, local against non-local features), a taxonomy of constraints, and
the open challenges: irrecoverable information loss
([model-form uncertainty](/definitions/model-form-uncertainty.md)),
non-identifiability (an inferred anisotropy perturbation in
[channel flow](/benchmarks/turbulent-channel-flow.md) reproduces mean velocity
and shear stress but not the anisotropy), the entanglement of discretization
and modelling errors in LES without explicit filtering (the subject of
[discretization-consistent closures](/definitions/discretization-consistent-closure.md)),
interpretability, uncertainty quantification and community benchmarks. No new
method or numerical study is introduced beyond illustrative figures.

# Version read

Accepted manuscript made available via CHORUS: one CHORUS cover page plus 25
manuscript pages (26 PDF pages), all read; not the APS typeset version of
record. The metadata above are those of the published version (Phys. Rev.
Fluids 6:050504, published 12 May 2021). The manuscript title is set in title
case ("Perspectives on Machine Learning-augmented Reynolds-averaged and Large
Eddy Simulation Models of Turbulence"); the words agree with the published
title. Section, equation and reference numbers on this page are those of the
accepted manuscript.

# Key claims

1. Coarse-graining the governing equations yields an equation for the
   coarse-grained state plus a known operator acting on an unclosed term; it
   "is *not* an approximation" (§II, Eq. 2). In the RANS example the operator is
   $-\nabla\cdot$ and the unclosed term is $R_{ij}$. **Derived**
2. Predictive turbulence modelling with machine learning has followed a
   "data-enabled" (not "data-driven") paradigm: data improve existing model
   structures, because applicability across regimes, geometries and boundary
   conditions requires a coarse-grained PDE setting (§I). **Stated**
3. Many closure approaches "have saturated in accuracy" over the past decade
   or more (§II). **Stated**
4. The first wave of machine learning in RANS modelling is Tracey et al.
   (2013): a priori supervised learning, on DNS, of discrepancies in the
   Reynolds-stress anisotropy; its advance over earlier uncertainty work was to
   move discrepancies from physical space $\boldsymbol x$ to a feature space
   $\boldsymbol\zeta(\boldsymbol x)$ (§I). **Stated**
5. The tensor-basis neural network writes
   $R_{ij}=2k\left(\tfrac13\delta_{ij}+\sum_{n=1}^{10}g^{(n)}(\boldsymbol\zeta;\boldsymbol\theta)T^{(n)}_{ij}\right)$
   with the ten integrity-basis tensors of the mean strain and rotation, and
   five invariants as features, "objective by definition" (§III.A, Eq. 4).
   **Stated**
6. Sparsity-enforcing regularizers in sparse-regression closures eliminate
   terms and simplify the model form (§III.A). **Stated**
7. Beck et al. and Xie et al. model the SGS force $\partial_j\tau_{ij}$
   directly, "since small errors in the subgrid scale *stresses* can otherwise
   generate large errors in the momentum equation" (§III.A). **Stated**
8. Neural-network deconvolution differs from classical approximate
   deconvolution in that the filter kernel is not assumed a priori (§III.B).
   **Stated**
9. A priori training "establishes the consistency of the ML model with the
   DNS field, but does not guarantee consistency with the RANS or LES
   environment" (§IV.A). **Stated**
10. Feature mismatch: a feature such as $\langle S_{ij}\rangle k/\varepsilon$
    (the strain-rate tensor made dimensionless by the time scale $k/\varepsilon$)
    computed from the model can differ from its DNS value even when the mean
    strain agrees, because the modelled $k$ and $\varepsilon$ can be very
    different from the DNS ones; RANS secondary variables are not one-to-one
    with DNS quantities (§IV.A). **Stated**
11. Error accumulation: a super-resolution network trained offline on exact
    coarse fields, used on-line on coarse fields carrying accumulated error,
    loses the fine-scale structure at $t^*=6.0$ while the offline
    reconstruction stays good at $t^*=0.6$ and $6.0$ (§IV.A, Fig. 1; the flow
    configuration is not specified). **Shown**
12. Successful a priori evaluation is "neither a necessary (e.g. Smagorinsky
    model) nor a sufficient condition for successful predictive models"
    (§IV.A). **Stated**
13. Using exact $k$ and $\varepsilon$ in the eddy viscosity of one- and
    two-equation models did not improve performance (Raiesi et al.), and
    substituting DNS Reynolds stresses may not give satisfactory velocity
    fields (Thompson et al.) (§IV.A). **Stated** (cited)
14. Field inversion solves a PDE-constrained inverse problem for a
    space–time augmentation field from possibly sparse data; it is consistent
    with the model and needs no full-field DNS (§IV.B, Eq. 7). **Stated**
15. Field inversion and machine learning (Eqs. 7–8) promote consistency, but
    imperfections of the learning step reintroduce inconsistency; integrating
    inference and learning in one optimization (Eq. 9) "ensures full
    consistency between the learning and prediction environments" (§IV.B).
    **Stated**
16. The drawback of the integrated approach is that features must be chosen
    before inference; separate inversion and learning stages are more flexible
    (§IV.B). **Stated**
17. Model-consistent training typically requires adjoint-driven optimization;
    adjoint intrusiveness is a barrier, and in LES chaos can make adjoint
    solutions unstable, requiring shadowing-type treatment (§IV.B). **Stated**
18. Weakly coupled alternatives ("embedded learning", "iterative machine
    learning", "CFD-driven machine learning", "closed loop training") move
    toward model consistency without adjoints, though some still need
    full-field DNS (§IV.B). **Stated**
19. In LES of decaying homogeneous isotropic turbulence, an a priori-trained
    SGS closure overpredicts the resolved kinetic energy, whereas the
    model-consistent (differentiable-physics) closure follows filtered DNS
    (§IV.B, Fig. 2, reproduced from Sirignano et al.). **Shown** (cited result)
20. The convergence of all these training methods needs rigorous study, and
    the choice of loss function "has not been studied in earnest" (§IV.B).
    **Stated**
21. Regression models are interpolative in feature space; with well-chosen
    features and an adequately populated feature space, embedding them in a
    physics-based model can predict better on unseen geometries (§V).
    **Stated**
22. Feature guidelines: local non-dimensionalization (e.g.
    $\langle S_{ij}\rangle k/\varepsilon$); rotational, reflectional and
    frame invariance, also of the normalizing variables; preference for local
    features, although the wall distance $d$, wall-stress measures and
    pressure-gradient features (as non-local surrogates) have proved important;
    a model with $n$ features needs data populating an $n$-dimensional space
    (§V). **Stated**
23. Wang et al. ranked 47 candidate features by random-forest importance (§V,
    Fig. 3). **Stated**
24. Constraints can act on inputs, on outputs (e.g. realizability of the
    correction in $R_{ij}=R^{\mathrm{b}}_{ij}+\delta_{ij}(\boldsymbol\zeta;\boldsymbol\theta)$,
    $\mathrm{b}$ the baseline), on physics-model outputs (e.g. integrated heat
    release in combustion), or through Bayesian priors (§VI). **Stated**
25. Model discrepancy is partly irrecoverable: infinitely many fine-scale
    realizations are compatible with a coarse-grained field, and the closure
    structure itself (single-point, Markovian) introduces errors that machine
    learning cannot address (§VII). **Stated**
26. Non-identifiability: a model-consistent anisotropy perturbation inferred
    from mean-velocity data in channel flow gives accurate mean velocity and
    Reynolds shear stress but inaccurate anisotropy; using the full Reynolds
    stress as data would remedy it (§VII, Fig. 4). **Shown** (no parameters
    given)
27. In LES, numerical and modelling errors are hard to disentangle,
    especially without explicit filtering, and explicit filtering may not fully
    address this (Lund); model-consistent training accounts for numerical
    errors "at least as far as reconstructing the training data is concerned"
    (§VII). **Stated**
28. Interpretable (symbolic-regression) models do not automatically
    generalize beyond their training scenarios (§VII). **Stated**
29. Machine-learning-augmented models have improved training cases and
    closely related ones (e.g. an airfoil of slightly different shape), but "the
    goal of more generalizable models has, however, not been achieved";
    community benchmarks, standardized evaluation and reproducibility are needed
    (§VII). **Stated**
30. Documenting the candidate model forms and parameter ranges explored in
    classical model development would inform rigorous priors (§VII).
    **Stated**

# Printed slips

- §III.A, Tracey et al. equation (unnumbered), printed:
  $\tau_m=2k_m\left(\frac13I+\tilde V_m(\tilde\Lambda_m+\delta_m(\tilde\eta_m;w)\tilde V_m^T)\right)$.
  The parenthesis closes after $\tilde V_m^T$, so $\tilde V_m^T$ multiplies
  only $\delta_m$; an eigendecomposition reads
  $\tilde V_m(\tilde\Lambda_m+\delta_m)\tilde V_m^T$ *(compiler check, not in
  the sources)*. The text defines "$\tilde k_m$" while the equation uses
  $k_m$.
- §III.A: "Ling and Templeton [28]"; ref. [28] is Ling, Kurzawski & Templeton
  (2016).
- §III.A: "Kaandorp and Dwight [32] leverage the above integrity basis ...
  random forest regression"; ref. [32] is printed as Mishra, Iaccarino &
  Duraisamy, "Sensitivity of flow evolution on turbulence structure", Phys.
  Rev. Fluids 1:052402 (2016), a verbatim copy of ref. [79]. The Kaandorp &
  Dwight work is absent from the list.
- §I: "Ma et al.[17, 18] (2016)"; ref. [17] is dated 2015.
- §IV.B, Eq. 7: the text says "Given a sparse dataset $\tilde Y^i$", the loss
  uses $Y^i$; the minimization is over the field $\delta^i_m$, but the
  constraint is written with the parametric model $\delta_m(\tilde\eta_m;w)$.
- §IV.B, Eq. 9: the loss uses $\delta(\tilde\eta_m;w)$ and the constraint
  $\delta_m(\tilde\eta_m;w)$ for the same object.
- §III.B: $\hat q$ is the unresolved part $q-\tilde q$ in §II, but the
  deconvolution is written $\hat q_m=\delta_m(\tilde q_m;w)$ and the SGS stress
  then uses $q_m$ (no hat), $\tau_m=\tilde q_m\otimes\tilde q_m-\widetilde{q_m\otimes q_m}$.
  This SGS stress also carries the opposite sign to the paper's own Reynolds
  stress of Table I, $\tau=\widetilde{(\hat u\otimes\hat u)}$.
- Symbol reuse: $f$ is the SGS scalar flux (Table I) and the SGS force
  (§III.A); $k$ is the turbulent kinetic energy and the number of inversion
  datasets (§IV.B); $T$ is temperature and the tensor basis.
- Typos: "in contrast to a a priori training" (§IV.B); "represened" (§III.A).
- Fig. 4 carries black arrows and green markers not explained in the caption,
  and no source reference.

# Notation map

| Duraisamy (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tilde q$ | $\langle q\rangle$ (RANS) or $\bar q$ (LES) | generic coarse-graining; **not** a Favre filter |
| $\hat q=q-\tilde q$ | $q'$ (RANS) or $q^<$ (LES) | unresolved part; in §III.B the reconstructed sub-filter part. **Collision**: the registry hat is the test filter |
| $\tau=\widetilde{(\hat u\otimes\hat u)}$ | $R_{ij}$ | kinematic, positive trace (Table I); agrees in sign |
| $\tau_m=\tilde q_m\otimes\tilde q_m-\widetilde{q_m\otimes q_m}$ (§III.B) | $-\tau_{ij}$ | SGS stress printed with the negative convention |
| $\tau_b$ | $R^{\mathrm{b}}_{ij}$ | baseline-model stress (§VI) |
| subscript $m$ | modelled quantity | un-subscripted = DNS or experiment |
| $k_m$, $\varepsilon_m$ | $k$, $\varepsilon$ of the model | |
| $\tilde V_m$, $\tilde\Lambda_m$, $I$ | eigenvector and eigenvalue matrices of the modelled anisotropy $b_{ij}$; $\delta_{ij}$ | Tracey et al. equation (§III.A) |
| $\delta$, $\delta^i_m$, $Y^i$ | target $\boldsymbol\delta$ extracted from DNS; inverted field $\beta(\boldsymbol x)$ of dataset $i$; data of dataset $i$ | Eqs. 5, 7 |
| $\tilde S_m$, $\tilde\Omega_m$ | $\langle S_{ij}\rangle$ or $\bar S_{ij}$; $\langle\Omega_{ij}\rangle$ or $\bar\Omega_{ij}$ | $\lvert\tilde S_m\rvert$ is not defined in the paper |
| $T^{(n)}$, $\delta^{(n)}_m$ | $T^{(n)}$, $g^{(n)}$ | integrity basis and its coefficients (Eq. 4) |
| $\delta_m(\tilde\eta_m;w)$ | $\boldsymbol\delta(\boldsymbol\zeta;\boldsymbol\theta)$ | learned correction |
| $\tilde\eta$, $\tilde\eta_m$ | $\boldsymbol\zeta$ | features from DNS and from the model. **Collision**: the registry $\eta$ is the Kolmogorov length |
| $w$ | $\boldsymbol\theta$ | trainable parameters |
| $\mathcal L$ | $\mathcal L$ | loss function; agrees |
| $\lambda$ | $\ell_1$ regularization weight | **collision** with the registry Taylor microscale $\lambda$ |
| $\Delta$ | $\Delta$ | filter width; agrees |
| $f$ | SGS scalar flux; SGS force $\partial_j\tau_{ij}$ | two meanings in the source; the registry $f_i$ is a body force |
| $\mathcal R$, $\mathcal N$, $F$, $\mathcal G_m$, $\mathcal R_a$, $Y$ | governing operator, known operator on the unclosed term, unclosed term, secondary-variable equations, augmented model, observables | paper-specific framing (§II) |
| $f_{NN}$, $e(t)$, $t^*$ | super-resolution map, accumulated error, time (Fig. 1) | $t^*$ normalization not given |
| a priori / on-line | a priori / a posteriori | the paper says "on-line" for use inside the solver |

# Reference list

The accepted manuscript prints 84 numbered references ([1]–[84]), with no
DOIs. The list is merged complete into the [bibliography](/bibliography.md)
with `citedby` duraisamy-2021. Ref. [5] is the ingested source
[Duraisamy et al. (2019)](/sources/duraisamy-2019.md). Ref. [32] is a verbatim
duplicate of ref. [79] (Mishra et al. 2016) and is recorded as that one work,
with a note that the text cites it for Kaandorp & Dwight. Ref. [61] is an
unresolved placeholder ("Manuscript in preparation. Bibliography details to be
available while this article is under review., 2018"); ref. [71] prints a
garbled author ("M-uacute, J.-D., ller", recorded as Müller J.-D.); ref. [43]
prints "Weinan, E." for E W.; ref. [60] prints a third author "de Bragança A.,
F. A. V." (kept as printed); ref. [19] (Durbin, Annu. Rev. Fluid Mech. 2017)
has no volume or pages.

# Pages created or updated

Chunk 1 (2026-10-25). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Discretization-consistent closure](/definitions/discretization-consistent-closure.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Machine-learning wall models](/methods/machine-learning-wall-model.md)
- [Model-consistent (a posteriori) training of learned closures](/methods/model-consistent-training.md)
- [Reinforcement-learning turbulence closures](/methods/reinforcement-learning-closure.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Tensor-basis neural network and the integrity basis](/methods/tensor-basis-neural-network.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
