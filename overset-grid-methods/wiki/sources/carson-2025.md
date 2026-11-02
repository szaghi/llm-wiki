---
type: Source
title: "Carson et al. (2025) — High-order accurate implicit–explicit time-stepping schemes for wave equations on overset grids"
description: "Single-step, three-level implicit modified-equation schemes of second and fourth order for wave equations in second-order form on overset grids, with upwind dissipation for stability, and a spatially partitioned implicit–explicit scheme that integrates component grids with small cells implicitly and the others explicitly."
resource: "doi:10.1016/j.jcp.2024.113513"
source_kind: paper
authors: [Carson A.M., Banks J.W., Henshaw W.D., Schwendeman D.W.]
year: 2025
venue: "J. Comput. Phys. 520:113513"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2025_Crossref_Journal_of_Computational_Physics_Carson_High-order_accurate_implicit-explicit_time-stepping_schemes.pdf"
tags: [wave-equation, imex, finite-difference, stability, high-order]
timestamp: 2026-11-02T15:25:00Z
---

# Summary

Wave problems on overset grids can be geometrically stiff: small cells needed to resolve fine features limit the explicit time step. Carson et al. build implicit modified-equation (IME) schemes — single step, three time levels, second and fourth order — for the wave equation in second-order form, with upwind dissipation added (preferably in a separate explicit predictor–corrector step) for stability on overset grids, and derive conditions for accuracy and unconditional stability. A spatially partitioned implicit–explicit (SPIE) scheme integrates component grids with small cells implicitly and the others (such as background Cartesian grids) explicitly ([IMEX time stepping on overlapping grids](/methods/imex-time-stepping-on-overset-grids.md), [upwind schemes for wave equations](/methods/upwind-wave-equation-overset.md)).

# Version read

arXiv preprint 2404.14592v1 (24 April 2024), 48 pages. Read in a targeted way (abstract, introduction, section structure, main results and conclusions closely; derivations and remaining results skimmed): from chunk 4 on, the bundle is compiled in the main session without reader subagents, by the owner's instruction. Claims below are limited to what was read closely.

# Key claims

1. Implicit modified-equation schemes are single step and three-level in time, second- and fourth-order accurate; the implied coefficient matrix is definite and suited to Krylov methods or multigrid (Abstract, Conclusions). **Derived**
2. Conditions for accuracy and unconditional stability of the IME schemes are derived (Conclusions). **Derived**
3. Upwind dissipation is incorporated for stability on overset grids; adding it in a separate explicit predictor–corrector step is useful (Abstract, Conclusions). **Stated**
4. The spatially partitioned implicit–explicit scheme, implicit on component grids with small cells and explicit elsewhere, can be many times faster and more accurate than the explicit scheme everywhere on geometrically stiff problems (Abstract, Conclusions). **Shown**
5. Fully implicit schemes allow very large time steps, useful e.g. for the WaveHoltz algorithm for Helmholtz problems (Abstract). **Stated**

# Printed slips

None recorded (targeted reading).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| IME, EME | implicit, explicit modified-equation schemes | |
| SPIE | spatially partitioned implicit–explicit scheme | |

# Reference list

45 references, merged complete into the [bibliography](/bibliography.md) with `citedby` carson-2025, from the Crossref deposited reference list. [Angel et al. (2023)](/sources/angel-2023.md) is cited; Ogen is `henshaw-1998`.

# Pages created or updated

Chunk 4 (2026-11-02). This source is cited on:

- [High-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md)
- [Implicit–explicit time stepping on overlapping grids](/methods/imex-time-stepping-on-overset-grids.md)
- [Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md)
- [Upwind schemes for wave equations on overlapping grids](/methods/upwind-wave-equation-overset.md)
