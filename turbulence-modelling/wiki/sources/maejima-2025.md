---
type: Source
title: "Maejima & Kawai (2025) — Unsupervised and supervised machine learning pipeline for super-resolution-based subgrid scale modelling in coarse-grid large-eddy simulations"
description: "Builds an SGS model for very coarse wall-bounded LES from a CycleGAN that maps unpaired coarse-LES fields to filtered-DNS quality and a conditional GAN that super-resolves them, extracting the stress from sub-cell fluctuations; in channel flow it corrects the mean velocity through spanwise backscatter and pressure redistribution."
resource: "doi:10.1017/jfm.2025.10211"
source_kind: paper
authors: [Maejima S., Kawai S.]
year: 2025
venue: "J. Fluid Mech. 1013:A28"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Journal_of_Fluid_Mechanics_Maejima_Unsupervised_and_supervised_machine_learning_pipeline_for_su.pdf"
tags: [les, sgs-model, neural-network, data-driven, backscatter, a-priori-a-posteriori]
timestamp: 2026-10-26T15:49:00Z
---

# Summary

Maejima & Kawai (2025) target very coarse-grid [LES](/definitions/large-eddy-simulation.md)
(vLES), in which even the energy-containing near-wall eddies are unresolved, so
that the resolved field is itself non-physical and its statistics differ from
filtered [DNS](/definitions/direct-numerical-simulation.md). Supervised
[neural-network SGS models](/methods/neural-network-sgs-model.md) trained on
filtered-DNS inputs then fail, and paired vLES/DNS instantaneous data cannot
exist. The paper proposes a two-stage [super-resolution SGS model](/methods/super-resolution-sgs-model.md).
An unsupervised CycleGAN, trained on unpaired vLES and filtered-DNS wall-parallel
planes, maps the vLES velocity to a filtered-DNS-quality field. A supervised
conditional GAN, trained on filtered and original DNS pairs, super-resolves it
eightfold. The SGS stress is the cell average of products of the reconstructed
sub-cell fluctuations, clipped so that the effective viscosity stays above a
negative floor; moderate [backscatter](/definitions/energy-backscatter.md) is
kept. This clipping is a variant of those discussed for structural models on
the [gradient model](/methods/gradient-model.md) page.

Tests use [turbulent channel flow](/benchmarks/turbulent-channel-flow.md) at
$Re_\tau\approx1000$, $M_b\approx0.1$, with a second-order
[kinetic-energy- and entropy-preserving](/properties/kinetic-energy-preservation.md)
central scheme chosen so that [numerical dissipation](/properties/numerical-dissipation.md)
does not contaminate the SGS dissipation. [A priori](/definitions/a-priori-and-a-posteriori-testing.md),
the pipeline reproduces DNS statistics from vLES input, while the conditional GAN
applied directly to vLES overpredicts the stresses. A posteriori, the pipeline
gives DNS-like mean velocity and shear stress at $Re_\tau\approx1000$ and at the
untrained $Re_\tau\approx2000$; the baseline selective mixed-scale model, in the
[scale-similarity and mixed](/methods/scale-similarity-model.md) family,
overpredicts the flow rate by 23% (pipeline 10%). Reynolds-stress budgets
attribute the gain to spanwise SGS backscatter, redistributed by pressure–strain
to the wall-normal component at resolved wavelengths. The introduction recalls
the [Smagorinsky](/methods/smagorinsky-model.md) and [dynamic](/methods/dynamic-procedure.md)
eddy-viscosity models, and the [grid-point requirements](/results/les-grid-point-requirements.md)
that motivate coarse LES.

# Version read

Version of record (J. Fluid Mech., Cambridge University Press, open access CC
BY 4.0; received 18 November 2024, revised 14 April 2025, accepted 17 April
2025), 51 pages (A28-1 to A28-51), all read; the equation pages were read
visually. Page 1 matches Crossref; no identity problem. Locators are the
journal's sections, equations, figures and tables.

# Key claims

Page-local symbols: vLES = LESx8, $(\Delta x^+,\Delta z^+)\approx(72,36)$;
LESx4 $\approx(36,18)$; $\nu_{\mathrm{eff}}$, $\nu_{\mathrm{clip}}$ the effective
SGS viscosity and its floor; $\bar\nu_w$ the mean wall viscosity (the
source writes $\mu$; ratios as printed);
$D^{\mathrm{sgs}}_{ij}$ and $D^{p}_{ij}$ the SGS-dissipation and
pressure-redistribution terms of the resolved Reynolds-stress budget; $k_z$,
$\lambda_z$ the spanwise wavenumber and wavelength.

