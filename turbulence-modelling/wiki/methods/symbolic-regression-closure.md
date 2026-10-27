---
type: Method
title: "Symbolic-regression turbulence closures"
description: "Closures whose model terms are explicit algebraic expressions found by a search over expression space (gene-expression programming, sparse and sparse Bayesian regression, deep symbolic regression, PySR), as integrity-basis coefficients, a scalar multiplier of a model term or an LES subgrid stress; covers learned k-ε and SST corrections and the higher-order gradient model."
status: established
aliases: [symbolic regression, PySR, SBL-SpaRTA, SR-CLS, SR-CND, deep symbolic regression, DSR, gene-expression programming, GEP, sparse regression, SpaRTA, explicit algebraic closure discovery, DSRRANS, relevance vector machine, RVM, NGM4, NGM6, equation discovery]
tags: [symbolic-regression, rans, les, sgs-model, data-driven, separated-flow]
timestamp: 2026-10-26T20:51:00Z
---

# Symbolic-regression turbulence closures

A **symbolic-regression closure** is a turbulence model whose unknown
terms are explicit algebraic expressions in local flow invariants, found
by a search over a space of expressions (operators, input variables,
constants) rather than by fitting a fixed form. In the RANS sources the
target is mostly the coefficient set $g^{(n)}$ of Pope's integrity-basis
expansion of the Reynolds-stress anisotropy $b_{ij}$, so the result is an
explicit non-linear eddy-viscosity model, objective by construction, that
can be implemented in a RANS code without a machine-learning runtime (Tang
et al. 2023, §I, §IV; see
[tensor-basis neural network](/methods/tensor-basis-neural-network.md)).
Wu et al. (2025) fit instead a scalar multiplier of a model term, and
Jakhar et al. (2026) the LES subgrid stress itself (sections below).
The interpretability of an explicit expression is the reason given for
the approach; Duraisamy (2021, §VII) adds that interpretable models from
symbolic regression do not automatically generalize beyond their training
scenarios.

## Search methods

| Method | Search | Recalled or read |
|---|---|---|
| gene-expression programming (Weatheritt & Sandberg 2016, 2017) | evolutionary search over expression trees | recalled by Duraisamy et al. (2019, §5.3), Duraisamy (2021, §III.A), Tang et al. (2023, §I) |
| CFD-driven gene-expression programming (Zhao et al. 2020) | candidates evaluated in the RANS solver during training | recalled by Tang et al. (2023, §I) |
| sparse regression, SpaRTA (Schmelzer et al.) | $\ell_1$-penalized linear regression over a library of candidate functions | recalled by Duraisamy (2021, §III.A, §IV.A), Tang et al. (2023, §III B) |
| deep symbolic regression, DSR (Petersen et al.) | a recurrent network samples expressions; trained by a risk-seeking policy gradient | read directly: Tang et al. (2023) |
| PySR (Cranmer) | genetic search over several populations with a complexity penalty | read directly: Wu et al. (2025) |
| sparse Bayesian regression, SBL-SpaRTA (Cherroud et al. 2022) | sparse Bayesian selection over a dictionary of invariant monomials; Gaussian posteriors of the coefficients | used, as recalled, by Oulghelou et al. (2025) |
| relevance vector machine, RVM (Tipping) | sparse Bayesian linear regression; basis functions pruned by the uncertainty of their weights | read directly: Jakhar et al. (2026), for an LES subgrid stress |

Tang et al. (2023, §I, §II C 1) contrast DSR with gene-expression
programming: GEP is "by nature a non-deterministic method", its
discovered form "can vary from different runs", and it "may produce
operations that violate imposed constraints, thus requiring rejections
post hoc", whereas DSR enforces the constraints during sampling.

## Deep symbolic regression for a $k$-$\varepsilon$ closure (Tang et al. 2023)

[Tang et al. (2023)](/sources/tang-2023.md) (arXiv v1) learn the
non-linear part of the anisotropy of the standard
[$k$-$\varepsilon$ model](/methods/k-epsilon-model.md) for incompressible
separated flows. The code is public (DSRRANS, §V).

