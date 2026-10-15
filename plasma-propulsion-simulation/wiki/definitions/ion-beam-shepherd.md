---
type: Definition
title: "Ion beam shepherd"
description: "Contactless space-debris removal by a shepherd satellite whose impulse-transfer ion thruster pushes the debris with its plume while a compensation thruster cancels the reaction; the beam force is modelled with a self-similar conical far-plume model, and the concept is the reference against which magnetic drag augmentation is compared."
status: established
aliases: [IBS, ion-beam shepherd, ion beam debris removal]
tags: [plume, ion-thruster, debris-removal]
timestamp: 2026-10-15T00:00:00Z
---

# Ion beam shepherd

An ion beam shepherd (IBS) removes a space-debris object without contact. A
shepherd satellite flies a few debris diameters ahead of the object and
carries two thrusters: an impulse transfer thruster (ITT), whose ion plume is
pointed at the debris and transfers de-orbiting momentum to it, and an
impulse compensation thruster (ICT), pointed the opposite way to cancel the
reaction force of the ITT
([Alpatov et al. (2018)](/sources/alpatov-2018.md), Introduction, Fig. 1;
concept attributed to Bombardelli & Peláez 2011, ref. [1]). The source
credits the concept with acceptable de-orbiting performance, low risk,
reusability over several missions and technological readiness (stated).

## Force balance

Write $F_{\mathrm{IT}}$ and $F_{\mathrm{CT}}$ for the ITT and ICT thrusts.
When the whole beam intercepts the debris, the force transmitted to it is
approximately $F_{\mathrm{IT}}$ along the beam axis; when part of the cone
misses the body, the force is smaller along the axis and acquires small
transverse components
([Alpatov et al. (2018)](/sources/alpatov-2018.md), §4, eq. 13; stated).
For the shepherd to follow the debris, the
compensation thruster must cancel the ITT reaction and also give the
shepherd the debris's acceleration, so the nominal compensation thrust is

$$|F_{\mathrm{CT}}|=F_{\mathrm{IT}}\left(1+\frac{\text{shepherd mass}}{\text{debris mass}}\right)$$

