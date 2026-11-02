---
type: Source
title: "Angel et al. (2023) — Efficient upwind finite-difference schemes for wave equations on overset grids"
description: "Adds upwinding to existing finite-difference schemes for wave equations in second-order form as a modular corrector stage acting as a special artificial dissipation, keeping the robustness of upwind schemes on overset grids with thin boundary-fitted grids at about a tenth of the cost of the earlier upwind formulation."
resource: "doi:10.1137/22m1516178"
source_kind: paper
authors: [Angel J.B., Banks J.W., Carson A.M., Henshaw W.D.]
year: 2023
venue: "SIAM J. Sci. Comput. 45:A2703-A2724"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2023_Crossref_SIAM_Journal_on_Scientific_Computing_Angel_Efficient_Upwind_Finite-Difference_Schemes_for_Wave_Equation.pdf"
tags: [wave-equation, finite-difference, stability, maxwell, high-order]
timestamp: 2026-11-02T15:25:00Z
---

# Summary

Wave equations lack natural dissipation, and centred schemes on overset grids — especially with thin boundary-fitted grids — are generally unstable. Angel et al. add upwinding to an existing (centred, dissipation-free) discretization of a wave equation in second-order form as a separate corrector stage that takes the form of a special artificial dissipation. The predictor–corrector scheme keeps the robustness of the authors' original upwind formulation and runs typically ten or more times faster; second- and fourth-order Maxwell solutions in second-order form measure the performance ([upwind schemes for wave equations on overlapping grids](/methods/upwind-wave-equation-overset.md), [Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md)).

# Version read

SIAM typeset version of record (download stamp 11/01/26), 22 pages. Read in a targeted way (abstract, introduction, section structure, main results and conclusions closely; derivations and remaining results skimmed): from chunk 4 on, the bundle is compiled in the main session without reader subagents, by the owner's instruction. Claims below are limited to what was read closely.

# Key claims

1. Upwinding can be added to an existing discretization of a second-order wave equation as a modular corrector stage, in the form of a special artificial dissipation (Abstract, §2–§3). **Stated**
2. The upwind predictor–corrector scheme is typically ten or more times faster than the original upwind formulation (Abstract). **Shown**
3. Theory and computations show that the scheme remains robust and stable on overset grids with thin boundary-fitted grids, where nondissipative schemes are generally unstable (Abstract). **Shown** / **Derived**
4. Maxwell's equations in second-order form are solved to second and fourth order on overset grids to assess run-time performance (Abstract, numerical section). **Shown**

# Printed slips

None recorded (targeted reading).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| predictor, corrector | centred update, upwind dissipation stage | |

# Reference list

19 references, merged complete into the [bibliography](/bibliography.md) with `citedby` angel-2023, from the Crossref deposited reference list. Ogen is `henshaw-1998`; Banks & Hagstrom's Galerkin-difference paper is `banks-2016-b`, distinct from the ingested [Banks et al. (2016)](/sources/banks-2016.md).

# Pages created or updated

Chunk 4 (2026-11-02). This source is cited on:

- [High-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md)
- [Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md)
- [Upwind schemes for wave equations on overlapping grids](/methods/upwind-wave-equation-overset.md)
