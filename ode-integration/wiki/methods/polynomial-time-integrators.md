---
type: Method
title: "Additive polynomial time integrators and FIMEX collocation methods"
description: "Polynomial time integrators build every coefficient from interpolating polynomials through a block of solution and derivative values; their additive extension yields FIMEX-Radau methods, whose implicit part is exactly Radau IIA and whose explicit part integrates the previous step's derivatives, plus iterator sweeps that raise the order."
status: established
aliases: [polynomial block method, PBM, additive polynomial block method, FIMEX, FIMEX-Radau, FIMEX-Radau*, fully implicit–explicit method, ODE polynomial, polynomial iterator, composite polynomial method]
tags: [imex, implicit, runge-kutta, order-reduction, parallel]
timestamp: 2026-10-20T16:00:00Z
---

# Additive polynomial time integrators and FIMEX collocation methods

A **polynomial time integrator** in the framework of Buvoli and Tokman, as recalled and
extended by [Buvoli & Southworth (2023)](/sources/buvoli-2023.md) (§3), carries a block of
solution values at scaled nodes and computes every output from **ODE polynomials**,
interpolating polynomials through solution and derivative values. No nonlinear order
conditions are solved: the coefficients are integrals of Lagrange basis polynomials, and
the order follows from the polynomial degrees. Buvoli & Southworth extend the framework
to additively partitioned problems $y'=\sum_qf^{\{q\}}(t,y)$ and build from it
**fully implicit–explicit (FIMEX)** methods for $y'=f^{\mathrm E}+f^{\mathrm I}$, whose
implicit part is exactly a [Radau IIA](/methods/fully-implicit-runge-kutta.md) collocation
method and whose explicit part needs no explicit stage inside the step. This answers what
they state cannot be done with [IMEX Runge–Kutta methods](/methods/imex-runge-kutta.md):
pairing an explicit method with a fully implicit one, "since the explicit stages would be
nonlinearly coupled to the fully implicit stages" (§1).

## The polynomial framework

Page-local symbols, used on this page only: the node radius $r>0$, the extrapolation
factor $\alpha$ with step $h=r\alpha$, nodes $\mathsf z_1,\dots,\mathsf z_{s+1}$ in $[-1,1]$
(sans-serif, distinct from $z=h\lambda$), a local time coordinate $\vartheta$ with
$t=t_n+r\vartheta$, and an expansion point $\mathsf b$ (distinct from the weights $b$). A
**polynomial block method** (PBM) carries the block $y^{[n]}_j\approx y(t_n+r\mathsf z_j)$
and produces $y^{[n+1]}_j\approx y(t_n+r\mathsf z_j+h)$; it has no stages in the
source's convention (§3, Eqs. (3.1)–(3.9)). Two families of ODE polynomials are used:

- **Adams type**: $p(\vartheta;\mathsf b)=L_y(\mathsf b)+\int_{\mathsf b}^{\vartheta}L_f(\xi)\,d\xi$,
  with $L_y$ interpolating solution values and $L_f$ (degree one less) interpolating
  scaled derivative values $r f_j$ (Eqs. (3.4)–(3.5); $\xi$ the integration variable);
- **BDF type**: the polynomial through solution values whose derivative matches one
  derivative value; it does not depend on $\mathsf b$ (Eq. (3.6)).

Every output is $y^{[n+1]}_j=p_j(\mathsf z_j+\alpha;\mathsf b_j)$. BDF, Adams–Moulton and
collocation methods are PBMs with a fixed $\alpha$ (§3). Setting $\alpha=0$ gives an
**iterator**, which recomputes the current block; iterators are related to
predictor–corrector block methods and to [spectral deferred
correction](/methods/deferred-correction.md) sweeps (§3.2). The order of a polynomial
method is bounded below by the minimum of the smallest ODE-polynomial degree and one less
than the smallest degree of the polynomials that supply derivatives (§3, citing Buvoli's
thesis).

