---
type: Method
title: "Runge–Kutta discontinuous Galerkin method (RKDG)"
description: "Cockburn and Shu's method of lines for conservation laws: a discontinuous piecewise-polynomial (degree K) Galerkin discretization with numerical fluxes at element faces, advanced by an SSP Runge–Kutta method of order K + 1 with a slope limiter after every stage; the limiter is a TVB-corrected minmod on the linear part, applied in local characteristic variables, on rectangles and triangles."
status: established
aliases: [RKDG, Runge-Kutta discontinuous Galerkin, Runge–Kutta DG, Cockburn–Shu DG, TVB slope limiter for DG]
tags: [dg, rkdg, limiter, tvb, unstructured, method-of-lines]
timestamp: 2026-10-13T00:00:00Z
---

# Runge–Kutta discontinuous Galerkin method (RKDG)

**Space discretization** ([Cockburn & Shu (1998)](/sources/cockburn-1998.md), §2.1).
The solution is a polynomial of total degree $K$ in each element, with no
continuity across faces. It is evolved by testing the conservation law
with every polynomial $v$ of degree $K$ on the element and integrating by
parts; in one dimension, with $\mathcal P_i = \sum_{l=0}^{K}\hat u^{(l)}_i P_l(\zeta)$,
$$\frac{d}{dt}\int_{I_i}\mathcal P_i\,v\,dx = \int_{I_i} f(\mathcal P_i)\,v'\,dx - \hat f_{i+1/2}\,v(x_{i+1/2}) + \hat f_{i-1/2}\,v(x_{i-1/2}).$$
In multi-D the face term is an edge integral of a numerical flux
$\hat f(a, b)$ for the normal flux $\mathbf f\cdot\mathbf n$: two-point,
Lipschitz, consistent, conservative, a [monotone flux](/definitions/monotone-flux.md)
in the scalar case and an exact or approximate Riemann solver for systems.
Cockburn and Shu use the Lax–Friedrichs flux
$\hat f(a, b) = \tfrac12\left[\mathbf f(a)\cdot\mathbf n + \mathbf f(b)\cdot\mathbf n - \alpha_{i+1/2}(b - a)\right]$,
with a local speed from the two adjacent element means, or, more
dissipative and more robust near walls with low velocity, density or
pressure, the maximum over a grid line (eq. 2.5, §3.1). Initial data are
the $L^2$ projection. The mass matrix is block diagonal, diagonal for a
locally orthogonal basis (§2.2).

**Order and quadrature** (§§2.1, 3.2). The approximation of
$\nabla\cdot\mathbf f(u)$ is of order $K + 1$ if the edge quadrature is
exact for degree $2K + 1$ and the volume quadrature for degree $2K$. With
$K = 0$ the scheme is a monotone finite-volume scheme, so DG is "a
high-order accurate extension of finite volume, monotone schemes".
Rectangles use Gauss rules in a scaled-Legendre basis; triangles use
edge-midpoint ($K = 1$) or midpoint-and-vertex ($K = 2$) nodal bases, the
latter with a full mass matrix (§§3.2–3.3).

**Time discretization** (§2.2, Table 1). The
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) method of order $K + 1$:
the optimal second-order method with $K = 1$, the optimal third-order one
with $K = 2$, both with $\mathcal C = 1$. Boundary data enter each stage at
its stage time, $t^n + \mathsf c\,\Delta t$ with $\mathsf c = 0, 1$ (RK2) or
$0, 1, \tfrac12$ (RK3). Courant numbers 0.3 ($K = 1$) and 0.18 ($K = 2$)
are used, against 1D von Neumann limits $1/3$ and $1/5$ (§4).

## The limiter

Applied to the initial projection and after every Runge–Kutta stage
(§2.3). Three properties are required (§3.4): a linear function is left
unchanged (accuracy), the element mean is kept (conservation), and the
gradient is not increased (slope limiting).

