---
type: Software
title: "ADAM"
description: "Block-structured octree/quadtree AMR library (CPU and GPU) whose Maxwell (PRISM) and MHD (FLUME) solvers hold the divergence in two different constraint classes."
status: hypothesis
tags: [amr, coarse-fine-interface, glm, collocation, gpu]
timestamp: 2026-10-08T00:00:00Z
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
