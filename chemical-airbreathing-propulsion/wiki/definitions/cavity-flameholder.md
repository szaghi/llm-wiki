---
type: Definition
title: "Cavity flameholder and lean blowoff"
description: "A wall cavity that stabilises the flame of a supersonic combustor in its shear layer and recirculation zone, together with its lean blowoff limit, the leanest fuelling at which combustion stays continuous, which for passive (upstream) injection rises with injection distance and passes through a multi-step extinction sequence."
status: established
aliases: [cavity flame holder, cavity-based flameholder, lean blowoff limit, lean blowout]
tags: [scramjet, cavity-flameholder, lean-blowoff, flame-stabilisation, ethylene, kerosene]
timestamp: 2026-10-14T00:00:00Z
---

# Cavity flameholder and lean blowoff

A cavity flameholder is a recess in the wall of a supersonic combustor
in which a recirculation zone forms below the shear layer that spans the
cavity mouth; the flame is anchored in that shear layer or in the
recirculation zone. [Song et al. (2018)](/sources/song-2018.md) study an
ethylene-fuelled model scramjet with one cavity on the lower wall (depth
16 mm, length 64 mm, aft ramp 45°; Figs. 2–3).
[Yan et al. (2018)](/sources/yan-2018.md) use two cavities in series as
the flameholders of a kerosene [RBCC](/definitions/rbcc-engine.md)
combustor.

## Lean blowoff limit

Song et al., §3.1, define the lean blowoff limit operationally as the
minimum fuel-injection pressure at which combustion stays continuous.
Starting from stable combustion they lower the injection pressure in
0.2 MPa steps and bracket the limit between the last stable and the first
failed point, each repeated at least five times. The abstract and
Conclusion 3 express the limit as a global $\phi$, linked to the pressure
only by the linear right axis of Fig. 5 ($\phi=0.2$ at 2 MPa). The
measured limits lie at $\phi$ of about 0.02–0.18 (figure readings).

They attribute to Driscoll and Rasmussen (refs. 22, 23) a correlation of
blowout limits by a modified Damköhler number built on a non-premixed
flame time from shear-layer similarity; as printed, the inverse Damköhler
number equals the overall $\phi$ at lean blowout and its inverse at rich
blowout.

## Passive and direct injection

Song et al. classify blowoff studies by where the fuel enters: directly
into the cavity, or upstream of it ("cavity passive fuel injection",
their configuration), so that the cavity is fuelled by entrainment from
the jet. Their results for passive injection (§3.1, Figs. 5–10):

* **Injection distance.** The limit rises with distance upstream of the
  cavity: for one 2 mm orifice from about 0.8 MPa at 10 mm to about
  1.8 MPa at the farthest station; for four 1 mm orifices (same global
  $\phi$ at equal pressure) from about 0.4 MPa at 10 mm to about 1.0 MPa at
  180 mm (stable points read from Fig. 5). The explanation given, by a
  jet-penetration correlation (ref. 48), is that a farther jet penetrates
  more above the cavity and entrains less fuel into the shear layer; it is
  stated, not computed.
* **Orifice number.** One orifice blows off at higher pressure than four.
  RANS of the 10 mm cases (SST k–ω, one-step ethylene chemistry) shows the
  four-orifice cavity hot throughout with fuel close to the cavity, and
  the single-orifice cavity hot only at its rear with fuel kept in the jet
  wake (Figs. 9–10).
* **Flame mode.** Four-orifice flames are basically steady and anchored
  in the shear layer; near the limit they sit just below the cavity mouth.
  Single-orifice flames are strongly unsteady, with intermittent local
  extinction in the shear layer (Figs. 6–7).
* **Wall pressure.** Combustion raises the lower-wall pressure only
  slightly (peak about 122 kPa against about 110 kPa cold, Fig. 8). At
  their respective limits the single-orifice flame produces the larger
  pressure rise, which the authors read as needing more combustion
  intensity to persist.

## Near-blowoff dynamics

From 20 000 frame/s luminosity imaging of the single-orifice flame,
Song et al. report:

* **Local extinction and reignition** (§3.2, Fig. 11; 0.8 MPa, 10 mm).
  The shear-layer flame weakens (0.00–0.15 ms), is cut near the trailing
  edge (0.20 ms), loses its downstream part and shrinks into the cavity
  (0.25 ms), spreads again (0.30–0.45 ms), breaks again (0.50 ms) and then
  strengthens and re-spreads to the main stream (0.65–1.00 ms). The
  proposed mechanism, not measured, is a downward shear-layer motion under
  an inflow disturbance, flame stretch beyond what the flame withstands
  near the trailing edge (ref. 35), and reignition by fuel entrained into
  the recirculation zone when a weaker flame lifts the shear layer less.
* **Five-step blowoff** (§3.3, Fig. 12; 0.6 MPa). (i) The shear-layer
  flame weakens; (ii) it is partly extinguished near the trailing edge;
  (iii) it shrinks into the rear of the cavity; (iv) it moves to the front
  half, near the front wall; (v) it goes out. Non-reacting RANS puts the
  lowest velocity and highest temperature in the front half of the cavity
  (Fig. 13), which the authors take as the "more combustible" region the
  flame migrates to; the argument is qualitative. They report agreement
  with the numerical multi-step blowoff of Wang et al. (ref. 39) and with
  the shrinking and fluctuating flames of Hammack and Allison (refs. 37,
  38).
* **Four orifices** never blew off at constant fuel supply; below their
  boundary spark ignition failed, and a flame lit by a hydrogen pilot went
  out when the hydrogen was cut (§3.3).

## Cavities and heat-release placement in an RBCC combustor

In the kerosene RBCC of [Yan et al. (2018)](/sources/yan-2018.md), the
two cavities set where heat is released: at flight Mach 3 the main heat
release should sit in the downstream, larger-area cavity, and it should
move upstream as flight Mach rises (Summary, §4.2, Fig. 11). In their
unsteady Mach-5 case, combustion grows behind the pylon and
[thermal choking](/definitions/thermal-choking.md) appears at the exit of
the frontal cavity (§4.1, Fig. 7).

# Citations

1. [Song et al. (2018)](/sources/song-2018.md) — §1 (refs. 22, 23), §2 (Figs. 2–4), §3.1 (Figs. 5–10, ref. 48), §3.2 (Fig. 11), §3.3 (Figs. 12–13), Conclusions.
2. [Yan et al. (2018)](/sources/yan-2018.md) — §2, §4.1 (Fig. 7), §4.2 (Fig. 11).
