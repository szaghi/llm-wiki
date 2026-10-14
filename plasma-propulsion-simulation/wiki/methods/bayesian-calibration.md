---
type: Method
title: "Bayesian calibration of thruster models"
description: "Inference of the free parameters of a reduced thruster model (anomalous-transport coefficients, neutral speed, loss and facility parameters) as a posterior distribution conditioned on measured or synthetic data, sampled by MCMC or nested sampling, often through a surrogate; it exposes non-identifiable parameters and residual model-form error that manual tuning hides."
status: established
aliases: [Bayesian inference of model parameters, Bayesian model calibration, probabilistic calibration, uncertainty quantification of thruster models]
tags: [calibration, uq, hall-thruster, fluid, anomalous-transport, verification]
timestamp: 2026-10-14T00:00:00Z
---

# Bayesian calibration of thruster models

Reduced Hall-thruster models, such as the
[one-dimensional fluid model](/methods/one-dimensional-fluid-hall-model.md),
carry free parameters that physics does not fix, above all the
[anomalous-transport](/definitions/anomalous-electron-transport.md)
coefficient profile $\alpha_{\mathrm B}(z)$. Bayesian calibration treats
the parameter vector $\boldsymbol\vartheta$ as uncertain and computes the
posterior
$$\pi(\boldsymbol\vartheta\mid\mathbf d)\propto\mathcal L(\boldsymbol\vartheta)\,\pi(\boldsymbol\vartheta)$$
from a prior and a likelihood of the data $\mathbf d$
([Saravia et al. (2026)](/sources/saravia-2026.md), §4.1, eq. 22;
[Eckels et al. (2024)](/sources/eckels-2024.md), eqs. 10–11). The result
is a distribution, so it shows which parameters the data constrain and
which they do not.

## Contrast: manual calibration

