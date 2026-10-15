---
type: Definition
title: "Notation registry"
description: "Normative symbol registry — every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-10-14T00:00:00Z
---

# Notation registry

Every concept page of this bundle writes mathematics in the symbols below.
A source's own symbols are translated on its Source page (`# Notation map`).
The registry was seeded on 2026-10-14 from the conventions that dominate
the field's literature (SI units, freestream subscript $\infty$, total
quantities subscript $0$). Subscripts name stations and qualifiers: $\infty$ freestream, $1$ and $2$
upstream and downstream of a shock or interaction, $\max$ peak value,
$\mathrm{ref}$ an undisturbed reference value, $j$ a jet (e.g. $q_{w,\max}$,
$p_2/p_1$, $p_{0,j}$). Extend this registry, and log the extension,
before writing a symbol it lacks.

## 1. Flow variables

| Symbol | Meaning | Note |
|---|---|---|
| $\rho$, $\mathbf u$, $p$, $T$ | density, velocity, pressure, temperature |  |
| $u$, $v$, $w$ | velocity components along $x$, $y$, $z$ |  |
| $\gamma$ | ratio of specific heats |  |
| $R$ | specific gas constant |  |
| $a$ | speed of sound |  |
| $h$, $h_0$ | specific and total enthalpy |  |
| $p_0$, $T_0$ | total (stagnation) pressure and temperature | subscript $\infty$ freestream |
| $\mu$, $k$ | dynamic viscosity, thermal conductivity |  |

## 2. Dimensionless groups

| Symbol | Meaning | Note |
|---|---|---|
| $\mathrm{Ma}$ | Mach number | $\mathrm{Ma}_\infty$ freestream |
| $\mathrm{Re}$ | Reynolds number (length scale stated) |  |
| $\mathrm{Pr}$ | Prandtl number |  |
| $\mathrm{St}$ | Stanton number |  |
| $C_f$, $C_p$ | skin-friction and pressure coefficients |  |
| $C_L$, $C_D$, $C_m$ | lift, drag and pitching-moment coefficients |  |
| $L/D$ | lift-to-drag ratio |  |

## 3. Boundary layers, shocks, heat flux

| Symbol | Meaning | Note |
|---|---|---|
| $\delta$ | boundary-layer thickness |  |
| $\tau_w$ | wall shear stress |  |
| $q_w$ | wall heat flux |  |
| $T_w$ | wall temperature |  |
| $\beta_s$ | shock angle | never the ratio of specific heats |
| $\theta_w$ | wedge or ramp (deflection) angle |  |
| $\sigma_0$ | total-pressure recovery coefficient, $p_{0,\mathrm{out}}/p_{0,\infty}$ |  |

## 4. Coordinates and numerics

| Symbol | Meaning | Note |
|---|---|---|
| $x$, $y$, $z$ | Cartesian coordinates; $x$ streamwise unless stated |  |
| $t$ | time |  |
| $\Delta x$, $\Delta t$ | grid spacing, time step |  |
| $y^+$ | wall distance in viscous units |  |

## 5. Configuration and performance quantities

| Symbol | Meaning | Note |
|---|---|---|
| $\alpha$ | angle of attack | |
| $J$ | jet-to-crossflow momentum flux ratio, $(\rho u^2)_j/(\rho u^2)_\infty$ | |
| $d_j$ | jet orifice diameter | |
| $L_{\mathrm{sep}}$ | separation length | location stated per page |
| $p_b$ | back pressure imposed at an inlet or isolator exit | $p_b/p_\infty$ the back-pressure ratio |
| $\varphi$ | mass capture ratio of an inlet, $\dot m_{\mathrm{capt}}/\dot m_\infty$ through the capture area | other normalisations are stated per page |
| $\mathrm{CR}$ | inlet contraction ratio (capture to throat area) | internal ratio $\mathrm{CR}_i$ |
| $\eta_V$ | volumetric efficiency of a lifting body, $V^{2/3}/S_{\mathrm{wet}}$ | $V$ volume, $S_{\mathrm{wet}}$ wetted area |
| $Q$ | integrated heat load on a surface | |
| $\mathrm{Kn}$ | Knudsen number | |
| $\beta_B$ | ballistic coefficient, $m/(C_DS)$ | $m$ mass, $S$ reference area |
| $ZT$ | thermoelectric figure of merit | |

## 6. Uncertainty quantification

| Symbol | Meaning | Note |
|---|---|---|
| $\boldsymbol\xi$ | vector of uncertain inputs | |
| $\Psi_k$ | orthogonal polynomial basis functions of a polynomial-chaos expansion | |
| $S_j$, $S_{T,j}$ | first-order and total Sobol' indices of input $j$ | |
