---
type: Method
title: "Model-consistent (a posteriori) training of learned closures"
description: "Training a learned closure with the solver in the loop, so the loss is evaluated on the model's own solution: field inversion, FIML, adjoint-based integrated training, differentiable-solver unrolling and reinforcement learning, contrasted with open-loop injection of a priori-trained corrections, with consistency arguments, costs and limits."
status: established
aliases: [a posteriori training, a-posteriori training, solver-in-the-loop training, integrated inference and learning, embedded learning, differentiable-physics training, online learning, CFD-driven machine learning, closed-loop training]
tags: [data-driven, neural-network, sgs-model, rans, les]
timestamp: 2026-10-29T10:10:00Z
---

# Model-consistent (a posteriori) training of learned closures

**Model-consistent training** fits the parameters $\boldsymbol\theta$ of a
learned closure with the closure embedded in the RANS, LES or wall-modelled
solver. The loss $\mathcal L$ compares solver outputs with data, and the
features the closure sees during training are those it sees in prediction.
Duraisamy (2021, §IV.B) defines the class against **a priori training**,
which regresses targets extracted from DNS onto features extracted from DNS
(Eq. 5), and argues that only training inside the model environment removes
the mismatch between learning and prediction. The mechanisms of that
mismatch are listed on
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).
Agdestein & Sanderse (2025) call the same thing "a-posteriori training";
Beck & Kurz (2023) realize it with reinforcement learning.

## The family

Page-local notation: $f(\boldsymbol\zeta;\boldsymbol\theta)$ is the learned
model; $\boldsymbol\zeta_{\mathrm m}$ are features computed from the model's
own solution; $\boldsymbol Y$ are data and $\boldsymbol Y_{\mathrm m}$ the
corresponding model outputs.

**A priori training (the reference point).** In Duraisamy (2021, Eq. 5),
a discrepancy $\boldsymbol\delta$ and features $\boldsymbol\zeta$ are
extracted from DNS, and the training problem is
$\min_{\boldsymbol\theta}\mathcal L[\boldsymbol\delta,f(\boldsymbol\zeta;\boldsymbol\theta)]$.
It is non-intrusive and admits direct physical constraints. Its drawbacks
are that it requires full-field DNS and loses consistency with the solver.

**Open-loop injection of a priori-trained corrections.**
[McConkey et al. (2022)](/sources/mcconkey-2022.md) (§II D, Fig. 7) train
two networks on labels computed from DNS, a non-negative optimal eddy
viscosity and the remaining non-linear part of the anisotropy (see
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)). Their
inputs are features of a converged base RANS solution. The predictions are
then injected once and held fixed while the mean-flow equations are
iterated to convergence around them, with no turbulence transport
equation solved after injection: a "one-time correction" in the term
they cite from Ho & West. The eddy viscosity enters implicitly, as an added
viscosity, and the divergence of the non-linear part explicitly, as a
source. Training is a priori; only the evaluation happens in the solver. Citing
earlier work, the authors state that open-loop frameworks are limited to steady flows, while
iterative frameworks that call the network at every iteration (Liu et al.)
can converge to solutions that depend on the initial field (§II D). The
authors bound what such a framework can reach by a conditioning test that
injects the exact DNS labels (§II C; see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).
[Tang et al. (2023)](/sources/tang-2023.md) (§II D–E) follow the same
pattern with a [symbolic-regression closure](/methods/symbolic-regression-closure.md)
of $k$-$\varepsilon$: the non-linear part of the anisotropy, learned
offline from DNS, is evaluated once on the converged baseline solution
and frozen ("loose coupling"), while the linear eddy-viscosity part is
updated implicitly until the residuals reconverge. They distinguish
"tight coupling", in which the learned term takes part in the RANS
iterations, and do not use it. They cite (§I) the CFD-driven
gene-expression programming of Zhao et al., which evaluates candidate
models in the solver during training; Tang et al. propose coupling their RL-driven
search with RANS as future work (§IV).

**Field inversion, then learning (FIML).** Field inversion is run for each
dataset, and the inferred fields are then regressed onto
$\boldsymbol\zeta_{\mathrm m}$ (Duraisamy 2021, Eqs. 7–8). The targets now
come from the model environment, but the regression step is still separate
from the solver. Duraisamy (2021) says it "promotes" consistency, and
regression errors reintroduce some inconsistency. See
[field inversion and machine learning](/methods/field-inversion-machine-learning.md).
[Yan et al. (2022)](/sources/yan-2022.md) show the effect on the S809
airfoil: across twelve network settings the regression loss and the a
posteriori lift error of the embedded Spalart–Allmaras correction are not
monotonically related (lift error from $-2.0\%$ to $15.1\%$ at $8^\circ$),
which they attribute to inputs the network meets only during the solver's
non-converged iterations (§3.1.2, Table 1). They keep two-step training and
select the network by its a posteriori error: model consistency enters at
model selection, not in the loss.
[Cato et al. (2023)](/sources/cato-2023.md) (§I) give the same rationale
for the two-step procedure: the inversion keeps the learned correction
consistent with the model structure, whereas learning Reynolds stresses
directly from DNS is called potentially "ill-conditioned" (citing
earlier work). Their
study of the inversion step shows that this consistency does not fix the
inferred field. Several of their six correction fields fit the same mean
velocity closely (Tables I–II). Some fits do so with eddy viscosities that "very
strongly overshoot" a DNS-based estimate, which the authors call "a
classical over-learning situation" (§III B, Fig. 6). The field that a
later regression would learn therefore depends on which correction is
inverted (see
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)).

**Integrated (tightly coupled) inference and learning.** The learned map
sits inside the solver constraint, and one optimization over
$\boldsymbol\theta$ minimizes
$\mathcal L[\boldsymbol Y,\boldsymbol Y_{\mathrm m}(f(\boldsymbol\zeta_{\mathrm m};\boldsymbol\theta))]$
subject to the augmented equations (Duraisamy 2021, Eq. 9). The author
states that it "ensures full consistency between the learning and
prediction environments". The review cites as examples embedded neural
networks in RANS (Holland et al.) and the DPM closure for LES (Sirignano,
MacArt & Freund). Its drawback is that features must be fixed before
inference.

**Adjoint-based training of an LES closure (Sirignano & MacArt 2023).**
[Sirignano & MacArt (2023)](/sources/sirignano-2023.md) follow this route
for incompressible LES of bluff-body wakes. A single network
$h_{ij}(\nabla\bar u;\boldsymbol\theta)$ (page-local), fed with the
filtered velocity-gradient tensor, replaces every unclosed term of the
filtered equations (Eq. 2.3):

