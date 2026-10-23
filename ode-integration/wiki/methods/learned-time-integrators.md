---
type: Method
title: "Learned time integrators: neural surrogates and physics-informed Runge–Kutta networks"
description: "Learned time integrators put a trained neural network into time stepping in three ways: a learned vector field advanced by a classical Runge–Kutta method, a learned flow map that replaces a stiff solve, and a neural trial function trained on the residual of a collocation Runge–Kutta scheme; the page states what each keeps exactly, proves or only measures."
status: established
aliases: [neural network integrators, neural ODE surrogates, Lagrangian neural networks, neural operator surrogate, DeepONet surrogate, AMORE, Runge–Kutta PINN, RK-PINN, time-discrete PINN]
tags: [learned-integrators, runge-kutta, structure-preserving, stiff, verification]
timestamp: 2026-10-20T06:18:00Z
---

# Learned time integrators: neural surrogates and physics-informed Runge–Kutta networks

A **learned time integrator** puts a trained neural network into the time
integration of $y'=f(t,y)$ or of a method-of-lines semi-discretization. The three
ingested sources use the network in three different places, and the time-integration
content differs accordingly:

1. **learned vector field, classical stepper.** A network defines the right-hand
   side, and a standard Runge–Kutta method advances it
   ([Müller 2023](/sources/muller-2023.md));
2. **learned flow map.** A network maps an initial state to the trajectory over a
   fixed horizon and replaces a stiff implicit solve
   ([Nath et al. 2026](/sources/nath-2026.md));
3. **time-discrete training loss.** A network is the trial function, and its loss is
   the squared residual of the pointwise form of a collocation Runge–Kutta or Galerkin
   time-stepping scheme ([Akrivis, Makridakis & Smaragdakis 2025](/sources/akrivis-2025.md)).

The bundle's scope covers these methods as time integrators: what the time scheme
contributes, what is exact, and what is proved. The machine-learning content
(architectures, loss weighting, training schedules) is summarized only where it
decides those questions. Page-local symbols: $q$, $\dot q$ positions and velocities of a
mechanical system (not the stage order); $\mathcal L_\theta$ a network Lagrangian with
weights $\theta$; $u$ the solution of a linear parabolic problem, $\mathcal A$ its operator
and $g$ its forcing.

## Learned vector field with exact invariants

Müller (2023) represents the Lagrangian of a mechanical system by a dense network
$\mathcal L_\theta(q,\dot q)$, after the Lagrangian neural networks of Cranmer et al.
as recalled there, obtains the acceleration from the Euler–Lagrange equations by
automatic differentiation and a Hessian solve,

$$\ddot q=\Bigl(\frac{\partial^2\mathcal L_\theta}{\partial\dot q\,\partial\dot q}\Bigr)^{-1}\Bigl(\frac{\partial\mathcal L_\theta}{\partial q}-\frac{\partial^2\mathcal L_\theta}{\partial q\,\partial\dot q}\,\dot q\Bigr)$$

(§2.2, Eqs. (8)–(10)), and integrates this second-order ODE with classical RK4 at
$h=10^{-2}$ (§3). The contribution is a **symmetry-enforcing input layer** that maps
$(q,\dot q)$ to scalar invariants of a continuous group (rotations $SO(D)$,
translations, or both) before the dense layers (Eq. (11), Table 1). The network
Lagrangian is then invariant under the group for every value of the weights, and
Noether's theorem, recalled in §2.1 (Eqs. (1)–(2)), makes the corresponding momenta
of the **learned** dynamics exact first integrals, "independent of the weights of the
neural network" (§2.3.1). Equivariance of a learned force alone does not give a
conserved quantity (§1.1.5).

**What is exact.** The conservation is a property of the continuous learned ODE. The
RK4 map that advances it does not conserve the network momenta in general: the author
writes that the momentum drift "would be zero in exact arithmetic and for an exact
time integrator" (§3.1.2). The network momenta are nonlinear functions of
$(q,\dot q)$, and RK4 is neither symplectic nor quadratic-invariant preserving
*(compiler remark, not in the source; see [symplecticity](/properties/symplecticity.md))*.
The measured drift of the network momenta, about $10^{-5}$ or below in relative norm,
is attributed by the author to single-precision rounding (§3.1.1–3.1.2); the paper
has no step-size study, so the RK4 truncation part of the drift is not separated.

