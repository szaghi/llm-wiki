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

## Relativistic (magneto)hydrodynamics

| Symbol | Meaning |
|---|---|
| $W$ | Lorentz factor |
| $\alpha_{\mathrm L}$, $\beta^i$, $\gamma_{ij}$ | lapse, shift and spatial metric of the 3+1 split (the indexed $\gamma_{ij}$ is distinct from the adiabatic index $\gamma$) |
| $D$, $S_i$, $\tau$ | conserved density, momentum and energy of the Valencia formulation |
