---
type: Method
title: "Super-resolution subgrid-scale models"
description: "An LES closure that reconstructs a fine-grid field from the coarse LES field with a neural network and computes the subgrid stress and scalar flux from the reconstruction; a priori generalization in premixed flames hinges on the filter-to-Kolmogorov ratio, and for very coarse wall-bounded LES an unsupervised CycleGAN first maps the LES field to filtered-DNS quality."
status: established
aliases: [super-resolution SGS model, super-resolution-based subgrid scale model, unsupervised-supervised pipeline, CycleGAN SGS model, GAN super-resolution closure, vLES]
tags: [neural-network, sgs-model, les, data-driven]
timestamp: 2026-10-28T17:41:00Z
---

# Super-resolution subgrid-scale models

A **super-resolution SGS model** does not predict the subgrid stress
directly. A neural network reconstructs, from the resolved LES velocity, a
velocity field $u^{\mathrm{SR}}_i$ (page-local) on a grid $m$ times finer
in each filtered direction ($m$ page-local, the super-resolution factor),
and the stress is computed from that reconstruction with the registry
definition, the overbar being the box filter over the $m\times m$ fine
points inside one LES cell:

$$\tau_{ij}=\overline{u^{\mathrm{SR}}_iu^{\mathrm{SR}}_j}-\bar u^{\mathrm{SR}}_i\,\bar u^{\mathrm{SR}}_j=\overline{u^*_iu^*_j},\qquad u^*_i=u^{\mathrm{SR}}_i-\bar u^{\mathrm{SR}}_i .$$

[Maejima & Kawai (2025)](/sources/maejima-2025.md) (§3.2, Fig. 4) print
the stress-sign form $\tau_{ij,SGS}\equiv-\widehat{u^*_iu^*_j}$, with the hat
for the box filter; the expression above is its registry translation
(positive-trace convention). It is symmetric, six components per point,
not made deviatoric, and fed to the momentum equation of their
compressible LES; the printed definition carries no density factor. The
flow is at bulk Mach number about 0.1, and the SGS terms of the energy
equation are neglected (§2.1). Maejima & Kawai (2025, §1) cite Bode et al.
(2021), who modelled the SGS stresses as the difference between filtered
DNS data and a reconstructed DNS field; [Ruggeri et al. (2022)](/sources/ruggeri-2022.md)
(§III) cite the same paper as a generative adversarial network with
physics-informed losses for the subgrid of reactive LES that "gives good
results in a priori and a posteriori tests", without details. See
[neural-network SGS models](/methods/neural-network-sgs-model.md) for
closures that output the stress itself.

## The physics-informed super-resolution GAN in reacting LES (as reviewed by Ihme et al. 2022)

[Ihme et al. (2022)](/sources/ihme-2022.md) (§4.1.4, Fig. 32) review the
same line of work, the physics-informed enhanced super-resolution GAN
(PIESRGAN) of Bode et al., as their example of a knowledge-guided remedy
for the a posteriori instability of learned subgrid closures. As they
describe it, the generator reconstructs the subfilter field from which the
subgrid stresses follow; its loss combines an adversarial term, an
accuracy term and a physics-informed term that penalizes violation of
continuity; the generator uses the residual-in-residual dense blocks of
the enhanced super-resolution GAN (ESRGAN); and the model was used both a
priori and a posteriori in LES of an $n$-dodecane spray flame. They also
cite a Wasserstein GAN that outperformed a CNN in capturing small-scale
structures of scalar transport, set against a fully connected network that
beat a variational autoencoder for joint scalar PDFs, and read the two as
"mixed findings" that call for a common benchmark dataset (§4.1.4). In
§5.4 they state that studies in turbulence modelling, citing the
PIESRGAN work and the joint-PDF comparison ([279, 570]), "indicate
improvements in generalizability, when using generative learning methods
instead of supervised learning"; their own §4.1.4 account of the
joint-PDF comparison reports that the variational autoencoder did *not*
beat the fully connected network. The review gives no numbers of its own for these
models (see
[physics-informed neural networks](/methods/physics-informed-neural-network.md)
for their classification of knowledge-guided losses).