**Measurements** (synthetic data from RK4 at $h=10^{-2}$ with Gaussian noise
$10^{-3}$; two hidden layers of 128 units; single precision; §3):

| Test | Unconstrained network | Symmetry-enforcing network |
|---|---|---|
| 3D [Kepler problem](/benchmarks/kepler-problem.md), $e=0.8$, $T=128$ | true angular momentum error grows to about 1 by $t\approx50$, then the orbit blows up | true angular momentum error below $10^{-3}$; perturbation of $10^{-3}$ grows to under 0.1 instead of over 1 by $t\approx55$ (Figs. 3–5) |
| relativistic particle, Schwarzschild metric, $T=1000$ | stays bounded, true angular momentum off by about 10 % | true angular momentum error below $10^{-3}$ (Figs. 6–8) |
| two particles in $D=4$, double-well potential, $T=8$ | true momenta off by 10–100 % | rotation and translation layer: within 1 %, no upward trend (Figs. 9–11) |

The author compares the exactly conserved network momentum to the shadow Hamiltonian
of a symplectic integrator, which explains near-conservation of the true quantity
(§2.3.1, §3.1.1). The comparison is an analogy, not a theorem: the shadow Hamiltonian
of [backward error analysis](/methods/backward-error-analysis.md) is an invariant of
the modified equation of the **discrete** map, whereas the network momentum is an
invariant of a **different continuous model** fitted to data. Müller also notes that
the Hessian solve costs $\mathcal O((Nd)^3)$ for $N$ particles in $d$ dimensions and
that the number of invariant features grows like $N^2$ (§4), and recalls that LSTM
next-state predictors "can be seen as an extension of classical linear multistep
methods" and that Hamiltonian networks were first integrated with non-symplectic RK4
and later with Störmer–Verlet (§1.1).

## Learned flow map for stiff chemistry

Nath et al. (2026) train a DeepONet to replace the stiff implicit integration of
zero-dimensional, adiabatic, constant-pressure gas-phase kinetics, the chemistry
sub-step of an [operator-split](/methods/operator-splitting.md) reacting-flow solver
(§1–2, Eq. (1)). The operator maps the thermochemical state at the start of a segment
to the trajectory on 101 uniformly spaced points, $10^{-7}$ s apart; that is, it is a
learned flow map with output on a fixed grid. Longer horizons are reached by
**autoregressive rollout**, feeding the end state back as the next initial value,
which is legitimate because the system is autonomous (§3.6). The training data come
from Cantera's VODE [BDF](/methods/backward-differentiation-formula.md) solver at
$\mathrm{rtol}=10^{-8}$, $\mathrm{atol}=10^{-12}$ with an analytic Jacobian (§4).

The time-integration-relevant devices are the treatment of the linear invariant and of
positivity. Mass conservation, $\sum_iy_i=1$ for the mass fractions, is imposed three
ways: a penalty (Eqs. (10)–(11)), an invertible map of the $n$ mass fractions to $n-1$
coordinates in $[0,1]$ that makes the sum exactly one (§3.5, App. B.3), and a softmax
output that gives positive mass fractions with unit sum together (§4.5, Eqs.
(33)–(35)). Compare the exact linear-invariant and positivity properties of
[modified Patankar methods](/methods/modified-patankar-methods.md) on
[production–destruction systems](/definitions/production-destruction-system.md),
which come from the time scheme rather than the output parametrization.

**Measurements.** On a syngas mechanism (11 species, 21 reactions) the mean relative
$L^2$ test error over 101-point segments falls from 0.154 % (baseline DeepONet) to
0.041 % (two-step training, per-sample adaptive weights) and 0.034–0.037 % with the
exact mass map (Tables 2, 3, C.4). In autoregressive rollout over $10^{-3}$ s the mean
test error is 0.51–0.64 %, the 90th-percentile per-variable error stays below 5 %, and
per-variable maxima reach 43.9 % and 52.8 % for HCO, concentrated near ignition
(Table 6, Table C.6, Fig. 11). GRI-Mech 3.0 with 24 retained states gives
0.075–0.084 % (§5.1). Training costs 10–26 GPU-hours per model (Table D.1).

