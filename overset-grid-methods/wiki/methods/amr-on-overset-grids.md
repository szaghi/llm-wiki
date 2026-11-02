---
type: Method
title: "Adaptive mesh refinement on overlapping grids"
description: "Block-structured adaptive mesh refinement on composite overlapping grids: Henshaw and Schwendeman build refinement patches on every component grid as restrictions of its mapping, so they move with moving base grids; the page gives the hierarchy, regridding, error estimator and time stepping, the equal-resolution and cost evidence, and the earlier proposals the sources recall."
status: established
aliases: [AMR on overlapping grids, AMR on overset grids, Chimera-AMR, adaptive overlapping grids, moving overlapping grids with AMR, adaptively refined overlapping grids]
tags: [amr, overset-grid, composite-grid, moving-grid, shock-capturing]
timestamp: 2026-11-02T14:54:00Z
---

# Adaptive mesh refinement on overlapping grids

**Adaptive mesh refinement (AMR) on overlapping grids** adds finer grid patches
where an estimate of the error is large, on top of a
[composite overlapping grid](/definitions/composite-overlapping-grid.md)
$\mathcal G=\{G_k\}$. In the construction of
[Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) every component grid
$G_k$, curvilinear or Cartesian, can carry its own block-structured hierarchy
of refinement grids, aligned with its parameter coordinates $\mathbf r$ and
defined as restrictions of its mapping $\mathbf d_k$; when $G_k$ moves, its
refinement grids move with it. The overlapping-grid connectivity then has two
kinds of receptor: points on refinement-grid boundaries that take values from
coarser levels of the same base grid, and points that take values from grids
of other base grids, which change when the grids move (§3.3).

## Origins and earlier proposals

The founding Chimera paper already lists adaptive refinement next to grid
embedding. [Benek et al. (1983)](/sources/benek-1983.md) (p. 373) class
adaptive grid techniques, which change the distribution and possibly the
number of points as the solution develops, as the third way to reduce grid
generation effort. They recall that "Berger has developed an adaptive
refinement method which dynamically embeds finer and finer grids to resolve
flow gradients" and state that "the promise of adaptive methods could be
greatly enhanced by combining them with the other methods discussed
previously", embedding among them.

Henshaw & Schwendeman (2006, §1) recall that AMR combined with overlapping
grids had been considered by Brislawn et al., by Boden & Toro, by Meakin, and
by Henshaw & Schwendeman's own earlier work on reactive flow, on which the
present approach is built. They place their work next to Meakin's moving
overlapping grids with AMR, "although his refinement grids were restricted to
the Cartesian background grids and thus his approach is not as general as the
one presented here" (none of these works is ingested here). Chan (2009, §6)
recalls the same Cartesian-only design as Meakin's off-body grids: multiple
Cartesian blocks with successive refinement levels set by the proximity to the
bodies, which "can also adapt to flow features" and are placed and re-adapted
automatically as the bodies move ([Chan (2009)](/sources/chan-2009.md); see
[OVERFLOW](/software/overflow.md)).

[Picard et al. (2021)](/sources/picard-2021.md) (§1) contrast their
finite-volume Chimera patches with patch-based AMR, which they judge not
suited to introducing a geometric alteration and not allowing non-matching
grids, and recall Chimera combined with AMR for reactive flows (works not
ingested here). Their own refined patch is a static, user-placed finer grid,
not an adaptive one; its patch-to-substrate cell-size ratio is studied on
[shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md).

## Refinement grids as restricted mappings

Henshaw & Schwendeman's hierarchy (§3.3) has the base component grids at
refinement level $l_{\mathrm r}=0$ and each further level a factor
$n_{\mathrm r}$ finer than the previous one, with $n_{\mathrm r}=4$ in all
their computations ($l_{\mathrm r}$, $n_{\mathrm r}$ page-local; the
registry's $\ell(k)$ is Benek's embedding level, a different notion). A
refinement grid $G_{k_r}$ of base grid $G_k$ is defined by
restricting the base mapping to a rectangle of parameter space,
$$\mathbf x=\mathbf d_{k_r}(\mathbf r,t):=\mathbf d_k\big(\mathbf a+\mathrm{diag}(b_1,\dots,b_{n_d})\,\mathbf r,\;t\big),\qquad\mathbf r\in[0,1]^{n_d},$$
with constants $\mathbf a$, $b_m$ (page-local) fixing the extent of the patch;
in 2-D the upper-left quadrant of $G_k$ is $\mathbf a=(0,\tfrac12)$,
$b_1=b_2=\tfrac12$ (§3.3). Three consequences follow, as the
authors state:

- refinement grids move with their base grid and do not move with respect to
  the base grid's parameter coordinates;
- their positions relative to other refinement grids of the same base grid
  never change, so that part of the connectivity survives the motion;
- their positions relative to grids of *other* base grids do change, and the
  refinement-grid points that interpolate from those grids are updated every
  time the grids move.

Interpolation between overlapping grids is "generally determined by a
tensor-product Lagrange interpolant in the parameter space of the donor grid"
(§3.1); the width $q$ and the order used are not stated in this paper. See
[inter-grid interpolation](/methods/inter-grid-interpolation.md).

## Regridding and the error estimator

A regridding step is performed every $n_{\mathrm{regrid}}$ time steps,
typically $n_{\mathrm{regrid}}=2n_{\mathrm r}=8$ (page-local): an error
estimate is computed from the current solution, grid points where it exceeds a
tolerance are flagged, a new set of refinement grids is generated to cover
all flagged points, and the solution is transferred from the old hierarchy to
the new one. Since regridding takes place at a fixed time, "it is effectively
decoupled from the moving grid stage" (§3.3).

The estimator measures first and second undivided differences of the $n_c$
solution components $u_{j,\mathbf i}$, $j=1,\dots,n_c$, plus, for reactive
flow, the truncation error of the reactive source term estimated by the
Runge–Kutta integrator of the source step (Eq. (6)):
$$\mathcal E_{\mathbf i}=\sum_{j=1}^{n_c}\frac1{n_d}\sum_{m=1}^{n_d}\Big(\frac{w_1}{\Lambda_j}\big\lvert\Delta_{0m}u_{j,\mathbf i}\big\rvert+\frac{w_2}{\Lambda_j}\big\lvert\Delta_{+m}\Delta_{-m}u_{j,\mathbf i}\big\rvert\Big)+\frac{w_\tau}{\Lambda_\tau}\,\epsilon_{\mathbf i},$$
where $\Delta_{0m}$, $\Delta_{\pm m}$ are the *undivided* central, forward and
backward differences in direction $m$, $w_1,w_2,w_\tau$ weights, $\Lambda_j$,
$\Lambda_\tau$ scale factors (for example for non-dimensionalization) and
$\epsilon_{\mathbf i}$ the source-term truncation-error estimate (all
page-local). The authors adjust the tolerance on this AMR error estimate so
that at most two or three Runge–Kutta steps of the source integration are
needed per cell (§4.2).

The initial hierarchy is built level by level: the initial condition is
applied on the base grids, the error is estimated, a refinement level is added
where it is too large, the initial condition is re-evaluated on the new
level, and the cycle repeats until the tolerance is met or the maximum number
of levels is reached (§3.4).

## Time stepping

Regridding is the first operation of each time step in Henshaw & Schwendeman's
loop (§3.4, Fig. 6), followed by moving the grids, updating the connectivity,
filling [exposed points](/definitions/exposed-point.md), advancing the
solution, and interpolating the receptors of both kinds; the loop is detailed
on [moving overset grids](/methods/moving-overset-grid.md). A single global
time step serves every component and refinement grid,
$\Delta t=C_{\mathrm{CFL}}\min_k\Delta t_k$ with $C_{\mathrm{CFL}}=0.9$
(page-local), the minimum taken over all grids including the refinement grids
(§4.2, Eq. (13)): the refinement levels are not advanced with smaller local
time steps.

## Evidence

