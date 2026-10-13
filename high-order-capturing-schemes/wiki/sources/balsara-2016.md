---
type: Source
title: "Balsara, Garain & Shu (2016) — An efficient class of WENO schemes with adaptive order"
description: "Legendre-basis reconstructions with smoothness indicators as sums of perfect squares (r = 3–9), and WENO-AO: a large centred high-order polynomial nonlinearly hybridized with the r = 3 central WENO, recursively (AO(7,5,3), AO(9,5,3)), needing no MP step."
resource: "doi:10.1016/j.jcp.2016.09.009"
source_kind: paper
authors: [Balsara D.S., Garain S., Shu C.-W.]
year: 2016
venue: "J. Comput. Phys. 326:780-804"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2016-JCP-Balsara-101016jjcp201609009.pdf"
tags: [weno, adaptive-order, legendre-basis, central-weno]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Two advances for finite-difference WENO: compact Legendre-basis formulas
that make very high order cheap, and adaptive-order schemes that keep a
large central stencil when the data allow and fall back to a very stable
third-order central WENO otherwise. Builds on Zhu–Qiu's device while
avoiding its van Albada-like clipping. Merged into
[adaptive-order WENO](/methods/weno-ao.md) (opening a `Contradictions`
entry about WENO-ZQ), with updates to central WENO, MP limiting, the
smoothness-indicator and modified-wavenumber pages and the benchmarks.

# Key claims

1. **Legendre basis** (§2): reconstructions and indicators for $r = 3$–$9$;
   indicators are sums of perfect squares, the same form for all stencils
   of an $r$ and nested across $r$.
2. **WENO-AO(5,3)** (§3.1): linear weights from $\gamma_{\mathrm{Hi}}$,
   $\gamma_{\mathrm{Lo}}$; $\tau$ (eq. 3.6); weights (eq. 3.7a, or the
   "more stable" 3.7b); reconstruction (eq. 3.9). AO(7,3), AO(9,3),
   recursive AO(7,5,3) with a convexity condition (§§3.2–3.4).
3. **Accuracy** (§4): design orders on advection, Burgers, 2D Euler;
   AO(5,3) more accurate than WENO-ZQ; spectral comparison with compact
   schemes.
4. **Tests** (§5): composite advection (ZQ overshoots as published),
   Lax, blast waves, Shu–Osher, DMR, forward step, oblique shock–vortex;
   relative cost (Table 4).
5. Analogy with MOOD: AO is an *a priori* adaptive order.

# Notation map

| Balsara et al. (2016) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $P^{r5}_3$, $P^{r3}_{1,2,3}$ | $P$ (large central), $p_k$ (CWENO stencils) | |
| $\gamma^{r5}_3$, $\gamma^{r3}_k$ | $d_P$, $d_k$ | |
| $\gamma_{\mathrm{Hi}}$, $\gamma_{\mathrm{Lo}}$ | $\gamma_{\mathrm{Hi}}$, $\gamma_{\mathrm{Lo}}$ | |
| $w$, $\bar w$ | $\tilde\omega$, $\omega$ | |
| $\beta^{r}_k$ | $\beta_k$ | |
| $u_x, u_{x^2}, \dots$ | Legendre moments | no registry symbol |
| $\lambda$ | $\alpha$ | LF speed |

# Pages created or updated

* Updated [Composite-profile linear advection (Jiang–Shu test)](/benchmarks/composite-advection-profile.md).
* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md).
* Updated [Mach 3 wind tunnel with a forward-facing step](/benchmarks/forward-facing-step.md).
* Updated [Woodward–Colella interacting blast waves](/benchmarks/interacting-blast-waves.md).
* Updated [Lax shock tube](/benchmarks/lax-shock-tube.md).
* Updated [Shock–vortex interaction](/benchmarks/shock-vortex-interaction.md).
* Updated [Shu–Osher shock/entropy-wave interaction](/benchmarks/shu-osher-problem.md).
* Updated [Modified wavenumber (dispersion and dissipation analysis)](/definitions/modified-wavenumber.md).
* Updated [Smoothness indicator](/definitions/smoothness-indicator.md).
* Updated [Central WENO (staggered, Levy–Puppo–Russo)](/methods/central-weno.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Hybrid compact-WENO schemes](/methods/hybrid-compact-weno.md).
* Updated [Monotonicity-preserving (MP) limiting](/methods/monotonicity-preserving-limiter.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Created [Unequal-stencil and adaptive-order WENO (WENO-ZQ, WENO-AO)](/methods/weno-ao.md).
* Updated [WENO-Z](/methods/weno-z.md).
* Updated [Notation registry](/notation.md): batch-2 registry extensions.
* Also cited on [Burgers equation: shock formation](/benchmarks/burgers-shock-formation.md) (created 2026-10-13).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2016-JCP-Balsara-101016jjcp201609009.pdf` (doi:10.1016/j.jcp.2016.09.009): text extraction, all sections; eqs. (3.6)–(3.9) read from the page image (p. 790). Legendre-basis coefficient formulas of §2 not reproduced. Reference list: 37 entries.
