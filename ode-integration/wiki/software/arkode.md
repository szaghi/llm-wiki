---
type: Software
title: "ARKODE"
description: "ARKODE, the SUNDIALS package for one-step methods: a shared time-loop infrastructure with ERKStep, ARKStep (IMEX additive Runge–Kutta) and MRIStep (multirate infinitesimal) steppers, its adaptivity, dense output and implicit predictors, and its measured performance on Brusselator and reacting-flow tests."
status: established
aliases: [ARKode, ERKStep, ARKStep, MRIStep]
tags: [software, imex, multirate, step-size-control, runge-kutta]
timestamp: 2026-10-19T00:00:00Z
---

# ARKODE

ARKODE is the [SUNDIALS](/software/sundials.md) package for one-step,
multi-stage integration of initial-value problems in linearly implicit
form
$$M(t)\,y'=f(t,y),\qquad y(t_0)=y_0,$$
with a user-specified mass matrix $M(t)$ that is nonsingular and
independent of $y$; terminal-value problems (integration backwards in
time) are also allowed ([Reynolds et al. (2023)](/sources/reynolds-2023.md),
§2, Eq. 1). Reynolds et al. (2023) describe ARKODE 5.5.0 in SUNDIALS
6.5.0 (§6) as an *infrastructure*: a core time loop to which
"time-stepping modules" attach by providing only an initialization
function and a step function that returns a candidate $y_{n+1}$ and a
local-error estimate (§2, Fig. 1). Gardner et al. (2022) summarize the
same package within the SUNDIALS redesign ([Gardner et al. (2022)](/sources/gardner-2022.md), §2.3).

## Steppers

**ERKStep** — embedded explicit Runge–Kutta pairs for $y'=f(t,y)$, with
built-in tables of order $p\in\{2,3,4,5,6,8\}$, each usually with an
embedding of order $\hat p=p-1$; a user table without embedding switches
off adaptivity ("fixed-step" mode, for reproducing legacy codes)
(Reynolds et al. 2023, §2.1). The defaults used in its experiments are
Heun–Euler (order 2), Bogacki–Shampine (3), Zonneveld (4) and Cash–Karp
(5) (§5.1.1). ERKStep duplicates a subset of ARKStep and is kept because
its simpler structure allows a leaner, more memory-friendly implementation
(§2.2). See [embedded Runge–Kutta pairs](/methods/embedded-runge-kutta-pair.md).

**ARKStep** — two-partition [additive (IMEX) Runge–Kutta](/methods/imex-runge-kutta.md)
methods for $M(t)y'=f^{\mathrm E}(t,y)+f^{\mathrm I}(t,y)$, written with
stage values:
$$\begin{aligned}
Y_i&=y_n+h_n\sum_{j<i}a^{\mathrm E}_{ij}M^{-1}f^{\mathrm E}(t_n+c^{\mathrm E}_jh_n,Y_j)+h_n\sum_{j\le i}a^{\mathrm I}_{ij}M^{-1}f^{\mathrm I}(t_n+c^{\mathrm I}_jh_n,Y_j),\\
y_{n+1}&=y_n+h_n\sum_{i=1}^s\big(b^{\mathrm E}_iM^{-1}f^{\mathrm E}(t_n+c^{\mathrm E}_ih_n,Y_i)+b^{\mathrm I}_iM^{-1}f^{\mathrm I}(t_n+c^{\mathrm I}_ih_n,Y_i)\big),
\end{aligned}$$
and $\hat y_{n+1}$ with the embedded weights $\hat b^{\mathrm E}$,
$\hat b^{\mathrm I}$ (Reynolds et al. 2023, §2.2, Eqs. 5–7; Gardner et
al. 2022, §2.3). The implicit table is lower triangular
([DIRK](/methods/diagonally-implicit-runge-kutta.md) structure); both
tables must share $s$ but may have $c^{\mathrm E}\ne c^{\mathrm I}$, which
SSP IMEX methods need (Reynolds et al. 2023, §2.2). Built in:
Kennedy–Carpenter IMEX tables of orders 3, 4, 5 with embeddings 2, 3, 4
(ARK3(2)4L[2]SA, ARK4(3)6L[2]SA, ARK5(4)8L[2]SA, and ARK4(3)7L[2]SA1) and
DIRK tables of orders 2–5 with embeddings 1–4. ARKStep also offers a
"linear" flag (`ARKStepSetLinear`) that performs a single Newton
iteration per implicit stage when $f^{\mathrm I}$ is linear in $y$, and a
native interface to XBraid for MGRIT parallel-in-time integration (no
results shown) (§2.2).

