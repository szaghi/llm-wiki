---
type: Definition
title: "Rocket-based combined-cycle engine"
description: "An air-breathing engine that integrates a rocket in a dual-mode ramjet/scramjet flow path so that one engine runs in ejector, ramjet, scramjet and rocket modes across the flight Mach range."
status: established
aliases: [RBCC, RBCC engine, rocket-based combined cycle]
tags: [rbcc, ramjet, scramjet, mode-transition, kerosene, combined-cycle]
timestamp: 2026-10-14T00:00:00Z
---

# Rocket-based combined-cycle engine

A rocket-based combined-cycle (RBCC) engine integrates a rocket engine
into the flow path of a dual-mode ramjet. [Ye et al. (2018)](/sources/ye-2018.md),
§1, describe four operating modes that depend on the flight state:
ejector, ramjet, scramjet and rocket, and place the engine in
two-stage-to-orbit and single-stage-to-orbit vehicle concepts. In all
three sources of this bundle the rocket sits inside the air flow path
(embedded in the flow path or in a central strut) and the air-breathing
combustor burns liquid kerosene.

## Configurations in the sources

| | [Wang et al. (2018)](/sources/wang-2018-c.md) | [Yan et al. (2018)](/sources/yan-2018.md) | [Ye et al. (2018)](/sources/ye-2018.md) |
|---|---|---|---|
| Study | full flow path, RANS | integrated flow path, RANS + freejet and direct-connect tests | combustor, direct-connect tests + RANS |
| Flight $\mathrm{Ma}_\infty$ | 1.5–6 (16 points, −4° to +8° incidence) | 3–6 (plus a Mach 2.5 case) | 2, 3, 4, 6 (design range 2–7) |
| Rocket | three embedded rockets | strut rocket, GOX/kerosene, 0.15 kg/s, mixture ratio 1.2, nozzle expansion ratio 6 | primary rocket in the strut, 0.12 kg/s, $O/F$ about 1.0, $p_c=1.5$ MPa, 1850 K |
| Rocket schedule | on for $\mathrm{Ma}_\infty\le3$, off from 4 | on at 2.5–5, off at 6 | on at 2–6 as a pilot; switched off at 4 and 6 |
| Flame holding | struts and cavities | two cavities, pylon and wall injection | streamwise-vortex fuel pylons, rocket pilot |
| Combustor | fixed, variable nozzle | two sections with exit area ratios 1.2 and 1.8 (times entrance height) | [variable geometry](/methods/variable-geometry-combustor.md) |

Sources: Wang et al., §2, §3.3, Table 1, Fig. 1; Yan et al., §2, Table 1,
Table 4; Ye et al., §2, Tables 1, 2, 4.

The rocket schedules differ because the engines differ: Wang et al. switch
the rockets off at the ejector-to-ramjet transition, which they place at
Mach 3 (and elsewhere in the same section "between 3 Ma and 4 Ma"), while
Ye et al. keep a low-flow rocket burning as an ignition source and study
its shut-off as a mode transition. This is a difference of design, not a
disagreement about the same engine.

## Modes and mode transition

* **Ejector to ramjet.** In the engine of
  [Wang et al. (2018)](/sources/wang-2018-c.md), §3.3, the inlet starts at
  about Mach 1.8, the ejector-to-ramjet transition is at Mach 3, the
  rockets are off from Mach 4, and cruise is above Mach 6.
* **Rocket-ramjet to ramjet.** [Ye et al. (2018)](/sources/ye-2018.md),
  §4.1, Table 5, switch the pilot rocket off in direct-connect tests at
  simulated Mach 4 and 6. Thrust falls by 10.8% and 12.2%; combustion
  efficiency $\eta_c$ rises from 0.898 to 0.947 and from 0.890 to 0.966;
  $I_{sp}$ (with rocket propellant counted in $\dot m_f$) rises from 1011 to
  1408 s and from 808 to 1026 s. The printed percentage gains of $I_{sp}$
  (28.2%, 37.1%) do not follow from these values (see the Source page).
  The [pre-combustion shock train](/definitions/precombustion-shock-train.md)
  moves toward the combustor and stays in the isolator.
* **Ramjet to scramjet.** [Yan et al. (2018)](/sources/yan-2018.md),
  §4.2–4.3, run ramjet mode with the rocket on up to Mach 5 and scramjet
  mode with the rocket off at Mach 6, where isolator injection keeps
  combustion self-sustained (combustion pressure 3.8 times the test
  reference pressure in a direct-connect test, Fig. 15).
  [Ye et al. (2018)](/sources/ye-2018.md), §4.2.2, compute that at Mach 6 a
  fixed-geometry combustor runs a "ramjet-scramjet mixed mode" (supersonic
  flow outside the pylons) while the variable-geometry one stays in
  ramjet mode.

## Component coordination

[Yan et al. (2018)](/sources/yan-2018.md) frame the RBCC design problem
as the "matching" of inlet, isolator shock train, heat release and
[thermal choking](/definitions/thermal-choking.md). At Mach 3,
front-loaded fuel pushed the shock into the inlet throat and cut air
capture by 17%, and moving fuel downstream restored the inlet and raised
the thrust coefficient from 0.402 to 0.458 (§4.2, Fig. 9, Table 5). The
best heat-release and choking location moves upstream as flight Mach
rises (Fig. 11).

## Skin friction

[Wang et al. (2018)](/sources/wang-2018-c.md), §3.2–3.3, Figs. 4–7,
Table 3, compute that in their engine at zero incidence:

* skin friction is about 12–15% of net thrust $F$ at Mach 1.5–3 (figure
  reading), about 19% at Mach 4, about 26% at Mach 5 and 40.3% at Mach 6;
* the combustor carries 48% of the skin friction at Mach 6 and 34% at
  Mach 1.5;
* the inlet has the highest mean wall shear stress at Mach 6, about
  640 Pa, twice the engine average (figure reading);
* the nozzle wall shear barely depends on flight speed and dominates the
  skin friction at low speed;
* with incidence from −4° to +8° the skin-friction share of thrust at
  Mach 6 ranges from 39.86% to 48.42%, minimum at +4°.

The authors call halving the skin friction worth 20% of thrust at Mach 6;
[boundary-layer combustion](/methods/boundary-layer-combustion.md) is the
reduction they study. This is a single engine computed without a stated
grid, trajectory or fuel schedule.

## Numerical modelling

All three sources use steady (Yan et al. also unsteady) 3-D RANS with
liquid-kerosene spray and finite-rate
[global kerosene chemistry](/methods/global-kerosene-mechanisms.md)
without a turbulence–chemistry interaction model: ANSYS Fluent with SST
k–ω and Lagrangian droplets (Wang et al., §2.2; Yan et al., §3), CFD++
with cubic k–ε and an Eulerian dispersed-phase spray (Ye et al., §3).
Validation is against wall pressure in direct-connect or freejet tests,
judged in words without an error metric in all three.

# Citations

1. [Wang et al. (2018)](/sources/wang-2018-c.md) — §2, §3.2–3.3, Table 1, Table 3, Figs. 1, 4–7.
2. [Yan et al. (2018)](/sources/yan-2018.md) — §2, §3, §4.2–4.3, Tables 1, 4, 5, Figs. 9, 11, 15.
3. [Ye et al. (2018)](/sources/ye-2018.md) — §1, §2, §3, §4.1, §4.2.2, Tables 1, 2, 4, 5.