$$\frac{\partial\bar u_i}{\partial t}=-\frac{\partial\bar p}{\partial x_i}-\frac{\partial\bar u_i\bar u_j}{\partial x_j}+\frac1{Re}\frac{\partial^2\bar u_i}{\partial x_j\partial x_j}-\frac{\partial h_{ij}}{\partial x_j}(\nabla\bar u;\boldsymbol\theta),\qquad\frac{\partial\bar u_k}{\partial x_k}=0,$$

with $Re$ based on the prism height and free-stream velocity. The
network is described on
[neural-network SGS models](/methods/neural-network-sgs-model.md). The
training loop (§2.2) is:

1. choose $N$ windows $[t_n,t_n+\tau_{\mathrm{tr}}]$ with
   $\tau_{\mathrm{tr}}=0.1$ time units (page-local symbol; "only a fraction
   of the mean-flow time scale");
2. start each window from filtered DNS and solve the LES in parallel;
3. evaluate the end-of-window mismatch (Eq. 2.8)
   $$\mathcal L(\boldsymbol\theta)=\sum_{n=1}^{N}\int_\Omega\big\|\bar u^{\boldsymbol\theta}(t_n+\tau_{\mathrm{tr}},\boldsymbol x)-\bar u^{\mathrm{DNS}}(t_n+\tau_{\mathrm{tr}},\boldsymbol x)\big\|\,d\boldsymbol x,$$
   where $\bar u^{\boldsymbol\theta}$ is the LES solution and
   $\bar u^{\mathrm{DNS}}$ the filtered, downsampled DNS;
4. solve $N$ continuous adjoint problems backward over the windows (Eq.
   2.9) and assemble $\nabla_{\boldsymbol\theta}\mathcal L$ as the
   space–time integral of the adjoint velocity times the
   $\boldsymbol\theta$-derivative of the divergence of $h_{ij}$ (Eq. 2.10);
5. update $\boldsymbol\theta$ with RMSprop.

The adjoint system has as many equations as the Navier–Stokes system
(three momentum, one continuity) whatever the size of $\boldsymbol\theta$,
which the authors give as the source of efficiency (§2.2). The adjoint
velocity is the sensitivity of the loss to the solution at each point, so
the optimization "naturally focuses" on the regions that most reduce the
loss. The problem is "highly non-convex". Training is synchronized
distributed RMSprop over "tens to hundreds of GPUs" with MPI; each GPU
holds $M$ forward and adjoint solutions as one tensor (§2.3). Citing
Sirignano, MacArt & Spiliopoulos (2023), the authors state (§2.2) that
global convergence of adjoint-trained network–PDE models is proven, as
hidden units and training time tend to infinity, only for linear PDE
operators.
The authors contrast adjoints with RL: adjoints "utilize the PDEs directly
during gradient calculations", whereas RL depends on the fidelity of the
"agent" to the flow dynamics (§1; see Qualifications).

**Weakly coupled variants.** Embedded learning, iterative machine
learning, CFD-driven machine learning and closed-loop training move toward
model consistency without adjoints, though some still need full-field DNS
(Duraisamy 2021, §IV.B).

**CFD-driven symbolic regression in turbomachinery.** Sandberg &
Michelassi (2022, §4.3) cite the CFD-driven machine learning of Zhao
et al. (2020) as gene-expression programming whose cost function is
evaluated on the RANS solution of each candidate model: it needs only
selected profiles of one variable, "the model is being used for its
ultimate, a posteriori predictive purpose", and its cost becomes limiting
for URANS and complex configurations. Models trained this way on
high-pressure-turbine data predicted the wake-loss profiles of
low-pressure turbines of other geometries at very different Reynolds
numbers. The same review gives the consistency argument for field
inversion, citing Parneix et al. (1998) and Wu et al. (2019): even the
true DNS Reynolds stress used in RANS does not guarantee an accurate mean
flow and can jeopardize robustness (§4.3; see
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)
and [symbolic-regression closures](/methods/symbolic-regression-closure.md)).

**A taxonomy of RANS frameworks (Sandberg & Zhao 2022).**
[Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) (§3.4), a review of
learned stress and heat-flux closures, largely of the authors' own
group, among them CFD-driven training, attribute the term "model-consistent" to Parish &
Duraisamy (2016) and list the frameworks that pursue it:

- **FIML and its advanced, simultaneous form** (Holland et al. 2019, as
  cited), costly for complex 3-D flows (see
  [field inversion and machine learning](/methods/field-inversion-machine-learning.md));
- **closed-loop feature consistency** (Taghizadeh et al. 2020, as cited):
  open-loop training is inconsistent at two levels, because the closure
  coefficients that generated the features differ from the trained ones
  and the transport-equation coefficients were calibrated with the
  original closure; the transport coefficients are iterated until
  consistent;
- **implicit treatment of the linear part** (Wu et al. 2018, as cited):
  an optimal eddy viscosity enters implicitly and the non-linear remainder
  is trained separately, against the ill-conditioning shown by Wu et al.
  (2019);
- **machine learning in the RANS loop** (Liu et al. 2021, as cited): a
  regressor called at every RANS iteration supplies an eddy viscosity for
  which the solver converges to the DNS velocity and pressure; trained on
  channel flow and tested on periodic hills, its gain was smaller than that
  of non-linear approaches, "presumably as only the linear part … was
  used";
- **CFD-driven machine learning** (Zhao et al. 2020, as cited): every
  candidate closure of a gene-expression-programming population is run in
  RANS and scored on quantities of interest, e.g. the mean squared
  wall-temperature error of a cooling flow (Eq. 11). Its stated
  advantages are much less training data (selected profiles, usable with
  experiments at conditions that DNS or LES cannot reach), exclusion of
  non-converging candidates during training, and a model already tested a
  posteriori when training ends; its drawback is a "dramatically higher"
  development cost, "currently intractable" for complex 3-D flows (§3.4,
  §4.1). Multi-expression, multi-objective training (Waschkowski et al.
  2022, as cited) trains a stress and a heat-flux closure together and
  keeps a Pareto front of the velocity and temperature errors (Eq. 17)
  instead of a weighted sum, which the authors call "at best an ad hoc
  process" (§4.5);
