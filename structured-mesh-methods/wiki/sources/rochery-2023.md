---
type: Source
title: "Rochery & Loseille (2023) — Fast high-order mesh correction for metric-based cavity remeshing and a posteriori curving of P2 tetrahedral meshes"
description: "Correction of curved meshes by linear programs that maximize the smallest Bézier control coefficient of the Jacobian per control point, with Riemannian edge-length curving and a cavity operator for P2 meshes."
resource: "doi:10.1016/j.cad.2023.103575"
source_kind: paper
authors: [Rochery L., Loseille A.]
year: 2023
venue: "Comput.-Aided Des. 163:103575"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2023_Crossref_Computer-Aided_Design_Rochery_Fast_High-Order_Mesh_Correction_for_Metric-Based_Cavity_Reme.pdf"
tags: [high-order-mesh, correction, anisotropic-adaptation, validity]
timestamp: 2026-11-08T20:54:00Z
---

# Summary

Rochery and Loseille correct curved meshes exactly and fast by linear programming on Bézier control coefficients ([high-order mesh curving](/methods/high-order-mesh-curving.md); [validity](/definitions/high-order-mesh-validity.md)) and extend metric-based cavity remeshing to second-order meshes.

# Version read

Version of record, Comput.-Aided Des. 163, 103575 (2023). Abstract and §1 read; method by structure; results in outline.

# Key claims

1. Maximizing the minimum control coefficient that depends on one control point is a linear program; the simplex method gives the global optimum in about eight evaluations (abstract, method). **Derived**
2. P2 tetrahedral meshes of up to 20 million elements are corrected in 10 s to 3.5 min (results). **Shown**

# Notation map

| Rochery & Loseille (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $N_i$ | Bézier control coefficients of $J$ | page-local |
| P2 | degree $k=2$ |  |

# Reference list

77 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 4 (2026-11-08). This source is cited on:

- [Validity of high-order curvilinear elements](/definitions/high-order-mesh-validity.md)
- [High-order mesh curving](/methods/high-order-mesh-curving.md)
