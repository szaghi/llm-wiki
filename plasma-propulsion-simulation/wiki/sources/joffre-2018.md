---
type: Source
title: "Joffre et al. (2018) — Trajectory design and guidance for landing on Phobos"
description: "Designs Phobos landings from libration-point-orbit manifolds with a polynomial open-loop guidance optimised by an interior-point method (about 7 m/s against 16.5 m/s for a forced vertical descent), shows by Monte Carlo on a perturbed truth model that open-loop guidance diverges, and brings a waypoint-based terminal-velocity guidance close to the open-loop cost."
resource: "doi:10.1016/j.actaastro.2018.06.024"
source_kind: paper
authors: [Joffre E., Zamaro M., Silva N., Marcos A., Simplício P.]
year: 2018
venue: "Acta Astronaut. 151:389–400"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Joffre_Trajectory_design_and_guidance_for_landing_on_Phobos.pdf"
tags: [context, guidance, small-body-landing, libration-point-orbits, trajectory-optimization]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

An Airbus Defence and Space / University of Bristol study for the UK Space
Agency, run in parallel with ESA's Phobos Sample Return Phase A. Because the
Mars–Phobos L1 and L2 points lie only about 3.5 km above the surface,
Keplerian orbits about Phobos do not exist; the authors use libration-point
orbits (LPOs) as observation platforms whose unstable invariant manifolds
serve as initial guesses for landing trajectories (§3.3). A polynomial
open-loop guidance (OLG) profile optimised by an interior-point NLP gives a
soft landing with about 7 m/s of propulsive $\Delta V$ in under 2 h, against
about 16.5 m/s (plus about 50 m/s per Phobos orbit of hovering
station-keeping) for a forced vertical translation from a 10 km hovering
point (§§3.4–3.5). A Monte Carlo campaign on a perturbed truth model shows
that the OLG diverges (crash or escape), so closed-loop guidance is needed
(§4). Direct constrained-terminal-velocity guidance (CTVG) has no path
constraint, can crash and costs 15.4 m/s; a waypoint-based CTVG with short
guidance horizons brings the mean $\Delta V$ down to 7.34 m/s (Table 5).
Propulsion enters only as an abstract commanded acceleration; no thruster
of any kind is modelled.

# Key claims

Symbols are the paper's (see the notation map).

1. **No Keplerian orbits** (§3.1, Fig. 3): the mass ratio
   $m_{\mathrm{Phobos}}/(m_{\mathrm{Mars}}+m_{\mathrm{Phobos}})=1.65\times10^{-8}$
   puts the circular-restricted-three-body L1 and L2 points about 3.5 km
   above the surface; Mars third-body perturbation cannot be neglected.
   Stated, specific to Mars–Phobos (footnote 5).
2. **Dominant perturbations** (§3.1, attributed to refs. [7,8]): Phobos'
   orbital eccentricity and non-spherical gravity; Mars $J_2$ is an order of
   magnitude smaller.
3. **Gravity field** (Eqs. 1–2): a spherical-harmonic expansion of the
   potential $U_g(r,\theta,\phi)$ with coefficients $C_{n,m}$, $S_{n,m}$,
   associated Legendre functions and reference radius $R=11$ km, to degree
   and order 4 from ref. [9] (e.g. $C_{2,0}=-0.04698$, $C_{2,2}=0.02276$, read from the Fig. 3 coefficient table).
4. **Dynamics** (Eqs. 3–4): $\dot{\underline X}=f(\underline X,t)+B\cdot\underline U$,
   augmented with Phobos' true anomaly,
   $\dot\nu=n(1+e\cos\nu)^2/(1-e^2)^{3/2}$ (non-autonomous because of the
   eccentricity); full equations in ref. [10].
5. **LPO manifolds** (§3.3, Figs. 4–5): Lyapunov, halo, quasi-halo and
   Lissajous families are computed in the restricted problem and continued
   to the full model by switching on the harmonics and then the
   eccentricity (method of ref. [8]); manifolds come from the monodromy
   matrix eigenvectors with a very small $\Delta V$. The ballistic manifold
   landing is not soft (touch-down velocity map about 4–8, presumably m/s).
