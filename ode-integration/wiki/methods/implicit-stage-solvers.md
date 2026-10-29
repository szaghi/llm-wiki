---
type: Method
title: "Solving the stage equations of implicit Runge–Kutta methods"
description: "How the nonlinear and linear systems of implicit Runge–Kutta stages (and of implicit multistep, two-derivative and Patankar steps) are solved: Newton, Picard, simplified and matrix-free Newton, predictors, tolerances and Jacobian reuse, real-Schur, diagonalization-based and stage-parallel preconditioning, extended block-Jacobi, stage formulations and Rana-type preconditioners, dual time stepping, parallel-in-time solves, positivity-preserving linear solves and solver software."
status: established
aliases: [stage solver, Newton iteration for implicit stages, simplified Newton, modified Newton, IRK preconditioning, stage-parallel preconditioner, implicit predictors, stage-parallel IRK, SPIRK, monolithic multigrid for IRK, Vanka relaxation, Picard iteration for stages, static condensation, frozen-coefficient predictor, block back substitution, extended block-Jacobi preconditioner, BJext, Jacobian-free Newton–Krylov, JFNK, matrix-free Newton–Krylov, inexact SDC, Jacobi iteration for Patankar systems, dual time stepping, pseudo-time stepping, pseudo-transient iteration, Rana preconditioner, IA splitting, Butcher transformed stage variables, stage-value formulation]
tags: [implicit, linear-algebra, stiff, runge-kutta, software, parallel]
timestamp: 2026-10-29T18:13:00Z
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
- **Inexact Newton.** [Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md) solve the coupled
  stage system of fully implicit methods for Navier–Stokes and MHD by Newton with
  Eisenstat–Walker forcing terms, i.e. the linear solve stops once the linearized residual is a
  fraction of the nonlinear one (§3.2); 1.35–2.70 Newton iterations per step suffice on the
  cylinder benchmark (§5.2, Table 6).
- **Picard (fixed-point) iteration.** [Orlando et al. (2025)](/sources/orlando-2025-b.md) solve
  the nonlinear Helmholtz-type pressure equation of each implicit stage of their IMEX scheme for
  low-Mach Euler flow by a Picard iteration with the enthalpy lagged, because the fully implicit
  enthalpy makes the system "strongly nonlinear and difficult to control" (§3.2). The iteration is
  first-order convergent, with experimental order about 1 (1.07 at the first step, 0.84 at the
  200th) and contraction rates 0.01–0.08 (Table 17). At Mach $10^{-1}$ it needs 1, 3 and 5
  iterations for tolerances $10^{-4}$, $10^{-6}$, $10^{-10}$; at Mach $10^{-4}$ one iteration
  suffices regardless of tolerance, so it costs about as much as a linearly implicit scheme there
  (Table 16). The linear pressure systems are solved through a Schur complement with
  Jacobi-preconditioned GMRES, and the symmetric positive definite blocks by CG with geometric
  multigrid (§3.5). Their semi-implicit variant avoids the nonlinear equation: a linearization of
  the internal-energy–pressure relation makes the pressure equation linear for general
  equations of state, and on a cubic-EOS test it saved about 70 % CPU time against the
  semi-implicit scheme that solves the nonlinear equation, with no visible difference
  (§3.4, Fig. 13);
  see [semi-implicit IMEX Runge–Kutta methods](/methods/semi-implicit-imex-runge-kutta.md).
- **Functional (fixed-point) iteration: when it converges.** The founding papers iterate the
  stage equations by substitution. [Butcher (1964)](/sources/butcher-1964.md) (Appendix,
  Thm. 14, Eq. (13)) iterates the stage derivatives as
  $g^{(i)}_N=f\bigl(y_n+h\sum_{j<i}a_{ij}g^{(j)}_N+h\sum_{j\ge i}a_{ij}g^{(j)}_{N-1}\bigr)$
  (page-local $g^{(i)}_N$, the $N$-th iterate of stage derivative $i$), so stage $i$ uses the
  current iterates of the earlier stages, and proves: if $f$ is Lipschitz with constant $L$
  and $\lvert h\rvert<1/(L\mathsf a)$, with $\mathsf a$ (page-local) the largest row sum of
  $\lvert a_{ij}\rvert$ over $j<i$ plus the largest row sum over $j\ge i$, the stage equations
  have a unique solution and the iteration converges to it, by the contraction-mapping theorem
  in the maximum norm. His numerical example, the three-stage Gauss method on $y'=y$ with
  $h=0.3$, converges to ten decimals in 8 iterations from stage derivatives 1 (§5, p. 62).
  [Dahlquist (1963)](/sources/dahlquist-1963.md) (p. 38) states for the trapezoidal rule that
  fixed-point iteration converges, "roughly speaking, only if all eigenvalues of
  $\frac12h\,\partial f/\partial x$ are located inside the unit circle", and that
  under-relaxation extends this to eigenvalues with real part below 1; he therefore proves
  existence and uniqueness of the implicit step by continuation in the step size, not by
  iteration (Lemmas 3.2–3.3). He adds, crediting H. Keller, that a fixed number $j$ of
  iterations can make the error grow without bound even when $\lvert h\,\partial f/\partial x\rvert$
  is small: for $y'=\lambda y$ with $h\lambda$ small and purely imaginary, boundedness depends
  on $j$ modulo 4 (pp. 42–43).
- **Modified Newton with a residual or displacement test.** For the ESDIRK stages of their
  additive pairs, [Kennedy & Carpenter (2003)](/sources/kennedy-2003.md) (§3.2.1,
  Eqs. (34)–(36)) write stage $i$ as $Y_i=y_n+X_i+h\gamma f^{\mathrm I}(Y_i)$, with $X_i$ the
  known explicit and implicit contributions of earlier stages (page-local), and iterate with
  the matrix $I-h\gamma\,\partial f^{\mathrm I}/\partial y$ evaluated at an earlier iterate;
  the iteration stops when the residual or the displacement falls below $c\epsilon$, with
  $\epsilon$ the integration tolerance and $c\approx0.005$ (page-local $c$, $\epsilon$). For large
  systems they point to inexact Newton methods.
- **Newton even for linear stages.** [Zeifang & Schütz (2022)](/sources/zeifang-2022.md) use
  Newton's method on linear problems too, citing Higham for its beneficial effect on the
  achieved accuracy (§3.2.1, not shown). Their corrector stages start so close to the solution
  that round-off prevents meeting a relative Newton tolerance, so an absolute tolerance
  $\lVert\Delta W\rVert_2\le10^{-12}$ is added ($\Delta W$ the Newton increment, page-local; §5.2).
