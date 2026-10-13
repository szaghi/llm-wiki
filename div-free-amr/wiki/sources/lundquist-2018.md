---
type: Source
title: "Lundquist, Malan & Nordström (2018) — A hybrid framework for coupling arbitrary summation-by-parts schemes on general meshes"
description: "Generalizes SBP-preserving interface coupling beyond tensor-product grids: stable non-collocated interfaces between arbitrary SBP schemes, including high-order FD to unstructured FV."
resource: "doi:10.1016/j.jcp.2018.02.018"
source_kind: paper
authors: [Lundquist T., Malan A., Nordström J.]
year: 2018
venue: "J. Comput. Phys. 362:49-68"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2018-JCP-Lundquist-101016jjcp201801047.pdf"
tags: [sbp, sat, interpolation, hybrid, unstructured, coarse-fine-interface]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Extends [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md)
to a **hybrid framework for arbitrary SBP schemes on general meshes**: the
formulation relies on neither tensor products nor curvilinear coordinate
transformations, so structured high-order FD blocks and unstructured
(node-centered, edge-based) FV blocks — the latter cast in SBP form —
couple through the same stable interface machinery, with interpolation
handling non-collocated node distributions and differing resolutions.
Demonstrated FD–FD (arbitrary order, curvilinear) and FD–FV couplings;
initial CFD experiments show "considerable efficiency gains … of up to an
order of magnitude" over non-hybrid computation.

# Key claims

1. **The interface theory outgrows its grid assumptions**: previous
   SBP-preserving couplings presumed tensor-product structure; here the
   conditions are posed on arbitrary node sets — the SBP interface
   framework becomes mesh-topology-agnostic.
2. **FD–FV hybridization under one energy estimate**: unstructured FV in
   SBP form couples stably to high-order FD, harvesting FD efficiency
   where geometry is simple and FV flexibility where it is not — the
   generalized-SBP umbrella
   ([Del Rey Fernández et al. (2014)](/sources/delreyfernandez-2014.md))
   put to work at interfaces.
3. **Minimal invasiveness as a design constraint**: existing schemes are
   coupled with "minimal algorithmic modifications" — interface machinery
   as an add-on layer, not a scheme rewrite.

# Notation map

| Lundquist et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| SBP-preserving interpolation on general node sets | $I_{C2F}, I_{F2C}$ generalized | non-collocated, non-tensor-product |
| FV in SBP form | generalized SBP member | node-centered edge-based |

# Pages created or updated

* Updated [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md) (general-mesh hybrid extension).

# Citations

1. `~/papers/mosaic/div-free-amr/2018-JCP-Lundquist-101016jjcp201801047.pdf` (doi:10.1016/j.jcp.2018.02.018) — text extraction, pp. 49–68.
