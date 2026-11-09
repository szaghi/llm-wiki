---
type: Source
title: "Knupp (2001) — Algebraic mesh quality metrics"
description: "A mathematical theory of mesh quality metrics built on element Jacobians referenced to an ideal element: factorization into orientation, volume and shape, algebraic shape metrics, and the condition number as distance to degeneracy, equivalent to the mean ratio."
resource: "doi:10.1137/s1064827500371499"
source_kind: paper
authors: [Knupp P.M.]
year: 2001
venue: "SIAM J. Sci. Comput. 23(1):193–218"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2001_Crossref_SIAM_Journal_on_Scientific_Computing_Knupp_Algebraic_Mesh_Quality_Metrics.pdf"
tags: [mesh-quality, element-jacobian, target-matrix]
timestamp: 2026-11-08T20:27:00Z
---

# Summary

Knupp gives the first algebraic theory of [mesh quality metrics](/definitions/mesh-quality-metric.md): metrics are functions of the element Jacobian relative to an ideal element, and properties such as shape, skew, length ratio, volume and orientation are defined abstractly, with equivalences proved through singular values.

# Version read

Version of record, SIAM J. Sci. Comput. 23, 193–218 (2001). §§1–9 and the conclusions read; §§10–14 by definitions.

# Key claims

1. Metrics are referenced to an ideal element through $\mathsf T=\mathsf A\mathsf W^{-1}$ (§5–§6). **Stated**
2. $d/\kappa(\mathsf T)$ is an algebraic shape metric and $\kappa$ measures the distance to degenerate elements (§9). **Derived**
3. Condition-number and mean-ratio metrics are equivalent (§8–§9). **Derived**

# Notation map

| Knupp (2001) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $A$, $W$, $T$ | $\mathsf A$, $\mathsf W$, $\mathsf T$ |  |
| $\tau=\det T$ | $\det\mathsf T$ | page-local; $\tau$ is the registry relaxation time |
| $n$ | $d$ | space dimension |

# Reference list

24 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 1 (2026-11-08). This source is cited on:

- [Mesh quality metric](/definitions/mesh-quality-metric.md)
