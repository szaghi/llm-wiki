---
type: Method
title: "Neural-network subgrid-scale models"
description: "LES closures in which a neural network maps resolved-field features to the subgrid stress, its divergence or a model coefficient; trained a priori on filtered DNS, by reinforcement learning or through adjoints. Covers inputs, output normalization for generalization, invariance, cost against dynamic models, and backscatter without clipping."
status: established
aliases: [ANN-SGS model, ANN-SGS mixed model, deep-learning LES closure, DL-LES, neural-network LES closure, data-driven SGS model, S-106H, SL-106H, SL-180C, DL-AR1, DL-AR2]
tags: [neural-network, sgs-model, les, machine-learning, data-driven]
timestamp: 2026-10-26T07:37:00Z
---

# Neural-network subgrid-scale models

A **neural-network SGS model** replaces the closure of the filtered
Navier–Stokes equations, or part of it, by a network
$f(\boldsymbol\zeta;\boldsymbol\theta)$ evaluated from resolved-field
features $\boldsymbol\zeta$ at each grid point or element. What the
network returns differs between the sources: the six components of the
subgrid stress $\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$ (Kang et al.
2023; Kim et al. 2022), a stress whose divergence stands for every
unclosed term (Sirignano & MacArt 2023), or the coefficient of an
analytical model (Kurz et al. 2023). How it is trained differs too: a
priori on filtered DNS (Kang et al.), by
[reinforcement learning](/methods/reinforcement-learning-closure.md) in
the running LES (Kim et al.; Kurz et al.), or through the adjoint of the
LES equations (Sirignano & MacArt); see
[model-consistent training](/methods/model-consistent-training.md) and
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).
As recalled by Duraisamy (2021, §III.A), other networks model the SGS
force $\partial_j\tau_{ij}$ directly (Beck et al.; Xie et al.), "since
small errors in the subgrid scale *stresses* can otherwise generate large
errors in the momentum equation".

## The models in the sources

| Source | Output | Inputs | Network | Training |
|---|---|---|---|---|
| [Kang et al. (2023)](/sources/kang-2023.md) | 6 components of $\tau_{ij}$ | single point: $\bar S_{ij}$ (S models) or $\bar S_{ij}$ and $L_{ij}$ (SL, "mixed") | 2 hidden layers of 12 neurons, Leaky ReLU, linear output | supervised on filtered DNS |
| [Kim et al. (2022)](/sources/kim-2022.md) | 6 components of $\tau_{ij}$ (or a scalar $\nu_t$), times $\Delta^2$ | single point: $\partial_i\bar u_j$ and grid size, in wall units | 6 hidden layers of 128 units | DRL on two mean profiles |
| [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) | a $3\times3$ tensor $h_{ij}$ whose divergence replaces all unclosed terms | the filtered velocity-gradient tensor | gated feed-forward, tanh, 50 units per layer | adjoint-based, in the LES |
| [Kurz et al. (2023)](/sources/kurz-2023.md) | one Smagorinsky $C_s\in[0,0.5]$ per DG element | the element's momentum field (or five velocity-gradient invariants) | 3D CNN, four convolution layers | PPO in the running LES |

Agdestein & Sanderse (2025) train a CNN on the discrete commutator error
of a staggered grid (see
[divergence-consistent LES](/methods/divergence-consistent-les.md) and
[discretization-consistent closure](/definitions/discretization-consistent-closure.md)).

## Supervised mixed network (Kang et al. 2023)

