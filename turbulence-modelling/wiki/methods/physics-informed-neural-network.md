---
type: Method
title: "Physics-informed neural networks for RANS"
description: "A neural network maps the coordinates to the mean velocity, pressure and Reynolds stresses and is trained on the RANS residuals plus boundary data; the RANS system is closed by data rather than by a turbulence model, with errors reported for boundary layers, an airfoil and the periodic hill."
status: established
aliases: [PINN, PINNs, physics-informed neural network, physics-informed RANS solver]
tags: [data-driven, neural-network, rans, boundary-layer]
timestamp: 2026-10-29T10:04:00Z
---

# Physics-informed neural networks for RANS

A **physics-informed neural network** (PINN) represents the solution of a
PDE by a neural network of the coordinates and trains its parameters
$\boldsymbol\theta$ on a loss that contains the PDE residuals, evaluated by
automatic differentiation, together with whatever data are available.
[Eivazi et al. (2022)](/sources/eivazi-2022.md) apply it to the
two-dimensional, incompressible, steady RANS equations. A fully connected
network maps $(x,y)$ to the six mean quantities $\langle u\rangle$,
$\langle v\rangle$, $\langle p\rangle$, $R_{11}$, $R_{12}$, $R_{22}$. The
RANS system has more unknowns than equations, and no turbulence model closes
it. The closure is supplied instead by data on the domain boundaries,
Reynolds stresses included, and by the residuals in the interior (Abstract,
§1–2). In every turbulent case the boundary data come from DNS or LES of
the flow being computed (§3), and the paper does not apply a trained network
to another flow.

## Formulation (Eivazi et al. 2022, §2, Fig. 1, Eq. 1)

With $\rho$ constant and $p$ the mean pressure, the residuals of the
momentum and continuity equations are, in registry notation,

$$\begin{aligned}
\mathcal E_1&=\langle u\rangle\partial_x\langle u\rangle+\langle v\rangle\partial_y\langle u\rangle+\rho^{-1}\partial_x\langle p\rangle-\nu\nabla^2\langle u\rangle+\partial_xR_{11}+\partial_yR_{12},\\
\mathcal E_2&=\langle u\rangle\partial_x\langle v\rangle+\langle v\rangle\partial_y\langle v\rangle+\rho^{-1}\partial_y\langle p\rangle-\nu\nabla^2\langle v\rangle+\partial_xR_{12}+\partial_yR_{22},\\
\mathcal E_3&=\partial_x\langle u\rangle+\partial_y\langle v\rangle,
\end{aligned}$$

where $\mathcal E_i$ (page-local) is the residual of equation $i$. The loss
is

$$\mathcal L=\mathcal L_e+\mathcal L_b,\qquad \mathcal L_e=\frac1{N_e}\sum_{i=1}^{3}\sum_{n=1}^{N_e}\lvert\mathcal E_i^n\rvert^2,\qquad \mathcal L_b=\frac1{N_b}\sum_{n=1}^{N_b}\lvert\boldsymbol Y_b^n-\boldsymbol Y_{\mathrm m,b}^n\rvert^2,$$

with $N_e$ residual points (interior collocation points plus boundary
points), $N_b$ boundary samples, $\boldsymbol Y_b^n$ the six reference
quantities at boundary point $n$ and $\boldsymbol Y_{\mathrm m,b}^n$ the
network's prediction there (page-local symbols; subscript $\mathrm m$ as in
the registry, the model's own output). The authors call $\mathcal L_b$ the
supervised and $\mathcal L_e$ the "unsupervised" loss. Weighting
coefficients between the two are possible, citing Jin et al. (2021), but
none is reported as used.

**Ingredients.**

- *Derivatives.* Reverse-mode automatic differentiation of the outputs with
  respect to the inputs (TensorFlow `GradientTape`).
- *Network.* Eight hidden layers of 20 neurons, $\tanh$ activations,
  stated for the laminar case and for the other cases as "similar" (§3).
- *Training.* Adam followed by BFGS, which stops on an increment tolerance.
- *Reynolds number.* It enters only through $\nu$ in the residuals (§1).
- *Not printed in the version read.* $N_e$, $N_b$, the collocation-point
  distribution, learning rates, epochs, training time and hardware.

