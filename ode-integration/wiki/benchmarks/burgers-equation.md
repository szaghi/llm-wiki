---
type: Benchmark
title: "Burgers equation"
description: "Inviscid Burgers u_t + (u²/2)_x = 0 and viscous Burgers with manufactured or periodic solutions; the sources use it to test relaxation, superviscosity filtering, IMEX and multirate entropy behaviour, order reduction from boundary data, TASE stability, bound-preserving and invariant-domain-preserving limiting, single-stage Lax–Wendroff and multiderivative schemes, asynchronous low-storage Runge–Kutta and Parareal; one source proves a cell entropy inequality on it."
status: established
aliases: [inviscid Burgers equation, viscous Burgers equation, Bateman–Burgers equation]
tags: [structure-preserving, order-reduction, verification, stiff]
timestamp: 2026-10-20T14:00:00Z
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
* **Nonlinear partition with frozen diffusion coefficient.** For Burgers with
  nonlinear diffusion, $u_t=\kappa(x)(\lvert u\rvert^{1/2}u_x)_x+w(x)(u^2)_x$
  (the viscosity $\kappa$ now a function of $x$; page-local advection coefficient $w(x)$), the partition
  $F(u,v)=\kappa(x)(\lvert v\rvert^{1/2}u_x)_x+w(x)(v^2)_x$ is linear in its
  implicit argument $u$: advection (fifth-order WENO) is explicit, the diffusion
  is semi-implicit with its coefficient frozen at $v$, and every implicit stage is
  a linear solve, whereas an additive partition would need nonlinear solves and a
  component partition an implicit WENO
  ([Buvoli et al. (2026)](/sources/buvoli-2026.md), §4.1, Eqs. (4.1)–(4.4); see
  [nonlinearly partitioned Runge–Kutta](/methods/nonlinearly-partitioned-runge-kutta.md)).

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
* **Nonlinear diffusion with spatially varying coefficients** (Buvoli et al.
  (2026), §4, Eqs. (4.1), (4.6)–(4.7)): $\kappa(x)=\tfrac12+2e^{-(x-1)^2/25}$,
  $w(x)=e^{-(x+1)^2/25}$ on $[-2,2]$, periodic, 300 points, final time $t=5$
  (§4.4 prints $t=6$, while §4 and Fig. 4 give 5). Two initial data:
  $u_0=\tfrac1{100}+e^{-60(x+3/2)^2}+e^{-60x^2}$, and the same plus a third
  pulse $e^{-60(x-3/2)^2}$ placed in the diffusive region. The pulses advect
  leftward, steepen into shocks and cross the diffusive right half.

* **Pre- and post-shock periodic data** ([Kuzmin et al. (2022)](/sources/kuzmin-2022.md),
  §5.3): $u_0=\tfrac12+\sin x$ on $(0,2\pi)$, periodic, shock at $t=1$; convergence at
  $t=0.5$ on 25 to 800 cells (Table 4) and shock capturing at $t=2$ on 100 cells (Fig. 3);
  fifth-order WENO finite volumes, $h=0.4\Delta x/(1+\gamma)$ ($\gamma$ the limiter's
  relaxation parameter, page-local).
* **Small-amplitude sine** ([Babbar et al. (2022)](/sources/babbar-2022.md), §8.3, Figs.
  18–20): $u_0=0.2\sin x$ on $[0,2\pi]$, periodic, shock at $x=\pi$ at $t=5$; errors at $t=2$,
  solutions at $t=2$, 4.5 and 8 with degree 3 on 100 cells and a TVB limiter; flux
  reconstruction with Lax–Wendroff or Runge–Kutta time stepping. A 2D version
  $u_t+(u^2/2)_x+(u^2/2)_y=0$ with $u_0=\tfrac14+\tfrac12\sin(2\pi(x+y))$, errors at $t=0.1$
  and the shock at $t=0.2$ (§11, Figs. 35–36).
* **Cosine and exponential data** ([Chouchoulis et al. (2022)](/sources/chouchoulis-2022.md),
  §6.1, Eq. 23, Figs. 2–3): $u_0=\tfrac14\cos\pi x$ on $[0,2]$, periodic, breaking time
  $4/\pi$, $T=0.8$; and $u_0=\tfrac14e^{\cos\pi x+\sin\pi x}$, breaking time $4/(\pi e)$,
  $T=0.3$; Courant number $\nu=0.5$, exact solutions by characteristics, meshes from 8 cells
  doubling.
