---
type: Method
title: "Lithium-combustion power systems"
description: "Stored-chemical-energy power source in which a molten lithium bath burns a gaseous oxidizer (in-situ CO2 on Venus, stored SF6 on Europa) and a sodium thermosiphon carries the heat to a Stirling engine or thermoelectric array, sized with a lumped energy balance and thermal-resistance network."
status: established
aliases: [lithium combustion power system, metal-combustion power system, stored chemical energy power system, SCEPS, Li–CO2 combustion, Li–SF6 combustion]
tags: [power-system, metal-combustion, lithium, heat-transfer, thermal-resistance-network, stirling, spacecraft, model]
timestamp: 2026-10-14T00:00:00Z
---

# Lithium-combustion power systems

A lithium-combustion power system stores chemical energy in lithium metal,
burns it with a gaseous oxidizer, and converts the heat to electric or
mechanical power with a heat engine. In the reactor of
[Greer et al. (2018)](/sources/greer-2018.md), §2–5, a liquid lithium bath
burns the oxidizer at its free surface; the condensed products sink, so there
is no exhaust and no pressure rise; a sodium thermosiphon immersed in the bath
delivers the heat to a Stirling engine or a thermoelectric generator (TEG)
array. The paper cites undersea lithium–SF₆ systems as heritage and a NASA
Venus-lander concept ("ALIVE") as the starting point (attributed).

Every result below is a prediction of a single steady-state model not
validated against measurements; the authors state that an experimental reactor
is under construction (§7).

## Reactions and energy release

* **Lithium–CO₂ (in-situ oxidizer on Venus).** The assumed mechanism is
  10 Li + 2 CO₂ → 4 Li₂O + Li₂C₂, followed by Li₂O + CO₂ → Li₂CO₃, net
  10 Li + 6 CO₂ → 4 Li₂CO₃ + Li₂C₂ ([Greer et al. (2018)](/sources/greer-2018.md),
  §5.1, Eqs. 1–3). Li₂O is assumed not to dissociate (dissociation only above
  2500 K, attributed; neither the model nor the reference reactor exceeds
  1600 K). The mechanism yields 27.5 MJ per kg of lithium; a well-mixed
  reactor producing only Li₂CO₃ and carbon could reach 39–45 MJ/kg
  (attributed). Fuel and oxidizer flows are tied by stoichiometry,
  $\dot m_f = \frac{10.0}{6.0}\cdot\frac{6.9}{44.0}\,\dot m_o$ (Eq. 4), and
  the heat of reaction comes from an enthalpy balance of reactant and product
  streams (Eqs. 5–6).
* **Lithium–SF₆ (stored oxidizer on Europa).** 8 Li + SF₆ → 6 LiF + Li₂S,
  complete and stoichiometric, 14.1 MJ per kg of reactants (§2.2, §6.2,
  Eq. 20).
* **Ignition.** The authors report Li/CO₂ auto-ignition at about 653 K
  (∼380 °C) and 430 kPa "in our first experiments", without data (§2.1); the
  Europa preheat assumes auto-ignition at about 673 K (~400 °C) for Li/SF₆
  (§6.2).

## Thermal model

[Greer et al. (2018)](/sources/greer-2018.md), §5, Figs. 5–7, Eqs. 7–18, solved
in Engineering Equation Solver:

* **Assumptions.** Steady state; well-mixed bath below the reacting surface;
  complete stoichiometric combustion; no heat loss through the fuel tank;
  negligible condenser resistance. The oxidizer mass flow is the independent
  variable, set to reach a target heat-release rate.
* **Network.** The heat of reaction splits into a **loss path** (bath,
  stainless-steel reactor wall, ceramic-fibre insulation, then forced
  convection and radiation in parallel to the ambient) and a **delivery
  path** (bath, thermosiphon wall, boiling sodium). Each path is a series of
  thermal resistances: convection, cylindrical conduction, forced convection
  and a linearized radiation resistance (Eqs. 7–11); the reaction heat equals
  loss plus delivered heat (Eqs. 12–14).
* **Closures.** Bath natural convection uses a Nusselt-number correlation
  proportional to a modified Boussinesq number to the power 0.096, adopted
  from a sodium-plenum correlation for fast-reactor severe accidents, with
  the correlation's heat flux replaced by the total reaction heat rate
  (§5.4, Eqs. 15–16); sodium pool boiling uses the Noyes correlation
  converted to SI (§5.5, Eq. 17); external convection on Venus uses
  Churchill–Bernstein (§5.3). As used, the modified Boussinesq number is not
  dimensionless, and its printed value does not reproduce from the printed
  inputs (see the source page).
