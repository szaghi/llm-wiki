---
type: Method
title: "Targeted ENO (TENO)"
description: "TENO builds a K-point reconstruction from candidate stencils of incremental width, separates smooth from non-smooth stencils by a strongly scale-separated measure and a sharp cut-off, and combines the surviving stencils with their renormalized linear weights, so that smooth regions recover the background linear scheme exactly; this page gives the basic recipe, its parameters, variants and recorded disagreements."
status: established
aliases: [TENO, targeted essentially non-oscillatory scheme, TENO5, TENO6, TENO7, TENO8]
tags: [teno, reconstruction, finite-difference, low-dissipation, turbulence]
timestamp: 2026-10-30T08:10:00Z
---

# Targeted ENO (TENO)

**Targeted ENO**, introduced by [Fu, Hu & Adams (2016)](/sources/fu-2016.md)
(§3, Eqs. (21)–(29), Tables 1–2, 5), is a family
of nonlinear shock-capturing reconstructions in which each candidate stencil is
either used with its *linear* weight or discarded completely. A $K$-point TENO
scheme combines $K-2$ candidate fluxes,
$\hat f_{i+1/2}=\sum_{k=0}^{K-3}\omega_k\hat f^{(k)}_{i+1/2}$, with
$\omega_k=d_k\delta_k/\sum_ld_l\delta_l$ and binary flags $\delta_k\in\{0,1\}$
decided by a sharp cut-off on a scale-separated smoothness measure
([Fu (2023)](/sources/fu-2023.md), §2, Eqs. (3)–(11);
[Takagi et al. (2022)](/sources/takagi-2022.md), §2.2;
[Ye et al. (2022)](/sources/ye-2022.md), §2;
[Fu (2021)](/sources/fu-2021.md), §§2–3;
[Huang, Liang & Fu (2023)](/sources/huang-2023-b.md), §2, Eqs. (6)–(14);
[Hong, Ye & Ye (2022)](/sources/hong-2022.md), §2, Eqs. (6)–(15);
[Liang et al. (2022)](/sources/liang-2022.md), §2.2, Eqs. (6)–(15)). This is the defining difference from
WENO, where every stencil contributes with a smoothness-dependent weight, and from
ENO, which keeps only the smoothest stencil and cannot recover the full-stencil
optimal accuracy (Fu 2023, §2.3). Fu et al. (2016, §3.1.4) explain the name: because
$\delta_k$ is binary, "a smooth-transition from high-order to low-order through the
weighting strategy is prevented", yet the scheme can reach "arbitrarily high-order
accuracy while satisfying the ENO property"
([ENO property](/definitions/eno-property.md)). Their motivation (§1) is that
classical WENO is too dissipative for turbulence simulations, that very-high-order
WENO loses robustness when several discontinuities lie close together, and that
WENO-CU6 produces spurious waves at marginally resolved wavenumbers
([WENO-CU6](/methods/weno-cu6.md)).

## The basic recipe (finite difference)

The setting is the conservative finite-difference scheme on split point fluxes
$f^\pm$ (see [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
and [Lax–Friedrichs flux splitting](/methods/lax-friedrichs-flux.md)); only the
upwind-biased reconstruction of $f^+$ is written, the other by mirror symmetry
about $x_{i+1/2}$.

**1. Candidate stencils of incremental width.** The widths are

$$\{r_k\}=\begin{cases}\{3,3,3,4,\dots,\tfrac{K+2}{2}\},&K\ \text{even},\\ \{3,3,3,4,\dots,\tfrac{K+1}{2}\},&K\ \text{odd},\end{cases}\qquad k=0,\dots,K-3,$$

(Fu et al. 2016, §3.1.1, Eq. (21), where $r$ is redefined as "the width of a specific
candidate stencil"; Fu 2023, Eq. (5); Ye et al., Eq. (1); Huang et al., Eq. (7); Hong et al., Eq. (7)). TENO numbers stencils differently from
the registry's WENO convention: $S_0=\{i-1,i,i+1\}$ is the central stencil,
$S_1=\{i,i+1,i+2\}$ the downwind-biased one, $S_2=\{i-2,i-1,i\}$ the upwind one,
then $S_3=\{i,\dots,i+3\}$, $S_4=\{i-3,\dots,i\}$, $S_5=\{i,\dots,i+4\}$, each
containing at least one upwind point, "decreasing the strong anti-dissipation induced
by a pure downwind stencil" (Fu et al. 2016, §3.1.1, Fig. 1, Table 1, which prints the
candidate fluxes up to $S_5$; Takagi et al., Fig. 1; Ye et al., Table 1). An order-$K$
reconstruction uses $\bigcup_{k=0}^{K-3}S_k$, and adding the upwind- or downwind-biased
$S_{K-2}$ gives order $K+1$; odd orders are upwind-biased and even orders central
(Fu et al. 2016, §3.1.1).
The three smallest are the WENO5-JS stencils, which Fu (2023, §2.1) credits for
keeping WENO5-JS robustness at very high order. Starting from 2-point stencils is
possible but adds the dissipation of a second-order candidate, "which renders the
motivation questionable" (§2.1). The fifth-order candidate fluxes are
$\hat f^{(0)}=\tfrac16(-f_{i-1}+5f_i+2f_{i+1})$,
$\hat f^{(1)}=\tfrac16(2f_i+5f_{i+1}-f_{i+2})$,
$\hat f^{(2)}=\tfrac16(2f_{i-2}-7f_{i-1}+11f_i)$ (Fu et al. 2016, Table 1; Takagi et al., Eq. (7)).

**2. Strong scale separation.**

$$\gamma_k=\Big(C+\frac{\tau_K}{\beta_k+\epsilon}\Big)^q,\qquad C=1,\ q=6,\ \epsilon=10^{-40}$$

(Fu 2023, Eq. (6); Takagi et al., Eq. (8); Ye et al., Eq. (6)), with $\beta_k$
the Jiang–Shu [smoothness indicator](/definitions/smoothness-indicator.md) of
$S_k$ and $\tau_K$ a smoothness measure of the full $K$-point stencil. Fu et al.
(2016, §3.1.2, Eqs. (22)–(23)) print the measure with $C=1$ and "typically $q=6$"
($q=6$ in all their runs, Table 5), and the indicator of a stencil of width $r_k$ as the
Jiang–Shu sum over the derivatives $1,\dots,r_k-1$; they print no value of $\epsilon$,
only "a small value to prevent division by zero" (§2.2). The value $10^{-40}$ is that
of the later sources cited above. Fu et al. argue that the large $q$ and small $C$
enhance discontinuity detection "rather than" sacrificing it, against WENO-Z and
WENO-CU6, which avoid $q>1$, and WENO-CU6-M, whose $C=1000$, $q=4$ "reduces the
effectiveness of discontinuity detection" (§3.1.2). The
subscript of $\tau_K$ is the full-stencil size $K$, as in the registry and the
sources, not the power of $\Delta x$ it carries ($\tau_K$ is of order 6 for every
$K\ge6$ below). Ye et al.
note the same form covers WENO-Z ($C=1$) and WENO-CU6 ($C=20$), with $q=2$ in
"most WENO schemes". The global indicators used are:

- $K=5$: $\tau_5=\lvert\beta_1-\beta_2\rvert$, the WENO-Z $\tau_5$ in TENO's
  labelling (the two outer stencils) (Takagi et al., §2.2; Ye et al., Eq. (24),
  with $\tau_5=O(\Delta x^5)$ and $\tau_5/(\beta_k+\epsilon)=O(\Delta x^3)$, Eqs. (25)–(27);
  Liang et al., §2.2, "for a low computational cost"; Huang et al., §2, "following"
  Borges et al. and Fu et al.; Hong et al., Eq. (17), chosen for cost instead of the
  full-stencil form). Fu et al. (2016, §3.2) state that $\tau_5$ "is taken from
  Eq. (14) in WENO-Z", where it is printed as $\lvert\beta_0-\beta_2\rvert$ in the
  WENO-JS labels (0 upwind, 2 downwind), i.e. the same outer-stencil difference; the
  TENO-label form $\lvert\beta_1-\beta_2\rvert$ is the later sources'. The adaptive TENO5-A replaces it by a sixth-order five-point
  $\tau_5$ ([adaptive TENO](/methods/adaptive-teno.md));
- $K\ge6$: $\tau_K=\big\lvert\beta_K-\tfrac16(\beta_1+\beta_2+4\beta_0)\big\rvert=O(\Delta x^6)$,
  with $\beta_K$ the indicator of the full stencil (the WENO-CU6 form; Fu 2023,
  Eq. (18); Ye et al., Eqs. (28)–(32), (39), with the 6-point $\beta_K$ printed in
  full in Eq. (29); Hong et al., Eq. (10), who print the five-point indicator
  $\beta_{5,5}$ of $\{i,\dots,i+4\}$ and the 8-point $\tau_8$ as a 36-term
  quadratic form with denominator 62270208000, Eqs. (19)–(20), to show the cost).
  For TENO6, Fu et al. (2016, §3.3) take the WENO-CU6 $\tau_6$ of their Eq. (19),
  printed as $\beta_6-\tfrac16(\beta_0+\beta_2+4\beta_1)$ in the WENO-JS labels,
  without absolute value. For general $K$ their own global indicator is a different
  one (App. A, Eqs. (A.1)–(A.3)): the part of the full-stencil Jiang–Shu indicator
  with the high derivatives,
  $\tau_K=\sum_{j=\lceil K/2\rceil}^{K-1}\Delta x^{2j-1}\int_{I_i}\big(\tfrac{d^j}{dx^j}\hat f_K(x)\big)^2dx
  =\Delta x^{2\lceil K/2\rceil}\big(f^{(\lceil K/2\rceil)}(x_i)\big)^2+O(\Delta x^{2\lceil K/2\rceil+2})$,
  "$\approx O(\Delta x^K)$", with $\hat f_K$ the $K$-point polynomial (the printed
  lower limit is $(K+1)/2$ for odd $K$ and $K/2$ for even $K$). The sixth-order
  $\tau_K$ for every $K\ge6$ is therefore the later sources' choice, not the
  appendix's.

**3. Normalization and sharp cut-off.**

$$\chi_k=\frac{\gamma_k}{\sum_l\gamma_l},\qquad
\delta_k=\begin{cases}0,&\chi_k<C_T,\\1,&\text{otherwise}\end{cases}$$

(Fu et al. 2016, §3.1.3, Eqs. (25)–(26); Fu 2023, Eqs. (8)–(9); Takagi et al.,
Eqs. (11)–(12)). Fu et al. call $C_T$ "a compromise between good spectral properties
and numerical robustness" and also "an effective and direct means to control the
spectral properties" for specific problems, such as compressible turbulence with
embedded shocklets (§3.1.3).

**4. Renormalized linear weights.** $\omega_k=d_k\delta_k/\sum_ld_l\delta_l$
(Fu et al. 2016, §3.1.4, Eqs. (27)–(28); Fu 2023, Eq. (10)). For TENO5 $d_0=6/10$, $d_1=3/10$, $d_2=1/10$, the
fifth-order upwind scheme in TENO labelling (Fu et al. 2016, Table 5; Takagi et al., Eq. (13)); for TENO7
$d=(18,9,3,4,1)/35$ (Ye et al., Eq. (4)). Fu et al. (2016, §3.1.1, Table 2) list the
formal-order weights for $K=3,\dots,8$, "the optimal weight for candidate stencil
$S_k$ to assemble a $K$-th order scheme", and Huang et al. (§2, Table 1) reprint
the same table:

| $K$ | $d_0,d_1,\dots,d_{K-3}$ |
|---|---|
| 3 | $1$ |
| 4 | $\tfrac36,\tfrac36$ |
| 5 | $\tfrac6{10},\tfrac3{10},\tfrac1{10}$ |
| 6 | $\tfrac9{20},\tfrac6{20},\tfrac1{20},\tfrac4{20}$ |
| 7 | $\tfrac{18}{35},\tfrac9{35},\tfrac3{35},\tfrac4{35},\tfrac1{35}$ |
| 8 | $\tfrac{30}{70},\tfrac{18}{70},\tfrac4{70},\tfrac{12}{70},\tfrac1{70},\tfrac5{70}$ |

The $K=7$ row agrees with Ye et al. The $d_k$ can instead be chosen by
spectral optimization (TENO8-opt; Fu 2023, §2.5), see
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md).
The founding paper already does so (Fu et al. 2016, §4, Eq. (31), Tables 3–5): the
order-$K$ background is replaced by $\eta_{\mathrm b}g^{(1)}+(1-\eta_{\mathrm b})g^{(2)}$
of two order-$(K-1)$ sub-schemes ($\eta_{\mathrm b}$ the page-local blending parameter
used for TENO-M below), at the cost of one order. TENO5-opt takes $\eta_{\mathrm b}=0.2$,
$d=(0.55,0.4,0.05)$ (fourth order; $\eta_{\mathrm b}=0.4$ is the upwind fifth-order scheme), and
TENO6-opt $\eta_{\mathrm b}=0.54$, $d=(0.462,0.3,0.054,0.184)$ (fifth order; $\eta_{\mathrm b}=0.5$ is
the sixth-order central scheme), chosen with the dispersion–dissipation ratio of Hu
et al. *(Compiler check, not in the sources: every row of their Tables 3–4 lies on
$d=(\tfrac12+\tfrac{\eta_{\mathrm b}}4,\tfrac12-\tfrac{\eta_{\mathrm b}}2,\tfrac{\eta_{\mathrm b}}4)$ for five points and
$d=(\tfrac3{10}+\tfrac{3\eta_{\mathrm b}}{10},\tfrac3{10},\tfrac{\eta_{\mathrm b}}{10},\tfrac25-\tfrac{2\eta_{\mathrm b}}5)$
for six, e.g. $\eta_{\mathrm b}=0.54$: $0.3+0.162=0.462$, $0.4-0.216=0.184$.)*
[Liang & Fu (2024b)](/sources/liang-2024-b.md) (§2.2, Eqs. (9)–(20);
§3.3.1, Eqs. (36)–(46)) recall the eight-point recipe in full, stencil
widths $\{3,3,3,4,4,5\}$, $q=6$, $\epsilon=10^{-40}$ and the sixth-order
$\tau_8$ with the prefactor $1/62270208000$ also printed by Hong et al.,
and optimize a sixth-order eight-point background with
$d=(0.4130855804023061,\ 0.2193140179474727,\ 0.06459052081827904,\ 0.1439236310125986,\ 0.02746675592227204,\ 0.1316194938970745)$:
its dispersive part minimizes $\int_0^\pi e^{7(\pi-\vartheta)}(\tilde\vartheta_r-\vartheta)^2d\vartheta$,
and its dissipation is fixed by a single coefficient $b_0=0.01$ chosen to
give the dispersion–dissipation ratio of order 10. *(Compiler check, not
in the sources: the flux difference of their Eq. (46) is the
antisymmetric eight-point central derivative with the coefficients
$a_\ell=(0.8441336457,\ -0.2441336457,\ 0.0570096577,\ -0.0067238318)$ of
their split-form flux plus $\tfrac{b_0}{70}$ times the eighth undivided
difference $(1,-8,28,-56,70,-56,28,-8,1)$, i.e. a central scheme with a
pure eighth-order dissipation term.)*
Fu (2023, §2.5) argues, from Kang and Li's criterion for the existence of
linear weights, that the TENO linear combination "will always work" for the first
derivative on uniform Cartesian meshes, and extends to non-uniform Cartesian
meshes because every candidate contains the evaluation point.

