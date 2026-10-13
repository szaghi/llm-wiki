---
type: Method
title: "Roe's approximate Riemann solver"
description: "Linearized Riemann solver: the exact solution of a constant-matrix problem whose matrix satisfies Property U (exact flux jump, complete eigenvectors), built for Euler from a parameter vector giving square-root-density averages; the base of the bundle's Roe-type MHD solvers, which lose the exact jump identity when they average arithmetically."
status: established
aliases: [Roe solver, Roe matrix, Roe average, Property U, Roe-type solver]
tags: [riemann-solver, godunov, shock-capturing, eigenvectors, entropy-fix]
timestamp: 2026-10-13T00:00:00Z
---

# Roe's approximate Riemann solver

[Roe (1981)](/sources/roe-1981.md) replaces the exact Riemann problem at a
cell face by the exact solution of a *linear* problem: the left and right
conserved states $U$ ([notation](/notation.md)) are kept, and the flux
Jacobian is replaced by one constant matrix depending on both states, the
**Roe matrix**. The solution is a fan of discontinuities, one per
eigenvalue $\lambda_k$ of that matrix, carrying the projections of the
jump of $U$ onto its eigenvectors (the **wave strengths**).

## Property U

The Roe matrix must satisfy four conditions (Roe 1981, p. 359):
1. it is a linear map from states to fluxes;
2. it tends to the flux Jacobian as both states tend to one state;
3. **the jump identity**: the Roe matrix times the jump of $U$ equals the
   jump of the physical flux, for any pair of states;
4. its eigenvectors are linearly independent.

Condition 3 makes the scheme conservative. Conditions 3 and 4 together
make the scheme "recognize" a shock: if the two states satisfy the
Rankine–Hugoniot relation, the shock speed is an eigenvalue, the jump lies
on one eigenvector, and the linear solution is exact (p. 360). Roe asserts
the sufficiency and necessity statements with a pointer to his conference
paper; they are not proved in the 1981 article. The obvious averages, the
mean of the two Jacobians and the Jacobian of the mean state, "in general"
fail condition 3 (p. 359).

## Constructions

* **Mean-value path** (Roe 1981, p. 361): the Jacobian integrated along the
  straight path between the two states satisfies Property U, but may lack a
  closed form or be costly.
* **Rational identities** (eqs. 6–7): an exact matrix from product and
  quotient rules for jumps, which Roe calls "far from unique", since the
  result depends on the order in which products are split.
* **Parameter vector** (eqs. 11–19): for the Euler equations every
  component of the state and fluxes is quadratic in the square root of
  density times (1, velocity, total enthalpy). Jumps of quadratic
  quantities factor exactly through arithmetic means of the parameter
  vector, which gives the **Roe averages**: velocity and total enthalpy
  weighted by the square root of density, with the sound speed recovered
  from them (eqs. 19–20). Roe calls the device one that "has so far worked
  each time that it has been tried" (p. 362).
* **Existence in general** ([Harten, Lax & van Leer (1983)](/sources/harten-lax-vanleer-1983.md),
  Theorem 2.1, Harten–Lax): any system with a convex entropy has a matrix
  with the jump identity, real eigenvalues and a complete eigenvector set,
  the product of a symmetric and a positive-definite factor in entropy
  variables.

## The flux

Roe (1981) prints only the split form: the flux difference is the sum of
$\lambda_k$ times strength times eigenvector, divided into left- and
right-moving parts by the sign of $\lambda_k$ (p. 370). The interface
flux as the central average of the two physical fluxes minus half the sum
of $|\lambda_k|$ times strength times eigenvector is the equivalent form
printed by Harten, Lax & van Leer (eq. 3.12b), who show that Roe's solver
is a Godunov-type scheme in their sense, and by
[Brio & Wu (1988)](/sources/brio-wu-1988.md) (eq. 15).
[Harten (1983)](/sources/harten-1983.md) uses the same decomposition as the
first-order member (his eq. 7.5) of a family whose second-order members are
[TVD](/properties/total-variation-diminishing.md).

## Entropy defect and fixes

