---
type: Method
title: "Reinforcement-learning turbulence closures"
description: "Closure parameters chosen online by a policy trained with reinforcement learning, with the running LES as the environment and a reward computed from solver statistics; element-local SGS coefficients and DG/FV blending in DG-LES, and a multi-agent wall-stress model in WMLES."
status: established
aliases: [RL closure, reinforcement-learning SGS model, multi-agent reinforcement learning wall model, MARL wall model, RL-Const, RL-Quad, RL-Blend]
tags: [reinforcement-learning, sgs-model, data-driven, implicit-les, wall-model]
timestamp: 2026-10-25T13:43:00Z
---

# Reinforcement-learning turbulence closures

A **reinforcement-learning (RL) closure** lets a trained policy set the
free parameters of a turbulence model while the simulation runs. The
problem is posed as a Markov decision process (Beck & Kurz 2023, §II B).
At each action interval the agent observes a state $s_t$ taken from the
resolved flow and applies an action $a_t$, such as a model coefficient or
a blending factor. The LES advances, and the agent receives a reward
$r_{t+1}$ that measures how close the simulation statistics are to a
target. The policy $\pi_{\boldsymbol\theta}(a_t\mid s_t)$ is a neural
network whose parameters are trained to maximize the expected cumulative
reward.

The LES itself, with its actual discretization, is the environment. RL
therefore optimizes the closure a posteriori, in the loop with the LES
operator (Beck & Kurz 2023, §I), without gradients of the solver. This
places it in the class that Duraisamy (2021, §IV.B) calls
[model-consistent training](/methods/model-consistent-training.md), as a
gradient-free, adjoint-free member; that review names RL only as a
flow-control application (§I) and does not discuss RL closures. Beck &
Kurz (2023) use it for SGS models in discontinuous Galerkin LES. Vadrot et
al. (2023b) assess a published RL wall model.

## SGS closures for DG-LES (Beck & Kurz 2023)

**Motivation.** The discrete operator of an implicitly filtered LES adds a
solution-dependent closure term that cannot be determined a priori.
Optimizing the closure segregated from the solver "is not constructive"
(§I; see
[discretization-consistent closure](/definitions/discretization-consistent-closure.md)).
RL is their instrument for optimizing in the loop.

**Baseline scheme.** The
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) of
[FLEXI](/software/flexi.md) on LGL nodes, in split form, with an L2-Roe
flux and BR1 lifting (§III A). The Relexi framework couples FLEXI to the
agent on HPC. Each DG element receives its own action.

**Three closures (§III B–C, Eqs. 12–17).**

| Model | Action per element | Range of the sampled action (Table I) |
|---|---|---|
| RL-Const | constant [Smagorinsky](/methods/smagorinsky-model.md) coefficient $C_s$ | $[0,0.5]$ |
| RL-Quad | $C_s(\xi)$ built from the zeroth and second Legendre modes (a "shifted hyperparaboloid"), clipped at zero at the nodes | constant part $[0,0.5]$, quadratic part $[-0.25,0.25]$ |
| RL-Blend | blending factor $\alpha$ of the hybrid DG/finite-volume subcell scheme, used as an implicit model | $[0,0.5]$ |

- **Explicit models.** The eddy viscosity is $\nu_t=(C_s\Delta)^2|\bar S|$
  with $\Delta=\sqrt[3]{V_e}/(N+1)$, where $V_e$ is the element volume
  (page-local). The authors stress that this filter-width definition is
  not unique (Eq. 11).
- **RL-Blend.** The semi-discrete operator is
  $(1-\alpha)R_{\mathrm{DG}}+\alpha R_{\mathrm{FV}}$, with $\alpha=1$ pure
  finite volume (Eq. 16; Hennemann et al., see
  [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)).
  The authors state that this scheme had "not been interpreted as a
  possible implicit SGS model alternative yet" (§V C).

**Agent (§IV B).**

- *Algorithm.* Proximal policy optimization (PPO).
- *Policy network.* Five 3D-convolution layers with ReLU, about 3300
  parameters; its input is the element-local solution.
