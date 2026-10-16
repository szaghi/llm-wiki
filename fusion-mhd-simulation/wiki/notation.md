---
type: Definition
title: "Notation registry"
description: "Normative symbol registry — every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-10-16T00:00:00Z
---

# Notation registry

Every concept page of this bundle writes mathematics in the symbols below.
A source's own symbols are translated on its Source page (`# Notation map`).
The registry was seeded on 2026-10-16 from the conventions that dominate the
nonlinear-MHD code literature of the first chunk (JOREK, M3D-C1, NIMROD, CLT,
BOUT++, the hybrid kinetic-MHD codes and the 3D equilibrium codes): SI units
with $\mu_0$ explicit, cylindrical coordinates $(R,Z,\phi)$, poloidal flux per
radian, $\gamma$ reserved for growth rates. Extend this registry, and log the
extension, before writing a symbol it lacks.

**Normalized units.** Most codes compute in normalized units (JOREK:
$\mu_0=1$, density normalized to a reference mass density; M3D-C1 and CLT:
Alfvén units with a reference length, field and density). Concept pages write
equations in SI; a number quoted from a normalized-unit source carries its
normalization in words ("$\eta=10^{-6}$ in JOREK units"), and the Source page
records the conversion when the source gives it.

## 1. Coordinates and geometry

| Symbol | Meaning | Note |
|---|---|---|
| $R$, $Z$, $\phi$ | cylindrical coordinates: major radius, vertical coordinate, geometric toroidal angle | the sign convention of $\phi$ is stated per page when it matters (COCOS) |
| $\mathbf e_R$, $\mathbf e_Z$, $\mathbf e_\phi$ | unit vectors | $\nabla\phi=\mathbf e_\phi/R$ |
| $\theta$ | a poloidal angle | which one (geometric, straight-field-line, Boozer, VMEC) is stated per page |
| $\zeta$ | a toroidal angle of a flux-coordinate system that differs from $\phi$ (Boozer, VMEC, DESC) | |
| $x$, $y$, $z$ | field-aligned coordinates: radial label, parallel (poloidal) coordinate, binormal coordinate | defined on the field-aligned-coordinates page |
| $r$, $a$ | geometric minor radius and its edge value | |
| $R_0$ | major radius of the magnetic axis or of the device | |
| $s$ | a normalized radial flux label | $s=\sqrt{\psi_N}$ or $s=\sqrt{\psi_{t,N}}$, stated per page |
| $\mathbf n$ | outward unit normal of a boundary or wall | |
| $N_{\mathrm{fp}}$ | number of field periods of a stellarator | |

## 2. Fields and potentials

| Symbol | Meaning | Note |
|---|---|---|
| $\mathbf B$, $\mathbf E$ | magnetic and electric fields | |
| $B$, $\mathbf b$ | field strength and unit vector $\mathbf b=\mathbf B/B$ | |
| $\mathbf A$ | magnetic vector potential, $\mathbf B=\nabla\times\mathbf A$ (plus a vacuum toroidal field when stated) | |
| $\Phi$ | electrostatic potential | |
| $\mathbf J$ | current density, $\mu_0\mathbf J=\nabla\times\mathbf B$ | $j_\phi$, $j_\parallel=\mathbf J\cdot\mathbf b$ components |
| $\psi$ | poloidal magnetic flux **per radian** ($\psi=RA_\phi$ in axisymmetry) | the poloidal flux through a disc is $2\pi\psi$; sources using the full flux are converted on their Source page |
| $\psi_N$ | normalized poloidal flux, $0$ on the axis and $1$ at the separatrix or boundary | |
| $\psi_t$, $\psi_{t,N}$ | toroidal flux per radian and its normalized value | stellarator and 3D-equilibrium pages |
| $F$ | $F=RB_\phi$; $F_0$ its constant (vacuum) value | |
| $\chi$ | magnetic scalar potential of the vacuum (coil) field, $\mathbf B_{\mathrm{vac}}=\nabla\chi$ | stellarator reduced MHD; tokamak limit $\chi=F_0\phi$ |
| $\mu_0$, $\varepsilon_0$, $c$ | vacuum permeability, permittivity, speed of light | |

