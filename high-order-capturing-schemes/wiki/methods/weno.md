---
type: Method
title: "WENO reconstruction (weighted ENO)"
description: "A convex combination of all r ENO candidate reconstructions with nonlinear weights driven by smoothness indicators: order 2r−1 in smooth regions (r+1 in the original Liu–Osher–Chan form), ENO-like near discontinuities, with a smooth flux and no logical branches."
status: established
aliases: [WENO, weighted essentially non-oscillatory, WENO-JS, WENO5]
tags: [weno, reconstruction, shock-capturing, nonlinear-weights]
timestamp: 2026-10-08T00:00:00Z
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
