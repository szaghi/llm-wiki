---
type: Source
title: "Fedele & Mungiguerra (2018) — Aerodynamics and flight mechanics activities for a suborbital flight test of a deployable heat shield capsule"
description: "Reports the trajectory analysis and preliminary all-regime aerodynamic database of MINI-IRENE, a suborbital demonstrator with an umbrella-like deployable heat shield: 3-DoF re-entry loads, a sin²-of-log-Knudsen bridging function between DSMC and continuum data, Newtonian and Mach-independence estimates, and static stability and trim from 0° to 180°."
resource: "doi:10.1016/j.actaastro.2018.05.044"
source_kind: paper
authors: [Fedele A., Mungiguerra S.]
year: 2018
venue: "Acta Astronaut. 151:324–333"
local_file: "/home/stefano/papers/mosaic/high-speed-aerothermodynamics/2018_Crossref_Acta_Astronautica_Fedele_Aerodynamics_and_flight_mechanics_activities_for_a_suborbita.pdf"
tags: [reentry, capsule, deployable-heat-shield, rarefied-flow, aerodynamic-database, flight-mechanics]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper reports the flight-mechanics and aerodynamics work for MINI-IRENE,
the suborbital Flight Demonstrator (FD) of the IRENE capsule, whose
umbrella-like mechanically deployable heat shield lowers the ballistic
coefficient $\beta_B$ to cut peak heat flux and mechanical loads. A 3-DoF
point-mass trajectory model (US1976 atmosphere, Tauber stagnation-point
heating, Newtonian stagnation pressure) is validated against a DLR VSB-30
reference trajectory (errors < 0.5%, impact point about 100 m) and used to
predict the capsule's suborbital re-entry after release from a VSB-30
sounding rocket launched from ESRANGE, its offset from the rocket's main
payload, and a LEO (ISS-orbit) re-entry used to size a plasma-wind-tunnel
(SCIROCCO) test of a Ground Demonstrator. A preliminary aerodynamic database
(AEDB) covers all flow regimes: DSMC in free-molecular flow, a
sin²-of-log-Knudsen bridging function in transitional flow, Navier–Stokes and
engineering methods (Newtonian blunt-cone formula, panel methods) in
continuum flow, for angles of attack 0–180°. Static stability and trim are
assessed from $C_m(\alpha)$ in each regime. Much of the content is
programmatic and preliminary; the quantitative contributions are the
trajectory loads and the AEDB.

# Key claims

1. **Ballistic coefficient** (§1, Eq. 1). $\beta_B=m/(C_DS)$. A lower
   $\beta_B$ lowers peak stagnation pressure and heat flux and moves the
   peaks to higher altitude (Fig. 2, illustrated). Quoted values: Apollo CM
   about 350 kg/m², Space Shuttle about 430 kg/m², IRENE target 25 kg/m².
   Stated.
2. **Drop tests** (§2, Fig. 6). A 3D-printed model, scaled down 1.5×, with
   $\beta_B$ about 4× lower than MINI-IRENE and centre of mass at about 40%
   of its length, dropped from 15 m and 300 m; from 15 m with initial angle
   of attack 90° or 180° it self-aligned with the flow in about 2.5 s,
   terminal velocity 12.5 m/s. Shown (UNINA).
3. **Prior CFD/DSMC** (§2, refs. [14], [15]). A 45° aero-brake half-cone is
   statically more stable than a 60° one (which decelerates more);
   transonic high-angle-of-attack unsteady CFD shows oscillatory flow and
   periodic loads (Fig. 5), relevant to buffeting. Stated, attributed.
4. **Mission** (§3, Figs. 7–8). The FD is released from the VSB-30 payload
   stage some seconds after second-stage burnout (59 s, about 72.5 km);
   apogee about 250 km; landing 860 s after separation; heat shield 76 cm in
   diameter open. The VSB-30 flight is not energetic enough for significant
   TPS heat flux, hence a plasma-wind-tunnel test for TRL 6; the VSB-30
   aerodynamic environment is "very close" to LEO entry, while MAXUS is too
   steep and still does not match LEO fluxes. Stated from analyses.