* **Only the linear part is limited** (§2.3). By assumption, whose
  justification the authors call "still an open problem", spurious
  oscillations are present only if present in the $P^1$ part of the
  solution. If the limiter leaves the $P^1$ part unchanged, nothing is
  changed and the higher moments are kept; otherwise they are discarded
  and the limited $P^1$ function replaces the solution.
* **TVB minmod on rectangles** (§3.4.1, eqs. 3.6–3.7). Each face
  deviation from the mean, $\tfrac12\hat u^{(10)}_{i,j}$ in $x$, is
  replaced by
  $\operatorname{minmod}_M\left(\tfrac12\hat u^{(10)}_{i,j},\ \bar u_{i+1,j} - \bar u_{i,j},\ \bar u_{i,j} - \bar u_{i-1,j}\right)$,
  with threshold $M h_x^2$, and likewise in $y$. The threshold leaves smooth
  extrema alone, where the slopes are $O(h^2)$. "Usually, the numerical
  results are not sensitive to the choice of M in a large range"; all
  their runs use $M = 50$.
* **Characteristic limiting** (§3.4.1). For systems the slope and the two
  mean differences are projected with $L$ of the $x$-Jacobian at the
  element mean, limited componentwise and projected back with $R$
  ([local characteristic decomposition](/methods/characteristic-decomposition.md)).
* **Triangles** (§3.4.2). At each edge midpoint the deviation from the
  mean is limited by $\operatorname{minmod}_M$ against 1.5 times a
  geometrically weighted combination of the mean differences to two
  neighbours. Where the three limited deviations do not sum to zero, the
  positive and negative ones are rescaled so that they do, which keeps
  the mean. Characteristic limiting uses the Jacobian in the direction
  from the barycentre to the edge midpoint.

The limiter of part IV of the series has a proved local maximum principle
on general triangulations; the authors describe this practical one as
simpler and better in practice, and give it no proof (§§1, 3.4).

**Positivity** (§4). On a forward-facing step with triangles and on
[shock diffraction](/benchmarks/shock-diffraction.md) with rectangles,
negative density or pressure appear, and ad hoc conservative rescalings of
the higher moments are added: on rectangles, a bound on the cell minimum of
density or total energy built from the mean and the absolute moments
triggers the scaling; on triangles, edge-midpoint values are lifted to
$10^{-10}$. They are claimed not to degrade the formal accuracy, without
proof. The [scaling limiter](/methods/positivity-preserving-scaling-limiter.md)
of [Zhang & Shu (2010)](/sources/zhang-2010.md) is the later
alternative, conservative, provably admissible and accuracy-preserving.

## Evidence

* *Higher order pays at equal resolution of fine features.* In the
  [double Mach reflection](/benchmarks/double-mach-reflection.md), $K = 2$
  on a mesh half as fine per direction resolves the Mach stems as well as
  $K = 1$, for about 2.1 times less CPU time (8 times fewer space–time
  cells as the paper counts them, at equal Courant number; 4.8 with the
  CFL numbers $\nu = 0.3$ and $0.18$ used); triangles and rectangles perform alike
  ([Cockburn & Shu (1998)](/sources/cockburn-1998.md), §§4–5). No
  convergence-order test is shown there; the order rests on the earlier
  parts of the series.
* *Corner artifacts* on the [forward-facing step](/benchmarks/forward-facing-step.md)
  without corner treatment: an entropy layer and a spurious Mach stem
  that shrink with refinement (Example 4.2).

## Later developments in the corpus

* *WENO limiters.* Flag troubled cells with the TVB limiter, then rebuild
  their moments from WENO point values; with a small $M$ that flags many
  good cells the order of unlimited RKDG is kept, which the TVB limiter
  alone loses ([Qiu & Shu (2005)](/sources/qiu-2005.md);
  [WENO-limited DG](/methods/weno-limited-dg.md)). Qiu and Shu find $M$
  hard to estimate for systems (eqs. 2.4–2.5), while Cockburn and Shu
  report insensitivity "in a large range": different emphases, not
  conflicting tests.
