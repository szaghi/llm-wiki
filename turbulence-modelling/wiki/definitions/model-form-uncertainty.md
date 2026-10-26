---
type: Definition
title: "Model-form uncertainty in turbulence closures"
description: "The uncertainty that comes from the structure of a turbulence closure rather than from its inputs or coefficients; the four layers of RANS assumptions, physics-based bounds, Bayesian calibration and discrepancy fields, stochastic discrepancies trained on indirect data, where to place the correction, non-unique inversions, identifiability, confidence scores and compensating errors."
status: established
aliases: [model-form uncertainty, structural uncertainty, epistemic uncertainty, aleatoric model uncertainty, model discrepancy, RANS uncertainty quantification, eigenspace perturbation, stochastic discrepancy closure]
tags: [uncertainty-quantification, rans, data-driven, field-inversion]
timestamp: 2026-10-26T10:25:00Z
---

# Model-form uncertainty in turbulence closures

Model-form uncertainty is the part of a prediction's error that comes from
the limitations of the physical model itself, as opposed to the imprecision
or variability of its inputs. Duraisamy et al. (2019) separate *aleatory*
uncertainty (imprecise or naturally variable inputs) from *epistemic and
model-form* uncertainty (limitations of the physics models); an uncertainty
description, probabilistic or an interval, is propagated through the model
to a quantity of interest, and for nonlinear models the extreme inputs need
not give the extreme outputs ([Duraisamy et al. (2019)](/sources/duraisamy-2019.md),
box "Uncertainty quantification", p. 5). In turbulence closures the model
discrepancy $\boldsymbol\delta$ (registry) is the gap between what the closure
can represent and the data, and it is the target of most data-driven
corrections.

Page-local symbols: $\mathcal N$ the Navier–Stokes operator, $\mathcal M$ the
closure model, $\mathcal P$ its algebraic or differential operators,
$\boldsymbol d$ the data with uncertainty $\boldsymbol\epsilon_d$, $\boldsymbol o$ the
model output that corresponds to the data, $\boldsymbol q$ a quantity of
interest. The model coefficients are the registry's $\boldsymbol\theta$ and
the features its $\boldsymbol\zeta$ (Duraisamy et al. write $\mathbf c$ and
$\boldsymbol\eta$, and use $\boldsymbol\theta$ for the data).

## Four layers of RANS assumptions

Duraisamy et al. (2019, §2, Eqs. 1–6) locate where a RANS model can be wrong:

- **L1, averaging:** $\langle\mathcal N(\cdot)\rangle\neq\mathcal N(\langle\cdot\rangle)$.
  Infinitely many instantaneous fields share one mean and may evolve
  differently, "leading to hysteresis-like phenomena". The uncertainty from
  this layer is "fundamentally irrecoverable regardless of the
  sophistication of the turbulence model".
- **L2, representation:** $\langle\mathcal N(\cdot)\rangle=\mathcal N(\langle\cdot\rangle)+\mathcal M(\cdot)$,
  with $\mathcal M=\nabla\cdot R$ for incompressible flow, a function of
  averaged variables, local (one-point) or non-local (two-point). The
  [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md) and algebraic
  stress models are L2 choices.
- **L3, functional form:** the operators $\mathcal P$, mimicking convection and
  diffusion, with source terms for wall and rotation effects.
- **L4, coefficients:** values set by asymptotic consistency or empirical
  evidence; the value of $C_\mu$ is "a classical L4 closure issue". Optimal
  coefficients are flow-specific, as the free-shear-flow values listed by
  Pope and Eisfeld show, so default values carry L4 uncertainty in complex
  flows (§4.2).

Duraisamy (2021) restates L1 for both RANS and LES: coarse-graining is exact
but unclosed (the coarse-grained equations equal the model equations of
the coarse variables plus a known operator acting on an unclosed term), and
the discrepancy between a coarse-grained model and the truth is in part
irrecoverable; single-point and Markovian closure structures add errors no
learned correction inside that structure can remove
([Duraisamy (2021)](/sources/duraisamy-2021.md), §II Eq. 2, §VII).

## Bounding from physical constraints

**Formal bounds.** The background-flow method (Howard; Busse;
Doering–Constantin; Seis, as recalled by Duraisamy et al. 2019, §4.1) bounds
quantities such as the dissipation for channel, shear and convective flows;
the authors find it "difficult to envision" such bounds for engineering
flows.

