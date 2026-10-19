---
type: Method
title: "Optimal stability polynomials for explicit Runge–Kutta methods"
description: "Choosing the free coefficients of an explicit method's stability polynomial to maximize the stable step for the spectrum of a given semi-discretization (Ketcheson–Ahmadia bisection over a convex problem), then realizing it by a tableau; gains grow with stage count and are measured per right-hand-side evaluation."
status: established
aliases: [stability-optimized Runge–Kutta, optimized explicit Runge–Kutta, Ketcheson–Ahmadia optimization, maximal stable step size optimization]
tags: [stability, explicit, runge-kutta, step-size-control]
timestamp: 2026-10-19T00:00:00Z
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
§3.1, Eq. (6)). Ketcheson & Ahmadia's reformulation, as recalled by Hedayati Nasab et
al. (§3.1, Alg. 1, Eqs. (7)–(8)), fixes $h$ and solves the **convex** inner problem

$$r(h)=\min_{\theta_{p+1},\dots,\theta_s}\ \max_{\lambda\in\mathcal E}\bigl(\lvert P(h\lambda)\rvert-1\bigr),$$

convex because $P(h\lambda)$ is affine in the $\theta_j$ and the modulus is convex;
the outer problem $\max\{h: r(h)\le0\}$ is a one-dimensional bisection. Hedayati Nasab
et al. converge the bisection to $10^{-12}$ with CVX in MATLAB. A tableau realizing the
polynomial is then built, e.g. by Ketcheson–Ahmadia's "least truncation" method
(§7.1), whose full Butcher arrays are given only in the supplementary material.

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
- **Internal stability** of many-stage methods (round-off amplification) is cited but
  not analysed by Hedayati Nasab et al.

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
- The source writes the polynomial coefficients as $\gamma_j$ and the order as $q$;
  here $\theta_j$ and $p$.

# Citations

- [Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md) — §2 (Eqs. 1–5), §3.1 (Eqs. 6–8, Alg. 1), §5, §6.1–6.5 (Figs. 4–6, Tables 1–9), §7.1–7.2 (Figs. 7–10).
- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §3, §5.5.4, §6.2–6.3 (Fig. 7), §7.1, App. B, Suppl. Table 1.
- [Biswas et al. (2025)](/sources/biswas-2025.md) — Lemma 2.1, Thm. 2.6, §7 (weak stage order constrains the polynomial).
