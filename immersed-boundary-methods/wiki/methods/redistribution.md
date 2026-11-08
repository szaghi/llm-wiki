---
type: Method
title: "Flux redistribution for cut cells"
description: "Stabilization of explicit cut-cell finite-volume schemes that takes a stable non-conservative update in each small cut cell and redistributes the resulting conservation deficit to neighbouring cells, so that the scheme stays conservative with a time step set by the full cells; Pember et al.'s mass-weighted algebraic version and its adaptive-mesh extension."
status: established
aliases: [redistribution, algebraic redistribution, mass-weighted redistribution, flux redistribution]
tags: [cut-cell, embedded-boundary, conservation, stability, small-cell]
timestamp: 2026-11-08T18:10:00Z
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

## Hybrid update and redistribution (Colella et al. 2006)

[Colella et al. (2006)](/sources/colella-2006.md) write the scheme
explicitly. Besides the conservative divergence $(\nabla\cdot\boldsymbol{\mathcal F})^{C}$
(which divides by $\kappa_{\mathbf i}$), a stable non-conservative divergence
$(\nabla\cdot\boldsymbol{\mathcal F})^{NC}$ is formed from the fluxes on the full Cartesian
cell, with states extrapolated to covered faces. The cut cell is updated with
the hybrid

$$(\nabla\cdot\boldsymbol{\mathcal F})^{H}_{\mathbf i}=\kappa_{\mathbf i}(\nabla\cdot\boldsymbol{\mathcal F})^{C}_{\mathbf i}+(1-\kappa_{\mathbf i})(\nabla\cdot\boldsymbol{\mathcal F})^{NC}_{\mathbf i},$$

which cancels the small denominator, and the conservation defect

$$\delta\mathbf M_{\mathbf i}=-\Delta t\,\kappa_{\mathbf i}(1-\kappa_{\mathbf i})\big[(\nabla\cdot\boldsymbol{\mathcal F})^{C}_{\mathbf i}-(\nabla\cdot\boldsymbol{\mathcal F})^{NC}_{\mathbf i}\big]$$

is distributed to the neighbours $\mathbf j\in N(\mathbf i)$ (indices within one of
$\mathbf i$) as $\mathbf q_{\mathbf j}\leftarrow\mathbf q_{\mathbf j}+w_{\mathbf i\mathbf j}\,\delta\mathbf M_{\mathbf i}$ with
$\sum_{\mathbf j}w_{\mathbf i\mathbf j}\kappa_{\mathbf j}=1$ and $w_{\mathbf i\mathbf j}$ bounded independently of
$\kappa_{\mathbf j}^{-1}$. Volume weighting takes $w_{\mathbf i\mathbf j}=\big(\sum_{N(\mathbf i)}\kappa_{\mathbf j}\big)^{-1}$;
mass weighting with a non-conservative density estimate, after Pember et al.,
is more robust for strong shocks. The scheme is locally conservative up to
redistribution across the boundary of a region, and the non-conservative
divergence must be designed so that a small cell comes into equilibrium with
its larger neighbours, because it carries almost the whole update when
$\kappa\ll1$.

The sign convention of $\delta\mathbf M$ and the precise update formula are written
here in registry form from the paper's description; the version read prints
the formulas in a garbled text layer ([Colella et al. 2006](/sources/colella-2006.md),
Version read).

## Assessment and successor

[Berger & Giuliani (2021)](/sources/berger-2021.md), §1, credit flux
redistribution with being simple and already used in 3-D, but note that it is
only first-order accurate at the cut cells and not linearity preserving; their
[state redistribution](/methods/state-redistribution.md) redistributes states
instead. [Natarajan et al. (2022)](/sources/natarajan-2022.md), §2, use the
hybrid divergence of Colella et al. with volume-weighted redistribution
($\sum_{\mathbf j}\kappa_{\mathbf j}w_{\mathbf j}=1$) for moving embedded boundaries.

# Citations

- [Pember et al. (1995)](/sources/pember-1995.md) — §1, §2.6, §3.
- [Colella et al. (2006)](/sources/colella-2006.md) — §2 (stable evolution, redistribution).
- [Berger & Giuliani (2021)](/sources/berger-2021.md) — §1.
- [Natarajan et al. (2022)](/sources/natarajan-2022.md) — §2.
