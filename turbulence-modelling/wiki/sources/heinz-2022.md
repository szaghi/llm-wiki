---
type: Source
title: "Heinz (2022) — Remarks on Energy Partitioning Control in the PITM Hybrid RANS/LES Method for the Simulation of Turbulent Flows"
description: "Short comment on Chaouat & Schiestel (2021): a variational analysis of the ε-equation destruction coefficient of hybrid k-ε models gives three resolution-dependent options, and argues that the PITM time-scale form is consistent only in homogeneous flow, favouring continuous eddy simulation with a length-scale ratio."
resource: "doi:10.1007/s10494-021-00302-w"
source_kind: paper
authors: [Heinz S.]
year: 2022
venue: "Flow Turbul. Combust. 108:927-933"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2021_Crossref_Flow_Turbulence_and_Combustion_Heinz_Remarks_on_Energy_Partitioning_Control_in_the_PITM_Hybrid_RA.pdf"
tags: [hybrid-rans-les, continuous-eddy-simulation, pitm, k-epsilon, energy-partition]
timestamp: 2026-10-27T15:55:00Z
---

# Summary

Heinz (2022) is a short comment on Chaouat & Schiestel (2021). It asks how a
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) model should make the
modelled and the resolved motions "communicate": the modelled viscosity must
be small enough not to extinguish resolved motion, yet grow on coarser grids
and at higher $Re$. The author compares two methods that address this
explicitly. One is the partially integrated transport modelling (PITM) of
Schiestel, Dejoan and Chaouat. The other is the author's own
[continuous eddy simulation](/methods/continuous-eddy-simulation.md) (CES).

The host is a filtered [$k$-$\varepsilon$ model](/methods/k-epsilon-model.md)
whose destruction term carries a variable coefficient,
$C_{\varepsilon1}\alpha^*\varepsilon^2/k$, with
$\alpha^*=\alpha=C_{\varepsilon2}/C_{\varepsilon1}=1.33$ in RANS. Taking the
variation of the $\varepsilon$ equation gives an exact relation for
$\delta\alpha^*$. Spatially and temporally uniform $\delta k/k$ and
$\delta\varepsilon/\varepsilon$ are assumed; the author says
Chaouat & Schiestel use the same assumption. Three options follow. O1
neglects the material derivatives and gives $\alpha_1^*=1+L_+^2(\alpha-1)$,
the CES choice. O2 neglects the turbulent-transport combination and gives
$\alpha_2^*=1+\tau_+(\alpha-1)$. O3 puts total viscosities in the transport
terms and recovers the O2 coefficient with no further assumption. The
ratios $L_+$ and $\tau_+$ are modelled-to-total length and time scales.

The central claim is that the O2 coefficient with the ordinary transport
terms is consistent only in homogeneous flow. In non-homogeneous flow it
implies a spurious source. The PITM-type choice $1+k_+(\alpha-1)$ (O2 with
$\varepsilon_+=1$), which Chaouat & Schiestel recommend also for
non-homogeneous flow, is therefore inconsistent. The author also calls
$\varepsilon_+=1$ inappropriate near walls. A figure reproduced from Heinz
et al. (2020) on the [periodic hill](/benchmarks/periodic-hill.md) shows a
prescribed PITM energy ratio failing to control the actual one. The
conclusions favour CES with O1, call O3 attractive but untested, say CES-O1
avoids similar problems of
[PANS](/methods/partially-averaged-navier-stokes.md), and extend the results to
$k$-$\omega$, [Reynolds-stress](/methods/reynolds-stress-model.md) and PDF
forms. No new simulation is reported.

# Version read

Version of record (Springer, Flow Turbul. Combust. 108:927–933, online
1 November 2021, issue 2022); 7 pages, all read, with pp. 929–932 checked
visually. Page 1 matches Crossref. The article is a comment ("Remarks") on
Chaouat & Schiestel (2021), Flow Turbul. Combust., doi
10.1007/s10494-021-00259-w. The "PITM" analysed excludes the relaxation
mechanism of what the paper calls "the usual computational implementation
of PITM methods", which forces the energy ratio to its target (§1).

# Key claims

