---
type: Source
title: "Cicchino, Del Rey Fernández, Nadarajah, Chan & Carpenter (2022) — Provably stable flux reconstruction high-order methods on curvilinear elements"
description: "Provably stable energy-stable flux reconstruction on curvilinear elements: conservative and non-conservative DG forms differ even with exact metrics, so split forms and metric-dependent correction functions on the full split form are required."
resource: "doi:10.1016/j.jcp.2022.111259"
source_kind: paper
authors: [Cicchino A., Del Rey Fernández D.C., Nadarajah S., Chan J., Carpenter M.H.]
year: 2022
venue: "J. Comput. Phys. 463:111259"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2022_Crossref_Journal_of_Computational_Physics_Cicchino_Provably_stable_flux_reconstruction_high-order_methods_on_cu.pdf"
tags: [flux-reconstruction, curvilinear-element, stability, metric-identities]
timestamp: 2026-11-08T20:47:00Z
---

# Summary

Cicchino et al. show that curved elements break the equivalence of DG strong forms and build provably stable flux reconstruction on them ([free-stream preservation](/properties/free-stream-preservation.md); [conservative metric evaluation](/methods/conservative-metric-evaluation.md)).

# Version read

Preprint submitted to J. Comput. Phys.; metadata from the version of record, J. Comput. Phys. 463, 111259 (2022). Abstract, introduction, Theorem 1, the metric-term appendix and conclusions read.

# Key claims

1. Discrete integration by parts fails in physical space on curvilinear elements even with exact integration and metrics (Theorem 1). **Derived**
2. Correction functions must act on the full split form; surface-only use diverges (results). **Shown**
3. Optimal convergence orders on a heavily warped 3-D grid (conclusions). **Shown**

# Notation map

| Cicchino, Del Rey Fernández, Nadarajah, Chan & Carpenter (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $C$ | metric cofactor matrix $J\mathbf a^i$ |  |
| ESFR | energy-stable flux reconstruction |  |

# Reference list

84 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 3 (2026-11-08). This source is cited on:

- [Conservative metric evaluation](/methods/conservative-metric-evaluation.md)
- [Free-stream preservation](/properties/free-stream-preservation.md)
