---
type: Source
title: "Buvoli & Minion (2024) — Exponential Runge–Kutta Parareal for non-diffusive equations"
description: "Uses exponential Runge–Kutta methods as both Parareal propagators for dispersive and hyperbolic problems, shows that repartitioning the linear operator is essential for stability, explains convergence mode by mode with a partitioned-Dahlquist analysis, and reaches 10x to 24x speedups on NLS, KP and Vlasov–Poisson runs."
resource: "doi:10.1016/j.jcp.2023.112623"
source_kind: paper
authors: [Buvoli T., Minion M.L.]
year: 2024
venue: "J. Comput. Phys. 497:112623"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_Journal_of_Computational_Physics_Buvoli_Exponential_Runge-Kutta_Parareal_for_non-diffusive_equations.pdf"
tags: [parallel, parareal, exponential, stability, hpc]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

[Parareal](/methods/parareal.md) converges slowly or goes unstable on
non-diffusive (dispersive, hyperbolic) problems unless the coarse
propagator closely tracks the fine one. The paper uses
[exponential Runge–Kutta](/methods/exponential-integrators.md) methods
(exponential Euler, Cox–Matthews ETD2RK and ETD3RK, Krogstad's fourth-order
scheme) as both coarse and fine propagators for $y'=Ly+N(t,y)$ with $L$ of
purely imaginary spectrum. Exponential integrators resolve the fast linear
waves even at coarse steps. All experiments use diagonal $L$, so φ-functions
are evaluated pointwise ([evaluating φ-functions](/methods/phi-function-evaluation.md)).

On the 1D [nonlinear Schrödinger equation](/benchmarks/nonlinear-schrodinger-equation.md)
on 2048 cores, Parareal with classical exponential RK diverges. With the
repartitioning of Buvoli & Minion (2022), which adds a damping $\epsilon D$ to $L$ and
subtracts it from $N$, rotating the spectrum by an angle $\rho$ into the left
half-plane, it converges. The theoretical speedup is 38.5 and the achieved
one 10.4, limited by communication. A high-frequency mode in the data stalls
convergence; more coarse steps per slice restore it at the cost of speedup.

A linear analysis on the partitioned Dahlquist equation explains this. It
writes the Parareal [stability function](/definitions/stability-function.md)
$R(z_1,z_2)$ of a whole iteration and a convergence region where the
error-propagation matrix has $\lVert\mathcal E\rVert_\infty<1$. Parareal
magnifies the mild instabilities of serial exponential RK, and
repartitioning removes them. Because the convergence region is narrow along
the stiff direction, only temporal modes with $|h\lambda|<r_1^{\max}$
converge to fine accuracy; the rest stay at coarse accuracy. A mode-by-mode
check on NLS confirms the prediction. The method is then run on the 2D KP-I equation, a
dispersive relative of the [Korteweg–de Vries equation](/benchmarks/korteweg-de-vries-equation.md),
with a 9.1x–11.7x reduction in time to solution. On the 2D bump-on-tail
[Vlasov–Poisson](/benchmarks/vlasov-poisson-equation.md) problem it gives 24x,
both against serial fourth-order exponential RK, and there the speedup
model matches the measured speedup. The paper places the method within
[parallel-in-time integration](/methods/parallel-in-time-integration.md).

# Version read

arXiv:2301.03764v2 [math.NA], 6 November 2023, Elsevier preprint template,
not the version of record. The file has 33 pages, but the footers number
them "Page k of 34": **the last page is missing from the file**. The text
runs without a gap to Appendix H and Fig. 24 on page 33, and the reference
list (pp. 25–27, refs [1]–[79]) is complete, so the missing page held at
most a trailing figure or nothing. Page 1 prints "Non-Diffusive Equations"
in title case; Crossref has "non-diffusive equations". Authors match, and
the file prints no DOI. Equation, figure and section numbers are those of
arXiv v2. This paper is distinct from the NPRK papers buvoli-2025 and
buvoli-2026.

# Key claims

