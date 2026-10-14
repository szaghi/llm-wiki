---
type: Software
title: "HYPHEN"
description: "Axisymmetric hybrid code of the UC3M EP2 group that couples a particle model of the heavy species with a drift-diffusion electron fluid on a magnetic-field-aligned mesh, applied to magnetically shielded Hall thrusters and electron-cyclotron-resonance thrusters."
status: established
aliases: [HYPHEN code]
tags: [software, hybrid, pic, fluid, hall-thruster, magnetic-nozzle, anomalous-transport]
timestamp: 2026-10-14T00:00:00Z
---

# HYPHEN

HYPHEN is the axisymmetric $(z,r)$ hybrid code of the Equipo de Propulsión
Espacial y Plasmas (UC3M) for Hall-effect and electrodeless thrusters. Its
heavy species are particles (PIC); its electrons are the slow-dynamics
[electron fluid model](/methods/electron-fluid-model.md) on a
[magnetic-field-aligned mesh](/methods/magnetic-field-aligned-mesh.md)
([Ahedo (2023)](/sources/ahedo-2023.md), §3, refs. 30, 36). It is an
instance of the [hybrid PIC–fluid model](/methods/hybrid-pic-fluid-model.md).
Language, parallelization, discretization and run times are not given in the
source.

## Electron model

* Parallel and perpendicular derivatives of the electron equations are
  computed directly on the field-aligned mesh to avoid numerical diffusion
  ([Ahedo (2023)](/sources/ahedo-2023.md), eq. 36).
* Anomalous transport by Bohm-type terms, either the isotropic model of
  ref. 30 or the model of ref. 36 acting only on the azimuthal equations
  (eqs. 18–21, 26); see
  [anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md).
* An azimuthal electron velocity limiter, the smaller of the effective Hall
  parameter times minus the axial electron velocity and twice the electron
  thermal speed, motivated by a 1D axial fluid model with electron inertia
  (p. 14; see [five-moment electron fluid model](/methods/five-moment-fluid-model.md)).
* For the ECR thruster, a cold-plasma-dielectric Maxwell solver supplies the
  wave power absorbed by the electrons (ref. 35).

## Runs shown in Ahedo (2023)

* **Magnetically shielded Hall thruster** (Fig. 1). The mesh has a singular
  null-field point inside the channel. Time-averaged maps of $n_e$, $T_e$
  (colour scale to 40 eV), $\phi$ (colour scale from −50 to about 300 V) and
  the electron and ion currents. The cathode current splits into a
  plume-neutralizing beam and a beam entering the channel; lines around the
  null point shield the walls from the current; magnetic lines are
  near-isothermal and the [thermalized potential](/definitions/thermalized-potential.md)
  varies little along them, while isopotentials are not aligned with them. See
  [magnetic shielding](/definitions/magnetic-shielding.md).
* **Plume boundary conditions** (Fig. 6, eq. 63). With a local zero-current
  condition, plume current loops depend strongly on plume size; a global
  current-free condition with a metallic surrounding wall is "more robust",
  and the main discharge is only slightly affected by the choice.
* **ECR thruster** (Fig. 2). Absorbed power density $10^5$–$10^9$ W m$^{-3}$,
  deposited around the resonance surface and the central rod; $T_e$ (colour
  scale to about 40 eV) nearly constant along lines, which the review ascribes
  to the large parallel conductivity; with a plume domain of 3–4
  channel widths there is "practically no cooling along the magnetic lines"
  (p. 21; see [polytropic electron closure](/definitions/polytropic-electron-closure.md)).

All values are read from figures in a review and are approximate; the review
gives no quantitative comparison with experiment for these runs
([Ahedo (2023)](/sources/ahedo-2023.md), Figs. 1, 2, 6).

# Citations

1. [Ahedo (2023)](/sources/ahedo-2023.md), §3, eqs. 18–21, 26, 36, 63, Figs. 1, 2, 6, pp. 14, 21.
