---
type: Benchmark
title: "NASA Juncture Flow"
description: "The NASA Juncture Flow wing–fuselage model, with smooth-body corner separation at the wing-root trailing edge at crank-chord Reynolds number 2.4 million, Mach 0.189 and 5° incidence, on which wall-modelled LES predicts wall pressure within 5% but mean velocity only within 3–8% on the fuselage and about 100% in the separated corner."
status: established
aliases: [Juncture Flow experiment, NASA JF, wing-body juncture flow]
tags: [benchmark, wmles, separated-flow, boundary-layer]
timestamp: 2026-10-25T13:30:00Z
---

# NASA Juncture Flow

The NASA Juncture Flow experiment is a full-span wing–fuselage model whose
wings are truncated DLR-F6-based wings with a leading-edge horn at the root,
tested in the NASA Langley 14×22-ft wind tunnel. At the wing–body juncture
near the trailing edge the flow separates in the corner from a smooth
surface, a three-dimensional separation that RANS models predicted poorly
in the Drag Prediction Workshops (as recalled by
[Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), §I). The data
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

Cost and error models built on this case are on
[grid-point requirements](/results/les-grid-point-requirements.md) and
[boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md).
As recalled by [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md), §I, the
classifier-plus-predictor machine-learning wall model of Lozano-Durán & Bae
was tested on this case and performed poorly in the separation zones (see
[machine-learning wall models](/methods/machine-learning-wall-model.md)).

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

# Citations

- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §I, §II.A–B, §III.A, §V.A–F, Figs. 3–22.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §I (recalled result).
