---
type: Source
title: "Yamaguchi et al. (2018) — Hayabusa2-Ryugu proximity operation planning and landing site selection"
description: "Describes the pre-arrival plan for Hayabusa2's proximity operations at asteroid Ryugu (Home Position frame, descent sequences, schedule drivers) and the joint landing-site selection process for the touchdown and the MASCOT/MINERVA-II robots, with the ion-engine cruise status as of March 2018."
resource: "doi:10.1016/j.actaastro.2018.05.032"
source_kind: paper
authors: [Yamaguchi T., Saiki T., Tanaka S., Takei Y., Okada T., Takahashi T., Tsuda Y.]
year: 2018
venue: "Acta Astronaut. 151:217–227"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Yamaguchi_Hayabusa2-Ryugu_proximity_operation_planning_and_landing_sit.pdf"
tags: [context, mission-operations, small-body-mission, sample-return, landing-site-selection]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

A mission-operations planning paper written before arrival (status as
of March 2018). It describes how JAXA's Hayabusa2 was to operate near
asteroid (162173) Ryugu and how the landing sites were to be chosen. It
defines the Home Position (HP) frame and the operation sequences: HP
observation at 20 km, mid-altitude observation at 5 km, a gravity
measurement, two touchdown (TD) rehearsals, the TD itself and the
deployment of the MASCOT and MINERVA-II surface robots. Three uncertain
asteroid parameters drive the schedule: gravity, thermal environment
and spin-axis orientation. The paper then presents the "joint" landing
site selection (LSS): the decision and data flow between JAXA
engineering, the science team and the DLR/CNES MASCOT team, a
"safety score" map, and an integrated LSS dry-run held April–September
2017. Electric propulsion enters only as mission context: the
spacecraft cruises on its ion engine system (IES), four ion engines of
10 mN each, and by March 2018 the IES had operated about 3900 h for
about 580 m/s of velocity increment. The paper has no equations, no
plasma content and no simulation with quantitative results.

# Key claims

Operating figures are as printed by the authors; none is derived here.

1. **Spacecraft** (§2, design data, stated): wet mass 609 kg, dry mass
   493 kg; main box 1.0 × 1.6 × 1.3 m. Four ion engines of 10 mN each,
   "20% larger thrust than Hayabusa", able to accelerate the spacecraft
   "up to 3.2 km/s with 66 kg of xenon fuel". Twelve chemical RCS
   thrusters of 20 N each; four reaction wheels (three on Hayabusa);
   X- and Ka-band high-gain antennas.
2. **Cruise and ion-engine operations** (§3, reported operations data):
   launch on 3 Dec 2014 on an H2A, with launch characteristic energy
   21 km²/s². The mission lasts 6 years: 3.5 years inbound, 1.5 years of
   proximity operations, 1 year outbound. 7000 h of IES operation are
   planned (stated both as the round-trip total and as the time to reach
   Ryugu; see Recorded as printed). 547 h of IES operation were completed before
   the Earth gravity assist (EGA). EGA closest approach was on
   2015-12-03 at 10:08 UTC, at 3090 km altitude over the Pacific. The
   first EGA trajectory-correction manoeuvre was made with the IES three
   months before EGA; TCM1 (30 days before) and TCM2 (7 days) used the
   RCS; TCM3 (2 days) was cancelled. As of March 2018 the first and
   second IES sessions lasted 798 h and 2558 h; the total IES time was
   about 3900 h, for about 580 m/s of velocity increment; the third IES
   session ran January–June 2018.
3. **Home Position frame** (§4.1, Fig. 3, definition): origin at Ryugu;
   $Z_{HP}$ points from the Ryugu centre to Earth;
   $Y_{HP}=Z_{HP}\times$ (asteroid-to-Sun vector);
   $X_{HP}=Z_{HP}\times Y_{HP}$ (as printed). The Sun always lies in the
   $+X_{HP}$ half-space. The nominal station is $(0,0,20\ \mathrm{km})$.
   There is no orbiting (weak gravity, limited RCS accuracy) and no
   excursion to $-Z_{HP}$ except during the small carry-on impactor
   (SCI) operation.
4. **Operations** (§§4.2–4.7, planned): station keeping once per day
   in the UDSC ground-station pass. Mid-altitude observation at 5 km by
   ground-control-point navigation (GCP-NAV): ground in the loop, LIDAR
   for the vertical, ground-based lateral navigation, round-trip light
   time up to 40 min, a manoeuvre every 2 or 10 min. ONC-T field of view
   5.7° × 5.7°. Gravity measurement to 3% accuracy by free fall from
   5 km to 1 km and ascent; the nominal expected gravity coefficient is
   32 m³/s². Two TD rehearsals to 50 m, 6 weeks and 1 week before TD. TD
   descent of about 17 h, ending with an autonomous phase of about
   10 min that uses a target marker. MASCOT release at a nominal trigger
   altitude of 60 m, then 24 h at 3 km to keep the communication link.
