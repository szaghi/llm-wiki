---
type: Source
title: "Huang, Ren & Russell (1994) — Moving mesh partial differential equations (MMPDES) based on the equidistribution principle"
description: "Continuous moving mesh equations derived from the equidistribution principle, analysed for stability and mesh crossing; versions relaxing toward equidistribution are robust and crossing-free."
resource: "doi:10.1137/0731038"
source_kind: paper
authors: [Huang W., Ren Y., Russell R.D.]
year: 1994
venue: "SIAM J. Numer. Anal. 31(3):709–730"
local_file: "/home/stefano/papers/mosaic/structured-mesh/1994_Crossref_SIAM_Journal_on_Numerical_Analysis_Huang_Moving_Mesh_Partial_Differential_Equations_MMPDES_Based_on_t.pdf"
tags: [moving-mesh, equidistribution, adaptation]
timestamp: 2026-11-08T20:27:00Z
---

# Summary

Huang, Ren and Russell write moving mesh methods as continuous [moving mesh PDEs](/methods/moving-mesh-pde.md) derived from the [equidistribution principle](/definitions/equidistribution-principle.md), and show that a relaxation term measuring the level of equidistribution makes them stable and free of mesh crossing.

# Version read

Version of record, SIAM J. Numer. Anal. 31, 709–730 (1994). §§1–3 and §5 read; §4 experiments in outline.

# Key claims

1. Static and dynamic adaptive methods differ in interpolation and in node count (§1). **Stated**
2. MMPDE1, the time-differentiated principle, can cross and drifts from equidistribution (§3, §5). **Shown**
3. MMPDE2–4 and MMPDE6 cannot cross under weak assumptions; their deviation from equidistribution is small for small $\tau$ (§3, §5). **Derived**

# Notation map

| Huang, Ren & Russell (1994) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\theta(t)$ | $\theta_M(t)$ | total monitor |
| $M(x,t)$ | $M$ |  |
| $\tau$ | $\tau$ | relaxation time |

# Reference list

22 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 1 (2026-11-08). This source is cited on:

- [Equidistribution principle](/definitions/equidistribution-principle.md)
- [Moving mesh partial differential equations](/methods/moving-mesh-pde.md)
