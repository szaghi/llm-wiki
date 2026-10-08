---
type: Method
title: "High-order adaptive mesh refinement for capturing schemes"
description: "Space–time adaptive Cartesian meshes for better-than-second-order schemes: cell-by-cell tree refinement with virtual (ghost) cells filled by projection and averaging, a refinement factor at least the reconstruction degree, conservative coarse–fine fluxes and time-accurate local time stepping made simple by one-step ADER updates."
status: established
aliases: [AMR, space-time adaptive mesh refinement, cell-by-cell AMR, local time stepping, high-order AMR]
tags: [amr, ader, single-step, finite-volume, dg]
timestamp: 2026-10-08T00:00:00Z
---

# High-order adaptive mesh refinement for capturing schemes

**Two strategies** ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §3;
[Zanotti et al. (2015)](/sources/zanotti-2015.md), §5.1). Block-structured
AMR (Berger, Colella, Oliger) nests logically rectangular patches.
*Cell-by-cell* AMR refines individual cells in a tree, close to
unstructured-mesh finite volume, and is "slightly more general". Both
papers use the tree. Most earlier AMR codes (AMRCLAW, AstroBEAR,
RAMSES, NIRVANA, PLUTO-AMR, Colella et al.'s fourth-order scheme) use the
method of lines with Runge–Kutta in time.

**Why the time scheme matters.** Runge–Kutta needs consistent ghost
values at every intermediate stage on every level. A one-step scheme
needs data only at the start of each local step, which makes
time-accurate local time stepping straightforward, and it reduces the
reconstructions and MPI exchanges
([ADER](/methods/ader.md); [Balsara et al. (2009)](/sources/balsara-2009.md), §1;
[Dumbser et al. (2013)](/sources/dumbser-2013.md), §§1, 5;
[Lax–Wendroff (Taylor) time discretization](/methods/taylor-time-discretization.md)).
The element-local space–time predictor needs no neighbour data, so it is
identical on uniform and adaptive grids. Only reconstruction and
coarse–fine fluxes change.

## Rules of the tree

([Dumbser et al. (2013)](/sources/dumbser-2013.md), §3.1.)
* A refined cell gets $r_{\mathrm{AMR}}^d$ children, and each level
  advances with its own step, $r_{\mathrm{AMR}}$ times that of the next
  finer level.
  To keep the WENO reconstruction local on the coarse level,
  $r_{\mathrm{AMR}} \ge K$, the reconstruction degree.
* Cells are active, virtual children (filled by $L^2$ projection of the
  active mother's space–time predictor at the needed time) or virtual
  mothers (recursive averages of their children). Every active cell is
  surrounded by at least $K$ layers of ghost cells on its own level, a
  "micro-patch" on which the uniform reconstruction runs unchanged.
* Node-sharing (Voronoi) neighbours differ by at most one level. Refining
  a cell virtually refines its unrefined neighbours.
* **Fluxes.** At a coarse–fine face the fine cells compute every flux
  on their own steps, using the coarse predictor, which is valid over
  the whole coarse step. Each flux is also accumulated in a virtual
  neighbour of the coarse cell, which later uses the sum and computes
  none. This keeps the scheme conservative.
* **Update order.** The finest level that satisfies the update criterion
  goes first. It takes $r_{\mathrm{AMR}}$ sub-steps before its parent
  takes one.
* **Refinement indicator.** A local estimator of normalized second
  derivatives (Löhner-type, including cross derivatives) of the
  density, with refinement above 0.2–0.25 and recoarsening below
  0.05–0.15. A filter parameter of 0.01 ignores small ripples.
  Refinement is forced one or two cells ahead of moving discontinuities
  ([Zanotti et al. (2015)](/sources/zanotti-2015.md), §5.1).
* **MPI.** Refinement at a processor border propagates through exchange
  lists, and ghost cells carry negative indices. There is no dynamic
  load balancing.

## Cost and benefit

* **Overhead.** The bookkeeping of virtual cells costs at most about 25%
  per element update at fourth order, and the second-order AMR scheme is
  9.4 times cheaper per element update than the fourth-order one
  ([Dumbser et al. (2013)](/sources/dumbser-2013.md), Table 1).
* **Speed-ups over the uniform fine grid.** The 2D explosion runs 3.5
  times faster at equal accuracy. The
  [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) runs 1.8 times
  faster, although most cells are refined. The [MHD rotor](/benchmarks/mhd-rotor.md)
  uses more than five times fewer elements and seven times less CPU
  ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4).
* **High order still pays inside AMR.** On a co-rotating vortex pair,
  which radiates sound about two orders of magnitude larger than the
  vortices, fourth-order AMR at about 10 points per wavelength
  matches the asymptotic far-field signal. Second-order AMR on a grid
  refined twice as much takes comparable CPU but merges the vortices
  spuriously at $t = 281$, which silences the source. On the
  [forward step](/benchmarks/forward-facing-step.md) third order rolls
  up the slip line where second order does not
  ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4).
* **With DG and subcell limiting.** AMR follows the flow features,
  while the [subcell limiter](/methods/a-posteriori-subcell-limiting.md)
  handles discontinuities. Combined, they show Kelvin–Helmholtz
  structure on [two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
  not seen in the original solutions
  ([Zanotti et al. (2015)](/sources/zanotti-2015.md), §6).

# Citations

1. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §§1, 3, 4, 5.
2. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §§1, 5, 6.
3. [Balsara et al. (2009)](/sources/balsara-2009.md), §1.
