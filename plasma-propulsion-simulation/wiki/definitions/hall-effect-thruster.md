---
type: Definition
title: "Hall-effect thruster"
description: "A gridless electrostatic thruster in which a mainly radial magnetic field across an annular channel impedes the cathode electrons' axial motion, so that an axial electric field accelerates unmagnetized ions; built as the stationary plasma thruster (SPT, ceramic walls, long channel) or the anode-layer thruster (TAL, metallic walls, short channel), and the main simulation target of this bundle."
status: established
aliases: [Hall thruster, HET, HT, stationary plasma thruster, SPT, anode layer thruster, thruster with anode layer, TAL, E×B thruster]
tags: [hall-thruster]
timestamp: 2026-10-15T00:00:00Z
---

# Hall-effect thruster

## Principle

A Hall thruster "is essentially a grid-less electrostatic acceleration
device": gas propellant, usually xenon or krypton, flows through holes in
an anode into an annular acceleration channel; an external hollow cathode
supplies electrons; and an applied, mainly radial magnetic field partly
traps the electrons in the channel, concentrating the ionization zone. A
potential difference of several hundred volts between anode and cathode
accelerates the ions out of the channel
([Boyd (2005)](/sources/boyd-2005.md), §3.4, Fig. 13). For a kW-class
thruster [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §1,
give a discharge current of about 4 A, of which about 20 % of the cathode
current enters the channel, a field of about 0.01 T (printed as 100 G) chosen to magnetize
electrons but not ions, about 90 % of the injected neutral flux ionized,
and BN-SiO$_2$ walls; the axial field penetrates the plasma because the
cross-field conductivity drops (attributed to Boeuf 2017). The electrons
drift azimuthally in $\mathbf E\times\mathbf B$; their axial transport is
set by the [cross-field mobility](/definitions/electron-mobility-and-hall-parameter.md),
which in real thrusters exceeds its classical value
([anomalous electron transport](/definitions/anomalous-electron-transport.md)).

## Configurations

[Boyd (2005)](/sources/boyd-2005.md), §3.4, distinguishes two:
* the **stationary plasma thruster (SPT)**, with a relatively long
  channel (a few centimetres) and ceramic insulator walls (e.g. boron
  nitride or silicon carbide); the [SPT-100](/benchmarks/spt-100.md) is
  the reference device of many simulations;
* the **anode-layer thruster (TAL)**, with a shorter channel (a few
  millimetres) and metallic walls (e.g. molybdenum).

"Almost all numerical modeling studies of Hall thrusters have considered
the SPT configuration". The TAL models Boyd cites are a multi-fluid model
of a bismuth TAL with good current–voltage agreement (Keidar & Boyd) and
a fully kinetic PIC model of a 50 W micro-TAL (Szabo & Martinez-Sanchez).

Variants named in [Adamovich et al. (2017)](/sources/adamovich-2017.md),
§12: the [magnetically shielded](/definitions/magnetic-shielding.md)
thruster, the wall-less configuration, and the nested-channel thruster
(the 10 kW-class two-channel X2 on xenon, Fig. 22), which in
magnetic-shielding configuration "was validated at 20 kW", with research
aiming above 100 kW.

## Operating range

| Quantity | Value | Source |
|---|---|---|
| thrust | 0.01–1000 mN | [Boyd (2005)](/sources/boyd-2005.md), Table 1 |
| | a few mN to 1 N | [Gallo et al. (2021)](/sources/gallo-2021.md), §1 |
| $I_{sp}$ | 1500–6000 s | [Boyd (2005)](/sources/boyd-2005.md), Table 1 |
| | 1500–2500 s typical, at overall efficiency of about 50–60 % | [Boyd (2005)](/sources/boyd-2005.md), §3.4 |
| | 1000–3000 s | [Gallo et al. (2021)](/sources/gallo-2021.md), §1 |
| power | 100 W–20 kW | [Gallo et al. (2021)](/sources/gallo-2021.md), §1 |
| plasma density | $10^{18}$–$10^{19}$ m$^{-3}$ ("kinetic" regime) | [Boyd (2005)](/sources/boyd-2005.md), Table 1 |
| | about $10^{17}$ m$^{-3}$ (SPT-100) | [Boyd (2005)](/sources/boyd-2005.md), §3.4 |

The tabulated ranges are typical-value statements, not measurements, and
they differ: Gallo et al.'s lower bound on $I_{sp}$ is below Boyd's, and
Boyd's table extends higher than his own text; his §3.4 SPT-100 density
also lies an order of magnitude below his own Table 1 range. Boyd's Table 1
gives no sources. Compared with gridded ion engines, Hall thrusters give a larger
thrust-to-power ratio, and the two are "the most advanced" electric
propulsion technologies ([Adamovich et al. (2017)](/sources/adamovich-2017.md),
§12, citing the 2012 Roadmap). As of May 2005, 14 operational spacecraft used Hall thrusters, for
station keeping ([Boyd (2005)](/sources/boyd-2005.md), §3.4). Alternative
propellants to xenon are a stated need
([Adamovich et al. (2017)](/sources/adamovich-2017.md), §12); water and
oxygen are simulated in [Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md).

## Loss mechanisms

[Boyd (2005)](/sources/boyd-2005.md), §3.4: ions striking the walls
recombine into slow neutrals that add no thrust; energetic ion impacts
sputter the walls, one of the primary lifetime limits; and the plume
diverges more than that of an ion thruster, owing to the leaking magnetic
field and the higher $T_e$.

## What models must capture

* **Species treatment.** In the SPT-100 the electrons are magnetized and
  the ions are not, so electrons may be modelled as a fluid while ions and
  neutrals need a kinetic description
  ([Boyd (2005)](/sources/boyd-2005.md), §3.4); see
  [hybrid PIC–fluid models](/methods/hybrid-pic-fluid-model.md) and
  [PIC-MCC](/methods/pic-mcc.md).
* **Anisotropy.** In the acceleration region, Ahedo estimates the ratio of
  parallel to perpendicular potential gradients at about 1/10 and of the
  in-plane perpendicular to azimuthal electron current at about 1/100
  (eq. 25), and parallel and perpendicular gradients differ by a factor
  of the order of the product of the classical and effective Hall
  parameters, "say $O(10^5)$ in conventional HETs" (eqs. 33–35), which motivates
  the [thermalized potential](/definitions/thermalized-potential.md) and
  [field-aligned meshes](/methods/magnetic-field-aligned-mesh.md)
  ([Ahedo (2023)](/sources/ahedo-2023.md)).
* **Electron transport.** The accuracy of fluid and hybrid models "depends
  heavily" on the electron mobility; Boyd bounds their prediction of
  thrust and power at about 10 % and ranks Hall thrusters with arcjets and
  pulsed plasma thrusters at 10–20 % accuracy, against about 5 % for
  resisto-jets and ion thrusters ([Boyd (2005)](/sources/boyd-2005.md),
  §§3.4, 4). [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md),
  §3.3, report that 2D $r$–$z$ PIC models with a fitted Bohm-type
  collision predict global performance within 20 % in thrust and
  discharge current.
* **Oscillations.** The [breathing mode](/definitions/breathing-mode.md),
  the [electron drift instability](/definitions/electron-drift-instability.md)
  and the [rotating spoke](/definitions/rotating-spoke.md).
* **Walls.** [Secondary electron emission](/definitions/secondary-electron-emission.md),
  [near-wall conductivity](/definitions/near-wall-conductivity.md) and
  erosion, for which [Adamovich et al. (2017)](/sources/adamovich-2017.md),
  §12, call for accurate secondary-emission and sputtering-yield data.
* **Facility effects.** Background pressure enters a coupled thruster
  model through the cathode coupling voltage, neutral ingestion, the
  location of the anomalous-transport transition and the plume divergence
  ([Eckels et al. (2024)](/sources/eckels-2024.md), eqs. 3–7);
  [Adamovich et al. (2017)](/sources/adamovich-2017.md), §12, call
  ground-test facility effects critical.
* **Research priorities (2017).** Electron transport, turbulence and
  confinement come first, and "The development of powerful 3D codes with
  predictive capabilities has become a necessity"
  ([Adamovich et al. (2017)](/sources/adamovich-2017.md), §12).

# Citations

1. [Boyd (2005)](/sources/boyd-2005.md), §§3.4, 4, Table 1, Fig. 13.
2. [Adamovich et al. (2017)](/sources/adamovich-2017.md), §12, Fig. 22.
3. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §§1, 3.3 (accepted manuscript).
4. [Gallo et al. (2021)](/sources/gallo-2021.md), §1.
5. [Ahedo (2023)](/sources/ahedo-2023.md), eqs. 25, 33–35.
6. [Eckels et al. (2024)](/sources/eckels-2024.md), eqs. 3–7.
7. [Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md), performance evaluation.
