---
type: Software
title: "SUNDIALS"
description: "The SUNDIALS suite (CVODE, CVODES, IDA, IDAS, ARKODE, KINSOL): its six packages, the object-oriented redesign into vector, matrix, linear-solver and nonlinear-solver classes, fused and many-vector operations, Fortran 2003 interfaces, and the measured cost of the redesign."
status: established
aliases: [SUite of Nonlinear and DIfferential/ALgebraic equation Solvers]
tags: [software, implicit-stage-solvers, parallel, step-size-control, linear-algebra]
timestamp: 2026-10-19T00:00:00Z
---

# SUNDIALS

SUNDIALS is a C library of time integrators and nonlinear solvers from
Lawrence Livermore National Laboratory, built around shared algebraic
building blocks (vectors, matrices, linear and nonlinear solvers) that
user code can replace. Gardner et al. (2022) document the redesign that
turned these building blocks into user-extensible classes (SUNDIALS v5.x),
and Reynolds et al. (2023) describe its one-step integrator package
[ARKODE](/software/arkode.md) as of SUNDIALS 6.5.0. The papers report
more than 90,000 downloads in 2020 ([Gardner et al. (2022)](/sources/gardner-2022.md), §1).

## Packages

[Gardner et al. (2022)](/sources/gardner-2022.md), §2, list six packages:

| Package | Problem | Methods (as of the source) |
|---|---|---|
| [CVODE](/software/cvode.md) | $y'=f(t,y)$ | variable-order, variable-step Adams–Moulton (orders 1–12) and BDF (orders 1–5) in fixed-leading-coefficient form; projection for constrained ODEs |
| CVODES | $y'=f(t,y,\cdot)$ with parameters | CVODE plus forward and adjoint sensitivity analysis |
| IDA | DAE $F(t,y,y')=0$ | variable-order, variable-step BDF of orders 1–5 |
| IDAS | parametrized DAE | IDA plus sensitivity analysis |
| [ARKODE](/software/arkode.md) | $My'=f(t,y)$, $M$ nonsingular | explicit, diagonally implicit and IMEX additive Runge–Kutta with embeddings; multirate infinitesimal (MIS, MRI-GARK) methods |
| KINSOL | $F(u)=0$ or $u=G(u)$ | inexact and modified Newton with optional line search; fixed-point and Picard iteration with optional Anderson acceleration |

For forward sensitivities, CVODES and IDAS use a block-diagonal
approximation of the combined Jacobian so that the state Jacobian is
reused without extra factorizations or preconditioner setups (§2.5).

## Architecture

**Class pattern.** Every base class is a C struct holding an opaque
`content` pointer and a table of function pointers (a virtual method
table) with required, overridable and optional methods; empty
constructors allocate the base and a derived class fills in content and
pointers (Gardner et al. 2022, §3.2, Fig. 1). The four base classes are
`N_Vector`, `SUNMatrix`, `SUNLinearSolver` and `SUNNonlinearSolver`.
Before the redesign every package carried its own interface to every
linear solver and embedded its nonlinear solver; the abstraction removed
"nine duplicate linear solver interfaces and three utility files in each
of the SUNDIALS packages" (§3.1, §5).

**Vectors.** Optional fused operations (`N_VLinearCombination`,
`N_VScaleAddMulti`, `N_VDotProdMulti`) and vector-array operations cut
kernel launches, memory traffic and MPI reductions; when a pointer is
`NULL` the base class falls back to the required operations (§4.1,
Table 1). In stand-alone CPU tests the fused streaming operations paid
off above about 1,000 unknowns per MPI task for high-order integrators and
the fused reductions below about 130,000 unknowns per task, thresholds the
authors call machine dependent (§4.1; data not shown). The
**MPIManyVector** joins independently parallelized subvectors (serial,
OpenMP, CUDA, MPI-aware or not) under one communicator, possibly an
intercommunicator for multiphysics coupling; with an optional local
reduction kernel, the WRMS norm of a many-vector costs one
`MPI_Allreduce` instead of one per subvector plus one (§4.2,
Algorithm 1). **MPIPlusX** wraps a single on-node vector with
a communicator (§4.3).

**Linear solvers.** A `SUNLinearSolver` declares one of three types —
matrix-based direct, matrix-based iterative, matrix-free iterative — and
solves $Ax=b$ to a tolerance; setup (factorization, preconditioner
construction) is separate and amortized because the integrators update
Jacobians infrequently (Gardner et al. 2022, §5, Tables 2–3). Iterative
solvers are asked to meet a 2-norm tolerance on the scaled, left- and
right-preconditioned system; for solvers that cannot scale, the
integrators divide the tolerance by the RMS of the left scaling, which
controls only the overall residual size, not its component balance (§5,
Eqs. 2–3). Provided implementations: dense (native, LAPACK, MAGMA), band
(native, LAPACK), sparse (KLU, SuperLU_MT, SuperLU_DIST, cuSOLVER), and
matrix-free scaled preconditioned GMRES, FGMRES, TFQMR, BiCGStab and CG
(§5).

**Nonlinear solvers.** A `SUNNonlinearSolver` is of root-finding or
fixed-point type and solves for a *correction* to a predicted value, to a
tolerance in the WRMS norm; the integrator supplies the linear setup and
solve functions and, optionally, the convergence test (§6, Tables 6–7).
The default stopping test is tied to the local error test through an
estimated convergence rate, so that iteration error does not pollute
temporal error control, with heuristics to detect divergence (§6). A
wrapper of PETSc's SNES is provided. The stage equations these solvers
receive are described on [implicit stage solvers](/methods/implicit-stage-solvers.md).

**Fortran.** SWIG-Fortran generates Fortran 2003 interfaces to all six
packages: thread safe (the old Fortran 77 interface used global memory),
covering CVODES and IDAS for the first time, and allowing derived classes
written in Fortran (§7).

## Shared integrator conventions

All packages measure errors in the weighted RMS norm
$$\lVert v\rVert_{\mathrm{WRMS}}=\Big(\frac1d\sum_{i=1}^d\Big(\frac{v_i}{\mathrm{rtol}\,\lvert y_{n,i}\rvert+\mathrm{atol}_i}\Big)^2\Big)^{1/2},$$
and a value $\le1$ means "within tolerance" ([Reynolds et al. (2023)](/sources/reynolds-2023.md),
§3.1, Eqs. 12–13). Nonlinear and linear solves are made only slightly
tighter than the enclosing level, and Jacobians or preconditioners are
lagged across steps, by heuristics that originate in
[CVODE](/software/cvode.md) and that ARKODE inherits (Reynolds et al.
2023, §3.4; Gardner et al. 2022, §5). Temporal root finding (sign-change
detection plus a modified secant method) is common to the packages
(Reynolds et al. 2023, §3.5). Error-based step-size selection is
treated on [step-size control](/methods/step-size-control.md).

## Measured performance

**No cost from the abstraction.** On a 2D heat equation
($4096\times4096$ grid, second-order differences, 256 MPI tasks on eight
LLNL Quartz nodes with two 18-core Intel Xeon E5-2695 v4 each,
$\mathrm{rtol}=10^{-5}$, $\mathrm{atol}=10^{-10}$, 100-run averages), run
times of v5.5 and v2.7.0 agree within the observed ~2% variability:
CVODE matrix-free GMRES 12.7 s vs 12.3 s, ARKODE matrix-free CG 102.0 s vs
104.2 s ([Gardner et al. (2022)](/sources/gardner-2022.md), §5.1, Table 5).
v2.7.0's CG had to be patched for this comparison because it tested
convergence in a WRMS norm instead of a weighted 2-norm (§5.1, footnote 1).

**Third-party solvers.** The same heat problem with hypre's CG or GMRES
plus PFMG multigrid, wrapped as a custom `SUNMatrix`/`SUNLinearSolver`,
gave the fastest runs: CVODE 8.8 s (CG) and 8.2 s (GMRES); ARKODE with its
default third-order DIRK 67.3 s and 67.5 s. Matrix-free SUNDIALS solvers
pay extra right-hand-side evaluations for difference-quotient
Jacobian–vector products (CVODE CG: 609 vs 109 evaluations, 13.0 vs
9.3 s); a user-supplied Jacobian–vector product removes that overhead
(Table 5). The CVODE/ARKODE gap is discussed on [CVODE](/software/cvode.md).

**Custom nonlinear solver.** For an IMEX ARKODE run of a stiff 1D
advection–reaction [Brusselator](/benchmarks/brusselator.md)
(advection explicit, reaction implicit), a user-written task-local Newton
solver — each MPI task solves its own reaction block with serial vectors,
with one global success check per solve — was 4.2× to 7.9× faster than a
global Newton–GMRES solve with task-local preconditioner, in a weak-scaling
study from 40 to 10,240 MPI tasks on LLNL Lassen (two IBM POWER9 per
node, 40 tasks per node, CPUs only, 20-run averages) (Gardner et al.
2022, §6.1, Fig. 3). The Fortran 2003 version gave identical solver
statistics and nearly identical run times (§7.1; numbers not given).

**Heterogeneous many-vector.** Reynolds et al. (2023), §5.2, run a 3D
reacting compressible Euler problem on Summit with an MPIManyVector whose
hydrodynamic fields live on the CPU and whose chemistry fields live on the
GPU, with MAGMA batched dense LU for the block-diagonal chemistry
Jacobian; the timing results are on [ARKODE](/software/arkode.md).

## Qualifications

- The heat-equation comparison uses default, untuned settings on one
  diffusion problem; the authors themselves present it as a demonstration
  of interchangeability, not as a method ranking (Gardner et al. 2022,
  §5.1).
- Both papers were read as arXiv preprints (Gardner et al. 2022: arXiv
  v2, 2021; Reynolds et al. 2023: arXiv v2, 2022); version numbers and
  feature lists are those of the preprints.

# Citations

- [Gardner et al. (2022)](/sources/gardner-2022.md) — §1–§7; Tables 1–7; Table 5 (heat demo); Fig. 3 (task-local Newton); Algorithm 1 (many-vector WRMS norm).
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §1, §3.1 (WRMS norm, Eqs. 12–14), §3.4–3.5, §5.2 (Summit run), §6 (SUNDIALS 6.5.0).
