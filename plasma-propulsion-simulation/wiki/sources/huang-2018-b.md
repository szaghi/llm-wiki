---
type: Source
title: "Huang et al. (2018) — Fixed-time attitude tracking control for spacecraft without unwinding"
description: "Two fixed-time attitude tracking controllers on the rotation group (avoiding quaternion unwinding): a nonsingular terminal sliding surface with a Gudermannian reaching law giving initial-condition-independent settling-time bounds, and an adaptive variant converging to residual sets under bounded disturbance, with proved auxiliary lemmas and simulations of a rigid microsatellite."
resource: "doi:10.1016/j.actaastro.2018.04.041"
source_kind: paper
authors: [Huang B., Li A., Guo Y., Wang C.]
year: 2018
venue: "Acta Astronaut. 151:818–827"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Huang_Fixed-time_attitude_tracking_control_for_spacecraft_without.pdf"
tags: [context, attitude-control, fixed-time-stability, sliding-mode-control]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

Two fixed-time attitude tracking controllers for a rigid spacecraft whose
attitude is a rotation matrix rather than a unit quaternion, so that the
unwinding of the quaternion double cover is avoided (§1, §2.1). The attitude
error uses the rotation-matrix error function of Guo and Song (ref. [25];
Eqs. 6–7), valid where the trace of the error matrix differs from −1, i.e.
where the error vector has norm below 1 (Remark 1). Controller 1 (Eq. 38)
combines a new nonsingular terminal sliding surface (Eqs. 35–37) with a
reaching law built on the Gudermannian function (Eqs. 39–40) and, without
disturbance, has explicit settling-time bounds independent of the initial
conditions (Theorem 3). Controller 2 (Eqs. 60–62) adds a linear term to the
surface and an adaptive estimate of the disturbance bound with a projection
operator, giving fixed-time convergence to residual sets under bounded
disturbance (Theorem 4). Two auxiliary results (Theorem 1, an inequality;
Theorem 2, a practical fixed-time lemma) are proved. Simulations of a rigid
body with inertia about diag(22.7, 23.3, 24.5) kg·m² converge in about
9–20 s. Pure attitude control: nothing on propulsion or plasma.

# Key claims

Symbols are the paper's (see the notation map).

1. **Theorem 1** (Eq. 21, proved): for $\beta_1\ge2\beta_2>0$ and
   $0<\alpha<1$,
   $\beta_1^{1-\alpha}-\beta_2^{1-\alpha}\ge(2^{1-\alpha}-1)(\beta_1-\beta_2)^{1-\alpha}$,
   via monotonicity of an auxiliary function (Eqs. 22–25); see Recorded as
   printed for a faulty step.
2. **Theorem 2** (Eqs. 26–27, proved): if
   $\dot V_1\le-aV_1^{1+1/\mu}-bV_1^{1-1/\mu}+\phi$ with $a,b,\phi>0$,
   $\mu>1$, then $V_1\le2\theta$ (where
   $a\theta^{1+1/\mu}+b\theta^{1-1/\mu}=\phi$) is reached within
   $T_1\le\pi\mu/(2\chi)$, $\chi=\min(a,\ b(2^{1-1/\mu}-1))$.
3. **Lemma 1** (Eqs. 14–16, attributed to ref. [29]):
   $\dot V\le-aV^{1-1/\mu}-bV^{1+1/\mu}$, $\mu>1$, gives fixed-time
   stability with $T\le\pi\mu/(2\sqrt{ab})$.
4. **Theorem 3** (Eqs. 41–44, proved, no disturbance): under Eq. 38 the
   surface is reached within $T_2\le\pi\eta_2/(2k_3)$; the error-vector norm
   stays below 1 for all time if it starts below 1 and the initial surface
   value is bounded; the error and its rate enter explicit regions within
   $T_3\le\pi\eta_2/(2k_3)+\pi\eta_1/(4\sqrt{k_1k_2})$.
