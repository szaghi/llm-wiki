---
type: Source
title: "Gardner et al. (2022) — Enabling New Flexibility in the SUNDIALS Suite of Nonlinear and Differential/Algebraic Equation Solvers"
description: "Software-design report on the object-oriented redesign of SUNDIALS: generic vector, matrix, linear-solver and nonlinear-solver classes, fused vector operations, the MPIManyVector and Fortran 2003 interfaces, with demonstrations showing no performance loss and 4x–8x speed-up from a task-local Newton solver."
resource: "doi:10.1145/3539801"
source_kind: paper
authors: [Gardner D.J., Reynolds D.R., Woodward C.S., Balos C.J.]
year: 2022
venue: "ACM Trans. Math. Softw. 48:1-24"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_ACM_Transactions_on_Mathematical_Software_Gardner_Enabling_New_Flexibility_in_the_SUNDIALS_Suite_of_Nonlinear.pdf"
tags: [software, sundials, implicit-stage-solvers, hpc]
timestamp: 2026-10-19T12:00:00Z
---

# Summary

The paper reports the redesign of [SUNDIALS](/software/sundials.md) (CVODE, CVODES,
IDA, IDAS, ARKODE, KINSOL) around object-oriented, user-extensible algebraic
components. It proposes no new integration method. The methods are recalled only to
motivate the algebraic operations the packages need: variable-order BDF and Adams
methods in fixed-leading-coefficient form ([CVODE](/software/cvode.md), and IDA for
[DAEs](/definitions/differential-algebraic-equation.md)), additive
[IMEX](/methods/imex-runge-kutta.md) and [DIRK](/methods/diagonally-implicit-runge-kutta.md)
methods and [multirate infinitesimal methods](/methods/multirate-infinitesimal-methods.md)
([ARKODE](/software/arkode.md)), and Newton, fixed-point and Anderson-accelerated
nonlinear solvers.

The contributions are software. The first is a uniform C class pattern (a content
pointer plus a table of required, overridable and optional methods) for four base
classes: `N_Vector`, `SUNMatrix`, `SUNLinearSolver` and `SUNNonlinearSolver`. The
second is optional fused vector operations that cut kernel launches, memory traffic
and MPI reductions. The third is the MPIManyVector, which assembles independently
parallelized subvectors and computes a WRMS norm with one global reduction instead
of $s+1$ for $s$ subvectors ($s$ is not the stage count here). The fourth is a generic linear-solver class (matrix-based direct,
matrix-based iterative, matrix-free iterative) with conventions for scaling,
preconditioning and tolerances. The fifth is a generic nonlinear-solver class that
solves for a correction to a predictor, with linear-setup, linear-solve and
convergence-test callbacks supplied by the integrator (see
[implicit stage solvers](/methods/implicit-stage-solvers.md)). The sixth is
SWIG-generated Fortran 2003 interfaces.

There are two demonstrations. A 2D heat equation on a $4096\times4096$ grid, solved
with hypre solvers wrapped as custom classes, shows no change in solver behaviour or
cost against SUNDIALS v2.7.0. The test also lets CVODE (BDF) and ARKODE (DIRK) be
swapped in one line; on this problem CVODE takes 8.8 s against ARKODE's 67.3 s. A stiff 1D
advection–reaction [Brusselator](/benchmarks/brusselator.md), integrated by ARKODE
IMEX with a custom task-local Newton solver for the reaction stages, runs 4x to
almost 8x faster than a global Newton–GMRES solve on up to 10240 MPI tasks. The
error-weighted tolerances tie into [step-size control](/methods/step-size-control.md)
through the WRMS norm.

# Version read

arXiv:2011.10073v2 [cs.MS], 23 Sep 2021, 24 pages, an author preprint in the ACM
TOMS template with placeholder volume, article and DOI ("Vol. 0, No. 0, Article 0",
"00.0000/0000000.0000000") and "Publication date: 2021". It is not the version of
record: the published issue is 2022, vol. 48. Report number LLNL-JRNL-816631. Title
and authors on page 1 match Crossref. Section, equation, table and page numbers on
this page are those of arXiv v2.

# Key claims