**Radau IIA as a block method** (§3.1, Eqs. (3.11)–(3.13)). Take $s+1$ nodes,
$\mathsf z_1=-1$ and $\mathsf z_{j+1}=2c_j-1$ with $c_j$ the $s$-stage Radau IIA abscissae,
let $L_y$ interpolate all inputs and $L_f$ the new derivatives at nodes $2,\dots,s+1$,
and set $\alpha=2$, $\mathsf b=1$. Then the last input node coincides with the first output
node, $y^{[n+1]}_1=y^{[n]}_{s+1}$, and the method is the $s$-stage Radau IIA method of
order $2s-1$ with $h=2r$: the Runge–Kutta step maps $y_n=y^{[n]}_{s+1}$ to
$y_{n+1}=y^{[n+1]}_{s+1}$ with stage values $Y_j=y^{[n+1]}_{j+1}$. For $s=2$, nodes
$(-1,-\tfrac13,1)$, the printed coefficients $\tfrac56,-\tfrac16$ and $\tfrac32,\tfrac12$ of
$rf$ become, with $r=h/2$, the Radau IIA rows $(\tfrac5{12},-\tfrac1{12})$ and
$(\tfrac34,\tfrac14)$ *(compiler check, not in the source)*. For general $\alpha$ and
$\mathsf b$ the same construction is an $s$-th-order fully implicit multivalued method.

## Additive extension

Buvoli & Southworth (2023, §4) define, for $y'=\sum_qf^{\{q\}}$:

- a **partitioned ODE dataset**, which stores each component $rf^{\{q\}}_j$ separately
  (Def. 4.1), and a **total derivative**, the sum of components taken at one node
  (Def. 4.2);
- **partitioned ODE polynomials**, whose coefficients come either from polynomials
  through solution values and total derivatives, or from sums
  $\sum_q l^{\{q\}}$ of polynomials each interpolating one component, possibly on
  different nodes (Def. 4.3); the partitioned Adams form is
  $p(\vartheta;\mathsf b)=L_y(\mathsf b)+\int_{\mathsf b}^{\vartheta}\sum_qL^{\{q\}}_f(\xi)\,d\xi$
  (Eqs. (4.5)–(4.6));
- **additive PBMs** in coefficient form
  $\mathbf y^{[n+1]}=\mathbf A(\alpha)\mathbf y^{[n]}+r\sum_q\mathbf B^{\{q\}}(\alpha)\mathbf f^{\{q\}[n]}+r\sum_q\mathbf C^{\{q\}}(\alpha)\mathbf f^{\{q\}[n+1]}$
  with $(s+1)\times(s+1)$ matrices (Eq. (4.9); bold block vectors and matrices are
  page-local).

With two partitions and $\mathbf C^{\{\mathrm E\}}$ strictly lower triangular, an additive
PBM is an IMEX **general linear method** with $3(s+1)$ inputs (the block and both
derivative blocks of the previous step), $s+1$ stages and coefficient matrices
parametrized by $\alpha$ (supplement SM4, Eq. (SM4.5)). Linear stability is defined on
the partitioned Dahlquist problem $y'=\lambda_{\mathrm I}y+\lambda_{\mathrm E}y$, with
$z_{\mathrm I}=h\lambda_{\mathrm I}$, $z_{\mathrm E}=h\lambda_{\mathrm E}$ (page-local):
the block recursion has an amplification matrix, and the stability region is the set of
$(z_{\mathrm I},z_{\mathrm E})$ where it is power bounded (§4.3, Eqs. (4.10)–(4.12)). The
paper plots slices: for fixed $\arg z_{\mathrm I}$ (about $\pi$ for symmetric positive
definite diffusion, $\pi/2$ for skew-symmetric advection) the set of stable
$z_{\mathrm E}$ as $\lvert z_{\mathrm I}\rvert$ grows (Eqs. (5.15)–(5.17)).

## FIMEX-Radau and FIMEX-Radau*

The FIMEX methods use a doubly partitioned Adams polynomial (§5, Eqs. (5.2)–(5.5)):

- $L_y$ of degree $s$ through all $s+1$ inputs, $\alpha=2$, $\mathsf b=1$;
- $L_f^{\mathrm I}$ through the **new** implicit derivatives $rf^{\mathrm I}$ at nodes
  $2,\dots,s+1$, i.e. the Radau IIA construction above;
- $L_f^{\mathrm E}$ through the **previous step's** explicit derivatives, at nodes
  $2,\dots,s+1$ (**FIMEX-Radau**, explicit order $s$) or at all $s+1$ nodes
  (**FIMEX-Radau\***, explicit order $s+1$).