5. **Remark 3** (stated): unlike ref. [25], no region of attraction has to
   be imposed; the error-norm bound is maintained by the controller.
6. **Theorem 4** (Eqs. 63–65, proved, $\lVert d\rVert\le D$): under
   Eqs. 60–62 the surface converges to $\lVert S\rVert\le\sqrt{2\theta_1}$
   and the error and its rate to residual regions, with a convergence-time
   bound independent of initial states, under $0.5<\beta_1<1$,
   $k_4\ge1/4$ and the constants of Eq. 63.
7. **Remark 5** (stated): the projection keeps $|\hat D|\le D$, hence
   $|\tilde D|\le2D$.
8. **Contributions** (§1, stated): the first fixed-time attitude controller
   without unwinding "to the best of the author's knowledge"; a surface
   without the region-of-attraction limit of ref. [25]; disturbance handling
   that the fixed-time controllers of refs. [27,28] lack.

# Methods

Model (§2.1): kinematics $\dot R=R\omega^\times$ (Eq. 1), dynamics
$J\dot\omega=-\omega^\times J\omega+u+d$ (Eq. 2); errors
$\tilde R=R_d^TR$, $\tilde\omega=\omega-\tilde R^T\omega_d$ (Eqs. 4–5).
Error function (Eqs. 6–7, from ref. [25]):
$\psi(\tilde R)=2-\sqrt{1+\mathrm{tr}(\tilde R)}$,
$e_{\tilde R}=\frac{1}{2\sqrt{1+\mathrm{tr}(\tilde R)}}(\tilde R-\tilde R^T)^\vee$;
error dynamics rewritten as a double-integrator-like system (Eqs. 8–13) in
$x_1=e_{\tilde R}$, $x_2=\dot x_1$. Notation
$\mathrm{sig}(\xi)^\alpha=\mathrm{sign}(\xi)|\xi|^\alpha$. Auxiliary lemmas:
Gudermannian $\mathrm{gd}(\xi)=\int_0^\xi\mathrm d\upsilon/\cosh\upsilon$
(Lemma 2, ref. [30]); power-sum inequalities (Lemma 3, ref. [31]);
$(a-b)^\zeta\le a^\zeta-b^\zeta$ for $\zeta>1$ (Lemma 4, ref. [32]).

Controller 1 (§3.1): surface
$S=x_2+\frac{k_1\mathrm{sig}(x_1)^{1+2/\eta_1}+k_2H(x_1)}{1-x_1^Tx_1}$
(Eq. 35), with $H$ switching below a threshold $\delta$ to
$\lambda_1x_{1i}+\lambda_2\mathrm{sig}(x_{1i})^c$ to avoid the
terminal-sliding singularity, $\lambda_1$, $\lambda_2$ chosen for $C^1$
continuity (Remark 2), $0<\delta<1$, $1<c\le2$, $\eta_1>2$; reaching term
$k_3G(S)$ with a Gudermannian-type $G$ (Eqs. 39–40), $\eta_2>2$. Controller
2 (§3.2): surface Eq. 35 plus $k_4x_1$; control Eq. 61 with two power-law
terms and a disturbance-compensation term $-\hat D\,J^{-T}E^TS/\lVert S^TEJ^{-1}\rVert$;
adaptive law with projection
$\dot{\hat D}=\mathrm{Proj}_{\hat D}[k_7(\lVert S^TEJ^{-1}\rVert-k_8\hat D)]$
(Eq. 62). In simulation the sign function is replaced by a saturation with
boundary layer 0.02 (Remark 7, Eq. 75). Integrator, step size and software
are not stated; Scenario 1 clips the torque at ±2 N·m.

# Tests and results

Common data (§4): inertia with rows $[22.7,0.2,-0.5]$, $[0.2,23.3,0.3]$,
$[-0.5,0.3,24.5]$ kg·m²; desired angular velocity
$[0.01\sin(t/40),-0.01\cos(t/50),-0.01\sin(t/60)]^T$ rad/s; desired
initial attitude the identity; called "a microsatellite".

