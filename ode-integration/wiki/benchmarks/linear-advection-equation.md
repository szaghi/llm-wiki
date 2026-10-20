---
type: Benchmark
title: "Linear advection equation"
description: "The constant- or variable-coefficient advection equation with its exact translated solution; the sources use it to verify temporal order, to compute von Neumann CFL limits of single-step and multiderivative schemes, to test bound-preserving limiting with non-SSP Runge–Kutta methods, boundary-induced order reduction, step-size control and implicit-stage solvers."
status: established
aliases: [linear advection, advection equation, scalar advection equation, transport equation, linear transport equation, travelling bump]
tags: [verification, stability, positivity, order-reduction, ssp]
timestamp: 2026-10-20T10:00:00Z
---

# Linear advection equation

The linear advection equation

$$\partial_tu+a\,\partial_xu=0,\qquad u(x,t)=u_0(x-at),$$

(page-local: $u$ the transported quantity, $a$ the advection speed; in two dimensions
$\partial_tu+\mathbf a\cdot\nabla u=0$) is the simplest hyperbolic test. Its exact solution
is known for all times, so the observed convergence order of a fully discrete scheme can be
measured without a reference run. Its upwind semi-discretizations have the spectra that
stability polynomials and CFL limits are designed for, and discontinuous data test whether a
scheme keeps the solution within its initial bounds. Most sources of the bundle that develop
explicit, single-step or multiderivative schemes for hyperbolic problems run it, usually
first.

## Set-ups in the sources

**One-dimensional, periodic.**

- [Kuzmin et al. (2022)](/sources/kuzmin-2022.md) (§5.2, Eqs. 58–59): $a=1$ on $(0,1)$,
  fifth-order WENO finite volumes with a local Lax–Friedrichs flux, $h=0.4\Delta x/(1+\kappa)$
  ($\kappa$ the relaxation parameter of their limiter, page-local, as on [bound-preserving flux limiting](/methods/bound-preserving-flux-limiting.md)), $t=1$, 25 to 1600 cells.
  Data: the Gaussian $u_0=e^{-100(x-0.5)^2}$, and a composite profile (from Guermond,
  Pasquetti and Popov, as recalled) with a narrow Gaussian, a step and a semi-ellipse, run to
  $t=1$ and $t=100$ on 200 cells.
- [Micalizzi & Torlo (2024)](/sources/micalizzi-2024.md) (§9.2.1, Table 7): $u_t+u_x=0$ on
  $[0,1]$, $u_0=\cos2\pi x$, $T=1$, CFL 0.1, continuous Galerkin with Bernstein (B2, B3),
  equispaced Lagrange (P2, P3) and Gauss–Lobatto Lagrange (PGL2–PGL4) elements and
  continuous-interior-penalty stabilization, advanced by explicit
  [deferred correction](/methods/deferred-correction.md).
- [Babbar et al. (2022)](/sources/babbar-2022.md) (§8.1, Figs. 2–14): $a=1$ on $[0,1]$ with
  $u_0=\sin2\pi x$ to $t=2$ (error growth to $t=15$ on 200 degrees of freedom), the same with
  inflow Dirichlet data, a wave packet $e^{-10x^2}\sin10\pi x$, a square hat, and the
  Jiang–Shu composite profile (Gaussian, rectangle, triangle, semi-ellipse) on $[-1,1]$ to
  $t=8$; flux reconstruction of degree $N$ (page-local) with
  [Lax–Wendroff time stepping](/methods/lax-wendroff-flux-reconstruction.md) against SSP
  Runge–Kutta.
- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) (§5.3.1): spectral-difference
  semi-discretizations, $h=\frac{0.5}{\mathsf M+1}\frac{\Delta x}{\lvert v_{\max}\rvert}$, ADER
  and DeC of orders 3 to 9.

**One-dimensional, variable coefficient or with boundaries.** Babbar et al. (2022, §8.2,
from Öffner and Ranocha) take $f=a(x)u$ with $a=x$, $u_0=\sin(12(x-0.1))$ on $[0.1,2\pi]$, and
$a=x^2$, $u_0=\cos(\pi x/2)$ on $[0.1,1]$ to $t=50$, both with exact solutions and inflow data.
[Biswas et al. (2023)](/sources/biswas-2023.md) (§6) and
[Biswas et al. (2025)](/sources/biswas-2025.md) (§5.1, CFL 0.9, $t=0.7$, Clawpack finite
volumes with exact boundary cell averages, forcing) impose time-dependent inflow data.

