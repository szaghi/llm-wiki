---
type: Method
title: "Evaluating φ-functions: Leja interpolation, Krylov and related methods"
description: "An exponential integrator spends its time on actions of φ-functions on vectors; the page compares Krylov projection (phipm, KIOPS, EPIC), polynomial interpolation at Leja points, structure-exploiting evaluation (FFT, μ-mode, diagonal operators) and dense precomputation by auxiliary time integration, with the cost models, tolerances and measured speed-ups the sources report."
status: established
aliases: [matrix-function action, φ-function action, phi-function evaluation, Leja interpolation, Leja method, Krylov exponential, KIOPS, phipm, phipm_simul_iom, EPIC, Chebyshev approximation, Arnoldi approximation, contour integral, Expokit, EXPINT, μ-mode integrator, auxiliary-problem integration, precomputed ETD matrices, Horner Taylor recursion]
tags: [exponential, linear-algebra, stiff, software]
timestamp: 2026-10-29T18:00:00Z
---

# Evaluating φ-functions: Leja interpolation, Krylov and related methods

Every step of an [exponential integrator](/methods/exponential-integrators.md) needs
linear combinations

$$\sum_{k=0}^{q}\phi_k(\rho\,hL)\,\rho^k v_k$$

of [φ-functions](/methods/exponential-integrators.md) of a large sparse matrix $hL$ (or
$hJ_n$) applied to vectors $v_k$, often for several scalings $0<\rho\le1$ ($q$, $\rho$,
$v_k$ page-local). For large problems the matrix functions are never formed. Their action is approximated by
projection onto a Krylov space, by polynomial interpolation, or, for structured $L$,
exactly in a transformed basis. The cost of these actions dominates the cost of the
integrator. The sources therefore measure the cost of a method by the number of
evaluations, or sequential evaluations, of such combinations rather than by stages
([Luan 2021](/sources/luan-2021.md), §2.1;
[Deka & Einkemmer 2022](/sources/deka-2022.md), §5.3).

## Krylov projection

**One call per combination.** The routine `phipm_simul_iom` of Luan, Pudykiewicz &
Reynolds (2019) takes scalings $\rho_1<\dots<\rho_r\le1$, a matrix $B$ and vectors
$v_0,\dots,v_q$. It returns all $r$ combinations
$\sum_k\phi_k(\rho_iB)\rho_i^kv_k$ in one call, combining Krylov projection, incomplete
orthogonalization and adaptive substepping, after Niesen–Wright's `phipm`
(Luan 2021, §2.1, §5, Eq. 5.2; page-local $B$, $r$; $M$ is kept for the mass matrix). Two kinds of stages can share a call:
those that use the same vectors $v_k$ and differ only in their node, and those that are
mutually independent. Luan builds exponential Runge–Kutta methods on this structure. His
expRK4s6 and expRK5s10 cost 4 and 5 calls per step, against 6 and 11 for the older
expRK4s5 and expRK5s8 (§5; see
[exponential integrators](/methods/exponential-integrators.md)). His settings are a
tolerance of $10^{-12}$, an initial Krylov dimension of 1 and an orthogonalization length
of 2 (§6). Luan notes that algorithms that do not build Krylov spaces may not support such
simultaneous evaluation, although they can still compute independent stages in parallel
(§1).

**Single projection per step.** [Dallerit & Tokman (2025)](/sources/dallerit-2025.md)
(§5.3) design their φ-order methods so that the whole update is one combination
$h\phi_1(hJ_n)f(y_n)+\sum_{k=3}^p\phi_k(hJ_n)v_k$, evaluated with one call of the adaptive
Krylov code KIOPS (Gaudreault, Rainwater & Tokman). An adaptive step with an embedded
estimate needs two calls (§5.4). The same adaptive substepping returns the solution at
intermediate fractions of the step at little extra cost, which supplies
[dense output](/methods/dense-output.md) and the past values of their multivalue methods
(§5.5, §6.3).