**MRIStep** — [multirate infinitesimal methods](/methods/multirate-infinitesimal-methods.md)
for $y'=f^{\mathrm E}+f^{\mathrm I}+f^{\{\mathrm f\}}$ (slow nonstiff,
slow stiff, fast). Each slow stage advances from $t_n+c_{i-1}H$ to
$t_n+c_iH$ by solving a fast IVP $v'=f^{\{\mathrm f\}}(t,v)+r_i(t)$,
where the forcing $r_i$ (page-local) is a polynomial in time built from
slow-function values at earlier stages (Reynolds et al. 2023, §2.3).
MRIStep implements all third- and fourth-order
[IMEX-MRI-GARK](/methods/imex-mri-gark.md) methods of Chinomona and
Reynolds, all third- and fourth-order MRI-GARK methods of Sandu, and the
third-order MIS method of Knoth–Wolke, plus a utility that converts any
sorted slow explicit table into MIS coefficients (§2.3, Eq. 11). Only
"solve-decoupled" slow coupling is supported: an implicit slow stage
occurs only where $c_i=c_{i-1}$, and it then reduces to an ordinary IMEX
stage of step $H$ that needs a nonlinear solve only if its diagonal
coefficient is nonzero (§2.3). The fast scale is integrated by a
user-supplied or an ARKStep "inner stepper"; temporal adaptivity is
available only at the fast scale, multirate adaptivity being called an
open research question (§2.3). The fast integrator can be any object
implementing `MRIStepInnerStepper` (Evolve, FullRHS, Reset), e.g. a
wrapped [CVODE](/software/cvode.md) (§5.1.3).

## Shared infrastructure

- **Error control.** The local error estimate is accepted when its
  WRMS norm, multiplied by a safety bias larger than one, is at most 1;
  for $M\ne I$ residual weights built from $My$ are used for quantities in
  "equation units" (Reynolds et al. 2023, §3.1–3.2, Eqs. 12–14, 17).
  Controllers: PID (the default), PI, I, explicit and implicit
  Gustafsson, an IMEX Gustafsson taking the minimum of the two, and
  user-supplied ones; defaults were tuned by "an exhaustive genetic
  optimization process" over dozens of problems including most of the
  "Test Set for IVP Solvers" (§3.2; the controller formulas are not
  printed, the optimization is not shown). CVODE's step-bounding
  heuristics (growth and decay limits, reduction after failed solves) are
  reused. See [step-size control](/methods/step-size-control.md).
- **Dense output.** Hermite interpolants up to degree 5 for nonstiff
  problems (degrees 4 and 5 cost one and four extra $f$ evaluations), and
  Lagrange interpolation through stored $y_n,\dots$ for stiff problems,
  because "interpolants that use derivative values … can result in order
  reduction" (§3.3; stated, not shown). See [dense output](/methods/dense-output.md).
- **Implicit stages.** The stage equation is posed for a correction to a
  predictor, either as a root-finding problem with Newton matrix
  $M-h_na^{\mathrm I}_{ii}J$ (here $J$ is the Jacobian of $f^{\mathrm I}$)
  or as a fixed-point problem; the Newton matrix is lagged by CVODE
  heuristics (§3.4, Eqs. 18–20). Four built-in predictors extrapolate the
  previous step's interpolant — trivial ($y_n$), maximum order (degree
  $\le\min\{p-1,5\}$), variable order, cutoff order — plus a
  user-supplied correction hook (§3.4.2). Mass-matrix and system solvers
  must be of the same type and storage (§3.4.3). See
  [implicit stage solvers](/methods/implicit-stage-solvers.md).
- **Events and constraints.** Root finding by sign change and modified
  secant; inequality constraints $y_i>0$, $<0$, $\ge0$, $\le0$ checked
  after each successful step, with a step reduction from a linear-in-time
  estimate (§3.5–3.6).
- **Problem changes.** "Reinit" clears all history; "reset" restarts
  from a new $(t_0,y_0)$; "resize" changes the number of unknowns between
  steps (spatial adaptivity) while keeping the adaptivity history (§4).

## Measured performance

All tests below use the 1D advection–diffusion–reaction
[Brusselator](/benchmarks/brusselator.md) ($N=512$ points, serial, one
LLNL Quartz node with Intel Xeon E5-2695 v4 CPUs) unless stated
(Reynolds et al. 2023, §5.1).

- **ERK orders.** With diffusion off, the second-order pair was most
  efficient at loose tolerances (despite more than twice the step
  attempts of third order), third order for errors $10^{-5}$–$10^{-7}$,
  fifth order below $10^{-7}$ (§5.1.1, Fig. 2).