Registry notation: $y'=Ly+N(t,y)$ (source $\mathbf y'=\mathbf L\mathbf y+N$; page-local
remainder $N(t,y)$, always written with its arguments), fine step $h$, slice
length $\Delta T$, number of slices $N$ (source $N_p$, also the number of
processors), iterate $U^{(k)}_j$ (source $y^k_n$), propagators $\mathcal F$,
$\mathcal G$, iteration count $K$, $\phi_k$ with the registry normalization
(source $\varphi_j$). Page-local: fine and coarse steps per slice $N_f$, $N_g$,
so $\Delta T=N_fh$ and the coarse step is $h_{\mathcal G}=N_fh/N_g$; total fine
steps $N_s=NN_f$; cost ratio $\alpha$; repartitioning weight $\epsilon$ and
angle $\rho$; partitioned Dahlquist parameters $z_i=h\lambda_i=\mathrm ir_i$;
Parareal matrices $\mathcal M_{\mathcal G}$, $\mathcal M_{\mathcal F}$ and
$\mathcal E=I-\mathcal M_{\mathcal G}^{-1}\mathcal M_{\mathcal F}$.

1. Parareal on non-diffusive problems converges slowly or goes unstable;
   unmodified Parareal needs a coarse propagator close to the fine one
   (§1, §4). **Stated**
2. Parareal speedup without communication is
   $S=N/\bigl(N\alpha+K(1+\alpha)\bigr)$ with $\alpha=C_{\mathcal G}/C_{\mathcal F}$ (Eq. (5), from
   ref [7]). **Stated** (a compiler check, not in the sources, reproduces the printed
   38.5 and 10.16)
3. Exponential integrators on operators with purely imaginary eigenvalues
   have stability regions of similar size to explicit integrators, but the
   instability is so weak that solutions stay usable over moderate step
   counts (§3.2, ref [16]). **Stated**
4. Repartitioning $\hat L=L+\epsilon D$, $\hat N=N-\epsilon Dy$ with
   $D=-U_L\lvert\Lambda\rvert U_L^{-1}$ and $\epsilon=1/\tan(\pi/2-\rho)$ rotates every
   eigenvalue of a non-diffusive $L$ by $\rho$ into the left half-plane and
   gives the exponential integrator a large stability region for a range
   of small $\epsilon$ (Eqs. (13)–(15), ref [16]). **Stated**
5. NLS (Table 3: $N=2048$, $N_s=2^{16}$, $N_f=32$, $N_g=1$, fine ERK4,
   coarse ERK3, $t=14$): Parareal with classical exponential RK diverges
   (error grows for $k>2$); repartitioned Parareal converges to the
   fine solution (error $3\times10^{-9}$) up to 38.5 times faster than serial
   ERK4 in theory (§4, Fig. 2). **Shown**
6. The achieved speedup on 2048 Cori cores is 10.4, a quarter of the
   theoretical 38.5, because of communication. Eq. (5) holds only when one
   fine step costs much more than sending the solution between nodes (§4).
   **Shown**
7. With an added high-frequency mode (data (20)), repartitioned Parareal
   stays stable but stalls at $3\times10^{-7}$ for $K\le6$. With $K$ up to
   160, classical exponential Parareal blows up for $k>9$ and the
   repartitioned one converges after 150 iterations, with theoretical
   speedup 10.16 (§4, Fig. 3, App. C). **Shown**
8. With 45-mode data (21), $N_g=1$ does not converge within six
   iterations; $N_g\in\{2,3\}$ improves convergence markedly at a cost in
   speedup (§4, Fig. 4). **Shown**
9. On the partitioned Dahlquist equation $y'=\lambda_1y+\lambda_2y$ every
   one-step exponential method, and Parareal itself, reduce to
   $y_{n+1}=R(z_1,z_2)y_n$. The Parareal error obeys
   $e^{(k)}=\mathcal Ee^{(k-1)}$, and the stability function of $k$ iterations is
   $R=c_2^\top\bigl(\sum_{i=0}^k\mathcal E^i\bigr)\mathcal M_{\mathcal G}^{-1}c_1$
   (Eqs. (30)–(37); formulas from ref [71] for unpartitioned problems).
   **Derived**
