---
type: Benchmark
title: "NASA Juncture Flow"
description: "The NASA Juncture Flow wing–fuselage model, with smooth-body corner separation at the wing-root trailing edge (crank-chord Reynolds number 2.4 million, Mach 0.189, 5°): wall-modelled LES predicts wall pressure within 5% but mean velocity only within 3–8% on the fuselage and about 100% in the corner, which a learned wall model does not fix."
status: established
aliases: [Juncture Flow experiment, NASA JF, wing-body juncture flow]
tags: [benchmark, wmles, separated-flow, boundary-layer, data-driven]
timestamp: 2026-10-29T10:03:00Z
---

# NASA Juncture Flow

The NASA Juncture Flow experiment is a full-span wing–fuselage model whose
wings are truncated DLR-F6-based wings with a leading-edge horn at the root,
tested in the NASA Langley 14×22-ft wind tunnel. At the wing–body juncture
near the trailing edge the flow separates in the corner from a smooth
surface, a three-dimensional separation that RANS models predicted poorly
in the Drag Prediction Workshops, which
[Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), §I, cite. The data
set (velocity profiles, Reynolds stresses, surface pressure, oil-film
visualization; no skin friction) makes the case a quantitative test of
[wall-modelled LES](/methods/wall-modelled-les.md) in a flow with corner
effects, adverse pressure gradient and separation.

## Configuration

From [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), §II.A:

- wingspan 3397.2 mm, fuselage length 4839.2 mm, crank chord (at the
  Yehudi break) 557.1 mm, the reference length of the Reynolds number;
- $Re_c=2.4\times10^6$ on the crank chord, $M=0.189$, temperature 288.84 K,
  dynamic pressure 2476 Pa, angle of attack $5^\circ$;
- sting and mast omitted ("free air"); domain about five fuselage lengths in
  each direction, plug inflow, non-reflecting characteristic outflow,
  free-slip lateral boundaries;
- wing tripping by displacing surface-mesh points by $\pm1$ mm near the
  leading edge along the experimental trip lines; the fuselage transitions
  naturally; dot tripping changed little at the juncture.

Three measurement stations are used: (1) on the fuselage, (2) in the
wing–body juncture and (3) in the separated region at the wing-root trailing
edge, plus surface pressure at four spanwise stations, including one near
the wing tip.

## Runs

All runs use [CharLES](/software/charles.md) with the dynamic Smagorinsky
model and an algebraic [equilibrium wall model](/methods/equilibrium-wall-model.md)
($\kappa=0.41$, $B=5.2$, matched at the first off-wall cell centre). Two grid
families are compared (§V.A):

| Case | Strategy | Near-wall size or parameters | Cells | Core-hours |
|---|---|---|---|---|
| C-D7, C-D4, C-D2 | constant size, whole surface | 6.7, 4.3, 2.2 mm | 14, 17, 31 M | 31k, 40k, 75k |
| C-D1, C-D0.5 | constant size, refined box at the juncture | 1.1, 0.5 mm | 50, 174 M | 116k, 398k |
| C-N5-R2e3 | [boundary-layer conforming](/methods/boundary-layer-conforming-grid.md) | 5 points per $\delta$, minimum grid Reynolds number $2.8\times10^3$ | 12 M | 27k |
| C-N10-R2e3 | boundary-layer conforming | 10 points per $\delta$, $2.8\times10^3$ | 40 M | 90k |
| C-N5-R5e3 | boundary-layer conforming | 5 points per $\delta$, $5.6\times10^3$ | 6 M | 13k |

Core-hours are on Intel Xeon E5-2670 processors (NASA Pleiades). The local
$\delta$ for the conforming grids comes from the departure of a WMLES mean
velocity from an inviscid solution; it grows from about zero at the wing
leading edge to about 30 mm at the wing trailing edge and above 50 mm on the
aft fuselage.

## Results

From [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), §V:

- **Wall pressure.** $C_p$ is within 5% on all grids, even with 0–1 points
  per boundary-layer thickness, and a free-slip inviscid run gives nearly the
  same $C_p$. The authors explain this by the outer-layer, inviscid nature of
  the wall pressure under the thin-boundary-layer approximation. Residual
  errors concentrate at the wing leading edge and the wing tip, where the
  error scales linearly with grid size (§V.E, Figs. 20–21).
