---
type: Method
title: "Solving the stage equations of implicit Runge–Kutta methods"
description: "How the nonlinear and linear systems of implicit Runge–Kutta stages are solved: Newton and simplified Newton iterations, predictors, tolerances and Jacobian reuse, real-Schur block preconditioning of fully implicit methods, block preconditioners in finite-element codes, multirate Newton structure, and solver software."
status: established
aliases: [stage solver, Newton iteration for implicit stages, simplified Newton, modified Newton, IRK preconditioning, stage-parallel preconditioner, implicit predictors]
tags: [implicit, linear-algebra, stiff, runge-kutta, software]
timestamp: 2026-10-19T00:00:00Z
---

# Solving the stage equations of implicit Runge–Kutta methods

An implicit [Runge–Kutta method](/definitions/runge-kutta-method.md) applied to
$My'=f(t,y)$ requires, at each step, the solution of the stage equations

$$M(Y_i-y_n)=h\sum_{j=1}^s a_{ij}f(t_n+c_jh,Y_j),\qquad i=1,\dots,s.$$

For a [DIRK method](/methods/diagonally-implicit-runge-kutta.md) these are $s$ consecutive
$d$-dimensional systems; for a [fully implicit method](/methods/fully-implicit-runge-kutta.md)
(Gauss, Radau IIA, Lobatto IIIC) one coupled $sd$-dimensional system. Newton-type iteration
on the stacked stages gives the linear system

$$\bigl(I_s\otimes M-h\,(A\otimes I_d)\,\mathrm{diag}(J_1,\dots,J_s)\bigr)\,\delta\mathbf Y=\mathbf r,$$

with $J_j$ the Jacobian (or a Picard linearization) of $f$ at stage $j$ and $\mathbf r$ the
stacked residual. [Roberts et al. (2021)](/sources/roberts-2021.md) write the multirate GARK
analogue this way (§4, Eqs. (4.1)–(4.4)); [Southworth et al. (2022)](/sources/southworth-2022.md)
write it in stage-derivative variables, $\bigl(I_s\otimes M-h\,[a_{ij}J_i]_{ij}\bigr)\delta\mathbf k=\mathbf r$
(Eqs. (1)–(4)). Multiplying the stage-value form by $A^{-1}\otimes I$ gives Southworth's
reformulation $\bigl(A^{-1}\otimes M-h\,\mathrm{diag}(J_i)\bigr)$ directly *(compiler check,
not in the sources)*. The cost of these solves, not the order theory, is why fully implicit
methods are "rarely used" for large PDE problems (Southworth et al. §1;
[Farrell et al. 2021](/sources/farrell-2021.md), §1).

## Newton variants

- **Full Newton** re-linearizes at every iterate and every stage.
- **Simplified Newton** uses one Jacobian $J$ for all stages and lags it across iterations. It
  loses quadratic convergence but makes the linear system Kronecker-structured,
  $I_s\otimes M-hA\otimes J$; it can win for small steps or mildly stiff problems (Southworth et
  al. §3, §7.1.2).
- **Lagged (modified) Newton.** Jacobians and preconditioners are reused across steps.
  [ARKODE](/software/arkode.md) uses the Newton matrix $M-h a_{ii}J$ with CVODE's lagging
  heuristics ([Reynolds et al. 2023](/sources/reynolds-2023.md), §3.4, Eqs. (18)–(20)).
  [Gardner et al. (2022)](/sources/gardner-2022.md) note that matrix-based solvers update
  Jacobians and factorizations infrequently, amortizing their cost over steps (§5). Roberts et al.
  reuse the fast Jacobian per micro-step and the slow one per macro-step in multirate methods
  (§4).
- **Linearly implicit stages.** For a right-hand side linear in $y$, ARKODE performs one Newton
  iteration per stage (Reynolds et al. §2.2). [Rosenbrock–Wanner methods](/methods/rosenbrock-wanner-method.md)
  build this single linear solve into the method.
