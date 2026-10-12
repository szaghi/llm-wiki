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

## Relativistic (magneto)hydrodynamics

| Symbol | Meaning |
|---|---|
| $W$ | Lorentz factor |
| $\alpha_{\mathrm L}$, $\beta^i$, $\gamma_{ij}$ | lapse, shift and spatial metric of the 3+1 split (the indexed $\gamma_{ij}$ is distinct from the adiabatic index $\gamma$) |
| $D$, $S_i$, $\tau$ | conserved density, momentum and energy of the Valencia formulation |
