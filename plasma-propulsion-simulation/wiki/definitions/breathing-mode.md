---
type: Definition
title: "Breathing mode"
description: "The low-frequency (about 10–30 kHz) longitudinal oscillation of a Hall-thruster discharge, driven by periodic depletion and refilling of the neutral gas, which sets the run length of whole-device simulations and is the usual target signal for calibrating one-dimensional models."
status: established
aliases: [breathing oscillation, ionization oscillation, discharge-current oscillation, low-frequency oscillation]
tags: [hall-thruster, oscillation, instability, fluid, hybrid, calibration]
timestamp: 2026-10-14T00:00:00Z
---

# Breathing mode

The breathing mode is the low-frequency oscillation of the discharge
current $I_d$ of a [Hall-effect thruster](/definitions/hall-effect-thruster.md),
in which ionization periodically depletes the neutral gas in the channel
and the gas then refills it. Its frequency is written $f_{\mathrm{BM}}$.

## Frequency

The sources give these values or ranges:

| Source | $f_{\mathrm{BM}}$ | Basis |
|---|---|---|
| [Boyd (2005)](/sources/boyd-2005.md), §3.4 | "a variety of oscillations including some in the range of 10–50 kHz" | experiments, attributed; not named the breathing mode |
| [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.6 | about 20 kHz | attributed to Boeuf & Garrigues (1998) and Darnon et al. (1999); the 30 µs period of the review's own Fig. 7 in the same section gives about 33 kHz (see below) |
| [Gallo et al. (2021)](/sources/gallo-2021.md), §1 | 10–30 kHz | stated, with a citation |
| [Troyetsky et al. (2026)](/sources/troyetsky-2026.md), neutral-transport section | 10–30 kHz | stated |
| [Marks & Gorodetsky (2025)](/sources/marks-2025.md), "Kinetic simulations in an engineering context" | about 10 kHz | stated, with a citation |
| [Giannetti et al. (2021)](/sources/giannetti-2021.md), §4, Table 2 | 25.4 kHz measured, 25.3 kHz simulated | HT5k thruster, 300 V, 8.4 mg/s xenon |

The ranges are statements about different devices and operating points,
not competing measurements of one quantity.

## Mechanism

* **Neutral depletion and refill.** [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md),
  §2.6, report the mechanism as a periodic depletion and refilling of the
  neutrals whose frequency scales inversely with the neutral refill time.
  Their Fig. 7 reproduces Darnon et al. (1999): an SPT-100 with BN-SiO$_2$
  walls at 280 V and 5 mg/s, compared with high-speed imaging, with a peak
  neutral density of $1.6\times10^{19}$ m$^{-3}$, a peak plasma density of
  $1.6\times10^{18}$ m$^{-3}$ and an emission period of 30 µs (about 33 kHz,
  computed here). They report spectroscopic confirmation attributed to
  Touzeau et al.
* **One cycle in a 1D fluid simulation.** [Giannetti et al. (2021)](/sources/giannetti-2021.md),
  §4, Figs. 7–8, show it in a calibrated
  [one-dimensional fluid model](/methods/one-dimensional-fluid-hall-model.md):
  neutrals advect from the anode into the high-$T_e$ region, a plasma
  density surge follows, and near the anode $n_e$ and $n_n$ oscillate almost
  in phase opposition. The plasma is pushed downstream and also upstream,
  through a weak reversed field near the anode that balances the electron
  pressure; the ion backflow recombines at the anode and refuels the
  neutrals. Every quantity oscillates at the same frequency over the whole
  domain, which the authors take as evidence that the mode is a "global
  self-sustained instability". They state the same conclusion was drawn
  from a wavelet analysis of probe data (their ref. 55).
* **Neutral speed sets the frequency.** In the same model the axial neutral
  velocity directly controls $f_{\mathrm{BM}}$: a faster neutral flow gives
  more frequent surges, which the authors read as consistent with an
  ionization-instability picture (§4, pp. 14–15). This agrees with the
  refill-time scaling above. The calibrated speed, 395 m/s, exceeds the
  100–300 m/s the authors infer for injection from Reid (§4).
* **Amplitude.** In the same model the wall-interaction scaling coefficient
  mainly controls the amplitude, and the in-channel anomalous coefficient
  affects both the mean current and the amplitude (§4, pp. 14–15; see
  [anomalous electron transport](/definitions/anomalous-electron-transport.md)).

## Operating regimes

[Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.6, Fig. 6,
report SPT-100 current–voltage curves at 5 mg/s xenon for three wall
materials (experiment of Gascon et al. 2003, 1D axial fluid calculation of
Barral et al. 2003): at low voltage, current oscillations of 10–50 % at
5–10 kHz; in the nominal regime, oscillations of 10–20 % at about 20 kHz;
and with Al$_2$O$_3$ or SiC walls (or BN-SiO$_2$ above 500 V) a pulsed
regime with amplitude above 100 % of the mean current.

## Measured and simulated waveform

[Giannetti et al. (2021)](/sources/giannetti-2021.md), §4, Fig. 5,
Table 2, measured against simulated, on the HT5k at 300 V and 8.4 mg/s:

| Quantity | Measured | Simulated |
|---|---|---|
| mean $I_d$ | 8.65 A | 8.67 A |
| max $I_d$ | 13.9–17.3 A | 16.4 A |
| min $I_d$ | 3.3–5 A | 4.5 A |
| RMS of $I_d$ | 4.1 A | 3.9 A |
| $f_{\mathrm{BM}}$ | 25.4 kHz | 25.3 kHz |

Both spectra show the fundamental and a second harmonic near 50 kHz; the
simulation adds a sharp peak near 100 kHz where the measured spectrum has
a broadband floor (Fig. 5).

## Consequences for simulation

* **Models that capture it.** [Boyd (2005)](/sources/boyd-2005.md), §3.4,
  attributes the first prediction of the 10–50 kHz oscillations to the 1D
  model of Boeuf & Garrigues (Vlasov ions, fluid neutrals at constant
  velocity) and cites Fife et al. for oscillations in a 2D hybrid model.
  [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.3, state
  that 2D $r$–$z$ PIC models with a Bohm-type anomalous collision capture
  the breathing and ion-transit-time oscillations.
* **Run length.** [Marks & Gorodetsky (2025)](/sources/marks-2025.md) estimate
  that self-consistent ionization introduces a mode of about 10 kHz, which
  calls for runs of about 1 ms, about 50 times the duration of the
  [axial–azimuthal PIC benchmark](/benchmarks/axial-azimuthal-pic-benchmark.md).
* **Excluded by design.** The axial–azimuthal benchmark imposes the
  ionization source, which precludes the breathing mode
  ([Charoy et al. (2020)](/sources/charoy-2020.md), p. 10).
  [Troyetsky et al. (2026)](/sources/troyetsky-2026.md) prescribe a
  quasi-steady neutral profile to suppress it so that their run reaches a
  steady state.
* **Calibration target.** The time-resolved $I_d$ of a breathing discharge
  is the data that [Giannetti et al. (2021)](/sources/giannetti-2021.md)
  calibrate on by hand and that [Saravia et al. (2026)](/sources/saravia-2026.md)
  use in a [Bayesian calibration](/methods/bayesian-calibration.md); the
  latter show that this signal alone does not identify the plume anomalous
  coefficient. In the LANDMARK test case 3 model
  ([1D fluid model](/methods/one-dimensional-fluid-hall-model.md)) the oscillation damps when the anomalous energy-loss coefficient
  exceeds a threshold ([Saravia et al. (2026)](/sources/saravia-2026.md),
  App. A).
* **Analogue in helicon sources.** [Takahashi (2019)](/sources/takahashi-2019.md)
  reports a comparison, attributed to Degeling et al. (1999), between
  neutral-depletion oscillations in helicon plasmas and the Hall-thruster
  ionization oscillation.

# Citations

1. [Boyd (2005)](/sources/boyd-2005.md), §3.4.
2. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §§2.6, 3.3, Figs. 6–7 (accepted manuscript).
3. [Giannetti et al. (2021)](/sources/giannetti-2021.md), §4, Figs. 5, 7–8, Table 2.
4. [Gallo et al. (2021)](/sources/gallo-2021.md), §1.
5. [Charoy et al. (2020)](/sources/charoy-2020.md), p. 10.
6. [Marks & Gorodetsky (2025)](/sources/marks-2025.md), section "Kinetic simulations in an engineering context".
7. [Troyetsky et al. (2026)](/sources/troyetsky-2026.md), neutral-transport section.
8. [Saravia et al. (2026)](/sources/saravia-2026.md), §§2.3, 6, App. A.
9. [Takahashi (2019)](/sources/takahashi-2019.md), neutral-depletion discussion.
