---
type: Method
title: "Ensemble Kalman filter calibration of turbulence closures"
description: "Derivative-free calibration of closure parameters from data with an ensemble of solver runs updated by a Kalman analysis; listed for RANS field inversion and used in LES to calibrate the dissipative coefficient of a gradient-plus-Smagorinsky mixed model against filtered-DNS energy spectra, with shifting and inflation for convergence."
status: established
aliases: [EnKF, ensemble Kalman filter, ensemble Kalman inversion, ensemble data assimilation, EnKF-MM, EnKF mixed model, EnKF-FM]
tags: [data-driven, field-inversion, sgs-model, les, uncertainty-quantification]
timestamp: 2026-10-26T20:51:00Z
---

# Ensemble Kalman filter calibration of turbulence closures

The **ensemble Kalman filter** (EnKF) calibrates the free parameters of a
closure by running an ensemble of simulations, each with its own parameter
values, and updating every member toward the data with a Kalman gain built
from the ensemble covariance. It needs no derivative of the solver: the
model equations enter only through the forward runs. In this bundle it
appears as one of the solvers of RANS
[field inversion](/methods/field-inversion-machine-learning.md), next to
adjoint-based optimization (Duraisamy et al. 2019, §5.1; Yan et al. 2022,
§1), and, in [Wang et al. (2023c)](/sources/wang-2023-c.md), as an a
posteriori calibration of an LES subgrid model inside the running LES (see
[model-consistent training](/methods/model-consistent-training.md)).

## Place among inversion methods

- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) (§5.1) list
  "derivative-free iterative ensemble Kalman methods" (recalled from
  Iglesias et al. 2013) beside adjoint-based optimization as solvers of
  the field-inversion problem.
- [Yan et al. (2022)](/sources/yan-2022.md) (§1) name Markov-chain Monte
  Carlo and the EnKF as methods for the full Bayesian posterior of the
  correction field, and the MAP estimate, which they compute by adjoints,
  as "field inversion or data assimilation".
- Wang et al. (2023c, §I, §V) place the EnKF among data-assimilation
  approaches to SGS modelling (adjoint-based variational methods, nudging,
  ensemble methods) and set it against a priori-trained neural-network
  closures, which "often" under-perform or go unstable a posteriori. They
  call the EnKF "numerically more convenient" than the adjoint-based
  variational calibration of their own group, add that finite differences
  would also do for a one-parameter problem, and expect the ensemble
  method to pay off in high-dimensional optimization (§V). No cost
  comparison is given.
- [Fanizza et al. (2025)](/sources/fanizza-2025.md) (§1) name ensemble
  Kalman methods as an alternative to variational data assimilation for
  steady RANS problems and use the variational route themselves: a
  discrete adjoint of a high-order DG Spalart–Allmaras solver with L-BFGS,
  for correction fields with one set of polynomial coefficients per element
  (see [field inversion and machine learning](/methods/field-inversion-machine-learning.md)).
- [Zhao et al. (2025)](/sources/zhao-2025.md) (§4) cite the ensemble
  data assimilation of Wang et al. (2023c) as the motivation for learning
  the Smagorinsky coefficient of their
  [physics-informed neural-operator surrogate](/methods/neural-operator-les-surrogate.md),
  but calibrate it by gradient descent on the residual of the filtered
  equations evaluated on one trajectory, not by an ensemble.

**A gradient-based counterpart.** The two LES calibrations differ in
target and filter, so their values are not comparable. Wang et al. (2023c)
match the filtered-DNS energy spectrum in forced isotropic turbulence at
$Re_\lambda\approx160$ (Gaussian filter, ratio 2) and obtain
$C_{\mathrm f}\approx0.00738$ for the dissipative part of a mixed model,
or 0.01 for a pure Smagorinsky-type model (App. C). Zhao et al. (2025,
Table 4) minimize the residual of the Smagorinsky-closed equations on
sharp-spectral-filtered DNS of decaying isotropic turbulence at
$Re_\lambda\approx60$ ($k_c=10$) and obtain $C_s\approx0.19$, and
$C_s\approx0.1$ when the data are Smagorinsky LES run with $C_s=0.1$, the
coefficient that generated them. With $C_{\mathrm f}=2C_s^2$, Wang et al.'s pure-model value
corresponds to $C_s\approx0.07$ *(compiler check, not in the sources)*.

## The mixed SGS model calibrated (Wang et al. 2023c)

Wang et al. (2023c) (arXiv v3) close incompressible LES with a mixed
model: the [gradient (Clark) model](/methods/gradient-model.md), with its
Taylor-expansion coefficient kept, plus a
[Smagorinsky](/methods/smagorinsky-model.md)-type dissipative part
(§II.A, Eq. 14):