[Giannetti et al. (2021)](/sources/giannetti-2021.md), §4, calibrate three
parameters of a 1D fluid model by hand against the discharge-current
signal of the HT5k thruster (mean, minimum, maximum, RMS and breathing
frequency): the neutral speed (395 m/s), a wall-interaction scaling
coefficient (0.115) and a two-level $\alpha_{\mathrm B}$ (0.075 in the
channel, 7.5 in the plume). They report qualitative sensitivities (the
neutral speed sets the frequency, the wall coefficient the amplitude, the
in-channel $\alpha_{\mathrm B}$ both mean and amplitude) but no
uncertainty. Earlier deterministic routes are reported by
[Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §§2.4–2.5:
fitted Bohm coefficients (Hagelaar et al. 2002; Ahedo et al. 2003; Koo &
Boyd 2004), a cross-field mobility profile adjusted to LIF ion velocities
(Garrigues et al. 2009), and a genetic-algorithm regression of the
anomalous frequency on data (Jorns 2018). They add that tuning anomalous
coefficients to match erosion does not guarantee matching current or
performance (Cheng & Martinez-Sanchez, §2.7).

## Set-ups

| | [Eckels et al. (2024)](/sources/eckels-2024.md) | [Saravia et al. (2026)](/sources/saravia-2026.md) |
|---|---|---|
| model | coupled cathode (semi-empirical) – thruster (HallThruster.jl, 1D multi-fluid) – plume (semi-empirical) | 1D fluid model of [LANDMARK test case 3](/methods/one-dimensional-fluid-hall-model.md) |
| parameters | 17 (cathode, thruster, plume), of 22 inputs | 4: neutral injection speed, anomalous energy-loss coefficient, in-channel and plume $\alpha_{\mathrm B}$ |
| data | SPT-100 literature data at several background pressures: cathode coupling voltage, thrust, $I_d$, LIF ion velocity, plume ion current density | synthetic: noisy $I_d(t)$ (noise s.d. 0.1 A), thrust 103 mN, plume $T_e$ 14.2 eV at $z=\tfrac32L_{\mathrm{ch}}$ |
| likelihood | Gaussian, experimental error bars read as s.d. = 1/4 of the error range; $I_d$ ±10 % assumed | Gaussian for thrust (s.d. 5 mN) and $T_e$ (20 %); Wasserstein likelihood for $I_d(t)$ |
| prior | domains of Table 1 | independent uniforms, plus in-channel $\alpha_{\mathrm B}$ < plume $\alpha_{\mathrm B}$ |
| sampler | DRAM MCMC, 100,000 iterations, 10 % burn-in, acceptance 22 % | nested sampling (UltraNest 4.3.3), 120 live points, stop at 1 % remaining posterior volume |
| model evaluations | through a surrogate (below) | direct; tens of thousands of runs in under 100 h on up to 280 cores |

Sources: [Eckels et al. (2024)](/sources/eckels-2024.md), Tables 1, 3,
App. C, p. 13; [Saravia et al. (2026)](/sources/saravia-2026.md), §§2.3,
4.1–4.2, Tables 1–2.

**Calibrated anomalous coefficients.** Eckels et al. write
$\nu_{\mathrm{ano}}$ as a coefficient times $\omega_{ce}$ in the channel
and that coefficient times a ratio downstream (eq. 5); their posterior
medians (Table 3: log$_{10}$ of the coefficient $-2.167$, ratio 14.6)
convert to $\alpha_{\mathrm B}\approx0.11$ in the channel and about 1.6
downstream (computed here). Saravia et al.'s reference values are 0.1 and
1.0 (Table 1).

## Likelihood for a time signal

An oscillating $I_d(t)$ cannot be compared pointwise, because model and
data are out of phase. [Saravia et al. (2026)](/sources/saravia-2026.md),
§4.1.2, eq. 27, following Greve et al. (2019), build a likelihood
"analog to the Normal distribution" in which the Euclidean misfit is
replaced by the squared quadratic Wasserstein (earth mover's) distance
between two-dimensional probability densities of the time-lagged phase
portrait (the signal against itself delayed by a fixed lag, histogrammed
on 50×50 bins). The lag used for the Hall case is not stated. The
likelihoods of the separate data are multiplied, all from one model run
per sample ("one-step data fusion", eq. 19). The method was first checked
on the Lorenz system, calibrating all three parameters at once from a
noisy reference: the medians of the Rayleigh-number and geometric
parameters match the reference closely, while the marginal of the
Prandtl-number parameter is nearly flat, which the authors attribute to
the attractor's critical points not depending on it (§5, Tables 3–4).

**The likelihood width.** Treating the width of the current likelihood as
a nuisance parameter with a Jeffreys prior on $[10^{-3},10^{2}]$ makes the
posteriors nearly flat, with medians near the prior mid-range: the width
"overwhelms" the physical parameters (§6.1, Table 5, App. B). The authors
fix it to 1, chosen because the Wasserstein distance scales with the
variance of Gaussian noise added to the reference, and call its
prescription an open problem.

## Identifiability

* **Current-only data.** With $I_d(t)$ alone, the medians of the neutral
  speed, the energy-loss coefficient and the in-channel $\alpha_{\mathrm B}$
  fall within 10 % of their reference values, but the plume
  $\alpha_{\mathrm B}$ stays flat at $3.50^{+1.74}_{-1.68}$ against a
  reference of 1.0, and the neutral speed is multimodal
  ([Saravia et al. (2026)](/sources/saravia-2026.md), §6.2, Table 5).
  Two posterior samples with very different parameters both reproduce the
  current by "typical fitting criteria" while missing thrust and plume
  $T_e$ (§6.3.3, Table 7).
* **Data fusion.** Adding thrust and plume $T_e$ removes the multimodality
  and recovers the plume $\alpha_{\mathrm B}$ as $1.57^{+1.78}_{-0.67}$
  (57 % error against 250 % with current only); the predicted thrust is
  $101.36^{+2.22}_{-3.27}$ mN (reference 103) and plume $T_e$
  $12.14^{+2.84}_{-2.91}$ eV (reference 14.2) (§6.2–6.3, Tables 5–6). The
  in-channel $\alpha_{\mathrm B}(z)$ is recovered in every case, the plume
  value only with plume data (§6.3.1, Fig. 9).
* **Over-parameterization.** In Eckels et al. the displacement parameter
  of the pressure-shifted anomalous-transport transition collapses onto
  its prior bound (0.4), and four parameters sit at prior boundaries
  ([Eckels et al. (2024)](/sources/eckels-2024.md), Table 3, Remarks
  1–4). The paper reads the collapse both as over-parameterization and as
  a truncation by the prior bound; the two readings are recorded on the
  Source page.

*Compiler note, not a source claim:* the plume coefficient that Saravia et
al. find unidentifiable from the current is the one Giannetti et al.
fixed at 7.5 from current data alone; Saravia et al.'s data are synthetic
and come from a different thruster model, so this is a qualification of
the manual calibration, not a refutation of its value.

## Model-form error

[Eckels et al. (2024)](/sources/eckels-2024.md) find that after
calibration the posterior standard deviation of the error is below about
0.3 % for every output while the errors themselves stay large (Table 4,
p. 22): residual error greatly exceeds the experimental noise and the
remaining parametric uncertainty is negligible, so they attribute the
discrepancy to model-form error. They state that the uncertainty bounds
are overconfident because they omit model-form and surrogate error
(Obs. 2, p. 17), and recommend accounting for both, e.g. with Gaussian
processes (pp. 26–28). The model's wrong thrust trend with background
pressure survives calibration (Obs. 1, Fig. 5).

## Surrogates (multi-index stochastic collocation)

Eckels et al. replace the thruster model by a multifidelity multi-index
stochastic collocation (MISC) surrogate: a combination of Lagrange
interpolants indexed by model fidelity (100, 150 or 200 cells; 1, 2 or 3
ion charge states) and by surrogate fidelity (an odd number of
interpolation points per input, over 12 inputs), with adaptive index sets
(eq. 9, p. 10). Field outputs (ion
velocity profile, plume current density) are compressed by SVD to 4 and 2
latent coefficients at 95 % retained variance (App. B, eq. 34); the field
error splits into interpolation and reconstruction parts (eqs. 13–17).
Many outputs reach a relative $L_2$ test error of 10 % or less for the
cost of about 200 high-fidelity evaluations, and the multifidelity
surrogate beats the single high-fidelity one at equal cost (Fig. 3,
pp. 12–13).

The surrogate can mislead: the posterior lies where the in-channel
coefficient is low and the model's thrust prediction is "discontinuous,
unstable", so the surrogate's thrust error rises from 1 % (prior) to 23 %
(posterior), and the true model's thrust error at the posterior median
worsens from 22 % to 29 % (Obs. 3, p. 17, Table 4) and from 22 % to 30 %
on an independent dataset (Table 5). The surrogate errors fall after
calibration (discharge current from 290 % to 45 %), which is the
"order of magnitude" improvement of the abstract.

[Saravia et al. (2026)](/sources/saravia-2026.md), §7, argue that their
time-resolved likelihood with nested sampling avoids Eckels et al.'s
reliance on steady data and surrogates, and agree with Marks & Jorns
(2023) on the need for time-dependent data. This is a methodological
contrast, not a disagreement on results.

## Sobol' sensitivity analysis

With the surrogate, [Eckels et al. (2024)](/sources/eckels-2024.md),
pp. 24–25, Fig. 12, App. E, Fig. 17, compute first-order and total Sobol'
indices $S_j$, $S_{T,j}$ ($N=5000$, 95 % Monte Carlo confidence
intervals) across background pressure:
* the two anomalous coefficients dominate the variance of thrust and exit
  ion velocity, the in-channel one with $S_{T,j}>0.8$ for exit ion velocity,
  growing with pressure;
* the shifted-transition parameters contribute little, which the authors
  read as over-parameterization;
* uncertainties in background pressure and anode flow are negligible;
* the anode neutral injection speed is "surprisingly" important for
  thrust, growing with pressure through the ingestion term;
* the vacuum coupling voltage dominates the cathode coupling voltage, and
  two plume coefficients dominate the peak plume current density.

## Related statements

[Adamovich et al. (2017)](/sources/adamovich-2017.md), §§17–19, call
verification and validation "even more important" for application-driven
plasma modelling, note that theoretical cross-section data rarely carry
uncertainty estimates, and name sensitivity analysis with error bars as a
tool for validated plasma-chemistry mechanisms.

# Citations

1. [Giannetti et al. (2021)](/sources/giannetti-2021.md), §4.
2. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §§2.4–2.5, 2.7 (accepted manuscript).
3. [Eckels et al. (2024)](/sources/eckels-2024.md), pp. 9–28, eqs. 9–17, 34, Tables 1, 3–5, Figs. 3, 5, 12, 17, Apps. B, C, E.
4. [Saravia et al. (2026)](/sources/saravia-2026.md), §§2.3, 4–7, eqs. 19–27, Tables 1–7, App. B.
5. [Adamovich et al. (2017)](/sources/adamovich-2017.md), §§17–19.
