---
type: Source
title: "García-Garrido, Pudsey & Mundt (2018) — Numerical simulations of radiative heat effects in a plasma wind-tunnel flow under Mars entry conditions"
description: "Simulates the supersonic CO2 jet of the HELM arc-heated plasma wind tunnel at 2.1 MJ/kg with two-temperature Navier–Stokes codes (NSMB, US3D) and a P1 radiation solver fed by a compact full-spectrum k-distribution database, matches TALIF temperatures to 10–100 K in the jet core, and finds radiation a minor effect (centreline cooling at most about 1.5%) in this optically thin gas."
resource: "doi:10.1016/j.actaastro.2018.06.011"
source_kind: paper
authors: [García-Garrido J., Pudsey A.S., Mundt C.]
year: 2018
venue: "Acta Astronaut. 151:334–341"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_García-Garrido_Numerical_simulations_of_radiative_heat_effects_in_a_plasma.pdf"
tags: [arc-heater, plasma-wind-tunnel, radiation, k-distribution, thermochemical-nonequilibrium, mars-entry, cfd]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper simulates the supersonic CO₂ jet of the arc-heated plasma wind
tunnel of the High Enthalpy Laboratory Munich (HELM) at one low-enthalpy
operating point: stagnation enthalpy 2.1 MJ/kg, 2 g/s, 20 kW, nozzle-inlet
stagnation 90 kPa and 2000 K. The density-based Navier–Stokes code NSMB is
run with two-temperature thermochemical non-equilibrium and Spalart–Allmaras
turbulence, and the flow is cross-checked against the US3D code and against
two-photon LIF (TALIF) temperature measurements at 2 mm and 22 mm
downstream of the nozzle exit. Radiation is coupled through a P1 solver
with a full-spectrum k-distribution (FSK) spectral model, whose
k-distributions are pre-computed with PARADE into a compact look-up
database parameterised by the two temperatures and the species
concentration, the Planck weighting being evaluated at the
vibrational-electronic temperature. NSMB and US3D agree to about 1.5% in
jet-core velocity and differ in shear-layer thickness; both agree with the
measured core temperatures to 10–50 K at 2 mm and 25–100 K at 22 mm.
Radiation lowers the centreline temperature by at most about 1.5% and
raises it in the inner mixing layer (maximum local difference about 3%);
the gas is optically thin, so radiation is a minor energy-transfer
mechanism at this condition. The arc heater is not modelled: the nozzle
supply is an equilibrium neutral gas, and no plasma is simulated.

# Key claims

1. **FSK reformulation** (§1.3.1, Eqs. 1–3). The spectral absorption
   coefficient is reordered into a monotonic function of an artificial
   variable in [0, 1], the Planck-weighted cumulative k-distribution
   (Eq. 2), and the radiative transfer equation without scattering (Eq. 1)
   becomes a transfer equation in that variable (Eq. 3). That FSK is exact
   for homogeneous media is stated, not proved.
2. **Planck weighting at the vibrational temperature** (§2, Fig. 5, Eq. 4).
   PARADE spectra at different excitation levels show that the
   vibrational-electronic temperature dominates the spectral curve, so the
   Planck function in the FSK definition is evaluated at it. Shown only
   qualitatively by Fig. 5.
3. **Compact FSK databases** (§1.3.2, §§2.1–2.2). For each participating
   species a three-component thermodynamic state (two temperatures and a
   concentration) points to a k-curve on a Chebyshev–Gauss quadrature in
   the cumulative variable; out-of-range states are extrapolated from the
   limit values; species are combined with literature mixing models
   (Ref. [20]), since exact mixing of k-distributions is impossible. Which
   mixing model produced the results is not stated.
4. **P1 coupling** (§3, Eqs. 5–7). Per quadrature point, a P1 equation for
   the incident radiation; the energy equation receives the divergence of
   the radiative flux as the sum over quadrature points of emission minus
   absorption. Eq. 5 writes the diffusion term with the absorption
   coefficient outside the Laplacian, i.e. locally constant (implicit, not
   stated).
5. **Code-to-code** (§3.1, Figs. 9–11; turbulent runs, same grid).
   Jet-core axial velocity differs by about 1.5%; NSMB gives a thicker
   nozzle boundary layer and a much thicker shear layer at 2 mm, the
   difference shrinking at 22 mm; CO₂ mass fractions differ by at most
   about 0.25%. Shown.
