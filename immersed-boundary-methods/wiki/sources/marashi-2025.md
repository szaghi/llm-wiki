---
type: Source
title: "Marashi & Hejranfar (2025) — A high-order hybrid compact-WENO finite-difference immersed boundary method for computing two-dimensional inviscid compressible flows"
description: "Ghost-point immersed boundary method in a fifth-order hybrid compact–WENO finite-difference scheme for 2D Euler flows, more accurate and cheaper than WENO-based immersed boundaries with somewhat more oscillation at shocks."
resource: "doi:10.1002/fld.5376"
source_kind: paper
authors: [Marashi M.H., Hejranfar K.]
year: 2025
venue: "Int. J. Numer. Methods Fluids 97(6):875–892"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2025_Crossref_International_Journal_for_Numerical_Methods_in_Fluids_Marashi_A_HighOrder_Hybrid_Compact_scpWENOscp.pdf"
tags: [ghost-cell, high-order, compressible, shock, weno]
timestamp: 2026-11-08T18:35:00Z
---

# Summary

Marashi and Hejranfar couple a [ghost-cell](/methods/ghost-cell-method.md) treatment (image point at minimum normal distance, bilinear interpolation, slip reflection) to a hybrid compact–WENO scheme switched by a smoothness indicator, and test it on [shock–obstacle problems](/benchmarks/shock-obstacle-interaction.md) ([high-order immersed boundary treatments](/methods/high-order-immersed-boundary.md)).

# Version read

Version of record, Int. J. Numer. Methods Fluids 97, 875–892 (2025). §§1–3 read, §4 tests in outline.

# Key claims

1. The hybrid scheme is more accurate at lower cost than WENO-based immersed boundaries and needs no filters (§4). **Shown**
2. With threshold $r_c=0.01$ it is about 2.9 times faster than WENO in one test, somewhat more oscillatory at discontinuities (§4). **Shown**

# Notation map

| Marashi & Hejranfar (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $r_c$ | smoothness-indicator threshold | page-local |

# Reference list

68 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 5 (2026-11-08). This source is cited on:

- [Shock–obstacle interaction](/benchmarks/shock-obstacle-interaction.md)
- [Ghost-cell immersed boundary method](/methods/ghost-cell-method.md)
- [High-order immersed boundary treatments for compressible flow](/methods/high-order-immersed-boundary.md)