**What is not shown.** The authors state that "online (inference) costs are much
smaller than implicit solvers" (§1), but they report no inference timing and no
comparison with the BDF reference. The surrogate has a fixed output spacing and
horizon, fixed pressure, no error estimate or control, and no stability guarantee
under rollout; the properties a stiff integrator provides through
[step-size control](/methods/step-size-control.md) and
[A- and L-stability](/properties/a-stability.md) are not claimed. Nath et al. also
criticize an earlier syngas DeepONet of Goswami et al. (2024), a different work from
the ingested [Goswami et al. (2023)](/sources/goswami-2023.md): according to Nath et
al., that model predicts only at four coarse output times and so likely misses the
stiff peaks, and its "auto-regressive" error was not computed autoregressively, which
those authors are said to have confirmed (§1). This is Nath et al.'s account.

## Runge–Kutta physics-informed networks

Akrivis et al. (2025) do not learn a time stepper; they use a Runge–Kutta scheme to
build the training loss of a physics-informed network (PINN) for the linear parabolic
problem $u'+\mathcal Au=g$ with $\mathcal A=-L$ coercive and self-adjoint (page-local, as on
[discrete maximal regularity](/results/discrete-maximal-regularity.md); the source writes $L$
or $A$ for the operator, $f$ for the forcing and $q$ for the stage count). The network $v$ is
interpolated in time at $s+1$ auxiliary nodes per step into a continuous piecewise polynomial
$\hat v$ of degree $s$, and the loss is

$$G_{\mathrm{RK}}(v)=\int_0^T\bigl\lVert\hat v_t+I_{s-1}\mathcal A\hat v-I_{s-1}g\bigr\rVert^2_{L^2(\Omega)}\,dt+\lvert\hat v(0)-u_0\rvert^2_{H^1(\Omega)},$$

with $I_{s-1}$ the piecewise interpolation at the collocation nodes $c_i$ (§2.4.2,
Eqs. (25)–(27); $\hat v$, $I_{s-1}$ page-local). The integrand is the residual of the
**pointwise form** $\hat U'+I_{s-1}\mathcal A\hat U=I_{s-1}g$ of an $s$-stage collocation
[Runge–Kutta method](/methods/fully-implicit-runge-kutta.md) (Gauss, Radau IIA,
Lobatto IIIA), so the loss vanishes exactly on that method's collocation polynomial. A
generalized loss with abstract projections (Eq. (28)) also covers continuous and
discontinuous Galerkin time stepping. Spatial integrals are still sampled
(quasi-Monte Carlo, Sobol points). The time-discrete PINN with the backward-Euler
residual, recalled from Gkanis, Gazoulis & Makridakis (§2.3, Eqs. (14)–(19)), is
stable and convergent, while the explicit-Euler analogue is not without a CFL
condition; explicit RK losses are deliberately not computed.

**Proved** (§3): stability of the discrete loss in the liminf–limsup
($\Gamma$-convergence) sense (Prop. 2, Lemmas 3–4) and convergence of the discrete
minimizers, $\hat u_\ell\to u$ in $L^2(0,T;H^1(\Omega))$ as the time partition and the
network spaces are refined (Thm. 7), assuming the networks approximate smooth functions.
The stability step rests on a **discrete maximal $L^2$ regularity** estimate of the
underlying time scheme, which §4 proves for variable steps; see
[discrete maximal regularity](/results/discrete-maximal-regularity.md).

