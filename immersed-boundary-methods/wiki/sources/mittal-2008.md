---
type: Source
title: "Mittal et al. (2008) — A versatile sharp interface immersed boundary method for incompressible flows with complex boundaries"
description: "Three-dimensional sharp-interface ghost-cell immersed boundary method for incompressible flow around stationary, moving and deforming bodies described by triangulated surfaces on non-uniform Cartesian grids: normal-probe image points with trilinear interpolation, a fresh-cell treatment, geometric multigrid, and validation from cylinders and spheres to a deforming fish fin."
resource: "doi:10.1016/j.jcp.2008.01.028"
source_kind: paper
authors: [Mittal R., Dong H., Bozkurttas M., Najjar F.M., Vargas A., von Loebbecke A.]
year: 2008
venue: "J. Comput. Phys. 227(10):4825-4852"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2008_Crossref_Journal_of_Computational_Physics_Mittal_A_versatile_sharp_interface_immersed_boundary_method_for_inc.pdf"
tags: [ghost-cell, sharp-interface, incompressible, moving-boundary, three-dimensional, biofluid]
timestamp: 2026-11-08T18:08:00Z
---

# Summary

Mittal, Dong, Bozkurttas, Najjar, Vargas and von Loebbecke present a
[ghost-cell method](/methods/ghost-cell-method.md) designed from the start
for complex, moving and deforming 3-D bodies. Surfaces are unstructured
triangle meshes; ghost values come from a normal probe to an image point with
trilinear interpolation, kept well conditioned by substituting the boundary
condition for the ghost node itself; cells that emerge from the body get an
interpolated value ([fresh-cell problem](/definitions/fresh-cell-problem.md)).
The collocated solver with separately updated face velocities and a geometric
multigrid Poisson solver is second order locally and globally; validation
covers [cylinders](/benchmarks/flow-past-circular-cylinder.md),
[spheres](/benchmarks/flow-past-sphere.md), accelerated plates and bodies,
and a fish pectoral fin with measured kinematics.

# Version read

Version of record, J. Comput. Phys. 227, 4825–4852 (2008), 28 pages. §§1–2
read in full, §3 for set-up and key comparisons. Page-1 title and authors
match Crossref (Crossref gives the fourth author as F. Najjar).

# Key claims

1. The method has no ad hoc constants and no momentum forcing in fluid cells, hence a sharp boundary (§1). **Stated**
2. Unlike Gibou et al.'s ghost-fluid method, the interpolation stays well conditioned without lower-order fixes, and normal-direction interpolation simplifies Neumann conditions (§1). **Stated**
3. Cut-cell methods give the same order of accuracy, but a 3-D cut-cell implementation had not been accomplished (§1, citing Mittal and Iaccarino). **Stated**
4. Collocated variables with separately updated face velocities conserve mass to machine accuracy and, with central differences, have good kinetic-energy conservation up to $Re\sim10^4$ without upwinding (§2.1). **Stated**
5. Geometric multigrid with a line Gauss–Seidel smoother solves the pressure equation with nearly linear cost, an advantage over unstructured body-conformal methods (§2.1). **Stated**
6. Solid–fluid demarcation for moving bodies needs only a narrow band of cells per step and takes a small fraction of CPU time (§2.2). **Stated**
7. Image-point trilinear interpolation, with the boundary condition replacing a ghost node in its own stencil, and coupled ghost values solved by point Gauss–Seidel (diagonally dominant) (§2.2). **Derived**
8. Dirichlet velocity conditions are imposed to second order, giving local and global second order for velocity (§2.2). **Derived**
9. Fresh cells, at most one layer per step, get their intermediate velocity by interpolation consistent with their previous ghost-cell stencil (§2.2). **Stated**
10. A grid refinement study gives second order in $L^1$, $L^2$ and $L_{\max}$ (§3). **Shown**
11. Cylinder drag, base pressure and Strouhal number, low-$Re$ airfoils, spheres for $Re=100$–$350$, an accelerating thin plate ($Re_h=126$, $1000$), a suddenly accelerated cylinder ($Re=550$) and sphere agree with established data; a deforming fish fin shows versatility (§3). **Shown**

# Notation map

| Mittal et al. (2008) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi$ | $w$ | generic variable |
| GC, BI, IP, $\Delta l$ | ghost point, $\mathbf x_{BI}$, $\mathbf x_{IP}$, $\Delta l$ | |
| $u_i$, $U_i$ | cell-centre and face-centre velocity, page-local | |
| $\hat n$ | $\mathbf n$ | outward from the body |

# Reference list

65 references, merged complete into the [bibliography](/bibliography.md)
from the Crossref deposited list.

# Pages created or updated

Chunk 2 (2026-11-08), list updated in chunk 4 (2026-11-08). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Flow past a sphere](/benchmarks/flow-past-sphere.md)
- [Fresh-cell problem](/definitions/fresh-cell-problem.md)
- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md)
- [Cut-cell (embedded-boundary) finite-volume method](/methods/cut-cell-method.md)
- [Ghost-cell immersed boundary method](/methods/ghost-cell-method.md)
- [Ghost fluid method](/methods/ghost-fluid-method.md)
- [Discrete conservation](/properties/discrete-conservation.md)
