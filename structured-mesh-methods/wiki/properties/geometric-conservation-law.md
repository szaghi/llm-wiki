---
type: Property
title: "Geometric conservation law"
description: "On moving grids the volume element must change exactly as the swept volume of its moving faces: the differential law ∂J/∂t + Σ∂(Jξ^i_t)/∂ξ^i = 0 solved with the same discrete operators as the flow equations makes the Jacobian consistent with the scheme's effective volume and keeps a uniform flow uniform."
status: established
aliases: [GCL, volume conservation law, discrete geometric conservation law]
tags: [gcl, moving-mesh, conservation, metric-identities]
timestamp: 2026-11-08T20:24:00Z
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

# Citations

- [Thomas & Lombard (1979)](/sources/thomas-1979.md) — GCL, modified finite-volume method, applications.
- [Thompson, Warsi & Mastin (1982)](/sources/thompson-1982.md) — Section P.
