---
type: Source
title: "Alberti et al. (2026) — Coupling IDDES with an algebraic transition model in a high-order discontinuous Galerkin solver"
description: "Builds a transitional SA-IDDES in an incompressible modal discontinuous Galerkin solver by putting the algebraic SA-BCM intermittency on production and destruction, forcing RANS mode wherever the intermittency is below one through a modified shielding function, and recalibrating the natural-transition constant; tested on the Eppler 387 and NACA 0012 airfoils and a supercritical sphere."
resource: "doi:10.1016/j.ijheatfluidflow.2026.110578"
source_kind: paper
authors: [Alberti L., Carnevali E., Crivellini A.]
year: 2026
venue: "Int. J. Heat Fluid Flow 121:110578"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_International_Journal_of_Heat_and_Fluid_Flow_Alberti_Coupling_IDDES_with_an_algebraic_transition_model_in_a_high-.pdf"
tags: [hybrid-rans-les, transition, spalart-allmaras, dg, airfoil]
timestamp: 2026-10-29T07:23:00Z
---

# Summary

Alberti et al. (2026) follow up the authors' study of
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) in a high-order modal DG
solver ([Alberti et al. (2025)](/sources/alberti-2025-b.md)) with a
transitional model. The base is the
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) IDDES of Shur et al.
([detached-eddy simulation](/methods/detached-eddy-simulation.md)), with the
Mockett length $\Delta_\omega$ replacing the whole IDDES filter width, all
lengths divided by $N+1$ and no low-Reynolds correction. Its RANS branch is
replaced by the algebraic SA-BCM of Cakmakcioglu et al.
([local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)),
whose intermittency $\gamma_{\mathrm{BC}}$ needs no extra transport equation.
Three changes are made: $\gamma_{\mathrm{BC}}$ multiplies both production and
destruction of $\tilde\nu$ (after Yalçın et al.); a modified shielding
$\hat f_d^*=\max\{\hat f_d,1-\gamma_{\mathrm{BC}}\}$ keeps RANS mode wherever
$\gamma_{\mathrm{BC}}<1$, enforcing the sequence laminar → RANS → LES; and the
SA-BCM constant $C_{\mathrm{BC}2}$ is raised from 50 to 1000 to place
natural transition. The authors state that the first two apply to any
intermittency-based transitional DES-like model. The solver is an
incompressible modal DG with Pascal bases, artificial-compressibility Godunov
flux, BR2 and ROS3Pw, the solver already described on the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) page.

On the [Eppler 387](/benchmarks/eppler-387-airfoil.md) at $Re_c=300\,000$
fully turbulent IDDES misses the [laminar separation
bubble](/definitions/laminar-separation-bubble.md); the transitional hybrid
matches transitional RANS in attached flow and, as $N$ grows, approaches the
experiments at stall, predicting the 16° stall with $N=5$. On a supercritical
sphere ($Re_D=420\,000$) the modified shielding prevents an upstream shift of
transition from $N=3$ to $N=4$ and gives $C_D=0.083$ against Achenbach's 0.085.
On the [NACA 0012](/benchmarks/naca-0012-airfoil.md) at $Re_c=130\,000$,
$\alpha=11.5°$, the transitional variants at $N=4$ reproduce the low-frequency
bubble burst and reformation cycle. An equivalent
[Smagorinsky](/methods/smagorinsky-model.md) constant shows that the LES branch
acts as an explicit subgrid model, not as [implicit LES](/definitions/implicit-les.md).
The authors concede that SA-BCM triggers natural transition through its
eddy-viscosity term $T_2$, not $T_1$, and leave a general fix open.

# Version read

Version of record (Elsevier, open access; received 5 March 2026, revised
8 July 2026, accepted 9 July 2026, online 16 July 2026), 13 pages, all read;
pp. 2–3 read visually for the equations. Page 1 matches the Crossref metadata;
no identity issue. Numbering is that of this version.

# Key claims

