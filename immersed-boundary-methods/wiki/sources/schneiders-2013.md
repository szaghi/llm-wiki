---
type: Source
title: "Schneiders, Hartmann, Meinke & Schröder (2013) — An accurate moving boundary formulation in cut-cell methods"
description: "Three-dimensional compressible viscous cut-cell method in which the small-cell treatment (interpolation plus redistribution) and the least-squares stencil weights vary smoothly as the boundary moves, removing the spurious force oscillations that abrupt operator changes, including cell merging, produce."
resource: "doi:10.1016/j.jcp.2012.09.038"
source_kind: paper
authors: [Schneiders L., Hartmann D., Meinke M., Schröder W.]
year: 2013
venue: "J. Comput. Phys. 235:786–809"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2013_Crossref_Journal_of_Computational_Physics_Schneiders_An_accurate_moving_boundary_formulation_in_cut-cell_methods.pdf"
tags: [cut-cell, moving-boundary, spurious-oscillations, redistribution, compressible]
timestamp: 2026-11-13T05:49:40Z
---

# Summary

Schneiders, Hartmann, Meinke and Schröder show that the [spurious force oscillations](/definitions/spurious-force-oscillations.md) of moving-boundary [cut-cell](/methods/cut-cell-method.md) methods come from abrupt changes of the discrete operator when cells emerge, submerge, become cut or become small, also with conservative [cell merging](/methods/cell-merging.md). Small cells take a blend of their regular update and an interpolated value, with the defect [redistributed](/methods/redistribution.md) to neighbours; the blending weight and the least-squares weights of emerging cells are continuously differentiable, so the operator changes smoothly.

# Version read

Version of record, J. Comput. Phys. 235, 786–809 (2013; online 2012). §§1–4 read, §5 by test, §6.

# Key claims

1. Abrupt changes of the discrete operator when the boundary moves act like an unphysical source term and produce spurious force oscillations, also with the conservative cell-merging technique (§1, §4.3). **Stated**
2. A small cell takes a blend of its regular Runge–Kutta update and a stable value from a first-order Taylor expansion about the boundary centroid; the defect goes to direct neighbours with weights summing to one, so the scheme is conservative (§4.1). **Derived**
3. The blending weight is a continuously differentiable function of the cell volume instead of a switch at volume fraction 0.5, and emerging or submerging cells enter least-squares stencils through a weight that ramps over about ten time steps (§4.2). **Derived**
4. A displacement with expected drag change of order $10^{-7}$ that makes one cell small produces a visible drag jump with merging or a switch and none with the smooth weights (§4.3). **Shown**
5. For viscous cylinder flows the drag fluctuations are lowered by up to two orders of magnitude compared with cell merging; oscillating airfoils and an oscillating sphere agree with reference data (§5, §6). **Shown**

# Notation map

| Schneiders, Hartmann, Meinke & Schröder (2013) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\kappa$ | small-cell blending weight | page-local: clashes with the registry volume fraction $\kappa_{\mathbf i}$ |
| $w$ | least-squares weight of a cell | page-local |
| $\sigma_{a,b}$ | $w_{\mathbf i\mathbf j}$ | redistribution weights |
| $Q_I$ | interpolated stable update | page-local |
| $V/h^d$ | $\kappa_{\mathbf i}$ |  |

# Reference list

81 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 7 (2026-11-13). This source is cited on:

- [Fresh-cell problem](/definitions/fresh-cell-problem.md)
- [Small-cell problem](/definitions/small-cell-problem.md)
- [Spurious force and pressure oscillations](/definitions/spurious-force-oscillations.md)
- [Cell merging for cut cells](/methods/cell-merging.md)
- [Cut-cell (embedded-boundary) finite-volume method](/methods/cut-cell-method.md)
- [Flux redistribution for cut cells](/methods/redistribution.md)
