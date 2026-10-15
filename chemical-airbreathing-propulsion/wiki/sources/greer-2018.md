---
type: Source
title: "Greer, Paul & Rattner (2018) — Analysis of lithium-combustion power systems for extreme environment spacecraft"
description: "Steady lumped energy-balance and thermal-resistance model of a molten-lithium combustion reactor feeding a sodium thermosiphon and a Stirling or thermoelectric converter, applied to a Venus lander burning in-situ CO2 and a Europa lander carrying SF6, with mass comparisons against batteries and engineering requirements; no experimental validation."
resource: "doi:10.1016/j.actaastro.2018.05.039"
source_kind: paper
authors: [Greer C.J., Paul M.V., Rattner A.S.]
year: 2018
venue: "Acta Astronaut. 151:68–79"
local_file: "/home/stefano/papers/mosaic/chemical-airbreathing-propulsion/2018_Crossref_Acta_Astronautica_Greer_Analysis_of_lithium-combustion_power_systems_for_extreme_env.pdf"
tags: [power-system, metal-combustion, lithium, heat-transfer, stirling, spacecraft, model]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper builds a steady-state, lumped thermodynamic and heat-transfer model
of a lithium-combustion reactor: a liquid lithium bath burns a gaseous
oxidizer at its free surface, and a sodium thermosiphon carries the heat to a
Stirling engine or a thermoelectric generator array. The model couples a
control-volume energy balance (complete, stoichiometric reaction; enthalpies
from EES and JANAF), a thermal-resistance network with a loss path to the
ambient and a delivery path through the thermosiphon, and borrowed closures
(modified-Boussinesq natural convection for the bath, sodium pool boiling,
Churchill–Bernstein external convection). It is applied to a Venus lander
using atmospheric CO₂ as an in-situ oxidizer, re-assessing NASA's "ALIVE"
concept, and to a Europa lander carrying SF₆, then compares system mass
against batteries over mission duration and proposes engineering
requirements. There is no experimental validation; the authors are building
an experimental reactor.

# Key claims

1. **Li–CO₂ mechanism** (§5.1, Eqs. 1–3). 10 Li + 2 CO₂ → 4 Li₂O + Li₂C₂;
   Li₂O + CO₂ → Li₂CO₃; net 10 Li + 6 CO₂ → 4 Li₂CO₃ + Li₂C₂. No Li₂O
   dissociation (only above 2500 K, attributed). 27.5 MJ/kg of lithium;
   39–45 MJ/kg for full conversion to Li₂CO₃ and carbon (attributed).
2. **Flow ratio and heat** (Eqs. 4–6). $\dot m_f=\frac{10.0}{6.0}\cdot
   \frac{6.9}{44.0}\,\dot m_o$; products = oxidizer + fuel; heat of reaction
   from an enthalpy balance.
3. **Li–SF₆** (§6.2, Eq. 20). 8 Li + SF₆ → 6 LiF + Li₂S; 14.1 MJ/kg of
   reactants (§2.2).
4. **Thermal-resistance network** (§5.3, Fig. 7, Eqs. 7–14). Loss path
   (surface, bath, 316 stainless-steel wall, insulation, parallel forced
   convection and radiation) and delivery path (bath, thermosiphon wall,
   boiling sodium); the radiation resistance (Eq. 11) is printed without the
   Stefan–Boltzmann constant.
5. **Bath convection** (§5.4, Eqs. 15–16). Nusselt number 2.9 times the
   modified Boussinesq number to the power 0.096, for 4×10⁴ to 2×10⁹,
   adopted from a fast-reactor sodium-plenum correlation with the heat flux
   replaced by the total reaction heat rate; at 1550 K this gives a Boussinesq
   number of 1.2×10⁵, Nusselt 8.9 and 8800 W m⁻² K⁻¹.
6. **Sodium boiling** (§5.5, Eqs. 17–18). Noyes correlation converted to SI;
   13.2 kW m⁻² K⁻¹ at baseline; condenser resistance neglected.
7. **Stirling efficiency** (§6.1, Eq. 19, attributed). 0.3323 times the
   temperature ratio to the power 0.3655 times the Carnot factor; 16 % at
   1223/740 K, 39 % at 700/190 K (checked by the reader).
8. **Venus ALIVE re-assessment** (§6.1). 5.8 kg/h of CO₂ instead of 6.3 kg/h
   for 14.0 kW thermal; 13.3 kW delivered, 0.7 kW lost (about 5 %); about
   185 kg of lithium for 5 days, 13 % below ALIVE's 200 kg; linear, 50 kg per
   1.36 days.
9. **Venus 1 kW mechanical** (§6.1). 17 kg of lithium per day; 145 kg for 5
   days, 231 kg for 10 days (59 kg hardware); a NaS battery at 300 W h/kg
   needs 400 kg for 5 days; ratios quoted as "1.8" and "2.5 times".