- **Correction form.** SUNDIALS integrators solve for a correction to a predicted stage, in
  root-finding form $G(\delta)=0$ or fixed-point form $\delta=\Phi(\delta)$ (page-local symbols).
  The solve must meet a tolerance in the WRMS norm, and the default convergence test estimates
  the convergence rate, detects divergence, and is tied to the local error test so that
  iteration errors do not corrupt [step-size control](/methods/step-size-control.md) (Gardner et
  al. 2022, §2.5, §6, Table 6; Reynolds et al. 2023, §3.4.1).
- **Tolerances.** Nonlinear and linear tolerances are set "slightly more accurately than the
  enclosing level" (Reynolds et al. §3.4.1, §3.4.3); iterative linear solvers stop on a scaled,
  preconditioned residual; for solvers without scaling support the integrators instead test the
  left-preconditioned residual against the tolerance divided by the RMS of the left scaling, which
  controls only the overall residual size, not component balance (Gardner et al. §5,
  Eqs. (2)–(3)).

## Predictors

The initial guess matters. ARKODE predicts each implicit stage by extrapolating the
[dense output](/methods/dense-output.md) of the previous step (Reynolds et al. 2023, §3.4.2):

- **trivial**: $y_n$, the most robust choice for very stiff problems or with constraints;
- **maximum order**: the highest available degree;
- **variable order**: a degree decreasing with the stage index;
- **cutoff order**: maximum order for stages in the first half of the step, linear after;
- **user-supplied**: a post-correction applied after the built-in predictor.

On an advection–diffusion–reaction [Brusselator](/benchmarks/brusselator.md)
(relative tolerance $10^{-4}$), the maximum-order predictor reduced all integrator statistics by
at least 32% against the trivial one for a DIRK and an IMEX splitting; with explicit reactions and
one Newton iteration per stage, the cutoff predictor was best, by up to 20% (§5.1.2, Table 1).
Roberts et al. (2021) take stage predictors for the fast micro-steps of compound-fast multirate
methods from the dense output of the compound step (§4).

## Fully implicit methods: real Schur block preconditioning

Southworth et al. (2022), Part II of a pair whose Part I treats linear problems, solve the
coupled stage system of fully implicit methods for **nonlinear** PDEs and DAEs. The main steps:

1. **Real Schur form.** Write $A^{-1}=Q_0R_0Q_0^\top$ with $Q_0$ orthogonal and $R_0$ block upper
   triangular, with $1\times1$ blocks $\eta$ for real eigenvalues and $2\times2$ blocks
   $\begin{bmatrix}\eta&\theta\\-\omega^2/\theta&\eta\end{bmatrix}$ for pairs $\eta\pm\mathrm i\omega$
   ($Q_0,R_0,\eta,\omega,\theta$ page-local). Under simplified Newton the stage system becomes
   block upper triangular. It is solved by back substitution through backward-Euler-like blocks
   $\eta I-\hat L$, with $\hat L=hM^{-1}J$ (page-local), and coupled $2\times2$ blocks (§3.1,
   Eqs. (8)–(9)). The authors credit the Schur trick to the RADAU code; the novelty they claim is
   the provably robust preconditioning (Remark 3).
2. **Assumptions.** All eigenvalues of $A$ have positive real part, which holds for A-stable,
   irreducible methods with invertible $A$ (Assumption 1). The field of values of the
   linearization lies in the closed left half-plane, $W(\hat L)\le0$, equivalent to
   $\lVert e^{t\hat L}\rVert\le1$ (Assumption 2, §2.2).
3. **Stage-dependent Jacobians.** With distinct $J_i$, the conjugated operator
   $(Q_0^\top\otimes I)\,\mathrm{diag}(\hat L_i)\,(Q_0\otimes I)$ has blocks that are weighted sums
   of the $\hat L_i$, and the off-diagonal weights sum to zero, i.e. they are differences of
   stage Jacobians (§3.2, Eqs. (11)–(12)). Four block-upper-triangular approximations follow:
   simplified Newton (0); Newton-like (1), block diagonal with one dominant $\hat L_k$ per block;
   Newton-like (2), block diagonal with the weighted sums; Newton-like (3), the full
   upper-triangular part. Newton-like (3) is exact Newton for two-stage methods; for two-stage
   Gauss no approximation is needed at all (§3.2).
