---
type: Software
title: "Irksome"
description: "Irksome, the Firedrake library that turns a UFL semidiscrete variational form and a Butcher tableau into the coupled Runge–Kutta stage equations, with collocation and DIRK tableaux, stage-derivative, stage-value and transformed formulations, ODE- and DAE-type stage boundary conditions, PETSc-composable and Rana-type stage solvers, and the measured cost of fully implicit methods."
status: established
aliases: [irksome, Irksome TimeStepper, bc_method, stage_type]
tags: [software, implicit, runge-kutta, implicit-stage-solvers, structure-preserving]
timestamp: 2026-10-20T14:00:00Z
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
to code and too expensive to solve (§1). [Kirby & MacLachlan (2025)](/sources/kirby-2025.md)
describe four later extensions: DAE-type stage boundary conditions, alternative stage
formulations, a dedicated DIRK path, and generic Rana-type stage preconditioners (§1).

## What it provides

**Interfaces.** `getForm` takes the UFL form, a tableau, time and
time-step constants and the solution coefficient, and returns the stage
form and stage boundary conditions; `TimeStepper` wraps it into a time
loop (Farrell et al. 2021, §3). In the later version `TimeStepper` is a
factory function configured by keywords, e.g.
`TimeStepper(F, RadauIIA(2), t, dt, up, bcs=bcs)` with options `stage_type`,
`splitting` and `bc_method` (Kirby & MacLachlan 2025, §2, Fig. 1). Example: the heat equation is
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

**Stage formulations** (Kirby & MacLachlan 2025, §2.2–2.3). Besides the stage
derivatives (`stage_type='deriv'`, the default), Irksome offers stage values
$Y_i$ (`stage_type='value'`), whose update needs one mass-matrix solve, skipped
automatically for stiffly accurate tableaux, and a DIRK path (`stage_type='dirk'`)
that builds one single-stage problem and reuses it for every stage. The keyword
`splitting` chooses the unknowns of the stage-derivative form: `AI` (the default,
$k$ itself) or `IA`, Butcher's transformed variables $w=(A\otimes I)k$, which make the
nonlinear part of the Jacobian block diagonal; `IA` checks that $A$ is invertible.
Details on [solving the stage equations](/methods/implicit-stage-solvers.md).

**Stage boundary conditions.** Two treatments of strong Dirichlet data
$u=g(t,\cdot)$ have been Irksome's default in turn; the authors replaced the first
by the second, so this is a documented change of default, not a disagreement:

- **ODE-type** (Farrell et al. 2021, §2.2.1, Eq. 18): the stage derivatives take
  the time derivative of the data, $k_i=\partial_tg(t_n+c_ih,\cdot)$, since $k_i$
  approximates $u_t$.
- **DAE-type** (Kirby & MacLachlan 2025, §2.1, Eqs. (2.15)–(2.17)): the data are
  imposed on the stage values, $Y_i=g(t_n+c_ih,\cdot)$ on the boundary, i.e.
  $\sum_ja_{ij}k_j=(g(t_n+c_ih,\cdot)-u_n)/h$, solvable for the boundary values of the
  $k_i$ when $A$ is invertible. It is now the default (`bc_method='DAE'`); the old
  treatment remains as `bc_method='ODE'`.

Kirby & MacLachlan state that the ODE-type heuristic "has proven to have some inherent
weaknesses", that "many practical cases show little difference", and that the DAE type
is "more robust and supported by standard RK convergence theory" (§2, §2.1). Their
example has incompatible data: the 1D heat equation with $u(0,x)=0$ and boundary values
1, P1 elements on 10 intervals, three-stage Lobatto IIIC, $h=0.05$; the ODE type sees a
zero boundary derivative and stays at zero, the DAE type approaches $u\equiv1$ (Fig. 2).
Weakly imposed data need only evaluation at stage times in either version. The
comparison is on [boundary conditions for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md).

**Tableaux.** Gauss–Legendre (implicit midpoint included), Lobatto IIIA
(Crank–Nicolson included) and Radau IIA (backward Euler included) of
arbitrary order, with nodes from FIAT quadrature and $A$, $b$ by
numerical integration; Lobatto IIIC of general order; forward Euler, an
SSP method, explicit midpoint and trapezoid, classical RK4, and Alexander's
L-stable DIRKs (§3.2). Kirby & MacLachlan (2025, §2.3, App. A) add DIRKs of high
[weak stage order](/definitions/weak-stage-order.md), WSODIRK433 and WSODIRK744
($s$ stages, order $p$, weak stage order $q_{\mathrm w}$ in the name WSODIRK$spq_{\mathrm w}$),
and print the tableaux of Radau IIA with 1–3 stages, Alexander's three-stage DIRK and
WSODIRK433; see [DIRK methods](/methods/diagonally-implicit-runge-kutta.md). The stability properties recalled for these
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

