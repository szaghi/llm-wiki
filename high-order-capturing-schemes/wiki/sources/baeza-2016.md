---
type: Source
title: "Baeza, Mulet & Zorío (2016) — High order weighted extrapolation for boundary conditions for finite difference methods on complex domains with Cartesian meshes"
description: "Ghost-cell values for fifth-order FD-WENO on Cartesian meshes of complex domains by extrapolation along boundary normals with dimensionless, scale-independent weights that reduce to the nearest value across discontinuities, blended with least squares (WLS-GAW) to remove the mild instability of Lagrange extrapolation."
resource: "doi:10.1007/s10915-016-0188-7"
source_kind: paper
authors: [Baeza A., Mulet P., Zorío D.]
year: 2016
venue: "J. Sci. Comput. 69:170-200"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2016-JSC-Baeza-101007s10915-016-0188-7.pdf"
tags: [boundary-treatment, weno, finite-difference, cut-cell]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper improves the authors' earlier thresholded node-selection
extrapolation (Baeza et al., J. Sci. Comput. 66, 2016) with fully
weighted designs. Several weight families are compared, and least
squares stabilizes complex domains. Merged into the new
[weighted extrapolation](/methods/weighted-extrapolation.md) page and
into the ILW, finite-difference, smoothness-indicator and benchmark
pages.

# Key claims

1. **Scheme** (§2): Shu–Osher FD with WENO5, Donat–Marquina splitting
   and RK3-TVD.
2. **Meshing and normals** (§3): ghost cells within $k$ cells of each
   mesh line. Nodes on the normal come from 1D interpolation, and
   Dirichlet stencils are re-spaced to start at the boundary point. Node
   spacing of at least $h$ was stable for high order.
3. **Weighted extrapolation** (§4.1): a nested recurrence that raises
   the degree only while the stencil looks smooth.
4. **Weight designs** (§§4.2–4.5): simple weights fail by taking data
   from the wrong side (counter-example $x^2 \mid 1$; Table 1). Improved
   weights recover third order (Table 2), and a data-based floor handles
   vanishing derivatives (Tables 3–4). The single weight comes in a tuned
   form with an exponential map, and the global average weight uses a
   harmonic/arithmetic mean ratio, proved in $[0, 1]$. All weights are
   dimensionless and scale-independent, unlike those of Tan and Shu's
   ILW work.
5. **Least squares** (§4.6): Lagrange extrapolation can be mildly
   unstable on complex 2D domains (also stated by Tan and Shu). WLS
   blends a degree-4 least-squares fit on 9 nodes with the nearest value.
6. **Tests** (§5): fifth order on advection and Burgers; Burgers shock
   hitting the inflow; interacting blasts; 2D advection on a square
   and on a complex domain, where Lagrange is unstable and WLS stable; a
   Mach 10 shock on a triangle (§5.2.3, "Double Mach Reflection");
   multiple cylinders; supersonic triangle. WLS-GAW is the recommended
   variant (§6).

# Notation map

| Baeza et al. (2016) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x^*$, $u^{(k)}_*$ | $x^{\mathrm g}$, $\breve u_k$ | registry $u^{(i)}$ is a Runge–Kutta stage |
| $\omega_k$, $\omega$ | $\omega^{\mathrm{ext}}_k$, $\omega^{\mathrm{ext}}$ | |
| $I_k$, $IS_k$, $IM_k$ | stencil-wide indicators | words on concept pages |
| $\lambda$ (tuned UW) | $\lambda_{\mathrm{UW}}$ | |
| $h_x$, $h_y$ | $h_x$, $h_y$ | |
| $r$, $R$, $r_0$, $s_1$, $s_2$, $m$ | (words) | degrees, stencil sizes, exponents |

# Pages created or updated

* Updated [Conservative finite-difference (flux) formulation](/methods/conservative-finite-difference.md).
* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md).
* Created [Inverse Lax–Wendroff numerical boundary treatment](/methods/inverse-lax-wendroff.md).
* Updated [Smoothness indicator](/definitions/smoothness-indicator.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Created [Weighted (WENO-type) extrapolation for ghost values](/methods/weighted-extrapolation.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [Woodward–Colella interacting blast waves](/benchmarks/interacting-blast-waves.md).
* Updated [Notation registry](/notation.md): batch-4 registry extensions.
* Also cited on [Self-similarity (scale invariance) of capturing schemes](/properties/self-similarity.md).
* Also cited on [Navier–Stokes characteristic boundary conditions](/methods/characteristic-boundary-conditions.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2016-JSC-Baeza-101007s10915-016-0188-7.pdf` (accepted manuscript, arXiv:2501.17106v1, 28 January 2025, not the version of record; published as J. Sci. Comput. 69:170–200 (2016), doi:10.1007/s10915-016-0188-7, checked on Crossref): text extraction, all sections. The weight formulas of §§4.2–4.5 are only partly legible in the text layer and are described, not reproduced. Reference list: 13 entries. Its first entry is a different Baeza, Mulet & Zorío paper of 2016 (J. Sci. Comput. 66:761), keyed `baeza-2016-b`.
