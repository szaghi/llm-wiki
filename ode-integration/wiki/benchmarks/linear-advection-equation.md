---
type: Benchmark
title: "Linear advection equation"
description: "The constant- or variable-coefficient advection equation with its exact translated solution; the sources use it to verify temporal order, to compute von Neumann CFL limits of single-step and multiderivative schemes, to test bound-preserving and invariant-domain-preserving limiting with non-SSP Runge–Kutta methods, boundary-induced order reduction, mesh-induced stiffness, asynchronous halo exchange, step-size control and implicit-stage solvers."
status: established
aliases: [linear advection, advection equation, scalar advection equation, transport equation, linear transport equation, travelling bump]
tags: [verification, stability, positivity, order-reduction, ssp]
timestamp: 2026-10-20T06:18:00Z
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
- [Ern & Guermond (2022)](/sources/ern-2022.md) (§4.3.1): $a=1$ on $(0,1)$, the compactly
  supported bump $u_0=\bigl(4\frac{(x-x_0)(x_1-x)}{x_1-x_0}\bigr)^6$ on $(x_0,x_1)=(0.1,0.4)$,
  $T=1$, fourth-order finite differences on 50 to 3200 points, relative $L^\infty$ error;
  explicit Runge–Kutta methods of orders 2 to 5 made
  [invariant-domain preserving](/methods/invariant-domain-preserving-time-stepping.md) by
  limiting, against SSP methods at equal cost.
- [Quezada de Luna & Ketcheson (2022)](/sources/quezadadeluna-2022.md) (§8.1, Eq. (35), with
  $\epsilon=0$): $a=1$ on $[0,2\pi]$ with $u_0=\sin^4x$ (see Qualifications), $t=2\pi$, WENO5
  finite volumes with a five-stage fifth-order SDIRK, $h=0.5\Delta x$, global bounds $[0,1]$;
  [space–time flux limiting](/methods/bound-preserving-flux-limiting.md) around a backward
  Euler low-order scheme.
- [Vermeire & Hedayati Nasab (2021)](/sources/vermeire-2021.md) (§5.1, Eq. (61)): $a=1$, the
  Gaussian $u_0=e^{-2x^2/5}$ on a periodic domain of length 20 to $t=20$ (one period), flux
  reconstruction (nodal DG) of degree 8 with upwind fluxes on 80 elements refined towards the
  centre so that the largest element is about $2.5\times10^5$ times the smallest; the refined
  middle half is integrated implicitly by element-wise
  [IMEX Runge–Kutta](/methods/imex-runge-kutta.md).

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
- Ern & Guermond (2022, §4.3.2): $\mathbf a=(0.9,1)$, not aligned with mesh edges, on
  $(0,1)^2$, product of two compactly supported bumps, $T=0.5$, continuous $\mathbb P_1$
  finite elements on uniform triangle meshes (superconvergent to third order at the nodes);
  and (§4.4.1, Eq. (44)) the rotation $\mathbf a=2\pi(-x_2,x_1)$ of a slotted cylinder, a cone
  and a smooth hump on the unit disk for one revolution on unstructured Delaunay meshes of
  1605 to 389,860 nodes, CFL 0.25.
- Quezada de Luna & Ketcheson (2022, §8.5–8.6, Eqs. (40)–(42)): LeVeque's solid-body rotation
  of a hump, a cone and a slotted disk on the periodic unit square, one revolution on
  $128^2$ cells, and LeVeque's periodic swirling flow
  $\mathbf a=\bigl(\sin^2(\pi x)\sin(2\pi y),-\sin^2(\pi y)\sin(2\pi x)\bigr)\cos(\pi t/T)$ with
  the same data, $T=1.5$.
- [Ranocha et al. (2022)](/sources/ranocha-2022.md) (§3), DG of degree 4 on uniform and
  curvilinear grids; [Gaburro et al. (2023)](/sources/gaburro-2023.md), a travelling bump on
  unstructured triangles to $t_f=3$ and $15$; [Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md)
  (§7.1), manufactured solutions on five element types.

**Advection–diffusion variants.** Two sources add a diffusion term
$\epsilon\,\partial_x^2u$ ($\epsilon$ page-local) and keep an exact solution:

- Quezada de Luna & Ketcheson (2022, §8.1, Eq. (35)) take $\epsilon=10^{-3}$ with
  $u_0=\sin^4x$, whose exact solution
  $\tfrac38-\tfrac12e^{-4\epsilon t}\cos2(x-t)+\tfrac18e^{-16\epsilon t}\cos4(x-t)$ they print,
  and (§8.7, Eq. (43)) the 2D analogue $u_t+u_x+u_y=\epsilon\Delta u$ on $[0,2\pi]^2$ with
  $u_0=\sin^4(x+y)$, $t=0.5$.
- [Goswami et al. (2023)](/sources/goswami-2023.md) (§3.5, Eq. (44)) take a periodic domain of
  length $2\pi$ and a sum of sines with random phases, whose modes decay like
  $e^{-\epsilon\kappa^2t}$ and travel with the advection speed ($\kappa$ the wavenumber,
  page-local); the values of the speed, $\epsilon$ and the final time are not printed. The
  processing elements exchange halo data with random delays.

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

**Robustness of order to the step size.** Ern & Guermond (2022) choose
$h=\mathrm{CFL}\times s\times h^*$, $h^*$ the largest step for which a forward Euler step of the
low-order scheme stays in the invariant domain, so all methods use the same number of flux
evaluations. In 1D, at CFL 0.25, SSPRK(2,2) leaves the asymptotic regime on the finest mesh
(rate $-0.50$ at 3200 points) while the midpoint rule RK(2,2;1) keeps rate 1.99 (Table 1); at
third order SSPRK(3,3) degrades (rates 1.35–1.81) more than Heun's third-order RK(3,3;1),
while RK(4,3;1), fourth order on linear problems, reaches 3.94 (Table 2); at fourth order and
CFL 0.2 only RK(5,4;1) stays optimal on fine meshes ($5.38\times10^{-9}$ against
$9.29\times10^{-8}$ for SSPRK(5,4)) (Table 3); the new seven-stage fifth-order RK(7,5;1)
reaches its asymptotic range at CFL 0.02–0.025 (Table 4). In 2D all methods give optimal
$L^1$ rates for CFL between 0.4 and 0.7; in $L^\infty$ at CFL 0.2 RK(4,3;1) is fourth order and
best overall and SSPRK(3,3) behaves poorly (Tables 5–6). See
[SSP methods](/methods/strong-stability-preserving-runge-kutta.md).

**Order under mesh-induced stiffness.** With the element-size ratio of about
$2.5\times10^5$, the accelerated IMEX schemes AIMEX$s$,2, $s=4,\dots,10$, converge at second
order (observed 1.96–2.00) with errors nearly independent of $s$, at
$h=10^{-3},\dots,1.25\times10^{-4}$; the Ascher–Ruuth–Spiteri pair IMEX3,2 they extend shows
observed orders 3.55, 2.47, 2.19 and smaller errors at small steps ($2.80\times10^{-8}$
against $1.03\times10^{-7}$ for AIMEX4,2 at $h=1.25\times10^{-4}$), which the paper does not
explain (Vermeire & Hedayati Nasab 2021, §5.1, Table 2). Their AIMEX stability polynomials are
optimized on von Neumann spectra of flux reconstruction for this equation: the optimal
four-stage polynomials allow 1.79–2.01 times the explicit step of IMEX3,2 for degrees 1–8
(Table 1), and the gain grows about linearly with $s$ (see
[optimal stability polynomials](/methods/optimal-stability-polynomial.md)).

**Asynchronous halo exchange.** In the advection–diffusion runs of Goswami et al. (2023,
§3.5, Figs. 4–6), at constant CFL, coupling low-storage Runge–Kutta stages naively with
delayed halo data caps the spatial convergence at slope $-3$ (after an initial slope $-4$ or
$-6$), while updating the halo points through the Runge–Kutta recurrence with temporal
asynchrony-tolerant stencils keeps slopes $-4$ (LSERK2 with fourth-order differences) and $-6$
(LSERK3a with sixth-order differences), close to the synchronous errors; at fixed resolution
the error grows linearly with the number of processing elements, as their error model
predicts. See [low-storage Runge–Kutta](/methods/low-storage-runge-kutta.md).

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
[positivity preservation](/properties/positivity-preservation.md).