- **Monolithic multigrid with stage-coupled patches.**
  [Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md) use Irksome to generate the
  coupled stage equations of Gauss, Radau IIA and Lobatto IIIC methods for
  incompressible Stokes, Navier–Stokes and visco-resistive MHD, and solve them with
  Newton (Eisenstat–Walker), FGMRES and a geometric multigrid V-cycle whose additive Vanka
  relaxation, built with PETSc's PCPATCH, puts all stage copies of a vertex patch into one
  small saddle-point solve; interpolation acts stage by stage, $I_s\otimes P$ (§4,
  §4.3). The largest runs reach 46,566,816 unknowns on 640 cores (§5.2). Details on
  [solving the stage equations](/methods/implicit-stage-solvers.md).
- **DAE stage form.** For the index-2 Stokes system Abu-Labdeh et al. advance the
  pressure, like the velocity, with stage derivatives and impose the incompressibility
  constraint on every stage value (§3.1); see
  [differential-algebraic equations](/definitions/differential-algebraic-equation.md).

- **Rana-type and block preconditioners.** Kirby & MacLachlan (2025, §3) add block
  Jacobi and block Gauss–Seidel from the additive split of $A$, and a preconditioner
  that replaces $A$ by the lower-triangular product $\tilde L\tilde D$ of its $LDU$
  factorization; the latter is implemented as a `firedrake.AuxiliaryOperatorPC` that
  rebuilds the stage form with the modified matrix, so it applies to nonlinear problems
  (PETSc option `'pc_python_type': 'irksome.RanaLD'`). Its GMRES counts stay nearly
  independent of $s$, while block Jacobi and Gauss–Seidel counts grow (§4.1, Fig. 5). The
  eigenvalue-based preconditioners of Southworth et al. and the SVD-based ones of Leveque
  et al. are not supported (§3.1). Numbers are on
  [implicit stage solvers](/methods/implicit-stage-solvers.md).

[Munch et al. (2024)](/sources/munch-2024.md) (§7) name Irksome as a possible code
generator for the batched stage operations of their stage-parallel deal.II
implementation; it is not used there.

A different route to the same coupled system — real Schur decomposition
of $A^{-1}$ with block-triangular preconditioning, implemented in MFEM
(the IRKIntegration code) — is developed by [Southworth et al. (2022)](/sources/southworth-2022.md),
who cite Irksome as concurrent work (Remark 2); both approaches are
compared on [implicit stage solvers](/methods/implicit-stage-solvers.md).

## Measured behaviour

Numbers are from Farrell et al. (2021) (arXiv v1 numbering; no hardware
stated) unless attributed to Abu-Labdeh et al. (2023) (arXiv v2 numbering;
Niagara cluster, Intel Skylake nodes).

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
- **Same benchmark, monolithic multigrid** (Abu-Labdeh et al. 2023, §5.2, Tables 5–6):
  Taylor–Hood elements, $h=1/400$, two- and three-stage Radau IIA and Lobatto IIIC give
  maximum drag 2.95 and lift 0.48 at every refinement level, with 1.35–2.70 Newton and
  1.61–8.19 linear iterations per step and 0.03–0.19 min per step on up to 640 cores;
  three-stage Gauss gives "highly oscillatory" drag and lift. See
  [flow past a cylinder](/benchmarks/flow-past-cylinder.md).
- **Stokes, manufactured solution** (Abu-Labdeh et al. 2023, §5.1, Tables 1–4): linear
  iterations per step stay between 8.70 and 25.97 from 1.1M to 19M unknowns per stage, and
  two-stage Radau IIA reaches the accuracy of a three-stage L-stable DIRK in about 60 %
  of the wall time on one eighth of the cores.

- **Order reduction, later version** (Kirby & MacLachlan 2025, §4.1, Figs. 3–4; 2D heat
  equation with serendipity elements, $h=M/N$, $M=1,4,8$): backward Euler is suboptimal in
  $L^2$ for every $M$, Alexander's DIRK at $M=8$, and with cubics two-stage Radau IIA (order
  3, stage order 2) loses $L^2$ accuracy at large steps, while three- and four-stage Radau
  IIA and WSODIRK433 stay spatial-error dominated. See
  [order reduction](/definitions/order-reduction.md).