4. **$2\times2$ blocks.** Each block is solved by GMRES with a block lower-triangular
   preconditioner whose Schur-complement approximation is $\mu I-\hat L_2$, with the shift
   $\mu_*=\eta+\omega^2/\eta$ ($\mu$ page-local; §4, Eqs. (14)–(19), Algorithm 1). Only
   backward-Euler-type preconditioners $\mu M-hJ$ are required.

**Conditioning results** (preconditioned Schur complement, 2-norm condition number $\kappa$):

- **Corollary 1** (identical stage Jacobians): $\kappa\le1+\omega^2/(2\eta^2)$, tight; the
  underlying bound is restated from Part I (§4, Eqs. (23)–(24)).
- **Theorem 2** (distinct stage Jacobians): if $\eta>0$, $W(\hat L_1),W(\hat L_2)\le0$ and
  $\langle\hat L_1w,\hat L_2w\rangle\ge0$ for all $w$, then $\kappa\le2+\omega^2/\eta^2$, at most
  a factor 2 worse. The authors believe the last hypothesis unnecessary but could not remove it
  (Eq. (25), App. A).
- **Table 1** values of the Corollary 1 bound: 1.17 (2-stage Gauss), 1.25 (2-stage Radau IIA),
  1.50 (2-stage Lobatto IIIC), at most 3.44 (5-stage Lobatto IIIC).

**Numerical evidence** (MFEM; counts are preconditioner applications per step, Tables 3, 5–7):

| Test | SDIRK4 | 4th-order Gauss |
|---|---|---|
| [isentropic vortex](/benchmarks/isentropic-vortex.md), $h=2\times10^{-2}$ | 59 | 36 |
| NACA0012, Re 40,000 | 481 | 244 |
| double shear layer, Re 10 | 365 | 161 |
| double shear layer, Re 25,000 | 177 | 75 |

7th- to 10th-order Gauss and Radau IIA cost about as much as SDIRK4 on the double shear layer.
The optimal shift helps even with distinct stage Jacobians: average Krylov iterations per
$2\times2$ solve drop from 14.9 to 7.6 for 10th-order Gauss and from 35.2 to 11.2 for 8th-order
Lobatto IIIC (Table 4). Better Newton approximations shorten run time on the NACA case: 33.8 s
to 21.6 s for 4th-order Gauss, 47.1 s to 25.4 s for 3rd-order Radau IIA (Fig. 2). DAEs lead to
$4\times4$ blocks; the theory covers index-1 problems through the reduced system (§6; see
[differential-algebraic equations](/definitions/differential-algebraic-equation.md)).

## Block preconditioners in finite-element codes

Farrell et al. (2021) generate the coupled stage system symbolically in
[Irksome](/software/irksome.md) and hand it to PETSc's composable solvers. For the heat
equation with mass matrix $M$ and stiffness matrix $K$ the system is
$(I_s\otimes M+hA\otimes K)$ (§2.3, Eq. (31)). Their solver choices (§2.3, §4.2–4.3):

- **Block diagonal.** The Mardal–Nilssen–Staff preconditioner
  $\mathrm{diag}(M+a_{ii}hK)$, each block inverted with one AMG V-cycle inside GMRES. Radau IIA
  with 2 and 3 stages cost about 3 and 5 backward-Euler solves per step, against 3 and 7 for
  Richardson step doubling to second and third order (§4.2, Fig. 3).
- **DIRKs need no special code.** A multiplicative field split on the block lower-triangular
  system is block forward substitution, exact in one iteration (§2.3, §4.3).
- **Explicit methods** need one mass-matrix solve per stage (Eq. (34)).

## Multirate and IMEX structure

