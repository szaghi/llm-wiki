---
type: Source
title: "Natarajan, Grout, Zhang & Day (2022) — A moving embedded boundary approach for the compressible Navier–Stokes equations in a block-structured adaptive refinement framework"
description: "Moving embedded boundaries for compressible viscous flow in AMReX: conservative unsplit cut cells with hybrid divergence and flux redistribution, a reflected ghost state for the flux on moving boundary faces, volume-averaged initialization of freshly cleared cells, least-squares wall stresses, and tests from acoustics to shocks and oscillating cylinders."
resource: "doi:10.1016/j.jcp.2022.111315"
source_kind: paper
authors: [Natarajan M., Grout R., Zhang W., Day M.]
year: 2022
venue: "J. Comput. Phys. 465:111315"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2022_Crossref_Journal_of_Computational_Physics_Natarajan_A_moving_embedded_boundary_approach_for_the_compressible_Nav.pdf"
tags: [cut-cell, embedded-boundary, moving-boundary, compressible, amr]
timestamp: 2026-11-08T18:12:00Z
---

# Summary

Natarajan, Grout, Zhang and Day extend the AMReX embedded-boundary
[cut-cell method](/methods/cut-cell-method.md) to moving bodies in compressible
viscous flow: the hybrid divergence and [redistribution](/methods/redistribution.md)
of Colella et al. stabilize small cells, the flux through the moving boundary
face comes from a Riemann problem with a reflected ghost state, and freshly
cleared cells are filled by volume averaging ([fresh-cell problem](/definitions/fresh-cell-problem.md)).
Tests span acoustics, expansion fans, shocks ([shock–obstacle interaction](/benchmarks/shock-obstacle-interaction.md))
and oscillating cylinders ([flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)).

# Version read

arXiv:2108.00126v1 (July 2021), the preprint of the published paper; title
and authors match Crossref. §§1–2 read in full, §3 for set-up and results.

# Key claims

1. Small cells are stabilized by a volume-fraction-weighted hybrid of conservative and non-conservative divergences with redistribution (§2). **Stated**
2. The flux on a moving boundary face uses a Riemann problem whose exterior state mirrors the cut-cell state with normal velocity reflected about the wall velocity (§2). **Derived**
3. Freshly cleared cells take a volume-weighted average of valid neighbours; uniform flow with a body moving at the flow speed is preserved exactly (§2). **Derived**
4. Wall stresses come from a third-order least-squares fit using the body velocity at the face (§2). **Stated**
5. A pulsating sphere matches the acoustic solution; the entropy error of a receding-piston expansion fan converges at first order (§3). **Shown**
6. The mass error of an oscillating piston in a closed cylinder decreases with refinement (§3). **Shown**
7. Shock–cylinder, shock–wedge, shock–cone, a pitching NACA 0012 and moving or oscillating cylinders at $Re=40$, $100$, $185$ agree with experiments and computations (§3). **Shown**

# Notation map

| Natarajan et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $Q$ | $\mathbf q$ | conserved variables |
| $\alpha$ (volume fraction) | $\kappa$ | |
| $u_w$, $u_s$ | $\mathbf u_\Gamma$, face velocity | |
| $w_j$ | $w_{\mathbf i\mathbf j}$ | redistribution weights |

# Reference list

90 references, merged complete into the [bibliography](/bibliography.md)
from the Crossref deposited list.

# Pages created or updated

Chunk 3 (2026-11-08). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Shock–obstacle interaction](/benchmarks/shock-obstacle-interaction.md)
- [Fresh-cell problem](/definitions/fresh-cell-problem.md)
- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Cut-cell (embedded-boundary) finite-volume method](/methods/cut-cell-method.md)
- [Ghost-cell immersed boundary method](/methods/ghost-cell-method.md)
- [Flux redistribution for cut cells](/methods/redistribution.md)
- [Discrete conservation](/properties/discrete-conservation.md)
