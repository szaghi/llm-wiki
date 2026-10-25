---
type: Method
title: "Reinforcement-learning turbulence closures"
description: "Closure parameters chosen online by a policy trained with reinforcement learning, with the running LES as the environment and a reward computed from solver statistics; element-local SGS coefficients and DG/FV blending in DG-LES, and multi-agent wall-stress models in WMLES with their training, tests and disputed extrapolation."
status: established
aliases: [RL closure, reinforcement-learning SGS model, multi-agent reinforcement learning wall model, MARL wall model, SciMARL, RL-Const, RL-Quad, RL-Blend, VWM, LLWM]
tags: [reinforcement-learning, sgs-model, data-driven, implicit-les, wall-model]
timestamp: 2026-10-25T19:46:00Z
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
Kurz (2023) use it for SGS models in discontinuous Galerkin LES.
[Bae & Koumoutsakos (2022)](/sources/bae-2022.md) use it, with many
cooperating agents, for wall-stress models in wall-modelled LES, and
Vadrot et al. (2023b) assess one of those wall models in another code.

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

## Multi-agent RL wall models (Bae & Koumoutsakos 2022)

Bae & Koumoutsakos (2022) call their framework scientific multi-agent
reinforcement learning (SciMARL). The version read is the Research Square
preprint v1 (22 June 2021); locators below refer to it. Page-local
notation: $\tau_{w,\mathrm m}$ is the modelled, instantaneous, local wall
stress and $u_{\tau,\mathrm m}=\sqrt{\tau_{w,\mathrm m}/\rho}$ the modelled
friction velocity (subscript $\mathrm m$ as in the registry: from the
model's own solution); $y^+_{\mathrm m}$, $u^+_{\mathrm m}$ are inner units
built on $\nu$ and $u_{\tau,\mathrm m}$ (the paper's superscript $*$, which
here is not the semi-local scaling); $\tau_w$ without subscript is the
true mean wall stress.

**Agents and action (pp. 3–4, Methods pp. 12–13).** Agents sit on the
channel walls every four grid cells in $x$ and $z$; each observes local
states at the matching height $h_{\mathrm{wm}}$ and acts at every time
step of the WMLES by $\tau_{w,\mathrm m}(t_{n+1})=a_n\,\tau_{w,\mathrm m}(t_n)$
with $a_n\in[0.9,1.1]$, which "does not require the model to produce the
exact wall-shear stress". All agents share and update one policy. The
states are scaled with $u_{\tau,\mathrm m}$, so no prior knowledge of the
true $u_\tau$ is needed (Eq. 2).

**Two models.**

- *Velocity-based wall model (VWM):* states $u^+_{\mathrm m}$,
  $\partial u^+_{\mathrm m}/\partial y^+_{\mathrm m}$ and
  $y^+_{\mathrm m}$ at $h_{\mathrm{wm}}$.
- *Log-law-based wall model (LLWM):* states the local log-law slope and
  intercept, $1/\kappa_{\mathrm m}=y^+_{\mathrm m}\,\partial u^+_{\mathrm m}/\partial y^+_{\mathrm m}$
  and $B_{\mathrm m}=u^+_{\mathrm m}-\kappa_{\mathrm m}^{-1}\ln y^+_{\mathrm m}$
  at $h_{\mathrm{wm}}$ (Methods p. 13; Vadrot et al. write
  $1/\kappa_{\mathrm{wm}}$, $B_{\mathrm{wm}}$). These states do not contain
  $y^+_{\mathrm m}$ explicitly, which the authors offer as the reason the
  LLWM extends beyond the trained heights. Evaluating the slope at one of
  the two finite-difference points instead of their midpoint changes the
  wall stress by about 5% (Methods p. 14).

The state–action maps conditioned on positive reward show that both
models learn to raise or lower the wall stress according to whether the
local state lies above or below the
[law of the wall](/definitions/law-of-the-wall.md) with $\kappa=0.41$,
$B=5.2$, without being given those constants (Fig. 2).

**Reward (Eq. 9).** Described as "proportional to the improvement in the
prediction" of $\tau_{w,\mathrm m}$ relative to the true mean $\tau_w$,
plus a bonus of one when the relative error is below 1% (see
Qualifications for the printed sign).

**Algorithm (Methods pp. 11–13).** V-RACER, an off-policy actor-critic
method for continuous actions, with Retrace value estimates and
Remember-and-Forget Experience Replay (ReF-ER), in the smarties library.
Gaussian policy from a network of two hidden layers of 128 units (softsign,
skip connections) initialized near $\mathcal N(1,10^{-4})$; discount factor
0.995; batch 512; replay memory $10^6$; Adam with learning rate $10^{-5}$;
trust-region bound 1.5 and target far-policy fraction 0.05; $10^7$
policy-gradient steps per training run.

**Training (Methods p. 12).** WMLES of
[channel flow](/benchmarks/turbulent-channel-flow.md) at $Re_\tau\approx2000$,
4200 or 8000 (sampled per episode), $\Delta_{x,y,z}\simeq0.05\delta$,
$h_{\mathrm{wm}}$ drawn at random in $[0.075\delta,0.15\delta]$ at each step,
episodes of $2\delta/u_\tau$. Each episode starts from "a previously
obtained WMLES flow field" plus white noise of standard deviation
$0.5u_\tau$, with the initial wall stress off by up to $\pm20\%$. The
trained range is quoted as $150<h^+_{\mathrm{wm}}<1200$ (p. 6). The solver is
a staggered second-order finite-difference code with the anisotropic
minimum-dissipation SGS model; the wall stress enters through a wall eddy
viscosity $\nu_t\vert_w=\tau_{w,\mathrm m}/(\rho\,\partial_y u\vert_w)-\nu$
(Eq. 10), which the authors state is better against
[log-layer mismatch](/definitions/log-layer-mismatch.md) than a Neumann
condition.

**Tests (pp. 6–8, Table 1, Figs. 3–7).** Channel flow from $Re_\tau=5200$
to $10^6$ at $\Delta_{x,z}=0.05\delta$, runs of $300\delta/u_\tau$:

| $Re_\tau$ | $\Delta_y/\delta$ | $h^+_{\mathrm{wm}}$ |
|---|---|---|
| 5200 | 0.05 | 520 |
| $10^4$ | 0.05 | 1000 |
| $2\times10^4$ | 0.05, 0.025 | 2000, 1000 |
| $5\times10^4$ | 0.05, 0.01 | 5000, 1000 |
| $10^5$ | 0.05 | $10^4$ |
| $10^6$ | 0.05 | $10^5$ |

Every row has $h_{\mathrm{wm}}=2\Delta_y$ *(compiler check, not in the
sources)*.

- The VWM works only while $h^+_{\mathrm{wm}}$ lies in the trained range;
  refining the wall-normal grid to bring it back "significantly"
  reduces the error.
- The LLWM's error "in the friction velocity is less than 5%" and its
  mean profiles align with the log law "regardless of the value of"
  $h^+_{\mathrm{wm}}$; the authors call this comparable to the
  [equilibrium wall model](/methods/equilibrium-wall-model.md), whose
  channel results are not plotted.
- Without retraining, the LLWM predicts the skin friction of a
  zero-pressure-gradient
  [turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md) for
  $Re_\theta=1000$ to 7000 comparably to the empirical correlation of
  Schlichting & Kestin (Fig. 5).
- The LLWM wall stress correlates with the off-wall velocity at
  $h_{\mathrm{wm}}=0.1\delta$ at about 0.3, the DNS value the authors
  recall, whereas the equilibrium model's correlation is perfect (Figs.
  6–7). The authors read this as the policy replicating "the natural
  mechanisms of wall-shear stress control" (pp. 10–11).