6. **Open-loop soft landing** (§3.4, Eqs. 5–6, Figs. 6–7, shown): a
   polynomial command $\underline U(t>t_b)=\sum_{k=0}^n\underline U_k((t-t_b)/T)^k$
   minimising $J=\int_{t_0}^{t_f}\lVert\underline U\rVert\,\mathrm dt$ with
   final tolerances 10 m and 10 cm/s, solved by an interior-point method
   (ref. [15]) in "a few seconds": duration under 2 h, $\Delta V\approx7$
   m/s, thrust from $t_b=0$. Local optima with $t_b>0$ have shorter thrust
   arcs, larger accelerations and larger $\Delta V$.
7. **Forced translation** (§3.5, Table 3, Eqs. 7–9, Figs. 8–9, shown): a
   trapezoidal velocity profile from a 10 km station-keeping point
   degenerates at the optimum to a triangular one; under 1 h,
   $\Delta V\approx16.5$ m/s, plus station-keeping of about 50 m/s per
   Phobos orbital period or 6.9 m/s per hour.
8. **Open loop fails** (§4, Fig. 10): the OLG designed on the guidance
   model and replayed in 200 Monte Carlo runs of the truth model "rapidly
   diverges": some runs crash, some never reach the surface. Qualitative; no
   statistics.
9. **Cost functionals** (§4.1, Eq. 10, Appendix B): the L1 cost
   $\int\lVert\underline U\rVert\mathrm dt$ is the true $\Delta V$ but
   non-smooth; the L2 cost $\int\lVert\underline U\rVert^2\mathrm dt$ is
   smooth and often analytic, suited to on-board guidance, at a $\Delta V$
   penalty. Proved for the double integrator of Appendix B.
10. **Guidance survey** (Table 4, attributed to refs. [16–21]):
    proportional navigation and its augmented and biased variants,
    final-time-velocity guidance
    $\underline U=\frac{3}{t_{go}^2}(\underline r_f-\underline r)-\frac{3}{t_{go}}\underline v-\frac32\underline g$,
    and CTVG
    $\underline U=\frac{6}{t_{go}^2}(\underline r_f-\underline r)-\frac{4}{t_{go}}\underline v-\underline g-\frac{2}{t_{go}}\underline v_f$,
    with ZEM/ZEV forms (Eq. 11).
11. **Direct CTVG** (§4.3, Fig. 12, shown): meets the landing requirements
    in principle but has no path constraint (trajectories can pass below the
    surface); the example crashes with $\Delta V=15.4$ m/s, "more than twice
    the OLG $\Delta V$".
12. **Waypoint CTVG** (§4.3, Eq. 12, Table 5, shown with perfect navigation
    and actuation): targeting intermediate states of the reference
    trajectory at a horizon $t_h$, re-planned every $t_g$; smaller $t_g$
    improves accuracy and shorter $t_h$ lowers $\Delta V$ towards the OLG
    value, until the loop becomes unstable.

# Methods

Two dynamics models (§3.2, Table 2): MAG (mission analysis and guidance;
Keplerian Mars, body-fixed frame fixed relative to the Hill frame, Phobos
harmonics to degree and order 4, deterministic) and DKE (truth model; Mars
Kepler plus $J_2$, librating body frame of 0.30–1.90° amplitude and 2.26
terrestrial years period, harmonics drawn from Gaussians with mean the MAG
value and standard deviation 100% of its magnitude). Frames: Hill (origin
Phobos barycentre, $x$ radial outward from the Mars–Phobos barycentre) and
body-centred body-fixed, differing by 180° in the orbital plane under tidal
lock. Physical data (Table 1, JPL ephemeris, 25 July 2012 00:00 UTC): Mars
$6.4185\times10^{23}$ kg; Phobos $1.0659\times10^{16}$ kg, semi-major axis
9379.2557 km, eccentricity 0.0156, inclination 0.0186°, mean ellipsoid
13.1 km × 11.1 km × 9.3 km, period about 7 h 40 min. Trajectory design: LPO
computation, continuation, STM manifolds, selection of manifolds hitting
Phobos, per site the most vertical one, site chosen by lowest touch-down
velocity. Optimisation: polynomial acceleration (order not stated), NLP by
interior point, decision variables the coefficients, $t_b$ and $t_f$, initial
guess zero thrust and the ballistic impact time. Closed loop: explicit and
implicit architectures (Fig. 11), analytic CTVG, waypoint variant (Fig. 13),
scan over $t_g\in\{10,100,200,400\}$ s and $t_h\in\{1000,2000,3000\}$ s in
DKE Monte Carlo; navigation and control allocation not modelled. Landing
requirements (§2.2): 20% surface accessibility (goal 50%), accuracy better
than 50 m at 95%, touch-down velocity below 1.5 m/s vertical and 1 m/s
horizontal, a final 20 m free fall that this work does not include
(footnote 6).

