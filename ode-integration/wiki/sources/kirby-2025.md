---
type: Source
title: "Kirby & MacLachlan (2025) — Extending Irksome: Improvements in Automated Runge–Kutta Time Stepping for Finite Element Methods"
description: "Software paper extending Irksome with DAE-type Dirichlet conditions on stage values, Butcher's A-inverse and stage-value formulations, a dedicated DIRK path and generic Rana-type preconditioners; fully implicit Radau IIA methods with good preconditioners match DIRK runtimes while being more accurate."
resource: "doi:10.1145/3759245"
source_kind: paper
authors: [Kirby R.C., MacLachlan S.P.]
year: 2025
venue: "ACM Trans. Math. Softw. 51:1-27, Art. 17"
local_file: "/home/stefano/papers/mosaic/ode-integration/2025_Crossref_ACM_Transactions_on_Mathematical_Software_Kirby_Extending_ttIrksomett.pdf"
tags: [software, fully-implicit, implicit-stage-solvers, boundary-conditions, dae, finite-elements]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

The paper describes extensions of [Irksome](/software/irksome.md), the
library that takes a UFL description of a semi-discrete finite element
problem and a Butcher tableau and generates the stage-coupled variational
problem of an implicit Runge–Kutta step, which Firedrake compiles and PETSc
solves. Four extensions are presented.

1. **DAE-type Dirichlet conditions.** Boundary data are imposed on the stage
   values, $y_n+h\sum_ja_{ij}k_j=g(t_n+c_ih)$ on the boundary. This replaces
   the earlier ODE-type rule that imposed $g'$ on the stage derivatives, which
   fails on incompatible data ([stage boundary treatment](/methods/runge-kutta-stage-boundary-treatment.md)).
   It keeps the [stage order](/definitions/stage-order.md), and stiffly
   accurate methods then match the boundary data exactly at $t_{n+1}$.
2. **Alternative stage formulations.** Butcher's $A^{-1}$ change of variables
   moves the stage coupling outside the nonlinearity. The stage-value form
   skips the final mass-matrix solve for stiffly accurate tableaux.
3. **A dedicated [DIRK](/methods/diagonally-implicit-runge-kutta.md) path.**
   One single-stage solver is built and reused across stages.
4. **Generic Rana-type preconditioners.** The approximation $A\approx LD$
   from $A=LDU$ is built by form manipulation and sits beside block Jacobi,
   block Gauss–Seidel and monolithic multigrid with stage-coupled patch
   relaxation ([stage solvers](/methods/implicit-stage-solvers.md)).

Experiments. On the [heat equation](/benchmarks/heat-equation.md), Radau IIA
($s\ge2$) and WSODIRK433 avoid order reduction, while Alexander's DIRK3 and
backward Euler do not. Block Jacobi and block Gauss–Seidel iteration counts
grow with $s$, while Rana-LD iteration counts stay flat. Navier–Stokes
[flow past a cylinder](/benchmarks/flow-past-cylinder.md) is an index-2
[DAE](/definitions/differential-algebraic-equation.md). There, monolithic
multigrid iteration counts are almost independent of $s$, and
[Radau IIA](/methods/fully-implicit-runge-kutta.md) costs about as much as a
DIRK with the same number of stages. The
[Cahn–Hilliard equation](/benchmarks/cahn-hilliard-equation.md) is solved
with $C^1$ Bell elements; the free energy decays for every method. Radau
IIA(3) and (4) give the best accuracy per runtime on both nonlinear
problems. The conclusion: a fully implicit RK method with good
preconditioners runs about as fast as a DIRK and is more accurate. Future
work named: adaptive [step-size control](/methods/step-size-control.md) for
implicit RK on DAEs, and IMEX support.

# Version read

The file is the version of record (ACM, open access CC BY 4.0), 27 pages
(17:1–17:27), received 12 Mar 2024, accepted 13 Jul 2025. Title, authors,
volume and DOI on page 1 match Crossref; page 1 prints the second author as
"Scott P. MacLachlan". "Irksome" is set in typewriter type in the title,
which is why the archive filename reads "Extending_ttIrksomett"; no identity
problem. Example codes are archived at Zenodo, DOI 10.5281/zenodo.14888648.
Equation and page numbers below are those of this version.

# Key claims