1. Hybrid RANS/LES needs a "communication" between modelled and resolved motions: the modelled viscosity must not extinguish resolved motion on coarse grids, yet its contribution must grow for coarser grids and higher $Re$; most hybrid methods do not address this (§1, pp. 927–928). **Stated**
2. CES and PITM are the hybrid methods that actively address mode control. Table 1 compares them. PITM: $k$-$\varepsilon$ and related RSM, one hybridization type, a spectral-theory modelling basis, empirical closures needed, option O2 with $\tau_+=k_+$. CES: $k$-$\varepsilon$, $k$-$\omega$, RSM and PDF equations, three equivalent hybridization types, variational analysis, no empirical closures, option O1 (§1, Table 1). **Stated**
3. "PITM" in the paper means the CES mode control replaced by the mode control for homogeneous flows; the PITM relaxation mechanism of Chaouat & Schiestel (2021) is not considered (§1, p. 928). **Stated**
4. If the CES and PITM mode controls are driven by $L_+^2=k_+^3$ and $\tau_+=k_+$, the relative error of the PITM assumption is $(k_+-k_+^3)k_+^{-3}\cdot100\%$: 2400, 300 and 56% for $k_+=0.2$, 0.5, 0.8 (§1, p. 928). **Derived**
5. Replacing $P_k$ in the $\varepsilon$ equation through $Dk/Dt=P_k-\varepsilon+D_k$ and taking the variation gives the exact relation Eq. (3), with $Q$ from Eq. (4) (§2, Eqs. 3–4). **Derived**
6. Following Friess et al. (2015) and the CES papers, $\delta k/k$ and $\delta\varepsilon/\varepsilon$ are taken uniform in space and in time; Chaouat & Schiestel (2021, App. E) use "exactly the same" assumption "although different language is used" (§2, pp. 929–930). **Stated**
7. Under that assumption $\delta D_k/D_k=3\delta k/k-\delta\varepsilon/\varepsilon$, $\delta D_\varepsilon/D_\varepsilon=2\delta k/k$ and Eq. (5) hold at leading order, and Eq. (3) reduces to Eq. (6), equivalently Eq. (7) (§2, Eqs. 5–7). **Derived**
8. Option O1 (no effect of $Dk/Dt$, $D\varepsilon/Dt$): integrating Eq. (6) gives $\alpha_1^*=1+L_+^2(\alpha-1)$, as in Heinz (2019) (§2, p. 930). **Derived**
9. Option O2 (no effect of the transport combination $D_*$, because model coefficients should not depend on non-systematic turbulent transport): integrating Eq. (7) gives $\alpha_2^*=1+\tau_+(\alpha-1)$ (§2, p. 930). **Derived**
10. Option O3 (modelled viscosity in the turbulent transport terms replaced by the total viscosity): $\delta D_k/D_k=\delta k/k$, $\delta D_\varepsilon/D_\varepsilon=\delta\varepsilon/\varepsilon$, and Eq. (3) reduces without further assumption to $\delta\alpha^*=(\alpha^*-1)[\delta k/k-\delta\varepsilon/\varepsilon]$, so $\alpha_3^*=1+\tau_+(\alpha-1)$ (§2, p. 930, Table 2). **Derived**
11. O3 is physically plausible but needs gradients of resolved quantities ($k_{\mathrm{res}}$, $\varepsilon_{\mathrm{res}}$) and lets resolved motion act on turbulent transport; its computational suitability "needs evidence that is currently missing" (§2, p. 931). **Stated**
12. O1 "is known to be very successful" with the ordinary transport terms (§2, observation 1, p. 931). **Stated** (by reference to the CES papers)
13. Using $\alpha_2^*$ with the ordinary transport terms in non-homogeneous flow "leads to inconsistent simulations due to a spurious source term (the difference of turbulent transport terms)"; O2 can only be used as the homogeneous-flow version of O3 (§2, observation 2, p. 931). **Derived** (the spurious term is not written out)
14. Flow-resolution indicators: the time-scale ratio $\tau_+$ under O3 conditions (homogeneous and non-homogeneous flows) and the length-scale ratio $L_+$ under O1 conditions (homogeneous case excluded) (§2, observation 3). **Derived**
15. $\varepsilon_+=1$ implies $L_+^2=k_+^3$ and $\tau_+=k_+$, hence $\alpha^*_{1k}=1+k_+^3(\alpha-1)$ and $\alpha^*_{2k}=1+k_+(\alpha-1)$ (§3, p. 931). **Derived**
16. Chaouat & Schiestel (2021) recommend $\alpha^*_{2k}$ with the ordinary transport terms also for non-homogeneous flows, while the CES papers recommend $\alpha_1^*$; by claim 13 the former is only the homogeneous version of O3 (§3, pp. 931–932). **Derived**
17. $\varepsilon_+=1$ is inappropriate near walls (Heinz et al. 2020) (§3, p. 932). **Stated**
18. Keeping $\varepsilon_+\neq1$ in the analysis of Chaouat & Schiestel (2021) implies $\alpha_1^*=1+k_+\varepsilon_+^{-2}(\alpha-1)$; the author asks why resolution should be measured by "the inverse quadratic acceleration" $k_+\varepsilon_+^{-2}=\tau_+^4/L_+^2$ (§3, p. 932). **Derived**
19. In periodic-hill simulations of Heinz et al. (2020) with a PITM-type grid parametrization of $k_+$ in place of the CES mode control, the prescribed energy ratio $R=C_\Delta\Delta_+^{2/3}$ does not control the actual $k_+$; small changes in $R$ can imply significant changes in $k_+$ (§3, Fig. 1). **Shown** (reproduced figure)
20. In the same simulations the behaviour near the upper and lower walls is called unphysical: the actual $k_+$ "cannot follow structural changes of imposed $k_+$" (§3, Fig. 1). **Shown** (reproduced figure)
21. CES with O1 is "a simple and stable way" to obtain correct mode communication and overcomes the PITM problems reported and "similar problems seen in" PANS (Girimaji 2006; Tazraei & Girimaji 2019) (§4, conclusion 1). **Stated**
22. CES with O3 has never been applied; it is theoretically attractive but faces non-trivial computational challenges (§4, conclusion 2). **Stated**
23. The conclusions, derived for the $k$-$\varepsilon$ model and one hybridization, carry over to $k$-$\omega$ models, other hybridizations and RSM and PDF CES methods (Heinz 2021a) (§4, conclusion 3). **Stated**