* **Scenario 1** (§4.1, Figs. 1–5; Eq. 38, no disturbance): initial
  angular velocity $[0.1,0.1,0.1]$ rad/s; $\delta=0.5$, $c=1.4$,
  $\eta_1=2.5$, $\eta_2=7$, $k_1=k_2=0.2$, $k_3=1$. Stated bounds
  $T_2=10.99$ s, $T_3=20.79$ s. Observed: surface reached within 9 s,
  attitude tracked within 19 s, torque within the ±2 N·m clip with a
  residual oscillation of order 0.02 N·m after 12 s.
* **Scenario 2** (§4.2, Figs. 6–15; Eqs. 61–62, disturbance
  $0.001[\sin(0.1t),-\cos(0.1t),\sin(0.1t)]^T$ N·m): $\delta=0.5$,
  $c=1.4$, $\eta_1=3$, $\eta_2=10$, $k_1=k_2=0.3$, $k_3=0.25$, $k_4=0.5$,
  $k_5=1$, $k_6=0.5$, $k_7=1$. Case 1 (Scenario 1 initial state): surface
  in about 15 s, attitude within 18 s; the disturbance-bound estimate
  starts at 0.001 and decays from about 11 s to near 0 by about 25 s
  (Fig. 11). Case 2 (a second initial attitude, initial angular velocity
  $[0.2,0.2,0.2]$ rad/s): surface within 18 s, attitude at about 20 s. The
  paper calls the convergence times "almost the same"; two cases
  illustrate, they do not demonstrate, initial-condition independence.

# Notation map

Attitude-control symbols; the registry has no attitude-dynamics section.

