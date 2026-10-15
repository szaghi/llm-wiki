---
type: Method
title: "Variable-geometry combustor"
description: "A ramjet combustor whose expansion angle and geometric-throat area are actuated to suit the inflow, sized by isobaric constant-velocity heating relations, which in an RBCC engine replaces the thermal throat by a geometric one and raised combustion efficiency, total-pressure recovery and specific impulse at Mach 3 and 6."
status: established
aliases: [variable geometry ramjet combustor, adjustable combustor, geometric-throat combustor]
tags: [rbcc, ramjet, variable-geometry, thermal-choking, combustor-design, kerosene]
timestamp: 2026-10-14T00:00:00Z
---

# Variable-geometry combustor

[Ye et al. (2018)](/sources/ye-2018.md) design a kerosene-fuelled
combustor for a [rocket-based combined-cycle engine](/definitions/rbcc-engine.md)
whose expansion angle and geometric-throat area are set by hydraulic
actuators according to the inflow (design range flight Mach 2–7). It
replaces the [thermal throat](/definitions/thermal-choking.md) of a
fixed-geometry combustor by a physical one.

## Design relations

The design assumes isobaric heating, under which the flow speed stays
constant (§2.1). With subscripts $i$ and $e$ for combustor inlet and exit,
the stated relations (not derived in the paper) are:

$$\frac{\mathrm{Ma}_e}{\mathrm{Ma}_i}=\left(\frac{T_{0,e}}{T_{0,i}}\left(1+\frac{\gamma-1}{2}\mathrm{Ma}_i^2\right)-\frac{\gamma-1}{2}\mathrm{Ma}_i^2\right)^{-1/2}\qquad\text{(Eq. 1)}$$

$$\frac{p_{0,e}}{p_{0,i}}=\left(\frac{1+\frac{\gamma-1}{2}\mathrm{Ma}_e^2}{1+\frac{\gamma-1}{2}\mathrm{Ma}_i^2}\right)^{\frac{\gamma}{\gamma-1}}\qquad\text{(Eq. 3)}$$

* **Area ratio** (Eq. 2). Neglecting viscous drag and the added fuel mass,
  the exit-to-inlet area ratio equals the bracket of Eq. 1, i.e. the
  inverse square of the Mach-number ratio, as constant velocity at
  constant pressure requires.
* **Throat area** (Eq. 4). The geometric-throat area follows from the
  choked mass-flow formula: the mass flow times $\sqrt{T_{0,e}}$ divided by
  a mass-flow constant (value not stated) and $p_{0,e}$.
* **Schedule** (Table 1). Expansion ratio and throat ratio decrease with
  flight Mach number from 2 to 6; at Mach 7 the combustor switches to an
  expanded configuration without a geometric throat. Table 1 is not a
  direct evaluation of Eq. 2: Eq. 2 gives an area ratio at least equal to
  the total-temperature ratio, but the table lists smaller values at Mach 2
  (3.2 against 3.5), 3 (2.8 against 3) and 4 (2.4 against 2.5) and an equal
  one at Mach 6 (1.7). The paper does not explain the difference.

## Hardware

The combustor (§2.2, Figs. 2–3) has a straight section, a fixed section
carrying streamwise-vortex fuel pylons, and a variable section of four
rods with hinge supports at both ends and cylinder hinges in between,
moved by two parallel hydraulic actuators. The geometric throat sits at
the junction with the inner nozzle. The fixed-geometry reference is the
same variable section set to a 2° expansion without a throat. A primary
rocket in the upstream strut, at 0.12 kg/s, serves as a pilot flame; the
secondary kerosene did not ignite reliably without it (§4.1).

## Performance against a fixed-geometry combustor

Steady 3-D RANS (CFD++, cubic k–ε, Eulerian spray, Westbrook–Dryer
[quasi-global kerosene mechanism](/methods/global-kerosene-mechanisms.md);
§3) at simulated Mach 3 and 6 (Table 6, Figs. 8–15):

| Quantity | Mach 3 fixed | Mach 3 variable | Mach 6 fixed | Mach 6 variable |
|---|---|---|---|---|
| Pressure force (N) | 3163 | 3684 | 2427 | 2849 |
| Drag (N) | −274 | −257 | −582 | −471 |
| Thrust $F$ (N) | 2889 | 3427 | 1845 | 2378 |
| $I_{sp}$ (s) | 924 | 1096 | 805 | 1016 |
| Exit $\eta_c$ | 0.81 | 0.90 | 0.78 | 0.92 |
| Exit total-pressure recovery | 0.58 | 0.63 | 0.24 | 0.32 |

Here $I_{sp}=F$ divided by standard gravity times the total fuel mass flow
including rocket propellant, and
$\eta_c=(T_0(x)-T_{0,i})/(T_{ad}-T_{0,i})$ with $T_{ad}$ from CEA (§4.1).
The $I_{sp}$ gains are +18.6% (Mach 3) and +26.2% (Mach 6); the thrust gains
are +18.6% and +28.9% (the paper's §4.3 assigns 26.2% to thrust).

Mechanisms reported:

* **Heat-release zone.** Concentrated between the pylons and the throat,
  20% shorter than in the fixed combustor, stated to help thermal
  protection (§4.2.1, Fig. 8).
* **Combustor Mach number.** Lower in the variable combustor, which cuts
  the total-pressure loss to combustion; the stronger
  [pre-combustion shock train](/definitions/precombustion-shock-train.md)
  loses more in the isolator (§4.3, Fig. 14).
* **Mode.** At Mach 6 the variable combustor stays in ramjet mode while
  the fixed one runs a "ramjet-scramjet mixed mode" (§4.2.2).

The authors attribute the $I_{sp}$ gain to the lower combustor Mach number
and the higher combustion efficiency together (Conclusion 3). The setup
has no grid-independence study for this geometry, and the validation
against sidewall pressure (Fig. 5) is judged "well fits" without a metric.

## Experiments

Direct-connect tests (vitiated air, Table 2) at simulated Mach 2, 3, 4 and
6 with the variable combustor (Table 5) gave $I_{sp}$ of 730, 1103, 1011 and
808 s with the rocket on, and 1408 s (Mach 4) and 1026 s (Mach 6) with it
off; the thrust column of three rows does not equal the printed pressure
force plus drag (see the Source page). No fixed-geometry test is
reported.

# Citations

1. [Ye et al. (2018)](/sources/ye-2018.md) — §2.1 (Eqs. 1–4, Table 1), §2.2 (Figs. 2–3), §3, §4.1 (Table 5), §4.2 (Figs. 8–13), §4.3 (Figs. 14–15, Table 6), Conclusion 3.
