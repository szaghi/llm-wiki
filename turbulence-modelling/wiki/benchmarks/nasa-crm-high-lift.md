---
type: Benchmark
title: "NASA CRM high-lift configuration"
description: "The NASA High-Lift Common Research Model (CRM-HL), a half-span transport in landing configuration at Mach 0.2 and mean-chord Reynolds number 5.49 million: a test of a learned wall model in wall-modelled LES at 7° and 19°, and of immersed-boundary wall-function RANS at 17.05° on a 2.4-billion-cell Cartesian grid."
status: established
aliases: [CRM-HL, HL-CRM, NASA High-Lift Common Research Model, NASA CRM-HL, HLPW-4 CRM-HL]
tags: [benchmark, wmles, wall-model, rans, immersed-boundary, machine-learning]
timestamp: 2026-10-26T10:26:00Z
---

# NASA CRM high-lift configuration

The NASA High-Lift Common Research Model (CRM-HL) is the half model of a
civil transport with deployed slats and flaps, a nacelle and pylon,
used as the test case of the Fourth AIAA High-Lift Prediction Workshop
(HLPW-4). Both sources run it at freestream Mach number $M_\infty=0.20$ and
$Re=5.49\times10^6$ based on the mean aerodynamic chord. The flow combines
thin leading-edge boundary layers on slats, main wing and flaps, wakes
merging over the flaps, and separation that spreads with incidence until
maximum lift. The quantities compared are the lift, drag and pitching-moment
coefficients $C_L$, $C_D$ and $C_M$ against incidence $\alpha$ (page-local:
angle of attack), and $C_p$ and $C_f$ on spanwise sections. In this bundle
it tests near-wall modelling at aircraft scale: a learned wall model in
[wall-modelled LES](/methods/wall-modelled-les.md) and a wall function at an
[immersed boundary](/methods/immersed-boundary-method.md) in RANS. A
second high-lift workshop configuration is the
[JAXA Standard Model](/benchmarks/jaxa-standard-model.md).

## Configurations in the sources

| Item | [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md), §4.7 | [Constant et al. (2024)](/sources/constant-2024.md), §6.3 |
|---|---|---|
| Model | wall-modelled LES (CharLES), dynamic Smagorinsky SGS model, [building-block-flow wall model](/methods/building-block-flow-wall-model.md) against the algebraic [equilibrium wall model](/methods/equilibrium-wall-model.md) | steady RANS with the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md) and Musker's wall function at a ghost-cell immersed boundary |
| Set-up | semi-span in free air; free-slip symmetry plane, plug inflow, non-reflecting outlet | HLPW-4 nominal configuration (slat 30°/30°, flap 40°/37° inboard/outboard), half span 29.4 m, mean aerodynamic chord 7.005 m; viscosity modified to reach the Reynolds number |
| Incidence | $7^\circ$ and $19^\circ$ for the learned wall model | $17.05^\circ$, below maximum lift "to avoid massive separation" |
| Grid | 30 million points, 0 to 20 points per boundary-layer thickness | octree Cartesian, $h_{\min}=3.5$ mm on slats, flaps and pylon, $2h_{\min}$ on the rest of the wing and nacelle, $8h_{\min}$ on the fuselage, target $y^+=500$, $2.4\times10^9$ cells |
| Reference | wind-tunnel data corrected to free air | body-fitted RANS of the LAVA structured solver on grid D ($5.5\times10^8$ cells, target $y^+=0.75$) |

## What the case tests

**A learned wall model on an aircraft it has not seen.**
[Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) deliberately
leave airfoils, wings and bumps out of the building blocks of their
[machine-learning wall model](/methods/machine-learning-wall-model.md), so
the CRM-HL is an out-of-sample test (§2.3, §4.7). The building-block model
gives moderate improvements over the equilibrium model, especially near
stall and most clearly in the pitching moment; the exception is $C_L$ at low
incidence, where the equilibrium model's better prediction is attributed to
error cancellation ("it has been reported", without citation) (§4.7,
Fig. 15). The model's confidence falls below 20% at the leading edges of
nacelle, slats and flaps, where the grid has no points across the boundary
layer, and in the separated regions at the wing tip and near the root
(Fig. 16; see [model-form uncertainty](/definitions/model-form-uncertainty.md)).
The authors find the external error of the SGS model, not the wall model,
the main limit of accuracy, and recall that Ling et al. (2022), extending
the building blocks to the SGS model, "greatly improved" $C_L$, $C_D$ and
$C_M$ on this configuration (§5(4), §6). The grid resolution, with 0 to 20
points per boundary-layer thickness, is recorded on
[grid-point requirements](/results/les-grid-point-requirements.md).

**Immersed-boundary RANS with a wall function.**
[Constant et al. (2024)](/sources/constant-2024.md) (read in the HAL
author manuscript) apply their modelling-height adaptation and their
higher-order reconstruction of the wall pressure, developed on the
[NACA 0012](/benchmarks/naca-0012-airfoil.md), to the CRM-HL (§6.3,
Table 9):

| Solution | $C_D$ | error | $C_L$ | error |
|---|---|---|---|---|
| IBM, single modelling height, zeroth-order wall pressure | 0.3767 | 9.1% | 2.2118 | 13% |
| IBM, adapted height, zeroth-order | 0.3783 | 9.5% | 2.2940 | 9.5% |
| IBM, adapted height, second-order | 0.3405 | 1.5% | 2.3205 | 8.4% |
| LAVA body-fitted (reference) | 0.3455 | — | 2.5341 | — |

The higher-order reconstruction "divides the error made on the drag
coefficient by six". Pre-processing of the Cartesian grid took under seven
hours in a massively parallel environment from the surface mesh alone,
which the authors set against weeks for a curvilinear grid of comparable
resolution and months to calibrate one for WMLES (§6.3, Table 8; stated,
without a breakdown). The run used "20×28" Intel Broadwell CPUs (as printed),
five runs of 15,000 iterations, the adaptation after the third (§6.3). The
$C_p$ and $C_f$ on sections D, E and F and the off-body vorticity are
compared in Figs. 37–39.

**What the two studies share.** Both locate the weak point at the leading
edges of the high-lift elements, where the boundary layers are thinnest
relative to the grid: the low confidence of the learned wall model there in
[Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md), and the
leading-edge wall-function error that the modelling-height adaptation
addresses in [Constant et al. (2024)](/sources/constant-2024.md).

## Qualifications

- The two studies differ in modelling level (WMLES against steady RANS),
  incidence ($7^\circ$ and $19^\circ$ against $17.05^\circ$) and reference
  (wind-tunnel data corrected to free air against a body-fitted RANS);
  neither compares its errors with the other's.
- The immersed-boundary errors of [Constant et al. (2024)](/sources/constant-2024.md)
  are relative to another RANS solution on a grid four times smaller, not
  to experiment; their lift error stays at 8.4% after both corrections.
  Their Table 9 drag error of 9.1% for the first row is 9.0% by the table's
  own coefficients *(compiler check, not in the sources)*.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) give their
  force comparison only in figures (Fig. 15); no coefficients are printed.

# Citations

- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §2.3; §4.7, Figs. 14–16; §5(4); §6.
- [Constant et al. (2024)](/sources/constant-2024.md) — §6.3, Tables 7–9, Figs. 35–39; §7.
