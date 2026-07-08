---
type: Source
title: "Teixeira (2013) — Differential forms in lattice field theories: an overview"
description: "Review of lattice EM via forms: ordinary vs twisted forms on primal/dual lattices, discrete Hodge construction routes, and a taxonomy of premetric inconsistencies on irregular lattices."
resource: "doi:10.1155/2013/487270"
source_kind: paper
authors: [Teixeira F.L.]
year: 2013
venue: "ISRN Mathematical Physics 2013:487270"
local_file: "~/papers/mosaic/div-free-amr/2013-ISRN-MP-Teixeira-101155_2013_487270.pdf"
tags: [differential-forms, electromagnetics, dual-grid, hodge, orientation, review]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Review of lattice field theory through differential forms: Maxwell's $F$
is an **ordinary** (internally oriented) 2-form while $G = \star F$ and the
current are **twisted** (externally oriented) forms — so the two live on
*different lattices*, primal $K$ and dual $\tilde K$, with the Hodge star
as the crossing ([orientation](/definitions/orientation.md)). Covers the
3+1 decomposition recovering $E, B$ (primal) and $D, H$ (dual), the main
routes to a discrete Hodge (Whitney/Galerkin mass matrices vs sparse
direct construction on the **barycentric dual**, where the underlying
barycentric decomposition lattice is simplicial and admits Whitney forms),
and a systematic taxonomy of **premetric inconsistencies** that afflict
naive discrete calculus on irregular lattices.

# Key claims

1. **Orientation dictates the lattice**: ordinary and twisted forms cannot
   share one lattice without breaking structure — the field-theory
   statement of the primal/dual necessity, converging with the CDO and
   Delft analyses from independent communities.
2. **Hodge routes compared**: Galerkin/Whitney (symmetric, generally
   non-diagonal) vs barycentric-dual direct construction (sparse) — the
   same design space as FIT's material matrices and DEC's volume-ratio
   star, surveyed with their trade-offs.
3. **Premetric inconsistencies classified**: failures on irregular
   lattices split into kinds by whether they afflict the primal or dual
   lattice separately or their pairing — a checklist of the ways discrete
   calculus silently breaks.

# Notation map

| Teixeira | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| ordinary / twisted forms | inner-/outer-oriented cochains | third vocabulary for one distinction |
| $K$, $\tilde K$, $\hat K$ | primal, dual, barycentric-decomposition lattices | |
| $\star_\epsilon, \star_{\mu^{-1}}$ | discrete Hodge/material operators | |

# Pages created or updated

* Created [Orientation (inner/outer)](/definitions/orientation.md).

# Citations

1. `~/papers/mosaic/div-free-amr/2013-ISRN-MP-Teixeira-101155_2013_487270.pdf` (doi:10.1155/2013/487270) — text extraction, 16 pp.