5. **Trajectory-model validation** (§4). 3-DoF, lift neglected, $\alpha=0$,
   US1976, Tauber correlation for stagnation heat flux, Newtonian stagnation
   pressure $\rho_\infty u_\infty^2$. From second-stage separation (60 s):
   errors in altitude, velocity, dynamic pressure and duration < 0.5%;
   impact point about 100 m off. Shown.
6. **Suborbital re-entry** (§4.1, Figs. 10–17). Separation at T0+75 s,
   100.87 km, 1718.26 m/s (including a 1 m/s separation increment), flight
   path angle 83.7°, azimuth 107.69°. Mass 8 kg; area 0.0491 m² closed
   until apogee, 0.342 m² deployed; nose radius 0.144 m; $C_D=1.1$, giving
   $\beta_B$ = 142 kg/m² closed and 21 kg/m² deployed. Peak pressure and
   deceleration at 40–45 km, peak heat flux near 50 km; maximum deceleration
   about 10 $g_0$; maximum heat flux < 70 kW/m², peak temperatures about
   700 °C; maximum dynamic pressure 1.8 kPa (constant $C_D$) or 2.2 kPa
   (variable $C_D$). Critical phase about 1 min around t = 8 min. Shown.
7. **Constant against variable $C_D$** (Table 1). Differences (constant −
   variable): duration 1.998 min, range −52.43 m, Δx 11.19 m, Δy −51.49 m.
   The impact point is insensitive; altitude differs by 1–3 km late in the
   trajectory. Shown.
8. **Capsule against main payload** (§4.2, Fig. 18, Table 2). Payload apogee
   about 190 m above the capsule's; impact points 68.46° N / 20.54° E
   (capsule) and 68.48° N / 20.52° E (payload); Δx 0.383 km, Δy −1.475 km.
   Shown.
9. **LEO re-entry** (§4.3, Figs. 19–22). Same $\beta_B$, nose radius
   0.288 m; entry at 120 km, 7600 m/s, flight path angle −1°; thermal loads
   almost one order of magnitude higher than suborbital. Shown (numbers in
   figures only).
10. **Regime map** (§5, Eq. 2, Fig. 23).
    $\mathrm{Kn}_\infty=1.25\sqrt{\gamma}\,\mathrm{Ma}_\infty/\mathrm{Re}_\infty$
    with the reference length as length scale; free-molecular limit
    "Kn ≈ M/Re = 10", continuum limit "= 0.001" (after Bird); from 250 km,
    free-molecular down to about 125 km, continuum from about 69 km,
    turbulent below about 19 km. Stated.
11. **Transition criterion** (§5, Eq. 3). Diameter-based freestream
    $\mathrm{Re}\ge5.0\times10^5$, justified by ARD post-flight data. Stated,
    no reference.
12. **Coefficients** (§5, Eqs. 4–6). Reference area 0.342 m², reference
    length 0.66 m (maximum diameter), moment pole at 35% of the reference
    length from the nose; sign convention in Fig. 24.
13. **AEDB** (§5, Fig. 25). Angle of attack 0–180° in 10° steps, all
    regimes, points by CIRA and UNINA along the trajectory.
14. **Free-molecular drag** (Fig. 26). DSMC $C_D$ is linear in Kn at
    $\alpha$ = 0, 20, 30°, rising from about 2 to about 6 over Kn 0–1400
    (approximate figure reading).
15. **Bridging function** (Eqs. 7–8, after Mitcheltree, ref. [23]). In
    $10^{-3}<\mathrm{Kn}_\infty<10$ each coefficient is the continuum value
    plus (free-molecular − continuum) times
    $\sin^2\left[\frac{\pi}{8}\left(3+\log_{10}\mathrm{Kn}_\infty\right)\right]$;
    Fig. 27 shows the S-shaped $C_D(\mathrm{Kn})$.
