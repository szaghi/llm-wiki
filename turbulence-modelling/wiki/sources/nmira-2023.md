---
type: Source
title: "Nmira et al. (2023) — Large-eddy simulation of lab-scale ethylene buoyant diffusion flames: Effects of subgrid turbulence/soot production interaction and radiation models"
description: "LES of 15-kW buoyant ethylene fire plumes with a non-adiabatic flamelet library, a two-equation soot model and a presumed bimodal subgrid soot closure; neglecting the soot–mixture-fraction correlation multiplies soot oxidation tenfold, and neglecting subgrid emission turbulence–radiation interaction doubles the soot volume fraction despite 80% resolved temperature variance."
resource: "doi:10.1016/j.proci.2022.07.004"
source_kind: paper
authors: [Nmira F., Bouffard A., Consalvi J.L., Wang Y.]
year: 2023
venue: "Proc. Combust. Inst. 39:3959–3968"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Proceedings_of_the_Combustion_Institute_Nmira_Large-eddy_simulation_of_lab-scale_ethylene_buoyant_diffusio.pdf"
tags: [combustion, soot, turbulence-radiation-interaction, tabulated-chemistry, buoyant-flames]
timestamp: 2026-10-28T07:05:00Z
---

# Summary

Nmira et al. (2023) extend their [LES](/definitions/large-eddy-simulation.md)
presumed filtered-density-function model, earlier validated on
non-sooting flames, to the 15-kW buoyant ethylene diffusion flames
measured at FM Global with oxidizer O$_2$ mole fractions 0.209, 0.168 and
0.152. The subgrid stress uses the dynamic
[Smagorinsky model](/methods/smagorinsky-model.md) and the subgrid scalar
flux a dynamic eddy diffusivity, both from the
[dynamic procedure](/methods/dynamic-procedure.md), as is the constant of
the scalar-dissipation model; no formula or constant is printed.
Thermochemistry comes from a non-adiabatic steady counterflow
[flamelet library](/methods/flamelet-tabulated-chemistry.md) in mixture
fraction, scalar dissipation rate and enthalpy defect, convolved with a
$\beta$ FDF in mixture fraction and delta FDFs in the other two.

Soot follows Lindstedt's two-equation model, and the subgrid
turbulence/soot-production interaction is closed by a presumed bimodal
conditional FDF (sooting and non-sooting modes) in two variants: S1
(intermittency only) and S2, which adds a Heaviside cut confining soot to
the rich side of the mixture fraction where acetylene is consumed.
Radiation uses a rank-correlated full-spectrum $k$-distribution model with
non-grey soot as reference, a WSGG alternative with grey soot, and a
presumed-FDF closure of subgrid emission. The baseline reproduces the
measured temperature, soot volume fraction and intermittency profiles and
the radiant fractions within about 15%. Dropping the soot–mixture-fraction
correlation raises soot oxidation by an order of magnitude and makes soot
radiation negligible; neglecting subgrid emission
turbulence–radiation interaction overpredicts the soot volume fraction by
a factor of about 2, although the grid resolves more than 80% of the
temperature variance; grey soot and WSGG change the radiant fraction
little.

# Version read

Version of record (Elsevier; received 27 December 2021, online 13 July
2022, issue 2023), 10 pages (3959–3968), all read; the equations of
§§2.2–2.3 read visually. Page 1 matches the published metadata; no
identity issue. The supplementary material (soot-model equations and
parameters, grid-independence and temperature-variance figures) is not in
the file, so claims 11 and 12 rest on the text alone. Equation, section
and table numbers are those of this version.

# Key claims

Page-local symbols: $Z$ the mixture fraction, $Z_v=\widetilde{Z^2}-\tilde Z^2$
its subgrid variance; $\chi_Z$ the scalar dissipation rate; $X_{\mathrm R}$ the
enthalpy defect; $X_{\mathrm{O_2}}$ the oxidizer O$_2$ mole fraction;
$N_{\mathrm s}$, $Y_{\mathrm s}$, $f_{\mathrm s}$ the soot number density, mass fraction and volume
fraction (SVF); $\alpha_{\mathrm s}$ the weight of the sooting mode; $Z_{\mathrm s}$ the
mixture fraction where soot is completely burnt; $H$ the Heaviside
function; $\dot Q$, $\dot Q_{\mathrm{em}}$, $\dot Q_{\mathrm{abs}}$ the heat
release rate, emitted and absorbed radiative power; $f_{\mathrm{rad}}$
the radiant fraction; TSI and TRI the subgrid turbulence/soot and
turbulence/radiation interactions.