## The cut-off $C_T$

$C_T$ is the non-dimensional threshold that decides "smooth" and sets the
wavenumber at which TENO departs from its linear scheme (Fu 2023, §2.5, Fig. 2).
Values used:

| value | context | source |
|---|---|---|
| $10^{-5}$; $10^{-7}$ | TENO5 and TENO5-opt; TENO6 and TENO6-opt (one parameter set for all tests); called "problem independent" | [Fu et al. (2016)](/sources/fu-2016.md), §5, Table 5; §6 |
| $10^{-5}$ to $10^{-7}$ | typical range; smaller resolves higher wavenumbers | Fu 2023, §2.3; Ye et al., §2.3 |
| $10^{-5}$ to $10^{-7}$ | "rather flexible" range, recalled for unstructured TENO | Ji et al., §3.3 |
| $10^{-5}$ | TENO5 default | Takagi et al., §4; Liang et al., §2.2; Huang et al., §2 ("by spectral analysis") |
| $10^{-4}$ | removes a small contact overshoot of TENO-THINC on the blast wave at very high resolution | Takagi et al., §4.5, Fig. 9 |
| $10^{-4}$ | needed for TENO5 to run stably on the Woodward–Colella blast wave ($N_x=400$) | Liang et al., §4.3 |
| $10^{-5}$; $10^{-7}$ | TENO-M; TENO6 and TENO8 (following Fu et al. 2018) | Hong et al., §4.3, §5 |
| $10^{-6}$ | unstructured finite-volume TENO3–6, both selection steps | Ji et al., §3.3 |
| $10^{-6}$ | default of the optimized TENO6 of TENO-HY (after Fu 2019) | Li et al., §4 |
| $10^{-5}$; $0.1$ | TENO-HY on the blast wave; TENO-HY and optimized TENO6 fail on Sedov "even with" $C_T=0.1$ | Li et al., §4.2 |
| $10^{-6}$–$10^{-8}$ | Rayleigh–Taylor: smaller resolves more small scales, $10^{-8}$ matches ninth-order WENO references | Ye et al., §4.7, Fig. 8 |
| $5\times10^{-4}$ | TENO-based discontinuity indicator | Fu 2023, §3.4 |
| $<10^{-3}$ | two-phase cavitation onset | Fu 2023, §5.1 |
| $10^{-5}$ | shock train under back-pressure (results insensitive) | Fu 2023, §5.4 |
| $10^{-7}$ | TENO5 in pure and Ducros-switched hybrid wall-modelled LES (after Fu et al. 2017) | [De Vanna et al. (2023a)](/sources/devanna-2023.md), §3.1 |
| $10^{-7}$; $10^{-6}$ | TENO6 and TENO8 comparators; equal-stencil TENO-type indicator of TENO-S | [Liang & Fu (2024b)](/sources/liang-2024-b.md), §3.1, §4 |
| $10^{-7}$ then $10^{-5}$ | unstructured TENO4-D to TENO7-D: all candidates, then small stencils only | [Ji, Liang & Fu (2023)](/sources/ji-2023.md), §3.2.2 |
| $10^{-5}$; $10^{-4}$ | FV TENO5 "usually"; TENO-type troubled-cell indicator and limiter for RKDG | [Huang & Fu (2024)](/sources/huang-2024.md), §2, §§4.3–4.4 |
| $10^{-7}$ | TENO6 and TENO6-opt comparators | [Zhang et al. (2024b)](/sources/zhang-2024-b.md), §2.5 |
| $10^{-5}$, $10^{-10}$, $10^{-13}$, $10^{-8}$ | the four wavenumber bands of TENO6-SA ([adaptive TENO](/methods/adaptive-teno.md)) | Zhang et al. (2024b), §5.1 |
| $10^{-5}$; $10^{-4}$ | TENO5 default; Woodward–Colella blast wave with Roe flux, "for a stable result" | [Liang & Fu (2024a)](/sources/liang-2024.md), §2.4, §4.3 |
| $10^{-5}$ (1D), $5\times10^{-4}$ (2D) | TENO-based troubled-cell indicator for spectral differences | [Chen & Fu (2024)](/sources/chen-2024.md), §4.2 |
| $10^{-4}$; $10^{-5}$ | TENO troubled-cell indicator; TENO step of the TENO-THINC limiter for RKDG | [Huang et al. (2025a)](/sources/huang-2025.md), §3.1, §3.2.1 |
| $10^{-10}$–$10^{-6}$, adaptive | TENO-E on unstructured meshes, from a jump-variance indicator | [Liang et al. (2025)](/sources/liang-2025.md), §3.3.4 ([adaptive TENO](/methods/adaptive-teno.md)) |
| $10^{-9}$–$10^{-1}$, adaptive; $10^{-1}$ | TENO5-A cut-off; every stencil containing an immersed-boundary ghost point | [Chen & Chen (2026)](/sources/chen-2026.md), §2.3.2 |
| $10^{-1}$; $10^{-10}$ or $10^{-8}$ | converged ENO: stencil discarded at the previous step; kept, large or small stencil | [Liang & Fu (2026)](/sources/liang-2026.md), §3.2.3 ([converged ENO](/methods/converged-eno.md)) |

