---
type: Method
title: "The k-τ model"
description: "Two-equation RANS eddy-viscosity model transporting the turbulent kinetic energy and the turbulence time scale 1/ω, whose wall value is zero and whose sources stay bounded; the spectral-element implementation of Tomboulides et al. with its source limiters, low-Reynolds variant, implicit source treatment and validation."
status: established
aliases: [k-tau, k-τ RANS model, k–τ, Speziale k-τ, Kalitzin k-τ, Kok–Spekreijse k-τ]
tags: [rans, eddy-viscosity, spectral-element, boundary-layer]
timestamp: 2026-10-27T15:55:00Z
---

# The k-τ model

The $k$-$\tau$ model is a two-equation RANS closure of the
$k$-$\omega$ family that transports, instead of the specific dissipation
rate $\omega$, its inverse, the turbulence time scale. On this page the
time scale is written $\tau_t=1/\omega$ (registry §11; the sources' $\tau$,
not to be confused with the registry's stresses $\tau_{ij}$ or the wall
shear $\tau_w$). With the [Boussinesq](/definitions/boussinesq-hypothesis.md)
closure the eddy viscosity is

$$\mu_t=\rho k\tau_t,$$

the $k$-$\omega$ value $\rho k/\omega$ written in the new variable. Its
selling point is the wall: $\omega$ grows like $d^{-2}$ as the wall
distance $d\to0$, whereas $\tau_t$ vanishes there and the source terms of
its equation stay bounded, so the model needs neither an arbitrarily large
wall value nor the regularization of the
[Wilcox $k$-$\omega$ model](/methods/k-omega-model.md). The page rests on
one source, Tomboulides et al. (2025), whose named contribution is a robust
implementation in the spectral-element codes [Nek5000](/software/nek5000.md)
and NekRS ([Tomboulides et al. (2025)](/sources/tomboulides-2025.md), §1–§2).

## Lineage

Tomboulides et al. trace the model to Speziale et al. (1992), Kalitzin et
al. (1996) and Kok & Spekreijse (2000), and take the base equations from
Kalitzin et al. with the Wilcox (2006) constants (§1–§2). They state,
citing earlier work:

- the wall boundary condition is $\tau_t=0$ and all sources of the
  $\tau_t$ equation are bounded, so no regularization and no wall-distance
  computation is needed (citing Kok & Spekreijse; Lloyd et al.);
- Kok & Spekreijse showed that transporting $\sqrt{\tau_t}$, as Kalitzin
  et al. proposed, makes the source terms unbounded, whereas for $\tau_t$
  itself they stay bounded near the wall (§1);
- the cross-diffusion term and the rewriting of the gradient-squared term
  below are Kok & Spekreijse's (§2).

The authors motivate the model by the defects of its neighbours: the
[$k$-$\varepsilon$ model](/methods/k-epsilon-model.md) needs wall damping
functions and wall distance and has no natural wall condition for
$\varepsilon$; the $k$-$\omega$ model has the $d^{-2}$ singularity, which
in high-order codes with negligible numerical diffusion produces persistent
oscillations and grid-sensitive solutions; and their own regularized
$k$-$\omega$ model has wall-distance-dependent extra sources that cannot be
treated implicitly (§1).

## Equations

In the incompressible form of Tomboulides et al. (§2, Eqs. 12–24),
with the mean strain magnitude $\lvert S\rvert$ (the source's $S$, already
with the factor two) and the production $\rho P_k=\mu_t\lvert S\rvert^2$
(Eq. 7), the base model reads

$$\begin{aligned}
\partial_t(\rho k)+\nabla\cdot(\rho k\boldsymbol u)&=\nabla\cdot\Big[\Big(\mu+\frac{\mu_t}{\sigma_k}\Big)\nabla k\Big]+\rho P_k-\rho\beta^*\frac{k}{\tau_t},\\
\partial_t(\rho\tau_t)+\nabla\cdot(\rho\tau_t\boldsymbol u)&=\nabla\cdot(\Gamma_\omega\nabla\tau_t)-\gamma_\omega\frac{\tau_t}{k}\rho P_k+\rho\beta_\omega-\frac{2\Gamma_\omega}{\tau_t}\nabla\tau_t\cdot\nabla\tau_t+C_{D\tau},
\end{aligned}$$

