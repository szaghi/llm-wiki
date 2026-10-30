---
type: Method
title: "WENO-Z weights"
description: "WENO-Z replaces the Jiang–Shu weights by α_k = d_k[1+(τ/(β_k+ε))^q], with a global smoothness indicator τ built from the local β_k; the weights approach the linear ones faster in smooth regions, and the less-smooth stencil keeps more weight than in WENO-JS."
status: established
aliases: [WENO-Z, WENO5-Z, WENO-Z3, WENO7-Z, WENO9-Z, WENO-Z5, WENO-Z7, Borges WENO]
tags: [weno, reconstruction, finite-difference]
timestamp: 2026-10-30T08:09:00Z
---

# WENO-Z weights

WENO-Z was introduced by [Borges et al. (2008)](/sources/borges-2008.md) for the fifth-order
finite-difference scheme; the arbitrary-order extension is Castro et al.'s, as recalled by Li et al.
(2022b), and Borges et al. (§6) only announce it as "currently underway". Li et al. (2022b), Luo & Wu
(2021) and Fu (2021) present it with mapped WENO as the fix for the critical-point defect of
WENO-JS; Borges et al. themselves credit its gains on shock problems to the weight it leaves on
discontinuous stencils rather than to its order at critical points (Remark 1; see *Properties*). It
keeps the candidate stencils, linear weights $d_k$ and indicators of
[WENO-JS](/methods/weno-js-reconstruction.md) and changes only the unnormalized weights:

$$\alpha_k=d_k\Big[1+\Big(\frac{\tau}{\beta_k+\epsilon}\Big)^q\Big],\qquad
\omega_k=\frac{\alpha_k}{\sum_l\alpha_l},$$

where $\tau$ is a **global smoothness indicator** on the whole $(2r-1)$-point stencil, built from
the local [smoothness indicators](/definitions/smoothness-indicator.md) $\beta_k$. For fifth order
$\tau_5=|\beta_0-\beta_2|$ (Borges et al. 2008, Eq. (25); Luo & Wu 2021, Eq. (4); Wang & Don 2022,
Eqs. (6)–(8)). Borges et al. first write the weights with $q=1$ through normalized indicators,
$\alpha_k=d_k(\beta_k+\tau_5+\epsilon)/(\beta_k+\epsilon)$ (Eqs. (27)–(28)), and generalize to the exponent
$q$ in §4 (Eq. (42)). They list the properties of $\tau_5$: $O(\Delta x^5)\ll\beta_k$ on a smooth five-point
stencil; $\beta_k\ll\tau_5$ for the smooth candidates when the full stencil contains a discontinuity;
$\tau_5\le\max_k\beta_k$ (§3).

## Global indicator and order

For general $r$, Li et al. (2022b, Eq. (15)) recall

$$\tau_{2r-1}=\begin{cases}|\beta_0-\beta_{r-1}|, & r\ \text{odd},\\ |\beta_0-\beta_1-\beta_{r-2}+\beta_{r-1}|, & r\ \text{even},\end{cases}$$

