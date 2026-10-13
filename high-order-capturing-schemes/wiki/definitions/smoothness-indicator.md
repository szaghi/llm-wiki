---
type: Definition
title: "Smoothness indicator"
description: "The per-stencil measure β_k that drives WENO weights: O(h²) on smooth data, O(1) across a jump; its form (undivided differences vs. L² norms of derivatives) decides the achievable order, including at critical points."
status: established
aliases: [smoothness indicator, smoothness measurement, IS_k, beta_k]
tags: [weno, nonlinear-weights]
timestamp: 2026-10-13T00:00:00Z
---

# Smoothness indicator

The quantity $\beta_k$ assigned to candidate stencil $S_k$ in the
[WENO](/methods/weno.md) weights. It must be $O(1)$ when $S_k$ contains a
discontinuity and small when the data on $S_k$ are smooth. Jiang and
Shu's design rule asks the indicators of all smooth stencils to agree to
relative order $h^{r-1}$: each $\beta_k$ equals one common nonzero
quantity, independent of $k$, times $\left(1 + O(h^{r-1})\right)$. This
makes each flux accurate to order $2r-1$ by itself; the order of the flux
*difference* needs Henrick et al.'s further condition
([accuracy conditions on WENO weights](/results/weno-weight-accuracy-conditions.md);
[Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md), §3).

**Undivided differences** ([Liu, Osher & Chan (1994)](/sources/liu-1994.md)):
the sum, over orders $l = 1, \dots, r-1$, of the averaged squares of the
$l$-th undivided differences on the stencil. For $r = 2$ it is
$(\bar u_j - \bar u_{j-1})^2$. Squares were Shu's suggestion; the
original absolute values work too but give a merely Lipschitz flux
(acknowledgement of the paper). This indicator is $O(h^2)$ on smooth
data but its leading term differs between stencils at $O(h)$ relative
size, so for $r = 3$ it gives fourth order in smooth monotone regions
and third order at critical points
([Jiang & Shu (1996)](/sources/jiang-1996.md), §2).

**$L^2$ norms of derivatives** ([Jiang & Shu (1996)](/sources/jiang-1996.md), eq. 3.1):
$$\beta_k = \sum_{l=1}^{r-1}\int_{x_{i-1/2}}^{x_{i+1/2}} h^{2l-1}\left(\frac{d^l p_k}{dx^l}\right)^2 dx,$$
"emulating the idea of minimizing the total variation"; the factor
$h^{2l-1}$ removes the $h$-dependence, which keeps the scheme
self-similar. For $r = 2$ it coincides with the Liu–Osher–Chan
indicator. Shu's lecture notes give the same integral with the explicit
$r = 2$ and $r = 3$ formulas, and call it "similar to but smoother than"
a total-variation measure based on the $L^1$ norm
([Shu (1998)](/sources/shu-1998.md), eqs. 2.61–2.63). For $r = 3$, in flux values,
$$\begin{aligned}
\beta_0 &= \tfrac{13}{12}\left(f_{i-2} - 2f_{i-1} + f_i\right)^2 + \tfrac14\left(f_{i-2} - 4f_{i-1} + 3f_i\right)^2,\\
\beta_1 &= \tfrac{13}{12}\left(f_{i-1} - 2f_i + f_{i+1}\right)^2 + \tfrac14\left(f_{i-1} - f_{i+1}\right)^2,\\
\beta_2 &= \tfrac{13}{12}\left(f_i - 2f_{i+1} + f_{i+2}\right)^2 + \tfrac14\left(3f_i - 4f_{i+1} + f_{i+2}\right)^2 .
\end{aligned}$$
Where $f' \neq 0$, $\beta_k = (f'h)^2(1 + O(h^2))$, which gives fifth
order. Jiang and Shu also state that at critical points
$\beta_k = \tfrac{13}{12}(f''h^2)^2(1 + O(h^2))$ and conclude that the
weights are fifth-order accurate there too (eq. 3.9). That expansion is
wrong: $\beta_0$ and $\beta_2$ differ at $O(h^5)$ when $f' = 0$, so the
relative agreement is only $O(h)$ and WENO5 is third order there
([Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md);
[accuracy at critical points](/properties/accuracy-at-critical-points.md)).
[Balsara & Shu (2000)](/sources/balsara-2000.md) tabulate the indicators
for $r = 4, 5, 6$ as quadratic forms in the stencil values.
[Levy, Puppo & Russo (1999)](/sources/levy-1999.md) use the same
integral for their central parabolas, with the remark that the
indicators are $O(h^2)$ in smooth regions and $O(h^4)$ at critical
points.

