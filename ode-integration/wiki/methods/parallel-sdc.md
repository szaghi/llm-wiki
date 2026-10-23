---
type: Method
title: "Parallel-across-the-method spectral deferred correction (diagonal SDC)"
description: "Diagonal SDC sweeps the collocation problem of one step with a diagonal preconditioner, so the node solves of each sweep run in parallel. The page gives the iteration matrices, the nilpotency-based coefficients MIN-SR-NS, MIN-SR-S and MIN-SR-FLEX, their order and stability, and measured and modelled efficiency, including adaptive steps."
status: established
aliases: [diagonal SDC, parallel SDC, parallel-across-the-method SDC, MIN-SR-NS, MIN-SR-S, MIN-SR-FLEX, VDHS, IEpar, parallel diagonally iterated Runge–Kutta, PDIRK]
tags: [parallel, implicit, stiff, stability, linear-algebra]
timestamp: 2026-10-20T03:57:00Z
---

# Parallel-across-the-method spectral deferred correction (diagonal SDC)

Spectral deferred correction (SDC) solves the collocation problem of one step
$[t_n,t_n+h]$ on $\mathsf M$ nodes $0\le c_1<\dots<c_{\mathsf M}\le1$,

$$Y=y_n\mathbf 1+h\,Q\,f(Y),\qquad Q_{ij}=\int_0^{c_i}\ell_j(s)\,ds,$$

with $Y=(Y_1,\dots,Y_{\mathsf M})$ the node values, $\ell_j$ the Lagrange polynomials on the
nodes and $f(Y)$ applied node by node. This is the
[collocation Runge–Kutta method](/methods/fully-implicit-runge-kutta.md) with $A=Q$, $c$
the nodes and $b_i=\int_0^1\ell_i$ ([Čaklović et al. (2025)](/sources/caklovic-2025.md),
§2.1, Eqs. (2.4)–(2.5); [Saupe et al. (2025)](/sources/saupe-2025.md), §2.1, Eqs. (6)–(7)).
SDC replaces the coupled $\mathsf Md\times\mathsf Md$ solve by $K$ **sweeps** of the
preconditioned fixed-point iteration

$$Y^{(k+1)}-h\,Q_\Delta f\big(Y^{(k+1)}\big)=y_n\mathbf 1+h\,(Q-Q_\Delta)\,f\big(Y^{(k)}\big),$$