10. **Europa 94 W, 20 days** (§6.2, Fig. 9). 39 % Stirling: 43 kg reactants,
    355 W reaction (113 lost, 242 delivered), 80 kg total, +2.15 kg/day; 25 %
    Stirling: 59 kg, 96 kg, +2.95 kg/day; 8 % TEG: 157 kg, 1300 W (125 lost,
    1175 delivered), 168 kg, +7.85 kg/day; battery 45 kW h in 70 kg
    (643 W h/kg, Li-CFx). Batteries lightest at 20 days; the 39 % Stirling
    lighter beyond 26 days (101 against 105 kg at 30 days).
11. **Europa preheat** (§6.2). 11.8 kg of lithium; melting and heating to
    about 400 °C costs 1.83 kg more (0.50 kg Li, 1.33 kg SF₆).
12. **Requirements** (§6.3). Venus: loss resistance at least about 0.8 K/W,
    delivery resistance at most about 6.0×10⁻³ K/W for under 5 % loss (about
    5 cm of ceramic fibre); surface 1550 K, bath 1300 K. Europa: at least
    about 5.4 K/W and at most about 0.025 K/W for under 10 % loss; at
    0.064 kg/h surface 720 K, bulk 705 K. Tanks: 0.38 m³ of lithium (Venus,
    5 days); 0.023 m³ each of lithium and SF₆ (Europa, 20 days; SF₆ saturated
    at 298 K and 2.4 MPa).
13. **Sensitivities** (§6.4). 20 % of lithium stopping at Li₂O: 34.6 →
    31.3 MJ/kg at 298 K (−10 %); bath convection coefficient halved: 13.3 →
    12.2 kW delivered (−8 %).
14. **Auto-ignition** (§2.1). Li/CO₂ at about 380 °C and 430 kPa "in our first
    experiments"; no data.

# Methods

* **Model.** Steady 0-D lumped analysis in Engineering Equation Solver; no
  CFD, no experiment. Assumptions: steady state, well-mixed bath, complete
  stoichiometric combustion, sinking condensed products (no exhaust, no
  pressure rise), no tank heat loss, negligible condenser resistance. The
  oxidizer flow is the independent variable.
* **Properties.** EES library, NIST-JANAF and cited sources; Appendix A
  tabulates every input and result.
* **Geometry** (Table 2, after the Penn State ARL reactor). Insulation
  0.1654 m × 0.4372 m, 0.0508 m thick (outer diameter 0.216 m); reactor
  0.1146 m × 0.4572 m, 0.0060 m wall; thermosiphon 0.0445 m × 0.3429 m,
  0.0025 m wall.
* **Materials.** 316 stainless steel 28.1 (Venus) and 20.0 (Europa)
  W m⁻¹ K⁻¹; ceramic fibre 0.27 and 0.09 W m⁻¹ K⁻¹; emissivity 0.2 (Venus,
  oxidized aluminium wrap) and 0.15 (Europa); Europa radiator 1 m² with
  emissivity 0.95 sets a 190 K cold side.
* **Environments.** Venus 740 K, 9.2 MPa, 96.5 % CO₂, wind 2 m/s
  (conservative maximum, attributed), Churchill–Bernstein Nusselt about 1100,
  274–275 W m⁻² K⁻¹, 0.012 K/W. Europa: vacuum, radiation only, about 100 K,
  gravity 1.31 m s⁻².

# Tests and results

* **Venus baseline** (§5.3, §6.1, Appendix A), all in K/W: surface–bath
  0.0171; bath–reactor 6.51×10⁻⁴; reactor wall 1.38×10⁻³; insulation 0.806;
  ambient convection 0.012; ambient radiation 0.155; loss total 0.819;
  bath–thermosiphon 2.30×10⁻³; thermosiphon wall 2.01×10⁻³; boiling
  1.8×10⁻³; delivery total 6.08×10⁻³. 13.3 kW out, 0.7 kW lost; insulation
  surface about 750 K; sodium 1223 K; bath surface 1550 K, mean 1300 K, near
  the about 1600 K melting point of stainless steel (Inconel X-750 or a
  refractory liner suggested).
* **ALIVE parameters** (Table 1, attributed): hot 1223 K, cold 773 K,
  Carnot 32 %, Stirling 50 %, loss 665 W, thermal 14 kW, electric 330 W,
  fuel 200 kg.
* **Europa baseline** (Appendix A): radiation 3.04, insulation 2.33, loss
  5.37, delivery 2.51×10⁻² K/W; bath 4.52×10³ and sodium 1.32×10³
  W m⁻² K⁻¹; Nusselt 5.60; Boussinesq 9.44×10²; SF₆ 6.4×10⁻² kg/h, lithium
  2.4×10⁻² kg/h; 242 W to the engine, 148 W rejected, 94 W electric.
