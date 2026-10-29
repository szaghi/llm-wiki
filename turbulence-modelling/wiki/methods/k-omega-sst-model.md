---
type: Method
title: "k-ω SST model"
description: "Menter's two-equation shear-stress-transport eddy-viscosity model, blending a k-ω inner formulation with an outer one through F1 and limiting the eddy viscosity through F2; its printed variants, log-ω, transition, PANS, DES and compressibility-corrected forms, high-order discretization, data-driven corrections, and evidence on airfoils, cascades, cars and separated flows."
status: established
aliases: [SST, k-omega SST, shear stress transport model, Menter SST, SST k-ω, SST-IDDES, SST-DDES, BSL k-ω, baseline k-ω model]
tags: [rans, eddy-viscosity, transition, pans, hybrid-rans-les]
timestamp: 2026-10-29T10:04:00Z
---

# k-ω SST model

The shear-stress-transport (SST) model of Menter is a two-equation RANS
closure that transports the turbulent kinetic energy $k$ and the specific
dissipation rate $\omega$ and computes a [Boussinesq](/definitions/boussinesq-hypothesis.md)
eddy viscosity from them. A blending function $F_1$ switches the constants
and a cross-diffusion term between an inner (near-wall) and an outer set; a
second function $F_2$ activates a limiter on $\nu_t$. In this bundle it is a
host model in three roles: the RANS model behind
[partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md),
the turbulence model coupled to the
[local-correlation-based transition models](/methods/local-correlation-based-transition-model.md),
and one of the two model families of the high-lift workshop RANS
submissions compared with wall-modelled LES. On this page the strain and
rotation magnitudes are those of the mean velocity. The unblended Wilcox
model from which the inner branch derives, with its 1998, 2006 and TNT
variants, is on the [Wilcox $k$-$\omega$ page](/methods/k-omega-model.md).

## Equations

Dzanic et al. (2022) print the full compressible model in its PANS form
([Dzanic et al. (2022)](/sources/dzanic-2022.md), §2.1, Eqs. 10–17; constants
in App. A, "as tabulated by Menter"). Their $\omega$-equation (Eq. 11) prints
the destruction as the bracket

$$-\rho\Big(P'-\frac{P'}{f_\omega}+\frac{\beta\omega_u}{f_\omega}\Big),\qquad P'=\frac{\rho\alpha\beta^*k_u}{\mu_u},$$

with $k_u$, $\omega_u$, $\mu_u$ the unresolved (modelled) quantities of
[PANS](/methods/partially-averaged-navier-stokes.md); at $f_\omega=1$ the
bracket reduces to $-\rho\beta\omega_u$. This term has the dimensions of
$\rho\omega$, while the left side $\partial_t(\rho\omega_u)$ has those of
$\rho\omega^2$; a factor $\omega_u$ restores consistency and gives the
destruction $-\rho\beta\omega_u^2$ *(compiler check, not in the sources)*.
With that correction, at $f_k=f_\omega=1$, where PANS reduces to RANS, and
rewritten in incompressible kinematic form (molecular and eddy viscosity
divided by $\rho$) *(compiler check, not in the sources)*, the model reads:

$$\begin{aligned}
\partial_tk+\langle u_j\rangle\partial_jk&=P_k-\beta^*k\omega+\partial_j\big[(\nu+\sigma_k\nu_t)\partial_jk\big],\\
\partial_t\omega+\langle u_j\rangle\partial_j\omega&=\frac{\alpha}{\nu_t}P_k-\beta\omega^2+\partial_j\big[(\nu+\sigma_\omega\nu_t)\partial_j\omega\big]+2(1-F_1)\frac{\sigma_{\omega2}}{\omega}\partial_jk\,\partial_j\omega,
\end{aligned}$$

$$\nu_t=\frac{a_1k}{\max(a_1\omega,\lvert\Omega\rvert F_2)},$$

$$F_1=\tanh\Big\{\Big[\min\Big(\max\Big(\frac{\sqrt k}{\beta^*\omega d},\frac{500\nu}{\omega d^2}\Big),\frac{4\sigma_{\omega2}k}{CD_{k\omega}d^2}\Big)\Big]^4\Big\},\qquad
F_2=\tanh\Big\{\Big[\max\Big(\frac{2\sqrt k}{\beta^*\omega d},\frac{500\nu}{\omega d^2}\Big)\Big]^2\Big\},$$

$$CD_{k\omega}=\max\Big(\frac{2\sigma_{\omega2}}{\omega}\partial_jk\,\partial_j\omega,\ 10^{-10}\Big).$$

The constants $\alpha$, $\beta$, $\sigma_k$, $\sigma_\omega$ are blended as
$\phi=F_1\phi_1+(1-F_1)\phi_2$ (Dzanic et al., App. A):

| $\alpha_1$ | $\alpha_2$ | $\beta_1$ | $\beta_2$ | $\sigma_{k1}$ | $\sigma_{k2}$ | $\sigma_{\omega1}$ | $\sigma_{\omega2}$ | $a_1$ | $\beta^*$ |
|---|---|---|---|---|---|---|---|---|---|
| 0.5532 | 0.4403 | 0.075 | 0.0828 | 0.85 | 1.0 | 0.5 | 0.856 | 0.31 | 0.09 |

Dzanic et al. set the wall value of $\omega$ to $60\nu/(\beta_1\Delta d_1^2)$, with
the first-point distance $\Delta d_1$ taken as the element height divided by
$N+1$ so that wall values agree between polynomial degrees (§3, Eq. 26).

**A second printed form.** Zhao et al. (2023b) print the compressible model
with the same $F_1$, $F_2$ and cross-diffusion, with $0.09$ in place of
$\beta^*$ inside $F_1$ and $F_2$, a floor of $10^{-20}$ on $CD_{k\omega}$, and
the limiter $\mu_t=\min\big[\rho k/\omega,\ \rho a_1k/(\Omega F_2)\big]$ with
$a_1=0.31$ and $\Omega=\lvert S_{ij}\rvert$, a strain magnitude whose
normalization is not printed; they print no other coefficient
([Zhao et al. (2023b)](/sources/zhao-2023-b.md), §2, Eqs. 2-2–2-4). The two
sources thus differ in the limiter's argument (rotation magnitude in
Dzanic et al., strain magnitude in Zhao et al.) and in the floor of
$CD_{k\omega}$ ($10^{-10}$ against $10^{-20}$); neither discusses the choice.
Zhao et al. impose $\omega_w=10\cdot6\nu/(\beta y^2)$ at the wall "according
to" Bassi et al., which is Dzanic et al.'s $60\nu/(\beta_1\Delta d_1^2)$
*(compiler check, not in the sources)*, and add that the wall constant
$C_w$ must be adjusted to the discretization: 2.5 in Hellsten's work, 0.3
in Bassi et al.'s, and 0.01 in theirs (§3.2).

**Wall treatment in a finite-volume code.** Delassaux et al. (2023) use
Fluent's $y^+$-insensitive wall treatment, which blends the viscous-sublayer
and log-layer values of $\omega$ in wall units,
$6/(C_{\omega2}y^{+2})$ and $1/(\sqrt{C_\mu}\,y^+)$ ($C_{\omega2}$ and $C_\mu$
the $k$-$\omega$ constants, values not printed), and state that SST
"requires the first node of the mesh to be in the viscous sublayer as
$y^+\simeq1$" ([Delassaux et al. (2023)](/sources/delassaux-2023.md),
§4.1.2; HAL author manuscript). Morsbach et al. (2024) use the 2003 version
of Menter et al. with the Kato–Launder production, without printing
constants ([Morsbach et al. (2024)](/sources/morsbach-2024.md), §2).

