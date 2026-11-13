---
type: Source
title: "Schneiders, Günther, Meinke & Schröder (2016) — An efficient conservative cut-cell method for rigid bodies interacting with viscous compressible flows"
description: "Strictly conservative compressible cut-cell method for freely moving rigid bodies, with a predictor-corrector reformulation of multistage Runge-Kutta that builds the moving geometry once per step, a weighted-Taylor small-cell reconstruction, conservative handling of emerging and submerging cells, and strong fluid-body coupling."
resource: "doi:10.1016/j.jcp.2016.01.026"
source_kind: paper
authors: [Schneiders L., Günther C., Meinke M., Schröder W.]
year: 2016
venue: "J. Comput. Phys. 311:62–86"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2016_Crossref_Journal_of_Computational_Physics_Schneiders_An_efficient_conservative_cut-cell_method_for_rigid_bodies_i.pdf"
tags: [cut-cell, moving-boundary, fluid-structure-interaction, conservation, particulate-flow]
timestamp: 2026-11-13T05:49:40Z
---

# Summary

Schneiders, Günther, Meinke and Schröder extend their moving-boundary [cut-cell](/methods/cut-cell-method.md) method to freely moving rigid bodies. A predictor–corrector Runge–Kutta scheme with the stability polynomial of the multistage scheme needs the cut-cell geometry only at $t^{n+1}$; cells that disappear into or emerge from the body are handled conservatively ([fresh-cell problem](/definitions/fresh-cell-problem.md)) and the [geometric conservation law](/definitions/geometric-conservation-law.md) is written for the scheme. Rigid bodies are coupled strongly ([fluid–structure coupling](/methods/fluid-structure-coupling.md)).

# Version read

Version of record, J. Comput. Phys. 311, 62–86 (2016). §§1–4 read, §5 by test, §6.

# Key claims

1. The predictor–corrector Runge–Kutta scheme combines residuals at $t^n$ and $t^{n+1}$ in every stage, keeps the stability polynomial of the multistage scheme and builds the residual operator once per step, giving speed-ups of 1.4 to 2.5 for five stages (§3.2). **Derived**
2. Coupled solvers need interface states only at $t^{n+1}$, so the rigid body is not moved within a step (§3.2). **Stated**
3. The contents of a submerging cell go to its neighbours with volume-weighted averaging that respects the GCL; an emerging cell is linked to a neighbour for a single step (§3.8). **Stated**
4. The method conserves mass, momentum and energy strictly, also for large displacements; for a Mach-2 piston the shock position and front velocity converge at second order in time (§5.1). **Shown**
5. Settling and oscillating spheres, an ellipsoid in shear and a particle cloud in decaying isotropic turbulence are computed without spurious force oscillations, even on coarse meshes (§5). **Shown**

# Notation map

| Schneiders, Günther, Meinke & Schröder (2016) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $QV$ | volume-integrated $\mathbf q$ | page-local |
| $R(t;Q)$ | discrete residual | page-local |
| $\alpha_k$ | Runge–Kutta stage coefficients | page-local |
| $\sigma_{c,l}$ | $w_{\mathbf i\mathbf j}$ | redistribution fractions |

# Reference list

94 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 7 (2026-11-13). This source is cited on:

- [Fresh-cell problem](/definitions/fresh-cell-problem.md)
- [Geometric conservation law](/definitions/geometric-conservation-law.md)
- [Small-cell problem](/definitions/small-cell-problem.md)
- [Spurious force and pressure oscillations](/definitions/spurious-force-oscillations.md)
- [Cell merging for cut cells](/methods/cell-merging.md)
- [Cut-cell (embedded-boundary) finite-volume method](/methods/cut-cell-method.md)
- [Fluid–structure coupling in immersed boundary methods](/methods/fluid-structure-coupling.md)
- [Flux redistribution for cut cells](/methods/redistribution.md)
- [Discrete conservation](/properties/discrete-conservation.md)
