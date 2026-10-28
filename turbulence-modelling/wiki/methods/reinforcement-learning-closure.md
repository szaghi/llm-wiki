---
type: Method
title: "Reinforcement-learning turbulence closures"
description: "Closures set or learned online by a policy trained with reinforcement learning, the running LES being the environment and the reward a solver statistic: element-local SGS coefficients in DG-LES, pointwise SGS stress tensors for channel LES trained on mean profiles, multi-agent wall-stress models with disputed extrapolation and Reynolds-number-independent states; RL also drives offline symbolic-expression search."
status: established
aliases: [RL closure, VYBA23, RLWM, PPO closure, reinforcement-learning SGS model, deep reinforcement learning SGS model, DRL SGS model, multi-agent reinforcement learning wall model, MARL wall model, SciMARL, RL-Const, RL-Quad, RL-Blend, VWM, LLWM, DRL180]
tags: [reinforcement-learning, sgs-model, data-driven, implicit-les, wall-model, neural-network]
timestamp: 2026-10-27T21:12:00Z
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
operator (Beck & Kurz 2023, §I), without gradients of the solver. See
[model-consistent training](/methods/model-consistent-training.md) for the
class of training inside the model environment that Duraisamy (2021,
§IV.B) defines; that review names RL only as a flow-control application
(§I) and does not discuss RL closures. Beck &
Kurz (2023) use it for SGS models in discontinuous Galerkin LES.
[Kim et al. (2022)](/sources/kim-2022.md) use it to learn a pointwise SGS
stress tensor for wall-resolved LES of channel flow from two mean profiles.
[Bae & Koumoutsakos (2022)](/sources/bae-2022.md) use it, with many
cooperating agents, for wall-stress models in wall-modelled LES, and
Vadrot et al. (2023b) assess one of those wall models in another code;
[Vadrot et al. (2023a)](/sources/vadrot-2023.md) then redesign its states
so that it extrapolates in Reynolds number.

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
flux and BR1 lifting (§III A). The [Relexi](/software/relexi.md) framework couples FLEXI to the
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

## The precursor: element-wise Smagorinsky coefficient (Kurz et al. 2023)

[Kurz et al. (2023)](/sources/kurz-2023.md) (arXiv v2) is an earlier
paper of the same group. Beck & Kurz (2023) extend its setting and agent:
beta-distributed instead of Gaussian actions, more polynomial degrees,
and quadratic and blending actions besides the constant coefficient. Its setting is
implicitly filtered [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md)
LES in [FLEXI](/software/flexi.md) (kinetic-energy-preserving split form
on LGL nodes) of forced
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
at $Re_\lambda\approx180$ and $M=0.1$, with Lundgren's linear forcing
applied at the nodes (§3.1–3.2). The agent runs in the
[Relexi](/software/relexi.md) framework.

**MDP (§3.4, Table 1).**

- *State.* The conserved-variable field of the LES.
- *Action.* One Smagorinsky coefficient per element, $C_s\in[0,0.5]$,
  updated every $\Delta t_{\mathrm{RL}}=0.1$; the eddy viscosity is
  $\mu_t=\rho(C_s\Delta)^2\lvert\bar S\rvert$ (Eq. 19; the paper does not
  define $\Delta$ for DG). Negative values are excluded to keep a
  monotone map from action to eddy viscosity; removing both limits gave
  similar accuracy for selected cases but needed many more iterations
  (footnote 3).
- *Policy.* A 3D CNN on one element's $(N+1)^3$ nodal values: four
  convolution layers (8, 8, 4 and 1 filters) with ReLU, then a sigmoid
  scaled to $[0,0.5]$ (Fig. 4). Every element is an agent and all share
  the weights. The value network adds two dense layers (16 and 1 neurons)
  that combine the element outputs.
- *Inputs compared.* The momentum field of the element, or the five
  invariants of the velocity-gradient tensor (Pope) used by Novati et al.
  for Galilean invariance. The momentum input is purely element-local; the
  authors present this as an improvement on Novati et al., who also fed
  the global dissipation rate and energy spectrum (§1, §3.4).
- *Exploration.* Actions are drawn from a normal distribution about the
  network output with fixed standard deviation 0.02.