Notation: $y'=f(t,y)$ (the source's $F$); stage derivatives
$k_j=f(t_n+c_jh,Y_j)$; $g$ the Dirichlet data on the boundary part $\Gamma$;
$M$, $K_{\mathrm{FE}}$ the finite element mass and stiffness matrices.

1. Imposing $\sum_ja_{ij}k_j=\bigl(g(t_n+c_ih)-y_n\bigr)/h$ on $\Gamma$ ("DAE-type" conditions) is solvable for the boundary values of $k_i$ whenever $A$ is invertible and keeps (at least) the stage order (§2, §2.1, Eqs. 2.15–2.17). **Stated**
2. For stiffly accurate schemes $y_{n+1}=Y_s$, so DAE-type conditions make $y_{n+1}$ match the boundary data at $t_{n+1}$ up to projection error; otherwise this is not guaranteed (§2.1, pp. 17:6–17:7). **Derived**
3. The earlier ODE-type rule of Farrell et al. (2021), $k_i|_{\partial\Omega}=g'(t_n+c_ih)$, "has proven to have some inherent weaknesses", and similar approaches limit accuracy (§2, p. 17:4). **Stated**
4. With incompatible data ($u_t=u_{xx}$ on $[0,1]$, $u(0,x)=0$, $u(t,0)=u(t,1)=1$; P1 on 10 intervals, three-stage Lobatto IIIC, $h=0.05$ to $t=0.5$) the ODE-type rule sees zero boundary time derivative and returns the zero solution; the DAE-type rule captures the approach to $u\equiv1$ (§2.1, Fig. 2). **Shown**
5. DAE-type conditions are the Irksome default; many practical cases show little difference, but they are "more robust and supported by standard RK convergence theory" (§2.1). **Stated**
6. In Butcher's formulation $w=(A\otimes I)k$, i.e. $\sum_j(A^{-1})_{ij}w_j-f(t_n+c_ih,y_n+hw_i)=0$, the stage coupling lies outside the nonlinearity, so the nonlinear Jacobian has $s$ rather than $s^2$ blocks (§2.2, Eq. 2.19). **Derived**
7. Any factorization $A=A_1A_2$ with $A_2$ invertible gives a valid change of variables $w=A_2k$; the authors know no splitting other than $A_2=A$ with similar benefits (§2.2). **Stated**
8. The stage-value update needs one mass-matrix solve, skipped automatically for stiffly accurate tableaux (§2.2, Eqs. 2.20–2.21). **Derived**
9. For linear problems a DIRK's stage system is block triangular and can be solved one diagonal block at a time through PETSc options; a dedicated DIRK path reuses one single-stage problem (§2.3). **Stated**
10. Alexander's three-stage DIRK is L-stable, of order 3, with stage order and weak stage order 1 (§2.3, §4.1). **Stated**
11. Block Jacobi $P_D$ and block Gauss–Seidel $P_L$ need outer iteration counts that grow with $s$ even with exact block solves; at $s=4$ about 47 and 22 GMRES iterations against about 10 for Rana-LD and 7 for the DIRK (§3.1, Fig. 5b). **Shown** (values read from the plot)
12. The Rana-type preconditioner $\tilde P_{LD}=(\tilde A_{LD}^{-1}\otimes M)+h(I\otimes K_{\mathrm{FE}})$, $\tilde A_{LD}=LD$, gives very low iteration counts "empirically independent of the number of RK stages" (§3.1, Eq. 3.5, Fig. 5). **Shown**
13. Staff et al. (2006) found right preconditioning better than left, and lower-triangular better than block-diagonal better than upper-triangular, on one model problem (§3.1). **Stated**
14. Kirby (2024) proves that if single-stage multigrid with additive Schwarz relaxation converges (possibly with a complex step), monolithic multigrid with patches holding all stages converges with a spectral radius not explicitly depending on $s$ (§3.2, Eq. 3.8). **Stated**
15. The eigenvalue-based preconditioners of Southworth et al. and the SVD-based ones of Leveque et al. are not supported: the nonlinear case does not map onto PETSc nonlinear solvers, and the SVD approach is problem-specific and linear-only (§3.1). **Stated**
16. Heat equation, degree-2 serendipity elements, $h=m/N$ with $m=1,4,8$: backward Euler is suboptimal in $L^2$ for all $m$, Alexander's DIRK at $m=8$ (order reduction); Radau IIA($s\ge2$) and WSODIRK433 give optimal spatial accuracy (§4.1, Fig. 3). **Shown**
17. With cubic serendipity elements Alexander's loss grows and Radau IIA(2) (order 3, stage order 2) loses $L^2$ but not $H^1$ accuracy at large steps; Radau IIA(3), (4) and WSODIRK433 are spatial-error dominated (§4.1, Fig. 4). **Shown**
18. For the linear heat equation the formulation differences are small, with a slight preference for Butcher's splitting with the stage-derivative form (§4.1). **Shown** (no data printed)
19. Heat-equation runtime: block Jacobi and block Gauss–Seidel are markedly slower than Rana-LD and the DIRK, which are very comparable (§4.1, Fig. 5a). **Shown**
20. Navier–Stokes cylinder on $[0,1]$: Rana needs fewer Newton and Krylov iterations and is faster for Radau IIA(2), (3); monolithic multigrid is faster for Radau IIA(4) (§4.2, Fig. 8). **Shown**
21. Navier–Stokes on $[0,8]$: Newton and Krylov counts are stable in $s$; Radau IIA(3) costs slightly more than 3 times Radau IIA(1), Radau IIA(4) slightly less than 4 times; DIRKs with $s$ stages run about as long as Radau IIA($s$) (§4.2, Fig. 9). **Shown**
22. Reference values on the fixed mesh (Radau IIA(5), finest step): maximum drag ≈ 2.89 at $t=3.93625$, maximum lift ≈ 0.47 at $t=5.68875$ (§4.2). **Shown**
23. Among the order-3 methods accuracy is comparable (Radau IIA(2) slightly better than Alexander, slightly better than WSODIRK433); the schemes generally exceed the stage-order bound for final drag and lift; Alexander under-achieves for maximum drag; Radau IIA(1) barely converges (§4.2, Fig. 10). **Shown**
24. For index-2 DAEs such as Navier–Stokes accuracy is governed by the stage order; DIRKs "are only guaranteed to have stage order one or two", Radau IIA($s$) has stage order $s$ (§2, p. 17:5; §4.2, p. 17:19). **Stated**
25. Accuracy against runtime: Radau IIA(3), (4) are best for final drag and lift; WSODIRK744 is accurate but "far more expensive" (§4.2, Fig. 11). **Shown**
26. Cahn–Hilliard: the free energy decreases monotonically for all methods; backward Euler is qualitatively different even at $h=6.25\times10^{-7}$ (§4.3, Fig. 13). **Shown**
27. Cahn–Hilliard runtime depends mainly on the stage count; Radau IIA costs slightly more than a DIRK with as many stages; Newton iterations approach about 4 per step as $h$ decreases (§4.3, Fig. 14). **Shown**
28. Cahn–Hilliard final-energy error: Radau IIA(3), (4) lowest, then WSODIRK744; Radau IIA(2) beats Alexander and WSODIRK433 at much lower cost; few schemes reach formal order, attributed to stiffness and stage order (§4.3, Fig. 15). **Shown**
29. For Cahn–Hilliard, monolithic multigrid is faster at small steps and Rana at large ones (§4.3). **Shown** (no data printed)
30. Fully implicit RK with Rana-type or monolithic multigrid preconditioning is competitive in runtime with DIRKs and more accurate (§1, §5). **Shown**

