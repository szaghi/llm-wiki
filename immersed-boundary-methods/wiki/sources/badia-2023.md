---
type: Source
title: "Badia, Dilip & Verdugo (2023) — Space-time unfitted finite element methods for time-dependent problems on moving domains"
description: "Space-time unfitted finite element method for parabolic problems on moving domains: unfitted elements in space and discontinuous Galerkin in time, made robust to the cut location by slab-wise cell aggregation (or a space-time ghost penalty), with stability, condition-number and optimal error estimates."
resource: "doi:10.1016/j.camwa.2023.01.032"
source_kind: paper
authors: [Badia S., Dilip H., Verdugo F.]
year: 2023
venue: "Comput. Math. Appl. 135:60–76"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2023_Crossref_Computers_amp_Mathematics_with_Applications_Badia_Space-time_unfitted_finite_element_methods_for_time-dependen.pdf"
tags: [unfitted, aggregation, space-time, moving-boundary, conditioning]
timestamp: 2026-11-13T05:49:40Z
---

# Summary

Badia, Dilip and Verdugo combine an unfitted finite element discretization in space with a discontinuous Galerkin method in time for parabolic problems on moving domains. The aggregated finite element method is extended to space-time slab by slab, so that the discrete space is a tensor product of spatial and temporal spaces on each slab; this gives robustness to the cut location ([small-cell problem](/definitions/small-cell-problem.md), [cell merging](/methods/cell-merging.md)) and optimal error estimates. A space-time ghost penalty is the alternative ([CutFEM](/methods/cutfem.md)).

# Version read

arXiv:2206.03626v2 (20 January 2023), the accepted manuscript; metadata from the version of record, Comput. Math. Appl. 135, 60–76 (2023). §§1–3 read, §4 by statement, §5 in outline, §6.

# Key claims

1. Small cut cells make unfitted finite element matrices almost singular; few unfitted formulations for moving domains are both robust to the cut and optimally convergent (§1). **Stated**
2. A space-time cell is well posed when its in-domain fraction over the slab exceeds a threshold; aggregating slab by slab gives a tensor-product space-time space (§2). **Derived**
3. The method is well posed and stable, with condition-number bounds independent of the cut location and optimal anisotropic a priori error estimates for the heat equation on moving domains (§4). **Derived**
4. Condition numbers of mass and stiffness matrices stay bounded as a disk moves across the mesh, unlike the unaggregated space-time method; the error converges at the expected rates; a mass transfer problem with a change of topology is solved (§5). **Shown**

# Notation map

| Badia, Dilip & Verdugo (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Omega(t)$ | $\Omega_f$ | the moving physical domain |
| $J^n$, $Q^n$ | time slab, space-time slab domain | page-local |
| $\eta^n(T^n)$, $\eta_0$ | in-domain fraction of a space-time cell, threshold | page-local: clashes with the registry penalization parameter $\eta$ |
| $p$, $q$ | spatial and temporal polynomial degrees | page-local: the registry writes $k$; $p$ is pressure |

# Reference list

57 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 7 (2026-11-13). This source is cited on:

- [Small-cell problem](/definitions/small-cell-problem.md)
- [Cell merging for cut cells](/methods/cell-merging.md)
- [CutFEM (cut finite element method)](/methods/cutfem.md)