10. Parareal with classical exponential RK is stable on a small part of
    the NLS parameter rectangle, and worse as $k$ grows; repartitioning
    enlarges the stability region greatly and the residual instabilities
    are too weak to matter (§5.3, Fig. 5). **Shown**
11. Even with repartitioning, exponential Parareal is stable only when
    $|r_2|\ll|r_1|$: the linear term must carry most of the stiffness (§5.3).
    **Shown**
12. Parareal magnifies the instabilities of serial ERK4, which is stable
    over the whole range of Fig. 5 with growth rates below 1.01. So
    repartitioning matters for Parareal even on time scales where serial
    exponential integrators do not need it (§5.3). **Shown**
13. $\mathcal E$ is nilpotent (exact convergence after $N$ iterations), so its
    spectrum does not give the rate. $\lVert\mathcal E\rVert<1$ guarantees
    monotone convergence (Eq. (39)), and
    $\lVert\mathcal E\rVert_\infty=\frac{1-|R_{\mathcal G}|^{N}}{1-|R_{\mathcal G}|}|R_{\mathcal G}-R_{\mathcal F}|$
    (Eq. (40), from ref [15]) (§5.4). **Stated**
14. Near the origin the convergence region grows about linearly with
    $N_g$, and for fixed small $(r_1,r_2)$,
    $\lVert\mathcal E\rVert_\infty=O(N_g^{-p})$ with $p$ the coarse order (§5.4,
    Remark 1, App. F). **Derived** (heuristic; App. F is internally
    inconsistent, see Printed slips)
15. For the NLS runs of Fig. 4 the whole $r_2$ range lies inside the
    convergence region but less than 20% of the $r_1$ range does, even with
    $N_g=3$: $r_1^{\max}=0.073,0.133,0.188$ for $N_g=1,2,3$ (§5.4, Figs. 6–7).
    **Shown**
16. Linear analysis predicts monotone convergence exactly for the Fourier
    coefficients with $r_1(n)=hn^2/16<r_1^{\max}$, i.e. $|n|\le73,99,118$ for
    $N_g=1,2,3$. Mode-by-mode Parareal errors on NLS confirm this "very
    accurately"; modes outside stay near coarse accuracy (§5.5, Figs.
    7–8). **Shown**
17. A higher-order coarse integrator (ERK1 to ERK4) gives a larger
    convergence region, to be weighed against reduced speedup (§5.6,
    Fig. 9). **Shown**
18. Without repartitioning ($\rho=0$) the convergence region is unbounded
    along $r_2=0$, where the exponential integrator is exact. Any
    repartitioning destroys this, and larger $\rho$ shrinks the region, so
    the smallest stabilizing $\rho$ should be chosen (§5.6, Fig. 10).
    **Shown**
19. Parareal reaches fine accuracy for low-frequency (non-stiff)
    oscillatory modes and only coarse accuracy for high-frequency (stiff)
    ones. Fast convergence cannot be guaranteed for high spatial
    frequencies of non-diffusive PDEs; rapid spectral broadening,
    high-order dispersive terms and Fourier pseudo-spectral discretizations
    are the hardest cases (§5.7, §7). **Derived** (linear analysis,
    supported by experiments)
20. Recipe for diagonalizable $L$ with spectral radius much larger than that of
    $\partial N/\partial y$: check stability on the rectangle (48), compute
    $r_1^{\max}(h)$ (49), and expect monotone convergence for coefficients
    with $|h\lambda_n|<r_1^{\max}(h)$ (50) (§5.7). **Derived**
