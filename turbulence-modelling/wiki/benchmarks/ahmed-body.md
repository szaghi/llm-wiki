---
type: Benchmark
title: "Ahmed body"
description: "The Ahmed body, a bluff car-like body with a slanted rear whose angle sets the separation regime: at 35° a test of immersed-boundary wall-modelled LES and of SST-based hybrid RANS/LES on lattice Boltzmann grids, at 25° the calibration case of a DDES procedure and a generalization test of symbolic-regression RANS corrections."
status: established
aliases: [Ahmed car body, Ahmed reference model, 25° Ahmed body, 35° Ahmed body]
tags: [benchmark, separated-flow, hybrid-rans-les, des, wmles, immersed-boundary, lattice-boltzmann, field-inversion]
timestamp: 2026-10-27T15:50:00Z
---

# Ahmed body

The Ahmed body is a simplified road-vehicle shape: a block with a rounded
front, a slanted upper rear surface of angle $\varphi$ (page-local) and a
vertical base, mounted on four cylindrical stilts above a ground plane. It
is about 1.04 m long and 0.29 m high. The flow stays attached over the
front and roof and separates at the rear, and the slant angle sets the
regime: [Cai et al. (2022)](/sources/cai-2022.md), §I and §V, citing
earlier work, state that drag
falls sharply ("drag crisis") above about 30°, where the flow separates
massively from the upstream edge of the slant, while at 25° the shear layer
separates and reattaches on the slant, a regime that the authors leave as a
challenge for future work. The quantities compared are the drag
and lift coefficients $C_D$ and $C_L$, the pressure on the slant and base,
and velocity profiles over the slant and in the wake. In this bundle the
case tests near-wall treatments of scale-resolving simulation on a separated
bluff body: immersed-boundary wall-modelled LES and the choice of hybrid
RANS/LES model. It is also a three-dimensional generalization test of
data-driven RANS corrections trained on two-dimensional flows.

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

[Wu et al. (2025)](/sources/wu-2025.md), §4.4, run the 25° body as a
half model at a Reynolds number of $2.78\times10^6$ on the body length,
$U_\infty=40$ m/s, with steady RANS (OpenFOAM simpleFoam) on three
structured meshes of about $3.6\times10^6$, $7.2\times10^6$ and
$1.4\times10^7$ cells, against the PIV of Lienhart et al. This length-based
value corresponds to $Re_H\approx7.67\times10^5$ with the printed length
and height of the other sources *(compiler check, not in the sources)*.

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

**SST-based hybrids with and without the wall model.**
[Mozaffari et al. (2024)](/sources/mozaffari-2024.md), §3.3, run the
same geometry ($1044\times389\times288$ mm, $U_\infty=40$ m/s,
$Re_H=7.68\times10^5$, ERCOFTAC domain $8L\times2L\times1.35L$) in the
same code, [ProLB](/software/prolb.md), but replace the subgrid model by
two hybrids built on [$k$-$\omega$ SST](/methods/k-omega-sst-model.md):
SST-IDDES ([detached-eddy simulation](/methods/detached-eddy-simulation.md))
and Heinz's [continuous eddy simulation](/methods/continuous-eddy-simulation.md)
(CES, see also [hybrid RANS/LES](/definitions/hybrid-rans-les.md)). The grid has 7
refinement levels, $\Delta x_{\min}=1.3$ mm, $45.8\times10^6$ nodes for
both slant angles, with more than 100 flow-through times $H/U_\infty$ and
the last 50 averaged. Two body-surface conditions are compared: the explicit
[equilibrium wall model](/methods/equilibrium-wall-model.md) of Cai &
Sagaut ("WM") and a zero-velocity Dirichlet condition imposed although
$y^+\gg1$ ("NS"; $y^+\approx100$–$150$ on the slant).

- With the wall model, neither hybrid separates on the slant at either
  angle, contrary to the fully detached 35° reference flow (Fig. 16). The
  authors attribute it to the equilibrium wall model, which has no
  pressure-gradient term, delaying or suppressing separation in the mild
  adverse pressure gradient, and to the missing instability on the slant,
  which keeps the hybrid from switching to LES (lines 465–470, 516–519).