1. The authors' LES/presumed-FDF model of refs. [15–17], validated for non-sooting flames, is extended to sooting flames (§1, §2.1). **Stated**
2. The subgrid stress uses a dynamic Smagorinsky model, the subgrid scalar flux a dynamic eddy-diffusivity model, and the filtered scalar dissipation rate the model of Jiménez et al. with a dynamically determined constant (§2.1). **Stated**
3. $Z_v$ is computed from its definition with $\widetilde{Z^2}$ transported (§2.1). **Stated**
4. Soot rates factor as $\dot\omega(\phi_g,\phi_s)=\dot\omega_g(\phi_g)\dot\omega_s(\phi_s)$, $\phi_g=\{Z,\chi_Z,X_{\mathrm R}\}$ tabulated, $\phi_s=\{N_{\mathrm s},Y_{\mathrm s}\}$ computed on the fly (§2.2, Eq. 1). **Stated**
5. S2 confines soot to $Z\ge Z_{\mathrm s}$, $Z_{\mathrm s}$ being the lean zero of the gas-phase surface-growth rate (acetylene fully consumed), so that $Z_{\mathrm s}=Z_{\mathrm s}(\chi_{Z,\mathrm{st}},X_{\mathrm R,\mathrm{st}})$ is fixed by the flamelet library (§2.2, Eqs. 5–7, Fig. 1). **Derived**
6. Lindstedt's model parameters are kept from earlier studies in which they predicted SVF within experimental uncertainty for laminar and turbulent C1–C3 flames (§2.2). **Stated**
7. CO and C$_2$H$_4$ radiation is negligible here; the participating species are H$_2$O, CO$_2$ and soot (§2.3). **Stated**
8. Subgrid absorption TRI is neglected, $\overline{\kappa_{a,i}I_i}=\bar\kappa_{a,i}\bar I_i$, following ref. [34] (§2.3). **Stated**
9. The RCFSK model uses 10 Gauss–Legendre points and Planck temperature 1500 K, being total-emission-preserving and weakly dependent on that temperature (§2.3). **Stated**
10. CPU time per time step on 700 cores: 5.34 s (M1), 5.02 (M2), 5.15 (M3), 4.10 (M4), 5.16 (M5) (§3.1, Table 1). **Shown**
11. Domain $3\times3\times1.5$ m$^3$ with $3.6\times10^6$ cells, 2.5 mm cells around the burner and 5 mm vertical spacing up to $z=0.60$ m; grid independence checked on a 1.25 mm mesh (supplementary Fig. 1) (§3.1). **Shown** (in the supplement, not in the file)
12. The grid resolves "on the whole more than 80% of temperature variance" (§3.1, supplementary Fig. 2). **Shown** (in the supplement, not in the file)
13. M1 reproduces "quantitatively" the radial profiles of mean and RMS temperature, mean and RMS SVF and soot intermittency at the three $X_{\mathrm{O_2}}$, except an underpredicted mean temperature and an overpredicted near-axis SVF and intermittency at $X_{\mathrm{O_2}}=0.209$ (§3.2, Figs. 2–4). **Shown**
14. $f_{\mathrm{rad}}=(\dot Q_{\mathrm{em}}-\dot Q_{\mathrm{abs}})/\dot Q$ of M1 is 0.389, 0.255, 0.192 against the measured 0.34, 0.30, 0.22, within about 15% (§3.2, Table 2). **Shown**
15. The soot share of emission is 0.496, 0.370, 0.267: gas and soot contribute similarly in air, gas increasingly dominates as $X_{\mathrm{O_2}}$ decreases (§3.2, Table 2). **Shown**
16. $\dot Q_{\mathrm{abs}}/\dot Q_{\mathrm{em}}$ ranges 0.261–0.322 and grows as $X_{\mathrm{O_2}}$ decreases, gases being more non-grey and less transparent than soot (§3.2, Table 2). **Shown**
17. M2 (S1) severely underpredicts SVF, especially on the flame wings, through an overestimated oxidation rate; the paper cites Kronenburg et al. [29] for the mechanism (soot and oxidizer barely overlap in $Z$ space) (§3.3, Figs. 2–4). **Shown**
18. Evaluated on the same M1 instantaneous fields, mean soot oxidation is an order of magnitude higher with S1 than with S2, the other soot processes little affected (§3.3, Fig. 5). **Shown**
19. With M2 soot radiation becomes negligible, the near-axis temperature rises, and $f_{\mathrm{rad}}$ drops to 0.219, 0.159, 0.138 (§3.3). **Shown**
20. Grey soot (M3) underpredicts $\dot Q_{\mathrm{abs}}$ by 11% but barely changes $f_{\mathrm{rad}}$ and the temperature and SVF statistics, the flames having moderate optical thickness (§3.4, Table 2, Fig. 6). **Shown**
21. WSGG (M4) overestimates gas emission (+13.5%) and absorption (+14.0%), which balance into a slight overprediction of $f_{\mathrm{rad}}$ (0.398 against 0.389) (§3.4, Table 2). **Shown**
22. Neglecting subgrid emission TRI (M5) lowers gas emission by 17.9%, raises the instantaneous gas temperature where soot forms, and overpredicts mean and RMS SVF by a factor of about 2; the larger soot emission (+15.1%) compensates, so $f_{\mathrm{rad}}$ and the temperature statistics change little (§3.4, Table 2, Fig. 6). **Shown**
23. Correct soot prediction is the most critical factor for the thermal field, subgrid emission TRI influences soot production more than the other radiative approximations, and non-grey WSGG with grey soot is an alternative to full-spectrum $k$-distribution models (§4). **Shown**

