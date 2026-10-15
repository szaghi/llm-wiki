---
type: Source
title: "Armbruster et al. (2018) — Experimental investigation of self-excited combustion instabilities with injection coupling in a cryogenic rocket combustor"
description: "Analyses a second, high-amplitude self-excited 1T instability (10.4–12.1 kHz) in DLR's 42-injector LOX/H2 combustor BKD, shows its frequency rising with amplitude in a way consistent with flame shortening, excludes detonation-like waves, shows that the NASA velocity-ratio and stability-limit correlations do not predict it, and proposes a triple coupling of the chamber 1T with the LOX-post 2L and hydrogen-injector 1L modes."
resource: "doi:10.1016/j.actaastro.2018.06.057"
source_kind: paper
authors: [Armbruster W., Hardi J.S., Suslov D., Oschwald M.]
year: 2018
venue: "Acta Astronaut. 151:655–667"
local_file: "/home/stefano/papers/mosaic/chemical-airbreathing-propulsion/2018_Crossref_Acta_Astronautica_Armbruster_Experimental_investigation_of_self-excited_combustion_instab.pdf"
tags: [combustion-instability, thermoacoustics, liquid-rocket-engine, injector-dynamics, acoustics, experiment]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper analyses a second ("type 2") self-excited high-frequency
instability in DLR's 42-element shear-coaxial LOX/H₂ research combustor BKD
at the P8 test facility, with peak-to-peak amplitudes of 75–86 % of the static
chamber pressure (the figure depends on the passage; see below). A
Hilbert-transform analysis of instantaneous amplitude and frequency and a
pressure-field reconstruction show the 1T mode switching between standing and
spinning, its frequency rising from about 9.5 kHz to almost 12 kHz with
amplitude. A phase-locked cycle shows a sinusoidal rise time (about 180°),
which excludes steep-fronted detonation-like waves. A normalized frequency
shift collapses the frequency rise against the transverse acoustic velocity
for all steady load points; by analogy with BKH optical results it is
interpreted as flame shortening raising the near-faceplate sound speed. The
classic NASA Lewis correlations (critical velocity ratio 6.5; stability-limit
parameter 42.1 kg/(s·m^0.75)) and the low-hydrogen-pressure-drop explanation
do not predict the instability. COMSOL Helmholtz models and a 1D acoustic
network model with mean flow place the hydrogen-injector 1L mode at
10–12 kHz, supporting a proposed triple coupling: onset through the LOX-post
2L mode, then, as amplitude raises the 1T frequency, lock-on to the
hydrogen-injector 1L mode.

# Key claims

1. **Type-2 instability** (§3.1, Fig. 2). Peak frequencies 10.4–12.1 kHz
   depending on operating conditions; occurred in 6 runs (liquid-hydrogen
   injection, and gaseous hydrogen only with the shorter injectors);
   amplitudes exceed the ±3 MPa (±30 bar) sensor range; maximum RMS 1.8 MPa
   (18 bar) against about 0.34 MPa (3.4 bar) averaged for type 1; growth from
   stable to saturation in under 5 ms. Shown.
2. **Injection pressure loss rises during instability** (§3.1, Fig. 8).
   Chamber pressure drops 1–2 % while manifold pressures rise; no LOX-dome
   temperature change, so not a density effect; hydrogen manifold
   temperature rises 5–15 K (liquid hydrogen) against about 2 K (gaseous)
   while the interface temperature is nearly constant; cause unresolved.
   Shown.
3. **Standing and spinning 1T** (§3.2, Fig. 9). Low amplitude tends to a
   standing mode, high amplitude to a fully spinning one; frequency follows
   amplitude with a slight lag from about 9.5 kHz to almost 12 kHz (more than
   25 %); the field stays 1T-like. Shown.
4. **No detonation-like waves** (§3.3, Fig. 10). Phase-locked over 200
   cycles (Run 1, 7 MPa, $O/F$ = 4, 6° bins, 7 sensors since one was
   damaged): spinning field of almost 3 MPa with a rise time close to 180°;
   detonation-like waves would rise in under 2 % of the period. Shown for one
   load point, generalized to all type-2 load points.
5. **Normalized frequency shift** (§3.3, Eqs. 3–5, Fig. 11). Defined against
   the zero-amplitude and chemical-equilibrium 1T frequencies; logistic fit
   with adjusted $R^2$ 0.6–0.76; similar curves across 70 bar $O/F$ = 4, 5, 6
   (liquid hydrogen) and 80 bar $O/F$ = 6 (gaseous hydrogen); lag of
   frequency behind amplitude 0.6–1.1 ms, 7–11 acoustic cycles (BKH: about 5
   measured, 15 computed, attributed). Fit shown; flame-shortening mechanism
   stated by analogy to BKH and numerical work.
6. **NASA correlations fail** (§4.1, Figs. 12–13, Eq. 6, Table 1). All
   type-2 points far exceed the critical velocity ratio 6.5 while stable
   points have similar ratios; all lie on the "stable" side of the
   stability-limit parameter (limit 42.1 kg/(s·m^0.75)); hydrogen injection
   pressure drops of 15–40 % are relatively high, so the Hutt & Rocker
   low-pressure-drop coupling does not account for it. Shown.
