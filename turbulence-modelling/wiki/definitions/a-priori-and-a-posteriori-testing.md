---
type: Definition
title: "A priori and a posteriori testing"
description: "A priori testing evaluates or trains a closure on filtered or averaged reference data outside the solver; a posteriori testing runs it inside the solver. The sources show that a priori agreement neither guarantees nor is required for a posteriori accuracy, and name the mechanisms."
status: established
aliases: [a priori test, a posteriori test, offline and online evaluation, a-priori training, a-posteriori training]
tags: [data-driven, a-priori-a-posteriori, sgs-model, les, rans]
timestamp: 2026-10-28T02:16:00Z
---

# A priori and a posteriori testing

An **a priori** test evaluates a closure model, or trains it, on reference
fields that are given in advance: DNS (or experimental) data are filtered
($\bar\phi$) or averaged ($\langle\phi\rangle$), the exact unclosed term
(the subgrid stress $\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$, the
Reynolds stress $R_{ij}$, a wall stress $\tau_w$) is computed from them, and
the model, fed with the same reference inputs, is compared with it. An
**a posteriori** test runs the model inside the LES, RANS or wall-modelled
solver and compares the solver's output with reference statistics. The two
differ because, in the solver, the model's inputs are the model's own
solution, errors accumulate and compensate in time, and the discretization
adds its own error to the closure. Every source of this bundle that runs
both tests reports cases in which the two verdicts disagree.

## Usage across the sources

The definition above is shared by Agrawal et al. (2022), Vela-Martín
(2022), Vicente Cruz & Lamballais (2023), Vadrot et al. (2023b), Griffin et
al. (2023) and Domingo & Vervisch (2023). [Bae & Koumoutsakos (2022)](/sources/bae-2022.md)
(preprint, p. 3) state it in the same terms: a priori testing measures how
well a supervised model predicts target values of a reference database
(typically DNS), and a posteriori testing integrates the equations in time
with the trained closure and compares the statistics with reference data.
[Prakash et al. (2022)](/sources/prakash-2022.md), [Abe (2021)](/sources/abe-2021.md)
and [Pereira et al. (2021)](/sources/pereira-2021.md) ("a priori
exercises" on filtered DNS) use the same pair. [Yan et al. (2022)](/sources/yan-2022.md)
call the out-of-solver evaluation of their network "offline prediction"
and its use embedded in the RANS solver the online test.
[Shan et al. (2023)](/sources/shan-2023.md) train their eddy-viscosity
network a priori on RANS fields, use the a priori $R^2$ and mean squared
error only to select hyperparameters, and choose the mix of training
data by the a posteriori lift-curve error of the coupled model (§III.D–E,
Figs. 12–13; see
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)).
[Hausmann et al. (2022)](/sources/hausmann-2022.md) assess their
[subgrid velocity enrichment](/methods/subgrid-velocity-enrichment.md)
only inside running LES, by the statistics of the generated field against
DNS.
[Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) (filtered-DNS
comparison against LES runs), [Helm & Martín (2022)](/sources/helm-2022.md),
[Kim et al. (2022)](/sources/kim-2022.md) and
[McConkey et al. (2022)](/sources/mcconkey-2022.md) use the pair in the
same sense. For McConkey et al. (§IV), a priori compares the network
outputs with the DNS labels before injection; a posteriori evaluates the
RANS solution after it has converged around the injected fields. The
combined anisotropy is available only a posteriori, because its linear part
evolves with the solution. [Kang et al. (2023)](/sources/kang-2023.md)
(filtered-DNS correlations and PDFs against actual LES),
[Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) (budgets of
filtered DNS against a dynamic-Smagorinsky LES, App. C) and
[Sirignano & MacArt (2023)](/sources/sirignano-2023.md) (§5: an offline
supervised fit to the filtered-DNS stress against the closure run in the
LES) use the pair in the same sense. Sirignano & MacArt add that
reinforcement learning "is not a priori learning under our taxonomy"
(§1). [Tang et al. (2023)](/sources/tang-2023.md) (§III C) check the
predicted anisotropy against DNS "a prior[i]", without re-solving, and
then inject the closure to obtain the a posteriori velocity.
[Kurz et al. (2023)](/sources/kurz-2023.md) use "a priori" for filtering
DNS onto the LES basis (Fig. 3) and "a posteriori" for the LES runs (§4).
[Kim et al. (2024)](/sources/kim-2024.md) (offline evaluation on box-filtered
DNS of a cylinder wake against actual LES, §4.1–4.2),
[Wang et al. (2023c)](/sources/wang-2023-c.md) (§V, filtered-DNS tests
against LES) and [Domaradzki (2024)](/sources/domaradzki-2024.md) (§1, on
the similarity models) use the pair in the same sense;
[Pacciani et al. (2025)](/sources/pacciani-2025.md) call the validation of
their RANS transition model in the solver "a posteriori".
[van Gastelen et al. (2024)](/sources/vangastelen-2024.md) do not use the
words for their own experiments, which are all run in the coarse solver,
but recall a priori and a posteriori results of other closures (§1).
Six further sources use the pair in the same sense.
[Maejima & Kawai (2025)](/sources/maejima-2025.md) (§5–6) test their
[super-resolution SGS model](/methods/super-resolution-sgs-model.md) a
priori on precomputed coarse-LES snapshots, the input the model meets in
use, rather than on filtered DNS, and then run it in the LES.
[Oulghelou et al. (2025)](/sources/oulghelou-2025.md) train their RANS
experts on frozen-RANS targets extracted from high-fidelity data and
evaluate the blended model in the solver (§2–4; see
[model aggregation](/methods/turbulence-model-aggregation.md)).
[Wu et al. (2025)](/sources/wu-2025.md) check the symbolic correction
against the inverted field without CFD iterations (Fig. 14) and run every
other test with the model coupled to the solver (§3.3, §4).
[Li et al. (2024)](/sources/li-2024.md) and
[Zhao et al. (2025)](/sources/zhao-2025.md) test their
[neural-operator surrogates](/methods/neural-operator-les-surrogate.md)
only a posteriori, by autoregressive rollouts from initial fields absent
from training (Li et al. §V: 10 fields; Zhao et al. §3: 5 fields).
[Mukha et al. (2025)](/sources/mukha-2025.md) (§III.B.3) compute an "a
priori" wall stress by feeding the wall model with velocity recorded in
the running WMLES, then compare with a posteriori runs.
Five further sources use the pair in the same sense.
[Wu & Lele (2026)](/sources/wu-2026.md) (arXiv v2, §4–6) evaluate their
[neural-network SGS models](/methods/neural-network-sgs-model.md) a priori
on a box-filtered hold-out set and a posteriori in two LES solvers.
[Jakhar et al. (2026)](/sources/jakhar-2026.md) (arXiv v3, pp. 1–4) use
the pair for tests on filtered DNS and in the running LES, and build
the a priori selection criterion of their
[symbolic-regression closure](/methods/symbolic-regression-closure.md)
so that it anticipates the a posteriori behaviour.
[Caban et al. (2026)](/sources/caban-2026.md) measure the subgrid-stress
error of approximate deconvolution a priori on filtered DNS of isotropic
turbulence (§4.2) and run the same models a posteriori in LES of the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) (§5).
[Rickard & Kasbaoui (2026)](/sources/rickard-2026.md) volume-filter
channel DNS a priori to calibrate a wall-slip model of
[immersed-boundary](/methods/immersed-boundary-method.md) WMLES and defer
the a posteriori tests to future work (§3, §7).
[Ranjbar et al. (2026)](/sources/ranjbar-2026.md) (arXiv v1, §III) test
their [explicit modal filter](/methods/explicit-modal-filtering.md) only
a posteriori, against an unmodelled run on the same coarse mesh ("coarse
DNS"); their joint PDFs of filter inputs and modal energy levels are
computed on those coarse runs (§III.B, Figs. 8–10), not on filtered DNS.
Two further sources use the pair in the same sense.
[Valencia et al. (2026)](/sources/valencia-2026.md) run an a priori study
only: deconvolution, dynamic Smagorinsky and dynamic mixed models are
evaluated on filtered and downsampled DNS of compressible isotropic
turbulence, and the a posteriori evaluation is deferred (§I, §VI).
[Nuca et al. (2025)](/sources/nuca-2025.md) (§VI) test explicit
[equilibrium wall models](/methods/equilibrium-wall-model.md) a priori
on a stored LES velocity signal of a channel and then in the running
WMLES of an airfoil, without naming the second test "a posteriori".
[Li et al. (2021)](/sources/li-2021.md) (§III B–C) test their
[gene-expression-programming](/methods/symbolic-regression-closure.md)
subgrid model a priori by its correlation with the filtered-DNS stress
and a posteriori in $128^3$ LES against filtered DNS.
[Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) (§4.3) print
the definitions for RANS: an a posteriori test is a full CFD run with the
new model, "accounting for its interplay with the RANS transport
equations or, in the case of multiple closures, between the different
models"; an a priori test checks whether the
trained model approximates training or other test data, for instance
whether a Reynolds-stress closure fed with reference velocity gradients
reproduces the reference Reynolds stress.
[Zangeneh (2021)](/sources/zangeneh-2021.md) (§III) reports only
"posteriori" tests of a random-forest wall-stress correction run in the
solver (see
[machine-learning wall models](/methods/machine-learning-wall-model.md)).
[Ruggeri et al. (2022)](/sources/ruggeri-2022.md) use the words only for
cited work (§III), not for their own tests: their neural Riemann solvers are first scored on held-out exact
solutions and then run as the interface flux of a finite-volume code
(§V–VI).
Five further sources use the pair in the same sense.
[Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) (§3.1, Fig. 9)
place it in a three-step machine-learning workflow (pre-processing,
training, testing): a priori the trained model approximates training or
test data; a posteriori it is implemented in the solver, which they also
call "forward-propagation". Their review's thesis is that a priori
improvements are common while a posteriori gains require model
consistency (§5; see
[model-consistent training](/methods/model-consistent-training.md)).
[He et al. (2022)](/sources/he-2022-b.md) (§2.2) call the two phases
"offline" (training and testing on frozen high-fidelity mean fields) and
"online" (the model called at every CFD iteration), and report the offline
phase only.
[Qi et al. (2022)](/sources/qi-2022-b.md) (§3–5) run both: correlations
of modelled and exact terms on box-filtered DNS, then LES.
[Tonicello et al. (2022)](/sources/tonicello-2022.md) (§4–5) evaluate
"a priori" the resolved kinetic-energy budget of their DNS, once with
Favre time–span averaging (the RANS sense) and once with a differential
filter of width $\Delta=2h$, $4h$, $8h$ (the LES sense); there is no LES.
[Cherroud et al. (2022)](/sources/cherroud-2022.md) (§3–4) fit their
sparse Bayesian closures to frozen-RANS targets out of the solver and
select the sparsity hyperparameter a posteriori, by running the MAP models
in OpenFOAM (below).
[Xu et al. (2023)](/sources/xu-2023.md) (§2.2, §3, §4) test their
compressible [neural-network SGS model](/methods/neural-network-sgs-model.md)
a priori on DNS of an isothermal-wall channel filtered by a top-hat
filter in the streamwise and spanwise directions only, and a posteriori in
LES of four channels and a supersonic boundary layer against DNS filtered
with the same filter-to-DNS-spacing ratios (below).
[Diez Sanhueza et al. (2023)](/sources/sanhueza-2023.md) (§3.2–3.3, §5)
train a network on field-inversion corrections of a $k$-$\varepsilon$
model and test it only a posteriori: the predicted correction is inserted
as a source term in the RANS solver and the mean velocity is compared with
DNS on held-out channels of a K-fold split (see
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)).
The words carry nine further meanings that must be kept apart:

- **Training rather than testing.** Duraisamy (2021, §IV) and Agdestein &
  Sanderse (2025, §4.3) speak of *a priori training* (the loss compares the
  model with reference data outside the solver) and *a posteriori training*
  (the loss is evaluated on solver output); the latter is
  [model-consistent training](/methods/model-consistent-training.md).
  Agdestein & Sanderse note the double use themselves: "a-priori" names
  training in their §4.3 and pre-LES analysis in their §5.1. Two further
  sources name the same split without the Latin words.
  [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) (§1, §2.2,
  Eqs. 11–12, after their ref. [64]) call fitting the discrete Reynolds stress
  "model regression" and fitting the solver's velocity and pressure
  "trajectory regression", which needs a differentiable solver. van
  Gastelen et al. (2024, §3.4, Eqs. 51–52) call a loss on the closure's
  right-hand side "derivative fitting" and a loss on unrolled coarse-solver
  trajectories "trajectory fitting".
- **"On-line" for a posteriori.** Duraisamy (2021, §IV.A) calls in-solver
  use "on-line" prediction and out-of-solver use "offline".
- **Not used in the LES sense.** Duraisamy et al. (2019, §5.3) write
  "a posteriori corrections" for corrections applied to an existing RANS
  model; the review does not use the pair for testing, though its argument
  on training and prediction environments (§5.4, §6) is the same one.
  Zhao et al. (2025, §4.1) call the training-stage behaviour of their
  coefficient loss an "a priori test", although no model is evaluated on
  frozen reference inputs there.