**Variants per case (§3).** The laminar case solves the Navier–Stokes
equations without Reynolds stresses and is supervised by boundary velocity
only. The zero-pressure-gradient boundary layer solves continuity and
streamwise momentum, with outputs $\langle u\rangle$, $\langle v\rangle$,
$R_{12}$. The adverse-pressure-gradient case solves continuity and both
momentum equations. The airfoil and the hill use the full system with all
six outputs; on the hill, since velocity and stresses vanish on the walls,
data are needed only at the inlet and outlet, plus pressure on all
boundaries.

## Results

The error metric is the relative $\ell_2$ norm over all computational
points, in percent, $100\,\lVert\phi-\phi_{\mathrm m}\rVert_2/\lVert\phi\rVert_2$
for each variable $\phi$ (Eq. 2, Table 1).

| Case | Reference data | Error (%) |
|---|---|---|
| Laminar Falkner–Skan boundary layer, $Re=100$, exponent $m=-0.08$ ($\beta_{\mathrm{FS}}=2m/(m+1)=-0.1739$; separation at $-0.1988$) | analytical solution | $\langle u\rangle$ 0.07, $\langle v\rangle$ 0.12, $\langle p\rangle$ 0.001 |
| Zero-pressure-gradient [turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md), $1000<Re_\theta<7000$ | DNS of Eitel-Amor et al. (2014) | $\langle u\rangle$ 1.02, $\langle v\rangle$ 4.25, $R_{12}$ 6.46 |
| Adverse-pressure-gradient boundary layer at Clauser parameter $\beta_{RC}\simeq1$, $910<Re_\theta<3360$ | Bobke et al. (2017) | $\langle u\rangle$ 0.28, $\langle v\rangle$ 1.57, $\langle p\rangle$ 4.60, $R_{12}$ 7.96 |
| NACA4412 suction-side boundary layer, $Re_c=200{,}000$, $0.5<x/c<1$ | well-resolved spectral-element LES of Vinuesa et al. (2018) | $\langle u\rangle$ 1.56, $\langle v\rangle$ 2.17, $\langle p\rangle$ 7.30, $R_{11}$ 9.43, $R_{12}$ 11.36, $R_{22}$ 4.69 |
| [Periodic hill](/benchmarks/periodic-hill.md), $Re_h=2800$, $1<x/h<5$ | spectral-element DNS (not cited) | $\langle u\rangle$ 2.77, $\langle v\rangle$ 19.70, $\langle p\rangle$ 8.61, $R_{11}$ 28.18, $R_{12}$ 16.70, $R_{22}$ 20.24 |

Here $\beta_{\mathrm{FS}}$ is the Falkner–Skan pressure-gradient parameter
and $\beta_{RC}=(\delta^*/\tau_w)\,\mathrm d p_\infty/\mathrm dx$ the Clauser
parameter, with $p_\infty$ the free-stream pressure ($\beta_{\mathrm{FS}}$
page-local, $\beta_{RC}$ registry §11; the paper writes both with $\beta$,
which the registry keeps for the field-inversion correction). The airfoil inputs are wall-tangent and wall-normal
coordinates.

**Statements of the authors.**

- *Laminar case.* The pressure is recovered to 0.001% although no pressure
  data were supplied (§3, Fig. 2).
- *Boundary layers.* Shape factor, $C_f$ against $Re_\theta$, and
  inner-scaled profiles of $u^+$ and $R_{12}^+$ at three stations agree with
  the references ("excellent accuracy"). In the adverse-pressure-gradient
  case $R_{12}$ "coincide[s] with the reference data" although no turbulence
  model is used (§3, Figs. 3–4). The average errors are 3.91% and 3.60%
  for the two boundary layers (§4).
- *Airfoil.* Inner-scaled profiles of $u^+$ and of the three stresses at
  $x/c\simeq0.625$, 0.75 and 0.875 show "excellent agreement" (Fig. 5).
- *Hill.* The extent of the separated region and the reattachment point are
  "accurately predicted"; $\langle u\rangle$ profiles at five stations agree
  (Fig. 6). No reattachment length is printed.
