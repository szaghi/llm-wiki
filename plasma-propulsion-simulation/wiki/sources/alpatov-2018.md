---
type: Source
title: "Alpatov, Khoroshylov & Bombardelli (2018) — Relative control of an ion beam shepherd satellite using the impulse compensation thruster"
description: "Designs a robust H-infinity controller that holds an ion-beam-shepherd satellite 7 m from a debris object using only small variations of the impulse compensation thruster along track, with the beam force on the debris taken from a self-similar conical far-plume model and bounded by the impulse-transfer thrust, and estimates a 100-day de-orbit for 10.58 kg of xenon against 10.59 kg of xenon plus 12.93 kg of hydrazine for a conventional scheme."
resource: "doi:10.1016/j.actaastro.2018.06.056"
source_kind: paper
authors: [Alpatov A., Khoroshylov S., Bombardelli C.]
year: 2018
venue: "Acta Astronaut. 151:543–554"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Alpatov_Relative_control_of_an_ion_beam_shepherd_satellite_using_the.pdf"
tags: [ion-thruster, plume, debris-removal, control]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper treats the relative-position control of an
[ion beam shepherd](/definitions/ion-beam-shepherd.md) (IBS): a shepherd
satellite carries an impulse transfer thruster (ITT), whose xenon ion plume
pushes a space-debris object (SDO), and an impulse compensation thruster
(ICT) pointed the other way to cancel the reaction. The shepherd must stay a
few debris diameters ahead of the object, and the in-plane relative dynamics
are unstable. The authors keep the ITT thrust at its maximum and use only a
small along-track variation of the ICT thrust as actuator, holding the
shepherd at $x=0$, $y=-7$ m in the local-vertical/local-horizontal frame.

The relative dynamics are linearized in-plane equations after Lawden. The ion
beam force on the debris enters as a bounded perturbation, computed with the
authors' earlier central-projection method (Alpatov et al. 2016, ref. [8])
and a self-similar conical far-plume model (after Merino et al. 2015,
ref. [14]); both are used, not derived here. Parametric uncertainty (orbital
rate and its derivative, the gravity-gradient parameter, both masses) is
written as linear fractional transformations, and a 7-state mixed-sensitivity
$H_\infty$ controller is synthesized by linear matrix inequalities. A
structured-singular-value check confirms robust stability and performance.
Nonlinear simulations with a Cyclone-3 upper stage as debris (drag, solar
radiation pressure, tumbling) give position errors within ±0.6 m and ICT
thrust variations within 10 % of nominal. The propellant budget of a 100-day
de-orbit is 10.58 kg of xenon, against 10.59 kg of xenon plus 12.93 kg of
hydrazine for a constant-ICT scheme with hydrazine thrusters for relative
control. The plasma content of the paper is the plume-force model of §4; the
rest is guidance and control.

# Key claims

1. **Open-loop instability** (Introduction, attributed to refs. [10,11]):
   the in-plane shepherd–debris relative dynamics are always unstable; the
   out-of-plane motion is stable only if the radial destabilizing effect of
   the beam does not exceed the gravity-gradient restoring force. Stated,
   attributed.
2. **Along-track controllability** (§3): with the variable ICT thrust acting
   along track as the only input, the controllability matrix has full rank.
   Stated; the rank computation is not shown.
3. **Beam force on a surface element** (§4, eqs. 6–7, after ref. [8]): the
   force on an element of the debris surface is the ion mass times ion
   density times ion velocity times the ion flux normal to the element,
   integrated over the irradiated surface. Used, not derived.
4. **Far-plume model** (§4, eqs. 8–11, after refs. [8,13,14]): ion density
   Gaussian in radius with a self-similar width; $C=6$ in the Gaussian
   exponent puts about 95 % of the ion current inside the reference radius
   (ref. [13]); "for typical values of the ion Mach number greater than or
   equal to 30 and distances to the SDO less than 10 m, it is safe to assume
   that the beam is conical with very little error" (ref. [14]); the axial
   ion velocity is constant in the "highly hypersonic" beam; the radial
   velocity grows linearly with radius. Used, not derived.
5. **Central projection and force bound** (§4, eq. 13, attributed to
   ref. [8]): the beam force on a 3D body can be computed from its central
   projection; when the whole beam hits the debris, the transmitted force is
   approximately the ITT thrust along $-y$, and partial overlap gives less
   along $y$ and small $x$ and $z$ components. Stated; this bound is the
   design assumption.
