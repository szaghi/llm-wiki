---
type: Method
title: "Operator splitting and Newton–Krylov treatment of atomic-physics sources"
description: "Ways of adding stiff, temperature-dependent ionization, recombination and charge-exchange sources to a staggered semi-implicit MHD advance: Crank–Nicolson linearization, Jacobian-free Newton–Krylov on the non-linear remainder, per-field Strang splitting, and Strang splitting interleaved in the leapfrog with a Douglas–Rachford-inspired coupling source; with the error taxonomy that ranks them and the explicit-source practice of the implicit codes."
status: established
aliases: [Strang splitting of atomic sources, SS-field, SS-leapfrog+DR, CN-JFNK, CN-linear, T-in-n error, ODE/PDE splitting]
tags: [time-integration, neutrals, numerics, edge]
timestamp: 2026-10-16T16:51:00Z
---

# Operator splitting and Newton–Krylov treatment of atomic-physics sources

Plasma–neutral reactions add local, stiff and non-linear source terms to the
MHD equations. Their temperature-dependent rate coefficients couple density
to temperature, and their relative-velocity terms couple the velocities of
the species, which breaks the field-by-field dependency structure exploited
by the [semi-implicit leapfrog](/methods/semi-implicit-leapfrog.md)
([Taheri et al. (2022)](/sources/taheri-2022.md), §1, §3.1).
[Taheri et al. (2022)](/sources/taheri-2022.md) compare four treatments
inside [NIMROD](/software/nimrod.md), using the single-species hydrogenic
plasma–neutral model of Meier and Shumlak with electron-impact ionization,
radiative recombination and resonant charge exchange (§2; the model is on
[fluid neutral models](/methods/fluid-neutral-models.md)). The reaction rates
are $\mathcal R_{\mathrm{ion}}=\langle\sigma v\rangle_{\mathrm{ion}}\,n_in_{\mathrm N}$
and $\mathcal R_{\mathrm{rec}}=\langle\sigma v\rangle_{\mathrm{rec}}\,n_i^2$
($n_e=n_i$), with rate coefficients from DEGAS2 tables interpolated by bicubic
splines (Eqs. 7–8).

## The four schemes

Write a field equation as $\mathrm d\mathbf u/\mathrm dt=\mathbf g(\mathbf u)$ and
its source expansion about the start of the step as
$\mathbf g(\mathbf u+\theta_{\mathrm t}\Delta\mathbf u)=\mathbf g_0+\theta_{\mathrm t}\,\mathbf g_1(\Delta\mathbf u)+\mathbf g_{\mathrm{nl}}(\Delta\mathbf u)$,
with $\mathbf g_1$ linear in the increment (e.g.
$\langle\sigma v\rangle_{\mathrm{ion}}(\Delta n_i\,n_{\mathrm N}+n_i\,\Delta n_{\mathrm N})$
for ionization) and $\mathbf g_{\mathrm{nl}}$ the remainder, which holds the
derivative of the rate coefficient because "the functional form of the cross
section may not be known a priori" (§3.1, Eq. 21).

1. **CN-linear.** The linear part $\mathbf g_1$ is Crank–Nicolson centred
   inside each field solve of the leapfrog and $\mathbf g_{\mathrm{nl}}$ is
   dropped (§3.1, Eqs. 19–20). It is a linear-implicit scheme, which "is not
   robust for all 1D test cases and can give spurious results at large
   time-step sizes" and is dropped in the 1D tests (§5), as Knoll et al.
   predict for linear-implicit schemes against implicitly balanced ones (§1).
