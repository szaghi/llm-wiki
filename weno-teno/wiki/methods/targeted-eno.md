---
type: Method
title: "Targeted ENO (TENO)"
description: "TENO builds a K-point reconstruction from candidate stencils of incremental width, separates smooth from non-smooth stencils by a strongly scale-separated measure and a sharp cut-off, and combines the surviving stencils with their renormalized linear weights, so that smooth regions recover the background linear scheme exactly; this page gives the standard recipe, its parameters, variants and recorded disagreements."
status: established
aliases: [TENO, targeted essentially non-oscillatory scheme, TENO5, TENO6, TENO7, TENO8]
tags: [teno, reconstruction, finite-difference, low-dissipation, turbulence]
timestamp: 2026-10-21T12:00:00Z
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
[Fu (2021)](/sources/fu-2021.md), §§2–3). This is the defining difference from
WENO, where every stencil contributes with a smoothness-dependent weight, and from
ENO, which keeps only the smoothest stencil and cannot recover the full-stencil
optimal accuracy (Fu 2023, §2.3).

## The standard recipe (finite difference)

The setting is the conservative finite-difference scheme on split point fluxes
$f^\pm$ (see [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
and [Lax–Friedrichs flux splitting](/methods/lax-friedrichs-flux.md)); only the
upwind-biased reconstruction of $f^+$ is written, the other by mirror symmetry
about $x_{i+1/2}$.

**1. Candidate stencils of incremental width.** The widths are

$$\{r_k\}=\begin{cases}\{3,3,3,4,\dots,\tfrac{K+2}{2}\},&K\ \text{even},\\ \{3,3,3,4,\dots,\tfrac{K+1}{2}\},&K\ \text{odd},\end{cases}\qquad k=0,\dots,K-3,$$

(Fu 2023, Eq. (5); Ye et al., Eq. (1)). TENO numbers stencils differently from
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
$S_k$ and $\tau_K$ a smoothness measure of the full $K$-point stencil. On this
page the subscript of $\tau_K$ is the full-stencil size $K$, as in the sources,
not the order that the registry's subscript of $\tau$ carries (page-local
convention; $\tau_K$ is of order 6 for every $K\ge6$ below). Ye et al.
note the same form covers WENO-Z ($C=1$) and WENO-CU6 ($C=20$), with $q=2$ in
"most WENO schemes". The global indicators used are:

- $K=5$: $\tau_5=\lvert\beta_1-\beta_2\rvert$, the WENO-Z $\tau_5$ in TENO's
  labelling (the two outer stencils) (Takagi et al., §2.2; Ye et al., Eq. (24),
  with $\tau_5=O(\Delta x^5)$ and $\tau_5/(\beta_k+\epsilon)=O(\Delta x^3)$, Eqs. (25)–(27));
- $K\ge6$: $\tau_K=\big\lvert\beta_K-\tfrac16(\beta_1+\beta_2+4\beta_0)\big\rvert=O(\Delta x^6)$,
  with $\beta_K$ the indicator of the full stencil (the WENO-CU6 form; Fu 2023,
  Eq. (18); Ye et al., Eqs. (28)–(32), (39), with the 6-point $\beta_K$ printed in
  full in Eq. (29)).

**3. Normalization and sharp cut-off.**

$$\chi_k=\frac{\gamma_k}{\sum_l\gamma_l},\qquad
\delta_k=\begin{cases}0,&\chi_k<C_T,\\1,&\text{otherwise}\end{cases}$$

(Fu 2023, Eqs. (8)–(9); Takagi et al., Eqs. (11)–(12)).

**4. Renormalized linear weights.** $\omega_k=d_k\delta_k/\sum_ld_l\delta_l$
(Fu 2023, Eq. (10)). For TENO5 $d_0=6/10$, $d_1=3/10$, $d_2=1/10$, the
fifth-order upwind scheme in TENO labelling (Takagi et al., Eq. (13)); for TENO7
$d=(18,9,3,4,1)/35$ (Ye et al., Eq. (4)). The $d_k$ can instead be chosen by
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
| $10^{-5}$ | TENO5 default | Takagi et al., §4 |
| $10^{-4}$ | removes a small contact overshoot of TENO-THINC on the blast wave at very high resolution | Takagi et al., §4.5, Fig. 9 |
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
  (Fu 2023, §2.5, Figs. 2–3; Takagi et al., §2.2).
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
  broadband turbulence, which is TENO's motivation. Yet standard TENO is "still
  excessively dissipative" for high-wavenumber physical fluctuations, because
  high-order undivided differences respond both to such fluctuations and to
  discontinuities ([Fu (2021)](/sources/fu-2021.md), §3.4; Fu 2023, §4.1).
- **Steady states.** Residuals of WENO stall at truncation-error level because of
  slight post-shock oscillations, and TENO behaves the same way, "an open problem"
  (Fu 2023, §4.2).
- **Cost.** TENO6-A costs 17% more than WENO5-JS on GPU and 47% more on CPU
  (Fu 2023, §5.4); TENO5 costs 810 ms against 696 ms for WENO5-Z per step on a
  $512\times128$ double Mach reflection (Takagi et al., Table 3).

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
- **Finite-volume TENO** shares the reconstruction subroutine with the finite
  difference one; TENO5-LFV switches between a low-dissipation flux (central or
  HLLC) where both full stencils are smooth and HLL otherwise, which improves wave
  resolution and avoids the carbuncle (Fu 2023, §3.6, Eq. (30); see
  [HLL-family solvers](/methods/hll-riemann-solvers.md) and
  [carbuncle](/definitions/carbuncle-phenomenon.md)).
- **Unstructured TENO** (Fu 2023, §3.9): one large central-biased stencil used
  alone when smooth, otherwise an *equal-weight* average of the smooth small
  directional third-order stencils; up to sixth order in 3D.
- **Very high order and adaptive order**: TENO8-AA, TENO10-AA and TENO-A, see
  [adaptive TENO](/methods/adaptive-teno.md); **TENO-THINC**, see
  [TENO-THINC](/methods/teno-thinc.md); **AFTENO**, see
  [AFTENO](/methods/afteno.md); **compact TENO** (TCNS, WCNS-T), see
  [WCNS](/methods/weighted-compact-nonlinear-scheme.md); learned weights with a
  TENO cut-off layer, see [learned WENO weights](/methods/learned-weno-weights.md).

## Qualifications

- "$K$-point TENO is $K$th order" (Fu 2023, §2) holds when the $d_k$ are chosen
  for maximum order; the spectrally optimized TENO8-AA and TENO10-AA of
  [Fu (2021)](/sources/fu-2021.md) are of order 6 and 8, and Fu (2023, §3.1)
  itself calls TENO10 a "10-point 8th-order" scheme.
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
al.'s rate is the one that smooth WENO-Z-type weights need.)*

# Citations

- [Fu (2023)](/sources/fu-2023.md) — §§1–5, Eqs. (2)–(33), Figs. 1–9: the review of the family.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §2.2, Eqs. (5)–(14), Table 2, Table 3: TENO5 recipe, order, cost.
- [Ye et al. (2022)](/sources/ye-2022.md) — §2, Eqs. (1)–(10); §3.3–3.5, Eqs. (24)–(39); §4.5, §4.7: stencils, $\tau_K$, $q$ and $C_T$ tests.
- [Fu (2021)](/sources/fu-2021.md) — §§2–3.4: TENO background, dissipation of standard TENO.
