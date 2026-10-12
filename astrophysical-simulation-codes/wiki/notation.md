---
type: Definition
title: "Notation registry"
description: "Normative symbol registry — every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-10-12T00:00:00Z
---

# Notation registry

This page is **normative** for the bundle. Concept pages must use these symbols
exclusively; each Source page maps its paper's native notation to this registry
in a `# Notation map` section. Extend this registry (and record the extension in
[the log](/log.md)) before writing math that needs a symbol it lacks.

The registry was seeded once, at scaffolding, from the conventions most common
in the astrophysical code papers (Athena, Athena++, PLUTO). It is wiki-native law
from then on.

## Conservation laws

| Symbol | Meaning |
|---|---|
| $u$ | conserved state; $u \in \mathbb{R}^m$ for a system |
| $f(u)$, $\mathbf f(u)$ | physical flux; $\partial_t u + \nabla\cdot\mathbf f(u) = s(u)$ |
| $s(u)$ | source term (gravity, cooling, radiation coupling, geometric terms) |
| $A(u)$ | flux Jacobian; eigenvalues $\lambda^{(p)}$, $p = 1,\dots,m$ |
| $\rho$, $\mathbf v$, $p$, $E$ | density, velocity, (thermal) pressure, total energy density |
| $e$, $T$ | specific internal energy and temperature |
| $\gamma$ | ratio of specific heats of an ideal gas (adiabatic index) |
| $c_s$ | adiabatic sound speed |
| $\mathbf B$ | magnetic field, in the units of each code as mapped on its Source page (Heaviside–Lorentz unless stated) |
| $c_f$, $c_A$ | fast magnetosonic and Alfvén speeds |

## Mesh and AMR

| Symbol | Meaning |
|---|---|
| $x_i$, $x_{i+1/2}$, $I_i$ | cell centre, cell interface, cell |
| $h$ | uniform cell size; $h_l$ on refinement level $l$ |
| $d$ | number of space dimensions |
| $l$ | refinement level, $l = 0$ the root (coarsest) level |
| $r_{\mathrm{ref}}$ | refinement ratio between consecutive levels ($h_{l+1} = h_l/r_{\mathrm{ref}}$) |
| $N_{\mathrm b}$ | cells per side of a mesh block (patch, tile) |
| $n_{\mathrm g}$ | number of ghost-cell layers |

## Fluxes and time stepping

| Symbol | Meaning |
|---|---|
| $u^-_{i+1/2}$, $u^+_{i+1/2}$ | left and right reconstructed states at an interface |
| $\hat f_{i+1/2}$ | numerical flux at $x_{i+1/2}$ |
| $\mathcal{L}(u)$ | spatial operator of the semi-discretization $\frac{d}{dt}u = \mathcal{L}(u)$ |
| $t^n$, $\Delta t$ | time level and time step; $\Delta t_l$ on level $l$ |
| $\nu$ | Courant (CFL) number |

## Self-gravity

| Symbol | Meaning |
|---|---|
| $\Phi$ | gravitational potential, $\nabla^2\Phi = 4\pi G\rho$ |
| $G$ | gravitational constant |
| $\mathbf g$ | gravitational acceleration, $\mathbf g = -\nabla\Phi$ |

## Radiation (moment methods)

| Symbol | Meaning |
|---|---|
| $c$ | speed of light (the sound speed is $c_s$) |
| $E_{\mathrm r}$, $\mathbf F_{\mathrm r}$, $\mathsf P_{\mathrm r}$ | radiation energy density, flux and pressure tensor |
| $\mathsf f_{\mathrm E}$ | Eddington tensor, $\mathsf P_{\mathrm r} = \mathsf f_{\mathrm E}E_{\mathrm r}$ |
| $\kappa$ | opacity (per unit mass, with subscripts for absorption and scattering) |

## Additions, batch 1 (2026-10-12)

