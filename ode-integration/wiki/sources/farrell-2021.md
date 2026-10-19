---
type: Source
title: "Farrell et al. (2021) — Irksome: Automating Runge–Kutta Time-stepping for Finite Element Methods"
description: "Presents Irksome, a library that turns a UFL semidiscrete variational form and a Butcher tableau into the coupled Runge–Kutta stage equations for Firedrake, solved with PETSc's composable preconditioners, and shows order reduction, stage-solver cost, energy and invariant behaviour of Gauss–Legendre, Radau IIA, Lobatto IIIC and DIRK methods on finite element tests."
resource: "doi:10.1145/3466168"
source_kind: paper
authors: [Farrell P.E., Kirby R.C., Marchena-Menéndez J.]
year: 2021
venue: "ACM Trans. Math. Softw. 47:1-26"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_ACM_Transactions_on_Mathematical_Software_Farrell_Irksome_Automating_RungeKutta_Time-stepping_for_Finite_Eleme.pdf"
tags: [software, runge-kutta, implicit, linear-algebra, order-reduction, geometric-integration]
timestamp: 2026-10-19T12:00:00Z
---

# Summary

The paper presents [Irksome](/software/irksome.md), a Python library. It
takes a UFL expression of a semidiscrete variational form
$G(t,u,u_t;v)=0$ and a Butcher tableau and generates the UFL of the fully
discrete, coupled $s$-stage
[Runge–Kutta](/definitions/runge-kutta-method.md) stage equations together
with the stage boundary conditions. The generated system is solved inside
Firedrake by PETSc solvers configured through options. The paper thereby
answers two objections to
[fully implicit Runge–Kutta methods](/methods/fully-implicit-runge-kutta.md)
(Gauss–Legendre, Radau IIA, Lobatto IIIC) in finite element practice.
Coding the coupled stage system is laborious; Irksome removes that cost by
mechanical substitution. The $(ds)\times(ds)$ system is thought too
expensive; Irksome exposes it to composable
[stage solvers](/methods/implicit-stage-solvers.md) such as the
Mardal–Nilssen–Staff block-diagonal preconditioner with one AMG V-cycle
per stage block. [DIRKs](/methods/diagonally-implicit-runge-kutta.md)
need no special code: a multiplicative field split of the block
lower-triangular system is block forward substitution. At the time,
[PETSc TS](/software/petsc-ts.md) offered no multi-stage implicit
Runge–Kutta methods. Built-in tableaux include Gauss–Legendre, Lobatto
IIIA and Radau IIA of any order, Lobatto IIIC, and classical explicit,
[SSP](/methods/strong-stability-preserving-runge-kutta.md) and DIRK
methods.

The tests are numerical. Heat-equation manufactured solutions show
[order reduction](/definitions/order-reduction.md) of 2-stage
Gauss–Legendre to its [stage order](/definitions/stage-order.md), while
3-stage Radau IIA keeps full accuracy. Block-diagonal AMG preconditioning
makes 2- and 3-stage Radau IIA cost about 3 and 5 backward-Euler solves.
On the mixed wave equation the
[symplectic](/properties/symplecticity.md) Gauss–Legendre methods conserve
energy, Radau IIA and Lobatto IIIC damp it (see
[A-, L- and algebraic stability](/properties/a-stability.md)), and a
symplectic DIRK matches Gauss–Legendre. Navier–Stokes flow past a cylinder
is treated as an index-2
[DAE](/definitions/differential-algebraic-equation.md) with 2-stage Radau
IIA. On a BBM solitary wave Gauss–Legendre preserves the linear and
quadratic invariants to round-off.

# Version read

arXiv:2006.16282v1 [math.NA], 29 June 2020, a 21-page preprint, not the
26-page ACM TOMS version of record. There is no ACM header, no DOI and no
received or accepted dates. Page 1 prints the title "Irksome: Automating
Runge–Kutta time-stepping for finite element methods"; the published title
uses title case. Authors and author order match the published version.
The version of record may differ in sections and numbers. Every locator on
this page refers to arXiv v1.

# Key claims