- **Matrix-free Newton–Krylov.** Zeifang & Schütz (2022, §4.2, Eqs. (23)–(24)) replace the
  assembled Jacobian by finite-difference Jacobian–vector products with perturbation
  $\sqrt{\varepsilon_{\mathrm{mach}}}/(\varepsilon\lVert\Delta W\rVert_2)$, scaled by the reference Mach
  number $\varepsilon$ (page-local $\varepsilon$ and $\varepsilon_{\mathrm{mach}}$, machine epsilon), after Knoll–Keyes.
  For their two-derivative stages this costs two (linear flux) or three (nonlinear flux)
  operator evaluations per GMRES iteration, and with right preconditioning it needs nearly the
  same GMRES iterations as the matrix-based solve (Fig. 6). ILU(0) is incompatible with it,
  since it needs the whole matrix.
- **Jacobian-free Newton–Krylov with a tolerance tied to the time error.**
  [Pan et al. (2022)](/sources/pan-2022.md) solve each ESDIRK stage of a high-order DG
  compressible-flow solver in modal coefficient space by Newton from the explicit part of the
  stage, with preconditioned GMRES on finite-difference Jacobian–vector products, a
  low-memory block relaxed Jacobi preconditioner and a GMRES tolerance of $0.05$ times the
  Newton residual, which "has no influence on the temporal accuracy" (§2.1.4, Eqs.
  (19)–(22)). Newton stops when the stage residual falls below $\eta_{\mathrm N}$ times the
  norm of the embedded temporal-error estimate, $\eta_{\mathrm N}=0.1$ (page-local; Eq. (37),
  taken from Birken et al. and Noventa et al.). Linearizing the stage residual, they derive
  the sufficient condition
  $\lVert J(I/h-a_{ii}J)^{-1}r\rVert\le\eta_{\mathrm N}\lVert e\rVert$ for the iteration
  error to stay below the temporal error ($r$ the residual, $e$ the error estimate,
  page-local), which tends to $\lVert r\rVert\le\eta_{\mathrm N}a_{ii}\lVert e\rVert$ as
  $h\to\infty$, with $0.25<a_{ii}<0.45$ in their schemes (§2.3, Eqs. (38)–(45)). On an
  [isentropic vortex](/benchmarks/isentropic-vortex.md) with ESDIRK3, fixed relative
  tolerances $10^{-6}\lVert v_0\rVert$ or $10^{-3}\lVert r_0\rVert$ degrade the temporal order,
  $10^{-10}$ or $10^{-7}$ recover it, and the adaptive tolerance gives observed order 3.27
  (§3.1.1, Fig. 2). The tolerance is the iterative leg of their balanced
  [step-size control](/methods/step-size-control.md).
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
methods from the dense output of the compound step (§4). Abu-Labdeh et al. (2023, §3.2) start
Newton from the previous step's stage derivatives.

Kennedy & Carpenter (2003, §3.2.2, Eqs. (37)–(38)) predict stage $i$ of step $n+1$ by
evaluating the previous step's [dense output](/methods/dense-output.md) at
$\theta_i=1+rc_i$, $r=h_{n+1}/h_n$ (page-local $\theta_i$), i.e. by extrapolating beyond the
previous step; for large $r$ the trivial guess "may be more prudent". For ARK4(3)6L[2]SA they
choose the second-order dense output for extrapolation, for stability of the extrapolant at
$\theta>1$, and the third-order one for interpolation (§5, Tables 5–7). With ARK4(3)6L[2]SA the extrapolated
starting values give a uniform speedup over the trivial guess for stiffness parameters from 1
to $10^{-6}$ on a reacting-shock problem (§8.5, Table 16); see
[Kennedy–Carpenter ARK methods](/methods/kennedy-carpenter-ark-methods.md).

**Predictors that freeze the nonlinear coefficients.** A predictor can do more than
supply the initial guess. In the implicit finite-volume scheme
[Quinpi](/methods/quinpi.md) of [Puppo et al. (2024)](/sources/puppo-2024.md) the stage
equations of a third-order SDIRK carry two nonlinearities, the physical flux and the
solution-dependent CWENO reconstruction weights, so the Newton Jacobian is
block-pentadiagonal with entries built from complicated weight expressions, and even a
linear PDE needs a nonlinear solve (§2.2, Eq. (16)). A first-order implicit predictor,
composite backward Euler at the DIRK abscissae with sub-steps $c_k-c_{k-1}$ and a
piecewise-constant reconstruction, is computed stage by stage before the corrector; its
only nonlinearity is the flux and its Jacobian is block-tridiagonal (§3.1, Eqs.
(19)–(24)). Its stage values serve three purposes (§3, Fig. 1):

- the reconstruction weights of corrector stage $k$ are computed from the predictor and
  frozen, so the boundary-extrapolated data are linear in the unknown cell averages and
  the corrector is nonlinear only through the flux, with a Jacobian of the same bandwidth
  whose entries "can now be computed explicitly" (Eqs. (17)–(18), (25)–(27));
- they are the Newton initial guess of the corrector;
- their first-order fluxes are the fallback of the a-posteriori time limiter.

Third-order accuracy survives the freezing if the weights differ from the optimal ones by
$O(\Delta x)$, which the predictor-based weights satisfy asymptotically (§3.2.1, Table 1).
The linear systems are solved by GMRES with ILU(0) inside Newton, with the Rusanov flux
Jacobian approximated by neglecting the derivative of its viscosity coefficient (§4). Puppo
et al. contrast this with the explicit first-order predictor of Gottlieb, Mullen & Ruuth,
which confines the method to small Courant numbers (§1, §3), and outline (not test) the
same freezing for characteristic-variable reconstructions (Remark 2).

## Stage formulations

The same Runge–Kutta step can be posed in different unknowns, which changes the structure
of the Newton system. [Kirby & MacLachlan (2025)](/sources/kirby-2025.md) (§2.2–2.3) offer
three in [Irksome](/software/irksome.md):

- **Stage derivatives** $k_i$, the original Irksome form: every block of the Jacobian couples
  the nonlinearity of one stage to all stages, $s^2$ nonlinear blocks to assemble.
