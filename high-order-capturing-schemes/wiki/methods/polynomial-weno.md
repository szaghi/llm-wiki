---
type: Method
title: "Polynomial WENO reconstruction with a dominant central stencil"
description: "WENO that blends whole candidate polynomials of the full degree K — one central and several one-sided or sector stencils — with a large linear weight on the central one, so accuracy never depends on optimal linear weights: no negative weights, any mesh, entire polynomials for ADER, at the price of a wider stencil."
status: established
aliases: [Dumbser-Käser WENO, unstructured WENO, reconstruction of entire polynomials, non-optimal WENO, modal WENO]
tags: [weno, reconstruction, finite-volume, unstructured, legendre-basis, ader]
timestamp: 2026-10-08T00:00:00Z
---

# Polynomial WENO reconstruction with a dominant central stencil

**Idea** ([Dumbser & Käser (2007)](/sources/dumbser-2007.md), §2.3).
Every candidate stencil $S_k$ carries a polynomial $p_k$ of the full
target degree $K$, and the reconstruction is the nonlinear combination
of these polynomials themselves:
$$\mathcal{P}_i = \sum_k \omega_k\, p_k,\qquad \omega_k = \frac{\tilde\omega_k}{\sum_l \tilde\omega_l},\qquad \tilde\omega_k = \frac{d_k}{(\varepsilon + \beta_k)^{q}},$$
with $d_k = d_{\mathrm c} \gg 1$ for the central stencil and $d_k = 1$
for the others. Order $K + 1$ comes from each candidate alone, not from
linear weights reproducing a larger stencil. The method therefore has
none of the negative linear weights of optimal WENO on general meshes
(Shi–Hu–Shu), and needs no separate reconstruction per quadrature point. The
output is an entire polynomial that can be evaluated and
differentiated anywhere, which is what [ADER](/methods/ader.md)
predictors and source-term quadratures need. The price, stated by the
authors, is that the scheme is not optimal: for a given order the total
stencil is wider than that of [WENO](/methods/weno.md) with optimal
weights ([Dumbser & Käser (2007)](/sources/dumbser-2007.md), §6;
[Dumbser et al. (2013)](/sources/dumbser-2013.md), §2.2).

**Unstructured meshes** ([Dumbser & Käser (2007)](/sources/dumbser-2007.md), §2).
* Each stencil is mapped to the reference triangle or tetrahedron of
  the cell being reconstructed. The Jacobians cancel from the
  conservation equations, which removes the scaling that makes physical-space
  reconstruction matrices ill-conditioned. The basis is a hierarchical
  orthogonal one, as in DG.
* Stencils are deliberately overdetermined, with 1.5 times the number of
  degrees of freedom in 2D and twice in 3D. They are solved by least
  squares with exact conservation in the central cell as a constraint.
  The inverse matrices are stored per element. Elements are added until
  no singular value vanishes.
* The stencil family is one central stencil (grown from face
  neighbours), three primary and three reverse sector stencils in 2D
  (seven in all), and four plus four in 3D (nine).
* Because everything lives on the reference element, the
  [smoothness indicator](/definitions/smoothness-indicator.md) is a
  mesh-independent quadratic form of the reconstructed coefficients,
  with one universal matrix precomputed per basis.
* Parameters: $\varepsilon = 10^{-5}$, $q = 4$, $d_{\mathrm c} = 10^3$.
  Results barely change for $d_{\mathrm c}$ between $10^2$ and $10^5$.
  Lower values favour discontinuities and higher values favour smooth
  data, and a very large $d_{\mathrm c}$ stays non-oscillatory because
  smooth one-sided stencils get far larger $\tilde\omega_k$ (§5.1, slotted cylinder).
* With ADER, WENO at most doubles the cost of the linear central-stencil
  reconstruction, despite seven or nine reconstructions. The authors
  state this is the first 3D unstructured WENO, reaching sixth order on
  tetrahedra. Very high orders oscillate on coarse grids when no smooth
  full-degree stencil fits between discontinuities. They do not lower
  the order there but rely on refinement.

