---
type: Source
title: "Čaklović et al. (2025) — Improving Efficiency of Parallel Across the Method Spectral Deferred Corrections"
description: "Derives diagonal preconditioners for parallel-across-the-method spectral deferred correction by making the stiff and non-stiff limit iteration matrices nilpotent (MIN-SR-NS, MIN-SR-S, MIN-SR-FLEX), proves two nilpotency theorems, and shows numerically that the variants gain an order per sweep, look A-stable and beat serial SDC and Runge–Kutta methods under a cost model."
resource: "doi:10.1137/24m1649800"
source_kind: paper
authors: [Čaklović G., Lunet T., Götschel S., Ruprecht D.]
year: 2025
venue: "SIAM J. Sci. Comput. 47:A430-A453"
local_file: "/home/stefano/papers/mosaic/ode-integration/2025_Crossref_SIAM_Journal_on_Scientific_Computing_Čaklović_Improving_Efficiency_of_Parallel_Across_the_Method_Spectral.pdf"
tags: [deferred-correction, parallel, stiff, stability, implicit-stage-solvers]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

[Spectral deferred correction](/methods/deferred-correction.md) (SDC) solves the
collocation problem $\mathbf Y-h\,Q f(\mathbf Y)=\mathbf 1\otimes y_n$ of a
[collocation Runge–Kutta method](/methods/fully-implicit-runge-kutta.md) on $\mathsf M$
nodes by sweeps preconditioned with an approximation $Q_\Delta$ of $Q$. When $Q_\Delta$ is
diagonal, the $\mathsf M$ node solves of a sweep are independent and run on $\mathsf M$
threads: this is [parallel-across-the-method SDC](/methods/parallel-sdc.md), one branch of
[parallel-in-time integration](/methods/parallel-in-time-integration.md). The paper notes
that the idea goes back to van der Houwen & Sommeijer's (1991) parallel iterated
Runge–Kutta methods, and that a lower-triangular sweep costs as much as a
[DIRK](/methods/diagonally-implicit-runge-kutta.md) step with $\mathsf M$ stages.

Earlier diagonal coefficients (VDHS, MIN, MIN3) came from minimizing ill-conditioned
spectral radii. The authors instead make the limit iteration matrices of the Dahlquist
error recursion nilpotent. With the isomorphism between node vectors and polynomials they
prove that $Q_\Delta=\mathrm{diag}(c_m/\mathsf M)$ makes the non-stiff limit $Q-Q_\Delta$
nilpotent (MIN-SR-NS, Thm. 2.8), and that the sweep-dependent choice
$Q_\Delta^{(k)}=\mathrm{diag}(c_m/k)$ makes the product of the stiff limits vanish after
$\mathsf M$ sweeps (MIN-SR-FLEX, Thm. 2.12). A third, stationary variant (MIN-SR-S) is
found numerically.

Order, [stability](/definitions/stability-function.md) and cost are studied numerically.
The new variants gain at least one order per sweep, MIN-SR-S appears
[A-stable](/properties/a-stability.md) for $K\ge3$ sweeps and MIN-SR-FLEX for every $K$
on Radau-right nodes, and their stability regions resemble those of serial LU-SDC. A cost
model counts Newton iterations of the [stage solves](/methods/implicit-stage-solvers.md)
and right-hand-side evaluations and divides the parallel cost by $0.8\,\mathsf M$. Under it
MIN-SR-NS wins on the Lorenz system, MIN-SR-S on the
[Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md) down to about
$10^{-6}$, and MIN-SR-FLEX on the 1D [Allen–Cahn equation](/benchmarks/allen-cahn-equation.md),
where MPI wall-clock runs confirm it. All runs use [pySDC](/software/pysdc.md).

# Version read