* **Viscous, discontinuous data, Dirichlet** ([Jin et al. (2025)](/sources/jin-2025.md),
  Example 4.3): $u_t+uu_x=\kappa u_{xx}$ on $(0,1)$, $u=0$ at both ends, $u_0$ the indicator of
  $(0,\tfrac12)$, $T=1$, $\kappa=1$ and $0.02$; fine step $1/2000$ or $10^{-4}$, ratios of
  fine to coarse steps 10 to 100; the spatial discretization is not stated.
* **Viscous, square pulse, periodic** ([Quezada de Luna & Ketcheson (2022)](/sources/quezadadeluna-2022.md),
  §8.2, Eq. (36)): $\kappa=0.01$ on $[-1,1]$, $u_0=2$ for $\lvert x\rvert<\tfrac12$ and 0
  otherwise, $t=0.25$, 200 and 400 cells, global bounds $[0,2]$; WENO5 finite volumes with a
  five-stage fifth-order SDIRK, limited in space and time around a backward Euler low-order
  scheme.
* **2D inviscid, square data** ([Ern & Guermond (2022)](/sources/ern-2022.md), §4.4.2,
  Eqs. (45)–(46), from Guermond and Popov, as recalled):
  $\partial_tu+\nabla\cdot\big(\tfrac12(u^2,u^2)\big)=0$ on $(-0.25,1.75)^2$, $u_0=1$ on a square
  and $-a$ elsewhere (page-local $a>0$; see Qualifications), invariant domain $[-a,1]$, exact
  solution available; "many sonic points", which defeat schemes with too little low-order or
  too little high-order viscosity; $T=0.65$, continuous $\mathbb P_1$ finite elements on
  uniform meshes.
* **3D viscous vector Burgers turbulence** ([Goswami et al. (2023)](/sources/goswami-2023.md),
  §5.1): $\partial_tu_i+u_j\partial_ju_i=\kappa\,\partial_j\partial_ju_i$ in a periodic box from
  random-phase sinusoidal modes, fourth- and sixth-order finite differences with low-storage
  Runge–Kutta, an MPI solver on up to 27,000 cores; $\kappa$ and the box size are not printed.

## Analysis on Burgers without experiments

[Wei & Shu (2026)](/sources/wei-2026.md) use inviscid Burgers as the model problem of a
proof, with no numerical experiments. For DG of degree 2 and 3 with the global
Lax–Friedrichs flux on arbitrary non-uniform meshes, and for every explicit three-stage
third-order Runge–Kutta method with $c_3=a_{31}+a_{32}=1$ and positive weights (the
one-parameter family $a_{21}\in(\tfrac13,\tfrac23)$, which contains Kutta's method at
$a_{21}=\tfrac12$ but not SSPRK(3,3)), they prove a fully discrete *cell* square-entropy
inequality under a CFL condition $h\le C\Delta x/\max\lvert u\rvert$, with $C$ depending only
on $a_{21}$ and not computed explicitly (Thms. 3 and 5); summed over cells it gives $L^2$
stability. Their companion paper, as they recall it, shows by counterexample that SSPRK(3,3)
with degree-2 DG is not $L^2$ stable on Burgers under $h\sim\Delta x$ (§1). See
[fully discrete cell entropy inequality](/results/fully-discrete-cell-entropy-inequality.md)
and [entropy stability](/properties/entropy-stability.md).

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
* **Multirate gains depend on where the stiffness sits.** Implicitly wrapped
  multirate NPRK methods of orders 2 and 3 (one or two implicit stages around an
  SSP2 or SSP3 explicit method composed $m$ times) converge at their design orders,
  are more accurate than single-rate IMEX-NPRK at a fixed step, stay stable at
  larger steps than explicit SSP methods (which the diffusion makes unstable at
  coarse steps), and reach moderate precision about four times faster than
  single-rate NPRK, with an implicit solve priced at four function evaluations.
  With two pulses they reach nearly the accuracy of the underlying explicit
  integrator; with the third pulse inside the diffusive region the gain is much
  smaller, because the diffusion is still stepped with the macro step (Buvoli et
  al. (2026), §4.4, Fig. 4). See
  [nonlinearly partitioned Runge–Kutta](/methods/nonlinearly-partitioned-runge-kutta.md).