- *Reward (Eq. 21).*
  $$r=2\exp\!\left(-\frac{1}{\alpha_r k_{\max}}\sum_{k=1}^{k_{\max}}\left(\frac{\langle E_{\mathrm{DNS}}\rangle(k)-E_{\mathrm{LES}}(k)}{\langle E_{\mathrm{DNS}}\rangle(k)}\right)^2\right)-1,$$
  stated to lie in $[-1,1]$, with $\langle E_{\mathrm{DNS}}\rangle$ the time-averaged DNS spectrum,
  $E_{\mathrm{LES}}$ the instantaneous LES spectrum and $\alpha_r=0.4$
  (page-local; the paper's $\alpha$). $k_{\max}$ is chosen so that 2.6 to 3
  points per wavelength remain at the cutoff, against a resolution
  capability of about 4 for these schemes, so that all represented
  wavenumbers are optimized (§3.5).
- *Training (§3.5).* PPO with clip 0.2, discount $\gamma_{\mathrm{RL}}=0.995$,
  Adam at $10^{-4}$, entropy coefficient 0, 5 epochs per iteration (1 at 48
  DOF), episodes of 5 time units (about 7 large-eddy turnovers) from
  filtered DNS at four instants; 16 or 32 episodes per update, and 32
  "consistently" sped up training (§4.1).

**Configurations (Table 2).** 24 DOF ($N=5$, $4^3$ elements, $k_{\max}=9$),
32 DOF ($N=7$, $4^3$, 12), 36 DOF ($N=5$, $6^3$, 13), 48 DOF ($N=5$,
$8^3$, 16).

**Results (§4).**

- *Training.* The return rises from negative values to a plateau just
  below the maximum of 50 (Fig. 5). The 48-DOF case needed fewer
  iterations than the 24-DOF case; the authors offer two reasons and note
  the speed-up could be stochastic.
- *Accuracy.* Tested from an unseen state to $t=20$ (four times the
  training horizon), the models are stable. No-model LES piles energy up
  at high wavenumbers; static Smagorinsky ($C_s=0.17$) is over-dissipative
  near the resolution limit. The RL model "clearly outperforms both" and
  matches the DNS spectrum "almost perfectly up to and even beyond" the
  resolution limit (Fig. 6). The dynamic model is as accurate, except at
  24 DOF, where the RL model is significantly better; the authors' "likely
  explanation" is a test filter outside the scale-similar range (§4.2).
- *Coefficient distribution.* Most predicted $C_s$ are near zero with a
  decaying tail; at 24 DOF the agent uses almost the whole range up to
  0.5, at 48 DOF it stays below 0.3 (Fig. 6).
- *Velocity PDFs.* Closer to DNS than the no-model and static models, but
  at 36 DOF the RL model gives an asymmetric fluctuation distribution whose
  origin is "still subject of on-going investigations".
- *Inputs.* Invariant inputs train slower and less stably and end worse,
  "quite substantial[ly]" at 36 DOF even with doubled training; the
  authors attribute this to their spread over orders of magnitude, the
  discontinuity of DG gradients at faces, and large gradients in the
  projected initial states (§4.3, Fig. 7).
- *Generalization.* The 36- and 48-DOF policies swapped between the two
  grids stay stable and accurate (§4.4, Fig. 8); policies trained at
  $Re_\lambda\approx180$ stay stable at $Re_\lambda\approx240$, still beat
  no-model LES and static Smagorinsky, match the dynamic model, and beat
  it at 24 DOF (§4.5, Fig. 9). See
  [discretization-consistent closure](/definitions/discretization-consistent-closure.md)
  for the authors' reading of the resolution dependence.
- *Cost.* On one CPU core at 48 DOF, the unoptimized policy took about
  10% more time than the dynamic procedure (§4.2). Training took one to
  five days (§4.1).

The authors "do not propose to use any of the models prescribed here in
practice" (§5). The dynamic baseline is element-wise in DG: modal cutoff
test filter to degree 2 ($N=5$) or 3 ($N=7$), element-averaged Germano–Lilly
coefficient, eddy viscosity clipped to $[-100\mu,1000\mu]$; unclipped, it
occasionally produced huge coefficients that "deteriorated the solution
quite drastically" (App. A; see
[dynamic procedure](/methods/dynamic-procedure.md)).

## Pointwise SGS stress models for channel LES (Kim et al. 2022)

Kim et al. (2022) train a neural-network SGS model for wall-resolved LES
of incompressible [channel flow](/benchmarks/turbulent-channel-flow.md)
with deep reinforcement learning (DRL). No filtered-DNS (fDNS) fields are
used. The only targets are two time-averaged fDNS profiles (Abstract, §II
B). The version read is arXiv v2. Page-local notation, in the paper's units
of the half-height $\delta$ and $u_\tau$:

- $\mathcal S_1(y)=Re_\tau^{-1}\,\mathrm d\langle\bar u\rangle/\mathrm dy$ is
  the mean viscous stress and $\mathcal S_2(y)=\langle\bar u'\bar v'\rangle$
  the mean resolved Reynolds shear stress, where $\langle\cdot\rangle$
  averages over the homogeneous directions and time and the prime is the
  fluctuation of the filtered velocity;
- $\gamma_{\mathrm{RL}}$ is the discount factor (not the ratio of specific
  heats);
- $\Delta t_{\mathrm{RL}}$ is the interval between actions, 30 LES steps,
  which the paper equates to 5.4 wall time units.

**Why two profiles suffice.** The mean total shear stress satisfies
$\mathcal S_1-\mathcal S_2-\langle\tau_{xy}\rangle=1-y$ (Eq. 11), so
matching two of the three terms fixes the third. Rewarding the viscous
stress and $\langle\tau_{xy}\rangle$ trained slightly more stably, but was
dropped because $\tau_{xy}$ is not available in practice (§II B).

