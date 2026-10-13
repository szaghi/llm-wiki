---
type: Method
title: "Godunov's method"
description: "The first-order conservative scheme that solves the Riemann problem between piecewise-constant cell states at every interface and updates the cell averages with the resulting fluxes: Godunov's 1959 derivation as the best monotone scheme, his exact iterative Lagrangian solver, time step and entropy inequality, the order barrier for monotone linear schemes, the Godunov-type generalization of Harten, Lax and van Leer, and the first-order Godunov runs and fallbacks in the bundle's sources."
status: established
aliases: [Godunov scheme, Godunov's scheme, first-order Godunov, Godunov-type scheme, Godunov's theorem]
tags: [hydro, riemann-solver]
timestamp: 2026-10-13T00:00:00Z
---

# Godunov's method

**Definition.** Cell values are taken as piecewise constant. At each
interface $x_{i+1/2}$ the Riemann problem between $u^n_i$ and $u^n_{i+1}$
is solved, and the numerical flux $\hat f_{i+1/2}$ is the physical flux of
the state the solution takes on the interface. The update is conservative,
$$u_i^{n+1} = u_i^n - \frac{\Delta t}{h}\left(\hat f_{i+1/2} - \hat f_{i-1/2}\right),$$
and the new values are the cell averages of the evolved, no longer
constant, solution
([Godunov (1959)](/sources/godunov-1959.md), Ch. II §2, p. 286;
[Harten et al. (1983)](/sources/harten-1983.md), §3A, eqs. 3.3–3.4). The
method is first order. The higher-order Godunov methods of this bundle,
[PPM](/methods/ppm.md) and the
[unsplit integrators](/methods/unsplit-godunov-integrators.md), replace the
constant states by reconstructed ones and the exact Riemann solution by
one of the [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).

## Origin: the best monotone scheme

Godunov derived the method as the answer to a question about linear
schemes (Godunov 1959, Ch. I):

* **Monotonicity criterion** (§2). A linear two-level scheme maps every
  monotone grid function to a monotone one iff all its weights are
  non-negative; if they also sum to 1, it is stable in the maximum norm.
* **Order barrier** (§3), now called Godunov's theorem. For linear
  advection there is no linear two-level scheme of second order (exact on
  quadratics), explicit or implicit and on any stencil, that keeps all
  monotone data monotone when the Courant number $\nu$ is not an integer.
  Schemes with more than two time levels are excluded from the statement.
* **Best monotone scheme** (§2, §4). Among first-order three-point schemes
  the closest to second order with non-negative weights is upwind (for
  wave speed $-1$, $u^{n+1}_i = \nu\,u^n_{i+1} + (1 - \nu)\,u^n_i$,
  $\nu \le 1$). Applied to each Riemann invariant of linear acoustics it
  gives a scheme whose interface pressure and velocity are exactly those
  between the two acoustic waves into which the interface discontinuity
  decays (§5, eqs. 7–8): the Riemann problem appears as an interpretation
  of the best monotone scheme, and is then carried over to the nonlinear
  equations.

## The original scheme: 1D Lagrangian gas dynamics

* **Equations.** Godunov's nonlinear scheme is for the 1D Lagrangian
  Euler equations; Eulerian interface positions are only advanced
  afterwards with the interface velocity (Godunov 1959, Ch. II §§1, 5).
  [Sod (1978)](/sources/sod-1978.md) (§2, p. 7) likewise describes the
  Riemann-solver Godunov method only in Lagrangian form.
* **Riemann solver.** Exact for an ideal gas: the interface pressure is a
  mean of the two pressures weighted by the Lagrangian wave speeds, each
  speed taken from a shock branch (Hugoniot adiabat) or a rarefaction
  branch (adiabat and Riemann invariant) according to whether the iterate
  exceeds that side's pressure; plain fixed-point iteration, with a
  relaxed variant for very strong rarefactions (Ch. II §4, pp. 287–292).
  It is the iteration that Sod uses "as modified by Chorin" (Sod 1978,
  §2, eqs. 12–19). See the batch-9 section of the
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
* **Time step.** $\Delta t$ at most $h$ over the largest Lagrangian wave
  speed, taken as an approximation of the time before waves from
  neighbouring interfaces interact and justified by stable runs (Ch. II
  §4, p. 292). Harten et al. (1983) separate the two conditions: the
  Riemann problems do not interact if $\nu < \tfrac12$, but the
  conservative form stays consistent with the averaged solution under
  $\nu \le 1$ (§3A, p. 45). Sod's finite-difference Godunov variant runs
  at $\nu \le 1$ (Sod 1978, Table I).