**Realizability.** Realizability constrains the eigenvalues of the Reynolds
stress strongly, the kinetic energy only weakly (non-negativity), and the
eigenvectors not at all (§4.1, Fig. 1).

**Eigenspace perturbation** (inline here). Writing the Reynolds stress through
its normalized anisotropy, $b_{ij}=V\Lambda V^{\top}$ with eigenvector matrix
$V$ and eigenvalue matrix $\Lambda$ (page-local),

$$R_{ij}=2k\Big(\tfrac13\delta_{ij}+(V\Lambda V^\top)_{ij}\Big),$$

the baseline RANS stress is perturbed in $k$, $\Lambda$ and $V$
([Duraisamy et al. (2019)](/sources/duraisamy-2019.md), §4.1, Eq. 10).
Emory et al. move the eigenvalues towards the one-, two- and
three-component vertices of the barycentric triangle; Iaccarino et al.
(2017) bound the eigenvectors by the two alignments that give maximum and
minimum production of $k$. Simulations at the extreme states give a
prediction interval $[\boldsymbol q^-;\boldsymbol q^+]$, which for a turbulent jet
"appear[s] to provide a satisfactory representation" of the model
uncertainty (Fig. 2, from Mishra & Iaccarino 2017). Tracey et al. learned
the eigenvalue perturbation from DNS by kernel regression in feature space,
the start of the machine-learning strand, as recalled by Duraisamy (2021,
§I, §III.A).

**Random matrices.** Xiao et al. (2017) treat the true stress as a random
symmetric positive semi-definite matrix whose mean is the RANS stress,
sampled from a maximum-entropy distribution. Eigenvalue and eigenvector
uncertainty are explored jointly, but without the "clear interpretations of
the limiting states" of the eigenspace approach; both approaches guarantee
realizability (§4.1).

## Calibration and discrepancy fields

Duraisamy et al. (2019, §3) express each class of data use as a form of the
calibrated model:

- **naive calibration** fits $\boldsymbol\theta$ to $\boldsymbol q$ and ignores
  measurement uncertainty, treating the coefficients as the dominant error
  source, a process that "has led to the proliferation of turbulence model
  variants" (§3.1, Eq. 7);
- **Bayesian inference** adds a discrepancy and the data noise,
  $\widetilde{\mathcal M}=\mathcal M(\boldsymbol\theta)+\boldsymbol\delta+\boldsymbol\epsilon_d$,
  with a Gaussian-random-field prior on $\boldsymbol\delta$ and Markov-chain
  Monte Carlo sampling, or with the posterior mode (MAP) only (§3.2, Eq. 8):
  $$\boldsymbol\theta_{\mathrm{MAP}}=\arg\min\tfrac12\Big[(\boldsymbol d-\boldsymbol o(\boldsymbol\theta))^{\top}Q_d^{-1}(\boldsymbol d-\boldsymbol o(\boldsymbol\theta))+(\boldsymbol\theta-\boldsymbol\theta_{\mathrm{prior}})^{\top}Q_\theta^{-1}(\boldsymbol\theta-\boldsymbol\theta_{\mathrm{prior}})\Big],$$
  with $Q_d$, $Q_\theta$ the observation and prior covariances (page-local);
- **Kennedy–O'Hagan** calibration adds a Gaussian-process discrepancy to the
  model *output*; the review calls it "black-box and thus physics-agnostic"
  and prefers discrepancies embedded inside the model (§3.4).

Applications recalled in §5.1 address L4 only: posterior distributions of
coefficients from channel DNS (Oliver & Moser 2011; Cheung et al. 2011,
called "the first" to do so), Bayesian model-scenario averaging (Edeling et
al.), calibration of $k$-$\varepsilon$ for a jet in crossflow (Ray et al.).
Because the stress enters through its divergence, the authors state that
the discrepancy is likely spatially varying, $\boldsymbol\delta(\boldsymbol x)$
(§4.1). Spatial models of it include the Reynolds-stress
discrepancy tensor of Oliver & Moser (2009), a random field obeying
stochastic equations simpler than Reynolds-stress transport, which "laid
the foundation" for later work; Gaussian processes; a "return-to-eddy-viscosity"
transport equation (Edeling et al. 2017); and a PDE-informed covariance
kernel (Wu et al.) (§4.1, §5.1).

