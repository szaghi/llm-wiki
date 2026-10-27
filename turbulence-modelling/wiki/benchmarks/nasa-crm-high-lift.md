---
type: Benchmark
title: "NASA CRM high-lift configuration"
description: "The NASA High-Lift Common Research Model (CRM-HL), a half-span transport in landing configuration at Mach 0.2: at mean-chord Reynolds number 5.49 million it tests a learned wall model in WMLES and immersed-boundary wall-function RANS, and its wing-body form at root-chord Reynolds number 5.6 million tests anisotropic mesh adaptation for DG RANS."
status: established
aliases: [CRM-HL, HL-CRM, NASA High-Lift Common Research Model, NASA CRM-HL, HLPW-4 CRM-HL, CRM-HL wing-body, HLPW-5 CRM-HL]
tags: [benchmark, wmles, wall-model, rans, immersed-boundary, data-driven, mesh-adaptation, dg]
timestamp: 2026-10-27T11:00:00Z
---

# NASA CRM high-lift configuration

The NASA High-Lift Common Research Model (CRM-HL) is the half model of a
civil transport with deployed slats and flaps, a nacelle and pylon,
used as the test case of the Fourth AIAA High-Lift Prediction Workshop
(HLPW-4), and in a wing-body form without nacelle and pylon in the fifth
workshop (HLPW-5). The two HLPW-4 sources run it at freestream Mach number
$M_\infty=0.20$ and $Re=5.49\times10^6$ based on the mean aerodynamic
chord; the HLPW-5 source runs the wing-body at $M_\infty=0.2$ and
$Re=5.6\times10^6$ based on the root chord. The flow combines
thin leading-edge boundary layers on slats, main wing and flaps, wakes
merging over the flaps, and separation that spreads with incidence until
maximum lift. The quantities compared are the lift, drag and pitching-moment
coefficients $C_L$, $C_D$ and $C_M$ against incidence $\alpha$ (page-local:
angle of attack), and $C_p$ and $C_f$ on spanwise sections. In this bundle
it tests near-wall modelling at aircraft scale: a learned wall model in
[wall-modelled LES](/methods/wall-modelled-les.md) and a wall function at an
[immersed boundary](/methods/immersed-boundary-method.md) in RANS, and
[mesh adaptation](/methods/mesh-adaptation.md) for high-order
discontinuous Galerkin RANS. A
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

The wing-body case of [Schotte et al. (2026)](/sources/schotte-2026.md),
§4.4: HLPW-5 CRM-HL wing-body, $M_\infty=0.2$, $\alpha=11^\circ$,
$Re=5.6\times10^6$ on the root chord; steady RANS with the negative
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md); modal
discontinuous Galerkin of degree $N=1$ and 2 in the ONERA–DLR–Airbus
solver CODA, remeshed by the Tucanos library from an initial mesh of
244,561 cells; target complexities $3\times10^5$ to $2.4\times10^6$ at
$N=1$ and $1.2\times10^5$ to $4.8\times10^5$ at $N=2$ (Table 5);
references are the finite-volume solvers FUN3D, USM3D, CHAMPS and CODA FV
under uniform refinement.

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

**Anisotropic mesh adaptation for high-order RANS.**
[Schotte et al. (2026)](/sources/schotte-2026.md) adapt the mesh with a
metric built from the Hessian of the Mach number, which sets the
orientations and anisotropy, scaled at $N\ge2$ by an isotropic DG
spectral error estimator that sets the element size (§3.2). On the
wing-body (§4.4, Figs. 18–22):

- all adapted DG strategies "clearly outperform FUN3D, CHAMPS and CODA FV
  solutions" in drag and lift at equal degrees of freedom; the $N=1$ drag
  is slightly less accurate, except at the finest complexity, and is
  equivalent to USM3D;
- at $N=2$ the scaling by the small-scale lifted estimator captures the
  wing-tip vortex better than the unscaled Hessian, a change of "+2 drag
  counts and +0.1 lift counts", and $N=2$ needs about $8\times10^6$ fewer
  degrees of freedom than $N=1$ for similar integrated values;
- the unscaled Mach Hessian "still performs well" at $N=2$, which the
  authors call "surprising", since the Hessian does not describe the
  interpolation error above second order;
- adaptation reaches a near-wall $y^+$ close to 1 at $N=1$, with
  anisotropic ratios up to $10^5$ near the wall (Fig. 22).

The authors present the case as the first published high-order DG
metric-based adaptation for "a full high-lift aircraft configuration"
(§1); the configuration run is the wing-body.

