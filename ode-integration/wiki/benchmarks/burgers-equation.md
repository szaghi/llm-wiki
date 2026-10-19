---
type: Benchmark
title: "Burgers equation"
description: "Inviscid Burgers u_t + (u²/2)_x = 0, whose smooth data steepen into a shock, and viscous Burgers with manufactured or periodic solutions; the sources use it to test relaxation, superviscosity filtering, IMEX and multirate entropy behaviour, order reduction from boundary data, and TASE stability with inexact Jacobians."
status: established
aliases: [inviscid Burgers equation, viscous Burgers equation, Bateman–Burgers equation]
tags: [structure-preserving, order-reduction, verification, stiff]
timestamp: 2026-10-19T23:00:00Z
---

# Burgers equation

The inviscid Burgers equation

$$\partial_tu+\partial_x\Big(\frac{u^2}2\Big)=0$$

is the scalar model of nonlinear steepening: smooth periodic data form a shock
in finite time. With the square entropy $\eta=u^2/2$ (entropy flux $u^3/3$),
entropy stability is $L^2$ stability
([Kang & Constantinescu (2022)](/sources/kang-2022.md), §2, Remark 1), which is
why the sources use it to test fully discrete
[entropy stability](/properties/entropy-stability.md). The viscous form adds
$\kappa\,\partial_x^2u$ (page-local viscosity $\kappa$; $\nu$ is the registry's
Courant number).

## Semidiscretizations used

* **Entropy-conservative DG flux.** Sun & Shu and Kang & Constantinescu both
  use the two-point flux
  $\hat f=\tfrac16\big((u^+)^2+u^+u^-+(u^-)^2\big)$
  ([Sun & Shu (2021)](/sources/sun-2021.md), Eq. (6.12); Kang & Constantinescu
  (2022), §1.2.4), the latter within Gassner's skew-symmetric (2/3 conservative,
  1/3 nonconservative) DG spectral element method with degree 3.
* **Entropy-stable flux.** Adding Lax–Friedrichs dissipation
  $\tfrac12\max(\lvert u^+\rvert,\lvert u^-\rvert)[\![u]\!]$ (Kang &
  Constantinescu (2022), §1.2.4), optionally with a minmod-type limiter of
  Chen and Shu applied after each step (§1.2.5).
* **Linearized-flux IMEX splitting.** Linearizing the flux about the element
  mean $\tilde u$ of $u_n$ gives an implicit linear part $\tilde uu$ and an
  explicit remainder $u^2/2-\tilde uu$, so each IMEX stage needs one linear
  solve (Kang & Constantinescu (2022), Remark 3, Eq. (11); see
  [IMEX Runge–Kutta](/methods/imex-runge-kutta.md)).

## Test configurations

* **Gaussian data** (Kang & Constantinescu (2022), Eq. (3)):
  $u_0=e^{-10x^2}$ on $[-1,1]$, periodic; a shock forms before $t=1$.
  Convergence on 100 uniform elements at $t=0.2$ against an RK4 reference with
  $h=5\times10^{-6}$; energy histories on 800 elements to $t=2$; a mesh refined
  five times toward the centre (2:1, element ratio 32) for multirate tests; and
  ten nested levels (3,099 elements) for a stability test.
* **Smooth periodic data** (Sun & Shu (2021), §6.3): entropy-conservative DG
  with second-order RK and $P^2$, and with Fehlberg's six-stage fifth-order
  method and $P^4$, $h=0.05\Delta x$, accuracy at $T=0.3$ and the shock at
  $x=\pi$ at $T=1.5$; the initial datum is not printed.
* **Viscous, manufactured** ([Biswas et al. (2023)](/sources/biswas-2023.md),
  §7.2, Eq. (31)): $u_t+uu_x=\kappa u_{xx}+g$ with $\kappa=0.1$, exact solution
  $u=\cos t$ (page-local forcing $g$), Dirichlet data, sixth-order finite
  differences on $10^3$ cells, $T=1$.
* **Viscous, manufactured with reaction and time-dependent Dirichlet data**
  ([González-Tabernero et al. (2024)](/sources/gonzaleztabernero-2024.md), §5.2):
  $u_t+(u^2/2)_x=2u_{xx}+(1+e^{-t}\cos x)\,u$ on $[-1,1]$ with exact solution
  $u=e^{-t}\sin x$ as Dirichlet data, local discontinuous Galerkin in space, a
  third-order IMEX Runge–Kutta method with convection and reaction explicit and
  diffusion implicit, CFL 0.4, $T=5$, 5 to 640 cells.
* **Viscous, periodic** ([Conte et al. (2024)](/sources/conte-2024.md), §7.1,
  Eqs. (7.1)–(7.3), from Calvo et al.): $u_t=\kappa u_{xx}-\tfrac12(u^2)_x$ on
  $[0,2\pi]$, periodic, $u_0=(1-\cos x)/2$, $t\in[0,4]$, fourth-order finite differences
  with 1024 points, $\kappa=10^{-1}$ and $10^{-2}$.