Registry notation: $h$ step (the source's $\Delta t$), $\Delta x$ mesh size
(the source's $h$), $f=-F$ for the source's $y'+F(t,y)=0$, $Y_i$ stage
values. $k_i=f(t_n+c_ih,Y_i)$ are the stage derivatives the source
iterates on. $K_{\mathrm{st}}$ is the stiffness matrix (page-local) and
$d$ the number of spatial unknowns.

1. Irksome's `getForm` takes a UFL semidiscrete form, a Butcher tableau,
   time and time-step `Constant`s and a solution `Coefficient`. It returns
   UFL for the coupled multi-stage form and the stage boundary conditions;
   `TimeStepper` wraps this and advances in time (§3). **Stated**
   (software description)
2. The stage form follows mechanically from the semidiscrete form. For each
   stage $i$, substitute $k_i$ for $u_t$, $u_n+h\sum_ja_{ij}k_j$ for $u$,
   $v_i$ for $v$ and $t_n+c_ih$ for $t$, then sum over stages (§2.2.1 after
   Eq. (17); §3.1). **Derived**
3. Strong Dirichlet data $u|_\Gamma=g(t,\cdot)$ become stage conditions
   $k_i|_\Gamma=\partial_tg(t_n+c_ih,\cdot)$, since $k_i$ approximates $u_t$
   at $t_n+c_ih$. Weak boundary conditions only need the data at stage
   times (Eq. (18)). **Derived**
4. For backward Euler, $k_1$ corresponds one-to-one to
   $(u_{n+1}-u_n)/h$, and the bilinear form defining $k_1$ (17) equals the
   one defining $u_{n+1}$ (12) (§2.2.1). **Derived**
5. For the heat equation the $s$-stage system is
   $(I\otimes M+hA\otimes K_{\mathrm{st}})\mathbf k=\mathbf f$ (Eq. (31)).
   For nonlinear problems the Jacobian couples all stages without the
   Kronecker structure (§2.3). **Derived**
6. Following Mardal–Nilssen–Staff, the block diagonal
   $\mathrm{diag}(M+a_{ii}hK_{\mathrm{st}})$ (Eq. (32)) "makes an excellent
   preconditioner, at least in the case of parabolic problems" (§2.3).
   **Stated** (cited; tested in claim 14)
7. For a DIRK the stage system is block lower triangular (Eq. (33)). A
   multiplicative field split with exact block solves solves it in one
   iteration, so DIRKs need no special handling (§2.3, §4.3). **Derived**
8. An explicit method needs one mass-matrix solve per stage (Eq. (34))
   (§2.3). **Derived**
9. Built-in families: Gauss–Legendre (implicit midpoint included), Lobatto
   IIIA (Crank–Nicolson included) and Radau IIA (backward Euler included)
   of arbitrary order via FIAT quadrature nodes; Lobatto IIIC; forward
   Euler, an SSP method, explicit midpoint and trapezoid, classical RK4 and
   Alexander's L-stable DIRKs (§3.2). **Stated**
10. All the collocation families listed are A-stable. Gauss–Legendre is
    B-stable and symplectic but not L-stable. Radau IIA is L-stable. Lobatto
    IIIC is L-, B- and A-stable (§3.2). **Stated** (background)
11. Heat-equation manufactured solution ($u=e^{-t}\sin(\pi x)\cos(\pi y)$,
    cubic serendipity, $N=8,\dots,128$, $h=1/N,4/N,16/N$, errors at
    $t=2$): Gauss–Legendre(2) shows order 4 in $L^2$ only at very small $h$
    and degenerates to stiff order 2. Lobatto IIIC(3) reduces in $L^2$
    while $H^1$ stays at order 3. Radau IIA(2) reduces in $L^2$ only. Radau
    IIA(3) shows full accuracy in both norms (§4.1, Fig. 1). **Shown**
12. For stiff problems collocation methods "reduce to the maximum truncation
    error per-stage (e.g. $s$ for an $s$-stage Gauss-Legendre method)"
    instead of the nominal $2s$ (§4.1, citing Hairer–Wanner). **Stated**
13. Mixed heat equation (RT3 × DG3 on right triangles): Gauss–Legendre(2)
    reduces (Fig. 2a), Radau IIA(3) does not (Fig. 2b). 2-stage Radau IIA
    and 3-stage Lobatto IIIC are also "satisfactory" (§4.1). **Shown**
14. Preconditioner cost (heat, $128\times128$ $Q^2$ mesh, $t\in[0,1]$,
    $h=0.078125$, GMRES with additive field split and one `gamg` V-cycle
    per block): Radau IIA(2) costs about 3 times Radau IIA(1), which is
    backward Euler, and Radau IIA(3) about 5 times (§4.2, Fig. 3). Read off
    Fig. 3: solver time about 9, 24, 46 (units not printed) and GMRES
    iterations per step about 4, 11, 17.5 for $s=1,2,3$. **Shown**
15. Richardson step doubling costs 3 backward-Euler solves for order 2 and
    7 for order 3. 2-stage Radau IIA costs about 3 and 3-stage Radau IIA
    about 5, "a clear win over step doubling" (§4.2). **Shown** (cost) /
    **Derived** (counting)
16. The semidiscrete mixed wave system conserves
    $E(t)=\frac12(\lVert u\rVert^2+\lVert\sigma\rVert^2)$ exactly (Eq. (36)).
    **Stated**
17. Wave equation ($10\times10$ triangles, $RT_2\times DG_1$,
    $h=0.1,0.5,1.0$, $t\in[0,10]$), ratio $E(10)/E(0)$: Gauss–Legendre(1),
    (2) give 1 "to machine precision". Lobatto IIIC(2) gives
    $3.79\times10^{-1}$, $9.75\times10^{-18}$, $1.17\times10^{-20}$; Lobatto
    IIIC(3) $9.99\times10^{-1}$, $5.19\times10^{-2}$, $3.65\times10^{-9}$;
    Radau IIA(1) $1.50\times10^{-8}$, $3.40\times10^{-16}$,
    $6.79\times10^{-14}$; Radau IIA(2) $9.00\times10^{-1}$,
    $7.10\times10^{-4}$, $3.77\times10^{-7}$ (Table 1). **Shown**
18. The 2-stage DIRK (37), $c=(\frac14,\frac34)$,
    $A=\begin{pmatrix}\frac14&0\\\frac12&\frac14\end{pmatrix}$,
    $b=(\frac12,\frac12)$, attributed to Qin/Zhang, is second order,
    A-stable and symplectic. Solved by a multiplicative field split with LU
    per block (Listing 3), it gives the same energy behaviour as
    Gauss–Legendre in Table 1 (§4.3). **Shown** (energy) / **Stated**
    (properties)
19. Navier–Stokes cylinder benchmark (Re 100, $t\in[0,8]$): Scott–Vogelius
    $P^4/P^3_{\mathrm{disc}}$ on 14,640 curvilinear cells (about 382k
    unknowns) with Radau IIA(2) and $h=0.00125$ matches the reference drag
    and lift ($Q_2/P_1^{\mathrm{disc}}$, about 667k unknowns, Crank–Nicolson,
    $h=0.000625$): "excellent agreement ... with half as many degrees of
    freedom and a time-step twice as large" (§4.4.1, Fig. 5). **Shown**
20. On the curvilinear mesh Scott–Vogelius is not pointwise divergence-free:
    $\lVert\nabla\cdot u\rVert_{L^2}$ ranged over about
    $10^{-5}$–$10^{-3}$ per step, and the method was nevertheless stable
    (§4.4.1). **Shown**
21. BBM solitary wave ($\Delta x=0.1$, P1, $T=18$): implicit midpoint gives
    about 0.15% relative $L^2$ error with $h=\Delta x$ and more than 10% with
    $h=10\Delta x$. Gauss–Legendre(2) with $h=10\Delta x$ gives 0.14%
    (§4.4.2). **Shown**
22. BBM invariants: the linear $I_1$ and quadratic $I_2$ are conserved to
    $O(10^{-15})$ by Gauss–Legendre(1) and (2). The cubic $I_3$ drifts:
    $I_3(18)/I_3(0)=0.9948969$ for GL(1) and $0.9999990$ for GL(2)
    (§4.4.2, Table 2). **Shown**
23. Gauss–Legendre methods are symplectic and preserve quadratic
    invariants; preserving cubic invariants requires "very strong
    conditions" (§4.4.2, citing Iserles–Zanna). **Stated**
24. DIRKs are "necessarily limited to low stage order". Pazner–Persson
    found preconditioned Radau IIA more efficient than DIRKs of comparable
    order for compressible Navier–Stokes (§1). **Stated**
25. PETSc TS, at the time of writing, offered only an enumerated set of
    Runge–Kutta methods, with no multi-stage implicit ones (§1).
    **Stated**
26. Current limitation: time derivatives may act only on unknown fields,
    not on expressions; one writes `2*t*u + t**2*Dt(u)` instead of
    `Dt(t**2*u)` (§3.1). **Stated**

# Printed slips

- Eq. (4) and the text after it: "for all $1\le i\le n$ the stages
  $k_i\in\mathbb R^n$ satisfy $k_i+F(t+c_i\Delta t,y+\Delta
  t\sum_{i=1}^nA_{ij}k_j)=0$" and "$A_{ij},b_i,c_i$ for $1\le i,j\le n$".
  The stage range should be $s$, the summation index $j=1,\dots,s$, and
  $t,y$ should be $t^n,y^n$.
- p. 3: "$y(t^n)\equiv y_n$" followed by "$y^{n+1}=y^n+\dots$" mixes
  sub- and superscripts.
- Eq. (10): "$(u_t,v)-(\nabla u,\nabla v)=(f,v)$" has the wrong sign on the
  diffusion term; Eqs. (11) and (14) use $+$.
- Eq. (15): "$u^{n+1}=u^n+\sum_{i=1}^sb_ik_i$" lacks the factor $\Delta t$
  (cf. Eq. (3)).
- Eqs. (14), (16): forcing evaluated at "$t+c_i\Delta t$" and
  "$t+\Delta t$" instead of $t^n+\dots$.
- Eq. (23) (wave) carries a forcing term $-(f(t^n+c_i\Delta t,\cdot),v_i)$
  that (22) lacks.
- §4.1: "the extra formal order of accuracy for Gauss-Lobatto methods does
  not materialize"; the method of Fig. 2a is Gauss–Legendre.
- Fig. 1(b) panel title "LobatoIIIC(3)".
- §4.2: "our three stage method (empirically) requires a cost comparable to
  only backward Euler evaluations" — the number (five) is missing.
- §4.2: $\Delta t=0.078125$ on $[0,1]$ gives 12.8 steps; the handling of
  the final time is not stated.
- "Benjamin-Bona-Mahoney" (Eq. (25)) against "Benjamin-Bona-Mahony"
  (§4.4.2); "conversion of the invariants" for "conservation" (§4.4.2).
- §4.1: Lobatto IIIC(3) "$H^1$ error stays at order three (which is both
  the stage order …)". In the standard classification $s$-stage Lobatto
  IIIC satisfies $C(s-1)$, so its stage order is 2 for $s=3$.
- Ref. [40] prints the authors of *Solving ODEs II* as "Gerhard Wanner and
  Ernst Hairer". §4.3 calls (37) the "Qin/Zhang" DIRK, while ref. [32]
  lists only "Zhang Mei-Qing".

# Notation map

| Farrell et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $y'(t)+F(t,y)=0$ | $y'=f(t,y)$, $f=-F$ | residual sign convention |
| $\Delta t$ | $h$ | step size |
| **$h$** | $\Delta x$ | **collision: the source's $h$ is the mesh size** |
| $t^n$, $y^n$ (also $t_n$, $y_n$) | $t_n$, $y_n$ | |
| $A=(A_{ij})$ or $(a_{ij})$, $\mathbf b$, $\mathbf c$ | $A$, $b$, $c$ | $c=A\mathbf 1$ not stated |
| $k_i$ | $f(t_n+c_ih,Y_i)$ | stage derivatives; the source never writes stage values |
| $u$, $v$, $v_i$ | — | finite element unknown, test function, per-stage test function |
| $M$ | $M$ | mass matrix; agrees |
| **$K$** | $K_{\mathrm{st}}$ | **collision with $K$ (correction iterations)**; stiffness matrix; $L=-M^{-1}K_{\mathrm{st}}$ |
| $P$ | — | block-diagonal preconditioner (Eq. (32)) |
| **$n$** | $d$ | **the source uses $n$ for both the ODE dimension and the step index** |
| $\lambda$ in $y'=\lambda y$ | $\lambda$ | agrees; $z=h\lambda$ not written |
| GL($s$), RadauIIA($s$), LobattoIIIC($s$) | — | the argument is the stage count, not the order |
| "stiff order" | — | observed order on stiff problems, used informally for the stage order |
| $\sigma$ | — | flux variable; collides with tree symmetry $\sigma(\tau)$ only nominally |
| $E(t)$, $I_1$, $I_2$, $I_3$ | — | wave energy and BBM invariants |
| $N$ | — | mesh cells per side, $h=c/N$ |

# Reference list

The paper prints 40 references in numbered style, alphabetical by first
author. All are merged complete into the [bibliography](/bibliography.md)
with `citedby` farrell-2021. The preprints [1] (arXiv:1806.01437) and [23]
(arXiv:2003.01632) are their own entries. Ref. [20] prints no volume
(JCAM, article 112497). Ref. [32] prints the author as "Zhang Mei-Qing",
keyed `zhang-1992`. Ref. [40] prints the author order "Wanner, Hairer";
it is the Hairer–Wanner book and is folded into `hairer-1996`. No same-key suffixes were
needed.

# Pages created or updated

Chunk 1 (2026-10-19); updated in later chunks. This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [Benjamin–Bona–Mahony equation](/benchmarks/benjamin-bona-mahony-equation.md)
* [Boundary conditions for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Differential-algebraic equations and their Runge–Kutta treatment](/definitions/differential-algebraic-equation.md)
* [Energy method for Runge–Kutta stability](/methods/runge-kutta-energy-method.md)
* [Flow past a cylinder (Schäfer–Turek)](/benchmarks/flow-past-cylinder.md)
* [Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)](/methods/fully-implicit-runge-kutta.md)
* [Irksome](/software/irksome.md)
* [Linear multistep methods](/methods/linear-multistep-method.md)
* [Order reduction](/definitions/order-reduction.md)
* [PETSc TS](/software/petsc-ts.md)
* [Runge–Kutta method](/definitions/runge-kutta-method.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Stage order](/definitions/stage-order.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
* [Symplecticity and quadratic-invariant preservation](/properties/symplecticity.md)
* [Unconditional strong stability of diagonal Padé schemes and its energy law](/results/diagonal-pade-strong-stability.md)