1. On vLES grids the resolved flow deviates from filtered DNS, so supervised SGS or super-resolution models trained on filtered-DNS→DNS pairs are inappropriate for vLES, and paired vLES/DNS data are unobtainable; an unsupervised model is required (§1, §3.1). **Stated**, supported by **Shown** (§5.3)
2. LESx4 with the selective mixed-scale model reproduces DNS mean velocity and Reynolds stresses well; LESx8 overestimates the mean velocity and deviates in Reynolds stresses (§4.1, Fig. 5). **Shown**
3. LESx8 places two to three grid points per near-wall streak wavelength $\lambda_z^+\approx100$, LESx4 five to six (§4.1, App. B). **Stated**
4. A single CycleGAN trained directly vLES→DNS did not converge properly, attributed to the unbalanced grid-point counts of the two datasets; the task was split into vLES→filtered DNS (CycleGAN) and filtered DNS→DNS (conditional GAN) (§3.1). **Stated** (not shown)
5. The CycleGAN generator gives fields whose streamwise and spanwise spectra and mean and resolved Reynolds stresses agree with filtered DNS while keeping the large resolved structures of the input; a slight underprediction of $\langle u'u'\rangle$ at $0.1\lesssim y/\delta\lesssim0.7$ is traced to low-wavenumber content (§5.1, Figs. 6–9). **Shown**
6. Processing each wall-parallel plane independently produces no visible wall-normal discontinuities, attributed to the continuity of convolutional layers with respect to the input (§5.1.1, Figs. 7, 11, 17). **Shown** (qualitative)
7. The conditional GAN (factor 8) reconstructs high-wavenumber content and also corrects resolved-wavenumber discrepancies, most evidently in $v$; remaining errors at the highest wavenumbers are three to four orders of magnitude below the most energetic eddies; spectral spikes are the chequerboard artefact of nearest-neighbour upsampling (§5.2, Figs. 12–14). **Shown**
8. A priori from vLES input the full pipeline reproduces DNS mean velocity, resolved Reynolds stresses and SGS stresses; the "typical supervised model" (conditional GAN on vLES) keeps the vLES mean velocity and overpredicts the streamwise and shear Reynolds and SGS stresses (§5.3, Figs. 18, 20, 21). **Shown**
9. In the spanwise premultiplied spectrum of $u$ at $y^+\approx15$ the pipeline peaks at $k_z\delta\approx60$ ($\lambda_z^+\approx100$), the typical supervised model at $k_z\delta\approx40$ ($\lambda_z^+\approx150$) (§5.3.2). **Stated** (figure not shown)
10. The pipeline restores the outer-layer energy at $2\lesssim k_z\delta\lesssim10$ for $y/\delta\gtrsim0.1$ that is absent in the vLES input (§5.3.2, Fig. 19). **Shown**
11. A posteriori at $Re_\tau\approx1000$ the pipeline model gives mean velocity in good agreement with DNS and the near-wall rise of total Reynolds shear stress ($3\lesssim y^+\lesssim30$); the selective mixed-scale model overpredicts the velocity and underpredicts the shear stress; the typical supervised model is slightly better than the conventional one but still overpredicts the velocity (§6.1, Fig. 22). **Shown**
12. With the pipeline the SGS shear stress exceeds the resolved one near the wall ($3\lesssim y^+\lesssim10$), qualitatively like filtered DNS; with the conventional model it is smaller (§6.1, Fig. 22c). **Shown**
13. Under constant body-force driving the mass flow rate is overpredicted by 23% with the conventional SGS model and by 10% with the pipeline (§6.1). **Shown**
14. Mean-velocity errors follow from the total shear-stress balance (Eq. 6.1): underpredicted near-wall Reynolds shear stress forces an overpredicted viscous stress and hence velocity (§6.1). **Derived** + **Shown**
15. The pipeline overpredicts the near-wall wall-normal and spanwise normal stresses (non-physical, but enabling the correct shear stress), with a larger fraction carried by the SGS part (§6.1, Fig. 23). **Shown**
16. The conventional model enlarges and deforms the near-wall resolved structures at $y^+\approx15$; the pipeline produces finer structures, notably in $v$ (§6.1, Fig. 24). **Shown** (qualitative)
17. In the resolved Reynolds-stress budget, $D^{\mathrm{sgs}}_{33}$ is positive (backscatter) for the pipeline at $y^+\lesssim100$ and negative for the conventional model; $D^{\mathrm{sgs}}_{22}$ is negligible for both (§6.2.1, Fig. 25). **Shown**
18. Pressure redistribution at $20\lesssim y^+\lesssim100$ with the pipeline is negative in the spanwise and positive in the wall-normal component, a transfer $w\to v$; for the conventional model the wall-normal peak is smaller and farther from the wall ($y^+\approx70$) (§6.2.1, Fig. 25). **Shown**
19. Proposed mechanism: spanwise SGS backscatter raises near-wall $\langle w'w'\rangle$, pressure redistribution passes it to $\langle v'v'\rangle$, which raises the near-wall Reynolds shear stress and corrects the mean velocity (§6.2.1, §6.2.3, §8). **Shown** (budget interpretation)
20. At $y^+\approx15$ the DNS wall-normal pressure redistribution peaks at $\lambda_z^+\lesssim60$, which vLES cannot resolve (Nyquist $2\Delta z^+\approx72$); with the pipeline it occurs at $0.03\lesssim k_z^+\lesssim0.05$, i.e. $3.5\Delta z\lesssim\lambda_z\lesssim5.8\Delta z$ ($130\lesssim\lambda_z^+\lesssim210$), peak at $\lambda_z^+\approx160$; the conventional model has no positive wall-normal peak (§6.2.2, Fig. 27). **Shown**
21. The mechanism is consistent with DNS analyses of spanwise near-wall backscatter (Hamba 2019; Inagaki & Kobayashi 2023) and with the redistribution of Abe's stabilized mixed model in coarse LES (Inagaki & Kobayashi 2020) (§6.2.3). **Stated** (cited)
22. Trained only at $Re_\tau\approx1000$, the pipeline applied at $Re_\tau\approx2000$ on the same wall-unit grid gives mean velocity and near-wall shear stress in good agreement with DNS, while the conventional model deviates (§7, Figs. 28–29). **Shown**
23. Because the CNNs act in computational coordinates, the wall-unit resolution must stay similar between training and testing, which limits transfer to other resolutions, aspect ratios and unstructured grids; the authors call this a CNN limitation (§7). **Stated**
24. Pointwise models, e.g. with velocity-gradient inputs, "may not be able to appropriately distinguish the non-physical structures", whereas CNNs see their spatial extent (§7). **Stated**
25. The pipeline also works for LESx4 a priori and a posteriori, without degrading well-resolved eddies, with mean velocity and near-wall shear stress closer to DNS than the conventional model (App. B, Figs. 30–36). **Shown**
26. Clipping sensitivity: as $\nu_{\mathrm{clip}}/\bar\nu_w$ decreases through 0, $\approx-1$, $\approx-2$ the mean velocity approaches DNS; $\approx-3$ is unstable; even $\nu_{\mathrm{clip}}=0$ (no backscatter) beats the conventional model (App. C, Fig. 37). **Shown**
27. Clipping is needed because, per Matsumoto, Inubushi & Goto (2024), machine-learned turbulence models on grids with $k_{\max}\eta<0.2$ cannot run stably; the present vLES has $k_{z,\max}\eta\approx0.13$ (App. C). **Stated** (cited criterion)
28. Hyperparameters from preliminary experiments: gradient-penalty weight 1, 10, 100 insensitive (10 slightly better); cycle-loss weight 1 better than the recommended 10; the conditional GAN preferred over a plain CNN with $L_2$ loss for small scales (§2.2, §3.1). **Stated** (not shown)

