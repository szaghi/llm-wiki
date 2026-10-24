---
type: Method
title: "Operator splitting for stiff source terms"
description: "Operator splitting advances the transport part of a balance law with an explicit shock-capturing step and a stiff term separately: chemistry as a constant-volume reactor per cell, two-phase relaxation as algebraic infinite-rate projections, bubble sources by Strang splitting, DG damping as a closed-form implicit stage; for a Dirac-delta source splitting is never well-balanced."
status: established
aliases: [Strang splitting, fractional-step method, convection–chemistry splitting, constant-volume reactor step, relaxation splitting, infinite-rate relaxation]
tags: [finite-volume, software, gpu, reacting-flows, stiff-source, well-balanced, multiphase]
timestamp: 2026-10-23T20:39:00Z
---

# Operator splitting for stiff source terms

For a balance law $\partial_tu+\nabla\cdot f(u)=S(u)$ whose source $S$ is stiff (finite-rate
chemistry with time scales far below the convective one), **operator splitting** advances
the two operators in sequence over one time step $\Delta t$: a transport step
$\partial_tu=-\nabla\cdot f(u)$ with the shock-capturing scheme, and a source step
$\partial_tu=S(u)$ in which the flow is frozen and each cell is an independent
constant-volume reactor. The source step can then use a stiff ODE integrator with its own
sub-steps, independent of the CFL step. It is the alternative to coupled
[IMEX Runge–Kutta](/methods/imex-runge-kutta.md) stepping, in which the stiff term is
implicit inside the stages of one scheme.

## The reactor step

In both sources the source step solves, per cell $i$, the species and energy equations at
constant volume and density. [Bielawski et al. (2023)](/sources/bielawski-2023.md) (§5,
Eqs. (11)–(12)) write $\mathrm d(\rho Y_k)_i/\mathrm dt=(\Omega_k)_i$ for the partial
densities (page-local mass production rates $\Omega_k$ of species $k$; $Y_k$ the mass
fractions, registry §10) together with a temperature equation, which in practice is
replaced by a Newton–Raphson solve at constant internal energy; the species equation is
integrated with an explicit adaptive-step scheme batched over cells. The splitting is
justified by "the limiting chemical timescale" being "sufficiently smaller than the flow
timescales, allowing for the flow to be considered frozen" (§2).
[Weng & Mével (2023)](/sources/weng-2023.md) (§3.1–3.2, Eqs. (13)–(14), (20)–(21)) correct
the partial densities and the sensible internal energy by an implicit solve of
$(\partial_t\rho Y_k)_S=\dot R_k$, $(\partial_te_{\mathrm s})_S=-\sum_k\dot R_kh_{\mathrm f,k}$
(page-local production rates $\dot R_k$, sensible internal energy $e_{\mathrm s}$, formation
enthalpies $h_{\mathrm f,k}$), with the rate taken as the forward difference
$\dot R_k=(c_{k,1}-c_{k,0})/\Delta t$ of the concentrations before and after a Cantera
constant-volume reactor integration over $\Delta t$ (adaptive sub-steps, relative and
absolute tolerances $10^{-12}$ and $10^{-15}$). Because the reactor holds internal energy and
density fixed, its code does not depend on the equation of state, so the same splitting
serves the Redlich–Kwong and Noble–Abel real-gas laws without modification (§3.2).

## Splitting order

- **Strang splitting.** Bielawski et al. (§3) combine explicit second-order Runge–Kutta for
  the flow with Strang splitting "to achieve nominally second order accuracy", citing
  earlier work; no convergence study is shown.
- **Strang splitting with a stiff ODE solver.** The INCA solver in the immersed-boundary
  assessment of [Başkaya et al. (2024)](/sources/baskaya-2024.md) (§3.2) advances reacting
  hypersonic flow with third-order WENO, HLLC and the Gottlieb–Shu third-order Runge–Kutta
  scheme, and the chemistry by second-order Strang splitting with the VODE integrator; the
  second code of that paper, CHESS, applies a Gauss–Seidel chemistry step after the
  Runge–Kutta step. No splitting error is examined.
- **Sequential steps.** Weng & Mével (§3.1) describe the blastFoam sequence: the convection
  step (MUSCL reconstruction with a limiter, an
  [HLL-family](/methods/hll-riemann-solvers.md) flux, [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)),
  then the update of the primitive variables from the conserved ones, then, for reactive
  runs, the chemistry correction. The paper does not state whether the sequence is
  symmetrized, nor its order.
