---
type: Source
title: "Permyakova & Goldobin (2025) — High-order schemes of exponential time differencing for stiff systems with nondiagonal linear part"
description: "Precomputes the matrix exponential and φ-function matrices of Cox–Matthews ETD Runge–Kutta schemes for a nondiagonal constant linear part by explicit integration of auxiliary linear problems over one step, and reports speedups of 10 to 1000 over explicit schemes on fourth- and sixth-order PDEs."
resource: "doi:10.1016/j.jcp.2024.113493"
source_kind: paper
authors: [Permyakova E.V., Goldobin D.S.]
year: 2025
venue: "J. Comput. Phys. 520:113493"
local_file: "/home/stefano/papers/mosaic/ode-integration/2025_Crossref_Journal_of_Computational_Physics_Permyakova_High-order_schemes_of_exponential_time_differencing_for_stif.pdf"
tags: [exponential, stiff, linear-algebra, explicit]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

The paper deals with the implementation of exponential time differencing
(ETD) [exponential integrators](/methods/exponential-integrators.md) for
semilinear stiff systems $y'=Ly+N(t,y)$ whose constant matrix $L$ is
nondiagonal. Examples are finite differences with variable coefficients,
spatially heterogeneous ("frozen disorder") parameters and non-Fourier
spectral bases. In these cases $e^{hL}$ and the ETD weight matrices have no
closed form. The authors take the three Runge–Kutta-type ETD schemes of Cox
and Matthews (ETD2RK, ETD3RK, ETD4RK) and rewrite them with the matrices
$e^{hL}=\phi_0(hL)$ and $\int_0^he^{(h-t)L}t^{n-1}\,dt=(n-1)!\,h^n\phi_n(hL)$.
They compute these matrices once, before the run, by integrating auxiliary
linear problems numerically. Column $k$ of $e^{hL}$ solves $y'=Ly$ from the
unit vector $e_k$. Column $k$ of the $n$-th integral matrix solves
$y'=Ly+e_kt^{n-1}$ from zero. An explicit Heun predictor–corrector with a
tiny step below its stability limit does the work, but only over one ETD
step. This is a new route for [evaluating φ-functions](/methods/phi-function-evaluation.md).
It avoids the cancellation of closed forms such as $(e^{hL}-I)/(hL)$ and
needs only matrix–vector products.

Tests are a 1-D convective Cahn–Hilliard equation, a 1-D Matthews–Cox
equation (sixth spatial derivative) and a Fourier-space Fokker–Planck chain
for a noisy network of quadratic integrate-and-fire neurons. Against
explicit predictor–corrector and Runge–Kutta–Merson at their stability
limits, the gains are about $10^2$ (Cahn–Hilliard), $10^3$ (Matthews–Cox),
and 3–10 (short runs) to about 100 (long runs) for the Fokker–Planck chain.
The preparation cost grows linearly in $h$. Appendix A computes reference
matrices in high-precision arithmetic. The precomputed matrices are only
accurate to about $10^{-6}$, but the solutions are much more accurate,
because the inaccurate entries belong to fast-decaying modes. The paper
states classical error terms for ETD3RK and ETD4RK and does not discuss the
[stiff order conditions](/results/exponential-runge-kutta-stiff-order-conditions.md),
which ETD4RK satisfies only in weakened form.

# Version read

arXiv:2208.14292v2 [math.NA], 13 October 2024, Elsevier preprint template,
footer "Preprint submitted to Journal of Computational Physics, October 15,
2024", 22 PDF pages (a highlights page and 21 numbered pages), all read. It
carries JCP highlights and CRediT and data statements, so it is very likely
the accepted manuscript, not the version of record (J. Comput. Phys.
520:113493). Title and authors match the published version. The file prints
no DOI. The basic idea was published earlier by the same authors in J.
Appl. Mech. Tech. Phys. 61 (2020) (ref. [46]); this paper extends it to the
third- and fourth-order schemes. Equation, figure and table numbers on this
page are those of arXiv v2.

# Key claims