**Where TENO turns nonlinear.** Zhang et al. (2024b, §3.2, Table 1) measure "through
numerical experiments" in the
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
the reduced wavenumber at which their six-point TENO leaves its linear background, as
a function of $C_T$ (the table does not name the scheme): $1.058$ at $10^{-4}$, $1.146$ at $10^{-5}$, $1.234$ at
$10^{-6}$, $1.322$ at $10^{-7}$, $1.398$ at $10^{-8}$, $1.473$ at $10^{-9}$,
$1.549$ at $10^{-10}$, $1.624$ at $10^{-11}$, $1.706$ at $10^{-12}$ and $1.794$ at
$10^{-13}$ *(compiler check, not in the sources: about $0.08$ per decade)*. This quantifies the statement of Fu (2023,
§2.5) that a smaller $C_T$ resolves higher wavenumbers. For TENO5, Fu et al. (2016,
§3.2, Fig. 3) state that the linear scheme's dispersion and dissipation are recovered
up to the wavenumbers 1.75, 1.85 and 1.95 for $C_T=10^{-5}$, $10^{-6}$ and $10^{-7}$;
for six points (§3.3, Fig. 4) WENO-CU6 departs from its linear scheme at 1.2 and
TENO6 "significantly" later.

An adaptive, locally varying $C_T$ is the subject of
[adaptive TENO](/methods/adaptive-teno.md).

## Properties

- **Exact recovery of the linear scheme.** Where all $\delta_k=1$, the scheme is
  its background linear scheme exactly, not asymptotically; TENO therefore keeps
  that scheme's dispersion and dissipation up to intermediate wavenumbers
  (Fu 2023, §2.5, Figs. 2–3; Takagi et al., §2.2; Huang et al., §1). Fu et al.
  (2016, §5.1, Fig. 10) show it first: on Gaussian-pulse advection the $L_\infty$
  convergence of TENO5, TENO6 and their optimized versions "coincide[s]" with that of
  their background linear schemes, the optimized ones one order lower. On
  Gaussian-pulse advection the $L_\infty$ errors of TENO5 equal those of the
  fifth-order linear scheme at every resolution from $N_x=80$ to $1280$
  (Liang et al., §4.1, Table 4, orders 4.83–5.00), and those of TENO6, TENO8 and
  TENO-M are "almost the same" as those of their linear backgrounds (Hong et al.,
  §5.1, Fig. 8); on unstructured triangles TENO3–TENO6 reproduce the linear
  schemes' errors digit for digit (Ji et al., §5.1, Tables 1–4).
- **Formal order.** Fu et al. (2016, §3.1.5, Eq. (29)) give a sufficient condition:
  all $\chi_k\ge C_T$ holds if every $\gamma_k\to C$ (with $C=1$), which they call "equivalent to"
  $\tau_K/(\beta_k+\epsilon)=O(\Delta x^s)$ for some $s>0$, "a much weaker condition
  than those required for previous WENO schemes"; the argument is one paragraph, with
  no proof (see Contradictions). They state that $\tau_5$, $\tau_6$ and the
  appendix $\tau_K$ satisfy it "even near critical points" ("It is easy to find",
  §§3.2–3.3, App. A); the paper contains no critical-point test.
