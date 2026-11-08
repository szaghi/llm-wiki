---
type: Source
title: "LeVeque & Li (1994) — The immersed interface method for elliptic equations with discontinuous coefficients and singular sources"
description: "Introduces the immersed interface method: on a uniform grid, irregular points next to an interface get six-point stencils and right-hand-side corrections derived from Taylor expansions in local coordinates and the jump conditions, giving global second-order accuracy for discontinuous coefficients, singular sources and prescribed jumps, where a discrete-delta source is only first order."
resource: "doi:10.1137/0731054"
source_kind: paper
authors: [LeVeque R.J., Li Z.]
year: 1994
venue: "SIAM J. Numer. Anal. 31(4):1019-1044"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/1994_Crossref_SIAM_Journal_on_Numerical_Analysis_LeVeque_The_Immersed_Interface_Method_for_Elliptic_Equations_with_Di.pdf"
tags: [immersed-interface, sharp-interface, elliptic, jump-conditions, accuracy, delta-function]
timestamp: 2026-11-08T17:44:00Z
---

# Summary

LeVeque and Li develop the [immersed interface method](/methods/immersed-interface-method.md)
for $\nabla\cdot(\beta\nabla u)+\kappa_0u=f_0$ on a rectangle with a uniform grid
and an interface $\Gamma$ not aligned with it, across which the coefficients
may jump, the source may carry a delta-function or dipole layer, and jumps in
$u$ and in the flux may be prescribed. At irregular points the stencil
coefficients and a correction term come from Taylor expansions about a point
of $\Gamma$ in local normal–tangential coordinates and from the jump
conditions; an $O(h)$ local truncation error on these points yields a
globally second-order solution. If $\beta$ is continuous only the right-hand
side changes, so fast Poisson solvers still apply. The discrete-delta
approach of Peskin's method, analysed for comparison, is first order in 2-D
([first-order accuracy of regularized-delta forcing](/results/first-order-accuracy-of-regularized-delta-forcing.md)).
The method is a sharp alternative to diffuse forcing
([sharp and diffuse interfaces](/definitions/sharp-and-diffuse-interface.md)).

# Version read

Version of record (SIAM download), SIAM J. Numer. Anal. 31, 1019–1044
(1994), 26 pages, all read. The text layer drops most Greek letters and
garbles many display equations; the structure of every derivation, the
linear systems' logic and all tables are legible. Page-1 title and authors
match Crossref.

# Key claims

1. Second-order accuracy on a uniform grid is possible with interfaces not aligned with the grid, by modifying the centred differences near the interface (Abstract, §6). **Shown**
2. The name "immersed interface method" was chosen because the approach is "in the same spirit as Peskin's immersed boundary method but allows more general interface conditions"; second-order IB methods for Navier–Stokes were the original motivation (§1). **Stated**
3. In 1-D, the hat discrete delta gives the exact solution of $u''=c\,\delta(x-x_\Gamma)$ at grid points (citing Beyer and LeVeque 1992); in 2-D a discrete-delta right-hand side "does not appear" able to give second order at all grid points (§1). **Stated**
4. Harmonic averaging of a discontinuous coefficient has an $O(1)$ local truncation error at interface points in 1-D but is second order by cancellation; in 2-D it does not appear to be second order (§1.1, §2). **Stated**/**Derived**
5. At irregular points six stencil points (the five-point stencil plus the nearest diagonal point) and six equations, from the vanishing of the coefficients of $u^-$ and its first and second derivatives in local coordinates, determine the weights; the correction $C_{\mathbf i}$ follows (§3–4). **Derived**
6. An $O(h)$ local truncation error at the irregular points suffices for $O(h^2)$ global error, because they form a lower-dimensional set (§3). **Stated**
7. The PDE is invariant under the shift-and-rotation to local coordinates (§4). **Derived**
8. If $\beta$ is continuous the standard five-point weights satisfy the system to $O(h)$; only the right-hand side changes (§4, §6). **Derived**
9. If $\beta^-/\beta^+>0$ the $6\times6$ system is uniquely solvable (proof "not very complicated but rather tedious", omitted); for $\beta^-\beta^+<0$ it is singular only for special jump values (§3). **Stated**
10. The resulting matrix is nearly diagonally dominant; line SOR with the optimal Poisson parameter converges almost as fast as for constant $\beta$ (§3). **Shown**
11. Example 1 (singular source on a circle): discrete delta first order, immersed interface method second order (§5, Table 1). **Shown**
12. Example 2 (coefficient jump with ratio $1/10$ and a negative ratio, plus a source) and Example 3 (prescribed jumps in $u$ and $\partial_n u$): second order; a quadratic solution is exact to round-off (§5, Tables 2–3). **Shown**

# Notation map

| LeVeque & Li (1994) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Omega$, $\Gamma$ | $\Omega$, $\Gamma$ | agree |
| $\beta$, $\kappa$, $f$ | $\beta$, $\kappa_0$, $f_0$ | **collision**: $\kappa$ is the volume fraction in the registry |
| $C(s)$ | $\sigma(s)$ | single-layer source strength |
| $w(\eta)=[u]$, $v(\eta)=[\beta u_n]$ | $w$, $g$ | prescribed jumps; registry reserves $\mathbf v$-like letters for velocities |
| $(\xi,\eta)$ | $(\xi,\zeta)$ | local normal and tangential coordinates; $\eta$ is the penalty parameter in the registry |
| $\gamma_k$, $C_{ij}$ | $\gamma_k$, $C_{\mathbf i}$ | stencil weights and correction, page-local |
| $d_h(x)$ | $h^{-1}\varphi(x/h)$ | discrete delta |
| $+$, $-$ sides | "$+$" / "$-$", $[w]=w^+-w^-$ | agree |
| $\rho=\beta^-/\beta^+$ | $\beta^-/\beta^+$ | $\rho$ is density in the registry |

# Reference list

The paper prints 26 numbered references; all are merged complete into the
[bibliography](/bibliography.md) from the Crossref deposited list (26
entries, one per printed reference).

# Pages created or updated

Chunk 1 (2026-11-08), list updated in chunk 4 (2026-11-08). This source is cited on:

- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md)
- [Classical (Peskin) immersed boundary method](/methods/classical-immersed-boundary-method.md)
- [Immersed interface method](/methods/immersed-interface-method.md)
- [Regularized delta function $\delta_h$](/operators/regularized-delta-function.md)
- [First-order accuracy of regularized-delta forcing at interfaces](/results/first-order-accuracy-of-regularized-delta-forcing.md)
