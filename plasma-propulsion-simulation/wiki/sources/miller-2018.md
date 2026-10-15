---
type: Source
title: "Miller et al. (2018) — Comparison of the space bubble detector response to space-like neutron spectra and high energy protons"
description: "Calibrates space-type superheated-drop bubble detectors in a space-like spallation neutron spectrum at LANSCE (scaling factor 1.78 to the AmBe calibration) and in 30–226 MeV proton beams, finding no Bragg-peak enhancement and a proton sensitivity comparable to the neutron sensitivity above about 13 MeV."
resource: "doi:10.1016/j.actaastro.2018.05.035"
source_kind: paper
authors: [Miller A., Machrafi R., Benton E., Kitamura H., Kodaira S.]
year: 2018
venue: "Acta Astronaut. 151:1–6"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Miller_Comparison_of_the_space_bubble_detector_response_to_space-li.pdf"
tags: [context, space-radiation, dosimetry, bubble-detector, calibration]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper reports ground calibration of "space-type" superheated-drop
bubble detectors (BTI, 10 ml active volume, about $10^4$ droplets) like
those flown on the ISS (Matroshka-R, Radi-N). Neutron exposures on the
LANSCE 30L (ICE House) spallation beamline (0.6–800 MeV) are compared
with the dose equivalent computed from the measured spectrum and ICRP74
coefficients; they give a scaling factor of 1.78 (range 1.5–2.2) to
correct the AmBe-based calibration for space-like hard neutron spectra.
Proton exposures at ProCure (78.2, 162 and 226 MeV, three orientations)
and NIRS (30–70 MeV, with absorbers) give the proton sensitivity as a
function of energy. The bubble density does not increase at the Bragg
peak, so the authors infer that bubbles come from high-LET secondary
recoils of nuclear reactions, not from direct proton ionization. Above
about 13 MeV the proton sensitivity is comparable to the neutron
sensitivity measured earlier by others. The work presented at IAC 2017
is purely experimental; modelling is deferred.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Neutron scaling factor** (§3.1, Fig. 8). For 8 detectors at LANSCE
   30L, the AmBe-calibrated reading $H_{eq}=N_b/S_{AmBe}$ (Eq. 1)
   under-measures the spectrum-computed dose equivalent
   $H_{eq}=\sum_i h_i(E)\Phi_i(E)$ (Eq. 2); weighted-average scaling factor
   1.78, individual values 1.5 to 2.2, compared by the authors with 1.62
   for commercial detectors (their ref. [6]). Shown (measured).
2. **No Bragg-peak enhancement** (§3.2, Fig. 10). With the Bragg peak
   inside the sensitive volume (52 MeV, NIRS) the bubble distribution
   stays uniform along the track. Inferred: bubbles form only above an LET
   threshold exceeding the maximum proton LET, from high-LET secondary
   recoils of nuclear interactions with C, O, Cl and Cs nuclei of the
   medium.
3. **Orientation** (§3.2, Fig. 9). At 78.2, 162 and 226 MeV the parallel,
   45° and perpendicular orientations show "no significant differences" in
   sensitivity. Shown, weakly (see Recorded as printed).
4. **Energy dependence** (§3.2, Fig. 11, Eq. 3). The normalized proton
   sensitivity $S_p$ rises from 30 to 50 MeV (peak about
   $2.7\times10^{-5}$ bubbles per proton cm⁻² near 45–50 MeV, read off the
   figure), falls steeply above 50 MeV and keeps decreasing (about
   $2\times10^{-6}$ at 226 MeV, read off the figure). That this tracks the
   proton reaction cross sections is stated; no cross-section data are
   shown.
5. **Comparison with neutrons** (§3.3, Fig. 13). Below about 13 MeV,
   protons cannot penetrate the 2 mm plastic tube; above 13 MeV the proton
   sensitivity is "comparable" to the mono-energetic neutron sensitivity of
   the authors' ref. [3]. Fig. 13 shows proton points of about
   $2\times10^{-6}$ to $3\times10^{-5}$ against a neutron curve of about
   $10^{-5}$ to $3\times10^{-5}$ over 10–300 MeV (read off the figure).
6. **Out-of-beam counts** (§3.2, Table 1, 78.2 MeV). In-beam 243 ± 16
   bubbles at a fluence of $(2.363\pm0.236)\times10^7$ protons cm⁻²; 3
   bubbles at 40 cm and 1 at 300 cm, attributed to scattered secondary
   neutrons (stated).

# Methods

* **Detectors** (§2.1): BTI space-type bubble detectors, 10 ml active
  volume, about $10^4$ droplets, AmBe sensitivity 100–200 bubbles/mSv; the
  polymer is firmer than in commercial units, so bubbles grow more slowly.
  Bubbles are counted with a BTI BDR-III reader (optical unit, frame
  grabber, software).
* **Neutrons** (§2.2): LANSCE spallation source, 800 MeV pulsed proton
  linac on a tungsten target, neutrons 0.6–800 MeV; the 30L beamline (ICE
  House) chosen for its space-like spectral shape, measured by time of
  flight (Fig. 4); fission-foil ionization-chamber monitor; fluence about
  $10^6$ neutrons cm⁻²; detectors exposed singly or in sets of three.
* **Protons, ProCure** (§2.3): cyclotron with range shifter (about
  60–230 MeV); 78.2, 162 and 226 MeV in three orientations; detectors at
  the isocentre and at 40 cm and about 300 cm lateral for neutron
  contamination; 150–300 bubbles per detector; counting at least 30 min
  after exposure, 30 min rest after decompression before re-use.