- **Butcher's transformed variables** $w=(A\otimes I)k$ (Butcher 1976, as recalled), for
  invertible $A$: the stage equations become
  $\sum_j(A^{-1})_{ij}w_j-f(t_n+c_ih,y_n+hw_i)=0$, so the coupling sits in the linear term and
  the nonlinear contribution to the Jacobian is block diagonal, $s$ blocks instead of $s^2$
  (Eqs. (2.18)–(2.19)). Any factorization $A=A_1A_2$ with $A_2$ invertible allows $w=A_2k$;
  the authors know no other useful one. For the linear heat equation the system becomes
  $(A^{-1}\otimes M)\mathbf w+h(I\otimes K)\mathbf w=\mathbf f$, the form also used by Munch et
  al. below (Eqs. (3.1)–(3.2); page-local stiffness $K$).
- **Stage values** $Y_i$ (Eqs. (2.20)–(2.21)), with an update that needs one mass-matrix
  solve in finite elements, skipped automatically for
  [stiffly accurate](/properties/stiff-accuracy.md) tableaux, where $y_{n+1}=Y_s$.

For the heat equation the differences are small, with a slight preference for the
transformed variables with stage derivatives; for Navier–Stokes the transformed variables
with stage values needed fewer iterations and were used (§4.1–4.2). A dedicated DIRK path
builds one single-stage problem and reuses it for all stages (§2.3).

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

## Fully implicit methods: diagonalization and stage parallelism

[Munch et al. (2024)](/sources/munch-2024.md) solve the Radau IIA stage system of the linear
finite-element problem $M\dot u+Ku=g$ (page-local stiffness $K$, load $g$) in the form obtained by
multiplying with $A^{-1}\otimes I$,

$$\big(A^{-1}\otimes M+h\,I_s\otimes K\big)\mathbf k=\mathbf r$$

(§2, Eq. (1)), by GMRES with one of two preconditioners whose blocks are independent:

- **Exact complex diagonalization** (Butcher 1976, as recalled): $A^{-1}=S\Lambda S^{-1}$ turns the
  system into blocks $\lambda_iM+hK$, $\lambda_i$ the eigenvalues of $A^{-1}$ (page-local $S$,
  $\Lambda$), with $\lceil s/2\rceil$ independent blocks for Radau IIA because the complex ones come
  in conjugate pairs (§2, Eq. (2)). Each complex block is written in real $2\times2$ form and
  preconditioned by PRESB, whose factorization needs two V-cycles on $(\operatorname{Re}\lambda_i+\operatorname{Im}\lambda_i)M+hK$,
  or by geometric multigrid on the $2\times2$ system, each block with its own GMRES (§6,
  Eqs. (9)–(11)).
- **Axelsson–Neytcheva preconditioner**: factor $A^{-1}=LU$ with $U$ unit upper triangular
  (page-local $L$, $U$), so that all eigenvalues of $L^{-1}A^{-1}$ equal one, and use
  $L\otimes M+hI_s\otimes K$; $L$ has a real eigendecomposition, giving $s$ real blocks
  $\tilde\lambda_iM+hK$, each approximated by one matrix-free geometric multigrid V-cycle
  (§2, Eq. (3)).

The blocks are solved concurrently on $s$ process subgroups of a stage-by-partition process grid;
the products $(D\otimes I)u$ with a $s\times s$ matrix $D$ (page-local), needed for basis changes,
are done by a Cannon-like ring of `MPI_Sendrecv_replace` steps (§3, Eqs. (4)–(6)). A performance
model gives $T_{\mathrm{serial}}=2T_S+\sum_iT_{B_i}$ against
$T_{\mathrm{parallel}}=2T'_S+\max_iT_{B_i}(N/s)$ (page-local: $T_S$ basis-change and $T_{B_i}$
block times, $N$ processes), so the speedup is at most $\sum_iT_{B_i}/\max_iT_{B_i}\le s$ and appears
only at the strong-scaling limit, where times are proportional to iteration counts (§4,
Eqs. (7)–(8)). Measured on SuperMUC-NG for a 3D heat equation up to 147,456 processes (§5):

- GMRES iterations per step with the real preconditioner grow with $s$: 5.0, 7.0, 9.9, 11.9 for
  $s=2,4,6,8$; the sequential V-cycle count falls from 103 to 12 for $s=8$ when the blocks run in
  parallel (Table 2). With complex blocks the per-block iteration counts barely depend on $s$
  (PRESB 5.0–6.2), but the complex variant's speedup is about half that of the real one, and both
  stage-parallel variants reach similar minimal times (§6, Figs. 16–17).
- Stage parallelism wins below about $10^4$ unknowns per process and loses about 20 % above
  $10^5$; on average far from the scaling limit it has 13 % lower throughput (§5.3, §7, Fig. 13).
- Running all stages as a multivector in one process group gave only 5–25 % speedup for $s=8$,
  because the intergrid transfer of the library serializes per stage (§5.4).

The authors contrast their stage-coupled preconditioner with Pazner and Persson's stage-uncoupled
block Jacobi, at similar cost because basis changes are cheap, and call the real-Schur approach of
Southworth et al. "inherently stage-serial" (§2, §6).

## Fully implicit methods: monolithic multigrid with stage-coupled relaxation

Abu-Labdeh et al. (2023) solve the stage systems of Gauss, Radau IIA and Lobatto IIIC methods for
incompressible Stokes, Navier–Stokes and visco-resistive MHD, index-2 saddle-point
[DAEs](/definitions/differential-algebraic-equation.md), monolithically (§4):

- **Outer iteration.** Newton with Eisenstat–Walker forcing, FGMRES (preferred to right-preconditioned
  GMRES because it saves a preconditioner application and allows GMRES inside the smoother), one
  geometric multigrid V-cycle as preconditioner.
- **Transfer and coarse levels.** Interpolation acts on each stage separately, $I_s\otimes P$ with the
  finite-element interpolation $P$ (page-local), restriction is its transpose, coarse operators are
  rediscretized, and the coarsest level is solved by MUMPS (§4.1).
- **Relaxation.** Additive Vanka patches, one per vertex, containing all degrees of freedom in the
  closure of the adjacent cells, only the pressure (and multiplier) degree of freedom at the vertex,
  and **all stage copies** of these, so each patch problem is a small stage-coupled saddle-point
  system (§4.2, Fig. 1). The patch smoother is accelerated by Chebyshev iteration with hand-tuned
  intervals or by GMRES; GMRES is better at high Reynolds number, Chebyshev at Reynolds number 1,
  where GMRES-accelerated relaxation sometimes failed (§5.4).
- **Why monolithic.** Block preconditioners need a Schur complement of the stage-coupled system that
  "may depend on properties of the specific IRK scheme"; the patch smoother avoids it (§4.2).

