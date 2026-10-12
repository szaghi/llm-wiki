---
type: Source
title: "Ranocha, Sayyari, Dalcin, Parsani & Ketcheson (2020) — Relaxation Runge–Kutta methods: fully discrete explicit entropy-stable schemes for the compressible Euler and Navier–Stokes equations"
description: "Generalizes relaxation Runge–Kutta to any convex functional: one scalar root per step rescales the update so the entropy changes by exactly the method's quadrature of its rate; proves a unique positive root γ = 1 + O(Δt^{p−1}), order p for RRK and p−1 for IDT, and couples it with entropy-stable SBP–SAT for fully discrete entropy-stable 3D Euler and Navier–Stokes, with no shock capturing."
resource: "doi:10.1137/19M1263480"
source_kind: paper
authors: [Ranocha H., Sayyari M., Dalcin L., Parsani M., Ketcheson D.I.]
year: 2020
venue: "SIAM J. Sci. Comput. 42:A612–A638"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2020-SISC-Ranocha-10113719m1263480.pdf"
tags: [time-discretization, runge-kutta, entropy]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

Explicit Runge–Kutta methods do not inherit the entropy stability of an
entropy-stable semi-discretization. The paper extends Ketcheson's
relaxation idea from inner-product norms to any smooth convex functional
$\mathcal S$. The update $\Delta t\sum_j\mathsf b_j\mathcal L(Y_j)$ is
multiplied by the positive root $\gamma^n_{\mathrm R}$ of a scalar convex
function, so $\mathcal S$ changes by exactly the method's quadrature of
$\frac{d}{dt}\mathcal S$. Combined with entropy-conservative or
entropy-stable flux-differencing SBP–SAT discretizations, this gives
explicit, fully discrete entropy-stable schemes of arbitrary order for 3D
Euler and Navier–Stokes. Merged into
[relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md).

# Key claims

1. **The relaxed step** (§2, eqs. 2.1–2.6). $u^{n+1}_\gamma = u^n + \gamma^n_{\mathrm R}\Delta t\sum_j\mathsf b_j\mathcal L(Y_j)$,
   with $\gamma^n_{\mathrm R}$ a root of $\Psi^n(\gamma)$. The two sums are
   accumulated during the stages, so low-storage implementations still
   work (p. 4).
2. **Entropy conservation and dissipation** (Theorem 2.2). With
   $\mathsf b_j \ge 0$ and $\gamma^n_{\mathrm R} \ge 0$ the step is
   dissipative. The Fehlberg and Dormand–Prince 5(4) pairs have
   $\mathsf b_5 < 0$ (Remark 2.3).
3. **Existence** (Lemmas 2.4, 2.6; Theorems 2.8, 2.15). Every method of order
   $\ge 2$ has, for small $\Delta t$, a unique positive root
   $\gamma^n_{\mathrm R} = 1 + O(\Delta t^{p_{\mathrm t}-1})$, and
   $\Psi^n(1) = O(\Delta t^{p_{\mathrm t}+1})$ (Corollary 2.13).
4. **IDT against RRK** (p. 4; Theorem 2.11). Assigned to $t^n + \Delta t$
   (IDT), the order drops by one; assigned to $t^n + \gamma^n_{\mathrm R}\Delta t$
   (RRK), it stays $p_{\mathrm t}$. Heun's three-stage third-order method
   with relaxation is fourth order on two oscillators (Remark 2.17).
5. **Retained structure** (§2.3). Linear invariants are kept. SSP
   properties are kept for $\gamma^n_{\mathrm R}$ near 1, cited from
   Ketcheson (2019) with no bound. Several convex quantities: take the
   smallest root. Proposition 2.18 extends existence to non-convex
   functionals under a nondegeneracy condition.
6. **Root-finding** (§2.4). Brent's method in the ODE tests; bisection to
   machine precision in the 3D solver (§4).
7. **CFD** (§4, Conclusions). Fully discrete entropy stability holds
   globally, not cell by cell. Positivity is not addressed. Relaxation
   adds no significant dissipation in the tests and can remove some.