7. **Hydrogen-injector 1L in the instability range** (§4.3, Figs. 16–19).
   2D COMSOL 9.8–11.9 kHz; 3D COMSOL 10.4–12.7 kHz, mean error 4 % against
   the measured hydrogen-manifold peak, gaseous-hydrogen and transient points
   overestimated by 2.6–7.6 %; 1D network model with flow improves these,
   regression slope 0.97, $R^2$ = 0.67 over nine load points. Shown.
8. **Triple coupling** (§4.2, §4.4, Figs. 14, 20, 21). Onset via LOX-post 2L
   coupling, then lock-on to the hydrogen-injector 1L; chamber peak 11.8 kHz
   with a matching hydrogen-manifold peak during instability; measured
   LOX-post frequency 5–9 % above the published 2L; a non-linear trigger is
   required. Hypothesis supported by data.
9. **Conclusion** (§5). Both BKD instability types are injection-coupled;
   coupling depends on chamber–injector frequency matching, not on the
   velocity ratio or the fuel injection pressure drop.
10. **Rayleigh criterion** (§1, Eq. 1). Stated, after Rayleigh and Putnam &
    Dennis.

# Methods

* **Facility.** BKD at P8, Lampoldshausen: chamber inner diameter 80 mm,
  cylindrical length 200 mm, throat 50 mm, contraction ratio 2.56,
  characteristic length 0.64 m; water-cooled copper alloy; 42 shear-coaxial
  injectors with recessed, tapered LOX posts, standard and shorter variants
  (§2.1, Figs. 3–4).
* **Operating range.** $p_c$ = 5–8 MPa, $O/F$ = 2–6; at 8 MPa, $O/F$ = 6:
  6.7 kg/s, about 24 kN, 87 MW thermal. Hydrogen through a liquid interface
  (about 45 K) or gaseous interface (95–100 K), both supercritical, on
  different sides of the hydrogen Widom line; transient ramps of 1.5–2 s
  (§2.3).
* **Diagnostics.** Eight water-cooled Kistler 6043A dynamic sensors in a ring
  between injector head and chamber, 100 kHz sampling, 30 kHz anti-aliasing,
  ±30 bar range; recessed manifold sensors with a modelled tube transfer
  function (gain 2–10 in 9–13 kHz, absorption coefficient validated only to
  4 kHz; about 3 dB uncertainty near 10 kHz) (§2.2, Figs. 5–6).
* **Signal processing.** Welch spectra (1 s, Hanning, 8192 samples, 4096
  overlap, dB re 80 bar); Hilbert transform with 9–12.5 kHz band-pass;
  pressure-field reconstruction for the spin ratio; 6° phase-locking;
  cross-correlation; logistic least squares; error bars from signal standard
  deviation and Gaussian propagation (§3, §4.1).
* **Properties.** CEA for chamber density, sound speed and equilibrium 1T
  frequency; REFPROP for propellant sound speeds (Fig. 15).
* **Acoustic models** (§4.3). COMSOL frequency-domain pressure acoustics
  without mean flow: 2D axisymmetric single hydrogen element with one
  forty-second of the manifold volume; 3D full injector head with LOX-post
  centring fins plus 50 mm of chamber, rigid walls, 1.3 million tetrahedra
  after a mesh-convergence study (numbers not given), constant sound speed
  per volume (chamber 1396 m/s). 1D network model: plane-wave Riemann
  invariants, transfer matrices after Polifke et al., eigenfrequencies from
  the zero determinant of the system matrix (Eqs. 7–8), mean flow from a 1D
  adiabatic cold-flow solver with 100 axial nodes and REFPROP properties,
  open-end boundaries.

# Tests and results

Table 1, load points with the type-2 instability (hydrogen pressure drop in
%, presumably of $p_c$):

| Run | Mode | $p_c$ (bar) | $O/F$ | Hydrogen | Injectors | Hydrogen pressure drop (%) |
|---|---|---|---|---|---|---|
| 1 | steady | 70 | 3 | liquid | original | 33 |
| 1 | steady | 70 | 4 | liquid | original | 26 |
| 1 | steady | 70 | 5 | liquid | original | 20 |
| 1 | steady | 70 | 6 | liquid | original | 15 |
| 2 | steady | 80 | 3 | liquid | original | 27 |
| 3 | transient | 80 | 2–3 | liquid | original | 40 |
| 4 | transient | 50–80 | 5 | liquid | original | 22 |
| 5 | steady | 80 | 6 | gas | short | 25 |
| 6 | steady | 80 | 6 | gas | short | 27 |

* Fig. 7: stable, type-1 (about 10 kHz, LOX-post related) and type-2 (broad
  peak about 11 kHz) spectra.
* Fig. 11: normalized shift up to about 0.6 at acoustic velocities up to
  about 600 m/s; type 1 at small velocities (below about 100 m/s) and small
  shift (read from the figure).