- **SpaRTA** (Schmelzer et al. 2020, as cited): sparse regression of
  candidate functions in which cross-validation ranking in the solver is
  the only expensive step (see
  [symbolic-regression closures](/methods/symbolic-regression-closure.md)).

**Frozen targets made consistent, solver only for selection (Cherroud et
al. 2022).** [Cherroud et al. (2022)](/sources/cherroud-2022.md) (§2.1)
extract their targets by the $k$-corrective-frozen procedure of Schmelzer
et al. (2020a), as they cite it: the $k$ and $\omega$ equations of
[$k$-$\omega$ SST](/methods/k-omega-sst-model.md) are solved with the
high-fidelity mean velocity, $k$ and anisotropy frozen, so that only
$\omega$ evolves, and the residual left in the $k$ equation becomes the
target of a production correction (Eqs. 10–12). They argue that
correcting the eddy viscosity and time scale indirectly through the
transport equations favours models consistent with the RANS solver and
reduces the propagation errors caused by ill-conditioning (citing Wu et
al. 2019), without putting the solver in the training loop. The solver
enters only in the a posteriori cross-validation that picks the sparsity
parameter (§4.2, Table 2; see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

**Unrolled differentiable solver.** Agdestein & Sanderse (2025, §4.3,
Eq. 25) minimize a trajectory loss: the relative error between the LES
solution and the filtered DNS, averaged over $n_{\mathrm{unroll}}=50$ time
steps that start from the same filtered state. Gradients come from
reverse-mode automatic differentiation through the unrolled LES (Zygote.jl).
An explicit Runge–Kutta integrator was chosen because it is easier to
differentiate (§2.4). The authors cite unroll lengths of 30–60 (List et al., 2D incompressible flow), 32 (Kochkov et al.), and 30
(good) versus 120 (poor) for Kuramoto–Sivashinsky (Melchers et al.).
[van Gastelen et al. (2024)](/sources/vangastelen-2024.md) (§3.4, Eqs.
51–52, App. E.2) combine the two losses for 1D Burgers and
Korteweg–de Vries closures: 100 iterations of "derivative fitting" (the
closure's right-hand side against the filtered fine-grid right-hand
side), then 20 of "trajectory fitting" (unrolled coarse solutions against
filtered fine-grid trajectories, 5 steps of $0.01$ for Burgers and 20
steps of $5\times10^{-3}$ for KdV), because trajectory fitting is the more
expensive. Derivative fitting alone left a vanilla convolutional closure
unstable and inaccurate, "especially in the KdV case", while their
energy-conserving closure was already reasonable with it (§4.2; see
[neural-network SGS models](/methods/neural-network-sgs-model.md)).
[Bezgin et al. (2025)](/sources/bezgin-2025.md) (§4.2, Eqs. 41–42,
Fig. 6) train a learned discretization rather than a closure: the networks
that weight the candidate polynomials of a TENO6-A reconstruction in an
[implicit LES](/definitions/implicit-les.md) of compressible decaying
isotropic turbulence. The fully differentiable solver JAX-Fluids is
unrolled for $N_T\in\{1,2,5\}$ coarse time steps (three Runge–Kutta
stages each; $N_T$ page-local) from a filtered-DNS state, the loss is the
cell-wise mean absolute error of density, velocity, pressure and
temperature against filtered DNS, each normalized by its initial
reference value, and the gradient comes from automatic differentiation
(Adam, learning rate $10^{-4}$, batches of 24 samples, 50 epochs, single
precision). The authors call end-to-end optimization "essential" for
discretization learning because "there is no a priori knowledge" of the
optimal discretization, only of the optimal solution trajectory, and
state that it improves inference stability because the gradients carry
the PDE dynamics and the model observes its own error accumulation; the
framework needs no derivation of adjoint equations (§4.2).

**Variational inference through an adjoint RANS solver.**
[Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) train a
[tensor-basis neural network](/methods/tensor-basis-neural-network.md)
together with a stochastic Reynolds-stress discrepancy on indirect data,
sparse LES mean velocity and pressure, which they call "model-consistent"
learning after Duraisamy (2021) and "trajectory regression" after their
ref. [64] (§1, §2.2). The loss is the evidence lower bound of a Bayesian
posterior; each iteration draws $K=5$ discrepancy samples, solves the
discrete RANS equations for each, and back-propagates the log-likelihood
through a discrete adjoint of the FEniCS solver coupled to PyTorch
autograd via Pyro (Algorithm 1, App. B, Eqs. B.1–B.12). The learning rate
is $10^{-6}$, "relatively small … due to the Monte Carlo noise" (§3.3). A
randomly initialized network "led to divergence of the solution even
after applying the stabilization schemes", so the network was first
pre-trained on baseline $k$-$\varepsilon$ closure data with added noise
(§3.3). See [model-form uncertainty](/definitions/model-form-uncertainty.md).

**Ensemble (derivative-free) calibration.**
[Wang et al. (2023c)](/sources/wang-2023-c.md) calibrate the one
functional coefficient of a mixed SGS model inside the LES with an
ensemble Kalman filter: an ensemble of LES runs, each with its own
coefficient, restarted from the same filtered-DNS field, is updated toward
the filtered-DNS energy spectra (§II.B; see
[ensemble Kalman calibration](/methods/ensemble-kalman-closure-calibration.md)).
No solver gradient is needed. They call the method "numerically more
convenient" than adjoint-based variational calibration, note that finite
differences would also serve for a single parameter, and expect the
ensemble method to pay off in high-dimensional problems (§V).

**Reinforcement learning.** Beck & Kurz (2023) pose the choice of closure
parameters as a Markov decision process. The LES with its actual
discretization is the environment, and the reward is computed from the LES
energy spectrum, so no gradient of the solver is needed.
[Kurz et al. (2023)](/sources/kurz-2023.md), the precursor of that
work, make the point explicit: the sample estimate of the policy gradient
(their Eq. 8) contains no term of the environment dynamics, so the
solver is never differentiated, and the implicit filter of the DG-LES is
"incorporated" into training by design (§2, §1). Vadrot et al.
(2023b, §II B 4) describe a wall model trained the same way in WMLES
without high-fidelity data. Its authors, [Bae & Koumoutsakos (2022)](/sources/bae-2022.md)
(preprint, pp. 3, 8, 10), give the consistency argument for wall models:
the agents are the computational elements, their actions compensate both
the closure and the solver's numerical errors, and the resulting models
are "robust with respect to the numerical discretizations, as these
errors are taken into consideration in the training process". The reward
uses only the true mean wall stress, so the training needs no DNS field,
and the states (velocity, its wall-normal gradient, wall distance) "do not
depend heavily on numerics or SGS models", unlike the filtered velocities
of a dynamic wall model.
[Kim et al. (2022)](/sources/kim-2022.md) train a pointwise SGS stress
network for channel LES in the same way. The reward compares two mean
profiles of the running LES (mean viscous stress and resolved Reynolds
shear stress) with filtered DNS, so no filtered-DNS fields are stored.
Because training and testing happen in the same LES, the authors argue
that the a priori/a posteriori gap of supervised SGS learning is removed
by construction (Abstract, §I, §III C). They contrast the approach with
differentiable-PDE training (Sirignano et al., MacArt et al., among
others). That route needs a differentiable solver and the storage of "all
three-dimensional flow data", but they credit it with guaranteeing
"robust performance, being superior to a standard supervised learning",
and they call for a quantitative comparison of the two (§IV). See
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md).

