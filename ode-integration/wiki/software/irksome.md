---
type: Software
title: "Irksome"
description: "Irksome, the Firedrake library that turns a UFL semidiscrete variational form and a Butcher tableau into the coupled Runge–Kutta stage equations, with arbitrary-order collocation tableaux, PETSc-composable stage solvers and the measured cost and conservation behaviour of fully implicit methods."
status: established
aliases: [irksome]
tags: [software, implicit, runge-kutta, implicit-stage-solvers, structure-preserving]
timestamp: 2026-10-19T00:00:00Z
---

# Irksome

Irksome is a Python library, part of the Firedrake finite-element project,
that generates fully discrete Runge–Kutta methods from a *semidiscrete*
variational form ([Farrell et al. (2021)](/sources/farrell-2021.md)). The
user writes the form $G(t,u,u_t;v)=0$ in UFL, using an added time
derivative operator `Dt`, and supplies a Butcher tableau; Irksome
symbolically produces the UFL of the coupled $s$-stage system and its
stage boundary conditions, which Firedrake assembles and PETSc solves
(§3). Its stated design principle is "separating mechanism from policy":
it provides methods without prescribing which to use (§1). The aim is to
make [fully implicit Runge–Kutta methods](/methods/fully-implicit-runge-kutta.md)
practical in finite-element codes, where they had been avoided as laborious
to code and too expensive to solve (§1).

## What it provides

**Interfaces.** `getForm` takes the UFL form, a tableau, time and
time-step constants and the solution coefficient, and returns the stage
form and stage boundary conditions; `TimeStepper` wraps it into a time
loop (Farrell et al. 2021, §3). Example: the heat equation is
`inner(Dt(u), v)*dx + inner(grad(u), grad(v))*dx` (§3.1).

**Stage form by substitution.** Irksome works with stage derivatives
$k_i\approx u_t(t_n+c_ih)$. In the semidiscrete form it substitutes, for
each stage $i$, $k_i$ for $u_t$, $u_n+h\sum_ja_{ij}k_j$ for $u$, a stage
test function $v_i$ for $v$ and $t_n+c_ih$ for $t$, and sums over stages
(§2.2.1, §3.1). Translated to stage values, the unknowns are
$Y_i=u_n+h\sum_ja_{ij}k_j$ and $u_{n+1}=u_n+h\sum_ib_ik_i$. The
substitution covers ODEs, semi-explicit and fully implicit DAEs and
Sobolev-type equations (§2.1, Eqs. 6–9). For the backward-Euler tableau
the stage form coincides with the usual backward-Euler variational form
(§2.2.1).

**Stage boundary conditions.** Strong Dirichlet data $u=g(t,\cdot)$ on
the boundary become $k_i=\partial_tg(t_n+c_ih,\cdot)$, since $k_i$
approximates $u_t$; weakly imposed data need only evaluation at stage
times (§2.2.1, Eq. 18).

**Tableaux.** Gauss–Legendre (implicit midpoint included), Lobatto IIIA
(Crank–Nicolson included) and Radau IIA (backward Euler included) of
arbitrary order, with nodes from FIAT quadrature and $A$, $b$ by
numerical integration; Lobatto IIIC of general order; forward Euler, an
SSP method, explicit midpoint and trapezoid, classical RK4, and Alexander's
L-stable DIRKs (§3.2). The stability properties recalled for these
families are on [fully implicit Runge–Kutta methods](/methods/fully-implicit-runge-kutta.md)
and [A-stability](/properties/a-stability.md).

**Limitation.** In the version described, `Dt` may act only on unknown
fields, not on expressions: one writes `2*t*u + t**2*Dt(u)` rather than
`Dt(t**2*u)` (§3.1).

## Stage solvers

Keeping the symbolic structure, rather than a black-box residual, is what
lets Irksome use Firedrake/PETSc's composable solvers: monolithic
multigrid, field-split and Schur-complement preconditioners, matrix-free
application (Farrell et al. 2021, §3). For the heat equation with mass
matrix $M$ and stiffness matrix $K$ (page-local), the stage system is
$(I\otimes M+hA\otimes K)\mathbf k=\mathbf f$ (§2.3, Eq. 31).