- **Strang splitting with an adaptive embedded Runge–Kutta pair.** In [MFC](/software/mfc.md) 5.0
  ([Wilfong et al. (2026)](/sources/wilfong-2026.md), §4.2.3) the stiff sub-grid bubble source is
  advanced for $\Delta t/2$, the transport for $\Delta t$, and the source again for $\Delta t/2$. The
  source sub-steps use the three-stage third-order TVD Runge–Kutta stages $k_1,k_2,k_3$ (page-local)
  with the embedded second-order solution
  $\hat u^{n+1}=u^n+\tfrac h8(3k_1+3k_2+2k_3)$ against $u^{n+1}=u^n+\tfrac h6(k_1+k_2+4k_3)$, so that the
  error estimate is $-\tfrac5{24}h(k_1+k_2-2k_3)$ for the sub-step $h$ (page-local). *(compiler check, not
  in the sources: $\tfrac16-\tfrac38=-\tfrac5{24}$ and $\tfrac46-\tfrac28=\tfrac5{12}$, consistent with the
  printed estimate.)* On a homogeneous bubble collapse with $p_\infty/p_{\mathrm b}=1427$ (page-local
  pressure ratio) the split solver runs at $\Delta t=0.8$ µs, where the unsplit scheme fails with a
  negative bubble radius and needs $\Delta t=0.008$ µs (Fig. 13). The paper calls the split solver
  second-order accurate in time (§7) without a temporal convergence test, and prints the governing
  equation as $\partial_tu=\nabla\cdot f(u)+s(u)$ while the transport sub-step carries
  $-\nabla\cdot f$.