*(Compiler check, not in the sources: with the printed $\dot Q=15$ kW, $(\dot Q_{\mathrm{em}}-\dot Q_{\mathrm{abs}})/\dot Q$ reproduces every printed $f_{\mathrm{rad}}$ of Table 2 within the rounding of the printed kW values, e.g. $(7.89-2.06)/15=0.389$; the largest difference is M4, $(8.32-2.34)/15=0.3987$ against the printed 0.398.)*

# Printed slips

- §3.1: "Six different modelling approaches were considered"; Table 1 and the text list five (M1–M5).
- Table 1, row M1: "RCSFK" (elsewhere "RCFSK").
- §2.2: "Let us first apply the Bayles theorem".
- §3.1: "A cell size of 2.5 $mm^3$".
- Table 2: the $X_{\mathrm{O_2}}$ column prints 20.9, 16.8, 15.2 in the first block and 0.209 in the second.
- Ref. [24]: page range "200–2013"; refs. [37] and [38] (different journals) both print pages "663–673".
- Typos: "underpediction" (§3.4), "small-sale" (§1), "enthaply" (§2.2).

# Notation map

| Nmira et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tilde\cdot$, $\bar\cdot$ | $\tilde\cdot$, $\bar\cdot$ | Favre filter and LES filter |
| $Z$, $V_Z$ | $Z$, $Z_v$ (page-local, as on the flamelet page) | mixture fraction and subgrid variance |
| $\chi$, $\chi_{st}$ | $\chi_Z$, $\chi_{Z,\mathrm{st}}$ (page-local) | **$\chi$ is the SA ratio $\tilde\nu/\nu$ in the registry** |
| $\chi_R$ | $f_{\mathrm{rad}}$ (page-local) | radiant fraction |
| $X_R$ | $X_{\mathrm R}$ (page-local) | enthalpy defect, not the radiant fraction |
| $\alpha$ | $\alpha_{\mathrm s}$ (page-local) | **$\alpha$ is the DG blending factor in the registry** |
| $\tilde\beta(Z)$ | presumed $\beta$ FDF | **not the field-inversion multiplier $\beta(\boldsymbol x)$** |
| $H$, $H_{int}$ | $H$, $H_{\mathrm{int}}$ | **$H$ is not a length here** |
| $\kappa_i$, $\kappa_\eta$ | $\kappa_{a,i}$, spectral absorption coefficient | **$\kappa$ is the von Kármán constant in the registry** |
| $\eta$ | wavenumber of the radiative spectrum | **$\eta$ is the Kolmogorov length in the registry** |
| $k$ ("$k$-distribution") | absorption-coefficient variable | **not the turbulent kinetic energy** |
| $N_g$, $a_i$, $g$, $T_p$ | page-local | quadrature points or grey gases, weights, cumulative $k$-$g$ distribution, Planck temperature |
| $N_{\mathrm s}$, $Y_{\mathrm s}$, $f_{\mathrm s}$ | page-local | soot number density, mass fraction, volume fraction |
| $\phi_g$, $\phi_s$, $\phi$ | page-local | gas-phase, soot and radiative state vectors |
| $\dot Q_{em}$, $\dot Q_{abs}$, $\dot Q$ | page-local | kW |
| $D$ | burner outer diameter, 15.2 cm | |

# Reference list

38 printed references, numbered (Elsevier style, no titles printed). The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Ref. [24] (Yang, Lew & Mueller, Combust. Flame 209)
is a different work from the bibliography's existing `yang-2019` and is keyed `yang-2019-h`; [24] prints the page range "200–2013" and [38] the pages
of [37], both kept as printed; two Consalvi (2016) works are keyed in
printed order. No printed duplicates and no unparseable items.

# Pages created or updated

Chunk 13 (2026-10-28). This source is cited on:

- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