Registry notation: $y$ is the state (source $\mathbf u$), $L$ the constant
linear part (source $\mathbf L$), $h$ the ETD step (source $\tau$), $d$ the
dimension (source $N$), and $\phi_k$ the registry φ-functions. The
nonlinear part $N(t,y)$ (source $\mathbf f(\mathbf u,t)$) is page-local, as
on the exponential-integrator pages. The source matrices translate as
$\mathbf Q(\tau)=\phi_0(hL)=e^{hL}$ and
$\mathbf M_n(\tau)=(n-1)!\,h^n\phi_n(hL)$; the step of the auxiliary
integrator is $h_{\mathrm{aux}}$ (source $\tau_1$), and the Taylor length of App. A is
$\mathsf m$ (source $M$), both page-local as on
[φ-function evaluation](/methods/phi-function-evaluation.md).

1. ETD methods solve the linear part exactly; an $n$-th order ETD scheme is
   exact when the nonlinear part is a polynomial of degree $n-1$ in time
   over a step (§1, citing Cox–Matthews [31]). **Stated**
2. The one-step errors of ETD2RK, ETD3RK and ETD4RK (Eqs. (2)–(4)) are
   $-h^3\ddot N/12$ (from [31]), $\propto h^4\,d^3N/dt^3$ and
   $\propto h^5\,d^4N/dt^4$ (§2, after Eq. (4d)). **Stated** (no stiff-order
   analysis)
3. Expressions with $L^{-n}$ are shorthands for power series starting at
   $L^m$, $m\ge n$, so zero eigenvalues of $L$ (conservation laws,
   bifurcation points) do no harm (§2; App. A after (A.2)). **Derived**
4. $e^{hL}$ and $(n-1)!\,h^n\phi_n(hL)$ are the solution operators of the
   auxiliary problems (5) and (7), which gives column-by-column definitions
   (6) and (8) suited to numerical computation (§2, Eqs. (5)–(8)).
   **Derived**
5. The recurrence $\mathbf M_{n+1}=L^{-1}(-h^nI+n\mathbf M_n)$ gives the
   closed forms (9a)–(9c), i.e. $h\phi_1(hL)$, $h^2\phi_2(hL)$ and
   $2h^3\phi_3(hL)$ (§2). **Derived** (checked by integration by parts *(compiler
   check, not in the sources)*)
6. In this form ETD2RK (10) needs $\phi_0,\phi_1,\phi_2$ at $hL$; ETD3RK (11)
   and ETD4RK (12) need in addition $\phi_0$ and $\phi_1$ at $\frac h2L$ and
   $\phi_3(hL)$. The final weights are $h(\phi_1-3\phi_2+4\phi_3)$ on the
   first stage, $h(4\phi_2-8\phi_3)$ on the midpoint stage of ETD3RK (split
   as $h(2\phi_2-4\phi_3)$ on each of the two midpoint stages of ETD4RK),
   and $h(4\phi_3-\phi_2)$ on the last stage (§2). **Derived** ((11c) and (12d) reproduce
   (3c) and (4d) *(compiler check, not in the sources)*)
7. The literature computes these matrices by Taylor or Krylov projection
   [38, 39] or contour integrals [40]. Closed forms suffer cancellation for
   small eigenvalues of $hL$, worse as $n$ grows; the auxiliary-problem
   algorithm does not (§2). **Stated** (no head-to-head comparison)
8. For the discrete Cahn–Hilliard equation (fourth derivative) explicit
   Euler and predictor–corrector are unstable unless $h_{\mathrm{aux}}<\Delta x^4/8$; for
   the Matthews–Cox equation (sixth derivative) unless $h_{\mathrm{aux}}<\Delta x^6/32$
   (§3.1.1, §3.2.1). **Stated** (consistent with
   $\lambda_{\mathrm{fast}}\approx-16/\Delta x^4$ and $-64/\Delta x^6$ of
   App. A)
9. The auxiliary problems are integrated by predictor–corrector (16) with
   $h_{\mathrm{aux}}=0.1\Delta x^4$ (Cahn–Hilliard) and $h_{\mathrm{aux}}=0.02\Delta x^6$
   (Matthews–Cox); reference solutions use $h_{\mathrm{aux}}=0.01\Delta x^4$ (§3.1.1–3.1.2,
   §3.2.1). **Shown**
