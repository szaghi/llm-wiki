---
type: Source
title: "Delchambre et al. (2018) — Momentum enhancement factor estimation for asteroid redirect missions"
description: "Proposes an end-to-end estimation of the kinetic-impactor momentum enhancement factor from a hovering observer spacecraft, with a linear error budget and a chain of three extended Kalman filters, and shows in a NEOShield-2 simulation that the 1σ uncertainty drops from 0.44 to 0.11 within 7 days after impact."
resource: "doi:10.1016/j.actaastro.2018.05.050"
source_kind: paper
authors: [Delchambre S., Ziegler T., Falke A., Janschek K.]
year: 2018
venue: "Acta Astronaut. 151:125–136"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Delchambre_Momentum_enhancement_factor_estimation_for_asteroid_redirect.pdf"
tags: [context, planetary-defence, kinetic-impactor, orbit-determination, kalman-filter, navigation]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper proposes an end-to-end method to estimate the momentum
enhancement factor $\beta_{lin}$ of a kinetic-impactor (KI) asteroid
deflection. An Explorer spacecraft hovers near the small body (SB) and
tracks it before and after the impact. A linear error budget over a
parameter breakdown tree (Fig. 2, Eq. 6) splits the $\beta_{lin}$
uncertainty into four drivers: SB mass, impactor mass, impactor velocity,
and the SB velocity change $\Delta v_{sb}$, the last dominant. The
along-track $\Delta v_{sb}$ follows from the semimajor-axis change via
vis-viva (Eq. 20); the cross-track components follow from assumed impact
and ejecta directions (Eqs. 27–30). Three extended Kalman filters in
chain estimate the SB orbit: an absolute Explorer navigation filter, a
relative Explorer–SB optical navigation filter, and an absolute SB
filter fed with "pseudo radioscience" measurements (the Explorer's
Doppler, range and Delta-DOR shifted onto the SB centre of mass). A
Matlab end-to-end simulation of the NEOShield-2 reference scenario
(asteroid 2001 QC34, $\beta_{lin}=2.61$) reduces the 1σ uncertainty of
$\beta_{lin}$ from 0.44 to 0.11 in 7 days after impact. The paper has no
plasma or electric-propulsion content.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Definition** (§1, Eqs. 1–4, attributed to the authors' earlier
   paper [11]): $M\Delta\mathbf v_{sb}=\boldsymbol\beta_{lin}m\mathbf u_{sc}=-\mathbf p_{ej}+m\Delta\mathbf v_{sc}$
   (Eq. 1 as printed), with $\boldsymbol\beta_{lin}=\beta_{lin}\mathbf R_\beta$
   a 3×3 matrix and scalar gain
   $\beta_{lin}=M|\Delta\mathbf v_{sb}|/(m|\mathbf u_{sc}|)$; a perfectly
   plastic collision gives $\beta_{lin}=1$.
2. **Error budget** (§3, Eq. 6): for uncorrelated parameters
   $\sigma^2_{\beta_{lin}}$ is the sum of squared sensitivities to $M$,
   $m$, $|\Delta\mathbf v_{sb}|$ and $|\mathbf u_{sc}|$ times their
   variances. Assumed: $\sigma_M=1\%$ (3σ, §3.1), $\sigma_m=5\%$ (3σ,
   §3.2), $\sigma_{u_{sc}}=[0.1\ 0.1\ 0.3]$ m/s (1σ, §3.3). Stated.