- *Action distribution.* The network outputs the two parameters of a beta
  distribution per action, passed through softplus plus one so that both
  exceed one. The beta distribution replaces the Gaussian of earlier work
  because it "has shown to accelerate the training".
- *Reward.* Built from the normalized squared error of the LES
  kinetic-energy spectrum $E(k)$ against the time-averaged DNS spectrum,
  summed up to $k_{\max}=9$ (24 DOF per direction) or 11 (36 DOF), with a
  scaling constant 0.4 (Eq. 18); see Qualifications for its sign.
- *Training settings.* Episodes of 5 time units (about 7 large-eddy
  turnovers), an action every 0.1 time units (50 per episode), 16 parallel
  episodes per iteration, 5 epochs per iteration, Adam with learning rate
  $10^{-4}$, 2000 iterations.
- *Evaluation.* The policy is evaluated greedily (most probable action)
  and trained stochastically. The authors attribute the higher evaluation
  rewards mainly to this difference (§V A, Fig. 7).

**Test.** Forced
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
at $Re_\lambda\approx180$ (§IV A). The DNS uses $N=7$ on $64^3$ elements
(512 points per direction). The LES use 24 or 36 DOF per direction with
$N=3$, 5 and 8, initialized from filtered DNS.

**Results (§V).**

- **Comparison with baselines.** The baselines are no-model LES, static
  Smagorinsky with $C_s=0.17$, and the [dynamic procedure](/methods/dynamic-procedure.md).
  The RL models outperform the dynamic model for $N=5$ and $N=8$. For
  $N=3$, no-model LES is best and the RL models do not reach it; there the
  agent's skewed $C_s$ distribution mimics $C_s=0$ (Figs. 8, 10). No
  reference model is best for every $N$. The authors read this as support
  for optimizing closure and discretization jointly.
- **RL-Quad against RL-Const.** RL-Quad collects more reward than
  RL-Const, and the gap grows with $N$. RL-Const at $N=8$ does not
  converge in 2000 iterations.
- **Learned coefficient.** The time-averaged RL-Quad coefficient is a
  parabola, largest at the element centre and near zero at the faces
  (Fig. 11). The authors interpret this as compensating the DG numerical
  dissipation, which acts only through the face fluxes, and flag the
  interpretation as needing investigation (see
  [numerical dissipation](/properties/numerical-dissipation.md)).
- **No test filter needed.** The policies find a suitable $C_s$ from the
  resolved field alone, without a scale-similarity assumption or a
  test-filtered solution (§V B).
- **RL-Blend.** Pure DG ($\alpha=0$) is under-dissipative and pure finite
  volume ($\alpha=1$) over-dissipative. The RL-chosen blend matches the DNS
  spectrum at 36 DOF and $N=5$ (Fig. 12), with rewards comparable to the
  explicit RL models. The authors explain this by where each scheme
  dissipates: finite-volume subcell dissipation is concentrated at the
  element centre, DG dissipation at the faces (§V C, Fig. 4).
- **Deformed mesh.** On a sinusoidally deformed mesh (App. A), the
  Cartesian-trained RL-Quad, without retraining, performs comparably to
  the dynamic model. RL-Const loses energy at wavenumbers 2–6.

## RL wall model in WMLES (as assessed by Vadrot et al. 2023b)

Vadrot et al. (2023b, §II B 4) implement in [LESGO](/software/lesgo.md)
the log-law variant of the multi-agent RL wall model of Bae &
Koumoutsakos (2022), and compare it with an
[equilibrium wall model](/methods/equilibrium-wall-model.md).

**Model.** Agents sit in a wall-parallel plane at the matching height.
Each agent multiplies its local wall stress at every action instant:
$\tau_w(t_{n+1})=a_n\tau_w(t_n)$, with $a_n\in[0.9,1.1]$ (Eq. 7).

**States (Eq. 8).** Two log-law fit parameters computed at
$h_{\mathrm{wm}}$ from the LES velocity and its wall-normal derivative:
a local inverse slope $1/\kappa_{\mathrm{wm}}$ and an intercept
$B_{\mathrm{wm}}$ (page-local names, mirroring $\kappa$ and $B$).