6. **Code-to-experiment** (§3.2, Fig. 13, TALIF from Refs. [15, 16]). Core
   temperature differences 10–50 K at 2 mm and 25–100 K at 22 mm, both
   codes over-predicting at 22 mm; NSMB mixes slightly better in the shear
   layer; both codes beat the CFD++ estimate of Ref. [16] in the core,
   while that estimate (other turbulence models) did better in the shear
   layer; measurements are hotter than both simulations outside the shear
   layer. Shown.
7. **Thermal equilibrium on the axis** (§4, Fig. 14). Along the centreline
   the translational and vibrational temperatures coincide (equilibrium
   favoured by high pressure and density despite the high enthalpy),
   falling from about 2000 K to about 1000 K, with a shock 0.035 m
   downstream of the nozzle exit. Shown.
8. **Radiation is minor** (§4, Figs. 15–16, §5; participating species CO₂,
   CO, O₂, O; 100–10 000 nm; wall emissivity 1). Centreline temperature
   drop at most about 1.5%; inner mixing-layer increase, maximum local
   difference about 3%; Planck-mean absorption coefficient 0.1–0.2 m⁻¹ on
   the centreline, falling by up to three orders of magnitude across the
   shear layer; the gas is optically thin. The radiation case lies closer
   to the 22 mm measurements in the core. Shown.

# Methods

* **Facility:** HELM arc-heated plasma wind tunnel with a Y-shaped plasma
  torch (Fig. 2), enthalpy up to about 20 MJ/kg, arc-region stagnation
  temperature of order 6000 K (§1.2); CO₂ operating envelope in Fig. 8.
  Simulated point: 2 g/s, 20 kW electric power, about 2 MJ/kg, about
  0.09 MPa.
* **Geometry and grid:** simplified nozzle and test chamber (Fig. 6),
  quarter model with two symmetry planes, multi-block structured 3-D grids
  (ANSYS ICEM CFD), first-cell $y^+\approx1$; three grids compared in cold
  flow without chemistry (Fig. 7), refined until the shock–jet structure
  was captured. Cell counts and a quantitative grid error are not printed.
* **Boundary conditions:** isothermal 300 K no-slip walls; far-field
  Riemann invariants on the outflow surfaces; nozzle supply from
  measurements, composition by NASA CEA (Ref. [22]) assuming a homogeneous
  equilibrium gas in the stagnation chamber (Table 1: 90 kPa, 2000 K,
  mass fractions CO₂ 0.98772, CO 0.00781, O₂ 0.00447; test section
  1.10 kPa, 300 K, pure CO₂).
* **NSMB:** steady implicit scheme, second order in space; 9 species (CO₂,
  CO, C, O₂, O, N₂, N, NO, CN) and 61 reactions (Park et al. 1994);
  two-temperature model; laminar and turbulent runs, Spalart–Allmaras with
  a compressibility correction.
* **US3D** (University of Minnesota): same grid; 8 species (no CN) and 41
  reactions (Johnston et al. 2012); the chemistry is the only stated
  difference.
* **Radiation:** FSK database pre-computed with PARADE (four excitation
  modes; bound–bound, bound–free, free–free), P1 solver inside NSMB. The
  number of quadrature points and the solver discretisation are not
  printed.
* **Experiment** (reported from Refs. [15, 16]): TALIF temperature profiles
  at 2 mm and 22 mm.

# Tests and results

| Test | Figure | Result |
|---|---|---|
| Grid study (cold flow) | 7 | axial velocity at 2 and 22 mm on three grids; no quantitative error |
| NSMB vs US3D | 9–11 | core velocity within ≈1.5% (contours 1200–1700 m/s); CO₂ mass fraction within ≈0.25%; NSMB higher plume velocities, US3D slightly higher in the diverging nozzle |
| Temperature fields | 12 | shocks at the same positions, different jump magnitudes |
| Codes vs TALIF | 13 | core: 10–50 K (2 mm), 25–100 K (22 mm) |
| Centreline temperatures | 14 | translational ≈ vibrational; ≈2000 → ≈1000 K; shock at 0.035 m |
| Radiation on/off | 15 | centreline drop ≤ ≈1.5%; maximum local difference ≈3% |
| Axis spectrum at 2 mm | 16 | emission and absorption, 10³–10⁵ Å |

Figure values are approximate plot readings by the reader.