Inferring a discrepancy field from data is
[field inversion](/methods/field-inversion-machine-learning.md); mapping it to
features $\boldsymbol\delta(\boldsymbol\zeta)$ so that it generalizes beyond one
geometry is the step to learned closures (§5.2;
[tensor-basis neural network](/methods/tensor-basis-neural-network.md),
[model-consistent training](/methods/model-consistent-training.md)).

## Non-unique inversions and physics-based priors

Yan et al. (2022) infer a spatial multiplier $\beta(\boldsymbol x)$ of the
Spalart–Allmaras production (the registry's field-inversion $\beta$) from
scarce data, assuming Gaussian, pointwise-independent prior and noise with
prior mean one, so that the MAP estimate minimizes

$$\mathcal L=\sum_i\frac{\big(d_i-o_i(\boldsymbol\beta)\big)^2}{\sigma_{\mathrm{obs}}^2}+\sum_j\frac{(\beta_j-1)^2}{\sigma_\beta^2},$$

with $o_i$ the model output at observation $i$ and $\sigma_{\mathrm{obs}}$,
$\sigma_\beta$ observation and prior standard deviations (page-local)
([Yan et al. (2022)](/sources/yan-2022.md), §2.1, Eq. 6). This is twice the
MAP objective of Duraisamy et al. above with diagonal covariances
$Q_d=\sigma_{\mathrm{obs}}^2I$, $Q_\theta=\sigma_\beta^2I$ and prior mean one
*(compiler check, not in the sources)*. Their findings bear on the
identifiability question below:

- **Many corrections fit the same data.** On the S809 airfoil, inversions on
  the lift alone with uniform and non-uniform prior widths give different
  $\beta$ fields that both reduce the error sufficiently (§3.1.1, Figs. 4–5);
  on the parametrized periodic hills an unregularized inversion yields an
  irregular field with no general tendency, which "might be not physical"
  (§3.2.1, Fig. 18).
- **Priors from physical mechanism.** Restricting the correction to a box
  around the separating shear layer, or a uniform regularization weight,
  still fits the data, and both give similar fields that lower the
  production at the start of the shear layer and raise it downstream; the
  authors read the agreement of the uniform-prior case as evidence that the
  inversion "captures" the model-form uncertainty in the critical region
  with little human intervention (§3.2.1, Table 2, Fig. 14).
- **Where the error sits.** The corrected regions coincide with those where
  turbulence is far from equilibrium: models are calibrated in equilibrium
  shear flow, where production exceeds dissipation by a factor of about 1.4
  to 1.8, while in separating shear layers production can be much larger
  (§1). The regions agree with the nonequilibrium switch of the authors'
  earlier $k$-$\overline{v^2}$-$\omega$ model and with Rumsey's separation fix
  of SST (§3.2.1, Figs. 11, 18).
- **More data, more credible inversions.** On an iced airfoil, inverting on
  lift and drag together gives a better pressure plateau, which was not
  observed, than inverting on lift alone (§3.3.1, Fig. 28). Yan et al. also
  recall Rumsey's finding that enhanced mixing in separated shear layers
  helps the periodic hill but worsens backward-facing-step flows, as an
  example of ad hoc corrections that do not generalize (§1).

See [field inversion and machine learning](/methods/field-inversion-machine-learning.md)
and the [SA page](/methods/spalart-allmaras-model.md) for the learned model.

## Where to put the correction

Cato et al. (2023) compare six space-dependent corrections of the
negative Spalart–Allmaras model, each optimized alone by adjoint-based
variational data assimilation against dense DNS mean velocity, with the
cost $\tfrac12\int\lVert\boldsymbol u_{\mathrm m}-\langle\boldsymbol u\rangle\rVert^2$
and no regularization ([Cato et al. (2023)](/sources/cato-2023.md), §II B–D,
Eqs. 5–6). Page-local names, as on the
[field-inversion page](/methods/field-inversion-machine-learning.md): a
momentum forcing $\boldsymbol f_u$; the divergence of a traceless symmetric
tensor $\boldsymbol\Psi$ (a conservative forcing; the source's
$\mathbf R_{\gamma\delta}$); the production multiplier, written in registry
form as $\beta P$ with $\beta-1$ the source's control (the source writes
$(1+\beta)P$ with prior zero); an additive source $f_{\tilde\nu}$ and a
proportional source $g_{\tilde\nu}\tilde\nu$ in the $\tilde\nu$-equation;
and a multiplier $1+\varphi$ of $\nu_t$ in the momentum equation (the
source's $\xi$). The four scalar
corrections keep the solution within the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md): "only the
length-scale of the turbulence is corrected, not the structure of the
Reynolds-stresses" (§II B).

