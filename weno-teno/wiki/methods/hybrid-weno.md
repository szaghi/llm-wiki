---
type: Method
title: "Hybrid central-WENO schemes"
description: "Hybrid schemes use a cheap linear (central or optimal upwind) reconstruction where a sensor declares the stencil smooth and a nonlinear WENO or TENO reconstruction elsewhere, sometimes with a smooth transition band; they cut dissipation and cost or help steady convergence, but their quality hinges on the shock sensor, whose misjudgments the sources measure."
status: established
aliases: [hybrid WENO, hybrid central/WENO, hybrid compact-WENO, hybrid TENO, hybrid linear–nonlinear scheme, WENO-H, MDAD-HY, TENO-HY, three-region hybrid]
tags: [weno, teno, reconstruction, low-dissipation, turbulence, limiting]
timestamp: 2026-10-23T10:00:00Z
---

# Hybrid central-WENO schemes

A hybrid scheme pairs a **linear** reconstruction, used where the solution is judged smooth, with a
**nonlinear** shock-capturing reconstruction, used elsewhere, and a **sensor** that decides between
them point by point. Luo & Wu (2021, §1) summarize the Li & Qiu strategy: indicators identify the
discontinuities; at a discontinuity or a steep gradient the nonlinear weights are turned on to give
the scheme the [ENO property](/definitions/eno-property.md); for a stencil smooth enough they are
turned off and the linear scheme is used. Two motives recur: lower numerical dissipation in smooth
regions, which matters for turbulence, and lower cost, since the linear scheme needs neither weights
nor, for systems, a [characteristic decomposition](/methods/characteristic-decomposition.md).

## Variants recalled in the sources

- **Hybrid compact-ENO/WENO.** Takagi et al. (2022, §1) recall Adams & Shariff's hybrid compact-ENO
  scheme for shock–turbulence interaction, Pirozzoli's conservative hybrid compact-WENO scheme and the
  characteristic-wise hybrid compact-WENO scheme of Ren et al. with a new flow sensor.
- **Freezing the nonlinear adaptation.** Fu (2021, §1) recalls Hill & Pullin's switch, which freezes
  the WENO adaptation when the ratio of the largest to the smallest smoothness indicator is below a
  problem-dependent threshold.
- **Hybrid TENO.** Fu (2023, §3.4, Eqs. (21)–(24)) recalls a hybrid that builds the sensor from the TENO
  scale separation itself. On four stencils, with $\gamma_k=(\beta_k+\epsilon)^{-q}$, $q=6$, where
  $\epsilon$ "also functions as a cut-off on the stencil smoothness", and $\chi_k=\gamma_k/\sum\gamma_l$,
  the flag is 0 (smooth) if $\chi_k>C_T$ for every $k$, with $C_T=5\times10^{-4}$, and 1 otherwise.
  Flag 0 selects the optimal linear scheme without characteristic decomposition, flag 1 the TENO6
  reconstruction. With SSP-RK3 the efficiency improves "by a factor of four", with unchanged shock
  capturing (reproduced 2-D Riemann configuration 12, Fig. 7). Because the indicator separates
  non-smooth scales in spectral space, Fu calls it "more universal" than physical sensors such as
  Ducros'. The same indicator has driven steepness-adjustable, minimized-dispersion and
  artificial-viscosity hybrids ([targeted ENO](/methods/targeted-eno.md)).
- **TENO-THINC.** Takagi et al. (2022, §3) also hybridize on TENO flags, but differently: in smooth
  regions the TENO5 flux restores the linear scheme anyway, and the flags select cells where THINC
  replaces TENO at genuine discontinuities. They contrast it with classical hybrids, which "dedicate
  to deploying the optimal linear scheme as much as possible in smooth regions" for efficiency
  (§3.2, item 4; [TENO-THINC](/methods/teno-thinc.md)).
