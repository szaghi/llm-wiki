---
type: Source
title: "Nissen, Kormann, Grandin & Virta (2014) — Stable difference methods for block-oriented adaptive grids"
description: "SBP-SAT adaptive mesh refinement on block-oriented grids: stable treatment of junction/corner points where interfaces of different refinement meet, at a local accuracy cost."
resource: "doi:10.1007/s10915-014-9969-z"
source_kind: paper
authors: [Nissen A., Kormann K., Grandin M., Virta K.]
year: 2014
venue: "J. Sci. Comput. 65:486-511 (arXiv:1405.0735)"
local_file: "~/papers/mosaic/div-free-amr/2014-arXiv-Nissen-101007s10915-014-9969-z.pdf"
tags: [sbp, sat, amr, block-structured, corner-points, interface-conditions]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Brings the SBP-SAT machinery to **genuinely adaptive** grids: a
block-oriented AMR scheme (non-overlapping blocks, whole-block anisotropic
refinement, adjoining blocks differing by at most a factor 2 per
direction) using the
[Mattsson–Carpenter interpolation operators](/operators/sbp-preserving-interpolation.md)
at level-change interfaces — and, the paper's contribution, a **stable
treatment of junction (corner) points** where interfaces with different
boundary treatments meet, which two-block analyses never encounter. New
"SBP-FD junction operators" allow interior (central FD) stencils to run
*across* same-level block boundaries, reserving SBP-SAT closures for
actual refinement jumps — fewer interfaces, smaller error constants.
First and second derivatives both analyzed; demonstrated on the
time-dependent Schrödinger and advection equations with automatic
adaptivity.

# Key claims

1. **The corner problem is real and separate**: Mattsson–Carpenter "only
   treat interfaces between two blocks of different refinement levels";
   a fully adaptive mesh has points where two or more such interfaces
   intersect, and treating them stably "without reduc[ing] the overall
   accuracy … is a challenging task."
2. **Stability at a local accuracy price**: as in Kramer et al.'s
   continuous formulation, stability at junctions costs local accuracy
   relative to the interior stencil — but numerically "the locally reduced
   accuracy does not severely reduce the accuracy of the time propagated
   numerical solution."
3. **Interface economy**: since SBP-SAT closures are lower order than
   interior stencils, the design maximizes use of interior stencils across
   block boundaries (equal refinement → no numerical interface at all),
   minimizing where the accuracy tax is paid.
4. **Block-oriented SAMR positioning**: whole-block refinement of
   non-overlapping blocks reduces grid-management overhead and
   parallelization complexity relative to Berger–Colella patch hierarchies
   — the SBP community's preferred AMR topology.

# Notation map

| Nissen et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| SBP-SAT interfaces + interpolation | $I_{C2F}, I_{F2C}$ in SATs | Mattsson–Carpenter operators reused |
| SBP-FD junction operators | — | mixed closure type; named inline |
| factor-2 per-direction refinement | 2:1 interface, anisotropic | block granularity |

# Pages created or updated

* Updated [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md) (corner/junction treatment resolved).
* Updated [Block-structured AMR](/definitions/block-structured-amr.md) (block-oriented SAMR variant).

# Citations

1. `~/papers/mosaic/div-free-amr/2014-arXiv-Nissen-101007s10915-014-9969-z.pdf` (doi:10.1007/s10915-014-9969-z) — text extraction, 27 pp.
