---
type: Method
title: "Constrained transport (CT)"
description: "Evolves face magnetic fluxes from once-computed edge EMFs so the discrete divergence of the field is conserved identically."
status: established
aliases: [CT]
tags: [constrained-transport, staggered, mhd, induction-equation]
timestamp: 2026-10-08T00:00:00Z
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
* **Embedded boundaries:** on a Cartesian mesh cut by a non-conforming
  wall or material interface, extrapolated ghost fields are not solenoidal,
  but they reach the active faces only through $E_h$. The invariant
  therefore survives in the active domain, while magnetic flux through the
  boundary is not conserved. A two-material interface keeps one global
  $B_h$ with fraction-weighted edge EMFs; one field per side would create
  monopoles
  ([embedded-boundary CT](/methods/embedded-boundary-constrained-transport.md);
  [Jones, McNally & Reynolds (2026)](/sources/jones-2026.md)).

## High-order extension

The scheme's divergence guarantee is a statement about cell/face *averages*;
above second order it survives only if the reconstruction of point values is
itself [divergence-free](/methods/divergence-free-reconstruction.md), and
the corner EMF becomes a genuinely two-dimensional four-state upwind flux
rather than an average —
[Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md), who
build a third-order ENO-based CT scheme on these two ingredients.
Their 2004 formalization,
[upwind constrained transport](/methods/upwind-constrained-transport.md),
says where the exact invariant lives on point values. The evolved primary
data are deconvolved face variables, whose point-value divergence is
preserved to machine precision. The point values that feed the fluxes are
recovered by an implicit inversion, so their divergence is exact only to the
inversion's precision ($10^{-7}$–$10^{-6}$ maxima at third order)
([Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md),
Appendix A). High-order CT on point values therefore holds the invariant on
a variable that the fluxes never see directly.

**A second-order CT step caps a high-order code.** With fifth-order
finite-difference WENO fluxes, the second-order CT of Ryu et al. (1998)
gives second-order convergence on 3D linear and circularly polarized
Alfvén waves. [Seo & Ryu (2023)](/sources/seo-2023.md) restore fifth order with a high-order staggered CT:
* the edge "advective fluxes" ($E_h$) are assembled from WENO-reconstructed
  magnetic fluxes, interpolated to edges at fourth order, and corrected to
  edge point values;
* faces are updated by fourth- or sixth-order central differences of those
  edge values (CT4, CT6);
* the cell-centred field is a sixth-order interpolation of the faces.

Both CT4 and CT6 converge at fifth order, at almost the same cost as the
second-order step. The paper states that the divergence is preserved "up
to the numerical truncation error"; its rotor diagnostic saturates there.
*Compiler reading:* each face update is a difference, along one axis, of
a single-valued edge array, and the divergence is evaluated with the
matching one-axis differences. Differences along different axes commute on
a tensor-product grid, so the update preserves that divergence identically,
as in [exact discrete divergence](/properties/exact-discrete-divergence.md).
The paper's "truncation" wording therefore probably refers to the
saturation level of its diagnostic rather than to a defect of the identity;
the text alone does not settle it.

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

**Unstaggered CT via the potential.** A second collocated line evolves a
collocated potential and replaces the predicted field with its central
curl, which holds $D_h^{\mathrm{c}} B_h = 0$. It runs from Tóth and Rossmanith
at second order to fourth order in
[Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md). See
[vector-potential evolution](/methods/vector-potential-evolution.md).

# Examples

Evans & Hawley calibrate CT against three vector-potential codes on Cartesian
square-wave advection, radial accretion onto a Schwarzschild hole, closed
field-loop infall, and accretion-disk formation; the divergence diagnostic
holds at $\sim 10^{-15}$ (double precision) through all runs.
In [Tóth (2000)](/sources/toth-2000.md)'s ten-problem shock-capturing
comparison, flux-CT ranks among the three most accurate and reliable schemes.
In production, CT runs on tree-based (octree) AMR in RAMSES-MHD with
2D-Riemann edge EMFs ([Fromang et al. (2006)](/sources/fromang-2006.md)),
and in Athena via unsplit CTU with the upwind-biased $\mathcal{E}^c$ EMF
([Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md)) — where
dimensional splitting is ruled out on principle (the constraint couples
all field components, so they must update together), and the scheme
reduces exactly to its 1D form for grid-aligned flow.

# Citations

1. [Evans & Hawley (1988)](/sources/evans-hawley-1988.md), §II–V.
2. [Tóth (2000)](/sources/toth-2000.md), §4, §7.
3. [Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md), §3–4.
4. [Fromang et al. (2006)](/sources/fromang-2006.md), §2.
5. [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md), §§3–4.
6. [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md), §§2.1, 2.3, Appendix A.
7. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §§1, 3, 6.
8. [Jones, McNally & Reynolds (2026)](/sources/jones-2026.md), §§4, 8.
9. [Seo & Ryu (2023)](/sources/seo-2023.md), §§1, 2.3, 3.1–3.2, 3.6.