Relative velocity errors $E_u$ after assimilation (Tables I–II):

| Correction | channel ($Re=12\,600$) | periodic hill ($Re_b=2800$) |
|---|---|---|
| baseline SA | $4.9\times10^{-2}$ | $7.1\times10^{-2}$ |
| $\boldsymbol f_u$ | $3.1\times10^{-3}$ | $3.8\times10^{-3}$ |
| $\boldsymbol\Psi$ | $2.9\times10^{-3}$ | $3.7\times10^{-3}$ |
| $\beta$ | $8.4\times10^{-3}$ | $3.2\times10^{-2}$ |
| $f_{\tilde\nu}$ | $8.1\times10^{-3}$ | $7.8\times10^{-3}$ |
| $g_{\tilde\nu}$ | $4.6\times10^{-3}$ | $7.5\times10^{-3}$ |
| $\varphi$ | $1.2\times10^{-2}$ | $4.3\times10^{-2}$ |

The channel is a converging–diverging channel. On a square cylinder at
$Re=22\,000$ the momentum corrections and $g_{\tilde\nu}$ reproduce the DNS, $\beta$
and $f_{\tilde\nu}$ improve it partially, and $\varphi$ "was not able to correct
the field" (§V B, Table III). The $\varphi$ problem can be
ill-conditioned, in agreement with Dow & Wang as the authors recall: its
gradient stays on a plateau while the others fall by three to four orders
of magnitude (§III B; App. B, Fig. 21).

**Non-uniqueness.** Three forms appear in the same paper:

- $\boldsymbol\Psi$ is defined only up to the gradient of a harmonic
  potential, which leaves the force unchanged (§II B);
- matching the mean velocity does not fix the Reynolds stresses: no
  correction reproduces the DNS stresses around the square cylinder, even
  the tensor one, so "the mean-flow prediction can be accurate even though
  the Reynolds stresses are wrong" (§V C, Figs. 16–17);
- in the channel, $\beta$, $f_{\tilde\nu}$ and $g_{\tilde\nu}$ recover the velocity "at the
  expense of large eddy-viscosity corrections, which very strongly
  overshoot the reference values", which the authors call "a classical
  over-learning situation" (§III B, Fig. 6).

They propose, without testing them, penalties on the control or on the
distance of $\nu_t$ from a RANS prior (§III B, Eqs. 19–20). Their summary
table ranks $g_{\tilde\nu}$ with the momentum corrections in all three
flows, while noting that $f_{\tilde\nu}$ and $g_{\tilde\nu}$ are "not naturally
dimensionless" and that vector and tensor corrections pose rotational
invariance problems (§VI, Table III).

**The Boussinesq (L2) choice on one flow.** McConkey et al. (2022) do not
frame their work as uncertainty quantification, but they measure the error
left by the best-fit Boussinesq closure: on a parametrized periodic hill,
even the eddy viscosity fitted to DNS stresses leaves anisotropy errors "on
the order of 100%", and injected into RANS it still gives significant
velocity errors at separation and reattachment, the "upper limit" of a
linear closure based on it
([McConkey et al. (2022)](/sources/mcconkey-2022.md), §II B, Figs. 1–4;
details on the [Boussinesq page](/definitions/boussinesq-hypothesis.md)).

## A stochastic discrepancy inside the closure, trained on indirect data

Agrawal & Koutsourelakis (2024) build the discrepancy into a learned
Reynolds-stress closure and quantify it by Bayesian inference from mean
velocity and pressure only
([Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md); arXiv v2). In
registry form the closure is

$$R=R_{\boldsymbol\theta}(\langle\boldsymbol u\rangle)+\boldsymbol\delta_R,\qquad R_{\boldsymbol\theta}=2k\,b_{\boldsymbol\theta}+\tfrac23k\,I,\qquad b_{\boldsymbol\theta}=\sum_{n=1}^{10}g^{(n)}_{\boldsymbol\theta}T^{(n)},$$