- **Metrics inside or outside the cost function.**
  [Fanizza et al. (2025)](/sources/fanizza-2025.md) (§3.5) call
  "iterative" the terms of the field-inversion cost and "a posteriori" the
  errors of quantities that do not enter it (velocity, wall pressure, skin
  friction, distance of the eddy viscosity from the baseline); both are
  computed on the converged data-assimilated RANS solution.
- **Error estimation in numerical analysis.** In
  [mesh adaptation](/methods/mesh-adaptation.md) the pair names the kind of
  discretization-error estimate, not a closure test.
  [Alauzet et al. (2022)](/sources/alauzet-2022.md) (§6.2) drive adaptation
  with an "a priori" goal-oriented estimate (an adjoint-weighted bound on
  interpolation errors); [Basile et al. (2023)](/sources/basile-2023.md)
  (§3.1) with an "a posteriori error estimator" computed from the
  solution's modal content and inter-element jumps.
- **DNS diagnostics that inspire a model.**
  [Chen et al. (2024)](/sources/chen-2024.md) call their §3 "a priori":
  DNS profiles of the eddy viscosity, defect velocity and turbulent
  Prandtl number are examined to choose the modifications of the
  [Baldwin–Lomax model](/methods/baldwin-lomax-model.md). Their §4 is "a
  posteriori": boundary-layer solutions with the modified model against
  twelve compressible DNS. No model is evaluated on frozen DNS inputs in
  §3.
- **Chemistry tabulation, not turbulence closure.**
  [Steinhausen et al. (2023)](/sources/steinhausen-2023.md) (§5, Fig. 7)
  and [Böttler et al. (2023)](/sources/bottler-2023.md) (§1, §3) apply the
  pair to [flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md).
  A priori, the manifold's control variables are extracted from the
  detailed-chemistry reference and the tabulated state is compared with the
  reference state; a posteriori, the control variables are transported in
  the coupled simulation. Steinhausen et al. state that the a priori test
  isolates the tabulation error from the errors of the transport equations
  of the control variables (§5).
  [Berger et al. (2022)](/sources/berger-2022.md) (§3.4.1–3.4.3, Eqs.
  22–24, Figs. 16, 22) choose manifold coordinates on DNS of turbulent
  lean hydrogen flames by the irreducible error of an optimal estimator,
  an out-of-solver assessment of candidate model inputs without the words
  a priori; the progress-variable source term is well parametrized by
  progress variable and mixture fraction, not by progress variable alone.
  They state that the measure sees only the correlation of fluctuations
  and is blind to a shift of the mean (§3.4.3).
  [Kumar et al. (2023)](/sources/kumar-2023.md) (§2.1–2.2, §3, §4)
  use the pair for reduced thermochemistry in DNS, not for a turbulence
  closure: the training data of principal-component transport are
  "generated a priori" (a two-dimensional species DNS), the choice of
  representative species is subject to "a priori validations" on those
  training data, and the coupled principal-component simulations are
  "a posteriori surrogate PC DNS", validated against a three-dimensional
  species DNS (§3.6).
- **Resolution adequacy of a hybrid model.** [Mays et al. (2023)](/sources/mays-2023.md)
  (§3.2.2, Fig. 13) call the theoretical modelled-to-total energy ratio
  $r_K$ of their scale-resolving hybrid model (page-local), computed from
  a RANS initialisation, "a simple a priori measure" of the resolution a
  grid and time step can attain, and the realised modelled-to-total ratio
  of the running simulation the a posteriori measure that highlights
  under-resolved regions (a patch with about 40% modelled energy at
  $Re_D=7.2\times10^5$); no closure is tested against reference data in
  either sense (see [hybrid RANS/LES](/definitions/hybrid-rans-les.md)).
- **Filtering before or after solving.** [Svärd (2022)](/sources/svard-2022.md)
  (§1, §6) uses "a priori" for a filter applied to the equations and "a
  posteriori filtering" for local averages of a computed weak entropy
  solution; neither sense is a model test.

For wall models, a priori means that the matching data at $h_{\mathrm{wm}}$
are taken from DNS and the model is run offline; a posteriori means the
model is coupled to the WMLES (Griffin et al. 2023, §§3–4; Vadrot et al.
2023b, §IV B). Nuca et al. (2025, §VI) take the a priori input not from
DNS but from a wall-resolved LES of a channel at $Re_\tau\approx1000$,
the velocity averaged over a cube of side $\delta/30$ centred at
$h_{\mathrm{wm}}=0.05\delta$ (a dataset designed for such tests by
Rezaeiravesh et al., as they cite it).

## Typical a priori metrics

- **Component correlations.** Agrawal et al. (2022, §V, Eq. 14) average,
  over the six independent components, the correlation coefficient between
  model and exact SGS stresses, and define a dissipation correlation by
  contracting both with $\bar S_{ij}$. They state that such correlations do
  not measure alignment between the model and exact tensors. The filtered
  DNS uses a discretely commutative filter with three vanishing moments of
  width three grid spacings (channel at $Re_\tau=395$ and 2000); widths of
  two to four spacings change the trends little ("not shown").
- **Plane-wise correlation and relative error.** Xu et al. (2023, §2.2,
  Eqs. 2.33–2.34) compute, in each wall-parallel plane of a channel, the
  correlation coefficient $C$ between the exact and modelled SGS term
  (each with its plane mean removed) and the relative error
  $E_r$, the root-mean-square difference over the root-mean-square exact
  value (page-local symbols), for every component of the deviatoric stress, its
  trace and the SGS heat flux, with 95% confidence intervals of $C$ from
  the Fisher transformation. They add the plane-averaged SGS fluxes of
  kinetic energy and temperature variance (§3.2, Fig. 12).
- **Correlation and energy-flux error.** Prakash et al. (2022, §III.A,
  Eq. 19) pair a mean correlation coefficient (C.C.) between model and
  exact SGS stress components with a relative error of the mean SGS energy
  flux $\Pi$ (R.E.F.), on box-filtered DNS of forced isotropic turbulence
  at $Re_\lambda=418$ with isotropic filters ($\Delta\approx6.5\eta$ to
  $68\eta$) and anisotropic "book" and "pencil" filters with aspect ratios
  up to about 19.5 (Figs. 1–3). The two numbers separate structural
  accuracy (C.C.) from dissipation (R.E.F.).
- **Equivalent eddy viscosity.** Abe (2021, §IV C, Eq. 17) projects each
  stress, exact or modelled, onto the resolved strain,
  $\nu_{\mathrm{eq}}=-\tau^d_{ij}\bar S_{ij}/(2\bar S_{kl}\bar S_{kl})$
  (page-local name), so that an eddy-viscosity model with this
  $\nu_{\mathrm{eq}}$ reproduces the local energy transfer of the stress,
  forward and backward. With the registry definitions,
  $\nu_{\mathrm{eq}}=\Pi/\lvert\bar S\rvert^2$ in incompressible flow
  *(compiler check, not in the sources)*. The metric compares dissipation,
  not stress components.
- **Spectral eddy viscosity.** Vicente Cruz & Lamballais (2023, §2.2,
  Eq. 23) estimate Kraichnan's spectral eddy viscosity $\nu_t(k\mid k_c)$ a
  priori from filtered DNS of the
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) and a posteriori
  from the LES energy budget (Eq. 29); see
  [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md).
- **Commutator-error loss.** Agdestein & Sanderse (2025, Eq. 24) take the
  batch-averaged relative error
  $\|m(\bar u)-c(u)\|^2/\|c(u)\|^2$ between the closure $m$ and the exact
  discrete closure term $c$ (see
  [divergence-consistent LES](/methods/divergence-consistent-les.md)).
- **Correlations, PDFs and backscatter fraction.** Seyedi & Zayernouri
  (2022, §III.2, Figs. 4–7) use ensemble-averaged correlation coefficients
  of the six SGS stress components, PDFs of $\Pi$ and of the SGS force
  components, and the share of grid points with $\Pi<0$, on box-filtered
  DNS of forced isotropic turbulence at $Re_\lambda=240$. They also fit the
  fractional order of their
  [fractional SGS model](/methods/fractional-sgs-model.md) a priori, by
  maximizing the correlation on ten snapshots each at $Re_\lambda=170$, 240
  and 355 (§III.1, Fig. 3).
- **Alignment with the resolved strain.** Kim et al. (2022, §III E, Eqs.
  27–28, Table IV) compare model and filtered-DNS stresses through the
  angle between $-\tau^d_{ij}$ and $\bar S_{ij}$, the angles between their
  eigenvectors, and pointwise correlations of $\bar S_{xy}$ with
  $-\tau_{xy}$ and of $\lvert\bar S\rvert^3$ with the SGS dissipation (see
  [reinforcement-learning closures](/methods/reinforcement-learning-closure.md)).
- **Label error of a RANS correction.** McConkey et al. (2022, §IV A, Figs.
  11–14) report the mean squared error of the predicted non-negative
  optimal eddy viscosity ($1.89\times10^{-7}\ \mathrm{m^4\,s^{-2}}$) and of
  the three components of the non-linear anisotropy ($9.40\times10^{-13}$
  to $2.31\times10^{-12}\ \mathrm{m^4\,s^{-4}}$) on a held-out periodic
  hill. The eddy viscosity is the harder target.
- **Component correlation with the resolved strain.** Kang et al. (2023,
  Eq. 3.1, Tables 3–4, 6) use the component-wise correlation coefficient
  $\langle\alpha_{ij}\beta_{ij}\rangle/(\langle\alpha_{ij}^2\rangle^{1/2}\langle\beta_{ij}^2\rangle^{1/2})$
  (page-local $\alpha_{ij}$, $\beta_{ij}$ for the two tensors), both
  between model and filtered-DNS stresses and between $\bar S_{12}$ and
  $\tau_{12}$. In forced isotropic turbulence at $Re_\lambda=106$ the
  filtered-DNS correlation of $\bar S_{12}$ with $\tau_{12}$ is $-0.2806$;
  a network fed with $\bar S_{ij}$ alone gives $-0.8217$, i.e. a stress
  nearly aligned with the strain (§3.1). See
  [neural-network SGS models](/methods/neural-network-sgs-model.md).
- **Budgets of the resolved Reynolds stress.** Inagaki & Kobayashi (2023,
  §II–IV) split the subgrid stress of filtered channel DNS at
  $Re_\tau=400$ into an energy-matching eddy-viscosity part and an
  anisotropic remainder that transfers no energy, and evaluate a priori
  each part's contribution to every component of the budget of
  $\langle\bar u_i'\bar u_j'\rangle$, also wavenumber by wavenumber (see
  [scale-similarity model](/methods/scale-similarity-model.md)). Their a
  priori test of three anisotropic-stress models compares these budget
  terms, not stress correlations (§IV B, Fig. 13).
- **Wall-stress ratio.** Vadrot et al. (2023b, §IV B, Fig. 12) feed a
  law-of-the-wall profile to machine-learning wall models and plot the
  ratio of the predicted $\tau_w$ to the law-of-the-wall value.
- **Mean stress, dissipation and backscatter profiles.** Kim et al. (2024,
  §4.1, Fig. 6) compare span- and time-averaged profiles of the SGS shear
  stress, of $\Pi=-\tau_{ij}\bar S_{ij}$ and of its negative part
  $\tfrac12\langle\Pi-|\Pi|\rangle$ (translated from their
  $\epsilon_{SGS}$) between six networks, the dynamic Smagorinsky model
  and filtered DNS at three stations of a cylinder wake at $Re_D=3900$ ($D$ the
  diameter).
- **Robustness to input noise.** Kim et al. (2024, §4.1, Eq. 4.1, Fig. 7)
  add Gaussian noise with the standard deviation of each training input to
  the strain-rate inputs and compare the change in the predicted stresses
  across architectures; the most robust network (T-SR-FU) is one of the
  two fusion networks that stay accurate on untrained grids (Table 3).
- **Correlation of energy transfers.** Domaradzki (2024, §3.1, Fig. 6)
  correlates the local SGS energy transfer of the
  [autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md)
  with that of a similarity stress: 0.81 in a plane and "in excess of 0.8"
  in 3-D, against "the value around 0.4" the paper quotes for the standard
  Smagorinsky model.
- **Tabulation error.** Böttler et al. (2023, §3.1, Fig. 3) report a priori
  relative deviations of temperature and OH mass fraction between two
  flamelet manifolds and detailed chemistry in a laminar hydrogen flame:
  up to 5% in $T$ and 40% in $Y_{\mathrm{OH}}$ for the enthalpy-based
  manifold, smaller and more localized for the curvature-based one.
- **Correlation of the energy transfer, split by sign.** Jakhar et al.
  (2026, App. B, Eq. 5, Figs. 1–2) use the domain-averaged correlation
  coefficient (CC) between model and filtered-DNS stresses, and also the
  CC of the inter-scale energy transfer $P_\tau$ (page-local, the paper's
  symbol; positive for forward transfer, which the paper calls diffusion,
  negative for backscatter), of its positive part and of its negative part,
  plus the ratios of the domain-mean energy and enstrophy transfers to
  their filtered-DNS values. The definitions of $P_\tau$ and of the
  enstrophy transfer are in the Supplemental Material, which is not in
  the version read.
