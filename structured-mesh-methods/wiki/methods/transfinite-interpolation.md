---
type: Method
title: "Transfinite interpolation"
description: "Algebraic grid generation by Boolean sums of univariate interpolation projectors with blending functions: the mapping of the unit square (cube) matches the boundary curves (and optionally interior curves and derivatives) at a non-denumerable set of points; the bilinear case is the Coons patch, isoparametric mappings are special cases, and validity (univalence) is not guaranteed."
status: established
aliases: [TFI, Coons patch, blending-function interpolation, algebraic grid generation]
tags: [algebraic-generation, interpolation, grid-generation]
timestamp: 2026-11-08T20:24:00Z
---

# Transfinite interpolation

[Gordon & Hall (1973)](/sources/gordon-1973.md) generate a
[boundary-fitted coordinate system](/definitions/boundary-fitted-coordinate-system.md)
by interpolating the boundary of the region, given as a "primitive" map
$\mathbf F$ known on the boundary of the unit square, into its interior.

## Construction

With univariate interpolation projectors $\mathcal P_\xi$ and $\mathcal P_\eta$
built from blending functions $\varphi_0,\varphi_1$ that satisfy
$\varphi_m(\xi_n)=\delta_{mn}$, the Boolean sum

$$\mathbf x=(\mathcal P_\xi\oplus\mathcal P_\eta)[\mathbf F]=\mathcal P_\xi[\mathbf F]+\mathcal P_\eta[\mathbf F]-\mathcal P_\xi\mathcal P_\eta[\mathbf F]$$

interpolates $\mathbf F$ on the *whole* boundary of the square — a
non-denumerable ("transfinite") set of points — whereas the tensor product
$\mathcal P_\xi\mathcal P_\eta$ matches only the four corners. With linear
blending functions this is the bilinearly blended interpolant

$$\begin{aligned}\mathbf x(\xi,\eta)={}&(1-\xi)\mathbf F(0,\eta)+\xi\mathbf F(1,\eta)+(1-\eta)\mathbf F(\xi,0)+\eta\mathbf F(\xi,1)\\&-\big[(1-\xi)(1-\eta)\mathbf F(0,0)+\xi(1-\eta)\mathbf F(1,0)+(1-\xi)\eta\mathbf F(0,1)+\xi\eta\mathbf F(1,1)\big],\end{aligned}$$

the simplest Coons patch. Higher-order (quadratic, cubic Hermite) blending
also matches interior coordinate curves or boundary derivatives;
isoparametric element mappings are special cases; the same formulas
coordinatize shell surfaces in 3-space and, with trivariate projectors,
solids.

## Validity

The map is cheap and explicit, but nothing makes it univalent. A nonzero
Jacobian gives only local invertibility, and a poor boundary
parametrization makes the map fold outside the region ("overspill"); for an
L-shaped region Gordon and Hall obtain a univalent map by reparametrizing
the boundary. Conformal maps, which would be orthogonal, are rejected as
equivalent in cost to solving Laplace's equation. Thompson, Warsi and
Mastin (1982, Section H) note that many algebraically generated grids lack
the smoothness of elliptic ones and propagate boundary slope
discontinuities inward ([elliptic grid generation](/methods/elliptic-grid-generation.md)).

# Citations

- [Gordon & Hall (1973)](/sources/gordon-1973.md) — transfinite mappings, univalency.
- [Thompson, Warsi & Mastin (1982)](/sources/thompson-1982.md) — Section H.
