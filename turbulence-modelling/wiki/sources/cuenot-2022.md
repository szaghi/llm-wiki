---
type: Source
title: "Cuenot et al. (2022) — The thickened flame approach for non-premixed combustion: Principles and implications for turbulent combustion modeling"
description: "Shows from the strained counterflow diffusion flame that non-premixed flames thicken on LES grids by themselves, their consumption speed scaling with the square root of strain times diffusivity, so that a thickened-flame correction acts on the diffusivities only; tested on coarse-mesh one-dimensional counterflow flames with two-step and reduced chemistry."
resource: "doi:10.1016/j.combustflame.2021.111702"
source_kind: paper
authors: [Cuenot B., Shum-Kivan F., Blanchard S.]
year: 2022
venue: "Combust. Flame 239:111702"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Combustion_and_Flame_Cuenot_The_thickened_flame_approach_for_non-premixed_combustion_Pri.pdf"
tags: [combustion, les, numerical-dissipation]
timestamp: 2026-10-27T10:58:00Z
---

# Summary

The [thickened flame model](/methods/thickened-flame-model.md) of Colin et
al. lets [LES](/definitions/large-eddy-simulation.md) resolve a premixed
front on the grid by multiplying the diffusivity and dividing the reaction
rate by a factor $F$, which keeps the flame speed ($\propto\sqrt{RD_{\mathrm m}}$)
and thickens the front ($\propto\sqrt{D_{\mathrm m}/R}$). Cuenot et al.
(2022) ask how the idea carries over to purely non-premixed flames, which
the earlier dynamically thickened flame works handled only in partially
premixed form.

From the steady strained laminar counterflow diffusion flame they derive
that at high Damköhler number the consumption speed scales as
$\sqrt{a_{\mathrm{cf}}D_{\mathrm m}}$ and the thermal thickness as
$\sqrt{D_{\mathrm m}/a_{\mathrm{cf}}}$, independently of chemistry:
changing the reaction rate has no effect, and a thickening that keeps the
consumption speed must multiply $D_{\mathrm m}$ and divide the strain rate
$a_{\mathrm{cf}}$ by the same factor. A diffusion flame has no intrinsic
thickness, so grid filtering of the strain rate and numerical diffusion
thicken it automatically, and no explicit artificial thickening is needed
for stability.

One-dimensional counterflow computations on uniform meshes of decreasing
resolution (methane–air with two-step chemistry; methane–oxygen at 54 bar
with 14-species reduced chemistry) stay stable on every mesh, while the
total heat release rises with coarsening through the
[numerical dissipation](/properties/numerical-dissipation.md) of
first-order upwinding, by up to 65% at two points per flame thickness
as printed (Table 2 implies 60.5%; see Printed slips).
Dividing all diffusivities by $F=(\dot\Omega_{T,\mathrm{coarse}}/\dot\Omega_{T,\mathrm{ref}})^2$
removes the error to within 3%; about five points in the reaction zone
capture the inner chemical structure. For LES the authors propose to divide
all diffusivities by $F_{\mathrm{LES}}=F_{\mathrm{num}}F_{\mathrm{sgs}}$,
with $F_{\mathrm{num}}$ from the resolved strain and scalar dissipation and
the subgrid factor left to future work. They contrast the approach with
[implicit LES](/definitions/implicit-les.md), and it may be combined with
[flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md).
No turbulent flame is computed.

# Version read

Version of record (Elsevier typeset, Combust. Flame 239:111702; received
31 March 2021, available online 4 September 2021), 10 pages, all read;
pp. 3, 6 and 9 were read on the page images because the extracted
equations are garbled. Page 1 matches the published title, authors and
DOI.

# Key claims

