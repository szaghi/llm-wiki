---
type: Source
title: "Bennett, Nikiforakis & Klein (2018) — A moving boundary flux stabilization method for Cartesian cut-cell grids using directional operator splitting"
description: "Extension of the Klein-Bates-Nikiforakis flux stabilization for cut cells, in which stable cut-cell fluxes are linear combinations of standard fluxes along a one-dimensional stencil in a dimensionally split scheme, to rigid bodies moving through the grid in compressible flow."
resource: "doi:10.1016/j.jcp.2018.04.048"
source_kind: paper
authors: [Bennett W.P., Nikiforakis N., Klein R.]
year: 2018
venue: "J. Comput. Phys. 368:333–358"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2018_Crossref_Journal_of_Computational_Physics_Bennett_A_moving_boundary_flux_stabilization_method_for_Cartesian_cu.pdf"
tags: [cut-cell, small-cell, moving-boundary, dimensional-splitting, compressible]
timestamp: 2026-11-13T05:49:40Z
---

# Summary

Bennett, Nikiforakis and Klein move rigid bodies through a dimensionally split [cut-cell](/methods/cut-cell-method.md) scheme for the Euler equations. The flux of a cut cell is a linear combination of standard fluxes along a one-dimensional extended stencil, with weights from the cut-cell geometry, which removes the [small-cell](/definitions/small-cell-problem.md) time-step limit for any flux approximation; for moving walls the weights use time-dependent volume and face fractions and the boundary is averaged over the step. Uncovered cells are filled by volume-weighted averaging ([fresh-cell problem](/definitions/fresh-cell-problem.md)); [conservation](/properties/discrete-conservation.md) is approximate.

# Version read

arXiv:1711.11361v2 (24 April 2018), the accepted manuscript; metadata from the version of record, J. Comput. Phys. 368, 333–358 (2018). §1 read, §2 in outline, §3 by test, §4.

# Key claims

1. The stable time step for arbitrarily small cut cells is of the order of that of regular cells, and the scheme is compatible with a wide range of numerical fluxes (abstract, §1). **Stated**
2. With dimensional splitting the swept volumes of the separate directional moves do not add up to the two-dimensional swept volume, which loses conservation and under-predicts the boundary work; time-averaged boundary properties and a conservation check for newly covered cells counter it (§2). **Stated**
3. A body moving with the surrounding fluid must reproduce the exact solution (consistency condition) (§1, §4). **Stated**
4. The cut cells are locally first order; the global error approaches second order under refinement while the maximum-norm error stays limited by the boundary region (§3). **Shown**
5. Six tests — oblique-channel advection, circular and triangular cylinders through a shock, a piston in a shock tube, an oscillating NACA 0012 airfoil and a Schardin wedge — agree with references; the wedge's mass error depends on resolution and on where its corners fall (§3). **Shown**

# Notation map

| Bennett, Nikiforakis & Klein (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\alpha$ (cut-cell volume fraction) | $\kappa_{\mathbf i}$ |  |
| $\beta$ (face fraction) | $a_{\mathbf i+\frac12\mathbf e_m}$ |  |
| $\phi$ | $\phi$ | level set |
| $u_s$ | $\mathbf u_\Gamma$ | rigid-body velocity |

# Reference list

75 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 7 (2026-11-13). This source is cited on:

- [Fresh-cell problem](/definitions/fresh-cell-problem.md)
- [Small-cell problem](/definitions/small-cell-problem.md)
- [Cut-cell (embedded-boundary) finite-volume method](/methods/cut-cell-method.md)
- [Discrete conservation](/properties/discrete-conservation.md)
