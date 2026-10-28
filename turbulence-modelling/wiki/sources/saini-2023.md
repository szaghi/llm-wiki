---
type: Source
title: "Saini et al. (2023) — Numerical Dissipation Rate Analysis of Finite-Volume and Continuous-Galerkin Methods for LES of Combustor Flow-Field"
description: "Extends the a posteriori numerical-dissipation-rate analysis to explicit (WALE) and spectral-vanishing-viscosity LES and finds that numerical dissipation dominates the non-viscous dissipation of both a second-order finite-volume and a fifth-order continuous-Galerkin LES, the high-order gain coming mainly from lower numerical dissipation."
resource: "doi:10.1007/s10494-023-00428-z"
source_kind: paper
authors: [Saini V., Xia H., Page G.]
year: 2023
venue: "Flow Turbul. Combust. 111:81-113"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Flow_Turbulence_and_Combustion_Saini_Numerical_Dissipation_Rate_Analysis_of_Finite-Volume_and_Con.pdf"
tags: [numerical-dissipation, implicit-les, spectral-vanishing-viscosity, high-order, les]
timestamp: 2026-10-26T07:41:00Z
---

# Summary

Saini et al. (2023) ask why a high-order LES beat a second-order one at
equal cost in the authors' earlier comparison (Saini et al. 2022, AIAA J.):
a second-order finite-volume LES (OpenFOAM v1712, `pimpleFoam`,
[WALE model](/methods/wale-model.md) with $C_w=0.325$) against a
polynomial-order-4 continuous-Galerkin spectral/hp LES
([Nektar++](/software/nektar-plus-plus.md) v4.5.0, stabilized by
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
with the power kernel of Moura et al. 2016). The two solvers differ both in
order and in closure, so the source of the gain was open. The method is
continuous Galerkin, not the
[discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md).

The authors extend the a posteriori technique of Schranner et al. (2015):
the resolved kinetic-energy budget is integrated over a subdomain, its
discrete residual is taken as minus the numerical dissipation rate, and the
budget now carries subgrid (WALE) or SVV dissipation and flux terms, plus a
term from the spatial variation of the SVV amplitude. The technique is
validated on the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
at $Re=3000$ and applied to the Taylor–Green vortex at $Re=1600$ (reference
spectral [DNS](/definitions/direct-numerical-simulation.md) of van Rees et
al. 2011) and to an isothermal combustor port flow at $Re_p=2.25\times10^4$
over four subdomains.

[Numerical dissipation](/properties/numerical-dissipation.md) supplies most
of the non-viscous dissipation in both solvers (abstract: 60–90%). The
non-viscous dissipation of the high-order run, normalized by the viscous
one, is much lower than that of the equal-cost second-order run, and the
difference comes mainly from the numerics, not from the model. The authors
read this as a challenge to "the usual assumption in LES practice" that the subgrid model
supplies most of the subgrid dissipation, in line with Ghosal (1996);
see [implicit LES](/definitions/implicit-les.md) and
[large-eddy simulation](/definitions/large-eddy-simulation.md).
The budget is the resolved kinetic-energy balance that
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
concerns; the paper makes no claim on a preserving scheme.

# Version read

Version of record (Springer, open access CC BY 4.0; received 30 September
2022, accepted 15 May 2023, online 20 June 2023): 33 pages (journal pp.
81–113), all read, equation pages also visually. Page-1 title, authors,
venue and DOI match the metadata above; no identity issue. Section,
equation, table and figure numbers on this page are those of this version.

# Key claims

