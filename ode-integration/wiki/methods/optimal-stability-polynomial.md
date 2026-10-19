---
type: Method
title: "Optimal stability polynomials for explicit Runge–Kutta methods"
description: "Choosing the free coefficients of an explicit method's stability polynomial to maximize the stable step for the spectrum of a given semi-discretization (Ketcheson–Ahmadia bisection over a convex problem, or a root parametrization for more than 100 stages), then realizing it by a tableau; gains grow with stage count and are measured per right-hand-side evaluation."
status: established
aliases: [stability-optimized Runge–Kutta, optimized explicit Runge–Kutta, Ketcheson–Ahmadia optimization, maximal stable step size optimization, pseudo-extrema, OSPREI]
tags: [stability, explicit, runge-kutta, step-size-control]
timestamp: 2026-10-20T03:00:00Z
---

# Optimal stability polynomials for explicit Runge–Kutta methods

An explicit $s$-stage method of linear order $p$ applied to $y'=\lambda y$ advances by
its [stability polynomial](/definitions/stability-function.md)

$$P(z)=\sum_{j=0}^s\theta_jz^j,\qquad \theta_j=\frac1{j!}\ (0\le j\le p),$$

which leaves $s-p$ free coefficients $\theta_{p+1},\dots,\theta_s$
([Hedayati Nasab et al. 2021](/sources/hedayatinasab-2021.md), §2, Eqs. (1)–(3)). For a
method-of-lines semi-discretization $y'=Ly$, linear stability requires
$h\lambda\in\mathcal S=\{z:\lvert P(z)\rvert\le1\}$ for every eigenvalue $\lambda$ of
$L$ (Eqs. (4)–(5)). When the step is limited by stability rather than accuracy (the
usual situation for explicit integration of hyperbolic and convection-dominated CFD
problems), the free coefficients can be spent on enlarging $\mathcal S$ in the shape
of the actual spectrum. An **optimal stability polynomial** maximizes the stable step
for a given eigenvalue set, stage count and order.

## The optimization problem

Let $\mathcal E$ be the set of semi-discrete eigenvalues (page-local). The problem

$$\max_{\theta_{p+1},\dots,\theta_s}\ h\quad\text{subject to}\quad \lvert P(h\lambda)\rvert-1\le0\ \ \forall\lambda\in\mathcal E$$

is nonconvex for $s>2$ with sub-optimal local optima (Hedayati Nasab et al. 2021,
§3.1, Eq. (6); [Hedayati Nasab & Vermeire 2022](/sources/hedayatinasab-2022.md),
§3.3). Ketcheson & Ahmadia's reformulation, as recalled by Hedayati Nasab et
al. (§3.1, Alg. 1, Eqs. (7)–(8)), fixes $h$ and solves the **convex** inner problem

$$r(h)=\min_{\theta_{p+1},\dots,\theta_s}\ \max_{\lambda\in\mathcal E}\bigl(\lvert P(h\lambda)\rvert-1\bigr),$$

convex because $P(h\lambda)$ is affine in the $\theta_j$ and the modulus is convex;
the outer problem $\max\{h: r(h)\le0\}$ is a one-dimensional bisection. Hedayati Nasab
et al. converge the bisection to $10^{-12}$ with CVX in MATLAB; the same formulation
drives the P-ERK constructions of Hedayati Nasab & Vermeire (2022, §3.3, Alg. 1) and
[Vermeire (2023)](/sources/vermeire-2023.md) (§4), and, written as a second-order cone
program, those of [Doehring et al. (2025)](/sources/doehring-2025.md) (App. C), who
solve it in extended and arbitrary precision with their own solver built on EiCOS. A
tableau realizing the polynomial is then built, e.g. by Ketcheson–Ahmadia's "least
truncation" method (§7.1), whose full Butcher arrays are given only in the
supplementary material.

