---
type: Benchmark
title: "Taylor–Green vortex (two-dimensional exact decaying solution)"
description: "The two-dimensional Taylor–Green exact solution of the incompressible Navier–Stokes equations as an overset accuracy test: a periodic vortex array crossed by a rotated overset patch for order of accuracy and kinetic-energy conservation up to Re 1e9, and a translating decaying vortex for interpolation order at high and low cell Reynolds number."
status: established
aliases: [Taylor–Green vortex, decaying Taylor vortex, TGV, Taylor vortex]
tags: [benchmark, incompressible, interpolation, unstructured]
timestamp: 2026-11-02T14:54:00Z
---

# Taylor–Green vortex

The two-dimensional Taylor–Green vortex is an exact, spatially periodic
solution of the incompressible Navier–Stokes equations
$\nabla\cdot\mathbf u=0$,
$\partial_t\mathbf u+(\mathbf u\cdot\nabla)\mathbf u+\nabla p=\nu\nabla^2\mathbf u$
($p$ kinematic, density 1) whose velocity is a single Fourier mode that
decays as $e^{-2a^2\nu t}$ for wavenumber $a$ in each direction, while the
nonlinear term is balanced exactly by the pressure. Because the exact
solution is known at every time, an overset grid laid over it measures the
error introduced by the overlap, and the analytic decay of kinetic energy
measures numerical dissipation. Two sources use it with overset grids, both
for incompressible solvers. Neither uses the three-dimensional Taylor–Green
transition-to-turbulence problem, which has no exact solution.

## Exact solutions as used

With $f(t)=e^{-2a^2\nu t}$, the stationary array

$$\begin{aligned}
u&=-\cos(ax)\sin(ay)\,f,\qquad v=\sin(ax)\cos(ay)\,f,\qquad w=0,\\
p&=-\tfrac14\left[\cos(2ax)+\cos(2ay)\right]f^2
\end{aligned}$$

satisfies the equations exactly *(compiler check, not in the sources)*; the
array $u=\sin(ax)\cos(ay)f$, $v=-\cos(ax)\sin(ay)f$ has the opposite
pressure sign. Adding a uniform velocity $(U,V)$ and evaluating the array at
$(x-Ut,\,y-Vt)$ gives the translating (Galilean-shifted) vortex.

- [Horne & Mahesh (2021, §4.2.1, Eq. 11)](/sources/horne-2021.md) use the
  stationary array with $a=2\pi$ in a triply periodic unit box,
  $L_x=L_y=L_z=1$, so $f=e^{-8\pi^2\nu t}$ (the $z$ direction carries no
  flow).
- [Sharma et al. (2021, §4.3.1, Eq. 29)](/sources/sharma-2021.md) use a
  translating vortex with $a=\pi$ and $(U,V)=(1,1)$:
  $u=1-\cos(\pi(x-t))\sin(\pi(y-t))e^{-2\pi^2\nu t}$,
  $v=1+\sin(\pi(x-t))\cos(\pi(y-t))e^{-2\pi^2\nu t}$, which they call the
  "decaying Taylor vortex". They write the viscosity as $\mu$; the decay
  rate $2\pi^2\mu$ makes it the kinematic viscosity $\nu$ with unit
  density *(compiler check, not in the sources)*. No pressure is printed.

## Cases

