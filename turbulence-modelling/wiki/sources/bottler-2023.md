---
type: Source
title: "Böttler et al. (2023) — Flamelet modeling of thermo-diffusively unstable hydrogen-air flames"
description: "Compares a new curvature-extended flamelet/progress-variable manifold with an unstretched-flame manifold against detailed chemistry for a laminar lean hydrogen-air spherical expanding flame with thermo-diffusive instabilities, a priori and in coupled simulations; curvature in the manifold improves the local flame structure, global properties are close for both."
resource: "doi:10.1016/j.proci.2022.07.159"
source_kind: paper
authors: [Böttler H., Lulic H., Steinhausen M., Wen X., Hasse C., Scholtissek A.]
year: 2023
venue: "Proc. Combust. Inst. 39:1567-1576"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Proceedings_of_the_Combustion_Institute_Böttler_Flamelet_modeling_of_thermo-diffusively_unstable_hydrogen-ai.pdf"
tags: [combustion, tabulated-chemistry, a-priori-a-posteriori]
timestamp: 2026-10-26T20:48:00Z
---

# Summary

Böttler et al. (2023) ask whether
[flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
can reproduce a lean ($\phi_{\mathrm{eq}}=0.4$, 300 K, atmospheric pressure) premixed
hydrogen–air spherical expanding flame that develops thermo-diffusive
cellular instabilities. The flame is laminar: there is no turbulence in the
configuration, and the paper enters this bundle only through its
tabulated-chemistry method and its
[a priori and a posteriori](/definitions/a-priori-and-a-posteriori-testing.md)
assessment of a reduced model against a resolved reference.

Two flamelet/progress-variable (FPV) manifolds are compared with a
detailed-chemistry (DC) dataset of Wen et al. FPV-h, from the authors'
earlier work, is built from unstretched premixed flames with enthalpy
variation, $\psi(Z,h_t,Y_c)$. The new FPV-$\kappa_c$ is
built with a composition space model over equivalence ratio
$0.275\le\phi_{\mathrm{eq}}\le0.6$ and curvature $-1500\le\kappa_{\mathrm f}\le5000$ m$^{-1}$ at
fixed strain 500 s$^{-1}$, with the curvature dimension mapped to a second
progress variable based on the H-radical mass fraction,
$\psi(Z,c,c_2)$. Both couple to the flow solver by
transporting the major species (H$_2$O, H$_2$, O$_2$) with mixture-averaged
diffusion and reconstructing the control variables from them.

A priori on the DC flame, the largest deviations lie in negatively curved
segments: up to 5% in temperature and 40% in $Y_{\mathrm{OH}}$ for FPV-h,
smaller and more localized for FPV-$\kappa_c$. A posteriori, linear stability
analysis of perturbed planar flames shows both FPV models predicting a wider
unstable range than DC; FPV-$\kappa_c$ reproduces the maximum growth rate.
Coupled two-dimensional axisymmetric flames up to about 6 cm radius show
smaller cells and a flame speed overpredicted by up to 15% at the largest
radii for both models, while FPV-$\kappa_c$ is closer to DC in the flame
microstructure.

# Version read

arXiv preprint arXiv:2301.06780v1 [physics.flu-dyn], 17 January 2023, 15 PDF
pages, all read: 12 pages of main text (references on pp. 10–12) plus a
3-page supplementary material on flame-tangential diffusion. The metadata
above are those of the published article (Proc. Combust. Inst. 39:1567–1576).
Page 1 title and authors match the published record. Page numbers on this
page are those of the arXiv file. Figures 3 and 8 are colour field images
described only as the text describes them.

# Key claims

1. Thermo-diffusive instabilities arise from a disproportion of thermal and mass diffusion, can be stabilizing or destabilizing, and are found only for mixtures with Lewis number below unity; Darrieus–Landau instabilities arise from thermal expansion and are always destabilizing (§1). **Stated**
2. Flame corrugation by intrinsic instabilities enhances the overall propagation speed, and thermo-diffusively unstable flames show characteristic cell sizes (§1, citing [1–11]). **Stated**
3. Simulations of intrinsic flame instabilities are sensitive to domain size, grid resolution, initialization and numerical methods, which restricts DNS to academic configurations (§1, §2.2). **Stated**
4. To the authors' knowledge, fully coupled (a posteriori) simulations of intrinsically unstable hydrogen–air flames with manifolds that include large curvature variations had not been presented before (§1). **Stated**
5. Canonical laminar flames (freely propagating, counterflow) are limited in the attainable strain and curvature; the composition space model takes arbitrary combinations of strain and curvature, which are its only external parameters (§2.1, citing [26, 27]). **Stated**
6. The FPV-$\kappa_c$ manifold covers $0.275\le\phi_{\mathrm{eq}}\le0.6$ and $-1500\le\kappa_{\mathrm f}\le5000$ m$^{-1}$ at fixed strain 500 s$^{-1}$; no burning solutions exist below $\kappa_{\mathrm f}=-1500$ m$^{-1}$ for this flame (§2.1, Fig. 1). **Shown**
7. The DC curvature distribution is well covered by the tabulated range, with few regions outside it (Fig. 1). **Shown**
8. In the composition-space solutions at $\phi_{\mathrm{eq}}=0.4$, curvature changes the local mixture composition and the maximum of $Y_c$ through differential diffusion, and $Y_{\mathrm H}$ increases monotonically with curvature, which justifies it as the curvature control variable (§2.1, Fig. 2). **Shown**
9. Transporting major species and reconstructing the control variables from them avoids extra modelling assumptions for the transport of composite quantities (mixture fraction, progress variable) and allows any number of transported species with a consistent mixture-fraction definition (§2.1, citing [19]). **Stated**
10. A priori on the DC flame: the largest temperature deviations of both models lie at negative curvature (concave towards the unburned mixture); FPV-h deviations reach 5% in temperature and 40% in $Y_{\mathrm{OH}}$; FPV-$\kappa_c$ deviations are smaller and confined to a smaller area (§3.1, Fig. 3). **Shown**
11. Linear stability analysis: both FPV models give a wider range of unstable wavelengths than DC, less so FPV-$\kappa_c$; FPV-$\kappa_c$ reproduces the maximum growth rate with the most unstable wavelength slightly shifted to shorter wavelengths; FPV-h has a larger peak growth rate shifted further; both agree at long wavelengths (§3.2, Fig. 4). **Shown**
12. Since the mean cell size relates to the fastest-growing modes, the dispersion relations imply smaller cells with FPV-$\kappa_c$ and smaller still with FPV-h than with DC (§3.2). **Derived** (from Fig. 4 and the cited result)
13. At a flame radius of about 6 cm, DC forms cells of nearly uniform size; FPV-h adds smaller secondary cells; FPV-$\kappa_c$ forms secondary cells too but fewer small cells (§3.3, Fig. 5). **Shown** (visual inspection, as printed)
14. The cell-size distributions peak at smaller sizes for both FPV models than for DC, consistently with the stability analysis (§3.3, Fig. 6). **Shown**
15. The most frequent (modal) DC cell wavelength is 7–8 flame thicknesses, larger than the about 6 of Berger et al. for planar flames; the authors attribute the difference to the curved configuration and the limited sample (§3.3). **Shown** / **Stated**
16. The perturbation amplitude shows three regimes (unperturbed propagation, linear growth, non-linear growth with interacting cells); in the linear regime both FPV models grow faster than DC (§3.3, Fig. 7). **Shown**
17. The two-dimensional flames follow the one-dimensional instability-free flame in the first two regimes and accelerate in the third; both FPV models propagate faster than DC owing to more small cells (§3.3, Fig. 7). **Shown**
18. Flame-speed deviations of 15% between the FPV models and DC appear at the largest radii; a similar overprediction was reported with a two-dimensional unstretched manifold by Schlup & Blanquart [17] (§3.3). **Shown** / **Stated**
19. Microstructure at a radius of about 6 cm: both FPV models predict richer mixtures than DC on the burned side, with a slight temperature overprediction; FPV-h predicts higher and broader OH; FPV-$\kappa_c$ only slightly overpredicts $Y_{\mathrm{OH}}$ at positive curvature, with a reaction-zone thickness similar to DC (§3.3, Fig. 8). **Shown**
20. $Y_{\mathrm{HO_2}}$ is non-negligible in negatively curved regions in all three computations; the heat-release marker $Y_{\mathrm{OH}}Y_{\mathrm{H_2}}$ is high at positive and low at negative curvature in all three (§3.3, Fig. 8). **Shown**
21. Both FPV models recover the unstretched laminar burning velocity very accurately (§4). **Stated** (no number given)
22. Including curvature in the manifold gives more accurate local characteristics and microstructure; the global characteristics of the two FPV models do not differ significantly (§3.3, §4). **Shown**
23. Supplementary: flame-tangential diffusion matters only in strongly negatively curved segments; FPV-$\kappa_c$ predicts normal and tangential diffusive fluxes better than FPV-h; both deviate where $\kappa_{\mathrm f}<-1500$ m$^{-1}$, outside the tabulated range (Supp. §1, Fig. S2). **Shown**
24. A manifold's ability to recover tangential diffusion correlates with its overall prediction of the thermochemical state (Supp. §1). **Stated** (from one segment)

# Printed slips

- **Ref. [15]:** title printed "Liminar premixed hydrogen/air counterflow flame simulations…".
- **Journal abbreviations:** "Proc. Combust. Instit." in [2] against "Proc. Combust. Inst." elsewhere; "Combust. Theor. Model." in [18] against "Combust. Theory Model." in [31].

# Notation map

The registry has no combustion symbols; the page-local symbols below follow [flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md), which keeps the model label FPV-$\kappa_c$ as FPV-$\kappa$.

| Böttler et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi$ | $\phi_{\mathrm{eq}}$ (page-local equivalence ratio) | the registry's $\phi$ is a generic field |
| $Z_{Bilger}$, $\beta$, $\gamma_l$ | $Z$, $\beta_{\mathrm B}$, $\gamma_l$ (page-local) | Bilger mixture fraction and coupling function, Eqs. 1–2; **collision:** $\beta$, $\gamma$ |
| $Y_k$, $Y_c=Y_{H_2O}-Y_{H_2}-Y_{O_2}$ | $Y_k$, $Y_c$ (page-local) | species mass fraction; progress variable |
| $c$, $c_2$ | $c$, $c_2$ (page-local) | normalized progress variable (Eq. 3) and H-radical progress variable (Eq. 4) |
| $h$ | $h_t$ (page-local) | **collision:** enthalpy, not the element size $h$ |
| $\psi$ | (tabulated thermochemical state) | |
| $\kappa_c=-\nabla\cdot\boldsymbol n_c$ | $\kappa_{\mathrm f}=-\nabla\cdot\boldsymbol n_{\mathrm f}$ (page-local) | **collision:** flame curvature, not the von Kármán constant; positive convex towards the unburned mixture |
| $K_s=\nabla_t\cdot\boldsymbol u_t-(\boldsymbol u\cdot\boldsymbol n_c)\kappa_c$ | $K_{\mathrm f}$ (flame strain rate, page-local) | **collision** with $K$; the source calls it strain although it contains a curvature term |
| $l_f$, $\tau_f=l_f/s_L$, $s_L$ | $l_{\mathrm F}$ (thermal flame thickness, page-local); flame time, laminar burning velocity | $l_{\mathrm F}=(T_b-T_u)/\max\lvert dT/dx\rvert$ |
| $\omega$, $k$, $\lambda$ | (growth rate, perturbation wavenumber, wavelength) | **collisions:** not the specific dissipation, turbulent kinetic energy or Taylor microscale |
| $\lambda_{cell}=2l_{arc}/\pi$ | (cell size) | |
| $A_0$, $A_{max}$, $R_f$, $s_f$ | (perturbation amplitudes, flame radius, flame speed) | |
| $N$ | (cells per histogram bin) | **collision:** not the polynomial degree |
| DC | detailed-chemistry resolved reference | a laminar computation, not DNS of turbulence |

# Reference list

32 printed references, numbered ([1]–[32]), DOIs printed for all but [20].
The list is merged complete into the [bibliography](/bibliography.md) with
`citedby` bottler-2023. Wen et al. part I [23] and part II [28] take
suffixes in printed order; [19], [23] and [28] print an article number and
no volume; [30] is the ULF software with a figshare DOI. No cited work is an
ingested source. No printed duplicates or unparseable items.

# Pages created or updated

Chunk 5 (2026-10-26). This source is cited on:

- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
