---
type: Source
title: "Armbruster et al. (2018) — Experimental investigation of self-excited combustion instabilities with injection coupling in a cryogenic rocket combustor"
description: "Characterizes a second (type 2) self-excited 1T instability in DLR's 42-injector LOX/H2 combustor BKD, shows a frequency rise with amplitude consistent with flame shortening, shows that the classic NASA velocity-ratio and stability-limit correlations do not predict it, and proposes a triple coupling of the chamber 1T mode with the LOX-post 2L and H2-injector 1L modes."
resource: "doi:10.1016/j.actaastro.2018.06.057"
source_kind: paper
authors: [Armbruster W., Hardi J.S., Suslov D., Oschwald M.]
year: 2018
venue: "Acta Astronaut. 151:655–667"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Armbruster_Experimental_investigation_of_self-excited_combustion_instab.pdf"
tags: [context, liquid-rocket-engine, combustion-instability, injection-coupling, thermoacoustics, experiment]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper analyses a second ("type 2") self-excited high-frequency
instability in DLR's research combustor BKD (42 shear-coaxial LOX/H2
injectors) at the P8 test bench, with peak-to-peak amplitudes up to 80–86%
of the static chamber pressure. Hilbert-transform instantaneous amplitude
and frequency, and a pressure-field reconstruction, show that the first
tangential (1T) mode switches between standing and spinning and that its
frequency rises from about 9.5 kHz to almost 12 kHz with amplitude. A
phase-locked cycle has a sinusoidal rise time (about 180°), which excludes
steep-fronted detonation-like waves. A normalized frequency shift collapses
the frequency rise against transverse acoustic velocity for all steady load
points; by analogy with optical results in another DLR combustor (BKH), the
authors interpret it as flame shortening raising the near-faceplate sound
speed. The classic NASA Lewis correlations (injection velocity ratio limit
6.5; Wanhainen stability-limit parameter 42.1 kg/(s·m^0.75)) and a low H2
injection pressure drop do not predict the BKD instability. A 3D COMSOL
Helmholtz model and a 1D acoustic network model with mean flow place the
H2-injector first longitudinal (1L) mode at 10–12 kHz, which supports a
proposed "triple coupling": onset through the LOX-post 2L mode (as in the
type 1 instability), then, as amplitude raises the 1T frequency, coupling
with the H2-injector 1L mode.

# Key claims

1. **Type 2 characteristics** (§3.1). Peak frequencies 10.4–12.1 kHz
   depending on operating conditions; found in 6 test runs (liquid-hydrogen
   injection, and two gaseous-hydrogen runs only with shorter injectors).
   Amplitudes exceeded the ±30 bar (±3 MPa) sensor range, "equivalent to
   peak-to-peak values of up to 80% of PCC"; maximum RMS 18 bar (1.8 MPa)
   against about 3.4 bar (0.34 MPa) averaged RMS for type 1. Growth from
   stable to ±30 bar in under 5 ms (§1, Fig. 2). Shown.
2. **Injection pressure loss rises during instability** (§3.1, Fig. 8).
   Static chamber pressure drops 1–2% while manifold pressures rise, with no
   LOX-dome temperature change (not a density effect). The H2 manifold
   temperature rises 5–15 K (liquid H2) against about 2 K (gaseous H2) while
   the interface temperature stays nearly constant; the cause is unresolved.
   Shown.
3. **Acoustic field dynamics** (§3.2, Fig. 9). Low amplitude tends to a
   standing 1T mode, high amplitude to a fully spinning one; the frequency
   follows the amplitude with a slight lag, from about 9.5 kHz to almost
   12 kHz (over 25%); the reconstructed field stays 1T-like. Shown.
4. **No detonation-like waves** (§3.3, Fig. 10). A phase-locked cycle (200
   cycles, Run 1, 70 bar ROF 4, 6° bins, 7 sensors) gives an about 30 bar
   spinning field with a rise time close to 180° (50% of the period);
   detonation-like waves would rise in under 2% of the period. Shown for one
   load point and generalised to all type 2 load points.
5. **Normalized frequency shift** (§3.3, Eqs. 3–5, Fig. 11). The shift of
   the 1T frequency from its unperturbed value, normalized by the shift to
   the 1T frequency at the chemical-equilibrium (CEA) sound speed (0 =
   unperturbed flame, 1 = zero-length flame), is plotted against an acoustic
   velocity estimated from the plane-wave relation. A logistic fit
   (adjusted $R^2$ 0.6–0.76) gives similar curves for 70 bar ROF 4/5/6
   (liquid H2) and 80 bar ROF 6 (gaseous H2); the shift is attributed to
   flame retraction while the mode stays 1T. The amplitude–frequency lag is
   0.6–1.1 ms, 7–11 acoustic cycles. Fit shown; the flame-shortening
   mechanism is stated by analogy with BKH and numerical work, not observed
   (BKD has no optical access).
