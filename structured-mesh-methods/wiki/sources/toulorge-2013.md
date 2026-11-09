---
type: Source
title: "Toulorge, Geuzaine, Remacle & Lambrechts (2013) — Robust untangling of curvilinear meshes"
description: "Untangling of high-order curvilinear meshes by unconstrained optimization with moving log-barriers on the element distortion, applied locally around invalid elements, with a metric-eigenvalue term that controls the explicit stable time step."
resource: "doi:10.1016/j.jcp.2013.07.022"
source_kind: paper
authors: [Toulorge T., Geuzaine C., Remacle J.-F., Lambrechts J.]
year: 2013
venue: "J. Comput. Phys. 254:8–26"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2013_Crossref_Journal_of_Computational_Physics_Toulorge_Robust_untangling_of_curvilinear_meshes.pdf"
tags: [high-order-mesh, untangling, mesh-optimization]
timestamp: 2026-11-08T21:10:00Z
---

# Summary

Toulorge et al. untangle curved meshes by optimizing node positions under moving barriers on the distortion ([high-order mesh curving](/methods/high-order-mesh-curving.md)), and show that the element metric, not only the Jacobian, governs the stable time step of explicit schemes.

# Version read

Preprint submitted to J. Comput. Phys. (author version); metadata from the version of record, J. Comput. Phys. 254, 8–26 (2013). §§1–4, §6 and §7 read; §5 examples in outline.

# Key claims

1. Linear smoothers (Laplacian, Winslow, linear elasticity) do not guarantee untangling (§1). **Stated**
2. A sequence of optimizations with a barrier moved from below the current minimum into the valid range untangles curved meshes, locally in groups of element layers (§4–§5). **Shown**
3. Curved elements with equal constant Jacobian can have different stable time steps; a barrier on the metric's smallest eigenvalue enlarges them (§6). **Shown**

# Notation map

| Toulorge, Geuzaine, Remacle & Lambrechts (2013) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| scaled Jacobian $J/J_0$ | $\mathcal D$ |  |
| $\epsilon$ | barrier threshold | page-local |
| $M$ | element metric tensor | page-local; not the registry monitor $M$ |

# Reference list

33 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 2 (2026-11-08). This source is cited on:

- [High-order mesh curving](/methods/high-order-mesh-curving.md)