* **Protons, NIRS** (§2.3): 70 MeV cyclotron; about 30–70 MeV with
  water-equivalent absorbers; fluences 0.5–$8\times10^6$ protons cm⁻²; ten
  experiments. Individual absorber thicknesses and energies are not
  reported.
* **Normalization** (Eq. 3):
  $S_p=N_b/\bigl(\Phi\cdot S_{AmBe}/(0.1\ \text{bubbles}/\mu\text{Sv})\bigr)$,
  in bubbles per proton cm⁻², normalized to a 0.1 bubbles/µSv detector.
  AmBe calibration at the BTI neutron facility with the ISO AmBe spectrum
  (Fig. 7).
* No transport or Monte Carlo simulation.

# Tests and results

* **LANSCE 30L, 8 detectors** (Fig. 8): measured (AmBe-calibrated) dose
  equivalent about 1800–2700 µSv against the spectrum-computed
  2800–5300 µSv (read off the figure); scaling factor 1.78 (1.5–2.2).
* **ProCure, 20 detectors** (Fig. 9), fluences 2–$4.5\times10^7$
  protons cm⁻² (§3.2): sensitivity about 0.85–$1.05\times10^{-5}$ at
  78 MeV, 4.2–$5.3\times10^{-6}$ at 162 MeV, 3–$5\times10^{-6}$ at 226 MeV,
  in bubbles per proton cm⁻² (read off the figure).
* **NIRS, 30–70 MeV** (Figs. 10–11): at 52 MeV the Bragg peak lies inside
  the medium, at 70 MeV beyond the detector (proton range 5 cm); bubble
  density uniform in both. Normalized sensitivity (read off Fig. 11):
  about $1.6\times10^{-5}$ at 33 MeV, $2.7\times10^{-5}$ at 47 MeV,
  $2.3\times10^{-5}$ at 60–65 MeV, $1.2\times10^{-5}$ at 70 MeV,
  $5\times10^{-6}$ at 78 MeV, $2.5\times10^{-6}$ at 162 MeV,
  $2\times10^{-6}$ at 226 MeV.
* **Table 1** (78.2 MeV): as in claim 6. **Fig. 13**: proton points
  against the neutron response curve of ref. [3], 0.1–300 MeV.

# Notation map

The paper is outside the bundle's domain; its symbols are kept in words.

| Miller et al. (2018) | Registry | Note |
|---|---|---|
| $H_{eq}$ | words (ambient dose equivalent, µSv) | **collision:** registry $H$ is spectral entropy |
| $N_b$ | words (bubble count) | |
| $S_{AmBe}$ | words (AmBe neutron sensitivity, bubbles/µSv) | **collision** with $S_j$ (Sobol' index) and $S(\mathbf x)$ (shape function) |
| $S_p$, $S_p(E)$ | words (normalized proton sensitivity) | same $S$ collision |
| $\Phi$, $\Phi_i(E)$ | words (particle fluence, cm⁻²) | not the electrostatic potential $\phi$ |
| $h_i(E)$ | words (ICRP74 fluence-to-dose coefficient) | |
| $E$ | words (particle kinetic energy, MeV) | **collision** with the electric field $\mathbf E$ |
| LET | words (linear energy transfer) | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Miller_Comparison_of_the_space_bubble_detector_response_to_space-li.pdf`.
   * **Version.** Publisher's final typeset PDF, 6 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.05.035, printed on page 1
     and checked on Crossref: title, the five authors, Acta Astronaut.
     151:1–6 match; published in print October 2018. Page 1 gives received
     27 Feb 2018, revised 10 May 2018, accepted 18 May 2018, online 19 May
     2018. Page 1 matches the filename title.
   * **How it was read.** Full text layer; Eqs. 1–3 read from rendered
     pages 3–4, legible. The figures carry no tabulated data: every value
     recorded as read off a figure is a visual reading at 110 dpi and
     approximate. The online supplementary material was not read.
   * **Recorded as printed.**
     * Series order: the abstract calls the NIRS series (30–70 MeV) the
       second and ProCure the third; §2.3 calls ProCure the second and NIRS
       the third; §3.2 calls NIRS the "second series of proton
       experiments".
     * ProCure fluence: 2 to about $15\times10^7$ protons cm⁻² in §2.3,
       2 to $4.5\times10^7$ in §3.2.
     * Range of comparability with neutrons: the conclusions say "in the
       range of 30–80 MeV", §3.3 says above 13 MeV with no upper limit,
       and the NIRS series spans 30–70 MeV, not 80. Reader's check: in
       Fig. 13 the 162 and 226 MeV proton points lie roughly 4–5 times
       below the neutron curve.
     * Reader's check: in Fig. 9 at 226 MeV the 45° point (about
       $4.9\times10^{-6}$) is about 1.5 times the parallel and
       perpendicular points (about 3.2–$3.4\times10^{-6}$), with
       non-overlapping error bars, against the "no significant
       differences" of §3.2.
     * §3.2 mentions "a total of four experimental sessions" but describes
       only the ProCure set and the NIRS series.
     * §3.2 says the sensitivity varies "proportionally" with the reaction
       cross sections of C, O, Cl and Cs without showing cross-section
       data; whether the medium contains Cs is not checkable from the
       paper.
     * The conclusions call 30–230 MeV protons "relativistic" (reader's
       check: $\beta\approx0.25$–0.59).
     * Eq. 2 is labelled "dose to fluence conversion coefficient"; the
       inverse is meant, as §3.1 itself says two sentences later.
   * **Reference list.** 10 printed entries, matching the Crossref
     reference count.
