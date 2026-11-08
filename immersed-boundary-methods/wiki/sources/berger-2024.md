---
type: Source
title: "Berger & Giuliani (2024) — A new provably stable weighted state redistribution algorithm"
description: "Weighted state redistribution for cut-cell finite volumes whose weights vanish continuously at the volume-fraction threshold, proved conservative and monotone, TVD and GKS stable in many configurations."
resource: "doi:10.1137/23m1597484"
source_kind: paper
authors: [Berger M., Giuliani A.]
year: 2024
venue: "SIAM J. Sci. Comput. 46(5):A2848–A2873"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2024_Crossref_SIAM_Journal_on_Scientific_Computing_Berger_A_New_Provably_Stable_Weighted_State_Redistribution_Algorith.pdf"
tags: [state-redistribution, cut-cell, stability, small-cell]
timestamp: 2026-11-08T18:48:00Z
---

# Summary

Berger and Giuliani give a weighted [state redistribution](/methods/state-redistribution.md) for the [small-cell problem](/definitions/small-cell-problem.md): weights decrease continuously to zero as a cut cell's volume fraction reaches the threshold, the same weights enter averaging and recombination, and the scheme preserves constants and conserves. They prove monotonicity, TVD and GKS stability for first-order upwinding in many merging configurations and show which central mergings fail.

# Version read

arXiv:2308.16332v2 (April 2024); metadata from the version of record, SIAM J. Sci. Comput. 46, A2848–A2873 (2024). §§1–4 read, §5 tests in outline.

# Key claims

1. The weighted SRD is conservative and constant-preserving (§2). **Derived**
2. First-order upwinding with normal merging at ramp angles up to $45^\circ$ is monotone; $3\times3$ central merging at $45^\circ$ is not (§3–§4). **Derived**
3. With limited reconstruction and SSP Runge–Kutta the second-order scheme is TVD (§4). **Derived**
4. The original SRD is monotone in most configurations, explaining its robustness (§4). **Stated**

# Notation map

| Berger & Giuliani (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $w_{i,j}$ | $w_{\mathbf i\mathbf j}$ | redistribution weights |
| $\hat V$ | weighted neighbourhood volume | page-local |

# Reference list

16 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 5 (2026-11-08). This source is cited on:

- [State redistribution](/methods/state-redistribution.md)
