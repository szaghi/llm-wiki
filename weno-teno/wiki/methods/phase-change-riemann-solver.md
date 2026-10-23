---
type: Method
title: "Riemann solvers with phase change"
description: "The liquid–vapour Riemann problem with phase change has four waves and jump conditions with latent heat and surface tension, closed by a mass-flux model; Long et al. approximate it by a four-wave HLL-type solver reduced to a scalar iteration on the mass flux from the states adjacent to the phase interface, the interfacial flux of a fully conservative cut-cell scheme."
status: established
aliases: [two-phase Riemann problem with phase change, four-wave HLL-type phase-change solver, phase-transition Riemann solver, Hertz–Knudsen closure, evaporation and condensation Riemann problem]
tags: [riemann-solver, multiphase, interface-capturing, numerical-flux]
timestamp: 2026-10-23T23:00:00Z
---

# Riemann solvers with phase change

At a liquid–vapour interface with evaporation or condensation, mass crosses the interface,
so the interface is not a contact and the two-phase Riemann problem acquires a **phase
interface** with its own jump conditions. [Long et al. (2023)](/sources/long-2023.md) build an
approximate solver for this problem and use it as the only coupling between the phases of a
conservative sharp-interface ([level-set](/methods/level-set-method.md), cut-cell) scheme for
inviscid compressible flow. Below the liquid is on the left, the vapour on the right, $V$ is the
normal velocity, $\dot m$ the mass flux through the phase interface (positive for
evaporation), $s_{\mathrm p}$ and $s_{\mathrm c}$ the speeds of the phase interface and of the
contact, $Q_{\mathrm{lat}}$ the latent heat, $\sigma_{\mathrm{st}}$ the surface-tension
coefficient and $\kappa_{\mathrm c}$ the curvature (all page-local; the source writes $j$,
$S_p$, $S_c$, $\sigma$, $\kappa$).

## The Riemann problem with phase change

As recalled by Long et al. (§3.1, Eqs. (9)–(12), after Fechter et al.), the "general" problem
has four waves: two outer nonlinear waves, the phase interface and a contact, with the
intermediate state between phase interface and contact belonging to the vapour for
evaporation and to the liquid for condensation (Eq. (11)). Across the phase interface, with
$[\![a]\!]=a^*_{\mathrm{vap}}-a^*_{\mathrm{liq}}$ the jump between the adjacent states,

$$[\![\rho(V-s_{\mathrm p})]\!]=0,\qquad [\![\rho(V-s_{\mathrm p})V+p]\!]=-\sigma_{\mathrm{st}}\kappa_{\mathrm c},\qquad \Big[\!\!\Big[\rho(V-s_{\mathrm p})\big(e+\tfrac12V^2\big)+pV\Big]\!\!\Big]=\dot m\,Q_{\mathrm{lat}}-\sigma_{\mathrm{st}}\kappa_{\mathrm c}\,s_{\mathrm p},$$

and $\dot m=\rho^*_{\mathrm{liq}}(V^*_{\mathrm{liq}}-s_{\mathrm p})=\rho^*_{\mathrm{vap}}(V^*_{\mathrm{vap}}-s_{\mathrm p})$:
the [Rankine–Hugoniot conditions](/definitions/rankine-hugoniot-condition.md) of a moving
interface with surface tension and a latent-heat source. When the phase interface is subsonic
and non-characteristic on both sides,
$V^*_k-c^*_k<s_{\mathrm p}<V^*_k+c^*_k$, the system is underdetermined and needs a
phase-change model for $\dot m$ (Eq. (12)). The exact solver of Fechter et al. requires an
eight-dimensional root finding, which Long et al. call "computationally expensive and not
robust" (§1).

## The four-wave HLL-type approximation

Long et al. (§3.2, Eqs. (13)–(25), App. A) extend the HLL-type solver of Fechter et al. (2018)
by "reconstructing a contact wave", so that five constant states
$u_{\mathrm L},u^*_{\mathrm L},u^*_{\mathrm M},u^*_{\mathrm R},u_{\mathrm R}$ are separated by four waves:

- outer waves treated as shocks with Davis speeds $s^-=V_{\mathrm L}-c_{\mathrm L}$,
  $s^+=V_{\mathrm R}+c_{\mathrm R}$ ([HLL-family solvers](/methods/hll-riemann-solvers.md)), across
  which mass, momentum and energy satisfy the jump relations
  $\rho^*_k(V^*_k-s_k)=\rho_k(V_k-s_k)$ and their momentum and energy analogues (Eq. (14));
- the phase interface with the jump conditions above;
- a contact, $V^*_{\mathrm M}=s_{\mathrm c}=V^*_k$, $p^*_{\mathrm M}=p^*_k$ on its other side
  (Eq. (15)).

This gives 13 independent equations for 15 unknowns (three star states, $s_{\mathrm p}$,
$s_{\mathrm c}$, $\dot m$). Two closures complete it:

1. a **density-ratio supplement** $\rho^*_{\mathrm{liq}}/\rho^*_{\mathrm{vap}}\approx\rho_{\mathrm L}/\rho_{\mathrm R}$
   (Eq. (19)), motivated by density ratios within one phase being $O(1)$ while the ratio across
   phases is large (Eqs. (16)–(18));
2. the **Hertz–Knudsen relation** as phase-change model (Eqs. (20)–(21), after Schrage),
   $$\dot m=\frac1{\sqrt{2\pi R_{\mathrm v}}}\Big(\lambda_{\mathrm{ev}}\frac{p_{\mathrm{sat}}(T^*_{\mathrm{liq}})}{\sqrt{T^*_{\mathrm{liq}}}}-\lambda_{\mathrm{co}}\frac{p^*_{\mathrm{vap}}}{\sqrt{T^*_{\mathrm{vap}}}}\Big),$$
   with the vapour gas constant $R_{\mathrm v}$ and evaporation and condensation coefficients
   $\lambda_{\mathrm{ev}}$, $\lambda_{\mathrm{co}}$ (page-local), for which "no general calibration
   law" exists.

All star states and both speeds are then closed-form functions of $\dot m$ alone (App. A,
Eq. (A.2)); as $\dot m\to0$ the phase interface and the contact merge,
$s_{\mathrm p},s_{\mathrm c}\to(l_2-r_2-\sigma_{\mathrm{st}}\kappa_{\mathrm c})/(l_1-r_1)$ with $l_k$,
$r_k$ the mass, momentum and energy fluxes relative to $s^\mp$ of the outer states (Eq. (A.3)),
and $\dot m=0$ is used for runs without phase change. The remaining scalar equation
$\dot m=f_{\mathrm{HK}}\big(u^*_{\mathrm{liq}}(\dot m),u^*_{\mathrm{vap}}(\dot m)\big)$ (page-local
$f_{\mathrm{HK}}$) is solved by Steffensen's method from $f_{\mathrm{HK}}(u_{\mathrm L},u_{\mathrm R})$ to
$\lvert\Delta\dot m\rvert<10^{-6}$, usually in 3–4 iterations (Eqs. (24)–(25)). The star
temperature is computed as $T^*(p^*,e^*)$, because under the HLL approximation the star density
is not consistent with the equation of state (§3.2). The authors state that the solver is
independent of the equation of state, since no EOS enters the derivation (§1); the tests use the
[stiffened-gas law](/definitions/stiffened-gas-equation-of-state.md) for water and a
Helmholtz-energy EOS for n-dodecane.

**Which states enter the mass flux.** Long et al. (§4.1.1, Eq. (29)) argue that $\dot m$ must be
evaluated from the states **adjacent to the phase interface**, $u^*_{\mathrm{liq}}$,
$u^*_{\mathrm{vap}}$, not from the initial left and right states as in Houim and Kuo and in Das
and Udaykumar: once the cut-cell input states approach the exact adjacent states, the Riemann
problem between them reproduces them, so a star-based $\dot m$ stays consistent, whereas
$f_{\mathrm{HK}}(u^0_{\mathrm L},u^0_{\mathrm R})\neq f_{\mathrm{HK}}(u^*_{\mathrm{liq}},u^*_{\mathrm{vap}})$; the
argument is claimed for any phase-change model, and the authors state that this has not been
reported before. On an n-dodecane evaporation tube the left–right choice converges to an
incorrect solution (Fig. 4).

