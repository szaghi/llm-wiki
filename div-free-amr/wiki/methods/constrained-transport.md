---
type: Method
title: "Constrained transport (CT)"
description: "Evolves face magnetic fluxes from once-computed edge EMFs so the discrete divergence of the field is conserved identically."
status: established
aliases: [CT]
tags: [constrained-transport, staggered, mhd, induction-equation]
timestamp: 2026-07-08T00:00:00Z
---

# Constrained transport (CT)

A finite-difference formulation of the ideal-MHD induction equation
$\partial_t \mathbf{B} = \nabla \times (\mathbf{V} \times \mathbf{B})$ that
maintains the [exact discrete divergence](/properties/exact-discrete-divergence.md)
of the magnetic field to machine roundoff, introduced by
[Evans & Hawley (1988)](/sources/evans-hawley-1988.md).

## Construction

1. **Integral form, flux as the variable.** The induction equation is placed
   in integral form: the rate of change of magnetic flux $\Phi_S$ through a
   (possibly moving) cell face equals minus the total EMF circulated around
   the face boundary. Fluxes through [staggered](/definitions/staggered-grid.md)
   cell faces — elements of $V_h^2$ — are the fundamental evolved quantities;
   the face field $B_h$ is the area-averaged flux.
2. **Edge EMFs, computed once.** Each cell edge carries one EMF value
   $E_h \in V_h^1$, obtained by any suitable transport approximation (donor
   cell, van Leer monotonic, PPM, …). Every edge EMF is *calculated once* and
   enters the two adjacent face updates it borders with opposite signs.
3. **Update.** In registry terms the scheme is
   $$\partial_t B_h = -\,C_h E_h,$$
   so the divergence is stationary by the complex identity:
   $$\partial_t\,(D_h B_h) = -\,D_h C_h E_h = 0 .$$
   (Evans & Hawley state this as the once-per-edge/twice-per-face sign
   cancellation of their eqs. 4.7/4.13; the identity $D_h C_h = 0$ is the
   compiled form — see the
   [source's notation map](/sources/evans-hawley-1988.md).)

## Properties

* **Transport-scheme agnostic:** no restriction on the order of accuracy of
  the EMF reconstruction; the constraint mechanism is the topology of the
  edge-face assembly, not the interpolant
  [Evans & Hawley (1988)](/sources/evans-hawley-1988.md).
* **Coordinate- and metric-independent:** with the magnetic vector density
  absorbing the metric, the same scheme runs in curvilinear coordinates and
  general-relativistic (3+1) spacetimes unchanged.
* **Moving/adaptive meshes:** the flux-integral form accounts for zone motion
  (grid velocity enters the net transport velocity), which Evans & Hawley
  argue admits adaptive meshes naturally — provided the remap is built from
  the flux-update form; naive differencing of the convective form destroys
  the constraint.
* **Preserves changes only:** initial data must satisfy $D_h B_h = 0$
  (e.g. via edge-differenced vector potential, their eq. 4.17); inflow
  boundaries can inject divergence — monitor a global diagnostic.
* **One-derivative Lorentz force:** compared with evolving the vector
  potential, CT computes currents from a single difference of the evolved
  field, avoiding the anomalous current oscillations produced by second
  differences of monotonically-advected quantities.

## Shock-capturing combinations and the collocated recast

CT as introduced is a finite-difference discretization; it was subsequently
combined with conservative Godunov-type base schemes by supplying the edge
EMF from base-scheme data — the field-CT / flux-CT / transport-flux-CT family
([Flux-CT and the Godunov CT variants](/methods/flux-ct.md);
[Tóth (2000)](/sources/toth-2000.md) §4).

[Tóth (2000)](/sources/toth-2000.md) further proves that these CT variants
are algebraically *identical* to pure finite-volume schemes on the
cell-centered field, conserving a corner-centered divergence
$D_h^{\mathrm{k}} B_h$ exactly —
[CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md).
The constraint mechanism of this family is therefore not staggering per se
but the symmetrized, once-per-edge assembly of the EMF; the staggered and
collocated formulations are two representations of one scheme, each exact in
its own divergence stencil.

# Examples

Evans & Hawley calibrate CT against three vector-potential codes on Cartesian
square-wave advection, radial accretion onto a Schwarzschild hole, closed
field-loop infall, and accretion-disk formation; the divergence diagnostic
holds at $\sim 10^{-15}$ (double precision) through all runs.
In [Tóth (2000)](/sources/toth-2000.md)'s ten-problem shock-capturing
comparison, flux-CT ranks among the three most accurate and reliable schemes.

# Citations

1. [Evans & Hawley (1988)](/sources/evans-hawley-1988.md), §II–V.
2. [Tóth (2000)](/sources/toth-2000.md), §4, §7.
