---
type: Source
title: "Zanotti, Fambri, Dumbser & Hidalgo (2015) — Space–time adaptive ADER discontinuous Galerkin finite element schemes with a posteriori sub-cell finite volume limiting"
description: "Combines ADER-DG with the a posteriori ADER-WENO subcell limiter on cell-by-cell space–time adaptive Cartesian meshes, extending projection and averaging to the subcell data, and shows design order to N = 8 and very low dissipation on Euler and GLM-MHD problems in 2D and 3D."
resource: "doi:10.1016/j.compfluid.2015.06.020"
source_kind: paper
authors: [Zanotti O., Fambri F., Dumbser M., Hidalgo A.]
year: 2015
venue: "Comput. Fluids 118:204-224"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2015-CompFluids-Zanotti-101016jcompfluid201506020.pdf"
tags: [dg, ader, amr, limiter, a-posteriori]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper brings together the 2014 subcell limiter and the 2013 AMR
framework. AMR follows flow features, and the limiter handles
discontinuities at the finest level. Merged into the
[a posteriori subcell limiting](/methods/a-posteriori-subcell-limiting.md),
[high-order AMR](/methods/high-order-amr.md) and [ADER](/methods/ader.md)
pages and into several benchmarks.

# Key claims

1. **Context** (§1): the explicit DG time step is
   $h/[d(2N + 1)\vert\lambda_{\max}\vert]$. RKDG reaches at most fourth
   order in time and in practice third. ADER via the local space–time DG
   predictor removes Cauchy–Kowalewski algebra and handles stiff sources.
2. **Limiter recap** (§4): PAD and a relaxed DMP with
   $\delta = \max\left(\delta_0, \epsilon(\max - \min)\right)$,
   $\delta_0 = 10^{-4}$, $\epsilon = 10^{-3}$, "as recommended in [53]"
   (eq. 17). [53] is Dumbser et al. 2014, whose arXiv version, read for
   this bundle, prints no $\delta_0$. The paper argues that $N_s = 2N + 1$
   is optimal, not heuristic.
3. **AMR coupling** (§5.2): virtual children inherit limiter status, a
   mother is troubled if any active child is, and troubled cells cannot
   be recoarsened. Subcell data are projected to finer levels by WENO
   reconstruction and averaged to coarser levels.
4. **Refinement** (§5.1): a Löhner-type estimator with thresholds as
   in the 2013 paper, plus forced refinement one or two cells ahead of
   discontinuities.
5. **Tests** (§6): isentropic vortex, $N = 2$–$8$, at design order;
   Sod and Lax with $N = 9$, limiter overhead about 1.5 with 15% of cells
   limited ($N = 2$); double Mach reflection, $N = 2, 5, 8$; forward step;
   four 2D Riemann problems with Kelvin–Helmholtz structures; 2D
   ($N = 9$) and 3D explosions; MHD rotor and Orszag–Tang ($N = 5$, GLM
   cleaning).
6. **Claim** (§7): the authors place the method in "a new generation of
   shock capturing schemes".

# Notation map

| Zanotti et al. (2015) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $N$, $\mathbf u_h$, $\mathbf q_h$ | $K$, $\mathcal{P}_i$, $u^{\mathrm p}_i$ | |
| $\beta$ (limiter status) | $\mathcal{B}_i$ | |
| $N_s$, $\mathbf v_h$ | $N_{\mathrm s}$, subcell averages $\bar v_{i,m}$ | |
| $\delta$, $\delta_0$, $\epsilon$ | $\delta_{\mathrm{DMP}}$, $\delta_0$, $\epsilon_{\mathrm{DMP}}$ | |
| $r$, $\ell_{\max}$ | $r_{\mathrm{AMR}}$, $N_{\mathrm{lev}}$ | |
| $\sigma$ (cell status) | (words) | |
| $\Phi$, $c_h$ | GLM scalar, cleaning speed | |

# Pages created or updated

* Created [A posteriori subcell finite-volume limiting (MOOD paradigm)](/methods/a-posteriori-subcell-limiting.md).
* Created [ADER one-step schemes (arbitrary high order using derivatives)](/methods/ader.md).
* Updated [Approximate Riemann solvers as building blocks of capturing schemes](/methods/approximate-riemann-solvers.md).
* Updated [Constrained transport for high-order capturing schemes (MHD)](/methods/constrained-transport.md).
* Created [Cylindrical and spherical explosion problem](/benchmarks/multidimensional-explosion.md).
* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md).
* Created [High-order adaptive mesh refinement for capturing schemes](/methods/high-order-amr.md).
* Updated [Isentropic vortex advection (smooth accuracy test)](/benchmarks/isentropic-vortex.md).
* Updated [Lax shock tube](/benchmarks/lax-shock-tube.md).
* Updated [Lax–Wendroff (Taylor) single-step time discretization](/methods/taylor-time-discretization.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Mach 3 wind tunnel with a forward-facing step](/benchmarks/forward-facing-step.md).
* Updated [MHD rotor](/benchmarks/mhd-rotor.md).
* Updated [Order barriers and optimal coefficients of SSP time discretizations](/results/ssp-order-barriers.md).
* Updated [Orszag–Tang vortex (2D MHD)](/benchmarks/orszag-tang-vortex.md).
* Updated [Sod shock tube](/benchmarks/sod-shock-tube.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Created [Two-dimensional Riemann problems (four-quadrant configurations)](/benchmarks/two-dimensional-riemann-problems.md).
* Updated [Notation registry](/notation.md): batch-4 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2015-CompFluids-Zanotti-101016jcompfluid201506020.pdf` (arXiv:1412.0081v2, 1 September 2015, despite the journal-style filename; preprint of Comput. Fluids 118:204–224 (2015), doi:10.1016/j.compfluid.2015.06.020, checked on Crossref; `pdftotext` reports a damaged xref table but extracts all pages): text extraction, all sections; eq. 17 read from the page image (p. 7). The 2D Riemann-problem table and the rotor and blast initial data are not reproduced. The 3D explosion is run with $N = 3$ according to the text and $N = 5$ according to the caption of Fig. 11. Reference list: 128 entries.
