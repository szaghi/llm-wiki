---
type: Source
title: "Ghassabian et al. (2018) — ALCIDES: A novel lunar mission concept study for the demonstration of enabling technologies in deep-space exploration and human-robots interaction"
description: "A desk-study concept for a crewed and tele-robotic lunar south-polar mission to the Amundsen-Ganswindt basin within the HERACLES architecture, with four traverses, a three-phase launch plan and a qualitative EML2-relay communication architecture; no propulsion, plasma or numerical content."
resource: "doi:10.1016/j.actaastro.2018.06.004"
source_kind: paper
authors: [Ghassabian G.H., Calzada Diaz A., Hettrich S., De Quattro N., Antonello A., Bielicki D.]
year: 2018
venue: "Acta Astronaut. 151:270–283"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Hady_ALCIDES_A_novel_lunar_mission_concept_study_for_the_demonstr.pdf"
tags: [context, mission-analysis, lunar-exploration, human-robotic-operations, lunar-communications]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

A mission-concept study, prepared for the ESA Moon Challenge
(Acknowledgements), of a crewed and robotic lunar surface mission named
ALCIDES. It sits inside the HERACLES architecture (Orion, the Small
Exploration Vehicle SEV, a Boeing reusable lander, Ariane 6, Falcon Heavy,
SLS) and assumes an Evolvable Deep-Space Habitat (eDSH) at the Earth–Moon L2
point (EML2). The landing site is the Amundsen-Ganswindt basin (81°S 120°E),
chosen for possible cold traps and permanently shadowed regions and for its
proximity to the Schrödinger basin. Four traverses are planned, three by a
tele-operated rover and one by a crew in the SEV with rover support; the
mission runs in three phases with four launches and three landings. A
qualitative communication architecture (EML2 halo-orbit relay; UHF, VHF, S
and X/Ka links) closes the paper. There are no equations, no simulation and
no experiment, and nothing on propulsion or plasma.

# Key claims

1. **Objectives** (§4.1–4.2): primary, the study of cold-trap volatiles,
   highlands geology and human–robotic operations; secondary, the Lunar
   Cataclysm Hypothesis and the radiation impact on astronauts. Stated.
2. **Site** (§5.2, Fig. 1): the Amundsen-Ganswindt basin (an unofficial
   name), about 335 km in diameter, pre-Nectarian. The authors' preliminary
   analysis of M3 strip M3G20090529T100749_V01_RFL shows OH signatures at
   points A, B, C, D1 and E and orthopyroxene (noritic) features at A, B, C,
   D2 and E (Fig. 2, Fig. A4). Shown only as spectral profiles, without
   quantitative analysis.
3. **Basin-wall composition** (§5.2, attributed to refs. [7,8]): a
   Clementine-derived FeO enhancement of 7–10 wt% fits a mix of 20–30%
   quenched South Pole–Aitken impact melt with 70–80% low-Fe highland
   material.
4. **Traverses** (§6): traverse 1 circular from landing site A, about
   160 km; traverse 2 about 119 km, ending at B; traverse 3 about 107 km,
   ending at C; traverse 4 crewed (SEV plus rover), about 85 km, designed to
   work even if the rover is lost. Design rules: slopes below 20° and
   avoidance of obstacles larger than 0.5 m (the LROC NAC resolution).
5. **Sample masses** (Table 1, following CAPTEM 2007, ref. [10]): 30, 30, 30
   and 147 kg for traverses 1–4.
6. **Mission plan** (§7.2, Figs. 12–15, 17): launch 1, Falcon Heavy
   (lander, rover, penetrator); launch 2, SLS + Orion (crew of 4); launch 3,
   Ariane 6 (SEV to point C); launch 4, SLS + Orion (crew of 4). In Phase 3
   one crew member stays in the eDSH and three land; the SEV and rover remain
   at C for later missions.
7. **Communications** (§8): an EML2 relay cuts the link range from about
   385000 km (direct to Earth) to about 65000 km (to an L2 halo orbit),
   lowering the surface power demand; the one-way light delay including the
   relay path is about 1.7 s. The halo orbit should stay above 10° elevation
   over 80°–90° S for seven continuous days per halo period, which narrows
   the choice to two halo orbits. Stated; no link budget is computed.

# Methods

A desk study. Datasets (§6): LROC-WAC (100 m/pixel), LROC-NAC (0.5 m/pixel,
via LROC Quickmap), LOLA (30 m/pixel), M3 (10 nm spectral, 70 m/pixel
spatial resolution) and the Diviner cold-trap map of Paige et al. (2010,
ref. [6]); slope map and traverses made in ArcGIS v.10.1 (Fig. A1).
Instruments (Table 2), with mass, power and data-rate limits per instrument:
XRD/XRF, gamma-ray/neutron spectrometer, APXS, ground-penetrating radar
(below 3.5 kg, below 7.8 W, 44.5 kbps), MastCam-like and close-up cameras on
the rover; nine DoseGUARD S dosimeters of 0.08 kg each; portable mass
spectrometer, drill (200 W for 5–10 min), optical microscope and HD cameras
on the SEV. The communication design (§8.1) is descriptive: dual helical
rover/SEV antennas (UHF A/B, steerable high gain plus omni low gain), a VHF
A/B duplex link between habitat and SEV, a relay multiplexing UHF and
sending to Earth over S band (TT&C, backup) and X or Ka band (payload), a
low-gain handshake for tracking data, and GNSS-SDR tracking at 65000 km
altitude (ref. [18]).

