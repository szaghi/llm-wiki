---
type: Definition
title: "Differential-algebraic equations and their Runge–Kutta treatment"
description: "A differential-algebraic equation couples differential equations with algebraic constraints, My'=f(t,y) with singular M or semi-explicit form; its index governs which Runge–Kutta, Rosenbrock and BDF methods converge at full order, how stage systems are solved, and which software accepts it."
status: established
aliases: [DAE, index-1 DAE, index-2 DAE, semi-explicit DAE, implicit ODE, singular mass matrix]
tags: [dae, stiff, implicit, order-reduction, software]
timestamp: 2026-10-20T16:00:00Z
---

# Differential-algebraic equations and their Runge–Kutta treatment

A **differential-algebraic equation (DAE)** is a system $My'=f(t,y)$ whose mass matrix $M$ is
**singular** (on this page only), or more generally a fully implicit system
$F(t,y,y')=0$ whose Jacobian with respect to $y'$ is singular. Some components are then defined
by algebraic constraints rather than by differential equations. The **semi-explicit** form
separates differential variables $y$ from algebraic variables $w$ (page-local):

$$y'=f(t,y,w),\qquad 0=g(t,y,w).$$

For the sources, the **index** classifies DAEs by how the constraint determines $w$:

- **index 1**: the constraint can be solved for $w$, i.e. $\partial g/\partial w$ is nonsingular,
  the hypothesis under which [Glandon et al. (2022)](/sources/glandon-2022.md) (Remark 5.10)
  treat semi-explicit index-1 DAEs;
- **index 2**: $0=g(y)$ does not contain $w$ and $g_yf_w$ is nonsingular near the solution
  ([Steinebach 2023](/sources/steinebach-2023.md), §2, Table 4).

Higher-index problems are usually reduced: Steinebach reduces the index-3 pendulum to index 2
by the velocity constraint and to index 1 by the acceleration constraint (§4).

[Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md) (§3.1) use the differentiation
count, after Hairer–Wanner: the index is the number of analytical differentiations needed
to turn the DAE into an explicit ODE. For time-dependent Stokes flow, differentiating the
constraint $\nabla\cdot u=0$ once and taking the divergence of the momentum equation
expresses the pressure through the velocity; a second differentiation gives an ODE for the
pressure, so the system has **index 2**. The same holds for their Navier–Stokes and
incompressible MHD semi-discretizations (§3.2–3.3).

DAEs are "infinitely stiff", so A- and L-stability matter ([Farrell et al. 2021](/sources/farrell-2021.md),
§2.1). They arise in method-of-lines semidiscretizations with constraints: mixed formulations of
the heat equation, incompressible flow (Farrell et al. §2.2, §4.4.1), vorticity–streamfunction
formulations ([Southworth et al. 2022](/sources/southworth-2022.md), §7.2), electrical circuits
and pipe networks (Steinebach 2023, §4).

## Runge–Kutta methods applied to DAEs

A Runge–Kutta method treats both variable groups with the same tableau. In stage-value form,

$$Y_i=y_n+h\sum_j a_{ij}f(t_n+c_jh,Y_j,W_j),\qquad 0=g(t_n+c_ih,Y_i,W_i),$$

with stage values $W_i$ of the algebraic variable (page-local). Southworth et al. (2022, §6,
Eq. (30)) write the same scheme in stage-derivative variables for both $y$ and $w$, with update
$w_{n+1}=w_n+h\sum_ib_i\kappa_i$, $\kappa_i$ the stage derivatives of $w$ (page-local); the two forms coincide when $A$ is invertible *(compiler check, not in the sources)*.

**Order.** Index-2 problems formally limit the order to the
[stage order](/definitions/stage-order.md) (Southworth et al. 2022, §2.1, citing Hairer–Wanner;
Abu-Labdeh et al. 2023, §2, §3.1, citing Hairer–Wanner §VII.4).
That is one reason both groups prefer fully implicit methods, whose stage order is $s$ for Gauss
and Radau IIA, over DIRK methods, whose stage order is "typically limited to 1" (2 for ESDIRK)
(Abu-Labdeh et al. 2023, §2). [Kirby & MacLachlan (2025)](/sources/kirby-2025.md) (§2,
§4.2) repeat the argument for the semi-discrete Navier–Stokes equations, an index-2 DAE: "it
is the so-called stage order of the scheme that matters, and not the global order", DIRKs
being limited to stage order one or two and Radau IIA having stage order $s$. Observed rates
fall short of the classical order in two applications and reach it in a third:

- *Incompressible Stokes* (Abu-Labdeh et al. 2023, §5.1, Tables 1–2), time step halved with
  each mesh refinement: velocity rates 2.5 (two-stage Gauss), 3.0–3.1 (two-stage Radau IIA),
  2.0 (two-stage Lobatto IIIC) and 2.4–3.1 for three stages; Gauss velocity errors are about
  four orders of magnitude larger than Radau IIA's at the finest level
  ($5.6\times10^{-4}$ against $5.0\times10^{-8}$ for two stages). Space and time errors are
  refined together, so the temporal rate is not isolated.
- *Fluid–structure interaction* ([Taddei et al. 2026](/sources/taddei-2026.md), §5.1.1,
  Table 1): Radau IIA with $s=2,3,4$ shows fitted rates of about 2.1, 2.4 and 3.5 against
  the formal $2s-1=3,5,7$. Taddei et al. attribute the shortfall to "the differential
  algebraic structure" of the semi-discrete system together with the spatial discretization,
  the ALE mesh motion and the iterative interface coupling; they do not analyse the index or
  the stage order.

- *Flow past a cylinder* (Kirby & MacLachlan 2025, §4.2, Figs. 9–10; Mardal–Tai–Winther
  elements, Radau IIA with 1–4 stages, Alexander's DIRK, WSODIRK433 and WSODIRK744, reference
  five-stage Radau IIA on the same mesh): for the final and maximal drag and lift the schemes
  "generally exceed the stage-order bound" and reach their formal order; Alexander's DIRK
  under-achieves on maximal drag and one-stage Radau IIA barely converges. The quantities are
  functionals at fixed mesh, not the full space–time error.

**Boundary data as constraints.** Kirby & MacLachlan (2025, §2.1) treat strong Dirichlet
conditions as algebraic equations on the boundary degrees of freedom and impose them on every
stage value, $Y_i=g(t_n+c_ih)$ on the boundary, now the default of
[Irksome](/software/irksome.md); with a stiffly accurate method the step-end value then
satisfies the data at $t_{n+1}$. The earlier default differentiated the condition and imposed
it on the stage derivatives. See
[boundary conditions for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md).

**Stiff accuracy.** With $b^\top$ equal to the last row of $A$, the update equals the last stage,
which satisfies $g=0$, so the update lies on the constraint manifold *(compiler check, not in the sources)*.
Steinebach's Rodas5P makes both its main and its embedded method stiffly accurate (§3); see
[stiff accuracy](/properties/stiff-accuracy.md).

**Linear algebra.** Linearizing the DAE stage system gives (Southworth et al. 2022, §6,
Eqs. (31)–(33))

$$I_s\otimes\begin{bmatrix}M&0\\0&0\end{bmatrix}-h\,A\otimes\begin{bmatrix}J_{yy}&J_{yw}\\G_y&G_w\end{bmatrix},$$

with stage-dependent blocks in the nonlinear case ($J_{yy},J_{yw},G_y,G_w$ the Jacobian blocks,
page-local). After the real Schur transformation of the
[stage solver](/methods/implicit-stage-solvers.md) the $2\times2$ blocks become $4\times4$
blocks (Eq. (34)). For index 1, the field-of-values assumption applies to the reduced problem and
the preconditioning theory holds formally when the constraint is inverted accurately inside
each preconditioner application. Index-2 (saddle-point) problems need problem-specific analysis,
and the assumption need not hold (§6).

**Index-1 example.** Southworth et al.'s double shear layer in vorticity–streamfunction form,
$\omega_t+\nabla\cdot(u\omega)=\mathrm{Re}^{-1}\Delta\omega$, $\Delta\psi=\omega$, is an index-1
DAE ($\omega,\psi,u$ page-local). Solving the coupled $4\times4$ system with the block
preconditioner beats a reordering that solves the vorticity block first and then two Poisson
problems (§7.2, Tables 6–8).

**Index-2 incompressible flow.** Abu-Labdeh et al. (2023, §3.1, Eq. (3)) treat the
Taylor–Hood Stokes system $M\dot u_h+Ku_h+Bp_h=Mf$, $B^\top u_h=0$ (page-local: $u_h$,
$p_h$ discrete velocity and pressure, $K$ stiffness, $B$ discrete gradient) with stage
derivatives for both variables, so that the pressure is advanced like a differential
variable, $p_{n+1}=p_n+h\sum_jb_j\kappa_j$ with pressure stage derivatives $\kappa_j$, and
the constraint $B^\top U_i=0$ is imposed on every velocity stage value $U_i$ (page-local).
The stage system is

$$\Big(I_s\otimes\begin{bmatrix}M&0\\0&0\end{bmatrix}+h\,A\otimes\begin{bmatrix}K&B\\B^\top&0\end{bmatrix}\Big)\mathbf k=\mathbf F,$$

a saddle-point system coupling all stages, which they solve by monolithic multigrid
([stage solvers](/methods/implicit-stage-solvers.md)). [Taddei et al. (2026)](/sources/taddei-2026.md)
(§2.3, Eq. (11)) write the arbitrary Lagrangian–Eulerian fluid–structure system as the
semi-explicit DAE $y'=f(t,y,w)$, $0=g(t,y)$, with masked momenta and the structural
displacement as differential variables and the fluid pressure as algebraic variable $w$
(the source's $z$); they apply Radau IIA in stage-value form with the constraints imposed at
every stage (§3.1, Eqs. (14)–(17)). Radau IIA is
[stiffly accurate](/properties/stiff-accuracy.md), so $y_{n+1}=Y_s$ satisfies the
constraints and the update step is omitted (§3.1). Taddei et al. do not state the index of the
fluid–structure system; incompressible flow with the pressure as algebraic variable is
index 2 in the classification of Abu-Labdeh et al. *(compiler check, not in the sources)*.

Kirby & MacLachlan (2025, §2, Eqs. (2.11)–(2.14)) write the Irksome form of incompressible
Navier–Stokes the same way: velocity and pressure stage derivatives, the stage values
$u_n+h\sum_ja_{ij}k^u_j$ and $p_n+h\sum_ja_{ij}k^p_j$, and incompressibility imposed in variational form on every
stage velocity ($k^u_j$, $k^p_j$, $p_n$ page-local); this needs an initial pressure. For the
Navier–Stokes runs they use Butcher's transformed variables with stage values, which needed
fewer iterations, and monolithic multigrid or Rana-type preconditioners with Vanka patches
containing one pressure and all velocity degrees of freedom of an element for every stage
(§4.2); see [implicit stage solvers](/methods/implicit-stage-solvers.md).

**Mixed finite elements.** Farrell et al. (2021) apply Runge–Kutta methods directly to
semi-explicit DAEs in [Irksome](/software/irksome.md); the heat equation in mixed
$H(\mathrm{div})\times L^2$ form is an example (§2.2, Eqs. (19)–(21)). On it, two-stage Gauss
shows [order reduction](/definitions/order-reduction.md) and three-stage Radau IIA does not
(§4.1, Fig. 2). Navier–Stokes with Scott–Vogelius elements and two-stage Radau IIA reproduces
the reference drag and lift of the cylinder benchmark (§4.4.1).

## Rosenbrock methods for DAEs

[Rosenbrock–Wanner methods](/methods/rosenbrock-wanner-method.md) handle $My'=f(t,y)$ with
singular $M$ and index at most 1 directly; index 1 guarantees that $M-h\gamma J$ is regular for
small $h$ (Steinebach 2023, §1). Matching order on index-1 DAEs requires extra order conditions
beyond the ODE ones: 23 additional conditions up to order 5, for 40 in total (Tables 2–3).
Steinebach's other findings:

- **Index 2.** The extra conditions of Lubich and Roche give order 2, or order 3 in $y$ and 2 in
  $w$ (Table 4). On an index-2 test Rodas3, Rodas4 and Rodas5 drop to order 1, while
  all other methods tested, [Rodas5P](/methods/rodas5p.md) included, reach order 2 (Table 8).
- **Inexact Jacobian.** W-method conditions keep order 2 for index-1 problems if the derivative
  of the algebraic equation with respect to the algebraic variable is exact (§2, §4 problem 5).
- **Dense output.** Hermite interpolation is "only applicable to ODE problems"; Rodas5 and
  Rodas5P get DAE-valid weight polynomials (§1, §3; see [dense output](/methods/dense-output.md)).
- **Benchmarks.** Index-1 DAE tests include the pendulum, a transistor amplifier (8 equations),
  a water-tube network (49 unknowns, reformulated from index 2 to index 1), and a photovoltaic
  network (5 algebraic and 2 differential equations) (§4, Figs. 5–7).

## Linearly implicit multistep methods for DAEs

[Glandon et al. (2022)](/sources/glandon-2022.md) (Remark 5.10, Eqs. (5.8)–(5.9)) extend
their convergence argument for [linearly implicit multistep methods](/methods/linearly-implicit-multistep-method.md)
to semi-explicit index-1 DAEs $y'=f(y,w)$, $0=g(y,w)$ with $g_w$ nonsingular and of
negative logarithmic norm: a Limm method whose Jacobian term acts on past solutions only
(not on past function values) and that is strictly stable at infinity gives $\mathcal O(h_{\max}^p)$ global errors in both the differential and the
algebraic variables, under smoothness of the global error. The argument is informal; one
linear solve per step replaces the nonlinear solve of BDF.

## BDF methods and software

- **IDA.** The [SUNDIALS](/software/sundials.md) package IDA solves fully implicit
  $F(t,y,y')=0$, $y(t_0)=y_0$, $y'(t_0)=y'_0$ by variable-order (1–5), variable-step BDF in
  fixed-leading-coefficient form; IDAS adds sensitivities ([Gardner et al. 2022](/sources/gardner-2022.md),
  §2.2, §2.5).
- **IDA nonlinear system.** Each step solves $F\bigl(t_{n+1},y_{n+1},h_n^{-1}\sum_i\alpha_{n,i}y_{n+1-i}\bigr)=0$
  with BDF coefficients $\alpha_{n,i}$ (page-local; Gardner et al. §2.5).
- **ARKODE and CVODE.** [ARKODE](/software/arkode.md) accepts $M(t)y'=f(t,y)$ only with $M(t)$
  nonsingular and independent of $y$, so it does not solve DAEs ([Reynolds et al. 2023](/sources/reynolds-2023.md),
  §2; Gardner et al. §2.3). [CVODE](/software/cvode.md) offers projection methods for ODEs whose
  solution must satisfy constraints $g(t,y)=0$ (Gardner et al. §2.1).
- **Rosenbrock methods.** DifferentialEquations.jl hosts the Rodas family for index-1 DAEs
  (Steinebach 2023, §1, §5).

## Qualifications

- "Index" is used in the sources without a formal definition; the characterizations above are
  those the sources state (index 2, and the differentiation count of Abu-Labdeh et al.) or
  assume as a hypothesis (index 1, Glandon et al.).
- The index-2 order limit to stage order is stated by Southworth et al., by Abu-Labdeh et al.
  and by Kirby & MacLachlan as a citation, not proved there; Kirby & MacLachlan's own cylinder
  results exceed it for drag and lift, a tension the paper acknowledges (§4.2).
- Abu-Labdeh et al. (2023, §5) state that Gauss, Radau IIA and Lobatto IIIC all have stage order
  equal to the number of stages; Lobatto IIIC has $s-1$ in the standard classification (see
  [fully implicit Runge–Kutta methods](/methods/fully-implicit-runge-kutta.md)). They do not
  explain the large Gauss errors on Stokes; their hypothesis for Gauss's oscillatory drag and
  lift on Navier–Stokes is the lack of L-stability (§5.2).

# Citations

- [Southworth et al. (2022)](/sources/southworth-2022.md) — §2.1 (order limits), §6 (Eqs. (29)–(34)), §7.2 (Tables 6–8).
- [Steinebach (2023)](/sources/steinebach-2023.md) — §1 (Table 1), §2 (Tables 2–4), §3, §4 (problems 1, 4, 5; Figs. 5–7), §5.
- [Farrell et al. (2021)](/sources/farrell-2021.md) — §2.1–2.2 (Eqs. (6)–(9), (19)–(21)), §4.1 (Fig. 2), §4.4.1.
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §2.1–2.3, §2.5.
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §2 (Eq. (1), nonsingular mass matrix).
- [Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md) — §2 (stage-order limits), §3.1–3.3 (index-2 argument, Eq. (3)), §5.1–5.2 (Tables 1–2).
- [Taddei et al. (2026)](/sources/taddei-2026.md) — §2.3 (Eq. (11)), §3.1 (Eqs. (14)–(17)), §5.1.1 (Table 1).
- [Glandon et al. (2022)](/sources/glandon-2022.md) — Remark 5.10, Eqs. (5.8)–(5.9).
- [Kirby & MacLachlan (2025)](/sources/kirby-2025.md) — §2 (Eqs. (2.11)–(2.14), p. 17:5), §2.1 (Eqs. (2.15)–(2.17)), §4.2 (Figs. 7, 9–10, p. 17:19).
