---
type: Source
title: "Luckring & Rizzi (2024) — Prediction of concentrated vortex aerodynamics: Current CFD capability survey"
description: "Survey of CFD capability for separation-induced vortex flows on aircraft (delta and diamond wings, vortex breakdown, vortex generators, strakes, SACCON, F-16XL, X-31): RANS predicts steady sharp-edge vortices, while secondary separation, blunt-edge onset, breakdown and hysteresis are not anchored; adaptive meshing and hybrid RANS/LES are recommended."
resource: "doi:10.1016/j.paerosci.2024.100998"
source_kind: paper
authors: [Luckring J.M., Rizzi A.]
year: 2024
venue: "Prog. Aerosp. Sci. 147:100998"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Progress_in_Aerospace_Sciences_Luckring_Prediction_of_concentrated_vortex_aerodynamics_Current_CFD_c.pdf"
tags: [review, separated-flow, hybrid-rans-les, rans, mesh-adaptation]
timestamp: 2026-10-28T17:01:00Z
---

# Summary

Luckring & Rizzi (2024) survey how well CFD predicts *concentrated vortex
flows*: coherent vortices that separate from swept edges (delta-wing
leading edges, strakes, vortex generators, chines) and that aircraft use
for vortex lift or flow control. The survey rests on the authors'
experience and a database of "over 6000 articles spanning approximately 20
years". It reviews applications, the elemental physics (primary and
secondary separation, blunt-leading-edge onset with an incipient-separation
region and an inner vortex, interactions, breakdown, hysteresis), and a
hierarchy of formulations with one application each:
[DNS](/definitions/direct-numerical-simulation.md), wall-resolved
[LES](/definitions/large-eddy-simulation.md) (including the high-order
[implicit LES](/definitions/implicit-les.md) of FDL3DI), RANS and URANS
([Spalart–Allmaras](/methods/spalart-allmaras-model.md),
[$k$-$\varepsilon$](/methods/k-epsilon-model.md),
[$k$-$\omega$](/methods/k-omega-model.md), [SST](/methods/k-omega-sst-model.md),
[EARSM](/methods/explicit-algebraic-reynolds-stress-model.md) and
[Reynolds-stress models](/methods/reynolds-stress-model.md)),
[wall-modelled LES](/methods/wall-modelled-les.md),
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) with
[DES, DDES and IDDES](/methods/detached-eddy-simulation.md), and the
[lattice Boltzmann method](/methods/lattice-boltzmann-method.md). The
fundamental and configuration cases it surveys are gathered on
[delta-wing and concentrated vortex flows](/benchmarks/delta-wing-vortex-flow.md).

The findings: steady coherent vortices from sharp-edged slender wings are
predicted well, often by RANS. Secondary vortices, blunt-leading-edge
onset, vortex breakdown, hysteresis, and the persistence of
vortex-generator and strake vortices are not anchored against measurements.
Well-established codes and models disagree at high incidence (SACCON,
X-31; see [model-form uncertainty](/definitions/model-form-uncertainty.md)).
The authors argue that time-accurate [mesh adaptation](/methods/mesh-adaptation.md)
is effectively a requirement. They find that high-order wall-resolved LES
reproduces plausible physics only at low Reynolds number, and they collect
[grid-point estimates](/results/les-grid-point-requirements.md) for DNS and LES.
A cost argument closes the paper: an F-35-based estimate puts CFD at about
20 times the wind-tunnel cost, and supercomputer growth is now half the
Moore's-law rate. The authors recommend hybrid test and simulation
programmes, open military configurations, unit-problem experiments, GPU
solvers and a reassessment of turbulence models for vortical flows. The
evidence is entirely from the studies cited; the authors compute nothing
beyond cost estimates.

# Version read

Version of record (Elsevier, open access CC BY 4.0; received 21 March 2024,
accepted 24 March 2024, available online 6 July 2024), 58 pages, all read;
figures are reproduced from the cited studies and no values were read off
them. Page 1 matches the Crossref metadata; no identity problem.

# Key claims