arXiv:2403.18641v2 [math.NA], 2 Dec 2024, the SIAM-style submitted manuscript
("Submitted to the editors DATE."), not the version of record; 24 pages, all read (pp. 9–12
also checked visually). Page-1 title and authors match Crossref; the running head
misspells "ACCROSS". The first author's surname carries a háček (Čaklović); the bundle
slug drops it. The reproducibility code is pySDC (Zenodo 10.5281/zenodo.13828395).
Section, equation, figure and page numbers cited here are those of arXiv v2.

# Key claims

Notation: $\mathsf M$ collocation nodes $0\le c_1<\dots<c_{\mathsf M}\le1$, $Q$ the
collocation matrix, $Q_\Delta$ the preconditioner, $\mathbf Y^{(k)}$ the node values after
sweep $k$, $K$ the number of sweeps, $\mathbf K(z)$ the error iteration matrix (bold, to
keep it apart from the sweep count). $Q_{\Delta,j}=\mathrm{diag}(c_1/j,\dots,c_{\mathsf M}/j)$.

1. SDC with a diagonal preconditioner can use as many threads as collocation nodes; its
   convergence speed, efficiency and stability depend critically on the diagonal
   coefficients. (Abstract, §1, §2.1) **Stated**
2. Classical SDC (lower-triangular $Q_\Delta$) is a specific iterated implicit Runge–Kutta
   method of van der Houwen & Sommeijer with lower-triangular preconditioner, and any
   iterated IRK of [45, Eq. 3.1a] with diagonal preconditioning equals the sweep
   $\mathbf Y^{(k+1)}-hQ_\Delta f(\mathbf Y^{(k+1)})=\mathbf 1\otimes y_n+h(Q-Q_\Delta)f(\mathbf Y^{(k)})$
   (2.8) with diagonal $Q_\Delta$, by identification $A=Q$, $b_i=\int_0^1\ell_i$, $c$ the
   nodes. (§1, §2.1) **Derived**
3. Setting $Q_\Delta=Q=A$ for the Butcher matrix of a DIRK or explicit Runge–Kutta method
   recovers that method from the sweep, so a generic SDC code runs any DIRK or ERK; pySDC
   does so. (Remark 2.2) **Derived**
4. The collocation update $y_n+h\,b^\top f(\mathbf Y)$ raises the order but can destroy
   stability: some preconditioners that appear A-stable lose it with this update. Only
   nodes with $c_{\mathsf M}=1$ (Radau-right, Lobatto) are therefore used. (Remark 2.1)
   **Stated** (experiments not shown)
5. On $y'=\lambda y$ the error $e^{(k)}=\mathbf Y^{(k)}-\mathbf Y^*$ to the collocation
   solution obeys $e^{(k+1)}=\mathbf K(z)e^{(k)}$ with
   $\mathbf K(z)=z(I-zQ_\Delta)^{-1}(Q-Q_\Delta)$; the non-stiff and stiff limits are
   $\mathbf K_{\mathrm{NS}}=\lim_{\lvert z\rvert\to0}\mathbf K(z)/z=Q-Q_\Delta$ and
   $\mathbf K_{\mathrm S}=\lim_{\lvert z\rvert\to\infty}\mathbf K(z)=I-Q_\Delta^{-1}Q$.
   (§2.2, Eqs. (2.11)–(2.13)) **Derived**
6. For $\mathsf M=4$ Radau-right nodes the literature coefficients give
   $\rho(\mathbf K_{\mathrm S})=0.025$ (VDHS), $0.42$ (MIN) and $0.0081$ (MIN3). (Table 1,
   App. A) **Shown**
7. Theorem 2.8 (MIN-SR-NS): for any nodes $0<c_1<\dots<c_{\mathsf M}\le1$,
   $Q-Q_{\Delta,\mathsf M}$ is nilpotent with index $\mathsf M$, so
   $\rho(\mathbf K_{\mathrm{NS}})=0$. (§2.2.2) **Proved**
