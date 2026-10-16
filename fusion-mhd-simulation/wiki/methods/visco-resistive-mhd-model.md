---
type: Method
title: "Single-fluid visco-resistive MHD model"
description: "The full (non-reduced) single-fluid, single-temperature resistive MHD system with viscosity, anisotropic heat conduction and particle diffusion that the nonlinear tokamak codes solve; its variants differ in the evolved field (B or A), the viscous and heat-flux closures, the source current in Ohm's law and the normalization."
status: established
aliases: [full MHD, visco-resistive full MHD, single-fluid resistive MHD, viscoresistive MHD]
tags: [mhd, full-mhd, tokamak, code]
timestamp: 2026-10-16T00:00:00Z
---

# Single-fluid visco-resistive MHD model

The single-fluid visco-resistive MHD model evolves mass density $\rho$,
centre-of-mass velocity $\mathbf v$, pressure $p$ (or temperature $T$) and
the magnetic field $\mathbf B$ (directly, or through the vector potential
$\mathbf A$), with resistive Ohm's law and the dissipative closures needed
to run nonlinear simulations: viscosity, anisotropic heat conduction and
particle diffusion. It is the "full MHD" of this bundle, in contrast with
[reduced MHD](/methods/reduced-mhd.md), which restricts $\mathbf B$ and
$\mathbf v$ by an ansatz or an ordering. Two-fluid, diamagnetic and
neoclassical extensions (extended MHD) are written as added terms in the
same system.

## Reference form (SI)

Written in the registry notation ([notation](/notation.md)), the common
core of the sources below is

$$\begin{aligned}
\partial_t\rho+\nabla\cdot(\rho\mathbf v)&=\nabla\cdot\big(D_\perp\nabla_\perp\rho+D_\parallel\nabla_\parallel\rho\big)+S_\rho,\\
\rho\big(\partial_t\mathbf v+\mathbf v\cdot\nabla\mathbf v\big)&=\mathbf J\times\mathbf B-\nabla p+\nu\nabla^2\mathbf v+\mathbf S_{\mathbf v},\\
\partial_t p+\mathbf v\cdot\nabla p+\Gamma p\,\nabla\cdot\mathbf v&=(\Gamma-1)\Big[\eta\,\mathbf J\cdot(\mathbf J-\mathbf J_x)+\nabla\cdot\big(\kappa_\parallel\nabla_\parallel T+\kappa_\perp\nabla_\perp T\big)\Big]+S_p,\\
\partial_t\mathbf B&=-\nabla\times\mathbf E,\qquad \mathbf E=-\mathbf v\times\mathbf B+\eta\,(\mathbf J-\mathbf J_x),\\
\mu_0\mathbf J&=\nabla\times\mathbf B,\qquad \nabla\cdot\mathbf B=0,
\end{aligned}$$

with $p=\sum_s n_sT_s$, a single temperature $T$, $\Gamma=5/3$, $\nu$ a
dynamic viscosity in the Laplacian form (the simplest closure used; the
stress-tensor closures are listed below), and $\mathbf J_x$ the current
density imposed in Ohm's law (an equilibrium current, a source current or
the bootstrap current, see
[bootstrap current](/definitions/bootstrap-current.md)). The Ohmic heating
$\eta\,\mathbf J\cdot(\mathbf J-\mathbf J_x)$ follows from
$(\mathbf E+\mathbf v\times\mathbf B)\cdot\mathbf J$
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eq. 16;
[Saxena et al. (2025)](/sources/saxena-2025.md), App. C, Eq. C3). In
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eqs. 15–16, the momentum
source $\mathbf S_{\mathbf v}$ also removes the momentum carried by the
mass source and by particle diffusion, and the pressure source carries the
viscous heating.

**Vector-potential form.** Codes that evolve $\mathbf A$ write Faraday's
law as $\partial_t\mathbf A=\mathbf v\times\mathbf B-\eta(\mathbf J-\mathbf J_x)-\nabla\Phi$
([Artola et al. (2021)](/sources/artola-2021.md), Eq. 1), so that
$\nabla\cdot\mathbf B=0$ holds by construction
([divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).
JOREK's full-MHD model uses the Weyl gauge $\Phi=0$ and adds a toroidal
field that is frozen in time,
$\mathbf B=F\nabla\phi+\nabla\times\mathbf A$, with $F(\psi)$ taken from the
[Grad–Shafranov](/definitions/grad-shafranov-equation.md) equilibrium "for
numerical reasons"; $A_\phi$ therefore evolves even in a steady state
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.1, Eq. 5;
[Bhole et al. (2023)](/sources/bhole-2023.md), Eqs. 8–10).

## Variants in the sources

