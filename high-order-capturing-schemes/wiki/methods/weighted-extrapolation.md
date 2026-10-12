---
type: Method
title: "Weighted (WENO-type) extrapolation for ghost values"
description: "Ghost-cell values for finite-difference WENO on Cartesian grids cut by complex boundaries, extrapolated along boundary normals with weights that raise the extrapolation degree only where the data are smooth: Baeza et al.'s dimensionless nested weights with a least-squares blend for stability, and the multi-resolution WENO extrapolation with constant linear weights used with inverse Lax–Wendroff."
status: established
aliases: [weighted extrapolation, WENO extrapolation, WLS-GAW, weighted least squares extrapolation, boundary extrapolation]
tags: [boundary-treatment, finite-difference, weno, cut-cell]
timestamp: 2026-10-12T00:00:00Z
---

# Weighted (WENO-type) extrapolation for ghost values

**Setting** ([Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §§2–3).
Shu–Osher [conservative finite differences](/methods/conservative-finite-difference.md)
with WENO5, Donat–Marquina flux splitting and SSP-RK3 run on the
intersection of a Cartesian lattice with the domain. Order $2r - 1$
needs $r$ extra points beyond every mesh line, called ghost cells. Each
ghost point is assigned from its nearest boundary point by
extrapolation along the normal. This takes three steps:
1. 1D interpolation, horizontal or vertical according to the normal's
   slope, gives data at points on the normal.
2. At Dirichlet boundaries, these are re-interpolated to an equally
   spaced stencil that starts at the boundary point. Outflow boundaries
   use the normal points directly.
3. A 1D extrapolation to $P$ follows.

Node spacing no smaller than $h$ was found stable for high-order
extrapolation, and the selection is done once for fixed boundaries.

**Why not plain Lagrange.** Lagrange extrapolation oscillates near
discontinuities. Classical ENO/WENO is unsuitable for extrapolation
(Baeza et al.'s earlier work). Straight Lagrange extrapolation can make
the scheme mildly unstable on complex 2D domains (also Tan and Shu).
The authors' earlier Boolean, thresholded node selection worked but
depended strongly on its parameter
([Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §§4, 5.2.4, 6).

## Weighted extrapolation

Order the nodes by distance from the target $x^{\mathrm g}$. Let $p_k$
be the degree-$k$ interpolant on the $k + 1$ closest nodes, and $j_0$
the closest node. Then
$$\breve u_0 = u_{j_0},\qquad \breve u_k = \left(1 - \omega^{\mathrm{ext}}_k\right)\breve u_{k-1} + \omega^{\mathrm{ext}}_k\,p_k(x^{\mathrm g}),$$
up to the full degree of the stencil,
with $\omega^{\mathrm{ext}}_k \approx 1$ where the nested stencil is
smooth and $\approx 0$ where it crosses a discontinuity. The weights use
Jiang–Shu-type indicators integrated over the whole stencil
([smoothness indicator](/definitions/smoothness-indicator.md)).

* **Simple weights** compare an indicator with the smallest
  sub-stencil indicator. They can take the smoothest data from the
  *wrong* side of a discontinuity: on $x^2$ joined to 1, the weights
  vanish and the result is the nearest value 0.25 instead of the
  correct 0.49. On $x^2 \mid 1 + x^3$ they converge to a non-unit
  limit, and the order falls to about one (Table 1).
* **Improved weights** add a second ratio that separates "smooth"
  from "crosses a discontinuity" from "smooth but on the wrong side".
  They recover third order there (Table 2). Adding to the indicators a
  floor of the size of smooth-data indicators, built from the data's
  undivided differences, keeps the order when a
  derivative vanishes, as for $\sin x \mid 1$ (Tables 3–4).
* **One weight (UW)** between the constant and the full-degree
  extrapolation, a convex combination of $u_{j_0}$ and the highest-degree
  $p_k(x^{\mathrm g})$ with weight $\omega^{\mathrm{ext}}$. It is
  cheaper and more robust once discontinuities are smeared. Its tuned
  form maps $\omega^{\mathrm{ext}} \mapsto (e^{\lambda_{\mathrm{UW}}\omega^{\mathrm{ext}}} - 1)/(e^{\lambda_{\mathrm{UW}}} - 1)$
  to push intermediate values toward 0 or 1.
* **Global average weight (GAW)** builds $\omega^{\mathrm{ext}}$ from the ratio of
  the harmonic to the arithmetic mean of the sub-stencil indicators,
  raised to a power. Every weight is dimensionless and
  scale-independent, unlike the weights of the
  [ILW](/methods/inverse-lax-wendroff.md) papers.
* **Weighted least squares (WLS-X).** Replace the full-degree Lagrange
  value by a least-squares fit, blended with the nearest value through
  a UW or GAW weight. This removes the mild instability on complex
  domains. The tests use a degree-4 fit on 9 nodes and three-point
  sub-stencils, with exponents chosen to match the boundary accuracy
  to the scheme and to mimic the WENO-JS power.

**Evidence** ([Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §5).
* All variants reach fifth order on smooth 1D advection and Burgers
  problems. IW behaves like Lagrange, and WLS is slightly less accurate
  because its stencil is wider.
* A Burgers shock that later reaches the inflow boundary is captured
  cleanly. The [interacting blast waves](/benchmarks/interacting-blast-waves.md)
  with reflecting walls agree with a reference solution at
  $h = 1/16000$.
* On a complex 2D domain, Lagrange extrapolation is mildly unstable,
  while WLS-UW and WLS-GAW stay stable and fifth order.
* High-order extrapolation resolves a Mach 10 shock reflecting off a
  triangle (a [double Mach reflection](/benchmarks/double-mach-reflection.md)
  variant) better than first-order extrapolation. WLS-GAW is best, and
  also handles shock interaction with multiple cylinders and steady
  supersonic flow past a triangle.

## Multi-resolution WENO extrapolation

([Lu et al. (2021)](/sources/lu-2021.md), §2.1, eqs. 2.9–2.15, read from
the page images.) The extrapolation that Tan and Shu pair with
[inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md) takes its linear
weights as powers of $h$ ($h^4, h^3, h^2, h$ and the remainder) and its
power $q$ per problem. Lu et al. call this a loss of self-similarity and
replace it with a multi-resolution construction after Zhu and Shu.
* Nested stencils $\{x_{N-k}, \dots, x_N\}$, $k = 0, \dots, 4$, carry
  interpolants $p_k$. These are recombined into hierarchical polynomials
  whose combination with constant linear weights
  $d_k = \tfrac1{15}, \tfrac2{15}, \tfrac15, \tfrac4{15}, \tfrac13$
  reproduces the degree-4 interpolant.
* The weights are WENO-Z-type,
  $\tilde\omega_k = d_k\left(1 + \left(\tau/(\varepsilon + \beta_k)\right)^4\right)$,
  with $\varepsilon = 10^{-4}$. The global indicator $\tau$ combines
  differences of the $\beta_k$ with $L^2$ distances between the
  candidates, and $\beta_0 = 0.1\,\beta_1$ (the constant has no
  indicator). A small factor on $\beta_0$ drives the result to constant
  extrapolation when a discontinuity lies next to the boundary.
* All boundary derivatives are taken from the weighted polynomial. In 2D,
  a least-squares degree-4 fit on a disc of radius about $5h$ gives the
  values on the normal, and the same nonlinear weights serve the
  tangential derivatives.
* **Caveat.** The paper argues self-similarity only from the constant
  $d_k$. The $L^2$ distances in $\tau$ are not normalized by $h$, so the
  weights are not dimensionless in Baeza et al.'s sense. No test
  isolates the new extrapolation from the old.

**Other variants in the ILW line.** For a 3D moving body, three nested
least-squares candidates on balls of radius $1.1h$, $2.1h$ and $3.1h$
are blended with WENO-JS weights. Their linear weights are
$h_x^2 + h_y^2 + h_z^2$, its square root, and the remainder, so they
depend on the grid scale
([Liu et al. (2022)](/sources/liu-2022.md), Appendix C). Lagrange or
least-squares extrapolation is used where the solution is smooth, and the
WENO-type one only near shocks
([Ding, Shu & Zhang (2020)](/sources/ding-2020.md), §2;
[Lu et al. (2021)](/sources/lu-2021.md), Remark 2.3;
[Liu et al. (2025)](/sources/liu-2025.md), §3.2).

**Later uses (batch 10).** A sharp-interface ghost-cell immersed-boundary
solver met the failure weighted extrapolation addresses: quadratic
interpolation to the image points produced negative density and
pressure behind shocks. It fell back to inverse-distance weighting, which
reproduces only constants (compiler's observation), rather than to a nonlinear weighted
extrapolation ([Seshadri & De (2020)](/sources/seshadri-2020.md), §4.6; [immersed-boundary methods](/methods/immersed-boundary-method.md)).

# Citations

1. [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §§1–6.
2. [Lu et al. (2021)](/sources/lu-2021.md), §2.1, Remark 2.3, §2.4.
3. [Liu et al. (2022)](/sources/liu-2022.md), Appendix C.
4. [Ding, Shu & Zhang (2020)](/sources/ding-2020.md), §2.
5. [Liu et al. (2025)](/sources/liu-2025.md), §3.2.
6. [Seshadri & De (2020)](/sources/seshadri-2020.md), §4.6 (author manuscript).
