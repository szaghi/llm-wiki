---
type: Method
title: "Bayesian calibration of turbulence-model coefficients"
description: "Calibration of RANS closure coefficients as Bayesian inference: priors on the constants, a polynomial-chaos surrogate with Sobol sensitivities, Markov-chain sampling with an embedded model error, MAP sets; seven Spalart–Allmaras constants recalibrated under finite-volume and DG discretizations, the SST and k-ω calibrations reviewed for supersonic flows, and Bayesian optimization."
status: established
aliases: [Bayesian calibration, Bayesian recalibration, Bayesian uncertainty quantification of closure coefficients, MAP calibration, polynomial-chaos calibration, non-intrusive polynomial chaos, embedded model error, turbo-RANS]
tags: [uncertainty-quantification, rans, data-driven, dg, compressible]
timestamp: 2026-10-29T10:04:00Z
---

# Bayesian calibration of turbulence-model coefficients

**Bayesian calibration** treats the closure coefficients
$\boldsymbol\theta$ of a RANS model (registry: model coefficients) as
random variables with a prior distribution, and updates them with data
$\boldsymbol d$ through Bayes' theorem,
$p(\boldsymbol\theta\mid\boldsymbol d)\propto p(\boldsymbol d\mid\boldsymbol\theta)\,p(\boldsymbol\theta)$.
The posterior gives a most probable coefficient set (the maximum a
posteriori, MAP, estimate), the spread of the coefficients the data
allow, and, propagated through the model, a predictive distribution of the
quantity of interest. In the four-layer taxonomy recorded on
[model-form uncertainty](/definitions/model-form-uncertainty.md) it acts on
the coefficient layer (L4) only: the functional form of the model is kept.
That page also records the review-level formulation (MAP objective,
Kennedy–O'Hagan discrepancy) and the early applications that Duraisamy et
al. (2019, §3.2, §5.1) cite. This page collects the full workflow of
[An et al. (2025)](/sources/an-2025.md) for seven
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) constants under two
discretizations, the supersonic-flow calibrations reviewed by
[Le et al. (2024)](/sources/le-2024.md), and the Bayesian-optimization
calibration reviewed by [Fang et al. (2026)](/sources/fang-2026.md).

Page-local symbols: $\boldsymbol d=(d_1,\dots,d_L)$ the data at $L$
stations, $\boldsymbol o(\boldsymbol\theta)$ the model output at the same
stations (as on the model-form page), $n_\theta$ the number of calibrated
coefficients, $s_{\mathrm e}^2$ and $s_{\mathrm m}^2$ the measurement and
model-discrepancy variances, $\boldsymbol z$ the standard random germ of a
polynomial-chaos expansion, $\varphi_k$ its orthogonal polynomials,
$a_k$ their coefficients, $\mathcal S_i$ the first-order Sobol index of
coefficient $i$.

## The likelihood with a model discrepancy

