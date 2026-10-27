---
type: Source
title: "Agostinelli et al. (2021) — Impact of wall heat transfer in Large Eddy Simulation of flame dynamics in a swirled combustion chamber"
description: "Wall-resolved reacting LES of the PRECCINSTA swirl burner comparing a tuned thermal-resistance wall condition with full conjugate heat transfer: the former predicts a spurious 224 Hz thermoacoustic limit cycle, the latter recovers the experimentally stable flame without changing the system's acoustic modes."
resource: "doi:10.1016/j.combustflame.2021.111728"
source_kind: paper
authors: [Agostinelli P.W., Laera D., Boxx I., Gicquel L., Poinsot T.]
year: 2021
venue: "Combust. Flame 234:111728"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2021_Crossref_Combustion_and_Flame_Agostinelli_Impact_of_wall_heat_transfer_in_Large_Eddy_Simulation_of_fla.pdf"
tags: [les, combustion, flame-wall-interaction, compressible]
timestamp: 2026-10-27T10:58:00Z
---

# Summary

Agostinelli et al. (2021) study how the thermal wall boundary condition
changes the [large-eddy simulation](/definitions/large-eddy-simulation.md)
prediction of flame shape and thermoacoustic stability in the PRECCINSTA
swirled premixed methane/air burner. The target point, case P10
(equivalence ratio 0.8, 10 kW), is a new DLR measurement and is
experimentally stable. The compressible reacting solver AVBP runs the
[$\sigma$ model](/methods/sigma-model.md) for the subgrid stress, the
third-order TTGC scheme, the dynamically
[thickened flame model](/methods/thickened-flame-model.md) with the
Charlette efficiency function, 20-species analytically reduced chemistry
and optically thin radiation. The 20.3M-tetrahedron mesh gives $y^+\approx1$–3
at the walls, so the LES is wall-resolved, not
[wall-modelled](/methods/wall-modelled-les.md). Earlier PRECCINSTA LES with
[filtered tabulated chemistry](/methods/flamelet-tabulated-chemistry.md) are
cited as background only.

Two wall treatments are compared. The authors' Heat Resistance Tuning (HRT)
imposes a wall heat flux $q_w=(T_f-T_{\mathrm{ref}})/R$ with one thermal
resistance $R$ per surface. The resistances are tuned against wall and flow
temperatures measured at two other operating points, on the premise that
they are a property of the rig and nearly independent of the operating
point. Full conjugate heat transfer (CHT) couples AVBP with the solid
conduction solver AVTP, with the solvers desynchronized to speed up the
convergence of the solid temperature.

HRT reproduces the mean flame at the tuning points. At P10, however, it
predicts a self-excited limit cycle at 224 Hz with about 800 Pa
(experiment: about 200 Pa, stable), and no change of the inlet acoustic
relaxation coefficients suppresses it. CHT gives a stable flame with the
right length and angle and good mean and r.m.s. velocity profiles. The
Helmholtz modes computed from the two mean fields are nearly identical
(257 and 480 Hz), so the difference is not in the acoustics. A dynamic mode
decomposition with a local Rayleigh index traces the HRT instability to
fuel-jet flapping. Under CHT, conduction through the solid redistributes heat
from the flame–wall contact zones and preheats the fresh gas to about 400 K,
which damps the flame branches and tips.

# Version read

Version of record (Elsevier, Combust. Flame 234:111728; received 12 May
2021, online 26 September 2021); 17 pages, all read, pp. 5, 9, 13–16 checked
visually. Page 1 prints the first author as "P.W. Agostinelli" (Crossref:
"Agostinelli P."); no other identity problem.

# Key claims