# Tests and results

Table 5, waypoint CTVG in DKE Monte Carlo (sample size not stated), rows
$t_h$ = 1000 / 2000 / 3000 s, columns $t_g$ = 10 / 100 / 200 / 400 s:

| Quantity | $t_h$ (s) | $t_g=10$ s | 100 s | 200 s | 400 s |
|---|---|---|---|---|---|
| mean $\Delta V$ (m/s) | 1000 | 7.34 | 7.36 | 7.36 | 7.66 |
| | 2000 | 8.07 | 8.16 | 8.23 | 8.39 |
| | 3000 | 9.91 | 10.1 | 10.3 | 10.9 |
| std $\Delta V$ (m/s) | 1000 | 0.96 | 0.96 | 0.95 | 1.10 |
| | 2000 | 1.05 | 1.08 | 1.12 | 1.08 |
| | 3000 | 1.13 | 1.17 | 1.23 | 1.27 |
| mean accuracy index (−) | 1000 | 0.17 | 0.55 | 0.68 | 4.71 |
| | 2000 | 0.15 | 0.52 | 0.51 | 4.63 |
| | 3000 | 0.13 | 0.45 | 0.53 | 5.55 |
| std accuracy index (−) | 1000 | 0.09 | 0.26 | 0.57 | 2.04 |
| | 2000 | 0.09 | 0.39 | 0.41 | 2.81 |
| | 3000 | 0.09 | 0.32 | 0.39 | 3.71 |

The accuracy index is Eq. 12,
$J=\sqrt{(\Delta r_f/\Delta r_{tol})^2+(\Delta v_f/\Delta v_{tol})^2}$.
Appendix B (double integrator, unit control bound, $t_f=10$, from 0 to 10;
Table B.6): the L1-optimal bang-coast-bang solution has L1 and L2 costs
2.25 and 2.25, the L2-optimal linear-in-time solution 3.00 and 1.20; the
unbounded L1 limit is 2.00. Reader's check: the L2 law
$u=\frac{6(b-a)}{t_f^2}(1-2t/t_f)$ gives 1.20 and 3.00, and the
bang-coast-bang with switching time $5-\sqrt{15}\approx1.127$ gives
$2\times1.127\approx2.25$ for both; all table values reproduce. The OLG
command reaches about $5.7\times10^{-3}$ m/s² at the end (Fig. 7, read from
the plot).

# Notation map

GNC and orbital-mechanics symbols; the registry has a counterpart only for
time.