**Cost.** Training the LLWM at $Re_\tau=4200$ costs $O(10^3)$ CPU-hours and
under 1 GB, against $O(10^7)$ CPU-hours and over 100 TB for DNS data for
supervised learning (p. 8). The authors propose adding a state dimension
to cover roughness, stratification or compressibility, not tested (pp.
10–11).

## RL wall model in WMLES (as assessed by Vadrot et al. 2023b)

Vadrot et al. (2023b, §II B 4) implement in [LESGO](/software/lesgo.md)
the log-law variant of the multi-agent RL wall model of Bae &
Koumoutsakos (2022), and compare it with an
[equilibrium wall model](/methods/equilibrium-wall-model.md). They cite
the published version; this bundle reads the preprint.

**Model.** Agents sit in a wall-parallel plane at the matching height.
Each agent multiplies its local wall stress at every action instant:
$\tau_w(t_{n+1})=a_n\tau_w(t_n)$, with $a_n\in[0.9,1.1]$ (Eq. 7).

**States (Eq. 8).** Two log-law fit parameters computed at
$h_{\mathrm{wm}}$ from the LES velocity and its wall-normal derivative:
a local inverse slope $1/\kappa_{\mathrm{wm}}$ and an intercept
$B_{\mathrm{wm}}$ (page-local names, mirroring $\kappa$ and $B$).

**Training.** As recalled there, the model was trained in WMLES at
$Re_\tau=2000$, 4200 and 8000, from fields generated with the equilibrium
model ("EWM-generated flow fields", §II B 4) and without high-fidelity
data, at about $10^7$ gradient steps (§IV D). The reward is not stated in this paper. The preprint of Bae &
Koumoutsakos (2022, Methods p. 12) says only that episodes start from "a
previously obtained WMLES flow field" plus noise; it does not name the
wall model that produced that field.