6. **Perturbation bounds** (§6, eq. 21): along $y$, at most
   $2.5\times10^{-5}$ N/kg (ITT thrust over the minimum debris mass), a
   bound justified because the beam acceleration exceeds the differential
   orbital perturbation by an order of magnitude even at the end of the
   mission; along $x$, $2\times10^{-7}$ N/kg, "selected based on the
   conservative estimate of the orbital perturbations at the end of the
   mission" (an orbital-perturbation bound, not a beam force); actuation
   errors $1\times10^{-4}$ N per axis; sensor errors 0.1 m. Stated.
7. **$H_\infty$ design** (§6, eqs. 18–27, Table 3, Appendix):
   mixed-sensitivity weights (eqs. 23–24), projective LMI method (ref. [20]),
   minimum attenuation level 0.978, 7th-order controller discretized by the
   bilinear transform at 1 Hz. Shown (matrices printed).
8. **Robustness** (§7, eqs. 28–29, Fig. 13): structured-singular-value upper
   bound 0.845 < 1, hence robust stability and performance over the whole
   uncertainty set. Shown (numerical bound).
9. **Accuracy** (§8): the base controller keeps the position within ±0.6 m
   for all mass combinations; sensor noise adds up to ±0.05 m; errors grow
   with eccentricity because the design model is time-invariant. Shown.
10. **Bandwidth limit** (§8): the achievable bandwidth is limited by a
    right-half-plane zero of the plant at 0.0019 (units not printed). Stated.
11. **Propellant** (§8): de-orbit at about 3 km/day for about 100 days from
    640 km; total ICT impulse $3.525\times10^5$ N s gives 10.58 kg of xenon at
    $I_{sp}=3400$ s; the conventional scheme (constant ICT plus 2×2 hydrazine
    thrusters of 2 N, 230 s) needs 10.59 kg of xenon and 12.93 kg of
    hydrazine. Shown (numerical estimate).
12. **Delays** (§8): 0.2 s sensor and actuator delays, shorter than the 1 s
    sampling period, do not degrade performance. Stated as a simulation
    outcome, no figure.
13. **Throttling feasibility** (Introduction, §8, attributed to ref. [4]):
    simulations and tests on flight-representative GOCE hardware showed
    thrust control within each 0.1 s demand period. Stated, attributed.

# Methods

* **Dynamics.** Linearized in-plane relative equations (eq. 1, after Lawden,
  ref. [12]) in a frame centred on the shepherd, $x$ radial, $y$ along track,
  $z$ orbit normal; orbital rate, its derivative and the gravity-gradient
  parameter from Keplerian elements (eq. 2); state-space form eq. 5. Debris
  attitude from Euler's equations (eq. 12) with beam, drag, gravity-gradient
  and solar-radiation-pressure torques.
* **Plume.** Xenon ion beam with the parameters of Table 2: far-region
  initial density $4.13\times10^{15}$ m⁻³, ion mass printed
  $2.8\times10^{-25}$ kg (see Recorded as printed), initial 95 % beam radius
  0.0808 m, axial ion velocity 71580 m/s, initial divergence half-angle 7°
  (ref. [15]), $I_{sp}=3400$ s, ITT thrust 0.031 N. Debris: Cyclone-3 upper
  stage as a cylinder 2.6 m high and 2.2 m in diameter. The force is
  computed by eqs. 6–7 with the algorithms of ref. [8].
* **Uncertainty.** Nominal and deviation values: orbital rate
  $1.15\times10^{-3}$ rad/s ± $0.3\times10^{-3}$; its derivative 0 ±
  $3\times10^{-7}$ rad/s²; gravity-gradient parameter $1.35\times10^{-6}$ s⁻²
  ± $0.55\times10^{-6}$; shepherd mass 500 ± 50 kg; debris mass 1575 ± 315 kg
  (eqs. 14–17).
* **Controller.** Generalized plant eqs. 18–20, weights eqs. 23–24
  (Table 3); modified designs MC1 and MC2 (Table 5).
* **Validation.** Nonlinear orbital dynamics with central gravity, thrusters,
  beam force, drag and solar radiation pressure; Gaussian sensor noise and
  actuation errors; start at 640 km; simulated masses 450 kg (shepherd) and
  1890 kg (debris); nominal ICT thrust
  $F_{\mathrm{CT}}=-F_{\mathrm{IT}}\,(1+\text{shepherd mass}/\text{debris mass})$
  with nominal masses (eq. 30).

# Tests and results