5. **Schedule drivers** (§5, stated/planned): the gravity coefficient is
   assumed in 11–92 m³/s² (bulk density 430–3600 kg/m³). Larger gravity
   costs more fuel per descent and allows fewer descents: at 92 m³/s²,
   two TDs and one rehearsal. The thermal constraint restricts the TD
   epoch to October 2018–May 2019, which corresponds to a solar distance
   of 1.25 AU (a lower bound on the solar distance). Guidance limits
   descents to within 200 m of the asteroid–Earth line, so the
   accessible latitude band depends on the spin-axis orientation and
   changes with the orbital motion (Figs. 8–9). TD1 is placed just
   before conjunction, at the end of 2018.
6. **Joint landing-site selection** (§6, Figs. 12–14, stated): the
   spacecraft TD sites and the MASCOT/MINERVA-II landing sites must not
   overlap, because the guidance could mistake a robot for a target
   marker and abort. The authors present this simultaneous selection as
   the main difference from the Rosetta/Philae LSS [22,23]. Primary and
   secondary site pairs must be decided by mid-August 2018, about one
   month after instrument checkout (mid-July 2018). A "safety score",
   a weighted sum of sub-Earth distance, local slope, local solar angle,
   local surface temperature and boulder distribution, is computed per
   shape-model polygon and mapped (Fig. 14); the weights are not given.
   The MASCOT flight-dynamics team computes landing dispersion by Monte
   Carlo analysis of the bouncing trajectories [24].
7. **Dry-run** (§§6–7, reported qualitatively): the integrated LSS
   dry-run of April–September 2017, on an artificial Ryugu model,
   refined the workflow. No quantitative outcome is reported.

# Methods

Operations planning and process design: no mathematical model, no
equation, no numerical scheme, no code. Navigation relies on GCP-NAV
[21], optical navigation with the ONC-W1 and ONC-T cameras, LIDAR and
laser range finder ranging, and ground radiometric ranging. The safety
score is described only as "a weight sum of the parameters". The MASCOT
landing-dispersion Monte Carlo of descent and bouncing dynamics is
cited [24], not shown.

# Tests and results

There is no test case with quantitative results. The only exercise is
the LSS integrated dry-run (April–September 2017), described in words;
Fig. 14 shows a safety-score map from it, without tabulated values. The
operational numbers reported are the ion-engine hours and velocity
increment and the EGA closest approach (Key claim 2).

# Notation map

The paper uses almost no symbols; its quantities are named in words.

| Yamaguchi et al. (2018) | Registry | Note |
|---|---|---|
| ion engine thrust (10 mN per engine) | $F$ | thrust |
| $X_{HP}$, $Y_{HP}$, $Z_{HP}$ | words (Home Position frame axes) | mission-specific frame |
| gravity coefficient (m³/s²) | words (asteroid gravitational parameter) | |
| C3 (km²/s²) | words (launch characteristic energy) | |
| velocity increment (m/s) | words | the registry has no velocity-increment symbol |
| RTLT | words (round-trip light time) | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Yamaguchi_Hayabusa2-Ryugu_proximity_operation_planning_and_landing_sit.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier, IAA
     copyright), 11 pages (217–227).
   * **Identity.** doi:10.1016/j.actaastro.2018.05.032, printed on page 1
     and checked on Crossref: title, all seven authors, Acta Astronaut.
     151:217–227 match; issue October 2018 (published-print 2018-10);
     page 1 gives received 29 Jan 2018, revised 30 Apr 2018, accepted
     15 May 2018, online 16 May 2018. Page 1 matches the filename title
     and first author.
   * **How it was read.** Full text layer, clean. The paper has no
     equations. Figs. 1–14 (spacecraft, trajectory, frame, sequences,
     schedules, LSS flow, safety-score map) are images; their content is
     recorded only through captions and text, as no number in the text
     depends on them.
   * **Recorded as printed.**
     * §3 gives 7000 h of IES operation once as the round-trip total
       (citing ref. [19]) and once as the time "to reach Ryugu"; recorded
       as printed.
     * §1 announces "Section 4 summarize the timeline…, Section 5 explain
       the joint landing site selection…, Section 6 concludes"; the paper
       has §4 operations, §5 schedule, §6 joint LSS, §7 conclusions.
     * §4.1 defines $X_{HP}$ as the "cross product of the ZHP and YHP";
       recorded as printed.
     * Ref. [22] (Ulamec et al.) is printed as Acta Astronaut. 207 (2015)
       79–86; Crossref gives "Rosetta Lander – Philae: Landing
       preparations", Acta Astronaut. 107:79–86 (2015),
       doi:10.1016/j.actaastro.2014.11.019, so the printed volume is a
       misprint.
     * Ref. [9] (Senshu et al., dust detection mode of the Hayabusa2
       LIDAR) is printed with pages 49–64, identical to ref. [8]; Crossref
       gives Space Sci. Rev. 208:65–79 (doi:10.1007/s11214-016-0242-7).
     * Refs. [12]–[16] print no volume (Space Sci. Rev. (2017) and
       pages); vol. 208 follows from the special issue, not printed.
     * Ref. [1] is printed "Proceedings of 28th International Symposium
       on Space Technology and Science, 2011 2011-k-19".
   * **Reference list.** 24 printed entries ([1]–[24]), matching the
     Crossref reference count.
