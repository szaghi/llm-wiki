---
type: Method
title: "Single-fluid visco-resistive MHD model"
description: "The full (non-reduced) single-fluid resistive MHD system, with one or two temperatures, viscosity, anisotropic heat conduction and particle diffusion, that the nonlinear tokamak and stellarator codes solve; its variants differ in the evolved field (B or A), the viscous and heat-flux closures, the source current in Ohm's law and the normalization, and its regime is set by the Lundquist, magnetic Prandtl and Hartmann numbers."
status: established
aliases: [full MHD, visco-resistive full MHD, single-fluid resistive MHD, viscoresistive MHD]
tags: [full-mhd, tokamak]
timestamp: 2026-10-16T18:35:00Z
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
| CLT and M3D-C1 benchmark model ([Zhang et al. (2021)](/sources/zhang-2021.md), Eqs. 1.1–1.6) | $\mathbf B$ (CLT), $\mathbf A$ (M3D-C1) | kinematic, $\rho\nabla\cdot(\nu\nabla\mathbf v)$ | diffusion of $\rho-\rho_{\rm eq}$; $\nabla\cdot[\kappa_\perp\nabla_\perp(p-p_{\rm eq})]+\nabla\cdot(\kappa_\parallel\nabla_\parallel p)$ with diffusivities acting on $p$; no Ohmic heating | $\mathbf J_x=\mathbf J_{\rm eq}$, so the equilibrium is not resistively diffused | Alfvén units, $L_0=1$ m, $B=1$ T, number density $10^{20}$ m$^{-3}$; $\eta$ in units of $\mu_0L_0^2/\tau_A$ |
| SCELT ([Ma & Guo (2022)](/sources/ma-2022.md), Eqs. 1–7) | $\mathbf B$, linearized | $\nu\nabla^2\mathbf v$ | none; Ohmic heating $(\Gamma-1)\eta J^2$ | $\mathbf J_x=0$ | $\mu_0=1$, lengths in $a$, time in $\tau_A$ |
| JOREK full MHD ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eqs. 1–24; [Bhole et al. (2023)](/sources/bhole-2023.md), Eqs. 1–10) | $\mathbf A$, Weyl gauge, frozen $F$ | stress tensor: parallel (Braginskii-type) part, perpendicular part with $\nu_\perp\propto T^{-3/2}$, neoclassical poloidal friction, gyroviscous cancellation; Bhole et al. use a scalar $\nu\propto T^{-3/2}$ in Laplacian form | anisotropic tensors $X_\parallel\mathbf b\otimes\mathbf b+X_\perp(\mathbf I-\mathbf b\otimes\mathbf b)$; $\kappa_\parallel\propto T^{5/2}$ (Spitzer–Härm), optional cap | $\eta\propto T^{-3/2}$; diamagnetic electron-pressure term; $\mathbf J_x$ a toroidal source current, optionally bootstrap-evolving | JOREK units, $\mu_0=1$, $(\Gamma-1)$ absorbed into $\kappa$ |
| M3D-C1 single fluid ([Saxena et al. (2025)](/sources/saxena-2025.md), App. C; [Artola et al. (2021)](/sources/artola-2021.md), §2) | $\mathbf A$ through scalar potentials | full ion stress tensor (perpendicular, gyroviscous, parallel); electron viscosity as hyper-resistivity | $\kappa_\parallel$, $\kappa_\perp$ on $T_e$ | $\eta\,\mathbf J\cdot(\mathbf J-\mathbf J_x)$ heating, $\mathbf J_x$ the bootstrap current; $\eta=\eta_{\rm norm}\eta_0T_e^{-3/2}$ | SI, $\mu_0$ explicit |
| NIMROD ([Artola et al. (2021)](/sources/artola-2021.md), §2; [Taheri et al. (2022)](/sources/taheri-2022.md), Eqs. 3, 5, 16–18) | $\mathbf B$ and $\mathbf v$ components | isotropic stress $-\rho\nu(\nabla\mathbf v+\nabla\mathbf v^{\mathsf T}-\tfrac23\mathbf I\nabla\cdot\mathbf v)$, $\nu$ kinematic | temperature equation instead of pressure equation; isotropic particle diffusivity | $\eta$ from the toroidally symmetric part of $T$ (Artola et al.) | SI |
| NIMROD with neoclassical closures ([Howell et al. (2022)](/sources/howell-2022.md), Eqs. 1–10) | $\mathbf B$, with $D_B\nabla\nabla\cdot\mathbf B$ cleaning in Faraday's law ($D_B$ page-local, $\kappa_B$ in the source) | classical plus heuristic neoclassical ion stress (poloidal flow damping) | species temperature equations, artificial particle diffusivity, anisotropic conduction | $\eta=\eta_0T_e^{-3/2}$ enhanced; neoclassical electron stress term in Ohm's law gives the bootstrap drive, no imposed $\mathbf J_x$ | SI |
| NIMROD with KPRAD impurities ([Zeng et al. (2023)](/sources/zeng-2023.md), Eqs. 1–6) | $\mathbf B$ | $\nabla\cdot(\rho\nu\nabla\mathbf v)$, constant $\nu$ | single $T_e$ for all species; continuity per neon charge state; constant $\kappa_\parallel,\kappa_\perp,D$ (diffusivities) | Spitzer $\eta$, $\mathbf J_x=0$; radiation sink | SI |
| NIMROD two-fluid ([Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md), Eqs. 1–6) | $\mathbf B$, with divergence cleaning | unmagnetized stress only | two temperatures, anisotropic conduction | Hall and electron-inertia terms in the flow study, no $\nabla p_e$ term as printed; $\eta$ given as a magnetic diffusivity | SI |
| M3D-C1 stellarator ([Zhou et al. (2023)](/sources/zhou-2023.md), Eqs. 1–3) | $\mathbf B$ (as printed) | $\Pi=-\nu(\nabla\mathbf v+\nabla\mathbf v^{\mathsf T})-2(\nu_c-\nu)(\nabla\cdot\mathbf v)\mathsf I$, dynamic, with a separate compressional viscosity $\nu_c$ | continuity not solved ($\rho$ constant); heat flux $-\kappa_\perp\nabla T-\kappa_\parallel\mathbf b\mathbf b\cdot\nabla T$; Gaussian heat source | $\mathbf J_x$ the ECCD current, toroidal; Ohmic heating printed as $\eta J^2$ (see *Contradictions*) | SI |
| JOREK full MHD, two temperatures ([Zhang et al. (2025)](/sources/zhang-2025.md), Eqs. 1–4, Table 1) | $\mathbf A$, Weyl gauge, frozen $F(\psi)$ | dynamic, $\nabla\cdot(\nu\nabla\mathbf v)$, $\nu\propto T_e^{-3/2}$; momentum loss $-S_\rho\mathbf v$ | separate $p_i$, $p_e$ equations; $\kappa_\parallel\propto T^{5/2}$ reduced 30 times for the heat-flux limit, $\kappa_\perp$ profiles solved so that the 2D temperatures stay stationary; $D_\perp=0$, uniform $D_\parallel$ for stability; no Ohmic heating, no ion–electron equipartition ("causing numerical instabilities") | $\eta\propto T_e^{-3/2}$ applied **only to the toroidal component**, $\eta(j_\phi-J_{x,\phi})\mathbf e_\phi$, "to improve the numerical stability", so $A_R$, $A_Z$ and $B_\phi$ evolve ideally; $\mathbf J_x$ the smoothed NBI + ECCD + bootstrap source; no Hall or diamagnetic terms | JOREK units, SI conversions printed |
| M3D-C1 stellarator, continuity solved ([Wright & Ferraro (2024)](/sources/wright-2024.md), App. A, Eqs. 1–2) | $\mathbf B$ (as printed) | dynamic $\nu=3.65\times10^{-4}$ kg/(m s), form of the stress not given; no hyper-diffusion | continuity solved, density fixed at the wall; heat flux with the full gradient in the perpendicular term, $\kappa_\perp/\kappa_\parallel=10^{-6}$ | $\eta=\eta_{\rm norm}[\eta_c+\eta_0T_e^{-3/2}]$, constant or Spitzer times 1, 10, 100; $\mathbf J_x=0$, Ohmic heating $\eta J^2$ | M3D-C1 units, $\eta_{\rm norm}=2.74$ Ω m |
| NIMROD two-fluid, two ion species ([Rahman et al. (2024)](/sources/rahman-2024.md), §II B 1, Eqs. 1–4) | $\mathbf B$ | ion stress $\mathsf\Pi_i$ with perpendicular, parallel, gyroviscous and neoclassical parts | species continuity (D, C, $n_e$ by quasineutrality) with $D_\perp$ and a toroidal hyperdiffusivity; species temperature equations, one ion temperature | Hall, $\nabla p_e$ and $\nabla\cdot\mathsf\Pi_e$ terms in Ohm's law; Spitzer $\eta$ with multi-ion collisions | SI |
| M3D-C1 with runaway electrons ([Liu et al. (2021)](/sources/liu-2021.md), Eqs. 1–9) | $\mathbf A$ | not specified | single temperature $T_e=T_i$ | $\mathbf E=-\mathbf v\times\mathbf B+\eta(\mathbf J-\mathbf J_{\rm RE})$, heating $\eta(\mathbf J-\mathbf J_{\rm RE})^2$, momentum force $en_{\rm RE}\mathbf E+(\mathbf J-\mathbf J_{\rm RE})\times\mathbf B$ | $\mu_0=1$ in Ampère's law as printed |

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
  [Howell et al. (2022)](/sources/howell-2022.md), Eqs. 8–10, obtain it
  instead from a heuristic neoclassical electron stress in Ohm's law; see
  [neoclassical tearing mode](/definitions/neoclassical-tearing-mode.md).
