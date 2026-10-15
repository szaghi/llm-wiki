---
type: Definition
title: "High-frequency combustion instability in liquid rocket engines"
description: "Self-excited coupling of chamber acoustic modes with unsteady heat release (Rayleigh criterion), here in its injection-coupled form, where a transverse chamber mode locks onto injector resonances, shifts in frequency as the flame shortens, and is not predicted by the classic velocity-ratio correlations."
status: established
aliases: [combustion instability, thermoacoustic instability, high-frequency instability, injection-coupled instability, self-excited combustion instability]
tags: [combustion-instability, thermoacoustics, liquid-rocket-engine, injector-dynamics, acoustics, experiment]
timestamp: 2026-10-14T00:00:00Z
---

# High-frequency combustion instability in liquid rocket engines

A high-frequency combustion instability is a self-excited oscillation in which
an acoustic mode of the combustion chamber and the unsteady heat release of
the flame feed each other. The instability condition is the Rayleigh
criterion, which [Armbruster et al. (2018)](/sources/armbruster-2018.md), §1,
Eq. 1, state after Rayleigh and Putnam & Dennis:

$$\iint p'(\mathbf x,t)\,\dot q'(\mathbf x,t)\,dV\,dt \;\ge\; 0,$$

where $\dot q'$ is the fluctuation of the heat-release rate $\dot q$. Energy
is added to the acoustic field when pressure and heat-release fluctuations are
in phase on average over the chamber volume and over time.

## Intrinsic and injection-coupled instabilities

[Armbruster et al. (2018)](/sources/armbruster-2018.md), §1, distinguish
intrinsic instabilities from **injection-coupled** ones, in which a chamber
mode couples with an acoustic resonance of the injectors or their feed
volumes. Their conclusion (§5) is that both instability types observed in the
BKD combustor (below) are injection-coupled, and that the coupling depends on
the matching of chamber and injector frequencies rather than on the injection
velocity ratio or the fuel injection pressure drop.

## The first tangential (1T) mode: standing and spinning

The instabilities studied in BKD are first-tangential (1T) chamber modes.
[Armbruster et al. (2018)](/sources/armbruster-2018.md), §3.2, Fig. 9, track
them with a Hilbert-transform instantaneous amplitude and frequency
(band-pass 9–12.5 kHz) and a pressure-field reconstruction that yields a
spin ratio (0 for a standing mode, magnitude 1 for a fully spinning mode).
Shown:

* the amplitude varies rapidly; at low amplitude the mode tends to a
  standing 1T, at high amplitude it is fully spinning;
* the frequency follows the amplitude with a slight lag, from about 9.5 kHz
  to almost 12 kHz, an increase of more than 25 %; the reconstructed field
  stays 1T-like throughout;
* the blurred one-second power spectra of the instability are explained by
  averaging over this varying frequency.

## Frequency shift by flame shortening

[Armbruster et al. (2018)](/sources/armbruster-2018.md), §3.3, Eqs. 3–5,
Fig. 11, define a **normalized frequency shift** of the 1T mode: the
difference between the 1T frequency at a given acoustic-velocity amplitude and
the 1T frequency extrapolated to zero amplitude, divided by the difference
between the 1T frequency computed with the chemical-equilibrium (CEA) sound
speed of the chamber and that zero-amplitude frequency. It is 0 for the
unperturbed flame and 1 for a chamber filled with gas at equilibrium sound
speed, i.e. a flame of zero length. The acoustic-velocity amplitude is taken
from the 1D plane-wave relation as the pressure amplitude divided by the
product of mean density and mean sound speed (Eq. 3; both from CEA).

* **Shown.** A logistic least-squares fit (Eq. 5) of the normalized shift
  against the acoustic velocity gives adjusted $R^2$ of 0.6–0.76; the curves
  are similar for 7 MPa (70 bar) at $O/F$ = 4, 5, 6 with liquid-hydrogen
  injection and 8 MPa (80 bar) at $O/F$ = 6 with gaseous-hydrogen injection,
  and reach about 0.6 at acoustic velocities up to about 600 m/s (read from
  Fig. 11). The mode stays 1T.
