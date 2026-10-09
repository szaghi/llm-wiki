---
type: Method
title: "WENO reconstruction (weighted ENO)"
description: "A convex combination of all r ENO candidate reconstructions with nonlinear weights driven by smoothness indicators: order 2r−1 in smooth regions (r+1 in the original Liu–Osher–Chan form), ENO-like near discontinuities, with a smooth flux and no logical branches."
status: established
aliases: [WENO, weighted essentially non-oscillatory, WENO-JS, WENO5]
tags: [weno, reconstruction, shock-capturing, nonlinear-weights]
timestamp: 2026-10-09T00:00:00Z
---

# WENO reconstruction (weighted ENO)

**The idea** ([Liu, Osher & Chan (1994)](/sources/liu-1994.md)). Instead
of picking the smoothest of the $r$ candidate stencils
([ENO](/methods/eno-reconstruction.md)), use all of them: the
reconstruction is $\sum_k \omega_k q_k$ with $\omega_k \ge 0$,
$\sum_k \omega_k = 1$. Near a discontinuity the stencils that cross it
get vanishing weight, which keeps the
[ENO property](/definitions/essentially-non-oscillatory.md); in smooth
regions the convex combination cancels truncation errors and raises the
order.

## Weights

With linear (optimal) weights $d_k$ such that $\sum_k d_k q_k$ is the
value of the $(2r-1)$-point upstream-central scheme, write
$$\hat f_{i+1/2} = \sum_k d_k q_k + \sum_k (\omega_k - d_k)\left(q_k - \mathcal{H}(x_{i+1/2})\right).$$
Since each $q_k - \mathcal{H} = O(h^r)$, order $2r-1$ follows if
$\omega_k = d_k + O(h^{r-1})$ ([Jiang & Shu (1996)](/sources/jiang-1996.md),
eqs. 2.12–2.14; [Shu (1998)](/sources/shu-1998.md), eq. 2.56). The
weights are
$$\tilde\omega_k = \frac{d_k}{(\varepsilon + \beta_k)^q},\qquad \omega_k = \frac{\tilde\omega_k}{\sum_l \tilde\omega_l},$$
and the condition holds if $\beta_k = D\left(1 + O(h^{r-1})\right)$ with
$D$ independent of $k$. A stencil containing a jump has $\beta_k = O(1)$
while smooth ones have $\beta_k = O(h^2)$, so its weight is
$O(h^{2q})$. With more than one smooth candidate, each gets an $O(1)$
weight: WENO does not reproduce ENO's "digital" choice, but uses the
information of every smooth stencil
([Jiang & Shu (1996)](/sources/jiang-1996.md), eq. 2.28).
Shu lists the design requirements: weights that are smooth functions of
the data and cheap (rational, not exponential)
([Shu (1998)](/sources/shu-1998.md), §2.2.2).

**Parameters in this corpus.**

| Source | $q$ | $\varepsilon$ | indicator |
|---|---|---|---|
| [Liu, Osher & Chan (1994)](/sources/liu-1994.md) | $r$ | $10^{-5}$ | undivided differences |
| [Jiang & Shu (1996)](/sources/jiang-1996.md) | 2 | $10^{-6}$ | $L^2$ norms of derivatives |
| [Levy, Puppo & Russo (1999)](/sources/levy-1999.md) | 2 | $10^{-6}$ | Jiang–Shu, central |
| [Balsara & Shu (2000)](/sources/balsara-2000.md) | 2 | $10^{-10}$ | Jiang–Shu, $r = 4$–$7$ |
| [Jiang & Wu (1999)](/sources/jiang-1999.md) | 2 | $10^{-6}$ | Jiang–Shu, $r = 3$, MHD |
| [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md) | 1 (WENO-Z form) | $h^2$ | undivided differences, $r = 2$, MHD |
| [Seo & Ryu (2023)](/sources/seo-2023.md) | 2 | $10^{-8}$ | Jiang–Shu, $r = 3$, MHD |

