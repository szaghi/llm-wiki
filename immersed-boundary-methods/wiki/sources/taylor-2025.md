---
type: Source
title: "Taylor, Wilcox & Chan (2025) — An energy stable high-order cut cell discontinuous Galerkin method with state redistribution for wave propagation"
description: "Proof that state redistribution, viewed as an L2-contractive filter, preserves the energy stability of a skew-symmetric high-order DG discretization of the acoustic wave equation on Cartesian cut meshes with arbitrary quadrature."
resource: "doi:10.1016/j.jcp.2024.113528"
source_kind: paper
authors: [Taylor C.G., Wilcox L.C., Chan J.]
year: 2025
venue: "J. Comput. Phys. 521:113528"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2025_Crossref_Journal_of_Computational_Physics_Taylor_An_energy_stable_high-order_cut_cell_discontinuous_Galerkin.pdf"
tags: [state-redistribution, discontinuous-galerkin, cut-cell, energy-stability, small-cell]
timestamp: 2026-11-08T18:44:00Z
---

# Summary

Taylor, Wilcox and Chan pair [state redistribution](/methods/state-redistribution.md) with a skew-symmetric DG scheme that is $L^2$ energy stable for arbitrary quadrature on cut elements, and prove that redistribution — a volume-weighted $L^2$ projection on merging neighbourhoods, hence contractive — keeps the scheme energy stable. They also survey remedies for the [small-cell problem](/definitions/small-cell-problem.md).

# Version read

arXiv:2404.06630v2 (23 April 2024); metadata from the version of record, J. Comput. Phys. 521, 113528 (2025). §§1–2 read in full, §3 in outline.

# Key claims

1. The skew-symmetric DG form is $L^2$ energy stable for arbitrary volume quadrature on cut meshes (§2). **Stated**
2. The state redistribution operator is contractive in $L^2$ (Theorem 2.1) and the DG scheme with redistribution remains energy stable (§2.3). **Derived**
3. Redistribution reduces the largest eigenvalue magnitude by about the length ratio of small to full cells (§3). **Shown**
4. High-order convergence and energy stability are verified, including the acoustic "Pacman" benchmark (§3). **Shown**

# Notation map

| Taylor, Wilcox & Chan (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Pi_k$ | volume-weighted projection on $M_{\mathbf k}$ | merging neighbourhood as in the registry |
| $\hat\Omega$, $\Omega_E$ | embedding domain, embedded region $\Omega_s$ |  |

# Reference list

57 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 6 (2026-11-08). This source is cited on:

- [Small-cell problem](/definitions/small-cell-problem.md)
- [State redistribution](/methods/state-redistribution.md)
