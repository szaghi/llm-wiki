---
type: Definition
title: "Summation by parts (SBP)"
description: "Difference operators mimicking integration by parts in a discrete inner product, so continuous energy estimates transfer verbatim to the semi-discretization."
status: established
aliases: [SBP]
tags: [sbp, energy-method, high-order, boundary-closure]
timestamp: 2026-07-08T00:00:00Z
---

# Summation by parts (SBP)

A difference operator $\mathsf{D}_1 = \mathsf{H}^{-1}\mathsf{Q}$
approximating $d/dx$ has the **SBP property** with respect to the discrete
inner product $(u,v)_h = u^T \mathsf{H} v$ ($\mathsf{H}$ SPD,
[notation](/notation.md)) when
$$(u, \mathsf{D}_1 v)_h + (\mathsf{D}_1 u, v)_h = \left[u v\right]_{\partial},$$
i.e. $\mathsf{Q} + \mathsf{Q}^T$ collapses to boundary terms — on the
semi-infinite line, $(u, \mathsf{D}_1 v)_h = -(\mathsf{D}_1 u, v)_h - u_0 v_0$,
equivalently $(u, \mathsf{D}_1 u)_h = -\tfrac12 u_0^2$
([Strand (1994)](/sources/strand-1994.md), eqs. 8–9, after Kreiss–Scherer).

This is the exact discrete mirror of integration by parts: for a
semibounded PDE, the continuous energy estimate
$\partial_t \|u\|^2 \le 0$ transfers *verbatim* to the semi-discretization,
giving stability by the energy method — with the boundary terms exposed
explicitly, where boundary conditions can then be imposed stably.

## Structure

* **Interior**: a centered antisymmetric stencil of order $2s$; the SBP
  constraint lives entirely in the **boundary closure** (a
  $(2\tau)\times(3\tau)$-sized block, order $\tau$) and the norm.
* **Norm classes** ([Strand (1994)](/sources/strand-1994.md)): *diagonal*
  ($\mathsf{H} = \mathrm{diag}(\lambda_i) > 0$), *full* (SPD boundary
  block), *restricted full* (first point decoupled). The class controls
  both the achievable boundary order and — decisively — for first-order
  hyperbolic *systems*, provable stability exists only for diagonal norms
  ([families and orders](/results/sbp-operator-existence.md)).
* $\mathsf{H}$ doubles as a quadrature: the SBP inner product is the
  discrete $L_2$ norm in which energy estimates hold.

Within this corpus, SBP is the finite-difference route to *provably stable
high-order* one-dimensional building blocks; its relevance to the
divergence-constraint problem is that any high-order FD divergence/gradient
pair inherits its stability theory from operators of this class.

Boundary and interface conditions are imposed weakly by the
[SAT technique](/methods/sbp-sat.md); the framework extends to multi-block
curvilinear grids with conservation and strict stability **conditional on
discrete metric conditions**
([Nordström & Carpenter (1999)](/sources/nordstrom-carpenter-1999.md)) —
the Jacobian enters the norm, and non-smooth meshes put the metric terms on
the critical path.

# Citations

1. [Strand (1994)](/sources/strand-1994.md), §1–2.
2. [Nordström & Carpenter (1999)](/sources/nordstrom-carpenter-1999.md), §§4–5.