* **Weak solutions and entropy.** Convergent limits satisfy the integral
  conservation laws (Godunov 1959, Ch. II §3), and the cell-average
  entropy does not decrease in a step, so limits satisfy the entropy
  inequality (Ch. II §4, eq. 9). Harten et al. (1983) prove the entropy
  inequality of Godunov's scheme via Jensen's inequality and extend the
  Lax–Wendroff theorem so that convergent limits of any
  entropy-consistent conservative scheme are entropy weak solutions
  (§1, Thm. 1.1; §3A, p. 45).
* **Contacts between two gases.** A linearized analysis shows a jump in
  the extrapolated velocity and pressure at a material interface,
  proportional to the difference between the two sides' maximal stable
  time steps; choosing the cell sizes so that these agree almost removes
  it (Godunov 1959, Ch. II §7, eq. 16, p. 300). Stability at such
  contacts is proved for Courant numbers below 1 on each side (§8).

## Properties stated in the sources

* For linear systems Godunov's method is the upwind scheme, the flux being
  the positive part of $A$ applied to the left state plus its negative
  part applied to the right (Harten et al. 1983, §3A, eqs. 3.5–3.6).
* The Godunov flux is continuous but only piecewise differentiable
  (Harten et al. 1983, p. 46).
* **Godunov-type schemes** (Harten et al. 1983, §3A, Thm. 3.1). A scheme
  built from an approximate Riemann solution that is consistent with the
  integral conservation law and the integral entropy inequality keeps
  the conservation and entropy properties of Godunov's scheme. Roe's
  solver and HLL are of Godunov type; Osher's scheme is not (§3B, p. 49).
  Such schemes extend to grids moving in time, "the natural choice for
  adaptive grids" (p. 49).

## First-order Godunov in the bundle's runs

* **Start-up and stationary shocks.** In Godunov's own runs a stationary
  shock profile forms within a few steps and moves with the correct
  jumps, leaving an **entropy trace** of two to three points where the
  start-up "erred in entropy" (Godunov 1959, §6, Appendix II); a
  second-order linear scheme gives humped, oscillating shocks
  (Appendix I).
* **Sod shock tube.** Sod ran Godunov's scheme in the finite-difference
  form of Godunov, Zabrodin & Prokopov for the Eulerian equations, with no
  Riemann solver: contact 7–8 and shock 5–6 zones wide, 3–4 and 1–2 with
  Harten's artificial compression (Sod 1978, §2, Table I, Figs. 4–5; see
  [Sod shock tube](/benchmarks/sod-shock-tube.md)).
* **Nearly stationary strong shock.** A first-order single-step Godunov
  run (pressure jump over six orders, nearly 8000 steps across 160 zones)
  leaves a 3 % error immediately behind the shock, which flattening cannot
  cure; 6 Riemann iterations are used, and 2 give "very large errors"
  ([Colella & Woodward (1984)](/sources/colella-1984.md), §4, Fig. 8).
* **Fallback inside higher-order schemes.** PPM's flattening coefficient
  equal to 1 makes a zone locally Godunov's first-order method (Colella &
  Woodward 1984, §4, p. 192; see [PPM](/methods/ppm.md)).
* **Interacting blast waves.** First-order Godunov has the largest $L_1$
  density error of the seven schemes compared, 0.330 at 200 zones and
  0.182 at 1200 (finest-pair rate 0.40, Table I), and cannot match the
  accuracy of 200-zone PPMLR "even if it is given twelve times as many
  zones" (p. 146); on the Mach 3 wind-tunnel step an unphysical
  rarefaction shock forms in the centred fan where the flow is sonic,
  because the flux error at a sonic interface "is one order smaller than
  everywhere else" (p. 157)
  ([Woodward & Colella (1984)](/sources/woodward-1984.md); see
  [interacting blast waves](/benchmarks/interacting-blast-waves.md)).

# Citations

1. [Godunov (1959)](/sources/godunov-1959.md), Ch. I §§1–5, Ch. II §§1–8, Appendices I–III.
2. [Harten et al. (1983)](/sources/harten-1983.md), §1, Thm. 1.1, §3A–3B, eqs. 3.3–3.6, Thm. 3.1.
3. [Sod (1978)](/sources/sod-1978.md), §2, Table I, Figs. 4–5.
4. [Colella & Woodward (1984)](/sources/colella-1984.md), §4, Fig. 8, p. 192.
5. [Woodward & Colella (1984)](/sources/woodward-1984.md), Table I, pp. 146, 157.
