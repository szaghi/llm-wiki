---
type: Source
title: "Batther & Lee (2022) — Numerical investigation of a pitching airfoil undergoing dynamic stall using Delayed Detached Eddy Simulations"
description: "DDES with four RANS closures (SST Langtry–Menter, SA Medida–Baeder, SA amplification-factor transport, fully turbulent SA) of a NACA 0012 pitching up at Re 200,000, compared with wall-resolved LES: laminar-bubble bursting, dynamic-stall-vortex formation, slightly early stall and lower peak lift."
resource: "doi:10.1016/j.compfluid.2022.105691"
source_kind: paper
authors: [Batther J., Lee S.]
year: 2022
venue: "Comput. Fluids 249:105691"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Computers_amp_Fluids_Batther_Numerical_investigation_of_a_pitching_airfoil_undergoing_dyn.pdf"
tags: [des, hybrid-rans-les, transition, separated-flow, rans]
timestamp: 2026-10-28T11:47:00Z
---

# Summary

Batther & Lee (2022) ask whether
[delayed detached-eddy simulation](/methods/detached-eddy-simulation.md)
(DDES) coupled to RANS transition models can reproduce the onset of
[dynamic stall](/definitions/dynamic-stall.md) that the wall-resolved
[LES](/definitions/large-eddy-simulation.md) of Visbal and Garmann (2018)
revealed for a [NACA 0012](/benchmarks/naca-0012-airfoil.md) pitching up
at a constant rate, at $Re_c=2\times10^5$ and $M=0.1$. The question is
taken verbatim from Visbal and Garmann, and the authors claim the
detailed DDES-against-LES comparison of stall onset as new. The code is
NASA's OVERFLOW 2.3 (fifth-order central differences with scalar
dissipation, 30 sub-iterations per step) on a $0.1c$ span. The retained
grid has about 16 million points, about 22% of the LES's 74 million.
Four RANS closures are compared inside DDES: the SST
Langtry–Menter and SA Medida–Baeder $\gamma$-$Re_\theta$
[local-correlation transition models](/methods/local-correlation-based-transition-model.md)
(built on [SST](/methods/k-omega-sst-model.md) and
[Spalart–Allmaras](/methods/spalart-allmaras-model.md)), Coder's
SA amplification-factor-transport (AFT) model, and fully turbulent SA. No
DDES formulation and no model equations are printed.

With every transition model, DDES stalls slightly earlier and with a
slightly lower peak lift than LES, but it reproduces the sequence the LES
showed. Transition moves upstream and a leading-edge
[laminar separation bubble](/definitions/laminar-separation-bubble.md)
forms. The bubble then bursts under the adverse pressure gradient
("suction collapse"). The separated shear layer rolls up into the
dynamic-stall vortex, which convects to 40–50% chord and sheds. DDES
gives a larger bubble with weaker reverse flow, earlier suction collapse
and faster vortex convection. SA-AFT comes closest to LES, and SST
Langtry–Menter stalls earliest. Fully turbulent SA
underpredicts lift at low incidence and forms an abrupt turbulent
separation bubble instead of a laminar one. The paper presents
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) as giving LES-like
stall physics at a fraction of the LES cost. The effect of the numerical
scheme ([numerical dissipation](/properties/numerical-dissipation.md)) on
the transition models is left open.

# Version read

Version of record (Comput. Fluids 249:105691, open access; received 31 May
2022, accepted 4 October 2022), 17 pages, all read; pp. 2–3 also checked
visually for Eq. 1 and Tables 1–2. Page-1 title, authors and DOI match the
metadata above. No identity problem. Numbering on this page is that of
this version.

# Key claims

