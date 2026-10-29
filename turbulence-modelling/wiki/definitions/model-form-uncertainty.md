---
type: Definition
title: "Model-form uncertainty in turbulence closures"
description: "The uncertainty that comes from the structure of a turbulence closure rather than from its inputs or coefficients; the four layers of RANS assumptions, physics-based bounds, Bayesian calibration and discrepancy fields, where to place the correction, sparse data, generalizability levels, blended experts, stochastic discrepancies, identifiability and compensating errors."
status: established
aliases: [model-form uncertainty, structural uncertainty, epistemic uncertainty, aleatoric model uncertainty, model discrepancy, RANS uncertainty quantification, eigenspace perturbation, stochastic discrepancy closure]
tags: [uncertainty-quantification, rans, data-driven, field-inversion]
timestamp: 2026-10-29T10:03:00Z
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

Four further sources restate the layers. [He et al. (2022)](/sources/he-2022-b.md)
(§1–2.1) adopt L1–L4 after Duraisamy et al. (2019) and map the
data-driven literature onto them: tensor-basis, random-forest and
symbolic anisotropy corrections are L2, field inversion of a transport
equation is L3, Bayesian calibration of coefficients is L4. They correct
the eddy viscosity of the Spalart–Allmaras model with the quadratic
constitutive relation (L3), stating that an L3 modification is "better
conditioned and more robust" than an L2 one, citing Wu et al.
(2019). [Brenner et al. (2022)](/sources/brenner-2022.md) (§1) name three
levels of model-form error, averaging, the functional representation of
the Reynolds stress and the choice of functions within the model, and
state that for a linear eddy-viscosity model the first two are
inevitable and only the third, how $\nu_t$ is computed, can be improved;
they add that parametric calibration (ensemble Kalman, polynomial chaos,
approximate Bayesian computation) gives limited gains because no
universal optimal coefficients may exist. [Cherroud et al. (2022)](/sources/cherroud-2022.md)
(§1) list three sources of RANS uncertainty: the applicability of the
RANS equations, the model form, and the parameters.
[Shan et al. (2023)](/sources/shan-2023.md) (§IV) adopt the four layers
of Duraisamy et al. (2019) and state that their data-driven
Spalart–Allmaras replacement reduces only the L4 (coefficient) layer,
leaving averaging, the linear stress representation and the functional
forms untouched. Their calibrations show the case dependence of L4
directly: the nine SA coefficients fitted to measured pressure at four
airfoil conditions spread from 3.550 to 7.295 in $c_{v1}$ and from 0.396
to 0.615 in $\kappa$, and a set fitted at one incidence degrades the rest
of the lift curve (Table B1, §III.C; see
[ensemble Kalman calibration](/methods/ensemble-kalman-closure-calibration.md)).
Duraisamy et al. (§4.2) state that optimal coefficients are
flow-specific, and Brenner et al. doubt that universal optimal
coefficients exist.

## Bounding from physical constraints

**Formal bounds.** The background-flow method (Howard; Busse;
Doering–Constantin; Seis, cited by Duraisamy et al. 2019, §4.1) bounds
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
which Duraisamy (2021, §I, §III.A) cites as the start of the
machine-learning strand.

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

Applications cited in §5.1 address L4 only: posterior distributions of
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
  observed, than inverting on lift alone (§3.3.1, Fig. 28). Yan et al. (§1) also
  cite Rumsey's finding that enhanced mixing in separated shear layers
  helps the periodic hill but worsens backward-facing-step flows, as an
  example of ad hoc corrections that do not generalize.

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
ill-conditioned, in agreement, the authors state, with Dow & Wang: its
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

**Corrections in a compressible, high-order setting.** Fanizza et al.
(2025) repeat the comparison of correction sites for the compressible SA
model on a high-order modal discontinuous Galerkin discretization, with a
momentum and energy source, an eddy-viscosity multiplier, a source
proportional to $\tilde\nu$ and a production multiplier written as
$(1+\beta)$ like Cato et al.'s ([Fanizza et al. (2025)](/sources/fanizza-2025.md),
§3.3). On the square cylinder at $Re=22\,000$ the source corrects the
velocity best, followed by the $\tilde\nu$-source and the production
multiplier, and the eddy-viscosity multiplier stalls on a plateau "from the
very first iterations", in agreement with Cato et al. (§4.2, Figs. 7–8). On
a supersonic shock/boundary-layer interaction only the source improves
velocity, $C_p$ and $C_f$ together (§4.3.1, Table 1; numbers on the
[Boussinesq page](/definitions/boussinesq-hypothesis.md)). Two of their
findings bear on the data side of the problem:

- **Sparse data.** With wall pressure as the only data, the source lowers
  the $C_p$ error by three orders of magnitude, but $C_f$ stays wrong
  (normalized error 0.854), and the three corrections acting through the
  eddy viscosity make $C_f$ worse than the baseline over the whole wall
  (1.56–1.70; §4.3.3, Table 2). An $L^2$ penalty on the correction
  improves the skin-friction error, "particularly when the penalty is
  sufficiently strong to outweigh the objective function", but the
  near-wall velocity and $C_f$ "did not significantly improve"; the authors
  conclude that sparse data need "advanced regularization" built on prior
  knowledge of flow physics or turbulence modelling (§4.3.4, Tables 3–4,
  §5).
