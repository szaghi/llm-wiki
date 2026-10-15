---
type: Source
title: "Conte & Spencer (2018) — Mission analysis for Earth to Mars-Phobos distant Retrograde Orbits"
description: "Designs impulsive transfers from low Earth orbit and from a lunar distant retrograde orbit to Mars-Phobos distant retrograde orbits, with a four-impulse arrival sequence and patched-conic Lambert legs over the 2020–2042 synodic periods, finding minimum total velocity increments of 5.1856 km/s from LEO and 2.7317 km/s from the lunar orbit."
resource: "doi:10.1016/j.actaastro.2018.06.049"
source_kind: paper
authors: [Conte D., Spencer D.B.]
year: 2018
venue: "Acta Astronaut. 151:761–771"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Conte_Mission_analysis_for_Earth_to_Mars-Phobos_distant_Retrograde.pdf"
tags: [context, mission-analysis, astrodynamics, mars, phobos, distant-retrograde-orbit, three-body-problem]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

An astrodynamics paper designing trajectories from low Earth orbit (LEO)
to a Mars-Phobos distant retrograde orbit (DRO), computed as periodic
orbits of the Mars-Phobos circular restricted three-body problem (CR3BP),
with a lunar DRO as an alternative departure point. Interplanetary legs
use patched conics and Lambert solutions on JPL DE430 ephemerides over
the 2020–2042 synodic periods (porkchop plots). The arrival is a
five-phase, four-impulse concept of operations: capture into a
400 × 75,000 km orbit, an apoareion plane change with periareion raise,
a phasing orbit, and DRO insertion; phases 1–4 use two-body dynamics and
phase 5 the CR3BP. The minimum total velocity increment from LEO to a
DRO with $A_x=30$ km is 5.1856 km/s (2041–2042), and from a lunar DRO as
low as 2.7317 km/s (2035–2036). The authors argue that a DRO "pit stop"
with refuelling lowers the initial mass in LEO and the gear ratio,
although the total velocity increment to low Mars orbit rises. All
manoeuvres are impulsive; the paper has no plasma or electric-propulsion
content.

# Key claims

Symbols are the paper's own (see the notation map).

1. **No Keplerian orbits about Phobos** (§1, attributed to ref. [2]):
   Phobos' sphere of influence lies below its surface; CR3BP periodic
   orbits (Lyapunov, halo, DRO) exist, and DROs are the stable family far
   enough from the surface.
2. **DRO stability** (§2, attributed to ref. [2]): DROs with $A_x>20$ km
   stay stable for over 60 days under full-force models without control;
   smaller ones need stationkeeping every 1–2 h of order cm/s. DROs with
   $A_x<15$ km collide with Phobos at once; the paper considers
   $A_x\in[15,300]$ km.
3. **Four-impulse arrival** (§3, Figs. 5–7, Table 3, shown by
   computation): the DRO is reached within 2 days of entering Mars'
   sphere of influence; for $v_\infty=2.543$ km/s, $i=20.93$°,
   $\alpha=15$°, $A_x=300$ km: total 1.5316 km/s, time of flight 1.18 days.
   Impulses (Eqs. 2–5): $\Delta V_1=|v_{1,p}-v_{2,p}|$,
   $\Delta V_2=\sqrt{v_{2,a}^2+v_{3,a}^2-2v_{2,a}v_{3,a}\cos i}$,
   $\Delta V_3=|v_{3,p}-v_{4,p}|$, $\Delta V_4=|v_{4,p}-v_{p,DRO}|$.
4. **Two-body approximation** (§3, Fig. 10, shown): Phobos' gravity
   perturbs phases 1–4 by at most 10–100 m in most $(A_x,\alpha)$ cases;
   near $\alpha\simeq0$ Phobos dominates and the approximation fails.
5. **Phasing** (§3, Eq. 6, Fig. 9): the phasing angle $\alpha$ affects
   only the time of flight of phase 5, not the velocity increment for
   given $v_\infty$, $i$, $A_x$; more phasing orbits $N$ do not lengthen
   the phasing time significantly. Eq. 6 is dimensionally inconsistent as
   printed (see Citations).
6. **LEO to DRO** (§4, Table 4, shown): per-synodic-period minima for
   $A_x=30$ km from a 300 km LEO; global minimum 5.1856 km/s
   (2041–2042, 315 d).
