---
type: Method
title: "Multirate infinitesimal methods (MIS, MRI-GARK)"
description: "Multirate infinitesimal methods advance the slow partition with a Runge–Kutta skeleton and reach each slow stage by solving a modified fast ODE forced by a polynomial in time built from slow tendencies; the page covers MIS, MRI-GARK and the stage-restart and exponential members, their order statements, embeddings and multirate step-size adaptivity, and their implementation and performance in ARKODE."
status: established
aliases: [MRI, MRI-GARK, MIS, multirate infinitesimal step method, multirate infinitesimal GARK, infinitesimal multirate, MRIStep]
tags: [multirate, runge-kutta, imex, software]
timestamp: 2026-10-20T05:00:00Z
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
[Roberts et al. (2021)](/sources/roberts-2021.md) (§1, in passing),
[Fish & Reynolds (2023)](/sources/fish-2023.md) (§1) and
[Loffeld et al. (2024)](/sources/loffeld-2024.md) (§2.1). Its IMEX
extensions are [IMEX-MRI-GARK](/methods/imex-mri-gark.md) and the stage-restart
[IMEX-MRI-SR](/methods/imex-mri-sr.md) methods; the
[multirate exponential](/methods/multirate-exponential-methods.md) MERK and MERB
methods are further members.

**Generic step.** Fish & Reynolds (2023, §1) write every member in one template:
$Y_1=y_n$; for $i=2,\dots,s$ solve $v_i'(\theta)=C_if^{\{\mathrm f\}}(\theta,v_i)+r_i(\theta)$ on
a stage interval from an initial value $v_{0,i}$ and set $Y_i$ to its end value; $y_{n+1}=Y_s$.
The method is fixed by the constants $C_i$, the intervals, the initial values and the forcings
$r_i$, linear combinations of the slow tendencies $f^{\{\mathrm s\}}(\cdot,Y_j)$ ($C_i$, $r_i$
page-local). MRI-GARK chains the intervals ($v_{0,i}=Y_{i-1}$ on $[c_{i-1}H,c_iH]$); IMEX-MRI-SR
and MERB restart every stage from $y_n$ on $[0,c_iH]$. The inner problems are solved by
subcycling a one-step method with micro step $H/m$. Multirate GARK methods are explicitly not
infinitesimal.

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

## Stage-restart and exponential members

- **Stage restart.** Fish et al. (2024) start every fast problem at $y_n$ and follow it by a
  diagonally implicit slow correction; this removes the sorted-abscissae requirement and the
  padding stages, simplifies the order conditions to conditions on the slow coefficients alone
  and allows embeddings without extra implicit solves
  ([IMEX-MRI-SR](/methods/imex-mri-sr.md); [Fish et al. 2024](/sources/fish-2024.md), §1.1, §2).
- **Exponential members.** Exponential Runge–Kutta and Rosenbrock stages whose weights are
  combinations of $\phi$-functions are exact solutions of linear fast ODEs with polynomial
  forcing; solving those ODEs by subcycling gives MERK (fixed linear fast operator) and MERB
  (per-step Jacobian as fast operator), of orders up to 5 and 6
  ([multirate exponential methods](/methods/multirate-exponential-methods.md);
  [Luan et al. 2022](/sources/luan-2022.md), Lemma 2.2). Fish et al. (2024, §5) show that MERK
  methods are explicit IMEX-MRI-SR methods.

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

**Inner-solver order.** Luan et al. (2022, Thm. 2.12, Remark 2.13) prove for MERB the bound
$CH^p+CHh^q+Ch^r$ with $q$ the order of the stage solves and $r$ that of the final solve, so
$q\ge p-1$, $r\ge p$ suffice, and state that MRI-GARK requires $q,r\ge p$. Fish & Reynolds (2023,
§2) model the fast error as the global error of the inner method over one macro step,
$\propto(H/m)^{p^{\{\mathrm f\}}}H$ ($p^{\{\mathrm f\}}$ the inner order, page-local).

**Highest order.** MRI-GARK and IMEX-MRI-GARK reach order 4; MERK reaches 5 and MERB 6, which
Luan et al. (2022, §1, §2.4.5) call "the first-ever sixth-order infinitesimal multirate method",
noting that no partitioned-RK-based infinitesimal method exceeded order four because the number
of conditions grows quickly. See *Qualifications* for a statement of a fourth-order ceiling.

**Measured behaviour at scale** ([Loffeld et al. 2024](/sources/loffeld-2024.md), §5–6). On a 3D
methane flame (GRI-Mech 3.0, 53 species, reactions fast, transport slow; $32^3$ cells, constant
steps) the explicit third-order MIS method of Knoth & Wolke with fast explicit Runge–Kutta
methods of orders 2–5 reaches its asymptotic regime at larger steps than multirate spectral
deferred correction (MRSDC), whose convergence is "highly non-monotonic"; at $H=6.25\times10^{-8}$ s
the MRI runs take 173–274 s against 376 s and 833 s for two MRSDC variants, because they need
fewer slow and fast evaluations (Table 2; see [deferred correction](/methods/deferred-correction.md)).
MRI-4 and MRI-5 are asymptotically third order, limited by the slow method, yet show slopes above
four where reactions dominate the error (§5.2). On a stiff-diffusion advection–diffusion–reaction
problem ($128^3$ cells, 512 ranks) IMEX-MRI-GARK3b and IMEX-MRI-GARK4 with ten fast steps per
slow step beat single-rate fourth-order ARK-IMEX, and two-level AMR compounds the gain to about
18× (§6; [IMEX-MRI-GARK](/methods/imex-mri-gark.md)).

## Implementation in ARKODE (MRIStep)