Every output is $y^{[n+1]}_j=y^{[n]}_{s+1}+\int_1^{\mathsf z_j+2}\bigl(L^{\mathrm I}_f+L^{\mathrm E}_f\bigr)\,d\xi$.
The order is the minimum of the implicit order $2s-1$ and the explicit order, i.e. $s$
for FIMEX-Radau and $s+1$ for FIMEX-Radau\*; for $s\ge2$ the explicit part limits
accuracy (§5). For $s=1$, FIMEX-Radau is IMEX Euler, and FIMEX-Radau\* is backward Euler
combined with second-order Adams–Bashforth for the explicit part (§5). For $s=2$
(Eq. (5.6)):

$$\begin{aligned}
y^{[n+1]}_1&=y^{[n]}_3,\\
y^{[n+1]}_2&=y^{[n]}_3+r\bigl(\tfrac56f^{\mathrm I[n+1]}_2-\tfrac16f^{\mathrm I[n+1]}_3\bigr)+r\bigl(-\tfrac16f^{\mathrm E[n]}_2+\tfrac56f^{\mathrm E[n]}_3\bigr),\\
y^{[n+1]}_3&=y^{[n]}_3+r\bigl(\tfrac32f^{\mathrm I[n+1]}_2+\tfrac12f^{\mathrm I[n+1]}_3\bigr)+r\bigl(-\tfrac32f^{\mathrm E[n]}_2+\tfrac72f^{\mathrm E[n]}_3\bigr),
\end{aligned}$$

with $f^{\mathrm I[n+1]}_j=f^{\mathrm I}(t_n+r\mathsf z_j+h,y^{[n+1]}_j)$ and
$f^{\mathrm E[n]}_j=f^{\mathrm E}(t_n+r\mathsf z_j,y^{[n]}_j)$. The FIMEX-Radau\* explicit
rows for $s=2$ are $(\tfrac8{27},-\tfrac{11}{18},\tfrac{53}{54})$ and
$(4,-\tfrac{15}2,\tfrac{11}2)$ on all three nodes (supplement SM1.1). Both sets of
explicit coefficients are reproduced by integrating the Lagrange basis on the printed
nodes *(compiler check, not in the source)*. The supplement tabulates the coefficients
for $s\le3$ and gives a MATLAB generator for nodes up to $s=7$ and beyond through
Chebfun (SM1.1–SM1.2).

**Structure of the solve.** The implicit equations are those of standard Radau IIA with a
modified right-hand side, so solvers and preconditioners for
[fully implicit Runge–Kutta methods](/methods/fully-implicit-runge-kutta.md) apply
unchanged (§5); the paper wraps BoomerAMG in the block preconditioning of Southworth et al.
(§6.3; see [implicit stage solvers](/methods/implicit-stage-solvers.md)). The $s+1$
explicit evaluations of a step use only previous-step data and are mutually independent,
so they can run in parallel (§5.2, §6.1). The method stores $s+1$ solution vectors.
Radau nodes are chosen for an L-stable implicit part; Legendre nodes would give a Gauss
implicit part (§5).

## Iterators and composite methods

With $\alpha=0$ and $\mathsf b=-1$ the same polynomials give an **iterator**
$y^{[n+1]}_j=y^{[n]}_1+\int_{-1}^{\mathsf z_j}\bigl(L^{\mathrm I}_f+L^{\mathrm E}_f\bigr)\,d\xi$,
which uses the Radau IIA coefficients for both parts: for $s=2$ the explicit coefficients
equal the implicit ones, $(\tfrac56,-\tfrac16)$ and $(\tfrac32,\tfrac12)$ (§5.1,
Eqs. (5.8)–(5.9)). Each sweep is a
semi-implicit correction in the manner of an IMEX SDC sweep. The paper states that if the
first block value has order at least $2s-1$, every sweep raises the order of the other
block values by one, up to $2s-1$, and that repeated sweeps converge to the stages and
output of $s$-stage Radau IIA (§5.1).

Iterators serve two purposes (§5.1–5.2):

- **Starting values.** From the constant guess $y_0$ at all nodes, $K$ sweeps give the
  first block; at least $K=s$ for FIMEX-Radau and $K=s+1$ for FIMEX-Radau\* (Eq. (5.10)).