- *Conclusion (§4).* For the airfoil and the hill the streamwise velocity
  error is below 3%, with "good accuracy even in the simulation of
  Reynolds-stress components".

## Place among data-driven closures

The PINN of Eivazi et al. learns no closure model: its inputs are the
coordinates, so the trained network represents the mean field of one flow,
and no map from flow features to stresses is learned (§2). The data it
uses are boundary values of the very quantities a closure would predict.
Two other routes of this bundle differ in what is inferred:

- [Field inversion](/methods/field-inversion-machine-learning.md) keeps a
  turbulence model and infers a spatial correction of it from data, then
  learns the correction as a function of local features so that it
  transfers to other flows.
- A [tensor-basis neural network](/methods/tensor-basis-neural-network.md)
  learns the Reynolds-stress anisotropy as a function of local invariants of
  the mean flow, for use inside a RANS solver.

Eivazi et al. (2022) make neither comparison and do not discuss
generalization, uniqueness of the reconstruction or sensitivity to the
boundary data (§1–4). Their stated precedent is the direct simulation of
turbulence with PINNs by Jin et al. (2021), which they cite as agreeing
well with DNS (§1). [Domingo & Vervisch (2023)](/sources/domingo-2023.md) (§7) name
physics-informed techniques that couple PDE solution and network training
as a coming perspective for combustion DNS, without a method.
[van Gastelen et al. (2024)](/sources/vangastelen-2024.md) (§1) mention
PINNs among machine-learning work on Burgers' equation in the same terms:
"the PDE is encoded into the loss function", with the advantage of
approximating the solution "without explicitly discretizing space and
time". Their own [closure](/methods/neural-network-sgs-model.md) is of a
different kind: a discrete coarse-grid closure whose energy conservation
is built into the architecture (§3).
[Ruggeri et al. (2022)](/sources/ruggeri-2022.md) (§III) cite the
same paper as PINNs for RANS that use only boundary data, with an
$\ell_2$ error of around 3% for turbulent flows; Eivazi et al. themselves
state errors below 3% (above). [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md)
(§4.3) call "initial work on LES wall modeling using physics-informed
neural networks" (Yang et al. 2019, as cited) "a promising path" for
reducing the cost of LES, without details (see [machine-learning wall models](/methods/machine-learning-wall-model.md)).
[Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) (§3.2) describe
PINNs as an approach "that does not seek to find explicit closure terms",
whose outputs are weighted against partial data such as boundary
conditions, and state that PINNs "do not yield closures that can be
utilized in predictive RANS-based CFD of new configurations"; their review
of learned stress and heat-flux closures covers tensor-basis,
symbolic-regression and model-consistent approaches (see
[model-consistent training](/methods/model-consistent-training.md)). The
review states the verdict without a test.

**PINNs as one form of knowledge-guided learning (Ihme et al. 2022).**
[Ihme et al. (2022)](/sources/ihme-2022.md) (§3.5, §3.5.1, Fig. 25,
Eqs. 64–66) classify the ways prior knowledge enters a supervised model by
where it is inserted: the loss function, the data (feature selection and
transformation), the architecture (the
[tensor-basis neural network](/methods/tensor-basis-neural-network.md),
neural ODEs, divergence-free generative networks), or the output (the
trained model embedded in a conventional solver). A constraint
$\mathcal C(\boldsymbol\zeta,\boldsymbol\theta)=0$ (page-local) is in
principle imposed by constrained minimization of the loss, and in
practice relaxed into a penalty,

$$\min_{\boldsymbol\theta}\ \mathcal L(\boldsymbol\theta)\quad\text{s.t.}\quad\mathcal C=0\qquad\longrightarrow\qquad\min_{\boldsymbol\theta}\ \mathcal L(\boldsymbol\theta)+\lambda_{\mathcal C}\,\mathcal C(\boldsymbol\zeta,\boldsymbol\theta),$$

with $\lambda_{\mathcal C}$ (page-local) a weight, so that the constraint
holds only weakly. PINNs are their flow-physics example of the loss route.
The authors prefer the name "knowledge-guided" to "physics-informed" for
combustion, which draws on disciplines other than physics (§1.3), and
hold that purely data-driven models "are not expected to be truly
predictive" (§1.3). Their turbulence example of a physics-informed loss is
the continuity term of a super-resolution GAN for subgrid stresses (see
[super-resolution SGS models](/methods/super-resolution-sgs-model.md)).
The review states the classification; it runs no PINN.

