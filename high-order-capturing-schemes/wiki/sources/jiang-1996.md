---
type: Source
title: "Jiang & Shu (1996) — Efficient implementation of weighted ENO schemes"
description: "WENO-JS: the finite-difference flux WENO with optimal linear weights and the L²-derivative smoothness indicator, giving fifth order from third-order ENO stencils; error analysis of Liu–Osher–Chan, convergence for smooth solutions, pressure–entropy weights, and a standard test suite."
resource: "doi:10.1006/jcph.1996.0130"
source_kind: paper
authors: [Jiang G.-S., Shu C.-W.]
year: 1996
venue: "J. Comput. Phys. 126:202-228 (read as the 40-page preprint)"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1996-JCP-Jiang-101006jcph19960130.pdf"
tags: [weno, finite-difference, nonlinear-weights, benchmark]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Recasts WENO in the Shu–Osher flux framework and shows that the $r$
candidate stencils can reach order $2r-1$ — the upstream-central scheme
on the union stencil — if the weights approach the optimal linear
weights to $O(h^{r-1})$. The Liu–Osher–Chan indicator falls short of
that for $r = 3$; a new indicator, the scaled $L^2$ norms of the
candidate polynomial's derivatives, gives fifth order. This WENO5 is
the scheme later called WENO-JS. The archived file is a preprint
(40 pp.); section and equation numbers below follow it. Merged into
[WENO](/methods/weno.md), [smoothness indicator](/definitions/smoothness-indicator.md),
[accuracy at critical points](/properties/accuracy-at-critical-points.md),
[characteristic decomposition](/methods/characteristic-decomposition.md)
and seven benchmark pages.

# Key claims

1. **Error analysis of Liu–Osher–Chan** (§2): order $r+1$ in smooth
   monotone regions; for $r = 3$ only third at critical points; the
   apparent super-convergence comes from larger coarse-grid errors.
   $q = 2$ adequate; $\varepsilon = 10^{-6}$; a discontinuous stencil's
   weight is $O(h^{2q})$.
2. **New indicator** (§3, eq. 3.1) and its $r = 3$ forms (3.2–3.4);
   $\beta_k = (f'h)^2(1 + O(h^2))$ where $f' \neq 0$, and
   $\beta_k = \tfrac{13}{12}(f''h^2)^2(1 + O(h^2))$ where $f' = 0$,
   "which implies that the weights … are also 5th order accurate at
   critical points" (eq. 3.9).
3. **Pressure–entropy weights for Euler** (§4): weights from pressure in
   the genuinely nonlinear fields and entropy in the linearly degenerate
   ones, two projections instead of many; about twice as fast; fails with
   strong shocks or reflected waves (explained by mirrored ghost values).
4. **Artificial compression** (§5, Yang's parameter 33) in contact fields.
5. **Convergence** for smooth solutions (§6, Theorem 6.1, via Strang).
6. **Efficiency** (§7): WENO4/WENO5 at least twice as fast as ENO4 on a
   CRAY C-90 (WENO5-PS up to 3.9 times in 3D), about as fast on
   workstations; a second-order TVD scheme is 3.5–10 times faster than
   ENO4.
7. **Tests** (§8): composite linear advection, Buckley–Leverett, Sod and
   Lax, 1D and 2D shock–entropy-wave interaction, interacting blast
   waves, quasi-1D nozzle to steady state (residual to $10^{-7}$), oblique
   Sod, forward step, double Mach reflection, shock–vortex interaction,
   supersonic flow past a cylinder.

# Notation map

| Jiang & Shu (1996) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $h(x)$ | $\mathcal{H}(x)$ | renamed: registry $h$ is the spacing |
| $\Delta x$, $h$ | $h$ | |
| $f^\pm$, $\alpha$ | $f^\pm$, $\alpha$ | LF splitting |
| $S_k$, $q^r_k$, $a^r_{k,l}$ | $S_k$, $q_k$, coefficients | Table 1 |
| $C^r_k$ | $d_k$ | optimal weights, Table 2 |
| $IS_k$ | $\beta_k$ | |
| $\alpha_k$ | $\tilde\omega_k$ | renamed: registry $\alpha$ is the LF speed |
| $\omega_k$, $\epsilon$, $p$ | $\omega_k$, $\varepsilon$, $q$ | |
| WENO-X-n, -PS, -A | scheme labels | order $n$ in $L_1$ sense |

# Pages created or updated

* Created [Composite-profile linear advection (Jiang–Shu test)](/benchmarks/composite-advection-profile.md).
* Created [Double Mach reflection](/benchmarks/double-mach-reflection.md).
* Created [Mach 3 wind tunnel with a forward-facing step](/benchmarks/forward-facing-step.md).
* Updated [Woodward–Colella interacting blast waves](/benchmarks/interacting-blast-waves.md).
* Updated [Lax shock tube](/benchmarks/lax-shock-tube.md).
* Created [Shock–vortex interaction](/benchmarks/shock-vortex-interaction.md).
* Updated [Shu–Osher shock/entropy-wave interaction](/benchmarks/shu-osher-problem.md).
* Updated [Sod shock tube](/benchmarks/sod-shock-tube.md).
* Updated [Essentially non-oscillatory (ENO property)](/definitions/essentially-non-oscillatory.md).
* Updated [Smoothness indicator](/definitions/smoothness-indicator.md).
* Created [Central WENO (staggered, Levy–Puppo–Russo)](/methods/central-weno.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Conservative finite-difference (flux) formulation](/methods/conservative-finite-difference.md).
* Updated [Contact-discontinuity sharpening (subcell resolution, artificial compression, steepening)](/methods/contact-sharpening.md).
* Updated [ENO reconstruction and schemes](/methods/eno-reconstruction.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [Accuracy at critical points](/properties/accuracy-at-critical-points.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/1996-JCP-Jiang-101006jcph19960130.pdf` (preprint of doi:10.1006/jcph.1996.0130, 40 pp.): text extraction (ligatures fi/ff/fl dropped), all sections and figure captions; Tables 1–2 and eqs. (2.13)–(3.10) read from page images (preprint pp. 5–9). Reference list (21 entries) from the preprint; [11] Roe is printed with Sod's venue.