- With the no-slip condition, IDDES at 35° reproduces the reference wake
  topology, including a small recirculation near the end of the slant also
  seen in the body-fitted IDDES of Guilmineau et al., with a recirculation
  extending just over 200 mm as in the experiment (Figs. 18–19). CES
  separates already on the roof, and its separation extends into the wake
  (Figs. 17, 19, 20).
- At 25° IDDES-NS separates late and does not reattach, which the authors
  attribute to the $y^+\approx100$–$150$ resolution on the slant
  (Figs. 22–24).
- The authors report "primary findings", without data, that the
  adverse-pressure-gradient wall model of Wilhelm et al. improves the
  results substantially (lines 553–557); see
  [wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md).

Drag coefficients of [Mozaffari et al. (2024)](/sources/mozaffari-2024.md),
Table 3:

| Run | $C_D$, 35° | $C_D$, 25° |
|---|---|---|
| IDDES-WM | 0.2878 | 0.2510 |
| CES-WM | 0.2738 | — |
| IDDES-NS | 0.2819 | 0.2970 |
| CES-NS | 0.3779 | — |
| experiment, Ahmed et al. ($Re_H=1.2\times10^6$) | 0.2580 | 0.2850 |
| experiment, Meile et al. ($Re_H=7.68\times10^5$) | 0.2790 | 0.2990 |
| experiment, Liu et al. ($Re_H=1.4\times10^5$) | 0.32 | — |
| experiment, Thacker et al. ($Re_H=1.4\times10^5$) | — | 0.3840 |
| body-fitted SST-NS / IDDES-NS (Guilmineau et al.) | 0.2999 / 0.3452 | 0.3218 / 0.3802 |

The 35° literature values quoted by both ProLB studies agree: Meile et
al. 0.279, Liu et al. 0.32, Guilmineau et al. SST 0.2999 and IDDES 0.3452
([Cai et al. (2022)](/sources/cai-2022.md), Table III;
[Mozaffari et al. (2024)](/sources/mozaffari-2024.md), Table 3); Ahmed et
al. is printed 0.26 and 0.2580. The 25° IDDES-NS drag (0.2970) lies within
0.002 of Meile et al. (0.2990) *(compiler check, not in the sources)*,
although its slant flow does not reattach (Figs. 22–24). The authors state that IDDES-NS "could
recover" the 35° WMLES solution of [Cai et al. (2022)](/sources/cai-2022.md)
at lower cost, without giving cost figures (lines 510–515).

**Choice of hybrid model at 25°.**
[Delassaux et al. (2023)](/sources/delassaux-2023.md), §5, recapitulate
their earlier calibration on the four 25° bodies: the realizable
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

**Data-driven RANS corrections at 25°.**
[Wu et al. (2025)](/sources/wu-2025.md), §4.4, use the 25° body as an
"L3" test, a separation mechanism like the training flows with a different
geometry and Reynolds number, for two
[symbolic-regression](/methods/symbolic-regression-closure.md) corrections
of the $\omega$-destruction term of
[$k$-$\omega$ SST](/methods/k-omega-sst-model.md), trained on
[field-inversion](/methods/field-inversion-machine-learning.md) data of a
curved backward-facing step and the
[NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md): SR-CLS
(classic inversion) and SR-CND (inversion gated by the DDES shielding
function, so that the correction vanishes in attached boundary layers).
Baseline SST predicts "a large separation starting from the beginning of
the slant"; both corrected models keep the flow "attached all along the
slant, agreeing with the experiment" (Fig. 45). Both raise the correction
$\beta$ in the separated shear layers from the upper and lower surfaces;
near the slant only SR-CLS raises it at the wall (Fig. 44). Velocity-profile
error against the PIV, normalized by $U_\infty$, on the fine mesh
(Table 7):

| Model | error | relative to SST |
|---|---|---|
| SST | 0.677 | 100.0% |
| SR-CND | 0.072 | 10.6% |
| SR-CLS | 0.069 | 10.2% |