Jiang and Shu find $q = 2$ adequate for essentially non-oscillatory
results at $r = 2, 3$; Levy et al. find the scheme almost insensitive to
$\varepsilon$, which must only avoid cancellation and so depends on the
magnitude of the solution. Indicators are compared on
[smoothness indicator](/definitions/smoothness-indicator.md).

## The Liu–Osher–Chan scheme (order $r+1$)

A cell-average (finite-volume) scheme with Roe-with-entropy-fix fluxes.
The constants $d_k$ are not the optimal linear weights: they are chosen
per cell, from the sign of $f'(\bar u_j)$, so that the leading error
vanishes at the one interface point that the upwind flux uses. That
gains one order over the base ENO scheme, $r+1$; their tables show
about fourth and fifth order for $r = 2, 3$, "surprisingly" above the
analysis ([Liu, Osher & Chan (1994)](/sources/liu-1994.md), §§3.4, 4).
[Jiang & Shu (1996)](/sources/jiang-1996.md) show the observed order is
superficial: it comes from larger errors on coarse grids, not smaller
errors on fine ones, and with the undivided-difference indicator the
$r = 3$ scheme is fourth order in smooth monotone regions and third order
at critical points. [Levy, Puppo & Russo (1999)](/sources/levy-1999.md)
see the same "super-convergence" and explain it the same way.

## The Jiang–Shu scheme (WENO-JS, order $2r-1$)

A finite-difference flux scheme
([conservative finite difference](/methods/conservative-finite-difference.md)).
For $r = 3$ (fifth order), with $f^+$ values,
$$\begin{aligned}
q_0 &= \tfrac{1}{6}\left(2f_{i-2} - 7f_{i-1} + 11 f_i\right), &
q_1 &= \tfrac{1}{6}\left(-f_{i-1} + 5f_i + 2f_{i+1}\right), &
q_2 &= \tfrac{1}{6}\left(2f_i + 5f_{i+1} - f_{i+2}\right),
\end{aligned}$$
$d = (\tfrac{1}{10}, \tfrac{6}{10}, \tfrac{3}{10})$ (for $r = 2$:
$(\tfrac13, \tfrac23)$), and the indicators of
[smoothness indicator](/definitions/smoothness-indicator.md)
([Jiang & Shu (1996)](/sources/jiang-1996.md), Tables 1–2, eqs. 3.2–3.4).
The $f^-$ part is the mirror image about $x_{i+1/2}$.
* **Convergence.** The flux is $C^\infty$ in its arguments with a smooth
  splitting. Its first variation is a $(2r-2)$-th order central
  difference plus a $(2r-1)$-th order upwind-biased one, whose spectrum
  lies in the left half plane, so by Strang's theorem WENO with an
  $n$-th order RK method ($n \ge \max(r,3)$) converges for smooth
  solutions under a suitable CFL number (Theorem 6.1).
* **Cost.** No logical branches: at least twice as fast as ENO on a
  CRAY C-90, about as fast on serial machines.
* **Accuracy at coarse resolution.** The fourth-order Liu–Osher–Chan
  scheme is slightly more accurate at 20 or fewer points per wavelength;
  WENO5 wins on finer grids ([Shu–Osher problem](/benchmarks/shu-osher-problem.md)).
* **A biasing remedy** for the 2D shock–entropy-wave problem, analogous
  to biased ENO, modifies the weights (their eq. 8.2, with a parameter
  set to 2) so that the optimal weights are used away from the shock and
  the computed ones near it; it also makes the fourth-order scheme fifth
  order in smooth regions.
* WENO smears contacts like ENO; Yang's artificial compression applies
  ([contact sharpening](/methods/contact-sharpening.md)).

## Higher orders and limits

