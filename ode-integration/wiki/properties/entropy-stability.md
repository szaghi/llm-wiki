---
type: Property
title: "Entropy stability and conservation of the fully discrete scheme"
description: "A fully discrete scheme is entropy stable when a convex entropy of the solution does not increase from step to step, and entropy conservative when it stays constant; semi-discrete entropy laws are generally lost by the time integrator, and relaxation, SSP and strong-stability arguments, or symplectic methods for quadratic invariants, restore them."
status: established
aliases: [entropy conservation, entropy dissipation, fully discrete entropy stability, energy stability, invariant preservation, entropy-stable time integration]
tags: [structure-preserving, stability, runge-kutta, geometric-integration, entropy-stability, relaxation]
timestamp: 2026-10-19T23:00:00Z
---

# Entropy stability and conservation of the fully discrete scheme

Let $\eta(y)$ be a convex functional of the solution (an entropy, an energy or
a Lyapunov function), with gradient $\eta'(y)$, the **entropy variables**. A
semi-discretization $y'=f(y)$ is **entropy dissipative** if
$\langle\eta'(y),f(y)\rangle\le0$ and **entropy conservative** if
$\langle\eta'(y),f(y)\rangle=0$ for all $y$; the exact solution then satisfies
$\tfrac{\mathrm d}{\mathrm dt}\eta(y(t))\le0$, resp. $=0$
([Bencomo & Chan (2023)](/sources/bencomo-2023.md), §2.2;
[Kang & Constantinescu (2022)](/sources/kang-2022.md), §2). The **fully
discrete** scheme is

* **entropy stable** if $\eta(y_{n+1})\le\eta(y_n)$ for every step, and
* **entropy conservative** if $\eta(y_{n+1})=\eta(y_n)$,

up to boundary fluxes, which a page states when they enter (Bencomo & Chan
(2023), §2.2; Kang & Constantinescu (2022), §2, Remark 1). For an invariant of
an ODE ($\eta$ need not be convex) "entropy conservative" is invariant
preservation ([Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md), §1, Eq. (9)).
For a system of several invariants the requirement applies to each.

## Origin in conservation laws

For a hyperbolic system $\partial_tu+\operatorname{div}F(u)=0$ with convex
entropy $\eta$ and entropy flux $G$ (page-local), smooth solutions satisfy
$\partial_t\eta+\operatorname{div}G=0$ and admissible weak solutions
$\partial_t\eta+\operatorname{div}G\le0$; the total entropy
$\int_\Omega\eta\,\mathrm dx$ then changes only through the boundary flux
([Gaburro et al. (2023)](/sources/gaburro-2023.md), Eqs. (1)–(5), after Harten
and Tadmor; Kang & Constantinescu (2022), §2, after Tadmor). The time
integrator sees this through the semi-discretization: entropy-conservative and
entropy-stable fluxes give semi-discretizations with
$\langle\eta'(y),f(y)\rangle=0$ or $\le0$ up to boundary terms, e.g. the
skew-symmetric DG spectral element method for Burgers (Kang & Constantinescu
(2022), §1.2.4; [Burgers equation](/benchmarks/burgers-equation.md)). For
Burgers with $\eta=u^2/2$, entropy stability is $L^2$ stability (Remark 1).

## The square entropy and strong stability

For $\eta(y)=\tfrac12\lVert y\rVert^2$ and a linear operator, fully discrete
entropy stability is [strong stability](/properties/strong-stability.md),
$\lVert y_{n+1}\rVert\le\lVert y_n\rVert$: [Sun & Shu (2021)](/sources/sun-2021.md)
(§1) call it the discrete form of the entropy inequality for the square
entropy, and observe that a semi-discrete entropy law can be lost by the time
discretization. Which explicit methods keep it, and the superviscosity remedy,
are on that page and on
[superviscosity-stabilized RK](/methods/superviscosity-stabilized-runge-kutta.md).

## Why time integration loses it

* All Runge–Kutta methods preserve linear invariants. Only symplectic
  Runge–Kutta methods preserve all quadratic invariants, and they are
  necessarily implicit; no Runge–Kutta method preserves all polynomial
  invariants of degree $\ge3$ (Biswas & Ketcheson (2023), §1, as recalled from
  Hairer–Lubich–Wanner). Classical explicit Runge–Kutta and linear multistep
  methods cannot preserve general quadratic invariants (Kang & Constantinescu
  (2022), footnote 2). See [symplecticity](/properties/symplecticity.md).