21. KP-I (Table 4a: $N=8192$, $N_s=2^{18}$, $N_f=32$, $N_g\in\{1,2,3\}$,
    $K\le28$, $t=4$): no configuration converges monotonically over all
    $k$ (fast early reduction, then a plateau); $N_g=3$ reaches accuracy
    comparable to the fine integrator; at $k=28$ the errors
    $2.7\times10^{-7}$, $1.3\times10^{-8}$, $1.8\times10^{-9}$ are reached 9.09x, 10.15x and 11.71x faster
    than serial ERK4 (§6.2, Fig. 14). **Shown**
22. For KP the speedup model (5) agrees with the achieved speedup because
    a 2D step (several 2D FFTs) is expensive relative to communication.
    The full KP run would need 256 nodes, so convergence was computed
    serially and the speedup extrapolated from a shortened run on 64 nodes
    (§6.1–6.2). **Shown** (with extrapolation)
23. Vlasov–Poisson bump-on-tail (Table 4b: $N=2048$, $N_s=2^{17}$,
    $N_f=64$, $N_g\in\{2,3\}$, $K\le12$, $t=50$): $N_g=2$ fails to converge
    although linear analysis predicts barely convergent behavior; $N_g=3$
    converges monotonically in eight iterations to error $6.6\times10^{-8}$,
    24 times faster than serial ERK4 (§6.3, Fig. 16). **Shown**
24. Possible reasons for the $N_g=2$ failure: linear analysis is not
    guaranteed for nonlinear problems, the case is only barely convergent,
    and the nonlinear term may not be non-stiff as assumed (§6.3).
    **Stated** (conjecture)
25. The larger Vlasov–Poisson gain (24x against about 10x for KP) comes
    from the absence of highly oscillatory temporal components, which
    allows a coarse step 21.3 times the fine step against 10.6 for KP
    (§6.3). **Shown**
26. The authors claim this is the first use of ETD Runge–Kutta methods
    inside Parareal. All experiments use diagonal $L$; non-diagonal $L$ is
    future work (§7). **Stated**

# Printed slips

- Eq. (9): $\varphi_j(h\mathbf L)=\int_0^1e^{(1-s)h\mathbf L}s^j\,ds$. The
  standard integrand has $s^{j-1}/(j-1)!$. As printed $\varphi_1(0)=1/2$,
  inconsistent with exponential Euler (10) and the App. A tableaux, which
  need $\varphi_j(0)=1/j!$.
- Eqs. (11)–(12): the first stage term carries $c_j$ where $c_i$ is meant;
  $N(c_j,Y_j)$ should be $N(t_n+c_jh,Y_j)$; and the sums lack the factor $h$
  (cf. (10)). §3.1 prints "$\varphi_0(h\mathbf L)\mathbf y_n=\mathbf y_n+\varphi_1(h\mathbf L)\mathbf L\mathbf y_n$"
  without $h$, "$\varphi_j(hK)$" for $\varphi_j(h\mathbf L)$, and "EKR4".
- Eq. (13): "$\hat N(t,\mathbf y)=N(t,\mathbf y)-\epsilon\mathbf D$", missing $\mathbf y$.
- §3.2 rotates the eigenvalues "by $\rho$ degrees" while
  $\rho\in(0,\pi/2)$ is in radians (§5.6 says radians), and writes the
  wedge as the two-element set "$\theta\in\{\pi/2+\rho,3\pi/2-\rho\}$".
- Eq. (17): "$N(t,\mathbf y)=2i\mathcal F(\mathcal F^{-1}(\mathbf y)*\mathrm{abs}(\mathcal F^{-1}(\mathbf y)))$"
  gives $2i|u|u$, not the $2i|u|^2u$ of (16).
- Eq. (24) defines $\bar\lambda_1=i\rho(\mathbf L)$; §5.1 writes
  "$\bar\lambda_1=\rho(\mathbf L)=(341/4)^2$" without $i$.
- §5.1 vs Eq. (25): the repartitioned parameters are
  $\hat\lambda_1=\lambda_1-\epsilon|\lambda_1|$, $\hat\lambda_2=\lambda_2+\epsilon|\lambda_1|$, but (25)
  prints $R(z_1+\epsilon|z_1|,z_2-\epsilon|z_1|)$, with opposite signs.