- **Order at critical points.** With the sixth-order $\tau_K$, TENO reaches its
  design order on Gaussian-pulse advection, with no degeneration for a test
  function with a second-order critical point or for Burgers, where WENO-JS and
  WENO-Z need $\epsilon$ tuning (Fu 2023, §3.1, numerics in cited work). Takagi et
  al. measure fifth order with $L_\infty$ errors identical to the linear upwind-5
  scheme on all grids (Table 2). On the pointwise test $f=x^{n_{\mathrm{cp}}+1}e^{100x}$,
  whose critical point at $x=0$ has order $n_{\mathrm{cp}}$,
  [Zhang et al. (2024b)](/sources/zhang-2024-b.md) (§5.4, Table 3, "disregarding
  the effect of $\epsilon$") measure for TENO6 the rates 6, 6, 2, 4, 4, 6, 6 for
  $n_{\mathrm{cp}}=0,\dots,6$, for TENO6-opt 5, 5, 2, 4, 4, 6, 6, and state that all
  six schemes tested lose order at high-order critical points; see Contradictions.
  See [accuracy at critical points](/properties/critical-point-accuracy.md).
- **Order with one candidate dropped.** [Liang & Fu (2024a)](/sources/liang-2024.md)
  (§3.1) state that when one TENO5 candidate is cut, the renormalized combination of
  the two others "will not achieve any accuracy order" beyond that of a single
  candidate, because the $d_k$ are designed for the three-stencil combination; their
  variant below reaches fourth order in that case. *(Compiler check, not in the
  sources: e.g. with $\delta_2=0$ the combination $\tfrac23\hat f^{(0)}+\tfrac13\hat f^{(1)}$
  is exact only for quadratics, so it is third order like each candidate.)*
- **Robustness with multiple discontinuities.** With two discontinuities in the
  global stencil all candidates of seventh-order WENO are non-smooth, while
  seventh-order TENO still contains a smooth three-point stencil (Fu et al. 2016,
  §3.1.1, Fig. 2; Ye et al., §2.1, Figs. 1–2; schematic), so that TENO "can recover the
  robustness of fifth-order WENO scheme even for very-high-order reconstructions"
  (Fu et al. 2016, §3.1.1).
- **Dissipation.** Fu (2023, §1) reports that WENO's excess dissipation can
  underpredict "approximately the upper 3/4 of the resolvable wavenumbers" in
  broadband turbulence, which is TENO's motivation. Yet fixed-cut-off TENO is "still
  excessively dissipative" for high-wavenumber physical fluctuations, because
  high-order undivided differences respond both to such fluctuations and to
  discontinuities ([Fu (2021)](/sources/fu-2021.md), §3.4; Fu 2023, §4.1).
- **Steady states.** Residuals of WENO stall at truncation-error level because of
  slight post-shock oscillations, and TENO behaves the same way, "an open problem"
  (Fu 2023, §4.2). [Liang & Fu (2026)](/sources/liang-2026.md) measure it for
  finite-volume TENO5 with HLLC and the mid-point rule on uniform meshes: the residual
  reaches near machine zero on a 1D stationary shock but stalls on 2D steady shock
  problems, "around $O(1)$" on a heterolateral and "around $10^{-1}$" on an ipsilateral
  shock interaction, with post-shock oscillations (§§5.1–5.6). They attribute the stall,
  after their finite-difference paper, to the variation in time of the stencil choice at
  fixed interfaces, and their [converged ENO](/methods/converged-eno.md) scheme makes the
  cut-off depend on the previous step; their parameters for TENO5 are not printed.
- **Cost.** Fu et al. (2016, §6) state that TENO's arithmetic operations are
  "similar to" those of classical WENO, "although not specially studied".
  TENO6-A costs 17% more than WENO5-JS on GPU and 47% more on CPU
  (Fu 2023, §5.4); TENO5 costs 810 ms against 696 ms for WENO5-Z per step on a
  $512\times128$ double Mach reflection (Takagi et al., Table 3), but 55.10 s
  against 54.99 s in the timing of Huang et al. (Table 3, same grid, hardware not
  stated). The cost of wide TENO lies in the large-stencil indicators and the
  full-stencil $\tau_K$: on CPU (Intel i9-10980XE, Fortran, per 1000 steps on
  Rayleigh–Taylor, double Mach reflection and a 2D Riemann problem) TENO6 takes
  125.75 / 1747.42 / 2034.43 s and TENO8 163.41 / 2277.26 / 2626.74 s, against
  88.64 / 1252.31 / 1432.34 s for WENO-JS and 105.80 / 1489.53 / 1746.42 s for
  WENO-CU6 (Hong et al., §6, Table 4); they recall that Fu et al. (2018) found
  eight-point TENO "nearly 70%" more expensive than WENO-CU6 on a $1024\times256$
  double Mach reflection. *(Compiler check, not in the sources: Hong et al.'s
  own ratio TENO8/WENO-CU6 is 1.50–1.54; codes, grids and hardware differ.)*
  In the 2D flow tests of [Zhang et al. (2024b)](/sources/zhang-2024-b.md) (Table 6),
  TENO6 costs 4.56–12.32 % more CPU time than WENO7-Z; on 1D advection TENO6 is
  slightly cheaper than EWENO-CU6 (890.53 s against 941.63 s at $N_x=1600$, Table 2).
  On double Mach reflection, [Liang & Fu (2024a)](/sources/liang-2024.md) (Table 1;
  hardware not stated) time TENO5 at 40.04 s and 630.89 s, TENO6 at 45.00 s and
  717.20 s, against 36.51 s and 593.16 s for WENO5-Z, on $400\times100$ and
  $1000\times250$.

## Evidence in the founding paper

Fu et al. (2016, §5, Table 5) run one parameter set throughout: Roe-averaged
[characteristic decomposition](/methods/characteristic-decomposition.md), global
[Lax–Friedrichs splitting](/methods/lax-friedrichs-flux.md) (Roe flux with entropy fix on
the blast waves), third-order (1D) or second-order (2D, on a wavelet-based adaptive
multiresolution grid) strongly stable Runge–Kutta, CFL 0.6, against WENO-JS, WENO-Z,
WENO-CU6 and WENO-CU6-M. They report:

- on the [Sod and Lax tubes](/benchmarks/sod-and-lax-shock-tubes.md) ($N_x=100$), sharper
  contacts than WENO-JS and slight oscillations or an overshoot of WENO-CU6-M at the
  contact (§5.2);
- on the [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md)
  ($N_x=400$), velocity overshoots of WENO-JS and WENO-Z near $x=0.86$, spurious waves of
  WENO-CU6 near $x=0.75$ and $0.86$, and a failure of WENO-CU6-M (§5.3);
- on the [Shu–Osher problem](/benchmarks/shu-osher-problem.md) ($N_x=200$), TENO5-opt
  best among the five-point schemes, with entropy-wave amplitudes "up to 4.52" for
  TENO6 and "about 4.4" for TENO5-opt (§5.4);
- on [double Mach reflection](/benchmarks/double-mach-reflection.md) (effective
  $1024\times256$), small scales of TENO5-opt "comparable to" fifth-order WENO-JS and of
  TENO6 to ninth-order WENO-JS, both at $\Delta x=1/960$ in a cited work, and a failure
  of WENO-CU6-M (§5.5);
- on [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) at $128\times512$,
  structures comparable to WENO-JS and WENO-Z at $256\times1024$ (§5.6), and on the
  [viscous shock tube](/benchmarks/viscous-shock-tube.md) at $\mathrm{Re}=1000$ the
  closest fit to the reference for TENO6-opt (§5.7).

## Variants

Recorded here because they have no page of their own:

- **TENO-N** (TENO without convex combination; Fu 2023, §3.2, Eq. (20), Fig. 6):
  hierarchical voting (a wide stencil judged smooth makes all its sub-stencils
  smooth), then a predefined optimal linear scheme on the largest stencil not
  crossed by a discontinuity; negative or non-existent linear weights are avoided
  by construction.
- **TENO with additional limiters** (Fu 2023, §3.3): non-smooth candidates are
  filtered by an MP or TVD limiter instead of being dropped, and all candidates are
  combined linearly.
- **Hybrid TENO** (Fu 2023, §3.4, Eqs. (21)–(24)): a four-stencil TENO indicator
  with $\gamma_k=1/(\beta_k+\epsilon)^q$, $q=6$, $C_T=5\times10^{-4}$, switches to
  the linear scheme without characteristic decomposition where all stencils are
  smooth, improving efficiency "by a factor of four"; see
  [hybrid central–WENO schemes](/methods/hybrid-weno.md).
  **TENO-S** ([Liang & Fu (2024b)](/sources/liang-2024-b.md), §§3.1–3.2,
  Eqs. (31)–(35), Algorithm 1) takes the same route with an eight-point
  indicator built from six *equal* three-point stencils covering
  $x_{i-3},\dots,x_{i+4}$, three of which do not contain $x_i$ (their
  Jiang–Shu indicators are extrapolated integrals over $I_i$, Eq. (31)):
  $\gamma_k=1/(\beta_k+\epsilon)^6$ with $\epsilon=10^{-4}$ in 1D and
  $10^{-2}$ in multi-D, normalized to $\chi_k$, and the point is smooth
  only if every $\chi_k>10^{-6}$; it is evaluated on the conserved
  density (and total energy in 1D) in physical space, direction by
  direction. Where smooth, the flux is an eight-point
  kinetic-energy-preserving skew-symmetric split form
  ([split convective forms](/methods/split-convective-forms.md)) with the
  optimized $a_\ell$ above; elsewhere the characteristic-wise eight-point
  TENO with the TENO-A cut-off ([adaptive TENO](/methods/adaptive-teno.md))
  and Rusanov splitting. Evidence (§4; SSP-RK3, CFL 0.4, one Ryzen 9 5950X
  core): sixth order on entropy-wave advection ($L_1$ orders up to 5.995),
  more than 90 % of the cells on the split-form branch in double Mach
  reflection (stated), wall times 25–52 % below WENO-CU6, TENO6 and TENO8
  on 2D problems (e.g. 388.08 s against 517.96, 540.17 and 628.79 s on
  Riemann configuration 12, $800^2$, Table 7), finer slip-line vortices
  at $512\times128$ than TENO8, and, in the inviscid
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) to $t=100$,
  long-time stable runs "preserving the total kinetic energy" where the
  other schemes smear the small vortices after $t\approx5$ (Figs. 17–18). The
  interacting blast waves need Roe splitting with entropy fix "to obtain
  a stable result", and positivity preservation is left to future work.
  *(Compiler check, not in the sources: with an absolute $\epsilon$ on
  raw density the indicator depends on the amplitude of the data; see
  [scale invariance](/properties/scale-invariance.md).)*
  [Li, Chen & Ren (2022)](/sources/li-2022.md) (§3.2, Eqs. (55)–(57), Fig. 9) run this
  indicator ($q=6$, $\epsilon=10^{-4}$, threshold $5\times10^{-4}$, distinct from the TENO
  $C_T$) on sine waves and find it correct only below the reduced wavenumber $0.64$, against
  $2.06$ for their modified Ren detector; on double Mach reflection its detection is
  "obviously better" than in Fu's own paper, which they attribute to their normalization of
  the detector inputs (§4.3.1), and the TENO-HY hybrid (upwind-5 plus an optimized TENO6) fails
  on the Sedov problem even with $C_T=0.1$ (§4.2).
