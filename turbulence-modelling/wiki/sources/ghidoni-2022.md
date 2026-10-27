---
type: Source
title: "Ghidoni et al. (2022) — Assessment of an adaptive time integration strategy for a high-order discretization of the unsteady RANS equations"
description: "Assessment of embedded-error time-step controllers (standard, PI 4.2, H211b, H312b, smooth limiter) for linearly implicit Rosenbrock and peer schemes in a high-order modal DG solver of URANS with a log-omega k-omega model, on cylinder, tandem-cylinder and vertical-axis wind-turbine flows."
resource: "doi:10.1002/fld.5131"
source_kind: paper
authors: [Ghidoni A., Massa F.C., Noventa G., Rebay S.]
year: 2022
venue: "Int. J. Numer. Methods Fluids 94:1923-1963"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_International_Journal_for_Numerical_Methods_in_Fluids_Ghidoni_Assessment_of_an_adaptive_time_integration_strategy_for_a_hi.pdf"
tags: [time-integration, dg, rans, k-omega, bluff-body]
timestamp: 2026-10-27T15:28:00Z
---

# Summary

Ghidoni et al. (2022) assess adaptive time-step control for linearly
implicit high-order time integration of the unsteady RANS equations, a
numerics paper whose turbulence content is the stiffness that the
[$k$-$\omega$ model](/methods/k-omega-model.md) (in the logarithmic form
$\tilde\omega_\ell=\ln\omega$, with $k$ limited to $\max(0,k)$) adds to the
system. Space is discretized by the authors' modal
[discontinuous Galerkin](/methods/discontinuous-galerkin-spectral-element-method.md)
method (BR2 viscous fluxes, exact-Riemann Godunov flux; an
artificial-compressibility Riemann solver for incompressible flow, which
turns the semi-discrete system into a DAE). Two families of time
integrators are compared: one-step Rosenbrock-type Runge–Kutta schemes
(ROS3PL, RODASP, ROD5_1, orders 3–5) and two-step linearly implicit peer
schemes (peer3/4/5), started by the authors' earlier procedure. The step
is controlled from an embedded error estimator by four controllers
(standard, PI 4.2, H211b, H312b), an arctan smooth limiter, a correction
factor and a step cap. For RANS the estimator must include $k$ and
$\tilde\omega_\ell$ in an $L^2$ norm over all variables.

Orders are verified on a laminar travelling-wave and an inviscid
isentropic-vortex case at $N=6$. The turbulent tests are 2D URANS at $N=5$
of the [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md) at
$Re_D=3900$ (compressible and incompressible) and $Re_D=140\,000$, tandem
cylinders at $Re_D=166\,000$, and a three-blade vertical-axis wind turbine
at $N=2$. The main finding: for small steps adaptivity changes nothing (no
rejections), but it extends the "near-stability zone", the largest step a
linearly implicit scheme tolerates on the nonlinear system, by up to an
order of magnitude, sometimes at lower cost. H211b-smooth and H312b are the
most robust controllers on the stiffer cases. The 2D URANS force
coefficients of the cylinders differ from LES, DNS and experiment but agree
with other 2D URANS; the reference values quoted include
[LES](/definitions/large-eddy-simulation.md), RANS–[implicit LES](/definitions/implicit-les.md)
and [Spalart–Allmaras](/methods/spalart-allmaras-model.md)-based
[DES](/methods/detached-eddy-simulation.md) results, and adaptive
integration for [hybrid RANS/LES](/definitions/hybrid-rans-les.md) is named
as future work. The evidence is numerical, on one solver.

# Version read

Version of record (Wiley, open access CC BY; received 7 February 2022,
accepted 13 July 2022), 41 pages (pp. 1923–1963), read fully; Eqs.
(1)–(8), (19)–(25), (32)–(35), (61)–(68) and Table 8 checked visually.
Page 1 matches the metadata; no identity issue. Equation, table and
reference numbers are those of this version.

# Key claims