The SGS stress (§3.2) and its clipping (Eq. 3.2), in registry notation with
$u^{\mathrm{SR}}_i$ the super-resolved velocity at the $m\times m$ sub-points of
a coarse cell, $\overline{(\cdot)}^m$ their average and
$u^\star_i=u^{\mathrm{SR}}_i-\overline{u^{\mathrm{SR}}_i}^m$:
$$\tau_{ij}=\overline{u^\star_iu^\star_j}^{\,m},\qquad \nu_{\mathrm{eff}}=-\frac{\tau_{ij}\,\partial_j\bar u_i}{2\bar S^d_{ij}\,\partial_j\bar u_i},\qquad \tau^{\mathrm{clip}}_{ij}=\begin{cases}\tau_{ij}, & \nu_{\mathrm{eff}}>\nu_{\mathrm{clip}},\\ \tau_{ij}+\left(\nu_{\mathrm{eff}}-\nu_{\mathrm{clip}}\right)2\bar S^d_{ij}, & \text{otherwise,}\end{cases}$$
so that the clipped stress has effective viscosity exactly $\nu_{\mathrm{clip}}\le0$;
$m=8$ and $\nu_{\mathrm{clip}}/\bar\nu_w\approx-2$ are used. No density factor
appears in the printed definition (low Mach number).

# Printed slips

