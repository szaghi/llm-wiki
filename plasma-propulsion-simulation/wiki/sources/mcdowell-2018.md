---
type: Source
title: "McDowell (2018) — The edge of space: Revisiting the Karman Line"
description: "Argues from history, upper-atmosphere physics, orbital data and a weight-to-drag ratio at circular orbital speed that the boundary of space lies near 80 km rather than 100 km, finding the effective Kármán line at 66–88 km for typical satellite ballistic coefficients and decaying satellites that survive several perigees below 100 km."
resource: "doi:10.1016/j.actaastro.2018.07.003"
source_kind: paper
authors: [McDowell J.C.]
year: 2018
venue: "Acta Astronaut. 151:668–677"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_McDowell_The_edge_of_space_Revisiting_the_Karman_Line.pdf"
tags: [context, karman-line, upper-atmosphere, orbital-decay, space-policy]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

McDowell re-examines where the boundary between Earth's atmosphere and
outer space lies, with historical, physical and technological arguments,
and argues for 80 km rather than the popular 100 km "von Kármán line".
§5 recasts von Kármán's criterion (orbital forces exceeding aerodynamic
forces) as the ratio $R$ of weight to drag for a body at circular
orbital speed, which depends only on the ballistic coefficient
$B=C_DA/m$, the geocentric radius and the air density. A logarithmic
"Karman parameter" $k=\log_{10}R$ is evaluated for its zero altitude with
the US Standard Atmosphere 1976 (USSA76) and with NRLMSISE-00 runs over
1960–2020. For typical satellites ($B$ = 0.005–0.05 m²/kg) the effective
Kármán line lies at 66–88 km. Two-line-element (TLE) data show
elliptical-orbit satellites surviving several perigees below 100 km,
some at 80–90 km. The paper also lists conventional boundaries in deep
space (LEO/MEO, GEO, an "EL1:4" resonance, the Hill sphere, the
asteroid belt, the heliopause). It is open access (CC BY 4.0).

# Key claims

Symbols are the paper's own (see the notation map).

1. **Thesis** (Abstract, §§1.1, 6, argued, shown numerically in §5.3). A
   moderately well-defined boundary of space exists; it coincides with
   the Kármán line as originally defined and lies near 80 km, not
   100 km.
