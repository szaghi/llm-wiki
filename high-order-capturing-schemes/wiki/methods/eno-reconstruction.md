---
type: Method
title: "ENO reconstruction and schemes"
description: "Essentially non-oscillatory schemes: an adaptive stencil grown one point at a time toward the smaller divided difference, giving uniform high order up to discontinuities without monotonicity limiters."
status: established
aliases: [ENO, essentially non-oscillatory schemes, adaptive stencil]
tags: [eno, reconstruction, shock-capturing]
timestamp: 2026-10-13T00:00:00Z
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
$r+1$ points ($r$ cells, order $r$) ([Harten et al. (1987)](/sources/harten-1987.md), §3;
[Shu (1998)](/sources/shu-1998.md), Procedure 2.1). On uniform grids
undivided differences $\Delta^l$ are used instead.
[Shu (1998)](/sources/shu-1998.md) reports that this hierarchy is more
robust across grid sizes than alternatives such as comparing only the
highest-degree differences of all candidates.

**Properties** for piecewise smooth data, starting from the two-point
stencil ([Shu (1998)](/sources/shu-1998.md), §2.2.1):
1. full accuracy: the interpolant of $\mathcal{U}$ on the chosen stencil
   differs from $\mathcal{U}$ by $O(h^{r+1})$ in every cell not
   containing a discontinuity, i.e. right up to it;
2. that interpolant is monotone in a cell that contains a discontinuity;
3. the reconstruction is total variation bounded.
Property 2 is proved for a step function by counting the zeros of the
interpolant's derivative.

## Schemes

* **Cell-average ENO** ([Harten et al. (1987)](/sources/harten-1987.md)):
  the abstract scheme reconstructs from $\bar u^n$, evolves the
  reconstruction exactly over $\Delta t$, and takes the cell averages of
  the result as $\bar u^{n+1}$ (Godunov for $r=1$, MUSCL-type for $r=2$). The exact "solution in the small" is
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
  ([Shu & Osher (1989)](/sources/shu-1989.md)). The smooth-data Burgers
  test that the ENO papers run is on
  [Burgers equation: shock formation](/benchmarks/burgers-shock-formation.md).

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
  stencil with a factor of about 2); the flux is not smooth; only one
  of $r$ candidate stencils is used, giving order $r$ where $2r-1$ is
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

**Later uses (batch 6): the reviews.**
* *Sign property* (Fjordholm, Mishra and Tadmor, as surveyed by
  [Shu (2020)](/sources/shu-2020.md), §2.3.2). For ENO reconstruction the interface jump
  $u^+_{i+1/2} - u^-_{i+1/2}$ has the sign of $\bar u_{i+1} - \bar u_i$, and
  their ratio is bounded by a constant that depends only on the degree.
  This rules out saw-tooth reconstructions and opens the way to
  entropy-stable ENO of any order. It cannot be proved for biased ENO and
  holds for WENO only in a very special class.
* *Why WENO replaced ENO* ([Shu (2020)](/sources/shu-2020.md), §3). The discarded stencils could help
  in smooth regions. The digital stencil choice makes the result at most
  Lipschitz in the data, which may hurt steady-state convergence. It can
  pick downwind-biased stencils, and for data with monotone derivatives
  such as $e^x$ the stencil can be very biased, with possible stability
  and accuracy issues (Rogerson and Meiburg, cited).
* The monotonicity of the polynomial in a discontinuous cell carries over
  to WENO's convex combination ([Shu (2009)](/sources/shu-2009.md), §2.1; [WENO](/methods/weno.md)).

