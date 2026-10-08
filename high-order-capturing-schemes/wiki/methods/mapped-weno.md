---
type: Method
title: "Mapped WENO (WENO-M)"
description: "Henrick–Aslam–Powers correction of WENO-JS: each nonlinear weight is mapped by a function flat at its linear weight, which restores fifth order at first-order critical points and removes the dependence of the order on ε."
status: established
aliases: [WENO-M, WENO5M, mapped WENO]
tags: [weno, nonlinear-weights, critical-points]
timestamp: 2026-10-08T00:00:00Z
---

# Mapped WENO (WENO-M)

**Why** ([Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md)). At a
critical point with $f' = 0$ but $f''' \neq 0$ the WENO-JS indicators
$\beta_0$ and $\beta_2$ differ at relative $O(h)$, so
$\omega_k = d_k + O(h)$ and fifth-order [WENO](/methods/weno.md) drops
to third order; the ε recommended in the literature, $10^{-6}$, had
masked this by dominating the indicators on fine grids
([accuracy at critical points](/properties/accuracy-at-critical-points.md)).

**The mapping.** For each $k$,
$$g_k(\omega) = \frac{\omega\left(d_k + d_k^2 - 3 d_k\,\omega + \omega^2\right)}{d_k^2 + \omega\,(1 - 2 d_k)},$$
which is monotone on $[0,1]$ with $g_k(0) = 0$, $g_k(1) = 1$,
$g_k(d_k) = d_k$ and $g_k'(d_k) = g_k''(d_k) = 0$. The mapped
weights are $\omega^{\mathrm{M}}_k = g_k(\omega_k)/\sum_l g_l(\omega_l)$
with $\omega_k$ the WENO-JS weights; a weight within $O(h)$ of $d_k$ is
moved to within $O(h^3)$, which satisfies the fifth-order conditions
(eq. 43–46; properties as listed by
[Borges et al. (2008)](/sources/borges-2008.md)). Weights near 0 or 1 are
barely changed, so the ENO behaviour is kept.

**Results.** WENO5M with $\varepsilon = 10^{-40}$ converges at fifth
order on $\sin(\pi x - \sin(\pi x)/\pi)$, whose critical points have
$f''' \neq 0$, and is indistinguishable from the upstream-central
scheme there; WENO5 with the same ε is third order, and with
$\varepsilon = 10^{-6}$ its observed order fluctuates and even exceeds
five as ε takes over — the explanation of the "super-convergence"
([Henrick et al. (2005)](/sources/henrick-2005.md), Tables 5–8, Fig. 7).
Applied once or twice to WENO of $r = 2$–$6$, the mapping recovers the
design order for $1 \le n_{\mathrm{cp}} < r - 1$; at
$n_{\mathrm{cp}} = r - 1$ the weights are $O(1)$ from ideal and no
mapping helps.

**With shocks.** WENO5M is sharper than WENO5 on the Shu–Osher problem,
the blast waves and Lax's problem, and about 10 % more accurate on Sod,
but both converge at roughly first order (5/6 for contacts); "the
improvement for flows with shocks is proportional rather than
geometric", and enthusiasm for high order with shocks "should be
proportionately tempered" ([Henrick et al. (2005)](/sources/henrick-2005.md), §§5.4–5.7).

**Cost and dissipation.** The mapping adds 20–30 % CPU over WENO-JS
([Borges et al. (2008)](/sources/borges-2008.md);
[Castro, Costa & Don (2011)](/sources/castro-2011.md)). For the same
power $q$, WENO-M assigns the largest weights to discontinuous stencils
of the three schemes (JS, Z, M), hence it is the least dissipative and
also the one that needs the largest $q$ to stay non-oscillatory at high
order ([Castro et al. (2011)](/sources/castro-2011.md), §5;
[WENO-Z](/methods/weno-z.md)).

# Citations

1. [Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md), §§3–6 (eqs. 37–46 and 60 read from the page images).
2. [Borges et al. (2008)](/sources/borges-2008.md), §2.
3. [Castro, Costa & Don (2011)](/sources/castro-2011.md), §§2, 4–5.