Results (Firedrake, [Irksome](/software/irksome.md), PETSc/PCPATCH, Niagara cluster): on 2D Stokes,
8.70–25.97 linear iterations per step from 1.1M to 19M unknowns per stage, with the stopping
tolerance falling by a factor 8 per level; weak scaling in wall time is not ideal (about 3.5× per
level against an ideal 2×), which the authors attribute to iteration growth, memory bandwidth and a
communication-bound coarse solve (§5.1, Tables 1–2). On the cylinder benchmark at Re 100, 1.61–8.19
linear iterations per step up to 46.6M unknowns on 640 cores (§5.2, Tables 5–6); on 2D MHD island
coalescence with Lobatto IIIC(2) up to Reynolds number 20,000, under about 10 linear iterations per
step, slightly more than the authors' earlier BDF2 solver (§5.3, Fig. 6).

## Coupled multiphysics: all-stage Newton with static condensation

For incompressible fluid–structure interaction, [Taddei et al. (2026)](/sources/taddei-2026.md)
apply Radau IIA to the full system and solve all stages together, without stage decoupling (§3):

1. The structural velocity stages are eliminated through the Butcher inverse,
   $\mathbf U_s=h^{-1}(A^{-1}\otimes I)\mathbf D_s-h^{-1}\big((A^{-1}\mathbf 1)\otimes I\big)d_n$
   (page-local stacked velocity and displacement stages $\mathbf U_s$, $\mathbf D_s$, start value
   $d_n$), which requires invertible $A$ (Eq. (18)).
2. The resulting system has the structure of the BDF–Newmark system with $s$ times more unknowns
   (§3.1, Eq. (19)). Each Newton step expresses the fluid and solid interior updates through the
   interface displacement increment and solves a Schur-complement (static-condensation) system for
   it (§3.2, Eqs. (23)–(24)).
3. This Newton step equals a sequential-quadratic-programming step for minimizing the interface
   residual subject to the subdomain equations, a formulation that extends to non-conforming
   interface grids (Eq. (25)).

The authors note that the cost of the all-stage system, which has limited fully implicit methods
in high-fidelity fluid–structure codes, matters much less in their reduced-order model, where
port reduction permits direct solvers (§1.2). No timings are reported.

## Structured direct solves for local space–time predictors

The element-local space–time predictor of ADER-DG for a linear system with a stiff
source is a linear system of $Q\,B\,(N+1)$ unknowns per element and step, with $Q$ fields,
$B=\binom{N+3}{3}$ spatial basis functions of degree $\le N$ and $N+1$ temporal ones
(page-local; [Wolf et al. (2022)](/sources/wolf-2022.md), §4.3, Eqs. (6)–(8); see
[ADER](/methods/ader-time-integration.md)). For poroelasticity ($Q=13$) this is 390
unknowns at $N=2$ and 7,644 at $N=6$ (Table 2 prints $7.64\cdot10^3$), and stored LU factors take 1.16 to 446 MB per
element for $N=2,\dots,6$. Wolf et al. replace the factorization by a block back
substitution built on two structural facts:

1. **Lemma 1 (proved).** For an orthogonal spatial basis ordered by non-decreasing degree,
   the stiffness matrices $\int\phi_k\partial_\alpha\phi_l$ are block upper triangular by
   degree, because $\partial_\alpha\phi_l$ has lower degree than $\phi_l$ and is orthogonal to
   every basis function of degree at least that of $\phi_l$ (§5.1). The predictor system is
   then block upper triangular in the spatial modes (Fig. 2).
2. The source matrix $E$ of the physics is upper triangular (§3.2, Fig. 1).

Back substitution over the spatial modes (Algorithm 1) and then over the fields, after
splitting $hE$ into diagonal and strictly upper parts (Algorithm 2), leaves $BQ$ solves of
size $(N+1)\times(N+1)$ with 13 precomputed inverses, chained by small matrix products;
Algorithm 3 fuses all modes of one degree into code-generated small GEMMs (§5.2). Against
forward and back substitution with stored LU factors, the flop count falls by 5.08, 9.52,
14.5, 19.7 and 24.8 times for $N=2,\dots,6$, and storage by $2.42\times10^2$ to
$5.08\times10^4$ times (Table 2). On SuperMUC-NG the kernels run at about 40 % of the
roofline, up to 1,406.7 GFLOP/s per node at $N=6$, which the authors estimate as about 10
times faster than an ideally performing LU solve (§7.2). The method applies to any linear
hyperbolic system whose stiff source matrix is upper triangular, such as viscoelastic
attenuation or damped Maxwell equations (§8.4, stated).

## Factored rational solves for linear second-order systems

For linear structural dynamics $M\ddot u+C\dot u+Ku=f$, [Song & Eisenträger (2022)](/sources/song-2022.md)
apply a rational approximation $\hat D_m(\mathcal A)^{-1}\hat N_m(\mathcal A)$ of the exponential
of the scaled state matrix $\mathcal A$ through its factored denominator $\prod_i(r_iI-\mathcal A)$
(page-local symbols of [Padé time integration](/methods/pade-time-integration.md)). Each real root
costs one solve with the sparse symmetric positive definite matrix $r^2M+rhC+h^2K$ of the original
size; each conjugate pair costs one complex symmetric solve with the same matrix form, from which
the real result is $-\operatorname{Im}\upsilon/\operatorname{Im}r$ ($\upsilon$ the complex solution);
$\mathcal A$ is never formed and $M$ never inverted, and factorizations are reused across steps
for linear problems (§2.3). For Gauss methods the roots $r_i$ are the eigenvalues of $A^{-1}$, so
this is the complex diagonalization above specialized to a second-order system *(compiler remark,
not in the sources)*.

## Two-derivative stages: extended systems and element-wise preconditioning

Implicit [multiderivative methods](/methods/multiderivative-runge-kutta.md) use $\dot f$ as well
as $f$. In the two-derivative deferred-correction scheme of Zeifang & Schütz (2022), every
predictor and corrector stage has the form

$$W-a_1h\,f(W)+\frac{a_2h^2}{2}\,\dot f(W)=b,$$

with $a_1=\Delta c/2$, $a_2=\Delta c^2/6$ in the predictor ($\Delta c$ the abscissa increment) and
$a_1=a_2=1$ in the corrector ($a_1,a_2,W,b$ page-local; §2.2, Eqs. (7)–(9)). To avoid the step
restriction that a direct spatial discretization of the second derivative caused in earlier work,
an auxiliary variable $V:=f(W)$ (page-local) is carried, $\dot f$ is discretized as a function of
$(W,V)$, and Newton acts on the doubled state $(W,V)$ (§3.2.1, Eqs. (17)–(18)). With $J=\partial f/\partial W$,
the extended Jacobian is