7. **DRO size** (§4, Fig. 15): raising $A_x$ from 30 to 300 km lowers the
   arrival velocity increment by "up to approximately 100 m/s".
8. **Lunar DRO departure** (§4, Table 5): lunar DRO ($A_x=61500$ km) to
   Mars-Phobos DRO ($A_x=30$ km), minimum 2.7317 km/s (2035–2036), "as
   little as two fifths" of a direct LEO to low-Mars-orbit transfer; the
   direct-transfer figure is not given. Stated.
9. **Conclusion** (§5, argued): Mars-Phobos DROs need a smaller velocity
   increment per mission segment than direct low-Mars-orbit arrival,
   reducing Earth-launched dry mass; no mass calculation is presented.

# Methods

* **Dynamics:** Mars-Phobos CR3BP, mean distance 9376 km, mass ratio
  $1.6610\times10^{-8}$; 1 LU = 9376 km, 1 TU = 4387 s, primaries' period
  7.657 h (Table 2). Phobos' inclination (1.093°) set to zero; its
  eccentricity is 0.0151 (Table 1).
* **DRO generation:** initial conditions at the $y=0$ crossing (periapse
  distance and velocity) chosen for periodicity (Fig. 4); the
  differential-correction scheme, integrator and tolerances are not
  described.
* **Interplanetary legs:** impulsive manoeuvres, patched conics, Lambert
  solutions, JPL DE430 ephemerides; other bodies' perturbations neglected
  inside Mars' sphere of influence. Frames: J2000 ecliptic to Earth mean
  equator (obliquity 23.43928°) to Mars mean equator by direction cosine
  matrices (Eq. 1); B-plane analysis (Fig. 12); RAAN set to zero to keep
  the patched-conic problem determined.
* **Arrival sequence** (§3): hyperbola targeting a 400 km periareion;
  capture into 400 × 75,000 km; plane change to zero inclination at
  apoareion with periareion raise to $(5980-r_{p,DRO})$ km altitude;
  phasing orbit; DRO insertion. One phasing orbit by default.

# Tests and results

* **Arrival example** (Table 3; departure 27 Jun 2035, sphere-of-influence
  arrival 15 Jan 2036): $r_{p,DRO}=298$ km, $v_{p,DRO}=0.1376$ km/s
  (relative to Phobos); impulses 0.7481, 0.1503, 0.3479, 0.2854 km/s;
  total 1.5316 km/s; 1.18 days; phasing apoareion altitude 17,254 km.
* **LEO to DRO, $A_x=30$ km** (Table 4; times include a conservative
  2-day arrival phase): 2020–21 5.5285 km/s, 207 d; 2022–23 5.6533,
  343 d; 2024–25 5.5279, 237 d; 2026–27 5.3489, 309 d; 2028–29 5.4369,
  301 d; 2030–31 5.7098, 285 d; 2032–33 5.6778, 205 d; 2035–36 5.2120,
  204 d; 2037–38 5.5269, 351 d; 2039–40 5.4540, 330 d; 2041–42 5.1856,
  315 d. Fig. 14 (2035–2036 contour) shows its period minimum 5.2120 km/s.
* **Arrival vs DRO size** (Fig. 15, figure reading): from about
  1.61 km/s at $A_x\approx15$ km to about 1.53 km/s at 300 km, roughly
  linear.
* **Lunar DRO to DRO** (Table 5): 2020–21 3.1115 km/s, 217 d; 2022–23
  3.7795, 245 d; 2024–25 3.9210, 267 d; 2026–27 3.8333, 294 d; 2028–29
  3.0988, 302 d; 2030–31 4.6486, 188 d; 2032–33 3.5602, 230 d; 2035–36
  2.7317, 205 d; 2037–38 3.3872, 239 d; 2039–40 3.7780, 254 d; 2041–42
  3.5128, 283 d. Lunar departure windows last about two days per month.

# Notation map

Astrodynamics symbols; none maps to the registry.