**Conditioning limit.** The monomial coefficients decay like $1/j!$, and
[Doehring et al. (2024)](/sources/doehring-2024.md) (§1, §2.1.1) state that in double
precision the monomial convex formulation is limited to about 16–20 stages for general
spectra; earlier monomial-based optimizations reached degrees 14, 7 and 8.
[Doehring et al. (2024b)](/sources/doehring-2024-b.md) (§4.2) put the reliable range of
the Ketcheson–Ahmadia optimizer at degree about 16 in the monomial basis and report that up
to about 2000 eigenvalue constraints are optimized in under a minute.

## Estimating the spectrum

The constraint set $\mathcal E$ must cover the spectrum of the full-resolution
semi-discretization, whose dense eigendecomposition is expensive. Doehring et al. (2024b,
§4.1) estimate its **boundary** in five steps: (1) compute the full spectrum of a
reduced-resolution semi-discretization, of size $\mathcal O(10^3)$; (2) take its convex hull,
densified so that consecutive points are closer than the mean hull spacing, in one quadrant
by symmetry, assuming no eigenvalue with positive real part; (3) build the sparse Jacobian at
the target resolution by algorithmic differentiation; (4) scale the hull points by the ratio of
the minimal mesh widths and run shifted Arnoldi (ARPACK) around each scaled point in parallel,
about $1000/K$ eigenvalues for each of the $K$ shifts (page-local), with a loose tolerance
because the spectrum drifts during the run; (5) take the union. For a Kelvin–Helmholtz DGSEM
case of degree 3 the reduced $1024\times1024$ eigendecomposition takes 0.4 s, the full
$16384\times16384$ one more than 11 minutes, and twenty shifted Arnoldi runs about 30 s in total,
giving 930 eigenvalues that capture the shape (Fig. 5). The method serves the Orszag–Tang,
Kelvin–Helmholtz and Rayleigh–Taylor families of their
[paired explicit Runge–Kutta](/methods/paired-explicit-runge-kutta.md) study; see
[Trixi.jl](/software/trixi-jl.md).

## Results on DG/flux-reconstruction spectra

Hedayati Nasab, Pereira & Vermeire (2021) compute optimal polynomials for
flux-reconstruction (DG-recovering, upwind) semi-discretizations of linear advection,
from a multidimensional von Neumann analysis over all wavenumbers and directions, on
line, quadrilateral, triangular, hexahedral, prismatic and tetrahedral elements,
spatial degree up to 6, $p=1,\dots,4$, $s\le16$ (§5–6). Findings:

- the optimal step grows approximately linearly in $s$, as in earlier studies (§6.1,
  Fig. 4);
- the stage-normalized step $h_{\mathrm{opt}}/s$ (page-local $h_{\mathrm{opt}}$)
  saturates for $p=1,2$ but still increases beyond $s=16$ for $p=3,4$ (Fig. 6); for
  high spatial degree, $p=2$ costs almost nothing over $p=1$ at large $s$;
- at small $s$ the stability regions of high-order polynomials protrude well beyond the
  scaled spectrum; at large $s$ they conform to it (Fig. 5);
- for quadrilaterals and hexahedra the multidimensional optimum equals the
  one-dimensional one (ratio 1.00 at degree 4, Tables 1, 3); triangles, prisms and
  tetrahedra gain up to 1.12, 1.09 and 1.09, because their spectra protrude towards
  the negative real axis (Tables 2, 4, 5);
- at $s=16$, spatial degree 4, the per-stage step ratio
  $(h_{\mathrm{opt}}/s)/(h_{\mathrm{RK}}/p)$ of the optimal $p=3$ polynomial against
  classical three-stage RK3 is 1.46–1.74, and of the optimal $p=4$ polynomial against
  classical RK4 1.63–1.97, across element types (Tables 7, 9); manufactured
  solutions confirm the design orders 1–4 with $s=16$ (§7.1, Fig. 7);
- in a Taylor–Green vortex DNS ($Re=1600$, degree 5, $256^3$ points, run at 80% of the
  bisected limit) the optimized $p=4$, $s=16$ scheme gives step-per-stage speedups of
  1.68 (hex), 1.64 (prism) and 1.57 (tet) over RK4 with visually indistinguishable
  dissipation and enstrophy (§7.2, Figs. 8–10); see
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md).