1. Concentrated vortex flows are classified as *steady* (unsteadiness no greater than typical attached-flow turbulence) or *unsteady*, and by coherence as *coherent* (stable, steady elements), *semicoherent* (instability and unsteadiness inside an organized vortex) and *incoherent vorticity* (no organized vortex, e.g. a bluff-body wake) (§2.1). **Stated**
2. An *anchored* formulation is one "with some degree of pedigree (historical applications, calibration history, validation history) for a new prediction"; verification, validation, prediction and calibration follow the AIAA and ASME guides as summarized by Oberkampf and Roy (§2.1). **Stated**
3. Primary-vortex properties over sharp-edged slender delta wings depend on geometry, incidence and Mach number, "Reynolds number is less influential"; the core has an outer inviscid rotational region and an inner viscous subcore that shrinks with Reynolds number; in the Hall and Stewartson–Hall conical model the axial velocity approaches three times the free-stream value (§2.3.1.1, Fig. 21). **Stated**
4. For blunt leading edges, higher incidence and higher Mach number promote leading-edge vortex separation, and greater bluntness and higher Reynolds number delay it (§2.3.1.2, from Luckring, ref. [39]). **Stated**
5. Blunt-leading-edge separation adds an incipient separation region upstream of vortex separation and an inner vortex of the same rotation as the primary, explained by Hitzel et al. as the collision of the vortex-induced inboard reattached flow with the upstream outboard attached flow (§2.3.1.2, Figs. 25, 30, 60). **Stated**
6. On Poll's 56° swept wing a Reynolds-number increase from $1.4\times10^6$ to $2.7\times10^6$ replaced the full-span leading-edge vortex by attached flow with a short bubble near midspan; 1° more incidence produced part-span swirling flow (§2.3.1.2, Fig. 29). **Stated** (from ref. [44])
7. DNS grid points scale as $N_x N_y N_z\propto Re_L^{9/4}$, and resolution with time steps "approximately with the cube of Reynolds number" (§2.4.1, §2.4.1.1). **Stated**
8. The DNS of the NACA 4412 by Hosseini et al. ($M=0.04$, $Re_c=0.4\times10^6$, 5°) used about $3.2\times10^9$ grid points in Nek5000, about 35 million core-hours over about 6 months, about ten chord lengths of advection and tripping at 10% chord; the EDGE EARSM RANS mean velocity correlates with it (§2.4.1.1, Fig. 43). **Stated**
9. Following Ghosal, for low-order discretizations "the truncation error can be the same order as the subfilter scale contributions, unless the cell size is considerably smaller than filter width Δ" (§2.4.1.2). **Stated**
10. Larsson et al.'s estimate for LES of the NACA 0012 upper surface ($M=0.1$, 2.5°): inner layer ($y/\delta<0.2$) $1.6\times10^7$, $1.9\times10^9$, $2.0\times10^{11}$ points and outer layer $3.3\times10^7$, $7.2\times10^7$, $2.5\times10^8$ points at $Re_c=10^6$, $10^7$, $10^8$, with trailing-edge $Re_\tau$ of $10^3$, $10^4$, $7\times10^4$; inner-layer points rise about two orders of magnitude per decade, and at $Re_c=40\times10^6$ the LES needs about 33 billion points (§2.4.1.4, Table 1). **Stated**
11. For WMLES "no well-established guidelines have been developed for many modelling choices, in particular for necessary grid resolution, but also for grid-cell topology, numerical schemes, subgridscale modelling" (§2.4.1.4). **Stated**
12. Wall-stress WMLES resolves the energetic motions of the outer boundary layer and of detached shear layers, DES97 only the latter, so "WMLES has the potential to be significantly more accurate than hybrid RANS/LES in non-equilibrium flows", with "approximately 80% of the boundary layer" treated by LES (§2.4.1.5). **Stated**
13. The authors know of no application of WMLES to concentrated vortex flows, and the survey found none of GPU solvers (§2.4.1.4, §5.3.1). **Stated**
14. DES replaces the SA wall distance $d$ by $\min(d,C_{\mathrm{DES}}\Delta)$, with $\Delta$ "the diameter of the cell" (elsewhere the wall-parallel spacing) and "only one additional model constant ($C_{DES}=0.65$)" (§2.4.1.4). **Stated**
15. On the F-15E at 65° ($M=0.3$, $Re_c=13.6\times10^6$, Forsythe et al.) URANS showed no significant unsteadiness and virtually no vorticity over the wing, whereas hybrid RANS/LES resolved it: "The hybrid RANS/LES formulation appears to be necessary for simulating flows with significant unsteady separated flow" (§2.4.1.4, Fig. 51). **Stated**
16. Steady coherent vortices from sharp-edged slender wings have been simulated well since the mid-1980s (Thomas et al. 1987, laminar thin-layer) and by Schiavetta et al. on a 65° delta ($M=0.4$, $Re_{\mathrm{mac}}=6\times10^6$) with several $k$-$\omega$ RANS models, including the turbulent secondary vortex (§3.1.1.1, Fig. 54). **Stated**
17. "In the course of this review, little to no correlation between simulation and physical experiments was found for secondary vortex flow features" (§3.1.1.2). **Stated**
18. VFE-2 (65° delta) and AVT-183 (53° diamond wing) established the structure of blunt-leading-edge separation (incipient region, primary onset, inner corotating vortex); the flow is well predicted when the predicted onset matches the experiment, but predicting onset "is not well established", and hybrid RANS/LES "appear to have done better than RANS methods" (§3.1.1.2, §4.1.1). **Stated**
19. Frink et al.'s USM3D RANS showed that extrapolating the primary reattachment line and the minimum suction under the primary vortex meets the minimum leading-edge $C_p$ inside the incipient separation region, supporting Luckring's criterion that this minimum approximates the origin of blunt-edge vortex separation (§3.1.1.2, Fig. 62). **Stated**
20. With free transition (DLR TAU, SST-$\gamma$-$Re_\theta$) the blunt-edge structures shift upstream and a laminar separation bubble appears upstream of incipient separation, so tripping matters at subscale tunnel Reynolds numbers (§3.1.1.2, Figs. 63–64). **Stated** (from Buzica and Breitsamter)
21. High-order WRLES (AFRL FDL3DI) captures laminar separation bubbles and their bursting, transition, side-edge vortices and, on the NACA 0012 at $M=0.4$, $Re_c=10^6$, 13.1° ($267\times10^6$ nodes), a succession of shocks and expansions ending in shock-induced separation, physics "not modeled, or have not been reported" in RANS and hybrid RANS/LES; WRLES is "currently restricted to low Reynolds numbers (on the order of 10⁴)" (§3.1.1.2, §4.1.1). **Stated**
22. Scaling Garmann and Visbal's C-130 afterbody WRLES ($210\times10^6$ nodes at $Re_D=0.2\times10^6$) to full scale, $Re_D=7.4\times10^6$, gives about 143 billion nodes, using Larsson et al.'s Table 1 (§3.1.1.2). **Derived** (method not detailed)
23. "At the time of this review, there is no reliable prediction technique for vortex breakdown"; time-accurate adaptive refinement "appears to be a requirement"; the most promising AVT-080 (70° delta) breakdown predictions came from hybrid RANS/LES, e.g. Morton's DES-SA with adaptive refinement (§3.1.2.1, §4.1.2). **Stated**
24. The survey found no demonstrated capability to simulate vortex hysteresis under dynamic motion of slender or nonslender wings (§4.1.2). **Stated**
25. In Zastawny's vortex-generator study (DLR TAU, $M=0.85$, $Re_{\mathrm{mac}}=5.3\times10^6$) the resolved approaches show a concentrated vortex one VG height downstream where the modelled-VG approach has already dissipated it, and at five heights all have, considered numerically induced; there is "no evidence of an anchored simulation capability for concentrated vortex flows from vortex generators" (§3.2.1.2, Fig. 76). **Stated**
26. Nacelle-strake vortex simulations (LBM on the CRM-HL at 16°, RANS on the DLR F11 at 17.5°) report strake-on and strake-off effects only, with no correlation of strake-vortex strength, trajectory or persistence with experiment (§3.2.2.2, Figs. 78–80). **Stated**
27. For SACCON ($\Lambda=53^\circ$, $M=0.144$, $Re_{c,\mathrm{ref}}=1.6\times10^6$), RANS from "well-established codes using well-established turbulence models" gives significantly different vortex flows at the rapid pitch-stability changes; under forced oscillation neither SA nor SST correlates well, SA being closer (§3.2.3.2, Figs. 84–88). **Stated**
28. In CAWAPI the standard deviation among CFD solutions at high incidence was "three times that of the moderate-angle-of-attack case"; CAWAPI-2 improved the secondary vortex with $k$-$\varepsilon$ instead of SA plus grid refinement, SA "fails to predict secondary separation because it does not transport the right quantities"; CAWAPI-3 hybrid RANS/LES one-standard-deviation pressure bands bracket the flight data (§3.2.3.3, Figs. 90–91). **Stated**
29. On the X-31 ($M=0.18$, $Re_{c,\mathrm{ref}}=2.07\times10^6$, 16°) DLR TAU (about $50\times10^6$ cells, SA) and NLR ENSOLV (about $31\times10^6$ cells, TNT $k$-$\omega$) give significantly different wing vortex flows; modelling the leading-edge flap gaps improved the pitching-moment correlation (§3.2.3.4, Figs. 93–94). **Stated**
30. In AVT-316 adaptive refinement was needed to resolve interacting vortices; on the triple delta wing (ISIS-CFD, anisotropic Hessian adaptation) hybrid RANS/LES was more reliable than URANS (§3.2.3.5, Figs. 97–98). **Stated**
31. Smith and McWaters' F-35-based estimate: 526 thousand CFD solutions using 17.1 billion core-hours at about USD 596 million, against a wind-tunnel programme the authors estimate at USD 30 million; CFD "costs about 20 times more" (§5.1). **Stated** / **Derived** ($596/30\approx19.9$ *(compiler check, not in the sources)*)
32. Supercomputer speed growth is now about half the Moore's-law rate of 1975–2015; the 40-year speedup ratio is $2.25\times10^{-6}$ (Table 2), delaying Zflop/s from 2030 to 2046 and Yflop/s from 2041 to 2067, and a 10× numerics or hardware speedup gives 2039 and 2060 (Table 3) (§5.1). **Derived** (authors' projection)
33. FUN3D GPU assessments show "speedups from four to thirty times that of CPU processing", CODA "a factor of three or more" (§5.3.1, §5.3.2.1). **Stated**

