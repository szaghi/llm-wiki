---
type: Method
title: "Shifted boundary method"
description: "Approximate-domain embedded method that applies boundary conditions on a surrogate boundary made of mesh faces near the true boundary, shifting their values by a Taylor expansion along the distance vector and imposing them weakly with Nitsche's method; no cut cells are integrated, so the small-cut-cell problem does not arise, and high-order versions keep optimal rates with a piecewise-linear surrogate."
status: established
aliases: [SBM, shifted boundary, surrogate boundary method, approximate domain method]
tags: [shifted-boundary, finite-element, nitsche, surrogate-boundary, small-cell, high-order]
timestamp: 2026-11-08T18:22:00Z
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
order $m$ for elements of degree $m$,
$S^m_hu=\sum_{k=0}^{m}\frac{1}{k!}\,\partial^k_{\mathbf d}u$, in the Nitsche terms, pairing
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

# Citations

- [Main & Scovazzi (2018)](/sources/main-2018.md) — §1–§4.
- [Atallah et al. (2022)](/sources/atallah-2022.md) — §1–§6.
- [Collins et al. (2023)](/sources/collins-2023.md) — §1–§5.
