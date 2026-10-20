---
type: Source
title: "Buvoli & Southworth (2023) — Additive Polynomial Time Integrators, Part I: Framework and Fully Implicit-Explicit Collocation Methods"
description: "Extends the polynomial time-integrator framework to additively partitioned problems and builds FIMEX-Radau methods, whose implicit part is exactly Radau IIA and whose explicit part reuses the previous step's derivatives, with iterator sweeps that raise the order; they beat IMEX Runge–Kutta on KdV, Van der Pol and DG tests."
resource: "doi:10.1137/21M1446988"
source_kind: paper
authors: [Buvoli T., Southworth B.S.]
year: 2023
venue: "SIAM J. Sci. Comput. 45:A2945-A2972"
local_file: "/home/stefano/papers/mosaic/ode-integration/2023_Crossref_SIAM_Journal_on_Scientific_Computing_Buvoli_Additive_Polynomial_Time_Integrators_Part_I_main_paper.pdf"
tags: [imex, polynomial-integrators, fully-implicit, order-reduction, general-linear-methods, parallel]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper extends the [polynomial time-integrator](/methods/polynomial-time-integrators.md)
framework of Buvoli and Tokman to additively partitioned problems
$y'=\sum_kf^{\{k\}}(t,y)$. In that framework every coefficient comes from
interpolating polynomials ("ODE polynomials") through block inputs, outputs
and stages. A node set is scaled by a node radius $r$ and advanced by an
extrapolation factor, so that the step is $h=r\alpha$. The paper defines
partitioned datasets, total derivatives and partitioned Adams and BDF ODE
polynomials. It writes additive polynomial block methods in coefficient
form, shows in the supplement that each IMEX one is a parametrized IMEX
general linear method, and defines linear stability through the partitioned
Dahlquist equation.

The main construction is the FIMEX ("fully implicit-explicit") family. Its
implicit part is exactly the $(q-1)$-stage Radau IIA collocation method of
order $2q-3$ ([fully implicit RK](/methods/fully-implicit-runge-kutta.md)),
rewritten as a multivalued block method on $q$ nodes. Its explicit part
integrates a Lagrange polynomial through the previous step's derivatives:
through the $q-1$ Radau nodes (FIMEX-Radau, explicit order $q-1$) or through
all $q$ nodes (FIMEX-Radau*, order $q$). This sidesteps the obstacle to
[IMEX Runge–Kutta](/methods/imex-runge-kutta.md) methods with a fully
implicit part. An "iterator" ($\alpha=0$) raises the order of the block by
one per sweep, up to $2q-3$. It yields starting values and composite methods
FIMEX-Radau$(q,\kappa)$. The stage systems have the Radau IIA structure, so
block preconditioners for fully implicit RK
([stage solvers](/methods/implicit-stage-solvers.md)) apply unchanged. The
$q$ explicit evaluations are independent and can run in parallel.

Evidence is numerical; no theorem is proved. On the
[Korteweg–de Vries equation](/benchmarks/korteweg-de-vries-equation.md)
with OpenMP-parallel evaluations, FIMEX-Radau* is about 2 to 30 times faster
than IMEX-RK. On the [Van der Pol oscillator](/benchmarks/van-der-pol-oscillator.md)
with $\varepsilon$ down to $10^{-8}$, FIMEX stays stable over the whole step
range, where IMEX-RK with a linearly implicit splitting does not, and the
[order reduction](/definitions/order-reduction.md) study shows each iterator
sweep adding about one order. In DG advection–diffusion(–reaction) tests
FIMEX-Radau* beats IMEX-RK and DIRK in error per wall-clock time.

# Version read