| Joffre et al. (2018) | Registry | Note |
|---|---|---|
| $\underline X$ | words (spacecraft state) | underline marks vectors in the paper |
| $\underline r$, $\underline v$, $\underline a$ | words (spacecraft position, velocity, acceleration) | **collision:** registry $\mathbf v$ is the phase-space velocity |
| $r$, $\theta$, $\phi$ | words (spherical radius, co-latitude, longitude) | **collision:** registry $r$, $\theta$ thruster coordinates, $\phi$ the potential |
| $U_g$, $\underline U$ | words (gravity potential, commanded acceleration) | |
| $\mu_g$ | words (gravitational parameter) | **collision:** registry $\mu_\perp$, $\mu_\parallel$ |
| $\mu[\cdot]$, $\sigma[\cdot]$ | words (mean, standard deviation) | **collision:** registry $\sigma_{sk}$ cross section |
| $C_{n,m}$, $S_{n,m}$ | words (harmonic coefficients) | **collision:** registry $S_j$ Sobol' indices |
| $e$ | words (Phobos eccentricity) | **collision:** registry $e$ elementary charge |
| $n$ | words (mean motion; also degree index) | **collision:** registry $n_s$ number density |
| $T$ | words (Phobos orbital period) | **collision:** registry $T_s$ temperature |
| $\nu$ | words (true anomaly) | **collision:** registry $\nu_{sk}$ collision frequency |
| $\underline g$ | words (apparent gravitational acceleration) | **collision:** registry $g$ relative speed, $g_0$ standard gravity |
| $k$ | words (navigation ratio; polynomial index) | **collision:** registry $k$ wavenumber |
| $J$, $J_{\mathcal L_1}$, $J_{\mathcal L_2}$ | words (cost functionals, accuracy index) | $\mathcal L_1$, $\mathcal L_2$ are norms, not the likelihood $\mathcal L$; L1/L2 also name Lagrange points |
| $B$ | words (command matrix) | **collision:** registry $\mathbf B$ magnetic field |
| $\underline\Lambda$, $V_c$, ZEM, ZEV | words (line of sight, closing velocity, zero-effort miss and velocity) | $V_c$ is not a voltage |
| $t$, $t_0$, $t_b$, $t_f$, $t_{go}$, $t_g$, $t_h$ | $t$ plus words | |
| $\Delta V$, $R$ | words (velocity increment, gravity reference radius) | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Joffre_Trajectory_design_and_guidance_for_landing_on_Phobos.pdf`.
   * **Version.** Publisher's typeset version of record (Crown Copyright
     2018, Elsevier on behalf of IAA), 12 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.024, printed on page 1
     and checked on Crossref: title, the five authors in order, Acta
     Astronaut. 151:389–400 match; issued 2018-10, no published-online
     field. Page 1: received 5 Mar 2017, revised 2 Jun 2018, accepted 9 Jun
     2018, online 18 Jun 2018. Page 1 matches the filename title. Funding:
     UK Space Agency, National Space Technology Programme (grant
     RP10G0348A205).
   * **How it was read.** Full text layer; Eqs. 1–12 and Tables 1–5 and
     B.6 read on rendered pages 391–394, 396–397 and 400. Not stated in the
     paper: the OLG polynomial order, the Table 5 Monte Carlo size, the
     selected landing-site coordinates, the Fig. 5 colour-bar unit.
   * **Recorded as printed.**
     * Reader's check (§3.5): 50 m/s per Phobos period of about 7.67 h is
       about 6.5 m/s per hour; the printed 6.9 m/s per hour corresponds to
       about 53 m/s per period.
     * Reader's check (§3.1): the Table 1 masses give a ratio of
       $1.661\times10^{-8}$; the text prints $1.65\times10^{-8}$.
     * Table 3 writes the intervals $[t_0,\Delta t_1]$,
       $[\Delta t_1,t_f-\Delta t_2]$, mixing a time with a duration;
       consistent only for $t_0=0$, which the position formulas assume.
     * Eq. 5 defines the command only for $t>t_b$ while the Eq. 6 cost
       integrates from $t_0$; consistent if the command is zero before
       $t_b$ (implicit).
     * Table 4 prints the augmented law with $-\frac k2\underline g_\perp$
       and the biased law with $-\underline g$ without stating whether
       $\underline g$ is gravity or its compensation.
     * §4.1 refers to "the block-diagram 11 below" for the fully explicit
       architecture while the "(Fig. 11)" parenthetical sits on the fully
       implicit sentence.
   * **Reference list.** 24 printed entries ([1]–[24]), matching the
     Crossref reference count. Printed author-name inversions kept: ref.
     [1] "Z. Junjun"; ref. [18] "K. Byung Soo, L. Jang Gyu, H. Hyung Seok";
     ref. [20] "G. Yanning, M. Hawkins, W. Bong"; keys follow the printed
     first-author surname. Ref. [15] prints pages "877900"; ref. [13]
     prints no year and is keyed with `-nd`.
