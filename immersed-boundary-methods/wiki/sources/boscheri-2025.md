---
type: Source
title: "Boscheri & Ciallella (2025) — High order treatment of moving curved boundaries: Arbitrary-Lagrangian-Eulerian methods with a shifted boundary polynomial correction"
description: "Shifted boundary polynomial correction in a direct high-order ALE finite volume scheme on moving straight-sided simplicial meshes: boundary data are corrected by one extra evaluation of the cell polynomial at the true curved boundary, recovering design order up to fourth."
resource: "doi:10.1016/j.jcp.2025.114215"
source_kind: paper
authors: [Boscheri W., Ciallella M.]
year: 2025
venue: "J. Comput. Phys. 539:114215"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2025_Crossref_Journal_of_Computational_Physics_Boscheri_High_order_treatment_of_moving_curved_boundaries_Arbitrary-L.pdf"
tags: [shifted-boundary, high-order, moving-mesh, curved-boundary, compressible]
timestamp: 2026-11-08T18:44:00Z
---

# Summary

Boscheri and Ciallella treat curved moving walls in a body-fitted direct arbitrary Lagrangian–Eulerian finite volume scheme on straight-sided simplicial meshes. The polygonal mesh boundary is a surrogate of the true wall; following the [shifted boundary method](/methods/shifted-boundary-method.md), the boundary data are corrected, here not by explicit Taylor terms but by the difference of the cell's reconstruction polynomial between the true and the surrogate point.

# Version read

Version of record, J. Comput. Phys. 539, 114215 (2025). §1 and §4 read in full, §3 in outline, §5 results.

# Key claims

1. The sum of all Taylor correction terms equals the difference of the cell polynomial between the true and the surrogate boundary point, so one extra polynomial evaluation replaces them (§4). **Derived**
2. On linear meshes slip walls lose order through the edge normals; the normal velocity is corrected with the true normal (§4). **Stated**
3. Without the correction every polynomial degree converges at second order; with it the design order is recovered on 2D and 3D manufactured moving-domain solutions (§5). **Shown**
4. Kidder's isentropic compression converges up to fourth order on moving tetrahedra, presented as the first convergence analysis above second order for this problem (§5). **Shown**

# Notation map

| Boscheri & Ciallella (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\partial\Omega_h$ | $\tilde\Gamma$ | surrogate boundary |
| $d(\tilde x)\,n$ | $\mathbf d$ |  |
| $\phi_D$ | $u_D$ | Dirichlet datum; page-local |

# Reference list

69 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 6 (2026-11-08). This source is cited on:

- [Shifted boundary method](/methods/shifted-boundary-method.md)