## Aligning the objective with deployment (Hu & Yang 2026)

[Hu & Yang (2026)](/sources/hu-2026.md) build their review of
machine-learning closures for RANS, LES and PINNs on one thesis. Learned
closures are trained on a pointwise, offline objective, but they must work
coupled to a solver, across many scales and in a statistically stationary
state. The remedies that work in each "pillar" share one design rule:
align the training objective with deployment (§I, Fig. 2, §III D, §VIII).
The authors label the attribution of the failure modes to this one root
"the interpretive synthesis proposed by this review, not an established
conclusion of the field". They identify model-consistent training, in
the sense of [Duraisamy (2021)](/sources/duraisamy-2021.md), as the key
determinant of robust a posteriori performance (§IV A).

**Remedies grouped under the rule.** All works below are cited by Hu &
Yang (2026); none is ingested here unless linked.

- *RANS (§III B, §VII C).* Corrective targets: scalar multipliers on the
  eddy viscosity or on the production, which the authors read as
  projecting the learned object onto a one-dimensional subspace the
  solver tolerates. The Reynolds force vector (the divergence of
  $R_{ij}$, Cruz et al.) as the learning target. CFD-driven training on
  several flows at once (Fang et al., a pool of ten cases). Online RANS
  optimization with embedded DNS (oRANS, Dehtyriov et al., preprint).
  Transport-equation corrections (Wu et al., nonlocal effects). Iterative
  coupling with under-relaxation, and non-linear super-stencils (Luther &
  Jenny). The listed RANS mitigations answer the ill-conditioning of the
  mean-momentum operator; see
  [tensor-basis neural network](/methods/tensor-basis-neural-network.md)
  and [field inversion and machine learning](/methods/field-inversion-machine-learning.md).
- *LES (§IV A).* Dissipativity constraints (non-negative $\nu_t$, or
  blending with a classical model), statistical or spectral losses,
  solver-in-the-loop training, and adaptive hybrid closures. The
  solver-in-the-loop entries are adjoint-based embedded training
  (Sirignano et al.; MacArt et al.) and PDE-constrained optimization
  through a differentiable solver (Shankar et al.). Hu & Yang report from
  Sirignano et al. that the same network trained purely a priori is
  "unusable a posteriori". The adjoint-trained network of
  [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) above
  is the same comparison on bluff-body wakes.
- *PINNs (§V A–B).* Causal training, weak-form losses and
  physics-informed neural operators; see
  [physics-informed neural networks](/methods/physics-informed-neural-network.md).

**Three degrees of coupling (§V C).** Hu & Yang order hybrid
machine-learning–solver couplings by how deeply the network enters the
solver:

| Coupling | What is learned | Example, as cited by Hu & Yang |
|---|---|---|
| Learned discretization | the coefficients of the numerical scheme | Bar-Sinai et al. |
| Solver in the loop | a correction trained through an unrolled solver | Um et al. |
| End-to-end differentiable CFD | the whole coarse-grid solver, trained through | Kochkov et al., high-resolution accuracy on grids "an order of magnitude coarser" |

They state that tighter coupling gives stronger a posteriori performance
at a higher training cost. The learned TENO weights of
[Bezgin et al. (2025)](/sources/bezgin-2025.md) above are a learned
discretization trained through an unrolled solver.

**The resolution-handoff bottleneck (§V C 4).** The authors ask where, in
scale and in space, the solver should hand the dynamics over to the
learned component. In Kochkov et al. the handoff is set implicitly by the
coarse grid. In oRANS it is spatial and explicit, an embedded DNS
subdomain. There, accuracy degrades when the interface is mishandled
("boundary-condition contamination") or when the embedded region is too
short to capture the relevant low-wavenumber modes. They link the
question to the grey area of
[detached-eddy simulation](/methods/detached-eddy-simulation.md) and cite
as a first step the learned RANS/LES switching coefficients of an
explicit-algebraic-stress DES (Liu et al.). Non-zonal, learned placement
of the crossover is, they state, open (see
[hybrid RANS/LES](/definitions/hybrid-rans-les.md)).

**Generalization, data and benchmarks (§VII).** Hu & Yang cite the
finding of Mandler & Weigand (2025): a data-driven eddy-viscosity
augmentation tailored to one phenomenon loses generality, and systematic
data mismatch, not extrapolation, dominates the generalization error.
They accept it within that model class and name three loopholes. First,
anisotropy and transport-equation closures leave the class. Second, the
learned object can be changed (the Reynolds force vector, multiplicative
corrections). Third, the result covers offline a priori training, not
CFD-driven or solver-in-the-loop training (§VII A). From the same
diagnosis they conclude that "a modest, well-chosen dataset consumed by
model-consistent or solver-in-the-loop training can outperform a far
larger one used for naive a priori regression" (§VII D). They also argue
that benchmarks ranking models only by mean-field $L_2$ error "would
reward exactly the objective–deployment mismatch" (§VII E; see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).
Their Table II rates the CFD-driven and online family qualitatively:
about 5–10 coupled training cases, a posteriori robustness "High",
interpretability "Medium". The authors call the table "a reader's guide
rather than a rigorous benchmark".

## Evidence

- **Decaying isotropic turbulence.** Duraisamy (2021, §IV.B, Fig. 2)
  shows, from Sirignano et al., that an a priori-trained SGS closure
  overpredicts the resolved kinetic energy over the plotted interval. The
  model-consistent DPM closure follows the filtered DNS.