**Closure (Eqs. 9, 15–16, 19).** With page-local
$\mathsf S_{ij}=\tfrac{k}{\varepsilon}\langle S_{ij}\rangle$,
$\mathsf W_{ij}=\tfrac{k}{\varepsilon}\langle\Omega_{ij}\rangle$, the
two-dimensional basis $T^{(1)}=\mathsf S$,
$T^{(2)}=\mathsf S\mathsf W-\mathsf W\mathsf S$,
$T^{(3)}=\mathsf S^2-\tfrac13\operatorname{tr}(\mathsf S^2)\,\mathsf I$ and the
invariants $I_1=\operatorname{tr}(\mathsf S^2)$, $I_2=\operatorname{tr}(\mathsf W^2)$
(as on [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md) and
[tensor-basis neural network](/methods/tensor-basis-neural-network.md)),
the Reynolds stress is

$$R_{ij}=\tfrac23k\delta_{ij}-2\nu_t\langle S_{ij}\rangle+2k\,b^\perp_{ij},\qquad b^\perp_{ij}=\frac{\beta_T}{20}\sum_{m=1}^{3}G^m(I_1,I_2)\,T^{(m)}_{ij},\quad\beta_T=7,$$

with $\nu_t=C_\mu k^2/\varepsilon$, $b^\perp_{ij}$ the non-linear part of
the registry anisotropy (page-local) and $\beta_T$ the paper's damping
factor (page-local; the registry $\beta$ is the field-inversion
multiplier). The paper normalizes the anisotropy as $R_{ij}/k-\tfrac23\delta_{ij}$,
twice the registry $b_{ij}$ (Eq. 10), and prints the prefactor $\beta/10$;
$\beta_T/20=0.35$ is that prefactor halved with the anisotropy *(compiler
check, not in the sources)*. The
factor $\beta_T/10$ is "selected following the suggestion by Shih" to
"ensure realizability"; the linear part is solved implicitly (§II C 2,
§III B). The $k$-$\varepsilon$ constants are $C_\mu=0.09$,
$C_{\varepsilon1}=1.44$, $C_{\varepsilon2}=1.92$, $\sigma_k=1.0$,
$\sigma_\varepsilon=1.3$ (Eqs. 4–8).

