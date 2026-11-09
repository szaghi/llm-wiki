---
type: Method
title: "Moving mesh partial differential equations"
description: "Continuous equations for the node motion of a mesh with a fixed number of points, derived from the equidistribution principle and solved together with the physical PDE; versions with a relaxation term that pulls the mesh back toward equidistribution are stable and provably free of mesh crossing, unlike the plain time-differentiated principle."
status: established
aliases: [MMPDE, MMPDE4, MMPDE5, MMPDE6, r-adaptivity, dynamic mesh adaptation]
tags: [moving-mesh, adaptation, monitor-function]
timestamp: 2026-11-08T20:24:00Z
---

# Moving mesh partial differential equations

Adaptive methods for time-dependent problems are **static** — a new mesh,
possibly with a different number of points, is built at chosen times and the
solution interpolated onto it — or **dynamic** (moving mesh): a fixed number
of nodes moves under a mesh equation with node velocities, solved together
with the physical equation, so no interpolation is needed
([Huang, Ren & Russell 1994](/sources/huang-1994.md)).

## From equidistribution to node motion

[Huang et al. (1994)](/sources/huang-1994.md) write continuous moving mesh
equations (MMPDEs) behind several discrete ones and derive new ones from the
[equidistribution principle](/definitions/equidistribution-principle.md):

- **MMPDE1**, the time derivative of the quasi-static principle, has no
  restoring term: its deviation from equidistribution depends on the initial
  mesh, and meshes can cross.
- Adding a relaxation toward equidistribution over a time scale $\tau$ gives
  MMPDE2 and its simpler forms, e.g.
  $$\text{MMPDE4: }\ (M\dot x_\xi)_\xi=-\tfrac1\tau(M\,x_\xi)_\xi,\qquad\text{MMPDE5: }\ \dot x=\tfrac1\tau(M\,x_\xi)_\xi,\qquad\text{MMPDE6: }\ \dot x_{\xi\xi}=-\tfrac1\tau(M\,x_\xi)_\xi,$$
  with $\dot x=\partial_t x|_\xi$.

The source-like term $(M x_\xi)_\xi$ measures how far the mesh is from
equidistribution; it moves the mesh even when $M$ does not change, stabilizes
it, and pulls it back. MMPDE2–4 and MMPDE6 are proved free of mesh crossing
under weak assumptions, and no crossing was observed for MMPDE2–7 in
computation; the deviation from equidistribution is small for small $\tau$.
Solving an MMPDE to steady state also produces an equidistributed initial
mesh.

Variational generators with solution-dependent weights pursue the same
concentration of points in several dimensions
([variational grid generation](/methods/variational-grid-generation.md)).
On moving grids the discretization must respect the
[geometric conservation law](/properties/geometric-conservation-law.md).

# Citations

- [Huang, Ren & Russell (1994)](/sources/huang-1994.md) — §1–§3, §5.
