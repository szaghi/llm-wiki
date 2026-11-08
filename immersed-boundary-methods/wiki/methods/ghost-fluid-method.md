---
type: Method
title: "Ghost fluid method"
description: "Sharp-interface Eulerian method for multimaterial compressible flow: a level set locates the interface, every grid point near it carries the real fluid and a ghost fluid of the other material whose pressure and normal velocity are copied and whose entropy is extrapolated, and each fluid is advanced with an unmodified single-phase scheme."
status: established
aliases: [GFM, ghost fluid method (Fedkiw), boundary-condition capturing with ghost cells]
tags: [ghost-fluid, sharp-interface, level-set, compressible, multimaterial, ghost-cell]
timestamp: 2026-11-08T18:08:00Z
---

# Ghost fluid method

## Problem

Eulerian shock-capturing schemes smear the density at a material interface,
and when the two sides obey different equations of state the smeared state
produces non-physical pressure oscillations; Lagrangian schemes keep the
interface sharp but fail under large deformation. Earlier Eulerian
interface-Riemann methods needed dimensional splitting and were awkward with
multistage time integrators ([Fedkiw et al. 1999](/sources/fedkiw-1999.md), §1).

## Method

- The interface is the zero level of a level set $\phi$, advected with the
  fluid velocity and reinitialized to a signed distance (§2.2, Appendix).
- At every grid point the real fluid of the side given by the sign of $\phi$
  is stored together with a **ghost fluid** of the other material. Both fluids
  are updated everywhere with a standard single-phase scheme (third-order
  ENO–local Lax–Friedrichs with TVD Runge–Kutta); after each stage the sign of
  $\phi$ selects which result is kept (§3). Only a band of 3–5 ghost cells on
  each side is needed.
- **Ghost state.** The pressure and velocity are continuous across a contact,
  so the ghost pressure and velocity are copied node by node from the real
  fluid; the entropy, the one free quantity of the linearly degenerate field,
  is extrapolated one-sided and constant from the real side, which removes the
  numerical dissipation across the contact. An **isobaric fix** replaces the
  entropy of the interface-adjacent real node with its neighbour's to reduce
  "overheating" errors (§4).
- In multi-D the extrapolation solves $\partial_t I\pm\mathbf n\cdot\nabla I=0$,
  $\mathbf n=\nabla\phi/|\nabla\phi|$, in fictitious time for a few steps after
  every Runge–Kutta stage; for slip lines the tangential velocity is
  extrapolated as well and the normal velocity taken from the real fluid, so a
  tangential jump stays sharp (§4).

"We do not need to solve a Riemann problem, consider the Rankine–Hugoniot
jump conditions, or solve an initial boundary value problem at the
interface": to compute air next to water, the water is replaced by ghost air
that "acts like the water in every way (pressure and velocity) but appears to
be air (entropy)" (§4). The justification offered is the solid-wall
reflection condition: the fluid sees its reflected twin and behaves as if the
boundary were impenetrable.

## Conservation and accuracy

The scheme is formally non-conservative at the interface, where fluxes
between two fluids are not unique; the conservation error is expected to
behave as $O(\Delta x^{n})$ integrated over the interface length. For a helium
bubble advected in air both the $L^1$ density error and the helium mass error
converge at second order (§4.5, Table I). In shock–interface Riemann tests the
contact is located one cell off at all resolutions, first order in position
(§5) — see [discrete conservation](/properties/discrete-conservation.md).

## Results reported

Gamma-law shock tubes, the multicomponent tests of Karni, a 2-D shock tube on
a diagonal, explosive (JWL) gas against water (Tait), gas–water shocks, a water
slab in gas, a shear wave with slip and the Mach 1.22 shock–helium-bubble
interaction (§5).

## Relevance to immersed boundaries

The device — fill values across a sharp $\Gamma$ on a fixed grid so that an
unmodified interior scheme can be applied — is a ghost-cell boundary
treatment; Fedkiw et al. (§4) motivate it from the reflection condition of a
solid wall, the case of an immersed rigid body.

## Descendants for solid walls

[Tseng & Ferziger (2003)](/sources/tseng-2003.md), §1, place the
[ghost-cell immersed boundary method](/methods/ghost-cell-method.md) in the
line of the ghost fluid method, citing also its use by Gibou et al. for a
variable-coefficient Poisson equation on irregular domains.
[Ghias et al. (2007)](/sources/ghias-2007.md), §2.5, and
[Mittal et al. (2008)](/sources/mittal-2008.md), §1, contrast their
normal-direction image-point interpolation with Gibou et al.'s ghost-fluid
extrapolation along Cartesian directions, which becomes ill conditioned for
small distances and falls back to first order.

# Citations

- [Fedkiw et al. (1999)](/sources/fedkiw-1999.md) — §1–§5, Appendix.
- [Tseng & Ferziger (2003)](/sources/tseng-2003.md) — §1.
- [Ghias et al. (2007)](/sources/ghias-2007.md) — §2.5.
- [Mittal et al. (2008)](/sources/mittal-2008.md) — §1.
