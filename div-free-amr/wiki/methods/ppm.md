---
type: Method
title: "Piecewise parabolic method (PPM)"
description: "Higher-order Godunov method with a conservative, monotonicity-constrained parabola per zone, fourth-order interface values, characteristic tracing of interface states and extra shock dissipation; constraint-agnostic, so its MHD uses take divergence balance from CT and consistent source terms."
status: established
aliases: [PPM, piecewise parabolic method]
tags: [ppm, reconstruction, godunov, high-order, shock-capturing]
timestamp: 2026-10-13T00:00:00Z
---

# Piecewise parabolic method (PPM)

A higher-order extension of Godunov's method in the MUSCL family, given in
full by [Colella & Woodward (1984)](/sources/colella-woodward-1984.md).
The primary source is pure hydrodynamics: it contains no magnetic field
and no divergence constraint. Everything this bundle uses it for comes
from later papers (below).

## Definition

**The zone parabola** (§1, eqs. 1.4–1.5). In each zone the profile is a
parabola fixed by its two edge values and the zone average, which it
reproduces exactly.

**Interface values** (eqs. 1.6, 1.9). The value at a zone edge is the
derivative there of the quartic interpolant of the indefinite integral
through five edges. On a non-uniform mesh it is third-order accurate,
"even where the mesh spacing changes discontinuously". On a uniform mesh
it is the fourth-order value

$$w_{j+1/2} = \tfrac{7}{12}\left(\bar w_j + \bar w_{j+1}\right) - \tfrac{1}{12}\left(\bar w_{j-1} + \bar w_{j+2}\right).$$

The slopes
inside the general formula are limited (eq. 1.8) so that the edge value
lies between the adjacent zone averages.

**Monotonicity constraint** (eq. 1.10). At a local extremum of the zone
averages the profile becomes constant. If the parabola overshoots near one
edge, the opposite edge value is reset so that the derivative vanishes at
that edge. *Compiler reading:* smooth extrema are clipped. Later codes
replace this limiter with ones that keep accuracy at smooth extrema
([CASTRO](/software/castro.md); the PPM4 limiter of
[Felker & Stone (2018)](/sources/felker-2018.md)).

**Accuracy, as stated.** Third order in general; fourth order for equally
spaced zones in the limit of vanishing time step. The gas-dynamics
schemes compute the nonlinear interaction of the two acoustic waves only
to second order in time (§2). No convergence table is given.

## Gas-dynamics variants

* **Lagrangian** (§2). Left and right Riemann states are averages of the
  parabolae over the sound-wave domains of dependence; a two-shock Riemann
  problem, solved with a fixed number of iterations, gives time-centred
  edge pressure and velocity. Pressure, not total energy, is
  interpolated.
* **Lagrange plus remap** (§2, end), not detailed in the paper.
* **Single-step Eulerian with characteristic tracing** (§3). A first guess
  averages over the fastest characteristic toward the interface; each wave
  family moving toward the interface is then subtracted by the linearized
  characteristic equations, and waves moving away contribute nothing.
  Geometric and gravity sources enter the tracing itself. Without pressure
  and velocity gradients the scheme reduces exactly to the §1 advection
  scheme.
* **Dimensionally split.** Multi-D is done by operator splitting in the
  original. Unsplit PPM with corner coupling is a later construction
  ([Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md), CTU;
  [Almgren et al. (2010)](/sources/almgren-2010.md)).

## Discontinuity handling

* **Contact steepening** (eqs. 1.14–1.17, 3.2), on density only and only at
  contacts, with tuned constants.
* **Flattening** (eq. 4.1): edge values blended toward the zone average at
  steep shocks, down to first-order Godunov.
* **Extra dissipation** (eqs. 4.2–4.5): post-shock noise appears in any
  such higher-order Godunov method for systems, so an artificial diffusive
  flux or grid motion is added. In multi-D its coefficient is driven by an
  undivided velocity divergence, the paper's only divergence. The tuned
  constants are in the Appendix, and "experimentation with different values
  of the parameters is not recommended".

**Stencil width.** The paper states no ghost-cell count. Its stencils
imply one: an edge value uses two zones on each side, and flattening
reaches further. *Compiler reading:* this is consistent with the four
ghost cells CASTRO gives as the PPM requirement
([Almgren et al. (2010)](/sources/almgren-2010.md);
[block-structured AMR](/definitions/block-structured-amr.md)); the count
is CASTRO's statement.

## Uses in this bundle

PPM is **constraint-agnostic**: divergence preservation in its MHD uses
comes from the CT layer and from consistent source terms, never from the
reconstruction.
* **Athena.** PPM interface states with Colella's CTU and staggered
  [CT](/methods/constrained-transport.md). For MHD the characteristic
  tracing needs multidimensional source terms proportional to normal-field
  derivatives, balanced so as to respect the divergence relation
  ([Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md);
  [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md);
  [field-loop advection](/benchmarks/field-loop-advection.md)). They enter
  the slot where Colella & Woodward put geometry and gravity sources; the
  divergence-balance requirement itself is post-1984 and MHD-specific. The
  code paper offers PLM or PPM in characteristic variables
  ([Stone et al. (2008)](/sources/stone-2008.md)); Athena++ uses PPM with
  characteristic limiting ([Pakmor et al. (2026)](/sources/pakmor-2026.md)).
* **AMR codes.** CHARM uses PPM for cell-centred fluid variables in
  12-solve CTU with face-centred CT
  ([Miniati & Martin (2011)](/sources/miniati-martin-2011.md)). Chombo-based
  PLUTO offers linear, PPM or WENO tracing with GLM cleaning
  ([Mignone et al. (2012)](/sources/mignone-2012.md)). CASTRO uses unsplit
  PPM without MHD ([CASTRO](/software/castro.md)).
* **Relativistic MHD.** WENO or PPM in the primitive vector, with the
  four-velocity reconstructed
  ([Balsara & Kim (2016)](/sources/balsara-kim-2016.md)).
* **Fourth order.** PPM4 in the McCorquodale–Colella fourth-order FV
  method, also for the corner states of the UCT EMF
  ([Felker & Stone (2018)](/sources/felker-2018.md);
  [UCT](/methods/upwind-constrained-transport.md)).

The limiter formula printed in the primary source carries a typo
(eq. 1.8 duplicates one difference term), a concrete instance of the
"original PPM limiter" typos that Felker & Stone report; see the
[source page](/sources/colella-woodward-1984.md).

# Citations

1. [Colella & Woodward (1984)](/sources/colella-woodward-1984.md), §§1–5, eqs. 1.4–1.17, 3.2–3.7, 4.1–4.5, Appendix.
2. [Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md), §§1, 3.
3. [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md), §§1, 3–4.
4. [Stone, Gardiner, Teuben, Hawley & Simon (2008)](/sources/stone-2008.md).
5. [Almgren et al. (2010)](/sources/almgren-2010.md), §§5, 6.1.
6. [Felker & Stone (2018)](/sources/felker-2018.md), §§3–4.
7. [Miniati & Martin (2011)](/sources/miniati-martin-2011.md).
8. [Mignone et al. (2012)](/sources/mignone-2012.md).
9. [Balsara & Kim (2016)](/sources/balsara-kim-2016.md), §2.
10. [Pakmor et al. (2026)](/sources/pakmor-2026.md).
