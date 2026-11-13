---
type: Source
title: "Bayyuk, Powell & van Leer (1993) — A simulation technique for 2-D unsteady inviscid flows around arbitrarily moving and deforming bodies of arbitrary geometry"
description: "Euler flows around bodies that move and deform across a stationary adaptive quadtree Cartesian grid, with cut cells merged into combined cells that keep their intersection topology over each motion step, removing the small-cell time-step limit and the vanishing- and newborn-cell problems."
resource: "doi:10.2514/6.1993-3391"
source_kind: paper
authors: [Bayyuk S.A., Powell K.G., van Leer B.]
year: 1993
venue: "11th AIAA Computational Fluid Dynamics Conference, AIAA Paper 93-3391"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/1993_Crossref_11th_Computational_Fluid_Dynamics_Conference_BAYYUK_A_simulation_technique_for_2-D_unsteady_inviscid_flows_aroun.pdf"
tags: [cut-cell, cell-merging, moving-boundary, quadtree, compressible]
timestamp: 2026-11-13T05:49:40Z
---

# Summary

Bayyuk, Powell and van Leer extend their quadtree [cut-cell](/methods/cut-cell-method.md) Euler solver (Roe fluxes, least-squares linear reconstruction, predictor–corrector time stepping, second order) to bodies that move and deform across the stationary grid. They state the [small-cell problem](/definitions/small-cell-problem.md) for moving boundaries together with the vanishing (swept-over) and newborn (uncovered) cells ([fresh-cell problem](/definitions/fresh-cell-problem.md)), and solve all three by [cell merging](/methods/cell-merging.md) under criteria that make every combined cell large and topologically invariant over a motion step.

# Version read

Version of record, AIAA Paper 93-3391 (11th AIAA CFD Conference, Orlando, July 1993), 12 pages. Text layer read in full; it is a degraded scan whose words are split or merged, the equations are not legible as text and the figures show only captions. No equation is reproduced here.

# Key claims

1. Cells near a moving or stationary body can always be merged into combined cells that keep their intersection topology over a motion step, under restrictions on the body's curvature and minimum width relative to the cut cells (abstract, merging section). **Stated**
2. The ratio of the smallest cut cell to the smallest uncut cell can be arbitrarily close to zero; small cut cells set the global time step and are numerically decoupled, because their residual is a small difference of large fluxes (small-cell section). **Stated**
3. Merging criteria: initial and final combined areas no smaller than the smallest uncut cell (or a fraction); no corner vertex of a combined cell crossed by the surface during the step; at most a bounded number of cells per group (merging section). **Derived**
4. With the second criterion, length-averaged fluxes of cells of varying area keep second-order time accuracy (merging section). **Stated**
5. The motion step must be below the smallest uncut cell length, so the permissible motion step decreases with the smallest radius of curvature of the body (merging section). **Stated**
6. An ellipse contracting through a gap between two fixed ellipses and a radially pulsating cylinder are computed; about 30 words of storage per cell (results, computational requirements). **Shown**

# Notation map

| Bayyuk, Powell & van Leer (1993) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| area of a cut cell | $V_{\mathbf i}=\kappa_{\mathbf i}h^d$ | 2-D areas |
| vanishing / newborn cells | cells covered / uncovered by $\Omega_s$ | see the fresh-cell page |
| merged group state | volume-weighted average | page-local |

# Reference list

10 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 7 (2026-11-13). This source is cited on:

- [Fresh-cell problem](/definitions/fresh-cell-problem.md)
- [Small-cell problem](/definitions/small-cell-problem.md)
- [Cell merging for cut cells](/methods/cell-merging.md)
- [Cut-cell (embedded-boundary) finite-volume method](/methods/cut-cell-method.md)