[Fang et al. (2026)](/sources/fang-2026.md) (§2.4), a later review,
list GAN super-resolution subgrid models of LES that recover the filtered
small scales, citing a parallel implementation and performance study by
Nista et al. (2025, their ref. [83]) and the premixed-flame
generalization study of [Nista et al. (2023)](/sources/nista-2023.md)
(their ref. [108]; below); the review's Fig. 5 (§2.2) sketches a convolutional
network that outputs both an enhanced-resolution field and a predicted
subgrid stress. The review prints no result of these models.

[Posch et al. (2025)](/sources/posch-2025.md) (§6.4.2), a review of
turbulent combustion models for engine CFD, report the same three works
as evidence for machine-learned subgrid closures in reacting flow. Bode
et al. reconstructed the subgrid mixture-fraction flux and subgrid
Reynolds stresses with a GAN, with physics-informed losses based on the
continuity equation, and achieved "good results" in a benchmark spray
case; the review records their caution that reactive scalars are harder
because fast-chemistry source terms depend on the smallest scales, and
their later reproduction of DNS data of an engine-like flame kernel on a
much coarser grid. Of Nista et al. (the review's ref. [481], the work on
this page's next section) it reports good extrapolation across benchmark
flames in Reynolds and Karlovitz numbers and OH mass fraction, with the
authors' warning not to change the filter-to-Kolmogorov ratio between
training and testing. The review's assessment of the whole class is that
these models "have been mostly developed and tested on benchmark flame
simulation cases" and that their transfer to engine combustion "is not
straight forward", data-driven models lacking extrapolation so that the
training data must cover the engine's temperature and pressure range
(§6.4.1–6.4.2). It prints no number of its own.

## Generalization of a super-resolution GAN in premixed flames (Nista et al. 2023)

[Nista et al. (2023)](/sources/nista-2023.md) apply the same idea to the
subfilter terms of the Favre-filtered reacting equations and ask how far
such a closure generalizes outside its training conditions. All tests are
a priori; a posteriori LES is named as future work (§4.4).

**Closure (§1, §3.1, Eqs. 1–5).** A generator maps the box-filtered DNS
fields of $u$, $v$, $w$ and $T$ to a field eight times finer in each
direction, and the unresolved terms are evaluated from the reconstruction
"directly at the DNS level": the Favre stress per unit mass
$\widetilde{u_iu_j}-\tilde u_i\tilde u_j$ (the registry's compressible
$\tau_{ij}$ divided by $\bar\rho$; full tensor, not deviatoric) and the
subfilter temperature flux $\widetilde{u_iT}-\tilde u_i\tilde T$, "the same
argument" holding for any scalar. The generator is a 3-D variant of ESRGAN
and of the physics-informed PIESRGAN of Bode et al. (as cited): 3-D
convolutions with leaky ReLU, one residual-in-residual dense block (ESRGAN
uses 23), three upsampling layers of nearest-neighbour doubling plus a
convolution, 64 filter maps per layer, about 25 million trainable
parameters; the discriminator is that of PIESRGAN. The generator loss is
$\mathcal L=\beta_1\mathcal L_{\mathrm{pixel}}+\beta_2\mathcal L_{\mathrm{grad}}+\beta_3\mathcal L_{\mathrm{RaGAN}}$
(page-local names and weights): mean squared errors of the field and of
its gradient plus a relativistic-average adversarial term, with
$(\beta_1,\beta_2,\beta_3)=(0.89,0.06,0.00006)$ taken from the authors'
earlier work (Eq. 4). The generator is pre-trained on the pixel loss alone
to avoid convergence failure of the adversarial training.

**Training (§3.2).** Only one DNS of a lean methane/air slot-jet flame
(R2K1: jet Reynolds number 5600, Karlovitz number 23), box filter of
width $\Delta=8h$ ($h$ the DNS spacing), 73,100 random sub-boxes of $64^3$
(fine) and $8^3$ (filtered) points with flips and rotations, global
min–max normalization, the last 10% of the snapshots held out. Training
on four nodes with one NVIDIA V100 each took 28 h instead of about 5 days.

**Results (§4, Figs. 2–8).**

- *In sample.* The joint PDF of modelled against DNS $\tau_{12}$ aligns
  with the diagonal, where the dynamic Smagorinsky model "exhibits a
  relatively low correlation"; the temperature flux is narrow along the
  diagonal but less accurate for negative values (§4, Fig. 2). The
  authors concede that the eddy-viscosity baseline "might be not optimal"
  for such a comparison.
- *Reynolds number.* At half and four times the training jet Reynolds
  number the stress and flux joint PDFs barely change (slightly worse at
  the higher one); at the lower one the root-mean-square error of the
  super-resolved field is "roughly 75% less" than that of the filtered
  input, though its textures still differ from DNS (§4.1, Figs. 3–5).
- *Karlovitz number.* At about ten times the training Karlovitz number
  (240) the stress joint PDF stays on the diagonal (§4.2, Figs. 4c, 5c).
- *Fuel.* On a hydrogen planar jet flame (jet Reynolds number 5000,
  Karlovitz number 43.5) with the training filter width,
  $\Delta/\eta\approx14.88$, the network over-predicts the jet velocity
  and the large velocity gradients; with a filter of $4h$
  ($\Delta/\eta\approx6.6$ as printed) the velocity-gradient PDF nearly
  matches DNS, slightly under-predicting the larger structures (§4.2,
  Figs. 6–7).
- *Untrained scalar.* Applied to the OH mass fraction, never seen in
  training, the network is poor where OH is nearly uniform (non-physical
  oscillations) and close to DNS at the jet/coflow flame boundary, where
  the gradients are largest (§4.3, Fig. 8).

**Generalization criterion (§4.1–4.2, §4.4, §5).** Across the
Reynolds-number series the ratios $\Delta/\eta\approx8$ and
$\Delta/\delta_{\mathrm L}\approx1.45$ ($\delta_{\mathrm L}$ the thermal
flame thickness, page-local) are both kept; at the high Karlovitz number
only $\Delta/\eta$ is kept and the closure still works; on the hydrogen
flame $\Delta/\eta$ differs and it fails. The authors conclude that
"the ratio $\Delta/\eta$ needs to be conserved between training and
application of the network", while $\Delta/\delta_{\mathrm L}$ "does not
seem" to be fundamental, and that the restriction to one $\Delta/\eta$
might be relaxed by training on a range of filter widths, since the LES
to DNS grid ratio is fixed in the architecture. Lower Karlovitz numbers,
where the flame thickness might matter, and other fuels are not covered
(§5). The inputs are filtered DNS, not solver
output, unlike the very coarse channel LES below (see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

## Why very coarse LES needs an unsupervised step

Maejima & Kawai (2025) target **very coarse-grid LES (vLES)**: grids on
which even the energy-containing near-wall eddies are not resolved, so the
resolved field is itself non-physical and its statistics differ from
filtered DNS, "fDNS $\neq$ vLES" (§1, §3.1). The authors draw two
consequences:

- **Supervised super-resolution is trained on the wrong input.**
  Supervised models are trained on pairs (filtered DNS, DNS) and assume the
  LES field looks like filtered DNS; on vLES that assumption fails.
  Paired (vLES, DNS) instantaneous data cannot exist, because vLES and DNS
  are separate simulations (§1). The alternative of degrading DNS
  artificially to look like vLES is rejected because coarse-grid errors are
  not understood well enough to build the degradation (§3.1).
- **Pointwise inputs cannot see the defect.** Pointwise models, such as
  velocity-gradient inputs, "may not be able to appropriately distinguish
  the non-physical structures", while convolutional networks see their
  spatial extent (§7).

## The unsupervised–supervised pipeline (Maejima & Kawai 2025)

The model is a composition of two generators acting on wall-parallel
planes of $(u,v,w)$ (§3, Fig. 3, Eq. 3.1):

$$u^{\mathrm{SR}}=G_{\mathrm{SR}}\big(G_{\mathrm{vLES}\to\mathrm{fDNS}}(\bar u)\big).$$

1. **$G_{\mathrm{vLES}\to\mathrm{fDNS}}$, unsupervised.** The generator of a
   CycleGAN trained on *unpaired* vLES and filtered-DNS planes
   ("style transfer"): two generators map each domain to the other, two
   critics judge each domain, and a cycle-consistency loss with weight
   $\lambda_{\mathrm{cyc}}=1$ requires a round trip to return the input
   (Eqs. 2.18–2.22). Both critics use the Wasserstein loss with a gradient
   penalty of weight $\lambda_{\mathrm{GP}}=10$ (page-local weights). The
   authors found $\lambda_{\mathrm{cyc}}=1$ better than the recommended 10
   (§2.2.2).
2. **$G_{\mathrm{SR}}$, supervised.** A conditional Wasserstein GAN with
   gradient penalty trained on pairs of box-filtered and original DNS
   planes; it upsamples by $m=8$ ($32\times32$ to $256\times256$ per patch;
   Eqs. 2.16–2.17, Table 4). A GAN is preferred to an $L_2$-loss CNN for
   small-scale structures, as found in preliminary tests (not shown).

A single CycleGAN mapping vLES directly to DNS "did not converge
properly"; the authors attribute this to the different numbers of grid
points of the two data sets and split the task in two (§3.1, not shown).
The comparator is a "typical supervised model": $G_{\mathrm{SR}}$ applied
directly to vLES (Fig. 15b).

**Networks and data (§4, App. A, Tables 3–4).** All networks are 2-D and
fully convolutional ($3\times3$ kernels, LeakyReLU, average-pooling and
nearest-neighbour resampling); each wall-parallel plane is processed
independently, because wall-normal convolutions on stretched grids would
change meaning between Reynolds numbers, and no wall-normal
discontinuities appear (§5.1.1). Inputs and outputs are normalized by the
input mean and standard deviation at each wall distance; since the input
standard deviation vanishes at the wall, the output is multiplied by zero
there and no-slip holds exactly. Training uses 1600 snapshots per plane
and wall at eight heights ($y^+\approx5$, 15, 30, 100 and $y/\delta=0.25$
to 1), patches of $2.304\delta\times1.152\delta$, Adam at $10^{-5}$,
batch 16.

**Clipping (§3.2, Eq. 3.2; App. C).** With $\nu_{\mathrm{eff}}$ (registry §11),
the effective viscosity of the stress projected on the resolved strain,
and a floor $\nu_{\mathrm{clip}}\le0$, the stress is modified only where
the local backscatter is extreme:

$$\nu_{\mathrm{eff}}=-\frac{\tau_{ij}\,\partial_j\bar u_i}{2\bar S^d_{ij}\,\partial_j\bar u_i},\qquad \tau^{\mathrm{clip}}_{ij}=\begin{cases}\tau_{ij}, & \nu_{\mathrm{eff}}>\nu_{\mathrm{clip}},\\ \tau_{ij}+2(\nu_{\mathrm{eff}}-\nu_{\mathrm{clip}})\,\bar S^d_{ij}, & \text{otherwise}.\end{cases}$$

The clipped stress has effective viscosity exactly $\nu_{\mathrm{clip}}$,
and, since $\bar S^d_{ij}\partial_j\bar u_i=\bar S^d_{ij}\bar S^d_{ij}$ and
$\tau_{ij}\partial_j\bar u_i=\tau_{ij}\bar S_{ij}$,
$\nu_{\mathrm{eff}}=\Pi/\lvert\bar S^d\rvert^2$ with the registry flux $\Pi$
(the stress carries no density factor, as on the
[gradient model](/methods/gradient-model.md) page): the same projection as
Abe's equivalent eddy viscosity on
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
*(compiler check, not in the sources)*. The run uses
$\nu_{\mathrm{clip}}/\bar\nu_w\approx-2$ (page-local $\bar\nu_w$: mean kinematic viscosity at the wall), so backscatter is weakened, not
removed; this contrasts with the clipping of structural models that sets
backscatter to zero (see [gradient model](/methods/gradient-model.md) and
[energy backscatter](/definitions/energy-backscatter.md)). The authors
justify the clipping by the criterion they cite from Matsumoto, Inubushi
& Goto (2024): machine-learning turbulence models cannot run stably on
grids with $k_{\max}\eta<0.2$; their vLES has $k_{z,\max}\eta\approx0.13$
(App. C).

## Test case: channel flow at $Re_\tau\approx1000$ and 2000

Compressible [channel flow](/benchmarks/turbulent-channel-flow.md) at
bulk Mach number about 0.1, driven by a constant body force set from
Dean's correlation so that $\tau_w$ and $Re_\tau$, hence the near-wall
resolution in wall units, are fixed across runs (§4.1, Eq. 4.1). The
solver is second-order and
[kinetic-energy- and entropy-preserving](/properties/kinetic-energy-preservation.md),
non-dissipative, "so that SGS dissipation is not contaminated by
numerical dissipation" (§4.1; see
[numerical dissipation](/properties/numerical-dissipation.md)); the
conventional SGS model is the selective mixed-scale model of Lenormand et
al. (2000), whose formula is not printed. Domain $6\pi\delta\times2\delta\times2\pi\delta$:

| Case | $\Delta x^+$ | $\Delta z^+$ | $\Delta y^+$ | $N_x\times N_y\times N_z$ |
|---|---|---|---|---|
| DNS, $Re_\tau\approx1000$ | 9.0 | 4.5 | 0.5–6.0 | $2160\times669\times1440$ |
| LESx4 | 36 | 18 | 0.8–6.0 | $540\times600\times360$ |
| LESx8 (vLES) | 72 | 36 | 0.8–16 | $270\times285\times180$ |
| DNS, $Re_\tau\approx2000$ | 9.0 | 4.5 | 0.5–6.0 | $4320\times819\times2880$ |
| LESx8, $Re_\tau\approx2000$ | 72 | 36 | 0.8–30 | $540\times335\times360$ |

(Tables 1–2.) LESx4 with the conventional model reproduces DNS; LESx8
over-predicts the mean velocity. LESx8 places two to three points across
a near-wall streak spacing $\lambda_z^+\approx100$, LESx4 five to six
(§4.1, App. B).

## Results (Maejima & Kawai 2025)

**A priori, on precomputed vLES fields (§5).**

- The CycleGAN output has filtered-DNS spectra and Reynolds stresses while
  keeping the large structures of its input; $\langle u'u'\rangle$ is
  slightly low at $0.1\lesssim y/\delta\lesssim0.7$ (§5.1, Figs. 6–9).
- The supervised stage restores high wavenumbers and also corrects
  resolved-wavenumber errors, most visibly in $v$; residual errors at the
  highest wavenumbers lie three to four orders of magnitude below the
  energetic eddies, and spectral spikes are the chequerboard artefact of
  nearest-neighbour upsampling (§5.2, Figs. 12–14).
- The full pipeline reproduces the DNS mean velocity, resolved Reynolds
  stresses and SGS stresses from vLES input and restores outer-layer
  energy at $2\lesssim k_z\delta\lesssim10$ missing in the input; the
  typical supervised model keeps the vLES mean velocity and over-predicts
  the streamwise and shear Reynolds and SGS stresses (§5.3, Figs. 18–21).

**A posteriori in vLES (§6–7).**

- At $Re_\tau\approx1000$ the pipeline gives a mean velocity in good
  agreement with DNS and the near-wall rise of the total Reynolds shear
  stress ($3\lesssim y^+\lesssim30$); under constant body-force driving
  the bulk flow rate is over-predicted by 10%, against 23% with the
  selective mixed-scale model; the typical supervised model is only
  slightly better than the conventional one (§6.1, Fig. 22).
- Near the wall ($3\lesssim y^+\lesssim10$) the pipeline's SGS shear
  stress exceeds the resolved one, as in filtered DNS; the near-wall
  wall-normal and spanwise normal stresses are over-predicted, which the
  authors accept as non-physical (§6.1, Figs. 22–23).
- Trained at $Re_\tau\approx1000$ only, the pipeline at $Re_\tau\approx2000$
  on the same wall-unit grid gives mean velocity and near-wall shear
  stress in good agreement with DNS, where the conventional model deviates
  significantly (§7, Figs. 28–29).
- On the LESx4 grid the pipeline does not degrade the resolved eddies and
  is closer to DNS than the conventional model (App. B, Figs. 30–36).

**Why it works: backscatter and pressure redistribution (§6.2).** In the
budget of the resolved Reynolds stresses, the SGS dissipation term of the
spanwise normal stress is positive (backscatter) with the pipeline model
below $y^+\approx100$ and negative with the conventional model; the
wall-normal SGS term is negligible for both (Fig. 25). Pressure–strain
then transfers energy from $w$ to $v$ at $20\lesssim y^+\lesssim100$. In
the spanwise spectral budget at $y^+\approx15$ the DNS redistribution
sits at $\lambda_z^+\lesssim60$, below the vLES Nyquist wavelength
$2\Delta z^+\approx72$; with the pipeline it occurs at resolved
wavelengths $130\lesssim\lambda_z^+\lesssim210$ ($3.5\Delta z$ to
$5.8\Delta z$, peak near $\lambda_z^+\approx160$), which the authors call
"compensation for the unresolved turbulence dynamics" (§6.2.2–6.2.3, Fig.
27). The chain they propose: spanwise SGS backscatter, more near-wall
$\langle w'w'\rangle$, redistribution to $\langle v'v'\rangle$, more
near-wall Reynolds shear stress, correct mean velocity through the total
shear-stress balance (§6.1, §6.2.3, §8). They state it is consistent with
DNS analyses of spanwise near-wall backscatter (Hamba 2019;
[Inagaki & Kobayashi 2023](/sources/inagaki-2023.md)).

**Clipping sensitivity (App. C, Fig. 37).** Lowering the floor
$\nu_{\mathrm{clip}}/\bar\nu_w$ from 0 to about $-1$ and $-2$ moves the mean
velocity toward DNS; about $-3$ is unstable; even $\nu_{\mathrm{clip}}=0$,
no net local backscatter, beats the conventional model.

## Qualifications

- **One flow, one solver.** All evidence is plane channel flow with one
  compressible finite-difference code, two Reynolds numbers and two grids.
  Because the networks act in computational coordinates, the wall-unit
  resolution must be similar in training and use, which limits transfer
  to other resolutions, aspect ratios and unstructured grids; the authors
  call this a limitation of CNNs in general (§7).
- **Accuracy claims are on mean velocity and shear stress.** The normal
  stresses near the wall are over-predicted (§6.1, Fig. 23).
- **Unshown preliminary tests** decide several choices (the two-stage
  split, $\lambda_{\mathrm{GP}}$, $\lambda_{\mathrm{cyc}}$, GAN against
  $L_2$ loss; §2.2, §3.1).
- **Printed slips (version of record).** In §6.2.2 the sentence on the
  blue regions of Fig. 26 repeats the signs given for the red regions,
  while the figure legend gives $\partial v'/\partial y<0$,
  $\partial w'/\partial z>0$. After Eq. 6.1 the viscous stress is written
  with $\partial u/\partial x$ for $\partial u/\partial y$. In §6.2.3 "$k_z^+\approx60$"
  is a wavelength, $\lambda_z^+\approx60$, as §6.2.2 shows. App. B.1 refers
  to §2.2.2 for results that are in §5.3. The reference list prints the
  same arXiv number for Kingma & Ba (2014) and Gulrajani et al. (2017).
  Ihme et al. (2022, §4.1.4) print "ERSGAN" for the network their
  ref. [580] titles "ESRGAN".
- **The filter ratios of Nista et al. (2023).** With the printed DNS
  spacing of 20 µm and $\Delta=8h$, the Reynolds-number series gives
  $\Delta/\eta$ from 6.4 to 8.9 (Table 1), which the paper summarizes as
  "≈8"; for the high-Karlovitz flame the printed $\delta_{\mathrm L}/h\approx15$
  and $\delta_{\mathrm L}=200$ µm give $\Delta/\delta_{\mathrm L}\approx0.53$,
  not the printed 0.062, while $\Delta/\eta\approx8.2$ agrees with the
  text; for the hydrogen flame, $\Delta/\eta\approx14.88$ at $8h$ implies
  about 7.4 at $4h$, against the printed 6.6 *(compiler check, not in the
  sources)*. The criterion's statement that $\Delta/\delta_{\mathrm L}$ is
  not fundamental rests on the high-Karlovitz value. The hydrogen flame's
  $\delta_{\mathrm L}$ is 435 µm in §2 and 444 µm in Table 1, and the
  mixture is called hydrogen/air and, in the same paragraph, a jet of
  hydrogen and oxygen. Eq. 1 prints the momentum equation with mismatched
  free indices, and §3.1 says "the $L_1$ norm is applied to each
  component" of a loss defined by mean squared errors. The evidence of
  the generalization study is joint PDFs, contours and one gradient PDF;
  no a posteriori test exists.
- **Notation (Maejima & Kawai 2025).** The paper's $S_{ij}$ carries no factor $\tfrac12$ (twice the
  deviatoric strain), its overbar is the LES filter in §2 and a Reynolds
  average in §6, and its hat is the box filter in §3 and a Fourier
  transform in §6; this page uses $\bar S^d_{ij}$, $\langle\cdot\rangle$ and
  the overbar as in the registry.

