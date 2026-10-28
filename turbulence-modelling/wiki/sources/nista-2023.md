---
type: Source
title: "Nista et al. (2023) — Investigation of the generalization capability of a generative adversarial network for large eddy simulation of turbulent premixed reacting flows"
description: "A priori study of a super-resolution GAN closure for the subfilter stress and temperature flux of premixed-flame LES, trained on one methane jet-flame DNS and tested at other Reynolds and Karlovitz numbers, on a hydrogen flame and on an untrained scalar; generalization holds when the filter-to-Kolmogorov ratio is kept."
resource: "doi:10.1016/j.proci.2022.07.244"
source_kind: paper
authors: [Nista L., Schumann C.D.K., Grenga T., Attili A., Pitsch H.]
year: 2023
venue: "Proc. Combust. Inst. 39:5279–5288"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Proceedings_of_the_Combustion_Institute_Nista_Investigation_of_the_generalization_capability_of_a_generati.pdf"
tags: [super-resolution, neural-network, combustion, a-priori-a-posteriori, generalization]
timestamp: 2026-10-28T06:44:00Z
---

# Summary

Nista et al. (2023) test a priori how far a
[super-resolution](/methods/super-resolution-sgs-model.md) generative
adversarial network, used as a subfilter closure for
[LES](/definitions/large-eddy-simulation.md) of turbulent premixed
combustion, generalizes beyond its training data. The generator, a 3-D
variant of ESRGAN and PIESRGAN with one residual-in-residual dense block
and three upsampling layers (factor 8 per direction, about 25 million
parameters), maps box-filtered [DNS](/definitions/direct-numerical-simulation.md)
fields $(\bar u,\bar v,\bar w,\bar T)$ with $\Delta=8h$ to DNS resolution;
the subfilter stress and temperature flux are then evaluated from the
reconstruction. The loss combines pixel and gradient mean-square errors
with a relativistic-average adversarial term. It belongs to the family of
[neural-network SGS models](/methods/neural-network-sgs-model.md).

Training uses only the R2K1 DNS of a lean methane/air slot jet flame. In
sample, the joint PDF of modelled against DNS $\tau_{12}$ lies on the
diagonal, while the [dynamic](/methods/dynamic-procedure.md)
[Smagorinsky model](/methods/smagorinsky-model.md) correlates poorly; the
authors concede that this baseline "might be not optimal". The network
extrapolates well to half and four times the training Reynolds number and
to a Karlovitz number ten times larger, where $\Delta/\delta_L$ changes but
$\Delta/\eta$ is kept; on a hydrogen jet flame with the training filter
($\Delta/\eta\approx14.88$) it overpredicts the jet velocity and the large
gradients, and with a $4h$ filter ($\Delta/\eta\approx6.6$) it nearly
matches. The authors conclude that $\Delta/\eta$ must be conserved between
training and application, while $\Delta/\delta_L$ does not seem
fundamental. Applied to the never-trained OH mass fraction, the network is
poor in near-uniform regions and good at the flame boundary. All evidence
is [a priori](/definitions/a-priori-and-a-posteriori-testing.md);
a posteriori LES is left to future work.

# Version read

Version of record (Elsevier; received 5 January 2022, online 24
September 2022, issue 2023), 10 pages (5279–5288), all read; Eqs. (1)–(5)
and Table 1 checked visually. Page 1 matches the published metadata; the
second author's initials are "C.D.K." in the byline and "C.K.D." in the
authors' own ref. [20]. The online supplementary material (further §4.1
statistics) is not in the file. Equation, section and figure numbers are
those of this version.

# Key claims

Page-local symbols: $\tau^T_i=\widetilde{u_iT}-\tilde u_i\tilde T$ the
subfilter temperature flux; $\delta_L$ the thermal flame thickness,
$s_{\mathrm L}$ the laminar flame speed (registry §11); $Ka$ the Karlovitz
number; $h$ the DNS grid spacing; $c_{\mathrm{pix}}$, $c_{\mathrm{grad}}$,
$c_{\mathrm{adv}}$ the loss weights; $\mathcal L_{\mathrm{pix}}$,
$\mathcal L_{\mathrm{grad}}$, $\mathcal L_{\mathrm{RaGAN}}$ the loss terms.
The subfilter stress is the per-unit-mass $\tau_{ij}/\bar\rho=\widetilde{u_iu_j}-\tilde u_i\tilde u_j$,
full tensor, positive trace.

