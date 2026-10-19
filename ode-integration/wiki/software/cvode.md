---
type: Software
title: "CVODE"
description: "CVODE, the SUNDIALS variable-order variable-step multistep integrator (Adams–Moulton 1–12, BDF 1–5 in fixed-leading-coefficient form), with its DAE and sensitivity siblings IDA, CVODES and IDAS, the solver heuristics other SUNDIALS packages inherit, and its measured behaviour."
status: established
aliases: [CVODES, IDA, IDAS]
tags: [software, stiff, dae, step-size-control, implicit-stage-solvers]
timestamp: 2026-10-19T23:00:00Z
---

# CVODE

CVODE is the [SUNDIALS](/software/sundials.md) integrator for ODE
initial-value problems $y'=f(t,y)$, $y(t_0)=y_0$, based on implicit
linear multistep methods with variable step size and variable order:
Adams–Moulton of orders 1 to 12 for nonstiff problems and backward
differentiation formulas (BDF) of orders 1 to 5 for stiff problems
([Gardner et al. (2022)](/sources/gardner-2022.md), §2.1); see
[linear multistep methods](/methods/linear-multistep-method.md) and
[BDF](/methods/backward-differentiation-formula.md). It also
supports projection methods for ODEs whose solution must satisfy
constraints $g(t,y)=0$ (§2.1; no detail given). Its solver heuristics are
the template for the rest of the suite, in particular for
[ARKODE](/software/arkode.md) ([Reynolds et al. (2023)](/sources/reynolds-2023.md), §3.4).

## Method form

CVODE writes its methods in fixed-leading-coefficient form. With
$h=t_n-t_{n-1}$ the step ending at $t_n$, and $\alpha_{n,i}$,
$\beta_{n,i}$ denoting the variable multistep coefficients (page-local),
$$\sum_{i=0}^{K_1}\alpha_{n,i}\,y_{n-i}+h\sum_{i=0}^{K_2}\beta_{n,i}\,f(t_{n-i},y_{n-i})=0,$$
where the summation limits $K_1$, $K_2$ (page-local) depend on method type
and order, and the coefficients depend on type, order and the recent
step-size history (Gardner et al. 2022, §2.1). Each step therefore
requires one nonlinear solve, which Gardner et al. write as
$y_n-h\beta_{n,0}f(t_n,y_n)-a_n=0$ with $a_n$ collecting known data
from past steps (§2.5), solved for a correction to a predicted value by a
`SUNNonlinearSolver` (see [SUNDIALS](/software/sundials.md)).

## Siblings