$$\begin{pmatrix}I-a_1hJ+\frac{a_2h^2}{2}\,\partial_W\dot f & \frac{a_2h^2}{2}\,J\\ -J & I\end{pmatrix},$$

because the discrete derivative of $\dot f$ with respect to $V$ equals $J$; the "Hessian" term
$\partial_W\dot f$ vanishes for linear fluxes and is assembled from flux Hessians otherwise
(§3.2.1–3.2.2). Two solver strategies are compared on a discontinuous Galerkin spectral element
discretization (FLEXI, PETSc GMRES):

- **Schur complement.** Eliminating $V$ halves the size but gives
  $I-a_1hJ+\frac{a_2h^2}{2}\partial_W\dot f+\frac{a_2h^2}{2}J^2$, with the square of the
  discretization Jacobian. It helps only at small steps; at large steps the GMRES iteration count
  "suddenly increases very rapidly and leads to non-convergence", with ILU(0) or block-Jacobi
  preconditioning alike (§3.2.4, §4.1, Figs. 2–3).
- **Extended block-Jacobi (BJext).** Element-local $2\times2$ blocks of the extended Jacobian,
  neighbour coupling dropped, with a closed-form inverse that needs one LU factorization per
  element of $I-a_1hJ_i+\frac{a_2h^2}{2}J_i^2$ ($J_i$ the element block). Dropping the Hessian
  term from the preconditioner (but keeping it in the system matrix) makes the blocks commute,
  needs only the backward-Euler-type element Jacobian, and costs almost no extra iterations
  (§3.2.3, Fig. 1).

On linear advection and on the Euler equations at reference Mach numbers $1$, $10^{-1}$, $10^{-2}$
($16^2$ elements, degree 5), GMRES iteration counts rank BJext $\approx$ BJext with Hessian $<$
ILU(0) $<$ no preconditioner, while standard element-wise block-Jacobi was *worse* than no
preconditioner; counts grow with stiffness. In wall-clock time BJext is the most efficient at
large steps, no preconditioner at small steps, and ILU(0) gains from larger steps "in only a few
cases" (§4.1, Figs. 4–5). BJext needs no inter-process communication in its application (§4.2).
Keeping the Hessian in the system matrix is needed for iteration counts linear in the step at
very large steps (Fig. 3). With BJext and matrix-free products the scheme ran a 3D Taylor–Green
vortex at about 200 times the explicit step (§5.3.3).

## Parallel-in-time solves of implicit steps

Two families of [parallel-in-time integration](/methods/parallel-in-time-integration.md) are,
at heart, solvers for implicit time-stepping systems:

- **All steps at once (ParaDiag).** For backward Euler or BDF on $y'=Ly+g$ with constant step,
  [ParaDiag](/methods/paradiag.md) writes all $N$ steps as one space-time system, and
  [Gander & Palitta (2024)](/sources/gander-2024.md) reduce it by an FFT in time and the
  Sherman–Morrison–Woodbury formula to $N$ independent **complex shifted** solves
  $((1-\omega_i)I-hL)x_i=r_i$, with $\omega_i$ the roots of unity (page-local), plus one
  $d\times d$ capacitance system solved by a Galerkin method on the Krylov space of $L$ whose
  reduced systems serve all shifts at once (§2–3, Algs. 2.1, 3.1). For symmetric positive
  definite $-L$ the capacitance matrix has condition number at most $1+1/(h\lambda_{\min}(-L))$
  (Thm. 3.1; on gaps in the printed proof see [ParaDiag](/methods/paradiag.md)). Shifted Krylov solvers for the inner solves are mentioned but not used (§3).
  This is the time-direction analogue of the complex diagonalization of the stage system
  above *(compiler remark)*.
- **Iterated collocation with a diagonal preconditioner (diagonal SDC).** Instead of the coupled
  $\mathsf Md$-dimensional collocation system, an SDC sweep solves $\mathsf M$ systems of size $d$
  ([Saupe et al. (2025)](/sources/saupe-2025.md), §2.1); with a diagonal $Q_\Delta$ they are
  independent and run in parallel ([diagonal SDC](/methods/parallel-sdc.md);
  [Čaklović et al. (2025)](/sources/caklovic-2025.md), §2.1). The sweep is a preconditioned
  fixed-point iteration for the [fully implicit](/methods/fully-implicit-runge-kutta.md)
  collocation step, so the number of sweeps $K$ plays the role of an outer iteration count.
  Čaklović et al. solve each node system by exact Newton up to the problem tolerance or 300
  iterations, and model one Newton iteration as costing about one right-hand side because their
  Jacobians are inverted analytically (§4.1). Saupe et al. use **inexact SDC**: the Newton
  tolerance is a fixed fraction of the current SDC residual ($10^{-5}$ for van der Pol, $10^{-1}$ for
  a quench problem) or the inner iterations are capped (9 and 5), which only their residual-driven
  adaptivity allows, since the increment-based variant needs the exact order of every sweep
  (§2.1).

In Parareal, the implicit solves sit inside the propagators: [Jin et al. (2025)](/sources/jin-2025.md)
solve the fully implicit Lobatto IIIC or Radau IIA stages of their fine propagator by Newton and
use a semi-implicit coarse propagator that needs one linear solve per step, with the nonlinear
reaction explicit (§4.2, Eq. (4.3)).

## Linear solves that must keep positivity

Patankar-type schemes ([modified Patankar methods](/methods/modified-patankar-methods.md)) are
linearly implicit, and their positivity rests on the solution of the linear system, so the
linear solver must not destroy it:

- **Jacobi iteration.** In the modified Patankar deferred-correction scheme for the water height
  of the shallow water equations, [Ciallella et al. (2022)](/sources/ciallella-2022.md) solve one
  sparse system per correction and subnode, with at most five nonzeros per row, by Jacobi
  iteration started from the right-hand side. Jacobi converges on this matrix and keeps every
  iterate positive, while Krylov methods "in general do not preserve positivity" (§5.1,
  Remark 5.1). It needs "usually 10–20 iterations", 40 in the worst cases, nearly independent of
  the mesh and growing with the CFL number, and takes about 10 % of the run time, with an
  overall overhead of about 18 % over explicit deferred correction at equal CFL (§5.1, §6.1,
  §6.6, Figs. 6, 15). The diagonal of the matrix is at least one and the off-diagonals are
  nonpositive (Eq. (30)), which is why Jacobi from a positive start stays positive *(compiler
  check, not in the source)*.
