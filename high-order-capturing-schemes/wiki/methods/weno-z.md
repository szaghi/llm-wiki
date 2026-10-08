---
type: Method
title: "WENO-Z"
description: "Borges–Carmona–Costa–Don weights built from a global higher-order smoothness indicator τ (|β₀ − β₂| at fifth order): closer to the linear weights in smooth regions, larger weights on discontinuous stencils, no mapping cost; extended to all odd orders by Castro–Costa–Don."
status: established
aliases: [WENO-Z, WENO-Z schemes]
tags: [weno, nonlinear-weights, critical-points, dissipation]
timestamp: 2026-10-08T00:00:00Z
---

# WENO-Z

**Weights** ([Borges et al. (2008)](/sources/borges-2008.md)). With the
WENO-JS indicators $\beta_k$ and the global indicator
$\tau_5 = \vert\beta_0 - \beta_2\vert$, whose truncation error is
$\tfrac{13}{3}\vert f' f'''\vert h^5$,
$$\tilde\omega_k = d_k\left(1 + \left(\frac{\tau_5}{\beta_k + \varepsilon}\right)^q\right),\qquad \omega_k = \frac{\tilde\omega_k}{\sum_l \tilde\omega_l}$$
(eq. 42; the original definition is $q = 1$). In smooth regions
$\tau_5 = O(h^5) \ll \beta_k$, so the weights approach $d_k$ fast; where a
jump crosses the whole stencil but not some sub-stencil, $\tau_5 \gg$
those $\beta_k$.

**Order at critical points.** WENO-Z is fourth order at
$n_{\mathrm{cp}} = 1$ ($q = 1$) and fifth with $q = 2$; WENO-JS is third
there and second when $f''$ also vanishes (analysis with a computer
algebra system and 64-digit arithmetic, $\varepsilon = 10^{-40}$,
[Borges et al. (2008)](/sources/borges-2008.md), §4). Larger $q$ makes
the scheme more dissipative at shocks, so the numerical tests use
$q = 1$.

**Why it is sharper.** WENO-M and WENO-Z resolve shock problems better
than WENO-JS, and Borges et al. attribute this not to order at critical
points but to the larger weight they give discontinuous stencils (about
$10^{-4}$ against $10^{-8}$ for WENO-JS in their example), i.e. to
lower dissipation; "contrary to common belief, the strategy should be to
augment the influence of the stencil containing the discontinuity as
much as possible, without destroying the essentially non-oscillatory
behavior". Cost is that of WENO-JS, about 25 % below WENO-M.

**All odd orders** ([Castro, Costa & Don (2011)](/sources/castro-2011.md)).
By symmetry of the Taylor expansions of the $\beta_k$ (Theorem 2),
$$\tau_{2r-1} = \begin{cases}\vert\beta_0 - \beta_{r-1}\vert, & r \text{ odd},\\ \vert\beta_0 - \beta_1 - \beta_{r-2} + \beta_{r-1}\vert, & r \text{ even},\end{cases}$$
is $O(h^{r+2})$, enough for order $2r-1$ in smooth regions; an optimal
linear combination of the $\beta_k$ of higher order exists (Proposition
8, tabulated for $r$ up to 9) and resolves high-order structure better at
$r = 6$. The general weight uses $(\tau_{2r-1}/(\beta_k + \varepsilon))^q$.
* **Critical points:** raising $q$ restores order at critical points for
  WENO-Z only — with $q = r - 1$ the full order returns for
  $n_{\mathrm{cp}} < r - 1$; changing $q$ in WENO-JS or WENO-M does not
  change their rates. Taking $\varepsilon$ of size $h^2$ (they use
  $\varepsilon = h^{r-1}$) acts as an implicit conditional between flat
  and rough regions and recovers the formal order at
  $n_{\mathrm{cp}} = r - 1$.
* **Dissipation hierarchy:** for the same $q$, WENO-JS is the most
  dissipative and WENO-M the least, WENO-Z in between; larger $q$
  increases dissipation for all three. With $q = 1$ none of the three
  advects a square wave without oscillation at eleventh order; with
  $q = 2$ WENO-JS and WENO-Z do, WENO-M does not; with $q = r - 1$ all do.
  On double Mach reflection $q \le 2$ is unstable for WENO-M ($r > 3$)
  and WENO-Z ($r > 4$).
* **A correction:** Remark 12 states that Borges et al. "incorrectly
  stated" that Henrick et al. credited WENO-M's shock results to its
  critical-point order; Henrick et al. made no such causal claim.

**Later uses.** WENO-Z is the base of the
[central-upwind](/methods/central-upwind-weno.md) and
[targeted ENO](/methods/teno.md) weights;
[Fu, Hu & Adams (2016)](/sources/fu-2016.md) note it was suggested to set
$q = 1$ because larger $q$ is too dissipative.
[Zhu & Qiu (2016)](/sources/zhu-2016.md) and
[Balsara, Garain & Shu (2016)](/sources/balsara-2016.md) build their
weights on the same form ([adaptive-order WENO](/methods/weno-ao.md)).
[Rathan & Naga Raju (2017)](/sources/rathan-2017.md) summarize
fifth-order WENO-Z as fourth order at $n_{\mathrm{cp}} = 1$ and second at
higher-order critical points, and compare their $L^1$-type seventh-order
scheme against seventh-order WENO-Z with the Don–Borges $\tau$
([smoothness indicator](/definitions/smoothness-indicator.md)).

**Batch 3.** WENO-Z weights with $q = 2$ and $\tau_5 = \vert\beta_2 - \beta_0\vert$
weight the compact candidate stencils of
[compact-reconstruction WENO](/methods/compact-reconstruction-weno.md),
chosen to avoid accuracy loss at critical points
([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.2). WENO-Z is a
baseline there, less sharp than the compact scheme on the Lax, Sod,
Shu–Osher and blast-wave tests (§3).

# Citations

1. [Borges et al. (2008)](/sources/borges-2008.md), §§2–5 (eqs. 24–27, 42 and Table 1 read from the page images).
2. [Castro, Costa & Don (2011)](/sources/castro-2011.md), §§2–5.
3. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §2.2.
4. [Rathan & Naga Raju (2017)](/sources/rathan-2017.md), §§1, 4.
5. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §§2.2, 3.