- Eq. (32): "$\mathbf E=\mathbf I-\mathbf M_G^{-1}\mathbf M_F^{-1}$"; from (30) the error matrix
  is $\mathbf I-\mathbf M_{\mathcal G}^{-1}\mathbf M_{\mathcal F}$.
- Eqs. (41)–(42) write the pair sets "$\in\mathbb C$" and "$\in\mathbb R$"
  for $\mathbb C^2$, $\mathbb R^2$. Fig. 6 caption writes "$z_2\in[-2h,2h]$"
  where (46) has $r_2$.
- Eq. (44): "$\lambda_1(n)=in^2/16$"; with $\mathbf L=\mathrm{diag}(-i\mathbf k^2)$,
  $\mathbf k=n/4$ the sign is negative. §5.7 item 1 writes
  $\sum_{n=0}^Ma_n(t)\mathbf v_j$ (index $j$ for $n$).
- Remark 1 (App. F) is headed "Stability regions grow approximately
  linearly in $N_g$" but concerns convergence regions. Its conclusion (65)
  "$|r_1|+|R_2|<(C_2N_gN_p)^{-1}$ grows linearly in $N_g$" contradicts
  itself: that bound shrinks with $N_g$, while (64) gives
  $|r_1|+|r_2|<N_g(C_2N_p)^{-1/q}$, which does grow linearly. "$|R_2|$" is
  printed for $|r_2|$.
- Table 4a (KP) lists "$f$ ERK3" and "$g$ ERK4", but §6.1–6.2 say the fine
  integrator is ERK4 and the coarse one ERK3: the entries are swapped.
- Table 4 caption has "$c_2=1$ in (48)"; §6.1 says "$c_2=0$ in (48)".
- §6.1: "256 nodes (8096 compute cores)"; 256 × 32 = 8192.
- §6.1 calls the convergence analysis of §5.7 "the linear stability
  analysis".
- Fig. 13(b) "KP Solution at $t=8$" while $t_{\rm final}=4$; its caption
  cites "region from (60)", the Vlasov–Poisson eigenvalue formula, where
  (59) is meant.
- Eq. (58) prints the KP eigenvalue at $k_x=0$ as $-i(\omega_xk_x)^3$,
  identically zero there.
- §6 text gives the KP line soliton as $2p^2\mathrm{sech}(p(x-4p^2t))$;
  it is $\mathrm{sech}^2$, as the initial data (55) use.
- §6.3 attributes the barely-convergent value $r_1^{\max}(h)=0.0740$ to
  $N_g=1$ and speaks of "$N_g=1$ and $N_g=2$", while Table 4b has
  $N_g\in\{2,3\}$ and 0.074 belongs to $N_g=2$: the labels are off by one.
- App. G (68) integrates over $[0,20\pi]$ in $v$, while $v\in[-8,8]$, and
  indexes its cases by $j$ instead of $k$.
- Typos: "narrrower", "repartioned", "Vlassov-Poisson",
  "Kadomtsev-Petvaishvili", "alogorithm", "convergences exponentially",
  "top column"/"bottom column" (rows) in Figs. 22–23; acknowledgement
  contract "DE-AC02005CH11231" (usually DE-AC02-05CH11231).
- Ref. [70] duplicates ref. [69] (Ruprecht 2017).

# Notation map