## 3. Fluid quantities

| Symbol | Meaning | Note |
|---|---|---|
| $\rho$ | mass density | never a radial coordinate in this bundle |
| $n_s$ | number density of species $s$ | $s\in\{e,i\}$; neutrals $n_{\mathrm N}$, impurities $n_{\mathrm{imp}}$, runaway electrons $n_{\mathrm{RE}}$, energetic particles $n_h$ |
| $\mathbf v$ | fluid (centre-of-mass) velocity | $v_\parallel=\mathbf v\cdot\mathbf b$ |
| $p$, $p_s$ | total and species pressure | $p=\sum_s n_sT_s$ |
| $T$, $T_s$ | temperature, in energy units | a single-temperature model writes $T$ for the total $T_e+T_i$ only if the page says so |
| $\mathsf P_h$ | pressure tensor of the energetic (hot) particles | $p_{\parallel h}$, $p_{\perp h}$ its gyrotropic components |
| $\Gamma$ | ratio of specific heats | **not** $\gamma$, which is a growth rate |
| $\eta$ | electrical resistivity | $\eta_{\mathrm{Sp}}$ Spitzer value; $\eta_h$ hyper-resistivity |
| $\nu$ | viscosity | kinematic or dynamic is stated per page; $\nu_h$ hyperviscosity |
| $\kappa_\parallel$, $\kappa_\perp$ | parallel and perpendicular heat conductivity (or diffusivity, stated per page) | $\chi_\parallel$, $\chi_\perp$ when a source writes thermal diffusivities |
| $D_\parallel$, $D_\perp$ | particle diffusivities | |
| $S_\rho$, $S_p$, $\mathbf S_{\mathbf v}$ | mass, pressure (energy) and momentum sources | |
| $Z$, $Z_{\mathrm{eff}}$, $z$ | ion charge, effective charge, impurity charge state | |

## 4. Reduced MHD and potentials of the flow

| Symbol | Meaning | Note |
|---|---|---|
| $u$ | velocity stream function of reduced MHD | the page writes its ansatz, e.g. $\mathbf v_\perp=-R^2\nabla u\times\nabla\phi$ |
| $\varpi$ | toroidal (or $\nabla\chi$-directed) vorticity, $\varpi=\Delta^\perp u$ or as defined per page | never $\omega$, which is a frequency |
| $j$ | the scalar current variable of reduced MHD, $j=\Delta^*\psi$ up to sign and $\mu_0$, as defined per page | |
| $\Delta^*$ | Grad–Shafranov operator, $\Delta^*\psi=R^2\nabla\cdot(R^{-2}\nabla\psi)$ | |
| $[f,g]$ | Poisson bracket of two scalars, defined per page (e.g. $\mathbf e_\phi\cdot\nabla f\times\nabla g$) | |
| $\nabla_\parallel$, $\nabla_\perp$ | gradients along and across $\mathbf B$ | |
| $\lambda_{\mathrm o}$ | small ordering parameter of a reduction (aspect ratio, $L_\perp/L_\parallel$) | stated per page |

## 5. Equilibrium and stability

| Symbol | Meaning | Note |
|---|---|---|
| $q$, $\iota$ | safety factor and rotational transform, $\iota=1/q$ | $q_0$ on axis, $q_{95}$ at $\psi_N=0.95$, $q_a$ the cylindrical edge value, $q_{\min}$ the minimum |
| $\beta$, $\beta_p$, $\beta_N$ | plasma beta, poloidal beta, normalized beta | $\beta_h$ energetic-particle beta |
| $l_i$ | internal inductance | definition stated per page |
| $m$, $n$ | poloidal and toroidal mode numbers | $m/n$ the helicity of a mode |
| $\gamma$ | linear growth rate | $\gamma\tau_A$ when normalized |
| $\omega$ | angular (real) frequency of a mode | $\omega_r$, $\gamma$ the real and imaginary parts; $f$ never a frequency here |
| $\tau_A$, $v_A$ | Alfvén time and speed, $v_A=B/\sqrt{\mu_0\rho}$ | the length in $\tau_A$ is stated per page |
| $\tau_R$, $S$ | resistive time and Lundquist number, $S=\tau_R/\tau_A$ | |
| $\Delta'$ | tearing stability index | |
| $W_{\mathrm{mag}}^{(n)}$, $W_{\mathrm{kin}}^{(n)}$ | magnetic and kinetic energy of toroidal harmonic $n$ | |
| $W_{\mathrm{th}}$ | thermal energy | |

