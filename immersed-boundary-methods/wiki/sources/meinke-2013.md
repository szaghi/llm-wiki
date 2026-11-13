---
type: Source
title: "Meinke, Schneiders, Günther & Schröder (2013) — A cut-cell method for sharp moving boundaries in Cartesian grids"
description: "Compressible viscous cut-cell method on octree Cartesian grids for sharp moving boundaries from level sets, with a smooth discrete formulation for emerging and vanishing cells against spurious oscillations, several level sets for independently moving parts, and multiply cut and split cells."
resource: "doi:10.1016/j.compfluid.2012.11.010"
source_kind: paper
authors: [Meinke M., Schneiders L., Günther C., Schröder W.]
year: 2013
venue: "Comput. Fluids 85:135–142"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2013_Crossref_Computers_amp_Fluids_Meinke_A_cut-cell_method_for_sharp_moving_boundaries_in_Cartesian_g.pdf"
tags: [cut-cell, moving-boundary, level-set, spurious-oscillations, compressible]
timestamp: 2026-11-13T05:49:40Z
---

# Summary

Meinke, Schneiders, Günther and Schröder present a [cut-cell](/methods/cut-cell-method.md) finite-volume method for compressible viscous flow with moving boundaries given by level sets. Abrupt changes of the discretization near the moving boundary — cells emerging, vanishing or becoming small — cause [spurious oscillations](/definitions/spurious-force-oscillations.md), which they avoid with smoothly varying least-squares weights and small-cell transitions; small cells are stabilized by interpolation plus flux [redistribution](/methods/redistribution.md). Separate level sets for parts moving at different speeds resolve the closing of an engine valve without remeshing.

# Version read

Version of record, Comput. Fluids 85, 135–142 (2013; online 2012). Read in full.

# Key claims

1. Abrupt changes of the discrete approximation near a moving boundary generate unphysical oscillations (abstract, §3.1). **Stated**
2. Increasing the weight of an emerging cell gradually in the least-squares reconstruction, and smoothing the transition between regular cut cells and small cells, avoids them (§3.1). **Stated**
3. Different level sets for parts moving at different speeds keep each boundary accurate when the gap between them is of the order of a cell (§3.2). **Stated**
4. A modified marching-cubes algorithm handles cells cut several times and cells split into unconnected parts (§3.2). **Stated**
5. For a transversely oscillating cylinder at $Re=185$ the force coefficients agree with reference data and the forces are smooth; a simplified internal-combustion engine with a moving valve is computed (§4). **Shown**

# Notation map

| Meinke, Schneiders, Günther & Schröder (2013) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi$ | $\phi$ |  |
| $\Omega_f$, $\Omega_s$, $\Gamma$ | $\Omega_f$, $\Omega_s$, $\Gamma$ |  |
| $Q$ | $\mathbf q$ |  |
| $L_D$ | discrete flux operator | page-local |

# Reference list

31 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 7 (2026-11-13). This source is cited on:

- [Fresh-cell problem](/definitions/fresh-cell-problem.md)
- [Spurious force and pressure oscillations](/definitions/spurious-force-oscillations.md)
- [Cut-cell (embedded-boundary) finite-volume method](/methods/cut-cell-method.md)
