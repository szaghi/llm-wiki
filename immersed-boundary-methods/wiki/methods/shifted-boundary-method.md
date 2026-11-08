---
type: Method
title: "Shifted boundary method"
description: "Approximate-domain embedded method that applies boundary conditions on a surrogate boundary made of mesh faces near the true boundary, shifting their values by a Taylor expansion along the distance vector and imposing them weakly with Nitsche's method; no cut cells are integrated, so the small-cut-cell problem does not arise, and high-order versions keep optimal rates with a piecewise-linear surrogate."
status: established
aliases: [SBM, shifted boundary, surrogate boundary method, approximate domain method]
tags: [shifted-boundary, finite-element, nitsche, surrogate-boundary, small-cell, high-order]
timestamp: 2026-11-08T18:43:00Z
---

# Shifted boundary method

## Idea

Instead of integrating over the cut part of elements, the shifted boundary
method (SBM) replaces the true domain $\Omega$ by a **surrogate domain**
$\tilde\Omega$ made of whole mesh elements; its boundary $\tilde\Gamma$ is the set of
mesh faces closest to $\Gamma$ ([Main & Scovazzi 2018](/sources/main-2018.md), §2).
A map $\mathcal M:\tilde\Gamma\to\Gamma$, usually the closest-point projection,
defines the distance vector $\mathbf d(\tilde{\mathbf x})=\mathcal M(\tilde{\mathbf x})-\tilde{\mathbf x}=\|\mathbf d\|\,\mathbf n$.
A Dirichlet condition $u=u_D$ on $\Gamma$ is shifted to $\tilde\Gamma$ by a Taylor
expansion,

$$u(\tilde{\mathbf x})+\nabla u(\tilde{\mathbf x})\cdot\mathbf d(\tilde{\mathbf x})\approx u_D\big(\mathcal M(\tilde{\mathbf x})\big),$$

and imposed weakly with Nitsche's method on $\tilde\Gamma$ (penalty $\propto h^{-1}$,
symmetric or unsymmetric forms, an optional tangential-gradient term). Without
the gradient correction the method is only first order (§1, §3). The
assumption $\mathbf n\cdot\tilde{\mathbf n}\ge0$ is read as a geometric-resolution
condition; for a circle on a square grid the angle between $\mathbf n$ and
$\tilde{\mathbf n}$ reaches $45^\circ$ (§2).

## High order

[Atallah et al. (2022)](/sources/atallah-2022.md) use a Taylor expansion of
order $m=k$ for elements of degree $k$,
$S^m_hu=\sum_{j=0}^{m}\frac{1}{j!}\,\partial^j_{\mathbf d}u$, in the Nitsche terms, pairing
the penalty with the first-order operator $S^1_hv$ to obtain an $L^2$ estimate by
duality. Optimal convergence ($h^m$ in $H^1$, $h^{m+1}$ in $L^2$) is retained
although the surrogate boundary is piecewise linear, so neither high-order
body-fitted meshes nor cut-cell quadrature is needed; the geometry need not even
be watertight at scales finer than the grid (§1, §5–§6).

## Analysis

- Poisson, linear elements: both forms are coercive and bounded; Strang's
  second lemma gives first order in the natural energy norm; an $L^2$ bound of
  order $h^{3/2}$ is proved, second order is observed (Main & Scovazzi 2018, §3.4).
- High order: coercivity (Poisson) and a uniform inf–sup condition (Stokes,
  equal-order with pressure stabilization or Taylor–Hood) under an assumption
  bounding $\|\mathbf d\|$ relative to the element size (Atallah et al. 2022, §5).
- Stokes with stabilized equal-order elements: pressure $L^2$ error at the rate
  $1.5$ predicted for stabilized methods (Main & Scovazzi 2018, §4).

## Relation to other methods