- **Stress and dissipation errors.** Wu & Lele (2026, §3.1, §4, Table 2)
  report the root-mean-square error of $\tau_{ij}$, the same error of the
  SGS dissipation $\Pi=-\tau_{ij}\bar S_{ij}$ (their DRMSE) and the
  correlation coefficient, as mean and standard deviation over the test
  set.
- **Spectral error of the subgrid stress under a mismatched filter.**
  Caban et al. (2026, §4.2, Eqs. 38–39, Fig. 8) deconvolve filtered DNS
  of isotropic turbulence ($Re_\lambda=100$, $384^3$, LES grid of 64
  points, Gaussian filter with $\Delta=2h$) with a filter other than the
  true one and integrate the resulting stress error over wavenumber; see
  [scale-similarity model](/methods/scale-similarity-model.md) for the
  approximate deconvolution model and
  [discretization-consistent closure](/definitions/discretization-consistent-closure.md)
  for the filters.

- **Correlation, relative error and regression slope against the total
  unresolved stress.** Valencia et al. (2026, §V A, Eqs. 53–54) score
  the components $\tau_{xx}$ and $\tau_{xy}$ by the domain-averaged
  correlation coefficient $C$ and the relative error
  $$E_{\mathrm{rel}}=\frac{\langle(\tau^{\mathrm{ref}}-\tau^{\mathrm{mod}})^2\rangle^{1/2}}{\langle(\tau^{\mathrm{ref}})^2\rangle^{1/2}}$$
  (page-local superscripts for the reference and model stresses; the
  brackets are domain averages here), plus the slope of the scatter-plot
  regression, PDFs and power spectra of the normalized stresses and
  mid-plane fields (Figs. 5–23). Their reference is the *total* unresolved
  stress of explicitly filtered LES (next section), not only the part a
  model can recover.
- **The same pair, on every unclosed term.** Three papers of one group
  use the same correlation coefficient $C$ and relative error
  $E_{\mathrm{rel}}$ against filtered DNS, Gaussian filter of 16 DNS
  spacings, LES spacing $\Delta/2$:
  [Wang et al. (2022)](/sources/wang-2022-j.md) (Eqs. 9–10, Table II) on
  $\tau_{11}$, $\tau_{12}$ in forced isotropic turbulence at
  $Re_\lambda\approx250$; [Zhang et al. (2022b)](/sources/zhang-2022-f.md)
  (Eqs. 35–36, Figs. 1–3) on $\tau_{11}$, $\tau_{12}$ and the subgrid heat
  flux of density-unweighted LES of compressible isotropic turbulence
  ($M_t=0.40$, 0.79); [Zhang et al. (2022d)](/sources/zhang-2022-h.md)
  (Eqs. 37–38, Figs. 1–2) on the stress, the subgrid pressure, pressure
  work and internal-energy flux of a dense gas. The two compressible
  papers add the rms of the divergence of each unclosed term, which ranks
  the terms before any model is chosen: in the density-unweighted
  equations the stress, mass-flux, heat-flux and turbulent-diffusion terms
  dominate and the density–temperature term is smallest (Zhang et al.
  2022b, Table II); in the dense gas the subgrid pressure and
  internal-energy flux are an order of magnitude below the other terms of
  their equations (Zhang et al. 2022d, Tables IV–V).
- **Correlations of every unclosed term of the compressible equations.**
  Qi et al. (2022, §4, Figs. 2–4) score their quasi-dynamic subgrid
  kinetic-energy model on DNS of a compressible channel at Mach 1.5
  ($900\times201\times300$ points), box-filtered in $x$ and $z$ at
  $6\Delta_z$ ($\Delta_z$ page-local, the DNS spanwise spacing), by the
  wall-normal profile of the correlation coefficient of the subgrid
  kinetic-energy flux and of the wall-normal subgrid heat flux ("almost
  higher than 0.95", against "much lower" for dynamic Smagorinsky and a
  dynamic $k_{\mathrm{sgs}}$-equation model), and also of the pressure
  and dissipation terms of the energy equation. A second a priori check
  compares the model coefficient inferred from each expanded term with the
  one the model actually uses (Figs. 4, 15); see
  [dynamic procedure](/methods/dynamic-procedure.md).
- **Correlation of the subgrid energy transfer with dilatation.**
  Tonicello et al. (2022, §4.2, §5, Tables 4–6) correlate the
  resolved-dilatation term of the kinetic-energy budget with the subgrid
  (or Reynolds-stress) dissipation, over the whole field and per quadrant
  of compression or expansion and forward or inverse transfer: 0.2775 for
  the Favre average, 0.1936 and 0.2682 for the filter widths $4h$ and $8h$
  (Table 4). Removing the spherical part of the stress drops the
  correlation to 0.1081, 0.0370 and 0.0889 (Table 6); see
  [energy backscatter](/definitions/energy-backscatter.md) and
  [pressure dilatation](/definitions/pressure-dilatation.md).

**A posteriori metric.** Wu & Lele (2026, §5, Eq. 5.1) sum the absolute
difference of the logarithms of the filtered-DNS and LES energy spectra
over the resolved wavenumbers (their "sum spectral error", SSE,
page-local). They call it "artificially sensitive to deviations in the
higher-wavenumber, dissipative range": it can rate a dissipative spectrum
worse than a spectrum with high-wavenumber pile-up, so visual inspection
of the spectra stays necessary (§5).

## A priori tests on the DNS grid or on the LES grid

Valencia et al. (2026, §I) state that classical a priori tests, run on the
DNS grid, "tend to overestimate model accuracy because the filtered and
resolved fields share the same grid resolution". Their "stringent"
protocol (§V A) mimics an LES grid in three steps: a top-hat filter of
width $h$ applied to $512^3$ DNS of decaying compressible isotropic
turbulence (initial turbulent Mach number 0.6), meant to emulate the
implicit filter of a centred finite-volume scheme; downsampling to a
coarse grid of spacing $h$; and an explicit Gaussian filter of width
$\Delta=\mathrm{FGR}\cdot h$ with filter-to-grid ratio
$\mathrm{FGR}=\Delta/h=1,2,4$ ($h$ the LES grid spacing, FGR page-local). The
reference stress is then the total unresolved stress of explicitly
filtered LES, $\tau^{\mathrm{tot}}_{ij}=\tau^{\mathrm{gr}}_{ij}+\tau^{\mathrm{sf}}_{ij}$
(page-local), the sum of a grid-truncation part (lost by the
projection on the coarse grid, which no deconvolution can recover) and a
sub-filter part (removed by the explicit filter); see
[large-eddy simulation](/definitions/large-eddy-simulation.md) and the
[scale-similarity model](/methods/scale-similarity-model.md) for the
decomposition and the deconvolution models (§II C, Eqs. 23–29). With the
explicit filter width fixed at 16 DNS spacings, the three retained cases
($128^3$ with FGR 4, $64^3$ with FGR 2, $32^3$ with FGR 1) leave 15–20% of
the kinetic energy unresolved, of which about 92%, 72% and 3.5% is
sub-filter (§V B, Table IV): the FGR decides how much of the target a
deconvolution model can reach.

Results (Tables VI–VII, values $C_{xx}$, $C_{xy}$ / $E_{\mathrm{rel},xx}$,
$E_{\mathrm{rel},xy}$):

| Model | FGR 2 | FGR 4 |
|---|---|---|
| approximate deconvolution, order 5 | 0.9795, 0.9839 / 0.2469, 0.1946 | 0.9968, 0.9976 / 0.0909, 0.0755 |
| discrete direct deconvolution, order 4 | 0.9792, 0.9838 / 0.2445, 0.1931 | 0.9972, 0.9980 / 0.0897, 0.0712 |
| dynamic iterative approximate deconvolution | 0.9735, 0.9800 / 0.2649, 0.2153 | 0.9946, 0.9964 / 0.1023, 0.0892 |
| spectral direct deconvolution (upper bound) | 0.9809, 0.9849 / 0.2402, 0.1881 | 0.9989, 0.9992 / 0.0626, 0.0457 |
| [dynamic Smagorinsky](/methods/dynamic-procedure.md) | 0.2726, 0.1369 / 1.2955, 1.0203 | 0.2562, 0.1156 / 1.9644, 1.0459 |
| dynamic mixed | 0.9057, 0.9144 / 0.4923, 0.4543 | 0.9126, 0.9089 / 0.4386, 0.4483 |

At FGR 1 approximate deconvolution is unusable ($C<0.15$,
$E_{\mathrm{rel}}>0.98$; §V B 1). The authors read the weak FGR
sensitivity of the dynamic Smagorinsky and mixed models as a structural
limit of eddy-viscosity formulations and conclude that compensating the
filter is "a requirement fulfilled exclusively by deconvolution-based
approaches" (§V C, §VI). Whether the low a priori correlation of the
dynamic Smagorinsky model predicts its behaviour in an LES is not tested:
Valencia et al. run no LES (see the evidence below that the two verdicts
can disagree).

## Evidence that the two verdicts disagree

**A priori success is not sufficient.**

- Agrawal et al. (2022, §V) find that the Bardina
  [scale-similarity model](/methods/scale-similarity-model.md) has much
  better a priori tensor correlations than their
  [dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md),
  yet is under-dissipative a posteriori and needs added Smagorinsky
  dissipation.
- Vadrot et al. (2023b, §I) cite Zhou et al. (2021), who reported
  good a priori but poor a posteriori results for a neural-network wall
  model on periodic hills. In their own tests the re-trained version
  (ZYZY22) is accurate a priori at every $Re_\tau$ except 180 (§IV B,
  Fig. 12), yet a posteriori it gives a log law with $\kappa=0.32$ (§III A,
  Eq. 9); the authors trace the error to the LES side (§V) while also
  writing that "it is not clear to the authors why" (§IV B).
- Duraisamy (2021, §IV.B, Fig. 2) shows, from Sirignano, MacArt &
  Freund, that an a priori-trained SGS closure overpredicts the resolved
  kinetic energy in decaying
  [homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md),
  while the same closure trained a posteriori follows filtered DNS.
- Agdestein & Sanderse (2025, §5.2.2) find that an a priori-trained CNN
  closure is unstable in the divergence-inconsistent LES formulation and
  worse than no closure at all resolutions except $\bar n=32$.
- Abe (2021, §IV C, §V) finds that the Bardina-type and modified-Leonard
  [scale-similarity models](/methods/scale-similarity-model.md) agree well
  with the reference $\nu_{\mathrm{eq}}$ in the shear layer behind a
  [backward-facing step](/benchmarks/backward-facing-step.md), and states
  that a pure scale-similarity model nevertheless "often causes numerical
  instability" a posteriori; citing the author's earlier work, the paper
  states that the similarity estimate of $k_{\mathrm{sgs}}$ did not always work a
  posteriori on coarse grids.
- Pereira et al. (2021, §III, §IV.2) set the
  [PANS](/methods/partially-averaged-navier-stokes.md) resolution
  parameters of their strategy S3 ($f_\varepsilon=1$, mass-flux ratio
  about $f_k/2$, density-correlation ratio $f_k$) from a priori filtering
  of DNS of homogeneous variable-density turbulence at Atwood number 0.75.
  A posteriori, in the transitional
  [Rayleigh–Taylor mixing layer](/benchmarks/rayleigh-taylor-mixing.md), S3
  does not converge toward the reference as $f_k$ is reduced and produces
  a nonphysical overshoot of the unresolved density–specific-volume
  correlation at $t=2.5$, while the simpler S1 and S2, which use no a
  priori information, converge. The authors attribute the failure to the
  fully-developed-turbulence assumption behind the a priori data, which the
  early, laminar and transitional stages violate.
- Yan et al. (2022, §3.1.2, Table 1) train twelve networks (four sizes,
  three epoch counts) to reproduce a field-inversion correction of the
  [Spalart–Allmaras model](/methods/spalart-allmaras-model.md) on the S809
  airfoil. Lower training and validation loss does not give lower a
  posteriori error: the embedded model's lift error at $8^\circ$ ranges
  from $-2.0\%$ to $15.1\%$ with no monotone relation to the root-mean-square
  error of the correction field. They call this "a kind of overfitting"
  and choose the network by its a posteriori lift error (see
  [field inversion and machine learning](/methods/field-inversion-machine-learning.md)).
- [Ihme et al. (2022)](/sources/ihme-2022.md) (§4.1.4) summarize the
  learned closures of reacting-flow LES: supervised models "often
  outperform physics-based closure models in a priori studies; however,
  caution is warranted for extrapolating these findings to a posteriori
  applications", because models trained on filtered DNS "can be unstable
  due to the accumulation of small errors over a large number of
  timesteps when evaluated a posteriori". They add that most applications
  to date are a priori tests on idealized problems (§6), and give a
  physics-informed loss as one remedy (see
  [neural-network SGS models](/methods/neural-network-sgs-model.md) and
  [super-resolution SGS models](/methods/super-resolution-sgs-model.md)).
  The review cites the evidence; it runs no test.
