---
type: Method
title: "Piecewise parabolic method (PPM)"
description: "Colella–Woodward higher-order Godunov method: fourth-order edge interpolation, monotonized parabolas per cell, characteristic domain-of-dependence states for the Riemann problem, contact steepening and shock flattening."
status: established
aliases: [PPM, piecewise parabolic method]
tags: [reconstruction, godunov, limiter, finite-volume]
timestamp: 2026-10-13T00:00:00Z
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

**The parabola** in cell $I_i$, in the cell coordinate $\zeta$, is
$$u(x) = u^+_{i-1/2} + \left(\zeta + \tfrac12\right)\left(\Delta u_i + u_{6,i}\left(\tfrac12 - \zeta\right)\right),$$
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

**Later uses (batch 6).** For relativistic MHD, a flattener built from the
undivided divergence of the four-velocity, compared with the smallest
relativistic sound speed over 27 cells, and spread to neighbours across
pressure jumps ([Balsara & Kim (2016)](/sources/balsara-2016-b.md), eqs. 2.8–2.9).
Its flattening coefficient is 0 in smooth flow, like $\phi_i$ here, while the same paper's
factor in the average–point conversion uses the opposite convention.

**Later uses (batch 7).**
* *A gentler overshoot reset.* With MC-limited differences inside the
  fourth-order edge formula, the author prefers resetting an overshooting
  zone to its MC linear profile, $u^\mp_{i\pm1/2} \to \bar u_i \pm \tfrac12\delta^{\mathrm{MC}}\bar u_i$ (the MC-limited slope),
  over the original reset to the constant ([Balsara (2017)](/sources/balsara-2017-d.md), §II.2,
  eqs. 16–17b). The review states that the original PPM was "restricted to
  second order accuracy by the use of a monotonicity preserving limiter"
  (citing Woodward 1986), and that the modern trend is to forgo steepeners
  (§III.1).

**Later uses (batch 11).** *The 1984 comparison.* The companion paper
[Woodward & Colella (1984)](/sources/woodward-1984.md) runs PPM in both
Eulerian forms, Lagrange step plus remap (PPMLR) and single step
(PPMDE), against MacCormack with Lapidus viscosity, BBC, ETBFCT,
first-order Godunov and MUSCL.
* *Accuracy and cost.* PPM is first in accuracy on a given grid and per
  CPU second, ahead of MUSCL, ETBFCT, BBC, MacCormack and Godunov (§VII).
  On the [interacting blast waves](/benchmarks/interacting-blast-waves.md)
  it is the only scheme whose density error converges at first order in
  $h$, the fastest possible when the error sits at discontinuities; the
  other schemes converge sub-linearly (§VIa). PPM costs about 20 % more
  CPU time than MUSCL and ETBFCT, and about 6 times MacCormack per zone.
* *Two forms, one accuracy.* PPMDE and PPMLR give nearly identical accuracy
  and cost, unlike MUSCL or Godunov in their two forms. The authors credit
  the third-order PPM remap and the slight broadening of stationary
  shocks, and advise remapping "with one extra order of accuracy over the
  Lagrangian step" (§§VIb–VII). This agrees with the "third-order in
  general" accuracy stated above.
* *The dissipation options for slow strong shocks* (§Vc). Without them,
  strong shocks moving slowly relative to the grid leave post-shock
  oscillations of about 1–2 % with wavelengths of many zones, which
  cannot be damped afterwards. PPM broadens such shocks to about 2 zones
  "in the worst cases". Flattening plus "jiggling" the remap grid gives a
  diffusive error that is fifth-order small; flattening plus Lapidus
  viscosity with coefficient 0.1 gives an error third-order small in
  smooth flow ([slowly moving shock anomaly](/definitions/slowly-moving-shock-anomaly.md)).
  The paper is inconsistent on which run used which: §Vc assigns the
  jiggled grid to Fig. 4 and Lapidus 0.1 to Fig. 9f, both PPMDE, while
  §VIb assigns the jiggled grid to PPMLR and Lapidus 0.1 to PPMDE.
* *Riemann solver.* All Godunov-type schemes in the comparison use
  Colella's approximate solver, which replaces rarefactions by rarefaction
  shocks and needs at most two Newton iterations (§Vc).
* On the [double Mach reflection](/benchmarks/double-mach-reflection.md)
  and the [step](/benchmarks/forward-facing-step.md), PPMDE shows
  essentially no noise at slow, grid-aligned shocks, where Godunov and
  MUSCL turn unstable, and the PPM forms are about 3–5 times more
  efficient than BBC.

**Later uses (batch 14).** *What PPM inherits from MUSCL*
([van Leer (1979)](/sources/vanleer-1979.md); [MUSCL](/methods/muscl.md)).
* *Specific volume, velocity and pressure.* Van Leer's Lagrangean step
  already distributes these, not total energy, because the more accurate
  energy-based distribution would make the monotonicity algorithm implicit
  in $p$ (eqs. 47–48, p. 107).
* *Second order in the wave interaction.* "Following van Leer" means: an
  iterated interface Riemann problem, then time derivatives of the
  resolved state from the characteristic equations at a discontinuity,
  and a half-step time-centring; only $O(\Delta t^2)$ accuracy is asked of
  the interface values (§§2.3–2.4, p. 110).
* *The MC-limited slope of the batch-7 reset* is van Leer's Lagrangean
  monotonicity algorithm applied to the central slope: eq. 101 with
  eq. B1 is $\delta^{\mathrm{MC}}\bar u_i$ (an identity; van Leer does not
  use the name).
* *Two forms.* Van Leer's MUSCL already separates the Lagrangean step from
  a least-squares remap (§3.2), whose moment fitting he calls "vastly
  superior" to the interface differencing of the Lagrangean step (App. B).
  *Compiler reading:* this asymmetry fits Woodward and Colella's advice to
  remap with one extra order and the accuracy gap between MUSCL's two
  forms, but neither paper links them.

# Citations

1. [Colella & Woodward (1984)](/sources/colella-1984.md), §§1–4 and the Appendix.
2. [Suresh & Huynh (1997)](/sources/suresh-1997.md), introduction and §2.
3. [Balsara & Shu (2000)](/sources/balsara-2000.md), §I, §§IV.b, VI.a, VII.c.
4. [McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §§2.4–2.5.
5. [Balsara & Kim (2016)](/sources/balsara-2016-b.md), §2.
6. [Balsara (2017)](/sources/balsara-2017-d.md), §§II.2, III.1.
7. [Woodward & Colella (1984)](/sources/woodward-1984.md), §§Vc, VIa–VII.
8. [van Leer (1979)](/sources/vanleer-1979.md), §§2.2–2.4, 3.2–3.3, App. B.
