---
type: Source
title: "Dumbser, Zanotti, Loubère & Diot (2014) — A posteriori subcell limiting of the discontinuous Galerkin finite element method for hyperbolic conservation laws"
description: "Extends the a posteriori MOOD paradigm to ADER-DG: an unlimited candidate is tested for positivity and a relaxed polynomial discrete maximum principle, and failed cells are recomputed from the previous time level by third-order ADER-WENO on 2N+1 subcells per direction, which matches the DG time step and keeps subcell resolution up to tenth order."
resource: "doi:10.1016/j.jcp.2014.08.009"
source_kind: paper
authors: [Dumbser M., Zanotti O., Loubère R., Diot S.]
year: 2014
venue: "J. Comput. Phys. 278:47-75"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2014-JCP-Dumbser-101016jjcp201408009.pdf"
tags: [dg, limiter, a-posteriori, ader, weno]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper turns MOOD's order decrementing into a change of scheme and
of mesh. Troubled DG cells are recomputed with a robust finite-volume
scheme on a fine subgrid and gathered back, so that shocks occupy a
subcell rather than a DG cell. It also reviews a priori DG limiters.
Merged into the new [a posteriori subcell limiting](/methods/a-posteriori-subcell-limiting.md)
page and into the [ADER](/methods/ader.md), [WENO-limited DG](/methods/weno-limited-dg.md)
and positivity pages and eight benchmarks.

# Key claims

1. **DG background** (§§1–2): the cell entropy inequality gives $L^2$
   stability for any degree, yet DG still needs limiting (Godunov's
   theorem). The CFL limit is about $1/(2N + 1)$ (eq. 17).
   Unlimited ADER-DG reaches order $N + 1$.
2. **Review** (§3.1): three a priori families, namely artificial
   viscosity, slope/moment limiters and (H)WENO limiters. WENO limiters
   partly lose subcell resolution, and detection parameters are
   problem-dependent.
3. **Detection** (§4.3): PAD (positivity) and NAD (relaxed DMP over the
   cell and its Voronoi neighbours, eq. 23), with
   $\delta = \epsilon(\max - \min)$, $\epsilon = 10^{-3}$ (eq. 24),
   evaluated on subcell averages (eq. 25). Information from two time
   levels is used.
4. **Subcell representation** (§4.2): projection $\mathcal{P}$ and
   least-squares reconstruction $\mathcal{R}$ with
   $\mathcal{R}\circ\mathcal{P} = I$ for $N_s \ge N + 1$.
5. **Recompute** (§4.3): third-order ADER-WENO on the subgrid, chosen
   over TVD so that physical extrema are not clipped. Neighbouring
   unlimited cells are flux-corrected on sub-faces.
6. **Optimal $N_s = 2N + 1$** (§4.5, eq. 29): it matches the subgrid
   finite-volume time step to the DG step, and ADER-FV errors carry
   $(1 - \mathrm{CFL})$.
7. **Tests** (§5): Sod and Lax with $N = 9$ on $20\times5$ cells;
   isentropic vortex convergence for $N = 2$–$9$; Shu–Osher on $40\times5$;
   double Mach reflection with $N = 1, 2, 5, 9$, where fewer cells are
   flagged at higher $N$; forward step; five 2D Riemann problems, with
   Kelvin–Helmholtz roll-up confirmed by sixth-order AMR; shock–vortex;
   3D explosion with $10^{10}$ space–time DOF on 8000 cores.
8. **Outlook** (§6): a further MOOD layer (TVD or first order) if
   WENO3 fails positivity, unstructured meshes, and MHD/RMHD.

# Notation map

| Dumbser et al. (2014) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $N$ (DG degree), $\mathbf u_h$ | $K$, $\mathcal{P}_i$ | |
| $\mathbf q_h$ | $u^{\mathrm p}_i$ | space–time predictor |
| $N_s$, $\mathbf v_h$, $v_{i,j}$ | $N_{\mathrm s}$, subcell field, $\bar v_{i,m}$ | |
| $\mathcal{P}$, $\mathcal{R}$ | $\Pi$, $\mathcal{R}$ | registry $\mathcal{P}_i$ is the cell polynomial |
| $\beta_i$ (limiter status) | $\mathcal{B}_i$ | registry $\beta_k$ is the smoothness indicator |
| $\delta$, $\epsilon$ | $\delta_{\mathrm{DMP}}$, $\epsilon_{\mathrm{DMP}}$ | |
| $\mathcal{V}_i$ | $V_i$ | |
| $\vert\lambda_{\max}\vert$, $d$ | $\vert\lambda_{\max}\vert$, $d$ | |

# Pages created or updated

* Created [A posteriori subcell finite-volume limiting (MOOD paradigm)](/methods/a-posteriori-subcell-limiting.md).
* Created [ADER one-step schemes (arbitrary high order using derivatives)](/methods/ader.md).
* Updated [Approximate Riemann solvers as building blocks of capturing schemes](/methods/approximate-riemann-solvers.md).
* Created [Cylindrical and spherical explosion problem](/benchmarks/multidimensional-explosion.md).
* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md).
* Updated [Isentropic vortex advection (smooth accuracy test)](/benchmarks/isentropic-vortex.md).
* Updated [Lax shock tube](/benchmarks/lax-shock-tube.md).
* Updated [Mach 3 wind tunnel with a forward-facing step](/benchmarks/forward-facing-step.md).
* Updated [Positivity preservation (invariance of the admissible set)](/properties/positivity-preserving.md).
* Updated [Shock–vortex interaction](/benchmarks/shock-vortex-interaction.md).
* Updated [Shu–Osher shock/entropy-wave interaction](/benchmarks/shu-osher-problem.md).
* Updated [Sod shock tube](/benchmarks/sod-shock-tube.md).
* Created [Two-dimensional Riemann problems (four-quadrant configurations)](/benchmarks/two-dimensional-riemann-problems.md).
* Created [WENO limiters for discontinuous Galerkin schemes](/methods/weno-limited-dg.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [Notation registry](/notation.md): batch-4 registry extensions.
* Also cited on [Hermite WENO](/methods/hermite-weno.md) (created 2026-10-13).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2014-JCP-Dumbser-101016jjcp201408009.pdf` (arXiv:1406.7416v3, 10 March 2015, despite the journal-style filename; preprint of J. Comput. Phys. 278:47–75 (2014), doi:10.1016/j.jcp.2014.08.009, checked on Crossref): text extraction, all sections; eqs. 15–17, 23–25 and 29 read from the page images (pp. 6, 12, 16). The 2D Riemann-problem states (Table 3) and the vortex formulas are not reproduced. Section 5.3 prints the Shu–Osher pre-shock density as $1 + 0.2\sin(5\pi x)$ and the final time as 0.18, recorded as printed. Reference list: 118 entries.