The corrected models change $C_D$ by about 0.005 from the coarse to the
medium mesh and by 0.001–0.002 from medium to fine, while the SST drag
"fluctuates" with refinement (Fig. 42); no drag values are printed for the
Ahmed body. Steady RANS with an eddy-viscosity closure is thus the third
modelling route on this page, next to wall-modelled LES and hybrid RANS/LES.

**What the two studies share.** In both, whether and where the slant flow
separates changes with the near-wall treatment: the boundary condition
(wall law or no-slip) and the grid of the immersed boundary in
[Cai et al. (2022)](/sources/cai-2022.md), §IV; the turbulence model, the
prism layers, the surface-mesh size and the CFL number of the hybrid
simulation in [Delassaux et al. (2023)](/sources/delassaux-2023.md), §5;
see [hybrid RANS/LES](/definitions/hybrid-rans-les.md). In
[Mozaffari et al. (2024)](/sources/mozaffari-2024.md), §3.3, it changes
with the body-surface condition (equilibrium wall model or no-slip) and
with the hybrid model (IDDES or CES) at a fixed grid.

The two ProLB studies differ on the wall-model runs at 35°: the fine-grid
Vreman WMLES of [Cai et al. (2022)](/sources/cai-2022.md) separates
massively with the wall law, while the SST hybrids of
[Mozaffari et al. (2024)](/sources/mozaffari-2024.md) with an explicit
equilibrium wall model that both papers credit to Cai & Sagaut (printed
with different constants; see [law of the wall](/definitions/law-of-the-wall.md))
do not separate. The runs differ in turbulence model and near-wall eddy
viscosity (constrained-LES eddy viscosity against SST-based IDDES and CES),
and neither paper sets the two outcomes side by side; Mozaffari et al. cite
Cai et al. for the statement that the equilibrium wall model is acceptable
in fully separated flows (lines 149–152).

## Qualifications

- [Wu et al. (2025)](/sources/wu-2025.md) were read in the authors' Word
  manuscript. The caption of their Table 7 says "MSEs", the text "mean
  square error", and the row label "RMSE"; the metric is ambiguous. The
  caption of Fig. 44 names the classic-inversion model "SST-CLS" for
  SR-CLS. Their slant-flow statement rests on the streamline plots of
  Fig. 45.

- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) were read in the
  HAL accepted manuscript. Their no-slip runs impose a zero velocity at
  $y^+\approx100$–$150$, an under-resolved wall condition. The conclusion
  (lines 557–558) calls it a "non-zero Dirichlet velocity", while §3.3
  (lines 475–476) and the caption of Table 3 call it "zero-velocity" and
  "zero-Dirichlet". Lines 535–536 call the "lift and drag coefficients"
  close to the references, but Table 3 gives only drag.

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

## Contradictions

- **Topology of the mean slant flow of the 25° body.** *Open.*
  [Wu et al. (2025)](/sources/wu-2025.md), §4.4 and Fig. 45, state that in
  the experiment (Lienhart et al. PIV) the flow "remains attached all along
  the slant", and credit their corrected RANS models for reproducing it.
  [Cai et al. (2022)](/sources/cai-2022.md), §I and §V, citing earlier
  work, state that the
  25° shear layer separates and reattaches on the slant, and
  [Delassaux et al. (2023)](/sources/delassaux-2023.md), §5, recapitulating
  their earlier paper, find the hybrids that separate and reattach (SAS,
  DDES, SBES) closer to their experiment than the realizable
  $k$-$\varepsilon$ model, which does not separate on the slant, with DDES
  closest. Wu et al. describe the Lienhart et al. PIV; Cai et al. describe
  the 25° regime without naming a data set; Delassaux et al. compare with
  their own experiment on four edge variants and do not name it in this
  paper.

# Citations

- [Cai et al. (2022)](/sources/cai-2022.md) — §I; §II.C; §III, Tables I–II, Figs. 2–3; §IV, Table III, Figs. 4–9; §V.
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — §1; §4.4; §5, Table 2, Figs. 11–12; §7.3.
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §2.2; §3.3, Table 3, Figs. 16–24; §4.
- [Wu et al. (2025)](/sources/wu-2025.md) — author manuscript: §1, Table 1 (L1–L4 levels); §4.4, Figs. 41–45, Table 7.
