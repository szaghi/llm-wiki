---
type: Definition
title: "Current-free double layer"
description: "A localized electrostatic potential drop, a few tens to hundreds of Debye lengths thick, that forms without net current where a helicon plasma expands into a diverging magnetic field and accelerates a supersonic ion beam; measurements and 1D PIC tie it to a depleted-tail electron distribution rather than beam electrons, and its potential drop scales with the electron temperature."
status: established
aliases: [CFDL, double layer, helicon double layer, HDLT]
tags: [helicon, magnetic-nozzle, kinetic, pic, sheath]
timestamp: 2026-10-14T00:00:00Z
---

# Current-free double layer

A current-free double layer (CFDL) is a localized potential drop that
forms, with no net current through it, where a radiofrequency plasma
expands from its source into a diverging magnetic field. Downstream of it,
supersonic beam ions coexist with thermal ions. Charles & Boswell (2004)
identified the beam energy with a CFDL potential drop a few tens to
hundreds of Debye lengths thick, and the CFDL has been seen in Ar, Xe,
N$_2$, N$_2$O, CH$_4$ and CO$_2$ ([Takahashi (2019)](/sources/takahashi-2019.md),
§5.2, Fig. 7). The helicon double-layer thruster concept is due to Charles
(2009) (§2).

## Formation

* The magnetic-field threshold depends on the source-tube diameter (tubes
  of 13.7, 6.5 and 4.6 cm, $B$ from 0 to 0.04 T, printed as 400 G). CFDL acceleration starts
  when the ion Larmor radius computed with the ion thermal speed falls below
  the tube radius (Takahashi et al. 2010;
  [Takahashi (2019)](/sources/takahashi-2019.md), §5.2, Fig. 8).
* **Simulation.** 1D PIC reproduced CFDL formation with a plasma-loss term
  added artificially downstream (Meige et al. 2005); 2D PIC showed
  spontaneous formation (Rao & Singh 2012) (§5.2). These are cited by the
  review, which runs no simulation.

## Electron physics

* Three theories are reported: backstreaming beam electrons (Lieberman &
  Charles 2006), a sheath-like current-free balance with Maxwellian
  electrons (Chen 2006), and hot tail electrons (Ahedo & Sánchez 2009)
  ([Takahashi (2019)](/sources/takahashi-2019.md), §5.2).
* 1D PIC showed no energetic beam electrons on the high-potential side
  (Meige & Boswell 2006). The measured upstream electron energy distribution
  has a depleted tail instead: trapped electrons at about 8 eV, upstream
  tail and downstream electrons at about 5 eV, a break energy of 27 eV that
  matches the double-layer potential at low pressure, and plasma potentials
  of 60 V upstream and 36 V downstream (Takahashi et al. 2007; §5.3,
  Figs. 9–10). The review concludes that the CFDL is sustained by a single
  source on the high-potential side, calls the beam-electron and hot-tail
  models "inconsistent with the experiments" (§5.4), and calls CFDLs in
  expanding plasmas "a new class" of double layer (§5.3).
* Energetic electrons leak along the outermost field lines and produce
  conical density structures (§5.3, Fig. 11).

## Potential drop

The current-free sheath-like balance of Chen (2006), as given by
[Takahashi (2019)](/sources/takahashi-2019.md), §5.4, Eq. 24, sets the
double-layer potential drop to
$$\frac12\left[1+\ln\left(\frac{m_i}{2\pi m_e}\right)\right]\frac{T_e}{e}\approx5.18\,\frac{T_e}{e}\quad\text{(argon)}.$$
This fits the 20–30 eV beams measured with a downstream $T_e\approx5$ eV
and the drop of about 25 eV observed by Charles & Boswell. The ECR thruster
gives 100–200 eV beams at $T_e\approx20$ eV, above this estimate, and for a
Druyvesteyn distribution the drop is about 4 times an effective electron
temperature over $e$ (§5.4).
Ion acceleration by ambipolar and CFDL fields imparts no significant net
momentum to the thruster: the measured thrust matches the source electron
pressure (§5.5.1); see
[thrust decomposition of a magnetic nozzle](/results/magnetic-nozzle-thrust-decomposition.md).

## A quasi-1D particle model

[Gallo et al. (2021)](/sources/gallo-2021.md), §3, §4.4, model a helicon
double-layer thruster along the outermost field line of the
[magnetic nozzle](/definitions/magnetic-nozzle.md) with heavy-species
macroparticles, isothermal [Boltzmann electrons](/methods/boltzmann-electron-model.md)
and a nonlinear Poisson equation with $\phi=0$ at both ends. No experiment
is compared.

* Argon, $T_e=10$ eV: potential drop 12 V, "mostly confined close to the
  chamber exit"; ions weakly supersonic (Mach number about $-1.2$ at the
  exit); $I_{sp}=662$ s, thrust 0.0126 mN (Fig. 10).
* $T_e$ = 5, 10, 15, 20 eV gives drops of 6, 12, 17 and 23 V and $I_{sp}$
  from 460 to 977 s; the computed $I_{sp}$ lies below the ideal value of an
  ion falling freely through the computed drop at every point (Fig. 11,
  §5). The ionization rate does not change the drop (Fig. 12).
* At equal ion mass flow, iodine gives about half the argon performance
  (Table 3).

These computed drops are 1.1–1.2 times $T_e/e$, below the $5.18\,T_e/e$ of
the Chen relation reported by [Takahashi (2019)](/sources/takahashi-2019.md).
[Gallo et al. (2021)](/sources/gallo-2021.md) compare neither with that
relation nor with measurement.

# Citations

1. [Takahashi (2019)](/sources/takahashi-2019.md), §2, §5.2–5.5, Eq. 24, Figs. 7–11.
2. [Gallo et al. (2021)](/sources/gallo-2021.md), §3, §4.4, §5, Eqs. 13–18, Figs. 10–12, Table 3.