**Two-dimensional.**

- Babbar et al. (2022, §11, Eq. 20): $\mathbf a=(1,1)$ with $\sin2\pi x\sin2\pi y$ on the
  periodic unit square to $t=1$; the rotating field $\mathbf a=(-y,x)$ with a Gaussian hump
  to $t=\pi/2$; LeVeque's rotation of a smooth hump, a cone and a slotted disc, one turn,
  $100\times100$ cells.
- [Zeifang & Schütz (2022)](/sources/zeifang-2022.md) (§4.1.1, §4.3.1, Eq. 20):
  $\mathbf a=(0.3,0.3)$ on $[-1,1]^2$ with exact solution $\sin(\pi(x-\mathbf at))$, DG spectral
  elements of degree 5 ($16^2$ elements, solver study) or 7 ($32^2$ elements, $T=0.8$,
  convergence study).
- [Ranocha et al. (2022)](/sources/ranocha-2022.md) (§3), DG of degree 4 on uniform and
  curvilinear grids; [Gaburro et al. (2023)](/sources/gaburro-2023.md), a travelling bump on
  unstructured triangles to $t_f=3$ and $15$; [Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md)
  (§7.1), manufactured solutions on five element types.

## What it shows

**Temporal order, and when the integrator limits it.**

- Kuzmin et al. (2022, Table 3): with WENO5 in space, the baseline errors at 1600 cells
  converge at 5.00 for the fifth-order extrapolated Euler method and Butcher's sixth-order
  seven-stage method, but at 4.29 for the fourth-order SSP54. The reading that the
  fourth-order integrator caps the rate on the finest grid is a *compiler
  reading*, not the authors'.
- Micalizzi & Torlo (2024, §9.2.1, Figs. 11–12): the interpolating variant bDeCu has the
  errors of the original DeC on every element type, and formal order is reached except with
  B3 and P3, which give second order for both; bDeCu is up to about 1.8 times faster. The
  supplement traces the B3/P3/B4 order loss to the continuous-Galerkin DeC itself: 10 (P3),
  80 (B3) or 320 (B4) iterations restore formal order, and CFL numbers 0.1, 0.01 and 0.001
  do not change it (Remark 9.1).
- Zeifang & Schütz (2022, §4.3.1, Fig. 7): their implicit two-derivative Hermite–Birkhoff
  predictor–corrector schemes HBPC(6,·) and HBPC(8,·) gain one order per correction up to the
  quadrature order; HBPC(4,·) is already fourth order after the predictor (see
  [multiderivative Runge–Kutta](/methods/multiderivative-runge-kutta.md)).
- ADER and DeC reach their design orders 3 to 9 (Han Veiga et al. 2021, §5.3.1; see
  [ADER](/methods/ader-time-integration.md)); relaxed ADER-DG of degrees 1–3 gives observed
  $L^2$ orders 1.78–1.84, 2.77–2.94 and 3.47–3.97 on the travelling bump, below the design
  orders 2–4 that the text claims (Gaburro et al. 2023, Table 1); manufactured solutions confirm the design orders of
  many-stage methods with optimal stability polynomials (Hedayati Nasab et al. 2021, §7.1).

**Fully discrete linear stability (von Neumann CFL limits).** For single-step schemes that
are not of method-of-lines type, the admissible Courant number $\nu$ comes from the Fourier
amplification matrix of the fully discrete scheme, not from an ODE stability region (see
[von Neumann stability analysis](/definitions/von-neumann-stability-analysis.md)):

- Babbar et al. (2022, §6, Table 1): for Lax–Wendroff flux reconstruction with Radau
  correction, evaluating the dissipative part of the numerical flux with the time-averaged
  solution (their D2) instead of the solution at $t_n$ (D1) raises the limit from 0.226,
  0.117, 0.072, 0.049 to 0.333, 0.170, 0.103, 0.069 for $N=1,\dots,4$; with the $g_2$
  correction from 0.465, 0.204, 0.116, 0.060 to 1.000, 0.333, 0.170, 0.103. D2 is exactly
  the upwind flux for constant advection (§5, Remark 1), and the limits are sharp: slightly
  larger steps blow up (§6).