| Buvoli & Minion (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf y$, $\mathbf L$ | $y$, $L$ | vectors not bold |
| **$N(t,\mathbf y)$** | $N(t,y)$ (page-local) | nonlinear remainder; **collision with the registry slice count $N$**, kept as on the exponential-integrators page and always written with arguments |
| $\varphi_j$ | $\phi_j$ | the printed definition (9) lacks $1/(j-1)!$; the tableaux use the registry normalization |
| $\varphi_{i,j}$ | $\phi_i(c_jhL)$ | |
| $c_i$, $a_{ij}(h\mathbf L)$, $b_j(h\mathbf L)$, $Y_i$ | $c_i$, $a_{ij}$, $b_j$, $Y_i$ | matrix-function coefficients |
| $h$ | $h$ | fine step, $h=t_{\rm final}/N_s$ |
| $\mathcal G$, $\mathcal F$ | $\mathcal G$, $\mathcal F$ | |
| **$g$**, **$f$** | coarse and fine one-step methods (page-local) | **$f$ is the registry right-hand side**, and also the Vlasov distribution function |
| $N_p$ | $N$ | number of slices and of processors |
| $N_f$, $N_g$, $N_s$ | page-local | fine and coarse steps per slice, total fine steps |
| $y^k_n$ | $U^{(k)}_j$ | |
| $K$ | $K$ | iteration count |
| **$\alpha$** | page-local | cost ratio $C_{\mathcal G}/C_{\mathcal F}$; **collision with Shu–Osher and Rosenbrock $\alpha$** |
| $\hat{\mathbf L}$, $\hat N$, $\mathbf D$, $\epsilon$, **$\rho$** | page-local | repartitioning; $\epsilon=\tan\rho$; **$\rho$ is also the spectral radius $\rho(\cdot)$ in the source** |
| **$\mathbf U$**, $\boldsymbol\Lambda$ | $U_L$, $\Lambda$ | eigenvector and eigenvalue matrices of $L$; **$\mathbf U$ collides with the iterate $U^{(k)}_j$** |
| $\lambda_1$, $\lambda_2$, $z_i=h\lambda_i$, $r_i$ | same | partitioned Dahlquist parameters, $z_i=\mathrm ir_i$ |
| $R(z_1,z_2)$, $R_g$, $R_f$, $R_{\mathcal G}$, $R_{\mathcal F}$ | same | $R_{\mathcal G}=R_g(\delta z_1,\delta z_2)^{N_g}$, $\delta=N_f/N_g$ |
| **$\mathbf M_{\mathcal G}$**, **$\mathbf M_{\mathcal F}$**, **$\mathbf E$**, $\mathbf e^k$ | $\mathcal M_{\mathcal G}$, $\mathcal M_{\mathcal F}$, $\mathcal E$, $e^{(k)}$ | **$M$ is the registry mass matrix** |
| **$S$**, $\hat S$ | $\mathcal S$, $\hat{\mathcal S}$ | stability region and its imaginary slice; **$S$ is also the speedup (5)** |
| $\mathcal C_\infty$, $\hat{\mathcal C}_\infty$, $r_1^{\max}$ | page-local | convergence regions and their width |
| **$q$** | $p$ | order of the coarse integrator; **$q$ is the registry stage order** |
| $k$ | $k$ | iteration index; also a wavenumber in (21) |

# Reference list

The paper prints 79 references in numbered style, without DOIs. All are
merged complete into the [bibliography](/bibliography.md) with `citedby`
buvoli-2024. Eight entries print a ditto dash for repeated authors and
were resolved. Ref. [70] duplicates ref. [69] (Ruprecht 2017); both are
folded into one entry, `ruprecht-2017`, so the 79 printed items give 78
entries. Ref. [17] (Caliari et al.) prints no
volume, [27] is a conference talk, [43] a catalogue with no venue, [62] an
arXiv preprint, [63] a dissertation without institution, [64] an item
without venue. Ref. [79] prints "G. Wanner and E. Hairer"; it is the Hairer &
Wanner monograph and is merged into `hairer-1996`.

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [Evaluating φ-functions: Leja interpolation, Krylov and related methods](/methods/phi-function-evaluation.md)
* [Exponential integrators and φ-functions](/methods/exponential-integrators.md)
* [Korteweg–de Vries equation](/benchmarks/korteweg-de-vries-equation.md)
* [Nonlinear Schrödinger equation](/benchmarks/nonlinear-schrodinger-equation.md)
* [Parallel-in-time integration](/methods/parallel-in-time-integration.md)
* [Parareal](/methods/parareal.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Vlasov–Poisson equation (Landau damping, two-stream instability)](/benchmarks/vlasov-poisson-equation.md)
