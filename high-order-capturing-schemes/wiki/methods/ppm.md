---
type: Method
title: "Piecewise parabolic method (PPM)"
description: "Colella–Woodward higher-order Godunov method: fourth-order edge interpolation, monotonized parabolas per cell, characteristic domain-of-dependence states for the Riemann problem, contact steepening and shock flattening."
status: established
aliases: [PPM, piecewise parabolic method]
tags: [reconstruction, godunov, limiter, finite-volume]
timestamp: 2026-10-08T00:00:00Z
---

# Piecewise parabolic method (PPM)

A higher-order extension of Godunov's method of the MUSCL type, introduced
by [Colella & Woodward (1984)](/sources/colella-1984.md). The cell data are
averages $\bar u_i$; each cell carries a parabola that reproduces its
average, and fluxes come from Riemann problems at the interfaces.

## Reconstruction

**Edge values.** An interface value $u_{i+1/2}$ is obtained by
interpolating the quartic through five values of the primitive
$\mathcal{U}$ and differentiating it at $x_{i+1/2}$
([finite-volume reconstruction](/methods/finite-volume-reconstruction.md)).
On a uniform grid, with unlimited slopes,
$$u_{i+1/2} = \tfrac{7}{12}\left(\bar u_i + \bar u_{i+1}\right) - \tfrac{1}{12}\left(\bar u_{i+2} + \bar u_{i-1}\right),$$
a centred four-point formula. The slope entering the general
(variable-mesh) formula is monotonized first, so that $u_{i+1/2}$ lies
between $\bar u_i$ and $\bar u_{i+1}$.

**The parabola** in cell $I_i$, with $x = (\xi - x_{i-1/2})/h_i$, is
$$u(\xi) = u^+_{i-1/2} + x\left(\Delta u_i + u_{6,i}(1 - x)\right),$$
with $\Delta u_i$ and $u_{6,i}$ as in the [registry](/notation.md); it
has average $\bar u_i$ by construction.

**Monotonicity constraint.** Normally $u^-_{i+1/2} = u^+_{i+1/2} = u_{i+1/2}$.
Two resets introduce interface discontinuities:
* if $\bar u_i$ is a local extremum, the parabola is replaced by the
  constant $\bar u_i$;
* if the parabola would overshoot inside the cell (the condition is
  $\vert\Delta u_i\vert < \vert u_{6,i}\vert$), the edge value on the far
  side is reset so that the parabola is monotone with zero derivative at
  the opposite edge.

**Accuracy.** The advection scheme is third-order accurate in general
and fourth-order in the limit of small time steps on a uniform grid
([Colella & Woodward (1984)](/sources/colella-1984.md), §1).
*Compiler reading:* the extremum reset clips smooth extrema, so the
stated orders hold away from them; this is the TVD-type degeneration
recorded in [total variation diminishing](/properties/total-variation-diminishing.md).
[Balsara & Shu (2000)](/sources/balsara-2000.md) class PPM among TVD
schemes, "restricted to being second-order accurate in the $L_1$ norm
even for smooth problems with extrema", and
[Suresh & Huynh (1997)](/sources/suresh-1997.md) state that PPM-type
limiting degenerates to first order near extrema. The two characterize
the same clipping at different norms; neither contradicts the
smooth-monotone orders claimed by the authors.

## Gas dynamics

* **Lagrangian step.** Specific volume, velocity and pressure (not total
  energy) are interpolated in the mass coordinate. Riemann states are
  averages of each profile over the domain of dependence of the
  interface during the step (traced along the sound characteristics),
  so that the interface values are time-centred in smooth flow. Third
  order in time is given up in the nonlinear wave interaction, to
  second order, following van Leer.
* **Eulerian schemes.** Either Lagrange step plus remap, or a
  single-step Eulerian scheme. In the latter, a first guess from the
  extreme characteristic speeds is corrected by subtracting, per
  characteristic family, the part of the wave that cannot reach the
  interface within $\Delta t$. Multi-D is by operator splitting.

## Discontinuity treatment

* **Contact steepening** ("discontinuity detection"): in cells judged to
  lie inside a contact (large third difference, sign change of the
  second difference, opposite signs of first and third differences, jump
  above a relative threshold), the edge values are taken from the
  limited linear profiles of the neighbours, which steepens the profile.
  Applied only to density, and only at jumps that are predominantly
  contacts. See also [contact sharpening](/methods/contact-sharpening.md).
* **Flattening** near strong shocks: the parabola is blended toward the
  constant $\bar u_i$ with weight $\phi_i$, set from the steepness of the
  pressure jump. It locally reduces the order and removes post-shock
  oscillations in the two Riemann invariants that cross the shock.
* **Extra dissipation** for slow, strong shocks: an explicit diffusive
  flux or an alternating grid motion. Flattening alone cannot remove the
  post-shock entropy error of a nearly stationary strong shock, which
  even the first-order Godunov scheme shows.

## Later comparisons

On long-time advection of the [composite profile](/benchmarks/composite-advection-profile.md),
[Balsara & Shu (2000)](/sources/balsara-2000.md) report that PPM flattens
every peak, turning all pulses into square-wave-like profiles, and that
the contact steepener without a balancing factor makes them
asymmetric. On a 45° supersonic vortex and an oblique shock–vortex
interaction, dimensionally split PPM is markedly less accurate than
$r = 5$ MPWENO ([monotonicity-preserving limiting](/methods/monotonicity-preserving-limiter.md)).
[Suresh & Huynh (1997)](/sources/suresh-1997.md) note that the
five-point interface value of MP5 is less prone to staircasing than the
four-point PPM value because its leading error is dissipative.

**Later uses (batch 5).** A fourth-order finite-volume scheme keeps the
PPM edge formula as a fourth-order face average but replaces the PPM
limiter with a modified Colella–Sekora extremum-preserving one. It drops
PPM's first stage, which bounds the face value between neighbouring
averages, as redundant and too dissipative with RK4. It keeps the
overshoot reset away from extrema and limits at extrema only when a
third-derivative test fails. Flattening and an artificial viscosity made
$O(h^4)$ in smooth flow handle strong shocks. Its flattening coefficient
is 1 for *no* flattening, the opposite of $\phi_i$ here
([fourth-order finite volume](/methods/fourth-order-finite-volume.md);
[McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §§2.4–2.5).

# Citations

1. [Colella & Woodward (1984)](/sources/colella-1984.md), §§1–4 and the Appendix.
2. [Suresh & Huynh (1997)](/sources/suresh-1997.md), introduction and §2.
3. [Balsara & Shu (2000)](/sources/balsara-2000.md), §I, §§IV.b, VI.a, VII.c.
4. [McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §§2.4–2.5.
