---
type: Source
title: "Balsara, Käppeli, Boscheri & Dumbser (2023) — Curl constraint-preserving reconstruction and the guidance it gives for mimetic scheme design"
description: "Edge-centred curl-preserving (ECCP) reconstruction for PDEs whose involution keeps a vector field curl-free or curl-constrained: tangential components on edges, a vertex potential upwinded by a multidimensional Riemann solver, closed-form reconstructions from 1D WENO edge moments (2D orders 1–4, 3D orders 1–3), a first-order upwinding argument, von Neumann CFL limits, and tests on a toy curl system and GPR heat conduction."
resource: "doi:10.1007/s42967-021-00160-3"
source_kind: paper
authors: [Balsara D.S., Käppeli R., Boscheri W., Dumbser M.]
year: 2023
venue: "Commun. Appl. Math. Comput. 5:235-294"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2023-CAMC-Balsara-101007s42967-021-00160-3.pdf"
tags: [involution, reconstruction, staggered, multidimensional-riemann-solver, weno]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The curl dual of divergence-free reconstruction and constrained
transport. Merged into the new
[curl-preserving reconstruction](/methods/curl-preserving-reconstruction.md)
page and the divergence-free reconstruction, GLM, Riemann-solver, SSP and
FV-reconstruction pages.

# Key claims

1. **Collocation** (§§1–1.1): edges for the field, vertices for the
   potential, with a multidimensional upwind value there.
2. **Failure of the naive reconstruction and its fix** (§2.2, eqs. 3–11):
   correction terms that vanish on edges, fixed by the curl constraint.
3. **Nonlinear hybridization** (§2.2): edge moments from 1D TVD or WENO.
   Constraint-born modes are part of the field (§2.3).
4. **Fourth order** (§2.4): zone-centred modes are needed; five free
   parameters fixed by least squares against zone-centred FV-WENO.
5. **3D** (§3): five independent face circulations; curl reconstruction
   contains divergence-free reconstruction of the curl.
6. **Upwinding** (§§2.5, 3.4): the first-order update is a centred
   difference plus directional parabolic dissipation.
7. **Von Neumann** (§4): maximum Courant numbers 0.7071, 1.1507 and 1.3040
   at orders 2–4.
8. **Tests** (§§5–6): stationary curl-free equilibrium (design order; the
   Table 1 fourth-order $L^1$ error at $256^2$ is a duplicated typo),
   inhomogeneous curl involution, GPR heat-conducting blast.
9. **Scope remark** (§1): skipping constraint-preserving reconstruction
   gives unstable DG-like schemes (Balsara and Käppeli, cited).

# Notation map

| Balsara et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf J$, $\mathbf R = \nabla\times\mathbf J$ | $\mathbf J$, $\boldsymbol\Omega$ | registry $R$ is the eigenvector matrix |
| $\phi$, $\chi$ (vertex potential) | (words) | collide with $\phi_i$, $\chi$ |
| $V^1_x, \dots$ (edge values), $\Delta_x V^1_x$ (edge moments) | (words) | the paper's $\Delta$ is a modal coefficient |
| $\tau$ (relaxation time) | (words) | registry $\tau$ is the WENO-Z indicator |
| $\gamma$ in $p = \gamma^2\rho$ (§5) | (words) | registry $\gamma$ is the specific-heat ratio |
| $\Delta x, \Delta y, \Delta z$ | $h_x, h_y, h_z$ | |

# Pages created or updated

* Updated [Approximate Riemann solvers as building blocks of capturing schemes](/methods/approximate-riemann-solvers.md).
* Created [Divergence-free reconstruction of face-centred magnetic fields](/methods/divergence-free-reconstruction.md).
* Created [Edge-centred curl-preserving (ECCP) reconstruction and schemes](/methods/curl-preserving-reconstruction.md).
* Created [Hyperbolic (GLM) divergence cleaning](/methods/hyperbolic-divergence-cleaning.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [Notation registry](/notation.md): batch-6 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2023-CAMC-Balsara-101007s42967-021-00160-3.pdf` (doi:10.1007/s42967-021-00160-3, checked on Crossref: Commun. Appl. Math. Comput. 5(1):235–294, issue March 2023, online December 2021; typeset open-access article): text extraction, all 60 pages; pp. 242–244, 254, 256, 272 and 283 read from the page images. The multi-line coefficient arrays of eqs. 12–23 and 42–57 are not reproduced. Misprint: eq. 26 divides by $\Delta x$ where $\Delta y$ is meant. Reference list: 55 entries.
