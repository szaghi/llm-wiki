---
type: Software
title: "elsA"
description: "ONERA's compressible cell-centred finite-volume solver for structured multi-block grids, as used in the sources: host of the zonal detached-eddy simulation of a turbofan fan stage, and the structured Spalart–Allmaras RANS reference against which mesh-adaptive RANS of NASA Rotor 37 is compared."
status: established
aliases: [elsA solver, ONERA elsA]
tags: [software, rans, des, turbomachinery, hybrid-rans-les]
timestamp: 2026-10-25T19:45:00Z
---

# elsA

**elsA** is ONERA's compressible finite-volume flow solver. Both sources
that use it describe it as cell-centred on structured multi-block grids,
with the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md) as the
RANS closure in their runs
([François et al. (2022)](/sources/francois-2022.md), §3.5;
[Alauzet et al. (2022)](/sources/alauzet-2022.md), §8.2.2). It hosts the
[zonal detached-eddy simulation](/methods/detached-eddy-simulation.md) of
Deck, "implemented in elsA" as recalled by François et al. (§3.1). The
sources use it in two roles: a scale-resolving production code for a fan
stage, and a structured-grid RANS baseline in turbomachinery.

## Numerics, as configured in the sources

The two configurations differ; each is the setting of one study, not a
default of the code.

| Item | François et al. (2022), ZDES of a fan stage | Alauzet et al. (2022), RANS of Rotor 37 |
|---|---|---|
| Convective flux | AUSM with a third-order limiter | Roe with the Van Albada limiter |
| Time integration | implicit second order, Newton algorithm with 5 sub-iterations (residuals down by one order) | implicit backward Euler, CFL ramped from 0.95 to 10 |
| Turbulence model | SA (URANS zones), ZDES mode 2 with SA | "standard" SA, adiabatic walls |
| Grids | structured multi-block, 380 million cells | structured meshes of 3, 7, 16 and 32 million cells from Autogrid |

(François et al. §3.5; Alauzet et al. §8.2.2.) Alauzet et al. do not state
whether the quadratic constitutive relation they use in their own solver
was also active in the elsA runs; they write only "the standard
Spalart-Allmaras model".

**Rotor–stator coupling.** For the fan–outlet-guide-vane stage a sliding-mesh
interface couples the rotating and fixed frames: the donor-grid state is
interpolated onto the receiving grid and a half-sum of donor and receiver
cells is taken on the conservative variables. Interpolation errors at this
interface, which produced spurious noise sources in the authors' 2020
simulation, were corrected in elsA and "have now fully disappeared"
(François et al. 2022, §3.3). Fan-wake vorticity crosses the interface and
the periodic boundaries "without noticeable attenuation or numerical
artefact" (§4.2, Figs. 8–9, qualitative).

## Uses in the sources

**ZDES of the ACAT1 fan stage** (François et al. 2022). URANS in the core
flow and upstream of the fan, ZDES mode 2 in the bypass, one fan and two
outlet-guide-vane channels (vane count changed from 44 to 40 at constant
solidity for periodicity). Time step $3.2\times10^{-7}$ s (48 000 steps per
revolution); convective CFL about 36 in the smallest wall cells and 0.35 in
the 0.5 mm free-shear cells; 28 nodes, 672 cores, 2 million CPU hours for
nearly four revolutions (§3.4–3.5). Global performance agrees with the rig
within 0.4% (Table 1). Results are on the
[detached-eddy simulation](/methods/detached-eddy-simulation.md) page.

**Structured RANS reference for NASA Rotor 37** (Alauzet et al. 2022). About
40 elsA simulations on four structured meshes are compared with
mesh-adaptive SA-QCR2000 RANS on tetrahedral meshes of the authors' solver
Wolf ([mesh adaptation](/methods/mesh-adaptation.md)). On meshes of about 5
million vertices (adapted) against 7 million cells (elsA), Table 2 gives at
choke a total-pressure ratio of 1.904–1.909 (adapted) against 1.965 (elsA),
and an isentropic efficiency of 0.874–0.877 (adapted) against 0.860 (elsA)
at peak efficiency and 0.854–0.857 against 0.830 near stall. Refined
globally, the structured meshes dissipate the induced tip vortex and weaken
the tip-leakage vortex downstream, which the adapted meshes keep (§8.2.5,
Figs. 42–43); refining elsA moves its radial profiles towards the adapted
solution near the endwalls (§8.2.4, Fig. 31). The authors attribute the
efficiency gap to the "lack of resolution of the non-adapted meshes"; their
total-pressure and total-temperature characteristics lie above the experimental data, against the
literature they cite, which they attribute mainly to computing the cold
instead of the hot blade geometry (§8.2.4). Neither attribution is tested.

## Qualifications

- *Compiler check, not in the sources:* in Alauzet et al.'s Table 2 the
  normalized mass flow MFR/MFR* of the elsA rows does not follow from the
  printed MFR divided by the printed choke value 20.71 (20.46/20.71 = 0.988
  against the printed 0.980; 18.86/20.71 = 0.911 against 0.925), whereas the
  rows of the adapted runs agree within 0.002; either the elsA reference
  mass flow differs from the printed choke value or the column is
  inconsistent.
- Alauzet et al. print the mesh generator as "Autrogrid" (§8.2.2).

# Citations

- [François et al. (2022)](/sources/francois-2022.md) — §3.1, §3.3, §3.4–3.5, §4.2 Figs. 8–9, Table 1.
- [Alauzet et al. (2022)](/sources/alauzet-2022.md) — §8.2.2, §8.2.4 Fig. 31, §8.2.5 Figs. 42–43, Table 2.