**Inputs.** Each invariant is squashed to $(-1,1)$ by
$\hat I=(1-e^{-I})/(1+e^{-I})$ before use, and the learned
coefficients are functions of the squashed invariants (Eq. 18; the hat
here is the paper's, not a test filter). The squashing equals
$\tanh(I/2)$ *(compiler check, not in the sources)*.

**Search (§II C 1, Algorithm 1, Apps. A–B).**

- *Generator.* An LSTM (three hidden layers of 64) emits a probability
  distribution over tokens ($+,-,\times,\div$, input invariants,
  constants), conditioned on the parent and sibling nodes; the token
  sequence is the pre-order traversal of an expression tree.
- *Constraints in sampling.* Probabilities of violating tokens are set to
  zero: minimum and maximum length (4 to 32 tokens), at least one
  non-constant child of a binary operator, no unary operator applied to
  its inverse, no nested trigonometric operators.
- *Constants.* Fitted for each sampled expression by BFGS in an inner
  loop, at most three per expression because the fit "can be
  prohibitively expensive" (§III B).
- *Risk-seeking policy gradient.* Each epoch samples a batch of 640
  expressions, keeps those whose reward is above the $(1-\epsilon_r)$
  quantile, $\epsilon_r=0.05$ (page-local risk factor; the paper's
  $\varepsilon$), and moves the generator weights along the mean of
  (reward minus quantile) times the score function, plus an entropy term
  with coefficient 0.005; learning rate 0.001, 20 epochs (Table II). The
  objective thus raises the reward of the best 5% of samples "without
  regard for samples below that threshold". This is
  [reinforcement learning](/methods/reinforcement-learning-closure.md)
  used offline, with no solver in the loop.

**Rewards.** The training target is the non-linear anisotropy of DNS on
the training case, interpolated onto the RANS grid; inputs come from the
converged baseline RANS (§II E). Model 1 uses the squashed normalized
root-mean-square error (Eq. 17),

$$r_1=\left(1+\frac1{\sigma_b}\sqrt{\frac1{n}\sum_{i=1}^{n}\big\|2b^{\perp,\mathrm{DNS}}_i-2b^\perp_i\big\|^2}\right)^{-1}\in(0,1],$$

with $\sigma_b$ the standard deviation of the DNS target $2b^{\perp,\mathrm{DNS}}$
and $n$ the number of training points (page-local); model 2 uses
$-\log\big(1+\tfrac1n\sum_i\|2b^{\perp,\mathrm{DNS}}_i-2b^\perp_i\|^2\big)$ (Eq.
21). The factor two carries the paper's doubled anisotropy into registry
notation.

**Learned model 1 (Eq. 20)**, in the squashed invariants:

$$\begin{aligned}G^1&=0.1893I_1+0.2229I_2+0.1176,\\G^2&=-0.1036I_1I_2^3-0.05182I_1^2I_2^2+0.1718I_1^2-0.2333,\\G^3&=-2.514I_1I_2^4-3.514I_2^3-0.01105I_2^2-2I_1I_2+2.98I_2.\end{aligned}$$

The coefficient of a higher-order basis tensor has the more complex form
with higher powers of the invariants (§III B). Model 2 (Eq. 22) has more
terms and higher powers (up to $I_1^2I_2^6$ in $G^2$). Allowing sin and
tan "could slightly improve the accuracy" but gave "extremely complex"
expressions and higher cost, so only the four arithmetic operators are
used (§III B).

**Tests (§III, Table I).** RANS in OpenFOAM (SIMPLE; second-order
upwind convection, central differences otherwise). The closure is
evaluated once on the converged baseline and frozen ("loose coupling");
the linear part is iterated to reconvergence (§II D; see
[model-consistent training](/methods/model-consistent-training.md)).

- *Training:* the parametrized
  [periodic hill](/benchmarks/periodic-hill.md) with steepness factor 0.8,
  $Re=5600$ on the hill height, about 9600 cells, DNS of Xiao et al.
- *Test:* hills with factors 0.5 and 1.0, and the
  [backward-facing step](/benchmarks/backward-facing-step.md) at $Re=5000$
  on the step height (about 46,000 cells; DNS of Le, Moin & Kim,
  experiment of Jovic & Driver).
- *Anisotropy.* On the training hill the baseline predicts the shear
  component reasonably but the normal components are "far removed" from
  DNS near the bottom wall; the learned model "captures the correct sign"
  of all components, with the largest gains in the streamwise and
  wall-normal normal components in separated regions (§III C, Fig. 7). In
  the barycentric map the baseline lies near the plane-strain line and
  the learned model is closer to DNS, with "a tiny minority of outliers"
  (Fig. 8).
- *Mean flow.* The baseline underestimates the separation bubble; the
  learned model enlarges it, and at the upstream crest its error is about
  half the baseline's ("nearly double larger" for the baseline; Fig. 9).
  On the test hills the velocity improves in the bulk; in the
  recirculation region the improvement is "not distinguishable" for the
  steepest hill (0.5) but present for 1.0 (§III D, Fig. 14). Error
  histograms show more points with low error, though the model "could
  produce higher errors in part of the computational domain" (Fig. 15).
  On the step the velocity profiles are "much closer" to DNS and
  experiment (Fig. 16).
- *Two models, one flow.* Models 1 and 2 give "strikingly close" velocity
  fields despite different forms, which the authors attribute to the mean
  velocity being a first-order statistic and the Reynolds stress a "less
  converged" second-order one (recalled from Thompson et al.; §III E, Fig.
  19). Model 2 has "no distinct advantages" for the anisotropy.
- *Cost.* Training takes about 100 h on 20 cores (Intel Xeon E5-2650);
  each RANS run converges in hundreds of seconds, at a cost "basically the
  same" as $k$-$\varepsilon$ (§III A–B).

## Symbolic regression of a field-inversion multiplier (Wu et al. 2025)

[Wu et al. (2025)](/sources/wu-2025.md) (author manuscript) fit a scalar,
not a tensor-basis coefficient: the multiplier $\beta$ of the
$\omega$-destruction term of the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md),
inferred by [field inversion](/methods/field-inversion-machine-learning.md)
on a curved backward-facing step and the NASA wall-mounted hump, either
everywhere (classic) or only outside attached boundary layers
(conditioned). The label is $\beta-1$.

