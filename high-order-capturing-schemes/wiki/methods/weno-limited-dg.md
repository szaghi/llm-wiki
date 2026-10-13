---
type: Method
title: "WENO limiters for discontinuous Galerkin schemes"
description: "Limiting RKDG by first flagging troubled cells (TVB minmod) and then replacing their polynomial — cell average kept — by one rebuilt from WENO reconstructions of neighbouring cell averages at Gauss-type points, which keeps the DG order where good cells are wrongly flagged."
status: established
aliases: [WENO limiter, RKDG with WENO limiters, troubled-cell indicator, TVB limiter, Hermite WENO limiter]
tags: [weno, dg, limiter, finite-volume]
timestamp: 2026-10-13T00:00:00Z
---

# WENO limiters for discontinuous Galerkin schemes

**Setting** ([Qiu & Shu (2005)](/sources/qiu-2005.md), §§1–2). The
Runge–Kutta DG method of Cockburn and Shu represents the solution in
$I_i$ by $\mathcal{P}_i = \sum_{l=0}^{K}\hat u^{(l)}_i P_l(\zeta)$. It
evolves the moments by testing with each basis function, with a
[monotone flux](/definitions/monotone-flux.md) or Riemann solver at
interfaces, and advances in time with [SSP Runge–Kutta](/methods/ssp-runge-kutta.md).
Smooth solutions and weak shocks need nothing more. Strong shocks
produce oscillations and nonlinear instability, and the authors call
robust limiters "one of the bottlenecks" of DG for conservation laws.

**The standard TVB limiter.** Replace each deviation of an interface
value from the mean, $\mathcal{P}_i(x_{i+1/2}) - \bar u_i$ and
$\bar u_i - \mathcal{P}_i(x_{i-1/2})$, by
$\operatorname{minmod}_M(\cdot,\ \bar u_{i+1} - \bar u_i,\ \bar u_i - \bar u_{i-1})$.
This returns its first argument when $\vert a_1\vert \le M h^2$ and the
plain minmod otherwise, so the constant $M$ sets how large a second
derivative at a smooth extremum is left alone. A
small $M$ degrades accuracy at extrema, and a large $M$ lets oscillations
through. For systems $M$ is hard to estimate
([Qiu & Shu (2005)](/sources/qiu-2005.md), eqs. 2.4–2.5).

## Two-step WENO limiting

([Qiu & Shu (2005)](/sources/qiu-2005.md), §2.)
1. **Troubled cells.** A cell is troubled ($\mathcal{B}_i = 1$) when
   the TVB limiter would change its interface values. False alarms
   cost time but not order, so the detector need not be sharp. For
   systems a characteristic-based detector is used, because the
   componentwise one flags many good cells.
2. **Reconstruction.** In troubled cells only $\bar u_i$ is kept. The
   point values at $K + 1$ Gauss-type points come from finite-volume
   [WENO](/methods/weno.md) of order at least $2K + 1$ on the
   $2K + 1$ cells $I_{i-K}, \dots, I_{i+K}$. The moments are then
   rebuilt by quadrature,
   $\hat u^{(l)}_i \propto \sum_G w_G\, u(x_G)\, P_l(x_G)$, $l \ge 1$,
   with Gauss-type points $x_G$ and weights $w_G$.
   The points are two-point Gauss for $K = 1$, four-point
   Gauss–Lobatto for $K = 2$, and four-point Gauss for $K = 3$.
   At three-point Gauss for $K = 2$ the linear weights of the middle
   point are negative, which Gauss–Lobatto avoids (Remark 2.1). For
   $K = 2$ the linear weights are $\tfrac1{10}$, $\tfrac6{10}$,
   $\tfrac3{10}$ at $x_{i+1/2}$, and
   $\tfrac{91 + 9\sqrt5}{440}$, $\tfrac{129}{220}$,
   $\tfrac{91 - 9\sqrt5}{440}$ at $x_i + \sqrt5 h/10$, left to right.
   The [smoothness indicators](/definitions/smoothness-indicator.md)
   are those of Jiang and Shu and are shared by all points of the cell.
   They use $q = 2$ and $\varepsilon = 10^{-6}$.
   Reconstructing the moments directly from averages works for $K = 1, 2$,
   but the linear weights do not exist for $K = 3$ (Remark 2.2).

**Evidence** ([Qiu & Shu (2005)](/sources/qiu-2005.md), §3).
* With $M = 0.01$, which flags many good cells, the WENO limiter keeps
  both the order and the error size of unlimited RKDG ($K = 1$–$3$, 1D
  and 2D Burgers, 2D Euler, non-uniform meshes). The TVB limiter alone
  at that $M$ would fall to second order in $L^1$.
* Larger $M$ flags fewer cells and resolves contacts and the
  post-shock waves of the [Shu–Osher problem](/benchmarks/shu-osher-problem.md)
  better, so RKDG resolves better than the WENO reconstruction it
  replaces. $M = 300$ is too large: weak shocks are no longer flagged
  and small oscillations appear.
* In the [double Mach reflection](/benchmarks/double-mach-reflection.md)
  only 2–25% of cells are troubled, more at higher $K$ and small $M$
  (Table 4). Results are comparable to TVB with $M = 50$.

**Limitations seen later.** In a review of a priori DG limiters,
[Dumbser et al. (2014)](/sources/dumbser-2014.md) (§3.1) group them
into three families: artificial viscosity, slope or moment limiters
(TVB, moment-based, hierarchical vertex-based), and (H)WENO limiters
of this kind. Two drawbacks of WENO limiting are noted.
* Moments rebuilt from main-grid averages lose part of DG's subcell
  resolution.