The model equations (Eqs. 1–2), translated, with $\bar u_i$ the filtered
velocity, $k$ and $\varepsilon$ the modelled energy and dissipation,
$\nu_t=C_\mu k^2/\varepsilon$ and $P_k=\nu_t|\bar S|^2$:

$$\frac{Dk}{Dt}=P_k-\varepsilon+D_k,\qquad \frac{D\varepsilon}{Dt}=C_{\varepsilon1}\frac{\varepsilon^2}{k}\Big(\frac{P_k}{\varepsilon}-\alpha^*\Big)+D_\varepsilon,$$

with $D_k=\partial_j(\nu_t^*\partial_jk)$,
$D_\varepsilon=\partial_j[(\nu_t^*/\sigma_\varepsilon)\partial_j\varepsilon]$,
$\nu_t^*=\nu_t$ (O1, O2) or the total viscosity (O3), $C_{\varepsilon1}=1.44$,
$C_{\varepsilon2}=1.92$, $\sigma_\varepsilon=1.3$; no $\sigma_k$ and no value of
$C_\mu$ are printed. The reduced relation (Eq. 7) is

$$\delta\alpha^*=(\alpha^*-1)\Big[\frac{\delta k}{k}-\frac{\delta\varepsilon}{\varepsilon}\Big]-\frac{D_*}{\varepsilon}\Big[2\frac{\delta k}{k}-\frac{\delta\varepsilon}{\varepsilon}\Big],\qquad D_*=D_k-\frac{kD_\varepsilon}{C_{\varepsilon1}\varepsilon}.$$

