---
type: Source
title: "de Prenter, Verhoosel, van Brummelen, Larson & Badia (2023) — Stability and conditioning of immersed finite element methods: analysis and remedies"
description: "Review of the stability and conditioning problems that small cut elements cause in immersed finite element methods, with analysis in terms of norm equivalences and detailed treatment of Schwarz preconditioning, element aggregation and ghost-penalty stabilization, including a unified analysis of the last two."
resource: "doi:10.1007/s11831-023-09913-0"
source_kind: paper
authors: [de Prenter F., Verhoosel C.V., van Brummelen E.H., Larson M.G., Badia S.]
year: 2023
venue: "Arch. Comput. Methods Eng. 30(6):3617-3656"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2023_Crossref_Archives_of_Computational_Methods_in_Engineering_de_Stability_and_Conditioning_of_Immersed_Finite_Element_Method.pdf"
tags: [review, finite-element, small-cell, conditioning, ghost-penalty, aggregation]
timestamp: 2026-11-08T18:24:00Z
---

# Summary

de Prenter, Verhoosel, van Brummelen, Larson and Badia review how small cut elements degrade immersed finite element methods, separating stability (Nitsche coercivity) from conditioning (eigenvalues near zero), and compare Schwarz preconditioning, element aggregation and the ghost penalty ([small-cell problem](/definitions/small-cell-problem.md); [CutFEM](/methods/cutfem.md)).

# Version read

Research Square preprint (DOI 10.21203/rs.3.rs-1970859/v1 on page 1), 62 pages, of the published paper. Framework and remedies sections read for their statements; the detailed proofs skimmed. Metadata are the published identity from Crossref.

# Key claims

1. Small cut elements cause stability problems (unbounded Nitsche parameters) and conditioning problems (eigenvalues approaching zero), which must be distinguished (§2). **Stated**
2. The condition number grows as an inverse power of the smallest volume fraction that increases with polynomial order; the cut shape is not dominant without diagonal scaling (§3). **Derived**/**Shown** (cited)
3. Schwarz preconditioning resolves conditioning; aggregation and ghost penalty resolve stability and conditioning (§3–§4). **Stated**
4. Aggregation and ghost-penalty stabilization admit a unified analysis (§4.5). **Derived**
5. Formulations avoiding Nitsche's penalty, such as the shifted boundary method, sidestep the stability problem at the cost of other properties (§4.2). **Stated**

# Notation map

| de Prenter, Verhoosel, van Brummelen, Larson & Badia (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\eta_i$, $\eta$ | element volume fraction, smallest volume fraction | $\kappa$; registry $\eta$ is the penalty parameter |

# Reference list

All 252 entries of the Crossref deposit of the published reference list are merged complete into the [bibliography](/bibliography.md).

# Pages created or updated

Chunk 4 (2026-11-08). This source is cited on:

- [Small-cell problem](/definitions/small-cell-problem.md)
- [CutFEM (cut finite element method)](/methods/cutfem.md)
