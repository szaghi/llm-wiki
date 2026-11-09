---
type: Source
title: "Camier, Dobrev, Knupp, Kolev, Mittal, Rieben & Tomov (2023) — Accelerating high-order mesh optimization using finite element partial assembly on GPUs"
description: "GPU-oriented high-order target-matrix optimization recast as finite-element operations with partial assembly, sum factorization and matrix-free Newton–MINRES solves, plus a reproducible mesh-optimization benchmark."
resource: "doi:10.1016/j.jcp.2022.111808"
source_kind: paper
authors: [Camier J.-S., Dobrev V., Knupp P., Kolev T., Mittal K., Rieben R., Tomov V.]
year: 2023
venue: "J. Comput. Phys. 474:111808"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2023_Crossref_Journal_of_Computational_Physics_Camier_Accelerating_high-order_mesh_optimization_using_finite_eleme.pdf"
tags: [mesh-optimization, target-matrix, gpu, matrix-free]
timestamp: 2026-11-08T20:54:00Z
---

# Summary

Camier et al. port [target-matrix optimization](/methods/target-matrix-optimization.md) to GPUs by partial assembly of its finite-element kernels.

# Version read

arXiv:2205.12721v2 (2 December 2022); metadata from the version of record, J. Comput. Phys. 474, 111808 (2023). Abstract, §§1–3 by structure and §5 read.

# Key claims

1. Partial assembly lowers storage and assembly to $O(k^d)$ and evaluation to $O(k^{d+1})$ per element (§1, §3). **Stated**
2. The Hessian is inverted by MINRES with Jacobi preconditioning; matrix-free preconditioning remains open (§2–§3, §5). **Stated**
3. Substantial performance gains on GPUs for quadrilaterals and hexahedra (§4–§5). **Shown**

# Notation map

| Camier, Dobrev, Knupp, Kolev, Mittal, Rieben & Tomov (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p$ | $k$ | polynomial degree |

# Reference list

42 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 4 (2026-11-08). This source is cited on:

- [Target-matrix optimization (TMOP)](/methods/target-matrix-optimization.md)