with the parametric part the
[tensor-basis neural network](/methods/tensor-basis-neural-network.md) of
Ling et al. (eight hidden layers of 30 nodes, 6970 parameters, $k$ and
$\varepsilon$ from the standard [$k$-$\varepsilon$](/methods/k-epsilon-model.md)
equations) and $\boldsymbol\delta_R$ (page-local) a latent random field of
stress discrepancies (§2.2, Eqs. 13–17, Table 3). The field is reduced to
$\boldsymbol\delta_R=W\boldsymbol E$, piecewise constant on $N_d$ subdomains
through a Boolean matrix $W$ ($W$, $\boldsymbol E$, $N_d$ page-local; 52
subdomains on a 12,180-node mesh), with an automatic-relevance-determination
prior: each component $E_{J\ell}$ is Gaussian with zero mean and precision
$\Lambda^E_{J\ell}$ (page-local; Gamma hyperprior with both parameters
$10^{-3}$), so that a large precision switches the discrepancy off and the
parametric closure accounts for most of the domain (§2.2.2, Eqs. 19–21).
The posterior over $(\boldsymbol\theta,\boldsymbol E,\Lambda^E)$ given sparse
observations is approximated by stochastic variational inference with point
masses on $\boldsymbol\theta$ and $\Lambda^E$ and diagonal Gaussians on
$\boldsymbol E$; the gradients come from a discrete adjoint of a
finite-element RANS solver coupled to automatic differentiation, i.e.
[model-consistent training](/methods/model-consistent-training.md) (§2.2.3–2.2.4,
App. B). Predictions sample $\boldsymbol E$ from its prior at the inferred
precisions and solve the RANS equations once per sample (§2.2.5, Eq. 32).

**Classification of the uncertainty.** The authors call the parametric
uncertainty in $\boldsymbol\theta$ epistemic, since its posterior collapses to
a point with infinite data, and the closure's model-form error *aleatoric*:
it stems from an insufficient parametric form and from the loss of
information in local (Markovian) input features, and the latent
$\boldsymbol\delta_R$ "remain random even in the limit of infinite data"
(title, §1, §2.2 after Eq. 13). See Qualifications for the difference in
terms from Duraisamy et al. (2019).

**Results on a backward-facing step.** Trained on LES mean fields at step
Reynolds numbers 300, 700, 900 and 1100 (observations at about 8% of the
nodes, no Reynolds-stress data) and tested at 500, with expansion ratio 2
(§3.1–3.2; see [backward-facing step](/benchmarks/backward-facing-step.md)):

- the learned parametric stress captures the main features of the LES
  stress, which the baseline badly misrepresents; the inferred precision is
  small, i.e. the discrepancy large, where the parametric stress errs most
  ($5<x/h<10$) and very large far downstream (§3.4, Fig. 7);
- the predicted mean fields agree with the LES although the stresses do
  not, which the authors read as non-uniqueness of the inverse problem, as
  "also reported by other works" (§3.4); this is the identifiability point of
  the next section;
- the predictive standard deviation is largest around the shear layers, and
  the credible intervals envelop the LES "in most areas" (Figs. 8–12);
- the reattachment length is $10.06\pm1.21$ step heights ($\pm3$ standard
  deviations) against 9.10 for the LES, 5.61 for the baseline
  $k$-$\varepsilon$ model and 5.52 for the tensor-basis network of Geneva &
  Zabaras, whose low value the authors attribute, as a conjecture, to the
  missing stochastic correction (Table 5);
- one run costs 1.3 baseline RANS runs, the LES 7679 (Table 4).

The authors state that the discrepancy depends on grid and geometry, so it
transfers to new flow conditions in the same geometry but not to a new
geometry (§2.2.3, §2.2.5), and they claim that uncertainty quantification
"has not been addressed for data-driven turbulence model training with
indirect observations" (§1).

## Identifiability and data–model consistency