- **One extra factorization per step.** The Patankar predictor–corrector of
  [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) post-processes an SDIRK step with
  one linear solve with $I-h\bar G$, an M-matrix built from the stages (page-local $\bar G$), so
  it costs one LU factorization per step in addition to the nonlinear stage solves, which the
  authors count as an extra MPRK-type stage; MPRK methods need one LU per stage (Remark 3.22).
  They propose, as future work, reusing $\bar G$ as the approximate Jacobian of the next step's
  nonlinear solve (§6).

## Multistep methods: one solve per step

- **Linearly implicit multistep methods.** [Glandon et al. (2022)](/sources/glandon-2022.md) add a
  Jacobian term to a linear multistep method so that each step needs exactly one linear solve with
  $I-h_n\kappa_kJ_n$ (page-local coefficient $\kappa_k$, the source's $\mu_{-1}$, playing the
  role of the Rosenbrock $\gamma$), instead of the Newton iteration of BDF (§2, Def. 2.2). Their implementation is slightly
  faster in CPU time than a BDF implementation in the same framework on 2D Gray–Scott (direct LU)
  and a quasi-geostrophic model (GMRES with tolerance one tenth of the integrator's); with GMRES the
  error–step curves are jagged at loose tolerances, which the authors attribute "possibly" to
  inexact solves degrading stability or causing order reduction (§8.2–8.3). See
  [linearly implicit multistep methods](/methods/linearly-implicit-multistep-method.md).
- **Factorization reuse by iterative refinement.** [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md)
  solve the one linear saddle-point system per step of their IMEX and semi-implicit BDF2
  Navier–Stokes schemes by iterative refinement with a factorization from an earlier step, starting
  from an extrapolated guess, and refactor after five iterations without convergence (§4). The
  number of LU factorizations is at most about 5 % of the steps on their manufactured test (§4.1,
  Fig. 4), and 53–92 factorizations for 4,384 to 93,671 steps on the cylinder benchmark (§4.2). See
  [backward differentiation formulas](/methods/backward-differentiation-formula.md).

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

Kirby & MacLachlan (2025, §3) extend the menu, in the transformed form
$(A^{-1}\otimes M)+h(I\otimes K)$:

- **Block Jacobi and block Gauss–Seidel** (Staff, Mardal, Nilssen): from the additive split
  $A=L_A+D_A+U_A$ (strictly lower, diagonal, strictly upper; page-local),
  $P_D=(D_A^{-1}\otimes M)+h(I\otimes K)$ and $P_L=((L_A+D_A)^{-1}\otimes M)+h(I\otimes K)$,
  with diagonal blocks $a_{jj}^{-1}M+hK$ approximated by one BoomerAMG cycle (Eqs.
  (3.3)–(3.4)). Outer iteration counts grow with $s$ even with exact block solves.
- **Rana-type preconditioner**: from the multiplicative factorization $A=\tilde L\tilde D\tilde U$
  (unit lower, diagonal, unit upper; page-local), replace $A$ by the lower-triangular
  $\tilde L\tilde D$, $\tilde P_{LD}=((\tilde L\tilde D)^{-1}\otimes M)+h(I\otimes K)$, which needs
  only diagonal-block solves (Eq. (3.5); after Rana et al. and Clines et al.). Irksome
  implements it generically, through `firedrake.AuxiliaryOperatorPC`, by rebuilding the
  stage form with $\tilde L\tilde D$ in place of $A$, so it applies to nonlinear problems too.
- **Monolithic multigrid** with additive Schwarz relaxation on patches that contain all
  stage copies of a vertex patch, $\mathbf V_i=V_i\times\dots\times V_i$ (Eq. (3.8)), as in
  Abu-Labdeh et al. above. Kirby (2024), as recalled, proves that if single-stage multigrid
  with this relaxation converges, possibly with a complex step, the stage-coupled one
  converges with a spectral radius not depending explicitly on $s$ (§3.2).
- **Not supported**: the eigendecomposition-based preconditioners of Southworth et al., whose
  nonlinear form does not map onto PETSc's nonlinear solvers, and the SVD-based ones of
  Leveque et al., which are problem-specific and linear only (§3.1).

Measured on the heat equation (Fig. 5, 8 cores; values read from the plot): GMRES
iterations per step at $s=4$ about 47 ($P_D$), 22 ($P_L$), 10 ($\tilde P_{LD}$) and 7 for a
DIRK with the same stage count, and run times about 180, 95, 43 and 40 s, all about 5 s at
$s=1$; the Rana iteration counts are "empirically independent of the number of RK stages"
(§4.1). On flow past a cylinder (Mardal–Tai–Winther elements, Newton–Krylov with
Eisenstat–Walker forcing, FGMRES with geometric multigrid V(3,3) cycles and Vanka
relaxation) Newton and Krylov counts are stable in $s$; Rana is faster for two- and
three-stage Radau IIA, monolithic multigrid for four stages, attributed to fewer hierarchy
traversals and higher arithmetic intensity; four-stage Radau IIA costs slightly less than
four times one stage, and DIRKs with $s$ stages run in about the time of $s$-stage Radau IIA
(§4.2, Figs. 8–9). On Cahn–Hilliard, monolithic multigrid is faster at small steps and Rana
at large ones (§4.3). See [flow past a cylinder](/benchmarks/flow-past-cylinder.md) and
[Cahn–Hilliard equation](/benchmarks/cahn-hilliard-equation.md).

## Stage systems of fully implicit–explicit polynomial methods

The implicit equations of the [FIMEX-Radau methods](/methods/polynomial-time-integrators.md)
are those of Radau IIA with a modified right-hand side, so fully implicit solvers apply
unchanged ([Buvoli & Southworth 2023](/sources/buvoli-2023.md), §5). On DG
advection–diffusion they wrap hypre's BoomerAMG in the block preconditioning of Southworth
et al. (§6.3); on Fourier-spectral KdV the linear implicit part is diagonal, so the
$s\times s$ inverses per mode are precomputed (§6.1.1). The iterator sweeps that follow the
propagator solve a system of the same structure, typically much faster because the
propagator supplies a very good initial guess (§5.2). Their DIRK comparators use simplified
Newton with 4–10 iterations per stage (§6.3.2).

## Dual time stepping

**Dual (pseudo-)time stepping** solves the nonlinear system of an implicit physical step by
marching a pseudotime derivative to steady state. [Sayyari & Yamaleev (2026)](/sources/sayyari-2026.md)
use it for BDF1 and BDF2 in a positivity-preserving entropy-stable spectral-collocation
solver for compressible Navier–Stokes (§4, §7). With pseudo-step $\delta$ and iterate
$y^{(m)}$ (page-local), the BDF1 equation $y_{n+1}=y_n+hf(y_{n+1})$ is iterated as

$$y^{(m+1)}=y^{(m)}+\delta\Big(-\frac{y^{(m+1)}-y_n}{h}+f(y^{(m)})\Big)
\quad\Longleftrightarrow\quad
y^{(m+1)}=C_1\Big(y^{(m)}+\frac{\delta}{h}y_n+\delta f(y^{(m)})\Big),\qquad C_1=\frac{h}{h+\delta},$$

i.e. the mass term is point-implicit and the residual explicit (Eqs. (9)–(13)); a fixed
point is the BDF1 solution. For BDF2,
$y^{(m+1)}=C_2\bigl(y^{(m)}+\frac{2\delta}hy_n-\frac\delta{2h}y_{n-1}+\delta f(y^{(m)})\bigr)$ with
$C_2=\frac{2h}{2h+3\delta}$ (Eqs. (23)–(24)). Since $0<C_1,C_2<1$, every iteration is a
scaled forward-Euler step from a combination of admissible states, so explicit positivity
proofs carry over:

- **Theorem 1** (density): with the first-order positivity-preserving density flux, $\rho^{(m+1)}>0$
  whenever $\delta$ is below the inverse of the forward-Euler bound term minus
  $\rho_n/(h\rho^{(m)})$, and without restriction when that difference is not positive
  (Eq. (16)); the pseudo-step bound therefore exceeds the forward-Euler one.
- **Internal energy**: positivity reduces to a quadratic in $\delta$ with positive constant
  term, so an admissible $\delta>0$ exists (Eqs. (18)–(19), (26); proof referred to earlier
  work).
- The variant with the BDF unknown at the old pseudo level has a *stricter* density bound
  than explicit Euler and is discarded (Remark 1, no derivation shown).
- High-order accuracy comes from element-wise convex flux limiting inside the same update
  (Eq. (22)); see [bound-preserving flux limiting](/methods/bound-preserving-flux-limiting.md)
  and [positivity preservation](/properties/positivity-preservation.md).

The authors contrast this with standard nonlinear solvers, which do not keep positivity at
each iteration (§1). Results: on a Mach 2.15 shock/boundary-layer interaction, steady-state
convergence nearly twice as fast as explicit forward Euler with $\delta$ three times the
forward-Euler step; at Mach 6.85 no gain, because the temperature constraint, which "is sharp and cannot be
relaxed", bounds $\delta$; on a Mach 10 Taylor–Green vortex BDF2 runs physical steps on
average 20 times those of SSPRK3 and saves about 30% wall-clock time at degree 6 on $64^3$
elements (§8.2–8.4; no hardware stated). See
[backward differentiation formulas](/methods/backward-differentiation-formula.md).

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
- **One operator per stage, multigrid per stage.** In an IMEX pair whose implicit part is an
  SDIRK, the stage matrix $I-ha_{ii}J$ with the Jacobian frozen at $t_n$ is the same at every
  stage, which is why all the recommended pairs of [Ascher et al. (1997)](/sources/ascher-1997.md)
  are SDIRK-based (§2). On a 2D viscous Burgers-type system with diffusion implicit they solve
  each stage's symmetric positive definite system by multigrid V(1,1) cycles to a residual
  tolerance of 0.003 and count fine-grid iterations (§5, Table 1). They state that the strongly
  damping L-stable pairs need the fewest iterations per stage at large viscosity and that weakly
  damping ones need more because "lingering high-frequency modes necessitate more work on the
  finest grid", most visibly the IMEX midpoint pair (1,2,2), which needs 3.13, 3.29, 3.68
  iterations at viscosities 0.03, 0.04, 0.05. The printed averages over viscosities 0.01–0.05 are
  2.58–3.90 for (2,2,2), 3.58–5.87 for (3,4,3), 4.77–7.84 for (4,4,3), 3.68–4.42 for (2,3,3) and
  2.23–3.68 for (1,2,2). The table is introduced as iterations "at each time step" but discussed
  per stage.
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
- Munch et al. (2024, §6) write Southworth et al.'s conjugate-pair blocks as
  $(\operatorname{Re}\lambda_iI-hM^{-1}K)^2+\operatorname{Im}\lambda_iI$, without the square on the
  imaginary part that the quadratic form needs *(compiler check, not in the sources)*. They assert without
  proof that the eigendecomposition of the triangular factor $L$ is real (§2), which holds when its
  diagonal entries are real and distinct. Their stage-system right-hand side carries $+Ku_n$ where
  $M\dot u+Ku=g$ needs $-Ku_n$ (Eq. (1) and before), and they print 786 for the 768 processes of 16
  nodes (§5.1) (arXiv v1).
- Abu-Labdeh et al. (2023) give no convergence theory for the stage-coupled smoother; Chebyshev
  intervals and stopping tolerances are hand-tuned, and no rigorous tolerance guaranteeing
  discretization-level accuracy is available (§5).
- Song & Eisenträger (2022) and Taddei et al. (2026) report no solver statistics beyond costs
  relative to Newmark (Song) or none at all (Taddei).
- Zeifang & Schütz (2022) were read as arXiv v1 (title without "Implicit"); their Eq. (9) omits
  the quadrature term $+I_l$ of the corrector right-hand side that Eq. (6) contains (recorded on
  the Source page). Their finding that standard block-Jacobi is worse than no preconditioner
  concerns the doubled two-derivative system, not ordinary implicit DG stages. Parallel
  performance of BJext is left to future work (§4.2).
- Gander & Palitta (2024) count parallel-in-time loops on a laptop with sequential block solves;
  no wall time is measured (§6). Čaklović et al.'s Newton cost assumption (one Newton iteration
  about one right-hand side) favours implicit methods relative to large-scale settings.
