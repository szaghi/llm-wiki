---
type: Source
title: "Greer, Paul & Rattner (2018) — Analysis of lithium-combustion power systems for extreme environment spacecraft"
description: "A steady lumped thermodynamic and thermal-resistance model of a liquid-lithium combustion reactor feeding a sodium thermosiphon and a Stirling engine or thermoelectric generator re-assesses the Venus ALIVE concept with atmospheric CO2, sizes a Europa lander burning SF6, compares system mass with batteries over mission duration, and proposes engineering requirements; there is no experimental validation."
resource: "doi:10.1016/j.actaastro.2018.05.039"
source_kind: paper
authors: [Greer C.J., Paul M.V., Rattner A.S.]
year: 2018
venue: "Acta Astronaut. 151:68–79"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Greer_Analysis_of_lithium-combustion_power_systems_for_extreme_env.pdf"
tags: [context, power-system, metal-combustion, lithium, heat-transfer, venus, europa]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper builds a steady, lumped thermodynamic and heat-transfer model of
a lithium-combustion reactor: a liquid Li bath burns a gaseous oxidizer at
its free surface, and a sodium thermosiphon carries the heat to a Stirling
engine or a thermoelectric generator (TEG) array. The model couples a
control-volume energy balance (complete stoichiometric reaction, enthalpies
from EES and JANAF), a thermal-resistance network with a loss path to the
ambient and a delivery path through the thermosiphon, and borrowed
closures: a modified-Boussinesq natural-convection correlation for the Li
bath, a sodium pool-boiling correlation and Churchill–Bernstein for
external convection. It is applied to a Venus lander using atmospheric CO2
as in-situ oxidizer, re-assessing the NASA COMPASS "ALIVE" concept, and to a
Europa lander carrying SF6. The paper compares system mass with batteries
over mission duration and proposes engineering requirements (resistance
bounds, operating temperatures, tank volumes). There is no experimental
validation; an experimental reactor is under construction.

# Key claims

1. **Li–CO2 mechanism** (§5.1, Eqs. 1–3). 10 Li + 2 CO2 → 4 Li2O + Li2C2,
   then Li2O + CO2 → Li2CO3, net 10 Li + 6 CO2 → 4 Li2CO3 + Li2C2; Li2O
   assumed not to dissociate (only above 2500 K, while neither the cited
   experiment nor the model exceeds 1600 K). Yield 27.5 MJ per kg Li; a
   well-mixed reactor producing only Li2CO3 and C could reach 39–45 MJ per
   kg Li (attributed).
2. **Mass and energy balance** (Eqs. 4–6). Fuel flow is (10/6)(6.9/44.0)
   times the oxidizer flow; product flow is their sum; the heat of reaction
   is the enthalpy-flux difference between reactants and products.
3. **Li–SF6 reaction** (§6.2, Eq. 20). 8 Li + SF6 → 6 LiF + Li2S, complete
   and stoichiometric; 14.1 MJ per kg reactants (§2.2).
4. **Thermal-resistance network** (§5.3, Fig. 7, Eqs. 7–14). Loss path:
   surface, bath, 316 stainless wall, insulation, then forced convection in
   parallel with radiation to the ambient. Delivery path: bath,
   thermosiphon wall, boiling sodium. The heat of reaction equals loss plus
   delivered heat. Eq. 11 (radiative resistance) is printed without the
   Stefan–Boltzmann constant.
5. **Li-bath natural convection** (§5.4, Eqs. 15–16). Nusselt number
   $=2.9$ times the modified Boussinesq number to the power 0.096 (valid
   4 × 10⁴ to 2 × 10⁹), adopted from a fast-reactor sodium-plenum correlation
   with the heat flux replaced by the total reaction heat rate. At 1550 K
   (expansion coefficient 2.4 × 10⁻⁴ K⁻¹, diffusivity 3.5 × 10⁻⁵ m² s⁻¹,
   conductivity 62 W m⁻¹ K⁻¹, Venus gravity 8.87 m s⁻²): modified
   Boussinesq number 1.2 × 10⁵, Nusselt number 8.9, coefficient
   8800 W m⁻² K⁻¹.
6. **Sodium pool boiling** (§5.5, Eqs. 17–18). The Noyes correlation
   converted to SI, giving 13.2 kW m⁻² K⁻¹ at baseline; condenser
   resistance neglected.
7. **Stirling efficiency** (§6.1, Eq. 19, attributed). A correlation in the
   hot-to-cold temperature ratio times the Carnot factor: 16% at 1223/740 K
   (Venus) and 39% at 700/190 K (Europa), checked by the reader.
8. **Venus ALIVE re-assessment** (§6.1). The model needs 5.8 kg/h oxidizer
   instead of ALIVE's 6.3 kg/h for 14.0 kW thermal, with 13.3 kW to the
   thermosiphon and 0.7 kW lost (about 5%, matching ALIVE); about 185 kg
   fuel for 5 days, 13% below ALIVE's 200 kg; fuel mass linear in duration,
   50 kg per 1.36 days. Model result.
