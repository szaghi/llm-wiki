---
type: Source
title: "Gomez Jenkins, Krejci & Lozano (2018) — CubeSat constellation management using Ionic Liquid Electrospray Propulsion"
description: "Optimizes, by Differential Evolution on Gauss's variational equations with J2 and drag, the drift-rate manoeuvre that separates two 3U CubeSats by 180° in right ascension of the ascending node with a projected ionic-liquid electrospray thruster (2500 s, 5.7 W), giving 164.2 d and 85 g at minimum time and 245.1 d and 44 g at minimum propellant."
resource: "doi:10.1016/j.actaastro.2018.06.007"
source_kind: paper
authors: [Gomez Jenkins M., Krejci D., Lozano P.]
year: 2018
venue: "Acta Astronaut. 151:243–252"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Gomez_CubeSat_constellation_management_using_Ionic_Liquid_Electros.pdf"
tags: [electrospray, ionic-liquid, cubesat, mission-analysis, trajectory-optimization, low-thrust]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

A mission-analysis case study. Two 3U CubeSats (SatA, SatB) start in the
same 500 km, 28.5° orbit and must reach a 180° difference in right
ascension of the ascending node (RAAN), propelled by the MIT ion
electrospray propulsion system (iEPS). The authors use the indirect
"drift rate manoeuvre": SatB raises its semi-major axis by continuous
tangential thrust, coasts while the difference in J2 nodal-precession
rate accumulates the RAAN separation, then descends; SatA only compensates
drag. Orbits are propagated with Gauss's variational equations (secular
J2, NRLMSISE-00 drag with an attitude-dependent projected area, fixed-step
RK4 at 100 s), and the drift-orbit radius and drift time are chosen by
Differential Evolution (PyGMO). Three optimizations are reported: minimum
time (164.2 d, 85 g), minimum propellant (245.1 d, 44 g) and a hybrid with
out-of-plane thrusting in the drift orbit (160.6 d, 158 g). The
electrospray content is a short device description (§2) and a performance
table (Table 1), both attributed to earlier MIT work; the thruster enters
the dynamics only as a constant-power, constant-$I_{sp}$ acceleration
(Eqs. 2–3). No plasma, beam or emitter physics is modelled.

# Key claims

Orbital symbols below are the paper's own (see the notation map).

1. **Device description** (§2, attributed to Refs. [6–13]). Electrospray
   emitters accelerate charged particles extracted from an ionic-liquid
   propellant electrostatically, with no ionization volume. The MIT
   emitters are microfabricated arrays of porous emitters fed passively by
   capillarity from an unpressurized reservoir; menisci form at the
   emitter apex under electric pull and surface tension (Ref. [10]);
   hundreds of emitters operate in parallel (Ref. [9]). Stated, attributed.
   Consistent at the descriptive level with
   [Taccogna et al. (2023)](/sources/taccogna-2023.md), who class
   electrospray among the electrostatic thrusters that need only Poisson's
   equation.
2. **Measured single-thruster performance** (§2, attributed to Ref. [9]).
   A thruster (emitter array plus a 1 mL tank, about 5 g) gives
   11–12.5 μN and 760 s at 150 μA emission current and an operating voltage
   below 1000 V. Stated, attributed; not measured in this paper.
3. **Efficiency losses** (§2, attributed to Ref. [9]). The present
   emitters lose efficiency through an increased beam opening angle and a
   small droplet population that lowers the beam's mean specific charge.
   The authors state these losses are "not inherent to electrospray
   propulsion" and are "expected" to decrease. Stated (a projection, not
   shown).
4. **Current vs target system** (Table 1). Thruster efficiency 39.1% /
   60%; total efficiency 31.3% / 50%; specific impulse 760 s / 2500 s for
   the current (CPS) and target (TPS) propulsion systems. The TPS is a
   projected design; all simulations use it (§3.3).
5. **Spacecraft** (§2, Fig. 2). 3U CubeSat with one propulsion module of
   32 emitter chips (28 axial, 4 perpendicular for three-axis attitude
   control); wet mass 4.0 kg, propellant 0.5 kg, 5.7 W available to the
   thrusters.