1. DDES with all transition models studied predicts the onset of lift stall slightly earlier and the peak lift coefficient slightly lower than the LES of Visbal and Garmann (Abstract, §4.5, Fig. 17). **Shown**
2. DDES captures the formation and collapse of the leading-edge laminar separation bubble and the subsequent formation of the dynamic-stall vortex that appear in LES (Abstract, §4.2.5, §4.5, Fig. 14). **Shown**
3. Coder's SA amplification-factor-transport model gives the closest match to LES (Abstract, §4.3.1, §5). **Shown**
4. SST Langtry–Menter gives the earliest stall onset; the two SA-based transition models give similar stall onsets; SA Medida–Baeder oscillates at lower angles of attack (§4.3.1, Fig. 17). **Shown**
5. The earlier stall with SST Langtry–Menter follows from an earlier loss of suction, which lets the vortex form and leave the surface sooner; the vortex takes about three stages, "approximately over 2° angle of incidence", from formation to peak strength (§4.3.1, Fig. 20). **Shown** (explanation **Stated**)
6. From suction collapse ($\alpha=16.9^\circ$) to stall onset ($\alpha=23.2^\circ$) the $C_p$ distributions of all transition models are similar: a "common ground for the flow physics post suction collapse, regardless of the transition model" (§4.3.1, Figs. 18–20). **Shown**
7. Fully turbulent SA DDES underpredicts lift at lower angles of attack but follows the LES trends at larger ones; it forms an abrupt turbulent separation bubble at $\alpha=14.1^\circ$–$14.5^\circ$ instead of a laminar one, a behaviour that "has not yet been documented in literature", and shows more trailing-edge separation, which does not propagate upstream to burst the bubble (§4.4, Figs. 17, 21, 22). **Shown**
8. A fully turbulent model "in a low Reynolds number regime may not be optimal" (§4.4). **Stated**
9. Against LES, DDES shows a larger bubble at $\alpha=15.2^\circ$ with smaller reverse-flow velocity, more oscillations around the bubble even after spanwise averaging, earlier suction collapse (the LES profile at $17.4^\circ$ resembles DDES at $15.2^\circ$) and faster vortex propagation (§4.2.5, §4.5, Fig. 14). **Shown**
10. The stall is of the leading-edge "pressure gradient bubble bursting" type, not "turbulent leading-edge" stall: reversed flow near the trailing edge (negative $C_f$) does not propagate upstream during the motion (§4.2.2, Fig. 7b, §4.2.5, §4.3.1). **Shown**
11. The bubble bursting is the initial trigger of the dynamic-stall process; the bubble's history before collapse "seemingly does not have a significant impact" on vortex formation (§4.2.3, §4.2.5, §4.3.1). **Shown** (interpretation agreeing with Visbal and Garmann)
12. Lift keeps increasing linearly after suction collapse, unlike static stall; the lift-curve slope rises suddenly at about $\alpha=18.6^\circ$ owing to vortex formation, as also documented by earlier studies (§4.2.3, Table 3, Fig. 5). **Shown**
13. The vortex reaches maximum strength at about 40% chord and then sheds, coinciding with peak lift just before stall onset; Table 3 places its detachment at "roughly 50% chord length" (§4.2.3, Table 3, Fig. 12b). **Shown**
14. Long slender streamwise vortices ("vortex sheets", $Q=100$) form at $\alpha\approx18^\circ$, shift rapidly across the span and persist beyond stall; the authors hypothesise that they trigger the vortex detachment and an earlier stall (§4.2.4, Fig. 13). **Shown** (presence) / **Stated** (hypothesis)
15. Two distinct reattachment branches behind the bubble at $\alpha=15.2^\circ$ explain the two kinks in the pressure-recovery region of $C_p$ (§4.2.2, §4.2.5, Figs. 6a, 15c). **Shown**
16. Transition, identified by a non-zero eddy viscosity at the first grid point, moves rapidly upstream after $\alpha=8^\circ$; a laminar separation bubble first forms near $\alpha=10^\circ$ (§4.2.3, Fig. 8). **Shown**
17. Strong high-frequency surface-pressure oscillations at $x/c=0.05$ precede vortex formation, as in the experiment of Lorber and Carta; the instantaneous minus low-pass-filtered pressure spikes before the bubble forms, "which might be crucial" for flow-control design (§4.2.5, Fig. 16). **Shown**
18. Grid sensitivity: Grids 2 and 3 give similar loads and stall inception, Grid 1 stalls early, and all grids underpredict the LES peak lift; Grid 2 ($811\times200\times100$) is retained (§4.2.1, Fig. 4). **Shown**
19. Grid 2 achieves the two-order sub-iteration residual drop up to about $\alpha=28^\circ$, which "confirms that 30 sub-iterations are sufficient" (§4.2.1, Fig. 4d). **Shown**
20. Grid 2 took "roughly 20 s per time step using 192 cores", "about 1500 total CPU hours", against LES that "typically requires several million CPU hours" (§4.2.1). **Stated** (see Printed slips)
21. The DDES uses about 22% of the LES grid points and, by §4.5, "a time step of roughly 8% of that used in LES", while §2.1 calls the DDES time step "one order of magnitude larger" than the LES one (§2.1, §4.5). **Stated** (contradictory, see Printed slips)
22. A 2-D static RANS validation (point count of Grid 2) at $M=0.1$, $Re_c=10^6$ agrees with the measured $C_L$, $C_D$ and pitching moment of Hristov and Ansell up to static stall (§4.1, Fig. 3). **Shown**
23. Visbal and Garmann found that spans from 10% to 120% chord do not change the overall flow features of this case, so a 10%-chord span is used (§2.1). **Stated** (cited)
24. The mean $y^+$ of the first point is about 0.4 on the upper surface for all grids (§2.2, Table 2). **Shown**

# Printed slips