8. Each MIN-SR-NS sweep removes the lowest-order term of the polynomial representation of
   the collocation error in the non-stiff limit until nothing is left. (Remark 2.9)
   **Derived**
9. MIN-SR-NS differs from van der Houwen & Sommeijer's non-stiff choice
   $Q_\Delta^{-1}c=Q^{-1}c$, which gives $Q_{\Delta,1}=\mathrm{diag}(c)$ (IEpar, implicit
   Euler from $t_n$ to each node); that work targeted non-stiff components at large steps,
   not $\rho(\mathbf K_{\mathrm{NS}})$. (§2.2.2) **Stated**
10. MIN-SR-S (Def. 2.10) is the diagonal $Q_\Delta$ with increasing entries that minimizes
    $\lvert\det[(1-t)I+tQ_\Delta^{-1}Q]-1\rvert$ at $t\in\{c_1,\dots,c_{\mathsf M}\}$. If
    $\mathbf K_{\mathrm S}$ is nilpotent this degree-$\mathsf M$ polynomial in $t$ vanishes
    identically; it vanishes at $t=0$, so checking the $\mathsf M$ nodes suffices. (§2.2.3)
    **Derived**
11. No theory says whether (2.37) has one, several or no solution; for $\mathsf M=2$ there
    are two minimizers, only one of them ordered. (§2.2.3) **Stated**
12. MIN-SR-S for $\mathsf M=4$ Radau-right nodes: $d=[0.05363588, 0.18297728, 0.31493338,
    0.38516736]$, $\rho(\mathbf K_{\mathrm S})=0.00024$. (§2.2.3, App. A) **Shown**
13. With MIN-SR-NS as initial guess the MIN-SR-S coefficients come out increasing up to
    $\mathsf M=4$; beyond, a power-law fit $\alpha t^\beta$ through
    $(c_i,\mathsf M d_i)$, rescaled by $1/(\mathsf M+1)$ at the new nodes, gives ordered
    coefficients with very small $\rho(\mathbf K_{\mathrm S})$ "in all numerical
    experiments". (§2.2.3) **Shown** (no numbers for $\mathsf M>4$)
14. Enforcing increasing coefficients when minimizing $\rho(I-Q_\Delta^{-1}Q)$ "provides a
    notable improvement in numerical stability". (Remark 3.1, §2.2.3) **Stated**
    (experiments not documented)
15. For nodes with $c_1=0$ (Lobatto) the first row and column are eliminated, the method
    is applied to the reduced collocation matrix on $c_2,\dots,c_{\mathsf M}$, and a zero
    coefficient is prepended. (Remark 2.11) **Derived**
16. Theorem 2.12 (MIN-SR-FLEX): for nodes with $c_1>0$,
    $(I-Q_{\Delta,\mathsf M}^{-1}Q)\cdots(I-Q_{\Delta,2}^{-1}Q)(I-Q_{\Delta,1}^{-1}Q)=0$, so
    the sweep-dependent choice $Q_\Delta^{(k)}=Q_{\Delta,k}$, $k=1,\dots,\mathsf M$, gives
    $\lim_{\lvert z\rvert\to\infty}e^{(\mathsf M)}=0$. The idea of iteration-dependent
    preconditioners is credited to Weiser. (§2.2.4) **Proved**
17. In the experiments MIN-SR-FLEX continues with MIN-SR-S for $k>\mathsf M$. (§2.2.4)
    **Stated**
18. For any diagonal $Q_\Delta$ the order after $K$ sweeps is $\min(K,p)$, $p$ the
    collocation order (van der Houwen et al., Thm. 2.1); confirmed for $y'=iy$ on
    $[0,2\pi]$. (§3.1, Figs. 2–4) **Stated** (cited) and **Shown**
19. MIN-SR-NS shows an unexplained extra order gain: Radau-right $\mathsf M=4$ gains two
    orders on the third sweep, Lobatto $\mathsf M=5$ from $K=3$ to $K=4$, and the Lorenz
    runs from $K=3$. (§3.1, Fig. 2; §4.2, Fig. 11) **Shown**
