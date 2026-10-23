---
type: Source
title: "Saupe et al. (2025) — Adaptive time step selection for spectral deferred correction"
description: "Transfers embedded-pair step-size control to spectral deferred correction with two problem-independent local error estimates, the increment of the last sweep and a dense-output comparison at an inner node, applies them to serial, block Gauss–Seidel and diagonal SDC, and shows on four stiff problems that adaptive parallel SDC beats fifth-order embedded Runge–Kutta pairs."
resource: "doi:10.1007/s11075-024-01964-z"
source_kind: paper
authors: [Saupe T., Götschel S., Lunet T., Ruprecht D., Speck R.]
year: 2025
venue: "Numer. Algorithms 100:369-393"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_Numerical_Algorithms_Saupe_Adaptive_time_step_selection_for_spectral_deferred_correctio.pdf"
tags: [deferred-correction, step-size-control, error-estimation, parallel, stiff]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

[Spectral deferred correction](/methods/deferred-correction.md) (SDC) solves the
collocation problem of one step, a [fully implicit collocation
method](/methods/fully-implicit-runge-kutta.md) on $\mathsf M$ nodes, by a preconditioned
Picard iteration whose sweeps are cheap low-order solves. Adaptive step selection for SDC
had used only step doubling and halving, or problem-specific quantities. The paper carries
the machinery of [embedded Runge–Kutta pairs](/methods/embedded-runge-kutta-pair.md) and
[step-size control](/methods/step-size-control.md) (an error estimate from two solutions
of different order, the elementary controller, local extrapolation, reject and recompute)
over to SDC with two generic local error estimates.

$h$-adaptivity runs a fixed number $K$ of sweeps and takes the increment between the last
two as the estimate. $h$-$k$-adaptivity iterates until the collocation residual is small,
then compares the collocation value at node $\mathsf M-1$ with the interpolant through the
other nodes, a use of the collocation polynomial as [dense output](/methods/dense-output.md).
It chooses both the step and the iteration count. Both are applied to
[parallel-in-time](/methods/parallel-in-time-integration.md) variants: pipelined block
Gauss–Seidel SDC (parallel across the steps) and [diagonal
SDC](/methods/parallel-sdc.md) with the MIN-SR-S preconditioner (parallel across the
method). Reusing the rejected step's collocation polynomial as initial guess cuts the cost
of restarts.

The evidence is numerical, with no theorems: the stiff
[van der Pol oscillator](/benchmarks/van-der-pol-oscillator.md) with $\mu=1000$, a 1D
superconducting-magnet quench, the 2D focusing
[nonlinear Schrödinger equation](/benchmarks/nonlinear-schrodinger-equation.md) and the 2D
forced [Allen–Cahn equation](/benchmarks/allen-cahn-equation.md), the last two with
IMEX-SDC. Adaptive SDC beats fixed-step and iteration-adaptive SDC everywhere (about 70
times fewer Newton iterations on van der Pol). At least one adaptive parallel variant is
faster than the fifth-order embedded pairs ESDIRK5(3) and ARK5(4) on every problem.
Combining block Gauss–Seidel and diagonal SDC does not help. All code is in
[pySDC](/software/pysdc.md).

# Version read

