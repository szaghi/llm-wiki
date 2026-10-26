---
type: Method
title: "Building-block-flow wall model"
description: "Supervised wall-stress model for wall-modelled LES that classifies the local near-wall state among seven canonical building-block flows and blends per-flow neural-network predictions by the class probabilities, trained on solver-consistent WMLES data, with a confidence score, and tested from laminar plates to the CRM-HL and the NASA Juncture Flow."
status: established
aliases: [BFWM, building-block flow wall model, machine-learning building-block-flow wall model]
tags: [wall-model, wmles, machine-learning, neural-network, data-driven]
timestamp: 2026-10-26T07:39:00Z
---

# Building-block-flow wall model

The building-block-flow wall model (BFWM) of [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md)
is a [machine-learning wall model](/methods/machine-learning-wall-model.md) for
[wall-modelled LES](/methods/wall-modelled-les.md). It rests on two stated
assumptions (§2.2): a finite set of simple canonical flows (the "building
blocks") contains the near-wall physics needed to predict the wall shear
stress $\tau_w$ in complex flows, and the effect of the missing near-wall
scales of a complex flow is a linear, probability-weighted combination of the
near-wall behaviour of the building blocks. A neural-network classifier
estimates, at every wall point, the probability that the local LES state
belongs to each building block; one predictor per block returns a wall stress;
the model output is the probability-weighted sum, accompanied by a confidence
score. A preliminary version was introduced by the same authors in 2020 (as
they cite it); the version of record read here supersedes it with a two-point
stencil, more building blocks and solver-consistent training data (§2.2,
§4.8).

## Requirements and assumptions

The authors list eight requirements (§2.1): one input/output format for all
flow physics; scalability to more building blocks; a confidence score at each
wall point; inputs local in space, so that the model applies to complex
geometries; training data consistent with the numerical errors of the LES
solver rather than filtered DNS; non-dimensional inputs and outputs;
invariance under constant translations and rotations of the frame; Galilean
invariance. Besides the two assumptions above, they assume (§2.2) that as many
non-dimensional local inputs as the minimum number of parameters
characterizing the collection (six here) suffice to discern the blocks; that
the kinematic viscosity and the wall distance give the best
non-dimensionalization (not for strong compressibility, reacting or multiphase
flows); that two contiguous wall-normal points suffice — the seven-point
stencil of the preliminary version "greatly complicated the model
implementation without providing important benefits"; and that history
effects enter only through instantaneous accelerations.

## Building blocks

Seven blocks, all incompressible flows between parallel walls $2\delta$ apart ($\delta$ the channel half-height; the source's $h$)
except the free stream (§2.3, Figs. 2–3; page-local $Re_P$, $Re_U$, $G_{zx}$):

| Block | Flow | Parameters and trained range |
|---|---|---|
| Free stream | uniform velocity | marks wall regions with no points per boundary-layer thickness; the zero-pressure-gradient predictor is then applied with low confidence |
| Laminar | Poiseuille flow | $Re_\tau=5$–$10^4$; wall stress from the analytical parabolic profile |
| Zero pressure gradient (ZPG) | [turbulent channel flow](/benchmarks/turbulent-channel-flow.md) | $Re_\tau=100$–$10\,000$ |
| Favourable, adverse pressure gradient (FPG, APG), separation | turbulent Poiseuille–Couette flow, bottom wall at rest, top wall at $U_t$ | $Re_P=\pm\sqrt{\lvert dP/dx\rvert/\rho}\,\delta/\nu$ from $-1.2\times10^3$ to $1.2\times10^3$ (sign $+$ for FPG), $Re_U=U_t\delta/\nu$ from $5\times10^3$ to $2\times10^4$; separation where the bottom-wall stress vanishes |
| Unsteady | channel with a sudden spanwise mean pressure gradient, initial transient only | $Re_\tau=100$–$1000$ before the gradient is imposed, $G_{zx}=(dP/dz)/(dP/dx)=5$–$100$ |

The Poiseuille–Couette family passes continuously from FPG through ZPG and APG
to separation by changing only the pressure gradient, which the authors credit
with filling the input space. The DNS database for the turbulent blocks holds
roughly 500 simulations, partly new and partly from earlier works they cite
(§2.3). Aerofoils, wings and bumps are excluded on purpose, to avoid
over-fitting to cases: the model "has never 'seen' an aircraft-like flow"
(§2.3, §4.7).

## Inputs and outputs

The stencil is the centre of the wall-attached control volume (index 1, where
$\tau_w$ is predicted) and the second control volume along the wall normal
(index 2); the two centres need not be aligned (§2.4). With $u_1$, $u_2$ the
magnitudes of the wall-parallel velocity relative to the wall at the two
points, $y_1$, $y_2$ their wall distances, $\varphi_{12}$ the angle between
the two velocity vectors, $\mathcal A_1$ the magnitude of the acceleration and
$\dot\varphi_1$ the rate of change of the direction of $\boldsymbol u_1$ at
point 1, and $k_1$, $k_{m1}$ the turbulent and mean kinetic energy at point 1
relative to the wall (all page-local; the source writes $\gamma_{12}$, $a_1$,
$\dot\gamma_1$), the six non-dimensional inputs are (Eq. 2.3)

$$\left\{\frac{u_1y_1}{\nu},\ \frac{u_2y_2}{\nu},\ \varphi_{12},\ \frac{\mathcal A_1y_1^3}{\nu^2},\ \frac{\dot\varphi_1y_1^2}{\nu},\ \frac{k_1}{k_{m1}}\right\}.$$

The two local Reynolds numbers detect the shape of the mean profile (channel,
pressure gradient, separation), $\varphi_{12}$ mean three-dimensionality, the
acceleration and angular rate unsteadiness in magnitude and direction, and
$k_1/k_{m1}$ separates turbulent from laminar or free-stream states. The
free-stream and bulk velocities are avoided because they cannot be identified
in an arbitrary geometry. The mean velocity entering $k_1$ and $k_{m1}$ is an
exponential time average with time scale $10\Delta/\sqrt{k_{m1}}$, $\Delta$
the cube root of the control volume, and the same average is applied to the
inputs (accounted for in training).

The outputs (Eqs. 2.2, 2.4) are the wall-stress magnitude scaled by the
pseudo-wall-stress $\mu\check u_1/y_1$ ($\check u_1$ the exponentially averaged
$u_1$; page-local, the source's overbar), the angle $\varphi_{1w}$ between
$\boldsymbol u_1$ and $\boldsymbol\tau_w$, the class probabilities
$p_i\in[0,1]$, $i=1,\dots,7$, and the confidence $p_{\mathrm{conf}}\in[0,1]$.
The scaling by $\mu\check u_1/y_1$ was chosen because it minimized the spread
of the data between cases.

## Classifier, predictors and confidence

- **Classifier** (§2.6): a feed-forward network of 5 hidden layers of 20
  neurons, ReLU, softmax output with $\sum_ip_i=1$, trained by cross-entropy
  on the whole training database independently of the predictors.
- **Predictors** (§2.6, Fig. 6): one network per turbulent block (ZPG, APG,
  FPG, separation, unsteady), 5 hidden layers of 30 neurons (the activations
  are described as "hyperbolic tangent sigmoid transfer functions and ReLU
  activation transfer functions"); the laminar block uses the analytical
  profile, the free stream the ZPG predictor. The model output is
  (Eq. 2.6)

  $$\frac{\tau_wy_1}{\mu\check u_1}=\sum_ip_i\,\frac{\tau^{(i)}_wy_1}{\mu\check u_1},\qquad \varphi_{1w}=\sum_ip_i\,\varphi^{(i)}_{1w},$$

  with $\tau^{(i)}_w$, $\varphi^{(i)}_{1w}$ the prediction of block $i$.
  Training uses Bayesian-regularization back-propagation with an 80/20 split
  in which the test set holds whole cases at Reynolds numbers and pressure-gradient
  ratios absent from training (found to improve interpolation and
  extrapolation), loss weights compensating unequal snapshot counts, and
  inputs and outputs standardized by the training statistics; layer and
  neuron counts come from a parametric study.
- **Confidence score** (§2.6, Fig. 1): from the ratio $d_s/d_{\mathrm{in}}$,
  clipped below one, with $d_{\mathrm{in}}$ the distance of the input to the
  nearest training sample and $d_s$ the mean distance of that sample to its ten
  nearest training samples (page-local). The map from the ratio to a
  percentage is not given beyond the clipping. The authors stress that the
  score measures similarity to the training data, not error: a
  low-confidence prediction can be accurate and vice versa (§5(2)); see
  [model-form uncertainty](/definitions/model-form-uncertainty.md).

The confusion matrix (Fig. 5) shows most samples classified correctly, with
intentional overlap between contiguous blocks; the one unintentional
misclassification is ZPG samples labelled FPG (column precision 85.2 % for
ZPG and 83.5 % for FPG; free stream and laminar 100 %).

## Training on solver-consistent WMLES data

The training data are not filtered DNS. The authors argue (§2.5, citing
earlier work of theirs and of Lund and Kaltenbach) that in an implicitly
filtered LES — a grid-filtered LES with an explicit SGS model, not
[implicit LES](/definitions/implicit-les.md) without one — the subgrid
tensor does not coincide with the stress obtained by filtering the
Navier–Stokes equations, so data from filtered DNS are inconsistent with
the solver; this is the [discretization-consistent closure](/definitions/discretization-consistent-closure.md)
argument applied to a wall model. They therefore generate data by running
WMLES in the deployment solver, [CharLES](/software/charles.md), with two
devices (Eq. 2.5):

- an **exact-for-the-mean SGS model**,
  $\tau^{\mathrm{ESGS}}_{ij}=\tau^{\mathrm{base}}_{ij}+\Delta\tau_{ij}$, with
  $\tau^{\mathrm{base}}_{ij}$ the [dynamic Smagorinsky](/methods/dynamic-procedure.md)
  stress and $\Delta\tau_{ij}$ a correction whose divergence is computed on
  the fly, at each wall-normal location and time step, as the force that makes
  the plane-averaged LES velocity equal the DNS mean at the next step (the
  source prints no sign or trace convention for these tensors); no
  instantaneous DNS field and no filter shape are needed;
- an **exact boundary condition** that draws the wall stress at each point and
  step from the DNS probability density of $\tau_w$ by inverse transform
  sampling.

WMLES with both (E-WMLES) runs on isotropic grids $\Delta=\delta/n$ with
$n=5,10,20,40,80,160,380$ (page-local $n$); below $\delta/380$ the model is trained
on DNS data so that it converges to no slip. Runs last 10 eddy-turnover times
$\delta/u_\tau$ (reducing to 3 "significantly reduced the performance"; not
shown), the unsteady block only between 0.5 and 2; 1000–10 000 snapshots per
case; data are augmented by rotating the mean-flow direction from $-45°$ to
$45°$ in steps of $5°$ (§2.6). The consequence the authors draw is that the
model must be retrained for every flow solver (§5(3)); the argument is that of
[model-consistent training](/methods/model-consistent-training.md), here
obtained by generating the data in the solver rather than by training through
it.

The two devices are also used in validation: replacing the SGS model by ESGS
removes the error of the LES input, so the remaining error isolates the wall
model ("internal" error), while the full WMLES adds the SGS-model error at the
matching location ("external" error) (§4.1; the split is that of
Lozano-Durán et al. 2022, see the [equilibrium wall model](/methods/equilibrium-wall-model.md)).

## Baseline

The comparison model is the algebraic [equilibrium wall model](/methods/equilibrium-wall-model.md)
(EQWM, Eq. 3.1), $u^+=y^++a_1(y^+)^2$ for $y^+<23$ and
$\kappa^{-1}\ln y^++B$ otherwise, with $\kappa=0.41$, $B=5.2$, $a_1$ from
$C^1$ continuity, adiabatic walls, and the input taken at the **second** grid
point off the wall. The SGS models are dynamic Smagorinsky with Lilly's
modification (DSM) and the [Vreman model](/methods/vreman-model.md) (§3.2).

## A posteriori evidence

All tests run the model inside CharLES (§4):

| Case | Conditions | Finding |
|---|---|---|
| Laminar (Blasius) boundary layer | $U_\infty L_0/\nu=10^4$–$10^6$, two points per thickness at the inlet, twenty at the outlet | classified laminar with confidence near 100 % except near the inlet (free stream, lower confidence); internal BFWM error below 1 % after the inflow transient, EQWM above 20 %; mean velocity within 5 % for all four DSM/Vreman × EQWM/BFWM combinations, the EQWM cases helped by cancellation of internal and external errors, the BFWM limited by external errors (§4.2, Fig. 8) |
| [Turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md), zero pressure gradient | $Re_\theta=800$–2000, DNS of the same set-up | classified ZPG with almost 100 % confidence over most of the domain, unsteady/APG near the inlet with confidence falling from 40 % to 20 %; mean internal wall-stress error below 0.5 % (BFWM) against about 2 % (EQWM); total errors 5–15 % for both (§4.3, Fig. 9) |
| Pipe flow | $Re_\tau\approx40\,000$ against experiment; grids $\Delta/R=1/5$–$1/40$ ($R$ the radius) | classified ZPG on all grids, confidence above 95 % for $R/\Delta>5$, below 60 % at $R/\Delta\approx5$ (attributed to the low near-wall shear given by DSM); internal errors below 5 % for both models even on the coarsest grid; total errors 4–12 %, mildly better with BFWM; non-monotonic grid convergence (§4.4, Fig. 10) |
| Poiseuille–Couette, APG and separation | $Re_U=14\,000$, $Re_P\times10^{-3}=-1.40$ to $-0.76$, $\delta/\Delta=10$ | classification confidence above 90 %; BFWM better in internal error; in total error EQWM is more accurate "for the wrong reasons": it under-predicts $\tau_w$ while the near-wall mean velocity is over-predicted (§4.5, Fig. 11) |
| Poiseuille–Couette, FPG | $Re_U=14\,000$, $Re_P\times10^{-3}=1.02$–$1.49$, $\delta/\Delta=10$ | total error rises from 5 % to 20 % with the favourable gradient for both models, BFWM better (§4.5, Fig. 12) |
| Channel with sudden spanwise pressure gradient | $G_{zx}=80$ from a channel at $Re_\tau=700$, $\delta/\Delta=10$ | change ZPG→unsteady detected at $t=0$ with high confidence; BFWM internal errors below 1 % at all times; it predicts the mild drop of the streamwise wall stress and the rise and fall of $\varphi_{1w}$, which EQWM misses ($\varphi_{1w}=0$ by construction) (§4.6, Fig. 13) |
| NASA CRM-HL (high-lift aircraft) | $Re=5.49\times10^6$ on the mean aerodynamic chord, $M_\infty=0.20$, 30 M points, 0–20 points per boundary-layer thickness, DSM, angles of attack 7° and 19° | moderate improvement of DSM-BFWM over DSM-EQWM, especially near stall and most clearly in pitching moment; at low incidence DSM-EQWM gives the better $C_L$, attributed to error cancellation ("it has been reported", no citation); confidence below 20 % at the leading edges of nacelle, slats and flaps (no points per thickness) and in separation at the wing tip and near the root; random inputs give 0 % (§4.7, Figs. 15–16) |
| [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md) | $Re=2.4\times10^6$, 5°, [boundary-layer-conforming grid](/methods/boundary-layer-conforming-grid.md) with 5 points per $\delta$, DSM | upstream fuselage: 88 % ZPG, 12 % FPG, confidence 98 %, errors below 2 % for both models; wing–body juncture: 52 % APG, 41 % ZPG, 7 % separation, confidence 82 %, BFWM better through the larger wall stress that decelerates the flow; trailing-edge corner separation: 56 % separation, confidence 22 %, BFWM better but "far from satisfactory" — the bubble is $0.3\delta$ thick on a grid of $\Delta\approx0.2\delta$ (Table 1, §4.8, Fig. 18) |

The present model is said to be more accurate on the Juncture Flow than the
preliminary version trained on filtered DNS; no side-by-side data are shown
(§4.8). [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) (§I) recall the
classifier-plus-predictor model of Lozano-Durán & Bae as poor in the
separation zones of the Juncture Flow, citing the 2020 arXiv preprint of the
preliminary version (their ref. [85]), not the version of record read here.

## The authors' conclusion: external errors dominate

Across the cases the BFWM reduces the internal error markedly, but the total
error is controlled by the external error that the SGS model makes at the
matching location (§4.7, §5(4), §6): "a superior wall model alone does not
suffice" unless the SGS model improves too. This agrees with the error
propagation of [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md)
(§IV.C), for whom wall models are more resilient to internal than to external
errors. The authors point to the extension of the building-block method to
the SGS model by Ling et al. (2022), which they report greatly improved the
CRM-HL lift, drag and moment (as they cite it). They also conclude that the
performance is controlled mainly by the physical assumptions, not by the
network architecture, the chosen networks being accurate "but may be far from
optimal" (§5(5), §6).

## Cost

Each network took about 12 h to train on four A100 GPUs (40 GB); WMLES with
the BFWM costs 1.1–1.3 times the same solver with the algebraic equilibrium
model, without optimization of the implementation (§2.6).

## Qualifications

- No mechanism for laminar–turbulent transition is included (§5(1)); the
  building blocks exclude compressibility and heat transfer, which the
  authors list among the sources of internal error (§4.1).
- **Printed ranges.** The stated trained range of the Poiseuille–Couette
  blocks is $Re_P$ from $-1.2\times10^3$ to $1.2\times10^3$ and $Re_U$ from
  $5\times10^3$ to $2\times10^4$ (§2.3); the Fig. 3(b,c) captions show
  building-block DNS at $Re_U=22\,360$, and the §4.5 validation uses $Re_P$
  down to $-1.40\times10^3$ and up to $1.49\times10^3$. The paper does not
  comment on either.
- **Printed slips in the version of record.** §2.3 calls
  $(dP/dz)/(dP/dx)$ "the ratio of streamwise to spanwise mean pressure
  gradients", while the formula and §4.6 give spanwise over streamwise;
  §4.5 refers to "§ 2.5" for the training and test sets, which are described
  in §2.6; §4.5 states that "ZPG cases are all predicted accurately by both
  wall models, with errors below 3 %" in a section that contains only APG,
  separation and FPG cases, so the case meant is not identifiable; the
  requirement list of §2.1 numbers its third item "(ii)"; the source uses
  $a_1$ both for the acceleration input and for the coefficient of the
  equilibrium profile.
- The invariance requirements (vii)–(viii) are stated; the paper gives no
  separate argument that the six inputs satisfy them beyond their being
  magnitudes and angles relative to the wall.

# Citations

- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §1; §2.1–2.6, Eqs. (2.1)–(2.6), Figs. 1–7; §3.1–3.2, Eq. (3.1); §4.1–4.8, Figs. 8–18, Table 1; §5; §6.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §IV.C.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §I.