- **Bluff-body wakes, same network trained both ways.** Sirignano & MacArt
  (2023, §5, Figs. 11–12) train their network a priori on the filtered-DNS
  subgrid stress and by adjoints, for a square prism at $Re=1000$. The a
  priori fit is "almost perfect"; in the LES the adjoint-trained network
  "substantially outperforms" it for all flow statistics, on the training
  case itself.
- **Short windows, long-time statistics.** The adjoint-trained models see
  only windows of 0.1 time units, with no guarantee of stability as
  $t\to\infty$, yet run stably for "several thousand time units" on grids
  with 1/64 or 1/512 of the DNS points (Sirignano & MacArt 2023, §2.2,
  §3.2). Their drag coefficients on four rectangular prisms (aspect ratios
  1, 2, 4; $Re=1000$ or 2000) are, against filtered DNS (Table 2):

  | Case | filtered DNS | no model | dynamic Smagorinsky | AMD | DL-AR1 | DL-AR2 |
  |---|---|---|---|---|---|---|
  | AR1, $Re=1000$ | 2.45 | 1.88 | 2.15 | 2.53 | 2.43 | 2.51 |
  | AR2, $Re=1000$ | 1.94 | 1.61 | 1.65 | 1.96 | 1.90 | 1.95 |
  | AR2, $Re=2000$ | 2.09 | 1.62 | 1.68 | 1.89 | 1.84 | 1.96 |
  | AR4, $Re=1000$ | 1.61 | 1.53 | 1.54 | 1.67 | 1.54 | 1.61 |

  DL-AR1 is trained on the first case, DL-AR2 on the third; AMD is the
  [anisotropic minimum-dissipation model](/methods/anisotropic-minimum-dissipation-model.md).
  The authors summarize that the learned models "consistently perform as
  well or better" than dynamic Smagorinsky and AMD, AMD being outperformed
  "by the in-sample or nearest DL model" (§4.1). By the table, DL-AR1 is
  less accurate than AMD on every case except its training case AR1, and
  on each of those three cases DL-AR2 is the more accurate one *(compiler
  check, not in the sources)*. Both learned models also run in a second solver on an
  equilateral triangular prism and a circular cylinder never seen in
  training; for the cylinder they "suppress all artificial primary
  recirculation", as DNS does, while no-model LES and AMD predict two
  recirculation regions (§6, Figs. 13–14).
- **Isotropic turbulence with RL in DG.** Kurz et al. (2023, §4.2, Fig. 6)
  train on episodes of 5 time units and test from an unseen state to
  $t=20$: the RL models stay stable over four times the training horizon,
  beat no-model LES and static Smagorinsky ($C_s=0.17$), match the dynamic
  model and beat it at the coarsest resolution (24 DOF per direction). See
  [reinforcement-learning closures](/methods/reinforcement-learning-closure.md).
- **2D Kolmogorov-forced turbulence.** Agdestein & Sanderse (2025,
  §5.2.2–5.2.3, Figs. 11–12) run DNS on $4096^2$ points at $Re=6000$ and
  LES on $\bar n\in\{32,\dots,256\}$ points per direction.
  - A posteriori fine-tuning lets a CNN trained with the
    non-divergence-consistent volume-averaging filter catch up with the
    face-averaging one.
  - In the divergence-inconsistent LES formulation, it reduces the error
    but does not remove the instability: the energy eventually grows.
  - Where the a priori-trained model was already stable (divergence-consistent
    formulation with face averaging), fine-tuning improves accuracy only
    slightly.
  See [divergence-consistent LES](/methods/divergence-consistent-les.md).
- **Smagorinsky coefficient fitted a posteriori.** Agdestein & Sanderse
  (2025, App. B.5, Table B.5) choose $C_s$ by grid search on the a
  posteriori training error. The values decrease with resolution, from
  0.129–0.144 at $\bar n=32$ to 0.000 (divergence-inconsistent) and
  0.014–0.023 (divergence-consistent) at $\bar n=256$. These are fitted 2D
  values, not model constants.
- **Discretization-specific coefficients.** Beck & Kurz (2023, §V) find
  that RL-optimized element-local Smagorinsky coefficients outperform the
  dynamic Smagorinsky model for $N=5$ and $N=8$ in forced isotropic
  turbulence (no-model LES stays best at $N=3$), and read this as support
  for considering closure and discretization jointly
  (see [discretization-consistent closure](/definitions/discretization-consistent-closure.md)).
- **Wall-resolved channel LES from mean profiles.** Kim et al. (2022, §III
  C) train at $Re_\tau=180$ on $(\Delta x^+,\Delta z^+)=(70.7,35.3)$. The
  trained tensor models reproduce the filtered-DNS mean velocity and
  Reynolds shear stress almost exactly. They also improve unrewarded
  statistics (rms velocities, mean SGS shear stress and transport, spectra)
  over the static Vreman, dynamic Smagorinsky and no-model LES. They cite
  a supervised network with the same local inputs (Park & Choi 2021) that
  "did not predict" the two target profiles well a posteriori (§III C).
- **One coefficient, calibrated in the LES.** Wang et al. (2023c, §III–IV,
  Figs. 3–17) obtain a functional coefficient $C_{\mathrm f}\approx0.00738$
  (page-local, the paper's $C_D$, which it identifies with $2C_s^2$, §III;
  as on [ensemble Kalman calibration](/methods/ensemble-kalman-closure-calibration.md)) in forced isotropic
  turbulence at
  $Re_\lambda\approx160$ and $C_{\mathrm f}\approx0.01$ in a temporal mixing layer.
  With these values the mixed model is closer to filtered DNS than the
  dynamic Smagorinsky, dynamic mixed and pure gradient models in spectra,
  kinetic energy, PDFs, structure functions and, in the mixing layer,
  momentum-thickness growth. The coefficient calibrated at
  $Re_\lambda\approx160$ also does better than those models at
  $Re_\lambda\approx259$, at twice the filter width and in decaying
  turbulence (App. B); the mixing layer was recalibrated.
- **Stability without accuracy loss in 1D.** van Gastelen et al. (2024,
  §4.3–4.4, Figs. 7–8) train ten replicas per method that differ only in
  the random seed. All energy-conserving models give only stable runs and
  nearly overlapping errors; the vanilla convolutional closures, trained
  with the same hybrid loss, are "hit or miss", two of them 100% unstable
  on the Burgers inflow–outflow case. In accuracy the two are roughly on
  par, the vanilla network being better on KdV at most resolutions.
