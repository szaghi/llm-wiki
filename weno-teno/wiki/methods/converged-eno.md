---
type: Method
title: "Converged ENO (CENO)"
description: "Converged ENO is a TENO-type reconstruction for steady flows whose stencil flags remember the previous step through a hysteretic cut-off and are frozen when the global indicator falls below the mesh width, with a prioritized fifth-order or third-order choice, so that steady residuals can fall to machine zero."
status: established
aliases: [CENO, converged ENO scheme, finite-volume converged ENO, CENO-AMR]
tags: [teno, reconstruction, finite-volume, limiting]
timestamp: 2026-10-23T20:37:00Z
---

# Converged ENO (CENO)

The **converged ENO** (CENO) scheme is a nonlinear reconstruction built from the stencil
selection of [targeted ENO](/methods/targeted-eno.md) for steady-state computations. Its
premise is that high-order shock-capturing schemes fail to drive the steady residual to machine
zero because the *reconstruction formula* at a spatially fixed interface (which stencils are
kept, which weights they get) keeps changing from one time step to the next. CENO therefore
makes the cut-off of each stencil depend on whether that stencil was kept at the previous step
(a hysteresis), freezes the flags altogether when the data are judged noise, and chooses between
only two formulas, the full-stencil linear scheme and a reduced one. The scheme was introduced in
finite differences by Liang & Fu (J. Comput. Phys. 519:113386, 2024, cited as their ref. [1]; not ingested);
[Liang & Fu (2026)](/sources/liang-2026.md) give its finite-volume form and couple it with
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md) (CENO-AMR). Everything below is
the finite-volume form of Liang & Fu (2026).

## Why steady residuals stall

Liang & Fu (2026, §1, §3.2.3) attribute the stall, following the finite-difference paper, to "the
unsteady effect of shock-induced numerical instability on the nonlinear weighting process as well
as the resultant variation of the numerical formula for the spatially fixed cell interface flux at
different time instants". They recall two earlier remedies, a modified smoothness indicator of
Zhang & Shu and the upwind-biased evaluation of the eigenvectors of Zhang, Jiang & Shu, which
reduce the residual to machine zero "in many test problems" but not "when encountering strong
shocks passing through the boundaries", and state that post-shock-oscillation-removal schemes,
among them the steady hybrid WENO-H of [Wan & Xia (2022)](/sources/wan-2022.md), still fail for
some 2D problems with shock interactions and reflections (§1, §3.2.3). Wan & Xia themselves
report residuals of $10^{-12}$ to $10^{-14}$ on all fourteen of their steady tests, which include
flows past plates and square columns and a forward-facing step
([hybrid schemes](/methods/hybrid-weno.md)); Liang & Fu do not run WENO-H, so the two claims are not
tested against each other.

In finite volumes the authors see an extra cause: unlike finite differences with a global
Lax–Friedrichs splitting before the reconstruction, there is no preliminary dissipative step, so
small noise from mesh adaptation and from shocks passing through smooth regions is "magnified
exponentially due to the power function" of the TENO measure and switches the formula
unnecessarily (p. 7).

## Stencils and measure

Liang & Fu (2026, §3.2.1, Eqs. (12)–(16)) use one five-point stencil $S_0=\{I_{i-2},\dots,I_{i+2}\}$
and two two-point stencils $S_1=\{I_{i-1},I_i\}$, $S_2=\{I_i,I_{i+1}\}$ (the source's numbering,
$S_0$ the large stencil, not the most upwind one). The left states at $x_{i+1/2}$ are

$$u^{(0)}=\tfrac1{60}\big(2\bar u_{i-2}-13\bar u_{i-1}+47\bar u_i+27\bar u_{i+1}-3\bar u_{i+2}\big),\qquad
u^{(1)}=\tfrac12\big(3\bar u_i-\bar u_{i-1}\big),\qquad u^{(2)}=\tfrac12\big(\bar u_i+\bar u_{i+1}\big),$$

the fifth-order linear finite-volume value and the two linear (degree-1, second-order accurate) extrapolations
*(compiler check, not in the sources, for the order of the two-point candidates)*;
the right state follows by mirror symmetry about $x_{i+1/2}$. The reconstruction acts on
[characteristic variables](/methods/characteristic-decomposition.md) (§2, Remark 1). The TENO measure
is (Eqs. (17)–(20))