# Printed slips

- Footnote 3: "See, Hirschel et al. [193], p136-139", while ref. [193] is "S. Görtz, Private Communication, 2023" and Hirschel et al. is ref. [147].
- §2.4.1.4: "Spalart [23] has given some guidelines for creating grids suitable for hybrid RANS/LES", while ref. [23] is Pearcey (1961) on shock-induced separation.
- §2.4.1.4: "isentropic cells represent a logical approach to resolving turbulent length scales", after a sentence on isotropic cells.
- §2.2.2.1: "the review by Lin [19], 2002" and then "In 2006 Lin [19] reviewed the μVG technology"; the list dates ref. [19] 2002.
- Caption of Fig. 53 "Morton [97], 2009", while ref. [97] is AIAA 2003-4217 and the text reads "Fig. 53 from Morton [96], originally published in 2003 [97]".
- Caption of Fig. 74 "Visbal and Gordnier [100], 2005" and §3.1.2.1 attributing the 50° sharp delta study to ref. [100], which is the 2003 paper on the 75° leading edge; the 2005 low-sweep study in the list is Gordnier and Visbal [134].
- Caption of Fig. 75 "Visbal [118], 1994", while ref. [118] is Garmann and Visbal (2019) and Visbal (1994) is ref. [138].
- §5: "the CFD Vision 2020 study by Slotnick et al., of 2014 [185]", while the title of ref. [185] is "CFD Vision 2030 Study".
- "In 2003, Forsythe et al. [92]" (§2.4.1.4), dated 2004 in the list and in the caption of Fig. 51; "Slotnik [154], 2021" (Fig. 81), dated 2019 in the list; "Taylor [179] 2024" (Figs. 95, 97) and "Hitzel [180], 2024" (Fig. 96), dated 2023 in the list.
- WRLES "currently restricted to low Reynolds numbers (on the order of 10⁴)" (§4.1.1), while the paper reports WRLES at $Re_c=0.2\times10^6$ and $10^6$ (§3.1.1.2).
- Name spellings: "Vissoneau" (ref. [183], text) and "Visonneau" (Fig. 98); "Xiaoa" and "Cinnellab" (ref. [73], text); "Brynes and Taylor [21]" for a single-author ref. [21]; "Lamat" (ref. [167]) and "Lamar" (text); "Garman" and "Visball" in the text; "Spalart-Almaras", "Spalart-Allmaris", "Lattice-Bolztmann"; the heading "3.1.1.2. Basic features are described in the following subsections." printed mid-sentence in §2.3.1.2.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u^*$ | $u_\tau$ | **collision:** $(\cdot)^*$ is semi-local scaling |
| $Re_\tau=u^*\delta/\nu$ | $Re_\tau$ | "Ret" in Table 1 |
| $h_{wm}$, $\tau_w$, $q_w$ | $h_{\mathrm{wm}}$, $\tau_w$, wall heat flux | wall-stress WMLES |
| $\nu_T$ | $\nu_t$ | RANS or SGS eddy viscosity |
| $d$, $d_1=\min(d,C_{DES}\Delta)$ | $d$, DES length | $C_{\mathrm{DES}}=0.65$; $\Delta$ "the diameter of the cell", a grid length |
| $S$ | $\lvert S\rvert$-type local strain rate (DES argument) | **collision:** also the entropy in the source |
| $Q=\tfrac12(\lVert\Omega\rVert-\lVert S\rVert)$ | $Q=\tfrac12(\Omega_{ij}\Omega_{ij}-S_{ij}S_{ij})$ | printed without squares on the norms |
| $\lambda_2$ | second eigenvalue of $\mathsf S^2+\mathsf\Omega^2$ | vortex criterion |
| $\lambda$ | taper ratio, roll angle, wavelength | **collision:** Taylor microscale |
| $k$ | wavenumber $2\pi/\lambda$ or turbulent kinetic energy | double use in the source |
| $u'$, $\bar U$ | $u'$, $\langle u\rangle$ | **collision:** the overbar is the LES filter |
| $\eta=2y/b$ | spanwise station | **collision:** Kolmogorov length; $y$ spanwise here |
| $\xi=(x-x_{le})/c$ | chordwise coordinate | **collision:** reference coordinate |
| $\gamma$ | intermittency | SST-$\gamma$-$Re_\theta$ only |
| $Re_c$, $Re_{cr}$, $Re_{cref}$, $Re_{mac}$, $Re_D$, $Re_L$ | $Re$ with the stated length | chord, root chord, reference chord, mean aerodynamic chord, diameter, apex distance; $Re_L$ also the integral-scale Reynolds number of the DNS scaling |
| $\Lambda$, $\alpha$, $\beta$, $\sigma$ | sweep, incidence, sideslip, total incidence | |
| $C_{p,le}$, $C_{fx}$ | leading-edge $C_p$, streamwise $C_f$ | |
| WRLES | wall-resolved LES | the paper equates plain LES with WRLES; FDL3DI is called WRLES in captions and ILES in the text |