- Ciallella et al. (2022) state no hardware and call their code unoptimized; their cost ratios
  are relative.
- **Pan et al. (2022), Table 1.** The ratios of the adaptive Newton tolerance to the largest
  admissible one are printed as 0.57, 0.14 and 0.31, but the printed columns give 0.57, 1.375
  and 3.15 for the second and third steps. Either the tolerance column is ten times too
  large in those rows, which the text's conclusion ("of the same order of 0.1") requires, or
  the adaptive tolerance exceeds the admissible one there *(compiler check of the printed
  quotients)*.
- **Kirby & MacLachlan (2025)** give the heat-equation solver mesh as $256\times256$ in the
  text and $64\times64$ in the caption of Fig. 5; their iteration and time values are read
  from plots. The Staff et al. ranking of block preconditioners that they recall
  (lower-triangular before block-diagonal before upper-triangular, right preconditioning
  better than left) comes from one model problem (§3.1).
- **Dual time stepping: what the proofs cover.** Sayyari & Yamaleev (2026) prove positivity
  of every pseudo-iterate, not of the converged BDF solution, of which a limit of positive
  iterates guarantees only nonnegativity, and they do not prove convergence of the
  iteration; the pseudo-step keeps an explicit CFL-type bound, so "no constraint on the
  physical time step" holds for the converged solution only (§9 concedes the pseudo-time
  limit). For BDF2 the subtracted term is $(2\rho_n-\frac12\rho_{n-1})/(h\rho^{(m)})$, positive
  only when $4\rho_n>\rho_{n-1}$, so the claim that the bound exceeds the forward-Euler one
  is not guaranteed for BDF2 when the density drops by more than a factor 4 in one step
  *(compiler check of §7.1)*. Their fully discrete entropy stability is argued for BDF1 only
  and assumes the pseudo-residual below the BDF1 entropy dissipation (§5). The file read is
  arXiv v3.
