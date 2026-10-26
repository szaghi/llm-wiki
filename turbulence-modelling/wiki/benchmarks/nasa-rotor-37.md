---
type: Benchmark
title: "NASA Rotor 37"
description: "The NASA Rotor 37 transonic axial-compressor rotor: a mesh-converged steady RANS benchmark of Spalart–Allmaras with anisotropic mesh adaptation against structured grids and experiment, and, unwound at mid-span into a linear cascade at ground idle, the application case of a GPU discontinuous Galerkin LES code."
status: established
aliases: [Rotor 37, NASA Rotor37, R37, Stage 37 rotor]
tags: [benchmark, turbomachinery, rans, mesh-adaptation, gpu, dg]
timestamp: 2026-10-26T15:57:00Z
---

# NASA Rotor 37

NASA Rotor 37 is the rotor of the transonic axial-compressor Stage 37, run
in isolation in the NASA rotor-alone experiment. As recalled by
[Alauzet et al. (2022)](/sources/alauzet-2022.md), §8.2, it has 36 blades
and runs at 17,188.7 rpm, with relative Mach numbers of 1.48 at the tip
and 1.13 at the hub, so leading-edge shocks stand in every passage, and the
measured data are performance characteristics (total-pressure and
total-temperature ratios and isentropic efficiency against mass flow) and
radial profiles at four stations, plus LDA maps of relative Mach number.
The flow combines shock–boundary-layer interaction, tip-leakage vortices,
hub-corner separation and, towards stall, tip separation. In this bundle
the rotor appears twice: as a full-rotor steady RANS case that tests
discretization error and mesh adaptation, and as a mid-span linear cascade
for scale-resolving simulation on GPUs.

## Configurations in the sources

| Item | [Alauzet et al. (2022)](/sources/alauzet-2022.md) | [Kurz et al. (2025)](/sources/kurz-2025.md) |
|---|---|---|
| Geometry | full rotor, one 10° sector with rotational periodicity; **cold** blade geometry regenerated from the NASA design code, with hub fillet, no hub cavity | mid-span blade profile unwound into a linear cascade, extruded by 5% of chord, one pitch, stagger 51.2° |
| Operating point | 23 points along the characteristic, outlet-to-inlet pressure ratio 1 to 1.300 | ground idle: tip Mach 0.824, total-pressure ratio 1.305 (design point: tip Mach 1.4939, ratio 2.106) |
| Flow parameters | inlet total pressure 101,325 Pa, total temperature 288.15 K | $Re=972{,}550$ on inflow velocity and chord, inlet relative Mach 0.758, incidence 10.1° to the mean camber line |
| Model | steady RANS, [Spalart–Allmaras](/methods/spalart-allmaras-model.md) without $f_{t2}$ and with QCR2000; no transition model | wall-resolved LES, split-form DGSEM (Pirozzoli flux), no explicit SGS model; [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md) |
| Discretization | vertex-centred second-order finite volume (HLLC, MUSCL) with P1 viscous terms, solver Wolf | $1.2\times10^6$ elements, $N=5$, $2.6\times10^8$ degrees of freedom; 14-stage fourth-order Runge–Kutta; sponge zones at inflow and outflow |
| Meshes | anisotropically adapted tetrahedra, about 0.36 to 11 million vertices; structured [elsA](/software/elsa.md) comparison on 3 to 32 million cells | one mesh |
| Reference | experiment (Suder); about 40 elsA runs | validation of the CPU code against experimental mid-span data in earlier work (not shown) |

## What the case tests

**Discretization error of steady RANS.**
[Alauzet et al. (2022)](/sources/alauzet-2022.md) run the rotor with
[mesh adaptation](/methods/mesh-adaptation.md) on purely tetrahedral
meshes, with feature-based ($L^4$ norm of the Mach number) and
goal-oriented (adjoint of the total-pressure ratio) error estimates, and
call a complexity converged when mass flow and pressure and temperature
ratios change by less than 1% over three adaptations (§3, §8.2.3).

- Mesh convergence is quick, a few hundred thousand vertices, from choke to
  near-peak efficiency (pressure ratio about 1.2) and harder towards stall;
  the total-temperature ratio converges everywhere with about half a
  million vertices (§8.2.4, Figs. 22–25). Goal-oriented adaptation
  converges earlier: the choke total-pressure ratio is within 0.1% of the
  finest reference after 0.5 million vertices, against 0.2–0.5% for
  feature-based adaptation (Fig. 32).
- Without exact differentiation of the rotating-frame wall condition the
  residual stalls and the pressure ratio oscillates and drops (§4.2.3,
  Fig. 2). Coarse adapted meshes diverge near a pressure ratio of 1.175,
  which motivates restarting each higher pressure ratio from the previous
  one (§3).