The speedup is a ratio of stable steps per right-hand-side evaluation; no wall-clock
times are reported, and memory for 16 stages is not discussed.

The members of [paired explicit Runge–Kutta](/methods/paired-explicit-runge-kutta.md)
families are optimized the same way on one-dimensional flux-reconstruction DG spectra.
For third order, spatial degrees 0–8 and $e=3,\dots,16$ evaluations (page-local $e$: the
number of active stages of a member, equal to the degree of its polynomial), the optimal step
grows about linearly with $e$ and the step per evaluation increases monotonically up
to $e=16$ for every degree, e.g. 0.418806 at $e=3$ and 0.853547 at $e=16$ for degree 0,
0.029895 and 0.046618 for degree 4 (Hedayati Nasab & Vermeire 2022, §4.2, Table 1,
Fig. 2). For second-order members and their first-order embedded polynomials
Vermeire (2023, §4, Table 1, Fig. 1) tabulates the maximal stable CFL numbers for
degrees 1–8, e.g. 0.59 at $e=3$ and 3.43 at $e=16$ for degree 1, 0.04 and 0.30 for
degree 8; there the embedded polynomial is optimized to have a slightly *smaller*
region than the main one, so that the pair detects the stability limit.

## Root parametrization for many stages

Doehring et al. (2024, §2.2, Eqs. (2.10)–(2.11)) write every polynomial of linear
order at least one as

$$P(z)=1+z\prod_{j=1}^{s-1}\Bigl(1-\frac z{\tilde r_j}\Bigr)$$

and optimize the roots $\tilde r_j$ of $(P-1)/z$, which they call **pseudo-extrema**
(page-local symbol; the set is closed under conjugation). Since
$P(\tilde r_j)=1$, all pseudo-extrema lie on the boundary of $\mathcal S$. The order
conditions become Vieta relations, e.g. $\frac12=-\sum_j1/\tilde r_j$ for order two
(§4.4, Eq. (4.3)). For the optimal disk polynomials (first order
$(1+z/s)^s$, second order $\frac{s-1}s(1+\frac z{s-1})^s+\frac1s$) they prove that the
pseudo-extrema are the positive Chebyshev extreme points projected onto the circle,
hence equally spaced in arc length (Thms. 1–2); for even $s$ one pseudo-extremum is
real.

From this they **assume** that for strictly convex spectra the optimal pseudo-extrema
lie at roughly equal arc length on the convex hull of the scaled spectrum, supported
by 16-stage optima for DG spectra of Burgers, shallow water, ideal MHD and 2D Euler
(§3.2, Fig. 2). Algorithm 1 (§5): compute the 16-stage optimum with the monomial
method; scale the step linearly in $s$ (Eq. (4.1)); place the pseudo-extrema on a
piecewise-linear interpolant of the hull at equal arc length, reusing for even $s$ the
solution at $s/2$ as every second root; solve the feasibility problem in the real
parts, then a second pass with imaginary corrections bounded by 2% of
the spectrum height (Ipopt, exact derivatives by algorithmic differentiation;
finite-difference derivatives failed). Polynomials of degree 26–128 and orders 1–3
are obtained in seconds to minutes: degree 128 for the Burgers spectrum in about 9 s,
against 15.5 s for degree 16 with the monomial method (§6, Table 1). Nonconvex
spectra are treated with their convex hull; the isentropic-vortex spectrum reaches
97.9% of the linearly scaled step at $s=28$ and 100% at $s=56,112$ (§8). Applied
through many-stage methods, these polynomials raise the characteristic speeds that
can be run at a fixed step by a factor of four against 16-stage monomial-based
methods (64 against 16 stages, §11), but on nonlinear problems the zero SSP
coefficient of the realization cuts the usable step to 28–79% of the linear limit; see
[stabilized explicit Runge–Kutta methods](/methods/stabilized-explicit-runge-kutta.md).

## Polynomials constrained by the tableau