- **Discretization error in the inferred correction.** They argue, without
  an FV–DG comparison, that corrections inferred on diffusive second-order
  finite-volume discretizations contain a strong discretization component
  and may not extrapolate to other meshes or codes, so that high-order
  discretizations will be "mandatory" if corrections are to compensate
  modelling errors only (§1). On a laminar cylinder at $Re=80$ the lowest
  cost minimum is reached at $N=2$, the lowest polynomial degree at which
  the baseline shows no grid dependence, and they recommend that degree for
  data assimilation (§4.1, Fig. 6; the source writes the degree $p$). See
  [discretization-consistent closures](/definitions/discretization-consistent-closure.md).

They propose the inferred correction fields as detectors of where a RANS
model fails (§5).

**A multiplier of a frozen eddy viscosity.** Brenner et al. (2022, §2.1,
Eq. 7) correct only the third level of their classification: the
effective viscosity of the momentum equation becomes $\nu+\beta\nu_t$,
with $\nu_t$ frozen from a converged
[$k$-$\varepsilon$](/methods/k-epsilon-model.md) solution and $\beta$
(the registry's field-inversion multiplier, the source's $\alpha$; one
value per cell) inferred by a discrete adjoint from
sparse LES velocity on the [periodic hill](/benchmarks/periodic-hill.md)
at $Re_h=10\,595$ (details on the
[field-inversion page](/methods/field-inversion-machine-learning.md)).
Their evidence of non-uniqueness: with a prescribed smooth $\beta$
generating synthetic data, the inversion recovers the velocity "very
well" but not the field, the recovered $\beta$ spanning
$[0.21,1.95]$ (§3.2, Figs. 6–7), so quantitative comparison of inferred
fields across data sets "is not meaningful" (§3.5). Interior velocity
data alone do not improve the wall shear stress; wall data alone improve
$C_f$ but worsen the interior; combining both shows a trade-off that the
authors call a possible Pareto front, and they cannot say whether the
residual errors come from the eddy-viscosity assumption or from the
assimilation and its regularization (§3.6, Fig. 16). Results
"considerably depend on the locations of the reference values and the
values of the hyperparameters" (§4).

**A discrepancy at the wall of a wall-modelled LES.**
[Zangeneh (2021)](/sources/zangeneh-2021.md) places the learned
discrepancy not in the closure equations but in the wall boundary
condition: a random forest maps local mean-flow features of an
IDDES-based [wall-modelled LES](/methods/wall-modelled-les.md) to the
discrepancies $\boldsymbol\delta$ of the wall shear stress and wall heat
flux against experiment or DNS, and the corrected wall values (baseline
plus predicted discrepancy) are used to correct the eddy viscosity and
turbulent Prandtl number fed back to the solver (§II.F, §III, Fig. 3;
the procedure for the corrected $\mu_t$ and $Pr_t$ is not printed). The
author calls this "a corrective approach and not 'standard' turbulence
model" (§III). The discrepancy is trained on the same geometry at a
lower Reynolds number; a model trained on both training flows corrects
less than the single-flow one, and the author concludes that the
training set "is far from being representative" of the flow physics
(§III.C, §IV). Details are on
[machine-learning wall models](/methods/machine-learning-wall-model.md);
the paper cites discrepancy-modelling work on Reynolds stresses (Xiao et
al. 2016; Wang et al. 2017) only as background (§I).

A $k$-$\varepsilon$ inversion makes the opposite choice to correcting
production. [Diez Sanhueza et al. (2023)](/sources/sanhueza-2023.md)
(§3.1, Eqs. 9–16) multiply the **dissipation** terms of both equations of
a low-Reynolds-number $k$-$\varepsilon$ model, $P_k-\beta_kD_k+T_k=0$ and
$P_\varepsilon-\beta_\varepsilon D_\varepsilon+T_\varepsilon=0$
(page-local $D$ for the destruction and $T$ for the diffusion terms,
$\beta_k$, $\beta_\varepsilon$ two fields of the registry's
$\beta(\boldsymbol x)$), "contrary to Parish and Duraisamy", as cited.
Their reasons: production appears with opposite sign in the mean kinetic
energy equation, so the choice "adhere[s] to energy conservation", and it
is active in a smaller part of the boundary layer. The cost regularizes
the additive discrepancy $\delta_k=D_k(\beta_k-1)$, $\delta_\varepsilon=D_\varepsilon(\beta_\varepsilon-1)$
normalized by the largest budget term of its equation, which the authors
describe as a fourth budget term free to follow patterns the baseline
terms do not have (§3.3). Different weightings, and inversions with only
$\delta_k$ or only $\delta_\varepsilon$, give corrections of the same
shape with different peak magnitudes (§4, Fig. 6); the normalized
$\delta_\varepsilon$ carries gradients up to 83.5% higher than the maximum
gradients of the normalized $\delta_k$, so only $\delta_k$ is learned (§4). Introducing $\beta_k$ can unbalance production and
dissipation in the log layer, which is why results with $\beta_\varepsilon$
alone are also given (§3.1). Details are on the
[field-inversion page](/methods/field-inversion-machine-learning.md).