**Training.** As recalled there, the model was trained in WMLES at
$Re_\tau=2000$, 4200 and 8000, from fields generated with the equilibrium
model and without high-fidelity data, at about $10^7$ gradient steps
(§IV D). The reward is not stated in this paper.

**Findings in half-channel flow from $Re_\tau=180$ to $10^{10}$ (§III,
§IV C, Table III).**

- **Log-layer mismatch.** The model gives the log law with a
  [log-layer mismatch](/definitions/log-layer-mismatch.md) of $+2.2$ inner
  units at $Re_\tau=180$, $+1.0$ to $+2.0$ from $10^3$ to $10^5$, and
  $-0.9$ to $-3.2$ from $10^6$ to $10^{10}$. It is best near
  $Re_\tau=10^5$, where the inner-scaled matching height is close to
  training conditions.
- **Source of the mismatch.** The authors trace it to a mismatch between
  two lines in the state plane: the neutral line, on which the LES velocity
  equals the log law, moves with $Re_\tau$ and with the grid; the line
  separating actions $a_n>1$ from $a_n<1$ does not. Classification accuracy
  is about 0.5 at all $Re_\tau$, and the mismatch correlates with the
  precision of the actions, not with accuracy or recall (Eqs. 10–14).
- **Agents and grid.** The number of agents (16, 64, 128) has negligible
  effect, except that 16 agents fail to converge for $Re_\tau>10^9$. The
  grid dependence is weak (Figs. 8–10).
- **Cost.** About 17 412 operations per evaluation (one agent per grid
  point), against 5 for the algebraic equilibrium model. The measured cost
  ratio of the ODE-based equilibrium model to the RL model is about four,
  from a rough timing (§IV D). The model needs the RL library coupled at
  run time.

See [machine-learning wall models](/methods/machine-learning-wall-model.md)
for the supervised models compared in the same study.

## Qualifications

- **Reward sign in Beck & Kurz (2023, Eq. 18).** The reward is printed as
  $$r=2\exp\!\left(\frac{\beta}{k_{\max}}\sum_{k=1}^{k_{\max}}\left(\frac{\overline E_{DNS}(k)-E_{LES}(k)}{\overline E_{DNS}(k)}\right)^2\right)-1,$$
  with $\beta=0.4$ (page-local, the paper's reward scaling, not the
  field-inversion $\beta(\boldsymbol x)$) and the overbar a time average,
  not the LES filter; it is stated to be normalized to $[-1,1]$. With a
  non-negative sum and a positive exponent, the printed form gives
  $r\ge1$; a negative exponent gives $r\in(-1,1]$ with $r=1$ at zero
  error, which matches the stated range *(compiler check, not in the
  sources)*.
- **No-model LES is not "implicit LES" there.** Beck & Kurz (2023, §V)
  label the baseline-scheme-only LES "no-model LES", to separate it from
  implicit modelling proper such as RL-Blend (see
  [implicit LES](/definitions/implicit-les.md)).
- **Generalization.** Beck & Kurz (2023, §VI) leave generalizability,
  interpretability and uncertainty as open challenges, and propose
  transfer learning and meta-RL to cut training cost. Vadrot et al. (2023b,
  §III A) obtain results "slightly different" from the original RL
  wall-model paper, "mainly because of the difference in the grid
  resolution". They set the log-layer mismatch they find away from the
  training conditions against the original authors' claim of
  "extrapolation to unseen Reynolds numbers" (§III A).

# Citations

- [Beck & Kurz (2023)](/sources/beck-2023.md) — §I (motivation), §II B (MDP, PPO), §III B–C, Eqs. 11–17, Table I, §IV A–B, Eq. 18, §V A–C, Figs. 7–14, App. A, §VI.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II B 4, Eqs. 7–8; §III A–B, Figs. 8–10; §IV C, Eqs. 10–14, Table III; §IV D.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §IV.B (model-consistent training as the class to which in-the-loop optimization belongs).