- **Navier–Stokes as an index-2 DAE** (Kirby & MacLachlan 2025, §2, §4.2, Figs. 9–11):
  velocity and pressure both carry stage derivatives, incompressibility is imposed on every
  stage, and an initial pressure is required (Eqs. (2.11)–(2.14)). On flow past a cylinder
  with Mardal–Tai–Winther elements over $t\in[0,8]$, the reference is five-stage Radau IIA
  at the finest step on the same fixed mesh (maximum drag about 2.89, lift about 0.47);
  three- and four-stage Radau IIA give the best accuracy per run time, WSODIRK744 is
  accurate but "far more expensive", and one-stage Radau IIA (backward Euler) barely
  converges. See [flow past a cylinder](/benchmarks/flow-past-cylinder.md) and
  [differential-algebraic equations](/definitions/differential-algebraic-equation.md).
- **Cahn–Hilliard** (Kirby & MacLachlan 2025, §4.3, Figs. 12–15; $C^1$ Bell elements): the
  free energy decreases monotonically for every method; three- and four-stage Radau IIA have
  the lowest final-energy error, and Radau IIA costs slightly more than a DIRK with the same
  stage count. See [Cahn–Hilliard equation](/benchmarks/cahn-hilliard-equation.md).
- **Overall.** Kirby & MacLachlan conclude that fully implicit methods with Rana-type or
  monolithic multigrid preconditioning are competitive with DIRKs in run time and more
  accurate (§1, §5). Adaptive time stepping for implicit Runge–Kutta DAEs and IMEX support
  are named as future work (§5).

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
- Abu-Labdeh et al. (2023, §5) also state that Gauss, Radau IIA and Lobatto IIIC all have
  stage order equal to the number of stages; for Lobatto IIIC the standard value is $s-1$
  (see [fully implicit Runge–Kutta methods](/methods/fully-implicit-runge-kutta.md)).
  Their solver tolerances and Chebyshev smoothing intervals are hand-tuned, and no
  convergence theory for the stage-coupled smoother is given (§5).

- Kirby & MacLachlan (2025, §4.2, p. 17:19) write that DIRKs "are only guaranteed to have
  stage order one or two". As a statement about classical stage order this is an upper
  bound, not a guarantee: at most 1 with invertible $A$ and at most 2 with an explicit first
  stage; their own WSODIRK433 reaches weak stage order 3 and matched three-stage Radau IIA on
  the heat equation (see [stage order](/definitions/stage-order.md)). The same paper states
  that for index-2 DAEs the stage order, not the global order, governs accuracy (§2), yet
  observes that the schemes "generally exceed the stage-order bound" on drag and lift,
  reaching their formal order (§4.2).
- Kirby & MacLachlan (2025) print the variational update without the factor $h$
  (Eq. (2.8)), the summation index of the stage value as $i$ instead of $j$ below
  Eq. (2.15), and the last coefficient of Alexander's DIRK garbled (App. A); the intended
  $\tfrac32\gamma^2-5\gamma+\tfrac54$ is the one tabulated on
  [DIRK methods](/methods/diagonally-implicit-runge-kutta.md). Their reference drag and
  lift come from a fixed coarse mesh and are not benchmark reference values.

# Citations

- [Farrell et al. (2021)](/sources/farrell-2021.md) — §1–§4; Eqs. 6–9, 18, 31–33; Listings 1–3; Figs. 1–3, 5; Tables 1–2 (arXiv v1).
- [Southworth et al. (2022)](/sources/southworth-2022.md) — §1.2 (IRKIntegration in MFEM), Remark 2 (Irksome as concurrent work).
- [Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md) — §3.1, §4, §4.3 (Irksome with PETSc/PCPATCH monolithic multigrid); §5.1–5.2, Tables 1–6.
- [Munch et al. (2024)](/sources/munch-2024.md) — §7 (Irksome as possible code generator for batched stage operations).
- [Kirby & MacLachlan (2025)](/sources/kirby-2025.md) — §1; §2 (Eqs. (2.1)–(2.14), Fig. 1); §2.1 (Eqs. (2.15)–(2.17), Fig. 2); §2.2–2.3 (Eqs. (2.18)–(2.21)); §3.1–3.2 (Eqs. (3.3)–(3.8)); §4.1–4.3 (Figs. 3–15); §5; App. A.
