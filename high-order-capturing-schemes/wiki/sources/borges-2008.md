---
type: Source
title: "Borges, Carmona, Costa & Don (2008) — An improved weighted essentially non-oscillatory scheme for hyperbolic conservation laws"
description: "WENO-Z: weights from a global fifth-order indicator τ₅ = |β₀ − β₂|, fourth order at first-order critical points (fifth with q = 2), and the argument that WENO-M and WENO-Z beat WENO-JS at shocks through larger weights on discontinuous stencils, at WENO-JS cost."
resource: "doi:10.1016/j.jcp.2007.11.038"
source_kind: paper
authors: [Borges R., Carmona M., Costa B., Don W.S.]
year: 2008
venue: "J. Comput. Phys. 227:3191-3211"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2008-JCP-Borges-101016jjcp200711038.pdf"
tags: [weno, weno-z, nonlinear-weights, dissipation]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Instead of mapping the weights, improve them with information already in
WENO-JS: the difference of the two outer indicators is a higher-order
measure of smoothness over the whole stencil. The resulting WENO-Z is as
sharp as WENO-M, 25 % cheaper, and the paper argues that the sharpness of
both comes from the weights they give discontinuous stencils, not from
critical-point accuracy. Merged into [WENO-Z](/methods/weno-z.md),
[mapped WENO](/methods/mapped-weno.md) and the critical-point and
weight-condition pages.

# Key claims

1. **Review** (§2): WENO-JS and WENO-M, Henrick's conditions, the mapping
   properties; WENO-JS second order when $f''$ also vanishes.
2. **WENO-Z** (§3, eqs. 25–28): $\tau_5$, normalized indicators, weights;
   $\omega - d = O(h^3)$ away from critical points.
3. **Discontinuous stencils** get weights around $10^{-4}$ (WENO-Z)
   versus $10^{-8}$ (WENO-JS), WENO-M slightly above JS (Fig. 3).
4. **Critical points** (§4): order $\min(5, s_1 + 2, s_2 + 3)$; 4 at
   $n_{\mathrm{cp}} = 1$; $q = 2$ (eq. 42) gives 5 but more dissipation.
5. **Tests** (§5, $\varepsilon = 10^{-6}$ for JS, $10^{-40}$ for M and Z,
   CFL 0.4, RK3): composite advection, Sod, Lax, 123, Shu–Osher
   ($k = 5, 10$), blast waves, Mach 3 shock–vortex, Mach 4.46
   Richtmyer–Meshkov; CPU per step (Tables 5–6).

# Notation map

| Borges et al. (2008) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tau_5$ | $\tau_5$ | |
| $\beta^z_k$ | normalized indicator $(\beta_k + \varepsilon)/(\beta_k + \tau_5 + \varepsilon)$ | |
| $\alpha^z_k$, $\omega^z_k$ | $\tilde\omega_k$, $\omega_k$ | |
| $q$ (eq. 42) | $q$ | |
| $d_0 = 3/10, d_1 = 3/5, d_2 = 1/10$ | $d_k$ | **reversed** stencil order relative to Jiang–Shu |
| $n_{cp}$ | $n_{\mathrm{cp}}$ | |

# Pages created or updated

* Updated [Composite-profile linear advection (Jiang–Shu test)](/benchmarks/composite-advection-profile.md).
* Updated [Woodward–Colella interacting blast waves](/benchmarks/interacting-blast-waves.md).
* Updated [Lax shock tube](/benchmarks/lax-shock-tube.md).
* Updated [Shock–vortex interaction](/benchmarks/shock-vortex-interaction.md).
* Updated [Shu–Osher shock/entropy-wave interaction](/benchmarks/shu-osher-problem.md).
* Updated [Sod shock tube](/benchmarks/sod-shock-tube.md).
* Updated [Smoothness indicator](/definitions/smoothness-indicator.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Mapped WENO (WENO-M)](/methods/mapped-weno.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Created [WENO-Z](/methods/weno-z.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [Accuracy at critical points](/properties/accuracy-at-critical-points.md).
* Updated [Accuracy conditions on WENO nonlinear weights](/results/weno-weight-accuracy-conditions.md).
* Updated [Notation registry](/notation.md): batch-2 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2008-JCP-Borges-101016jjcp200711038.pdf` (doi:10.1016/j.jcp.2007.11.038): text extraction, all sections; eqs. (24)–(27), (38)–(42) and Table 1 read from page images (pp. 3196, 3200). Reference list: 8 entries.
