---
type: Method
title: "Multirate infinitesimal methods (MIS, MRI-GARK)"
description: "Multirate infinitesimal methods advance the slow partition with a Runge–Kutta skeleton and reach each slow stage by solving a modified fast ODE forced by a polynomial in time built from slow tendencies; the page covers MIS and MRI-GARK, their stage structure, order statements and implementation in ARKODE."
status: established
aliases: [MRI, MRI-GARK, MIS, multirate infinitesimal step method, multirate infinitesimal GARK, infinitesimal multirate]
tags: [multirate, runge-kutta, imex, software]
timestamp: 2026-10-19T12:00:00Z
---

# Multirate infinitesimal methods (MIS, MRI-GARK)

A multirate infinitesimal method splits $y'=f^{\{\mathrm f\}}(t,y)+f^{\{\mathrm s\}}(t,y)$
into a slow partition, sampled only at the $s$ stages of an outer Runge–Kutta-like
skeleton of macro step $H$, and a fast partition, which is integrated
"infinitesimally": between two consecutive slow stages the method solves a
**modified fast initial-value problem** whose forcing is a polynomial in time
built from the slow stage tendencies. Any sufficiently accurate inner solver, with
any inner step, may solve that problem. The family comprises the multirate
infinitesimal step (MIS) methods of Knoth & Wolke and Schlegel et al. and the
MRI-GARK methods of Sandu, as recalled by
[Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) (§2),
[Reynolds et al. (2023)](/sources/reynolds-2023.md) (§2.3),
[Gardner et al. (2022)](/sources/gardner-2022.md) (§2.3) and
[Roberts et al. (2021)](/sources/roberts-2021.md) (§1, in passing). Its IMEX
extension is [IMEX-MRI-GARK](/methods/imex-mri-gark.md).

## Stage structure (MRI-GARK)

The slow abscissae satisfy $0=c_1\le c_2\le\dots\le c_s=1$ (sorted), with
$\Delta c_i=c_i-c_{i-1}\ge0$. Coupling polynomials
$\gamma_{ij}(\theta)=\sum_{k=0}^{k_{\max}}\gamma^{(k)}_{ij}\theta^k$ collect lower-triangular
coupling matrices $\Gamma^{(k)}=(\gamma^{(k)}_{ij})$ (registry notation; the sources
write $\Gamma^{\{k\}}$).
One macro step from $t_n$ (Chinomona & Reynolds 2021, eqs. 2.1–2.2):

$$\begin{aligned}
&Y_1=y_n;\qquad\text{for }i=2,\dots,s:\quad v(0)=Y_{i-1},\\
&v'(\theta)=\Delta c_i\,f^{\{\mathrm f\}}\big(t_n+c_{i-1}H+\Delta c_i\theta,\,v(\theta)\big)+\sum_{j=1}^{i}\gamma_{ij}\big(\tfrac\theta H\big)f^{\{\mathrm s\}}\big(t_n+c_jH,\,Y_j\big),\qquad\theta\in[0,H],\\
&Y_i=v(H);\qquad y_{n+1}=Y_s.
\end{aligned}$$

Here $\theta$ and $v$ are the inner time and inner solution (page-local). A nonzero
$\gamma^{(k)}_{ii}$ makes stage $i$ implicit in the slow function. The example
MRI-GARK-ERK33a of Sandu, as printed by Chinomona & Reynolds (2021, p. 4), has
$c=(0,\tfrac13,\tfrac23,1)$,
$\Gamma^{(0)}$ with rows $(0)$, $(\tfrac13)$, $(-\tfrac13,\tfrac23)$, $(0,-\tfrac23,1)$
and $\Gamma^{(1)}$ with the single nonzero row $(\tfrac12,0,-\tfrac12,0)$ in
position 4: three fast solves and three slow evaluations per step.

