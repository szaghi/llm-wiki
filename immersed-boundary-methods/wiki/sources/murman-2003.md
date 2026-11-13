---
type: Source
title: "Murman, Aftosmis & Berger (2003) — Implicit approaches for moving boundaries in a 3-D Cartesian method"
description: "Moving boundaries in a 3-D Cartesian cut-cell method with an implicit dual-time scheme, a rigid domain motion in arbitrary Lagrangian-Eulerian form, a relative body motion analysed in space-time, and a hierarchy of conservative approximations of the swept geometry."
resource: "doi:10.2514/6.2003-1119"
source_kind: paper
authors: [Murman S.M., Aftosmis M.J., Berger M.J.]
year: 2003
venue: "41st AIAA Aerospace Sciences Meeting and Exhibit, AIAA Paper 2003-1119"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2003_Crossref_41st_Aerospace_Sciences_Meeting_and_Exhibit_Murman_Implicit_Approaches_for_Moving_Boundaries_in_a_3-D_Cartesian.pdf"
tags: [cut-cell, moving-boundary, implicit, space-time, conservation]
timestamp: 2026-11-13T05:49:40Z
---

# Summary

Murman, Aftosmis and Berger move geometry within a fixed [cut-cell](/methods/cut-cell-method.md) Cartesian mesh. An implicit dual-time scheme decouples the time step from the smallest cut cells and limits how often the body must be re-intersected with the mesh; a rigid motion of the whole domain is handled in arbitrary Lagrangian–Eulerian form, and the relative motion of bodies through the mesh by a space-time analysis that yields the [geometric conservation law](/definitions/geometric-conservation-law.md), flux telescoping for swept cells (equivalent to [cell merging](/methods/cell-merging.md) ahead of the front) and a hierarchy of conservative approximations of the moving geometry.

# Version read

Version of record, AIAA Paper 2003-1119 (41st Aerospace Sciences Meeting, Reno, January 2003), 20 pages. §§1–4 read, §5 by test; three-dimensional results read in outline.

# Key claims

1. Re-intersecting the body with the Cartesian mesh is the most expensive and robustness-critical step, and in three dimensions it touches a surface's worth of cells; an implicit scheme lets the time step follow the physics and reduces the re-intersections (§1). **Stated**
2. A van Leer flux-vector splitting written with the Mach number relative to the moving boundary and a split energy flux is consistent and Galilean invariant (§2). **Derived**
3. An impermeable moving wall contributes only pressure, acting on the spatial projection of its swept area; the change of a cell's volume equals the swept volume (§4). **Derived**
4. Ahead of the moving front flux telescoping is mathematically equivalent to cell merging; behind it no reconstruction is needed (§4). **Stated**
5. Sequential-static, backward-Euler (geometry frozen over the step) and approximate space-time-geometry levels all conserve discretely and differ in accuracy (§4). **Stated**
6. A Mach-2 piston matches the exact shock position and piston pressure at two wall CFL numbers; a pitching NACA 0012 airfoil reproduces the measured normal-force hysteresis with both the ALE and the relative-motion formulations (§5). **Shown**

# Notation map

| Murman, Aftosmis & Berger (2003) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $Q$ | $\mathbf q$ |  |
| $\tau$ | pseudo-time | page-local |
| $w$, $u_\Omega$ | $\mathbf u_\Gamma$, rigid-domain velocity | page-local |
| $t_c$ | time a cell vertex is crossed | page-local |

# Reference list

37 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 7 (2026-11-13). This source is cited on:

- [Fresh-cell problem](/definitions/fresh-cell-problem.md)
- [Geometric conservation law](/definitions/geometric-conservation-law.md)
- [Small-cell problem](/definitions/small-cell-problem.md)
- [Cell merging for cut cells](/methods/cell-merging.md)
- [Cut-cell (embedded-boundary) finite-volume method](/methods/cut-cell-method.md)
- [Discrete conservation](/properties/discrete-conservation.md)
