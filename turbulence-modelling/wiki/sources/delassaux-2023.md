---
type: Source
title: "Delassaux et al. (2023) — Numerical analysis of unsteady flow features around a realistic Estate vehicle with hybrid RANS/LES methods"
description: "Compares realizable k-ε and k-ω SST RANS with SST-based delayed detached-eddy simulation on a full-scale simplified Estate car against S2A wind-tunnel data: RANS matches the drag by error cancellation, DDES reproduces the single-bubble wake, and a too-fine surface mesh triggers grid-induced separation."
resource: "doi:10.1016/j.compfluid.2023.105935"
source_kind: paper
authors: [Delassaux F., Mortazavi I., Herbert V., Ribes C.]
year: 2023
venue: "Comput. Fluids 262:105935"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Computers_amp_Fluids_Delassaux_Numerical_analysis_of_unsteady_flow_features_around_a_realis.pdf"
tags: [hybrid-rans-les, des, rans, separated-flow, grid-requirements]
timestamp: 2026-10-28T07:08:00Z
---

# Summary

Delassaux et al. (2023) validate steady RANS against
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) for the full-scale flow
around a simplified production car, a 2013 Peugeot 308 SW (an Estate, or
squareback, shape) with closed inlets, a smoothed underbody and wheels
replaced by fairings. The procedure was calibrated earlier by the authors on
four 25° [Ahmed bodies](/benchmarks/ahmed-body.md) and is transposed here.
Three models run in ANSYS Fluent 2020R2 (incompressible, cell-centred finite
volume, bounded central differencing for convection): the realizable
[$k$-$\varepsilon$ model](/methods/k-epsilon-model.md) with a two-layer
near-wall treatment, the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md),
and SST-based delayed [detached-eddy simulation](/methods/detached-eddy-simulation.md).
The flow is at $V_\infty=140$ kph and a printed $Re=1.3\times10^7$ (vehicle
length), on tetrahedral grids of 115M and 180M cells with 20 prism layers at
$y^+\approx1$, against in-house S2A wind-tunnel data (balance, 90 pressure
taps, PIV, multi-hole-probe wake planes).

The RANS models give $C_D=0.242$ against the measured 0.244 and DDES gives
0.255, yet a cumulative-drag analysis shows that the RANS agreement comes from
error cancellation along the car. DDES reproduces the measured wake: a single
large recirculation bubble fed by the rising underbody flow and capped by the
roof shear layer, where both RANS models overpredict the recirculation. On
rounded separation lines SST is closest to the measurements, and DDES
underpredicts $C_p$ there. The authors trace this to grid-induced separation:
a 3 mm surface mesh is too fine there, and 6 mm is advised, in line with
Menter's criterion on the ratio of the largest cell size to the boundary-layer
thickness. The [numerical dissipation](/properties/numerical-dissipation.md)
of the convection scheme and the CFL number are chosen from the Ahmed-body
experience. A DDES run costs 18 times the wall-clock time of a RANS run.
Section 4.1 places the work in a taxonomy of scale-resolving methods
([implicit LES](/definitions/implicit-les.md),
[wall-modelled LES](/methods/wall-modelled-les.md),
[DNS](/definitions/direct-numerical-simulation.md)) and cites Spalart's
forecast of [grid requirements](/results/les-grid-point-requirements.md)
(wall-resolved LES and DNS of a full-scale geometry in 2050 and 2080).

# Version read

HAL author manuscript hal-04103180v1 (deposited 2 October 2023), 31 PDF pages
(a HAL cover page and 30 manuscript pages numbered 1–30), all read; the
equation pages were also checked visually. The manuscript is titled
"Computational analysis of unsteady flow features around a realistic Estate
vehicle with hybrid RANS/LES methods", whereas the Crossref record of the
published version reads "Numerical analysis …"; authors, venue, volume,
article number and DOI agree, and the HAL cover page names the published
article, so it is the same work. Section, equation, table and figure numbers
cited on this page are those of the manuscript.

