---
type: Method
title: "k-ω SST model"
description: "Menter's two-equation shear-stress-transport eddy-viscosity model, blending a k-ω inner formulation with an outer one through F1 and limiting the eddy viscosity through F2; its equations and constants, its transition, PANS and DES forms and modifications, and evidence on airfoils, fan stages, vortex flows and its transported k."
status: established
aliases: [SST, k-omega SST, shear stress transport model, Menter SST, SST k-ω, SST-IDDES, SST-DDES]
tags: [rans, eddy-viscosity, transition, pans, hybrid-rans-les]
timestamp: 2026-10-25T20:27:00Z
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
rotation magnitudes are those of the mean velocity.

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
- Carreño Ruiz & D'Ambrosio print the turbulent viscosity ratio as
  $k/(\omega\mu)$ (Eq. 24), which is not dimensionless; $\rho k/(\omega\mu)$
  is *(compiler check, not in the sources)*. Their Eq. 1 prints the
  diffusion term with an unbalanced parenthesis,
  $\nabla\cdot[(\mu+\sigma_k\mu_t)\nabla k)]$; the form above drops the stray
  ")".

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
