---
type: Method
title: "Twilight-zone flow (manufactured solutions)"
description: "Verification by forcing: add to the equations, boundary and interface conditions the residual of a chosen smooth function so that it becomes the exact solution, then measure convergence rates through boundaries and inter-grid interpolation; covers incompressible, compressible, Maxwell, fluid–structure and finite-volume proxy tests on overlapping grids, and unforced exact solutions used the same way."
status: established
aliases: [twilight zone, twilight-zone forcing, method of manufactured solutions, MMS, manufactured solution, forced exact solution, method of analytic solutions]
tags: [benchmark, composite-grid, high-order, incompressible, compressible, maxwell]
timestamp: 2026-11-02T14:54:00Z
---

# Twilight-zone flow (manufactured solutions)

Twilight-zone flow is a way to verify a discretization against a known exact
solution. Choose a smooth function $u_{\mathrm{ex}}(\mathbf x,t)$. Add to the
equations the forcing $\mathbf f$ that makes $u_{\mathrm{ex}}$ an exact
solution, and take boundary and initial data from $u_{\mathrm{ex}}$. Then
compute the error $e=u_{\mathrm{ex}}-u$ on a sequence of grids and fit the
observed rate $\sigma$ in $\lVert e\rVert\propto h^\sigma$.
[Henshaw (1994)](/sources/henshaw-1994.md) (§5.1) describes the method as
forcing the equations "so that the solution equals a chosen function" and,
as recalled there, credits the name to D. Brown (private communication). On
composite overlapping grids the forced solution crosses interpolation
boundaries. The measured rate therefore checks interior stencils, numerical
boundary conditions and [inter-grid interpolation](/methods/inter-grid-interpolation.md)
together. [Henshaw (2006)](/sources/henshaw-2006-b.md) (§10.1) and
[Banks et al. (2016)](/sources/banks-2016.md) (§5.1) call it the "method of
analytic solutions" and identify it with twilight-zone forcing and the
method of manufactured solutions (as recalled there);
[Sharma et al. (2021)](/sources/sharma-2021.md) (§4.1.1) call it the method
of manufactured solutions.

## Practice

- **Exactness test.** Henshaw (§5.1) notes that quadratic polynomials should
  be computed exactly on rectangular grids, which is useful for debugging.
  For the fourth-order Maxwell scheme, polynomials of degree at most 4 must
  be reproduced exactly on Cartesian or overlapping Cartesian grids
  (Henshaw 2006, §10.1).
- **Forcing the interface conditions.** In fluid–structure interaction the
  forcing is added to the fluid and solid equations, the boundary conditions
  and the interface conditions (Banks et al. 2016, §5.1).
