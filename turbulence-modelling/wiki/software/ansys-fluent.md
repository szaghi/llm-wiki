---
type: Software
title: "ANSYS Fluent"
description: "ANSYS Fluent is the commercial cell-centred finite-volume code in which bundle sources run RANS, SST-DDES, DES, SBES and wall-resolved LES of cars, impellers, pitching airfoils and hypersonic fins, and implement transition models; this page records the versions, schemes and model forms they report."
status: established
aliases: [Fluent, ANSYS-Fluent, Ansys Fluent, ANSYS FLUENT]
tags: [software, rans, des, hybrid-rans-les, les, transition]
timestamp: 2026-10-29T07:41:00Z
---

# ANSYS Fluent

**ANSYS Fluent** is a commercial, unstructured, cell-centred finite-volume
flow solver with pressure-based (segregated or coupled) and density-based
formulations. In this bundle it is never the subject of a study: five
sources run their RANS, hybrid RANS/LES or LES in it, or implement a model
in it, and each states its own version, schemes and model. Equations of the
vendor's theory guide are given here only where a source prints them. None of the settings below is shown to be a default of the
code unless the source says so.

## Versions, solvers and schemes as reported

| Source | Version | Formulation and schemes | Turbulence treatment | Flow |
|---|---|---|---|---|
| [Menter et al. (2022)](/sources/menter-2022.md), §3 | R21, double precision | pressure-based coupled solver, second-order convection for all equations, ICEM CFD hexahedral meshes | [$k$-$\omega$ SST](/methods/k-omega-sst-model.md) with algebraic, one-equation and two-equation [transition models](/methods/local-correlation-based-transition-model.md) | ERCOFTAC T3 plates, airfoils, Pak-B cascade |
| [Delassaux et al. (2023)](/sources/delassaux-2023.md), §4 | 2020R2 | incompressible, cell-centred; bounded central differencing for convection, second-order central diffusion, SIMPLEC, second-order implicit time; point-implicit Gauss–Seidel with algebraic multigrid | realizable [$k$-$\varepsilon$](/methods/k-epsilon-model.md) with Enhanced Wall Treatment, SST, SST-based delayed [DES](/methods/detached-eddy-simulation.md) | full-scale car, $1.3\times10^7$ on vehicle length |
| [Pan & Zhang (2023)](/sources/pan-2023.md), §II.E | not printed | default parameters; least-squares cell-based gradients, "bounded second-order implicit" time, SIMPLE, multiple reference frame | Spalart–Allmaras DES and DDES; [LES](/definitions/large-eddy-simulation.md) with the [dynamic](/methods/dynamic-procedure.md) Smagorinsky–Lilly model | centrifugal impeller at 25% of design flow |
| [Baldan & Guardone (2025)](/sources/baldan-2025.md), §1.2 | 2023R2 | incompressible, second-order upwind, least-squares gradients, Rhie–Chow face fluxes, SIMPLE (RANS) and SIMPLEC (LES), bounded second-order implicit time, rigidly rotating O-grid | wall-resolved LES with the [WALE model](/methods/wale-model.md); SST with $\gamma$ intermittency for initialization; SBES comparison data | pitching NACA 0012, $Re_c=1.35\times10^5$ |
| [Thawait et al. (2023)](/sources/thawait-2023.md), §II | 2022R1 | density-based implicit, AUSM+ inviscid flux, dual time stepping with second-order backward differences in physical time, second-order upwind convection, second-order central diffusion, least-squares gradients, ILU smoothing with algebraic multigrid; diffusion-based mesh smoothing | SST-based DDES | deployable fin at Mach 3–6 coupled to ANSYS Mechanical |

## Model forms printed from the code

**SST $\omega$ production.** Menter et al. (2022, Eq. 6) state that Fluent
writes the production of the $\omega$ equation as
$\alpha\rho P_k/(\mu_t+0.001\mu)$ to avoid a division by zero ($\alpha$ the
production coefficient of the $\omega$ equation, as printed), with little
effect in fully turbulent flow and "a small noticeable" effect on
transition prediction.