**Two-dimensional multi-element airfoils.** The three-element airfoils
that the sources run are separate configurations, not sections of the
CRM-HL. [Huang et al. (2022b)](/sources/huang-2022-d.md), §3.3, run the
30P-30N at $\alpha=16^\circ$, $Re=9\times10^6$, $M=0.2$ with steady
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) RANS on a hybrid
mesh of 53,870 cells (non-dimensional first-layer height $10^{-6}$,
growth 1.25): their
optimized fourth-order variational-reconstruction finite-volume scheme
predicts lift and drag closer to the DLR reference than the fourth-order
scheme with the earlier weights of Pan et al. that they cite, both beat the
second-order scheme (lower lift, higher drag), and its skin friction is
closer to a degree-4 DG solution of 1,119,530 degrees of freedom (the FV
grid has 4.8% of that), though all schemes miss some peaks (Figs. 33–34).
The fourth-order scheme carries the slat-wake eddy viscosity to the
outlet, where the second-order one dissipates it, which the authors link
to the better skin friction (Fig. 35); a WBAP limiter with a shock detector
stabilizes only the start-up iterations. The LEISA2 three-element airfoil
run in ZDES on a lattice Boltzmann solver is recorded on
[detached-eddy simulation](/methods/detached-eddy-simulation.md) and
[lattice Boltzmann method](/methods/lattice-boltzmann-method.md).
The 30P-30N conditions of Huang et al. are those that
[Wang et al. (2013)](/sources/wang-2013.md), §4.11, specify as case C3.1 of
the first High-Order CFD Workshop: two-dimensional RANS with the
Spalart–Allmaras or $k$-$\omega$ model, $M=0.2$, $\alpha=16^\circ$,
$Re=9\times10^6$, fully turbulent, reference chord 0.5588 m; no workshop
results are shown for it. [Bose & Park (2018)](/sources/bose-2018.md),
§4.3, cite the wall-modelled LES of the 30P/30N at $Re_c=9\times10^6$ with
an equilibrium wall model by Bodart et al. (2013): the lift polar is
"qualitatively similar" to the measurements and the maximal lift "well
captured", but the stall angle is about $23^\circ$ against about $21^\circ$
in the experiment, a discrepancy they attribute "potentially" to blockage
corrections of the data, limited spanwise domains or statistical
convergence; their Fig. 7b compares $C_p$ at $19^\circ$ without and with an
equilibrium wall model (Bodart & Larsson 2011) against the experiment.
The same review also cites a wall-modelled LES of the NASA Common
Research Model at $M=0.85$, $\alpha=4^\circ$, $Re_c=5\times10^6$ (Lehmkuhl
et al. 2016, algebraic Werner–Wengle wall-stress closure), which is not
the high-lift configuration of this page and is not a high-lift result.

**Wall-model robustness.** [Nuca et al. (2025)](/sources/nuca-2025.md), §I,
cite CRM-HL wall-modelled LES among the complex applications that motivate
their explicit, iteration-free forms of the algebraic and ODE
[equilibrium wall models](/methods/equilibrium-wall-model.md), but do not
run the configuration.

**What the two HLPW-4 studies share.** Both locate the weak point at the leading
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
  are relative to another RANS solution ($5.5\times10^8$ cells against
  their $2.4\times10^9$), not to experiment; their lift error stays at 8.4% after both corrections.
  Their Table 9 drag error of 9.1% for the first row is 9.0% by the table's
  own coefficients *(compiler check, not in the sources)*.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) give their
  force comparison only in figures (Fig. 15); no coefficients are printed.
- The Reynolds numbers $5.49\times10^6$ (HLPW-4, on the mean aerodynamic
  chord) and $5.6\times10^6$ ([Schotte et al. (2026)](/sources/schotte-2026.md),
  HLPW-5 wing-body, on the root chord) refer to different reference
  lengths and different configurations of the same model; they are not
  competing values for one case. [Schotte et al. (2026)](/sources/schotte-2026.md)
  print no force coefficients for the case (Figs. 20–21 only) and compare
  with other RANS solutions, not with experiment.
- The 30P/30N and Common Research Model results of
  [Bose & Park (2018)](/sources/bose-2018.md) are cited from the works
  they review; the review prints no force coefficients for them.

# Citations

- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §2.3; §4.7, Figs. 14–16; §5(4); §6.
- [Constant et al. (2024)](/sources/constant-2024.md) — §6.3, Tables 7–9, Figs. 35–39; §7.
- [Schotte et al. (2026)](/sources/schotte-2026.md) — §1; §3.2; §4.4, Table 5, Figs. 18–22.
- [Huang et al. (2022b)](/sources/huang-2022-d.md) — §3.3, Figs. 33–35 (30P-30N, a separate configuration).
- [Nuca et al. (2025)](/sources/nuca-2025.md) — §I (cited application only).
- [Bose & Park (2018)](/sources/bose-2018.md) — §4.3, Fig. 7b (cited results: 30P/30N; the $M=0.85$ Common Research Model, not CRM-HL).
- [Wang et al. (2013)](/sources/wang-2013.md) — §4.11 (case C3.1; specification only).
