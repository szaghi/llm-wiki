---
type: Method
title: "Field inversion and machine learning"
description: "Field inversion infers a spatial correction field of a RANS model from data by solving a PDE-constrained inverse problem; FIML then learns that field as a function of local flow features and embeds the learned map in the solver, so the training targets come from the model's own environment."
status: established
aliases: [FIML, field inversion, field-inversion and machine-learning, inference before learning]
tags: [field-inversion, data-driven, machine-learning, rans, uncertainty-quantification, separated-flow]
timestamp: 2026-10-25T19:46:00Z
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
[Yan et al. (2022)](/sources/yan-2022.md) (§2.1, Eq. 6) write the same MAP
problem explicitly. With Gaussian, pointwise-independent data and
correction values and a prior mean $\beta=1$ (the baseline model), FI
minimizes

$$\mathcal L=\sum_i\sigma_{\mathrm{obs}}^{-2}\big(Y_i-Y_{\mathrm m,i}(\beta)\big)^2+\sum_j\sigma_\beta^{-2}(\beta_j-1)^2,$$

where $\beta_j$ is the value of $\beta$ at grid point $j$ and
$\sigma_{\mathrm{obs}}$, $\sigma_\beta$ (page-local) are the observation and
prior standard deviations (the paper calls them variances, but they enter
as $\sigma^{-2}$). The second term is a regularization; relative to the
data misfit its weight is $\sigma_{\mathrm{obs}}^2/\sigma_\beta^2$ *(compiler
check, not in the sources)*.

**Solvers.** Duraisamy et al. (2019, §5.1) list adjoint-based optimization
and derivative-free iterative ensemble Kalman methods. Yan et al. (2022,
§2.2, Eqs. 7–11) use the discrete adjoint of the ADflow solver, built with
the Tapenade automatic-differentiation tool, with one adjoint solve giving
the gradient with respect to every $\beta_j$. An augmented discrete adjoint
holds a constraint fixed during the inversion: the lift coefficient on the
airfoils, the bulk velocity on the hills, where the driving volume force
is adjusted automatically.

**What is inverted.** Duraisamy et al. (2019, §5.1) recall three kinds of
inversion:

- an eddy-viscosity field from full-field DNS velocity (Dow & Wang);
- multipliers of transport-equation terms from limited surface data, for
  channel flow, shock/boundary-layer interaction, curvature and separation
  (Duraisamy et al.; Singh & Duraisamy);
- Reynolds-stress magnitude and anisotropy from sparse velocity data
  (Xiao et al.; Wu et al.).

Duraisamy (2021, §IV.B) adds the mean-flow momentum equation as a target.
Yan et al. (2022) invert the production multiplier of Spalart–Allmaras
from deliberately scarce data: the experimental lift coefficient alone
(S809 airfoil), DNS mean-velocity profiles at a few stations (parametrized
hills), and lift alone or lift and drag (iced airfoil).

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

## Application to separated flows (Yan et al. 2022)

Yan et al. (2022) apply the three steps to the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md) in 2D steady
RANS of three separated flows, with $\beta(\boldsymbol x)$ multiplying only
the production term $c_{b1}\tilde S\tilde\nu$ ($\beta=1$ recovers the
baseline; §2.1, Eq. 5), the same form as the representative example above.

**Physical motivation.** As recalled there (§1), models are calibrated in
equilibrium shear flows where $P_k/\varepsilon$ is about 1.4 to 1.8, while
in separating shear layers, corner separation and compressor boundary
layers production can greatly exceed dissipation. Ad hoc fixes generalize
poorly: as recalled by the authors, Rumsey's separation fix of SST improves
the periodic hill but worsens backward-step flows, and LES of Fang et al.
shows production both increased and decreased in such regions, where the
authors' own earlier separating-shear-layer fix only increased it. The
authors read $\beta$ as "closely related to the equilibrium state of the
turbulence".