Page-local symbols: $e=\tfrac12\bar u_i\bar u_i$ the resolved kinetic
energy per unit mass (the source's $k$); for a subdomain of volume $V$,
$K_t=\mathrm d_t\int_Ve\,\mathrm dV$, the viscous dissipation
$\mathcal E_\nu=\int_V\nu\,\partial_j\bar u_i\partial_j\bar u_i\,\mathrm dV$,
the subgrid dissipation $\mathcal E_{\mathrm{sgs}}=\int_V\Pi\,\mathrm dV$,
the SVV dissipation $\mathcal E_{\mathrm{svv}}$, the numerical dissipation
$\mathcal E_{\mathrm{num}}$, $\mathcal E_{\mathrm{model}}$ standing for
$\mathcal E_{\mathrm{sgs}}$ or $\mathcal E_{\mathrm{svv}}$; flux terms
$F_k$ (advection), $F_{\mathrm{ac}}$ (pressure work), $F_\nu$, $F_{\mathrm{sgs}}$,
$F_{\mathrm{svv}}$; $H_{\mathrm{svv}}$ the SVV-amplitude-variation term;
TND (total non-viscous dissipation) $=\mathcal E_{\mathrm{model}}+\mathcal E_{\mathrm{num}}$.

1. A fifth-order (polynomial order $N=4$) continuous-Galerkin LES is more accurate than a second-order finite-volume LES at the same cost primarily because of lower numerical dissipation; the LES model dissipation plays a secondary role (Abstract; §5; §6). **Shown**
2. Numerical dissipation contributes 60–90% of the total numerical-plus-model dissipation (Abstract). **Shown**
3. The Schranner et al. (2015) dissipation-rate technique is extended to include subgrid terms, both an explicit eddy-viscosity model (WALE) and SVV; per the authors, the first application of the technique to compare two different discretizations and their LES approaches (§1, §2.2). **Derived**
4. With SVV the subdomain budget is $K_t+\mathcal E_\nu+\mathcal E_{\mathrm{svv}}+F_k+F_{\mathrm{ac}}-F_\nu-F_{\mathrm{svv}}+H_{\mathrm{svv}}=0$, with $H_{\mathrm{svv}}=\int_V\bar u_iQ_{ij}\,\partial_j\epsilon_{\mathrm{svv}}\,\mathrm dV$ from the spatial variation of the SVV amplitude (§2.2, Eqs. 6–8); with an explicit model, $K_t+\mathcal E_\nu+\mathcal E_{\mathrm{sgs}}+F_k+F_{\mathrm{ac}}-F_\nu-F_{\mathrm{sgs}}=0$ (Eq. 5). **Derived**
5. $H_{\mathrm{svv}}$ is consistently below 5% of $\mathcal E_{\mathrm{svv}}$ in the port-flow subdomains, about 10% in the jet-stream subdomain, and is omitted from the plots (§2.2; §5.2). **Shown**
6. The discrete residual, $[\cdot]_\Delta=-\mathcal E_{\mathrm{num}}$ (Eqs. 9–10), contains dissipative and dispersive errors, but over a large enough subdomain it has been seen to be positive and so measures the numerical dissipation rate (§2.2, citing Schranner et al. 2015, Castiglioni & Domaradzki 2015, Cadieux et al. 2017). **Stated**
7. Full-domain Taylor–Green validation at $Re=3000$ (64 solution points per direction): flux terms individually near zero; $-K_t$ and $\mathcal E_\nu$ match $-\mathrm dE_k/\mathrm dt$ and the enstrophy-based dissipation "excellently" for both solvers; their difference matches $\mathcal E_{\mathrm{sgs}}+\mathcal E_{\mathrm{num}}$; an OpenFOAM run without model confirms $\mathcal E_{\mathrm{sgs}}=0$; the FFT-based SVV terms are satisfactory (§4, Fig. 5); the octant gives similar results (Appendix, Fig. 17). **Shown**
8. Interior-box validation against Castiglioni & Domaradzki (2015), a commercial second-order finite-volume solver without model: excellent match for $t^*<3$, deteriorating later with trends reproduced; Nektar++ needs a slightly larger box because of its 16-element discretization (§4, Fig. 6). **Shown**
9. Without the subgrid model, the numerical dissipation of the second-order solver "adjusts" to a higher value (Fig. 5a against b) (§5.1). **Shown**
10. Taylor–Green vortex at $Re=1600$: the $16^3$ elements, $N=4$ run costs 1.3 times the $64^3$ OpenFOAM baseline but is about ten times more accurate in the $L_2$ sense; $128^3$ OpenFOAM is better but costs eight times the baseline; $8^3$ elements at $N=4$ match $128^3$ OpenFOAM until $t^*=5$ at 0.15 times the baseline cost; the baseline cost 285 s on 56 cores (§3.1, Fig. 1). **Shown** (from Saini et al. 2022)
11. Taylor–Green $64^3$ OpenFOAM: a TND peak at $t^*\approx5$, about 75% numerical, moves the dissipation peak earlier than the reference; $128^3$ lowers the peak, the numerical share staying 65–70% for $t^*>5$ (§5.1, Fig. 7a–b). **Shown**
12. Taylor–Green $16^3$, $N=4$: negligible TND until $t^*=3$ (the $64^3$ OpenFOAM run has non-zero TND even for $t^*<3$); TND at $t^*=5$ a quarter of the $64^3$ OpenFOAM value; 90–95% numerical. $8^3$, $N=4$: TND tiny until $t^*=3$, then a strong rise of numerical dissipation, SVV share 10–20%; $\mathcal E_{\mathrm{svv}}$ smaller in absolute value than $\mathcal E_{\mathrm{sgs}}$ of $64^3$ OpenFOAM (§5.1, Fig. 7c–d). **Shown**
13. Taylor–Green relative TND $(\mathcal E_{\mathrm{model}}+\mathcal E_{\mathrm{num}})/\mathcal E_\nu$ approaches 4 for $64^3$ OpenFOAM, a much lower effective $Re$; the subgrid dissipation is significant even in the initial resolved period; for $16^3$, $N=4$ the ratio stays at most 1.2. $\mathcal E_{\mathrm{num}}/\mathcal E_\nu$ is slightly negative in the laminar phase of the high-order runs (ratio of two small quantities, as in Castiglioni & Domaradzki 2015) (§5.1, Fig. 8). **Shown**
14. Taylor–Green summary: the numerics contribute 65–75% of TND in OpenFOAM and 85–95% in Nektar++; the TND of the high-order runs is about a quarter of the second-order one at similar cost (§5.1). **Shown**
15. Port flow, impingement subdomain: $\mathcal E_{\mathrm{num}}$ much larger than $\mathcal E_\nu$ and $\mathcal E_{\mathrm{model}}$; $F_\nu$ negligible and the model flux small; $K_t$, $F_k$, $F_{\mathrm{ac}}$ dominant and fluctuating more than the dissipation terms (§5.2, Fig. 10). **Shown**
16. Impingement subdomain: the 48M-cell OpenFOAM TND is almost 30% below the 16M-cell one; the 8.4M-point Nektar++ TND is 40% below the equal-cost 16M OpenFOAM; the model dissipation of the latter two is about the same, so the TND difference is numerical; model share 20% (Nektar++) against about 10% (OpenFOAM) (§5.2, Fig. 11). **Shown**
17. Recirculation subdomain: $\mathcal E_{\mathrm{num}}$ an order of magnitude above viscous and model dissipation; 16M OpenFOAM highest TND, Nektar++ and 48M OpenFOAM equal and 25% lower; model share about 15% (Nektar++) against about 8% (OpenFOAM) (§5.2, Figs. 12–13). **Shown**
18. Downstream subdomain: Nektar++ resolves a much higher $\mathcal E_\nu$ (four times 16M, three times 48M OpenFOAM) and has higher SVV dissipation; refining OpenFOAM 16M→48M lowers the normalized subgrid and numerical dissipation by 40% and 30% and the normalized TND by 35% at five times the cost; the Nektar++ normalized TND is one fifth of the 16M OpenFOAM one; SVV share 44% (15–20% upstream), subgrid share 20% (10%) (§5.2, Figs. 14–15). **Shown**
19. Jet-stream subdomain: flux terms much larger than dissipation (large coherent vortices); 48M OpenFOAM shows more numerical dissipation than 16M and the standard error is about 20%, so the analysis is judged unreliable there (§5.2, Fig. 16). **Shown**
20. In the turbulent subdomains $\mathcal E_{\mathrm{num}}$ is 4–12 times $\mathcal E_{\mathrm{sgs}}$ (second order) and 1.3–6 times $\mathcal E_{\mathrm{svv}}$ (high order); of the difference in normalized TND between 16M and 48M OpenFOAM, 15% is due to the model and 85% to the numerics; the numerics are 80–90% of TND in OpenFOAM and 56–86% in Nektar++ (§5.2, summary item 1). **Shown**
21. The normalized TND (equivalent viscosity, Eq. 11: $\nu_{\mathrm{num}}=\nu\,\mathcal E_{\mathrm{num}}/\mathcal E_\nu$ and likewise for the models) ranges 10–23 for 16M OpenFOAM, 8–15 for 48M OpenFOAM and 2.5–7 for 8.4M Nektar++; Nektar++ is below the five-times-costlier 48M run except in the recirculation subdomain, where they are about equal; for the Taylor–Green vortex the ratio was 1–4 for the second-order runs (§5.2, summary item 2). **Shown**
22. $\mathcal E_{\mathrm{model}}/\mathcal E_\nu$ fluctuates much less than $\mathcal E_{\mathrm{num}}/\mathcal E_\nu$: the numerical dissipation responds more to the instantaneous flow than the model dissipation (§5.2, Fig. 11; summary item 3). **Shown**
23. Hypothesis offered: the model contribution in OpenFOAM is lower because the numerical dissipation already suppresses the velocity gradients that WALE acts on (§5.2 item 1c). **Stated**
24. The findings align with Ghosal (1996), for whom second-order numerical dissipation can be similar to or larger than the subgrid-model dissipation over the energy-containing range, and challenge the assumption that the subgrid model supplies most of the subgrid dissipation (§6). **Stated**
25. $(\mathcal E_{\mathrm{num}}+\mathcal E_{\mathrm{model}})/\mathcal E_\nu$ is proportional to the effective viscosity of the LES; lower values mean a higher effective Reynolds number at given cost (§6; Eq. 11). **Derived**
26. Port-flow cost: 16M OpenFOAM baseline 178 h on 336 cores; 8.4M Nektar++ (130 000 elements, $N=4$) relative cost 1.03; 48M OpenFOAM 5.23 (Table 2; §3.2). **Stated** (from Saini et al. 2022)
27. Earlier comparisons (cited): Nek5000 against OpenFOAM (Sprague et al. 2010; Capuano et al. 2019) reached comparable accuracy with 7–8 times fewer points; fifth-order PyFR against a commercial finite-volume code (Vermeire et al. 2017) was better but about 2 and 6 times more expensive; third-order flux reconstruction (Jia et al. 2019) was more accurate at one third of the cost of a second-order run on a 64 times larger mesh (§1). **Stated**
28. Grid-type effects on the dissipation rate were not explored (§6). **Stated**

# Printed slips

- **§2.2, after Eq. (10):** "the ratio of the dissipation from subgrid scale term and numerical term, i.e., $\mathcal E_{\rm sgs}/\mathcal E_\nu$ or $\mathcal E_{\rm svv}/\mathcal E_\nu$": the denominator printed is the viscous, not the numerical, dissipation.
- **List of Symbols** defines "$\varepsilon$ Dissipation rate", while Eq. (19) uses $\varepsilon$ for the enstrophy.
- **§4, after Eq. (18):** "where $\Omega$ is the flow domain volume" follows Eq. (18) although $\Omega$ appears in Eq. (17); "$D_t-D_v(=D_n)$" prints $D_v$ for $D_\nu$.
- **Case of the SVV amplitude:** $\epsilon_{\rm svv}$ (§2.2) against $\epsilon_{\rm SVV}$ (Eq. 14); §2.2 calls it "the maximum value of the artificial viscosity" while Eq. (14) makes it local, $\epsilon_0U_lh/P$.
- **§3.1:** "The Nektar++ runs have 16 and 8 mesh points"; they are elements per direction.
- **Percentage ranges:** §5.1 gives the numerics "85–95%" of TND in the Nektar++ Taylor–Green runs, while it states an SVV share of 10–20% for the $8^3$ run; the abstract gives "60–90%" for the numerics, while §5.2 item 1(c) gives "56–86%" for Nektar++ (with an SVV share of 44% in the downstream subdomain).
- **Per-subdomain against summary values:** the conclusion's high-order TND "around 1/4th" of the similar-cost second-order runs fits the Taylor–Green ($t^*=5$, "a quarter") and downstream ("one-fifth") statements, not the impingement and recirculation ones (40% and 25% lower, i.e. 0.6 and 0.75 of the second-order value) *(compiler check, not in the sources)*.
- **References:** Tadmor (1989) journal entry carries "(Accessed 2022-09-11)"; the Saini (2022) thesis DOI ends with a stray quote character; Castiglioni & Domaradzki (2015) has two printed entries (TSFP 9 and Comput. Fluids 119) with the same author–year label, so in-text citations are ambiguous between them. Keywords print "Continuos Galerkin".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_i$, $\phi$, $S_{ij}$ (filtered, no mark) | $\bar u_i$, $\bar p$, $\bar S_{ij}$ | filtered quantities carry no mark in the source |
| $\varphi=\phi/\rho$ | $\bar p$ (kinematic) | |
| $\tau^s_{ij}$ | $\tau_{ij}$ | sign and trace not printed; enters the momentum equation as $-\partial_j\tau^s_{ij}$, the registry convention |
| $-\tau^s_{ij}\partial_ju_i$ (integrand of $\mathcal E_{\rm sgs}$) | $\Pi$ | |
| $k=\tfrac12u_iu_i$ (§2) | $e$ (page-local resolved kinetic energy) | **collision:** not the turbulent kinetic energy $k$; $k$ is also the wavenumber in Eq. (13) |
| $k$, $k_{2C}$ (§3.2) | $k$, (two-component estimate from PIV) | |
| $\overline{u}$, $\overline{u'u'}$ (§3.2) | $\langle u\rangle$, $R_{11}$ | **collision:** overbar = ensemble average, not the filter |
| $\mathcal E_\nu$, $\mathcal E_{\rm sgs}$, $\mathcal E_{\rm svv}$, $\mathcal E_{\rm num}$, $\mathcal E_{\rm model}$ | same (page-local) | subdomain-integrated dissipation rates |
| $F_k$, $F_{\rm ac}$, $F_\nu$, $F_{\rm sgs}$, $F_{\rm svv}$, $H_{\rm svv}$, $K_t$ | same (page-local) | |
| $\nu_{\rm sgs}$, $\nu_{\rm svv}$, $\nu_{\rm num}$ | (equivalent viscosities, Eq. 11) | not the eddy viscosity $\nu_t$ of a model |
| $\epsilon_{\rm svv}$, $Q$, $Q_{u_ix_j}$, $\hat Q(m)$, $\star$ | $\epsilon_{\rm svv}$, $Q$, $Q_{ij}$ (page-local SVV amplitude, kernel, $Q\star\partial_j\bar u_i$, modal spectrum, convolution) | **collision:** $\hat Q$ is not a test filter |
| $P$, $m$, $P_{\rm SVV}$ | $N$, (mode index, kernel exponent) | |
| $\epsilon_0$, $U_l$, $h$ | (SVV parameter, local advection speed), $h$ | $h$ = cube root of the element volume |
| $C_w$ | $C_w$ (WALE constant) | 0.325 |
| $\varepsilon$ (Eq. 19) | (enstrophy) | **collision:** not the dissipation rate $\varepsilon$ |
| $\omega$ | $\omega_i$ | vorticity, not the specific dissipation rate |
| $E_k$, $D_t$, $D_\nu$, $D_n$ | (volume-averaged kinetic energy, $-\mathrm dE_k/\mathrm dt$, enstrophy-based dissipation, their difference) | Taylor–Green diagnostics |
| $\Omega$ | (domain volume) | **collision:** not the rotation-rate tensor |
| $\alpha$ | (port/core velocity ratio; Tukey parameter 0.25) | **collision:** not the DG/FV blending factor |
| $B$, $Re_p$, $D_p$, $U_p$ | (bleed ratio), $Re$ on port diameter and velocity | |
| $t^*=tV_0/L$ | $t^*$ | |

# Reference list

37 printed references, author–year style (alphabetical, unnumbered). The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Castiglioni et al. (2015) appears three times as
distinct works (an SFB/TRR 40 report, TSFP 9 and Comput. Fluids 119),
keyed in printed order; the authors' thesis and AIAA J. paper are
`saini-2022` and `saini-2022-b`. The cited `domaradzki-2003` and
`moratillavega-2020` are different works from the archive papers keyed
`domaradzki-2024` and `moratillavega-2024`. The defects listed under Printed slips are kept
as printed; no item is unparseable.

# Pages created or updated

Chunk 4 (2026-10-26), cited further in chunks 5, 6, 14. This source is cited on:

- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Flux reconstruction](/methods/flux-reconstruction.md)
- [Continuous-Galerkin spectral-element method](/methods/spectral-element-method.md)
- [Spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
- [WALE model](/methods/wale-model.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Nektar++](/software/nektar-plus-plus.md)
- [OpenFOAM](/software/openfoam.md)
- [PyFR](/software/pyfr.md)