- Sirignano & MacArt (2023, §5, Figs. 11–12) train the same gated network,
  with the same hyperparameters, two ways for LES of a square prism in
  confined cross-flow ($Re=1000$ on the prism height). Fitted by supervised
  learning to the filtered-DNS subgrid stress, it matches that stress
  "almost perfectly" a priori; run in the LES it is "substantially
  outperform[ed]" for every flow statistic by the network trained through
  the solver with adjoints, even on the training case (see
  [model-consistent training](/methods/model-consistent-training.md)).
- Kang et al. (2023, §3.3, Table 6) rank the a priori correlations of
  model and filtered-DNS stress in forced isotropic turbulence: the
  dynamic two-parameter mixed model with a Clark term 0.9104–0.9135, their
  mixed network 0.7040–0.7176, the one-parameter dynamic mixed model
  0.7057–0.7170, the dynamic two-parameter similarity model 0.5181–0.5353,
  dynamic Smagorinsky 0.2718–0.3006. A posteriori the network gives the
  most accurate spectra and decay of kinetic energy and SGS dissipation in
  decaying isotropic turbulence, and in forced turbulence a spectrum nearly
  identical to that of the best-correlated model (Figs. 19, 21–22). The
  authors conclude that a higher a priori correlation "does not guarantee"
  a better LES. The algebraic dynamic models also need averaging and
  clipping to run at all (§3.3; see
  [energy backscatter](/definitions/energy-backscatter.md)).
- Wang et al. (2023c, §III, Figs. 3–4) find in forced isotropic turbulence
  at $Re_\lambda\approx160$ that the pure [gradient model](/methods/gradient-model.md)
  gives the PDFs of the SGS stress closest to filtered DNS, but the worst
  energy spectrum and kinetic-energy evolution of the models tested
  (underdissipation). "Accurately reconstructing the SGS stress may not
  guarantee the adequate prediction of other important flow statistics."
  Their mixed model, whose functional coefficient is calibrated a
  posteriori, slightly degrades the stress PDFs and gives the best a
  posteriori statistics (see
  [ensemble Kalman calibration](/methods/ensemble-kalman-closure-calibration.md)).
- Kim et al. (2024, §4.1) state, citing earlier studies, that a better a
  priori prediction does not guarantee a better a posteriori result. A priori, their networks
  fed with the velocity-gradient tensor beat those fed with the strain
  rate (§4.1, Fig. 6); a posteriori at the training grid the grid-filtered
  and fusion networks give recirculation lengths $L_r/D$ of 1.51 (G-SR),
  1.56 (G-VG), 1.59 (T-SR-FU) and 1.56 (T-VG-FU) against 1.56 in DNS
  (Table 3; $L_r$ page-local, the mean recirculation length from the base
  point).
- Domaradzki (2024, §1), citing Bardina et al. and Liu et al., states that
  similarity models correlate highly with filtered-DNS stresses a priori
  and are insufficiently dissipative a posteriori; eddy-viscosity models do
  the reverse.
- van Gastelen et al. (2024, §1) recall networks with good a priori
  correlation that were unstable a posteriori (Beck et al.; Kurz & Beck;
  Park & Choi). In their own 1D tests a vanilla convolutional closure
  trained by derivative fitting alone was unstable and inaccurate,
  "especially in the KdV case", while their energy-conserving closure
  was already reasonable (§4.2; see
  [neural-network SGS models](/methods/neural-network-sgs-model.md)).
- Zhao et al. (2025, §3.1, Table 2, Figs. 6–7) find the lowest test loss
  in decaying isotropic turbulence for the data-driven Fourier neural
  operator (0.029 against 0.058–0.059 for the physics-informed LESnets),
  yet in rollout it deviates in rms velocity and vorticity by $t\approx2T_E$
  and fails on the kinetic energy at $t\approx T_E$ ($T_E$ the large-eddy
  turnover time, page-local), while LESnets stay close to filtered DNS over
  about $5T_E$. With 2000 training fields the
  test loss is already about 0.059, but the a posteriori rms velocity and
  spectra are too high until 3000 fields are used (§5.3, Fig. 25). See
  [neural-operator surrogates](/methods/neural-operator-les-surrogate.md).
- Mukha et al. (2025, §III.B.3, Table III, Figs. 4–5) find a priori that
  time-averaging the input of an algebraic wall model reduces the
  wall-stress error, most of the gain being reached at an averaging time
  of $0.01\,\delta/u_\tau$; with the mean velocity as input the error
  drops to 0.06%, 0.2% and $-1.07$% on three meshes. A posteriori, WMLES
  with averaging times of 5 to 500 time steps show "no systematic accuracy
  gain", because the velocity at the sampling point itself changes with
  the averaging, "violating" the a priori assumption. The authors
  conclude that for algebraic models the matching height matters more
  than the averaging, "at odds with" Yang et al. as they cite them (see
  [wall-modelled LES](/methods/wall-modelled-les.md)).
- Wu & Lele (2026, §4, Table 2) find the ten networks they test a priori
  indistinguishable: RMSE 0.750–0.772, DRMSE 0.661–0.693, correlation
  0.636–0.661, "within 5 percent of each other". A posteriori the same
  networks spread widely in their sum spectral error: 3.68 to 18.87 in a
  Fourier-spectral solver with two-thirds dealiasing and 5.59 to 35.33 in
  a sixth-order compact finite-difference solver without dealiasing, in
  forced isotropic turbulence at $Re_\lambda=433$ on $64^3$ (Tables 3–4;
  the sets of networks in the a priori and a posteriori tables are not
  identical). A network trained on box-filtered data only with
  higher-order velocity-gradient inputs is badly under-dissipative in both
  solvers (18.87 and 32.58), with a pile-up of high-wavenumber energy
  (§5.1.1, §5.2.1). Two-filter training removes most of the gap (4.0 and
  11.93) at no a priori cost (see
  [neural-network SGS models](/methods/neural-network-sgs-model.md)).
- Jakhar et al. (2026, pp. 1, 4) recall that the second-order
  [gradient model](/methods/gradient-model.md) reaches a priori pattern
  correlations "above 0.9" with filtered DNS, and find that in forced 2-D
  turbulence its LES is unstable "for any case and any LES resolution".
  As they state, the model produces no inter-scale energy transfer in 2-D
  (ratio of mean transfers 0, Fig. 2 table).
- Sandberg & Zhao (2022, §4.1) cite the junction-flow closure of
  Weatheritt & Sandberg (2019), whose cost included the divergence of
  the Reynolds stress, strongly reduced the a priori error yet improved
  the a posteriori velocity only marginally; gene-expression and
  tensor-basis models of a jet in crossflow, trained on an inline jet and
  tested a priori on a skewed one, both failed where the streamwise
  vorticity is strongest. The review adds that training on DNS Reynolds
  stresses cannot guarantee an accurate RANS mean flow (§3.1, citing Wu et
  al. 2019 and Brener et al. 2021).

**An a priori criterion chosen for its a posteriori consequence.** Jakhar
et al. (2026, pp. 2–4, Figs. 1–3) select a closure from a 930-term
library by an L-curve of an a priori score against the sparsity
threshold. Scored by the CC of $\tau_{ij}$ alone, the elbow returns the
unstable second-order gradient model. Scored by the minimum of the CCs of
$\tau_{ij}$, of $P_\tau$ and of its positive and negative parts, it returns
a five-term closure, the fourth-order truncation of the gradient
expansion. That closure keeps a CC of about 0.99 for $\tau_{ij}$, recovers
62% of the filtered-DNS mean energy transfer including backscatter, and
runs stably a posteriori when the LES resolves more than 80% of the DNS
enstrophy. The authors call it "the first closure to simultaneously excel
in both a priori and a posteriori tests" (p. 4); see
[symbolic-regression closures](/methods/symbolic-regression-closure.md).
The two verdicts agree here once the a priori score contains the energy
transfer; the stress correlation alone did not discriminate.

**An a priori fit selected a posteriori.** Cherroud et al. (2022, §3–4,
Eqs. 29–32, Table 2) regress the coefficients of
[sparse Bayesian closures](/methods/symbolic-regression-closure.md) out of
the solver, on frozen-RANS targets, for five values of the sparsity
parameter, and choose among them by running the maximum-a-posteriori
models in OpenFOAM and scoring the mean-square errors of velocity, $k$,
Reynolds shear stress and $C_f$ against the baseline. The a posteriori
score decides the model and depends on the quantities it contains: scored
on velocity alone, models with a non-zero anisotropy correction win for
two of the three training scenarios; scored on all four quantities, the
production-only model at the largest sparsity wins for all three (Table
2). Yan et al. (2022) chose their network by its a posteriori lift error
for a related reason (above).

**Deconvolution filters: one verdict agrees, one does not.** Caban et al.
(2026) test the approximate deconvolution model both ways. A priori
(§4.1–4.2, Eqs. 36–37, Figs. 6, 8) a deconvolution filter of lower order than the true filter
amplifies the deconvolved field, and with the second-order finite-difference
filter the stress error grows with the number of deconvolution terms,
while compact filters of second and fourth order give low-wavenumber
errors about two orders of magnitude below those of that filter and of
the Layton–Lewandowski model (no deconvolution). A posteriori, in LES of
the transitional Taylor–Green vortex at $Re=1600$ on $64^3$, deconvolution
with second- to fourth-order finite-difference filters on a sixth-order
compact LES filter and the explicit regularization filter (their N-DI-R
variant) is unstable, which the authors attribute to the
amplification of resolved scales by low-order deconvolution (§5.4.2,
Table 9): the two tests agree on the low-order filters. Yet the best
Layton–Lewandowski run (energy error $2.03\times10^{-2}$) beats the best
deconvolution run ($2.31\times10^{-2}$; §5.4, Tables 5, 9), against the
a priori ranking. The a priori test uses a Gaussian LES filter and the
LES runs compact or finite-difference ones, so the two rankings are not
on the same filter *(compiler check, not in the sources)*.

**A priori failure on the deployment input predicts a posteriori
failure.** Maejima & Kawai (2025) test a supervised super-resolution
network, trained on (filtered DNS, DNS) pairs, on its deployment input,
very coarse LES fields that differ from filtered DNS ("fDNS $\neq$ vLES").
A priori it keeps the coarse-LES mean velocity and over-predicts the
streamwise and shear Reynolds and SGS stresses (§5.3, Figs. 18–21); a
posteriori it is only slightly better than the conventional model and
still over-predicts the velocity (§6.1, Fig. 22). Their pipeline, which
first maps the coarse-LES field to filtered-DNS quality without paired
data, passes both tests (§5.3, §6.1). The a priori test here is run on
solver output (precomputed coarse-LES fields), not on filtered DNS; see
[super-resolution SGS models](/methods/super-resolution-sgs-model.md).

**A priori success is not necessary.** Duraisamy (2021, §IV.A) states
that successful a priori evaluation is "neither a necessary (e.g.
Smagorinsky model) nor a sufficient condition for successful predictive
models". Vela-Martín (2022, §8) gives a mechanism for the "not necessary"
half. The filtered equations depend on $\tau_{ij}$ only through its
divergence, so stresses that differ by a divergence-free tensor are
physically equivalent (§3). The paper's "standard" stress and its optimised
equivalent correlate only about 0.6 at filter scale $0.64L$, falling to
about 0.4 at $0.08L$ (§6.3). A low a priori correlation between a
model and $\tau_{ij}$ is therefore not by itself evidence of poor
modelling. The author offers this as a possible reason why
[eddy-viscosity models](/methods/smagorinsky-model.md) succeed despite poor
a priori correlation (see
[energy backscatter](/definitions/energy-backscatter.md)).

**A priori and a posteriori quantities can be unrelated.** Vicente Cruz &
Lamballais (2023, §6.3, Fig. 11) find that the a posteriori spectral eddy
viscosity of the Smagorinsky model at $C_s=0.1$ has "no common features"
with its a priori estimate: it is of the same order at low $k$ but
underestimated, weakly $k$-dependent, and vanishes near $k_c$ where the a
priori one rises. The drop scales on $k_c$, not on the filter wavenumber,
which they read as a signature of numerical error.

**Equal a priori dissipation, different a posteriori results.** Prakash et
al. (2022) compare two ways of removing the local backscatter of Clark's
[gradient model](/methods/gradient-model.md): standard clipping (set the
model stress to zero where $\tau_{ij}\bar S_{ij}>0$) and their optimal
clipping (the nearest backscatter-free tensor). A priori the two have
identical SGS dissipation, while optimal clipping keeps the correlation
coefficient of the unclipped model and standard clipping lowers it (§III.A,
Figs. 1–3). Where the structural model backscatters, both give
$\Pi=0$ pointwise, so the identity of the a priori dissipation is exact
*(compiler check, not in the sources)*. A posteriori, in forced isotropic
turbulence and the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
at $Re=1600$, the two are close; in wall-resolved
[channel flow](/benchmarks/turbulent-channel-flow.md) at $Re_\tau=590$
optimal clipping gives $C_f=0.0051$ and $0.0053$ on the coarse and medium
meshes against $0.0047$ and $0.0050$ for standard clipping and $0.0058$ in
DNS (§III.B.3, Table 4), with better mean velocity and Reynolds shear
stress. The authors "hypothesize" that structural accuracy, not
dissipation, explains the gain in the anisotropic wall-bounded flow (§IV),
following the argument they cite from Baggett et al. that HIT needs only
the right dissipation (§I–II).