Two files were read. The main file (the `local_file`) is the arXiv
preprint 2109.03317v2 [math.NA], 30 Dec 2022, not the journal typeset. It
has 37 PDF pages: 29 pages of paper (references pp. 27–29) followed by the
arXiv copy of the supplement (SM1–SM8). Its page-1 title reads "…Fully-Implicit-Explicit
(FIMEX) Collocation Methods"; the published title has no "(FIMEX)". Its
cross-references to the supplement print as "??". The second file,
`2023_Crossref_SIAM_Journal_on_Scientific_Computing_Buvoli_Additive_Polynomial_Time_Integrators_Part_I_Framework_and_Fu.pdf`
in the same archive folder, is the SIAM supplementary material of the
version of record (8 pages, SM1–SM8: coefficients and a MATLAB script,
FIMEX-Radau stability, Van der Pol figures, polynomial block methods as
general linear methods). It prints the DOI and resolves the cross-references.
The two supplement copies differ in the row labels of Fig. SM1 (see Printed
slips). Numbering on this page is that of the arXiv v2 file; SM numbers are
common to both.

# Key claims

Notation: $f^{\{1\}}=f^{\mathrm I}$ (implicit, stiff) and $f^{\{2\}}=f^{\mathrm E}$
(explicit) when $m=2$; $q$ is the number of block nodes (**not** the stage
order); $\kappa$ the number of iterator sweeps.