**Non-uniqueness and physics-shaped priors.** Many correction fields
reduce the observed error enough (§3.1.1, Figs. 4–5). Without
regularization, inversion on the hills gives an irregular field with no
general tendency, which "might be not physical" (§3.2.1, Fig. 18). The
authors shape the prior from the nonequilibrium mechanism: a nonuniform
$\sigma_\beta$ (on S809, 200 for $x<1.0$ and 20 for $x>1.0$, Eq. 15, with
$x$ not defined in the paper; motivated by the strong adverse pressure
gradient near the boundary layer) or corrections
confined to a box over the separating shear layer (hills, Case 2). A
uniform prior with the same weight (Case 3) gives a correction similar to
the box-limited one, which the authors take as evidence that FI captures
the [model-form uncertainty](/definitions/model-form-uncertainty.md) in the
critical region "with less human intervention" (§3.2.1, Table 2).

**Where the corrections sit.** On the hills and the iced airfoil the
inferred $\beta$ is below one at the start of the separating shear layer
and above one downstream, so turbulent mixing is both reduced and enhanced
(§3.2.1, §3.3.1, Figs. 18, 26). The enhanced region coincides, by visual
comparison, with the region where the authors' earlier
$k$-$\overline{v^2}$-$\omega$ separation fix activates (where
$P_k/\varepsilon\gg1$) and with Rumsey's fix region (Figs. 11, 18, 27). On
S809 at $8^\circ$ and $14^\circ$ the inversion from lift alone suppresses
production mainly in the strong adverse-pressure-gradient region and
enlarges the separation (Fig. 6).

**Unobserved quantities improve.** On S809 the pressure distribution
improves though only lift was observed (Fig. 7). On the hills the
lower-wall $C_f$ improves though only velocity was observed (Fig. 16). On
the iced airfoil (GLC305 with horn-ice shape 944, $M=0.12$,
$Re_c=3.5\times10^6$) baseline SA gives $C_L=0.393$ and 0.495 at $4^\circ$
and $6^\circ$ against 0.489 and 0.669 measured; inversion on lift and drag
(FI1) matches both to the printed digits, inversion on lift alone (FI2)
gives $C_D=0.0648$ and 0.0950 against 0.0566 and 0.1024, and FI1 gives the
better pressure plateau. The authors conclude that more observations make
the assimilation more credible (§3.3.1, Table 3, Fig. 28). At $6^\circ$ the
corrected separation bubble covers about half the chord instead of the
whole airfoil (Fig. 25).

