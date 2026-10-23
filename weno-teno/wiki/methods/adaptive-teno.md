---
type: Method
title: "Adaptive TENO (TENO-A, TENO-AA)"
description: "Adaptive TENO varies the TENO cut-off locally through a discontinuity measure, a wavenumber scale sensor or a global smoothness factor (TENO-A, TENO-LAD, TENO-AZ) and, in TENO-AA, also tests nested symmetric large stencils largest-first so that the accuracy order drops recursively near discontinuities; this page gives the formulas, parameters, orders and evidence of these variants."
status: established
aliases: [TENO-A, TENO-AA, TENO5-A, TENO8-AA, TENO10-AA, TENO-AZ, TENO-LAD, adaptive dissipation TENO, adaptive cut-off TENO, TENO with adaptive accuracy order]
tags: [teno, reconstruction, low-dissipation, turbulence, finite-difference]
timestamp: 2026-10-23T23:45:00Z
---

# Adaptive TENO (TENO-A, TENO-AA)

Two adaptations of [targeted ENO](/methods/targeted-eno.md) by Fu's group:
**TENO-A** replaces the constant cut-off $C_T$ by a locally varying one driven by
a discontinuity measure, so that the scheme is nearly linear on smooth
high-wavenumber content and strongly nonlinear at shocks
([Fu (2023)](/sources/fu-2023.md), §4); **TENO-AA** ("adaptive accuracy order and
adaptive dissipation control") adds a new stencil arrangement in which nested
symmetric large stencils are tested largest-first, and the first one found
smooth supplies the whole flux ([Fu (2021)](/sources/fu-2021.md), §3). A later
five-point variant keeps the TENO5-A recipe but drives the cut-off by a
wavenumber [scale sensor](/definitions/scale-sensor.md) instead of the
discontinuity measure ([Huang, Liang & Fu (2023)](/sources/huang-2023-b.md), §3).
As recalled by [Hong, Ye & Ye (2022)](/sources/hong-2022.md) (abstract, §1, §2.5),
the adaptive TENO paper of Fu et al. (2018) is also the origin of the
hierarchical voting of nested stencils, of explicit discontinuity-location
detection and of the dissipation-optimized six- and eight-point background
schemes that other TENO variants reuse (see the TENO-M variant on
[targeted ENO](/methods/targeted-eno.md)).

## Adaptive cut-off (TENO-A)

**Motivation.** High-order undivided differences, on which the smoothness
indicators are built, cannot separate under-resolved high-wavenumber turbulent
fluctuations from genuine discontinuities; low-order undivided differences can
([Fu (2023)](/sources/fu-2023.md), §4.1, Figs. 12–13;
[Fu (2021)](/sources/fu-2021.md), §3.4). Design constraints listed by Fu (2023,
§4.1): no case-by-case tuning, Galilean invariance, no physical-variable sensors,
no spurious oscillations, and, as an implicit LES model, Kolmogorov scaling for
infinite-$\mathrm{Re}$ under-resolved turbulence. Huang et al. (2023, §1) restate
the aim: low dissipation at low wavenumbers, comparatively high dissipation at
high wavenumbers, adequate dissipation at discontinuities.

**Discontinuity measure** (after Ren, Liu and Zhang 2003, as recalled; page-local
symbols $\sigma_i$, $\mu_d$, $\Delta f_{i+1/2}$):

$$\sigma_i=\frac{\lvert2\Delta f_{i+1/2}\Delta f_{i-1/2}\rvert+\epsilon_\sigma}{(\Delta f_{i+1/2})^2+(\Delta f_{i-1/2})^2+\epsilon_\sigma},\qquad
\sigma_{i+1/2}=\min(\sigma_{i-1},\sigma_i,\sigma_{i+1},\sigma_{i+2}),\qquad
\mu_d=1-\min\Big(1,\frac{\sigma_{i+1/2}}{C_r}\Big),$$

with $\Delta f_{i+1/2}$ the first undivided difference of the reconstructed
variable and
$\mu_d\approx1$ at discontinuities, $\approx0$ in smooth regions
([Fu (2023)](/sources/fu-2023.md), Eqs. (31)–(32);
[Fu (2021)](/sources/fu-2021.md), Eqs. (17)–(18)). Huang et al. (2023, §3.1,
Eqs. (18)–(19)) write $\Delta f_{i+1/2}=f_{i+1}-f_i$ explicitly, which neither Fu
paper does. The regularization differs:
Fu (2021) uses $\epsilon_\sigma=10^{-40}$ and $C_r=0.265$; Fu (2023) writes
$\epsilon_\sigma=\frac{0.9C_r}{1-0.9C_r}\,\xi_{\mathrm A}^2$ with scheme-dependent
constants $C_r$, $\xi_{\mathrm A}$ (page-local) whose values it does not give.

**Variant of the sensor stencil and constant in TENO5-A.** For the five-point
TENO5-A, [Huang et al. (2023)](/sources/huang-2023-b.md) (§3.1, Eq. (19) and the
following line) print the same $\epsilon_\sigma$ form as Fu (2023) with
$\xi_{\mathrm A}=10^{-3}$ and $C_r=0.24$, and a **three-point** minimum,
$\sigma_{i+1/2}=\min(\sigma_{i-1},\sigma_i,\sigma_{i+1})$, where the two Fu
papers (on TENO-A of various orders and on TENO-AA) use the four-point minimum
above and Fu (2021) $C_r=0.265$. No source states that the other's stencil or
constant is wrong; the values are recorded as variants, possibly scheme-dependent
(five-point against wider schemes), which none of the sources discusses. In a
different use, the shock detector of hybrid schemes,
[Li, Chen & Ren (2022)](/sources/li-2022.md) (§3.2, Eqs. (48)–(54)) recall
Ren's original as a two-point minimum
$\sigma_{i+1/2}=\min(\sigma_i,\sigma_{i+1})$ with threshold $0.3$ and
$\xi_{\mathrm A}=10^{-3}$, and run it with the four-point minimum "after Kim and
Kwon" and a binary switch; so the minimum over two, three and four points all
occur in the sources.

**Cut-off.** With page-local $\varphi$ and $b$,

$$\varphi(\mu_d)=(1-\mu_d)^4(1+4\mu_d),\qquad b=b_1-b_2\big(1-\varphi(\mu_d)\big),\qquad C_T=10^{-\lfloor b\rfloor}$$

([Fu (2023)](/sources/fu-2023.md), Eq. (33); [Fu (2021)](/sources/fu-2021.md),
Eq. (19); [Huang et al. (2023)](/sources/huang-2023-b.md), Eq. (20), with
$\lfloor\cdot\rfloor$ the "Gauss bracket"). At a discontinuity, $\varphi\approx0$ and
$C_T\to10^{-\lfloor b_1-b_2\rfloor}$ (robust shock capturing); in smooth regions,
$\varphi\approx1$ and $C_T\approx10^{-\lfloor b_1\rfloor}$ (near-linear). Fu
(2023, Fig. 13) interprets $10^{-\lfloor b_1\rfloor}$ as separating low from high
wavenumbers and $10^{-\lfloor b_1-b_2\rfloor}$ as separating high wavenumbers
from discontinuities. TENO-AA uses $b_1=14$, $b_2=6.4$, so $C_T$ moves between
$10^{-7}$ and $10^{-14}$ (Fu 2021, §3.4); TENO5-A uses $b_1=10$, $b_2=5$, so
$C_T$ moves between $10^{-5}$ and $10^{-10}$ (Huang et al. 2023, Eq. (20));
Fu (2023) calls $b_1$, $b_2$ case-independent but does not print them. Variants
recalled by Fu (2023, §4.1): TCNS with adaptive dissipation, TENO6-A with a
[modified Ducros sensor](/definitions/ducros-shock-sensor.md) in place of $\mu_d$, and a cheaper adaptive control of
Peng et al.; the family runs from TENO5-A to TENO8-A, plus TENO10-A with a
positivity-preserving limiter.

**TENO5-A ingredients besides the cut-off** (as recalled and used by Huang et al.
2023, §3.2, Eqs. (32)–(35)): TENO5 stencils and Jiang–Shu $\beta_k$, $C=1$,
$q=6$, the spectrally optimized linear weights $d_0=0.5065006634$,
$d_1=0.3699651429$, $d_2=0.1235341937$ (the small-stencil weights of TENO-AA
below), and a global indicator $\tau_5$ printed as a quadratic form in
$f_{i-2},\dots,f_{i+2}$ with denominator $5040$, called "sixth-order" and
different from the $\tau_5$ of classical TENO5 ($\lvert\beta_0-\beta_2\rvert$ in the
registry's stencil numbering).
*(Compiler check, not in the sources: the printed form is mirror-symmetric under
$i\pm m\leftrightarrow i\mp m$ and vanishes on samples of polynomials of degree
at most 2, so on smooth data it is $O(\Delta x^6)$, consistent with the name.)*
With these weights the background linear scheme is third order, and Huang et
al. measure exactly third order for both TENO5-A and their variant on
$\partial_tu+\partial_xu=0$, $u_0=\sin(\pi x)$, with identical errors (e.g.
$L_1=7.37\times10^{-8}$, $L_\infty=1.16\times10^{-7}$ at $N_x=640$; §4.1,
Table 2): the "five-point" of the name is the stencil, not the order.

**Parameters in two later uses.** [Liang & Fu (2024b)](/sources/liang-2024-b.md)
(§3.3.2, Eqs. (47)–(49)) take the TENO-A cut-off of Fu et al. (2018)
for the eight-point TENO branch of their hybrid TENO-S scheme (see
[targeted ENO](/methods/targeted-eno.md)) with the four-point minimum,
$\xi_{\mathrm A}=10^{-3}$, $C_r=0.23$, $b_1=10.5$, $b_2=3.5$, so that
$C_T$ moves between $10^{-7}$ at discontinuities and $10^{-10}$ in
smooth regions. [Tang (2024)](/sources/tang-2024.md) (§2, Eqs.
(15)–(16)) recalls TENO-A for the fifth-order scheme with the three-point
minimum, $\xi_{\mathrm A}=10^{-3}$, $C_r=0.24$, $b_1=10$, $b_2=5$,
Huang et al.'s TENO5-A values.

## Scale-sensor-driven cut-off (Huang et al. 2023)

**Criticism of the discontinuity measure.** $\mu_d$ "can roughly locate the
discontinuities, but is incapable of estimating the specific wavenumber": on four
test functions its value at critical points of a sine differs from its value at
other points of the same wavenumber, and in one case it is smaller at the
discontinuity than at some critical points ([Huang et al. (2023)](/sources/huang-2023-b.md),
§3.1, Fig. 2). The six-point scale sensors of Su et al. and Sun et al. and the six-point sensor of
[Li, Chen & Ren (2022)](/sources/li-2022.md) cannot be applied directly to a five-point
stencil (Huang et al., §1, §3.1).

**Five-point scale sensor** (Huang et al., §3.1, Eqs. (29)–(31); page-local
$\vartheta_{\mathrm{ESW}}$ for their estimated scaled wavenumber and
$\mathsf D_p$ for the five-point central approximations of
$\Delta x^pf^{(p)}(x_i)$ and $\varepsilon_{\mathrm s}$ for the regularization, as on
[scale sensors](/definitions/scale-sensor.md)):

$$\vartheta_{\mathrm{ESW},i}=\sqrt{\frac{\lvert\mathsf D_3\rvert+\lvert\mathsf D_4\rvert}{\lvert\mathsf D_1\rvert+\lvert\mathsf D_2\rvert+\varepsilon_{\mathrm s}}},\quad\varepsilon_{\mathrm s}=10^{-12},\qquad
\begin{aligned}
\mathsf D_1&=\tfrac1{12}f_{i-2}-\tfrac23f_{i-1}+\tfrac23f_{i+1}-\tfrac1{12}f_{i+2},\\
\mathsf D_2&=-\tfrac1{12}f_{i-2}+\tfrac43f_{i-1}-\tfrac52f_i+\tfrac43f_{i+1}-\tfrac1{12}f_{i+2},\\
\mathsf D_3&=-\tfrac12f_{i-2}+f_{i-1}-f_{i+1}+\tfrac12f_{i+2},\\
\mathsf D_4&=f_{i-2}-4f_{i-1}+6f_i-4f_{i+1}+f_{i+2}.
\end{aligned}$$

For $f=A\sin(k_wx+\varphi_0)$ the ratios of exact derivatives give $\vartheta=k_w\Delta x$ at every
point, critical and inflection points included, and the sensor is large at
discontinuities (Eqs. (24)–(28)). It is evaluated at $x_i$ rather than at
$x_{i+1/2}$ as in the six-point version, which the authors call "almost
identical" without a test (§3.1); they also state, without a sensitivity study,
that results are insensitive to $\varepsilon_{\mathrm s}$. The construction
is developed on [scale sensors](/definitions/scale-sensor.md).

**Cut-off** (Eq. (33)): with the mapping $\tanh(1.01\,\vartheta_{\mathrm{ESW}})$,
chosen for "its rigorous boundedness and good smoothness",

$$b=b_1-b_2\tanh(1.01\,\vartheta_{\mathrm{ESW}}),\qquad C_T=10^{-\lfloor b\rfloor},\qquad b_1=10,\ b_2=5,$$

so small wavenumbers give $C_T=10^{-10}$ (nearly linear) and large sensor values
$C_T\to10^{-5}$. *(Compiler check, not in the sources: with
$\tanh\in[0,1)$, $b\in(5,10]$, so $C_T$ takes the six values
$10^{-10},\dots,10^{-5}$, the same extremes as TENO5-A, whose mapping
$\varphi(\mu_d)$ is decreasing in the measure and enters through $1-\varphi$.)*
Everything else is TENO5-A.

**Evidence** (Huang et al., §§3.2–4.7; Rusanov splitting, Roe-average
characteristic decomposition, SSP-RK3 at CFL 0.4): its
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
has lower dispersion and dissipation than TENO5 (Fig. 3); on Jiang–Shu
multi-wave advection to $t=2$ it equals TENO5-A and is sharper than WENO5-Z and
TENO5, and to $t=18$ it avoids the "obvious oscillations even in the smooth
regions" of TENO5-A (Figs. 4–5); on Shu–Osher it removes TENO5-A's slight
overshoot near $x=3.25$; on double Mach reflection at $1024\times256$ it gives
"much less numerical noise" behind the incident shock than TENO5-A; on
Rayleigh–Taylor ($96\times384$) it resolves the richest structure. The cost
equals TENO5-A's: 80.41 s against 78.47 s at $512\times128$, with WENO5-Z 54.99 s
and TENO5 55.10 s (Table 3; hardware and step count not stated). The claim of
"much lower dissipation than the existing five-point shock-capturing schemes"
(§5) rests on comparisons with WENO5-Z, TENO5 and TENO5-A only.

## Cut-off from shock sensors (TENO-LAD) and from a global factor (TENO-AZ)

**TENO-LAD** (Peng et al. 2021, as recalled by
[Tang (2024)](/sources/tang-2024.md), §2, Eqs. (17)–(18)) adapts $C_T$
through the shock sensor of Peng et al.'s adaptive WENO-Z. With
page-local $\theta_{\mathrm L}$, $m_{\mathrm L}$ and $H$,

$$C_T=10^{-m_{\mathrm L}},\qquad m_{\mathrm L}=B_l+\big\lfloor\theta_{\mathrm L}(B_u-B_l)\big\rfloor,\qquad
\theta_{\mathrm L}=\frac{1}{1+\max_k\big(\tfrac{\tau_5}{\beta_k+\epsilon}\big)/H},$$

$H=10$, $B_l=4$, $B_u=10$, so $C_T$ moves between $10^{-4}$ and $10^{-10}$
*(compiler check, not in the sources)*. Tang recalls that TENO-LAD was
motivated by cases in which TENO-A's adaptive $C_T$ is "ineffective in
the control of numerical oscillations", and that its authors report
about 20 % less CPU time than TENO-A in 2D.

**TENO-AZ** ([Tang (2024)](/sources/tang-2024.md), §3, Eqs.
(19)–(20)) replaces both the discontinuity measure and the TENO-Z
global indicator of the five-point scheme by one factor, a second
difference of the Jiang–Shu indicators,

$$\tau_{\mathrm{AZ}}=\lvert\beta_0+\beta_2-2\beta_1\rvert,\qquad
\gamma_k=\Big(1+\frac{\tau_{\mathrm{AZ}}}{\beta_k+\epsilon}\Big)^6,\qquad
C_T=\min\big(10^{-5},\ \tau_{\mathrm{AZ}}\big)$$

($\tau_{\mathrm{AZ}}$ page-local; TENO5 stencils, $d_k=(0.1,0.6,0.3)$
from the most upwind stencil, $\epsilon=10^{-40}$). The design aims are
few parameters, a simple structure, and $C_T=0$ in smooth regions: with
$C_T=0$ every $\delta_k=1$, and the flux is the fifth-order linear
upwind scheme. Near discontinuities $\tau_{\mathrm{AZ}}>0$ and the cut-off
is capped at $10^{-5}$, the TENO-Z value. Tang states, without results,
that using $\tau_5$ in the cut-off instead "will produce numerical
oscillations" and instability, and that keeping $\tau_5$ in $\gamma_k$
with the new $C_T$ also restores the order at critical points but saves
no time. No order estimate of $\tau_{\mathrm{AZ}}$ is derived. *(Compiler
check, not in the sources: under $f\mapsto\sigma f$ the measure
$\chi_k$ is unchanged while $\tau_{\mathrm{AZ}}\mapsto\sigma^2\tau_{\mathrm{AZ}}$,
so the cut-off $\min(10^{-5},\tau_{\mathrm{AZ}})$ depends on the
amplitude of the data; see [scale invariance](/properties/scale-invariance.md).)*

**Evidence** (Tang 2024, §4; third-order TVD Runge–Kutta, CFL 0.5,
global Lax–Friedrichs splitting; whether the reconstruction is
characteristic-wise is not stated):

- *Critical points* (Tables 1–3; $f=e^x-\sum_{k=1}^{n_{\mathrm{cp}}}x^k/k!$,
  $\epsilon=\Delta x^{2n_{\mathrm{cp}}+3}$, $\Delta x=0.001/2^j$, $j=0,\dots,5$).
  At a first-order critical point all four schemes give orders 6.00,
  5.58, 5.41, 5.32, 5.26. At $n_{\mathrm{cp}}=2$ TENO-Z, TENO-A and
  TENO-LAD fall to 3.00, 2.58, 2.41, 2.32, 2.26 and at $n_{\mathrm{cp}}=3$
  to 4.01, 3.59, 3.41, 3.32, 3.26, while TENO-AZ keeps the errors of
  the linear scheme; see
  [critical-point accuracy](/properties/critical-point-accuracy.md).
- *Spectral properties.* Its [approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
  lies between TENO-Z and TENO-A/TENO-LAD in both dispersion and
  dissipation (Fig. 1).
- *Shock problems.* On Sod, the double rarefaction and the interacting
  blast waves (200 cells) TENO-A shows pronounced oscillations and, near
  the centre of the 123 problem, a trend "directly opposite" to the
  reference; TENO-AZ is comparable to TENO-LAD and better than TENO-A
  and TENO-Z. TENO-A and TENO-LAD fail the blast waves above CFL 0.2.
  In 2D (isentropic vortex, Riemann problem, implosion, double Mach
  reflection, Rayleigh–Taylor, forward-facing step) TENO-AZ resolves
  comparable or finer structure, TENO-A more vortices with more noise
  in double Mach reflection (Figs. 6–17).
- *Robustness.* On the inviscid shock–shear-layer problem on
  $1000\times200$, TENO-Z and TENO-LAD fail at CFL 0.3, 0.5 and 0.8,
  TENO-A runs at 0.3 only, TENO-AZ at all three (§4.4.6, Fig. 16). Tang
  attributes this to the "jump breaks" of the floor-function cut-offs
  against the continuity of the new one, without testing the cause.
- *Cost* (Intel i7-9700, averages of 1000 runs in 1D and 100 in 2D;
  Tables 5–6), relative to TENO-Z: TENO-AZ 0.95–1.03, TENO-A 1.06–1.44,
  TENO-LAD 1.10–1.38. In 1D TENO-LAD is slower than TENO-A in three of
  four cases; in 2D it is faster, in line with the saving Peng et al.
  report.

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
isotropic turbulence on $64^3$. For TENO5-A, Huang et al. (2023, Figs. 4–11)
find a sharper Gaussian pulse and triangle than WENO5-Z and TENO5, better
high-wavenumber resolution on Shu–Osher and a better blast-wave peak near
$x=0.78$, but long-time oscillations and post-shock noise that their
scale-sensor variant removes (previous section).

## TENO-A5 and TENO-A7 in a hybrid wall-turbulence solver

The URANOS finite-difference solver ([URANOS](/software/uranos.md)) carries
TENO-A5 next to TENO5 and WENO-Z of orders 3, 5 and 7. It uses them pure or
switched against a sixth-order kinetic-energy-preserving central scheme by a
[modified Ducros sensor](/definitions/ducros-shock-sensor.md).

**Parameters.** [De Vanna et al. (2023a)](/sources/devanna-2023.md) (§3.1)
and [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) (§3.1) set them
"according to" Fu et al. (2018). $C_T$ "ranges between $10^{-7}$ and
$10^{-10}$ given $\alpha_1=10.5$, $\alpha_2=3.5$, $C_r=0.25$ and
$\xi=10^{-3}$", against the fixed $C_T=10^{-7}$ of their TENO5. No formula is
printed. *(Compiler check, not in the sources: read as $b_1=10.5$ and
$b_2=3.5$ in the cut-off $C_T=10^{-\lfloor b\rfloor}$ above, $b$ runs over
$[7,10.5]$ and $C_T$ over $10^{-10},\dots,10^{-7}$, the printed range, and
$\xi$ is then $\xi_{\mathrm A}$. The identification of the symbols is
inferred, not stated.)* The constant $C_r=0.25$ is a third value next to Fu
(2021)'s $0.265$ and Huang et al.'s $0.24$. De Vanna et al. (2023a, §3.1)
credit the shock-sensor adaptation of $C_T$ to two later works (Hamzehloo et
al.; Peng et al.) and only the parameters to Fu et al. (2018). In the
immersed-boundary work,
[De Vanna et al. (2023c)](/sources/devanna-2023-c.md) (§3.1) use TENO-A7 on a
flat plate and TENO-A5 on a compression ramp, hybridized at the Ducros
threshold $\Psi^*=0.1$, with parameters "suggested by Fu et al." that are not
printed (§§4.3–4.4).

**Evidence on canonical tests** (De Vanna et al. 2023b, App. A):

- *Convergence.* On an advected density wave, all six convective schemes,
  TENO-A5 included, are "scaling with their theoretical order of accuracy"
  in $L_1$, $L_2$ and $L_\infty$ (App. A.1, Fig. 11). The TENO-A5 panel is
  drawn against a fifth-order guide line. The linear weights are not printed
  (see Qualifications).
- *Shocks.* On Sod and Shu–Osher with 200 points, all shock-capturing schemes
  "accurately represent the system dynamics", with "a marked dependence on
  the order of accuracy as well as moving from WENO to TENO" (App. A.2,
  Fig. 12). On a four-quadrant 2D Riemann problem on $1600^2$, the higher
  WENO orders and the TENO schemes resolve more shear-layer instabilities
  (App. A.3, Fig. 13).

**Evidence on wall-resolved and wall-modelled LES** of spatially developing boundary layers
(De Vanna et al. 2023a, §§4.2–4.4;
[supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md)):

- In wall-resolved LES at Mach 2, agreement with DNS friction improves as the
  WENO order rises and from WENO to TENO. The central scheme fits DNS best
  (§4.2, Figs. 1–2).
- In wall-modelled LES, no WENO or TENO scheme collapses onto the central
  solution (§4.3.1). With hybridization at $\Psi^*=0.1$, TENO-A5 and the central
  scheme give the best mean-velocity and fluctuation profiles on the coarse
  grid (§4.3.2, Fig. 6). On the fine grid, TENO5 and TENO-A5 recover DNS
  "almost as the EP scheme, at the evident penalty of a roughly doubled
  computing cost"; the cost figure is cited from other works.
- At Mach 5.86 with the threshold at $\Psi^*=0.2$, all TENO schemes capture the mean
  velocity "precisely" (§4.4.1, Fig. 9). The URANOS validation case at this
  Mach number, run with TENO-A5, agrees "excellently" with DNS in mean
  velocity and temperature and deviates in the inner-layer turbulent kinetic
  energy (De Vanna et al. 2023b, §5.2, Fig. 10).
- **Cost.** In wall-clock time per iteration normalized by the central
  scheme, pure TENO-A5 is the most expensive variant, at 1.32 on the fine
  grid. The hybrids run at 0.90–1.00 (De Vanna et al. 2023a, §4.3.1, Table 2;
  13 Intel KNL 7250 nodes).

## Motivation from fixed-cut-off schemes

Hiejima (2022, §§3.2–3.3, §4) gives a case from outside the TENO papers for adapting the cut-off. Hiejima's
TENO-weighted [WCNS](/methods/weighted-compact-nonlinear-scheme.md) interpolation (WCNS-T) uses the
simplified measure $\gamma_k=1/(\beta_k+\epsilon)^q$ with $q=6$, $\epsilon=10^{-40}$ and a fixed
$C_T=10^{-5}$ on all candidate stencils. At this value Sod shows slight under- and overshoots that
grow with the order, while $C_T=10^{-7}$ makes the Lax plateau between shock and contact oscillate
(stated, not shown); at 11th order the Shu–Osher result does not improve on the 9th. Hiejima proposes
to optimize $q$ and $C_T$ "following" adaptive TENO, citing the 10-point eighth-order TENO10-A,
but does not do it. [Liang et al. (2022)](/sources/liang-2022.md) (§1) mention TENO-A among the
low-dissipation TENO developments but build their own low-dissipation scheme on fixed-cut-off
TENO5 ([TENO-THINC](/methods/teno-thinc.md)).

## Qualifications

- Huang et al. (2023, Table 2) confirm that the TENO5-A linear background with the
  Arshed–Hoffmann weights is third order. *(Compiler check, not in the sources,
  and in agreement: with these weights the combined 5-point linear fallback of
  TENO-AA reproduces the target exactly only for polynomials up to degree 2,
  by exact evaluation of $\sum_kd_k\hat f^{(k)}_{i+1/2}$ on $x^n$, $n\le5$.)*
  Fu (2021) calls it "the five-point reconstruction" without stating its order.
- The order of TENO-A5 is reported two ways. Huang et al. (2023, Table 2)
  measure third order for TENO5-A with the Arshed–Hoffmann linear weights.
  De Vanna et al. (2023b, App. A.1, Fig. 11) state that their TENO-A5
  converges at its "theoretical order" and plot it against a fifth-order
  guide line. De Vanna et al. print neither the linear weights nor the
  global indicator, so the two papers may run different linear backgrounds
  under one name *(compiler check, not in the sources: with the TENO5
  weights $6/10$, $3/10$, $1/10$ of [targeted ENO](/methods/targeted-eno.md)
  the background is the fifth-order upwind scheme)*. The page does not record this as a
  contradiction, because the two statements need not concern the same
  scheme. Printing the URANOS weights would decide it.
- Four values of $C_r$ are recorded for nominally the same TENO-A recipe:
  $0.265$ (Fu 2021), $0.24$ (Huang et al. 2023; Tang 2024), $0.25$ (De
  Vanna et al. 2023a, 2023b, both attributing the value to Fu et al.
  2018) and $0.23$ (Liang & Fu 2024b, citing Fu et al. 2018). No source
  discusses the difference.
- Tang (2024) prints the TENO-A cut-off as $C_T=10^{\lfloor b\rfloor}$
  (Eq. (15)); with $b\in[5,10]$ this gives $C_T\ge10^5$, above every
  normalized measure $\chi_k\le1$, so every stencil would be cut. The
  exponent is $-\lfloor b\rfloor$, as Fu (2021), Fu (2023) and Huang et
  al. (2023) print *(compiler check, not in the sources)*. Tang's
  Table 5 prints the TENO-A/TENO-Z ratio of the blast wave as 1.30;
  the printed times give $2.0913/1.5552=1.345$ *(compiler check, not in
  the sources)*.
- Tang's order recovery at critical points rests on $\epsilon=\Delta x^{2n_{\mathrm{cp}}+3}$,
  which uses the order of the critical point, and on $n_{\mathrm{cp}}\le3$;
  "optimal order accuracy at any order critical point" is not shown
  beyond that. All other tests use $\epsilon=10^{-40}$. The errors of
  Tables 1–3 fall to $2.6\times10^{-22}$ on data of size one, below
  double-precision rounding of the point values *(compiler check, not
  in the sources)*; the arithmetic precision is not stated.
- Tang's introduction says TENO-Z, TENO-A and TENO-LAD all fail at
  CFL $\ge0.3$ on the $1000\times200$ shear-layer mesh, §4.4.6 that
  TENO-A runs at 0.3; the section is followed here.
- The design orders of TENO8-AA and TENO10-AA (6 and 8) are below their point
  counts by construction; Fu (2023) writes "10-point 8th-order".
- The Rayleigh–Taylor solution of TENO-AA loses mirror symmetry; Fu (2021,
  §5.5.2) attributes this to round-off that low dissipation no longer hides.
  Huang et al. (2023, §4.7) report the same loss for TENO5, TENO5-A and their
  variant and give the same explanation; see
  [symmetry preservation](/properties/symmetry-preservation.md).
- Fu (2021) prints $\gamma_k$ for $k=0,\dots,p-1$ with $p$ "the total candidate
  stencil number", while the selection uses $S_p$ as the largest stencil; the two
  indexings cannot both hold.
- Huang et al. (2023, Eq. (20)) define the exponent as $\beta$ and use $\bar\beta$
  in the next line; Eq. (33) uses $\bar\beta$ throughout. The page writes $b$.
- The GPU argument of Fu (2021, §4.4), that wide stencils are not the parallel
  bottleneck, rests on other codes (HTR, 96.6% weak-scaling efficiency on 512
  GPUs); no TENO-AA timing is given. TENO6-A costs 17% more than WENO5-JS on GPU,
  47% on CPU (Fu 2023, §5.4); TENO5-A costs 42% more than TENO5 per run at
  $512\times128$ in Huang et al.'s timing (78.47 s against 55.10 s, Table 3).
  *(Compiler check, not in the sources: the 42% is the ratio of the printed times,
  $78.47/55.10=1.424$.)*

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §§3–5, Eqs. (11)–(29), Remarks 3.1–3.3, Figs. 1–15: TENO-AA.
- [Fu (2023)](/sources/fu-2023.md) — §3.1, Eq. (19); §4, Eqs. (31)–(33), Figs. 12–17; §5.4: TENO-A and its evidence.
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §3.1, Eqs. (18)–(31), Fig. 2; §3.2, Eqs. (32)–(35), Fig. 3; §4, Tables 2–3, Figs. 4–11: TENO5-A parameters and the scale-sensor variant (arXiv v1).
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — abstract, §1, §2.5: adaptive TENO of Fu et al. (2018) as the origin of hierarchical voting and optimized backgrounds.
- [Li, Chen & Ren (2022)](/sources/li-2022.md) — §1, §3.2, Eqs. (48)–(54): Ren's detector, two- and four-point minimum.
- [Liang et al. (2022)](/sources/liang-2022.md) — §1: TENO-A recalled.
- [Tang (2024)](/sources/tang-2024.md) — §§2–4, Eqs. (15)–(20), Tables 1–6, Figs. 1–17: TENO-A and TENO-LAD recalled, TENO-AZ and its evidence.
- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — §3.3.2, Eqs. (47)–(49): TENO-A cut-off in the TENO branch of TENO-S.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §1; §2.5.2, Eqs. (16)–(18); §§3.1–3.3; §4: fixed-cut-off WCNS-T and the proposal to adapt it.
- [De Vanna et al. (2023a)](/sources/devanna-2023.md) — §3.1; §§4.2–4.4, Table 2, Figs. 1–9: TENO-A5 parameters, wall-modelled LES evidence, cost.
- [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) — §3.1; §5.2, Fig. 10; App. A.1–A.3, Figs. 11–13: TENO-A5 in URANOS, convergence, shock tests.
- [De Vanna et al. (2023c)](/sources/devanna-2023-c.md) — §3.1; §§4.3–4.4: hybrid TENO-A7 and TENO-A5 with immersed boundaries.
