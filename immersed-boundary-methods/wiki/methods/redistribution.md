---
type: Method
title: "Flux redistribution for cut cells"
description: "Stabilization of explicit cut-cell finite-volume schemes that takes a stable non-conservative update in each small cut cell and redistributes the resulting conservation deficit to neighbouring cells, so that the scheme stays conservative with a time step set by the full cells; Pember et al.'s mass-weighted algebraic version and its adaptive-mesh extension."
status: established
aliases: [redistribution, algebraic redistribution, mass-weighted redistribution, flux redistribution]
tags: [cut-cell, embedded-boundary, conservation, stability, small-cell]
timestamp: 2026-11-08T17:31:00Z
---

# Flux redistribution for cut cells

Redistribution answers the [small-cell problem](/definitions/small-cell-problem.md)
of the [cut-cell method](/methods/cut-cell-method.md) without changing the
grid. In each cut cell $\mathbf i$ the conservative update would divide by the
small volume $\kappa_{\mathbf i}h^d$; instead a stable update weighted by
$\kappa_{\mathbf i}$ is taken, and the amount of conserved quantity it fails to
deposit, $(1-\kappa_{\mathbf i})\,\delta\mathbf M_{\mathbf i}$ ("mass" meaning integrated
mass, momentum and energy), is added to nearby cells with weights
$w_{\mathbf i\mathbf j}$ that sum to one. Total conservation holds exactly, and the
scheme is equivalent to a modification of the edge fluxes of the predictor
([Pember et al. 1995](/sources/pember-1995.md), §2.6).

## Pember et al. (1995)

- **Neighbourhood.** For a stationary reflecting wall the whole deficit goes to
  the cut and fluid cells among the 26 immediate neighbours of the cut cell; a
  moving front would need a characteristic decomposition (Chern and Colella
  1987, Bell, Colella and Trangenstein).
- **Weights.** $w_{\mathbf i\mathbf j}\propto\rho_{\mathbf j}\kappa_{\mathbf j}$ (mass-weighted),
  using the preliminary density, rather than the volume-weighted
  $w_{\mathbf i\mathbf j}\propto\kappa_{\mathbf j}$ of the shock-tracking algorithm of Chern
  and Colella; mass weighting was "superior … in the presence of strong
  shocks" in their experiments, and the preliminary-update density was the
  most robust choice. For a general hyperbolic system mass weighting may not
  be meaningful.
- **Stability.** Not proved (nor by Chern and Colella). The heuristic argument
  is that the whole algorithm divides only by full-cell widths or volumes, and
  the mass moved into a cut cell is roughly proportional to its volume.
- **Geometry limits.** A cut cell redistributes to all neighbours, even ones in
  a separate fluid region, so distinct regions must be separated by at least
  one full body cell, and every cut cell needs enough fluid neighbours.
- **Adaptive refinement.** Redistribution across a coarse–fine boundary is
  corrected by a composite refluxing/redistribution step ("re-redistribution")
  so the AMR hierarchy stays conservative (§3).

# Citations

- [Pember et al. (1995)](/sources/pember-1995.md) — §1, §2.6, §3.
