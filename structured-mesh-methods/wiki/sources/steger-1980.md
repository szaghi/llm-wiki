---
type: Source
title: "Steger & Chaussee (1980) — Generation of body-fitted coordinates using hyperbolic partial differential equations"
description: "Hyperbolic grid generation: orthogonality plus a prescribed arc-length increment or cell area marched outward from a body by a noniterative implicit scheme, giving fast, smooth exterior grids with spacing control near the body."
resource: "doi:10.1137/0901031"
source_kind: paper
authors: [Steger J.L., Chaussee D.S.]
year: 1980
venue: "SIAM J. Sci. Stat. Comput. 1(4):431–437"
local_file: "/home/stefano/papers/mosaic/structured-mesh/1980_Crossref_SIAM_Journal_on_Scientific_and_Statistical_Computing_Steger_Generation_of_Body-Fitted_Coordinates_Using_Hyperbolic_Parti.pdf"
tags: [hyperbolic-generation, orthogonality, grid-generation]
timestamp: 2026-11-08T20:27:00Z
---

# Summary

Steger and Chaussee show that the constructive orthogonal-grid procedure of McNally and Graves is an initial-value problem for a hyperbolic system, and add a cell-volume variant that keeps the Jacobian positive ([hyperbolic grid generation](/methods/hyperbolic-grid-generation.md)).

# Version read

Version of record, SIAM J. Sci. Stat. Comput. 1, 431–437 (1980). Read in full.

# Key claims

1. Orthogonality with a prescribed increment makes the grid equations hyperbolic and well posed for data on the body (analysis section). **Derived**
2. Prescribing cell area keeps the Jacobian positive and avoids singular grids except in severe concavity (cell volume scheme). **Derived**
3. The marching generator costs about one sweep of an elliptic line-relaxation generator (applications). **Stated**

# Notation map

| Steger & Chaussee (1980) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $V$ | $V$ | prescribed cell area |
| $\Delta s$ | $\Delta s$ |  |

# Reference list

9 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 1 (2026-11-08). This source is cited on:

- [Hyperbolic grid generation](/methods/hyperbolic-grid-generation.md)