6. **Thrust model** (§3.1, Eqs. 2–3). Acceleration $2\eta P/(m g I_{sp})$
   and mass rate $-2\eta P/(g I_{sp})^2$, i.e. in registry form
   $F=2\eta P/(g_0I_{sp})$ and $\dot m=2\eta P/(g_0I_{sp})^2$, which follow
   from $\eta=F^2/(2\dot mP)$ and $F=\dot m g_0I_{sp}$. The paper does not
   define $\eta$ (see Recorded as printed).
7. **Orbit model** (§3.1, Eqs. 1, 4–13, Appendix A Eqs. 40–46, from
   Ref. [19]). Thrust direction in the radial/along-track/normal frame from
   pitch, yaw and flight-path angle; secular J2 rates of node and perigee
   only (short- and long-period terms neglected as cyclical); drag
   $-\tfrac12\rho V^2 SC_D/m$ with no lift and no atmospheric rotation.
8. **Projected area of a cuboid** (§3.1, Eqs. 14–29), presented as "a
   method developed in this paper": edge vectors rotated by pitch and yaw,
   projected area the sum of three parallelograms; pure pitch
   $S=w(h\cos\alpha+l\sin\alpha)$ (Eq. 28), pure yaw
   $S=h(w\cos\beta+l\sin\beta)$ (Eq. 29). Derived.
9. **Optimization formulation** (§3.2, Eqs. 30–36, 39). Minimise final time
   (or propellant mass) subject to equal semi-major axis, zero
   eccentricity, equal inclination and a RAAN difference of $\pi$ at the
   final time; the RAAN constraint enters a weighted augmented cost
   $J=W_{t_f}t_f+W_{\Delta\Omega}(\Omega_1(t_f)-\Omega_2(t_f)-\pi)$ (paper
   symbols). Indirect (costate) methods are rejected because the problem is
   multi-point. Bang-bang schedule (Table 2): thrust along-track at maximum
   up, coast, thrust anti-along-track at maximum down.
10. **Hybrid control law** (Eqs. 37–38, from Ref. [22]): zero pitch, yaw
    switching between ±90° at the nodes, claimed to give the largest RAAN
    rate. As printed it is the inclination-change law (see Recorded as
    printed).
11. **Results** (§3.4, Table 5). Shown (simulation):
    * Sim 1, minimum time: drift-orbit semi-major axis 7377.96 km, drift
      time 78.0 d, total 164.2 d, propellant 0.085 kg, final RAAN
      difference 180.09°; drift-rate difference 1.46°/day.
    * Sim 2, minimum propellant: 7131.91 km, 200.0 d (the search-space
      upper bound), 245.1 d, 0.044 kg, 179.91°; drift-rate difference
      0.8°/day; +49% time and −48% propellant against Sim 1.
    * Sim 3, hybrid: 7377.84 km, 75.2 d, 160.6 d, 0.158 kg, 179.91°; −2%
      time and +86% propellant against Sim 1. The maximum RAAN-rate
      difference produced by the thruster is 0.1°/day, against 1.46°/day
      from the drift.
12. **Drag compensation** (§3.4, Fig. 10). At 500 km SatA loses 1 km of
    semi-major axis in about 81 days; 3 reboosts in 245 days cost 0.27 g.
    Shown.
13. **Conclusions** (§4). Out-of-plane thrusting to change RAAN directly is
    "not suitable" for CubeSat constellations (low RAAN-rate authority,
    180° attitude flips twice per revolution, Fig. 9); Differential
    Evolution gives "sub-optimal trajectories consistent with theoretical
    expectations". Stated; optimality is asserted, not shown (no
    convergence or repeatability study of the 20 × 100 heuristic run).

# Methods

* **Dynamics:** point-mass orbit propagation by Gauss's form of Lagrange's
  planetary equations (Appendix A, Eqs. 40–46, from Ref. [19]) with thrust,
  secular J2 and drag; Earth's shadow neglected (continuous thrust except
  during the drift); no other perturbations (§3.3).
* **Thruster:** constant power 5.7 W, constant $I_{sp}$ = 2500 s (TPS),
  Eqs. 2–3.
* **Atmosphere:** NRLMSISE-00; $C_D$ = 2.2 (citing Ref. [30]); 10 × 10 ×
  30 cm body; projected area by Eqs. 14–29.
* **Integrator:** RK4, fixed step 100 s, stated sufficient for the accuracy
  requirements (§3.3); no convergence study shown.