* **ADER.** With spectral-difference space discretizations, ADER reaches
  design orders 3–9 on Burgers, and a final flux-integral update was "more
  stable" there than the predictor end value
  ([Han Veiga et al. (2021)](/sources/hanveiga-2021.md), §5.3.1; see
  [ADER](/methods/ader-time-integration.md)).

* **Bound preservation with non-SSP Runge–Kutta.** With the global monolithic convex limiter of
  Kuzmin et al. (2022, §5.3, Table 4, Fig. 3), no limited scheme converges at the optimal rate
  for $\gamma=0$; $\gamma=1$ restores full accuracy for SSP54, Butcher's sixth-order method
  limited at the final stage, and its stagewise-limited variant, while the fifth-order
  extrapolated Euler method needs $\gamma\ge2$ (order 2.70 at 800 cells with $\gamma=1$).
  After the shock the limited SSP54 and sixth-order solutions coincide with the baselines, which
  already respect the global bounds ($\delta=1.64\times10^{-4}$). See
  [bound-preserving flux limiting](/methods/bound-preserving-flux-limiting.md) and
  [extrapolation methods](/methods/extrapolation-methods.md).
* **Face fluxes of a single-stage Lax–Wendroff scheme.** Extrapolating the interior
  time-averaged flux to the faces (AE) converges like $O(h^{N+1/2})$ at odd degree $N$, with
  errors concentrated near sonic points $f'(u)=0$, while applying the approximate Lax–Wendroff
  procedure at the faces (EA) gives $O(h^{N+1})$ at every $N$; with AE only the global
  Lax–Friedrichs flux gives optimal rates, and "the reason for this behaviour is not known at
  present" (Babbar et al. 2022, §8.3, Figs. 19–20). See
  [Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md).
* **Multiderivative schemes with approximate Taylor derivatives.** The predicted order
  $\min(2p,q)$ of Chouchoulis et al.'s MDRKCAT schemes (stencil half-width $p$, time order
  $q$, page-local) is observed on both data sets, while the underlying compact approximate
  Taylor schemes of order $2p$ with $p=4,5,6$ diverge rapidly at $\nu=0.5$ well before the
  shock forms (§6.1, Figs. 2–3). See
  [multiderivative Runge–Kutta](/methods/multiderivative-runge-kutta.md).
* **Bounds with implicit time stepping at any step.** On the viscous square pulse the
  unlimited WENO–SDIRK solution undershoots the lower bound by $2.67\times10^{-9}$ on 200 cells
  and $2.41\times10^{-5}$ on 400 cells, while the FCT and global-monolithic-convex limited
  schemes and the backward Euler low-order scheme stay within the bounds to round-off
  ($10^{-14}$–$10^{-15}$) (Quezada de Luna & Ketcheson 2022, §8.2, Fig. 2). See
  [bound-preserving flux limiting](/methods/bound-preserving-flux-limiting.md).
* **Invariant-domain preservation and the CFL number.** With invariant-domain-preserving
  limiting after each incremental stage, all explicit methods converge at $L^1$ rates
  0.60–1.05 at CFL 0.25 (the text says "close to 0.9"), as well as SSP methods (Ern & Guermond
  2022, Table 8). Sweeping CFL over $[0.05,1]$ on a $401^2$ grid, SSPRK(2,2) starts to lose
  accuracy at CFL $\gtrsim\tfrac12$ and stability at CFL $\gtrsim0.9$, SSPRK(3,3) at
  $\gtrsim\tfrac13$ and $\gtrsim0.6$, while the midpoint rule RK(2,2;1), Heun's third-order
  RK(3,3;1) and RK(4,3;1) behave properly over the whole range, and the optimally efficient
  fourth-order methods are slightly more accurate than SSPRK(5,4) (§4.4.2, Fig. 4). Their CFL
  is scaled by the number of stages, so equal CFL means equal cost. See
  [invariant-domain-preserving time stepping](/methods/invariant-domain-preserving-time-stepping.md).