**Tests.**
* *ODEs* (§3): conserved and dissipated exponential entropies, and the
  nonlinear pendulum at $\Delta t = 0.9$ to $t = 1000$. Unmodified
  SSPRK(3,3) gains energy and RK4 loses it; RRK and IDT conserve it to
  round-off. IDT is fragile to the nonlinear solver (Fig. 2c).
* *3D isentropic vortex* (§4.1): $L^2$ rates 4.21, 5.17 and 6.15 for
  degrees 3–5 (Table 1). Quadruple-precision entropy conservation with
  all 13 methods on random-degree nonconforming grids; without
  relaxation every method changes the entropy (Fig. 7).
* *Viscous shock* (§4.2): Mach 2.5, Re 10, $\Delta t \propto h^2$; rates
  4.19, 5.33 and 6.23 (Table 2).
* *Sod* (§4.3) and *Titarev–Toro sine–shock* (§4.4): degree 3, no shock
  capturing; small overshoots, identical with and without relaxation,
  $\vert\gamma^n_{\mathrm R} - 1\vert < 5\times10^{-4}$.
* *Lid-driven cavity* (§4.5) and *supersonic square rod* (§4.6, Mach 1.5,
  Re $10^4$): stable, $\vert\gamma^n_{\mathrm R} - 1\vert \le 2.5\times10^{-7}$.

# Notation map

| Ranocha et al. (2020) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $f(t, u)$, $f_i$ | $\mathcal L(u)$, $\mathcal L(Y_i)$ | $f$ is the flux in the registry |
| $A = (a_{ij})$, $b_i$, $c_i$; $y_i$ | $\mathsf a_{ij}$, $\mathsf b_i$, $\mathsf c_i$; $Y_i$ | Butcher form |
| $p$ | $p_{\mathrm t}$ | also the SBP degree in §4 |
| $\gamma_n$ | $\gamma^n_{\mathrm R}$ | the paper also uses $\gamma = 1.4$ |
| $\eta$ | $\mathcal S$ | registry $\eta$ is the coercivity constant |
| $r(\gamma)$ | $\Psi^n(\gamma)$ | $r$ is the stencil count |
| $S$, $w$ | $U$, $U'(u)$ | entropy density and variables |
| $d^n$, $e$ | words | accumulated direction and entropy estimate |

# Pages created or updated

* Created [Relaxation Runge–Kutta methods](/methods/relaxation-runge-kutta.md), [Explicit Runge–Kutta methods](/methods/explicit-runge-kutta.md).
* Updated [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) (entropy needs forward Euler), [Low-storage Runge–Kutta](/methods/low-storage-runge-kutta.md), [Positivity preservation](/properties/positivity-preserving.md), [Isentropic vortex](/benchmarks/isentropic-vortex.md), [Sod](/benchmarks/sod-shock-tube.md), [Shu–Osher problem](/benchmarks/shu-osher-problem.md).
* Updated [Notation registry](/notation.md): $\gamma^n_{\mathrm R}$, $\Psi^n$, $\mathcal S$, $U$, Butcher symbols.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2020-SISC-Ranocha-10113719m1263480.pdf`.
   * **Version.** arXiv:1905.09129v4 (23 November 2019), 28 pages, not
     the typeset article; the preprint title reads "Fully-Discrete".
   * **Identity.** doi:10.1137/19M1263480, checked on Crossref: SIAM J.
     Sci. Comput. 42(2):A612–A638, 2020.
   * **How it was read.** Text extraction, all sections; eqs. 2.1–2.7 and
     Theorem 2.2 checked on the page image. The integral remainders of
     eqs. 2.8–2.11, eq. 3.3 and parts of eqs. 4.7 and 4.9 are garbled in
     the text layer and not reproduced.
   * **Recorded as printed.** The sine–shock left-state velocity is
     printed "0523346".
   * **Reference list:** 58 entries (Crossref counts 57 for the published
     version). Ref. 53 prints Titarev & Toro's JCP 201:238 with the year
     2014; it is merged as `titarev-2004`. Del Rey Fernández is printed
     "Fernández".