| Case | Location | Conditions | Result |
|---|---|---|---|
| Base controller, near-circular | §8, Figs. 14–17 | eccentricity 0.002, with and without noise | debris tumbles, beam force unchanged (whole cone hits) |
| Debris displaced out of plane | §8, Figs. 18–20 | $z=1$ m, eccentricity 0.002 | beam force varies strongly with tumbling; controller copes |
| Eccentric orbits | §8, Figs. 21–23 | eccentricity 0.02, 0.04 | errors grow with eccentricity; beam transmission still good at 0.04 |
| Sensor noise | §8 | base controller | extra error up to ±0.05 m |
| ICT thrust variation | §8, Fig. 25 | eccentricity 0.04 | within 10 % of nominal; variable-component impulse over 25000 s 2.27 (noise) and 2.2 (noise-free), printed "N"; nominal ICT impulse 1000 N s |
| Non-zero initial conditions | §8, Figs. 26–27 | sensor noise | much wider thrust variation, overshoot in $y$, no collision |
| All mass combinations | §8 | §5 bounds | within ±0.6 m |
| MC1 | §8, Fig. 28, Table 5 | eccentricity 0.04 | ±0.28 m noise-free, ±0.4 m with noise |
| MC2 | §8, Figs. 29–30 | eccentricity 0.04 | ±0.2 m noise-free; with noise about as the base controller; ICT variation orders of magnitude larger |
| Delays | §8 | 0.2 s on sensors and ICT | no deterioration |
| Propellant | §8 | 100-day de-orbit | 10.58 kg Xe vs 10.59 kg Xe + 12.93 kg N₂H₄ (conventional, ±0.1 m) |
| Robustness | §7, Fig. 13 | nominal design | structured singular value at most 0.845 |

# Notation map

