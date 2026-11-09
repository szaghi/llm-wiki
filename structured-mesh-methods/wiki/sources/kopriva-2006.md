---
type: Source
title: "Kopriva (2006) — Metric identities and the discontinuous spectral element method on curvilinear meshes"
description: "Discrete metric identities for discontinuous spectral elements on curved quadrilaterals and hexahedra: the cross-product form satisfies them in 2-D for isoparametric geometry but not in 3-D, while interpolated conservative and invariant curl forms always do."
resource: "doi:10.1007/s10915-005-9070-8"
source_kind: paper
authors: [Kopriva D.A.]
year: 2006
venue: "J. Sci. Comput. 26(3):301–327"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2006_Crossref_Journal_of_Scientific_Computing_Kopriva_Metric_Identities_and_the_Discontinuous_Spectral_Element_Met.pdf"
tags: [metric-identities, free-stream-preservation, spectral-element, discontinuous-galerkin]
timestamp: 2026-11-08T20:38:00Z
---

# Summary

Kopriva shows that violating the discrete metric identities on curved spectral elements produces stationary errors and spurious acoustic waves ([free-stream preservation](/properties/free-stream-preservation.md)), writes the conservative and invariant forms of the metric terms as curls, and proves which discrete forms satisfy the identities ([conservative metric evaluation](/methods/conservative-metric-evaluation.md)).

# Version read

Version of record, J. Sci. Comput. 26, 301–327 (2006). §§1–2, §7 and §9 read; theorem statements read, proofs not; §8 examples in outline.

# Key claims

1. Unsatisfied metric identities give stationary and propagating spurious errors; a uniform Mach 0.6 flow shows both (§1, Fig. 1). **Shown**
2. The conservative and invariant forms of the metric terms are curls, hence divergence free (§2–§3). **Derived**
3. In 3-D the cross-product form does not satisfy the discrete identities except in special cases; interpolated curl forms always do with Gauss quadrature (Theorems 4–5). **Derived**

# Notation map

| Kopriva (2006) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $J a^i$ | $J\mathbf a^i$ | metric terms |
| $I_N$ | $\mathcal I_k$ | interpolation, $N=k$ |
| $N$ | $k$ | polynomial degree |

# Reference list

26 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 2 (2026-11-08). This source is cited on:

- [Conservative metric evaluation](/methods/conservative-metric-evaluation.md)
- [Free-stream preservation](/properties/free-stream-preservation.md)