Beyond the SSP paradigm, two sources keep the bounds with methods that are not SSP. With
invariant-domain-preserving limiting after each incremental stage, the midpoint rule, "often
shun in the literature for its lack of stability", performs very well on the three-solids
rotation at CFL 0.25, and RK(2,2;1) and RK(4,3;1) converge at $L^1$ rates of about 0.8 (Ern &
Guermond 2022, §4.4.1, Fig. 2, Table 7). With space–time flux limiting of a fifth-order SDIRK,
the unlimited WENO–SDIRK solution of the solid-body rotation ranges over
$[-7.80\times10^{-4},1.0023]$ at the final time, with $L^1$ error $2.09\times10^{-2}$; the FCT
and global-monolithic-convex limited versions stay within $[0,1]$ with errors
$2.22\times10^{-2}$ and $2.10\times10^{-2}$, and the backward Euler low-order scheme has error
$1.32\times10^{-1}$ (Quezada de Luna & Ketcheson 2022, §8.5, Fig. 6); on the swirling flow the
unlimited range is $[-7.01\times10^{-3},1.0366]$ and the limited errors equal the unlimited
one to two digits (§8.6, Fig. 7). On the smooth $\sin^4$ data with $\epsilon=0$ and
$h=0.5\Delta x$, the unlimited scheme reaches $L^1$ error $1.25\times10^{-4}$ at $\Delta x=1/200$
(rate 4.15) with a bound violation of $2.08\times10^{-5}$; FCT needs two limiter iterations, and
the convex limiter a relaxation parameter of at least 2, to match it while keeping the bounds
to round-off; one FCT iteration gives rate 3.65 (Table 1). With $\epsilon=10^{-3}$ physical
diffusion reduces limiter action and one iteration suffices (rates 4.52–4.55, Table 2); with
$\epsilon$ alone ($a=0$) the limiters do not activate (§8.1); in 2D full accuracy needs two FCT
iterations or relaxation parameter at least 1 (rates 4.52–4.70, Table 5). The observed rates
mix temporal and spatial error, since $h$ and $\Delta x$ are refined together. In the other direction,
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
- **Initial datum of Quezada de Luna & Ketcheson (2022).** Eq. (35) prints
  $u(x,0)=\sin^4(2\pi x)$ on $[0,2\pi]$, but their printed exact solution equals
  $\sin^4(x-t)$ at $\epsilon=0$, and the 2D analogue (43) prints $\sin^4(x+y)$; the datum run is
  $\sin^4x$ ($\sin^4x=\frac38-\frac12\cos2x+\frac18\cos4x$; compiler check, not in the source).
  Their tables list $\Delta x=1/25,\dots,1/200$ on a domain of length $2\pi$, which is
  ambiguous as printed. They call the baseline integrator a fifth-order SDIRK, but every
  measured rate is about 4 and temporal and spatial errors are not separated.
- Ern & Guermond (2022) measure "efficiency" as $1/(s\,\Delta c_{\max})$ of the incremental
  stages, a quantity different from the SSP effective coefficient $\mathcal C_{\mathrm{eff}}$
  except for SSPRK(2,2) and SSPRK(3,3); the two are not comparable (see
  [invariant-domain-preserving time stepping](/methods/invariant-domain-preserving-time-stepping.md)).
- Vermeire & Hedayati Nasab (2021) analyse only the explicit stability polynomial on the
  explicit-region spectrum; the coupled stability at the implicit–explicit interface is
  checked only visually.
- Goswami et al. (2023) refine at constant CFL and report convergence against the number of
  grid points; their slopes are spatial orders of the coupled scheme.
- Ern & Guermond (2022) were read as the HAL manuscript, Quezada de Luna & Ketcheson (2022)
  as arXiv v1.
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
- [Ern & Guermond (2022)](/sources/ern-2022.md) — §4.2 (Eq. (42)), §4.3.1–4.3.2 (Tables 1–6), §4.4.1 (Eq. (44), Fig. 2, Table 7); HAL v2.
- [Quezada de Luna & Ketcheson (2022)](/sources/quezadadeluna-2022.md) — §8.1 (Eq. (35), Tables 1–3), §8.5–8.7 (Eqs. (40)–(43), Figs. 6–7, Table 5); arXiv v1.
- [Vermeire & Hedayati Nasab (2021)](/sources/vermeire-2021.md) — §4.3 (Table 1), §5.1 (Eq. (61), Table 2).
- [Goswami et al. (2023)](/sources/goswami-2023.md) — §3.5 (Eq. (44), Figs. 4–6).