- **Controllers.** The I controller was frequently the least efficient,
  with 13%–50% rejected steps; PI and Gustafsson were often the most
  efficient (<7% rejections); PID fell between PI and I (§5.1.1).
- **Predictors.** For DIRK and an IMEX split with advection explicit
  (ARK4(3)6L[2]SA, $\mathrm{rtol}=10^{-4}$, $\mathrm{atol}=10^{-9}$), the
  maximum-order predictor cut every integrator statistic by at least 32%
  relative to the trivial one (DIRK: 34 → 21 steps, 528 → 256 nonlinear
  iterations); with advection and reaction explicit and one Newton
  iteration, the cutoff predictor was best, by up to 20% (§5.1.2,
  Table 1). IMEX evaluates $f^{\mathrm E}$ once per stage rather than once
  per nonlinear iteration (§5.1.2).
- **Fast integrators under MRI.** With IMEX-MRI-GARK3a at fixed $H=0.1$
  (100 slow steps), a fast DIRK3 gave the smallest error and fewest fast
  steps (307) but the most fast-function evaluations (3,470); a fast ERK3
  was most efficient (2,111 evaluations); a fast CVODE BDF needed 1,709
  steps and 2,620 evaluations (§5.1.3, Table 2).
- **Multirate at scale.** For 3D reacting compressible Euler
  (10-species primordial chemistry, fifth-order FD-WENO) on Summit (IBM
  POWER9 + six NVIDIA V100 per node, one GPU per rank, $25^3$ cells per
  rank), a multirate run (explicit MIS "RK3" slow advection, rank-local
  DIRK fast chemistry) ran in about 10–45 s against about 2,000–3,000 s
  for ARK4(3)7L[2]SA1 IMEX (values read from Fig. 3), from 24 ranks up to
  5,184 (IMEX) and 24,000 (multirate). Both showed ideal algorithmic weak
  scaling; the slowdown in run time is dominated by `MPI_Allreduce`
  synchronizations, which IMEX incurs after every rank-local linear solve
  and MRI only at the slow scale (§5.2, Fig. 3).
- **Implicit solvers.** In the SUNDIALS heat demo ARKODE's default
  third-order DIRK took 144–148 steps and about 67 s against CVODE's 84
  steps and 8–9 s ([Gardner et al. (2022)](/sources/gardner-2022.md),
  §5.1, Table 5); a task-local Newton solver gave 4.2×–7.9× speedups in
  ARKODE IMEX runs (§6.1) — both on [SUNDIALS](/software/sundials.md).
- **Research use.** Chinomona and Reynolds run their IMEX-MRI-GARK
  Brusselator experiments in C on the ARKODE infrastructure (201 and 801
  points), with ARKODE's default fifth-order DIRK at $H=10^{-7}$ as the
  reference solution ([Chinomona and Reynolds (2021)](/sources/chinomona-2021.md), §5.2).

## Qualifications

- **Default vs evidence.** Reynolds et al. (2023) make PID the default
  controller (§3.2) while their own Brusselator test ranks PI and
  Gustafsson above PID (§5.1.1); the paper does not reconcile the two.
  Ranocha et al. find that controller parameters must be tuned to the
  pair; see [step-size control](/methods/step-size-control.md).
- **Order labels.** Reynolds et al. (2023), Eq. 15, write the error of
  one step from exact data as $Ch_n^{p+1}$ and call $p$ a "global order";
  the expression is the local error of a method of global order $p$.
- **Printed slips.** Reynolds et al. (2023), Eq. 22, print the diffusion
  term of all three Brusselator equations as $d\,u_{xx}$; the $v$ and $w$
  equations should carry $d\,v_{xx}$ and $d\,w_{xx}$. Gardner et al.
  (2022), §2.3 and §2.5, index the abscissae inside the weight sums and
  the stage equation as $c_j$ where $c_i$ is meant. The MRI forcing is
  printed with a factor $1/(c_i-c_{i-1})$ although implicit slow stages
  require $c_i=c_{i-1}$; the paper replaces such a stage by its IMEX limit
  without stating the limit (Reynolds et al. 2023, §2.3).
- **Scope.** Reynolds et al. (2023) state that, among PETSc/TS,
  Trilinos/Tempus and DifferentialEquations.jl, only PETSc offered
  multirate methods (§1), a statement dated to 2022; see
  [PETSc TS](/software/petsc-ts.md).

# Citations

- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §1–§6; Eqs. 1, 5–7, 11–22; Fig. 1–3; Tables 1–2 (arXiv v2 numbering).
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §2.3, §2.5, §5.1 (Table 5), §6.1 (Fig. 3).
- [Chinomona and Reynolds (2021)](/sources/chinomona-2021.md) — §5.2 (ARKODE-based Brusselator experiments).
