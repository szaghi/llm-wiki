---
type: Software
title: "ForestClaw"
description: "ForestClaw is a quadtree patch-based adaptive mesh refinement code on p4est with fixed-size Cartesian patches and 2:1 balance; the bundle's sources build Active Flux solvers in it, with conservative coarse–fine transfer of averages and point values, sub-cycling without time interpolation and Berger–Colella refluxing."
status: established
aliases: [ForestClaw, forest-of-quadtrees AMR, p4est patch AMR]
tags: [software, finite-volume, amr]
timestamp: 2026-10-23T11:06:00Z
---

# ForestClaw

ForestClaw is a code for
[block-structured adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
in which the leaves of a quadtree, or of a forest of quadtrees over several
blocks, each carry a Cartesian patch, the tree being managed by the p4est
library. As [Calhoun, Chudzik & Helzel (2023)](/sources/calhoun-2023.md)
(§3, arXiv v2) describe it, refinement bisects a quadrant of level $\ell$
into four quadrants of level $\ell+1$, every patch has the same number of
cells on every level ($8\times8$, $16\times16$ or $32\times32$ typically;
$16\times16$ in all their tests), so the refinement ratio is 2, and
adjacent quadrants differ by at most one level, which the authors call
"well-balanced" in the p4est sense (not the sense of
[well-balancing](/properties/well-balancing.md)). The mesh is refined and
coarsened at every time step; four siblings are merged only when all of
them satisfy the coarsening criterion. Both sources of the bundle that use
it are by the same group and implement
[Active Flux](/methods/active-flux.md) methods in it;
[Chudzik et al. (2024)](/sources/chudzik-2024.md) state that the code is
publicly available on GitHub (Data Availability).

## Active Flux on the patch hierarchy

Calhoun et al. present this as the first implementation of Active Flux on
adaptively refined Cartesian grids (Abstract). Active Flux has, per cell
and per variable, a cell average and point values at the corners and edge
midpoints shared with the neighbours, and a biquadratic reconstruction
that interpolates the eight boundary values and matches the average. The
code needs three transfer operations (§3.1, Figs. 3–4):

- **fine to coarse** (coarsening, and coarse ghost cells next to a finer
  patch): the coarse average is the mean of the four fine averages, the
  coarse point values are copied from fine-cell vertices, and fine values
  that are not at coarse locations are discarded;
- **coarse to fine** (refinement, and fine ghost cells next to a coarser
  patch): the coarse reconstruction is evaluated at the fine point-value
  locations and the fine averages are computed by the two-dimensional
  Simpson rule, which needs four extra evaluations at the fine cell
  centres; Simpson's rule is exact for the biquadratic reconstruction, so
  the four fine averages sum exactly to the coarse one and the transfer is
  conservative;
- **same level**: copies.

**Sub-cycling** (§3.2, Figs. 5–6). Level $\ell+1$ advances with
$\Delta t_{\ell+1}=\Delta t_\ell/2$. Unlike Berger–Oliger–Colella, coarse
ghost data are never interpolated in time: two ghost layers are
reconstructed around each patch, the first is advanced together with the
interior and used at the intermediate times, and at synchronized times the
ghost data are replaced by averaged or interpolated data from the
neighbours. Conservation at coarse–fine faces uses the Berger–Colella fix,
coarse and fine cells being updated with the fine fluxes. Physical boundary
conditions are applied at every time level.

**Refinement criteria** (§4). Solution variation per patch,
$q_{\max}-q_{\min}>0.001$ for advection and
$\lvert p_{\max}-p_{\min}\rvert\ge0.001$ for acoustics, a centred difference
quotient of at least 15 for two-dimensional Burgers (the same cells are then
limited), and a band forced along a diagonal in the convergence tests.

## Results obtained with it

Calhoun et al. measure third order in $L^1$ on adaptive grids for
smoothed-disc advection, [solid-body rotation](/benchmarks/solid-body-rotation.md),
a time-dependent swirl and acoustics (Tables 1–4): refinement that follows
the solution matches the finest uniform grid (disc advection,
$1.07\times10^{-6}$ against $1.07\times10^{-6}$), while refinement along a
fixed diagonal band matches the coarser one. Their constant-state
preserving variant for the swirl keeps constants exactly with global time
stepping (Corollary 4.3) but not with sub-cycling, where a constant field
shows an error of $10^{-13}$ against about $10^{-16}$
([free-stream preservation](/properties/free-stream-preservation.md));
sub-cycling does not change the accuracy noticeably on smooth swirl data
(Table 3). With the stationarity-preserving acoustic operator of Barsukow
et al. the solver is stable on a regular grid and unstable with adaptive
refinement (§4.6, Conclusions).

Chudzik et al. (2024) implement in ForestClaw their Active Flux methods
whose point values are updated by approximate evolution operators from the
method of bicharacteristics, "using patches of Cartesian grids that also
allow adaptive mesh refinement and sub-cycling" as in Calhoun et al.
(Conclusions). Their single adaptive run is the smooth two-pulse problem of
the linearized Euler equations with the EG2 operator at CFL 0.267 (§6.1,
Fig. 16); its convergence study is done on uniform grids (Table 7), so the
paper adds no measurement of the adaptive mode.

## Qualifications

- Neither source describes the parallel implementation or reports run
  times of the code; ForestClaw enters only as the host of the
  Active Flux solvers.
- The refinement ratio, patch size and level structure are those stated by
  Calhoun et al.; Chudzik et al. give no AMR parameters for their run.
- Calhoun et al.'s reference list prints the Berger–Colella paper as
  "82:484–512, 1984", the year and pages of its preceding Berger–Oliger
  entry; the other citing sources of the bundle (e.g. Qin et al. 2023,
  Zaghi et al. 2023) give J. Comput. Phys. 82:64–84 (1989). This does not
  touch the method.

# Citations

- [Calhoun, Chudzik & Helzel (2023)](/sources/calhoun-2023.md) — arXiv v2: Abstract; §3, §3.1–3.2, Figs. 3–6; §4.1–4.6, Corollary 4.3, Tables 1–4; Conclusions.
- [Chudzik et al. (2024)](/sources/chudzik-2024.md) — §6.1, Fig. 16, Table 7; Conclusions; Data Availability.