# Key claims

1. Realizable $k$-$\varepsilon$ and SST RANS give $C_D=0.242$ on the Reference grid (20 prism layers), against the measured $C_D=0.244$; SST DDES gives $C_D=0.255$ (§6, Table 3). **Shown**
2. Going from 20 to 30 prism layers leaves $C_D$ essentially unchanged for all three models (0.242→0.242, 0.242→0.241, 0.255→0.254) (§6, Table 3). **Shown**
3. Halving the cell size of the wake and underbody boxes (Refined grid) gives $C_D$ = 0.243 (realizable $k$-$\varepsilon$), 0.249 (SST), 0.254 (DDES), and DDES mean velocity fields on the symmetry plane "almost exactly the same" as on the Reference grid, which is retained (§6, Table 3, Fig. 14). **Shown**
4. Hybrid RANS/LES does not give better integrated loads than RANS on the realistic car; the authors call this "well known" for DDES/LES and PANS ([partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)), citing refs. [11], [47], [32], [53] (§6). **Shown** (own data), **Stated** (literature)
5. The RANS drag agrees by error cancellation: the cumulative drag of realizable $k$-$\varepsilon$ and DDES differs around the front fairings, is almost the same for $X\in[0.5,2.5]$ m and differs mainly at the rear ($X>2.5$ m); "There is no valid reason that RANS predicts a more accurate $C_d$ than DDES" (§6, Fig. 13). **Shown** (interpretation **Stated**)
6. Lift is "globally not accurate for all cases" and is not shown, partly because the balance may be affected by the absence of wheels touching the ground (§6). **Stated**
7. On the rear pressure lines (Y0, Y500), SST DDES matches the measurements in the separated region, whereas RANS is better on the roof (§7.2, Figs. 15–16). **Shown**
8. In the symmetry plane, DDES reproduces the size of the recirculation bubble and the mean velocity fields; RANS produces an underbody jet far into the wake that the experiment does not show, SST predicts two massive separation bubbles, and realizable $k$-$\varepsilon$ lies between SST and DDES (§7.2, Figs. 17–18). **Shown**
9. The Estate wake is one large recirculation bubble: the underbody flow rises (the ascending underbody exit acts as a diffuser) and is bounded above by the roof shear layer, unlike the two stacked bubbles of Notchback and Fastback wakes; this region is "responsible of more than one third of the total drag contribution" (§7.6, §8). **Shown** (drag fraction **Stated**)
10. In the upper wake plane Z970, realizable $k$-$\varepsilon$ predicts the streamwise velocity better than both SST models, and SST RANS and DDES slightly underestimate the separation length (§7.2, Fig. 19). **Shown**
11. On rounded separation lines (probes 41 and 44), SST is closest to the measurements, realizable $k$-$\varepsilon$ overpredicts and DDES underpredicts $C_p$; on the sharp rear lump (probe 49) DDES is the most accurate, consistent with the authors' Ahmed-body findings (§7.3, Fig. 20). **Shown**
12. Along line L1 a 3 mm surface mesh is "too fine and leads to GIS" (grid-induced separation); 6 mm and 10 mm surface meshes give better $C_p$ in the rounded separation area, and 6 mm is advised (§7.3, Fig. 21). **Shown**
13. Around the rear-right fairing (2D PIV), SST predicts massive separation, realizable $k$-$\varepsilon$ a larger and DDES a smaller recirculation than measured; surface and volume refinement did not change this (§7.4, Fig. 23). **Shown**
14. On the underbody, DDES best captures $C_p$ near separation, and on plane Z320 DDES shows "an almost perfect match" of the three velocity components, while both RANS models overestimate the recirculation (§7.5, Figs. 24–26). **Shown**
15. In the X100 cross-plane, RANS shows a massive outward expansion of the underbody flow, DDES captures the vertical velocity behind the rear window and bumper, and four vortical structures are identified in the streamwise vorticity; RANS overestimates their intensity (§7.6, Figs. 27–28). **Shown**
16. A RANS run takes about 2 hours on 384 cores and a DDES run about one and a half days on 1152 cores; "The hybrid RANS/LES simulation is 18 times more expensive than the RANS computation" (§7.6). **Stated** (see Printed slips)
17. Ahmed-body recap of ref. [12]: realizable $k$-$\varepsilon$ gives no separation on the 25° slant and SST massive separation; SAS, SST DDES and SST SBES all separate and reattach, with SAS overestimating and SBES underestimating the recirculation length and DDES the closest; SST DDES is selected (§5). **Stated** (results of ref. [12])
18. Ahmed-body recap: with the 20-layer grid and $\Delta t=5\times10^{-5}$ s, SST DDES gives maximal errors of 3.3% on drag and 7.1% on lift over the four bodies (§5, Table 2). **Stated** (from ref. [12], tabulated)
19. Ahmed-body recap: $\Delta t=1.5\times10^{-5}$ s and $5\times10^{-5}$ s give globally the same results, the latter with a maximum CFL of 3 in the separation area; a CFL above 10 gives no separation or massive separation on the slant (§5). **Stated** (from ref. [12])
20. Ahmed-body recap: $y^+<1$ and "at least 15 or 20 prism layers" are needed (30 better with sharp edges), a 5 mm tetrahedron edge in the wake, and Menter's criterion gives a 3 mm minimal surface size (§5). **Stated** (from ref. [12])
21. Raising the DDES shielding constant $C_{d1}$ from 20 to 30 increases the shielding of the boundary layer, as observed on the Ahmed body, and is "then advised for this case" (§4.4). **Stated**
22. A maximum CFL of 5 in the LES region is advised from experience, above which turbulent structures can be badly computed or vanish; the time step used gives "a CFL number below 2 around the car" (§4.2). **Stated**
23. Citing Menter (ref. [26]), with $r=\Delta_{\max}/\delta$ the impact of grid refinement is delayed to $r<0.2$ in DDES against $r<1$ in DES (§4.1.3). **Stated** (cited)
24. Under local equilibrium (production equal to dissipation), the DDES subgrid model reduces to the Smagorinsky–Lilly model ([Smagorinsky model](/methods/smagorinsky-model.md)), citing ref. [42]; no derivation is printed (§4.1.3). **Stated**
25. Keeping the first-cell height and total height with 30 prism layers requires a growth ratio of 1.23, within the recommendation of Spalart & Streett (ref. [45]) of a ratio below 1.25 for hybrid methods ([boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md)) (§4.4). **Stated**
26. Literature summary: for Fastback and Notchback DrivAer shapes RANS can predict flow and loads with a wall-resolved grid, whereas for the Estate hybrid RANS/LES is required to predict the wake and the loads (§1). **Stated**
27. Cited cost figure: Goc et al. (ref. [16]) ran WMLES of an aircraft in landing configuration on 157 million cells, 30 flow passes in 7.5 days on 2000 CPU cores against 7 hours on 96 GPUs (§4.1). **Stated** (cited)
28. Cited accuracy figure: Menter et al. (ref. [31]) report wall-function LES of the Notchback DrivAer on GPUs with drag errors of 24 counts (SBES), 10 counts (250M-cell LES) and 2 counts (500M-cell LES) (§1). **Stated** (cited)

