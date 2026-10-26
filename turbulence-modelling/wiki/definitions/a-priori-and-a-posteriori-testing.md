---
type: Definition
title: "A priori and a posteriori testing"
description: "A priori testing evaluates or trains a closure on filtered or averaged reference data outside the solver; a posteriori testing runs it inside the solver. The sources show that a priori agreement neither guarantees nor is required for a posteriori accuracy, and name the mechanisms."
status: established
aliases: [a priori test, a posteriori test, offline and online evaluation, a-priori training, a-posteriori training]
tags: [data-driven, sgs-model, machine-learning, les, rans]
timestamp: 2026-10-25T20:39:00Z
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
adds its own error to the closure. Every source of this bundle that uses
the pair reports cases in which the two verdicts disagree.

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
[Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) (filtered-DNS
comparison against LES runs), [Helm & Martín (2022)](/sources/helm-2022.md),
[Kim et al. (2022)](/sources/kim-2022.md) and
[McConkey et al. (2022)](/sources/mcconkey-2022.md) use the pair in the
same sense. For McConkey et al. (§IV), a priori compares the network
outputs with the DNS labels before injection; a posteriori evaluates the
RANS solution after it has converged around the injected fields. The
combined anisotropy is available only a posteriori, because its linear part
evolves with the solution. The words carry
four further meanings that must be kept apart:

- **Training rather than testing.** Duraisamy (2021, §IV) and Agdestein &
  Sanderse (2025, §4.3) speak of *a priori training* (the loss compares the
  model with reference data outside the solver) and *a posteriori training*
  (the loss is evaluated on solver output); the latter is
  [model-consistent training](/methods/model-consistent-training.md).
  Agdestein & Sanderse note the double use themselves: "a-priori" names
  training in their §4.3 and pre-LES analysis in their §5.1.
- **"On-line" for a posteriori.** Duraisamy (2021, §IV.A) calls in-solver
  use "on-line" prediction and out-of-solver use "offline".
- **Not used in the LES sense.** Duraisamy et al. (2019, §5.3) write
  "a posteriori corrections" for corrections applied to an existing RANS
  model; the review does not use the pair for testing, though its argument
  on training and prediction environments (§5.4, §6) is the same one.
- **Error estimation in numerical analysis.** In
  [mesh adaptation](/methods/mesh-adaptation.md) the pair names the kind of
  discretization-error estimate, not a closure test.
  [Alauzet et al. (2022)](/sources/alauzet-2022.md) (§6.2) drive adaptation
  with an "a priori" goal-oriented estimate (an adjoint-weighted bound on
  interpolation errors); [Basile et al. (2023)](/sources/basile-2023.md)
  (§3.1) with an "a posteriori error estimator" computed from the
  solution's modal content and inter-element jumps.

For wall models, a priori means that the matching data at $h_{\mathrm{wm}}$
are taken from DNS and the model is run offline; a posteriori means the
model is coupled to the WMLES (Griffin et al. 2023, §§3–4; Vadrot et al.
2023b, §IV B).

## Typical a priori metrics

- **Component correlations.** Agrawal et al. (2022, §V, Eq. 14) average,
  over the six independent components, the correlation coefficient between
  model and exact SGS stresses, and define a dissipation correlation by
  contracting both with $\bar S_{ij}$. They state that such correlations do
  not measure alignment between the model and exact tensors. The filtered
  DNS uses a discretely commutative filter with three vanishing moments of
  width three grid spacings (channel at $Re_\tau=395$ and 2000); widths of
  two to four spacings change the trends little ("not shown").
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
- **Wall-stress ratio.** Vadrot et al. (2023b, §IV B, Fig. 12) feed a
  law-of-the-wall profile to machine-learning wall models and plot the
  ratio of the predicted $\tau_w$ to the law-of-the-wall value.

## Evidence that the two verdicts disagree

**A priori success is not sufficient.**

- Agrawal et al. (2022, §V) find that the Bardina
  [scale-similarity model](/methods/scale-similarity-model.md) has much
  better a priori tensor correlations than their
  [dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md),
  yet is under-dissipative a posteriori and needs added Smagorinsky
  dissipation.
- As recalled by Vadrot et al. (2023b, §I), Zhou et al. (2021) reported
  good a priori but poor a posteriori results for a neural-network wall
  model on periodic hills. In their own tests the re-trained version
  (ZYZY22) is accurate a priori at every $Re_\tau$ except 180 (§IV B,
  Fig. 12), yet a posteriori it gives a log law with $\kappa=0.32$ (§III A,
  Eq. 9); the authors trace the error to the LES side (§V) while also
  writing that "it is not clear to the authors why" (§IV B).
