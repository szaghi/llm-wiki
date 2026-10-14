---
type: Software
title: "EX-PWS"
description: "Beihang University's three-dimensional hybrid PIC-DSMC plume code on unstructured tetrahedral grids, with macroparticle heavy species, isothermal Boltzmann electrons, untracked background gas and Maxwell-reflection surfaces, validated on ion-thruster plume force against a torsional micro-thrust balance."
status: established
aliases: [Extension of Plume Work Station, EX-PWS code]
tags: [software, hybrid, dsmc, pic, plume, ion-thruster]
timestamp: 2026-10-14T00:00:00Z
---

# EX-PWS

EX-PWS ("Extension of Plume Work Station") is the plume code of Beihang
University used by [Cai et al. (2018)](/sources/cai-2018.md). Language,
licence and run times are not stated; the domain is split into "several
parallel partitions" (§2.3).

## Model

* **Species and collisions.** Xe, Xe$^+$, Xe$^{2+}$ and single and double
  [charge-exchange ions](/definitions/charge-exchange-ions.md) are
  macroparticles. Elastic collisions (Xe–Xe, Xe$^+$–Xe, Xe$^{2+}$–Xe,
  CEX$^+$–Xe) and single and double charge exchange are computed by
  [DSMC](/methods/dsmc.md), with cross sections from an earlier paper of
  the group (§2.1, eqs. 1–6). Triply and more highly charged ions are
  neglected, stated without demonstration to have no effect on accuracy.
* **Background gas.** Facility gas is represented by temporary neutrals
  created in every cell at every iteration, at the uniform static facility
  temperature and pressure, and not tracked; in a collision only the
  simulated particle's velocity changes (§2.1). Background pressure is
  $2\times10^{-3}$ Pa in the force cases and zero in the vacuum study.
* **Electrons.** Collisionless, unmagnetized, isothermal and quasi-neutral,
  following the [Boltzmann relation](/methods/boltzmann-electron-model.md)
  with reference density $1\times10^{16}$ m$^{-3}$ at $\phi=0$ and
  $T_e=3.5$ eV (§2.1, eqs. 7–9). No Poisson equation is solved; the
  magnetic field is neglected. This is a
  [hybrid PIC–fluid model](/methods/hybrid-pic-fluid-model.md).
* **Surfaces.** Maxwell reflection with species-dependent normal and
  tangential accommodation coefficients (Corey et al. formula), sticking
  coefficient 0 as baseline, ions neutralized on impact, Yamamura
  sputtering, sheaths ignored; the force on a surface is the sum of
  incident, reflected and sputtered momentum fluxes (§2.2, eqs. 10–15,
  Tables 1–2). See [gas–surface interaction models](/methods/gas-surface-interaction.md).
* **Grid and step.** 3D unstructured tetrahedral grid; cells larger than
  $\lambda_D$ (about $10^{-5}$ m) and of order $\lambda_{\mathrm{mfp}}$
  (about 0.1 m); about 2 million cells (1, 2, 4 million tested);
  $\Delta t=1\times10^{-7}$ s; $W=2\times10^8$; particles per cell not
  stated (§2.3, Fig. 2).

## Validation

The LIPS-200 xenon ion thruster (200 mm diameter, thrust $40\pm4$ mN,
$I_{sp}$ $3000\pm300$ s) fires at a 300 mm aluminium plate in Beihang's
PES vacuum chamber (5.2 m diameter, 12.6 m long, about $2\times10^{-3}$ Pa
during operation). A torsional micro-thrust balance with 1.45% measurement
error measures the axial plume force. Over plate distances of 0.6–1.0 m the
simulated force is generally higher than the measured one, with a maximum
relative error of 16.36% (§3, §4.1, Fig. 4). The inflow beam model was
validated against Faraday probes in the group's earlier paper (§2.1).

# Citations

1. [Cai et al. (2018)](/sources/cai-2018.md), §2.1–2.3, eqs. 1–15, Tables 1–2, §3, §4.1, Figs. 2, 4.
