---
type: Method
title: "AMR projection method"
description: "Subcycled projection-method incompressible flow on patch hierarchies: MAC-projected advection velocities, approximate nodal projections, and elliptic synchronization at interfaces."
status: established
aliases: [adaptive projection, IAMR method]
tags: [amr, projection, incompressible, subcycling, synchronization]
timestamp: 2026-10-08T00:00:00Z
---

# AMR projection method

The extension of the [projection method](/methods/projection-method.md) to
subcycled [block-structured AMR](/definitions/block-structured-amr.md),
as consolidated by [Almgren et al. (1998)](/sources/almgren-1998.md) for
variable-density incompressible Navier–Stokes.

## Structure of one level advance

1. **Predict** face-based advection velocities (second-order Godunov
   upwinding with limited slopes).
2. **MAC-project** them: an exact $D_h^{\mathrm{f}}$-constraint solve on
   faces ([MAC method](/methods/mac-method.md)) so all advective fluxes are
   built from a divergence-free half-time velocity — this is what makes
   conservative differencing and
   [free-stream preservation](/properties/free-stream-preservation.md)
   possible.
3. **Advance** conservatively; Crank–Nicolson for diffusion.
4. **Approximately project** the cell-centered end-of-step velocity with
   node-based pressure — approximate because the collocated stencil
   enforces the constraint only to discretization accuracy, trading
   exactness for robustness on the cell-centered data Godunov schemes want.

## The synchronization suite

Subcycling leaves four coarse–fine mismatches, each with its own repair:
averaging down; the **MAC sync solve** (elliptic) for the advection-velocity
flux mismatch, whose gradient re-advects the level; **refluxing**, which
for viscous flow becomes *elliptic refluxing solves*
([refluxing](/methods/refluxing.md)); and the composite **sync projection**
restoring the Neumann matching the level projections could not see. The
lesson generalizing beyond incompressible flow: for elliptically
constrained systems, interface consistency is itself an *elliptic* problem —
local flux fixes are not sufficient, and skipping the elliptic
synchronization demonstrably costs accuracy.

## Tree-based, collocated variant

[Blomquist, West, Binswanger & Theillard (2024)](/sources/blomquist-2024.md) project node-collocated velocities on non-graded quadtrees and octrees,
with no subcycling and no synchronization suite: the tree is one mesh, and
hanging nodes at T-junctions get ghost values.
* **The divergence's ghost rule decides stability.** Using the same
  third-order ghost interpolation for the divergence as for the gradient
  and Laplacian is unstable. Quadratic, linear, ENO and WENO ghost
  interpolation are all stable in tests, and the stability condition
  depends on that rule alone.
* **A first-order divergence on purpose.** The divergence uses the plain
  central formula, first-order accurate on the adaptive stencil, because
  the second-order weighted form leads to instability in the purely nodal
  setting.
* Second order overall, randomly refined quadtrees included; CFL up to 10
  on oscillating and fixed cylinders.

*Compiler reading:* this is the incompressible counterpart of the
divergence-at-seams theme of this bundle. At an AMR interface the
stability of the constraint step is set by how the divergence reaches
across the level jump, not by the interior operators, just as the
[seam divergence source](/results/collocated-seam-divergence-source.md) is
set by the seam operator.

## Constraint class

Tolerance-level, twice over: solver tolerance in the MAC/sync solves and
discretization-level looseness in the approximate nodal projection — the
weakest-held divergence among the AMR strategies in this bundle (contrast
[electric-field correction](/methods/electric-field-correction.md)'s
algebraic exactness on staggered data), accepted deliberately for
compatibility with cell-centered Godunov advection and general low-Mach
extensions.

# Citations

1. [Almgren et al. (1998)](/sources/almgren-1998.md), §§2–3.
2. [Blomquist, West, Binswanger & Theillard (2024)](/sources/blomquist-2024.md), §§3.3–3.4, 4–5.