**Cost growth.** In the experiments of Deka & Einkemmer (2022, §4.2) the Krylov basis grows
with the step, and the cost grows quadratically in its size. With the traditional
step-size controller, Krylov runs of EXPRB43 converged only for tolerances $10^{-5}$ and
$10^{-6}$ in one test case, and the cost-based controller rescued the runs at lenient
tolerances (see [step-size control](/methods/step-size-control.md)). [Caliari et al.
(2024)](/sources/caliari-2024.md) (§5) run kiops at tolerance $h^{p+1}/100$, with $p$ the
order of the integrator. Deka & Einkemmer use the Krylov-based EPIC library (Tokman 2014).

**Krylov-friendly method design.** EPIRK methods are built so that one Krylov basis can be
reused, and so that higher-index $\phi_k$, whose Krylov approximations converge faster,
appear in the later stages. Those design conditions are redundant for interpolation
methods (Deka & Einkemmer 2022, §5.3, after Tokman & Loffeld 2010). The same concern shapes
the reformulation of exponential Rosenbrock methods by
[Hochbruck & Ostermann (2010)](/sources/hochbruck-2010.md) (§2.4, Eq. (2.48)): every stage is
a perturbed exponential Rosenbrock–Euler step whose corrections $D_j$ are small in norm, so
"only one computationally expensive Krylov approximation will be required in each time
step, namely that involving" $f(y_n)$, and in their
exponential Adams methods the backward differences $\nabla^jG_n=\mathcal O(h^j)$ make the
higher-order terms cheap to approximate (§2.5; see
[exponential integrators](/methods/exponential-integrators.md)).

## Polynomial interpolation at Leja points

Interpolation methods approximate $\phi_k(hJ_n)v$ by $p_m(hJ_n)v$, with $p_m$ a polynomial
interpolating $\phi_k$ at Leja points of a set containing the spectrum (the Leja method of
Caliari, Bergamaschi and co-workers, 2004–2014, as recalled by Deka & Einkemmer 2022, §2.3). Given $\xi_0$, the Leja points are defined
recursively by

$$\xi_m\in\arg\max_{\xi\in K}\prod_{j=0}^{m-1}\lvert\xi-\xi_j\rvert,$$

with $K=[-2,2]$ (page-local $\xi_m$, $K$). The interpolant is built in Newton form
$p_m=p_{m-1}+d_m\pi_{m-1}$, where $\pi_m$ is the nodal product and $d_m$ are divided
differences (page-local). Each new point therefore costs one more matrix–vector product,
whereas Chebyshev interpolation would need re-evaluation at all nodes. The spectrum is
mapped onto $K$ by a shift of $\Lambda/2$ and a scale of $\Lambda/4$, where $\Lambda$
(page-local) estimates the extreme eigenvalue of the Jacobian. Hochbruck & Ostermann (2010,
§4.3) describe the same construction (reference Leja points on $[-2,2]$ with $\xi_0=2$, the
Newton form as a two-term recurrence, Eq. (4.6)), credit it to Caliari, Vianello &
Bergamaschi (2004) and, for $\phi_k$ with $k>1$, to Caliari (2007), recall superlinear
convergence on confocal ellipses and sub-stepping (Caliari & Ostermann 2009), and note that
the method needs a priori information on the field of values, for instance from Gerschgorin
discs.

**Matrix-free variant** (Deka & Einkemmer 2022, contribution, §2.3, §3.1, §4.2.1). Jacobian–vector
products are forward finite differences of the right-hand side. $\Lambda$ comes from power
iterations with a safety factor and is recomputed only every 50 steps. The authors call
this "to the best of our knowledge" the first matrix-free Leja-based exponential
integrator (§1). Refreshing the estimate every 50 steps rather than every step changes the
total runtime as follows (KHI case III, EXPRB43, cost-based controller; Table 3):

