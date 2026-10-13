---
type: Method
title: "Multi-resolution WENO"
description: "Zhu–Shu WENO on a hierarchy of nested central stencils of increasing order (7, 5, 3 and 1 cells in 1D), recombined so that any positive linear weights reproduce the largest stencil's polynomial: advocated by Shu for unstructured meshes, derivatives, integrals and compact DG limiters, and used in the corpus as AFD-WENO interpolation and as a one-sided WENO extrapolation for inverse Lax–Wendroff boundaries."
status: established
aliases: [multiresolution WENO, MR-WENO, Zhu–Shu WENO, multi-resolution WENO limiter, multi-resolution WENO extrapolation]
tags: [weno, adaptive-order, nonlinear-weights, unstructured, interpolation]
timestamp: 2026-10-13T00:00:00Z
---

# Multi-resolution WENO

**Idea.** Multi-resolution WENO (Zhu and Shu, 2018–2020, not ingested)
is the [unequal-stencil device](/methods/weno-ao.md) taken to a full
hierarchy. All stencils are central and nested; in 1D, if the largest
has seven cells, the smaller ones have five, three and one. Because the
small stencils enter only through a weight-adjusted subtraction, the
linear weights are arbitrary positive numbers summing to one, and the
result is a polynomial on the whole target cell, not values at chosen
points ([Shu (2020)](/sources/shu-2020.md), §3.2.3). The hierarchy ends
in first order: the lowest level may go "all the way down to first order
accuracy" when every stencil carries a non-smooth solution, where WENO-ZQ
stops at two linear polynomials and WENO-AO at a third-order central
WENO ([Balsara et al. (2025)](/sources/balsara-2025.md), §III). Balsara
et al. read WENO-AO, WENO-ZQ and multi-resolution WENO as one
multiresolution strategy: a non-linear hybridization of a large,
centred, very accurate stencil with a lower-order but stable scheme
(§III).

## The nested recombination

The corpus prints the recombination only in one-sided extrapolation
form ([Lu et al. (2021)](/sources/lu-2021.md), §2.1, eqs. 2.11–2.15,
checked against the page image), which its authors take from Zhu and
Shu. Let $S_k$, $k = 0, \dots, 4$, be the nested stencils, each one point
wider than the last, $p_k$ the interpolant of degree $k$ on $S_k$, and
$d_k > 0$ with $\sum_k d_k = 1$. Hierarchical polynomials are defined
recursively: the first is $p_0$, and the $k$-th equals
$$\frac{1}{d_k}\left(\sum_{m=0}^{k} d_m\right) p_k$$
minus $1/d_k$ times the $d_m$-weighted sum of the earlier hierarchical
polynomials, $m < k$. By induction the $d$-weighted sum of the first
$k + 1$ hierarchical polynomials equals $\left(\sum_{m \le k} d_m\right) p_k$,
so with all of them the linear combination is exactly $p_4$, whatever the
positive $d_k$. Replacing $d_k$ by nonlinear weights $\omega_k$ gives the
WENO polynomial, and every derivative is read off it.
* Lu et al. take $d_k = \tfrac1{15}, \tfrac2{15}, \tfrac15, \tfrac4{15}, \tfrac13$
  and WENO-Z-type weights,
  $\tilde\omega_k = d_k\left(1 + \left(\tau/(\varepsilon + \beta_k)\right)^4\right)$,
  $\varepsilon = 10^{-4}$, with $\beta_0 = 0.1\,\beta_1$ because the
  constant has no indicator; the global indicator $\tau$ is given on
  [weighted extrapolation](/methods/weighted-extrapolation.md), with its
  caveats.
* Constant linear weights are the point of the change: the
  extrapolation they replace took weights as powers of $h$, which Lu et
  al. say breaks self-similarity (Remark 2.1).

Zhu and Shu's own nonlinear weights and indicators, and their order
proofs, are in papers the corpus does not hold. On weights, Shu argues
that small stencils of low order force the nonlinear weights to stay
closer to the linear ones than in classical WENO, so mapped or WENO-Z
weights "would be preferable" ([Shu (2020)](/sources/shu-2020.md),
§3.2.3; [mapped WENO](/methods/mapped-weno.md), [WENO-Z](/methods/weno-z.md)).
This is an accuracy argument for the unequal-stencil class, not a test.

