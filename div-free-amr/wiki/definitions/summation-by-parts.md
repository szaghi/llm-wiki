---
type: Definition
title: "Summation by parts (SBP)"
description: "Difference operators mimicking integration by parts in a discrete inner product, so continuous energy estimates transfer verbatim to the semi-discretization."
status: established
aliases: [SBP]
tags: [sbp, energy-method, high-order, boundary-closure]
timestamp: 2026-10-08T00:00:00Z
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
* $\mathsf{H}$ doubles as a quadrature — precisely: the diagonal norm of a
  $2p$-order operator is a $2p$-accurate quadrature rule
  ([Del Rey Fernández et al. (2014)](/sources/delreyfernandez-2014.md)).
  This identity carries the modern theory: **dual-consistent**
  discretizations deliver functionals superconvergent at order $2p$
  despite $p$-order boundary closures, and it caps interface-interpolation
  accuracy (the bound circumvented at
  [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md)).
  Defining SBP *through* the quadrature property generalizes the class to
  nodal pseudo-spectral and DG operators under one umbrella.

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

Second derivatives have their own SBP operators
$\mathsf{D}_2 = \mathsf{H}^{-1}(A + \mathsf{B}S)$, $A + A^T \le 0$, built
on the **same norm** as $\mathsf{D}_1$ so mixed problems close under one
energy estimate; minimal-width forms match the first-derivative stencil,
and boundary closures two orders below the interior preserve the design
order ([Mattsson & Nordström (2004)](/sources/mattsson-nordstrom-2004.md)).

## Nullspace consistency and grid oscillations

An SBP derivative is **nullspace consistent** when
$\ker\mathsf{D}_1 = \mathrm{span}\{1\}$: only constants are annihilated.
Its $\mathsf{H}$-adjoint $\mathsf{D}_1^*$ ([notation](/notation.md)) then
has a one-dimensional kernel, spanned by a **grid-oscillation mode** that
alternates $\pm1$ in the interior, with boundary values set by the
closure. These modes are orthogonal to everything $\mathsf{D}_1$ can
produce. In tensor-product form they are exactly what separates the
kernels from the images in collocated discrete vector calculus
([exactness theorems](/results/discrete-exactness-theorems.md);
[Ranocha, Ostaszewski & Heinisch (2020)](/sources/ranocha-2020.md)).

# Citations

1. [Strand (1994)](/sources/strand-1994.md), §1–2.
2. [Nordström & Carpenter (1999)](/sources/nordstrom-carpenter-1999.md), §§4–5.
3. [Mattsson & Nordström (2004)](/sources/mattsson-nordstrom-2004.md), §§2–3.
4. [Del Rey Fernández et al. (2014)](/sources/delreyfernandez-2014.md), §§2, 8–9.

**Convergence rates** are their own theory: the boundary-localized
truncation error is *weakened* rather than dominant, and the size of the
gain is governed by the **determinant condition** (nonsingularity of the
Laplace-space boundary system for $\mathrm{Re}(s)\ge 0$) — two orders when
it holds, but many common closures fail it at $s=0$ and the actual gain
can fall either side of two; energy stability alone certifies only half an
order ([Wang & Kreiss (2017)](/sources/wang-kreiss-2017.md)).

The theory extends to 2D by diagonalization into 1D mode families, with
line-distributed and **corner-localized** truncation errors carrying
different gains
([Wang, Nissen & Kreiss (2017)](/sources/wang-nissen-kreiss-2017.md)) —
the accuracy-side companion of the block-AMR junction-point stability
treatments.

5. [Wang & Kreiss (2017)](/sources/wang-kreiss-2017.md), §§1, 3–4.
6. [Wang, Nissen & Kreiss (2017)](/sources/wang-nissen-kreiss-2017.md), §§1–2.
7. [Ranocha, Ostaszewski & Heinisch (2020)](/sources/ranocha-2020.md), §§2–3.1.