**Low correlation, good a posteriori results.** Kim et al. (2022, §III E,
Table IV) evaluate models on one resolved channel-flow field at
$Re_\tau=180$. The correlation between $\bar S_{xy}$ and $-\tau_{xy}$ is
$-0.20$ at $y^+\approx15$ and 0.19 at $y^+\approx50$ in filtered DNS,
0.95 and 0.94 for the dynamic Smagorinsky model, and 0.34 and 0.58 for
their RL-trained model. The RL model, whose stress correlates less with the
strain than the dynamic model's, gives the better LES: it reproduces the
filtered-DNS mean velocity and Reynolds shear stress, which the dynamic
model overpredicts (§III C). The authors attribute the gain to the
non-alignment of $\tau^d_{ij}$ with $\bar S_{ij}$, "rather than the level
of eddy viscosity" (§III E). Like Prakash et al. (2022), they credit stress
structure, not dissipation. By contrast, Kim et al. cite supervised
networks fed with local velocity gradients (Park & Choi 2021) that reach a
correlation of only about 0.5 with the filtered-DNS stress, and the one
with the same inputs as the RL model did not predict the two target
profiles well (§III C, §III E).

**Wrong stresses, right mean flow (RANS).** In field inversion on mean
velocity, Cato et al. (2023, §V C, Figs. 16–19) reconstruct the mean flow
past a square cylinder although no correction reproduces the DNS Reynolds
stresses. They conclude that "even with the wrong stresses, it is possible
to have accurate mean fields, as long as the Reynolds force vector is
correctly represented", the Reynolds-force vector being the divergence of
the stress (see
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)).
Agrawal & Koutsourelakis (2024,
§3.4, Fig. 7) report the same outcome for a tensor-basis closure trained
only on sparse mean velocity and pressure through an adjoint RANS solver
on a [backward-facing step](/benchmarks/backward-facing-step.md): the
learned Reynolds stress shows discrepancies against LES, largest at
$5<x/h<10$, while the predicted mean fields agree well. They read this as
non-uniqueness of the inverse problem, "also reported by other works".
Brenner et al. (2022, §3.5, Fig. 13) find the same with an adjoint
inversion of a multiplicative eddy-viscosity field on the
[periodic hill](/benchmarks/periodic-hill.md): the assimilated mean
velocities improve "definitely", while the stress–strain alignment of the
Reynolds stress is "neither considerably nor consistently improved"
against the baseline $k$-$\varepsilon$ solution. Cherroud et al. (2022,
§4.2, Fig. 7) learn production corrections of the
[$k$-$\omega$ SST model](/methods/k-omega-sst-model.md) that improve
velocity and skin friction on three separated flows while every model
over-predicts $k$ in the separated regions.

**A priori failure that predicts a posteriori failure.** Kim et al. (2024)
feed grid- and test-filtered strain rates (or velocity gradients) into one
network without fusion (T-SR-nFU, T-VG-nFU). A priori these networks give
mean SGS shear stress and SGS dissipation of the wrong sign in the near
shear layers at $x/D=1.06$ (§4.1, Fig. 6). A posteriori they fail:
$L_r/D=0.79$ and 1.28 against 1.56 in DNS, T-SR-nFU being worse than no
model (1.25), and the authors trace the early shear-layer transition to the
weak SGS dissipation seen a priori (§4.2.1, Fig. 9, Table 3).

**A less exact flux, a more exact solution (Riemann solvers).** Ruggeri
et al. (2022, §VI, Fig. 6) find on a supercritical-CO$_2$ shock tube that
the network flux, whose stand-alone mean absolute percentage errors
against the exact Riemann solution are at most 0.191% (variant with the
exact relations) and 1.120% (stand-alone network) over the three real
fluids (Tables III–V), gives a CFD
solution closer to the exact Riemann solution than the exact solver used
as the flux: "the small error made by the neural network … unexpectedly
works in the direction of improving the CFD prediction". They state that
an exact numerical flux "does not guarantee that the CFD solver will
yield the exact solution" of the Riemann problem discretized over many
cells, and that the advantage shrinks at fourth order (§VI, Fig. 7). The
case is inviscid and laminar.

**Cases where the verdicts agree.** Abe (2021) tests the filter width of
eddy-viscosity models on cells of aspect ratio up to about 100 in the free
shear layer behind a backward-facing step. A priori the
[Smagorinsky model](/methods/smagorinsky-model.md) with
$\Delta=(\Delta x\Delta y\Delta z)^{1/3}$ gives a $\nu_{\mathrm{eq}}$ "much
smaller than the reference data" in the shear layer, while the same model
with $\Delta=\max(\Delta x,\Delta y,\Delta z)$ is reasonable; the author's
own mixed model behaves the other way round when the widths are swapped
(§IV C–D, Figs. 9–10). A posteriori, the mixed model with the cube-root
width lengthens the reattachment length from $7.19H$ to $7.43H$ (experiment
$6.51H$) and suppresses the SGS values in the shear layer as the a priori
test predicted (§IV D, Tables II–III, Fig. 11).

Xu et al. (2023) test a family of nonlinear algebraic SGS models of
compressible wall-bounded turbulence both ways (details on
[neural-network SGS models](/methods/neural-network-sgs-model.md)):

- *A priori* (channel at $M=1.5$, training filter ratios 8 and 4 in $x$
  and $z$). The dynamic Smagorinsky, Vreman and WALE models have
  correlations "almost lower than 0.6" and relative errors near 1.0 (§2.2,
  Figs. 1–3); the dynamically closed nonlinear model (ODNA) improves only
  away from the wall ($C>0.4$ for $y^+>50$, $E_r\approx0.98$; §3.1); the
  network-closed version with grid-width-normalized gradients (MANA)
  reaches $C>0.91$ and $E_r<0.4$ for every component (§3.2, Fig. 10).
- *A posteriori.* MANA, run on an untrained LES grid and in untrained
  channels at $M=3.0$, 1.0 and 0.2 and a boundary layer at $M=2.25$,
  matches the filtered-DNS mean velocity, temperature, r.m.s. and
  Reynolds-stress profiles better than the eddy-viscosity models and an
  unmodelled run (§4, Figs. 13–31).
- *Exception.* The dynamically closed model with the same grid-width
  normalization (MDNA), better a priori than ODNA near the wall (Fig. 8),
  is "sometimes unstable" a posteriori when the homogeneous directions
  have few grid points, and costs about 2.54 times the dynamic
  Smagorinsky model, so it is not shown a posteriori (§4.1).
- *Mean SGS fluxes.* A priori (fDNS of the training channel, $n_x=8$,
  $n_z=4$), the dynamic Smagorinsky, Vreman and WALE models and MDNA
  "significantly underestimate" the plane-averaged SGS fluxes of kinetic
  energy and temperature variance (§3.2, Fig. 12). A posteriori (the same
  channel on the untrained $64\times65\times64$ LES grid, $n_x=6$,
  $n_z=2$), the dynamic Smagorinsky model "strongly overestimates" the
  kinetic-energy flux and underestimates the temperature-variance flux,
  while Vreman and WALE underestimate both (§4.1, Fig. 17). The two
  set-ups differ in filter ratios and grid.

Tang et al. (2023) report agreement for a symbolic RANS closure trained a
priori on one [periodic hill](/benchmarks/periodic-hill.md): its predicted
anisotropy is closer to DNS than the $k$-$\varepsilon$ baseline on the
training hill and on two test hills (§III C–D, Figs. 7–8, 12–13), and the
injected closure improves the velocity, though on the steepest test hill
the improvement is "not distinguishable" in the recirculation region
(§III D, Fig. 14; see
[symbolic-regression closures](/methods/symbolic-regression-closure.md)).

Seyedi & Zayernouri (2022) report agreement for their dynamic fractional
SGS model in isotropic turbulence:

- *A priori.* At filter widths 4 and 8 (the paper's dimensionless units,
  filter width over twice the DNS spacing), the model has higher
  correlations than the static and dynamic Smagorinsky models and the
  static fractional model for all six components. Its backscatter share is
  24% and 25%, against 26% and 30% in filtered DNS and 20% and 18% for
  dynamic Smagorinsky (§III.2, Figs. 4–5).
- *A posteriori.* In decaying turbulence at $Re_\lambda=240$, its spectrum
  lies between the over-dissipative Smagorinsky model and the no-model run.
  Its resolved-energy decay is closer to filtered DNS than that of dynamic
  Smagorinsky, markedly so at the larger, VLES filter width (§IV, Figs.
  8–9).
- *A dissipation-tail link.* The authors connect the a priori
  overprediction of the tails of the dynamic Smagorinsky dissipation PDF
  with that model's need for averaging in a posteriori runs (§III.2).

Qi et al. (2022) report agreement for their quasi-dynamic subgrid
kinetic-energy model of compressible flow. A priori its kinetic-energy flux
and wall-normal heat flux correlate with filtered DNS at about 0.95, far
above dynamic Smagorinsky and the dynamic $k_{\mathrm{sgs}}$-equation model
(§4, Figs. 2–3). A posteriori, in LES of the Mach 1.5 channel on three
grids, it reproduces the DNS $Re_\tau=220$ (220, 221 and 218 against
213–201 for dynamic Smagorinsky and 215–208 for the $k_{\mathrm{sgs}}$
model, Tables 2–4), and it is closest to DNS in a Mach 2.25 transitional
boundary layer and a converging Richtmyer–Meshkov flow (§5–6). The
ranking holds in both tests; the shared filter-width coefficient that the
model assumes for all expanded terms is supported a priori only at the
two box-filter widths tested ($6\Delta_z$ channel, $3\Delta_z$ flat
plate), while the LES use the grid filter.

Three papers of one group report the same ranking in both tests, all with
a Gaussian filter of 16 DNS spacings and a filter-to-grid ratio of two:

- *Constant-coefficient spatial gradient model.* Wang et al. (2022)
  rank, a priori, the 19-term network model (correlations 0.985, 0.981 for
  $\tau_{11}$, $\tau_{12}$) above their derived constant-coefficient model
  SGM-7-19 (0.973, 0.973) and the classical
  [gradient model](/methods/gradient-model.md) (0.945, 0.946) (Table II).
  A posteriori they run SGM-7-19, not the network, against the dynamic
  Smagorinsky and dynamic mixed models and implicit LES: SGM-7-19 is
  closest to filtered DNS in spectra, strain-rate and velocity-increment
  PDFs in isotropic turbulence, and in momentum thickness, spectra,
  kinetic energy and Reynolds shear stress in a
  [temporal mixing layer](/benchmarks/temporal-mixing-layer.md)
  (§IV–V, Figs. 2–16), with backscatter clipped for stability (§IV).
- *Density-unweighted compressible LES.* Zhang et al. (2022b) find the
  dynamic iterative approximate deconvolution (DIAD) model best a priori
  ($C>0.98$, $E_{\mathrm{rel}}$ about 0.1, after two iterations) ahead of
  approximate deconvolution (also $C>0.98$) and the gradient model
  ($C>0.9$), and best a
  posteriori in decaying compressible isotropic turbulence, where the
  dynamic Smagorinsky and dynamic mixed models are over-dissipative and
  approximate deconvolution under-dissipative (Abstract, §IV, Figs. 1–23;
  see [scale-similarity model](/methods/scale-similarity-model.md)).
- *Dense gas.* Zhang et al. (2022d) find DIAD's correlations above 0.98
  and relative errors below 0.2 for the stress, the subgrid pressure and
  the pressure work, the exception being the internal-energy flux at
  $M_t=0.4$ (above 0.96, below 0.3); a posteriori DIAD reproduces the PDFs
  of those terms and beats dynamic Smagorinsky in kinetic-energy decay,
  spectra and the PDFs of the subgrid energy flux, strain and vorticity
  (§IV, Figs. 1–18). Dropping the thermodynamic subgrid terms changes the
  a posteriori statistics little, consistent with their small a priori rms
  (§IV B, §V).

These rankings and that of Valencia et al. (2026, table above) stand
side by side: Valencia et al. place DIAD slightly below
approximate and discrete direct deconvolution a priori, against the
*total* unresolved stress on the LES grid at filter-to-grid ratios 2 and
4, while Zhang et al. (2022b) rank it first against the filtered-DNS
subgrid stress and in LES, and Zhang et al. (2022d, §I) cite that result.

**Both tests on the same filter widths.** Inagaki & Kobayashi (2023)
report an a priori and an a posteriori result for channel flow at
$Re_\tau=400$. A priori, with a "medium" filter ($\Delta x^+=52.4$,
$\Delta z^+=26.2$ equivalent), the anisotropic, energy-neutral part of the
mean subgrid shear stress is negligible, so an eddy-viscosity model can
carry both the energy transfer and the mean shear stress; with a "coarse"
filter ($105$, $52.4$) it is comparable to the eddy-viscosity part (§III C,
Fig. 3). A posteriori, a dynamic-Smagorinsky LES on the medium grid
predicts the DNS mean velocity and on the coarse grid overestimates it
(App. C, Figs. 16–17, Table I). The authors chose the filter lengths so
that "the conventional eddy-viscosity models can fairly predict the mean
velocity profile for the medium filter case, whereas it fails for the
coarse filter case" (§V). The paper does not test its anisotropic models
a posteriori.