* No Runge–Kutta method is energy preserving for every Hamiltonian system,
  although an explicit method can be for one specific system
  ([de León et al. (2025)](/sources/deleon-2025.md), §1, citing
  Celledoni et al. 2009).
* In floating-point arithmetic even an exactly conservative scheme drifts at
  round-off level, so "numerical energy conservation is effectively a matter
  of making the energy error small in any case" (de León et al.
  (2025), §1).

## How the sources restore it

| Route | Property obtained | Source |
|---|---|---|
| [Relaxation](/methods/relaxation-runge-kutta.md): rescale the update by a root $\gamma_n$ of a scalar entropy equation | conservation or dissipation for any convex $\eta$, explicit or IMEX base, $b_i\ge0$ for dissipation | Kang & Constantinescu (2022); Bencomo & Chan (2023); [Al Jahdali et al. (2022)](/sources/aljahdali-2022.md); Gaburro et al. (2023) |
| Multiple relaxation | conservation of several invariants at once | Biswas & Ketcheson (2023) |
| [SSP](/methods/strong-stability-preserving-runge-kutta.md) with the entropy as convex functional | $\eta(y_{n+1})\le\eta(y_n)$ under a step restriction, if forward Euler is entropy stable | [Gottlieb et al. (2022)](/sources/gottlieb-2022.md), Remark 3 |
| Superviscosity filter | $\lVert y_{n+1}\rVert\le\lVert y_n\rVert$ (square entropy) | Sun & Shu (2021), §5 |
| Symplectic Runge–Kutta methods (necessarily implicit) | exact quadratic invariants | Biswas & Ketcheson (2023), §1 |
| [Pseudo-energy preservation](/methods/pseudo-energy-preserving-runge-kutta.md) | energy error $O(h^{q+1})$ per step with $q>p$ | de León et al. (2025) |
| Consistent fluxes in a [semi-implicit IMEX](/methods/semi-implicit-imex-runge-kutta.md) partition | exact discrete conservation of a linear invariant (total energy) shared by explicit and implicit terms | [Southworth et al. (2024)](/sources/southworth-2024.md) |

**SSP route.** Gottlieb et al. (2022, Remark 3, Eqs. (53)–(56)) take the
discrete kinetic entropy $\sum_k\Delta x\int f_k\log f_k\,\mathrm dv$ as the
convex functional in their SSP theorem for IMEX multiderivative methods; for
the Broadwell and BGK models with first-order upwind transport this gives
discrete entropy decay, the verification being deferred to earlier work.

**Relaxation route.** The decomposition behind it is

