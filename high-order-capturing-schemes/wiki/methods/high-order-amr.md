---
type: Method
title: "High-order adaptive mesh refinement for capturing schemes"
description: "Adaptive Cartesian meshes for better-than-second-order schemes: cell-by-cell tree refinement with one-step ADER updates and local time stepping, and block-structured (Berger–Colella) hierarchies with Runge–Kutta time stepping, usually subcycled, where ghost values must match the intermediate stages and refluxing, conservative interpolation and high order pull against each other."
status: established
aliases: [AMR, space-time adaptive mesh refinement, cell-by-cell AMR, local time stepping, high-order AMR, block-structured AMR, subcycling, refluxing]
tags: [amr, ader, single-step, finite-volume, finite-difference, dg, time-discretization]
timestamp: 2026-10-13T00:00:00Z
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

## Block-structured hierarchies with Runge–Kutta time stepping

The Berger–Colella design nests logically rectangular patches. With
subcycling, each level advances with its own step and is recursively
caught up by the finer ones. Fine data are then averaged down, and the coarse cells next to the
fine region are corrected by the difference between coarse and summed
fine fluxes ("refluxing"). Four papers carry it past second order with
method-of-lines time stepping: fourth-order finite volume with RK4,
subcycled
([McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md);
[Owen, Guzik & Gao (2018)](/sources/owen-2018.md);
[fourth-order finite volume](/methods/fourth-order-finite-volume.md)),
and fifth-order finite differences with SSP-RK3, subcycled in
[Wang et al. (2025)](/sources/wang-2025.md) (preprint) and with one
global time step in [Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md)
(no subcycling).

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

**MHD on refined meshes (batch 7).**
* *Divergence-free AMR on a Yee mesh* ([Balsara (2001)](/sources/balsara-2001.md), §§IV–VI). Fine
  faces are prolonged with a divergence-free reconstruction that matches
  the four fine faces under each coarse face (ratio 2; 4 and 8 by
  recursion). Coarse face fields are restricted as the average of the fine
  ones. Coarse faces that only share an edge with the fine patch are then
  corrected by the difference between the space–time average of the fine
  edge electric fields and the coarse one: Berger–Colella refluxing moved
  from faces to edges. Second order, RK2 at Courant number 0.4 on all
  levels with ratio-2 subcycling and proper nesting. The undivided
  divergence stays below $10^{-13}$ in 3D runs; no run without the
  correction is shown ([divergence-free reconstruction](/methods/divergence-free-reconstruction.md)).
* *Cleaning on AMR.* GLM's derivation needs a constant, uniform cleaning
  speed and damping. A damping length set to the finest cell, a time step
  halved by each new level, and level-local time steps all break it; in an
  AMR cloud collapse a time-step-tied cleaning speed inflates the peak
  field by five orders of magnitude over CT ([Tomida et al. (2026)](/sources/tomida-2026.md), §§2.3.3, 3.4;
  [hyperbolic divergence cleaning](/methods/hyperbolic-divergence-cleaning.md)).
* *Entropy-stable GLM on block AMR* gives rotor and Orszag–Tang results
  close to staggered CT in FLASH ([Derigs et al. (2018)](/sources/derigs-2018.md), §§5.3–5.4).

