---
type: Method
title: "Quinpi — implicit CWENO time stepping"
description: "Quinpi is an implicit finite-volume framework that freezes CWENO weights on a first-order implicit predictor, integrates with a diagonally implicit Runge–Kutta method, limits in time by a CWENO-type blend with the predictor and restores conservation by an interface correction; its scalar third-order version Q3P1 converges at third order for time steps of one and ten cell widths."
status: established
aliases: [Quinpi, CWENO implicit, Q3P1, D3P1, implicit CWENO, predictor-based nonlinear weights]
tags: [cweno, finite-volume, reconstruction, limiting]
timestamp: 2026-10-22T04:49:00Z
---

# Quinpi — implicit CWENO time stepping

**Quinpi** ("CWENO Implicit") of [Puppo et al. (2023)](/sources/puppo-2023.md) is a
framework for high-order *implicit* finite-volume integration of
$\partial_tu+\partial_xf(u)=0$, aimed at stiff problems (low-Mach gas dynamics, kinetic
and relaxation systems) where the explicit time step set by the fastest waves is
needlessly small. It addresses the three nonlinearities of a high-order implicit scheme
(after Arbogast et al.): the flux, the nonlinear weights of the reconstruction, and the
limiting in time that a high-order Runge–Kutta step needs because it is itself a
polynomial reconstruction in time. The published instance, **Q3P1**, is third order, 1D
and scalar; systems, BDF and higher orders are left to future work (§5).

## Design

The design principles are stated in §2–§3 (p. 6–7): unconditional stability from a
diagonally implicit Runge–Kutta (DIRK) method; space limiting per implicit Euler stage,
since a Runge–Kutta step is a combination of Euler steps; removal of the
reconstruction's nonlinearity by a first-order predictor; and limiting in time by
blending the accurate solution with that predictor, *without* coupling space and time
limiting, which is what distinguishes it from Duraisamy–Baeder(–Liu) and Arbogast et al.

The motivation is the TVD analysis of §2 (see
[TVD](/definitions/total-variation-diminishing.md)): the implicit Euler step with a TVD
limiter is TVD for every $\Delta t/\Delta x$ under exactly the explicit limiter
conditions, and the limiter may be computed from any at least first-order
approximation of $u(x,t^{n+1})$.

## The three bricks of Q3P1

Semi-discretization: cell averages $\bar u_i$, global
[Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) with $a=\max_u\lvert f'(u)\rvert$
(Eq. (14)), third-order [CWENO](/methods/cweno.md) reconstruction of Levy, Puppo and
Russo with two linear and one central polynomial, Jiang–Shu
[smoothness indicators](/definitions/smoothness-indicator.md), $\epsilon=\Delta x^2$,
exponent $q=2$ (§3.1, Eqs. (5)–(13)); the linear weights used are not stated.

1. **Predictor (IE).** A composite backward-Euler step with piecewise-constant
   reconstruction, one sub-step for each ordered DIRK abscissa; it is equivalent to a
   DIRK with tableau (19), first order, stable and non-oscillatory, and gives first-order
   values $\bar u^{\mathrm{IE},(k)}$ at every stage (§3.3.1, Eqs. (19)–(20)). Its stage
   systems are nonlinear only through $f$ and are solved by Newton.
2. **Corrector (D3P1).** The three-stage, third-order, L-stable DIRK of Alexander with
   CWENO3 whose nonlinear weights at stage $k$ are computed from $\bar u^{\mathrm{IE},(k)}$
   (§3.3.2). With the weights frozen, the interface values are linear in the unknowns,
   $u^-_{i+1/2}=\sum_{l=-1}^1W^-_{i,l}\bar u_{i+l}$ with coefficients depending only on
   the predictor (Eq. (21); page-local $W^\pm$). For a linear conservation law a step is a
   sequence of narrow-banded linear systems, for nonlinear $f$ the systems are nonlinear
   only through $f$. The DIRK is stiffly accurate, with diagonal
   $\lambda_{\mathrm D}=0.4358665215$ (page-local; tableau (18)). D3P1 is third order on
   smooth data but can oscillate, being unlimited in time.
3. **Blending in time and conservative correction (Q3P1).** With the continuous
   extensions of the DIRK and of the predictor, the cell value at $t^{n+1}$ is blended in
   CWENO form (§3.3.3, Eqs. (22)–(27)):

   $$u^{\mathrm B,n+1}_i=\frac{\omega^{\mathrm H}_i}{d^t_{\mathrm H}}\big(u^{\mathrm{D3P1},n+1}_i-d^t_{\mathrm L}u^{\mathrm{IE},n+1}_i\big)+\omega^{\mathrm L}_iu^{\mathrm{IE},n+1}_i,$$

   with linear weights $d^t_{\mathrm L}+d^t_{\mathrm H}=1$ (page-local, the superscript $t$ keeping them apart from the CWENO weights $d_k$) and nonlinear weights
   $\omega^{\mathrm L}_i\propto d^t_{\mathrm L}/\epsilon_t^2$,
   $\omega^{\mathrm H}_i\propto d^t_{\mathrm H}/(\epsilon_t+\beta^{\mathrm{st}}_i)^2$,
   $\epsilon_t=\Delta t^2$ (page-local: $\omega^{\mathrm L},\omega^{\mathrm H}$ the time-blending
   weights, $\beta^{\mathrm{st}}_i$ a space–time smoothness indicator: the Jiang–Shu
   indicator of the DIRK's continuous extension in time plus squared differences of the
   D3P1 stage values with both neighbours). Citing Semplice and Visconti, a third-order
   time-limited solution needs $d^t_{\mathrm L}=\Delta t^2$; the tests use
   $d^t_{\mathrm H}=1-\Delta t^2$. The blend is not conservative: the interface mass defect is
   redistributed to the two neighbours in proportion to their high-order weights, which
   yields a conservative scheme with an explicit interface flux in which the high-order
   flux is weighted by the harmonic mean
   $2\omega^{\mathrm H}_i\omega^{\mathrm H}_{i+1}/(\omega^{\mathrm H}_i+\omega^{\mathrm H}_{i+1})$
   (§3.3.4, Eqs. (28)–(32)); the high-order flux counts only where both neighbours are
   detected smooth. See [local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md).

