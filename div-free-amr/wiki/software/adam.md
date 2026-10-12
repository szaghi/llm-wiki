---
type: Software
title: "ADAM"
description: "Block-structured octree/quadtree AMR library (CPU and GPU) whose Maxwell (PRISM) and MHD (FLUME) solvers hold the divergence in two different constraint classes."
status: hypothesis
tags: [amr, coarse-fine-interface, glm, collocation, gpu]
timestamp: 2026-10-12T00:00:00Z
---

# ADAM

A block-structured AMR library: an octree or quadtree of Cartesian blocks,
2:1 balance, CPU (MPI + OpenMP) and GPU (MPI + OpenACC) backends, and
multi-realm forests glued by seams. Everything here is from the author's
own record, [Zaghi (2026)](/sources/zaghi-2026.md), so the page carries
`status: hypothesis`. Two of its solvers sit on opposite sides of the
divergence-constraint taxonomy, which makes the code a controlled
comparison: the same seam machinery serves both.

| Solver | Equations | Field update | Constraint class ([exact discrete divergence](/properties/exact-discrete-divergence.md)) |
|---|---|---|---|
| PRISM | Maxwell | centered high-order FD (or FV), $B_h$ evolved by the collocated curl $C_h^{\mathrm{c}}$ | **exact** on uniform grids, $D_h^{\mathrm{c}} C_h^{\mathrm{c}} = 0$; lost at 2:1 seams |
| FLUME | compressible Euler, ideal and resistive MHD | WENO finite differences in flux-divergence form, flux splitting or Riemann solvers | **controlled**: [GLM](/methods/glm-divergence-cleaning.md) or EGLM, no exact invariant |

## Interface machinery

* **Ghost fill at 2:1 seams.** Selectable injection, restriction-compatible
  or tricubic fills $\Gamma$. Tricubic is the default because compatibility
  caps the order
  ([point-value restriction bound](/results/point-value-restriction-compatibility.md)).
* **Reflux.** Berger–Colella [refluxing](/methods/refluxing.md) restores
  conservation of all conserved rows, $B_h$ and $\psi_h$ included. It does
  not touch the seam divergence.
* **Seam coupling cadence** between realms, end-of-step or stage-coincident.
  Only the stage-coincident cadence keeps a 1:1 seam exactly
  divergence-free.
* **Guard-rail.** An opt-in run-time monitor on the seam divergence. It
  implements the accept-truncation resolution of the
  [seam divergence source](/results/collocated-seam-divergence-source.md).
  The only exact alternative, a staggered field at the seam, is parked.

## Published record (Zaghi et al. 2023)

A peer-reviewed paper on the code at its 2023 state
([Zaghi et al. (2023)](/sources/zaghi-2023.md)) independently supports, as published fact, the
infrastructure claims above. It supports none of the divergence-related
ones, which is why this page keeps `status: hypothesis`.
* **Supported.**
  * An octree of identical Cartesian blocks of cell-centred cells, split
    8 ways, with 26 ghost regions per block.
  * 2:1 balance: "the AMR level between two contiguous blocks must differ
    by at most one".
  * A tree held in a hash map keyed by a 64-bit "Morton index", replicated
    on every MPI rank and updated serially.
  * Load balancing along Morton curves.
  * A field that stays on the GPU, with the block index fastest-varying
    for coalescing (§2.2, Fig. 2).
  * WENO finite differences with Lax–Friedrichs flux splitting and
    SSP-RK3, for the compressible Navier–Stokes application NASTO (§3.1).
* **Different in 2023.**
  * The only GPU back-end was CUDA Fortran with CUDA-aware MPI. OpenMP and
    OpenACC back-ends were future work (§§2.2, 4).
  * Ghost fill across level jumps used "second-order interpolations", not
    the tricubic default recorded above (§2.2).
  * These are version differences, not contradictions. The 2023 paper is
    not evidence for OpenACC or for the tricubic fill.
* **Silent.**
  * Refluxing, the quadtree, realms and seams, and the PRISM and FLUME
    solvers.
  * There is no subcycling: one global time step is taken from the
    smallest cell (eq. 9).
  * Ghosts are refreshed at every Runge–Kutta stage (§3.1.1).
* **Performance** on V100 GPUs (Marconi100), shock diffraction over a
  sphere:
  * strong scaling superlinear to 8 GPUs, about 89 % efficient at 16, below
    60 % at 32;
  * efficient above about 250 000 cells per GPU;
  * the serial tree update is the bottleneck: 527.97 s per update at
    684 258 blocks (§3.2, Table 1).
* **A third-party description** agrees: Jaber et al. list the 2023 code
  among those whose mesh is "hosted and managed, in whole or part, on the
  CPU" ([Jaber, Essel & Sullivan (2025)](/sources/jaber-essel-sullivan-2025.md), §1).

## Evidence it contributes

* The seam-source characterization and the five failed fix classes
  ([Result](/results/collocated-seam-divergence-source.md)).
* GLM's limits under a growing seam source, its accuracy cost on solenoidal
  data, and EGLM robustness at low plasma β
  ([GLM](/methods/glm-divergence-cleaning.md)).
* [Field-loop](/benchmarks/field-loop-advection.md) runs on uniform and
  2:1 grids.

# Citations

1. [Zaghi (2026)](/sources/zaghi-2026.md): FLUME `index.md`, `numerics.md`, `models.md`; `forest.md`; `prism-regression.md`; issues #21, #29, #30, #31.
2. [Zaghi et al. (2023)](/sources/zaghi-2023.md), §§2.2, 3.1–3.2, 4, Table 1.
3. [Jaber, Essel & Sullivan (2025)](/sources/jaber-essel-sullivan-2025.md), §1.