**Findings in half-channel flow from $Re_\tau=180$ to $10^{10}$ (§III,
§IV C, Table III).**

- **Log-layer mismatch.** The model gives the log law with a
  [log-layer mismatch](/definitions/log-layer-mismatch.md) of $+2.2$ inner
  units at $Re_\tau=180$, $+1.0$ to $+2.0$ from $10^3$ to $10^5$, and
  $-0.9$ to $-3.2$ from $10^6$ to $10^{10}$. The authors attribute "the
  good performance at $Re_\tau=10^5$ and $10^6$" to $h^+_{\mathrm{wm}}$
  being near the training values, and the mismatches at lower and higher
  $Re_\tau$ to its distance from them (§III A).
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
  transfer learning and meta-RL to cut training cost.
- **Reynolds-number extrapolation of the log-law RL wall model.** Bae &
  Koumoutsakos (2022, preprint p. 6, Figs. 3–4), training at
  $Re_\tau=2000$–8000, report for the LLWM a friction-velocity error
  "less than 5%" and mean profiles "well-aligned with the log law
  regardless of the value of" $h^+_{\mathrm{wm}}$, in channel flow from
  $Re_\tau=5200$ to $10^6$ in their finite-difference solver
  ($\Delta_{x,z}=0.05\delta$, Table 1). Vadrot et al. (2023b), who name
  the original authors' claim of "extrapolation to unseen Reynolds
  numbers" as one they assess (§I), find in LESGO a log-layer mismatch of
  $+1.0$ to $+2.0$ inner units from $Re_\tau=10^3$ to $10^5$ and $-0.9$ to
  $-3.2$ from $10^6$ to $10^{10}$ (Table III), and call their results
  "slightly different" from the original ones, "mainly because of the
  difference in the grid resolution" (§III A). The two use different
  solvers, SGS models, grids and error measures, and Vadrot et al. cite
  the published version while this bundle reads the preprint. The
  normative entry on this disagreement is on
  [machine-learning wall models](/methods/machine-learning-wall-model.md).
- **Reward sign in Bae & Koumoutsakos (2022, Eq. 9).** The preprint prints
  $$r_n=\frac{\lvert\tau_w-\tau_{w,\mathrm m}(t_n)\rvert-\lvert\tau_w-\tau_{w,\mathrm m}(t_{n-1})\rvert}{\tau_w}+\mathbb 1\!\left(\frac{\lvert\tau_w-\tau_{w,\mathrm m}(t_n)\rvert}{\tau_w}<0.01\right),$$
  whose first term is positive when the error grows from $t_{n-1}$ to
  $t_n$, while the text twice calls the reward proportional to the
  improvement *(compiler check, not in the sources)*. The same preprint's
  ReF-ER weight update (Eq. 8) prints, in its second branch,
  $\beta\leftarrow\beta+(1-\eta)\beta$, i.e. nearly doubling a weight that
  Eq. 7 uses with its complement $1-\beta$ (here $\beta$ is the ReF-ER
  weight and $\eta$ a learning rate, page-local) *(compiler check, not in
  the sources)*.
- **Which VWM cases fail.** Bae & Koumoutsakos (2022, p. 6) name only
  $Re_\tau=2\times10^4$ and $5\times10^4$ at $\Delta_y=0.05\delta$ as
  failing because $h^+_{\mathrm{wm}}$ leaves the trained range; by their
  Table 1 the $Re_\tau=10^5$ and $10^6$ cases are also outside it, and the
  Fig. 4 caption omits "the two largest Reynolds number cases for VWM"
  because their profiles fall outside the plot.
- **Error metric.** The text (p. 6) quotes the LLWM error in the friction
  velocity; the Fig. 3 caption calls the plotted quantity the error in the
  time-averaged wall stress. Since $\tau_w\propto u_\tau^2$ the two differ by
  about a factor two for small errors *(compiler check, not in the
  sources)*.
- **Robustness to numerics.** Bae & Koumoutsakos (2022, pp. 3, 10) claim
  robustness to the discretization because numerical errors enter
  training; the preprint uses one solver and one SGS model (see
  [model-consistent training](/methods/model-consistent-training.md)).

# Citations

- [Beck & Kurz (2023)](/sources/beck-2023.md) — §I (motivation), §II B (MDP, PPO), §III B–C, Eqs. 11–17, Table I, §IV A–B, Eq. 18, §V A–C, Figs. 7–14, App. A, §VI.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II B 4, Eqs. 7–8; §III A–B, Figs. 8–10; §IV C, Eqs. 10–14, Table III; §IV D.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §IV.B (model-consistent training as the class to which in-the-loop optimization belongs).
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Research Square preprint v1: pp. 3–8, Eqs. 1–3, 9–10, Table 1, Figs. 2–7; Discussion pp. 10–11; Methods pp. 11–14, Eqs. 4–8.
