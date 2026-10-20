---
type: Software
title: "pySDC"
description: "pySDC is the Python prototyping library for spectral deferred correction and its parallel-in-time variants that holds the implementations of the diagonal-SDC and adaptive-SDC studies; it also runs any DIRK or explicit Runge–Kutta method as an SDC sweep with Q_Delta = Q = A."
status: established
aliases: [pySDC, Python SDC library]
tags: [software, parallel, implicit, verification]
timestamp: 2026-10-20T10:00:00Z
---

# pySDC

**pySDC** is a Python library for prototyping
[spectral deferred correction](/methods/deferred-correction.md) and the
parallel-in-time methods built on it (Speck 2019, as recalled by
[Saupe et al. (2025)](/sources/saupe-2025.md); code at
github.com/Parallel-in-Time/pySDC). Both sources that use it publish their experiments
as pySDC projects: [Čaklović et al. (2025)](/sources/caklovic-2025.md) archive the
version used on Zenodo (doi 10.5281/zenodo.13828395), and Saupe et al. give reproduction
instructions on the project's website.

## What the sources use

- **Sweepers.** SDC sweeps with lower-triangular preconditioners (implicit Euler, Weiser's
  LU), explicit and implicit-explicit sweeps, Picard iteration and the diagonal
  preconditioners of [diagonal SDC](/methods/parallel-sdc.md) (VDHS, MIN, MIN3, MIN-SR-NS,
  MIN-SR-S, MIN-SR-FLEX) (Čaklović et al. 2025, §2, §4; Saupe et al. 2025, §2.1).
- **Runge–Kutta methods as sweeps.** Setting $Q_\Delta=Q=A$ for the Butcher matrix $A$ of a
  [DIRK](/methods/diagonally-implicit-runge-kutta.md) or explicit Runge–Kutta method makes
  one sweep reproduce that method, so the same code runs both families. Čaklović et al.
  (2025, Remark 2.2, §4.1) run their comparison methods, classical RK4 and the L-stable
  ESDIRK4(3)6L[2]SA, this way.
- **Parallel-in-time variants.** Pipelined block Gauss–Seidel SDC and diagonal SDC with
  several processes, and their combination (Saupe et al. 2025, §2.3, §4.1).
- **Adaptivity.** The $\Delta t$- and $\Delta t$-$k$-adaptive strategies of Saupe et al.
  (2025, Algorithms 1–2), with restarts from the collocation polynomial of a rejected step;
  see [step-size control](/methods/step-size-control.md).

## Performance context

Wall-clock results from pySDC are Python timings. Čaklović et al. (2025, §4.4) time the
Allen–Cahn runs on one JUSUF node (AMD EPYC 7742) with Python 3.11.9, numpy 2.0.2, scipy 1.14.1
and mpi4py 4.0.0 over ParaStationMPI, solving each Newton step with a scipy sparse solver;
the measured parallel efficiency of diagonal SDC was 74–93 %. Their cost model assumes a
parallel efficiency of 0.8, which they consider achievable with compiled code and OpenMP
(§4.1). Saupe et al. (2025, §4) also report wall-clock times on JUSUF.

## Qualifications

- Comparisons run inside pySDC put serial Runge–Kutta methods and parallel SDC in the same
  Python framework; the ESDIRK43 comparator of Čaklović et al. runs serially there. Speedups
  from such runs are not measurements against optimized serial production codes.
- Both sources were read as arXiv v2 preprints.

# Citations

- [Čaklović et al. (2025)](/sources/caklovic-2025.md) — arXiv v2: §1 (code availability), Remark 2.2, §4.1, §4.4.
- [Saupe et al. (2025)](/sources/saupe-2025.md) — arXiv v2: §1, §2.1–2.3, Algorithms 1–2, §4.