**Actor and critic (§II B–C, §II F).** The algorithm starts from DDPG and
TD3 (actor–critic, with clipped double Q-learning, delayed policy updates
and target smoothing).

- *Actor.* A pointwise fully connected network of six hidden layers of 128
  units, chosen pointwise so as to be mesh-agnostic. It maps the local
  resolved velocity gradient $\partial_i\bar u_j$ and the local grid size
  $(\Delta x^+\Delta y^+\Delta z^+)^{1/3}$, both in wall units, to the six
  components of $\tau_{ij}$. A variant outputs a scalar $\nu_t$ in
  $\tau^d_{ij}=-2\nu_t\bar S_{ij}$. The output is multiplied by the
  square of the filter width $\Delta$. The authors state that this improves
  generalization across grids; without it the network can produce strong
  SGS stress even on DNS-resolution grids (§II C).
- *Critic.* A 2D convolutional network on an $8\times1\times8$ patch of
  local states, plus plane-averaged global states (mean velocities and their
  wall-normal gradients, rms velocities, $\mathcal S_2$, $y^+$).
- *Optimization.* Adam with learning rates $10^{-4}$ (critic) and
  $2\times10^{-6}$ (actor), mini-batch 64, replay buffer 64,000. Eight
  parallel LES with different exploration noise run at once, in one long
  episode restarted on divergence, from a no-model initial field.

**Reward (Eqs. 12–17).** The reward is localized in $y$:

$$r_t(y)=-\sum_{i=1}^{2}c_i\left\lvert\mathcal S_i^{\mathrm{fDNS}}(y)-\mathcal S_i^{\mathrm{LES}}(y)\right\rvert^{1/2},\qquad c_1=1,\ c_2=0.5.$$

With $c_1=c_2=1$ the mean velocity fluctuated and learning was unstable.
The square root, which evens out the reward scale across $y$, trained
better than the absolute value. In the form used, the LES statistic is a
discount-weighted time average over the next $N_s$ (page-local) action
intervals.

**Four modifications of DDPG/TD3 (contribution, §II B–D, Algorithm 1).**

1. *Localized reward.* The reward is a function of $y$, as above.
2. *Truncated return.* The discount-weighted time-averaged reward replaces
   the Bellman bootstrap: the critic regresses this reward directly. This
   gives the simplified algorithm.
3. *Exploration noise.* Noise is added in parameter space and correlated in
   space and time by an Ornstein–Uhlenbeck process. Its amplitude adapts to
   keep a target policy distance $d$ (page-local, one minus the mean
   correlation between perturbed and unperturbed actions).