* *Positivity.* Third-order RKDG with the TVB limiter first and the
  scaling limiter second; the positivity limiter lets $M$ be raised far
  above values that otherwise blow up, but the TVB limiter is still
  needed at shocks ([Zhang & Shu (2010)](/sources/zhang-2010.md), §4;
  [positivity preservation](/properties/positivity-preserving.md)).
  Navier–Stokes DG with only the positivity limiter becomes less
  oscillatory once the viscous scales are resolved
  ([Zhang (2017)](/sources/zhang-2017.md), §§1.7, 6).
* *Third order in practice.* Explicit Runge–Kutta needs more stages than
  its order beyond four, and the fourth-order SSP method is complex, so
  RKDG is used up to third order ([Dumbser & Käser (2007)](/sources/dumbser-2007.md), §3.1.1;
  [Zanotti et al. (2015)](/sources/zanotti-2015.md), §1;
  [SSP order barriers](/results/ssp-order-barriers.md)); this is the
  argument for one-step [ADER](/methods/ader.md) DG. Cockburn and Shu stop
  at $K = 2$ with RK3 without discussing why.
* *Robustness.* DG is "less robust in dealing with solutions with strong
  shocks" than WENO because its limiters lag behind
  ([Shu (2009)](/sources/shu-2009.md), §5.1). A priori DG limiters fall
  into artificial viscosity, slope or moment limiters (TVB among them)
  and (H)WENO limiters; the a posteriori alternative recomputes troubled
  cells on a subgrid ([Dumbser et al. (2014)](/sources/dumbser-2014.md), §3.1;
  [a posteriori subcell limiting](/methods/a-posteriori-subcell-limiting.md)).
* *Compact limiting at third order in 2D*, with RKDG and MOOD limiters,
  in [Balsara (2017)](/sources/balsara-2017-d.md), §VI.

**Later uses (batch 18).** *Part II of the series, the 1D framework*
([Cockburn & Shu (1989)](/sources/cockburn-1989.md)), now ingested; the
page above rests on part V.
* *Framework* (§2, eqs. 2.2–2.14). The same weak form for the 1D scalar
  law and any degree $K$, with moments normalized so the zeroth is
  $\bar u_i$, a monotone two-point flux at the interfaces, and a cell-mean
  equation that "resembles a MUSCL type finite difference scheme". The
  interface flux is undefined in the weak form: "It is this freedom which
  gives us a chance to adopt the successful finite difference
  nonoscillatory methodology" (p. 415).