9. **Venus, 1 kW mechanical** (§6.1). At 16% Stirling efficiency, 17 kg
   fuel per day: 86 kg fuel and 145 kg total (with 59 kg hardware) for 5
   days, 231 kg for 10 days; a NaS battery at 300 W h kg⁻¹ needs 400 kg for
   5 days. Ratios of "1.8 times" (5 days) and "2.5 times" (10 days) are
   stated. Model result.
10. **Europa, 94 W for 20 days** (§6.2, Fig. 9). High-efficiency Stirling
    (39%): 43 kg reactants, reactor 355 W (113 W lost, 242 W delivered),
    +2.15 kg per day, 80 kg total. Conservative Stirling (25%): 59 kg
    reactants, +2.95 kg per day, 96 kg total. TEG (8%): 157 kg reactants,
    1300 W reaction (125 W lost, 1175 W delivered), +7.85 kg per day, 168 kg
    total. Battery: 45 kW h in 70 kg (643 W h kg⁻¹, attainable with Li-CFx).
    Batteries are lightest at 20 days; the high-efficiency Stirling becomes
    lighter beyond 26 days (101 kg against 105 kg at 30 days). Model result.
11. **Europa preheat** (§6.2). 11.8 kg Li for 20 days; melting and heating
    it to auto-ignition (about 400 °C) costs a further 1.83 kg of reactants
    (0.50 kg Li, 1.33 kg SF6).
12. **Engineering requirements** (§6.3). Venus: loss resistance at least
    about 0.8 K/W and delivery resistance at most about 6.0 × 10⁻³ K/W for
    under 5% loss (about 5 cm of ceramic fiber); at 5.8 kg/h the reacting
    surface is 1550 K and the bath mean 1300 K. Europa: at least about
    5.4 K/W and at most about 0.025 K/W for under 10% loss; at 0.064 kg/h,
    surface 720 K, bulk 705 K. Tanks: 0.38 m³ Li for 5 days on Venus;
    0.023 m³ each of Li and SF6 for 20 days on Europa.
13. **Sensitivities** (§6.4). If 20% of the Li stops at Li2O, the heat of
    reaction at 298 K falls from 34.6 to 31.3 MJ per kg Li (−10%); halving
    the bath natural-convection coefficient cuts delivered heat from 13.3 to
    12.2 kW (−8%).
14. **Own experiment** (§2.1). Li/CO2 auto-ignition at about 380 °C and
    430 kPa "in our first experiments"; stated, no data shown.

# Methods

* **Model**: steady 0-D lumped model solved in Engineering Equation Solver
  (EES); no CFD and no experiment. Assumptions: steady state, well-mixed
  molten bath below the reacting interface, complete stoichiometric
  combustion, condensed products that sink (no pressure rise, no exhaust),
  no tank heat loss, negligible condenser resistance. The oxidizer flow is
  the independent variable. Properties from EES, NIST-JANAF and the cited
  sources; Appendix A tabulates all inputs and results.
* **Geometry** (Table 2), based on the Penn State ARL experimental reactor:

  | Component | Diameter [m] | Length [m] | Thickness [m] |
  |---|---|---|---|
  | Insulation | 0.1654 | 0.4372 | 0.0508 |
  | Reactor | 0.1146 | 0.4572 | 0.0060 |
  | Thermosiphon | 0.0445 | 0.3429 | 0.0025 |

* **Materials**: 316 stainless steel (28.1 and 20.0 W m⁻¹ K⁻¹ for Venus and
  Europa), ceramic fiber (0.27 and 0.09 W m⁻¹ K⁻¹), emissivity 0.2 (Venus)
  and 0.15 (Europa); a 1 m² radiator with emissivity 0.95 sets the 190 K
  cold side on Europa.
* **Environments**: Venus 740 K, 9.2 MPa, 96.5% CO2, wind 2 m/s
  (Churchill–Bernstein: Nusselt number about 1100, 275 W m⁻² K⁻¹,
  0.012 K/W); Europa vacuum, radiation only, about 100 K, gravity
  1.31 m s⁻².

# Tests and results

* **Venus baseline** (§5.3, §6.1, Appendix A): 14.0 kW thermal at 5.8 kg/h
  CO2; resistances (K/W) surface–bath 0.0171, bath–reactor 6.51 × 10⁻⁴,
  reactor wall 1.38 × 10⁻³, insulation 0.806, ambient convection 0.012,
  ambient radiation 0.155, total loss 0.819; bath–thermosiphon
  2.30 × 10⁻³, thermosiphon wall 2.01 × 10⁻³, boiling 1.8 × 10⁻³, total
  delivery 6.08 × 10⁻³; insulation surface about 750 K, sodium 1223 K. The
  1550 K bath is close to the about 1600 K melting point of stainless steel,
  so Inconel X-750 or a refractory liner may be needed.
* **ALIVE parameters** (Table 1, from the ALIVE report): hot 1223 K, cold
  773 K, Carnot efficiency 32%, Stirling 50% (of Carnot), loss 665 W,
  thermal 14 kW, electric 330 W, fuel 200 kg.