arXiv:2403.13454v2 [math.NA], 4 Sep 2024, typeset in the Springer Nature 2021 LaTeX
template: the author manuscript, not the version of record. Its 29 pages were all read
(pp. 7–9, 12, 15–16 also checked visually); the journal pagination 369–393 is not printed.
Page-1 title and authors match Crossref up to capitalization ("Spectral Deferred
Correction"). The corresponding-author address on page 1 carries the first author's former
surname; the work's identity is not affected. The published issue is 2025, online 2024.
Section, equation, algorithm and page numbers cited here are those of arXiv v2.

# Key claims

Notation: $\mathsf M$ collocation nodes $c_m$ (with $c_0=0$), $Q$ the collocation matrix,
$Q_\Delta$ the preconditioner, $\mathbf Y^{(k)}$ the node values after sweep $k$.
$\epsilon$ is the local error estimate and $\epsilon_{\rm TOL}$ the tolerance, so the
registry's scaled estimate is $\mathrm{err}_n=\epsilon/\epsilon_{\rm TOL}$.

1. The collocation problem $\mathbf Y=\mathbf 1\otimes y_n+hQf(\mathbf Y)$ is a fully
   implicit Runge–Kutta method, and Gauss–Legendre, Gauss–Lobatto and Gauss–Radau nodes give
   superconvergence "up to order $2\mathsf M$" at the right end of the step. (§2.1, Eq. (7))
   **Stated**
2. Plain Picard iteration converges only for small $h$ or non-stiff problems; SDC
   preconditions it with a low-order method, giving the sweep
   $(I-hQ_\Delta f)(\mathbf Y^{(k+1)})=\mathbf 1\otimes y_n+h(Q-Q_\Delta)f(\mathbf Y^{(k)})$.
   (§2.1, Eqs. (8)–(12)) **Derived**
3. With an implicit- or explicit-Euler preconditioner each sweep raises the order by one,
   up to the collocation order, if the iteration converges. Runge–Kutta preconditioners can
   sometimes gain more, but a non-smooth error can limit the gain to one per sweep,
   particularly on non-equidistant nodes. (§2.1) **Stated**
4. The LU preconditioner ($Q_\Delta=U^\top$ with $LU=Q^\top$) and diagonal preconditioners
   cannot guarantee exactly one order per sweep, so implicit Euler is used for most runs;
   most of these preconditioners are not A-stable marching schemes and restrict the
   convergence domain. (§2.1) **Stated**
5. Evaluated inside the step, the collocation polynomial is accurate to order $\mathsf M$;
   the endpoint is accurate up to order $2\mathsf M$. (§2.1, "Dense output") **Stated**
6. From two solutions of orders $p<q$, $\epsilon=\lVert y^{(p)}-y^{(q)}\rVert_\infty$
   estimates the error of the lower-order one up to $O(h^{q+1})$. The controller is
   $h_{\rm new}=0.9\,h\,\mathrm{err}_n^{-1/(p+1)}$, the step advances with the higher-order
   solution and is rejected and recomputed with $h_{\rm new}$ if $\mathrm{err}_n>1$. (§2.2,
   Eqs. (14)–(15)) **Derived** (standard)
7. $h$-adaptivity (Algorithm 1): with a fixed number $K$ of sweeps, the increment
   $\lVert\mathbf Y^{(K)}-\mathbf Y^{(K-1)}\rVert$ is the estimate and the controller
   exponent is $1/K$. Dutt, Greengard & Rokhlin used the same increment with doubling and
   halving only. (§2.2) **Stated** (algorithm proposed)
8. $h$-$k$-adaptivity (Algorithm 2): after convergence, the degree-$(\mathsf M-1)$
   interpolant through the nodes $\{c_0,\dots,c_{\mathsf M-2},c_{\mathsf M}\}$ is evaluated
   at $c_{\mathsf M-1}$ and compared with the collocation value there; the controller
   exponent is $1/\mathsf M$, step growth is capped by a factor 4, the iteration cap is 16,
   and divergence (residual above $10^9$, growing, or at the cap) divides the step by 4 and
   restarts. Untabulated tests suggest the choice of node is "more or less arbitrar[y]".
   (§2.2, Eqs. (16)–(18)) **Stated**; the node choice **Shown** (not documented)
9. The residual tolerance must be balanced against $\epsilon_{\rm TOL}$; the runs use
   $10^{-5}$ (van der Pol), $10^{-1}$ (quench), $10^{-4}$ (Schrödinger) and $10^{-3}$
   (Allen–Cahn) times $\epsilon_{\rm TOL}$. (§2.2, §3) **Stated**
10. Evaluating the rejected step's converged collocation polynomial at the new nodes gives
    the initial guess of the restart. For $h$-adaptivity this is expected not to help,
    because the controller would overestimate the next step from one exceptionally good
    guess. In tests it reduces iterations but barely changes total cost, restarts being
    few; with diagonal SDC it needs all-to-all communication. (§2.2, §4.1) **Shown**
    (qualitatively)
11. Iteration-only adaptivity at fixed $h$ is inferior: $k$ is an integer (coarse control),
    and the residual measures the iteration error with respect to the collocation solution,
    not the truncation error. (§2.2) **Stated**
12. Block Gauss–Seidel SDC keeps its order as the number of steps in a block grows, so the
    controller is used unmodified with one step size per block; the increment then
    estimates the error within the block, treated as local to it. (§2.3) **Stated**
13. Restarting from the first step of the block whose estimate fails (heuristic) "performed
    consistently better" than restarting from the block start, and only it is shown. (§2.3)
    **Shown** (not documented)
14. On van der Pol with $\mu=1000$ over $t\in[0,20]$ (one fast transition), fixed-step
    schemes need about 70 times the Newton iterations of the step-size-adaptive strategies;
    smaller $\mu$ gives similar but weaker trends (not shown). (§4.1, Fig. 6) **Shown**
15. Adaptive step selection pays off on all four problems and is essential for van der Pol;
    $h$-$k$-adaptive SDC is particularly efficient on the PDE examples. (§4.1, Fig. 7)
    **Shown**
16. On Allen–Cahn the IMEX scheme becomes unstable at large steps, causing "around 100
    restarts" at loose tolerances in $h$-$k$-adaptivity; capping the step helped (not
    shown), and solutions stay physical at every tolerance. (§4.1) **Shown**