- **Mean velocity.** Errors are about 3–8% on the fuselage, converging
  linearly in $\Delta/\delta$ ($\Delta$ the isotropic cell size) with a constant about 0.14 (against 0.08 in
  [channel flow](/benchmarks/turbulent-channel-flow.md)); about 15% at the
  juncture, converging with exponent about 0.4; about 100% at the separated
  trailing edge, with exponent about 0.6. The constant-size grids put 30–80
  points per $\delta$ at the juncture, an order of magnitude more than on the
  fuselage, yet are least accurate there (§V.B, Fig. 15).
- **Grid strategy.** The 12 M-cell conforming grid beats the 31 M-cell
  constant-size grid at the juncture and the trailing edge; conforming grids
  lower the error constant, not the convergence rate. The authors trace the
  advantage to errors generated at the under-resolved leading edge and
  advected downstream over about $300\delta_0$ ($\delta_0$ the boundary-layer
  thickness where the error originates), and collapse the fuselage
  errors onto the channel calibration with an upstream-averaged boundary-layer
  thickness (§V.C, Figs. 16–17).
- **Separation.** The predicted bubble is about 100 mm long and 60 mm wide
  (C-D0.5), about 15% smaller than the oil-film footprint (120×80 mm),
  consistent with earlier WMLES; the authors caution that the two measures
  are not one-to-one comparable (§V.F, Fig. 22).
- **Reynolds stresses.** Resolved stresses follow the experimental trends
  but are under-predicted at the juncture and trailing edge, as expected
  when the subgrid contribution is not added (§V.B).

**A machine-learning wall model on the same case.**
[Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md), §4.8, Table 1,
Fig. 18, run the [building-block-flow wall model](/methods/building-block-flow-wall-model.md)
(a classifier of seven canonical flow types plus one network per type,
trained on wall-modelled LES of those flows) against the algebraic
equilibrium wall model, both with the dynamic Smagorinsky model in
CharLES, on a boundary-layer-conforming grid with 5 points per $\delta$, at
$Re=2.4\times10^6$ on the Yehudi-break chord and $5^\circ$, against the
experiment of Kegerise et al. Per station:

| Station | Classification by the model | Confidence | Outcome |
|---|---|---|---|
| upstream fuselage ($x=1168.4$ mm) | 88% zero pressure gradient, 12% favourable | 98% | errors below 2% for both wall models |
| wing–body juncture ($x=2747.6$ mm) | 52% adverse pressure gradient, 41% zero, 7% separation | 82% | the learned model better, through a larger wall stress that decelerates the flow |
| trailing-edge corner separation ($x=2922.6$ mm) | 56% separation | 22% | the learned model better but "far from satisfactory" |

The separation bubble at the trailing edge is about $0.3\delta$ thick on a
grid with $\Delta\approx0.2\delta$, one point across the bubble, and the
authors attribute the remaining error there to the SGS model rather than
the wall model (§4.8). They state, without side-by-side numbers, that this
version is more accurate on the case than their preliminary version of
2020 trained on filtered DNS. Vadrot et al. (2023b) cite a result on this case (below); the work
they cite (their ref. [85]) is the 2020 arXiv preprint of the preliminary
version (Lozano-Durán & Bae 2020). The model was never trained on wing or aircraft flows
(§2.3).

Cost and error models built on this case are on
[grid-point requirements](/results/les-grid-point-requirements.md) and
[boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md).
[Vadrot et al. (2023b)](/sources/vadrot-2023-b.md), §I, cite the result that the
classifier-plus-predictor machine-learning wall model of Lozano-Durán & Bae
was tested on this case and performed poorly in the separation zones (see
[machine-learning wall models](/methods/machine-learning-wall-model.md)).

## As a precedent in an aircraft-workshop assessment