## Generalizability and the attached boundary layer

Wu et al. (2025) grade the generalizability of field-inversion corrections
on four levels (Table 1): **L1**, good performance on geometries similar to
the training ones; **L2**, no degradation of the baseline in simple attached
flows such as the zero-pressure-gradient flat plate; **L3**, good
performance on flows with similar separation features but different
geometry and Reynolds number; **L4**, good performance across different
separation features ([Wu et al. (2025)](/sources/wu-2025.md), §1, Table 1;
authors' manuscript). Most published inversions, they state, test L1
only. They cite Spalart for the proposal that L2 be a hard constraint on
data-driven models, and Rumsey et al. for a model trained on an
adverse-pressure-gradient plate that fails on the zero-pressure-gradient
one (§1).

The L2 failure has an algebraic cause in the
[$k$-$\omega$ SST model](/methods/k-omega-sst-model.md): its log-layer
solution requires $\beta_\omega-\beta^*\gamma_\omega=\kappa^2\sqrt{\beta^*}\sigma_\omega$
(registry-§11 $\beta_\omega$, $\gamma_\omega$: the SST $\omega$-destruction and
$\omega$-production coefficients, $\beta$ and $\alpha$ on the SST page), and a
multiplier $\beta(\boldsymbol x)$ of the $\omega$-destruction turns the left
side into $\beta(\boldsymbol x)\beta_\omega-\beta^*\gamma_\omega$, so the calibration holds
only where $\beta(\boldsymbol x)=1$ (§2.1, Eqs. 3–4; the source writes the SST
destruction coefficient $\theta$ and the production coefficient $\gamma$).
Their remedy, *conditioned* field inversion, gates the multiplier with the
DDES shielding function $f_d$ during both inversion and prediction, so that
the correction vanishes in the attached boundary layer (details on the
[field-inversion page](/methods/field-inversion-machine-learning.md)). The
two learned models differ exactly there: on the zero-pressure-gradient
plate the classically trained one has $\beta(\boldsymbol x)\approx1.06$ in
the boundary layer, overpredicts $C_f$ and distorts the log layer, while
the conditioned one keeps $\beta(\boldsymbol x)=1$ and reproduces SST and the
Wieghardt–Tillmann data; on the NACA 0012 at $0^\circ$ the conditioned model
matches SST and the classic one overpredicts $C_f$ (§4.5, Figs. 47–50). On
the separated test flows the two reach comparable L3 accuracy (§4.1–4.4).
The construction rests on an assumption the authors state: "the baseline
model accurately calculates the attached boundary layer and requires no
modification in this region" (§1).

Diez Sanhueza et al. (2023, §5, Table 3, Fig. 9) report the K-fold
spread of a learned $k$-$\varepsilon$ correction for variable-property
channels: the error falls in almost every held-out case, and for the
hardest case, held out in six trials, the maximum–minimum envelope of the
six predictions, which the authors call an "uncertainty quantification
process", shows every prediction more accurate than the baseline (L∞
velocity errors 4.0–10.2% against 23.4%). The one large
degradation, 2.3% to 14.0% on an incompressible channel at
$Re_\tau=4200$, they attribute to extrapolation: the nearest training
case is at $Re_\tau=2000$ (§5).

## Blending specialized corrections

Corrections trained on one flow class "do not generalize to radically
different flows, and often deteriorate the representation of canonical
flows" (Oulghelou et al. 2025, §1). Their two symbolic SST corrections show
it on a channel at $Re_\tau=1000$: the mean absolute error of $u^+$ is 0.44
for SST, 2.41 for the separated-flow correction and 8.97 for the jet
correction ([Oulghelou et al. (2025)](/sources/oulghelou-2025.md), §4.2.1,
Table 3; arXiv v2). The authors' earlier external aggregation mixes the
*solutions* of several such models with space-dependent weights read as
local model probabilities, after Bayesian model averaging, and uses the
spread between the component solutions as an estimate of model-form
uncertainty; it costs one simulation per model and the mixed field is "in
general not a solution of the governing equations" (§1, Fig. 1). Blending
the corrections *inside* one RANS solve fixes both but "does not deliver
estimates of the predictive uncertainty as naturally", so it is "no
longer an uncertainty quantification method" (§1, §3). See
[turbulence-model aggregation](/methods/turbulence-model-aggregation.md).
Sandberg & Zhao (2022, §5) state, from their review of learned stress
and heat-flux closures, that universal models are unlikely and that
classes of models for flow topologies, blended by machine-learning
classifiers, are the more plausible future
([Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md)).

## Posterior coefficient distributions from sparse Bayesian regression

