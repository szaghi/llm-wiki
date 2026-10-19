---
type: Software
title: "PETSc TS"
description: "PETSc's TS time-stepping component as the sources report it: explicit Runge–Kutta pairs with PID step-size control used for large-scale compressible-flow runs, a multirate partitioned method, the absence of multi-stage implicit Runge–Kutta in 2020, and PETSc solvers used by other integrators."
status: established
aliases: [PETSc/TS, TS]
tags: [software, step-size-control, multirate, parallel]
timestamp: 2026-10-19T00:00:00Z
---

# PETSc TS

TS is the time-stepping component of the PETSc library for scalable
solution of discretized PDEs. No source of this bundle is a paper about
TS itself; three sources use it, wrap PETSc solvers, or position their own
software against it, and this page collects what they report, each claim
dated by its source.

## Methods reported

- **Explicit Runge–Kutta with PID control.** [Ranocha et al. (2022)](/sources/ranocha-2022.md)
  run all their compressible-flow experiments in the SSDC solver, which
  is built on PETSc and uses the TS interfaces for explicit Runge–Kutta
  pairs and the digital-filter PID step-size controllers of
  Gustafsson and Söderlind implemented in PETSc (§2.2; refs. [1, 6]);
  their methods are implemented in PETSc/TS within SSDC (companion
  artefacts listed by the paper). See [step-size control](/methods/step-size-control.md)
  and [low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md).
- **Multirate.** [Reynolds et al. (2023)](/sources/reynolds-2023.md)
  state that among PETSc/TS, Trilinos/Tempus and DifferentialEquations.jl
  only PETSc supported multirate methods, namely a second-order multirate
  partitioned Runge–Kutta method (§1, ref. [33]); compare
  [multirate GARK methods](/methods/multirate-gark.md) and ARKODE's
  [MRIStep](/software/arkode.md).
- **No multi-stage implicit Runge–Kutta (2020).** [Farrell et al. (2021)](/sources/farrell-2021.md)
  state that PETSc TS "only provides a small, enumerated set of RK
  methods, and these do not include multi-stage implicit RK methods",
  which motivates [Irksome](/software/irksome.md) (§1; arXiv v1, June 2020).
  A footnote mentions a firedrake-ts wrapper of TS.

## PETSc solvers used by other integrators

- Irksome hands its coupled stage system to PETSc's linear solvers:
  GMRES with additive field split and one `gamg` algebraic-multigrid
  V-cycle per stage block, or multiplicative field split as block forward
  substitution for DIRKs (Farrell et al. 2021, §2.3, Listings 2–3). See
  [implicit stage solvers](/methods/implicit-stage-solvers.md).
- SUNDIALS provides a `SUNNonlinearSolver` wrapping PETSc's SNES
  nonlinear solvers ([Gardner et al. (2022)](/sources/gardner-2022.md),
  §6; not a TS feature, recorded for completeness).

## Measured performance (Ranocha et al. 2022)

All runs on the Cray XC40 Shaheen (Intel Haswell, 2.3 GHz, two 16-core
sockets per node), entropy-dissipative DG spectral-collocation
semidiscretizations ([Ranocha et al. (2022)](/sources/ranocha-2022.md), §7):

- **NASA juncture flow** ($\approx6.76\times10^5$ hexahedra,
  $\approx4.09\times10^7$ degrees of freedom, polynomial degrees 1–3,
  Re $2.4\times10^6$, Ma 0.189, eight nodes): CFL control with $\nu=1$
  needed about 50% more right-hand-side evaluations and wall time than
  error-based control at tolerance $10^{-8}$; for BS3(2)3F, 3,598 vs
  1,786 evaluations and 1,171.60 s vs 586.49 s; the SSP pair
  SSP3(2)4[3S\*$_+$] was "nearly 50%" faster than BS3(2)3F (376.18 s)
  (§7.2, Table 8).
- **Imperial Front Wing** ($3.4\times10^6$ hexahedra, Re $2.2\times10^5$,
  Ma 0.036): error control at $10^{-8}$ again cost about half of CFL
  control with $\nu=1$; at polynomial degree 1, CFL control with $\nu=1$
  crashed for SSP3(2)4[3S\*$_+$], $\nu=0.85$ worked and was a few percent
  cheaper (1,304 evaluations, 321.54 s) than error control (1,352,
  331.97 s), which needed no tuning (§7.3, Tables 9–10).

These results measure the time-integration strategy, not TS against
another library.

## Qualifications

- Every capability statement on this page is a statement *about* PETSc
  made by a source at its date (Farrell et al.: 2020 preprint; Ranocha et
  al.: 2021 preprint; Reynolds et al.: 2022 preprint). The sources do not
  conflict: Farrell et al. speak of implicit Runge–Kutta methods,
  Reynolds et al. of multirate ones.
- The bundle holds no source describing TS's own design, its implicit or
  IMEX methods, or its adjoint capabilities.

# Citations

- [Farrell et al. (2021)](/sources/farrell-2021.md) — §1 (TS method set in 2020, firedrake-ts footnote), §2.3, Listings 2–3 (PETSc field-split solvers).
- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §2.2 (PID controllers in PETSc), §7.2–§7.3, Tables 8–10.
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §1 (multirate support among libraries).
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §6 (SNES wrapper).
