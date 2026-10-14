---
type: Definition
title: "Magnetic shielding"
description: "A Hall-thruster magnetic topology, with field lines grazing the channel walls and a chamfered channel, that keeps the electrons near the walls cold so that the radial electric field and the sheath drop shrink; reported to cut computed wall erosion by three orders of magnitude."
status: established
aliases: [magnetically shielded Hall thruster, MS-HET, MS configuration, magnetic shielding configuration]
tags: [hall-thruster, wall-interaction, sheath]
timestamp: 2026-10-14T00:00:00Z
---

# Magnetic shielding

## Principle

In a magnetically shielded (MS) [Hall-effect thruster](/definitions/hall-effect-thruster.md)
the field lines near the walls run parallel to them and the channel is
chamfered, which keeps the electrons near the walls cold, so that the
radial electric field (their eq. 25, the
[thermalized-potential](/definitions/thermalized-potential.md) relation)
and the sheath drop (their eq. 27) shrink
([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.8). In the H6 thruster at 300 V and 20 A,
wall-probe data and 2D fluid computations show the MS potential along the
wall nearly flat at about the discharge potential (Fig. 10, attributed to
Mikellides et al. 2014a).
In MS thrusters, ionization sits at the exit plane and acceleration in the
near plume (attributed to Grimaud & Mazouffre 2017 and Garrigues et al.).

## Effect on erosion and lifetime

* Computed wall erosion falls by three orders of magnitude, confirmed
  experimentally ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md),
  §2.8, attributed to Mikellides et al. 2014a,b). A graphite wall in MS
  configuration does not drastically change performance (attributed to
  Grimaud & Mazouffre 2017).
* The MS configuration "has led to a drastic improvement in thruster
  lifetimes" ([Adamovich et al. (2017)](/sources/adamovich-2017.md), §12,
  citing Mazouffre 2016 and Hofer et al. 2014).
* In unshielded configurations the integrated ion wall flux reaches up to
  40 % of the total ion production
  ([Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. III C).

## Thrusters named

The H6 (comparison of unshielded and shielded versions), the H9 and the
200 W MaSMi at JPL ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md),
§2.8); the nested-channel X2, "validated at 20 kW" in MS configuration
([Adamovich et al. (2017)](/sources/adamovich-2017.md), §12).

## In simulations

* **HYPHEN.** [Ahedo (2023)](/sources/ahedo-2023.md), Figs. 1 and 6, shows
  axisymmetric [HYPHEN](/software/hyphen.md) runs of an MS thruster on a
  [magnetic-field-aligned mesh](/methods/magnetic-field-aligned-mesh.md)
  with a singular null-field point inside the channel: the lines around
  the null point shield the electron current from the walls, the magnetic
  lines are nearly isothermal, and the cathode current splits into a
  plume-neutralizing beam and a beam entering the channel.
* **Fluid wall losses.** [Giannetti et al. (2021)](/sources/giannetti-2021.md),
  §4, needed a strong reduction of the wall-loss terms of their
  [1D fluid model](/methods/one-dimensional-fluid-hall-model.md) and
  attribute it partly to the chamfered channel of their end-of-life
  thruster configuration shielding the walls magnetically (stated, with
  citations), besides unresolved radial gradients and fluid sheath models
  that overestimate wall losses.

# Citations

1. [Adamovich et al. (2017)](/sources/adamovich-2017.md), §12.
2. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.8, Fig. 10 (accepted manuscript).
3. [Giannetti et al. (2021)](/sources/giannetti-2021.md), §4.
4. [Ahedo (2023)](/sources/ahedo-2023.md), Figs. 1, 6.
5. [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. III C (accepted manuscript).