# Printed slips

- **Refined-grid size.** The abstract ("Two grids with 115 and 185 million elements") and the Fig. 10 caption ("Refined grid - 185M elements") give 185M; §4.4, §6 and §8 give "180M cells".
- **Table 3 sign.** The 30-prism-layer DDES row prints $C_D=0.254$, $\Delta C_D=-0.010$; every other row uses $\Delta C_D=C_D-0.244$, which here gives $+0.010$ *(compiler check, not in the sources)*.
- **Number of refinement boxes.** §4.4 says "A total of 8 refinement boxes"; the itemised list and Table 1 have nine (BW, BW1, BW2, BW3, UB, Exit UB, Fairings, Spoiler, Window).
- **Viscosity units.** §4.3 prints "kinematic viscosity $\nu=1.7894\times10^{-5}$ kg/m.s"; the units are those of a dynamic viscosity. With the printed $\rho=1.204$ kg/m³ the kinematic viscosity is $1.486\times10^{-5}$ m²/s *(compiler check, not in the sources)*.
- **Non-dimensional times.** With $V_\infty=140$ kph and $L_v=4.585$ m, $\Delta t\,V_\infty/L_v=4.24\times10^{-4}$ (printed 0.00044), 3 s are 25.4 transit times (printed "27") and 1.5 s are 12.7 (printed "14 transit times (1.5 seconds of physical time)"); with $\nu=1.486\times10^{-5}$ m²/s, $Re=1.20\times10^7$ (printed $1.3\times10^7$) *(compiler check, not in the sources)*.
- **Balance precision.** "Drag ($C_d$) and lift ($C_l$) coefficients have respectively a precision of 0.002 and 0.03 [55], corresponding to a measurement error of 0.3% and 3.5%"; $0.002/0.244=0.82\%$ *(compiler check, not in the sources; the basis of the printed percentage is not stated)*.
- **Cost ratio.** "18 times more expensive" is the wall-clock ratio (36 h against 2 h); at the printed core counts the core-hour ratio is $1152\times36/(384\times2)=54$ *(compiler check, not in the sources)*.
- **Prism-layer height.** The text keeps the total prism height constant ("45 mm on the vehicle"); with $h_1=0.020$ mm, 20 layers at ratio 1.4 sum to 41.8 mm and 30 layers at ratio 1.23 to 43.2 mm *(compiler check, not in the sources)*.
- **Table 2.** From the printed three-digit values, the roof-rounded and side-plus-roof-rounded drag errors are $\pm0.34\%$, printed $0.7$ and $-0.7$; the other six percentages of the table reproduce *(compiler check, not in the sources)*.
- **Cross-reference.** §5 refers to "Menter's criterion, detailed in Sect. 4.1.2"; the criterion is in §4.1.3.
- **Duplicate caption.** The Fig. 21 caption repeats that of Fig. 20, whereas the text describes Fig. 21 as the surface-grid comparison (3, 6, 10 mm) along L1.
- **Spelling.** Text "Wolfstein [57]", reference list "Wolfshtein"; ref. [18] prints "Schtze"; ref. [25] pages "269289"; Fig. 14 caption "REF and RAF grids"; "et 70 for the vehicle" and "X500 et X1000" (§4.4, §3).
- **$C_{d1}$ of the vehicle runs.** §4.1.3 gives $C_{d1}=20$, §4.4 says 30 was "investigated" and "then advised for this case"; no vehicle result is labelled with the value used.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$, $y$, $z$ (Nomenclature) | $x$ streamwise, $z$ spanwise, $y$ vertical | **collision:** the source's $y$ is spanwise and $z$ vertical (wall-normal on roof and underbody); plane names (Y0, Z320, …) are kept as printed |
| $V_x$, $V_y$, $V_z$ | time-averaged velocity components | in the source's axes |
| $\Omega_x$ | streamwise mean vorticity | **collision:** not the rotation-rate tensor $\Omega_{ij}$ |
| $V_\infty$, $U_0$ | free-stream velocity | |
| $Re_L$ | $Re$ based on vehicle length $L_v$ | |
| $C_d$, $C_l$, $C_p$ | $C_D$, $C_L$, $C_p$ | "counts" = 0.001 in $C_D$ |
| $SC_d$ | cumulative drag along $X$ (page-local) | Fig. 13 |
| $C_{d1}$, $C_{d2}$ (printed "$Cd_1$") | DDES delay constants | **collision:** typographically close to the drag coefficient |
| $k$, $\varepsilon$, $\omega$, $\nu_t$ | $k$, $\varepsilon$, $\omega$, $\nu_t$ | agree |
| $\beta^*$, $F_1$, $F_2$, $C_\mu$ | $\beta^*$, $F_1$, $F_2$, $C_\mu$ | values and formulas not printed |
| $Y_k$ | destruction term of the $k$ equation (page-local) | Fluent notation |
| $l_{RANS}$, $l_{LES}$, $l_{DES}$, $l_{DDES}$ | DES length scales | Eqs. 7–11 |
| $C_{DES}=C_{DES1}F_1+C_{DES2}(1-F_1)$ | DES constant | 0.78, 0.61 |
| $\Delta_{max}=\max(\Delta_x,\Delta_y,\Delta_z)$ | DES grid scale | not the registry's filter width in general |
| $\delta$ | $\delta$ | boundary-layer thickness |
| $r=\Delta_{max}/\delta$, $f_d$, $r_d$ | grid-to-boundary-layer ratio; DDES delay function and its argument | $r_d$ formula not printed |
| $Re_y=\rho y\sqrt k/\mu$ | $R_y=d\sqrt k/\nu$ (wall-distance turbulent Reynolds number, registry §11, as on the [k-ε](/methods/k-epsilon-model.md) and [SST](/methods/k-omega-sst-model.md) pages) | **collision:** not the registry's $Re_y=Uy/\nu$ of explicit wall laws; switch value 200 |
| $\omega^+_{sub}$, $\omega^+_{log}$ (printed "$w^+$") | viscous-sublayer and log-layer $\omega$ in wall units | $C_{\omega2}$ not printed |
| $\Delta x^+=u_\tau\Delta x/\nu$ | $\Delta x^+$ | |
| $\tau$ (Eq. 5) | $\sigma_{ij}$ | viscous stress, not a turbulent stress |
| $\Phi$, $\Gamma_\Phi$, $S_\Phi$ | generic transported scalar, its diffusivity and source | finite-volume Eqs. 1–3 |
| $CFL=V_\infty\Delta t/\Delta x$ | CFL number | based on the free-stream velocity |
| $h_1$, $L_{ref}$ | first prism-layer height, reference tetrahedron edge | |
| $L_v$, $W_V$, $H_V$; $L_{AB}$, $W_{AB}$, $H_{AB}$ | vehicle and Ahmed-body dimensions | 4585, 1804, 1471 mm; 1044, 380, 288 mm |
| $I$ | $Tu$ | inlet intensity 0.5% |

# Reference list

57 printed references, numbered [1]–[57] in a numeric style and ordered
alphabetically except refs. [17] and [18], which are swapped. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Ref. [31] (Menter et al., GPU solver for external aerodynamics, SIMVEC
2022) is a different work from the Source `menter-2022` and is keyed `menter-2022-b`;
ref. [16] is the Source `goc-2021`. Ref. [30] (Menter & Egorov, SAS Part 1) is
printed truncated, with no venue, volume, pages or year; ref. [1] prints no
pages and ref. [9] no volume; refs. [14], [22], [31] and [36] print "et al.".
Ref. [11] is an internship report and ref. [49] an undated wind-tunnel web
page. No printed duplicates.

# Pages created or updated

Chunk 4 (2026-10-26), cited further in chunks 8, 12. This source is cited on:

- [Ahmed body](/benchmarks/ahmed-body.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Boundary-layer-conforming grids for wall-modelled LES](/methods/boundary-layer-conforming-grid.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
- [Scale-adaptive simulation](/methods/scale-adaptive-simulation.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [ANSYS Fluent](/software/ansys-fluent.md)
