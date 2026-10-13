---
type: Method
title: "State redistribution for cut cells"
description: "Post-processing that stabilizes small cut cells under a full time step: merge each small cell with neighbours into an overlapping neighbourhood, average and reconstruct linearly on the neighbourhoods with weights 1/(overlap count), and average the reconstructions back; exactly conservative and linearity-preserving (proved), not monotone, with a weighted variant that switches on smoothly and a re-redistribution register for AMR."
status: established
aliases: [SRD, weighted state redistribution, WSRD, re-redistribution, state redistribution algorithm]
tags: [boundary-treatment, embedded-boundary, conservation, amr]
timestamp: 2026-10-13T00:00:00Z
---

# State redistribution for cut cells

[Berger & Giuliani (2021)](/sources/berger-2021.md) remove the
small-cell time-step restriction of [cut-cell finite volume](/methods/cut-cell-finite-volume.md)
by post-processing states rather than fluxes. Every cell, small cut
cells included, first takes the provisional update $u^{\mathrm{pr}}_i$
with the step of the regular cells (after each stage of a method of
lines, or once for a one-step Godunov scheme). Then (§4, eqs. 35–42):
1. **Neighbourhoods** (preprocessing). A cut cell with
   $\vert I_i\vert < \tfrac12 h^d$ merges with neighbours, preferably in
   the direction of the wall normal, until
   $\sum_{j\in\mathcal N_i}\vert I_j\vert \ge \tfrac12 h^d$; it falls back to
   a centred 3×3, then 5×5 tile. Neighbourhoods may overlap, and
   $N^{\mathrm{ov}}_j$ counts those containing cell $j$.
2. **Average** each neighbourhood with weights $\vert I_j\vert/N^{\mathrm{ov}}_j$:
   $$\bar u^{\mathcal N}_i = \frac{1}{\widehat{\mathcal V}_i}\sum_{j\in\mathcal N_i}\frac{\vert I_j\vert}{N^{\mathrm{ov}}_j}\,u^{\mathrm{pr}}_j,\qquad \widehat{\mathcal V}_i = \sum_{j\in\mathcal N_i}\frac{\vert I_j\vert}{N^{\mathrm{ov}}_j}.$$
3. **Reconstruct** $q^{\mathcal N}_i(\mathbf x) = \bar u^{\mathcal N}_i + \nabla q^{\mathcal N}_i\cdot(\mathbf x - \hat{\mathbf x}_i)$
   about the weighted centroid, with a least-squares gradient from the
   neighbouring neighbourhoods and a Barth–Jespersen limiter.
4. **Average back:** $u^{n+1}_i = \frac{1}{N^{\mathrm{ov}}_i}\sum_{k:\,i\in\mathcal N_k} q^{\mathcal N}_k(\mathbf x_i)$.

**What is proved.** Exact conservation, $\sum_i\vert I_i\vert u^{n+1}_i = \sum_i\vert I_i\vert u^{\mathrm{pr}}_i$,
because each weighted term appears $N^{\mathrm{ov}}_j$ times and the
linear part integrates to zero about the weighted centroid (§4.4), and
exact preservation of linear functions (§4.3), which flux redistribution
lacks. The authors note that this is not an order-of-accuracy proof.
Naive overlapping merging, which averages the merged values, is not
conservative (§2, eq. 6). The comparison with the flux-based cure is on the
[flux redistribution](/methods/flux-redistribution.md) page.

**What is not proved.** Stability in 2D and 3D (the half-cell threshold
is a 1D result; "We have not encountered any issues"). Positivity is
asserted qualitatively. SRD is **not monotone and not TVD**: in the 1D
analysis the neighbour coefficients turn negative for small cells, as
they do for flux redistribution (§2, after eq. 13). The tests are offered
as evidence that this "is not a significant issue": a Mach 10
[double Mach reflection](/benchmarks/double-mach-reflection.md) on an
embedded wedge runs cleanly with volume fractions down to
$2.95\times10^{-7}$ (§5.3).