17. Tolerance proportionality: the global error scales as
    $\epsilon_{\rm TOL}^{q/(p+1)}$, i.e. linearly in $\epsilon_{\rm TOL}$ for
    $h$-adaptivity and as $\epsilon_{\rm TOL}^{5/4}$ for $h$-$k$-adaptivity "in our case",
    observed "to a reasonable degree". The exception is $h$-adaptivity on the quench
    problem, whose error depends on how the onset of runaway heating is resolved. (§4.1,
    Fig. 8) **Derived** and **Shown**
18. All SDC configurations compared have global order 5. (Captions of Figs. 8 and 10)
    **Stated**
19. $h$-$k$-adaptive diagonal SDC (MIN-SR-S, 3 processes) is the most efficient variant on
    the three PDE examples and roughly halves the wall time; $h$-adaptive block Gauss–Seidel
    SDC on 4 processes speeds up van der Pol and Allen–Cahn; diagonal SDC is especially
    efficient on the quench problem, whose Newton and finite-difference solves are
    expensive. (§4.1, Fig. 9) **Shown**
20. Combining block Gauss–Seidel and diagonal SDC (4 × 3 processes) does not improve
    performance: block Gauss–Seidel works best with implicit Euler, a diagonal
    preconditioner inside it "significantly increases the number of iterations", and on
    Allen–Cahn the combination gives very large errors or crashes. (§4.1, Fig. 9) **Shown**
21. Against the order-5 embedded pairs ESDIRK5(3) (van der Pol, quench) and ARK5(4)
    (Schrödinger, Allen–Cahn) of Kennedy & Carpenter, at least one adaptive parallel SDC
    variant is faster on every problem; the Runge–Kutta pair wins only on Schrödinger at
    low accuracy. (§4.2, Fig. 10) **Shown**
22. Explicit Runge–Kutta methods were not competitive: every problem was stiff enough to
    cause instability, unphysical solutions or no solution in reasonable time. (§4.2)
    **Shown** (not documented)
23. With third-order methods (not shown) at least one SDC method again beat the Runge–Kutta
    method. (§4.2) **Shown** (not documented)
24. ARK5(4) is "the highest order additive RKM we are aware of"; stage-parallel Runge–Kutta
    methods "often have worse stability than their serial counterparts", and the authors
    found no embedded stage-parallel method of order above 4. (§4.2) **Stated**