1. Thermal wall treatments fall into four categories of increasing complexity: adiabatic, imposed wall temperature, imposed local thermal resistance $q_w=(T_f-T_{\mathrm{ref}})/R$, and CHT (classification attributed to Kraus et al.; §1). **Stated**
2. To the authors' knowledge the effect of heat transfer on the thermoacoustic behaviour of PRECCINSTA had not been analysed; Bénard et al. first introduced wall heat losses there (stable regime, numerically tuned imposed temperature profile, adiabatic centerbody; §1). **Stated**
3. Thermal resistances are an intrinsic property of the system (geometry, materials, cooling) and, to a first approximation, do not change significantly with the operating condition, so resistances tuned at a few regimes hold for all (§3.1, footnote 2). **Stated** (assumption)
4. Tuning on case P20$_{\mathrm{CB}}$ gives $R_{\mathrm{backplane}}=4.3\times10^{-3}$ and $R_{\mathrm{centerbody}}=7.5\times10^{-3}$ m²K/W; the LES centerbody tip reaches 600 K and the backplane 650 K against measured 580–610 K and 630–670 K (§3.1, Fig. 5). **Shown**
5. HRT predicts a locally higher backplane temperature at ±17 mm than measured, a limitation of one resistance per surface: transverse conduction in the solid (Biot number much lower than one) homogenizes the real wall temperature (§3.1, Fig. 5b). **Shown**
6. Tuning on case P30$_{\mathrm W}$ (flow temperature profiles) gives $R_{\mathrm{walls}}=7\times10^{-2}$ m²K/W, with good mean and r.m.s. temperature profiles and a slight underestimate of the flame angle and of the r.m.s. peak at 30 mm (§3.1, Fig. 6). **Shown**
7. With HRT the centerbody tip reaches about 900 K in P30$_{\mathrm W}$ against 600 K in P20$_{\mathrm{CB}}$, which may explain why Fredrich et al., prescribing the P20$_{\mathrm{CB}}$ temperature, did not obtain an attached flame (§3.1). **Stated** (interpretation of a shown result)
8. A fixed wall-temperature profile is "not appropriate in reactive LES": temperature is an output that must respond to flame–wall interaction, and the profile is case-dependent; HRT is "more general and more powerful" (§3.1). **Stated**
9. At P10, HRT captures the mean flame angle with a slightly short flame but predicts a limit cycle at 224 Hz with $p'\simeq800$ Pa against $\simeq200$ Pa measured, the pressure–heat-release phase lying within $\pi/2$ (Rayleigh criterion met), with a second pressure peak at 480 Hz (§3.1, Figs. 8–9). **Shown**
10. The HRT limit cycle is driven by fuel-jet flapping in the swirler, which pushes rich pockets into the chamber periodically, as in the mechanism of Franzelli et al. for the pulsating flame of Meier et al. (§3.1, Fig. 10). **Shown**
11. Varying the NSCBC relaxation coefficients ($K_{\mathrm{air}}=50$ s⁻¹ with $K_{\mathrm{fuel}}=5\times10^3$ or $5\times10^5$ s⁻¹; $K_{\mathrm{air}}=5\times10^3$ s⁻¹; almost anechoic $K_{\mathrm{air}}=5$ s⁻¹) never suppresses the oscillation; the fuel-line impedance has no relevant effect, a stiffer air line raises the amplitude and shifts the frequency to 244 Hz, and underestimated acoustic damping is not the cause (§3.1, Fig. 11). **Shown**
12. The 390 Hz against 290 Hz frequency error of Franzelli et al., attributed there to the fuel-line impedance, was "maybe due to the adiabatic walls (i.e. higher sound speed) and to the $K_{\mathrm{air}}$ coefficient" (footnote 5). **Stated**
13. Fluid and solid time scales differ greatly (time steps $\sim10^{-8}$ s against $\sim10^{-5}$ s; flow-through time of order ms against a solid time of 1–10 s); desynchronizing the solvers is equivalent to reducing the solid heat capacity and accelerates convergence to the solid steady state (§3.2). **Stated**
14. CHT recovers a stable flame: after thermal convergence the pressure fluctuations are of order 200 Pa, heat release is no longer correlated with pressure, and the 224 Hz peak is absent ($t\ge0.83$ s), leaving a weak 480 Hz peak (§3.2, Fig. 13). **Shown**
15. CHT predicts an internal chamber-wall temperature up to about 1350 K at 40 mm from the backplane, a uniform backplane at about 600 K and a centerbody tip at about 800 K (§3.2, Fig. 14a). **Shown**
16. CHT predicts preheating of the fresh gas to about 400 K (inlet 293 K), non-homogeneous and higher near the walls, against the 320 K assumed in earlier studies (§3.2, Fig. 14b). **Shown**
17. CHT flame length and angle agree better with OH* chemiluminescence than HRT; mean axial velocity is captured, the central recirculation slightly weak at 15 and 20 mm and the r.m.s. slightly high; the poorer tangential-velocity match is attributed to out-of-plane sPIV error (§3.2, Figs. 15–17). **Shown**
18. The mean sound-speed fields differ, but the Helmholtz modes of both are comparable (257 Hz quarter-wave plenum mode, 480 Hz three-quarter-wave chamber mode): heat transfer "does not change the system acoustics significantly" (§3.3, Figs. 18–19). **Shown**
19. The HRT limit cycle (224 Hz) couples with the quarter-wave mode (257 Hz); the computed modes match the two small experimental peaks (260 and 480 Hz) (§3.3). **Shown**
20. DMD of 400 LES snapshots at 224 Hz: under HRT the Rayleigh index is positive (driving) at the flame root and branches ($10<x<40$ mm) and negative downstream of the centerbody and slightly at the flame tips; the equivalence-ratio correlation index confirms that rich pockets feed the oscillation (§3.3, Fig. 20a). **Shown**
21. During the HRT-to-CHT transient the root still drives, the branches drive less and less coherently and the tips damp more; stabilization starts at the branches and tips in contact with the chamber walls (§3.3, Figs. 20b, 21). **Shown**
22. The axially averaged mean heat release peaks at $x=27$ mm (HRT) against 35 mm (CHT, a longer flame); the CHT Rayleigh-index distribution is almost zero (§3.3, Fig. 21). **Shown**
23. Only CHT captures the rapid redistribution of heat from where the flame reaches the walls; a locally tuned $R$ would still miss the non-homogeneous preheating, and with $T_{\mathrm{ref}}=293$ K HRT always transfers heat from gas to solid (§3.3, footnote 6). **Stated** (supported by the shown comparisons)
24. High-fidelity combustion LES needs precise wall thermal boundary conditions, not only precise inlet and outlet acoustic impedances (§4). **Stated**
25. The initial resistance estimates are $R=2.4\times10^{-3}$ m²K/W for centerbody and backplane (conduction, $L_s=36$ mm, $\lambda_s=15$ W/(m K)) and $R_{\mathrm{eq}}=1\times10^{-2}$ m²K/W for the chamber walls (conduction plus external natural convection and radiation), of "the same order of magnitude" as the tuned values; one tuning iteration sufficed (App. A, Eqs. A.1–A.7). **Derived**

