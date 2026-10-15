---
type: Definition
title: "Notation registry"
description: "Normative symbol registry — every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-10-15T00:00:00Z
---

# Notation registry

Every concept page of this bundle writes mathematics in the symbols below.
A source's own symbols are translated on its Source page (`# Notation map`).
The registry was seeded on 2026-10-14 from the conventions that dominate the
low-temperature plasma and electric-propulsion modelling literature: SI
units, a species index $s$, Hall-thruster coordinates with $z$ axial, $r$
radial and $\theta$ azimuthal (the $\mathbf E\times\mathbf B$ direction),
and temperatures in energy units. Extend this registry, and log the
extension, before writing a symbol it lacks.

## 1. Coordinates, time, discretization

| Symbol | Meaning | Note |
|---|---|---|
| $\mathbf x$, $t$ | position, time | |
| $z$, $r$, $\theta$ | axial, radial, azimuthal coordinates of an axisymmetric thruster | $\theta$ is the $\mathbf E\times\mathbf B$ direction in a Hall thruster |
| $x$, $y$ | Cartesian coordinates of planar (e.g. axial–azimuthal) simulation domains | the mapping to $z,\theta$ is stated per page |
| $\Delta x$, $\Delta t$ | cell size, time step | |
| $L$ | a domain or channel length | qualified by subscript when several appear |

Conventions: a vector component is written with the coordinate after a
comma in the subscript, $u_{e,\theta}$, $j_{z}$, $E_{\theta}$; one-dimensional
axial models drop it ($u_i$ is the axial ion velocity) and say so. A
subscript $0$ marks a reference or upstream value ($n_0$, $T_{e0}$).
$\langle\cdot\rangle$ is an average (the page states over what: azimuth,
time, an ensemble) and $\tilde{(\cdot)}$ the fluctuation about it.

## 2. Species and kinetic description

| Symbol | Meaning | Note |
|---|---|---|
| $s$ | species index; $s\in\{e,i,n\}$ for electrons, ions, neutrals | |
| $m_s$, $q_s$ | species mass and charge | $q_e=-e$ |
| $e$ | elementary charge | |
| $Z$ | ion charge state | |
| $f_s(\mathbf x,\mathbf v,t)$ | velocity distribution function | |
| $\mathbf v$ | particle velocity (phase-space variable) | |
| $n_s$ | number density | $n_0$ a reference density |
| $\mathbf u_s$ | mean (fluid) velocity of species $s$ | |
| $T_s$ | temperature, in energy units unless stated | $T_e$ in eV is the common case |
| $T_{\parallel e}$, $T_{\perp e}$ | electron temperatures along and across $\mathbf B$ | |
| $\bar v_s$ | mean thermal speed of species $s$ | |
| $g$ | relative speed of two colliding particles | |
| $p_s$ | scalar pressure, $p_s=n_sT_s$ | |
| $\mathsf P_s$ | pressure tensor | |
| $\mathbf q_s$ | heat-flux vector | |
| $\mathbf j$ | current density | $\mathbf j_s=q_sn_s\mathbf u_s$ |
| $\dot m$ | propellant mass flow rate | |

## 3. Fields

| Symbol | Meaning | Note |
|---|---|---|
| $\phi$ | electrostatic potential | |
| $\mathbf E$, $\mathbf B$ | electric and magnetic fields | $\mathbf B$ is usually applied and static in Hall thrusters |
| $\rho_c$ | charge density | |
| $\varepsilon_0$, $\mu_0$ | vacuum permittivity and permeability | |
| $c$ | speed of light | |
| $k_B$ | Boltzmann constant | |

## 4. Plasma parameters

| Symbol | Meaning | Note |
|---|---|---|
| $\lambda_D$ | Debye length, $\lambda_D=\sqrt{\varepsilon_0T_e/(n_ee^2)}$ ($T_e$ in J) | |
| $\omega_{pe}$, $\omega_{pi}$ | electron and ion plasma frequencies | |
| $\omega_{ce}$ | electron cyclotron frequency, $eB/m_e$ | |
| $r_{L}$ | Larmor radius | subscript $e$ or $i$ when needed |
| $v_{th,s}$ | thermal speed of species $s$ | definition (with or without $\sqrt2$) stated per page |
| $c_s$ | ion acoustic (Bohm) speed, $\sqrt{T_e/m_i}$ | |
| $\nu_{sk}$ | collision frequency of species $s$ with $k$ | e.g. $\nu_{en}$, $\nu_{ei}$; $k=w$ for a wall, $\nu_{iw}$ |
| $\nu_e$ | total effective electron momentum-transfer frequency | |
| $\nu_{\mathrm{ano}}$ | anomalous (effective) collision frequency of a transport model | |
| $\alpha_{\mathrm B}$ | Bohm-type anomalous coefficient in the convention $\nu_{\mathrm{ano}}=\alpha_{\mathrm B}\,\omega_{ce}/16$ | sources writing $\nu_{\mathrm{ano}}=\alpha\,\omega_{ce}$ have $\alpha=\alpha_{\mathrm B}/16$; the conversion is stated on each Source page |
| $\nu_w$ | electron–wall (near-wall) collision frequency | |
| $\nu_{\mathrm{ion}}$, $k_{\mathrm{ion}}$ | ionization frequency and rate coefficient | |
| $\Omega_e$ | electron Hall parameter, $\omega_{ce}/\nu_e$ | |
| $\mu_\perp$, $\mu_\parallel$ | electron mobility across and along $\mathbf B$ | classical $\mu_\perp=\mu_\parallel/(1+\Omega_e^2)$, $\mu_\parallel=e/(m_e\nu_e)$ |
| $\phi^*$ | thermalized potential, constant along a magnetic line under the stated closure | |
| $\gamma$ | polytropic index ($p_s\propto n_s^\gamma$); also the ratio of specific heats of a neutral gas | never a growth rate |
| $\delta_{\mathrm{SEE}}$ | secondary-electron emission yield (emitted per incident electron) | $\delta^*_{\mathrm{SEE}}$ the space-charge-saturation value |
| $\Delta\phi_{\mathrm{sh}}$ | sheath potential drop | |
| $\mathbf R_{sk}$ | momentum-exchange (friction) force density on species $s$ from $k$ | e.g. $\mathbf R_{ei}$, $\mathbf R_{ie}=-\mathbf R_{ei}$ |
| $\sigma_{sk}$ | collision cross section | process named in words |
| $\lambda_{\mathrm{mfp}}$ | mean free path | |
| $\mathrm{Kn}$ | Knudsen number | |

