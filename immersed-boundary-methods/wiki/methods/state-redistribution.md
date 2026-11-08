---
type: Method
title: "State redistribution"
description: "Postprocessing stabilization for explicit cut-cell finite volumes: after an unstable update with the full-cell time step, each small cut cell is temporarily merged into a possibly overlapping neighbourhood, and cell values are replaced by overlap-weighted averages of neighbourhood polynomials; conservative, linearity preserving and second order at the cut cells, extended to 3-D, a weighted less dissipative form, diffusion and reacting flows."
status: established
aliases: [SRD, weighted state redistribution, WSRD]
tags: [cut-cell, embedded-boundary, small-cell, conservation, redistribution, amr]
timestamp: 2026-11-08T18:32:00Z
---

# State redistribution

[Berger & Giuliani (2021)](/sources/berger-2021.md) propose state
redistribution (SRD) for the [small-cell problem](/definitions/small-cell-problem.md).
The base finite-volume scheme updates every cell, cut cells included, with a
time step set by the full cells — an update unstable on small cells — and SRD
then postprocesses the **states** (not the fluxes, hence the name, by contrast
with [flux redistribution](/methods/redistribution.md)).

## Algorithm

1. **Neighbourhoods** (preprocessing). Every cell has a merging neighbourhood
   $M_{\mathbf i}$: a small cut cell merges with neighbours until the
   neighbourhood volume exceeds a threshold (half a full cell); a large cell is
   its own neighbourhood. Neighbourhoods may overlap; $N_{\mathbf k}$ counts the
   neighbourhoods containing cell $\mathbf k$.
2. **Weighted averages.** On each neighbourhood
   $\hat{\mathbf q}_{\mathbf i}=\sum_{\mathbf k\in M_{\mathbf i}}(V_{\mathbf k}/N_{\mathbf k})\,\mathbf q_{\mathbf k}\big/\sum_{\mathbf k\in M_{\mathbf i}}V_{\mathbf k}/N_{\mathbf k}$,
   where $V_{\mathbf k}=\kappa_{\mathbf k}h^d$; dividing by the overlap count is what
   keeps overlapping merging conservative, which naive overlapping merging is not
   (§2).
3. **Second order.** A limited least-squares gradient is reconstructed on each
   neighbourhood about its weighted centroid (Barth–Jespersen limiter adapted to
   cut cells).
4. **Recombination.** Each cell's final value is the average, over the
   neighbourhoods that contain it, of their linear reconstructions evaluated at
   the cell centroid.

The result is conservative (proved), linearity preserving (so second order at
the cut cells), and its weights stay bounded as $\kappa\to0$; like flux
redistribution it is not monotone for very small cells, which did not matter in
the tests (§2, §4). Flux redistribution, by contrast, is first order at the cut
cells and not linearity preserving; cell merging has no robust general 3-D
implementation because non-overlapping merged cells can be chosen in many
incompatible ways; $h$-box methods are second order but have not been extended
to 3-D (§1).

## Weighted SRD and production use

[Giuliani et al. (2022b)](/sources/giuliani-2022-b.md) extend SRD to three
dimensions and replace the sharp volume-fraction threshold of the original —
under which a cell just below the threshold is fully merged, an $O(1)$ change for
an $O(10^{-7}h)$ wall shift — by weights $\alpha$ (the cell's own contribution) and
$\beta$ (its neighbours') that switch on smoothly as $\kappa$ decreases and reduce
dissipation (§3). Merging along the boundary normal is less diffusive than
central merging (10–15 % lower errors), and weighted SRD cuts the error of a
supersonic vortex in a quarter annulus by a factor of 2–3 on coarse grids. The
least-squares stencil grows when weighted centroids are too close, and the
scheme falls back to first order where gradients cannot be computed well.
Because SRD only acts on the updated state, it stabilizes advective, diffusive
and reactive updates alike, for compressible and (with a subsequent
projection) incompressible flow (§4–§5). It runs in AMReX-Hydro and the IAMR,
Pele and MFIX-Exa codes with domain decomposition and hybrid parallelism, at a
negligible share of the cost (§6). SRD has also been applied to
discontinuous Galerkin schemes in 2-D.

## Discontinuous Galerkin

[Giuliani (2022)](/sources/giuliani-2022.md) applies state redistribution to
high-order discontinuous Galerkin methods on 2-D curvilinear cut-cell grids:
the solution is $L^2$-projected onto polynomials on each merging neighbourhood
in an overlap-weighted inner product, then projected back and averaged; the
scheme is conservative and preserves polynomials of degree $p$, runs at the
time step of the background cells (volume fractions down to $10^{-9}$), and
converges at order $p+1$ in $L^1$ and between $p$ and $p+1$ in $L^\infty$ on
smooth problems (solid-body rotation, Ringleb-type transonic channel flow);
with curved cut cells the DG scheme is about an order of magnitude more
accurate than a second-order rotated-grid $h$-box method, and a Mach 10 double
Mach reflection is computed with limiting.

## Provable stability

[Berger & Giuliani (2024)](/sources/berger-2024.md) give a weighted SRD whose
weights vanish continuously as a cut cell's volume fraction reaches the
threshold, conservative and constant-preserving, and prove it monotone, total
variation diminishing and GKS stable in many configurations: for first-order
upwinding with merging normal to a ramp of angle up to $45^\circ$ it is monotone,
while $3\times3$ central merging at $45^\circ$ is not; with limiting and SSP
Runge–Kutta the second-order version is TVD. The analysis also explains why the
original SRD worked so well — it is monotone in most configurations.

# Citations

- [Berger & Giuliani (2021)](/sources/berger-2021.md) — §1–§6.
- [Giuliani et al. (2022b)](/sources/giuliani-2022-b.md) — §1–§6.
- [Giuliani (2022)](/sources/giuliani-2022.md) — §1–§6.
- [Berger & Giuliani (2024)](/sources/berger-2024.md) — §1–§5.
