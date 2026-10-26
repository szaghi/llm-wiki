---
type: Source
title: "Domingo & Vervisch (2023) — Recent developments in DNS of turbulent combustion"
description: "Invited review of direct numerical simulation of turbulent flames from 2017 to 2022: resolution limits in Re_T, Da and Ka, DNS embedded in LES as a closure test bed (deconvolution, CNN closures), flame-resolved burner simulations, and the downsizing of real geometries."
resource: "doi:10.1016/j.proci.2022.06.030"
source_kind: paper
authors: [Domingo P., Vervisch L.]
year: 2023
venue: "Proc. Combust. Inst. 39:2055-2076"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Proceedings_of_the_Combustion_Institute_Domingo_Recent_developments_in_DNS_of_turbulent_combustion.pdf"
tags: [dns, review, combustion, les, a-priori-a-posteriori, machine-learning]
timestamp: 2026-10-25T13:42:00Z
---

# Summary

Domingo & Vervisch (2023) review [direct numerical simulation](/definitions/direct-numerical-simulation.md)
of turbulent flames, mostly the literature of 2017–2022. The bundle reads it at its periphery:
turbulent combustion is the subject, and turbulence enters as an ingredient. The authors first
state the resolution limits. A mesh spacing $h=2\eta$ resolves the dissipative range, so a box of
side $L_o$ needs $N_{\mathrm{pts}}=(L_o/2L)^3Re_T^{9/4}$ points. With $Da\,Ka\approx Re_T^{1/2}$ this
becomes $N_{\mathrm{pts}}=(L_o/2L)^3\,Da\,Ka\,Re_T^{7/4}$, so high $Re_T$, $Da$ and $Ka$ cannot be
reached together and a DNS box spans only a few integral scales (the grid-count side of
[grid-point requirements](/results/les-grid-point-requirements.md)). A census follows (about 80, 140
and 200 flame-DNS papers in 2007–2011, 2012–2016 and 2017–2021), together with a list of DNS codes
and their orders of accuracy. The review also defines "quasi-DNS".

Three lines of the authors' own work illustrate the trends. (1) **DNS embedded in
[LES](/definitions/large-eddy-simulation.md):** a well-resolved LES of a premixed Bunsen jet (subgrid
momentum flux closed by the [Vreman model](/methods/vreman-model.md)) carries a nested 50 µm DNS
box. The box serves as a test bed for
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md): approximate
deconvolution, a structural closure related to
[scale-similarity models](/methods/scale-similarity-model.md), is compared with flamelet-tabulated
deconvolution, and convolutional neural networks are trained for the filtered source and the
unresolved scalar fluxes (about 1% maximum error at trained filter sizes, 16% at an untrained one).
A 1.6-billion-cell flame-resolved simulation of the Cambridge/Sandia bluff-body burner supplies
regime diagrams. (2) **DNS as a test bed for numerics:** neural-network chemistry runs 25 times
faster than detailed chemistry in a syngas wall-flame DNS. (3) **Downsizing:** every length is
scaled by $s<1$ with the fluid properties and velocities kept, so
$Re_T^\star=sRe_T$ and $\eta^\star=s^{1/4}\eta$. Chemical times are
rescaled to keep either $Da$ or $Ka$. A downsized quasi-DNS of a 10 MW incinerator led to an
injection redesign. The review closes with carbon-footprint estimates of a DNS run.

# Version read

HAL author manuscript hal-03784205v1 (deposited 22 September 2022; the cover gives the journal
reference as "In press"). It is the authors' LaTeX manuscript, paginated 1–22, plus the HAL cover:
23 PDF pages, of which the text fills pp. 1–13 and the references pp. 13–22. It is not the journal
typeset, and the journal pagination 2055–2076 cannot be checked against this copy. Title and
authors match the published version; the metadata above are those of the published version
(Crossref). On pp. 2–3 the text layer is overprinted by the text layers of reprinted figures, so
those pages were read visually. Section, equation and page numbers on this page are those of the
manuscript.

# Key claims