* Detection depends on parameters that are often problem-dependent.

Hermite WENO limiters, which also use derivatives, were introduced for
compactness (Qiu and Shu 2003, 2005, cited there). A polynomial
reconstruction on unstructured meshes was proposed as a DG limiter by
[Dumbser & Käser (2007)](/sources/dumbser-2007.md) (§6;
[polynomial WENO](/methods/polynomial-weno.md)). The a posteriori
alternative recomputes troubled cells with a different scheme on a
subgrid instead of post-processing them
([a posteriori subcell limiting](/methods/a-posteriori-subcell-limiting.md)).

**Later uses (batch 6).** *The reviews.* DG is more flexible than WENO on
unstructured meshes but "less robust in dealing with solutions with
strong shocks", because its limiters lag behind WENO ([Shu (2009)](/sources/shu-2009.md), §5.1). WENO
reconstruction suits troubled cells because it keeps high order where a
smooth cell is flagged by mistake, and no troubled-cell indicator "is
bullet-proof". After the first, wider limiters came compact ones (Zhong
and Shu; Zhu et al.) and multi-resolution limiters, which "appear to be
quite robust". Hermite WENO fits DG's compact data structure
([Shu (2020)](/sources/shu-2020.md), §§3.2.4, 4.3).
Both limiter families have their own pages: [Hermite WENO](/methods/hermite-weno.md) and [multi-resolution WENO](/methods/multi-resolution-weno.md).

**Later uses (batch 7).**
* *Viscous flows need no oscillation limiter.* Euler DG with only the
  positivity limiter becomes more oscillatory under refinement or higher
  degree, and oscillations can move shocks. Navier–Stokes DG with only the
  positivity limiter becomes less oscillatory once the viscous scales are
  resolved. TVB-limited DG cannot run a Mach 10 corner problem without the
  positivity limiter and smears its Kelvin–Helmholtz roll-ups
  ([Zhang (2017)](/sources/zhang-2017.md), §§1.7, 6).
* *The compact limiter in full* at third order in 2D: each von Neumann
  neighbour's polynomial is shifted into the zone with its mean replaced
  by the zone's; the indicator is
  $(\hat u^{(10)})^2 + (\hat u^{(01)})^2 + \tfrac{13}{3}\left((\hat u^{(20)})^2 + (\hat u^{(02)})^2\right) + \tfrac76(\hat u^{(11)})^2$;
  linear weights 0.96 for the zone and 0.01 for each neighbour, power 2,
  $\varepsilon = 10^{-12}$, attributed to Zhong and Shu (2013), not in the
  corpus ([Balsara (2017)](/sources/balsara-2017-d.md), §VI.2, eqs. 95–109).
* *PNPM in perspective*: evolving degree 1 or 2 and reconstructing higher
  "often" gives most of the accuracy of DG at larger time steps (§VI).

**Later uses (batch 16).** *The TVB limiter at its multi-D source*
([Cockburn & Shu (1998)](/sources/cockburn-1998.md), §§2.3, 3.4;
[RKDG](/methods/rkdg.md)).
* *Formula.* On rectangles each face deviation from the mean,
  $\tfrac12\hat u^{(10)}$ in $x$ and $\tfrac12\hat u^{(01)}$ in $y$, is
  replaced by $\operatorname{minmod}_M$ of itself and the two mean
  differences in that direction, threshold $M h^2$ per direction (eqs.
  3.6–3.7): the standard limiter above, written for the linear moments.
* *Choice of $M$.* "Usually, the numerical results are not sensitive to
  the choice of M in a large range. In all the calculations in this paper
  we take M to be 50", with an estimate from second derivatives referred
  to part II of the series. This is the $M = 50$ of the Qiu–Shu
  comparison above. Qiu and Shu's "for systems $M$ is hard to estimate"
  and Cockburn and Shu's insensitivity are different emphases: neither
  paper tests the other's claim.
* *Characteristic limiting.* For systems the slope and the two mean
  differences are projected with the left eigenvectors of the directional
  Jacobian at the cell mean, limited componentwise and projected back; on
  triangles the direction is from the barycentre to each edge midpoint
  ([local characteristic decomposition](/methods/characteristic-decomposition.md)).
* *Only the linear part.* Assuming, without proof ("still an open
  problem"), that oscillations show in the $P^1$ part whenever present,
  a cell whose $P^1$ part the limiter leaves unchanged keeps all its
  moments, and otherwise its moments above the first are discarded and
  the limited linear function is kept. The WENO limiter above rebuilds
  those moments instead of discarding them.
* *Required properties and triangles.* Linear functions unchanged, mean
  kept, gradient not increased; on triangles the edge-midpoint deviations
  are limited against 1.5 times a combination of neighbour mean
  differences and rescaled to sum to zero (§3.4.2).

# Citations

1. [Qiu & Shu (2005)](/sources/qiu-2005.md), §§1–4.
2. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §§1, 3.1.
3. [Dumbser & Käser (2007)](/sources/dumbser-2007.md), §6.
4. [Shu (2009)](/sources/shu-2009.md), §5.1.
5. [Shu (2020)](/sources/shu-2020.md), §§3.2.4, 4.3.
6. [Zhang (2017)](/sources/zhang-2017.md), §§1.7, 6.
7. [Balsara (2017)](/sources/balsara-2017-d.md), §VI.
8. [Cockburn & Shu (1998)](/sources/cockburn-1998.md), §§2.3, 3.4.