[ARKODE](/software/arkode.md)'s MRIStep implements the third-order MIS method,
all third- and fourth-order MRI-GARK methods of Sandu and all IMEX-MRI-GARK
methods of Chinomona & Reynolds (Reynolds et al. 2023, §2.3). The fast scale is
advanced by an "inner stepper" (ARKStep or user-supplied, e.g. CVODE wrapped
through the Evolve/FullRHS/Reset interface), and each inner problem restarts it
through a "reset". Temporal adaptivity exists only at the fast scale; multirate
step-size adaptivity is called an open research question (§2.3). Loffeld et al. (2024, §4)
describe MRIStep the same way (explicit MIS, explicit and solve-decoupled implicit MRI-GARK,
IMEX-MRI-GARK, ARKStep or a user integrator for the fast scale) and wrap BoxLib and AMReX data in
custom vectors for block-structured AMR.

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

## Embeddings and multirate adaptivity

The MRI-GARK embedding re-solves only the last stage with an alternate forcing, so its cost is
one extra fast solve; Fish & Reynolds (2023, §4.2, §5) know of no other infinitesimal family
with embeddings (as of their writing) and use a post-publication correction of the
MRI-GARK-ERK45a embedding row taken from the arXiv version of Sandu's paper. Fish et al. (2024)
add embedded IMEX-MRI-SR methods.

Against the open question recorded by Reynolds et al. (2023, §2.3), Fish & Reynolds (2023)
adapt the macro step $H$ and the multirate ratio $m$ together, from an error split into slow
and fast parts, with controllers derived from Gustafsson's observer framework and fast-error
estimates accumulated from the inner embedded pair (LASA); on seven test problems their
controllers beat single-rate controllers run at fixed $m$ (details on
[step-size control](/methods/step-size-control.md)). The two statements are not in conflict: the
ARKODE paper describes the software as of 2022, and the controllers are not reported as part of
it.

## Relation to other multirate methods

- [Multirate GARK](/methods/multirate-gark.md) methods fix the fast base method and
  the number of micro steps; MRI methods leave the inner solver free and treat the
  fast problem as exactly solvable.
- Lie–Trotter and Strang–Marchuk [splittings](/methods/operator-splitting.md) with
  an exactly solved fast sub-flow are the first- and second-order members of the
  infinitesimal idea; Chinomona & Reynolds (2021, §1) use them as baselines. Loffeld et al.
  (2024, §2.1) write them as infinitesimal methods with zero forcing, of orders 1 and 2, and
  Fish et al. (2024, §1.1) attribute the order limit to their "initial condition" coupling.
- [Nonlinearly partitioned](/methods/nonlinearly-partitioned-runge-kutta.md) multirate
  methods (MR-NPRK) of Buvoli et al. (2026) are not infinitesimal but leave the fast explicit
  method free, as MRI methods do.
- [Local time stepping](/methods/local-time-stepping.md) splits the unknowns by mesh region
  instead of splitting the right-hand side.

## Qualifications

- Every order statement assumes the fast problem is solved exactly or with at
  least the target order; measured rates on stiff semi-discretizations fall below
  design order.
- Reynolds et al. print the forcing with a factor $1/\Delta c_i$ and replace
  $\Delta c_i=0$ stages by ARK stages without stating the limit; the limit is
  the coefficient $\sum_k\gamma^{(k)}_{ij}/(k+1)$ given above.
- Gardner et al. (2022, §2.3) write the stage time as $t_n+c_iH_n$ while their step
  starts at $t_{n-1}$; the index is inconsistent as printed.
- Luan et al. (2022) bound the inner-solver errors with a bounded fast Jacobian, so their
  constants are not uniform in the fast stiffness (reader's observation on the Source page).
- Loffeld et al. (2024) compare at constant steps on one problem per study and report times
  without units in their AMR table (§6.3); their Table 1 prints two convergence rates that the
  printed errors do not reproduce (reader's check on the Source page).
- Loffeld et al. (2024, §2.2, arXiv v1 of 2022) write that the coupling strategy "currently limits
  MRI approaches to at-best fourth order in time", in contrast to SDC. The "MRI approaches" of
  their paper are MIS, MRI-GARK and IMEX-MRI-GARK (§2.1), all of order at most four, so the
  sentence describes the methods available to them, time-stamped "currently", not a barrier;
  it does not hold for the exponential members: MERK5 of Luan, Chinomona & Reynolds (2020),
  which Loffeld et al. cite among multirate methods but not as an infinitesimal one and which
  Fish et al. (2024, §5) place in an infinitesimal class, and MERB5–6 of Luan et al. (2022),
  which those authors call infinitesimal. Recorded as a
  qualification, not a contradiction: no source asserts an order barrier for infinitesimal
  methods.

# Citations

- [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) — §1, §2 (eqs. 2.1–2.2, MRI-GARK-ERK33a), §4.1 (Remark 4.1), §5 (Figs. 2–3).
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §1, §2.3 (algorithm, eq. 11, MIS order conditions), §5.1.3 (Table 2), §5.2 (Fig. 3).
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §2.3 (auxiliary fast problem).
- [Roberts et al. (2021)](/sources/roberts-2021.md) — §1 (MRI-GARK and MIS order conditions cited in passing).
- [Fish & Reynolds (2023)](/sources/fish-2023.md) — §1 (generic step), §2 (error models), §4.2 (embeddings, ERK45a correction), §4.7, §5.
- [Fish et al. (2024)](/sources/fish-2024.md) — §1.1, §2, §5.
- [Luan et al. (2022)](/sources/luan-2022.md) — §1, Lemma 2.2, Thm. 2.12, Remark 2.13, §2.4.5.
- [Loffeld et al. (2024)](/sources/loffeld-2024.md) — §2.1–2.2, §4, §5 (Tables 1–2, Figs. 3–4), §6 (Fig. 5, Table 9), §7.