* **Communication-avoiding Runge–Kutta at scale.** On the 3D turbulence problem at $512^3$
  on 4096 cores, the communication- and synchronization-avoiding variants with delayed halo
  data reproduce the decay of kinetic energy and dissipation of the synchronous solver and its
  velocity-gradient moments to about four digits (Goswami et al. 2023, §5.2, Fig. 7, Table 4);
  in strong scaling of a $240^3$ grid on 27,000 cores the communication-avoiding variant is
  4.81 times (fourth order, two-stage LSERK2) and 6.68 times (sixth order, three-stage LSERK3a)
  faster than the synchronous one, and about 2 times faster in weak scaling (Figs. 8, 10). The
  temporal order on this nonlinear problem is not measured. See
  [low-storage Runge–Kutta](/methods/low-storage-runge-kutta.md).
* **Parareal coarse propagators.** Optimized coarse propagators contract the Parareal error by
  about 0.04 per iteration for $\kappa=1$, and by about 0.06 against 0.21 for backward Euler at
  $\kappa=0.02$ with step ratio 10; at ratio 100 both converge slowly, the optimized one "still
  competitive" (Jin et al. 2025, §4.2, Figs. 4.6–4.7). Their optimization is linear, so the
  gain shrinks for small viscosity. See [Parareal](/methods/parareal.md).

## Qualifications

* Kuzmin et al. (2022, §5.1, §5.3) print the wave-speed bound as
  $\max\{u_i,u_{i+1},\dots\}$ without absolute values, although $u_0=\tfrac12+\sin x$ takes
  negative values; their Table 4a prints order "0.00" in the first row where the other tables
  print a dash.
* Babbar et al. (2022) swap the panel descriptions (b) and (c) of Fig. 19 between caption and
  text.
* Chouchoulis et al. (2022) run 3DRKCAT5-2 and 3DRKCAT7-3 at $\nu=0.5$, above their critical
  linear Courant numbers 0.4275 and 0.2300, and those schemes still converge on Burgers; the
  paper does not comment (§6.1; see
  [linear advection equation](/benchmarks/linear-advection-equation.md)).
* **Initial datum of Ern & Guermond (2022).** Eq. (46) prints $u_0=1$ where
  $\lvert x_1-\tfrac12\rvert\le1$ and $\lvert x_2-\tfrac12\rvert\le1$, a square
  $[-\tfrac12,\tfrac32]^2$ that extends beyond the domain $(-0.25,1.75)^2$ on two sides, and
  gives no value of $a$ *(compiler check, not in the source)*. The datum actually run is not
  fully specified by the paper; the colour bar of their Fig. 3 spans $[-0.75,1]$.
* Quezada de Luna & Ketcheson (2022) print Eq. (36a) without the $x$-derivative on the flux,
  and use undefined hatted face states in the wave-speed estimate of §8.2.
* Goswami et al. (2023) analyse their asynchronous stages on the linear diffusion equation
  only; on vector Burgers they verify agreement with the synchronous solver, not the order.
* Jin et al. (2025) state that a ratio "$\Delta T/\nu$ is unchanged" between their viscous and
  linear runs; no pair of their printed settings matches (§4.2, as printed).

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
- [Kuzmin et al. (2022)](/sources/kuzmin-2022.md) — §5.1, §5.3 (Table 4, Fig. 3); arXiv v2.
- [Babbar et al. (2022)](/sources/babbar-2022.md) — §8.3 (Figs. 18–20), §11 (Figs. 35–36); arXiv v1.
- [Chouchoulis et al. (2022)](/sources/chouchoulis-2022.md) — §6.1 (Eq. 23, Figs. 2–3), Table 2.
- [Jin et al. (2025)](/sources/jin-2025.md) — §4.2, Example 4.3 (Figs. 4.6–4.7); arXiv v2.
- [Buvoli et al. (2026)](/sources/buvoli-2026.md) — §4.1–4.4, Eqs. (4.1)–(4.7), Figs. 3–4.
- [Quezada de Luna & Ketcheson (2022)](/sources/quezadadeluna-2022.md) — §8.2 (Eq. (36), Fig. 2); arXiv v1.
- [Ern & Guermond (2022)](/sources/ern-2022.md) — §4.2 (Eq. (42)), §4.4.2 (Eqs. (45)–(46), Fig. 3–4, Table 8); HAL v2.
- [Goswami et al. (2023)](/sources/goswami-2023.md) — §5.1–5.2 (Figs. 7–10, Table 4).
- [Wei & Shu (2026)](/sources/wei-2026.md) — §1, §3 (Thms. 3 and 5); author manuscript, analysis only.