| Conte & Spencer (2018) | Registry | Note |
|---|---|---|
| $\Delta V$, $\Delta V_k$, $\Delta V_{tot}$ | words (velocity increment) | |
| $v_\infty$, $C_3$ | words (hyperbolic excess speed, characteristic energy) | |
| $\lambda$ | words (CR3BP mass ratio) | **collision** with $\lambda_D$, $\lambda_{\mathrm{mfp}}$, $\lambda_w$ |
| $\mu_{Mars}$ | words (gravitational parameter) | **collision** with $\mu_0$, $\mu_\perp$, $\mu_\parallel$ |
| $n_{Phobos}$ | words (mean motion) | **collision:** registry $n_s$ is number density |
| $\alpha$ | words (phasing angle) | **collision** with $\alpha_{\mathrm B}$, $\alpha_E$, $\alpha_\tau$, $\alpha_n$ |
| $i$ | words (inclination) | **collision:** subscript $i$ denotes ions |
| $N$ | words (number of phasing orbits) | |
| $A_x$, $r_{p,DRO}$, $v_{p,DRO}$, $v_{y0}$, $h_{phasing}$, $a_{phasing}$ | words (DRO and phasing-orbit geometry) | |
| $m_1$, $m_2$, $m_3$, $\vec r_1$, $\vec r_2$, LU, TU | words (CR3BP masses, positions, canonical units) | |
| $\varepsilon_\oplus$ | words (Earth obliquity) | **collision** with $\varepsilon_0$, $f_\varepsilon$ |
| $R^{Ecl-EME}$, $R^{EME-MME}$, $\hat B$, $\hat S$, $\hat T$, $\hat R$ | words (rotation matrices, B-plane unit vectors) | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Conte_Mission_analysis_for_Earth_to_Mars-Phobos_distant_Retrograde.pdf`.
   * **Version.** Publisher's final typeset version (Elsevier, © 2018
     IAA), 11 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.049, printed on p. 761
     and checked on Crossref: title, both authors, Acta Astronaut.
     151:761–771 match; issued and published-print 2018-10, no
     published-online field. Page 1: received 21 Feb 2018, revised 6 Jun
     2018, accepted 24 Jun 2018, online 20 Jul 2018. Page 1 matches the
     filename title.
   * **How it was read.** Full text layer; Eqs. 2–5 read from the
     rendered page. No passage illegible. Fig. 15 values are approximate
     readings.
   * **Recorded as printed.**
     * Eq. 6,
       $a_{phasing}=\big[\frac{1}{n_{Phobos}}\big(N+\frac{2\pi-\alpha}{2\pi}\big)\big]^{3/2}\frac{1}{\mu_{Mars}}$,
       is dimensionally inconsistent. Reader's check: Kepler's third law
       with period $T=(N+(2\pi-\alpha)/(2\pi))\,2\pi/n_{Phobos}$ gives
       $a=[\mu_{Mars}(T/2\pi)^2]^{1/3}$ (exponent 2/3, $\mu^{1/3}$); applied
       literally, the printed formula cannot give the 17,254 km phasing
       altitude. A per-orbit division by $N$ would also be expected if $T$
       is the total phasing time; not verifiable.
     * Lunar-DRO minimum: §4 (p. 769) gives 2.362 km/s for departure
       23 Jun 2035, arrival 12 Jan 2036, 203/205 d, while Table 5 and the
       text on p. 770 give 2.7317 km/s for the same dates and times.
     * The paragraph introducing Table 5 (pp. 769–770) refers to "Table 4"
       and LEO departures; it should be Table 5 and lunar-DRO departures.
     * Reader's check: Fig. 15 shows a drop of about 70–80 m/s from
       $A_x=30$ to 300 km, against the text's "approximately 100 m/s".
     * The abstract's lower initial mass in LEO and the "two fifths"
       comparison are stated without any mass calculation or direct-transfer
       figure.
     * Fig. 14's 5.2120 km/s is the 2035–2036 minimum, not the global one
       (5.1856 km/s, 2041–2042); consistent, easy to misquote.
     * Ref. [14] (Clohessy–Wiltshire) is printed "Aerospace Science 29
       (1960) 653–658"; the paper is usually cited as J. Aerosp. Sci. 27(9)
       (not checked on Crossref). Ref. [9] prints 2017 for Acta Astronaut.
       143 (the February 2018 volume, online 2017). Ref. [3] prints its DOI
       as "doi:/10.1007/s10569-017-9798-0" (stray slash) and no year.
     * The paper states no conflict with published work.
   * **Reference list.** 20 printed entries ([1]–[20]), matching the
     Crossref reference count.
