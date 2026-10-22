---
type: Method
title: "Targeted ENO (TENO)"
description: "TENO builds a K-point reconstruction from candidate stencils of incremental width, separates smooth from non-smooth stencils by a strongly scale-separated measure and a sharp cut-off, and combines the surviving stencils with their renormalized linear weights, so that smooth regions recover the background linear scheme exactly; this page gives the basic recipe, its parameters, variants and recorded disagreements."
status: established
aliases: [TENO, targeted essentially non-oscillatory scheme, TENO5, TENO6, TENO7, TENO8]
tags: [teno, reconstruction, finite-difference, low-dissipation, turbulence]
timestamp: 2026-10-23T10:00:00Z
---

# Targeted ENO (TENO)

**Targeted ENO** (Fu, Hu and Adams 2016, as recalled by the sources) is a family
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
optimal accuracy (Fu 2023, §2.3).

## The basic recipe (finite difference)

The setting is the conservative finite-difference scheme on split point fluxes
$f^\pm$ (see [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
and [Lax–Friedrichs flux splitting](/methods/lax-friedrichs-flux.md)); only the
upwind-biased reconstruction of $f^+$ is written, the other by mirror symmetry
about $x_{i+1/2}$.

**1. Candidate stencils of incremental width.** The widths are

$$\{r_k\}=\begin{cases}\{3,3,3,4,\dots,\tfrac{K+2}{2}\},&K\ \text{even},\\ \{3,3,3,4,\dots,\tfrac{K+1}{2}\},&K\ \text{odd},\end{cases}\qquad k=0,\dots,K-3,$$

(Fu 2023, Eq. (5); Ye et al., Eq. (1); Huang et al., Eq. (7); Hong et al., Eq. (7)). TENO numbers stencils differently from
the registry's WENO convention: $S_0=\{i-1,i,i+1\}$ is the central stencil,
$S_1=\{i,i+1,i+2\}$ the downwind-biased one, $S_2=\{i-2,i-1,i\}$ the upwind one,
then $S_3=\{i,\dots,i+3\}$, $S_4=\{i-3,\dots,i\}$, $S_5=\{i,\dots,i+4\}$, each
containing at least one upwind point (Takagi et al., Fig. 1; Ye et al., Table 1).
The three smallest are the WENO5-JS stencils, which Fu (2023, §2.1) credits for
keeping WENO5-JS robustness at very high order. Starting from 2-point stencils is
possible but adds the dissipation of a second-order candidate, "which renders the
motivation questionable" (§2.1). The fifth-order candidate fluxes are
$\hat f^{(0)}=\tfrac16(-f_{i-1}+5f_i+2f_{i+1})$,
$\hat f^{(1)}=\tfrac16(2f_i+5f_{i+1}-f_{i+2})$,
$\hat f^{(2)}=\tfrac16(2f_{i-2}-7f_{i-1}+11f_i)$ (Takagi et al., Eq. (7)).

**2. Strong scale separation.**

$$\gamma_k=\Big(C+\frac{\tau_K}{\beta_k+\epsilon}\Big)^q,\qquad C=1,\ q=6,\ \epsilon=10^{-40}$$

(Fu 2023, Eq. (6); Takagi et al., Eq. (8); Ye et al., Eq. (6)), with $\beta_k$
the Jiang–Shu [smoothness indicator](/definitions/smoothness-indicator.md) of
$S_k$ and $\tau_K$ a smoothness measure of the full $K$-point stencil. The
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
  full-stencil form). The adaptive TENO5-A replaces it by a sixth-order five-point
  $\tau_5$ ([adaptive TENO](/methods/adaptive-teno.md));
- $K\ge6$: $\tau_K=\big\lvert\beta_K-\tfrac16(\beta_1+\beta_2+4\beta_0)\big\rvert=O(\Delta x^6)$,
  with $\beta_K$ the indicator of the full stencil (the WENO-CU6 form; Fu 2023,
  Eq. (18); Ye et al., Eqs. (28)–(32), (39), with the 6-point $\beta_K$ printed in
  full in Eq. (29); Hong et al., Eq. (10), who print the five-point indicator
  $\beta_{5,5}$ of $\{i,\dots,i+4\}$ and the 8-point $\tau_8$ as a 36-term
  quadratic form with denominator 62270208000, Eqs. (19)–(20), to show the cost).

**3. Normalization and sharp cut-off.**

$$\chi_k=\frac{\gamma_k}{\sum_l\gamma_l},\qquad
\delta_k=\begin{cases}0,&\chi_k<C_T,\\1,&\text{otherwise}\end{cases}$$

(Fu 2023, Eqs. (8)–(9); Takagi et al., Eqs. (11)–(12)).

