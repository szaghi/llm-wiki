---
type: Source
title: "Harten, Engquist, Osher & Chakravarthy (1987) — Uniformly high order accurate essentially non-oscillatory schemes, III"
description: "The arbitrary-order ENO paper: adaptive-stencil reconstruction from cell averages (via primitive function or deconvolution), the abstract reconstruct–evolve–average scheme with Cauchy–Kowalewski solution in the small, characteristic-wise extension to systems, and Euler tests."
resource: "doi:10.1016/0021-9991(87)90031-3"
source_kind: paper
authors: [Harten A., Engquist B., Osher S., Chakravarthy S.R.]
year: 1987
venue: "J. Comput. Phys. 71:231-303"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1987-JCP-Harten-1010160021-99918790031-3.pdf"
tags: [eno, reconstruction, finite-volume, systems, euler]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The third paper of the ENO series (after Harten–Osher, second order,
and a constant-coefficient stability study) and the one that defines
ENO schemes of any order. It generalizes Godunov's scheme: reconstruct
an $r$-th order piecewise polynomial from cell averages with an adaptive
stencil, evolve it exactly (approximated by a local Taylor expansion and
a Riemann solver), and average. The weakened stability notion —
essentially non-oscillatory instead of TVD — is what allows uniform
high order. Merged into [ENO](/methods/eno-reconstruction.md),
[essentially non-oscillatory](/definitions/essentially-non-oscillatory.md),
[finite-volume reconstruction](/methods/finite-volume-reconstruction.md)
and [characteristic decomposition](/methods/characteristic-decomposition.md).

# Key claims

1. **Accuracy in cell-average sense** (§1): local truncation
   $O(h^{r+1})$ in cell averages if the numerical flux has error
   $d(x)h^r$ with $d$ Lipschitz; where it is not (stencil turns at
   critical points), the scheme is "$r$th order accurate" ($r$ in $L_1$,
   $r-1$ in max norm).
2. **ENO reconstruction** (§3): requirements (1.9a–c), including
   $TV(R) \le TV(w) + O(h^r)$; RP (primitive function) and RD
   (deconvolution); stencil growth by smaller divided difference.
3. **TVD is first order at extrema; strict non-oscillation limits the
   order to 2** (§2), hence the essentially non-oscillatory notion.
4. **Solution in the small** (§4): Cauchy–Kowalewski in time, quadrature
   of the flux, Riemann solver as a pointer; Roe flux adequate with an
   entropy fix; the Riemann solver's importance decreases with order.
5. **Systems** (§§5–6): characteristic-wise reconstruction needed
   because discontinuities collide; Euler implementation with Roe
   average.
6. **Experiments** (§7): Burgers-type smooth and Riemann data, non-convex
   fluxes; Sod and Lax shock tubes (component-wise noise, characteristic
   cure); interacting blast waves with a local positivity order
   reduction; semi-discrete RK version (CFL ≤ 0.5); non-uniform and
   adaptive grids; outline of 2D via genuine 2D reconstruction
   (Strang splitting being only second order).

# Notation map

| Harten et al. (1987) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar w_j$, $\bar u_j^n$ | $\bar u_i$ | cell averages |
| $W(x)$ | $\mathcal{U}(x)$ | primitive function |
| $H_m(x; w)$ | ENO interpolant | |
| $R(x; \bar w)$ | reconstruction $p_i$ on each cell | |
| $\bar f_{j+1/2}$ | $\hat f_{i+1/2}$ | numerical flux |
| $f^R$, $f^{\mathrm{Roe}}$ | exact / Roe monotone flux | [monotone flux](/definitions/monotone-flux.md) |
| $r$ | order (degree $r-1$) | same role as $k$ in Shu (1998) |
| $\lambda = \tau/h$ | $\Delta t/h$ | |
| RP, RD | reconstruction via primitive / deconvolution | |

# Pages created or updated

* Created [Woodward–Colella interacting blast waves](/benchmarks/interacting-blast-waves.md).
* Created [Lax shock tube](/benchmarks/lax-shock-tube.md).
* Created [Sod shock tube](/benchmarks/sod-shock-tube.md).
* Created [Essentially non-oscillatory (ENO property)](/definitions/essentially-non-oscillatory.md).
* Created [Monotone numerical flux](/definitions/monotone-flux.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Created [ENO reconstruction and schemes](/methods/eno-reconstruction.md).
* Created [Reconstruction from cell averages](/methods/finite-volume-reconstruction.md).
* Created [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Created [Accuracy at critical points](/properties/accuracy-at-critical-points.md).
* Created [Total variation diminishing (TVD) and bounded (TVB)](/properties/total-variation-diminishing.md).
* Updated [Notation registry](/notation.md): batch-1 registry extensions.
* Also cited on [Lax–Wendroff (Taylor) single-step time discretization](/methods/taylor-time-discretization.md).
* Also cited on [Burgers equation: shock formation](/benchmarks/burgers-shock-formation.md) (created 2026-10-13).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/1987-JCP-Harten-1010160021-99918790031-3.pdf` (doi:10.1016/0021-9991(87)90031-3): text extraction (heavily garbled OCR layer, 73 pages), all sections read, plus page images of pp. 233–234 for eqs. (1.7)–(1.12). Reference list (32 entries) transcribed from page images. Equations of §§4–6 and the Appendix are described, not reproduced.
