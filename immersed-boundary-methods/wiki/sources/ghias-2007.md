---
type: Source
title: "Ghias, Mittal & Dong (2007) — A sharp interface immersed boundary method for compressible viscous flows"
description: "Ghost-cell sharp-interface immersed boundary method for viscous subsonic compressible flow on Cartesian or body-non-conformal curvilinear grids, with image-point bilinear interpolation in computational space that stays well posed for all boundary positions; second order locally and globally, validated on cylinders, an airfoil and a wing tip."
resource: "doi:10.1016/j.jcp.2006.12.007"
source_kind: paper
authors: [Ghias R., Mittal R., Dong H.]
year: 2007
venue: "J. Comput. Phys. 225(1):528-553"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2007_Crossref_Journal_of_Computational_Physics_Ghias_A_sharp_interface_immersed_boundary_method_for_compressible.pdf"
tags: [ghost-cell, sharp-interface, compressible, curvilinear-grid, viscous]
timestamp: 2026-11-08T18:08:00Z
---

# Summary

Ghias, Mittal and Dong build what they present as the first immersed
boundary method for viscous compressible flow: a
[ghost-cell method](/methods/ghost-cell-method.md) on Cartesian or
body-non-conformal curvilinear grids, which keep boundary-layer resolution
with a simple grid topology. Ghost values follow from bilinear interpolation
at an image point in computational space, with boundary-condition rows
replacing missing nodes so the interpolation stays well posed. The solver is
second order in space (locally and globally) and time; it is validated on
[flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
up to $Re=3900$ and at $M=0.4$, an Eppler 211 airfoil and a wing-tip flow.
The paper states the trade-off between local accuracy and conservation for
sharp-interface methods ([discrete conservation](/properties/discrete-conservation.md)).

# Version read

Version of record, J. Comput. Phys. 225, 528–553 (2007), 26 pages. §§1–2
read in full, §3 for set-up and key comparisons. Page-1 title and authors
match Crossref.

# Key claims

1. No sharp-interface immersed boundary implementation for compressible viscous flow existed to the authors' knowledge (§1). **Stated**
2. Continuous forcing gives a diffuse boundary; discrete forcing can be sharp but depends on the discretization (§1). **Stated**
3. Non-conformal curvilinear grids combine boundary-layer resolution with simple topology, countering the faster growth of Cartesian grids with $Re$ (§1). **Stated**
4. Colella's embedded-boundary method is globally second order but locally first order and must handle small cells; the ghost-cell method keeps cell sizes and has no small-cell problem (§1). **Stated**
5. Convection by a hybrid central/QUICK scheme with a weight raised in steps of 0.03 to at most 0.1; diagonal diffusion Crank–Nicolson, the rest RK3 at CFL about 1 (§2.1–2.2). **Stated**
6. Boundary cells revert to central differences so ghost cells are only the solid cells adjacent (including diagonally) to fluid cells (§2.4). **Stated**
7. Image-point bilinear interpolation in computational space with boundary-condition rows for missing nodes is well posed for all positions, unlike Gibou et al.'s ghost-fluid extrapolation, which falls back to first order (§2.4–2.5). **Derived**
8. Sharp ghost-cell methods choose local second-order accuracy over strict conservation; only cut cells deliver both (§2.5). **Stated**
9. Grid refinement on a cylinder shows nearly second order in $L^2$ and $L^\infty$, "globally and locally second-order accurate"; time accuracy second order (§3). **Shown**
10. Cylinder drag, base pressure and Strouhal number agree with spectral and experimental data up to $Re=3900$; an $M=0.4$ case reaches local $M\approx0.55$; Eppler 211 airfoil at $Re_c=6\times10^4$, $M=0.2$, against Althaus; wing-tip flow (§3). **Shown**
11. MPI domain decomposition with an approximate cross-partition line SOR (§2.6). **Stated**

# Notation map

| Ghias et al. (2007) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi$ | $w$ | generic variable; $\phi$ is the level set |
| GC, BI, IP | ghost point, $\mathbf x_{BI}$, $\mathbf x_{IP}$ | |
| $(y^1,y^2)$, $J$, $B^{jk}$ | curvilinear coordinates, Jacobian, metric tensor, page-local | |
| $E_t$ | $E$ | total energy per unit volume |
| $n$ (QUICK weight) | page-local | |

# Reference list

43 references, merged complete into the [bibliography](/bibliography.md)
from the Crossref deposited list.

# Pages created or updated

Chunk 2 (2026-11-08), list updated in chunk 4 (2026-11-08). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md)
- [Small-cell problem](/definitions/small-cell-problem.md)
- [Cut-cell (embedded-boundary) finite-volume method](/methods/cut-cell-method.md)
- [Ghost-cell immersed boundary method](/methods/ghost-cell-method.md)
- [Ghost fluid method](/methods/ghost-fluid-method.md)
- [Discrete conservation](/properties/discrete-conservation.md)