- As recalled by Duraisamy (2021, §IV.B, Fig. 2, from Sirignano, MacArt &
  Freund), an a priori-trained SGS closure overpredicts the resolved
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
  instability" a posteriori; as recalled there from the author's earlier
  work, the similarity estimate of $k_{\mathrm{sgs}}$ did not always work a
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
following the argument they recall from Baggett et al. that HIT needs only
the right dissipation (§I–II). This is the converse of Vela-Martín's
reading above: for Prakash et al. a priori stress correlation is
predictive where dissipation is held equal.

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
structure, not dissipation. By contrast, as Kim et al. recall, supervised
networks fed with local velocity gradients (Park & Choi 2021) reach a
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
The argument has the structure of Vela-Martín's gauge argument above: a
stress error with zero divergence leaves the mean equations unchanged; the
parallel is not drawn by either source, which do not cite each other
*(compiler check, not in the sources)*.

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

**An a priori advantage that shows only in one flow region.** As recalled
by Helm & Martín (2022, Sec. II, Sec. IV F), the a priori study of Martín
et al. (2000) in compressible isotropic turbulence found better stress and
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
   (recalled from their ref. 22), compounding errors are expected to hurt
   more in wall-modelled LES. They recall a posteriori studies that exposed
   ill-conditioning of data-driven SGS models. Kim et al. (2022, §III C)
   make the same point for SGS models: their training succeeds "through the
   online learning process in which the temporal reaction of the SGS model
   in the actual LES is considered".
3. **Balance between model terms.** Exact inputs do not repair a model
   whose other terms were tuned to its own variables. As recalled by
   Duraisamy (2021, §IV.A), using exact DNS or LES $k$ and $\varepsilon$ in
   the eddy viscosity of one- and two-equation models did not improve
   predictions (Raiesi et al.), and substituting DNS Reynolds stresses did
   not give satisfactory velocity fields (Thompson et al.). Duraisamy et
   al. (2019, §6) recall the same Thompson et al. result, with Poroseva et
   al., and attribute it partly to ill-conditioning of the RANS equations
   (Wu et al.). McConkey et al. (2022, §II B–C, Figs. 4–6) quantify how the
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

## Testbeds that allow both tests

Domingo & Vervisch (2023, §3.1) describe a DNS box nested inside a
well-resolved LES of a premixed Bunsen burner. Coarsening the DNS zone to
LES filter widths of 170–640 µm gives a posteriori tests on the same
configuration that provides the a priori data (Fig. 6). On this database,
CNN closures for the filtered progress-variable source reach about 1%
maximum a priori error on the trained filter sizes and 16% on an untrained
one (Fig. 9). See
[direct numerical simulation](/definitions/direct-numerical-simulation.md).

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

**Discretization-aware a priori data.** As recalled by Basile et al.
(2023, §3.2, §4.2.3), Chapelier and co-workers set an under-resolution
threshold of a DG smoothness indicator a priori from DNS of the
Taylor–Green vortex at $Re=5000$, finding values close to the $-5/3$
inertial slope, and Beck et al. projected filtered DNS onto a DG grid a
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
  with a supervised model is recalled from another study (Park & Choi
  2021), not rerun with the same solver.
- Seyedi & Zayernouri (2022) quote no correlation values; they are shown
  only in Figs. 4 and 7. Their a posteriori LES start from filtered DNS,
  and the authors note that DNS and LES "have not been initiated with the
  same initial conditions", hence the comparison with filtered DNS (§IV).
- The conditioning comparison of McConkey et al. (2022) is confounded, as
  the authors state: the fully explicit injection needed first-order
  convection schemes (§II C).

# Citations

- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §IV.A (three mechanisms, "neither necessary nor sufficient", Fig. 1), §IV.B (Fig. 2, recalled from Sirignano et al.).
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
- [Basile et al. (2023)](/sources/basile-2023.md) — HAL accepted manuscript, §3.1 (a posteriori error estimator), §3.2, §4.2.3 (a priori DG studies recalled).
- [Alauzet et al. (2022)](/sources/alauzet-2022.md) — §6.2 (a priori goal-oriented error estimate).
- [Kim et al. (2022)](/sources/kim-2022.md) — arXiv v2: §III C (training in the LES, a posteriori results, supervised model recalled), §III E, Eqs. 27–28, Table IV (alignment and correlation metrics).
- [McConkey et al. (2022)](/sources/mcconkey-2022.md) — arXiv v1: §II A–C, Eq. 6, Figs. 4–6 (conditioning test); §IV A, Figs. 11–14 (a priori errors); §IV B, Figs. 20–21; §V.
- [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) — arXiv v3: §III.1–III.2, Figs. 4–7 (a priori); §IV, Figs. 8–10 (a posteriori).
- [Helm & Martín (2022)](/sources/helm-2022.md) — Sec. II, Sec. IV F, Figs. 30–33, Sec. V; abstract (a priori study recalled, a posteriori ablation).
- [Cato et al. (2023)](/sources/cato-2023.md) — HAL author manuscript: §V C, Figs. 16–19 (mean flow without the right stresses), Eq. 18.
