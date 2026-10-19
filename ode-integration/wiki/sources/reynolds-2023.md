---
type: Source
title: "Reynolds et al. (2023) — ARKODE: A Flexible IVP Solver Infrastructure for One-step Methods"
description: "Software paper describing ARKODE, the SUNDIALS infrastructure for one-step methods: a shared time loop with error control, dense output, implicit predictors and solver interfaces, plus explicit, additive IMEX and multirate infinitesimal stepping modules, demonstrated on a Brusselator and a GPU reacting-flow weak-scaling study."
resource: "doi:10.1145/3594632"
source_kind: paper
authors: [Reynolds D.R., Gardner D.J., Woodward C.S., Chinomona R.]
year: 2023
venue: "ACM Trans. Math. Softw. 49:1-26"
local_file: "/home/stefano/papers/mosaic/ode-integration/2023_Crossref_ACM_Transactions_on_Mathematical_Software_Reynolds_ARKODE_A_Flexible_IVP_Solver_Infrastructure_for_One-step_Met.pdf"
tags: [software, sundials, imex, multirate, step-size-control]
timestamp: 2026-10-19T12:00:00Z
---

# Summary

[ARKODE](/software/arkode.md), the [SUNDIALS](/software/sundials.md) package for
one-step multistage [Runge–Kutta](/definitions/runge-kutta-method.md)-type
integration, solves IVPs $M(t)y'=f(t,y)$ with a nonsingular, $y$-independent mass
matrix (see [differential-algebraic equations](/definitions/differential-algebraic-equation.md)).
The paper presents it as an infrastructure. A shared time loop provides
[step-size control](/methods/step-size-control.md) in the WRMS norm,
[dense output](/methods/dense-output.md) by Hermite or Lagrange interpolation,
implicit-stage predictors, interfaces to SUNDIALS nonlinear and linear solvers with
Jacobian-lagging heuristics inherited from [CVODE](/software/cvode.md) (see
[implicit stage solvers](/methods/implicit-stage-solvers.md)), event detection,
inequality constraints and reinit/reset/resize. A stepping module only supplies an
initialization function and a step function that returns a candidate solution and
a local error estimate.

Three modules exist. ERKStep provides [embedded](/methods/embedded-runge-kutta-pair.md)
explicit pairs of orders 2–8. ARKStep provides two-partition
[additive IMEX](/methods/imex-runge-kutta.md) methods (Kennedy–Carpenter ARK of
orders 3–5), DIRK and explicit methods, with a mass matrix, a one-Newton-iteration
option for linear $f^{\mathrm I}$ and an XBraid parallel-in-time interface. MRIStep
provides [multirate infinitesimal methods](/methods/multirate-infinitesimal-methods.md):
[IMEX-MRI-GARK](/methods/imex-mri-gark.md), MRI-GARK and MIS, with a user-supplied
or ARKStep inner integrator for $f^{\{\mathrm f\}}$, and adaptivity only at the fast
scale.

The numerical section illustrates rather than proves. A 1D advection–diffusion–reaction
[Brusselator](/benchmarks/brusselator.md) compares explicit orders 2–5 and
controllers, DIRK against two IMEX splittings with four predictors, and three fast
integrators under IMEX-MRI-GARK3a. A 3D reacting compressible Euler weak-scaling
study on Summit compares an IMEX ARK run with an explicit-MIS multirate run (CPU
hydrodynamics, GPU chemistry). The multirate run is roughly 50–100 times faster
because the costly advection operator, and the global reductions, are evaluated only
at the slow scale. The paper compares ARKODE with [PETSc TS](/software/petsc-ts.md)
and [DifferentialEquations.jl](/software/differentialequations-jl.md), and mentions
[splitting](/methods/operator-splitting.md) as the low-order alternative. No theorems
are proved.

# Version read

