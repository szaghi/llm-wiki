---
type: Source
title: "Fedele & Mungiguerra (2018) — Aerodynamics and flight mechanics activities for a suborbital flight test of a deployable heat shield capsule"
description: "Reports the flight-mechanics and aerodynamic work for MINI-IRENE, a suborbital demonstrator of a capsule with a deployable umbrella heat shield: a validated 3-DoF trajectory model predicting suborbital and LEO re-entry loads, and a preliminary aerodynamic database across free-molecular, transitional and continuum regimes built from DSMC, a Knudsen bridging function and Navier–Stokes and Newtonian methods, with static stability and trim."
resource: "doi:10.1016/j.actaastro.2018.05.044"
source_kind: paper
authors: [Fedele A., Mungiguerra S.]
year: 2018
venue: "Acta Astronaut. 151:324–333"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Fedele_Aerodynamics_and_flight_mechanics_activities_for_a_suborbita.pdf"
tags: [context, reentry, capsule, flight-mechanics, dsmc]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper reports the flight-mechanics and aerodynamics work for
MINI-IRENE, the suborbital Flight Demonstrator (FD) of the IRENE capsule,
whose umbrella-like mechanically deployable heat shield lowers the
ballistic coefficient to cut peak heat flux and mechanical loads. A 3-DoF
point-mass trajectory model (US1976 atmosphere, Tauber stagnation-point
heating, Newtonian stagnation pressure) is validated against a DLR VSB-30
reference trajectory (errors below 0.5%, impact point about 100 m) and
used to predict the capsule's re-entry after release from a VSB-30
(MAPHEUS-type) flight from ESRANGE, its offset from the rocket's main
payload, and a LEO re-entry used to size a SCIROCCO plasma-wind-tunnel
test of a Ground Demonstrator. A preliminary aerodynamic database (AEDB)
covers all flow regimes: DSMC in free-molecular flow, a sin²-of-log-Knudsen
bridging function in transitional flow, Navier–Stokes and engineering
methods (Newtonian blunt-cone formula, panel methods) in continuum flow,
for angles of attack 0–180°. Static stability and trim are read from the
pitching-moment curves in each regime. Much of the content is
programmatic and preliminary; the quantitative contributions are the
trajectory loads and the AEDB.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Ballistic coefficient** (§1, Eq. 1): $B=m/(C_DA)$. Lower $B$ reduces
   peak stagnation pressure and heat flux and moves the peaks higher
   (Fig. 2, illustrated). Quoted values: Apollo CM about 350 kg/m², Space
   Shuttle about 430 kg/m², IRENE target 25 kg/m². Stated.
2. **Drop tests** (§2, Fig. 6; shown): a 1.5× downscaled 3D-printed model
   ($B$ about 4× lower than MINI-IRENE, centre of mass at about 40% of
   length) dropped from 15 m and 300 m self-aligned with the flow in about
   2.5 s from initial angles of attack of 90° or 180°, with terminal
   velocity 12.5 m/s.
3. **Earlier CFD/DSMC** (§2, refs. [14, 15]; stated): a 45° half-cone
   aero-brake is more statically stable than a 60° one (which decelerates
   more); transonic high-incidence unsteady CFD shows periodic loads
   (Fig. 5), relevant to buffeting.
4. **Mission** (§3, Figs. 7–8): release from the VSB-30 payload stage after
   second-stage burnout (59 s, about 72.5 km); apogee about 250 km; landing
   860 s after separation; open shield 76 cm in diameter. The VSB-30 flight
   cannot load the thermal protection enough, hence a plasma-wind-tunnel
   test for TRL 6; the VSB-30 aerodynamic environment is "very close" to LEO
   entry, MAXUS is aerodynamically too severe and still short of LEO fluxes
   (stated from analyses).
5. **Trajectory-model validation** (§4): 3-DoF, lift neglected, zero
   incidence, US1976, Tauber heating, Newtonian stagnation pressure
   $\rho_\infty V_\infty^2$; from second-stage separation (60 s), errors on
   altitude, velocity, dynamic pressure and duration below 0.5%, impact
   point about 100 m off. Shown.
6. **Suborbital re-entry** (§4.1, Figs. 10–17; shown): separation at
   T0+75 s, 100.87 km, 1718.26 m/s (including a 1 m/s separation impulse),
   flight-path angle 83.7°, azimuth 107.69°; mass 8 kg; area 0.0491 m²
   closed until apogee and 0.342 m² deployed; nose radius 0.144 m;
   $C_D=1.1$, so $B=142$ kg/m² closed and 21 kg/m² deployed. Peak pressure
   and deceleration at 40–45 km, peak heat flux near 50 km; maximum
   deceleration about 10 $g_0$; maximum heat flux below 70 kW/m², peak
   temperatures about 700 °C; maximum dynamic pressure 1.8 kPa (constant
   $C_D$) or 2.2 kPa (variable $C_D$); critical phase about 1 min around
   t = 8 min.
