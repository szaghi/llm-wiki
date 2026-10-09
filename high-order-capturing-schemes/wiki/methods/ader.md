---
type: Method
title: "ADER one-step schemes (arbitrary high order using derivatives)"
description: "Fully discrete one-step finite-volume and DG schemes that evolve the reconstructed polynomial in each cell in time — by Cauchy–Kowalewski Taylor series or by an element-local space–time Galerkin predictor — and update with space–time-averaged interface fluxes, giving equal order in space and time with one reconstruction per step."
status: established
aliases: [ADER, ADER-WENO, ADER-DG, ADER-CG, generalized Riemann problem, local space-time DG predictor, arbitrary derivative Riemann problem]
tags: [ader, single-step, time-discretization, finite-volume, dg, amr]
timestamp: 2026-10-09T00:00:00Z
---

# ADER one-step schemes

**Idea.** Solve, at each interface, a *generalized Riemann problem*
whose initial data are the two reconstructed polynomials rather than
constants. The time-integrated flux it gives then updates the cell average in
one step,
$$\bar u^{n+1}_i = \bar u^n_i - \frac{\Delta t}{h}\left(\hat{\mathcal{F}}_{i+1/2} - \hat{\mathcal{F}}_{i-1/2}\right),\qquad
\hat{\mathcal{F}}_{i+1/2} = \frac{1}{\Delta t}\int_{t^n}^{t^{n+1}}\hat f\left(u^{\mathrm p}_i(x_{i+1/2}, t),\, u^{\mathrm p}_{i+1}(x_{i+1/2}, t)\right)dt,$$
with a time quadrature (or exact integration) of the flux between
the two predictors. The order in time then matches the order of the
spatial reconstruction ([WENO](/methods/weno.md) or
[polynomial WENO](/methods/polynomial-weno.md)). The name stands for
"Arbitrary high order schemes using DERivatives" (Toro and coworkers)
([Dumbser & Käser (2007)](/sources/dumbser-2007.md), §1;
[Dumbser et al. (2013)](/sources/dumbser-2013.md), §1). The lineage is
the one-step MUSCL (van Leer) and ENO (Harten et al.) schemes, which
first evolve the reconstruction "in the small"
([Dumbser et al. (2013)](/sources/dumbser-2013.md), §1;
[Lax–Wendroff (Taylor) time discretization](/methods/taylor-time-discretization.md)).

## Two ways to build the predictor

**Cauchy–Kowalewski (Taylor) ADER.** Expand in time and replace each
time derivative by space derivatives through the PDE. In Toro and
Titarev's original version the leading interface state comes from an exact Riemann
solver on the extrapolated states, and the higher derivatives from
linearized Riemann problems for the extrapolated derivatives
([Dumbser et al. (2013)](/sources/dumbser-2013.md), §1). For *linear*
systems the order of time integration and flux evaluation can be
exchanged. The reconstruction is evolved inside each element, and the
time-integrated boundary values enter an exact Riemann solver. In 1D
the substitution is $\partial^k_t u = (-A)^k\partial^k_x u$, the
one-dimensional case of their eq. (42), which they state in reference
coordinates on triangles and tetrahedra. All space–time integrals are
precomputed on the reference element as flux matrices, which makes
the scheme quadrature-free. The scheme is stated stable up to Courant
number one in 1D ([Dumbser & Käser (2007)](/sources/dumbser-2007.md), §3).
The drawback is the algebra: for nonlinear systems the procedure is
cumbersome and problem-dependent, and it fails with stiff sources
([Zanotti et al. (2015)](/sources/zanotti-2015.md), §1;
[Dumbser et al. (2013)](/sources/dumbser-2013.md), §1).