* **Current drive.** [Zhou et al. (2023)](/sources/zhou-2023.md), Eq. 3, put a
  fixed ECCD profile in the Ohm's-law source current.
* **Runaway electrons.** [Liu et al. (2021)](/sources/liu-2021.md), Eqs. 1–5,
  remove the runaway current from the resistive term and add the runaway
  continuity equation; see
  [runaway-electron fluid model](/methods/runaway-electron-fluid-model.md).

## Properties

* **Dimensionless regime.** Besides the Lundquist number
  $S=\tau_R/\tau_A$, the visco-resistive regime is set by the magnetic
  Prandtl number $\nu\mu_0/(\rho\eta)$ (dynamic $\nu$) and the Hartmann
  number $\big(\mu_0L^2v_A^2/(\eta\nu_{\rm kin})\big)^{1/2}$, with
  $\nu_{\rm kin}$ the kinematic viscosity and $L$ a reference length. In the
  JOREK flux-pumping study of ASDEX Upgrade, with $L=0.1$ m, $S=2.8\times10^8$,
  the Prandtl number is 1400 and the Hartmann number $7.9\times10^6$
  (realistic resistivity, semi-empirical viscosity between the Braginskii
  perpendicular and gyroviscous values); lowering the Hartmann number by
  raising $\eta$ and $\nu$ changes a saturated helical core into
  sawtooth-like oscillations near $10^5$ and a resistive internal kink near
  $10^4$ ([Zhang et al. (2025)](/sources/zhang-2025.md), §2.4, Table 1,
  §6.2, not shown). The reversed-field-pinch analogue, single versus
  multiple helicity at Hartmann numbers below about $10^3$ and above about
  $10^4$, is cited there (Cappello & Escande 2000, as cited). Keeping
  $\nu\propto T^{-3/2}$ with $\eta\propto T^{-3/2}$ holds the Prandtl number
  fixed ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md);
  [Hu et al. (2021)](/sources/hu-2021.md), on the reduced model).
