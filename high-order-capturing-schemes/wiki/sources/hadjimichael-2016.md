---
type: Source
title: "Hadjimichael, Ketcheson, Lóczi & Németh (2016) — Strong stability preserving explicit linear multistep methods with variable step size"
description: "First explicit SSP linear multistep methods with step-history-dependent coefficients: the SSP condition with a state-dependent forward-Euler limit, the sharp bound C ≤ (Ω−p)/(Ω−1), closed-form optimal second-order and four/five-step third-order formulae, a greedy step rule whose step tends to the fixed-step SSP step, and order-2 and order-3 convergence."
resource: "doi:10.1137/15M101717X"
source_kind: paper
authors: [Hadjimichael Y., Ketcheson D.I., Lóczi L., Németh A.]
year: 2016
venue: "SIAM J. Numer. Anal. 54:2799–2832"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2016-SINUM-Hadjimichael-10113715m101717x.pdf"
tags: [time-discretization, ssp, multistep]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

SSP multistep methods use one evaluation of $\mathcal L$ per step and
need no stages, but their coefficients assume a fixed step, while a
CFL-limited step changes with the solution. The paper builds explicit
SSP multistep methods whose coefficients depend on the step history. It
gives the SSP condition with a state-dependent forward-Euler limit,
proves a sharp bound on the SSP coefficient, and derives closed-form
optimal formulae at second order (any number of steps) and third order
(four and five steps). It also gives a greedy step rule, bounds on the
resulting step sequence, and convergence. Merged into
[SSP linear multistep methods](/methods/ssp-linear-multistep.md).

# Key claims

1. **Form** (eqs. 3–5): coefficients depend on the step ratios
   $\Delta t^{n-j}/\Delta t^n$ (not ratios of adjacent steps); a
   *formula* is one coefficient set, a *method* adds the step rule (§2).
2. **SSP condition** (Theorem 1, eqs. 11–14; Remarks 1–2): the step bound
   takes the minimum over all past states of
   $\frac{a_{i,n}}{b_{i,n}}\Delta t_{\mathrm{FE}}(u^{n+1-i})$, and it is
   also necessary; using only the last state "will not give the correct
   step size in general".
3. **Bound** (Theorem 2, eq. 18): $\mathcal C \le (\Omega_{\Delta t} - p_{\mathrm t})/(\Omega_{\Delta t} - 1)$
   for $\Omega_{\Delta t} > p_{\mathrm t}$, else $\le 0$; Lenferink's
   $(m - p_{\mathrm t})/(m - 1)$ for fixed steps. Proved by LP duality with
   a polynomial certificate (§8.1).
4. **Second order** (Theorem 3, eqs. 19–21): exists iff
   $\Omega_{\Delta t} > 2$; optimal $\mathcal C = (\Omega_{\Delta t} - 2)/(\Omega_{\Delta t} - 1)$;
   SSPMSV32 is the three-step member.
5. **Third order** (Theorem 4, Proposition 1, eqs. 22–29): exists iff
   $\Omega_{\Delta t} > 3$; the four- and five-step formula (eq. 27) is
   optimal for $2 < \Omega_{\Delta t} - 1 \le 2(1 + \sqrt2)$; with fixed
   steps that holds iff $m = 4$ or $5$. SSPMSV43 is the four-step member.
   The optimal sparsity pattern can change with the history (Remark 4).
6. **Any order** (Theorem 5): exists for bounded step ratios and enough
   steps; no formula above order 3 is constructed.
7. **Greedy steps** (§4, eqs. 36, 39; Theorems 6–7): closed-form rule; the
   step tends to $\frac{m - p_{\mathrm t}}{m - 1}\Delta t_{\mathrm{FE}}$;
   third order needs slow variation of $\Delta t_{\mathrm{FE}}$ (eq. 34)
   and bounded starting steps (eq. 40).
8. **Convergence** (§5, Theorems 8–10): nonnegative $a_{i,n}$ give
   zero-stability; convergence of order 2 and 3.
9. **Motivation** (§1): with a positivity limiter, Runge–Kutta methods
   "can lead to order reduction, so linear multistep methods are
   recommended", citing Gottlieb, Ketcheson & Shu and Zhang & Shu's
   maximum-principle paper.

**Tests** (§6; spatial discretization from SharpClaw: MC-limited TVD for
second order, WENO5 for third, except Woodward–Colella; forward-Euler
Courant limit $1/2$ for all, proved only for the TVD scheme):
variable-coefficient advection, orders 1.95–2.99 (Table 1); Burgers,
Courant number settling at $1/4$ and $1/6$; the
[Woodward–Colella blast waves](/benchmarks/interacting-blast-waves.md) to
$t = 0.04$; a 2D shallow-water radial wave; an axisymmetric hydrodynamic
shock–bubble. No comparison with SSP Runge–Kutta, no timings.

# Notation map

| Hadjimichael et al. (2016) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $h$, $h_n$ | $\Delta t$, $\Delta t^n$ | $h$ is the grid spacing |
| $f(u)$ | $\mathcal L(u)$ | |
| $h_{\mathrm{FE}}(u)$ | $\Delta t_{\mathrm{FE}}(u)$ | |
| $k$ (steps) | $m$ | as on the barrier page |
| $\alpha_{j,n}$, $\beta_{j,n}$ | $a_{i,n}$, $b_{i,n}$, $i = m - j$ | index reversed |
| $\omega_j$, $\Omega_j$; $\Omega_k$ | words; $\Omega_{\Delta t}$ | $\omega_k$ are WENO weights |
| $\mu_n$ | $\min_i\Delta t_{\mathrm{FE}}(u^{n+1-i})$ | $\mu$ is the diffusion coefficient |
| $\gamma$ (safety factor), $s$ (efficiency ratio) | words | collide with $\gamma$ and $s$ |
| $\nu_{\mathrm{FE}}$ | words | forward-Euler Courant limit |

# Pages created or updated

* Created [SSP linear multistep methods](/methods/ssp-linear-multistep.md).
* Updated [SSP order barriers](/results/ssp-order-barriers.md) (Lenferink and variable-step bounds), [SSP Runge–Kutta](/methods/ssp-runge-kutta.md), [Positivity preservation](/properties/positivity-preserving.md) (why multistep), [Step-size control](/methods/runge-kutta-step-size-control.md), [Interacting blast waves](/benchmarks/interacting-blast-waves.md).
* Updated [Notation registry](/notation.md): $m$ (multistep), $\Omega_{\Delta t}$, $\Delta t_{\mathrm{FE}}(u)$.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2016-SINUM-Hadjimichael-10113715m101717x.pdf`.
   * **Version.** arXiv:1504.04107v2 (24 March 2016; the title page shows
     its build date, 21 March 2018), 42 pages, not the typeset article.
   * **Identity.** doi:10.1137/15M101717X, checked on Crossref: SIAM J.
     Numer. Anal. 54(5):2799–2832, 2016.
   * **How it was read.** Text extraction, all sections; Theorem 4 (p. 9)
     checked on the page image and summarized, not transcribed. The proofs
     of §§8.2–8.4 and 9.2–9.3 were skimmed.
   * **Reference list:** 16 entries; titles cut at the page edge were
     recovered from the text layer. The printed Zhang & Shu (2010) is the
     maximum-principle paper, merged as `zhang-2010-b`.