| Huang et al. (2018) | Registry | Note |
|---|---|---|
| $R$, $R_d$, $\tilde R$ | words (rotation matrices) | **collision:** registry $\mathbf R_{sk}$ is a friction force density |
| $\omega$, $\omega_d$, $\tilde\omega$ | words (angular velocity) | **collision:** registry $\omega$ is a mode angular frequency |
| $J$ | words (inertia matrix) | not the current density $\mathbf j$ |
| $u$ | words (control torque) | **collision:** registry $\mathbf u_s$ is a fluid velocity |
| $d$, $D$, $\hat D$, $\tilde D$ | words (disturbance, its bound, estimate, error) | **collision:** registry $\mathbf d$ is observed data |
| $E$ | words (kinematic matrix, Eq. 10) | **collision:** registry $\mathbf E$ is the electric field |
| $F$ | words (lumped nonlinear term, Eq. 13) | **collision:** registry $F$ is thrust |
| $S$ | words (sliding surface) | **collision:** registry $S(\mathbf x)$ shape function, $S_j$ Sobol' indices |
| $H$, $G$ | words (surface nonlinearity, reaching function) | **collision:** registry $H$ is the spectral entropy |
| $\eta_1$, $\eta_2$, $\eta_3$ | words (exponents) | **collision:** registry $\eta$ is the thrust efficiency |
| $\mu$ | words (fixed-time lemma exponent) | **collision:** registry $\mu_0$, $\mu_\perp$, $\mu_\parallel$ |
| $\lambda_1$, $\lambda_2$ | words (continuity coefficients) | **collision:** registry $\lambda$-family lengths |
| $c$ | words (exponent, $1<c\le2$) | **collision:** registry $c$ is the speed of light |
| $\theta$, $\theta_1$, $\theta_2$ | words (residual-set radii) | **collision:** registry $\theta$ is the azimuthal coordinate |
| $\delta$, $k_1$–$k_8$, $a$, $b$, $\phi$, $\chi$, $\beta_1$, $\beta_2$ | words (threshold, gains, constants) | $\phi$ is not the potential |
| $T$, $T_1$–$T_3$ | words (settling times) | not a temperature $T_s$ |
| $e_{\tilde R}$, $\psi$, $\mathrm{gd}$, $\mathrm{sig}$ | words | $e$ is not the elementary charge |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Huang_Fixed-time_attitude_tracking_control_for_spacecraft_without.pdf`.
   * **Version.** Publisher's final typeset version (Elsevier, © 2018
     IAA), 10 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.04.041, printed on page 1
     and checked on Crossref: title, all four authors, Acta Astronaut.
     151:818–827 match; issued 2018-10, no published-online field. Page 1:
     received 20 Jan 2018, revised 28 Mar 2018, accepted 23 Apr 2018, online
     30 Apr 2018. Page 1 matches the filename title. Second of the three
     Huang 2018 files in archive-filename order, hence `huang-2018-b`.
   * **How it was read.** Full text layer, equations checked on rendered
     pages; the long expressions of Eqs. 38, 46, 61 and 66–68 are recorded
     in words. Scenario 2 omits $\eta_3$, $k_8$, $\beta_1$, the bound $D$
     used by the projection and the initial estimate, so it cannot be
     reproduced from the paper. Remark 1's set symbol is missing from the
     typeset PDF ("must be developed in the set ,"); Remark 3 calls it
     $\Upsilon$.
   * **Recorded as printed.**
     * Theorem 1 proof, Eq. 24: the chain ends with
       $(1-\alpha)(x^{-\alpha}-(x-\beta_2)^{-\alpha})>0$, but that bracket
       is negative since $x>x-\beta_2>0$. Reader's check: the theorem still
       holds, because the derivative of the auxiliary function is positive
       iff $((x-\beta_2)/x)^\alpha>2^{1-\alpha}-1$, true at $x=2\beta_2$ and
       beyond.
     * Theorem 2 proof (after Eq. 33): "arctan$(U)=0$ only if $V_1=0$",
       but $U=0$ means $V_1=\theta$, and Eq. 29 was derived only for
       $V_1\ge2\theta$; the argument is loose about which set is reached.
     * The text of Eqs. 49–50 writes $\eta$ for $\eta_2$.
     * Reader's check (§4.1): $T_2=\pi\cdot7/2=10.996$ s matches 10.99 s,
       but $T_3=10.996+\pi\cdot2.5/0.8=20.81$ s against the printed
       20.79 s.
     * Reader's check (§4.1, §4.2): the printed initial attitudes are not
       rotation matrices: the Scenario 1 matrix has an off-diagonal entry
       of $RR^T$ of 0.753 (rows 1 and 3) and determinant 0.515; the Case 2
       matrix has squared row norms 0.734, 0.755, 0.753 and determinant
       0.554. §2.1 requires the rotation group; either the matrices are
       misprinted or the runs started off it.
     * §4.1 reports an error norm "≤ 1" where the objective (§2.4, Remark
       1) requires strictly below 1.
     * The theorems assume unconstrained torque; Scenario 1 clips it at
       ±2 N·m (on the clip for the first ~5 s, Fig. 5), and the paper says
       this has "nothing to do with the input saturation problem".
     * §1 credits "Zuo et al. [27,28]" with the fixed-time concept; ref.
       [27]'s first author is Tian, ref. [28] is a 2015 consensus paper,
       and Lemma 1 is cited to Defoort, Polyakov et al. (ref. [29]).
     * Scenario 2 settling times differ between the two cases (surface 15
       vs 18 s, attitude 18 vs 20 s); Theorem 4 gives no explicit number for
       these parameters.
   * **Reference list.** 32 printed entries ([1]–[32]), matching the
     Crossref reference count. No DOIs printed. Ref. [25] prints no year
     (Chin. J. Aeronaut. 27(2):375–382) and is keyed with `-nd`.
     Same-surname-year pairs take suffixes in printed order: Wu 2011 (refs.
     [11], [19]); Guo 2016 (refs. [3] H.D. Guo and [26] Y. Guo). Ref. [9] is
     printed "34 (6) (2012)" for J. Guid. Control Dyn., kept as printed.
