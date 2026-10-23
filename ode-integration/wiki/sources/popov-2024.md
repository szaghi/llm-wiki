---
type: Source
title: "Popov (2024) — Arbitrary High Order ADER-DG Method with Local DG Predictor for Solutions of Initial Value Problems for Systems of First-Order Ordinary Differential Equations"
description: "Uses ADER-DG with a nodal Gauss–Legendre local DG predictor as a one-step ODE solver, an (N+1)-stage implicit Runge–Kutta method in disguise, argues A- and L-stability from plots and a rank count, confirms orders 2N+1 at the nodes and N+1 for the local solution up to N=60 in 500-digit arithmetic, and tests a stiff flame problem."
resource: "doi:10.1007/s10915-024-02578-2"
source_kind: paper
authors: [Popov I.S.]
year: 2024
venue: "J. Sci. Comput. 100:22"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_Journal_of_Scientific_Computing_Popov_Arbitrary_High_Order_ADER-DG_Method_with_Local_DG_Predictor.pdf"
tags: [ader, implicit, stability, stiff, verification]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

ADER-DG with a local discontinuous-Galerkin predictor, developed by Dumbser and co-workers for
hyperbolic PDEs, is applied here as a stand-alone [ADER time integrator](/methods/ader-time-integration.md)
for $y'=f(t,y)$. On each step the local solution is a degree-$\mathsf M$ polynomial in the Lagrange
basis on the $\mathsf M+1$ Gauss–Legendre points. It solves the weak form of the ODE with the upwind
value $y_n$ at the left end. Representing $f$ by its nodal values turns the predictor into the
algebraic system $Y_p-h\sum_qa_{pq}f(t_n+c_qh,Y_q)=y_n$, solved by Picard or Newton iteration
to convergence. Gauss–Legendre quadrature then gives $y_{n+1}=y_n+h\sum_pb_pf(t_n+c_ph,Y_p)$.
The scheme is an $(\mathsf M+1)$-stage [implicit Runge–Kutta method](/methods/fully-implicit-runge-kutta.md),
and the paper uses that reading to write its [stability function](/definitions/stability-function.md).

The paper argues [A-stability](/properties/a-stability.md) from plotted stability regions for
$1\le \mathsf M\le60$. It argues L-stability ("more precisely L1-stable") from a rank count for
$\mathsf M\le80$: the numerator of $R$ has degree $\mathsf M$ and the denominator degree $\mathsf M+1$. It confirms
the orders $2\mathsf M+1$ at the grid nodes and $\mathsf M+1$ for the local solution, expected from
Baccouch's proofs for modal DG, on six non-stiff problems with $\mathsf M$ up to 60 in 500-digit
arithmetic (orders up to about 121). The local polynomial solution is offered as built-in
[dense output](/methods/dense-output.md), accurate between the nodes even on very coarse grids.
The stiff flame problem $y'=y^2-y^3$ is solved with Newton iterations, but the observed orders
collapse to values independent of $\mathsf M$, a possible case of [order reduction](/definitions/order-reduction.md)
that the paper attributes to the sharp layer.

A cost count finds more function and Jacobian evaluations per step than for Runge–Kutta
methods, and the Python/mpmath code is slower than scipy's integrators at comparable order.
It reaches errors that classical methods cannot reach on coarse grids. The introduction cites
[deferred correction](/methods/deferred-correction.md) and the
[DeC–ADER equivalence](/results/dec-ader-equivalence.md) as closely related. Apart from the
stability-function formula, every claim rests on computation.

# Version read

arXiv:2409.09933v1 [math.NA], 16 Sep 2024, in the Springer LaTeX template; the
acknowledgments thank anonymous reviewers, so it is most likely the accepted manuscript, not
the version of record. 44 pages, all read (pp. 7, 21–22, 26–27 and 31–33 also checked
visually). Page-1 title and author match Crossref up to capitalization; the file prints no
DOI. Equation, table, figure and page numbers cited here are those of the arXiv file.

# Key claims

Notation: $\mathsf M$ the polynomial degree (the source's $N$), $s=\mathsf M+1$ stages; $c_p$ the Gauss–Legendre nodes on
$[0,1]$, $b_p$ the Gauss–Legendre weights, $A=\mathcal D^{-1}\operatorname{diag}(b)$ the predictor matrix
built from the source's upwind matrix $\mathcal D$ (page-local, as on
[ADER](/methods/ader-time-integration.md)) and the diagonal time mass matrix $\operatorname{diag}(b)$; $Y_p$ the nodal predictor values; $y_L(t)$ the local
piecewise-polynomial solution.

