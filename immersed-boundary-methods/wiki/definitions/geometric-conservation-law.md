---
type: Definition
title: "Geometric conservation law"
description: "The discrete requirement that the change of a control volume over a time step equal the volume swept by its moving faces, so that a uniform flow is preserved whatever the motion; for bodies moving across a fixed grid it is violated by stair-step boundaries and by cells changing status, which act as spurious mass sources."
status: established
aliases: [GCL, space-time conservation law, swept-volume condition]
tags: [moving-boundary, conservation, cut-cell, sharp-interface]
timestamp: 2026-11-13T05:47:00Z
---

# Geometric conservation law

For a control volume $V(t)$ whose boundary moves, the **geometric conservation
law** (GCL) states that the change of the volume equals the volume its
boundary sweeps:

$$\frac{d}{dt}\int_{V(t)} dV=\oint_{\partial V(t)}\mathbf u_\Gamma\cdot\mathbf n\,dA ,$$

with $\mathbf u_\Gamma$ the velocity of the moving part of $\partial V$. A
discretization that does not satisfy its discrete form alters a uniform flow
when the control volumes move, even though each flux balance is conservative;
in arbitrary Lagrangian–Eulerian schemes the GCL therefore fixes how the
conserved quantities per volume are recovered from the integrated ones and
must be written for the time integrator actually used
([Schneiders et al. 2016](/sources/schneiders-2016.md), §3.6).

## In space-time form

[Murman, Aftosmis & Berger (2003)](/sources/murman-2003.md), §4, write the
moving cut cell as a space-time cell: the change of cell volume equals the
volume swept by the moving boundary, and a supplementary space-time condition
requires the space-time cell to close. An impermeable moving wall then
contributes only pressure, acting on the projection of the swept wall area
along the spatial axes. Their hierarchy of approximations to the space-time
geometry — a steady solution per step, geometry frozen over the step, and an
approximate space-time area closed by the GCL — keeps conservation discretely
at every level and differs only in accuracy.

## Violation by immersed boundaries on fixed grids

[Seo & Mittal (2011)](/sources/seo-2011.md), §2, show what a finite-difference
sharp-interface method actually conserves when the body moves: mass
conservation is written on full cells bounded by a stair-step surface. The
effective balance carries three error terms: a volume source from cells that
change status ([fresh and dead cells](/definitions/fresh-cell-problem.md)),
discontinuous in time; a transpiration flux due to the shape difference
between the stair-step and the true boundary (for a circle of radius $R$ the
stair-step perimeter is $8R$ against $2\pi R$); and a term from the offset
between the two surfaces, proportional to the near-wall velocity gradient and
non-zero even for a stationary body. They call these geometric conservation
errors. The first term, per fresh or dead cell, scales as $h^d/\Delta t$, so it
grows with the cell volume and with a smaller time step; for a body moving
uniformly at a CFL number of exactly one it vanishes. They identify this term
as the main source of
[spurious pressure oscillations](/definitions/spurious-force-oscillations.md)
and restore the GCL near the body with cut-cell volume and face fractions in
the pressure equation only.

## In moving cut-cell methods

[Schneiders et al. (2016)](/sources/schneiders-2016.md) formulate the GCL for
their predictor–corrector Runge–Kutta scheme, update the cut-cell volumes at
every stage, and give the contents of a cell that disappears into the body to
its neighbours with volume-weighted averaging so that the GCL still holds
(§3.6, §3.8). For a cylinder drifting with a uniform flow they report the mass
loss and the error with and without the GCL (§3.7).

# Citations

- [Murman, Aftosmis & Berger (2003)](/sources/murman-2003.md) — §4.
- [Seo & Mittal (2011)](/sources/seo-2011.md) — §2–§3.
- [Schneiders et al. (2016)](/sources/schneiders-2016.md) — §3.6–§3.8.