- **Time step, §2.1 against §4.5:** "this time step ($\Delta t^*$) is one order of magnitude larger than that used in LES for the same case" against "a time step of roughly 8% of that used in LES". Both cannot hold.
- **Cost, §4.2.1** *(compiler check, not in the sources)*: "roughly 20 s per time step using 192 cores", over the printed "35,000 steps during the upstroke motion", gives $35{,}000\times20\ \mathrm s\approx194$ h of wall time, about $3.7\times10^4$ core-hours, not the printed "about 1500 total CPU hours".
- **§4.2.2:** "from stage 3 ($\alpha=10.6^\circ$) to stage 7"; Table 3 gives stage 3 at $12.9^\circ$ and stage 2 at $10.6^\circ$.
- **Table 2 note:** "$\overline{\Delta x^+}, \overline{\Delta x^+}, \overline{\Delta x^+}$ indicate the grid spacings averaged across the airfoil upper surface"; the column headers read $\overline{\Delta x^+}$, $\overline{\Delta y^+}$, $\overline{\Delta z^+}$.
- **§4.3.1:** the sentence "The SST Langtry–Menter model shows the earliest onset of stall while both SA models show similar points of stall onset" is printed twice in succession.
- **§2.1:** "Ligget and Smith" for reference [13] "Liggett N, Smith M".
- **Eq. 2:** $\nu$ is used for the second generalized coordinate.
- **Vortex detachment:** "roughly 40% chord length, from which the DSV starts to shed" (§4.2.3) against "up until roughly 50% chord length where it detaches" (Table 3, stage 7).
- **References:** [15] prints its author list twice ("Jespersen D, Pulliam T, Buning P, Jespersen D, Pulliam T, Buning P"); [8] and [10] print no volume ("J Fluid Mech 2019;860–85", "2019;870–900").
- **Typos:** "hybrod LES" (§1), "cyle-to-cyle" (§1), "beings to roll up" (§4.2.3), "early of onset" (§4.3.1), "AIAA avitation 2020 forum" (ref. [17]).

# Notation map

| Batther & Lee | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\alpha$ | $\alpha$ (page-local: angle of attack) | **collision** with the registry's DG blending factor; page-local as on the [NACA 0012 page](/benchmarks/naca-0012-airfoil.md) |
| $\dot\alpha(t^*)=\psi_\circ^+(1-e^{-4.6t^*/t_\circ})$ | pitch rate with $\dot\alpha_0^+=0.05$, $t_0=0.5$ (page-local, as on [dynamic stall](/definitions/dynamic-stall.md)) | Eq. 1 |
| $t^*=tU_\infty/c$, $\Delta t^*=0.000256$ | (convective time, time step) | |
| $Re$ | $Re_c$ | chord Reynolds number, $2\times10^5$ |
| $M$ | $M$ | 0.1 |
| $\xi,\nu,\zeta$ | (generalized coordinates) | **collision:** $\nu$ is the kinematic viscosity in the registry |
| $C_L$, $C_l$, $C_D$, $C_M$, $C_p$, $C_f$ | $C_L$, $C_D$, $C_p$, $C_f$ (+ $C_M$ pitching moment) | upper and lower case both used for lift |
| $\langle C_p\rangle$, $\langle C_p\rangle_{lpf}$ | (spanwise-averaged; spanwise-averaged and low-pass-filtered $C_p$) | **collision:** $\langle\cdot\rangle$ is a spanwise average here, a Reynolds average in the registry |
| $\Delta x^+$, $\Delta y^+$, $\Delta z^+$ | $\Delta x^+$, $\Delta y^+$, $\Delta z^+$ | at $x/c=0.8$; overbar = upper-surface mean (not an LES filter) |
| $\gamma$–$\widetilde{Re}_{\theta t}$ | $\gamma$-$\mathcal R_{\theta t}$ | intermittency and transported onset Reynolds number, as on the [transition-model page](/methods/local-correlation-based-transition-model.md) |
| AFT | (amplification-factor transport) | Coder & Maughmer |
| LSB, DSV, TEV | (laminar separation bubble, dynamic-stall vortex, trailing-edge vortex) | |
| $Q$ | (Q-criterion) | iso-value 100, units not printed |

# Reference list

39 printed references, numbered, Elsevier abbreviated form, most with DOIs
printed as `http://dx.doi.org/` links. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Same-author
same-year works take suffixes in printed order (Jia & Lee 2020, [20],
[21]; Jia & Lee 2022, [22], [23]). Incomplete or malformed items: [8] and
[10] print no volume, [15] prints its author list twice (entered once),
[22] and [23] print no DOI; [31] and [34] are NASA reports, and nine items
are conference papers. No printed duplicates.

# Pages created or updated

Chunk 8 (2026-10-27). This source is cited on:

- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [Dynamic stall](/definitions/dynamic-stall.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