* Fig. 14: spectra before (13.5–13.9 s) and during (14.2–14.6 s) instability;
  chamber peak 11.8 kHz; 1T between 9.6 and 12 kHz within the window.
* §4.4: deviation of model from instability frequency, COMSOL −2.6 to
  +7.6 %, network model −8.2 to +2.8 %.
* Fig. 20: Run 5 hydrogen peak 11.7 kHz, above the equilibrium-limit 1T;
  spacing of chamber 1T maximum to hydrogen peak about 5 % in the gaseous
  case.
* Fig. 21: switching between LOX-2L-locked and hydrogen-1L-locked states;
  intermittent on/off near 28 s.

# Notation map

| Armbruster et al. (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p'$, $\hat p'$ | $p'$; words (amplitude) | the hat (amplitude) is not registered |
| $\dot q'$ | $\dot q'$ | fluctuation of $\dot q$; prime as in $p'$ (not separately registered) |
| PCC | $p_c$ | static chamber pressure |
| ROF | $O/F$ | |
| $T_{H2}$ | words | hydrogen injection temperature |
| $f$, $f_{1T}$ | $f$; words for the mode label | 1T, 1L, 2L labels in prose |
| $f_{1T,CEA}$ | words | 1T frequency at equilibrium sound speed |
| $\eta_{\Delta f_{1T}}$ | words (normalized frequency shift) | **collision risk** with $\eta_c$ |
| $u_{ac}$, $\hat u_{ac}$ | words (acoustic velocity) | |
| $\rho_0$, $c_0$ | $\rho$; words (mean sound speed) | subscript 0 means mean, not total |
| $\phi_R$ | words (spin ratio) | **collision** with $\phi$, equivalence ratio |
| VR | $\mathrm{VR}$ | |
| $\Delta p_{H2}$ | words (hydrogen injection pressure drop) | |
| $w_{cr}$ | words (stability-limit parameter) | |
| $r_{O2}$ | words (oxidizer-post exit radius) | |
| $f$, $g$ (Riemann invariants) | words | **collision** with $f$, frequency |
| $S(\omega)$ | words (network system matrix) | |
| $T$ (period, Fig. 10 text) | words | **collision** with $T$, temperature |
| Ma | $\mathrm{Ma}$ | |

# Pages created or updated

Chunk 2 (2026-10-14) created every page of the bundle. This source is cited on:

* [High-frequency combustion instability in liquid rocket engines](/definitions/combustion-instability.md)

# Citations

1. `/home/stefano/papers/mosaic/chemical-airbreathing-propulsion/2018_Crossref_Acta_Astronautica_Armbruster_Experimental_investigation_of_self-excited_combustion_instab.pdf`.
   * **Version.** Publisher's typeset version (Elsevier, © 2018 IAA), 13 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.057, printed on page 1 and
     checked on Crossref: title, four authors, vol. 151, pp. 655–667 match;
     issue 2018-10; Crossref has no online date, page 1 gives 20 July 2018
     (received 6 Feb 2018, revised 29 May 2018, accepted 28 Jun 2018). Page 1
     matches the filename title. The file was first filed in the
     plasma-propulsion archive; the paper has no plasma content.
   * **How it was read.** Full text; equations from rendered pages; plot
     values beyond the text are approximate readings (Fig. 11). Fitted
     parameters of Eq. 5, grid-convergence numbers, solver settings and the
     network transfer matrices are not given.
   * **Recorded as printed.**
     * Peak-to-peak amplitude given three ways: "more than 75 %" of the
       static chamber pressure (abstract), "up to 80 %" (§3.1), "up to 86 %"
       (§5).
     * Peak-frequency range 10.4–12.1 kHz in §3.1, 10.8–12.1 kHz in §5.
     * The COMSOL deviation is "between 2.6 and 7.6 %" overestimation in
       §4.3 and "about −2.6 to +7.6 %" in §4.4; the sign of 2.6 differs.
     * Eq. 5: the subtracted term uses $e^{-x_1x_2}$, whereas evaluating the
       first term at zero amplitude gives $e^{+x_1x_2}$, so the fit is not
       zero at zero amplitude as the text intends; the logistic denominators
       read "1 −" rather than "1 +". Reproduced as read; not resolvable from
       the paper.
     * Eq. 6 has a stray "∗" after "2·"; Eq. 8 has stray "|" delimiters.
     * "Raleigh" for Rayleigh (§1).
     * Table 1 does not state the reference of the hydrogen pressure drop
       percentage.
     * The detonation exclusion is shown for one load point and generalized
       to all type-2 load points (§3.3).
   * **Reference list.** 44 printed entries (Crossref reference-count 44).
     Ref. [43] prints the first author as "Poﬂike"; the text says Polifke et
     al. Same first author and year twice: jensen-1989 / jensen-1989-b,
     armbruster-2016 / armbruster-2016-b, webster-2016 / webster-2016-b,
     groning-2017 (CEAS) / groning-2017-b (thesis).
