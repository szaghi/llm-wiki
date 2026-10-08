---
type: Method
title: "ENO reconstruction and schemes"
description: "Essentially non-oscillatory schemes: an adaptive stencil grown one point at a time toward the smaller divided difference, giving uniform high order up to discontinuities without monotonicity limiters."
status: established
aliases: [ENO, essentially non-oscillatory schemes, adaptive stencil]
tags: [eno, reconstruction, shock-capturing]
timestamp: 2026-10-08T00:00:00Z
---

# ENO reconstruction and schemes

Introduced in its arbitrary-order form by
[Harten et al. (1987)](/sources/harten-1987.md), the third paper of a
series that began with a second-order non-oscillatory modification of
MUSCL (Harten & Osher). The aim is uniform order $r$ in smooth regions
with no Gibbs-like oscillation at discontinuities
([essentially non-oscillatory](/definitions/essentially-non-oscillatory.md)).

## The stencil choice

The reconstruction ([finite-volume reconstruction](/methods/finite-volume-reconstruction.md))
interpolates the primitive $\mathcal{U}$. Divided differences measure
smoothness: where $\mathcal{U}$ is smooth,
$\mathcal{U}[x_a, \dots, x_{a+j}] = \mathcal{U}^{(j)}(\xi)/j!$, while
a jump inside the stencil makes it $O(h^{-j})$.
The stencil for cell $I_i$ starts from the two points
$\{x_{i-1/2}, x_{i+1/2}\}$ (one cell) and grows by one point at a time,
adding the left or the right neighbour according to which gives the
smaller absolute divided difference of the next degree, until it has
$k+1$ points ([Harten et al. (1987)](/sources/harten-1987.md), §3;
[Shu (1998)](/sources/shu-1998.md), Procedure 2.1). On uniform grids
undivided differences $\Delta^l$ are used instead.
[Shu (1998)](/sources/shu-1998.md) reports that this hierarchy is more
robust across grid sizes than alternatives such as comparing only the
highest-degree differences of all candidates.

**Properties** for piecewise smooth data, starting from the two-point
stencil ([Shu (1998)](/sources/shu-1998.md), §2.2.1):
1. full accuracy, $P = \mathcal{U} + O(h^{k+1})$, in every cell not
   containing a discontinuity, i.e. right up to it;
2. $P$ is monotone in a cell that contains a discontinuity;
3. the reconstruction is total variation bounded.
Property 2 is proved for a step function by counting the zeros of $P'$.

## Schemes

* **Cell-average ENO** ([Harten et al. (1987)](/sources/harten-1987.md)):
  the abstract scheme reconstructs, evolves exactly and averages,
  $\bar u^{n+1} = A_h E(\Delta t) R(\cdot; \bar u^n)$ (Godunov for
  $r=1$, MUSCL-type for $r=2$). The exact "solution in the small" is
  replaced by a Cauchy–Kowalewski Taylor expansion in time of each
  cell's polynomial, a Gaussian quadrature of the interface flux in
  time, and a Riemann solver (Roe's) that serves only as a *pointer*
  deciding which side's expansion is valid at the interface. The
  importance of the Riemann solver decreases with order. Systems use
  [characteristic decomposition](/methods/characteristic-decomposition.md).
* **Flux ENO** ([Shu & Osher (1988)](/sources/shu-1988.md),
  [(1989)](/sources/shu-1989.md)): the adaptive stencil is applied to
  the numerical flux of a point-value scheme
  ([conservative finite difference](/methods/conservative-finite-difference.md)),
  with [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) time stepping.
  This removes the reconstruction and the Lax–Wendroff procedure and
  makes multi-D simple. For linear 1D equations it is equivalent to
  cell-average ENO with RP up to the choice of stencil.
* **Upwinding by the first point.** The initial stencil point fixes the
  upwind bias; starting on the wrong side was unstable for Burgers'
  equation even with ENO stencil choice up to third order
  ([Shu & Osher (1989)](/sources/shu-1989.md)).

## Accuracy and stability

* Orders are formal: from the local truncation error in smooth regions.
  The leading error coefficient is discontinuous where the stencil
  changes orientation, which can happen at critical points; there the
  pointwise error loses one order, so Harten et al. write such schemes
  as "$r$th order accurate" in quotes ($r$-th in $L_1$, $(r-1)$-th in
  the maximum norm). A variant pushes the non-smoothness to
  $O(h^{r+1})$ ([Harten et al. (1987)](/sources/harten-1987.md),
  Remarks 1.2, 3.1). See
  [accuracy at critical points](/properties/accuracy-at-critical-points.md).
* Linear stability analysis does not apply: the stencil moves. Harten
  et al. show the adaptivity reacts to a growing downwind instability by
  turning the stencil. No convergence result exists above second order,
  even for smooth solutions ([Shu (1998)](/sources/shu-1998.md), §2.3.4).
  A capped variant is provably convergent but impractical (mesh-size
  dependent parameters), and Shu cautions against modifying schemes only
  to obtain proofs.
* **Drawbacks** that motivated [WENO](/methods/weno.md)
  ([Jiang & Shu (1996)](/sources/jiang-1996.md);
  [Shu (1998)](/sources/shu-1998.md), §2.2.2): the stencil can switch on
  round-off near zeros of the solution's derivatives, which can cost
  accuracy (Rogerson & Meiburg; repaired by biasing toward a preferred
  stencil with a factor $b \approx 2$); the flux is not smooth; only one
  of $k$ candidate stencils is used, giving order $k$ where $2k-1$ is
  available; and the logical branches run poorly on vector machines.
  [Suresh & Huynh (1997)](/sources/suresh-1997.md) add that ENO (and
  WENO) smear discontinuities nearly as much as each other.

## Boundaries

ENO needs no numerical boundary conditions in the usual sense: the
stencil is restricted to available points, which biases it against the
wind at one boundary; experiments show strong stability
([Harten et al. (1987)](/sources/harten-1987.md); see also
[Shu (1998)](/sources/shu-1998.md), §2.3.3, for ghost values set huge so
that the selection avoids them).

## Positivity in the reconstruction

For the two interacting blast waves, high-order polynomials can make
density or pressure negative when a low-pressure region shrinks to one
or two cells. [Harten et al. (1987)](/sources/harten-1987.md) impose a
positivity condition on the reconstruction and lower the order locally
until it holds; since the test is $O(h)$ in smooth regions, the
asymptotic order is unaffected.

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §§1–7 and Appendix.
2. [Shu & Osher (1988)](/sources/shu-1988.md), §III.
3. [Shu & Osher (1989)](/sources/shu-1989.md), §II.
4. [Shu (1998)](/sources/shu-1998.md), §§2.2.1, 2.3.3–2.3.4.
5. [Jiang & Shu (1996)](/sources/jiang-1996.md), §1.
6. [Suresh & Huynh (1997)](/sources/suresh-1997.md), introduction.
