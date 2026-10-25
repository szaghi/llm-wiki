---
type: Method
title: "Field inversion and machine learning"
description: "Field inversion infers a spatial correction field of a RANS model from data by solving a PDE-constrained inverse problem; FIML then learns that field as a function of local flow features and embeds the learned map in the solver, so the training targets come from the model's own environment."
status: established
aliases: [FIML, field inversion, field-inversion and machine-learning, inference before learning]
tags: [field-inversion, data-driven, machine-learning, rans, uncertainty-quantification]
timestamp: 2026-10-25T13:43:00Z
---

# Field inversion and machine learning

**Field inversion** (FI) treats a correction of a RANS closure as an unknown
field, $\beta(\boldsymbol x)$, and infers it from data by solving an inverse
problem constrained by the model equations. In the representative example
of Duraisamy et al. (2019, §5.1), $\beta$ multiplies the production term of
the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md). The inferred
field belongs to one geometry and one flow condition. **Field inversion and
machine learning** (FIML) generalizes it in three steps. Field inversion is
run on several datasets. A regression model
$\beta\approx f(\boldsymbol\zeta;\boldsymbol\theta)$ is then trained on the
inferred fields as a function of local flow features $\boldsymbol\zeta$.
Finally, the learned map is embedded in the RANS solver as a correction
(Duraisamy et al. 2019, §5.4; Duraisamy 2021, §IV.B, Eqs. 7–8). The
sources present FIML as a remedy for the inconsistency between
learning from DNS and predicting in RANS (see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

## Place in the modelling framework

Duraisamy et al. (2019, §2) sort RANS modelling assumptions into four
layers:

- **L1**, the information lost by averaging, which they call
  "fundamentally irrecoverable";
- **L2**, the representation of $R_{ij}$ in terms of the averaged
  variables (e.g. the [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md));
- **L3**, the functional form of the model operators;
- **L4**, the coefficient values.

Calibrating coefficients, by Bayesian inference or otherwise, addresses L4
only (§5.1). A spatially varying field is needed because the discrepancy
enters through the divergence of the Reynolds stress and is "likely
spatially varying" (§4.1). Field inversion instead lets the data inform the
L3 operators. The authors read the inferred multiplier as data acting on the
functional form (§5.1). See
[model-form uncertainty](/definitions/model-form-uncertainty.md) for the
layers and for the realizability-constrained perturbation alternatives.

## Step 1: field inversion

Let $\boldsymbol Y$ denote the available data (page-local: observables
such as $C_p$, $C_f$, sparse velocities, or a lift coefficient), and
$\boldsymbol Y_{\mathrm m}(\beta)$ the same observables computed by the
augmented model. Duraisamy (2021, Eq. 7) writes FI for dataset $i$ as

$$\min_{\beta^{(i)}}\ \mathcal L\big[\boldsymbol Y^{(i)},\boldsymbol Y^{(i)}_{\mathrm m}(\beta^{(i)})\big]\quad\text{subject to the augmented RANS equations,}$$

which yields a problem-specific field $\beta^{(i)}(\boldsymbol x,t)$. Two
properties follow from this form. FI is consistent with the model, and it
does not require full-field DNS (§IV.B). Duraisamy et al. (2019, box p. 7)
give the Bayesian reading. With Gaussian prior and likelihood, the maximum
a posteriori (MAP) estimate minimizes a data misfit weighted by the
observation covariance plus a prior misfit weighted by the prior covariance.
Using only the posterior mode makes the estimate deterministic (§3.2).

**Solvers.** Duraisamy et al. (2019, §5.1) list adjoint-based optimization
and derivative-free iterative ensemble Kalman methods.

**What is inverted.** Duraisamy et al. (2019, §5.1) recall three kinds of
inversion:

- an eddy-viscosity field from full-field DNS velocity (Dow & Wang);
- multipliers of transport-equation terms from limited surface data, for
  channel flow, shock/boundary-layer interaction, curvature and separation
  (Duraisamy et al.; Singh & Duraisamy);
- Reynolds-stress magnitude and anisotropy from sparse velocity data
  (Xiao et al.; Wu et al.).

Duraisamy (2021, §IV.B) adds the mean-flow momentum equation as a target.

**Representative example.** As recalled by Duraisamy et al. (2019, §5.1,
Figs. 4–5, from Singh & Duraisamy 2016), $\beta$ multiplies the production
term of Spalart–Allmaras in a channel with a convex wall. It is inferred
only from LES $C_f$ on the lower convex wall. The inverted model reproduces
the LES velocity and Reynolds stresses well and improves considerably on
both SA and its rotation–curvature variant SARC. The review states that the
trend of the inferred field is consistent with convex curvature reducing
turbulence, and that the comparison suggests SARC needs improvement in the
log layer. The review gives no Reynolds number for this case.

## Step 2: learning the inferred fields

Inferred fields are tied to one geometry and flow condition. Duraisamy et
al. (2019, §5.2) name the remedy: map the discrepancy from physical space
to a feature space. They credit Tracey et al. (2013) with this step.
Duraisamy (2021, §I) calls it the key advance over the earlier
uncertainty-quantification work.

FIML collects the fields of $k$ datasets,
$\{\beta^{(1)},\dots,\beta^{(k)}\}$, with their model-computed features
$\{\boldsymbol\zeta^{(1)}_{\mathrm m},\dots,\boldsymbol\zeta^{(k)}_{\mathrm m}\}$
(page-local: subscript $\mathrm m$ marks a quantity computed from the
model's own solution). It then solves the supervised problem

$$\min_{\boldsymbol\theta}\ \mathcal L\big[\{\beta^{(i)}\},\,f(\{\boldsymbol\zeta^{(i)}_{\mathrm m}\};\boldsymbol\theta)\big]$$

(Duraisamy 2021, Eq. 8). Duraisamy writes $k$ for the number of datasets;
it is not the turbulent kinetic energy. The difference from a
priori learning is that both targets and features come from model
solutions, not from coarse-grained DNS. Duraisamy (2021, §V) gives the
feature guidelines: local non-dimensionalization, rotational, reflectional
and frame invariance of the features and of the normalizing variables, and
a preference for local features. Wall distance, wall-stress measures and
pressure-gradient features have proved important as non-local surrogates.

## Step 3: prediction

The learned $f$ is embedded in the solver, so the RANS equations are solved
with $\beta=f(\boldsymbol\zeta_{\mathrm m};\boldsymbol\theta)$ evaluated
from the running solution. As recalled by Duraisamy et al. (2019, §5.4,
Fig. 8, from Singh et al. 2017), a data-driven Spalart–Allmaras model for
airfoils with separation improves the surface pressure markedly over the
baseline, even when the data are "very limited experimental measurements,
such as the lift coefficient". As recalled by Duraisamy (2021, §VII),
FIML-augmented models improve predictions on cases close to their training
set, e.g. an airfoil of slightly different shape. Duraisamy (2021, §IV.B)
states that FIML has been used in transition modelling as well as
turbulence modelling.

## Consistency claims

Both reviews argue that FIML is preferable to learning directly from DNS,
because the training targets come from the environment in which the model
is used:

- Duraisamy et al. (2019, §5.4, §6) recommend that inference precede
  learning, which "enforces consistency" between the learning and
  prediction environments.
- Duraisamy (2021, §IV.B) states a weaker version. FIML "promotes"
  consistency, but imperfections of the regression step (Eq. 8)
  reintroduce inconsistency. Only an integrated optimization, in which the
  learned map sits inside the constraint and the loss is evaluated on model
  outputs, "ensures full consistency" (Eq. 9; see
  [model-consistent training](/methods/model-consistent-training.md)).
- The integrated route has a cost: features must be chosen before
  inference. The separate FI and ML stages are more flexible (§IV.B).

## Qualifications

- **Identifiability.** Duraisamy (2021, §VII, Fig. 4) shows a
  model-consistent inference in channel flow. An anisotropy perturbation is
  inferred from mean-velocity data. It reproduces the mean velocity and the
  Reynolds shear stress accurately, but not the anisotropy. The author
  states that using the full Reynolds-stress tensor as data would remedy
  this. No Reynolds number is given.
- **Generalization.** Duraisamy (2021, §VII) states that "the goal of more
  generalizable models has, however, not been achieved". Machine-learning
  regressions are interpolative in feature space (§V), and a model with
  $n$ features needs data that populate an $n$-dimensional space (the
  paper's $d$; renamed here because $d$ is the wall distance).
- **L1 errors remain.** Single-point, Markovian closures carry structural
  errors that no learned correction removes (Duraisamy 2021, §VII;
  Duraisamy et al. 2019, §2).
- The two reviews use different symbols for the same objects. Duraisamy
  et al. (2019) write the data as $\boldsymbol\theta$, the features as
  $\boldsymbol\eta$ and the discrepancy as $\boldsymbol\delta$. Duraisamy
  (2021) writes the data as $Y$, the features as $\tilde\eta_m$, the
  network weights as $w$ and the inferred field as $\delta^i_m$. This page
  translates all of them to the registry.
- Duraisamy (2021) prints Eq. 7 with the parametric model
  $\delta_m(\tilde\eta_m;w)$ in the constraint, although the optimization
  variable is the field $\delta^i_m$. The text also introduces the data as
  "$\tilde Y^i$" while the loss uses $Y^i$. This page writes the
  constraint with the field being inferred, as the surrounding text
  describes.

# Citations

- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §2 (layers L1–L4), §3.2 and box p. 7 (MAP), §4.1, §5.1 (field inversion, Figs. 4–5), §5.2 (feature space), §5.4 and §6 (FIML, Fig. 8; inference before learning).
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §I, §IV.B, Eqs. 7–9 (FI, FIML, integrated training), §V (features), §VII (identifiability, Fig. 4; generalization).