10. Cahn–Hilliard ($d=200$, $\Delta x=0.05$, $0<t<50$): for an error rate
    of $10^{-6}$ one can take $h\approx0.005$ (ETD2RK), $0.02$ (ETD3RK) and
    $0.04$ (ETD4RK). The gain over predictor–corrector exceeds a factor 100
    for all three, and is largest for ETD4RK (§3.1.2, Fig. 3). **Shown**
11. Doubling the spatial resolution ($d=400$) increases the ETD gain
    considerably (§3.1.2, Fig. 4). **Shown**
12. The preparation time grows linearly in $h$. For short and moderate runs
    the optimal $h$ balances preparation and run time, and ETD2RK is then
    the most efficient. For long runs (spatio-temporal chaos, frozen
    disorder) the preparation cost is negligible (§3.1.2, Figs. 3–4).
    **Shown**
13. The error of the precomputed matrices is dominated by fast-decaying
    modes, whose influence on $y(t)$ is exponentially suppressed; the net
    error is what matters (§3.1.2, App. A). **Shown** (Figs. 10–11 against
    Figs. 3–8)
14. Matthews–Cox: "even more dramatic performance gain than for CHE",
    about three orders of magnitude (§3.2.2, Figs. 6–7, §4). **Shown**
15. For PDEs whose highest spatial derivative has order $m$ the gain is
    $\propto\Delta x^{m-2}$, "as anticipated in [46]" (§3.2.2, §4).
    **Stated** (scaling argument, not derived here)
16. Entries of the matrices decay fast away from the diagonal; for moderate
    $h$ a large fraction is below about $10^{-16}$ and can be zeroed, giving
    a further but smaller speedup that shrinks as $m$ grows (§3.2.2, Figs.
    2, 5). **Shown** (qualitatively; no timings for the sparse version)
17. Fokker–Planck chain (25): the explicit stability threshold is estimated
    from $\{2j\sqrt{(1+A_\eta)^2+\gamma^2}+4j^2\sigma^2\}h_*\sim1$; for $j\sim1000$,
    $h_*\sim10^{-7}/(\sigma^2+0.0005\sqrt{(1+A_\eta)^2+\gamma^2})$ for both
    explicit baselines (§3.3.2). **Derived**
18. For this chain $L$ cannot practically be diagonalized; the matrices are
    computed with Runge–Kutta–Merson or predictor–corrector. Fig. 8
    ($d=200$, $h=0.025$, $h_{\mathrm{aux}}=1.25\times10^{-6}$) shows errors decreasing
    with ETD order (§3.3.2). **Shown**
19. Table 1 ($t\in[0,5]$, averages over 100 runs): Runge–Kutta–Merson at its
    largest stable step ($2.3\times10^{-6}$, $10^{-6}$,
    $0.5\times10^{-6}$ for $d=200,300,400$) takes 16.1, 53.0 and 139 s;
    predictor–corrector ($1.2\times10^{-6}$, $5.5\times10^{-7}$,
    $3.1\times10^{-7}$) takes 13.8, 49.9 and 106 s with relative errors
    $6.1\times10^{-11}$, $1.4\times10^{-11}$, $4.9\times10^{-10}$. For
    $d=200$: ETD4RK at $h=0.0005$ costs 1.25 s preparation and 2.59 s run
    (error $5.6\times10^{-11}$), at $h=0.005$ 12.5 s and 0.397 s
    ($4.2\times10^{-10}$); ETD2RK at $h=0.0005$ 0.752 s and 0.936 s
    ($5.1\times10^{-8}$), at $h=0.005$ 7.51 s and 0.149 s
    ($5.0\times10^{-6}$); ETD3RK at $h=0.0005$ 1.25 s and 2.12 s
    ($1.1\times10^{-10}$), at $h=0.005$ 12.5 s and 0.345 s
    ($1.0\times10^{-7}$). **Shown**
20. Short runs: optimal $h\approx0.0005$, gain 3–10; long runs: $h=0.005$,
    gain up to two orders of magnitude (§3.3.2). **Shown**