**Equal effective resolution.** On the shock-driven cylinder (a Mach-1.5
shock drives a free rigid cylinder of radius 1/2 in a channel; §6.3.2), the
authors compare three composite grids of the same finest spacing, written
$\mathcal G^{(j,l)}$ for base resolution factor $j$ (spacing $h_j=1/(10j)$)
with up to $l$ refinement levels of ratio 4 (page-local notation): the
uniform $\mathcal G^{(32,0)}$ (about $1.56\times10^6$ points, 8200 of them on
the annulus), $\mathcal G^{(8,1)}$ and $\mathcal G^{(2,2)}$. The cylinder
position, velocity and force histories are "in excellent agreement" (Fig. 18).
The uniform-grid self-convergence rate in the 1-norm is 1.47–1.49 at $t=1$
(Table 5); see [shock–cylinder interaction](/benchmarks/shock-cylinder-interaction.md).

**Cost.** CPU time per step on a 2.2 GHz Xeon Linux desktop with 2 GB
(Table 6):

| part of the step | moving, $\mathcal G^{(32,0)}$ (s) | % | moving + AMR, $\mathcal G^{(8,1)}$ (s) | % |
|---|---|---|---|---|
| flux update | 16.36 | 91.6 | 2.43 | 63.7 |
| boundary conditions | 0.066 | 0.37 | 0.072 | 1.9 |
| interpolation (overlap + AMR) | 0.042 | 0.24 | 0.552 | 14.5 |
| moving-grid generation | 0.66 | 3.7 | 0.164 | 4.3 |
| exposed points | 0.024 | 0.13 | 0.0064 | 0.17 |
| AMR regrid and transfer | 0.00 | 0.0 | 0.211 | 5.5 |
| total (printed) | 17.8 | 100 | 3.81 | 100 |

The authors describe the AMR overhead as "about 20%" altogether for
interpolation and regridding (14.5 % + 5.5 %), still much less than the flux
update, and the moving-grid update as below 5 % in both cases (§6.3.2). The
AMR run is about 4.7 times cheaper per step than the uniform run
*(compiler check, not in the sources: 17.8/3.81)*; the paper does not state a
speed-up.

**Many moving bodies.** In the reactive demonstrations (§7), a CJ detonation
crossing 26 free rigid cylinders is computed with one refinement level
($n_{\mathrm r}=4$) on a base grid of spacing about 1/160 (background
$721\times321$, about 260,000 points in total); the number of component grids,
base plus refinement, ranges from 28 to about 400 during the run (§7.2). In
the detonation initiated by an impulsively moved cylinder, the shock position
converges with resolution while the von Neumann pressure peak is not fully
converged on the finest grid (§7.1, Fig. 21).

## Qualifications

- The rows of Table 6 do not add up to the printed totals: 17.152 s against
  17.8 s (percentages 96.0 %) without AMR, and 3.435 s against 3.81 s
  (90.1 %) with AMR, so about 4 % and 10 % of the time is in parts not listed
  *(compiler check, not in the sources)*.
- The caption of Fig. 19 places the AMR grids "at t = 1", while the text
  (§6.3.2) shows them at $t=1.5$, the last frame of Fig. 16.
- In §7.1 the stated "representative grid spacing" $h_j=2/(5j)$ disagrees by a
  factor 10 with the Cartesian and radial spacings that follow from the
  printed grid definitions ($0.04/j$); it agrees only with the printed
  circumferential point count. Which value is the slip cannot be decided from
  the paper.
- The comparison with Meakin's Cartesian-only refinement is the authors'
  characterization of a work not ingested here.
- The single global time step is the minimum over all grids, refinement
  grids included (Eq. (13)); the paper neither uses nor discusses smaller time
  steps on the refinement levels.

# Citations

- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) — §1 (earlier AMR-overlapping work, Meakin as recalled); §3.1; §3.3 (hierarchy, restriction mapping, Eq. (6)); §3.4 (Fig. 6, initial hierarchy); §4.2 (Eq. (13), source-step tolerance); §6.3.2 (Tables 5–6, Figs. 18–19); §7.1–7.2.
- [Benek et al. (1983)](/sources/benek-1983.md) — p. 373 (adaptive grids and Berger's refinement, as recalled).
- [Chan (2009)](/sources/chan-2009.md) — §6 (Meakin's adaptive off-body Cartesian grids, as recalled).
- [Picard et al. (2021)](/sources/picard-2021.md) — §1 (patch-based AMR and Chimera–AMR, as recalled).
