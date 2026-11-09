---
type: Source
title: "Dobrev, Knupp, Kolev, Mittal, Rieben & Tomov (2020) — Simulation-driven optimization of high-order meshes in ALE hydrodynamics"
description: "High-order target-matrix optimization driven by discrete simulation fields for multi-material ALE shock hydrodynamics: adaptive targets, normalized multi-metric objectives, space-dependent limiting of node motion and TMOP-based ALE triggers."
resource: "doi:10.1016/j.compfluid.2020.104602"
source_kind: paper
authors: [Dobrev V., Knupp P., Kolev T., Mittal K., Rieben R., Tomov V.]
year: 2020
venue: "Comput. Fluids 208:104602"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2020_Crossref_Computers_amp_Fluids_Dobrev_Simulation-driven_optimization_of_high-order_meshes_in_ALE_h.pdf"
tags: [mesh-optimization, target-matrix, ale, r-adaptivity]
timestamp: 2026-11-08T20:47:00Z
---

# Summary

Dobrev et al. use [target-matrix optimization](/methods/target-matrix-optimization.md) as the remesh step of high-order ALE hydrodynamics, with targets adapted to discrete simulation fields, limited node motion and adaptive remesh triggers.

# Version read

arXiv:2001.11536v1 (30 January 2020, preprint submitted to Computers & Fluids); metadata from the version of record, Comput. Fluids 208, 104602 (2020). §§1–4 and the conclusions read; §5 simulations in outline.

# Key claims

1. Normalizing each metric integral by its initial value makes multi-metric objectives independent of units, refinement and domain size (§3.1). **Stated**
2. A space-dependent limiting term keeps nodes near Lagrangian positions to preserve features and reduce remap error (§3.2). **Stated**
3. TMOP metrics define adaptive ALE triggers that balance time-step size and remap frequency (§4.2). **Stated**

# Notation map

| Dobrev, Knupp, Kolev, Mittal, Rieben & Tomov (2020) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x_0$ | Lagrangian node positions | page-local |
| $\omega$ | metric weight | page-local |

# Reference list

39 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 3 (2026-11-08). This source is cited on:

- [Target-matrix optimization (TMOP)](/methods/target-matrix-optimization.md)
