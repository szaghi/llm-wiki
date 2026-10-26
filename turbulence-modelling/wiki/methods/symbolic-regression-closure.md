---
type: Method
title: "Symbolic-regression turbulence closures"
description: "Closures whose model terms are explicit algebraic expressions found by a search over expression space (gene-expression programming, sparse regression, deep symbolic regression), usually as coefficients of Pope's integrity basis in RANS; covers a deep-symbolic-regression closure of k-ε, its rewards, learned models and tests on separated flows."
status: established
aliases: [symbolic regression, deep symbolic regression, DSR, gene-expression programming, GEP, sparse regression, SpaRTA, explicit algebraic closure discovery, DSRRANS]
tags: [symbolic-regression, rans, data-driven, machine-learning, separated-flow]
timestamp: 2026-10-26T10:26:00Z
---

# Symbolic-regression turbulence closures

A **symbolic-regression closure** is a turbulence model whose unknown
terms are explicit algebraic expressions in local flow invariants, found
by a search over a space of expressions (operators, input variables,
constants) rather than by fitting a fixed form. In the sources the target
is the coefficient set $g^{(n)}$ of Pope's integrity-basis expansion of the
Reynolds-stress anisotropy $b_{ij}$, so the result is an explicit
non-linear eddy-viscosity model, objective by construction, that can be
implemented in a RANS code without a machine-learning runtime (Tang et al.
2023, §I, §IV; see
[tensor-basis neural network](/methods/tensor-basis-neural-network.md)).
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
- **Symbol clashes in the source.** $\varepsilon$ is both the dissipation
  and the risk factor, $\alpha$ both the learning rate and the hill
  steepness, $\sigma$ both a standard deviation and the sigmoid.

# Citations

- [Tang et al. (2023)](/sources/tang-2023.md) — arXiv v1: §I (GEP, CFD-driven GEP recalled), §II C 1, Algorithm 1, Apps. A–B, Eq. B1 (DSR), §II C 2, Eqs. 4–19 (closure, constants, split, squashing, rewards), §II D–E (coupling, workflow), §III A–E, Table I–II, Eqs. 20–22, Figs. 7–19, §IV, §V.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §III.A, §IV.A (symbolic and sparse regression, $\ell_1$ loss), §VII (interpretability does not imply generalization).
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §5.3 (gene-expression programming recalled; uncertainty on the periodic hill when trained on a backward-facing step).
- [Pacciani et al. (2025)](/sources/pacciani-2025.md) — §1, §3.2 (GEP corrections of the earlier model recalled), §4.1, Eq. 10 (length scale from trained expressions), §4.5, Eqs. 23–27 (separation switch as a training candidate).
