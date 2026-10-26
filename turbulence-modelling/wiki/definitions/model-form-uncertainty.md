---
type: Definition
title: "Model-form uncertainty in turbulence closures"
description: "The epistemic uncertainty that comes from the structure of a turbulence closure rather than from its inputs or coefficients; the four layers of RANS assumptions, physics-based bounds by eigenspace perturbation and random matrices, Bayesian calibration and discrepancy fields, where to place the correction, non-unique inversions and physics-based priors, and the limits of identifiability."
status: established
aliases: [model-form uncertainty, structural uncertainty, epistemic uncertainty, model discrepancy, RANS uncertainty quantification, eigenspace perturbation]
tags: [uncertainty-quantification, rans, data-driven, field-inversion]
timestamp: 2026-10-25T20:38:00Z
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