arXiv:2205.14077v2 [cs.MS], 21 Dec 2022, 26 pages (0:1–0:26), typeset in the ACM
TOMS author template with placeholders ("Vol. 0, No. 0, Article 0", "Publication
date: 2022", DOI `XXXXXXX.XXXXXXX`). It is not the version of record: the published
issue is 2023, vol. 49. Title and authors on page 1 match Crossref. The software
described is ARKODE 5.5.0 in SUNDIALS 6.5.0. Section, equation and page numbers on
this page are those of arXiv v2.

# Key claims

1. ARKODE treats $M(t)y'=f(t,y)$, $y(t_0)=y_0$, with $M(t)$ user-supplied, nonsingular and independent of $y$; terminal-value problems (reverse integration) are allowed (§2, Eq. (1)). **Stated**
2. The core provides the time loop; a stepper attaches by supplying an initialization function and a step function that returns a candidate $y_{n+1}$ and a local error estimate (§2, Fig. 1). **Stated**
3. ERKStep supplies embedded explicit pairs of orders $p\in\{2,3,4,5,6,8\}$, usually with $\hat p=p-1$; a user tableau without embedding disables adaptivity (fixed-step mode) (§2.1). **Stated**
4. ARKStep provides Kennedy–Carpenter IMEX ARK tableaux of orders $p\in\{3,4,5\}$ ($\hat p\in\{2,3,4\}$) and DIRK tableaux of orders $p\in\{2,3,4,5\}$ ($\hat p\in\{1,2,3,4\}$); the explicit and implicit tableaux must share $s$ but may have $c^{\mathrm E}\neq c^{\mathrm I}$, as SSP IMEX methods need (§2.2). **Stated**
5. ERKStep is kept although ARKStep with $f^{\mathrm I}$ disabled contains it, because its simpler form allows a more efficient, memory-friendly implementation (§2.2). **Stated**
6. `ARKStepSetLinear` declares $f^{\mathrm I}$ linear in $y$, and only one Newton iteration is then done per implicit stage (§2.2). **Stated**
7. ARKStep has a native interface to XBraid (MGRIT parallel-in-time) (§2.2). **Stated**
8. MRIStep implements all third- and fourth-order IMEX-MRI-GARK methods of Chinomona–Reynolds, the third-order MIS method of Knoth–Wolke, and all third- and fourth-order MRI-GARK methods of Sandu; it supports only solve-decoupled diagonally implicit slow coupling, and adaptivity only at the fast scale (multirate adaptivity is called an open question) (§2.3). **Stated**
9. An MIS method built from a slow explicit tableau of order at least 2 has order 2; it has order 3 if the tableau has order at least 3 and satisfies Knoth–Wolke's extra condition (§2.3, after Eq. (11)). **Stated** (cited)
10. A solve-decoupled MRI stage with $\Delta c_i=0$ reduces to an IMEX ARK stage of step $H$ with $A^{\mathrm E}_{ij}=\sum_k\omega^{(k)}_{ij}/(k+1)$, $A^{\mathrm I}_{ij}=\sum_k\gamma^{(k)}_{ij}/(k+1)$, with $\omega^{(k)}_{ij}$, $\gamma^{(k)}_{ij}$ the entries of $\Omega^{(k)}$, $\Gamma^{(k)}$; a nonlinear solve is needed only if $A^{\mathrm I}_{ii}\neq0$ (§2.3). **Derived**
11. A step is accepted when $\mathrm{err}_n=\lVert\text{local error estimate}\rVert_{\mathrm{WRMS}}\le1$, with weights $w_i=(\mathrm{rtol}\lvert y_{n,i}\rvert+\mathrm{atol}_i)^{-1}$; residual weights are used for equation-unit quantities when $M\neq I$ (§3.1–3.2, Eqs. (12)–(14), (17)). **Stated**
12. The controllers are PID (the default), PI, I ("standard" in most public solvers), explicit and implicit Gustafsson, and an IMEX Gustafsson taking the minimum of the two, plus user-supplied ones; the default parameters come from "an exhaustive genetic optimization process" on dozens of test problems (§3.2). **Stated** (optimization not shown; formulas not printed)
13. Hermite dense output reaches degree 5 for non-stiff problems, with degrees 4 and 5 costing one and four extra $f$ evaluations; Lagrange interpolation of stored solutions is used for stiff problems because derivative-based interpolants "can result in order reduction" (§3.3). **Stated**
14. There are four built-in implicit predictors (trivial, maximum order, variable order, cutoff order) plus a user hook; the maximum-order degree is capped at $\min\{p-1,\xi_{\mathrm{user}},5\}$ (§3.4.2). **Stated**
15. Nonlinear and linear solver tolerances are set slightly tighter than the enclosing level, and the Jacobian or preconditioner is lagged across steps, following CVODE heuristics (§3.4.1, §3.4.3). **Stated**
16. Mass-matrix and system linear solvers must be of the same type and, if matrix-based, use the same storage, to form $M-\gamma J$ (§3.4.3). **Stated**
17. Root finding checks for sign changes after each successful step and refines with a modified secant method; inequality constraints are checked after a successful step and before the error test, reducing the step from a linear-in-time estimate (§3.5–3.6). **Stated**
18. "Resize" changes the number of unknowns between steps (spatial AMR) without discarding adaptivity history; MRIStep uses "reset" for each fast IVP (§4). **Stated**
19. On the advection–reaction Brusselator with explicit orders 2–5, order 2 (Heun–Euler) is the most efficient at coarse accuracy despite more than twice the step attempts of order 3, order 3 for errors $10^{-5}$–$10^{-7}$, and order 5 below $10^{-7}$ (§5.1.1, Fig. 2). **Shown**
20. On the same test the I controller is often the least efficient, with 13%–50% rejected steps; PI and Gustafsson are often the most efficient (under 7% rejections); PID lies between PI and I (§5.1.1). **Shown**
21. For DIRK and IMEX-1 (ARK4(3)6L[2]SA, $\mathrm{rtol}=10^{-4}$, $\mathrm{atol}=10^{-9}$) the maximum-order predictor cuts every integrator statistic by at least 32% against the trivial predictor, and the variable- and cutoff-order predictors by at least 19%; for IMEX-2 (explicit reactions, one Newton iteration) the cutoff predictor is best, up to 20% better (§5.1.2, Table 1). **Shown**
22. With IMEX ARK, $f^{\mathrm E}$ is evaluated once per stage rather than once per nonlinear iteration, which favours IMEX when the non-stiff term is costly (§5.1.2). **Shown** (Table 1 counts)
23. Under IMEX-MRI-GARK3a ($H=0.1$, 100 slow steps), a fast DIRK gives the smallest error with the fewest fast steps (307) but the most $f^{\{\mathrm f\}}$ evaluations (3470); a fast explicit method is the most efficient (2111 evaluations); CVODE BDF uses 1709 steps and 2620 evaluations (§5.1.3, Table 2). **Shown**
24. CVODE's multistep methods restart from first order after each reset and lose their error history; the example limits the step growth after the first internal step from $10^4$ to 10 (§5.1.3). **Stated**
25. On Summit (6 V100 per node, one GPU per rank, $25^3$ cells per rank, $H\le10\Delta x$), both IMEX and multirate runs show ideal algorithmic weak scalability, and the multirate run "easily outperforms" IMEX through far fewer advection evaluations (§5.2, Fig. 3). **Shown** (from Fig. 3: IMEX about 2000–3000 s over 24–5184 ranks, multirate about 10–45 s over 24–24000 ranks)
26. The loss of parallel efficiency in both runs is dominated by `MPI_Allreduce` synchronizations, which follow every rank-local linear solve for IMEX but occur only at the slow scale for multirate (§5.2). **Shown**
27. Among PETSc TS, Trilinos Tempus and DifferentialEquations.jl, only PETSc supports multirate methods (a second-order multirate partitioned RK) (§1). **Stated** (as of 2022)

# Printed slips

- Eq. (22), Brusselator: "$v_t=-c\,v_x+d\,u_{xx}+w\,u-v\,u^2$" and "$w_t=-c\,w_x+d\,u_{xx}+(b-w)/\epsilon-w\,u$": the diffusion terms should be $d\,v_{xx}$ and $d\,w_{xx}$ (checked visually, p. 15).
- §3.2: "an 'ImEx' Gustaffson controller", for Gustafsson.
- §3.3.1 against §3.4.2: $\pi_0$ is $\tfrac12(y_{n-1}+y_n)$ in the Hermite list but $\pi_0(t)=y_{n-1}$ for the trivial predictor.
- §3.3.2: the Lagrange basis is printed with nodes $t_i$, $t_j$ while the data are $y_{n-j}$; the nodes should be $t_{n-i}$, $t_{n-j}$.
- §2.3: the MRI forcing $r_i(t)$ carries a factor $1/\Delta c_i$, while implicit solve-decoupled stages require $\Delta c_i=0$; the paper replaces such a stage by an IMEX ARK stage without stating the limit.
- Eq. (15): "$\lVert y_n-y(t_n)\rVert=Ch_n^{q+1}+O(h_n^{q+2})$ … assumed exact initial conditions for the step" describes the local error, yet $q$ and $p$ are called "global orders".
- §2.1: "The embedding, $\tilde y_n$. typically provides …", a stray full stop.
- §5.1: "two Intel Xeon 5-2695 v4 CPUs", for E5-2695 v4.
- §5.1.3: the fast right-hand side is printed $f^f$ against $f^F$ in §2.3.
- §5.2: "non-block fat tree topology", for non-blocking.
- References [34]/[35] (Kennedy & Carpenter 2003), [36]/[37] (Kennedy & Carpenter 2019) and [52]/[53] (Schlegel et al. 2009) are each the same work printed twice.
- Fig. 3: the IMEX panels span 24–5184 ranks and the multirate panels 24–24000; the text does not say so.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $M(t)$ | $M$ | mass matrix, here time-dependent and nonsingular |
| $h_n=t_n-t_{n-1}$, step $y_{n-1}\to y_n$ | $h_n$, step $y_n\to y_{n+1}$ | index shift by one |
| $z_i$ | $Y_i$ | stage values |
| $A$, $b$, $c$, $\tilde b$, $\tilde y_n$ | $A$, $b$, $c$, $\hat b$, $\hat y_{n+1}$ | |
| **$q$, $p$** | $p$, $\hat p$ | **collision:** source $q$ is the method order and $p$ the embedding order; registry $q$ is the stage order |
| $f^E$, $f^I$; $A^E$, $A^I$, $b^E$, $b^I$, $c^E$, $c^I$ | $f^{\mathrm E}$, $f^{\mathrm I}$; $A^{\mathrm E}$, … | agrees |
| $\hat f^{E}$, $\hat f^{I}$ | $M^{-1}f^{\mathrm E}$, $M^{-1}f^{\mathrm I}$ | the hat does not mean embedded here |
| $f^F$ (also $f^f$); $f^E+f^I$ | $f^{\{\mathrm f\}}$; $f^{\{\mathrm s\}}$ | fast and slow parts |
| $H$, $h$ | $H$, $h$ | macro and micro step; agrees |
| $\omega_{i,j}(\theta)$, $\gamma_{i,j}(\theta)$; $\omega^{\{k\}}_{i,j}$, $\gamma^{\{k\}}_{i,j}$, $\Omega^{\{k\}}$, $\Gamma^{\{k\}}$ | $\omega_{ij}(\theta)$, $\gamma_{ij}(\theta)$; $\omega^{(k)}_{ij}$, $\gamma^{(k)}_{ij}$, $\Omega^{(k)}$, $\Gamma^{(k)}$ | MRI coupling polynomials and coefficient tables (explicit, implicit slow part); the source's brace superscript **collides** with the GARK partition index $\{q\}$; $\gamma_{i,j}$ clashes with the tree density and Rosenbrock $\gamma$ |
| $\Delta c_i$, $r_i(t)$, $v(t)$ | kept | abscissa increment, forcing and fast IVP of an MRI stage |
| $T_n$ | local truncation error of the step | kept |
| **$\varepsilon_k=\beta\lVert T_k\rVert_{\mathrm{WRMS}}$** | $\mathrm{err}_k$ (biased) | **collision:** $\varepsilon$ is the registry stiffness parameter and $\beta$ (bias $>1$) clashes with the PID exponents |
| $\lVert\cdot\rVert_{\mathrm{WRMS}}$, $w_i$, $\sigma_i$ | $\lVert\cdot\rVert_{\mathrm{WRMS}}$ | $\sigma_i$ residual weights |
| rtol, atol, ratol | $\mathrm{rtol}$, $\mathrm{atol}$ | ratol: residual absolute tolerance |
| $\gamma_i$, $\mathcal A=M-\gamma\,\partial f^I/\partial z$ | $\gamma_i\propto hA^{\mathrm I}_{ii}$, Newton matrix $M-\gamma J$ | $J$ agrees |
| $\pi_\xi$ | kept | interpolant of degree $\xi$ |
| $\epsilon$ (Brusselator) | $\varepsilon$ | stiffness parameter |
| **$c$, $w$** (Brusselator) | kept | advection speed and third species; **collide** with abscissae $c$ and weights $w_i$ |

# Reference list

66 printed references, numbered [1]–[66] in ACM style, alphabetical by first author.
The list is merged complete into the [bibliography](/bibliography.md) with `citedby`
reynolds-2023. Three works are printed twice ([34]/[35], [36]/[37], [52]/[53]); these printed
duplicates are one entry each in the bibliography. Schlegel 2012 [54]/[55] are distinct works and take
suffixes, as do the two Reynolds 2022 items ([46] demonstration code, [48] user
documentation). arXiv citations ([2], [14], [18], [33], [47]) are separate entries.
No unparseable items.

# Pages created or updated

Chunk 1 (2026-10-19); updated in later chunks. This source is cited on:

* [ARKODE](/software/arkode.md)
* [Backward differentiation formulas (BDF)](/methods/backward-differentiation-formula.md)
* [Brusselator](/benchmarks/brusselator.md)
* [CVODE](/software/cvode.md)
* [Dense output](/methods/dense-output.md)
* [Differential-algebraic equations and their Runge–Kutta treatment](/definitions/differential-algebraic-equation.md)
* [DifferentialEquations.jl](/software/differentialequations-jl.md)
* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [IMEX multirate infinitesimal GARK methods](/methods/imex-mri-gark.md)
* [Linear multistep methods](/methods/linear-multistep-method.md)
* [Multirate infinitesimal methods (MIS, MRI-GARK)](/methods/multirate-infinitesimal-methods.md)
* [Negative-coefficient barrier for splitting methods](/results/negative-coefficient-barrier.md)
* [Operator splitting: Lie–Trotter, Strang and dimensional splitting](/methods/operator-splitting.md)
* [PETSc TS](/software/petsc-ts.md)
* [Runge–Kutta method](/definitions/runge-kutta-method.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
* [SUNDIALS](/software/sundials.md)