## 5. Particle methods

| Symbol | Meaning | Note |
|---|---|---|
| $W$ | macroparticle weight: real particles per simulation particle | |
| $N_{\mathrm{ppc}}$ | simulation particles per cell | |
| $S(\mathbf x)$ | particle shape (weighting) function | |
| $\mathbf x_p$, $\mathbf v_p$ | position and velocity of macroparticle $p$ | |
| $P_c$ | collision probability of a particle in one step, $1-\exp(-\nu\Delta t)$ | |
| $f_\varepsilon$ | permittivity-scaling factor: $\varepsilon_0\to f_\varepsilon^2\varepsilon_0$, so $\lambda_D\to f_\varepsilon\lambda_D$ | sources that scale $\varepsilon_0$ by a factor $\xi$ have $f_\varepsilon=\sqrt\xi$; stated per Source page |
| $f_m$ | ion-mass scaling factor, $m_i\to m_i/f_m$ | |
| $f_g$ | geometric (size) scaling factor | |

## 5a. Waves and oscillations

| Symbol | Meaning | Note |
|---|---|---|
| $k$, $\omega$ | wavenumber and angular frequency of a mode | $k_\theta$ azimuthal component |
| $\omega_r$, $\omega_i$ | real frequency and growth rate, $\omega=\omega_r+\mathrm i\,\omega_i$ | |
| $\lambda_w$ | wavelength | not $\lambda_D$ |
| $f_{\mathrm{BM}}$ | breathing-mode frequency | |
| $H$ | normalized spectral entropy of a signal | defined on the spectral-entropy page |

## 5b. Inference and uncertainty

| Symbol | Meaning | Note |
|---|---|---|
| $\boldsymbol\vartheta$ | vector of model parameters to calibrate | never $\theta$, the azimuthal coordinate |
| $\mathbf d$ | observed data | |
| $\pi(\boldsymbol\vartheta)$, $\pi(\boldsymbol\vartheta\mid\mathbf d)$ | prior and posterior densities | |
| $\mathcal L(\boldsymbol\vartheta)$ | likelihood | |
| $S_j$, $S_{T,j}$ | first-order and total Sobol' indices of parameter $j$ | |

## 5c. Surfaces

| Symbol | Meaning | Note |
|---|---|---|
| $T_w$ | wall temperature | |
| $v_n$, $v_{t1}$, $v_{t2}$ | normal and two tangential components of a particle velocity at a wall | |
| $\alpha_E$ | energy accommodation coefficient | |
| $\alpha_\tau$, $\alpha_n$ | tangential and normal momentum accommodation coefficients | |
| $Y$ | sputtering yield | |

## 6. Thruster performance

| Symbol | Meaning | Note |
|---|---|---|
| $F$ | thrust | |
| $I_{sp}$ | specific impulse | |
| $g_0$ | standard gravity | |
| $P$ | electric power | |
| $\eta$ | thrust efficiency, $F^2/(2\dot mP)$ unless a page says otherwise | |
| $V_d$, $I_d$ | discharge voltage and current | |
| $I_b$ | ion beam current | |
| $\eta_c$, $\eta_m$ | current utilization $I_b/I_d$ and propellant (mass) utilization efficiency | |
| $I_{\mathrm{bit}}$ | impulse bit of a pulsed thruster | |
| $F_s$, $F_B$, $F_w$ | magnetic-nozzle thrust components: source electron pressure, magnetic (diamagnetic $\mathbf j\times\mathbf B$), wall | $F=F_s+F_B+F_w$ |
| $M_A$ | Alfvén Mach number | |

## 7. Plasma–body interaction

| Symbol | Meaning | Note |
|---|---|---|
| $C_D$ | drag coefficient of a body in a flowing plasma or gas, referred to its cross-section and the flow dynamic pressure | $C_{D0}$: the same body unmagnetized |
| $p_{\mathrm{dyn}}$ | dynamic pressure of the incident flow, $\tfrac12 m_in_iu_i^2$ for an ion flow unless a page states the convention | |
| $p_{Bw}$ | magnetic pressure $B_w^2/(2\mu_0)$ at the body surface | $B_w$ the surface field |
| $r_w$ | radius of a spherical body | |
| $L_{\mathrm{so}}$ | standoff distance of a mini-magnetosphere boundary from the body centre | not the domain length $L$ |
| $F_{\mathrm{IT}}$, $F_{\mathrm{CT}}$ | thrusts of the impulse-transfer and compensation thrusters of an ion-beam shepherd | |