When the tableau structure fixes part of the polynomial, the free tableau entries,
not the monomial coefficients, are the natural unknowns. For fourth-order P-ERK only
$e-5$ coefficients are free, and Doehring et al. (2025, §4.2, Eqs. (4.7)–(4.8))
make the polynomial affine in products of subdiagonal tableau entries, which keeps
the second-order cone formulation; fitting tableau entries to optimized monomial
coefficients by least squares gave "significantly inferior results". The constrained
optimum reaches 85% of the unconstrained fourth-order one at $e=6$ and 96.5% at
$e=16$ (§4.3, Figs. 1–2). At second order Vermeire (2023, §3) recovers the tableau
from the polynomial sequentially, without a nonlinear solver, a recovery restated by
Doehring et al. (2024b, §4.3, Eq. (4.5)). At third order Doehring et al. (2024b, Eqs.
(4.6)–(4.7)) fix the abscissae in advance and solve for the tableau with a trust-region
method from random starts, requiring positive entries.

## Other design targets

Maximal stable step is one objective among several; Doehring et al. (2024, §2.1)
exclude dispersion–dissipation and SSP objectives explicitly.
[Faleichik & Moisa (2026)](/sources/faleichik-2026.md) (§1–3) maximize instead the
interval on which $P$ is positive and nondecreasing, giving up most of the real
stability interval of Runge–Kutta–Chebyshev methods for more convex regions and a
smaller error constant; the shifted Chebyshev and Legendre polynomials of stabilized
methods are fixed, not optimized, choices for the negative real axis. Both are on
[stabilized explicit Runge–Kutta methods](/methods/stabilized-explicit-runge-kutta.md).

## Optimized polynomials inside adaptive pairs

Ranocha, Dalcin, Parsani & Ketcheson build their low-storage embedded pairs
RK3(2)5[3S*₊], RK4(3)9[3S*₊], RK5(4)10[3S*₊] (and FSAL variants) on the main methods of
Parsani, Ketcheson & Deconinck, whose stability polynomials were optimized for
spectral-difference/DG spectra; the embedded method is designed so that its stability
region contains the main method's, and a PID controller is optimized for each pair
([Ranocha et al. 2022](/sources/ranocha-2022.md), §6, App. B). Their observations bear
on optimization targets:

- efficiency ratios follow the **real stability interval per evaluation**: the new
  third-order pair (4.93 over 5 evaluations, 0.99 per evaluation) is up to 18% more
  efficient than Bogacki–Shampine 3(2) (0.84), "in accordance with the relative
  lengths of the real stability intervals" (§6.2, §7.1, Suppl. Table 1);
- low Mach numbers stress the negative real axis more than the rest of the advection
  spectrum (§5.5.4);
- a from-scratch construction (Fourier footprint of the spectral-element operator,
  optimal polynomial via Ketcheson–Ahmadia, minimized error constants in RK-Opt) gave
  methods no better than those built on Parsani et al.; optimizing with more stages,
  or optimizing third-order methods for a fifth-order spatial discretization, gave no
  consistent speedup, consistent with the similar scaled convex hulls of DG spectra
  for spatial degree 1–4 (§6.2–6.3, Fig. 7).

With error-based [step-size control](/methods/step-size-control.md) the controller
settles at essentially the largest stable step (§3), so stability-optimized polynomials
pay off without a hand-tuned CFL number; see also
[low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md) and
[embedded pairs](/methods/embedded-runge-kutta-pair.md).

## Constraints that compete with stability

- **Weak stage order.** For an explicit method, weak stage order $q_{\mathrm w}$ fixes
  the highest $q_{\mathrm w}-1$ coefficients of the stability polynomial to zero,
  dually to order $p$ fixing the first $p+1$; methods attaining the stage bound
  $p+q_{\mathrm w}=s+1$ have $P$ equal to the degree-$p$ Taylor polynomial
  ([Biswas et al. 2025](/sources/biswas-2025.md), Lemma 2.1, Thm. 2.6, §7). Optimizing
  the polynomial and raising
  [weak stage order](/definitions/weak-stage-order.md) compete for the same freedom.
