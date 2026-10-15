---
type: Source
title: "Le May et al. (2018) — Space debris collision probability analysis for proposed global broadband constellations"
description: "Estimates with ESA's MASTER-2009 debris flux the collisions expected over a 5-year operational phase for the proposed OneWeb (720 satellites) and SpaceX (4591 satellites) constellations, classed by energy-to-mass ratio and trackability, finding at least one collision near-certain for both and a probability of at least one catastrophic collision of 5.0% for OneWeb and 45.8% for SpaceX under intermediate mitigation."
resource: "doi:10.1016/j.actaastro.2018.06.036"
source_kind: paper
authors: [Le May S., Gehly S., Carter B.A., Flegel S.]
year: 2018
venue: "Acta Astronaut. 151:445–455"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Le_Space_debris_collision_probability_analysis_for_proposed_glo.pdf"
tags: [context, space-debris, collision-probability, satellite-constellation, debris-environment-model]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper estimates the number of collisions, and the probability of at
least one, between debris and the satellites of the proposed OneWeb
constellation (720 satellites at 1200 km) and the proposed SpaceX
constellation (4591 satellites including spares, 1110–1325 km) during a
5-year operational phase. The debris flux comes from ESA's MASTER-2009
model under three future scenarios: business as usual (BAU),
intermediate mitigation (MIT1) and full mitigation (MIT2). It extends
the method of Radtke et al. (the paper's ref. [11]) in two ways:
collisions are classed by energy-to-mass ratio (catastrophic if
EMR ≥ 40 kJ/kg) and by trackability (non-trackable if the impactor
radius is below 5 cm), and a box-wing geometry built with MASTER's
oriented-surface option is used alongside the equivalent sphere. At
least one collision is near-certain for both constellations; under MIT1
the probability of at least one catastrophic collision is 5.0% for
OneWeb and 45.8% for SpaceX. The mitigation scenarios hardly change the
results, because MASTER phases the reductions in from 2020. The paper
also examines sensitivity to the EMR threshold, to satellite size and
count, and the long-term collision accumulation of satellites that fail
to deorbit. MASTER's flux carries no quantified uncertainty, and the
results are presented as mean collisional behaviour, not forecasts
(§5).

# Key claims

Symbols are the paper's own (see the notation map).

1. **Collision statistics** (§3.1, Eqs. 1–5, stated, from Radtke et al.
   and Klinkrad, refs. [11, 15]). Mean collisions per satellite
   $N_{sat}=F\,A_c\,T$ with sphere cross-section
   $A_c=\pi(r_{tar}+r_{imp})^2$; Poisson probability
   $P_{\geq1,sat}=1-e^{-N_{sat}}$; for the constellation
   $N_{const}=F\,A_c\,T\,\Sigma$ and $P_{\geq1,const}=1-e^{-N_{const}}$,
   $\Sigma$ the number of satellites.
2. **Classification** (§3.2, Eq. 6). $EMR=M_{imp}v_{rel}^2/(2M_{tar})$; a
   collision is catastrophic if EMR ≥ 40,000 J/kg (threshold attributed
   to McKnight et al., ref. [21]) and non-trackable if $r_{imp}<5$ cm,
   because only objects of 10 cm and larger are catalogued (ref. [22]).
   Impacts on solar panels are assumed never catastrophic.
3. **Panel cross-section** (§3.3, Eq. 7).
   $A_c=LW+\pi r_{imp}^2+2r_{imp}W+2r_{imp}L$ for a rectangular panel,
   exact only for normal impact; off-normal impacts are scaled by the
   slant angle, because MASTER gives the impact angle only relative to
   the surface normal.
4. **Headline numbers** (§4.1, Figs. 7–8, Table A.5). SpaceX under BAU,
   sphere model: $N_{const}$ (total) 304, probability of at least one
   catastrophic collision 0.468. Under MIT1: SpaceX total 267, OneWeb
   5.70. MIT1 and MIT2 cut SpaceX's total by about 12% relative to BAU;
   the catastrophic count improves by "less than 1%" (see Recorded as
   printed).
5. **Non-trackable collisions** (§4.1.2). Probability of at least one:
   0.996 for OneWeb, 1.000 for SpaceX.
6. **Geometry** (§4.1.3, Fig. 9). The box-wing model changes the results
   by about ±10% against the sphere: OneWeb total 5.70 → 6.31 (+10%),
   SpaceX 267 → 245 ("9%"). The statistical significance of the
   differences is left open.
7. **EMR threshold** (§4.2, Figs. 10–11). Raising the catastrophic
   threshold above 40 kJ/kg would not change the results significantly;
   only classing 0–5 kJ/kg as catastrophic would, since $N_{const}$ is an
   order of magnitude higher in that bin. Attributed to Pardini and
   Anselmo (ref. [5]): 3 of the 4 accidental collisions since 1990
   exceeded 40 kJ/kg yet together produced only 9 catalogued fragments.
8. **Size against count** (§4.3, Fig. 12). $N_{const}$ grows
   quadratically with $r_{tar}$ and linearly with satellite count. A
   SpaceX satellite of OneWeb's radius ("0.86 m") gives 36.2; a SpaceX
   constellation of 720 satellites gives 41.8. Smaller satellites are
   "marginally better" than fewer.
9. **Failed satellites** (§4.4, Figs. 13–14). If 10% of satellites fail
   to deorbit, total collisions after 50 years are about 35 (OneWeb) and
   about 250 (SpaceX), with fewer than one catastrophic on average;
   called optimistic because background flux and future launches are
   held fixed.
10. **Operators' figures** (§5). OneWeb's single-satellite probability is
    about 0.008 (MASTER, debris ≥ 3 mm) against 0.003 in OneWeb's own
    filing (ORDEM3, ≥ 1 cm); the paper says they "align well" given the
    different size floors. It reproduces SpaceX's "about 1% per decade"
    for a failed satellite against tracked debris (supporting result
    "not shown"), but adds a non-trackable probability of 0.124 after
    10 years.

# Methods

- **Debris environment**: MASTER-2009 flux (per m² per year) on the
  target orbits, debris ≥ 3 mm (ejecta, solid-rocket-motor slag, NaK
  droplets, explosion and collision fragments). The 3 mm floor assumes
  minimal shielding stops anything smaller; objects below 3 mm give 197
  impacts per m² per year on the OneWeb orbit and are excluded (§3.2).
- **Scenarios**: BAU (no mitigation); MIT1 (no mission-related objects,
  fewer explosion fragments and motor by-products); MIT2 (MIT1 plus 100%
  deorbit of rocket bodies and payloads within 25 years).
- **Geometry**: equivalent sphere (Tables 2–3: OneWeb average
  cross-section 2.35 m², equivalent radius 0.93 m, 150 kg; SpaceX
  17.99 m², 2.39 m, 386 kg; cross-sections from CROC in DRAMA 2.0), and
  an eight-panel box-wing model (Fig. 6) with nadir-pointing body and
  Sun-pointing arrays.
- **Constellations**: OneWeb 18 planes × 40 at 1200 km and 87.9°
  (Table 1). SpaceX (Table 4): 1664 satellites at 1150 km and 53°
  (initial), 1664 at 1110 km and 53.8°, 416 at 1130 km and 74°, 385 at
  1275 km and 81°, 462 at 1325 km and 70°, each shell with 2 spares per
  plane: 4425 plus 166 spares.
- **Time**: 5-year operational phase from 2018. Long-term analysis: the
  MIT1 annual $N_{sat}$ times the failed fraction (1%, 5%, 10%) of the
  constellation, over 0–50 years.

# Tests and results

Table A.5, sphere model unless stated; $P$ is the probability of at
least one collision.

| Case | Total | Catastrophic | Non-trackable | Catastrophic non-trackable |
|---|---|---|---|---|
| OneWeb BAU | 6.64 | 5.46E-02 ($P$ 5.32E-02) | 6.59 | 1.29E-02 |
| OneWeb MIT1 | 5.70 ($P$ 0.997) | 5.15E-02 ($P$ 5.02E-02) | 5.65 ($P$ 0.996) | 1.08E-02 |
| OneWeb MIT2 | 5.53 | 5.14E-02 ($P$ 5.01E-02) | 5.48 | 1.08E-02 |
| OneWeb MIT1 box-wing | 6.31 ($P$ 0.998) | 5.52E-02 ($P$ 5.37E-02) | 6.22 | 9.47E-03 |
| SpaceX BAU | 304 | 0.630 ($P$ 0.468) | 303 | 0.107 ($P$ 0.102) |
| SpaceX MIT1 | 267 | 0.613 ($P$ 0.458) | 266 | 9.71E-02 ($P$ 9.25E-02) |
| SpaceX MIT2 | 269 | 0.619 ($P$ 0.462) | 268 | 0.102 ($P$ 9.73E-02) |
| SpaceX MIT1 box-wing | 245 | 0.499 ($P$ 0.393) | 243 | 5.78E-02 ($P$ 5.62E-02) |

- Single satellite under MIT1: OneWeb $N_{sat}$ 7.91E-03 ($P$
  7.88E-03); SpaceX $N_{sat}$ 5.81E-02.
- Size and count sweep (Fig. 12, SpaceX, MIT1): 36.2 at
  $r_{tar}=0.86$ m, 41.8 with 720 satellites.
- Failed satellites (Figs. 13–14, MIT1, 10% failed, 50 years): about 35
  (OneWeb) and about 250 (SpaceX) in the text; the rendered Fig. 13
  curves end near 37 and about 270.

# Notation map

The paper's symbols are those of debris-risk analysis; none is a
plasma-propulsion quantity.

| Le May et al. (2018) | Registry | Note |
|---|---|---|
| $F$ | words (debris flux, per m² per year) | **collision:** registry $F$ is thrust |
| $A_c$ | words (combined collision cross-section) | |
| $T$ | words (operational lifetime) | **collision:** registry $T_s$ is temperature |
| $N_{sat}$, $N_{const}$ | words (mean number of collisions) | |
| $P_{\geq1,sat}$, $P_{\geq1,const}$ | words (Poisson probability of at least one collision) | same form as registry $P_c$, a different quantity (debris impact over a mission, not a per-step particle collision); not mapped |
| $\Sigma$ | words (number of satellites) | |
| $r_{tar}$, $r_{imp}$ | words (target and impactor radii) | not the radial coordinate $r$ |
| $L$, $W$ | words (panel length and width) | **collisions:** registry $L$ is a domain length, $W$ the macroparticle weight |
| $v_{rel}$ | words (impact relative speed) | registry $g$ is the relative speed of colliding gas particles; not mapped |
| $M_{imp}$, $M_{tar}$ | words (impactor and target masses) | |
| EMR | words (energy-to-mass ratio, J/kg) | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Le_Space_debris_collision_probability_analysis_for_proposed_glo.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier), 11 pages
     with Appendix A.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.036, printed on page 1
     and checked on Crossref: title, authors (S. Le May, S. Gehly, B.A.
     Carter, S. Flegel), Acta Astronaut. 151:445–455 match; issued
     2018-10, no published-online field. Page 1: received 28 Feb 2018,
     revised 11 Jun 2018, accepted 14 Jun 2018, online 19 Jun 2018.
     Page 1 matches the filename title. The archive filename gives the
     first author as "Le", but the surname is the two-word Le May (page 1
     and Crossref family name), so the slug is `lemay-2018`, not the
     `le-2018` first assigned from the filename (re-slugged in chunk 4).
   * **How it was read.** Full text layer; Eq. 6 and Figs. 4, 5, 12, 13
     checked on rendered pages 448 and 452. Figure values are recorded
     only where the text or Table A.5 also gives them.
   * **Recorded as printed.**
     * Table 2 gives OneWeb's equivalent radius as 0.93 m, while §4.3 and
       Fig. 12 use "0.86 m". Reader's check: the Table 2 cross-section
       gives $\sqrt{2.35/\pi}=0.865$ m, matching 0.86; the SpaceX entry
       is consistent ($\sqrt{17.99/\pi}=2.39$ m).
     * §2 lists a SpaceX shell at 1100 km; Table 4 has 1110 km.
     * §4.1 prints 0.103 for the SpaceX BAU catastrophic non-trackable
       probability; Table A.5 prints 1.02E-01.
     * Reader's check: the "less than 1%" improvement of catastrophic
       collisions (§4.1.1) is not a relative change in Table A.5 (SpaceX
       0.630 → 0.613 or 0.619, −2.7% and −1.7%; OneWeb about −6%); it
       holds only as an absolute probability difference (SpaceX 0.468 →
       0.458 or 0.462).
     * §4.1.3 gives a "9%" box-wing reduction for SpaceX; 267 → 245 is
       −8.2%.
     * Reader's check: the stated long-term method (MIT1 $N_{sat}$/5 ×
       50 years × 72 failed OneWeb satellites) gives about 5.7 collisions
       at 50 years, against about 35–37 in text and Fig. 13; the same
       arithmetic for SpaceX (459 satellites) gives about 267, matching
       the figure (about 270) but not the text's "~250". The paper does
       not explain the OneWeb factor of about 6.
     * Reader's check: the §5 non-trackable probability of 0.124 after 10
       years matches the BAU single-satellite value (6.60E-02 × 2 = 0.132,
       $P=0.124$), not MIT1 ($P\approx0.109$), although §§4.2–4.4 use
       MIT1; the scenario is not stated.
     * Ref. [7] (Matney, 2010) prints doi:10.1016/0094-5765(93)90151-L,
       which has the form of a 1993 Acta Astronautica DOI and cannot
       belong to a 2010 item; ref. [28] prints "doi:AAS 09–233", an AAS
       paper number. Neither is recorded as a DOI.
   * **Reference list.** 28 printed entries ([1]–[28]), matching the
     Crossref reference count. Refs. [9] (first author printed "B.B.
     Virgili") and [27] ("B. Bastida Virgili") name the same person and
     land under two surname spellings, left for the whole-corpus
     duplicate sweep.