1. A mesh resolution $h=2\eta$ suffices to capture the dissipative range (citing Moin & Mahesh). The number of points in a volume $L_o^3$ is $N_{\mathrm{pts}}=(L_o/2\eta)^3=(L_o/2L)^3Re_T^{9/4}$, with $Re_T=k^{1/2}L/\nu\approx(L/\eta)^{4/3}$ (§2, Eqs. 1–2). **Stated** ($h=2\eta$) / **Derived** (scaling).
2. A gas-turbine swirl burner with $Re_T\sim1500$ and $L\sim5$ mm needs "more than 10 billon mesh points" to resolve $10^3$ cm³ of shear layer (§2). **Derived**. *(Compiler check, not in the sources: Eq. 2 with $L_o=10$ cm gives $10^3\times1500^{9/4}\approx1.4\times10^{10}$, consistent.)*
3. $Da\,Ka\approx Re_T^{1/2}$ (Eq. 5), hence $N_{\mathrm{pts}}=(L_o/2L)^3\,Da\,Ka\,Re_T^{7/4}$ (Eq. 6). DNS cannot explore high $Da$ and high $Ka$ together. At fixed $Da$, $Re_T\approx Ka^2$, so raising $Ka$ by a factor $a$ requires raising $Re_T$ by $a^2$ (§2). **Derived**.
4. Canonical DNS (planar flames in homogeneous or shear turbulence) spans only a few integral scales ($L_o\simeq L$), which limits the range of flame-wrinkling lengths. Many DNS are at low Reynolds number with $L$ of the order of the flame thickness, which "may partially" explain why few DNS-derived closures have reached engineering codes (§1, §2). **Stated**.
5. A priori tests (models fed exact, frozen DNS inputs) "cannot always allow for reaching definitive conclusions", because they miss error accumulation and error compensation in time (§1). **Stated**.
6. The number of published gaseous-flame DNS papers grew roughly linearly: about 80 (2007–2011), 140 (2012–2016), 200 (2017–2021) (§1). **Stated** (the authors' census).
7. DNS codes and their orders, as listed: SENGA, DINO, S3D, FK³, KARFS and HOLOMAC are 6th to 10th order; Nek5000 uses spectral elements; NGA, PsiPhi, AVBP and OpenFOAM are 4th or 2nd order (§1). **Stated**.
8. "Quasi-DNS" (or "flame resolved-DNS"), quoted from Zirwes et al., is "a model-free simulation which does not fulfill all of the strict requirements of a DNS … but is accurate enough so that the results of a full DNS are expected to be similar". Its numerical dissipation needs careful calibration (§1). **Stated**.
9. Finite-volume high-order spectral-element methods "will become a standard" for fully resolved simulations in real geometries (§1). **Stated** (forecast).
10. DNS embedded in LES lets the flame see shear-layer turbulence developed by the burner instead of synthetic fluctuations. The streamwise extent of the DNS zone is set with the flame-brush growth law (Eq. 7); the brush adjusts in about half an eddy turnover time. In the example the eddy turnover time is about 1.13 ms at the DNS-zone entry and the residence time in the refined mesh about 2 ms (§3.1). **Shown/Derived**.
11. The embedded-DNS case: Bunsen jet with $D=12$ mm, $Re=24{,}000$, bulk velocity 30 m/s, $U'/S_L=5$ and $3<Ka<5$ in the DNS zone. The LES mesh has about 171 million nodes over $16D\times8D\times8D$ at about 150 µm; the DNS box at $x/D=4.5$ has 28.58 million nodes over 12 mm × 18 mm × 18 mm at 50 µm; $\delta_L\approx400$ µm and the measured Kolmogorov scale is about 50 µm (§3.1, Fig. 4). **Shown**.
12. Concave scalar geometries (towards the fresh reactants) prevail ahead of the burning region, and convex ones are more probable in the products (§3.1). **Shown** (in cited work).
13. The error of one-dimensional flamelet-tabulated deconvolution grows with the subgrid flame wrinkling $\Xi$; for each filter size $0.75<\Delta/\delta_L<3$ there is a threshold $\Xi$ beyond which the error stays almost constant (§3.1, Fig. 5). **Shown**.
14. A posteriori tests, run by coarsening the DNS zone to LES ($170$ µm $<\Delta<640$ µm), show that flamelet-based (1D) deconvolution overestimates CH₄ and O₂ consumption more than 3D approximate deconvolution, and enhances the CO overestimation (§3.1, Fig. 6). **Shown**.
15. Convolutional neural networks trained on the embedded DNS ($\Delta=0.3$ and $0.9$ mm) predict the filtered progress-variable source "very well": maximum error about 1% on the trained database and 16% on untrained filter sizes, against up to 25% for 1D tabulated-flame deconvolution at $\Delta=3\delta_L$ (§3.1, Fig. 9). **Shown** (in cited work of the authors' group).
16. A flame-resolved simulation of the Cambridge/Sandia lean premixed bluff-body burner used 1.6 billion cells at 100 µm, "about twice the Kolmogorov scale", and is validated against measured mean and RMS velocity, temperature and CO (§3.2, Figs. 10–11). **Shown** (in cited work).
17. Regime diagrams conditioned on height and progress variable show that the combustion regime of the bluff-body burner is "not unique": the unburned side lies in the thin-reaction-zone regime, larger progress shows corrugated flamelets, and some distributions are multi-modal (§3.2, Fig. 12). **Shown** (in cited work).
18. Neural-network chemistry trained off-line on a non-adiabatic, non-premixed micro-mixing problem agrees with detailed and reduced chemistry in DNS of a syngas oxy-flame with a cooled wall, and is "25 times faster in terms of CPU cost than the detailed mechanism and 3 times faster than the reduced mechanism having the same number of species" (§4, Figs. 13–14). **Shown** (in cited work).
19. DNS is the right test bed for new numerical procedures because it excludes interference between numerics and subgrid-scale models (§4). **Stated**.
20. Downsizing: scaling every length by $s<1$ with fluid properties, velocities and mass-flow ratios kept leaves $k$ unchanged and gives $Re_T^\star=sRe_T$, $\eta^\star=s^{1/4}\eta$, $\varepsilon^\star=\varepsilon/s$, $\tau_T^\star=s\tau_T$, $\tau_\eta^\star=s^{1/2}\tau_\eta$ and a residence time $\tau_R^\star=s\tau_R$ (§5, Eqs. 13–18). **Derived**.
21. Keeping $Da$ requires $\tau_c^\star=s\tau_c$ (all pre-exponential factors multiplied by $s^{-1}$); keeping $Ka$ requires $\tau_c^\star=s^{1/2}\tau_c$; both cannot hold. The choice follows the local ratio of a scalar length $\ell_\phi$ to a flow length $\ell$: linear scaling for $\ell_\phi\ll\ell$, square-root scaling for $\ell_\phi\gg\ell$, a "dynamic rescaling" (§5, Eqs. 19–21). **Derived**.
22. A $s=1/30$ downsized quasi-DNS of a 10 MW SNCR incinerator (16.0 m long, 4.45 m in diameter) used $h=150$ µm in the shear layers, 162 million cells, a fourth-order unstructured solver and reduced chemistry. It resolves mixing that a full-size LES with the same node count (5 mm resolution) cannot. A modified cooling-water injection raised the DeNOx efficiency by 7%, "also observed in the real system" (§5, Figs. 15–17). **Shown** (in cited work) / **Stated** (plant confirmation).
23. Downsized DNS was also applied to a rapid compression machine, to quantify wall heat transfer and the effect of weak pressure waves on undesired ignition (§5, Fig. 18). **Stated** (cited).
24. A 2-billion-cell low-Mach DNS with tabulated chemistry, run one week on 10,000 cores (about 1.68 million core hours) in France, emits 776 kg CO₂e, about 6000 km by car at 130 g/km or 70 tree-years; the same run emits 255 kg in Vancouver and 11,000 kg on coal electricity; a full life-cycle account raises the compensation to "up 500 years" of tree sequestration (§6). **Stated** (computed with cited calculators). *(Compiler check, not in the sources: $168\times10^4=1.68\times10^6$ core hours and $776/0.130\approx5970$ km, consistent.)*
25. The boundary between DNS and high-fidelity LES is "getting progressively blurred", because combustion chambers are shorter than 1 m and free of high-Reynolds-number wall boundary layers (§7). **Stated**.
26. Physics-informed techniques coupling PDE solution and network training "will certainly soon open new perspectives in combustion DNS" (§7). **Stated** (forecast).

# Printed slips

- Fig. 12 caption: "bout: c ∈ [0, 8, 0.98]"; the neighbouring bands (pheat $[0.6,0.8]$, burned $[0.98,0.99]$) show it is $[0.8,0.98]$.
- §3.1 after Eq. (7): "Because $C_s\approx2$ [254], the mean turbulent flame brush adjusts to turbulence with a characteristic time of the order of half the eddy turnover time ($b_2$ = 1.78)". By Eq. (7) the relaxation time is $\tau_T/C_s$, so the half follows from $C_s\approx2$; the parenthetical "$b_2=1.78$" repeats the growth constant out of place.
- Eq. (8) and the text after it: the diffusivity is $D_\phi$ in Eq. (8) and in $\tau_T=\Delta^2/(24D_\phi)$, but the text then names "$D_c$ the molecular diffusion coefficient". The same passage reuses $\tau_T$ for a micro-mixing time (the integral time of Eq. 3), and Eq. (10) reuses $\tau_c$ for an unresolved flux (the chemical time of §2).
- §1: the premixed-flame citation range is printed "[21, 27, 37, 38, 41–43, 49–75, 75–190]", counting ref. 75 twice.
- §3.1: a box of 12 mm × 18 mm × 18 mm at a "fixed resolution of 50µm" is given as "28.58 million nodes". *(Compiler check, not in the sources: $240\times360\times360\approx3.11\times10^7$; the paper does not say how nodes are counted, so the difference is recorded, not asserted as a slip.)*
- Reference list: [24] prints "J. Comput. Phys. 1 (101) (1992)", with 1 in the volume position and 101 in the issue position; the volume, year and page data of [244] and [245] are flagged for verification on Crossref, not asserted as exchanged; [236] prints pages "433459" and [275] "331?356".

# Notation map

| Domingo & Vervisch (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\eta_k$ | $\eta$ | Kolmogorov length |
| $\ell_T$ | $L$ | integral length scale |
| $\epsilon$ | $\varepsilon$ | dissipation rate |
| $k$ | $k$ | defined density-weighted: $\langle\rho\rangle k=\tfrac12\langle\rho u_iu_i\rangle-\tfrac12\langle\rho u_i\rangle\langle\rho u_i\rangle/\langle\rho\rangle$ (§2) |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | Reynolds average, used only in the definition of $k$ |
| $h$ | $h$ | mesh spacing; in Eq. (12) the LES mesh size |
| $N$ | $N_{\mathrm{pts}}$ (local) | **collision:** registry $N$ is the polynomial degree; here a total point count, and in Eq. (11) the number of stencil points |
| $L_o$ | $L_o$ (local) | side of the computational box |
| $Re_T=k^{1/2}\ell_T/\nu$ | $Re_T$ (local) | turbulent Reynolds number on $k^{1/2}$ and $L$ |
| $Da$, $Ka$ | $Da$, $Ka$ (local) | Damköhler $\tau_T/\tau_c$, Karlovitz $\tau_c/\tau_\eta$ |
| $\tau_T$, $\tau_k$ | $k/\varepsilon$, $\tau_\eta$ | integral and Kolmogorov times; $\tau_T$ also reused for the micro-mixing time $\Delta^2/(24D_\phi)$ |
| $\tau_c$ | $\tau_c$ (local) | chemical time (§2), as on the DNS page; the source reuses $\tau_c$ for the unresolved convective flux of Eq. (10) |
| $\tau_D$ ($\tau_{D_c}$), $\tau_c$ | — | unresolved diffusive and convective fluxes of the progress variable, Eqs. (9)–(10); not the SGS stress $\tau_{ij}$ |
| $\overline{\phi}$, $\tilde\phi$ | $\bar\phi$, $\tilde\phi$ | LES filter and Favre filter, as in the registry |
| $\Delta$ | $\Delta$ | filter size, quoted in µm, mm or units of $\delta_L$ |
| $C_s$ | — | **collision:** flame-brush growth constant ($\approx2$) of Eq. (7), not the Smagorinsky coefficient |
| $b_2$ | — | flame-brush growth constant (1.78) |
| $\delta_T$, $\delta_L$ | — | flame-brush thickness, laminar flame thickness; not the boundary-layer $\delta$ |
| $\beta$ | $s$ (local) | downsizing factor, as on the [DNS](/definitions/direct-numerical-simulation.md) page; **collision** with the field-inversion $\beta(\boldsymbol x)$ |
| $(\cdot)^\star$ | — | quantity of the downsized model |
| $\mathcal S_{ij}$ | $S_{ij}$ | strain-rate tensor of Eq. (21); the norm convention of $\lvert\mathcal S\rvert$ is not stated |
| $\Xi$ | — | subgrid flame wrinkling $\overline{\lvert\nabla c\rvert}/\lvert\nabla\bar c\rvert$ |
| $\widetilde{\mathcal L}_\Delta$, $\widetilde{\mathcal L}^{-1}_\Delta$ | — | numerical filter and inverse-filter deconvolution (Fig. 7) |
| $D_\phi$, $D_c$ | — | molecular diffusivity, used interchangeably around Eq. (8) |

# Reference list

284 printed references in numbered style, in order of first citation, all merged into the
[bibliography](/bibliography.md) with `citedby` this slug. Four works are printed twice under two
numbers ([28]=[219], [148]=[231], [159]=[226], [168]=[228]) and are folded into one entry each.
Ref. [167] (Liu & Wang, Combust. Flame 238, 2022) is a different work from the bundle's planned
source of slug `liu-2022` and takes a disambiguated key. Undated web items (SENGA, FK³, AVBP,
Nek5000, OpenFOAM, Green Algorithms) carry the printed "(2021)". Odd author strings ([25], [281],
[283]) are kept as printed; no item is unparseable.

# Pages created or updated

Chunk 1 (2026-10-25), cited further in chunks 2, 3, 5, 6. This source is cited on:

- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
- [Physics-informed neural networks for RANS](/methods/physics-informed-neural-network.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Vreman model](/methods/vreman-model.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [Nek5000 and NekRS](/software/nek5000.md)
- [OpenFOAM](/software/openfoam.md)