21. For long runs ETD4RK gives the largest gain; for short runs ETD2RK is
    somewhat more efficient (§4). **Shown**
22. Extension to several dimensions is "straightforward" [46] but memory
    demanding: $d=N_xN_y$ gives $d\times d$ matrices; with sparsity one
    stores $d\times N_{\mathrm{spr}}$ (formula in §4). **Stated** (formula
    without derivation, dimensionally doubtful *(compiler check, not in the sources)*)
23. The bulk of the work is large matrix–vector products, "naturally
    suitable for parallel- and super-computing" (§4). **Stated**
24. The Horner-type recursion $Q_{m-1}=I+\frac hm LQ_m$ (page-local $Q_m$),
    $Q_{\mathsf m}=I$, run from $m=\mathsf m$ down to 1, gives $e^{hL}=Q_0$
    and $(n-1)!\,h^n\phi_n(hL)=\frac{h^n}nQ_n$, i.e. $\phi_n(hL)=Q_n/n!$, with the slowest accumulation
    of cancellation error (App. A, Eqs. (A.5)–(A.6)). **Derived**
25. The minimal Taylor length that avoids explosion of the fastest mode is
    $\mathsf m_*=e|\lambda_{\mathrm{fast}}|h$ (A.7, from Stirling): 1740
    (Cahn–Hilliard at $h=2.5\times10^{-4}$, $d=200$), 870 (Matthews–Cox),
    435 (Fokker–Planck) (App. A). **Derived**
26. "Exact" reference matrices need 384, 192 and 96 decimal digits (Taylor
    lengths 2088, 1044, 522) to trust 20 digits. The predictor–corrector
    matrices have relative errors somewhat below $10^{-6}$ (Cahn–Hilliard),
    at most about $10^{-6}$ (Matthews–Cox) and somewhat below $10^{-5}$
    (Fokker–Planck) (App. A, Figs. 10–11). **Shown**
27. A predictor–corrector step of about $10^{-7}$ gives the best
    double-precision reference for the Fokker–Planck chain, with a net
    error rate per unit time "well below $10^{-12}$" (§3.3.2, footnote 1).
    **Stated**

# Printed slips

- Eq. (7): "$\dot{\mathbf u}=\mathbf L\cdot\mathbf u+\mathbf g\,t^n$"; the
  definition that follows and Eq. (8) use $t^{n-1}$, which is correct.
- Eq. (A.2): the general term
  "$\frac{\tau^{n+m}\mathbf L^{n+m}}{n(n+1)\dots(n+m)}$" should carry
  $\mathbf L^m$, by the preceding terms.
- Eq. (16c): "$\mathbf F(t+\tau_1)=\mathbf L\cdot\mathbf a+\mathbf f(\mathbf a,t)$";
  the time argument should be $t+\tau_1$ (it matters for the
  Fokker–Planck case with input $I(t)$).
- Fig. 6 caption: "$N=50$ (i.e. $h_x=0.2$); $\tau_1=0.02h_x^6=1.6\times10^{-7}$",
  but $0.02\times0.2^6=1.28\times10^{-6}$.
- Figs. 8–9 use $\tau_1=1.25\times10^{-6}$ for the Fokker–Planck chain,
  above the predictor–corrector stability limit $1.2\times10^{-6}$ of
  Table 1 for $N=200$; the text does not say whether Runge–Kutta–Merson
  was used instead.
- §2 calls ETD2RK, ETD3RK, ETD4RK "two-step", "three-step", "four-step"
  schemes; they are one-step schemes with 2, 3, 4 stages.
- Typos: "three EDT schemes" (§3.3.2), "disabled hypertrading" (Fig. 3
  caption), "forth-order" (§3.1.1).
- Ref. [14] (Shtilman & Sivashinsky, Physica D 52) prints the year 1958,
  while its DOI 10.1016/0167-2789(91)90140-5 indicates 1991. Ref. [62]
  prints the DOI with a stray "h". The titles of refs. [28], [48] and [52]
  run off the page margin and are truncated in the PDF itself.

# Notation map

