---
type: Method
title: "Reconstruction from cell averages"
description: "Recovering point values (or polynomials) of $k$-th order accuracy from cell averages via interpolation of the primitive function; the building block of finite-volume ENO/WENO/PPM schemes."
status: established
aliases: [reconstruction via primitive function, finite-volume reconstruction]
tags: [reconstruction, finite-volume]
timestamp: 2026-10-08T00:00:00Z
---

# Reconstruction from cell averages

**The problem** ([Shu (1998)](/sources/shu-1998.md), Problem 2.1): given
cell averages $\bar u_i$, find in each cell a polynomial $p_i$ of degree
at most $k-1$ with $p_i(x) = u(x) + O(h^k)$ in $I_i$. The interface values
$u^-_{i+1/2} = p_i(x_{i+1/2})$ and $u^+_{i-1/2} = p_i(x_{i-1/2})$ are then
$k$-th order accurate.

**Via the primitive** ([Harten et al. (1987)](/sources/harten-1987.md),
"RP"). The primitive $\mathcal{U}$ is known exactly at interfaces from
the averages. Interpolate it at the $k+1$ interface points of a
$k$-cell stencil by a polynomial $P$ of degree $k$ and set $p = P'$.
Then $p$ reproduces every cell average in the stencil, and
$p = u + O(h^k)$ where $u$ is smooth there. The procedure needs no
uniform grid. Because the map from averages to interface values is
linear, each stencil position relative to $x_{i+1/2}$ gives fixed
constants that express $u_{i+1/2}$ as a linear combination of the
stencil's averages; they depend on the local spacings but not on the
data, and are tabulated for uniform grids up to seventh order
([Shu (1998)](/sources/shu-1998.md), Table 2.1).

**Via deconvolution** ([Harten et al. (1987)](/sources/harten-1987.md),
"RD"). On a uniform grid the averages are point values of the sliding
average of $u$. Taylor-expanding the sliding average gives a triangular,
diagonally dominant linear system between derivatives of the averaged
function and of $u$. Interpolating the averages and inverting the system
(back substitution) recovers $u$ and its derivatives to $O(h^k)$.

**Adaptive stencils.** Fixed-stencil reconstruction of degree two or
higher oscillates at discontinuities, with an $O(1)$ Gibbs-like
overshoot that does not decay with refinement
([Shu (1998)](/sources/shu-1998.md), Fig. 2.1). The stencil is therefore
chosen adaptively ([ENO](/methods/eno-reconstruction.md)) or the
candidate reconstructions are blended ([WENO](/methods/weno.md),
[central WENO](/methods/central-weno.md)), or a higher-order value is
limited ([PPM](/methods/ppm.md),
[monotonicity-preserving limiting](/methods/monotonicity-preserving-limiter.md)).

## In a finite-volume scheme

The semi-discrete scheme is
$\frac{d}{dt}\bar u_i = -\frac{1}{h_i}\left(\hat f_{i+1/2} - \hat f_{i-1/2}\right)$
with $\hat f_{i+1/2} = \hat f(u^-_{i+1/2}, u^+_{i+1/2})$ a
[monotone flux](/definitions/monotone-flux.md) or a Riemann solver
([Shu (1998)](/sources/shu-1998.md), §2.3.1). It applies on arbitrary
meshes ([Liu, Osher & Chan (1994)](/sources/liu-1994.md) use this form
for WENO).

**Multi-D cost.** On Cartesian grids, the reconstruction uses tensor
products: two successive one-dimensional reconstructions per point in 2D
($n$ in $n$ dimensions). Above second order the face fluxes also need
Gaussian quadrature, and for WENO the linear weights differ at each
quadrature point. [Shu (1998)](/sources/shu-1998.md) (§3.3) concludes
that multi-D finite-volume schemes above second order are rarely used,
and that the finite-difference version costs about a factor of four less
in 2D ([conservative finite difference](/methods/conservative-finite-difference.md)).
[Balsara & Shu (2000)](/sources/balsara-2000.md) give the same cost
argument against high-order finite-volume ENO.

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §§1, 3 and Appendix.
2. [Shu (1998)](/sources/shu-1998.md), §§2.1.1, 2.3.1, 3.1.1, 3.3.1.
3. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §§2–3.
4. [Balsara & Shu (2000)](/sources/balsara-2000.md), §I.
