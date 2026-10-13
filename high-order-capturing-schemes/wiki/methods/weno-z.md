---
type: Method
title: "WENO-Z"
description: "Borges–Carmona–Costa–Don weights built from a global higher-order smoothness indicator τ (|β₀ − β₂| at fifth order): closer to the linear weights in smooth regions, larger weights on discontinuous stencils, no mapping cost; extended to all odd orders by Castro–Costa–Don."
status: established
aliases: [WENO-Z, WENO-Z schemes]
tags: [weno, nonlinear-weights, critical-points, dissipation]
timestamp: 2026-10-13T00:00:00Z
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
  change their rates. Taking $\varepsilon$ of size $h^2$ acts as an
  implicit conditional between flat and rough regions: with
  $\varepsilon = h^2$ and $q = 1$, WENO-Z of orders 5–11 recovers the
  formal order at $n_{\mathrm{cp}} = r - 1$ (Table 5), and "the same
  occurs for WENO-JS and WENO-M (not shown)" (§4). The value
  $\varepsilon = h^{r-1}$ used in almost all their shock tests is a
  separate compromise, chosen to stop a fixed ε from dominating and to
  bound the ratio of the indicators (Remark 13); it is not the value of
  the critical-point table (corrected at the 2026-10-13 deep lint).
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

**Later uses (batch 2).** WENO-Z is the base of the
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

**Later uses (batch 3).** WENO-Z weights with $q = 2$ and $\tau_5 = \vert\beta_2 - \beta_0\vert$
weight the compact candidate stencils of
[compact-reconstruction WENO](/methods/compact-reconstruction-weno.md),
chosen to avoid accuracy loss at critical points
([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.2). WENO-Z is a
baseline there, less sharp than the compact scheme on the Lax, Sod,
Shu–Osher and blast-wave tests (§3).

**Later uses (batch 4).** The energy-stable WENO of Yamaleev and Carpenter uses the
same functional form, $d_k\left(1 + \tau/(\varepsilon + \beta_k)\right)$,
on two-point candidates of a fourth-order central scheme, with $\tau$
the squared third undivided difference. It requires a dimensional
$\varepsilon$ between $O(h^3)$ and $O(h^2)$ for design order at critical
points ([energy-stable WENO](/methods/energy-stable-weno.md); [Fisher et al. (2011)](/sources/fisher-2011.md), §§2.2, 5.2).

**Later uses (batch 6).** WENO-Z ($q = 1$, $\tau_5 = |\beta_0 - \beta_2|$,
$\varepsilon = 10^{-40}$) on characteristic, globally Lax–Friedrichs split
fluxes for GLM-MHD. It costs about 1.45–1.48 times third-order WENO and is
slightly behind MP5 in accuracy and sharpness. The printed $\beta_1$ in
the preprint has a misprint ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md),
§3.2.3). A point-value version with linear weights
$\tfrac1{16}, \tfrac58, \tfrac5{16}$ serves fourth-order finite volume
([Berta et al. (2024)](/sources/berta-2024.md), §3.2). Applied in
characteristic variables with 4-point Gauss–Lobatto nodes, it is the
reconstruction of a provably positive MHD scheme
([Ding & Wu (2024)](/sources/ding-2024.md), §2.2.2).

# Citations

1. [Borges et al. (2008)](/sources/borges-2008.md), §§2–5 (eqs. 24–27, 42 and Table 1 read from the page images).
2. [Castro, Costa & Don (2011)](/sources/castro-2011.md), §§2–5.
3. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §2.2.
4. [Rathan & Naga Raju (2017)](/sources/rathan-2017.md), §§1, 4.
5. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §§2.2, 3.
6. [Fisher et al. (2011)](/sources/fisher-2011.md), §§2.2, 5.2.
7. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §3.2.3 (arXiv v2).
8. [Berta et al. (2024)](/sources/berta-2024.md), §3.2 (arXiv v4).
9. [Ding & Wu (2024)](/sources/ding-2024.md), §2.2.2 (arXiv v1).
10. [Zhu & Qiu (2016)](/sources/zhu-2016.md), §2 (eqs. 2.19–2.20).
11. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §3.1 (eqs. 3.6–3.7).
