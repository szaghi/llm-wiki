---
type: Method
title: "High-order adaptive mesh refinement for capturing schemes"
description: "Adaptive Cartesian meshes for better-than-second-order schemes: cell-by-cell tree refinement with one-step ADER updates and local time stepping, and block-structured (Berger–Colella) hierarchies with Runge–Kutta subcycling, where ghost values must match the intermediate stages and refluxing, conservative interpolation and high order pull against each other."
status: established
aliases: [AMR, space-time adaptive mesh refinement, cell-by-cell AMR, local time stepping, high-order AMR, block-structured AMR, subcycling, refluxing]
tags: [amr, ader, single-step, finite-volume, finite-difference, dg, time-discretization]
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
  $r_{\mathrm{AMR}} \ge K$, the reconstruction degree. The rule belongs
  to this tree design, where reconstruction runs on micro-patches of the
  coarse level. Block-structured codes below run fourth and fifth order
  with $r_{\mathrm{AMR}} = 2$, because they interpolate ghost values
  instead.
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

## Block-structured hierarchies with Runge–Kutta subcycling

The Berger–Colella design nests logically rectangular patches. Each level
advances with its own step and is recursively caught up by the finer
ones. Fine data are then averaged down, and the coarse cells next to the
fine region are corrected by the difference between coarse and summed
fine fluxes ("refluxing"). Three papers carry it past second order with
method-of-lines time stepping: fourth-order finite volume with RK4
([McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md);
[Owen, Guzik & Gao (2018)](/sources/owen-2018.md);
[fourth-order finite volume](/methods/fourth-order-finite-volume.md)),
and fifth-order finite differences with SSP-RK3
([Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), no subcycling;
[Wang et al. (2025)](/sources/wang-2025.md), preprint).