3. **Along-track velocity change** (§3.4.1, Eq. 20):
   $\Delta v_{//sb}=\sqrt{(2a^+\mu_s-\rho\mu_s)/(a^+\rho)}-\sqrt{(2a^-\mu_s-\rho\mu_s)/(a^-\rho)}$,
   assuming a constant SB–Sun distance $\rho$ across the impact and an
   instantaneous semimajor-axis change; slow ejecta escape is out of
   scope.
4. **Cross-track components** (§3.4.2, Eqs. 27–30):
   $\Delta v_{/\perp sb}=\Delta v_{//sb}\tan\theta_{sb}$ and
   $\Delta v_{\perp\perp sb}=\Delta v_{//sb}\tan\gamma_{sb}/\cos\theta_{sb}$,
   the angles combining impactor and ejecta directions; a priori
   $|\Delta\mathbf v_{ej}|=|\Delta\mathbf v_{sc}|$.
5. **Ejecta direction** (§3.4.2, Eqs. 37–39): ejecta leave preferentially
   along the surface normal (attributed to Housen & Holsapple [25]; the
   crater stays circular except for strongly oblique impacts [26]); the
   ejecta-cone half-angle uncertainty is
   $\sigma_\alpha=\max\{\alpha_a,\alpha_b\}/2$ for an ellipsoid
   $a\times b\times b$ and a 3σ targeting accuracy of $c$ m.
6. **Pseudo radioscience** (Eqs. 23–26): first-order Taylor shifts of
   range, Doppler and Delta-DOR from the Explorer to the SB centre of mass
   using the relative-navigation pose. The linearisation errors are stated
   to be close to machine precision ($10^{-16}$) "due to the geometry of
   the problem"; the shifted measurements are non-Gaussian because the
   relative-filter errors are. Stated.
7. **Main result** (§5, Fig. 7): $\beta_{lin}$ knowledge 0.44 (1σ) at
   impact, 0.15 at 3 days, 0.11 at 7 days after impact, with 66.9%
   ground-station availability; estimate 2.54 against the nominal 2.61
   (error 0.07, 2.7%). For the $\beta_{lin}$ range 4–10 reported for rocky
   targets at ~10 km/s (attributed to [25]), 0.11 would be a 1.1–2.75%
   error. The abstract restates the result as 0.33 (3σ) after 1 week.
   Shown (one simulated scenario).
8. **Driver breakdown** (§5, Fig. 8, Eqs. 42–43): the $\Delta v_{sb}$ share
   of the $\beta_{lin}$ variance falls from 99.5% to 89.5%, the impactor
   mass share rises from 0.5% to 10.2%, SB mass and impactor velocity stay
   below 0.5% each. Recommendation: extend the monitoring windows; if cost
   forces a cut, shorten the post-impact window to 3 days first, since the
   last 4 days improve the knowledge by only 12%
   (= (0.15−0.11)/(0.44−0.11)).

# Methods

* Frames (§3.4): inertial frame J at the Solar System Barycentre
  (ecliptic, vernal equinox); SB flight frame G with $e_{//}$ along the SB
  velocity, $e_{\perp\perp}$ along the orbital angular momentum,
  $e_{/\perp}$ completing it; related by the direction-cosine matrix
  $R_J$ (Eq. 11), whose orbit-determination errors are treated as
  negligible.
* Estimation chain (§3.4.1, Fig. 4), three EKFs:
  1. absolute Explorer navigation (dynamics: Sun and planets, solar
     radiation pressure, SB gravity, GNC commands; X-band Doppler
     0.1 mm/s every 1 min, range 5 m every 10 min, Delta-DOR 10 nrad
     daily, Table 2; ESTRACK Cebreros, Malargüe, New Norcia);
  2. relative Explorer–SB navigation (monocamera landmark pose 5 m per
     axis, accelerometer 10 nm/s²; converges 3 h after manoeuvres);
  3. absolute SB orbit-determination filter on the pseudo radioscience
     measurements.

  §4 calls the filters "CEKF" (consider EKF; not defined) with biases as
  consider parameters. Operational square-root information filtering
  [22–24] is declared out of scope.
* Explorer orbit: near-inertial day-side hovering with thrust pulses
  (refs [4–7], Fig. 5), daily station-keeping (Δv ~2 cm/s), wheel
  off-loading.
* Filter tuning (§4): NEES consistency test (Eqs. 40–41) with acceptance
  interval $[r_1,r_2]$ [34]; Monte Carlo runs per ECSS-E-HB-60-10A [35],
  number of runs not reported; the SB filter rejects pseudo-Doppler for
  2 h after each station-keeping manoeuvre; SB process noise enlarged at
  impact to cover the possible $\beta_{lin}$ range.
* Simulator (§4): Matlab end-to-end, high-fidelity SB and Explorer
  dynamics (SRP, Yarkovsky, solar and planetary gravity), image chain in
  high (PANGU v4.01 plus pose estimation) or medium fidelity
  (Gaussian-biased poses; the medium chain produced the results),
  medium-fidelity actuators and sensors, on-board translational GNC,
  X-band radioscience link; 1 min step over 14 days; attitude by a
  ROSETTA-based performance model [18].

# Tests and results

* Reference scenario (§4, Table 1), NEOShield-2 [31], 2001 QC34
  (230 m × 160 m × 160 m): launch MJD2000 10205.0, Explorer arrival
  12129.0, impact 12592.9; impactor 1294 kg at 9.61 km/s relative; SB
  mass $5.88\times10^9$ kg; $\beta_{lin}=2.61$; $|\Delta v_{sb}|=5.51$ mm/s
  (azimuth/elevation 143.6°/−2.6°), $|\Delta v_{sc}|=2.11$ mm/s
  (143.1°/3.0°), $|\Delta v_{ej}|=3.41$ mm/s (144.0°/−6.1°).
* Monitoring 7 days before and 7 days after impact; results from MJD2000
  12592.9 to 12599.9.
* $\beta_{lin}$ knowledge (Fig. 7): 0.44 (1σ) at impact, nearly flat for
  24 h (impact, momentum off-loading, hovering control), 0.15 at 3 days,
  0.11 at 7 days; station availability 66.9%, mostly Cebreros (15°
  elevation mask).
* Velocity-change estimate (Fig. 9): true inertial
  $\Delta v_{sb}=[-4.4\ 3.3\ 0.3]$ mm/s = $\Delta v_{sc}$ $[-1.6\ 1.3\ 0.1]$
  + $\Delta v_{ej}$ $[-2.8\ 2.0\ 0.2]$ mm/s; final errors
  $[99.3\ -59.7\ -6.1]$ µm/s, stated as 1.8–2.2% of the true components;
  caption: below 100 µm/s per axis after 7 days.
* Relative velocity navigation (Fig. 10): 1σ between 0.03 and 0.7 mm/s;
  reconvergence in 3–4 h after thrusting down to the 0.1 mm/s Doppler
  level; peaks from the impact, wheel off-loading (~0.5 days after
  impact) and daily station-keeping.
* Conclusion (§6): 2 weeks of monitoring at 67% availability gives
  $\sigma_\beta=0.11$ (1σ), below 5% of the nominal value.

# Notation map

The paper is planetary-defence navigation; none of its quantities has a
registry counterpart.

| Delchambre et al. (2018) | Registry | Note |
|---|---|---|
| $\beta_{lin}$, $\boldsymbol\beta_{lin}$, $\mathbf R_\beta$ | words (momentum enhancement factor, scalar and 3×3) | |
| $M$, $m$ | words (SB mass, impactor mass) | **collision** with $m_s$ (species mass) and $M_A$ |
| $\mathbf u_{sc}$ | words (impactor relative velocity) | **collision** with $\mathbf u_s$ (mean velocity) |
| $\Delta\mathbf v_{sb}$, $\Delta\mathbf v_{sc}$, $\Delta\mathbf v_{ej}$ | words (SB, impactor-induced, ejecta-induced velocity changes) | not the phase-space velocity $\mathbf v$ |
| $\mathbf p_{ej}$ | words (ejecta momentum) | the nomenclature's ${}^J\mathbf p$ is a 6-D pose |
| $a^-$, $a^+$ | words (semimajor axis before/after impact) | |
| $\rho$ | words (SB–Sun distance) | **collision** with $\rho_c$ |
| $\mu_s$ | words (solar gravitational parameter) | **collision** with $\mu_\perp$, $\mu_\parallel$, $\mu_0$ |
| $\theta$, $\gamma$ (text); $\vartheta$, $\Phi$/$\varphi$ (nomenclature, Fig. 2) | words (azimuth and elevation in the flight frame) | **collisions** with $\theta$, $\gamma$, $\boldsymbol\vartheta$ |
| $\sigma_x$ | words (standard deviation) | **collision** with $\sigma_{sk}$ |
| $\alpha_a$, $\alpha_b$, $\sigma_\alpha$ | words (ejecta-cone angles) | **collision** with $\alpha_{\mathrm B}$, $\alpha_E$ |
| $\varepsilon_k$, $P_k^+$, $n$ | words (NEES, a-posteriori covariance, state dimension) | **collisions** with $\varepsilon_0$, $P$, $n_s$ |
| $R$, $D$, $el$, $az$, $R_J$ | words (range, Doppler, Delta-DOR angles, direction-cosine matrix) | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Delchambre_Momentum_enhancement_factor_estimation_for_asteroid_redirect.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier), 12 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.05.050, printed on page 1
     and checked on Crossref: title, four authors, Acta Astronaut.
     151:125–136 match; issue October 2018 (no published-online field on
     Crossref); page 1 gives received 22 Nov 2017, revised 23 May 2018,
     accepted 26 May 2018, online 1 Jun 2018. Page 1 matches the filename
     title.
   * **How it was read.** Full text layer; pages 127, 128, 129, 131, 132
     and 133 rendered to check equations and tables. Figs. 1, 4, 5, 8, 9
     and 10 were not rendered: their numbers come from text and captions.
     Supplementary data (online only) not read.
   * **Recorded as printed.**
     * Eqs. 7–9 put $|\Delta\mathbf v_{sc}|$ in the denominators where
       differentiating Eq. 4 gives $|\mathbf u_{sc}|$; since
       $|\Delta\mathbf v_{sc}|=m|\mathbf u_{sc}|/M$, printed Eq. 7 equals
       $\beta_{lin}/m$ instead of $\beta_{lin}/M$ and Eq. 8 is off by
       $M/m$. Eq. 10 correctly uses $\mathbf u_{sc}$. §5 and Eqs. 42–43
       also label the impactor-velocity term "$\Delta v_{sc}$". Whether
       the computed results used the correct derivatives cannot be told.
     * Eq. 19 prints $a=\sqrt{\mu_s\rho/(2\mu_s-\rho v_{//}^2)}$; vis-viva
       has no square root and the printed form has units of √m. Eq. 20 is
       consistent with the correct form.
     * Eq. 22: the $\rho$ and $\mu_s$ terms are partials of a single
       velocity, not of $v^+-v^-$; the $\mu_s$ partial lacks the factor
       1/2; the $a^+$ partial carries a sign that is immaterial once
       squared.
     * Eq. 34: the $\theta_{sb}$ sensitivity has $\cos\theta$ where
       differentiating Eq. 28 gives $\cos^2\theta$.
     * Eqs. 31–32: the left-hand side reads $\sigma^2_{\Delta v_{//sb}}$ in
       the text layer, but the equations give the uncertainty of
       $\Delta v_{/\perp sb}$; the subscript is ambiguous on the rendered
       page (low-confidence flag).
     * Eqs. 42–43: the impactor-mass term is printed with $\sigma^2_M$
       instead of $\sigma^2_m$.
     * Table 2 (absolute SB filter) pairs "Impactor S/C Mass Uncertainty"
       and "Impactor Velocity Uncertainty" with 1% and 5% (3σ), while §3.1–3.3
       assign 1% to the SB mass, 5% to the impactor mass and
       [0.1 0.1 0.3] m/s (1σ) to the impactor velocity; Table 2 also lists
       [0.1 0.1 0.3] m/s under the Explorer filter. Labels or values are
       misassigned.
     * Table 1: SB inertial position "[−0.79 1.05 0.36]·10¹¹ (km)", of
       magnitude about $1.36\times10^{11}$ km (≈910 AU), implausible for a
       NEO; $10^{11}$ m or $10^8$ km would give ≈0.94 AU. The velocity
       "[6.21 3.80 2.40]·10¹ km/s" has magnitude ≈77 km/s, high near 1 AU.
       Neither enters the $\beta_{lin}$ formula. Unresolved.
     * Convergence times: 3 h (§3.4.1), 2 h filter resumption (§4), 3–4 h
       (§5, Fig. 10). Minor.
     * Azimuth/elevation are $\theta,\gamma$ in the text, $\vartheta$
       (listed twice) and $\Phi$ in the nomenclature, $\vartheta,\varphi$ in
       Fig. 2.
     * The abstract says "after only 1 week of monitoring", the conclusion
       "overall monitoring time of 2 weeks": both fit 7 days before plus
       7 days after impact.
     * §4 uses "CEKF" without definition or reference; the Monte Carlo
       sample size and the NEES interval $r_1,r_2$ are not reported.
     * Reader's check: $M|\Delta v_{sb}|/(m|u_{sc}|)=5.88\times10^9\times5.51\times10^{-3}/(1294\times9610)=2.605$
       and $mu_{sc}/M=2.115$ mm/s, both consistent with Table 1.
     * Reader's check: the Fig. 9 errors are 2.26%, 1.81% and 2.03% of the
       true components; the x component slightly exceeds the stated 2.2%.
   * **Reference list.** 31 printed entries, numbered [1]–[7], [11],
     [12], [14]–[35] (numbers [8]–[10] and [13] are absent and never
     cited), matching the Crossref reference count of 31. Kept as printed:
     [19] first author "Plätzold" (Pätzold), [27] "A. Vallado"
     (D.A. Vallado), [14] co-authors "Joshua, P.E." and "Ellen, S.H."
     (garbled J.P. Emery and E.S. Howell); [3] has no year. Only [17]
     prints a DOI.