20. MIN-SR-S and MIN-SR-FLEX gain exactly one order per sweep, with larger errors than
    MIN-SR-NS on the non-stiff Dahlquist case; no literature analyses the order of a
    non-stationary iteration like MIN-SR-FLEX. (§3.1, Figs. 3–4) **Shown**
21. Picard SDC ($Q_\Delta=0$) with $K$ sweeps reproduces the stability contour of the
    explicit $K$-stage order-$K$ Runge–Kutta method (explicit Euler at $K=1$, classical RK4
    at $K=4$) and is never A-stable. (§3.2, Fig. 5) **Shown**
22. MIN-SR-NS is not A-stable for any $K$, but its regions are much larger than Picard's.
    (§3.2, Fig. 6) **Shown**
23. For $\mathsf M=4$ Radau-right nodes MIN-SR-S "appears" A-stable for $K\ge3$ and
    MIN-SR-FLEX "seems" A-stable for every $K$; Lobatto $\mathsf M=5$, $K=4$ MIN-SR-FLEX is
    not A-stable (not shown). No proof. (§3.2, Figs. 7–8, §5) **Shown** (plots only)
24. MIN-SR-FLEX stability regions are similar to those of Weiser's serial LU-SDC and of
    IE-SDC: "with an optimized choice of coefficients, parallelism in SDC can be obtained
    without loss of stability". (§3.2, Fig. 9) **Shown**
25. VDHS-SDC has very small stability regions for $K\in\{1,2,3\}$ that never include the
    imaginary axis, so it is unsuited to purely imaginary eigenvalues; MIN also has bounded
    regions. (§3.2, Fig. 10) **Shown**
26. Cost model: Newton iterations plus right-hand-side evaluations (Allen–Cahn: twice the
    Newton iterations), the parallel SDC cost divided by $\mathsf M P_{\mathrm{eff}}$ with
    assumed $P_{\mathrm{eff}}=0.8$; Newton to tolerance or 300 iterations. Measured MPI
    efficiencies on Allen–Cahn are 74–93 %. (§4.1) **Stated** (model) and **Shown**
    (efficiency)
27. Lorenz ($\mathsf M=4$, $K=4$): parallel and Picard preconditioners clearly beat
    explicit-Euler and LU-SDC; MIN-SR-NS is the most efficient and beats VDHS and
    ESDIRK4(3)6L[2]SA; RK4 is more efficient for errors above $10^{-4}$, MIN-SR-NS below
    $10^{-6}$; the advantage grows at $K=5$. (§4.2, Figs. 12–13) **Shown**
28. Prothero–Robinson ($\varepsilon=10^{-3}$, $K=4$): all parallel SDC variants show an
    error plateau over a range of $h$ (order reduction); MIN-SR-S beats LU-SDC down to an
    error of about $10^{-6}$, LU-SDC is more efficient beyond; with $K=6$ the crossover
    moves to about $10^{-8}$. (§4.3, Figs. 14–15) **Shown**
29. Allen–Cahn (2047 points, $T=50$): all methods saturate at about $2\times10^{-4}$
    (spatial error). Per step LU-SDC converges fastest, then ESDIRK43, then MIN-SR-FLEX; per
    modelled cost and per wall-clock time MIN-SR-FLEX is the most efficient, and LU-SDC
    would catch up only below 40 % parallel efficiency. (§4.4, Figs. 16–17) **Shown**
    (JUSUF, AMD EPYC 7742, Python 3.11.9 with mpi4py)
30. The new variants "can outperform existing parallel SDC variants, state-of-the-art
    serial SDC methods as well as RKM4 and ESDIRK43" on all three problems. (§5)
    **Stated**, and qualified by claims 27 and 28, where RK4 and LU-SDC win in parts of
    the accuracy range.

