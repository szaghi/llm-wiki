---
type: Method
title: "Immersed boundary projection method"
description: "Taira and Colonius's formulation that treats the immersed-boundary forces as Lagrange multipliers of the no-slip constraint, grouped with the pressure, so that one projection of a block-LU fractional step removes both divergence and slip; no gains, no-slip and continuity satisfied exactly at the new time level, symmetric positive-definite systems."
status: established
aliases: [IBPM, IB projection method, Lagrange-multiplier immersed boundary method]
tags: [immersed-boundary, projection, lagrange-multiplier, incompressible, delta-function]
timestamp: 2026-11-08T18:08:00Z
---

# Immersed boundary projection method

In the incompressible Navier–Stokes equations the pressure is the Lagrange
multiplier of the divergence-free constraint. [Taira & Colonius (2007)](/sources/taira-2007.md)
treat the boundary force at the Lagrangian points $\mathbf X_\ell$ in the same way,
as the multiplier of the no-slip constraint $\mathcal J\mathbf u^{n+1}=\mathbf u_\Gamma^{n+1}$
(the idea of the distributed Lagrange multiplier method of Glowinski et al.).
Written on a staggered finite-volume grid with Crank–Nicolson viscous and
Adams–Bashforth convective terms, the discrete system for the velocity (stored as face fluxes) $\mathbf u$,
pressure $\mathbf p$ and force $\tilde{\mathbf f}$ is

$$\begin{pmatrix} A & G & H\\ D & 0 & 0\\ E & 0 & 0\end{pmatrix}\begin{pmatrix}\mathbf u^{n+1}\\ \mathbf p\\ \tilde{\mathbf f}\end{pmatrix}=\begin{pmatrix}\mathbf r^n\\ \mathbf 0\\ \mathbf u_\Gamma^{n+1}\end{pmatrix}+\text{b.c. terms},$$

where $H$ and $E$ are the regularization (spreading) and interpolation
operators built from the 3-point [regularized delta function](/operators/regularized-delta-function.md)
of Roma, Peskin and Berger, scaled so that $E=H^{\mathsf T}$, and $D=G^{\mathsf T}$
(§3). Grouping $\boldsymbol\lambda=(\mathbf p,\tilde{\mathbf f})$ and $Q=[G,\ H]$
gives a Karush–Kuhn–Tucker system of exactly the form of the plain
Navier–Stokes system, which the algebraic fractional step of Perot solves as
a block-LU decomposition:

$$A\mathbf u^*=\mathbf r^n,\qquad Q^{\mathsf T}B^NQ\,\boldsymbol\lambda=Q^{\mathsf T}\mathbf u^*-\mathbf r_2,\qquad \mathbf u^{n+1}=\mathbf u^*-B^NQ\boldsymbol\lambda ,$$

with $B^N$ the $N$-th order Taylor approximation of $A^{-1}$; $N=3$ is
recommended because the splitting error cannot be absorbed into
$\boldsymbol\lambda$ (§3). The modified Poisson system determines pressure and
boundary force together and is symmetric positive-definite, so conjugate
gradients apply.

## Properties claimed

- No constitutive law or gain: CFL numbers up to about one, against
  $O(10^{-3})$–$O(10^{-1})$ for spring and [feedback](/methods/feedback-forcing.md)
  formulations of rigid bodies (§4.1).
- Continuity and no-slip hold exactly at $t^{n+1}$ (to machine precision or a
  prescribed tolerance); [direct forcing](/methods/direct-forcing.md) imposes
  no-slip only on the intermediate velocity, so a slip remains unless the whole
  step is iterated (§4.2).
- One projection removes both the divergent and the slip components, where
  the distributed Lagrange multiplier method applies separate projections
  (§4.4).
- Second order in time; in space the $L^\infty$ error is first order (the delta
  function smears the boundary) and the $L^2$ error about $1.5$ to second order
  (§5) — consistent with the [first-order accuracy of regularized-delta forcing](/results/first-order-accuracy-of-regularized-delta-forcing.md).
- Lagrangian spacing about equal to the grid spacing: too many points make
  $Q^{\mathsf T}B^NQ$ nearly singular, too few let the flow penetrate (§3).
- Validated on [flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
  at $Re=20$, $40$, $200$ and an impulsively started cylinder; not limited to
  rigid bodies (§5).

# Citations

- [Taira & Colonius (2007)](/sources/taira-2007.md) — §1–§5.