**Features (Table 2).** Three invariants of the mean strain and rotation
normalized by $\beta^*\omega$, $\operatorname{tr}(\hat{\mathbf S}^2)$,
$\operatorname{tr}(\hat{\boldsymbol\Omega}^2)$ and
$\operatorname{tr}(\hat{\boldsymbol\Omega}^2\hat{\mathbf S}^2)$ (the third and
fourth of Pope's five vanish in 2-D), plus the vorticity Reynolds number
$\lvert\Omega\rvert d^2/\nu$, $P_k/\varepsilon$ from the Boussinesq stress, and
a feature found in the authors' earlier work. Since $\beta^*\omega=\varepsilon/k$,
the normalization is that of the page-local $\mathsf S$, $\mathsf W$ above,
so the first two invariants are $I_1$ and $I_2$ of Tang et al.; write
$I_5=\operatorname{tr}(\mathsf W^2\mathsf S^2)$ (page-local) for the third
*(compiler check, not in the sources)*.

**Search (§2.2, §3.2, Eqs. 16–17, 19–20, Table 3).** PySR with 20
populations of 80 expressions and 1000 iterations; unary operators exp,
tanh, $1/(1+x)$, $1/x$, binary $+,-,\times,\div$, min, max and power; a
weighted mean squared error; complexity
$C=N_{\mathrm{opr}}+2N_{\mathrm{var}}+4N_{\mathrm{const}}$ (page-local:
numbers of operators, variables and constants) capped at 16, the most
accurate expression within the cap being kept. Samples with
$\lvert\beta-1\rvert<0.05$ ("trivial") are randomly downsampled to the
number of the others and reweighted by the original ratio, after Yan et
al., leaving about 3000 samples per dataset; about 10 000 samples could
take "dozens of hours".

**Learned models (Table 4).**

$$\text{SR-CLS:}\quad\beta-1=-\tfrac{3}{500}\,I_5\tanh(-0.092\,I_2),\qquad\text{SR-CND:}\quad\beta-1=\min\big(0.00435\,I_2^2,\ 3.806\big).$$

Only the two rotation-carrying invariants survive. Both raise $\beta$ where
rotation or strain is large; a larger $\beta$ lowers $\omega$, raises the
eddy viscosity and the momentum diffusion into the recirculation, and
shrinks the separation, which the authors relate to the underestimated
eddy viscosity of RANS in separated shear layers, as recalled there
(§3.2, §4.2). Since $I_2^2\ge0$, SR-CND never lowers $\beta$ below 1 and
saturates at $\beta=1+3.806=4.806$ *(compiler check, not in the
sources)*. The models add about 15% (SR-CLS) and 10% (SR-CND) to the
runtime, against about 30 times for a random forest called every
iteration, as reported by Yin et al., whom they cite (§3.2). Results on separated flows,
the flat plate and the airfoil are on
[field inversion and machine learning](/methods/field-inversion-machine-learning.md):
both models improve separated flows similarly, and only SR-CND, inserted
behind the boundary-layer gate, leaves attached flow at the SST solution.

## Discovering an LES closure: the higher-order gradient model (Jakhar et al. 2026)

[Jakhar et al. (2026)](/sources/jakhar-2026.md) (arXiv v3; the
Supplemental Material is not in the file read) apply equation discovery to
the subgrid stress $\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$ of LES of
forced two-dimensional turbulence, the only LES application on this page.

**Library and regression (p. 2, Eq. 3).** Each element of $\tau_{ij}$ is
regressed separately, for each case, on a library of 930 products of
derivatives of the filtered velocity components (derivative orders up to
8 in total, powers up to 2) and of material derivatives of the filtered
vorticity or strain, included to represent memory effects. The relevance
vector machine minimizes the mean squared error over $n=100$
filtered-DNS snapshots and prunes the basis functions whose weight
uncertainty exceeds a threshold $\alpha_{\mathrm{RVM}}$ (page-local); a
higher threshold keeps more terms. The filter is Gaussian with $\Delta$
twice the LES grid spacing; 20 independent snapshots are used for testing.

**Selection criterion (pp. 2–3, Fig. 1).** The model is chosen at the
elbow of an L-curve of an a priori score against $\alpha_{\mathrm{RVM}}$.
With the correlation coefficient (CC) of $\tau_{ij}$ as score, as in
Zanna & Bolton and Jakhar et al. (2024) as cited, the elbow returns the
two-term second-order gradient model. With the authors' physics-informed
score, the minimum of the CCs of $\tau_{ij}$, of the inter-scale energy
transfer $P_\tau$ (page-local, the paper's symbol) and of its positive and
negative parts, the elbow moves to a five-term closure; a nine-term one
follows at higher thresholds, with negligible gain. Memory terms "never
emerged".

**The discovered closures (p. 3, Eq. 4)** are the truncations of the
Taylor expansion of $\tau_{ij}$ in the filter width:

$$\tau_{ij}=\frac{\Delta^2}{12}\frac{\partial\bar u_i}{\partial x_k}\frac{\partial\bar u_j}{\partial x_k}+\frac1{2!}\frac{\Delta^4}{12^2}\frac{\partial^2\bar u_i}{\partial x_k\partial x_l}\frac{\partial^2\bar u_j}{\partial x_k\partial x_l}+\frac1{3!}\frac{\Delta^6}{12^3}\frac{\partial^3\bar u_i}{\partial x_k\partial x_l\partial x_m}\frac{\partial^3\bar u_j}{\partial x_k\partial x_l\partial x_m}+O(\Delta^8),$$

whose first term is the [gradient model](/methods/gradient-model.md)
(NGM2), the first two NGM4, all three NGM6. The coefficients are those of
the exact expansion
$\overline{fg}-\bar f\bar g=\sum_{n\ge1}\frac1{n!}(\Delta^2/12)^n\,\partial^n\bar f\cdot\partial^n\bar g$
for a Gaussian filter of transfer function $\hat G(k)=\exp(-k^2\Delta^2/24)$
*(compiler check, not in the sources)*. No coefficient is fitted: only
$\Delta$ enters, which is the authors' argument that NGM4 is
"generalizable" (p. 4). In their reading the closures are truncations of
the non-local deconvolution operator, NGM4 "the minimal local truncation"
that meets their criteria (p. 5; see
[scale-similarity model](/methods/scale-similarity-model.md)).

**Tests (pp. 3–4, Figs. 2–4).** Four doubly periodic cases, solved
pseudo-spectrally (vorticity–streamfunction, Adams–Bashforth and
Crank–Nicolson): $Re=2\times10^4$ with forcing wavenumbers $(4,0)$, the
same on a $\beta$-plane with $(4,4)$ (zonal jets), $(25,25)$, and
$Re=10^5$ with $(25,25)$; DNS on $1024^2$ ($2048^2$ for the last), LES on
$128^2$ (cases 1–2) and $512^2$ (cases 3–4). A priori, mean $\pm$ standard
deviation over the four cases:

| Closure | mean energy transfer / filtered DNS | mean enstrophy transfer / filtered DNS |
|---|---|---|
| NGM2 | 0 | $1.00\pm0.01$ |
| NGM4 | $0.62\pm0.04$ | $1.00\pm0.01$ |
| NGM6 | $0.78\pm0.04$ | $1.00\pm0.01$ |
| Smagorinsky, $C_s=0.17$ | $-62.24\pm37.80$ | $-3.22\pm1.18$ |
| dynamic Smagorinsky | $-28.48\pm15.38$ | $-1.49\pm0.45$ |
| dynamic Leith | $-6.91\pm2.73$ | $-0.37\pm0.06$ |

NGM4 and NGM6 reach a CC near 0.99 for $\tau_{ij}$ and reproduce the
backscatter of filtered DNS (see
[energy backscatter](/definitions/energy-backscatter.md)); the
eddy-viscosity closures, $\nu_t=(C_s\Delta)^2\lvert\bar S\rvert$ and the
Leith form $\nu_t=(C_l\Delta)^3\lvert\nabla\bar\omega_z\rvert$ (page-local
$C_l$, $\bar\omega_z$ the filtered 2-D vorticity), with dynamic
coefficients clipped to $\nu_t\ge0$, are "purely and excessively
diffusive" (App. D). A posteriori, NGM2 is unstable "for any case and any
LES resolution"; NGM4 and NGM6 are long-term stable when the LES resolves
more than 80% of the DNS enstrophy, capture the tails of the vorticity
PDF and give better short-term forecasts than the eddy-viscosity
closures, which underestimate the large-scale enstrophy. NGM6 brings no a
posteriori advantage, "suggesting that in practice, using NGM4 might be
enough" (pp. 4–5).

## Sparse Bayesian experts for model blending (Oulghelou et al. 2025)

[Oulghelou et al. (2025)](/sources/oulghelou-2025.md) (arXiv v2, §2–3,
Table 1) use three SST models whose corrections were regressed with
SBL-SpaRTA, citing Cherroud et al. (2022, 2025): an
additive anisotropy $b^\Delta_{ij}$ and a $k$-equation term
$2k\,b^R_{ij}\partial_j\langle u_i\rangle$ (page-local), each a sum over the
three 2-D basis tensors built from $S_{ij}/\omega$ and $\Omega_{ij}/\omega$,
with coefficients selected from a dictionary of monomials of the two
invariants and Gaussian posteriors (§2.1). The printed models are

| Expert | $b^\Delta_{ij}$ | $b^R_{ij}$ | Training data |
|---|---|---|---|
| separated flows | $(5.21\pm0.0173)\,T^{(2)}_{ij}$ | $(0.681\pm0.02)\,T^{(1)}_{ij}$ | periodic hill, converging–diverging channel, curved backward-facing step |
| near-sonic jet | $(0.25\pm7.26\times10^{-3})\,T^{(1)}_{ij}$ | 0 | PIV of an axisymmetric jet |

with the basis tensors of this paper normalized by $\omega$ rather than
$k/\varepsilon$, i.e. $T^{(1)}=\beta^*\mathsf S$ *(compiler check, not in the
sources)*. The posterior standard deviations are small, so the coefficients
are treated as deterministic (§3). Each expert helps its own class and
hurts others: the separated-flow model raises the eddy viscosity and
spoils the channel log layer (mean absolute error of $u^+$ 2.41 against
0.44 for SST), the jet model lowers it and fails in the channel (8.97)
(§4.2.1, Table 3). The paper combines them with learned spatial weights;
see [model aggregation](/methods/turbulence-model-aggregation.md).

## Symbolic regression in transition modelling (Pacciani et al. 2025)

[Pacciani et al. (2025)](/sources/pacciani-2025.md) do not run a symbolic
search, but their reformulated
[laminar-kinetic-energy transition model](/methods/laminar-kinetic-energy-transition-model.md)
is shaped by earlier gene-expression-programming results and built as a
base for later ones (§1, §3.2):

- *Motivation.* As recalled there, Fang et al. (2024) trained the
  production and transfer terms of the authors' earlier model with a
  multi-objective, multi-case machine-learning algorithm and found
  opposite correction trends for separated-flow and bypass transition; the
  authors read this as a lack of generality of the baseline (§1, §3.2).
- *Inputs taken from learned expressions.* The new laminar-fluctuation
  production uses the length scale $\lvert\Omega\rvert d^2/U$
  (page-local: $U$ the local velocity magnitude, $d$ the wall distance;
  vorticity or strain magnitude, Eq. 10), "taken from" expressions trained
  by gene-expression programming in Akolekar et al. (2021, 2022) (§4.1).
  The separation switch uses $r=\lvert S\rvert d/U$ because that group
  "appears" in machine-learnt threshold terms (Akolekar et al.; Fang et al.)
  (§4.5, Eqs. 23–27).
- *Training targets left open.* The onset threshold, the separation
  switch, its critical vorticity Reynolds number and the production term
  are designed as candidate functions for later GEP training; the
  separation switch "has no ambition of generality" (§4.5).

The paper itself calibrates its constants by hand on the
[ERCOFTAC T3 flat plates](/benchmarks/ercoftac-t3-flat-plate.md) and does
not report a learned expression.

## Qualifications

- **Evidence base.** Tang et al. (2023) train on one 2D case and compare
  only with the $k$-$\varepsilon$ baseline; no other data-driven or
  non-linear model is run. Realizability is supported by barycentric
  plots, with outliers for model 1, not by a proof.
- **Generalization of explicit models.** As recalled by Duraisamy et al.
  (2019, §5.3), gene-expression-programming models trained on
  low-Reynolds-number DNS of a backward-facing step show "a high level of
  uncertainty" on the periodic hill; Tang et al. (2023) train on a hill
  and test on a step, the reverse direction, with one training case.
- **Determinism.** Tang et al. call DSR "deterministic" (§I), and §II C 1
  says "the token with the highest probability is then sampled", while
  their Algorithm 1 samples expressions from the generator's distribution.
- **Constant coefficients.** Their statement that sparse-regression
  closures "only contain constant coefficients" (§III B) conflicts with
  the description of sparse regression by Duraisamy (2021, §III.A); the
  open entry is under Contradictions on
  [tensor-basis neural network](/methods/tensor-basis-neural-network.md).
  The SBL-SpaRTA experts printed by Oulghelou et al. (2025, Table 1) have
  constant coefficients although their dictionary contains invariant
  monomials (§2.1); the open entry on that page records this.
- **Scalar against tensor targets.** Wu et al. (2025) regress one scalar
  multiplier of a transport-equation term, so their models keep the
  Boussinesq form; Tang et al. (2023) and the experts of Oulghelou et al.
  (2025) regress coefficients of the anisotropy basis, and Jakhar et al.
  (2026) each component of the LES subgrid stress over a library of
  derivative products.
- **Generalization claims of Wu et al. (2025)** rest on two training
  flows and six test geometries (periodic hills at three slopes, the
  NLR-7301 airfoil, the SAE notchback, the Ahmed body, the flat plate, the
  NACA 0012), all steady RANS (§3–4).
- **Printed slips in Tang et al. (2023).**
  - Eq. 16 writes the non-linear part as $\sum G^m T^m$ without the factor
    $\beta_T/10$ that Eq. 19 includes; the printed coefficients of Eqs. 20
    and 22 belong to the form with the factor.
  - The captions of Figs. 17–18 swap the equation numbers of models 1 and
    2 (Eq. 20 is model 1, Eq. 22 model 2).
  - The risk-seeking objective (Eq. B1) is printed as
    $\mathbb E_{\tau\sim p(\tau\mid\theta)}[R(\tau)\ge R_\varepsilon(\theta)]$,
    the expectation of an inequality; the text describes the expected
    reward of the samples above the quantile.
  - §III C lists the first barycentric station as $x/h=1.5$; the Fig. 8
    caption gives 0.5. §III D swaps the reference numbers of the step DNS
    and experiment. The Fig. 15 caption calls the difference
    $U_p-U_{\mathrm{DNS}}$ a relative error.
  - The input of the learned map is written $\omega_i(\boldsymbol S,\boldsymbol R)$
    in §II E, never defined.
- **Jakhar et al. (2026): what the version read supports.** The
  definitions of $P_\tau$ and of the enstrophy transfer, the stability
  runs (Fig. S2) and the generalized Taylor expansion are in the
  Supplemental Material, absent from the file read. The text states
  coarse-graining to "4 to 64×" coarser LES grids, while case 4 is also
  run at $N_x=1024$ against a $2048^2$ DNS, a factor 2 *(compiler check,
  not in the sources)*. The paper states that the expansion "had not been
  previously pursued" and that NGM4 is "the first closure to
  simultaneously excel in both a priori and a posteriori tests" (pp. 4–5);
  these are the authors' claims. The result concerns 2-D turbulence, where
  NGM2 transfers no energy between scales; the gradient model in 3-D is
  treated on its own page.
- **Symbol clashes in the source.** $\varepsilon$ is both the dissipation
  and the risk factor, $\alpha$ both the learning rate and the hill
  steepness, $\sigma$ both a standard deviation and the sigmoid.

# Citations

- [Tang et al. (2023)](/sources/tang-2023.md) — arXiv v1: §I (GEP, CFD-driven GEP recalled), §II C 1, Algorithm 1, Apps. A–B, Eq. B1 (DSR), §II C 2, Eqs. 4–19 (closure, constants, split, squashing, rewards), §II D–E (coupling, workflow), §III A–E, Table I–II, Eqs. 20–22, Figs. 7–19, §IV, §V.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §III.A, §IV.A (symbolic and sparse regression, $\ell_1$ loss), §VII (interpretability does not imply generalization).
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §5.3 (gene-expression programming recalled; uncertainty on the periodic hill when trained on a backward-facing step).
- [Wu et al. (2025)](/sources/wu-2025.md) — author manuscript: §2.2, Eqs. 16–17, 19–20, Tables 2–4 (PySR set-up, features, rebalancing, learned models); §3.2 (interpretation, cost); §4.2.
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — arXiv v2: §2–2.1, Eqs. 7–10, Table 1 (SBL-SpaRTA experts); §3; §4.2.1, Table 3.
- [Jakhar et al. (2026)](/sources/jakhar-2026.md) — arXiv v3: pp. 1–5, Eqs. 3–4, Figs. 1–4 (library, RVM, criterion, NGM closures, a priori table, a posteriori results, cases); App. B, Eq. 5; App. C (solver); App. D (eddy-viscosity baselines).
- [Pacciani et al. (2025)](/sources/pacciani-2025.md) — §1, §3.2 (GEP corrections of the earlier model recalled), §4.1, Eq. 10 (length scale from trained expressions), §4.5, Eqs. 23–27 (separation switch as a training candidate).