* **Shown.** Cross-correlation gives a lag of the frequency behind the
  amplitude of 0.6–1.1 ms, i.e. 7–11 acoustic cycles, against about 5 cycles
  measured and 15 cycles computed in the optically accessible BKH combustor
  (attributed).
* **Stated by analogy.** The physical mechanism, transverse acoustic velocity
  shortening the flame and raising the sound speed near the faceplate, is
  taken from BKH optical results and numerical studies; BKD has no optical
  access, so it is not observed there.

## Steep-fronted (detonation-like) waves

Rocket-combustor literature reports detonation-like spinning waves in resonant
combustion (attributed in [Armbruster et al. (2018)](/sources/armbruster-2018.md), §1).
Armbruster et al. exclude them for the BKD type-2 instability by a rise-time
test (§3.3, Fig. 10): a phase-locked average over 200 cycles (Run 1, 7 MPa,
$O/F$ = 4, 6° bins, 7 sensors) gives a spinning tangential field of about
3 MPa (30 bar) amplitude whose rise time is close to 180°, half the period,
as expected for a sinusoidal acoustic wave; detonation-like waves would rise
in under 2 % of the period (6°). The test was made at one load point and is
generalized by the authors to all type-2 load points.

[Peng et al. (2018)](/sources/peng-2018.md), §3.2.3, state from the other
side that the low-pressure-rise "sawtooth" wave of a
[rotating detonation engine](/definitions/rotating-detonation-engine.md)
near its lean limit is "a manifestation of high-frequency tangential
instability in rocket combustor"; they do not demonstrate the mechanism.

## Stability correlations and the BKD counter-evidence

Two classical NASA Lewis correlations for hydrogen–oxygen coaxial injection,
by Wanhainen et al., are tested by [Armbruster et al. (2018)](/sources/armbruster-2018.md), §4.1,
Figs. 12–13, Eq. 6, Table 1:

* **Injection velocity ratio.** The critical gas-to-liquid velocity ratio
  $\mathrm{VR}$ is 6.5 (attributed). All BKD type-2 load points lie far above
  it, but stable load points have similar $\mathrm{VR}$, so $\mathrm{VR}$ is
  excluded as the driver.
* **Stability-limit parameter.** The parameter is the product of the square
  root of twice the hydrogen injection pressure drop over the hydrogen
  density, the oxygen density, the oxidizer-post exit diameter to the power
  1.25, and $(O/F)^{-1/2}$; its limit is 42.1 kg/(s·m^0.75) (attributed). All
  type-2 load points lie on the "stable" side.
* **Low fuel injection pressure drop.** The hydrogen injection pressure drop
  is 15–40 % (Table 1, presumably of $p_c$), relatively high, so the
  low-pressure-drop coupling explanation of Hutt & Rocker (attributed) does
  not account for the BKD instability.

These are the paper's own measurements against correlations of sources this
bundle has not ingested; they are recorded here as attributed counter-evidence.

## Triple coupling (hypothesis)

[Armbruster et al. (2018)](/sources/armbruster-2018.md), §4.2–4.4, Figs. 14,
20, 21, propose a "triple-coupling" mechanism for the BKD type-2 instability,
supported by data but not demonstrated:

1. **Onset.** The 1T mode couples with the second longitudinal (2L) mode of
   the LOX posts, as in the type-1 instability. Before onset (Run 1, 7 MPa,
   $O/F$ = 3, 13.5–13.9 s) the 1T near 10 kHz is slightly excited and the LOX
   manifold peaks near 10 kHz.
2. **Lock-on to the hydrogen injectors.** As the amplitude rises and the 1T
   frequency increases, it couples with the first longitudinal (1L) mode of
   the hydrogen injectors. During the instability (14.2–14.6 s) the chamber
   peaks at 11.8 kHz with a matching hydrogen-manifold peak, an increase well
   above the 3 dB sensor-tube uncertainty.
3. **Conditions.** A necessary but not sufficient condition is an unperturbed
   1T frequency close to the LOX-post 2L, with the hydrogen 1L slightly
   higher. Appearance and disappearance at constant conditions (Fig. 21,
   about 28 s) indicate that a non-linear trigger is required.