The CES ratios: $L_+=L/L_{\mathrm{tot}}$ with $L=\langle k\rangle^{3/2}/\langle\varepsilon\rangle$
and $L_{\mathrm{tot}}=k_{\mathrm{tot}}^{3/2}/\varepsilon_{\mathrm{tot}}$,
$k_{\mathrm{tot}}=\langle k\rangle+k_{\mathrm{res}}$,
$\varepsilon_{\mathrm{tot}}=\langle\varepsilon\rangle+\varepsilon_{\mathrm{res}}$,
$\langle\cdot\rangle$ a time average. The PITM-type prescription of Fig. 1:
$\Delta_+=\Delta/L_{\mathrm{tot}}$, $\Delta=(\Delta_x\Delta_y\Delta_z)^{1/3}$,
$C_\Delta=3C_K/(2\pi^{2/3})=1.06$ with $C_K$ the Kolmogorov constant.

# Printed slips

- §4, conclusion 2: "but is faces non-trivial computational challenges" ("it faces").

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tilde U_i$, $\tilde p$ | $\bar u_i$, $\bar p$ | **collision:** the source's tilde is the (incompressible) hybrid filter, not a Favre filter |
| $\tilde S_{ij}$, $S=(2\tilde S_{mn}\tilde S_{nm})^{1/2}$ | $\bar S_{ij}$, $\lvert\bar S\rvert$ | factor two included in the source |
| $k$, $\epsilon$ | $k$, $\varepsilon$ (modelled parts) | |
| $P$ | $P_k$ | $\nu_t\lvert\bar S\rvert^2$ |
| $D_k$, $D_\epsilon$ | $D_k$, $D_\varepsilon$ (turbulent transport, page-local) | |
| $C_{\epsilon_1}$, $C_{\epsilon_2}$, $\sigma_\epsilon$ | $C_{\varepsilon1}$, $C_{\varepsilon2}$, $\sigma_\varepsilon$ | 1.44, 1.92, 1.3 |
| $\alpha$, $\alpha^*$, $\alpha^*_{1,2,3}$, $\alpha^*_{1k,2k}$ | $\alpha_\varepsilon$, $\alpha^*_\varepsilon$ (page-local, as on [continuous eddy simulation](/methods/continuous-eddy-simulation.md)); subscripts kept on this page | **collision** with the DG/FV blending factor $\alpha$ and the Wilcox constant $\alpha^*$ |
| $\tau=k/\epsilon$ | $\tau_k=k/\varepsilon$ (page-local) | **collision** with $\tau_{ij}$ and $\tau_w$ |
| $L_+$, $\tau_+$, $k_+$, $\epsilon_+$ | $L_+$, $\tau_+$, $k_+$, $\varepsilon_+$ (modelled-to-total ratios, registry §11) | **collision:** "+" is not wall units; $L_+$ as on [hybrid RANS/LES](/definitions/hybrid-rans-les.md) |
| $k_{res}$, $\epsilon_{res}$, $k_{tot}$, $\epsilon_{tot}$, $L$, $L_{tot}$ | $k_{\mathrm{res}}$, $\varepsilon_{\mathrm{res}}$, $k_{\mathrm{tot}}$, $\varepsilon_{\mathrm{tot}}$, $L$, $L_{\mathrm{tot}}$ | $L$ a RANS-type length, not the integral scale of §8 |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | time average |
| $\nu_t^*$, $\nu_{t,tot}$ | (viscosity in the transport terms; total viscosity, page-local) | |
| $Q$, $D_*$ | same (page-local abbreviations) | |
| $R$, $\Delta_+$, $C_\Delta$, $C_K$ | same (page-local) | $\Delta$ the cube root of the cell volume |
| $\delta$ | $\delta$ (variation) | **collision** with the boundary-layer thickness |

# Reference list

16 printed references, author–year (Springer) style, alphabetical. The list
is merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. Same-author same-year works are keyed in printed order (Heinz
2020 and Heinz et al. 2020; Heinz 2021a, 2021b and Heinz et al. 2021).
Chaouat & Schiestel (2021), the paper commented on, is printed with a DOI
only; the second author of Fröhlich & von Terzi (2008) is printed
"Terzi, D.V.". No printed duplicates; all items parsed.

# Pages created or updated

Chunk 7 (2026-10-26). This source is cited on:

- [Periodic hill](/benchmarks/periodic-hill.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Continuous eddy simulation](/methods/continuous-eddy-simulation.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [Partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
