---
type: Software
title: "AMReX"
description: "C++ framework for block-structured AMR, successor of BoxLib: cell-, face- and node-centred data, optional subcycling, embedded boundaries, geometric multigrid, particles and MPI+X / MPI+GPU parallelism; the hierarchy under CASTRO and one of Flash-X's AMR back-ends."
status: established
aliases: [BoxLib]
tags: [amr, block-structured, framework, gpu]
timestamp: 2026-10-12T00:00:00Z
---

# AMReX

A C++ framework for building [block-structured AMR](/definitions/block-structured-amr.md)
solvers for systems of PDEs, descended from BoxLib
([Zhang et al. (2019)](/sources/zhang-2019.md)). The software paper lists
capabilities without algorithms, tests or performance numbers.
* **Advance strategies.** Level-by-level advance "with or without
  subcycling in time", with unspecified multilevel synchronization, or
  full-hierarchy approaches.
* **Data and geometry.** Mesh data on cell centres, faces or nodes;
  embedded-boundary (cut-cell) geometry; particles.
* **Solvers.** Native geometric multigrid and BiCGStab, with hypre and
  PETSc interfaces, on regular and cut-cell data.
* **Parallelism.** MPI+X with OpenMP tiling, and MPI+CUDA+X, with CUDA
  the only back-end of AMReX itself in 2019.
* **Not stated:** the refinement ratio, the ghost-fill and restriction
  orders, refluxing, and whether the multigrid is composite across levels.
* **No divergence content.** The paper never mentions projections or
  divergence constraints.

**Evidence from codes built on it.**
* *Flux register.* In Flash-X on AMReX, the register between two levels
  can hold a linear combination of the Runge–Kutta stage fluxes and is
  applied once at the end of the step
  ([Couch et al. (2021)](/sources/couch-2021.md); [refluxing](/methods/refluxing.md)).
* *CASTRO, on BoxLib.*
  * Arbitrary-size grids with refinement ratio 2 or 4, proper nesting
    without parent–child links, subcycling, and Berger–Colella refluxing.
  * A multilevel self-gravity synchronization with a second flux
    register.
  * Grids distributed by a knapsack heuristic or a Morton
    [space-filling curve](/definitions/space-filling-curve.md)
    ([Almgren et al. (2010)](/sources/almgren-2010.md), §§6–7;
    [CASTRO](/software/castro.md)).

# Citations

1. [Zhang et al. (2019)](/sources/zhang-2019.md).
2. [Couch et al. (2021)](/sources/couch-2021.md), AMR section.
3. [Almgren et al. (2010)](/sources/almgren-2010.md), §§6–7.