Cherroud et al. (2022) attach the uncertainty to the coefficients of a
learned [explicit algebraic correction](/methods/explicit-algebraic-reynolds-stress-model.md)
of [$k$-$\omega$ SST](/methods/k-omega-sst-model.md): sparse Bayesian
learning with an automatic-relevance-determination Gaussian prior on each
weight and a Laplace-type hyperprior on its precision (one sparsity
parameter for all) gives a Gaussian posterior for the surviving
coefficients (§3, Eqs. 16–27; method on
[symbolic-regression closures](/methods/symbolic-regression-closure.md)).
The selected models have a single stochastic coefficient, e.g.
$0.8433\pm0.0142$ for the production correction of their first scenario
(App. A, Eq. A.13), and are propagated by non-intrusive probabilistic
collocation with second-order Hermite polynomial chaos, three CFD runs per
model (§4.2). Findings:

- the $\pm3\sigma$ bands widen where the prediction departs from the LES
  or DNS, which the authors read as a warning about reliability (Figs.
  5–7, §5);
- the bands of one model are too narrow to cover the reference everywhere
  (§4.2, Fig. 5);
- the solution posterior is "likely asymmetric" although the parameter
  posterior is symmetric, because of the non-linearity of the
  Navier–Stokes equations, yet the bands are drawn symmetric (§4.2);
- Sobol indices from the same expansion, for a richer four-parameter
  model, show the near-wall stress sensitive mainly to the production
  correction and the recirculation region to the anisotropy correction,
  dominated by its linear term, with interactions beyond second order
  negligible (§4.3, Fig. 8). The authors conclude that linear
  eddy-viscosity models are "overall sufficient" for these 2-D separated
  flows "provided that the eddy viscosity coefficient is properly tuned"
  (§4.3).

Propagating only the maximum-a-posteriori coefficients costs one run (§5).

## Explaining a learned correction