| Symbol | Meaning |
|---|---|
| $P^*$ | total pressure $p + \tfrac12 B^2$ (magnetic field in the units of the registry row for $\mathbf B$) |
| $\mathbf J$ | current density, $\mathbf J = \nabla\times\mathbf B$ |
| $\boldsymbol{\mathcal E}$ | electric field (EMF) of ideal MHD, $\boldsymbol{\mathcal E} = -\mathbf v\times\mathbf B$; in constrained transport its components live on cell edges |
| $\psi$, $c_h$, $c_p$ | GLM cleaning scalar, its propagation speed, and the damping parameter ($\partial_t\psi + c_h^2\nabla\cdot\mathbf B = -(c_h^2/c_p^2)\psi$) |
| $\hat c$, $f_c$ | reduced speed of light used in the radiation time derivatives, and the reduction factor $f_c = \hat c/c$ |
| $f_{\mathrm r}$, $\chi_{\mathrm E}$, $\hat{\mathbf n}$ | reduced flux $\vert\mathbf F_{\mathrm r}\vert/(cE_{\mathrm r})$ (or $\vert\mathbf F_{\mathrm{ph}}\vert/(cN_{\mathrm{ph}})$ in photon-number form), Eddington factor, and flux direction of the M1 closure, $\mathsf f_{\mathrm E} = \tfrac{1-\chi_{\mathrm E}}{2}\mathsf I + \tfrac{3\chi_{\mathrm E}-1}{2}\hat{\mathbf n}\hat{\mathbf n}$ |
| $N_{\mathrm{ph}}$, $\mathbf F_{\mathrm{ph}}$ | photon number density and photon number flux (moments written in photon number rather than energy) |
| $\tau$ (optical depth) | optical depth across a length scale, written $\tau_{\max}$ or $\tau_\lambda$ when the scale matters (the unsubscripted $\tau$ is otherwise the Valencia energy, below) |
| $\mathsf T_{\mathbf g}$, $E_{\mathrm g}$ | gravitational stress tensor $\frac{1}{4\pi G}\left(\nabla\Phi\nabla\Phi - \tfrac12\vert\nabla\Phi\vert^2\mathsf I\right)$, with $\nabla\cdot\mathsf T_{\mathbf g} = -\rho\mathbf g$, and a gravitational energy density |
| $a$ | cosmological scale factor (comoving formulations) |
| $\eta_1$, $\eta_2$ | dual-energy thresholds: select the internal-energy equation where the thermal fraction of the energy is below $\eta_1$, and resynchronize it from the total energy where it exceeds $\eta_2$ |
| $\omega_{\mathrm{SOR}}$ | over-relaxation parameter of a Gauss–Seidel smoother |
| $\hat f^{\rho}_{i+1/2}$ | mass (density) component of the numerical flux at $x_{i+1/2}$ |

## Additions, batch 2 (2026-10-12)

