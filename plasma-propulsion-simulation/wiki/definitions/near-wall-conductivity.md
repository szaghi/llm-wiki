---
type: Definition
title: "Near-wall conductivity"
description: "Electron cross-field transport produced by electron collisions with the channel walls and by secondary-electron emission, modelled in fluid codes as an electron–wall collision frequency and resolved in radial PIC; the sources treat it as a contributor to, not the explanation of, anomalous transport."
status: established
aliases: [NWC, wall collisionality, electron–wall collisions, wall-collision mobility]
tags: [anomalous-transport, wall-interaction, sheath, hall-thruster, pic, fluid]
timestamp: 2026-10-15T00:00:00Z
---

# Near-wall conductivity

Near-wall conductivity (NWC) is the axial electron transport that
collisions of electrons with the dielectric channel walls, and the
[secondary electrons](/definitions/secondary-electron-emission.md) the
walls emit, add to the bulk
[cross-field mobility](/definitions/electron-mobility-and-hall-parameter.md).
It is one of the two explanations of
[anomalous electron transport](/definitions/anomalous-electron-transport.md)
considered since the 1990s, the other being instability-driven (Bohm-type)
transport ([Boyd (2005)](/sources/boyd-2005.md), §3.4).

## Fluid-model representation

* **Sheath-based electron–wall frequency.** Taccogna & Garrigues (2019,
  §2.3, eq. 28, attributed to Fife 1998, Barral 2003, Ahedo 2003, Parra
  2006 and Garrigues 2006) give an electron–wall momentum frequency equal
  to $c_s$ divided by the channel width, times
  $\bar\delta_{\mathrm{SEE}}/(1-\bar\delta_{\mathrm{SEE}})$, where
  $\bar\delta_{\mathrm{SEE}}$ is the Maxwellian-averaged emission yield
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md)). It grows
  without bound as the yield approaches 1; the sheath saturates first, at
  $\delta^*_{\mathrm{SEE}}=1-8.3\sqrt{m_e/m_i}\approx0.983$ for xenon (eq.
  27, attributed to Hobbs & Wesson 1967).
  [Giannetti et al. (2021)](/sources/giannetti-2021.md) (App. A, eqs.
  A4–A6) use instead $\nu_w=\nu_{iw}/(1-\delta_{\mathrm{SEE}})$, with an ion
  wall-loss frequency $\nu_{iw}$ equal to $c_s$ times twice the inverse
  channel width times a calibrated dimensionless wall-scaling coefficient
  (0.115, §4), and a yield capped at 0.983. The numerators differ
  ($\bar\delta_{\mathrm{SEE}}$ against 1); the sources do not discuss the
  difference (compiler note).
* **Empirical wall collision term.** A constant frequency scaled from
  $10^7$ s⁻¹, applied inside the channel only, with an empirical energy
  loss proportional to the mean electron energy times the exponential of
  minus 20 eV divided by that energy (Taccogna & Garrigues 2019, eq. 30,
  Fig. 3, with coefficient 0.7, attributed to Boeuf &
  Garrigues 1998 and Hagelaar 2002). Values in use: scale factor 0.1 in
  the 1D axial comparison runs of
  [Reza et al. (2022)](/sources/reza-2022.md) (§5.1, Eqs. 14–15,
  implemented as a fictitious MCC event); best fit 0.4 to the PIC friction
  force inside the channel in
  [Charoy et al. (2020)](/sources/charoy-2020.md) (§IV A–B, Eqs. 8–9,
  Fig. 7); $\nu_w=10^7$ s⁻¹ inside the channel and 0 outside in the
  LANDMARK test case 3 ([1D fluid model](/methods/one-dimensional-fluid-hall-model.md))
  implementation of [Saravia et al. (2026)](/sources/saravia-2026.md)
  (eq. 6).
* **NWC as a Bohm-type form.** Table II of Taccogna & Garrigues (2019,
  §2.4) lists an NWC anomalous frequency proportional to $c_s$ (Barral et
  al. 2003). Ahedo (2023, Appendix) reports that some 2D models fold wall
  collisionality into the anomalous collisionality.
* **Inertia.** The wall loss of azimuthal electron momentum is the
  primary-electron wall flux times $m_e$ times the azimuthal electron
  velocity at the sheath edge; it "cannot be imposed in an inertialess
  model" ([Ahedo (2023)](/sources/ahedo-2023.md), Appendix, Eq. 73).

## Evidence on its weight

* In the P5 thruster comparison reviewed by Boyd (2005, Fig. 16), the
  wall-collision mobility model makes the potential drop too far upstream,
  the Bohm model too far downstream, and the measurement lies between
  them. Boyd reports that Latocha et al. analysed NWC.
* Taccogna & Garrigues (2019) report:
  * NWC alone cannot explain anomalous transport (§2.4, attributed to
    Ahedo et al. 2003); 1D calculations with secondary emission as the only
    anomalous mechanism underestimate the discharge current (§2.6);
  * Boltzmann solvers with walls deplete the high-energy electron tail,
    give wall-loss frequencies far below Maxwellian estimates, no space-charge
    saturation and a minor NWC (§3.1, attributed to Latocha 2002 and
    Meezan & Cappelli 2002);
  * in 2D radial–azimuthal PIC, raising the yield from 0 to the saturation
    value doubles the near-wall mobility while the bulk anomalous mobility
    falls by 20%, so the total stays about constant (§3.4, attributed to
    Tavant 2018 and Taccogna 2019).
* In a [reduced-order](/methods/reduced-order-pic.md) radial–azimuthal PIC,
  the mobility averaged over the whole radius exceeds the mobility of the
  central half of the channel once the sheath is space-charge saturated,
  which the authors read as NWC; in the axial–radial plane a radial
  oscillation of the electron axial drift is attributed to NWC (shown,
  figure images missing from the preprint)
  ([Reza et al. (2022)](/sources/reza-2022.md), §4.3.2, §5.2, Fig. 13b).
  The single-region approximation drives the radial wall physics with
  axially averaged bulk conditions and overpredicts wall-induced mobility
  near the anode, which produces a spurious anode sheath (§5.2).
* In a 1D radial PIC of a Hall-thruster cross-section, the gyroviscous
  pressure term causes Larmor-scale undulations of the axial electron
  current that resemble NWC; Ahedo reports "a certain consensus" that
  wave-based turbulence matters more than wall collisionality for
  anomalous transport ([Ahedo (2023)](/sources/ahedo-2023.md), Eqs. 44–46,
  Fig. 4, Appendix).
* Charoy et al. (2020, §III A) show that axial–azimuthal PIC develops the
  anomalous transport without any electron–wall collision, since the
  domain has no radial walls.

# Citations

1. [Boyd (2005)](/sources/boyd-2005.md), §3.4, Fig. 16.
2. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §§2.3, 2.4, 2.6, 3.1, 3.4, eqs. 27–30, Tab. II (accepted manuscript).
3. [Charoy et al. (2020)](/sources/charoy-2020.md), §§III A, IV A–B, Eqs. 8–9, Fig. 7 (accepted manuscript).
4. [Giannetti et al. (2021)](/sources/giannetti-2021.md), §4, App. A, eqs. A4–A6.
5. [Reza et al. (2022)](/sources/reza-2022.md), §§4.3.2, 5.1, 5.2, Eqs. 14–15, Fig. 13 (preprint).
6. [Ahedo (2023)](/sources/ahedo-2023.md), Eqs. 44–46, 73, Fig. 4, Appendix.
7. [Saravia et al. (2026)](/sources/saravia-2026.md), §2.1, eq. 6.