- **Open-loop RANS correction trained a priori.** McConkey et al. (2022,
  §IV B, Fig. 21) inject the predictions of their DNS-trained networks into
  a $v^2$-$f$-type RANS on a held-out periodic hill. The reattachment-point
  error falls from 20% (base model) to 8.9%. The velocity error is smaller
  than the error of the injected closure term (Fig. 20), so "under certain
  conditions, the RANS equations can suppress rather than amplify errors in
  the closure prediction" (§IV B, §V). This is an a posteriori improvement
  from a priori training, shown for one geometry family in interpolation.
- **CFD-driven against frozen training in turbomachinery and cooling
  flows**, as Sandberg & Zhao (2022) cite them:
  - CFD-driven gene-expression models of high- and low-pressure-turbine
    wake mixing were simpler than frozen-trained ones and improved the
    wake profiles in every a posteriori test on other geometries, the
    gain coming "predominantly" from increased diffusion (§4.1);
  - the first CFD-driven heat-flux training (Lav et al. 2021) worked best
    with the wall temperature in the cost; a model trained at blowing ratio
    1.26 predicted a mean turbulent Prandtl number of 0.32 and performed
    well at two other blowing ratios, and training on several blowing
    ratios at once generalized better (§4.2.1);
  - a frozen-trained closure of the stochastic stress and heat flux in
    URANS of a trailing-edge slot (Lav & Sandberg 2020) improved the
    adiabatic effectiveness at blowing ratio 0.86 only up to $x/s=20$ ($s$
    the lip thickness, page-local), which the review attributes to the
    frozen, not model-consistent, training (§4.4.2, Fig. 11);
  - multi-objective training of coupled stress and heat-flux closures
    improved both mean velocity and temperature of vertical natural
    convection over the baseline and over separately trained models
    (§4.5, Figs. 12–13).
- **Unroll length against long-time statistics.** In Bezgin et al.
  (2025, §5.1–5.2, Tables 2–3), on $32^3$ cells at turbulent Mach numbers
  0.4, 0.6 and 0.8, each unroll length gives the lowest cell-wise error
  at its own horizon over 1 to 20 steps from unseen states, the $N_T=5$
  model at 5, 10 and 20 steps; over the full decay ($t\in[0,10\tau]$,
  $\tau$ the Taylor time scale) the $N_T=1$ model has the lowest spectral
  error at all three Mach numbers (mean absolute log-spectrum error
  0.8849, 0.7923, 0.6178, against 1.110, 1.153, 1.173 for TENO6-A) and the
  $N_T=5$ model the highest (1.480, 1.562, 1.428). The authors conclude
  that "the cell-wise error … does not necessarily correspond to good
  spectral properties during the decay" (§5.2); the comparison is on
  [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).
  For comparison, the unroll lengths cited by Agdestein & Sanderse
  (above) for Kuramoto–Sivashinsky are 30 steps (good) against 120
  (poor), in a different system and metric.
- **Sparse Bayesian closures selected in the solver.** Cherroud et al.
  (2022, §4.2, Fig. 5, App. C) find the selected single-term production
  corrections nearly as robust and cheap as SST and clearly better in
  velocity on three separated flows, and better than the physics-based
  BSL-EARSM of Menter et al. (2012) in OpenFOAM (see
  [explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md)).

## Costs

| Source | Training | Cost reported |
|---|---|---|
| Agdestein & Sanderse (2025, §5.2.7, Table 3) | a priori, $10^4$ iterations | 160.6 s ($\bar n=32$) to 1583.6 s ($\bar n=256$), one H100 GPU |
| Agdestein & Sanderse (2025, §5.2.7, Table 3) | a posteriori, 1000 iterations | 4449.3–5849.2 s, one H100 GPU |
| Agdestein & Sanderse (2025, §5.2.7) | DNS and filtering of all data | $1.5739\times10^4$ s |
| Beck & Kurz (2023, §IV B) | 2000 iterations of 16 parallel episodes | at most 0.8 CPU-hours per LES; 8 or 16 cores per LES |
| Vadrot et al. (2023b, §IV D) | RL wall model of Bae & Koumoutsakos | about $10^7$ gradient steps (cited) |
| Bae & Koumoutsakos (2022, preprint pp. 8, 12–13) | multi-agent RL in WMLES, $10^7$ policy-gradient steps | $O(10^3)$ CPU-hours and under 1 GB at $Re_\tau=4200$, against $O(10^7)$ CPU-hours and over 100 TB to generate DNS data for supervised training (no hardware given) |
| Kim et al. (2022, §II F) | DRL of a pointwise SGS network in channel LES, 10,000–15,000 iterations, eight parallel LES; supervised pretraining of 50,000 iterations | about 2–4 days on one NVIDIA Titan Xp GPU; pretraining "only a few minutes" |
| Kurz et al. (2023, §4.1) | PPO of an element-local Smagorinsky coefficient in DG-LES, 16 or 32 episodes per update | 1 day (smallest) to 5 days (largest case) on HAWK, up to 1024 CPU cores for the LES plus one GPU node for the policy |
| Sirignano & MacArt (2023, §2.3) | adjoint-based training, distributed RMSprop | "tens to hundreds of GPUs"; no timing given |
| van Gastelen et al. (2024, §4.3.2) | hybrid derivative and trajectory fitting of a 1D convolutional closure | about 20 min per network; each training DNS at most 5 s on a laptop CPU |
| Agrawal & Koutsourelakis (2024, §3.4, Table 4) | variational inference through an adjoint FE RANS solver (for prediction cost) | one prediction run 1.3 times a baseline $k$-$\varepsilon$ run; the reference LES 7679 times; no training time given |
| Tang et al. (2023, §III B) | a priori symbolic regression with an RL-trained expression generator (for contrast) | about 100 h on 20 cores (Intel Xeon E5-2650) |