* **The defect.** A sonic expansion fan is assigned wholly to one side; in
  the extreme case of equal fluxes with different states, both split parts
  vanish and an expansion shock stays (Roe 1981, pp. 370–371). Harten, Lax
  & van Leer prove the general form: with the Roe viscosity every
  stationary discontinuity is a steady solution, admissible or not
  (p. 43).
* **Roe's cure** is stated in words only: an artificial equal and opposite
  contribution to both split parts in each interval containing a sonic
  point. No formula is given.
* **Harten's entropy fix** ([Harten (1983)](/sources/harten-1983.md),
  eq. 5.4) replaces the absolute value of the local Courant number in the
  numerical viscosity by a parabola, the square over four times a width
  plus the width, inside a band of twice the width about zero. Harten
  adopts a width of 0.1 for genuinely nonlinear fields and 0 for linearly
  degenerate ones (p. 375).
  [Ryu & Jones (1995)](/sources/ryu-jones-1995.md) use this formula
  verbatim with per-family widths 0.1, 0.2, 0.1, 0.0 (fast, Alfvén, slow,
  entropy), and [Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md)
  0.3, 0.1, 0.45, 0.0, "optimized for the multi-dimensional code".

## Cost

On Sod's shock tube with a first-order upwind scheme, the Roe solver and
Godunov's exact solver agree to within $3\times10^{-4}$ in density in
the shock region (indices 72–80), and
the Roe run takes 1.09 s against 2.02 s (Roe 1981, Table I, pp. 369–370).
Harten (1983) calls the Roe average "rather expensive" and says the
arithmetic average "will do just as well" in many applications (§6,
eq. 6.4b), though all his runs use the Roe average (p. 381).

## Roe-type solvers for MHD

For ideal MHD no parameter vector is known in general.
* [Brio & Wu (1988)](/sources/brio-wu-1988.md) find an exact Roe matrix
  only for $\gamma = 2$. For general $\gamma$ they evaluate the Jacobian at
  an arithmetic average, which keeps hyperbolicity and consistency but
  loses condition 3, so "stationary discontinuities are no longer steady
  solutions". At $\gamma = 2$ the exact and arithmetic variants agree to
  four significant digits in constant states.
* [Ryu & Jones (1995)](/sources/ryu-jones-1995.md) and
  [Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md) use the
  arithmetic interface average inside a Harten TVD scheme.
* [Powell (1994)](/sources/powell-1994.md) uses an arithmetic average in
  the first-order Roe-type solver of the
  [eight-wave formulation](/methods/eight-wave.md); a Roe average "does
  exist", per a private communication from Roe.
* [Roe & Balsara (1996)](/sources/roe-balsara-1996.md) show that near the
  triple umbilic the Roe-type flux changes only in proportion to the
  distance the linearization state moves, although individual wave
  strengths change by $O(1)$.

An arithmetic-average solver is therefore "Roe-type" in its wave
decomposition, not in the Property U sense: Roe (1981) names exactly these
averages as the candidates that fail the jump identity (p. 359).

**Multi-dimensional caveat.** Roe (1981, p. 360) notes that under
dimensional splitting oblique shocks are not recognized as in equilibrium
by either split operator: "the concept of operator splitting becomes rather
dubious". No remedy is given.

# Citations

1. [Roe (1981)](/sources/roe-1981.md), pp. 359–371, eqs. 5–22, Table I.
2. [Harten, Lax & van Leer (1983)](/sources/harten-lax-vanleer-1983.md), §2 (Theorem 2.1, eq. 2.20), §3B (eqs. 3.11–3.12b).
3. [Harten (1983)](/sources/harten-1983.md), §5 (eq. 5.4), §6 (eq. 6.4), §7 (eq. 7.5).
4. [Brio & Wu (1988)](/sources/brio-wu-1988.md), §§III, IV.1, V.
5. [Ryu & Jones (1995)](/sources/ryu-jones-1995.md), §2.3, eqs. 2.80–2.95.
6. [Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md), §2.2, eqs. 2.20–2.21.
7. [Powell (1994)](/sources/powell-1994.md), §2, p. 8.
8. [Roe & Balsara (1996)](/sources/roe-balsara-1996.md), §4.
