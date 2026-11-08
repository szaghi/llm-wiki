---
type: Source
title: "Tseng & Ferziger (2003) — A ghost-cell immersed boundary method for flow in complex geometry"
description: "Introduces a ghost-cell immersed boundary method on Cartesian grids: ghost values inside the body are extrapolated by linear or quadratic polynomial reconstruction (or through an image point) so that Dirichlet, Neumann or Robin conditions hold on the boundary; second order overall, applied to a cylinder, LES over a wavy wall and an ocean model."
resource: "doi:10.1016/j.jcp.2003.07.024"
source_kind: paper
authors: [Tseng Y.-H., Ferziger J.H.]
year: 2003
venue: "J. Comput. Phys. 192(2):593-623"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2003_Crossref_Journal_of_Computational_Physics_Tseng_A_ghost-cell_immersed_boundary_method_for_flow_in_complex_ge.pdf"
tags: [ghost-cell, sharp-interface, incompressible, les, geophysical]
timestamp: 2026-11-08T18:08:00Z
---

# Summary

Tseng and Ferziger extend the direct forcing of Fadlun et al. into a
[ghost-cell immersed boundary method](/methods/ghost-cell-method.md): cells
whose centre lies inside the body next to fluid nodes receive values
extrapolated from a polynomial fitted through nearby fluid nodes and a
boundary point, so the boundary condition is imposed implicitly and sharply.
Large negative extrapolation weights are avoided with an image point or by
moving the boundary point; Neumann and Robin conditions, staggered grids and
3-D follow by changing the fitted system. Linear and quadratic
reconstructions both keep overall second order on a cylinder; the method is
applied to LES over a wavy wall and to the MIT ocean model.

# Version read

Version of record, J. Comput. Phys. 192, 593–623 (2003), 31 pages. §§1–2 read
in full; §§3–4 (applications) for set-up and conclusions. Page-1 title and
authors match Crossref.

# Key claims

1. Feedback forcing induces spurious oscillations and restricts the time step, "effectively limiting the technique to two-dimensions"; Mohd-Yusof's forcing does not (§1). **Stated**
2. Immersed boundary schemes either spread the forcing near the surface or reconstruct the solution locally from boundary values, "and the two approaches are equivalent"; local reconstruction is more flexible and can be made accurate (§2.2, citing Iaccarino and Verzicco). **Stated**
3. The ghost-cell forcing has no free constants, enforces the condition to numerical precision, costs no extra CPU and does not affect the stability of the time integration (§2.2). **Stated**
4. Linear reconstruction on the ghost node, two nearest fluid nodes and the boundary point needs a $3\times3$ system in 2-D ($4\times4$ in 3-D); quadratic needs $6\times6$ ($10\times10$) (§2.3). **Derived**
5. Extrapolation can give large negative weights when the boundary is close to a fluid node, leading to non-convergence; an image point (Majumdar et al.) or moving the boundary point onto fluid nodes closer than $0.1\Delta x$ (Gibou et al.) cures it (§2.3, Fig. 4). **Stated**
6. Inverse-distance weighting preserves local extrema and gives smooth reconstructions (§2.3). **Stated**
7. Neumann and Robin conditions are imposed by changing the reconstruction matrix ($B_R=aB_D+bB_N$) (§2.4–2.5). **Derived**
8. Staggered grids need separate weights for each variable; the extra storage is small because the boundary is lower dimensional (§2.6). **Stated**
9. Cylinder flow: overall second order with both linear and quadratic reconstruction; the higher-order boundary treatment is slightly more accurate (§3). **Shown**
10. LES (dynamic mixed model) of turbulent flow over a wavy boundary agrees with a boundary-fitted simulation at lower CPU and memory cost; the MITGCM implementation improves on stair-step and partial-cell topography (§3–§4). **Shown**

# Notation map

| Tseng & Ferziger (2003) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi$ | $w$ (generic variable) | $\phi$ is the level set in the registry |
| $G$, $O$, $I$ | ghost point, boundary point $\mathbf x_{BI}$, image point $\mathbf x_{IP}$ | |
| $V_i$ | $\mathbf V$ or $\mathbf u_\Gamma$ | target / boundary velocity |
| $B$ | reconstruction (Vandermonde) matrix, page-local | |
| $P$ | $p/\rho$ (kinematic pressure) | |
| $p$ (IDW power) | page-local | registry $p$ is pressure |

# Reference list

49 printed references, merged complete into the [bibliography](/bibliography.md)
from the Crossref deposited list.

# Pages created or updated

Chunk 2 (2026-11-08), list updated in chunk 3 (2026-11-08). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Direct (discrete-time) forcing](/methods/direct-forcing.md)
- [Ghost-cell immersed boundary method](/methods/ghost-cell-method.md)
- [Ghost fluid method](/methods/ghost-fluid-method.md)