- **An implicit damping step inside each Runge–Kutta stage.** In the entropy-stable
  oscillation-free DG scheme for MHD of [Liu et al. (2025b)](/sources/liu-2025-b.md) (§3.3,
  Eqs. (3.20)–(3.21)) the stiff term is the damping $\frac2h\sigma(u_h)(u_h-\bar u_h)$ (page-local
  coefficient $\sigma$ and element size $h$). Treated explicitly within third-order TVD Runge–Kutta
  it "may lead to restricted CFL conditions", so every forward-Euler stage is split into the
  explicit DG step $\tilde u$ and an implicit damping step solved in closed form,
  $u=\frac1{1+\alpha_\sigma}\tilde u+\frac{\alpha_\sigma}{1+\alpha_\sigma}\bar{\tilde u}$ with
  $\alpha_\sigma=\frac{2\Delta t}h\sigma(\tilde u)$ (page-local $\alpha_\sigma$; the paper's time step $\tau$), which keeps the cell
  mean and needs no iteration. The splitting is at most first order, but does not degrade the
  accuracy because $\sigma$ is of high order in smooth regions, the proof for linear scalar laws
  being referred to the [OEDG](/methods/oedg.md) paper; the CFL gain is not quantified.

## Two-phase relaxation: algebraic source steps

[Wakimura et al. (2024)](/sources/wakimura-2024.md) (§2.4, §3, Eqs. (9)–(20), (45), Apps. B–D)
solve the six-equation two-phase model of Pelanti and Shyue with heat and mass transfer by a
fractional-step method in which the stiff sources are **relaxation terms with infinite rates**:
pressure relaxation $\mu_{\mathrm p}(p_1-p_2)$, thermal relaxation proportional to $T_2-T_1$ and
chemical relaxation proportional to the difference of the phasic Gibbs energies (page-local rates
$\mu_{\mathrm p}$, temperatures $T_k$; $\phi_k$, $\rho_k$, $Y_k$ registry §10). With the rates set to
infinity each source step is an algebraic projection onto an equilibrium manifold, not an ODE
integration. With page-local operators $\mathcal H^{(\Delta t)}$ (hyperbolic step) and
$\mathcal R_{\mathrm p}$, $\mathcal R_{\mathrm{pT}}$, $\mathcal R_{\mathrm{pTg}}$ (mechanical,
mechanical–thermal and mechanical–thermal–chemical equilibrium), the four variants are (Eq. (45))

$$u^{n+1}=\mathcal R_{\mathrm p}\mathcal H^{(\Delta t)}u^n,\quad
\mathcal R_{\mathrm{pT}}\mathcal R_{\mathrm p}\mathcal H^{(\Delta t)}u^n,\quad
\mathcal R_{\mathrm{pTg}}\mathcal R_{\mathrm p}\mathcal H^{(\Delta t)}u^n,\quad
\mathcal R_{\mathrm{pTg}}\mathcal R_{\mathrm{pT}}\mathcal R_{\mathrm p}\mathcal H^{(\Delta t)}u^n;$$

only the last two reach Gibbs equilibrium, i.e. model phase change. Mechanical relaxation comes
first, on the assumption that it is the fastest process. MFC 5.0 adds the same infinite-rate
pT and pTg relaxations for $N$ fluids as a fractional step, solved by Newton's method
([Wilfong et al. (2026)](/sources/wilfong-2026.md), §4.1.3;
[six-equation model](/definitions/six-equation-model.md)).

- **Pressure equilibrium** (App. B): at constant $\phi_k\rho_k$, $\rho v$ and total energy, with
  interface pressure equal to the relaxed pressure $p^*$, the stiffened-gas law gives a quadratic
  for $p^*$ (Eqs. (B.5)–(B.6)), solved by a cancellation-free root formula (Eq. (B.7), App. E);
  the relaxed variables are stated to be mixture-energy consistent.
- **Pressure–temperature equilibrium** (App. C): at constant $Y_k$, $\rho$ and internal energy,
  again a quadratic in the common pressure (Eqs. (C.4)–(C.5)), with $\phi_1$ in closed form (Eq. (C.7)).
- **Gibbs equilibrium** (App. D): $Y_k$ now changes; eliminating it gives a quadratic for the
  temperature as a function of pressure (Eqs. (D.4)–(D.5)), substituted into the saturation curve
  and solved for the pressure by Newton–Raphson (Eq. (D.7)).

Thermal and chemical relaxation are activated only in mixture cells,
$\epsilon_I\le\phi_1\le1-\epsilon_I$ with $\epsilon_I=10^{-4}$ (page-local), and chemical relaxation
only where the liquid is superheated, $T_{\mathrm{liq}}>T_{\mathrm{sat}}(p)$, so the model has
evaporation and no condensation; the authors state that this does not affect the solution for
small enough $\epsilon_I$, without showing a comparison (§2.4, Eqs. (10)–(11)). The hyperbolic
step is HLLC in wave-propagation form with BVD-selected MUSCL/THINC reconstruction and SSP-RK3
([HLL-family solvers](/methods/hll-riemann-solvers.md),
[five- and six-equation models](/definitions/five-equation-model.md),
[stiffened gas](/definitions/stiffened-gas-equation-of-state.md)); the order of the splitting is
not stated or measured. On a 1D water cavitation tube the four variants are compared, and in a
2D piston-driven dodecane vapour-bubble compression the full p-pT-pTg sequence generates new
vapour bubbles near $y=0.5$ (§4.1, §4.4).

## Singular sources: splitting is never well-balanced

For the 1D Euler equations with a source concentrated at $x=0$,
$\partial_tu+\partial_xf(u)=\delta_{\mathrm D}(x)\,S$ with $\delta_{\mathrm D}$ the Dirac delta and,
for positive velocities on both sides, $S=\mathrm{diag}(k_1,k_2,k_3)\,f(u(0^-))$ (page-local
symbols; constants $k_l>-1$), the source induces a stationary wave at $x=0$ with jump relation
$f(u^-)+S=f(u^+)$, $u^\mp=u(0^\mp)$ ([Yu, Liu & Feng (2023)](/sources/yu-2023.md), §1–§2). Splitting advances
$u^{n+1}=\mathcal S^{(\Delta t)}\mathcal C^{(\Delta t)}(u^n)$, with $\mathcal C$ the convection
and $\mathcal S$ the source solution operator (page-local; Eqs. (3.5)–(3.6)).

**Theorem 3.1** (Yu et al.): the splitting method is not well-balanced for any $\Delta t>0$,
even when both sub-problems are solved exactly. The proof: exact convection of the
stationary data $(u^-,u^+)$ changes them, because the classical Riemann problem between
$u^-$ and $u^+$ would otherwise be a single stationary contact, which needs zero velocity on
both sides and so contradicts $u^-\ne u^+$, or a single stationary shock, excluded by their
admissibility criterion; the source step acts only at $x=0$, so the perturbation that the
convection step leaves elsewhere persists (Proof 3.1). Their upwind discretization of the
source step (Eq. (3.9)) maps every stationary state to itself (stated, "It can be shown"), so the defect comes from
the convection step, and they conclude that no consistent and stable choice of the
transport scheme can repair it (§3.1). In their Test 1 the split scheme (third-order DG with
a TVD limiter and local Lax–Friedrichs fluxes) shows spurious perturbations along the three
characteristic families and overshoots at the origin that do not shrink from $\Delta x=0.05$ to
$\Delta x=0.00625$ (§5, Fig. 2), while an unsplit conservative scheme with two one-sided interface
fluxes at the source is well-balanced; that construction is on
[well-balancing](/properties/well-balancing.md).

## Cost and parallel implementation

The source step dominates the cost of detailed chemistry, and its cost varies strongly
between cells. Bielawski et al. report sub-step counts that differ by $O(10^4)$ between cells
for stiff mechanisms (§4) and give two GPU algorithms for the operator-split reactor problem
(§5):

- a **static-cell** algorithm, in which every kernel runs over all $N_C$ cells of the rank
  (page-local) and finished cells are frozen by multiplying their source terms by an
  indicator that is 0 once the local time has reached $\Delta t$ (Alg. 3, Eqs. (13)–(14));
- an **adaptive-cell** hybrid algorithm, which every few iterations compacts the cells still
  reacting into contiguous arrays and hands the last few (100 in the tests) to the CPU
  (Alg. 4, Table 1); with suitable parameters it reduces to the static algorithm or to a
  CPU-only integration.

On 1D detonations (H$_2$/air, CH$_4$/O$_2$, RP2/O$_2$; CFL 0.2, simulation step about 6 ns,
ratio of simulation step to chemical time scale of order $10^2$ for the first two and $10^4$
for RP2) the speedup of the adaptive over the static algorithm grows with cells per GPU and
with the stiffness of the mechanism (§6.4, Figs. 11–12; values only in the figure). The text
states a "factor of 70 reduction in computational cost for the chemical system" from the
adaptive rearrangement (§4), a number no table or test of the paper reproduces. In the
production runs the reaction step takes 42.3 % of the time (rotating detonation engine,
1176 GPUs) and 33.5 % (scramjet, 300 GPUs) (Table 2).

Weng & Mével state that real-gas simulations cost 2 to 6 times the corresponding ideal-gas
runs, with no table or hardware (§4); with [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
the refined ZND computation is at least ten times faster than the uniform one at the same
finest resolution (§4.5).

## Evidence

Weng & Mével validate the split solver against reference solutions computed outside the
code: the constant-volume reactor at 800 K and 10 MPa reproduces Cantera's temperature and
species histories; 1D detonation speeds deviate from Chapman–Jouguet theory by less than
0.1 % (ideal gas) and at most 0.5 % (Redlich–Kwong); the ZND profiles agree except an
under-resolved density peak; the mean cell width of a 2D cellular detonation, $18.3$ and
$20.2$ half-reaction lengths for ideal and Noble–Abel gas, agrees with Taileb et al.'s value
of about 20 (§4.3–4.6; [shock-induced combustion](/benchmarks/shock-induced-combustion.md)).
Neither source isolates the splitting error.

## Qualifications

- No source measures the order of the split scheme or compares it with an unsplit
  (IMEX) integration, for stiff chemistry or, in Wakimura et al., for relaxation. The
  comparisons with an unsplit scheme are Yu et al.'s, which concerns a singular source and a
  stationary equilibrium, and Wilfong et al.'s, which compares admissible time steps on one
  bubble collapse, not accuracy.
- Bielawski et al. print the reactor temperature equation (Eq. (12)) with
  $\sum_kY_k/c_{v,k}$ in place of $1/(\rho\sum_kY_kc_{v,k})$ and without the factor $1/\rho$
  that the units require; they replace that equation by a Newton solve in practice, so the
  method is unaffected *(compiler check, not in the sources: the constant-volume energy
  balance gives $\mathrm dT/\mathrm dt=-\big(\rho\sum_kY_kc_{v,k}\big)^{-1}\sum_k(\epsilon_k/W_k)\Omega_k$,
  with page-local molar internal energies $\epsilon_k$ and molecular weights $W_k$)*.
- Weng & Mével cite Eq. (20) where the forward-difference rate is Eq. (14) (§4.3).

# Citations

- [Bielawski et al. (2023)](/sources/bielawski-2023.md) — §2, §3, §4, §5 (Eqs. (11)–(14), Algs. 3–4, Table 1), §6.4 (Figs. 11–12, Table 3), Table 2 (accepted manuscript).
- [Weng & Mével (2023)](/sources/weng-2023.md) — §3.1–3.2 (Eqs. (12)–(14), (20)–(21)), §4 (§§4.3–4.6).
- [Yu, Liu & Feng (2023)](/sources/yu-2023.md) — §1, §2.1, §3.1 (Eqs. (3.5)–(3.9), Thm. 3.1), §5 (Test 1, Fig. 2) (arXiv v1).
- [Başkaya et al. (2024)](/sources/baskaya-2024.md) — §3.2 (author preprint).
- [Wakimura et al. (2024)](/sources/wakimura-2024.md) — §2.4 (Eqs. (9)–(11)), §3 (Eqs. (17)–(20), (45)), §4.1, §4.4, Apps. B–E.
- [Wilfong et al. (2026)](/sources/wilfong-2026.md) — §4.1.3, §4.2.3 (Fig. 13), §7: Strang splitting with an embedded Runge–Kutta pair and infinite-rate relaxation in MFC 5.0.
- [Liu et al. (2025b)](/sources/liu-2025-b.md) — §3.3 (Eqs. (3.20)–(3.21)): stage-wise implicit damping step.