* **Why full MHD for the $1/1$ quasi-interchange.** The mode has
  $B\,\delta B_\parallel\sim-\delta p$, which the JOREK reduced model
  cannot represent (Zhang et al. 2025, §2.2, citing Pamela et al. 2020; see
  [reduced MHD](/methods/reduced-mhd.md)).

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
* [Zeng et al. (2023)](/sources/zeng-2023.md), Eq. 4, print the compression
  and conduction terms of the temperature equation with $+$ signs, which as
  typeset makes conduction anti-diffusive.
* [Liu et al. (2021)](/sources/liu-2021.md), Eq. 9, print the heat flux
  without the minus sign, also anti-diffusive with $-\nabla\cdot\mathbf q$ in
  their Eq. 8.
* [Zhou et al. (2023)](/sources/zhou-2023.md) use the full gradient in the
  perpendicular heat flux, so the effective parallel conductivity is
  $\kappa_\parallel+\kappa_\perp$, negligible at their anisotropy; they call the
  system "extended MHD" although no two-fluid term is active.
* [Howell et al. (2022)](/sources/howell-2022.md), App. A, write the ion
  viscous power with the opposite sign of their momentum equation.

## Contradictions

* **Ohmic heating with a source current in M3D-C1.** *Open.*
  [Saxena et al. (2025)](/sources/saxena-2025.md), App. C, Eq. C3, print the
  M3D-C1 single-fluid heating as $\eta\,\mathbf J\cdot(\mathbf J-\mathbf J_x)$,
  the form that follows from $(\mathbf E+\mathbf v\times\mathbf B)\cdot\mathbf J$
  (reference form above). [Zhou et al. (2023)](/sources/zhou-2023.md),
  Eqs. 2–3, print for the same code $\eta J^2$ in the pressure equation
  together with $\eta(\mathbf J-\mathbf J_x)$ in Ohm's law, with $\mathbf J_x$ the
  ECCD current. Either the code uses $\eta J^2$ in that run, so that the
  energy associated with the source current is not accounted for in the same
  way, or the printed equation is simplified; neither source comments.
  [Wright & Ferraro (2024)](/sources/wright-2024.md) (App. A) also print
  $\eta J^2$ for the M3D-C1 stellarator model, but with $\mathbf J_x=0$,
  where the two forms coincide, so they do not bear on the entry.