**4. Renormalized linear weights.** $\omega_k=d_k\delta_k/\sum_ld_l\delta_l$
(Fu 2023, Eq. (10)). For TENO5 $d_0=6/10$, $d_1=3/10$, $d_2=1/10$, the
fifth-order upwind scheme in TENO labelling (Takagi et al., Eq. (13)); for TENO7
$d=(18,9,3,4,1)/35$ (Ye et al., Eq. (4)). Huang et al. (§2, Table 1) list the
formal-order weights for $K=3,\dots,8$:

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

An adaptive, locally varying $C_T$ is the subject of
[adaptive TENO](/methods/adaptive-teno.md).

## Properties

- **Exact recovery of the linear scheme.** Where all $\delta_k=1$, the scheme is
  its background linear scheme exactly, not asymptotically; TENO therefore keeps
  that scheme's dispersion and dissipation up to intermediate wavenumbers
  (Fu 2023, §2.5, Figs. 2–3; Takagi et al., §2.2; Huang et al., §1). On
  Gaussian-pulse advection the $L_\infty$ errors of TENO5 equal those of the
  fifth-order linear scheme at every resolution from $N_x=80$ to $1280$
  (Liang et al., §4.1, Table 4, orders 4.83–5.00), and those of TENO6, TENO8 and
  TENO-M are "almost the same" as those of their linear backgrounds (Hong et al.,
  §5.1, Fig. 8); on unstructured triangles TENO3–TENO6 reproduce the linear
  schemes' errors digit for digit (Ji et al., §5.1, Tables 1–4).
- **Order at critical points.** With the sixth-order $\tau_K$, TENO reaches its
  design order on Gaussian-pulse advection, with no degeneration for a test
  function with a second-order critical point or for Burgers, where WENO-JS and
  WENO-Z need $\epsilon$ tuning (Fu 2023, §3.1, numerics in cited work). Takagi et
  al. measure fifth order with $L_\infty$ errors identical to the linear upwind-5
  scheme on all grids (Table 2). See [accuracy at critical points](/properties/critical-point-accuracy.md).
- **Robustness with multiple discontinuities.** With two discontinuities in the
  global stencil all candidates of seventh-order WENO are non-smooth, while
  seventh-order TENO still contains a smooth three-point stencil (Ye et al.,
  §2.1, Figs. 1–2; schematic).
- **Dissipation.** Fu (2023, §1) reports that WENO's excess dissipation can
  underpredict "approximately the upper 3/4 of the resolvable wavenumbers" in
  broadband turbulence, which is TENO's motivation. Yet fixed-cut-off TENO is "still
  excessively dissipative" for high-wavenumber physical fluctuations, because
  high-order undivided differences respond both to such fluctuations and to
  discontinuities ([Fu (2021)](/sources/fu-2021.md), §3.4; Fu 2023, §4.1).
- **Steady states.** Residuals of WENO stall at truncation-error level because of
  slight post-shock oscillations, and TENO behaves the same way, "an open problem"
  (Fu 2023, §4.2).
- **Cost.** TENO6-A costs 17% more than WENO5-JS on GPU and 47% more on CPU
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

## Qualifications

- "$K$-point TENO is $K$th order" (Fu 2023, §2) holds when the $d_k$ are chosen
  for maximum order; the spectrally optimized TENO8-AA and TENO10-AA of
  [Fu (2021)](/sources/fu-2021.md) are of order 6 and 8, and Fu (2023, §3.1)
  itself calls TENO10 a "10-point 8th-order" scheme. Likewise TENO6 and TENO-M6
  are fifth order and TENO8 and TENO-M8 sixth order, by the dissipation-optimized
  backgrounds ([Hong et al. (2022)](/sources/hong-2022.md), §5.1), and TENO5-A is
  third order ([adaptive TENO](/methods/adaptive-teno.md)). *(Compiler check, not in
  the sources: in TENO-M8 the target schemes on the seven-point unions adjacent to a
  discontinuity, $\hat f_1$ and $\hat f_7$ of Hong et al.'s Eq. (30), are seventh
  order, above the sixth-order background used where all stencils are smooth.)*
- Hong et al. run Rayleigh–Taylor with $\epsilon=10^{-4}$ instead of $10^{-40}$ "to
  alleviate" round-off symmetry breaking, following Fu et al. (2018) (§5.5; see
  [symmetry preservation](/properties/symmetry-preservation.md)).
- [Ye et al. (2022)](/sources/ye-2022.md) print the cut-off test as
  $\gamma_k\ge C_T$ (Eq. (8)) while their text compares the normalized $\chi_k$;
  the latter is the recipe of all the other sources.
- Ye et al. find on the shock–entropy-wave test that the exponent matters more
  than $C_T$, and that $q=2$ brings AFTENO closer to the reference than $q=6$
  (§4.5, Fig. 5): the default $q=6$ is not uniformly best.

