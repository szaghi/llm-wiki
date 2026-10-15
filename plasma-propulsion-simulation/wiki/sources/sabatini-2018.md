---
type: Source
title: "Sabatini et al. (2018) — Effects of a High Fidelity Filter on the attitude stabilization of a flexible spacecraft"
description: "Shows on an air-bearing testbed with flexible PZT-instrumented panels that a 0.11 s GNC loop delay destabilizes PD attitude control, and that both Finite Spectrum Assignment and a low-process-noise Kalman filter (the High Fidelity Filter) restore stability, the latter with better accuracy and 16% thruster duty against 39% and 79%."
resource: "doi:10.1016/j.actaastro.2018.06.016"
source_kind: paper
authors: [Sabatini M., Palmerini G.B., Ribet M., Gasbarri P., Lampani L.]
year: 2018
venue: "Acta Astronaut. 151:260–269"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Sabatini_Effects_of_a_High_Fidelity_Filter_on_the_attitude_stabilizat.pdf"
tags: [context, attitude-control, flexible-spacecraft, time-delay, kalman-filter, piezoelectric-sensing]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The testbed is a planar air-bearing free-floating platform (PINOCCHIO,
10 kg bus) with two flexible fibreglass panels and on-off cold-gas
thrusters. Its GNC loop has a measured mean sensor-to-actuator delay of
about 0.11 s, which destabilizes a PD attitude controller whose
discrete-time delay margin is only 0.098 s. The composite panels carry
embedded PZT patches; a camera with Hough-transform tracking calibrates
the PZT electromechanical parameters so that the PZTs alone can then
measure elastic displacement. Two stabilization techniques are compared:
Finite Spectrum Assignment (FSA), which predicts the state one delay
ahead, and the authors' "High Fidelity Filter" (HFF), a linear Kalman
filter with a very low process-noise covariance, which changes the
open-loop transfer function and raises the delay margin. The paper
supports this with a delay-margin map over two process-noise entries
and with ADAMS/SIMULINK co-simulation. In experiments both techniques
stabilize a 30° slew; HFF gives better final attitude accuracy,
near-zero residual vibration and the lowest thruster duty, 16% of the
time against 39% for FSA and 79% for plain PD.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Loop delay** (§4, Fig. 10). The GNC loop delay is time-varying with
   a mean of about 0.11 s; individual delays read off Fig. 10 are 0.095,
   0.149, 0.126 and 0.106 s. Shown (experiment).
2. **Delay margin** (§7, Fig. 12). With $k_P=0.1$, $k_D=0.3801$ (Eq. 6),
   the continuous open loop has a delay margin of 0.133 s; the discrete
   loop with 0.07 s sampling has only 0.098 s, below the 0.11 s delay, so
   the loop is unstable; co-simulation confirms it (Fig. 13). Shown
   (analysis and simulation).
3. **Smith predictor and FSA** (§8.1, Eqs. 8–11). The Smith predictor
   does not suit unstable or lightly damped processes because the
   compensated closed loop keeps the process poles (attributed). FSA
   stabilizes the delayed system provided $A+BK_{PD}$ is Hurwitz;
   asserted ("It can be demonstrated"), not proved.
4. **High Fidelity Filter** (§8.2, Eqs. 17–20, Figs. 15–18). The
   stationary Kalman filter changes the loop transfer function. With
   process-noise covariance $\mathrm{diag}(0,0,10^{-6},10^{-6})$ the closed
   loop is unstable in co-simulation, with
   $\mathrm{diag}(0,0,10^{-9},10^{-9})$ it is stable; lower process noise
   gives larger phase and delay margins (Figs. 16–17), and a 2-D scan finds
   a region of the two entries with enough margin for 0.11 s (Fig. 18). The
   experiments use an intermediate value whose number is not printed.
   Shown (numerical).
5. **Experiment** (§9, Figs. 19–21). In the 30° slew plain PD is
   unstable; FSA is stable but leaves a non-negligible steady-state
   attitude error, attributed "probably" to model mismatch and a
   non-constant delay; HFF is stable, more precise and reduces the
   panel-tip oscillation "nearly to zero". Thrusters are on 79% (PD), 39%
   (FSA) and 16% (HFF) of the time. Shown.
6. **PZT calibration** (§3, Fig. 7). After a best fit against camera
   tip-displacement measurements, the PZT-derived tip displacement
   "approximatively coincide[s]" with the camera's; no error number.
7. **Camera tracking** (§3). Corner, Hough and BLOB detectors perform
   similarly; corner detection is slightly less robust to noise and BLOB
   filtering can miss small displacements, so Hough is chosen. The
   camera's maximum stable rate, 25 Hz, resolves the first two modes (up
   to 6.34 Hz) below the Nyquist frequency. Stated.

# Methods

