---
type: Definition
title: "Smoothness indicators"
description: "A smoothness indicator β_k is a quadratic functional of the data on candidate stencil S_k, of size O(Δx²) on smooth data and O(1) across a jump; the Jiang–Shu form, a scaled sum of squared derivative L² norms of the candidate polynomial, underlies WENO, TENO and Hermite-WENO weights in the bundle."
status: established
aliases: [smoothness indicator, local smoothness indicator, LSI, IS_k, Jiang–Shu indicator, global smoothness indicator]
tags: [reconstruction, weno, teno]
timestamp: 2026-10-21T12:00:00Z
---

# Smoothness indicators

A smoothness indicator $\beta_k$ measures how far the data on a candidate stencil $S_k$ are from
smooth. It enters the nonlinear weights of [WENO](/methods/weno-js-reconstruction.md) as
$\alpha_k\propto d_k/(\beta_k+\epsilon)^q$ and the scale-separated measure $\gamma_k$ of
[TENO](/methods/targeted-eno.md). Its defining behaviour: on smooth data $\beta_k=O(\Delta x^2)$ (all
$\beta_k$ sharing their leading term), while a stencil crossed by a discontinuity has
$\beta_k=O(1)$, so its weight is driven towards zero (the
[ENO property](/definitions/eno-property.md)).

## Jiang–Shu form

The form used by nearly every source of the bundle is that of Jiang & Shu (Li et al. 2022, Eq. (7);
Wang & Don 2022, Eq. (8); Fu 2023, Eq. (7); Fu 2021, Eq. (12); Takagi et al. 2022, Eq. (9)): with
$\hat f_k(x)$ the degree-$(r_k-1)$ candidate polynomial of $S_k$ on cell $I_i$,

$$\beta_k=\sum_{j=1}^{r_k-1}\Delta x^{2j-1}\int_{x_{i-1/2}}^{x_{i+1/2}}\Big(\frac{d^j\hat f_k}{dx^j}\Big)^2dx .$$

It is a sum of scaled squared $L^2$ norms of all derivatives of the candidate, hence a quadratic form
in the stencil values. For the three-point stencils of fifth-order WENO, in the Jiang–Shu labelling
($S_0$ most upwind; Luo & Wu 2021, Eq. (5)):

$$\begin{aligned}
\beta_0&=\tfrac{13}{12}(f_{i-2}-2f_{i-1}+f_i)^2+\tfrac14(f_{i-2}-4f_{i-1}+3f_i)^2,\\
\beta_1&=\tfrac{13}{12}(f_{i-1}-2f_i+f_{i+1})^2+\tfrac14(f_{i-1}-f_{i+1})^2,\\
\beta_2&=\tfrac{13}{12}(f_i-2f_{i+1}+f_{i+2})^2+\tfrac14(3f_i-4f_{i+1}+f_{i+2})^2 .
\end{aligned}$$

The same three expressions appear in TENO papers under the central-first labelling
(Fu 2021, Eq. (28); Takagi et al. 2022, Eq. (10); Ye et al. 2022, Eq. (5)). On the compact two-point
stencils of third-order WENO they reduce to $\beta_0=(\bar u_{i-1}-\bar u_i)^2$,
$\beta_1=(\bar u_i-\bar u_{i+1})^2$ (Deng 2023, Eq. (4.22); Huang et al. 2026, Eq. (3.4)).

**Wider stencils.** Ye et al. (2022, Eq. (5)) give the four-point indicators of TENO7, e.g. for
$\{i,\dots,i+3\}$

$$\beta=\tfrac1{36}(-11f_i+18f_{i+1}-9f_{i+2}+2f_{i+3})^2+\tfrac{13}{12}(2f_i-5f_{i+1}+4f_{i+2}-f_{i+3})^2+\tfrac{781}{720}(-f_i+3f_{i+1}-3f_{i+2}+f_{i+3})^2 .$$

Fu (2021, Eq. (28)) prints the six-, eight- and ten-point indicators of TENO-AA as rational quadratic
forms (prefactors $1/120960$, $1/62270208000$, $1/8002967132160000$); the six-point one is the
indicator $\beta_6$ that Ye et al. (2022, Eq. (29)) attribute to [WENO-CU6](/methods/weno-cu6.md).
*(Compiler check, not in the sources: the four-point form above and the six-point $\beta_6$ of Ye et
al. were recomputed from the integral definition and agree exactly.)*

**Legendre form.** Li et al. (2022, Eqs. (8)–(11)), after Balsara et al., expand the candidate in
the rescaled Legendre basis $1,\ \xi,\ \xi^2-\tfrac1{12},\ \xi^3-\tfrac3{20}\xi$ on
$[-\tfrac12,\tfrac12]$ with modal coefficients $p^{[l]}_k$; for $r=4$

$$\beta_k=\Big(p^{[1]}_k+\tfrac{1}{10}p^{[3]}_k\Big)^2+\tfrac{13}{3}\big(p^{[2]}_k\big)^2+\tfrac{781}{20}\big(p^{[3]}_k\big)^2 .$$

