---
type: Result
title: "Accuracy conditions on WENO nonlinear weights"
description: "How close the nonlinear weights must be to the linear weights for a WENO flux difference to keep its design order: Jiang–Shu's sufficient condition, Henrick et al.'s necessary-and-sufficient set (with the condition missing from Jiang–Shu), the simple sufficient condition ω − d = O(h³) at fifth order, and its general form."
status: established
aliases: [WENO order conditions, weight convergence conditions]
tags: [weno, accuracy, nonlinear-weights, critical-points]
timestamp: 2026-10-08T00:00:00Z
---

# Accuracy conditions on WENO nonlinear weights

Write each candidate flux as $q_k = \mathcal{H}(x_{i+1/2}) + A_k h^r + O(h^{r+1})$
and the WENO flux as
$\hat f_{i+1/2} = \sum_k d_k q_k + \sum_k(\omega_k - d_k)\,q_k$
([WENO](/methods/weno.md)). The order of the *difference*
$(\hat f_{i+1/2} - \hat f_{i-1/2})/h$ is what matters.

**Jiang–Shu (sufficient).** $\omega_k = d_k + O(h^{r-1})$ gives order
$2r-1$ for each flux; it follows if $\beta_k = D(1 + O(h^{r-1}))$
([Jiang & Shu (1996)](/sources/jiang-1996.md), eqs. 2.14, 2.17).

**Henrick–Aslam–Powers (fifth order, $r = 3$).** Considering the flux
difference, with superscripts $\pm$ for the weights at $x_{i\pm1/2}$,
fifth order holds if and only if
1. $\sum_k \omega^\pm_k = 1$;
2. $\sum_k A_k(\omega^+_k - \omega^-_k) = O(h^3)$ — explicitly
   $3\omega^+_0 - 3\omega^-_0 - \omega^+_1 + \omega^-_1 + \omega^+_2 - \omega^-_2 = O(h^3)$
   up to ordering;
3. $\omega^\pm_k - d_k = O(h^2)$.

Condition 2 "is not presented" by Jiang and Shu, whose constraints are
therefore incomplete; a simple sufficient condition is
$\omega_k - d_k = O(h^3)$
([Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md), eqs. 25–29;
restated by [Borges et al. (2008)](/sources/borges-2008.md) and
[Castro, Costa & Don (2011)](/sources/castro-2011.md)). WENO-JS weights
satisfy 1 and 3 away from critical points, but at $f' = 0$ only
$\omega_k = d_k + O(h)$ ([accuracy at critical points](/properties/accuracy-at-critical-points.md)).

**General odd order.** $\omega_k - d_k = O(h^r)$ for order $2r-1$, met by
WENO-Z when $\tau_{2r-1} = O(h^{r+2})$ since $\beta_k = O(h^2)$
([Castro et al. (2011)](/sources/castro-2011.md), eqs. 26–27;
[WENO-Z](/methods/weno-z.md)).

**Other forms in this corpus.**
* Sixth-order central-upwind: $\omega_k - d_k = O(h^4)$
  ([Hu, Wang & Adams (2010)](/sources/hu-2010.md), eq. 23).
* WENO-ZQ: $\omega - d = O(h^4)$ from $\tau/(\varepsilon + \beta) = O(h^4)$
  ([Zhu & Qiu (2016)](/sources/zhu-2016.md), eq. 2.21).
* TENO: since a retained stencil carries exactly $d_k$, order is restored
  if every $\chi_k \ge C_T$, i.e. all $\gamma_k$ tend to $C_w$ as
  $h \to 0$, a "much weaker" condition than for WENO
  ([Fu, Hu & Adams (2016)](/sources/fu-2016.md), eq. 29;
  [TENO](/methods/teno.md)).
* Seventh-order $L^1$-indicator weights: an exponent $s$ on the weight
  ratio meets the sufficient condition at $n_{\mathrm{cp}} = 1$ for
  $s \ge 1$ and at $n_{\mathrm{cp}} = 2$ for $s \ge 2$
  ([Rathan & Naga Raju (2017)](/sources/rathan-2017.md), §3).

**Role of ε.** The analyses take $\varepsilon = 0$. With a fixed $\varepsilon$
the weights tend to $d_k$ once $\varepsilon \gg \beta_k$, so the observed
order depends on $\varepsilon$ and the grid in a way that cannot be known a
priori; ε is dimensional
([Henrick et al. (2005)](/sources/henrick-2005.md), §4.3). Castro et al.
use $\varepsilon = h^{r-1}$ and note that $\varepsilon \sim h^2$ separates
flat from rough data like a conditional.

**In the reviews (batch 6).**
* Shu's form of the sufficient condition at fifth order is
  $\omega_k = d_k + O(h^2)$, "when the function u(x) is smooth in the large
  stencil", with weights $O(h^4)$ on a discontinuous stencil ([Shu (2009)](/sources/shu-2009.md), eq. 2.7).
* With unequal stencils whose small members are only second order, the
  weights must sit closer to the linear ones than in classical WENO
  ([Shu (2020)](/sources/shu-2020.md), §3.2.3). The WENO-ZQ condition above is the quantitative form.
* On ε, Shu requires a value relative to the solution's size, with no
  mesh-dependent thresholds ([Shu (2009)](/sources/shu-2009.md), §§3.5.1, 7). That conflicts as a design
  principle with $\varepsilon = h^{r-1}$ and similar choices
  ([self-similarity](/properties/self-similarity.md)).

# Citations

1. [Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md), §§3–4.
2. [Jiang & Shu (1996)](/sources/jiang-1996.md), §2.
3. [Borges et al. (2008)](/sources/borges-2008.md), §2.
4. [Castro, Costa & Don (2011)](/sources/castro-2011.md), §§2–4.
5. [Hu, Wang & Adams (2010)](/sources/hu-2010.md), §2.3.
6. [Zhu & Qiu (2016)](/sources/zhu-2016.md), §2.
7. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §3.1.5.
8. [Rathan & Naga Raju (2017)](/sources/rathan-2017.md), §3.
9. [Shu (2009)](/sources/shu-2009.md), §§2.1, 3.5.1, 7.
10. [Shu (2020)](/sources/shu-2020.md), §3.2.3.