**Ghost values in time must match the stages.** The coarse RK4 stages
give a cubic dense output (Fok–Rosales),
$$u(t^n + \chi\Delta t) = u^{(0)} + \chi k_1 + \tfrac12\chi^2(-3k_1 + 2k_2 + 2k_3 - k_4) + \tfrac23\chi^3(k_1 - k_2 - k_3 + k_4) + O(\Delta t^4),$$
with $k_m = \Delta t\,\mathcal L(u^{(m-1)})$ and $0 \le \chi \le 1$ the fraction of
the coarse step. Evaluating it at the fine stage times is fourth order,
but it does not match the fine intermediate *stages*, and that mismatch
sets off the limiter on smooth data. The ghost values are instead built
to match the Taylor expansions of the stage values, using the dense
output's derivatives and $4(k_3 - k_2)/\Delta t^2$ for the one term that
is not a time derivative
([McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §3.1,
eqs. 39–49). On a shear flow with the limiter on, the naive version
converges at rates 3.75, 1.39 and 1.59, "not even second order", against
4.05, 3.95 and 3.98 for the stage-matched one (Table 5). The same issue
appears for SSP-RK3, with the quadratic dense output
$u^n + \chi k_1 + \left(-\tfrac56k_1 + \tfrac16k_2 + \tfrac23k_3\right)\chi^2$
([Wang et al. (2025)](/sources/wang-2025.md), §4.2.3, eq. 15; its
stage-matched formulas are not printed). It is the AMR form of the
boundary-data problem inside Runge–Kutta stages
([SSP Runge–Kutta](/methods/ssp-runge-kutta.md);
[inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md)).

**Ghost values in space.**
* *Finite volume:* a constrained least-squares cubic over 12–13 coarse
  cells in 2D (31–33 in 3D). It matches the coarse cell average exactly,
  so it is conservative, and the neighbours in the least-squares sense.
  The same operator is used for regridding
  ([McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §3.2).
* *Finite differences:* dimension-by-dimension 1D interpolation, fifth
  order where possible (fourth in a few corner cases), limited by an
  MP-like limiter for non-uniform stencils. Coarse ghost cells are
  restricted on the fine block and sent; fine ghost cells are prolonged
  locally. Three ghost layers and blocks of at least 6 cells suffice
  ([Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), §4;
  [monotonicity-preserving limiting](/methods/monotonicity-preserving-limiter.md)).
  With second-order ghost cells instead, the global $L^1$ order falls
  from 5 to 2 (Table 2).
* *WENO interpolation:* Sebastian–Shu-type WENO interpolation for
  prolongation, and a symmetric six-point WENO interpolation for
  restriction ([Wang et al. (2025)](/sources/wang-2025.md), §4.2,
  Appendix A).

**Refluxing, conservation and order.** These three pull against each
other in finite differences.
* *Finite volume* refluxes the RK4 total flux, including the
  artificial-viscosity increment. Truncation error is $O(h^4)$ away from
  coarse–fine boundaries and $O(h^3)$ at them, and the observed max-norm
  order is about $15/4$ ([McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §§3, 4.2).
* *Finite differences without refluxing.* Refluxing would make the FD
  scheme second order next to the jump, so it is omitted, and
  conservation holds only to truncation error there. Because the
  resolution changes are lower-dimensional sets, the $L^1$ order stays 5
  even where the $L^\infty$ order drops to 3. Mass errors on a square wave
  stay below $4\times10^{-4}$ over 10 periods without accumulating
  ([Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), §§4.3–4.5, 5.4).
* *Finite differences with refluxing.* Storing the FD point values at
  cell centres puts the patch boundaries on flux points, so refluxing
  applies. The conservation error then converges at second order instead
  of fifth, which the authors accept for robustness. Prolongation and
  restriction stay non-conservative in smooth regions
  ([Wang et al. (2025)](/sources/wang-2025.md), §§4.1, 6.1).

Chen et al. and Wang et al. agree on the order effect of refluxing in
finite differences and choose differently. This is a design trade-off,
not a contradiction.

**Shocks crossing levels** ([Wang et al. (2025)](/sources/wang-2025.md),
§§5–6; preprint). Non-conservative WENO interpolation fails in three
scenarios. Inside the finest level it is harmless. A shock crossing a
coarse–fine interface accumulates conservation errors. Refining or
coarsening a shock is the worst: WENO restriction picks one-sided values
and steepens the shock artificially. The proposed hybrid uses WENO
interpolation in smooth cells and second-order conservative interpolation
in troubled cells, flagged by a Lax entropy condition on Roe-averaged
speeds plus a mapped pressure curvature. With pure WENO or Lagrange
interpolation, the [double Mach reflection](/benchmarks/double-mach-reflection.md)
produces negative density at once, a Mach 3 shock crossing a static
interface fails, and decaying isotropic turbulence at turbulent Mach 1
blows up at about 3.4 eddy turnover times. The hybrid survives all three.
On [Sod](/benchmarks/sod-shock-tube.md) and [Lax](/benchmarks/lax-shock-tube.md)
with infrequent regridding, WENO interpolation gives oscillations and a
wrong shock speed. There is no stability analysis of the hybrid.

**Refinement indicators.** Normalized undivided differences with
thresholds 0.05–0.1, combined by logical OR. The authors of that indicator
note that a criterion consistent with fourth order is still open
([Owen, Guzik & Gao (2018)](/sources/owen-2018.md), §3.5). Density
gradients ([Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), §5.7;
[McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §4.2).

**Cost.** Fifth-order FD AMR costs about 3 times the second-order scheme,
on uniform and adaptive grids alike. Ghost-cell filling takes 6.88 s of
22.42 s on 32 processors for double Mach reflection
([Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), Table 6).

# Citations

1. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §§1, 3, 4, 5.
2. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §§1, 5, 6.
3. [Balsara et al. (2009)](/sources/balsara-2009.md), §1.
4. [McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §§3–4.
5. [Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), §§4–5 (accepted manuscript).
6. [Owen, Guzik & Gao (2018)](/sources/owen-2018.md), §§3.3–3.5, 4.6 (accepted manuscript).
7. [Wang et al. (2025)](/sources/wang-2025.md), §§4–6, Appendix A (arXiv preprint).