* **Optimizer:** Differential Evolution in ESA's PyGMO (Ref. [29]),
  population 20, 100 generations; drift time in [0, 200] d, drift-orbit
  semi-major axis in [6928, 7378] km (altitude kept below 1000 km for
  radiation).
* **Initial orbit (Table 4):** semi-major axis 6878 km, eccentricity
  0.0001 (to avoid the zero-eccentricity singularity of Gauss's equations),
  inclination 28.5°, other angles zero. Accuracy requirements: 1.0 km,
  0.0005, 0.01°, 0.01°.
* **SatA policy:** tangential thrust back to the original altitude whenever
  the semi-major axis falls by more than 1 km.
* **Coverage illustration** (§3, Figs. 3–4): two satellites at 500 km,
  28.5°, 180° apart in RAAN, ground station at MIT, omnidirectional
  antennas, 0° minimum elevation; qualitative only.

# Tests and results

| Case | Conditions | Result |
|---|---|---|
| Sim 1, min time (Fig. 6) | Table 4, TPS | final errors 0.023 km, 2.3 × 10⁻⁵, 0 in $a$, $e$, $i$; RAAN 180.09°; 164.2 d; 0.085 kg |
| Sim 2, min propellant (Fig. 7) | same | 0.022 km, 3.5 × 10⁻⁵, 0; 179.91°; 245.1 d; 0.044 kg |
| Sim 3, hybrid (Figs. 8–9, 11–12) | out-of-plane law in the drift orbit | 0.010 km, 4.8 × 10⁻⁵, 7.4 × 10⁻⁵ deg; 179.91°; 160.6 d; 0.158 kg |
| SatA drag compensation (Fig. 10) | Sim 2 duration | −1 km in ≈81 d; 3 reboosts; 0.27 g |
| Appendix B (Figs. 11–12) | Sim 3, SatB | eccentricity ≈0.8–1.5 × 10⁻⁴; inclination within ≈±0.0005° about 28.4990° |

# Notation map

The orbital and attitude symbols have no registry counterpart and collide
with several registry symbols; they are kept in words.

| Gomez Jenkins et al. (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $T$, $T_{Max}$ (thrust) | $F$ | **collision:** registry $T_s$ is a temperature |
| $I_{sp}$ | $I_{sp}$ | |
| $g$ | $g_0$ | standard gravity; **collision:** registry $g$ is a relative collision speed |
| $P$ | $P$ | electric power to the thrusters, 5.7 W |
| $\eta$ | $\eta$ | undefined in the paper; Eqs. 2–3 are consistent with $\eta=F^2/(2\dot mP)$; the propellant masses imply the 60% "thruster efficiency" of Table 1 |
| $dm/dt$ | $-\dot m$ | |
| $m$, $m_p$/$M_p$ | words (spacecraft mass, propellant mass) | **collision** with species mass $m_s$ |
| $a_T$, $a_D$ | words (thrust and drag accelerations) | $a_D$ also denotes the drift-orbit semi-major axis (Eq. 35): paper-internal collision |
| $a,e,i,\Omega,\omega,M,\nu,E,u,p,r,n$ | words (orbital elements, anomalies, semi-latus rectum, radius, mean motion) | **collisions:** $e$ elementary charge, $\Omega_e$ Hall parameter, $\nu_{sk}$ collision frequency, $\mathbf E$ field, $p_s$ pressure, $r$ radial coordinate, $n_s$ density, $\omega$ angular frequency |
| $\mu$ | words (gravitational parameter) | **collision** with mobilities $\mu_\perp$, $\mu_\parallel$ |
| $J_2$, $R_E$ | words | |
| $\alpha$, $\beta$, $\gamma$ | words (pitch, yaw, flight-path angle) | **collisions:** $\gamma$ polytropic index; $\alpha_{\mathrm B}$, $\alpha_E$ |
| $S$, $S_1$–$S_3$ | words (projected area) | **collision** with shape function $S(\mathbf x)$ and Sobol' indices $S_j$ |
| $\rho$, $V$ | words (atmospheric density, orbital speed) | |
| $C_D$ | $C_D$ | drag coefficient referred to the cross-section and $\tfrac12\rho V^2$ |
| $W_{t_f}$, $W_{\Delta\Omega}$, $W_{m_p}$ | words (cost weights) | **collision** with macroparticle weight $W$ |
| $T_D$, $T_\Omega$ | words (drift and thrusting times) | |

# Pages created or updated

No concept page cites this source yet. It was ingested in full (bundle law, chunk 3), but none of its contributions earns a concept page under the granularity rule: electrospray propulsion appears only as attributed background (a device description and a performance table), and the paper's own contribution is orbit mechanics and trajectory optimization.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Gomez_CubeSat_constellation_management_using_Ionic_Liquid_Electros.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier, © 2018 IAA), 10
     pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.007, printed on page 1
     and checked on Crossref: title, authors (family name "Gomez Jenkins"),
     Acta Astronaut. 151:243–252 match; issue October 2018 (no
     published-online field on Crossref); page 1 gives received 6 Sep 2017,
     revised 8 May 2018, accepted 3 Jun 2018, online 6 Jun 2018. Page 1
     matches the filename title. The filename's "Gomez" is the first half
     of the two-part surname; the slug is `gomezjenkins-2018`.
   * **How it was read.** Full text layer; equations and Figs. 8–12 checked
     on rendered pages 246, 250, 251 and 252. Figs. 1–4 and 6–7 were not
     inspected visually; their numbers are restated in the text and
     Table 5.
   * **Recorded as printed.**
     * Eq. 38 and Table 3 print the hybrid yaw law as switching with the
       sign of the cosine of the argument of latitude, which by the paper's
       own Eqs. 42–43 maximizes the inclination rate, not the RAAN rate.
       The text places the switch at the nodes, where the sine changes
       sign, and Fig. 12 and Table 5 (inclination error 7.4 × 10⁻⁵ deg)
       show no secular inclination drift. Reader's check: a cosine law at
       this acceleration would change the inclination by about 2° over
       75 days, so the implemented law was the sine law.
     * $\eta$ in Eqs. 2–3 is not defined. Reader's check: Eq. 3 integrated
       over the thrusting time with 5.7 W and 2500 s gives 84.8, 44.3 and
       157.9 g with $\eta$ = 0.60 (Table 5: 85, 44, 158 g) and 70.6, 37.0,
       131.6 g with $\eta$ = 0.50. The simulations used the TPS thruster
       efficiency (60%), not the total efficiency (50%); if the total
       efficiency is the one that applies to 5.7 W of bus power, the
       propellant masses are about 17% low and the thrust about 20% high
       (not discussed in the paper).
     * The eccentricity tolerance is 0.0001 in the §3.3 text and 0.0005 in
       Table 4 (all results satisfy both).
     * Table 4 labels the 10 × 10 × 30 body dimensions "(m3)"; the 3U body
       is in centimetres.
     * §3 places the MIT ground station at longitude 228.91°; MIT is at
       about 288.91° E (probable typo; affects only the Fig. 3
       illustration).
     * Eq. 41 writes lowercase thrust-component subscripts where the rest
       of the paper uses capitals.
     * $a_D$ is both the drag acceleration (Eq. 8) and the drift-orbit
       semi-major axis (Eq. 35, Table 5).
     * §3.4 calls the Table 5 results the "optimal trajectory", §4
       "sub-optimal"; Sim 2's drift time sits on the 200-day search bound,
       so its minimum-propellant result is bound-constrained.
     * The abstract gives 161 days for Sim 3 (Table 5: 160.6 d; rounding).
     * Reader's check: the secular J2 nodal rates (6.724°/day at 6878 km,
       5.260°/day at 7377.96 km, 5.923°/day at 7131.91 km) reproduce the
       printed drift-rate differences 1.46 and 0.8°/day; the SatA reboost
       Δv (about 0.553 m/s per km) reproduces 0.27 g; the thruster's peak
       RAAN rate at 7378 km (about 0.098°/day) is consistent with the
       printed 0.1°/day.
   * **Reference list.** 30 printed entries ([1]–[30]), matching the
     Crossref reference count; no DOIs printed. Ref. [3] prints two years
     ("Acta Astronaut. 62 (2008) (2007) 97–111"); ref. [22] is printed as
     the "23nd International Electric Propulsion Conference, 2011" (the
     2011 IEPC was the 32nd; not verified). The self-citation [16] prints
     the author as "Gomez-Jenkins".
