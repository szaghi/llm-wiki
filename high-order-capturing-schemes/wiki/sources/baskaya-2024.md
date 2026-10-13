---
type: Source
title: "Başkaya, Capriati, Turchi, Magin & Hickel (2024) — Assessment of immersed boundary methods for hypersonic flows with gas–surface interactions"
description: "Compares a strictly conservative cut-cell immersed boundary (INCA), two ghost-cell immersed boundaries and a body-fitted reference on reacting hypersonic flows: all agree on adiabatic walls and surface pressure, but on a Mach 8.98 cylinder with a 300 K wall the ghost-cell methods miss the stagnation heat flux (0.167 against 7.19 MW/m²) and the ablation blowing rate, which the authors trace to wall conservation errors rather than reconstruction order."
resource: "doi:10.1016/j.compfluid.2023.106134"
source_kind: paper
authors: [Başkaya A.O., Capriati M., Turchi A., Magin T., Hickel S.]
year: 2024
venue: "Comput. Fluids 270:106134"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2024-CompFluids-Baskaya-101016jcompfluid2023106134.pdf"
tags: [immersed-boundary, embedded-boundary, hypersonic, conservation]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

Three Cartesian immersed-boundary solvers and one body-fitted solver are
compared on reacting, viscous hypersonic flows with gas–surface
interaction: INCA's conservative cut-element method (third-order WENO,
HLLC, third-order Runge–Kutta), INCA with the conservative flux treatment
switched off, the ghost-cell solver CHESS, and the body-fitted US3D. The
isolating experiment is the INCA on/off pair, which differ only in the
conservative wall treatment. Merged into
[immersed-boundary methods](/methods/immersed-boundary-method.md) and
[cut-cell finite volume](/methods/cut-cell-finite-volume.md).

# Key claims

1. **Taxonomy** (§3, Fig. 1): ghost-cell IB fills ghost cells from image
   points; cut-cell IB balances fluxes over the fluid part of each cut
   cell; both are discrete-forcing methods.
2. **Ghost-cell conservation error** (§3): from the nonlinear flux, the
   image-point interpolation and the wall curvature.
3. **Small cut cells** are mixed or merged with neighbours; the procedure
   is not described here (§3).
4. **Cut-element method** (§3.2): keeps every intersection with the
   surface triangulation and also fills ghost cells, so interior stencils
   are unchanged.
5. **Reconstruction order is not the cause** (§4.5.2): the conservative
   method also uses second-order reconstruction and gets the heat flux
   right, against an earlier attribution to linear temperature
   interpolation.
6. **Controlled experiment** (§5, Fig. 18): with the conservative flux
   treatment off, INCA fails too: on the cylinder heat flux it is closer
   than CHESS but "clearly wrong", and on the ablator it gives "a very
   similar overprediction" of the blowing rate (corrected at the
   2026-10-13 deep lint; it read "fails like CHESS").
7. **Scaling of the error** (§5): expected to follow the truncation error
   and matter only at steep wall gradients, as at cold walls (stated, not
   measured).
8. **Gas–surface conditions** (§2.2, eqs. 8–13): surface mass balance,
   impingement flux, blowing velocity, graphite nitridation efficiency.

**Tests** (§4): a 0-D reactor, 1-D diffusion and catalytic diffusion, a
reacting shock tube (Grossman–Cinnella), the HEG cylinder at Mach 8.98
(adiabatic, 300 K inert, and fully catalytic walls; Table 7), and a
graphite ablator in a nitrogen plasma. No order study, no moving
boundary. The cylinder is a viscous reacting blunt body, not the
inviscid [hypersonic blunt body](/benchmarks/hypersonic-blunt-body.md).

# Notation map

| Başkaya et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho_i$, $J_i$, $\dot\omega_i$ | words | species density, diffusion flux, source |
| $\gamma$ (reaction efficiency) | words | $\gamma$ is the ratio of specific heats |
| $q_w$, $p_0$ | words | wall heat flux, stagnation pressure |
| $M_\infty$ | $\mathrm{Ma}$ | |

# Pages created or updated

* Contributed to [Immersed-boundary methods](/methods/immersed-boundary-method.md), [Cut-cell finite volume](/methods/cut-cell-finite-volume.md).
* Updated [Inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md) (conservation at the wall).
* Also cited on [HLLC Riemann solver](/methods/hllc-riemann-solver.md) (created in batch 12).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2024-CompFluids-Baskaya-101016jcompfluid2023106134.pdf`.
   * **Version.** arXiv:2309.09657v1, the submitted preprint (it opens
     with the graphical abstract), not the typeset article.
   * **Identity.** doi:10.1016/j.compfluid.2023.106134, checked on
     Crossref: Comput. Fluids 270:106134, issue February 2024.
   * **How it was read.** Text extraction, all sections; Tables 3, 5 and 7
     and eq. 13 checked on the page images. The 0.167 MW/m² ghost-cell
     heat flux is as printed in Table 7.
   * **Reference list:** 60 entries.