with $\Gamma_\omega=\mu+\mu_t/\sigma_\omega$ (registry §11), the
cross-diffusion term

$$C_{D\tau}=\rho\sigma_d\tau_t\min(\nabla k\cdot\nabla\tau_t,0),$$

and Menter's production limiter $\rho P_k\leftarrow\min(\rho P_k,10\rho\beta^*k/\tau_t)$
(Eq. 17). $\beta_\omega$ and $\gamma_\omega$ are the registry's destruction
and production coefficients of the $\omega$ equation (the source's $\beta$
and $\alpha$). The $\tau_t$ equation follows from the $\omega$ equation of
the Wilcox model by $\omega=1/\tau_t$: multiplying the $\omega$ cross
diffusion $\rho(\sigma_d/\omega)\max(\nabla k\cdot\nabla\omega,0)$ by
$-\tau_t^2$ gives $C_{D\tau}$ *(compiler check, not in the sources)*, and
the authors note that the $\tau_t$ and $\omega$ transport equations are
equivalent (§3.1).

**Constants.** Wilcox (2006) values as printed: $\beta_\omega=0.0708$,
$\beta^*=0.09$, $\gamma_\omega=0.52$, $\sigma_k=1/0.6$,
$\sigma_\omega=2.0$, $\sigma_d=1/8$, in the divisor convention of the
diffusivities above; they agree with the Wilcox (2006) set on the
[$k$-$\omega$ page](/methods/k-omega-model.md).

**Near-wall behaviour.** In the viscous sublayer
$\tau_t\to\beta_\omega d^2/(6\nu)$ (Eq. 19, after Wilcox), the inverse of
the wall value $\omega_w=6\nu/(\beta_\omega d^2)$ that the authors impose in
their OpenFOAM comparison runs (§3.1) *(compiler check, not in the
sources)*. Following Kok & Spekreijse the
authors give the wall limits of the three non-transport terms of the
$\tau_t$ equation: $\rho\beta_\omega$, a diffusion
$\nabla\cdot(\mu\nabla\tau_t)\to\tfrac13\rho\beta_\omega$ and a
gradient-squared term $(2\mu/\tau_t)\lvert\nabla\tau_t\rvert^2\to\tfrac43\rho\beta_\omega$,
which balance (§2).

## The implementation of Tomboulides et al.

Four modifications make the model robust in a high-order code (§2–§2.2):

1. **Square-root rewrite.** The gradient-squared term is written
   $$\frac{2\Gamma_\omega}{\tau_t}\nabla\tau_t\cdot\nabla\tau_t=8\Gamma_\omega S_\tau,\qquad S_\tau=\nabla\tau_t^{1/2}\cdot\nabla\tau_t^{1/2}$$
   (Eq. 18; $S_\tau$ page-local), numerically preferable because
   $\tau_t^{1/2}$ is linear near the wall and no division by $\tau_t$
   occurs (after Kok & Spekreijse).
2. **Cap on the molecular part (new).** Gradient errors near sharp
   corners and during transients drove $\tau_t$ and $\mu_t$ to unphysically
   small values that persisted to steady state and were convected away
   from walls; the authors therefore cap the molecular part,
   $$8\Gamma_\omega S_\tau\leftarrow\min(S_{\lim},8\mu S_\tau)+8\frac{\mu_t}{\sigma_\omega}S_\tau$$
   (Eq. 21; $S_{\lim}$ page-local). The theoretical value is the wall limit
   $S_{\lim}=\tfrac43\rho\beta_\omega$ (Eq. 20); every reported run uses
   the relaxed $S_{\lim}=\tfrac83\rho\beta_\omega$ for robustness.
3. **Free-stream limiter.** After Kalitzin et al., all sources of both
   equations are multiplied by
   $$R_{\mathrm{fs}}=\begin{cases}\min\big(1,\mu_t/(r\mu)\big),& d>y_{\lim},\\ 1,& d\le y_{\lim},\end{cases}$$
   (Eq. 22; $R_{\mathrm{fs}}$, $r$, $y_{\lim}$ page-local), with $r=0.01$
   and $y_{\lim}=0.5D_h$, $D_h$ the hydraulic diameter. It suppresses the
   unphysically large free-stream $\tau_t$ that the constant source
   $\rho\beta_\omega$ would build; where $\mu_t>r\mu$ the sources are
   unchanged, and all sources vanish as $\mu_t\to0$. The authors say it may
   be ignored for internal flows, that solutions are insensitive to
   $y_{\lim}$, and that for external flows it is "imperative" (§2, §3.4).
   The final model is Eqs. 23–24, the base model with these three changes.