[Xiao et al. (2025)](/sources/xiao-2025.md) (§1) give the cost argument
from the solver side: model-consistent and reinforcement-learning training
of SGS and wall models (they cite Duraisamy for the term) needs "hundreds
or even thousands" of LES runs, which is their motivation for the GPU
solver [CaLES](/software/cales.md); one A100 is 12 to 19 times faster than
a full 32-core CPU node in their channel benchmark (§3.2, Fig. 2). They train no model (see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

Duraisamy (2021, §IV.B) names the obstacles to adjoint-based integrated
training. Adjoints are intrusive. In LES the chaotic dynamics can make
adjoint solutions unstable, which requires shadowing-type treatments. Both
the convergence of these training methods and the choice of loss function
"has not been studied in earnest".

## Qualifications

- **Consistency is not generalization.** Duraisamy (2021, §VII) states
  that ML-augmented models have improved predictions on training cases and
  closely related ones, but that "the goal of more generalizable models
  has, however, not been achieved". Training in the model environment also
  ties the closure to that environment. Beck & Kurz (2023, §VI) present
  their trained models as a way of developing discretization-specific
  closures, not as ready-to-use ones. Agdestein & Sanderse (2025, §5.2.7)
  keep one parameter set per grid, filter and formulation. Kim et al.
  (2022, §III D) show the same limit for an RL-trained SGS model: trained
  at $Re_\tau=180$, it gives reasonable Reynolds shear stress at untrained
  $Re_\tau$ but fails on an untrained coarser grid, and the authors
  conclude that "a model trained in a single environment might not perform
  well in a different environment". Sirignano & MacArt (2023, §4, §6)
  report the other side for adjoint training: models trained on one prism
  and one Reynolds number stay stable, and are often the most accurate, on
  other aspect ratios, the other Reynolds number, two unseen geometries and
  a second solver, all at $Re\le2000$; a test at $Re=12\,000$ is
  mentioned as "stable and, in some cases, accurate" but not shown (§7).
- **Statistics as targets leave the closure under-determined.** Kim et al.
  (2022, §III C) find that models trained to the same two mean profiles
  give different mean SGS dissipation. Cato et al. (2023, §III B, §V C)
  find, for inversions on mean velocity, that an accurate mean flow can
  come with wrong Reynolds stresses or overshooting eddy viscosity.
- **Robustness to the discretization is claimed, not tested.** Bae &
  Koumoutsakos (2022) train and test their wall models with one solver
  (staggered second-order finite differences) and one SGS model
  (anisotropic minimum dissipation); the robustness to numerics they
  claim (pp. 3, 10) is not tested with another solver or SGS model. Beck & Kurz
  (2023, §VI), who also train in the loop, present their SGS closures as
  discretization-specific rather than transferable.
- **"No reference data" is relative.** The reward of Bae & Koumoutsakos
  (2022, Eq. 9) contains the true mean wall stress at each training
  $Re_\tau$ (2000, 4200, 8000); the preprint does not say where those
  values come from. In-solver training removes the need for full DNS
  fields, not for reference statistics.
- **Extrapolation.** Vadrot et al. (2023b, §III A, §IV C, Table III) test
  the RL wall model, trained at $Re_\tau=2000$, 4200 and 8000, from
  $Re_\tau=180$ to $10^{10}$. They find a log-layer mismatch of $+1.5$ to
  $+2.0$ inner units for $Re_\tau$ from $2\times10^3$ to $10^4$, $+1.0$ at
  $10^5$, and $-2.2$ to $-3.2$ for $Re_\tau\ge10^7$, i.e. errors both near
  and far beyond the training range (see
  [machine-learning wall models](/methods/machine-learning-wall-model.md)).
  Bae & Koumoutsakos (2022, preprint p. 6, Figs. 3–4) report for their own
  log-law model a friction-velocity error below 5% from $Re_\tau=5200$ to
  $10^6$. The two assessments differ in solver, grid and error measure;
  the side-by-side record is on
  [machine-learning wall models](/methods/machine-learning-wall-model.md).
- **Identifiability.** Duraisamy (2021, §VII, Fig. 4) shows an anisotropy
  perturbation inferred from mean-velocity data in channel flow that
  reproduces the mean velocity and shear stress but not the anisotropy, and
  states that the full Reynolds-stress tensor as data would remedy it.
- **Error ambiguity in LES.** Model-consistent training absorbs numerical
  error into the closure. Duraisamy (2021, §VII) notes that this accounts
  for numerical errors "at least as far as reconstructing the training
  data is concerned". Disambiguating numerical from modelling error
  remains hard without explicit filtering, and possibly even with it.
- **Adjoints against RL, as characterized.** Sirignano & MacArt (2023, §1)
  write that RL "typically approximates the flow dynamics using a DNN
  model", so its consistency depends on the fidelity of the agent, and add
  that "model-free reinforcement learning can also be used" (citing
  Pino et al. 2023). In the RL closures of this bundle the
  environment is the running LES or WMLES itself, not a network model of
  the flow (Beck & Kurz 2023, §II B; Kurz et al. 2023, §2, Eq. 8; Kim et
  al. 2022, §II; Bae & Koumoutsakos 2022, pp. 3–4). No source compares the
  two routes on one case; Kim et al. (2022, §IV) call for such a
  comparison.
- **Cost of adjoint training is not reported.** Sirignano & MacArt (2023)
  give hardware ("tens to hundreds of GPUs") but no training time, and
  their training needs filtered DNS fields at the start and end of every
  window. The rewards of the RL closures use only statistics (Kurz et al.
  2023, §3.5; Kim et al. 2022), although Kurz et al. start their training
  episodes from DNS fields projected onto the LES grid (§3.5).
- **Targets that complex flows do not provide.** Kim et al. (2024, §1,
  §5), who train their cylinder-wake networks a priori, state that their
  models do not remove the a priori/a posteriori inconsistency, and argue
  that the adjoint route (Sirignano et al.) and the RL route (Kim et al.
  2022) need target statistics that are "unknown a priori" for complex
  geometries. The RL wall model of Vadrot et al. (2023a, §II.B.2–3) takes
  as target the true mean wall stress, "obtained from the equations of
  motion for an unidirectional mean flow" (after Eq. 4).
- **Differentiable RANS solvers.** Agrawal & Koutsourelakis (2024, §1)
  state that a differentiable RANS solver in an automatic-differentiation
  framework "has not been accomplished yet" to their knowledge, and use an
  adjoint instead; they cite in the same paper Ströfer & Xiao's
  "end-to-end differentiable" learning with adjoints. The statement names
  automatic differentiation of the whole solver; adjoint-based training
  also appears in Yan et al. (2022) and Sirignano & MacArt (2023)
  (sections above).
- **The case against binding the closure to the solver.**
  [Wu & Lele (2026)](/sources/wu-2026.md) (arXiv v2, §1) argue that
  end-to-end training through a differentiable solver (Sirignano & MacArt
  2023; Duraisamy 2021; a differentiable-physics closure on unstructured
  grids by Kim, Shankar, Viswanathan & Maulik, preprint, as they cite it),
  "can suffer similar issues" as reinforcement learning, whose models are "limited in their transferability to other solvers, as they learn the combined effect of solver-specific numerical effects and turbulence physics": the end-to-end network "is also unlikely to transfer directly to different flow solvers", and that it costs more because the
  LES must run during training. They train supervised instead, on DNS
  filtered with several filter shapes, and run one network in two solvers
  without retraining (§5.2.1, §7; see
  [neural-network SGS models](/methods/neural-network-sgs-model.md) and
  [discretization-consistent closure](/definitions/discretization-consistent-closure.md)).
  The non-transferability is stated, not tested; Sirignano & MacArt
  (2023, §6) report a partial transfer to a second solver (above).
- **The review's evidence is cited.** Sandberg & Zhao (2022) present
  no new computation beyond a jet-in-crossflow illustration; the results
  above are those of the cited works, mostly the authors' own group, shown
  through reproduced figures. They attribute the downstream weakness of
  the trailing-edge closure to the frozen training without a comparison
  run, and write that the nearly perfect effectiveness at the training
  blowing ratio "might be fortuitous" since the velocity profiles do not
  match closely (§4.4.2).
- **Noise.** Agdestein & Sanderse (2025, §6) report that adding noise to
  the training data, a common stabilizer, can destroy the divergence-free
  property. Validation errors were better without noise; no data are
  shown.
- **Printed slips in Hu & Yang (2026).** In Table II the inference-cost
  cell of the CFD-driven and online family reads "Medium/low", while the
  caption says these methods "incur medium training but low inference
  cost"; the caption of the same table refers to "Tables 1 and 3" for the
  paper's Tables I and III.
- **A review's ratings.** Hu & Yang (2026) present no new computation;
  they call their Table II, with its robustness and interpretability
  grades, "a reader's guide rather than a rigorous benchmark".

# Citations

- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §IV.A, Eq. 5; §IV.B, Eqs. 7–9 (FI, FIML, integrated training, weakly coupled variants, adjoints, Fig. 2); §VII (generalization, identifiability, numerical error).
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §2.4, §4.3, Eq. 25 (trajectory loss, unrolling), §5.2.2–§5.2.7, Figs. 11–12, Table 3; §6; App. B.5, Table B.5.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §I, §IV B (RL in the loop, training cost), §V, §VI.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II B 4, §III A, §IV C, Table III, §IV D.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Research Square preprint v1, pp. 3, 6, 8, 10 (consistency argument, cost, states), Eq. 9 (reward), Methods pp. 12–13 (training).
- [Yan et al. (2022)](/sources/yan-2022.md) — accepted manuscript, §3.1.2, Table 1 (regression loss against a posteriori error; selection by a posteriori error).
- [Kim et al. (2022)](/sources/kim-2022.md) — arXiv v2: Abstract, §I, §II F (cost), §III C–E (results, comparison with supervised learning, non-unique SGS dissipation, generalization), §IV (differentiable-PDE training).
- [Cato et al. (2023)](/sources/cato-2023.md) — HAL author manuscript: §I (two-step FIML rationale), §III B, Fig. 6 (over-learning), §V C (mean flow without the right stresses).
- [McConkey et al. (2022)](/sources/mcconkey-2022.md) — arXiv v1: §II C–D, Fig. 7 (conditioning, open-loop injection), §IV B, Figs. 20–21, §V.
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §1 (adjoints against RL), §2, Eqs. 2.3, 2.8–2.10 (adjoint training), §2.2–§2.3 (algorithm, GPUs, convergence result cited), §3.2, §4.1, Table 2, §5, Figs. 11–12, §6, Figs. 13–15, §7.
- [Kurz et al. (2023)](/sources/kurz-2023.md) — arXiv v2: §1, §2, Eq. 8 (no solver gradient), §3.5, §4.1 (cost), §4.2, Fig. 6.
- [Tang et al. (2023)](/sources/tang-2023.md) — arXiv v1: §I (CFD-driven GEP cited), §II D–E (loose and tight coupling), §III B (cost), §IV.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §4.3 (CFD-driven GEP of Zhao et al. cited, cost, transfer from high- to low-pressure turbines; injected DNS stress).
- [van Gastelen et al. (2024)](/sources/vangastelen-2024.md) — arXiv v5: §3.4, Eqs. 51–52, App. E.2 (derivative and trajectory fitting); §4.2–4.4, Figs. 7–8 (stability across seeds); §4.3.2 (cost).
- [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) — arXiv v2: §1, §2.2, Algorithm 1, App. B (variational inference through an adjoint solver); §3.3 (learning rate, pre-training); §3.4, Table 4 (cost).
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — arXiv v3: §II.B (ensemble calibration in the LES); §III–IV, Figs. 3–17; App. B; §V (against adjoint calibration).
- [Kim et al. (2024)](/sources/kim-2024.md) — §1, §5 (targets for complex geometries).
- [Vadrot et al. (2023a)](/sources/vadrot-2023.md) — arXiv v3: §II.B.3 (reward on the known mean wall stress).
- [Wu & Lele (2026)](/sources/wu-2026.md) — arXiv v2: §1 (transferability and cost of end-to-end and RL training), §5.2.1, §7 (multi-filter supervised alternative).
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §3.4 (taxonomy of model-consistent frameworks, CFD-driven training, advantages and cost); §4.1, §4.2.1 Eq. 11, §4.4.2 Fig. 11, §4.5 Eq. 17 Figs. 12–13 (results of cited works).
- [Cherroud et al. (2022)](/sources/cherroud-2022.md) — §2.1, Eqs. 10–12 ($k$-corrective-frozen targets, consistency argument); §4.2, Table 2, Fig. 5, App. C (a posteriori selection, results against SST and BSL-EARSM).
- [Xiao et al. (2025)](/sources/xiao-2025.md) — §1 (shift to LES-generated data and model-consistent or RL training; many LES runs needed); §3.2, Fig. 2 (GPU speed-up). No training performed.
- [Bezgin et al. (2025)](/sources/bezgin-2025.md) — §4.2, Eqs. (41)–(42), Fig. 6 (end-to-end training through JAX-Fluids); §5.1–5.2, Tables 2–3 (unroll length, cell-wise against spectral error).
- [Hu & Yang (2026)](/sources/hu-2026.md) — review: §I, Fig. 2, §III D, §VIII (objective–deployment thesis, attributed); §III B, §IV A, §V A–C (remedies, coupling taxonomy, resolution-handoff bottleneck); §VII A, C–E, Table II (Mandler & Weigand loopholes, data, benchmarks, ratings).
