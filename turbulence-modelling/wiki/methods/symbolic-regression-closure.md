---
type: Method
title: "Symbolic-regression turbulence closures"
description: "Closures whose model terms are explicit algebraic expressions found by a search over expression space (gene-expression programming, sparse and sparse Bayesian regression, deep symbolic regression, PySR), as integrity-basis coefficients, a scalar multiplier of a model term or an LES subgrid stress; covers learned k-ε and SST corrections and the higher-order gradient model."
status: established
aliases: [symbolic regression, PySR, SBL-SpaRTA, SR-CLS, SR-CND, deep symbolic regression, DSR, gene-expression programming, GEP, sparse regression, SpaRTA, explicit algebraic closure discovery, DSRRANS, relevance vector machine, RVM, NGM4, NGM6, equation discovery]
tags: [symbolic-regression, rans, les, sgs-model, data-driven, separated-flow]
timestamp: 2026-10-27T15:50:00Z
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
Li et al. (2021) and Jakhar et al. (2026) the LES subgrid stress itself
(sections below).
The interpretability of an explicit expression is the reason given for
the approach; Duraisamy (2021, §VII) adds that interpretable models from
symbolic regression do not automatically generalize beyond their training
scenarios.

## Search methods

| Method | Search | Cited or read |
|---|---|---|
| gene-expression programming (Weatheritt & Sandberg 2016, 2017) | evolutionary search over expression trees | cited by Duraisamy et al. (2019, §5.3), Duraisamy (2021, §III.A), Tang et al. (2023, §I), Sandberg & Michelassi (2022, §4.3), Sandberg & Zhao (2022, §4); read directly for an LES subgrid stress: Li et al. (2021) |
| CFD-driven gene-expression programming (Zhao et al. 2020) | candidates evaluated in the RANS solver during training | cited by Tang et al. (2023, §I), Sandberg & Michelassi (2022, §4.3), Sandberg & Zhao (2022, §3.4), Ruggeri et al. (2022, §III) |
| sparse regression, SpaRTA (Schmelzer et al.) | $\ell_1$-penalized linear regression over a library of candidate functions | cited by Duraisamy (2021, §III.A, §IV.A), Tang et al. (2023, §III B), Sandberg & Zhao (2022, §3.4, Eq. 8), Cherroud et al. (2022, §1, App. B) |
| deep symbolic regression, DSR (Petersen et al.) | a recurrent network samples expressions; trained by a risk-seeking policy gradient | read directly: Tang et al. (2023) |
| PySR (Cranmer) | genetic search over several populations with a complexity penalty | read directly: Wu et al. (2025) |
| sparse Bayesian regression, SBL-SpaRTA (Cherroud et al. 2022) | sparse Bayesian selection over a dictionary of invariant monomials; Gaussian posteriors of the coefficients | read directly: Cherroud et al. (2022); used by Oulghelou et al. (2025) |
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

**Closure (Eqs. 9, 15–16, 19).** With registry-§11
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
  converged" second-order one (citing Thompson et al.; §III E, Fig.
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
the normalization is that of the registry-§11 $\mathsf S$, $\mathsf W$ above,
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
shrinks the separation, which the authors relate, citing earlier work,
to the underestimated eddy viscosity of RANS in separated shear layers
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
forced two-dimensional turbulence; the three-dimensional LES application
on this page is that of Li et al. (2021), next section.

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

## Gene-expression programming for an LES subgrid stress (Li et al. 2021)

[Li et al. (2021)](/sources/li-2021.md) use gene-expression programming
(GEP) to learn an explicit algebraic subgrid model for LES of forced
incompressible [homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md);
they call it the first GEP subgrid model applied to fully developed
isotropic turbulence and tested both a priori and a posteriori, after
Schoepplein et al. (2018, a priori only, on premixed-flame DNS) and
Reissmann et al. (2021, a posteriori on the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) without
turbulence statistics), both cited in their §I.

**The algorithm (§II B, Eqs. 15–16, Table I).** GEP is a genetic
algorithm for symbolic regression: the coefficient functions are encoded
as chromosomes, a population evolves over generations by selection,
mutation (diversity) and crossover (coupling strong genes), and the
fittest individual is written out as an expression. The search is a
global random optimization, not a local gradient-based one. The fitness,
minimized, is the mean relative Frobenius-norm error of the deviatoric
stress over the $n_p$ training points (page-local),
$\frac1{n_p}\sum_k\lVert\tau^{d,\mathrm{DNS}}(k)-\tau^{d,\mathrm{m}}(k)\rVert_F/\lVert\tau^{d,\mathrm{DNS}}(k)\rVert_F$.
Hyperparameters: 100 individuals, 500 generations, probability of
invariants 0.5, set from earlier experience and resources; the code is
the in-house EVE3 (University of Melbourne). Sandberg & Michelassi (2022,
margin definition, p. 267) define GEP in the same terms, as an algorithm that
"evolves a population of syntactically correct candidate symbolic
expressions over various generations toward a specified and constrained
training objective".