- **Incompressible choices.** Henshaw's exact solutions for the
  incompressible equations are as follows. In 2-D, with a page-local
  frequency $\varpi$ (Henshaw's $f$),
  $$\mathbf u_{\mathrm{ex}}=\big(\sin^2(\varpi x)\sin(2\varpi y),\;-\sin(2\varpi x)\sin^2(\varpi y)\big)\cos2\pi t,\qquad p_{\mathrm{ex}}=\sin(\varpi x)\sin(\varpi y)\cos2\pi t .$$
  In 3-D,
  $$\mathbf u_{\mathrm{ex}}=\big(\sin\varpi x\cos\varpi y\cos\varpi z,\;\cos\varpi x\sin\varpi y\cos\varpi z,\;-2\cos\varpi x\cos\varpi y\sin\varpi z\big)\cos2\pi t,\qquad p_{\mathrm{ex}}=\sin\varpi x\sin\varpi y\sin\varpi z\cos2\pi t,$$
  with $\nu=0.05$. Both fields satisfy $\nabla\cdot\mathbf u_{\mathrm{ex}}=0$
  *(compiler check, not in the sources)*.
- **Rate fitting.** Both papers fit $\sigma$ by least squares over the grid
  sequence ([Chesshire & Henshaw (1990)](/sources/chesshire-1990.md), §5.3;
  Henshaw 1994, §5).

## Results on overlapping grids

**Fourth-order incompressible Navier–Stokes** (Henshaw 1994, Tables I–III,
VI–VII). The solver is fourth order in space, with second-order Adams
predictor–corrector time stepping at small $\Delta t$. Max-norm rates
$\sigma$:

| domain | grids | $\varpi$, $t$ | $\sigma$: $\mathbf u$, $p$, $\nabla\cdot\mathbf u$ |
|---|---|---|---|
| unit square | $20^2,30^2,40^2$ | 1, 1 | 3.9, 4.0, 5.6 |
| square rotated by $45^\circ$ | same | 1, 1 | 4.2, 3.5, 5.8 |
| circle of radius 1, overlapping | $35^2\cup55\times11$, $69^2\cup109\times21$ | 1/2, 1 | 4.0, 4.0, 4.3 |
| unit cube | $20^3,30^3$ | 1, 1 | 4.3, 4.4, 5.4 |
| spherical shell $r_{\mathrm{in}}=1/2$, $r_{\mathrm{out}}=1$, two patches | $25^2\times7$ to $49^2\times13$ per patch | 1/4, 0.5 | 4.0, 4.2, 4.2 |

On the unit square the velocity errors are $1.2\times10^{-3}$,
$2.5\times10^{-4}$ and $7.9\times10^{-5}$. The rotated square tests boundary
conditions written in normal and tangential components with an unrotated
exact solution. The circle and the shell are genuine overlapping grids
coupled by quartic interpolation with two receptor lines. They confirm the
[interpolation-order requirement](/results/interpolation-order-requirement.md)
at fourth order.

**Compressible Navier–Stokes, cylinder in a channel**
(Chesshire & Henshaw 1990, §6.4 Test 1, Tables V–VI). The forcing makes
$$\begin{aligned}\rho&=1.5+\cos2\pi x\cos2\pi y\cos2\pi t, & u&=1.25+\cos2\pi x\sin2\pi y\cos2\pi t,\\ v&=\cos\pi x\sin\pi y\cos\pi t, & T&=\cos\pi x\sin2\pi y\cos\pi t\end{aligned}$$
exact. The other data are $Re=50$, $M=0.85$, $Pr=1$, $\gamma=1.4$, a no-slip
cylinder, subsonic inflow and outflow, and symmetry walls. The composite grid
has a background and an annular cylinder grid, refined in the spacing ratio
$2:\sqrt2:1$. Max errors at $t=1$ fall by ratios of 2.0–2.2 per refinement:
$\rho$: 0.52, 0.25, 0.12; $u$: 0.20, 0.093, 0.044. The expected ratio for
second order is 2. This is second-order accuracy of the CGNVT solver,
including interpolation.

**Poisson and model problems** (Chesshire & Henshaw 1990, §5.3, §5.5). The
right side is computed from a chosen exact solution:
$u=\sin\pi x+\cos\pi x+\sin2\pi x+\cos2\pi x$ in 1-D, and
$u=\cos2\pi x\cos2\pi y$ on a 2-D composite grid. These tests established
that one order less of interpolation costs one order of convergence. See the
[interpolation-order requirement](/results/interpolation-order-requirement.md).

**Fourth-order Maxwell** (Henshaw 2006, §10.1, Tables 1–2). The
divergence-free exact fields, with $c_x=\cos\pi x$, $s_x=\sin\pi x$ and so on
(page-local), are
$$(E_x,E_y,H_z)=\big(\tfrac12c_xc_y,\ \tfrac12s_xs_y,\ c_xs_y\big)\cos\pi t,\qquad (E_x,E_y,E_z)=\big(c_xc_yc_z,\ \tfrac12s_xs_yc_z,\ \tfrac12s_xc_ys_z\big)\cos\pi t$$
in 2-D and 3-D. On a cylinder in a channel (Cartesian $61\times61$ plus an
annulus, PEC walls) the max-norm rates at $t=1$ over three grids are 4.40,
3.93 and 4.02 for $E_x$, $E_y$, $H_z$, and 3.94 for the normalized divergence;
on a sphere in a box ($41^3$ plus two orthographic patches) 4.12, 4.26, 4.11
and 3.47. See [Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md).

**Fluid–structure interaction on deforming composite grids** (Banks et al.
2016, §5.1, Figs. 7–8). An "elastic piston": a Saint Venant–Kirchhoff solid
on $[-1,0]\times[0,1]$ next to an ideal gas, with trigonometric exact fields of
amplitude $10^{-2}$ in both domains and the interface forced to move as
$x_1=0.5\,t$. The fluid uses a static background and a deforming
hyperbolic interface grid. Max-norm rates at $t=0.5$, spacings $1/20$ to
$1/160$: $\rho$ 1.95, fluid velocity 2.01 and 2.10, $T$ 1.87, solid
displacement 1.91, solid velocity 2.00, stress 2.02. Because the interface
motion is prescribed, the test checks accuracy but not the stability of the
coupling. See
[fluid–structure interaction on overlapping grids](/methods/fluid-structure-interaction-on-overset-grids.md).

**Finite-volume proxies** (Sharma et al. 2021, §4.1). A diffusion equation
$-\nabla\cdot(\kappa_{\mathrm T}\nabla T)=f_T$ is forced so that
$T_{\mathrm{ex}}=\tfrac{\kappa_{\mathrm T}}4(\cos2\pi x+\cos2\pi y)$, with
$f_T=\kappa_{\mathrm T}^2\pi^2(\cos2\pi x+\cos2\pi y)$ (Eqs. (24)–(25);
$\kappa_{\mathrm T}$ page-local, value not printed), on two overlapping
Cartesian meshes; the exact advected wave
$\sin\pi(x-ct)+\sin\pi(y-ct)$, $c=1/\pi$, serves for linear advection
(Eq. (26)). The tests measure which interpolation order keeps second order;
see [interpolation order and overlap requirements](/results/interpolation-order-requirement.md).

**Exact non-manufactured solutions.** When an exact solution of the unforced
equations exists, it serves the same purpose. Henshaw (1994) (§5.1.1,
Table IV) uses Wannier's Stokes flow past a cylinder near a moving wall, on
two overlapping grids. See
[incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md).
[Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) (§6, Tables 1–2)
verify their moving-grid Euler solver without forcing: a steady Mach 1.5
supersonic expansion over a curved wall gives max-norm rates 1.77–1.95, and
a piston with prescribed motion $-t^4/8$ gives nearly equal errors on one
grid and on a moving grid cutting a hole in a fixed grid, with rates
2.04–2.47. Exact incompressible solutions are the decaying Taylor vortex of
Sharma et al. (2021) (§4.3.1, Eq. (29)) and the Taylor–Green vortex of
[Horne & Mahesh (2021)](/sources/horne-2021.md) (§4.2.1, Eq. (11)), on a
rotated overset patch; see the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md).

