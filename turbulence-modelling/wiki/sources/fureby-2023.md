---
type: Source
title: "Fureby & Nilsson (2023) — Large Eddy Simulation of cavity stabilized ramjet combustion"
description: "Finite-rate-chemistry LES (LDKM subgrid model, PaSR combustion closure, OpenFOAM density-based solver) of the Michigan dual-mode ramjet with a cavity flameholder: the chemical mechanism decides the predicted flame-stabilisation mode, and intermediate stagnation temperature gives mode switching coupled with the isolator shock train."
resource: "doi:10.1016/j.ast.2023.108503"
source_kind: paper
authors: [Fureby C., Nilsson T.]
year: 2023
venue: "Aerosp. Sci. Technol. 141:108503"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Aerospace_Science_and_Technology_Fureby_Large_Eddy_Simulation_of_cavity_stabilized_ramjet_combustion.pdf"
tags: [les, combustion, compressible, sgs-model, shock-boundary-layer-interaction]
timestamp: 2026-10-28T07:09:00Z
---

# Summary

Fureby & Nilsson (2023) apply finite-rate-chemistry
[LES](/definitions/large-eddy-simulation.md) to the University of
Michigan dual-mode ramjet combustor (Micka & Driscoll): hydrogen injected
sonically from a wall port upstream of a rectangular cavity, isolator
entrance Mach 2.2, air stagnation temperatures from 1080 to 1370 K
(cases A–E). The experiments show cavity-stabilised combustion at low
stagnation temperature, jet-wake-stabilised combustion at high, and
oscillation between them in between. The turbulence closures are fixed,
cited choices: the Favre-filtered equations closed by the localised
dynamic $k$-equation model, a
[one-equation subgrid kinetic-energy model](/methods/subgrid-kinetic-energy-equation-model.md)
whose coefficients come dynamically from scale similarity (preferred to
the [Smagorinsky](/methods/smagorinsky-model.md), [WALE](/methods/wale-model.md)
and hyperviscosity models on the strength of the authors' earlier study),
gradient-diffusion subgrid fluxes, the partially stirred reactor (PaSR)
combustion model, and a no-slip subgrid wall model
([wall-modelled LES](/methods/wall-modelled-les.md)), solved with a
density-based [OpenFOAM](/software/openfoam.md) solver (second-order
Kurganov flux, operator splitting, Rosenbrock chemistry). Flamelet models
([tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)) are
rejected because the flame is fragmented and flow and chemical time
scales are similar; the [thickened flame model](/methods/thickened-flame-model.md)
and [artificial diffusivity](/methods/artificial-viscosity-shock-capturing.md)
are listed as alternatives, not used.

Three hydrogen–air mechanisms are compared: only the authors' Z22
reproduces both stabilisation modes. A grid study gives 90%, 94% and 96%
resolved turbulent kinetic energy on 7.3, 24.6 and 57.8 million cells
([grid requirements](/results/les-grid-point-requirements.md)). For the
intermediate case a ~60 Hz switching between a high- and a low-intensity
mode, with ~800 Hz flame excursions, couples with the motion of the
isolator shock train ([shock–boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).
POD with FFT, an extended Takeno flame index (premixed-dominated at low,
non-premixed at high stagnation temperature), wall pressure against
experiment and one-dimensional efficiency and thrust metrics complete the
analysis. The combustion and propulsion results stay on this page.

# Version read

Version of record (Elsevier, open access CC BY; received 29 April 2023,
accepted 4 July 2023, online 13 July 2023), 16 pages, all read; equation
pages 3–4 and pages 5, 8, 11–14 read visually. Page 1 matches the
metadata; no identity issue. Equation, figure and table numbers are those
of this version.

# Key claims

Symbols: $T_0$ the air stagnation temperature (cases A–E: 1080, 1130,
1240, 1300, 1370 K), $Sc_t$ the turbulent Schmidt number,
$\tau_\Delta=\Delta/u'_\Delta$ the subgrid shear time and $\delta_u$ the
laminar flame thickness (page-local); $c_k$ and $c_\varepsilon$ the
coefficients of the $k$-equation model, $\gamma^*_{\mathrm{PaSR}}$ the PaSR
reacting volume fraction, $\tau_{\mathrm{ch}}$ and $\tau_{\mathrm{mix}}$ chemical
and mixing time scales, $u'_\Delta$ a subgrid velocity scale and
$s_{\mathrm L}$ the laminar flame speed (registry §11).

1. With Z22, LES gives cavity-stabilised combustion anchored at the cavity leading edge for case A (1080 K), jet-wake-stabilised combustion for case E (1370 K), and oscillation between the modes for case C (1240 K) (Abstract, §6.3–6.4, Figs. 2a, 5–7). **Shown**
2. The mechanism decides the predicted mode: for case A, D7 gives jet-wake stabilisation, J20 "virtually no combustion", Z22 cavity stabilisation; for case E all three give jet-wake stabilisation (§6.1, Fig. 4). **Shown**
3. D7 underpredicts and J20 overpredicts the ignition delay at low temperature; only Z22 reproduces it below 900 K (§4, §6.1, Fig. 1a). **Shown** (0-D and 1-D comparisons)
4. M1 overpredicts laminar flame speed and extinction strain rate; ES7, BG7 and D7 underpredict both; J20, K30, USCII and Z22 agree with experiments (§4, Fig. 1b–c). **Shown**
5. Grid study (case A): the three grids give similar mean and rms fields and 90%, 94%, 96% resolved turbulent kinetic energy, "rendering all grids appropriate for LES according to [75] as well as with the more stringent requirements of [76]" (§6.2). **Shown** (thresholds not stated)
6. The subgrid model "performs better than many other subgrid models with respect to turbulent boundary layers, mixing and shock-boundary layer interactions", from the authors' earlier high-speed studies [39] (§3.2). **Stated**
7. The $k$-equation model with PaSR is "a reliable combination, capable of matching the more advanced and expensive models" [53] (§6). **Stated**
8. Finite-rate chemistry is chosen over flamelet models because the flame is fragmented and flow and chemical time scales are similar (§3.3). **Stated**
9. Case C oscillates at about 60 Hz between a high-intensity mode resembling jet-wake stabilisation (about two thirds of the time) and a low-intensity near-extinction mode resembling cavity stabilisation, with about 800 Hz flame excursions in the high-intensity mode, both coupled with the isolator shock train (§6.4, Figs. 7, 9). **Shown**
10. In case C the high-intensity mode lasts about 10 ms while the shock train retreats almost to the isolator entrance; combustion above the cavity then stops and restarts after about 5 ms (§6.4). **Shown**
11. The switching is hypothesised to be a two-way coupling of the isolator pressure jump and the flame through reflected pressure waves; the "driving mechanism … not fully understood" (§6.4, Fig. 10). **Stated** (hypothesis)
12. In case A self-ignition occurs in the cavity shear layer heated from beneath by entrained products; "contrary to what is postulated based on experimental results, [14], virtually no radicals (H, O, OH, HO2, H2O2) are spotted between the fuel injector and the high temperature regions" (§6.3, Fig. 6). **Shown**
13. POD and FFT (Table 2): case A is dominated by a 164 Hz weak longitudinal pressure fluctuation, case C by a 67 Hz strong one, case E by a 196 Hz weak one with high-frequency combustion fluctuations along the plume (§6.5). **Shown**
14. These frequencies are mostly below the Rossiter frequencies (about 2400 Hz), "thereby excluding cavity resonance as a key mechanism" (§6.5). **Stated** (Rossiter estimate not shown)
15. Phase portraits of the two lowest POD coefficients rank the unsteadiness C, A, E; "In all cases the Lyapunov exponent is positive" (§6.5, Fig. 11g–i). **Stated** (no Lyapunov computation shown)
16. Extended Takeno index: case A is dominated by lean premixed combustion, case E by non-premixed combustion with rich premixed burning in the plume core; case C is intermediate (§6.6, Fig. 12). **Shown**
17. Mean and rms wall pressure agree well with experiment for cases A, C, E; case C is least steady, rms highest in the isolator (§6.7, Fig. 13). **Shown**
18. Variances of the 1-D heat release, Mach number, efficiency and stream thrust are a few percent of the mean for cases A and E, up to 20% for case C (§6.7, Fig. 14). **Shown**
19. The 1-D Mach number is about 2 in the nozzle, about 0.5 in the downstream isolator and cavity and about 1.7 at the outlet: all cases run in ramjet mode (§6.7, Fig. 14d–f). **Shown**
20. Combustion efficiency approaches one downstream and is higher for cases A and E than for case C (§6.7). **Shown**
21. The mixture burns as an auto-ignition-assisted premixed flame in the cavity-stabilised case ($T_0\lesssim1100$ K) and as a diffusion flame in the jet-wake case ($T_0\gtrsim1300$ K) (§7). **Shown**
22. Extending subgrid models from incompressible to compressible reacting flows by dimensional arguments "can be disputed but in the absence of better alternatives this constitutes today's standards" (§3.2). **Stated**

The subgrid closure (§3.2), in registry notation:
$\bar\rho\tau_{ij}\approx\tfrac23\bar\rho k_{\mathrm{sgs}}\delta_{ij}-2\mu_t\tilde S^d_{ij}$,
$\mu_t=c_k\bar\rho\Delta\sqrt{k_{\mathrm{sgs}}}$,
$\partial_t(\bar\rho k_{\mathrm{sgs}})+\nabla\cdot(\bar\rho k_{\mathrm{sgs}}\tilde{\boldsymbol u})=-\bar\rho\tau_{ij}\tilde S_{ij}+\nabla\cdot(\mu_t\nabla k_{\mathrm{sgs}})-c_\varepsilon\bar\rho k_{\mathrm{sgs}}^{3/2}/\Delta$,
with $c_k$, $c_\varepsilon$ "dynamically evaluated from scale similarity"
(no values printed), $Pr_t\approx0.7$, $Sc_t\approx0.85$. The PaSR
filtered rate multiplies the forward and backward rates at the filtered
state by $\gamma^*_{\mathrm{PaSR}}=\tau_{\mathrm{ch}}/(\tau_{\mathrm{mix}}+\tau_{\mathrm{ch}})$, with
$\tau_{\mathrm{ch}}\approx\delta_u/s_{\mathrm L}$ and $\tau_{\mathrm{mix}}\approx\sqrt{\tau_\eta\tau_\Delta}$
(Eq. 4).

# Printed slips

- **Table 1:** the inflow density and velocity of case C (1.19, 598) nearly repeat case A's (1.19, 599), and case D's (1.14, 612) case B's (1.14, 613), while the inflow temperature rises from 916 to 1052 K and from 958 to 1103 K.
- **§3.3:** $\tau_m\approx\sqrt{\tau_K\tau_\Delta}$ is called the "harmonic mean"; the printed formula is the geometric mean.
- **Subgrid fluxes (§3.2):** $\boldsymbol b_E=(\mu/\mathrm{Pr_t})\nabla\tilde E$ and $\boldsymbol b_i=(\mu/Sc_t)\nabla\tilde Y_i$ are printed with $\mu$, not the subgrid viscosity $\mu_k$.
- **Fig. 1 caption:** "(a) laminar flame speed, (b) ignition delay time"; panel (a) plots the ignition delay and (b) the flame speed, as the text of §4 says. The legends show "B12" and "USC2", the text K30 and USCII.
- **POD case labels (§6.5):** snapshots are of cases A, C and E, but "Figs. 11a to 11c present the first five POD modes … for cases A, B and C" (also the caption), and Table 2 rows read "Case A, Case B, Case E", the text attributing the row-B frequencies to case C; row B also lists 365 and 730 Hz, not mentioned in the text.
- **§6.7:** "The most noteworthy feature of Fig. 13 is that the variances …" refers to Fig. 14; "panels 15a-15c" (there is no Fig. 15); "cases A and D", "cases B and D" where the cases shown are A, C, E; Fig. 14 caption "(h)-(i) combustion efficiency" for (g)–(i).
- **Fig. 2a legend** "Present LES set B" against the text's "green stars".
- **§7:** "stagnation temperatures from $T_0=1080$ K to 1500 K", Table 1 ending at 1370 K; jet-wake stabilisation for "$T_0\gtrsim1350$ K" (experiment, §7) and "$T_0\gtrsim1300$ K" (§6.3, §7).
- **Eq. (3):** brace labels $\Omega_{f,i}$, $\Omega_{b,i}$ against the text's $\Omega_{f,j}$, $\Omega_{b,j}$; text "$\tilde k_{f,i}$" against the equation's $\tilde k_{f,j}$.
- **Eq. (6):** viscous term printed "$\nabla\boldsymbol v^T-\frac23tr(\boldsymbol D\boldsymbol I)$".
- Line references "(1$_1$)" to "(8$_3$)"; §2 "Ben-Yakar & Hansen" against the reference's "R.K. Hanson".
- Reference-list spellings: [35] "G. Erlebasher, M. Hussaini, C. Special, T. Sang", [59] "A. Kurgaonov", [78] "L. Sirowich"; [55] pages "319.–321.".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tilde{(\cdot)}$, $\overline{(\cdot)}$, $\Delta$ | $\tilde{(\cdot)}$, $\bar{(\cdot)}$, $\Delta$ | Favre and unweighted filter; $\Delta$ not defined further |
| $\boldsymbol v$ | $u_i$ | |
| $\boldsymbol B=\bar\rho(\widetilde{\boldsymbol v\otimes\boldsymbol v}-\tilde{\boldsymbol v}\otimes\tilde{\boldsymbol v})$ | $\bar\rho\tau_{ij}$ | full stress, positive trace |
| $\boldsymbol D$, $\boldsymbol D_D$ | $S_{ij}$, $S^d_{ij}$ | |
| $\boldsymbol S\approx2\mu\boldsymbol D_D$ | $\sigma_{ij}$ | **collision:** the source's $\boldsymbol S$ is the viscous stress |
| $k$ | $k_{\mathrm{sgs}}$ | also an index in Eqs. 2–4 |
| $\mu_k$ | $\mu_t$ | subgrid viscosity |
| $c_k$, $c_\varepsilon$ | $c_k$, $c_\varepsilon$ (registry §11) | as on the [one-equation model page](/methods/subgrid-kinetic-energy-equation-model.md); not the DES length-scale factor $C_k$ |
| $\mathrm{Pr_t}$, $Sc_t$ | $Pr_t$, $Sc_t$ | |
| $\boldsymbol b_i$, $\boldsymbol b_E$ | (subgrid species and energy fluxes) | |
| $E$ | (total sensible energy per unit mass, page-local) | not the registry's $E$ per unit volume |
| $\kappa$ | (thermal conductivity, page-local) | **collision** with the von Kármán constant |
| $\gamma^*$ | $\gamma^*_{\mathrm{PaSR}}$ (registry §11) | **collision** with $\gamma$ |
| $\tau_c$, $\tau_m$ | $\tau_{\mathrm{ch}}$, $\tau_{\mathrm{mix}}$ (registry §11) | chemical and mixing time scales |
| $\tau_K$, $\tau_\Delta=\Delta/v'$ | $\tau_\eta$, $\tau_\Delta=\Delta/u'_\Delta$ | $u'_\Delta$ registry §11, $\tau_\Delta$ page-local; $v$ is the registry's wall-normal velocity |
| $\delta_u$, $s_u$ | $\delta_u$ (page-local), $s_{\mathrm L}$ (registry §11) | laminar flame thickness and speed; $s_{\mathrm L}$ is not the Lundquist number $S_L$ |
| $\lambda_2$ | (vortex criterion, page-local) | **collision** with the Taylor microscale |
| $T_0$, $p_0$ | (stagnation values) | $T_0$ is also the reference temperature of $E$ |
| $\zeta$, $\zeta_M$, $z$, $z_{st}$ | $\zeta$, $\zeta_M$, $Z$, $Z_{\mathrm{st}}$ (page-local) | Takeno indices; mixture fraction and its stoichiometric value, as on [flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md) |
| $\psi_i^\varphi$, $a_i^\varphi$ | (POD modes and coefficients) | |
| $Q$ | (heat-release rate) | |

# Reference list

80 printed references, numbered style. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug; [2] is an
undated web page; same-author same-year works (Micka 2008, 2009) are
keyed in printed order; misspelt names are recorded as printed. Ref [21]
(H.B. Wang et al., Int. J. Hydrog. Energy 38, 2013) is another work than
the ingested [wang-2013](/sources/wang-2013.md) and is keyed `wang-2013-k`. No
item is unparseable.

# Pages created or updated

Chunk 11 (2026-10-27). This source is cited on:

- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [One-equation subgrid kinetic-energy models](/methods/subgrid-kinetic-energy-equation-model.md)
- [Thickened flame model](/methods/thickened-flame-model.md)
- [WALE model](/methods/wale-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [OpenFOAM](/software/openfoam.md)
