---
type: Method
title: "Central WENO (staggered, Levy–Puppo–Russo)"
description: "A WENO reconstruction with weights symmetric about the cell centre, used inside a staggered Nessyahu–Tadmor-type central scheme with Runge–Kutta natural continuous extensions: no Riemann solver, no characteristic decomposition; fourth order from parabolas."
status: established
aliases: [CWENO, central WENO, Levy-Puppo-Russo scheme]
tags: [central-scheme, weno, staggered]
timestamp: 2026-10-13T00:00:00Z
---

# Central WENO (staggered, Levy–Puppo–Russo)

**Framework.** Central schemes extend the staggered Lax–Friedrichs
scheme: a piecewise-polynomial reconstruction is evolved exactly and
averaged on the staggered cells $[x_j, x_{j+1}]$. Under a CFL condition
the waves from the interfaces do not reach the staggered cell edges, so
the time integral of the flux there is over smooth data and a quadrature
(Simpson's rule for fourth order) suffices — no Riemann solver and no
characteristic decomposition (Nessyahu–Tadmor at second order; Liu–Tadmor
and Bianco–Puppo–Russo at third and higher with ENO).
[Levy, Puppo & Russo (1999)](/sources/levy-1999.md) replace the ENO step
by a centred WENO reconstruction.

**CWENO reconstruction.** In each cell $I_j$, three parabolas
$p_0, p_1, p_2$ are built, centred on $I_{j-1}$, $I_j$ and $I_{j+1}$,
each interpolating the cell averages of the three consecutive cells
centred on its own cell. The reconstruction in $I_j$ is the convex
combination $\sum_k \omega_k p_k(x)$ (a five-cell stencil); it reproduces $\bar u_j$, but no other interpolation
condition. The constants $d_k$ are chosen symmetric about the cell
centre — the "central" choice — in two sets: one for the
reconstruction from cell averages and one for the point-value
reconstruction of the flux derivative. By symmetry, any symmetric choice
gives a fourth-order point value at the cell centre; fifth order would
need non-positive constants, i.e. a non-convex combination, which the
method excludes. Indicators are Jiang–Shu's, $q = 2$,
$\varepsilon = 10^{-6}$
([smoothness indicator](/definitions/smoothness-indicator.md)).

**Time integration.** Predicted values at the quadrature nodes come from
a Runge–Kutta method with natural continuous extension (NCE), which gives
uniformly accurate dense output from one RK step; the flux derivative at
each RK stage uses the CWENO point-value reconstruction of $f$
([SSP Runge–Kutta](/methods/ssp-runge-kutta.md), use in this corpus).
The smoothness indicators can be computed once per step from the cell
averages and reused at all stages, with results indistinguishable from
per-stage indicators.

**Results.** Third- and fourth-order schemes reach their orders, with the
"super-convergence" of [Jiang & Shu (1996)](/sources/jiang-1996.md)
reproduced on $\sin^4$-type data. On Euler, component-wise indicators
give irregular weights near contacts, a global indicator shared by all
components is cheaper and better, and a density-based one better still
([characteristic decomposition](/methods/characteristic-decomposition.md)).
Sod, Lax and the
[interacting blast waves](/benchmarks/interacting-blast-waves.md) are
resolved without oscillation at shocks, with small wiggles near contacts
that decay under refinement. The new third-order scheme is more accurate
than third-order central ENO; the old fourth-order central ENO
(quartic polynomials) is more accurate than the fourth-order CWENO
(parabolas), at higher cost.

**The $r = 3$ CWENO in adaptive-order WENO.**
[Balsara, Garain & Shu (2016)](/sources/balsara-2016.md) use the three
third-order stencils with the central one weighted most (citing Levy,
Puppo & Russo's compact central WENO of 2000 and Cravero–Semplice) as the
fallback of WENO-AO, reporting that $r = 3$ CWENO "is extremely stable,
rivaling the stability of TVD schemes" and preserves physical extrema
([adaptive-order WENO](/methods/weno-ao.md)). This is a non-staggered use
of central weights inside a finite-difference scheme.

*Compiler note on naming:* later literature uses "CWENO" also for
reconstructions that blend a single high-degree "optimal" polynomial
with lower-degree ones; this page records the 1999 staggered scheme only.

**Later uses (batch 3).** The $r = 3$ CWENO, being robust and able to capture
extrema, is also the low-order level of pointwise WENO-AO
*interpolation* in [AFD-WENO](/methods/alternative-finite-difference-weno.md).
Its centred stencil gets weight $\gamma_{\mathrm{Lo}}$ and each biased one
$(1 - \gamma_{\mathrm{Lo}})/2$ ([Balsara et al. (2025)](/sources/balsara-2025.md), §III.a).

**Later uses (batch 6).** Shu credits central WENO with the first use of
unequal-size candidate stencils with free positive weights, later taken
up by WENO-ZQ and multi-resolution WENO ([Shu (2020)](/sources/shu-2020.md), §3.2.3;
[WENO-AO / WENO-ZQ](/methods/weno-ao.md)). For central WENO,
componentwise reconstruction works at third and even fourth order, but
very high order needs characteristic decomposition (Qiu and Shu, as cited
by [Shu (2009)](/sources/shu-2009.md), §3.5.5; [characteristic decomposition](/methods/characteristic-decomposition.md)).

# Citations

1. [Levy, Puppo & Russo (1999)](/sources/levy-1999.md), §§1–5.
2. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §1.
3. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §III.a.
4. [Shu (2020)](/sources/shu-2020.md), §3.2.3.
5. [Shu (2009)](/sources/shu-2009.md), §3.5.5.
6. [Jiang & Shu (1996)](/sources/jiang-1996.md), §2.
