---
type: Method
title: "Cut-cell (embedded-boundary) finite-volume method"
description: "Sharp-interface finite-volume method on a Cartesian grid whose cells are clipped by the boundary: volume and face-area fractions describe the geometry, fluxes on the clipped faces and the wall flux enter a conservative update, and the small cut cells are stabilized by merging or redistribution; the compressible (Pember et al.) and incompressible (Ye et al.) founding versions."
status: established
aliases: [embedded boundary method, Cartesian cut-cell method, Cartesian grid method, volume-of-fluid boundary representation]
tags: [cut-cell, embedded-boundary, sharp-interface, finite-volume, conservation, compressible, incompressible]
timestamp: 2026-11-13T05:47:00Z
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

## A formally consistent version: Colella et al. (2006)

[Colella et al. (2006)](/sources/colella-2006.md) recast the compressible
embedded-boundary method so that it is formally consistent. Control volumes
are $V_{\mathbf i}=\Upsilon_{\mathbf i}\cap\Omega$ with apertures on the faces and a boundary
face; cells are regular, irregular (cut) or covered, with the state stored at
Cartesian cell centres; all geometric quantities are computed to $O(h^2)$, and a
covered face implies a covered neighbour (a minimum-thickness assumption,
relaxed in their code to several control volumes per cell). The conservative
divergence $(\nabla\cdot\boldsymbol{\mathcal F})^{C}$ sums aperture-weighted fluxes
**interpolated to the face centroids** (linear in 2-D, bilinear in 3-D) plus
the boundary flux and divides by $\kappa_{\mathbf i}h$. This makes the truncation error
$O(h)$ in the irregular cells and their neighbours and $O(h^2)$ elsewhere,
whereas the earlier methods, Pember et al.'s included, have $O(1)$ truncation
errors at the boundary. A modified-equation argument predicts a solution error
$O(h^2)$ in $L^1$, $O(h^{3/2})$ in $L^2$ and $O(h)$ in $L^\infty$ when the boundary is
characteristic, and $O(h^2)$ when it is not; a gas-dynamics wall is
characteristic for particle paths but mostly not for sound waves, so
intermediate rates are expected and measured: second order in $L^1$ for smooth
2-D and 3-D acoustic problems. Fluxes come from an unsplit Godunov method in
primitive variables with fourth-order limited slopes, flattening and
artificial viscosity; states at covered faces are extrapolated along the
boundary normal so that a small cell relaxes towards a locally constant state
around it. The small-cell instability is removed by hybridization with a
non-conservative divergence and [redistribution](/methods/redistribution.md).

## Later assessments

