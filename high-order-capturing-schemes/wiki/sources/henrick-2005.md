---
type: Source
title: "Henrick, Aslam & Powers (2005) — Mapped weighted essentially non-oscillatory schemes: achieving optimal order near critical points"
description: "Shows that WENO-JS is only third order at critical points with f′ = 0, f‴ ≠ 0 (a missing order condition, hidden by ε), gives necessary and sufficient weight conditions and the rate formula for orders 3–11, and restores fifth order with a weight mapping (WENO-M)."
resource: "doi:10.1016/j.jcp.2005.01.023"
source_kind: paper
authors: [Henrick A.K., Aslam T.D., Powers J.M.]
year: 2005
venue: "J. Comput. Phys. 207:542-567"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2005-JCP-Henrick-101016jjcp200501023.pdf"
tags: [weno, mapped-weno, critical-points, accuracy]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

A careful re-derivation of fifth-order finite-difference WENO. The
conditions on the weights for fifth order involve the flux *difference*,
which adds a condition missing from Jiang and Shu. The WENO-JS weights
violate the conditions near critical points where $f'$ vanishes but
$f'''$ does not, so WENO5 is third order there; the effect was hidden
because the usual test functions have $f' = f''' = 0$ together and
because $\varepsilon = 10^{-6}$ dominates the indicators on fine grids.
A mapping of the weights fixes it. Merged into
[mapped WENO](/methods/mapped-weno.md),
[accuracy at critical points](/properties/accuracy-at-critical-points.md)
(closing its `Contradictions` entry) and
[weight accuracy conditions](/results/weno-weight-accuracy-conditions.md).

# Key claims

1. **Upstream-central flux** and candidate fluxes derived via the flux
   function (§§2–3); individual fluxes are only fifth order, but the
   leading errors cancel in the difference.
2. **Necessary and sufficient conditions** (eqs. 25–29): sum to one,
   $\omega^\pm - d = O(h^2)$, and a new condition on
   $\sum_k A_k(\omega^+_k - \omega^-_k)$.
3. **WENO-JS fails them at critical points** (Table 1, eqs. 37–39), with a
   stated discrepancy from Jiang–Shu's expansions 3.5, 3.7, 3.9.
4. **ε** (§4.3) is dimensional and sets the observed order; machine-
   precision values ($10^{-40}$, 128-bit arithmetic) expose third order on
   $x^3 + \cos x$ at $x = 0$ (Table 3).
5. **WENO5M** (§5): mapping $g_k$ (eq. 43), fifth order on
   $\sin(\pi x - \sin(\pi x)/\pi)$ at $\varepsilon = 10^{-40}$; WENO5 is
   third order at that ε and "super-convergent" at $10^{-6}$.
6. **Euler tests**: Shu–Osher, blast waves, Lax, Sod convergence (both
   schemes about 5/6 order, WENO5M about 10 % more accurate).
7. **Orders 3–11** (§6): $r_c = \max(2r - 2 - n_{\mathrm{cp}}, n_{\mathrm{cp}})$
   near critical points ($r \le 6$, Table 10); one or two mappings recover
   optimal rates for $1 \le n_{\mathrm{cp}} < r - 1$.

# Notation map

| Henrick et al. (2005) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $h(x)$, $\hat f$ | $\mathcal{H}(x)$, $\hat f_{i+1/2}$ | |
| $\Delta x$ | $h$ | |
| $\bar\omega_k$ | $d_k$ | ideal weights |
| $\omega^{(JS)}_k$, $\omega^{(M)}_k$ | $\omega_k$ (JS), mapped weights | |
| $\alpha_k$, $\epsilon$, $p$ | $\tilde\omega_k$, $\varepsilon$, $q$ | |
| $g_k(\omega)$ | $g_k(\omega)$ | |
| $n_{CP}$ | $n_{\mathrm{cp}}$ | |
| $r_c$ | convergence rate | |

# Pages created or updated

* Updated [Woodward–Colella interacting blast waves](/benchmarks/interacting-blast-waves.md).
* Updated [Lax shock tube](/benchmarks/lax-shock-tube.md).
* Updated [Shu–Osher shock/entropy-wave interaction](/benchmarks/shu-osher-problem.md).
* Updated [Sod shock tube](/benchmarks/sod-shock-tube.md).
* Updated [Smoothness indicator](/definitions/smoothness-indicator.md).
* Updated [Conservative finite-difference (flux) formulation](/methods/conservative-finite-difference.md).
* Created [Mapped WENO (WENO-M)](/methods/mapped-weno.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [Accuracy at critical points](/properties/accuracy-at-critical-points.md).
* Created [Accuracy conditions on WENO nonlinear weights](/results/weno-weight-accuracy-conditions.md).
* Updated [Notation registry](/notation.md): batch-2 registry extensions.
* Also cited on [Self-similarity (scale invariance) of capturing schemes](/properties/self-similarity.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2005-JCP-Henrick-101016jjcp200501023.pdf` (doi:10.1016/j.jcp.2005.01.023): text extraction, all sections; Table 1, eqs. (37)–(43), Table 3 and eq. (60) read from page images (pp. 552, 555, 565). Reference list: 19 entries.