1. A super-resolution GAN closes the subfilter stress and scalar flux of the filtered reactive Navier–Stokes equations: the generator reconstructs DNS-resolution fields from filtered DNS, so that Eqs. (2) and (3) are evaluated at DNS level (§1, Eqs. 1–3). **Stated**
2. Filtered-DNS fields are treated as statistically similar to LES fields for the a priori tests (§1). **Stated**
3. Generator: 3-D convolutional layers with leaky ReLU, one RRDB (ESRGAN has 23), three nearest-neighbour upsampling layers each followed by a convolution, factor 8 per direction, 64 filter maps per layer, about 25 million parameters, 4 channels (§3.1, Fig. 1). **Stated**
4. Discriminator as in PIESRGAN (3-D convolutions, binary output, filter maps doubling from 64) (§3.1). **Stated**
5. $\mathcal L=c_{\mathrm{pix}}\mathcal L_{\mathrm{pix}}+c_{\mathrm{grad}}\mathcal L_{\mathrm{grad}}+c_{\mathrm{adv}}\mathcal L_{\mathrm{RaGAN}}$ with weights $[0.89,0.06,0.00006]$ tuned in [20], $\mathcal L_{\mathrm{pix}}$ and $\mathcal L_{\mathrm{grad}}$ the mean-square errors of the field and of its gradient, applied per tensor element (§3.1, Eq. 4). **Stated**
6. The generator is pre-trained with the pixel loss only, to prevent convergence failure, then trained adversarially until no further improvement (§3.1). **Stated**
7. Training data: R2K1 only, box filter $\Delta=8h$, 73,100 random sub-boxes of $64^3$ (DNS) and $8^3$ (filtered) points, last 10% of the snapshots held out, flips and rotations, global min–max normalization (§3.2). **Stated**
8. Four nodes with one NVIDIA V100 32 GB each cut the wall training time "from roughly 5 days to 28 h"; mini-batch 8 per GPU, learning rate $10^{-4}$, ADAM (§3.2). **Stated**
9. In sample, the GAN's $\tau_{12}$ joint PDF aligns with the diagonal while the dynamic Smagorinsky model "exhibits a relatively low correlation" (§4, Fig. 2a,b). **Shown**
10. In sample, $\tau^T_1$ spreads narrowly along the diagonal, but the model "is not so accurate in predicting negative SFS scalar values" (§4, Fig. 2c). **Shown**
11. R1K1 (lower $Re$): the RMSE of the super-resolved fields is "roughly 75% less than the RMSE of the F-DNS", with textures still differing from DNS (§4.1, Fig. 3). **Shown**
12. R1K1 and R4K1: the $\tau_{12}$ and $\tau^T_1$ joint PDFs barely differ from the in-sample case (R4K1 slightly worse); the GAN extrapolates to lower and higher $Re$ (§4.1, Figs. 4a,b, 5a,b). **Shown**
13. Across the $Re$ series $\Delta/\eta\approx8$ and $\Delta/\delta_L\approx1.45$ are conserved, conjectured to be fundamental for extrapolation, as [19] found for the progress-variable variance (§4.1). **Stated**
14. R2K2 ($Ka$ about ten times the training value) keeps only $\Delta/\eta\approx8$ ($\Delta/\delta_L\approx0.062$ printed); the $\tau_{12}$ joint PDF stays on the diagonal, so $\Delta/\delta_L$ "might be not fundamental for generalizability" (§4.2, Figs. 4c, 5c). **Shown**
15. H2K2 with $\Delta=8h$ ($\Delta/\eta\approx14.88$, $\Delta/\delta_L\approx0.31$): the GAN strongly overpredicts the jet velocity, without small-scale oscillations, and the PDF of the normalized streamwise velocity gradient overpredicts large gradients (§4.2, Figs. 6–7 top). **Shown**
16. H2K2 with $\Delta=4h$ ($\Delta/\eta\approx6.6$): the reconstruction is sharper, thin features bulkier than DNS, and the gradient PDF deviates marginally; exact matching of $\Delta/\eta$ is hard because the network upsamples only by 8 (§4.2, Figs. 6–7 bottom). **Shown**
17. "The ratio $\Delta/\eta$ needs to be conserved between training and application of the network. However, the $\Delta/\delta_L$ ratio does not seems to be fundamental" (§4.2). **Shown** (H2K2 and R2K2 tests, a priori only)
18. The OH mass fraction predicted by the $(u,v,w,T)$-trained network is poor in the coflow and central jet (non-physical oscillations) and close to DNS at the jet–coflow boundary, attributed possibly to the link between OH and velocity [27] and to the gradient loss (§4.3, Fig. 8). **Shown**
19. Early tests showed systematic over- or underprediction when $\Delta/\eta$ is not conserved (§4.4). **Stated** (not shown)
20. Training on a range of filter sizes might relax the single-$\Delta/\eta$ restriction, within the memory limits of 3-D upsampling; a posteriori LES is required (§4.4). **Stated**
21. The results do not cover Karlovitz numbers below the critical one, where the flame thickness might matter, nor other fuels (§5). **Stated**

# Printed slips

