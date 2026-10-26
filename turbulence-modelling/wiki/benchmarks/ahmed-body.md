---
type: Benchmark
title: "Ahmed body"
description: "The Ahmed body, a bluff car-like body with a slanted rear, whose slant angle sets the separation regime: at 35° (massive separation) a test of immersed-boundary wall-modelled LES on lattice Boltzmann grids, at 25° (separation and reattachment) the calibration case of a DDES procedure later applied to a full-scale estate car."
status: established
aliases: [Ahmed car body, Ahmed reference model, 25° Ahmed body, 35° Ahmed body]
tags: [benchmark, separated-flow, hybrid-rans-les, des, wmles, immersed-boundary]
timestamp: 2026-10-26T07:40:00Z
---

# Ahmed body

The Ahmed body is a simplified road-vehicle shape: a block with a rounded
front, a slanted upper rear surface of angle $\varphi$ (page-local) and a
vertical base, mounted on four cylindrical stilts above a ground plane. It
is about 1.04 m long and 0.29 m high. The flow stays attached over the
front and roof and separates at the rear, and the slant angle sets the
regime: as recalled by [Cai et al. (2022)](/sources/cai-2022.md), drag
falls sharply ("drag crisis") above about 30°, where the flow separates
massively from the upstream edge of the slant, while at 25° the shear layer
separates and reattaches on the slant, a regime that the authors leave as a
challenge for future work. The quantities compared are the drag
and lift coefficients $C_D$ and $C_L$, the pressure on the slant and base,
and velocity profiles over the slant and in the wake. In this bundle the
case tests near-wall treatments of scale-resolving simulation on a separated
bluff body: immersed-boundary wall-modelled LES and the choice of hybrid
RANS/LES model.

## Configurations in the sources

| Item | [Cai et al. (2022)](/sources/cai-2022.md) | [Delassaux et al. (2023)](/sources/delassaux-2023.md) |
|---|---|---|
| Slant angle | 35° | 25°, four variants: sharp edges; side edges rounded; roof edge rounded; both rounded |
| Dimensions | length 1.044 m, height 0.288 m, width 0.389 m; ground clearance 0.05 m; stilts of 0.03 m diameter | length 1044 mm, width 380 mm, height 288 mm |
| Reynolds number | $Re_H=7.68\times10^5$ on height, $U_\infty=40$ m/s (Lienhart & Becker) | not given |
| Domain | about $8L\times5W\times5H$ (ERCOFTAC), blockage 4% | not given (recap of earlier work) |
| Solver | lattice Boltzmann (ProLB, D3Q19, regularized collision) on octree Cartesian grids | ANSYS Fluent, incompressible cell-centred finite volume, bounded central convection |
| Model | Vreman SGS model, explicit equilibrium wall model, near-wall constrained-LES eddy viscosity, at the immersed boundary | SST-based DDES selected after comparing realizable $k$-$\varepsilon$, SST, SAS, SST DDES and SBES |
| Grid | coarse $1.36\times10^7$ cells ($\Delta x_{\min}=9.0\times10^{-3}H$), fine $4.03\times10^7$ ($4.5\times10^{-3}H$) | 20 prism layers at $y^+<1$, 3–4 mm surface cells, 5 mm wake tetrahedra |
| Time | 200 flow-through times $H/U_\infty$, last 150 averaged; Mach number raised from 0.12 to 0.24 to enlarge the time step | $\Delta t=5\times10^{-5}$ s (also $1.5\times10^{-5}$ s) |
| Reference data | Lienhart & Becker velocity profiles; drag of Ahmed et al., Meile et al., Liu et al.; body-fitted RANS and DES of Guilmineau et al. | experimental $C_D$, $C_L$, $C_p$ (source not detailed) |

The data of [Delassaux et al. (2023)](/sources/delassaux-2023.md), §5,
are a recapitulation of the authors' earlier paper, used to calibrate the
procedure they then apply to a full-scale estate car.

## What the case tests

**Immersed-boundary wall modelling in massive separation.**
[Cai et al. (2022)](/sources/cai-2022.md) run the 35° body with an
[immersed boundary method](/methods/immersed-boundary-method.md) in the
[lattice Boltzmann](/methods/lattice-boltzmann-method.md) code
[ProLB](/software/prolb.md), comparing two strategies: the wall model on
the whole body ("wall-law") and a no-slip condition imposed in advance on
the slant and base ("no-slip"). On the coarse grid the wall-law run does not
separate on the slant, which the authors attribute to the assumed alignment
of wall stress and tangential velocity and to too little near-wall turbulent
stress. On the fine grid it separates massively and its resolved
fluctuations compare well with experiment toward the end of the slant, while
the no-slip run separates too early on the slant (§IV, Figs. 4–9). The
authors state that enhancing the near-wall Reynolds stress with their
constrained-LES eddy viscosity is "very essential" for separation in the
immersed-boundary framework, without showing a run that omits it. See
[wall-modelled LES](/methods/wall-modelled-les.md) and
[equilibrium wall model](/methods/equilibrium-wall-model.md).