Page-local symbols: $\gamma_{\mathrm{BC}}$ the algebraic intermittency of
SA-BCM (transition-page $\gamma$); $T_1$, $T_2$ its onset terms (not a
temperature); $C_{\mathrm{BC}1}=0.002$, $C_{\mathrm{BC}2}$ its constants
(not the SA ratio $\chi$); $Re_\Omega=d^2\lvert\Omega\rvert/\nu$ the vorticity
Reynolds number; $\chi_\infty=\tilde\nu_\infty/\nu$ the free-stream SA ratio;
$\hat f_d$, $\hat f_d^*$ the IDDES shielding (1 = RANS) and its modified form;
$\alpha_{\mathrm{ID}}=0.25-d/\Delta_{\max}$; $C_{S,\mathrm{eq}}$ the equivalent
Smagorinsky constant; $\phi$, $\phi_T$, $\phi_S$ the sphere angle from the
stagnation point, at transition and at separation.

1. DES-like hybrids cannot by default predict laminar-to-turbulent evolution; transition needs either a dynamic $C_{\mathrm{DES}}$ (Yin et al.; Yin & Durbin) or a transitional RANS background model (§1). **Stated**
2. In the authors' earlier study the DDES shielding can weaken and IDDES usually outperforms DDES thanks to its additional protection layer; only IDDES is used (§1). **Stated**
3. Replacing the whole IDDES filter width by $\Delta_\omega$ does not undermine IDDES, whose function rests mainly on $\hat f_d$; the IDDES width causes a fast eddy-viscosity decay in the grey area in their DG framework (§2.1). **Stated** (shown in the earlier paper)
4. No low-Reynolds correction is used, because high-order DG suits implicit LES and excess eddy viscosity is detrimental (§2.1). **Stated**
5. The SA-IDDES length is $l_{\mathrm{IDDES}}=\hat f_d(1+f_e)d+(1-\hat f_d)C_{\mathrm{DES}}\Delta$ with $C_{\mathrm{DES}}=0.65$, $\hat f_d=\max\{1-f_{dt},f_B\}$, $f_{dt}=1-\tanh[(8r_{dt})^3]$, $f_B=\min\{2\exp(-9\alpha_{\mathrm{ID}}^2),1\}$; the source term clips $\tilde\nu$ to $\max\{0,\tilde\nu\}$ and limits the SA $r$ to $r_{\max}=10$ (Crivellini et al. 2013) (§2.1, Eqs. 2–5). **Stated**
6. Change (1): in hybrid mode $s_{\tilde\nu}=\gamma_{\mathrm{BC}}\big[c_{b1}\tilde S\tilde\nu-c_{w1}f_w(\tilde\nu/l_{\mathrm{IDDES}})^2\big]+\frac{c_{b2}}{\sigma}\partial_i\tilde\nu\,\partial_i\tilde\nu$, both production and destruction multiplied, whereas pure RANS SA-BCM multiplies production only (§2.1.1, Eq. 6). **Stated**
7. SA-BCM: $\gamma_{\mathrm{BC}}=1-\exp\big(-\sqrt{T_1/C_{\mathrm{BC}1}}-\sqrt{C_{\mathrm{BC}2}T_2}\big)$, $T_1=\max\{Re_\Omega/(2.193Re_{\theta c})-1,0\}$, $T_2=\max\{\nu_t/\nu,0\}$, $Re_{\theta c}=803.73(Tu_\infty+0.6067)^{-1.027}$; the Spalart–Garbaruk correction $c_{w2,\mathrm{LRe}}=c_{w4}+c_{w5}/(\chi/40+1)^2$, $c_{w4}=0.21$, $c_{w5}=1.5$ (§2.1.1, Eqs. 7–8). **Stated**
8. Change (2): $\hat f_d^*=\max\{\hat f_d,1-\gamma_{\mathrm{BC}}\}$ keeps the shielding active wherever $\gamma_{\mathrm{BC}}<1$, forcing laminar → RANS → LES; the DDES analogue is $f_d^*=\min\{f_d,\gamma_{\mathrm{BC}}\}$ (§2.1.1, Eq. 9). **Derived** (definition); effect **Shown** in §3.2–3.3
9. Change (3): $C_{\mathrm{BC}2}$ is raised from 50 to 1000; Cakmakcioglu et al. tested up to 10 000 with minimal change of RANS $C_f$, but the authors observed that 1000 can already alter pure RANS solutions, so the change is recommended only for DES-like models (§2.1.1, §4). **Stated** / **Shown**
10. Changes (1) and (2) apply to all transitional DES-like models based on an intermittency function (§2.1.1, Abstract, §4). **Stated** (not tested on non-algebraic models)
11. The DG scheme is of order $N+1$ for all unknowns except pressure, of order $N$; $N_{\mathrm{dof}}=\prod_{m=1}^d(N+m)/m$ per element (§2.2). **Stated**
12. Eppler 387, $\alpha=0°$: transitional hybrid and transitional RANS curves overlap; $C_{\mathrm{BC}2}=1000$ slightly suppresses the bubble (early transition); $C_{\mathrm{BC}2}=50$ keeps the SA-BCM mean profiles but promotes instabilities downstream of the bubble; fully turbulent IDDES gives attached flow without a bubble (§3.1, Fig. 2, Table 3). **Shown**
13. With the original shielding the Eppler 387 results are practically identical to those with $\hat f_d^*$ (not reported) (§3.1). **Stated**
14. Eppler 387, $\alpha=8°$: with $C_{\mathrm{BC}2}=50$ transition resembles a separation-induced process; with 1000 transition sits at $x/c\approx0.2$ as in McGhee (1988) and the solution stays in RANS mode; only for 50 is $T_2$ preceded by $T_1$, at $x/c>0.6$ (§3.1, Figs. 3–5). **Shown**
15. In natural transition SA-BCM does not work as designed: $\gamma_{\mathrm{BC}}$ is activated by $T_2$, so onset depends almost entirely on $\chi_\infty$ and $C_{\mathrm{BC}2}$; a fix should act on $T_1$ (better $Re_{\theta c}$ correlations or a local substitute for $Tu_\infty$) (§3.1–3.2, §4). **Shown** (diagnosis) / **Stated** (remedy)
16. Eppler 387, $\alpha=14°$ and 16°: the transitional hybrid with $\hat f_d^*$ approaches the experiments as $N$ grows; at 16° $N=5$ predicts stall over the whole suction side, which RANS cannot; fully turbulent IDDES under-predicts the separated region (§3.1, Figs. 6–7, Table 3). **Shown**
17. Eppler 387 at 16° (Table 3): hybrid with $\hat f_d^*$ $C_L=1.169$, $C_D=0.300$ ($N=5$); 1.139, 0.314 ($N=4$, 395 325 degrees of freedom); fully turbulent IDDES 1.427, 0.119 ($N=3$); experiments $C_L=0.99$ (McGhee) and $C_L=1.09$, $C_D=0.25$ (Emmerson & Verstraete). **Shown**
18. Sphere, $Re_D=420\,000$: with $C_{\mathrm{BC}2}=50$ transition is separation-induced, separation "anticipated down to $\phi\approx105°$" (text); with 1000 natural transition precedes turbulent separation at $\phi\approx120°$ (§3.2, Fig. 9). **Shown**
19. Sphere: with the original shielding, $N=3\to4$ moves transition upstream ($\phi_T=102°\to79°$), with $\hat f_d^*$ it does not ($97°\to96°$); at $\phi=95°$, $N=4$, $\delta^+=1240$ against 600 with $\hat f_d^*$, read as $\hat f_d^*$ preventing a mesh-induced switch from laminar flow directly to LES (§3.2, Table 5, Fig. 11). **Shown**
20. Sphere drag with $\hat f_d^*$: $C_D=0.095$ ($N=3$), 0.083 ($N=4$), $\phi_T=96°$, $\phi_S=118°$ against Achenbach's 0.085, 98°, 119°; unsteady SA-BCM ($N=3$) 0.375, 123°, 130° (Table 5). **Shown**
21. The correct sphere transition owes partly to calibrated inflow ($\chi_\infty=0.001$, chosen to put onset at the experimental location) (§3, §3.2, Table 1). **Stated**
22. NACA 0012, $\alpha=11.5°$: fully turbulent IDDES has too much eddy viscosity (mild separation from $x/c\approx0.2$, no proper bubble); steady SA-BCM separates over almost the whole suction side; the transitional hybrids give a chaotic signal at $N=3$ and capture both phases of the cycle at $N=4$ ($C_L\approx1$ attached with a small bubble, $C_L\approx0.5$ stalled) (§3.3, Figs. 14–15). **Shown**
23. Cycle Strouhal number: 0.0077 (original shielding) and 0.0097 ($\hat f_d^*$) against 0.008 (Rinoie & Takemura) and 0.0083 (AlMutairi et al.) (§3.3). **Shown**
24. At $N=4$ the mean $C_L$ lies between the LES of AlMutairi et al. (0.714) and the experiment (0.880), and $C_D$ equals the LES value (0.127) with about two orders of magnitude fewer degrees of freedom and a time step about 50 times larger (§3.3, Table 7). **Shown** (cost **Stated**)
25. On the NACA 0012 the solver behaves as WMLES even in attached flow and never returns to pure RANS after stall (§3.3). **Shown**
26. The LES branch acts as a subgrid model, not as implicit LES: $C_{S,\mathrm{eq}}=\sqrt{\nu_t/(\Delta^2\lvert\Omega\rvert)}$ with $\Delta=V^{1/3}$ is about 0.5 in RANS-dominated regions and 0.1–0.2 over most of the LES region, with a plateau of 0.14 at $x/c=0.4$; the modelled stress dominates near the wall at $x/c=0.2$ and contributes about 10% at 0.4 (§3.3, Eq. 14, Fig. 16). **Shown**
27. $\hat f_d^*$ divides the laminar, RANS and LES regions more consistently on the NACA 0012 (§3.3, Fig. 13). **Shown**
28. Drawbacks of change (3): it slightly suppresses the bubble without massive separation, and the natural-transition location depends strongly on $C_{\mathrm{BC}2}$ and must be balanced against $\chi_\infty$; benefit: complete near-wall penetration of $\gamma_{\mathrm{BC}}$ in massively separated flows (§4). **Shown** / **Stated**

