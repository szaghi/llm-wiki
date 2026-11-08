---
type: Method
title: "Inverse Lax–Wendroff boundary treatment"
description: "High-order finite-difference boundary treatment for hyperbolic conservation laws on Cartesian grids that cut the boundary arbitrarily: at inflow boundaries the PDE is used repeatedly to convert normal derivatives into time and tangential derivatives of the boundary data, ghost values follow from a Taylor expansion, and outflow quantities are extrapolated (WENO-type near shocks)."
status: established
aliases: [ILW, inverse Lax-Wendroff procedure]
tags: [inverse-lax-wendroff, high-order, ghost-cell, hyperbolic, compressible, sharp-interface]
timestamp: 2026-11-08T18:43:00Z
---

# Inverse Lax–Wendroff boundary treatment

A high-order interior scheme on a Cartesian grid needs several ghost points
next to a boundary that cuts the grid arbitrarily: three per direction for a
fifth-order WENO scheme. [Tan & Shu (2010)](/sources/tan-2010.md) fill them
by a Taylor expansion from the boundary point $x_b$,

$$w_j=\sum_{q=0}^{r-1}\frac{(x_j-x_b)^q}{q!}\,\frac{\partial^q w}{\partial x^q}\Big|_{x_b},$$

and obtain the normal derivatives as follows (§2).

- **Inflow (ILW).** Use the PDE repeatedly to write $\partial^q w/\partial x^q$
  at the boundary through time derivatives (and, in 2-D, tangential
  derivatives) of the prescribed boundary data. For $w_t+f(w)_x=0$ with
  $w(x_b,t)=g(t)$: $w_x=-g'/f'(g)$, then $w_{xx}$ from the differentiated equation,
  and so on. It is the inverse of the Lax–Wendroff procedure, which converts
  time into space derivatives; the idea comes from boundary conditions for
  static Hamilton–Jacobi equations.
- **Outflow.** Lagrange extrapolation of order $r$, or least-squares
  extrapolation (plain high-order extrapolation was mildly unstable at subsonic
  outflow); near a shock a **WENO-type extrapolation** with three candidate
  sub-stencils and nonlinear weights degrades gracefully to first order.
- **Systems.** A local characteristic decomposition at the boundary decides
  which characteristic variables are prescribed (ILW) and which are
  extrapolated; when an eigenvalue is near zero ($|M|<0.01$) an extra
  extrapolation equation turns the system into a well-conditioned least-squares
  problem; at a solid wall ($\mathbf u\cdot\mathbf n=0$) the entropy wave is outgoing.
- **Two dimensions.** For a ghost point, find the boundary point on the normal
  through it, rotate to local normal–tangential coordinates, apply ILW in the
  normal direction, and compute tangential derivatives along the boundary from
  analytical data or by least-squares (or WENO) differentiation.

With third-order TVD Runge–Kutta time stepping the boundary data of the
intermediate stages are matched as Carpenter et al. prescribe to keep third
order.

## Stability and accuracy

For linear advection on a quarter plane the semi-discrete scheme with the ILW
inflow condition and the fifth-order linear-weight WENO interior is stable in
the GKS sense, and extrapolation at outflow is stable for every order; in
practice the interior CFL condition is not tightened (§2). The designed fifth
order is observed for 1-D scalar and Euler problems, the 2-D wave equation and
an isentropic vortex on a square and on a disk; the boundary treatment's share
of CPU time is tabulated. A double Mach reflection with the $30^\circ$ wedge not
aligned with the grid and supersonic flow past a circular cylinder test solid
walls with shocks (§3; [shock–obstacle interaction](/benchmarks/shock-obstacle-interaction.md)).

## Relation to other methods

ILW is a [ghost-cell](/methods/ghost-cell-method.md)-type sharp boundary
treatment for high-order finite differences. Tan and Shu (§1) contrast it with
the reflection technique for solid walls, accurate only when grid points are
symmetric about the wall, with finite-volume cut cells, which need $h$-box or
similar devices for the time step, and with second-order embedded finite
differences.

## Simplified ILW with auxiliary points

The simplified ILW obtains only low-order normal derivatives through the PDE
and extrapolates the higher ones; an eigenvalue analysis shows it stable at the
periodic CFL number for every cut fraction only at third order.
[Liu et al. (2024)](/sources/liu-2024.md) build ghost values in two steps —
interpolation to artificial auxiliary points from the interior, then
extrapolation through those values and the ILW boundary derivatives — and
choose the auxiliary-point position so that stability holds with fewer ILW
terms (for third order with two ILW terms, a position parameter
$\alpha\ge0.61$), improving efficiency at the same accuracy
([high-order immersed boundary treatments](/methods/high-order-immersed-boundary.md)).

## Deformable solids

[Liu, Jiang, Shu & Zhang (2025)](/sources/liu-2025.md) extend ILW to
compressible flow interacting with linearly elastic solids: third-order WENO
on a fixed Cartesian grid for the fluid, Lagrangian discontinuous Galerkin
for the solid. At the interface the PDEs of both media and the interface
conditions (continuity of normal velocity, balance of traction) form one
linear system for the normal derivatives, from which follow the fluid ghost
values and the solid's interface fluxes. Without sub-iterations the
treatment stays stable for fluid-to-solid density ratios from $10^{-2}$ to
$10^{2}$, where a weakly coupled ILW becomes unstable at $10^{2}$ (see
[fluid–structure coupling](/methods/fluid-structure-coupling.md)).

# Citations

- [Tan & Shu (2010)](/sources/tan-2010.md) — §1–§3.
- [Liu et al. (2024)](/sources/liu-2024.md) — §1–§4.
- [Liu, Jiang, Shu & Zhang (2025)](/sources/liu-2025.md) — §1–§4.