- **Composite methods.** One propagator step followed by $K$ sweeps (registry $K$, the
  source's $\kappa$), $\mathbf y^{[n+1]}=M^K(P(\mathbf y^{[n]}))$ with $P$ the propagator
  and $M$ the iterator ($P$, $M$ page-local operators). The stated orders are
  $\min(2s-1,\,s+K)$ for FIMEX-Radau and $\min(2s-1,\,s+1+K)$ for FIMEX-Radau\*
  (Eqs. (5.12)–(5.13)). Each step costs one Radau-type solve plus $K$ iterator solves,
  which are cheap with iterative solvers because the propagator supplies a very good
  initial guess (§5.2).

The source labels composites FIMEX-Radau$(q,\kappa)$ with $q=s+1$ nodes and $\kappa=K$
sweeps; this page keeps the labels when quoting results. The idea of composite PBMs comes
from the authors' earlier exponential PBMs, and the comparison with SDC is theirs (§5.2).

## Linear stability

The FIMEX-Radau\*(4,$K$) regions always contain a segment of the imaginary axis in
$z_{\mathrm E}$ for the three values of $\arg z_{\mathrm I}$ shown; for $K=0$ they are very
small in the oscillatory case and grow slowly with $\lvert z_{\mathrm I}\rvert$, while one
iterator sweep enlarges them markedly (§5.3, Fig. 4, Fig. SM1). The lower-degree explicit
polynomial of FIMEX-Radau gives larger regions than FIMEX-Radau\* (§5.3).

## Numerical evidence

- **Korteweg–de Vries** (§6.1, Fig. 5; [KdV](/benchmarks/korteweg-de-vries-equation.md)):
  512 Fourier modes, linear dispersive part implicit (diagonal in Fourier space, so the
  $s\times s$ inverses are precomputed), final time $3.6/\pi$. Serially, the seventh-order
  FIMEX-Radau\*(5,2) beats all other methods below relative error $10^{-2}$. With the five
  explicit evaluations on five OpenMP threads (FFTs single-threaded, 14-core Xeon E5-2683
  v3), it is the most efficient at every accuracy, about 2 times faster than any
  Runge–Kutta method at $10^{-2}$ and about 30 times faster than IMEX-RK4 below $10^{-4}$.
  The comparators are IMEX(1,1,1), IMEX(2,3,2), ARK3(2)4L[2]SA and ARK4(3)6L[2]SA.
  FIMEX-Radau\*(3,2) converges at fourth order over most of the step range and beats the
  paper's "IMEX-RK4" while storing three solution vectors instead of five.
- **Van der Pol** (§6.2, Fig. 6, Figs. SM2–SM4; [Van der Pol oscillator](/benchmarks/van-der-pol-oscillator.md)):
  stiffness parameter from 1 to $10^{-8}$, $h\in[10^{-4},0.25]$, a semi-implicit splitting
  (first component explicit) and a linearly implicit one with the exact Jacobian. All
  FIMEX methods are stable over the whole step range with both splittings, whereas all
  IMEX Runge–Kutta methods tested needed much smaller steps with the linearly implicit
  splitting. For small stiffness parameter each sweep raises the observed order by about
  one; with the semi-implicit splitting the $K=2$ methods show markedly reduced rates for
  parameters in $[10^{-4},10^{-2}]$ but remain the most accurate; FIMEX-Radau\*(5,0) with
  the linearly implicit splitting is stable but does not converge at large steps, which one
  sweep fixes. See [order reduction](/definitions/order-reduction.md).
- **DG advection–diffusion** (§6.3.1, Figs. 7–8, Table 1; MFEM, hypre, 120 MPI processes):
  advection explicit, diffusion implicit. Among the Ascher–Ruuth–Spiteri pairs only those
  with both parts [stiffly accurate](/properties/stiff-accuracy.md) were reasonably stable,
  and IMEX(1,2,1) is "very unstable" at the forward-Euler advective limit. FIMEX methods are
  the most efficient below errors of about $10^{-3}$; at diffusion coefficient $0.01$ and
  $h=0.01$ only IMEX(1,1,1) and IMEX(4,4,3) did not diverge among the IMEX-RK pairs:

  | method | $\ell^2$ error | runtime |
  |---|---|---|
  | IMEX(1,1,1) | 0.018 | 35 s |
  | FIMEX-Radau\*(2,0) | 0.009 | 37 s |
  | FIMEX-Radau(2,1) | 0.009 | 71 s |
  | IMEX(4,4,3) | $7.4\times10^{-5}$ | 165 s |
  | FIMEX-Radau(3,1) | $2.1\times10^{-5}$ | 122 s |
  | FIMEX-Radau\*(3,2) | $2.6\times10^{-6}$ | 151 s |
  | FIMEX-Radau\*(4,2) | $2.9\times10^{-8}$ | 184 s |

  FIMEX-Radau\*(4,0) largely diverges at diffusion coefficient $0.1$ except at the smallest
  step; one or two sweeps make it stable. All methods show some order reduction, FIMEX with
  much smaller error constants.
- **DG advection–diffusion–reaction** (§6.3.2, Fig. 9; 64 MPI processes): reaction
  explicit, so the AMG hierarchy need not be rebuilt each step. The IMEX schemes beat
  L-stable [DIRKs](/methods/diagonally-implicit-runge-kutta.md) with simplified Newton in
  accuracy per wall-clock time; FIMEX-Radau\* is best below errors of about $10^{-4}$, and
  at third order its error is 10–100 times smaller than that of comparable IMEX-RK pairs at
  equal step. IMEX-RK and DIRK do not quite reach third order, which the authors relate,
  "possibly", to the time-dependent boundary data.

## Qualifications

- **No theorems.** Part I proves nothing: the composite orders, the order gain per sweep
  and the convergence of repeated sweeps to Radau IIA are stated from the polynomial
  construction and checked numerically (§5–6).
- **High stage order and order reduction.** The conclusion that high-degree ODE
  polynomials give "high stage order that prevents order reduction on stiff problems"
  (§7) sits beside the paper's own reduced rates on Van der Pol with the semi-implicit
  splitting and on the DG tests (§6.2–6.3). It is a design argument, not a demonstrated
  property.
- **Stability statement for splitting (2.4).** §5.3 states that with the semilinear
  splitting $f^{\mathrm I}=Ly$, $f^{\mathrm E}=N(t,y)$ the stability region equals that of
  the implicit Radau IIA method. On the partitioned Dahlquist problem the explicit part is
  then nonzero; the equality holds for the linearly implicit splitting with the exact
  Jacobian, $f^{\mathrm I}=J_ny$, $f^{\mathrm E}=f-J_ny$, under which a linear problem has
  $f^{\mathrm E}\equiv0$ and the method reduces to its implicit part *(compiler check, not in
  the source)*.
- **Printed slips (arXiv v2 read; supplement read in its SIAM version).**
  - The Fig. 4 row labels of the arXiv text read $\arg z_{\mathrm I}=0,\tfrac{3\pi}2,\tfrac\pi2$
    and the text calls $\arg z_{\mathrm I}=0$ diffusive, against the same page's convention
    that $\arg z_{\mathrm I}=\pi$ represents diffusion. The SIAM supplement's Fig. SM1 labels
    the rows $\pi,\tfrac{3\pi}4,\tfrac\pi2$, consistent with that convention, whereas the
    arXiv copy of Fig. SM1 keeps $0,\tfrac{3\pi}2,\tfrac\pi2$.
  - The implicit Fourier-space solve of §6.1.1 is printed with the explicit matrix
    $\mathbf B^{\{2\}}$; by Eq. (5.7) the implicit matrix is $\mathbf B^{\{1\}}$.
  - Eq. (5.17) prints the same argument twice inside the maximum (the conjugate is
    presumably meant); the partitioned BDF polynomial (4.7) is said to interpolate $g-1$
    solution values and then $g$; the speedups of §6.3.1 for two diffusion coefficients are
    both printed as "≈16×"; one sentence of §6.3.1 merges the final time and the process
    count.
- **Labels of the compared pairs** follow Ascher–Ruuth–Spiteri, IMEX$(s,\sigma,p)$, and
  Kennedy–Carpenter, ARK3(2)4L[2]SA and ARK4(3)6L[2]SA; see
  [IMEX Runge–Kutta methods](/methods/imex-runge-kutta.md).
- Part II, announced in §7, builds diagonally implicit IMEX polynomial methods from BDF ODE
  polynomials; it is not ingested.

# Citations

- [Buvoli & Southworth (2023)](/sources/buvoli-2023.md) — arXiv v2 and SIAM supplement: §1; §3 (Eqs. (3.1)–(3.13)), §3.1–3.2; §4 (Defs. 4.1–4.3, Eqs. (4.4)–(4.12)); §5 (Eqs. (5.2)–(5.17)), §5.1–5.3 (Fig. 4); §6.1–6.3 (Figs. 5–9, Table 1); §7; supplement SM1 (coefficients, script), SM2 (Fig. SM1), SM3, SM4 (Eq. (SM4.5)).