## Where Shu advocates it

([Shu (2020)](/sources/shu-2020.md), §§3.3–3.4, 4.3.)
* **Unstructured meshes.** Classical WENO on triangles and tetrahedra
  needs point-dependent linear weights that "could easily become
  negative" ([negative linear weights](/methods/negative-linear-weights.md)).
  Arbitrary positive weights avoid this, and Shu "would advocate in
  particular" the multi-resolution schemes, "a simple and effective"
  procedure on 2D and 3D unstructured meshes (§3.3).
* **Derivatives and integrals.** Because the result is a polynomial,
  the $m$-th derivative is that of the WENO polynomial and the cell
  integral is its integral. The smoothness-indicator sum must then start
  one order above the derivative sought (§§3.4.1–3.4.2).
* **DG limiters.** Compact WENO limiters of Zhu, Qiu and Shu (2020),
  built on multi-resolution WENO and using only immediate neighbours,
  "appear to be quite robust for RKDG methods of various orders" (§4.3;
  [WENO limiters for DG](/methods/weno-limited-dg.md)). This is the
  reviewer's assessment; the corpus holds no test of it.

## Uses in the corpus

* **AFD-WENO interpolation.** Every interface-derivative formula of
  [alternative finite-difference WENO](/methods/alternative-finite-difference-weno.md)
  carries over to multi-resolution interpolation, with a piecewise-linear
  smallest stencil on the two points beside the interface and fourth,
  sixth and eighth order from the larger ones; the hybridization "is the
  same as in Zhu and Shu" ([Balsara et al. (2025)](/sources/balsara-2025.md),
  §IV.e). It costs slightly more than WENO-AO interpolation because more
  stencils are built, at the same stencil width (§V).
* **Accuracy.** On 2D vortices for Euler, relativistic hydrodynamics and
  the ten-moment equations at orders 3, 5, 7, 9, with a piecewise-linear
  MC-limited lowest level, the authors find that the two forms "produce
  comparable accuracies" on the Euler vortex and that both reach design
  accuracy on the other two (§VI, Tables I–III;
  [isentropic vortex](/benchmarks/isentropic-vortex.md)). In Table I the
  finest-grid $L^1$ orders are 2.57, 5.33, 6.93 and 8.72 for
  multi-resolution against 3.00, 4.71, 6.93 and 8.73 for WENO-AO, and the
  third-order multi-resolution $L^\infty$ orders are 2.46, 2.58 and 2.29;
  the authors do not comment on the third-order shortfall.
* **Boundary extrapolation.** The one-sided nested form above supplies
  the ghost-point derivatives of [inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md)
  boundaries; it tends to constant extrapolation when a discontinuity
  sits next to the boundary, and Lagrange extrapolation replaces it where
  the solution is smooth ([Lu et al. (2021)](/sources/lu-2021.md),
  §2.1, Remark 2.3; [weighted extrapolation](/methods/weighted-extrapolation.md)).

**Not to be confused with** Harten's multiresolution framework, a
wavelet-type decomposition that has been combined with WENO into
adaptive multiresolution WENO schemes
([Shu (2009)](/sources/shu-2009.md), §5.4), nor with adaptive
multiresolution grid refinement as run by
[Brahmi et al. (2020)](/sources/brahmi-2020.md), §2.1. Both adapt the
grid or the representation, not the WENO stencils.

# Citations

1. [Shu (2020)](/sources/shu-2020.md), §§3.2.3, 3.3, 3.4.1–3.4.2, 4.3.
2. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §§III, IV.e, V, VI, Tables I–III.
3. [Lu, Shu, Tan & Zhang (2021)](/sources/lu-2021.md), §2.1, eqs. 2.11–2.15, Remarks 2.1, 2.3.
4. [Shu (2009)](/sources/shu-2009.md), §5.4.
5. [Brahmi et al. (2020)](/sources/brahmi-2020.md), §2.1.
