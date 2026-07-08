---
type: Method
title: "Yee scheme (FDTD)"
description: "Leapfrog update of Maxwell's curl equations on the Yee lattice: electric field on edges, magnetic field on faces, staggered in space and time."
status: established
aliases: [FDTD, finite-difference time-domain, Yee lattice]
tags: [yee, fdtd, maxwell, staggered, electromagnetics]
timestamp: 2026-07-08T00:00:00Z
---

# Yee scheme (FDTD)

The finite-difference time-domain discretization of Maxwell's curl equations
introduced by [Yee (1966)](/sources/yee-1966.md): on a rectangular lattice,
$E_h$ lives on cell edges and $B_h$ (via $B = \mu H$) on cell faces — the
electromagnetic instance of the
[staggered arrangement](/definitions/staggered-grid.md) — and the two fields
leapfrog in time, offset by half a step. Each face-field update is the
circulation of the four surrounding edge fields; in registry terms
([notation](/notation.md)) the magnetic update is
$$\partial_t B_h = -\,C_h E_h ,$$
second-order in space and time, stable under
$c\,\Delta t < \sqrt{(\Delta x)^2+(\Delta y)^2+(\Delta z)^2}$ (constant
coefficients).

## Properties

* **Boundary conditions by placement.** Yee's stated design driver: with
  tangential $E_h$ DOFs lying *in* a perfectly conducting surface, the PEC
  condition is imposed exactly by zeroing boundary edges; normal-$H$
  vanishing follows. The collocation is chosen for the boundary condition,
  not for the divergence constraint.
* **Divergence preservation — implicit, unstated.** The curl-form update
  gives $\partial_t (D_h^{\mathrm{f}} B_h) = -D_h^{\mathrm{f}} C_h E_h = 0$,
  the same once-per-edge cancellation later made explicit and central by
  [constrained transport](/methods/constrained-transport.md). **Yee (1966)
  itself never states this** — the divergence equations do not appear in the
  paper; the solenoidal reading of the lattice belongs to later literature.
  Structurally, the Yee lattice is the earliest instance in this corpus of
  the full $V_h^1 \xrightarrow{C_h} V_h^2$ edge–face pairing that CT
  reuses for the induction equation.
* **Time staggering** (leapfrog) complements the spatial staggering; the
  scheme is explicit and non-dissipative.

# Examples

TM pulse scattering off a perfectly conducting square (95 time cycles,
$\Delta x = \alpha/8$), validated against Friedlander's closed-form wedge
diffraction along the obstacle edge — agreement "good, even for this coarse
grid spacing" ([Yee (1966)](/sources/yee-1966.md), Figs. 3–7).

# Citations

1. [Yee (1966)](/sources/yee-1966.md), eqs. (5)–(8), (13)–(14), Fig. 1.
