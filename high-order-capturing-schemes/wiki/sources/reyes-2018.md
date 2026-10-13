---
type: Source
title: "Reyes, Lee, Graziani & Tzeferacos (2018) — A new class of high-order methods for fluid dynamics simulations using Gaussian process modeling: one-dimensional case"
description: "Gaussian-process interpolation and reconstruction from cell averages with a squared-exponential kernel, and GP-WENO with RKHS-norm smoothness indicators; order 2R+1 on 2R+1 cells, a tunable length scale, tested on 1D Euler and MHD."
resource: "doi:10.1007/s10915-017-0625-2"
source_kind: paper
authors: [Reyes A., Lee D., Graziani C., Tzeferacos P.]
year: 2018
venue: "J. Sci. Comput. 76:443-480"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2018-JSC-Reyes-101007s10915-017-0625-2.pdf"
tags: [weno, gaussian-process, non-polynomial, finite-volume, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

A non-polynomial reconstruction for FV schemes based on GP regression,
made non-oscillatory by WENO weighting with new GP smoothness
indicators. Published online 6 Dec 2017 in volume 76 (2018), so the
slug carries the issue year (bundle law). Merged into the new
[GP-WENO](/methods/gp-weno.md) page and into the smoothness-indicator
and benchmark pages.

# Key claims

1. **GP prediction** (§2.1): posterior mean $\bar f + \mathbf k_*^{T}\mathbf K^{-1}(\mathbf f - \bar{\mathbf f})$;
   data-independent weights; this differs from RBF, which is parametric.
2. **Reconstruction** (§2.3): integrated covariances for cell-average
   data, closed-form for the SE kernel; isotropic multi-D stencils are
   possible.
3. **GP-WENO** (§2.5): $R+1$ sub-stencils; least-squares optimal weights;
   Jiang–Shu weights with $q = 1$, $\varepsilon = 10^{-36}$; RKHS-norm
   indicators, equal to minus twice the log likelihood up to a constant.
   No accuracy proof is given.
4. **Conditioning** (§§3, 5.2): weights precomputed in quadruple
   precision; double precision plateaus near $10^{-7}$.
5. **Results** (§5): order $2R+1$ for $R = 1$–$5$; GP-R2 30% and GP-R3 60%
   faster than WENO-JS to a given error; $\ell$ near the feature size
   minimizes error; Shu–Osher, Sod, Einfeldt, Brio–Wu, Ryu–Jones; GP-R1
   oscillates most at shocks.

# Notation map

| Reyes et al. (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $K(x, y)$, $\ell$, $\Sigma^2$ | $\mathcal{K}(x, y)$, $\ell$, $\Sigma^2$ | |
| $\mathbf K$, $\mathbf C$, $\mathbf T_*$, $\mathbf z$ | $\boldsymbol{\mathcal K}$, $\mathbf C$, $\mathbf t_*$, $\mathbf z$ | |
| $\lambda^m_i$, $\mathbf v^m_i$, $\alpha^m_i$ | $\mu^{(k)}_i$, $\mathbf e^{(k)}_i$, $c^{(k)}_i$ | registry $\lambda$ is a Jacobian eigenvalue |
| $R$ (stencil radius) | $R$ | $R = r - 1$ |
| $S_m$, $\gamma_m$, $\omega_m$, $\beta_m$ | $S_k$, $d_k$, $\omega_k$, $\beta_k$ | $m = 1, \dots, R+1$ |
| $p$ (weight power) | $q$ | $q = 1$ here |
| $\epsilon$ | $\varepsilon$ | |
| $\langle q\rangle_i$ | $\bar u_i$ | |
| $\Delta$ | $h$ | |
| $C_{cfl}$ | $\nu$ | |

# Pages created or updated

* Updated [Double-rarefaction (near-vacuum) Riemann problems](/benchmarks/double-rarefaction.md).
* Updated [Shu–Osher shock/entropy-wave interaction](/benchmarks/shu-osher-problem.md).
* Updated [Sod shock tube](/benchmarks/sod-shock-tube.md).
* Updated [Smoothness indicator](/definitions/smoothness-indicator.md).
* Updated [Approximate Riemann solvers as building blocks of capturing schemes](/methods/approximate-riemann-solvers.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Reconstruction from cell averages](/methods/finite-volume-reconstruction.md).
* Created [Gaussian-process reconstruction and GP-WENO](/methods/gp-weno.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [Notation registry](/notation.md): batch-3 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2018-JSC-Reyes-101007s10915-017-0625-2.pdf` (doi:10.1007/s10915-017-0625-2; open-access typeset article): text extraction, all sections and Appendices A–D; eqs. (1)–(3), (24)–(35) and (42) read from the page images (pp. 446, 454–456). Reference list: 73 entries.