**Learning step.** A fully connected network (three hidden layers, sigmoid
activations, batch normalization, z-score inputs, Adam, mean-squared loss)
maps eight local features to $\beta$: $\chi$, the SA production and its
ratio to destruction, the strain-rate magnitude and its ratio to the
vorticity magnitude, a Reynolds-stress magnitude, a modified DES shielding
function $1-\tanh(r_d^{0.5})$ and $\lvert\nabla\tilde\nu\rvert$ (§2.3; the
norm conventions and $r_d$ are not defined in the paper). Networks are
preferred to Gaussian processes and random forests because their
evaluation cost does not grow with the training set, which matters for a
model called at every grid point and iteration (§2.3). Network size and
epochs are chosen by the a posteriori error of the embedded model, not by
the validation loss, because the two are not monotonically related
(§3.1.2, Table 1; see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

**Prediction results.**

| Case | Training data | Network, samples | A posteriori result |
|---|---|---|---|
| S809, $M=0.10$, $Re_c=2\times10^6$ | FI at $8^\circ$ and $14^\circ$ | (16, 16, 8), 300 epochs, 88 658 | lift error 2.4% at $8^\circ$, $-0.1\%$ at $14^\circ$ (Table 1); lift and drag improved at $Re_c=1$, 2 and $3\times10^6$ over a range of incidence, drag not used in FI (Fig. 10) |
| Parametrized hills, $Re_b=5600$ | FI on two hill-width factors | (32, 16, 8), 11 200 | closer to DNS than SA in most regions at an interpolated width (1.0) and extrapolated widths (0.5, 1.5); "can still be further promoted" (§3.2.2, Fig. 22) |
| GLC305/944 | FI1 at $4^\circ$ and $6^\circ$ | (64, 32, 16), 2000 epochs, 131 328 | lift error from $-21.5\%$ to $-7.0\%$ ($4^\circ$) and $-26.8\%$ to $-5.5\%$ ($6^\circ$); drag error from 6.4% to 3.5% and $-7.1\%$ to $-6.3\%$ (Table 4); good for incidence below $6^\circ$, deteriorating beyond (Fig. 33) |

The hills are the parametrized family of Xiao et al. (hill width scaled at
fixed height, $Re_b=5600$ on crest height and bulk velocity at the crest),
not the configuration of the [periodic hill](/benchmarks/periodic-hill.md)
benchmark at $Re_h=10{,}595$ (§3.2). All evidence is 2D steady RANS.

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
- Yan et al. (2022, §3.1.2, Table 1) give a concrete instance of the
  inconsistency that Duraisamy (2021) assigns to the regression step: on
  S809, regression error and a posteriori lift error of the embedded model
  are not monotonically related across twelve network settings. The paper
  keeps the two-step form and moves the model selection, not the training,
  into the solver (see
  [model-consistent training](/methods/model-consistent-training.md)).

## Qualifications

- **Identifiability.** Duraisamy (2021, §VII, Fig. 4) shows a
  model-consistent inference in channel flow. An anisotropy perturbation is
  inferred from mean-velocity data. It reproduces the mean velocity and the
  Reynolds shear stress accurately, but not the anisotropy. The author
  states that using the full Reynolds-stress tensor as data would remedy
  this. No Reynolds number is given. Yan et al. (2022, §3.1.1, §3.2.1)
  meet the same problem as the non-uniqueness of $\beta$ when the data
  are a single integral quantity, and answer it with priors rather than
  with more data, except on the iced airfoil, where adding drag to lift
  improves the unobserved pressure (§3.3.1).
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
- Yan et al. (2022) print slips that bear on the numbers above. The text
  of §3.2.2 names the two hill training geometries as width factors 0.5
  and 0.8, while the same section calls 0.5 an extrapolation case; the
  training set is therefore ambiguous as printed. The periodic-hill
  objective (Eq. 17) carries an index mismatch ($\lambda_i$ under a sum
  over $j$), and the text then uses a scalar weight $\lambda=8\times10^{-6}$.
  Table 4's baseline SA errors ($-21.5\%$, $-26.8\%$ in lift) do not equal
  the relative errors computed from Table 3 ($-19.6\%$, $-26.0\%$)
  *(compiler check, not in the sources)*; the reductions quoted above are
  those of Table 4.
- Yan et al. (2022) write the SA working variable as $\tilde\nu$ and the
  data as $d_i$, the model prediction as $h_i(\boldsymbol\beta)$, the
  features as $\eta$; this page translates them to $Y_i$,
  $Y_{\mathrm m,i}(\beta)$ and $\boldsymbol\zeta$. The paper's $\alpha$ is
  both the angle of attack and the hill-width factor; the page uses words
  for both.

# Citations

- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §2 (layers L1–L4), §3.2 and box p. 7 (MAP), §4.1, §5.1 (field inversion, Figs. 4–5), §5.2 (feature space), §5.4 and §6 (FIML, Fig. 8; inference before learning).
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §I, §IV.B, Eqs. 7–9 (FI, FIML, integrated training), §V (features), §VII (identifiability, Fig. 4; generalization).
- [Yan et al. (2022)](/sources/yan-2022.md) — accepted manuscript, §1, §2.1–2.3, Eqs. 5–11, 14–17; §3.1 (S809, Figs. 4–7, 10, Table 1); §3.2 (parametrized hills, Figs. 11, 13–22, Table 2); §3.3 (GLC305/944, Figs. 25–33, Tables 3–4).