| Symbol | Meaning |
|---|---|
| $\lambda_{\mathrm J}$, $N_{\mathrm J}$ | Jeans length, and cells per Jeans length $N_{\mathrm J} = \lambda_{\mathrm J}/h$ (Truelove's number is $1/N_{\mathrm J}$, written in words because $J$ is the current density) |
| $t_{\mathrm{ff}}$ | free-fall time |
| $\rho_{\mathrm{thr}}$ | sink-formation density threshold |
| $M_{\mathrm s}$, $\mathbf v_{\mathrm s}$ | sink-particle mass and velocity |
| $r_{\mathrm{acc}}$, $r_{\mathrm{soft}}$, $r_K$ | sink accretion radius, gravitational softening radius, accretion-kernel radius |
| $r_{\mathrm B}$, $r_{\mathrm{BH}}$, $\lambda_{\mathrm B}$ | Bondi and Bondi–Hoyle radii, and the Bondi constant (subscripted, so distinct from the eigenvalues $\lambda^{(p)}$) |
| $\dot M$ | mass accretion rate |
| $\infty$ (subscript) | far-field (ambient) state |
| $\Lambda(T)$, $\Lambda_{\mathrm{ref}}$, $T_{\mathrm{ref}}$, $\alpha_{\mathrm c}$ | cooling function (energy per unit volume per unit time per $n_{\mathrm e}n_{\mathrm H}$ or as stated), its reference value and temperature, and a power-law exponent of $\Lambda$ |
| $t_{\mathrm{cool}}$, $Y(T)$ | cooling time, and Townsend's temporal evolution function |
| $n_{\mathrm{tot}}$, $n_i$, $n_{\mathrm e}$, $n_{\mathrm H}$ | total, species, electron and hydrogen number densities (subscripted, so distinct from the time level $n$) |
| $C_i$, $D_i$ | creation and destruction terms of species $i$ in a chemistry network |
| $\Delta t_{\mathrm{sub}}$ | sub-cycle step of a stiff source integration |
| $\mu$, $\mu_{\mathrm e}$, $\mu_{\mathrm H}$, $\mu_Z$ | mean molecular weight and its electron, hydrogen and metal variants (dimensionless; the corresponding mass per particle is $\mu m_{\mathrm H}$) |
| $k_{\mathrm B}$, $m_{\mathrm H}$, $T_{\mathrm{CMB}}$ | Boltzmann constant, hydrogen mass, cosmic-microwave-background temperature |
| $\Gamma_1$ | first (generalized) adiabatic index $\Gamma_1 = \rho c_s^2/p$ (distinct from $\gamma$, which is the ideal-gas constant) |
| $\eta_{\mathrm{tab}}$ | exponent used to tabulate a general EOS |
| $h_{\mathrm{rel}}$ | relativistic specific enthalpy $1 + e + p/\rho$ (the bare $h$ is the cell size) |
| $Y_{\mathrm e}$ | electron fraction |
| $\mu_{\mathrm r}$, $f_{\mathrm m}$, $\Delta_\mu$ | Kastaun's recovery variable $1/(Wh_{\mathrm{rel}})$, the master function whose root it is, and the root tolerance (subscripted, so distinct from $\mu$ and $f$) |
| $M_{\mathrm{BH}}$, $r_{\mathrm g}$ | black-hole mass and gravitational radius $GM_{\mathrm{BH}}/c^2$ |
| $r_{\mathrm{ph}}$, $r_{\mathrm{mb}}$, $r_{\mathrm{ms}}$ | photon-orbit, marginally bound and marginally stable radii |
| $\Phi_{\mathrm N}$, $\Phi_{\mathrm{PW}}$, $\Phi_{\mathrm{NW}}$, $\Phi_{\mathrm G}$ | Newtonian, Paczyński–Wiita, Nowak–Wagoner and Tejeda–Rosswog generalized potentials of a point mass (not solutions of the self-gravity Poisson equation for $\Phi$; $\Phi_{\mathrm G}$ depends on velocity) |
| $r_{\mathrm t}$, $r_{\mathrm p}$ | tidal and pericentre radii |
| $\mathbf F_{\mathrm g}$ | gravitational energy flux of the conservative self-gravity energy equation |
| $N$ | number of cells per dimension of a test grid (resolution); the bare capital, distinct from the subscripted $N_{\mathrm b}$, $N_{\mathrm J}$, $N_{\mathrm{ph}}$ |

## Additions, batch 3 (2026-10-12)

| Symbol | Meaning |
|---|---|
| $a_{\mathrm r}$ | radiation constant, $E_{\mathrm r} = a_{\mathrm r}T^4$ in equilibrium |
| $\kappa_{\mathrm P}$, $\kappa_{\mathrm E}$, $\kappa_{\mathrm F}$, $\kappa_{\mathrm R}$ | Planck-mean, energy-mean, flux-mean and Rosseland-mean opacities (subscripted forms of the registry $\kappa$) |
| $\Delta t_{\mathrm{hyp}}$, $\Delta t_{\mathrm{par}}$ | time-step limits of the hyperbolic (advective) and parabolic (diffusive) terms |
| $s_{\mathrm{RKL}}$ | number of stages of a Runge–Kutta–Legendre super-time-step |

## Relativistic (magneto)hydrodynamics

| Symbol | Meaning |
|---|---|
| $W$ | Lorentz factor |
| $\alpha_{\mathrm L}$, $\beta^i$, $\gamma_{ij}$ | lapse, shift and spatial metric of the 3+1 split (the indexed $\gamma_{ij}$ is distinct from the adiabatic index $\gamma$) |
| $D$, $S_i$, $\tau$ | conserved density, momentum and energy of the Valencia formulation |