25. Christlieb et al. (2015) found the increment a poor error estimate for revisionist
    integral deferred correction because local errors of different steps accumulate; it
    works for block Gauss–Seidel SDC because fixed-size blocks share one step size, making
    the accumulated error local to the block. (§5) **Stated**
26. Earlier SDC step selection based on conserved quantities mitigates
    [order reduction](/definitions/order-reduction.md), and comparison with a low-order
    secondary solution has been used; both are problem-specific. Adaptive steps for
    parallel-in-time methods had been studied only for Parareal. (§1) **Stated**
27. IMEX-SDC typically has the order of the unsplit version, though order reduction can
    occur, and has beaten DIRK-based IMEX Runge–Kutta in wall time for incompressible flow.
    (§2.1) **Stated**

*(Compiler checks, not in the sources.)* Claim 1 is imprecise: only Gauss–Legendre nodes reach
order $2\mathsf M$; Radau gives $2\mathsf M-1$ and Lobatto $2\mathsf M-2$, and Gauss–Legendre
nodes exclude the endpoint. The exponent $5/4$ of claim 17 needs $\mathsf M=4$ with order 5,
while the diagonal-SDC runs use 3 processes, one per node, and $2\mathsf M-1=5$ fits
$\mathsf M=3$ Radau-right nodes, which would give $5/3$. The paper never states $\mathsf M$ or
the node type of its runs, so the inconsistency cannot be settled from the text. The
tolerance-proportionality argument is heuristic and ignores error accumulation.

# Printed slips

- Algorithm 2, p. 9: "$\Delta t\leftarrow\max\big(\gamma,\beta(\epsilon_{\rm TOL}/\epsilon)^{1/M}\big)\Delta t$"
  contradicts the text (pp. 8–9), where $\gamma=4$ is a "relative limit ... on how much
  the step size is allowed to increase"; a cap needs $\min$. As printed the step would
  always grow by at least a factor 4.
- §4.1, p. 16: "we expect a linear dependence of global error on step size for
  $\Delta t$-adaptivity for any $q$"; the derivation and Fig. 8 concern the tolerance, not
  the step size.
- §4.1, p. 16: exponent printed "$\epsilon_{\rm TOL}^{q/p+1}$", meaning $q/(p+1)$.
- Eq. (13), p. 5: the implicit-Euler preconditioner has first column $\tau_2-\tau_1$ in
  every row and first row $(\tau_2-\tau_1,0,\dots,0)$, where the usual matrix has
  $\tau_1-\tau_0$; as printed it is shifted by one index or assumes $\tau_1=0$.
- Fig. 2 caption (p. 12): "we solve only the shaded transition at $t\approx800$", while
  §3.1 and Fig. 6 solve from $u_0=1.1$ on $[0,20]$; Fig. 6 says the "next transition
  appearing at around $t=600$ (see Figure 2)", whereas Fig. 2 shows transitions at about
  800 and 1600.
- Eq. (31), p. 15: $u_0(x)=\tanh\big(\frac{R_0\|x\|}{\sqrt2\epsilon}\big)$; a circle of
  radius $R_0$ needs $R_0-\|x\|$ (no minus sign is visible on the page).
- §3.1: "$\|\mu\|\ll1$", "$\|\mu\|\gg1$", a norm on a scalar.
- $\epsilon$ is both the local error estimate and the Allen–Cahn interface width (Eq. (33)).
- Ref. [29] carries a garbled URL "https://arxiv.org/abs/https://onlinelibrary.wiley.com/doi/pdf/...".
- Ref. [19] (Christlieb, Ong & Qiu, Math. Comp. 79(270)) is printed with year 2009; volume
  79 is the 2010 volume (online 2009). Recorded as printed.

# Notation map