- Adapted meshes reach $y^+=1$ ahead of the shock and about 2 in the
  separated layer behind it, unchanged from 0.36 to 2.8 million vertices,
  without prismatic layers (§8.2.5, Fig. 40); see
  [boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md)
  for the opposite design choice.

Performance on about 5 million vertices against 7 million elsA cells
(Table 2):

| Run | choke mass flow | choke total-pressure ratio | peak efficiency | near-stall efficiency |
|---|---|---|---|---|
| adapted, feature-based | 20.58 | 1.904 | 0.874 | 0.854 |
| adapted, goal-oriented | 20.66 | 1.909 | 0.877 | 0.857 |
| elsA, structured | 20.71 | 1.965 | 0.860 | 0.830 |

The adapted solutions keep the induced tip vortex and the tip-leakage
vortex that globally refined structured meshes dissipate (Figs. 42–43),
and match the radial profiles near the end walls better; refining elsA
moves it towards the adapted solution (Fig. 31). Both their
total-pressure and total-temperature characteristics lie above the
experiment, "not in accordance with the literature", which generally lies
below; the authors attribute this to computing the cold rather than the hot
geometry, and the efficiency gap to elsA to "lack of resolution of the
non-adapted meshes", testing neither (§8.2.4). Near stall (93% of choke
mass flow) the hub-corner separation barely changes while the tip
separation and leakage grow, from which they infer that stall starts near
the tip (Fig. 41). Transition is not modelled because, as they recall
from LES, it occurs almost at the leading edge, triggered by the shocks
(§8.2). The authors propose comparing SA with
[$k$-$\omega$ SST](/methods/k-omega-sst-model.md) on such meshes once
discretization error is removed (§9). See also
[numerical dissipation](/properties/numerical-dissipation.md).

**A GPU LES of the mid-span cascade.**
[Kurz et al. (2025)](/sources/kurz-2025.md) (read in arXiv v2), §6, use
the unwound mid-span section as the application case of
[GALÆXI](/software/galaexi.md), the GPU port of [FLEXI](/software/flexi.md).
Far-field inflow, subsonic outflow, adiabatic walls, Sutherland's law,
periodic pitch and span; the run starts from a converged state and is
advanced 8 convective times. The subcell finite-volume blending is active
only near the near-normal leading-edge shock, with blending factors 0.1 to
0.7 there, so high order is kept in smooth regions (Fig. 13). Energy to
solution per convective time (Table 3):

| Code | ranks | degrees of freedom per rank | wall time per convective time | energy per convective time |
|---|---|---|---|---|
| GALÆXI, A100 GPUs | 128 | $2.03\times10^6$ | 9209 s | 147 kWh |
| FLEXI, CPU cores | 32,768 | $7.93\times10^3$ | 7538 s | 339 kWh |

The GPU run saves 56.8% of the energy (59.5% in the energy-normalized
performance index); power was measured rack-wise, including network
switches and, for the GPU system only, cooling, which the authors call a
rough estimate and a conservative lower bound (§6.3). GALÆXI's
performance index is about 35% worse here than in the periodic-box tests,
attributed to sponge zones, boundary conditions, the shock indicator,
finite-volume shock capturing and load imbalance. No turbulence statistics
are shown, only an instantaneous Mach field, and the near-wall resolution
in wall units is not printed.

## Qualifications

- The two configurations share only the blade: a full rotor in steady RANS
  at near-design speed against a two-dimensional extruded mid-span section
  at ground idle in LES. No source compares them.
- The design tip Mach number is printed as 1.48 (relative, as recalled by
  [Alauzet et al. (2022)](/sources/alauzet-2022.md)) and 1.4939
  ([Kurz et al. (2025)](/sources/kurz-2025.md)); neither defines the value
  further, so this is recorded as a difference in printing.
- The two sources cite different NASA reports for the stage: Alauzet et
  al. (ref. [60]) Reid & Moore (1978), NASA TP 1338, whose title gives a
  design pressure ratio of 1.82; Kurz et al. (ref. [60]) Moore & Reid
  (1980), NASA TP 1659, whose title gives 2.05. Kurz et al. print a design
  total-pressure ratio of 2.106 (§6). Neither source comments on the
  other report (see the [bibliography](/bibliography.md)).
- [Alauzet et al. (2022)](/sources/alauzet-2022.md) print a stall-row
  pressure ratio of 1.305 above the largest 1.300 of their lists, and say
  that complexities 40,000 and 80,000 diverge although their Rotor 37 list
  starts at 160,000; dividing their printed elsA mass flows by the elsA
  choke mass flow does not give the printed normalized values *(compiler
  check, not in the sources)*.

# Citations

- [Alauzet et al. (2022)](/sources/alauzet-2022.md) — §3; §4.2.3, Fig. 2; §8.2–8.2.6, Tables 2–3, Figs. 22–43; §9.
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv v2: §6.1–6.3, Table 3, Figs. 12–13.