2. **History** (§§1.3, 2). The USAF awarded astronaut wings for flights
   above 50 statute miles, within 500 m of 80 km. The "official" 100 km
   rests on an undated FAI/ICARE web paper (the paper's ref. [12]),
   called "poorly researched": the low-orbit satellite it describes is
   identified as Kosmos-149 (245 × 285 km, in orbit 21 Mar – 7 Apr 1967,
   last US data a 201 km circular orbit on 5 Apr). Under a 100 km limit,
   X-15 pilots White (95 km on 17 Jul 1962), Rushworth, McKay, Dana and
   Adams would lose space-traveller status.
3. **Atmospheric layers** (§3.1). Stratopause about 50 km, mesopause
   about 85–90 km, thermosphere about 85–500 km, turbopause about
   100–120 km. USSA76 fixes the mesopause at 86 km; TIMED/SABER data
   (Xu et al., ref. [15]) give 97 ± 2 km (equatorial and winter polar)
   and 86 ± 2 km (summer polar). The 118 km "edge of space" of Sangalli
   et al. (ref. [14]) is the ion-dynamics transition height and is said
   not to be a generic result.
4. **Technological lower limit** (§4.1). Air-breathing or lift-dependent
   vehicles reach about 50 km at most (Ye-266M 37.65 km, Helios 29 km,
   the ISAS BU60-1 balloon 53 km), so the stratopause (50 km) is a
   sensible lower limit.
5. **Lowest circular orbits** (§4.2). GAMBIT 4346 (1976-27A) held perigee
   125–135 km for a month; Lixing-1 held 124 × 133 km for 3 days
   (16–19 Aug 2016), stated as the lowest circular orbit sustained for
   several days. Hence 125 km is a conservative upper limit for the
   start of space.
6. **Lowest sustainable perigee** (§4.3). Perigee kept over more than two
   revolutions is the better criterion. In 90 million TLE sets for 43000
   satellites the author found 50 satellites keeping geodetic perigee
   below 100 km for 2 or more revolutions; Elektron (SSN 748) made about
   10 revolutions at or below 85 km, Centaur AV-031 (SSN 38255) kept
   perigee below 110 km for 4 days, 80–95 km for much of it. A perigee
   below 80 km makes completing the next orbit "highly unlikely";
   meteors usually disintegrate at 70–100 km.
7. **Perigee pitfalls** (§4.3). SGP4 mean-element perigee can differ from
   the osculating perigee by about 10 km; the spherical-to-ellipsoidal
   correction reaches 22 km at the poles (WGS-84 used); single element
   sets are suspect (Kosmos-168's 52 × 386 km on 4 Jul 1967 was an
   erroneous solution).
8. **Kármán ratio** (§5.1, Eqs. 1–5). Lift is $F=\tfrac12AC_L\rho v^2$ (Eq. 1)
   and drag has the same form with $C_D$; following Haley, drag replaces
   lift, and $R=W/F=mg/(\tfrac12AC_D\rho v^2)$, $g=GM_E/r^2$ and $v=\sqrt{GM_E/r}$
   reduce to $R=2/(Br\rho)$.
9. **Karman parameter** (§§5.1–5.2, Eqs. 6–9).
   $k=\log_{10}R=\log_{10}(2/(Br\rho))$; with fiducial $B_0=0.01$ m²/kg,
   $k=k_0-\log_{10}(B/B_0)$; $z(x)$ is the geodetic altitude where $k_0=x$
   and $z_B(x)=z(x+\log_{10}(B/B_0))$. The effective Kármán line is
   $z_B(0)$.
10. **Numbers** (§5.3). USSA76 gives $z(-0.3)=72.0$ km, $z(0.0)=76.7$ km,
    $z(0.7)=86.7$ km; the NRLMSISE-00 runs stay within about 5 km of
    USSA76, for an overall range of 66–88 km over a factor 10 in $B$.
    $z(0)$ lies in 70–90 km and "100 km is always too high".
11. **Elliptical orbits** (§5.4, Eqs. 10–11). At perigee
    $v=v_c\sqrt{1+e}$, so $R=2/(Br\rho(1+e))$: the line is "somewhat
    higher", tending to the circular value as drag circularises the orbit
    before reentry.
12. **Attribution** (§5.1). Haley (ref. [3], p. 78) placed the line at
    84 km; the paper suggests the name "von Karman-Haley line" and calls
    the von Kármán line a "folk theorem" never formally published by von
    Kármán (history after Gangale, ref. [44]).

# Methods

- **Kind of work**: a review and argument paper (historical, legal-policy
  and physical) with one semi-analytic model (§5) and an empirical data
  review (§4.3).
- **Model**: point-mass force balance at circular Keplerian speed in
  Newtonian gravity, without lift, Earth rotation or a co-rotating
  atmosphere; orbital flight only. Ascent and suborbital flight have
  lower speed, so their effective line is lower.
- **Atmospheres**: USSA76 (fixed reference, Fig. 2) and NRLMSISE-00
  every 10 days from Jan 1960 to Jan 2020, at 0, 6, 12, 18 h GMT, at
  latitudes 80° S, 0°, 45° N, 80° N and longitudes 0°, 90°, 180°, 270° E,
  with actual or predicted solar activity from the Celestrak
  space-weather archive. The NRLMSISE-00 code used is not named.
- **Orbital data**: US TLEs (SGP4 mean elements) federated with the
  author's satellite catalogue; perigee converted to osculating elements
  and then to geodetic height above WGS-84.
- **Ballistic coefficients** (§5.2): $C_D$ 2.0–2.4, typical $B$ about
  0.006–0.05 m²/kg; ISS 0.010 m²/kg (average area 2040 m²); Planet Dove
  0.01–0.1 depending on attitude; Echo about 22 m²/kg; LARES about
  0.001; LOADS 2 about 0.002 m²/kg; a hypothetical 10 m osmium sphere
  $8\times10^{-6}$ m²/kg.

# Tests and results

- **Fig. 1** (§4.3): geodetic apogee and perigee against time for six
  decaying elliptical-orbit objects (SSN 748, Molniya-3 No. 30,
  Kosmos-1518, Kosmos-2217, a CZ-3A third stage, Centaur AV-031), each
  surviving several perigees below 100 km.
- **Fig. 2**: $k_0$ against geodetic altitude for USSA76, with the NRL
  variation range as error bars.
- **Fig. 3** (45° N, 1960–2020, approximate readings): $z(4)$ about
  140 km and nearly flat; $z(5)$ about 180–215 km; $z(6)$ about
  230–340 km, varying strongly with the solar cycle.
- **Fig. 4**: $z(-0.3)$, $z(0.0)$, $z(0.7)$ against date per latitude;
  seasonal variation largest at the poles but only a few kilometres;
  solar flares have negligible effect.
- **Extremes** (§5.3): Echo about 140 km; LARES about 60 km; the osmium
  sphere at the tropopause; LOADS-type dense satellites reentered at
  perigee about 120 km.

# Notation map

The paper's symbols are those of flight mechanics; none is a
plasma-propulsion quantity.

| McDowell (2018) | Registry | Note |
|---|---|---|
| $m$, $A$, $C_L$, $C_D$ | words (spacecraft mass, area, lift and drag coefficients) | |
| $v$, $v_c$ | words (vehicle speed, circular orbital speed) | not the phase-space velocity $\mathbf v$ |
| $r$ | words (geocentric radius) | **collision:** registry $r$ is the radial coordinate of an axisymmetric thruster |
| $\rho$ | words (atmospheric mass density) | registry has charge density $\rho_c$ only |
| $G$, $M_E$, $g$ | words (gravitational constant, Earth mass, local gravity) | **collision:** registry $g$ is the relative speed of colliding particles |
| $F$, $W$ | words (aerodynamic force, weight) | **collisions:** registry $F$ is thrust, $W$ the macroparticle weight |
| $R$ | words (weight-to-drag ratio) | |
| $B=C_DA/m$ | words (ballistic coefficient; some authors use $1/B$) | **collision:** registry $\mathbf B$ is the magnetic field |
| $k$, $k_0$, $B_0$ | words (Karman parameter, its fiducial value, fiducial $B$) | **collision:** registry $k$ is a wavenumber |
| $z(x)$, $z_B(x)$ | words (geodetic altitude where $k_0=x$) | **collision:** registry $z$ is the axial coordinate |
| $e$ | words (orbital eccentricity) | **collision:** registry $e$ is the elementary charge |
| $\delta$ | words (fractional change of semi-major axis, footnote 1) | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_McDowell_The_edge_of_space_Revisiting_the_Karman_Line.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier, open access,
     CC BY 4.0), 10 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.07.003, printed on page 1
     and checked on Crossref: title, sole author, Acta Astronaut.
     151:668–677 match; issued 2018-10. Page 1: received 13 May 2018,
     accepted 1 Jul 2018, online 3 Jul 2018. Page 1 matches the filename
     title.
   * **How it was read.** Full text layer; Eqs. 1–11 checked on rendered
     pages 674 and 676. Figs. 1, 2, 4 were not rendered (content from
     captions and text); Fig. 3 values are approximate readings. The
     50-satellite list of §4.3 is not tabulated in the paper.
   * **Recorded as printed.**
     * Reader's check: footnote 1 (Reijnen criterion) states
       $\delta r=2\pi B\rho r^2$, so $\delta=2\pi B\rho r=4\pi/R$ by
       Eq. 5; the footnote writes "So $\delta=R$" and concludes $k=-2.7$
       ($\log_{10}0.002$ for $\delta=0.2\%$), whereas $\delta=0.002$ gives
       $R\approx6.3\times10^3$, $k\approx+3.8$. It also mixes "10% of
       height" with "about 0.2%" of radius, consistent only for a height
       near 130 km.
     * Reader's check: Echo's $z(1)$ (§5.3) does not follow from Eq. 8
       with $B\approx22$ m²/kg (§5.2), which needs
       $k_0=\log_{10}(22/0.01)\approx3.3$; the quoted "around 140 km" fits
       the $z(4)$ curve of Fig. 3. Either the label or the stated $B$ is a
       slip.
     * Reader's check: for the osmium sphere ($B=8\times10^{-6}$ m²/kg)
       Eq. 8 gives $k_0\approx-3.1$, not the printed $z(-4)$.
     * §4.3 calls SSN 748 "Elektron-4", reentered in 1997; the Fig. 1
       caption labels SSN 748 as "1964-006 B, Elektron 2, 2D No. 2".
     * §3.1 writes "mesosphere altitude of 97 ± 2 km" for the mesopause.
     * Stated disagreements with published work: the FAI/ICARE 100 km
       paper (ref. [12]), Oduntan's premise of a 150 km lowest perigee
       (ref. [18]), and Goedhart (ref. [2]), said to contradict himself on
       aeroplanes above 50 km; agreement in order of magnitude with Haley
       (ref. [3]).
     * Typos: "expressed my the same equation" (§5.1), "calcualted"
       (§5.3), "consquently" (§5.4), "fo the physical" (§1.2), "Modelss"
       (ref. [35]), lost diacritics in ref. [12].
   * **Reference list.** 44 printed entries ([1]–[44]), matching the
     Crossref reference count. Ref. [34] (McDowell, General Catalog of
     Space Objects, 2018, in preparation) has the same author-year as this
     source and is keyed with a suffix.