1. The additive polynomial framework builds additive integrators of any order for any number $m$ of partitions without nonlinear order conditions, because all coefficients come from interpolating polynomials; high-degree ODE polynomials give high stage order, which "prevents order reduction on stiff problems" (§1, §7). **Stated**
2. Any additive integrator that treats $f^{\{1\}}=J_ny$ implicitly and $f^{\{2\}}=f-J_ny$ explicitly is a linearly implicit method (a W-method if $J_n$ is approximate) (§1, Eq. 1.3). **Stated**
3. IMEX RK methods cannot be built on fully implicit RK methods, "since the explicit stages would be nonlinearly coupled to the fully implicit stages"; the polynomial framework avoids this by taking derivatives from the previous step (§1). **Stated**
4. The order of a polynomial method is at least $\min(g_{\min},\delta-1)$, with $g_{\min}$ the minimum ODE-polynomial degree and $\delta$ the minimum degree of the polynomials that give the approximate derivatives (§3, citing Buvoli's thesis). **Stated**
5. The block method (3.12) on the Radau nodes $\{-1,2x_1-1,\dots,2x_{q-1}-1\}$ with $\alpha=2$, $b=1$ is the $(q-1)$-stage Radau IIA method of order $2q-3$ with $h=2r$; for general $b,\alpha$ it is a fully implicit multivalued integrator of order $q-1$ (§3.1, Eq. 3.13). **Derived**
6. Additive polynomial block methods (4.9) with $m=2$ and a strictly lower triangular explicit matrix are IMEX general linear methods with $3q$ inputs and $q$ stages, parametrized by $\alpha$ (§4.2; SM4). **Derived**
7. The order of FIMEX (5.5) is the minimum of the implicit order $2q-3$ and the explicit order, $q-1$ for FIMEX-Radau and $q$ for FIMEX-Radau*; for every $q>2$ the explicit part limits the accuracy (§5). **Stated**
8. For $q=2$, FIMEX-Radau is IMEX Euler, and FIMEX-Radau* is backward Euler for $f^{\{1\}}$ with the second-order Adams–Bashforth method for $f^{\{2\}}$ (§5). **Derived**
9. For $q>2$ the implicit equations of FIMEX-Radau are those of Radau IIA with a modified right-hand side, so fully implicit RK solvers apply unchanged (§5). **Stated**
10. If the first block value has order $2q-3$ or higher, each iterator sweep (5.8) raises the order of all other block values by one, up to $2q-3$; a converged iteration reproduces the outputs and stages of Radau IIA (§5.1). **Stated**
11. Starting procedure: a constant initial guess $y_0$ followed by $\kappa$ iterator sweeps, with minimum $\kappa=q-1$ for FIMEX-Radau and $\kappa=q$ for FIMEX-Radau* (§5.1, Eq. 5.10). **Stated**
12. Composite orders: FIMEX-Radau$(q,\kappa)$ has order $\min(2q-3,q-1+\kappa)$ and FIMEX-Radau*$(q,\kappa)$ has order $\min(2q-3,q+\kappa)$ (§5.2, Eqs. 5.12–5.13). **Stated** (checked numerically in §6)
13. With iterative solvers the iterator's implicit solve is much faster than the propagator's, thanks to the good initial guess (§5.2). **Stated**
14. FIMEX-Radau*$(4,\kappa)$ stability regions in the explicit variable always enclose the imaginary axis for the three values of $\arg$ of the implicit variable shown; for $\kappa=0$ they are small in the oscillatory case, and one iterator sweep enlarges them markedly; the lower-order explicit polynomial (FIMEX-Radau) gives larger regions than FIMEX-Radau* (§5.3, Fig. 4; Fig. SM1). **Shown**
15. KdV (512 Fourier modes): the serial seventh-order FIMEX-Radau*(5,2) beats all other methods below relative error $10^{-2}$; with OpenMP (5 threads) it is the most efficient at all accuracies, about 2 times faster than any RK method at $10^{-2}$ and about 30 times faster than IMEX-RK4 below $10^{-4}$ (§6.1.2, Fig. 5). **Shown**
16. FIMEX-Radau*(3,2) converges at fourth order over most of the step range and beats IMEX-RK4 while storing three solution vectors instead of five; FIMEX-Radau*(2,1) is more efficient and more stable than IMEX-RK1 (§6.1.2). **Shown**
17. Van der Pol, $\varepsilon\in[10^{-8},1]$: FIMEX-Radau and FIMEX-Radau* are stable for all $h\in[10^{-4},0.25]$ with both the semi-implicit and the linearly implicit splitting; all IMEX-RK methods tested needed much smaller steps with the linearly implicit splitting (§6.2, Fig. 6, Fig. SM4). **Shown**
18. For small $\varepsilon$ each iterator sweep raises the observed order by about one; with the semi-implicit splitting the $\kappa=2$ methods show reduced rates for $\varepsilon\in[10^{-4},10^{-2}]$ but remain the most accurate; FIMEX-Radau*(5,0) with the linearly implicit splitting does not converge at large steps, and $\kappa=1$ fixes it (§6.2). **Shown**
19. In the DG advection–diffusion test only the Ascher–Ruuth–Spiteri IMEX-RK schemes whose two parts are both stiffly accurate (IMEX(1,1,1), (2,2,2), (4,4,3)) were reasonably stable; IMEX(1,2,1) is very unstable at the forward-Euler advective limit (§6.3.1, Fig. 7). **Shown**
20. DG advection–diffusion: FIMEX-Radau methods are the most efficient below about $10^{-3}$; for diffusion coefficients 0.1 and 10, FIMEX-Radau* reaches about $10^{-5}$ "≈16× and ≈16× faster" than the best IMEX-RK, IMEX(4,4,3); all methods show some order reduction, FIMEX-Radau* with much smaller error constants (§6.3.1, Fig. 8). **Shown**
21. At diffusion coefficient 0.01 and $h=0.01$ only IMEX(1,1,1) and IMEX(4,4,3) among the IMEX-RK schemes do not diverge; FIMEX-Radau*(4,2) reaches $\ell^2$ error $2.9\cdot10^{-8}$ in 184 s against $7.4\cdot10^{-5}$ in 165 s for IMEX(4,4,3) (§6.3.1, Table 1). **Shown**
22. DG advection–diffusion–reaction with explicit reaction: IMEX schemes beat DIRK with simplified Newton in accuracy per wall-clock time; FIMEX-Radau* is best below about $10^{-4}$, and at third order and fixed $h$ its error is 10 to 100 times smaller than that of comparable IMEX-RK (§6.3.2, Fig. 9). **Shown**
23. Treating the reaction explicitly avoids rebuilding the algebraic multigrid solver at every step or nonlinear iteration (§6.3.2). **Stated**
24. Additive linear multistep methods are cheap but high-order ones become unstable with little diffusion; additive DIRK methods suffer order reduction on stiff problems; high-order additive RK construction through nonlinear order conditions becomes increasingly difficult (§1). **Stated**

Claim 1 is not proved, and the paper's own results show order reduction
(claims 18 and 20). §5.3 states that with the semilinear splitting (2.4)
the additive stability region equals that of the implicit Radau IIA part;
that holds only when the explicit part vanishes on the linear test problem,
as with the fully linearized splitting (2.7) or (2.8) with the exact
Jacobian, so the equation reference is likely wrong *(compiler check, not in
the sources)*.

# Printed slips

- Fig. 4 (arXiv v2, p. 18) labels its rows $\arg(z_1)=0,\frac{3\pi}{2},\frac{\pi}{2}$, and p. 17 calls $\arg(z_1)=0$ "the diffusive case", while the same page says $\arg(z_1)=\pi$ represents a symmetric positive-definite diffusion. The SIAM supplement's Fig. SM1 labels the rows $\pi,\frac{3\pi}{4},\frac{\pi}{2}$; the arXiv copy of SM1 keeps $0,\frac{3\pi}{2},\frac{\pi}{2}$. The published version corrected the labels.
- p. 17: "the stability regions grow slowly in $r$", where the plotted parameter is $\lvert z_1\rvert$; "For the remaining splittings (2.4)-(2.6)" after (2.4) has been treated.
- (5.14) is called a "five-dimensional stability region" for $z_1,z_2\in\mathbb C$ at fixed $\alpha$: four real dimensions.
- (5.17): both arguments of the max are printed $\rho(\mathbf M(\gamma e^{i\theta},z_2,2))$ (the conjugate was presumably intended), and no "$<1$" condition is printed.
- (3.10) speaks of "$m$ collocation points" but sums over $j=1..\sigma$; end of §2: "high-order additive integrators for (2.3)", where (2.3) is IMEX Euler and (2.1) is meant.
- (4.7): $H_y$ of degree $g$ "satisfies $g-1$ solution values", then $g$ interpolation conditions; §4.1.1 refers to "(4.6)" for the classical Adams polynomial (3.5).
- §5: polynomials "of order $q-2$", "$q-1$" for degree.
- §6.1.1: the implicit solve is printed "$(I-rL_{kk}\mathbf B^{\{2\}})x=b$"; the implicit matrix is $\mathbf B^{\{1\}}$. The error norm is printed "$\|y-y_{\rm ref}\|_\infty/\|]y_{\rm ref}\|$".
- §6.3.1 (p. 23): "run to final (simulation) time tf = 2 120 total MPI processes" (merged sentence); "≈16× and ≈16× faster" (duplicated factor); "RK(1,2,1)", "RK(2,2,2)" for IMEX(1,2,1), IMEX(2,2,2).
- §6.1.2 discusses "FIMEX-Radau*(2,1)" while Fig. 5 shows FIMEX-Radau*$(q,2)$.
- Typos: "interator", "converence", "noticable".
- References: [28] (Hairer–Nørsett–Wanner, Solving ODEs I) printed as "SIAM Review, 8 (1993), p. 528"; [29] (a 1999 J. Comput. Appl. Math. Radau paper) is cited with book locators "[29, IV.2]", "[29, p. 403]" that match Solving ODEs II, which is [47]; [47] prints the authors as "G. Wanner and E. Hairer"; [9] "University of Washigton"; [46] carries "www.scopus.com. Cited By :19."
- Supplement: SM1.1 announces coefficients for $q=3$ and $q=4$, then gives $q=2,3,4$; SM4 writes "a GLM with q = 3q inputs" and "Butcher tablue".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $f^{\{k\}}$, $m$ | $f^{\{q\}}$ (GARK partitions); $f^{\mathrm I}=f^{\{1\}}$, $f^{\mathrm E}=f^{\{2\}}$ | $m$ partitions; the source also uses $m$ for collocation points in (3.10) |
| $h=r\alpha$ | $h$ | step |
| $r$ | same (page-local) | node radius; **collision** with the step ratio $r_n$ |
| $\alpha$ | same (page-local) | extrapolation factor; **collision** with Shu–Osher and Rosenbrock $\alpha$ |
| $q$ | same (page-local) | number of block nodes; **collision** with the stage order $q$ |
| $\sigma$ | $s$ | RK stages in §3.1; Radau IIA has $s=q-1$ |
| $z_j$ | same (page-local) | block nodes in $[-1,1]$; **collision** with $z=h\lambda$, which the source also uses as $z_k=h\lambda_k$ |
| $\lambda_k$, $z_k=h\lambda_k$ | $\lambda$, $z$ per partition | partitioned Dahlquist equation $y'=\sum_k\lambda_ky$ |
| $y_j^{[n]}$, $f_j^{\{k\}[n]}$ | same (page-local) | block inputs and derivatives at $t_n+rz_j$ |
| $Y_{j-1}=y_j^{[n+1]}$ | $Y_i$ | Radau IIA stage values in the block form |
| $p(\tau;b)$, $a_j(b)$, $L_y$, $L_f$, $H_y$ | same (page-local) | ODE polynomial, expansion point, interpolants; $b$ **collides** with the RK weights |
| $\mathbf A$, $\mathbf B^{\{k\}}$, $\mathbf C^{\{k\}}$ | same (page-local) | block-method coefficient matrices (bold); **collision** with the Butcher $A$ |
| $P$, $M$, $M^\kappa$ | same (page-local) | propagator and iterator; **collision**: $M$ is the mass matrix, $P$ the stability polynomial |
| $\kappa$ | same (page-local) | number of iterator sweeps |
| $\mathbf M(z_1,\dots,z_m,\alpha)$ | same (page-local) | amplification matrix of the partitioned Dahlquist problem |
| $J_n$ | $J_n$ | agrees |
| $\epsilon$ | $\varepsilon$ | Van der Pol stiffness; **collision**: in §6.3 it is the DG diffusion coefficient |
| $F$ | same (page-local) | total derivative; **collision** with the elementary differential $F(\tau)$ |
| IMEX$(s,\sigma,p)$ | same | Ascher–Ruuth–Spiteri naming |

# Reference list

The paper prints 48 references in numbered style ([1]–[48]), alphabetical.
The list is merged complete into the [bibliography](/bibliography.md), with
`citedby` this slug. The supplement has no reference list. Arxiv-only items
([11], [26], [27], [31], [38], [43], [44]) are kept as their own preprint
entries. [43] is the arXiv form of Part II of Southworth et al.'s
fully-implicit-RK preconditioning paper, `southworth-2021-b`, and stays
distinct from the published southworth-2022; [44] (Part I) is
`southworth-2021`. Ref. [2] (MFEM, printed 2020 without volume) is merged into
the published `anderson-2021`. Printed oddities ([28], [29], [46], [47], see
Printed slips; [45] without volume) are kept as printed: [28] is merged into
`hairer-1993`, [29] is `hairer-1999`, and [47], printed "G. Wanner and E.
Hairer", is `hairer-1996` (author order reversed in print). No printed duplicates.

# Pages created or updated

Chunk 6 (2026-10-20). This source is cited on:

* [Additive polynomial time integrators and FIMEX collocation methods](/methods/polynomial-time-integrators.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)](/methods/fully-implicit-runge-kutta.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [Korteweg–de Vries equation](/benchmarks/korteweg-de-vries-equation.md)
* [Order reduction](/definitions/order-reduction.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Van der Pol oscillator](/benchmarks/van-der-pol-oscillator.md)