* **Panels** (§2): two plates 540 × 150 × 1.6 mm; Hexcel prepreg, M34
  epoxy at 41% by volume, 300 g/m² woven glass fabric; six ±45° plies,
  triangular cut-outs, tip dummy masses. Table 1: density 1880 kg/m³,
  longitudinal and transverse moduli 21 GPa, shear modulus 4 GPa, Poisson
  ratio 0.2. FE eigenfrequencies (Table 2): 1.32 Hz (flexural), 6.34 Hz
  (flexural), 9.88 Hz (torsional). One plate carries three embedded
  PIC255 PZT patches, 10 × 10 × 0.2 mm, read through a charge amplifier.
* **PZT calibration** (§3, Fig. 6): beam model (cut-outs smeared, PZTs
  not affecting dynamics or thickness); best fit of the PZT parameters,
  chiefly the electromechanical coupling factor, against the camera tip
  displacement, with the root clamped.
* **Platform** (§4): PINOCCHIO, 10 kg bus on an air-bearing pad at 3 bar;
  eight cold-gas nozzles on on-off electrovalves at 5 bar, maximum torque
  about 0.017 N m; PWM-modulated control; delay measured with an
  oscilloscope between PZT output and valve input (Fig. 9).
* **Simplified model** (§5, Eqs. 1–4): rigid bus with two identical
  appendages as flexural beams, first mode only, linearized:
  $$\begin{aligned} J\ddot\theta+(2\gamma_1+D\gamma_0)\ddot A&=\tau,\\ \gamma_2\ddot A+\bigl(\gamma_1+\tfrac{D}{2}\gamma_0\bigr)\ddot\theta+\omega^2A+c\dot A&=0,\end{aligned}$$
  with participation factors $\gamma_0$, $\gamma_1$ and mass-normalized
  $\gamma_2=1$; $J=0.3615$ kg m², $\gamma_0=-0.58909\sqrt{\mathrm{kg}}$,
  $\gamma_1=-0.2775\sqrt{\mathrm{kg}}\,\mathrm m$, $\omega=5.7343$ rad/s,
  $c=0.02294$ (units not printed). Plant transfer function (Eq. 4):
  $P(s)=\dfrac{9.025s^2+0.207s+296.8}{s^4+0.07483s^3+107.3s^2}$.
* **Refined model** (§6, Fig. 11): MSC ADAMS multibody model with panel
  FEM from MSC NASTRAN and lock joints, co-simulated with
  MATLAB/SIMULINK (sensors, filter, PD, PWM, delay).
* **Control** (§7, Eqs. 5–7): $\tau=-k_P(\theta-\theta_{ref})-k_D\dot\theta$,
  tuned to reach the reference in under 15 s without overshoot;
  $C(s)=(0.3801s+0.1)/(0.001s+1)$; sampling time 0.07 s.