*(Compiler checks, not in the sources.)* The definition of A-stability in §3.2 is misprinted
(see slips). The efficiency conclusions rest on an assumed parallel efficiency, with
wall-clock timings only for Allen–Cahn, and on a Newton cost of about one right-hand side
per iteration, which favours implicit methods relative to large-scale settings.

# Printed slips

- Table 1: column header "spectral radius $\rho(K_S)$", but caption "Spectral radius
  $\rho(K_{NS})$ of the non-stiff iteration matrix"; the text and App. A say
  $\rho(K_S)$, so the caption is wrong.
- After (2.11): "(NS) denotes the non-stiff and (S) the stiff limit" is printed before
  $K_{NS}$, $K_S$ are defined.
- Proof of Thm. 2.8 (p. 9): "any polynomial $p\in P_{M-1}$ with
  $p(t)=\sum_{j=1}^{M}p_jt^j$" has degree $M$ and no constant term; (2.35) then sums
  $j=1..M-1$. The sum should run $j=0..M-1$ as in (2.44), and the image of the constant
  term under $Q-Q_{\Delta,M}$ is not treated (Props. 2.3 and 2.5 start at $n=1$). The same
  proof writes "kernel of $Q-Q_{\Delta,m}$" with $m$ for $M$.
- (2.31): vector entry $\tau_m^{n+1}$ for $\tau_M^{n+1}$.
- Prop. 2.7 states $1\le n\le M-1$, but for $n=M-1$ the monomial $\tau^M$ lies outside
  $\mathbb P_{M-1}$ and outside the stated isomorphism.
- Proof of Thm. 2.12: "$\tau^n\in\ker(I-Q_{\Delta,n+1}^{-1})$" lacks the factor $Q$;
  (2.46) prints the last factor as $(I-Q_{\Delta,M-2}^{-1}Q)$ although the text runs "until
  $k=M$"; "$P_{M-1}\setminus P_{M-1}\cup\{0\}$" lacks parentheses.
- Thm. 2.8 requires $0<\tau_1$, yet Figs. 2–4 (right) apply MIN-SR-NS to Lobatto nodes;
  Remark 2.11 is invoked for MIN-SR-S and MIN-SR-FLEX but not for MIN-SR-NS.
- §3.2: "A method is called A-stable if $S_C\subset\mathbb C^-$, that is, if the stability
  domain includes the negative complex half-plane". The contour $\lvert R\rvert=1$ lying in
  $\mathbb C^-$ is not the condition; A-stability requires the contour to lie in the closed
  right half-plane.
- §2.2.3: "Because order coefficients led to better stability" for "ordered".
- §4.2: "Figure 12 shows error against modelled computational cost for MIN-SR-S" while the
  discussion and the figure feature MIN-SR-NS.
- Fig. 9 axes Re($\lambda$)/Im($\lambda$), the other figures Re($z$)/Im($z$). Fig. 13
  caption "ESIDRK43"; the text mixes "RK4" and "RKM4". Fig. 17 legend "HOUWEN-SOMMEIJER"
  (left) and "VDHS" (right) for the same method.
- Typos: "parallel SDC methods are remain accurate", "can compete standard RKM ... against",
  "It is in important", "oberserved", "noticable", "efficiences", "loose this property".

# Notation map

