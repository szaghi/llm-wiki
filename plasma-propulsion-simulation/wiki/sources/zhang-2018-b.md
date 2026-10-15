---
type: Source
title: "Zhang et al. (2018) — An anti-saturation steering law for Three Dimensional Magnetically Suspended Wheel cluster with angle constraint"
description: "Proposes a weighted pseudo-inverse steering law for a cluster of three-dimensional magnetically suspended wheels whose shaft-deflection weights fall toward zero as the 3° tilt limit is approached, shifting torque to wheel-speed (flywheel) mode; one 10° roll manoeuvre simulation shows it staying within the limit where the plain pseudo inverse oscillates and saturates."
resource: "doi:10.1016/j.actaastro.2018.06.039"
source_kind: paper
authors: [Zhang R., Yu Y., Han C., Yang Z.]
year: 2018
venue: "Acta Astronaut. 151:467–474"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Zhang_An_anti-saturation_steering_law_for_Three_Dimensional_Magnet.pdf"
tags: [context, attitude-control, magnetically-suspended-wheel, steering-law, momentum-exchange-actuator]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper proposes a steering law for a cluster of three-dimensional
magnetically suspended wheels (3-DMSW). A 3-DMSW is a momentum wheel on
active magnetic bearings: it gives two-axis radial torque by tilting the
rotor shaft (the paper's "CMG mode") and axial torque by changing the
rotor speed ("FW mode"). The shaft tilt saturates at a small angle (3°
in the simulations). The law is a weighted pseudo inverse,
$B^\#=WB^T(BWB^T)^{-1}$; each shaft-deflection weight is an exponential
of the reciprocal unsaturation degree, with a sign set by whether the
shaft moves toward or away from saturation. A simulated 10° roll
manoeuvre compares three cases: the proposed law tracks the commanded
torque and stays within the 3° limit; the plain pseudo inverse
oscillates and hits the angle limit; a flywheel-only cluster is slower
and spans a wider wheel-speed range. The magnetic bearings are actuator
hardware; the paper has no plasma or propulsion content.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Cluster model** (Eqs. 1–5): cluster angular momentum
   $h_g=\sum_iA_iI\hat h_{gi}$ with
   $\hat h_{gi}=\Omega_i[\sin\beta_i,\,-\sin\alpha_i\cos\beta_i,\,\cos\alpha_i\cos\beta_i]^T$;
   output torque $T_o=-\dot h_g=BR$, with the actuator command
   $R_i=[\dot\alpha_i,\,\dot\beta_i,\,\dot\Omega_i]^T$ and $B_i$ from
   Eq. 4. The reader re-derived Eq. 4 from Eqs. 2–3: consistent.
2. **Plain pseudo inverse unsuitable** (§3, Eqs. 6–7, stated):
   $R=B^+T_c$, $B^+=B^T(BB^T)^{-1}$ does not suit a 3-DMSW cluster,
   because the CMG-mode columns of $B$ carry the factor $\Omega_i$ and
   are orders of magnitude larger than the FW-mode columns. Supported
   only by the Case 2 simulation.
3. **Anti-saturation weighted pseudo inverse** (Eqs. 8–13):
   $R=B^\#T_c$, $B^\#=WB^T(BWB^T)^{-1}$,
   $W=\mathrm{diag}(W_{\alpha1},W_{\beta1},W_{\Omega1},\ldots)$,
   $$W_{\alpha i}=W_0\exp\!\left(-\frac{\omega_{\alpha i}}{|\omega_{\alpha i}|}\,\frac{\alpha_i}{|\alpha_i|}\,\frac{1}{\varepsilon K_{\alpha i}}\right),$$
   likewise for $\beta$ (Eq. 11), with the unsaturation degree
   $K_{\alpha i}=\big||\alpha_i|-\alpha_{\max}\big|$ (Eq. 12),
   $W_{\Omega i}=1$ (Eq. 13), $W_0=1$ and a tuning parameter
   $\varepsilon$.
4. **Three regimes** (§3, Fig. 5, stated from the shape of
   $e^{\pm1/x}$): far from saturation the weight is close to 1 (CMG
   mode); near saturation and moving toward it the weight tends to 0, so
   FW mode takes over; near saturation and moving away it grows without
   bound. The abstract calls the method "demonstrated theoretically";
   the demonstration is this qualitative argument, with no proof of
   stability or of constraint satisfaction.
5. **Simulation** (§4, Figs. 7–13, shown by simulation only): with the
   proposed law the roll angle reaches 10° quickly and the deflection
   angles stay within 3°; with the plain pseudo inverse (Case 2) all
   three axes oscillate and the angles saturate at 3°; the
   flywheel-only cluster (Case 3) is slower and uses a wider rotor-speed
   range.

# Methods

* Model: rigid spacecraft with three 3-DMSWs mounted orthogonally, spin
  axes along roll, pitch and yaw (Fig. 6). Assumptions (§2): maximum
  deflection torque above the rotary torque; at least three units; only
  the rotor polar inertia kept. Rotation sequence: about $x_f$ by
  $\alpha$, then about $y_f$ by $\beta$.
* Control: PD attitude controller, $K_p=0.3$, $K_d=0.8$ (§4), closed
  loop as in Fig. 4. The attitude kinematics and dynamics are not
  printed.
* Steering: Case 1, Eqs. 8–13; Case 2, Eqs. 6–7; Case 3, flywheels only
  with the pseudo inverse.
* Parameters (Table 1): rotor polar inertia $I=0.0277$ kg·m²; satellite
  inertia $J$ with rows $(8.83,\,0.68,\,-0.16)$,
  $(0.68,\,7.70,\,-0.10)$, $(-0.16,\,-0.10,\,13.0)$ kg·m²; initial rotor
  speed 2500 rpm, maximum 5000 rpm, maximum rotor acceleration
  2.166 rad/s²; initial deflections 0°, limits $\alpha_{\max}=\beta_{\max}=3°$;
  orbit rate 0.0011 rad/s.
* Not reported: the value of $\varepsilon$, the integrator, the time
  step and the simulation software.

# Tests and results

* One scenario (§4): a 10° rotation about the roll axis, finished after
  about 50 s.
* Attitude (Fig. 7): Case 1 reaches the roll target rapidly with a slight
  pitch and yaw fluctuation that returns to zero; Case 2 oscillates
  strongly in all three angles and does not settle; Case 3 takes "a much
  longer time". No settling times or errors are given.
* Torque (Figs. 8–10): Case 1 tracks well early; later the output drops
  because the FW-mode limit (the 2.166 rad/s² acceleration bound) is
  reached. Case 2: strong oscillation of command and output. Case 3: the
  torque limit always binds.
* Deflections and rotor speeds (Figs. 11–13): Case 1 angles stay within
  3° and the cluster works in FW mode in the middle and late stages;
  after 50 s angles and speeds drift slowly with the orbit rate. Case 2
  angles are clipped at 3° and the rotor speeds barely change, so torque
  is not routed to FW mode. Case 3 wheel speeds vary over a much wider
  range, loading the desaturation.
* All results are plots; no tabulated metric.

# Notation map

The paper is attitude control; none of its quantities has a registry
counterpart.

| Zhang et al. (2018) | Registry | Note |
|---|---|---|
| $\alpha_i$, $\beta_i$ | words (shaft deflection angles) | not $\alpha_{\mathrm B}$, $\alpha_E$, $\alpha_\tau$, $\alpha_n$ |
| $\Omega_i$ | words (rotor spin rate) | **collision** with the Hall parameter $\Omega_e$ |
| $\omega_{\alpha i}$, $\omega_{\beta i}$ | words (deflection angular rates) | **collision** with the mode angular frequency $\omega$ |
| $I$ | words (rotor polar inertia) | not $I_{sp}$, $I_d$, $I_b$ |
| $W$, $W_{\alpha i}$, $W_0$ | words (pseudo-inverse weights) | **collision:** registry $W$ is the macroparticle weight |
| $\varepsilon$ | words (weight tuning parameter) | not $\varepsilon_0$ |
| $B$, $B^+$, $B^\#$ | words (steering matrix and its inverses) | not the magnetic field $\mathbf B$ |
| $K_{\alpha i}$, $K_{\beta i}$ | words (unsaturation degrees) | |
| $A_i$, $R$, $T_c$, $T_o$, $h_g$, $J$, $K_p$, $K_d$ | words | $T_c$, $T_o$ are torques, not temperatures $T_s$ |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Zhang_An_anti-saturation_steering_law_for_Three_Dimensional_Magnet.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier), 8 pages
     (467–474).
   * **Identity.** doi:10.1016/j.actaastro.2018.06.039, printed on page 1
     and checked on Crossref: title, all four authors, Acta Astronaut.
     151:467–474 match; issue October 2018 (published-print 2018-10);
     page 1 gives received 22 Sep 2017, revised 14 Jun 2018, accepted
     17 Jun 2018, online 20 Jun 2018. Page 1 matches the filename title.
   * **How it was read.** Full text layer; Eq. 11 is garbled there and
     was read on rendered page 470 (legible). Figs. 1–13 are diagrams
     and plots; no values were read off them, and the paper prints none.
   * **Recorded as printed.**
     * §4 calls 2.166 rad/s² the FW-mode "maximum torque output
       limitation"; that value is the acceleration bound of Table 1, a
       unit slip.
     * Reader's check: the implied torque limit is
       $I\times2.166\ \mathrm{rad/s^2}=0.0277\times2.166\approx0.060$ N·m
       (not printed).
     * In Eq. 11 the sign factors $\alpha_i/|\alpha_i|$ and
       $\omega_{\alpha i}/|\omega_{\alpha i}|$ are undefined at zero, and
       zero initial deflection is the stated initial condition (Table 1);
       the paper does not say how this is handled.
     * Reader's check: a weight "close to 1" far from saturation needs
       $1/(\varepsilon K)\ll1$; at zero deflection
       $K=\alpha_{\max}=3°\approx0.052$ rad, so $\varepsilon\gg19$. The
       value of $\varepsilon$ is never given, so the claim cannot be
       checked.
     * The text after Eq. 10 writes "$W_{\alpha n}$ and $W_{\beta i}$";
       the index $n$ should be $i$.
     * Eq. 3 takes $T_o=-\dot h_g$ with $A$ constant and omits the
       gyroscopic term of the body-frame derivative; the paper does not
       say whether it is neglected or compensated (the attitude dynamics
       are not printed).
     * "Demonstrated theoretically" (abstract) overstates the qualitative
       Fig. 5 argument.
   * **Reference list.** 32 printed entries ([1]–[32]), matching the
     Crossref reference count. Ref. [22] prints no authors; they come
     from the Crossref record of its printed DOI 10.1007/BF03256544
     (title matches). Ref. [19] prints a malformed DOI
     ("doi:2514/1.A33944") and ref. [25] a CNKI identifier as a DOI; both
     are kept only as notes.