| Code (source) | Evolved field | Viscosity | Heat and particle transport | Ohm's law, $\mathbf J_x$ | Units |
|---|---|---|---|---|---|
| CLT and M3D-C1 benchmark model ([Zhang et al. (2021)](/sources/zhang-2021.md), Eqs. 1.1–1.6) | $\mathbf B$ (CLT), $\mathbf A$ (M3D-C1) | kinematic, $\rho\nabla\cdot(\nu\nabla\mathbf v)$ | diffusion of $\rho-\rho_{\rm eq}$; $\nabla\cdot[\kappa_\perp\nabla_\perp(p-p_{\rm eq})]+\nabla\cdot(\kappa_\parallel\nabla_\parallel p)$ with diffusivities acting on $p$; no Ohmic heating | $\mathbf J_x=\mathbf J_{\rm eq}$, so the equilibrium is not resistively diffused | Alfvén units, $L_0=1$ m, $B=1$ T, $n=10^{20}$ m$^{-3}$; $\eta$ in units of $\mu_0L_0^2/\tau_A$ |
| SCELT ([Ma & Guo (2022)](/sources/ma-2022.md), Eqs. 1–7) | $\mathbf B$, linearized | $\nu\nabla^2\mathbf v$ | none; Ohmic heating $(\Gamma-1)\eta J^2$ | $\mathbf J_x=0$ | $\mu_0=1$, lengths in $a$, time in $\tau_A$ |
| JOREK full MHD ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eqs. 1–24; [Bhole et al. (2023)](/sources/bhole-2023.md), Eqs. 1–10) | $\mathbf A$, Weyl gauge, frozen $F$ | stress tensor: parallel (Braginskii-type) part, perpendicular part with $\nu_\perp\propto T^{-3/2}$, neoclassical poloidal friction, gyroviscous cancellation; Bhole et al. use a scalar $\nu\propto T^{-3/2}$ in Laplacian form | anisotropic tensors $X_\parallel\mathbf b\otimes\mathbf b+X_\perp(\mathbf I-\mathbf b\otimes\mathbf b)$; $\kappa_\parallel\propto T^{5/2}$ (Spitzer–Härm), optional cap | $\eta\propto T^{-3/2}$; diamagnetic electron-pressure term; $\mathbf J_x$ a toroidal source current, optionally bootstrap-evolving | JOREK units, $\mu_0=1$, $(\Gamma-1)$ absorbed into $\kappa$ |
| M3D-C1 single fluid ([Saxena et al. (2025)](/sources/saxena-2025.md), App. C; [Artola et al. (2021)](/sources/artola-2021.md), §2) | $\mathbf A$ through scalar potentials | full ion stress tensor (perpendicular, gyroviscous, parallel); electron viscosity as hyper-resistivity | $\kappa_\parallel$, $\kappa_\perp$ on $T_e$ | $\eta\,\mathbf J\cdot(\mathbf J-\mathbf J_x)$ heating, $\mathbf J_x$ the bootstrap current; $\eta=\eta_{\rm norm}\eta_0T_e^{-3/2}$ | SI, $\mu_0$ explicit |
| NIMROD ([Artola et al. (2021)](/sources/artola-2021.md), §2; [Taheri et al. (2022)](/sources/taheri-2022.md), Eqs. 3, 5, 16–18) | $\mathbf B$ and $\mathbf v$ components | isotropic stress $-\rho\nu(\nabla\mathbf v+\nabla\mathbf v^{\mathsf T}-\tfrac23\mathbf I\nabla\cdot\mathbf v)$, $\nu$ kinematic | temperature equation instead of pressure equation; isotropic particle diffusivity | $\eta$ from the toroidally symmetric part of $T$ (Artola et al.) | SI |

The model of [Zhang et al. (2021)](/sources/zhang-2021.md), §2, is the
same in both codes "with the same definitions and normalizations of these
dissipation parameters"; it is the basis of the
[CLT–M3D-C1 benchmark](/benchmarks/clt-m3d-c1-benchmark.md). In M3D-C1 the
field is advanced through $\mathbf A$, of which Eq. 1.4 is the curl
([Zhang et al. (2021)](/sources/zhang-2021.md), §2). NIMROD keeps
$\nabla\cdot\mathbf B$ under control with a diffusive correction
proportional to $\nabla(\nabla\cdot\mathbf B)$ added to Faraday's law
([Artola et al. (2021)](/sources/artola-2021.md), §2).

Physics extensions sit on the same core:

* **Impurities.** [Bhole et al. (2023)](/sources/bhole-2023.md), Eqs. 3–5,
  11–13, add an impurity mass density with its own continuity equation,
  a pressure $p=\rho T$ plus an impurity contribution proportional to
  $\rho_{\rm imp}T$ whose weight counts the free electrons of the coronal
  charge-state mix, an ionization-potential-energy term in the pressure
  equation and a radiation sink; see
  [coronal-equilibrium impurity model](/methods/coronal-equilibrium-impurity-model.md).
* **Neutrals.** [Taheri et al. (2022)](/sources/taheri-2022.md), Eqs. 1–6,
  couple a hydrogenic neutral fluid through ionization, recombination and
  charge-exchange sources in all moment equations; see
  [fluid neutral models](/methods/fluid-neutral-models.md).