| Čaklović et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u'=f(t,u)$, $u\in\mathbb R^{N_{\rm dof}}$ | $y'=f(t,y)$, $y\in\mathbb R^d$ | scalar notation in the text |
| $\Delta t$ | $h$ | |
| $t_0$, $u_0$ | $t_n$, $y_n$ | step index not written |
| $M$ | $\mathsf M$ | number of collocation nodes (stages, threads); **not the registry mass matrix** |
| $\tau_m$, $t_m=t_0+\tau_m\Delta t$ | $c_m$, $t_{n,m}$ | nodes in $[0,1]$; Radau-right = Radau IIA nodes |
| $A$, $b$, $c$, $s$ | same | stage-value form (1.2) |
| $Q$, $q_{ij}=\int_0^{\tau_i}\ell_j$ | $Q$ | the Butcher matrix $A$ of the collocation method |
| $Q_\Delta$, $Q_\Delta^{(k)}$ | $Q_\Delta$, $Q_\Delta^{(k)}$ | diagonal (parallel) or lower-triangular (serial); $(k)$: sweep-dependent |
| $Q_{\Delta,m}=\mathrm{diag}(\tau_j/m)$ | $Q_{\Delta,j}=\mathrm{diag}(c_m/j)$ | page-local index swap; $j=\mathsf M$ MIN-SR-NS, $j=k$ MIN-SR-FLEX, $j=1$ IEpar |
| $u^k$ | $\mathbf Y^{(k)}$ | node values after sweep $k$ |
| $K$ (sweeps) | $K$ | |
| $K(z)$, $K_{NS}$, $K_S$ | $\mathbf K(z)$, $\mathbf K_{\mathrm{NS}}$, $\mathbf K_{\mathrm S}$ | **bold here: the source uses $K$ for both the sweep count and the iteration matrix** |
| $e^k$ | $e^{(k)}$ | error to the collocation solution, not to $y(t)$ |
| $z=\Delta t\lambda$, $R(z)$ | $z=h\lambda$, $R(z)$ | |
| $S_C$ | $\partial\mathcal S$ | contour $\lvert R\rvert=1$ |
| $p^*$ | $p$ | order of the collocation method ($2\mathsf M-1$ Radau-right, $2\mathsf M-2$ Lobatto) |
| $d$, $d^M$ | kept | diagonal coefficients of $Q_\Delta$ |
| $\Phi$, $\mathcal Q$, $\boldsymbol\tau^n$ | kept, page-local | isomorphism $\mathbb R^{\mathsf M}\to\mathbb P_{\mathsf M-1}$ and node-power vectors; **$\Phi$ is not the registry elementary weight** |
| $\alpha$, $\beta$ (power law) | kept, page-local | **not the Shu–Osher or PID coefficients** |
| $P$, $P_{\rm eff}$ | kept, page-local | SDC preconditioning operator; parallel efficiency; **$P$ is not the registry stability polynomial** |
| $\varepsilon$ | $\varepsilon$ | Prothero–Robinson stiffness and Allen–Cahn interface width |

# Reference list

48 printed references, numbered [1]–[48] in SIAM style with titles. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` caklovic-2025. Several
items are pre-publication and stay their own entries: [1] ("Submitted", 2024; first author
printed as T. Baumann) is the submitted form of the ingested source
[Saupe et al. (2025)](/sources/saupe-2025.md) and is keyed `baumann-2024`; [10] (the
Freese et al. arXiv preprint 2403.20135) and [22] (Leveque et al. 2023, no venue). [21] is
the Kennedy & Carpenter 2016 DIRK review (a NASA technical report, the institution not
named). [25] is the ingested source [Munch et al. (2024)](/sources/munch-2024.md), printed
with the year 2023 and no volume. [29] and [37] print no pages. [41] is the pySDC software on
Zenodo, keyed `speck-2024`. [29] is cited as a "recent review" of parallel-in-time methods,
though its title is about deferred correction. No unparseable items.

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [Allen–Cahn equation](/benchmarks/allen-cahn-equation.md)
* [Deferred correction (DeC)](/methods/deferred-correction.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)](/methods/fully-implicit-runge-kutta.md)
* [Order reduction](/definitions/order-reduction.md)
* [Parallel-across-the-method spectral deferred correction (diagonal SDC)](/methods/parallel-sdc.md)
* [Parallel-in-time integration](/methods/parallel-in-time-integration.md)
* [Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md)
* [pySDC](/software/pysdc.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
