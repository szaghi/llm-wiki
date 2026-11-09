---
type: Source
title: "Barrera, Kolev, Mittal & Tomov (2023) — High-order mesh morphing for boundary and interface fitting to implicit geometries"
description: "Morphing high-order meshes so that selected faces fit the zero isocontour of a discrete level-set function, by adding an adaptive fitting penalty to target-matrix optimization and representing the level set on an adaptive background mesh."
resource: "doi:10.1016/j.cad.2023.103499"
source_kind: paper
authors: [Barrera J.-L., Kolev T., Mittal K., Tomov V.]
year: 2023
venue: "Comput.-Aided Des. 158:103499"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2023_Crossref_Computer-Aided_Design_Barrera_High-Order_Mesh_Morphing_for_Boundary_and_Interface_Fitting.pdf"
tags: [mesh-optimization, target-matrix, implicit-geometry, high-order-mesh]
timestamp: 2026-11-08T20:54:00Z
---

# Summary

Barrera et al. fit high-order meshes to implicitly defined boundaries and interfaces with a penalty term in [target-matrix optimization](/methods/target-matrix-optimization.md).

# Version read

arXiv:2208.05062v2 (6 February 2023); metadata from the version of record, Comput.-Aided Des. 158, 103499 (2023). Abstract and §§1–3 read; conclusions by structure; examples in outline.

# Key claims

1. A penalty on the level-set values at selected nodes weakly enforces fitting while TMOP keeps quality (§3). **Stated**
2. Adaptive choice of the fitted faces and of the penalty weight, and a refined background mesh for the level set, make fitting robust (§3). **Shown**

# Notation map

| Barrera, Kolev, Mittal & Tomov (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\sigma(\mathbf x)$, $w_\sigma$ | $\sigma$, $w_\sigma$ |  |

# Reference list

47 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 4 (2026-11-08). This source is cited on:

- [Target-matrix optimization (TMOP)](/methods/target-matrix-optimization.md)