# Notation map

The radiative-transfer symbols have no registry counterpart and several
collide with registry symbols; they are kept in words.

| García-Garrido et al. (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $T$ | words (translational–rotational temperature, K) | registry $T_s$ is a species temperature, usually in eV |
| $T_{vib}$ | words (vibrational–electronic temperature, K) | |
| $I$, $I_\lambda$, $I_b$, $I_{b\lambda}$ | words (radiative intensity, spectral, blackbody) | not $I_d$, $I_b$ (ion beam current) or $I_{sp}$: **collision** of $I_b$ |
| $\kappa_\lambda$ / $k_\lambda$, $k_g$, $k_i$ | words (spectral and reordered absorption coefficients) | **collision:** registry $k$ is a wavenumber |
| $g$ | words (cumulative k-distribution variable) | **collision:** registry $g$ is a relative collision speed |
| $G$, $G_i$ | words (incident radiation) | |
| $\varepsilon_\lambda$, $\varepsilon_g$ | words (emission coefficient) | **collision risk** with $\varepsilon_0$ |
| $\lambda$ | words (radiation wavelength) | registry wavelength is $\lambda_w$ |
| $\Omega$ | words (solid angle) | **collision** with Hall parameter $\Omega_e$ |
| $\vec q$ | words (radiative heat flux) | not the species heat flux $\mathbf q_s$ |
| $s$ | words (path coordinate) | **collision:** registry $s$ is the species index |
| $\dot m$ | $\dot m$ | mass flow rate |
| $y^+$ | words | |

# Pages created or updated

No concept page cites this source yet. It was ingested in full (bundle law, chunk 3), but none of its contributions earns a concept page under the granularity rule: the radiation and wind-tunnel models have no second source and touch no thruster page, since the arc heater shared with arcjets is not modelled (the nozzle supply is an equilibrium neutral gas).

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_García-Garrido_Numerical_simulations_of_radiative_heat_effects_in_a_plasma.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier), 8 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.011, printed on page 1
     and checked on Crossref: title, authors, Acta Astronaut. 151:334–341
     match; issue October 2018 (no published-online field on Crossref);
     page 1 gives received 7 Feb 2018, revised 16 May 2018, accepted 3 Jun
     2018, online 7 Jun 2018. Page 1 matches the filename title.
   * **How it was read.** Full text layer, clean; equations and figures
     checked on rendered pages 2–7, none illegible. Figure values are
     approximate readings.
   * **Recorded as printed.**
     * Eqs. 2 and 4 print the integrand of the k-distribution as the Planck
       function times $(k-\kappa_\lambda)$; the standard FSK definition
       (Modest, Ref. [17]; Wang et al., Ref. [18]) has a Dirac delta
       $\delta(k-\kappa_\lambda)$. Checked on the rendered page; a
       typesetting slip that makes the printed definition wrong.
     * The nomenclature lists $G$ as "Artificial Wavelength [−]", but $G$ in
       Eqs. 5–7 is the incident radiation (the artificial variable is the
       lowercase $g$); it lists $Q$ "Radiative Heat Flux" in W/m³, the unit
       of its divergence; Eq. 1 writes $k_\lambda$ where the nomenclature
       defines $\kappa_\lambda$.
     * The abstract gives ambient pressures of 600–1000 Pa; Table 1 gives a
       test-section pressure of 1.10 kPa.
     * §1.1 describes Mars air as 97% CO₂ and 3% N₂, but the simulated test
       gas is pure CO₂ (Table 1), while the 9-species model carries
       nitrogen species.
     * The conclusions say "measurements deviate from the experiments at
       the shear layer", evidently meaning simulations deviate from
       measurements.
     * §4 is presented as an analysis "under the measured conditions" while
       assuming chemical equilibrium at the nozzle supply, which §5 itself
       calls "very restrictive".
     * The 1.5% (centreline decrease) and 3% (maximum local difference) of
       §4 are consistent only if the 3% is the mixing-layer increase, the
       reading the conclusions support.
   * **Reference list.** 30 printed entries ([1]–[30]), matching the
     Crossref reference count. Two printed duplicates: refs. [9] and [29]
     are the same work (Johnston, Brandis & Sutton, AIAA 2012-2866), and
     refs. [10] and [23] are the same work (Park et al. 1994, J.
     Thermophys. Heat Transf. 8(1)).
