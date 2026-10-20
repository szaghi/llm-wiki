---
type: Source
title: "Zeifang & Schütz (2022) — Implicit two-derivative deferred correction time discretization for the discontinuous Galerkin method"
description: "Builds a fully implicit two-derivative Hermite–Birkhoff predictor–corrector (deferred-correction) time discretization of order up to 8 for the DG spectral element method, discretizes the second time derivative through an auxiliary variable, and solves the doubled stage systems with Newton–GMRES and a new closed-form element-block preconditioner, matrix-free."
resource: "doi:10.1016/j.jcp.2022.111353"
source_kind: paper
authors: [Zeifang J., Schütz J.]
year: 2022
venue: "J. Comput. Phys. 464:111353"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_Journal_of_Computational_Physics_Zeifang_Implicit_two-derivative_deferred_correction_time_discretizat.pdf"
tags: [multiderivative, deferred-correction, implicit-stage-solvers, preconditioning, cfd]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

[Multiderivative](/methods/multiderivative-runge-kutta.md) time integrators use $\dot f$, the
second time derivative of the solution, besides $f$, and reach high order with fewer
quadrature nodes. The paper takes the two-derivative Hermite–Birkhoff predictor–corrector
HBPC($p$, $K$) of Schütz, Seal and Zeifang, a [deferred-correction](/methods/deferred-correction.md)
approximation with $K$ corrections of a two-derivative Hermite–Birkhoff Runge–Kutta method of
order $p$. It drops the IMEX splitting and replaces the predictor by successive steps of the
implicit fourth-order two-point Hermite rule. The order is $\min(4+K,p)$, with tableaux for
$p=4,6,8$. The scheme is coupled to the discontinuous Galerkin spectral element method of the
FLEXI code for the compressible Euler and Navier–Stokes equations.

The main difficulty is the spatial discretization of $\dot f$. A direct discretization had
shown a severe step restriction despite the A-stability of the ODE method. Following Schütz,
Seal and Jaust, an auxiliary variable $\sigma=f_h(y)$ is introduced, and $\dot f_h$ becomes a
DG operator in $(y,\sigma)$ with a differentiated Lax–Friedrichs flux. Every stage is then a
nonlinear system for $(Y,\sigma)$, twice the size of an implicit-Euler step, solved by Newton
with GMRES.

On the [solver side](/methods/implicit-stage-solvers.md) the paper exposes the structure of the
extended Jacobian and shows that a Schur-complement reduction, half the size but squaring the
DG Jacobian, fails at large steps. It introduces an element-wise extended block-Jacobi
preconditioner with a closed-form inverse (one LU per element), with and without the flux
Hessian, and implements it matrix-free with finite-difference Jacobian–vector products. The
preconditioner beats ILU(0), standard block Jacobi and no preconditioning at large steps.
Orders up to 8 are verified for advection, Euler and Navier–Stokes, and steps 200–500 times
the explicit limit are used for a lid-driven cavity, the
[flow past a cylinder](/benchmarks/flow-past-cylinder.md) at $\mathrm{Re}_D=200$ and the 3D
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md). No theorem is proved.

# Version read

arXiv:2109.04804v1 [math.NA], 10 Sep 2021, header "Preprint (2021) 1–22": the preprint, not
the version of record. 22 pages, all read (pp. 3, 4, 15 and 22 also checked visually).
**Title difference:** the arXiv version is titled "Two-derivative deferred correction time
discretization for the discontinuous Galerkin method", without the leading "Implicit" of the
published title. Authors and work are the same, but content added in review is not covered
here. Section, equation and figure numbers cited here are those of arXiv v1.

# Key claims

Notation: the semi-discrete system $y'=f_h(y)$ with $f_h=R^{(1)}_h$ and
$\ddot y=\dot f_h(y,\sigma)$ with $\sigma=f_h(y)$. $Y^{(k)}_l$ is stage $l$ after $k$
corrections, $K$ the number of corrections, $p$ the order of the limiting quadrature,
$(a_{lj},\dot a_{lj},c_l)$ the two-derivative tableau, $\Delta c_l=c_l-c_{l-1}$.

1. Two-derivative methods use $\ddot y$ besides $\dot y$ and so reach high order with fewer
   temporal quadrature nodes; they belong to Hairer & Wanner's
   multistep–multistage–multiderivative class. (§1) **Stated**
