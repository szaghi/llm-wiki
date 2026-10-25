---
type: Definition
title: "A priori and a posteriori testing"
description: "A priori testing evaluates or trains a closure on filtered or averaged reference data outside the solver; a posteriori testing runs it inside the solver. The sources show that a priori agreement neither guarantees nor is required for a posteriori accuracy, and name the mechanisms."
status: established
aliases: [a priori test, a posteriori test, offline and online evaluation, a-priori training, a-posteriori training]
tags: [data-driven, sgs-model, machine-learning, les, rans]
timestamp: 2026-10-25T13:40:00Z
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
al. (2023) and Domingo & Vervisch (2023). The words carry three further
meanings that must be kept apart:

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
3. **Balance between model terms.** Exact inputs do not repair a model
   whose other terms were tuned to its own variables. As recalled by
   Duraisamy (2021, §IV.A), using exact DNS or LES $k$ and $\varepsilon$ in
   the eddy viscosity of one- and two-equation models did not improve
   predictions (Raiesi et al.), and substituting DNS Reynolds stresses did
   not give satisfactory velocity fields (Thompson et al.). Duraisamy et
   al. (2019, §6) recall the same Thompson et al. result, with Poroseva et
   al., and attribute it partly to ill-conditioning of the RANS equations
   (Wu et al.).
4. **Discretization error.** In LES the discrete operator adds a
   solution-dependent term that the a priori analysis of the continuous
   filtered equations does not contain. Beck & Kurz (2023, §I) state that
   this term "is at the heart of the discrepancy between a priori and a
   posteriori closure model performance"; see
   [discretization-consistent closure](/definitions/discretization-consistent-closure.md).
   Agdestein & Sanderse (2025, App. F) compute the continuous and the
   discrete convective commutator errors of the 2D Taylor–Green vortex:
   they have the same spatial form but different coefficients.

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