**Transition model hysteresis.** The one-equation $\gamma$ model showed a
dependence of the transition location on the initial condition (laminar or
fully turbulent start) in Fluent, a cell-centred finite-volume code, but
not in ANSYS CFX, where the model was developed; Menter et al. (2022, §2.3,
Fig. 3) attribute this to the different numerical stencils. A harmonic
average of $k$ over the face-connected cells in the local turbulence
intensity removes it; the authors state that it is now made standard in
the one-equation model.
The Fluent and NTS implementations of their new algebraic model agree
closely; NTS slightly delays the T3 onset and differs a little on the S809
airfoil (Figs. 7, 12).

**Enhanced Wall Treatment.** The two-layer near-wall treatment of the
realizable $k$-$\varepsilon$ model used by Delassaux et al. (2023, §4.1.1)
switches on the wall-distance Reynolds number $R_y=\rho y\sqrt k/\mu$ (the
registry's $R_y=d\sqrt k/\nu$): for $R_y<200$ the eddy viscosity comes from
the one-equation model of Wolfshtein, above it from $k$-$\varepsilon$. The
authors call it the numerical reference of their industrial practice.

**SST-based DDES.** Thawait et al. (2023, §II.B, Eqs. 9–13), citing the
2022R1 theory guide, print the delayed DES of the SST model as a
multiplier of the destruction term of the $k$ equation,
$$\rho\beta^*k\omega\,F_{\mathrm{DES}},\qquad F_{\mathrm{DES}}=\max\!\left(\frac{L_t}{C_{\mathrm{DES}}\Delta_{\max}}\left(1-F_{\mathrm{DDES}}\right),\,1\right),\qquad L_t=\frac{\sqrt k}{\beta^*\omega},$$
with $C_{\mathrm{DES}}=0.61$, $F_{\mathrm{DDES}}=\tanh[(C_{d1}r_d)^{C_{d2}}]$,
$C_{d1}=20$, $C_{d2}=3$ and
$r_d=(\nu_t+\nu)/\big(\kappa^2y^2\sqrt{0.5(|S|^2+|\Omega|^2)}\big)$, $\kappa=0.41$.
Page-local: $L_t$ the RANS length scale, $\Delta_{\max}$ the local grid
spacing (the source's "grid spacing"), $r_d$ the DDES sensor. Thawait et
al. state that DDES "preserves RANS in the boundary layer" (§II.B); with
$F_{\mathrm{DDES}}=1$, Eq. (10) gives $F_{\mathrm{DES}}=1$, the unmodified
destruction term *(compiler check, not in the sources)*. The
same section also prints the DDES length scale
$d_{\mathrm{DDES}}=d-f_d\max(0,d-C_{\mathrm{DES}}\Delta_{\max})$ (the source's
$\tilde d$), $f_d=1-F_{\mathrm{DDES}}$
(Eq. 14), without saying where it enters the SST equations. The same model
family, with the shielding of ANSYS CFX, is used on a turbine cascade by
Yang & Ma (2022); see [turbine cascades](/benchmarks/turbine-cascade.md)
and [detached-eddy simulation](/methods/detached-eddy-simulation.md).

## Applications in the sources

- **Transition models** (Menter et al. 2022): the algebraic
  $\gamma$-alg-SST model is calibrated and validated in Fluent R21 against
  the one- and two-equation transport models on flat plates, airfoils and
  the Pak-B cascade; see
  [local-correlation-based transition models](/methods/local-correlation-based-transition-model.md),
  [ERCOFTAC T3](/benchmarks/ercoftac-t3-flat-plate.md) and
  [turbine cascades](/benchmarks/turbine-cascade.md).
- **Full-scale car** (Delassaux et al. 2023): tetrahedral grids of 115M
  and 180M cells with 20 prism layers at $y^+\approx1$; RANS
  ($C_D=0.242$) and SST-DDES ($C_D=0.255$) against the measured 0.244, the
  RANS agreement coming from error cancellation along the car; one DDES run
  costs 18 times the wall-clock time of a RANS run. The convection scheme
  is bounded central differencing because second-order upwind "would
  annihilate the turbulent structures" and pure central differencing "can
  be unstable"; the advised maximum CFL number in the LES region is 5
  (§4.2, §6). See [hybrid RANS/LES](/definitions/hybrid-rans-les.md) and
  [numerical dissipation](/properties/numerical-dissipation.md).
- **Centrifugal impeller in rotating stall** (Pan & Zhang 2023): a
  12.33-million-cell structured grid (maximum $y^+\approx1.2$), one degree
  of rotation per time step ($\Delta t=0.00023$ s), "default Fluent
  parameters for every approach" to keep the comparison fair (§II.E).
  Neither DES nor DDES is better than the other for every quantity
  ([detached-eddy simulation](/methods/detached-eddy-simulation.md)).
- **Deep dynamic stall** (Baldan & Guardone 2025): wall-resolved WALE LES
  on 62.7M to 374.7M nodes over spans of 0.2 to 1.2 chords; the span must
  be at least one chord once the dynamic-stall vortex forms (see
  [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md) and
  [dynamic stall](/definitions/dynamic-stall.md)).
- **Hypersonic fin with joint freeplay** (Thawait et al. 2023): a strongly
  coupled fluid–thermal–structural set-up in which Fluent is linked to
  ANSYS Mechanical through ANSYS System Coupling (profile-preserving
  mapping of displacement and temperature, conservative mapping of
  forces). Structured hexahedral flow grids of 1 million cells with first
  layer $y^+<1$ serve the two validation cases (a Mach 3 flutter wing and a
  heated panel at Mach 4); the fin runs on an unstructured tetrahedral grid
  of 2.7 million cells chosen by a three-grid convergence-index study
  (§V–§VI, Table II). The paper compares DDES with no other turbulence
  model, and its validations test the structural response (flutter
  velocity within 5%, panel deflections within 3.18% and 0.12%), not the
  closure.
- **Rotating detonation rocket engine, as cited** (Vignat et al. 2024):
  in their survey of the groups that computed the same AFRL methane–oxygen
  rotating detonation engine (Table 1), Vignat et al. list the LES of
  Strakey & Fergusson (which they cite) as run in Fluent with a
  one-equation subgrid turbulent-kinetic-energy model; Vignat et al.'s own
  LES is run in a different, unstructured compressible code (see
  [CharLES](/software/charles.md)). The study is not ingested, and Table 1
  gives no further Fluent settings. See
  [one-equation subgrid kinetic-energy models](/methods/subgrid-kinetic-energy-equation-model.md).

## Qualifications

- Pan & Zhang (2023, §III.A) call their LES both a dynamic
  Smagorinsky–Lilly LES and "the implicit filtered LES approach of
  ANSYS-Fluent", citing a work on [implicit LES](/definitions/implicit-les.md);
  the two descriptions are recorded side by side.
- Thawait et al. (2023, Table II) pair the three grids of 1.35, 2.7 and 5
  million cells with minimum cell sizes of 3.8, 5 and 7.5 mm in the same
  order, so the finest spacing is printed against the fewest cells. Their Table I Reynolds numbers
  (12.2 to $24.3\times10^6$ for Mach 3 to 6) are printed without a
  reference length.
- The versions read are the arXiv v2 preprint for Baldan & Guardone (2025)
  and the HAL author manuscript for Delassaux et al. (2023); see their
  Source pages.
- Menter et al. (2022) are ANSYS authors validating their own model in the
  vendor's code; the other four sources are users. Vignat et al. (2024)
  only cite a Fluent study.

# Citations

- [Menter et al. (2022)](/sources/menter-2022.md) — §2.3, Eq. (6), Fig. 3 (Fluent SST production, hysteresis, harmonic averaging); §3, Figs. 7, 12 (Fluent R21 set-up, comparison with NTS).
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — HAL author manuscript: §4.1–4.2, Eqs. (1)–(5) (finite-volume formulation, BCD, SIMPLEC, Enhanced Wall Treatment, CFL); §6, Table 3, Fig. 13 (drag, cost).
- [Pan & Zhang (2023)](/sources/pan-2023.md) — §II.E (Fluent set-up, default parameters); §III.A (LES description).
- [Baldan & Guardone (2025)](/sources/baldan-2025.md) — arXiv v2: §1.1–1.2, Table 2 (grids, Fluent 2023R2 schemes, WALE, iSST, SBES).
- [Thawait et al. (2023)](/sources/thawait-2023.md) — §II.B–E, Eqs. (9)–(19) (SST-DDES, AUSM+, mesh smoothing, dual time); §IV (System Coupling); §V–§VI, Tables I–II (validation, grids).
- [Vignat et al. (2024)](/sources/vignat-2024.md) — §3.3, Table 1 (Fluent LES of the AFRL rotating detonation engine by Strakey & Fergusson, as cited).