- Eq. (1): "$\partial\bar\rho\tilde u_i\tilde u_j/\partial x_i$", "$-\partial\bar p/\partial x_j$", "$\partial\bar\tau_{ij}/\partial x_i$", "$\partial\bar\rho\tau^r_{ij}/\partial x_i$" with the time derivative of $\bar\rho\tilde u_i$: the pressure term's free index $j$ differs from that of the time-derivative term.
- H2K2: $\delta_L=435$ μm (§2) against 444 μm (Table 1); "a hydrogen/air mixture" (§2, Table 1 caption) against "a central jet of a gaseous mixture of hydrogen and oxygen" in the same paragraph.
- Pressure: "4 atm" for the $Re$ series, "4 bar" for R2K2 (§2).
- R2K2: $\Delta/\delta_L\approx0.062$ (§4.2). *(Compiler check, not in the sources: the printed $\delta_L/h\approx15$ and $\delta_L=200$ μm give $h\approx13.3$ μm, $\Delta=8h\approx107$ μm and $\Delta/\delta_L\approx0.53$; the same values give $\Delta/\eta\approx8.2$, consistent with the printed $\approx8$.)*
- H2K2: $\Delta/\eta\approx14.88$, $\Delta/\delta_L\approx0.31$ at $8h$ and $\Delta/\eta\approx6.6$ at $4h$. *(Compiler check, not in the sources: $\Delta/\eta=14.88$ with $\eta=10.2$ μm gives $\Delta\approx152$ μm, hence $\Delta/\delta_L\approx0.34$ with 444 μm, and halving the filter gives $\Delta/\eta\approx7.44$.)*
- $Re$ series: $\Delta/\eta\approx8$ (§4.1). *(Compiler check, not in the sources: $h=20$ μm, $\Delta=160$ μm and the Table 1 values of $\eta$ give 8.9, 7.0, 6.4 and 6.4 for R1K1–R4K1; $\Delta/\delta_L=160/110=1.45$ as printed.)*
- §2: the $Re$-series DNS is "produced by Luca et al. [21]", while ref. [21] lists Attili A. first.
- The dynamic Smagorinsky model is cited to [25], Smagorinsky (1963), only.
- §3.1: "The $L_1$ norm is applied to each component of the loss function", beside losses defined as mean-square errors in Eq. (4).
- "Karloviz number" (§2), "can applied" (§2), "does not seems" (§4.2), "further understating" (§4.4).

# Notation map

| Nista et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tilde\cdot$ | $\tilde\cdot$ | Favre filter, Eqs. (1)–(3) |
| $\bar\cdot$ | $\bar\cdot$, and $\tilde\cdot$ after Eq. (3) | **the paper writes the Favre filter as an overbar "for brevity" after Eq. (3)** |
| $\tau^r_{ij}=\widetilde{u_iu_j}-\tilde u_i\tilde u_j$ | $\tau_{ij}/\bar\rho$ | per unit mass, full tensor; called a "Reynolds-stress" tensor in §1 |
| $\bar\tau_{ij}$ | $\bar\sigma_{ij}$ | **filtered viscous stress, not the SGS stress** |
| $\tau^T_i$ | $\tau^T_i$ (page-local) | subfilter temperature flux |
| $U,V,W$ | $u,v,w$ | **$U$ is also the jet bulk velocity in Table 1** |
| $dx$ | $h$ | DNS grid spacing |
| $S_L$ | $s_{\mathrm L}$ | **$S_L$ is the Lundquist number in the registry** |
| $\delta_L$, $Ka$, $H$ | page-local | thermal flame thickness, Karlovitz number, slot width |
| $\phi$ | equivalence ratio (§2); generic field (Eq. 4, Fig. 1) | two meanings |
| $\beta=[\beta_1,\beta_2,\beta_3]$ | $c_{\mathrm{pix}}$, $c_{\mathrm{grad}}$, $c_{\mathrm{adv}}$ | **not the field-inversion multiplier $\beta(\boldsymbol x)$** |
| $L_{gen}$, $L_{pixel}$, $L_{gradient}$, $L_{RaGAN}$ | $\mathcal L$, $\mathcal L_{\mathrm{pix}}$, $\mathcal L_{\mathrm{grad}}$, $\mathcal L_{\mathrm{RaGAN}}$ | |
| $\eta$, $\Delta$ | $\eta$, $\Delta$ | box filter |
| F-DNS, SR, GT | filtered DNS, super-resolved field, ground truth | |

# Reference list

27 printed references, numbered [1]–[27] (Elsevier style). The list is
merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. [18] and [21] are two Attili et al. (2021) works, keyed in
printed order; [4] is the ingested `ihme-2022`. [11] prints pages "0–0",
[16] is in article-in-press form, [26] has no page range. No printed
duplicates and no unparseable items.

# Pages created or updated

Chunk 13 (2026-10-28). This source is cited on:

- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Neural-network subgrid-scale models](/methods/neural-network-sgs-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Super-resolution subgrid-scale models](/methods/super-resolution-sgs-model.md)