[Balsara & Shu (2000)](/sources/balsara-2000.md) tabulate candidate
coefficients, indicators and optimal weights for $r = 4, 5, 6$ (orders
7, 9, 11; $r = 7$ treated as well). Interpolation costs
$r^3 + 4r^2 + 2r$ operations, yet $r = 5$ runs only 35–50 % slower than
$r = 3$ thanks to cache reuse. Dispersion error falls markedly from
$r = 3$ to $r = 6$. Used alone, the higher-order schemes are not always
monotonicity preserving, and $r = 5$ with RK3 needs CFL near 0.2 to stay
non-oscillatory; the remedy is the Suresh–Huynh bound, giving MPWENO
([monotonicity-preserving limiting](/methods/monotonicity-preserving-limiter.md)).
[Suresh & Huynh (1997)](/sources/suresh-1997.md) note that WENO is still
diffusive, smearing discontinuities nearly as much as ENO.

## The family after WENO-JS

* **Weight design.** [Mapped WENO](/methods/mapped-weno.md) and
  [WENO-Z](/methods/weno-z.md) restore order at critical points and
  lower dissipation; [central-upwind WENO](/methods/central-upwind-weno.md)
  and the [symmetric, bandwidth-optimized WENO](/methods/bandwidth-optimized-weno.md)
  add a downwind stencil; [TENO](/methods/teno.md) replaces smooth weights
  by a 0/1 selection; [adaptive-order WENO](/methods/weno-ao.md) blends one
  large centred polynomial with small ones.
* **Two sources of dissipation:** the linear (optimal) scheme and the
  adaptation ([Martín et al. (2006)](/sources/martin-2006.md)); larger
  weights on discontinuous stencils lower the second
  ([Borges et al. (2008)](/sources/borges-2008.md)); for the same power
  $q$, WENO-JS > WENO-Z > WENO-M in dissipation and larger $q$ is more
  dissipative ([Castro, Costa & Don (2011)](/sources/castro-2011.md)).
* **ε is not innocent:** it is dimensional and, if fixed, decides the
  observed order on fine grids ([Henrick et al. (2005)](/sources/henrick-2005.md));
  values in use range from $10^{-6}$ to $10^{-40}$, or $h^{r-1}$
  ([weight accuracy conditions](/results/weno-weight-accuracy-conditions.md)).
* **Hybrids** switch WENO on only near discontinuities
  ([hybrid compact-WENO](/methods/hybrid-compact-weno.md)).

Accuracy claims at critical points are collected on
[accuracy at critical points](/properties/accuracy-at-critical-points.md).
A centred, staggered variant is [central WENO](/methods/central-weno.md).

**Batch 3 additions.** WENO weights on other approximations:
[compact-reconstruction WENO](/methods/compact-reconstruction-weno.md)
(weights on implicit compact stencils;
[Guo, Xiong & Shi (2014)](/sources/guo-2014.md)) and
[Gaussian-process WENO](/methods/gp-weno.md) (weights on kernel
predictions with RKHS-norm indicators;
[Reyes et al. (2018)](/sources/reyes-2018.md)). WENO *interpolation* of
point values, as opposed to reconstruction from averages, drives the
[alternative finite-difference WENO](/methods/alternative-finite-difference-weno.md);
the two produce polynomials of equal degree with different coefficients
([Balsara et al. (2025)](/sources/balsara-2025.md), §I). For
three-dimensional FV-WENO, dimension-by-dimension sweeps to face Gauss
points need their own linear weights
([finite-volume reconstruction](/methods/finite-volume-reconstruction.md);
[Titarev & Toro (2004)](/sources/titarev-2004.md)). Standard WENO is not
positivity-preserving for Euler; see the
[scaling](/methods/positivity-preserving-scaling-limiter.md) and
[flux](/methods/positivity-preserving-flux-limiter.md) limiters
([Zhang & Shu (2010)](/sources/zhang-2010.md), §1).

**Batch 4 additions.**
* *As a DG limiter.* Finite-volume WENO rebuilds the polynomial of
  troubled DG cells from neighbouring averages
  ([WENO limiters for DG](/methods/weno-limited-dg.md); [Qiu & Shu (2005)](/sources/qiu-2005.md)).