## Qualifications

- **Time-step independence.** The tests measure spatial order. Henshaw takes
  $\Delta t$ small enough for time errors to be negligible (§5), and the time
  integrator is second order.
- **Printed rates.** In Henshaw's Table I, the printed pressure rate is 4.0. A
  least-squares fit of the printed errors ($4.1\times10^{-3}$,
  $6.8\times10^{-4}$, $2.1\times10^{-4}$) against $h=1/N$ gives 4.3. The same
  fit reproduces the printed velocity (3.9) and divergence (5.6) rates
  *(compiler check, not in the sources)*. The fitting details are not stated,
  so this is recorded as an unexplained discrepancy, not a corrected value.
- **Grid size.** Chesshire & Henshaw's Table V prints the finest background
  grid as $139\times199$. The stated $2:\sqrt2:1$ spacing ratio and the other
  entries ($70\times50$, $99\times71$) imply about $139\times99$ *(compiler
  check, not in the sources)*.
- **Printed rate in Henshaw (2006).** Table 1's $E_x$ rate is 4.40; the
  least-squares slope of the printed errors on three grids equally spaced in
  $\log h$ is $\log_2(9.1\times10^{-5}/2.2\times10^{-7})/2=4.35$ *(compiler
  check, not in the sources)*. Recorded as unexplained, like the Henshaw
  (1994) case above.
- **Printed slips in Sharma et al. (2021)** *(compiler checks, not in the
  sources)*: the advection equation is printed $\partial_t\phi+c\nabla\cdot\phi=0$
  for a scalar $\phi$; its exact solution satisfies
  $\partial_t\phi+c(\partial_x\phi+\partial_y\phi)=0$. The advection–diffusion
  solution (Eq. (27)) applies the decay $e^{-\kappa_{\mathrm T}\pi^2t}$ to the
  first sine only; both sines must decay for it to solve the equation.
- **Printed slip in Horne & Mahesh (2021)** *(compiler check, not in the
  sources)*: with $u=-\cos2\pi x\sin2\pi y\,e^{-8\pi^2\nu t}$,
  $v=\sin2\pi x\cos2\pi y\,e^{-8\pi^2\nu t}$, the momentum balance gives the
  kinematic pressure $-\tfrac14(\cos4\pi x+\cos4\pi y)e^{-16\pi^2\nu t}$; the
  paper prints $+0.25$.

# Citations

- [Henshaw (1994)](/sources/henshaw-1994.md) — §5.1 (method, name credited to Brown, exact solutions), Tables I–III, VI, VII; §5.1.1 Table IV.
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §5.3 (1-D model, Tables I–II), §5.5 (Tables III–IV), §6.4 Test 1 (Tables V–VI).
- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) — §6, Tables 1–2 (unforced exact solutions on moving overlapping grids).
- [Henshaw (2006)](/sources/henshaw-2006-b.md) — §10.1 (method of analytic solutions, exact fields, polynomial exactness, Tables 1–2).
- [Banks et al. (2016)](/sources/banks-2016.md) — §5.1, Figs. 7–8 (elastic piston).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — §4.1, Eqs. (24)–(27); §4.3.1, Eq. (29).
- [Horne & Mahesh (2021)](/sources/horne-2021.md) — §4.2.1, Eq. (11).