Page-local symbols: $\Delta t^n$ the $n$-th step; $r^{n+1}$ the embedded
local error estimator, $q_r$ its order, $\mathrm{TOL}$ the tolerance;
$\alpha^{\mathrm c}_j$, $\beta^{\mathrm c}_j$ the controller coefficients
(the source's $\alpha_j$, $\beta_j$); $\kappa_{\mathrm s}$ the
smooth-limiter parameter, $\eta_{\mathrm c}$ the correction factor,
$\Delta t_{\max}$ the step cap (the source's $\kappa$, $\eta$,
$\Delta t_{limit}$); $s$ the number of stages; $\lambda_{\mathrm{tsr}}$ the
tip-speed ratio; $C_{\mathrm{pow}}$ the turbine power coefficient; $T$ the
shedding (or test) period; $\theta_{\mathrm{sep}}$ the separation angle.

1. Adaptive time-step strategies for implicit integration of DG-discretized unsteady RANS had not been assessed; prior assessments exist only for Navier–Stokes (refs 7, 8) (§1). **Stated**
2. Rosenbrock and peer schemes are linearly implicit: one linear system per stage, the Jacobian assembled once per step (or less often for peer) (§1, §4). **Stated**
3. Although A- and L-stable, linearly implicit schemes applied to nonlinear ODE/DAE systems suffer a step-size restriction because they solve a linearized system; its limit is called the "near-stability zone", a drawback relative to nonlinear implicit schemes (§4). **Stated**
4. Table 1: ROS3PL one-step, order 3, 4 stages, embedded order 2; RODASP order 4, 6 stages, embedded 3; ROD5_1 order 5, 8 stages, embedded 4; peer3/4/5 two-step, orders 3/4/5, 3/4/5 stages, embedded 2/3/4, not self-starting; all A- and L-stable (Table 1). **Stated**
5. All one-step schemes verify the design order (3, 4, 5) on travelling waves and the isentropic vortex at $N=6$, $50\times50$ quadrilaterals, 70 000 DOFs per equation, linear-solver tolerance $10^{-16}$; errors below $10^{-11}$ are polluted by the spatial error (§4.1, Tables 2–3, Figs 1–2). **Shown**
6. Peer schemes with exact initialization verify orders 3, 4, 5 on both cases; their performance deteriorates in the compressible (ODE) case (§4.2, Tables 5–6). **Shown**
7. Peer schemes tolerate an inexact Jacobian: freezing it reduces cost, but beyond a refresh interval of 10 steps (peer3) or 5 (peer4, peer5) the saving is lost to slower linear solves; the largest saving, for peer5, is about 24% at $\Delta t=T/200$ (§4.2, Fig. 3). **Shown**
8. With the chosen peer parameters (Table 4: peer3 2.165162598341552, peer4 1.038881828680110, peer5 0.5614731292097847, all with angle $90°$) the peer methods reach order $s$ for constant steps, one more than the guaranteed $s-1$ (§4.2, Table 4, from Podhaisky et al.). **Stated**
9. The starting procedure preserves the global accuracy of the peer scheme whichever one-step starter is used (ROS3PL or RODASP); a lower-order starter makes the start more expensive (§4.2, Table 7). **Shown**
10. For RANS the error estimator must include all variables, including $k$ and $\tilde\omega_\ell$ (irregular, and the main cause of instability); a domain average of the per-variable estimators is not enough, the $L^2$ norm $r^{n+1}=\sqrt{\sum_j(r_j^{n+1})^2}$ is mandatory; using only the turbulent variables could give too small steps (§5, Eq. 67). **Stated**
11. All four controllers' coefficient sets satisfy $\sum_j(\alpha^{\mathrm c}_j+\beta^{\mathrm c}_j)=1$ (Table 8). **Stated** *(compiler check, not in the sources: the identity holds for every row of Table 8.)*
12. For small steps all controller/scheme combinations behave like fixed-step runs with no rejected steps; adaptivity becomes useful only near the near-stability zone, and lets the run go beyond it (§6.1, Figs 7–9, §7). **Shown**
13. Cylinder at $Re_D=3900$ (compressible): H211b gives the largest increase of the near-stability zone, up to one order of magnitude for schemes with more stages; ROS3PL gains much robustness at reduced or negligible extra cost (§6.1, Table 10). **Shown**
14. With H211b-smooth (compressible, $Re_D=3900$), ROS3PL is best at relatively high error levels, ROD5_1 at low ones; $\kappa_{\mathrm s}=0.4$ is the best compromise of cost and robustness (§6.1, Figs 11–12). **Shown**
15. Incompressible $Re_D=3900$: robustness gains are larger than in the compressible case; H211b-smooth and H312b give the largest near-stability increase; the peer schemes show the highest increase at reduced or negligible extra cost (except peer4: +9.94% clock time) (§6.1, Table 11). **Shown**
16. Incompressible: ROD5_1 loses its compressible-case efficiency, and RODASP and peer5 outperform it at low error. Observed orders on the turbulent cylinder: ROS3PL 2.8, RODASP 4.3, ROD5_1 5.4, peer3 3.3, peer4 3.1, peer5 1.8 (§6.1, Fig. 15). **Shown**
17. URANS at $N=5$, cylinder $Re_D=3900$: incompressible $C_D=1.52$, $C_{L,\mathrm{rms}}=1.13$, $St=0.23$; compressible $C_D=1.62$ (the text and Table 9 differ on $C_{L,\mathrm{rms}}$ and $St$; see Printed slips). The values differ from LES, DNS and experiment but agree with other 2D URANS (Rajani et al., 2D: $C_D=1.65$, $St=0.244$), which the authors attribute to the 2D simulation missing 3D effects (§6.1, Table 9). **Shown**
18. The compressible solver is more efficient than the incompressible one on complex cases because the DAE linear systems are worse conditioned (§6, §6.4). **Stated** (no separate evidence printed)
19. Cylinder at $Re_D=140\,000$ with $k$-$\omega$ (no trigger keeping the boundary layer laminar, unlike SA in Travin et al.'s DES): $St=0.271$, $C_D=0.751$, $\theta_{\mathrm{sep}}=91°$, $-C_{p,b}=0.86$, $L_r/D=0.72$, $C_{L,\mathrm{rms}}=0.44$, close to the 2D RANS of Moussaed et al. (§6.2, Table 12). **Shown**
20. At $Re_D=140\,000$, H211b-smooth and H312b are the best controllers; the smooth limiter removes the sharp step changes of the standard controller (§6.2, Table 13, Fig. 19). **Shown**
21. Tandem cylinders, $Re_D=166\,000$, $L/D=3.7$: the stability improvement costs efficiency for all schemes and controllers (Table 14); the influence of smoothing and of the controller order grows with the stiffness of the case (§6.3). **Shown**
22. Limiting the maximum step $\Delta t_{\max}$ substantially improves the robustness and efficiency of the controllers, which are not affected by the bound on the maximum increase or reduction ($\eta_{\mathrm c}$) (§6.3, Figs 26–28). **Shown**
23. Vertical-axis wind turbine at $\lambda_{\mathrm{tsr}}=1.5$: ROS3PL + H211b-smooth gives a mean step $0.023\,c/u_\infty$ (maximum 0.0475, minimum 0.0142), against mean 0.0038, maximum 0.035, minimum 0.00012 in the authors' earlier implementation (Noventa et al., ref 4), a mean larger by a factor of about 6 (§6.4, Fig. 31). **Shown**
24. The largest stable fixed step of the turbine case is $0.014\,c/u_\infty$, 1.64 times smaller than the adaptive mean; about 9.5% of the steps are rejected (§6.4). **Shown**
25. Mean $C_{\mathrm{pow}}$ at $\lambda_{\mathrm{tsr}}=1.5$: Noventa et al. 0.152, this work 0.173, the 2D RANS of Raciti Castelli et al. 0.171 (Table 17). **Shown**
26. A sudden drop of the step near $\theta=85°$ coincides with the bottom blade being perturbed by a shed vortex and an instability growing on the suction side of the upstream blade (§6.4, Figs 29–31). **Shown**
27. Higher tolerances raise the rejected fraction (Table 18: 7.3–10.6% at the near-stability point), but a case-dependent optimal tolerance gives both robustness and efficiency gains (§7, Tables 18–19). **Shown**

# Printed slips

- **§1, §7 against Table 1:** ROS3PL is called a "three stages" scheme, while Table 1 gives 4 stages.
- **§3:** "the system (3) is firstly multiplied by an arbitrary smooth test function"; Eq. (3) is the turbulent stress, the system is Eq. (14).
- **§2:** "the turbulent and total stress tensor, $\hat\tau_{ij}$ and $\tau_{ij}$", while Eqs. (3)–(4) make $\tau_{ij}$ the turbulent and $\hat\tau_{ij}$ the total stress.
- **§6.3:** "the correction factor $\eta$, defined in Equation (5), and the maximum allowed time-step $\Delta t_{limit}$, defined in Equation (5)"; they are Eqs. (69) and (70), Eq. (5) is the heat flux.
- **§5:** "H221b controller"; Fig. 31 caption "H21b-smooth".
- **Eq. (32):** prints "$(W_{i,n}-W_0*i)$".
- **Eq. (62):** $\psi_T^{n+2-j}=TOL/\Delta t^{n+1-j}$. *(Compiler check, not in the sources: the controller formulas (64)–(66) follow from Eqs. (57), (60) and Table 8 only with $\psi_T^{n+2-j}=TOL/(\Delta t^{n+1-j})^{q_r}$; with that exponent every exponent of $\Delta t$ and $r$ in (64)–(66) checks.)*
- **Table 2, ROD5_1 pressure, row $T/160$:** printed order 5.00. *(Compiler check, not in the sources: the printed errors 3.96E−10 at $T/160$ and 4.79E−11 at $T/320$ give $\log_2 8.27=3.05$; the velocity columns, 6.16E−10 and 1.94E−11, give 4.99.)*
- **§6.1 against Table 9:** the text gives the compressible $c'_L=1.19$ and $St=0.225$; Table 9 ("RANS DG-P5 comp.") gives $c_{L\,rms}=1.13$ and $St=0.23$.
- **Table 10, 11, 14 captions:** "DG-P6" and "$tol_{System}=10^{-16}$", while §6.1 and Figs 7–9 state DG-P5 and $tol_{system}=10^{-14}$ (Table 13's caption says DG-P5).
- **Tables 13–14 percentages.** *(Compiler check, not in the sources: Table 13, ROS3PL standard, 1.19E−05/1.38E−06 gives +762% against the printed 3416.51%; Table 18 prints 768.62% for the same case. Table 14's caption limits are identical to Table 13's and do not reproduce Table 14's percentages, e.g. 5.91E−06/1.38E−06 gives +328% against the printed 4411.45%.)* Table 13's caption prints the ROD5_1 limit "56.24E−08", Table 14's "5.62E−08". Table 14's $\Delta$clock values for ROS3PL (155.25, 108.40, 88.65, 383.35, 140.42) differ from Table 18's for the same tandem rows (30.77, 6.67, −3.59, 147.69, 23.08), while the $\Delta$error values coincide.
- **Table 11 against Table 18** (incompressible $Re_D=3900$): $\Delta$error 4871.40 against 4876.08, $\Delta$clock −69.52 against −69.43, for the same runs.
- **Table 19, tandem:** the H211b-smooth row (2266.41, −3.59) equals Table 18's tandem H211b row; the PI 4.2 and H312b rows have identical $\Delta$error and $\Delta$clock (483.97, −15.38) with different rejected fractions.
- **§7 against §6.4:** the turbine is said to be computed "with the ROS3PL scheme and the H211b controller" (§7) and with H211b-smooth (§6.4).
- **Citations against the reference list:** "Lourenco and Shih exp.31" and "Parnaudeau et al.31" both cite ref 31 (Parnaudeau et al.; Lourenco & Shih are not listed); "Mittal and Moin32" and "Beaudan and Moin.32" cite ref 32, which is Kravchenko & Moin (2000); Table 12 cites "Travin et al. SA-DES" as ref 44, which is Shur, Spalart, Strelets & Travin on an airfoil at high angle of attack; ref 27 (Rajani et al.) is titled "LES of Flow past Circular Cylinder at Re=3900" but cited for 2D/3D URANS.
- **Fig. 19 caption:** the exponent of "$\|err_p\|\sim10$" is displaced.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $u_i$, $p$, $T$ (no averaging symbol) | $\langle\rho\rangle$, $\langle u_i\rangle_\rho$, $\langle p\rangle$, $\langle T\rangle_\rho$ | mean-flow variables; averaging not marked in the source |
| $\bar k=\max(0,k)$ | $\max(0,k)$ | **collision:** the overbar is a limiter, not the LES filter |
| $\tilde\omega=\log\omega$, $\tilde\omega_r$ | $\tilde\omega_\ell$, (realizability-constrained value, page-local) | **collision:** the tilde is a logarithm, not a Favre filter |
| $\bar\mu_t=\alpha^*\rho\bar ke^{-\tilde\omega_r}$ | $\mu_t$ | |
| $\tau_{ij}$ | $-\langle\rho u_i''u_j''\rangle$ | **negative convention**; Boussinesq form with $-\frac23\rho k\delta_{ij}$ |
| $\hat\tau_{ij}$ | $\sigma_{ij}-\langle\rho u_i''u_j''\rangle$ | total stress; **collision:** hat is not a test filter |
| $\alpha,\alpha^*,\beta,\beta^*,\sigma,\sigma^*,\sigma_d$ | $\gamma_\omega$, $\alpha^*$, $\beta_\omega$, $\beta^*$, $\sigma_\omega$, $\sigma_k$, $\sigma_d$ | $k$-$\omega$ constants, values not printed |
| $e_0$, $h_0$ | (total energy and enthalpy per unit mass) | |
| $\mathbb P^k_d$, DG-P$k$ | $N$ | **collision:** the source's $k$ is the polynomial degree |
| $\gamma$ | $\gamma$; (Rosenbrock diagonal, peer parameter, page-local) | three meanings in the source |
| $\boldsymbol\omega$ (frame rotation) | $\Omega_{\mathrm{rot}}$ | **collision** with the specific dissipation rate |
| $\alpha_j$, $\beta_j$, $z$ | $\alpha^{\mathrm c}_j$, $\beta^{\mathrm c}_j$, (history length) | controller coefficients, Table 8 |
| $\kappa$, $\eta$, $\Delta t_{limit}$ | $\kappa_{\mathrm s}$, $\eta_{\mathrm c}$, $\Delta t_{\max}$ | **collisions** with the von Kármán constant and the Kolmogorov length |
| $\mu$ (safety factor, 2) | $\mu_{\mathrm s}$ (page-local) | **collision** with the viscosity |
| $TOL$, $r^{n+1}$, $r_j$, $q_g,q_l,q_r$ | same, page-local | |
| $\lambda$ | $\lambda_{\mathrm{tsr}}$ | **collision** with the Taylor microscale |
| $c_P$ | $C_{\mathrm{pow}}$ (page-local) | **collision:** not the pressure coefficient $C_p$ |
| $c_D$, $c'_L$, $c_{L\,rms}$, $c_{pb}$ | $C_D$, $C_{L,\mathrm{rms}}$, $C_{p,b}$ | |
| $L_r/D$ | $L_r/D$ | |
| $y^+_1$ | $y_1^+$ | first-element height |
| $M_P$, $J_P$, $R$, $\tilde R$ | (mass matrix, Jacobian, residual, page-local) | |

# Reference list

51 printed references, numbered (Wiley style), all parsed. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. Same-author same-year works are keyed in printed order
(Bassi et al. 2015, refs 1 and 3; Bassi et al. 2014, refs 5 and 18).
Ref 10 (Steinebach) prints "Techn. Hochsch., Fachbereich Mathematik;
1995:1995" and is recorded as a 1995 report; ref 37 has a malformed
author list and no venue; ref 42 is a book chapter without a book title.
The citation–content mismatches of refs 27, 31, 32 and 44 are listed
under Printed slips. No printed duplicate.

# Pages created or updated

Chunk 10 (2026-10-27). This source is cited on:

- [Circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Wilcox k-ω model](/methods/k-omega-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