2. **CN-JFNK.** The non-linear remainder is kept,
   $$\Delta\mathbf u-\Delta t\big[\mathbf g(\mathbf u^{j})+\tfrac12\mathbf g'(\mathbf u^{j})\Delta\mathbf u+\mathbf g_{\mathrm{nl}}(\mathbf u^{j},\Delta\mathbf u)\big]=0,\qquad \mathbf g_{\mathrm{nl}}=\mathbf g(\mathbf u^{j}+\tfrac12\Delta\mathbf u)-\mathbf g(\mathbf u^{j})-\tfrac12\mathbf g'(\mathbf u^{j})\Delta\mathbf u$$
   (Eqs. 22–23), and solved by the Newton sequence
   $$\Big[\mathsf I-\tfrac12\Delta t\,\mathbf g'(\mathbf u^{j})-\Delta t\,\frac{\partial\mathbf g_{\mathrm{nl}}}{\partial\Delta\mathbf u_m}\Big]\Delta\mathbf u_{m+1}=\Delta t\Big[\mathbf g(\mathbf u^{j})+\mathbf g_{\mathrm{nl}}(\mathbf u^{j},\Delta\mathbf u_m)-\frac{\partial\mathbf g_{\mathrm{nl}}}{\partial\Delta\mathbf u_m}\Delta\mathbf u_m\Big]$$
   (Eq. 24), with a finite-difference Jacobian
   $\partial\mathbf g_{\mathrm{nl}}/\partial\Delta\mathbf u\approx[\mathbf g_{\mathrm{nl}}(\Delta\mathbf u)-\mathbf g_{\mathrm{nl}}((1-\epsilon)\Delta\mathbf u)]/(\epsilon\Delta\mathbf u)$
   (Eq. 25), a relative-residual stopping rule (Eq. 26), a dynamic floor that
   keeps $n_i$ and $T$ positive, a relaxation factor and GMRES for the linear
   solves (§3.2). The inter-species parts of $\mathbf g'$ are moved into
   $\mathbf g_{\mathrm{nl}}$, so the two velocities are still solved
   separately while their coupling is centred through the iteration.
3. **SS-field (per-field Strang splitting).** For each field
   $f\in\{n_i,\mathbf v,T\}$: an ODE half-step of the local sources
   ($\partial_tn_i=\mathcal R_{\mathrm{ion}}-\mathcal R_{\mathrm{rec}}$), the
   unchanged PDE advance of the transport terms
   ($\partial_tn_i+\nabla\cdot(n_i\mathbf v)=0$), then a second ODE half-step,
   $$f\ \xrightarrow{\ \mathcal P_{\mathrm{ode}}(\Delta t/2)\ }\ \xrightarrow{\ \mathcal P_{\mathrm{pde}}(\Delta t)\ }\ \xrightarrow{\ \mathcal P_{\mathrm{ode}}(\Delta t/2)\ }\ f^{\mathrm{new}}$$
   (§3.3, Eqs. 27–29, Fig. 2), with $\mathcal P_{\mathrm{ode}}$, $\mathcal P_{\mathrm{pde}}$
   (page-local) the propagators of the ODE and PDE sub-steps, the ODE solved
   by lsode with Adams methods.
   The PDE solves of the two species become independent, giving smaller
   systems with less fill-in.
4. **SS-leapfrog+DR (the paper's contribution).** The whole system is split as
   $\mathrm d\mathbf u/\mathrm dt=\mathcal A_{\mathrm{at}}(\mathbf u)+\mathcal A_{\mathrm{fl}}(\mathbf u)$,
   $\mathcal A_{\mathrm{at}}$ the local non-linear atomic physics and
   $\mathcal A_{\mathrm{fl}}$ the linearized fluid system, and the ODE
   half-steps are interleaved into the leapfrog (§3.4, Eqs. 30–35, Fig. 3):
   $$\mathbf u^{(j+\frac12,j)}=\mathcal P_{\mathrm{ode}}\big(\tfrac{\Delta t}2;\mathbf s_{\mathrm{DR}}^{j}\big)\mathbf u^{(j,j)},\quad \mathbf u^{(j+\frac12,j+1)}=\mathcal P_{\mathrm{pde}}\big(\Delta t;\mathbf s_{\mathrm{DR}}^{j}\big)\mathbf u^{(j+\frac12,j)},\quad \mathbf u^{(j+1,j+1)}=\mathcal P_{\mathrm{ode}}\big(\tfrac{\Delta t}2;\mathbf s_{\mathrm{DR}}^{j}\big)\mathbf u^{(j+\frac12,j+1)},$$
   where the first superscript is the ODE time and the second the PDE time.
   The ODE step solves $\mathrm d\mathbf u/\mathrm dt=\mathcal A_{\mathrm{at}}+\mathbf s_{\mathrm{DR}}$
   with an adaptive multistep solver and the PDE step solves
   $\mathrm d\mathbf u/\mathrm dt=\mathcal A_{\mathrm{fl}}-\mathbf s_{\mathrm{DR}}$
   with the staggered Crank–Nicolson leapfrog (Eqs. 32–33). The
   Douglas–Rachford-inspired coupling source is
   $$\mathbf s_{\mathrm{DR}}^{j}=-\min\Big(\max\Big(-\frac{|\mathcal A_{\mathrm{fl}}|}{|\mathcal A_{\mathrm{at}}|},0\Big),1\Big)\,\mathcal A_{\mathrm{at}}\big(\mathbf u^{(j+\frac12,j)}\big)$$
   (Eq. 34, as printed), designed to vanish when the ODE and PDE tendencies
   have the same sign and to be limited to the smaller of the two magnitudes.
   To avoid an extra mass-matrix solve for second derivatives with $C^0$
   elements, $\mathcal A_{\mathrm{fl}}$ is lagged:
   $\mathcal A_{\mathrm{fl}}(\mathbf u^{(j+\frac12,j)})\simeq(\mathbf u^{(j,j)}-\mathbf u^{(j,j-1)})/\Delta t+\mathbf s_{\mathrm{DR}}^{j-1}$
   (Eq. 35). In 0D the scheme reduces to an adaptive ODE integration of the
   whole system, with error set by the solver tolerance $10^{-12}$ (§4).

## Error taxonomy

Taheri et al. sort the errors by source (§3.5): the **non-linear error**
(removed by JFNK or by the adaptive ODE solver); the **Crank–Nicolson
centring error**, $O(\Delta t^2)$, removed for the atomic terms by the ODE
solver; the **"T-in-n" error** from centring the temperature explicitly in the
density advance when rates depend on $T$ (removed by SS-leapfrog+DR); the
**field-staggering error** from the relative-velocity terms (also removed by
SS-leapfrog+DR); and the **ODE/PDE splitting error**, which grows with
ODE/PDE cancellation, causes oscillations and wrong steady states, and is
reduced by $\mathbf s_{\mathrm{DR}}$. In the 0D tests the gaps between schemes
isolate these errors: CN-linear minus CN-JFNK is the non-linear error, CN-JFNK
minus SS-field the centring error, SS-field minus the tolerance the T-in-n
error, and they are "not strictly additive" (§4.1, Fig. 4a).

## Results

- **0D** (tokamak core, edge, non-linear ionization, flow relaxation;
  Tables 1–4, Fig. 4): three separated error levels in the core case; the
  non-linear error matters at every $\Delta t$ in the edge case; CN-linear is
  most accurate in the non-linear-ionization case through a "fortuitous"
  cancellation of its overshoot against the T-in-n error; field staggering
  dominates flow relaxation (§4.1–4.4).
- **1D neutral expansion into a frozen tokamak pedestal** (40 × 4 biquintic
  elements): the SS-field steady state depends on $\Delta t$ through the
  splitting error and underestimates the neutral flux (errors about
  $10^{-2}$), while CN-JFNK and SS-leapfrog+DR agree (errors about
  $10^{-8}$–$10^{-6}$); SS-leapfrog+DR is the more accurate below
  $\Delta t\approx5\times10^{-7}$ s. CN-JFNK costs about three times the
  SS-field wall-clock time, and SS-field about 1.1 times SS-leapfrog+DR
  (§5.1, Figs. 6–8).
- **1D snowplow into a neutral slug:** all schemes share an error at large
  $\Delta t$; at small $\Delta t$ the splitting error flattens the SS-field
  convergence (§5.2, Fig. 11). Some permutations failed to converge with
  CN-JFNK, "potentially because our JFNK is approximate" (§6).

## Explicit sources in implicit codes

The fully implicit JOREK advance (see
[implicit time integration](/methods/implicit-time-integration.md)) takes a
different route for its particle-based sources: the
[kinetic neutral model](/methods/kinetic-neutral-model.md) applies its
ionization, charge-exchange, radiation and recombination moments explicitly,
once per fluid step, multiplying implicit MHD terms; the authors note that
accuracy may drop in order when kinetic particles dominate and leave
(semi-)implicit coupling to future work
([Korving et al. (2023)](/sources/korving-2023.md), §IV C). The
runaway-electron sources are likewise explicit inside the implicit advance
([Bandaru et al. (2024)](/sources/bandaru-2024.md), §II A).

## Qualifications

- **Eq. 34 as typeset vanishes identically.** The ratio of magnitudes is
  non-negative, so $\max(-|\mathcal A_{\mathrm{fl}}|/|\mathcal A_{\mathrm{at}}|,0)=0$
  and $\mathbf s_{\mathrm{DR}}\equiv0$; the stated design (vanish for equal
  signs, limit to the lesser magnitude) needs a signed ratio such as
  $-\mathcal A_{\mathrm{fl}}/\mathcal A_{\mathrm{at}}$ (reader's check; the CPC
  version should be checked).
- **Unproved order claim.** SS-leapfrog+DR is said to be "second-order
  accurate in time regardless of the choice" of the coupling source; "analysis
  shows" is asserted but no analysis is given (§3.4).
- **"Crank–Nicolson" is the implicit midpoint rule.** Eqs. 22–23 evaluate
  $\mathbf g$ at $\mathbf u^{j}+\tfrac12\Delta\mathbf u$, which coincides with
  Crank–Nicolson only for linear $\mathbf g$ (reader's note).
- **ODE integrator naming** varies between "lsode, with Adams methods",
  "time adaptive Adam-Bashforth" and "multi-step ODE solver"; lsode's Adams
  option is Adams–Moulton predictor–corrector (reader's note).
- **Error metric.** Eq. 36 is called an $l_2$ norm but is a mean absolute
  relative error, ill-defined for fields that cross zero (reader's note).
- The 0D tests ignore the ionization energy loss and so conserve energy,
  which the paper calls "optically thick" against the optically thin model of
  §2; the 0D reference step is printed "$2\times10^{12}$ s" for
  $2\times10^{-12}$ s; the comparison is among four NIMROD schemes only, with
  no other code (reader's notes).

# Citations

- [Taheri et al. (2022)](/sources/taheri-2022.md) — §1–6, Eqs. 7–8, 19–36, Figs. 1–11.
- [Korving et al. (2023)](/sources/korving-2023.md) — §IV C.
- [Bandaru et al. (2024)](/sources/bandaru-2024.md) — §II A.
