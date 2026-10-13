---
type: Property
title: "Total variation diminishing (TVD)"
description: "A scheme is TVD (Harten's TVNI) when the total variation of the discrete solution never increases; Harten's lemma gives a sufficient incremental-form condition, linear TVD schemes are first order, and the second-order nonlinear constructions are proved TVD only for scalar or constant-coefficient problems."
status: established
aliases: [TVD, TVNI, total variation nonincreasing, Harten's lemma]
tags: [tvd, shock-capturing, stability, invariant]
timestamp: 2026-10-13T00:00:00Z
---

# Total variation diminishing (TVD)

The **total variation** of a 1D grid function $w_j$ ([notation](/notation.md))
is the sum over $j$ of $|w_{j+1} - w_j|$. A scheme is **total variation
nonincreasing** (TVNI) if one step never increases it. The term and the
definition are [Harten (1983)](/sources/harten-1983.md)'s (§2,
eqs. 2.4–2.5); he writes TVNI throughout and never "TVD", the name later
papers use. Like the [exact discrete divergence](/properties/exact-discrete-divergence.md),
it is a statement about the scheme's algebra, but an inequality, not an
identity, and it bounds a seminorm of each scalar component rather than
holding a constraint on a field.

## Hierarchy

Harten (1983, Theorem 2.1, p. 360): monotone schemes are TVNI, and TVNI
schemes are monotonicity preserving. Monotone schemes are at most first
order (eq. 2.7). A *linear* monotonicity-preserving scheme has nonnegative
coefficients (eq. 2.8b, after Godunov), so a linear TVNI scheme is first
order (p. 361). Second order therefore requires a **nonlinear** scheme:
the limiter.

## Harten's lemma

(Harten 1983, Lemma 2.2, p. 362.) Write one step in incremental form: the
new value is the old value, plus a coefficient times the forward
difference at $j+1/2$, minus a coefficient times the backward difference
at $j-1/2$ (eq. 2.9b). If both coefficients are nonnegative at every face
(eq. 2.10a), and their sum at each face is at most one (eq. 2.10b), the
scheme is TVNI. The proof differences the update, takes absolute values,
and re-indexes the sum. Any 3-point conservative scheme with a
differentiable flux can be written this way by the mean value theorem
(eq. 2.13).

## Second order under the first-order CFL limit

Harten's construction ([Harten (1983)](/sources/harten-1983.md), §3)
applies a 3-point first-order TVNI scheme, whose numerical viscosity is a
function of the local Courant number bounded between its absolute value
and one, to a **modified flux**: the physical flux plus a correction equal
to a minmod-limited approximation of the first-order scheme's own
diffusion term. The 5-point result is second order (Lemmas 3.2–3.3) and
TVNI under **the same CFL restriction** as the first-order scheme
(Lemma 3.4). Accuracy drops locally to first order at extrema (Remark 2,
p. 368).

## Scope of the proofs

* **Scalar**: TVNI and convergence are proved in the constant-coefficient
  case; the nonlinear scalar case would also need entropy consistency,
  which is not proved (Harten 1983, Remark 1, §3).
* **Systems**: the scheme is applied field by field to a characteristic
  decomposition at an average state ([Roe's solver](/methods/roe-solver.md)).
  It is TVNI, for the total variation summed over the characteristic wave
  strengths, **only for a constant Jacobian** (Lemma 4.2). For nonlinear
  systems Harten has no TV estimate and "cannot prove convergence"
  (Remark 3, p. 373).

Harten's proofs therefore do not cover the nonlinear seven-wave MHD
system to which the bundle's TVD codes apply his characteristic-wise
scheme.

**Asserted, not proved, in a MUSCL-type MHD code.** [Balsara (1998)](/sources/balsara-1998-b.md) states that TVD "is already guaranteed by our choice of interpolation and Riemann solver" (§4, p. 137), with no proof for the MHD system. His fourth-order hyperviscosity is switched off where the largest characteristic switch exceeds 0.5 (eq. 4.11), after Swanson & Turkel (1992), to avoid damaging TVD.

## Uses in the bundle

* **Harten-TVD MHD codes.** [Ryu & Jones (1995)](/sources/ryu-jones-1995.md)
  use Harten's ULT1 flux (Harten eqs. 7.1b, 7.2) and his entropy fix with
  per-family widths; [Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md)
  Strang-split it in several dimensions, and
  [Ryu et al. (1998)](/sources/ryu-1998.md) add staggered
  [constrained transport](/methods/constrained-transport.md).
  [Brio & Wu (1988)](/sources/brio-wu-1988.md) reach second order "by
  Harten's approach".
* **TVD time stepping.** The third-order TVD Runge–Kutta scheme of Shu &
  Osher, used with [WENO](/methods/weno.md) by
  [Jiang & Shu (1996)](/sources/jiang-shu-1996.md), carries the TV bound of
  a forward-Euler step to the full step under a reduced CFL number
  ([Shu & Osher (1988)](/sources/shu-osher-1988.md), Proposition 2.1).
* **TVD reconstruction of the field.** Balsara's divergence-free
  reconstruction reduces to standard TVD reconstruction under 1D variation
  ([divergence-free reconstruction](/methods/divergence-free-reconstruction.md);
  [Balsara (2001)](/sources/balsara-2001.md),
  [Balsara (2004)](/sources/balsara-2004.md)).

# Citations

1. [Harten (1983)](/sources/harten-1983.md), §§2–4, eqs. 2.4–2.13, 3.1–3.12, Lemmas 2.2, 3.1–3.4, 4.2.
2. [Ryu & Jones (1995)](/sources/ryu-jones-1995.md), §2.3, eqs. 2.87–2.95.
3. [Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md), §2.2.
4. [Ryu et al. (1998)](/sources/ryu-1998.md).
5. [Brio & Wu (1988)](/sources/brio-wu-1988.md), §III.
6. [Jiang & Shu (1996)](/sources/jiang-shu-1996.md), §1, eqs. 1.2–1.4.
7. [Shu & Osher (1988)](/sources/shu-osher-1988.md), §II, Proposition 2.1.
8. [Balsara (2001)](/sources/balsara-2001.md); [Balsara (2004)](/sources/balsara-2004.md).
9. [Balsara (1998)](/sources/balsara-1998-b.md), §4.