* *Whole polynomials.* Blending full-degree candidates with a dominant
  central linear weight trades optimality for positivity of the linear
  weights on any mesh. It supplies the entire polynomial that one-step
  [ADER](/methods/ader.md) predictors need
  ([polynomial WENO](/methods/polynomial-weno.md); [Dumbser & Käser (2007)](/sources/dumbser-2007.md); [Balsara et al. (2009)](/sources/balsara-2009.md); [Dumbser et al. (2013)](/sources/dumbser-2013.md)).
* *On subgrids.* Third-order ADER-WENO recomputes troubled DG cells in
  the [a posteriori subcell limiter](/methods/a-posteriori-subcell-limiting.md) ([Dumbser et al. (2014)](/sources/dumbser-2014.md)).
* *Energy stability.* A WENO-Z-type fourth-order central scheme in
  summation-by-parts form, plus design-order dissipation, is provably
  $L^2$-stable for linear systems
  ([energy-stable WENO](/methods/energy-stable-weno.md); [Fisher et al. (2011)](/sources/fisher-2011.md)).
* *Near boundaries.* The upwind-biased linear schemes of orders 3–13 are
  WENO with the nonlinear weights turned off. They serve as the
  prototype for the stability analysis of
  [inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md) boundaries ([Li, Shu & Zhang (2016)](/sources/li-2016.md), §2.1).
  WENO-type [weighted extrapolation](/methods/weighted-extrapolation.md)
  fills ghost cells on complex domains ([Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md)).

**Batch 5 additions.**
* *Ideal MHD.* Fifth-order FD-WENO, written as the fourth-order central
  flux minus a nonlinear correction, with characteristic decomposition on
  Brio–Wu normalized eigenvectors, reaches $L^1$ order 4.5–4.8 on smooth
  MHD data. Extrapolated to 3D at equal accuracy, third-order ENO needs
  2.5 times and a second-order scheme 20 times its CPU time. It is
  insensitive to $\varepsilon \in [10^{-7}, 10^{-5}]$, and it needs
  divergence control to stay stable
  ([Jiang & Wu (1999)](/sources/jiang-1999.md), §§2–3;
  [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md);
  [constrained transport](/methods/constrained-transport.md)).
* *Conservation with physical boundaries.* With inverse Lax–Wendroff
  boundaries, the mass that FD-WENO conserves is accurate only to
  second order unless it is redefined with boundary quadrature weights
  ([inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md);
  [Ding, Shu & Zhang (2020)](/sources/ding-2020.md)).

**Batch 6 additions: the reviews.**
* *An approximation procedure.* Shu presents WENO as independent of any
  PDE, in three forms: interpolation of point values, reconstruction from
  cell averages, and approximation of derivatives and integrals
  ([Shu (2009)](/sources/shu-2009.md), §2; [Shu (2020)](/sources/shu-2020.md), §3). The fifth-order interpolation candidates are
  $\tfrac38 u_{i-2} - \tfrac54 u_{i-1} + \tfrac{15}{8}u_i$,
  $-\tfrac18 u_{i-1} + \tfrac34 u_i + \tfrac38 u_{i+1}$ and
  $\tfrac38 u_i + \tfrac34 u_{i+1} - \tfrac18 u_{i+2}$, with linear weights
  $\tfrac1{16}, \tfrac58, \tfrac5{16}$ ([Shu (2009)](/sources/shu-2009.md), eqs. 2.1–2.5;
  [alternative finite-difference WENO](/methods/alternative-finite-difference-weno.md)).
* *Why a discontinuity in every stencil is harmless.* If a jump lies in
  the target interval, every candidate and the big-stencil polynomial are
  monotone there, so their convex combination is too, whatever the
  nonlinear weights ([Shu (2009)](/sources/shu-2009.md), §2.1; [Shu (2020)](/sources/shu-2020.md), §3.1;
  [ENO](/methods/eno-reconstruction.md)).
* *For derivatives*, the indicator sum must start one order higher than
  the derivative approximated. Including the derivative itself is "a
  common mistake", costing accuracy and causing oscillations
  ([Shu (2020)](/sources/shu-2020.md), §3.4.1; [Shu (2009)](/sources/shu-2009.md), §2.3.4). Derivative and integral linear weights
  are often negative ([negative linear weights](/methods/negative-linear-weights.md)).
