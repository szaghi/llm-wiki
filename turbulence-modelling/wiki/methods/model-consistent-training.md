---
type: Method
title: "Model-consistent (a posteriori) training of learned closures"
description: "Training a learned closure with the solver in the loop, so the loss is evaluated on the model's own solution: field inversion, FIML, adjoint-based integrated training, differentiable-solver unrolling and reinforcement learning, with their consistency arguments, costs and limits."
status: established
aliases: [a posteriori training, a-posteriori training, solver-in-the-loop training, integrated inference and learning, embedded learning, differentiable-physics training]
tags: [data-driven, machine-learning, neural-network, sgs-model, rans, les]
timestamp: 2026-10-25T19:46:00Z
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

**Integrated (tightly coupled) inference and learning.** The learned map
sits inside the solver constraint, and one optimization over
$\boldsymbol\theta$ minimizes
$\mathcal L[\boldsymbol Y,\boldsymbol Y_{\mathrm m}(f(\boldsymbol\zeta_{\mathrm m};\boldsymbol\theta))]$
subject to the augmented equations (Duraisamy 2021, Eq. 9). The author
states that it "ensures full consistency between the learning and
prediction environments". As recalled there, examples are embedded neural
networks in RANS (Holland et al.) and the DPM closure for LES (Sirignano,
MacArt & Freund). Its drawback is that features must be fixed before
inference.

**Weakly coupled variants.** Embedded learning, iterative machine
learning, CFD-driven machine learning and closed-loop training move toward
model consistency without adjoints, though some still need full-field DNS
(Duraisamy 2021, §IV.B).

**Unrolled differentiable solver.** Agdestein & Sanderse (2025, §4.3,
Eq. 25) minimize a trajectory loss: the relative error between the LES
solution and the filtered DNS, averaged over $n_{\mathrm{unroll}}=50$ time
steps that start from the same filtered state. Gradients come from
reverse-mode automatic differentiation through the unrolled LES (Zygote.jl).
An explicit Runge–Kutta integrator was chosen because it is easier to
differentiate (§2.4). As recalled there, others have used unroll lengths
of 30–60 (List et al., 2D incompressible flow), 32 (Kochkov et al.), and 30
(good) versus 120 (poor) for Kuramoto–Sivashinsky (Melchers et al.).

**Reinforcement learning.** Beck & Kurz (2023) pose the choice of closure
parameters as a Markov decision process. The LES with its actual
discretization is the environment, and the reward is computed from the LES
energy spectrum, so no gradient of the solver is needed. Vadrot et al.
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
of a dynamic wall model. See
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md).

## Evidence

- **Decaying isotropic turbulence.** As recalled by Duraisamy (2021,
  §IV.B, Fig. 2, from Sirignano et al.), an a priori-trained SGS closure
  overpredicts the resolved kinetic energy over the plotted interval. The
  model-consistent DPM closure follows the filtered DNS.
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

## Costs

| Source | Training | Cost reported |
|---|---|---|
| Agdestein & Sanderse (2025, §5.2.7, Table 3) | a priori, $10^4$ iterations | 160.6 s ($\bar n=32$) to 1583.6 s ($\bar n=256$), one H100 GPU |
| Agdestein & Sanderse (2025, §5.2.7, Table 3) | a posteriori, 1000 iterations | 4449.3–5849.2 s, one H100 GPU |
| Agdestein & Sanderse (2025, §5.2.7) | DNS and filtering of all data | $1.5739\times10^4$ s |
| Beck & Kurz (2023, §IV B) | 2000 iterations of 16 parallel episodes | at most 0.8 CPU-hours per LES; 8 or 16 cores per LES |
| Vadrot et al. (2023b, §IV D) | RL wall model of Bae & Koumoutsakos | about $10^7$ gradient steps (recalled) |
| Bae & Koumoutsakos (2022, preprint pp. 8, 12–13) | multi-agent RL in WMLES, $10^7$ policy-gradient steps | $O(10^3)$ CPU-hours and under 1 GB at $Re_\tau=4200$, against $O(10^7)$ CPU-hours and over 100 TB to generate DNS data for supervised training (no hardware given) |

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
  keep one parameter set per grid, filter and formulation.
- **Robustness to the discretization is claimed, not tested.** Bae &
  Koumoutsakos (2022) train and test their wall models with one solver
  (staggered second-order finite differences) and one SGS model
  (anisotropic minimum dissipation); the robustness to numerics they
  claim (pp. 3, 10) is an argument from the training setup. Beck & Kurz
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
  the normative entry on this disagreement is on
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
- **Noise.** Agdestein & Sanderse (2025, §6) report that adding noise to
  the training data, a common stabilizer, can destroy the divergence-free
  property. Validation errors were better without noise; no data are
  shown.

# Citations

- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §IV.A, Eq. 5; §IV.B, Eqs. 7–9 (FI, FIML, integrated training, weakly coupled variants, adjoints, Fig. 2); §VII (generalization, identifiability, numerical error).
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §2.4, §4.3, Eq. 25 (trajectory loss, unrolling), §5.2.2–§5.2.7, Figs. 11–12, Table 3; §6; App. B.5, Table B.5.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §I, §IV B (RL in the loop, training cost), §V, §VI.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II B 4, §III A, §IV C, Table III, §IV D.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Research Square preprint v1, pp. 3, 6, 8, 10 (consistency argument, cost, states), Eq. 9 (reward), Methods pp. 12–13 (training).
- [Yan et al. (2022)](/sources/yan-2022.md) — accepted manuscript, §3.1.2, Table 1 (regression loss against a posteriori error; selection by a posteriori error).