1. The scheme is "a completely one-step ODE solver with uniform steps", simple to implement,
   and allows variable steps $h_n$. (Abstract, §1.1) **Stated**
2. The local DG predictor reduces to $Y_p-h\sum_{q=0}^{\mathsf M}a_{pq}f(t_n+c_qh,Y_q)=y_n$,
   $0\le p\le \mathsf M$, with $A=\mathcal D^{-1}\operatorname{diag}(b)$, using $\sum_q(\mathcal D^{-1})_{pq}\ell_q(0)=1$.
   (§1.1, Eqs. (9)–(12)) **Derived**
3. On Gauss–Legendre nodes the Lagrange basis is $L^2$-orthogonal, so the time mass matrix is
   $\operatorname{diag}(b)$, and the nodal representation of $f$ needs no integrals of $f$. (§1.1, Eq. (10))
   **Stated**
4. The update is Gauss–Legendre quadrature of the predictor,
   $y_{n+1}=y_n+h\sum_pb_pf(t_n+c_ph,Y_p)$. (Eq. (13)) **Derived**
5. The stability function is
   $R(z)=1+zb^\top(I-zA)^{-1}\mathbf 1=\det(I-zA+z\mathbf 1b^\top)/\det(I-zA)$, the implicit
   Runge–Kutta formula with Butcher matrix $A$ and weights $b$. (Eq. (15); see slips)
   **Derived**
6. The regions of instability for $1\le \mathsf M\le60$ are bounded closed curves in
   $\operatorname{Re}z>0$, so the method "is A-stable". (§1.2, Fig. 1) **Shown** (plots only)
7. $\operatorname{rank}(A-\mathbf 1b^\top)=\mathsf M$ and $\operatorname{rank}A=\mathsf M+1$ for
   $1\le \mathsf M\le80$; after cancelling $z^{\mathsf M+1}$, $R$ is a degree-$\mathsf M$ over degree-$(\mathsf M+1)$ rational
   function, so $\lvert R(z)\rvert\sim\lvert z\rvert^{-1}$ in every direction and the method is
   "L-stable; more precisely — L1-stable". (§1.2, Fig. 2) **Derived** (rank checked
   numerically)
8. Two outputs are produced: the nodal values $y_n$ and the local solution $y_L(t)$,
   discontinuous at the nodes, which "is not some kind of reconstruction ... it is precisely
   the representation of the solution in the form of a finite element". (§1.3, Eq. (16))
   **Stated**
9. Tabulating $y_L$ at many subnodes is one matrix product of precomputed basis values with
   the coefficient matrix. (§1.3) **Stated**
10. Harmonic oscillator on $[0,100\pi]$ with 96 steps ($h$ above half a period), double
    precision: with $\mathsf M=8$ the nodal solution reaches round-off and $y_L$ is very accurate;
    with $\mathsf M=16$ both reach round-off; with $\mathsf M=32$ only more of the $10^3$ subnodes of $y_L$
    reach errors of $10^{-15}$–$10^{-16}$. (§1.3, Fig. 3) **Shown**
11. The expected orders are $2\mathsf M+1$ at the nodes and $\mathsf M+1$ for the local solution, "expected
    to be correct" from Baccouch's proofs for modal Legendre DG and "typical for DG methods".
    (Introduction, Eq. (20)) **Stated** (no proof for this nodal variant)
12. Harmonic oscillator on $[0,2\pi]$, 500 digits: nodal orders match $2\mathsf M+1$ up to $\mathsf M=60$
    (121.01 at $\mathsf M=60$) and local orders match $\mathsf M+1$ (61.00), with a slight shortfall at
    $\mathsf M=1,2$; nodal and local error levels differ by up to 100 orders of magnitude at $\mathsf M=60$.
    (§2.1.1, Table 1, Fig. 4) **Shown**
13. $\ddot x-x=0$: nodal orders exceed $2\mathsf M+1$ by up to about 0.35 (7.31 against 7 at $\mathsf M=3$;
    121.22 against 121 at $\mathsf M=60$); local orders match $\mathsf M+1$. (§2.1.2, Table 2) **Shown**
