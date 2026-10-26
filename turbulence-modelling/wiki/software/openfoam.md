---
type: Software
title: "OpenFOAM"
description: "OpenFOAM is the open-source unstructured finite-volume toolbox that many bundle sources use as baseline RANS solver for data-driven closures, as second-order LES solver and as host of in-house solvers; this page records the solvers, schemes and versions they report and what the comparisons with high-order codes say about its dissipation."
status: established
aliases: [OpenFOAM, simpleFoam, pimpleFoam, DAFoam]
tags: [software, rans, les, data-driven, numerical-dissipation]
timestamp: 2026-10-26T15:52:00Z
---

# OpenFOAM

**OpenFOAM** is an open-source C++ toolbox for unstructured, cell-centred
finite-volume solution of the flow equations. Rismondo et al. (2025) cite it
to Weller et al. (1998). In this bundle it is never the subject of a study.
It runs the baseline RANS of several
data-driven closure papers, the second-order LES that high-order codes are
compared against, and the base of in-house and adjoint solvers. Every
source reports its own solver application, schemes and version. None of
these is a default of the code.

## Solvers and schemes as reported

| Source | Application | Pressure–velocity coupling and schemes | Version |
|---|---|---|---|
| [Rismondo et al. (2025)](/sources/rismondo-2025.md), §2.1 | incompressible LES in a multiple reference frame, [WALE](/methods/wale-model.md) | PISO with two correctors and two non-orthogonal correctors; second-order backward time, Gauss linear (central) space; bi-conjugate gradient for momentum, GAMG for pressure | not printed |
| [Saini et al. (2023)](/sources/saini-2023.md), §2.1 | incompressible LES, WALE ($C_w=0.325$) | `pimpleFoam`, second order | v1712 |
| [Wu et al. (2025)](/sources/wu-2025.md), §2–§3 | steady incompressible RANS, [SST](/methods/k-omega-sst-model.md) | `simpleFoam`; discrete adjoint by DAFoam, Jacobians by automatic differentiation (CoDiPack) | not printed |
| [Oulghelou et al. (2025)](/sources/oulghelou-2025.md), §4.1 | steady RANS, SST with blended learned corrections (modified solver) | SIMPLE, linear upwind convection, second-order central viscous terms, Gauss–Seidel smoother | "v23-06" in the text, "Version 10" in the reference list |
| [Tang et al. (2023)](/sources/tang-2023.md), §III | steady RANS, [$k$-$\varepsilon$](/methods/k-epsilon-model.md) with a frozen learned anisotropy | SIMPLE, second-order upwind convection, central otherwise | not printed |
| [McConkey et al. (2022)](/sources/mcconkey-2022.md) | RANS, $k$-$\varepsilon$-$\varphi$-$f$ elliptic relaxation | not printed | v2006 |
| [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md), §3.2 | standard $k$-$\varepsilon$ RANS (`simpleFoam`); WALE LES reference | not printed | not printed |
| [Liu et al. (2024)](/sources/liu-2024.md) | SSG/LRR-$\omega$ [Reynolds-stress model](/methods/reynolds-stress-model.md) coupled to Menter's $\gamma$ model | time-averaged URANS for the 3D cascades, first-order upwind for the turbulence variables and $\gamma$ | not printed |

## Roles in the bundle

**Baseline solver of data-driven RANS closures.** The learned corrections
of [field inversion and machine learning](/methods/field-inversion-machine-learning.md),
[symbolic-regression closures](/methods/symbolic-regression-closure.md),
[tensor-basis](/methods/tensor-basis-neural-network.md) and probabilistic
closures are trained and tested in OpenFOAM by several authors:

- Wu et al. (2025) invert a conditioned correction field on the SST
  $\omega$ destruction with DAFoam's discrete adjoint and SLSQP. They then
  test symbolic-regression models in `simpleFoam` on the
  [periodic hill](/benchmarks/periodic-hill.md), the
  [NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md), a
  flat plate, the [NACA 0012](/benchmarks/naca-0012-airfoil.md), an SAE
  notchback and the [Ahmed body](/benchmarks/ahmed-body.md). The 3D runs
  use half models of up to $3.3\times10^7$ (notchback) and
  $1.4\times10^7$ (Ahmed) cells (§3, Tables 6–7).
- Oulghelou et al. (2025) blend learned SST corrections inside a modified
  solver ([aggregation of data-driven models](/methods/turbulence-model-aggregation.md)),
  on 2D steady cases including the NASA hump and the NACA 0012. They state
  that the grids are fine enough for the discretization error to be
  negligible against the model effect, and show no grid study (§4.1).
- Tang et al. (2023) and McConkey et al. (2022) inject frozen learned
  anisotropies into the $k$-$\varepsilon$ and $k$-$\varepsilon$-$\varphi$-$f$
  solvers on the periodic hill. Agrawal & Koutsourelakis (2024) train on a
  [backward-facing step](/benchmarks/backward-facing-step.md), with OpenFOAM
  WALE LES as reference data (1,428,920 degrees of freedom).
- Liu et al. (2024) implement the SSG/LRR-$\omega$ model with Menter's
  one-equation $\gamma$ model in OpenFOAM, and test it on the
  [ERCOFTAC T3](/benchmarks/ercoftac-t3-flat-plate.md) plates and on
  [compressor cascades](/benchmarks/compressor-cascade.md) (see
  [local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)).

