---
type: Source
title: "Kumar et al. (2018) — Fault-tolerant attitude control of miniature satellites using reaction wheels"
description: "Proposes an adaptive sliding-mode attitude tracking law for a miniature satellite with four reaction wheels that tolerates wheel failure or fading without fault detection and isolation, proves uniform ultimate boundedness by a Lyapunov argument, and demonstrates attitude recovery in hardware-in-the-loop tests of three fault cases."
resource: "doi:10.1016/j.actaastro.2018.05.004"
source_kind: paper
authors: [Kumar K.D., Godard, Abreu N., Sinha M.]
year: 2018
venue: "Acta Astronaut. 151:206–216"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Kumar_Fault-tolerant_attitude_control_of_miniature_satellites_usin.pdf"
tags: [context, attitude-control, fault-tolerant-control, sliding-mode-control, reaction-wheels, hardware-in-the-loop]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

An adaptive fault-tolerant sliding-mode (continuous variable-structure)
attitude tracking law for a rigid miniature satellite actuated by four
reaction wheels, with no explicit fault detection and isolation (FDI).
Wheel faults enter through a diagonal effectiveness matrix $\Gamma$ (0
healthy, 1 failed); the lumped nonlinearity and disturbance term is
handled by a bound that needs no regressor (after Cai et al., the
paper's ref. [17]) with an adaptive gain $\rho$. A Lyapunov argument
(Theorem 5.3, §3.3) shows convergence of the sliding variable to a ball,
that is uniform ultimate boundedness. The torque command is converted to
armature voltage through a brushless-DC wheel model with Coulomb plus
viscous friction, and the law is tested in hardware in the loop on
wheels built at Ryerson University (not space-qualified), in two
configurations: three orthogonal wheels plus one skewed (A1) and a
four-wheel pyramid (A2). In three fault cases the attitude recovers
(Figs. 6–8).

# Key claims

Symbols are the paper's own (see the notation map).

1. **Sliding manifold** (§3.1, Eqs. 25–31, proved, standard). On
   $\sigma=\omega_e+\beta\,\mathrm{sgn}(q_{4e})\,q_e$, $\beta>0$, the
   function $V=[q_{4e}-\mathrm{sgn}(q_{4e})]^2+q_e^Tq_e$ gives
   $\dot V=-\beta q_e^Tq_e$, so $q_e\to0$, $q_{4e}\to\pm1$ and
   $\omega_e\to0$.
2. **Control and adaptive laws** (§3.2, Eqs. 34–36, design).
   $u_r=-\alpha A^T\sigma-(\rho+1)\eta A^T\mathrm{sgn}(\sigma)$ and
   $\dot\rho=-b_1\rho+b_2\eta\|\sigma\|$, under the assumed bound
   $\|\Delta\|<p_0+p_1\|X\|=\eta$.
3. **Theorem 5.3** (Eqs. 38–52, proved, subject to the slips recorded
   below). With $\lambda_{\min}$, $\lambda_{\max}<1$ the extreme
   eigenvalues of $A\Gamma A^T$ and $\zeta=1/(1-\lambda_{\min})$, the
   closed loop converges to $\|\sigma\|\le\varepsilon^0/\eta$ with
   $\varepsilon^0=b_1\zeta^2/(4b_2(1-\lambda_{\max}))$, for either sign
   of $q_{4e}$; "all the states are uniformly ultimately bounded".
4. **Admissible faults** (§3.3, stated, not proved). $\lambda_{\min}<1$
   holds as long as no more than two wheels (pyramid A2) or one wheel
   (A1) lose power completely.
5. **No FDI** (§1, §5, shown in hardware in the loop). Failure instants,
   patterns and magnitudes stay unknown to the controller; the adaptive
   gain redistributes the effort to the healthy wheels.
6. **Fault physics** (Remark 1, stated). Multiplicative wheel faults are
   caused physically by viscous-friction changes (temperature, loss of
   bearing lubricant) and by changes of the motor torque constant $K_t$.
7. **Outcome** (§5, shown qualitatively). In all three cases the
   satellite is stabilised on three axes "with reasonable pointing
   performance" without thrusters or magnetorquers; no numerical
   pointing accuracy, settling time or baseline comparison is reported.

# Methods

- **Dynamics** (§2.2, Eq. 1): rigid body with four wheels,
  $J\dot\omega^B_{BI}=-\omega^B_{BI}\times(J_s\omega^B_{BI}+AJ_w\Omega)+A\tau_{rw}-A\Gamma\tau_{rw}+\tau_e$,
  $A$ the 3×4 wheel projection matrix,
  $\Gamma=\mathrm{diag}(\gamma_1,\dots,\gamma_4)$, $0\le\gamma_i\le1$.
  Unit-quaternion kinematics relative to the orbit frame (Eqs. 2–7),
  circular orbit.
- **Disturbances** (§2.2.2): gravity-gradient torque (Eq. 8) plus the
  Cai et al. disturbance (Eq. 9),
  $(\tfrac12+\|\omega^B_{BL}\|^2)[\sin 0.8t,\ \cos 0.5t,\ \cos 0.3t]^T$,
  units not stated.
- **Wheel model** (§§2.3–2.4): friction $N_c\,\mathrm{sgn}(s)+fs$ with
  $N_c=7.06\times10^{-4}$ N·m and $f=1.21\times10^{-6}$ N·m/rpm, $s$ the
  wheel speed in rpm; brushless DC motor with torque constant $K_t$,
  back-EMF constant $K_b$, inductance neglected; voltage command
  $e_a=K_b\Omega-R_aK_t^{-1}(u_r-\tau_f)$ (Eq. 20).
- **Configurations** (§4): A1 with the fourth wheel at 45° to all axes
  (Eq. 53); A2 a pyramid with all wheels skewed at 45° (unnumbered
  matrix).
- **Hardware in the loop** (§4, Figs. 4–5): each wheel board carries a
  dsPIC30F3010 driving a three-phase brushless DC motor, linked by I²C to
  the main controller. A Simulink model computes body torques,
  distributes them through $A$, converts them to voltages and sends them
  by radio; tachometer speeds come back, are smoothed, differentiated
  and multiplied by the wheel inertia to estimate the applied torque.
  Data are converted from 8-byte to 4-byte floats; the sampling
  frequency is not stated. The equations are integrated with the IMSL
  routine DDASPG (Petzold–Gear BDF).
- **Parameters** (Tables 1–2): $K_b=K_t$ = 0.0082, 0.0080, 0.0071,
  0.0075 for wheels x, y, z, o; $R_a=0.6$ Ω; dead zones ±1.10, ±1.15,
  ±1.20, ±1.15 V; orbit radius 6878 km; 0.1 m cube with inertias 0.0015,
  0.0017, 0.0020 kg·m²; wheel inertia $1\times10^{-5}$ kg·m²; maximum
  armature voltage 5 V. Gains $\alpha=0.1$, $\beta=0.6$, $b_1=0.5$,
  $b_2=2.5$; initial vector part of the quaternion 0.4 per axis, zero
  rate (Eq. 54).

# Tests and results

All runs are hardware in the loop, 100 s long, with faults injected at
15 s (§5). Values are approximate plot readings.

- **Case I (A1)**: the y wheel fails completely. $q_{4e}$ rises from
  about 0.72 to about 1 within about 10 s; rate errors fall from about
  −0.22 °/s to within ±0.05 °/s; wheel torques peak near
  6×10⁻³ N·m; $\rho$ peaks near 1.2 and decays to about 0.07 by 40–50 s
  (Fig. 6).
- **Case II (A1)**: the y and z wheels supply 40% and 60% of their
  actuation power. Attitude and rate histories are qualitatively
  identical to Case I; $\rho$ peaks near 1.3 (Fig. 7).
- **Case III (A2)**: wheels 3 and 4 fail completely. The attitude
  recovers similarly; rate errors within about ±0.03–0.05 °/s; torques
  peak near 5.5×10⁻³ N·m; $\rho$ peaks near 1.3 (Fig. 8).
- At plot resolution no effect of the 15 s fault is visible in the error
  histories.

# Notation map

The paper's symbols are those of attitude control; none is a
plasma-propulsion quantity.

| Kumar et al. (2018) | Registry | Note |
|---|---|---|
| $\omega^B_{BI}$, $\omega^B_{BL}$, $\omega_e$, $\omega_0$ | words (spacecraft angular velocities, orbital rate) | **collision:** registry $\omega$ is a mode angular frequency |
| $\Omega$ | words (wheel-speed vector) | **collision:** registry $\Omega_e$ is the Hall parameter |
| $\Gamma$, $\gamma_i$ | words (wheel effectiveness) | **collision:** registry $\gamma$ is the polytropic index |
| $\sigma$ | words (sliding variable) | **collision** with $\sigma_{sk}$ |
| $\rho$ | words (adaptive gain) | **collision** with $\rho_c$ |
| $\eta$, $p_0$, $p_1$ | words (uncertainty bound) | **collision:** registry $\eta$ is thrust efficiency |
| $\zeta$, $\lambda_{\min}$, $\lambda_{\max}$, $\varepsilon^0$ | words (fault margin, eigenvalues of $A\Gamma A^T$, ultimate bound) | **collision** with $\lambda_D$, $\lambda_w$ |
| $q_e$, $q_{4e}$, $q_v$ | words (quaternion error and parts) | **collision** with species charge $q_s$ |
| $e_a$, $e_b$ | words (armature and back-EMF voltages) | **collision:** registry $e$ is the elementary charge |
| $s$ | words (wheel speed, rpm) | **collision:** registry $s$ is the species index |
| $L$ | words (orbit frame label) | **collision:** registry $L$ is a length |
| $A$, $J$, $J_s$, $J_w$, $K_t$, $K_b$, $R_a$, $N_c$, $f$, $\tau$, $u_r$ | words | $K_b$ unrelated to $k_B$ |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Kumar_Fault-tolerant_attitude_control_of_miniature_satellites_usin.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier, © 2018 IAA),
     11 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.05.004, printed on page 1
     and checked on Crossref: title, authors (the second author deposited
     under the single name Godard), Acta Astronaut. 151:206–216 match;
     issued 2018-10, no published-online field. Page 1: received 1 May
     2018, accepted 2 May 2018, online 5 Jun 2018. Page 1 matches the
     filename title.
   * **How it was read.** Full text layer; all equations (1)–(54) checked
     on rendered pages 208, 210, 212–215 (Eq. 9 at 200 dpi). Figs. 2–4 are
     schematics; the supplementary data were not accessed.
   * **Recorded as printed.**
     * The third case is printed "Case II" (p. 216) and §5 lists "cases I,
       II, and II"; the Fig. 8 caption says Case III.
     * §5 sets "$p_1=1$, and $p_2=2$", but the bound (Eq. 34) uses $p_0$
       and $p_1$; no $p_2$ exists in the model.
     * §5 says the A2 matrix is "given by Eqs. (53) and (54)"; the pyramid
       matrix is unnumbered and Eq. 54 is the initial condition.
     * "Theorem 5.3" sits in §3.3; §3.3 cites a nonexistent "Eq. (3.3)";
       the introduction refers to Sections II–VI, while the sections are
       numbered 1–6.
     * Reader's check: Eq. 37, obtained by substituting Eq. 35 into
       Eq. 32, requires $AA^T=I$. Neither printed $A$ satisfies it: for
       Eq. 53 $AA^T=I+vv^T$ with $v$ the skewed column, for the pyramid at
       45° $AA^T=\mathrm{diag}(1,1,2)$. The proof inherits the assumption
       silently.
     * Eq. 33 adds the 3×3 matrix
       $\tfrac{\beta}{2}\mathrm{sgn}(q_{4e})(q_{4e}I+[q_e^\times])$ to torque
       vectors; the factor $\omega_e$ that differentiation via Eq. 12 would
       produce is missing.
     * The abstract and conclusion speak of "asymptotic stabilization",
       while Theorem 5.3 proves only convergence to a ball (uniform
       ultimate boundedness).
     * §1 announces complete failure of one wheel and fading of two
       wheels in both configurations, the abstract one wheel (A1) and two
       wheels (A2); the cases run are A1 one-wheel failure, A1 two-wheel
       fading and A2 two-wheel failure.
     * Case II's "40% and 60% of the actuation power" is not translated
       into $\gamma_i$ values.
     * §5 integrates with IMSL DDASPG while §§1 and 4 describe a
       MATLAB/Simulink loop; how they combine is not stated.
     * The attitude and rate panels of Figs. 6 and 7 are visually
       near-identical despite different fault cases; whether this is a
       result or a figure duplication cannot be told from the PDF.
     * Table 1 lists dead zones of ±1.10–1.20 V (of 5 V) and §1 stresses
       dead-zone losses, but neither the law nor Eq. 20 compensates for
       them.
   * **Reference list.** 28 printed entries ([1]–[28]), matching the
     Crossref reference count.