- **TENO-M** ([Hong, Ye & Ye (2022)](/sources/hong-2022.md), §§3–4, Eqs. (21)–(30),
  Tables 1–3): a cheaper route to six- and eight-point TENO. Wide TENO with
  hierarchical voting ($\delta_k=1$ for a wide stencil sets all its nested sub-stencils
  smooth, and $\delta_1\delta_2=1$ sets $\delta_0=1$; Eq. (15), attributed to Fu et al. 2018)
  admits 6, 9 and 17 flag combinations for $K=5,6,8$, against $2^{K-2}-1$ without voting.
  TENO-M first runs TENO5 on $S_0,S_1,S_2$ as an explicit detector of where
  discontinuities lie, then enlarges the target stencil one point at a time on each side
  with *three-point* stencils only, $S^*_3=\{i+1,i+2,i+3\}$, $S^*_4=\{i-3,i-2,i-1\}$,
  $S^*_5=\{i+2,i+3,i+4\}$ (page-local), an extension being considered only if the inner
  stencil on the same side was accepted and accepted when two Jiang–Shu-type three-point
  indicators, both evaluated at the node the two stencils share, differ by a relative amount
  below $C_s$ (page-local): $\lvert\beta^*_a-\beta^*_b\rvert/(\max(\beta^*_a,\beta^*_b)+\epsilon)<C_s$
  (Eqs. (22)–(26)). The flux is then the maximum-order linear scheme on the accepted union,
  tabulated in full (Eqs. (18), (27)–(30)); with all stencils accepted it is the
  dissipation-optimized background of Fu et al. (2018): $\eta_{\mathrm b}\hat f^{(5,\mathrm{up})}+(1-\eta_{\mathrm b})\hat f^{(5,\mathrm{down})}$
  with the page-local blending parameter $\eta_{\mathrm b}=0.57$ (fifth order) for six points, and a printed sixth-order eight-point scheme.
  $C_s=0$ recovers TENO5 and $C_s=1$ the linear background at low and intermediate
  wavenumbers in the [approximate dispersion relation](/definitions/approximate-dispersion-relation.md);
  $C_s=0.8$ is adopted, with $C_T=10^{-5}$. *(Compiler check, not in the sources: since the
  ratio is always below 1, $C_s=1$ accepts every extension the base detection allows and
  $C_s=0$ none, consistent with these statements.)* TENO-M6 is close to TENO6 and TENO-M8 to
  TENO8 on shock tubes, blast waves, Shu–Osher, Rayleigh–Taylor (where TENO is "slightly
  better"), double Mach reflection, a 2D Riemann problem (TENO-M slightly better) and decaying
  compressible isotropic turbulence at $128^3$, all much better than WENO-JS, WENO7 and WENO9
  (§5). TENO6 costs about 25% and TENO8 about 44% more than TENO-M6 and TENO-M8; TENO-M8 costs
  about as much as WENO-CU6 and WENO9, while TENO-M6 still costs 12–14% more than WENO-JS
  (§6, Table 4) *(compiler check, not in the sources: the last ratio, from the printed times)*. The TENO and
  TENO-M runs differ in $\tau$ (TENO5's $\tau_5$ against the full-stencil $\tau_K$) and in
  $C_T$ ($10^{-5}$ against $10^{-7}$) as well as in the stencil logic.
- **Finite-volume TENO** shares the reconstruction subroutine with the finite
  difference one; TENO5-LFV switches between a low-dissipation flux (central or
  HLLC) where both full stencils are smooth and HLL otherwise, which improves wave
  resolution and avoids the carbuncle (Fu 2023, §3.6, Eq. (30); see
  [HLL-family solvers](/methods/hll-riemann-solvers.md) and
  [carbuncle](/definitions/carbuncle-phenomenon.md)).
- **Unstructured TENO** (Fu 2023, §3.9): one large central-biased stencil used
  alone when smooth, otherwise an *equal-weight* average of the smooth small
  directional third-order stencils; up to sixth order in 3D. The primary account is
  [Ji, Liang & Fu (2022)](/sources/ji-2022.md) (§3, Eqs. (23)–(28), Fig. 1), who present it
  as the first extension of TENO to unstructured meshes "as far as the authors' knowledge",
  for cell-centred finite volumes on triangles, mixed meshes and tetrahedra in the
  [UCNS3D](/software/ucns3d.md) code. The layout is CWENO's: a large central-biased stencil
  carrying the target-order polynomial and $n_s$ (page-local) small directional stencils with
  quadratic polynomials, all from constrained least-squares fits of cell averages with twice as many
  cells as coefficients ([CWENO](/methods/cweno.md),
  [gradient reconstruction on unstructured meshes](/methods/unstructured-gradient-reconstruction.md)).
  The measure has neither $C$ nor $\tau$, $\gamma_k=1/(\beta_k+\epsilon)^6$ with
  $\epsilon=10^{-12}$ (a WENO-Z-type form "can be applied" but costs more), and the
  selection has two steps with the same $C_T=10^{-6}$: if the large stencil survives the
  cut-off among all $n_s+1$ stencils its polynomial is the reconstruction; otherwise the
  cut-off is redone among the small stencils and the reconstruction is
  $\sum_k\omega_kP_k$ with $\omega_k=\delta_k/\sum_l\delta_l$ over them (page-local $P_k$ the
  candidate polynomials). No linear weights are needed, unlike unstructured WENO, where
  they may be negative or not exist, and CWENO. *(Compiler check, not in the sources: a
  survivor always exists in the second step, since $\max_k\chi_k\ge1/n_s>C_T$.)* With HLL
  fluxes and SSP-RK3 at CFL 0.4, TENO3–6 reach their orders (finest-pair $L_\infty$ orders
  2.92, 3.61, 4.93, 5.97; the fourth-order one stays below 4 at the two finest pairs, although
  the text says the order is restored "for all" schemes), are less dissipative than CWENO and
  equal-order WENO on solid-body rotation, Shu–Osher, Kelvin–Helmholtz and double Mach
  reflection, and stay robust where equal-order WENO5/6 need an extra limiter (§5). TENO and
  CWENO of equal order cost the same, and TENO6 about 65% more per element and step than
  TENO3 (Table 7).
  **Dual cut-off (TENO-D).** [Ji, Liang & Fu (2023)](/sources/ji-2023.md) (§3.2,
  Eqs. (29)–(36)) keep the two-step selection on the same layout, with $n_s$ small
  directional stencils, $\gamma_k=1/(\beta_k+\epsilon)^6$, $\epsilon=10^{-12}$,
  but use two cut-offs: $C_T=10^{-7}$ among all $n_s+1$ candidates, so that the
  large-stencil polynomial, which is then used exactly, survives up to higher
  wavenumbers, and the larger $C_T=10^{-5}$ among the small stencils, for "a
  stronger separation of the discontinuities"; the survivors are averaged
  with $d_k=1/n_s$. They build TENO4-D to TENO7-D in UCNS3D (HLL in the rotated
  face frame, SSP-RK3, CFL 0.4, one parameter set for all tests, §4). On
  $u_t+u_x+u_y=0$ on triangles ($N_e=374$ to $58{,}330$) the errors equal
  the linear schemes' digit for digit, with finest-pair $L_\infty$/$L_2$
  orders 3.61/3.83, 4.93/5.01, 5.97/5.90 and 6.44/6.53 for orders 4–7
  (Tables 1–4). TENO6-D and TENO7-D are less dissipative than CWENO6 and
  CWENO7 on Shu–Osher, double Mach reflection (up to 752,708 triangles) and
  a single-material [triple point](/benchmarks/triple-point-problem.md),
  with solid-body rotation, explosions, shock–vortex interaction, Schardin's
  wedge and a 3D explosion run robustly. Their wall times are "approximately
  the same" as CWENO's (Tables 6–7): TENO-D/CWENO ratios are 0.949 and 0.932
  on Shu–Osher and 1.070 and 1.025 on double Mach reflection *(compiler
  check, not in the sources)*.
- **Finite-volume TENO5 with a five-point candidate** ([Huang & Fu (2024)](/sources/huang-2024.md),
  §2, Eqs. (7)–(15), after Fu et al. 2017): the three TENO5 stencils plus
  the full five-point stencil $S_3$ (their numbering: $S_0$ central,
  $S_1$ downwind, $S_2$ upwind), $\gamma_k=(1+\tau_5/(\beta_k+\epsilon))^6$
  with the full-stencil form $\tau_5=\lvert\beta_{3}-\tfrac16(\beta_1+\beta_2+4\beta_0)\rvert=O(\Delta x^6)$
  in place of the outer-stencil difference; if $S_3$ survives, its fifth-order
  value is used, otherwise the small-stencil combination with $d=(6/10,3/10,1/10)$.
- **TENO weighting in DG limiting** ([Huang & Fu (2024)](/sources/huang-2024.md),
  §§4.3–4.4, §5, Eqs. (32)–(64)): a troubled-cell indicator that normalizes
  $\gamma_n=1/(\beta_n+10^{-3})^6$ of the DG polynomials of cells $i-1,i,i+1$
  and flags cell $i$ when its own $\chi_i<C_T=10^{-4}$ (direction by direction
  in 2D), and a compact limiter for $\mathbb P^2$ RKDG that keeps the cell
  average and rebuilds the higher modes from Hermite-type candidate
  polynomials with TENO weights $\gamma_n=t_n/(\beta_n+10^{-10})^6$, a bias
  $t_n=10$ towards the central candidates and $C_T=10^{-4}$; see
  [troubled-cell indicators](/definitions/troubled-cell-indicator.md) and
  [WENO limiters for DG](/methods/weno-limiter-dg.md). On density waves the
  indicator triggers no limiting (errors equal the unlimited scheme's, third
  order), and on shock problems the limiter is less dissipative than the
  compact WENO limiter of Zhu, Qiu and Zhu it is compared with (visual
  evidence).
- **Non-polynomial TENO with target-stencil selection** ([Liang & Fu (2024a)](/sources/liang-2024.md),
  §3, Eqs. (16)–(36)). The TENO5 cut-off ($q=6$, $\epsilon=10^{-40}$,
  $\tau_5=\lvert\beta_1-\beta_2\rvert$, $C_T=10^{-5}$) only *classifies* the three
  candidates. The flags $(\delta_0,\delta_1,\delta_2)$ select one target stencil, the
  widest that does not cross the non-smooth region: all five points when all are
  smooth, $\{i-2,\dots,i+1\}$ when the downwind $S_1$ is cut,
  $\{i-1,\dots,i+2\}$ when the upwind $S_2$ is cut, and the single surviving
  three-point stencil otherwise. The flux is the one reconstruction on that stencil,
  of order 5, 4 or 3, with no convex combination and no linear weights, the logic of
  TENO-N above. The reconstructions are Gaussian radial-basis-function
  interpolants of the primitive function with an adaptive shape parameter
  ([RBF-WENO](/methods/rbf-weno.md); the shape-parameter law is on
  [adaptive TENO](/methods/adaptive-teno.md)), and cells marked by the TENO-flag
  detector of Liang et al. (2022) take its tanh jump flux
  ([TENO-THINC](/methods/teno-thinc.md)). *(Compiler check, not in the sources: the
  all-cut combination cannot occur, since $\sum_k\chi_k=1$ forces
  $\max_k\chi_k\ge1/3>C_T$.)* Evidence: fifth order in $L_\infty$ on Gaussian-pulse
  advection, ADR dispersion and dissipation better than TENO5 and WENO5-Z, more
  small-scale structure than WENO5-Z and TENO5 on Shu–Osher, double Mach
  reflection, Rayleigh–Taylor, Kelvin–Helmholtz and three 2D Riemann
  configurations, and than the six-point TENO6 on double Mach reflection and the
  2D Riemann problems, at about 1.4 times the wall time of TENO5 (§4, Table 1;
  Figs. 3–16).
- **Band-wise relay of linear schemes (TENO6-SA)** ([Zhang et al. (2024b)](/sources/zhang-2024-b.md),
  §5): TENO6 whose linear background and cut-off switch among sixth-, fourth- and
  second-order schemes by the wavenumber of a scale sensor; see
  [adaptive TENO](/methods/adaptive-teno.md).
- **TENO weighting in limiters for spectral differences** ([Chen & Fu (2024)](/sources/chen-2024.md),
  §§4–7): the troubled-cell indicator of the DG variant above, carried to the nodal
  [spectral difference method](/methods/spectral-difference-method.md) with
  $\gamma_k=1/(\beta_k+\epsilon)^6$ on the polynomials of cells $i-1,i,i+1$,
  $\epsilon=10^{-4}$ and cut-off $10^{-5}$ in 1D, $\epsilon=10^{-3}$ and
  $5\times10^{-4}$ in 2D, flags set per direction, and a cell flagged when *any* of the
  three normalized measures falls below the cut-off (Eq. (18)), where Huang & Fu
  test only the cell's own measure; the limiter combines
  Hermite candidates with TENO-A weights ([adaptive TENO](/methods/adaptive-teno.md),
  [troubled-cell indicators](/definitions/troubled-cell-indicator.md)). A very small
  $\epsilon$ such as $10^{-12}$ is "not good" because high-wavenumber noise of very low
  amplitude would then be flagged (§4.2).
- **TENO5 with hierarchical target schemes in an immersed-boundary solver**
  ([Chen & Chen (2026)](/sources/chen-2026.md), §2.3.1, Eqs. (14)–(22), Table 2, after Fu,
  Hu & Adams 2017). On the TENO5 stencils, numbered here from the most upwind
  ($S_0=\{i-2,i-1,i\}$, $S_1=\{i-1,i,i+1\}$, $S_2=\{i,i+1,i+2\}$, the registry's order),
  each flag pattern selects a predefined target: all smooth, the fifth-order upwind
  combination $(\tfrac1{10},\tfrac6{10},\tfrac3{10})$; $(1,1,0)$, $\tfrac14\hat f^{(0)}+\tfrac34\hat f^{(1)}$;
  $(0,1,1)$, $\tfrac12\hat f^{(1)}+\tfrac12\hat f^{(2)}$; a single survivor, its own flux. A
  wider stencil judged smooth forces its sub-stencils to be considered smooth. *(Compiler
  check, not in the sources: the two four-point targets are the fourth-order
  reconstructions $\tfrac1{12}(f_{i-2}-5f_{i-1}+13f_i+3f_{i+1})$ and
  $\tfrac1{12}(-f_{i-1}+7f_i+7f_{i+1}-f_{i+2})$, so a dropped outer stencil costs one order, unlike
  the renormalized weights discussed under Properties.)* The cut-off is adaptive, and stencils
  touching ghost points of the [immersed boundary](/methods/immersed-boundary-method.md) take
  $C_T=10^{-1}$ ([adaptive TENO](/methods/adaptive-teno.md)).
- **TENO-E on unstructured meshes** ([Liang et al. (2025)](/sources/liang-2025.md), §3.3,
  Eqs. (21)–(28)): the two-level unstructured selection of Ji, Liang & Fu above with
  $\gamma_k=1/(\beta_k+\epsilon)^6$, $\epsilon=10^{-12}$, one cut-off for both levels and equal
  weights $1/n_s$ ($n_s$ the number of directional stencils, the source's $K$) on the surviving third-order directional stencils, at fifth to seventh order on
  triangles, tetrahedra and hexahedra; it is applied only in cells flagged by a jump-variance
  indicator, the linear large-stencil reconstruction acting elsewhere on the conserved variables,
  and its cut-off follows the same indicator ([hybrid schemes](/methods/hybrid-weno.md),
  [adaptive TENO](/methods/adaptive-teno.md)). Final $L_\infty$ orders on an entropy wave on
  triangles are 4.95, 5.81 and 6.99, and the cost is 0.52–0.88 of CWENO5 (Tables 1–2).
- **Converged ENO** ([Liang & Fu (2026)](/sources/liang-2026.md)): a finite-volume TENO-type
  selection whose stencil-wise cut-off depends on the previous step's flags, with a noise filter
  and a choice between the five-point linear value and a two-stencil third-order combination, for
  steady states; see [converged ENO](/methods/converged-eno.md).
- **An equal-weight TENO polynomial in a DG limiter** ([Huang et al. (2025a)](/sources/huang-2025.md),
  §3.2.1, Eqs. (15)–(19)): the TENO cut-off ($q=6$, $\epsilon=10^{-10}$, $C_T=10^{-5}$) on the DG
  polynomials of the cell and its two neighbours, the survivors averaged with equal weights and no
  linear weights; it is one candidate of the [TENO-THINC](/methods/teno-thinc.md) limiter.
- **Very high order and adaptive order**: TENO8-AA, TENO10-AA and TENO-A, see
  [adaptive TENO](/methods/adaptive-teno.md); **TENO-THINC** and its improved
  detector and interpolation-like jump flux of [Liang et al. (2022)](/sources/liang-2022.md), see
  [TENO-THINC](/methods/teno-thinc.md); **AFTENO**, see
  [AFTENO](/methods/afteno.md); **compact TENO** (TCNS, WCNS-T), see
  [WCNS](/methods/weighted-compact-nonlinear-scheme.md); learned weights with a
  TENO cut-off layer, see [learned WENO weights](/methods/learned-weno-weights.md).

## Ingredients borrowed outside TENO

The incremental-stencil WENO interpolation of the WCNS-IS of Wong, Angel, Barad & Kiris (2021, §4.3,
Eqs. (91)–(101)), adapted from Wang, Xiang & Hu, takes two TENO ingredients into a WENO-type convex
combination ([WCNS](/methods/weighted-compact-nonlinear-scheme.md)):

- **Incremental candidates**, but starting from two points: $\{i,i+1\}$ and $\{i-1,i\}$ (second
  order), then $\{i,i+1,i+2\}$ and $\{i-2,i-1,i\}$ (third order), with linear weights
  $\tfrac{15}{32},\tfrac5{32},\tfrac5{16},\tfrac1{16}$ that reproduce the five-point interpolant. Wong
  et al. credit the two-point stencils with robustness when discontinuities are closely located (p.
  20, citing Wang et al.). Fu (2023, §2.1) judges that starting TENO from two-point stencils adds the
  dissipation of a second-order candidate, "which renders the motivation questionable"; the two
  statements weigh robustness and dissipation differently and do not test the same scheme.
- **The TENO reference indicator** $\tau^{\mathrm{ref}}_5$, the third- and fourth-derivative part of
  the five-point Jiang–Shu indicator, attributed to Fu, Hu & Adams, with
  $\tau^{\mathrm{ref}}_5=(u_i''')^2\Delta x^6+O(\Delta x^8)$ (Eq. (100); App. B, Eq. (B.20)); it enters
  WENO-Z-type weights, not a cut-off ([smoothness indicators](/definitions/smoothness-indicator.md),
  [WENO-Z](/methods/weno-z.md)). Its order, 6, matches that of the sixth-order $\tau_K$ above.
  *(Compiler check, not in the sources: the appendix $\tau_K$ of Fu et al. (2016) at $K=5$ sums
  $j=3,4$, which is this third- and fourth-derivative part by definition; for a smooth $f$ its
  expansion is $\Delta x^6(f^{(3)})^2+O(\Delta x^8)$.)* Fu et al. themselves run TENO5 with the WENO-Z $\tau_5$, not with
  it (§3.2).

[Zhang et al. (2024a)](/sources/zhang-2024.md) (§3.3, App. C, Eqs. (C.1)–(C.11)) use the same
incremental-stencil WENO5IS, with the same linear weights and reference indicator, as the base
reconstruction of a finite-volume WENO–THINC multiphase scheme
([incremental-stencil WENO](/methods/incremental-stencil-weno.md)). Measured by how often the
positivity- and boundedness-preserving limiter of their scheme fires in a Mach 10 bubble collapse
at $1920\times960$, TENO5 as base scheme needs it much less often than WENO-JS5, which exceeds
1 % of the cells, and WENO5IS least, never above 0.04 % (§4.8, Fig. 16(b);
[shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)).

Two further schemes take only the cut-off or the stencils:

- **TENO-weighted WCNS interpolation.** Hiejima's WCNS-T (2022, §2.3, §2.5.2, Fig. 1, Eqs. (16)–(18))
  interpolates primitive point values to $x_{i+1/2}$ on $K-2$ candidates over $K$ points, $K=5,7,9,11$
  (the source's $2r-1$): the central $\{i-1,i,i+1\}$, then pairs $\{i,\dots,i+s+1\}$ and
  $\{i-s-1,\dots,i\}$, $s=1,\dots,\tfrac{K-3}2$, described as the "pyramid" of the original TENO
  scheme. *(Compiler check, not in the sources: this is the stencil set of $K$-point TENO for odd $K$,
  e.g. the five TENO7 stencils $S_0,\dots,S_4$ listed above for $K=7$.)* Its linear weights are those
  of point-value interpolation, e.g.
  $(\tfrac{35}{64},\tfrac{35}{128},\tfrac7{128},\tfrac7{64},\tfrac1{64})$ for $K=7$ in the order central,
  downwind, upwind, downwind, upwind (Table 2), not TENO7's $(18,9,3,4,1)/35$. The measure has no
  constant and no global indicator, $\gamma_k=1/(\beta_k+\epsilon)^q$ with $q=6$, $\epsilon=10^{-40}$,
  the form of the hybrid TENO indicator and of Fu (2021) above; the cut-off $C_T=10^{-5}$ acts on every
  candidate independently, with no hierarchical voting, and the surviving linear weights are
  renormalized ([WCNS](/methods/weighted-compact-nonlinear-scheme.md),
  [adaptive TENO](/methods/adaptive-teno.md)). Hiejima (§1) also recalls TENO as candidate stencils
  "defined in incremental width in combination with strong scale separation and ENO-like stencil
  selection".
- **A cut-off on learned weights.** The ENO layer of WENO3-NN applies the sharp cut-off, "similarly"
  to TENO, directly to the two network weights, $c_{\mathrm{eno}}=2\times10^{-4}$, and renormalizes
  (Bezgin, Schmidt & Adams 2022, §3.2, Eq. (16)); there is no scale-separated measure in between
  ([learned WENO weights](/methods/learned-weno-weights.md)).

## TENO5 as a reference scheme in other groups' studies

Two groups run TENO5 as a comparison scheme. Neither prints its
parameters beyond $C_T$, and they report opposite tendencies.

**Wall-modelled LES with a central baseline.**
[De Vanna et al. (2023a)](/sources/devanna-2023.md) compare TENO5 and TENO-A5
with WENO-Z of orders 3, 5 and 7 and with a sixth-order
kinetic-energy-preserving central scheme. The tests are spatially developing
boundary layers at Mach 2 and 5.86, run either pure or switched by a
[modified Ducros sensor](/definitions/ducros-shock-sensor.md).

- In wall-resolved LES, agreement with DNS improves "as the WENO order
  increases as well as when going to a TENO reconstruction" (§4.2.1).
- With pure schemes on the medium wall-modelled grid, the low-dissipation
  property of TENO is "particularly evident": TENO5 approximates the
  reference "quite accurately", where WENO-Z5 and WENO-Z7 give a bulge-like
  log region (§4.3.3, Fig. 7).
- No WENO or TENO scheme collapses onto the central solution, which remains
  the best approximation of DNS (§4.3.1).
- On the fine wall-modelled grid, pure WENO and TENO overestimate the wall
  friction (§4.3.1, Fig. 5(e)).

De Vanna et al. (2023c, §3.1) describe TENO in one sentence, as a discrete
cut-off that "removes non-smooth candidate stencils in the flux
reconstruction". See [adaptive TENO](/methods/adaptive-teno.md) for the
TENO-A results and the cost table.

**Gradient-based reconstruction against TENO5.**
[Chamarthi (2023a)](/sources/chamarthi-2023.md) uses TENO5 (Fu, Hu & Adams
2016; $C_T$ not printed) as the reference for the author's MP-limited
[gradient-based reconstructions](/methods/gradient-based-reconstruction.md).
They run in a point-value finite-difference framework that reconstructs
primitive variables and applies an HLLC flux (arXiv v2). Chamarthi reports:

- **Order.** Fifth order on linear advection. The absolute errors on the
  finest grid are close to those of the author's fourth-order schemes:
  $2.21\times10^{-7}$ against $3.37\times10^{-7}$ (MIG4) and
  $2.35\times10^{-7}$ (MEG6) at $N=802$ (Ex. 4.3, Table 2).
- **Nonlinear order.** Only second order on the nonlinear isentropic vortex,
  like the author's own schemes, with equal errors at $N=2002$ (Table 3). Chamarthi
  attributes this to state reconstruction of primitive variables, after
  Zhang, Zhang & Shu. The companion paper restores the design order by
  reconstructing point fluxes in smooth regions
  ([Chamarthi (2023b)](/sources/chamarthi-2023-b.md), §2.4;
  [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)).
  Chamarthi also states that the conservative-variable finite-volume TENO of Fu et
  al. (2019) is likewise only second order for nonlinear problems and that
  its authors "did not formally compute the order of accuracy" (§4,
  Ex. 4.3; §5). The cited work is not ingested.
- **Oscillations and resolution.**
  - TENO5 oscillates near the Mach stem of the
    [double Mach reflection](/benchmarks/double-mach-reflection.md) at
    $768\times256$ (Ex. 4.4, Fig. 7).
  - It oscillates on the 2D shock–entropy wave, which "may indicate
    insufficient dissipation" (Ex. 4.6, Fig. 9).
  - It oscillates with larger amplitude on the
    [LeBlanc tube](/benchmarks/leblanc-shock-tube.md) at $N=900$. Chamarthi
    finds this consistent with a figure of Li, Fu & Adams, who filter the
    non-smooth TENO8-A stencils by an MP limiter (Ex. 4.10, Fig. 14). That
    filtering is the "TENO with additional limiters" variant above.
  - It "severely under-resolves" the Titarev–Toro waves (Ex. 4.12, Fig. 16).
  - It shows "no roll-up vortices at all" in a single-gas
    [Richtmyer–Meshkov](/benchmarks/richtmyer-meshkov-instability.md) case on
    $320\times80$ (Ex. 4.8, Fig. 11).
- **Spectral rating.** Chamarthi's Table 5 rates the dissipation error of TENO5 "Low"
  and its dispersion error "High"
  ([approximate dispersion relation](/definitions/approximate-dispersion-relation.md)).
- **Cost.** On the viscous shock tube, TENO5 with explicit-gradient viscous
  fluxes takes 50880 s and with compact-gradient viscous fluxes 58680 s,
  against 51146 s for MIG4 (Table 1; hardware not stated).
- **Multicomponent flows.** Chamarthi states that "the implementation of the TENO
  scheme for the multi-component flows, specifically for the 5-equation
  model, is not presented in the open literature" and runs TENO5 on the
  [five-equation model](/definitions/five-equation-model.md) for the
  [shock–helium-bubble](/benchmarks/shock-bubble-interaction.md) case
  (Ex. 4.16). [Fu (2023)](/sources/fu-2023.md) (§5.1) records finite-volume
  TENO with primitive-variable reconstruction for two-phase cavitation
  without naming the model, so the bundle neither confirms nor refutes the
  statement.

## Qualifications

- The two groups above report opposite tendencies for TENO5: low
  dissipation in under-resolved wall turbulence (De Vanna et al.), and
  oscillations from insufficient dissipation at shocks and Mach stems
  together with under-resolution of small structures (Chamarthi). The
  page does not record a contradiction. The flows differ, and Chamarthi
  prints neither $C_T$ nor the variables of the TENO5 reconstruction, so the
  results are not known to concern the same scheme instance as each other
  or as Fu's (2023) reports.
- "$K$-point TENO is $K$th order" (Fu 2023, §2) holds when the $d_k$ are chosen
  for maximum order; the spectrally optimized TENO8-AA and TENO10-AA of
  [Fu (2021)](/sources/fu-2021.md) are of order 6 and 8, and Fu (2023, §3.1)
  itself calls TENO10 a "10-point 8th-order" scheme. [Hong et al. (2022)](/sources/hong-2022.md)
  (§5.1) state that TENO6 and TENO-M6 are fifth order and TENO8 and TENO-M8 sixth order, by
  the dissipation-optimized backgrounds they use; in the founding paper the TENO6 with
  $d=(9,6,1,4)/20$ is sixth order and only TENO6-opt is fifth order (Fu et al. 2016,
  Table 5, §5.1), so the name TENO6 denotes different backgrounds in the two sources.
  TENO5-A is third order ([adaptive TENO](/methods/adaptive-teno.md)). *(Compiler check, not in
  the sources: in TENO-M8 the target schemes on the seven-point unions adjacent to a
  discontinuity, $\hat f_1$ and $\hat f_7$ of Hong et al.'s Eq. (30), are seventh
  order, above the sixth-order background used where all stencils are smooth.)*
- Fu et al. (2016, §6) call the cut-off "problem independent", determined by spectral
  analysis; they use $10^{-5}$ for the five-point and $10^{-7}$ for the six-point schemes
  (Table 5), and Takagi et al. and Liang et al. (table above) raise it to $10^{-4}$ on the
  blast wave.
- Hong et al. run Rayleigh–Taylor with $\epsilon=10^{-4}$ instead of $10^{-40}$ "to
  alleviate" round-off symmetry breaking, following Fu et al. (2018) (§5.5; see
  [symmetry preservation](/properties/symmetry-preservation.md)).
- [Ye et al. (2022)](/sources/ye-2022.md) print the cut-off test as
  $\gamma_k\ge C_T$ (Eq. (8)) while their text compares the normalized $\chi_k$;
  the latter is the recipe of all the other sources.
- Ye et al. find on the shock–entropy-wave test that the exponent matters more
  than $C_T$, and that $q=2$ brings AFTENO closer to the reference than $q=6$
  (§4.5, Fig. 5): the default $q=6$ is not uniformly best.

- Ji, Liang & Fu (2023, §3.3) present the dual selection as "novel"
  against their 2022 unstructured TENO, which already had the two-step
  structure with one $C_T=10^{-6}$; the new element is the pair of
  different cut-offs and the extension to seventh order. They call the
  $C_T$ values "rather generally applicable" without case-by-case tuning,
  while changing them between the two papers. Their fourth-order scheme
  stays below 4 and the seventh-order one reaches 6.44/6.53 at the finest
  pair, against the text's "without degeneration"; the fourth- to
  sixth-order finest-pair orders equal those recorded for the 2022 paper,
  as expected if the same linear schemes run on the same meshes.
- Huang & Fu (2024, §4.3) take $C_T=10^{-4}$ in DG "for better robustness"
  while recalling (§2) that $10^{-5}$ is "usually" taken; their indicator's absolute
  $\epsilon_1=10^{-3}$ makes it depend on the amplitude of the data
  *(compiler check, not in the sources)*, and they do not state the
  variables on which the indicator and limiter act for the Euler system.
- Liang & Fu (2024b) claim the TENO-S indicator needs no case-by-case
  tuning, yet its $\epsilon$ differs between 1D ($10^{-4}$) and multi-D
  ($10^{-2}$).
- Chen & Chen (2026, Eq. (19)) print the TENO5 measure as $\gamma_k=1/(\beta_k+\epsilon)^q$,
  $\epsilon=10^{-40}$, "inspired by" Fu & Tang, without the $C+\tau_K/(\cdot)$ form of step 2 that this
  page records for the TENO5 of Fu et al. they cite; whether the printed form is the one run is not
  stated.
- The explanations of stalled steady residuals differ: Fu (2023, §4.2) speaks of slight post-shock
  oscillations, Liang & Fu (2026, §1, §3.2.3) of the variation of the reconstruction formula at fixed
  interfaces, which they contrast with the post-shock-oscillation account of Zhang & Shu. The two are
  not recorded as a contradiction: Liang & Fu describe the formula variation as an effect of
  shock-induced instability, so the accounts can describe one mechanism, and neither source tests
  them against each other.

## Contradictions

**Accuracy condition on the global indicator $\tau_K$.** *Open.*
[Fu (2023)](/sources/fu-2023.md) (§3.1, Eq. (17), attributed to Fu, Hu and
Adams 2016) states that "to guarantee the $K$th-order accuracy of a $K$-point
TENO scheme in smooth regions" the criterion is
$\tau_K/(\beta_k+\epsilon)=O(\Delta x^s)$ for some $s>0$, "much weaker" than
the $\tau_K=O(\Delta x^K)$ typically required by WENO-Z. The founding paper prints
this side: [Fu et al. (2016)](/sources/fu-2016.md) (§3.1.5, Eq. (29)) derive
$\tau_K/(\beta_{k}+\epsilon)=O(\Delta x^s)$, $s>0$, in one paragraph from
$\chi_k\ge C_T$ and $\gamma_k\to C$ ("equivalent to"), call it "much weaker than those
required for previous WENO schemes", and say nothing on how $C_T$ must compare with
$1/(K-2)$.
[Ye et al. (2022)](/sources/ye-2022.md) (§3.5, Eqs. (36)–(38), attributed to Fu,
Hu and Adams 2017) state that "to ensure that the overall scheme achieves $K$th-order
accuracy" the condition $\tau_K/(\beta_k+\epsilon)=O(\Delta x^{K-2})$ "need[s] to
be satisfied", hence, with $\beta_k=O(\Delta x^2)$, $\tau_K=O(\Delta x^K)$. Both
statements concern the same property (design order of TENO in smooth regions,
with the same sharp cut-off), so they are a genuine conflict and not two
conditions for different properties: Fu's sufficient condition makes Ye et al.'s
necessary one false. The two sources cite different earlier papers: Fu 2023's
[117] is the 2016 JCP paper, now ingested as Fu et al. (2016), and Ye et al.'s [14] the 2017 JCP paper,
not ingested; Fu et al. (2016) do not state Ye et al.'s $O(\Delta x^{K-2})$ condition.
*(Compiler check, not in the sources: their appendix $\tau_K$, printed as
$\approx O(\Delta x^K)$, gives $\tau_K/(\beta_k+\epsilon)=O(\Delta x^{K-2})$ where
$\beta_k=O(\Delta x^2)$, so it meets both conditions and does not decide the question.)*
Ye et al. are also at odds with themselves: they adopt the sixth-order
$\tau_K$ of Eq. (39) as "enough" for TENO of any order, which violates their
Eq. (38) for $K\ge7$. What would decide it: an analysis of the cut-off step,
showing whether $\chi_k\ge C_T$ for every $k$ (and hence $\omega_k=d_k$ exactly)
follows from $\tau_K/(\beta_k+\epsilon)\to0$ at any rate, or a convergence test
of TENO7 and TENO8 with a $\tau_K$ of order below $K$. *(Compiler check, not in
the sources, and not a resolution: if every ratio tends to zero, then
$\gamma_k\to C^q$ for every $k$, $\chi_k\to1/(K-2)$, and all flags are 1 on fine
enough grids as long as $C_T<1/(K-2)$, which supports the weaker condition for
the sharp cut-off away from critical points where $\beta_k$ vanishes; Ye et
al.'s rate is the one that smooth WENO-Z-type weights need.)* Hong et al.'s
evidence does not decide it: TENO8 with the sixth-order $\tau_8$ reaches order 6
on Gaussian-pulse advection ([Hong et al. (2022)](/sources/hong-2022.md), §5.1),
but its background scheme is itself only sixth order, so the test cannot
distinguish the two conditions.

**Order of TENO at a second-order critical point.** *Open.*
[Fu (2023)](/sources/fu-2023.md) (§3.1, numerics in cited work, not shown in the
review) states that with the $\tau_K$ of its Eq. (18), the sixth-order
$\tau_K$ above,
"the accuracy order does not degenerate even for the test function with a
second-order critical point", for the TENO family. [Zhang et al.
(2024b)](/sources/zhang-2024-b.md) (§5.4, Table 3) measure, for TENO6 with a $\tau_6$
of the same form (their Eq. (13), "the stencil arrangement order is changed"),
$C=1$, $q=6$, $\epsilon=10^{-40}$ and $C_T=10^{-7}$, the convergence rate of the
reconstructed derivative of $x^{n_{\mathrm{cp}}+1}e^{100x}$ at $x=0$: 6 at
$n_{\mathrm{cp}}=0,1$, 2 at the second-order critical point, 4 at the third- and
fourth-order ones; they state that all six schemes tested lose order at
high-order critical points. Both statements concern a six-point-class TENO with
the same sixth-order global indicator at a critical point where the first and
second derivatives vanish. Neither source names the other's test: Fu states
neither the test function nor $\epsilon$ and $C_T$; Zhang et al. report their rates
"disregarding the effect of $\epsilon$". The founding paper does not supply Fu's
numerics: [Fu et al. (2016)](/sources/fu-2016.md) only state that their global indicators
satisfy Eq. (29) "even near critical points" (§§3.2–3.3, App. A) and test convergence on
Gaussian-pulse advection alone (§5.1). What would decide it: the same pointwise
test with TENO6 at several $\epsilon$ and $C_T$, reporting which $\delta_k$ are cut
at the critical point.

# Citations

- [Fu, Hu & Adams (2016)](/sources/fu-2016.md) — §1; §3, Eqs. (21)–(29), Tables 1–2, Figs. 1–4; §4, Eq. (31), Tables 3–5; §5, Figs. 10–23; §6; App. A, Eqs. (A.1)–(A.3): the founding paper: stencils, scale separation, cut-off, formal-order condition, TENO5/TENO6 and optimized backgrounds, tests.
- [Fu (2023)](/sources/fu-2023.md) — §§1–5, Eqs. (2)–(33), Figs. 1–9: the review of the family.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §2.2, Eqs. (5)–(14), Table 2, Table 3: TENO5 recipe, order, cost.
- [Ye et al. (2022)](/sources/ye-2022.md) — §2, Eqs. (1)–(10); §3.3–3.5, Eqs. (24)–(39); §4.5, §4.7: stencils, $\tau_K$, $q$ and $C_T$ tests.
- [Fu (2021)](/sources/fu-2021.md) — §§2–3.4: TENO background, dissipation of fixed-cut-off TENO.
- [Wong et al. (2021)](/sources/wong-2021.md) — §4.3, Eqs. (84)–(101); App. B: incremental-stencil interpolation with the TENO reference indicator.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §1; §2.3, Fig. 1, Tables 2, 4, 6; §2.5.2, Eqs. (16)–(18): TENO stencils and cut-off in WCNS interpolation.
- [Bezgin, Schmidt & Adams (2022)](/sources/bezgin-2022.md) — §3.2, Eq. (16): TENO-like cut-off on learned weights.
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §§2–6, Eqs. (6)–(30), Tables 1–4, Figs. 6–16: hierarchical voting, TENO-M, cost of wide TENO.
- [Ji, Liang & Fu (2023)](/sources/ji-2023.md) — §3.2, Eqs. (29)–(36); §3.3; §4, Tables 1–7: dual-cut-off unstructured TENO4-D to TENO7-D.
- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — §2.2, Eqs. (9)–(20); §§3.1–3.3, Eqs. (31)–(46), Algorithm 1; §4, Tables 1–12: TENO8 recipe, optimized background, TENO-S hybrid.
- [Huang & Fu (2024)](/sources/huang-2024.md) — §2, Eqs. (7)–(15); §§4.3–4.4, §5: FV TENO5 with a five-point candidate; TENO-type troubled-cell indicator and limiter for RKDG.
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §§3–5, Eqs. (23)–(28), Tables 1–4, 7: unstructured finite-volume TENO (preprint).
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §2, Eqs. (6)–(16), Table 1; Table 3: general recipe, formal-order linear weights, cost (arXiv v1).
- [Liang et al. (2022)](/sources/liang-2022.md) — §2.2, Eqs. (6)–(15); §4.1, Table 4; §4.3: TENO5 recipe, linear recovery, $C_T$ for the blast wave.
- [Li, Chen & Ren (2022)](/sources/li-2022.md) — §3.2, Eqs. (55)–(57), Fig. 9; §4.2–4.3.1: TENO-based detector and TENO-HY assessed.
- [De Vanna et al. (2023a)](/sources/devanna-2023.md) — §3.1; §§4.2–4.3, Figs. 1, 5, 7: TENO5 with $C_T=10^{-7}$ in wall-resolved and wall-modelled LES.
- [De Vanna et al. (2023c)](/sources/devanna-2023-c.md) — §3.1: TENO described as a discrete cut-off.
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Ex. 4.1–4.16, Tables 1–3, 5, Figs. 7, 9, 11, 14, 16: TENO5 as reference scheme, nonlinear order, oscillations, cost (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — §2.4: order loss of state reconstruction for nonlinear problems (arXiv v1).
- [Zhang et al. (2024b)](/sources/zhang-2024-b.md) — §2.5, Eqs. (14)–(16); §3.2, Table 1; §5.1; §5.4, Table 3; Tables 2, 6: TENO6 parameters, cut-off against nonlinearity onset, critical-point rates, cost, TENO6-SA.
- [Liang & Fu (2024a)](/sources/liang-2024.md) — §2, Eqs. (7)–(15); §3.1–3.3; §4, Table 1: TENO5 recipe, target-stencil selection without linear weights, $C_T$ for the blast wave, cost.
- [Chen & Fu (2024)](/sources/chen-2024.md) — §4.2, Eqs. (15)–(20); §§5.4–5.7: TENO troubled-cell indicator and TENO weighting for spectral-difference limiters.
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §3.3, App. C; §4.8, Fig. 16(b): incremental-stencil WENO5IS with the TENO reference indicator; limiter frequency of WENO-JS5, TENO5 and WENO5IS.
- [Chen & Chen (2026)](/sources/chen-2026.md) — §2.3.1–2.3.2, Eqs. (14)–(26), Table 2, Fig. 3: TENO5 targets, adaptive cut-off, ghost-point rule.
- [Liang et al. (2025)](/sources/liang-2025.md) — §3.3, Eqs. (21)–(28); §4, Tables 1–4: TENO-E on unstructured meshes.
- [Liang & Fu (2026)](/sources/liang-2026.md) — §1; §3.2, Eqs. (17)–(26); §5: converged ENO, steady-state stall of FV TENO5.
- [Huang et al. (2025a)](/sources/huang-2025.md) — §3.1–3.2.1, Eqs. (11)–(19): TENO indicator and equal-weight TENO polynomial in a DG limiter.