with $Q_\Delta$ a cheap approximation of $Q$ (Čaklović et al., Eq. (2.8); Saupe et al.,
Eq. (12)). $Q_\Delta=0$ is Picard iteration. A lower-triangular $Q_\Delta$ (implicit Euler
between nodes, or Weiser's LU factor) gives the classical serial sweep, which costs one
DIRK step with $\mathsf M$ stages. A **diagonal** $Q_\Delta$ makes the $\mathsf M$ node solves
of a sweep independent, so they run on $\mathsf M$ threads or processes: parallelism
*across the method* in the taxonomy of
[parallel-in-time integration](/methods/parallel-in-time-integration.md). The general
SDC framework is on [deferred correction](/methods/deferred-correction.md).

## Equivalences

- SDC with lower-triangular $Q_\Delta$ is a specific iterated implicit Runge–Kutta method
  of van der Houwen & Sommeijer (1991), and every one of their diagonally preconditioned
  iterated IRK methods is an SDC sweep with diagonal $Q_\Delta$. Speck (2018) proposed
  diagonal SDC unaware of that earlier work (Čaklović et al. 2025, §1, §2.1).
- With $Q_\Delta=Q=A$ for the Butcher matrix of a DIRK or explicit Runge–Kutta method, the
  sweep reproduces that method, so a generic SDC code runs any DIRK or ERK; [pySDC](/software/pysdc.md)
  does so (Remark 2.2).
- Only nodes with $c_{\mathsf M}=1$ (Radau IIA, called "Radau-Right", and Lobatto) are used,
  with $y_{n+1}=Y_{\mathsf M}$: the collocation update $y_n+hb^\top f(Y)$ raises the order but
  made some apparently A-stable preconditioners lose A-stability (Remark 2.1; experiments not
  shown).

## Iteration matrices

On the Dahlquist equation, with $z=h\lambda$ and the error $e^{(k)}=Y^{(k)}-Y$ with respect to
the collocation solution (not the exact solution), $e^{(k+1)}=E(z)\,e^{(k)}$ with

$$E(z)=z\,(I-zQ_\Delta)^{-1}(Q-Q_\Delta),\qquad E_{\mathrm{NS}}=\lim_{z\to0}\frac{E(z)}{z}=Q-Q_\Delta,\qquad E_{\mathrm S}=\lim_{\lvert z\rvert\to\infty}E(z)=I-Q_\Delta^{-1}Q$$

(page-local symbols; Čaklović et al. 2025, §2.2, Eqs. (2.11)–(2.13)). Earlier diagonal
coefficients minimized the spectral radius of one limit numerically: VDHS (van der Houwen &
Sommeijer), MIN (Speck 2018) and MIN3 (a black-box optimizer no longer available). The
diagonals $\mathrm{diag}(Q)$ and $\mathrm{diag}(c)$, the latter "IEpar", implicit Euler from
$t_n$ to each node, converge slowly. Čaklović et al. instead make the limit matrices
**nilpotent**, after Weiser, using the isomorphism between $\mathbb R^{\mathsf M}$ and
polynomials of degree $\mathsf M-1$ under which $Q$ is integration of the interpolant
(§2.2.1, Props. 2.3–2.7).

**MIN-SR-NS (Theorem 2.8).** For any nodes $0<c_1<\dots<c_{\mathsf M}\le1$,

$$Q_\Delta=\mathrm{diag}\Big(\frac{c_1}{\mathsf M},\dots,\frac{c_{\mathsf M}}{\mathsf M}\Big)$$

makes $Q-Q_\Delta$ nilpotent of index $\mathsf M$, so $\rho(E_{\mathrm{NS}})=0$. On monomials,
$Q-Q_\Delta$ maps degree $n$ to degree $n+1$ with factor $\frac1{n+1}-\frac1{\mathsf M}$ and kills
degree $\mathsf M-1$; each sweep removes the lowest-order term of the collocation error in
the non-stiff limit (Eq. (2.34), Remark 2.9). It differs from van der Houwen & Sommeijer's
non-stiff choice, which gives IEpar.

**MIN-SR-S (Definition 2.10).** A stationary diagonal with increasing entries that drives
$\det[(1-t)I+tQ_\Delta^{-1}Q]-1$ to zero at the nodes $t=c_m$. If $E_{\mathrm S}$ is nilpotent
this degree-$\mathsf M$ polynomial vanishes identically, and since it vanishes at $t=0$, the
$\mathsf M$ nodes suffice. It is solved numerically (MINPACK hybrd), from MIN-SR-NS as initial
guess up to $\mathsf M=4$ and from a power-law extrapolation of the coefficients for larger
$\mathsf M$. No theory says whether a solution exists for every $\mathsf M$; for $\mathsf M=2$
two minimizers exist, one ordered (§2.2.3).

**MIN-SR-FLEX (Theorem 2.12).** The sweep-dependent choice

$$Q_\Delta^{(k)}=\mathrm{diag}\Big(\frac{c_1}{k},\dots,\frac{c_{\mathsf M}}{k}\Big),\qquad k=1,\dots,\mathsf M,$$

makes the product $(I-Q_\Delta^{(\mathsf M)\,-1}Q)\cdots(I-Q_\Delta^{(1)\,-1}Q)$ vanish for nodes with
$c_1>0$, so the error tends to zero in the stiff limit after $\mathsf M$ sweeps: factor $k$
annihilates degree $k-1$ and maps every other monomial to a multiple of itself
(Eq. (2.43)). The idea of iteration-dependent preconditioners is credited to Weiser. The
first factor is IEpar. In the experiments, sweeps beyond $\mathsf M$ use MIN-SR-S (§2.2.4).
For Lobatto nodes ($c_1=0$) the first node is eliminated and the method applied to the
reduced matrix, with a zero prepended (Remark 2.11).

**Coefficients for $\mathsf M=4$ Radau IIA nodes** (Appendix A, §2.2.3):

| $Q_\Delta$ | diagonal entries | $\rho(E_{\mathrm S})$ |
|---|---|---|
| VDHS | $0.32049937$, $0.08915379$, $0.18173956$, $0.2333628$ | $0.025$ |
| MIN | $0.17534868$, $0.0619158$, $0.1381934$, $0.19617814$ | $0.42$ |
| MIN3 | $0.31987868$, $0.08887606$, $0.18123663$, $0.23273925$ | $0.0081$ |
| MIN-SR-S | $0.05363588$, $0.18297728$, $0.31493338$, $0.38516736$ | $0.00024$ |

Only MIN-SR-S is increasingly ordered; enforcing ordered coefficients "provides a notable
improvement in numerical stability" (Remark 3.1, experiments not documented).

## Order

Van der Houwen et al. proved that any diagonal $Q_\Delta$ gives order $\min(K,p^*)$ after $K$
sweeps, $p^*$ the collocation order (Čaklović et al. 2025, §3.1, as recalled); the
Dahlquist runs with $\lambda=i$ confirm it. MIN-SR-S and MIN-SR-FLEX gain exactly one order
per sweep. MIN-SR-NS sometimes gains two: with $\mathsf M=4$ Radau IIA on the third sweep, with
$\mathsf M=5$ Lobatto from $K=3$ to $K=4$, and on the Lorenz system from $K=3$; the authors leave
this unexplained (§3.1, §4.2, Figs. 2–4, 11). No analysis exists for the order of a
non-stationary iteration such as MIN-SR-FLEX. Saupe et al. (2025, §2.1) note that diagonal
and LU preconditioners cannot guarantee a gain of *exactly* one order per sweep, which their
increment-based error estimate needs; they therefore use implicit Euler sweeps for most runs
and diagonal SDC only with their residual-based adaptivity.

## Stability

With $K$ fixed, an SDC configuration is a one-step method with a
[stability function](/definitions/stability-function.md) $R(z)$ (Čaklović et al. 2025, §3.2,
Figs. 5–10, $\mathsf M=4$ Radau IIA):

- Picard SDC with $K$ sweeps reproduces the stability polynomial of the $K$-stage explicit
  Runge–Kutta method of order $K$ (explicit Euler at $K=1$, classical RK4 at $K=4$); never
  A-stable.
- MIN-SR-NS is not A-stable for any $K$, with regions much larger than Picard's.
- MIN-SR-S "appears" [A-stable](/properties/a-stability.md) for $K\ge3$ and MIN-SR-FLEX
  "seems" A-stable for every $K$, from plots only; MIN-SR-FLEX with $\mathsf M=5$ Lobatto nodes
  and $K=4$ is not A-stable (stated, not shown).
- The MIN-SR-FLEX regions resemble those of serial LU-SDC and implicit-Euler SDC; the
  authors conclude that "parallelism in SDC can be obtained without loss of stability".
- VDHS has very small regions for $K\le3$ that never include the imaginary axis; MIN also has
  bounded regions.

## Efficiency

**Cost model** (Čaklović et al. 2025, §4.1): cost $=$ Newton iterations plus right-hand-side
evaluations (twice the Newton count for Allen–Cahn), divided by $\mathsf MP_{\mathrm{eff}}$ with an
assumed parallel efficiency $P_{\mathrm{eff}}=0.8$ (page-local) for parallel SDC; each node or
stage system is solved by exact Newton with an analytically inverted Jacobian, so that
one Newton iteration costs about one right-hand side. Results, with $\mathsf M=4$:

- **Lorenz system** ($K=4$): parallel and Picard sweeps beat explicit-Euler and LU sweeps;
  MIN-SR-NS is the most efficient SDC variant and beats VDHS and the L-stable
  ESDIRK4(3)6L[2]SA; RK4 is more efficient above error $10^{-4}$, MIN-SR-NS below $10^{-6}$
  (§4.2, Figs. 12–13).
- **[Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md)**
  ($\varepsilon=10^{-3}$, $K=4$): all parallel variants show an error plateau over a range of
  steps ([order reduction](/definitions/order-reduction.md)); MIN-SR-S beats LU-SDC down to
  error $\approx10^{-6}$, LU-SDC is better below; with $K=6$ the crossover moves to
  $\approx10^{-8}$ (§4.3, Figs. 14–15).
- **[Allen–Cahn equation](/benchmarks/allen-cahn-equation.md)** (1D, travelling front, 2047
  points): per step LU-SDC converges fastest, then ESDIRK43, then MIN-SR-FLEX; per modelled
  cost and per measured MPI wall-clock time MIN-SR-FLEX is the most efficient, and LU-SDC
  would catch up only below 40 % parallel efficiency; measured efficiency 74–93 % (§4.4,
  Figs. 16–17).

**Adaptive diagonal SDC.** Saupe et al. (2025) combine MIN-SR-S sweeps with their
$\Delta t$-$k$-adaptivity (iterate to a residual tolerance, estimate the error from the
collocation polynomial, choose the step; see [step-size control](/methods/step-size-control.md)).
With three processes it was the most efficient variant on the three PDE problems
(superconducting-magnet quench, nonlinear Schrödinger, 2D Allen–Cahn), "roughly halving"
the measured wall time on JUSUF, with especially good parallel efficiency on the quench problem, whose Newton
solves are expensive (§4.1, Fig. 9). At least one parallel adaptive SDC variant beat the
embedded order-5 pair used for each problem, ESDIRK5(3) on van der Pol and the quench problem
and ARK5(4) on Schrödinger and Allen–Cahn, in measured wall time; the Runge–Kutta pair was
faster only on Schrödinger at low accuracy (§4.2, Fig. 10). Restarting a
rejected step from the old collocation polynomial needs all-to-all communication in diagonal
SDC (§4.1).

## Qualifications

- **A-stability wording.** Čaklović et al. (2025, §3.2) call a configuration A-stable "if
  $S_C\subset\mathbb C^-$", with $S_C$ the contour $\lvert R(z)\rvert=1$, glossed as "the stability
  domain includes the negative complex half-plane". The gloss is the correct condition,
  $\{z:\lvert R(z)\rvert\le1\}\supseteq\mathbb C^-$, but the contour must then lie in the closed
  right half-plane, not in $\mathbb C^-$; the formula is a slip. All A-stability statements on
  this page rest on plots.
- **Conclusion versus results.** Their conclusion (§5) says the new variants outperform
  serial SDC, RK4 and ESDIRK43 "for all three test problems", but their own §4.2 has RK4 more
  efficient above error $10^{-4}$ on Lorenz and §4.3 has LU-SDC more efficient below about
  $10^{-6}$ ($K=4$) on Prothero–Robinson. The efficiency claims rest on a cost model with an
  assumed $P_{\mathrm{eff}}$; only Allen–Cahn was timed, in Python with mpi4py, and the Newton
  cost assumption favours implicit methods relative to large-scale settings.
- **Proof details.** In the proof of Theorem 2.8 the polynomial is written
  $\sum_{j=1}^{\mathsf M}p_jt^j$, of degree $\mathsf M$ and without constant term; the constant term
  is not treated. Theorem 2.8 requires $c_1>0$, yet MIN-SR-NS is also run on Lobatto nodes,
  covered only implicitly by Remark 2.11. Table 1's caption says $\rho(E_{\mathrm{NS}})$ where the
  column and the text give $\rho(E_{\mathrm S})$.
- **Superconvergence statement of Saupe et al.** Saupe et al. (2025, §2.1) write that
  Gauss–Legendre, Gauss–Lobatto and Gauss–Radau nodes reach "up to order $2\mathsf M$" at the
  step end. Only Gauss–Legendre nodes give $2\mathsf M$; Radau IIA gives $2\mathsf M-1$ and
  Lobatto $2\mathsf M-2$, as Čaklović et al. (2025, §2.1) state and as the theorems Saupe et al.
  cite give. Gauss–Legendre nodes also exclude the step end, which then needs the collocation
  update.
- **Implicit-Euler preconditioner as printed.** Saupe et al. (2025, §2.1, Eq. (13)) print
  $Q_\Delta^{\mathrm{IE}}$ with first column $\tau_2-\tau_1$ in every row and last diagonal entry
  $\tau_{\mathsf M}-\tau_{\mathsf M-1}$ (their nodes $\tau$ are the $c$ here), so the
  $\mathsf M\times\mathsf M$ matrix carries only the $\mathsf M-1$ node-to-node differences. The
  implicit-Euler sweep integrates from $t_n$ to $c_1$ first: row $m$ is
  $(c_1-c_0,\dots,c_m-c_{m-1})$ with $c_0=0$, as Čaklović et al. (2025, §2.1) define it. The
  printed matrix is shifted by one index, or valid only for a left node $c_1=0$; a printed
  slip, checked on the typeset page *(compiler check, not in the sources)*.
- **Versions read.** Čaklović et al.: arXiv v2 (2 Dec 2024); Saupe et al.: arXiv v2 (4 Sep
  2024).

# Citations

- [Čaklović et al. (2025)](/sources/caklovic-2025.md) — arXiv v2: §1, §1.1; §2.1 (Eqs. (2.4)–(2.8), Remarks 2.1–2.2); §2.2 (Eqs. (2.11)–(2.13), Props. 2.3–2.7, Thm. 2.8, Remark 2.9, Def. 2.10, Remark 2.11, Thm. 2.12, Eq. (2.43)); §3.1–3.2 (Figs. 2–10, Remark 3.1); §4.1–4.4 (Figs. 11–17); §5; App. A.
- [Saupe et al. (2025)](/sources/saupe-2025.md) — arXiv v2: §2.1 (Eqs. (6)–(13)); §2.2; §4.1 (Fig. 9); §4.2 (Fig. 10).
