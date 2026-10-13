---
type: Source
title: "Zhang & Shu (2010) — On positivity-preserving high order discontinuous Galerkin schemes for compressible Euler equations on rectangular meshes"
description: "A sufficient condition — admissible Gauss–Lobatto point values plus a CFL bound — for positivity of cell averages of any-order FV or DG schemes for Euler, enforced by a conservative, accuracy-preserving linear scaling limiter; extended to rectangular meshes and tested with third-order RKDG."
resource: "doi:10.1016/j.jcp.2010.08.016"
source_kind: paper
authors: [Zhang X., Shu C.-W.]
year: 2010
venue: "J. Comput. Phys. 229:8918-8934"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2010-JCP-Zhang-101016jjcp201008016.pdf"
tags: [positivity, limiter, dg, finite-volume, euler]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Generalizes Zhang and Shu's maximum-principle limiter and Perthame and
Shu's positivity framework to a simple, provable positivity limiter for
Euler at arbitrary order. Merged into the new
[positivity preservation](/properties/positivity-preserving.md) and
[scaling limiter](/methods/positivity-preserving-scaling-limiter.md)
pages and into five new benchmarks.

# Key claims

1. **Convexity** (§1): $p$ is concave for $\rho \ge 0$, so $\mathcal{G}$
   is convex; standard RKDG-TVB, ENO and WENO schemes are not
   positivity-preserving.
2. **Theorem 2.1**: if the degree-$K$ polynomial is admissible at the
   $N_{\mathrm{GL}}$ Gauss–Lobatto points, the forward-Euler cell average
   is admissible under $\nu \le \hat w_1\nu_0$; SSP stepping keeps it
   (Remark 2.2). Any quadrature containing both cell ends would do, and
   Gauss–Lobatto is best for $K = 2, 3$ (Remark 2.3).
3. **Lax–Friedrichs** (Remark 2.4): $\nu_0$ relaxed from Perthame–Shu's
   $1/2$ to 1. CFL bounds in Table 2.1: $1/6$ ($K = 2, 3$), $1/12$
   ($K = 4, 5$).
4. **Limiter** (§2.2): density scaling $\theta_\rho$, then pressure
   scaling $\theta_p$ from quadratic equations; conservative,
   admissible (Lemma 2.5) and $O(h^{K+1})$ accurate. A safety factor of
   2–3 on the stage wave speed is used with RK3 (Remark 2.7).
5. **2D rectangular meshes** (§3): tensor Gauss × Gauss–Lobatto
   quadratures, Theorem 3.1.
6. **Tests** (§4, RKDG3): low-density accuracy, 1D and 2D Sedov,
   double rarefaction, Leblanc, Mach 80 and Mach 2000 jets, shock
   diffraction. The positivity limiter lets the TVB constant be raised
   far beyond the values that otherwise blow up; the TVB limiter is still
   needed at shocks.

# Notation map

| Zhang & Shu (2010) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf w = (\rho, m, E)$ | $u$ | conserved state |
| $G$, $G^\varepsilon$ | $\mathcal{G}$ and its $\epsilon_{\mathcal{G}}$-shrunk version | |
| $\varepsilon$ ($10^{-13}$) | $\epsilon_{\mathcal{G}}$ | not the WENO $\varepsilon$ |
| $\mathbf q_j(x)$, degree $k$ | $\mathcal{P}_i(x)$, degree $K$ | |
| $\hat x^\alpha_j$, $\hat w_\alpha$, $N$ | $\hat x^{(a)}_i$, $\hat w_a$, $N_{\mathrm{GL}}$ | registry $\alpha$ is the LF speed |
| $\lambda = \Delta t/\Delta x$, $\alpha_0$ | $\Delta t/h$, $\nu_0$ | |
| $a_0 = \Vert(\vert u\vert + c)\Vert_\infty$ | $\alpha$ | LF speed |
| $\theta_1$, $\theta_2$ | $\theta_\rho$, $\theta_p$ | |
| $\mathbf h(\cdot,\cdot)$ | $\hat f(\cdot,\cdot)$ | |

# Pages created or updated

* Created [Double-rarefaction (near-vacuum) Riemann problems](/benchmarks/double-rarefaction.md).
* Created [High-Mach-number astrophysical jet (Mach 80 and Mach 2000)](/benchmarks/high-mach-astrophysical-jet.md).
* Created [Leblanc shock tube (extreme pressure and density ratio)](/benchmarks/leblanc-shock-tube.md).
* Created [Sedov point-blast wave (low-density positivity test)](/benchmarks/sedov-blast-wave.md).
* Created [Shock diffraction at a backward-facing corner](/benchmarks/shock-diffraction.md).
* Updated [Monotone numerical flux](/definitions/monotone-flux.md).
* Created [Zhang–Shu positivity-preserving scaling limiter](/methods/positivity-preserving-scaling-limiter.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Created [Positivity preservation (invariance of the admissible set)](/properties/positivity-preserving.md).
* Updated [Notation registry](/notation.md): batch-3 registry extensions.
* Also cited on [SSP linear multistep methods](/methods/ssp-linear-multistep.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2010-JCP-Zhang-101016jjcp201008016.pdf` (doi:10.1016/j.jcp.2010.08.016; typeset article): text extraction, all sections; eqs. (1.1)–(2.12) and Table 2.1 read from the page images (pp. 8919–8923). Initial data of the 2D Sedov corner cell are not legible in the text layer and are not reproduced. Reference list: 28 entries.