**Representation (Eqs. 9–14).** The deviatoric subgrid stress is expanded
on Pope's ten-tensor basis of the filtered strain and rotation, scaled by
$\Delta$ and the strain magnitude (details and the normalization on
[tensor-basis neural network](/methods/tensor-basis-neural-network.md)).
In registry notation, with page-local $\mathsf s_{ij}=\sqrt2\,\bar S_{ij}/\lvert\bar S\rvert$
and $\mathsf w_{ij}=\sqrt2\,\bar\Omega_{ij}/\lvert\bar S\rvert$ (the paper
normalizes by $\sqrt{\bar S_{mn}\bar S_{mn}}=\lvert\bar S\rvert/\sqrt2$),

$$\tau^d_{ij}=\frac{\Delta^2\lvert\bar S\rvert^2}{2}\sum_{n=1}^{N_0}g^{(n)}(I_1,\dots,I_4)\,T^{(n)}_{ij}(\mathsf s,\mathsf w),$$

with $N_0$ (page-local) the number of basis tensors offered to the
search, from 1 to 10.

**Data (§III A).** A $1024^3$ pseudospectral DNS at $Re_\lambda\approx260$
(from Xie et al. 2020, as cited) is filtered with a top-hat filter of width
$\Delta=16$ DNS spacings, in the inertial range with about 5% of the
kinetic energy filtered, and coarse-grained to $64^3$ points; $8\times64^3$
points are split 70/30 between training and testing.

**The retained model GEP(4) (Eq. 22).** Trained with
$T^{(1)}$–$T^{(4)}$, the search returns constant coefficients,

$$\tau^d_{ij}=\frac{\Delta^2\lvert\bar S\rvert^2}{2}\left(-0.01\,T^{(1)}_{ij}-0.1\,T^{(2)}_{ij}+0.07\,T^{(3)}_{ij}-0.11\,T^{(4)}_{ij}\right).$$

Over 30 training runs the coefficients are invariant-free constants in
83% ($g^{(1)}\in[-0.02,0]$), 93% ($g^{(2)}\in[-0.11,-0.10]$), 60%
($g^{(3)}\in[0.06,0.10]$) and 97% ($g^{(4)}\in[-0.11,-0.10]$) of the runs
(Table III). The linear term is an eddy viscosity
$\nu_t=\tfrac{0.01}{2\sqrt2}\Delta^2\lvert\bar S\rvert\approx3.5\times10^{-3}\Delta^2\lvert\bar S\rvert$,
i.e. a Smagorinsky form with $C_s\approx0.059$ *(compiler check, not in
the sources)*; the authors state only that this coefficient is much
smaller than in (dynamic) Smagorinsky models, so the model is less
dissipative, and relate the dominant terms $T^{(2)}$ and $T^{(4)}$ to the
rotation rate and to intense vortex filaments (§III D, §IV).

**Tests.** A priori, the correlation coefficient with filtered DNS rises
from 0.321 for one tensor to 0.888 for four and falls beyond seven
(Table II); a posteriori, $128^3$ LES (grid spacing $\Delta/2$) with GEP(4)
matches filtered DNS in spectra, structure functions, stress PDFs and the
backscatter tail of the SGS energy flux about as well as an artificial
neural network of Xie et al. (2020) and better than the dynamic
Smagorinsky and dynamic mixed models (§III C, Figs. 2–8); details on
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
and [neural-network SGS models](/methods/neural-network-sgs-model.md). Its
cost per iteration is slightly above that of the dynamic Smagorinsky model
and much below the network's (Fig. 13; no timings printed). The
generalization to $64^3$ and $32^3$ LES and to $Re_\lambda=180$ and 250 is
shown with energy spectra only (§III E, Figs. 11–12). The authors limit
their conclusions to isotropic turbulence (§IV).

## Gene-expression programming in turbomachinery RANS (Sandberg & Michelassi 2022)