## Interfacial flux and conservation

In each cut cell the interfacial flux on the interface segment $\Delta\Gamma$ is
$\pm\Delta\Gamma\,\big[\dot m,\ (\dot mV^*+p^*)n,\ \dot m(e^*+\tfrac12V^{*2})+p^*V^*\big]^\top$,
with $+$ for the vapour and $-$ for the liquid (Eq. (26)). Their sum is
$\big[0,\ -\sigma_{\mathrm{st}}\kappa_{\mathrm c}n,\ \dot mQ_{\mathrm{lat}}-\sigma_{\mathrm{st}}\kappa_{\mathrm c}s_{\mathrm p}\big]^\top$
(Eq. (27)): mass is conserved exactly and the momentum and energy residuals are the
surface-tension force and the latent-heat and surface-tension work. Total energy including the
latent heat of the converted mass is therefore conserved, which the authors contrast with the
2018 solver of Fechter et al., which omits the energy coupling in the vapour (§3.2, Eq. (34));
see [local conservation](/results/local-conservation-flux-form.md). With phase change and surface
tension off the scheme reduces to the conservative sharp-interface method of Hu et al.

## Evidence

Long et al. (§4; fifth-order WENO, SSP-RK2, CFL $0.6$, wavelet multiresolution grids):

- 1D evaporation and condensation tubes for n-dodecane and water against exact solutions on
  200 and 2000 cells ([gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md));
  the error of the density-ratio supplement is about $11.6\%$ initially and then drops quickly
  (Fig. 5); the condensation phase-interface–contact gap ($4.9\times10^{-5}$ m for n-dodecane,
  $2.6\times10^{-6}$ m for water) stays unresolved on 2000 cells without spurious waves.
- To match the exact solution the Hertz–Knudsen coefficients differ between the two choices of
  states: $(\lambda_{\mathrm{ev}},\lambda_{\mathrm{co}})=(1.0,0.9)$ with star states, $(0.756,0.680)$
  with left–right states (§4.1.1).
- Cost (AMD EPYC 7351): a circular droplet with evaporation takes $318.165$ s with the exact and
  $86.9863$ s with the approximate solver, a circular bubble with condensation $325.824$ s and
  $106.925$ s (§4.2), attributed to the scalar iteration and to avoiding EOS calls.
  *(compiler check, not in the sources: speed-ups $3.66$ and $3.05$.)*
- An oscillating droplet has period $0.207$ ms against $0.204$ ms from the two-phase Rayleigh
  formula, an error of about $1.47\%$ (§4.3); shock–droplet interactions in 2D and 3D
  ([shock–water-column interaction](/benchmarks/shock-water-column.md)) and near-wall vapour-bubble
  collapse follow (§4.4–§4.5).

## Qualifications

- **Fully conservative, with limits.** Level-set reinitialization can delete under-resolved
  droplets or bubbles, which violates conservation; remedies are left to future work (§3.2).
- The comparison of star-state and left–right mass fluxes uses different Hertz–Knudsen
  coefficient pairs, each chosen so that the computed solution matches the exact one (§4.1.1).
- Printed slips: Eq. (18) prints the within-phase ratios with identical numerator and
  denominator; after Eq. (A.3) the text names $u^*_{\mathrm L}$ as the vanishing state and as one of
  the states used, while the state that disappears when phase interface and contact merge is
  $u^*_{\mathrm M}$; Eq. (27) omits the factor $\Delta\Gamma$ of Eq. (26).

# Citations

- [Long et al. (2023)](/sources/long-2023.md) — §1, §2.3, §3.1 (Eqs. (9)–(12)), §3.2 (Eqs. (13)–(27), (34)), §4.1–§4.5 (Figs. 4–5, 12–13), App. A (Eqs. (A.1)–(A.3)).
