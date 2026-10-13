---
type: Source
title: "Titarev & Toro (2004) — Finite-volume WENO schemes for three-dimensional conservation laws"
description: "Extends finite-volume WENO to 3D and to fifth and seventh order by dimension-by-dimension sweeps to two-point Gauss quadratures (with the needed Gauss-point linear weights), and replaces the Rusanov flux by HLLC and the Riemann-solver-free MUSTA flux."
resource: "doi:10.1016/j.jcp.2004.05.015"
source_kind: paper
authors: [Titarev V.A., Toro E.F.]
year: 2004
venue: "J. Comput. Phys. 201:238-260"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2004-JCP-Titarev-101016jjcp200405015.pdf"
tags: [weno, finite-volume, 3d, riemann-solver, hllc, musta]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Two improvements to FV-WENO: a complete 3D, dimension-by-dimension
recipe at fifth ($r = 3$) and seventh ($r = 4$) order, with the
Gauss-point linear weights needed for the transverse sweeps; and more
accurate interface fluxes (HLLC, MUSTA) in place of Rusanov. Merged
into [finite-volume reconstruction](/methods/finite-volume-reconstruction.md)
and the new [approximate Riemann solvers](/methods/approximate-riemann-solvers.md),
with benchmark updates.

# Key claims

1. **Framework** (§2): tensor $N$-point Gauss rule on faces; RK3; CFL
   bounds 1 (1D), 1/2 (2D, as unsplit Godunov) and 1/3 (3D, numerical
   experiments); eqs. (9)–(12) checked on the page image.
2. **Reconstruction** (§3): x-sweep to face averages, then y and z sweeps
   to Gauss points; Gauss-point weights for $r = 3$
   ($\frac{210\mp\sqrt3}{1080}$, $\frac{11}{18}$, $\frac{210\pm\sqrt3}{1080}$)
   and $r = 4$; two-point Gauss is best for cost/accuracy. Reconstruction
   is always characteristic, with order reduction to minmod MUSCL when
   two close discontinuities leave no smooth stencil.
3. **Fluxes** (§4): HLLC (all waves, no linearization, robust at low
   density and sonic points); MUSTA with a FORCE predictor and $k = 2$
   stages, needing no eigenstructure.
4. **Tests** (§5): a long-time modified Shu–Osher problem and the 2D/3D
   vortex (HLLC and MUSTA about twice as accurate as Shi–Hu–Shu's
   Rusanov-based scheme); DMR at three meshes; 3D spherical explosion.
   Accuracy tests run at a fixed CFL, not $\Delta t \propto h^{5/3}$.
5. **Cost** (§5.5): equal to Shi–Hu–Shu in 2D, cheaper in 3D (fewer
   Gauss points); FV is about three times FD's cost in 2D, but runs on
   unstructured meshes and, with MUSTA, without eigenvectors.

# Notation map

| Titarev & Toro (2004) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf Q$, $\mathbf F, \mathbf G, \mathbf H$ | $u$, $\mathbf f$ components | |
| $Q^L_{i+1/2}$, $Q^R_{i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | |
| $S_0, S_1, S_2$ | stencils written explicitly | $S_0$ is the rightmost here |
| $d_l$, $\omega_l$, $\beta_l$, $e$ | $d_k$, $\omega_k$, $\beta_k$, $\varepsilon$ | |
| $C_{cfl}$ | $\nu$ | |
| $\Delta x, \Delta y, \Delta z$ | $h_x, h_y, h_z$ | |
| $S_L, S_*, S_R$ | $S_L, S_M, S_R$ | HLLC speeds |

# Pages created or updated

* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md).
* Created [Isentropic vortex advection (smooth accuracy test)](/benchmarks/isentropic-vortex.md).
* Updated [Shu–Osher shock/entropy-wave interaction](/benchmarks/shu-osher-problem.md).
* Created [Approximate Riemann solvers as building blocks of capturing schemes](/methods/approximate-riemann-solvers.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Conservative finite-difference (flux) formulation](/methods/conservative-finite-difference.md).
* Updated [Reconstruction from cell averages](/methods/finite-volume-reconstruction.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [Notation registry](/notation.md): batch-3 registry extensions.
* Also cited on [HLLC Riemann solver](/methods/hllc-riemann-solver.md) (created in batch 12).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2004-JCP-Titarev-101016jjcp200405015.pdf` (doi:10.1016/j.jcp.2004.05.015; typeset article): text extraction, all sections; eqs. (9)–(12) and (19)–(31) read from the page images (pp. 241, 243–244). The $r = 4$ weights and the HLLC star-state formulas are not reproduced. Reference list: 24 entries.