* **FSA** (§8.1, Eqs. 8–11): for $\dot{\mathbf X}(t)=A X(t)+\bar B\tau(t-\delta t)$,
  the prediction
  $\hat{\mathbf X}(t+\delta t)=e^{\mathbf A\delta t}\hat{\mathbf X}(t)+\int_0^{\delta t}e^{\mathbf A\upsilon}\bar{\mathbf B}\tau(t-\upsilon)\,d\upsilon$
  feeds $\tau(t)=\mathbf K_{PD}\hat{\mathbf X}(t+\delta t)$ (called "Delay
  Compensation" in the authors' earlier work).
* **HFF** (§8.2, Eqs. 12–20): continuous linear Kalman filter with
  measurements from the three PZTs and a gyro, gain from the stationary
  Riccati solution; the measurement-noise covariance is fixed by the
  sensors and only the two dynamic diagonal entries of the process-noise
  covariance are varied (kinematic entries and cross-correlations zero);
  the delay margin is evaluated on the discrete open loop including the
  filter transfer function.

# Tests and results

| Test | Section, figure | Conditions | Result |
|---|---|---|---|
| T1 | §3, Fig. 7 | root-clamped plate, camera against PZT tip displacement | mismatch before calibration, "approximatively coincide" after; no error metric |
| T2 | §4, Fig. 10 | oscilloscope, PZT signal to 12 V valve | delay time-varying, mean ≈ 0.11 s |
| T3 | §7, Fig. 12 | Bode of the open loop | delay margin 0.133 s continuous, 0.098 s discrete (0.07 s sampling) |
| T4 | §7, Fig. 13 | co-simulation with and without delay | unstable tip displacement with delay |
| T5 | §8.1, Fig. 14 | co-simulation, FSA against ideal no-delay | stabilized, reference reached, performance below ideal |
| T6 | §8.2, Fig. 15 | co-simulation, process noise $10^{-6}$ against $10^{-9}$ | large unstable oscillation at $10^{-6}$, stable at $10^{-9}$; filter transfer functions in Eqs. 18 and 20 |
| T7 | §8.2, Figs. 16–18 | margins against process noise (1-D, then 2-D map) | lower process noise, larger delay margin; stable region identified |
| T8 | §9, Figs. 19–21 | experiment, 30° slew, PD, PD+FSA, PD+HFF | PD unstable (79% thruster duty); FSA stable with steady-state error (39%); HFF stable, best accuracy, tip oscillation near zero (16%) |

# Notation map

The paper is outside the bundle's domain; its symbols are kept in words.

| Sabatini et al. (2018) | Registry | Note |
|---|---|---|
| $\theta$ | words (attitude angle) | **collision:** registry $\theta$ is the azimuthal coordinate |
| $A$; $\mathbf A$ | words (first modal amplitude; state matrix) | two meanings inside the paper |
| $\omega$ | $\omega$ | first-mode angular frequency of the panel |
| $c$ | words (first-mode damping coefficient) | **collision:** registry $c$ is the speed of light |
| $\tau$, $J$ | words (control torque, global moment of inertia) | |
| $\gamma_0$, $\gamma_1$, $\gamma_2$ | words (modal participation factors) | **collision:** registry $\gamma$ is the polytropic index |
| $\mu$ | words (panel mass per unit length) | **collision** with the mobilities $\mu_\perp$, $\mu_\parallel$ |
| $\varphi$, $\xi$ | words (first mode shape, panel axial coordinate) | not $\phi$ |
| $L$, $D$ | $L$ (panel length); $D$ in words (half bus base) | |
| $Q$, $R$, $P$ | words (process-noise, measurement-noise and error covariances) | **collision:** registry $P$ is electric power |
| $\mathbf H$ | words (measurement matrix) | **collision:** registry $H$ is spectral entropy |
| $\mathbf K_F$, $\mathbf K_{PD}$, $k_P$, $k_D$ | words (gains) | **collision:** registry $k$ is a wavenumber |
| $\mathbf M$, $\mathbf K$, $\mathbf B$ | words (mass, stiffness, input matrices) | **collision:** registry $\mathbf B$ is the magnetic field |
| $\delta t$ | words (GNC loop delay) | not the time step $\Delta t$ |
| $\mathbf z$ | words (measurement vector) | **collision:** registry $z$ is the axial coordinate |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Sabatini_Effects_of_a_High_Fidelity_Filter_on_the_attitude_stabilizat.pdf`.
   * **Version.** Publisher's final typeset PDF (version of record), 10
     pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.016, printed on page 1
     and checked on Crossref: title, the five authors, Acta Astronaut.
     151:260–269 match; published in print October 2018 (no
     published-online field on Crossref). Page 1 gives received 24 Jan
     2018, revised 11 May 2018, accepted 5 Jun 2018, online 15 Jun 2018.
     Page 1 matches the filename title.
   * **How it was read.** Full text layer; all equations read from the
     rendered pages 5–7, including the definition of $J$. Figs. 7, 13–21
     are graphical; no attitude errors or tip amplitudes are given in the
     text beyond the duty percentages. The experimental process-noise value
     and the measurement-noise covariance are not printed.
   * **Recorded as printed.**
     * Eq. 13: with $\mathbf z=[A_{PZT1}\ A_{PZT2}\ A_{PZT3}\ \dot\theta]^T$
       and $\mathbf X=[\theta\ \dot\theta\ A\ \dot A]^T$ the PZT rows should
       be $[0\ 0\ 1\ 0]$ and the gyro row $[0\ 1\ 0\ 0]$; the printed
       $\mathbf H$ has three rows $[0\ 1\ 0\ 0]$ and a last row
       $[0\ 0\ 1\ 0]$ (checked on the rendered page). Either $\mathbf H$ or
       the order of $\mathbf z$ is wrong as printed.
     * Eq. 16 writes the closed-filter matrix as
       $\mathbf A-\mathbf K_{PD}-\mathbf K_F\mathbf H$; substituting
       $\tau=\mathbf K_{PD}\hat{\mathbf X}$ into Eq. 12 gives
       $\mathbf A+\bar{\mathbf B}\mathbf K_{PD}-\mathbf K_F\mathbf H$, as
       §8.1's "$A+B\mathbf K_{PD}$ is Hurwitz" implies.
     * Eq. 10 prints an unbalanced large parenthesis in the integrand.
     * The abstract says "Finite Spectrum Analysis"; the body says
       "Finite Spectrum Assignment".
     * §7 says the reference attitude "is set equal to 30 s"; 30° is meant
       (§9).
     * Table 2 gives the first mode at 1.32 Hz (about 8.29 rad/s), while
       the model uses $\omega=5.7343$ rad/s (about 0.913 Hz) as the "first
       modal pulsation", not reconciled in the paper. Reader's check: the
       plant denominator's $107.3s^2$ implies a free-floating coupled pole
       at about 10.36 rad/s, consistent with the given $J$, $\gamma_i$ and
       $\omega$, and $c\cdot107.3/\omega^2=0.0749$ matches the printed
       0.07483, so the transfer function is internally consistent.
     * The units of $c$ are not given (1/s for a mass-normalized
       equation); the 16% thruster duty is stated without the manoeuvre
       duration over which it is computed.
   * **Reference list.** 32 printed entries ([1]–[32]), matching the
     Crossref reference count.