- **Nonlinear stability.** The optimization targets linear stability of linear
  advection only; SSP or positivity is not imposed, and the least-truncation tableaus
  are not SSP (Hedayati Nasab et al. 2021, as noted in the reading of that source).
  The [SSP](/methods/strong-stability-preserving-runge-kutta.md) analogue optimizes the
  radius of absolute monotonicity or the nonlinear SSP coefficient instead.
- **Internal stability.** A polynomial with many stages must be realized so that
  stage perturbations are not amplified; Hedayati Nasab et al. (2021) cite but do not
  analyse it, while Doehring et al. (2024, §9) find it "the major difficulty in
  realizing the maximum timestep" and reduce it by ordering and grouping the factors,
  and Doehring et al. (2025, §4.4) by the choice of free abscissae. See
  [internal stability](/definitions/internal-stability.md).

## Qualifications

- **Different baselines.** Hedayati Nasab et al. report up to 1.97 over classical RK4;
  Ranocha et al. find no consistent gain from further optimization over the
  already-optimized Parsani–Ketcheson–Deconinck methods. The two are compatible: the
  first measures against unoptimized methods at the linear stability limit, the
  second against optimized methods inside error-controlled runs.
- Hedayati Nasab et al. remove semi-discrete eigenvalues with machine-precision positive
  real part before optimizing, "as a consensus" (§5); their hull is called "concave"
  in places and "convex" in others (§6.2–6.3). Their speedup tables 6 and 8 carry the
  per-stage formula of Tables 7 and 9 in the caption, while reporting plain step
  ratios (e.g. 8.31 against RK3 at $s=16$).
- **Optimality of many-stage polynomials.** The monomial formulation solves a convex
  problem for each fixed step and so finds the global optimum of the bisection. The
  root parametrization of Doehring et al. (2024) is nonconvex, starts from an unproved
  equal-arc-length assumption, and in its fast feasibility mode only certifies the
  linearly scaled 16-stage step; its polynomials of more than 16 stages are feasible
  at that step, not proven maxima. The authors also note that the linear scaling
  brings no further gain per stage once reached (§4.3).
- Hedayati Nasab & Vermeire (2022, Eq. (40)) start the free-coefficient sum at
  $j=3$ although the free coefficients start at $j=4$.
- The sources write the polynomial coefficients as $\gamma_j$ or $\alpha_j$, the order
  as $q$ or $p$, the stage count as $s$, $S$, $e$ or $E$; here $\theta_j$, $p$, $s$
  and, for P-ERK members, $e$.

# Citations

- [Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md) — §2 (Eqs. 1–5), §3.1 (Eqs. 6–8, Alg. 1), §5, §6.1–6.5 (Figs. 4–6, Tables 1–9), §7.1–7.2 (Figs. 7–10).
- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §3, §5.5.4, §6.2–6.3 (Fig. 7), §7.1, App. B, Suppl. Table 1.
- [Biswas et al. (2025)](/sources/biswas-2025.md) — Lemma 2.1, Thm. 2.6, §7 (weak stage order constrains the polynomial).
- [Hedayati Nasab & Vermeire (2022)](/sources/hedayatinasab-2022.md) — §3.3 (Problems 1–3, Alg. 1, Eq. 40), §4.2 (Table 1, Fig. 2).
- [Vermeire (2023)](/sources/vermeire-2023.md) — §3, §4 (Eqs. 24–28, Table 1, Figs. 1–2).
- [Doehring et al. (2024)](/sources/doehring-2024.md) — §1, §2.1–2.2 (Eqs. 2.7–2.11), §3 (Thms. 1–2), §4.3–4.4, §5 (Alg. 1), §6 (Table 1), §8, §9, §11.
- [Doehring et al. (2025)](/sources/doehring-2025.md) — §4.2–4.4 (Eqs. 4.7–4.8, Figs. 1–2), App. C.
- [Doehring et al. (2024b)](/sources/doehring-2024-b.md) — §4.1 (Fig. 5), §4.2, §4.3 (Eqs. 4.4–4.7).
- [Faleichik & Moisa (2026)](/sources/faleichik-2026.md) — §1–3 (monotonicity interval as objective).