- **Hybrid Hermite WENO.** In the moment-based [HWENO](/methods/hermite-weno.md) of Zhao, Chen &
  Qiu, made positivity-preserving by Fan, Zhang & Qiu (2021, §1, §4), a troubled-cell indicator
  selects the cells where the nonlinear HWENO reconstruction, preceded by a limiter on the first
  moment, replaces a linear Hermite reconstruction. With 0.97–19.57 % of cells flagged in their shock
  tests, the hybrid saves 59.05–89.64 % of the CPU time of the non-hybrid positivity-preserving HWENO
  (Table 4.2, hardware not stated), and the positivity limiter is triggered in identical fractions of
  cells in both (Table 4.2). The hybrid of Zhao et al. without positivity preservation blows up on
  their Examples 4.3–4.7 (Euler).

- **PDE-aware hybrids.** Balsara, Samantaray & Subramanian (2023, §6.3) recall Li & Ren's hybrid, which
  uses the central stencil wherever the solution is smooth and WENO only in troubled zones. Hong, Ye & Ye (2022, §1) recall Fu's TENO-based-indicator hybrid as the
  alternative to their own speed-up, which makes TENO itself cheaper instead
  ([targeted ENO](/methods/targeted-eno.md)).

## A dissipation-adaptive hybrid: MDAD-HY

Li, Chen & Ren (2022, §3) hybridize the six-point MDAD flux, a linear fourth-order flux whose
dissipation follows a [scale sensor](/definitions/scale-sensor.md), with its WENO-CU6-type counterpart
MDAD-WENO by a binary flag $\delta^{\mathrm H}_{i+1/2}$ (page-local; [MDCD schemes](/methods/mdcd-scheme.md)),
and compare four detectors on static data and in the approximate dispersion relation:

- **Harten's**, $1-|f_{i-1}-2f_i+f_{i+1}|/(|f_{i-1}-f_i|+|f_i-f_{i+1}|+\epsilon)$ against 0.3 (Eq. (47));
- **Ren et al.'s**, $\mathfrak s_i=(2\mathsf a\mathsf b+\epsilon)/(\mathsf a^2+\mathsf b^2+\epsilon)$ with the one-sided
  variations $\mathsf a=|f_i-f_{i-1}|$, $\mathsf b=|f_i-f_{i+1}|$ (page-local $\mathfrak s$, $\mathsf a$,
  $\mathsf b$), minimized over neighbouring points, $\epsilon=\tfrac{0.9\mathfrak s_c}{1-0.9\mathfrak s_c}\xi^2$,
  $\xi=10^{-3}$ (page-local), threshold $\mathfrak s_c=0.3$ (Eqs. (48)–(54));
- **Fu's TENO-based** one, $\gamma_k=(\beta_k+\epsilon)^{-6}$, $\epsilon=10^{-4}$, smooth iff every normalized
  $\chi_k$ exceeds $5\times10^{-4}$ (Eqs. (55)–(57));
- a **new** one: Ren's form with second differences added to the variations,
  $\mathsf a=|f_i-f_{i-1}|+|f_i-2f_{i-1}+f_{i-2}|$, $\mathsf b=|f_i-f_{i+1}|+|f_i-2f_{i+1}+f_{i+2}|$,
  $\xi=10^{-2}$, $\mathfrak s_c=0.4$ (Eqs. (58)–(60)); without $\epsilon$, $\mathfrak s_i=2/(\mathsf a/\mathsf b+\mathsf b/\mathsf a)$
  vanishes at extrema, where one first difference vanishes, and the second differences, which also jump
  at a discontinuity but vary little at an extremum, keep the ratio moderate.