An et al. (2025, §2.3.2, Eqs. 19–22) write each datum as the truth plus
measurement noise, and the truth as the model plus a discrepancy
$\delta(x_i)$ (the registry's $\boldsymbol\delta$):

$$d_i=o_i(\boldsymbol\theta)+\delta(x_i)+\epsilon_i,\qquad \delta\sim N(0,s_{\mathrm m}^2),\quad \epsilon_i\sim N(0,s_{\mathrm e}^2),$$

so that the log-likelihood is

$$\ln p(\boldsymbol d\mid\boldsymbol\theta)=-\sum_{i=1}^{L}\frac{\big[d_i-o_i(\boldsymbol\theta)\big]^2}{2(s_{\mathrm m}^2+s_{\mathrm e}^2)}-\frac L2\ln\big[2\pi(s_{\mathrm m}^2+s_{\mathrm e}^2)\big],$$

with the noise level $s_{\mathrm e}$ inferred together with the
coefficients. The posterior is sampled by Markov-chain Monte Carlo (MCMC)
and represented by kernel density estimates; An et al. state that MCMC
"typically" needs $\mathcal O(10^5)$ to $\mathcal O(10^6)$ effective
samples and use 100 000 (§2.3.2, §3.1). Le et al. (2024, §3.1.1) report
the same sample range for the MCMC calibration of SA and SST by Hosder et
al., and cite Sargsyan et al. for the remark that the MAP point can be
found by optimization without MCMC. The MAP objective with Gaussian prior
and likelihood is the one written on
[model-form uncertainty](/definitions/model-form-uncertainty.md).

**Embedded model error.** A discrepancy added to the output, as above, is
the form that Duraisamy et al. (2019, §3.4) call physics-agnostic when it
is a Gaussian process. An et al. use instead the embedded model-error
approach of Sargsyan et al. (as cited, ref. [30]): the discrepancy is put
inside the coefficients,

$$\boldsymbol\theta_{\mathrm{emb}}=\boldsymbol\theta+\mathsf A(\boldsymbol a)\,\boldsymbol z_{\mathrm e},\qquad \mathsf A(\boldsymbol a)=\mathrm{diag}(a_1,\dots,a_J),$$

with $\boldsymbol z_{\mathrm e}$ a vector of $J$ independent standard
normal variables and the magnitudes $a_j$ (page-local) calibrated for the
error-embedded coefficients and zero for the others (§2.3.2, Eq. 23). The
model output becomes random, $d_i=o_i(\boldsymbol\theta_{\mathrm{emb}})+\epsilon_i$,
is expanded in polynomial chaos in $\boldsymbol z_{\mathrm e}$, and enters
a Gaussian likelihood through its mean $\mu_i$ and variance
$s^2_{\mathrm{emb},i}$:

$$\ln p(\boldsymbol d\mid\boldsymbol\theta)=-\sum_{i=1}^{L}\frac{\big[d_i-\mu_i\big]^2}{2\big(s^2_{\mathrm{emb},i}+s_{\mathrm e}^2\big)}-\frac12\sum_{i=1}^{L}\ln\big[2\pi\big(s^2_{\mathrm{emb},i}+s_{\mathrm e}^2\big)\big]$$

(Eqs. 24–26). The paper does not say which coefficients carry the embedded
error (§2.3.2).

**Variance decomposition.** The posterior predictive variance at a station
is split into three parts (Eqs. 29–30),

$$s_p^2=s^2_{\mathrm{emb}}+s^2_{pp}+s^2_{s},$$

the mean of the posterior variances, which the authors call model error;
the variance of the posterior means, called posterior uncertainty; and the
surrogate error, the mean squared difference between surrogate and RANS
over the validation samples (page-local $s_p$, $s_{pp}$, $s_s$). Posterior
means are reported with 90% intervals.

## Surrogate and sensitivities: polynomial chaos

Because each likelihood evaluation needs a RANS solution, An et al. (2025,
§2.3.1, Eqs. 15–18) replace the solver by a non-intrusive polynomial-chaos
(PC) surrogate of the output at each wall station,

$$o(\boldsymbol\theta)\approx\sum_{k=1}^{K-1}a_k\,\varphi_k(\boldsymbol z)\quad\text{(Eq. 16)},\qquad N_{\mathrm{PC}}=\frac{(n_\theta+q)!}{n_\theta!\,q!}\quad\text{(Eq. 17)},$$

with the coefficients mapped to the germ by their own expansion
(Eq. 15), $q$ the polynomial order and $N_{\mathrm{PC}}$ the number of
terms of an order-$q$ expansion (page-local; the summation limit $K$ is
printed as such, and its relation to $N_{\mathrm{PC}}$ is not stated). The coefficients $a_k$ are fitted by
regression on $n_e N_{\mathrm{PC}}$ RANS samples, $n_e$ the oversampling
ratio (page-local). The first-order Sobol index of coefficient $i$ follows
from the expansion without further runs,

$$\mathcal S_i\approx\frac{1}{s_y^2}\sum_{j=1}^{N_i}a^2_{k_j(i)}\,\lVert\varphi_{k_j(i)}\rVert^2,$$

with $k_1(i),\dots,k_{N_i}(i)$ the indices of the expansion terms of
coefficient $i$ (as printed), $\lVert\varphi\rVert^2$ the squared norm of a basis
polynomial and $s_y^2$ the variance of the output (page-local; Eq. 18).
With $n_\theta=7$, $q=2$ and $n_e=2$, An et al. use $N_{\mathrm{PC}}=36$,
72 Latin-hypercube training samples and 36 validation samples (§3.1).
The same machinery appears in the bundle in
[Cherroud et al. (2022)](/sources/cherroud-2022.md), who propagate the
posteriors of sparse-Bayesian SST corrections with second-order Hermite
polynomial chaos and compute Sobol indices from it (details on
[model-form uncertainty](/definitions/model-form-uncertainty.md)), and in
Yang et al.'s non-intrusive-PC, Bayesian and particle-swarm calibration of
SST, as reviewed by Le et al. (2024, §3.1.1; below).

## Seven Spalart–Allmaras coefficients under two discretizations (An et al. 2025)

**Set-up.** An et al. (2025) calibrate seven SA constants,
$\boldsymbol\theta=(c_{b1},c_{b2},\sigma,c_{w2},c_{w3},c_{v1},\kappa)$,
which they call the most sensitive to complex flow structures, with
$c_{w1}$ following from its formula (§3.1, Table 1). The authors state
that $c_{b1}$, $c_{b2}$ and $\sigma$ are fixed by free shear flows and the
other four by the zero-pressure-gradient flat-plate boundary layer, citing
the original model (§3.1). Priors are uniform: $\sigma\in[0.6,1]$,
$c_{w2}$, $c_{w3}$, $c_{v1}$ and $\kappa$ within $\pm50\%$ and $c_{b1}$,
$c_{b2}$ within $\pm25\%$ of the original values ($c_{b1}=0.1355$,
$c_{b2}=0.622$, $\sigma=2/3$, $c_{w2}=0.3$, $c_{w3}=2$, $c_{v1}=7.1$,
$\kappa=0.41$), chosen "to ensure that non-physical solutions do not
occur" (§2.1, §3.1, Table 1). Every calibration uses wall $C_p$ or wall
$C_f$ alone, never both (Eq. 27). The same workflow is run with two
solvers:

- a second-order cell-centred finite-volume method, NASA CFL3D (MUSCL
  reconstruction, Roe flux, central viscous fluxes, approximate
  factorization) (§2.2.1);
- the authors' in-house third-order
  [discontinuous Galerkin](/methods/discontinuous-galerkin-spectral-element-method.md)
  RANS–SA solver (Roe flux, $p$-multigrid-preconditioned GMRES with
  line-implicit Gauss–Seidel smoothing), with a modal troubled-cell
  detector built on $\rho\tilde\nu$, a Hermite-WENO limiter and a
  positivity limiter on $\tilde\nu$ (§2.2.2, App., Eqs. A.1–A.2; see
  [shock sensors](/definitions/shock-sensor.md) and
  [WENO schemes](/methods/weno-scheme.md)).

All computations are two-dimensional steady RANS.

**Calibration flows.** The Driver–Seegmiller
[backward-facing step](/benchmarks/backward-facing-step.md)
($Re_H=36\,000$, $M=0.128$, experiment; finite-volume grid
$436\times225$ with $y^+\approx1$, DG grid $249\times81$ with
$y^+\approx4$, "only 0.21 times the size") and the
[Gaussian bump](/benchmarks/gaussian-bump.md) at $Re_L=10^6$, $M=0.2$
(DNS of Uzun & Malik; finite volume $401\times161$, $y^+\approx1$, DG
$\approx201\times81$, $y^+\approx5$) (§3.1–3.2, Table 2).

**Baseline comparison.** On the step, DG on the coarser grid gives results
"comparable to or even better than" finite volume: finite volume is better
for $C_p$ before the step and in the separation zone, DG after
reattachment, especially in $C_f$; both overpredict $C_f$ before the step
and in the separation zone, and both predict a separation size in good
agreement with the experiment (§3.1, Fig. 6). On the bump DG is better at
the crest and in the small separation (§3.2, Fig. 16). The authors
hypothesize that the lower dissipation of the high-order scheme "may
amplify" the model's errors in the separated shear layer, where SA is
outside its calibration (§3.1; see
[numerical dissipation](/properties/numerical-dissipation.md)).

**Sensitivities (§3.1–3.2, Figs. 9, 17).**

- $\kappa$, $c_{b1}$ and $c_{v1}$ carry most of the variance on the step
  for either scheme and either quantity; $\kappa$ "remains the dominant
  contributor", largely unaffected by the discretization.
- Under DG the contribution of $c_{b1}$ falls (most for $C_p$) and that of
  $c_{v1}$ is "approximately 120% higher than in the FVM scheme", mainly at
  reattachment and in recovery.
- In finite volume $c_{v1}$ becomes the second most influential
  coefficient for $C_f$ from reattachment on; the authors offer two
  hypotheses: $C_f$ depends on velocity gradients and $C_p$ on velocity,
  and $C_f$ depends on the Reynolds shear stress, to which they tie
  $c_{v1}$ (citing Atzori et al. and Renard & Deck; see
  [skin-friction decomposition](/definitions/skin-friction-decomposition.md)).
- On the bump, $c_{b2}$, $\sigma$ and $c_{w3}$, insensitive on the step,
  show "a substantial increase in sensitivity", higher under DG; the
  authors tie them to first derivatives whose computation changes with
  streamline curvature and with high-order discretization. The
  sensitivity of $c_{v1}$ falls in the favourable gradient, which they
  attribute to relaminarization, and rises in the adverse gradient and in
  separation.

The physical attributions are stated by the authors as hypotheses; the
indices are the computed result.

**Surrogate and posterior.** The PC surrogate's relative error stays below
20% for $C_p$ (absolute error below 0.03); for $C_f$ it is below 10% in
most regions but reaches 80% at $x/H\approx0$, where $C_f\approx0$
(§3.1, Eq. 28, Fig. 10). In the variance decomposition the model error is
"considerable across all positions, especially in the separation region",
the posterior uncertainty concentrates near separation, and the surrogate
error is the smallest part; for $C_f$ calibration all DG parts are
"significantly smaller" than the finite-volume ones except in parts of the
separation zone (§3.1, Fig. 12). Calibrated on $C_f$, DG gives more accurate
posteriors with wider intervals that cover the data (§3.1, Fig. 11). The
posteriors of the three or four most sensitive coefficients are unimodal;
$c_{b1}$ is flat under finite volume and unimodal under DG, and the
inference of $c_{w3}$ from finite-volume $C_p$ "fails to yield reliable or
significant results" (§3.1, Figs. 13–14).

**MAP sets.** Two flows, two schemes and two quantities give eight MAP
sets (§3.3, Table 3; $C_p$ / $C_f$ calibration):

| Coefficient | step, FV | step, DG | bump, FV | bump, DG |
|---|---|---|---|---|
| $c_{b1}$ | 0.11857 / 0.11780 | 0.10304 / 0.11776 | 0.13816 / 0.133725 | 0.12492 / 0.12352 |
| $c_{b2}$ | 0.77421 / 0.46899 | 0.56069 / 0.46972 | 0.74489 / 0.50965 | 0.593825 / 0.58488 |
| $\sigma$ | 0.61406 / 0.78930 | 0.89941 / 0.99171 | 0.93369 / 0.91766 | 0.85145 / 0.717545 |
| $c_{w3}$ | 1.3590 / 1.8418 | 2.9789 / 1.5261 | 2.3040 / 2.8558 | 2.8919 / 2.1408 |
| $c_{v1}$ | 3.59145 / 9.6510 | 9.1208 / 8.9585 | 8.9318 / 9.7334 | 9.9965 / 10.378 |
| $\kappa$ | 0.61481 / 0.60892 | 0.238365 / 0.24679 | 0.21765 / 0.41909 | 0.39771 / 0.41882 |
| $c_{w2}$ | 0.43921 / 0.44389 | 0.16533 / 0.44149 | 0.445975 / 0.21669 | 0.43373 / 0.37144 |

Several MAP values lie within 1.5% of a prior bound: $\kappa=0.61481$
(bound 0.615), $c_{b2}=0.77421$ (0.7775), $c_{w3}=2.9789$ (3), $\sigma=0.99171$
(1), $c_{w2}=0.445975$ and $0.44389$ (0.45), $c_{v1}=3.59145$ (3.55),
$c_{b1}=0.10304$ (0.101625), the bounds taken from Table 1 *(compiler
check, not in the sources)*; the paper does not comment on it. In Shan et
al.'s metaheuristic calibration of SA several calibrated values equal a
bound of its $\pm50\%$ box (see
[ensemble Kalman calibration](/methods/ensemble-kalman-closure-calibration.md)).
The calibrated $\kappa$ spans 0.218 to 0.615 across the eight sets, while
the paper itself states that $\kappa$ is fixed by the flat-plate boundary
layer (§3.1).

**The final set.** The authors combine the eight sets into one "modified SA
model tailored for DG schemes" by rules (§3.3, Table 4, §5): $c_{b2}$,
$\sigma$, $c_{w3}$, $c_{v1}$ and $\kappa$ follow the high-order results,
$c_{b1}$ prioritizes finite volume, $c_{w2}$ (negligible sensitivity) is
left at 0.3; the offsets are weighted "based on the deviation error between
the baseline SA model computations and high-fidelity data as well as the
magnitude of sensitivity to numerical schemes", then "validated and
fine-tuned" in the two calibration cases. The weights are not given.

| | $c_{b2}$ | $\sigma$ | $c_{w3}$ | $c_{v1}$ | $\kappa$ | $c_{b1}$ (separation) | $c_{b1}$ (boundary layer) |
|---|---|---|---|---|---|---|---|
| original | 0.622 | 0.667 | 2 | 7.1 | 0.41 | 0.1355 | 0.1355 |
| final | 0.592 | 0.806 | 2.641 | 10.3 | 0.39 | 0.1186 | 0.1382 |

The paper does not say how a computation switches between the two
$c_{b1}$ values (§3.3).

**Validation (§4).** With the final set:

- Gaussian bump at $Re_L=2\times10^6$ (finite volume $401\times201$, DG
  $181\times93$): the baseline SA "nearly eliminate[s]" the large
  separation behind the bump; the calibrated model improves the separation
  zone little but aligns with the DNS in the crest transition region,
  "yielding 26.44% error reduction versus baseline" in $C_f$ (§4.1,
  Figs. 20–21);
- HiFi-TURB-DLR rounded step ($Re_H=78\,490$, $M=0.13455$, no
  separation, ERCOFTAC DNS reference): about 25% overall reduction of the
  $C_f$ error, near the pressure-gradient transition (§4.2, Figs. 23–24);
- [NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md)
  ($Re_c=9.36\times10^5$, $M=0.1$): "limited improvements" in $C_f$; the
  DG calibrated model improves $C_p$ at the crest transitions and in the
  separation zone (§4.3, Figs. 26–27).

## Calibrated coefficients depend on the discretization

An et al. (2025, §3.3, §5) argue that coefficients calibrated for
second-order finite-volume practice are not optimal for a high-order DG
discretization. Their Table 3 prints, on the step, a MAP $\kappa$ of
0.61481 / 0.60892 under finite volume and 0.238365 / 0.24679 under DG
($C_p$ / $C_f$ calibration). [Fanizza et al. (2025)](/sources/fanizza-2025.md)
(§1) argue, for inferred correction *fields* and without a
finite-volume–DG comparison, that corrections inferred on diffusive
second-order discretizations contain a discretization component (see
[model-form uncertainty](/definitions/model-form-uncertainty.md) and
[field inversion](/methods/field-inversion-machine-learning.md)).

## Calibrations surveyed by Le et al. (2024)

Le et al. (2024, §3.1.1, pp. 10–11), reviewing machine learning for
supersonic flow and combustion, open with the premise of the method:
nominal coefficients are developer calibrations on simple flows, and
"There is currently no evidence suggesting that nominal values perform
well across all types of flows". The works they cite, as they describe
them (no coefficient values are printed in the review):

- Bayesian uncertainty quantification of SA in incompressible boundary
  layers (Cheung et al.), of SA for supersonic jet interaction (Li et al.)
  and, by an efficient Bayesian method, of a $k$-$\omega$-$\gamma$
  transition model and SST on a supersonic flat plate (Zhang & Song);
  uncertainty quantification of the closure coefficients on the RAE 2822
  (Schaefer et al.; see
  [RAE 2822 airfoil](/benchmarks/rae-2822-airfoil.md)) and of the
  closure-coefficient uncertainty for a scramjet isolator and strut
  injector (Di Stefano et al.);
- Bayesian recalibration of three
  [$k$-$\omega$ models](/methods/k-omega-model.md) for hypersonic
  [shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
  (Li et al.);
- Bayesian calibration of [SST](/methods/k-omega-sst-model.md) in
  compression corners at $M\approx2.85$ (Tang et al.): turbulence near the
  wall is enhanced by a larger eddy viscosity and the adverse-gradient
  prediction improves, but SST "cannot simulate the inherent shock
  instability" by modified coefficients, and the separation-region wall
  pressure "remains too high" (Fig. 8);
- SST coefficients calibrated on a $24^\circ$ compression corner and
  applied to $20^\circ$, $16^\circ$ and $8^\circ$ corners and to $M=2.9$,
  close to experiment, "confirming the turbulence model parameters'
  applicability within a narrow range of Mach numbers" (Fig. 9);
- non-intrusive PC, Bayesian inference and particle-swarm optimization of
  SST for supersonic cavities and hollow cylinders (Yang et al., the
  authors' group): the maximum relative wall-pressure error falls "from
  29.71% to 9.00%" and the average "from 9.86% to 3.67%", the MAP values
  beating the nominal ones on three criteria.

The review's Table 3 credits uncertainty analysis with quantifying model
error and charges it with "Excessive cost" (p. 15).

## Bayesian optimization of RANS coefficients (as reviewed by Fang et al. 2026)

Fang et al. (2026, §3.4, §4.3, Table 3) describe turbo-RANS (McConkey et
al., as cited) as a calibration of RANS coefficients by Bayesian
optimization with a new objective function, GEDCP, usable with holistic,
sparse or dense data; Table 3 quotes an accuracy gain "by 12–26% compared
to default RANS model". As the review describes it, the method returns
one optimized coefficient set; no posterior distribution is described.
The review files it among data-driven optimal-control strategies
(§3.4), not under uncertainty quantification (§4.2.4).

## Relation to other calibration routes

- **Ensemble Kalman filter.** A derivative-free ensemble update of the
  coefficients toward the data; in this bundle it calibrates one LES
  constant against spectra (see
  [ensemble Kalman calibration](/methods/ensemble-kalman-closure-calibration.md)).
- **Metaheuristic optimization.** Shan et al. (2023) calibrate nine SA
  constants against measured pressure by teaching–learning-based
  optimization, a point estimate without a posterior (same page).
- **Sparse Bayesian regression.** Cherroud et al. (2022) obtain Gaussian
  posteriors for the coefficients of a learned correction, not of the
  baseline model (see
  [symbolic-regression closures](/methods/symbolic-regression-closure.md)).
- **Field inversion.** The correction becomes a spatial field
  $\beta(\boldsymbol x)$ and the MAP problem is high-dimensional (see
  [field inversion and machine learning](/methods/field-inversion-machine-learning.md)).
  [Brenner et al. (2022)](/sources/brenner-2022.md) (§1) class
  polynomial-chaos, ensemble-Kalman and approximate-Bayesian calibration of
  coefficients as parametric calibration with limited gains, because no
  universal optimal coefficients may exist.

## Qualifications

- **Scope of the gains.** Brenner et al. (2022, §1) class coefficient
  calibration as parametric calibration with limited gains and give no
  test of their own. An et al. (2025) report reductions of 26.44% (bump
  crest transition region) and about 25% (rounded step, $C_f$) in
  attached pressure-gradient regions, "limited improvement" in the bump
  separation and "limited improvements" on the hump (§4); their variance
  decomposition puts the model error highest in the separation region
  (§3.1, Fig. 12).
- **Flow-specific sets.** The eight MAP sets of An et al. differ widely
  ($c_{v1}$ from 3.59 to 10.38, $\kappa$ from 0.218 to 0.615; Table 3), as do
  Shan et al.'s, and Le et al.'s reviewed SST calibration transfers only
  "within a narrow range of Mach numbers". Duraisamy et al. (2019, §4.2)
  state that optimal coefficients are flow-specific (see
  [model-form uncertainty](/definitions/model-form-uncertainty.md)).
- **Printed slips in An et al. (2025).** Table 1 prints the row "Upper
  boundary" with the smaller value in every column and "Lower boundary"
  with the larger; the text gives the $c_{b1}$, $c_{b2}$ range as "±25
  times the original value", while Table 1 gives $0.75$ and $1.25$ times
  ($0.101625=0.75\times0.1355$, $0.7775=1.25\times0.622$) *(compiler check,
  not in the sources)*; "the range of $C_2$" (§3.1) is that of $c_{w2}$
  (bounds 0.15–0.45 in Table 1); the oversampling ratio is $n_e$ in §2.3.1
  and "$n_p=2$" in §3.1; Eq. 18 calls $\sigma$ "the standard variance" of
  the output, which enters as a variance; Eqs. 21–22 print mismatched
  brackets; the PC sums run to $K-1$ in Eqs. 15–16 and to $K$ in Eq. 24;
  the posterior mean is $\mu_p$ in §3.1 and $\mu_x$ in §3.2; the bump DNS
  is attributed to "Malik et al." while the reference lists Uzun & Malik.
  The validation grids are said to reduce the grid points "by 54%"; from
  the printed sizes $181\times93=16\,833$ against $401\times201=80\,601$ the
  reduction is 79%, and 54–55% is the per-direction reduction
  ($181/401=0.451$, $93/201=0.463$) *(compiler check, not in the sources)*.
  §3.3 states that the high-order MAP values of $\kappa$ "consistently
  deviat[e] below normative values" and that $c_{w3}$ is larger under the
  high-order scheme; Table 3 prints $\kappa=0.41882$ (bump, DG, $C_f$) and
  $c_{w3}=1.5261$ (step, DG, $C_f$), exceptions to both statements.
- **Attributions in Le et al. (2024).** The $24^\circ$-corner calibration
  is attributed to "Gaitonde and Adler [151]", whose printed reference is
  a review titled "Dynamics of three-dimensional shock-wave/boundary-layer
  interactions"; the model list "$k$-$\varepsilon$ [130], $k$-$\omega$
  [131]" cites by title a $k$-$\omega$ paper (Wilcox 1988) as [130] and a
  $k$-$\varepsilon$ paper (Launder & Spalding 1974) as [131], and "SST
  [132]" is a calibration study of SST, not its origin (§3.1.1). The page
  therefore names the reviewed works by the authors as printed in the text
  and does not use these reference numbers for origins.
- **GEDCP.** Fang et al. (2026) expand the acronym two ways for the same
  reference: "Generalized Error and Default Coefficient Preference"
  (p. 2844) and "Gradient-Enhanced Data-Consistency Penalization"
  (p. 2855).
- **Notation.** An et al. write the coefficients $\boldsymbol\lambda$, the
  PC germ and the embedded germ both $\boldsymbol\xi$, the basis $\Psi_k$,
  the variances $\sigma_e^2$, $\sigma_m^2$ and the Sobol index $S_i$; the
  page translates them to $\boldsymbol\theta$, $\boldsymbol z$,
  $\boldsymbol z_{\mathrm e}$, $\varphi_k$, $s_{\mathrm e}^2$,
  $s_{\mathrm m}^2$ and $\mathcal S_i$, because the registry gives $\xi$,
  $\sigma$ and $S$ other meanings. The SA constants are written in lower
  case as on the SA page (the source's $C_{b1}$, …).

# Citations

- [An et al. (2025)](/sources/an-2025.md) — §1, §2.1 (SA constants), §2.2.1–2.2.2 (CFL3D and DG solvers), §2.3.1, Eqs. 15–18 (polynomial chaos, Sobol indices), §2.3.2, Eqs. 19–30 (likelihood, embedded model error, variance decomposition), §3.1, Table 1, Figs. 6–14 (backward-facing step: priors, baseline, sensitivities, surrogate error, posteriors), §3.2, Table 2, Figs. 16–18 (Gaussian bump), §3.3, Tables 3–4 (MAP sets, final set), §4.1–4.3, Figs. 20–27 (validation), §5, App. Eqs. A.1–A.2.
- [Le et al. (2024)](/sources/le-2024.md) — §3.1.1, pp. 10–11, Figs. 8–9 (nominal values, reviewed Bayesian calibrations of SA, $k$-$\omega$ and SST, MCMC cost, MAP by optimization, PC–Bayes–PSO calibration); Table 3, p. 15 (cost of uncertainty analysis).
- [Fang et al. (2026)](/sources/fang-2026.md) — §3.4, §4.3, Table 3 (turbo-RANS calibration by Bayesian optimization, GEDCP, pp. 2844, 2855).
- [Fanizza et al. (2025)](/sources/fanizza-2025.md) — §1 (discretization component of inferred corrections).
- [Brenner et al. (2022)](/sources/brenner-2022.md) — §1 (parametric calibration with limited gains).
- [Cherroud et al. (2022)](/sources/cherroud-2022.md) — §4.2–4.3 (polynomial-chaos propagation and Sobol indices of sparse-Bayesian corrections).
- [Shan et al. (2023)](/sources/shan-2023.md) — §II.B, §III.B–C, Table B1 (metaheuristic calibration of SA, case-dependent sets).
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §3.2, §3.4, §4.2, §5.1 (Bayesian calibration, output discrepancy, flow-specific coefficients).