**Architecture and data (§2.4).** A multilayer perceptron with layer map
$X^n_i=\sigma(\sum_jW^n_{ij}X^{n-1}_j+b^n_i)$ (page-local), two hidden
layers of 12 neurons and a linear output of six stress components. The
loss is the mean squared error over the six independent components
against filtered DNS (Eq. 2.10); mini-batches of 128, Adam at $10^{-4}$,
$5\times10^5$ iterations. Isotropic turbulence supplies $2\times10^8$
samples from 30 snapshots (80% training); channel flow
$3.5\times10^7$ from five fields. The inputs are single-point, a choice
made for numerical stability, following Park & Choi (2021), and for low
cost. Grid and test filters are Gaussian with $\hat\Delta/\Delta=\sqrt5$
in isotropic turbulence (top-hat filters gave "no considerable
differences"), and fourth-order commutative discrete filters with
$\Delta=4$ and $\hat\Delta=8$ DNS spacings in the channel (§2–§3.5).

**Inputs: strain alone or strain plus resolved stress.** With $\bar S_{ij}$
alone the network "only rescales the given input" and predicts a stress
nearly aligned with the strain: a priori, in forced isotropic turbulence
at $Re_\lambda=106$, the correlation of $\bar S_{12}$ with the predicted
$\tau_{12}$ is $-0.8217$, against $-0.2806$ in filtered DNS (§3.1, Table
3). Like an eddy-viscosity model it cannot backscatter, and a posteriori
it performs almost identically to the dynamic Smagorinsky model. Adding
the six components of the resolved stress
$L_{ij}=\widehat{\bar u_i\bar u_j}-\hat{\bar u}_i\hat{\bar u}_j$, the term
of the [dynamic mixed models](/methods/scale-similarity-model.md), raises
the a priori correlation of the deviatoric stress with filtered DNS from
0.3509–0.3692 to 0.7040–0.7176 (Table 4) and reproduces the PDF of the
SGS dissipation including backscatter. In LES the mixed network runs
stably "without any ad hoc procedures", whereas the algebraic dynamic
models need averaging in homogeneous directions and clipping, without
which they overestimate both backscatter and forward scatter and diverge
"within tens of time steps" (§3.1, §3.3; see
[energy backscatter](/definitions/energy-backscatter.md)). Among
similarity terms tried as second input (modified Leonard term, $L_{ij}$,
the [gradient-model](/methods/gradient-model.md) term), $L_{ij}$ is best
overall; the gradient term gives the largest spectral errors on coarse
grids, which the authors attribute to its truncation error (App. C).

**Normalization for generalization (§2.4, §3.2).** Inputs are divided by
the volume average of their tensor norm, $\bar S_{ij}/\langle\lvert\bar S\rvert\rangle$
and $L_{ij}/\langle\lvert L\rvert\rangle$ (here $\langle\cdot\rangle$ is a
volume or plane average and $\lvert\cdot\rvert$ the $L_2$ norm of the
tensor, as in the paper). The output would need $\langle\lvert\tau\rvert\rangle$,
unknown in LES, so it is replaced by an estimate: the norm of the
gradient-model term $\tfrac1{12}\Delta^2\partial_k\bar u_i\partial_k\bar u_j$
in isotropic turbulence, whose ratio to the filtered-DNS norm stays the
most constant across $Re_\lambda$ and across training-to-test filter-width
ratios $1/2$, 1 and 2 (Fig. 10); and $\langle\lvert L\rvert\rangle$ in the
channel, because the gradient term has an incorrect near-wall scaling
(recalled from Liu et al. 1994). The design rule is that the normalized
input and output distributions must not change with Reynolds number or
resolution; otherwise a "prior probability shift" degrades the model.
Normalizations by wall units, or by the rms velocity and Taylor
microscale, fail on untrained grids because they ignore the filter-width
change (App. E).

**Results.**

- *Isotropic turbulence.* Models trained at $Re_\lambda=106$, 286 or both
  perform almost identically, so one Reynolds number and one resolution
  suffice there (§3.2). Trained on forced turbulence only, the mixed
  networks predict decaying turbulence on $24^3$, $48^3$, $96^3$ and (at
  $Re_\lambda=286$) $128^3$ grids more accurately than dynamic
  Smagorinsky, stably (Table 5, Figs. 13–17).
- *Against algebraic mixed models.* The network beats the one- and
  two-parameter dynamic mixed models a posteriori in decaying turbulence
  although its a priori correlation is lower than that of the
  two-parameter model with a Clark term (0.70–0.72 against 0.91; §3.3,
  Table 6).
- *Channel flow at $Re_\tau=180$* ($48^3$, $\Delta x^+=47.2$,
  $\Delta z^+=15.7$). The network trained on channel data gives
  $C_f=0.0092$ against 0.0085 in filtered DNS, 0.0072 for dynamic
  Smagorinsky and 0.0103 without model, and better mean velocity, rms
  velocities and Reynolds shear stress than dynamic Smagorinsky (§3.5,
  Table 11). It also beats it on untrained coarser
  ($32\times48\times32$) and finer ($64^3$) grids and at $Re_\tau=395$
  (Figs. 26–27). The strain-only network underpredicts the mean velocity
  at $Re_\tau=395$.
- *Training flow matters for the mean shear.* Trained on isotropic
  turbulence only, the mixed network is stable in the channel and gives
  good fluctuations but underpredicts the mean velocity, attributed to the
  vanishing mean off-diagonal SGS stress of isotropic training data; a
  network trained jointly on both flows is accurate in both (§3.5, Fig.
  29). Normalizing by plane averages instead of volume averages makes the
  mean SGS shear stress vanish at the wall and improves the mean velocity
  of the isotropic-trained model (§3.6, Fig. 30).
- *SGS anisotropy.* In the anisotropy-invariant map of the plane-averaged
  SGS stress (Lumley–Newman form), the channel-trained mixed network
  reaches the two-component limit at the wall like filtered DNS; the
  strain-only network stays near the isotropic origin (§3.7, Fig. 32).
  The authors consider the use of $L_{ij}$ "the most important factor"
  for generalization to an untrained channel flow, since $L_{xy}$ follows
  the near-wall distribution of $\tau_{xy}$ while $\bar S_{xy}$ grows
  toward the wall (§3.7, Fig. 31).

**Reference DNS and forcing (App. A).** With the negative-viscosity
forcing that Langford & Moser (1999) report using, the authors obtain
$Re_\lambda=122.9$ instead of 164; the deterministic forcing of Machiels
(1997) gives 164.7 and reproduces the reported statistics, and is used
for all analyses (Table 14; see
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)).