Duraisamy (2021) shows a channel-flow inference of an anisotropy perturbation
from mean-velocity data that reproduces the mean velocity and shear stress
accurately but not the anisotropy: the data do not identify the full
discrepancy, which the full Reynolds-stress tensor as data would remedy
(§VII, Fig. 4). Latent RANS variables such as the dissipation rate supply
scale information and differ from their true values, so discrepancies
learned directly from DNS are inconsistent with the model environment;
substituting DNS Reynolds stresses into RANS can still give poor velocity
fields, partly because the RANS equations can be ill-conditioned
(Duraisamy et al. 2019, §5.4, §6; Duraisamy 2021, §IV.A; see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

## Confidence of a learned closure and the location of its error

Lozano-Durán & Bae (2023) attach to each prediction of their
[building-block-flow wall model](/methods/building-block-flow-wall-model.md)
a confidence score in $[0,1]$ built from the distance of the input to its
nearest neighbour in the training set, "based on the ratio $d_s/d_i$
(clipped to be less than 1)", with $d_i$ that distance and $d_s$ the mean
distance of that training sample to its ten nearest training samples
(page-local symbols; [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md),
§2.6). The score measures similarity to the training data, not an error
bound: low confidence may still come with an accurate prediction and high
confidence with an inaccurate one; the authors point to uncertainty
quantification frameworks as the way to an error estimate (§5(2)). In use it
flags the inputs farthest from the training flows: below 20% at the
leading edges of nacelle, slats and flaps of a high-lift aircraft, where
the grid has no point inside the boundary layer, and in the separated
regions near wing tip and root; 22% in the trailing-edge corner separation
of the [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md), where the
prediction is "far from satisfactory"; 0% for random inputs (§4.7–4.8,
Table 1, Figs. 16, 18).

The same paper separates where the error of a wall-modelled LES comes
from. Training and testing the model inside an LES whose subgrid model is
corrected to be "exact for the mean" isolates the *internal* error of the
wall model from the *external* error that the subgrid model makes at the
matching point; the learned model reduces the internal error well below
that of the equilibrium wall model, yet the total error is dominated by
the external one, so the authors conclude that further gains need better
subgrid models (§4.1, §4.7, §5(4), §6; see
[wall-modelled LES](/methods/wall-modelled-les.md) and
[machine-learning wall models](/methods/machine-learning-wall-model.md)).
This is the LES counterpart of the RANS question above of which model
layer carries the discrepancy.

**Agreement through compensating errors.** Three sources show quantities
right for the wrong reason. Lozano-Durán & Bae (2023) find the total error
of the equilibrium wall model smaller than that of their learned model in
the laminar boundary layer and in adverse-pressure-gradient
Poiseuille–Couette flows, through cancellation of its internal and
external errors (§4.2, §4.5, Figs. 8, 11). Delassaux et al.
(2023) find RANS drag within 0.002 of the measurement on a full-scale car
and attribute it to error cancellation, locating with a cumulative drag
along the body where RANS and DDES differ (front fairings and rear), while
the RANS wake topology is wrong ([Delassaux et al. (2023)](/sources/delassaux-2023.md), §6, Fig. 13;
HAL author manuscript). Morsbach et al. (2024) show that reducing the RANS
inflow length scale brings the turbine wake loss within 2.7% of the LES
while leaving an open separation that the LES does not have, "a lucky
cancellation of errors" ([Morsbach et al. (2024)](/sources/morsbach-2024.md),
§4.1, Figs. 8–9). Agreement in an integrated quantity does not, therefore,
validate the model form.

Both reviews conclude that predictions should carry explicit uncertainty
estimates, and Duraisamy et al. (2019) recommend that inference precede
learning, that information content and closure assumptions be assessed, and
that physical and mathematical constraints be enforced (§6, Eq. 13).
Duraisamy (2021) adds that the goal of more generalizable models "has,
however, not been achieved" and calls for community benchmarks (§VII).

## Qualifications

- Duraisamy et al. (2019) print the production as $P=\tau_{ij}\partial U_i/\partial x_j$
  (§4.1) while their Eq. 10 and the positive semi-definite random matrix
  make $\tau$ the kinematic $\langle u_i'u_j'\rangle$, for which the production is
  $-R_{ij}\partial_j\langle u_i\rangle$ (registry $P_k$). The sign swaps the
  names of the maximum- and minimum-production alignments but not the pair
  *(compiler check, not in the sources)*.