## Contradictions

**Accuracy condition on the global indicator $\tau_K$.** *Open.*
[Fu (2023)](/sources/fu-2023.md) (§3.1, Eq. (17), attributed to Fu, Hu and
Adams 2016) states that "to guarantee the $K$th-order accuracy of a $K$-point
TENO scheme in smooth regions" the criterion is
$\tau_K/(\beta_k+\epsilon)=O(\Delta x^s)$ for some $s>0$, "much weaker" than
the $\tau_K=O(\Delta x^K)$ typically required by WENO-Z.
[Ye et al. (2022)](/sources/ye-2022.md) (§3.5, Eqs. (36)–(38), attributed to Fu,
Hu and Adams 2017) state that "to ensure that the overall scheme achieves $K$th-order
accuracy" the condition $\tau_K/(\beta_k+\epsilon)=O(\Delta x^{K-2})$ "need[s] to
be satisfied", hence, with $\beta_k=O(\Delta x^2)$, $\tau_K=O(\Delta x^K)$. Both
statements concern the same property (design order of TENO in smooth regions,
with the same sharp cut-off), so they are a genuine conflict and not two
conditions for different properties: Fu's sufficient condition makes Ye et al.'s
necessary one false. The two sources cite different earlier papers (Fu 2023's
[117] is the 2016 JCP paper, Ye et al.'s [14] the 2017 JCP paper), neither
ingested. Ye et al. are also at odds with themselves: they adopt the sixth-order
$\tau_K$ of Eq. (39) as "enough" for TENO of any order, which violates their
Eq. (38) for $K\ge7$. What would decide it: an analysis of the cut-off step,
showing whether $\chi_k\ge C_T$ for every $k$ (and hence $\omega_k=d_k$ exactly)
follows from $\tau_K/(\beta_k+\epsilon)\to0$ at any rate, or a convergence test
of TENO7 and TENO8 with a $\tau_K$ of order below $K$. *(Compiler check, not in
the sources, and not a resolution: if every ratio tends to zero, then
$\gamma_k\to C^q$ for every $k$, $\chi_k\to1/(K-2)$, and all flags are 1 on fine
enough grids as long as $C_T<1/(K-2)$, which supports the weaker condition for
the sharp cut-off away from critical points where $\beta_k$ vanishes; Ye et
al.'s rate is the one that smooth WENO-Z-type weights need.)* The chunk-4
evidence does not decide it: TENO8 with the sixth-order $\tau_8$ reaches order 6
on Gaussian-pulse advection ([Hong et al. (2022)](/sources/hong-2022.md), §5.1),
but its background scheme is itself only sixth order, so the test cannot
distinguish the two conditions.

# Citations

- [Fu (2023)](/sources/fu-2023.md) — §§1–5, Eqs. (2)–(33), Figs. 1–9: the review of the family.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §2.2, Eqs. (5)–(14), Table 2, Table 3: TENO5 recipe, order, cost.
- [Ye et al. (2022)](/sources/ye-2022.md) — §2, Eqs. (1)–(10); §3.3–3.5, Eqs. (24)–(39); §4.5, §4.7: stencils, $\tau_K$, $q$ and $C_T$ tests.
- [Fu (2021)](/sources/fu-2021.md) — §§2–3.4: TENO background, dissipation of fixed-cut-off TENO.
- [Wong et al. (2021)](/sources/wong-2021.md) — §4.3, Eqs. (84)–(101); App. B: incremental-stencil interpolation with the TENO reference indicator.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §1; §2.3, Fig. 1, Tables 2, 4, 6; §2.5.2, Eqs. (16)–(18): TENO stencils and cut-off in WCNS interpolation.
- [Bezgin, Schmidt & Adams (2022)](/sources/bezgin-2022.md) — §3.2, Eq. (16): TENO-like cut-off on learned weights.
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §§2–6, Eqs. (6)–(30), Tables 1–4, Figs. 6–16: hierarchical voting, TENO-M, cost of wide TENO.
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §§3–5, Eqs. (23)–(28), Tables 1–4, 7: unstructured finite-volume TENO (preprint).
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §2, Eqs. (6)–(16), Table 1; Table 3: general recipe, formal-order linear weights, cost (arXiv v1).
- [Liang et al. (2022)](/sources/liang-2022.md) — §2.2, Eqs. (6)–(15); §4.1, Table 4; §4.3: TENO5 recipe, linear recovery, $C_T$ for the blast wave.
- [Li, Chen & Ren (2022)](/sources/li-2022.md) — §3.2, Eqs. (55)–(57), Fig. 9; §4.2–4.3.1: TENO-based detector and TENO-HY assessed.