6. **NASA correlations fail** (§4.1, Figs. 12–13, Eq. 6, Table 1). All
   type 2 load points far exceed the critical velocity ratio 6.5 (Wanhainen
   et al. 1966), and stable points have similar ratios; all lie on the
   "stable" side of the Wanhainen et al. (1968) stability-limit parameter
   (limit 42.1 kg/(s·m^0.75)); H2 injection pressure drops of 15–40% are
   high, so the low-pressure-drop coupling of Hutt & Rocker does not account
   for the instability. Shown.
7. **H2-injector 1L mode in the instability range** (§4.3, Figs. 16–19).
   2D axisymmetric COMSOL single element: 9.8–11.9 kHz; 3D COMSOL full
   injector head: 10.4–12.7 kHz, mean error against the measured
   H2-manifold peak 4%, gaseous-H2 and transient points overestimated by
   2.6–7.6% (attributed to neglected flow, annulus Mach up to 0.4). The 1D
   network model with flow improves those points: four points of one run
   underpredicted by about 7%, the other five runs within 1% (steady) and
   about ±3.5% (transient); regression slope 0.97, $R^2=0.67$ over nine load
   points. Shown (model against experiment).
8. **Triple coupling** (§4.2, §4.4, Figs. 14, 20, 21). Before onset the 1T
   mode near 10 kHz is slightly excited with a LOX-manifold peak near
   10 kHz (LOX-post 2L); during the instability the chamber peak is at
   11.8 kHz with a matching H2-manifold peak. Probability distributions in
   the 9–12.5 kHz band show two chamber-frequency accumulations. The
   measured LOX-post frequency is 5–9% above the published 2L value. A
   necessary, not sufficient, condition is an unperturbed 1T close to the
   LOX-post 2L with the H2 1L slightly higher; on/off switching at constant
   conditions (Fig. 21, about 28 s) indicates a non-linear trigger.
   Hypothesis supported by data.
9. **Conclusion** (§5). Both BKD instability types are injection-coupled;
   the coupling depends on frequency matching between chamber and injectors,
   not on velocity ratio or fuel injection pressure drop.
10. **Rayleigh criterion** (§1, Eq. 1). Stated from Putnam & Dennis: the
    space–time integral of the product of pressure and heat-release
    fluctuations being non-negative is the instability condition.

# Methods

* **Facility** (§2.1, Figs. 3–4): BKD at P8 (Lampoldshausen); cylindrical
  chamber, inner diameter 80 mm, cylindrical segment 200 mm, throat
  diameter 50 mm, contraction ratio 2.56, characteristic length 0.64 m;
  water-cooled copper alloy; 42 shear-coaxial injectors with recessed,
  tapered LOX post, standard and shorter variants.
* **Operating range** (§2.3): chamber pressure 50–80 bar (5–8 MPa), mixture
  ratio 2–6; at 80 bar ROF 6: 6.7 kg/s total, thrust about 24 kN, thermal
  power 87 MW. H2 through a liquid interface (about 45 K) or a gaseous one
  (95–100 K), both supercritical; transient ramps 1.5–2 s.
* **Diagnostics** (§2.2): eight water-cooled Kistler 6043A dynamic sensors
  in a ring between injector head and chamber; 100 kHz sampling, 30 kHz
  anti-aliasing, ±30 bar range. Recessed manifold sensors; H2 tube transfer
  function from a model validated only to 4 kHz and extrapolated (gain 2–10
  at 9–13 kHz; H2 amplitude uncertainty near 10 kHz about 3 dB).
* **Signal processing**: Welch PSD (1 s, Hann 8192 samples, 4096 overlap);
  Hilbert transform on a 9–12.5 kHz band-pass; pressure-field
  reconstruction for the standing/spinning indicator; 6° phase-locking;
  cross-correlation for the lag; least-squares logistic fit.
* **Properties**: NASA CEA for equilibrium density, sound speed and 1T
  frequency; REFPROP for H2 and propellant sound speeds.
* **Acoustic models** (§4.3): COMSOL frequency-domain Helmholtz without
  mean flow (2D axisymmetric single element; 3D full injector head plus
  50 mm of chamber, 1.3 million tetrahedra after a convergence study, one
  sound speed per volume, chamber 1396 m/s); 1D plane-wave network model
  (Riemann invariants, transfer matrices, eigenfrequencies from the
  vanishing determinant of the system matrix, Eqs. 7–8) fed by a 1D
  adiabatic cold-flow solver with 100 nodes.

# Tests and results

Table 1, load points with type 2 instability (H2 pressure drop presumably
in % of chamber pressure; the unit is not defined):