1. In the steady laminar counterflow the mixture fraction is $Z(x)=\tfrac12(1-\mathrm{erf}\,\eta_Z(x))$ and the stoichiometric scalar dissipation is $\chi_{Z,\mathrm{st}}=C_{\mathrm{st}}^2a_{\mathrm{cf}}/\pi$ with $C_{\mathrm{st}}=\exp(-\eta_{Z,\mathrm{st}}^2)\rho_{\mathrm{st}}/\rho_0$ (§2, Eqs. 2–3). **Stated** (from earlier work); $\chi_{Z,\mathrm{st}}$ **Derived**
2. The flame solution in mixture-fraction space, $-\chi_Z\,\partial^2\phi_v/\partial Z^2=\dot\omega_{\phi_v}$ (Eq. 4), is insensitive to the diffusion coefficients for steady strained flames (§2). **Derived**
3. The consumption speed in physical space is $\dot\Omega_{\phi_v}=-\frac1{C_{\mathrm{st}}}\sqrt{\frac{2a_{\mathrm{cf}}D_{\mathrm m}}{\pi}}\Bigl(\frac{\phi_{v,+\infty}-\phi_{v,\mathrm{st}}}{1-Z_{\mathrm{st}}}-\frac{\phi_{v,\mathrm{st}}-\phi_{v,-\infty}}{Z_{\mathrm{st}}}\Bigr)$, and for the heat release Eq. (10) (§2.1, Eqs. 5–10). **Derived**
4. The thermal thickness of a diffusion flame is $\delta_{\mathrm f}=\frac1{C_{\mathrm{st}}}\sqrt{\frac{2\pi D_{\mathrm m}}{a_{\mathrm{cf}}}}$ (§2.2, Eq. 11). **Derived**
5. At high Damköhler number the consumption speed scales as $\sqrt{a_{\mathrm{cf}}D_{\mathrm m}}$ and the thickness as $\sqrt{D_{\mathrm m}/a_{\mathrm{cf}}}$; modifying the chemical source term has no effect on them (§2.2). **Derived**
6. Hence the premixed transformation (multiply $D_{\mathrm m}$, divide the reaction rate by $F$) cannot be applied to diffusion flames; keeping the consumption speed while thickening requires multiplying $D_{\mathrm m}$ and dividing $a_{\mathrm{cf}}$ by the same $F$ (§2.2). **Derived**
7. A diffusion flame has no intrinsic thickness: grid filtering lowers the resolved strain rate and numerical diffusion adds to physical diffusion, so it thickens automatically on LES grids and needs no explicit artificial thickening (§2.2, §7). **Derived** / **Shown**
8. The two-step BFER* scheme reproduces the GRI3.0 total heat release against strain rate and the temperature profile in $Z$ at $a_{\mathrm{cf}}=250$ s$^{-1}$, with a higher extinction strain rate (§3, Fig. 2). **Shown**
9. Methane–air at $a_{\mathrm{cf}}=100$ s$^{-1}$ ($\delta_{\mathrm f}\approx4$ mm, total heat release 323 kW) gives a stable solution even with 10 grid points, the reaction zone then described by one point (§4, Figs. 3–4). **Shown**
10. CANTERA's first-order upwind discretization introduces a dissipation error of the form $\sin(kh)/(kh)$, with a maximum factor $2/\pi$ at the highest discrete wavenumber (§4). **Stated**
11. The total heat release deviates from the reference for $RR\le20$ and rises by up to 65% on M10 ($RR=2$), interpreted as numerical over-diffusion consistent with Eq. (10) (§4, Fig. 5). **Shown**
12. The effective diffusivity of Eq. (14), $F=D^*_{\mathrm m}/D_{\mathrm m}=(\dot\Omega_{T,M^*}/\dot\Omega_{T,\mathrm{M1000}})^2$, is 1, 1.113, 1.27, 1.505 and 2.575 for M500, M100, M50, M30 and M10; multiplying all diffusivities by $F$ on the fine mesh "exactly" retrieves the coarse-mesh solutions (Table 2, Fig. 6). **Shown**
13. Dividing all diffusivities by $F$ on the coarse meshes recovers the reference consumption rate within 3%, even at $RR=2$ (§4, Fig. 7). **Shown**
14. The consumption rate can be corrected with only two points in the reaction zone provided one lies close to stoichiometry (§4). **Shown** / **Stated**
15. The reduced (ARC) scheme for methane oxy-combustion has 14 transported and 4 quasi-steady species and 136 reactions, with a consumption-rate error below 1.5% on laminar diffusion flames at various strain rates (§5). **Stated**
16. Methane–oxygen at 54 bar, 280 K and $a_{\mathrm{cf}}=810$ s$^{-1}$ ($\delta_{\mathrm f}=300$ µm, 2020 kW) converges on all nine meshes, 30 to 1500 points, $RR$ 0.9 to 45 (§5, Table 3). **Shown**
17. The ARC correction factors are 1, 1.01, 1.03, 1.04, 1.08, 1.12, 1.19, 1.25 and 1.46 for $RR=45$, 30, 21, 15, 9, 6, 3, 1.5 and 0.9, slightly above the two-step values at equal $RR$ (Table 3). **Shown**
18. With $D_{\mathrm m}/F$ the consumption rate is recovered within 2% except on M50, the only mesh without a grid point near stoichiometry (§5, Fig. 9). **Shown**
19. On M200 ($RR=6$) the heat-release profile keeps its endothermic–exothermic double structure; on M30 ($RR=0.9$) it degenerates to one peak; top-hat filtered M1500 profiles at 50 µm and 333 µm are "remarkably close" to M200 and M30 (§5, Fig. 10). **Shown**
20. Major species in $Z$-space agree on all meshes; intermediate species are captured on M200 but not on M30, OH reasonably (§5, Fig. 11). **Shown**
21. About five grid points in the reaction zone are needed to capture the inner chemical structure (§5, §6). **Shown**
22. The correction by $F$ does not modify the Damköhler number and so preserves the flamelet regime (§5). **Stated**
23. For non-premixed LES all diffusivities are divided by $F_{\mathrm{LES}}=F_{\mathrm{num}}F_{\mathrm{sgs}}$, which may be above or below one (§6). **Stated** (proposal, not tested)
24. $F_{\mathrm{num}}=\dfrac{C_{\mathrm{st}}^2a_{\mathrm{cf}}^{\mathrm{LES}}/\pi}{\chi^{\mathrm{LES}}_{Z,\mathrm{st}}}$ from the resolved strain and scalar dissipation (Eq. 15); $F_{\mathrm{sgs}}\le1$ accounts for subgrid strain and wrinkling and is left to future work (§6). **Stated**
25. The dominant error is set by the Kolmogorov resolution $RR_\eta=\eta/h$: for $RR_\eta\le RR$ (strong turbulence) the modelling error dominates, for $RR_\eta\ge RR$ (weak turbulence) the numerical error (§6). **Stated**
26. $F_{\mathrm{LES}}\approx1$ means that numerical diffusion compensates the subgrid effects, as in Breda et al., where LES with and without a subgrid combustion model gave similar results (§6). **Stated**
27. The thickened flame approach is "totally different from pdf-based or viscosity-based (ILES) methods" (§1). **Stated**

