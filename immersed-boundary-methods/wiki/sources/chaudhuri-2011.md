---
type: Source
title: "Chaudhuri, Hadjadj & Chinnayya (2011) — On the use of immersed boundary methods for shock/obstacle interactions"
description: "Ghost-point direct-forcing immersed boundary method combined with a fifth-order WENO scheme for inviscid shock–obstacle interaction: image-point values by inverse-distance weighting that excludes solid nodes, per-direction ghost data at corners, validated against oblique-shock theory, bow-shock stand-off and experiments for moving shocks over a prism and a cylinder."
resource: "doi:10.1016/j.jcp.2010.11.016"
source_kind: paper
authors: [Chaudhuri A., Hadjadj A., Chinnayya A.]
year: 2011
venue: "J. Comput. Phys. 230(5):1731-1748"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2011_Crossref_Journal_of_Computational_Physics_Chaudhuri_On_the_use_of_immersed_boundary_methods_for_shockobstacle_in.pdf"
tags: [ghost-cell, compressible, shock, weno, high-order]
timestamp: 2026-11-08T18:08:00Z
---

# Summary

Chaudhuri, Hadjadj and Chinnayya couple a [ghost-cell](/methods/ghost-cell-method.md)
direct-forcing immersed boundary method with the fifth-order WENO scheme for
2-D Euler flows with strong shocks. Two layers of ghost points receive values
reflected from image points, which are interpolated by inverse-distance
weighting that drops solid neighbours; ghost data are kept per direction so
sharp corners need no special treatment. The method reproduces oblique-shock
and bow-shock theory and experimental triple-point trajectories for
Schardin's problem and a shocked cylinder
([shock–obstacle interaction](/benchmarks/shock-obstacle-interaction.md)).

# Version read

Version of record, J. Comput. Phys. 230, 1731–1748 (2011), 18 pages. Read in
full; the discussion of wake pressure spectra skimmed. Page-1 title and
authors match Crossref.

# Key claims

1. Ghost points are solid points with a fluid point within two indices, two layers as needed by the WENO stencil; each is linked to a unique image point along the boundary normal (§2.2). **Stated**
2. Image-point values come from inverse-distance weighting of the four surrounding nodes, with solid nodes excluded by letting their distance go to infinity, and the nearest node used when a distance vanishes (§2.2). The abstract calls the interpolation "a local quadratic scheme". **Stated**
3. Storing ghost data per space direction lets x-fluxes and y-fluxes use different image points at sharp corners, keeping unbiased stencils (§2.2). **Stated**
4. $M=3.5$ past a $20^\circ$ prism: shock angle $34.5^\circ$ with interpolation against $34.58^\circ$ from theory; without it $31.9^\circ$ (8 % off) with spurious oscillations and secondary shocks (§3.1). **Shown**
5. $M=3.5$ past a cylinder on grids from 0.061 to 16 million points: the $\theta$–$\beta$–$M$ relation along the bow shock and the stand-off distance converge to theory (§3.1). **Shown**
6. The boundary accuracy is second order and the global $L^2$ accuracy at least second order, measured against the finest grid away from the unsteady wake (§3.1). **Shown**
7. Schardin's problem and a $M_s=2.81$ shock on a cylinder reproduce triple-point and vortex trajectories of experiments and earlier computations (§4). **Shown**
8. Simulations needed 200–500 CPU hours on 24–40 processors (§3). **Stated**

# Notation map

| Chaudhuri et al. (2011) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| GP, IP, BP, NP | ghost point, $\mathbf x_{IP}$, $\mathbf x_{BI}$, neighbour points | |
| $\psi_b$ | $\Gamma$ (boundary function) | |
| $Q$ | $\mathbf q$ or primitive variables | |
| $\theta$, $\beta$ | deflection and shock angles, page-local | $\beta$ is the elliptic coefficient elsewhere |

# Reference list

37 references, merged complete into the [bibliography](/bibliography.md)
from the Crossref deposited list.

# Pages created or updated

Chunk 2 (2026-11-08). This source is cited on:

- [Shock–obstacle interaction](/benchmarks/shock-obstacle-interaction.md)
- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Ghost-cell immersed boundary method](/methods/ghost-cell-method.md)
