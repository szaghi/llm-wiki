---
type: Source
title: "Jakhar et al. (2026) — Analytical and AI-Discovered Stable, Accurate, and Generalizable Subgrid-Scale Closure for Geophysical Turbulence"
description: "Sparse Bayesian equation discovery of subgrid closures for forced two-dimensional turbulence, selected by a criterion that adds the inter-scale energy transfer and its backscatter part, recovers the fourth-order Taylor truncation of the gradient model; it is stable a posteriori, captures backscatter and extremes, and has no tunable coefficient."
resource: "doi:10.1103/v28b-5qmp"
source_kind: paper
authors: [Jakhar K., Guan Y., Hassanzadeh P.]
year: 2026
venue: "Phys. Rev. Lett. 136:064201"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_Physical_Review_Letters_Jakhar_Analytical_and_AI-Discovered_Stable_Accurate_and_Generalizab.pdf"
tags: [les, sgs-model, symbolic-regression, backscatter, a-priori-a-posteriori, data-driven]
timestamp: 2026-10-26T20:50:00Z
---

# Summary

Jakhar et al. (2026) ask what an "ideal" subgrid closure for
[LES](/definitions/large-eddy-simulation.md) of two-dimensional
(geophysical) turbulence must do: reproduce the structure of the subgrid
stress (a priori pattern correlation), reproduce the inter-scale energy
and enstrophy transfers including
[backscatter](/definitions/energy-backscatter.md), and give a posteriori
statistics (spectra, extremes) that match DNS
([a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).
The Clark [gradient model](/methods/gradient-model.md), here NGM2, meets
the first condition (correlation above 0.9) but has zero inter-scale energy
transfer in 2-D and gives unstable LES; eddy-viscosity closures
([Smagorinsky](/methods/smagorinsky-model.md), dynamic Smagorinsky and
dynamic Leith through the [dynamic procedure](/methods/dynamic-procedure.md))
are stable but purely and excessively diffusive.

The method is [symbolic-regression](/methods/symbolic-regression-closure.md)
equation discovery by a relevance vector machine (sparse Bayesian linear
regression) over a 930-term library of products of filtered velocity,
vorticity and strain derivatives up to total order 8, with material
derivatives as memory terms, trained on 100 snapshots of Gaussian-filtered
[DNS](/definitions/direct-numerical-simulation.md), coarse-grained to
LES grids "4 to 64× coarser" (p. 2). With the conventional
selection criterion (correlation of $\tau_{ij}$ against the sparsity
threshold) the elbow of the L-curve is NGM2. The new criterion takes the
minimum of the correlations of $\tau_{ij}$, of the inter-scale energy
transfer and of its positive and negative parts; its elbow is a 5-term
closure the authors identify as the fourth-order Taylor (Gaussian-filter)
truncation, NGM4, and a 9-term NGM6 follows. Memory terms never appear.

In four cases of forced 2-D turbulence (one on a $\beta$-plane, one at
$Re=10^5$), NGM4 and NGM6 reach correlations near 0.99, reproduce the
enstrophy transfer and 62 % and 78 % of the mean energy transfer, with
backscatter, where eddy-viscosity closures have the wrong sign. They are
stable a posteriori when the LES resolves over 80 % of the DNS enstrophy
(compared with the 80 %-of-energy rule of 3-D LES, see
[LES grid-point requirements](/results/les-grid-point-requirements.md)),
capture vorticity extremes and forecast better; NGM2 is always unstable.
NGM4 depends on second derivatives and so violates the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md); the authors
read the gradient models as local truncations of the nonlocal deconvolution
behind [scale-similarity models](/methods/scale-similarity-model.md),
contrast the interpretable closure with
[neural-network SGS models](/methods/neural-network-sgs-model.md), and
propose it as a target where weather and climate models rely on
[implicit LES](/definitions/implicit-les.md).

# Version read

arXiv preprint 2509.20365v3 [physics.ao-ph], 1 January 2026 (header dated
5 January 2026), REVTeX preprint layout; 11 pages (main text, references,
End Matter Appendices A–D, Fig. 4), all read, pages 2, 3, 10, 11 checked
visually. The metadata above are those of the published version (Phys.
Rev. Lett. 136:064201, 2026), whose content was not seen. The page-1 title
carries a leading "An" and different capitalization; authors match. The
Supplemental Material is cited with a placeholder URL and is **not** in the
file: Figs. S1–S5, Tables S1–S2, the definitions of the inter-scale
transfers and the generalized Taylor expansion were not read, and claims
resting on them are marked. Numbering on this page is that of arXiv v3.

