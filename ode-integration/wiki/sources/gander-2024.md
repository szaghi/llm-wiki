---
type: Source
title: "Gander & Palitta (2024) — A New ParaDiag Time-Parallel Time Integration Method"
description: "Solves the all-at-once backward-Euler system of linear parabolic problems by FFT diagonalization of the circulant part plus an exact Sherman–Morrison–Woodbury correction whose capacitance system is solved by a FOM-like Krylov method, proves its conditioning for SPD operators, and extends it to α-circulants and BDF up to order six."
resource: "doi:10.1137/23m1568028"
source_kind: paper
authors: [Gander M.J., Palitta D.]
year: 2024
venue: "SIAM J. Sci. Comput. 46:A697-A718"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_SIAM_Journal_on_Scientific_Computing_Gander_A_New_ParaDiag_Time-Parallel_Time_Integration_Method.pdf"
tags: [parallel, paradiag, linear-algebra, implicit-stage-solvers, bdf, parabolic]
timestamp: 2026-10-20T10:00:00Z
---

# Summary

The paper adds a member to the [ParaDiag](/methods/paradiag.md) family of
[parallel-in-time](/methods/parallel-in-time-integration.md) solvers. For a
linear parabolic or advection–diffusion problem semi-discretized as
$y'=Ly+g(t)$, backward Euler with $N$ uniform steps gives the all-at-once
matrix equation $(I-hL)Y-Y\Sigma_1^\top=[y_0+hg(t_1),\dots,hg(t_N)]$, where the
time-shift matrix $\Sigma_1$ (ones on the first subdiagonal) is a Jordan
block. It is not diagonalizable, but $\Sigma_1=C_1-e_1e_N^\top$ with $C_1$
circulant. Earlier ParaDiag methods drop the rank-one term and use the
circulant as a GMRES preconditioner (McDonald, Pestana & Wathen), or use
variable steps to make the time matrix diagonalizable. Here the rank-one
term is kept **exactly** through the Sherman–Morrison–Woodbury (SMW)
formula. After an FFT in time the main part is block diagonal, with $N$
shifted blocks $(1-\omega_i)I-hL$ solved in parallel. The SMW capacitance
system has spatial size and is solved by a FOM-like Galerkin method on the
polynomial Krylov space of $L$; each residual check costs one
parallel-in-time loop. These shifted complex solves belong to the
toolbox of [solvers for implicit stages](/methods/implicit-stage-solvers.md).
For $-L$ symmetric positive definite the capacitance matrix is Hermitian
positive definite with condition number at most $1+1/(h\lambda_{\min}(-L))$.