## What it shows

* **Relaxation keeps the order, IDT loses one.** With IMEX ARK2/ARK3,
  relaxation converges at 2.00 and 2.98–3.00, IDT at about 1 and 2 (Kang &
  Constantinescu (2022), Tables 2–3). With the multirate MRK2 at $t=1$, after
  the shock, IDT errors are at least 60 times larger and its shock lags,
  more so with the limiter (Table 4, Fig. 13). See
  [relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md).
* **Energy behaviour of plain methods.** With the entropy-conservative flux,
  relaxed and IDT methods hold the energy to $O(10^{-13})$; plain IMEX loses
  energy slightly, which the authors attribute to IMEX acting as a
  high-frequency filter, while explicit RK2 gains energy and blows up at twice
  the step (Kang & Constantinescu (2022), Fig. 5). Plain multirate MRK2 drifts
  to $O(10^{-1})$ (Fig. 11). Mass is conserved to $O(10^{-14})$ by all
  variants without limiter (Figs. 9, 15).
* **Superviscosity filter.** Sun & Shu (2021, Table 6.7, Figs. 6.8–6.10): the
  adaptive filter turns the growing $L^2$ norm of the plain methods into a
  decreasing one at orders 2 and 5; it does not suppress the post-shock
  oscillations, which need a strong fixed coefficient. See
  [superviscosity-stabilized RK](/methods/superviscosity-stabilized-runge-kutta.md).
* **Order reduction on a nonlinear problem.** DIRKs of weak stage order 4–5
  reach only order 3 on the viscous manufactured problem, better than weak
  stage order 1 but below their classical order 4–5 (Biswas et al. (2023),
  §7.2, Fig. 11); see [weak stage order](/definitions/weak-stage-order.md) and
  [order reduction](/definitions/order-reduction.md).
* **Boundary-induced order reduction and its cure.** On the reaction-forced problem with
  time-dependent Dirichlet data, imposing the data naively at the IMEX stage times gives
  observed rates 2.65, 2.26, 1.98 in $L^1$, $L^2$, $L^\infty$ for the third-order
  scheme; computing the stage boundary values from the stage equations and the PDE
  restores 3.01, 3.00, 3.00, "even in this nonlinear problem with huge temporal
  variations at the boundaries" (González-Tabernero et al. (2024), §5.2, Table 2). See
  [boundary conditions for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md).
* **TASE stability with an inexact Jacobian.** With the TASE operator built on the
  constant matrix $\kappa_{\mathrm s}(\kappa L_\Delta-2I)$ (page-local: $L_\Delta$ the
  discrete second derivative, $\kappa_{\mathrm s}$ a scaling), all TASE–Runge–Kutta
  methods of orders 2–4 are unconditionally stable for $\kappa=10^{-1}$,
  $\kappa_{\mathrm s}=1$; for $\kappa=10^{-2}$ generalized eigenvalues
  $-0.4875\pm3.4130\,\mathrm i$ leave the unconditional stability diagram, the
  second-order method is unstable at step 0.5, and $\kappa_{\mathrm s}=3$ restores
  unconditional stability. With the constant matrix the methods beat Rosenbrock methods
  of the same order with the exact Jacobian in error against CPU time at $\kappa=10^{-1}$
  (Conte et al. (2024), §7.1, Figs. 7–8). See [TASE operators](/methods/tase-operators.md).
* **ADER.** With spectral-difference space discretizations, ADER reaches
  design orders 3–9 on Burgers, and a final flux-integral update was "more
  stable" there than the predictor end value
  ([Han Veiga et al. (2021)](/sources/hanveiga-2021.md), §5.3.1; see
  [ADER](/methods/ader-time-integration.md)).

## Qualifications

* Biswas et al. (2023) contrast their order-3 result with Ketcheson et al.
  (2020), who reported clean full order on the same problem for weak stage
  order up to 3, as recalled; the orders and setups differ, and the paper does
  not reconcile them.
* Kang & Constantinescu (2022) print the shock front near $x\approx-0.25$ at
  $t=1$ and a relaxed time of 0.998 in one panel labelled $t=1$ (Fig. 13(f)),
  a consequence of the relaxed step lengths.

# Citations

- [Kang & Constantinescu (2022)](/sources/kang-2022.md) — §1.2.4–1.2.5, §2 (Remark 1), Remark 3 (Eq. (11)), §3 (Eq. (3), Tables 2–4, Figs. 5–16).
- [Sun & Shu (2021)](/sources/sun-2021.md) — §6.3 (Eqs. (6.11)–(6.12), Table 6.7, Figs. 6.8–6.10).
- [Biswas et al. (2023)](/sources/biswas-2023.md) — §7.2 (Eq. (31), Fig. 11).
- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) — §5.3.1.
- [González-Tabernero et al. (2024)](/sources/gonzaleztabernero-2024.md) — §5.2, Table 2.
- [Conte et al. (2024)](/sources/conte-2024.md) — §7.1, Eqs. (7.1)–(7.3), Figs. 7–8.