# Key claims

Page-local symbols: $P_\tau$ and $P_Z$ the inter-scale energy and
enstrophy transfers by the subgrid stress (defined in the Supplemental
Material, not read; printed sign: $P_\tau>0$ "diffusion", $P_\tau<0$
backscatter, as for $\Pi$); CC the domain-averaged correlation coefficient
(Eq. 5); $\alpha_{\mathrm{RVM}}$ the sparsity threshold of the relevance
vector machine (higher means more terms); $\tau^{\mathrm{NGM}n}_{ij}$ the
gradient model truncated at order $\Delta^n$; $\bar\omega_z$ the filtered
(scalar) vorticity; $N_{\mathrm{LES}}$, $N_{\mathrm{DNS}}$ grid points per
direction; ratios $\langle P_\tau\rangle/\langle P_\tau^{\mathrm{FDNS}}\rangle$
against filtered DNS.

1. Structural closures such as NGM2 meet the structure condition with "above 0.9 pattern correlation with filtered DNS (FDNS)" but produce no inter-scale energy transfer in 2-D and unstable LES (p. 1). **Stated** (cited)
2. Eddy-viscosity closures (Smagorinsky, Leith) give stable LES but are "often overly dissipative and miss backscattering", degrade extremes and fail the structure condition, "e.g., lower than 0.5 pattern correlation" (p. 1). **Stated** (cited)
3. NGM2 gives exactly zero inter-scale energy transfer in 2-D, $P_\tau^{\mathrm{NGM2}}=0$ ("NGM2 captures neither diffusion nor backscattering"), the instability cause suggested by Jakhar et al. (2024) (p. 3; Fig. 2 table gives the ratio 0). **Stated** / **Shown**
4. The library has 930 terms: derivative orders $0\le q\le8$, powers $0\le p\le2$, total derivative order at most 8; high-order derivatives are computed with arbitrary-precision methods (p. 2, Eq. 3). **Stated**
5. With the conventional criterion (CC of $\tau_{ij}$ against $\alpha_{\mathrm{RVM}}$) CC rises from 0 and plateaus near 1, and the elbow (2 terms) robustly recovers NGM2, consistent with Zanna & Bolton (2020) and Jakhar et al. (2024) (pp. 2–3, Fig. 1a). **Shown**
6. With the physics-informed criterion (minimum CC of $\tau_{ij}$, $P_\tau$, $P_\tau>0$, $P_\tau<0$) the L-curve has no elbow at NGM2 but at a 5-term closure with CC of $\tau_{ij}$ above 0.99 and non-zero energy transfer: NGM2 plus the $O(\Delta^4)$ Taylor term, NGM4 (p. 3, Fig. 1b, Eq. 4). **Shown**
7. Increasing $\alpha_{\mathrm{RVM}}$ further gives a 9-term closure with negligible CC gain, identified as NGM6; at $\alpha_{\mathrm{RVM}}\sim10^5$ about 100 terms (p. 3, Fig. 1a). **Shown**
8. The L-curves of Fig. 1 "are consistently observed for all cases with any other $N_{\mathrm{LES}}$" (p. 3). **Stated** (shown for four case–resolution pairs)
9. The discovery "confirms that Taylor-series expansion offers the best representation of both $\tau_{ij}$ and the inter-scale energy transfer"; "the memory terms never emerged during the discovery" (p. 3). **Shown**
10. A priori ratio $\langle P_\tau\rangle/\langle P_\tau^{\mathrm{FDNS}}\rangle$ (mean ± s.d. over Cases 1–2 at $N_{\mathrm{LES}}=128$ and Cases 3–4 at $512$): NGM2 0; NGM4 $0.62\pm0.04$; NGM6 $0.78\pm0.04$; Smagorinsky $-62.24\pm37.80$; dynamic Smagorinsky $-28.48\pm15.38$; dynamic Leith $-6.91\pm2.73$ (Fig. 2 table). **Shown**
11. A priori ratio $\langle P_Z\rangle/\langle P_Z^{\mathrm{FDNS}}\rangle$: NGM2, NGM4, NGM6 all $1.00\pm0.01$; Smagorinsky $-3.22\pm1.18$; dynamic Smagorinsky $-1.49\pm0.45$; dynamic Leith $-0.37\pm0.06$ (Fig. 2 table). **Shown**
12. NGM4 and NGM6 "perfectly capture the structure of the FDNS SGS stress and inter-scale enstrophy transfers, and very well capture the inter-scale energy transfers (both diffusion and backscattering)"; eddy-viscosity closures are "purely and excessively diffusive (as indicated by the negative CC values)" (pp. 3–4, Fig. 2). **Shown**
13. NGM4 and NGM6 capture the energy backscatter of filtered DNS (p. 3). **Shown**
14. A priori NGM4 and NGM6 are "fairly comparable, though NGM6 has a better $P_\tau$" (p. 4, Table S1). **Shown** (Supplemental Material, not read)
15. LES with NGM4 and NGM6 "remain long-term stable when the LES resolution is high enough to capture over 80% of DNS enstrophy" (Fig. S2), compared with 3-D LES needing at least 80 % of the DNS kinetic energy (p. 4). **Shown** (Supplemental Material, not read) / analogy **Stated**
16. "Using NGM2 for any case and any LES resolution leads to instabilities" (p. 4). **Shown** (stated as a result; no main-text figure)
17. When stable, LES with NGM4/NGM6 capture both bulk and tails of the vorticity PDF; eddy-viscosity LES fail to capture extremes, "especially for Cases 3 and 4, which have high-wavenumber forcings" (p. 4, Fig. 3a–b, Figs. S3–S4). **Shown**
18. LES with NGM4/NGM6 outperform eddy-viscosity closures in short-term forecasts of vorticity (pattern CC against time in eddy-turnover units) (p. 4, Fig. 3a–b insets). **Shown**
19. LES with NGM4/NGM6 better capture domain-averaged kinetic energy and enstrophy (p. 4, Table S2). **Shown** (Supplemental Material, not read)
20. Spectral tails do not discriminate between closures; at low wavenumbers eddy-viscosity LES underestimate the large-scale enstrophy, "likely due to the excessive diffusion", and likewise the energy spectra (p. 4, Fig. 3c–d, Fig. S5). **Shown** (cause **Stated**)
21. A posteriori NGM4 and NGM6 perform "fairly similar[ly]", "suggesting that in practice, using NGM4 might be enough"; NGM6 also represents the Reynolds stress but shows no a posteriori advantage in stability or accuracy (pp. 4–5). **Shown**
22. NGM4 represents the Leonard and cross stresses and is therefore "interpretable" (p. 4). **Derived** (in the Supplemental Material, not read)
23. NGM4 is "generalizable" because its coefficients "are entirely determined by the filter width ($\Delta$)", with no $Re$- or parameter-dependent part (p. 4). **Stated** (argument from form)
24. "NGM4 is accurate: it is the first closure to simultaneously excel in both a priori and a posteriori tests" (p. 4). **Stated**
25. "The analytical expansion of the gradient model to higher-order terms had not been previously pursued"; "It was only after the AI-based discovery that the connection with higher-order Taylor-series expansion became clear" (pp. 4–5). **Stated** (the reference list includes Eyink's "Multi-scale gradient expansion of the turbulent stress tensor" and Carati, Winckelmans & Jeanmart)
26. NGM4 and NGM6 violate the Boussinesq hypothesis since they depend on second-order velocity gradients (p. 5). **Stated**
27. Finite-order gradient closures are truncations of the nonlocal deconvolution operator; NGM4 is "the minimal local truncation" capturing the leading nonlocal effects the criteria require; Padé-like rational approximations or nonlocal kernels are natural extensions (p. 5). **Stated**
28. Where weather and climate models use implicit LES, NGM4 can serve as a diagnostic target for inter-scale transfers and extremes, or be combined with the discretization when explicit backscatter is wanted (p. 6). **Stated**
29. Coarse-graining any quadratic nonlinearity can lead to an NGM-like representation, e.g. the heat flux in Rayleigh–Bénard convection (p. 6). **Stated**

The closures (Eq. 4), with the filter width $\Delta$ twice the LES grid
spacing:

$$\tau_{ij}^{\mathrm{NGM6}}=\underbrace{\underbrace{\frac{\Delta^2}{12}\,\partial_k\bar u_i\,\partial_k\bar u_j}_{\tau_{ij}^{\mathrm{NGM2}}}+\frac{1}{2!}\frac{\Delta^4}{12^2}\,\partial_k\partial_l\bar u_i\,\partial_k\partial_l\bar u_j}_{\tau_{ij}^{\mathrm{NGM4}}}+\frac{1}{3!}\frac{\Delta^6}{12^3}\,\partial_k\partial_l\partial_m\bar u_i\,\partial_k\partial_l\partial_m\bar u_j+O(\Delta^8).$$

The eddy-viscosity baselines (App. D) are $\tau_{ij}=-2\nu_t\bar S_{ij}$ with
$\nu_t=(C_s\Delta)^2\lvert\bar S\rvert$, $C_s=0.17$ (credited to Lilly 1967),
and Leith's $\nu_t=(C_l\Delta)^3\lvert\nabla\bar\omega_z\rvert$ ($C_l$
page-local), the dynamic versions with positive clipping $\nu_t\ge0$.