* **Europa baseline** (Appendix A): radiation 3.04, insulation 2.33, total
  loss 5.37, delivery 2.51 × 10⁻² K/W; bath coefficient
  4.52 × 10³ and sodium 1.32 × 10³ W m⁻² K⁻¹; Nusselt 5.60; modified
  Boussinesq 9.44 × 10²; SF6 6.4 × 10⁻² kg/h, Li 2.4 × 10⁻² kg/h; 242 W
  thermal to the engine, 148 W rejected, 94 W electric.
* Figs. 8–9 are used only through the values quoted in the text.
* Reader's checks: Eq. 4 at 5.8 kg/h gives 1.51 kg Li per hour, 182 kg for
  5 days (consistent with 185 kg); the Europa reactant masses follow from
  14.1 MJ/kg and the stated heat rates.

# Notation map

The paper is outside the plasma-propulsion domain; the registry column
gives a [notation](/notation.md) symbol only where its registry meaning
fits, otherwise "words".

| Greer, Paul & Rattner (2018) | Registry | Note |
|---|---|---|
| $\dot m_{oxidizer}$, $\dot m_{fuel}$, $\dot m_{products}$ | $\dot m$ with words | |
| $Q_{reaction}$, $Q_{out}$, $Q_{loss}$ | words (heat rates, W) | the dot is dropped in several equations |
| $i$ | words (specific enthalpy) | |
| $h$, $h_{Li}$, $h_{sodium}$ | words (heat-transfer coefficients) | |
| $R$ | words (thermal resistance) | |
| $k$, $\alpha$, $\beta$ | words (conductivity, diffusivity, expansion) | **collision** with $k$ (wavenumber) |
| $\varepsilon$ | words (emissivity) | **collision risk** with $\varepsilon_0$ |
| $\eta$, $\eta_{stirling}$, $\eta_{carnot}$ | words (conversion efficiencies) | **collision** with $\eta$ (thrust efficiency) |
| $T_H$, $T_C$, $\Delta T_{sat}$ | words | |
| $Nu$, $Bo^*$, $Pr$, $L_r$, $g$ | words | **collision:** registry $g$ is a relative speed |
| $D$, $r_1$, $r_2$, $L$, $A$ | words (geometry) | registry $L$ is a domain length |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Greer_Analysis_of_lithium-combustion_power_systems_for_extreme_env.pdf`.
   * **Version.** Publisher's typeset version (Elsevier), 12 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.05.039, printed on page 1
     and checked on Crossref (title, three authors, vol. 151, pp. 68–79
     match); issued and published-print 2018-10; Crossref has no online
     date, the PDF prints 21 May 2018 (received 23 February, revised 9 May,
     accepted 18 May 2018). Page 1 matches the filename title.
   * **How it was read.** Full text; all equations read cleanly from the
     rendered pages 5–7; Figs. 8–9 only through quoted values.
   * **Recorded as printed.**
     * Surface-to-bath resistance 0.017 K/W (§5.3, first paragraph;
       Appendix A 1.71 × 10⁻²) and "the same … 0.17 K/W" in the
       delivery-path paragraph.
     * The text says all resistances "were then summed in series", but
       neither printed total includes the surface-to-bath resistance
       (delivery 2.30 + 2.01 + 1.78 = 6.09 × 10⁻³; loss 0.819 without it);
       Fig. 7 draws it as a branch.
     * Characteristic length "0.63 m" (§5.4), while Table 2 gives
       0.1146 − 0.0445 = 0.070 m and the printed coefficient implies about
       0.063 m.
     * The modified Boussinesq number with a total heat rate in place of a
       heat flux is not dimensionless (m²); 1.2 × 10⁵ does not reproduce
       from the printed inputs (reader's check).
     * Battery-to-Stirling ratios "1.75–2.5 times" (abstract) and
       "1.8–2.5 times" (§6.1, §7); the printed masses give total-mass
       ratios 2.76 (5 days) and 3.46 (10 days); the stated figures match
       the excess mass.
     * Heat of reaction 27.5 MJ per kg Li (§5.1, §6.1, abstract) against
       34.6 MJ per kg Li for the same assumption at 298 K (§6.4);
       1.51 kg/h × 27.5 MJ/kg gives 11.5 kW, not the stated 14.0 kW.
     * Venus cooling capacity "2 kW" (§4) against "358 W" (§6.1), both
       attributed to ALIVE.
     * Table 1 Carnot efficiency 32%, while 1 − 773/1223 = 36.8%.
     * Appendix A labels the boiling resistance
       "R_thermosiphon,conduction".
     * Eq. 11 lacks the Stefan–Boltzmann constant.
     * Auto-ignition about 380 °C (Li/CO2, §2.1) and about 400 °C (Li/SF6,
       §6.2) concern different oxidizers.
     * The paper differs from ALIVE in oxidizer flow (5.8 against 6.3 kg/h)
       and fuel mass (185 against 200 kg), attributed to a different heat
       of reaction that ALIVE does not report.
   * **Reference list.** 49 printed entries (Crossref reference-count 49).