| tolerance | every 50 steps: total / power iteration (s) | every step: total / power iteration (s) |
|---|---|---|
| $10^{-3}$ | 110 / 2 | 165 / 63 |
| $10^{-4}$ | 115 / 2 | 196 / 77 |
| $10^{-5}$ | 98 / 3 | 211 / 108 |
| $10^{-6}$ | 151 / 4 | 320 / 167 |
| $10^{-7}$ | 426 / 19 | 1294 / 887 |

At $10^{-4}$ the estimate costs about 1.7% of the runtime against 39%.

**Limits.** The interpolation converges only if the step and the norm of the interpolated
function are not too large. Otherwise the step is rejected and retried with the smaller
step of the traditional controller. Deka & Einkemmer cap the number of Leja points at 500,
and for EPIRK5P1 on the reconnection problem the cap is reached at large steps (§2.3, §5.2).
Leja interpolation needs only matrix–vector products and no inner products, which the
authors expect to favour GPUs (§1, §6).

## Leja versus Krylov: measured comparisons

Deka & Einkemmer (2022) compare the two on resistive MHD with wall-clock time; the
hardware is not stated:

- **Kelvin–Helmholtz instability, EXPRB43** (§4.2): Leja is faster by about 2.5 (against
  tolerance) and 1.65 (against error) in the diffusion-dominated case I, by about 3 in case II,
  and in the low-diffusion cases III–IV by about 1.8–2.3 (error) and 6–8 (tolerance), there
  for lenient and intermediate tolerances. Krylov's error and cost are "somewhat
  unpredictable" in cases I–II. See [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md).
- **Magnetic reconnection** (§5.2): with EXPRB43, Leja is faster by up to 87% (tolerance) and
  50% (error) in case V, and by factors up to 6.4 and 4.3 in case VI. With the Krylov-friendly
  EPIRK5P1, Krylov beats Leja. That scheme has different coefficients for its internal
  stages, its solution and its error estimate, so none of its φ-evaluations can be reused
  (§5.3).

The ranking is therefore scheme-dependent. The introduction's "up to a factor of three"
understates the body's factors of 6, 8 and 6.4 (§1 versus §4.2, §5.2).

## Error bounds and further approaches (Hochbruck & Ostermann 2010, §4)

Hochbruck & Ostermann's survey recalls the convergence theory behind the polynomial and Krylov
approaches; the bounds below are for $e^{hL}v$, with $\varrho$ the half-width or length of the
spectral interval and $m$ the number of terms or Krylov steps (page-local $\varrho$, $m$).

- **Chebyshev series** (§4.1). Truncated Chebyshev expansions, evaluated by the Clenshaw
  algorithm, need the spectrum in advance. For $-L$ Hermitian positive semidefinite with
  spectrum in $[0,\varrho]$ the error after $m\le h\varrho$ terms is at most
  $2e^{-\beta m^2/(h\varrho)}\big(1+\sqrt{h\varrho\pi/(4\beta)}\big)+2\delta^{h\varrho}/(1-\delta)$
  with $\beta=2/(1+\sqrt5)\approx0.618$, $\delta=e^\beta/(2+\sqrt5)\approx0.438$ (Thm. 4.1, after
  Stewart & Leyk 1996; page-local $\beta$, $\delta$), a bound they call not optimal (Remark
  4.2); a skew-Hermitian bound is Thm. 4.3 (after Lubich 2008). General matrices need Faber
  series.
- **Krylov (Arnoldi) approximation** (§4.2). With the Arnoldi basis $V_m$ and Hessenberg matrix
  $\mathsf H_m$ of $hL$ and $v$ (page-local), $\phi(hL)v\approx V_m\phi(\mathsf H_m)e_1$ as printed (Eq. (4.5)),
  which they derive as a Galerkin approximation of the Cauchy-integral representation
  (Eqs. (4.2)–(4.5)); the small $\phi(\mathsf H_m)e_1$ is computed by diagonalization, Padé or
  contour methods. "A remarkable property is that the convergence is always superlinear", but
  its onset depends on the field of values: for $-L$ Hermitian positive semidefinite with
  spectrum in $[0,\varrho]$ the superlinear regime starts at $m\ge\sqrt{\varrho h}$
  (Thm. 4.4, after Hochbruck & Lubich 1997), for skew-Hermitian $L$ with spectrum in an
  interval of half-length $\varrho$ only at $m\ge\varrho h$ (Thm. 4.5, with bound
  $8e^{-(\varrho h)^2/(4m)}(e\varrho h/(2m))^m$), and for a field of values in a wedge of
  half-angle $\theta$ at $m\ge(h\lVert L\rVert)^{\pi/(2(\pi-\theta))}$ (page-local $\theta$).
  Restarted variants exist (Eiermann & Ernst 2006; Niehoff 2007).