Drag coefficients at $Re_H=7.68\times10^5$ ([Cai et al. (2022)](/sources/cai-2022.md),
Table III; near-field / far-field evaluation):

| Run | $C_D$ |
|---|---|
| wall-law, fine | 0.2347 / 0.2380 |
| wall-law, coarse | 0.2742 / 0.2912 |
| no-slip, fine | 0.2553 / 0.2588 |
| no-slip, coarse | 0.2548 / 0.2486 |
| experiment, Meile et al. (same $Re_H$) | 0.279 |
| experiment, Ahmed et al. ($Re_H=1.2\times10^6$) | 0.26 |
| experiment, Liu et al. ($Re_H=1.4\times10^5$) | 0.32 |
| body-fitted $k$-$\omega$ SST / EARSM / DES / IDDES (Guilmineau et al.) | 0.2999 / 0.2603 / 0.3156 / 0.3452 |

The authors call all their values "close to the existing values" and the
fine wall-law drag closer to Meile et al. than the body-fitted IDDES; it is
also farther from Meile et al. than the fine no-slip run, the body-fitted
SST, EARSM and DES, and the coarse wall-law run whose slant flow does not
separate *(compiler check, not in the sources)*.

**Choice of hybrid model at 25°.** As recalled by
[Delassaux et al. (2023)](/sources/delassaux-2023.md), §5, from their
earlier calibration on the four 25° bodies: the realizable
[$k$-$\varepsilon$ model](/methods/k-epsilon-model.md) gives no separation
on the slant and [$k$-$\omega$ SST](/methods/k-omega-sst-model.md) a
massive one; SAS, SST DDES and SST SBES all separate and reattach, SAS
over-estimating and SBES under-estimating the recirculation length, and
[DDES](/methods/detached-eddy-simulation.md) closest to experiment. With SST
DDES on the 20-layer grid the errors are at most 3.3% on drag and 7.1% on
lift (Table 2):

| Body | $C_D$ exp. / DDES | $C_L$ exp. / DDES |
|---|---|---|
| sharp edges | 0.356 / 0.365 | 0.311 / 0.333 |
| side edges rounded | 0.359 / 0.347 | 0.241 / 0.257 |
| roof edge rounded | 0.298 / 0.299 | 0.333 / 0.337 |
| side and roof rounded | 0.297 / 0.296 | 0.254 / 0.255 |

The recap also fixes the numerical practice: $y^+<1$ with at least 15 to
20 prism layers (30 better for the sharp-edged body), 5 mm tetrahedra in the
wake, a 3 mm minimum surface size from Menter's criterion against LES
intrusion into the boundary layer, and a time step giving a maximum CFL
number of 3 in the separated region; with CFL numbers above 10 the slant
shows no separation or a massive one (§5). Rounded separation lines remain the weak point: on the car the
authors find DDES under-predicting $C_p$ there, "consistent" with the
Ahmed-body results, and relate it to grid-induced separation (§7.3).

**What the two studies share.** In both, whether and where the slant flow
separates changes with the near-wall treatment: the boundary condition
(wall law or no-slip) and the grid of the immersed boundary in
[Cai et al. (2022)](/sources/cai-2022.md), §IV; the turbulence model, the
prism layers, the surface-mesh size and the CFL number of the hybrid
simulation in [Delassaux et al. (2023)](/sources/delassaux-2023.md), §5;
see [hybrid RANS/LES](/definitions/hybrid-rans-les.md).

## Qualifications

- The two sources print different widths, 0.389 m
  ([Cai et al. (2022)](/sources/cai-2022.md)) and 380 mm
  ([Delassaux et al. (2023)](/sources/delassaux-2023.md)), with equal length
  and height; neither comments on it.
- [Cai et al. (2022)](/sources/cai-2022.md) were read in a HAL deposit of
  the typeset article. They use $z$ vertical and $y$ spanwise, raise the
  Mach number artificially (citing Fares) without quantifying its effect,
  and do not report near-wall resolution in wall units. Their claim that the
  wall-law boundary condition outperforms the no-slip one rests on velocity
  profiles, not on drag.
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) were read in a HAL
  author manuscript. Their Table 2 percentages for the two bodies with a
  rounded roof (0.7 and $-0.7$) are about twice those computed from the
  printed three-digit coefficients ($\pm0.34\%$), while the other six
  percentages of the table reproduce from the printed values *(compiler
  check, not in the sources)*. They do not give
  the Reynolds number or the source of the experimental data in this paper.

# Citations

- [Cai et al. (2022)](/sources/cai-2022.md) — §I; §II.C; §III, Tables I–II, Figs. 2–3; §IV, Table III, Figs. 4–9; §V.
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — §1; §4.4; §5, Table 2, Figs. 11–12; §7.3.