2. An implicit Lax–Wendroff-type direct discretization of an A-stable two-derivative method
   (with HDG) showed "a severe timestep restriction"; an extra solution variable per time
   derivative removed it, so that a linear PDE discretization keeps the stability of the ODE
   solver. (§1) **Stated** (cited)
3. HBPC($p$, $K$) approximates, with $K$ corrections, a two-derivative Hermite–Birkhoff
   Runge–Kutta method of order $p$. Here the predictor applies the implicit two-point Hermite
   rule on each subinterval,
   $Y_l=Y_{l-1}+\frac{\Delta c_lh}{2}\big(f(Y_{l-1})+f(Y_l)\big)+\frac{(\Delta c_lh)^2}{12}\big(\dot f(Y_{l-1})-\dot f(Y_l)\big)$,
   instead of an IMEX predictor; the corrector is
   $Y^{(k+1)}_l=y_n+h\big(f(Y^{(k+1)}_l)-f(Y^{(k)}_l)\big)-\frac{h^2}{2}\big(\dot f(Y^{(k+1)}_l)-\dot f(Y^{(k)}_l)\big)+I_l$,
   with $I_l$ the two-derivative quadrature of the previous iterate. (§2, Alg. 1, Eqs. (5)–(6))
   **Stated** (the predictor change is the paper's own)
4. The order is $\min(4+K,p)$: one order per correction from the fourth-order predictor up to
   the quadrature order (proved in the HBPC paper). (§2, Remark 2) **Stated** (cited);
   **Shown** in Figs. 7–9
5. Every predictor and corrector stage is
   $G(W)=W-\alpha_1hf(W)+\frac{\alpha_2h^2}{2}\dot f(W)-b=0$, with $\alpha_1=\Delta c_l/2$,
   $\alpha_2=\Delta c_l^2/6$ (predictor) or $\alpha_1=\alpha_2=1$ (corrector). (§2.2, Eqs.
   (7)–(9)) **Derived**
6. With $\sigma=f_h(y)$ the DG second-derivative operator (16) satisfies
   $\partial\dot f_h/\partial\sigma\equiv\partial f_h/\partial y$, and the Hessian part
   $\partial\dot f_h/\partial y$ vanishes for a linear flux. (§3.2.1) **Derived**
7. Newton's method is used even for linear problems because it "can have a beneficial
   influence on the achieved accuracy" (citing Higham). (§3.2.1) **Stated**
8. $\partial\dot f_h/\partial y$ is assembled with the routines of the standard DGSEM
   Jacobian, with flux Hessians in place of flux Jacobians. (§3.2.2) **Stated**
9. The extended block-Jacobi preconditioner (element blocks $A_i$, $B_i$, $C_i$, $I$) has a
   closed-form inverse that needs a single LU factorization of the element matrix
   $A_i-B_iC_i$ per element. (§3.2.3, Fig. 1) **Derived**
10. Dropping the Hessian from $A_i$ (BJext) makes the blocks commute, saves a matrix product
    per element, and needs only the implicit-Euler-type DGSEM Jacobian, at the price of a
    "slightly worse approximation". (§3.2.3) **Derived**
11. The Schur complement halves the system but needs $(\partial f_h/\partial y)^2$; it helps
    only at small steps, and at large $h$ the GMRES count "suddenly increases very rapidly
    and leads to non-convergence", with ILU(0) or block Jacobi. (§3.2.4, §4.1, Figs. 2–3)
    **Shown**
12. Linear advection ($16^2$ elements, degree 5, ILU(0)): GMRES iterations per predictor
    stage grow with slope close to one, slightly steeper than implicit Euler; BJext lowers
    both slope and count "drastically". (§4.1.1, Fig. 2) **Shown**
13. Euler with reference Mach number $\varepsilon\in\{1,10^{-1},10^{-2}\}$, ILU(0): the
    implicit-Euler slope stays below one, the predictor slope slightly above one, growing at
    $\varepsilon=10^{-2}$. (§4.1.2, Fig. 3) **Shown**
14. Dropping the Hessian from the system matrix matters little at moderate steps, but only
    the full matrix keeps linear iteration scaling at very large steps, so it is always kept
    there. (§4.1.2, Fig. 3) **Shown**
15. GMRES iterations (Euler): BJext ≈ BJext with Hessian < ILU(0) < none, and standard
    element block Jacobi is worse than no preconditioning; slopes grow with stiffness.
    Missing points did not converge within 7000 GMRES iterations per Newton step. (§4.1.2,
    Fig. 4) **Shown**
16. Wall-clock (Euler): BJext is the most efficient at large $h$, no preconditioning at small
    $h$; ILU(0) pays off "in only a few cases"; BJext beats its Hessian variant because it is
    cheaper to build. BJext is used thereafter. (§4.1.2, Fig. 5) **Shown**
17. The matrix-free Jacobian–vector product costs two (linear) or three (nonlinear) operator
    evaluations per GMRES iteration, and gives GMRES counts very close to the matrix-based
    ones with right BJext preconditioning. (§4.2, Eqs. (23)–(24), Fig. 6) **Shown**
18. BJext needs no inter-process communication when applied; ILU(0) needs the whole matrix and
    is incompatible with the matrix-free approach. Parallel performance is left to future
    work. (§4.2) **Stated**
19. Linear advection ($32^2$ elements, degree 7): HBPC(4, $K$) does not change with $K$; HBPC(6,
    ·) and HBPC(8, ·) gain one order per correction up to $p$; HBPC(8, $K\ge4$) is slightly
    above the expected order for some refinements; corrections beyond saturation can still
    improve accuracy. (§4.3.1, Fig. 7) **Shown**
20. Euler ($\varepsilon=1$): expected orders "in most cases", HBPC(8, $K\ge4$) again slightly
    above. (§4.3.2, Fig. 8) **Shown**
21. Navier–Stokes ($\mu=10^{-3}$): all HBPC($p$, $K$) reach their orders; HBPC(8, $K\ge3$)
    loses order at the last refinement to round-off; the asymptotic regime starts at smaller
    $h$ than for Euler, attributed to the fast parabolic characteristics. (§5.2, Fig. 9)
    **Shown**
22. An absolute Newton tolerance $\lVert\Delta W\rVert_2\le10^{-12}$ was needed, because the
    initial Newton residual of a correction stage can already be so small that round-off
    blocks the relative tolerance. (§5.2) **Shown**
23. Lid-driven cavity, $\mathrm{Re}=400$, $\varepsilon=0.1$, HBPC(6,2), $h=0.02$, steady at
    $t=50$: centreline velocities match Ghia et al. (§5.3.1, Fig. 10) **Shown**
24. Cylinder, $\mathrm{Re}_D=200$, $\varepsilon=0.1$, HBPC(6,2): $h=0.1$ and $0.25$, about 200
    and 500 times the step of the fourth-order explicit low-storage method, give Strouhal
    numbers 0.1971 and 0.1968 against 0.1957 and 0.196 in the literature, and the lift
    history of the explicit reference. (§5.3.2, Fig. 11) **Shown**
25. 3D Taylor–Green vortex, $\mathrm{Re}=800$, $32^3$ elements, degree 3, HBPC(4,0) with
    $h=0.25$ (about 200 times the explicit step): the kinetic-energy dissipation rate matches
    the explicit run and DNS; the peak near $t\approx9$ is slightly low, attributed to the
    coarse spatial resolution. (§5.3.3, Fig. 12) **Shown**
26. The dissipation constant of the global Lax–Friedrichs flux "is crucial for both stability
    and efficiency". (§6) **Stated**
27. With another quadrature rule and enough corrections, any order is attainable "in
    principle". (§4.3.1) **Stated**

*(Compiler checks, not in the sources.)* The name HBPC is kept although the predictor differs
from the IMEX predictor of the original HBPC paper; the two variants must not be conflated.
The finding that standard block Jacobi is worse than no preconditioning (claim 15) concerns
the doubled system and runs against common experience with implicit DG.

# Printed slips

- Eq. (9): the corrector right-hand side
  $b=w^{n-1,[k_{max}],s}-\alpha_1\Delta tR^{(1)}(w^{n,[k],l})+\frac{\alpha_2\Delta t^2}{2}R^{(2)}(w^{n,[k],l})$
  omits the $+I_l$ of Eq. (6).
- Algorithm 1 says "Solve ... for $w^{n,[0],l}$ and $1\le l\le s$", while step 1 has
  $2\le l\le s$ (stage 1 is assigned).
- Eq. (22): "$a:=(0.3.0.3)^T$". Eq. (20): $w(x,t=0)=\sin(\pi x)$ with a 2D vector $x$, the
  scalar argument undefined.
- §5.3.3 (p. 19, checked visually): the Taylor–Green initial velocity is printed
  $v=(\cos x\cos y\cos z,-\cos x\sin y\cos z,0)^T$; with this first component the field is not
  divergence-free, and the standard field has $\sin x\cos y\cos z$. The dissipation rate is
  printed without the minus sign that Fig. 12 plots.
- Figs. 3–4 legends: "predicto". App. A: "eigth-order". §4.2: "is is"; §5: "the the". §3.2.4
  writes $\Delta w$ where the rest writes $\Delta W$.
- Ref. [46]: "458 (2018) (2002)", where 2018 is the issue number of Proc. R. Soc. A 458.
- Footnote 2 omits point 117 of Ghia et al. (Table II) "as this number seems to be
  erroneous", a slip claimed in the cited work.

# Notation map

| Zeifang & Schütz | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $w$, $W$ | $y$, $Y$ | state; stage unknown (Eq. (21) also uses $W$ for the Euler state) |
| $R^{(1)}(w)=-\nabla_x\cdot F(w)$, $R^{(1)}_h$ | $f(y)$, $f_h$ | method-of-lines right-hand side, autonomous |
| $R^{(2)}(w,R^{(1)}(w))$, $R^{(2)}_h(w,\sigma)$ | $\dot f$, $\dot f_h(y,\sigma)$ | second time derivative, discretized separately |
| $\sigma:=R^{(1)}_h(w)$ | $\sigma$, kept | auxiliary variable; **not the tree symmetry or the multistep $\sigma(\zeta)$** |
| $B^{(1)}$, $B^{(2)}$, $c$ | $(a_{lj})$, $(\dot a_{lj})$, $c$ | two-derivative tableau; **$B^{(2)}$ multiplies $h^2$ directly, with no factor $1/2$** |
| $q$ | $p$ | order of the limiting quadrature (4, 6, 8) |
| $s$ | $s$ | stages, the first explicit ($c_1=0$) |
| $k_{max}$, $[k]$ | $K$, $(k)$ | corrections and correction index |
| $w^{n,[k],l}$ | $Y^{(k)}_l$ | stage $l$ of step $n$ after $k$ corrections |
| $\Delta t$ | $h$ | subscript $h$ means discrete in space |
| $\alpha_1$, $\alpha_2$ | kept, page-local | stage-equation coefficients; **not the Shu–Osher or Rosenbrock $\alpha$** |
| $G$, $g$, $b$ | kept, page-local | stage residual; **$G$ is not the registry G-norm matrix, $b$ not the weights** |
| $X=(W,\sigma)$, $J$, $J_{Schur}$ | kept | extended state, Newton Jacobian of the extended system, Schur complement |
| $P$ | kept, page-local | preconditioner; **not the registry stability polynomial** |
| $\varepsilon$ | $\varepsilon$ | reference Mach number; also scales the finite-difference step $\varepsilon_{FD}$ |
| $\lambda$ | kept, page-local | Lax–Friedrichs dissipation constant and (§5) thermal conductivity; **not the registry eigenvalue** |
| $N$, $n_E$ | kept | polynomial degree, number of elements |

# Reference list

46 printed references, numbered [1]–[46], none with a DOI. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` zeifang-2022. Two arXiv preprints stay
their own entries: [15] Chouchoulis et al. (arXiv:2107.06633, keyed `chouchoulis-2021`) and
[21] Schütz, Seal & Zeifang (arXiv:2101.07846, `schutz-2021-b`). Same-key works take
suffixes in printed order (`schutz-2021`/`-b`). [32] (Zeifang et al., Commun. Comput.
Phys. 27) prints the year 2020 and is merged into the existing entry `zeifang-2019`, so
[29] alone is `zeifang-2020`. [46] (`toro-2002`) prints "458 (2018) (2002)" and is
recorded as volume 458, year 2002, with the issue number in the note. No unparseable items.

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [Deferred correction (DeC)](/methods/deferred-correction.md)
* [Flow past a cylinder (Schäfer–Turek)](/benchmarks/flow-past-cylinder.md)
* [Linear advection equation](/benchmarks/linear-advection-equation.md)
* [Multiderivative Runge–Kutta methods and the backward derivative condition](/methods/multiderivative-runge-kutta.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