4. **Implicit sources.** Writing each equation as
   $\rho(\partial_t\phi+\boldsymbol u\cdot\nabla\phi)=\nabla\cdot(\epsilon_\phi\nabla\phi)+s_{nl}\phi+s_l$
   ($\phi=k,\tau_t$; $\epsilon_\phi$, $s_{nl}$, $s_l$ page-local), the
   non-linear coefficients $s_{nl}$ become a diagonal matrix that is moved
   into the Helmholtz operator of the BDF/extrapolation scheme of the
   [spectral element method](/methods/spectral-element-method.md),
   $\hat{\mathsf K}=\mathsf K-\mathsf M s_{nl}$ (Eqs. 32–38). This adds no
   cost to the Helmholtz solve and leaves the time step bounded only by
   the convective CFL condition, about 0.5 for second-order BDF (§2.2).
   Every term of $s_{nl}$ as printed (Eq. 34) is non-positive, so the
   modified stiffness matrix keeps the symmetric positive-definite
   character of $\mathsf K$ *(compiler check, not in the sources)*.

**Low-Reynolds variant.** Wilcox's (1992) low-Reynolds damping of the
$k$-$\omega$ model is transferred to $k$-$\tau$ to capture the near-wall
peak of $k$ (§2.1, Eqs. 25–31). With the turbulence Reynolds number
$Re_T=\rho k\tau_t/\mu$ and the page-local damping coefficients
$\alpha^*$, $\alpha^*_0$, $\alpha_0$:

$$\begin{aligned}
\mu_t&=\alpha^*\rho k\tau_t,\qquad \alpha^*=\frac{\alpha^*_0+Re_T/R_k}{1+Re_T/R_k},\\
\beta^*&=\beta^*_\infty\,\frac{4/15+(Re_T/R_\beta)^4}{1+(Re_T/R_\beta)^4},\qquad
\gamma_\omega=\frac{\gamma_{\omega,\infty}}{\alpha^*}\,\frac{\alpha_0+Re_T/R_\tau}{1+Re_T/R_\tau},
\end{aligned}$$

with $R_k=6$, $R_\beta=8$, $R_\tau=2.95$, $\beta^*_\infty=0.09$,
$\gamma_{\omega,\infty}=0.52$, $\alpha^*_0=\beta_\omega/3$
($R_k$, $R_\beta$, $R_\tau$ page-local constants).

## Evidence