14. Bratu initial-value problem: orders match for $\mathsf M<6$; nodal orders dip at $\mathsf M=7$–8
    (12.24–13.06 against 15 at $\mathsf M=7$), attributed to the chosen grid sequence, and exceed
    $2\mathsf M+1$ for $\mathsf M\ge10$ (42.65 against 41 at $\mathsf M=20$), "an unexpected result"; local orders
    match $\mathsf M+1$. (§2.1.3, Table 3) **Shown**
15. Linear third-order problem: nodal and local orders agree with $2\mathsf M+1$ and $\mathsf M+1$ within
    about 0.05 for $\mathsf M=1,\dots,60$. (§2.1.4, Table 4) **Shown**
16. Nonlinear third-order problem (29): nodal orders fall below $2\mathsf M+1$ for intermediate $\mathsf M$
    (39.25 against 41 at $\mathsf M=20$) and exceed it for $\mathsf M=50$–60 (122.93 against 121 at $\mathsf M=60$);
    local orders are close to $\mathsf M+1$. (§2.1.5, Table 5) **Shown**
17. Nonlinear third-order problem (32) on $[1,2]$: for $\mathsf M\ge25$ the nodal orders exceed
    $2\mathsf M+1$, by more than 2–4 at $\mathsf M=50$–60 (105.70 against 101 at $\mathsf M=50$). (§2.1.6, Table 6)
    **Shown**
18. In all non-stiff tests the nodal error grows roughly linearly in $t$; for $\mathsf M>1$ local and
    nodal error levels differ by orders of magnitude. (§2.1) **Shown**
19. Stiff flame problem $y'=y^2-y^3$, $y(0)=\varepsilon$, $t\in[0,2/\varepsilon]$, with
    $\varepsilon=10^{-4}$ on a graded grid: both $y_n$ and $y_L$ resolve the sharp
    transition near $t=1/\varepsilon$ for $\mathsf M=1,10,60$, without the artifacts reported in the
    literature; past the front the error is $10^{-128}$–$10^{-248}$. (§2.2, Fig. 10) **Shown**
20. With $\varepsilon=10^{-5}$ ("extreme stiffness") $\mathsf M=1$ places the front too late; the
    artifact vanishes as $\mathsf M$ grows or $h$ shrinks, and "can also be observed for the Radau IIA
    numerical method" in scipy. (§2.2, Fig. 11) **Shown**; the Radau IIA remark **Stated**
    (no figure)
21. Stiff orders: for $\varepsilon=10^{-4}$ the nodal orders saturate at 8.15, 8.02, 7.65
    ($L_1$, $L_2$, $L_\infty$) for every $\mathsf M\ge3$ (7.99–8.10 at $\mathsf M=2$, above the expected 5),
    the local ones at 6.50, 6.45, 5.93 for $\mathsf M\ge6$; for $\varepsilon=10^{-5}$ at 4.21, 4.08,
    3.78 (nodal) and 4.22, 4.20, 3.40 (local), with nodal $L_\infty$ order 0.04 at $\mathsf M=1$. The
    paper finds agreement "up to polynomial degree $\mathsf M\le3$" (nodes) and "$\mathsf M\le4$" (local)
    for $\varepsilon=10^{-4}$ and none for $\varepsilon=10^{-5}$, because "the solution
    changes too sharply". (§2.2, Table 7) **Shown**
22. On the stiff problem Picard iteration of the predictor diverges at large $h$ from simple
    initial guesses, so Newton is used; on the non-stiff problems either works. (§2.2)
    **Stated** (no data shown)
23. Each Picard iteration needs "at least $(\mathsf M+1)^2$" evaluations of $f$ and each Newton
    iteration also "$(\mathsf M+1)^2$" Jacobians assembled into an $(\mathsf M+1)d\times(\mathsf M+1)d$ matrix, while
    an $s$-stage implicit Runge–Kutta method needs $s$ evaluations and $s$ Jacobians for
    $I\otimes I-hA\otimes J$. (§2.3) **Stated**
24. "8th order methods are 11-stage"; the minimal stage count of a 121st-order explicit
    method is unknown, so the comparison of evaluation counts at very high order stays open.
    (§2.3) **Stated**
25. ADER-DG costs more $f$ and $J$ evaluations per step than explicit and implicit
    Runge–Kutta and Rosenbrock methods; better initial guesses reduce the iteration count but
    "will not affect the final asymptotic estimates". (§2.3, Conclusion) **Stated**