* **Bootstrap current.** [Saxena et al. (2025)](/sources/saxena-2025.md),
  Eq. 2.1, put the bootstrap current in $\mathbf J_x$; see
  [bootstrap current](/definitions/bootstrap-current.md).

## Properties

* **Waves.** The full system carries the fast magnetosonic wave. It
  therefore "may demand higher resolution" and is harder to stabilize in
  the presence of shocks than reduced MHD
  ([Bhole et al. (2023)](/sources/bhole-2023.md), §1, p. 3).
* **Momentum.** Full MHD conserves linear momentum exactly at the level of
  the equations, while reduced MHD does not
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.3).
* **Projection of momentum.** JOREK projects the momentum equation on the
  test vectors $(\mathbf e_R,\mathbf e_Z,\mathbf B)$. The third projection is
  parallel, so $\mathbf J\times\mathbf B$ drops out of it exactly at the
  discrete level, and the fast wave is removed from that scalar equation
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eqs. 21–24;
  [Bhole et al. (2023)](/sources/bhole-2023.md), p. 20).
* **Resistivity.** The Spitzer scaling $\eta\propto T^{-3/2}$ is the common
  choice, often multiplied by a constant: 10 times Spitzer in the
  [NSTX VDE benchmark](/benchmarks/nstx-vde-benchmarks.md),
  $\eta=1.75\times10^{-2}\,T_e[\mathrm{eV}]^{-3/2}\ \Omega\,\mathrm m$
  ([Artola et al. (2021)](/sources/artola-2021.md), Table 2), and a factor
  $\eta_0\in\{1,10,10^3,10^4\}$ on $\eta_{\rm norm}=2.74\ \Omega\,\mathrm m$
  in M3D-C1 ([Saxena et al. (2025)](/sources/saxena-2025.md), Eq. 3.2).
  [Bhole et al. (2023)](/sources/bhole-2023.md), Eq. 14, add a
  $Z_{\rm eff}$ dependence.
* **Numerics.** The same system is advanced explicitly (CLT: fourth-order
  finite differences, fourth-order Runge–Kutta), implicitly (M3D-C1,
  JOREK) or with a semi-implicit leapfrog (NIMROD)
  ([Zhang et al. (2021)](/sources/zhang-2021.md), §2;
  [Artola et al. (2021)](/sources/artola-2021.md), Table 1); see
  [implicit time integration](/methods/implicit-time-integration.md) and
  [semi-implicit leapfrog](/methods/semi-implicit-leapfrog.md).

## Verification of full against reduced models

JOREK's full and reduced models agree within 5% on peeling–ballooning
growth rates in a JET-like X-point plasma, and full MHD agrees with
CASTOR3D on the $1/1$ resistive kink and the $2/1$ tearing mode where
reduced MHD deviates
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.4–4.5, Figs. 18–22;
see [reduced MHD](/methods/reduced-mhd.md)). In the
[NSTX VDE benchmarks](/benchmarks/nstx-vde-benchmarks.md) the full-MHD
codes M3D-C1 and NIMROD and the reduced-MHD JOREK agree on the onset of the
3D phase, the thermal-quench duration and the wall forces, but not on the
toroidal asymmetry of $I_p$
([Artola et al. (2021)](/sources/artola-2021.md), §4–5).

## Printed variants

These are recorded as printed and do not change the model above:

* [Bhole et al. (2023)](/sources/bhole-2023.md), Eq. 1, prints
  $\partial_t\mathbf A+\mathbf v\times\mathbf B=\ldots$; the weak form on
  p. 20 uses $\partial_t\mathbf A-\mathbf v\times\mathbf B$, the physical
  sign. Their p. 8 source term contains Ohmic heating, while §4.3.1 and §5
  state that the model used "does not include the Ohmic heating term".
* [Saxena et al. (2025)](/sources/saxena-2025.md), Eq. C5, prints the heat
  flux with $+\kappa_\perp\nabla T_e$, against the Fourier sign.
* [Ma & Guo (2022)](/sources/ma-2022.md), §2, print normalizations without
  the minor radius ($\eta/(\mu_0{}^2/\tau_A)$, $\tau_A=V_A$).

# Citations

* [Zhang et al. (2021)](/sources/zhang-2021.md) — CLT and M3D-C1 resistive MHD model and normalization.
* [Artola et al. (2021)](/sources/artola-2021.md) — JOREK, M3D-C1 and NIMROD model descriptions.
* [Bhole et al. (2023)](/sources/bhole-2023.md) — JOREK full MHD with impurities.
* [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — JOREK full MHD equations and closures.
* [Ma & Guo (2022)](/sources/ma-2022.md) — compressible resistive MHD of the SCELT eigenvalue code.
* [Saxena et al. (2025)](/sources/saxena-2025.md) — M3D-C1 single-fluid equations with a non-inductive current.
* [Taheri et al. (2022)](/sources/taheri-2022.md) — NIMROD resistive MHD with a neutral fluid.
