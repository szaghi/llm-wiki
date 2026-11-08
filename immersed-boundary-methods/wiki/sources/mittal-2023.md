---
type: Source
title: "Mittal & Seo (2023) — Origin and evolution of immersed boundary methods in computational fluid dynamics"
description: "Invited history and perspective of immersed boundary methods from the marker-and-cell era to the 2020s, with a five-condition definition of sharp-interface methods by equivalence with body-conformal methods."
resource: "doi:10.1103/physrevfluids.8.100501"
source_kind: paper
authors: [Mittal R., Seo J.H.]
year: 2023
venue: "Phys. Rev. Fluids 8:100501"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2023_Crossref_Physical_Review_Fluids_Mittal_Origin_and_evolution_of_immersed_boundary_methods_in_computa.pdf"
tags: [review, history, sharp-interface, classification]
timestamp: 2026-11-08T18:35:00Z
---

# Summary

Mittal and Seo trace the [immersed boundary method](/definitions/immersed-boundary-method.md) from Harlow and Welch's marker-and-cell method and Viecelli's curved boundaries through Peskin's [classical method](/methods/classical-immersed-boundary-method.md), the decades in which body-conformal, ALE and overset grids dominated aerospace computing, and the resurgence of the 1990s and 2000s. Their main conceptual contribution is a five-condition definition of a [sharp-interface method](/definitions/sharp-and-diffuse-interface.md) and a classification of continuous forcing, cut-cell, ghost-cell and stair-step methods against it.

# Version read

Version of record (invited article), Phys. Rev. Fluids 8, 100501 (2023). History, classification and sharp-interface sections read in full; later perspectives (moving bodies, wall models, compressible flow, GPUs, outlook) skimmed. The text carries no section numbers; claims cite part names.

# Key claims

1. Peskin's regularized delta function is the method's "Achilles heel": the interface is diffuse and boundary-condition satisfaction depends on resolution (history). **Stated**
2. Cut-cell methods are the only immersed boundary methods that conserve mass and momentum strictly (discrete forcing part). **Stated**
3. A method is sharp iff (1) boundary conditions sit at discrete points on the boundary only, (2) spaced like the grid, (3) with consistent accuracy, (4) every grid point solves the native equations, (5) the equations are not solved inside the body (classification). **Stated**
4. Continuous forcing, fictitious-domain and front-tracking methods meet none of the conditions; cut-cell and ghost-cell methods are sharp; stair-stepping fails condition (1) (classification). **Stated**
5. Without a pressure condition on the boundary, a fractional step leaves slip and penetration errors of order $\Delta t^m\,\partial p/\partial\boldsymbol\tau$ and $\Delta t^m\,\partial p/\partial n$ (classification). **Derived**

# Notation map

| Mittal & Seo (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $m$ | order of the fractional-step splitting | page-local |
| $\partial p/\partial\tau$ | tangential pressure derivative |  |

# Reference list

140 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 5 (2026-11-08). This source is cited on:

- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md)
