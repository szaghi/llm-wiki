---
type: Definition
title: "Rotating spoke"
description: "A large-scale, kHz, centimetre-wavelength azimuthal structure rotating at a fraction of the E x B drift in Hall thrusters and other E x B discharges, classed as a coherent structure of the discharge and studied with 3D PIC and 2D axial–azimuthal hybrid models."
status: established
aliases: [spoke, rotating spokes, m = 1 rotating structure]
tags: [instability, oscillation, hall-thruster, pic]
timestamp: 2026-10-14T00:00:00Z
---

# Rotating spoke

A rotating spoke is a large-scale azimuthal structure of the discharge that
rotates in the $\mathbf E\times\mathbf B$ direction at a speed well below the
electron drift. It occurs in Hall thrusters and in other
$\mathbf E\times\mathbf B$ discharges.

* **Class.** The 2017 Plasma Roadmap classes rotating spokes in
  $\mathbf E\times\mathbf B$ discharges (Hall thrusters, magnetrons, Penning
  discharges, magnetic filters) as large-scale self-organized coherent
  structures, citing Skiff & Wurtele (2016) and Boeuf (2014). It reproduces
  an experimental image of a spoke in a Hall thruster (Ellison, Raitses &
  Fisch 2012) and a PIC simulation of a spoke in a magnetron
  ([Adamovich et al. (2017)](/sources/adamovich-2017.md), §16, Fig. 30b–c).
* **Scales.** kHz frequency, centimetre wavelength, phase velocity about
  $0.2\,E_z/B_r$, located near the anode or near the plume
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.5,
  attributed to Ellison et al. 2012). The spoke is thus distinct from the
  MHz, millimetre [electron drift instability](/definitions/electron-drift-instability.md)
  and from the axial [breathing mode](/definitions/breathing-mode.md).
* **Operating regime.** In the low-voltage regime of the SPT-100 current–
  voltage characteristic, with BN–SiO₂ walls, a stable rotating structure
  of azimuthal mode number 1 is observed; a 2D axial–azimuthal hybrid model
  gives a 40 kHz rotating instability of mode numbers 1 and 2 at 100 V
  (Taccogna & Garrigues 2019, §2.6, attributed to Sekerak 2015, Mazouffre
  2017 and Lam et al. 2015).
* **Simulation.** Spokes have been studied with 3D PIC (Taccogna &
  Garrigues 2019, §3.5, citing Tang et al. 2012 and Matyash 2017; the
  Tang et al. entry is missing from the review's reference list).
  [Taccogna et al. (2023)](/sources/taccogna-2023.md) (Conclusions) list
  spokes among the instabilities that particle models of Hall thrusters
  must address, with the ECDI, the MTSI, the ion transit-time and the
  gradient-drift instabilities.
* **Theory.** The Roadmap recommends studying instability onset with
  kinetic or PIC simulations in reduced domains and importing turbulence
  methods from fusion research (Adamovich et al. 2017, §16).

# Citations

1. [Adamovich et al. (2017)](/sources/adamovich-2017.md), §16, Fig. 30.
2. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §§2.6, 3.5 (accepted manuscript).
3. [Taccogna et al. (2023)](/sources/taccogna-2023.md), Conclusions (accepted manuscript).