**Local space–time Galerkin predictor.** Write the PDE in weak form on
the space–time reference element of each cell, test with space–time
basis functions, and integrate by parts in time. The reconstructed
polynomial enters as initial data in the weak sense. The result is an
element-local nonlinear system for the predictor's degrees of freedom,
solved by fixed-point (Picard) iteration. It needs only pointwise
evaluations of fluxes and sources, and in its discontinuous-in-time
form it handles stiff sources ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §2.3;
[Dumbser et al. (2014)](/sources/dumbser-2014.md), §2.2;
[Zanotti et al. (2015)](/sources/zanotti-2015.md), §3.1). With a nodal
tensor basis through Gauss–Legendre points every matrix is block-sparse
and the products act dimension by dimension
([Dumbser et al. (2013)](/sources/dumbser-2013.md), §2.3).

**ADER-CG** ([Balsara et al. (2009)](/sources/balsara-2009.md), §3) is
the modal, continuous-in-time variant. The predictor is required to
equal the reconstruction at $t = t^n$, so the purely spatial modes are
fixed and only the time-dependent modes are iterated. This needs fewer
flux evaluations, at the price of the weak form in time and of stiff
sources. Explicit third-order formulas are given on structured meshes
(second and fourth in appendices). The authors use exactly $K + 1$
iterations for order $K + 1$ and report never needing more, justified
by the Picard-iteration theory.

## Fluxes and the corrector

The space–time-averaged face flux needs Riemann solutions at many
quadrature points. [Balsara et al. (2009)](/sources/balsara-2009.md)
(§4.1) instead freeze the HLL signal speeds at the face's space–time
barycentre. The HLL flux then becomes linear in the left/right states
and fluxes, whose space–time averages the predictor supplies exactly. Rusanov and an
Osher-type path-integral flux are used by
[Dumbser et al. (2013)](/sources/dumbser-2013.md), §2.1. The same
predictor drives a one-step *DG* corrector: test the PDE with the
spatial basis, integrate over $I_i \times [t^n, t^{n+1}]$, and insert
$u^{\mathrm p}_i$ in the volume and boundary terms (ADER-DG;
[Dumbser et al. (2014)](/sources/dumbser-2014.md), §2.3). For MHD, the
predictor also supplies the space–time averages of the edge electric
fields ([constrained transport](/methods/constrained-transport.md)).

## Why one step

* **Cost.** One nonlinear reconstruction per element and step, instead
  of one per Runge–Kutta stage. On tetrahedra, a fifth-order optimal
  pointwise WENO would need 28 face quadrature points, and so 84
  reconstructions per step with RK3, for a scheme only third order in
  time. ADER-FV with a polynomial reconstruction is fifth order in space
  and time with one ([Dumbser & Käser (2007)](/sources/dumbser-2007.md), §6).
  For MHD on one core, the second-order ADER-WENO updates 31,000 zones
  per second in 3D. Third order costs 2.5 times second order, and
  fourth costs 3 times third ([Balsara et al. (2009)](/sources/balsara-2009.md), §4.2).
* **No Butcher barriers.** Explicit Runge–Kutta needs more stages than
  its order beyond four ([Dumbser & Käser (2007)](/sources/dumbser-2007.md), §3.1.1;
  [Balsara et al. (2009)](/sources/balsara-2009.md), §8). RKDG in
  practice stops at third order, the fourth-order TVD method being
  complex ([Zanotti et al. (2015)](/sources/zanotti-2015.md), §1).
  This agrees with the SSP barriers ([SSP order barriers](/results/ssp-order-barriers.md)).
* **Storage and AMR.** A one-step update needs no intermediate stages.
  It therefore allows time-accurate local time stepping on space–time
  adaptive grids, and needs fewer MPI exchanges
  ([Balsara et al. (2009)](/sources/balsara-2009.md), §1;
  [Dumbser et al. (2013)](/sources/dumbser-2013.md), §§1, 5;
  [high-order AMR](/methods/high-order-amr.md)).