([Alpatov et al. (2018)](/sources/alpatov-2018.md), eq. 30, written there
with a minus sign for the opposite direction). With $F_{\mathrm{IT}}=0.031$ N,
a 500 kg shepherd and a 1575 kg debris object this is 0.0408 N, which matches
the total ICT impulse of $3.525\times10^5$ N s over the 100-day de-orbit
(reader's check on the Source page).

Compensating the reaction is not enough to hold the separation: the in-plane
shepherd–debris relative dynamics are unstable, and the out-of-plane motion
is stable only if the radial destabilizing effect of the beam does not exceed
the gravity-gradient restoring force
([Alpatov et al. (2018)](/sources/alpatov-2018.md), Introduction, attributed
to Bombardelli et al. 2012 and Bombardelli 2018). The shepherd therefore
needs active relative-position control.

## Beam force from a far-plume model

Alpatov et al. compute the beam force on the debris with a self-similar
far-plume model and a central-projection method, both taken from earlier
work and not derived in the paper
([Alpatov et al. (2018)](/sources/alpatov-2018.md), §4, eqs. 6–11, after
Merino et al. 2015, ref. [14], and Alpatov et al. 2016, ref. [8]):

* **Momentum transfer.** The force on a surface element is
  $m_in_i\,\mathbf u_i$ times the ion flux through the element (the
  component of $\mathbf u_i$ along the inward normal) times its area,
  integrated over the irradiated surface (eqs. 6–7). Every incident ion
  deposits its full momentum; no reflection, sputtering or
  accommodation enters the expression (reader's reading of eq. 6).
* **Density.** In the far region $n_i$ is Gaussian in the radial distance
  from the beam axis, with a width that grows with axial distance $z$
  through a self-similarity function, and the peak decays as the inverse
  square of that width so that the ion flux is conserved; $n_0$ is the
  density at the start of the far region. A Gaussian constant of 6 puts
  about 95 % of the ion current inside the reference radius, the
  conventional fraction that defines the beam divergence angle (eq. 8,
  attributed to Cichocki et al. 2015, ref. [13]).
* **Conical beam.** "For typical values of the ion Mach number greater than
  or equal to 30 and distances to the SDO less than 10 m, it is safe to
  assume that the beam is conical with very little error": the width grows
  linearly with $z$ at the initial divergence half-angle of the 95 %
  streamtube (eq. 9, attributed to ref. [14]).
* **Velocity.** In the "highly hypersonic" beam the axial ion velocity
  $u_{i,z}$ stays at its initial value; the radial velocity $u_{i,r}$ is
  $u_{i,z}$ times the normalized radius times the logarithmic derivative of
  the width (eqs. 10–11); with the conical width the ions move on straight
  rays from a virtual apex (reader's reading).
* **Central projection.** The force on a three-dimensional body can be
  computed from the body's central projection onto a plane normal to the
  beam axis (§4, Fig. 2, attributed to ref. [8]).

The model as used is collisionless and hypersonic. It contains no
[charge-exchange ions](/definitions/charge-exchange-ions.md), backflow,
electron pressure or electric field; its stated validity is limited to ion
Mach numbers of at least 30 and distances below 10 m. The case studied is a
xenon beam of 0.031 N with initial divergence half-angle 7°, initial 95 %
radius 0.0808 m, axial ion velocity 71580 m/s and $I_{sp}=3400$ s (as
printed; 71580 m/s corresponds to about 7300 s, see the Source page), acting on
a Cyclone-3 upper stage modelled as a cylinder 2.6 m high and 2.2 m in
diameter, 7 m from the shepherd
([Alpatov et al. (2018)](/sources/alpatov-2018.md), §4, Table 2, §6). The
beam force then enters the control design only as a bounded perturbation:
at most $F_{\mathrm{IT}}$ over the minimum debris mass,
$2.5\times10^{-5}$ N/kg, along track, a bound justified because the beam
acceleration exceeds the differential orbital perturbation by an order of
magnitude even at the end of the mission; the radial bound,
$2\times10^{-7}$ N/kg, is a conservative estimate of the orbital
perturbations (§6, eq. 21; stated).

The same plume–body momentum transfer is computed at the opposite fidelity
extreme by full 3D PIC-DSMC hybrids: EX-PWS, with Boltzmann electrons,
charge-exchange ions and a plate force made of incident, reflected and
sputtered contributions (Maxwell reflection with species-dependent
accommodation), over-predicts the measured axial force of the LIPS-200
ion-thruster plume on a 300 mm plate at 0.6–1.0 m, by at most 16.36 %
against a torsional-balance measurement
([Cai et al. (2018)](/sources/cai-2018.md), §4.1, Fig. 4; see
[hybrid PIC–fluid models](/methods/hybrid-pic-fluid-model.md) and
[EX-PWS](/software/ex-pws.md)). Cai et al.'s sensitivities support the
full-deposition, CEX-free assumption at 0.6–1.0 m: setting the sticking
coefficient to 1 changes the plate force by about 0.1–0.25 % (§4.1,
Fig. 5; see [gas–surface interaction](/methods/gas-surface-interaction.md)),
and charge-exchange ions carry less than 0.1 % of the plate momentum
(§4.1, Table 3). No ingested source tests the assumption at shepherd
distances.

## Relative-position control and propellant

Alpatov et al. hold the shepherd 7 m ahead of the debris using only
along-track ICT throttling under a robust controller; a 100-day de-orbit
costs 10.58 kg of xenon and no hydrazine, against 10.59 kg of xenon plus
12.93 kg of hydrazine for a conventional scheme
([Alpatov et al. (2018)](/sources/alpatov-2018.md), §§5–9; see the Source
page for the controller).

## Comparisons and variants

* **Magnetic drag augmentation.** Shuvalov et al. compare the ion beam
  shepherd with deorbiting by the plasma drag of a magnetized body
  ([plasma drag augmentation of a magnetized body](/results/magnetized-body-plasma-drag.md);
  [Shuvalov et al. (2018)](/sources/shuvalov-2018.md), §6, Figs. 8–9).
  The beam pressures they quote, from the literature, are 8.43 mN/m² at 7 m
  and 4.04 mN/m² at 10 m for a 3.5 keV Xe⁺ beam (LEOSWEEP project), and
  5.78 mN/m² and 1.44 mN/m² at 20 m for a 6 keV Xe⁺ beam of divergence
  half-angle about 3° and 6° (a large-GEO-debris reorbiter, Kitamura et al.
  2014). From their empirical drag law they calculate, not measure, that a
  body field of 0.6–0.8 T gives a drag pressure close to that of the 3.5 keV
  beam at 10 m (4.04 mN/m²) and of the 6 keV beam of divergence half-angle about 6° at 20 m
  (1.44 mN/m²), citing their 250–800 km altitude scan (Fig. 9); in their
  own Fig. 8 (700 km) the 0.6–0.8 T range matches only the latter, and the
  7 m LEOSWEEP value (8.43 mN/m²) needs about 2.6 T. The ion energy implied by Alpatov et al.'s
  71580 m/s xenon beam, about 3.5 keV, is that of the LEOSWEEP beam
  (reader's check).
* **Electrodeless variant.** The review notes that the ion beam shepherd
  has been proposed with two ion-gridded thrusters, and reports a
  bidirectional helicon-type
  [magnetic-nozzle](/definitions/magnetic-nozzle.md) thruster, a single
  device that fills both the impulse-transfer and the compensation roles,
  demonstrated in a laboratory experiment (Takahashi et al. 2018, cited in
  the review) with simultaneous force measurements on the thruster (zero
  net force) and on a target plate (finite decelerating force)
  ([Takahashi (2019)](/sources/takahashi-2019.md), §6.4). The review gives
  no shepherd force balance or control analysis.

# Citations

1. [Alpatov et al. (2018)](/sources/alpatov-2018.md), §§1, 3–9, eqs. 6–13,
   21, 30, Table 2, Figs. 1–2.
2. [Shuvalov et al. (2018)](/sources/shuvalov-2018.md), §6, Figs. 8–9.
3. [Takahashi (2019)](/sources/takahashi-2019.md), §6.4.
4. [Cai et al. (2018)](/sources/cai-2018.md), §4.1, Figs. 4–5, Table 3 (PIC-DSMC plume
   force and its wall-model and CEX sensitivities).