4. *Pretraining.* The actor is first fitted by least squares to a
   conventional model, mostly the static
   [Vreman model](/methods/vreman-model.md), for 50,000 iterations ("only a
   few minutes").

**Built-in constraints (§II E, Eq. 22).**

- *Reflectional equivariance in $y$ and $z$.* It is imposed by averaging
  the actor over mirror images of its input; the same is done for the
  critic.
- *Zero SGS stress at the wall.* The actor output is multiplied by the
  2-norm of the seven velocity-gradient components that vanish at a
  no-slip wall. The authors stress that no van Driest damping is used.
- *Not imposed.* Rotational and Galilean invariance. A
  [tensor-basis neural network](/methods/tensor-basis-neural-network.md)
  was tried for rotational invariance without conclusive gain.

**Hyperparameter findings (§III A–B).**

- *Return.* One-step temporal-difference learning and the instantaneous
  reward ($N_s=1$) both fail to raise the accuracy. Accumulation helps from
  $N_s=20$ and saturates for $N_s\ge50$; $\gamma_{\mathrm{RL}}=0.99$ is best
  for $N_s=200$ (Fig. 4).
- *Return time scale.* $-\Delta t_{\mathrm{RL}}/\ln\gamma_{\mathrm{RL}}\approx100\,\Delta t_{\mathrm{RL}}$,
  "approximately 500 wall time units". The authors relate this to a
  wall-shear-stress structure lifetime of about 60 wall units, citing
  Quadrio & Luchini, and argue for accumulating returns over about ten
  lifetimes.
- *Noise.* The correlated parameter-space noise gives a "critical
  improvement" over no noise and over uncorrelated Gaussian action noise of
  20% of the local rms action. Distance $d=0.05$ is fastest and most
  stable; $0.02$ is slow, and $0.1$ oscillates because LES runs diverge
  (Fig. 5).
- *Actor depth.* Three hidden layers fail in a coarse LES; six and nine
  succeed, and six is chosen for cost.
- *Constraints.* The wall constraint makes learning faster and more stable.
  Without it, exploration produces "nonphysically strong SGS mean shear
  stress near the wall". Without reflectional equivariance, a spanwise mean
  velocity appears, because spanwise statistics are not in the reward (Fig.
  6).
- *Pretraining target.* Pretraining on Vreman or on the dynamic
  Smagorinsky model both work, Vreman converging slightly faster.
  Pretraining on the [scale-similarity model](/methods/scale-similarity-model.md)
  makes the DRL unstable because that LES is numerically unstable (§II D,
  no results shown).

**Environments (Tables I–III).** The DNS of the targets have
$(\Delta x^+,\Delta z^+)=(17.7,8.84)$ at $Re_\tau=180$, 360 and 720.

| Model | Training $Re_\tau$ | LES grid | $(\Delta x^+,\Delta z^+)$ | DRL iterations |
|---|---|---|---|---|
| DRL180, DRL180(clip), DRL180($\nu_t$) | 180 | $32\times49\times32$ | (70.7, 35.3) | 10,000 |
| DRL180c, DRL180c(clip) | 180 | $24\times49\times24$ | (94.2, 47.1) | 15,000 |
| DRL360 | 360 | $32\times65\times32$ | (70.7, 35.3) | 15,000 |

"(clip)" sets negative SGS dissipation to zero; "($\nu_t$)" is the
eddy-viscosity variant. Testing adds $Re_\tau=720$ on $32\times97\times32$
at (70.7, 35.3). The baselines are the static Vreman model with constant
0.08, the [dynamic Smagorinsky model](/methods/dynamic-procedure.md) and
no-model LES. Training takes 2–4 days on one NVIDIA Titan Xp GPU (§II F).

**Results in the training environment (§III C, Figs. 7–11).**

- *Targets.* DRL180 and DRL180(clip) reproduce the fDNS mean velocity and
  Reynolds shear stress almost exactly.
- *Other statistics.* They also predict the rms velocity, the mean SGS
  shear stress and the mean SGS transport better than the Vreman, dynamic
  and no-model LES.
- *Eddy-viscosity form.* DRL180($\nu_t$) overpredicts
  $\langle\bar u\rangle$ in the buffer and log layers, as the dynamic model
  does. The authors conclude that "the eddy-viscosity assumption could
  seriously limit the performance".
- *SGS dissipation.* The two targets do not fix the mean SGS dissipation:
  models trained with the same settings give different values. An accurate
  mean SGS transport "appears to be a necessary condition" for accurate
  targets.
- *Backscatter.* Clipping it changes almost nothing (see
  [energy backscatter](/definitions/energy-backscatter.md)).
- *Coarser grid and higher $Re_\tau$.* Training also succeeds on the
  coarser grid, where the fDNS peak of the mean SGS shear stress is about
  twice that of the finer grid and three times that of the dynamic model.
  It succeeds at $Re_\tau=360$ with the same hyperparameters.

**Generalization (§III D, Figs. 12–13).**

- *Untrained $Re_\tau$ at fixed wall-unit resolution.* DRL180 underestimates
  the buffer-layer slope of $\langle\bar u\rangle$ at $Re_\tau=360$. DRL360
  overestimates $\langle\bar u\rangle$ at 180, and both underestimate the
  slope at 720. Their Reynolds shear stress stays "quite precise", while the
  dynamic and no-model LES overpredict it at every $Re_\tau$.
- *Untrained coarser grid.* DRL180 overpredicts the Reynolds shear stress
  and underpredicts the SGS shear stress (not plotted). The authors
  conclude that "a model trained in a single environment might not perform
  well in a different environment".

**Stress–strain alignment (§III E, Eqs. 27–28, Table IV, Figs. 15–20).**
All models are evaluated on the same resolved field (the LES with DRL180)
and compared with fDNS. The tensor angle between $-\tau^d_{ij}$ and
$\bar S_{ij}$ is zero by construction for a linear eddy-viscosity model.

| Quantity | $y^+$ | fDNS | dynamic Smagorinsky | DRL180 |
|---|---|---|---|---|
| correlation of $\bar S_{xy}$ and $-\tau_{xy}$ | 15 | $-0.20$ | 0.95 | 0.34 |
|  | 50 | 0.19 | 0.94 | 0.58 |
| correlation of $\lvert\bar S\rvert^3$ and the SGS dissipation | 15 | 0.01 | 0.92 | 0.56 |
|  | 50 | 0.28 | 0.88 | 0.73 |

- *Tensor angle.* In fDNS its mean is near $\pi/2$ at every height. Its PDF
  is compared with the $\sin^3$ PDF of the angle between two random
  trace-free symmetric tensors (a five-dimensional space). For DRL180 the
  peak moves from about 0.3 rad near the wall toward $\pi/2$ with distance;
  for DRL180(clip) the mean is about 0.9 rad at all heights.
- *Eigenvectors.* In fDNS the most-stretching eigenvectors of the two
  tensors are at about $\pi/4$ near the wall, the most-compressing ones
  almost random, and both tend to random away from the wall. DRL180 aligns
  both, imperfectly, at $y^+\approx15$.
- *Eddy-viscosity level.* The eigenvalue ratio of $-\tau^d_{ij}$ to
  $\bar S_{ij}$ (twice a plane-averaged eddy viscosity) is "one order of
  magnitude larger" in fDNS than in every model. The models are close to
  one another, DRL being about twice the dynamic and Vreman models for
  $y^+\le15$ (Fig. 20).
- *Authors' conclusion.* "The non-alignment nature between" $-\tau^d_{ij}$
  and $\bar S_{ij}$, "rather than the level of eddy viscosity, plays a more
  important role". The evidence offered is the correlations, angle PDFs and
  eigenvalue ratios above; no model with the fDNS alignment but a
  different eddy-viscosity level is run (§III E).

**Comparison with supervised learning (§III C, §III E).** Kim et al. cite
supervised network SGS models fed with local velocity gradients (Park &
Choi 2021) that reach a correlation of only about 0.5 with
the fDNS stress. The supervised model of that study with the same inputs
as here "did not predict" the two target profiles well and "highly
overpredicted" $\lvert\tau_{xy}\rvert$. The authors conclude that "DRL using
only statistical data for training can be superior to the standard
supervised learning using expensive filtered DNS data" (see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

## Comparison of the RL closures

| | Kurz et al. (2023) | Beck & Kurz (2023) | Kim et al. (2022) | Bae & Koumoutsakos (2022) | Vadrot et al. (2023a) |
|---|---|---|---|---|---|
| Closure | element-local Smagorinsky coefficient | element-local Smagorinsky coefficient (constant or quadratic) or DG/FV blending | full SGS stress tensor (or $\nu_t$) at every grid point | multiplicative update of the local wall stress | as Bae & Koumoutsakos, with Reynolds-number-independent states |
| Flow | forced isotropic turbulence, DG-LES, $N=5,7$ | forced isotropic turbulence, DG-LES, $N=3,5,8$ | wall-resolved channel LES, $Re_\tau=180$, 360 | wall-modelled channel LES | wall-modelled half channel, $48^3$, trained at $Re_\tau=10^4$ |
| Reward | LES energy spectrum against DNS | LES energy spectrum against DNS | mean viscous and resolved Reynolds shear stress profiles against fDNS | true mean wall stress | true mean wall stress |
| Algorithm | PPO, Gaussian actions | PPO, beta-distributed actions | DDPG/TD3 with truncated return | V-RACER | V-RACER |

The two DG studies overlap at 24 and 36 DOF with $N=5$ and agree there:
Kurz et al. (2023, §4.2) find the dynamic model as accurate as RL at 36
DOF and worse at 24 DOF, as Beck & Kurz (2023, §V B) do.

## RL as an optimizer of model expressions (Tang et al. 2023)

[Tang et al. (2023)](/sources/tang-2023.md) use RL in another role: the
policy is a recurrent network that writes algebraic expressions token by
token, and it is trained offline with a risk-seeking policy gradient to
maximize the fit of the expressions to DNS anisotropy data. The learned
object is an explicit RANS closure, and no solver runs during training
(§II C). The authors recall the RL closures of Novati et al., Kim et al.,
Bae & Koumoutsakos and Kurz et al. as precedents (§I). See
[symbolic-regression closures](/methods/symbolic-regression-closure.md).
The training loss compares the expressions with DNS data outside the
solver (§II E); Tang et al. name coupling the search with RANS as future
work (§IV).

Sirignano & MacArt (2023, §1) set RL against adjoint training on
consistency grounds; see
[model-consistent training](/methods/model-consistent-training.md) for the
characterization and its scope.

Kim et al. (2022, §I) cite Novati et al. (2021), who found learning
with fully dispersed agents at all grid points unsuccessful in isotropic
turbulence and restricted the actions to Smagorinsky-type eddy
viscosities. Kim et al. use pointwise tensor actions at every grid point.

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
  cite, whereas the equilibrium model's correlation is perfect (Figs.
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

**Training.** Vadrot et al. state, citing the original work, that the
model was trained in WMLES at
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

## Reynolds-number-independent states (Vadrot et al. 2023a)

[Vadrot et al. (2023a)](/sources/vadrot-2023.md) (arXiv v3) develop a
new multi-agent RL wall model, named VYBA23, as a correction of the
log-law model of Bae & Koumoutsakos (BK22 in their naming), in
[LESGO](/software/lesgo.md) half-channel flow. Page-local notation as in
the section above: $1/\kappa_{\mathrm{wm}}$ and $B_{\mathrm{wm}}$ are the
local log-law slope and intercept at $h_{\mathrm{wm}}$; $\kappa=0.4$,
$B=5$ are the reference log-law constants; $\Delta a$ is the action range,
$a_n\in[1-\Delta a,1+\Delta a]$; $\Delta t_{\mathrm{RL}}$ the action
interval (registry §11), in LES time steps $\Delta t$.

**Diagnosis (§II.B.3, Eq. 9, Fig. 3a).** The neutral line of the state
plane, on which the LES velocity at $h_{\mathrm{wm}}$ equals the log law,

$$\frac{1}{\kappa_{\mathrm{wm}}}\ln h^+_{\mathrm{wm}}+B_{\mathrm{wm}}-\Big(\frac1\kappa\ln h^+_{\mathrm{wm}}+B\Big)=0,$$

has slope $-1/\ln h^+_{\mathrm{wm}}$ in the $(B_{\mathrm{wm}},1/\kappa_{\mathrm{wm}})$
plane, which the paper writes $-1/(\ln(\Delta y/\delta)+\ln Re_\tau)$
with $h_{\mathrm{wm}}$ one wall-normal spacing $\Delta y$ (wall-normal $z$
in the paper). It rotates with $Re_\tau$ and saturates at large
$Re_\tau$, which the authors give as the cause of BK22's saturating
large-$Re_\tau$ [log-layer mismatch](/definitions/log-layer-mismatch.md),
following their survey (Vadrot et al. 2023b).

**New state (Eq. 10).** The first state is replaced by

$$s_1=\Big(\frac{1}{\kappa_{\mathrm{wm}}}-\frac1\kappa\Big)\ln h^+_{\mathrm{wm}},\qquad s_2=B_{\mathrm{wm}},$$

so that the neutral line becomes $s_1+s_2-B=0$ for every $Re_\tau$ (Fig.
3b). Action, reward and algorithm are those of BK22: $\tau_w$ multiplied
by $a_n$, reward on the distance from the true mean wall stress
$\tau_w=-\delta\,dp_0/dx$ of the pressure-driven channel, V-RACER in the
smarties library (§II.B.2–3, Eqs. 3–6).

**Training and tests (Table I, §III).** One training Reynolds number,
$Re_\tau=10^4$, on a $48^3$ grid, 256 agents spaced three cells apart,
$\Delta a=0.10$, $\Delta t_{\mathrm{RL}}=10\Delta t$, started from an
equilibrium-wall-model field. Tests at eleven $Re_\tau$ from 180 to
$10^{10}$ against the equilibrium model and BK22 retrained by the authors
in LESGO at $Re_\tau=10^4$.

- VYBA23 recovers the log law up to $Re_\tau=10^{10}$ whenever
  $h_{\mathrm{wm}}$ lies in the log layer; at $Re_\tau=180$ its profile
  lies above DNS (§III.A, Fig. 6).
- The retrained BK22 loses its low-$Re_\tau$ mismatch but keeps the
  large-$Re_\tau$ one (§II.B.2, Fig. 2); the authors attribute the
  difference from the original BK22 to the training Reynolds number, the
  RL settings and possibly the solver.
- Accuracy of the sign of $a_n-1$ against the neutral line (Table III):

  | $Re_\tau$ | 180 | $10^3$ | $10^5$ | $10^{10}$ |
  |---|---|---|---|---|
  | BK22 | 0.49 | 0.50 | 0.53 | 0.49 |
  | VYBA23 | 0.92 | 0.91 | 0.83 | 0.64 |

**Agent parameters (§III.B, §IV, Figs. 9–12).** Mean velocity is
essentially insensitive to $\Delta a$, $\Delta t_{\mathrm{RL}}$ and agent
spacing, "the only exception being when the time-step between actions
becomes too large" ($\Delta t_{\mathrm{RL}}>10\Delta t$). Wall-stress
fluctuations grow with $\Delta a$ and fall with $\Delta t_{\mathrm{RL}}$;
agent spacing matters little. Repeated maximal actions give the
similarity rule (Eqs. 15–17)

$$\frac{\ln(1+a_1)}{b_1}=\frac{\ln(1+a_2)}{b_2}\ \Rightarrow\ \frac{a_1}{b_1}=\frac{a_2}{b_2}\quad(a\ll1)$$

for two models with $(\Delta a,\Delta t_{\mathrm{RL}})=(a_1,b_1\Delta t)$
and $(a_2,b_2\Delta t)$, confirmed by overlapping fluctuation curves for
ratios 2 and 10 (Fig. 12). The setting closest to filtered-DNS wall-stress
fluctuations is $\Delta a=0.10$, $\Delta t_{\mathrm{RL}}=5\Delta t$,
spacing of three cells, "possibly" solver dependent.

**Claims about RL.** The authors state that the model "does not rely on
high-fidelity data, as the back-propagation process is based on a reward
rather than output error", that the two-state map makes the policy
interpretable, and that RL "surpass[es] supervised ML" by removing the
need for filtered DNS and the a priori/a posteriori input inconsistency
(Abstract, §IV, §V). The same conclusion says that "the purpose of this
paper is not to establish the superiority of the RL approach" (§V).
Training was "challenging and time-consuming": "hundreds of simulations
and millions of policy gradient updates", several rewards tried (§II.B.3).
See [machine-learning wall models](/methods/machine-learning-wall-model.md).

## RL as seen by other data-driven sources

- [van Gastelen et al. (2024)](/sources/vangastelen-2024.md) (§1) name RL
  as the other route to stable learned closures, one that needs no
  gradients, and build their own stability into the network architecture
  instead (see [neural-network SGS models](/methods/neural-network-sgs-model.md)).
- [Kim et al. (2024)](/sources/kim-2024.md) (§1, §5) argue that RL, like
  adjoint training, needs target statistics that are "unknown a priori"
  for flows over complex geometries, and train their cylinder-wake
  networks on filtered DNS instead. The rewards of the RL closures above
  use DNS spectra (Beck & Kurz; Kurz et al.), filtered-DNS mean profiles
  (Kim et al. 2022) or the known mean wall stress of a pressure-driven
  channel (Bae & Koumoutsakos; Vadrot et al. 2023a).
- [Wu & Lele (2026)](/sources/wu-2026.md) (arXiv v2, §1) cite Kim et al.
  (2022), Bae & Koumoutsakos (2022), Kurz et al. (2023) and Guan et al.
  as RL closures that learn "the combined effect of solver numerics and
  physics", hence "limited in their transferability to other solvers",
  and costlier to train because LES must run during training. Their own
  route is supervised training on several filter shapes (see
  [neural-network SGS models](/methods/neural-network-sgs-model.md) and
  [discretization-consistent closure](/definitions/discretization-consistent-closure.md)).
  The transferability claim is not tested there; Kurz et al. (2023, §4.4)
  report RL policies that stay stable and accurate across two DG
  resolutions, within one code.
- [Ihme et al. (2022)](/sources/ihme-2022.md) review RL for combustion
  control, not for turbulence closures (§3.4, §4.2; their tutorial is
  Q-learning control of a well-stirred reactor, §3.4.3). They name three
  generic obstacles to the technical adoption of deep RL: data
  inefficiency (upward of $\mathcal O(10^5)$ training samples, "more than
  $10^5$ training steps" in §5), unpredictable behaviour outside the
  training conditions, and lack of interpretability (§3.4.2, §5).

## Qualifications

- **Reward sign in Beck & Kurz (2023, Eq. 18).** The reward is printed as
  $$r=2\exp\!\left(\frac{\beta}{k_{\max}}\sum_{k=1}^{k_{\max}}\left(\frac{\overline E_{DNS}(k)-E_{LES}(k)}{\overline E_{DNS}(k)}\right)^2\right)-1,$$
  with $\beta=0.4$ (page-local, the paper's reward scaling, not the
  field-inversion $\beta(\boldsymbol x)$) and the overbar a time average,
  not the LES filter; it is stated to be normalized to $[-1,1]$. With a
  non-negative sum and a positive exponent, the printed form gives
  $r\ge1$; a negative exponent gives $r\in(-1,1]$ with $r=1$ at zero
  error, which matches the stated range *(compiler check, not in the
  sources)*. The precursor paper of the same group, Kurz et al. (2023,
  Eq. 21), prints the same reward with the negative exponent,
  $-1/(\alpha_rk_{\max})$, and the range $[-1,1]$, with the same scaling
  value 0.4.
- **Printed slips in Kurz et al. (2023).** The reward is written
  $\mathcal R(s_t,s_{t+1})$ in Table 1 and §2 and $\mathcal R(s)$ in Eq. 21;
  the episode length is $\Delta t_{\mathrm{end}}$ in §3.5 and $t_{\mathrm{end}}$
  in the Fig. 5 caption. The sigmoid output layer gives the open interval
  $(0,0.5)$, while $C_s\in[0,0.5]$ is printed *(compiler check, not in the
  sources)*. In §4.4 the coefficient distributions are said not to
  change with resolution, and the next sentences give different maxima
  for the two policies (0.4 and 0.3); the two are consistent only if the
  first statement means each policy across the two grids.
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
- **What the channel DRL model guarantees.** Kim et al. (2022) state that
  training in the LES "guarantees the accuracy of the LES statistics used as
  the training target" (§III C). Their own §III D shows this holds in the training
  environment only: the same model fails on an untrained coarser grid.
  The authors also assume that SGS inputs in wall units are universal,
  "although it is not proven that subgrid-scale turbulence is universal in
  general" (§II F).
- **Run length in Kim et al. (2022, §II F).** The episode length is printed
  as "approximately $1.1\times10^5$ $(=\Delta t^{DRL}\times N^{DRL})$ in wall
  time units". With $\Delta t_{\mathrm{RL}}\approx5.4$ wall units and
  10,000–15,000 iterations, the product is $5.4\times10^4$ to
  $8.1\times10^4$ *(compiler check, not in the sources)*. The paper does
  not restate the $N_s$ used for the production runs; $N_s=200$ with
  $\gamma_{\mathrm{RL}}=0.99$ is the optimum of its §III A.
- **Printed slips in Kim et al. (2022).** Eq. 22 opens a parenthesis after
  the wall-constraint factor that it never closes before the division by
  four; the inline form for the reflection-averaged actor is balanced. The
  captions of Figs. 15–16 name the correlation of $\bar S_{xy}$ with
  $\tau_{xy}$, while the text and Table IV use $-\tau_{xy}$. The activation
  is printed as a "rectified linear unit with a slope of 2", not explained.
  The abstract writes "reflectional invariance" for what the body calls
  equivariance.
- **Notation of Kim et al. (2022).** The paper writes the actor weights as
  $\omega$, the critic weights as $\theta$, the discount factor as
  $\gamma$, the target statistics as $S_i$ and the velocity gradient as
  $\bar\alpha_{ij}=\partial\bar u_j/\partial x_i$; its tilde is the test
  filter. This page uses $\pi_{\boldsymbol\theta}$ for the policy,
  $\gamma_{\mathrm{RL}}$, $\mathcal S_i$, $\partial_i\bar u_j$ and the hat.
- **Printed slips in Vadrot et al. (2023a).** Eq. 4 prints the reward as
  $\big(\lvert\tau_w-\tau_{w,\mathrm m}(t_n)\rvert-\lvert\tau_w-\tau_{w,\mathrm m}(t_{n-1})\rvert\big)/\tau_w$
  plus a bonus ($\tau_w$ the true mean wall stress, $\tau_{w,\mathrm m}$ the
  modelled one, as in the reward-sign item above), in the same order as Bae & Koumoutsakos (2022, Eq. 9; see
  their [Source page](/sources/bae-2022.md)), so that as printed the first
  term is positive when the error grows *(compiler check, not in the
  sources)*.
  Eq. 6 writes $\tau_w(x,z,t_n)$ in its condition, where the agents' plane
  coordinates are $(x,y)$ in the paper's convention. Eq. 12, presented as a
  rewriting of the equilibrium model (Eq. 2), prints
  $\tau_w=\rho\,\kappa\tilde U_{\mathrm{LES}}/(\ln h^+_{\mathrm{wm}}+B)$,
  without the square, while Eq. 2 with the printed definition of the
  roughness-like length gives $[\kappa U_{\mathrm{LES}}/(\ln h^+_{\mathrm{wm}}+\kappa B)]^2$
  *(compiler check, not in the sources)*. The paper does not state which
  SGS model its LES used (§II.A).
- **Robustness to numerics.** Bae & Koumoutsakos (2022, pp. 3, 10) claim
  robustness to the discretization because numerical errors enter
  training; the preprint uses one solver and one SGS model (see
  [model-consistent training](/methods/model-consistent-training.md)).

# Citations

- [Beck & Kurz (2023)](/sources/beck-2023.md) — §I (motivation), §II B (MDP, PPO), §III B–C, Eqs. 11–17, Table I, §IV A–B, Eq. 18, §V A–C, Figs. 7–14, App. A, §VI.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II B 4, Eqs. 7–8; §III A–B, Figs. 8–10; §IV C, Eqs. 10–14, Table III; §IV D.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §IV.B (model-consistent training as the class to which in-the-loop optimization belongs).
- [Kim et al. (2022)](/sources/kim-2022.md) — arXiv v2: Abstract; §I (Novati et al. cited); §II B–F, Eqs. 11–25, Algorithm 1 (state, action, reward, truncated return, noise, pretraining, constraints, architecture, cost); §III A–B, Figs. 4–6; §III C, Figs. 7–11; §III D, Figs. 12–13; §III E, Eqs. 27–28, Table IV, Figs. 15–20; §IV; Tables I–III.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Research Square preprint v1: pp. 3–8, Eqs. 1–3, 9–10, Table 1, Figs. 2–7; Discussion pp. 10–11; Methods pp. 11–14, Eqs. 4–8.
- [Kurz et al. (2023)](/sources/kurz-2023.md) — arXiv v2: §1, §2, Eqs. 8–11 (policy gradient, PPO), §3.1–3.5, Table 1–2, Fig. 4, Eqs. 19, 21 (MDP, policy, reward, training), §4.1–4.5, Figs. 5–9 (results, inputs, generalization, cost), §5, App. A (dynamic baseline in DG), footnote 3.
- [Tang et al. (2023)](/sources/tang-2023.md) — arXiv v1: §I (RL closures cited), §II C (RL-trained expression generator), §IV.
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §1 (RL against adjoint training).
- [Vadrot et al. (2023a)](/sources/vadrot-2023.md) — arXiv v3: Abstract; §II.A; §II.B.2–3, Eqs. 3–6, 9–10, Table I, Figs. 2–3; §III.A–B, Figs. 6, 9–10; §IV, Eqs. 12–17, Table III, Figs. 11–12; §V.
- [van Gastelen et al. (2024)](/sources/vangastelen-2024.md) — arXiv v5: §1 (RL as a gradient-free route to stability).
- [Kim et al. (2024)](/sources/kim-2024.md) — §1, §5 (targets unknown for complex geometries).
- [Wu & Lele (2026)](/sources/wu-2026.md) — arXiv v2: §1 (RL closures as solver-specific, transferability and cost).
- [Ihme et al. (2022)](/sources/ihme-2022.md) — §3.4.2, §5 (three obstacles to deep RL); §3.4.3 (Q-learning reactor-control tutorial, combustion control, not a closure).