- **IDA** solves fully implicit DAEs $F(t,y,y')=0$ with consistent
  $y(t_0)$, $y'(t_0)$ by variable-order, variable-step BDF of orders 1–5
  in fixed-leading-coefficient form; each step solves
  $F\big(t_n,y_n,h^{-1}\sum_{i=0}^{q}\alpha_{n,i}y_{n-i}\big)=0$, where
  $q\le5$ is here the BDF order (page-local use) (Gardner et al. 2022,
  §2.2, §2.5). See [differential-algebraic equations](/definitions/differential-algebraic-equation.md).
- **CVODES** and **IDAS** add forward and adjoint sensitivity analysis
  with respect to parameters; forward sensitivities use a block-diagonal
  approximation of the combined Jacobian so that the state Jacobian is
  reused without extra factorizations (§2.5).

## Heuristics inherited by the suite

Reynolds et al. (2023) attribute to CVODE the rules that ARKODE reuses:
WRMS error weights $1/(\mathrm{rtol}\,\lvert y_{n,i}\rvert+\mathrm{atol}_i)$,
nonlinear and linear tolerances "slightly more accurate" than the
enclosing level, lagging of the Newton matrix or preconditioner across
steps, step-size bounding after error or solver failures, and temporal
root finding (§3.1–3.5). Gardner et al. (2022) add that the default
nonlinear convergence test is tied to the local error test via an
estimated convergence rate (§6). See [step-size control](/methods/step-size-control.md)
and [implicit stage solvers](/methods/implicit-stage-solvers.md).

[Glandon et al. (2022)](/sources/glandon-2022.md) describe the
multistep-specific heuristics of a variable-step, variable-order code,
in their own MATLAB implementation of linearly implicit multistep methods
and of a BDF baseline (§7). They do not discuss CVODE itself:

- **History.** Past data are kept as divided differences updated
  recursively, much like the Nordsieck-vector updates of VODE and
  LSODE, which they cite as multistep codes of this kind.
- **Step growth.** Steps grow only after $k$ successful steps at the
  current size, which they call best practice for variable-step multistep
  codes (Remark 7.3).
- **Order selection.** Orders $k-1$, $k$ and $k+1$ are compared (Eq. (7.1)).

See [linearly implicit multistep methods](/methods/linearly-implicit-multistep-method.md).

## Measured behaviour

**Diffusion: CVODE vs ARKODE.** On the SUNDIALS 2D heat demo
($4096\times4096$ grid, 256 MPI tasks on LLNL Quartz,
$\mathrm{rtol}=10^{-5}$, $\mathrm{atol}=10^{-10}$), CVODE with
adaptive-order BDF and hypre CG+PFMG took 84 steps, 106 nonlinear and 449
linear iterations, error $3.2\times10^{-7}$, in 8.8 s; ARKODE with its
default third-order DIRK took 148 steps, 451 nonlinear iterations, error
$4.0\times10^{-7}$, in 67.3 s ([Gardner et al. (2022)](/sources/gardner-2022.md),
§5.1, Table 5). The authors explain the gap by CVODE needing one
nonlinear solve per step regardless of order and adapting its order,
while ARKODE uses a fixed-order method with several implicit stage solves
per step (§5.1).

**As a fast integrator inside MRI.** Wrapped as an ARKODE
`MRIStepInnerStepper` for the fast reactions of a Brusselator under
IMEX-MRI-GARK3a, CVODE's BDF needed 1,709 fast steps and 2,620 fast
evaluations (24% fewer evaluations than a fast DIRK, more than a fast
ERK), error $1.3\times10^{-4}$ ([Reynolds et al. (2023)](/sources/reynolds-2023.md),
§5.1.3, Table 2). A multistep method restarts from first order after
every "reset" and loses its error history; the experiment therefore
lowered CVODE's maximum step-size growth after the first internal step
from $10^4$ to 10 (§5.1.3).

## Qualifications

- **Not a ranking of BDF against DIRK.** The heat-demo comparison is
  one diffusion problem with default, untuned settings; Gardner et al.
  (2022) present it as an example of easy interchange of integrators and
  solvers (§5.1).
- **Sign convention.** Gardner et al. (2022) print the multistep formula
  with $+h\sum\beta_{n,i}f$ (§2.1) but the per-step nonlinear system with
  $-h\beta_{n,0}f$ (§2.5); the sign convention of $\beta_{n,i}$ is not
  reconciled in the paper.
- **Method theory lives elsewhere.** Order, A($\alpha$)-stability angles
  of BDF1–BDF5, Dahlquist's barrier and the stability of variable-step
  BDF are on [BDF](/methods/backward-differentiation-formula.md),
  [linear multistep methods](/methods/linear-multistep-method.md),
  [zero-stability](/definitions/zero-stability.md) and
  [variable-step BDF2 stability](/results/variable-step-bdf2-stability.md).
  None of the ingested sources analyses CVODE's own variable-coefficient
  formulas.

# Citations

- [Gardner et al. (2022)](/sources/gardner-2022.md) — §2.1–§2.2, §2.5, §5.1 (Table 5), §6.
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §3.1–§3.5, §5.1.3 (Table 2).
- [Glandon et al. (2022)](/sources/glandon-2022.md) — §7 (Eqs. (7.1), (7.6)–(7.8), Remark 7.3; VODE/LSODE as Nordsieck-type codes).
