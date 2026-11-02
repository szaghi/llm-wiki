---
type: Source
title: "Kumar et al. (2026) — GPU optimized integration of immersed boundary method and overset meshes"
description: "A GPU-accelerated overset immersed-boundary framework for incompressible flows with several moving bodies, combining Cartesian immersed boundaries with overset local refinement, with a lightweight sliding-window reallocation strategy and minimal interface storage to follow arbitrary body motion, applied to bio-inspired and drone-propeller aerodynamics."
resource: "doi:10.1016/j.cma.2026.119241"
source_kind: paper
authors: [Kumar D., Sharma S.D., Bose C., Roy S.]
year: 2026
venue: "Comput. Methods Appl. Mech. Eng. 461:119241"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2026_Crossref_Computer_Methods_in_Applied_Mechanics_and_Engineering_Kumar_GPU_optimized_integration_of_immersed_boundary_method_and_ov.pdf"
tags: [immersed-boundary, gpu, moving-grid, incompressible]
timestamp: 2026-11-02T15:41:00Z
---

# Summary

Kumar et al. combine Cartesian [immersed-boundary](/methods/immersed-boundary-on-overset-grids.md) methods with overset local refinement on GPUs for incompressible flows with several moving bodies. To let the overset meshes follow arbitrary body motion, a lightweight sliding-window reallocation strategy with minimal interface storage is developed ([moving overset grids](/methods/moving-overset-grid.md), [parallel and GPU assembly](/methods/parallel-overset-grid-assembly.md)); applications include bio-inspired aerodynamics and drone propellers.

# Version read

Version of record (Elsevier), 36 pages. Read in a targeted way (abstract, introduction, section structure, main results and conclusions closely; derivations and remaining results skimmed): from chunk 4 on, the bundle is compiled in the main session without reader subagents, by the owner's instruction. Claims below are limited to what was read closely.

# Key claims

1. The framework combines the simplicity of Cartesian immersed-boundary methods with the local refinement of overset grids for incompressible flows with several moving bodies, accelerated on GPUs (Abstract). **Stated**
2. A lightweight sliding-window reallocation strategy with minimal interface-storage requirements supports overset mesh movement due to arbitrary body motion (Abstract). **Stated**
3. Applications to bio-inspired and drone-propeller aerodynamics are shown (Abstract, keywords). **Shown**

# Printed slips

None recorded (targeted reading).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| overset mesh, background mesh | $G_k$ of higher, lower priority | |

# Reference list

69 references, merged complete into the [bibliography](/bibliography.md) with `citedby` kumar-2026, from the Crossref deposited reference list; Meakin's adaptive-refinement paper, printed with the year 19895, is `meakin-1995-b`. [Horne & Mahesh (2021)](/sources/horne-2021.md) and [Wang et al. (2025)](/sources/wang-2025.md) are cited.

# Pages created or updated

Chunk 5 (2026-11-02). This source is cited on:

- [Immersed boundaries on overlapping grids](/methods/immersed-boundary-on-overset-grids.md)
- [Moving overset grids](/methods/moving-overset-grid.md)
- [Parallel and GPU overset grid assembly](/methods/parallel-overset-grid-assembly.md)