1. SUNDIALS comprises CVODE, CVODES, IDA, IDAS, ARKODE and KINSOL; all but ARKODE are described in Hindmarsh et al. (2005) (§2). **Stated**
2. CVODE uses variable-order, variable-step linear multistep methods in fixed-leading-coefficient form: Adams–Moulton of orders 1–12 for non-stiff and BDF of orders 1–5 for stiff problems; it also supports projection for ODEs with constraints $g(t,y)=0$ (§2.1). **Stated**
3. IDA solves $F(t,y,y')=0$ with variable-order, variable-step BDF of orders 1–5 in fixed-leading-coefficient form (§2.2). **Stated**
4. ARKODE solves $M(t)y'=f(t,y)$, $M$ nonsingular, with explicit, implicit and IMEX additive Runge–Kutta methods (with embeddings) and with MIS and MRI-GARK multirate methods (§2.3). **Stated**
5. In forward sensitivity analysis CVODES and IDAS use the block-diagonal Jacobian approximation of Maly & Petzold, so the ODE/DAE Jacobian is reused without extra factorizations, and one solver interface serves both kinds of integrator (§2.5). **Stated**
6. Before the redesign each package had its own interface to each linear solver, and nonlinear solvers were built into the integrators (§3.1). **Stated**
7. The abstract classes removed "nine duplicate linear solver interfaces and three utility files in each of the SUNDIALS packages" while widening the set of linear solvers each package can use (§5). **Stated**
8. Fused streaming vector operations pay off in standalone CPU tests with many vectors (high-order integrators, above about 1000 unknowns per MPI task), and fused reductions with fewer than about 130K unknowns per task; the thresholds are machine-dependent (§4.1). **Shown** (data not printed)
9. The MPIManyVector computes a WRMS norm with one global reduction instead of $s+1$ ($s$ subvectors) when every subvector provides the local squared-sum kernel (§4.2, Algorithm 1). **Derived**
10. With matrix-based linear solvers, integrators update Jacobians and factorizations rarely, amortizing their cost; with iterative solvers they choose tolerances "just tight enough" to help the outer Newton iteration (§5). **Stated**
11. Iterative linear solvers stop on $\lVert\tilde b-\tilde A\tilde x\rVert_2<\mathrm{tol}$ for the scaled, preconditioned system (Eq. 2); a solver without scaling support is asked for $\lVert P_1^{-1}b-P_1^{-1}Ax\rVert_2<\mathrm{tol}/\bar s_1$ (Eq. 3), which controls only the overall residual size (§5). **Stated**
12. On the heat problem (256 MPI tasks, $\mathrm{rtol}=10^{-5}$, $\mathrm{atol}=10^{-10}$), CVODE with hypre CG + PFMG is the most efficient (84 steps, 109 right-hand-side evaluations, 8.8 s); CVODE with hypre GMRES takes 8.2 s; ARKODE with its default third-order DIRK takes 67.3 s (CG) and 67.5 s (GMRES) (§5.1, Table 5). **Shown**
13. CVODE suits the heat problem because it needs one nonlinear solve per step whatever its order and adapts the order, while ARKODE uses a fixed-order method with several implicit solves per step (§5.1). **Stated**
14. Matrix-free SUNDIALS solvers are slower because finite-difference Jacobian–vector products cost extra right-hand-side evaluations (CVODE CG: 609 against 109 evaluations, 13.0 against 9.3 s); a user-supplied product removes this; SUNDIALS solvers still take about 0.5 more linear iterations per nonlinear iteration than hypre, partly because of the tolerance adjustment (3) (§5.1, Table 5). **Shown**
15. The new linear-solver infrastructure costs nothing: run times of v5.5 and v2.7.0 agree within the observed ~2% variability (e.g. CVODE matrix-free GMRES 12.7 s against 12.3 s) (§5.1, Table 5). **Shown**
16. The CG solver of SUNDIALS v2.7.0 wrongly used a WRMS norm instead of a weighted 2-norm in its convergence test; the v2.7.0 results use a patched version (§5.1, footnote 1). **Stated**
17. The integrators pose the nonlinear system for a correction to a predicted solution, to be solved to a tolerance in the WRMS norm (§6, Table 6). **Stated**
18. The default nonlinear stopping test is tied to the local error test, through an estimate of the convergence rate with divergence heuristics, so that iteration errors do not disturb temporal error control (§6). **Stated**
19. On the stiff advection–reaction Brusselator (ARKODE default third-order IMEX, explicit advection, implicit reaction), a task-local Newton solver gives speed-ups of 4.2x to 7.9x over global Newton–GMRES with a task-local preconditioner, from 40 to 10240 MPI tasks in weak scaling, without hurting scaling (§6.1, Fig. 3). **Shown**
20. With the task-local solver, the only global communication left is a check that every local solve succeeded (§6.1). **Stated**
21. The Fortran 2003 interfaces give access to all features of all six packages (CVODES and IDAS were unreachable from Fortran 77), are thread-safe, and allow derived classes written in Fortran (§7). **Stated**
22. The C and Fortran 2003 versions of the Brusselator demonstration give identical statistics and nearly identical run times (§7.1). **Shown** (no numbers given)
23. SUNDIALS had more than 90,000 downloads in 2020 (§1). **Stated**

# Printed slips

- §2.3 (p. 4), the update and embedded solution of the additive method: "$\hat f^E(t_{n-1}+c^E_j h_n, z_i)$" and "$\hat f^I(t_{n-1}+c^I_j h_n, z_i)$" inside $\sum_{i=1}^s$: the abscissa index should be $i$.
- §2.5 (p. 4), ARKODE stage system: "$z_i - h_nA^I_{i,i}\hat f^I(t_{n-1}+c^I_j h_n, z_i) - a_i = 0$": should be $c^I_i$.
- §2.3 (p. 4), MIS: "$T_i = t_n + c_iH_n$", while the step starts at $t_{n-1}$ elsewhere.
- §2.1 against §2.5: the multistep formula is printed with $+h_n\sum_i\beta_{n,i}f$ while the CVODE stage system reads $y_n-h_n\beta_{n,0}f(t_n,y_n)-a_n=0$; the sign convention of $\beta_{n,i}$ is not reconciled.
- §5.1 (p. 14): "the constants $k_x = k_x = 1.0$", for $k_x=k_y=1.0$.
- §6 (p. 16): "root-finding, $F(u)=0$, or fixed-point, $G(u)=0$", against Eq. (1) $G(u)=u$.
- Typos: "achieved achieved" (§5), "utility methods methods" (§3.2), "strategy[27]" (§2.4).
- Reference [61] prints the title as "Differentialequations. jl–a performant…".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\dot y$, $\dot y=f(t,y)$ | $y'$, $y'=f(t,y)$ | the dot is a time derivative, **not** the registry $\dot f=f'f$ |
| $M(t)$ | $M$ | mass matrix, nonsingular |
| $h_n=t_n-t_{n-1}$, step $y_{n-1}\to y_n$ | $h_n$, step $y_n\to y_{n+1}$ | index shift by one |
| $z_i$ | $Y_i$ | stage values |
| $\tilde y_n$, $\tilde b$ | $\hat y_{n+1}$, $\hat b$ | embedded solution |
| $f^E$, $f^I$; $A^E$, $A^I$, $b^E$, $b^I$, $c^E$, $c^I$ | $f^{\mathrm E}$, $f^{\mathrm I}$; $A^{\mathrm E}$, … | agrees |
| $\hat f^E$, $\hat f^I$ | $M^{-1}f^{\mathrm E}$, $M^{-1}f^{\mathrm I}$ | the hat does not mean embedded here |
| $f^S$, $f^F$, $H_n$, $h_n$ | $f^{\{\mathrm s\}}$, $f^{\{\mathrm f\}}$, $H$, $h$ | multirate |
| **$\alpha_{n,i}$, $\beta_{n,i}$** | kept | variable multistep coefficients; **collide** with the Shu–Osher $\alpha_{ij}$, $\beta_{ij}$ and the PID $\beta$ |
| **$q$** | BDF order, in words here | **collision** with the registry stage order |
| $F(t,y,\dot y)$ | kept | DAE residual (IDA); $F(u)$ is also the KINSOL root function |
| **$A$, $x$, $b$** (linear system) | kept | **collide** with the Butcher $A$, $b$ |
| $P_1$, $P_2$, $S_1$, $S_2$, $\bar s_1$, tol | kept | preconditioners, scalings, RMS of $\mathrm{diag}(S_1)$, solver tolerance |
| $\lVert\cdot\rVert_{wrms}$, $w$ | $\lVert\cdot\rVert_{\mathrm{WRMS}}$ | |
| $s$ (§4.2) | kept | number of subvectors, not stages |
| $\epsilon$ (Brusselator) | $\varepsilon$ | stiffness parameter |

# Reference list

76 printed references, numbered [1]–[76] in ACM style, alphabetical by first author.
The list is merged complete into the [bibliography](/bibliography.md) with `citedby`
gardner-2022. Same-key collisions take suffixes in printed order (Balay 2021,
Brown 1989, Hindmarsh 1995, Schlegel 2012, two SUNDIALS-team web items). [11]
(Balos et al., printed "To appear", arXiv:2011.12984) is kept as its own
pre-publication entry. [47] prints the volume "PP" (early access) and [51] prints
"46, 4 (2010), 7". No printed duplicates and no unparseable items.

# Pages created or updated

Chunk 1 (2026-10-19); updated in later chunks. This source is cited on:

* [ARKODE](/software/arkode.md)
* [Backward differentiation formulas (BDF)](/methods/backward-differentiation-formula.md)
* [Brusselator](/benchmarks/brusselator.md)
* [CVODE](/software/cvode.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Differential-algebraic equations and their Runge–Kutta treatment](/definitions/differential-algebraic-equation.md)
* [Heat equation](/benchmarks/heat-equation.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [Linear multistep methods](/methods/linear-multistep-method.md)
* [Multirate infinitesimal methods (MIS, MRI-GARK)](/methods/multirate-infinitesimal-methods.md)
* [PETSc TS](/software/petsc-ts.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
* [SUNDIALS](/software/sundials.md)