**Later uses (batch 18).** *The first paper of the series: UNO2*
([Harten & Osher (1987)](/sources/harten-1987-b.md)), now ingested; it is
the "second-order non-oscillatory modification of MUSCL (Harten & Osher)"
of the opening paragraph.
* *The modification is the slope* (§§3–4, 7, eqs. 3.2, 4.2, 7.1–7.3). The
  scheme is a Godunov/MUSCL-type scheme with a piecewise-linear
  reconstruction $\mathcal P_i = \bar u_i + \hat u^{(1)}_i\zeta$ and
  $$\hat u^{(1)}_i = \operatorname{minmod}\left(\Delta^1\bar u_i - \tfrac12\operatorname{minmod}(\delta^2\bar u_i, \delta^2\bar u_{i+1}),\ \Delta^1\bar u_{i-1} + \tfrac12\operatorname{minmod}(\delta^2\bar u_{i-1}, \delta^2\bar u_i)\right),$$
  the minmod of the one-sided derivatives (times $h$) of a nonoscillatory
  piecewise-parabolic interpolant of the cell averages. Its TVD
  counterpart TVD2 uses $\Delta^1\bar u_i$ and $\Delta^1\bar u_{i-1}$ in
  the same minmod and differs "only in the reconstruction step". The UNO2
  slope approximates $\partial_x u$ to $O(h^2)$ also at extrema, the TVD
  slope only to $O(h)$, with a coefficient that is not smooth at extrema
  (p. 282).
* *A two-candidate precursor of the stencil choice* (§3, eq. 3.2d). On
  $[x_i, x_{i+1}]$ the interpolant takes, of the parabolas through
  $\{x_{i-1}, x_i, x_{i+1}\}$ and $\{x_i, x_{i+1}, x_{i+2}\}$, the one with
  the smaller second difference, the one that "deviates the least from the
  line" through the two shared points. It has no more local extrema than
  the data (pp. 285–286). Growing such a choice one point at a time is
  the ENO procedure above (reader's reading; the 1987 paper does not use
  the word "ENO").
* *Measured* (§7, Tables 2–3). Linear advection of $\sin\pi x$ to $t = 2$
  at CFL 0.8: UNO2 is second order in $L_\infty$ and $L_1$, TVD2 "only
  first-order accurate in $L_\infty$"; at 160 cells the $L_\infty$ errors
  are $9.201\times10^{-5}$ and $5.975\times10^{-3}$. On smooth Burgers data
  ($\sin\pi x$, $t = 0.15$, CFL 0.5) the same ordering holds, and the
  nonlinear scheme is proved second order "including local extrema and
  sonic ($f' = 0$) points" (eqs. 6.8–6.10, p. 294)
  ([accuracy at critical points](/properties/accuracy-at-critical-points.md)).
* *The price.* Not TVD: the TV may grow by a bounded amount per step
  (5.5b), and uniform TV boundedness is not proved
  ([essentially non-oscillatory](/definitions/essentially-non-oscillatory.md)).
* *Primitive function, at second order* (§7, eqs. 7.10b–d). ANO2,
  initialized with exact cell averages, recovers point values by
  differentiating the interpolant of $\mathcal U(x_{i+1/2})$, the
  reconstruction-via-primitive idea of the stencil-choice section above in
  second-order form.
* *Systems* (eqs. 7.12–7.15): a "formal extension" with a Roe average and
  field-by-field slopes in local characteristic variables
  ([characteristic decomposition](/methods/characteristic-decomposition.md)).
* *No third order in it.* The paper builds only the second-order scheme
  and its variants (UNO2, FNO2, ANO2); higher orders are announced for the
  later papers of the series.

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §§1–7 and Appendix.
2. [Shu & Osher (1988)](/sources/shu-1988.md), §III.
3. [Shu & Osher (1989)](/sources/shu-1989.md), §II.
4. [Shu (1998)](/sources/shu-1998.md), §§2.2.1, 2.3.3–2.3.4.
5. [Jiang & Shu (1996)](/sources/jiang-1996.md), §1.
6. [Suresh & Huynh (1997)](/sources/suresh-1997.md), introduction.
7. [Shu (2020)](/sources/shu-2020.md), §§2–3.
8. [Shu (2009)](/sources/shu-2009.md), §2.1.
9. [Harten & Osher (1987)](/sources/harten-1987-b.md), §§1–7, Tables 2–3.
