---
type: Source
title: "Thawait et al. (2023) — Delayed detached eddy simulation-based aerothermoelastic analysis of deployable control fin in supersonic and hypersonic flows"
description: "Strongly coupled fluid–thermal–structural analysis of a deployable control fin with joint freeplay at Mach 3–6, assembled from ANSYS Fluent (density-based, AUSM+, SST-based delayed detached-eddy simulation), ANSYS Mechanical and System Coupling; validated on a flutter and a heated-panel experiment, with no turbulence-model assessment."
resource: "doi:10.1063/5.0165168"
source_kind: paper
authors: [Thawait A.K., Tandaiya P., Jain P.C., Chandy A.J.]
year: 2023
venue: "Phys. Fluids 35:096110"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Physics_of_Fluids_Thawait_Delayed_detached_eddy_simulation-based_aerothermoelastic_ana.pdf"
tags: [des, fluid-structure-interaction, hypersonic, software, compressible]
timestamp: 2026-10-28T02:16:00Z
---

# Summary

Thawait et al. (2023) compute the nonlinear aerothermoelastic response of a
deployable cropped-delta control fin with a diamond section, whose outboard
part is connected to the inboard part by a revolute joint with freeplay,
at Mach 3 to 6 at 15 km altitude conditions. The time-domain
fluid–thermal–structural coupling is assembled from commercial components:
[ANSYS Fluent](/software/ansys-fluent.md) as flow solver
(density-based implicit finite volume, AUSM+ flux, dual time stepping) with
the [SST](/methods/k-omega-sst-model.md)-based delayed
[detached-eddy simulation](/methods/detached-eddy-simulation.md), ANSYS
Mechanical (20-node thermoelastic bricks, a zero-stiffness revolute joint
with stoppers, HHT-$\alpha$ time integration), and ANSYS System Coupling
with profile-preserving and conservative mapping; the mesh moves by
diffusion-based smoothing. DES is chosen as the
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) remedy because RANS is
said to be unsuitable for shock and separation unsteadiness and
[shock–boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
(citing Sartor & Timme) while LES is too costly near walls.

The coupling is validated on the flutter onset of a $45^\circ$ swept wing
at Mach 3 (flutter velocity within 5%, stiffness-altitude parameter 0.41
against 0.385) and on the time-averaged deflection of a pre-heated buckled
panel at Mach 4 (errors of 3.18% and 0.12%). A three-grid study selects
2.7 million cells. The parametric study over Mach number, angle of attack
and freeplay finds two shocks over the inner half-span, separation and
attachment lines and the highest modelled $k$ behind the joint, a
leading-edge temperature growing with Mach number to about 550 K at Mach 6
and insensitive to incidence and freeplay, tip deformation growing with
Mach number (through the temperature-dependent modulus), incidence and
freeplay, and a bending–torsion response without freeplay against bending
only with it. Turbulence enters only as the off-the-shelf closure: the
paper assesses neither the hybrid switch nor the resolution of its LES
branch, and compares the DDES with no RANS run.

# Version read

Version of record (AIP; received 27 June 2023, published online 20
September 2023); 19 PDF pages (cover sheet plus pages 096110-1 to
096110-18), all read, with Eqs. (1)–(25) and Table II checked visually.
Page 1 matches Crossref.

# Key claims

1. RANS models are "not suitable" for "unsteadiness in the shock and separated region, and shock-boundary layer interaction", so shock-induced vibration predictions are less accurate (ref. 33); LES is costly near walls and restricted to moderate Reynolds numbers; DES is adopted as the hybrid remedy (§I). **Stated**
2. To the authors' knowledge no earlier study gives a high-fidelity aerothermoelastic analysis of a deployable fin with joint freeplay in supersonic or hypersonic flow, nor couples a DDES flow solver strongly to a thermoelastic finite-element solver (§I). **Stated**
3. The maximum Mach number is 6 at a dynamic pressure of 3 bar and the maximum temperature about 550 K; since departures from a calorically perfect gas "start appearing after 800—1000 K", the air is calorically perfect and non-equilibrium effects are neglected (§I, refs 25, 30, 34). **Stated**
4. The original DES switches between RANS and LES on the local grid size and suffers modelled-stress depletion when LES activates in cells smaller than the boundary-layer thickness; DDES "preserves RANS in the boundary layer" (§II B, refs 36–37). **Stated**
5. SST "accounts for the transport of the turbulent shear stress and is more accurate than the standard version", and the eddy-viscosity limiter is applied because standard $k$-$\omega$ "overpredicts the eddy viscosity" (§II B, Eq. 8, citing the ANSYS theory guide). **Stated**
6. The SST-DDES modifies the destruction of $k$, $Y_k=\rho\beta^*k\omega F_{\mathrm{DES}}$, with $F_{\mathrm{DES}}=\max\big(l_{\mathrm{RANS}}(1-F_{\mathrm{DDES}})/(C_{\mathrm{DES}}\Delta_{\max}),1\big)$, $l_{\mathrm{RANS}}=\sqrt k/(\beta^*\omega)$, $C_{\mathrm{DES}}=0.61$, $F_{\mathrm{DDES}}=\tanh[(C_{d1}r_d)^{C_{d2}}]$, $C_{d1}=20$, $C_{d2}=3$, $r_d=(\nu_t+\nu)/\big(\kappa^2d^2\sqrt{0.5(S^2+\Omega^2)}\big)$ (§II B, Eqs. 9–13; $S$, $\Omega$ the strain and vorticity magnitudes, normalization not stated). **Stated**
7. AUSM+ "provides exact resolution of shock discontinuities, preserves positivity of scalar quantities, and is free of oscillations at stationary and moving shocks" (§II C, citing the ANSYS guide). **Stated**
8. The flow solver uses second-order dual time stepping (BDF2 coefficients 3/2, 2, 1/2), second-order upwind convection, second-order central diffusion, least-squares cell gradients, and ILU smoothing with algebraic multigrid (§II E, Eqs. 18–19). **Stated**
9. HHT-$\alpha$ with Newton–Raphson gives "controllable numerical dissipation in high-frequency modes" at second order (§III). **Stated**
10. Mach 3 wing: at the experimental flutter velocity (618.7 m/s) the tip oscillation has constant amplitude; at 1.05 times it (dynamic pressure from 60 to 66 kPa) the response diverges, so the flutter-velocity error is "below 5%" (§V A, Fig. 3). **Shown**
11. Mach 3 wing: the stiffness-altitude parameter is 0.41 against 0.385 in the literature, an error of 6.6% (§V A). **Shown**
12. Heated panel at Mach 4: the time-averaged deformations at the two bay centres agree with the experiment within "approximately 3.18% for point A and 0.12% for point B"; the high-frequency panel oscillations of the experiment are not captured, the time step they need being infeasible with the implicit strategy (§V B, Fig. 6). **Shown**
13. Grid study on 1.35, 2.7 and 5 million cells: the quantities are "well converged for 2.7×10⁶ cells", used throughout; apparent orders 3.17, 3.8, 5.1 and GCI of 3.1%, 8.4%, 1.33% for the root and tip $C_p$ and the maximum temperature (§VI A, Table II, Fig. 8). **Shown**
14. Two shocks form up to half the span, from the leading edge and from the thickness increase at the root and joint; their strength decreases toward the tip, and with Mach number the shock angle decreases and the strength increases (§VI B, Fig. 9). **Shown**
15. The modelled $k$ is minimum near the leading edge and maximum at the trailing edge, highest behind the joint section, decreasing toward the tip and increasing with Mach number, read as increasing fluid shear stress (§VI B, Fig. 10). **Shown**
16. Skin-friction lines show two separation lines caused by the thicker joint and two attachment lines with higher wall shear over it (Mach 5, $2^\circ$); a reversed-flow zone with spiralling streamlines appears behind the joint trailing edge (§VI B, Figs. 11–12). **Shown**
17. At $2^\circ$ incidence and Mach 5 the shock is weaker on the top and stronger on the bottom surface; wall pressure and temperature are higher on the bottom and peak at the leading edge and the thickening zones; tip vortices give a small low-pressure, high-shear zone (§VI B, Figs. 13–14). **Shown**
18. $C_f$ is positive along the whole chord at all sections and decreases with Mach number; a jump near the trailing edge is largest at the root; with incidence $C_p$ increases and $C_f$ rises on the bottom and falls on the top surface (§VI B, Figs. 15–16). **Shown**
19. Without freeplay the trailing-edge-tip deformation is largest and combines bending and torsion; with freeplay the fin oscillates in bending only after the freeplay motion (Mach 5, $2^\circ$, Fig. 17). **Shown**
20. Tip deformation grows with Mach number, attributed to the lower elastic modulus of the temperature-dependent Ti6Al4V; the amplitude is largest for Mach 5 up to 0.02 s and for Mach 6 afterwards; the frequency increases with Mach number except at Mach 5 (§VI C, Fig. 18a). **Shown**
21. With incidence the amplitude, frequency and mean deformation increase; with freeplay the amplitude increases and the frequency does not change (§VI C, Figs. 18b–c). **Shown**
22. The leading-edge-tip temperature grows with Mach number, faster at higher Mach numbers; thermal effects are "significant for flow having Mach number 4 and greater"; incidence and freeplay barely affect it (§VI C, Fig. 19). **Shown**
23. Kinetic and strain energies show decaying amplitudes, i.e. dynamically stable behaviour, while the strain-energy mean differs between cases; for Mach numbers above 3 it grows and "the fin may fail" once stresses exceed the yield strength (§VI C, Figs. 20–21). **Shown** (failure remark **Stated**)
24. Increasing Mach number, incidence and freeplay all give "a significant increase in deformation with reduced stability"; the frequency increases with Mach number and incidence but not with freeplay (§VII). **Shown**

Beside the SST-DDES of Eqs. (9)–(13), §II B prints "the length scale for
the DDES model" (Eq. 14) $d_{\mathrm{DDES}}=d-f_d\max(0,d-C_{\mathrm{DES}}\Delta_{\max})$
with $f_d=1-F_{\mathrm{DDES}}$, the wall-distance form of the
Spalart–Allmaras DDES, without saying where it enters the SST equations.
The flow solver integrates on a deforming mesh in arbitrary
Lagrangian–Eulerian form (Eq. 5); the paper does not discuss the geometric
conservation law.

# Printed slips

- Table II prints "$N_1,N_2,N_3$ (×10⁶): 1.35, 2.7, 5" against "$h_1,h_2,h_3$ (mm): 3.8, 5, 7.5": the smallest cell size is paired with the fewest cells; the printed ratios $r_{21}=1.32$, $r_{32}=1.5$ follow from the $h$ row.
- Table II, maximum-temperature column: $\phi_2=234$ and $\phi_3=291$ give $|\phi_2-\phi_3|/\phi_2=24.36\%$, while $e_a^{32}$ is printed "2.7863"; the other printed relative errors agree with their printed $\phi$ values to within about 0.02 percentage points *(compiler check, not in the sources)*.
- Table II, tip $C_p$ column: $e_a^{21}$ is printed "12.2836, 5"; $\phi_1=0.5658$, $\phi_2=0.6386$ give 12.87% *(compiler check, not in the sources)*.
- §V B and §VI: "density = 4430 kg/m2" for the titanium panel and fin.
- Table I lists "Reynolds no. (10⁶)" of 12.2, 16.2, 20.3, 24.3 for Mach 3 to 6 without a reference length.
- $\tau_{ij}$ is the Reynolds stress in Eq. (2) and the viscous stress in the flux $G'$ of Eq. (18); the wall distance is $y$ in Eq. (13) and $d$ in Eq. (14).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\overline{(\cdot)}$, $\widetilde{(\cdot)}$, $u_i''$ | $\langle\cdot\rangle$, $\langle\cdot\rangle_\rho$, $u_i''$ | **collision:** the overbar is a time average, not an LES filter |
| $\tau_{ij}$ ("Reynolds stress tensor") | $\langle\rho\rangle R_{ij}$ (sign not stated) | **collision** with the SGS stress; added to $\bar\sigma_{ij}$ in Eq. (2) |
| $\sigma_{ij}$ | $\sigma_{ij}$ | viscous stress; $\sigma_s$ the structural stress |
| $k$, $\omega$, $\mu_t$, $\nu_t$ | same | |
| $G_k$, $G_\omega$, $Y_k$, $Y_\omega$, $D_\omega$ | (production, destruction and cross-diffusion terms, Fluent names) | |
| $\Gamma_k$, $\Gamma_\omega$ | $\Gamma_k$, $\Gamma_\omega$ (diffusivities $\mu+\mu_t/\sigma_k$, $\mu+\mu_t/\sigma_\omega$) | |
| $\alpha^*$, $a_1$, $F_2$, $\beta^*$ | same (SST constants and blending function) | values and $F_2$ not printed; $\beta^*$ "calculated using $\rho$, $k$, $\mu$, $\omega$" |
| $S$, $\Omega$ | $\lvert S\rvert$, $\lvert\Omega\rvert$ | normalization not stated |
| $C_{des}$, $\Delta_{\max}$, $L_t$ | $C_{\mathrm{DES}}$, $\Delta_{\max}$, $l_{\mathrm{RANS}}$ (as on the DES page) | |
| $F_{DES}$, $F_{DDES}$, $f_d$, $r_d$, $C_{d1}$, $C_{d2}$ | $F_{\mathrm{DES}}$, $F_{\mathrm{DDES}}=1-f_d$, $f_d$, $r_d$, $C_{d1}$, $C_{d2}$ | $F_{\mathrm{DDES}}\to1$ in the boundary layer, the opposite polarity of $f_d$ |
| $\tilde d$ | $d_{\mathrm{DDES}}$ | **collision:** not a Favre quantity |
| $y$ (Eq. 13), $d$ | $d$ | |
| $\kappa=0.41$ | $\kappa$ | |
| $Y^+$ | $y^+$ (first-cell height) | |
| $\mu$ (mass ratio), $b$, $\omega_\alpha$, $a$ | (flutter parameters, page-local) | **collision** with the viscosity $\mu$ and $\omega$ |
| $\alpha$ | (mesh-diffusion exponent; thermal expansion; HHT parameter) | **collision** with the DG blending factor $\alpha$ |
| $\varepsilon_0$, $\varepsilon_1$, $\varepsilon_2$ | (BDF2 coefficients, page-local) | **collision** with $\varepsilon$ (dissipation rate) |
| $p$ (Table II), $h_i$, $\phi_i$, GCI | (apparent order, grid size, grid-study quantity) | **collision:** $p$ is the pressure, $h$ the cell size |

# Reference list

42 printed references, numbered (superscript) AIP style, all parsed. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Ref. 35 (a NASA Turbulence Modeling Resource web
page) prints no author or year and ref. 38 is the ANSYS 2022R1 theory
guide; ref. 28 is printed with first author "A. A. Kumar" and cited in the
text as "Arun et al."; refs. 36 and 37 are Spalart (1997) and Strelets
(2001), already in the bibliography. No printed duplicates.

# Pages created or updated

Chunk 12 (2026-10-28). This source is cited on:

- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Geometric conservation law and free-stream preservation](/properties/geometric-conservation-law.md)
- [ANSYS Fluent](/software/ansys-fluent.md)
