---
type: Source
title: "Sharan, Brady & Livescu (2022) — High-order dimensionally-split Cartesian embedded boundary method for non-dissipative schemes"
description: "Dimensionally split finite-difference embedded-boundary stencils satisfying discrete primary and secondary (energy) conservation in summation-by-parts form, provably time stable without dissipation, up to sixth order inside and fourth order globally, and free of the small-cell problem."
resource: "doi:10.1016/j.jcp.2022.111341"
source_kind: paper
authors: [Sharan N., Brady P.T., Livescu D.]
year: 2022
venue: "J. Comput. Phys. 464:111341"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2022_Crossref_Journal_of_Computational_Physics_Sharan_High-order_dimensionally-split_Cartesian_embedded_boundary_m.pdf"
tags: [cut-cell, embedded-boundary, high-order, summation-by-parts, small-cell, finite-difference]
timestamp: 2026-11-08T18:26:00Z
---

# Summary

Sharan, Brady and Livescu build embedded-boundary stencils for non-dissipative centred finite differences ([cut-cell method](/methods/cut-cell-method.md)): along each grid line the first interval next to the boundary is shortened, and first- and second-derivative operators are derived to satisfy discrete primary and secondary conservation (a summation-by-parts structure with weak boundary imposition), so long-time stability holds without artificial dissipation. The stencils need no cut-cell volumes and have no [small-cell problem](/definitions/small-cell-problem.md).

# Version read

Los Alamos accepted manuscript (LA-UR-21-30871). §§1–3 read in full, §§4–5 (tests) for results. Title and authors match Crossref.

# Key claims

1. Non-dissipative schemes need boundary treatments stable without artificial dissipation; earlier Taylor-based EB stencils were not stable in the inviscid limit (§1). **Stated**
2. Dimensionally split stencils avoid surface and volume reconstruction (§1). **Stated**
3. Operators satisfying discrete primary and secondary conservation with a positive norm matrix give time stability (§2–§3). **Derived**
4. Up to sixth order in the interior and fourth order globally for hyperbolic, parabolic and incompletely parabolic problems; observed global $p+1$ (first derivative) and $p+2$ (second derivative, $p\ge2$) (§4). **Shown**
5. All tests run at CFL 0.5 for arbitrary cut distances: no small-cell problem (§4–§5). **Shown**
6. An isentropic vortex crossing embedded boundaries stays bounded, with reflections but no instability (§5). **Shown**

# Notation map

| Sharan, Brady & Livescu (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $D_1$, $D_2$, $W$ | first- and second-derivative operators, norm matrix | page-local |
| $\alpha_l$, $\alpha_r$ | cut-distance fractions | page-local |
| $2p$ | interior order | registry order $r$ |

# Reference list

49 references, merged complete into the [bibliography](/bibliography.md)
from the Crossref deposited list.

# Pages created or updated

Chunk 4 (2026-11-08). This source is cited on:

- [Small-cell problem](/definitions/small-cell-problem.md)
- [Cut-cell (embedded-boundary) finite-volume method](/methods/cut-cell-method.md)