## Adjoint-trained network for bluff-body LES (Sirignano & MacArt 2023)

The network of Sirignano & MacArt (2023, §2.1, Eq. 2.7) is a gated
feed-forward network. With input features $\boldsymbol\zeta$ the filtered
velocity-gradient components at a grid point (the paper's $z$), weights $W^k$,
biases $b^k$, $\sigma=\tanh$ and $\odot$ the elementwise product:

$$\begin{aligned}H^1&=\sigma(W^1\boldsymbol\zeta+b^1),\qquad H^2=\sigma(W^2H^1+b^2),\\H^3&=G^1\odot H^2,\quad G^1=\sigma(W^5\boldsymbol\zeta+b^5),\\H^4&=\sigma(W^3H^3+b^3),\\H^5&=G^2\odot H^4,\quad G^2=\sigma(W^6\boldsymbol\zeta+b^6),\\h(\boldsymbol\zeta;\boldsymbol\theta)&=W^4H^5+b^4,\end{aligned}$$

with 50 hidden units per layer; the gates are likened to those of
LSTM and GRU networks and add nonlinearity. The output is a $3\times3$
tensor $h_{ij}$ whose divergence replaces the subgrid-stress divergence
and the extra terms of filtering at the body and of filter–derivative
non-commutation on the non-uniform mesh (§2). One network and one
parameter set serve the whole domain, near the walls and far from them,
so there is no separate [wall model](/methods/machine-learning-wall-model.md);
the LES do not resolve $y^+=10$ at most stations, yet the near-wall mean
profiles "generally slightly outperform" the
[anisotropic minimum-dissipation model](/methods/anisotropic-minimum-dissipation-model.md)
and "dramatically outperform" dynamic Smagorinsky and no-model LES (§4.3,
Fig. 10). In boundary-layer regions no-model and dynamic-Smagorinsky LES
give "incorrectly large" resolved Reynolds stresses where filtered DNS is
near zero (§4.2, Figs. 8–9). Training and drag results are on
[model-consistent training](/methods/model-consistent-training.md).

## Invariance and constraints

- Sirignano & MacArt (2023, §2.1): velocity-gradient inputs make the model
  Galilean invariant, not rotationally invariant; tensor-basis networks
  are future work (§7; see
  [tensor-basis neural network](/methods/tensor-basis-neural-network.md)).
- Kim et al. (2022, §II E) impose reflectional equivariance and a zero
  stress at the wall, not rotational or Galilean invariance; a tensor
  basis brought no conclusive gain.
- Kurz et al. (2023, §3.4) offer the velocity-gradient invariants as a
  Galilean-invariant input, following Novati et al.; they trained slower
  and ended worse than the element's raw momentum field (§4.3).
- Kang et al. (2023) state no invariance property of their network.

## Cost against the dynamic model

| Source | Comparison | Ratio to the dynamic Smagorinsky model |
|---|---|---|
| Kang et al. (2023, §3.4, Figs. 23–24) | SGS-stress evaluation, 16 CPU cores, 100 steps, forward pass in the LES code | network 0.71 (12 neurons), 0.89 (24), 1.42 (48); algebraic mixed models 1.68–2.24 |
| Kang et al. (2023, §1), recalled | earlier ANN-SGS models | 1.3 (Park & Choi 2021), 1.8 (Wang et al. 2018), 2.4 (Yuan et al. 2020), 15 (Xie & Wang 2019), 256 (Xie et al. 2020a) |
| Kurz et al. (2023, §4.2) | policy evaluation against the dynamic procedure, one CPU core, 48 DOF, unoptimized | about 1.1 |

## Qualifications

- **Printed activation.** Kang et al. (2023, §2.4, p. A38-8) print the
  Leaky ReLU as $\sigma(x)=\max[-0.02x,x]$. For $x<0$ this returns
  $-0.02x>0$, a non-monotone function; a leaky ReLU with slope 0.02 for
  negative arguments is $\max[0.02x,x]$ *(compiler check, not in the
  sources)*. Whether the code
  used the printed form cannot be told from the paper.
- **Printed Reynolds number.** The caption of Kang et al.'s Fig. 10 gives
  $Re_\lambda=106$, 168 and 286; the DNS cases are at 106, 164 and 286
  (Table 1).
- **Illegible equation.** In Kang et al.'s Eq. 3.4, the second term of the
  tensor $H_{ij}$ of the one-parameter dynamic mixed model is typeset with
  colliding accents and is not legible; it is not reconstructed here (see
  [scale-similarity model](/methods/scale-similarity-model.md)).
- **Scope of the stability claim.** The mixed network's stability without
  clipping is shown in pseudospectral isotropic turbulence and a
  fourth-order finite-difference channel (Kang et al. 2023, §2–§3). The
  cost ratios are relative to dynamic Smagorinsky with test filtering in
  the authors' solvers; no static model is timed.
- **Comparisons are not on common cases.** The four models of the first
  table are tested on isotropic turbulence, channel flow and bluff-body
  wakes, with different solvers and references; no source compares
  supervised, RL and adjoint training of the same network on one case
  except Sirignano & MacArt (2023, §5), who compare supervised and adjoint
  training (see
  [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).
- **Notation.** Kang et al. write the third filter level of their
  two-parameter models as a tilde, which this bundle reserves for the
  Favre filter. Sirignano & MacArt write the adjoint variables with a
  hat, which this bundle reserves for the test filter, and use $G$ both
  for the filter kernel and for the gates.

# Citations

- [Kang et al. (2023)](/sources/kang-2023.md) — §1 (earlier costs), §2.4, Eqs. 2.9–2.10 (architecture, loss, normalization), §3.1, Tables 3–4, Figs. 4–8; §3.2, Figs. 10–17, Table 5; §3.3, Table 6, Figs. 19–22; §3.4, Figs. 23–24; §3.5, Tables 9–11, Figs. 25–29; §3.6, Fig. 30; §3.7, Figs. 31–32; App. A, Table 14; App. C; App. E.
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §2, Eqs. 2.2–2.3; §2.1, Eq. 2.7; §4.2–§4.3, Figs. 8–10; §7.
- [Kim et al. (2022)](/sources/kim-2022.md) — arXiv v2: §II C, §II E (actor, outputs, constraints, tensor basis).
- [Kurz et al. (2023)](/sources/kurz-2023.md) — arXiv v2: §3.4, Fig. 4 (CNN policy, inputs), §4.2 (cost), §4.3, Fig. 7 (inputs compared).
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §III.A (networks for the SGS force, recalled).
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §4.4.2 (CNN on the discrete commutator error).