**An a priori advantage that shows only in one flow region.** Helm &
Martín (2022, Sec. II, Sec. IV F) cite the a priori study of Martín et al.
(2000) in compressible isotropic turbulence, which found better stress and
heat-flux correlations for the dynamic mixed model than for the dynamic
eddy-viscosity model. In a posteriori LES of compression-ramp
[shock–boundary-layer interactions](/benchmarks/shock-turbulent-boundary-layer-interaction.md),
removing the scale-similar part changes the Mach 3 separation length by
less than 5%. The reverse-flow probability at the attached Mach 7 corner
moves from 31% to 35%. The separated Mach 7 case is the exception: the
separation length grows by 30% (Sec. IV F, Sec. V; "as much as a 32%" in
the abstract). The difference originates in the separation shear layer,
whose spreading rate falls from 0.194 to 0.173 without the similarity
term, while the incoming boundary layers are identical (Sec. IV F, Figs.
30–33; see [scale-similarity model](/methods/scale-similarity-model.md)).

**A posteriori errors smaller than a priori errors.** McConkey et al.
(2022, §IV B, Figs. 20–21) inject their network predictions into RANS of
the held-out hill. The relative error of the converged velocity is smaller
than the relative error of the injected closure term, and the reattachment
point moves from $x_R/h=5.42$ (base model) to 4.10, against 4.50 in DNS
(errors of 20% and 8.9%). The authors conclude that "under certain
conditions, the RANS equations can suppress rather than amplify errors in
the closure prediction" (§V). This is one geometry family, tested by
interpolation in the steepness factor.

**A priori subgrid production against a posteriori total dissipation.**
[Cao et al. (2022b)](/sources/cao-2022-c.md) compare a volume average
computed a priori with one inferred a posteriori, in the compressible
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at Mach 0.1,
$Re=1600$. A priori, box-filtered $1024^3$ DNS (two cells coarsened into
one per direction) gives the mean subgrid production
$\langle\Pi\rangle$, with forward and backward transfer coexisting
pointwise, and a mean far below the solenoidal viscous dissipation
(§IV B, Table I, Figs. 5–6). A posteriori, $256^3$ LES with a
fourth-order gas-kinetic scheme give the total subgrid dissipation as the
residual $-\mathrm dE_k/\mathrm dt$ minus the physical dissipation, the
modelled and numerical parts together (§IV C, Eq. 22, Table II; see
[implicit LES](/definitions/implicit-les.md)). The authors state that
the a posteriori value exceeds the a priori one except in the late decay
($t=15$), and read the comparison as numerical dissipation already
sufficient for this flow, so that an explicit eddy viscosity adds
dissipation that is not needed (§IV B–C, §V). The a priori number is a
filtered-DNS transfer at the a priori filter width (Eq. 18), the a
posteriori one a residual of the LES energy budget (Eq. 22). See
Qualifications for how the printed statements fit the tables.

## Mechanisms named by the sources

1. **Feature mismatch.** Features computed from reference data differ from
   the same features computed in the solver. Duraisamy (2021, §IV.A)
   writes $\boldsymbol\zeta$ for features from DNS and $\boldsymbol\zeta_{\mathrm m}$
   for the same features from the model (page-local: subscript
   $\mathrm m$ marks a quantity of the model's own solution). The paper's
   example is the mean strain-rate tensor made dimensionless by
   $k/\varepsilon$: the model's $k$ and
   $\varepsilon$ can be very different from the DNS values even when the
   mean strain agrees, so RANS secondary variables "should not be
   interpreted as one-to-one with DNS quantities". Duraisamy et al. (2019,
   §5.4) make the same point: the RANS dissipation rate supplies scale
   information, and its calibrated value differs from the true one.
   Duraisamy (2021) recommends monitoring the correlation between $\boldsymbol\zeta$ and
   $\boldsymbol\zeta_{\mathrm m}$, not only between target and prediction.
   Sirignano & MacArt (2023, §1, §5) state the LES version: an a priori
   network "is trained on DNS inputs but receives LES or RANS inputs
   during prediction". Maejima & Kawai (2025, §1, §3.1) state the extreme
   case: on very coarse grids the resolved LES field is itself
   non-physical, so filtered DNS is the wrong training input, and paired
   (LES, DNS) data cannot exist because the two are separate simulations;
   their remedy is an unsupervised map from LES to filtered-DNS fields.
   Oulghelou et al. (2025, §3), following Cherroud et al. as they cite
   them, evaluate the features of their weight regressor on the baseline RANS
   solution, the same input the model receives in prediction.
   Sandberg & Zhao (2022, §3.2) name the RANS case for the time scale:
   the $k/\varepsilon$ or $1/\omega$ of the RANS model can differ
   substantially from that of the reference data, and the frozen approach
   of Parneix et al., as they cite it, solves the $\varepsilon$ or
   $\omega$ equation with the reference mean velocity and Reynolds
   stresses frozen, so that the training features carry the time scale
   the trained model will meet in the solver.
2. **Error accumulation.** In the solver the model sees inputs that carry
   its own past errors. Duraisamy (2021, §IV.A, Fig. 1) illustrates this
   with a neural super-resolution map: it reconstructs fine scales well
   offline at nondimensional times 0.6 and 6.0, but loses them on-line by
   time 6.0. The flow, grid and network of this example are not specified.
   Domingo & Vervisch (2023, §1) state that a priori tests on frozen DNS
   inputs "cannot always allow for reaching definitive conclusions",
   because they miss error accumulation and error compensation in time.
   Bae & Koumoutsakos (2022, preprint p. 3) state the same argument for
   wall models: supervised closures trained on single-step targets are not
   trained to compensate systematic DNS–LES discrepancies or compounding
   errors, and, since "wall models are more sensitive than SGS models"
   (citing their ref. 22), compounding errors are expected to hurt
   more in wall-modelled LES. They recall a posteriori studies that exposed
   ill-conditioning of data-driven SGS models. Kim et al. (2022, §III C)
   make the same point for SGS models: their training succeeds "through the
   online learning process in which the temporal reaction of the SGS model
   in the actual LES is considered".
3. **Balance between model terms.** Exact inputs do not repair a model
   whose other terms were tuned to its own variables. Duraisamy (2021,
   §IV.A) cites results in which using exact DNS or LES $k$ and
   $\varepsilon$ in the eddy viscosity of one- and two-equation models did not improve
   predictions (Raiesi et al.), and substituting DNS Reynolds stresses did
   not give satisfactory velocity fields (Thompson et al.). Duraisamy et
   al. (2019, §6) recall the same Thompson et al. result, with Poroseva et
   al., and attribute it partly to ill-conditioning of the RANS equations
   (Wu et al.). Agrawal & Koutsourelakis (2024, §1, §2.2) make the same
   argument against "model regression": small errors in the stress can be
   amplified when the RANS equations are solved, citing Thompson et al. McConkey et al. (2022, §II B–C, Figs. 4–6) quantify how the
   injection form decides the error left by a perfect prediction. They
   inject DNS-derived quantities into RANS of the periodic hill with
   steepness factor 1.2 at $Re_h=5600$ and compare the converged
   velocities:

   | Injection | RMSE of $\langle u\rangle$ (m/s) | RMSE of $\langle v\rangle$ (m/s) |
   |---|---|---|
   | DNS anisotropy, fully explicit | $2.613\times10^{-3}$ | $6.408\times10^{-4}$ |
   | non-negative optimal eddy viscosity implicit, remaining anisotropy explicit | $2.265\times10^{-4}$ | $6.444\times10^{-5}$ |
   | optimal eddy viscosity alone (no non-linear part) | $1.672\times10^{-3}$ | $2.978\times10^{-4}$ |

   The split form is "an order of magnitude" better than the fully explicit
   one. The authors note that part of the difference can come from the
   first-order schemes that the explicit injection needed for stability.
   They recommend evaluating every data-driven framework by the
   conditioning error that remains after a perfect model prediction (§II
   C, §IV B).
4. **Discretization error.** In LES the discrete operator adds a
   solution-dependent term that the a priori analysis of the continuous
   filtered equations does not contain. Beck & Kurz (2023, §I) state that
   this term "is at the heart of the discrepancy between a priori and a
   posteriori closure model performance"; see
   [discretization-consistent closure](/definitions/discretization-consistent-closure.md).
   Agdestein & Sanderse (2025, App. F) compute the continuous and the
   discrete convective commutator errors of the 2D Taylor–Green vortex:
   they have the same spatial form but different coefficients.
   Kurz et al. (2023, §1, §3.3) push the argument further for implicitly
   filtered DG-LES: the filter is unknown (an element-local $L_2$
   projection coupled through the numerical fluxes, a non-linear kernel),
   so the exact closure term cannot be computed even from the full DNS and
   supervised learning there is, "from our perspective, ill-posed".
   Surrogate targets from an approximating explicit filter produce
   "severe inconsistencies between the training and actual simulations"
   (§1, citing their ref. [8]). Lozano-Durán & Bae (2023, §2.5)
   give the same reason for not training a wall model on filtered DNS:
   the subgrid tensor of an implicitly filtered LES does not coincide with
   the stress obtained by filtering the Navier–Stokes equations.
   Kim et al. (2024, p. A6-21, Eqs. 4.2–4.3, Table 4) estimate the size of
   this error for their second-order finite-difference cylinder LES,
   following Sirignano et al.: the mean relative difference between
   velocity gradients differenced on the LES and on the DNS grid is
   0.5690, 0.5455, 0.5320, 0.5136 and 0.4986 from the coarsest to the
   finest LES grid. They call the finite-difference errors "not so
   significant" and conclude that their networks "may not suffer" from
   them; the numbers are those printed, the judgement is theirs.
5. **Inputs outside the training distribution during convergence.** In a
   steady RANS solver the embedded model is evaluated on every iterate, not
   only on the converged field it was trained on. Yan et al. (2022, §3.1.2)
   attribute the mismatch between regression loss and a posteriori error
   to this: a low loss guarantees the correct correction only on the
   converged field, while during the non-converged iterations the network
   sees inputs unlike its training data.
6. **Flow-regime mismatch of the reference data.** A priori data drawn from
   one regime can fail in another. Pereira et al. (2021, §IV.3.2) trace the
   a posteriori failure of their S3 strategy to resolution parameters
   taken from fully developed homogeneous turbulence and applied to a flow
   that is laminar and then transitional at early times; they suggest
   dynamic, stage-dependent parameters (§V).
7. **Distribution shift between training and use.** Kang et al. (2023,
   §3.2) name the failure of a network on an untrained Reynolds number or
   grid a "prior probability shift", the output distribution differing
   between training and test (citing the machine-learning
   literature). Their remedy is to normalize inputs and outputs so that the
   normalized distributions do not change with $Re$ and resolution (see
   [neural-network SGS models](/methods/neural-network-sgs-model.md)).
   Wu & Lele (2026, §1, §3, §7) read the whole a priori/a posteriori gap
   of supervised SGS networks as a distribution shift between training
   data and LES (citing Hu et al. 2025) and name two spatial sources,
   setting aside the error accumulation of mechanism 2. On the *output*
   side, the statistics of $\tau_{ij}$ depend on the filter shape, and
   the implicit filter of the LES, "a product of both the grid and the
   numerical method" (two-thirds dealiasing, for instance), differs from
   the box filter of the training data; applying the dealiasing cutoff on
   top of the box filter "completely changes the subgrid stress field"
   (§3.2.2, Fig. 4). A network trained on one filter can then "overfit to
   filter peculiarities". On the *input* side, higher powers of the
   velocity-gradient tensor "suffer more from numerical artifacts such as
   aliasing, especially at the grid cutoff resolution". Their remedies are
   training on several filter shapes and simpler inputs (see
   [neural-network SGS models](/methods/neural-network-sgs-model.md)).
8. **The solver changes the input the a priori test froze.** Mukha et al.
   (2025, §III.B.3) find that time-averaging the wall-model input, which
   helps a priori on recorded velocity, alters the velocity at the
   sampling point once the model is coupled, so the a priori gain does
   not carry over. Model and input are coupled through the solution,
   which an a priori test with fixed inputs does not represent.
9. **A score that does not see the energy transfer.** A stress
   correlation can be high for a model that transfers no energy between
   scales. Jakhar et al. (2026, pp. 1–3) find this for the second-order
   gradient model in 2-D turbulence and repair the selection score by
   adding the correlations of the energy transfer and of its forward and
   backscatter parts (above).

## Testbeds that allow both tests

Domingo & Vervisch (2023, §3.1) describe a DNS box nested inside a
well-resolved LES of a premixed Bunsen burner. Coarsening the DNS zone to
LES filter widths of 170–640 µm gives a posteriori tests on the same
configuration that provides the a priori data (Fig. 6). On this database,
CNN closures for the filtered progress-variable source reach about 1%
maximum a priori error on the trained filter sizes and 16% on an untrained
one (Fig. 9). See
[direct numerical simulation](/definitions/direct-numerical-simulation.md).