An α-circulant variant shrinks the SMW correction by $\alpha^{1/N}$, at the
price of an eigenvector matrix with condition number $\alpha^{-(N-1)/N}$.
The method extends to [BDF](/methods/backward-differentiation-formula.md)
of order $k\le6$, where the time matrix is circulant plus rank $k$ and the
inner solve uses a block Krylov space; this extension is not tested. The
authors expect the same structure for all-at-once
[fully implicit Runge–Kutta](/methods/fully-implicit-runge-kutta.md)
discretizations, by citation only. Experiments on the 2D
[heat equation](/benchmarks/heat-equation.md) and a recirculating 2D
advection–diffusion problem count cost in parallel-in-time loops (#PinT),
on a laptop, without a parallel implementation. One FOM iteration
suffices for the heat equation. For advection–diffusion the α-variant
needs 3 #PinT, against 5 for circulant-preconditioned GMRES and 2 for the
Kressner–Massei–Zhu interpolation scheme, with comparable or better
accuracy at equal #PinT.

# Version read

arXiv:2304.12597v2 [math.NA], stamped 23 September 2023, 22 pages, all
read. This is not the SIAM version of record (pp. A697–A718). It thanks
anonymous reviewers, so it is most likely the post-review text, but the
file does not say so. Page 1 prints the title in capitals; title and
authors match the published version. Equation, theorem and table numbers
are those of arXiv v2.

# Key claims

Registry notation: semi-discrete problem $y'=Ly+g(t)$ with $L=-K$ (source
stiffness matrix $K$, sign convention $u'=-Ku+f$), step $h$ (source $\tau$),
dimension $d$ (source $\bar n$), BDF order $k$ (source $s$), number of time
steps $N$ (source $\ell$; each step is a slice, $\Delta T=h$). Page-local, as on
[ParaDiag](/methods/paradiag.md):
all-at-once matrix $Y=[y_1,\dots,y_N]$ (source $U$), DFT matrix $\mathcal D$
(source $F$), circulant eigenvalues $\omega_i$ and SMW weights $g_i$,
capacitance matrix $S_N$ (source $J_\ell$), circulant parameter
$\alpha$, and the right-hand side $R=[y_0+hg(t_1),\dots,hg(t_N)]$.

1. Backward Euler with $N$ uniform steps gives the all-at-once equation
   $(I-hL)Y-Y\Sigma_1^\top=R$, with $\Sigma_1$ zero except ones on the first
   subdiagonal (§1, Eq. (1.2)). **Stated** (cites Palitta 2021)
2. $\Sigma_1$ is a Jordan block, not diagonalizable, but
   $\Sigma_1=C_1-e_1e_N^\top$ with $C_1$ the circulant shift, and
   $\mathcal DC_1\mathcal D^{-1}=\mathrm{diag}(\omega_i)$ (§2, Eq. (2.1)). **Derived**
3. Keeping the rank-one term, the FFT-transformed Kronecker system is
   $P+UV^\top$ with $P=I_N\otimes(I-hL)-\mathrm{diag}(\omega_i)\otimes I$
   block diagonal; SMW gives the solution through $P^{-1}$ and the inverse
   of the $d\times d$ capacitance matrix (§2, Eqs. (2.3)–(2.4)). **Derived**
4. Because $\mathcal De_1=\mathbf 1$, the capacitance matrix is
   $S_N=I+\sum_{i=1}^Ng_i\bigl((1-\omega_i)I-hL\bigr)^{-1}$,
   $[g_i]=\mathcal D^{-\top}e_N$ (§2, Eq. (2.6)). **Derived**
5. Forming $S_N$ explicitly would apply $P^{-1}$ to $d$ columns and
   destroy time parallelism, so a projection method is used (§2).
   **Stated**
6. The capacitance system is solved by a FOM-like Galerkin method on the
   polynomial Krylov space of $L$ (not of $S_N$). Shift invariance of
   the Arnoldi relation reduces the Galerkin condition to an $m\times m$
   system (3.4) with a closed-form residual norm (3.5). Each residual
   check needs $N$ parallel shifted solves (§3, Alg. 3.1). **Derived**
7. Checking the residual every $q_{\mathrm r}$ iterations makes the total
   number of parallel-in-time loops $m/q_{\mathrm r}+2$ (§3). **Stated**
8. Theorem 3.1: if $-L$ is symmetric positive definite, $S_N$ is
   Hermitian positive definite for every $N\ge1$ and
   $\operatorname{cond}(S_N)\le1+1/(h\lambda_{\min}(-L))$ (Eq. (3.6), proof in the
   appendix). **Proved** (the reader finds rigor gaps in the proof; the
   statement is plausible and checkable eigenvalue by eigenvalue)
9. For symmetric positive definite $-L$ the FOM-like iterate minimizes the
   $S_N$-energy error over the Krylov space, and the method is the
   Lanczos approximation of a rational function of $L$ applied to $b$, so a
   priori Lanczos bounds could fix $m$ in advance (§3). **Stated**
10. Convergence is fast for large $h\lambda_{\min}(-L)$ (coarse time grid)
    and can need many iterations on very fine time grids with small
    $\lambda_{\min}(-L)$ (§3). **Stated** (from the bound)
11. With $\Sigma_1=C_\alpha-\alpha e_1e_N^\top$, $C_\alpha=\mathcal D_\alpha^{-1}\mathcal D^{-1}\Omega_\alpha\mathcal D\mathcal D_\alpha$,
    $\Omega_\alpha=\alpha^{1/N}\mathrm{diag}(\omega_i)$, the SMW correction carries the weight
    $\alpha^{1/N}$ and the capacitance matrix
    $I+\alpha^{1/N}\sum_ig_i\bigl((1-\omega_i)I-hL\bigr)^{-1}$ is close to $I$ for
    $\alpha\ll1$ (§4, Eqs. (4.1)–(4.3)). **Derived**
12. $\operatorname{cond}(\mathcal D\mathcal D_\alpha)=\alpha^{-(N-1)/N}$, and the error of the computed
    solution is "proportional to" it, so a very small $\alpha$ pollutes the
    solution; choosing $\alpha$ is a trade-off (§4). **Stated** (observed,
    not proved)
13. For BDF of order $k\le6$ the all-at-once system is
    $(I-h\beta L)Y-Y\Sigma_k^\top=G$, and $\Sigma_k$ is a circulant minus a
    rank-$k$ term; the same SMW approach applies with a $kd\times kd$
    capacitance matrix (§5, Eqs. (5.1)–(5.3), Table 5.1). **Derived**
14. The block capacitance system is solved by a Galerkin method on a block
    Krylov space; Proposition 5.1 gives the reduced system and the
    residual norm (§5). **Proved** (one line, "the exact same arguments"
    as §3)
15. BDF of order $k>6$ is unstable (§5, citing Ascher & Petzold). **Stated**
16. 2D heat equation, 5-point Laplacian: the bound (3.6) is 13.969,
    26.938 and about 52.88 for $N=256,512,1024$, essentially independent
    of $d\in\{65\,536,262\,144,1\,048\,576\}$, and grows linearly in $N$
    (Table 6.1). **Shown** (computed)
17. Heat equation with $g=0$, $y_0=xy(x-1)(1-y)$: a **single** iteration of
    Alg. 3.1 reaches relative residual below $10^{-8}$ for every $d$ and $N$
    of Table 6.1; the spectrum of $S_N$ lies in $[1,1.004]$ (§6.1).
    **Shown**
18. Advection–diffusion ($d=65\,536$, viscosity $2^{-5}$, $N=64$, one FOM
    iteration): the direct α-circulant part $Y_1$ is essentially
    independent of $\alpha$ and the correction $Y_2$ scales with $\alpha$. If a
    relative residual near $10^{-7}$ suffices, $Y_2$ can be dropped with
    $\alpha\approx10^{-7}$, leaving one parallel-in-time loop (§6.2, Fig. 6.1).
    **Shown**
19. In the same test the error and residual of $Y_1+Y_2$ scale like $\alpha^2$,
    the residual of $Y_1$ alone like $\alpha$; for $\alpha\le10^{-4}$ the error grows
    as $\operatorname{cond}(\mathcal D\mathcal D_\alpha)$ takes over (§6.2, Fig. 6.1). **Shown**
20. Comparison over $d\in\{16\,384,65\,536\}$, $N\in\{32,64,128\}$, viscosity
    $10^{-1},10^{-2},10^{-3}$ (Table 6.2): Alg. 4.1 ($\alpha=10^{-4}$) uses 3
    #PinT in every case, residuals $4.0\cdot10^{-13}$ to $3.4\cdot10^{-10}$;
    circulant-preconditioned GMRES uses 5 #PinT, residuals $4.5\cdot10^{-14}$
    to $2.1\cdot10^{-10}$; Ev-Int (Kressner–Massei–Zhu, two loops) uses 2
    #PinT, residuals $2.2\cdot10^{-12}$ to $8.6\cdot10^{-11}$. Alg. 4.1 and
    GMRES counts are robust in $d$, $N$ and viscosity (§6.3). **Shown**
21. Alg. 4.1 gets more accurate as the viscosity decreases; GMRES usually
    shows the opposite trend; Ev-Int is less regular (§6.3). **Shown**
22. At equal cost, Alg. 4.1 is "in general at least as accurate as" Ev-Int
    at 2 #PinT and "often three orders of magnitude more accurate" at
    1 #PinT ($8.2\cdot10^{-9}$ to $5.9\cdot10^{-8}$ against $3.4\cdot10^{-6}$ to
    $2.9\cdot10^{-5}$) (§6.3, Table 6.3). **Shown** (not uniformly: several
    2-#PinT rows favor Ev-Int)
23. No timings are reported: runs are on a laptop, $P^{-1}$ is applied
    sequentially, and #PinT is proposed as the fair cost measure (§6).
    **Stated**
24. The approach applies to any time discretization whose all-at-once
    operator is circulant plus low rank; through Kressner, Massei & Zhu
    (§4 of their paper), all-at-once Runge–Kutta discretizations have such a
    structure (§7). **Stated**
25. Low-rank space–time matrix-equation solvers need a low-rank
    right-hand side $R$; the new method does not (§1). **Stated**

# Printed slips

- Eq. (2.2): the right-hand side is printed "$[u_0+f_1,\dots,f_\ell]$",
  missing $\tau$; (1.2), (2.3) and (2.4) have it (checked visually, p. 3).
- §3, shifted Arnoldi relation (p. 6):
  "$((1-\pi_i)I_{\bar n}+\tau K)V_m=V_m((1-\pi_i)I_m+\tau T_m)+t_{m+1,m}v_{m+1}e_m^T$".
  The last term needs the factor $\tau$; the omission propagates into
  (3.3)–(3.5) and, as $\tau\beta$, into (5.6). The same sentence has the
  misplaced parenthesis "$((1-\pi_iI_m)+\tau T_m)^{-1}$".
- Alg. 3.1, line 12 uses an undefined index $j$ ("$t_{m+1,j}$", "$e_j^T$")
  where (3.4) has $m$; line 13 omits the weights $g_i$ (source $\gamma_i$) that (3.5) has; the
  input "$b\in\mathbb R^{\bar n}$" is complex in general.
- §3, p. 6: the rational function is printed
  "$f(K)=(I+\sum_i\gamma_i((1-\pi_i)I_{\bar n}+\tau K)^{-1})^{-1}b$", with $b$
  inside the definition (correct on p. 8).
- §6.3, GMRES preconditioner
  "$x\mapsto(F\otimes I_{\bar n})(I_\ell\otimes(I_{\bar n}+\tau K)+\Pi_1\otimes I_{\bar n})(F^{-1}\otimes I_{\bar n})x$"
  has $+\Pi_1$ where the circulant approximation has $-\Pi_1\otimes I$, and
  defines the preconditioner where the text applies its inverse.
- §5: $N:=F^{-T}[e_{\ell-s+1},\dots,e_\ell]\boldsymbol\alpha_s^T$ lacks the
  "$\otimes I_{\bar n}$" that $M$ has; $\mathcal V_m\in\mathbb R^{n\times sm}$ writes $n$
  for $\bar n$.
- Appendix: $z\in\mathbb C^\ell$ should be $\mathbb C^{\bar n}$; "$|\pi_i|\le1$"
  where $|\pi_i|=1$; the even-$\ell$ sum
  "$\sum_{j\in J}(\mathrm{Re}(\pi_j)-\mathrm{Re}(\pi_j))$" should pair $\pi_j$ with
  its partner $\pi_{k_j}$; "nonegativity".
- Table 6.1 caption: "Upper bound of the coefficient matrix" means the
  bound on its condition number.
- Footnote 1 "A anonymous reviewer"; §3 "the the right-hand side".

The proof of Theorem 3.1 treats $\mathrm{Re}(g_iw)$ as
$\mathrm{Re}(g_i)\mathrm{Re}(w)$ for complex $w$, writes a minimum of a sum as
a sum of minima with an equality sign, and evaluates (7.1) with
$h\lambda_{\max}(-L)$ for every $i$ regardless of the sign of
$\mathrm{Re}(\omega_i)$ (reader's finding, not a typo).

# Notation map

| Gander & Palitta (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $K$ | $-L$ | stiffness matrix of $u'=-Ku+f$; **collision with the iteration count $K$** |
| $u$, $f$ | $y$, $g(t)$ | forcing renamed to keep $f$ for the right-hand side |
| $\tau$ | $h$ | **collision with the tree $\tau$**; $h$ is the source's mesh width, here $\Delta x$ |
| **$h$** | $\Delta x$ | mesh width $1/(n+1)$ |
| $\bar n$, $n$ | $d$, — | spatial unknowns, nodes per direction |
| **$\ell$** | $N$ | number of time steps; **$\ell$ is the registry micro-step index** |
| **$U$** | $Y$ (page-local) | all-at-once solution matrix; **collision with the Parareal iterate $U^{(k)}_j$** |
| $\Sigma_1$, $\Sigma_s$, $C_1$, $C_s$, $C_\alpha$ | $\Sigma_1$, $\Sigma_k$, $C_1$, $C_k$, $C_\alpha$ | time matrices and their circulant completions |
| **$F$** | $\mathcal D$ (page-local, as on [ParaDiag](/methods/paradiag.md)) | DFT matrix; **collisions with the elementary differential $F(\tau)$ and the fine propagator $\mathcal F$** |
| **$\pi_i$**, $\Pi_1$, $\Pi_\alpha$ | $\omega_i$, $\Omega$, $\Omega_\alpha$ (page-local, as on ParaDiag) | circulant eigenvalues, the $N$-th roots of unity; **collisions with the processor $\pi_h$ and the Patankar notation** |
| **$\gamma_i$** | $g_i$ (page-local, as on ParaDiag) | entries of $\mathcal D^{-\top}e_N$; renamed because of the composition weights $\gamma_j$ |
| **$J_\ell$**, $J^{(s)}_\ell$ | $S_N$, $S^{(k)}_N$ (page-local, as on ParaDiag) | SMW capacitance matrix; **$J$ is the registry Jacobian** |
| **$M$**, $N$, $P$ | $U$, $V$, $P$ (page-local, as on ParaDiag) | SMW factors and block-diagonal part; **$M$ is the registry mass matrix, $N$ the slice count; this $U$ is not the source's solution matrix $U$** |
| **$\alpha$** | $\alpha$ (page-local) | α-circulant parameter; **also the BDF $\alpha_j$ and $\boldsymbol\alpha_s$ in §5, and the Shu–Osher $\alpha$** |
| $D_\alpha$ | $\mathcal D_\alpha$ | diagonal scaling of the α-circulant transform |
| $\alpha_j$, $\beta$ | $\alpha_j$, $\beta$ in the form $y_n=\sum_j\alpha_jy_{n-j}+h\beta f_n$ | signs flipped against Ascher & Petzold; not the registry normalization $\sum_j\alpha_jy_{n+j}=h\sum_j\beta_jf_{n+j}$ |
| **$s$** | $k$ | BDF order; **$s$ is the registry stage count** |
| **$\mathcal K_m(K,b)$** | polynomial Krylov space of $L$ (page-local) | **collision with the registry $\mathcal K_m$ of weak stage order** |
| $V_m$, $T_m$, $t_{m+1,m}$, $h_i$, $S_i$ | page-local | Arnoldi basis and projected quantities |
| **$q$** | $q_{\mathrm r}$ | residual-check frequency; **$q$ is the registry stage order** |
| $U_1$, $U_2$ | $Y_1$, $Y_2$ | α-circulant direct part and SMW correction |
| $\nu$ | viscosity (page-local) | **collision with the Courant number $\nu$** |
| $\kappa(\cdot)$ | $\operatorname{cond}(\cdot)$ | condition number |
| #PinT | #PinT | number of parallel-in-time loops, the paper's cost measure |

# Reference list

The paper prints 34 references in numbered style, alphabetical, without
DOIs. All are merged complete into the [bibliography](/bibliography.md)
with `citedby` gander-2024. Refs. [16] and [34] print a ditto dash for
repeated authors and were expanded. Three arXiv preprints ([5], [13],
[19]) are their own items. Refs. [27] and [34] print no page or article
number, and [17] prints a URL without pages. Same-author same-year works
take printed-order suffixes: `gander-2019`/`gander-2019-b`,
`gander-2020`/`gander-2020-b`, `palitta-2021`/`palitta-2021-b`.

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [Backward differentiation formulas (BDF)](/methods/backward-differentiation-formula.md)
* [Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)](/methods/fully-implicit-runge-kutta.md)
* [Heat equation](/benchmarks/heat-equation.md)
* [ParaDiag: diagonalization-based parallel-in-time methods](/methods/paradiag.md)
* [Parallel-in-time integration](/methods/parallel-in-time-integration.md)
* [Parareal](/methods/parareal.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