7. **Constant vs variable $C_D$** (Table 1, constant minus variable):
   Δt = 1.998 min, Δrange −52.43 m, Δx 11.19 m, Δy −51.49 m; impact point
   insensitive, altitude differences of 1–3 km late in the flight.
8. **Capsule vs main payload** (§4.2, Fig. 18, Table 2): payload apogee
   about 190 m higher; impact points 68.46° N 20.54° E (capsule) and
   68.48° N 20.52° E (payload), Δx 0.383 km, Δy −1.475 km.
9. **LEO re-entry** (§4.3, Figs. 19–22): same $B$, nose radius 0.288 m,
   entry interface 120 km, 7600 m/s, flight-path angle −1°; thermal loads
   almost an order of magnitude above the suborbital case (numbers only in
   figures).
10. **Flow regimes** (§5, Eq. 2, Fig. 23):
    $\mathrm{Kn}_{\infty L_{ref}}=\lambda/L_{ref}=1.25\sqrt\gamma\,M_\infty/\mathrm{Re}_{\infty L_{ref}}$;
    free-molecular above "Kn ≈ M/Re = 10", continuum below 0.001 (after
    Bird); from 250 km the flow is free-molecular down to about 125 km,
    continuum from about 69 km, turbulent below about 19 km.
11. **Transition criterion** (§5, Eq. 3): $\mathrm{Re}_{\infty,D}=\rho_\infty u_\infty D/\mu_\infty\ge5.0\times10^5$
    on the capsule diameter, justified by ARD post-flight data (stated, no
    reference).
12. **Coefficients** (Eqs. 4–6): lift, drag and pitching moment referred to
    $\tfrac12\rho_\infty v_\infty^2S_{ref}$ (and $L_{ref}$), with
    $S_{ref}=0.342$ m², $L_{ref}=0.66$ m (maximum diameter), moment pole at
    35% $L_{ref}$ from the nose.
13. **AEDB** (§5, Fig. 25): incidence 0–180° in 10° steps, all regimes,
    points along the trajectory from CIRA and UNINA.
14. **Free-molecular drag** (Fig. 26): DSMC $C_D$ linear in Kn at 0, 20,
    30°, rising from about 2 to about 6 over Kn 0–1400 (approximate).
15. **Bridging function** (Eqs. 7–8, after Mitcheltree):
    $C_{i,trans}=C_{i,cont}+(C_{i,FM}-C_{i,cont})\,\overline C_i$ with
    $\overline C_i=F(\mathrm{Kn}_\infty)=\sin^2[\tfrac{\pi}{8}(3+\log_{10}\mathrm{Kn}_\infty)]$
    for $10^{-3}<\mathrm{Kn}_\infty<10$; S-shaped $C_D$(Kn) in Fig. 27.
16. **Newtonian blunt-cone drag** (Eq. 9, after Bertin):
    $C_D=2\sin^2\theta_c+(R_N/R_B)^2\cos^4\theta_c$, with $R_N/R_B\approx0.44$
    and $\theta_c=45°$ (value not printed; about 1.05 per the reader).
17. **Mach independence** (Fig. 28): continuum $C_D$ becomes independent of
    Mach number from about Mach 5 (Oswatitsch); at 0° about 1.40 at Mach 2
    to 1.29 at Mach 7, at 20° about 1.22 to 1.15, at 30° about 1.14 to 1.08
    (approximate).
18. **Stability and trim** (Fig. 29; free-molecular 250 km, transitional
    80 km Mach 6.43, continuum 36 km Mach 2.16): statically stable below
    about 50° with the centre of gravity at 0.25 $L_{ref}$; free-molecular
    trims at 0° (stable) and 180°; continuum hypersonic trims at 0°,
    140–150° (unstable) and 180°.

# Methods

* **Experiments** (prior, summarised): thermal-protection materials in the
  SPES hypersonic tunnel (Naples) and a nose-plus-flexible-TPS subsystem in
  CIRA's SCIROCCO plasma wind tunnel (conditions not stated); drop tests
  (claim 2).
* **Flight mechanics**: 3-DoF point-mass equations over a spherical planet
  (Vinh, Busemann, Culp), drag and weight only, US1976, Tauber
  stagnation-point correlation (formula not printed), Newtonian stagnation
  pressure; integrator and step not stated; validated against DLR VSB-30
  data (claim 5).
* **Aerodynamics**: DSMC (UNINA) for free-molecular flow; Navier–Stokes
  (CIRA, UNINA) for continuum; Newtonian and panel methods (CIRA);
  bridging function in between. Codes, models, grids, schemes and grid
  convergence are not stated. No uncertainty quantification.

# Tests and results