**Time step.** ADER-FV keeps the Godunov-type Courant limit. Explicit
DG of degree $K$ is restricted to
$$\Delta t \le \frac{1}{d\,(2K+1)}\,\frac{h}{\vert\lambda_{\max}\vert}$$
in $d$ dimensions ([Dumbser et al. (2014)](/sources/dumbser-2014.md),
eq. 17). ADER-DG and Lax–Wendroff DG are slightly stricter still
([Zanotti et al. (2015)](/sources/zanotti-2015.md), §3.2). This bound
fixes the subcell count of the
[a posteriori subcell limiter](/methods/a-posteriori-subcell-limiting.md).

**Observed order.** ADER-FV with linear reconstruction reaches its
design order from second to seventh on irregular triangles. Up to sixth
order is reached on tetrahedra, with WENO as well
([Dumbser & Käser (2007)](/sources/dumbser-2007.md), Tables 5–8).
ADER-WENO with ADER-CG reaches its order at second to fourth order on
2D and 3D Euler and MHD problems
([Balsara et al. (2009)](/sources/balsara-2009.md), §5). On AMR it
reaches third and fourth order ([Dumbser et al. (2013)](/sources/dumbser-2013.md),
Table 2), and ADER-DG reaches it for $K \le 9$
([Dumbser et al. (2014)](/sources/dumbser-2014.md), Table 2).

**Scope.** Every ADER scheme here is finite volume or DG. This is consistent
with the claim that finite-difference schemes, lacking a volumetric
reconstruction, cannot use ADER predictors
([Lax–Wendroff (Taylor) time discretization](/methods/taylor-time-discretization.md)).

**Later uses (batch 6): a primitive-variable predictor for relativistic MHD.**
([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §3.) To keep
velocities below the speed of light, the predictor evolves the primitive
vector with the four-velocity, in quasi-linear form, with the Jacobians
inverted numerically at each node. Runge–Kutta was rejected because its
internal stages carry no subluminal guarantee. The corrector stays
conservative, so the order is not lost.
* Second order is a Lax–Wendroff step. At third and fourth order the
  predictor is nodal collocation: the spatial modes stay fixed, the PDE is
  enforced at chosen space–time nodes, and the nodes at $t^n$ are
  evaluated once.
* It uses two Picard iterations at third order and three at fourth,
  citing Dumbser et al. (2008). That is $K$ iterations for order $K + 1$,
  against the $K + 1$ reported above for the ADER-CG predictor. The
  predictors differ, so this is a difference of practice, not a
  contradiction.

**Later uses (batch 7).**
* *A third-order toy predictor in 1D* with six space–time nodes and the
  explicit Galerkin relations $\hat u_t = -\hat f_x$, $\hat u_{tt} = -\hat f_{xt}/2$,
  $\hat u_{xt} = -2\hat f_{xx}$ in the predictor's local modes ([Balsara (2017)](/sources/balsara-2017-d.md),
  §V.2, eqs. 58–67), and the 2D analogue (eq. 77).
* *Iteration count.* "For a temporally Nth order scheme, one only needs
  (N-1) steps": two iterations at third order, three at fourth, then a
  final repetition of the nodal flux evaluation (a "polish", Steps 7–8 of
  the stepwise box). The Balsara et al. (2009) statement above says $K + 1$
  iterations for order $K + 1$. *Compiler's reading:* the two counts agree
  if the polish is counted as an iteration; the review does not say so.
* *Time-step table for PNPM* (from Dumbser et al. 2008): limiting 1D CFL
  numbers 1.00, about 0.32, 0.17, 0.10 and 0.069 for evolved degree 0 to 4
  with matched space–time order, divided by the dimension in multi-D
  (§VI).

# Citations

1. [Dumbser & Käser (2007)](/sources/dumbser-2007.md), §§1, 3, 4, 6.
2. [Balsara et al. (2009)](/sources/balsara-2009.md), §§1, 3, 4, 5, 8.
3. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §§1, 2, 5.
4. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §§1, 2.
5. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §§1, 3.
6. [Balsara & Kim (2016)](/sources/balsara-2016-b.md), §§2–3.
7. [Balsara (2017)](/sources/balsara-2017-d.md), §§V, VI.
