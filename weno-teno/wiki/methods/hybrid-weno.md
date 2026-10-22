---
type: Method
title: "Hybrid central-WENO schemes"
description: "Hybrid schemes use a cheap linear (central or optimal upwind) reconstruction where a sensor declares the stencil smooth and switch to a nonlinear WENO or TENO reconstruction elsewhere; they cut dissipation and cost, but their quality hinges on the sensor, which the sources call case- and parameter-sensitive unless it is built from the TENO cut-off flags."
status: established
aliases: [hybrid WENO, hybrid central/WENO, hybrid compact-WENO, hybrid TENO, hybrid linear–nonlinear scheme]
tags: [weno, teno, reconstruction, low-dissipation, turbulence, limiting]
timestamp: 2026-10-22T00:00:00Z
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