26. CPU time against nodal error (oscillator on $[0,10\pi]$, $\mathsf M=1,\dots,60$): the mpmath code
    is slower than scipy's RK23, RK45, DOP853 and Radau IIA(5) at comparable order, but for
    $\mathsf M\ge30$–35 (orders 61–71) it reaches errors "unattainable for classical Runge–Kutta
    methods" on coarse grids; the paper calls the comparison "not a representative result".
    (§2.3, Fig. 12) **Shown**
27. ADER and DeC are closely connected: explicit ADER can be read as a special DeC, and DeC
    methods "compete with" ADER and are easier to implement (citing Han Veiga et al.).
    (Introduction) **Stated**
28. Taylor and approximate-Taylor methods are close to the Cauchy–Kovalevskaya procedure of
    the original ADER, which modern ADER replaced by a local DG predictor; extrapolation
    methods "usually" give the solution only at the nodes. (Introduction) **Stated**

*(Compiler checks, not in the sources.)* For $f=\lambda y$ the nodal representation of $f$ is
exact, so the predictor is the classical upwind DG-in-time discretization of degree $\mathsf M$,
whose stability function is the $(\mathsf M,\mathsf M+1)$ subdiagonal Padé approximant of $e^z$, the
Radau IIA one. That gives A- and L-stability for every $\mathsf M$ and nodal order $2\mathsf M+1=2s-1$,
with no need for plots or rank checks; the paper does not make this identification (it is consistent with the
DG-in-time–Radau IIA equivalence recorded on the
[fully implicit Runge–Kutta](/methods/fully-implicit-runge-kutta.md) page), and its
evidence is computational, not a proof. "L1-stable" is a nonstandard label for
$R(z)=O(\lvert z\rvert^{-1})$. The cost count of claim 23 looks wrong by a factor $\mathsf M+1$: one
Picard sweep of the predictor evaluates $f$ at $\mathsf M+1$ nodes and one Newton step needs $\mathsf M+1$
Jacobians, as for an $s$-stage implicit method. Nodal orders above $2\mathsf M+1$ at $\mathsf M\ge25$ are fits
over six grids at errors of $10^{-100}$–$10^{-280}$ and are better read as pre-asymptotic. On
the flame problem the order 7.99 at $\mathsf M=2$ contradicts the claimed agreement "up to $\mathsf M\le3$",
and the common saturation for all $\mathsf M$ points to the layer resolution of the graded grids. The
abstract's "uniform steps" seems to mean the same formula on every step; there is no step-size
control.

# Printed slips

- Eq. (15), p. 7 (checked visually): the middle expression is printed
  $R(z)=1+\mathbf w^T[\mathrm E-z\mathrm B]^{-1}\mathbf 1$, missing the factor $z$ in front of
  $\mathbf w^T$; the determinant form $\lvert\mathrm E-z\mathrm B+z\mathbf 1\otimes\mathbf w\rvert/\lvert\mathrm E-z\mathrm B\rvert$
  is correct. (Found while compiling.)
- Eq. (27), second component: $2t\big((1-t^2)e^{-2t}-1\big)$ should be
  $2t\big((1-t)e^{-2t}-1\big)$, the derivative of $x=t^2e^{-2t}-t^2+3$.
- Eq. (26): $u_1(0)=1$, where (25) and the exact solution give $x(0)=3$.
- Eqs. (31)–(32): initial data printed at $t=0$ for the domain $1\le t\le2$; they are the
  values of $\sin4\pi t$ at $t=1$.
- §§2.1.3–2.1.6: step $\Delta t=2\pi/(L-1)$ copied from Examples 1–2 for domains of length 1.
- Eq. (34): "$u_1(0)=\delta$" for a scalar unknown. Eq. (19): stray "$dt$" in the $L_\infty$
  error. §2.1.3: "a number of steps $L=6$", where $L$ counts nodes.
- Figs. 10–11: zoom windows "$t\in[0.9995,1.0025]$" and "$t\in[0.999,1.001]$" lack the
  factor $1/\delta$. §2.2: "the results ... in case 2". Fig. 12 caption: "ADDER-DG", and
  "8, 9, 10 (12c)" with a stray "12".
- §1.1: "Legendre interpolation polynomials" for the Lagrange basis; §1.2: "local DG prector".
  Introduction: "[42, 42–44]".