On sine waves the new detector keeps the smooth flag up to $\vartheta=2.06$, Fu's only below 0.64, and
Harten's and Ren's fail "at very low wavenumbers" by flagging critical points; on a jump between two
sines only the new one separates the jump from both waves (Figs. 9–10). In the approximate dispersion
relation MDAD-HY recovers the linear scheme up to $\vartheta=2.06$, while TENO-HY and MDCD-HY show
irregular dissipation at low wavenumbers (Figs. 11–12;
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md)). Implementation
details matter: inputs normalized by $\max(|f_{\max}|,1)$ (after which TENO-HY detects "obviously
better" than in Fu's own paper), detection on density and entropy once per step, buffer zones of 1–3
points, and a second detection on each split characteristic flux at flagged interfaces (§3.4, §4.3.1).
Thresholds still vary by case: 0.5 for the blast waves, 0.8 for Sedov (§4.2).

## A three-region hybrid for steady states: WENO-H

Wan & Xia (2022, §3) argue that hybrid schemes are rarely used for steady problems "since the gap between
different kinds of approximations hinders the convergence of residue", and add a **transition region**.
With the Jiang–Shu indicators of the three stencils, the detector
$\mathfrak n=\tau_5/\big(\epsilon+\tfrac13\sum_k\beta_k\big)$ (page-local $\mathfrak n$; $\epsilon=10^{-6}$) is
$O(\Delta x^3)$ in smooth regions without critical points. A stencil is smooth for $\mathfrak n\le\tfrac12$
(fifth-order linear upwind reconstruction), non-smooth for $\mathfrak n\ge1$, and in transition between, where
the two reconstructions are blended by $M_{\mathrm t}(\mathfrak n)=\exp\!\big(-\tfrac{(2\mathfrak n-1)^2}{1-(2\mathfrak n-1)^2}\big)$
or the linear $2-2\mathfrak n$ (page-local $M_{\mathrm t}$; Eqs. (3.14)–(3.15)), which the authors call "essential for
the steady-state convergence" (no sharp-switch ablation shown). The non-smooth reconstruction uses the
[CWENO](/methods/cweno.md) stencils (a quartic and two linear polynomials) with linear weights
$(0.8,0.1,0.1)$ and WENO-ZQ-type weights whose ratio is divided by
$C_R=\big(\sum_{j=i-2}^{i+2}|u_j|\big)^2\Delta x+\beta_{\mathrm{opt}}+0.01$ (page-local; $\beta_{\mathrm{opt}}$ the quartic's indicator; Eqs. (3.2)–(3.4)), then blended with
the linear combination of the same polynomials so that its indicator stays bounded
([smoothness indicators](/definitions/smoothness-indicator.md)). WENO-H drives the average residue to
$10^{-12}$–$10^{-14}$ on all 14 steady tests, including flows past plates, square columns and a
[forward-facing step](/benchmarks/forward-facing-step.md), where CWENOZ or multi-resolution WENO stall in
some (§4; [multi-resolution WENO](/methods/multi-resolution-weno.md)); on smooth steady problems its errors
equal those of the linear scheme to every printed digit (Tables 4.1, 4.3).

## TENO-flag hybrids at discontinuities

Liang, Xiao, Shyy & Fu (2022) replace, in cells flagged by a detector built only from the TENO5 cut-off
flags, the TENO flux by a tanh interpolation; like [TENO-THINC](/methods/teno-thinc.md), this is a
hybrid whose second member is a jump reconstruction, not a linear scheme. They recall Hill & Pullin's
switch and WENO-RL as other hybrids (§1).

## Blends with a first-order flux

A second kind of hybrid blends a WENO flux with a **first-order** one through a limiter function,
rather than switching to a linear high-order scheme:

- In MFC, Bryngelson et al. (2021, §4.2.2, Eq. (34)) add an optional flux limiter, because "the WENO
  schemes we utilize are, in general, not TVD": the flux is the first-order (piecewise-constant)
  Riemann flux plus a limiter of the volume-fraction ratio
  $(\phi_i-\phi_{i-1})/(\phi_{i+1}-\phi_i)$ (upwinded with the contact velocity; page-local
  volume fraction $\phi_i$) times the difference between the WENO and first-order fluxes, with
  minmod, MC, ospre, superbee, Sweby, van Albada or van Leer limiters; the blend is described in words
  ([MFC](/software/mfc.md)).
- Matsushita & Aoki (2021, §3.1, Eqs. (26)–(27)) write the advective derivative as
  $f_x^{\mathrm{1st}}+\psi(r_i)\big(f_x^{\mathrm{WENO}}-f_x^{\mathrm{1st}}\big)$ with the minmod
  limiter $\psi$ of the upwinded slope ratio $r_i$ and third-order Hamilton–Jacobi WENO, to prevent
  instabilities at the steep density change of a gas–liquid interface.

Both are TVD-limiter hybrids localized at material interfaces
([TVD limiters](/definitions/total-variation-diminishing.md)), the counterpart of the
low-order/high-order flux blending used for bound preservation
([positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)).

## The sensor problem

Wang et al. (2021, §1), recalling Hu, Wang & Adams, call the hybrid method "minimally dissipative"
with "sharp shocks and well-resolved broadband turbulence", but say that it "relies on an appropriate
shock senor [sic]". Takagi et al. (2022, §1) state that hybrid schemes, although much less dissipative than their ENO or
WENO counterparts, depend in practice on the effectiveness of a shock sensor "which is mostly case
and parameter sensitive", and point to the parameter-free
[boundary variation diminishing](/definitions/boundary-variation-diminishing.md) selection as the
exception. Fu (2023, §3.4) recalls a systematic survey of shock sensors for hybrid schemes concluding
that hybrids generally perform better with a low-dissipation TENO than with WENO as the nonlinear
component, regardless of the sensor. Fu (2023, §5.4) also reports that the TENO6-A variant used for
transitional shock/boundary-layer interaction replaces the TENO discontinuity measure by a modified
Ducros sensor ([adaptive TENO](/methods/adaptive-teno.md)).

## Limits of the linear target

Luo & Wu (2021, §1) quote the common view behind hybridization: "the accuracy and resolution of the
upwind central are the limits of the improvement of the WENO scheme". They dispute it with WENO-Z+M,
whose nonlinear weights give smaller errors than the linear scheme UD5 itself on a smooth test
([WENO-Z+](/methods/weno-z-plus.md)). A hybrid cannot do better than its linear scheme in smooth
regions; the gain comes from the choice of that scheme, which TENO papers optimize spectrally
([approximate dispersion relation](/definitions/approximate-dispersion-relation.md)).

## Qualifications

- **Detector rankings depend on the test.** Fu (2023, §3.4) calls the TENO-based indicator "more
  universal" than physical sensors; Li, Chen & Ren (2022, Figs. 9–12) measure it correct only below
  $\vartheta=0.64$ on sine waves, with detector inputs normalized by $\max(|f_{\max}|,1)$, a step to which
  they attribute TENO-HY's better detection than in Fu's own paper (§4.3.1).
- Wan & Xia (2022, Example 4.3) state fifth order for all schemes on the isentropic vortex while their
  WENO-H orders are 2.42 ($L^\infty$) at $80^2$ and 8.19 at $160^2$, with an $L^1$ error at $80^2$ about 3.5
  times that of the linear UW5 (Table 4.2); their bound on the blended indicator is misstated (see
  [smoothness indicators](/definitions/smoothness-indicator.md)).
- The factor-four speed-up of the hybrid TENO is quoted from earlier work in a review; neither the
  hardware nor the share of flagged points is given in the review.

# Citations

- [Fu (2023)](/sources/fu-2023.md) — §1; §3.4, Eqs. (21)–(24), Fig. 7; §5.4.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1; §3.2.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §1; §5.3.1, Table 1.
- [Fu (2021)](/sources/fu-2021.md) — §1.
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §1; §4, Table 4.2.
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §4.2.2, Eq. (34).
- [Matsushita & Aoki (2021)](/sources/matsushita-2021.md) — §3.1, Eqs. (26)–(27).
- [Wang et al. (2021)](/sources/wang-2021.md) — §1.
- [Li, Chen & Ren (2022)](/sources/li-2022.md) — §3.2, Eqs. (46)–(60), Figs. 9–12; §3.4; §4.2–4.3.
- [Wan & Xia (2022)](/sources/wan-2022.md) — §1; §3, Eqs. (3.1)–(3.15), Algorithm 1, Remark 3.1; §4, Tables 4.1–4.3.
- [Liang et al. (2022)](/sources/liang-2022.md) — §1; §3.1–3.2.
- [Balsara, Samantaray & Subramanian (2023)](/sources/balsara-2023.md) — §6.3.
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §1.
