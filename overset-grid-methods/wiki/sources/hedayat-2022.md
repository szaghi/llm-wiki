---
type: Source
title: "Hedayat et al. (2022) — A parallel dynamic overset grid framework for immersed boundary methods"
description: "Extends a curvilinear immersed-boundary incompressible solver with fixed overset grids to moving overset grids with a fully parallel in-core assembly: explicit hole cutting by ray tracing, oriented-bounding-box query search, walking donor search, a PETSc interpolation matrix, non-inertial frames per moving grid and a flux correction for mass conservation."
resource: "doi:10.1016/j.compfluid.2022.105378"
source_kind: paper
authors: [Hedayat M., Akbarzadeh A.M., Borazjani I.]
year: 2022
venue: "Comput. Fluids 239:105378"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2022_Crossref_Computers_amp_Fluids_Hedayat_A_parallel_dynamic_overset_grid_framework_for_immersed_bound.pdf"
tags: [immersed-boundary, moving-grid, parallel, incompressible, fsi]
timestamp: 2026-11-02T15:02:00Z
---

# Summary

Hedayat et al. extend the overset-CURVIB solver (a curvilinear, sharp-interface [immersed-boundary](/methods/immersed-boundary-on-overset-grids.md) incompressible Navier–Stokes solver) from fixed overset grids with a sequential, file-based assembly to [moving overset grids](/methods/moving-overset-grid.md) with a [parallel in-core assembly](/methods/parallel-overset-grid-assembly.md). Every block is partitioned over all processors as the flow solver prefers; explicit [hole cutting](/methods/hole-cutting.md) by ray tracing, oriented-bounding-box query identification, a walking [donor search](/methods/donor-search.md) with brute-force fallback, trilinear [interpolation](/methods/inter-grid-interpolation.md) applied as a sparse PETSc matrix, and non-blocking communication with data packing. Moving grids are solved in a non-inertial frame attached to each body, so their metrics are not recomputed. Mass conservation is restored by a flux correction over each blanked region and each overset interface ([conservative overset interface](/methods/conservative-overset-interface.md)). Tests: a [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) with a translating or rotating grid, oscillating [cylinders](/benchmarks/flow-past-circular-cylinder.md), freely falling cylinders with [fluid–structure coupling](/methods/fluid-structure-interaction-on-overset-grids.md), and a school of four self-propelled fish.

# Version read

arXiv preprint 1910.09315v1 (13 October 2019, "Preprint submitted to Elsevier"), 38 pages, all read. The preprint prints two authors (Hedayat, Borazjani); the published paper adds Akbarzadeh as second author. Equation, section and table numbers are those of the preprint.

# Key claims