All results are from Tomboulides et al. (2025, §3), against the regularized
$k$-$\omega$ model in Nek5000 and the SST model of
[OpenFOAM](/software/openfoam.md) (version 12, simpleFoam); polynomial
degrees $N=2$–9 (the source's $p$).

- **[Channel](/benchmarks/turbulent-channel-flow.md), $Re_\tau\approx5200$**
  ($Re_b=125{,}000$ on the half-width), 7 elements across the half-channel,
  $N=3,5,7,9$ with first-node $y^+=1.7$, 0.73, 0.39, 0.25: velocity, $k^+$
  and $\tau_t^+$ profiles are insensitive to the near-wall resolution and
  indistinguishable under $p$-refinement except at $N=3$. Friction
  velocity (Table 1): $k$-$\tau$ 0.0412, low-Reynolds $k$-$\tau$ 0.0414,
  regularized $k$-$\omega$ 0.0413 and 0.0415, OpenFOAM SST 0.0409, DNS
  0.0415 (§3.1).
- **Pipe, $Re_\tau=1142$** ($Re_b=44{,}000$, $N=7$, mean $y^+\approx0.8$):
  $u_\tau=0.0523$ ($k$-$\tau$) and 0.0528 (low-Reynolds) against 0.0519
  from the DNS of Wu & Moin, errors below 1% and 2% (Table 2); the
  low-Reynolds variant captures the near-wall peak of $k$, slightly offset
  from DNS, and collapses on the base model towards the axis (§3.2,
  Fig. 6). The log layer follows the [law of the wall](/definitions/law-of-the-wall.md)
  with $\kappa=0.41$, $B=5.5$ (§3.2).
- **[Backward-facing step](/benchmarks/backward-facing-step.md)** of Driver
  & Seegmiller, $Re=37{,}425$ on the step height $H$, $N=7$, 2553
  elements: reattachment at $6.48H$ ($k$-$\tau$), $6.49H$ (regularized
  $k$-$\omega$), $6.44H$ (OpenFOAM SST, fine grid) against $6.26H$
  measured. All models underpredict the downstream velocity; the departure
  of $k$ from SST downstream "may be explained" by the absence of SST
  blending in $k$-$\tau$ (§3.3).
- **[NACA 0012](/benchmarks/naca-0012-airfoil.md)**, $Re=6\times10^6$,
  $M=0.15$, 5974 elements, $N=7$ ($N=5$ differs by less than 0.1%),
  inlet $k=\tau_t=0$: at $\alpha=0^\circ$, $C_D=0.00831$ against 0.0081
  measured and 0.00809–0.00854 from the NASA codes CFL3D and FUN3D with
  Spalart–Allmaras, SST and $k$-$\omega$ (Table 3); at $\alpha=10^\circ$,
  $C_D=0.01381$ and $C_L=1.0618$ against 0.012 and 1.075 measured, the
  NASA codes giving $C_D=0.01231$–0.01297 and $C_L=1.0778$–1.1012
  (Table 4). The $k$-$\tau$ model overpredicts drag and underpredicts lift
  at $10^\circ$; its lift error is smaller than that of the $k$-$\omega$
  model in either NASA code. With the limiter $R_{\mathrm{fs}}$ the
  coefficients are consistent even for zero free-stream $k$ (§3.4).
- **T-junction** (OECD/NEA 2010 benchmark, $Re=40{,}000$ at both inlets,
  41,304 elements, $N=5$–9): both RANS models overpredict the axial
  velocity at moderate wall distances and underpredict it in the core,
  against LES and experiment; $k$-$\tau$ ran stably at a CFL number of
  about 2, the regularized $k$-$\omega$ only at about 0.1 (§3.5, §4).

The authors report NekRS, the GPU counterpart of Nek5000, as carrying the
same implementation, without results (§1, §4), and list as future work
$k$-$\tau$ [wall functions](/methods/rans-wall-function.md) (reported in
earlier reports by Shaver et al., 2022 and 2023), steady solvers, and an SST
version of $k$-$\tau$ as the basis of a
[delayed detached-eddy simulation](/methods/detached-eddy-simulation.md)
(§4).

## Qualifications

- **Wall distance.** The authors state that the model eliminates the
  dependence on the wall distance, yet the free-stream limiter as printed
  switches on $d>y_{\lim}$ (Eq. 22) and $y_{\lim}$ is defined through a
  hydraulic diameter, which an external flow such as the airfoil lacks.
  The authors' mitigation is that $R_{\mathrm{fs}}$ may be dropped for
  internal flows and that solutions are insensitive to $y_{\lim}$ (§2).
- **Airfoil drag at $10^\circ$.** The text calls the drag a slight
  overprediction; the printed values give $+15\%$ against the measurement,
  while the largest NASA-code value, 0.01297, is $+8\%$
  *(compiler check, not in the sources)*.
- **The cap $S_{\lim}$** is an empirical relaxation (twice the theoretical
  wall limit) justified by the authors' experimentation; no figure shows
  the failure without it (§2).
- **Printed slips.** The pipe section is headed "$Re_\tau=1000$" while the
  text gives 1142; Eq. 29 writes $Re_\tau$ where Eq. 30 defines
  $R_\tau=2.95$, and $\alpha_0$ is given no value; §1 calls $\varepsilon$
  "specific dissipation"; the T-junction text cites a $p=9$ mesh where the
  captions of Figs. 18–22 say $p=7$.

# Citations

- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) — §1, §2 Eqs. 7, 12–24, §2.1 Eqs. 25–31, §2.2 Eqs. 32–38, §3.1–3.5 Tables 1–4, Figs. 6, 18–22, §4.