$$\gamma_k=\Big(1+\frac{\tau_{\mathrm C}}{\beta_k+\epsilon}\Big)^6,\qquad
\chi_k=\frac{\gamma_k}{\sum_{l=0}^2\gamma_l},\qquad\tau_{\mathrm C}=\big\lvert2\beta_0-(\beta_1+\beta_2)\big\rvert,\qquad\epsilon=10^{-8},$$

with the Jiang–Shu $\beta_0$ of the quartic and squared differences for $\beta_1,\beta_2$; the
registry measure with $C=1$, $q=6$, and a global indicator $\tau_{\mathrm C}$ (page-local) that is not the WENO-Z
$\tau_5$. Its expansion, $\tau_{\mathrm C}=\big\lvert(\tfrac23u'u'''-\tfrac53u''^2)\Delta x^4+O(\Delta x^6)\big\rvert$,
and the printed slip in the expansions of the $\beta_k$ are on
[smoothness indicators](/definitions/smoothness-indicator.md).

## Converged stencil selection

**Hysteretic cut-off** (§3.2.3, Eq. (21)). With $\tilde\delta_k$ the flag of stencil $k$ at the
previous reconstruction (page-local), a temporary flag is set by a stencil-wise cut-off,

$$\hat\delta_k=\begin{cases}0,&\chi_k<C_{T,k},\\1,&\text{otherwise},\end{cases}\qquad
C_{T,k}=\begin{cases}10^{-1},&\tilde\delta_k=0,\\10^{-10}\ (S_0)\ \text{or}\ 10^{-8}\ (S_1,S_2),&\tilde\delta_k=1.\end{cases}$$

A stencil discarded at the previous step must pass a much stricter test to be readmitted, an
adopted one a much looser test to stay; the values are taken from earlier TENO work
([Liang & Fu (2026)](/sources/liang-2026.md), pp. 6–7). The authors state that, although the
hysteresis makes the selection "insensitive to the smoothness indicator visually", stable shock
capturing is kept "due to the strong scale separation properties" of the measure (p. 7). All
flags are initialized as smooth (§5).

**Noise filter** (§3.2.3, Eq. (24)). The final flags are

$$\delta_k=\begin{cases}\tilde\delta_k,&\tau_{\mathrm C}<\Delta x,\\\hat\delta_k,&\text{otherwise},\end{cases}\qquad k=0,1,2,$$

so the previous selection is kept whenever the global indicator is below the local mesh width.
Because $\Delta x$ is the width of the cell at its level, the threshold is level dependent on the
adaptive grid ("scale-adaptive filtering in multi-resolution grids", p. 9). The authors prefer
$\tau_{\mathrm C}$ to the $\beta_k$ for this test because the $\beta_k$ have little contrast between smooth and
non-smooth flow and their leading term depends only on $u'$ (§3.2.3).

**Prioritized reconstruction** (§3.2.4, Eqs. (25)–(26)). If $\delta_0=1$, the fifth-order value
$u^{(0)}$ is used alone. Otherwise

$$u^-_{i+1/2}=\omega_1u^{(1)}+\omega_2u^{(2)},\qquad\omega_k=\frac{d_k\delta_k}{d_1\delta_1+d_2\delta_2},\qquad d_1=\tfrac13,\ d_2=\tfrac23,$$

the third-order linear scheme on $\{I_{i-1},I_i,I_{i+1}\}$ if both survive and the single surviving
linear candidate if one is dropped, "such that the ENO property is achieved"
([ENO property](/definitions/eno-property.md)). The authors contrast this with the convex
combination of WENO and with the incremental-stencil TENO, which blends several stencils; CENO
never blends $S_0$ with the small stencils. *(Compiler check, not in the sources: the paper does
not treat $\delta_0=\delta_1=\delta_2=0$, where the denominator vanishes; it cannot occur, because
the three $\chi_k$ sum to one, so one of them is at least $\tfrac13$, above every cut-off
($\le10^{-1}$), and the filter only reuses flags produced in the same way from an all-smooth start.)*

The same two-level pattern, the large stencil alone or a reduced combination of small stencils,
is used by the unstructured TENO of Ji, Liang & Fu and by TENO-E
([Liang et al. (2025)](/sources/liang-2025.md); [targeted ENO](/methods/targeted-eno.md)); what is
specific to CENO is the dependence of the cut-off and of the flags on the previous step.

## Multi-dimensional scheme and mesh adaptation

The 2D scheme reconstructs dimension by dimension at face midpoints, uses the HLLC flux
([HLL-family solvers](/methods/hll-riemann-solvers.md)) and the mid-point rule for the face
integrals, and is therefore "overall-speaking second-order" for nonlinear multi-D problems, which
the authors state; they recall from Zhang, Zhang & Shu that mid-point and Gaussian finite-volume WENO
give comparable results on non-smooth problems, and keep the 1D reconstruction fifth order
(§4.1, Eq. (30), Algorithm 1). Time stepping is second-order
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) with local time stepping at CFL 0.4 (§5).

