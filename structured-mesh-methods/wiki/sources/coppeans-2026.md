---
type: Source
title: "Coppeans, Fidkowski & Martins (2026) — Anisotropic mesh adaptation for high-order meshes in two dimensions"
description: "Metric-based anisotropic adaptation directly on curved high-order meshes with high-order edge split, collapse, swap and node movement that reject invalid elements, avoiding linearization and re-curving."
resource: "doi:10.1016/j.jcp.2025.114506"
source_kind: paper
authors: [Coppeans A.W.C., Fidkowski K.J., Martins J.R.R.A.]
year: 2026
venue: "J. Comput. Phys. 545:114506"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2026_Crossref_Journal_of_Computational_Physics_Coppeans_Anisotropic_mesh_adaptation_for_high-Order_meshes_in_two_dim.pdf"
tags: [anisotropic-adaptation, high-order-mesh, validity, discontinuous-galerkin]
timestamp: 2026-11-08T21:07:00Z
---

# Summary

Coppeans, Fidkowski and Martins keep meshes curved and valid throughout [anisotropic mesh adaptation](/methods/anisotropic-mesh-adaptation.md).

# Version read

Version of record, J. Comput. Phys. 545, 114506 (2026). Abstract, §1, §§5–6 by structure and §8 read.

# Key claims

1. Linearizing a valid curved mesh can invert elements and re-curving can fail (§1). **Stated**
2. High-order edge primitives that reject invalid operations keep valid curved meshes and recover optimal error convergence (§6–§8). **Shown**

# Notation map

| Coppeans, Fidkowski & Martins (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| HOEP | high-order edge primitives |  |
| MOESS | metric optimization by error sampling and synthesis |  |

# Reference list

57 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 6 (2026-11-08). This source is cited on:

- [Validity of high-order curvilinear elements](/definitions/high-order-mesh-validity.md)
- [Anisotropic mesh adaptation](/methods/anisotropic-mesh-adaptation.md)
