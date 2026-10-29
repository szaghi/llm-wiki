---
type: Software
title: "PHengLEI"
description: "PHengLEI is the compressible multi-block structured-grid solver of the China Aerodynamics Research and Development Center; this page records the finite-difference numerics, nonlinear weights, time integration and turbulence treatments (SATES variants, SST-IDDES and AIDDES, Smagorinsky LES) with which four bundle sources run high-lift airfoils, cylinders and a supersonic base flow in it."
status: established
aliases: [PHengLEI solver, CARDC PHengLEI]
tags: [software, hybrid-rans-les, numerical-dissipation, compressible, separated-flow]
timestamp: 2026-10-29T07:36:00Z
---

# PHengLEI

**PHengLEI** is the compressible flow solver of the China Aerodynamics
Research and Development Center (CARDC), described by the first two bundle
sources that use it as "a cell-central finite differencing formulation based on
multi-block structured grids" ([Wu et al. 2023](/sources/wu-2023-b.md),
§2.2; [Wu et al. 2024](/sources/wu-2024.md), §2.4, both citing the code's
own reference), and in the same words by the group's third paper,
[Wu et al. (2024b)](/sources/wu-2024-b.md), §IV.C. In the bundle it is the host of
[self-adaptive turbulence eddy simulation](/methods/self-adaptive-turbulence-eddy-simulation.md)
(SATES) and of its σ-model variant, run with the fourth-order
[weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md)
(WCNS) on the [30P30N high-lift airfoil](/benchmarks/30p30n-high-lift-airfoil.md)
and on canonical validation flows, and of the smooth TENO-type weights of
Wu et al. (2024b) for the same closure. The group's fourth paper,
[Wu et al. (2026)](/sources/wu-2026-b.md), §3.4, runs the high-order
branch PHengLEI-HyOrder, described there as a cell-centred finite
differencing solver on multi-block structured grids and cited to a 2025
paper of the group in the Aeronautical Journal that the bundle has not
ingested. None of the sources gives the code's parallelization or licence;
cost is reported as CPU hours relative to one scheme (Wu et al. 2024b) or as wall-clock hours on stated core counts (Wu et al. 2026; below).

## Numerics as the sources configure them

**Convective terms: WCNS.** Wu et al. (2023) and Wu et al. (2024) use the fourth-order explicit WCNS
of Deng & Zhang (2000, which they cite): an explicit flux difference

$$f'_j=\frac{\alpha_{\mathrm W}}{h}\big(f^*_{j+1/2}-f^*_{j-1/2}\big)+\frac{b_{\mathrm W}}{h}\big(f^*_{j+3/2}-f^*_{j-3/2}\big),\qquad \alpha_{\mathrm W}=\tfrac98,\ b_{\mathrm W}=-\tfrac1{24},$$

with $\alpha_{\mathrm W}$, $b_{\mathrm W}$ the flux-difference coefficients
of weighted compact nonlinear schemes (registry §11), $f$ the convective
flux (page-local), $f^*_{j+1/2}$ the Roe flux of interpolated interface states
and $h$ the grid spacing (Wu et al. 2023, Eq. 12; Wu et al. 2024, Eq. 14).
The interpolation is fifth order:

- Wu et al. (2023, Eq. 14) use WENO-Z-type weights with regularization
  parameter $\epsilon_{\mathrm Z}=10^{-6}$ (WCNS-Z) or $\epsilon_{\mathrm Z}=100$
  (WCNS-L, nearly linear);