- The heat-equation comparison of Gardner et al., CVODE BDF 8.8 s against ARKODE's default DIRK
  67.3 s, is problem-specific; the authors attribute it to BDF's single solve per step and order
  adaptivity (§5.1).

# Citations

- [Southworth et al. (2022)](/sources/southworth-2022.md) — §1–2 (Eqs. (1)–(6), Assumptions 1–2), §3 (Eqs. (8)–(13)), §4 (Cor. 1, Thm. 2, Table 1), §5 (Algorithm 1), §6, §7 (Tables 2–7, Fig. 2), App. A.
- [Farrell et al. (2021)](/sources/farrell-2021.md) — §1, §2.3 (Eqs. (31)–(34)), §4.2 (Fig. 3), §4.3.
- [Roberts et al. (2021)](/sources/roberts-2021.md) — §4.1–4.4 (Eqs. (4.1)–(4.5)).
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §2.2, §3.4 (Eqs. (18)–(21)), §5.1.2 (Table 1).
- [Butcher (1964)](/sources/butcher-1964.md) — §5 (p. 62), Appendix (Eq. (13), Thm. 14).
- [Dahlquist (1963)](/sources/dahlquist-1963.md) — p. 38 (Lemmas 3.2–3.3, remark on fixed-point iteration), pp. 42–43 (iterated trapezoidal rule, remark credited to H. Keller).
- [Kennedy & Carpenter (2003)](/sources/kennedy-2003.md) — NASA/TM-2001-211038: §3.2.1–3.2.2 (Eqs. (34)–(38)), §5 (Tables 5–7), §8.5 (Table 16).
- [Ascher et al. (1997)](/sources/ascher-1997.md) — §2 (SDIRK stage operator), §5 (Table 1).
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §2.5, §5 (Eqs. (2)–(3), Table 5), §6 (Table 6), §6.1 (Fig. 3).
- [Munch et al. (2024)](/sources/munch-2024.md) — §1–7 (Eqs. (1)–(11), Table 2, Figs. 5–18).
- [Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md) — §3.1–3.2, §4 (Fig. 1), §5.1–5.4 (Tables 1–7, Figs. 5–7).
- [Taddei et al. (2026)](/sources/taddei-2026.md) — §1.2, §3.1–3.2 (Eqs. (18)–(25)).
- [Song & Eisenträger (2022)](/sources/song-2022.md) — §2.3 (Eqs. (37)–(54)).
- [Glandon et al. (2022)](/sources/glandon-2022.md) — §2 (Def. 2.2), §8.2–8.3.
- [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md) — §4, §4.1–4.2 (Fig. 4).
- [Orlando et al. (2025)](/sources/orlando-2025-b.md) — §3.2, §3.4–3.5, Tables 16–17, Fig. 13.
- [Puppo et al. (2024)](/sources/puppo-2024.md) — §1, §2.2 (Eq. (16)), §3 (Eqs. (17)–(27), Fig. 1, Remark 2), §3.2.1 (Table 1), §4.
- [Wolf et al. (2022)](/sources/wolf-2022.md) — §3.2 (Fig. 1), §4.3 (Eqs. (6)–(8)), §5.1 (Lemma 1, Fig. 2), §5.2 (Algorithms 1–3, Table 2), §7.2, §8.4.
- [Zeifang & Schütz (2022)](/sources/zeifang-2022.md) — arXiv v1: §2.2 (Eqs. (7)–(9)), §3.2.1–3.2.4 (Eqs. (17)–(19), Fig. 1), §4.1–4.2 (Eqs. (23)–(24), Figs. 2–6), §5.2, §5.3.3.
- [Gander & Palitta (2024)](/sources/gander-2024.md) — arXiv v2: §2–3 (Algs. 2.1, 3.1, Thm. 3.1), §6.
- [Čaklović et al. (2025)](/sources/caklovic-2025.md) — arXiv v2: §2.1, §4.1.
- [Saupe et al. (2025)](/sources/saupe-2025.md) — arXiv v2: §2.1 (inexact SDC).
- [Jin et al. (2025)](/sources/jin-2025.md) — arXiv v2: §4.2 (Eq. (4.3)).
- [Ciallella et al. (2022)](/sources/ciallella-2022.md) — arXiv v3: §5.1 (Remark 5.1), §6.1, §6.6 (Figs. 6, 15).
- [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) — CSL-TR-26-1: Remark 3.22, §6.
- [Pan et al. (2022)](/sources/pan-2022.md) — §2.1.4 (Eqs. (19)–(23)), §2.3 (Eqs. (37)–(46)), §3.1.1 (Fig. 2, Table 1).
- [Kirby & MacLachlan (2025)](/sources/kirby-2025.md) — §2.2–2.3 (Eqs. (2.18)–(2.21)), §3.1–3.2 (Eqs. (3.1)–(3.8)), §4.1–4.3 (Figs. 5, 8–9).
- [Buvoli & Southworth (2023)](/sources/buvoli-2023.md) — arXiv v2: §5, §5.2, §6.1.1, §6.3.
- [Sayyari & Yamaleev (2026)](/sources/sayyari-2026.md) — arXiv v3: §1, §4 (Eqs. (9)–(13), Remark 1), §5.1–5.2 (Thm. 1, Eqs. (16)–(19)), §6.2 (Eq. (22)), §7 (Eqs. (23)–(26)), §8.2–8.4, §9.