## A label-free physics-informed loss outside turbulence (Ruggeri et al. 2022)

Ruggeri et al. (2022, App. C, Fig. 10, Table XI) train a network without
labels on the one-dimensional Riemann problem of the ideal-gas Euler
equations, as an alternative to their supervised neural Riemann
solvers. The inputs are pressure, velocity and sound speed of the two
initial states, the output the velocity $u^*$ of the star region. From
$u^*$ the pressures that the left and right states need to reach it are
computed; the loss is their mismatch $\lvert p_{II}-p_{III}\rvert$
(page-local: the pressures left and right of the contact), or the
arbitrary value $10^{20}$ when a sound speed would become non-positive
(e.g. too strong a rarefaction). Training is slower than supervised
training, inference equally fast. Its mean absolute percentage errors,
0.670% in $u^*$, 0.371% in $p^*$, 0.475% and 0.458% in the two star
densities, beat their supervised stand-alone network (4.026% and 1.415%
in $u^*$ and $p^*$, Table VIII) and fall short of the network that
predicts one star value and computes the rest from the exact relations
(0.435% and 0.134%). The authors conclude that for "a safe deployment of
the model in the CFD solver, it is important to use a physics-informed
neural network, or to avoid extreme cases" such as constant initial
conditions (Conclusions). They call the label-free network
physics-informed (App. C heading); its loss is the pressure mismatch
above. Ruggeri et al. (§I) cite Wang's PINN for supercritical-fluid
Riemann problems embedded in a CFD solver. The flows are inviscid and
laminar.

## From PINNs to physics-informed neural operators (Zhao et al. 2025)

[Zhao et al. (2025)](/sources/zhao-2025.md) (§2.2, Eq. 8) recall the
generic PINN loss for $\partial_tu=\mathcal N(u)$ (page-local
$\mathcal N$, the PDE operator): the squared residual over the domain and
time, plus weighted boundary and initial-condition misfits, with
derivatives by automatic differentiation. They state that PINNs
struggle on multiscale problems and cite the physics-informed neural
operator (PINO) of Li et al., which combines a data loss with the PDE loss
on a Fourier neural operator and, as they cite it, reaches 6% relative
error on 2-D turbulence at $T=0.125$ but about 74% at $T=0.5$ (§2.4). The authors name three
drawbacks of that PINO: long-time error, competing losses (initial,
equation, data), and overlapping training and prediction windows.

Their LESnets apply the physics-informed loss to the time advance of
LES: the network is an operator
from one filtered velocity field to the next ten, trained only on the
residuals of continuity and of the filtered momentum equation closed by
the Smagorinsky model, with the initial field as input rather than as a
loss term, so that the trained operator can be rolled out (§2.5). Unlike
the PINN of Eivazi et al., which represents one flow as a function of the
coordinates, the operator is trained on 5000 initial fields and applied
to unseen ones (§3.1). With the original initial-condition loss the
rollout diverges (App. A). Details and results are on
[neural-operator surrogates of LES](/methods/neural-operator-les-surrogate.md).

## PINNs in two later reviews (Le et al. 2024; Fang et al. 2026)

Two reviews of machine learning in turbulence and supersonic flow survey
PINNs without running one.

