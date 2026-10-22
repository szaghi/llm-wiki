---
type: Method
title: "WENO-Z weights"
description: "WENO-Z replaces the Jiang–Shu weights by α_k = d_k[1+(τ/(β_k+ε))^q], with a global smoothness indicator τ built from the local β_k; the weights approach the linear ones faster in smooth regions, and the less-smooth stencil keeps more weight than in WENO-JS."
status: established
aliases: [WENO-Z, WENO5-Z, WENO-Z3, WENO7-Z, WENO9-Z, Borges WENO]
tags: [weno, reconstruction, finite-difference]
timestamp: 2026-10-21T12:00:00Z
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

## Uses in the bundle

WENO-Z is the interpolation of the fifth-order [A-WENO](/methods/alternative-weno.md) schemes of
Wang et al. (2023, §2), applied characteristic-wise; the comparator WENO5-Z of Takagi et al. (2022)
and Huang et al. (2026, §6.8); the base of AFWENO-Z in Ye et al. (2022); and the template of the
WENO-AO $\tau$ of Balsara et al. (2024, App. D) ([WENO-AO](/methods/weno-ao.md)). Its descendants
in the bundle are [WENO-Z+ and WENO-Z+M](/methods/weno-z-plus.md),
[WENO-ZN](/methods/weno-zn.md) and the affine-invariant Ai-WENO-Z.

## Qualifications

- Ye et al. (2022, §1) attribute the redesign of the smoothness indicator for WENO-M to Borges et
  al. and the WENO-Z scheme to Castro et al.; their §2.2 then correctly cites WENO-Z to Borges et al.
- Huang et al. (2026, Eq. (3.6)) and Deng (2023, Eq. (4.24)) print the index $k$ inside $\alpha_j$;
  the index is $j$.

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
