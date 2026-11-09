---
type: Source
title: "Brackbill & Saltzman (1982) — Adaptive zoning for singular problems in two dimensions"
description: "Variational mesh generation minimizing a weighted sum of smoothness, orthogonality and weighted-volume functionals; a solution-dependent weight adapts the mesh and reduces the error of singular problems several-fold."
resource: "doi:10.1016/0021-9991(82)90020-1"
source_kind: paper
authors: [Brackbill J.U., Saltzman J.S.]
year: 1982
venue: "J. Comput. Phys. 46(3):342–368"
local_file: "/home/stefano/papers/mosaic/structured-mesh/1982_Crossref_Journal_of_Computational_Physics_Brackbill_Adaptive_zoning_for_singular_problems_in_two_dimensions.pdf"
tags: [variational-generation, adaptation, grid-generation]
timestamp: 2026-11-08T20:27:00Z
---

# Summary

Brackbill and Saltzman extend Winslow's generator by a variational principle combining integral measures of smoothness, orthogonality and weighted cell volume ([variational grid generation](/methods/variational-grid-generation.md)), and show that the weighted-volume term adapts the mesh to singular solutions.

# Version read

Version of record (scan with text layer), J. Comput. Phys. 46, 342–368 (1982). §§1–3 and the conclusion read; §4 by examples. Initials completed from page 1.

# Key claims

1. Orthogonality and volume-variation functionals alone have non-unique minimizers and are combined with the smoothness functional (§2). **Derived**
2. Increasing the volume weight increases volume variation at the expense of smoothness; the volume-weighted orthogonality term is compatible with volume control (§4). **Shown**
3. With adaptive weights the error of a 2-D singular problem falls from 25 % to 3.5 % (§4). **Shown**

# Notation map

| Brackbill & Saltzman (1982) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $I_S$, $I_O$, $I_V$ | $I_s$, $I_o$, $I_v$ |  |
| $\lambda_O$, $\lambda_V$ | $\lambda_o$, $\lambda_v$ |  |
| $w$ | $w$ | weight function |

# Reference list

25 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 1 (2026-11-08). This source is cited on:

- [Equidistribution principle](/definitions/equidistribution-principle.md)
- [Variational grid generation](/methods/variational-grid-generation.md)