**Two equivalent time conventions.** Chinomona & Reynolds (and Gardner et al.)
pose every inner problem on $\theta\in[0,H]$ with the fast right-hand side scaled
by $\Delta c_i$. Reynolds et al. (2023, §2.3) pose it in physical time on
$[t_n+c_{i-1}H,\ t_n+c_iH]$ as $v'=f^{\{\mathrm f\}}(t,v)+r_i(t)$, with forcing
$r_i(t)=\frac1{\Delta c_i}\sum_j\gamma_{ij}\big(\frac{t-t_n-c_{i-1}H}{\Delta c_iH}\big)f^{\{\mathrm s\}}_j$.
The two differ by the change of variable $t=t_n+c_{i-1}H+\Delta c_i\theta$.
Chinomona & Reynolds also include the zero first row ($\Delta c_1=0$) in the
tables, a presentational change relative to Sandu.

## Solve-decoupled stages

A stage with $\Delta c_i=0$ has no fast evolution: integrating the polynomial
forcing over $[0,H]$ turns it into an ordinary additive Runge–Kutta stage with
coefficients $\sum_k\gamma^{(k)}_{ij}/(k+1)$ (Reynolds et al. 2023, §2.3). A
**solve-decoupled** method puts every implicit slow stage ($\gamma^{(k)}_{ii}\ne0$)
at $\Delta c_i=0$, so implicit slow solves and fast evolutions alternate, and a
nonlinear solve is needed only where the diagonal coefficient is nonzero. A
**solve-coupled** stage, with $\gamma_{ii}\ne0$ and $\Delta c_i\ne0$, would need the
stage value both inside the fast forcing and as the end value of the fast
problem. Solve-decoupled methods are easier to implement but, as Chinomona &
Reynolds (2021, §4.1) report, less stable; they cite two works by Roberts and
co-authors, one of them the arXiv preprint of Roberts et al. (2021). Compare the
decoupled-method barrier on
[multirate A-stability barriers](/results/multirate-a-stability-barriers.md).
ARKODE supports only solve-decoupled, diagonally implicit slow coupling
(Reynolds et al. 2023, §2.3).

## MIS as an MRI-GARK method

Given a slow **explicit** tableau $(A^{\mathrm E},b^{\mathrm E},c^{\mathrm E})$ with
$\hat s$ stages (page-local count) and sorted abscissae, the MIS method has
$s=\hat s+1$ stages, $c=(c^{\mathrm E}_1,\dots,c^{\mathrm E}_{\hat s},1)$, constant
coupling ($k_{\max}=0$) and

$$\gamma^{(0)}_{ij}=\begin{cases}0,&i=1,\\ a^{\mathrm E}_{ij}-a^{\mathrm E}_{i-1,j},&2\le i\le\hat s,\\ b^{\mathrm E}_j-a^{\mathrm E}_{\hat s,j},&i=s\end{cases}$$

(Reynolds et al. 2023, eq. 11; a utility in ARKODE performs the conversion). As
recalled there from Knoth & Wolke, the MIS method has order 2 if the slow table
has order at least 2, and order 3 if the slow table has order at least 3 and

$$\sum_{i=2}^{\hat s}\big(c^{\mathrm E}_i-c^{\mathrm E}_{i-1}\big)(e_i+e_{i-1})^\top A^{\mathrm E}c^{\mathrm E}+\big(1-c^{\mathrm E}_{\hat s}\big)\Big(\tfrac12+e_{\hat s}^\top A^{\mathrm E}c^{\mathrm E}\Big)=\tfrac13,$$

with $e_k$ the $k$-th unit vector (page-local). Chinomona & Reynolds (2021,
Remark 4.1) state that, for solve-decoupled tables with $k_{\max}=0$, each of
their third-order coupling conditions is equivalent to this MIS condition.

## Order and accuracy

The order of an MRI method is that of its GARK representation under an exact (or
at least equally accurate) inner solve
([GARK](/methods/generalized-additive-runge-kutta.md)); third- and fourth-order
MRI-GARK conditions are due to Sandu, as cited by Chinomona & Reynolds and by
Roberts et al. On a nonlinear multirate Kværnø–Prothero–Robinson problem
([Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md); fast step
$H/20$), Chinomona & Reynolds (2021, §5.1, Fig. 2) measure rates 3.06 for implicit
MRI-GARK-ESDIRK34a and 3.93 for MRI-GARK-ESDIRK46a, against 0.99 for Lie–Trotter
and 1.98 for a Strang–Marchuk splitting. On the stiff
[Brusselator](/benchmarks/brusselator.md) the same two MRI-GARK methods measure
2.94 and 2.94 on 201 points and 3.02 and 2.42 on 801 points: higher-order methods
show [order reduction](/definitions/order-reduction.md) under spatial refinement.
MRI-GARK-ESDIRK46a is unstable for $H>1/40$ (201 points) and $H>1/80$ (801
points), and is the most efficient method below errors of $10^{-8}$ (§5.2).