$$\tau_{ij}=\frac{\Delta^2}{12}\frac{\partial\bar u_i}{\partial x_k}\frac{\partial\bar u_j}{\partial x_k}-C_{\mathrm f}\,\Delta^2\lvert\bar S\rvert\bar S_{ij},$$

with $\tau_{ij}$ the full (positive-trace) SGS stress and $C_{\mathrm f}$
(page-local; the paper's $C_D$) the single calibrated coefficient. The
functional part carries no factor two, so $C_{\mathrm f}$ corresponds to
$2C_s^2$; the paper bounds its initial ensemble by
$2C_s^2\approx0.05$ with $C_s=0.16$ (§III). The structural coefficient is
kept at $1/12$ "to retain its a priori SGS accuracy", justified by the
group's earlier adjoint study in which that coefficient stayed close to
its original value when optimized (§II.A). The paper calls the model
EnKF-MM.

## The calibration loop (§II.B, Eqs. 15–18, Fig. 1)

Page-local notation: $N_e$ ensemble members; $\boldsymbol e_i$ the state
of member $i$; $\boldsymbol q$ the observations; $\mathsf H$ the
observation matrix; $\mathsf P$ the ensemble covariance; $\mathsf K$ the
Kalman gain; $\mathsf R$ the observation-noise covariance; $\boldsymbol w_i$
the observation noise.

- **State.** Each member's state is the LES energy spectrum $E(k)$ at $n$
  observation instants, concatenated with the member's coefficient: a
  vector of size $n\,k_c+1$, with $k_c$ the largest resolved wavenumber. The observation $\boldsymbol q$ is the
  filtered-DNS spectrum at the same instants, and $\mathsf H$ selects the
  spectrum entries of the state. Taking the spectrum itself as part of the
  state avoids building an observation operator from flow variables, and
  matching a spectrum rather than fields avoids pointwise comparison of
  chaotic solutions.
- **Analysis.**
  $$\boldsymbol e^{a}_i=\boldsymbol e_i+\mathsf K\big(\boldsymbol q-\mathsf H\boldsymbol e_i+\boldsymbol w_i\big),\qquad \mathsf K=\mathsf P\mathsf H^T\big(\mathsf H\mathsf P\mathsf H^T+\mathsf R\big)^{-1},$$
  $$\mathsf P=\frac{1}{N_e-1}\sum_{i=1}^{N_e}(\boldsymbol e_i-\boldsymbol e_{\mathrm{mean}})(\boldsymbol e_i-\boldsymbol e_{\mathrm{mean}})^T,$$
  with $\boldsymbol e_{\mathrm{mean}}$ the ensemble mean and $\mathsf R$ approximated as diagonal. The
  observation noise is uniform at machine level, $U(-1,1)\times10^{-7}$,
  "of order $10^{-7}$ for a single-precision solver", because the data
  come from DNS (§III, Table II).
- **Loop.** (1) draw the coefficients uniformly in $(0,0.05)$; (2) start
  every member from the same filtered-DNS field; (3) run the LES;
  (4) store the spectra at the observation instants; (5) compute LES and
  filtered-DNS spectra; (6) update the coefficients; (7) repeat from (2)
  for a fixed number of iterations. The misfit is the summed absolute
  spectrum error over instants and wavenumbers (Eq. 20).
- **Shifting (§IV, Eq. 25).** In the mixing layer every member's
  coefficient is shifted by the difference between the coefficient of the
  best member (smallest spectrum error) and the ensemble mean, which drags
  the ensemble toward the best member; the authors state that this step
  "must be additionally incorporated" for convergence there. No run
  without it is shown.
- **Inflation (Eq. 26).** Deviations from the ensemble mean are multiplied
  by a factor $F$; $F=1.5$ lets an ensemble of 10 reach the converged value
  that ensembles of 20 and 40 reach without inflation, with a larger
  remaining ensemble spread (§IV, Fig. 11).

## Calibrated values and settings

| Flow | DNS | LES | EnKF settings | Calibrated $C_{\mathrm f}$ |
|---|---|---|---|---|
| forced [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md), $Re_\lambda\approx160$ | $512^3$ pseudospectral | $64^3$, Gaussian filter $\Delta=16$ DNS spacings, filter-to-grid ratio 2 | $N_e=10$ and 20, 50 iterations, observations every $0.3$ large-eddy turnover times over 6 | about 0.00738 for both ensemble sizes |
| temporal mixing layer | $256\times512\times512$ | $64\times128\times128$, $\Delta=8$ DNS spacings | $N_e=10$, 20, 40, 20 iterations, observations every $10\tau_\theta$ from $50\tau_\theta$ to $800\tau_\theta$ ($\tau_\theta=\theta_0/\Delta U$, $\theta_0$ the initial momentum thickness, $\Delta U$ the velocity difference); shifting, inflation for $N_e=10$ | about 0.01 |

(§III–IV, Tables I–IV.) The isotropic value is far below the
$2C_s^2\approx0.05$ of the classical $C_s=0.16$: the authors call the tuned
functional coefficient "no more than 20 percent of its original value" and
conclude that the structural part dominates the model (App. C). The filter-to-grid ratio of two is
chosen so that numerical errors are much smaller than the SGS model's
contribution (§III).

## A posteriori results (§III–IV, Apps. A–C)

Against the dynamic Smagorinsky model, the dynamic mixed model and the
pure gradient model, all compared with filtered DNS:

- *Isotropic turbulence.* EnKF-MM is closest in spectrum and
  kinetic-energy evolution; the dynamic models slightly overestimate
  large-scale and underestimate small-scale energy, the pure gradient
  model does the reverse (Fig. 3). EnKF-MM also gives the best PDFs of
  strain and rotation rate and of the SGS energy flux $\Pi$, and the best
  longitudinal structure functions of orders 2 to 8, with an accuracy that
  degrades with the order, which the authors relate to calibrating on a
  second-order statistic (Figs. 5–9; see
  [energy backscatter](/definitions/energy-backscatter.md)).
- *SGS stress against flow statistics.* The pure gradient model has the
  stress PDFs closest to filtered DNS but the worst kinetic energy;
  adding the calibrated dissipative part slightly degrades the stress
  PDFs (Figs. 3–4; see
  [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).
- *Mixing layer.* EnKF-MM is best in momentum-thickness growth through
  transition and linear growth, spectra, kinetic energy and the Reynolds
  shear stress; all models give a reasonable mean velocity (Figs. 12–16).
- *Generalization (App. A–B).* The coefficient calibrated at
  $Re_\lambda\approx160$ with a Gaussian filter also gives the best
  results with a top-hat filter (same second moment), at
  $Re_\lambda\approx259$ with filter widths of 16 and 32 DNS spacings,
  and in decaying turbulence; the pure gradient model diverges at
  $Re_\lambda\approx259$ with the narrower filter. The authors state that
  flows of "significantly different" configuration need recalibration
  (§II.B); the mixing layer was recalibrated.
- *Functional part alone (App. C).* Calibrating a pure Smagorinsky-type
  model the same way (EnKF-FM) gives $C_{\mathrm f}=0.01$, about 36% above
  the mixed-model value; it reproduces the spectrum except at high
  wavenumbers but is worse than EnKF-MM in strain and rotation PDFs and
  the worst of all models in the SGS energy flux.

## Qualifications

- **One parameter.** The LES application calibrates a single constant
  against spectra; the dimension that, by the authors' argument, favours
  the EnKF over finite differences is not exercised (§V). Applying it to
  wall-bounded LES "still needs further adjustments of EnKF and
  improvements for computational efficiency" (§VI).
- **Local minima.** The authors state, citing Evensen, that the EnKF
  "does not to the same degree suffer from" local minima as traditional
  parameter estimation (§IV); the paper shows no comparison with a
  gradient-based calibration, and the mixing layer needed the shifting
  step to converge (§IV).
- **Noise.** The observation noise is set at $10^{-7}$ (§III, Tables II,
  IV); no calibration against noisier data is shown.
- **Printed slips (arXiv v3).** The momentum-thickness integral (Eq. 24)
  runs over $-L_2/4$ to $L_2/4$ while the profile (Eq. 23) is defined on
  $(0,L_2]$ and centred at $L_2/2$; $\Delta U$ is written with averaging
  brackets although it is a constant. The abstract speaks of "model
  coefficients" while only one is determined.
- **Notation.** The paper writes the coefficient as $C_D$, which the registry keeps for the drag coefficient,
  and orders the mixing-layer coordinates spanwise, normal, streamwise.

# Citations

- [Wang et al. (2023c)](/sources/wang-2023-c.md) — arXiv v3: §I; §II.A, Eqs. 11–14 (mixed model); §II.B, Eqs. 15–20, Fig. 1 (EnKF loop); §III, Tables I–II, Figs. 2–9 (isotropic turbulence); §IV, Eqs. 23–27, Tables III–IV, Figs. 11–17 (mixing layer, shifting, inflation); §V–VI; Apps. A–C, Figs. 18–24.
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §5.1 (ensemble Kalman methods as field-inversion solvers).
- [Yan et al. (2022)](/sources/yan-2022.md) — accepted manuscript, §1 (MCMC and EnKF for the full posterior; MAP as field inversion).
- [Fanizza et al. (2025)](/sources/fanizza-2025.md) — §1 (ensemble Kalman methods named as alternative to variational assimilation).
- [Zhao et al. (2025)](/sources/zhao-2025.md) — arXiv v3: §4, Eqs. 25–26, Table 4 (gradient-based learning of the Smagorinsky coefficient, ensemble assimilation cited as motivation).
