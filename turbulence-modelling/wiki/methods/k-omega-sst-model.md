---
type: Method
title: "k-ω SST model"
description: "Menter's two-equation shear-stress-transport eddy-viscosity model, blending a k-ω inner formulation with an outer one through F1 and limiting the eddy viscosity through F2; its equations, constants and printed variants, its transition, PANS, DES and compressibility-corrected forms, high-order discretization, data-driven corrections, and evidence on airfoils, cascades, cars, separated flows and its transported k."
status: established
aliases: [SST, k-omega SST, shear stress transport model, Menter SST, SST k-ω, SST-IDDES, SST-DDES]
tags: [rans, eddy-viscosity, transition, pans, hybrid-rans-les]
timestamp: 2026-10-26T20:48:00Z
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

### Compressibility correction

Zhao et al. (2023b) add the dilatational-dissipation and
pressure-dilatation correction of Suzen & Hoffmann, active only through the
factor $(1-F_1)$, i.e. in the outer branch. In their nondimensional form
the $k$-destruction becomes $\big[1+\alpha_1M_t^2(1-F_1)\big]\beta^*\rho k\omega$
plus a pressure-dilatation source $(1-F_1)\,p''d''$ (page-local, the source's
$\overline{p''d''}$; the double primes are not Favre fluctuations), with

$$p''d''=-\alpha_2\,\tau_{ij}\partial_ju_iM_t^2+\alpha_3\rho\beta^*k\omega M_t^2,\qquad \alpha_1=1.0,\ \alpha_2=0.4,\ \alpha_3=0.2,$$

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
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md)). The
high-order accuracy therefore applies to the mean-flow variables only
*(compiler check, not in the sources)*. They
recall the opposite choice of Bassi et al., who solve for $\log\omega$ at high
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

- **Separation fix.** Yan et al. (2022) recall Rumsey's fix of SST, a
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
  $L_t$).
- **Roughness.** D'Ayer et al. (2026) cite roughness corrections of SST
  (Aupoix, their ref. [7]) among the roughness models whose development
  their rough-wall DNS databases are meant to support
  ([D'Ayer et al. (2026)](/sources/dayer-2026.md), §1, refs. [6]–[8]; HAL
  submitted manuscript).

- **Transitional DDES.** Möller et al. (2024) couple SST-DDES to the
  one-equation $\gamma$ model by multiplying the production of $k$ by
  $\gamma$ and the DDES destruction by $\max(0.1,\gamma)$
  (§II.B.3; see [detached-eddy simulation](/methods/detached-eddy-simulation.md)).

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
  [JAXA Standard Model](/benchmarks/jaxa-standard-model.md)).
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
- **Hypersonic heat flux.** Huang et al. (2022) recall that SA and SST predict
  hypersonic zero-pressure-gradient heat flux less accurately than algebraic
  models with compressibility corrections (Rumsey 2010; Gnoffo et al. 2013)
  ([Huang et al. (2022)](/sources/huang-2022.md), §1).
- Alauzet et al. (2022) name a comparison of SA and SST on mesh-converged
  adapted meshes as future work ([Alauzet et al. (2022)](/sources/alauzet-2022.md), §9).
- **Ahmed body.** As recalled by Cai et al. (2022), Menter & Kuntz ran
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
- **Aircraft wake precursor.** Bouhafid et al. (2024) use an SST RANS on an
  adapted mesh as the precursor of a temporal LES of a NACA 0012 wing with a
  jet ([Bouhafid et al. (2024)](/sources/bouhafid-2024.md), §2.2, §3; see
  [hybrid RANS/LES](/definitions/hybrid-rans-les.md)).

## Qualifications

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
  Table 11). The two statements concern different regimes (turbulent vortex
  flow, laminar periodic shedding) and are not incompatible.
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