## 6. Walls, disruptions, currents

| Symbol | Meaning | Note |
|---|---|---|
| $I_p$ | plasma current | |
| $I_{\mathrm{halo}}$ | halo current (poloidal unless stated) | |
| $\mathrm{TPF}$ | toroidal peaking factor of the halo current | |
| $\eta_w$, $d_w$ | wall resistivity and thickness | thin-wall codes use $\eta_w/d_w$ |
| $\tau_w$ | wall time | |
| $\mathbf F_w$ | electromagnetic force on the wall | $F_{w,z}$ vertical, $F_{w,h}=\sqrt{F_{w,x}^2+F_{w,y}^2}$ horizontal (sideways) |
| $E_\parallel$, $E_c$ | parallel electric field and the critical field of runaway generation | $E_c^{\mathrm{eff}}$ the effective critical field |
| $\mathbf J_{\mathrm{RE}}$ | runaway-electron current density | |
| $\Gamma_{\mathrm{av}}$ | avalanche growth rate of the runaway density | |
| $\mathbf J_x$ | a non-inductive (e.g. bootstrap) current density imposed in Ohm's law | |
| $P_{\mathrm{rad}}$ | radiated power density | |

## 7. Kinetic and particle quantities

| Symbol | Meaning | Note |
|---|---|---|
| $f_s(\mathbf x,\mathbf v,t)$ | distribution function of species $s$ | $f_h$ energetic particles; $f_0$ equilibrium part, $\delta f$ perturbation |
| $\mathbf x_p$, $\mathbf v_p$ | position and velocity of marker (macroparticle) $p$ | $\mathbf X$ a guiding-centre position |
| $w_p$ | marker weight (full-$f$) or $\delta f$ weight | |
| $v_{\parallel p}$ | parallel velocity of a particle | distinct from the fluid $v_\parallel$ |
| $\mu$ | magnetic moment of a particle | never a viscosity |
| $\mathcal E$ | particle kinetic energy | |
| $P_\phi$ | canonical toroidal momentum | |
| $\Omega_s$ | cyclotron frequency of species $s$ | |
| $\rho_L$ | Larmor radius | |
| $m_s$, $q_s$, $e$ | species mass and charge, elementary charge | |

## 8. Discretization and time integration

| Symbol | Meaning | Note |
|---|---|---|
| $\Delta t$, $\Delta x$ | time step and a mesh spacing | |
| $h_e$ | element size | defined per page |
| $N_{\mathrm{tor}}$ | number of toroidal harmonics kept ($n=0,\dots,n_{\max}$) | the counting convention is stated per page |
| $\theta_{\mathrm{t}}$ | implicitness parameter of a $\theta$-scheme ($1/2$ Crank–Nicolson, $1$ implicit Euler) | distinct from the angle $\theta$ |
| $\tau_{\mathrm{s}}$ | stabilization (intrinsic time-scale) parameter of a stabilized FEM | |
| $\mathcal L$ | a linearized (Jacobian) operator | |
| $\mathbf u$ | the full discrete state vector | distinct from the stream function $u$ |

## 9. Extensions logged with chunk 1 (2026-10-16)

Symbols the chunk-1 concept pages needed beyond §§1–8. Each is also defined
where it is used.