[Kiris et al. (2023)](/sources/kiris-2023.md), summarizing the
wall-modelled LES of the [NASA CRM-HL](/benchmarks/nasa-crm-high-lift.md)
at the Fourth High-Lift Prediction Workshop, use this case as the
precedent for judging scale-resolving simulations by pressure rather than
by velocity profiles (§I). For the Juncture Flow experiment, whose laser
Doppler velocimetry gives velocity profiles, LES needed substantial grid
resolution to approach the measurements (they cite the LAVA and CharLES
studies of their refs. [9]–[11], [23]), and the LDV data encouraged WMLES
on grids "at least 4× finer" in some cases to study convergence in
velocity (§VI 5a). Corner-flow RANS closures (the QCR improvements of
their ref. [24]) left errors of order one in the mean velocity inside the
juncture separation, yet captured the surface topology of the separation
and gave very accurate mean $C_p$ (§I). They also cite juncture-flow
WMLES in which grids of aspect ratio one at the juncture gave the most
accurate corner flow (their ref. [11], §I.2), and recommend LDV- and
PIV-type velocity measurements "as was done in experiments like wing–body
juncture flow" for future high-lift tests (§VI 5a). In the runs of
Lozano-Durán et al. (2022) above, $C_p$ is within 5% on all grids while
the velocity error is about 15% at the juncture and about 100% in the
separation.

## Junction flows as a RANS modelling challenge

The Juncture Flow model belongs to a wider class:
[Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md), §2.1, list junction
flows (finite objects protruding from a surface) among the "completely
statistically three-dimensional" flows for which an eddy-viscosity closure
is "even more ill-suited" (see
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)). The review
does not mention the NASA model; the data-driven junction-flow work it cites
(§4.1) is on [symbolic-regression closures](/methods/symbolic-regression-closure.md).

[Devenport & Lowe (2022)](/sources/devenport-2022.md), §5.1, name the
Juncture Flow test (citing Rumsey) together with an earlier wing–body
junction study as examples of **pressure-driven three-dimensional
turbulent boundary layers**: the fuselage boundary layer approaching the
wing is turned by a lateral pressure gradient, and streamwise vorticity is
generated at the wall by that gradient acting with viscosity. Their
review of such layers (§5.4; see
[turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md)) rests
on the attached endwall layer of a wing–body junction of Ölçmen & Simpson,
a different geometry: there the direction of the turbulent shear stress
lags the direction of the mean velocity gradient, and Townsend's
structure parameter $A_1$ (page-local: the shear-stress magnitude over
twice the turbulent kinetic energy) falls below its two-dimensional value,
both of which the authors trace to a suppressed pressure–strain source of
$\langle v'v'\rangle$ (Lowe & Simpson's pressure–strain measurements at
$Re_\theta=7500$). An isotropic eddy viscosity forces the two directions
to coincide, which the authors present as a challenge "both in RANS and
wall-modeled LES" (§5.1, §5.4; see
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)). The
review shows no Juncture Flow data.

## Qualifications

- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) use an aircraft
  frame ($x$ along the fuselage from the nose, $y$ spanwise, $z$ vertical),
  not the wall frame of the registry; station coordinates are quoted in that
  frame on their Source page.
- The version read (arXiv v1) prints the minimum grid Reynolds numbers of
  C-N5-R2e3 and C-N5-R5e3 as $2.6\times10^3$ and $5.8\times10^3$ in §V.D,
  against $2.8\times10^3$ and $5.6\times10^3$ in §V.A, the Fig. 18 caption
  and the case names; and it announces "six" constant-size cases in §V.A
  while listing five.
- Averaging times are not printed.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) state the
  reference length as the chord at the Yehudi break, the same crank chord
  as Lozano-Durán et al. (2022), and use the same aircraft frame for their
  station coordinates; their runs are a single grid, not a convergence
  study.
- [Devenport & Lowe (2022)](/sources/devenport-2022.md) cite the Juncture
  Flow test only as an example; the wing–body junction data they discuss
  are those of Ölçmen & Simpson and Lowe & Simpson, not of this model.
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) do not mention
  the NASA Juncture Flow model; their junction-flow statements concern the
  class of flows and other geometries (a junction body, a wall-mounted
  cube), not this case.

# Citations

- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §I, §II.A–B, §III.A, §V.A–F, Figs. 3–22.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §I (cited result).
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §2.3; §4.8, Table 1, Fig. 18.
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §2.1 (junction flows as a class; passing mention, the NASA model is not discussed); §4.1.
- [Devenport & Lowe (2022)](/sources/devenport-2022.md) — §5.1, §5.4, Figs. 39, 41 (pressure-driven 3D boundary layers; Juncture Flow cited as an example).
- [Kiris et al. (2023)](/sources/kiris-2023.md) — §I, §I.2; §VI 5a (cited results; the case as precedent for pressure-based assessment).
