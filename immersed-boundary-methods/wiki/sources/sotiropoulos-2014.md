---
type: Source
title: "Sotiropoulos & Yang (2014) — Immersed boundary methods for simulating fluid–structure interaction"
description: "Review of immersed boundary methods for fluid–structure interaction: diffused-interface (classic, direct forcing, penalization) and sharp-interface (cut cell, immersed interface, hybrid Cartesian, curvilinear immersed boundary) methods, loose and strong partitioned coupling with added-mass issues and convergence acceleration, iterative solvers, and applications from vortex-induced vibration to renewable energy."
resource: "doi:10.1016/j.paerosci.2013.09.003"
source_kind: paper
authors: [Sotiropoulos F., Yang X.]
year: 2014
venue: "Prog. Aerosp. Sci. 65:1-21"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2014_Crossref_Progress_in_Aerospace_Sciences_Sotiropoulos_Immersed_boundary_methods_for_simulating_fluidstructure_inte.pdf"
tags: [review, fluid-structure-interaction, coupling, sharp-interface, diffuse-interface]
timestamp: 2026-11-08T18:12:00Z
---

# Summary

Sotiropoulos and Yang review immersed boundary methods with emphasis on
fluid–structure interaction. They split the methods into diffused-interface
and sharp-interface classes ([sharp and diffuse interfaces](/definitions/sharp-and-diffuse-interface.md)),
including the curvilinear immersed boundary (CURVIB) method of their group
([ghost-cell method](/methods/ghost-cell-method.md)), and organize coupling
strategies into monolithic, loosely coupled and strongly coupled partitioned
schemes with relaxation and Newton acceleration
([fluid–structure coupling](/methods/fluid-structure-coupling.md)).

# Version read

Version of record, Prog. Aerosp. Sci. 65, 1–21 (2014), 21 pages. Methods and
coupling sections (§1–§4) read; applications and conclusions (§5–§7) skimmed.
Page-1 title and authors match Crossref.

# Key claims

1. Immersed boundary methods avoid the dynamic remeshing that arbitrary Lagrangian–Eulerian methods need for complex bodies and large deformations (§1). **Stated**
2. Methods divide into diffused-interface (classic IB, explicit and implicit direct forcing, penalization) and sharp-interface (cut cell, immersed interface, hybrid Cartesian–IB, CURVIB) methods (§3). **Stated**
3. In sharp reconstruction schemes the boundary velocity is imposed on the intermediate velocity, so mass conservation must be corrected in the final projection step (§3). **Stated**
4. Monolithic coupling is unconditionally stable but loses modularity; loose coupling is subject to artificial added-mass instability for light structures (§4). **Stated**
5. Added mass is constant as $\Delta t\to0$ in incompressible flow and proportional to $\Delta t$ in compressible flow (§4, citing Causin et al.). **Stated** (cited)
6. Strong coupling iterates within each step, with under-relaxation fixed or by Aitken's $\Delta^2$ or steepest descent, or with Newton–Raphson methods (§4.3–4.4). **Stated**
7. A limitation is the inability to cluster grid points near walls, motivating wall models and coupling with adaptive refinement for high-Reynolds-number flows (§7). **Stated**

# Notation map

| Sotiropoulos & Yang (2014) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf X_\Gamma$, $\mathbf u(\mathbf X_\Gamma)$ | $\mathbf X_\ell$, $\mathcal J\mathbf u$ | |
| $\xi^i$ | curvilinear coordinates, page-local | |
| $\omega$ | under-relaxation factor, page-local | |

# Reference list

219 references, merged complete into the [bibliography](/bibliography.md)
from the Crossref deposited list.

# Pages created or updated

Chunk 3 (2026-11-08). This source is cited on:

- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md)
- [Fluid–structure coupling in immersed boundary methods](/methods/fluid-structure-coupling.md)
- [Ghost-cell immersed boundary method](/methods/ghost-cell-method.md)
