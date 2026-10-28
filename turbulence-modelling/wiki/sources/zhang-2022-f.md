---
type: Source
title: "Zhang et al. (2022b) — Density-unweighted subgrid-scale models for large-eddy simulations of compressible turbulence"
description: "Writes compressible LES with a plain (density-unweighted) filter, whose extra unclosed terms include a subgrid mass flux and density–temperature correlation, derives gradient-model closures for them and compares gradient, approximate-deconvolution, dynamic Smagorinsky, dynamic mixed and DIAD models a priori and a posteriori in decaying compressible isotropic turbulence."
resource: "doi:10.1063/5.0095726"
source_kind: paper
authors: [Zhang C., Yuan Z., Wang Y., Zhang R., Wang J.]
year: 2022
venue: "Phys. Fluids 34:065137"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Physics_of_Fluids_Zhang_Density-unweighted_subgrid-scale_models_for_large-eddy_simul.pdf"
tags: [les, compressible, sgs-model, approximate-deconvolution, gradient-model, a-priori-a-posteriori]
timestamp: 2026-10-27T21:10:00Z
---

# Summary

Zhang et al. (2022b) study [large-eddy simulation](/definitions/large-eddy-simulation.md)
of compressible turbulence with a plain, density-unweighted spatial filter
instead of Favre filtering. The filtered equations then carry more unclosed
terms: a subgrid mass flux in the continuity equation, a subgrid
density–temperature correlation in the momentum and energy equations, the
density-weighted subgrid stress, the subgrid heat flux, turbulent and
viscous diffusion, and time derivatives of subgrid terms that the authors
say can cause numerical instability. Five closures are compared: the
[gradient model](/methods/gradient-model.md), whose density-unweighted forms
for all terms the authors derive; the scale-similar approximate
deconvolution model (van Cittert series of order four) and the dynamic
iterative approximate deconvolution (DIAD) model of Yuan et al., here
applied to compressible turbulence for the first time, and the dynamic
mixed model, all on the [scale-similarity](/methods/scale-similarity-model.md)
page; and the [dynamic Smagorinsky](/methods/dynamic-procedure.md) model,
the last two rewritten for density-unweighted terms in an appendix.