# Printed slips

- Eq. (A.4) prints $R_{rad}=\epsilon\sigma(T_{wall}^4-T_{ambient}^4)/(T_{wall}-T_{ambient})$. The right-hand side has the units W/(m²K) of a heat-transfer coefficient, that is of $1/R_{rad}$, while Eq. (A.3) correctly writes $1/R_{conv}=h_{conv}$ *(compiler check by dimensions, not in the sources)*.
- Symbol drift in App. A: $L_{conv}$ in Eq. (A.3) against $L_{cv}$ in the text; $R_{conduction}$ against $R_{cond}$. §1 writes the resistance condition with $q$, §3.1 with $\Phi_q$.
- §3.1: "Figure 10(a–c) correspond to the minimum (ϕ = 0) and maximum (ϕ = π)" and "Fig. 10(b–d)" use an en-dash for "and" (panels a and c, b and d).
- References [3] and [27] are the same work (Huang, Sung, Hsieh, Yang, J. Propul. Power 19 (2003) 782–794), printed twice; ref. [72] prints the journal name fused into the title ("International journal of heat and fluid flow development and assessment of a coupled strategy…"); ref. [60] prints the URL "www.me.berkley.edu".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Phi_q$, $q$ | $q_w$ (wall heat flux, page-local) | |
| $\Phi_{q,i}$ | (conductive heat flux in the solid, page-local) | Fourier's law, Eq. (2) |
| $T_f$, $T_{ref}$, $T_{wall}$, $T_{flow}$ | same with roman subscripts (page-local) | fluid temperature at the wall; reference (ambient or external-wall) temperature; wall temperature; near-wall flow temperature outside the thermal layer |
| $R$, $R_{eq}$, $R_{cond}$, $R_{conv}$, $R_{rad}$, $R_{flow}$ | same (thermal resistances per unit area, page-local) | m²K/W |
| $\lambda_s$, $\lambda_{air}$ | (thermal conductivities, page-local) | **collision** with the Taylor microscale $\lambda$ |
| $\rho_s$, $C_s$ | (solid density, heat capacity, page-local) | |
| $\epsilon$, $\sigma$ | (emissivity, Stefan–Boltzmann constant, page-local) | **collision** with $\varepsilon$ (dissipation) and $\sigma_{ij}$ (viscous stress) |
| $h$, $Bi$, $\mathrm{Ra}_L$ | (heat-transfer coefficient, Biot and Rayleigh numbers, page-local) | **collision:** the registry $h$ is the cell size |
| $\Delta_x$ | $h$ | cell size in the flame zone, 300 μm; not the filter width $\Delta$ |
| $y^+$ | $y^+$ | |
| $\overline c$, $\overline T$ | $\langle c\rangle$, $\langle T\rangle$ | **collision:** the source's overbar is a time average, not the LES filter |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle_{S_c}$ (cross-section average over $S_c$, page-local) | Eq. (3); written with the subscript so as not to be confused with the time average above |
| $\phi$ | (equivalence ratio, page-local) | |
| $K_{air}$, $K_{fuel}$ | same (NSCBC relaxation coefficients, page-local) | s⁻¹ |
| $\beta_{Ch}$ | same (Charlette efficiency-function exponent, page-local) | 0.5 |
| $\hat p$, $\hat q$, $\hat\phi$, $\varphi_p$, $\varphi_q$, $\varphi_\phi$ | (DMD mode amplitudes and phases, page-local) | the hat is not a test filter |
| $\mathcal{R}e(\widehat{RI})=\mathcal T_{q,p}$, $\mathcal T_{\phi,p}$ | same (local Rayleigh index; equivalence-ratio–pressure index, page-local) | |
| $\tau_f$, $\tau_s$ | (fluid flow-through and solid thermal times, page-local) | **collision** with $\tau_{ij}$ |

The paper prints neither the filtered equations nor the $\sigma$-model
constant.

# Reference list

80 printed references, numbered style ([1]–[80]). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Refs. [3] and [27] are one work printed twice (folded into one entry).
Ref. [57] (Agostinelli et al., *Static mesh adaptation for reliable Large
Eddy Simulation of turbulent reacting flows*, Phys. Fluids 33 (2021)
035141) is a different work from this paper and is keyed `agostinelli-2021-b`. Ref. [52] is printed without volume, ref. [60] is a web item (GRI-Mech
3.0); all items parsed.

# Pages created or updated

Chunk 9 (2026-10-27). This source is cited on:

- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
- [Sigma model](/methods/sigma-model.md)
- [Thickened flame model](/methods/thickened-flame-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
