---
type: Method
title: "Cut-cell (embedded-boundary) finite-volume method"
description: "Sharp-interface finite-volume method on a Cartesian grid whose cells are clipped by the boundary: volume and face-area fractions describe the geometry, fluxes on the clipped faces and the wall flux enter a conservative update, and the small cut cells are stabilized by merging or redistribution; the compressible (Pember et al.) and incompressible (Ye et al.) founding versions."
status: established
aliases: [embedded boundary method, Cartesian cut-cell method, Cartesian grid method, volume-of-fluid boundary representation]
tags: [cut-cell, embedded-boundary, sharp-interface, finite-volume, conservation, compressible, incompressible]
timestamp: 2026-11-08T17:31:00Z
---

# Cut-cell (embedded-boundary) finite-volume method

A Cartesian grid covers $\Omega$; cells crossed by $\Gamma$ are clipped to
their fluid part, and the finite-volume balance is written on the clipped
control volumes. The geometry enters through the volume fraction
$\kappa_{\mathbf i}$ of each cell and the area fractions $a$ of its faces, plus an
effective wall normal; there are no metric terms and the data structures are
those of the regular grid ([Pember et al. 1995](/sources/pember-1995.md),
§1–§2, Figs. 1–2). The boundary is kept sharp
([sharp and diffuse interfaces](/definitions/sharp-and-diffuse-interface.md))
and the discretization is conservative by construction, but cut cells can be
arbitrarily small ([small-cell problem](/definitions/small-cell-problem.md)).

## Compressible flow: Pember et al. (1995)

For the time-dependent Euler equations (2-D Cartesian and axisymmetric, 3-D)
the single-grid step is explicit and has two parts:

1. An unsplit second-order Godunov method computes fluxes as if the body were
   absent, with states extrapolated into body cells next to the boundary, and
   a **reference state** $\mathbf q^{\mathrm{ref}}$ in every cell.
2. In each cut cell the **conservative update** $\mathbf q^{\mathrm c}$ uses
   area-fraction-weighted face fluxes and a wall flux whose pressure comes
   from a one-dimensional Riemann problem with the normal velocity reflected.
   It is "correct and conservative but potentially unstable", because it
   divides by $\kappa h^d$. A stable but non-conservative **preliminary update**
   weights the conservative and reference updates by the volume fraction, and
   the conservation deficit $\delta\mathbf M_{\mathbf i}$ that this leaves, scaled by
   $(1-\kappa_{\mathbf i})$, is handed to the neighbours by
   [redistribution](/methods/redistribution.md).

The time step follows from the full-cell CFL condition. The single-grid
scheme is coupled to block-structured adaptive mesh refinement (Bell et al.
1994, extending Berger and Colella 1989), with the geometry kept consistent
across levels and refluxing extended to redistribution across coarse–fine
boundaries (§3). Smooth-flow results suggest global second order and first
order at the boundary (§1); with shocks the $L^1$ convergence is about first
order (§4).

## Incompressible flow: Ye et al. (1999)

[Ye et al. (1999)](/sources/ye-1999.md), §2, build a 2-D finite-volume
solver on a cell-centred collocated grid with separately updated face-centre
velocities (after Zang, Street and Koseff), a fractional step with
Adams–Bashforth convection and Crank–Nicolson diffusion, and an integral
pressure Poisson equation.

- $\Gamma$ is a chain of line segments. Cut cells whose centre lies in the
  fluid are clipped; cut pieces whose centre lies in the body are merged into
  neighbours, so the control volumes near $\Gamma$ are trapezoids (sometimes
  triangles or pentagons).
- Fluxes on trapezoid faces, values and normal derivatives, come from a
  compact interpolant linear in one direction and quadratic in the other,
  $w=c_1xy^2+c_2y^2+c_3xy+c_4y+c_5x+c_6$, on six points including
  boundary points; a trapezoid-shrinking test confirms second-order local
  accuracy of the face fluxes (Appendix).
- The pressure operator loses diagonal dominance near cut cells; BiCGSTAB
  preconditioned by line SOR is about six times faster than line SOR in work
  units on a $100\times100$ cylinder case.

Wannier's Stokes flow past a cylinder near a moving wall converges at second
order; [flows past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
in a free stream ($Re=20$–$300$) and in a channel reproduce drag, recirculation
length, Strouhal number and critical Reynolds numbers; tube bundles and a
turbomachinery cascade show complex geometry (§3).

## Qualifications

- Pember et al. (1995, §2.6) require distinct fluid regions to be separated by
  at least one full body cell (no infinitely thin plates) and every cut cell
  to have enough fluid neighbours.
- Ye et al. (1999) treat 2-D only; the interpolation is "in principle
  extendable to three-dimensions".

# Citations

- [Pember et al. (1995)](/sources/pember-1995.md) — §1–§4.
- [Ye et al. (1999)](/sources/ye-1999.md) — §1–§3, Appendix.