The data are DNS of compressible [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
at $1024^3$ (hybrid compact and seventh-order [WENO](/methods/weno-scheme.md)
scheme) forced to $M_t=0.40$ and 0.79 at $Re_\lambda\approx260$, then let
decay; a Gaussian filter of width $16h_{\mathrm{DNS}}$ and LES on $128^3$.
[A priori](/definitions/a-priori-and-a-posteriori-testing.md), the gradient
model correlates above 0.9 and approximate deconvolution and DIAD above
0.98, DIAD best. The mass-flux, stress, heat-flux and turbulent-diffusion
terms dominate, while the density–temperature term is small but grows with
$M_t$. A posteriori DIAD best reproduces the kinetic-energy decay,
spectra, the PDFs of the subgrid terms, of the subgrid energy flux, strain
rate and vorticity, and instantaneous structures; the
[Smagorinsky](/methods/smagorinsky-model.md)-based dynamic models are
over-dissipative, approximate deconvolution under-dissipative, the gradient
model close to DIAD and cheapest. The negative
([backscatter](/definitions/energy-backscatter.md)) tail of the subgrid
energy flux lengthens as $M_t$ grows.

# Version read

Version of record (AIP; submitted 12 April 2022, accepted 3 June 2022,
published online 24 June 2022), 26 PDF pages (an AIP cover page and
article pages 065137-1 to 065137-25), all read; equations read visually
because text extraction garbles them. Page 1 matches the metadata. No
identity problem. Numbering on this page is that of this version.

# Key claims

Page-local symbols (density-unweighted filtering; the overbar is a plain
filter and no tilde appears): $m_j=\overline{\rho u_j}-\bar\rho\bar u_j$
the subgrid mass flux; $H_{\rho T}=\overline{\rho T}-\bar\rho\bar T$ the
subgrid density–temperature correlation;
$\tau^\rho_{ij}=\overline{\rho u_iu_j}-\bar\rho\bar u_i\bar u_j$ the
density-weighted subgrid stress (full tensor, not divided by $\bar\rho$;
not the registry's Favre form); $\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$
the velocity-only stress (the source's $\tau'_{ij}$);
$q^\rho_j=\overline{\rho Tu_j}-\bar\rho\bar T\bar u_j$ and
$q_j=\overline{Tu_j}-\bar T\bar u_j$ the subgrid heat fluxes;
$J_j=\overline{\rho u_ju_ku_k}-\bar\rho\bar u_j\bar u_k\bar u_k$ (turbulent
diffusion through $\partial_jJ_j$) and $D_j=\overline{\sigma_{ij}u_i}-\bar\sigma_{ij}\bar u_i$
(viscous diffusion); $N_i$ the DIAD iteration count;
$h_{\mathrm{DNS}}$, $h_{\mathrm{LES}}=\Delta/2$ the grid spacings;
$C(\cdot)$, $E_r(\cdot)$ the a priori correlation coefficient and relative
error (Eqs. 35–36).

1. Compared with Favre filtering, density-unweighted LES has more unclosed terms ($m_j$, $H_{\rho T}$, $J_j$, $D_j$ besides $\tau^\rho_{ij}$ and $q^\rho_j$) and extra unsteady terms $\partial_tm_i$, $\partial_t(\tfrac12\tau^\rho_{kk})$, $\partial_tH_{\rho T}$ that "can lead to numerical instability" (§II, Eqs. 10–20). **Derived** (the equations), **Stated** (the instability)
2. Only a few models had been proposed for the density-unweighted method: the dynamic Smagorinsky model (refs. 29, 64) and the gradient model (refs. 35, 36) (§I). **Stated**
3. The authors give gradient-model closures for the density-unweighted terms: $m_j=\tfrac{\Delta^2}{12}\partial_k\bar\rho\,\partial_k\bar u_j$, $H_{\rho T}=\tfrac{\Delta^2}{12}\partial_k\bar\rho\,\partial_k\bar T$, $\tau^\rho_{ij}=\tfrac{\Delta^2}{12}(\bar\rho\,\partial_k\bar u_i\partial_k\bar u_j+\bar u_i\,\partial_k\bar\rho\,\partial_k\bar u_j+\bar u_j\,\partial_k\bar\rho\,\partial_k\bar u_i)$, and analogous forms for $q^\rho_j$ and $J_j$ (Eqs. 22–26). **Derived** (results printed, steps not shown)
4. The DIAD model is applied to compressible turbulence for the first time (Abstract, §I, §III B, §V). **Stated**
5. $\tau^\rho_{ij}$ and $q^\rho_j$ are the dominant unclosed terms in the present ranges of $M_t$ and $Re_\lambda$; neglecting the nonlinearity of the diffusion terms ($D_j$) is acceptable, with $\bar\sigma_{ij}\approx2\bar\rho\nu\bar S^d_{ij}$ for constant kinematic viscosity (§II, citing refs. 6, 71, 73). **Stated**
6. Root-mean-square magnitudes at $\Delta=16h_{\mathrm{DNS}}$ for $M_t=0.40$/0.79: $\partial_j\tau^\rho_{ij}$ 10.32/10.54; $\partial_jm_j$ 3.9/3.68; $\frac{1}{(\gamma-1)M^2}\partial_jq^\rho_j$ 51.29/50.81; $\frac1{\gamma M^2}\partial_jH_{\rho T}$ 0.0060/0.11; $\partial_j(\tfrac12J_j)$ 24.60/17.19 (Table II). **Shown**
7. The $H_{\rho T}$ term is printed as "two orders of magnitude higher" at $M_t=0.8$ than at 0.4; compressibility strongly influences it, and it is kept because it "might have special significance" in flows with rapidly changing density (§IV A). **Stated** (see Printed slips)
8. A priori, the gradient-model correlation coefficients for $\tau^\rho_{11}$, $\tau^\rho_{12}$ and $q^\rho_1$ exceed 0.9 at both $M_t$, the heat-flux correlation being higher than the stress ones (§IV A, Fig. 1). **Shown**
9. A priori, approximate deconvolution and DIAD correlate above 0.98 with relative errors below 0.2; DIAD has the highest correlation and the lowest error (Abstract, §IV A, Figs. 1–2). **Shown**
10. A priori, the correlation increases and the relative error decreases during the decay, more strongly at $M_t=0.8$ (§IV A). **Shown**
11. DIAD improves significantly from $N_i=1$ to $N_i=2$ and is nearly constant beyond; $N_i=2$ is used, with stencil size $N_{\mathrm{st}}=3$ and $\Delta/h=2$ (§III B, §IV A, Fig. 3). **Shown**
12. Approximate deconvolution with $N_{\mathrm{AD}}=3$–5 is recommended for stability; $N_{\mathrm{AD}}=4$ is used (§III B, Eq. 29, citing ref. 24). **Stated**
13. Scale-similarity forms, not direct deconvolution forms, are used for approximate deconvolution and DIAD because Yuan et al. showed they satisfy symmetry and realizability conditions (§III B, Eq. 28, refs. 24, 65). **Stated**
14. Cost per time step on 32 cores (Xeon Gold 6140), $M_t=0.40$/0.80: dynamic Smagorinsky 0.850/0.853, dynamic mixed 1.411/1.418, gradient 0.321/0.319, approximate deconvolution 0.678/0.678, DIAD 0.876/0.870 CPU s (Table III, §IV B). **Shown**
15. A posteriori, DIAD predicts the kinetic-energy decay closest to filtered DNS; the other models over-predict the kinetic energy; approximate deconvolution and gradient models agree at $M_t=0.4$ but differ at 0.8 (§IV B, Fig. 5). **Shown**
16. Velocity spectra: all models agree with filtered DNS at low wavenumbers; DIAD best overall; approximate deconvolution over-estimates the high-wavenumber energy; the dynamic Smagorinsky and mixed models are over-dissipative; the gradient model does better at the larger $M_t$ (§IV B, Fig. 6). **Shown**
17. The negative tail of the PDF of $H_{\rho T}$ is shorter at $M_t=0.8$; DIAD reproduces the PDF reasonably, approximate deconvolution always under-estimates it, the gradient model over-predicts the negative tail at $M_t=0.4$ (§IV B, Fig. 7). **Shown**
18. PDFs of $m_1$: DIAD agrees with filtered DNS; the gradient model has longer tails, approximate deconvolution under-estimates (§IV B, Fig. 8). **Shown**
19. PDFs of the subgrid energy flux $-\tau^\rho_{ij}\bar S_{ij}$: DIAD close to filtered DNS; the dynamic models and approximate deconvolution under-estimate with narrow PDFs; the gradient model is good early and over-estimates later; as $M_t$ increases the negative tail lengthens, so "compressibility enhances the energy transfer from small to large scales" (§IV B, Fig. 9). **Shown**
20. Spatial mean of the flux: approximate deconvolution and DIAD under-estimate filtered DNS in the initial decay; the gradient model under-estimates at $M_t=0.4$ and slightly over-estimates at 0.8; approximate deconvolution is worst (§IV B, Fig. 10). **Shown**
21. PDFs of the deviatoric stress: the dynamic models and approximate deconvolution are narrower than the exact ones; DIAD and the gradient model are the most accurate at all times (§IV B, Figs. 13–14). **Shown**
22. Strain-rate PDFs: DIAD almost overlaps filtered DNS, approximate deconvolution exceeds it, the gradient model is good early and worse later, the dynamic models overestimate the peak of the $\lvert\bar S\rvert$ PDF (§IV B, Figs. 15–17). **Shown**
23. Vorticity PDF and contours: DIAD best, with more small-scale structures (§IV B, Figs. 18–20). **Shown**
24. Heat flux $q^\rho_1$: DIAD agrees with filtered DNS at both $M_t$; approximate deconvolution is lower and misses the small-scale structure; the gradient model is slightly high at $M_t=0.4$ and nearly overlapping at 0.8 (§IV B, Figs. 21–23). **Shown**
25. Density-unweighted LES with these models gives statistics and instantaneous structures consistent with filtered DNS; DIAD "can reconstruct unclosed terms in density-unweighted LES very well" (§V). **Shown** (decaying isotropic turbulence only)

The appendix's dynamic Smagorinsky model for density-unweighted terms
closes the deviatoric $\tau_{ij}$ with $C_s$, its trace with
$\tau_{kk}=2C_I\Delta^2\lvert\bar S\rvert^2$, $m_j=-C_\rho\Delta^2\lvert\bar S\rvert\partial_j\bar\rho$,
$q_j=-C_T\Delta^2\lvert\bar S\rvert\partial_j\bar T$ and
$H_{\rho T}=-C_H\Delta^2\partial_j\bar\rho\,\partial_j\bar T$, each
coefficient by Lilly's least squares over the domain with a test filter
$\hat\Delta=2\Delta$ (Eqs. A1–A6); the dynamic mixed model adds a
scale-similar part to each with two least-squares coefficients
(Eqs. A7–A24). The density-weighted terms are rebuilt from the
velocity-only ones as $\tau^\rho_{ij}\approx\bar\rho\tau_{ij}+\bar u_im_j+\bar u_jm_i$,
$q^\rho_j\approx\bar\rho q_j+\bar Tm_j+\bar u_jH_{\rho T}$ (Eqs. 32–34).

# Printed slips

- **§IV A against Table II:** "the magnitude of $\frac{1}{\gamma M^2}\frac{\partial H}{\partial x_j}$ at $M_t=0.8$ is two orders of magnitude higher than that of $M_t=0.4$"; Table II prints 0.11 and 0.0060, a ratio of about 18 *(compiler check, not in the sources)*.
- **Turbulent Mach number of case 2:** 0.79 in Tables I and II, 0.80 in Table III, 0.8 in the text.
- **Fig. 3:** the text says it shows "$\tau_{11}$ and $\tau_{22}$", the caption "normal and shear components", the legend $\tau_{11}$, $\tau_{11}$, $\tau_{12}$, $\tau_{13}$.
- **Eq. (6)** is printed $\lambda=\sqrt{\langle u_iu_i\rangle/\langle(\partial u_j/\partial x_j)^2\rangle}$, with the velocity divergence in the denominator.
- **§I citation ranges against the printed list:** "dynamic mixed model (DMM),51–54" includes ref. 54 (Stolz & Adams, *An approximate deconvolution procedure for large-eddy simulation*); "(ADM),24,55–59" includes ref. 59 (Boris et al., *New insights into large eddy simulation*); "implicit-LES (ILES).60–64" and "DSM29,64" both include ref. 64 (Bodony & Lele, jet noise).
- **References:** ref. 8 prints "S. B. Pope and S. B. Pope"; refs. 35, 36, 38 print the first author as "S. Gs" while the text says "Sidharth et al." and ref. 37 prints "G. Sidharth"; ref. 44 prints "B. Halpern" as the author of an edited volume; ref. 71 prints the journal as "Appl. Sci."; ref. 31 prints its pages as "Annual Research Briefs No. 365–377".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar f=G\otimes f$ | $\bar f$ | plain (density-unweighted) filter; no Favre filter is used |
| $\hat{(\cdot)}$, $\hat\Delta=2\Delta$ | $\hat{(\cdot)}$, $\hat\Delta$ | test filter |
| right over-arrow (App.) | (filter at $4\Delta$, page-local) | dynamic mixed model only |
| $\Delta_{DNS}$ | $h_{\mathrm{DNS}}$ (page-local) | **collision:** $\Delta$ is the filter width |
| $\tau_{ij}=\overline{\rho u_iu_j}-\bar\rho\bar u_i\bar u_j$ | $\tau^\rho_{ij}$ (page-local) | **not** the registry's $\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$; positive trace |
| $\tau'_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$ | $\tau_{ij}$ | |
| $\tau^A_{ij}$ (Figs. 13–14) | $\tau^{\rho,d}_{ij}$ | deviatoric part |
| $M_j$ | $m_j$ (page-local) | **collision** with the dynamic-procedure tensor $M_{ij}$ |
| $H$, $Q_j$, $Q'_j$, $J_j$, $D_j$ | $H_{\rho T}$, $q^\rho_j$, $q_j$, $J_j$, $D_j$ (page-local) | |
| $\Pi=-\tau_{ij}\bar S_{ij}$ | $-\tau^\rho_{ij}\bar S_{ij}$ | the registry's $\Pi$ with the density-weighted full stress; positive = forward |
| $\bar S_{ij}$, $\lvert\bar S\rvert$ | $\bar S_{ij}$, $\lvert\bar S\rvert$ | factor two included |
| $\sigma_{ij}$ | $\sigma_{ij}$ | viscous stress |
| $C_s^2$, $C_I$, $C_\rho$, $C_T$, $C_H$ | $C_s^2$, $C_I$, (page-local) | **collision:** $C_T$ is not the TENO cut-off |
| $L_{ij}$, $M_{ij}$ (App.) | $L_{ij}$, $M_{ij}$ | dynamic procedure |
| $N$ (ADM), $N_i$, $(N_s,R)$ (DIAD) | $N_{\mathrm{AD}}$, $N_i$ (page-local), $(N_{\mathrm{st}},\Delta/h)$ | **collision:** $N$ is the polynomial degree |
| $M$, $Re$, $Pr$, $\gamma$ | $M$, $Re$, $Pr$, $\gamma$ | reference values |
| $\alpha=PrRe(\gamma-1)M^2$ | (page-local) | |
| $M_t=Mu^{rms}/\langle\sqrt T\rangle$ | $M_t$ | $u^{rms}=\sqrt{\langle u_iu_i\rangle}$ (three components) |
| $Re_\lambda$, $\lambda$, $\eta$, $L_I$ | $Re_\lambda$, $\lambda$, $\eta$, $L$ | $\lambda$ as printed in Eq. (6) |
| $\tau=L_I/u^{rms}$ | $T_E$ | **collision:** $\tau$ is a time |
| $\theta$, $\omega$ (Table I) | $\partial_ju_j$, $\lvert\omega_i\rvert$ | **collision:** $\theta$ is the velocity divergence, not a momentum thickness |
| $P_j$, $S$ (App.) | (auxiliary tensors, page-local) | **collision** with pressure and strain |
| fDNS | filtered DNS | |

# Reference list

87 printed references, numbered (AIP) style. The list is merged complete
into the [bibliography](/bibliography.md) with `citedby` this slug. Ref. 25
(Li et al. 2021, Phys. Fluids 33:125127) is the ingested
[li-2021](/sources/li-2021.md). Refs. 35, 36 and 38, printed with the
author "S. Gs", are keyed as printed (`gs-*`), alias candidates of the
Sidharth entries; ref. 44 is keyed `halpern-1993` as printed; ref. 63
prints "G. Page" as the author of *Implicit Large Eddy Simulation,
Computing Turbulent Fluid Dynamics*; ref. 8 (Pope) prints the author twice.
No item is unparseable.

# Pages created or updated

Chunk 11 (2026-10-27). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Gradient (Clark) model and the clipping of structural SGS models](/methods/gradient-model.md)
- [Neural-network subgrid-scale models](/methods/neural-network-sgs-model.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