The review of [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md)
(§3.2.3, §4.3) cites the GEP closures of Akolekar et al., Lav et al. and
Zhao et al. for turbomachinery wakes. The explicit algebraic stress model
that it cites from Akolekar et al. (2019) (Eq. 2) reads in registry
notation

$$\langle\rho u_i''u_j''\rangle-\tfrac23\langle\rho\rangle k\,\delta_{ij}=-2\mu_t\,S^d_{ij}+2\langle\rho\rangle k\sum_{n=1}^{4}g^{(n)}(I_1,I_2)\,T^{(n)}_{ij},$$

with $S^d_{ij}$ the deviatoric strain of the Favre-averaged velocity, the
$n=1$ term an "additional linear term" and $n=2$–4 the non-linear terms;
GEP finds the $g^{(n)}$ (the review's $\zeta_k$) as functions of two
invariants by minimizing a normalized mean-square error $J$ against
phase-lock-averaged DNS, and the performance measure is the percentage
reduction of $J$ over the linear baseline (Fig. 7). The review reports,
citing the original works:

- *Phase dependence.* Models trained on one phase of phase-locked
  low-pressure-turbine data perform well on that phase but can perform
  poorly on others (developed on phase 10, tested on phase 18); the
  non-linear terms contribute more in phases with wake–wake interaction,
  and two distinct models suffice to improve wake mixing over all phases
  (Akolekar et al. 2019; §4.3, Fig. 7).
- *Triple decomposition.* A closure trained on only the stochastic part of
  a triple decomposition of wake LES data, so that the shedding is not
  accounted twice in URANS, has a much smaller turbulent-diffusion
  coefficient and improves near- and far-wake prediction (Lav et al. 2019;
  §3.2.3).
- *CFD-driven training.* With a full RANS solve per candidate (Zhao et al.
  2020), much less data are needed, and models trained on high-pressure-
  turbine data predicted low-pressure-turbine wake-loss profiles for other
  geometries and very different Reynolds numbers (§4.3; see
  [model-consistent training](/methods/model-consistent-training.md)).

The authors' outlook is that machine learning will not yield models that
predict all turbulent flow features in turbomachines, but will patch the
weaknesses of specific mechanisms in multi-expression approaches (Future
issue 5). Cascade context is on
[turbine cascades](/benchmarks/turbine-cascade.md).

## Sparse Bayesian learning of SST corrections (Cherroud et al. 2022)

[Cherroud et al. (2022)](/sources/cherroud-2022.md) introduce
SBL-SpaRTA, a stochastic counterpart of the deterministic SpaRTA of
Schmelzer et al. (2020a, as cited), in which one regression both selects
the terms and gives their posterior distributions (§1, §3). The SST
anisotropy receives an additive correction and the $k$ and $\omega$
equations a production correction (§2.1, Eqs. 5, 12; registry-§11
$b^\Delta_{ij}$, $b^R_{ij}$):

$$R_{ij}=2k\Big(\tfrac13\delta_{ij}-\frac{\nu_t}{k}\langle S_{ij}\rangle+b^\Delta_{ij}\Big),\qquad P_k\ \to\ P_k+2k\,b^R_{ij}\,\partial_j\langle u_i\rangle,$$

each a sum over the three 2-D basis tensors $T^{(1)}$–$T^{(3)}$ built from
the mean strain and rotation divided by $\omega$, with coefficients that
are functions of the two invariants $I_1$, $I_2$ (page-local: the squared
norms of the $\omega$-scaled strain and rotation) (Eqs. 7–8, 13). The
production term is written here in the form the source prints; its sign
convention is discussed under Qualifications.

- **Targets** come from the $k$-corrective-frozen procedure: the SST
  transport equations are solved with the high-fidelity mean velocity, $k$
  and anisotropy frozen, giving $\omega$ and the residual of the $k$
  equation (Eqs. 9–11; see
  [model-consistent training](/methods/model-consistent-training.md)). The
  regressed anisotropy target is $2k\,b^\Delta_{ij}$, because
  $b^\Delta_{ij}$ is $0/0$ at the wall (§2.2).
- **Dictionary.** Monomials of $I_1$ and $I_2$ up to degree nine and mixed
  products of total degree two to four, 25 per coefficient function, 75
  per target and 150 in all (Eq. 14).
- **Regression.** Tipping's sparse Bayesian learning: Gaussian likelihood,
  a zero-mean Gaussian prior on each weight with its own precision
  (automatic relevance determination), and, in place of Tipping's Gamma
  hyperprior, the "demi-Bayesian LASSO" hyperprior
  $p(\alpha_i)\propto\exp(-\lambda/(2\alpha_i))$ (page-local $\alpha_i$
  precisions, $\lambda$ one sparsity parameter for all) of Balakrishnan &
  Madigan, as cited, for "improved sparsity" (Eqs. 16–20). Type-II maximum
  likelihood gives fixed-point updates of the precisions and the noise;
  weights whose precision reaches a limit are pruned; the weight posterior
  is Gaussian (Eqs. 24–27).
- **Selection.** $\lambda\in\{10^2,10^3,10^4,10^5,2\times10^5\}$ is chosen
  a posteriori: the MAP models run in OpenFOAM, and a score sums the
  relative mean-square-error reductions over baseline SST of velocity,
  $k$, Reynolds shear stress and $C_f$, with the left-out test flow
  weighted twice (Eqs. 29–32).
- **Data.** Three 2-D separated flows in leave-one-out scenarios:
  [periodic hill](/benchmarks/periodic-hill.md) at $Re=10\,595$,
  converging–diverging channel at $Re=12\,600$ and curved
  [backward-facing step](/benchmarks/backward-facing-step.md) at
  $Re=13\,700$, with full-field LES or DNS (§4.1, Table 1).

**Learned models (App. A).** As $\lambda$ grows the anisotropy correction
thins out, while the production correction reduces to one $T^{(1)}$ term
at every $\lambda$, its coefficient decreasing (0.989, 0.982, 0.959, 0.887,
0.8433 in the first scenario); above $2\times10^5$ both vanish and SST is
recovered (§4.2). At $\lambda=10^2$ the anisotropy correction has
invariant-dependent coefficients, e.g.
$[(-0.496\pm0.0133)+(21.6\pm0.366)I_1+(17.4\pm0.374)I_2]\,T^{(1)}+\dots$
(Eq. A.1). The three selected models, all at $\lambda=2\times10^5$, have
no anisotropy correction and one stochastic production coefficient,
$0.8433\pm0.0142$, $0.382\pm0.0184$ and $0.197\pm0.0156$ (Eqs.
A.13–A.15); the deterministic SpaRTA models of Schmelzer et al. for the
same scenarios have production coefficients 0.39, 1.39 and 0.93 (App. B).

**Results (§4.2–4.3, Figs. 1–8).**

- Every learned model has a much lower velocity error than SST; richer
  models are slightly better on the training flows, sparser ones
  generalize better (Fig. 1).
- Scored on velocity, $k$, shear stress and $C_f$ together, the best
  models are the production-only ones, with average improvements $m^G$
  of 6.0%, 28% and 31% for the three scenarios (Table 2); scored on
  velocity alone, models with an anisotropy correction win in two
  scenarios, a limit the authors attribute to stresses that depend on the
  mean velocity gradient only.
- The production correction raises the eddy viscosity in the separated
  region and reattaches the boundary layer earlier; on the
  converging–diverging channel no model locates the small LES bubble, and
  on the curved step attached-flow $C_f$ is slightly worse than SST; all
  models over-predict $k$ in separated regions (Figs. 6–7).
- The selected models beat the physics-based BSL-EARSM of Menter et al.
  (2012) on the three flows (App. C; see
  [explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md)).

The authors conclude that correcting the production is "generally
sufficient" for these 2-D separated flows, consistent with Schmelzer et
al. (2020a), but not for 3-D flows, where Huijing et al. (2021, as cited)
needed non-linear terms (§5). Uncertainty propagation and Sobol indices
are on [model-form uncertainty](/definitions/model-form-uncertainty.md).

## Gene-expression programming for stresses and heat fluxes (Sandberg & Zhao 2022)

The review of [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md)
extends the turbomachinery account of Sandberg & Michelassi (2022, above)
to heat flux and transition, citing the original works (§3–4):

- *Basis.* The target is the coefficient set of Pope's ten tensors and
  five invariants of the time-scale-normalized strain and rotation (Eqs.
  2–4); for statistically 2-D flows only $T^{(1)}$–$T^{(4)}$ and two
  invariants are used (§4.1). The time scale comes from a frozen solve of
  the $\omega$ or $\varepsilon$ equation with reference velocity and
  stresses (Parneix et al. 1998, as cited, §3.2).
- *Stresses.* Trained on a backward-facing step, GEP gave "excellent" a
  posteriori periodic-hill predictions with the first four tensors and two
  invariants, but some individuals had very large coefficients,
  non-realizable stresses and unstable runs, removable thanks to the
  explicit form though "not robustly" automatically; on jets in crossflow
  GEP and a tensor-basis network both improved greatly on the linear
  baseline and both failed where the streamwise vorticity is strongest
  (§4.1).
- *Heat flux.* GEP was used for a spatially varying turbulent Prandtl
  number, with mean values 0.42–0.6 on trailing-edge slots (Haghiri &
  Sandberg 2020), "well below typically used values of 0.85–0.9", and for a three-term
  tensor-diffusivity closure selected by recursive feature elimination
  (Weatheritt et al. 2020), whose leading terms are the generalized and
  higher-order generalized gradient-diffusion forms (§4.2; formulas on
  [explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md)).
- *Unsteady flows.* Phase-wise GEP closures where the
  [spectral gap](/definitions/spectral-gap.md) exists, and closures of the
  stochastic part of a triple decomposition where it does not (§4.4).
- *Multi-expression training.* Coupled stress and heat-flux expressions
  trained together with Pareto-based multi-objective selection (Waschkowski
  et al. 2022) improved both velocity and temperature of vertical natural
  convection (§4.5; see
  [model-consistent training](/methods/model-consistent-training.md)).

The authors weigh symbolic regression as interpretable and easy to
implement but less expressive than deep networks (§3.1). He et al.
(2022, §1) list GEP and sparse regression among the explainable
alternatives to black-box corrections, without using them
([He et al. (2022)](/sources/he-2022-b.md)).

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

- *Motivation.* The authors cite Fang et al. (2024), who trained the
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
- **Generalization of explicit models.** Duraisamy et al. (2019, §5.3)
  cite gene-expression-programming models trained on
  low-Reynolds-number DNS of a backward-facing step that show "a high level
  of uncertainty" on the periodic hill; Sandberg & Zhao (2022, §4.1)
  describe GEP trained on a backward-facing step as giving "excellent"
  a posteriori periodic-hill predictions (above). Both are second-hand
  accounts of cited work. Tang et al. (2023) train on a hill and test on a
  step, the reverse direction, with one training case.
- **Determinism.** Tang et al. call DSR "deterministic" (§I), and §II C 1
  says "the token with the highest probability is then sampled", while
  their Algorithm 1 samples expressions from the generator's distribution.
- **Constant coefficients.** Their statement that sparse-regression
  closures "only contain constant coefficients" (§III B) conflicts with
  the description of sparse regression by Duraisamy (2021, §III.A); the
  open entry is under Contradictions on
  [tensor-basis neural network](/methods/tensor-basis-neural-network.md).
  The SBL-SpaRTA experts printed by Oulghelou et al. (2025, Table 1) and
  the selected models of Cherroud et al. (2022, Eqs. A.13–A.15) have
  constant coefficients although their dictionaries contain invariant
  monomials; Cherroud et al. (Eq. A.1) also print invariant-dependent
  coefficients at small sparsity. The open entry on that page records
  both.
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
- **Li et al. (2021): scope and slips.** The a priori correlations of
  Table II are each the best of 20 training runs. The coefficients of Eq.
  22, $(-0.01,-0.1,0.07,-0.11)$, differ from those of the four-term model
  of the ablation, $(-0.02,-0.11,0.07,-0.10)$ (Table IV, model 6); the
  paper does not say which set the ablation uses. §III A states that
  "every 17th grid point in each direction" of the $1024^3$ field gives
  "$16^3$ different datasets of $64^3$" points; $1024/64=16$, so the
  stated datasets correspond to a stride of 16 *(compiler check, not in
  the sources)*. The LES uses a "high-order dissipative numerical method"
  at high wavenumbers (§II A), whose share of the dissipation is not
  separated from the model's.
- **Sandberg & Michelassi (2022), Eq. 2 sign.** The review defines the
  Reynolds stress as $-\overline{\rho u_i''u_j''}$ (p. 259), whose trace is
  $-2\bar\rho k$; its Eq. 2 subtracts $\tfrac23\bar\rho k\delta_{ij}$ and
  writes $-2\mu_t$ on the right, which is the form for the
  positive-trace stress, so Eq. 2 is consistent only with the opposite
  sign convention *(compiler check, not in the sources)*. The equation
  above is written in the registry's positive convention.
- **Cherroud et al. (2022): sign of the production and printed
  slips.** With the Reynolds stress entering the momentum equation as
  $-\partial_jR_{ij}$ (their Eq. 2), the production is
  $-R_{ij}\partial_j\langle u_i\rangle=2k\big(\tfrac{\nu_t}{k}\langle S_{ij}\rangle-b^\Delta_{ij}\big)\partial_j\langle u_i\rangle$,
  whereas their Eq. 11 prints the opposite overall sign, which would make
  the Boussinesq production negative *(compiler check, not in the
  sources)*; Eq. 12, $2k\,b^R_{ij}\partial_j\langle u_i\rangle$, follows the
  printed convention, so the sign of the learned $b^R$ coefficients
  relative to $\nu_t$ depends on it. The text says the production
  correction raises the eddy viscosity in separated regions (§4.2). The
  dictionary set of Eq. 14 does not state $p,q\ge1$ for the mixed
  products, which the count of 25 requires *(compiler check, not in the
  sources)*; the noise standard deviation of Eq. A.9 (0.358) is ten times
  that of the same production model at every other $\lambda$
  (0.0358–0.0364); the text cites the SpaRTA models as Schmelzer et al.
  (2020b), the captions and App. B as (2020a).
- **Sandberg & Zhao (2022)** present no new closure; the GEP results
  above are those of the cited works, mostly the authors' group.
- **Symbol clashes in the source.** $\varepsilon$ is both the dissipation
  and the risk factor, $\alpha$ both the learning rate and the hill
  steepness, $\sigma$ both a standard deviation and the sigmoid.

# Citations

- [Tang et al. (2023)](/sources/tang-2023.md) — arXiv v1: §I (GEP, CFD-driven GEP cited), §II C 1, Algorithm 1, Apps. A–B, Eq. B1 (DSR), §II C 2, Eqs. 4–19 (closure, constants, split, squashing, rewards), §II D–E (coupling, workflow), §III A–E, Table I–II, Eqs. 20–22, Figs. 7–19, §IV, §V.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §III.A, §IV.A (symbolic and sparse regression, $\ell_1$ loss), §VII (interpretability does not imply generalization).
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §5.3 (gene-expression programming cited; uncertainty on the periodic hill when trained on a backward-facing step).
- [Wu et al. (2025)](/sources/wu-2025.md) — author manuscript: §2.2, Eqs. 16–17, 19–20, Tables 2–4 (PySR set-up, features, rebalancing, learned models); §3.2 (interpretation, cost); §4.2.
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — arXiv v2: §2–2.1, Eqs. 7–10, Table 1 (SBL-SpaRTA experts); §3; §4.2.1, Table 3.
- [Jakhar et al. (2026)](/sources/jakhar-2026.md) — arXiv v3: pp. 1–5, Eqs. 3–4, Figs. 1–4 (library, RVM, criterion, NGM closures, a priori table, a posteriori results, cases); App. B, Eq. 5; App. C (solver); App. D (eddy-viscosity baselines).
- [Li et al. (2021)](/sources/li-2021.md) — §I (earlier GEP-LES work), §II A–B, Eqs. 9–16, 22, Table I (representation, algorithm, fitness, hyperparameters, GEP(4)); §III A (data); Tables II–IV; §III C–F, Figs. 2–13; §IV.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §3.2.3 (triple decomposition, Lav et al.), §4.3, Eq. 2, Fig. 7, margin p. 267 (GEP definition, phase-locked EARSM, CFD-driven training); p. 259 (stress definition); Future issue 5.
- [Ruggeri et al. (2022)](/sources/ruggeri-2022.md) — §III (CFD-driven GEP of Zhao et al. cited, in passing).
- [Pacciani et al. (2025)](/sources/pacciani-2025.md) — §1, §3.2 (GEP corrections of the earlier model, cited), §4.1, Eq. 10 (length scale from trained expressions), §4.5, Eqs. 23–27 (separation switch as a training candidate).
- [Cherroud et al. (2022)](/sources/cherroud-2022.md) — §1, §2.1–2.2, Eqs. 2, 5–15 (corrections, frozen targets, dictionary); §3, Eqs. 16–32 (sparse Bayesian learning, cross-validation); §4.1–4.3, Table 2, Figs. 1–8; §5; Apps. A–C, Eqs. A.1, A.9, A.13–A.15.
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §3.1–3.4, Eqs. 2–4, 8 (basis, frozen time scale, SpaRTA, CFD-driven training); §4.1–4.5 (GEP stress, heat-flux, unsteady and multi-expression closures of cited works).
- [He et al. (2022)](/sources/he-2022-b.md) — §1 (GEP and sparse regression as explainable alternatives, in passing).