**Shown** (§5, three-stage Gauss, Lobatto IIIA and Radau IIA against uniform time
sampling with four times as many time points): smaller misfit and better conservation
of total heat on a 2D [heat equation](/benchmarks/heat-equation.md) with Neumann
boundaries (Figs. 1–4). With discontinuous initial data Gauss and Lobatto IIIA
oscillate near $t=0$ while Radau IIA smooths, as the stability functions predict
($\lvert R(\infty)\rvert=1$ against $R(\infty)=0$); on a 2D wave equation Gauss and Lobatto
conserve energy best and uniform sampling is the most diffusive (Figs. 5–7). The
loss inherits the qualitative behaviour of the time scheme it is built from. All
numerical evidence is graphical, without convergence rates. The convergence theory for
hyperbolic problems "remains to be developed" (§1). A related residual-loss construction
for multiscale kinetic equations, the asymptotic-preserving neural network whose loss is
built on the micro–macro system rather than on the kinetic equation, is recorded on
[micro–macro decomposition](/methods/micro-macro-decomposition.md) ([Jin 2022](/sources/jin-2022.md), §5.7).

## Learned and optimized coarse propagators

[Jin et al. (2025)](/sources/jin-2025.md) place their optimized rational coarse
propagator for [Parareal](/methods/parareal.md) within "learning/optimizing numerical
algorithms" and cite neural-network coarse propagators, but their optimization uses no
training data (§1). The bundle has no ingested source on neural coarse propagators.

## Comparison

| | Müller (2023) | Nath et al. (2026) | Akrivis et al. (2025) |
|---|---|---|---|
| What is learned | right-hand side (via a Lagrangian) | flow map over a fixed horizon | the solution itself, as a trial function |
| Time scheme | RK4 advances the learned ODE | BDF generates training data; none at inference | collocation RK or Galerkin residual defines the loss |
| Exact by construction | Noether momenta of the continuous learned ODE | unit sum of mass fractions; positivity (softmax variant) | none; the loss is zero on the collocation solution |
| Proved | Noether's theorem (recalled) | nothing about the time integration | stability and convergence for linear parabolic problems |
| Evidence on cost | none | training cost only | none |

## Qualifications

- **Bundle fit.** All three sources are primarily scientific machine learning.
  Müller's time integration is a black-box RK4, and Nath et al.'s is a reference
  BDF solver plus a learned flow map; only Akrivis et al. contribute time-integration
  theory (§4 of their paper), which stands independently of the network.
- **"Exact" in titles.** Müller's "exact conservation laws for neural network
  integrators" holds for the continuous learned dynamics, not for the integrator's
  steps (see above).
- **Speed claims.** Neither Müller nor Nath et al. measures the cost of a learned step
  against a classical integrator; Nath et al.'s cheaper inference is a stated
  premise. Their $\mathcal O(n^3)$ cost of implicit chemistry for $n$ species is the
  dense direct-solver count (§1).
- **Printed slips.** Müller (2023) twice attributes the Lagrangian network to the
  Hamiltonian-network paper of Greydanus et al. (§2.2), where his §1.2 and §4 cite
  Cranmer et al., and prints $(\dot x^{(1)})^2$ twice in the two-particle Lagrangian
  (Eq. (22); Eq. (33) has the correct $m_2\dot x^{(2)}$). Nath et al. (2026) swap the
  H and HO$_2$ column labels of Table C.5 against Table 4. Akrivis et al. (2025) print a
  minus sign in the computable residual (Eq. (118)) where the definition (Eqs.
  (116)–(117)) has a plus, and refer Theorem 7 to the backward-Euler functional (14)
  instead of the generalized one (28).

# Citations

- [Müller (2023)](/sources/muller-2023.md) — §1.1, §2.1 (Eqs. 1–2), §2.2 (Eqs. 8–11), §2.3 (Eqs. 14, 21, 32, Table 1), §3.1 (Figs. 3–11), §4.
- [Nath et al. (2026)](/sources/nath-2026.md) — §1, §2 (Eqs. 1–3), §3.2–3.6, §4 (Tables 2–6), §4.4–4.5 (Eqs. 33–35), §5.1, App. B.3, Tables C.4, C.6, D.1.
- [Akrivis, Makridakis & Smaragdakis (2025)](/sources/akrivis-2025.md) — §1, §2.3–2.4 (Eqs. 14–29), §3 (Prop. 2, Lemmas 3–4, Thm. 7), §5 (Figs. 1–7).
- [Jin et al. (2025)](/sources/jin-2025.md) — §1 (learned and optimized coarse propagators, in passing).
- [Jin (2022)](/sources/jin-2022.md) — §5.7 (asymptotic-preserving neural networks, cross-reference only).