# Printed slips

- §6: with Eq. (15) as printed, "If numerical diffusion appears, $\chi^{LES}_{st}$ decreases and $F_{num}<1$", while a decreasing denominator of Eq. (15) gives $F_{\mathrm{num}}>1$, the value that §§4–5 need ($F\ge1$ in Tables 2–3) *(compiler check, not in the sources)*.
- §6 prints $\varepsilon_{num}=(F_{num}^2-1)\dot\Omega_{T,exact}$; with Eq. (14), $\dot\Omega_{T,\mathrm{num}}=F^{1/2}\dot\Omega_{T,\mathrm{exact}}$, so the error is $(F^{1/2}-1)\dot\Omega_{T,\mathrm{exact}}$ *(compiler check, not in the sources)*.
- §4: "relative increase of 65% for mesh M10 (RR = 2)", while Table 2 prints $F=2.575$ for M10, which by Eq. (14) is a heat-release ratio of $\sqrt{2.575}=1.605$, an increase of 60.5% *(compiler check, not in the sources)*.
- §5: the heat release "is multiplied by about 1.46 for the coarsest mesh" and on M200 "the integral is only 1.12 higher than the reference value": 1.46 and 1.12 are the Table 3 $F$ values of M30 and M200, which by Eq. (14) correspond to heat-release ratios $\sqrt{1.46}=1.21$ and $\sqrt{1.12}=1.06$ *(compiler check, not in the sources)*.
- Eq. (6) substitutes $a/\pi$ for $\chi_{st}=C_{st}^2a/\pi$ "replacing $\chi_{st}$ with the strain rate"; carried through Eqs. (6)–(8), $C_{\mathrm{st}}^2$ gives the prefactor $C_{\mathrm{st}}\sqrt{2a_{\mathrm{cf}}D_{\mathrm m}/\pi}$ in Eq. (9) instead of the printed $\frac1{C_{st}}\sqrt{2aD/\pi}$; the scaling with $\sqrt{a_{\mathrm{cf}}D_{\mathrm m}}$ is unaffected *(compiler check, not in the sources)*.
- §4 takes "the reference fine mesh M1000" and Eq. (14) normalizes by M1000, while the Fig. 6 caption and legend read "mesh M500 with D×F" and Table 2 lists M500 with $F=1$ and no M1000.
- Fig. 7 caption: "for the various meshes of Table 2"; the meshes are defined in Table 1.
- §5: "profiles are less steep on the fuel (left) side due to larger diffusion coefficients in this stream compared to the fuel stream".
- "much successfull" (§1), "ant taken" (§2.1), "sill hold" (§5), "due to but their specific nature" (Abstract), "same structure than of" (§2).
- Ref. [11] (Pitsch, Riesmeier & Peters, Combust. Sci. Technol. 158) prints the year 1988 and the title of ref. [9]; ref. [40] prints a garbled author list; ref. [27] ends its title with "acta astronautica".