## Weighted state redistribution

Original SRD switches on at a sharp cutoff, so moving a wall by
$10^{-7}$ of a cell across $\kappa_i = 0.5$ changes the solution by
0.132 with 2×2 merging (0.0051 with vertical-only merging). [Giuliani et al. (2022)](/sources/giuliani-2022.md) (§3.1,
eqs. 8–13) keep the neighbourhoods and let a small cell keep a share of
its own provisional state:
$$\eta^{\mathrm{nb}}_i = \frac{\tfrac12 h^d - \vert I_i\vert}{\sum_{j\in\mathcal N_i\setminus\{i\}}\vert I_j\vert},\qquad \eta^{\mathrm{self}}_i = 1 - \frac{1}{N^{\mathrm{ov}}_i}\sum_{k\ne i,\ i\in\mathcal N_k}\eta^{\mathrm{nb}}_k,$$
with $\eta^{\mathrm{nb}}_i = 0$ for cells at or above half a cell. The same
perturbation then changes the solution by about $10^{-8}$ (Fig. 5). No
stability bound is given for the weighted version.
* **Conservation criterion** (§3.1). Write $\widehat{\mathcal V} = \mathsf W\,\vert I\vert$.
  Both the original and the weighted scheme have $\mathbf 1^{\mathsf T}\mathsf W = \mathbf 1^{\mathsf T}$,
  and any redistribution matrix with unit column sums gives a
  conservative scheme; the slopes do not change the total. Any such
  weights define an SRD, which leaves room for solution-dependent or
  monotonicity-preserving weights (not pursued).
* **Accuracy** (§3.2, observed). On the
  [supersonic vortex](/benchmarks/supersonic-vortex-annulus.md), second
  order in the volume and about 1.4 on the boundary for both variants;
  the weighted version cuts the error of centred merging by a factor of
  2–3 and of normal merging by 10–15 %, and depends much less on the
  neighbourhood size.
* **In production** (§§4–6). AMReX-Hydro, used by PeleC, IAMR and
  MFIX-Exa; SRD takes at most about 2 % of the run time. The 2022
  implementation assumes the coarse–fine boundary crosses no cut cell, so
  SRD runs one level at a time; re-redistribution (below) lifts the
  restriction.

## Re-redistribution under AMR

When cut cells sit at a coarse–fine boundary, each level's redistribution
moves conserved quantities into covered coarse cells and fine ghost
cells, outside the composite solution
([Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §§2.4, 3.4).
The fix is a register built from the sparse matrix form of weighted SRD,
which records the extensive contribution each provisional state makes to
each cell (eqs. 14–16). At synchronization it is combined with the
refluxing correction and spread, flux-redistribution style, over the
uncovered coarse neighbours, because adding it to a tiny cut cell is
unstable (§3.4.2); with a two-stage method of lines each stage counts
one half (eq. 19).
* Conservation holds by construction and is observed to round-off in 2D
  and 3D, with Godunov or method-of-lines time stepping and also for
  flux redistribution (Fig. 3). There is no proof and no convergence
  order.
* It still fails when an uncovered coarse cut cell at the interface has
  a volume fraction below about $10^{-4}$: the first step gives negative
  energy and pressure (§4.1).
* The synchronization terms are at most a few percent of the
  coarse–fine mass flux; the solutions with and without them differ by a
  few percent in max norm (§4.1).
* Adaptive refinement of the EB cut a piston-engine run's cost by 3–4×
  against refining the whole EB, with the same flow features (§4.4,
  Table 1).

# Citations

1. [Berger & Giuliani (2021)](/sources/berger-2021.md), §§2–5 (arXiv v1).
2. [Giuliani et al. (2022)](/sources/giuliani-2022.md), §§3–6 (arXiv v2; eqs. 1–13 checked on the page images).
3. [Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §§2–4 (arXiv v1).