- Reference slips: [19] garbled volume and year; [41] authors "Daniel, V. J.W. amd Pereyra,
  Schumaker, L.L."; [42] "Dutt, A., Greengard, L., V., R."; [43], *Semi-implicit spectral
  deferred correction methods for ordinary differential equations* (Commun. Math. Sci. 1, 2003),
  is printed with the authors of [46] (Abgrall, Bacigaluppi, Tokareva), while title, venue and
  pages are those of Minion's paper; [31] "Front. Phys. 32, 8 (2020)" with volume and article number apparently
  swapped; [62] pages "4232–42471"; [63], [65] "Shampine, L.W."; [13] "Hou, S., , Shu".

# Notation map

| Popov | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $du/dt=F(u,t)$, $u\in\mathbb R^K$ | $y'=f(t,y)$, $y\in\mathbb R^d$ | **source $K$ is the dimension, not the registry iteration count** |
| $f=\Delta t_nF$ | $hf$ | right-hand side rescaled to $[0,1]$ |
| $t_n$, $\Delta t_n$, $\Omega_n$ | $t_n$, $h_n$, $[t_n,t_{n+1}]$ | |
| $\tau$, $t=t_n+\Delta t\,\tau$ | $\theta$, $t=t_n+\theta h$ | local time |
| $u_n$ | $y_n$ | nodal solution |
| $q(\tau)$, $\hat q_p$ | $Y_p$ | predictor; nodal values are stage values |
| $u_L(t)$ | $y_L(t)$ | local piecewise-polynomial solution |
| $N$ | $\mathsf M$, $s=\mathsf M+1$ | polynomial degree; stages; registry $N$ is the number of parallel-in-time slices |
| $\phi_p(\tau)$ | $\ell_p(\theta)$ | Lagrange basis on Gauss–Legendre nodes; **not the registry $\phi_k$ functions** |
| $\tau_p$, $w_p$ | $c_p$, $b_p$ | Gauss–Legendre nodes and weights |
| $K=\lVert K_{pq}\rVert$ | $\mathcal D$, page-local | upwind "stiffness" matrix; **clashes with the source's own dimension $K$** |
| $M=\lVert M_{pq}\rVert$ | $\operatorname{diag}(b)$ | diagonal time mass matrix; **not the registry mass matrix $M$, and the source reuses $M$ for the $10^3$ subnodes** |
| $B=K^{-1}M$ | $A$ | Butcher matrix |
| $E$, $\mathbf 1\otimes w$ | $I$, $\mathbf 1b^\top$ | |
| $z=\lambda\Delta t_n$, $R(z)$ | $z=h\lambda$, $R(z)$ | region printed with strict $\lvert R\rvert<1$ |
| $\nu$ | kept | variable of $\lvert A-\nu E\rvert$, $z=1/\nu$ |
| $\xi_m$, $t_{n,m}$ | $\xi_m$, page-local | tabulation points of $y_L$, not the registry subnodes $t_{n,m}$ |
| $\delta$ | $\varepsilon$ | flame-problem stiffness parameter |
| $J=\partial F/\partial u$ | $J$ | |
| $s$, $A$ (comparison IRK) | $s$, $A$ | |
| $L$ | kept | number of grid nodes; $\Delta t=\lvert\Omega\rvert/(L-1)$; **not the registry linear operator** |
| $W$ | kept | Lambert W function |

# Reference list

65 printed references, numbered [1]–[65] in Springer style, no DOIs. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` popov-2024. Parse problems
recorded as printed, with the printed form in each `note`: [19] (garbled volume and year), [41]
and [42] (garbled author lists, entered with the evident authors Daniel J.W., Pereyra V.,
Schumaker L.L. and Dutt A., Greengard L., Rokhlin V.), [43] (misattributed authors; entered as Minion (2003), `minion-2003`, by title, venue and pages), [63]
and [65] (Shampine L.F. for "L.W."). Same-key works take suffixes in printed order: Baccouch
2016, 2017, 2021 and 2023, Cockburn 1989, Dumbser 2014 and 2018, Zanotti 2015. [40] is the
ingested [Han Veiga et al. (2021)](/sources/hanveiga-2021.md).

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [ADER as a time integrator](/methods/ader-time-integration.md)
* [Deferred correction (DeC)](/methods/deferred-correction.md)
* [Dense output](/methods/dense-output.md)
* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Equivalence of DeC and ADER](/results/dec-ader-equivalence.md)
* [Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)](/methods/fully-implicit-runge-kutta.md)
* [Lax–Wendroff flux reconstruction (single-stage Taylor time stepping)](/methods/lax-wendroff-flux-reconstruction.md)
* [Order reduction](/definitions/order-reduction.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
