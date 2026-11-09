---
type: Source
title: "Visbal & Gaitonde (2002) — On the use of higher-order finite-difference schemes on curvilinear and deforming meshes"
description: "Sixth-order compact schemes with high-order filters on stretched, curvilinear and deforming meshes: filtering for nonsmooth meshes, conservative metric evaluation for 3-D free-stream preservation, and the time derivative of the Jacobian from the geometric conservation law on moving meshes."
resource: "doi:10.1006/jcph.2002.7117"
source_kind: paper
authors: [Visbal M.R., Gaitonde D.V.]
year: 2002
venue: "J. Comput. Phys. 181(1):155–185"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2002_Crossref_Journal_of_Computational_Physics_Visbal_On_the_Use_of_Higher-Order_Finite-Difference_Schemes_on_Curv.pdf"
tags: [free-stream-preservation, gcl, compact-scheme, moving-mesh, high-order]
timestamp: 2026-11-08T20:38:00Z
---

# Summary

Visbal and Gaitonde make high-order compact schemes usable on practical meshes: a discriminating low-pass filter controls the oscillations caused by nonsmooth grids, Thomas and Lombard's conservative metric form differenced with the flux scheme restores [free-stream preservation](/properties/free-stream-preservation.md) in 3-D ([conservative metric evaluation](/methods/conservative-metric-evaluation.md)), and the [geometric conservation law](/properties/geometric-conservation-law.md) supplies the time derivative of the Jacobian on deforming meshes.

# Version read

Version of record, J. Comput. Phys. 181, 155–185 (2002). §§4.1–4.3 and §5 read in full; §§1–3 and the applications in outline.

# Key claims

1. Without a filter, compact schemes on nonsmooth meshes oscillate; the filter restores stability and accuracy across large grid discontinuities (§4.1). **Shown**
2. In 3-D, standard metric evaluation violates the identities even at sixth order; the conservative form with the flux operator preserves the free stream on a wavy mesh (§4.2, Table VII). **Shown**
3. Evaluating the time derivative of the Jacobian from the GCL makes all discrete identities vanish for uniform flow, independently of how grid speeds are computed (§4.3). **Derived**

# Notation map

| Visbal & Gaitonde (2002) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\hat\xi_x=J^{-1}\xi_x$, $J$ (inverse convention) | $J\xi_x$ (metric terms), $J$ | the source's $J$ is the inverse Jacobian $\partial(\xi,\eta,\zeta)/\partial(x,y,z)$ |
| $\tau$ | $t$ at fixed $\boldsymbol\xi$ |  |
| $I_1$–$I_4$ | metric identities and GCL |  |

# Reference list

28 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 2 (2026-11-08). This source is cited on:

- [Conservative metric evaluation](/methods/conservative-metric-evaluation.md)
- [Free-stream preservation](/properties/free-stream-preservation.md)
- [Geometric conservation law](/properties/geometric-conservation-law.md)
- [Grid-induced truncation error](/results/grid-induced-truncation-error.md)