16. **Newtonian blunt-cone drag** (Eq. 9, after Bertin, ref. [24]). $C_D$ =
    2 sin² of the cone half-angle + (nose radius / base radius)² × cos⁴ of
    the half-angle; for MINI-IRENE the radius ratio is about 0.44 and the
    half-angle 45°. Stated; the paper gives no value (the reader evaluates
    about 1.05).
17. **Mach independence** (Fig. 28). Continuum $C_D$ is Mach-independent
    ("Oswatich", i.e. Oswatitsch) from about $\mathrm{Ma}_\infty=5$;
    approximate readings: 0° about 1.40 at Mach 2 to 1.29 at Mach 7; 20°
    about 1.22 to 1.15; 30° about 1.14 to 1.08.
18. **Stability and trim** (Fig. 29; free-molecular 250 km, transitional
    80 km Mach 6.43, continuum 36 km Mach 2.16). Statically stable,
    $\partial C_m/\partial\alpha<0$, for $\alpha$ below about 50° with the
    centre of gravity at 0.25 reference lengths. Free-molecular: trim at 0°
    (stable) and 180°. Continuum hypersonic: trims at 0°, 140–150°
    (unstable; 150° at lower, 140° at higher hypersonic speeds) and 180°.
    Shown.

# Methods

* Experiments (summarized, prior): TPS material (3 mm Nextel flexible layer,
  ceramic-foam nose) in the SPES hypersonic wind tunnel (Naples); nose plus
  flexible TPS in CIRA's SCIROCCO plasma wind tunnel (Fig. 3), conditions not
  stated; drop tests (claim 2).
* Flight mechanics: 3-DoF point-mass equations over a spherical planet (Vinh,
  Busemann & Culp), drag and weight only; US1976; Tauber correlation
  (formula not printed); Newtonian stagnation pressure. Integrator and time
  step not stated. MAPHEUS nominal initial conditions at 60 s: flight path
  84°, azimuth 107.36°; ground range 75–80 km (ref. [21]).
* Aerodynamics: DSMC (UNINA) in free-molecular flow; Navier–Stokes (CIRA,
  UNINA) in continuum flow; closed-form Newtonian and panel methods (CIRA);
  bridging function in transitional flow. Codes, grids, models and
  convergence not stated. No uncertainty quantification.

# Tests and results

| Case | § | Conditions | Findings |
|---|---|---|---|
| Drop test | §2, Fig. 6 | 15 m, 300 m | self-aligns in about 2.5 s; 12.5 m/s terminal |
| Trajectory validation | §4 | VSB-30 from 60 s | < 0.5% error; impact point about 100 m |
| Suborbital re-entry | §4.1 | 100.87 km, 1718.26 m/s, 83.7°, 8 kg | about 10 $g_0$; < 70 kW/m²; about 700 °C; 1.8 / 2.2 kPa |
| Constant vs variable $C_D$ | Table 1 | — | duration 1.998 min; range −52.43 m |
| Capsule vs payload | §4.2, Table 2 | 1 m/s separation | 0.383 km / −1.475 km |
| LEO re-entry | §4.3 | 120 km, 7600 m/s, −1° | thermal loads about 10× suborbital |
| Free-molecular $C_D$ | Fig. 26 | 0, 20, 30° | linear in Kn |
| Transitional $C_D$ | Fig. 27 | Eq. 8 | S-shape |
| Continuum $C_D$ | Fig. 28 | Mach about 2–7 | Mach-independent from about 5 |
| $C_m(\alpha)$ | Fig. 29 | three regimes | trims as in claim 18 |

# Notation map

