---
type: Source
title: "Jones, McNally & Reynolds (2026) — A constrained-transport embedded boundary method for compressible resistive magnetohydrodynamics"
description: "Embedded boundaries for compressible resistive MHD on Cartesian grids: Forrer–Jeltsch cut cells without a small-cell time-step limit, face-centred staggered constrained transport kept divergence free at the boundary, and a ghost fluid coupling for moving two-material interfaces."
resource: "doi:10.1016/j.jcp.2025.114641"
source_kind: paper
authors: [Jones S.W., McNally C.P., Reynolds M.]
year: 2026
venue: "J. Comput. Phys. 550:114641"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2026_Crossref_Journal_of_Computational_Physics_Jones_A_constrained-transport_embedded_boundary_method_for_compres.pdf"
tags: [cut-cell, mhd, constrained-transport, ghost-fluid, plasma]
timestamp: 2026-11-08T18:44:00Z
---

# Summary

Jones, McNally and Reynolds, motivated by magneto-inertial fusion devices, combine a [cut-cell](/methods/cut-cell-method.md) scheme that computes fluxes on full Cartesian faces (no [small-cell](/definitions/small-cell-problem.md) limit, local conservation errors) with staggered constrained transport for the induction equation, and couple two materials across a moving interface by a [ghost fluid method](/methods/ghost-fluid-method.md) with a single global magnetic field.

# Version read

arXiv:2601.04099v1 (7 January 2026; accepted manuscript carrying the JCP DOI); metadata from the version of record, J. Comput. Phys. 550, 114641 (2026). §§1–5 read, §7 results by test.

# Key claims

1. Computing fluxes on full Cartesian faces and edges avoids the small-time-step problem of cut cells, at the cost of local conservation errors (§1, §3). **Stated**
2. At embedded boundaries magnetic flux is not conserved but no monopoles are introduced (§1, §4). **Stated**
3. Separate magnetic fields on the two sides of a material interface would create monopoles; one global field with per-material edge electric fields averaged by occupation is used (§4). **Stated**
4. Second-order convergence without discontinuities, first order with a material discontinuity (abstract, §7). **Shown**

# Notation map

| Jones, McNally & Reynolds (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi$ | level set $\phi$ |  |
| $\eta$ | resistivity (magnetic diffusivity) | page-local: clashes with the registry penalization parameter $\eta$ |
| $\mathbf B$, $\mathbf E$, $\mathbf J$ | magnetic field, electric field, current density | page-local |

# Reference list

47 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 6 (2026-11-08). This source is cited on:

- [Small-cell problem](/definitions/small-cell-problem.md)
- [Cut-cell (embedded-boundary) finite-volume method](/methods/cut-cell-method.md)
- [Ghost fluid method](/methods/ghost-fluid-method.md)
- [Discrete conservation](/properties/discrete-conservation.md)