- [Chouchoulis et al. (2022)](/sources/chouchoulis-2022.md) (§5, Thm. 2, Table 2): on linear
  advection their multiderivative Runge–Kutta schemes with compact approximate Taylor
  derivatives reduce to an "MDRK–Lax–Wendroff" scheme, with critical Courant numbers 1.2954
  (2DRKCAT3-2), 1.4718 (2DRKCAT4-2), 1.0619 (2DRKCAT5-3), 0.4275 (3DRKCAT5-2), 0.2300
  (3DRKCAT7-3) and 0.8563 (4DRKCAT6-2), against 1 for the underlying CAT schemes. Schemes
  with an even number of derivatives are more stable, and the method-of-lines stability
  region is a misleading predictor: the "MOL viewpoint is inadequate".
- Method-of-lines analyses use the same equation: Hedayati Nasab et al. (2021) compute
  optimal stability polynomials from the multidimensional von Neumann spectrum of upwind
  flux reconstruction (see [optimal stability polynomials](/methods/optimal-stability-polynomial.md)),
  and [Vermeire (2023)](/sources/vermeire-2023.md) (Table 1) tabulates the maximal stable
  Courant numbers of embedded paired explicit pairs, which grow with the number of active
  stages.

**Long-time behaviour.** Babbar et al. (2022, §8.1.1, Figs. 3–5) find slightly smaller
errors and slower error growth for Runge–Kutta flux reconstruction than for the Lax–Wendroff
version, attributed to the superconvergence of Runge–Kutta DG. At $N=4$ with periodic data both
show a mild linear instability: the relative $L^2$ norm grows linearly with slopes of about
$6.2\times10^{-10}$ (D1) and $5.4\times10^{-10}$ (D2) for Lax–Wendroff and about
$2.9\times10^{-13}$ and $1.9\times10^{-13}$ for SSPRK54 and SSPRK55. Norm monotonicity of
Runge–Kutta methods on upwind and central DG is the subject of
[Sun & Shu (2021)](/sources/sun-2021.md) (see
[superviscosity-stabilized Runge–Kutta](/methods/superviscosity-stabilized-runge-kutta.md)).

**Bounds with discontinuous data.** On the composite profile with 200 cells the unlimited
WENO baselines undershoot the global minimum by $4.97\times10^{-6}$ at $t=1$ and by
$1.32\times10^{-2}$ at $t=100$; with the global monolithic convex limiter of Kuzmin et al.
(relaxation $\kappa=1$) the bound violation is at round-off level ($\sim10^{-15}$) and smooth
regions are untouched (§5.2, Fig. 2). On the Gaussian, $\kappa=1$ keeps the optimal rates for
every limited scheme, while $\kappa=0$ drops them to about 2.7, except when only the final
stage of the sixth-order method is limited (EOC 5.00) (Table 3). See
[bound-preserving flux limiting](/methods/bound-preserving-flux-limiting.md),
[extrapolation methods](/methods/extrapolation-methods.md) and
[positivity preservation](/properties/positivity-preservation.md). In the other direction,
paired explicit Runge–Kutta families on first-order upwind finite volumes are linearly stable
but violate Harten's monotonicity criterion at the interface between members
([Doehring et al. 2024b](/sources/doehring-2024-b.md), §3.2; see
[paired explicit Runge–Kutta](/methods/paired-explicit-runge-kutta.md)).

**Boundary data and order reduction.** With time-dependent inflow data the error
concentrates in a numerical boundary layer of width $O(h)$, so methods of weak stage order 1
lose a full order in $u_x$ (Biswas et al. 2023, §6, DIRK-(12,5,4) order 5 in $u$ and 4 in
$u_x$; Biswas et al. 2025, §5.1, SSPRK3, RK4 and Dormand–Prince drop to order 2 in $u$ and 1 in
$u_x$). See [order reduction](/definitions/order-reduction.md) and
[weak stage order](/definitions/weak-stage-order.md). Babbar et al. (2022, §8.1.1, Remark 4,
Fig. 6b) see slightly larger Runge–Kutta errors than Lax–Wendroff errors at $N=3,4$ with
inflow data, which they attribute to the boundary treatment inside Runge–Kutta stages; their
Lax–Wendroff scheme imposes the time average of the boundary flux by Gauss quadrature
in time (see [boundary conditions for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md)).