**Structured meshes, modal form** ([Balsara et al. (2009)](/sources/balsara-2009.md), §2).
Reconstruct in the scaled Legendre basis,
$\mathcal{P}_i(\zeta) = \bar u_i + \hat u^{(1)}_i P_1(\zeta) + \hat u^{(2)}_i P_2(\zeta) + \dots$,
dimension by dimension, giving the cross terms afterwards. The
central stencil's linear weight is 100 times the one-sided ones and the
indicators are raised to the fourth power, again preferring stability
to the extra order of optimal weights. At third order the three
three-cell stencils give (eqs. 6–8, checked on the page image)
$$\begin{aligned}
&\text{left: } \hat u^{(1)} = \tfrac12\bar u_{i-2} - 2\bar u_{i-1} + \tfrac32\bar u_i, && \hat u^{(2)} = \tfrac12\left(\bar u_{i-2} - 2\bar u_{i-1} + \bar u_i\right),\\
&\text{central: } \hat u^{(1)} = \tfrac12\left(\bar u_{i+1} - \bar u_{i-1}\right), && \hat u^{(2)} = \tfrac12\left(\bar u_{i-1} - 2\bar u_i + \bar u_{i+1}\right),\\
&\text{right: } \hat u^{(1)} = -\tfrac32\bar u_i + 2\bar u_{i+1} - \tfrac12\bar u_{i+2}, && \hat u^{(2)} = \tfrac12\left(\bar u_i - 2\bar u_{i+1} + \bar u_{i+2}\right),
\end{aligned}$$
each with $\beta = \left(\hat u^{(1)}\right)^2 + \tfrac{13}{3}\left(\hat u^{(2)}\right)^2$
(eq. 9). At fourth order,
$\beta = \left(\hat u^{(1)} + \hat u^{(3)}/10\right)^2 + \tfrac{13}{3}\left(\hat u^{(2)}\right)^2 + \tfrac{781}{20}\left(\hat u^{(3)}\right)^2$
(eq. 15). Formulas are also given for fifth order, the building block of
Balsara and Shu's ninth-order pointwise scheme. Finite-volume
reconstruction also needs the cross moments.
* At third order, $\hat u^{(11)}$ comes from four candidates, each
  using one diagonal neighbour together with the already limited 1D
  moments.
* At fourth order, five stencils (four biased and one central with 100
  times the weight) give the three mixed second- and third-order
  moments. Eight diagonal stencils give the $xyz$ moment. The indicators
  are again sums of squares (eqs. 24–42).

This is cheaper than the earlier Balsara–Rumpf–Munz cross-term
strategy because the stencils are smaller.

**Dimension by dimension, nodal form** ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §2.2).
The 1D candidates are written in a Lagrange basis through the
Gauss–Legendre points of $[0, 1]$, and the sweeps are applied to the
degrees of freedom in $x$, then $y$, then $z$. Odd orders use three
stencils (central, fully left, fully right). Even orders use four (two
central, offset by one, and the two fully one-sided ones), each of
$K + 1$ cells. Parameters are $d_{\mathrm c} = 10^5$,
$\varepsilon = 10^{-14}$ and $q = 8$, compared with
$10^3$, $10^{-5}$ and $4$ in 2007; the values are a design choice that
differs between papers.

**Related designs.** [WENO-AO](/methods/weno-ao.md) also gives a large
centred stencil a dominant linear weight, but keeps a high-order
central polynomial whose order exceeds that of the small candidates. As
a limiter, the same reconstruction was proposed for DG on unstructured
meshes ([Dumbser & Käser (2007)](/sources/dumbser-2007.md), §6;
[WENO limiters for DG](/methods/weno-limited-dg.md)). On subgrids it is
the robust scheme of the
[a posteriori subcell limiter](/methods/a-posteriori-subcell-limiting.md).

**In the reviews (batch 6).** Shu cites Dumbser and Käser among the
schemes that take arbitrary positive linear weights, accepting the
small-stencil order on unstructured meshes ([Shu (2020)](/sources/shu-2020.md), §§3.2.2–3.3;
[negative linear weights](/methods/negative-linear-weights.md)).

# Citations

1. [Dumbser & Käser (2007)](/sources/dumbser-2007.md), §§2, 5, 6 (eqs. 19–25 read from the page images).
2. [Balsara et al. (2009)](/sources/balsara-2009.md), §2 (eqs. 6–15 read from the page image).
3. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §2.2.
4. [Shu (2020)](/sources/shu-2020.md), §§3.2.2–3.3.