Claims 24 and 23 sit in tension inside the paper: the stage-order bound is
stated to govern index-2 accuracy, yet the Navier–Stokes runs reach formal
order. Claim 24's "stage order one or two" is loose: a DIRK with
nonsingular $A$ has stage order at most 1, and stage order 2 needs an
explicit first stage *(compiler check, not in the sources: $q\ge2$ requires
$a_{11}c_1=c_1^2/2$ with $c_1=a_{11}$, hence $a_{11}=0$)*.

# Printed slips

- Eq. 2.8 (p. 17:4): "$u^{n+1} = u^n + \sum_{i=1}^s b_ik_i$" lacks the factor $\Delta t$ of Eq. 2.3 and of the example that follows.
- Below Eq. 2.15 (p. 17:6): "$u_i = u^n + \Delta t\sum_{i=1}^s a_{ij}k_j$", summation index $i$ for $j$.
- Appendix A (p. 17:27), Alexander's DIRK: "$z = \frac32 x^{-}5x + \frac54$" is garbled; $z=\frac32x^2-5x+\frac54$ is intended, the value that makes $x+y+z=1$ *(compiler check)*.
- Fig. 5 caption "cubic serendipity elements on a 64 × 64 mesh" against the text's "fixed 256 × 256 mesh" (pp. 17:15–17:16).
- "five-stage RadauII approximation" (p. 17:17) for Radau IIA(5).
- Text cites "Leveque et al. [2023]" (p. 17:12); the reference list dates it 2024.
- "United Form Language (UFL)" (p. 17:2) against "Unified Form Language" in the abstract and references.
- "degree-2 DAEs" (p. 17:5) against "index 2 DAE" (p. 17:19).
- $\tilde P_{LD}$ in Eq. 3.5 is written $P_{LD}$ without tilde on p. 17:15.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $y'-F(t,y)=0$ | $y'=f(t,y)$ | the finite element form keeps a mass matrix on $u_t$ |
| $\Delta t$ | $h$ | the source's $h$ is the mesh size |
| $t^n$, $y^n$, $u^n$ | $t_n$, $y_n$ | |
| $A$, $\mathbf b$, $\mathbf c$, $s$ | $A$, $b$, $c$, $s$ | agrees |
| $k_i$ | $k_i=f(t_n+c_ih,Y_i)$ | stage derivatives, the unknowns of the default ("AI") formulation |
| $Y_i$, $u_i$ | $Y_i$ | stage values |
| $w_i=\sum_ja_{ij}k_j$ | same (page-local) | Butcher's transformed stage variables ("IA" splitting) |
| $M$ | $M$ | finite element mass matrix; **collision** with the Cahn–Hilliard mobility $M$ (§4.3) and the ratio $\Delta t=M/N$ (§4.1), here $m$ |
| $K$ | $K_{\mathrm{FE}}$ (page-local) | stiffness matrix; **collision** with the registry iteration count $K$ |
| $L$, $D$, $U$ | same (page-local) | additive (strict) split $A=L+D+U$ in §3.1, then multiplicative $A=LDU$ with unit triangular factors: two meanings in the source |
| $P_D$, $P_L$, $P_U$, $\tilde P_{LD}$, $\tilde A_{LD}$ | same (page-local) | stage preconditioners and the approximate Butcher matrix |
| $P_s(z)$ | same (page-local) | characteristic polynomial of $A^{-1}$; **collision** with the stability polynomial $P(z)$ |
| $A_i$, $V_i$, $p_i$, $r_i$ | same (page-local) | Schwarz patch operator and spaces; **collision**: $A_i$ is not the Butcher matrix |
| $g$, $g'$ | same (page-local) | Dirichlet data and its time derivative |
| $\lambda$, $f(c)$, $E(c)$, $\beta$ | same (page-local) | Cahn–Hilliard gradient coefficient, double-well potential, free energy, Nitsche penalty; **collisions** with the eigenvalue $\lambda$ and the right-hand side $f$ |
| formal order, stage order, WSO | $p$, $q$, $q_{\mathrm w}$ | WSODIRK$spq$: $s$ stages, order $p$, weak stage order $q_{\mathrm w}$ |

