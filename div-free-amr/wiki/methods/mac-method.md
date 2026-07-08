---
type: Method
title: "MAC method (marker-and-cell)"
description: "Staggered primitive-variable scheme for incompressible flow: a pressure Poisson equation enforces the face-difference velocity divergence to zero each cycle."
status: established
aliases: [marker-and-cell]
tags: [mac, staggered, incompressible, pressure-poisson]
timestamp: 2026-07-08T00:00:00Z
---

# MAC method (marker-and-cell)

The original staggered-grid scheme for time-dependent viscous incompressible
flow, introduced by [Harlow & Welch (1965)](/sources/harlow-welch-1965.md):
primitive variables on the [staggered arrangement](/definitions/staggered-grid.md)
(face-normal velocities, cell-centered pressure $\phi_h$), explicit
finite-difference momentum advancement, and marker particles used only to
track the free surface.

## The constraint mechanism

The incompressibility constraint is discretized as the face-difference
divergence $D_h^{\mathrm{f}} u_h = 0$ in every cell
([notation](/notation.md)). Substituting the discrete momentum equations
into it yields an evolution equation for $D_h^{\mathrm{f}} u_h$; demanding
that the end-of-cycle divergence vanish produces a discrete Poisson equation
$$D_h^{\mathrm{f}} G_h\, \phi_h = -R_h,$$
solved iteratively for the pressure each cycle. Two structural points:

* **Tolerance-level enforcement, self-correcting.** The constraint holds to
  the accuracy of the iterative Poisson solve — the same guarantee class as
  the later [projection method](/methods/projection-method.md). Crucially,
  the source $R_h$ retains the current $D_h^{\mathrm{f}} u_h/\delta t$ term,
  so divergence left by an imperfect solve enters the next cycle's
  right-hand side with a restoring sign: errors decay instead of
  accumulating.
* **Boundary conditions are derived from the constraint.** Ghost velocities
  at walls and free-surface velocities are chosen exactly so that
  $D_h^{\mathrm{f}} u_h = 0$ holds in exterior/surface cells, and the
  pressure-equation boundary values are made consistent with the same
  requirement — an early instance of the rule that the discrete constraint
  dictates the boundary treatment.

The staggering is what makes the mechanism compact: face velocities and
centered pressure give a two-point-per-direction divergence and a five-point
$D_h^{\mathrm{f}} G_h$ Laplacian with no checkerboard null mode.

# Examples

Broken-dam and sluice-gate flows with free surfaces, validated against the
Martin & Moyce experiments; Rayleigh–Taylor of a falling free surface;
splash problems ([Harlow & Welch (1965)](/sources/harlow-welch-1965.md),
Figs. 5–7). Stability observed without artificial viscosity.

## Afterlife

The face-collocated pressure solve survives as the **MAC projection** — an
intermediate step inside modern schemes: the
[AMR projection method](/methods/amr-projection-method.md) MAC-projects its
face-based advection velocities each step precisely because the compact
$D_h^{\mathrm{f}}$ constraint is the one worth holding exactly on faces
([Almgren et al. (1998)](/sources/almgren-1998.md)).

# Citations

1. [Harlow & Welch (1965)](/sources/harlow-welch-1965.md), eqs. (4)–(10), Figs. 1–4.
2. [Almgren et al. (1998)](/sources/almgren-1998.md), §2.
