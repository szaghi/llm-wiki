---
type: Source
title: "Lewis et al. (2023) — Large Eddy Simulation of the ACAT1 fan stage for broadband noise prediction"
description: "Compares two wall-modelled LES of the ACAT1 fan–outlet-guide-vane stage at approach (95 and 210 million cells, both within published WMLES wall-mesh criteria) with RANS and measurements; the refinement removes a stator separation, improves wakes and spectra, and the wall pressure feeds acoustic analogies for broadband noise."
resource: "doi:10.1016/j.jsv.2023.117888"
source_kind: paper
authors: [Lewis D., Moreau S., Jacob M.C., Sanjosé M.]
year: 2023
venue: "J. Sound Vib. 565:117888"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Journal_of_Sound_and_Vibration_Lewis_Large_Eddy_Simulation_of_the_ACAT1_fan_stage_for_broadband_n.pdf"
tags: [les, wmles, wall-model, turbomachinery, aeroacoustics, grid-requirements]
timestamp: 2026-10-26T07:39:00Z
---

# Summary

Lewis et al. (2023) predict the broadband noise of the
[ACAT1 fan stage](/benchmarks/acat1-fan-stage.md) (20 blades, 44 outlet
guide vanes, AneCom UFFA rig) at the approach point with a hybrid method.
A scale-resolving simulation supplies the wall-pressure fluctuations on
rotor and stator, which then feed acoustic analogies as dipole sources.
Two [wall-modelled LES](/methods/wall-modelled-les.md) are run with the
compressible unstructured solver AVBP (Lax–Wendroff scheme, second order;
[WALE](/methods/wale-model.md) subgrid model; rotor and stator domains
coupled by an overset method). LES1 has 95 million cells and comes from the
authors' earlier work; LES2 has 210 million, with 14 instead of 8 prism
layers and finer blade and vane surface meshes. The wall treatment is an
algebraic [equilibrium](/methods/equilibrium-wall-model.md)
[wall law](/definitions/law-of-the-wall.md), linear below $y^+=11$ and
logarithmic above. Both LES are compared with a wall-resolved
[$k$-$\omega$ SST](/methods/k-omega-sst-model.md) RANS, with ZDES results of
the same stage ([detached-eddy simulation](/methods/detached-eddy-simulation.md))
and with hot-wire and acoustic measurements. To simulate an 18° sector,
the vane count is reduced from 44 to 40 rescaled vanes.

Both meshes are stated to meet published WMLES wall-mesh requirements
([grid-point requirements](/results/les-grid-point-requirements.md)).
Yet the large mid-chord stator separation of LES1 disappears in LES2, and
the authors conclude that wall laws must be used with caution because the
criteria "are actually quite broad". LES2 also improves the interstage wake
profiles and velocity spectra. LES1's wake grows abruptly at the
rotor/stator interface, where its coarser downstream mesh "enhances
diffusion" ([numerical dissipation](/properties/numerical-dissipation.md)).
The wall pressure reveals three broadband mechanisms: the rotor
leading-edge radial vortex with transition and trailing-edge scattering;
the rotor–stator interaction at the vane leading edge; and the vane
boundary-layer transition with trailing-edge scattering. Free-field
Ffowcs Williams–Hawkings predictions overpredict the noise levels;
Goldstein's in-duct analogy lowers them; with an indicative rotor-shielding
correction, LES2 agrees very well with the measurements. The paper is an
aeroacoustics application, peripheral to closure modelling; its modelling
content is the [LES](/definitions/large-eddy-simulation.md) mesh-sensitivity
finding.

# Version read

