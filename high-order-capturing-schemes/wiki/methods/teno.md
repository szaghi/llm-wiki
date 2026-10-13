---
type: Method
title: "Targeted ENO (TENO)"
description: "Fu–Hu–Adams scheme family: candidate stencils of incrementally increasing width, a strongly scale-separating smoothness measure, and an ENO-like 0/1 cutoff that keeps each stencil at its linear weight or drops it; the background linear scheme is optimized for dispersion and dissipation."
status: established
aliases: [TENO, TENO5, TENO6, targeted essentially non-oscillatory]
tags: [teno, low-dissipation, turbulence, nonlinear-weights]
timestamp: 2026-10-13T00:00:00Z
---

# Targeted ENO (TENO)

**Stencils.** The candidates have widths $3, 3, 3, 4, \dots$ points (one
more point per added stencil, each keeping at least one upwind point), so
the first three are exactly WENO5's. Their union is the full stencil, and
the design order equals its number of points (5 for TENO5, 6 for
TENO6). With two shocks close together the three-point stencil can still be smooth when every wide classical WENO
stencil is crossed, which recovers WENO5's robustness at very high order
([Fu, Hu & Adams (2016)](/sources/fu-2016.md), §3.1.1, Fig. 2).

**Selection** (eqs. 22–28, read from the page images):
$$\gamma_k = \left(C_w + \frac{\tau}{\beta_k + \varepsilon}\right)^q,\quad \chi_k = \frac{\gamma_k}{\sum_l \gamma_l},\quad \delta_k = \begin{cases}0, & \chi_k < C_T,\\ 1, & \text{otherwise},\end{cases}\quad \omega_k = \frac{d_k\delta_k}{\sum_l d_l\delta_l},$$
with $C_w = 1$, $q = 6$ (a strong separation between resolved and
non-resolved scales, against $q = 1$ in WENO-Z and WENO-CU6), and $\tau$
the global indicator of the full stencil: $\tau_5$ of WENO-Z for TENO5,
$\tau_6$ of WENO-CU6 for TENO6. A stencil is used with its *linear*
weight or not at all, so in smooth regions the scheme is exactly its
linear background scheme and the nonlinear dissipation of smooth
weight adaptation disappears. Order is restored under a condition on
$\tau$ weaker than the WENO conditions
([weight accuracy conditions](/results/weno-weight-accuracy-conditions.md));
the authors state it holds "even near critical points" for $\tau_6$ and
for their general full-stencil $\tau$. $C_T$ ($10^{-5}$ for TENO5, $10^{-7}$ for
TENO6) trades spectral resolution against shock detection and is set
case-independently.

**Optimized background scheme.** The background scheme of the full
stencil is replaced by a blend of two sub-schemes one order lower, with a
free blending parameter chosen to satisfy an approximate dispersion–dissipation
relation (Hu et al.) rather than to minimize dispersion error alone,
which in other optimized WENO schemes produced anti-dissipation at low
wavenumbers ([modified wavenumber](/definitions/modified-wavenumber.md)).
The "-opt" variants lose one order but resolve more; the published
parameter sets are $d = (0.6, 0.3, 0.1)$ (TENO5), $(0.55, 0.4, 0.05)$
(TENO5-opt), $(0.45, 0.3, 0.05, 0.2)$ (TENO6), $(0.462, 0.3, 0.054, 0.184)$
(TENO6-opt), Table 5.

**Results** (single parameter set, CFL 0.6, Roe characteristic
decomposition with global LF splitting): background-scheme order on a
Gaussian pulse; Sod and Lax monotone; blast waves sharper than WENO-JS
and WENO-Z and free of the overshoots of WENO-JS, WENO-Z and WENO-CU6;
Shu–Osher entropy waves retained best by TENO6 and TENO5-opt; double
Mach reflection at $1024 \times 256$ comparable to WENO-JS at
$1/960$; Rayleigh–Taylor; a viscous shock-tube matching the reference.
WENO-CU6-M fails the blast-wave and double Mach tests. Cost is about
that of classical WENO.

# Citations

1. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §§1–6 and Appendix A.
