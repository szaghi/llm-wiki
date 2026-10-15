---
type: Source
title: "Meng et al. (2018) — Vibration suppression control of free-floating space robots with flexible appendages for autonomous target capturing"
description: "Derives generalized rigid and flexible Jacobians for a free-floating space robot with flexible appendages and an energy-based adaptive joint controller (EBVC) with a Lyapunov dissipation argument, and shows in planar and 7-DOF simulations and a single-DOF air-bearing experiment that it reduces appendage vibration during target capture relative to PD control."
resource: "doi:10.1016/j.actaastro.2018.07.044"
source_kind: paper
authors: [Meng D., Lu W., Xu W., She Y., Wang X., Liang B., Yuan B.]
year: 2018
venue: "Acta Astronaut. 151:904–918"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Meng_Vibration_suppression_control_of_free-floating_space_robots.pdf"
tags: [context, space-robotics, vibration-control, flexible-appendages, target-capture]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper treats the pre-impact phase of autonomous capture of a
stationary or moving target by a free-floating space robot (uncontrolled
base) carrying flexible appendages such as solar wings. The rigid–flexible
coupled dynamics are written with assumed modes (modal matrix from FEM),
and momentum conservation gives a "Generalized Rigid Jacobian" (the
classical generalized Jacobian matrix) and a "Generalized Flexible
Jacobian" mapping joint rates and modal rates to the end-effector
velocity. A closed-loop capture scheme (relative pose measurement,
PD-form end-effector velocity planning, damped-least-squares joint-rate
inversion, joint control) is built around an energy-based adaptive joint
controller (EBVC), adapted from Trevisani & Valcher to time-varying joint
references, with a Lyapunov argument giving a non-increasing energy
function. Simulations of a 3-DOF planar robot with two flexible paddles
(stationary and moving target) and of a 7-DOF 3D robot with one flexible
wing compare EBVC with plain PD control, and a single-DOF air-bearing
experiment with a thin aluminium plate and a piezoelectric sensor
compares vibration decay. EBVC lowers peak and residual appendage
deflection substantially, while the base pose drift is nearly the same
for both controllers.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Generalized Jacobians** (§2.2, Eqs. 9–13). With zero initial
   momentum and no external loads,
   $\dot x_b=-H_{bb}^{-1}H_{b\theta}\dot\Theta-H_{bb}^{-1}H_{b\xi}\dot\xi$
   and $\dot x_e=J_g\dot\Theta+J_\xi\dot\xi$, with
   $J_g=J_m-J_bH_{bb}^{-1}H_{b\theta}\in\mathbb R^{6\times n}$ and
   $J_\xi=-J_bH_{bb}^{-1}H_{b\xi}\in\mathbb R^{6\times s}$. Derived.