The measured LOX-post frequency is 5–9 % above the published 2L value
(attributed to Gröning et al.).

## Acoustic modelling of the injector resonance

[Armbruster et al. (2018)](/sources/armbruster-2018.md), §4.3, Figs. 16–19,
compute the hydrogen-injector 1L frequency three ways:

| Model | Hydrogen 1L frequency | Agreement with the measured hydrogen-manifold peak |
|---|---|---|
| 2D axisymmetric Helmholtz (COMSOL), one element, no mean flow | 9.8–11.9 kHz | — |
| 3D Helmholtz (COMSOL), full injector head plus 50 mm of chamber, 1.3 million tetrahedra, no mean flow | 10.4–12.7 kHz | mean error 4 %; gaseous-hydrogen and transient points overestimated by 2.6–7.6 %, attributed to neglected flow (annulus $\mathrm{Ma}$ up to 0.4) |
| 1D acoustic network with mean flow (plane-wave transfer matrices, eigenfrequencies from the zero determinant of the system matrix) | — | improves those points; one run underpredicted by about 7 %, the other five within 1 % (steady) and about ±3.5 % (transient); regression slope 0.97, $R^2$ = 0.67 over nine load points |

The 3D model's chamber sound speed, 1396 m/s, was set to match the 1T of the
gaseous-hydrogen 8 MPa, $O/F$ = 6 case.

## Test case: the BKD combustor

DLR's research combustor BKD, at the P8 test facility, Lampoldshausen, is the
test case of [Armbruster et al. (2018)](/sources/armbruster-2018.md), §2:

* 42 shear-coaxial LOX/H₂ injectors with recessed, tapered LOX posts, in
  standard and shortened variants; cylindrical chamber of 80 mm inner
  diameter and 200 mm cylindrical length, 50 mm throat, contraction ratio
  2.56, characteristic length 0.64 m; water-cooled copper alloy.
* $p_c$ = 5–8 MPa (50–80 bar), $O/F$ = 2–6; at 8 MPa and $O/F$ = 6, total
  $\dot m$ 6.7 kg/s, $F\approx$ 24 kN, thermal power 87 MW. Hydrogen injected
  as liquid (about 45 K) or gas (95–100 K).
* Eight water-cooled dynamic pressure sensors in a ring next to the faceplate,
  sampled at 100 kHz with a 30 kHz anti-aliasing filter and a ±3 MPa (±30 bar)
  range; dynamic sensors in the LOX dome and hydrogen manifold.

The type-2 instability (§3.1) has peak frequencies of 10.4–12.1 kHz, appeared
in 6 runs (liquid-hydrogen injection, and gaseous hydrogen only with the
shorter injectors), saturates the ±3 MPa sensors, and grows from stable to
saturation in under 5 ms; the maximum RMS is 1.8 MPa (18 bar), against about
0.34 MPa (3.4 bar) averaged for the earlier type-1 instability near 10 kHz.
During the instability the static chamber pressure falls by 1–2 % while the
manifold pressures rise, so the injection pressure loss increases (Fig. 8).

## Injector-side oscillations

Gas–liquid coaxial injectors can oscillate by themselves, without combustion:
[self-pulsation](/definitions/injector-self-pulsation.md) of a recessed swirl
coaxial injector produces recess-pressure oscillations from about 1.2 kHz up to an
"ultra-high frequency" band of 8–9 kHz in cold flow
([Bai et al. (2018)](/sources/bai-2018.md), §3.3, Fig. 10; the lower values
read from the figure). Bai et al. list
the LOX-post recess length as the parameter that, in Bazarov's attributed
account, matters most (§1). Their study is a cold-flow injector study; it
does not test coupling with a chamber mode.

# Citations

1. [Armbruster et al. (2018)](/sources/armbruster-2018.md) — §1 (Eq. 1, classification, detonation-like waves), §2 (BKD), §3.1–3.3 (Eqs. 3–5, Figs. 7–11), §4.1–4.4 (Eq. 6, Table 1, Figs. 12–21), §5.
2. [Bai et al. (2018)](/sources/bai-2018.md) — §1, §3.3.
3. [Peng et al. (2018)](/sources/peng-2018.md) — §3.2.3.