# Printed slips

- **App. B heading (p. 10):** "Correlation coefficienct".
- **Fig. 4 caption (p. 11):** "$(k_x,k_y)$ are the wavenumbers of the time-invariant forcing", while the panels print $(k_{fx},k_{fy})$.
- **Supplemental Material:** cited as "See Supplemental Material at [URL]" with the placeholder unfilled.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\overline{(\cdot)}$ | $\bar\phi$ | Gaussian LES filter |
| $\bar u_i$, $\bar p$, $Re$ | $\bar u_i$, $\bar p$, $Re$ | 2-D, $i=1,2$, both directions horizontal; non-dimensionalization in Jakhar et al. (2024) |
| $Q_i$ | $f_i$ | time-invariant forcing, Rayleigh drag and Coriolis force |
| $\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$ | $\tau_{ij}$ | full, positive trace |
| $\Delta$ | $\Delta$ | twice the LES grid spacing |
| $\bar S_{ij}$, $\sqrt{2\bar S_{ij}\bar S_{ij}}$ | $\bar S_{ij}$, $\lvert\bar S\rvert$ | |
| $\nu_e$ | $\nu_t$ | |
| $C_s=0.17$, $C_l$ | $C_s$, $C_l$ (page-local) | Smagorinsky and Leith coefficients |
| $\omega$, $\bar\omega$ (printed $\varpi$) | $\omega_z$, $\bar\omega_z$ (page-local) | scalar 2-D vorticity; **collision:** $\omega$ is the specific dissipation rate, $\varpi^\pm$ the Elsasser vorticities |
| $E=\frac12u_iu_i$, $Z=\frac12\omega^2$, $\hat E(k)$, $\hat Z(k)$ | (energy, enstrophy), $E(k)$, $Z(k)$ | **collision:** $E$ is the total energy; the hat is not a test filter |
| $P_\tau$, $P_Z$ | $P_\tau$, $P_Z$ (page-local) | inter-scale energy and enstrophy transfer; sign of $P_\tau$ as for $\Pi$; **collision:** not the production $P_k$ |
| $\alpha$ | $\alpha_{\mathrm{RVM}}$ (page-local) | sparsity threshold; **collision:** $\alpha$ is the DG/FV blending factor |
| $\boldsymbol\Phi$, $\boldsymbol c$ | (library, weights) | |
| $(k_{fx},k_{fy})$, $\beta$ | (forcing wavenumbers), $\beta_{\mathrm{C}}$ (page-local) | $\beta$-plane Coriolis gradient; **collision:** $\beta(\boldsymbol x)$ is the field-inversion multiplier |
| $t_\eta=1/\sqrt{\langle\omega^2\rangle}$ | (eddy-turnover time) | **collision:** not the Kolmogorov time $\tau_\eta$ |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | domain average |

# Reference list

91 printed references, numbered style (APS); [88]–[91] are cited only
through the Supplemental Material. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Duraisamy et
al. (2019), Kang et al. (2023), Bae & Koumoutsakos (2022) and Kurz et al.
(2023) are the ingested sources of those keys. The paper's own
Supplemental Material [73] and the undated GitHub code [86] would take this
source's key and are keyed `jakhar-2026-b` and `jakhar-2026-c`; Jakhar
(2024) items take suffixes in printed order. Preprints (Guan et al. 2024,
Wang et al. 2025, Cranmer 2023, Dong et al. 2025) are separate entries.
[10], [45], [57] and [84] print no volume. None is unparseable; no printed
duplicates.

# Pages created or updated

Chunk 7 (2026-10-26). This source is cited on:

- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Gradient (Clark) model and the clipping of structural SGS models](/methods/gradient-model.md)
- [Neural-network subgrid-scale models](/methods/neural-network-sgs-model.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Symbolic-regression turbulence closures](/methods/symbolic-regression-closure.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