# Citations

* [Zhang et al. (2021)](/sources/zhang-2021.md) — CLT and M3D-C1 resistive MHD model and normalization.
* [Artola et al. (2021)](/sources/artola-2021.md) — JOREK, M3D-C1 and NIMROD model descriptions.
* [Bhole et al. (2023)](/sources/bhole-2023.md) — JOREK full MHD with impurities.
* [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — JOREK full MHD equations and closures.
* [Ma & Guo (2022)](/sources/ma-2022.md) — compressible resistive MHD of the SCELT eigenvalue code.
* [Saxena et al. (2025)](/sources/saxena-2025.md) — M3D-C1 single-fluid equations with a non-inductive current.
* [Taheri et al. (2022)](/sources/taheri-2022.md) — NIMROD resistive MHD with a neutral fluid.
* [Howell et al. (2022)](/sources/howell-2022.md) — NIMROD with heuristic neoclassical closures.
* [Zeng et al. (2023)](/sources/zeng-2023.md) — NIMROD with charge-state-resolved impurities.
* [Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md) — NIMROD two-fluid Ohm's law.
* [Zhou et al. (2023)](/sources/zhou-2023.md) — M3D-C1 stellarator model with ECCD source current.
* [Liu et al. (2021)](/sources/liu-2021.md) — M3D-C1 model with a runaway-electron fluid.
* [Zhang et al. (2025)](/sources/zhang-2025.md) — JOREK two-temperature full MHD with toroidal-only resistivity; Prandtl and Hartmann numbers.
* [Wright & Ferraro (2024)](/sources/wright-2024.md) — M3D-C1 stellarator model with continuity and four resistivity models.
* [Rahman et al. (2024)](/sources/rahman-2024.md) — NIMROD two-fluid model with carbon and deuterium ions.