| Saupe et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_t=f(u)$ | $y'=f(y)$ | autonomous, scalar for notation only |
| $\Delta t$ | $h$ | |
| $M$ | $\mathsf M$ | number of collocation nodes; **not the registry mass matrix** |
| $\tau_m$, $\tau_0=0$ | $c_m$, $c_0=0$ | normalized nodes; node type of the runs not stated |
| $l^\tau_j$ | $\ell_j$ | Lagrange basis on the nodes |
| $q_{mj}$, $Q$ | $Q$ | collocation matrix, the Butcher matrix $A$ of the collocation method |
| $Q_\Delta$, $\tilde q^I$, $\tilde q^E$ | $Q_\Delta$, $Q^{\mathrm I}_\Delta$, $Q^{\mathrm E}_\Delta$ | preconditioner; IMEX entries |
| $\vec u$, $\vec u_0$, $F(\vec u)$ | $\mathbf Y$, $\mathbf 1\otimes y_n$, $f(\mathbf Y)$ | node values, not stage derivatives |
| $k$ (superscript) | $(k)$ | sweep index |
| $k_{\max}$ | $K$ ($h$-adaptivity); $k_{\max}=16$ ($h$-$k$) | **the source uses $k_{\max}$ for both the fixed sweep count and the iteration cap** |
| $\vec r^k$, $r$, $r_{\rm TOL}$ | kept | collocation residual and its tolerance; both $r_{\rm TOL}$ and $r_{\rm tol}$ printed |
| $\epsilon$, $\epsilon_{\rm TOL}$ | $\epsilon$, $\epsilon_{\rm TOL}$; $\mathrm{err}_n=\epsilon/\epsilon_{\rm TOL}$ | **$\epsilon$ also the Allen–Cahn interface width, the registry $\varepsilon$** |
| $\delta^{(p)}$, $u^{(p)}$, $u^{(q)}$ | kept | local error; solutions of orders $p<q$ |
| $\beta=0.9$ | safety factor 0.9 | **not the registry PID exponents $\beta_j$** |
| $\gamma=4$ | growth and shrink factor 4 | **not the Rosenbrock $\gamma$** |
| $f^I$, $f^E$ | $f^{\mathrm I}$, $f^{\mathrm E}$ | IMEX parts |
| $N=a\times b$ | kept | processes: $a$ block Gauss–Seidel, $b$ diagonal SDC; $N$ also the steps per block |
| $\mu$ | $\mu$ | van der Pol parameter |

# Reference list

56 printed references, numbered [1]–[56]. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` saupe-2025. Three arXiv preprints stay their
own entries: [24] Čaklović et al. 2024 (arXiv:2403.18641), keyed `caklovic-2024` and
distinct from the ingested published paper
[Čaklović et al. (2025)](/sources/caklovic-2025.md); [25] Freese et al. 2024
(arXiv:2403.20135); [55] Chegini et al. 2023 (arXiv:2311.07206). [29] has a garbled URL; its
DOI 10.1002/fld.5177 is taken as printed. [19] (Christlieb, Ong & Qiu, Math. Comp. 79,
printed 2009) is keyed by its volume year as `christlieb-2010`; [20] is `christlieb-2009`
(Commun. Appl. Math. Comput. Sci. 4), [37] `christlieb-2010-b` and [56]
`christlieb-2015-b`. [39] is the pySDC software paper (Speck 2019). No unparseable
items.

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [Allen–Cahn equation](/benchmarks/allen-cahn-equation.md)
* [Deferred correction (DeC)](/methods/deferred-correction.md)
* [Dense output](/methods/dense-output.md)
* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)](/methods/fully-implicit-runge-kutta.md)
* [Lax–Wendroff flux reconstruction (single-stage Taylor time stepping)](/methods/lax-wendroff-flux-reconstruction.md)
* [Nonlinear Schrödinger equation](/benchmarks/nonlinear-schrodinger-equation.md)
* [Order reduction](/definitions/order-reduction.md)
* [Parallel-across-the-method spectral deferred correction (diagonal SDC)](/methods/parallel-sdc.md)
* [Parallel-in-time integration](/methods/parallel-in-time-integration.md)
* [pySDC](/software/pysdc.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
* [Van der Pol oscillator](/benchmarks/van-der-pol-oscillator.md)