2. **Joint-rate inversion** (§3.3.2, Eqs. 19–22). The desired joint rates
   come from damped least squares,
   $J_g^{\#}=(J_g^TJ_g+\lambda^2I)^{-1}J_g^T$, with adaptive
   $\lambda^2=0$ if $\hat\sigma_n\ge\varepsilon$, else
   $(1-(\hat\sigma_n/\varepsilon)^2)\lambda_m^2$. A vibration-compensated
   end-effector velocity $\hat{\dot x}_{ed}=\dot x_{ed}-J_\xi\dot\xi$ is
   defined (Eq. 19), but Eq. 20 inverts the uncompensated $\dot x_{ed}$,
   and the text says modal variables are hard to obtain; the compensation
   is described but apparently not used.
3. **EBVC control law** (§4.1, Eqs. 25–28).
   $\tau_i=k_{pi}e_i+k_{di}\dot e_i-\sum_{j=n+2}^{n+m+1}k_{ij}(t)f_{ij}(t)$,
   with adaptation
   $\dot k_{ij}=\alpha_if_{ij}\dot\theta_i-\beta_ik_{ij}-\frac{\alpha_ik_{pi}}{k_{ij}}e_i\dot\theta_{di}-\frac{\alpha_ik_{di}}{k_{ij}}\dot e_i\dot\theta_i$;
   $k_{ij}$ is clipped to
   $[-k_{ij\max},-k_{ij\min}]\cup[k_{ij\min},k_{ij\max}]$ with
   $k_{ij\min}>0$, and $f_{ij}$ is the $y$-deflection of an appendage point
   in the floating frame. Setting $k_{ij}\equiv0$ recovers PD (Eq. 38).
4. **Dissipation** (§4.2, Eqs. 29–34). With
   $V=E_k+E_p+\tfrac12\sum k_{pi}(\theta_{di}-\theta_i)^2+\tfrac12\sum\sum k_{ij}^2/\alpha_i$,
   substitution gives $\dot V=-\sum_i\sum_j(\beta_i/\alpha_i)k_{ij}^2\le0$;
   the paper concludes the closed loop is "energy dissipative" and stable.
   Proved only to negative semi-definiteness: no convergence of tracking
   error or vibration is claimed in the proof, the clipping of $k_{ij}$ is
   not covered, and the vibration suppression itself rests on simulation
   and experiment.
5. **Planar, stationary target** (§5.1.1). Peak deflection of appendage
   B5: 193 mm (PD) against 143 mm (EBVC); EBVC amplitude below 10 mm after
   $t=3$ s, PD still 60 mm at $t=10.4$ s; capture at $t_f=12.52$ s with
   EBVC. Shown (simulation).
6. **Planar, moving target** (§5.1.2). Peak 100 mm (PD) against 74 mm
   (EBVC); final deflection −63 mm (PD) against −2.8 mm (EBVC, which
   satisfies the grasp condition). Shown (simulation).
7. **3D, 7-DOF** (§5.2.2). Final wing deflection −23 mm (PD) against
   −0.02 mm (EBVC); vibration near zero after 40 s with EBVC; capture
   commanded at 49 s (PD) and 51.7 s (EBVC). Shown (simulation).
8. **Experiment** (§6.2). With EBVC the vibration is "substantially zero
   after 24 s"; with PD the piezoelectric voltage is still up to 2.5 V at
   the end. Shown (experiment, qualitative curves).

# Methods

* **Model** (§2.1, Eqs. 1–4): an $n$-DOF serial manipulator on a rigid
  base with $m$ flexible appendages, each on a 1-DOF hinge. Floating-frame
  formulation with assumed modes, $^i\eta_P=\varphi\xi(t)=\sum_{j=1}^{s_i}\varphi_j\xi_j$,
  modal matrix from FEM. Block dynamics (Eq. 4) with sub-mass matrices
  $H_{bb},H_{b\theta},H_{b\xi},H_{\theta\theta},H_{\theta\xi},H_{\xi\xi}$,
  a Coriolis/centrifugal matrix, a stiffness matrix and the joint torque,
  taken from the authors' ref. [25]. No integrator, time step or solver is
  stated.
* **Kinematics** (Eqs. 5–8): base Jacobian built from the identity and
  the skew matrix of $p_{1e}=p_e-r_1$; manipulator Jacobian with columns
  $k_i\times(p_e-p_i)$ over $k_i$.
* **Closed-loop capture** (§3, Fig. 4): stopping criteria on position,
  orientation and time; pose errors (Eqs. 14–15); target velocities
  assumed known (estimation not studied); end-effector velocity planning
  in PD form with saturation (Eqs. 16–18), gains diag[1,1,1]; joint-rate
  saturation (Eq. 23); $\Theta_d=\Theta+\dot\Theta_d\Delta t$ (Eq. 24).
* **Planar case** (§5.1, Fig. 5, Table 1): 3-DOF arm; two appendages of
  length 3.5 m, linear density 10 kg/m, $EI=175$ kg m² (units as printed),
  mounted at ±0.75 m on the base; base 1530 kg, target 5000 kg; initial
  joint angles $[-80^\circ,80^\circ,80^\circ]$, target at $[4.22,0.45]$ m, 90°.
* **3D case** (§5.2, Tables 4–5): 7-DOF arm; one solar wing
  16.262 × 2.29 × 0.025 m, density 30 kg/m³, Young's modulus
  $8\times10^9$ Pa, Poisson ratio 0.3; ANSYS modal analysis gives first
  three natural frequencies 0.1841, 1.1154, 2.4119 Hz; the target frame is
  the apogee-engine nozzle frame, 2.29 m from the target centre of mass;
  base 1500 kg, target 5000 kg.
* **Experiment** (§6, Fig. 28): single-DOF air-bearing robot on a marble
  platform; steel-plate link; thin aluminium-plate appendage;
  piezoelectric sensor; 24 V supply; joint moved from 0° to 20° along a
  third-order polynomial over a 20 s planning time (30 s total), with a
  large initial vibration imposed. Experimental controller gains are not
  stated.

# Tests and results

* **§5.1.1, planar, stationary target** (Table 2 gains $k_p=0.01$,
  $k_d=1600$, $\alpha=50000$, $\beta=0.1$): deflections as in claim 5
  (Figs. 7–8). Base attitude 0° to "29.1°" (PD) and −29.2° (EBVC), base
  position $[0.0382,-0.0388]$ m and $[0.0382,-0.0387]$ m (Fig. 10):
  "essentially identical".
* **§5.1.2, planar, moving target**, $v_t=[-100\sin2t,\,100\sin2t]$ mm/s,
  $\omega_t=\sin(2t)$ °/s (Eqs. 39–40), Table 3 gains $k_p=2000$,
  $k_d=160$, $\alpha=50000$, $\beta=0.1$: deflections as in claim 6. Base
  attitude 0° to −33° (PD) and −30.2° (EBVC); position $[0.045,-0.042]$ m
  and $[0.039,-0.039]$ m (Fig. 16). With PD the base accelerations jump
  after about 12 s, exciting large vibrations (Fig. 17).
* **§5.2.2, 3D, moving target**: target velocity $[-5,5,5]$ mm/s and
  angular velocity $[0.3,0,0]$ °/s; gains $K_p=[80,80,20,40,2,20,0.2]$,
  $K_d=[200,280,100,120,10,120,1]$,
  $\alpha=[1.5\times10^6,1.5\times10^6,900,40,2,2,1]$, $\beta=0.1$;
  thresholds 0.01 m and 1°. Results as in claim 7. Final base attitude
  $[8.66^\circ,-39.73^\circ,-2.242^\circ]$ (PD) and $[9.49^\circ,-39.85^\circ,-2.77^\circ]$ (EBVC);
  base position $[-0.047,-0.0016,-0.023]$ m and
  $[-0.049,-0.0022,-0.025]$ m.
* **§6.2, experiment**: as in claim 8; Fig. 31 shows the adaptive gain
  going to zero once vibration and joint velocity vanish.

# Notation map

The paper is outside the bundle's domain; its symbols are kept in words.

| Meng et al. (2018) | Registry | Note |
|---|---|---|
| $\theta_i$, $\Theta$ | words (joint angle, joint vector) | **collision:** registry $\theta$ is the azimuthal coordinate |
| $\varphi$, $\varphi_j$ | words (modal matrix, mode shapes) | not the electrostatic potential $\phi$ |
| $\xi$, $\xi_j$ | words (modal coordinates) | not a registry symbol (the registry mentions $\xi$ only as some sources' permittivity factor) |
| $s_i$, $s$ | words (number of modal coordinates) | **collision:** registry $s$ is the species index |
| $E$ (in $J_b$), $E_k$, $E_p$; $E$ (Table 4) | words (identity matrix; kinetic and elastic energies; Young's modulus) | **collision** with the electric field $\mathbf E$ |
| $k_i$, $k_{ij}(t)$, $k_{pi}$, $k_{di}$ | words (joint-axis unit vector; adaptive gain; PD gains) | **collision:** registry $k$ is a wavenumber |
| $\alpha_i$, $\beta_i$ | words (adaptation gains) | not $\alpha_{\mathrm B}$ |
| $\lambda$, $\lambda_m$ | words (damped-least-squares damping) | not $\lambda_D$, $\lambda_w$, $\lambda_{\mathrm{mfp}}$ |
| $\omega_e$, $\omega_t$, $\omega_1$ | words (angular velocities) | **collision:** registry $\omega$ is a mode angular frequency |
| $\varepsilon$, $\varepsilon_p$, $\varepsilon_o$ | words (thresholds) | not $\varepsilon_0$ |
| $H_{bb}$, $H_{b\theta}$, … | words (sub-mass matrices) | **collision:** registry $H$ is spectral entropy |
| $f_{ij}(t)$ | words (vibration feedback signal) | **collision:** registry $f_s$ is a distribution function |
| $m$ | words (number of appendages) | not $m_s$ |
| $\tau_i$, $V(t)$, $J_g$, $J_\xi$ | words (joint torque, Lyapunov function, Jacobians) | no registry entry |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Meng_Vibration_suppression_control_of_free-floating_space_robots.pdf`.
   * **Version.** Publisher's final typeset PDF (version of record), 15
     pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.07.044, printed on page 1
     and checked on Crossref: title, the seven authors, Acta Astronaut.
     151:904–918 match; published in print October 2018. Page 1 gives
     received 18 Dec 2017, revised 14 Jul 2018, accepted 22 Jul 2018,
     online 24 Jul 2018. Page 1 matches the filename title.
   * **How it was read.** Full text layer. Eq. 4 and Eqs. 22, 25, 27,
     31–34 are garbled in the text layer; Eqs. 22 and 25–34 were read from
     rendered pages 6 and 8 (pp. 909, 911); Eq. 4 is recorded only in
     block structure, not term by term. Figure curves (Figs. 6–17, 23–31)
     were read only where the text quotes numbers.
   * **Recorded as printed.**
     * §4.1 restricts $k_{ij}$ away from zero ($k_{ij\min}>0$, needed
       because Eq. 27 divides by $k_{ij}$), yet §6.2 and Fig. 31 state that
       "the value of k becomes zero".
     * Eq. 31 uses $k_{ij}^2/\alpha_i$; Eqs. 32–33 switch to
       $k_{sj}\dot k_{sj}/\alpha_i$.
     * The text calls the stiffness matrix $K_\varphi$; Eq. 4 prints
       $K_\xi$.
     * Eq. 19 writes $J_g^{-1}$ although $J_g$ is $6\times n$ (non-square
       for $n=3$ and $n=7$); Eq. 20 inverts the uncompensated velocity
       instead of the compensated one defined in Eq. 19.
     * §5.1.1 gives the PD base attitude change as "0° to 29.1°" and the
       EBVC one as −29.2°; Fig. 10 shows both negative (sign dropped).
     * Table 2 (stationary case) gains $k_p=0.01$, $k_d=1600$ against
       Table 3 (moving case) $k_p=2000$, $k_d=160$: the stationary values
       look transposed or mis-scaled; not verifiable.
     * Fig. 28 caption: 5 = piezoelectric sensor, 6 = aluminium plate,
       7 = aluminium block; §6.1 says label 5 = flexible appendage,
       6 = piezoelectric sensor, and again "Label '5' represents aluminium
       blocks".
     * §6.2 speaks of "the end of the simulation" for the experiment.
     * The text after Eq. 47 calls $\omega_t$ "the angular velocity of the
       chaser's base"; it is the target's.
     * The introduction attributes ref. [24] to "Zhang et al.", but ref.
       [24] is Yu, Liu & Cai (2016); "Benoit [7]" uses the given name of
       ref. [7]'s first author, B.P. Larouche.
     * Reader's check: in the Lyapunov derivation the $k_{di}$ term
       cancels out of $\dot V$ via Eq. 27, so all dissipation in the proof
       comes from the $\beta_i$ leakage term.
   * **Reference list.** 36 printed entries ([1]–[36]), matching the
     Crossref reference count.
