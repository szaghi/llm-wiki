---
type: Source
title: "Pallone, Pontani & Teofilatto (2018) — Performance evaluation methodology for multistage launch vehicles with high-fidelity modeling"
description: "Estimates the payload-versus-circular-orbit-altitude performance of the four-stage Scout launcher with DATCOM-fitted aerodynamics, open-loop constant-angle-of-attack lower stages, an analytic coast and a minimum-principle upper-stage burn, solving the six-parameter problem with a firework algorithm and reporting 785–2474 km for 200–50 kg payloads."
resource: "doi:10.1016/j.actaastro.2018.06.012"
source_kind: paper
authors: [Pallone M., Pontani M., Teofilatto P.]
year: 2018
venue: "Acta Astronaut. 151:522–531"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Pallone_Performance_evaluation_methodology_for_multistage_launch_veh.pdf"
tags: [context, launch-vehicle, trajectory-optimization, optimal-control, heuristic-optimization]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper proposes a quick estimate of the performance of a multistage
launch vehicle, i.e. payload mass against circular-orbit altitude, and
applies it to the four-stage Scout rocket, modelled as a point mass with
two degrees of freedom in the equatorial plane, launched eastward.
Aerodynamics come from Missile DATCOM: drag and lift coefficients are
fitted with fourth-degree polynomials in angle of attack and Mach number
(subsonic and supersonic sets), with a Matlab interpolation routine in
the transonic range. Thrust and propellant mass are interpolated linearly
from the Scout manual. The first three stages fly open-loop at constant
angles of attack, an analytic Keplerian coast follows, and the
fourth-stage burn is made indirectly optimal through Pontryagin's minimum
principle, maximising the final circular-orbit radius. The resulting
six-parameter problem (three angles of attack, two initial costates, a
coast true-anomaly increment) is solved by a firework algorithm, a
stochastic swarm heuristic, that drives an auxiliary injection-error
function toward zero. For payloads from 50 to 200 kg the paper reports
injection altitudes from 2474 km down to 785 km and claims that they
"considerably outperform" the Scout manual curve.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Efficiency** (§1, §3). The method gives a fast, near-optimal
   performance evaluation with high-fidelity aerodynamics and propulsion
   at "only a limited amount of computational effort". Stated; no timings
   are given.
2. **Dual formulation** (§3, Eqs. 19–20). For a given payload and full
   propellant use, maximise the circular-orbit altitude, $J=-k_1r_f$, with
   $v_{I,f}=\sqrt{\mu_E/r_f}$ and $\gamma_{I,f}=0$; contrasted with the
   usual minimum-upper-stage-propellant formulation.
3. **Eliminated costate** (§3.2, Eqs. 30–31). Stationarity with respect to
   the coast true-anomaly parameter, $\partial\Phi/\partial f_4=0$, gives
   $\lambda_{30}$ in closed form in terms of $\lambda_{10}$, $\lambda_{20}$
   and $f_4$, removing one unknown. Derived.
