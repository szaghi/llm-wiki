---
type: Method
title: "Adaptive TENO (TENO-A, TENO-AA)"
description: "Adaptive TENO varies the TENO cut-off locally through a low-order-undivided-difference discontinuity measure (TENO-A, adaptive dissipation) and, in TENO-AA, also tests nested symmetric large stencils largest-first so that the accuracy order drops recursively near discontinuities; this page gives the formulas, parameters, orders and evidence of both."
status: established
aliases: [TENO-A, TENO-AA, TENO8-AA, TENO10-AA, adaptive dissipation TENO, adaptive cut-off TENO, TENO with adaptive accuracy order]
tags: [teno, reconstruction, low-dissipation, turbulence, finite-difference]
timestamp: 2026-10-22T20:00:00Z
---

# Adaptive TENO (TENO-A, TENO-AA)

Two adaptations of [targeted ENO](/methods/targeted-eno.md) by Fu's group:
**TENO-A** replaces the constant cut-off $C_T$ by a locally varying one driven by
a discontinuity measure, so that the scheme is nearly linear on smooth
high-wavenumber content and strongly nonlinear at shocks
([Fu (2023)](/sources/fu-2023.md), §4); **TENO-AA** ("adaptive accuracy order and
adaptive dissipation control") adds a new stencil arrangement in which nested
symmetric large stencils are tested largest-first, and the first one found
smooth supplies the whole flux ([Fu (2021)](/sources/fu-2021.md), §3).

## Adaptive cut-off (TENO-A)

**Motivation.** High-order undivided differences, on which the smoothness
indicators are built, cannot separate under-resolved high-wavenumber turbulent
fluctuations from genuine discontinuities; low-order undivided differences can
([Fu (2023)](/sources/fu-2023.md), §4.1, Figs. 12–13;
[Fu (2021)](/sources/fu-2021.md), §3.4). Design constraints listed by Fu (2023,
§4.1): no case-by-case tuning, Galilean invariance, no physical-variable sensors,
no spurious oscillations, and, as an implicit LES model, Kolmogorov scaling for
infinite-$\mathrm{Re}$ under-resolved turbulence.

**Discontinuity measure** (after Ren, Liu and Zhang 2003, as recalled; page-local
symbols $\sigma_i$, $\mu_d$, $\Delta f_{i+1/2}$):

$$\sigma_i=\frac{\lvert2\Delta f_{i+1/2}\Delta f_{i-1/2}\rvert+\epsilon_\sigma}{(\Delta f_{i+1/2})^2+(\Delta f_{i-1/2})^2+\epsilon_\sigma},\qquad
\sigma_{i+1/2}=\min(\sigma_{i-1},\sigma_i,\sigma_{i+1},\sigma_{i+2}),\qquad
\mu_d=1-\min\Big(1,\frac{\sigma_{i+1/2}}{C_r}\Big),$$

with $\Delta f_{i+1/2}$ the first undivided difference of the reconstructed
variable (neither source defines it further) and
$\mu_d\approx1$ at discontinuities, $\approx0$ in smooth regions
([Fu (2023)](/sources/fu-2023.md), Eqs. (31)–(32);
[Fu (2021)](/sources/fu-2021.md), Eqs. (17)–(18)). The regularization differs:
Fu (2021) uses $\epsilon_\sigma=10^{-40}$ and $C_r=0.265$; Fu (2023) writes
$\epsilon_\sigma=\frac{0.9C_r}{1-0.9C_r}\,\xi_{\mathrm A}^2$ with scheme-dependent
constants $C_r$, $\xi_{\mathrm A}$ (page-local) whose values it does not give.

**Cut-off.** With page-local $\varphi$ and $b$,

$$\varphi(\mu_d)=(1-\mu_d)^4(1+4\mu_d),\qquad b=b_1-b_2\big(1-\varphi(\mu_d)\big),\qquad C_T=10^{-\lfloor b\rfloor}$$

([Fu (2023)](/sources/fu-2023.md), Eq. (33); [Fu (2021)](/sources/fu-2021.md),
Eq. (19)). At a discontinuity, $\varphi\approx0$ and
$C_T\to10^{-\lfloor b_1-b_2\rfloor}$ (robust shock capturing); in smooth regions,
$\varphi\approx1$ and $C_T\approx10^{-\lfloor b_1\rfloor}$ (near-linear). Fu
(2023, Fig. 13) interprets $10^{-\lfloor b_1\rfloor}$ as separating low from high
wavenumbers and $10^{-\lfloor b_1-b_2\rfloor}$ as separating high wavenumbers
from discontinuities. TENO-AA uses $b_1=14$, $b_2=6.4$, so $C_T$ moves between
$10^{-7}$ and $10^{-14}$ (Fu 2021, §3.4); Fu (2023) calls $b_1$, $b_2$
case-independent but does not print them. Variants recalled by Fu (2023, §4.1):
TCNS with adaptive dissipation, TENO6-A with a modified Ducros sensor in place of
$\mu_d$, and a cheaper adaptive control of Peng et al.; the family runs from
TENO5-A to TENO8-A, plus TENO10-A with a positivity-preserving limiter.

## Adaptive accuracy order (TENO-AA)

**Stencils** ([Fu (2021)](/sources/fu-2021.md), §3.1, Fig. 1(b)): the three
3-point stencils of TENO5, $S_0,S_1,S_2$, plus nested large stencils symmetric
about $x_{i+1/2}$, $S_3=\{i-2,\dots,i+3\}$ (6 points), $S_4=\{i-3,\dots,i+4\}$
(8 points), $S_5=\{i-4,\dots,i+5\}$ (10 points), and so on. Upwind-biased large
candidates, those of the original TENO, are "particularly not recommended" because
their spectral properties "typically do not satisfy the approximate
dispersion-relation" (§3.1).

**Scale separation** without the constant and the global indicator,
$\gamma_k=1/(\beta_k+\epsilon)^q$ with $q=7$, $\epsilon=10^{-40}$
(Fu 2021, Eq. (11); the same simplified form, "validated for up to 10-point
8th-order" TENO, in [Fu (2023)](/sources/fu-2023.md), Eq. (19)).

**Selection** (Fu 2021, §3.3, Eqs. (13)–(16)): the groups
$(S_0,S_1,S_2,S_p),(S_0,S_1,S_2,S_{p-1}),\dots,(S_0,S_1,S_2,S_3)$ are tested
starting from the largest stencil. In each group the four $\beta$, $\gamma$,
$\chi$ and $\delta$ are computed with the sharp cut-off; if the large stencil
passes, its linear flux alone is returned. If no large stencil passes, the flux
is the TENO5-type combination $\omega_k=d_k\delta_k/\sum_{l=0}^2d_l\delta_l$ of the
three small stencils; the paper does not say from which group the flags are
taken. The small stencils serve both as the reference against which a large
stencil's smoothness is judged and as the shock-capturing fallback (Remark 3.1).
In smooth regions the largest stencil is always selected, so the design order
holds (Remark 3.2).

**Linear schemes.** The large-stencil schemes are spectrally optimized, with a
dispersive part minimizing a weighted wavenumber-error integral and a
dissipative part satisfying the Hu-type dispersion–dissipation condition
$\zeta\approx O(10)$ (see [approximate dispersion relation](/definitions/approximate-dispersion-relation.md)),
with relaxed order: 4th order on the 6-point, 6th on the 8-point, 8th on the
10-point stencil (Fu 2021, §4.1, Eqs. (25)–(27), coefficients printed to 16
digits; smoothness indicators of the 6-, 8- and 10-point stencils as exact
rational quadratic forms, Eq. (28)). TENO10-AA thus has order 8 and TENO8-AA
(TENO10-AA without $S_5$) order 6; both reach these orders in $L_\infty$ on
Gaussian-pulse advection (§5.1, Fig. 2, no error table). The small-stencil linear
weights are $d_0=0.5065006634$, $d_1=0.3699651429$, $d_2=0.1235341937$ (from
Arshed and Hoffmann), not the fifth-order $6/10$, $3/10$, $1/10$.

**Evidence.** Numerical only, with one fixed parameter set
([Fu (2021)](/sources/fu-2021.md), §5): sharper Shu–Osher and Titarev–Toro waves
than WENO-CU6, which oscillates near shocklets; a better blast-wave density peak;
"much more small-scale vortical structures" in double Mach reflection at
$512\times128$ than WENO-CU6 at $1024\times256$; finer Rayleigh–Taylor and
Kelvin–Helmholtz structure; extreme cases (double rarefaction, Le Blanc, Sedov,
Mach 80 and 2000 jets, 3D Noh) computed stably only together with the
Hu–Adams–Shu positivity-preserving flux limiter. For TENO-A,
[Fu (2023)](/sources/fu-2023.md) (§4.2, Figs. 14–17, reproduced) reports similar
or more small-scale structure than WENO of the same order on half the
resolution per direction, Kolmogorov scaling for infinite-$\mathrm{Re}$
turbulence, a Taylor–Green dissipation rate on $64^3$ closer to DNS than dynamic
Smagorinsky and ALDM, and agreement with filtered DNS for decaying compressible
isotropic turbulence on $64^3$.

## Motivation from fixed-cut-off schemes

Hiejima (2022, §§3.2–3.3, §4) gives a case from outside the TENO papers for adapting the cut-off. His
TENO-weighted [WCNS](/methods/weighted-compact-nonlinear-scheme.md) interpolation (WCNS-T) uses the
simplified measure $\gamma_k=1/(\beta_k+\epsilon)^q$ with $q=6$, $\epsilon=10^{-40}$ and a fixed
$C_T=10^{-5}$ on all candidate stencils. At this value Sod shows slight under- and overshoots that
grow with the order, while $C_T=10^{-7}$ makes the Lax plateau between shock and contact oscillate
(stated, not shown); at 11th order the Shu–Osher result does not improve on the 9th. He proposes
to optimize $q$ and $C_T$ "following" adaptive TENO, citing the 10-point eighth-order TENO10-A,
but does not do it.

## Qualifications

- *(Compiler check, not in the sources.)* With the Arshed–Hoffmann weights the
  combined 5-point linear fallback of TENO-AA reproduces the target exactly only
  for polynomials up to degree 2: it is third-order accurate, not fifth (exact
  evaluation of $\sum_kd_k\hat f^{(k)}_{i+1/2}$ on $x^n$, $n\le5$). Fu (2021)
  calls it "the five-point reconstruction" without stating its order.
- The design orders of TENO8-AA and TENO10-AA (6 and 8) are below their point
  counts by construction; Fu (2023) writes "10-point 8th-order".
- The Rayleigh–Taylor solution of TENO-AA loses mirror symmetry; Fu (2021,
  §5.5.2) attributes this to round-off that low dissipation no longer hides; see
  [symmetry preservation](/properties/symmetry-preservation.md).
- Fu (2021) prints $\gamma_k$ for $k=0,\dots,p-1$ with $p$ "the total candidate
  stencil number", while the selection uses $S_p$ as the largest stencil; the two
  indexings cannot both hold.
- The GPU argument of Fu (2021, §4.4), that wide stencils are not the parallel
  bottleneck, rests on other codes (HTR, 96.6% weak-scaling efficiency on 512
  GPUs); no TENO-AA timing is given. TENO6-A costs 17% more than WENO5-JS on GPU,
  47% on CPU (Fu 2023, §5.4).

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §§3–5, Eqs. (11)–(29), Remarks 3.1–3.3, Figs. 1–15: TENO-AA.
- [Fu (2023)](/sources/fu-2023.md) — §3.1, Eq. (19); §4, Eqs. (31)–(33), Figs. 12–17; §5.4: TENO-A and its evidence.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §1; §2.5.2, Eqs. (16)–(18); §§3.1–3.3; §4: fixed-cut-off WCNS-T and the proposal to adapt it.