- The same review states that regularized least squares equals MAP "assuming
  that all distributions are Gaussian", with the scalar regularization
  weight equated to the matrix product $Q_dQ_\theta^{-1}$ (in this page's
  symbols), an unsquared regularization norm and no prior mean in the printed
  least-squares objective. *Compiler check, not in the sources:* equality
  holds for a squared norm, zero prior mean and isotropic covariances, with
  the scalar weight equal to the ratio of observation to prior variance.
- Duraisamy et al. (2019) credit "the scenario averaging (Edeling et al.
  2014b)", whereas their reference list gives the scenario-averaging paper
  the label 2014a.
- Yan et al. call $\sigma_{\mathrm{obs}}$ and $\sigma_\beta$ "variances" while
  they enter squared in the denominators, as standard deviations (Eqs. 6,
  14–15); their periodic-hill objective writes the weight as $\lambda_i$ under
  a sum over $j$ (Eq. 17).
- Cato et al. (2023) rank $\beta$ below $f_{\tilde\nu}$ for the converging–diverging
  channel in their summary (Table III) although their Table I gives the two
  nearly equal errors ($E_u$ $8.4\times10^{-3}$ against $8.1\times10^{-3}$,
  skin-friction error 0.18 against 0.19).
- **Terms differ between sources.** Duraisamy et al. (2019) file the
  limitations of the physical model under *epistemic and model-form*
  uncertainty and reserve *aleatory* for imprecise or naturally variable
  inputs (box "Uncertainty quantification", p. 5); Agrawal & Koutsourelakis
  (2024) call the model-form error of a closure *aleatoric*, because it
  remains random with infinite data, and keep *epistemic* for the parameter
  uncertainty that data remove (§1, §2.2). The two sources classify by
  different criteria, as their definitions print them: the origin of the
  error (inputs against physical model) for Duraisamy et al., reducibility
  by data for Agrawal & Koutsourelakis. The difference is one of
  terminology, not of fact, so it is recorded here rather than as a
  contradiction. This page keeps the review's usage in its title and lead.
- Agrawal & Koutsourelakis print the Reynolds stress with a minus sign,
  $-\langle u_i'u_j'\rangle$, and $k=-\tfrac12\mathrm{tr}$ of it (Eqs. 9–10),
  while their Eqs. 10, 14 and 17 write the positive isotropic part
  $\tfrac23kI$; the registry form above follows Eqs. 14 and 17. They call
  the marginal of their sparsity prior "a light-tailed, Student's
  t-distribution" (§2.2.2); a Student-t has polynomially decaying, i.e.
  heavy, tails *(compiler check, not in the sources)*. Their 10%
  Bernoulli selection of nodes is said to yield about 8% of the nodes
  (§3.2).
- Cato et al. rate the production multiplier $\beta$ in their middle class
  in all three flows (Table III), while Yan et al. use it as their only
  correction (above). The settings differ as the sources state them: Cato
  et al. invert dense velocity data with no regularization (§II B, Eq. 6),
  Yan et al. scarce data with a Gaussian prior (§2.1, Eq. 6).

# Citations

- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §2 Eqs. 1–6, boxes pp. 3, 5, 7, §3 Eqs. 7–9, §4.1 Eq. 10 Figs. 1–2, §4.2, §5.1–5.2, §5.4, §6 Eq. 13.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §I, §II Eq. 2, §III.A, §IV.A, §VII Fig. 4.
- [Yan et al. (2022)](/sources/yan-2022.md) — §1, §2.1 Eqs. 6, 14–17, §3.1.1 Figs. 4–5, §3.2.1 Table 2 Figs. 11, 14, 18, §3.3.1 Fig. 28.
- [Cato et al. (2023)](/sources/cato-2023.md) — §II B–D Eqs. 5–6, §III B Table I Eqs. 19–20 Fig. 6, §IV B Table II, §V B–C Figs. 16–17, §VI Table III, App. B Fig. 21 (HAL v2).
- [McConkey et al. (2022)](/sources/mcconkey-2022.md) — §II B, Figs. 1–4 (arXiv v1).
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §2.6, §4.1, §4.2, §4.5, §4.7–4.8 Table 1 Figs. 8, 11, 16, 18, §5, §6.
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — §6, Fig. 13 (HAL author manuscript).
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §4.1, Figs. 8–9.
- [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) — §1, §2.2–2.2.5 Eqs. 9–21, 32, §3.1–3.4 Figs. 7–12 Tables 3–5, App. B (arXiv v2).
