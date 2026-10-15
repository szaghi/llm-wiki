---
type: Method
title: "Fuel-cooled thermoelectric generators for hypersonic vehicles"
description: "On-board electricity generation by thermoelectric modules placed between fuel already heated in the engine-wall cooling channels and fresh fuel, modelled as a quasi-one-dimensional nodal network; single-stage SiGe modules give the higher power density, two-stage modules the higher efficiency at maximum power."
status: established
aliases: [thermoelectric generator, TEG, two-stage thermoelectric generator, fuel-cooled TEG]
tags: [thermoelectric, power-generation, thermal-management, fuel-cooling, hypersonic-vehicle]
timestamp: 2026-10-14T00:00:00Z
---

# Fuel-cooled thermoelectric generators for hypersonic vehicles

On a hypersonic vehicle the air is too hot to serve as coolant, so on-board
fuel is the only heat sink ([Cheng et al. (2018)](/sources/cheng-2018.md),
§1, stated). The fuel-cooled thermoelectric generator (TEG) uses that sink
twice: hydrogen already heated in the engine-wall cooling channels flows on
the hot side of the thermoelectric modules, and fresh hydrogen, before it
enters the wall channels, flows in counter-flow on the cold side (§2).
Hydrogen avoids hydrocarbon coking (§2.4).

## Model

All from [Cheng et al. (2018)](/sources/cheng-2018.md), §3:

* **Nodal network.** Per streamwise element: hot fuel → convection → hot
  wall → ceramic plate (β-Si$_3$N$_4$, 0.2 mm) → hot junction (Peltier term,
  half the Joule heat, conduction through the legs) → cold junction → ceramic
  → cold wall → convection → cold fuel. One stage gives a 4 × 4 linear system
  per element (Eq. 9); two stages, with an intermediate ceramic plate, give
  6 × 6 (Eq. 23). Elements are in electrical series, so the open-circuit
  voltage and internal resistance are sums over elements (Eqs. 10–11).
* **Channels.** Quasi-1D first-order finite-difference mass, momentum (with
  friction), energy and ideal-gas equations for each channel (Eqs. 24–27),
  with convection from the Dittus–Boelter correlation (Eqs. 30–31); the
  friction-factor correlation is not stated. The TEG and channel systems are
  iterated to convergence.
* **Load.** The load resistance is set equal to the internal resistance. The
  authors note that this is only approximately the maximum-power point,
  because the junction temperatures, hence the open-circuit voltage, depend
  on the current (§3.1, after Eq. 13).
* **Material.** SiGe legs with $ZT$ rising from about 0.15 at 300 K to about
  1.3 at 1200 K (Fig. 2, after Wang et al.); hydrogen properties from
  CHEMKIN-II. Element 2 × 2 × 8 mm, gap 0.4 mm (Table 1). Mass flow 0.3 g/s,
  cold inlet 300 K at 3 MPa (Table 2).

## Results

[Cheng et al. (2018)](/sources/cheng-2018.md), §4.4, Tables 3–4, at
heating-channel inlet temperatures of 800, 1000 and 1200 K:

| Configuration | Maximum power density [kW/m²] | Efficiency at maximum power [%] |
|---|---|---|
| Single stage | 4.22 / 9.35 / 16.53 | 4.63 / 6.85 / 8.96 |
| Two stages | 3.38 / 7.43 / 12.94 | 5.79 / 8.45 / 10.78 |

* **Trade-off.** The single stage gives more power per unit area, attributed
  to its lower total internal resistance; the two stages convert more of the
  input heat, attributed to less heat conducted "in vain" to the cold channel
  through the taller module. Both quantities rise with the hot inlet
  temperature.
* **Heat bypass.** At 1200 K the hot fuel cools by about 390 K and the cold
  fuel warms by 360 K in the single stage (250 K and 220 K with two stages),
  so most of the heat passes to the cold fuel rather than being converted
  (§4.2–4.3, Figs. 5, 7).
* **Material per stage.** In the two-stage module the second stage runs at
  $ZT$ of about 0.34–0.77 against about 0.94–1.24 in the first (Fig. 8,
  approximate readings); the authors recommend a lower-temperature material
  for the second stage, such as AgPb$_m$SbTe$_{2+m}$ (recommendation, not
  computed).
* **Feasibility.** The authors conclude that thermoelectric generation is
  feasible as an auxiliary electricity source (§5); no system-level mass or
  power budget is given.

## Limits of the evidence

The model is not validated against measured TEG data; channel dimensions,
channel and element counts, two-stage leg heights, p-leg material data and
convergence tolerance are not stated
([Cheng et al. (2018)](/sources/cheng-2018.md), §2–3).

# Citations

1. [Cheng et al. (2018)](/sources/cheng-2018.md) — §1, §2 (Tables 1–2, Fig. 2), §3 (Eqs. 1–31), §4.2–4.4 (Figs. 5–8, Tables 3–4), §5.