**Later uses (batch 10): cut cells at refinement interfaces.**
* Redistributing small cut cells level by level moves conserved
  quantities into covered coarse cells and fine ghost cells, outside the
  composite solution, and a reflux correction added to a tiny cut cell is
  unstable. The repair, re-redistribution, merges the redistribution
  register with the reflux register and spreads it over uncovered coarse
  neighbours; it restores conservation to round-off but still fails for
  coarse cut cells below a volume fraction of about $10^{-4}$
  ([Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §§2.4, 3.4, 4.1; [state redistribution](/methods/state-redistribution.md)).
* The simpler practice is to keep coarse–fine boundaries off the cut
  cells ([Giuliani et al. (2022)](/sources/giuliani-2022.md), §4) or to refine every cut cell to the finest
  level ([Natarajan et al. (2022)](/sources/natarajan-2022.md), §3.1).
* These three papers and [Wang et al. (2025)](/sources/wang-2025.md) run on
  the AMReX framework, described with its codes on the
  [AMReX and PeleC](/software/amrex.md) page.

**Later uses (batch 15).** *The Berger–Colella algorithm as printed*
([Berger & Colella (1989)](/sources/berger-1989.md), §§2–7). A
second-order, 2D algorithm; the block-structured section above summarizes
it correctly, and the primary source adds:
* *Patches and nesting.* Patch edges lie on coarse-grid lines (no rotated
  patches), which is what makes conservation simple. Proper nesting: a
  fine patch starts and ends at a coarse cell corner, and at least one
  level-$(l-1)$ cell separates level $l$ from level $l-2$ in each
  coordinate direction, except at the physical boundary (§2). The buffer
  of flagged neighbours is "two cells in each direction" as typical (§5)
  and one cell in the test runs (§7); the buffer
  $\lceil 5/r_{\mathrm{AMR}}\rceil + 2$ is McCorquodale and Colella's, not
  part of the 1989 algorithm.
* *Refinement in time.* The same $r_{\mathrm{AMR}}$ in space and time, so
  $\Delta t/h$ is equal on all levels, and only **even**
  $r_{\mathrm{AMR}}$ are allowed, to simplify the error estimator (§2). The
  runs use $r_{\mathrm{AMR}} = 4$ with three levels. Coarse levels advance
  first, and finer levels catch up before the coarse level moves on (§3).
* *The flux register* (§3, eqs. 2–5). For an uncovered coarse cell next
  to a fine grid, the coarse flux through the shared face is replaced by
  the fine fluxes through the $r_{\mathrm{AMR}}$ fine faces, summed over the
  $r_{\mathrm{AMR}}$ fine steps and divided by $r_{\mathrm{AMR}}^2$. The
  register starts as minus the coarse flux, accumulates the fine fluxes
  after each fine step, and is added to the coarse neighbour, times the
  coarse $\Delta t/h_x$, after the last one. Each coarse edge is corrected
  once even where fine grids overlap. Cost about 0.3 % of a run. The paper
  calls it a correction pass, not "refluxing"; averaging down is the
  separate fix-up for covered cells. The [flux](/methods/flux-redistribution.md)
  and [state redistribution](/methods/state-redistribution.md) registers
  of the batch-10 block are merged with this register.
* *Ghost values* (§4). From same-level neighbours where they exist,
  otherwise bilinear interpolation in space and, if needed, linear
  interpolation in time from the coarser level: second order, with no
  limiter and no conservation constraint stated. The interpolation that
  initializes new fine grids is not specified. The fourth- and
  fifth-order ghost-value constructions above replace this step.
* *Error estimation by Richardson extrapolation* (§6). Two steps on a
  grid against one step of twice the size on the grid coarsened by 2 give
  the local truncation error, for any scheme of known order. The estimate
  always flags captured discontinuities, since there it does not shrink
  with $h$; shocks themselves need no refinement, but contacts widen in
  time and do. This is a further refinement criterion beside the
  undivided-difference and second-derivative indicators above.
* *Clustering* (§5). Bisection of a bounding rectangle until the share of
  flagged cells exceeds a minimum (e.g. 60 %), then merging where cheaper.
* *Strong shocks crossing levels, the original mechanism* (§6,
  Figs. 6.1–6.2). Captured fluxes near a shock are $O(1)$ wrong; on a
  uniform grid those errors cancel in time, but at a resolution jump the
  two grids' errors differ and emit $O(1)$ spurious waves, observed to
  scale with the characteristic jump across the shock. Strong shocks "must
  be refined everywhere, if they are to be refined anywhere". Wang et
  al.'s failures of non-conservative interpolation, above, are a further
  mechanism of the same scenario, not a contradiction.
* *Cost* (§7, Tables I–II). Integration 78.29 % and interpolation 12.95 %
  of 5674 s on a Cray X-MP; over 90 % of cell updates are on the finest
  level, which covers about 10 % of the domain, for an estimated factor of
  8 in CPU time and 2.2 or more in memory over a uniform fine grid.

# Citations

1. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §§1, 3, 4, 5.
2. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §§1, 5, 6.
3. [Balsara et al. (2009)](/sources/balsara-2009.md), §1.
4. [McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §§3–4.
5. [Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), §§4–5 (accepted manuscript).
6. [Owen, Guzik & Gao (2018)](/sources/owen-2018.md), §§3.3–3.5, 4.6 (accepted manuscript).
7. [Wang et al. (2025)](/sources/wang-2025.md), §§4–6, Appendix A (arXiv preprint).
8. [Balsara (2001)](/sources/balsara-2001.md), §§IV–VI.
9. [Tomida et al. (2026)](/sources/tomida-2026.md), §§2.3.3, 3.4.
10. [Derigs et al. (2018)](/sources/derigs-2018.md), §§5.3–5.4.
11. [Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §§2.4, 3.4, 4.1 (arXiv v1).
12. [Giuliani et al. (2022)](/sources/giuliani-2022.md), §4 (arXiv v2).
13. [Natarajan et al. (2022)](/sources/natarajan-2022.md), §3.1 (arXiv v1).
14. [Berger & Colella (1989)](/sources/berger-1989.md), §§2–7, Tables I–II.