| Permyakova & Goldobin (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf u(t)$ | $y(t)$ | state vector |
| $\mathbf L$ | $L$ | constant, nondiagonal linear part |
| $\mathbf f(\mathbf u,t)$ | $N(t,y)$ | nonlinear part, page-local $N$ as on the exponential-integrator pages; **source $\mathbf f$ is not the full right-hand side $f$** |
| $\dot{\mathbf u}=\mathbf L\cdot\mathbf u+\mathbf f$ | $y'=Ly+N(t,y)$ | |
| $\tau$ | $h$ | ETD step |
| $\tau_1$, $\tau_*$ | $h_{\mathrm{aux}}$, $h_*$ (page-local) | step of the auxiliary or baseline explicit integrator; explicit stability threshold |
| $\mathbf Q(\tau)$, $\mathbf Q_{\tau/2}$ | $\phi_0(hL)=e^{hL}$, $\phi_0(\frac h2L)$ | |
| $\mathbf M_n(\tau)=\int_0^\tau e^{\mathbf L(\tau-t)}t^{n-1}dt$ | $(n-1)!\,h^n\phi_n(hL)$ | **not normalized like $\phi_n$**: $\mathbf M_1=h\phi_1$, $\mathbf M_2=h^2\phi_2$, $\mathbf M_3=2h^3\phi_3$ |
| $\mathbf M_{1,\tau/2}$ | $\frac h2\phi_1(\frac h2L)$ | |
| $\mathbf L^{-1}(e^{\mathbf L\tau}-\mathbf I)$, $\mathbf L^{-2}(e^{\mathbf L\tau}-\mathbf I-\mathbf L\tau)$ | $h\phi_1(hL)$, $h^2\phi_2(hL)$ | closed forms of Cox–Matthews |
| $\mathbf a,\mathbf b,\mathbf c$ | — | stage values (at $t+\tau/2$ or $t+\tau$, per scheme) |
| $N$ | $d$ | number of nodes or modes; **source $N$ collides with the page-local nonlinearity $N$** |
| $h_x$ | $\Delta x$ | grid spacing; **source $h_x$ is not the step $h$** |
| $\lambda_j$, $\mathbf y_j$, $\mathbf v_j$; $\lambda_{\mathrm{fast}}$ | $\lambda$; — | eigenvalues, right and left eigenvectors of $L$; fastest mode |
| **$M$, $M_*$** | $\mathsf m$, $\mathsf m_*$ (page-local) | Taylor truncation length and its minimum; **collide with the mass matrix $M$ and with $\mathbf M_n$** |
| $m$ | — | order of the highest spatial derivative |
| $\mathbf F(t)$ | $f(t,y)$ | full right-hand side in the predictor–corrector scheme (16) |
| $\varepsilon$ | — | relative error of Table 1; **collides with the stiffness parameter $\varepsilon$** |
| $\gamma$, $\sigma$, $\eta$, $J$ | — | Lorentzian width, noise amplitude, excitability, coupling of the neuron model; **collide with registry $\gamma$, $\sigma$, $\eta$ and the Jacobian $J$** |
| "$n$-step scheme" | $s$-stage one-step method | not a multistep method |
| "strong" / "soft" accuracy | — | accuracy of the precomputed matrices / of the solution (paper-specific) |

# Reference list

The paper prints 63 references in numbered style. All are merged complete
into the [bibliography](/bibliography.md) with `citedby` permyakova-2025.
Refs. [28], [48] and [52] have titles truncated at the page margin in the
PDF, recorded as printed with a note. Ref. [14] is recorded with its
printed year 1958 (key `shtilman-1958`), with a note that its DOI indicates
1991. Ref. [30] is an arXiv preprint (arXiv:2311.06159); ref. [32] is an
NTNU technical report with URL; refs. [3], [57] and [60] are books; ref.
[59] prints a URL and no DOI.

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [Cahn–Hilliard equation](/benchmarks/cahn-hilliard-equation.md)
* [Evaluating φ-functions: Leja interpolation, Krylov and related methods](/methods/phi-function-evaluation.md)
* [Exponential integrators and φ-functions](/methods/exponential-integrators.md)
* [Stiff order conditions of exponential Runge–Kutta methods and φ-order conditions](/results/exponential-runge-kutta-stiff-order-conditions.md)