| Alpatov et al. (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $m_I$ | $m_i$ | xenon ion mass |
| $n_I$, $n_0$ | $n_i$, $n_0$ | $n_0$ the density at the start of the far region, a reference value as in the registry |
| $\mathbf U$ | $\mathbf u_i$ | ion fluid velocity |
| $u_z$, $u_{z0}$, $u_r$ | $u_{i,z}$, words, $u_{i,r}$ | beam-axis components; $z$ here is the beam axis |
| $r$, $z$ (eq. 8) | $r$, $z$ | beam-axis cylindrical coordinates |
| $\tilde r$, $\tilde z$ | words | normalized by the initial beam radius; **collision:** registry $\tilde{(\cdot)}$ is a fluctuation |
| $R_0$ | words (initial 95 % beam radius) | **collision:** the paper's $R$ is also the orbital radius (eq. 2) |
| $h(\tilde z)$, $C$ | words | self-similarity function; Gaussian constant |
| $\alpha$ | words (initial divergence half-angle) | **collision** with $\alpha_{\mathrm B}$, $\alpha_E$ |
| $\mathbf V$, $\mathrm ds$ | words | unit surface normal, surface element |
| $f_T$ | $F_{\mathrm{IT}}$ | ITT thrust, 0.031 N |
| $f_c$, $f_c^n$, $f_c^v$ | $F_{\mathrm{CT}}$; words | ICT thrust, nominal and variable parts |
| $\mathbf F_I^d$ | words | beam force on the debris |
| $x$, $y$, $z$ (LVLH) | words | **collision:** radial, along-track, orbit-normal; not simulation-domain Cartesian, $z$ not thruster axial |
| $\omega$, $\dot\omega$ | words (orbital rate) | **collision** with registry $\omega$ (mode angular frequency) |
| $k=Gm/R^3$ | words (gravity-gradient parameter) | **collision** with registry $k$ (wavenumber) |
| $\Omega$, $I$, $\mathbf T$ | words | debris angular velocity, inertia tensor, torque; **collision** with $\Omega_e$ |
| $\gamma$, $\gamma_{\min}$ | words ($H_\infty$ attenuation level) | **collision:** registry $\gamma$ is the polytropic index |
| $\mu(N)$ | words (structured singular value) | **collision** with $\mu_0$, $\mu_\perp$ |
| $\Delta x$, $\Delta y$ | words (measurement noise) | **collision** with registry $\Delta x$ (cell size) |
| $I_{sp}$ | $I_{sp}$ | |
| $m^s$, $m^d$ | words | shepherd and debris masses |
| $\varepsilon$, $\upsilon$ ($\nu$) | words | eccentricity, true anomaly; **collision** risk with $\varepsilon_0$, $\nu_{sk}$ |

# Pages created or updated

* [Ion beam shepherd](/definitions/ion-beam-shepherd.md) — created; this
  source is its main one.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Alpatov_Relative_control_of_an_ion_beam_shepherd_satellite_using_the.pdf`.
   * **Version.** Publisher's typeset version (Elsevier), 12 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.056, printed on page 1
     and checked on Crossref: title, three authors, Acta Astronaut.
     151:543–554, issue October 2018, reference count 24, all agree. Page 1:
     received 9 Jan 2018, revised 19 May 2018, accepted 28 Jun 2018, online
     6 Jul 2018. Page 1 matches the filename title. Funding: EU FP7 grant
     607457 (LEOSWEEP).
   * **How it was read.** Full text layer; all equations checked on rendered
     pages 2–5 (pp. 544–547) and Table 2 on p. 545, none illegible. Figures
     7–30 are plots; only values stated in the text are recorded.
   * **Recorded as printed.**
     * Eq. 1, radial row: $\ddot x-\omega^2x-2\omega\dot y-\dot\omega y-kx$
       gives a coefficient $\omega^2+k$ on $x$, while matrix $A$ (eq. 5,
       row 3) has $\omega^2+2k$; the standard linearized radial equation has
       $2k$, so eq. 1 drops a factor 2 (pp. 544–545).
     * Eq. 2 prints the orbital rate as $\sqrt{Gm/p^3}(1+\varepsilon\cos\upsilon)$;
       the Keplerian rate has the bracket squared, and the printed derivative
       is consistent only with the squared form. The true anomaly is written
       both $\upsilon$ and $\nu$.
     * The text attributes the along-track linear regulator to "Starin et
       al. [7]"; ref. [7] is Kumar(a), Bang & Tahk (2007), Starin et al. is
       ref. [6].
     * Fig. 14 is cited for both the noise-free and the noise case
       (sub-panels intended); the de-orbit rate "≈3 km/day (see Fig. 17)"
       points to the debris angular-velocity figure, the altitude is Fig. 15.
     * $G_{ij}$ "using the matrices of the state-space representation (4)"
       should refer to eqs. 18/20; the Appendix "matrices of the
       representation (25)" should be eq. 27.
     * Units: the variable-component ICT impulse is printed "2.27 N" and
       "2.2 N" (N s meant); the hydrazine minimum impulse bit "0.01 N"
       (N s meant).
     * Table 1 allows eccentricity up to 0.05 and Fig. 3 plots bounds for
       0.05, while simulations go to 0.04 (noted, not a contradiction).
     * Fig. 12 caption typo "NUx and.NUy".
     * Table 2 prints the xenon ion mass as $2.8\times10^{-25}$ kg (checked
       on the rendered page). Reader's check: the xenon ion mass is
       $2.18\times10^{-25}$ kg. Integrating the Gaussian momentum flux of
       eq. 8 at the start of the far region with the Table 2 values gives
       0.0315 N with $2.18\times10^{-25}$ kg, matching the printed ITT
       thrust 0.031 N, and 0.0405 N with $2.8\times10^{-25}$ kg; the ion
       energy at 71580 m/s is 3.49 keV with the xenon mass. The printed value
       is most likely a dropped digit.
     * Table 2 gives $I_{sp}=3400$ s together with an axial ion velocity of
       71580 m/s. Reader's check: 71580 m/s corresponds to 7300 s; with
       3400 s the ITT mass flow is $9.3\times10^{-7}$ kg/s against an ion
       mass flow of $4.3\times10^{-7}$ kg/s (0.031 N / 71580 m/s), i.e. an
       implied propellant utilization of about 0.47, not stated. The xenon
       budget (10.58 kg) uses 3400 s.
     * Reader's check: $3.525\times10^5$ N s$/(3400\times9.81$ m/s²$)=10.57$ kg,
       consistent with 10.58 kg; $3.525\times10^5$ N s over 100 days is
       0.0408 N, equal to $0.031\times(1+500/1575)=0.0408$ N from eq. 30;
       3 km/day for 100 days takes the debris from 640 to 340 km.
   * **Reference list.** 24 printed entries, matching the Crossref count. In
     the bibliography, ref. [14] is the existing `merino-2015` (printed here
     without the article number) and ref. [1] the existing
     `bombardelli-2011`. Ref. [16] (Zhou, Doyle & Glover, *Robust and
     Optimal Control*, 1996) collides with an existing `zhou-1996` key for a
     different work. Ref. [7] prints the first author as "K.D. Kumara".
     Printed spellings kept: "Kept" (ref. [3]), "Brignton" (ref. [17]),
     "Willey" (ref. [21]).
