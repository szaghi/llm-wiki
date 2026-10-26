---
type: Method
title: "Super-resolution subgrid-scale models"
description: "An LES closure that reconstructs a fine-grid velocity field from the coarse LES field with a neural network and computes the subgrid stress by filtering products of the reconstructed sub-cell fluctuations; for very coarse wall-bounded LES an unsupervised CycleGAN first maps the LES field to filtered-DNS quality, with a clipping that keeps moderate backscatter."
status: established
aliases: [super-resolution SGS model, super-resolution-based subgrid scale model, unsupervised-supervised pipeline, CycleGAN SGS model, GAN super-resolution closure, vLES]
tags: [neural-network, sgs-model, les, machine-learning, data-driven]
timestamp: 2026-10-26T15:53:00Z
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
DNS data and a reconstructed DNS field. See
[neural-network SGS models](/methods/neural-network-sgs-model.md) for
closures that output the stress itself.

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

**Clipping (§3.2, Eq. 3.2; App. C).** With page-local $\nu_{\mathrm{eff}}$,
the effective viscosity of the stress projected on the resolved strain,
and a floor $\nu_{\mathrm{clip}}\le0$, the stress is modified only where
the local backscatter is extreme:

$$\nu_{\mathrm{eff}}=-\frac{\tau_{ij}\,\partial_j\bar u_i}{2\bar S^d_{ij}\,\partial_j\bar u_i},\qquad \tau^{\mathrm{clip}}_{ij}=\begin{cases}\tau_{ij}, & \nu_{\mathrm{eff}}>\nu_{\mathrm{clip}},\\ \tau_{ij}+2(\nu_{\mathrm{eff}}-\nu_{\mathrm{clip}})\,\bar S^d_{ij}, & \text{otherwise}.\end{cases}$$

The clipped stress has effective viscosity exactly $\nu_{\mathrm{clip}}$,
and $\nu_{\mathrm{eff}}$ (the stress carries no density factor, as on the
[gradient model](/methods/gradient-model.md) page) is the analogue of the
equivalent eddy viscosity $\Pi/\lvert\bar S\rvert^2$ used as an a priori
metric on [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
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
- **Notation.** The paper's $S_{ij}$ carries no factor $\tfrac12$ (twice the
  deviatoric strain), its overbar is the LES filter in §2 and a Reynolds
  average in §6, and its hat is the box filter in §3 and a Fourier
  transform in §6; this page uses $\bar S^d_{ij}$, $\langle\cdot\rangle$ and
  the overbar as in the registry.

# Citations

- [Maejima & Kawai (2025)](/sources/maejima-2025.md) — §1 (fDNS against vLES, supervised super-resolution, Bode et al. cited); §2.1–2.2, Eqs. 2.1–2.22 (equations, cGAN, CycleGAN); §3, Eqs. 3.1–3.2, Figs. 3–4 (pipeline, stress extraction, clipping); §4, Tables 1–4, Eq. 4.1 (channel set-up, networks, data); §5, Figs. 6–21 (a priori); §6, Eqs. 6.1–6.15, Figs. 22–27 (a posteriori, budgets, mechanism); §7, Figs. 28–29 ($Re_\tau\approx2000$, CNN limits, pointwise inputs); §8; App. A–C, Figs. 30–37.