**Global (reference) indicators.** Later weights compare each $\beta_k$
with a higher-order combination over the whole stencil:
$\tau_5 = \vert\beta_0 - \beta_2\vert = O(h^5)$
([Borges et al. (2008)](/sources/borges-2008.md)); $\tau_{2r-1}$ for all
odd orders and an optimal higher-order combination
([Castro, Costa & Don (2011)](/sources/castro-2011.md)); $\tau_6$ from the
six-point indicator ([Hu, Wang & Adams (2010)](/sources/hu-2010.md));
averages of $\vert\beta_P - \beta_k\vert$ between a large central
polynomial and small ones ([Zhu & Qiu (2016)](/sources/zhu-2016.md);
[Balsara, Garain & Shu (2016)](/sources/balsara-2016.md)). See
[WENO-Z](/methods/weno-z.md), [central-upwind WENO](/methods/central-upwind-weno.md),
[TENO](/methods/teno.md), [adaptive-order WENO](/methods/weno-ao.md).

**Other local forms.**
* In a Legendre basis the Jiang–Shu indicator is a sum of perfect squares
  of the polynomial's moments, the same expression for every stencil of a
  given $r$ and nested across $r$ ($r = 3$–$9$), which is both cheaper and
  evidently positive ([Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §2).
* $L^1$-type indicators: weighted absolute values of generalized undivided
  differences, each a fourth-order approximation of a scaled derivative at
  $x_{i+1/2}$, with balancing parameters, for a seventh-order scheme
  ([Rathan & Naga Raju (2017)](/sources/rathan-2017.md); after Ha et al.).

**For systems** the indicator can be computed per characteristic field
(standard), from pressure and entropy (Jiang–Shu "PS"), or as one global
indicator shared by all components
([characteristic decomposition](/methods/characteristic-decomposition.md)).

**Batch 3.** For pointwise WENO *interpolation*, the Legendre-basis
indicators are the same sums of perfect squares as for reconstruction
([Balsara et al. (2025)](/sources/balsara-2025.md), §III). Gaussian-process
WENO replaces derivative norms by the squared norm of the sub-stencil
point values in the reproducing-kernel Hilbert space of the covariance
kernel, $\beta_k = \sum_i \left(c^{(k)}_i\right)^2/\mu^{(k)}_i$ over the kernel
matrix's eigenpairs. It equals, up to a constant, minus twice the log
likelihood of the data, and no Taylor-expansion accuracy proof is given
([Reyes et al. (2018)](/sources/reyes-2018.md), §2.5;
[GP-WENO](/methods/gp-weno.md)).

**Modal, reference-element and boundary forms (batch 4).**
* In the scaled Legendre basis the third-order indicator is
  $\beta = \left(\hat u^{(1)}\right)^2 + \tfrac{13}{3}\left(\hat u^{(2)}\right)^2$,
  and the fourth-order one is
  $\left(\hat u^{(1)} + \hat u^{(3)}/10\right)^2 + \tfrac{13}{3}\left(\hat u^{(2)}\right)^2 + \tfrac{781}{20}\left(\hat u^{(3)}\right)^2$.
  Both are sums of squares, so their positivity is evident
  ([Balsara et al. (2009)](/sources/balsara-2009.md), eqs. 9, 15; [polynomial WENO](/methods/polynomial-weno.md)).
  This is the same structure Balsara, Garain and Shu exploit.
* On unstructured meshes, integrating the squared derivatives over the
  *reference* element removes the cell size. The indicator becomes
  $\beta_k = \hat{\mathbf u}_k^{\mathsf T}\mathsf B\,\hat{\mathbf u}_k$ of the reconstructed coefficients,
  with one universal matrix $\mathsf B$ that depends only on the basis
  ([Dumbser & Käser (2007)](/sources/dumbser-2007.md), eqs. 23–25).
* Two-point candidates use squared first differences,
  $\beta_k = (f_{j+1} - f_j)^2$ and its shifts, together with
  $\tau = (\Delta^3 f_{j-1})^2$ ([energy-stable WENO](/methods/energy-stable-weno.md); [Fisher et al. (2011)](/sources/fisher-2011.md)).
* For boundary *extrapolation* the Jiang–Shu integral is taken over the
  whole stencil, not one cell. Ratios of such indicators, rather than
  their absolute size, set dimensionless weights
  ([weighted extrapolation](/methods/weighted-extrapolation.md); [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §4).

**In the reviews (batch 6).**
* Shu calls the indicator "a scaled sum of the square $L^2$ norms of all
  the derivatives", and later prefers "roughness indicator". The scaling
  makes it independent of $h$ on uniform meshes, and on non-uniform meshes
  dependent only on mesh-size ratios ([Shu (2009)](/sources/shu-2009.md), eq. 2.8; [Shu (2020)](/sources/shu-2020.md), §3.1).
* *For point-value interpolation* the fifth-order indicators are quadratic
  forms such as
  $\beta_1 = \tfrac13\left(4u_{i-2}^2 - 19u_{i-2}u_{i-1} + 25u_{i-1}^2 + 11u_{i-2}u_i - 31u_{i-1}u_i + 10u_i^2\right)$
  ([Shu (2009)](/sources/shu-2009.md), eq. 2.9, read from the page image).
* *For an $l$-th derivative*, the sum must start at derivative order
  $l + 1$ ([Shu (2020)](/sources/shu-2020.md), §3.4.1).
* A Zhang–Shu indicator improves steady-state convergence ([Shu (2009)](/sources/shu-2009.md), §2.3.5).

# Citations

1. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §3.2 and acknowledgement.
2. [Jiang & Shu (1996)](/sources/jiang-1996.md), §§2–3 (eqs. 3.1–3.9 read from the page images).
3. [Shu (1998)](/sources/shu-1998.md), eqs. 2.61–2.63.
4. [Levy, Puppo & Russo (1999)](/sources/levy-1999.md), eqs. 3.13–3.15.
5. [Balsara & Shu (2000)](/sources/balsara-2000.md), §III.
6. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §III.
7. [Reyes et al. (2018)](/sources/reyes-2018.md), §2.5.
8. [Balsara et al. (2009)](/sources/balsara-2009.md), §2 (eqs. 9 and 15 read from the page image).
9. [Dumbser & Käser (2007)](/sources/dumbser-2007.md), §2.3 (eqs. 23–25 read from the page image).
10. [Fisher et al. (2011)](/sources/fisher-2011.md), eq. 19.
11. [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §4.
12. [Shu (2009)](/sources/shu-2009.md), §§2.1, 2.3.5.
13. [Shu (2020)](/sources/shu-2020.md), §§3.1, 3.4.1.
14. [Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md), §§2–3.
15. [Borges et al. (2008)](/sources/borges-2008.md), §3 (eqs. 25–28).
16. [Castro, Costa & Don (2011)](/sources/castro-2011.md), §3 (Theorem 2).
17. [Hu, Wang & Adams (2010)](/sources/hu-2010.md), eqs. 24–27.
18. [Zhu & Qiu (2016)](/sources/zhu-2016.md), §2 (eqs. 2.11–2.16).
19. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §2.
20. [Rathan & Naga Raju (2017)](/sources/rathan-2017.md), §3.
