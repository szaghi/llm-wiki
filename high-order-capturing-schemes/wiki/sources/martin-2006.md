---
type: Source
title: "Martín, Taylor, Wu & Weirs (2006) — A bandwidth-optimized WENO scheme for the effective direct numerical simulation of compressible turbulence"
description: "WENO-SYM: a downwind candidate stencil makes the set symmetric; the optimal weights are order-optimized (WENO-SYMOO, non-dissipative, unstable at contacts) or bandwidth-optimized (WENO-SYMBO); validated on canonical problems, isotropic turbulence and a supersonic boundary layer."
resource: "doi:10.1016/j.jcp.2006.05.009"
source_kind: paper
authors: [Martín M.P., Taylor E.M., Wu M., Weirs V.G.]
year: 2006
venue: "J. Comput. Phys. 220:270-289"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2006-JCP-Martin-101016jjcp200605009.pdf"
tags: [weno, low-dissipation, turbulence, spectral-resolution]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Targets the dissipation of the WENO-JS optimal stencil for "effective"
DNS (all turbulent scales resolved, shocks not). Adding a downwind
candidate makes the stencil set symmetric; the optimal weights are then
chosen for maximum order or for bandwidth by minimizing a spectral error
integral. Merged into [bandwidth-optimized WENO](/methods/bandwidth-optimized-weno.md)
and [modified wavenumber](/definitions/modified-wavenumber.md).

# Key claims

1. Two dissipation sources: adaptation and the optimal stencil (§1).
2. **WENO-SYM** (§4): $r + 1$ candidates; the downwind weight capped below
   the smallest upwind weight.
3. **SYMOO**: order $2r$, zero dissipation, unstable near contacts.
   **SYMBO**: bandwidth index 0.49 vs 0.35 ($r = 3$), 0.56 vs 0.42 ($r = 4$);
   parameters by trial and error.
4. **Tests** (§§5–7; $\varepsilon = 10^{-10}$, $q = 1$ unless stated): wave
   advection, shock tube, Shu–Osher and variants, decaying isotropic
   turbulence ($M_t = 0.1$ vs Padé; $M_t = 1.5$), Mach 2.32 boundary layer.
5. Shock-capturing error is first order and propagates downstream; the
   nonlinear part is not optimized (§8).

# Notation map

| Martín et al. (2006) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q^r_k$, $a^r_{kl}$ | $q_k$, coefficients | |
| $C^r_k$, $\tilde C^r_k$ | $d_k$ (order- and bandwidth-optimized) | |
| $IS_k$ | $\beta_k$ | |
| $\kappa$, $\tilde\kappa$ | $\xi$, $\tilde\xi$ | scaled and modified wavenumber |
| $\Delta$ | $h$ | |
| $p$, $\epsilon$ | $q$, $\varepsilon$ | |

# Pages created or updated

* Updated [Shu–Osher shock/entropy-wave interaction](/benchmarks/shu-osher-problem.md).
* Updated [Sod shock tube](/benchmarks/sod-shock-tube.md).
* Updated [Modified wavenumber (dispersion and dissipation analysis)](/definitions/modified-wavenumber.md).
* Created [Symmetric and bandwidth-optimized WENO (WENO-SYMOO, WENO-SYMBO)](/methods/bandwidth-optimized-weno.md).
* Created [Central-upwind WENO (WENO-CU6)](/methods/central-upwind-weno.md).
* Updated [Hybrid compact-WENO schemes](/methods/hybrid-compact-weno.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [Notation registry](/notation.md): batch-2 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2006-JCP-Martin-101016jjcp200605009.pdf` (doi:10.1016/j.jcp.2006.05.009): text extraction, all sections and the Appendix tables (coefficients not transcribed); the downwind-indicator constraint (eq. 15) is illegible and described in words. Reference list: 35 entries.
