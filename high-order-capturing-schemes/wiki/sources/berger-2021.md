---
type: Source
title: "Berger & Giuliani (2021) — A state redistribution algorithm for finite volume schemes on cut cell meshes"
description: "Introduces state redistribution: after a provisional full-Δt update, small cut cells are merged into overlapping neighbourhoods whose overlap-weighted averages and limited linear reconstructions are averaged back, which is exactly conservative and linearity-preserving (proved) though not monotone; second order in the volume and about 1.4–1.5 on the boundary, robust down to volume fractions of 3e-7."
resource: "doi:10.1016/j.jcp.2020.109820"
source_kind: paper
authors: [Berger M., Giuliani A.]
year: 2021
venue: "J. Comput. Phys. 428:109820"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2021-JCP-Berger-101016jjcp2020109820.pdf"
tags: [embedded-boundary, boundary-treatment, conservation]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

Explicit finite-volume schemes on Cartesian cut-cell meshes need a step
proportional to the smallest cut cell. State redistribution (SRD) lets
the step follow the regular cells: every cell takes a provisional
update, then small cells are temporarily merged with neighbours into
overlapping neighbourhoods of at least half a cell, whose overlap-weighted
averages and limited linear reconstructions are averaged back. The
paper proves conservation and exactness for linear functions, and tests
two second-order base schemes on 2D Euler problems. Merged into
[state redistribution](/methods/state-redistribution.md) and
[cut-cell finite volume](/methods/cut-cell-finite-volume.md).

# Key claims

1. **Setting** (§§1, 3). Cut-cell finite volume with cell-centred
   unknowns; the wall flux uses the pressure extrapolated to the wall-face
   midpoint. Small-cell cures in the literature: flux redistribution
   (most common, first order at cut cells, not linearity-preserving), cell
   merging, h-box (second order, not extended to 3D), cell linking,
   implicit cut cells (§1).
2. **Naive overlapping merging is not conservative** (§2, eq. 6).
3. **Algorithm** (§4, eqs. 35–42): normal merging, falling back to 3×3
   and 5×5 tiles; weights $\vert I_j\vert/N^{\mathrm{ov}}_j$; least-squares
   gradients at weighted centroids, Barth–Jespersen limited; average of
   the overlapping reconstructions.
4. **Proved:** conservation (§4.4, eqs. 52–55) and exactness for linear
   data (§4.3, eqs. 43–51), explicitly not an order proof.
5. **Not proved:** stability (the half-cell threshold is a 1D result);
   positivity (qualitative). Not monotone and not TVD (§2, after eq. 13).
6. **Base schemes** (§3). A method of lines with Heun's method and local
   Lax–Friedrichs, SRD after each stage; and Colella's unsplit MUSCL, SRD
   once. The Barth–Jespersen limiter is evaluated at neighbour centroids
   to keep linearity preservation (§3.3).

**Tests** (§5, 2D Euler, no AMR, no moving bodies):
the [supersonic vortex](/benchmarks/supersonic-vortex-annulus.md)
(volume error order about 2, boundary 1.38–1.5, the same as with local
time stepping); a Mach 2 [shock reflection from a cylinder](/benchmarks/shock-reflection-from-cylinder.md)
(smallest volume fraction $1.17\times10^{-4}$); and a Mach 10
[double Mach reflection](/benchmarks/double-mach-reflection.md) on an
embedded wedge (smallest $2.95\times10^{-7}$).

**Later evidence (batch 18).** The "h-box (second order …)" summary is qualified by the primary source, [Berger et al. (2003)](/sources/berger-2003.md). It proves second order for 1D advection with one small cell (Prop. 2) and observes it on irregular 1D grids and a 2D nonuniform tensor grid. It has no cut cells and states that no Cartesian embedded-boundary method was yet second order at boundary cells (§8). See [cut-cell finite volume](/methods/cut-cell-finite-volume.md).

# Notation map

| Berger & Giuliani (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $V_{i,j}$, $\alpha$ (volume fraction) | $\vert I_i\vert$, $\kappa_i$ | $\alpha$ is the Lax–Friedrichs speed; $V_i$ the Voronoi set |
| $\widehat U$ | $u^{\mathrm{pr}}$ | |
| $M_{i,j}$, $N_{i,j}$, $W_{i,j}$ | $\mathcal N_i$, $N^{\mathrm{ov}}_i$, words | |
| $\widehat V_{i,j}$, $(\hat x, \hat y)$ | $\widehat{\mathcal V}_i$, $\hat{\mathbf x}_i$ | |
| $\widehat Q_{i,j}$, $\hat q_{i,j}$ | $\bar u^{\mathcal N}_i$, $q^{\mathcal N}_i$ | |
| $\hat\sigma_x$, $\hat\sigma_y$ | $\nabla q^{\mathcal N}_i$ | |
| $h$ (1D cell size) | $h$ | |

# Pages created or updated

* Created [State redistribution](/methods/state-redistribution.md), [Cut-cell finite volume](/methods/cut-cell-finite-volume.md), [Supersonic vortex in a quarter annulus](/benchmarks/supersonic-vortex-annulus.md), [Shock reflection from a cylinder](/benchmarks/shock-reflection-from-cylinder.md).
* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md) (embedded wedge), [Positivity preservation](/properties/positivity-preserving.md).
* Updated [Notation registry](/notation.md): $\kappa_i$, $u^{\mathrm{pr}}$, $\mathcal N_i$, $N^{\mathrm{ov}}_i$, $\widehat{\mathcal V}_i$, $\bar u^{\mathcal N}_i$, $q^{\mathcal N}_i$.
* Also cited on [Flux redistribution for small cut cells](/methods/flux-redistribution.md) (created 2026-10-13).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2021-JCP-Berger-101016jjcp2020109820.pdf`.
   * **Version.** arXiv:2005.05734v1 (12 May 2020), 34 pages, not the
     typeset article. The collection labelled it "marsha-2020".
   * **Identity.** doi:10.1016/j.jcp.2020.109820, found and checked on
     Crossref by title: J. Comput. Phys. 428:109820, March 2021.
   * **How it was read.** Text extraction, all sections.
   * **Recorded as printed.** Eq. 31 prints max where min is meant; eq. 13
     uses an undefined $\lambda$; the tables print error ratios, not orders.
   * **Reference list:** 24 entries. Muralidharan is printed
     "Muralidhara"; the entry is merged into `muralidharan-2016`.
