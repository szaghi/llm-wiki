---
type: Source
title: "Johnen, Remacle & Geuzaine (2013) — Geometrical validity of curvilinear finite elements"
description: "Provable bounds on the Jacobian determinant of curved polynomial elements from its Bézier expansion with adaptive subdivision, giving a sharp validity test and a distortion measure for all element types."
resource: "doi:10.1016/j.jcp.2012.08.051"
source_kind: paper
authors: [Johnen A., Remacle J.-F., Geuzaine C.]
year: 2013
venue: "J. Comput. Phys. 233:359–372"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2013_Crossref_Journal_of_Computational_Physics_Johnen_Geometrical_validity_of_curvilinear_finite_elements.pdf"
tags: [high-order-mesh, validity, bezier-bounds]
timestamp: 2026-11-08T20:38:00Z
---

# Summary

Johnen, Remacle and Geuzaine decide the [validity of curved elements](/definitions/high-order-mesh-validity.md) exactly: the Jacobian determinant is a polynomial, its Bézier coefficients bound it, and subdivision sharpens the bound.

# Version read

Version of record, J. Comput. Phys. 233, 359–372 (2013). Read in full; examples in outline.

# Key claims

1. Sampling the Jacobian gives only a necessary condition, and more points can lower the prediction accuracy (§2, §5). **Shown**
2. The Bézier expansion bounds the Jacobian determinant, and adaptive subdivision converges quadratically (§3–§4). **Derived**
3. 8,112 invalid elements among 82,009 sixth-order triangles are detected in about 2 s (§5). **Shown**

# Notation map

| Johnen, Remacle & Geuzaine (2013) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $J(\xi)=\det X_{,\xi}$ | $J$ |  |
| $d(\xi)$ | $\mathcal D$ | distortion |
| $p$ | $k$ |  |

# Reference list

10 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 2 (2026-11-08). This source is cited on:

- [Validity of high-order curvilinear elements](/definitions/high-order-mesh-validity.md)
- [Mesh quality metric](/definitions/mesh-quality-metric.md)
