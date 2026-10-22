---
type: Method
title: "Operator splitting for stiff source terms"
description: "Operator splitting advances the transport part of a reacting-flow balance law with an explicit shock-capturing step and the stiff chemical source separately, as a constant-volume reactor in each cell with the flow frozen; the bundle's two sources use Strang splitting with second-order Runge–Kutta, and a convection–primitive-update–chemistry sequence with a Cantera reactor."
status: established
aliases: [Strang splitting, fractional-step method, convection–chemistry splitting, constant-volume reactor step]
tags: [finite-volume, software, gpu, reacting-flows, stiff-source]
timestamp: 2026-10-23T16:00:00Z
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
- **Sequential steps.** Weng & Mével (§3.1) describe the blastFoam sequence: the convection
  step (MUSCL reconstruction with a limiter, an
  [HLL-family](/methods/hll-riemann-solvers.md) flux, [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)),
  then the update of the primitive variables from the conserved ones, then, for reactive
  runs, the chemistry correction. The paper does not state whether the sequence is
  symmetrized, nor its order.

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

- Neither source measures the order of the split scheme or compares it with an unsplit
  (IMEX) integration.
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