He et al. (2022) ask what a learned correction has captured. Their random
forest maps nine bounded local features (pressure gradient, strain against
rotation, flow misalignment, the SA wall function $f_w$ as a wall-region
classifier, the viscosity ratio $\nu_t/\nu$) to the eddy-viscosity
discrepancy $\Delta\nu_t$ of SA-QCR on the transonic Bachalo–Johnson bump,
trained on the wall-resolved LES of Uzun & Malik at $M_\infty=0.875$
(§2.2–2.7, Table 2; see
[shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).
Two kinds of explanation are applied:

- **Intrinsic** (reduce complexity): a grid search over the number of
  trees $T$ and the feature fraction gives a Pareto front of five-fold
  cross-validated $R^2$ against complexity; $T=20$ with 5 of 9 features
  per split reaches $R^2=0.90682$ against $0.91011$ for the best set
  ($T=130$, 6 of 9) at about one-eighth of the complexity (§4.1, Fig. 9).
  Feature selection drops redundant pressure-gradient and strain–rotation
  features, keeping six (§4.2).
- **Post hoc** (Shapley additive explanations, SHAP): the prediction is
  decomposed additively into one contribution per feature, and
  pairwise interaction values separate pure effects from interactions
  (§3.2, Eqs. 13–18). The global ranking is viscosity ratio ≫ normalized
  Q-criterion > wall function > ratio of pressure normal stress to
  "normal shear stress" > streamwise pressure gradient > misalignment
  (§5.1, Fig. 13).

The authors read the monotone SHAP trends as the forest re-discovering
known physics, the scaling of the SA source terms with $\nu_t$ and the
shear-enhances/rotation-reduces effect, and as suggesting a new one, more
eddy viscosity where the pressure normal stress dominates, which "needs
verification" (abstract, §5.3). From the trend of the wall-function
feature they infer that the equilibrium assumption of SA "fails" on the
bump (§5.1). They state the limits of the method themselves: SHAP is
data-dependent, describes how and not why the model responds, and cannot
find physics outside the chosen features (§5.3). They attribute the
discrepancy at the shock foot to shock buffet, "conceptually impossible
to be modeled by steady RANS" (§2.7); the paper argues this attribution
but does not test it. All results are offline, on frozen mean fields: the
corrected model is not run in the solver (§2.2; see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

## Modelling error against discretization error

[Fidkowski (2022)](/sources/fidkowski-2022.md) shows the two errors
separating under mesh adaptation. On a NACA 0012 at $Re=2\times10^4$
(transitional, with a separation bubble) and on a high-lift airfoil at
$Re=10^6$, output-based adaptation of the uncorrected SA RANS converges to
a wrong mean lift with "imperceptibly small" discretization-error
estimates: the residual error is modelling error, invisible to a
discretization-error estimator (§6.2–6.3, Figs. 12, 18). The author notes
that the cases lie outside the usual applicability of RANS, so the result
is not representative of attached high-Reynolds-number flows (§7). Adapting
instead with a field-inversion-corrected RANS used as a single-use
surrogate of the time-averaged unsteady solution recovers the right lift
(see [mesh adaptation](/methods/mesh-adaptation.md)).

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
$\varepsilon$ from the [$k$-$\varepsilon$](/methods/k-epsilon-model.md)
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
§4.1, Figs. 8–9).

**Agreement between models as an argument against model-form error.**
Baldan & Guardone (2025) argue the converse case: a wall-resolved LES,
a two-dimensional URANS and a stress-blended eddy simulation of a NACA 0012
in deep dynamic stall agree with one another (within 0.1 in $C_L$ in
attached flow, peak lift at $22^\circ$ in all three) but share an offset
of 0.2 in $C_L$ and a $2^\circ$ shift of peak lift from the experiment, so
the authors attribute the discrepancy to wind-tunnel effects or surface
roughness rather than to the turbulence model, against the many URANS and
hybrid studies they cite that blame the model
([Baldan & Guardone (2025)](/sources/baldan-2025.md), Introduction, §2.2,
Fig. 9, §3; arXiv v2). The paper does not test this attribution: one
pitching cycle is computed, without phase averaging or cycle-to-cycle
variation (§2.2). See
[hybrid RANS/LES](/definitions/hybrid-rans-les.md).

Both reviews conclude that predictions should carry explicit uncertainty
estimates, and Duraisamy et al. (2019) recommend that inference precede
learning, that information content and closure assumptions be assessed, and
that physical and mathematical constraints be enforced (§6, Eq. 13).
Duraisamy (2021) adds that the goal of more generalizable models "has,
however, not been achieved" and calls for community benchmarks (§VII).

## Uncertainty of learned models: a statistical taxonomy (Ihme et al. 2022)

[Ihme et al. (2022)](/sources/ihme-2022.md), reviewing machine learning
in combustion, give the uncertainty vocabulary of statistical learning
(§2.5–2.7, §5.3–5.4, Fig. 9):

- **Epistemic and aleatoric.** Epistemic uncertainty, from lack of
  knowledge, is subdivided into *parameter* and *structural* uncertainty
  and identified with systematic uncertainty; aleatoric uncertainty,
  irreducible, is *homoscedastic* or *heteroscedastic* and identified with
  statistical uncertainty (§2.6).
- **Bias and variance.** The expected generalization error splits into
  noise, bias and variance (Eq. 34), illustrated by polynomial fits of
  laminar flame speeds that underfit at first order and overfit at fifth
  (§2.5, Fig. 7).
- **Dataset shift.** A model meets out-of-distribution inputs through
  covariate shift, label (prior-probability) shift, concept drift or
  open-set recognition; the authors stress the common case of a model
  trained on simulation data and deployed on real systems (§2.7). They
  name the Wasserstein metric and the Mahalanobis distance as gauges of
  whether a trained model applies to new samples (§5.4); see the
  training-set distance of Lozano-Durán & Bae (2023) above.
- **Quantification tools.** Gaussian-process regression, Bayesian neural
  networks and quantile-regression networks (§5.3). Gaussian-process
  inference cost grows cubically with the number of observations;
  Bayesian-network uncertainty estimates depend strongly on the inference
  algorithm and their training can take orders of magnitude longer than
  that of deterministic networks. In the authors' assessment Gaussian
  processes currently give accurate means, reliable uncertainty estimates
  and robustness to out-of-distribution instances (§5.3).
- **Uncertainty classifiers as model selectors.** A random-forest
  assignment of combustion submodels of different fidelity in LES, which
  the authors cite as inspired by the RANS-uncertainty classifier of Ling
  and Templeton, cut cost by 20%, with errors "limited by the predictive
  capability of the lowest-performing submodel" (§4.1.4, Fig. 34).

The review states these as background; its only computed examples are
its tutorials.

## The industrial view of model-form error (Mani & Dorgan 2023)

[Mani & Dorgan (2023)](/sources/mani-2023.md), an industrial
perspective, place the uncertainty of turbulence closures inside
verification and validation. Numerically, the credibility of a
prediction is assessed by varying the turbulence model, the mesh, the
algorithm, "or even the uncertainty in closure coefficients" (they cite
Schaefer et al. 2017 for the SA coefficients), and today the uncertainty
of the wind-tunnel data is weighed as well (§4.1). They state that the
industrial RANS workhorses (SA with its rotation-curvature and
quadratic-constitutive-relation variants, SST, Smith's $k$-$l$) "can be
inadequate" for large separation, that many other modifications have
been studied but "rarely have they provided general improvements", and name the
macroscopic forcing method of Mani & Park as a direction that "avoids
model-form inaccuracies" by not resting on the Boussinesq approximation,
isotropy or scale separation and by avoiding tuning constants; it is not
ready for industrial use (§4.5.1). Uncertainty-quantification
practice is one of their requirements for certification by analysis
(§5). The review gives no equations or new data.

## Model error inside a coefficient calibration (An et al. 2025)

[An et al. (2025)](/sources/an-2025.md) calibrate seven
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) constants by
Bayesian inference with the embedded model-error formulation of Sargsyan
et al. (as cited): the discrepancy enters as random perturbations of the
coefficients rather than as an additive output term (§2.3.2, Eqs. 23–26;
method on [Bayesian calibration](/methods/bayesian-closure-calibration.md)).
The posterior predictive variance then splits into a model-error part (the
mean of the posterior variances), a posterior-uncertainty part (the
variance of the posterior means) and a surrogate-error part (Eqs. 29–30).
On the backward-facing step the model error is "considerable across all
positions, especially in the separation region", the posterior uncertainty
concentrates near separation, and the surrogate error is the smallest of
the three (§3.1, Fig. 12). The calibration changes the coefficients only
(layer L4 above). The validation gains of the final set (26.44% on the
bump crest transition region, about 25% in $C_f$ on the rounded step)
are in attached pressure-gradient regions, with "limited improvement" in
the bump separation and "limited improvements" on the hump (§4).

**Discretization in the calibrated coefficients.** The same calibration
run with a second-order finite-volume solver and a third-order
discontinuous Galerkin solver gives different MAP coefficients and
different sensitivities: on the step the MAP von Kármán constant is 0.61
under finite volume and 0.24 under DG, and the Sobol index of $c_{v1}$ is
"approximately 120% higher" under DG (§3.1, §3.3, Table 3, Fig. 9). The
authors hypothesize that the lower dissipation of the high-order scheme
exposes the model error in the separated shear layer (§3.1). For
inferred correction fields, Fanizza et al. (2025, §1) argue that fields
inferred on diffusive second-order discretizations contain a
discretization component (above); they run no finite-volume–DG
comparison, while An et al. compare the two discretizations on the
coefficients.

## Model-form uncertainty in four further reviews

- **Nominal coefficients (Le et al. 2024).** [Le et al. (2024)](/sources/le-2024.md)
  (§3.1, §3.1.1, pp. 10–11) sort machine-learning uses in RANS into
  uncertainty analysis, model improvement and model replacement, and state
  that "There is currently no evidence suggesting that nominal values
  perform well across all types of flows". They report that a Bayesian
  recalibration of
  [SST](/methods/k-omega-sst-model.md) in compression-corner
  [shock/boundary-layer interactions](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
  improves the adverse-gradient prediction but "cannot simulate the
  inherent shock instability", and the separation-region wall pressure
  "remains too high" (Tang et al., as cited; Fig. 8). They also cite Ling
  & Templeton's classification of regions of high RANS uncertainty
  (§3.1.2), the classifier that Ihme et al. (2022) cite above, and report
  that physics-informed corrections of Reynolds-stress discrepancies can
  "degrade the computational results of the original RANS model" in
  regions with geometric changes, even for similar separated flows
  (§3.1.2, p. 12).
- **Uncertainty of learned models (Fang et al. 2026).**
  [Fang et al. (2026)](/sources/fang-2026.md) (§4.2.4) separate aleatoric
  uncertainty, from noise or variability in the data, from epistemic
  uncertainty, from the model structure or insufficient data (the
  definitions of Duraisamy et al. (2019) and Agrawal & Koutsourelakis
  (2024) are under Qualifications). Among the methods they cite, deep ensembles, Monte
  Carlo dropout, Bayesian neural networks and stochastic variational
  inference, deep ensembles had the highest predictive accuracy but were
  "prone to overconfidence in out-of-distribution regimes", while
  stochastic variational inference was "more conservative" (Grogan et al.,
  as cited); Bayesian neural networks capture aleatoric and epistemic
  uncertainty of reacting-flow closures a priori, and Mondrian forests are a non-parametric
  alternative (§4.2.4). The review quotes these results without numbers of
  its own.
- **Disagreement of established models (Luckring & Rizzi 2024).**
  [Luckring & Rizzi (2024)](/sources/luckring-2024.md) reproduce the
  formulation hierarchy of Xiao & Cinnella and cite Wilcox for the statement
  that no model gives accurate results in all flows without ad hoc
  adjustment of its constants (§2.4.1). Their survey of concentrated
  vortex flows records disagreement between
  "well-established codes using well-established turbulence models": on
  the SACCON configuration RANS solutions give significantly different
  vortex fields where the pitch stability changes rapidly, and on the X-31
  two codes with SA and with a $k$-$\omega$ model give significantly
  different wing vortex flows (§3.2.3.2, §3.2.3.4, Figs. 84–88, 93–94; see
  [delta-wing vortex flows](/benchmarks/delta-wing-vortex-flow.md)). They
  define calibration, after the ASME guide, as adjusting physical
  modelling parameters "to improve agreement with experimental data", and
  call a formulation *anchored* when it has "some degree of pedigree
  (historical applications, calibration history, validation history)" for
  a new prediction (§2.1).
- **Uncertainty as the motive and the Bayesian family (Hu & Yang 2026).**
  [Hu & Yang (2026)](/sources/hu-2026.md) (§I) open their review of
  machine-learning closures by stating that model-form and parametric
  uncertainties "remain a major obstacle" to the predictive capability of
  RANS models. They list a Bayesian philosophy of machine-learning RANS
  (§III C, Table I), whose stated strength is quantified predictive
  uncertainty, "crucial for engineering decision-making". As they cite
  them, the members are: physics-informed Bayesian inference of
  Reynolds-stress discrepancies that respects realizability, such as
  positive semi-definiteness (Xiao et al.); a Bayesian deep network
  trained by Stein variational gradient descent, whose weight
  distribution gives uncertainty bounds on the predicted fields (Geneva &
  Zabaras); Bayesian model-scenario averaging, weighting each closure by
  its posterior probability, and MAP-based predictions (Edeling et al.);
  space-dependent aggregation of stochastic SBL-SpaRTA experts with a
  mixture of experts (Cherroud et al., 2025); and the blending of
  [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) (see the
  section on blending specialized corrections above and [turbulence-model aggregation](/methods/turbulence-model-aggregation.md)).
  Their qualitative Table II ("a reader's guide rather than a rigorous
  benchmark") gives the family about 5–20 training cases with priors,
  "Medium" inference cost, "High" a posteriori robustness and
  "Medium–high" interpretability. They note (§VI A) that the Fourier
  neural operator and DeepONet are deterministic point predictors without
  native uncertainty quantification. Diffusion-based generative models
  could provide uncertainty estimates for closures, but they call this "a
  potential rather than a demonstrated capability" (§VI D). From Mandler
  & Weigand (2025), as cited (§I, §VII A), they take the finding that a
  systematic mismatch between training inputs and target responses, not
  extrapolation, dominates the generalization error of data-driven
  eddy-viscosity models.

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
  by data for Agrawal & Koutsourelakis. This page keeps the review's usage in its title and lead.
  Fang et al. (2026, §4.2.4) define aleatoric uncertainty as arising from
  noise or variability in the data and epistemic uncertainty as arising
  from the model structure or insufficient data.
- **Parametric gains against model form.** Brenner et al. (2022, §1)
  class coefficient calibration as parametric calibration with limited
  gains, because no universal optimal coefficients may exist; they give
  no test of their own. An et al. (2025, §4) report, for their
  Bayesian-calibrated SA set, a 26.44% error reduction in the crest
  transition region of the Gaussian bump and about 25% overall $C_f$
  error reduction on the rounded step (attached pressure-gradient
  regions), and "limited improvement" in the bump separation and
  "limited improvements" on the hump; their variance decomposition puts
  the largest model error in the separation region (§3.1, Fig. 12).
- Agrawal & Koutsourelakis print the Reynolds stress with a minus sign,
  $-\langle u_i'u_j'\rangle$, and $k=-\tfrac12\mathrm{tr}$ of it (Eqs. 9–10),
  while their Eqs. 10, 14 and 17 write the positive isotropic part
  $\tfrac23kI$; the registry form above follows Eqs. 14 and 17. Their 10%
  Bernoulli selection of nodes is said to yield about 8% of the nodes
  (§3.2).
- Cato et al. rate the production multiplier $\beta$ in their middle class
  in all three flows (Table III), while Yan et al. use it as their only
  correction (above). The settings differ as the sources state them: Cato
  et al. invert dense velocity data with no regularization (§II B, Eq. 6),
  Yan et al. scarce data with a Gaussian prior (§2.1, Eq. 6).
- Wu et al. (2025) build their conditioned inversion on the assumption that
  the attached boundary layer needs no correction (§1) and attribute
  separation errors mainly to the separated shear layer, citing earlier
  work (§2.1). Yan et al.'s inversion on the lift of the S809 airfoil near
  stall acts "mainly in the strong adverse-pressure-gradient region near
  the boundary layer" ([Yan et al. (2022)](/sources/yan-2022.md), §3.1.1,
  Fig. 6). The two statements concern different flows (smooth-surface
  separation onset on an airfoil against the curved step and hump on which
  Wu et al. train), and Yan et al. show that their inversions are not unique
  (above); Wu et al. list smooth-surface
  separation among their L3 examples (Table 1) but train on the hump and the
  curved step only.
- Fanizza et al. (2025) print slips around their regularization study:
  §4.3.4 says the penalty degrades the velocity and wall-pressure errors,
  while their Table 3 against Table 2 shows the velocity error improving
  for three of the four corrections (e.g. 0.458 to 0.406 and 0.433 for the
  eddy-viscosity multiplier) and the pressure error improving for that
  multiplier at the smaller penalty (0.17357 to 0.1576); Tables 3 and 4
  print different penalty weights for the $\tilde\nu$-source and the
  production multiplier; and §4.3.1 says the errors of the three
  Boussinesq-type corrections are "reduced by less than one order of
  magnitude", while Table 1 gives the production multiplier a $C_f$ error
  of 1.145, above the baseline.
- He et al. (2022) print the strain in their Boussinesq relation as
  "$S^*_{ij}=S_{ij}-\mathrm{tr}(S_{ij})$ the traceless strain rate tensor"
  (§2.1, Eq. 2); their own least-squares eddy viscosity (Eq. 6), with
  $\tfrac13$ factors on the trace terms, follows from the traceless
  $S_{ij}-\tfrac13S_{kk}\delta_{ij}$ *(compiler check, not in the
  sources)*. In §5.2 they write that $q_3$ "increases the eddy viscosity
  ($\phi_{3,3}<0$)", where their §5.1 trend gives a positive contribution
  for large $q_3$; the page follows §5.1. Their conclusion prints "87.5%" lower
  complexity; §4.1 calls the ratio "about 1/8" and prints $11.11$ against
  $86.67$, 87.2% lower *(compiler check, not in the sources)*.
- Cherroud et al. (2022) print the evidence of their sparse Bayesian
  regression (Eq. 26) without the inverse of the covariance matrix in the
  quadratic term and with the prior sum from $i=0$; the Gaussian marginal
  likelihood built from their Eqs. 17 and 19 needs
  $\mathbf t^\top(\sigma^2\mathbf I+\mathbf C\mathbf A^{-1}\mathbf C^\top)^{-1}\mathbf t$
  (page-local symbols of the source) *(compiler check, not in the
  sources)*. The symbol $\gamma_i$ in their update (Eq. 27) is not defined
  in the paper.

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
- [Fanizza et al. (2025)](/sources/fanizza-2025.md) — §1, §3.3, §4.1 Fig. 6, §4.2 Figs. 7–8, §4.3.1 Table 1, §4.3.3–4.3.4 Tables 2–4, §5.
- [Wu et al. (2025)](/sources/wu-2025.md) — §1 Table 1, §2.1 Eqs. 3–4, §4.1–4.5 Figs. 47–50 (authors' manuscript).
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — §1 Fig. 1, §3, §4.2.1 Table 3 (arXiv v2).
- [Zangeneh (2021)](/sources/zangeneh-2021.md) — §I (discrepancy modelling cited), §II.F, §III, Fig. 3 (wall-stress and heat-flux discrepancy, feedback), §III.C, §IV (generalization).
- [Baldan & Guardone (2025)](/sources/baldan-2025.md) — Introduction, §2.2 Fig. 9, §3 (arXiv v2).
- [He et al. (2022)](/sources/he-2022-b.md) — §1–2.1 (L1–L4 mapping, L3 against L2), §2.2–2.7 Table 2 (framework, features, offline only), §3.2 Eqs. 13–18 (SHAP), §4.1–4.2 Fig. 9 (Pareto front, feature selection), §5.1–5.3 Fig. 13.
- [Brenner et al. (2022)](/sources/brenner-2022.md) — §1 (three levels, parametric calibration), §2.1 Eq. 7, §3.2 Figs. 6–7 (synthetic non-uniqueness), §3.5, §3.6 Fig. 16, §4.
- [Cherroud et al. (2022)](/sources/cherroud-2022.md) — §1, §3 Eqs. 16–27, §4.2 Figs. 5–7, §4.3 Fig. 8, §5, App. A Eq. A.13.
- [Fidkowski (2022)](/sources/fidkowski-2022.md) — §6.2–6.3 Figs. 12, 18 (RANS adaptation converges to a wrong lift), §7.
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §5 (classes of models blended by classifiers).
- [Shan et al. (2023)](/sources/shan-2023.md) — §IV (four layers; only coefficients reduced); §III.C, Table B1 (case-dependent calibrated SA coefficients).
- [Ihme et al. (2022)](/sources/ihme-2022.md) — §2.5–2.7, Eq. 34, Figs. 7, 9 (bias–variance, epistemic and aleatoric uncertainty, dataset shift); §4.1.4, Fig. 34 (classifier-based submodel assignment); §5.3–5.4 (Gaussian processes, Bayesian networks, out-of-distribution gauges).
- [Mani & Dorgan (2023)](/sources/mani-2023.md) — §4.1 (uncertainty in V&V, closure-coefficient UQ cited); §4.5.1 (RANS workhorses, macroscopic forcing method); §5 (UQ for certification by analysis).
- [An et al. (2025)](/sources/an-2025.md) — §2.3.2, Eqs. 23–30 (embedded model error, variance decomposition); §3.1, §3.3, Table 3, Figs. 9, 12 (model error in separation, discretization-dependent MAP sets and sensitivities); §4 (validation gains).
- [Le et al. (2024)](/sources/le-2024.md) — §3.1, §3.1.1, Fig. 8 (three ML uses, nominal coefficients, limit of SST calibration in SWBLI); §3.1.2, p. 12 (uncertainty classification, degradation by discrepancy corrections).
- [Fang et al. (2026)](/sources/fang-2026.md) — §4.2.4 (aleatoric and epistemic uncertainty, deep ensembles, MC dropout, Bayesian networks, SVI, Mondrian forests).
- [Luckring & Rizzi (2024)](/sources/luckring-2024.md) — §2.1 (calibration, anchored formulation), §2.4.1 (formulation hierarchy, Wilcox cited), §3.2.3.2, §3.2.3.4, Figs. 84–88, 93–94 (SACCON and X-31 model disagreement).
- [Diez Sanhueza et al. (2023)](/sources/sanhueza-2023.md) — §3.1, Eqs. 9–16 (multipliers on the dissipation terms, additive discrepancy in the cost); §3.3; §4, Fig. 6 (similar shapes); §5, Table 3, Fig. 9 (K-fold spread, extrapolation in $Re_\tau$).
- [Hu & Yang (2026)](/sources/hu-2026.md) — review: §I (uncertainties as obstacle); §III C, Tables I–II (Bayesian family as cited, ratings); §VI A, §VI D (no native UQ in neural operators; generative models as potential); §VII A (Mandler & Weigand, as cited).
