---
type: Source
title: "Steger & Sorenson (1979) — Automatic mesh-point clustering near a boundary in grid generation with elliptic partial differential equations"
description: "Control functions of the elliptic generator that decay away from the inner boundary and are solved for iteratively so that the grid has a prescribed first spacing and intersects the boundary at a prescribed angle."
resource: "doi:10.1016/0021-9991(79)90165-7"
source_kind: paper
authors: [Steger J.L., Sorenson R.L.]
year: 1979
venue: "J. Comput. Phys. 33(3):405–410"
local_file: "/home/stefano/papers/mosaic/structured-mesh/1979_Crossref_Journal_of_Computational_Physics_Steger_Automatic_mesh-point_clustering_near_a_boundary_in_grid_gene.pdf"
tags: [elliptic-generation, clustering, orthogonality, control-functions]
timestamp: 2026-11-08T20:27:00Z
---

# Summary

Steger and Sorenson make the control functions of [elliptic grid generation](/methods/elliptic-grid-generation.md) automatic near a boundary: exponentially decaying $P,Q$ whose boundary values follow from imposing a first spacing and an intersection angle, updated during the relaxation. Airfoil grids with spacings down to $10^{-5}$ chord result.

# Version read

Version of record (note), J. Comput. Phys. 33, 405–410 (1979). Read in full. Authors' initials completed from page 1.

# Key claims

1. No automatic way to choose $P,Q$ for a desired clustering had existed (introduction). **Stated**
2. Evaluating the generator on the boundary, with prescribed spacing and angle, gives two equations for the boundary values of the control functions (method). **Derived**
3. One-sided differencing of the forcing derivatives and small relaxation factors keep the iteration stable (method). **Stated**
4. Orthogonal airfoil grids with prescribed first spacing are produced (results). **Shown**

# Notation map

| Steger & Sorenson (1979) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $P_1$, $Q_1$, $a$, $b$ | control-function amplitudes and decay rates | page-local |
| $ds$ | $\Delta s$ | first spacing |
| $\theta$ | boundary intersection angle | page-local use of the registry angle |

# Reference list

12 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 1 (2026-11-08). This source is cited on:

- [Elliptic grid generation](/methods/elliptic-grid-generation.md)
