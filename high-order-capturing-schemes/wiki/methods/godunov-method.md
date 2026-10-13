---
type: Method
title: "Godunov's method"
description: "First-order conservative scheme that holds the solution constant in each cell, solves the exact Riemann problem at every interface and updates the cell averages from the resulting interface fluxes; introduced in Lagrangian form with a fixed-point Riemann solver and proofs that limits are entropy-satisfying weak solutions, it is the first-order base that MUSCL, PPM, ENO and the a posteriori limiters build on."
status: established
aliases: [Godunov scheme, Godunov's scheme, first-order Godunov, Godunov-type scheme]
tags: [godunov, riemann-problem, finite-volume, first-order, euler]
timestamp: 2026-10-13T00:00:00Z
---

# Godunov's method

## The original scheme

**Motivation from linear monotone schemes**
([Godunov (1959)](/sources/godunov-1959.md), Ch. I). A linear scheme that
keeps monotone data monotone is at most first order
([Godunov's order barrier](/results/godunov-order-barrier.md)); the most
accurate monotone three-point scheme for advection is upwind. For the
linear acoustic system, the upwind scheme applied to each Riemann
invariant becomes a conservative update whose interface pressure and
velocity are exactly the state between the two acoustic waves of the
*decay of the discontinuity* (the Riemann problem) between neighbouring
constant layers. These interface values stay constant until waves from
the neighbouring interfaces arrive; "curiously", the step bound this
requires coincides with the scheme's stability condition (§5, p. 283).
The new layer values are averages of a no longer constant solution.

**The nonlinear scheme** (Ch. II §2). Godunov transfers this picture to
the Lagrangian equations of 1D ideal-gas dynamics, in velocity, specific
volume and specific internal energy, with a mass-type Lagrangian
coordinate. One step:
1. the gas is split into layers, each constant at the start of the step;
2. at every interface the Riemann problem between the two adjacent layers
   is solved exactly for the star pressure $p_*$ and velocity $v_{n*}$;
3. each layer's velocity, specific volume and total specific energy are
   updated by $\Delta t/h$ (times the Lagrangian scaling constant) times
   the differences of the interface pressures, interface velocities and
   interface products $p_* v_{n*}$.

The new values are layer averages that replace the true distribution
(p. 286). The original paper has no Eulerian fixed-grid version; particle
positions can be tracked by moving the interfaces with $v_{n*}$, which
also yields the specific volume (§5).

**Interface Riemann problem** (§4). The star pressure is a combination of
the two side pressures weighted by the mass fluxes through the left and
right waves, and those mass fluxes depend on $p_*$ through the shock and
rarefaction relations. Godunov solves this by fixed-point iteration on
$p_*$, with a relaxed variant for strong rarefactions; the convergence
analysis is omitted as "standard" (formulas on the
[source page](/sources/godunov-1959.md); later iterations in
[exact Riemann solver](/methods/exact-riemann-solver.md)).

**Time step** (§4, p. 292). The step is bounded by the interface spacing
over the largest Lagrangian wave speed of the interface problems: a
Courant number of 1 relative to the interface-to-interface distance.
Godunov justifies the nonlinear bound empirically ("a large number of
varied computations convincingly show" stability), not by proof.

**What is proved** (§§3–4).
* *Weak solutions.* If the grid functions converge, as the steps are
  refined, to piecewise smooth limits, the limits satisfy the integral
  conservation laws: discrete conservation on rectangular contours, plus
  convergence of the interface values to the same limits as the layer
  values (§3, eq. 5).
* *Entropy.* The exact in-layer evolution does not lower entropy, and
  convexity (Jensen-type inequalities) carries this to the average: the
  specific entropy of each layer average does not decrease over a step
  (eq. 9). Limits therefore satisfy the entropy condition (§4, credited
  in a footnote to an observation of L. I. Sedov).

**Known defects in the original** (§§6–7, Appendices II–III).
* *Start-up entropy error.* While a captured shock profile forms from a
  step, the scheme "erred" in entropy; the error stays as a permanent mark
  in the specific volume near the starting point, because the smooth
  region conserves it. A similar trace forms at a wall hit by cold gas.
  Such traces "usually occupy two–three computational points" and at fine
  steps do not affect the results (p. 295).
* *Material contacts.* With the contact at an interface and each gas's
  constants on its own side, the discrete solution near the contact has
  linear profiles whose extrapolations disagree by an amount proportional
  to the difference of the two sides' stable time steps; Godunov's cure is
  to choose the spacings so that these steps agree (§7, eq. 16).
* *Shock profiles.* Godunov's scheme forms a stationary captured shock
  without overshoot within a few steps, where a second-order
  (Lax–Wendroff-type) scheme gives post-shock overshoots that pulsate
  from step to step (Appendices I–II).

## Later formulations

* *Eulerian form.* The interface flux is the physical flux of the exact
  solution sampled on the $t$-axis; the scheme is stable up to Courant
  number 1 ([Toro (1997)](/sources/toro-1997.md), §§6.2–6.3;
  [exact Riemann solver](/methods/exact-riemann-solver.md)). In the
  scalar case this flux is the min/max form listed under
  [monotone numerical flux](/definitions/monotone-flux.md)
  ([Shu (1998)](/sources/shu-1998.md); [Liu, Osher & Chan (1994)](/sources/liu-1994.md)),
  a later statement that is not in Godunov's paper.
* *Approximate solvers.* Godunov-type schemes replace the exact solver
  by approximate ones ([approximate Riemann solvers](/methods/approximate-riemann-solvers.md));
  Harten's first-order "ROE" variant, with numerical viscosity
  $\Theta_{i+1/2} = \vert\hat a_{i+1/2}\vert$ per field, is the least
  dissipative scheme of his three-point TVD family
  ([Harten (1983)](/sources/harten-1983.md), §§5, 7).

## Base of the higher-order schemes

* *Reconstruct, evolve, average.* Harten et al.'s abstract ENO scheme
  generalizes Godunov's: piecewise constant ($r = 1$) gives Godunov,
  piecewise linear a MUSCL-type scheme
  ([Harten et al. (1987)](/sources/harten-1987.md);
  [ENO](/methods/eno-reconstruction.md)). PPM is a higher-order Godunov
  method of the MUSCL type ([Colella & Woodward (1984)](/sources/colella-1984.md);
  [PPM](/methods/ppm.md)).
* *Fallback.* The a posteriori limiting cascade ends at a first-order
  Godunov update, "supposed" monotone and positivity-preserving under its
  CFL condition ([Dumbser et al. (2014)](/sources/dumbser-2014.md), §4.1;
  [a posteriori subcell limiting](/methods/a-posteriori-subcell-limiting.md)).
* *Stability properties.* Godunov's scheme is TVD in the scalar case
  ([Harten et al. (1987)](/sources/harten-1987.md);
  [TVD](/properties/total-variation-diminishing.md)), and its flux keeps
  the admissible set of Euler states under its CFL condition
  ([positivity preservation](/properties/positivity-preserving.md);
  [Zhang & Shu (2010)](/sources/zhang-2010.md), §1).

## Measured behaviour in later sources

* *Sod's comparison.* Godunov's iteration as modified by Chorin (an
  under-relaxation halved on non-convergence); contact and shock over
  7–8 and 5–6 zones; with Hyman's scheme the best of the plain schemes
  ([Sod (1978)](/sources/sod-1978.md); [Sod shock tube](/benchmarks/sod-shock-tube.md)).
* *Convergence and cost.* On the interacting blast waves the error of
  first-order Godunov converges like $h^{0.15}$ at first and $h^{0.4}$ on
  the finest grids, and the scheme cannot match 200-zone PPM even with 12
  times the zones; it costs about twice MacCormack's scheme per zone and
  step ([Woodward & Colella (1984)](/sources/woodward-1984.md), §§IIIc,
  VIa).
* *Entropy at sonic points and slow shocks.* A small "unphysical
  rarefaction shock" forms where the $x$-sweep Mach number is 1
  ([Woodward & Colella (1984)](/sources/woodward-1984.md), §VIb); Toro's
  "entropy glitch" in sonic rarefactions should vanish as $h \to 0$
  because the method is entropy satisfying ([Toro (1997)](/sources/toro-1997.md),
  §6.4.1). Even first-order Godunov has a 3 % post-shock entropy error at
  slowly moving strong shocks ([Colella & Woodward (1984)](/sources/colella-1984.md),
  §4; [slowly moving shock anomaly](/definitions/slowly-moving-shock-anomaly.md)).
  Harten finds that Godunov's scheme "actually exhibits a surprisingly
  poor entropy enforcement" ([Harten (1983)](/sources/harten-1983.md),
  p. 374, citing Harten & Hyman). These are statements about finite
  grids; Godunov's proofs concern the cell entropy inequality and the
  limit, so they qualify each other rather than conflict.
* *Shock instability.* Godunov's exact solver resolves contacts and
  shear exactly and is among the solvers prone to the carbuncle and
  kinked Mach stems; Woodward and Colella already report a 2D instability
  of strong, nearly grid-aligned stationary shocks for Godunov and MUSCL
  ([numerical shock instability](/definitions/numerical-shock-instability.md);
  [Simon & Mandal (2019)](/sources/simon-2019.md), §4.1;
  [Woodward & Colella (1984)](/sources/woodward-1984.md), §VIb).

**Later uses (batch 16).**
* *Eulerian form and entropy, restated* ([Harten, Lax & van Leer (1983)](/sources/harten-1983-d.md),
  §3A, eqs. 3.3–3.6, pp. 45–46). The update is the cell average of the
  exact solutions of the interface Riemann problems, equal to the
  conservative scheme whose flux is the physical flux of the exact
  solution on the interface. It satisfies a cell entropy inequality, by
  the exact solution's entropy inequality and Jensen's inequality, the
  argument of Godunov's §4 above. Two Courant bounds are kept apart:
  neighbouring Riemann problems do not interact for
  $\Delta t\max_p\vert\lambda^{(p)}\vert/h < \tfrac12$, while the conservative
  form "remains consistent" with the averaging up to $\le 1$, the bound of
  the Eulerian bullet above. The Godunov flux is only piecewise
  differentiable; for linear systems it is Courant–Isaacson–Rees upwinding.
* *What "Godunov-type" means* (Theorem 3.1). The alias on this page has a
  precise definition there: an approximate Riemann solution consistent
  with the integral forms of both the conservation law and the entropy
  inequality, averaged over the half cells. Such schemes are conservative
  and entropy-satisfying, and "if such a scheme converges, the limit
  satisfies the conservation law and the entropy condition in the weak
  sense"; convergence is assumed, not proved (p. 38). The paper presents
  Roe's solver as Godunov-type in the sense of its flux formula (3.9),
  which needs only the conservation condition, and says Osher's is not
  (§3B)
  ([approximate Riemann solvers](/methods/approximate-riemann-solvers.md);
  [HLL](/methods/hll-riemann-solver.md)).
* *Positivity* ([Einfeldt et al. (1991)](/sources/einfeldt-1991.md), §2).
  Godunov's method is positively conservative: the averages stay in the
  convex admissible set if "no vacuum occurs in the exact solution to the
  Riemann problem at the cell interfaces". The time-step condition is not
  stated with the proof; the paper's runs use
  $\Delta t\max_i(\vert v_{x,i}\vert + c_i)/h \le \tfrac12$
  ([positivity preservation](/properties/positivity-preserving.md)).
* *The weak-limit statement before Godunov* ([Lax (1954)](/sources/lax-1954.md),
  pp. 163–164). Lax had shown for his conservative scheme that a bounded
  a.e. (strong) limit is a weak solution, insisting that "a weak limit of
  weak solutions is not a weak solution unless it is also a strong
  limit"; Godunov cites the paper.

# Citations

1. [Godunov (1959)](/sources/godunov-1959.md), Ch. I §§2–5, Ch. II §§2–7, Appendices I–III (reader's translation of the Russian original).
2. [Toro (1997)](/sources/toro-1997.md), §§6.2–6.4.
3. [Shu (1998)](/sources/shu-1998.md), §2.3.1.
4. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §2.
5. [Harten (1983)](/sources/harten-1983.md), §§5, 7.
6. [Harten et al. (1987)](/sources/harten-1987.md).
7. [Colella & Woodward (1984)](/sources/colella-1984.md), §4.
8. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §4.1.
9. [Zhang & Shu (2010)](/sources/zhang-2010.md), §1.
10. [Sod (1978)](/sources/sod-1978.md), eqs. 12–19, Table I.
11. [Woodward & Colella (1984)](/sources/woodward-1984.md), §§IIIc, VIa–VIb.
12. [Simon & Mandal (2019)](/sources/simon-2019.md), §4.1.
13. [Harten, Lax & van Leer (1983)](/sources/harten-1983-d.md), §3A, eqs. 3.3–3.8, pp. 38, 45–46.
14. [Einfeldt et al. (1991)](/sources/einfeldt-1991.md), §§2, 6.
15. [Lax (1954)](/sources/lax-1954.md), pp. 163–164.
