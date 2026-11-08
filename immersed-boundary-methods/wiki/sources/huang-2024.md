---
type: Source
title: "Huang, Yang & Cai (2024) — A high-order no image point sharp interface immersed boundary method for compressible flows"
description: "Third-order ghost-point immersed boundary method for 2D compressible flow without image points: ghost values from a constrained weighted-least-squares Taylor polynomial with the boundary condition at grid-line intersections, in an upwind compact scheme needing one ghost layer."
resource: "doi:10.1063/5.0241364"
source_kind: paper
authors: [Huang C., Yang Y., Cai Q.]
year: 2024
venue: "Phys. Fluids 36(12):126106"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2024_Crossref_Physics_of_Fluids_Huang_A_high-order_no_image_point_sharp_interface_immersed_boundar.pdf"
tags: [ghost-cell, high-order, compressible, compact-scheme]
timestamp: 2026-11-08T18:35:00Z
---

# Summary

Huang, Yang and Cai build a [ghost-cell](/methods/ghost-cell-method.md) treatment that avoids image points, whose location is costly near complex boundaries and in narrow gaps: ghost values are extrapolated from a Taylor polynomial fitted by constrained weighted least squares, with the boundary condition imposed where the geometry cuts grid lines. An upwind compact scheme modified to need one ghost layer gives global third order ([high-order immersed boundary treatments](/methods/high-order-immersed-boundary.md)).

# Version read

Version of record, Phys. Fluids 36, 126106 (2024). §§1–2 read, §3 tests in outline.

# Key claims

1. Image points are costly or hard to place near complex boundaries and in narrow regions (§1). **Stated**
2. Constrained weighted least squares with the boundary condition at grid-line intersections yields ghost values without image points (§2). **Derived**
3. One ghost layer suffices for global third order with the upwind compact scheme (§2–§3). **Shown**
4. Third-order convergence on a smooth bump, a Prandtl–Meyer expansion, a supersonic vortex and a cylinder at $M=0.2$, $Re=40$ (§3). **Shown**

# Notation map

| Huang, Yang & Cai (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $a$, $b$ | dissipation and dispersion parameters of the compact scheme | page-local |

# Reference list

36 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 5 (2026-11-08). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Ghost-cell immersed boundary method](/methods/ghost-cell-method.md)
- [High-order immersed boundary treatments for compressible flow](/methods/high-order-immersed-boundary.md)