**An approximation tested against its own original.** Nuca et al.
(2025, §VI) test explicit closed-form approximations of the Spalding,
Reichardt and equilibrium-ODE wall laws, whose reference is the iterated
original model, not DNS. A priori on the channel signal the explicit
wall stress differs from the iterated one by less than 0.07% for the
fixed-constant ($N=3$-bump) approximations and 0.7% for the global
($N=1$) ones; a posteriori, in WMLES of the Aérospatiale A-airfoil near
stall (OpenFOAM, $18.7\times10^6$ cells, wall model on the suction side),
the explicit Spalding stress deviates by at most 0.06% over a much wider
range of the local Reynolds number $Re_y$ (Fig. 8), so the verdicts
agree. The robustness question, however, appears only in the running
complex flow: Newton iterations of the original laws "would often
sporadically diverge" near transition and with sampling heights above
the first off-wall node, and the authors state that channel and
flat-plate tests, on which much of the wall-model literature rests, probe
accuracy but not robustness (§I–II). As initial guesses the explicit
laws cut the maximum iteration count from 11 and 10 to 3 (Reichardt,
Spalding) and the fixed-point maximum of the ODE model from the cap of
100 (non-convergence) to 6 on the airfoil, against 3 to 2 and 6 to 2 on
the channel (Tables VII–VIII); see
[equilibrium wall model](/methods/equilibrium-wall-model.md).

For wall models, Griffin et al. (2023) test their
[inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md)
a priori on 48 DNS cases with matching data at $h_{\mathrm{wm}}=0.3\delta$
(§3), then a posteriori in WMLES of nine compressible channels with 12
points per half-height (§4). In this case the two verdicts agree: the new
model beats the classical one in both. Vadrot et al. (2023b) use channel
flow at $Re_\tau$ from 180 to $10^{10}$ as an a posteriori sanity check
for [machine-learning wall models](/methods/machine-learning-wall-model.md),
and add a priori law-of-the-wall tests to locate where each model fails
(§IV B).

**Reference data that are not DNS.** Abe (2021, §IV B, Fig. 5) takes the a
priori reference from a fine wall-resolved LES of the backward-facing step
($\Delta x^+=\Delta z^+=7.25$), top-hat filtered in $x$ and $z$ to the
coarse grid ($\Delta x^+=29$), on 20 snapshots. The fine LES's subgrid
share of the turbulent energy and shear stress is very small, so it "can
be approximately regarded as DNS data"; filtering also in $y$ changes the
SGS values little (App. C). Pereira et al. (2021, §II, App. B) take as
reference the same code run without closure ($f_k=0$) on the same grid,
whose initial interface perturbations are not fully resolved (§IV.2).
Lozano-Durán & Bae (2023, §2.5) train their
[building-block-flow wall model](/methods/building-block-flow-wall-model.md)
on wall-modelled LES run in the deployment solver, with a subgrid
correction that forces the LES mean profile onto the DNS one and a wall
boundary condition sampling the DNS wall-stress PDF. The training data
then carry the solver's numerical errors and gridding; only DNS
statistics, no instantaneous DNS fields or filter shape, are needed. Kurz
et al. (2023, §3.5) note that the reward of their RL closure could use
any high-level statistic (literature or experimental data, the $k^{-5/3}$
law) in place of the DNS spectrum. Vadrot et al. (2023a, §II.B.3, §V)
reward their [reinforcement-learning wall model](/methods/reinforcement-learning-closure.md)
by the distance of the modelled wall stress from the mean value fixed by
the driving pressure gradient of the channel, $\tau_w=-\delta\,dp_0/dx$
(translated: $\delta$ the half-height), so training uses no filtered DNS
and, in their words, removes the a priori/a posteriori input
inconsistency. Wang et al. (2023c, §II.B) calibrate an SGS coefficient
against the filtered-DNS energy spectrum only, not against fields.

**Averaging and filtering on the same DNS.** Tonicello et al. (2022,
§4.2, Fig. 19) evaluate the same unclosed term of a compression–expansion
ramp DNS at Mach 2.91 in both senses: the Favre time–span average
(RANS) and filtered snapshots (LES, 30 snapshots, $\Delta=2h$, $4h$,
$8h$). The PDF of the subgrid or Reynolds-stress dissipation is
dominated by forward transfer for the average and has much wider positive
and negative tails for the filtered fields, with a similar mean. The
authors read this as consistent with eddy-viscosity models reproducing the
mean transfer but not the local one (see
[energy backscatter](/definitions/energy-backscatter.md)).

**Discretization-aware a priori data.** Basile et al. (2023, §3.2,
§4.2.3) cite Chapelier and co-workers, who set an under-resolution
threshold of a DG smoothness indicator a priori from DNS of the
Taylor–Green vortex at $Re=5000$, finding values close to the $-5/3$
inertial slope, and Beck et al., who projected filtered DNS onto a DG grid a
priori, obtaining fields that are discontinuous at element interfaces; see
[mesh adaptation](/methods/mesh-adaptation.md) and
[discretization-consistent closure](/definitions/discretization-consistent-closure.md).

## Qualifications

- The pair describes where a test is done, not the quality of the reference.
  A posteriori LES are compared with filtered DNS, whose filter is a
  choice. Vicente Cruz & Lamballais (2023, §6.4, Fig. 19) show that the a
  priori cusp of the spectral eddy viscosity changes by more than an order
  of magnitude between a super-Gaussian and a sharp cutoff filter, while
  the low-wavenumber plateau is insensitive to the filter shape.