# Reference list

The paper prints 49 references in author–year style (ACM), alphabetical.
The list is merged complete into the [bibliography](/bibliography.md), with
`citedby` this slug. Two references are software or web items (the PETSc web
page, dated 2024 as printed, and the Zenodo code archive, 2025). Same-author
same-year pairs take suffixes: the PETSc manual and web page, Irksome and
PCPATCH (Farrell et al. 2021, keyed `farrell-2021` and `farrell-2021-c`; the
first is the ingested [Farrell et al. (2021)](/sources/farrell-2021.md)), and Southworth et al.
2022 parts I and II, printed part II first. "Wanner and Hairer [1996]" is
printed with the authors reversed; it is `hairer-1996`. No unparseable items.

# Pages created or updated

Chunk 6 (2026-10-20). This source is cited on:

* [Boundary conditions for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md)
* [Cahn–Hilliard equation](/benchmarks/cahn-hilliard-equation.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Differential-algebraic equations and their Runge–Kutta treatment](/definitions/differential-algebraic-equation.md)
* [Flow past a cylinder (Schäfer–Turek)](/benchmarks/flow-past-cylinder.md)
* [Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)](/methods/fully-implicit-runge-kutta.md)
* [Heat equation](/benchmarks/heat-equation.md)
* [Irksome](/software/irksome.md)
* [Runge–Kutta method](/definitions/runge-kutta-method.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Stage order](/definitions/stage-order.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
* [Stiff accuracy](/properties/stiff-accuracy.md)