* **Geometry.** Based on the Penn State ARL experimental reactor: reactor
  0.1146 m diameter and 0.4572 m long, thermosiphon 0.0445 m diameter and
  0.3429 m long, insulation 0.0508 m thick (Table 2).

## Conversion efficiency

The Stirling efficiency is taken from a correlation of the earlier Venus
concept (attributed): 0.3323 times the hot-to-cold temperature ratio to the
power 0.3655, times the Carnot factor (§6.1, Eq. 19). It gives 16 % between
1223 K and 740 K (Venus) and 39 % between 700 K and 190 K (Europa). A
conservative 25 % Stirling and an 8 % TEG are also assessed for Europa
(§6.2).

## Venus lander with in-situ CO₂

[Greer et al. (2018)](/sources/greer-2018.md), §5.3, §6.1, Appendix A; Venus
ambient 740 K, 9.2 MPa, 96.5 % CO₂, wind 2 m/s:

* **ALIVE re-assessment.** 14.0 kW of reaction heat needs
  $\dot m_o$ = 1.61×10⁻³ kg/s (5.8 kg/h) instead of ALIVE's 1.75×10⁻³ kg/s
  (6.3 kg/h); 13.3 kW is delivered and 0.7 kW, about 5 %, is lost, as in
  ALIVE. The lithium for 5 days is about 185 kg, 13 % less than ALIVE's
  200 kg; the paper attributes the difference to a different heat of
  reaction.
* **Temperatures.** Reacting surface 1550 K, mean bath 1300 K, sodium
  1223 K, insulation outer surface about 750 K. 1550 K is close to the about
  1600 K average melting point of stainless steel, so Inconel X-750 or a
  refractory liner may be warranted.
* **1 kW of mechanical power at 16 %.** 17 kg of lithium per day; 145 kg in
  total for 5 days (86 kg of fuel plus 59 kg of hardware) and 231 kg for
  10 days (172 kg plus 59 kg). A sodium–sulfur battery at 1.08 MJ/kg
  (300 W h/kg) needs 400 kg for 5 days. The paper's "1.8 times" and "2.5
  times" are excess-mass ratios; the masses are the quantities to quote.
* **Requirements.** Total loss resistance at least about 0.8 K/W and
  delivery resistance at most about 6.0×10⁻³ K/W for under 5 % loss,
  achievable with about 5 cm of ceramic-fibre insulation; 0.38 m³ of lithium
  for 5 days (§6.3).

## Europa lander with stored SF₆

[Greer et al. (2018)](/sources/greer-2018.md), §6.2–6.3, Fig. 9; vacuum,
radiation only, ambient about 100 K; 94 W of electric power for 20 days:

| Converter | Reactant mass (20 days) | Reaction heat | Total system mass | Added per day |
|---|---|---|---|---|
| Stirling, 39 % | 43 kg | 355 W (113 W lost, 242 W delivered) | 80 kg | 2.15 kg |
| Stirling, 25 % | 59 kg | — | 96 kg | 2.95 kg |
| TEG, 8 % | 157 kg | 1300 W (125 W lost, 1175 W delivered) | 168 kg | 7.85 kg |
| Battery, 2.31 MJ/kg (643 W h/kg) | — | — | 70 kg (162 MJ, 45 kW h) | — |

* **Crossover.** Batteries are lightest at 20 days; the 39 % Stirling system
  becomes lighter beyond 26 days (101 kg against 105 kg at 30 days).
* **Preheat.** Melting the 11.8 kg of lithium and heating it to auto-ignition
  costs a further 1.83 kg of reactants (0.50 kg lithium, 1.33 kg SF₆).
* **Requirements.** Loss resistance at least about 5.4 K/W and delivery
  resistance at most about 0.025 K/W for under 10 % loss; at
  1.78×10⁻⁵ kg/s (0.064 kg/h) of SF₆ the surface is at 720 K and the bulk at
  705 K; 0.023 m³ each of lithium and SF₆.

## Sensitivities

If 20 % of the lithium stops at Li₂O, the heat of reaction at 298 K falls from
34.6 to 31.3 MJ per kg of lithium (−10 %); halving the bath convection
coefficient cuts the delivered heat on Venus from 13.3 to 12.2 kW (−8 %)
([Greer et al. (2018)](/sources/greer-2018.md), §6.4). The 34.6 MJ/kg of this
section and the 27.5 MJ/kg used for the Venus baseline are not reconciled in
the paper.

# Citations

1. [Greer et al. (2018)](/sources/greer-2018.md) — §2 (2.1–2.2), §5.1–5.5 (Eqs. 1–18, Table 2, Figs. 5–7), §6.1–6.4 (Eqs. 19–20, Table 1, Figs. 8–9), §7, Appendix A.