* *The limiter at its source* (eqs. 2.21–2.24). The two face deviations
  $u^-_{i+1/2} - \bar u_i$ and $\bar u_i - u^+_{i-1/2}$ are each replaced by
  $\operatorname{minmod}_M$ of themselves, $\Delta^1\bar u_i$ and
  $\Delta^1\bar u_{i-1}$; the TVB threshold is credited to Shu. For $K = 1$
  this is the part-V rule above, since the face deviation is
  $\tfrac12\hat u^{(1)}_i$ (compiler's conversion).
* *The choice of $M$* (Lemma 2.2, eq. 2.25). $M = \tfrac23\max\vert\partial_{xx}u\vert$,
  the maximum taken in practice over a neighbourhood of the smooth critical
  points of the initial data, or a cell-dependent value "very small except
  near critical points", leaves the accuracy untouched wherever
  $u \in C^2$ with that bound. This is the second-derivative estimate that
  part V and [WENO-limited DG](/methods/weno-limited-dg.md) refer to; part
  V's runs use $M = 50$ without it.
* *Higher moments after limiting: a different recipe from part V*
  (eqs. 2.26–2.27). For $K = 2$ part II limits both face deviations and
  rebuilds $\hat u^{(1)}_i$ and $\hat u^{(2)}_i$ from them (their sum and
  three times their difference, compiler's conversion), so a limited
  $P^2$ moment is kept, not discarded as in part V's $P^1$-part rule. For
  $K \ge 3$ the moments above degree 2 are kept unless the first two
  changed, and then set to zero. Different papers, different limiters: a
  variant, not a contradiction.
* *What is proved* (Lemmas 2.1–2.3, Prop. 2.11). TVD (minmod) or TVB
  ($\operatorname{minmod}_M$) of the cell means, under a forward-Euler
  bound of $\tfrac12$ on $\Delta t/h$ times the sum of the Lipschitz
  constants of $\hat f$ in its two arguments, times the Runge–Kutta CFL
  coefficient 1; TVB of the whole solution; a convergent subsequence; with
  extra limiter arguments, convergence to the entropy solution
  (Lemmas 2.8–2.9), whose constants "must be tuned for each individual
  problem" and which the authors do not use. Order is "in the sense of
  local truncation error"; "In practice, we suggest using the schemes in
  (iii)", the TVB limiter with Lemma 2.2's $M$.
* *Linear stability: sufficient bounds, not sharp limits* (Lemma 2.10,
  eq. 2.35; a qualification of "1D von Neumann limits $1/3$ and $1/5$"
  above). The unlimited scheme with the Runge–Kutta methods above is
  linearly stable under $\nu \le 1/(2K+1)$ for $K = 1, 2$. This is proved
  as a sufficient condition (the $K = 2$ proof "is more technical, and is
  thus omitted"), with no claim that it is sharp, and "We do not know
  whether (2.35) is the correct CFL condition for linear stability when
  [$K \ge 3$]." Forward Euler is linearly unstable at any fixed CFL number.
* *Why third order* (a partial answer to "without discussing why" above).
  Part II proves linear stability only for $K = 1, 2$, and notes that its
  Runge–Kutta form can be made of order $s$ with $s$ stages for
  $s \le 4$ (§2; the paper's $r$ is the stage count).
* *Quadrature* (Remark 2.6). In 1D the volume integral needs error
  $O(h^{2K+2})$: Simpson for $K = 1$, three-point Gauss for $K = 2$;
  Gauss–Lobatto points let the interface fluxes be reused.
* *Boundaries* (§3, Prop. 3.1). At an inflow boundary the interface value
  is the data $g(t)$ and the face deviation is limited also against
  $2(\bar u_0 - g(t))$; at an outflow boundary against the inner mean
  difference only. Both keep TVBM and TVB; the compact stencil makes this
  simpler than wide-stencil finite-difference TVB.
* *The convergence test the part-V runs lack* (§4, Tables 1–4; a
  qualification of "No convergence-order test is shown there" under
  Evidence). Third order ($K = 2$, RK3, Roe flux with entropy fix,
  cell-dependent $M$) on Burgers' equation with
  $u_0 = \tfrac14 + \tfrac12\sin\pi x$ at $t = 0.3$: $L^1$ orders 2.92,
  2.97 and $L^\infty$ orders 2.86, 2.87 from $h = 1/10$ to $1/40$
  (periodic); 2.90, 2.94 and 2.77, 2.78 with inflow/outflow boundaries.
  Away from the shock (0.1 band, $h = 1/40$) the errors stay small after
  it forms, "including at critical and sonic points". The CFL number and
  $M$ are not printed
  ([Burgers shock formation](/benchmarks/burgers-shock-formation.md)).

# Citations

1. [Cockburn & Shu (1998)](/sources/cockburn-1998.md), §§1–5, Table 1, eqs. 2.1–2.5, 3.6–3.7.
2. [Qiu & Shu (2005)](/sources/qiu-2005.md), §§1–3.
3. [Zhang & Shu (2010)](/sources/zhang-2010.md), §4.
4. [Zhang (2017)](/sources/zhang-2017.md), §§1.7, 6.
5. [Dumbser & Käser (2007)](/sources/dumbser-2007.md), §3.1.1.
6. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §1.
7. [Shu (2009)](/sources/shu-2009.md), §5.1.
8. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §3.1.
9. [Balsara (2017)](/sources/balsara-2017-d.md), §VI.
10. [Cockburn & Shu (1989)](/sources/cockburn-1989.md), §§2–4, Lemmas 2.1–2.10, Prop. 2.11, Remarks 2.4–2.6, Tables 1–4.