$$\eta(y^{\gamma}_{n+1})-\eta(y_n)=\underbrace{\eta(y^{\gamma}_{n+1})-\eta(y_n)-\gamma_nh\sum_ib_i\langle\eta'(Y_i),f(Y_i)\rangle}_{=0\text{ by the choice of }\gamma_n}+\gamma_nh\sum_ib_i\langle\eta'(Y_i),f(Y_i)\rangle,$$

and the last term is $\le0$ when the semi-discretization is dissipative,
$b_i\ge0$ and $\gamma_n>0$ (Kang & Constantinescu (2022), §2.1). For
conservation laws the inner products become the cell entropy balances: Gaburro
et al. (2023, §4.1, Eqs. (21)–(22)) add Abgrall's cell-wise correction
$\alpha\int\nabla\psi\,A_0\nabla v_h$ so that each cell's central-flux entropy
production equals the numerical entropy flux, which splits the update into an
entropy-conservative part and an entropy-dissipative upwind part; relaxation
in time then matches the total entropy to that budget.

**Linear invariants across IMEX partitions.** All Runge–Kutta methods preserve linear
invariants, but Southworth et al. (2024, §4.3) point out that this is "much more
challenging" for IMEX integration when an invariant is shared by terms that the two
partitions evaluate at different stage vectors. In radiation hydrodynamics the total energy
$\rho e_t+E_r$ (page-local) is exchanged between an explicitly and an implicitly treated
equation. For their LIMEX-Euler step with finite volumes they prove local conservation if the
numerical fluxes satisfy $\hat F_E=\hat F_{\rho e_t}+\hat F_{E_r}$ (local Lax–Friedrichs with
one common viscosity coefficient does) and the diffusion and radiation-pressure work terms are
discretized identically in both equations, and global conservation up to boundary fluxes
(§4.1–4.2, Eqs. (31)–(37)). Each stage of a LIMEX-RK method is a scaled LIMEX-Euler step,
so the result extends to every such method (§4.3).

## Scope and limits of the guarantee

* **Synchronization only (multirate).** With one global relaxation parameter,
  relaxed multirate methods are entropy stable only at the synchronization
  time of the coarsest level; instability inside stages or substeps is not
  controlled, so entropy-stable fluxes are recommended over
  entropy-conservative ones for deep refinement (Kang & Constantinescu (2022),
  §3.3, §4). They state, without evidence, that relaxed IMEX methods can damp
  stage instability "because of the implicit correction step at each stage"
  (§4).
* **Partition-wise hypotheses (IMEX).** For an IMEX method with different
  explicit and implicit weights, the proof needs each part entropy stable
  separately; with equal weights only the sum (Kang & Constantinescu (2022),
  Prop. 2.1, Cor. 2.1.1).
* **Stability without a guarantee.** In industrial compressible-flow runs,
  entropy-stable DG with explicit RK was stable without relaxation; relaxation
  adds the guarantee, "indisputable robustness" in the authors' words, at a
  cost of up to about 33% more evaluations with error-based step control
  (Al Jahdali et al. (2022), §3–§4).
* **Conserving more than the semi-discretization does.** Gaburro et al. (2023)
  can drop the upwind dissipation from the relaxation target and force exact
  entropy conservation in time although the spatial scheme dissipates; their
  contact-discontinuity and "123" tests report conservation of the exact
  total entropy to machine precision (Figs. 12, 16), and shocks, which need
  dissipation, are left to future work with limiters (§6). Biswas & Ketcheson
  (2023, §6.2) enforce the KdV Whitham invariant, which the semi-discretization
  conserves only to truncation error: no existence guarantee holds, the
  invariant drift falls but not to round-off, and the long-time error grows
  roughly linearly with jitter.

## Long-time error growth

Conservative methods often grow the global error linearly instead of
quadratically on periodic or solitary-wave solutions. Biswas & Ketcheson
(2023) observe linear growth with relaxation on the rigid body, Lotka–Volterra,
the [Kepler problem](/benchmarks/kepler-problem.md) and the 1-soliton KdV
solution, in agreement with de Frutos & Sanz-Serna (as recalled), but
quadratic growth persists for the 3-soliton solution even though mass and
energy are conserved: the energies of the individual solitons change linearly
and the phase errors grow quadratically (§6.1.3, §7). Mass and energy
conservation therefore do not guarantee linear error growth for multi-soliton
solutions. de León et al. (2025, §4) report longer linear-growth
phases for pseudo-energy-preserving methods.

# Citations

- [Kang & Constantinescu (2022)](/sources/kang-2022.md) — §1.2.4, §2 (Remark 1, Eq. (9)), §2.1, §2.2 (Prop. 2.1, Cor. 2.1.1), footnote 2, §3.3, §4.
- [Bencomo & Chan (2023)](/sources/bencomo-2023.md) — §2.2 (entropy conservative and dissipative definitions, discrete targets).
- [Gaburro et al. (2023)](/sources/gaburro-2023.md) — Eqs. (1)–(5), §4.1 (Eqs. (15)–(22)), §4.2, §5 (Figs. 12, 16), §6.
- [Al Jahdali et al. (2022)](/sources/aljahdali-2022.md) — §3 (Table 4), §4.
- [Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md) — §1, Eq. (9), §6.1–6.2, §7.
- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — Remark 3 (Eqs. (53)–(56)).
- [Sun & Shu (2021)](/sources/sun-2021.md) — §1, §5.
- [de León et al. (2025)](/sources/deleon-2025.md) — §1, §4.
- [Southworth et al. (2024)](/sources/southworth-2024.md) — §4.1–4.3 (Eqs. (31)–(37)).