**Step-size control in the stability-limited regime.** On 2D linear advection a PI
controller settles automatically at the maximal stable step, $\nu=2.1$, matching the best
hand-tuned CFL run, and doubles it on a curvilinear grid without tuning (Ranocha et al. 2022,
§3; see [step-size control](/methods/step-size-control.md)).

**Implicit stage solvers.** For the extended system of the two-derivative HBPC scheme, the
GMRES iterations per predictor step grow with the step at a slope slightly steeper than for
implicit Euler, close to one; their element-wise extended block-Jacobi preconditioner reduces
both the slope and the count "drastically" (Zeifang & Schütz 2022, §4.1.1, Fig. 2; see
[implicit stage solvers](/methods/implicit-stage-solvers.md)).

## Qualifications

- Kuzmin et al. (2022) print the 1D SSP step bound (Eq. B.9) with the factor $(1+\kappa)$ in
  the numerator, whereas their Eq. 28, their default $h=0.4\Delta x/(1+\kappa)$ and their
  statement that larger $\kappa$ tightens the CFL condition require it in the denominator
  *(compiler check of pp. 15 and 32; printed slip)*.
- Babbar et al. (2022) print 160 degrees of freedom for the wave-packet test in the
  Fig. 8 caption and 200 in the text (§8.1.1).
- Zeifang & Schütz (2022, Eq. 20) write the 2D datum as $\sin(\pi x)$ with vector $x$; how the
  scalar argument is formed is not printed.
- Chouchoulis et al. (2022) run their Burgers, Buckley–Leverett and Euler tests at $\nu=0.5$,
  above the critical linear Courant numbers of 3DRKCAT5-2 and 3DRKCAT7-3, and those schemes
  still converge there; the paper does not comment, so Table 2 is not a sharp practical limit
  (§6).
- Micalizzi & Torlo's measured speedups differ from their stage-count predictions in both
  directions (e.g. about 2 measured against 1.757 predicted for an ODE test, §9.1.1); stage
  counts are not cost (Remark 5.1).

# Citations

- [Kuzmin et al. (2022)](/sources/kuzmin-2022.md) — §5.2 (Eqs. 58–59, Table 3, Fig. 2), App. B (Eq. B.9); arXiv v2.
- [Micalizzi & Torlo (2024)](/sources/micalizzi-2024.md) — §9.2.1 (Table 7, Figs. 11–12), Remark 9.1, Supplement §3.2; arXiv v4.
- [Babbar et al. (2022)](/sources/babbar-2022.md) — §5 (Remark 1), §6 (Table 1), §8.1–8.2 (Figs. 2–17), Remark 4, §11 (Eq. 20, Figs. 31–34); arXiv v1.
- [Chouchoulis et al. (2022)](/sources/chouchoulis-2022.md) — §5 (Thm. 2, Prop. 1, Table 2), §6.
- [Zeifang & Schütz (2022)](/sources/zeifang-2022.md) — §4.1.1 (Eq. 20, Fig. 2), §4.3.1 (Fig. 7); arXiv v1.
- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) — §5.3.1.
- [Biswas et al. (2023)](/sources/biswas-2023.md) — §6 (linear advection, Fig. 6).
- [Biswas et al. (2025)](/sources/biswas-2025.md) — §1.3, §5.1 (Fig. 5.1).
- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §3 (Figs. 2–3).
- [Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md) — §5–6, §7.1 (Fig. 7).
- [Vermeire (2023)](/sources/vermeire-2023.md) — Table 1.
- [Gaburro et al. (2023)](/sources/gaburro-2023.md) — Table 1 (travelling bump).
- [Doehring et al. (2024b)](/sources/doehring-2024-b.md) — §3.2 (Figs. 2–3).
- [Sun & Shu (2021)](/sources/sun-2021.md) — numerical tests on upwind and central DG for linear advection.