- Wu et al. (2024, Eq. 15) use linear weights only (WCNS-E-4 "to reduce the
  numerical dissipation"), with the left interface state
  $\hat u^L_{j+1/2}=(3u_{j-2}-20u_{j-1}+90u_j+60u_{j+1}-5u_{j+2})/128$ and its
  mirror for the right state.

*(Compiler check, not in the sources: $\alpha_{\mathrm W}+3b_{\mathrm W}=1$, the
consistency condition of the flux difference, and the five interpolation
weights sum to one.)* Both papers state that the WCNS satisfies the
[geometric conservation law](/properties/geometric-conservation-law.md) on
curvilinear grids, citing two GCL works, without printing a free-stream
test. Viscous terms are fourth-order central differences in both.

**A sixth-order flux difference with TENO-type weights.** Wu et al.
(2024b, §II.B, Eq. 10) run the fifth-order WCNS with an explicit
sixth-order midpoint flux difference, coefficients $75/64$, $-25/384$ and
$3/640$ on the interface-flux differences at distances $1/2$, $3/2$ and
$5/2$ (for $E=x$ the printed coefficients give
$75/64-75/384+15/640=1$, *compiler check, not in the sources*), a Roe
flux, and
nonlinear interpolation on characteristic variables with Jiang–Shu,
Z-type, TENO-type (sharp cut-off $C_T=10^{-5}$), smooth-cutoff and
adaptive smooth-cutoff weights (Eqs. 11–23); the weights are on
[weighted compact nonlinear schemes](/methods/weighted-compact-nonlinear-scheme.md)
and [WENO and hybrid schemes](/methods/weno-scheme.md). Their motivation is
specific to PHengLEI's implicit time integration: the sharp TENO cut-off
makes the weights discontinuous for marginally resolved turbulence, which
the authors hold responsible for poor convergence of the Newton-like
sub-iterations. In the supersonic base-flow runs the sub-iteration
residual falls by about one order with the sharp cut-off, three with the
smooth one and two with the adaptive one (§IV.C.2, Fig. 13); on the 30P30N
the sharp cut-off also converges worse (Fig. 9). Cost in CPU hours
normalized by the Jiang–Shu weights (Table I): linear 0.97, Z 1.03,
TENO-type 1.51, smooth 1.52, adaptive smooth 1.68 on the 30P30N; Z 1.02,
TENO-type 1.58, smooth 1.55, adaptive smooth 1.54 on the base flow.

**PHengLEI-HyOrder: a sixth-order WCNS with adaptive Roe dissipation.**
Wu et al. (2026, §3.1–§3.4) interpolate primitive variables with a
sixth-order WCNS of multi-order candidates (MOC6): three third-order
candidates and one sixth-order optimized linear candidate on
a six-point stencil, with linear weights $d_k=(1/16,\,10/16,\,5/16,\,100)$,
indicators "given by Ma et al. (2024)" (not printed) and
$\epsilon_{\mathrm Z}=10^{-40}$, and they add the smooth tanh cut-off of
Wu et al. (2024b) with an adaptive $C_T$ (MOC6-STA, Eqs. 22–25; on the
[WCNS page](/methods/weighted-compact-nonlinear-scheme.md)). The Roe flux
carries a dissipation coefficient built per variable from a
total-variation indicator and the Ducros factor (Eqs. 27–28; see
[shock sensors](/definitions/shock-sensor.md)). Viscous terms are
fourth-order central, the turbulence-model equations use a "classical
second-order upwind scheme", time integration is second-order backward
differentiation with LU-SGS and Newton-like sub-iterations, and DES, DDES
and IDDES are available in their SST versions (§3.4).

**Lower-order alternatives** used to show the effect of
[numerical dissipation](/properties/numerical-dissipation.md):

- a blended central/upwind second-order scheme (BCD) with upwind fraction
  $\sigma_b=0.02$ (Wu et al. 2023, Eq. 15, §2.2.2);
- a MUSCL scheme with a second-order flux difference and a smooth van
  Leer-type limiter with $\varepsilon\approx10^{-6}$ (Wu et al. 2024, Eqs.
  16–17), called third order in §2.4 and second order in §4, with both
  wordings in §3.2 (see Qualifications).

**Time integration.** Second-order backward differentiation with implicit
LU-SGS and Newton-like sub-iterations, for the Navier–Stokes and the
turbulence-model equations alike; unsteady runs restart from a converged
RANS solution (Wu et al. 2023, §2.2; Wu et al. 2024, §2.4).

## Turbulence treatments

- **SATES** with constant cut-off coefficient $C_x=0.61$ (called SATES-SM by
  Wu et al. 2024): the BSL [$k$-$\omega$](/methods/k-omega-sst-model.md)
  equations with the eddy viscosity multiplied by the resolution control
  function $F_r$ (Wu et al. 2023, Eqs. 4–7).
- **SATES-σ**, which makes $C_x$ local through a
  [σ-model](/methods/sigma-model.md) factor (Wu et al. 2024, Eqs. 8–11).
- **SST-IDDES** of Gritskevich et al. (2012) as the
  [detached-eddy simulation](/methods/detached-eddy-simulation.md)
  comparator (Wu et al. 2023, 2024).
- **SATES-II** and **AIDDES**: a two-layer cut-off coefficient, WALE-type
  near walls and σ-model-based outside, used in SATES on an SST host and as
  the LES coefficient of SST-IDDES (Wu et al. 2026, §2.2–§2.3; see
  [SATES](/methods/self-adaptive-turbulence-eddy-simulation.md)).
- **Smagorinsky LES** with $C_s=0.1$, $\Delta=(\Delta_x\Delta_y\Delta_z)^{1/3}$
  and no wall damping mentioned ([Smagorinsky model](/methods/smagorinsky-model.md);
  Wu et al. 2023, Eq. 8).

## Studies run with it

| Study | Flow | Grid | Result reported |
|---|---|---|---|
| Wu et al. (2023), §3 | modified 30P30N, $Re_c=1.71\times10^6$, $M=0.17$, $\alpha=5.5^\circ$ | 7.2M, 19M, 27M cells | SATES with WCNS-L gives $C_L$ within 3% of the measured 2.83 on all grids; BCD $-11.0\%$, WCNS-Z $-6.7\%$, LES $-6.7\%$, IDDES $-19.8\%$ (Table 2) |
| Wu et al. (2024), §3.1a | [channel flow](/benchmarks/turbulent-channel-flow.md), $Re_\tau=395$ | $64\times96\times64$, $128\times120\times64$ | mean velocity agrees with DNS on the finer grid |
| Wu et al. (2024), §3.1b | [square cylinder](/benchmarks/square-cylinder-flow.md), $Re_D=2.2\times10^4$ | 0.66M, 1.73M cells | mean and resolved normal stresses agree with DNS and LDV |
| Wu et al. (2024), §3.2 | [circular cylinder](/benchmarks/circular-cylinder-wake.md), $Re_D=3\times10^6$ | about 6.7M cells | SATES-σ with WCNS gives $C_D=0.55$, $St=0.24$; with MUSCL $C_D=1.26$ (Table 3) |
| Wu et al. (2024), §3.3 | MD-30P30N, $Re_c=9\times10^6$, $M=0.2$, $\alpha=8$–$24^\circ$ | 12.8M, 26.4M cells | total lift error of SATES-σ "always less than 6.5%, even at post-stall conditions" |
| Wu et al. (2024b), §IV.C.1 | modified 30P30N, $Re_c=1.71\times10^6$, $M=0.17$, $\alpha=5.5^\circ$, SATES | about 27M cells | Jiang–Shu weights deviate in flap $C_p$ and suppress the slat-cove shear-layer instability; TENO-type and smooth weights agree with experiment and with the linear WCNS (Figs. 7–10) |
| Wu et al. (2026), §2.4 | zero-pressure-gradient flat plate, $M=0.2$, $Re=5\times10^6$ per unit length | $137\times97\times97$ | SATES-II and AIDDES recover the SST skin friction, SATES-SM under-predicts it (Fig. 1) |
| Wu et al. (2026), §4.1 | [supersonic axisymmetric base flow](/benchmarks/supersonic-axisymmetric-base-flow.md), $M_\infty=2.46$ | $5.07$ M and $9.5$ M cells, four grids | recirculation length $L_r/R$: SATES-SM 3.17, SATES-II 2.81, IDDES 3.58, AIDDES 2.81, experiment 2.63; 45–52 wall-clock hours on 640 cores (Table 3) |
| Wu et al. (2026), §4.2 | MD-30P30N, $Re_c=9\times10^6$, $M=0.2$, $\alpha=21^\circ$ | about 4.26 M and 27 M cells | SATES-SM separates prematurely on the slat; SATES-II and AIDDES improve the near-wall and downstream profiles (Figs. 12–14) |
| Wu et al. (2024b), §IV.C.2 | supersonic axisymmetric base flow of Herrin & Dutton, $M_\infty=2.46$, SATES | about 7M and 42M cells | on the coarse grid the adaptive smooth weights give the best resolved-TKE peaks, against Jiang–Shu weights on the fine grid as numerical reference (Fig. 14) |

Both groups of results lead the authors to the same conclusion on the
scheme: the low-dissipation (linear-weight) WCNS is needed, and the more
dissipative options (BCD, Z-type weights, MUSCL) delay shear-layer
instability; on the cylinder MUSCL fails to reproduce the delayed
separation of the supercritical regime (Wu et al. 2024, §3.2, Figs. 13–17).

## Qualifications

- The descriptions of the code come from four papers of the same group,
  all users of SATES with WCNS; the code's own reference is cited but not
  ingested.
- Wu et al. (2024b, Table I) give the adaptive smooth weights a lower
  base-flow cost (1.54) than the smooth ones (1.55), while their Appendix
  says the adaptive variant costs "a slightly further increase" over the
  smooth one, which holds for the 30P30N (1.68 against 1.52). The
  sub-iteration counts per step are not stated in the text.
- Wu et al. (2024) print the MUSCL interpolation as "third-order" (§2.4)
  and the scheme as "second-order MUSCL" (§3.2, §4), with a second-order
  flux difference (Eq. 16); §3.2 also writes "The third-order MUSCL and
  high-order WCNS-E-4 schemes were compared".
- Wu et al. (2024) print the 30P30N grids as 12.8M and 26.4M cells (§3.3)
  and "approximately 24 million cells" for the relatively coarse grid in
  §4.

# Citations

- [Wu et al. (2023)](/sources/wu-2023-b.md) — §2.2 (solver, WCNS, BCD, time integration), Eqs. 4–8, 12–15, §3, Table 2.
- [Wu et al. (2024)](/sources/wu-2024.md) — §2.3–§2.4 (WCNS-E-4, MUSCL, solver), Eqs. 8–17, §3, Table 3, §4.
- [Wu et al. (2026)](/sources/wu-2026-b.md) — §2.2–§2.4 (SATES-II, AIDDES, flat plate); §3.1–§3.4, Eqs. (22)–(28) (MOC6-STA, adaptive Roe dissipation, PHengLEI-HyOrder configuration); §4.1–§4.2, Tables 2–3 (base flow and 30P30N runs, cost).
- [Wu et al. (2024b)](/sources/wu-2024-b.md) — §II.B–§II.D, Eqs. (10)–(23) (sixth-order flux difference, nonlinear weights); §IV.C.1–§IV.C.2, Figs. 7–14 (30P30N and base flow in PHengLEI, sub-iteration convergence); Table I, Appendix (cost).