**Second-order LES and its dissipation.** Saini et al. (2023) give the
sharpest quantitative statement on OpenFOAM's numerical dissipation in
LES. On the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) the
discretization supplies 65–75% of the non-viscous dissipation in OpenFOAM,
against 85–95% in [Nektar++](/software/nektar-plus-plus.md), and the
normalized total non-viscous dissipation of the second-order runs is 1–4
times the viscous one. On a
combustor port flow the equivalent numerical viscosity is 10–23 times the
molecular viscosity on 16M cells and 8–15 times on 48M cells, against 2.5–7
for an equal-cost spectral/hp run (§5, Table 2). They attribute the
accuracy-per-cost gap mainly to numerical dissipation, the model playing a
secondary role (see [numerical dissipation](/properties/numerical-dissipation.md)).
Rismondo et al. (2025) run a wall-resolved WALE LES of a model wind turbine
on about 144 million cells. It is the source of a
[Ffowcs Williams–Hawkings](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)
noise computation. They claim second-order accuracy "in both space and
time" and give no grid-convergence study. Their maximum Courant number is
about 10 in a few cells near the blade tips, with an average of about 0.017
(§2.1, §2.3).

**Wall-modelled LES, as recalled.** [Mukha et al. (2025)](/sources/mukha-2025.md),
§II.C.4, §IV.B, recall that the viscosity-based wall-stress condition
(no-slip plus a wall eddy viscosity that reproduces the modelled stress)
"has long been used in OpenFOAM". They recall an earlier OpenFOAM WMLES of
a flat-plate boundary layer, at about 2 cells per boundary-layer thickness,
as less accurate than their spectral-element results. In
[Nek5000](/software/nek5000.md) the same condition fails (see that page and
[wall-modelled LES](/methods/wall-modelled-les.md)).

**Other uses.** Steinhausen et al. (2023, §2.1) run DNS of side-wall
flame quenching with an in-house finite-rate chemistry solver, OpenFOAM-based
according to the titles of the works they cite for it, of fourth order in space and second order in time
([direct numerical simulation](/definitions/direct-numerical-simulation.md)).
Domingo & Vervisch (2023, §1) list OpenFOAM among the DNS codes of second
or fourth order. Goc et al. (2021, §1, §4) quote an OpenFOAM
Spalart–Allmaras RANS of the Third High-Lift Prediction Workshop on 109
million cells at about $60\times10^3$ core-hours, about the cost of their
medium-grid WMLES ([Spalart–Allmaras model](/methods/spalart-allmaras-model.md),
[CharLES](/software/charles.md)).

## Qualifications

- Oulghelou et al. (2025) give two version labels for the same solver
  (§4.1 against ref. [57]), and do not say how compressibility is handled
  in their near-sonic jet case, which runs in an incompressible-form
  solver.
- Rismondo et al. (2025, Eq. 2.2) write the subgrid term as
  $+\partial_j\tau_{ij}$ without defining $\tau_{ij}$; for Eq. (2.2) to
  hold, their $\tau_{ij}$ is the negative of the registry's positive-trace
  $\tau_{ij}$, as their Source page's Notation map records.
- Cost and accuracy statements on this page are those of each study's
  set-up (mesh, schemes, model). None isolates OpenFOAM from its
  configuration.

# Citations

- [Rismondo et al. (2025)](/sources/rismondo-2025.md) — §2.1, Eqs. (2.1)–(2.2) (LES solver and schemes); §2.3 (mesh, Courant number).
- [Saini et al. (2023)](/sources/saini-2023.md) — §2.1, Table 1 (pimpleFoam v1712, WALE); §3, Table 2 (costs); §5–6 (dissipation shares).
- [Wu et al. (2025)](/sources/wu-2025.md) — authors' manuscript: §2 (DAFoam discrete adjoint, CoDiPack, SLSQP); §3, Tables 6–7 (simpleFoam test cases).
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — arXiv v2: §4.1 (modified solver, schemes, version); §4 (test cases).
- [Tang et al. (2023)](/sources/tang-2023.md) — §II A, §III, Table I (k-ε baseline, SIMPLE, schemes).
- [McConkey et al. (2022)](/sources/mcconkey-2022.md) — Eqs. (10)–(16) (k-ε-φ-f model in OpenFOAM v2006).
- [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) — §3.2, §3.4 (simpleFoam baseline, WALE LES reference).
- [Liu et al. (2024)](/sources/liu-2024.md) — Eqs. (1)–(21), "Flow solvers" (SSG/LRR-ω with γ in OpenFOAM).
- [Mukha et al. (2025)](/sources/mukha-2025.md) — arXiv v1: §II.C.4, §IV.B (viscosity-based wall condition and OpenFOAM WMLES, as recalled).
- [Steinhausen et al. (2023)](/sources/steinhausen-2023.md) — §2.1 (OpenFOAM-based DNS solver).
- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — §1 (OpenFOAM among DNS codes).
- [Goc et al. (2021)](/sources/goc-2021.md) — §1, §4 (OpenFOAM SA RANS cost reference).