| Run | Mode | $P_{CC}$ [bar] | ROF | H2 | Injectors | $\Delta p_{H2}$ [%] |
|---|---|---|---|---|---|---|
| 1 | steady | 70 | 3, 4, 5, 6 | liquid | original | 33, 26, 20, 15 |
| 2 | steady | 80 | 3 | liquid | original | 27 |
| 3 | transient | 80 | 2–3 | liquid | original | 40 |
| 4 | transient | 50–80 | 5 | liquid | original | 22 |
| 5 | steady | 80 | 6 | gaseous | short | 25 |
| 6 | steady | 80 | 6 | gaseous | short | 27 |

* Fig. 11 (read from the figure, approximate): acoustic-velocity factor up
  to about 600 m/s, normalized shift up to about 0.6; type 1 points below
  about 100 m/s.
* Fig. 14: 1T varies 9.6–12 kHz within the PSD window; chamber peak
  11.8 kHz during instability.
* §4.4: deviation of model from instability frequency: COMSOL −2.6 to
  +7.6%, network model −8.2 to +2.8%.
* Fig. 20: H2 peak at 11.7 kHz in Run 5, above the equilibrium-limit 1T.

# Notation map

The paper is outside the plasma-propulsion domain; the registry column
gives a [notation](/notation.md) symbol only where its registry meaning
fits, otherwise "words".

| Armbruster et al. (2018) | Registry | Note |
|---|---|---|
| $p'$, $\hat p'$ | words (pressure fluctuation, amplitude) | registry $p_s$ is a species pressure |
| $\dot q'$ | words (heat-release fluctuation) | **collision risk** with $\mathbf q_s$ (heat flux) |
| $P_{CC}$ | words (static chamber pressure) | |
| ROF | words (oxidizer-to-fuel mass ratio) | |
| $f$, $f_{1T}$, $f_{1T,CEA}$ | words (mode frequency) | **collision risk** with $f_s$ (distribution function) |
| $\eta_{\Delta f_{1T}}$ | words (normalized frequency shift) | **collision** with $\eta$ (thrust efficiency) |
| $u_{ac}$, $\hat u_{ac}$ | words (acoustic velocity) | |
| $\rho_0$, $c_0$ | words (mean density, sound speed) | **collision:** registry $c$ is the speed of light |
| $\phi_R$ | words (standing/spinning indicator) | **collision** with $\phi$ (electrostatic potential) |
| VR, $\Delta p_{H2}$, $w_{cr}$, $r_{O2}$ | words | |
| $f$, $g$ (Riemann invariants) | words | |
| $S(\omega)$, $\omega$ | words; $\omega$ | **collision risk:** $S$ is the particle shape function |
| $\theta$, $r$ | $\theta$, $r$ | cylindrical chamber coordinates |
| Ma | words (Mach number) | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Armbruster_Experimental_investigation_of_self-excited_combustion_instab.pdf`.
   * **Version.** Publisher's typeset version (Elsevier, © 2018 IAA), 13
     pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.057, printed on page 1
     and checked on Crossref (title, four authors, vol. 151, pp. 655–667
     match); issued and published-print 2018-10; Crossref has no online
     date, page 1 gives 20 July 2018 (received 6 February, revised 29 May,
     accepted 28 June 2018). Page 1 matches the filename title.
   * **How it was read.** Full text; equations from the rendered pages;
     figure values only where stated as read from the figure (Fig. 11).
     Grid-convergence numbers, solver settings and fitted parameters are
     not printed.
   * **Recorded as printed.**
     * Peak-to-peak amplitude given three ways: more than 75% of static
       chamber pressure (abstract), up to 80% (§3.1), up to 86% (§5).
     * Peak-frequency range 10.4–12.1 kHz (§3.1) against 10.8–12.1 kHz
       (§5).
     * COMSOL deviation "between 2.6 and 7.6%" overestimation (§4.3)
       against "about −2.6 to +7.6%" (§4.4): the sign of 2.6 differs.
     * Eq. 5: the subtracted term carries $e^{-x_1x_2}$, while the first
       term at zero velocity gives $e^{+x_1x_2}$, so the fitted shift at zero
       velocity is not $x_4$ as the text intends; the logistic denominators
       print "1 −" for the usual "1 +".
     * Eq. 6 has a stray "∗" after "2·"; Eq. 8 has stray "|" delimiters.
     * "Raleigh" for Rayleigh (§1).
     * Detonation exclusion shown at one load point and stated for all
       type 2 load points (§3.3).
     * Table 1 does not define the unit of the H2 pressure drop.
     * Ref. 43's first author printed "Poﬂike"; the text says Polifke et al.
   * **Reference list.** 44 printed entries (Crossref reference-count 44).
