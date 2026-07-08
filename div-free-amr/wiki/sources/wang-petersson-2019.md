---
type: Source
title: "Wang & Petersson (2019) — Fourth order finite difference methods for the wave equation with mesh refinement interfaces"
description: "Fourth-order SBP discretizations at hanging-node refinement interfaces: ghost-point (strong) vs SAT (weak) imposition compared, with energy stability and no time-step penalty for the ghost-point method."
resource: "doi:10.1137/18M1211465"
source_kind: paper
authors: [Wang S., Petersson N.A.]
year: 2019
venue: "SIAM J. Sci. Comput. 41(5) (arXiv:1809.04310)"
local_file: "~/papers/mosaic/div-free-amr/2019-SISC-WangPetersson-10113718M1211465.pdf"
tags: [sbp, ghost-points, coarse-fine-interface, wave-equation, second-derivative, stability]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Fourth-order SBP treatment of the 2D acoustic wave equation (second-order
form, variable and even discontinuous coefficients) at **hanging-node mesh
refinement interfaces** — mesh size per subdomain chosen inversely to wave
speed, so 2:1-type interfaces arise from physics, not just adaptivity. Two
interface impositions are developed and *connected*: **SBP-GP** (strong,
via ghost points) and [SBP-SAT](/methods/sbp-sat.md) (weak, penalties).
A previously unexplored relation between ghost-point and ghost-free SBP
operators yields an improved fourth-order SBP-GP needing ghost points from
only one side of the interface. Energy stability is proved; numerical
experiments show clean fourth-order convergence.

# Key claims

1. **Strong vs weak imposition finally compared**: SBP-GP and SBP-SAT had
   coexisted without a bridge; the paper relates the two operator families
   and quantifies the trade — the improved GP variant solves a *smaller*
   ghost-value system and "the explicit time step does not need to be
   reduced relative to the corresponding periodic problem," whereas the
   SAT route pays a time-step (stiffness) penalty at interfaces; a
   detailed accuracy/time-step comparison against SAT is given.
2. **One-sided ghost points**: the new GP formulation uses ghost data from
   one side only — cheaper updates and a simpler path to 3D.
3. **Fourth order at hanging nodes with discontinuous media** — the
   combination (high order + nonconforming interface + coefficient jumps)
   that each earlier work handled only partially.
4. **Projection-based imposition acknowledged** as a third route, not
   pursued here.

# Notation map

| Wang & Petersson | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| SBP-GP operators | $\mathsf{D}_2$-type with ghost DOFs | strong imposition |
| SAT penalties | as on [SBP-SAT](/methods/sbp-sat.md) | weak imposition |
| hanging nodes | 2:1-type coarse-fine interface | trace nonconformity |

# Pages created or updated

* Updated [SBP-SAT technique](/methods/sbp-sat.md) (strong-imposition alternative and the time-step trade).

# Citations

1. `~/papers/mosaic/div-free-amr/2019-SISC-WangPetersson-10113718M1211465.pdf` (doi:10.1137/18M1211465) — text extraction, 32 pp.
