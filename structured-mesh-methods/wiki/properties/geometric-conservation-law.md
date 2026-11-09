---
type: Property
title: "Geometric conservation law"
description: "On moving grids the volume element must change exactly as the swept volume of its moving faces: the differential law ∂J/∂t + Σ∂(Jξ^i_t)/∂ξ^i = 0 solved with the same discrete operators as the flow equations makes the Jacobian consistent with the scheme's effective volume and keeps a uniform flow uniform."
status: established
aliases: [GCL, volume conservation law, discrete geometric conservation law]
tags: [gcl, moving-mesh, conservation, metric-identities]
timestamp: 2026-11-08T20:37:00Z
---

# Geometric conservation law

## Statement

[Thomas & Lombard (1979)](/sources/thomas-1979.md) observe that a
finite-volume scheme on moving cells implicitly solves an integral law for
cell volume, $\frac{d}{dt}\int_V dV=\oint_{\partial V}\dot{\mathbf x}\cdot d\mathbf S$,
which they call the **geometric conservation law**. In curvilinear
coordinates the Jacobian $J$ multiplies the solution inside the time
derivative, $\partial_t(J\mathbf q)|_{\boldsymbol\xi}$, and its differential
counterpart is

$$\partial_t J\big|_{\boldsymbol\xi}+\sum_i\frac{\partial(J\xi^i_t)}{\partial\xi^i}=0,\qquad \xi^i_t=-\dot{\mathbf x}\cdot\mathbf a^i$$

([notation](/notation.md)).

## Why it matters discretely

The $J$ used to recover $\mathbf q$ from $J\mathbf q$ must equal the
effective volume element that the difference scheme implies; computing it by
arbitrary geometric formulas on a time-varying grid introduces errors, a
point Thomas and Lombard say "apparently has not been recognized previously".
Their remedy is to integrate the differential law **with the same difference
scheme** as the flow equations; at interior points the result coincides with
the finite-volume method (with central differences) without any geometric
construction of volumes and face areas.

The test is uniform flow. A spatially uniform state must stay uniform
($\Delta\mathbf q=0$). On a fixed grid this requires the discrete
[metric identities](/properties/free-stream-preservation.md); on a moving grid
it requires in addition that the discrete geometric conservation law hold.
Thomas and Lombard apply it to implicit (Beam–Warming) unsteady
Navier–Stokes solutions on moving grids and to explicit MacCormack marching of
steady supersonic flow; Thompson, Warsi and Mastin (1982, Section P) list
the conservation-law forms of the time-dependent equations that make the
time variation of $J$ explicit.

## Time metrics at high order

[Visbal & Gaitonde (2002)](/sources/visbal-2002.md) split the time derivative
as $\partial_t(J\mathbf q)=J\,\partial_t\mathbf q+\mathbf q\,\partial_tJ$ (not strictly
conservative in time, so not meant for fast strong shocks) and take
$\partial_tJ$ not from the grid coordinates but from the law itself,
$\partial_tJ=-\sum_i\delta_i(J\xi^i_t)$, with
$\xi^i_t=-\dot{\mathbf x}\cdot\mathbf a^i$ and the conservatively evaluated
spatial metrics. The free-stream residual then regroups into the four
discrete identities, which all vanish, whatever way the grid velocities are
obtained, analytically or numerically; an analytic $\partial_tJ$ brings back
errors like those of analytic spatial metrics. With sixth-order compact
schemes and filters this keeps a uniform flow uniform on rapidly deforming
meshes (pitching airfoil, fluttering panel). [Deng et al. (2011)](/sources/deng-2011.md)
call this part the volume conservation law and the spatial part the surface
conservation law ([free-stream preservation](/properties/free-stream-preservation.md)).

# Citations

- [Thomas & Lombard (1979)](/sources/thomas-1979.md) — GCL, modified finite-volume method, applications.
- [Thompson, Warsi & Mastin (1982)](/sources/thompson-1982.md) — Section P.
- [Visbal & Gaitonde (2002)](/sources/visbal-2002.md) — §4.3.
- [Deng et al. (2011)](/sources/deng-2011.md) — §1.