- **Contour integrals and rational methods** (§4.4). "A major disadvantage of polynomial
  approximations is that the required degree of the polynomials grows with the norm of $A$";
  when shifted systems $(zI-hL)$ are cheap to solve, rational approximations are the
  alternative. The best rational approximation of the exponential on the negative real line
  "converges geometrically with rate $1/9.28903\ldots$" (as recalled from Schmelzer & Trefethen
  2007). They list rational and extended Krylov methods and the Laplace-inversion method of
  López-Fernández, Palencia & Schädle (2006), a trapezoidal rule on a hyperbolic contour with an
  error bound decaying exponentially in the number of nodes (Thm. 4.6); for $\phi_k$ it needs one
  linear solve with $zI-hL$ per node (López-Fernández 2009).
- **Software in 2010** (§4.5): exp4 (Hochbruck, Lubich & Selhofer 1998; variable step,
  MATLAB and C, dense or Krylov), EXPINT (Berland, Skaflestad & Wright; MATLAB, constant step,
  φ-functions by extended scaling and squaring), Expokit (Sidje 1998; MATLAB and Fortran,
  Krylov), the SPARSKIT routines EXPPRO and PHIPRO (Saad), and phipm (Niesen & Wright; MATLAB,
  Krylov). "Most of the mathematical software for exponential integrators is still in its
  infancy."

## Exploiting structure: FFT and μ-mode products

When the linear part has constant coefficients, its φ-functions can be evaluated exactly at
low cost. Caliari et al. (2024, §3, §5) choose $L$ that way, moving the variable-coefficient
remainder into the explicit part (see [Lawson methods](/methods/lawson-methods.md)):

- **Periodic domains.** The matrix functions are diagonal in Fourier space and cost a few FFTs
  per step: 7 per step for their first-order and 13 for their second-order schemes in 2D.
  The wall-clock time then barely depends on the integrator (§5.1, Fig. 6).
