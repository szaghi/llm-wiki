---
type: Source
title: "Chorin (1968) — Numerical solution of the Navier-Stokes equations"
description: "Introduces the projection method: advance an auxiliary velocity, then Hodge-decompose it into a discretely divergence-free field plus a discrete pressure gradient."
resource: "doi:10.1090/S0025-5718-1968-0242392-2"
source_kind: paper
authors: [Chorin A.J.]
year: 1968
venue: "Math. Comp. 22:745-762"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1968-MathComp-Chorin-101090S00255718196802423922.pdf"
tags: [projection, incompressible, hodge-decomposition, collocation, implicit]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Introduces the **projection method** for the time-dependent incompressible
Navier–Stokes equations in primitive variables, 2D and 3D. Each step: (i)
advance an auxiliary field $u^{\mathrm{aux}}$ by the momentum equation
*without* the pressure term (implicit ADI variants, since explicit 3D
schemes force $\Delta t < \Delta x^2/6$); (ii) decompose
$u^{\mathrm{aux}} = u^{n+1} + b^{-1} G_h\, p^{n+1}$ with
$D_h u^{n+1} = 0$ — the discrete Hodge decomposition into a
divergence-free part (kept as the new velocity) and a curl-free part (the
pressure gradient). The decomposition is computed by a simultaneous
velocity–pressure relaxation iteration whose form was suggested by the
author's artificial-compressibility method; iterations also supply the
pressure boundary data and enforce the constraint at the boundary.

# Key claims

1. **The projection principle**: $\partial_t u_i + \partial_i p = \mathcal{F}_i u$
   with $\mathcal{F}_i u$ pressure-free; the decomposition of
   $\mathcal{F}_i u$ into divergence-free and curl-free parts "exists and is
   uniquely determined whenever the initial value problem … is well posed."
   The discrete analog gives $D_h u_h^{n+1} = 0$ each step
   ([projection method](/methods/projection-method.md)).
2. **Collocated, wide-stencil operators**: velocities and pressure share
   nodes; $D_h$ and $G_h$ are central differences, so the composite
   $L_h = D_h G_h$ is a five-point Laplacian **on a stencil of spacing
   $2\Delta x_1, 2\Delta x_2$** — the discrete analog of
   $\nabla^2 p = \partial_i\partial_j (u_i u_j) + \partial_j E_j$. (Contrast
   the compact staggered Laplacian of the
   [MAC method](/methods/mac-method.md); the odd–even decoupling of the wide
   collocated operator is not discussed in the paper.)
3. **Constraint to iteration tolerance**: the pressure iteration stops at
   $\max|p^{n+1,l+1} - p^{n+1,l}| \le \epsilon$; the divergence-free
   property of $u^{n+1}$ holds to the accuracy of the converged relaxation,
   in the interior *and on the boundary*.
4. **Stability conjecture**: the overall scheme is conjectured stable
   whenever the auxiliary (Burgers-step) scheme is stable — supported
   numerically, not proved here.
5. **Applications**: test problems plus a three-dimensional thermal
   convection computation; accuracy $O(\Delta t) + O(\Delta x^2)$ with
   $\Delta t = O(\Delta x^2)$ assumed.

# Notation map

| Chorin | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_i$, $p$ at shared nodes | $u_h$, $\phi_h$, collocated | primitive variables |
| $Du$ (difference divergence) | $D_h^{\mathrm{c}} u_h$ | central, collocated |
| $G_i p$ | $G_h \phi_h$ | central, collocated |
| $Lp = DGp$ | $D_h^{\mathrm{c}} G_h \phi_h$ | five-point, $2\Delta x$-spaced stencil |
| $u^{\mathrm{aux}}$ | provisional field $u_h^*$ | pressure-free advance |
| $b\,u^{n+1} - Bu$ | discretization of $\partial_t u$ | multi-level form |

# Pages created or updated

* Updated [Projection method](/methods/projection-method.md) (origin section: Hodge decomposition, collocated operators, iterative enforcement).

# Citations

1. `~/papers/mosaic/div-free-amr/1968-MathComp-Chorin-101090S00255718196802423922.pdf` (doi:10.1090/S0025-5718-1968-0242392-2) — text extraction, pp. 745–762.
