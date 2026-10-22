---
type: Method
title: "WENO-Z weights"
description: "WENO-Z replaces the Jiang–Shu weights by α_k = d_k[1+(τ/(β_k+ε))^q], with a global smoothness indicator τ built from the local β_k; the weights approach the linear ones faster in smooth regions, and the less-smooth stencil keeps more weight than in WENO-JS."
status: established
aliases: [WENO-Z, WENO5-Z, WENO-Z3, WENO7-Z, WENO9-Z, Borges WENO]
tags: [weno, reconstruction, finite-difference]
timestamp: 2026-10-22T20:00:00Z
---

# WENO-Z weights

WENO-Z (Borges et al., with the higher-order extension of Castro et al., as recalled by Li et al.
2022, Luo & Wu 2021 and Fu 2021, who present it with mapped WENO as the fix for the
critical-point defect of WENO-JS) keeps the candidate stencils and linear weights $d_k$ of
[WENO-JS](/methods/weno-js-reconstruction.md) and changes only the unnormalized weights:

$$\alpha_k=d_k\Big[1+\Big(\frac{\tau}{\beta_k+\epsilon}\Big)^q\Big],\qquad
\omega_k=\frac{\alpha_k}{\sum_l\alpha_l},$$

where $\tau$ is a **global smoothness indicator** on the whole $(2r-1)$-point stencil, built from
the local [smoothness indicators](/definitions/smoothness-indicator.md) $\beta_k$. For fifth order
$\tau_5=|\beta_0-\beta_2|$ (Luo & Wu 2021, Eq. (4); Wang & Don 2022, Eqs. (6)–(8)).

## Global indicator and order

For general $r$, Li et al. (2022, Eq. (15)) recall

$$\tau_{2r-1}=\begin{cases}|\beta_0-\beta_{r-1}|, & r\ \text{odd},\\ |\beta_0-\beta_1-\beta_{r-2}+\beta_{r-1}|, & r\ \text{even},\end{cases}$$

where the subscript labels the order $2r-1$ of the scheme; it is not always the power of $\Delta x$
that $\tau$ carries. Because the $\beta_k$ share their leading term, the differences in $\tau$ cancel
it, the ratio $\tau/\beta_k$ vanishes as $\Delta x\to0$ away from critical points, and
$\omega_k\to d_k$ faster than with Jiang–Shu weights. *(Compiler check,
not in the sources: a Taylor expansion of the Jiang–Shu $\beta_k$ for $r=3$ gives
$\beta_0-\beta_2=\big(f'f^{(4)}-\tfrac{13}{3}f''f'''\big)\Delta x^5+O(\Delta x^6)$ up to sign, so
$\tau_5=O(\Delta x^5)$.)* For $r=4$, Li et al. (2022, Eq. (17)) derive
$\tau_7=\big|\tfrac43f'f^{(5)}-\tfrac{13}{3}f''f^{(4)}\big|\Delta x^6+O(\Delta x^8)$, so $\tau_7$ is
$O(\Delta x^6)$ and $\tau_7/\beta_k=O(\Delta x^4)$.

Li et al. (2022, §2) state a structural limit: when the leading term of $\tau_{2r-1}$ has the same
order as that of $\beta_k$, WENO-Z falls back to the convergence rate of the $r$th-order ENO scheme.
This happens at critical points ([critical-point accuracy](/properties/critical-point-accuracy.md)):
their Table 4 shows that WENO7-Z cannot improve the order at a third-order critical point for
either $q=1$ or $q=2$, confirmed numerically by orders 3.55, 3.39, 3.24 (Table 7). At fifth order,
WENO5-Z reaches 5.14–5.37 at a first-order critical point but only 2.11–2.32 at a second-order one
and 1.16–2.11 at a third-order one (Table 6). Fu (2023, §3.1) contrasts TENO's requirement
$\tau_K/(\beta_k+\epsilon)=O(\Delta x^s)$, $s>0$, with WENO-Z's "typical" $\tau_K=O(\Delta x^K)$.

## Parameters

- **Exponent.** Luo & Wu (2021, §2.2) use $q=2$ for fifth order, as do Wang & Don (2022, §2.1);
  Li et al. (2022, §3.2) state instead that $q=1$ is widely used at fifth order (less dissipation)
  and $q=2$ is suggested for higher orders for robustness. These are choices, not a disagreement
  about the scheme.