*(Compiler check: this equals the Jiang–Shu integral exactly.)* Balsara et al. (2024, §I) stress that
indicators written as sums of perfect squares cost few operations, which they credit with improving
the speed and stability of high-order FD-WENO; they extend the closed forms to finite volumes.

**Other forms recalled.** Li et al. (2022, Eq. (6)) recall the earlier Liu–Osher–Chan indicator, a
sum of squared undivided differences of all orders below $r$. Fu (2023, §2.2) notes that improved
indicators developed for WENO can be used in TENO unchanged.

## Behaviour in smooth regions

For $r=4$, Li et al. (2022, Eq. (16)) give
$\beta_k=f'^2\Delta x^2+\tfrac{13}{12}f''^2\Delta x^4+a_kf'f^{(4)}\Delta x^5+\dots$ with $k$-dependent
$a_k$; Ye et al. (2022, Eqs. (25), (30)) give the fifth- and sixth-order expansions. The leading term
is common to all stencils, which is what allows global indicators $\tau$ built from differences of
$\beta_k$ to be of higher order: $\tau_5=|\beta_0-\beta_2|=O(\Delta x^5)$ for
[WENO-Z](/methods/weno-z.md), $\tau_6=\big|\beta_6-\tfrac16(\beta_0+\beta_2+4\beta_1)\big|=O(\Delta x^6)$
for WENO-CU6 and sixth-order TENO (Ye et al. 2022, Eqs. (28), (39), translated here to the Jiang–Shu
labelling). At an $m$th-order
critical point the leading term drops to $O(\Delta x^{2m+2})$, and the ratios $\tau/\beta_k$ that
control the weights lose orders ([critical-point accuracy](/properties/critical-point-accuracy.md);
[WENO-ZN](/methods/weno-zn.md) replaces $\tau$ by an undivided difference for that reason).

Scaling: $\beta_k[\sigma f+\mu]=\sigma^2\beta_k[f]$ for constants $\sigma$, $\mu$ (page-local; Wang
& Don 2022, Eq. (18)). This quadratic scaling against an absolute $\epsilon$ is the source of the
scale dependence of classical weights ([scale invariance](/properties/scale-invariance.md)).

## Indicators on element methods

Kuzmin & Vedral (2023, Eq. (10)) use, for a polynomial $v$ on a finite element $K_e$ in $d$
dimensions, the scaled Sobolev seminorm

$$\|v\|_e=\Big(\sum_{1\le|\mathbf k|\le N}h_e^{2|\mathbf k|-d}\int_{K_e}|D^{\mathbf k}v|^2dx\Big)^{1/2},$$

over all derivatives of order 1 to the polynomial degree $N$ (page-local: multi-indices $\mathbf k$,
local mesh size $h_e$).
Their Hermite-WENO candidates are weighted with $\beta_l=\|u_{h,l}\|_e^{q}$ (page-local seminorm
exponent $q\ge1$, not the weight exponent), generalizing the Jiang–Shu ($q=2$, 1-D) and Friedrich
($q=1$, 2-D) indicators; the same seminorm of the difference
between the finite element solution and its WENO reconstruction defines their smoothness sensor
([Hermite WENO](/methods/hermite-weno.md),
[WENO-stabilized continuous Galerkin](/methods/weno-stabilized-continuous-galerkin.md),
[troubled-cell indicators](/definitions/troubled-cell-indicator.md)). Because only derivatives enter,
the cell-average correction of the candidates does not affect the indicator (Remark 3).

## Qualifications

- Fu (2023, §3.8) recalls Don et al.'s attribution of symmetry breaking in low-dissipation schemes to
  round-off in unstable forms of low-order indicators, and their compact rewriting; Fleischmann et al.
  instead remove floating-point inconsistencies ([symmetry preservation](/properties/symmetry-preservation.md)).
- Deng (2023, Eq. (4.21)) and Huang et al. (2026, Eq. (3.3)) print the two third-order indicators as
  $IS_0$ and $\beta_1$; both are the Jiang–Shu $\beta$ of the two-point stencils.
- Fu (2021, Eq. (11)) uses the indicator without the TENO reference constant,
  $\gamma_k=(\beta_k+\epsilon)^{-q}$ with $q=7$; this is a choice of weight, not of indicator.

# Citations

- [Li et al. (2022)](/sources/li-2022-b.md) — §2, Eqs. (6)–(11), (16), Table 3.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §2.1, Eq. (5).
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §2.1, Eq. (8); §2.3, Eq. (18).
- [Ye et al. (2022)](/sources/ye-2022.md) — §2.1, Eq. (5); §3, Eqs. (18), (25), (28)–(30), (33)–(39).
- [Fu (2021)](/sources/fu-2021.md) — §3.2, Eqs. (11)–(12); §4.2, Eq. (28).
- [Fu (2023)](/sources/fu-2023.md) — §2.2, Eq. (7); §3.8.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §2.2, Eqs. (9)–(10).
- [Deng (2023)](/sources/deng-2023.md) — §4.3, Eqs. (4.21)–(4.22).
- [Huang et al. (2026)](/sources/huang-2026.md) — §3.1, Eqs. (3.3)–(3.4).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I.
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — Eqs. (9)–(10), Remark 1; §5, Eq. (11), Remark 3.