*(Compiler check, not in the sources:)* with
$N_{\mathrm{dof}}=20$, 35, 56 per element for $N=3$, 4, 5 in three
dimensions, the printed totals $7644\times\{20,35,56\}=152\,880$, 267 540,
428 064 (Eppler 387), $53\,360\times\{20,35\}=1\,067\,200$, 1 867 600 (sphere)
and $9650\times\{20,35,56\}=193\,000$, 337 750, 540 400 (NACA 0012) all
follow. Eq. (1) prints the diffusive flux of $\tilde\nu$ as
$-(\nu+\tilde\nu)\partial_i\tilde\nu$ with no $1/\sigma$, while the cross term
of Eq. (2) carries $c_{b2}/\sigma$; the two printed equations pair the factor
differently.

# Printed slips

- **Eq. (3):** "$r=r^*$, $0\le r<r_{\max}$; $r_{\max}$, $r<0$ or $r\ge r_{\max}$": the case conditions are written on $r$ while defining $r$.
- **§3.2 against Table 5:** the text places separation for $C_{\mathrm{BC}2}=50$ at "$\phi\approx105°$", Table 5 prints $\phi_S=99°$ (and $\phi_T=99°$) for that case at $N=3$.
- **Eq. (8):** $\chi$ is not defined in the paper.
- **§3.3:** "$\Delta t=4\times10^{-3}$" printed without units.
- **Table 5:** "IDDES$_{TRA}$ ($\chi_2=50$)" does not name its shielding function, while Table 3 writes "IDDES$_{TRA}$ ($\chi_2=50$, $\tilde f_d^*$)".
- **§3.2:** "$\phi_T$ being push backward with the standard $f_d$"; **§2.1:** "neat of gravitational effects".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $k$ | $N$ | polynomial degree; **collision** with the turbulent kinetic energy $k$ |
| $N_{dof}$, $N_{DOF}$ | $N_{\mathrm{dof}}$, (total) | Pascal basis |
| $\mathbf w=[p,u_i,\tilde\nu]$, $p=P/\rho$ | $p$ (kinematic), $u_i$, $\tilde\nu$ | incompressible |
| $C_{b1},C_{b2},C_{w1},C_{w4},C_{w5}$ | $c_{b1},c_{b2},c_{w1},c_{w4},c_{w5}$ | SA constants as in the original model |
| $\tilde S$, $f_w$, $r^*$, $r$ | $\tilde S$, $f_w$, $r$ | SA functions |
| $d_w$, $\tilde d$ | $d$, $l_{\mathrm{IDDES}}$ | as on the DES page |
| $\tilde\Delta_\omega$ | $\Delta_\omega$ | Mockett et al.; divided by $N+1$ |
| $\Delta_{IDDES}$ | IDDES width ($\Delta_{dw}$ on the DES page) | not used here |
| $h_{max}$ | $\Delta_{\max}$ | |
| $\tilde f_d$ | $\hat f_d$ | IDDES shielding, 1 = RANS; **opposite convention to $f_d$** |
| $\tilde f_d^*$, $f_d^*$ | $\hat f_d^*$, $f_d^*$ (page-local) | this paper |
| $\alpha=0.25-d_w/h_{max}$ | $\alpha_{\mathrm{ID}}$ (page-local) | **collision** with the DG blending $\alpha$ and the angle of attack |
| $\gamma_{BC}$ | $\gamma_{\mathrm{BC}}$ (page-local) | transition-page intermittency |
| $\chi_1$, $\chi_2$ | $C_{\mathrm{BC}1}$, $C_{\mathrm{BC}2}$ (page-local) | **collision** with the SA ratio $\chi$ |
| $\chi$ (Eq. 8) | $\chi$ | SA ratio, undefined in the paper |
| $T_1$, $T_2$ | $T_1$, $T_2$ (page-local) | onset terms; **collision** with the temperature $T$ |
| $Re_\omega=d_w^2\Omega/\nu$ | $Re_\Omega$ (page-local) | **collision**: $\omega$ is the specific dissipation rate |
| $\Omega$ | $\lvert\Omega\rvert$ | vorticity magnitude |
| $Re_{\theta c}$, $Tu_\infty$ | $Re_{\theta c}$, $Tu$ | |
| $\tilde\nu_\infty/\nu$ | $\chi_\infty$ | free-stream value |
| $\tilde C_S$ | $C_{S,\mathrm{eq}}$ (page-local) | Eq. 14; the tilde is not a Favre filter |
| $\Delta^+_{y,w}$ | $y_1^+$ | divided by $N+1$ |
| $\phi$, $\phi_T$, $\phi_S$, $\delta^+$ | page-local | sphere angles; boundary-layer thickness in wall units |
| $s$, $m_j$, $\gamma_{ii}$, $a_{ij}$, $c_{ij}$ | (ROS3Pw coefficients) | $\gamma_{ii}$ is not the intermittency |
| $[[\circ]]=\circ^+-\circ^-$ | $[\![\cdot]\!]$ | interface jump |
| $\lambda_2$ | (vortex criterion) | isosurfaces $\lambda_2=-1$ |
| $Re_c$, $Re_D$ | $Re_c$, $Re_D$ | chord, diameter |

# Reference list

35 printed references, author–year (Elsevier Harvard) style, alphabetical.
The list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. "Alberti et al., 2025" is the ingested
[alberti-2025-b](/sources/alberti-2025-b.md) (same DOI, printed "Comput. &
Fluids 106686" without volume); Möller et al. (2024) is the ingested
[moller-2024](/sources/moller-2024.md). Basile et al. (2022, AIAA SciTech) is
a different work from the ingested Basile et al. (2023). Two Yalçın 2021
items (a PhD thesis and an ETMM paper) take suffixes in printed order; Yin et
al. (2015) prints no page or article number; McGhee (1988) is NASA TM 4062,
printed as "vol. 4062". No item is unparseable.

# Pages created or updated

Chunk 16 (2026-10-29). This source is cited on:

- [Eppler 387 airfoil](/benchmarks/eppler-387-airfoil.md)
- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