| Symbol | Meaning | Note |
|---|---|---|
| $\delta(\cdot)$ | linear perturbation of a field, e.g. $\delta\mathbf B$, $\delta p$, $\delta B_\parallel$ | |
| $A_\parallel$ | $\mathbf A\cdot\mathbf b$ | |
| $\langle\cdot\rangle$ | flux-surface average or gyroaverage, as the page states | |
| $\nabla_{\mathrm{pol}}$ | gradient in the $(R,Z)$ plane | |
| $\theta^*$ | straight-field-line poloidal angle | |
| $\hat s$, $\alpha_{\mathrm{b}}$ | magnetic shear and normalized pressure gradient of ballooning theory | $s$ stays the radial label |
| $\psi_\chi$, $\partial^\parallel$, $\nabla^\perp$, $\Delta^\perp$ | stellarator reduced MHD: field-line-bending potential in $\mathbf B=\nabla\chi+\nabla\psi_\chi\times\nabla\chi$ and derivatives relative to $\nabla\chi$ (not $\mathbf B$) | $\psi_\chi\to\psi/F_0$ in the tokamak limit |
| $G$, $I$, $M$, $N$ | Boozer covariant field components; helicity integers of a quasi-symmetric field | |
| $\mathbf f$ | normal-projected Maxwell stress on a surface, $[(\mathbf B\cdot\mathbf n)\mathbf B-\tfrac12B^2\mathbf n]/\mu_0$ | wall-force pages |
| $\mathbf J_h$, $\mathbf M_h$, $\mathbf K_h$ | energetic-particle current, magnetization and momentum densities | current coupling |
| $\mathbf B^*$, $B^*_\parallel$ | guiding-centre modified field and its parallel component (phase-space Jacobian) | |
| $\mathbf v_d$, $\mathbf v_E$ | guiding-centre drift velocity; $\mathbf E\times\mathbf B$ velocity | |
| $g$ | marker phase-space sampling density | $\delta f$ pages |
| $\mathsf I$ | identity tensor | |
| $\langle\sigma v\rangle_{\mathrm{ion}}$, $\langle\sigma v\rangle_{\mathrm{rec}}$, $\langle\sigma v\rangle_{\mathrm{cx}}$ | ionization, recombination, charge-exchange rate coefficients (per charge state $z$ when subscripted) | |
| $\mathcal R_{\mathrm{ion}}$, $\mathcal R_{\mathrm{rec}}$, $\mathcal R_{\mathrm{cx}}$ | volumetric reaction rates | never $\Gamma$ |
| $n_{\mathrm{imp},z}$, $\langle z\rangle$, $Z_{\mathrm{imp}}$, $\rho_{\mathrm{imp}}$, $m_{\mathrm{imp}}$ | density of charge state $z$, mean charge, atomic number, mass density and mass of an impurity | |
| $\varepsilon_{\mathrm{ion},z}$, $L_{\mathrm{rad}}$ | ionization energy of state $z$; radiation power coefficient ($P_{\mathrm{rad}}=n_en_{\mathrm{imp}}L_{\mathrm{rad}}$) | line, recombination, bremsstrahlung parts subscripted |
| $\rho_{\mathrm N}$, $\mathbf v_{\mathrm N}$, $T_{\mathrm N}$, $D_{\mathrm N}$ | neutral mass density, velocity, temperature, diffusivity | |
| $\mathsf D$, $\mathsf K$ | anisotropic diffusion and conduction tensors $X_\parallel\mathbf b\mathbf b+X_\perp(\mathsf I-\mathbf b\mathbf b)$ | |
| $c_s$, $\delta_{\mathrm{sh}}$ | ion sound speed; sheath heat-transmission factor | |
| $\ln\Lambda$, $E_D$, $\tau_c$ | Coulomb logarithm, Dreicer field, relativistic collision time | runaway pages |
| $S_{\mathrm{av}}$, $S_{\mathrm T}$, $S_{\mathrm C}$ | avalanche, tritium-decay and Compton runaway sources | |
| $\Lambda_k$ | a finite-element basis function | projection pages |
| $\xi_{\mathrm t}$, $\phi_{\mathrm t}$ | multistep weights of the $\theta$–$\xi$ time scheme | with $\theta_{\mathrm t}$ (§8) |
| $v_{f}$ | fast magnetosonic speed | stabilization pages |
| $\nu_{\mathrm{sc}}$ | shock-capturing artificial diffusivity | |
| $\hat q$, $\mathcal I_s$ | local field-line pitch; integrated shear | field-aligned coordinates |

Other page-local symbols (Dommaschk coefficients, Sauter coefficients, matrix
names of a particular code) are defined on their page and not registered.
