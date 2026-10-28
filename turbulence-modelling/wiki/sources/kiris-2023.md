---
type: Source
title: "Kiris et al. (2023) — HLPW-4: Wall-Modeled Large-Eddy Simulation and Lattice–Boltzmann Technology Focus Group Workshop Summary"
description: "Summary of the HLPW-4 wall-modelled LES and lattice-Boltzmann focus group: nine codes on the CRM-HL at Re_MAC 5.5×10^6, Mach 0.2, free air and in tunnel; over 250M degrees of freedom needed for high-angle pitching moment, two inboard-stall topologies, cost 5–10 times steady RANS."
resource: "doi:10.2514/1.C037193"
source_kind: paper
authors: [Kiris C.C., Ghate A.S., Browne O.M.F., Slotnick J., Larsson J.]
year: 2023
venue: "J. Aircraft 60:1118–1140"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Journal_of_Aircraft_Kiris_HLPW-4_Wall-Modeled_Large-Eddy_Simulation_and_LatticeBoltzma.pdf"
tags: [wmles, high-lift, wall-model, grid-requirements, lattice-boltzmann]
timestamp: 2026-10-28T01:51:00Z
---

# Summary

Kiris et al. (2023) summarize the Wall-Modeled LES and Lattice–Boltzmann
Technology Focus Group of the 4th AIAA High-Lift Prediction Workshop. Nine
participants (LAVA, [CharLES](/software/charles.md), Real Flight
Simulator, BCFD, PowerFLOW, Alya, [hpMusic](/software/hpmusic.md),
FFVHC-ACE, FUN3D) simulated the
[NASA CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md) at
$Re_{\mathrm{MAC}}=5.5\times10^6$, $M=0.2$, in free air (case 2a) and, for
three teams, inside the QinetiQ 5 m tunnel (case 2b), all on $y^+\gg1$
grids. Seven used an adiabatic [equilibrium wall model](/methods/equilibrium-wall-model.md)
in the stress-based [wall-modelled LES](/methods/wall-modelled-les.md)
algorithm, PowerFLOW a proprietary pressure-aware
[non-equilibrium model](/methods/nonequilibrium-wall-model.md) with a
$k$-$\varepsilon$ very-large-eddy closure in a
[lattice Boltzmann](/methods/lattice-boltzmann-method.md) solver on a
Cartesian [immersed-boundary](/methods/immersed-boundary-method.md) grid
(a [hybrid RANS/LES](/definitions/hybrid-rans-les.md) philosophy), and one
team inviscid [implicit LES](/definitions/implicit-les.md) with zero-shear
[slip walls](/methods/slip-wall-model.md), which the authors reject. Most
used the constant-coefficient [Vreman model](/methods/vreman-model.md);
one the dynamic [Smagorinsky model](/methods/smagorinsky-model.md); the
[flux-reconstruction](/methods/flux-reconstruction.md) code ran implicit
LES; the discretizations minimized
[numerical dissipation](/properties/numerical-dissipation.md) through
blended upwinding or [kinetic-energy- and entropy-consistent](/properties/kinetic-energy-preservation.md)
fluxes.

