---
type: Definition
title: "Thermal choking and the thermal throat"
description: "Choking of a ramjet or dual-mode combustor by heat release rather than by a geometric throat, whose axial location, set by the fuel distribution, governs how inlet, isolator and combustor match across flight Mach numbers."
status: established
aliases: [thermal throat, thermal choke, heat-release choking]
tags: [ramjet, scramjet, rbcc, heat-release, fuel-injection, mode-transition]
timestamp: 2026-10-14T00:00:00Z
---

# Thermal choking and the thermal throat

In a combustor without a geometric throat, heat release can bring the
flow to sonic conditions; the sonic section is the thermal throat, and the
combustor is thermally choked. The two sources of this bundle that study
it treat it as the counterpart of a geometric throat:
[Ye et al. (2018)](/sources/ye-2018.md), §4.2, compare a fixed-geometry
combustor that runs on a thermal throat with a
[variable-geometry combustor](/methods/variable-geometry-combustor.md)
that has a geometric one, and
[Yan et al. (2018)](/sources/yan-2018.md) use the axial location of
thermal choking as the variable that couples heat release to the
[pre-combustion shock train](/definitions/precombustion-shock-train.md)
in a [rocket-based combined-cycle engine](/definitions/rbcc-engine.md).

## Structure of the thermal throat

[Ye et al. (2018)](/sources/ye-2018.md), §4.2.1, Fig. 10, compute that at
simulated Mach 3 the fixed-geometry combustor (2° expansion) forms a
thermal choke with a complex three-dimensional sonic surface; its wall
pressure rises before the secondary injection and then falls. The
variable-geometry combustor at the same condition burns at nearly
constant pressure ahead of its geometric throat, in a heat-release zone
20% shorter. At Mach 6 the fixed combustor keeps supersonic flow outside
the fuel pylons ("ramjet-scramjet mixed mode"), while the variable one
stays in ramjet mode (§4.2.2, Figs. 11–13).

## Location against flight Mach number

[Yan et al. (2018)](/sources/yan-2018.md), Fig. 11, Table 5, find from
their RANS cases that the best thermal-choking location is at the
combustor exit (largest-expansion section) at $\mathrm{Ma}_\infty=3$ and
moves upstream, into regions of smaller expansion, as $\mathrm{Ma}_\infty$
rises. At $\mathrm{Ma}_\infty=6$ with the rocket off, no clear thermal
choking forms and subsonic and supersonic regions coexist (§4.2, Fig. 10c).
In their unsteady Mach-5 case, thermal choking appears at the exit of the
frontal cavity once the shock train has settled (§4.1, Fig. 7).

The two sources agree at $\mathrm{Ma}_\infty=6$. Neither finds a clean
thermal choke there: Yan et al. see subsonic and supersonic regions
coexist (§4.2, Fig. 10c), and the fixed-geometry combustor of
[Ye et al. (2018)](/sources/ye-2018.md) keeps supersonic flow outside the
fuel pylons (§4.2.2, Figs. 11–13). Both find that combustion survives
shutting off the rocket: Ye et al. in direct-connect experiments at
simulated Mach 4 and 6, where the engine passes smoothly from
rocket-ramjet to ramjet mode (§4.1, Figs. 6–7), and Yan et al. in a
Mach-6 direct-connect test whose forward-combustor pressure stays at 3.8
times the reference pressure with the rocket off (§4.3, Fig. 15).

They attribute three related observations to the literature (§1):
thermal choking forms more easily in a constant-area section (ref. 14,
cited as Doolan); a gradient heat-release model represents it better than
a linear one (Riggins, ref. 16); and an upstream injector with faster
heat release moves the thermal throat forward (Wang, ref. 17).

## Distributed heat release

Yan et al. call "distributed heat release" the split of the fuel between
injection stations (I0 in the isolator, I1 and I2 in the combustor, at $x$ = 28, 42
and 50 inlet-throat heights) to place heat release, and with it the choking point, where the
inlet stays started (§4.2, Figs. 8–10, Tables 4–5). Their results:

| Flight $\mathrm{Ma}_\infty$ | Fuel split ($\phi$ at I0 / I1 / I2) | Outcome | Thrust coefficient |
|---|---|---|---|
| 3 | – / 0.6 / 0.3 | pressure 4.5 times the reference pressure, shock pushed into the inlet throat, air capture −17% | 0.402 |
| 3 | – / 0.3 / 0.6 | inlet restored, choking moved to the combustor exit | 0.458 |
| 4 | – / 0.9 / – | shock at the isolator entrance, the limit of inlet operation | 0.433 |
| 4 | – / 0.7 / 0.2 | shock back in the isolator, total heat release +18%, choking moved downstream | 0.460 |
| 4 | – / 0.3 / 0.6 | lower $\eta_c$, total heat release 8% below the 0.7 / 0.2 split | 0.437 |
| 6 | – / 1.0 / – | rocket off; $\eta_c$ about 81% (figure reading) | 0.297 |
| 6 | 0.4 / 0.6 / – | rocket off; $\eta_c$ about 89% (figure reading), higher pressure in the first combustor region | 0.316 |

The thrust coefficient is the effective thrust divided by the freestream
dynamic pressure times the capture area (Eq. 6). The paper calls the
Mach-3 gain "+12%"; the table values give +13.9%. Its axial heat-release
curves (Eq. 5, Fig. 8c) are a total-enthalpy flux with mislabelled units,
not the volumetric $\dot q$ of this bundle's registry (see the Source
page).

[Ye et al. (2018)](/sources/ye-2018.md) take a different approach: instead of moving the thermal throat with the fuel
split, they impose a geometric throat whose area is scheduled with flight
Mach number. The two papers do not compare the approaches with each
other.

# Citations

1. [Yan et al. (2018)](/sources/yan-2018.md) — §1 (refs. 14, 16, 17), §4.1 (Fig. 7), §4.2 (Figs. 8–11, Eqs. 5–6, Tables 4–5), §4.3 (Fig. 15).
2. [Ye et al. (2018)](/sources/ye-2018.md) — §4.1 (Figs. 6–7), §4.2.1 (Figs. 8–10), §4.2.2 (Figs. 11–13).