# Citations

- [Ruggeri et al. (2022)](/sources/ruggeri-2022.md) — §III (physics-informed GAN of Bode et al. cited, in passing).
- [Ihme et al. (2022)](/sources/ihme-2022.md) — §4.1.4, Fig. 32 (PIESRGAN reviewed: adversarial, accuracy and continuity losses, RRDB blocks, a priori and a posteriori spray-flame LES; generative against supervised findings); §5.4 (generalizability of generative methods).
- [Maejima & Kawai (2025)](/sources/maejima-2025.md) — §1 (fDNS against vLES, supervised super-resolution, Bode et al. cited); §2.1–2.2, Eqs. 2.1–2.22 (equations, cGAN, CycleGAN); §3, Eqs. 3.1–3.2, Figs. 3–4 (pipeline, stress extraction, clipping); §4, Tables 1–4, Eq. 4.1 (channel set-up, networks, data); §5, Figs. 6–21 (a priori); §6, Eqs. 6.1–6.15, Figs. 22–27 (a posteriori, budgets, mechanism); §7, Figs. 28–29 ($Re_\tau\approx2000$, CNN limits, pointwise inputs); §8; App. A–C, Figs. 30–37.
- [Posch et al. (2025)](/sources/posch-2025.md) — §6.4.1–6.4.2 (GAN super-resolution closures of Bode et al. and Nista et al., refs. [479]–[481], reviewed; transfer to engines).
- [Nista et al. (2023)](/sources/nista-2023.md) — §1, Eqs. 1–3, 5 (subfilter stress and temperature flux from the reconstruction); §3.1–3.2, Eq. 4, Fig. 1 (generator, loss, training); §4–4.3, Table 1, Figs. 2–8 (a priori generalization across Reynolds and Karlovitz numbers, fuel, OH); §4.4, §5 ($\Delta/\eta$ criterion, a posteriori deferred).
- [Fang et al. (2026)](/sources/fang-2026.md) — §2.2, Fig. 5; §2.4 (GAN super-resolution SGS models cited). Review, citation only.