Main and Scovazzi (2018, §1) separate *immersed boundary* methods (equations
solved inside and outside, boundary imposed by a forcing, interpretable as
penalty methods, smeared and usually first order) from *embedded boundary*
methods (equations solved only in the physical domain, sharp). The SBM is an
embedded, approximate-domain method; they place the
[ghost fluid method](/methods/ghost-fluid-method.md) among the earliest
approximate-domain methods. Its motivation is the cost and fragility of
[CutFEM](/methods/cutfem.md)-type methods: cut-element geometry and quadrature,
and the ghost penalty, which they find delicate for nonlinear problems and
which enlarges low-order stencils. Atallah et al. (2022, §1) relate it to the
boundary approximations of Bramble, Dupont and Thomée (impractical with
corners) and Bramble and King (needing a distance $O(h^2)$), and to Cockburn and
Solano's transfer paths. Earlier extensions cited there cover
advection–diffusion and Navier–Stokes, hyperbolic conservation laws and
elasticity.

## Penalty-free version

[Collins et al. (2023)](/sources/collins-2023.md) remove the Nitsche penalty
with a formulation inspired by the non-symmetric Nitsche method, prove stability
through an inf–sup estimate and energy-norm convergence of order $h^k$ for
elements of degree $k$, and an $L^2$ estimate half an order suboptimal (optimal
under an extra mesh assumption); numerically $L^2$ converges at $k+1$ for $k=1$–$5$.
For linear elasticity with Neumann conditions the method loses one order,
because stresses are extrapolated by a Taylor expansion of one order lower.

## Compressible Euler flow with shocks

[Zeng, Song & Scovazzi (2025)](/sources/zeng-2025.md) apply the method to the
compressible Euler equations with a stabilized continuous piecewise-linear
finite element method, weakly imposed conditions and entropy- or Lax-type
artificial viscosity. The shifted slip-wall condition expresses
$\mathbf u\cdot\mathbf n=0$ on $\Gamma$ through a Taylor expansion along
$\mathbf d$ with the true normal. On a square with shifted slip walls the
method converges at second order, while a zeroth-order variant ($\mathbf d=0$)
and a computation that only integrates the body-fitted boundary terms on
$\tilde\Gamma$ are at best first order; at comparable resolution the results
match body-fitted computations with or without artificial viscosity, also
for strong shocks meeting the staircase surrogate. Two further uses: shifted
conditions on a body-fitted *polygonal* mesh remove the error of the
polygonal wall, and a Kutta condition on an immersed airfoil is obtained by
extending the camber line beyond the trailing edge as an embedded slip
interface.

## Polynomial correction instead of Taylor terms

[Boscheri & Ciallella (2025)](/sources/boscheri-2025.md) use the
shifted-boundary idea on a body-fitted moving mesh whose straight-sided
boundary $\tilde\Gamma$ approximates a curved wall. Rather than evaluating
the Taylor terms of $S^m_h$ one by one, the whole correction is the
difference of the cell's reconstruction polynomial $u_h$ between the true and
the surrogate point: a Dirichlet value at $\tilde{\mathbf x}\in\tilde\Gamma$ is
imposed as $u_D(\mathcal M(\tilde{\mathbf x}))-[u_h(\tilde{\mathbf x}+\mathbf d)-u_h(\tilde{\mathbf x})]$,
one extra polynomial evaluation per quadrature point. For slip walls the
normal velocity is corrected the same way with the true normal. In a direct
arbitrary Lagrangian–Eulerian finite volume scheme this recovers design order
(up to fourth on moving tetrahedra for Kidder's isentropic compression),
where the uncorrected boundary limits every degree to second order.

# Citations

- [Main & Scovazzi (2018)](/sources/main-2018.md) — §1–§4.
- [Atallah et al. (2022)](/sources/atallah-2022.md) — §1–§6.
- [Collins et al. (2023)](/sources/collins-2023.md) — §1–§5.
- [Zeng, Song & Scovazzi (2025)](/sources/zeng-2025.md) — §1, §3, §4.
- [Boscheri & Ciallella (2025)](/sources/boscheri-2025.md) — §4–§5.