4. **Optimal thrust angle** (Eqs. 33–34).
   $\sin\alpha_T^*=-\frac{\lambda_3}{x_2}\Bigl[\bigl(\frac{\lambda_3}{x_2}\bigr)^2+\lambda_2^2\Bigr]^{-1/2}$,
   $\cos\alpha_T^*=-\lambda_2\Bigl[\bigl(\frac{\lambda_3}{x_2}\bigr)^2+\lambda_2^2\Bigr]^{-1/2}$.
   Derived; consistent with the Hamiltonian of Eq. 23 (reader's check).
5. **Costate scaling** (§3.3). Because the transversality condition can be
   ignored, the initial costates can be searched in $[-1,1]$ and their
   scaling recovered afterwards. Stated, no proof.
6. **Results** (Table 5, §3.3): optimal parameters and injection altitudes
   for 50–200 kg payloads (see Tests and results), with coast durations of
   944.4 s (50 kg) and 540.1 s (200 kg). Shown numerically.
7. **Against the Scout manual** (§3.3, §4, Fig. 9). The results
   "considerably outperform" the manual's performance curve. Shown only as
   markers on the manual's chart; the paper does not discuss that its
   idealisations (equatorial eastward launch, point mass, no upper-stage
   aerodynamics, a fixed 5 s vertical rise, optimal upper-stage steering)
   differ from the manual's assumptions, so the comparison is not like for
   like.
8. **Aerodynamic load** (§3.3). With constant angles of attack in
   suitable ranges the aerodynamic load stays bounded; for 50 kg the
   product of dynamic pressure and angle of attack never exceeds
   80000 Pa·deg. Stated; no figure.
9. **Robustness** (abstract, §4). "The numerical results unequivocally
   prove that the methodology at hand is rather robust, effective, and
   accurate". Rhetorical: no repeated stochastic runs and no comparison
   with a reference direct or indirect solver are reported.
10. **Coast duration** (§1, attributed to Lu et al.). Coast duration
    usually increases with injection altitude; consistent with Table 5.

# Methods

* **Vehicle** (§2, Table 1): Scout, four subrockets with structural /
  propellant masses 1736/12810, 915/3749, 346/1173 and 33/281 kg; each
  stage's payload is the next stage's initial mass (Eq. 1); final payload
  50–200 kg. Thrust and propellant mass interpolated linearly from the
  Scout manual (Figs. 2–3).
* **Aerodynamics** (§2.2): lift and drag
  $\tfrac12C_{L,D}(\alpha,M)S^{(i)}\rho v^2$ (Eq. 2); reference areas
  1.026, 0.487 and 0.458 m² for subrockets 1–3 (Table 2); DATCOM data fitted
  by a full bivariate quartic in angle of attack and Mach number with 15
  coefficients (Eq. 3), subsonic ($M\in[0,0.8]$, Table 3) and supersonic
  ($M\in[1.2,10]$, Table 4), Matlab interpolation in $[0.8,1.2]$; the
  fourth stage flies above about 120 km and its aerodynamics are
  neglected.
* **Dynamics** (§2.2–2.3, Eqs. 4–9): Earth-fixed frame rotating at
  $\omega_E=7.292115\times10^{-5}$ s⁻¹; planar equations for radius,
  flight-path angle and relative speed with thrust, gravity
  ($\mu_E=398600.4$ km³/s²), lift, drag, Coriolis and centrifugal terms;
  thrust along the body axis (Eq. 21). Initial conditions: Earth radius,
  flight-path angle 86°, speed 1 m/s, radial thrust for the first 5 s
  (Eqs. 36–37). The integrator is not named.
* **Coast** (Eqs. 10–18, 22): conversion to inertial states and in-plane
  orbital elements; propagation by a true-anomaly increment $\Delta f$;
  ignition time from Kepler's equation.
* **Upper-stage optimal control** (Eqs. 23–34): inertial state
  $\mathbf x=[r,v_I,\gamma_I]^T$, Hamiltonian (Eq. 23), boundary function
  with five multipliers (Eq. 24), adjoint equations (Eqs. 25–27,
  consistent with $-\partial H/\partial x_k$ on the reader's check),
  transversality and sign conditions (Eqs. 28–29), control law
  (Eqs. 32–34).
* **Solution** (§3.2): unknowns
  $\{\alpha_1,\alpha_2,\alpha_3,\lambda_{10},\lambda_{20},\Delta f\}$;
  auxiliary objective
  $J'=\bigl|x_{2f}-\sqrt{\mu_E/x_{1f}}\bigr|+|x_{3f}|$ (Eq. 35). Search
  ranges: $\alpha_1$ 0–5°, $\alpha_{2,3}$ 0–10°, costates in $[-1,1]$,
  $\Delta f$ in $[0,\pi]$. Canonical units: DU = 6378.165 km,
  TU = 806.8 s.
* **Firework algorithm** (Appendix A, after Tan): decreasing minimum
  amplitude, fitness-based spark numbers and amplitudes, displacement and
  Gaussian operators, uniform re-mapping of out-of-bound components,
  elitist plus random selection; 10 fireworks, at most 30 sparks, 50000
  evaluations; stop when $J'$ reaches order $10^{-4}$.

# Tests and results

One test family: Scout, equatorial eastward launch (Table 5, §3.3;
altitudes with $R_E=6378.136$ km).

| Payload [kg] | $\alpha_1$ [deg] | $\alpha_2$ [deg] | $\alpha_3$ [deg] | $\Delta f$ [deg] | Altitude [km] |
|---|---|---|---|---|---|
| 50 | 1.425 | 1.16 | 8.98 | 19.02 | 2474.08 |
| 75 | 1.93 | 4.32 | 2.22 | 22.99 | 2154.76 |
| 100 | 2.27 | 5.32 | 2.50 | 25.17 | 1808.20 |
| 125 | 2.66 | 4.66 | 2.33 | 26.24 | 1506.31 |
| 150 | 3.09 | 2.70 | 2.07 | 26.42 | 1251.16 |
| 175 | 3.29 | 4.75 | 0.06 | 25.61 | 997.93 |
| 200 | 3.60 | 2.78 | 2.12 | 24.07 | 784.83 |

* Fig. 6: convergence of $J'$ against the number of evaluations for the
  seven payloads, on an axis running to about 7000 evaluations.
* Figs. 7–8: state histories and control for 50 and 200 kg; in both the
  last stage makes a nearly horizontal circularisation burn.
* Fig. 9: the optimised points lie above the Scout manual's
  circular-orbit performance curve.

# Notation map

The paper is outside the bundle's domain; its symbols are kept in words
except the thrust.

| Pallone et al. (2018) | Registry | Note |
|---|---|---|
| $T$, $T^{(j)}$ | $F$ (thrust) | **collision:** registry $T_s$ is temperature |
| $m$, $m_0^{(i)}$, $m_S$, $m_P$, $m_U$ | words (vehicle, structural, propellant, payload mass) | **collision** with $m_s$ (species mass) |
| $\gamma$, $\gamma_I$ | words (flight-path angle) | **collision:** registry $\gamma$ is the polytropic index |
| $\alpha$, $\alpha_i$, $\alpha_T$ | words (angle of attack, thrust angle) | not $\alpha_{\mathrm B}$, $\alpha_E$, $\alpha_\tau$, $\alpha_n$ |
| $r$ | words (radius from the Earth's centre) | **collision:** registry $r$ is the thruster radial coordinate |
| $v$, $v_I$ | words (relative and inertial speed) | not the particle velocity $\mathbf v$ |
| $L$, $D$ | words (lift, drag) | **collision:** registry $L$ is a length |
| $S^{(i)}$ | words (aerodynamic reference area) | **collision** with $S_j$ |
| $M$ | words (Mach number) | registry has only $M_A$ |
| $\rho$ | words (atmospheric density) | not $\rho_c$ |
| $\mu_E$ | words (Earth gravitational parameter) | **collision** with $\mu_\perp$, $\mu_\parallel$, $\mu_0$ |
| $\omega_E$ | words (Earth rotation rate) | registry $\omega$ is a mode angular frequency |
| $\mathbf E$, $\hat E$, $E(t)$ | words (east unit vector, eccentric anomaly) | **collision** with the electric field $\mathbf E$ |
| $e$ | words (eccentricity) | **collision** with the elementary charge $e$ |
| $a$, $f$, $f_4$, $\Delta f$ | words (semimajor axis, true anomaly and its increment) | **collision** of $f$ with $f_s$, $f_\varepsilon$, $f_m$, $f_g$, $f_{\mathrm{BM}}$ |
| $H$ | words (Hamiltonian) | **collision:** registry $H$ is spectral entropy |
| $\lambda_k$ | words (costates) | **collision** with $\lambda_D$, $\lambda_{\mathrm{mfp}}$, $\lambda_w$ |
| $\nu_k$ | words (boundary multipliers) | **collision** with $\nu_{sk}$ |
| $\xi$, $\theta_g$ | words (longitude, Greenwich sidereal angle) | registry $\theta$ is the azimuthal coordinate |
| $k_1$ | words (objective weight) | **collision:** registry $k$ is a wavenumber |
| $J$, $J'$, $Q$, $N_F$, $N_S$ | words (objective, auxiliary objective, dynamic pressure, firework counts) | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Pallone_Performance_evaluation_methodology_for_multistage_launch_veh.pdf`.
   * **Version.** Publisher's final typeset PDF, 10 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.012, printed on page 1
     and checked on Crossref: title, the three authors, Acta Astronaut.
     151:522–531 match; published in print October 2018 (no
     published-online field on Crossref). Page 1 gives received 10 Feb
     2017, accepted 5 Jun 2018, online 14 Jun 2018. Page 1 matches the
     filename title.
   * **How it was read.** Full text layer; Eqs. 3, 8, 9, 12–18 and 22–35,
     garbled in the text layer, read from the rendered pages 525–528.
     Figs. 2, 3 and 6–9 are plots; only values quoted in the text were
     taken.
   * **Recorded as printed.**
     * Eq. 13 prints $e=\sqrt{1-rv_I\cos\gamma_I/(\mu_Ea)}$, dimensionally
       inconsistent; reader's check: from the angular momentum
       $rv_I\cos\gamma_I=\sqrt{\mu_Ea(1-e^2)}$ the numerator must be squared
       (confirmed as printed on the rendered page 526).
     * Eq. 31: the second term's denominator reads $e_2+\cos f_4$, the
       first term's $e_3+\cos f_4$; evidently $e_3$ (rendered page 527).
     * Eq. 22 writes $E(t_{b3})$ and $E(t_{B3})$ for the same event
       (third-stage burnout).
     * Two Earth radii: DU = 6378.165 km (§3.3), $R_E=6378.136$ km (below
       Table 5).
     * The stopping rule ($J'$ of order $10^{-4}$, 50000 evaluations)
       against Fig. 6: only the 200 kg curve nears $10^{-4}$, the others
       plateau between about $10^{-3}$ and $4\times10^{-4}$, and every curve
       ends below about 6500 evaluations (read off the figure).
     * The abstract and §4 call one unknown "the coast time interval"; the
       parameter is the true-anomaly increment $\Delta f$, the coast time
       following from Eq. 22.
     * The final-time range is printed
       "$1/\mathrm{TU}\le t_f\le30/\mathrm{TU}$" (inverse time units), and
       $t_f$ is not among the six unknowns.
     * Table 5's optimal angles are non-monotonic ($\alpha_3$ = 8.98° at
       50 kg, 0.06° at 175 kg, about 2° elsewhere; $\alpha_2$ alternating
       between 2.7° and 5.3°) while the altitude trend is smooth: a flat
       objective or different near-optima of the stochastic search, which
       weakens the robustness claim.
     * The Table 1 caption says "first three subrockets" over four rows;
       Table 2 is headed with index $j$ and the row is labelled $S^{(i)}$.
   * **Reference list.** 20 printed entries, matching the Crossref
     reference count. Kept as printed: refs. [1] and [2] are both printed
     "part 1" (ref. [2], the application part, should be part 2); ref. [4]
     has no volume, year or pages; ref. [18] prints the garbled
     "Ingegneria, 2000, p. 2008".