| Case | Section | Finding |
|---|---|---|
| Drop tests | §2, Fig. 6 | self-alignment in about 2.5 s, 12.5 m/s terminal |
| Model validation | §4 | errors below 0.5%, impact point about 100 m |
| Suborbital re-entry | §4.1, Figs. 10–17 | about 10 $g_0$, below 70 kW/m², about 700 °C, 1.8–2.2 kPa |
| Constant vs variable $C_D$ | Table 1 | Δt 1.998 min, Δrange −52.43 m |
| Capsule vs payload | §4.2, Table 2 | offset 0.383 km / −1.475 km |
| LEO re-entry | §4.3, Figs. 19–22 | loads about 10× suborbital |
| AEDB | Figs. 26–29 | claims 14–18 |

# Notation map

| Fedele & Mungiguerra (2018) | Registry | Note |
|---|---|---|
| $\mathrm{Kn}_\infty$, $\mathrm{Kn}_{\infty L_{ref}}$ | $\mathrm{Kn}$ | reference length stated |
| $\lambda$ | $\lambda_{\mathrm{mfp}}$ | mean free path |
| $\gamma$ | $\gamma$ | ratio of specific heats; the flight-path angle is written in words |
| $g_0$ | $g_0$ | standard gravity |
| $B$ | words (ballistic coefficient) | |
| $m$ | words (capsule mass) | **collision risk** with species masses $m_s$ |
| $C_D$, $C_L$, $C_M$, $C_{M\alpha}$ | words | |
| $A$, $S_{ref}$, $L_{ref}$, $D$, $R_N$, $R_B$ | words | |
| $M_\infty$, $\mathrm{Re}_{\infty L_{ref}}$, $\mathrm{Re}_{\infty,D}$ | words | |
| $\rho_\infty$, $u_\infty$, $v_\infty$, $V_\infty$, $\mu_\infty$ | words | **collision:** registry $\mathbf v$ is the particle velocity, $\mu_\perp$ a mobility |
| $\alpha$ | words (angle of attack) | |
| $\theta_c$ | words (cone half-angle) | **collision:** registry $\theta$ is the azimuthal coordinate |
| $\overline C_i$, $F(\mathrm{Kn})$ | words (bridging function) | **collision:** registry $F$ is thrust |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Fedele_Aerodynamics_and_flight_mechanics_activities_for_a_suborbita.pdf`.
   * **Version.** Publisher's PDF, 10 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.05.044, printed on page 1
     and checked on Crossref: title, two authors, Acta Astronaut.
     151:324–333 match; issue October 2018 (no online date on Crossref);
     page 1 gives received 21 Dec 2017, revised 2 May 2018, accepted 21 May
     2018, online 22 May 2018. Page 1 matches the filename title.
   * **How it was read.** Text layer; pp. 331–332 (Eqs. 2–9, Figs. 24–29)
     rendered. Trajectory and load curves (Figs. 2, 8, 10–22) are graphical
     only; the Tauber formula is not printed; Fig. 29 read qualitatively.
   * **Recorded as printed.**
     * The open heat shield is 76 cm in diameter (§3), while $L_{ref}=0.66$
       m is called the "maximum capsule diameter" (§5), consistent with
       $S_{ref}=0.342$ m².
     * Closed ballistic coefficient: 8/(1.1 × 0.0491) = 148 kg/m², printed
       142 kg/m²; the deployed 21 kg/m² checks.
     * Moment pole at 35% $L_{ref}$ from the nose, stability discussed for a
       centre of gravity at 0.25 $L_{ref}$; Fig. 29's reference point is
       unclear, and $L_{ref}$ is a diameter used as a length.
     * The regime boundaries identify Kn with M/Re, while Eq. 2 carries the
       factor $1.25\sqrt\gamma$.
     * The free-molecular limit is about 125 km in the text; Fig. 25's
       regime line sits near 107 km (approximate reading).
     * Eq. 8 holds for $10^{-3}<\mathrm{Kn}<10$, but Fig. 27's axis runs to
       Kn = 100.
     * "Navier–Stokes predictions compare favourably with DSMC" appears in
       the free-molecular paragraph (§5), where Navier–Stokes is outside its
       validity.
     * The trajectory's constant $C_D=1.1$ lies below the database
       continuum values at zero incidence (1.29–1.40, Fig. 28); Eq. 9 gives
       about 1.05.
     * The Fig. 9 caption reads "VSB-3018"; "Oswatich" for Oswatitsch;
       "DMCS" for DSMC.
   * **Reference list.** 24 printed entries, matching the Crossref
     reference count. Ref. [4] carries the authors, volume and pages of
     ref. [14] (Carandente, Zuppardi, Savino, Acta Astronaut. 93 (2014)
     291–303) with the title of ref. [3]: probably a duplicate of [14] under
     a wrong title, to be checked at merge.