- **Multirate GARK.** Roberts et al. (2021) cost decoupled DIRK-based multirate methods at
  $O(\mathbf sd^3)$ per step for $\mathbf s$ total stages (page-local), reduced to $O(md^3)$ with
  factorization reuse ($m$ the multirate ratio); compound-fast methods cost $O(md^3)$, or less
  for component-partitioned systems (§4.1–4.2).
- **Stage reducibility.** When a coupling row repeats across partitions, the coupled Newton
  system collapses to dimension $d$ with matrix $I-h\gamma J^{\{\mathrm f\}}-H\gamma J^{\{\mathrm s\}}$,
  argued to be better conditioned than $I-H\gamma J$ when $m$ matches the stiffness ratio; a
  Woodbury identity handles low-rank couplings (§4.3–4.4). See
  [multirate GARK methods](/methods/multirate-gark.md).
- **IMEX.** The explicit part is evaluated once per stage, the implicit part once per Newton
  iteration, which favours IMEX when the nonstiff term is expensive (Reynolds et al. 2023,
  §5.1.2); see [IMEX Runge–Kutta](/methods/imex-runge-kutta.md).
- **Locality.** When the implicit terms are local, as for pointwise reactions, Gardner et
  al. (2022) solve each MPI task's block with a task-local Newton solver. The only global
  communication left is a final success check. Speedups over a global Newton–GMRES solve are
  4.2× to 7.9× from 40 to 10240 MPI tasks (§6.1, Fig. 3).

## Software

The [SUNDIALS](/software/sundials.md) redesign gives every integrator generic nonlinear-solver
and linear-solver classes (Gardner et al. 2022, §5–6):

- three linear-solver types: matrix-based direct, matrix-based iterative, matrix-free iterative;
- direct solvers: dense, banded and sparse (KLU, SuperLU, cuSOLVER);
- Krylov solvers: GMRES, FGMRES, TFQMR, BiCGStab, CG;
- a wrapper for PETSc SNES.

Matrix-free Jacobian-vector products by finite differences cost extra right-hand-side
evaluations: 609 against 109 for CVODE with CG on a 2D heat problem, removed by a user-supplied
product (§5.1, Table 5). In ARKODE, mass-matrix and system solvers must be of the same type to
form $M-ha_{ii}J$ (Reynolds et al. §3.4.3).

## Qualifications

- Southworth et al. claim that 4th-order Gauss needs "about half" the preconditioner applications
  of SDIRK4 "to achieve the same accuracy". Their tables compare equal *order* at equal $h$, not
  equal error, and the ratio is 0.61 in Table 3.
- Southworth et al. print the NACA step as $5\times10^{-2}$ in the text and Table 5 but as
  $2\times10^{-2}$ in the caption of Fig. 2.
- Farrell et al.'s cost figures are for one mesh and one step size, with no hardware or time
  units stated (§4.2).
- The heat-equation comparison of Gardner et al., CVODE BDF 8.8 s against ARKODE's default DIRK
  67.3 s, is problem-specific; the authors attribute it to BDF's single solve per step and order
  adaptivity (§5.1).

# Citations

- [Southworth et al. (2022)](/sources/southworth-2022.md) — §1–2 (Eqs. (1)–(6), Assumptions 1–2), §3 (Eqs. (8)–(13)), §4 (Cor. 1, Thm. 2, Table 1), §5 (Algorithm 1), §6, §7 (Tables 2–7, Fig. 2), App. A.
- [Farrell et al. (2021)](/sources/farrell-2021.md) — §1, §2.3 (Eqs. (31)–(34)), §4.2 (Fig. 3), §4.3.
- [Roberts et al. (2021)](/sources/roberts-2021.md) — §4.1–4.4 (Eqs. (4.1)–(4.5)).
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §2.2, §3.4 (Eqs. (18)–(21)), §5.1.2 (Table 1).
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §2.5, §5 (Eqs. (2)–(3), Table 5), §6 (Table 6), §6.1 (Fig. 3).