[Mittal & Iaccarino (2005)](/sources/mittal-2005.md) credit the cut-cell
approach with being "globally as well as locally second-order accurate" and
exactly conservative for mass and momentum (Ye et al.'s version), but judge
its extension to three dimensions nontrivial because of complex polyhedral
cells; [Mittal et al. (2008)](/sources/mittal-2008.md), §1, repeat that a
3-D cut-cell implementation had not been accomplished in their line of work
and choose [ghost cells](/methods/ghost-cell-method.md). [Ghias et al. (2007)](/sources/ghias-2007.md),
§1, describe Colella's method as globally second order but locally first
order near the boundary, adequate for inviscid flows without boundary layers.

## Moving embedded boundaries

[Natarajan et al. (2022)](/sources/natarajan-2022.md) move the embedded
boundary through a block-structured adaptive grid (AMReX) for the compressible
Navier–Stokes equations: unsplit cut cells with hybrid divergence and flux
redistribution, a Reynolds-transport form for the moving control volume, and a
flux on the moving boundary face from a Riemann problem whose exterior state is
the reflection of the cut-cell state with the wall velocity
([ghost-cell](/methods/ghost-cell-method.md)-type). Freshly cleared cells take a
volume-weighted average of their valid neighbours
([fresh-cell problem](/definitions/fresh-cell-problem.md)), a uniform flow
around a body moving with it is preserved exactly, viscous wall stresses come
from a third-order least-squares fit, and all cut cells are kept on the finest
level. The mass error of an oscillating piston in a closed cylinder falls with
refinement; the entropy error of a receding-piston expansion fan converges at
first order (§2–§3).

## High order and implicit variants

- [Sharan et al. (2022)](/sources/sharan-2022.md) derive dimensionally split
  finite-difference embedded-boundary stencils, built only along grid lines with
  a shortened first interval, that satisfy discrete primary and secondary
  (energy) conservation in summation-by-parts form with weakly imposed boundary
  data. With non-dissipative centred interiors up to sixth order they are
  provably time stable without artificial dissipation and fourth order globally
  for hyperbolic, parabolic and incompletely parabolic problems, with no
  small-cell problem at CFL 0.5.
- [Xie et al. (2022)](/sources/xie-2022.md) solve a 3-D cut-cell finite volume
  implicitly (PISO), which needs no small-cell treatment, with consistent mass
  and momentum fluxes and a solid-volume source in moving cut cells that
  removes most [spurious pressure oscillations](/definitions/spurious-force-oscillations.md).

## Constrained-transport MHD

[Jones, McNally & Reynolds (2026)](/sources/jones-2026.md) build an embedded
boundary for compressible resistive MHD on the Forrer–Jeltsch cut-cell
scheme (see [small-cell problem](/definitions/small-cell-problem.md)) with a
face-centred staggered constrained-transport induction equation, so that the
discrete magnetic field stays divergence free. Ghost cells are filled by
reflection about the boundary with bilinear interpolation at the image; the
normal magnetic field and the tangential electric field are prescribed on
embedded faces and edges. Magnetic flux is not conserved at the embedded
boundary, but no monopoles are introduced. Moving two-material interfaces use
a [ghost fluid method](/methods/ghost-fluid-method.md). The scheme converges
at second order for smooth problems and at first order with a material
discontinuity.

## Moving bodies across fixed grids, 1993–2018

- [Bayyuk, Powell & van Leer (1993)](/sources/bayyuk-1993.md) move and deform
  bodies across a stationary, solution-adaptive quadtree grid for the Euler
  equations (Roe fluxes, least-squares linear reconstruction, a
  predictor–corrector step, second order in space and time). Each motion step
  coarsens the grid around the bodies, moves them, and rebuilds the cut cells
  down to the intersection level, so only cells near the bodies are touched;
  [cell merging](/methods/cell-merging.md) removes small, vanishing and
  newborn cells.
- [Murman, Aftosmis & Berger (2003)](/sources/murman-2003.md) split a motion
  into a rigid motion of the whole domain, treated by an arbitrary
  Lagrangian–Eulerian formulation with precomputed rotations of the Cartesian
  face normals and a van Leer flux-vector splitting written with the Mach
  number relative to the moving boundary (Galilean invariant, with a
  consistent energy flux), plus a relative motion of bodies through the fixed
  mesh, analysed in space-time ([geometric conservation law](/definitions/geometric-conservation-law.md)).
  An implicit dual-time scheme lets the time step follow the physics. A
  Mach-2 piston and a pitching NACA 0012 airfoil match the exact solution and
  experiment (§5).
- [Meinke et al. (2013)](/sources/meinke-2013.md) and
  [Schneiders et al. (2013)](/sources/schneiders-2013.md) build a
  three-dimensional viscous compressible cut-cell method on octree grids with
  boundaries from a level set $\phi$, whose discrete operator changes smoothly
  as the boundary moves ([spurious force oscillations](/definitions/spurious-force-oscillations.md));
  Meinke et al. use separate level sets for independently moving parts, such
  as a valve and a cylinder head, and a modified marching-cubes algorithm for
  cells cut several times or split into unconnected parts.
- [Schneiders et al. (2016)](/sources/schneiders-2016.md) extend it to freely
  moving rigid bodies and add a predictor–corrector reformulation of the
  low-storage multistage Runge–Kutta scheme: each stage combines the residual
  at $t^n$, stored from the previous step, with the residual at $t^{n+1}$, so
  the stability polynomial is unchanged but the cut-cell geometry and the
  least-squares systems are built once per step instead of once per stage —
  1.4 to 2.5 times faster for five stages, second order in time (§3.2, §5.1).
- [Bennett, Nikiforakis & Klein (2018)](/sources/bennett-2018.md) move rigid
  bodies through a dimensionally split cut-cell scheme with flux
  stabilization ([small-cell problem](/definitions/small-cell-problem.md)),
  using time-averaged boundary geometry over each step. The cut cells are
  locally first order and the global error approaches second order under
  refinement; the scheme is not strictly conservative, and the mass error of
  a wedge passing a shock depends on resolution and on where the wedge's
  corners fall in the cells.

# Citations

- [Pember et al. (1995)](/sources/pember-1995.md) — §1–§4.
- [Ye et al. (1999)](/sources/ye-1999.md) — §1–§3, Appendix.
- [Mittal & Iaccarino (2005)](/sources/mittal-2005.md) — discrete-forcing section (cut cells).
- [Colella et al. (2006)](/sources/colella-2006.md) — §1–§5.
- [Ghias et al. (2007)](/sources/ghias-2007.md) — §1.
- [Mittal et al. (2008)](/sources/mittal-2008.md) — §1.
- [Natarajan et al. (2022)](/sources/natarajan-2022.md) — §2–§3.
- [Sharan et al. (2022)](/sources/sharan-2022.md) — §1–§5.
- [Xie et al. (2022)](/sources/xie-2022.md) — §2–§4.
- [Jones, McNally & Reynolds (2026)](/sources/jones-2026.md) — §3–§4, §7.
- [Bayyuk, Powell & van Leer (1993)](/sources/bayyuk-1993.md) — whole paper.
- [Murman, Aftosmis & Berger (2003)](/sources/murman-2003.md) — §2–§5.
- [Meinke et al. (2013)](/sources/meinke-2013.md) — §3.
- [Schneiders et al. (2013)](/sources/schneiders-2013.md) — §3–§4.
- [Schneiders et al. (2016)](/sources/schneiders-2016.md) — §3, §5.
- [Bennett, Nikiforakis & Klein (2018)](/sources/bennett-2018.md) — §2–§4.
