---
type: Source
title: "Burman, Hansbo, Larson & Zahedi (2025) — Cut finite element methods"
description: "Acta Numerica review of CutFEM: active meshes, weakly imposed conditions, error and condition-number analysis, weak (ghost-penalty) and strong (extension) stabilization, surface PDEs, Lagrange multipliers and time-dependent domains."
resource: "doi:10.1017/s0962492925000017"
source_kind: paper
authors: [Burman E., Hansbo P., Larson M.G., Zahedi S.]
year: 2025
venue: "Acta Numer. 34:1–121"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2025_Crossref_Acta_Numerica_Burman_Cut_finite_element_methods.pdf"
tags: [cutfem, review, ghost-penalty, stabilization]
timestamp: 2026-11-08T18:35:00Z
---

# Summary

Burman, Hansbo, Larson and Zahedi review [CutFEM](/methods/cutfem.md): finite element spaces on active meshes of elements meeting the domain, boundary and interface conditions imposed weakly, and robustness with respect to the geometry–mesh position obtained by ghost-penalty stabilization or by extension that eliminates unstable degrees of freedom, connected to each other in the review.

# Version read

Version of record (open access), Acta Numer. 34, 1–121 (2025). Scoped reading: abstract, contents and §1 in full; §§2–9 by structure and key statements; proofs not read.

# Key claims

1. Robustness with respect to the position of the geometry relative to the mesh is the design goal, achieved by stabilization that also bounds the condition number (§1, §3–§4). **Stated**
2. Strong stabilization by extension is connected to weak ghost-penalty stabilization (§6). **Stated**
3. The framework extends to surface PDEs, Lagrange multipliers and hybridization, and time-dependent domains (§5, §7, §9). **Stated**

# Notation map

| Burman, Hansbo, Larson & Zahedi (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathcal T_h$ | active mesh (elements meeting the domain) | page-local; the registry has no CutFEM mesh symbol |
| $g_h$ | ghost-penalty form | page-local |

# Reference list

224 references, transcribed from the printed alphabetical list (no Crossref deposit) and merged complete into the [bibliography](/bibliography.md); the reference extraction covers the whole list although the reading is scoped.

# Pages created or updated

Chunk 5 (2026-11-08). This source is cited on:

- [CutFEM (cut finite element method)](/methods/cutfem.md)