## Implementation in ARKODE (MRIStep)

[ARKODE](/software/arkode.md)'s MRIStep implements the third-order MIS method,
all third- and fourth-order MRI-GARK methods of Sandu and all IMEX-MRI-GARK
methods of Chinomona & Reynolds (Reynolds et al. 2023, §2.3). The fast scale is
advanced by an "inner stepper" (ARKStep or user-supplied, e.g. CVODE wrapped
through the Evolve/FullRHS/Reset interface), and each inner problem restarts it
through a "reset". Temporal adaptivity exists only at the fast scale; multirate
step-size adaptivity is called an open research question (§2.3).

- **Inner-solver choice** (Brusselator, IMEX-MRI-GARK3a slow step $H=0.1$, 100 slow
  steps; Table 2): a DIRK inner solver gives the lowest error ($0.01\times10^{-4}$)
  with the fewest fast steps (307) but the most fast evaluations (3,470); an
  explicit inner solver is the most efficient (2,111 evaluations, error
  $0.44\times10^{-4}$); CVODE's BDF needs 1,709 steps and 2,620 evaluations (error
  $1.3\times10^{-4}$), because a multistep inner solver restarts at first order
  and loses its error history after every reset (§5.1.3).
- **Large-scale demonstration** (3D reacting compressible Euler on Summit, weak
  scaling to 24,000 MPI ranks, explicit MIS "RK3" slow advection with rank-local
  DIRK chemistry): the multirate run takes about 10–45 s against about
  2,000–3,000 s for an IMEX ARK4(3)7L[2]SA1 run (values read from Fig. 3), because
  the expensive advection is evaluated far less often and global
  `MPI_Allreduce` synchronizations occur only at the slow scale (§5.2). The IMEX
  panels span 24–5,184 ranks, the multirate ones 24–24,000.

Among PETSc TS, Trilinos Tempus and DifferentialEquations.jl, Reynolds et al.
(2023, §1) state that only [PETSc TS](/software/petsc-ts.md) supported multirate
methods (a second-order multirate partitioned Runge–Kutta method), as of 2022.

## Relation to other multirate methods

- [Multirate GARK](/methods/multirate-gark.md) methods fix the fast base method and
  the number of micro steps; MRI methods leave the inner solver free and treat the
  fast problem as exactly solvable.
- Lie–Trotter and Strang–Marchuk [splittings](/methods/operator-splitting.md) with
  an exactly solved fast sub-flow are the first- and second-order members of the
  infinitesimal idea; Chinomona & Reynolds (2021, §1) use them as baselines.

## Qualifications

- Every order statement assumes the fast problem is solved exactly or with at
  least the target order; measured rates on stiff semi-discretizations fall below
  design order.
- Reynolds et al. print the forcing with a factor $1/\Delta c_i$ and replace
  $\Delta c_i=0$ stages by ARK stages without stating the limit; the limit is
  the coefficient $\sum_k\gamma^{(k)}_{ij}/(k+1)$ given above.
- Gardner et al. (2022, §2.3) write the stage time as $t_n+c_iH_n$ while their step
  starts at $t_{n-1}$; the index is inconsistent as printed.

# Citations

- [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) — §1, §2 (eqs. 2.1–2.2, MRI-GARK-ERK33a), §4.1 (Remark 4.1), §5 (Figs. 2–3).
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §1, §2.3 (algorithm, eq. 11, MIS order conditions), §5.1.3 (Table 2), §5.2 (Fig. 3).
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §2.3 (auxiliary fast problem).
- [Roberts et al. (2021)](/sources/roberts-2021.md) — §1 (MRI-GARK and MIS order conditions cited in passing).
