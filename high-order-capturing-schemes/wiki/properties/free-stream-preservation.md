---
type: Property
title: "Free-stream preservation on curvilinear grids"
description: "A scheme on a mapped (curvilinear) grid preserves free streams if a uniform flow, an exact steady solution, stays uniform to round-off; for high-order finite differences this requires the discrete metric identities, obtained by writing the metrics in conservative form and differencing them with the flux operator itself."
status: established
aliases: [freestream preservation, free-stream preserving, geometric conservation law, metric identities]
tags: [mapped-grid, finite-difference, finite-volume, amr]
timestamp: 2026-10-08T00:00:00Z
---

# Free-stream preservation on curvilinear grids

**The property.** On a grid mapped smoothly from computational
coordinates $\mathbf X = (X^1, X^2, X^3)$, the equations are solved in
strong conservation form for $\mathcal J u$, with
$\mathcal J = \det(\partial\mathbf x/\partial\mathbf X)$ and contravariant
fluxes $\tilde f^a = \sum_b \tilde m^a_b f_b$, where
$\tilde m^a_b = \mathcal J\,\partial X^a/\partial x^b$ are the metric terms.
For a uniform state the semi-discrete residual reduces to the discrete
value of $\sum_a \partial_{X^a}\tilde m^a_b$ times the constant flux. That
sum vanishes exactly in the continuum (the metric identity), but not in
general after discretization. A scheme *preserves free streams* when the
discrete sum is zero, so that uniform flow stays uniform to round-off
([Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), §3, eqs. 12–19).

**How high-order finite differences get it.**
* Compute the metrics in the conservative (Thomas–Lombard) form, for
  example $\tilde m^1_x = \partial_{X^3}\left(z\,\partial_{X^2}y\right) - \partial_{X^2}\left(z\,\partial_{X^3}y\right)$,
  and difference them with the same operator as the fluxes. Face values
  of the grid coordinates come from one fixed, unlimited six-point
  interpolation, which need not be the limited interpolation used for
  the solution. The two sums then cancel to round-off
  ([Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), §3, eqs. 15–17).
* A future limiter on the flux correction must leave the formulas
  unchanged for a free stream (§3).
* The two finite-difference forms differ here. The classical
  flux-splitting form does not preserve free streams on curvilinear
  meshes. The alternative form, which interpolates the solution and calls
  a Riemann solver at the face, does (Jiang, Shu and Zhang, as cited by
  [Balsara et al. (2025)](/sources/balsara-2025.md), §I;
  [conservative finite difference](/methods/conservative-finite-difference.md);
  [alternative finite-difference WENO](/methods/alternative-finite-difference-weno.md)).

**Evidence.**
* Fifth-order FD on a two-level refined spherical shell: the maximum
  error of a uniform flow after 100 steps is $2.5\times10^{-14}$. On a
  refined polar grid, a density peak advects with no error in the
  uniform-flow region ([Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), §§5.3.2, 5.6).
* Fourth-order finite volume on a warped mapped grid with two levels of
  moving refinement (the refined region rotates once about the centre,
  1000 steps): the largest change in $L^1$ is $2.1\times10^{-14}$
  ([Owen, Guzik & Gao (2018)](/sources/owen-2018.md), §4.6, Table 4;
  [fourth-order finite volume](/methods/fourth-order-finite-volume.md);
  [high-order AMR](/methods/high-order-amr.md)).

# Citations

1. [Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), §§3, 5.3.2, 5.6 (accepted manuscript).
2. [Owen, Guzik & Gao (2018)](/sources/owen-2018.md), §4.6 (accepted manuscript).
3. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §I.
