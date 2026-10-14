---
type: Method
title: "Laser-ablation plume model"
description: "Coupled model of nanosecond laser ablation of a metal target (enthalpy heat conduction with vaporization, phase explosion and plume shielding) and of the ablation plume as a 2D axisymmetric multi-species Euler flow with finite-rate ionization and inverse-bremsstrahlung absorption, applied to the first stage of a laser ablation plasma thruster."
status: established
aliases: [laser ablation plume model, ablation plume hydrodynamics, LA-PPT plume model]
tags: [pulsed-plasma-thruster, fluid, plume, verification]
timestamp: 2026-10-14T00:00:00Z
---

# Laser-ablation plume model

[Zhang et al. (2018)](/sources/zhang-2018.md) model the first stage of a
[laser ablation plasma thruster](/definitions/pulsed-plasma-thruster.md):
a nanosecond Nd:YAG pulse ablates an aluminium target inside a ceramic
tube, and the plume expands and ionizes in the tube. The electromagnetic
acceleration stage is not modelled. They argue that a 2D model is needed
because the tube wall confines the radial expansion, whereas most earlier
hydrodynamic ablation-plume models are 1D (§1). The equations below are
stated in words; the paper's own symbols are translated on the
[Source page](/sources/zhang-2018.md).

## Target model

* **Heat conduction** in volumetric-enthalpy form in $(z,r)$, with
  temperature-dependent density, conductivity, reflectivity and absorption,
  a surface-recession advection term and the laser source (§2.1, Eq. 1).
  Melting is handled through the enthalpy, and the moving surface by a
  coordinate mapping onto a fixed domain (Eqs. 9–11). The rear and side
  boundaries are insulated; at the ablation surface the conducted heat
  balances the latent heat carried by the receding surface (Eq. 12).
* **Vaporization** by the Hertz–Knudsen rate with a Clausius–Clapeyron
  saturation pressure, with coefficient 0.82, reference pressure
  $1.01325\times10^5$ Pa and atom mass $4.48\times10^{-26}$ kg (Eq. 2).
* **Phase explosion** by homogeneous nucleation above 0.8 of the critical
  temperature, strong near 0.9 of it, from a critical bubble radius and a
  nucleation rate (Eqs. 3–5); the superheated liquid is taken at 0.85 of the
  critical temperature. Surface recession speed is the sum of the
  vaporization and explosion mass rates over the density (Eq. 6).
* **Laser deposition** by Beer–Lambert absorption with surface and
  dielectric-transition reflectivities (the target becomes dielectric near
  the critical temperature), and plume shielding of the incident intensity
  by the optical depth of the plume (Eqs. 7–8).

## Plume model

* 2D axisymmetric inviscid Euler equations with species continuity for Al,
  Al$^+$, Al$^{2+}$, Al$^{3+}$ and electrons, a geometric source term and
  mass sources from ionization (§2.2, Eq. 13). The energy includes
  electronic excitation through partition sums (Eqs. 14–15); $T_e$ equals
  the heavy-species temperature; the plasma is quasi-neutral (Eq. 19).
* **Ionization** Al → Al$^+$ → Al$^{2+}$ → Al$^{3+}$ by electron impact at
  finite rate, with forward rates from a reference-cross-section expression
  (reference diameter $2\times10^{-10}$ m) and backward rates from Saha-type
  equilibrium constants with partition functions (Eqs. 17–23). Ionization
  energies 5.98577, 18.82856 and 28.44765 eV (Table 3).
* **Absorption** of the laser in the plume by inverse bremsstrahlung,
  electron–neutral plus electron–ion with charge-squared weights 1, 4, 9
  (Eq. 24).
* No electric or magnetic field is solved, and there is no kinetic species,
  no sheath and no secondary electron emission.

## Numerics and coupling

* Explicit finite differences for the heat equation; AUSM+-up for the
  Euler equations; stated second order in space and time. Target and plume
  are solved together and coupled every time step (§2.3, §3.2).
* Grid $100\times200$ in the target and $100\times200$ in the plume,
  $\Delta t=1\times10^{-12}$ s; target 6 mm in diameter and 5 µm thick; tube
  10 mm long; ambient pressure $5.0\times10^{-3}$ Pa; no-slip at the tube
  wall (§2.3, §3.2). Grids of $1\times10^4$, $2\times10^4$ and
  $4\times10^4$ cells and time steps of $5\times10^{-13}$–$5\times10^{-12}$ s
  were compared (Figs. 4–5).
* An a-priori error-accumulation estimate (after Smirnov et al.) bounds the
  summed discretization error of 30 ns runs by 5%; all cases give
  0.387–1.225% (Eqs. 25–27, Table 5). Code name, language and parallelism
  are not stated.

## Validation and results

* Against the experiments of Porneala & Willis (1064 nm, 5 ns FWHM,
  160 µm spot, atmospheric conditions): the computed ablation threshold is
  about $5\times10^4$ J/m$^2$ against $5.2\times10^4$ J/m$^2$ measured
  (printed as 5 and 5.2 J/cm$^2$), and plume fronts agree with
  shadowgraphs; the comparison is graphical, with no error metric, and the
  model has no ambient-gas dynamics, so it shows no shock (§3.1, Fig. 3).
* At $10^5$ J/m$^2$ (printed as 10 J/cm$^2$), the target surface passes the boiling point at 3 ns and is
  held at 0.9 of the critical temperature by phase explosion from 4 to
  10.5 ns; ablation ends at 20 ns (§3.3, Fig. 6).
* The tube wall converts radial to axial velocity and heats the plume near
  the wall to about 25000 K at 100 ns, with secondary and tertiary
  ionization there; on the axis only single ionization occurs (§3.4,
  Figs. 9–12).
* Over $5\times10^4$–$3\times10^5$ J/m$^2$ (printed as 5–30 J/cm$^2$) the impulse bit grows from 13 to 16 µN·s and the
  ablated mass from 0.15 to 0.9 µg; the authors conclude that at higher
  fluence more of the laser energy goes to ablating mass than to plume
  energy (§3.5, Figs. 13–15). How thrust is computed from the plume
  solution is not stated.

# Citations

1. [Zhang et al. (2018)](/sources/zhang-2018.md), §1, §2.1–2.3, Eqs. 1–27, Tables 3, 5, §3.1–3.5, Figs. 3–15.