1. Moving grids are solved in a non-inertial frame attached to each body, avoiding recomputation of the curvilinear metrics, while the background is solved in the inertial frame; interpolated velocities are rotated between frames (Abstract, §2.1, §2.3, Eqs. 1–10). **Stated**
2. Every block is distributed over all processors; data packing reduces the worst-case number of messages from $C(n,2)\times P(m,2)$ to $n\times P(m,2)$ for $n$ blocks and $m$ processors (§2.2.1, §2.2.4, Algorithm 2). **Stated**
3. Implicit hole cutting is said to need about an order of magnitude more computation than explicit hole cutting, so ray-tracing explicit hole cutting is used for dynamic grids and strongly coupled fluid–structure problems (§2.2.2). **Stated** (no measurement)
4. Oriented bounding boxes (axes from the eigenvectors of a covariance matrix) bound each partition more tightly than axis-aligned boxes (§2.2.3, Eq. 12). **Stated**
5. A walking donor search replaces brute force, with a fallback to brute force in the control cell when the walk gets stuck (§2.2.5, Algorithm 3). **Stated**
6. Interpolation is applied as a sparse PETSc matrix formed once per time step and applied by matrix–vector products, judged more efficient in the authors' tests (§2.2.6). **Stated**
7. Because the predicted velocity does not satisfy continuity and trilinear interpolation is not conservative, a flux correction sets the net flux through each blanked-region boundary and each overset interface to zero; colliding blanked regions are corrected on their combined boundary (§2.4.1, Eq. 21, Figs. 10–11). **Stated** (from Borazjani et al. 2013)
8. When an overset interface crosses an immersed body, the region around the body is blanked in the other grid instead of assigning approximate velocities to solid nodes (§2.4, Fig. 11). **Stated**
9. Taylor–Green vortex ($Re=10$, $t=1$) with a translating or rotating grid: the error decreases at about second order under combined space–time refinement at constant CFL (§3.1, Figs. 12–13). **Shown**
10. Rotationally oscillating cylinder ($Re=300$): overset and single-grid torque agree over eight cycles; forced in-line oscillating cylinder ($Re=100$, $KC=5$) agrees with the experiment of Dütsch et al. (§3.2–3.3, Figs. 14–15). **Shown**
11. Freely falling cylinder: overset and single-grid fall velocities differ by about 0.2 %; for three cylinders by at most about 4 % (§3.4, Figs. 16–18). **Shown**
12. Four self-propelled mackerels: about 29 M nodes against at least 470 M for a single grid of similar resolution (§3.5). **Shown**
13. Strong scaling (about 30 M points, 1.2 M receptors, up to 560 cores): assembly 5.1 s on 8 cores to 0.40 s on 140 cores, then 0.58 s on 560; about 7 % of the flow-solver time at 560 cores; interpolation below 0.1 %; assembly speed-up near ideal to 140 cores, then limited by load imbalance (§4, Fig. 23). **Shown**

# Printed slips

- Eq. 14 (trilinear interpolation) uses factors $(a_k-1)$ for which the weights sum to $(2a_1-1)(2a_2-1)(2a_3-1)$, not 1 *(compiler check, not in the sources)*.
- The unit normal of Eq. 13 is not normalized; Algorithm 3 has no exit for a successful search.
- The Taylor–Green grid list repeats $81\times49$ (six grids for "five simulations"); the rotating-cylinder domain is printed "50D<x<50D"; the probe location is $0.6D$ in the text and $-0.6D$ in the caption of Fig. 15; the single table is labelled "Table 4"; the equivalent single grid is "470 M" in §3.5 and "500 M" in §5.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| blanked node, interface node | hole $\mathcal H_k$, receptor $\mathcal R_k$ | |
| background, overset grid | $G_k$ of lower, higher priority | donor priority: background first |
| non-inertial frame of a moving grid | body frame; grid velocity $\mathbf u_g$ | |

# Reference list

100 printed references, author–year style, merged complete into the [bibliography](/bibliography.md) with `citedby` hedayat-2022. "Steger & Benek 1968, Proc. Steklov Inst. Math." prints the venue, volume and pages of Volkov's composite-mesh paper and is merged into `volkov-1968` with a note on the misprinted authors. No printed duplicates.

# Pages created or updated

Chunk 3 (2026-11-02), cited further in chunk 4. This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Taylor–Green vortex (two-dimensional exact decaying solution)](/benchmarks/taylor-green-vortex.md)
- [Composite overlapping grid](/definitions/composite-overlapping-grid.md)
- [Domain connectivity and overset grid assembly](/definitions/domain-connectivity.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [Conservative overset interface](/methods/conservative-overset-interface.md)
- [Donor search](/methods/donor-search.md)
- [Fluid–structure interaction on overlapping grids](/methods/fluid-structure-interaction-on-overset-grids.md)
- [Hole cutting](/methods/hole-cutting.md)
- [Immersed boundaries on overlapping grids](/methods/immersed-boundary-on-overset-grids.md)
- [Implicit hole cutting](/methods/implicit-hole-cutting.md)
- [Incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Moving overset grids](/methods/moving-overset-grid.md)
- [Parallel and GPU overset grid assembly](/methods/parallel-overset-grid-assembly.md)
- [Wall-distance hole cutting](/methods/wall-distance-hole-cutting.md)
