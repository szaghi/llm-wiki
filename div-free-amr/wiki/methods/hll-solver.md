---
type: Method
title: "HLL Riemann solver"
description: "One-intermediate-state approximate Riemann solver of Harten, Lax and van Leer: two signal-speed bounds and the single state fixed by the integral conservation law; entropy-satisfying when the bounds are true, with positivity and the MHD wave-speed choices supplied by later work; the base of the HLL forms of the UCT edge EMF."
status: established
aliases: [HLL, HLL flux, HLLE, one-intermediate-state solver]
tags: [riemann-solver, godunov, shock-capturing, positivity, upwind-emf]
timestamp: 2026-10-13T00:00:00Z
---

# HLL Riemann solver

[Harten, Lax & van Leer (1983)](/sources/harten-lax-vanleer-1983.md)
(§3B(i), eqs. 3.13–3.16) build the simplest
**Godunov-type** approximate Riemann solver: a fan of two waves enclosing
one constant intermediate state.

## Construction

Two speeds are given, a lower and an upper bound "for the smallest and
largest signal velocity, calculated according to some algorithm" (p. 50).
The paper gives no algorithm. The approximate solution is the left
conserved state $U$ ([notation](/notation.md)) left of the slower bound,
the right state right of the faster one, and one intermediate state
between them. Consistency with the integral form of the conservation law
over the fan (their eq. 3.7a) fixes that state: the speed-weighted
difference of the two states, minus the jump of the physical flux, divided
by the difference of the two bounds (eq. 3.14).

The numerical flux is the left physical flux when both bounds are
positive, the right one when both are negative, and otherwise (eq. 3.15a)
the combination of the two physical fluxes weighted by the opposite bounds,
plus the product of the bounds times the jump of $U$, all over the
difference of the bounds. Eq. 3.15b writes the three cases as one formula.
When the bounds are equal and opposite, the flux is the local
Lax–Friedrichs flux, which [Wu & Shu (2019)](/sources/wu-shu-2019.md)
treat as the symmetric HLL case (their $\alpha^{\mathrm{LF}}$).

## What is proved

Harten, Lax & van Leer prove two things (p. 50):
* the intermediate state equals the mean of the **exact** Riemann solution
  over the fan, so by Jensen's inequality the scheme satisfies the discrete
  entropy inequality, and (through their Theorem 1.1) a convergent HLL
  scheme converges to an entropy weak solution;
* if the two states are joined by a single shock of the slowest or fastest
  family and the speed algorithm returns that shock's speed, the flux is
  exact.

The mean-value argument holds only if the two speeds truly bound the
signal speeds of the exact solution. The paper does not claim positivity of
the intermediate state: its only positivity statement is a caution that
density and pressure must stay positive (§1).

## Wave speeds and positivity (later work)

* **Einfeldt's speeds (HLLE).** [Stone et al. (2008)](/sources/stone-2008.md)
  state that the HLLE intermediate state is positive, so first-order 1D
  schemes built on it are positive and serve as a fallback when Roe fails;
  in several dimensions at higher order positivity "depends on the details
  of the multidimensional integrator". The attribution is to the HLLE
  (Einfeldt) variant, not to Harten, Lax & van Leer.
* **MHD positivity speeds.** [Wu & Shu (2019)](/sources/wu-shu-2019.md)
  (Theorem 2.2) give explicit bounds under which the HLL intermediate state
  is admissible ($\mathcal G$) up to a term in the jump of $B_n$, and fully
  admissible when $B_n$ is continuous. The standard Davis and Einfeldt
  speeds are not guaranteed to work. The theorem fills the gap the 1983
  paper leaves open ("some algorithm") for ideal MHD
  ([positivity–divergence coupling](/results/positivity-divergence-coupling.md)).
* **Positivity through HLLD (Miyoshi & Kusano 2005).**
  [Miyoshi & Kusano (2005)](/sources/miyoshi-kusano-2005.md) (§5.3, p. 332)
  argue 1D positivity of the four [HLLD](/methods/hlld-solver.md) states
  when each outer speed exceeds the adjacent normal velocity by more than
  $\sqrt{(\gamma-1)/(2\gamma)}$ times the adjacent fast speed, and write
  that the proof "will also be applicable to the single-state HLL Riemann
  solver since the one intermediate state of the HLL solver is given by the
  average of the HLLD intermediate states contained in G" ($\mathcal G$).
  They write that HLLD "clearly satisfies" this bound (their eq. 98) with
  their simple speeds of eq. 67 (extreme normal velocity plus or minus the
  larger fast speed), which also give the first assumption of the
  derivation.
  **A qualification, not a contradiction** of Wu & Shu's "not guaranteed":
  the derivation also assumes that the outer speed exceeds the HLLD middle
  speed by at least the fast speed, which Miyoshi & Kusano cannot confirm
  "at any situation" and check only for strong expansions; their
  conclusion is that HLLD "is thought to be a positively conservative
  scheme", and they restrict it to 1D. Their claim is conditional where Wu
  & Shu prove explicit sufficient bounds, so the two do not assert
  incompatible things about the same speeds.
* **First-order zone updates.** [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md)
  call a first-order zone update with HLL or LLF fluxes positive, "as was
  first proved by Gurski" (2004).

## Uses in divergence-preserving schemes

* **Edge EMFs.** The HLL forms of the
  [UCT](/methods/upwind-constrained-transport.md) four-state edge EMF
  ([Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md),
  eq. 56) reduce to the central-scheme formulas of Kurganov–Noelle–Petrova.
  [Felker & Stone (2018)](/sources/felker-2018.md) select the corner EMF by
  the HLL four-state formula with Einfeldt wavespeeds from the four
  adjacent face solves. [Mignone & Del Zanna (2021)](/sources/mignone-2021.md)
  derive HLL coefficients for their composition formula; UCT-HLL is the most
  diffusive of their EMFs. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md)
  give a 2D HLL edge EMF (their eqs. 18–20). The two-dimensional four-state
  construction is not in the 1983 paper, which is one-dimensional.
* **Base schemes.** [Balsara & Kim (2004)](/sources/balsara-kim-2004.md)
  run their cleaning-versus-CT comparison on one HLL base scheme.
  [Balsara (2009)](/sources/balsara-2009.md) finds that the linearized
  solver's advantage over HLL shrinks as the order rises.

# Citations

1. [Harten, Lax & van Leer (1983)](/sources/harten-lax-vanleer-1983.md), §1, §3B(i), eqs. 3.7a, 3.13–3.16, p. 50.
2. [Stone et al. (2008)](/sources/stone-2008.md), §4.3.
3. [Wu & Shu (2019)](/sources/wu-shu-2019.md), Theorem 2.2, Remarks 2.4–2.5.
4. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§3, 5.
5. [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md), §2.3, eq. 56.
6. [Felker & Stone (2018)](/sources/felker-2018.md), §4.1–4.2.
7. [Mignone & Del Zanna (2021)](/sources/mignone-2021.md), §§5–6.
8. [Balsara & Kim (2004)](/sources/balsara-kim-2004.md), Summary (base scheme).
9. [Balsara (2009)](/sources/balsara-2009.md), §5.1.
10. [Miyoshi & Kusano (2005)](/sources/miyoshi-kusano-2005.md), §§4–5.3, p. 332.
