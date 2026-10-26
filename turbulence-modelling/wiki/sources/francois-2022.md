---
type: Source
title: "François et al. (2022) — Zonal Detached Eddy Simulation of the Fan-Outlet Guide Vanes Stage of a Turbofan Engine: Part I—Methodology, Numerical Setup, and Aerodynamic Analysis"
description: "Applies ZDES mode 2 with the Spalart–Allmaras model in elsA to the ACAT1 fan–outlet-guide-vane stage at approach (380 million cells), and validates global performance, mean and RMS wake profiles against hot-wire data and RANS."
resource: "doi:10.1115/1.4054528"
source_kind: paper
authors: [François B., Polacsek C., Barrier R.]
year: 2022
venue: "J. Turbomach. 144:111004"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Turbomachinery_François_Zonal_Detached_Eddy_Simulation_of_the_Fan-Outlet_Guide_Vanes.pdf"
tags: [hybrid-rans-les, des, turbomachinery, rans, aeroacoustics]
timestamp: 2026-10-25T19:45:00Z
---

# Summary

François et al. (2022) run a zonal
[detached-eddy simulation](/methods/detached-eddy-simulation.md) (ZDES, mode
2 of Deck 2012) of the ACAT1 fan–outlet-guide-vane (OGV) stage of a modern
turbofan. The rig is the AneCom UFFA rig of the EU TurboNoiseBB project,
run at approach conditions. The aim is to supply the turbulent fan wakes
that drive rotor–stator-interaction broadband noise. Part I covers the
aerodynamics, and the acoustics are left to a companion Part II. The solver
is ONERA's [elsA](/software/elsa.md), and the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md) is the RANS
closure of this [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
approach. The core flow and the inflow region upstream of the fan run in
URANS, and the bypass flow runs in ZDES mode 2. In mode 2 the boundary
layers are shielded in RANS by the delayed-DES function $f_d$, computed from
the SA variable $\tilde\nu$. The subgrid length scale switches from the
largest cell dimension to the cube root of the cell volume at $f_d=0.8$.

The OGV count is reduced from 44 to 40 at constant solidity, so that one fan
channel and two OGV channels with periodic boundaries form the domain. The
structured grid has 380 million cells, with 0.5 mm cells in the free-shear
regions, sized from an acoustic gust-wavelength criterion. The authors state
that the same free-shear density would need more cells with
[wall-modelled LES](/methods/wall-modelled-les.md) than with RANS-treated
boundary layers. Statistics are taken with a cyclostationary (phase-averaged
plus stochastic) decomposition.

Against hot-wire data between fan and OGV, global performance agrees within
0.4%. Mean axial and tangential velocities agree within 3%, and the RMS
profiles lie inside the measurement band, also in the tip-gap region. RANS
with the [$k$-$\omega$ SST](/methods/k-omega-sst-model.md) and Smith $k$-$l$
models fails there: its RMS values are reconstructed through the
[Boussinesq relation](/definitions/boussinesq-hypothesis.md) and have the
wrong shape in the tip gap. ZDES over-predicts the wake velocity deficit by
10–15% and the RMS peak by 15% on average. It predicts no background
turbulence outside the wakes, although the measurements show some. The
paper is an application and validation of an existing
[LES](/definitions/large-eddy-simulation.md)-type hybrid method, not a new
model.

# Version read

ASME accepted manuscript ("Accepted Manuscript Not Copyedited", manuscript
TURBO-21-1140; received 6 July 2021, posted 4 May 2022), not the typeset
version of record. It has 34 pages: text pp. 1–27, references pp. 28–31,
and lists of figures and tables pp. 32–34. The page-1 title abbreviates the
Crossref title ("Fan-OGV Stage", "Part I - Methodology, Numerical Setup and
Aerodynamic Analysis"). It is the same work, and the authors appear in the
same order. The DOI is printed on every page. The companion Part II
(Polacsek et al., ref. [2], "Submitted to Journal of Turbomachinery") is a
different work. Section, figure, table and reference numbers on this page
are those of the accepted manuscript.

# Key claims

1. A ZDES (mode 2) of the ACAT1 fan–OGV stage, with URANS in the core flow and upstream and ZDES mode 2 in the bypass flow, was run for nearly four revolutions and reached statistical convergence (Abstract; §3.5; §3.6). **Shown**
2. In ZDES mode 2 the boundary layer is shielded in URANS by the DDES function $f_d=1-\tanh(8r_d)^3$ (cube placement as printed, see Printed slips) with $r_d=(\nu+\tilde\nu)/(\sqrt{\partial_ju_i\,\partial_iu_j}\,\kappa^2d^2)$. It is computed from the Spalart–Allmaras variable $\tilde\nu$ rather than from $\nu_t$ as in classic DDES (§3.1, equation on p. 5, footnote 2). **Stated**
3. ZDES mode 2 differs from DDES mainly in the length scale: $\Delta=\Delta_{\max}=\max(\Delta x,\Delta y,\Delta z)$ if $f_d<f_{d0}$ and $\Delta=\Delta_{\mathrm{vol}}=(\Delta x\Delta y\Delta z)^{1/3}$ if $f_d>f_{d0}$, with $f_{d0}=0.8$, while DDES uses the maximum everywhere (§3.1, p. 6). **Stated** (from Deck [4]). The DES modification of the SA destruction term itself is not printed.
4. Citing Deck et al. [4], ZDES keeps the attached-boundary-layer treatment of DDES and reduces the delay in the formation of instabilities (mixing-layer, backward-facing-step and airfoil comparisons) (§3.1). **Stated**
5. The measured inflow turbulence is about 0.3% [15]. Noise from inflow turbulence hitting the fan is therefore negligible next to rotor–stator-interaction noise, so URANS suffices upstream of the fan (§3.2.1). **Stated**
6. The URANS/ZDES border near the core/bypass splitter must be placed so that all streamlines passing near the fan blade and entering the bypass are in ZDES mode 2. Otherwise part of the wakes reaching the OGV stays "RANS-like" (§3.2.1, Fig. 2). **Stated**
7. Phase-lag boundary conditions based on Fourier decomposition do not suit the convection of broadband structures. The OGV count is therefore reduced from 44 to 40 at constant solidity (chord +10%; leading-edge position, sweep, lean, thickness-to-chord ratio and angle laws unchanged), giving 1 fan + 2 OGV channels with periodic boundary conditions (§3.2.2). **Stated**. Earlier RANS at equal mass flow [6] gave identical radial evolutions of absolute flow angle and Mach number upstream and downstream of the OGV. **Stated** (from [6])
8. Interpolation errors at the rotor–stator sliding interface, which produced spurious noise sources in [7], were corrected in elsA and "have now fully disappeared" (§3.3). **Stated**
9. Mesh criteria: free-shear cells with $\Delta x^+,\Delta y^+,\Delta z^+<200$ (below 0.6 mm here) and first wall cell $\Delta y^+\le1$ (ONERA internal ZDES mode 2 best practice). An acoustic gust criterion $\lambda_h=U_c/f$ with 20 points per wavelength at $U_c=100$ m/s gives 0.25 mm at 20 kHz, which would mean 3 billion cells. The compromise is 0.5 mm, i.e. 20 points at 10 kHz and about 400 million cells (§3.4.1). **Derived**
10. The grid is structured multi-block with 380 million cells: a first cell of 3 µm ($y^+=1$ at the cell centre), 180 million cells per fan channel and 100 million per OGV channel (Fig. 4). Inlet and outlet buffer zones have an axial stretching ratio below 1.2 and largest cells of 3 cm upstream and 2 cm downstream (§3.4.2). **Stated**
11. Numerics: elsA cell-centred finite volume; implicit second-order time scheme with Newton sub-iterations (5 sub-iterations, residuals down by one order); $\Delta t=3.2\times10^{-7}$ s (2400 steps per fan blade passage, 48000 per revolution); convective CFL about 36 in the smallest boundary-layer cells and 0.35 in the 0.5 mm cells; AUSM convective flux with a third-order limiter; Spalart–Allmaras model (§3.5). **Stated**
12. Cost: 28 nodes, 672 cores on CINES machines, 2 million CPU hours in total for nearly four revolutions (§3.5). **Stated**
13. The numerical transient lasts two revolutions (40 fan blade passages, FBP). Over ten-FBP windows the time-averaged bypass mass flow then varies by less than 0.2%, and statistics use $t=40$ to $76$ FBP (§3.6.1, Fig. 6). **Shown**
14. A cyclostationary decomposition $u=u_{\mathrm{cyclo}}+u_{\mathrm{stoc}}$ (after Hussain & Reynolds [27]) gives converged phase averages over the 36 FBP of statistics. The RMS of the stochastic part converges within 5% at a tip-gap probe (90% height, near the OGV leading edge) and within 2% at mid-height probes (§3.6.2, Fig. 7). **Shown**
15. The shielding function ($f_d=0.95$ contour) covers the whole boundary layer on both fan and OGV blades and switches rapidly from RANS to LES at the trailing edge. Wake turbulence impinging on the OGV does not (qualitatively) degrade the OGV boundary-layer shielding (§4.2, Fig. 9). **Shown** (qualitative)
16. Fan-wake vorticity crosses the sliding interface and the periodic boundaries "without noticeable attenuation or numerical artefact" (§4.2, Figs. 8b, 9). **Shown** (qualitative)
17. Relying on RANS in the boundary layer allows 0.5 mm cells in the free-shear regions. The authors state that such a density "would require a larger number of cells in the whole mesh with a WMLES approach" (§4.1). **Stated** (no cost comparison shown)
18. Global performance against measurement (Table 1): core mass flow 6.43 kg/s (measured 6.41), bypass mass flow 48.60 kg/s (measured 48.76), bypass pressure ratio 1.105 (measured 1.108), maximum discrepancy below 0.4%. The previous ZDES [6] gave 6.44, 49.26 and 1.106, a 1% mass-flow error (§5.1). **Shown**
19. Hot-wire RMS data were corrected by a factor of 1.5 because the probes cut off at about 8.5 kHz. The factor is estimated from the Parseval identity and the integration of the velocity PSD up to 8.5 kHz (§5.2, footnote 7). **Stated**
20. Cyclostationary 2D maps at the hot-wire plane HW1 match the measured wakes and tip-gap flow. The velocity-deficit depth is slightly over-estimated, and the tip vortex is a bit larger in the experiment. Measurements show a background turbulence outside the wakes that no simulation in the EU project reproduces (§5.2, Figs. 10–11). **Shown**
21. Radial profiles at HW1: ZDES over-predicts the mean axial and tangential velocities by less than 3%. The casing boundary layer is still not correct, but improves on [6], where it was too thin. The radial velocity is over-predicted by 5–10 m/s and agrees better with long-gap measurements; the authors leave this short-gap/long-gap difference "unexplained yet" (§5.3, Fig. 12). **Shown**
22. RANS ($k$-$\omega$ SST [30] and Smith $k$-$l$ [31], 5-million-cell mesh, 1 rotor + 1 stator channel) is close to ZDES for the tangential and radial mean velocities. It is off by +6–7% on the axial velocity, which the authors attribute to an over-estimated tip-gap flow area (§5.3). **Shown**
23. The ZDES RMS radial profiles of the three velocity components and of $k$ lie within the measurement uncertainty band, particularly in the tip-gap flow. RANS RMS values, reconstructed through the Boussinesq relation, show larger discrepancies and the wrong profile shape in the tip gap (§5.3, Fig. 13). **Shown**
24. Azimuthal cyclostationary profiles at 50% and 75% height: ZDES reproduces the wake thickness but over-estimates the deficit depth by 10–15%. RANS gives the same deficit with a narrower wake. At 97% height (tip gap), RANS over-estimates the main dip and peak by a factor of two (§5.4, Fig. 14). **Shown**
25. Azimuthal RMS profiles: the ZDES wake width is "very consistent" with measurement, and the RMS peak height is over-estimated by 15% on average (3% to 25% depending on the plot). RANS wakes are always narrower, and in the tip gap RANS predicts only one peak with over-estimated levels (§5.4, Fig. 15). **Shown**
26. The measured channel-to-channel heterogeneity is the only uncertainty contribution in the grey bands. The authors attribute it to small fan-blade geometry or stagger differences, amplified by leading-edge separation near surge. The bands are the min/max over 20 sub-zones, one per fan channel (Appendix). **Stated**

# Printed slips

- **Fig. 14 caption** (p. 22 and list of figures p. 33): "50% (a-b-c), 75% (g-h-i) and 97% (g-h-i)". The analogous Fig. 15 caption prints "75% (d-e-f)".
- **Fig. 11 caption:** "Maps of axial velocity flow fields … axial velocity (a-b) - tangential velocity (c-d)". The lead phrase says "axial" for a figure that shows both components; Fig. 10's caption reads "Maps of velocity flow fields".
- **Appendix figure references (p. 27):** the averaged RMS maps are referred to as "(see Fig. 15-b and 15-d)", but they are Fig. 11 (b, d); Fig. 15 holds azimuthal RMS profiles with panels a–i. "The cyclostationnary flow velocity field … at the HW1 measurement plane (Fig. 13)" points to a figure of RMS radial profiles; the cyclostationary fields are in Figs. 10 and 12.
- **Mass-flow discrepancy (§3.3):** "from +1% to −0.25%", stated for the bypass back-pressure adjustment. *(Compiler check, not in the sources)*: from Table 1 the bypass mass flow differs by $(48.60-48.76)/48.76=-0.33\%$, and the total mass flow ($55.03$ against $55.17$ kg/s) by $-0.25\%$. The printed figure therefore matches the total, not the bypass flow.
- **Shielding function:** printed "$f_d=1-tanh\left(8r_d\right)^3$", with the cube outside the parenthesis of $8r_d$. Recorded as printed; the paper's own statement ($f_d=0$ in the boundary layer, where $r_d\approx1$) holds for either reading, since $\tanh8\approx1$ *(compiler check, not in the sources)*.
- **Typography:** an unmatched parenthesis in the Abstract ("(The wake shape, a key feature in the mechanism of generation of rotor-stator interaction noise), is …"); "gemeotry" (§5.3); "Turbululence" (acknowledgements); "questionnable", "cyclostationnary".

# Notation map

| François et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tilde\nu$ | $\tilde\nu$ | SA working variable, called "the eddy viscosity solved in the equation of the Spalart-Allmaras turbulence model"; agrees |
| $\nu$, $\nu_t$ | $\nu$, $\nu_t$ | agree; $\nu_t$ enters $r_d$ in classic DDES (footnote 2) |
| $U_{i,j}$ | $\partial_ju_i$ | comma derivative; $r_d$ prints $\sqrt{U_{i,j}U_{j,i}}$ |
| $d_w$ | $d$ | wall distance |
| $\kappa$ | $\kappa$ | value not printed |
| $r_d$, $f_d$, $f_{d0}$ | $r_d$, $f_d$, $f_{d0}$ (page-local) | DDES shielding parameter and function, switch threshold 0.8 |
| $\Delta$, $\Delta_{max}$, $\Delta_{vol}$ | $\Delta$, $\Delta_{\max}$, $\Delta_{\mathrm{vol}}$ (grid lengths of the [DES page](/methods/detached-eddy-simulation.md)) | **collision:** the source's $\Delta$ is the DES grid length that caps the RANS length, not an LES filter width |
| $\Delta x^+$, $\Delta y^+$, $\Delta z^+$, $y^+$ | $\Delta x^+$, $\Delta y^+$, $\Delta z^+$, $y^+$ | agree; also applied to free-shear cells (< 200) |
| $\lambda_h=U_cf^{-1}$ | (hydrodynamic gust wavelength) | **collision:** not the Taylor microscale |
| $u_{cyclo}$, $u_{stoc}$ | $u_{\mathrm{cyclo}}$, $u_{\mathrm{stoc}}$ (page-local) | phase-averaged part (contains the time mean) and stochastic part; not a Reynolds decomposition |
| $N(t)$, $E$, $T_{BP}$, $t_0$ | (blade-passage count, floor function, blade-passage period, transient duration) | **collision:** $N$ is not a polynomial degree; $E$ is not an energy |
| $\Omega$ | $\Omega_{\mathrm{rot}}$ | rotation speed, 3828.4 rpm |
| $M_{tip}$ | $M_{\mathrm{tip}}$ | tip Mach number 0.57; not defined further |
| TKE | $k$ | |
| $Q$ | $Q$ | Q-criterion, non-dimensionalized by $t_{adim}^2$, $t_{adim}=2.915$ ms |

The paper prints no Reynolds-stress or subgrid-stress formula and no
explicit SGS model: in the LES regions the SA model acts as the subgrid
model through the grid length $\Delta$. The Reynolds number is given only as
"around one million", without a definition.

# Reference list

31 printed references, numbered in citation order, ASME style with titles.
The list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Part II (ref. [2], "Submitted to Journal of
Turbomachinery", printed 2022) is kept as its own pre-publication entry.
Refs. [9] (Leonard et al. 2016, AIAA conference) and [10] (Arroyo et al.
2019, J. Sound Vib.) print the same title but differ in year and venue, and
are distinct entries. Several items are printed incompletely (no volume for
[18], [23] and [29]; the Turbo Expo paper [6] printed with its volume
string), and are recorded as printed. No printed duplicates or unparseable
items.

# Pages created or updated

Chunk 2 (2026-10-25), cited further in chunk 4. This source is cited on:

- [ACAT1 fan stage](/benchmarks/acat1-fan-stage.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [elsA](/software/elsa.md)