- **Loss.** [Fang et al. (2026)](/sources/fang-2026.md) (§2.1, Eq. 9,
  Fig. 4c) write the loss as a data term plus a weighted PDE-residual
  term, $\mathcal L=\mathcal L_{\mathrm{data}}+w_{\mathrm{PDE}}\mathcal L_{\mathrm{PDE}}$
  (page-local $w_{\mathrm{PDE}}$, the source's $\lambda$), the weight
  balancing data fidelity against physical consistency, and call the PDE
  penalty a "soft constraint" (§4.2.2).
  [Le et al. (2024)](/sources/le-2024.md) (§2.2.3, Fig. 6) describe the
  same structure: mismatch of data, initial and boundary values plus the
  residual at collocation points, optimized together.
- **Turbulence-model-augmented PINNs.** Fang et al. (§4.2.2, Table 4)
  cite PINNs that carry a RANS closure in the residual (the PINN of
  Eivazi et al. (2022) learns no closure model, above): a Spalart–Allmaras-augmented
  PINN that reconstructs mean flows from sparse velocity data, with the
  mean-velocity reconstruction error "from 11.7% to 3.1%, a reduction of
  about 73%" and an improvement on variational data assimilation in
  high-gradient regions (Patel et al., as cited); and PINNs with the
  standard [$k$-$\varepsilon$](/methods/k-epsilon-model.md) model or a
  mixing-length-type "hybrid length model" that predict a
  [backward-facing step](/benchmarks/backward-facing-step.md) at Reynolds
  number 5100 from sparse data (Pioch et al., as cited). They also cite
  the RANS PINN of Eivazi et al. (2022) and a parametric variant (PT-PINN,
  Jiang et al., as cited) that takes physical parameters such as the
  Reynolds number as inputs, "train once, generalize across parameters",
  for a three-dimensional backward-facing step at a cost "up to 1/16 of
  traditional CFD methods" (§4.2.2, Fig. 9).
- **Variants and applications (Le et al.).** cPINN, hp-VPINN, XPINN with
  space–time domain decomposition, SA-PINN with trainable pointwise
  adaptive weights, which beats other PINNs in $L_2$ error with fewer
  training cycles, and the separable PINN, motivated by computational and
  memory costs "increasing exponentially with grid resolution" (§2.2.3,
  p. 7). Applications cited: high-speed flows,
  hypersonic cones, hidden fluid mechanics, Euler-constrained
  convolutional networks for supersonic inlet fields, a Mach-10 inviscid
  inlet, POD reduced-order models of a rotating detonation combustor and
  pressure recovery from 1% sparse data (§2.2.3, §4.3, Table 8), and a
  three-dimensional reconstruction of turbulent premixed flames from
  synthetic sparse data with separate sub-networks for momentum, species
  and temperature, whose effectiveness depends on dataset size, noise and
  turbulence–flame interaction (Liu et al., as cited; §3.3, Fig. 17).
- **Evaluative statements.** Fang et al. (§4.2.2) state that PINNs "offer
  improved interpretability" over purely data-driven models and that in
  the SA-augmented PINN "the error caused by discretization in the
  variational method is avoided"; Le et al. state the exponential cost
  growth.

## PINNs in a combustion review (Posch et al. 2025)

[Posch et al. (2025)](/sources/posch-2025.md), reviewing turbulent
combustion models for engine CFD, place PINNs under machine learning for
chemistry integration, not under turbulence closures (§6.4.1). Data-driven
models such as networks lack extrapolation capability, so the training
data must cover the temperature and pressure range of the engine's
operating conditions; "to deal with the issue of missing extrapolation
capability, so-called hybrid methods which combine data-driven and
physics models (e.g., physics-informed neural networks [475]) may be
beneficial", ref. [475] being Raissi et al. (2019). They cite Zhang et
al. (2024, CRK-PINN) for solving combustion reaction kinetics "by
integrating the required ODEs into the loss function of an ANN"
(§6.4.1). On the closure side (§6.4.2) they cite super-resolution
generative networks for the subgrid mixture-fraction flux and Reynolds
stresses with "physics-informed loss functions based on the continuity
equation" (Bode et al., as cited), the example Ihme et al. (2022) also
give (above; see [super-resolution SGS models](/methods/super-resolution-sgs-model.md)),
and state that machine-learned closures "have been mostly developed and
tested on benchmark flame simulation cases", their transfer to engines
being "not straight forward". The review runs no PINN.

## Why vanilla PINNs miss developed turbulence (Hu & Yang 2026)

[Hu & Yang (2026)](/sources/hu-2026.md) give PINNs a section of their
review of machine-learning closures (§V, Eq. 6, Fig. 3, Table IV). They
write the composite loss as

$$\mathcal L=\mathcal L_{\mathrm{data}}+w_{\mathrm{PDE}}\,\mathcal L_{\mathrm{PDE}}+w_{\mathrm{BC}}\,\mathcal L_{\mathrm{BC/IC}},$$

with $\mathcal L_{\mathrm{PDE}}$ evaluated at collocation points by
automatic differentiation. The weights $w_{\mathrm{PDE}}$ and
$w_{\mathrm{BC}}$ are page-local; the source writes $\lambda$ and $\mu$
and prints no values. Hu & Yang call a "vanilla" PINN a single
multilayer perceptron minimizing this loss. They state that it cannot
recover fully developed turbulence "without additional ingredients", and
they present this verdict as "an author perspective, not a settled
consensus" (§V A). Their Table IV names three failure mechanisms:

| Mechanism | Manifestation | Mitigations named | Works cited there |
|---|---|---|---|
| Spectral bias of the neural tangent kernel (NTK) | low-wavenumber modes are learned orders of magnitude faster than high-wavenumber ones, so the Kolmogorov cascade is out of reach | causal training, adaptive residual-point sampling, gradients weighted by NTK eigenvalues | Wang, Yu & Perdikaris (2022); Wang, Sankaran & Perdikaris (causal training) |
| Representational bandwidth limit of smooth finite-width networks | the derivatives are too band-limited and the spectrum decays too fast; the field is "too viscous" | physics-informed neural operators (PINO), weak or variational losses (VPINN, Deep Ritz), data constraints on high wavenumbers | Li et al. (PINO); Eivazi et al. (2024, experimental fluid mechanics) |
| Chaotic long-time unpredictability | trajectories diverge exponentially, so no stationary function of $(\boldsymbol x,t)$ exists to regress | use PINNs for inverse and reconstruction problems, for mean or filtered fields, or in hybrid PINN–LES/RANS | Raissi et al. (hidden fluid mechanics); Jin et al. (NSFnets) |

All works in the table are cited by Hu & Yang (2026). The Eivazi et
al. entry is a 2024 review of experimental applications, a different
work from the RANS PINN of [Eivazi et al. (2022)](/sources/eivazi-2022.md)
above.

Hu & Yang (§V A–B) list the variants they see as answers to these
obstacles: NSFnets in velocity–pressure or velocity–vorticity form,
non-Newtonian PINNs, conservative and extended PINNs with domain
decomposition (cPINN, XPINN) and their distributed MPI+X version,
DeepXDE, causal training and NTK-based adaptive weights. To their
knowledge, none of these variants (PINO, VPINN, Deep Ritz, causal
training, hybrid PINN–LES/RANS) has shown a statistically faithful
forward integration of high-Reynolds-number three-dimensional
wall-bounded turbulence without substantial external data. They cite
NSFnets as "accurate simulations across incompressible flows ranging from
laminar to turbulent regimes", and they count them among the variants
that succeed by working on mean or filtered fields, "as in NSFnets
applied to modest-Reynolds-number laminar-to-turbulent regimes". Their
conclusion is that vanilla PINNs are "best understood as a
reconstruction tool for data-constrained fluid-mechanics problems,
rather than a general-purpose substitute for DNS or LES in the forward
direction".

Hu & Yang read the three
mechanisms as the PINN form of one obstacle common to all
machine-learning closures: a pointwise training objective that does not
match a multi-scale, solver-coupled deployment. They state that tracing
the failures to this single root is their own interpretive synthesis,
"not an established conclusion of the field" (§I, Fig. 2, §VIII). See
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
and [model-consistent training](/methods/model-consistent-training.md).

## Qualifications

- **Data requirement.** The reconstruction of each turbulent case uses
  boundary values of the Reynolds stresses from DNS or LES of the same flow
  (§2–3). The paper's phrase "without any specific model or assumption for
  turbulence" (Abstract) describes the form of the closure, not an absence
  of turbulence data.
- **Accuracy on the hill.** The Reynolds-stress errors on the periodic hill
  are 16.7% to 28.2% and the wall-normal velocity error 19.7% (Table 1),
  against the paper's summary "good accuracy" for the stresses (§4). The
  hill subdomain $1<x/h<5$ is a part of the hill period. The hill reference
  DNS is described but not cited.
- **Version read.** The source page records arXiv v1 (six pages); the
  published version may differ. All numbers above are those of v1.
- **Printed slips.** Eq. 1b sums residuals over three equations, while the
  zero-pressure-gradient case solves two and the laminar case has no
  Reynolds stresses: Eq. 1 is the general form. The Fig. 4 caption labels a
  panel (d) that the figure, which has panels (a)–(c), does not contain;
  the text refers to Fig. 4(c).
- **A mismatched citation.** van Gastelen et al. (2024, §1) write that "in
  [29] physics-informed neural networks (PINNs) were succesfully applied to
  Burgers' equation"; their ref. [29] is Shankar et al., a
  differentiable-physics closure for Burgers turbulence, printed again
  identically as ref. [32]; the title printed for it names a
  differentiable-physics closure, not a PINN, and the PINN work meant is
  not identified.
- **Attributions in Le et al. (2024).** The physics-informed
  convolutional network with channel interaction (PICNNCI) is attributed
  to "Deng et al. [248]", whose printed reference is a Kong et al.
  schlieren-to-velocity paper; the review's Fig. 23 cites the Deng et al.
  work as [268] (§4.3, p. 26). "Wang et al. [232]" (a PINN premixed
  combustion model) and "Xiong et al. [233]" (a PINN reconstruction) cite
  references whose printed titles are a waverider boundary-layer study and
  a shock-train experiment (§3.3, p. 21). The page names those works by
  the description in the text only.
- The convention of the Reynolds stresses in the version read (positive
  correlations $\overline{uv}$ on the left-hand side of momentum, kinematic)
  matches the registry $R_{ij}$; the paper writes the means as $U$, $V$,
  $P$.

# Citations

- [Eivazi et al. (2022)](/sources/eivazi-2022.md) — arXiv v1: Abstract; §1 (underdetermined RANS, precedent); §2, Fig. 1, Eqs. 1–2 (network, residuals, loss, error metric); §3, Figs. 2–6, Table 1 (five cases); §4 (conclusions).
- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — §7 (physics-informed techniques as a perspective for combustion DNS).
- [Zhao et al. (2025)](/sources/zhao-2025.md) — arXiv v3: §2.2, Eq. 8 (PINN loss); §2.4 (PINO and its drawbacks, cited); §2.5, Eq. 17 (LESnets); §3.1; App. A.
- [Ruggeri et al. (2022)](/sources/ruggeri-2022.md) — §I (Wang's PINN cited), §III (Eivazi et al. cited), App. C, Fig. 10, Tables VIII, XI (label-free Riemann-problem network); Conclusions.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §4.3 (PINN-based LES wall modelling cited).
- [van Gastelen et al. (2024)](/sources/vangastelen-2024.md) — arXiv v5: §1 (PINNs mentioned among machine-learning work on Burgers' equation; ref. [29] as printed); §3 (energy-conserving architecture).
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §3.2 (PINNs yield no predictive closures for new configurations).
- [Ihme et al. (2022)](/sources/ihme-2022.md) — §1.3 (knowledge-guided against purely data-driven); §3.5, §3.5.1, Fig. 25, Eqs. 64–66 (four insertion points of prior knowledge; constraint relaxed to a penalty; PINNs as the example).
- [Fang et al. (2026)](/sources/fang-2026.md) — §2.1, Eq. 9, Fig. 4c (PINN loss); §4.2.2, Fig. 9, Table 4 (soft constraint, SA-augmented and $k$-$\varepsilon$ PINNs, PT-PINNs, Eivazi et al. cited, interpretability claim).
- [Le et al. (2024)](/sources/le-2024.md) — §2.2.3, p. 7, Fig. 6 (loss, variants, cost claim); §3.3, Fig. 17 (flame reconstruction); §4.3, p. 26, Table 8 (physics-informed reconstruction of inlet fields).
- [Posch et al. (2025)](/sources/posch-2025.md) — §6.4.1 (PINNs as hybrid remedy for missing extrapolation, CRK-PINN cited); §6.4.2 (physics-informed GAN loss cited; closures tested on benchmark flames).
- [Hu & Yang (2026)](/sources/hu-2026.md) — review: §I, Fig. 2, §VIII (single-root thesis, attributed); §V A–B, Eq. 6, Fig. 3, Table IV (composite loss, three failure mechanisms, variants, verdict as author perspective).