- **§6.2.2, p. A28-36:** "Conversely, at blue regions in the figure, $(\partial v'/\partial y)>0$ and $(\partial w'/\partial z)<0$ are satisfied" repeats the signs given for the red regions; the Fig. 26 legend gives blue as $\partial v''/\partial y<0$, $\partial w''/\partial z>0$.
- **§6.1, p. A28-30:** "the viscous shear stress $\overline{\mu(\partial u/\partial x)}$", while Eq. (6.1) has $\overline{\mu\,\partial u/\partial y}$.
- **§6.2.3, p. A28-38:** "the spanwise wavenumber of $k_z^+\approx60$"; §6.2.2 gives 60 as the wavelength $\lambda_z^+$, with $k_z^+\gtrsim0.1$.
- **App. B.1, p. A28-45:** "qualitatively similar to the LESx8 case discussed in § 2.2.2"; the LESx8 a priori pipeline results are in §5.3.
- **Reference list:** Kingma & Ba (2014) is printed with "arXiv:1704.00028", the identifier also printed for Gulrajani et al. (2017).
- Wording: the pipeline is called the "proposed unsupervised SGS model" (Fig. 23 caption, §7) although it is unsupervised–supervised; "four-times courser" (§1); the Dean (1978) entry prints a URL in an "arXiv:" field.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $S_{ij}=\partial_ju_i+\partial_iu_j-\tfrac23\delta_{ij}\partial_ku_k$ | $2S^d_{ij}$ | **no factor 1/2** in the source |
| $\tau_{ij}=\mu S_{ij}$ | $\sigma_{ij}$ | viscous stress |
| $\overline f$ (§2), $\overline f$ (§6) | $\bar f$; $\langle f\rangle$ | **collision:** the overbar is the LES filter in §2 and the Reynolds average in §6 |
| $\widetilde f$, $f''$ | $\tilde f$, $f''$ | Favre filter and fluctuation |
| $\widehat{(\cdot)}$ (§3.2), $\widehat{(\cdot)}$ (§6.2.2) | $\overline{(\cdot)}^m$; $\phi_{\boldsymbol k}$ | **collision:** the hat is the sub-cell top-hat average and the Fourier transform, never the registry's test filter |
| $u^*_{i,kl}$ | $u^\star_i$ | sub-cell fluctuation of the super-resolved field |
| $\tau_{ij,SGS}=-\widehat{u_i^*u_j^*}$ | $-\tau_{ij}$ | **negative convention:** the source's SGS stress is the negative of the registry's |
| $\mu_{eff}$, $\mu_{clip}$ | $\nu_{\mathrm{eff}}$, $\nu_{\mathrm{clip}}$ | page-local, as on the [gradient model](/methods/gradient-model.md) page; defined with the source's $S_{ij}$ and a stress without density factor |
| $\overline\mu_w$ | $\bar\nu_w$ (mean wall viscosity) | the ratio $\mu_{clip}/\overline\mu_w$ is quoted as printed |
| $D_{SGS,ij}$, $D_{p,ij}$, $P_{ij}$, $T_{\cdot,ij}$ | page-local | resolved Reynolds-stress budget (Eqs. 6.2–6.11); $D^{\mathrm{sgs}}_{ii}>0$ read as backscatter |
| $\check F_{ij}(k,y)$ | page-local | spanwise spectral density of a budget term |
| $\delta$, $u_b$, $M_b$, $Re_\tau$ | $\delta$, $U_b$, $M_b$, $Re_\tau$ | channel half-width, bulk velocity |
| $G_{vLES-fDNS}$, $G_{SR}$, $F$, $D_X$, $D_Y$ | page-local | CycleGAN and conditional-GAN generators and critics; parameters part of $\boldsymbol\theta$ |
| $\lambda_{GP}$, $\lambda_{cyc}$ | page-local | gradient-penalty and cycle-loss weights; **collision** with the Taylor microscale |
| $\kappa(T)$ | page-local | heat conductivity; **collision** with the von Kármán constant |
| $k_z$, $\lambda_z$, $k_{max}\eta$ | page-local, $k_{\max}\eta$ | spanwise wavenumber and wavelength |
| a priori / a posteriori | same | the a priori input is precomputed vLES, not filtered DNS |

# Reference list

60 printed references in JFM author–year style, alphabetical; merged complete
into the [bibliography](/bibliography.md) with `citedby` this slug. Duraisamy
(2021) and Inagaki & Kobayashi (2023) are the ingested `duraisamy-2021` and
`inagaki-2023`; Maeyama & Kawai (2023, J. Fluid Mech. 969:A29) is distinct from
the ingested `maeyama-2022`. The arXiv preprints (Gulrajani 2017, Kingma 2014,
Mirza 2014, Tian 2022, Zhu 2020) are preprint entries as printed. Recorded as
printed: Slotnick et al. (2014) "Tech. Rep," without institution, Lilly (1966)
NCAR report, the Smith & Metzler issue "(-1)", and the Kingma & Ba arXiv
identifier (see the printed slips).

# Pages created or updated

Chunk 6 (2026-10-26). This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Gradient (Clark) model and the clipping of structural SGS models](/methods/gradient-model.md)
- [Neural-network subgrid-scale models](/methods/neural-network-sgs-model.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Super-resolution subgrid-scale models](/methods/super-resolution-sgs-model.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