CENO is coupled with Harten's cell-average multiresolution on a pyramid of blocks. The adaptation
criterion reuses the $\beta_k$ through a detection variable $\chi_{\mathrm d}\in(0,1]$ (page-local,
written out on [smoothness indicators](/definitions/smoothness-indicator.md)): a block is refined if
any cell has $\chi_{\mathrm d}<0.3$, coarsened if all cells have $\chi_{\mathrm d}>0.7$, and left unchanged
otherwise, so that the band between the thresholds freezes the mesh at steady state; and the
residual of the time-varying mesh is computed on a fixed virtual root level obtained by recursive
coarsening of the leaves (§3.3, §4.2, Eqs. (27)–(28), (31)). The authors hold that conventional
adaptation criteria keep refining and coarsening at steady state and so change the reconstruction
formula, which is the same mechanism as above (§1, §3.3). Details are on
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).

## Evidence

All tests are steady Euler problems with $\gamma=1.4$, compared with finite-volume WENO5-Z and
TENO5 on uniform meshes ([steady shock problems](/benchmarks/steady-shock-problems.md);
Liang & Fu 2026, §5):

- **1D stationary shock**, Mach 2, finest $N=512$: all schemes reach near machine zero, CENO-AMR
  with the lowest residual during the run (§5.1, Fig. 5; no values printed).
- **2D steady shocks** (oblique shock, regular shock reflection, supersonic flow past a plate at
  $25^\circ$, multiple shock reflection): only the CENO-AMR residual settles at machine-zero level,
  and WENO5-Z and TENO5 show post-shock oscillations; compression ratios above 90% (§§5.2–5.4, 5.7).
- **Shock interactions**: heterolateral, CENO-AMR residual "around $10^{-13}$" against "around $O(1)$"
  for WENO5-Z and TENO5; ipsilateral, machine-zero level against "around $10^{-1}$" (§§5.5–5.6).
- **Insensitivity** of the results to the adaptation thresholds over five pairs from $(0.2,0.6)$ to
  $(0.35,0.8)$ (Figs. 9–10, 14–15).
- **Cost** (user CPU time at the finest effective resolution, ratio to WENO5-Z): 0.408 (1D shock),
  0.277 (oblique shock), 0.252 (regular reflection), 0.163 (plate), 0.528 (heterolateral) and 0.425
  (ipsilateral), with TENO5 at 1.003 to 1.412 (Table 1); no hardware, core count or compiler is printed.

## Qualifications

- The causal thesis, formula variation at fixed interfaces rather than post-shock oscillations, is
  the authors' own, carried over from their finite-difference paper; it is supported here by the
  residual histories, not by an analysis that separates the two causes.
- The comparators run on uniform meshes without adaptation and their parameters are not printed,
  so the residual and cost gains combine the effect of the selection and of the mesh adaptation;
  no run of CENO on a uniform mesh, or of WENO5-Z with adaptation, is shown.
- "Fifth order" refers to the 1D reconstruction; all 2D results, including compression ratios and
  CPU savings, belong to a second-order (mid-point) finite-volume scheme, as the authors state.
- The text gives one symbol, $C_{T1}$, two values ($10^{-10}$ and $10^{-8}$, for the large and the
  small stencils, p. 7), where Eq. (21) defines one; the page writes the stencil-wise values.
- The paper calls the quartic of $S_0$ a "fifth-order polynomial" and the linear candidates
  "second-order polynomials", order-of-accuracy wording for degrees 4 and 1.

# Citations

- [Liang & Fu (2026)](/sources/liang-2026.md) — §1; §3.2.1–3.2.4, Eqs. (12)–(26); §3.3, Eqs. (27)–(28); §4.1–4.2, Eqs. (30)–(31), Algorithm 1; §5, Figs. 5–26, Table 1: finite-volume CENO, hysteretic cut-off, noise filter, prioritized reconstruction, CENO-AMR and its steady-state evidence.
- [Wan & Xia (2022)](/sources/wan-2022.md) — §3–§4: steady hybrid WENO-H, residuals on its own steady tests (cited by Liang & Fu among the earlier remedies).
- [Liang et al. (2025)](/sources/liang-2025.md) — §3.3.3, Eqs. (22)–(27): the same two-level structure without history dependence.
