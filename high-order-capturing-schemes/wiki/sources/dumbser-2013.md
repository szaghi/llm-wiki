---
type: Source
title: "Dumbser, Zanotti, Hidalgo & Balsara (2013) — ADER-WENO finite volume schemes with space–time adaptive mesh refinement"
description: "The first better-than-second-order one-step ADER-WENO finite-volume scheme on cell-by-cell, space–time adaptive Cartesian meshes with time-accurate local time stepping and MPI, using a dimension-by-dimension polynomial WENO and a local space–time DG predictor; tested on Euler and GLM-MHD problems."
resource: "doi:10.1016/j.jcp.2013.04.017"
source_kind: paper
authors: [Dumbser M., Zanotti O., Hidalgo A., Balsara D.S.]
year: 2013
venue: "J. Comput. Phys. 248:257-286"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2013-arXiv-Dumbser-1048550arXiv12123585.pdf"
tags: [ader, amr, weno, finite-volume, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper combines ADER-WENO with tree-based AMR. Because the space–time
predictor is element-local and the update is one-step, each level runs
on its own time step and the AMR overhead stays near 25%. Merged into
the new [high-order AMR](/methods/high-order-amr.md),
[ADER](/methods/ader.md) and [polynomial WENO](/methods/polynomial-weno.md)
pages, and into the new [2D Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
and [explosion](/benchmarks/multidimensional-explosion.md) benchmarks.

# Key claims

1. **Lineage** (§1): one-step schemes go back to van Leer (MUSCL) and
   Harten et al. (ENO). Original ADER is Cauchy–Kowalewski based and
   impracticable for complex nonlinear systems. The space–time DG
   predictor replaces it and also handles stiff sources.
2. **WENO** (§2.2): a nodal 1D polynomial WENO on Gauss–Legendre points,
   applied dimension by dimension. It uses three stencils for odd and four
   for even orders, $\lambda = 10^5$ for central stencils, $\epsilon = 10^{-14}$
   and $r = 8$. It is not optimal: the stencil is wider than optimal WENO.
3. **Predictor** (§2.3): element-local weak form in space–time, solved
   by iteration with a MUSCL-type initial guess. The matrices are
   sparse and act dimension by dimension.
4. **AMR rules** (§3): cell-by-cell tree; refinement factor $r \ge M$
   (the reconstruction degree); active, virtual-child and virtual-mother
   status; Voronoi neighbours differ by at most one level; conservative
   coarse–fine fluxes; Löhner-type refinement estimator; MPI exchange
   lists without load balancing.
5. **Overhead** (Table 1): at most 25% at fourth order. The second-order
   AMR scheme is 9.4 times cheaper per element update than fourth order.
6. **Tests** (§4): isentropic vortex convergence at third and fourth
   order, interacting blasts, 2D/3D explosions (2D AMR 3.5 times faster
   than the uniform fine grid), double Mach reflection, forward step, 2D
   Riemann problems, and a co-rotating vortex pair, where second-order
   AMR suffers spurious vortex merging. MHD runs use GLM cleaning: the
   Orszag–Tang vortex (1.8 times faster) and the rotor (more than five
   times fewer elements, no spurious oscillations).

# Notation map

| Dumbser et al. (2013) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $M$ (reconstruction degree) | $K$ | |
| $w_h$, $q_h$ | $\mathcal{P}_i$, $u^{\mathrm p}_i$ | |
| $\lambda_s$, $\lambda$ (central) | $d_k$, $d_{\mathrm c}$ | |
| $\epsilon$, $r$ (power) | $\varepsilon$, $q$ | |
| $\sigma_s$, $\Sigma$ | $\beta_k$, $\mathsf B$ | |
| $r$ (refinement factor), $\ell$, $\ell_{\max}$ | $r_{\mathrm{AMR}}$, level, $N_{\mathrm{lev}}$ | |
| $\sigma$ (status) | (not used) | the troubled-cell flag $\mathcal{B}_i$ is a different flag |
| $\Psi$, $c_h$ | GLM scalar, cleaning speed | words on concept pages |

# Pages created or updated

* Created [ADER one-step schemes (arbitrary high order using derivatives)](/methods/ader.md).
* Updated [Approximate Riemann solvers as building blocks of capturing schemes](/methods/approximate-riemann-solvers.md).
* Updated [Constrained transport for high-order capturing schemes (MHD)](/methods/constrained-transport.md).
* Created [Cylindrical and spherical explosion problem](/benchmarks/multidimensional-explosion.md).
* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md).
* Created [High-order adaptive mesh refinement for capturing schemes](/methods/high-order-amr.md).
* Updated [Isentropic vortex advection (smooth accuracy test)](/benchmarks/isentropic-vortex.md).
* Updated [Lax–Wendroff (Taylor) single-step time discretization](/methods/taylor-time-discretization.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Mach 3 wind tunnel with a forward-facing step](/benchmarks/forward-facing-step.md).
* Updated [MHD rotor](/benchmarks/mhd-rotor.md).
* Updated [Orszag–Tang vortex (2D MHD)](/benchmarks/orszag-tang-vortex.md).
* Created [Polynomial WENO reconstruction with a dominant central stencil](/methods/polynomial-weno.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Created [Two-dimensional Riemann problems (four-quadrant configurations)](/benchmarks/two-dimensional-riemann-problems.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [Woodward–Colella interacting blast waves](/benchmarks/interacting-blast-waves.md).
* Updated [Notation registry](/notation.md): batch-4 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2013-arXiv-Dumbser-1048550arXiv12123585.pdf` (arXiv:1212.3585v3, 10 March 2015; author preprint of the published J. Comput. Phys. 248:257–286 (2013), doi:10.1016/j.jcp.2013.04.017, checked on Crossref): text extraction, all sections. The section numbering of the numerical tests is not legible in the text layer, so tests are cited as §4. The refinement estimator (eq. 45) and the vortex-pair formulas are not reproduced. Reference list: 107 entries.
