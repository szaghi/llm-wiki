---
type: Method
title: "k-ω SST model"
description: "Menter's two-equation shear-stress-transport eddy-viscosity model, blending a k-ω inner formulation with an outer one through F1 and limiting the eddy viscosity through F2; its equations and constants as printed in the sources, its transition and PANS forms, and its unsuitability where k must be the true kinetic energy."
status: established
aliases: [SST, k-omega SST, shear stress transport model, Menter SST, SST k-ω]
tags: [rans, eddy-viscosity, transition, pans, hybrid-rans-les]
timestamp: 2026-10-25T13:40:00Z
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

# Citations

- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §2.1 Eqs. 10–17, §3 Eq. 26, App. A.
- [Menter et al. (2022)](/sources/menter-2022.md) — §1, §2.1 Eqs. 5–7.
- [Haering et al. (2022)](/sources/haering-2022.md) — §IV B.
- [Goc et al. (2021)](/sources/goc-2021.md) — §1, Fig. 1.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §IV.A.