Most participants predict $C_{L,\max}$ between 2.48 and 2.57; the
pitching-moment scatter is small at $C_{L,\max}$ and large at 7° and
21.47°. Accurate outboard slat and main-element suction peaks, hence the
high-angle pitching moment, required more than 250M degrees of freedom
([grid requirements](/results/les-grid-point-requirements.md)), attributed
to inviscid curvature-induced acceleration, a requirement the authors call
"somewhat contradictory" to the coarse WMLES success on the
[JAXA Standard Model](/benchmarks/jaxa-standard-model.md). The remaining
scatter comes from the predicted onset of inboard stall, in two surface
topologies (wing–body corner flow; wing–pylon juncture). WMLES avoids the
excess outboard separation of steady RANS and costs about 5–10 times a
representative steady RANS. The
[NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md),
[wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md) and
[shock/boundary-layer interactions](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
are cited as academic nonequilibrium WMLES cases; the isotropic against
anisotropic grid question ([boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md))
is left open. RANS comparisons ([Spalart–Allmaras](/methods/spalart-allmaras-model.md)
with QCR among them) come from the companion workshop papers.

# Version read

Version of record (J. Aircraft 60(4):1118–1140, AIAA, open access, U.S.
Government work; received 2 Sep 2022, published online 17 Mar 2023), 23
pages, all read; pages with missing glyphs (pp. 1–6, 12) were checked
visually. Page-1 title, five authors and DOI match the metadata. The
footnote states it was "Presented as Paper 2022-3294 at the AIAA Aviation
2022 Forum": that conference paper is a distinct bibliography entry
(`kiris-2022-b`). The bibliography entry `kiris-2023` already cited by
[volpiani-2024](/sources/volpiani-2024.md) is this work. Numbering on this
page is that of this version.

# Key claims

Grid spacing is written $h$ (the source's $\Delta$), the boundary-layer
thickness $\delta$ (the source's $\delta_{BL}$); participant identifiers
W-0xx are the workshop's. No model equation or constant is printed in the
paper.

1. More than 250M spatial degrees of freedom are needed to predict pitching moments accurately at high angles of attack, because of large pressure gradients on the outboard slat and main element for $\alpha>17^\circ$ (abstract; §IV; §VI 1a, "at least 250M grid cells"). **Shown**
2. Except W-030 and W-031, the participants obtain $C_{L,\max}$ "with values between 2.48 and 2.57" (§III, Fig. 4). **Shown**
3. At $C_{L,\max}$ the pitching-moment scatter is small, "suggesting that the agreement in $C_{L,\max}$ is likely due to the correct prediction of the flow-topology"; the scatter is larger at 21.4° and 7° (§III). **Shown**
4. RANS submissions that obtain $C_{L,\max}$ "invariably predict far-too-high nose-up pitching moments", i.e. $C_{L,\max}$ through cancellation of inboard excess lift and outboard loss of lift; most WMLES do not show this (§III). **Stated** (RANS data from the companion papers)
5. WMLES lacks the excess outboard separation of RANS; most WMLES and LB submissions predict wedge-shaped separation consistent with oil flow (abstract; §IV; Fig. 33). **Shown**
6. Full-airframe WMLES with fewer than $10^9$ degrees of freedom are "coarse-grid simulations", with $h/L_{\mathrm{span}}$ substantially coarser than academic WMLES of nonequilibrium boundary layers (hump, Gaussian bump, shock interaction, buffet) (§I). **Stated**
7. Grid convergence of wall-bounded LES is likely non-monotonic in mean velocity profiles, and numerically induced transition shifts virtual origins with the grid, so grid convergence is assessed only on the time-averaged static pressure (§I.1a). **Stated**
8. Qualitatively accurate near-surface topology appears sufficient to predict total loads within community accuracy; the precedent is corner-flow RANS (QCR) with $\mathcal O(1)$ errors in the mean velocity within the juncture separation but accurate $C_p$ (§I). **Stated**
9. Explicit time stepping suits near-unity-aspect-ratio grids for compressible solvers at $M\ge0.2$: the decorrelation time of inertial-range eddies scales as $k^{-2/3}$ in the grid Nyquist wavenumber $k$, the acoustic CFL limit as $k^{-1}$ (§II.3). **Derived** (scaling argument)
10. The implicit codes used time steps "only about 10× larger", consistent with the incompressible-against-acoustic CFL difference at $M=0.2$; implicit stepping was chosen for grid-quality reasons (§VI 1c; §II.3). **Stated**
11. A hybrid RANS/LES time-step study suggests large inaccuracies in wing-root separation at 21.47° from the dissipative large time steps that A-stable BDF2 allows (§VI 1c). **Stated** (cited)
12. W-021 "reported little sensitivity" between dynamic Smagorinsky and Vreman on intermediate grids (§II.4). **Stated** (participant report)
13. ODE and algebraic equilibrium wall-model variants "are of no consequence for the present flow"; applying the wall stress at nodes (W-020, W-034, W-050) or at cell centres (W-021, W-031, W-047) may be a larger source of discrepancy (§II.5). **Stated**
14. W-030 (inviscid implicit LES, slip walls, $Re\to\infty$) cannot predict loads within the desired accuracy: the experiments show more than 5% lift sensitivity between the lowest and the highest two Reynolds numbers, skin-friction drag is about 10% of the total at 7.05°, and corner-flow separation is a viscous effect (§II). **Shown** and **Stated**
15. W-021's refinement from 12M to 362M Voronoi degrees of freedom converged largely monotonically, the leading-order effect being kinematic (inviscid curvature-induced acceleration on the outboard wing and slats) (§III, Fig. 6). **Shown**
16. W-020's off-wall refinement (275M to 360M) improved the chine-vortex resolution and delayed the onset of corner-flow separation by over 1.5° (§III, Fig. 7). **Shown**
17. W-034: anisotropic grids with finer near-wall spacing give more accurate outboard $C_p$ on coarser grids than unity-aspect-ratio Voronoi grids with larger wall-normal spacing (§III; Figs. 8, 16, 21). **Shown**
18. All submissions meeting the outboard suction-peak criterion (peaks at 19.57° higher than the experiment at 17.05°) used more than 250M degrees of freedom (§IV, Fig. 12). **Shown**
19. W-020 (over 300M) shows little $C_p$ sensitivity under refinement and W-021 (under 300M) a large one; the boundary layers differ but the pressure field is insensitive, giving reasonable loads on coarse grids (§IV.2, Figs. 14–17). **Shown**
20. Among the submissions above 250M, most pitching-moment scatter at 21.47° stems from the predicted onset of inboard stall, in topology A (corner flow at the side of body; pitch break between 20.5° and 21.47°$+\varepsilon$, $\varepsilon<0.3^\circ$) or topology B (inboard wing–pylon juncture; pitch break unlikely near 21.47°) (§IV.3, Figs. 23–25). **Shown**
21. The two free-air topologies resemble the two stall mechanisms Evans et al. observed in the QinetiQ 5 m and Langley 14×22 tunnels; since both occur in free-air WMLES, the tunnel floor boundary layer may not explain them, and nacelle-lip separation is proposed instead (§IV). **Stated** (hypothesis)
22. All WMLES submissions predicted nacelle-lip separation for $\alpha>17.05^\circ$ around $C_{L,\max}$, absent in the experiment; trip dots twice as large (W-020) did not remove it; under-resolution plus a non-optimal cowl design are blamed (§IV; §VI 1d). **Shown**
23. In the tunnel, no team reproduced the thick floor boundary layer measured by the rake; W-021 predicts the pitch break between 18.9° and 19.9° "in perfect agreement with the experiment"; all three show wedge-shaped outboard separation and massive wing-root separation at 19.9°, which RANS does not capture (§V, Figs. 27–33). **Shown**
24. With W-020's slip-wall tunnel variant, the onset of the pitch break is sensitive to the floor boundary layer but the stalled state at 19.9° is largely invariant to it (§V.4, Figs. 35–36). **Shown**
25. Proposed causes of the free-air against in-tunnel discrepancy: inadequate blockage corrections, the induced-drag change from the stand-off, and the floor boundary layer altering the fuselage roll-off vortex (§V). **Stated**
26. W-047 (high-order flux reconstruction, $N=2$, 13M degrees of freedom) obtained reasonably accurate integrated loads at $C_{L,\max}$ but no outboard slat-bracket-wake separation (§VI 1a). **Shown**
27. WMLES and hybrid RANS/LES under-predict the outboard flap suction peak (stations E, F) relative to steady RANS at 21.47°, which explains the excessive nose-up pitching moment of all WMLES for $\alpha>17^\circ$; the cause is unclear (§VI 1e, Fig. 37). **Shown**
28. No participant had the resolution for smooth-body separation on the flaps by the Gaussian-bump best practices; the results show a non-monotonic trend at low $\alpha$ (§VI 1f). **Stated**
29. Best-practice WMLES cost about 5–10 times a representative steady RANS at $Re_{\mathrm{MAC}}=5.5\times10^6$; W-021 and W-047 reduced wall-clock time substantially on GPUs; a WMLES cost scaling with Reynolds number for such a configuration does not exist (§VI 4). **Stated**
30. No clear answer on isotropic against anisotropic grids: W-034 favours anisotropic near-wall refinement, W-020 shows the need to resolve off-body vorticity for $\alpha>19^\circ$, for which isotropic grids suit (§VI 2). **Shown**

# Printed slips

- **§IV, topologies:** topology A lists "Submissions W-020, W-021, W-032, W-047, and W-050", topology B "Submissions W-031, W-032, and W-049", and the text later says "Submission W-032 (which falls under topology B)".
- **§II.3, explicit and implicit counts:** "Six out of the nine participants used explicit time-stepping schemes, while the remaining three used implicit". *(compiler check, not in the sources)* Table 1 lists RK3 or explicit LBM for W-020, W-021, W-032, W-049, RK3 convective with implicit Crank–Nicolson viscous terms for W-034, "Imp." for W-030 and "Imp. BDF2" for W-031, W-047, W-050: five explicit and four implicit. §VI 1c names five explicit and three implicit, omitting W-030; §II.3 names "W-047 and W-050" as "the majority of the participants utilizing implicit time-stepping schemes".
- **§VI 1c, time-step ratio:** implicit codes "used time-step sized only about 10× larger". *(compiler check, not in the sources)* From Table 2 (explicit $2.9\times10^{-5}$–$5.7\times10^{-5}$; implicit W-031 $5.8\times10^{-4}$, W-050 $5\times10^{-4}$, W-047 $9.7\times10^{-5}$) the ratios are about 9–20 for W-031 and W-050 and 1.7–3.3 for W-047.
- **W-020 finest grid:** "the 1.2B grid" (§III, §VI 1a) against "W-020.5 (1100M)" in the Fig. 3 legend; the legend also lists W-020.1 (300M), absent from the text's 275M, 360M, 650M, 1.2B sequence.
- **Angles:** the free-air high angle is printed 21.4° (§III) and 21.47° (Fig. 5 caption, §IV); in-tunnel angles 17.9°, 18.9°, 19.9° (§V) and 17.98°, 19.98°, 19.99° (§VI 3, Figs. 33, 34); the abstract places the low-angle scatter at "α < 11°", §III at 7°.
- **Resolution units:** ">250 M spatial degrees of freedom" (abstract), "at least 250M grid cells" (§VI 1a), "grids with >250 M points" (§IV).
- **References:** [18] "AIAA SciTech 2021 Forum, AIAA Paper 2020-1438, 2021" with DOI 10.2514/6.2021-1438; [36] "AIAA SciTech 2022 Forum, AIAA Paper 2020-1556, 2022" with DOI 10.2514/6.2022-1556; [16] "Prediciton"; [37] "NASAVision".
- **Typos:** "spacial" (Table 1 caption), "angels of attack" (§III), "time-step sized" (§VI 1c).

# Notation map

| Kiris et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta$ | $h$ | grid spacing, also wall-normal spacing; exchange locations in multiples of it; $\Delta$ stays the filter width |
| $\Delta/L_{\rm span}$, $\Delta_{\rm span}$ | $h/L_{\mathrm{span}}$, $h_z$ | spacing per unit span; spanwise spacing (page-local) |
| $\delta_{BL}$ | $\delta$ | boundary-layer thickness |
| $k$ (§II.3) | $k$ | grid Nyquist wavenumber, spectral meaning (clash list); not the turbulent kinetic energy |
| $\varepsilon$ (§IV) | $\varepsilon$ | **collision:** a small angle ($<0.3^\circ$), not the dissipation rate |
| $\eta$ | $\eta_{\mathrm s}$ | spanwise station coordinate, page-local; **collision** with the Kolmogorov length $\eta$ |
| $\alpha$ | $\alpha$ | angle of attack; **collision** with the DG/FV blending factor |
| $C_L$, $C_D$, $C_{My}$, $C_{L,\max}$, $C_p$, $C_f$ | same | $c_L$, $c_D$, $c_{MY}$, $c_P$ in figures |
| $Re$ | $Re_{\mathrm{MAC}}$ | based on the mean aerodynamic chord |
| $\tau_w$, $q_w$ | $\tau_w$, (wall heat flux) | agree |
| $y^+$ | $y^+$ | agree |
| CTU | $tU_{\mathrm{ref}}/L_{\mathrm{ref}}$ | convective time unit on the MAC |
| p2 | $N=2$ | polynomial degree of the FR code |
| DoF | (spatial degrees of freedom) | used interchangeably with cells and points |

# Reference list

58 printed references, numbered [1]–[58] (AIAA style, DOIs printed for
most), all parseable; [16], [23], [50] and [56] are web items. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. Refs. [13] and [46] are the ingested
[goc-2021](/sources/goc-2021.md) and [bose-2018](/sources/bose-2018.md).
Many printed keys name works other than the master entries of the same key
and are re-keyed (`park-2017-b`, `park-2016-b`, `wang-2022-c`, `tamaki-2022-c`, `rumsey-2022-d`, `rumsey-2022-e`, `rumsey-2020-b`, `rumsey-2018-b`, `ghate-2020-c`, and `kiris-2022-c` for
kiris-2022-b, whose printed reference is the focus group's 2022 briefing
slides, not the AIAA 2022-3294 conference paper held under the master key `kiris-2022-b`); ref. [25] is the master
`meyers-2007-b` and ref. [10] the master `lozanoduran-2020-c`. No printed
duplicates.

# Pages created or updated

Chunk 12 (2026-10-28). This source is cited on:

- [JAXA Standard Model high-lift configuration](/benchmarks/jaxa-standard-model.md)
- [NASA CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md)
- [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md)
- [NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md)
- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Boundary-layer-conforming grids for wall-modelled LES](/methods/boundary-layer-conforming-grid.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Flux reconstruction](/methods/flux-reconstruction.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Lattice Boltzmann methods for turbulent flow](/methods/lattice-boltzmann-method.md)
- [Non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)
- [Slip-wall models](/methods/slip-wall-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Vreman model](/methods/vreman-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [CharLES](/software/charles.md)
- [hpMusic](/software/hpmusic.md)