* *Practice.* Fifth, ninth and thirteenth order "perform better than"
  third, seventh and eleventh, on unpublished experiments. New users should
  start with WENO-JS5, because "the benefits of these modifications and
  improvements are not universal" ([Shu (2020)](/sources/shu-2020.md), §§3.1–3.2). High-order WENO may
  use 3 to 10 times the CPU time of a second-order scheme and still pay
  off ([Shu (2009)](/sources/shu-2009.md), §1).
* *Scale invariance.* With ε a small fraction of the solution's size,
  WENO schemes are self-similar
  ([self-similarity](/properties/self-similarity.md); [Shu (2009)](/sources/shu-2009.md), §3.5.1).
* *Accuracy behind shocks.* For scalar problems full order holds away from
  a discontinuity. For systems, characteristics of other fields cross the
  shock and carry its error downstream: in a quasi-1D nozzle the
  downstream order is about 2 with regular integration, and about 4 with
  subcell integration in the shock cell ([Shu (2009)](/sources/shu-2009.md), §3.5.2, Table 3.1).
* *Open problems* (2009): implicit WENO, whose weights defeat Newton
  iteration near shocks at large steps; tailored weights; 3D unstructured
  WENO; non-polynomial bases; analysis of the unmodified schemes ([Shu (2009)](/sources/shu-2009.md), §7).

**Later uses (batch 7).**
* *A finite-volume recipe.* For modal third-order FV WENO: linear weights
  1, 50 to 400, 1 (left, centre, right), power 4, $\varepsilon = 10^{-12}$, as
  in central WENO; the reconstruction is then only third order. The
  author warns that "it might be safer to not impart too large a weight to
  the central stencil" for extreme astrophysical flows, and claims the
  optimal-weight accuracy gain is "only most effective" for finite
  differences, and that the power should increase with order
  ([Balsara (2017)](/sources/balsara-2017-d.md), §III.1, eqs. 19–29).

# Citations

1. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §§3–4 (read visually; image-only scan).
2. [Jiang & Shu (1996)](/sources/jiang-1996.md), §§2–3, 6–8 (preprint version).
3. [Shu (1998)](/sources/shu-1998.md), §2.2.2, Procedure 2.2.
4. [Balsara & Shu (2000)](/sources/balsara-2000.md), §§I–III.
5. [Levy, Puppo & Russo (1999)](/sources/levy-1999.md), §§3, 5.1.
6. [Suresh & Huynh (1997)](/sources/suresh-1997.md), introduction.
7. [Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md), §4.3.
8. [Martín et al. (2006)](/sources/martin-2006.md), §1.
9. [Borges et al. (2008)](/sources/borges-2008.md), §3.
10. [Castro, Costa & Don (2011)](/sources/castro-2011.md), §5.
11. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.
12. [Reyes et al. (2018)](/sources/reyes-2018.md), §2.5.
13. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §§I, III.
14. [Titarev & Toro (2004)](/sources/titarev-2004.md), §3.
15. [Zhang & Shu (2010)](/sources/zhang-2010.md), §1.
16. [Qiu & Shu (2005)](/sources/qiu-2005.md), §2.
17. [Dumbser & Käser (2007)](/sources/dumbser-2007.md), §2.3.
18. [Balsara et al. (2009)](/sources/balsara-2009.md), §2.
19. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §2.2.
20. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §4.
21. [Fisher et al. (2011)](/sources/fisher-2011.md), §2.
22. [Li, Shu & Zhang (2016)](/sources/li-2016.md), §2.1.
23. [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §4.
24. [Jiang & Wu (1999)](/sources/jiang-1999.md), §§2–3.
25. [Ding, Shu & Zhang (2020)](/sources/ding-2020.md), §1.
26. [Shu (2009)](/sources/shu-2009.md), §§1–3, 7.
27. [Shu (2020)](/sources/shu-2020.md), §§3–4.
28. [Balsara (2017)](/sources/balsara-2017-d.md), §III.1.
