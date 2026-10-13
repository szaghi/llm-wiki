---
type: Result
title: "Godunov's order barrier for monotone linear schemes"
description: "A linear two-level scheme keeps monotone data monotone iff all its coefficients are nonnegative, and no such scheme for linear advection is second order unless the Courant number is an integer; with Harten's chain monotone ⇒ TVD ⇒ monotonicity preserving, a linear TVD scheme is first order, so every higher-order capturing scheme must be nonlinear."
status: established
aliases: [Godunov's theorem, Godunov barrier, Godunov's order barrier, linear monotone schemes are first order]
tags: [impossibility, monotonicity, tvd, stability]
timestamp: 2026-10-13T00:00:00Z
---

# Godunov's order barrier for monotone linear schemes

## Godunov's statement

**Setting** ([Godunov (1959)](/sources/godunov-1959.md), Ch. I §§2–3).
Linear, constant-coefficient, two-level schemes for the scalar advection
equation $\partial_t u = \partial_x u$, explicit or implicit, on a
stencil of any width. An implicit scheme whose implicit coefficients form a
polynomial with no roots of modulus 1 is uniquely solvable in bounded sequences, so
every such scheme can be written explicitly, each $u^{n+1}_i$ a fixed
linear combination (possibly infinite) of the $u^n_j$. Godunov calls a
scheme monotone when it maps every monotone grid function to a monotone
grid function with the same direction of growth.

**Monotonicity criterion** (§2). A linear scheme is monotone in this
sense iff all coefficients of the combination are nonnegative. The new
differences $\Delta^1 u^{n+1}_i$ are the same combination of the old
differences, which gives sufficiency; a unit step placed at a negative
coefficient gives necessity. Nonnegative coefficients that sum to 1
(constants reproduced) also give max-norm stability.

**The barrier** (§3). When $\nu \neq 0, 1, 2, \dots$, no linear
two-level scheme for $\partial_t u = \partial_x u$ that maps all monotone
functions to monotone functions is second order. Second order is
*defined* as exactness on quadratic data. Proof: the datum
$u(x) = (x/h - \tfrac12)^2 - \tfrac14$ has nonnegative samples
$(j - \tfrac12)^2 - \tfrac14$ at every integer $j$. An exact scheme
returns $(l + \nu - \tfrac12)^2 - \tfrac14$ at node $l$, which is negative
at the integer $l$ with $l - 1 < -\nu < l$; a scheme with nonnegative
coefficients cannot produce a negative value from nonnegative data. The
test datum is not itself monotone: the proof goes through the
coefficient criterion.

**Three-point illustration** (§§1–2). The unique second-order
three-point scheme (Lax–Wendroff form, Godunov's "tripod") turns a unit
step into the value $1 + \tfrac12(\nu - \nu^2) > 1$: an overshoot. Among
the first-order three-point schemes, the one closest to second order with
all coefficients nonnegative is upwind,
$u^{n+1}_i = \nu u^n_{i+1} + (1 - \nu)u^n_i$ for $\nu \le 1$. Godunov
builds [his method](/methods/godunov-method.md) on this scheme and its
Riemann-problem reading.

## Harten's chain

[Harten (1983)](/sources/harten-1983.md), §2, places the barrier in the
hierarchy of nonlinear stability notions.
* **Definitions.** A scheme is *monotonicity preserving* if monotone mesh
  functions stay monotone (Godunov's "monotone"); *monotone* if each new
  value is a nondecreasing function of every old value it depends on;
  *TVNI* if $TV(u^{n+1}) \le TV(u^n)$ for all data of bounded variation
  ([TVD](/properties/total-variation-diminishing.md)).
* **Theorem 2.1.** Monotone ⇒ TVD ⇒ monotonicity preserving. Monotone
  schemes are $l_1$-contractive, which gives the first implication; a
  monotone step profile gives the second.
* **Linear case** (eq. 2.8, citing Godunov). A linear scheme is
  monotonicity preserving iff all its coefficients are nonnegative, so
  for linear schemes the three notions coincide: "any *linear*
  monotonicity-preserving scheme, and therefore any TVNI linear scheme,
  is a monotone scheme and consequently first order accurate".
* **Monotone schemes in general** are first order by their modified
  equation, which carries a nonnegative, not identically zero diffusion
  coefficient (eq. 2.7) ([monotone numerical flux](/definitions/monotone-flux.md)).
* **The way out.** None of this excludes *nonlinear* second-order TVD or
  monotonicity-preserving schemes, which are then not monotone. Harten
  builds such schemes by a limited, solution-dependent antidiffusive flux
  (§3).

Godunov's "monotone" is therefore Harten's "monotonicity preserving";
the two meanings of *monotone* agree only for linear schemes.

## How the bundle uses it

* **Why capturing schemes are nonlinear.** The higher-order schemes of
  this bundle control oscillations at discontinuities with devices that
  are nonlinear in the data: TVD limiters, ENO stencil choice, WENO weights,
  monotonicity-preserving bounds
  ([TVD](/properties/total-variation-diminishing.md), "What replaced
  it"; [Harten (1983)](/sources/harten-1983.md), §2).
* **A separate, later barrier.** That nonlinear TVD schemes are first
  order at smooth extrema ([Harten et al. (1987)](/sources/harten-1987.md);
  [Shu & Osher (1988)](/sources/shu-1988.md)) is a different result about
  nonlinear schemes, not a consequence of Godunov's theorem. Harten
  (1983) already observes that his second-order scheme "may degenerate
  locally" at extrema (Remark 2).
* **DG still needs limiting.** The cell entropy inequality gives DG
  $L^2$ stability for any degree, but limiting is still required, by
  Godunov's theorem ([Dumbser et al. (2014)](/sources/dumbser-2014.md),
  §§1–2; [a posteriori subcell limiting](/methods/a-posteriori-subcell-limiting.md)).
  The a posteriori cascade ends in a first-order Godunov update,
  "supposed" monotone under its CFL condition (same source, §4.1).

# Citations

1. [Godunov (1959)](/sources/godunov-1959.md), Ch. I §§1–3 (pp. 272–278; reader's translation of the Russian original).
2. [Harten (1983)](/sources/harten-1983.md), §2 (Theorem 2.1, eqs. 2.6–2.8), §3 Remark 2.
3. [Harten et al. (1987)](/sources/harten-1987.md), §2.
4. [Shu & Osher (1988)](/sources/shu-1988.md), §I.
5. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §§1–2, 4.1.