# Tests and results

None numerical or experimental. The results are the M3 spectral
identifications (Fig. 2, Fig. A4), the slope map (Fig. A1), the traverse
maps (Figs. 3, A2, A3) and the design tables. Reader's check: the Table 1
sums are consistent (T1 2+10+8+10 = 30 kg; T2 4+10+6+10 = 30 kg; T3 15+5+10
= 30 kg; T4 20+90+10+10+17 = 147 kg).

# Notation map

| Ghassabian et al. (2018) | Registry | Note |
|---|---|---|
| (none) | words | The paper has no equations or symbols; its quantities (link range in km, delay in s, mass in kg, power in W, data rate in kbps) are written in plain units. Nothing maps to or collides with the registry. |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Hady_ALCIDES_A_novel_lunar_mission_concept_study_for_the_demonstr.pdf`.
   * **Version.** Publisher's typeset version of record (Elsevier), 14
     pages; clean text layer.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.004, printed on page 1
     and checked on Crossref: title, Acta Astronaut. 151:270–283 match;
     issued 2018-10, no issue number, no published-online field. Page 1:
     received 2 Feb 2017, revised 28 May 2018, accepted 3 Jun 2018, online
     8 Jun 2018. Page 1 matches the filename title. **Author names:** the
     byline prints all six names surname-first ("Ghassabian G. Hady,
     Calzada Diaz Abigail, Hettrich Sebastian, De Quattro Nicola, Antonello
     Andrea, Bielicki Damian"); the corresponding e-mail is
     hady.ghassabian@…, and ref. [18] prints "N. De Quattro". The running
     head and the corresponding-author line give "G.G. Hady", and Crossref
     deposits all six names with given and family swapped (author 1: given
     "Ghassabian G.", family "Hady"; author 2: given "Calzada Diaz", family
     "Abigail"; likewise "Sebastian", "Nicola", "Andrea", "Damian").
     The archive filename follows the publisher ("Hady"). This page reads
     the byline surname-first for all six authors, so the first author is
     Ghassabian and the slug is `ghassabian-2018` (re-slugged from
     `hady-2018`); read with its systematic swap, the Crossref record supports
     this reading, and only the running head and the corresponding-author
     line read "Hady" as the surname.
   * **How it was read.** Full text layer. Figs. 4–16 are artist
     renderings without data; Figs. A1–A4 are images whose spectral and
     slope values are not tabulated and were not digitised. Footnotes 3 and
     4 (on the Fig. A3 and A4 captions) have no text in the text layer.
   * **Recorded as printed.**
     * In-text citations [11]–[17] (§§5.2, 7.1, 8) are shifted by one
       against the list: the text cites [11] for the NRC SCEM goals (list
       [12]), [12] for the HERACLES elements (list [13], the GER near-term
       scenario paper), [13] for the eDSH (list [14]), [14] for the
       Lagrange-point definition (list [15], HyperPhysics), [15] for the
       lunar L2 navigation paper (list [16], Hill et al.), [16] for the
       Opportunity rover (list [17]) and [17] for the GNSS-SDR demonstration
       (list [18], Pirazzi, De Quattro, Dionisio). List [11] (the CAPTEM
       website, whose printed title drops "Curation and") appears to have
       been inserted late. The Fig. 20 caption's [16] correctly matches
       Hill et al.
     * §6 says the cold traps were observed by "the Diviner and the M2
       instruments [6]": M3 is meant, and ref. [6] (Paige 2010) covers
       Diviner only.
     * §8 calls Lagrange points places where a small body "can maintain a
       stable position", then calls EML2 "radially unstable"; the collinear
       points are in fact unstable.
     * §8 places Schrödinger and Amundsen "on the far side of the Moon";
       both are south-polar, and the paper elsewhere motivates the relay by
       south-pole visibility.
     * Ref. [8] mixes a journal citation (Earth Planet. Sci. Lett.
       427:31–36, 2015) with a conference-abstract label ("Early Sol. Syst.
       Impact Bombardment III … Abstract #3035"); Crossref resolves it to
       the EPSL paper.
     * Ref. [12] gives the NRC SCEM report the venue "Bull. Am. Astron.
       Soc. 38 (2007)", kept as printed.
     * Typos: "knowledge gas" (gap), "Boing", "in-site" (in situ).
   * **Reference list.** 22 printed entries ([1]–[22]); Crossref deposits
     20 (it leaves out printed [4] and [15]). DOIs are printed only for
     [7] and [21]. Entries without a printed author are keyed by
     organisation (ISECG, CAPTEM, NRC, the IAC-15 paper), entries without
     a printed year with `-nd` (the CAPTEM, NASASpaceflight, HyperPhysics
     and Luxorion web pages, and Lewis, printed "n.d.").