# Notation map

| Cuenot et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $var$, $\dot\omega_{var}$ | $\phi_v$, $\dot\omega_{\phi_v}$ (any species mass fraction or temperature, its source; page-local) | **collision:** $\dot\omega$ is not the specific dissipation rate |
| $D$, $D^*$ | $D_{\mathrm m}$, $D^*_{\mathrm m}$ (molecular and effective diffusivity, page-local) | **collision:** not the differentiation matrix $D_{ij}$ |
| $a$, $a^{LES}$ | $a_{\mathrm{cf}}$, $a_{\mathrm{cf}}^{\mathrm{LES}}$ (counterflow strain rate, page-local) | $\lvert u_O-u_F\rvert/L$ |
| $Z$, $Z_{st}$ | $Z$, $Z_{\mathrm{st}}$ (page-local) | 1 in the fuel, 0 in the oxidizer |
| $\eta(x)$, $\zeta(x)$ | $\eta_Z$, $\zeta_Z$ (similarity variable, density-weighted coordinate; page-local) | **collision:** $\eta$ is also the Kolmogorov length in §6 |
| $\chi=2D(\partial Z/\partial x)^2$, $\chi_{st}$ | $\chi_Z$, $\chi_{Z,\mathrm{st}}$ (page-local) | **collision:** not the SA ratio $\chi$ |
| $C_{st}$, $\rho_0$ | $C_{\mathrm{st}}$, $\rho_0$ (page-local) | density at the stagnation point |
| Da $=1/\tau_c\chi_{st}$ | $Da=1/(\tau_c\chi_{Z,\mathrm{st}})$ (page-local) | $\tau_c$ chemical time |
| $\dot\Omega^Z_{var}$, $\dot\Omega_{var}$, $\dot\Omega_T$ | consumption rate in $Z$-space and physical space, total heat release (page-local) | quoted in kW |
| $\delta_f$ | $\delta_{\mathrm f}$ (thermal flame thickness, page-local) | **collision:** not the boundary-layer thickness $\delta$ |
| $R$ | premixed reaction-rate scale (page-local) | premixed thickened flame only |
| $F$, $F_{num}$, $F_{sgs}$, $F_{LES}$ | $F$, $F_{\mathrm{num}}$, $F_{\mathrm{sgs}}$, $F_{\mathrm{LES}}$ (page-local) | here the diffusivities are divided by $F$ |
| $\varepsilon_{num}$, $\varepsilon_{sgs}$ | numerical and modelling errors of the consumption rate (page-local) | **collision:** not the dissipation rate $\varepsilon$ |
| $RR=\delta_f/\Delta x$, $RR_\eta=\eta/\Delta x$ | $RR$, $RR_\eta$ with $h$ the grid step (page-local) | |
| $\Delta x$ | $h$ | uniform grid step; "LES filter" and "grid filter" are used interchangeably |
| M$N$ | mesh with $N$ points | |

# Reference list

53 printed references, numbered Elsevier style ([1]–[53]). The list is
merged complete into the [bibliography](/bibliography.md) with `citedby`
cuenot-2022. Ref. [11] is keyed by its printed year 1988; ref. [40] is
entered from its garbled author list; ref. [28] prints no pages; ref. [49]
(GRI-Mech) carries an access-date year; ref. [1] has a corporate author.
The authors' own works [43] and [45] are distinct from this source. No
printed duplicates.

# Pages created or updated

Chunk 9 (2026-10-27). This source is cited on:

- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
- [Thickened flame model](/methods/thickened-flame-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