| Fedele & Mungiguerra (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $B$ | $\beta_B$ | ballistic coefficient |
| $A$, $S_{ref}$ | $S$ | reference area |
| $L_{ref}$, $D$ | words (reference length, diameter) | |
| $C_D$, $C_L$, $C_M$ | $C_D$, $C_L$, $C_m$ | |
| $C_{M\alpha}$ | $\partial C_m/\partial\alpha$ | |
| $M_\infty$ | $\mathrm{Ma}_\infty$ | |
| $\mathrm{Re}_{\infty L_{ref}}$, $\mathrm{Re}_{\infty,D}$ | $\mathrm{Re}_\infty$ | length scale stated |
| $\mathrm{Kn}_\infty$ | $\mathrm{Kn}_\infty$ | |
| $\lambda$ | words (mean free path) | |
| $\rho_\infty$, $u_\infty$/$v_\infty$, $\mu_\infty$ | $\rho_\infty$, $u_\infty$, $\mu_\infty$ | the paper uses both u and v for freestream speed |
| $\alpha$, AoA | $\alpha$ | |
| $\theta_c$, $R_N$, $R_B$ | words (cone half-angle, nose and base radii) | distinct from $\theta_w$ |
| $\overline{C}_i$, $F(\mathrm{Kn})$ | words (bridging function) | |
| $m$, $g_0$ | $m$; words | |
| flight path angle (words in the paper) | words | not $\gamma$ |

# Pages created or updated

* [Re-entry capsule aerodynamics across flow regimes](/methods/reentry-capsule-aerodynamics-across-regimes.md)

# Citations

1. `/home/stefano/papers/mosaic/high-speed-aerothermodynamics/2018_Crossref_Acta_Astronautica_Fedele_Aerodynamics_and_flight_mechanics_activities_for_a_suborbita.pdf`.
   * **Version.** Publisher PDF (Elsevier, 10 pages).
   * **Identity.** doi:10.1016/j.actaastro.2018.05.044, printed on page 1 and
     checked on Crossref: Acta Astronaut. 151, 324–333, authors Fedele and
     Mungiguerra, issue 2018-10 (no online date in Crossref). Received
     21 Dec 2017, revised 2 May 2018, accepted 21 May 2018, online 22 May
     2018 (page 1). Page-1 title matches the filename.
   * **How it was read.** Text layer (`pdftotext -layout`); pp. 331–332
     (Eqs. 2–9, Figs. 24–29) rendered and read visually. Trajectory and load
     curves (Figs. 2, 8, 10–22) are graphical only; figure values above are
     approximate. The Tauber formula is not printed in the paper.
   * **Recorded as printed.**
     * Heat-shield diameter: 76 cm open (§3) against a 0.66 m maximum
       diameter as reference length (§5), which is consistent with the
       0.342 m² reference area.
     * Closed ballistic coefficient: 8 / (1.1 × 0.0491) = 148 kg/m², not the
       printed 142 kg/m²; the deployed 21 kg/m² checks.
     * Moment pole at 35% of the reference length; stability stated for the
       centre of gravity at 0.25; which one Fig. 29 uses is not said. The
       reference length is a diameter, so "% of reference length from the
       nose" mixes length and diameter.
     * The regime boundaries are stated as "Kn ≈ M/Re", while Eq. 2 carries
       the factor $1.25\sqrt\gamma$ (about 1.48 for $\gamma=1.4$).
     * The free-molecular limit is about 125 km in the text; Fig. 25 draws
       the regime line near 107 km (approximate reading).
     * Eq. 8 is stated for $10^{-3}<\mathrm{Kn}<10$, but Fig. 27 extends to
       Kn = 100.
     * "Navier–Stokes predictions compare favourably with DSMC" sits inside
       the free-molecular paragraph.
     * The trajectory's constant $C_D=1.1$ is below the database continuum
       values at $\alpha=0$ (about 1.29–1.40, Fig. 28).
     * Fig. 9 caption "VSB-3018" (garbled reference); "Oswatich" for
       Oswatitsch; "DMCS" for DSMC.
   * **Reference list.** 24 printed entries (Crossref count 24). Ref. [4] is
     printed with the authors, volume and pages of ref. [14] (Acta Astronaut.
     93 (2014) 291–303) but the title of ref. [3]; it is almost certainly a
     duplicate of ref. [14] with a wrong title.