where the subscript labels the order $2r-1$ of the scheme; it is not always the power of $\Delta x$
that $\tau$ carries. Because the $\beta_k$ share their leading term, the differences in $\tau$ cancel
it, the ratio $\tau/\beta_k$ vanishes as $\Delta x\to0$ away from critical points, and
$\omega_k\to d_k$ faster than with Jiang–Shu weights: with $\epsilon=0$, $\omega_k=d_k+O(\Delta x^3)$ away
from critical points, the sufficient condition for fifth order (Borges et al. 2008, §3, Eq. (29)).
*(Compiler check, not in the sources: the expansions of Borges et al. (Eqs. (12), (14)) give
$\beta_0-\beta_2=\big(f'f^{(4)}-\tfrac{13}{3}f''f'''\big)\Delta x^5+O(\Delta x^6)$ up to sign, so
$\tau_5=O(\Delta x^5)$; their Eq. (26) prints only the $\tfrac{13}3|f''f'''|$ term.)* For $r=4$, Li et al. (2022b, Eq. (17)) derive
$\tau_7=\big|\tfrac43f'f^{(5)}-\tfrac{13}{3}f''f^{(4)}\big|\Delta x^6+O(\Delta x^8)$, so $\tau_7$ is
$O(\Delta x^6)$ and $\tau_7/\beta_k=O(\Delta x^4)$.

**Order at critical points (founding analysis).** Borges et al. (2008, §4, Eqs. (32)–(41), Tables 1–2)
write the order as $\min(5,s_1+2,s_2+3)$, with $\sum_k\mathsf a_k(\omega^+_k-\omega^-_k)=O(\Delta x^{s_1})$ and
$\omega^\pm_k-d_k=O(\Delta x^{s_2})$ (page-local $\mathsf a_k$, $s_1$, $s_2$), and find with a symbolic algebra
program order 5, 4 and 2 at critical points of order $0$, $1$ and $\ge2$ for $q=1$; with $q=2$ the order is
5 at a first-order critical point. Their test on $x^3+\cos x$ at $x=0$, $\epsilon=10^{-40}$, in 64-digit
arithmetic, gives orders 3.93–3.99 for $q=1$ and 4.80–4.98 for $q=2$, against 2.95–2.99 for WENO-JS
(Table 3). Raising $q$ brings the scheme closer to the linear one in smooth regions but lowers the
relative weight of a discontinuous stencil, "making the scheme more dissipative", so all their runs use
$q=1$ (§4–5).

Li et al. (2022b, §2) state a structural limit: when the leading term of $\tau_{2r-1}$ has the same
order as that of $\beta_k$, WENO-Z falls back to the convergence rate of the $r$th-order ENO scheme.
This happens at critical points ([critical-point accuracy](/properties/critical-point-accuracy.md)):
their Table 4 shows that WENO7-Z cannot improve the order at a third-order critical point for
either $q=1$ or $q=2$, confirmed numerically by orders 3.55, 3.39, 3.24 (Table 7). At fifth order,
WENO5-Z reaches 5.14–5.37 at a first-order critical point but only 2.11–2.32 at a second-order one
and 1.16–2.11 at a third-order one (Table 6). Fu (2023, §3.1) contrasts TENO's requirement
$\tau_K/(\beta_k+\epsilon)=O(\Delta x^s)$, $s>0$, with WENO-Z's "typical" $\tau_K=O(\Delta x^K)$.

## Parameters

- **Exponent.** Borges et al. (2008) use $q=1$ in all experiments and introduce $q=2$ only as the
  remedy at first-order critical points (§4); Fu et al. (2016, §2.2) recall that $q=1$ was suggested
  "as a larger value of $q$ results in a too dissipative scheme in non-smooth regions". Luo & Wu (2021, §2.2) use $q=2$ for fifth order, as do Wang & Don (2022, §2.1);
  Li et al. (2022b, §3.2) state instead that $q=1$ is widely used at fifth order (less dissipation)
  and $q=2$ is suggested for higher orders for robustness. These are choices, not a disagreement
  about the scheme.
- **Regularization.** Borges et al. (2008, Remark 2, §5) reject the $10^{-6}$ "commonly suggested in the
  literature", which dominates $\beta_k$, and use $\epsilon=10^{-40}$ for WENO-Z and mapped WENO "to force this
  parameter to play only its original role of not allowing vanishing denominators" ($10^{-6}$ for their
  WENO-JS runs); Deng (2023, §4.3) recalls the same suggestion; Luo & Wu (2021) use $10^{-40}$; Wang & Don
  (2022) test $10^{-12}$ and $10^{-40}$.
  De Vanna et al. (2023a, §3.1) and De Vanna et al. (2023b, §3.1), in the arbitrary-order WENO-Z of
  Castro et al. at orders 3, 5 and 7, set $\epsilon=10^{-12}$ to limit the dissipation ("to reduce the dissipation", 2023a).
- **WCNS interpolation.** Chen & Deng (2023, Eqs. (17)–(18)) run WCNS-Z with $q=2$ and
  $\epsilon=10^{-40}$, "as suggested" by Borges et al. to avoid division by zero only, and reuse $\tau_5$
  inside the stencil-local exponent of their [exponential weights](/methods/exponential-nonlinear-weights.md).
  Zhong et al. (2023, Eq. (10)) recall WENO-Z with exponent 2 and $\epsilon=10^{-40}$ for all their
  schemes; on $\sin^3(\pi x)$ it falls to $L_2$ order about 3 ([accuracy at critical points](/properties/critical-point-accuracy.md)).
- **Third order.** In the compact three-cell stencil, $\tau_Z=|\beta_0-\beta_1|$ with exponent 1
  (Deng 2023, Eqs. (4.24)–(4.25); Huang et al. 2026, Eqs. (3.6)–(3.7)).
- **Common template.** Ye et al. (2022, §2.2) write WENO-Z, WENO-CU6 and TENO as instances of
  $\big(C+\tau/(\beta_k+\epsilon)\big)^q$, with $C=1$ for WENO-Z, $C=20$ for
  [WENO-CU6](/methods/weno-cu6.md) and $q=6$ for [TENO](/methods/targeted-eno.md). Zhou et al. (2023,
  Eq. (14)) use the same template with a free, adapted $C$ (between $2\times10^8$ and $2\times10^{10}$) and
  the six-point $\tau_6$ in a WCNS after Wong & Lele ([WCNS](/methods/weighted-compact-nonlinear-scheme.md)).

## Properties

- **Weight of the less-smooth stencil.** Borges et al. (2008, §3, Eq. (31), Fig. 3) show that a
  discontinuity in one candidate raises that candidate's weight relative to WENO-JS: next to the jump of
  a piecewise sine, WENO-JS gives the discontinuous stencils weights "around $10^{-8}$", mapped WENO a
  small increase and WENO-Z about $10^{-4}$. Their Remark 1 credits the shock results of WENO-Z and mapped
  WENO to this "smaller dissipation", "distinctly from" Henrick et al., who credited the critical-point
  order. On shock tubes, the Shu–Osher problem and blast waves WENO-Z is equivalent to or slightly sharper
  than mapped WENO and better than WENO-JS at $N=200$–$800$ (§5.2, Figs. 6–10); on the Jiang–Shu composite
  advection at $N=1600$, $t=8$, the $L_1$ errors are $7.73\times10^{-3}$ (Z), $8.06\times10^{-3}$ (mapped) and
  $9.93\times10^{-3}$ (JS) (Table 4; [composite advection](/benchmarks/jiang-shu-composite-advection.md)).
  Deng (2023, §1, §4.3) states that WENO-Z assigns a larger
  weight to a stencil containing a discontinuity than WENO-JS, gives sharper solutions than mapped
  WENO and is cheaper than [mapped WENO](/methods/mapped-weno.md); Luo & Wu (2021, §1, §4) note that
  the WENO-Z weight of the less-smooth stencil is still always below its linear weight. This is the
  starting point of [WENO-Z+](/methods/weno-z-plus.md), which pushes that weight above $d_k$.
- **Spectral behaviour.** WENO-Z is a reference curve in the approximate dispersion relations of
  Li et al. (2022b, Fig. 2), Fu (2023, Fig. 2) and Luo & Wu (2021, Fig. 3); in each, the newer
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
  Wu 2021, §5.2.5, §5.3.3–5.3.4). Li et al. (2022b, Fig. 3) report an asymmetric WENO7-Z solution near
  the square wave of the Jiang–Shu composite profile.
- **Seventh order as a reference.** Zhang, Jiang, Qin, Qu & Yan (2024b, Eq. (9), §5) run WENO7-Z with $q=2$ and
  $\epsilon=10^{-40}$ against sixth-order TENO variants: seventh order on smooth advection ($L_1=3.40\times10^{-17}$ at
  $N_x=1600$; Table 2), rates 7, 7, 6, 3, 4, 5, 6 at critical points of order 0–6 (Table 3), ADR resolved
  bandwidths 1.330 and 1.418 at 1 % and 1.5 % dispersion error, above every six-point scheme except their TENO6-SA
  (1.767 and 1.774) and, at 1.5 %, TENO6-A (1.590), with larger dissipation "due to the upwind mechanism" (§5.2, Fig. 5), the smallest errors of all
  compared schemes on a long-time 2-D Gaussian advection ($L_1=4.10\times10^{-5}$ against $9.34\times10^{-5}$ for
  TENO6-SA; Table 4), and the lowest cost, "as it avoids calculating the complex $\tau_6$" (§5.3). They use WENO7-Z
  on $500^3$ and $512^3$ grids as the reference for their Taylor–Green and isotropic-turbulence runs (§6.4;
  [scale sensors](/definitions/scale-sensor.md), [critical-point accuracy](/properties/critical-point-accuracy.md)).

## Z-type weights on other stencil families

The form $d_k\big(1+\tau/(\beta_k+\epsilon)\big)$ is reused far from the classical shifted stencils,
each time with a global indicator built against the largest candidate:

| scheme | global indicator | ratio | source |
|---|---|---|---|
| fifth-order [multi-resolution WENO](/methods/multi-resolution-weno.md), stencils of 1, 3, 5 points | $\tau=\big(\tfrac12(\lvert\beta_3-\beta_1\rvert+\lvert\beta_3-\beta_2\rvert)\big)^2$ | $\tau/(\epsilon+\beta_m)$, $\epsilon=10^{-10}$ | Wang et al. 2021, Eq. (3.17), "same as the popular WENO-Z scheme" |
| sixth-order multi-resolution [HWENO](/methods/hermite-weno.md), four levels | $\tau=\big(\tfrac13\sum_{l\le3}\lvert\beta_4-\beta_l\rvert\big)^2$ | $\tau/(\beta_l+\epsilon)$, $\epsilon=10^{-10}$ | Li, Shu & Qiu 2022d, Eqs. (2.21)–(2.22), citing Castro, Costa & Don |
| 2-D WENO-ZQ ([CWENO](/methods/cweno.md)), $\mathbb P^3$ and four $\mathbb P^1$ | $\tau=\big(\tfrac14\sum_{k\le4}\lvert\beta_0-\beta_k\rvert\big)^2$ | $\tau/(\beta_k+\epsilon)$, $\epsilon=10^{-14}$ | Zheng, Cai, Qiu & Qiu 2022, Eqs. (13)–(14) |
| Zhu–Qiu WENO on triangles ([CWENO](/methods/cweno.md)), quadratic and four linear | $\tau^2$ with $\tau=\tfrac14\sum_{\ell\le4}\lvert\beta_0-\beta_\ell\rvert$ (Zhu & Qiu's $\tau$) | $\tau^2/(\beta_\ell+\epsilon)$ (Zhu & Qiu); $\tau^2/(\beta_\ell+\epsilon)^2$, $\epsilon=\lvert K_0\rvert\max\bar u^2$ (Chen & Wu) | Chen & Wu 2022, Eqs. (32)–(34) |
| [incremental-stencil](/methods/incremental-stencil-weno.md) interpolation of WCNS-IS (also WENO5IS) | TENO reference indicator $\tau^{\mathrm{ref}}_5$ (page-local; see [smoothness indicators](/definitions/smoothness-indicator.md)) | $\tau^{\mathrm{ref}}_5/(\beta_k+\epsilon)$, times $\tau^{\mathrm{ref}}_5/(\beta_{01}+\epsilon)$ for the two-point stencils | Wong et al. 2021, Eqs. (91)–(93) |
| WENO-AO($\mathcal R$,3) | $\tau=\tfrac13\sum_k\lvert\beta_{\mathrm H}-\beta_k\rvert$ | $\tau^2$, $\tau^3$, $\tau^4$ over $(\beta+\epsilon)^2$ for $\mathcal R=5,7,9$ | Balsara et al. 2024, App. D ([WENO-AO](/methods/weno-ao.md)) |
| WCNS-MR interpolation of Qin et al. ([shock-capturing boundary closure](/methods/shock-capturing-boundary-closure.md)), indicators with scaled derivative sums | as in the first row | $\tau/(\beta_m+\epsilon)$, $\epsilon=10^{-10}$ | Qin, Chen, Lin & Deng 2023, Eqs. (11)–(14) |
| MR-AWENO interpolation ([multi-resolution WENO](/methods/multi-resolution-weno.md)) | as in the first row | $\tau/(\beta_k+\epsilon)$, $\epsilon=10^{-6}$ | Li, Li, Don & Wang 2023a, Eqs. (23)–(24), recalling Wang, Zhu, Yang & Zhao |
| MR-AWENO-Si | squared fifth undivided difference $\tau^*$ on six points | $\tau^*/(\beta_k+\epsilon\mathsf m^2)$, descaler $\mathsf m$ | Li, Li, Don & Wang 2023a, Eqs. (42)–(44) |
| WENO-G ([RBF-based WENO](/methods/rbf-weno.md)) | $\lvert\nabla^4f\rvert^2$, an exponential-moment fourth difference | $(\tau/(\beta_k+\epsilon))^q$, $q=1$ (2 on blast waves), RBF ideal weights | Jeong, Yang & Yoon 2022, Eqs. (37)–(39) |
| WENO-H non-smooth region ([hybrid schemes](/methods/hybrid-weno.md)) | as in the CWENOZ/WENO-ZQ rows, five-point | $\tau/\big((\epsilon+\beta_k)C_R\big)$, data- and grid-dependent $C_R$ | Wan & Xia 2022, Eqs. (3.1)–(3.4) |
| MR-WCNS interpolation ([multi-resolution WENO](/methods/multi-resolution-weno.md)) | as in the first row | $\tau/(\epsilon+\beta_n)$, $\epsilon=10^{-6}$ | Wang, Zhu, Wang & Zhao 2023c, Eq. (3.23) |
| third-order two-level WENO on moving quadrilaterals | $\lvert\beta_2-\beta_1\rvert$ | $(\tau/(\beta_l+\epsilon))^2$, $\epsilon=10^{-3}$ | Gu, Li, Cheng & Shu 2023, §2.4, after Castro, Costa & Don |
| unstructured CWENOZ ([CWENO](/methods/cweno.md)) | $\big(\tfrac1{s_t-1}\sum_{s\ge1}\lvert\beta_s-\beta_0\rvert\big)^4$ | $\tau/(\epsilon+\beta_s)$, $\epsilon=10^{-14}$ | Maltsev et al. 2023, Eqs. (22)–(23) |
| IMWENO-P ([smoothness indicators](/definitions/smoothness-indicator.md)) | squared undivided fourth difference $\tau^{\mathrm{IMP}}$ | $(\tau^{\mathrm{IMP}}/(\beta^{\mathrm{IMP}}_k+\epsilon))^q$, $q=1$, $\epsilon=10^{-40}$ | Zhong et al. 2023, Eqs. (23)–(26) |
| third-order WCNS3-MR ([multi-resolution WENO](/methods/multi-resolution-weno.md)), stencils of 1 and 3 points | $\tau_{\mathrm{MR}}=\lvert\beta_2-\beta_1\rvert^2$ | $\tau_{\mathrm{MR}}/(\beta_m+\epsilon)$, $\epsilon=10^{-10}$ | Fan et al. 2025b, Eqs. (16)–(17), after Qin et al. |
| compact gas-kinetic reconstruction ([WENO-AO](/methods/weno-ao.md)) | $\lvert3(\beta_1-\beta_2)+(\beta_3-\beta_2)\rvert$ (1-D), $\tfrac13\sum\lvert2\beta_0-\beta_k-\beta_l\rvert$ (triangles) | $(\tau/(\beta_k+\epsilon))^2$, $\epsilon=10^{-5}$ | Zhao, Ji, Shyy & Xu 2023, Eqs. (29), (31)–(32) |

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

Of the MR-AWENO, MR-AWENO-Si, WENO-G and WENO-H rows, the MR-AWENO row has degree 2 like the first three; Li et al. (2023a, §2.3,
Theorem 3) prove that this operator is not scale-invariant and trace it to the different scalings of
$\beta_k$, $\tau$ and $\epsilon$; MR-AWENO-Si and WENO-G are of degree 0,
the former exactly once $\epsilon$ is scaled by $\mathsf m^2$ (Theorem 4) *(compiler check, not in the sources,
for WENO-G: $\nabla^4f$ and the $\beta_k^{1/2}$ are homogeneous of degree 1 in the data, so the ratio has
degree 0 up to $\epsilon$)*. Wan & Xia's $C_R$ contains $\big(\sum|u_j|\big)^2\Delta x$, a deliberate amplitude
dependence meant to make the weights more linear on fine grids (§3.1).

*(Compiler check, not in the sources, for the MR-WCNS, moving-quadrilateral, CWENOZ, IMWENO-P and compact gas-kinetic rows.)* The MR-WCNS ratio has
degree 2 like the first row; it is the MR-AWENO weight, and Li et al.'s (2023a) Theorem 3 covers it. The
moving-quadrilateral, IMWENO-P and compact gas-kinetic ratios have degree 0 up to $\epsilon$, though
$\epsilon=10^{-3}$ in the first is large against small-amplitude data. The CWENOZ ratio, with its mean difference raised to the power 4, has degree
6, the strongest amplitude dependence in the table. IMWENO-P is invariant to data scaling
up to $\epsilon$ but its indicators $\beta^{\mathrm{IMP}}_k$ carry the cell width as a factor, so its weights change with the unit
of length; see [scale invariance](/properties/scale-invariance.md).

*(Compiler check, not in the sources, for the WCNS3-MR row.)* The squared difference of two
indicators over one indicator has degree 2 in the data, like the first row.

## Uses in the bundle

WENO-Z is the interpolation of the fifth-order [A-WENO](/methods/alternative-weno.md) schemes of
Wang et al. (2023b, §2), applied characteristic-wise, and of Chu, Kurganov & Na (2022, Eqs. (3.4)–(3.7)):
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

**Point values in finite volumes, particles and hypersonic overset grids.** Berta, Mignone, Bugli & Mattia (2024, §3.2,
Eqs. (24)–(28); arXiv v4 read) use the same point-value interpolation weights $(\tfrac1{16},\tfrac58,\tfrac5{16})$ inside a
fourth-order finite-volume scheme for classical and relativistic MHD, on point values recovered from the cell averages,
with $\tau_5$ at exponent $q=1$, $\epsilon=10^{-40}$, in primitive or characteristic variables, and claim the first such
use in a finite-volume scheme ([WENO-JS](/methods/weno-js-reconstruction.md),
[MP limiter](/methods/monotonicity-preserving-limiter.md)). Their third-order fallback is the Yamaleev–Carpenter WENO3 in
point-value form, $\alpha_l=d_l\big(1+|u_{i+1}-2u_i+u_{i-1}|^2/(\beta_l+\epsilon)\big)$ with squared one-sided differences as
$\beta_l$, $d=(\tfrac34,\tfrac14)$ and $\epsilon=\Delta x^2$ "to avoid loss of accuracy at critical points" (Eqs. (27)–(28)).
In their tests WENO-Z and MP5 have almost identical errors on the circularly polarized Alfvén wave (orders reaching 4.00)
and WENO-Z "performs the best" in [field-loop advection](/benchmarks/field-loop-advection.md) (§5.3–5.4). Jiang et al.
(2024, §3.2, Eqs. (12)–(15)) embed fifth-order Z-type weights, $\tau_5$ with exponent 2 and $\epsilon=10^{-10}$ in
numerator and denominator, plus the WENO-Z+ term, in a Lagrangian meshless particle method, interpolating primitive
variables component-wise along each particle pair; the observed orders are only 2.2–2.35 on smooth density waves
(Tables 1–2; [WENO-Z+](/methods/weno-z-plus.md)). McQuaid & Brehm (2024, §3.8) use fifth-order finite-difference WENO-Z
with Roe-averaged characteristic reconstruction and Steger–Warming splitting on the Cartesian grid of a hypersonic overset
solver, blended with a first-order flux by the Ducros sensor at strong shocks ([hybrid schemes](/methods/hybrid-weno.md));
they print it as "the WENO-Z scheme of Jiang and Shu with smoothness indicators proposed by Liu et al.", and state that it
"eliminates order reduction at critical points" without qualification, against the second-order rates of WENO5-Z at
second-order critical points recalled above (Li et al. 2022b, Table 6).

Several TENO variants take the fifth-order $\tau_5$ as their global indicator "for a low
computational cost": Hong, Ye & Ye (2022, Eq. (17)) in TENO-M and Liang et al. (2022, §2.2) in TENO5,
written $|\beta_1-\beta_2|$ in the TENO labelling, the same outer pair; Huang, Liang & Fu (2023, §3.2) use
a sixth-order five-point form in TENO5-A instead, and Ji, Liang & Fu (2022, §3.2) say a WENO-Z-type measure
"can be applied" on unstructured meshes but drop it to save cost ([targeted ENO](/methods/targeted-eno.md)).
Wan & Xia (2022, §3) divide $\tau_5$ by the mean of the three $\beta_k$ to get a three-region smoothness
detector ([hybrid schemes](/methods/hybrid-weno.md)). As a comparator WENO5-Z is the most dissipative
scheme in the approximate dispersion relation of Li, Chen & Ren (2022a, Figs. 11–12) and generates their
reference solutions; Huang, Liang & Fu (2023, §4.6) find it, like TENO5, "excessively dissipative" on double
Mach reflection; Jeong et al. (2022, Table 1) measure the same $L^\infty$ error as WENO-M on smooth
advection at $N_x=640$ ($1.96\times10^{-8}$). Liang et al. (2022, §2.2) note that WENO-Z "typically" uses $q=1$ and $C=1$ in the template
above.

**At strong shocks and steady states.** [Ren et al. (2025)](/sources/ren-2025.md) (§2.2, Eqs. (6)–(13)) take
finite-volume WENO-Z with exponent 1, $\epsilon=10^{-15}$, $d=(\tfrac1{10},\tfrac6{10},\tfrac3{10})$ and one weight per
conserved variable as the fifth-order reconstruction of their
[matrix stability analysis](/methods/matrix-stability-analysis.md) of the
[carbuncle](/definitions/carbuncle-phenomenon.md). On a planar Mach 20 normal shock the scheme is unstable with the
Roe, HLLC, HLL and van Leer fluxes and with three fluxes that are shock-stable at first and second order (HLLC-ADC,
hybrid SLAU, HLLC-EC), and blunt-body runs at Mach 20 confirm it (§4.1); mid-point and two-point Gauss face
integration give the same verdicts (Table 2), and characteristic-wise reconstruction lowers the largest growth rate
without removing the instability (§4.4, Figs. 29–30). Inside the numerical shock structure the weights stay $O(1)$,
$(0.21135,0.62458,0.16407)$ at the face next to the shock with HLL (Table 3; [ENO property](/definitions/eno-property.md)).
As a steady-state comparator, finite-volume WENO5-Z with HLLC and the mid-point rule reaches near machine zero only
on a 1D stationary shock; on 2D steady shock problems its residual stalls ("around $O(1)$" on a heterolateral shock
interaction) with post-shock oscillations, against the [converged ENO](/methods/converged-eno.md) scheme of
[Liang & Fu (2026)](/sources/liang-2026.md) (§§5.1–5.6), whose user CPU time is 0.16–0.53 of WENO5-Z's at the finest
effective resolution (Table 1). Chen & Chen (2026, §3.2) use WENO-Z with an immersed boundary as the comparator of
their adaptive TENO on Schardin's problem, where it agrees with the experiment but resolves fewer fine structures
([adaptive TENO](/methods/adaptive-teno.md)).

**In LES of wall turbulence and in GPU codes.** De Vanna et al. (2023a) compare WENO-Z3, Z5 and Z7 with
TENO5, TENO-A5 and a sixth-order energy-preserving central scheme in wall-resolved and wall-modelled LES of
supersonic boundary layers ([supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md),
[wall-modelled LES](/methods/wall-modeled-les.md)). In wall-resolved LES the friction is underestimated and the
log-layer and turbulent-kinetic-energy peak overshoot, less with higher order (§4.2, Figs. 1–2). Used everywhere
in wall-modelled LES, WENO-Z3 mispredicts the wall flow regardless of grid resolution (§6), the higher orders damp the turbulence, and no
WENO-Z order collapses on the central solution (§4.3.1, Figs. 4–5); a hybrid switched by the modified [Ducros sensor](/definitions/ducros-shock-sensor.md) restores it, and at its
threshold $\Psi^*=0.4$ all WENO and TENO variants give identical profiles ([hybrid schemes](/methods/hybrid-weno.md)).
In the solver URANOS the same three WENO-Z orders reach their design order on an advected density wave and
WENO-Z7 is sharper than WENO-Z5 on 1-D and 2-D Riemann problems (De Vanna et al. 2023b, App. A, Figs. 11–13;
[URANOS](/software/uranos.md)). Chandravamsi et al. (2023) use WENO-Z as the comparator of the
[gradient-based schemes](/methods/gradient-based-reconstruction.md): on a uniform-grid double Mach reflection it
resolves the shear layer less well (Fig. 9f); in an implicit LES of a Mach 1.35 jet on 13 M cells it predicts a
screech Strouhal number of 0.432 against 0.306 measured and an axisymmetric instead of a flapping mode, which
the authors attribute to its "relatively poor spectral properties" without a controlled test (§8.3.2–8.3.3,
Table 3); on GPUs it is the fastest scheme on the inviscid double Mach reflection, because it needs no
gradients, and costs about as much as MIG4 on viscous cases (§9.1, Tables 5–7, maximum speedup 209.8×).

## Qualifications

- **Orders at critical points from different measurements.** Li et al. (2022b, Table 6) measure WENO5-Z at
  5.14–5.37 at a first-order critical point, where Borges et al. (2008, Table 3) measure 3.93–3.99 with $q=1$ and
  4.80–4.98 with $q=2$; the test functions, $\epsilon$ and (on this page) the exponent of Li et al.'s run differ, so
  the pair is not recorded as a contradiction. At $n_{\mathrm{cp}}\ge2$ Borges et al.'s analysis gives order 2, Li
  et al. measure 2.11–2.32 at a second-order point, and their general statement names "the $r$th-order ENO" rate.
- McQuaid & Brehm's "WENO-Z scheme of Jiang and Shu with smoothness indicators proposed by Liu et al." differs
  from the founding papers' attribution: they print WENO-Z as Borges et al.'s, on Jiang–Shu indicators, and Liu et al.'s
  indicators are of the undivided-difference form ([smoothness indicators](/definitions/smoothness-indicator.md)).
  Their "eliminates order reduction at critical points" also differs from Borges et al.'s own order 4 at a
  first-order critical point for $q=1$.
- Borges et al. (2008, §2) print the linear weights in an order that matches a left-shift labelling of the
  stencils while their Fig. 1 labels $S_0$ upwind ([WENO-JS](/methods/weno-js-reconstruction.md),
  Qualifications); $\tau_5$ is symmetric in the two outer stencils and unaffected.
- Ye et al. (2022, §1) attribute the redesign of the smoothness indicator for WENO-M to Borges et
  al. and the WENO-Z scheme to Castro et al.; their §2.2 then cites WENO-Z to Borges et al., the founding
  paper ([Borges et al. (2008)](/sources/borges-2008.md)).
- Huang et al. (2026, Eq. (3.6)) and Deng (2023, Eq. (4.24)) print the index $k$ inside $\alpha_j$;
  the index is $j$.
- Hiejima (2022, §1) recalls WENO-Z only in passing, as "more accurate than the nonlinear weights
  of JS as a high-order global smoothness indicator"; the WCNS-JS weighting Hiejima uses is the Jiang–Shu
  one ([WCNS](/methods/weighted-compact-nonlinear-scheme.md)).
- Jeong, Yang & Yoon (2022, Eq. (10)) recall WENO-Z with $\tau_5=|\beta_2-\beta_0|^2$, squared, and $q=1$
  recommended; Luo & Wu (2021) and Wang & Don (2022) write $|\beta_0-\beta_2|$. The recall is not used in their own
  scheme, and the two forms differ in the homogeneity count of the previous section.
- Berta et al. (2024, Eq. (27)) print the upwind WENO3 candidate and the indicator labels inconsistently with their
  linear weights; see [WENO-JS](/methods/weno-js-reconstruction.md). Jiang et al. (2024, Eq. (14)) label all three
  indicators alike and repeat the point $i+1$ in the last term of the third, where the first term of the same indicator
  and the candidate of Eq. (13) use $i+2$, i.e. the stencil $\{i,i+1,i+2\}$.
- Ren et al. (2025) present the reconstruction and the analysis in conserved variables (§2.2, §3.1) but state in
  §4.4 that §§4.1–4.3 reconstruct primitive variables; which variables the main results use is not settled by the
  paper.
- **Naming.** WENO-ZQ (Zhu & Qiu) shares the Z-type weight form but is a different reconstruction,
  of CWENO type (Zheng, Cai, Qiu & Qiu 2022, §2.2); it is not the WENO-Z of Borges et al.

## Contradictions

**Cost of WENO-Z against mapped WENO.** *Open.* [Deng (2023)](/sources/deng-2023.md) (§1, after Borges et al.) states that
WENO-Z is "less computationally expensive than the WENO-M scheme" ([mapped WENO](/methods/mapped-weno.md));
[McQuaid & Brehm (2024)](/sources/mcquaid-2024.md) (§3.8, citing Brehm et al. 2015) state that WENO-Z "is more expensive
than a mapped WENO scheme". Both are statements about the same comparison, WENO-Z against Henrick et al.'s mapped
weights, each resting on a cited work; neither paper prints a timing. Further evidence: Borges et al. (2008, §5.3,
Tables 5–6) time both in one code (same subroutines and compiler options, only the weight routine differing) on one
machine (AMD Opteron 250): CPU time per Runge–Kutta step 1.39 s for WENO-Z against 1.87 s for WENO-M (and 1.47 s for
WENO-JS) on the $400^2$ shock–vortex interaction, 6.15 s against 8.27 s at $800^2$, 6.07 s against 8.13 s on the
$800^2$ Richtmyer–Meshkov run, "about 25% faster" since "WENO-Z does not make use of any mapping". This is one
implementation and one machine; McQuaid & Brehm's cited measurement may concern another implementation. What would decide it: wall-clock or operation counts of WENO-Z and
WENO-M in further codes and hardware, or the implementation behind Brehm et al.'s statement.

# Citations

- [Borges et al. (2008)](/sources/borges-2008.md) — §1; §2, Remarks 1–2; §3, Eqs. (25)–(31), Fig. 3; §4, Eqs. (32)–(42), Tables 1–3; §5, Table 4, Figs. 6–10; §5.3, Tables 5–6; §6.
- [Fu et al. (2016)](/sources/fu-2016.md) — §2.2, Eqs. (14)–(15).
- [Li et al. (2022b)](/sources/li-2022-b.md) — §2, Eqs. (14)–(17), Table 4; §3.2; Tables 6–7; Fig. 3.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §1; §2.2, Eq. (4); §4; §5, Table 1.
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §2.1, Eqs. (4)–(8); §3.2.
- [Deng (2023)](/sources/deng-2023.md) — §1; §4.3, Eqs. (4.24)–(4.25); Fig. 13.
- [Huang et al. (2026)](/sources/huang-2026.md) — §3.1, Eqs. (3.6)–(3.7); §6.8.
- [Ye et al. (2022)](/sources/ye-2022.md) — §1; §2.2, Eq. (6).
- [Fu (2023)](/sources/fu-2023.md) — §2.5, Fig. 2; §3.1, Eq. (17).
- [Fu (2021)](/sources/fu-2021.md) — §1.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1; §4 (WENO5-Z comparator).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §2.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I; App. D.
- [Wang et al. (2021)](/sources/wang-2021.md) — §3.1.1, Step 5, Eq. (3.17).
- [Li, Shu & Qiu (2022d)](/sources/li-2022-d.md) — §2.1, Eqs. (2.16)–(2.22).
- [Zheng, Cai, Qiu & Qiu (2022)](/sources/zheng-2022.md) — §2.2, Eqs. (13)–(14).
- [Wong et al. (2021)](/sources/wong-2021.md) — §4.3, Eqs. (91)–(93); App. B, Eqs. (B.14), (B.20)–(B.21).
- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §2.2.4; App. B.
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — §3.2.1, Eqs. (32)–(34), Lemma 3.1, Remark 3.3; Example 4.4.
- [Chu, Kurganov & Na (2022)](/sources/chu-2022.md) — §3, Eqs. (3.4)–(3.7); §4.
- [Bezgin, Schmidt & Adams (2022)](/sources/bezgin-2022.md) — §3.4–3.5, Figs. 2, 4; §4.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §1.
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §2.5, Eq. (17).
- [Liang et al. (2022)](/sources/liang-2022.md) — §2.2, Eqs. (10)–(12); §4.
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §2, Eqs. (15)–(16); §3.2, Eq. (32); §4.6.
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §3.2.
- [Li, Chen & Ren (2022a)](/sources/li-2022.md) — §3.3, Figs. 11–12; §4.
- [Li, Li, Don & Wang (2023a)](/sources/li-2023.md) — §2.1.1, Eqs. (23)–(24); §2.3, Eqs. (42)–(44), Theorems 3–4.
- [Jeong, Yang & Yoon (2022)](/sources/jeong-2022.md) — §2.2, Eq. (10); §4.3, Eqs. (37)–(39); §5, Table 1.
- [Wan & Xia (2022)](/sources/wan-2022.md) — §2.3, Eq. (2.28); §3, Eqs. (3.1)–(3.4).
- [De Vanna et al. (2023a)](/sources/devanna-2023.md) — §3.1; §4.2–4.3, Figs. 1–5, 7.
- [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) — §3.1; App. A, Figs. 11–13.
- [Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md) — §8.1.3, Fig. 9f; §8.3.2–8.3.3, Table 3; §9.1, Tables 5–7.
- [Zhou, Ding, Huang & Luo (2023)](/sources/zhou-2023.md) — §2.3, Eq. (14).
- [Qin, Chen, Lin & Deng (2023)](/sources/qin-2023.md) — §2.1, Eqs. (11)–(14).
- [Zhao et al. (2023)](/sources/zhao-2023.md) — §3.3, Eq. (27); §3.4, Eqs. (28)–(32).
- [Chen & Deng (2023)](/sources/chen-2023.md) — §2, Eqs. (17)–(18); §3, Eq. (33).
- [Zhong et al. (2023)](/sources/zhong-2023.md) — §2, Eqs. (10)–(11); §3.2, Eqs. (23)–(26); Table 4.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — §3, Eq. (3.23).
- [Gu et al. (2023)](/sources/gu-2023.md) — §2.4.
- [Maltsev et al. (2023)](/sources/maltsev-2023.md) — §2.2.2, Eqs. (22)–(25).
- [Berta et al. (2024)](/sources/berta-2024.md) — §1; §3.2, Eqs. (24)–(28); §5.3–5.4 (arXiv v4).
- [Jiang et al. (2024)](/sources/jiang-2024.md) — §3.2, Eqs. (12)–(15); §4.1, Tables 1–2.
- [McQuaid & Brehm (2024)](/sources/mcquaid-2024.md) — §3.8, Eq. (20).
- [Zhang et al. (2024b)](/sources/zhang-2024-b.md) — §2.3, Eq. (9); §5.2–5.5, Tables 2–4, Fig. 5; §6.4.
- [Fan et al. (2025b)](/sources/fan-2025-b.md) — §2.2, Eqs. (16)–(17): Z-type weights of WCNS3-MR.
- [Ren et al. (2025)](/sources/ren-2025.md) — §2.2, Eqs. (6)–(13); §4.1–4.4, Tables 2–3: finite-volume WENO-Z in the matrix stability analysis of strong shocks.
- [Liang & Fu (2026)](/sources/liang-2026.md) — §5, Figs. 5–26, Table 1: FV WENO5-Z as steady-state comparator.
- [Chen & Chen (2026)](/sources/chen-2026.md) — §3.2, Figs. 11–13: WENO-Z with an immersed boundary as comparator.