* **Figs. 8–9** (heat rates against oxidizer flow at 185 kg; duration
  against mass) read only through values quoted in the text.
* **Reader's checks.** Eq. 4 at 5.8 kg/h gives 1.51 kg/h of lithium, 182 kg
  for 5 days (consistent with 185 kg); Europa reactant masses reproduce from
  14.1 MJ/kg (355 W × 20 days → 43.5 kg; 1300 W → 159 kg).

# Notation map

| Greer et al. (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\dot m_{oxidizer}$, $\dot m_{fuel}$ | $\dot m_o$, $\dot m_f$ | |
| $\dot m_{products}$ | words | |
| $Q_{reaction}$, $Q_{out}$, $Q_{loss}$ | words (heat rates, W) | registry $\dot q$ is volumetric; the paper drops the dot |
| $i$ (specific enthalpy) | words | |
| $h$, $h_{Li}$, $h_{sodium}$ | words (heat-transfer coefficients) | |
| $R$ (K/W) | words (thermal resistance) | |
| $k$ | $\lambda$ | thermal conductivity |
| $\alpha$, $\beta$ | words (diffusivity, expansion coefficient) | |
| $\varepsilon$ (emissivity) | words | **collision** with $\varepsilon$, strain |
| $\eta_{stirling}$, $\eta_{carnot}$ | words | distinct from $\eta_c$ |
| $T_H$, $T_C$ | $T$ with words | |
| $Nu$, $Bo^*$, $Pr$ | words | |
| $L_r$, $g$, $\Delta T_{sat}$ | words | |

# Pages created or updated

Chunk 2 (2026-10-14) created every page of the bundle. This source is cited on:

* [Lithium-combustion power systems](/methods/metal-combustion-power-system.md)

# Citations

1. `/home/stefano/papers/mosaic/chemical-airbreathing-propulsion/2018_Crossref_Acta_Astronautica_Greer_Analysis_of_lithium-combustion_power_systems_for_extreme_env.pdf`.
   * **Version.** Publisher's typeset version (Elsevier), 12 pages. Funding
     NASA NIAC NNX15AQ30G.
   * **Identity.** doi:10.1016/j.actaastro.2018.05.039, printed on page 1 and
     checked on Crossref: title, authors, vol. 151, pp. 68–79 match; issue
     2018-10; Crossref has no online date, page 1 gives 21 May 2018
     (received 23 Feb 2018, revised 9 May 2018, accepted 18 May 2018). Page 1
     matches the filename title. First filed in the plasma-propulsion
     archive.
   * **How it was read.** Full text; all equations read cleanly from rendered
     pages 5–7; Figs. 8–9 not digitised.
   * **Recorded as printed.**
     * Surface-to-bath resistance 0.017 K/W in §5.3 and Appendix A
       (1.71×10⁻²), "0.17 K W⁻¹" in the delivery-path paragraph.
     * The text says all resistances were "summed in series", but neither
       total includes the surface-to-bath resistance; Fig. 7 draws it as a
       branch, consistent with Eqs. 12–13.
     * Characteristic length printed as 0.63 m (reactor minus thermosiphon
       diameter), against 0.070 m from Table 2; the reported coefficient
       implies about 0.063 m, a factor-10 slip.
     * The modified Boussinesq number, with a total heat rate in place of a
       heat flux, is not dimensionless, and 1.2×10⁵ does not reproduce from
       the printed inputs (reader's check); the 0.096 exponent keeps the
       downstream effect small.
     * Battery-to-Stirling mass ratios "1.75–2.5 times" (abstract) and
       "1.8–2.5 times" (§6.1, §7); the printed masses give total-mass ratios
       of 2.76 (5 days) and 3.46 (10 days), so the quoted figures are excess
       mass.
     * 27.5 MJ/kg (§5.1, §6.1, abstract) against 34.6 MJ/kg for the same
       assumption at 298 K (§6.4), not reconciled; 1.51 kg/h × 27.5 MJ/kg is
       11.5 kW, not the stated 14.0 kW (34.6 MJ/kg gives 14.5 kW).
     * Venus cooling capacity "2 kW" (§4) and "358 W" (§6.1), both
       attributed to ALIVE.
     * Table 1 Carnot efficiency 32 % against 1 − 773/1223 = 36.8 %.
     * Appendix A labels the boiling resistance "R_thermosiphon,conduction".
     * Auto-ignition about 380 °C (Li/CO₂, §2.1) and about 400 °C (Li/SF₆,
       §6.2) concern different oxidizers.
     * Stated conflict with ALIVE: 5.8 against 6.3 kg/h and 185 against
       200 kg, attributed to a different heat of reaction.
   * **Reference list.** 49 printed entries (Crossref reference-count 49).
