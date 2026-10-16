---
type: Software
title: "GMEC"
description: "Gyrokinetic-MHD energetic-particle code family (Zhejiang University): reduced MHD in global field-aligned coordinates with arbitrary-order finite differences in all three directions, Scott's or a simple shifted metric, metrics and their derivatives precomputed from the equilibrium, and discrete equations generated symbolically at compile time."
status: established
aliases: [GMEC_I, gyrokinetic-MHD energetic particle simulation code, Compile-time Symbolic Solver, CSS]
tags: [software, field-aligned-coordinates, shifted-metric, finite-difference, metric]
timestamp: 2026-10-16T00:00:00Z
---

# GMEC

GMEC (gyrokinetic-MHD energetic particle simulation code) is a code family
developed at Zhejiang University for energetic-particle-driven Alfvén
instabilities in tokamaks. GMEC_I is its reduced-MHD foundation
([Jiang et al. (2024)](/sources/jiang-2024.md)); the hybrid version adds
gyrokinetic particles ([Liu et al. (2024)](/sources/liu-2024.md)). This page
records only its coordinate, metric and discretization choices; its plasma
models are outside the bundle.

## Coordinates and metric

* Global [field-aligned coordinates](/definitions/field-aligned-coordinates.md)
  built on straight-field-line [flux coordinates](/definitions/magnetic-flux-coordinates.md):
  Boozer in GMEC_I (Jiang et al., §III A, p. 3), PEST in the hybrid version
  (Liu et al., p. 5). GMEC_I implements plain field-aligned coordinates,
  Scott's [shifted metric](/methods/shifted-metric.md) and the simple shifted
  metric (Jiang et al., §III D, p. 4); the hybrid version uses plain
  field-aligned coordinates with a vorticity diffusion instead (Liu et al.,
  p. 2).
* All equilibrium quantities, including $J$, $g^{ij}$, $g_{ij}$, the
  integrated shear and their derivatives up to the order the equations need,
  are computed outside the code "with high-precision method" from the output
  of an equilibrium code and stored in a grid file, replicated on every MPI
  rank (Jiang et al., §IV E, p. 5; App. A, Table I, p. 16). From VMEC the
  equilibrium is first transformed to Boozer coordinates, with differences
  "applied only to the VMEC's original data" so that the stored fields are
  smooth; DESC supplies high-accuracy derivatives directly (App. C–D,
  pp. 16–17). Liu et al. compute the field-aligned metric from the flux-system
  metric analytically (their eqs. (26)–(28), p. 5) and note that the
  equilibrium-file abstraction "can be applicable to any curvilinear
  coordinates, and even generalized to simulations of stellarators" (p. 5).
  No source discusses a discrete metric identity or free-stream test for this
  arrangement.

## Discretization

* Finite differences of arbitrary order and stencil in all three directions,
  five points per direction by default (fourth order), biased stencils near
  Dirichlet and Neumann boundaries, ghost points for periodic and
  interpolated-periodic (twist-shift) boundaries (Jiang et al., §IV B, p. 5,
  fig. 4; Liu et al., p. 3):
  $$\partial_i\phi\to\frac{1}{\Delta\xi^i}\sum_\ell\mathcal C_\ell\,\phi(\xi^i+\ell\Delta\xi^i),\qquad \partial_i\partial_j\phi\to\frac{1}{\Delta\xi^i\Delta\xi^j}\sum_{\ell,\ell'}\mathcal C_{\ell\ell'}\,\phi(\xi^i+\ell\Delta\xi^i,\xi^j+\ell'\Delta\xi^j)$$
  (Jiang et al., eqs. (50)–(51), p. 8; no sum on $i,j$).
* **Expanded, not conservative, form.** Divergence-form operators are
  expanded by the product rule before differencing: the perturbed current
  $\frac{1}{JB}\partial_i\!\left(JB^2g^{ij}\partial_j(A/B)\right)$ becomes
  first-derivative terms with the precomputed coefficient
  $\frac{1}{JB^2}\partial_i(JB^2g^{ij})$ plus second-derivative terms with
  $g^{ij}$ (eq. (52), p. 8; the printed equation differs from eq. (48) in
  sign and $B$ factors, see the [Source page](/sources/jiang-2024.md)). The
  Poisson operator expands to 18 terms and the current to 48 (eqs. (47)–(48),
  p. 6). See [Laplacian](/definitions/laplacian.md).
* **Compile-time Symbolic Solver (CSS).** A C++20 metaprogramming library
  that expands the vector equations into components, applies the stencils,
  assembles the implicit matrices, and selects scheme order, boundary
  conditions and shifted-metric type as template parameters at compile time
  (§V, pp. 6–8). "Merging of coefficients" precomputes the products of
  stencil coefficients and metric factors into one contiguous array, so each
  offset value needs one multiplication at run time; the evaluation of the
  current becomes 6 times faster than "the usual method", which needs about
  60 multiplications and several equilibrium arrays per point (§VII,
  pp. 8–10). The authors' claim that this is "the minimum number of
  multiplications" is stated without proof (p. 10).
* The vorticity–potential Poisson problem is solved in the $(\xi^1,\xi^3)$
  plane with the $\partial_2$ terms dropped (the flute-ordering
  approximation), which is why the domain is decomposed in $\xi^2$ only
  (Jiang et al., §IV E, p. 5; Liu et al., p. 5).

# Citations

* [Jiang et al. (2024)](/sources/jiang-2024.md), §§III–V, pp. 3–8; §VII, pp. 8–10; App. A, C, D, pp. 16–17.
* [Liu et al. (2024)](/sources/liu-2024.md), §II A–D, pp. 2–5.