**Rotated overset patch on an unstructured GPU solver (Horne & Mahesh
2021, §4.2.1, Figs. 12–14).**
- *Grids.* A background mesh of the periodic box and an empty overset patch
  half the domain size, rotated by $25^\circ$ about each of the three Euler
  axes, with about 30% overlap; the patch surrounds no body, so the test
  isolates the overlap. The solver is a collocated, cell-centred,
  kinetic-energy-preserving finite-volume scheme on unstructured meshes,
  Crank–Nicolson in time, with receptor values reconstructed from the
  overlapping mesh (the authors' supercell interpolant) and injected
  directly into the linear systems, pressure included.
- *Order of accuracy.* Refining both meshes at fixed CFL number, the
  $L_2$ error averaged over $t\in[0,0.5]$ converges at second order in $u$
  and $p$, with errors "several orders of magnitude" below the authors'
  earlier predictor–corrector scheme (Fig. 13). Space and time are refined
  together; no separate temporal-order test is made.
- *Kinetic energy.* With spacing $0.0125$ on both meshes and the time step
  reduced until the result changes by less than 1%, the total kinetic
  energy follows the analytic decay for every Reynolds number tested, up to
  $Re=10^9$ (nearly inviscid); the authors state that the errors at the
  overset boundaries stay bounded (Fig. 14).
- The solver and its pressure formulation are on
  [incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md).

**Translating vortex in a node-centred solver (Sharma et al. 2021,
§4.3.1, Fig. 25).**
- *Grids and solver.* The two-grid overset mesh of their Fig. 7 (a
  Cartesian background with an offset near-body grid), assembled by TIOGA
  with implicit hole cutting so that the fringe gap $d$ shrinks with $h$; a
  second-order node-centred finite-volume scheme with BDF2, all grids
  solved as one linear system with the interpolation equations as
  constraint rows; linear Lagrange interpolation ($q=2$); $t=0.2$, time
  step about 0.1 of the CFL limit, 10 Picard iterations, GMRES to
  $10^{-12}$.
- *Result.* With $\nu=0.001$ (maximum cell Reynolds number about 400 on the
  coarsest mesh) second order is retained; with $\nu=0.5$ (cell Reynolds
  number about 1) linear interpolation fails to retain second order. The
  authors read this through the
  [interpolation-order requirement](/results/interpolation-order-requirement.md):
  when $d\propto h$, linear interpolation suffices for the advective
  (first-order) part but not for diffusion-dominated (second-order)
  behaviour, and they "strongly recommend" higher-order interpolation for
  incompressible flow, since the pressure equation is elliptic. Their
  interpolation experiments are on
  [inter-grid interpolation](/methods/inter-grid-interpolation.md).

## What the cases measure

| Source | Overlap | Interpolation | Measured |
|---|---|---|---|
| Horne & Mahesh (2021) | rotated empty patch, ~30% overlap, unstructured | supercell reconstruction, injected | 2nd order in $u$, $p$; kinetic energy follows the exact decay up to $Re=10^9$ |
| Sharma et al. (2021) | Cartesian overset pair, $d\propto h$ | linear Lagrange, $q=2$ | 2nd order at cell $Re\approx400$; order lost at cell $Re\approx1$ |

## Qualifications

- Horne & Mahesh print the pressure of their Eq. (11) as
  $p=+0.25(\cos4\pi x+\cos4\pi y)f^2$ with the velocity
  $u=-\cos(2\pi x)\sin(2\pi y)f$, $v=\sin(2\pi x)\cos(2\pi y)f$; with unit
  density the momentum balance of that velocity requires
  $p=-\tfrac14(\cos4\pi x+\cos4\pi y)f^2$, and the printed sign belongs to
  the field $u=\sin(2\pi x)\cos(2\pi y)f$, $v=-\cos(2\pi x)\sin(2\pi y)f$
  *(compiler check, not in the sources)*. The density is not stated, and
  the paper does not say which pair its code used.
- Sharma et al. do not state the density or the mesh spacings for this
  case; the cell Reynolds numbers (about 400 and about 1) are theirs.
- Neither paper tabulates the errors; the orders are read from the papers'
  statements, not from their figures.

# Citations

- [Horne & Mahesh (2021)](/sources/horne-2021.md) — §3 (solver, injection of overset reconstructions); §4.2.1, Eq. (11), Figs. 12–14 (rotated patch, second-order convergence, kinetic energy up to $Re=10^9$).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — §3 and Fig. 4 (TIOGA implicit hole cutting, $d\propto h$); §4.3.1, Eq. (29), Fig. 25 (translating decaying vortex, $\nu=0.001$ and $0.5$, recommendation of higher-order interpolation).