HAL deposit hal-04152947v1 of the accepted author manuscript (file
"JSV_LES2_revision.pdf"; footer "Preprint submitted to JOURNAL OF SOUND
AND VIBRATION, March 12, 2023"; Elsevier CC BY-NC notice), not the
typeset version of record. The PDF has 47 pages: a HAL cover page, 43
manuscript pages, highlights and statements, all read. Page 1 matches the
metadata (the cover page prints the title in sentence case and the author
"Marc Jacob"). Page, section, equation, figure and table numbers on this
page are those of the manuscript.

# Key claims

1. Two WMLES of the full ACAT1 stage at approach differ in mesh refinement: LES1 has $56+39=95$ million cells, LES2 $125+85=210$ million (rotor plus stator) (§3.3, Table 7). **Shown**
2. Both meshes are stated to satisfy the WMLES wall-mesh requirements of Table 5 ($\Delta x^+$ 100–600, $\Delta z^+$ 100–300, $\Delta y^+$ 30–150), with mean/maximum $\Delta y^+$ of 25/66 (LES1) and 17/64 (LES2) and mean/maximum streamwise and spanwise $\Delta^+$ of 80/300 (LES1) and 64/195 (LES2) on blade and vane surfaces (§3.3, Tables 5–6, Figs. 4–6). **Shown** (see Printed slips, item 1)
3. The large separation at about 65% of the stator chord over almost the whole vane span in LES1, with a radial vortex at 60% chord, disappears in LES2 through wall-mesh refinement: "wall laws should be used with caution since wall-mesh requirements for WMLES are actually quite broad", and two compliant WMLES "may exhibit significant discrepancies" (§4.2.1, Fig. 13; §4.2.2, Fig. 17). **Shown**
4. Even WMLES able to predict large detachments "might fail to accurately predict the exact detachment and reattachment points" (§4.2.2). **Stated**
5. RANS and LES1 reproduce the measured mass flow and fan pressure ratios closely (LES1: total mass flow $+0.05\%$, total pressure ratio $-0.36\%$); LES2 overpredicts the mass flow by 2.7% (bypass $+2.8\%$), attributed to its changed stator flow topology (§4.1, Tables 9–10). **Shown**
6. A strong radial vortex forms at the rotor leading edge in all simulations, from 40% span to the tip in RANS and over almost 80% of the span in both LES; it is considered characteristic of fans at low speed (§4.2.1, Fig. 12). **Shown**
7. The rotor leading-edge separation covers, as printed, "75% to 95% of the rotor span" and the first 15% of the chord; in RANS it extends from 25% span to the tip; in the LES the flow reattaches before a quarter chord and detaches again at 60% chord between 30% and 60% span (§4.2.2, Fig. 16). **Shown**
8. The apparent split of the mean rotor separation in two parts results from averaging an intermittent separation bubble (§4.2.2; §4.4.1, Fig. 26). **Shown**
9. RANS misses the radial secondary flows predicted by both LES (§4.2.2). **Shown**
10. Mean and rms wake profiles at the interstage plane HW1 improve from LES1 to LES2: at 75% span the LES2 rms profiles lie almost entirely within the experimental range over a revolution, at 95% span only LES2 recovers the measured rms levels, and the LES rms profile shapes match the measured ones better than RANS (§4.3.1, Figs. 19–23). **Shown**
11. LES1 overestimates the axial-velocity spectrum at HW1 (50% span) by 5–10 dB between 1 and 5 kHz, LES2 by less than 5 dB at low frequency, decreasing to 2 dB above 4 kHz; for the azimuthal component the gap is an almost constant 10 dB for LES1 and 1–2 dB up to 3 kHz, rising to 5 dB at 7 kHz, for LES2; for the radial component LES2 is within 1–3 dB (§4.3.2, Fig. 24). **Shown**
12. The measured spectra drop at 7–8 kHz because the hot wires (up to 12 µm diameter) cut off at about 8 kHz; Polacsek et al. estimated the measured rms to be underestimated by a factor of about 1.5 (§4.3.2). **Stated** (cited)
13. In LES1 the wake grows abruptly at the rotor/stator domain interface because the coarser downstream mesh "enhances diffusion"; in LES2 this disappears except at 25% span, where the interstage refinement block does not reach (§4.4.1, Fig. 26). **Shown**
14. Stator wall-pressure rms shows the rotor–stator interaction source at the leading edge (lower in LES2 than in LES1) and a second high-rms zone from about 60% chord, associated with boundary-layer transition; on the rotor the high rms sits at the leading-edge vortex, with a magnitude comparable to the stator leading edge (§5.1, Figs. 27–28). **Shown**
15. The rear-part (60–100% chord) stator pressure spectrum is most intense between 1 and 8 kHz and 10 dB higher in LES1 than in LES2; on the rotor the wall-pressure spectrum decreases by 10–15 dB from leading to trailing edge (§5.1, Figs. 29–30). **Shown**
16. The mean radial coherence length of the incident velocity at the vane leading edge is 5–10% of the stator span for all components, less than the 20% found by de Laborderie et al. on the CME2 compressor (§5.2.1, Fig. 33, Eq. 4). **Shown**
17. Coherence maps were filtered by fitting a Gaussian to the values above 0.25 before integration, because raw integration overestimates the length scale; the procedure is still nonphysical above 15 kHz (§5.2.1). **Shown**
18. The radial coherence of the vane wall pressure at 0.5% chord decays quickly from midspan except at blade-passing-frequency harmonics, consistent with the hypothesis of Posson's model (§5.2.2, Figs. 34–35). **Shown**
19. Ffowcs Williams–Hawkings stator noise from LES2 recovers the spectral shapes but overpredicts: by 5–7 dB upstream between 1 and 5 kHz, by at most 5 dB downstream at low-to-mid frequencies, and by an almost constant 4 dB (upstream) and 2 dB (downstream) above 5 kHz (§5.3.1, Fig. 36). **Shown**
20. LES2 reduces the low-to-mid-frequency gap of LES1 by almost 5 dB; above 5 kHz the two LES predictions almost coincide (§5.3.1, Fig. 37). **Shown**
21. Goldstein's in-duct analogy gives levels at least 2 dB below Ffowcs Williams–Hawkings over the whole range, about 5 dB below between 3 and 6 kHz, confirming that neglecting duct cut-off causes part of the overprediction (§5.3.1, Figs. 36, 38–39). **Shown**
22. With an indicative rotor-shielding correction ($-3$ dB upstream, $+3$ dB downstream, from Blázquez-Navarro & Corral), the LES2 Goldstein predictions agree very well with the measurements (§5.3.1, Fig. 42). **Shown**
23. Splitting the vane into a front (first 40% of the maximum axial chord) and an aft part, the aft part is the dominant stator contributor in both LES, even in LES2 without stator separation; front and aft are strongly correlated; the aft–front gap is about 10 dB, against about 5 dB in Polacsek et al.'s split at 50% chord (§5.3.1, Eq. 5, Figs. 40–41). **Shown**
24. Rotor noise from both LES is comparable to or higher than the noise of the vane front part; for LES2 the rotor noise above 8 kHz is similar to that of the whole vane row (§5.3.2, Fig. 43). **Shown**
25. Three broadband mechanisms are identified (rotor leading-edge radial vortex with transition and trailing-edge scattering; rotor–stator interaction at the vane leading edge; vane boundary-layer transition with trailing-edge scattering), and the turbulent trailing-edge scattering "could exceed that of the RSI mechanism", which questions the assumption that rotor–stator interaction alone dominates fan broadband noise at approach (§6; Abstract; Highlights). **Shown**
26. A mesh as fine as LES2 is "mandatory to provide reliable results using this approach" (§5.3.1; §6). **Stated**
27. Quadrupole and monopole sources are neglected because the rotor relative tip Mach number is 0.57 (§5.3). **Stated**

# Printed slips

1. §3.3 states that Figs. 5–6 confirm that "the mesh is consistent with the wall requirements for wall-modelled LES", but the printed mean $\Delta y^+$ (25 for LES1, 17 for LES2, Table 6) lies below the WMLES range 30–150 of Table 5, and the mean streamwise and spanwise $\Delta^+$ (80, 64) lie below the ranges 100–600 and 100–300. The paper does not say whether the ranges are meant as upper limits.
2. Table 9 prints the LES2 total mass flow as 56.647 kg/s, while its bypass and core values sum to $50.108+6.500=56.608$ kg/s; the printed $+2.7\%$ matches 56.647 *(compiler check, not in the sources)*.
3. Table 10 prints the LES2 bypass pressure ratio as "1.109 (−0.01%)" against the measured 1.110, while $1.109/1.110-1=-0.09\%$ *(compiler check, not in the sources)*.
4. §3.1, introducing LES2: "LES1 computational domain is strictly identical to that of the LES1 presented by Lewis et al. [16]".
5. Eq. (3) text names the point "$(x,r,\theta)$", while the equation uses $(x,\theta,r)$.
6. In the reference list, [6] and [67] are the same Ffowcs Williams & Hawkings (1969) paper, and [18] and [56] the same Meyer et al. ETC2019-330 paper; [36] prints the second author of the NSCBC paper as "S. Lelef"; [38] prints "E. Nicoud"; [35] prints "arXiv:arXiv:1503.01439v1" for a 1999 paper; [50] prints "arXiv:https://arc.aiaa.org/doi/pdf/10.2514/6.2021-2256"; [52] prints a JSV article with the DOI prefix "10.1017/jfm".

# Notation map

| Lewis et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $n^+$, $y^+$ | $\Delta y^+$ | wall-normal cell size at the wall in wall units; the source uses $n^+$ and $y^+$ interchangeably |
| $s^+$, $r^+$ | $\Delta x^+$, $\Delta z^+$ | streamwise and "third local direction" cell sizes in wall units; **collision:** $r$ is also the radius |
| $C_f=\tau_w/(\tfrac12\rho_\infty V_\infty^2)$, $\tau_w=\mu(\partial V_s/\partial n)_{\mathrm{wall}}$ | $C_f$, $\tau_w$ | normalized with the inlet density and velocity |
| $V_x$, $V_\theta$, $V_r$; $V'_{x,rms}$ | (mean axial, azimuthal, radial velocity; rms fluctuations) | cylindrical components |
| TKE | $k$ | hot-wire value; no formula printed |
| $\Phi_{u_i}$, $\phi_{pp}$ | (cross-spectral density of a velocity component; wall-pressure spectrum in dB re $2\cdot10^{-5}$ Pa) | |
| $\gamma^2_{u_i}$, $\gamma^2_p$ | (squared coherence, page-local) | **collision:** not the ratio of specific heats |
| $\omega$ | (angular frequency) | **collision:** not the specific dissipation rate or the vorticity |
| $u_{xc}$, $w$, $u_r$ | (chordwise, upwash, radial velocity in the cascade frame) | **collision:** $w$ is not the spanwise velocity component |
| $L_{r,u_i}$, $L_{r,p}$ | (radial coherence lengths, Eq. 4) | normalized by $R_T-R_H$ |
| $R_H$, $R_T$ | (hub and tip radius) | |
| $\Phi_{Full}$, $\Phi_{Front}$, $\Phi_{Aft}$ | (observer spectra of the full, front and aft vane, Eq. 5) | |
| BPF, FPR, RSI, SWL | (blade passing frequency, fan pressure ratio, rotor–stator interaction, sound power level) | |
| LES1, LES2 | (95 and 210 million-cell WMLES) | |

No Reynolds number of the configuration and no filter definition are printed.

# Reference list

68 printed references, numbered style. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug. Two printed
duplicates are folded into one entry each: [6] = [67] (Ffowcs Williams &
Hawkings 1969) and [18] = [56] (Meyer et al. 2019). Same-author same-year
works take suffixes in printed order (Lewis et al. 2020 AIAA paper and
Lewis's 2020 PhD thesis; Pérez Arroyo et al. 2021 Parts I and II; Al-Am et
al. 2022, JSV and AIAA paper; de Laborderie 2013 AIAA paper and thesis).
The citation of François et al. (2022, ZDES Part I) is the bundle's Source
[francois-2022](/sources/francois-2022.md). Reference [17] prints the AIAA
J. 60(1) (2022) issue of the work that francois-2022 cites as AIAA J.
(2021) without a volume (one entry, `lewis-2021`); reference [24] prints the published form (J.
Turbomach. 144:111005) of the ZDES Part II that francois-2022 cites as
submitted, which stays a distinct entry (`polacsek-2022-b`) under the preprint rule. [50]
prints no year (2021 is read from its AIAA paper number), [46] is a book
printed without publisher, and [62] prints a handle in its DOI field; all
are recorded as printed.

# Pages created or updated

Chunk 4 (2026-10-26), cited further in chunk 6. This source is cited on:

- [ACAT1 fan stage](/benchmarks/acat1-fan-stage.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Ffowcs Williams–Hawkings acoustic analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [WALE model](/methods/wale-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
