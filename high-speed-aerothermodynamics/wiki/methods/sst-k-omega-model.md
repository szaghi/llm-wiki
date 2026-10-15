---
type: Method
title: "SST k–ω turbulence model in high-speed flow"
description: "Menter's two-equation shear-stress-transport model is the RANS closure of four of the bundle's inlet, isolator, aeroheating and waverider studies, once with a compressibility correction, and is validated in them only against wall pressure."
status: established
aliases: [SST, Menter SST, k-omega SST, shear-stress transport model]
tags: [turbulence-model, rans, numerics, inlet, isolator, aeroheating]
timestamp: 2026-10-14T00:00:00Z
---

# SST k–ω turbulence model in high-speed flow

The shear-stress-transport (SST) model of Menter (1994) is a two-equation
RANS closure that solves transport equations for the turbulent kinetic
energy and the specific dissipation rate, with two sets of model
constants (a k–ω set and a k–ε set) and an eddy-viscosity limiter. This
page records the forms and constants the
sources print and how they use and test the model; the transport
equations themselves are given in
[Liu H. et al. (2018)](/sources/liu-2018-d.md), Eqs. 7–12, and
[Moradi et al. (2018)](/sources/moradi-2018.md), Eqs. 1–11.

## Constants as printed

[Liu H. et al. (2018)](/sources/liu-2018-d.md), §2, Eqs. 7–12:

| Constant | Set 1 | Set 2 |
|---|---|---|
| diffusion coefficient of turbulent kinetic energy | 0.85 | 1.0 |
| diffusion coefficient of specific dissipation rate | 0.5 | 0.856 |
| destruction coefficient | 0.075 | 0.0828 |
| production coefficient of the dissipation-rate equation | 0.5332 | 0.4403 |

The eddy-viscosity limiter constant is 0.31, and the production of
turbulent kinetic energy is written with the vorticity magnitude (eddy
viscosity times vorticity squared). Laminar viscosity follows Sutherland's
law, with $\mathrm{Pr}=0.72$ and turbulent Prandtl number 0.9 (§2). The
paper cites Shur et al. (2008), a DDES/WMLES paper, alongside Menter (1994)
for the model.

## Compressibility correction

[Moradi et al. (2018)](/sources/moradi-2018.md), §2.3, Eqs. 3–11, add a
dilatation-dissipation correction: the destruction coefficients of both
equations are modified by a function of the turbulent Mach number (the
square root of twice the turbulent kinetic energy over $a^2$). The
function is zero below a threshold turbulent Mach number of 0.25 and
equals the difference of the squares of the turbulent and threshold
turbulent Mach numbers above it, with a multiplier of 1.5; the production
of turbulent kinetic energy is limited to 10 times its destruction term.
The paper presents this as the standard formulation, restated.

## Use in the sources

| Source | Flow | Numerics | Validation shown |
|---|---|---|---|
| [Liu H. et al. (2018)](/sources/liu-2018-d.md), §2, §4 | two-ramp hypersonic inlet and isolator, $\mathrm{Ma}_\infty=5.9$; 3-D RANS on a spanwise-periodic slab | unnamed in-house finite-volume code, Roe flux-difference splitting with second-order MUSCL, central viscous fluxes, implicit LU-SGS, CFL 3.0, 30000 steps; isothermal walls | DLR GK-01 inlet at $\mathrm{Ma}_\infty=7.0$: wall $C_p$ within a ±5.6% experimental band (graphical, no error norm); Li et al. shock-tunnel inlet: cowl-wall pressure agrees except slightly downstream in the isolator |
| [Meng et al. (2018)](/sources/meng-2018.md), §3 | curved isolators, entrance Mach 2 | unnamed code, second-order upwind Roe, implicit, 5000 steps | Kawatsu et al. back-pressured duct at Mach 2.3: wall pressure overpredicted upstream of the shock train by up to 52%, shock-train leading edge reproduced, minimum deviation 1.3% inside the shock train |
| [Moradi et al. (2018)](/sources/moradi-2018.md), §2.3 | spike with aerodome and coolant jets ahead of a blunt nose, $\mathrm{Ma}_\infty=5$ | in-house implicit cell-centred finite volume, Roe, second-order upwind, with the compressibility correction | none in the paper; agreement with experiment stated for earlier papers of the authors |
| [Zhao et al. (2018)](/sources/zhao-2018.md), §4 | osculating-cone waveriders, Mach 3–10 at 25 km | ANSYS Fluent, coupled implicit, second-order upwind, ideal gas, half domain | none; the viscous shock is deflected downward from the inviscid design location by the boundary layer |

Other closures in the same sources: the standard k–ε model with wall
functions ($y^+\approx30$–60) in a Mach-4 inward-turning intake
([Zuo & Huang (2018)](/sources/zuo-2018.md), §3.1.2), and the RNG k–ε
model with second-order AUSM in Fluent for waveriders
([Wang et al. (2018)](/sources/wang-2018-d.md), §3). No source compares SST
with another closure on the same case. The wall-pressure validations above
do not test heat flux or separation length, and the one stringent
comparison (the back-pressured duct) shows a 52% pressure deviation ahead
of the shock train.

Related pages: [Inlet start, unstart and hysteresis](/definitions/inlet-start-and-unstart.md),
[Isolator and shock train](/definitions/isolator-shock-train.md),
[Aeroheating reduction by spikes and coolant jets](/methods/aeroheating-reduction-spikes-and-jets.md).

# Citations

1. [Liu H. et al. (2018)](/sources/liu-2018-d.md), §2 (Eqs. 7–12), §4.1–4.3 (Figs. 3–7, Table 1).
2. [Meng et al. (2018)](/sources/meng-2018.md), §3 (Fig. 7, Table 3).
3. [Moradi et al. (2018)](/sources/moradi-2018.md), §2.3 (Eqs. 1–11), §3.
4. [Zhao et al. (2018)](/sources/zhao-2018.md), §4 (Figs. 9–11).
5. [Zuo & Huang (2018)](/sources/zuo-2018.md), §3.1.2.
6. [Wang et al. (2018)](/sources/wang-2018-d.md), §3.