- Xu et al. (2023, §2.2, §4) filter in the streamwise and spanwise
  directions only, and their a posteriori reference in each case is the DNS
  filtered with the ratios $n_x$, $n_z$ (page-local) of the LES to the DNS
  spacing in those directions (6 and 2 on the untrained grid of the
  training channel); no averaging times are stated. Their summaries of the
  eddy-viscosity correlations differ between §2.2 ("almost lower than
  0.6") and §3.1 ("mostly smaller than 0.4").
- Vela-Martín (2022) is an a priori study only (filtered DNS of forced
  isotropic turbulence at $Re_\lambda=140$, 240 and 324). Its conclusion
  that local backscatter need not be modelled is not tested a posteriori
  there.
- Agdestein & Sanderse (2025, §5.2) show that the ordering can reverse.
  In their divergence-consistent formulation with a face-averaging filter,
  an a priori-trained CNN is already stable and accurate, and a posteriori
  training improves it only slightly. Agreement between the two tests
  depends on how closely the a priori data match the discrete equations
  the model will be used in.
- Prakash et al. (2022, Eq. 19) define C.C. as a double sum
  $\sum_i\sum_j$ of per-component correlation coefficients and state that a
  perfect model has C.C. $=1$; as printed, a perfect model would give 9,
  so an averaging factor is missing, as the text's "mean correlation
  coefficient" implies *(compiler check, not in the sources)*.
- The structural-accuracy explanation of Prakash et al. (2022) and the
  gauge argument of Vela-Martín (2022) answer different questions: the
  first holds dissipation fixed and varies correlation, the second shows
  that correlation with one gauge of $\tau_{ij}$ is not a unique measure.
  Neither paper tests the other's claim; no contradiction is recorded.
- In Abe's (2021) test the a priori metric is $\nu_{\mathrm{eq}}$, a
  dissipation measure; the author notes that good $\nu_{\mathrm{eq}}$
  agreement of the similarity models does not imply their a posteriori
  stability (§V). The same projection of a stress on a strain appears in
  RANS as the optimal eddy viscosity of Wu et al.,
  $-\tfrac12(R_{ij}-\tfrac23k\delta_{ij})S_{ij}/(S_{kl}S_{kl})$ (McConkey et
  al. 2022, Eq. 6, whose non-negative version, Eq. 7, is their training
  label), and as the DNS eddy-viscosity estimate of Cato et al. (2023, Eq.
  18), which reduces to the same expression once its
  $\nabla_s\langle\boldsymbol u\rangle=2S_{ij}$ and sign convention are
  translated *(compiler check, not in the sources)*.
- Kim et al. (2022) train a posteriori by construction. Their comparison
  with a supervised model is cited from another study (Park & Choi
  2021), not rerun with the same solver.
- Seyedi & Zayernouri (2022) quote no correlation values; they are shown
  only in Figs. 4 and 7. Their a posteriori LES start from filtered DNS,
  and the authors note that DNS and LES "have not been initiated with the
  same initial conditions", hence the comparison with filtered DNS (§IV).
- The conditioning comparison of McConkey et al. (2022) is confounded, as
  the authors state: the fully explicit injection needed first-order
  convection schemes (§II C).
- Sirignano & MacArt (2023) state the strength of their a posteriori
  result differently in two places: "for all cases and all statistics"
  the learned closure matches filtered DNS more closely than the no-model,
  dynamic Smagorinsky and anisotropic minimum-dissipation LES (§4.2),
  while the conclusion says the learned and minimum-dissipation models
  "had similar error for the RMS velocity components" (§7).
- Kang et al. (2023) compare their network with the algebraic mixed models
  as each is run in practice: the algebraic models with averaging and
  clipping, the network without clipping and without averaging of its
  output, though its normalization factors are volume averages (§2.4,
  §3.3). The a posteriori ranking is
  therefore one of models with their stabilization, not of the stress
  forms alone.
- Kim et al. (2024) report the networks "better than" the dynamic
  Smagorinsky model on the training grid and on a coarser one; on the
  finer untrained grid they find the dynamic model in good agreement with
  DNS, $L_r/D=1.45$, against 1.62 and 1.57 for the two fusion networks and
  1.56 in DNS (§4.2.2, Table 3). Their dynamic coefficient is averaged in
  the span only (§4.2).
- Steinhausen et al. (2023) validate their manifold a priori only; the
  coupled a posteriori test is deferred (§5–6). Böttler et al. (2023) run
  both and find the curvature-based manifold better in each (§3.1–3.3).
  Both are laminar or DNS-resolved combustion configurations without a
  turbulence closure.
- **One-sided studies.** Some sources run only one of the two tests, so
  the disagreement stated in the lead cannot arise in them.
  Zangeneh (2021) reports no a priori evaluation of its random forest
  (§III); Berger et al. (2022) assess manifold inputs on DNS without a
  coupled simulation.
  He et al. (2022, §2.2, §4.3) evaluate their random-forest correction of
  the Spalart–Allmaras model offline only: the statement that the
  corrected viscosity ratio "matches well" the target profiles (Fig. 12)
  is made on frozen mean fields, not on a converged coupled RANS solution.
  Tonicello et al. (2022) are a priori only; their proposed bulk-viscosity
  model of the subgrid trace is not run (§5–6).
  Rickard & Kasbaoui (2026) run only the a priori analysis of their
  wall-slip models and present no forward simulation (§2, §7); Ranjbar
  et al. (2026) run only a posteriori tests. Valencia et al. (2026) are
  a priori only: their conclusion that only deconvolution compensates the
  filter, and their cost statements (taken from cited a posteriori works,
  §V C), are not tested in an LES there; the a priori snapshot time is not
  stated. Their text says that from FGR 2 to 4 the relative errors of the
  deconvolution models fall "by nearly half" and that the classical models
  improve marginally, whereas Tables VI–VII show reductions by factors of
  about 2.4 to 4.1 and a dynamic-Smagorinsky $E_{\mathrm{rel},xx}$ that
  grows from 1.2955 to 1.9644 *(compiler check, not in the sources)*.
- **Nuca et al. (2025)** have no DNS or experimental reference in either
  test; accuracy against data is explicitly not their goal (§VI), and the
  airfoil statistics cover one chord-based flow time.
- **What Jakhar et al. (2026) show in the version read.** The a priori
  tables of the main text and the stated stability threshold (80% of the
  DNS enstrophy) are printed; the stability runs, Table S1 and the
  domain-averaged energies are in the Supplemental Material, which is not
  in the arXiv file read. The claim that the closure is "generalizable"
  rests on its having no tunable coefficient besides $\Delta$ (p. 4).
- **The a priori test set of Wu & Lele (2026)** is box-filtered for every
  network (§4), whatever filters the network was trained on; Table 2
  lists ten of the eighteen networks of Table 1, while the text speaks of
  "all" networks.
- **Cao et al. (2022b): text against tables.** The abstract and §IV B
  call the solenoidal dissipation "approximately 20 times larger" than the
  a priori subgrid production; Table I gives ratios of about 68, 32, 22
  and 35 at $t=2.5$, 5, 10, 15 *(compiler check, not in the sources)*.
  §IV C states that the a posteriori total subgrid dissipation exceeds the
  a priori production "except for the late decaying stage at $t=15$";
  at $t=15$ Table II gives $2.5\times10^{-4}$ (static Smagorinsky) and
  $1.8\times10^{-4}$ (Vreman), both above the a priori
  $1.3\times10^{-4}$, so the exception holds for implicit LES
  ($1.8\times10^{-5}$) and the dynamic model ($9.4\times10^{-5}$) only
  *(compiler check, not in the sources)*. The abstract calls the a priori
  quantity the "ensemble filtered SGS dissipation rate", §IV B the
  "filtered SGS production term".
- **Zhang et al. (2022b), Table II against text.** §IV A calls the
  density–temperature term at $M_t=0.8$ "two orders of magnitude higher"
  than at $M_t=0.4$; Table II prints 0.11 and 0.0060, a factor of about
  18 *(compiler check, not in the sources)*. The case-2 turbulent Mach
  number is 0.79 in Tables I–II and 0.80 in Table III.
- **Wang et al. (2022), two tables.** The neighbour coefficients of the
  19-term network are printed as $\mp1.6\times10^{-2}$ in Table I and as
  $\mp0.0016$ in Table II; the text's statement that the local
  coefficient (0.18) is "one order larger" matches Table I.

# Citations

- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §IV.A (three mechanisms, "neither necessary nor sufficient", Fig. 1), §IV.B (Fig. 2, from Sirignano et al.).
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §5.3 (terminology), §5.4 and §6 (training and prediction environments, operational latent variables).
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §V, Eq. 14 (correlation metric), Bardina model a priori against a posteriori.
- [Vela-Martín (2022)](/sources/velamartin-2022.md) — §3 (gauge invariance), §6.3 (correlation of equivalent stresses), §8 (interpretation).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §2.2, Eqs. 23 and 29; §6.3, Fig. 11; §6.4, Fig. 19.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §I (discretization-induced term and the a priori/a posteriori gap).
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §4.3, Eq. 24; §5.2.2; App. F.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §I (literature), §III A, Eq. 9; §IV B, Fig. 12; §V.
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §3 (a priori, 48 DNS cases), §4 (a posteriori WMLES).
- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — §1 (limits of a priori tests), §3.1, Figs. 6 and 9.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — preprint v1, p. 3 (definitions, single-step targets, compounding errors).
- [Prakash et al. (2022)](/sources/prakash-2022.md) — arXiv v2, §I–II, §III.A, Eq. 19, Figs. 1–3; §III.B.3, Table 4; §IV.
- [Abe (2021)](/sources/abe-2021.md) — §IV B–D, Eq. 17, Figs. 5, 9–11, Tables II–III; §V; App. C.
- [Pereira et al. (2021)](/sources/pereira-2021.md) — arXiv v2, §II, §III (strategies S1–S3), §IV.2, §IV.3.2, §V, App. B.
- [Yan et al. (2022)](/sources/yan-2022.md) — accepted manuscript, §3.1.2, Table 1; §3.2.2 (offline and online prediction).
- [Basile et al. (2023)](/sources/basile-2023.md) — HAL accepted manuscript, §3.1 (a posteriori error estimator), §3.2, §4.2.3 (a priori DG studies cited).
- [Alauzet et al. (2022)](/sources/alauzet-2022.md) — §6.2 (a priori goal-oriented error estimate).
- [Kim et al. (2022)](/sources/kim-2022.md) — arXiv v2: §III C (training in the LES, a posteriori results, supervised model cited), §III E, Eqs. 27–28, Table IV (alignment and correlation metrics).
- [McConkey et al. (2022)](/sources/mcconkey-2022.md) — arXiv v1: §II A–C, Eq. 6, Figs. 4–6 (conditioning test); §IV A, Figs. 11–14 (a priori errors); §IV B, Figs. 20–21; §V.
- [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) — arXiv v3: §III.1–III.2, Figs. 4–7 (a priori); §IV, Figs. 8–10 (a posteriori).
- [Helm & Martín (2022)](/sources/helm-2022.md) — Sec. II, Sec. IV F, Figs. 30–33, Sec. V; abstract (a priori study cited, a posteriori ablation).
- [Cato et al. (2023)](/sources/cato-2023.md) — HAL author manuscript: §V C, Figs. 16–19 (mean flow without the right stresses), Eq. 18.
- [Kang et al. (2023)](/sources/kang-2023.md) — Eq. 3.1, §3.1, Tables 3–4 (correlations, alignment); §3.2 (prior probability shift); §3.3, Table 6, Figs. 19–22 (a priori ranking against a posteriori accuracy, averaging and clipping).
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §1 (DNS inputs against LES inputs, RL not a priori), §4.2, §5, Figs. 11–12 (a priori against adjoint-trained network), §7.
- [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) — arXiv v3: §II–III, Fig. 3 (a priori budgets, medium and coarse filters), §IV B, Fig. 13 (a priori model test), App. C, Figs. 16–17, Table I (a posteriori DSM LES), §V (choice of filter lengths).
- [Tang et al. (2023)](/sources/tang-2023.md) — arXiv v1: §III C–D, Figs. 7–8, 12–14 (a priori anisotropy, a posteriori velocity).
- [Kurz et al. (2023)](/sources/kurz-2023.md) — arXiv v2: §1, §3.3 (unknown implicit filter, supervised learning ill-posed), Fig. 3, §3.5 (reward targets), §4.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §2.5 (training on solver-consistent WMLES instead of filtered DNS).
- [Kim et al. (2024)](/sources/kim-2024.md) — §4.1, Figs. 6–7, Eq. 4.1 (a priori profiles, noise robustness); §4.2, Table 3, Fig. 9 (a posteriori); p. A6-21, Eqs. 4.2–4.3, Table 4 (discretization error).
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — arXiv v3: §II.B (spectrum target); §III, Figs. 3–4 (stress PDFs against a posteriori statistics); §V.
- [Domaradzki (2024)](/sources/domaradzki-2024.md) — §1 (similarity models cited); §3.1, Fig. 6 (transfer correlations).
- [van Gastelen et al. (2024)](/sources/vangastelen-2024.md) — arXiv v5: §1 (cited cases); §3.4, Eqs. 51–52 (derivative and trajectory fitting); §4.2.
- [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) — arXiv v2: §1, §2.2, Eqs. 11–12 (model and trajectory regression); §3.4, Fig. 7 (stress discrepancy, accurate mean fields).
- [Vadrot et al. (2023a)](/sources/vadrot-2023.md) — arXiv v3: §II.B.3, Eqs. 4–5 (reward on the known mean wall stress); §V.
- [Chen et al. (2024)](/sources/chen-2024.md) — §3 ("a priori" DNS diagnostics), §4 ("a posteriori" boundary-layer solutions).
- [Pacciani et al. (2025)](/sources/pacciani-2025.md) — validation called "a posteriori".
- [Steinhausen et al. (2023)](/sources/steinhausen-2023.md) — arXiv v1: §5, Fig. 7 (a priori manifold test, tabulation error isolated), §6.
- [Böttler et al. (2023)](/sources/bottler-2023.md) — arXiv v1: §1, §3.1, Fig. 3 (a priori deviations), §3.2–3.3 (a posteriori).
- [Maejima & Kawai (2025)](/sources/maejima-2025.md) — §1, §3.1 (fDNS against coarse LES, unpaired data); §5.3, Figs. 18–21 (a priori on coarse-LES input); §6.1, Fig. 22 (a posteriori).
- [Zhao et al. (2025)](/sources/zhao-2025.md) — arXiv v3: §3, §3.1, Table 2, Figs. 6–7 (test loss against rollout); §4.1 ("a priori test" of training behaviour); §5.3, Fig. 25.
- [Li et al. (2024)](/sources/li-2024.md) — arXiv v2: §V (a posteriori rollouts from 10 unseen initial fields).
- [Mukha et al. (2025)](/sources/mukha-2025.md) — arXiv v1: §III.B.3, Table III, Figs. 4–5 (a priori wall stress, time averaging, a posteriori without gain).
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — arXiv v2: §2–3 (frozen-RANS targets, features from the baseline solution), §4–5 (a posteriori).
- [Wu et al. (2025)](/sources/wu-2025.md) — author manuscript: Fig. 14 (a priori check of the correction), §3.3, §4 (a posteriori).
- [Fanizza et al. (2025)](/sources/fanizza-2025.md) — §3.5 (iterative and a posteriori metrics of data assimilation).
- [Wu & Lele (2026)](/sources/wu-2026.md) — arXiv v2: §1, §3, §3.2.2, Fig. 4 (distribution shift, filter dependence of $\tau_{ij}$); §4, Table 2 (a priori metrics); §5, Eq. 5.1, Tables 3–4 (sum spectral error, a posteriori spread); §5.1.1, §5.2.1; §7.
- [Jakhar et al. (2026)](/sources/jakhar-2026.md) — arXiv v3: pp. 1–4, Figs. 1–3 (criterion, a priori table, a posteriori stability and threshold); App. B, Eq. 5 (CC).
- [Caban et al. (2026)](/sources/caban-2026.md) — §4.1–4.2, Eqs. 36–39, Figs. 6, 8 (a priori deconvolution error); §5.4, Tables 5, 9 (a posteriori Taylor–Green vortex).
- [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md) — §2, §3, §7 (a priori analysis only, a posteriori deferred).
- [Valencia et al. (2026)](/sources/valencia-2026.md) — §I (a priori on the DNS grid overestimates accuracy); §II C, Eqs. 23–29 (total, grid-truncation and sub-filter stresses); §V A, Eqs. 53–54 (protocol, metrics); §V B–C, Tables III–VII, Figs. 5–23; §VI.
- [Nuca et al. (2025)](/sources/nuca-2025.md) — §I–II, Fig. 2 (robustness only in complex flows); §VI, Tables VII–VIII, Fig. 8 (a priori channel signal, in-situ airfoil WMLES).
- [Li et al. (2021)](/sources/li-2021.md) — §III B–C, Eq. 18 (a priori correlation, a posteriori LES against filtered DNS).
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §4.3 (definitions for RANS closures).
- [Zangeneh (2021)](/sources/zangeneh-2021.md) — §III (a posteriori tests only).
- [Ruggeri et al. (2022)](/sources/ruggeri-2022.md) — §V, Tables III–V (stand-alone errors); §VI, Figs. 6–7 (network flux beats the exact flux in the CFD solution; fourth order).
- [Berger et al. (2022)](/sources/berger-2022.md) — §3.4.1–3.4.3, Eqs. 22–24, Figs. 16, 22 (optimal-estimator assessment of manifold inputs; blind to mean shifts).
- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) — arXiv v1: §III, §III.B, Figs. 8–10 (a posteriori tests against coarse unmodelled runs).
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §3.1, Fig. 9 (workflow, definitions, cost on mean quantities); §3.2 (frozen time scale); §4.1 (junction flow and jet in crossflow, cited); §5.
- [He et al. (2022)](/sources/he-2022-b.md) — §2.2 (offline and online phases), §4.3, Fig. 12 (offline only).
- [Qi et al. (2022)](/sources/qi-2022-b.md) — §4, Figs. 2–4, 15 (a priori correlations and coefficient check); §5–6, Tables 2–4 (a posteriori LES).
- [Tonicello et al. (2022)](/sources/tonicello-2022.md) — §4.2, Fig. 19, Tables 4–6 (averaged and filtered a priori budgets); §5–6.
- [Cherroud et al. (2022)](/sources/cherroud-2022.md) — §3–4, Eqs. 29–32, Table 2 (a posteriori cross-validation); §4.2, Fig. 7.
- [Brenner et al. (2022)](/sources/brenner-2022.md) — §3.5, Fig. 13 (mean velocity improved, stress–strain alignment not).
- [Svärd (2022)](/sources/svard-2022.md) — §1, §6 (filtering "a priori" against "a posteriori", in passing).
- [Shan et al. (2023)](/sources/shan-2023.md) — §III.D–E, Figs. 12–13 (a priori scores for hyperparameters only; data mix chosen a posteriori).
- [Hausmann et al. (2022)](/sources/hausmann-2022.md) — §IV (enrichment assessed only in running LES, in passing).
- [Wang et al. (2022)](/sources/wang-2022-j.md) — Eqs. 9–10, Tables I–II (a priori metrics and correlations); §IV–V, Figs. 2–16, Table V (a posteriori in isotropic turbulence and a temporal mixing layer).
- [Zhang et al. (2022b)](/sources/zhang-2022-f.md) — Eqs. 35–36, Tables I–II, Figs. 1–3 (a priori); §IV B, Figs. 5–23 (a posteriori).
- [Zhang et al. (2022d)](/sources/zhang-2022-h.md) — §I; Eqs. 37–38, Tables IV–V, Figs. 1–2 (a priori); §IV B, Figs. 3–18; §V.
- [Ihme et al. (2022)](/sources/ihme-2022.md) — §4.1.4 (a priori success, a posteriori instability of learned reacting-flow closures); §6.
- [Cao et al. (2022b)](/sources/cao-2022-c.md) — §IV B, Eqs. 17–18, Table I, Figs. 5–6 (a priori production); §IV C, Eqs. 20–22, Table II (a posteriori total subgrid dissipation); §V.
- [Xu et al. (2023)](/sources/xu-2023.md) — §2.2, Eqs. 2.32–2.34, Figs. 1–3 (filter, plane-wise correlation and relative error); §3.1–3.2, Figs. 4, 8, 10, 12 (a priori ranking); §4, Figs. 13–31 (a posteriori); §4.1 (MDNA unstable and costly).
- [Diez Sanhueza et al. (2023)](/sources/sanhueza-2023.md) — §3.2–3.3, Fig. 3(b) (correction inserted in the solver); §5, Table 3 (a posteriori K-fold errors).
- [Kumar et al. (2023)](/sources/kumar-2023.md) — §2.1–2.2, §3.6, §4 (training data generated a priori, a priori validation of the representative species, a posteriori coupled principal-component DNS).
- [Mays et al. (2023)](/sources/mays-2023.md) — §3.2.2, Fig. 13 ($r_K$ as an a priori resolution measure, realised energy ratio a posteriori).