# Reference list

201 printed references, numbered [1]–[201] (Elsevier), with titles. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Ref. [196] is the ingested
[duraisamy-2019](/sources/duraisamy-2019.md). Non-journal items: private
communications [13], [106], [193]; patents [27], [28]; web pages [191],
[201] ([201] without a year); ESDU [24] without a year. Seven special issues
are printed with the author "Numerous" ([103], [110], [159], [168], [169],
[170], [176]) and several items have corporate authors (AGARD, AIAA, ASME,
ESDU, RTO, STO). Ref. [73] prints "H. Xiaoa, P. Cinnellab" and ref. [183]
"M. Vissoneau"; their keys follow the resolver's spelling decision. No item
is unparseable; [158], [198] and [199] print no pages.

# Pages created or updated

Chunk 14 (2026-10-28). This source is cited on:

- [Delta-wing and concentrated vortex flows](/benchmarks/delta-wing-vortex-flow.md)
- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [NACA 4412 airfoil](/benchmarks/naca-4412-airfoil.md)
- [NASA CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Dynamic stall](/definitions/dynamic-stall.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [Wilcox k-ω model](/methods/k-omega-model.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Lattice Boltzmann methods for turbulent flow](/methods/lattice-boltzmann-method.md)
- [Local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [Nek5000 and NekRS](/software/nek5000.md)
