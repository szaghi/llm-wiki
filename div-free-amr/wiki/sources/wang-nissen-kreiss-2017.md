---
type: Source
title: "Wang, Nissen & Kreiss (2017) — Convergence of finite difference methods for the wave equation in two space dimensions"
description: "Extends normal-mode accuracy analysis to 2D by diagonalization, separately treating truncation errors along entire boundaries and errors localized at corners."
resource: "arXiv:1702.01383 (published Math. Comp. 87:2737-2763, 2018, doi:10.1090/mcom/3319)"
source_kind: paper
authors: [Wang S., Nissen A., Kreiss G.]
year: 2017
venue: "arXiv:1702.01383v2; Math. Comp. 87:2737-2763 (2018)"
local_file: "~/papers/mosaic/div-free-amr/2017-arXiv-Wang-1048550arXiv170201383.pdf"
tags: [sbp, convergence, normal-mode-analysis, accuracy, corner-points, wave-equation]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The 2D companion to [Wang & Kreiss (2017)](/sources/wang-kreiss-2017.md):
normal-mode accuracy analysis had been strictly one-dimensional; here a
**diagonalization procedure** decomposes the 2D semi-discretization into
families of 1D problems of the same type, with a general framework for
assembling the 2D convergence rate from the 1D results. Two structurally
different error geometries are analyzed: truncation error along an
**entire boundary line**, and truncation error **localized at a few grid
points near a corner** — the latter being exactly the geometry of the
junction points in adaptive block grids
([Nissen et al. (2014)](/sources/nissen-2014.md)). Applied to the
SBP-SAT wave equation; corroborated numerically; the technique is stated
to be not limited to SBP methods.

# Key claims

1. **Dimensionality is not a formality**: 1D gain results do not transfer
   verbatim — the 2D rate depends on whether the large truncation error
   is line-distributed or corner-localized, which have different gains.
2. **Corner errors analyzed rigorously for the first time** in this
   framework — providing the accuracy theory for the corner/junction
   treatments whose stability was settled separately.

# Notation map

| Wang, Nissen & Kreiss | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| diagonalized 1D families | normal-mode reduction | per transverse mode |
| corner-localized truncation error | junction-point error geometry | cf. block-AMR corners |

# Pages created or updated

* Updated [Summation by parts (SBP)](/definitions/summation-by-parts.md) (2D/corner extension of the convergence theory).

# Citations

1. `~/papers/mosaic/div-free-amr/2017-arXiv-Wang-1048550arXiv170201383.pdf` (arXiv:1702.01383) — text extraction, 30 pp. **Venue corrected 2026-10-08 (DOI audit).** The published venue was recorded earlier as SIAM J. Numer. Anal. 56(5):3016-3048, which page 1 does not support; Crossref places the paper in Math. Comp. 87:2737-2763 (2018), doi:10.1090/mcom/3319.