- **Block-diagonal preconditioning.** Following Mardal–Nilssen–Staff,
  the preconditioner $\mathrm{diag}(M+a_{ii}hK)$ is applied with one
  algebraic-multigrid (`gamg`) V-cycle per block inside GMRES, via PETSc
  additive field split; each block is a backward-Euler-like solve (§2.3,
  Eq. 32, Listing 2).
- **DIRKs need no special code.** For lower-triangular $A$ the stage
  system is block lower triangular, and a multiplicative field split with
  exact block solves is block forward substitution, exact in one
  iteration (§2.3, Eq. 33, §4.3, Listing 3).

A different route to the same coupled system — real Schur decomposition
of $A^{-1}$ with block-triangular preconditioning, implemented in MFEM
(the IRKIntegration code) — is developed by [Southworth et al. (2022)](/sources/southworth-2022.md),
who cite Irksome as concurrent work (Remark 2); both approaches are
compared on [implicit stage solvers](/methods/implicit-stage-solvers.md).

## Measured behaviour

All numbers are from Farrell et al. (2021) (arXiv v1 numbering); no
hardware is stated.

- **Order reduction.** On a manufactured heat solution (cubic
  serendipity elements, $N=8$–$128$, $h\in\{1/N,4/N,16/N\}$), two-stage
  Gauss–Legendre falls from order 4 to "stiff order" 2 except at very
  small $h$, while three-stage Radau IIA keeps full accuracy in both
  norms; the same holds in a mixed RT$_3\times$DG$_3$ formulation (§4.1,
  Figs. 1–2). See [order reduction](/definitions/order-reduction.md).
- **Solver cost.** With block-diagonal AMG preconditioning on a
  $128\times128$ $Q^2$ mesh, two- and three-stage Radau IIA cost about 3×
  and 5× a backward-Euler solve (solver time ≈ 9, 24, 46 and GMRES
  iterations per step ≈ 4, 11, 17.5 for $s=1,2,3$, read from Fig. 3).
  The authors compare this with Richardson step doubling, which needs 3
  backward-Euler solves for order 2 and 7 for order 3 (§4.2).
- **Energy.** On a mixed wave equation whose semidiscretization conserves
  energy exactly, Gauss–Legendre with one and two stages keep
  $E(10)/E(0)=1$ for $h=0.1,0.5,1.0$, while Radau IIA and Lobatto IIIC
  damp strongly (e.g. two-stage Lobatto IIIC: $0.379$, $9.75\times10^{-18}$,
  $1.17\times10^{-20}$); a two-stage symplectic DIRK solved by
  multiplicative field split matches Gauss–Legendre (§4.3, Table 1). See
  [symplecticity](/properties/symplecticity.md).
- **Invariants.** For the BBM solitary wave, one- and two-stage
  Gauss–Legendre conserve the linear and quadratic invariants to
  $O(10^{-15})$; the cubic invariant drifts to $0.9948969$ and $0.9999990$
  of its initial value (§4.4.2, Table 2).
- **Navier–Stokes.** Flow past a cylinder at Re 100 with Scott–Vogelius
  $P^4/P^3_{\mathrm{disc}}$ (≈382k dofs) and two-stage Radau IIA at
  $h=0.00125$ matches reference drag and lift computed with ≈667k dofs and
  Crank–Nicolson at half the step (§4.4.1, Fig. 5).

## Qualifications

- The cost ratios (3×, 5×) are from one mesh and one step size, without
  timing units or hardware; Farrell et al. (2021) do not claim they
  generalize (§4.2).
- Farrell et al. (2021) state that three-stage Lobatto IIIC has stage
  order 3 (§4.1); as usually classified, $s$-stage Lobatto IIIC satisfies
  $C(s-1)$, i.e. stage order 2 for $s=3$. See
  [stage order](/definitions/stage-order.md).
- The paper prints the update without the factor $h$ (Eq. 15) and the
  diffusion term of the heat equation with the wrong sign (Eq. 10); its
  own Eqs. 3, 11 and 14 have the correct forms.
- "Half as many degrees of freedom" in the cylinder test is 382k against
  667k, a factor of about 0.57.

# Citations

- [Farrell et al. (2021)](/sources/farrell-2021.md) — §1–§4; Eqs. 6–9, 18, 31–33; Listings 1–3; Figs. 1–3, 5; Tables 1–2 (arXiv v1).
- [Southworth et al. (2022)](/sources/southworth-2022.md) — §1.2 (IRKIntegration in MFEM), Remark 2 (Irksome as concurrent work).
