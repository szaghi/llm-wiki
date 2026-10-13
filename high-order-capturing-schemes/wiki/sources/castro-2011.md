---
type: Source
title: "Castro, Costa & Don (2011) — High order weighted essentially non-oscillatory WENO-Z schemes for hyperbolic conservation laws"
description: "Extends WENO-Z to all odd orders with a closed-form global indicator and an optimal-order variant, shows that the power q (not the mapping) restores order at critical points for WENO-Z only, and ranks WENO-JS, WENO-Z, WENO-M by dissipation."
resource: "doi:10.1016/j.jcp.2010.11.028"
source_kind: paper
authors: [Castro M., Costa B., Don W.S.]
year: 2011
venue: "J. Comput. Phys. 230:1766-1792"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2011-JCP-Castro-101016jjcp201011028.pdf"
tags: [weno, weno-z, very-high-order, dissipation]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Taylor-expansion symmetries of the Jiang–Shu indicators give a global
indicator $\tau_{2r-1}$ for every odd order; the paper then studies how
the power $q$ and ε control critical-point order and dissipation, and
corrects a statement of Borges et al. about Henrick et al. Merged into
[WENO-Z](/methods/weno-z.md), [mapped WENO](/methods/mapped-weno.md),
[weight accuracy conditions](/results/weno-weight-accuracy-conditions.md)
and benchmark pages.

# Key claims

1. **Theorem 2:** $\tau_{2r-1} = \vert\beta_0 - \beta_{r-1}\vert$ ($r$ odd)
   or $\vert\beta_0 - \beta_1 - \beta_{r-2} + \beta_{r-1}\vert$ ($r$ even),
   $O(h^{r+2})$; Proposition 8: the optimal order of a linear combination
   of the $\beta_k$ (Table 2, $r \le 9$).
2. **Critical points** (§4): $q$ raises WENO-Z's rate (full order with
   $q = r - 1$ for $n_{\mathrm{cp}} < r - 1$); not for WENO-JS or WENO-M;
   $\varepsilon = h^2$-size as an implicit conditional.
3. **Remark 12** corrects Borges et al.; Remark 13: no meaningful shock
   example shows a substantial gain from critical-point treatment.
4. **Dissipation** (§5): weights on discontinuous stencils rank
   M > Z > JS for each $q$; larger $q$ more dissipative; oscillation
   tests at orders 5–11; DMR with orders 5, 9, 11 at three resolutions.

# Notation map

| Castro et al. (2011) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tau_{2r-1}$, $\tau^{opt}_{2r-1}$ | $\tau_{2r-1}$, optimal variant | |
| $p$ | $q$ | power parameter |
| $\epsilon = \Delta x^{r-1}$ | $\varepsilon$ | |
| $\beta_k$, $d_k$, $\omega^Z_k$ | $\beta_k$, $d_k$, $\omega_k$ | |
| $n_{cp}$ | $n_{\mathrm{cp}}$ | |

# Pages created or updated

* Updated [Composite-profile linear advection (Jiang–Shu test)](/benchmarks/composite-advection-profile.md).
* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md).
* Updated [Lax shock tube](/benchmarks/lax-shock-tube.md).
* Updated [Shu–Osher shock/entropy-wave interaction](/benchmarks/shu-osher-problem.md).
* Updated [Smoothness indicator](/definitions/smoothness-indicator.md).
* Updated [Mapped WENO (WENO-M)](/methods/mapped-weno.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [WENO-Z](/methods/weno-z.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [Accuracy at critical points](/properties/accuracy-at-critical-points.md).
* Updated [Accuracy conditions on WENO nonlinear weights](/results/weno-weight-accuracy-conditions.md).
* Updated [Notation registry](/notation.md): batch-2 registry extensions.
* Also cited on [Self-similarity (scale invariance) of capturing schemes](/properties/self-similarity.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2011-JCP-Castro-101016jjcp201011028.pdf` (doi:10.1016/j.jcp.2010.11.028): text extraction, all sections including the proofs of §3 (read for structure; the matrices of Proposition 8 not reproduced). Reference list: 19 printed entries, numbered to 21 with [6] and [18] missing in the original.