**A third printed form, with constants.** Oulghelou et al. (2025) print
the incompressible model of their modified OpenFOAM with the same $F_1$,
$F_2$ and cross-diffusion and the constants $\sigma_k=(0.85,1)$,
$\sigma_\omega=(0.5,0.856)$, $\alpha=(5/9,0.44)$, $\beta=(0.075,0.0828)$,
$\beta^*=0.09$, $a_1=0.31$, the source's names being $\alpha_k$, $\alpha_\omega$
and $\gamma$ for the registry's $\sigma_k$, $\sigma_\omega$ and $\alpha$
([Oulghelou et al. (2025)](/sources/oulghelou-2025.md), §2 Eqs. 3–6, App. B;
arXiv v2). The production is limited, $P_k\le c_1\beta^*k\omega$ with
$c_1=10$, and the eddy viscosity is
$\nu_t=a_1k/\max\big(a_1\omega,\,b_1\lvert S\rvert F_{23}\big)$ with $b_1=1$, a
strain magnitude, and $F_{23}=F_2F_3$ when the optional
$F_3=1-\tanh\big[\big(\min(150\nu/(\omega d^2),10)\big)^4\big]$ is enabled.
The production coefficients follow from the log-layer condition
$\alpha=\beta/\beta^*-\sigma_\omega\kappa^2/\sqrt{\beta^*}$: with $\kappa=0.41$
this gives 0.5532 and 0.4403, the values Dzanic et al. tabulate; Oulghelou
et al.'s 0.44 is the rounding of 0.4403, while their $5/9\approx0.5556$
differs from 0.5532 in the third digit, so it is not a rounding of the
log-layer value *(compiler check, not in the sources)*. The same condition,
written as $\beta_\omega-\beta^*\gamma_\omega=\kappa^2\sqrt{\beta^*}\sigma_\omega$
with the registry-§11 $\beta_\omega$, $\gamma_\omega$ for the $\beta$ and $\alpha$ of
the equations above (Wu et al.'s $\theta$ and $\gamma$), is the one Wu et al.
(2025) use to argue that a field-inversion multiplier of the destruction
must equal one in the log layer (below). Oulghelou et al. call SST itself
a heuristic blend of $k$-$\varepsilon$ and $k$-$\omega$ (§1).

Möller et al. (2024) print the compressible model in Favre-averaged form
with the rotation-magnitude limiter of Dzanic et al., $a_1=0.31$ and
$\beta^*=0.09$, without the other constants
([Möller et al. (2024)](/sources/moller-2024.md), §II.B.1, Eqs. 14–16;
accepted manuscript). Klose et al. (2025) use, like Morsbach et al., the
Kato–Launder production with the $\gamma$-$Re_\theta$ model in the
finite-volume part of [TRACE](/software/trace.md)
([Klose et al. (2025)](/sources/klose-2025.md), §2; ASME accepted
manuscript).

**A fourth printed form, for a high-order solver.** Elzaabalawy et al.
(2023) print Menter's 2003 SST and BSL ("SST without viscosity limiter") in
incompressible kinematic form with $\sigma_k=(0.85,1.0)$,
$\sigma_\omega=(0.5,0.856)$, $\beta=(0.75,0.0828)$ as printed,
$\alpha=(5/9,0.44)$ (the source's $\zeta$), $\beta^*=0.09$ and $a_1=0.43$,
the limiter $\nu_t=a_1k/\max(a_1\omega,F_2S)$ with a strain norm $S$ not
defined, and the cross-diffusion floor $10^{-10}$ of Dzanic et al.; the
production is limited by $15\beta^*\omega k$ for all their models
([Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md), §3.1.1 Eq. 55,
§3.2, Eq. 71; see Qualifications for $\beta_1$ and $a_1$). Their blending
functions evaluate $\omega$ through the interpolant of $1/\omega$ (§3.2).

**BSL as the host of a hybrid.** Wu et al. (2023) print Menter's BSL
$k$-$\omega$ model, the blend $\phi=F_1\phi_1+(1-F_1)\phi_2$ of a Wilcox
$k$-$\omega$ set and a $k$-$\varepsilon$ set (Eq. 3), as the unchanged
transport equations of their self-adaptive turbulence eddy simulation
([Wu et al. (2023)](/sources/wu-2023-b.md), §2.1.1, Eqs. 1–3, Table 1). With
$\mathcal T_{ij}$ (page-local) the source's $\tau_{ij}$, "the Reynolds
stress tensor terms", whose sign and density weighting are not stated,
the printed equations read

$$\frac{D\rho k}{Dt}=\mathcal T_{ij}\partial_ju_i-\beta^*\rho\omega k+\partial_j\big[(\mu+\sigma_k\mu_t)\partial_jk\big],\qquad
\frac{D\rho\omega}{Dt}=\omega\Big(\frac{\gamma_\omega}{k}\mathcal T_{ij}\partial_ju_i-\beta_\omega\rho\omega^2\Big)+\partial_j\big[(\mu+\sigma_\omega\mu_t)\partial_j\omega\big]+\mathrm{CD},$$

with $\gamma_\omega$, $\beta_\omega$ the registry-§11 production and
destruction coefficients (the source's $\gamma$, $\beta$) and CD the
cross-diffusion term, both as printed (see Qualifications for the bracket and the cross-diffusion). $F_1$ is
1 near the wall and 0 away from it, and is not printed. Table 1 as printed:
$\beta^*=0.09$ (the source's $\beta_1^*$), $\sigma_k=(0.5,1.0)$,
$\sigma_\omega=(0.5,0.856)$, $\beta_\omega=(0.075,0.0828)$,
$\gamma_\omega=(0.553,0.44)$. Against the SST table above, the
$\sigma_\omega$, $\beta_\omega$ and outer $\sigma_k$ values are the same,
$\gamma_\omega$ is printed to three and two digits (0.553 and 0.44 against
0.5532 and 0.4403), and the inner $\sigma_k$ is 0.5 against 0.85; the source
names the model BSL, not SST. The hybrid
multiplies only the eddy viscosity, $\mu_t=F_r\rho k/\omega$, by a
resolution function (on the
[hybrid RANS/LES page](/definitions/hybrid-rans-les.md)).
Wu et al. (2024) print the same BSL host for their SATES-σ variant (§2.1,
Eqs. 1–3), with the destruction written $\omega(\ldots-\beta_\omega\rho\omega)$
and the cross-diffusion $2\rho(1-F_1)\sigma_{\omega2}\omega^{-1}\partial_jk\,\partial_j\omega$
without a trailing factor, a form with the dimensions of $D\rho\omega/Dt$
throughout *(compiler check, not in the sources)*; of the constants they
print only $\beta^*=0.09$ (their $\beta_1^*$)
([Wu et al. (2024)](/sources/wu-2024.md); the model is on the
[SATES page](/methods/self-adaptive-turbulence-eddy-simulation.md)).
Wu et al. (2024b) print the BSL host a third time in the same form, the
cross-diffusion again $2\rho(1-F_1)\sigma_{\omega2}\omega^{-1}\partial_jk\,\partial_j\omega$,
with $\mu_{\mathrm{RANS}}=\rho k/\omega$ and only $\beta^*=0.09$ given among
the constants ([Wu et al. (2024b)](/sources/wu-2024-b.md), §III.A,
Eqs. 24–27).
[Wu et al. (2026)](/sources/wu-2026-b.md) state instead that the same
group's SATES "is developed based on the SST k-ω turbulence model" and
print only its eddy viscosity, with the limiter written as a factor,
$\mu_t=\rho(k/\omega)F_{\mathrm{cor}}$ with
$F_{\mathrm{cor}}=\omega/\max(\omega,\lvert S\rvert F_2/a_1)$ (page-local; their
"correction function in SST model"),
$F_2=\tanh\big[\max\big(2\sqrt k/(\beta^*\omega d),\,500\mu/(\rho\omega d^2)\big)^2\big]$
and $\beta^*=0.09$; $a_1$, the normalization of $\lvert S\rvert$ and the
transport equations are not printed (§2.1, Eqs. 1–3). This is the limiter
of the Equations section with $\lvert S\rvert$ in place of $\lvert\Omega\rvert$
*(compiler check, not in the sources)*. Their SATES-II also builds a
blending function from $F_2$, $\tanh[(0.67\max(\cdot,\cdot))^4]$ with the
same two arguments and $\nu$ in place of $\mu/\rho$, to switch a near-wall
coefficient on in the inner boundary layer (Eqs. 15–16; on the
[SATES page](/methods/self-adaptive-turbulence-eddy-simulation.md)), and
their SST-IDDES uses $C_{\mathrm{DES}}=0.78F_1+0.61(1-F_1)$ (Eq. 19).

**A log-$\omega$ form for flux reconstruction.** Vandenhoeck et al. (2022)
rewrite the SST-2003 model with $\tilde\omega_\ell=\ln\omega$ as unknown
(page-local symbol, as on the [Wilcox page](/methods/k-omega-model.md); the
source writes $\tilde\omega$, which is not a Favre filter), extending to SST
the log-$\omega$ transport that Bassi et al. (2005) introduced for the
Wilcox model in DG ([Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md),
§1.1, Eqs. 1–20, Table 1). In their compressible form the $\omega$ equation
divided by $\omega$ reads

$$\partial_t(\rho\tilde\omega_\ell)+\partial_j(\rho u_j\tilde\omega_\ell)=\frac{\rho\alpha}{\mu_t}e^{-\tilde\omega_\ell}\rho P_k-\beta\rho e^{\tilde\omega_\ell}+(\mu+\sigma_\omega\mu_t)\lvert\nabla\tilde\omega_\ell\rvert^2+\partial_j\big[(\mu+\sigma_\omega\mu_t)\partial_j\tilde\omega_\ell\big]+2(1-F_1)\rho\sigma_{\omega2}e^{-\tilde\omega_\ell}\partial_jk\,\partial_j\tilde\omega_\ell,$$

with, against the Wilcox log form of Bassi et al., two new terms: the
transformed SST cross diffusion (their Eq. 17) and the gradient-squared
term from transforming the diffusion (Eq. 18). The rest is the SST of the
Equations section in $e^{\tilde\omega_\ell}$: $F_1$, $F_2$ and
$CD_{k\omega}$ with $\beta^*$ (floor $10^{-10}$), the limiter
$\mu_t=\rho a_1k/\max(a_1e^{\tilde\omega_\ell},\lvert S\rvert F_2)$ on the
strain magnitude, the production limited by $10\beta^*\rho k e^{\tilde\omega_\ell}$,
$k$ replaced by $\max(k,0)$ in the sources (needed only in the initial
transient), and the constants $\alpha=(5/9,0.44)$, $\sigma_k=(0.85,1.0)$,
$\sigma_\omega=(0.5,0.856)$, $\beta=(0.075,0.0828)$, $\beta^*=0.09$,
$a_1=0.31$, those of Oulghelou et al. above. The authors state that with
the original variable the steep near-wall growth of $\omega$ resolved by
high-order polynomials made the solver unstable and lost the positivity of
$\omega$, while $\ln\omega$ is much smoother near the wall and guarantees
$\omega>0$; the equation is conservative in $\tilde\omega_\ell$ but not in
$\omega$, which Bassi et al. found to cause no significant discrepancy
(§1.1). The wall condition is
$\tilde\omega_\ell=\ln\big(60\mu/(\rho\beta_1d_1^2)\big)$ with $d_1$ the
wall distance of the first solution point, which should be zero in theory
(§3.3.1, Eq. 88): the Dzanic et al. value in logarithmic form, with the
first-point distance in place of the element height over $N+1$
*(compiler check, not in the sources)*. Coupled to the Langtry–Menter
transition model, $F_1=\max(F_{1,\mathrm{SST}},F_3)$ with
$F_3=\exp\big[-(R_y/120)^8\big]$ (Eq. 38; see Contradictions; this Langtry–Menter $F_3$, which both sources write with that name, is a different function from the optional SST $F_3$ above). Their
implicit Jacobian, its source-term treatments and the COOLFluiD
implementation are on the [flux-reconstruction](/methods/flux-reconstruction.md)
and [COOLFluiD](/software/coolfluid.md) pages.

### Compressibility correction

Zhao et al. (2023b) add the dilatational-dissipation and
pressure-dilatation correction of Suzen & Hoffmann, active only through the
factor $(1-F_1)$, i.e. in the outer branch. In their nondimensional form
the $k$-destruction becomes $\big[1+\alpha_1M_t^2(1-F_1)\big]\beta^*\rho k\omega$
plus a pressure-dilatation source $(1-F_1)\,\Pi^{\mathrm t}_{\mathrm{pd}}$ (the modelled
turbulent [pressure dilatation](/definitions/pressure-dilatation.md), registry §11;
the source's $\overline{p''d''}$, whose double primes are not Favre fluctuations), with

$$\Pi^{\mathrm t}_{\mathrm{pd}}=-\alpha_2\,\tau_{ij}\partial_ju_iM_t^2+\alpha_3\rho\beta^*k\omega M_t^2,\qquad \alpha_1=1.0,\ \alpha_2=0.4,\ \alpha_3=0.2,$$

with $\tau_{ij}$ their (unspecified-sign) stress of the production term, $M_t$ the turbulent Mach number, which is
not defined in the paper, and the $\omega$-equation receiving the matching
terms (§2, Eq. 2-5; the $\alpha_i$ page-local, not the SST $\alpha$). On the
Settles supersonic cavity–ramp at $M=2.92$ the uncorrected model "produces
excessive turbulent viscosity" and a too dissipative, too wide shear layer,
while the corrected one reproduces the measured shear-layer velocity
profiles (§5.4, Figs. 5-14, 5-15). The authors write that DG RANS has
"rarely" included such a correction (§2).

### Discretization in a high-order solver

Zhao et al. (2023b) solve the mean flow with a high-order interior-penalty
discontinuous Galerkin method and the two SST equations with a first-order
cell-centred finite-volume scheme on the same mesh, with piecewise-constant
turbulence variables and the DG velocity gradients $L^2$-projected onto the
finite-volume space, "to pursue numerical stability and positivity" after
Burgess & Mavriplis (§1, §3.2; see
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md)). They
cite (§1) the opposite choice of Bassi et al., who solve for $\log\omega$ at high
order to enhance stability (§1).

Elzaabalawy et al. (2023) solve SST and BSL at high order with a
hybridizable DG method. Because the max and min functions of SST make the
eddy viscosity only $C^0$ inside an element, they evaluate it at quadrature
points and fit a degree-$N$ polynomial by regression; the derivative of the
fit "was found" unstable, so the diffusion terms are written in weak form
for SST and BSL (§3.2.1). In their flat-plate tests BSL and SST are less
robust than the unblended TNT and Wilcox (1998) models when the inlet eddy
viscosity is low, and they conclude that "the robustness of the SST model in
the high-order framework is questionable due to the polynomial regression",
excluding it from the rest of the study (§5.3), while recommending models
less sensitive to inlet turbulence, "such as SST", if the $C^0$ viscosity
can be handled (§7). The remedies common to the $k$-$\omega$ family
(interpolation of $1/\omega$, wall-element removal, scaling limiter on $k$ and
$1/\omega$) are on the [Wilcox $k$-$\omega$ page](/methods/k-omega-model.md).

### Implementation variants

Menter et al. (2022) document two departures from the textbook form in Ansys
Fluent's SST, both relevant to transition prediction
([Menter et al. (2022)](/sources/menter-2022.md), §2.1, Eqs. 6–7):

- the $\omega$ production is computed as $\alpha P_k/(\nu_t+0.001\nu)$ (in
  their density-weighted form, $\alpha\rho P_k/(\mu_t+0.001\mu)$) to avoid a
  division by zero; it has little effect in fully turbulent flow but a
  small noticeable influence on transition;
- the Langtry–Menter (2009) modification of $F_1$ is retained for
  transitional boundary layers,
  $$F_1=\max(F_{1,\mathrm{SST}},F_3),\qquad F_3=\exp\big[-(R_y/120)^2\big],\qquad R_y=\frac{d\sqrt k}{\nu},$$
  with the exponent 2 as Menter et al. print it (Eq. 7).

Menter et al. couple their algebraic transition model to SST or to GEKO, a
generalized $k$-$\omega$ model whose free coefficients users can change
"without negative effect on the integrity of the model" (§1, §2.1; Eq. 5).
The intermittency multiplies only the production $P_k$ of the $k$-equation,
not its destruction.

### The $\gamma$-$Re_\theta$ coupling and free-stream sustaining terms

In the $\gamma$-$Re_\theta$ model as implemented in STAR-CCM+ the coupling
is different: Carreño Ruiz & D'Ambrosio (2022) print the $k$-equation as

$$\rho\frac{Dk}{Dt}=\nabla\cdot\big[(\mu+\sigma_k\mu_t)\nabla k\big]+\gamma_{\mathrm{eff}}P_k-\min\big[\max(\gamma_{\mathrm{eff}},0.1),1\big]D_k,\qquad D_k=\rho\beta^*f_{\beta^*}(\omega k-\omega_0k_0),$$

so the effective intermittency $\gamma_{\mathrm{eff}}$ (page-local; see the
[transition-model page](/methods/local-correlation-based-transition-model.md))
also scales the destruction, between 0.1 and 1. $P_k$ collects shear,
nonlinear and buoyancy production, $f_{\beta^*}$ is a free-shear modification
factor, and $\omega_0$, $k_0$ are ambient values of the sustaining terms of
Spalart & Rumsey (2007), which keep the free-stream turbulence from decaying
between inlet and body ([Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md),
§2, Eqs. 1–3, §3.4). This is the "earlier" kind of coupling that Menter et
al. (2022) contrast with their production-only form. With the sustaining
terms active, the inlet ratio $\mu_t/\mu$ has an "almost negligible" effect
once it is large enough to avoid a dormant turbulence model; Carreño Ruiz &
D'Ambrosio use $\mu_t/\mu=1$, higher than the values Rumsey & Spalart (2009)
recommend for SST, arguing that those were meant for SST without a
transition model. At $Tu=0.43\%$ with $\mu_t/\mu=0.001$ or 0.01 the solution
is an inconsistent laminar one with negative lift (§3.4, Table 4).

### Separation, pressure-gradient and hybrid modifications

- **Wall-pressure-dependent $\beta^*$ and $Pr_t$ for shock interactions.**
  Yu et al. (2023b) print SST (Menter 1993, 1994, 2003 as cited) in
  compressible form with $\beta^*=0.09$, $\alpha=(5/9,0.44)$,
  $\beta_\omega=(3/40,0.0828)$, $\sigma_k=(0.85,1)$, $\sigma_\omega=(0.5,0.856)$
  and the limiter $\mu_t=a_1k/\max(a_1\omega,SF_2)$ with $a_1$ not given
  ([Yu et al. (2023b)](/sources/yu-2023-b.md), §V, Eqs. 27–33). From an a
  priori test on their Mach 5 oblique-shock DNS they take $\beta^*$, which
  they call equivalent to $C_\mu$, as
  $\beta^*(x)=0.09/[1+C_{\mu,1}(\langle p_w\rangle(x)/\langle p_w\rangle_r-1)]$
  ($C_{\mu,1}$ page-local, 1 in the DNS fit; details on
  [$k$-$\varepsilon$ models](/methods/k-epsilon-model.md)), and set
  $Pr_t=0.9-0.5\tanh(10\lvert\nabla p\,\delta/U_\infty\rvert)$ (see
  [turbulent Prandtl number](/definitions/turbulent-prandtl-number.md)) (§IV,
  Eq. 21; §V). Their rationale: lowering $C_\mu$ lowers the modelled
  dissipation in the $k$ equation and raises $k$ and the shear stress, while
  the $\omega$ equation ties the dissipation of mean and turbulent kinetic
  energy, whereas the separated shear layer raises production without
  instantly raising the turbulent dissipation (a cascade delay), so that
  $\omega$ is overpredicted downstream (§V). Evidence is under Evidence below.
- **Separation fix.** Yan et al. (2022, §1) cite Rumsey's fix of SST, a
  multiplier $F_{sf}$ that increases the $\omega$ destruction in separating
  shear layers where production greatly exceeds dissipation (formula not
  printed), and Rumsey's finding that enhanced mixing there improves the
  periodic hill but worsens backward-facing-step flows; their own field
  inversion of the SA model localizes its corrections in the same region
  ([Yan et al. (2022)](/sources/yan-2022.md), §1, §3.2, Fig. 11; see the
  [SA page](/methods/spalart-allmaras-model.md)).
- **Adverse pressure gradient.** Knopp (2022) describes, in words only, a
  preliminary augmentation term in the $\omega$-equation of
  "$k$-$\omega$ type" models (Knopp 2016) that reproduces a half-power law
  above the log law, activated by a blending function built from Knopp's
  correlations in $y^+$, $Re_\tau$ and the pressure-gradient parameter
  ([Knopp (2022)](/sources/knopp-2022.md), §1; see
  [wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)).
- **Hybrid forms.** SST is the base of the DDES ("DDES-SST") and IDDES
  models of the ISIS-CFD solver ([Mozaffari et al. (2022)](/sources/mozaffari-2022.md),
  §2; see [detached-eddy simulation](/methods/detached-eddy-simulation.md)).
  Carlsson et al. (2023) use SST-DDES and SST-IDDES (after Gritskevich et
  al.), in which the low-Reynolds-number correction of the LES length is
  not needed ($\Psi=1$); in LES mode on decaying isotropic turbulence the
  constant of the $k$-$\varepsilon$ branch, $C_{\mathrm{DES}}=0.61$, reproduces
  the measured spectra with a low-dissipation scheme, and the
  $k$-$\omega$-branch value 0.78 gives "nearly identical results" (not shown)
  ([Carlsson et al. (2023)](/sources/carlsson-2023.md), §3, §4.2). SST-IDDES
  of channel flow at $M_b=0.15$ and 1.5 then follows DNS and the log law
  except for a small log-layer mismatch at the interface (§4.3).
  Delassaux et al. (2023) blend the two constants through $F_1$,
  $C_{\mathrm{DES}}=0.78F_1+0.61(1-F_1)$, and use $C_{d1}=20$, $C_{d2}=3$ in the
  DDES shielding function, raising $C_{d1}$ to 30 for more shielding
  (§4.1.3, Eqs. 6–11, §4.4).
  Wang et al. (2021) derive these two constants from the length-scale
  equation and the Smagorinsky constant $C_s=0.18$: the theoretical values
  are 0.805 for the $k$-$\omega$ branch and 0.630 for the
  $k$-$\varepsilon$ branch, "with calibration values of 0.78 and 0.61",
  blended through $F_1$, with the RANS length $\sqrt k/(C_\mu\omega)$
  ([Wang et al. (2021)](/sources/wang-2021-l.md), §2.3, Eqs. 17–18; details
  on the [DES page](/methods/detached-eddy-simulation.md)). Yang & Ma (2022)
  use the SST-DES of ANSYS CFX, in which the $k$ destruction is multiplied
  by $\max\big(L_t(1-F_2)/(C_{\mathrm{DES}}\Delta),1\big)$ with
  $L_t=\sqrt k/(\beta^*\omega)$, $C_{\mathrm{DES}}=0.61$ and $\Delta$ the
  largest cell edge, $F_2$ serving as shielding against grid-induced
  separation and modelled-stress depletion
  ([Yang & Ma (2022)](/sources/yang-2022-b.md), §2.1, Eqs. 1–5; page-local
  $L_t$). Thawait et al. (2023) print the SST-DDES of ANSYS Fluent with the
  same structure and the DDES shielding function in place of $F_2$: the
  $k$ destruction is $\rho\beta^*k\omega F_{\mathrm{DES}}$ with
  $$F_{\mathrm{DES}}=\max\Big(\frac{L_t}{C_{\mathrm{DES}}\Delta_{\max}}(1-F_{\mathrm{DDES}}),1\Big),\qquad
  F_{\mathrm{DDES}}=\tanh\big[(C_{d1}r_d)^{C_{d2}}\big],\qquad
  r_d=\frac{\nu_t+\nu}{\kappa^2d^2\sqrt{0.5(S^2+\Omega^2)}},$$
  $C_{\mathrm{DES}}=0.61$, $C_{d1}=20$, $C_{d2}=3$, $\kappa=0.41$, $\Delta_{\max}$
  "the grid spacing" and $S$, $\Omega$ the strain-rate and vorticity
  magnitudes, whose normalization is not stated (page-local
  $F_{\mathrm{DES}}$, $F_{\mathrm{DDES}}$, $\Delta_{\max}$; [Thawait et al. (2023)](/sources/thawait-2023.md),
  §II B, Eqs. 6–13). Their eddy viscosity is written
  $\mu_t=(\rho k/\omega)/\max[1/\alpha^*,SF_2/(a_1\omega)]$ (Eq. 8), with
  $\alpha^*$ and $a_1$ not given and $\beta^*$ "calculated using $\rho$, $k$,
  $\mu$, and $\omega$"; the authors state, from the Fluent theory guide,
  that SST "accounts for the transport of the turbulent shear stress and is
  more accurate than the standard version", and that the limiter is applied
  because standard $k$-$\omega$ "overpredicts the eddy viscosity". With
  $F_{\mathrm{DDES}}\to1$ the factor is $F_{\mathrm{DES}}=1$, the SST
  destruction *(compiler check, not in the sources)*. See [ANSYS Fluent](/software/ansys-fluent.md). Zangeneh (2021) runs SST-IDDES (after Gritskevich et al. 2012)
  as a wall-modelled LES of supersonic flows, solving the RANS inner
  layer on an auxiliary wall grid embedded in the coarse LES mesh; in the
  printed $k$ equation the destruction is $\rho\sqrt{k^3}/l_{\mathrm{IDDES}}$,
  with $l_{\mathrm{IDDES}}$ the IDDES blend of the RANS and LES lengths, and
  the eddy viscosity keeps the SST limiter
  $\mu_t=\rho a_1k/\max(a_1\omega,F_2S)$, with $S$ a strain measure the
  source does not define (page-local); no coefficient is printed, the paper
  referring to Gritskevich et al.
  ([Zangeneh (2021)](/sources/zangeneh-2021.md), §II.A–B, Eqs. 1, 5–7;
  see [detached-eddy simulation](/methods/detached-eddy-simulation.md) and
  [wall-modelled LES](/methods/wall-modelled-les.md)).
- **Roughness.** D'Ayer et al. (2026) cite roughness corrections of SST
  (Aupoix, their ref. [7]) among the roughness models whose development
  their rough-wall DNS databases are meant to support
  ([D'Ayer et al. (2026)](/sources/dayer-2026.md), §1, refs. [6]–[8]; HAL
  submitted manuscript).

- **A $k$-$\tau$ successor.** Tomboulides et al. (2025) list an SST
  version of their [$k$-$\tau$ model](/methods/k-tau-model.md) as the
  basis of a planned DDES, after Gritskevich et al.
  ([Tomboulides et al. (2025)](/sources/tomboulides-2025.md), §4).
  Kumar et al. (2025) build it in Nek5000: the $k$-$\tau$ SST, with the SST
  functions $F_1$, $F_2$ and the eddy-viscosity limiter written in
  $\tau_t=1/\omega$ and the SST constants $\gamma_{\omega1}=5/9$, $\beta_{\omega1}=0.075$,
  $\sigma_{k1}=0.85$, $\sigma_{\omega1}=0.5$, $\gamma_{\omega2}=0.44$,
  $\beta_{\omega2}=0.0828$, $\sigma_{k2}=1$, $\sigma_{\omega2}=0.856$, $a_1=0.31$, is
  the host of their DDES; the appendix prints the $\omega$ form with the
  production limiter $\min(\mu_t\lvert S\rvert^2,10C_\mu\rho k\omega)$ and the same
  constants, and its DDES with $l_{\mathrm{RANS}}=\sqrt k/(C_\mu\omega)$
  ([Kumar et al. (2025)](/sources/kumar-2025.md), §2.1–§2.2, Eqs. 11–28,
  App. A.5–A.6; see the [$k$-$\tau$ model](/methods/k-tau-model.md) and
  [detached-eddy simulation](/methods/detached-eddy-simulation.md)).
- **Transitional DDES.** Möller et al. (2024) couple SST-DDES to the
  one-equation $\gamma$ model by multiplying the production of $k$ by
  $\gamma$ and the DDES destruction by $\max(0.1,\gamma)$
  (§II.B.3; see [detached-eddy simulation](/methods/detached-eddy-simulation.md)).
- **SST-IDDES as a comparator.** Li et al. (2022) and Wu et al. (2023) use
  SST-IDDES (Gritskevich et al.) as the reference hybrid. On the transonic
  hammerhead buffet it breaks up the separated shear layer later than the
  Reynolds-stress IDDES forms and gives a $C_p$-RMS of 0.0897 at the
  location of the experimental maximum (0.0454), which Li et al. attribute,
  after Spalart, to its larger modelled stress in the shear-layer extension
  ([Li et al. (2022)](/sources/li-2022-k.md), §III C, Figs. 15–18); on the
  30P30N airfoil it underpredicts lift by 19.8%, with early flap separation
  and large eddy viscosity in the slat cove (Wu et al. 2023, §3.4, Table 2;
  both on the [DES page](/methods/detached-eddy-simulation.md)). Mani &
  Dorgan (2023) list SST-based variants of DES (Bush & Mani; Strelets;
  Winkler et al.) beside the SA-based original at Boeing
  ([Mani & Dorgan (2023)](/sources/mani-2023.md), §4.5.2).
- **SST-DES and SST-DDES in OpenFOAM, with a filtered eddy viscosity.**
  Guo & Wang (2025) print Strelets' SST-DES in the zonal form
  $l_{\mathrm{DES}}=\min\big[l_{\mathrm{RANS}},\,C_{\mathrm{DES}}\Delta/(1-F_{\mathrm{SST}})\big]$,
  $l_{\mathrm{RANS}}=\sqrt k/(\beta^*\omega)$, with $F_{\mathrm{SST}}$ "either
  $F_1$ or $F_2$", the $k$ destruction $\rho k^{3/2}/l_{\mathrm{DES}}$ and a
  vorticity-based production $\mu_t\lvert\Omega\rvert^2$; the eddy viscosity
  $\nu_t=a_1k/\max(a_1\omega,\lvert\Omega\rvert F_2)$ with $a_1=0.31$ and
  $\sigma_{\omega2}=0.856$ (Eqs. 1–5). Their SST-DDES follows Gritskevich et
  al. with $f_d=1-\tanh[(20r_d)^3]$ and the LES coefficient printed as
  $C_{\mathrm{DDES}}=0.78F_1+0.61F_2$ (Eqs. 6–9), where Delassaux et al.
  write $0.78F_1+0.61(1-F_1)$ (above). On this base they multiply the
  eddy viscosity by $\big(\min(L_t,\Delta_{\mathrm F})/L_t\big)^{4/3}$, with
  $L_t=\sqrt k/(\beta^*\omega)$ and a resolvable filter width $\Delta_{\mathrm F}$
  built from the time step and the grid (page-local $L_t$, $\Delta_{\mathrm F}$), and
  switch the grid scale between the largest cell edge and a least-squares
  length by flow region, the ADD-SSTFDDES model of the
  [DES page](/methods/detached-eddy-simulation.md)
  ([Guo & Wang (2025)](/sources/guo-2025.md), §2.1, Eqs. 10–15). Their
  OpenFOAM $\omega$ wall function sets $\omega_w=6\nu/(\beta_1y^2)$ with
  $\beta_1=0.075$ (Eq. 20; see [RANS wall functions](/methods/rans-wall-function.md)).

### Data-driven corrections of SST

- **Conditioned field inversion.** Wu et al. (2025) multiply the
  $\omega$-destruction $\beta_\omega\omega^2$ by a spatial field
  $\beta(\boldsymbol x)$, which classic field inversion lets act everywhere
  and which, by the log-layer condition above, spoils the calibration
  wherever it differs from one; they gate it as
  $\big[(\beta(\boldsymbol x)-1)f_d+1\big]\beta_\omega\omega^2$, with $f_d$ the DDES
  shielding function, so that the model is SST inside attached boundary
  layers ([Wu et al. (2025)](/sources/wu-2025.md), §2.1, Eqs. 2–6;
  authors' manuscript; $\beta_\omega$ is the SST coefficient $\beta$ of the
  equations above, which the source calls $\theta$). Symbolic fits of the inverted fields add about 10–15% to the
  run time (§3.2). Details on the
  [field-inversion page](/methods/field-inversion-machine-learning.md) and
  [model-form uncertainty](/definitions/model-form-uncertainty.md).
- **Tensor-basis corrections and their blending.** Oulghelou et al. (2025)
  add a symbolic extra-anisotropy and a $k$-equation production correction
  to SST and blend several such experts in space (§2–§3; see the
  [Boussinesq page](/definitions/boussinesq-hypothesis.md) and
  [turbulence-model aggregation](/methods/turbulence-model-aggregation.md)).
- **Wall-flux correction of an SST-IDDES.** Zangeneh (2021) leaves the
  SST-IDDES equations untouched and corrects its outputs: a random forest
  predicts the error of the wall shear stress and wall heat flux of the
  baseline from local mean-flow features, and the corrected values are used
  to correct $\mu_t$ and $Pr_t$, which are fed back to the solver, "a
  corrective approach and not 'standard' turbulence model"; how $\mu_t$ and
  $Pr_t$ are obtained from the corrected fluxes is not printed (§II.F–G,
  §III; details on the
  [machine-learning wall-model page](/methods/machine-learning-wall-model.md)).
- **Production correction from a frozen solve.** Cherroud et al. (2022)
  correct SST by an extra anisotropy $b^\Delta_{ij}$ in the stress and a
  residual $R$ added to the production of both the $k$- and the
  $\omega$-equation, the latter as $(\gamma_\omega/\nu_t)(P_k+R)$, with the
  production limited to $10\beta^*\omega k$; the targets come from solving
  the two equations with the high-fidelity mean velocity, $k$ and
  anisotropy frozen, so that $\omega$ and $R$ are consistent with the SST
  transport equations ([Cherroud et al. (2022)](/sources/cherroud-2022.md),
  §2.1, Eqs. 9–13; constants "found in Menter 1992", not printed; no
  cross-diffusion or blending term is printed in their Eq. 10). Their
  selected sparse-Bayesian models keep $b^\Delta=0$ and a single production
  term on $T^{(1)}$, which raises the eddy viscosity in the separated
  region; details and coefficients on the
  [explicit algebraic Reynolds-stress model](/methods/explicit-algebraic-reynolds-stress-model.md)
  page. Sandberg & Zhao (2022) review the same SpaRTA-type correction as
  tractable for 3-D flows ([Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md),
  §3.4, Eq. 8, §4.1).

### Implementation in a lattice Boltzmann solver

Mozaffari et al. (2024) implement SST, and SST-based IDDES and continuous
eddy simulation, in a research version of the lattice Boltzmann solver
[ProLB](/software/prolb.md), claiming that SST "has never been used in the
standard LBM framework", a non-standard finite-volume lattice Boltzmann
method on unstructured grids being the one precedent they cite
([Mozaffari et al. (2024)](/sources/mozaffari-2024.md), §1, lines 43–46,
68–69; HAL accepted manuscript). They print the model of the Equations
section with the limiter $\nu_t=(k/\omega)/\max\{1,\lvert\Omega\rvert F_2/(a_1\omega)\}$,
$a_1=0.31$, $\lvert\Omega\rvert$ "the absolute value of the vorticity", and
$0.09$ in place of $\beta^*$ inside $F_1$ and $F_2$ (§2.3, Eqs. 16–21), the
same rotation-based limiter as Dzanic et al. and the same literal 0.09 as
Zhao et al. (2023b); no other coefficient is printed. The eddy viscosity
enters the lattice Boltzmann scheme only through the relaxation time (see
[lattice Boltzmann methods](/methods/lattice-boltzmann-method.md)). The two
transport equations are solved by finite differences on the Cartesian grid
inside the collision step: fourth-order centred derivatives, one-sided
differences at walls, second-order centred differences at grid-level
transitions, and a hybrid centred/upwind TVD advection with a modified
Van Albada limiter calibrated on an inclined flat plate to avoid large
$\omega$ fluxes near the wall (§2.3, lines 201–209). Wall values of $k$
and $\omega$ come from wall functions that switch at $y^+=11.06$ (after
Kalitzin et al.) between the viscous-sublayer values
$k=C_ku_\tau^2y^{+3.23}$, $\omega=6u_\tau^2/(\nu\beta_1y^{+2})$ and the
log-layer values $k=u_\tau^2/\sqrt{C_\mu}$, $\omega=u_\tau^2/(\nu\sqrt{C_\mu}\kappa y^+)$,
with an optional blend of the two $\omega$ values after Knopp et al.
($C_k$, $\beta_1$, $C_\mu$ not given values; §2.3, Eqs. 22–25).

### PANS form with a dynamic resolution parameter

Petrocchi & Barakos (2024) print the compressible SST-PANS model of Luo et
al. that their HMB3 solver uses, with the unresolved $k_u$, $\omega_u$
written without subscripts
([Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md), §2, Eqs. 3–5):
the diffusion coefficients and the cross-diffusion term carry the factor
$f_\omega/f_k$, the $\omega$-destruction coefficient becomes

$$\beta'=\alpha\beta^*-\frac{\alpha\beta^*}{f_\omega}+\frac{\beta}{f_\omega}$$

(the source's $\gamma$ is the registry's SST $\alpha$), and the limiter is
$\mu_t=\min(\rho k/\omega,\ \rho a_1k/(\lvert S\rvert F_2))$ with $a_1=0.31$,
a strain magnitude whose normalization is not printed. At $f_\omega=1$,
$\beta'=\beta$ *(compiler check, not in the sources)*. This $\beta'$
multiplies $\rho\omega^2$, so Petrocchi & Barakos's destruction has the
dimensions of the left side, unlike the bracket printed by Dzanic et al.
(see Qualifications) *(compiler check, not in the sources)*. Their
dynamic $f_k$ and its effect on buffet are on the
[PANS page](/methods/partially-averaged-navier-stokes.md).

## What the transported $k$ represents

Haering et al. (2022) exclude SST as the base model of their
[active model split](/methods/active-model-split.md) method because its $k$
is, in attached boundary layers, "more akin to $\tfrac32v^2$" ($v^2$ the wall-normal velocity variance of a $v^2$-$f$ model, page-local) than
to the turbulent kinetic energy; AMS needs a $k$-equation whose $k$ is the
kinetic energy, and they use a low-Reynolds $k$-$\varepsilon$ model and a
$v^2$-$f$ model instead ([Haering et al. (2022)](/sources/haering-2022.md),
§IV B, p. 14). The statement is asserted, without a figure. Duraisamy (2021)
makes the general point that a RANS model's secondary variables play an
operational role and need not match their DNS counterparts
([Duraisamy (2021)](/sources/duraisamy-2021.md), §IV.A).

## Evidence

- **High-lift aircraft.** In the AIAA Third High-Lift Prediction Workshop most
  submissions were steady RANS with Spalart–Allmaras or SST variants; they
  cluster in the linear lift range and scatter widely near maximum lift,
  which motivates the wall-modelled LES of Goc et al.
  ([Goc et al. (2021)](/sources/goc-2021.md), §1, Fig. 1;
  [JAXA Standard Model](/benchmarks/jaxa-standard-model.md)). Mani &
  Dorgan (2023) name Menter's SST, with SA and its rotation–curvature and
  quadratic-constitutive variants, as Boeing's workhorse RANS models for
  design, analysis and risk mitigation (Lockheed Martin's Falcon code uses
  Smith's $k$-$l$ model); all "work well for attached flows, and flows with
  small amounts of separation", but can be inadequate where large
  separation dominates, as at high angle of attack, and they reproduce the
  workshop RANS lift curves (§4.5.1, Figs. 6, 12).
- **Transition.** With the algebraic intermittency of Menter et al. (2022),
  SST reproduces the ERCOFTAC T3 plates, a separated flat plate, four
  airfoils and a turbine cascade with accuracy similar to the transport
  transition models; see the
  [transition-model page](/methods/local-correlation-based-transition-model.md).
- **Very-low-Reynolds airfoils.** Coupled to $\gamma$-$Re_\theta$, SST
  reproduces the two-dimensional transition of airfoils at
  $Re=2\times10^4$–$2\times10^5$ "with an accuracy that increases with the
  Reynolds number", but gives too little skin friction after reattachment,
  which can lead to early stall (Carreño Ruiz & D'Ambrosio 2022, §3.5, §7;
  details on the transition-model page).
- **Fan stage.** François et al. (2022) compare SST and Smith $k$-$l$ RANS
  (5 million cells, one rotor and one stator channel) with zonal DES and
  hot-wire data behind a turbofan fan: tangential and radial mean velocities
  are close to the DES, the axial velocity is off by $+6$–$7\%$ (attributed
  to an over-estimated tip-gap flow area), the wakes are narrower, and in
  the tip gap RANS over-estimates the main dip and peak by a factor of two
  and gives the wrong shape of the RMS profiles, reconstructed through the
  [Boussinesq](/definitions/boussinesq-hypothesis.md) relation
  ([François et al. (2022)](/sources/francois-2022.md), §5.3–5.4, Figs. 12–15).
  On the same [ACAT1 stage](/benchmarks/acat1-fan-stage.md) Lewis et al.
  (2023) find that a wall-resolved SST RANS reproduces the measured mass
  flow and fan pressure ratios as closely as their coarser wall-modelled
  LES, but misses the radial secondary flows predicted by both LES and gives
  worse RMS wake shapes; its rotor leading-edge separation extends from 25%
  of the span to the tip ([Lewis et al. (2023)](/sources/lewis-2023.md),
  §4.1, §4.2.2, §4.3.1, Tables 9–10; HAL accepted manuscript).
- **Low-pressure turbine cascade.** Morsbach et al. (2024) compare SST
  (with $\gamma$-$Re_\theta$) and the SSG/LRR-$\omega$ differential
  Reynolds-stress model with a wall-resolved high-order implicit LES of the
  T161 cascade at an exit Reynolds number of $9\times10^4$ and Mach 0.6, with
  inflow turbulence tuned so that the RANS free-stream decay matches the LES
  (§3.3). Both RANS miss the midspan
  [laminar separation bubble](/definitions/laminar-separation-bubble.md) and
  underestimate the mixed-out wake loss by 35% (SST) and 29% (SSG/LRR-$\omega$);
  SST with the inflow length scale reduced to $1/16.7$ gets within 2.7% by
  "a lucky cancellation of errors" while leaving an open separation (§4.1,
  Figs. 7–9). In the end-wall region both overpredict the peak loss, by 34%
  (SST) and 48% (SSG/LRR-$\omega$), with passage and trailing shed vortices
  too strong and too far from the wall. SST qualitatively reproduces the
  elevated $k$ in the passage-vortex core, while the Reynolds-stress model
  produces too little $k$ there and too compact, persistent vortices,
  "contrary" to the reputation of such models as less diffusive for
  vortices; it does reproduce the free-stream anisotropy that SST, through
  the Boussinesq relation, cannot (§4.2, Figs. 10–15). The authors question
  its high-Reynolds formulation, with the LRR pressure–strain near walls and
  no explicit near-wall terms (§4.2).
- **Full-scale car.** On a simplified estate car at $Re_L=1.3\times10^7$
  Delassaux et al. (2023) find SST drag 0.242 against 0.244 measured (0.241
  with 30 prism layers, 0.249 on a refined wake grid), but two massive
  separation bubbles in the wake where the experiment has one, massive
  separation behind the rear fairing, and the best pressure coefficient of
  all models on rounded separation lines (§6–§7, Table 3, Figs. 17–23); on
  the 25° Ahmed body SST separates massively on the slant (§5). See
  [k-ε models](/methods/k-epsilon-model.md) and
  [detached-eddy simulation](/methods/detached-eddy-simulation.md).
- **Airfoils with a DG discretization.** With the hybrid DG/finite-volume
  scheme above, Zhao et al. (2023b) obtain on NACA 0012 ($M=0.15$,
  $Re_c\approx6\times10^6$) $C_L=0.00$, $C_D=0.0084$ at $0^\circ$ and $C_L=0.93$,
  $C_D=0.011$ at $10^\circ$, against McCroskey's 0.00, 0.0083, 1.05 and 0.012,
  attributing the $10^\circ$ lift deficit to "the RANS assumption"; at
  $M=0.804$ the shock end lags slightly behind the ONERA data (§5.2–5.3,
  Table 5-1). The zero-pressure-gradient flat plate at $M=0.2$,
  $Re_L=1.12\times10^7$ agrees with the reference log-layer velocity and
  $k$ profiles (§5.1, Fig. 5-2).
- **Delta wing.** On a hybrid delta wing at $\alpha=24^\circ$,
  $Re=2.17\times10^6$, SST on a 60-million-cell adapted mesh (steady
  solution, instantaneous refinement criterion) predicts forces and the
  experimental vortex features well, as does DDES-SST (which over-predicts
  the core velocity peaks and the kinetic energy of the first vortex),
  while the SSG/LRR-$\omega$ Reynolds-stress model gives an unsteady, smeared vortex with too much
  kinetic energy (Mozaffari et al. 2022, §5.2, Figs. 26–27).
- **Hypersonic heat flux.** Huang et al. (2022, §1) state, citing Rumsey (2010) and Gnoffo et al. (2013), that SA and SST predict
  hypersonic zero-pressure-gradient heat flux less accurately than algebraic
  models with compressibility corrections
  ([Huang et al. (2022)](/sources/huang-2022.md)).
- Alauzet et al. (2022) name a comparison of SA and SST on mesh-converged
  adapted meshes as future work ([Alauzet et al. (2022)](/sources/alauzet-2022.md), §9).
- **Ahmed body.** Cai et al. (2022) cite Menter & Kuntz, who ran
  $k$-$\varepsilon$ and SST with wall models and obtained fully separated
  flow on the 35° slant but a 25° case "much more sensitive to the
  numerical schemes and the turbulence models", improved with DES; in
  Guilmineau et al.'s body-fitted comparison at 35° and $Re_H=7.68\times10^5$
  SST gives a drag coefficient of 0.2999 and EARSM 0.2603 against 0.279
  measured by Meile et al. ([Cai et al. (2022)](/sources/cai-2022.md), §I,
  Table III).
- **PANS.** Dzanic et al. (2022) use SST as the PANS closure on the
  [periodic hill](/benchmarks/periodic-hill.md) and the circular cylinder at
  $Re_D=3900$, with high-order flux reconstruction.
- **Transonic buffet.** On the OAT15A supercritical airfoil at
  $M_\infty=0.73$, $Re_c=3\times10^6$, Petrocchi & Barakos (2024) find that
  SST URANS in HMB3 predicts no self-sustained shock oscillation at
  $\alpha=3.5^\circ$, in two dimensions (even at $3.9^\circ$) and in a
  three-dimensional model of half the wind tunnel, where it converges to a
  steady state, while SST-PANS on the same grids predicts buffet (§4.3,
  §4.5.5, Table 2). They attribute the three-dimensional failure to
  excessive corner separation at the wing–wall junction, which deflects the
  trailing-edge flow spanwise and keeps the shock-foot and trailing-edge
  separations apart, and to too high a post-shock eddy viscosity (§4.5.5).
  Their compilation of earlier URANS of this case shows wide scatter
  between models and solvers, with Thiery & Coustols reporting buffet with
  SST in [elsA](/software/elsa.md) (App. A, Table A.4).
- **Lattice Boltzmann airfoils and bluff bodies.** In ProLB, SST and
  Spalart–Allmaras RANS give close eddy-viscosity fields on the NACA 23012
  at $Re_c=1.88\times10^6$, $M=0.18$, except at $0^\circ$, where SST gives
  a lower $\nu_t$; lift coefficients are 0.12, 0.83, 1.12 (SST) and 0.12,
  0.79, 1.175 (SA) against 0.12, 0.79, 1.07 measured at $0^\circ$,
  $6.2^\circ$, $9.3^\circ$, and the drag error grows with incidence,
  largest for SST at $9.3^\circ$ (Mozaffari et al. 2024, §3.1, Table 1,
  Figs. 4–5). On the three-dimensional NACA 0012 at $Re_c=3\times10^6$ and
  $45^\circ$, SST RANS gives $C_L=2.238$, $C_D=2.053$ against reference
  values of 1.097 and 1.180, which the SST-based hybrids bring to
  1.23/1.04 (IDDES) and 1.19/0.99 (CES) (§3.2, Table 2; see
  [hybrid RANS/LES](/definitions/hybrid-rans-les.md)).
- **Compressor cascades.** Liu et al. (2024) find that SST overpredicts
  the suction-side corner separation of the PVD linear compressor cascade
  ($Re\approx2.3\times10^5$) at $-7^\circ$ and $0^\circ$ incidence, predicts
  an endwall separation at $0^\circ$ "much larger" than measured and
  underpredicts $C_p$ over 50–100% of the axial chord; the fully turbulent
  SSG/LRR-$\omega$ Reynolds-stress model is "only slightly more accurate"
  ([Liu et al. (2024)](/sources/liu-2024.md), Figs. 8–13, Conclusions; see
  [Reynolds-stress models](/methods/reynolds-stress-model.md)). On the
  ERCOFTAC T3 flat plates, fully turbulent SST and SSG/LRR-$\omega$ have
  similar accuracy (Fig. 6). The SST $F_1$ is the function that blends the
  inner and outer coefficient sets of SSG/LRR-$\omega$ (Eq. 9).
- **Host of a laminar-kinetic-energy transition model.** Pacciani et al.
  (2025) couple their reformulated
  [laminar-kinetic-energy model](/methods/laminar-kinetic-energy-transition-model.md)
  to SST through an intermittency that multiplies $P_k$ and, bounded below
  by 0.1, the destruction, keeping the SST limiter
  $\mu_t=\rho a_1k/\max(a_1\omega,F_2\lvert S\rvert)$
  ([Pacciani et al. (2025)](/sources/pacciani-2025.md), §4.2, Eqs. 15–18,
  App. A Eq. A14). They chose SST over the Wilcox $k$-$\omega$ model for its
  "more reliable response to freestream turbulence": with Wilcox's model
  the leading-edge heat transfer of the VKI LS89 vane stayed below the
  measurements even with an exaggerated inlet length scale, and the
  realizability constraint was "mandatory" for physically consistent
  results (§4.2, §6.1). With the same transition model, Wilcox $k$-$\omega$
  gives the same onset on T3A as SST but a quicker transition and a
  different turbulent $C_f$, so the constants "should be retouched" per
  host model (§5.1.1, Fig. 5).
- **Separated flows as baseline of data-driven corrections.** Wu et al.
  (2025) find SST overpredicting separation in every separated case they
  test: it reattaches too late on the curved backward-facing step, does not
  reattach before the next hill on the parametrized periodic hill
  ($Re=5600$, slope parameter 0.8; DNS reattachment near $x=5.2$),
  stalls early on the NLR-7301 two-element airfoil ($C_{L,\max}=2.84$ at
  $11.1^\circ$ against 3.03 at $14.1^\circ$ measured; $Re=2.51\times10^6$),
  underpredicts the drag of the SAE notchback (0.181 against 0.207) and
  separates from the start of the slant of the $25^\circ$
  [Ahmed body](/benchmarks/ahmed-body.md), where they state that the
  experiment stays attached (velocity-profile error 0.677; the slant
  topology is disputed between sources, see that page's Contradictions); their conditioned symbolic
  correction gives 3.00 at $13.1^\circ$, 0.211 and 0.072 (§4.1–4.4, Tables
  5–7). On the zero-pressure-gradient flat plate and the NACA 0012 at
  $0^\circ$, SST is the reference the corrections must reproduce (§4.5).
  Oulghelou et al. (2025) report SST separation lengths, in units of the
  case length, of 7.42 on the [periodic hill](/benchmarks/periodic-hill.md)
  ($Re=10\,595$; LES 4.49), 3.41 on a converging–diverging channel (DNS
  0.85) and 3.59 on the curved step (LES 3.55); on the
  [NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md) at
  $Re=9.36\times10^5$ its bubble extends from $x/c=0.62$ to 1.24 against
  1.15 measured (Tables 6, 11). On the
  [zero-pressure-gradient boundary layer](/benchmarks/turbulent-boundary-layer.md)
  SST beats all their corrected models (mean absolute $C_f$ error
  $8.4\times10^{-5}$; Table 9).
- **Three 2-D separated flows with uncertainty bands.** Cherroud et al.
  (2022) take SST in OpenFOAM as the baseline of their learned corrections
  on the [periodic hill](/benchmarks/periodic-hill.md) ($Re=10\,595$), a
  converging–diverging channel ($Re=12\,600$) and the curved
  [backward-facing step](/benchmarks/backward-facing-step.md)
  ($Re=13\,700$): SST overpredicts the separation size on all three, and
  the corrected models improve velocity and $C_f$, with $\pm3\sigma$ bands that
  widen where they depart from the high-fidelity data; they overpredict $k$
  in the separated regions, miss the small bubble of the channel, and on
  the curved step their $C_f$ in attached regions is slightly worse than
  SST's (§4.2, Figs. 5–7).
- **Jet in crossflow and cooling slots.** Sandberg & Zhao (2022) show
  steady SST RANS with an eddy-diffusivity heat flux ($Pr_t=0.9$) against
  DNS of a jet in crossflow (jet Reynolds number 12 500, blowing ratio
  0.5): reduced spanwise spread of wall temperature, an underpredicted
  horseshoe vortex, a spanwise velocity of the wrong sign off the axis and
  a much too small heat flux near the wall; SST URANS (Menter et al. 2003)
  with $Pr_t=0.9$ is the baseline of their trailing-edge-slot closures
  (§2.3 Fig. 5, §4.4.2 Fig. 11; see the
  [Boussinesq page](/definitions/boussinesq-hypothesis.md) and
  [spectral gap](/definitions/spectral-gap.md)).
- **Hypersonic shock/boundary-layer interactions.** With the refinement
  above, Yu et al. (2023b) compute the Schülein Mach 5 oblique-shock
  experiments ($14^\circ$, $10^\circ$ wedges; unit Reynolds number
  $3.7\times10^7$/m) and the Holden et al. Mach 8 compression ramps
  ($27^\circ$, $30^\circ$, $33^\circ$; $600\times250$ grid) by steady RANS with
  fifth-order WENO (§V, Figs. 21–24). On the oblique shocks $C_f$ improves and
  the error of the Stanton-number maximum falls from about 50% to below 10%.
  Against their DNS, the original SST underpredicts $k$ and the shear stress
  globally; the refined model is better downstream but still inaccurate
  inside the interaction, where a nonlinear stress term would be needed,
  "not necessary" if only wall quantities matter (Fig. 22). On the ramps the
  original SST overpredicts separation at $27^\circ$ and $30^\circ$ and
  underpredicts it at $33^\circ$; the refined one gives the onset and plateau
  at $33^\circ$ almost exactly and no separation at the smallest angle, as
  measured (Figs. 23–24). See
  [shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).
- **Supersonic film cooling with combustion.** Wei et al. (2023) use SST RAS
  as the precursor of their wall-resolved LES of the Burrows–Kurkov hydrogen
  film (Ma 2.44) and compare the two (§IV F, Figs. 36–37): RAS over-predicts
  the wall fluxes, shows no combustion-induced friction reduction and a
  strong heat-flux increase with combustion, inconsistent with experiment
  and with the LES. They attribute this to isotropic eddy-viscosity
  modelling, estimating that an isotropic redistribution of the
  $0.6:0.2:0.2$ split (LES, streamwise to wall-normal to spanwise) of the kinetic energy would raise the wall-normal
  fluctuation substantially, and recommend v2f or Reynolds-stress models
  ([Wei et al. (2023)](/sources/wei-2023.md); see the
  [turbulent Prandtl number](/definitions/turbulent-prandtl-number.md) and
  [Reynolds-stress models](/methods/reynolds-stress-model.md)).
- **SST-IDDES as comparator of a hybrid.** On a supercritical cylinder at
  $Re_D=3\times10^6$ SST-IDDES gives $St=0.29$, $C_{pb}=-0.68$, $L_r/D=0.63$,
  $C_D=0.62$, a drag the authors call satisfactory and a delayed separation
  point, where SATES-SM predicts the subcritical topology; on the MD-30P30N
  airfoil its $C_p$ is less accurate than that of SATES-σ (Wu et al. 2024, §3.2–§3.3,
  Table 3; see the [SATES page](/methods/self-adaptive-turbulence-eddy-simulation.md)
  and [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)).
- **Transonic bump with QCR.** On the axisymmetric transonic bump of
  Bachalo & Johnson ($Re_c=2.763\times10^6$, $M_\infty=0.6$–$0.925$) He et al.
  (2022) find SST with the quadratic constitutive relation predicting the
  wall pressure well at all six Mach numbers, especially the shock
  position and post-shock plateau for $M_\infty\ge0.85$, where SA-QCR
  delays the shock and the shock-induced separation; both underpredict
  the Reynolds shear stress downstream of the shock at $M_\infty=0.875$,
  SST-QCR slightly less, and the authors use SST-QCR fields as surrogate
  high-fidelity data to tune their learned correction of SA-QCR
  ([He et al. (2022)](/sources/he-2022-b.md), §2.5, Figs. 5–6, §4; see
  [shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).
- **Transonic compressor buffet.** On the TCTA transonic cascade (inlet
  $M=1.21$, $Re=1.35\times10^6$), URANS with SST, Kato–Launder production and
  $\gamma$-$Re_\theta$ captures the shock-buffet Strouhal number of the
  implicit LES ($ft_c=0.161$ against 0.163–0.165; experiment about 0.14) but
  places the mean shock upstream ($x_s/c=0.504$ against 0.528–0.537),
  with less than half the oscillation amplitude of the LES (0.072 against
  0.158–0.278), a mainly laminar suction side and wrong surface
  distributions; it needed $\Delta t/t_c=2.8\times10^{-5}$ ($t_c$ the convective
  time, page-local), "because the shock oscillation magnitude and frequency
  are otherwise not correctly predicted", and cost 74.6 core-hours per
  convective time against 15 583 to 152 850 for the LES (Klose et al. 2025,
  §6, Tables 1–2, Fig. 7; see
  [compressor cascades](/benchmarks/compressor-cascade.md) and
  [shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).
- **Dynamic stall.** SST with an intermittency transport equation, as
  two-dimensional URANS and as the RANS part of a stress-blended eddy
  simulation, agrees with a wall-resolved LES of a pitching NACA 0012
  within 0.1 in $C_L$ in attached flow and gives the same $22^\circ$ peak-lift
  angle ([Baldan & Guardone (2025)](/sources/baldan-2025.md), §2.2,
  Fig. 9; arXiv v2; see [hybrid RANS/LES](/definitions/hybrid-rans-les.md)).
- **High-order flat plate.** On the NASA zero-pressure-gradient plate at
  $Re=10^7$, HDG with SST and an inlet eddy-viscosity ratio of 100
  overestimates the skin friction by 1.6% against an SST finite-volume
  reference (ISIS-CFD) (Elzaabalawy et al. 2023, §5.3, Figs. 21–23; see
  [turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md)).
- **Tandem cylinders.** SST-IDDES gives a primary shedding frequency of
  172 Hz against 179–180 Hz measured and slightly overpredicts the $C_p$
  RMS peaks of the downstream cylinder, where an IDDES on the SSG/LRR-$\omega$
  [Reynolds-stress model](/methods/reynolds-stress-model.md) gives 176 Hz and
  better peaks; on a transonic hammerhead launch vehicle SST-IDDES places
  the $C_p$ RMS peak at $x=0.62$ against 0.58 estimated from experiment
  (Wang et al. 2021, §3.2–§3.3, Table 1, Figs. 5, 11).
- **Turbine tip-leakage vortex.** In a transonic turbine cascade with a tip
  gap, SST URANS over-predicts the Reynolds shear stress along the
  tip-leakage vortex and misses the trailing-edge mixing that SST-DES
  resolves; both agree with the measured midspan isentropic Mach number
  except near the suction-side shock (Yang & Ma 2022, §3.1–§3.2, Figs. 6, 8;
  see [turbine cascades](/benchmarks/turbine-cascade.md)).
- **Canonical flows against $k$-$\tau$.** Tomboulides et al. (2025) use
  OpenFOAM's SST (version 12, simpleFoam, wall $\omega$ from
  $6\nu/(\beta d^2)$ at $y^+\sim1$) as the finite-volume comparison of
  their spectral-element [$k$-$\tau$ model](/methods/k-tau-model.md): in a
  channel at $Re_\tau\approx5200$ it gives $u_\tau=0.0409$ against 0.0415
  from DNS, the Nek5000 models being closer (§3.1, Table 1); on the
  Driver–Seegmiller [backward-facing step](/benchmarks/backward-facing-step.md)
  it reattaches at $6.44$ step heights on the fine grid against $6.26$
  measured, underpredicts the skin friction, "a known behavior of the SST
  model"; the authors cite Menter (1994), who reported $6.5$ for SST and $6.4$
  for $k$-$\omega$ (§3.3). In the NACA 0012 tables they reproduce, SST in
  CFL3D and FUN3D gives $C_D=0.00809$ and 0.00816 at $0^\circ$, and
  $C_D=0.01236$, $C_L=1.0778$ and 0.01253, 1.0840 at $10^\circ$, against
  0.0081, 0.012 and 1.075 measured (§3.4, Tables 3–4). Kumar et al. (2025,
  Table 3) print 1.05 for the measured lift at $10^\circ$, both papers citing
  Ladson (the [NACA 0012](/benchmarks/naca-0012-airfoil.md) page holds the
  record).
- **A regularized SST in a spectral-element code.** Kumar et al. (2025)
  compare the $k$-$\tau$ SST with the regularized $k$-$\omega$ SST of
  Tomboulides et al. (2018), which splits $\omega=\omega_w+\omega'$ with the
  wall-asymptotic part $\omega_w$ proportional to $\nu/d^2$ and solves for
  $\omega'$ with a zero wall value (App. A.5.1, Eqs. A23–A31; see the
  [Wilcox $k$-$\omega$ page](/methods/k-omega-model.md)), on the NASA
  zero-pressure-gradient flat plate at $Re_L=5\times10^6$: under wall-normal
  refinement ($N=6$, average first-node $y^+$ 0.09 to 2.9) both give
  oscillatory drag for $y^+>1.5$, the regularized SST then converging like
  SA in CFL3D and the $k$-$\tau$ SST oscillating, all within 1% of the
  CFL3D and FUN3D predictions; the converged $k$-$\tau$ SST profiles agree
  with the CFL3D SST data (§3.1.2–§3.1.3, Figs. 2–4).
- **Transitional dynamic stall.** As the base of the Langtry–Menter
  transition model inside delayed DES, SST-2003 gives the earliest
  suction collapse and stall of four RANS closures on a NACA 0012 pitching
  up at $Re=2\times10^5$, against a wall-resolved LES
  ([Batther & Lee (2022)](/sources/batther-2022.md), §3.1, §4.3.1, Fig. 17;
  see [dynamic stall](/definitions/dynamic-stall.md) and the
  [transition-model page](/methods/local-correlation-based-transition-model.md)).
- **High-order flux reconstruction.** With the log-$\omega$ SST above,
  Vandenhoeck et al. (2022) compute Wieghardt's flat plate
  ($Re_L=1.03\times10^7$) up to $\mathbb P^6$: profiles of all high orders
  coincide with the measurements, Spalding's law and a DG $\mathbb P^2$
  Wilcox reference, the $\mathbb P^4$ skin friction lies closer to the
  experiment than lower orders, and with first-element $y_1^+\simeq25$ the
  $\mathbb P^5$ and $\mathbb P^6$ solutions match the finer-mesh $\mathbb P^4$
  one without wall functions (§4.1, Figs. 9–10; see
  [turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md)).
- **Hypersonic fluid–thermal–structure interaction.** Thawait et al.
  (2023) run the Fluent SST-DDES above, with AUSM+ fluxes, dual time
  stepping and a density-based implicit solver, strongly coupled to a
  thermoelastic finite-element model of a deployable control fin with joint
  freeplay at Mach 3–6 (15 km altitude; Reynolds numbers printed as
  12.2–24.3 $\times10^6$ in Table I, without a reference length), on a
  2.7-million-cell tetrahedral grid (the validations on hexahedral grids of
  one million cells with first-layer $y^+<1$; §II, §V, §VI A). The validations test the structural
  response (a Mach 3 flutter velocity within 5%, time-averaged deflections of
  a heated panel at Mach 4 within 3.18% and 0.12%), not the turbulence model,
  and the paper compares DDES with no RANS run (§V–§VI); the turbulent
  kinetic energy it reports is the modelled $k$ (§VI B, Fig. 10). See
  [detached-eddy simulation](/methods/detached-eddy-simulation.md).
- **Aircraft wake precursor.** Bouhafid et al. (2024) use an SST RANS on an
  adapted mesh as the precursor of a temporal LES of a NACA 0012 wing with a
  jet ([Bouhafid et al. (2024)](/sources/bouhafid-2024.md), §2.2, §3; see
  [hybrid RANS/LES](/definitions/hybrid-rans-les.md)).
- **Hypersonic panel flutter under a swept interaction.** Ye et al. (2024)
  use SST URANS (Menter 1994, no correction or constant printed; AUSM+
  fluxes, third-order MUSCL, dual time stepping) loosely coupled to a
  finite-element plate, for a flexible panel under the Mach 5 sharp-fin
  swept shock/boundary-layer interaction of Schülein & Zheltovodov
  ($12^\circ$ fin); the flow solution is validated by wall pressure at two
  stations, and turbulence modelling is not studied
  ([Ye et al. (2024)](/sources/ye-2024.md), §II A, Eqs. 6–7, §III A, Fig. 3; see
  [shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).
- **Bayesian recalibration for shock interactions and cavities, as
  reviewed.** Le et al. (2024) report, from the works they review, that
  Bayesian calibration of SST coefficients on compression-corner
  interactions enhances near-wall turbulence through a larger eddy
  viscosity and improves adverse-pressure-gradient predictions, but that
  SST "cannot simulate the inherent shock instability" by changing
  parameters and its wall pressure in the separation region "remains too
  high" (Tang et al., as cited); that a polynomial-chaos, Bayesian and
  particle-swarm recalibration for supersonic cavities lowers the maximum
  wall-pressure error from 29.71% to 9.00% and the mean from 9.86% to 3.67%
  (Yang et al., as cited); that coefficients calibrated on a 24° corner
  transfer to 20°, 16° and 8° corners only "within a narrow range of Mach
  numbers"; and that ensemble inversion of the Reynolds-stress discrepancy
  of SST for such interactions overcomes "some limitations of the eddy
  viscosity assumption" ([Le et al. (2024)](/sources/le-2024.md), §3.1.1,
  Figs. 8–9, §3.1.2, Fig. 12; review, citing only; see
  [Bayesian closure calibration](/methods/bayesian-closure-calibration.md)).
  Fang et al. (2026) cite a physically constrained symbolic-regression
  enhancement of SST (Wu & Zhang, as cited) as an interpretable closure
  that generalizes across configurations
  ([Fang et al. (2026)](/sources/fang-2026.md), §5.2; see
  [symbolic-regression closures](/methods/symbolic-regression-closure.md)).
- **Vortex flows, as surveyed.** Luckring & Rizzi (2024) cite steady SST
  RANS of a wing with vortex generators (Förster & White, ANSYS CFX,
  $M=0.2$, $Re_{\mathrm{mac}}=10^6$) with excellent lift and drag correlation
  at low angle of attack, reasonable at moderate and almost none at deep
  stall (§3.2.1), and, on the SACCON configuration under forced pitch
  oscillation, neither SST nor Spalart–Allmaras correlating well with the
  measurements, SA being closer (§3.2.3.2)
  ([Luckring & Rizzi (2024)](/sources/luckring-2024.md); see
  [delta-wing vortex flow](/benchmarks/delta-wing-vortex-flow.md)).

## Qualifications

- Yu et al. (2023b) do not say whether the variable $\beta^*$ replaces the
  constant also in $F_1$ and $F_2$, nor which $C_{\mu,1}$ the RANS runs use;
  they note that RANS constants can differ from DNS-fitted ones (§V). Their
  a priori finding (the standard coefficient overestimates the eddy
  viscosity downstream) and their a posteriori one (the original SST
  underpredicts $k$ and shear stress) are opposite trends, which they explain
  by the equilibrium the two transport equations reach, not by $C_\mu$ alone
  (§IV–§V). Eq. 28 prints the cross-diffusion coefficient as $\sigma_{w2}$ and
  the product as $\partial_jk\,\partial_i\omega$ with mismatched indices,
  while Eq. 31 prints $\partial_ik\,\partial_i\omega$; the text calls the
  blending function "$F_l$".
- Wei et al. (2023) print no SST coefficients.
- Guo & Wang (2025) print the same quantity of the blending functions as
  $\sqrt k/(0.09\,\omega y)$ in $F_1$ (Eq. 3) and as $2\sqrt k/(0.99\,\omega y)$
  in $F_2$ (Eq. 5), and print the cross-diffusion with the indices
  $\partial_ik\,\partial_j\omega$ (Eq. 3); $\beta^*$, $\sigma_k$ and $\kappa$ have
  no printed values there.

Dzanic et al. (2022) print several slips in the SST equations of the
version read (arXiv v1):

- Eq. 12 writes the limiter with $\alpha_1$ (0.5532), while Appendix A also
  lists $a_1=0.31$, which appears in no printed equation. The form above
  writes $a_1$ in the limiter, the only listed constant that no printed
  equation uses *(compiler check, not in the sources)*.
- The diffusion coefficients of Eqs. 10–11 print $\mu_t$, never defined,
  while the eddy viscosity is called $\mu_u$ elsewhere.
- The production is printed as $P_k=\tau_{ij}\partial_ju_i$ with $\tau_{ij}$ the
  molecular viscous stress of their Eq. 4, not the modelled stress.
- In Eq. 11 the destruction bracket $\rho(P'-P'/f_\omega+\beta\omega_u/f_\omega)$
  has the dimensions of $\rho\omega$, not $\rho\omega^2$ like the left side
  *(compiler check, not in the sources)*; the printed form and the
  corrected RANS destruction $\beta\omega^2$ are both given under
  Equations.

- Mozaffari et al. (2022) call RANS predictions of unsteady flow at high
  incidence incorrect, "since according to the RANS velocity decomposition,
  with the right Reynolds stresses, the mean flow should be steady" (§5.2).
  Carreño Ruiz & D'Ambrosio (2022) need unsteady RANS at low incidence, where
  the boundary layer stays laminar and trailing-edge vortex shedding raises
  the mean lift by 22.8% (SD7003, $Re=23{,}000$, $\alpha=2^\circ$; §5,
  Table 11).
- Zhao et al. (2023b) print the diffusion coefficient of Eq. 2-2 as
  $\mu_L+\sigma_k\mu_T$ and that of the compressibility-corrected Eq. 2-5 as
  $\mu+\sigma_k\mu_t$, while §2 defines $\mu=\mu_L+\mu_T$; read literally, Eq.
  2-5 counts the eddy viscosity twice. Eq. 2-5 also contains an undefined
  $\upsilon_t$. Their wall condition $\omega_w=10\cdot6\nu/(\beta y^2)$ does not
  contain the constant $C_w=\sqrt{(50^2/10)(\beta/6)}$ that the text says is
  "reset to 0.01", so how $C_w$ enters is not printed (§3.2).
- Carreño Ruiz & D'Ambrosio print the turbulent viscosity ratio as
  $k/(\omega\mu)$ (Eq. 24), which is not dimensionless; $\rho k/(\omega\mu)$
  is *(compiler check, not in the sources)*. Their Eq. 1 prints the
  diffusion term with an unbalanced parenthesis,
  $\nabla\cdot[(\mu+\sigma_k\mu_t)\nabla k)]$; the form above drops the stray
  ")".
- Mozaffari et al. (2024) print the production in both transport equations
  as $\tau_{ij}\partial u_j/\partial x_j$, with the index $j$ repeated, which
  leaves a free index $i$ in a scalar equation; a scalar production needs
  the contraction with $\partial u_i/\partial x_j$ (Eqs. 16–17) *(compiler
  check, not in the sources)*. They also attribute SST to
  "Menter et al. [41]", a single-author 2009 review, after citing Menter
  (1994) for it (line 196).
- Petrocchi & Barakos (2024) expand SST as "Shear Stress Tensor" in the
  nomenclature and "Shear Stress Model" in a table caption, against
  "Shear-Stress Transport" in the text (nomenclature, Table A.4, §1).

- Elzaabalawy et al. (2023, §3.2) print $\beta_1=0.75$; with their printed
  $\alpha_1=5/9$ and $\sigma_{\omega1}=0.5$, the log-layer relation
  $\alpha=\beta/\beta^*-\sigma_\omega\kappa^2/\sqrt{\beta^*}$ that they state
  for TNT needs $\beta_1=0.075$ (giving 0.553, against 8.05 for 0.75), the
  value of every other source above *(compiler check, not in the sources)*.
  They also print $a_1=0.43$, where Dzanic et al., Zhao et al. (2023b),
  Oulghelou et al., Möller et al., Mozaffari et al. (2024) and Petrocchi &
  Barakos print 0.31; the
  paper gives no reason for the value.
- Zangeneh (2021) prints the convective term of the $k$ equation as
  $\nabla\cdot(\rho\boldsymbol u\omega)$, the term of the $\omega$ equation
  (Eq. 6), prints the cross diffusion with a factor 2 on both sides of a
  line break (Eq. 5), and expands SST as "shear stress tensor" while citing
  Gritskevich et al.'s "$k$-$\omega$ shear stress transport model"
  (§II.B), like the Petrocchi & Barakos nomenclature above.
- Monfaredi et al. (2021) attribute part of the differences between their
  Spalart–Allmaras URANS of a rod–airfoil configuration and two published
  2D URANS of the same case to the closure ("may be due"), those URANS
  using SST; they do not run SST themselves
  ([Monfaredi et al. (2021)](/sources/monfaredi-2021.md), §4.2, Fig. 7; see
  the [SA page](/methods/spalart-allmaras-model.md)).

- Cherroud et al. (2022) print the SST $\omega$-destruction with $\beta^*$,
  the coefficient of the $k$-equation sink, and the diffusion coefficient
  as $\sigma_w$ (Eq. 10); the page records it as printed. The sign of
  their limited production (Eq. 11) is discussed on the
  [explicit algebraic Reynolds-stress model](/methods/explicit-algebraic-reynolds-stress-model.md)
  page.
- Wu et al. (2023, Eq. 2) print the BSL cross-diffusion as
  $2\rho(1-F_1)\sigma_{\omega2}\omega^{-1}\partial_jk\,\partial_j\omega\;\beta\rho\omega^2$,
  with a trailing factor $\beta\rho\omega^2$ that repeats the destruction
  term of the bracket. Without the trailing factor the term has the
  dimensions of $D\rho\omega/Dt$, like the other terms of their equation;
  with it, it does not *(compiler check, not in the sources)*.
  Their text calls "$\beta$ and $n$" the constants of the resolution
  function, which Eq. 5 and Table 1 write $\beta^*$ (0.002), distinct from
  the $\beta_1^*=0.09$ of the $k$-equation. Their Eq. 2 also places the
  destruction inside the bracket multiplied by $\omega$,
  $\omega(\ldots-\beta\rho\omega^2)$, which gives a destruction
  $\beta\rho\omega^3$, one power of $\omega$ more than the dimensions of the
  left side $D\rho\omega/Dt$, while the production
  $\omega\gamma\mathcal T_{ij}\partial_ju_i/k$ has them, $\mathcal T_{ij}\partial_ju_i$
  having the dimensions of $D\rho k/Dt$ by their Eq. 1 *(compiler check,
  not in the sources)*.

## Contradictions

- **Exponent of the Langtry–Menter $F_3$.** *Open.* Menter et al. (2022)
  print the Langtry–Menter (2009) modification of the SST blending retained
  in Ansys Fluent as $F_3=\exp[-(R_y/120)^2]$ (§2.1, Eq. 7); Vandenhoeck et
  al. (2022) print the same named modification of SST-2003-LM2009 as
  $F_3=\exp[-(R_y/120)^8]$ (§1.2, Eq. 38). Both define
  $R_y=\rho d\sqrt k/\mu$. The functions agree near the wall and differ in
  how sharply they switch off around $R_y=120$ *(compiler check, not in
  the sources)*. Langtry & Menter's 2009
  paper is not ingested, and neither source calls its form an
  implementation variant.

# Citations

- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §2.1 Eqs. 10–17, §3 Eq. 26, App. A.
- [Menter et al. (2022)](/sources/menter-2022.md) — §1, §2.1 Eqs. 5–7.
- [Haering et al. (2022)](/sources/haering-2022.md) — §IV B.
- [Goc et al. (2021)](/sources/goc-2021.md) — §1, Fig. 1.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §IV.A.
- [Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md) — §2 Eqs. 1–3, 24, §3.4 Table 4, §3.5, §5 Table 11, §7.
- [François et al. (2022)](/sources/francois-2022.md) — §5.3–5.4, Figs. 12–15.
- [Mozaffari et al. (2022)](/sources/mozaffari-2022.md) — §2, §5.2, Figs. 26–27.
- [Yan et al. (2022)](/sources/yan-2022.md) — §1, §3.2, Fig. 11.
- [Knopp (2022)](/sources/knopp-2022.md) — §1.
- [Huang et al. (2022)](/sources/huang-2022.md) — §1.
- [Alauzet et al. (2022)](/sources/alauzet-2022.md) — §9.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §3, §4.2, §4.3.
- [Cai et al. (2022)](/sources/cai-2022.md) — §I, Table III (HAL v1).
- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §1, §2 Eqs. 2-2–2-5, §3.2, §5.1–5.4 Table 5-1 Figs. 5-2, 5-14, 5-15.
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — §4.1.2–4.1.3 Eqs. 6–11, §4.4, §5, §6–§7 Table 3 Figs. 17–23 (HAL author manuscript).
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §2, §3.3, §4.1 Figs. 7–9, §4.2 Figs. 10–15.
- [Lewis et al. (2023)](/sources/lewis-2023.md) — §4.1, §4.2.2, §4.3.1, Tables 9–10 (HAL accepted manuscript).
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §1, §2.3 Eqs. 16–25, §3.1 Table 1 Figs. 4–5, §3.2 Table 2 (HAL accepted manuscript).
- [Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md) — §2 Eqs. 3–5, §4.3, §4.5.5, Table 2, App. A Table A.4.
- [Liu et al. (2024)](/sources/liu-2024.md) — Eq. 9, Figs. 6, 8–13, Conclusions.
- [Pacciani et al. (2025)](/sources/pacciani-2025.md) — §4.2 Eqs. 15–18, §5.1.1 Fig. 5, §6.1, App. A Eq. A14.
- [Bouhafid et al. (2024)](/sources/bouhafid-2024.md) — §2.2, §3.
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — §1, §2 Eqs. 3–6, App. B, Tables 6, 9, 11 (arXiv v2).
- [Möller et al. (2024)](/sources/moller-2024.md) — §II.B.1 Eqs. 14–16, §II.B.3 (accepted manuscript).
- [Klose et al. (2025)](/sources/klose-2025.md) — §2, §6, Tables 1–2, Fig. 7 (ASME accepted manuscript).
- [Wu et al. (2025)](/sources/wu-2025.md) — §2.1 Eqs. 2–6, §3.2, §4.1–4.5, Tables 5–7 (authors' manuscript).
- [Baldan & Guardone (2025)](/sources/baldan-2025.md) — §2.2, Fig. 9 (arXiv v2).
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §3.1.1 Eq. 55, §3.2–3.2.1 Eq. 71, §5.3 Figs. 21–23, §7.
- [Wang et al. (2021)](/sources/wang-2021-l.md) — §2.3 Eqs. 17–18, §3.2–§3.3 Table 1, Figs. 5, 11.
- [Yang & Ma (2022)](/sources/yang-2022-b.md) — §2.1 Eqs. 1–5, §3.1–§3.2 Figs. 6, 8.
- [D'Ayer et al. (2026)](/sources/dayer-2026.md) — §1, refs. [6]–[8] (HAL submitted manuscript).
- [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) — §1.1 Eqs. 1–20 Table 1, §1.2 Eq. 38, §3.3.1 Eq. 88, §4.1 Figs. 9–10.
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) — §3.1 Table 1, §3.3, §3.4 Tables 3–4, §4.
- [Kumar et al. (2025)](/sources/kumar-2025.md) — §2.1–§2.2, Eqs. (11)–(28) ($k$-$\tau$ SST and its DDES); §3.1.2–§3.1.3, Figs. 2–4 (flat plate against the regularized $k$-$\omega$ SST); App. A.5–A.6, Eqs. (A13)–(A40).
- [Batther & Lee (2022)](/sources/batther-2022.md) — §3.1, §4.3.1, Fig. 17.
- [Zangeneh (2021)](/sources/zangeneh-2021.md) — §II.A–B Eqs. 1, 5–7, §II.F–G, §III.
- [Monfaredi et al. (2021)](/sources/monfaredi-2021.md) — §4.2, Fig. 7.
- [Cherroud et al. (2022)](/sources/cherroud-2022.md) — §2.1 Eqs. 9–13, §4.2 Figs. 5–7.
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §2.3 Fig. 5, §3.4 Eq. 8, §4.1, §4.4.2 Fig. 11.
- [He et al. (2022)](/sources/he-2022-b.md) — §2.5 Figs. 5–6, §4.
- [Wu et al. (2023)](/sources/wu-2023-b.md) — §2.1.1 Eqs. 1–4 Table 1, §3.4 Table 2.
- [Li et al. (2022)](/sources/li-2022-k.md) — §III C, Figs. 15–18.
- [Mani & Dorgan (2023)](/sources/mani-2023.md) — §4.5.1–4.5.2, Figs. 6, 12.
- [Thawait et al. (2023)](/sources/thawait-2023.md) — §II B Eqs. 6–14, §V, §VI A–B Table I Fig. 10.
- [Yu et al. (2023b)](/sources/yu-2023-b.md) — §IV, Eq. (21) (wall-pressure-dependent coefficient); §V, Eqs. (27)–(33), Figs. 21–24 (printed SST, refined $\beta^*$ and $Pr_t$, Schülein and Holden cases).
- [Wei et al. (2023)](/sources/wei-2023.md) — §IV F, Figs. 36–37 (SST RAS against LES of a combusting hydrogen film).
- [Wu et al. (2024)](/sources/wu-2024.md) — §2.1, Eqs. (1)–(3) (BSL host of SATES-σ); §3.2–§3.3, Table 3 (SST-IDDES comparator).
- [Wu et al. (2024b)](/sources/wu-2024-b.md) — §III.A, Eqs. (24)–(27) (BSL host of SATES).
- [Wu et al. (2026)](/sources/wu-2026-b.md) — §2.1, Eqs. (1)–(3) (SST eddy viscosity with $F_{\mathrm{cor}}$ and $F_2$ as host of SATES); §2.2, Eqs. (15)–(16) ($F_2$-type blending of SATES-II); §2.3, Eq. (19) (SST-IDDES $C_{\mathrm{DES}}$).
- [Guo & Wang (2025)](/sources/guo-2025.md) — §2.1, Eqs. (1)–(15) (SST-DES, SST-DDES, filtered eddy viscosity, adaptive grid scale); Eq. (20) ($\omega$ wall function).
- [Ye et al. (2024)](/sources/ye-2024.md) — §II A, Eqs. (6)–(7); §III (SST URANS of a Mach 5 swept interaction with a flexible panel).
- [Le et al. (2024)](/sources/le-2024.md) — §3.1.1, Figs. 8–9; §3.1.2, Fig. 12 (Bayesian SST calibration and discrepancy inversion, as reviewed).
- [Fang et al. (2026)](/sources/fang-2026.md) — §5.2 (symbolic-regression SST enhancement, as cited).
- [Luckring & Rizzi (2024)](/sources/luckring-2024.md) — §3.2.1 (vortex-generator RANS with SST, as cited); §3.2.3.2 (SACCON forced oscillation, as cited).