- **Kronecker sums.** If $L=L_d\oplus\dots\oplus L_1$ (finite differences on a box), then
  $e^{L}v=\mathrm{vec}\big(V\times_1e^{L_1}\times_2\cdots\times_de^{L_d}\big)$ with
  $v=\mathrm{vec}(V)$. This needs only small one-dimensional exponentials and $d$ level-3
  BLAS calls ($\times_\mu$ the μ-mode tensor–matrix product and $d$ the number of space
  dimensions, page-local; §5.2, after the
  authors' earlier μ-mode integrator). It applies to the exponential, which is why it
  pairs with Lawson schemes. The authors note that Kronecker structure is easier to exploit
  for exponentials than for linear solves, and that a good preconditioner gives a fast linear
  solver but not fast matrix functions (§1).

**Diagonal operators.** When $L$ is diagonal, as in Fourier-space semi-discretizations of
periodic problems, the φ-functions act elementwise and their evaluation is trivial;
[Buvoli & Minion (2024)](/sources/buvoli-2024.md) use only such operators and cite scaling and
squaring, contour integrals, Krylov methods and parallel rational approximations for the general
case without using them (§3.1, §7).

## Precomputing dense matrix functions by auxiliary time integration

For a constant **nondiagonal** $L$ of moderate size, [Permyakova & Goldobin (2025)](/sources/permyakova-2025.md)
(§2, Eqs. 5–8, contribution, extending their 2020 paper) form the matrices themselves, once,
before the run. Column $j$ of $e^{hL}$ is the solution at time $h$ of $y'=Ly$, $y(0)=e_j$;
column $j$ of $(k-1)!\,h^k\phi_k(hL)=\int_0^he^{(h-s)L}s^{k-1}\,ds$ is the solution at time
$h$ of $y'=Ly+e_j\,s^{k-1}$, $y(0)=0$ ($e_j$ the unit vector, $s$ the time, page-local). These
auxiliary problems are integrated over one step with an explicit low-order scheme at a tiny step
$h_{\mathrm{aux}}$ (page-local) below its stability limit: Heun's predictor–corrector with
$h_{\mathrm{aux}}=0.1\Delta x^4$ for a fourth-order and $0.02\Delta x^6$ for a sixth-order
spatial operator, whose explicit limits are $\Delta x^4/8$ and $\Delta x^6/32$ (§3.1.1, §3.2.1);
"Runge–Kutta–Merson or simplest predictor-corrector" for their Fokker–Planck chain. The
half-step matrices come from the same integration at $t=h/2$. The integration evolves the
whole $N\times N$ matrix, needs only matrix–vector products, and costs a time proportional to
$h/h_{\mathrm{aux}}$, i.e. linear in $h$ (page-local $N$, the number of unknowns). It avoids the
cancellation of the closed forms such as $(e^{hL}-I)(hL)^{-1}$ for small eigenvalues, which
grows with $k$ (§2). The authors contrast the route with Taylor and Krylov projection
(Hochbruck–Lubich–Selhofer, Tokman's EPI) and with contour integrals (Kassam–Trefethen), as
recalled, but give no head-to-head comparison.

**Strong and soft accuracy.** To check the matrices they compute "exact" ones in
high-precision arithmetic (Maple, up to 384 digits) by the Horner-type recursion

$$Q_{\mathsf m}=I,\qquad Q_{m-1}=I+\frac hm\,L\,Q_m\quad(m=\mathsf m,\dots,1),\qquad
e^{hL}=Q_0,\qquad \phi_k(hL)=\frac{Q_k}{k!}$$

(App. A, Eqs. A.5–A.6; page-local $Q_m$ and truncation length $\mathsf m$; the source writes
$\mathbf M_n=\frac{\tau^n}{n}\mathbf Q_n$, translated with the convention above *(compiler
check, not in the source)*). The truncation must exceed $e\lvert\lambda_{\mathrm{fast}}\rvert h$ (from Stirling's
formula; $\lambda_{\mathrm{fast}}$ the fastest eigenvalue of $L$) so that the fastest mode does
not explode, and $1.2$ times that length is used (Eq. A.7). Against these, the
time-integrated matrices are accurate only to about $10^{-6}$ ("strong" accuracy), yet the
solutions are far more accurate ("soft" accuracy), because the inaccurate entries belong to fast,
strongly damped modes whose influence on the solution is exponentially suppressed (§3.1.2,
App. A, Figs. 10–11). The matrices are dense in principle, but their entries decay rapidly away
from the diagonal; entries below about $10^{-16}$ can be dropped for a further, unquantified,
speedup (§3.2.2, Figs. 2, 5). The application results are on
[exponential integrators](/methods/exponential-integrators.md).

Other routes cited without use are the Taylor method of Al-Mohy–Higham and its
augmented-matrix evaluation of linear combinations. Deka & Einkemmer propose the latter as
future work (§5.3); Caliari et al. (2024, §1) list rational Krylov and others.

## Qualifications

- All the speed-ups above are serial runtimes on unspecified (Deka & Einkemmer 2022) or
  single-workstation (Caliari et al. 2024, MATLAB on an Intel i7-10750H; Luan 2021, MATLAB on
  an iMac) hardware. Luan's evaluation counts assume simultaneous evaluation in
  `phipm_simul_iom`; with other algorithms the saving needs parallel hardware, and no parallel
  runs are reported.
- Deka & Einkemmer's Krylov comparisons exclude runs that "fail to converge within a
  reasonable amount of time" (§4.2).
- Permyakova & Goldobin's preparation is affordable only while dense $N\times N$ matrices fit
  in memory; they call the multidimensional extension memory-demanding and give a
  sparsified storage estimate without derivation (§4). Their speedups are against explicit
  schemes at the stability limit, not against Krylov or Leja evaluation.
- Printed slips in Permyakova & Goldobin (2025), arXiv v2: the auxiliary problem (Eq. 7) is
  printed with forcing $g\,t^n$ where the definition and Eq. 8 use $t^{n-1}$; the general term
  of the series (Eq. A.2) carries $L^{n+m}$ for $L^m$; the Fig. 6 caption gives
  $h_{\mathrm{aux}}=0.02\Delta x^6=1.6\times10^{-7}$ at $\Delta x=0.2$, where the product is
  $1.28\times10^{-6}$; and the auxiliary step $1.25\times10^{-6}$ of the Fokker–Planck runs
  exceeds the maximal stable predictor–corrector step $1.2\times10^{-6}$ of their Table 1, while
  the text does not say which of the two integrators was used.
- Hochbruck & Ostermann (2010, p. 268) write that the wedge case $\theta=0$ corresponds to
  Theorem 4.4 "while Theorem 4.4 treats the case $\theta=\pi/2$"; the onset exponent
  $\pi/(2(\pi-\theta))$ equals $\tfrac12$ at $\theta=0$ and $1$ at $\theta=\pi/2$, the onsets
  of their Theorems 4.4 and 4.5 respectively, so the second reference is read as Theorem 4.5
  *(compiler check, not in the sources)*.
- Printed slips: Luan (2021, §5) lists the scalings of one expRK5s10 call as
  $[c_9,c_{10},c_8]$, which is not increasing as the routine requires. Deka & Einkemmer
  (2022) use $\alpha$ both for the eigenvalue estimate (§2.3) and for a controller
  parameter (§2.4).

# Citations

- [Deka & Einkemmer (2022)](/sources/deka-2022.md) — §1, §2.3 (Leja points, Newton form, shift and scale, convergence caveat), §3.1 (matrix-free Jacobian), §4.2 (Krylov cost, Leja vs Krylov on KHI), §4.2.1 Table 3, §5.2–5.3 (reconnection, EPIRK Krylov-friendliness, augmented matrices), §6; author manuscript.
- [Luan (2021)](/sources/luan-2021.md) — §1, §2.1, §5 Eqs. 5.1–5.3 (`phipm_simul_iom`, evaluation counts), §6 (settings); arXiv v1.
- [Dallerit & Tokman (2025)](/sources/dallerit-2025.md) — §5.3–5.5, §6.3 (single KIOPS projection, embedded estimate with two calls, Krylov dense output).
- [Permyakova & Goldobin (2025)](/sources/permyakova-2025.md) — §2 Eqs. 5–9 (auxiliary problems, cancellation), §3.1–3.3 (auxiliary steps, sparsity, Figs. 2, 5), §4, App. A Eqs. A.1–A.7 (Horner recursion, truncation, strong vs soft accuracy, Figs. 10–11); arXiv v2.
- [Buvoli & Minion (2024)](/sources/buvoli-2024.md) — §3.1, §7 (diagonal operators, methods cited); arXiv v2.
- [Hochbruck & Ostermann (2010)](/sources/hochbruck-2010.md) — §2.4 Eq. (2.48), §2.5 Eq. (2.70) (Krylov-motivated reformulations); §4.1 Thms. 4.1, 4.3, Remark 4.2 (Chebyshev); §4.2 Eqs. (4.2)–(4.5), Thms. 4.4–4.5, p. 268 (Krylov); §4.3 Eq. (4.6) (Leja); §4.4 Thm. 4.6 (contour integrals); §4.5 (software); version of record.
- [Caliari et al. (2024)](/sources/caliari-2024.md) — §1, §3, §5.1–5.2 (FFT, μ-mode/Kronecker sums, kiops tolerance, Figs. 6, 8–9); arXiv v2.