- **Regularization.** Deng (2023, §4.3) recalls that Borges et al. suggest $\epsilon=10^{-40}$, so
  that $\epsilon$ only excludes vanishing denominators; Luo & Wu (2021) use $10^{-40}$; Wang & Don
  (2022) test $10^{-12}$ and $10^{-40}$.
- **Third order.** In the compact three-cell stencil, $\tau_Z=|\beta_0-\beta_1|$ with exponent 1
  (Deng 2023, Eqs. (4.24)–(4.25); Huang et al. 2026, Eqs. (3.6)–(3.7)).
- **Common template.** Ye et al. (2022, §2.2) write WENO-Z, WENO-CU6 and TENO as instances of
  $\big(C+\tau/(\beta_k+\epsilon)\big)^q$, with $C=1$ for WENO-Z, $C=20$ for
  [WENO-CU6](/methods/weno-cu6.md) and $q=6$ for [TENO](/methods/targeted-eno.md).

## Properties

- **Weight of the less-smooth stencil.** Deng (2023, §1, §4.3) states that WENO-Z assigns a larger
  weight to a stencil containing a discontinuity than WENO-JS, gives sharper solutions than mapped
  WENO and is cheaper than [mapped WENO](/methods/mapped-weno.md); Luo & Wu (2021, §1, §4) note that
  the WENO-Z weight of the less-smooth stencil is still always below its linear weight. This is the
  starting point of [WENO-Z+](/methods/weno-z-plus.md), which pushes that weight above $d_k$.
- **Spectral behaviour.** WENO-Z is a reference curve in the approximate dispersion relations of
  Li et al. (2022, Fig. 2), Fu (2023, Fig. 2) and Luo & Wu (2021, Fig. 3); in each, the newer
  scheme (WENO-ZN, TENO, WENO-Z+M) shows less dissipation than WENO-Z at medium wavenumbers
  ([approximate dispersion relation](/definitions/approximate-dispersion-relation.md)). Luo & Wu
  (2021, Table 1) find WENO-Z and UD5 errors identical on a smooth 2-D density wave
  ($L_1=0.7896\times10^{-13}$ at $641^2$).
- **Scale dependence.** WENO-Z is not scale-invariant: Deng (2023, Fig. 13) shows WENO-Z3 with
  $\epsilon=10^{-40}$ deviating from scale invariance for small scaling factors, and Wang & Don (2022)
  show the classical WENO-Z losing the ENO property on translated data of small amplitude
  ([scale invariance](/properties/scale-invariance.md),
  [affine-invariant WENO](/methods/affine-invariant-weno.md)).
- **High order.** WENO9-Z fails on interacting blast waves at $N_x=401$ and needs CFL 0.1 on double
  Mach reflection; WENO7-Z and WENO9-Z both fail on the forward-facing step at $481\times161$ (Luo &
  Wu 2021, §5.2.5, §5.3.3–5.3.4). Li et al. (2022, Fig. 3) report an asymmetric WENO7-Z solution near
  the square wave of the Jiang–Shu composite profile.

## Z-type weights on other stencil families

The form $d_k\big(1+\tau/(\beta_k+\epsilon)\big)$ is reused far from the classical shifted stencils,
each time with a global indicator built against the largest candidate:

| scheme | global indicator | ratio | source |
|---|---|---|---|
| fifth-order [multi-resolution WENO](/methods/multi-resolution-weno.md), stencils of 1, 3, 5 points | $\tau=\big(\tfrac12(\lvert\beta_3-\beta_1\rvert+\lvert\beta_3-\beta_2\rvert)\big)^2$ | $\tau/(\epsilon+\beta_m)$, $\epsilon=10^{-10}$ | Wang et al. 2021, Eq. (3.17), "same as the popular WENO-Z scheme" |
| sixth-order multi-resolution [HWENO](/methods/hermite-weno.md), four levels | $\tau=\big(\tfrac13\sum_{l\le3}\lvert\beta_4-\beta_l\rvert\big)^2$ | $\tau/(\beta_l+\epsilon)$, $\epsilon=10^{-10}$ | Li, Shu & Qiu 2022, Eqs. (2.21)–(2.22), citing Castro, Costa & Don |
| 2-D WENO-ZQ ([CWENO](/methods/cweno.md)), $\mathbb P^3$ and four $\mathbb P^1$ | $\tau=\big(\tfrac14\sum_{k\le4}\lvert\beta_0-\beta_k\rvert\big)^2$ | $\tau/(\beta_k+\epsilon)$, $\epsilon=10^{-14}$ | Zheng, Cai, Qiu & Qiu 2022, Eqs. (13)–(14) |
| Zhu–Qiu WENO on triangles ([CWENO](/methods/cweno.md)), quadratic and four linear | $\tau^2$ with $\tau=\tfrac14\sum_{\ell\le4}\lvert\beta_0-\beta_\ell\rvert$ (Zhu & Qiu's $\tau$) | $\tau^2/(\beta_\ell+\epsilon)$ (Zhu & Qiu); $\tau^2/(\beta_\ell+\epsilon)^2$, $\epsilon=\lvert K_0\rvert\max\bar u^2$ (Chen & Wu) | Chen & Wu 2022, Eqs. (32)–(34) |
| incremental-stencil interpolation of WCNS-IS | TENO reference indicator $\tau^{\mathrm{ref}}_5$ (page-local; see [smoothness indicators](/definitions/smoothness-indicator.md)) | $\tau^{\mathrm{ref}}_5/(\beta_k+\epsilon)$, times $\tau^{\mathrm{ref}}_5/(\beta_{01}+\epsilon)$ for the two-point stencils | Wong et al. 2021, Eqs. (91)–(93) |
| WENO-AO($\mathcal R$,3) | $\tau=\tfrac13\sum_k\lvert\beta_{\mathrm H}-\beta_k\rvert$ | $\tau^2$, $\tau^3$, $\tau^4$ over $(\beta+\epsilon)^2$ for $\mathcal R=5,7,9$ | Balsara et al. 2024, App. D ([WENO-AO](/methods/weno-ao.md)) |

All the $\tau$ in the table are page-local and none is the registry's $\tau_5$. The same construction,
with the mean of $(\beta_0-\beta_r)^2$ over four small stencils of a six-point stencil, drives the
smooth discontinuity indicator of Zheng, Shu & Qiu (2021, §2.2.4), who cite Zhu & Qiu for it rather
than Borges et al. ([troubled-cell indicators](/definitions/troubled-cell-indicator.md)). For the
incremental stencils, Wong et al. (2021, App. B, Eqs. (B.14), (B.21)) derive
$\tau^{\mathrm{ref}}_5/(\beta_k+\epsilon)=O(\Delta x^4)$ away from critical points and defer the last
step of the fifth-order argument to Borges et al.

*(Compiler check, not in the sources.)* The first three rows square the mean absolute difference and
keep exponent 1 on the ratio, so the ratio is homogeneous of degree 2 in the data: under
$f\mapsto\sigma f$ (page-local $\sigma$) it scales by $\sigma^2$ even with $\epsilon=0$, whereas
$(\tau/(\beta+\epsilon))^q$ with the classical $\tau_5$, the AO(5,3) ratio and the WENO-IS ratio are
of degree 0 when $\epsilon\to0$ (the AO(7,3) and AO(9,3) ratios are of degree 2 and 4). These weights therefore depend on the amplitude of the data beyond the
$\epsilon$ effect discussed under [scale invariance](/properties/scale-invariance.md); none of the
three sources discusses it. Chen & Wu (2022, Remark 3.3) make exactly this argument for the Zhu–Qiu
weights on triangles ($\tau^2$ scales as $\sigma^4$, $\beta_\ell+\epsilon$ as $\sigma^2$ under
$f\mapsto\sigma f$) and restore degree 0 by squaring the denominator and scaling $\epsilon$
with the data; on scaled Riemann problems the original weights oscillate and break the homogeneity of
the solution, the new ones keep it to $10^{-12}$–$10^{-13}$ (Example 4.4).

## Uses in the bundle

WENO-Z is the interpolation of the fifth-order [A-WENO](/methods/alternative-weno.md) schemes of
Wang et al. (2023, §2), applied characteristic-wise, and of Chu, Kurganov & Na (2022, Eqs. (3.4)–(3.7)):
point-value interpolation at $x_{i+1/2}$ with $d=(\tfrac1{16},\tfrac58,\tfrac5{16})$, $q=2$,
$\epsilon=10^{-12}$, and at the quarter points $x_{i\mp1/4}$ of their cell quadrature with the same
indicators, the same $\tau_5$ and $d=(\tfrac{15}{64},\tfrac{21}{32},\tfrac7{64})$ (§4); the comparator
WENO3-Z (the improved third-order version of Don & Borges) and WENO5-Z of Bezgin, Schmidt & Adams
(2022, §3.4–3.5), where WENO3-Z converges at 2.40 on $\sin^3(\pi x)$ and degenerates at its saddle
point like WENO3-JS; the comparator WENO5-Z of Takagi et al. (2022)
and Huang et al. (2026, §6.8); the base of AFWENO-Z in Ye et al. (2022); and the template of the
WENO-AO $\tau$ of Balsara et al. (2024, App. D) ([WENO-AO](/methods/weno-ao.md)). Its descendants
in the bundle are [WENO-Z+ and WENO-Z+M](/methods/weno-z-plus.md),
[WENO-ZN](/methods/weno-zn.md) and the affine-invariant Ai-WENO-Z.

## Qualifications

- Ye et al. (2022, §1) attribute the redesign of the smoothness indicator for WENO-M to Borges et
  al. and the WENO-Z scheme to Castro et al.; their §2.2 then correctly cites WENO-Z to Borges et al.
- Huang et al. (2026, Eq. (3.6)) and Deng (2023, Eq. (4.24)) print the index $k$ inside $\alpha_j$;
  the index is $j$.
- Hiejima (2022, §1) recalls WENO-Z only in passing, as "more accurate than the nonlinear weights
  of JS as a high-order global smoothness indicator"; the WCNS-JS weighting he uses is the Jiang–Shu
  one ([WCNS](/methods/weighted-compact-nonlinear-scheme.md)).
- **Naming.** WENO-ZQ (Zhu & Qiu) shares the Z-type weight form but is a different reconstruction,
  of CWENO type (Zheng, Cai, Qiu & Qiu 2022, §2.2); it is not the WENO-Z of Borges et al.

# Citations

- [Li et al. (2022)](/sources/li-2022-b.md) — §2, Eqs. (14)–(17), Table 4; §3.2; Tables 6–7; Fig. 3.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §1; §2.2, Eq. (4); §4; §5, Table 1.
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §2.1, Eqs. (4)–(8); §3.2.
- [Deng (2023)](/sources/deng-2023.md) — §1; §4.3, Eqs. (4.24)–(4.25); Fig. 13.
- [Huang et al. (2026)](/sources/huang-2026.md) — §3.1, Eqs. (3.6)–(3.7); §6.8.
- [Ye et al. (2022)](/sources/ye-2022.md) — §1; §2.2, Eq. (6).
- [Fu (2023)](/sources/fu-2023.md) — §2.5, Fig. 2; §3.1, Eq. (17).
- [Fu (2021)](/sources/fu-2021.md) — §1.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1; §4 (WENO5-Z comparator).
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §2.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I; App. D.
- [Wang et al. (2021)](/sources/wang-2021.md) — §3.1.1, Step 5, Eq. (3.17).
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — §2.1, Eqs. (2.16)–(2.22).
- [Zheng, Cai, Qiu & Qiu (2022)](/sources/zheng-2022.md) — §2.2, Eqs. (13)–(14).
- [Wong et al. (2021)](/sources/wong-2021.md) — §4.3, Eqs. (91)–(93); App. B, Eqs. (B.14), (B.20)–(B.21).
- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §2.2.4; App. B.
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — §3.2.1, Eqs. (32)–(34), Lemma 3.1, Remark 3.3; Example 4.4.
- [Chu, Kurganov & Na (2022)](/sources/chu-2022.md) — §3, Eqs. (3.4)–(3.7); §4.
- [Bezgin, Schmidt & Adams (2022)](/sources/bezgin-2022.md) — §3.4–3.5, Figs. 2, 4; §4.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §1.
