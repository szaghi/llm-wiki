---
type: Method
title: "Twilight-zone flow (manufactured solutions)"
description: "Verification by forcing: add to the equations the residual of a chosen smooth function so that it becomes the exact solution, then measure convergence rates through boundaries and inter-grid interpolation; covers Henshaw's trigonometric incompressible solutions and Chesshire and Henshaw's compressible Navier–Stokes and Poisson tests."
status: established
aliases: [twilight zone, twilight-zone forcing, method of manufactured solutions, MMS, manufactured solution, forced exact solution]
tags: [benchmark, composite-grid, high-order, incompressible, compressible]
timestamp: 2026-11-02T11:28:00Z
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
together.

## Practice

- **Exactness test.** Henshaw (§5.1) notes that quadratic polynomials should
  be computed exactly on rectangular grids, which is useful for debugging.
- **Incompressible choices.** Henshaw's exact solutions for the
  incompressible equations are as follows. In 2-D, with a page-local
  frequency $\kappa$ (Henshaw's $f$),
  $$\mathbf u_{\mathrm{ex}}=\big(\sin^2(\kappa x)\sin(2\kappa y),\;-\sin(2\kappa x)\sin^2(\kappa y)\big)\cos2\pi t,\qquad p_{\mathrm{ex}}=\sin(\kappa x)\sin(\kappa y)\cos2\pi t .$$
  In 3-D,
  $$\mathbf u_{\mathrm{ex}}=\big(\sin\kappa x\cos\kappa y\cos\kappa z,\;\cos\kappa x\sin\kappa y\cos\kappa z,\;-2\cos\kappa x\cos\kappa y\sin\kappa z\big)\cos2\pi t,\qquad p_{\mathrm{ex}}=\sin\kappa x\sin\kappa y\sin\kappa z\cos2\pi t,$$
  with $\nu=0.05$. Both fields satisfy $\nabla\cdot\mathbf u_{\mathrm{ex}}=0$
  *(compiler check, not in the sources)*.
- **Rate fitting.** Both papers fit $\sigma$ by least squares over the grid
  sequence ([Chesshire & Henshaw 1990](/sources/chesshire-1990.md), §5.3;
  Henshaw 1994, §5).

## Results on overlapping grids

**Fourth-order incompressible Navier–Stokes** (Henshaw 1994, Tables I–III,
VI–VII). The solver is fourth order in space, with second-order Adams
predictor–corrector time stepping at small $\Delta t$. Max-norm rates
$\sigma$:

| domain | grids | $\kappa$, $t$ | $\sigma$: $\mathbf u$, $p$, $\nabla\cdot\mathbf u$ |
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

**Exact non-manufactured solutions.** When an exact solution of the unforced
equations exists, it serves the same purpose. Henshaw (1994) (§5.1.1,
Table IV) uses Wannier's Stokes flow past a cylinder near a moving wall, on
two overlapping grids. See
[incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md).

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

# Citations

- [Henshaw (1994)](/sources/henshaw-1994.md) — §5.1 (method, name credited to Brown, exact solutions), Tables I–III, VI, VII; §5.1.1 Table IV.
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §5.3 (1-D model, Tables I–II), §5.5 (Tables III–IV), §6.4 Test 1 (Tables V–VI).