Quinpi differs from the flux-implicit WENO of Gottlieb, Mullen and Ruuth, which computes
the weights from an explicit predictor in a single step: here the predictor is implicit,
evaluated at each DIRK abscissa, and doubles as the low-order fallback of the time
limiting (§3.3).

## Evidence

All tests are scalar 1D (§4); the time step is quoted as a multiple of $\Delta x$, which
with $\max\lvert f'\rvert\approx1$ is approximately the CFL number.

- **Accuracy** (Burgers, $u_0=0.5-0.25\sin\pi x$ on $[0,2]$, $t=1$; Table 1). Third order
  in $L^1$ and $L^\infty$: at $\Delta t=\Delta x$, $N_x=2560$, $L^1$ error
  $3.66\times10^{-7}$, rates 2.99/2.98; at $\Delta t=10\Delta x$, $N_x=5120$,
  $1.29\times10^{-7}$, 2.99/2.98; at $\Delta t=50\Delta x$, $N_x=5120$,
  $1.41\times10^{-5}$, 2.79/2.52. IE is first and D3P1 third order (Fig. 1). The
  authors state smaller errors than Arbogast et al. at large CFL on the same grid,
  without reproducing their numbers.
- **Discontinuous transport** (400 cells, $\Delta t=3\Delta x,5\Delta x$, one period):
  IE very diffusive, D3P1 oscillates, Q3P1 much less diffusive than IE without spurious
  oscillations (Fig. 2); on a top-hat at $\Delta t=5\Delta x$ residual oscillations remain,
  with higher frequency and slightly lower amplitude on finer grids (Fig. 3).
- **Burgers shocks**: shock formation (256 cells; a non-limited DIRK with linear CWENO
  weights oscillates strongly even at moderate CFL, Figs. 4–5), shock interaction
  ($\Delta t=5\Delta x$, Fig. 9), and the conservative correction (Fig. 7, see above). An
  explicit first-order predictor, even evaluated at each abscissa, does not prevent
  oscillations at $\Delta t=5\Delta x$ (Fig. 8).
- **Buckley–Leverett** (100 cells, $\Delta t=1.1\Delta x,4.4\Delta x$, $\epsilon_t=\Delta t^3$):
  at large CFL Q3P1 avoids the overshoots of D3P1 (Fig. 10). See
  [Buckley–Leverett problem](/benchmarks/buckley-leverett-problem.md) and
  [Burgers equation tests](/benchmarks/burgers-equation-tests.md).
- **Cost** (Intel Core i7-6600U; Table 2): one Q3P1 step costs 2.5–3.1 explicit
  [SSP-RK3](/methods/ssp-runge-kutta.md) steps on linear transport and 3.5–6.0 on Burgers;
  six Newton solves per step on nonlinear problems, with at most two to three iterations
  each (Fig. 11).

## Qualifications

- Non-oscillation at large CFL is shown numerically, not proved; Q3P1 claims no SSP or
  TVD property for the high-order step, and Fig. 3 shows residual oscillations.
- *(Compiler check, not in the sources: under $u\mapsto\sigma u$ the indicator
  $\beta^{\mathrm{st}}_i$ scales by $\sigma^2$ while $\epsilon_t=\Delta t^2$ and
  $d^t_{\mathrm L}=\Delta t^2$ do not, so the time-blending weights depend on the scale of
  $u$; they also depend on the unit of $t$ through $\Delta t^2$.)*
- Printed slips in the version read: Eq. (20) contains the term
  $-\tfrac a2\bar u^{\mathrm{IE},(k)}_{i+1}$ twice, where the Lax–Friedrichs stencil needs one
  of them at $i-1$; Table 2(a), $N=1600$, prints an SSP-RK3 time of 0.095 with ratio 3.08,
  which needs 0.0095; the Fig. 7 caption gives $t=5$ for a run to $t=0.5$; the
  Buckley–Leverett step is printed on $[-0.25,0.25]$ for the periodic domain $[0,1]$.

# Citations

- [Puppo et al. (2023)](/sources/puppo-2023.md) — §2 (TVD bounds), §3.1 (Eqs. (5)–(13), (21)), §3.3 (Eqs. (14)–(32)), §4 (Tables 1–2, Figs. 1–11), §5 (arXiv v2).
