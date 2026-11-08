---
type: Method
title: "Immersed interface method"
description: "Sharp-interface finite-difference method for problems with discontinuous coefficients, singular sources or prescribed jumps across an interface not aligned with a uniform grid: at irregular points the stencil coefficients and a right-hand-side correction are derived from Taylor expansions about the interface and the jump conditions, giving global second-order accuracy."
status: established
aliases: [IIM, LeVeque–Li method]
tags: [immersed-interface, sharp-interface, elliptic, jump-conditions, finite-difference]
timestamp: 2026-11-08T18:22:00Z
---

# Immersed interface method

[LeVeque & Li (1994)](/sources/leveque-1994.md) consider
$\nabla\cdot(\beta\nabla u)+\kappa_0u=f_0$ on a rectangle with a uniform grid,
where $\beta$, $\kappa_0$ and $f_0$ may jump across an interface $\Gamma$ of
codimension one, $f_0$ may carry a single-layer source
$\int\sigma(s)\delta(\mathbf x-\mathbf X(s))\,ds$ (or a dipole), and jumps
$[u]=w(s)$, $[\beta\,\partial_n u]=g(s)$ may be prescribed. The solution or its
derivatives are then discontinuous across $\Gamma$, and standard differences
across $\Gamma$ are inaccurate. They named the method "the immersed interface
method since it is in the same spirit as Peskin's immersed boundary method
but allows more general interface conditions" (§1); its motivation was a
second-order solver for the incompressible Navier–Stokes equations with
immersed boundaries, where the pressure and the normal derivative of the
tangential velocity jump across $\Gamma$.

## Construction (2-D)

- *Regular points* — the five-point stencil does not straddle $\Gamma$:
  standard centred differences, $O(h^2)$ local truncation error.
- *Irregular points* — choose a point $(x^*,y^*)$ on $\Gamma$ (usually the
  projection of the grid point), rotate to local normal and tangential
  coordinates $(\xi,\zeta)$ (the PDE is invariant under shift and rotation),
  Taylor-expand every stencil value about $(x^*,y^*)$ from its own side,
  and use the jump conditions, differentiated along $\Gamma$, to express all
  "$+$" limits through "$-$" limits.
- Require the coefficient of each of $u^-,u^-_\xi,u^-_\zeta,u^-_{\xi\xi},u^-_{\xi\zeta},u^-_{\zeta\zeta}$
  in the local truncation error to vanish: a $6\times6$ linear system for the
  stencil weights $\gamma_k$, which needs six points — the five-point stencil
  plus the diagonal neighbour nearest $(x^*,y^*)$ — and a right-hand-side
  correction $C_{\mathbf i}$ from the jumps and the source.
- An $O(h)$ truncation error on the irregular points, a set of codimension
  one, suffices for a globally $O(h^2)$ solution (§3).

If $\beta$ is continuous the standard five-point stencil satisfies the
system to $O(h)$, so only the right-hand side changes and fast Poisson solvers
remain usable (§4, §6). The system has a unique solution when
$\beta^-/\beta^+>0$ (proof omitted); the resulting matrix is nearly diagonally
dominant and was solved with line SOR at the optimal Poisson relaxation
parameter (§3).

## Against the discrete delta function

In 1-D the hat function $\varphi(r)=1-|r|$ reproduces the solution of
$u''=c\,\delta(x-x_\Gamma)$ exactly at the grid points (citing Beyer and LeVeque
1992), and in 1-D a singular source can be represented to second order. In 2-D
a right-hand side $f_{\mathbf i}=\sum_\ell\sigma_\ell\,\delta_h(\mathbf x_{\mathbf i}-\mathbf X_\ell)\Delta s$
"does not appear" able to give second order at all points (§1). For a circular
interface with $[\partial_n u]=2$, the discrete-delta solution converges at
first order (error ratio about 2) and the immersed-interface solution at
second order (ratio about 4) (§5, Example 1, Table 1) —
[first-order accuracy of regularized-delta forcing](/results/first-order-accuracy-of-regularized-delta-forcing.md).

Harmonic averaging of a discontinuous $\beta$ has an $O(1)$ local
truncation error at the interface points in 1-D yet is second order "by
fortuitous cancellation"; in 2-D it is not second order (§1.1, §2).

## Results reported

Circle of radius $1/2$ in $[-1,1]^2$: singular source (Example 1),
coefficient jump $\beta^-/\beta^+=1/10$ and a negative ratio with a source
(Example 2), prescribed jumps $[u]$ and $[\partial_n u]$ for the Laplace
equation (Example 3), all second order; a quadratic exact solution is
reproduced to round-off (§5).

## Relation to other methods

[Peskin (2002, §6)](/sources/peskin-2002.md) cites the immersed interface
method as the cure for the first-order interpolation of the
[classical method](/methods/classical-immersed-boundary-method.md) at true
interfaces. [Ye et al. (1999)](/sources/ye-1999.md), §2, contrast it with
their finite-volume cut-cell scheme: a finite-difference method altered near
$\Gamma$ to keep global second order versus a finite-volume method designed
for second order both locally and globally.

## For the Navier–Stokes equations

[Griffith & Patankar (2020)](/sources/griffith-2020.md) describe immersed
interface methods for incompressible flow that impose the jumps in pressure and
in the normal velocity derivative directly (Li and Lai 2001; Kolahdouz et al.
2019, using only the lowest-order jump conditions), with spreading and
interpolation operators that incorporate the jumps. They remove the spurious
interior flow of regularized-delta methods but need more geometry
computations; adjoint pairs of such operators were still lacking.

## Thin porous structures

[Boustani et al. (2022)](/sources/boustani-2022.md) use a higher-order
finite-difference immersed interface method for the compressible
Navier–Stokes equations on adaptive Cartesian grids (NASA LAVA), extended to
membranes thinner than a grid cell — ray–triangle in–out tests, irregular
points per grid direction, weighted least-squares stencils built by graph
walking on the correct side of the sheet — and impose the porosity of parachute
fabric as a Darcy–Forchheimer jump condition across the interface, since the
fabric cannot be resolved as a porous volume; loosely coupled to a shell solver
with contact, it reproduces opening loads of supersonic disk-gap-band parachutes
([fluid–structure coupling](/methods/fluid-structure-coupling.md)).

# Citations

- [LeVeque & Li (1994)](/sources/leveque-1994.md) — §1–§6.
- [Ye et al. (1999)](/sources/ye-1999.md) — §2.
- [Peskin (2002)](/sources/peskin-2002.md) — §6.
- [Griffith & Patankar (2020)](/sources/griffith-2020.md) — jump conditions, benchmarks, future issues.
- [Boustani et al. (2022)](/sources/boustani-2022.md) — §3–§5.
