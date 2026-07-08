---
type: Method
title: "Projection method (divergence cleaning by Poisson solve)"
description: "Removes the divergence of the updated field by solving a Poisson problem and subtracting a gradient; constraint held to solver tolerance."
status: established
aliases: [Hodge projection, divergence cleaning (elliptic)]
tags: [projection, poisson, divergence-constraint]
timestamp: 2026-07-08T00:00:00Z
---

# Projection method

After the base scheme produces a provisional field $B_h^*$, solve
$$D_h^{\mathrm{c}} G_h\, \phi_h = D_h^{\mathrm{c}} B_h^{*},$$
then correct $B_h = B_h^* - G_h \phi_h$, removing the cell-centered discrete
divergence ([notation](/notation.md)) to the tolerance of the Poisson solver.

## Origin

The method is [Chorin (1968)](/sources/chorin-1968.md)'s scheme for
incompressible Navier–Stokes, transplanted to the induction equation:
advance an auxiliary field without the constraint-enforcing gradient, then
perform the **discrete Hodge decomposition**
$u_h^{\mathrm{aux}} = u_h^{n+1} + b^{-1} G_h \phi_h$ with
$D_h u_h^{n+1} = 0$ — keep the divergence-free part, discard the gradient
part into the pressure. Chorin works *collocated* with central $D_h$ and
$G_h$, so his composite Laplacian $D_h^{\mathrm{c}} G_h$ is a five-point
stencil of spacing $2\Delta x$ (the compact staggered alternative is the
[MAC](/methods/mac-method.md) pressure equation, which enforces the same
constraint family through the momentum update rather than as a separate
projection). The existence and uniqueness of the decomposition is inherited
from the well-posedness of the continuous problem. The MHD adaptation
(Brackbill & Barnes) is not yet ingested as a primary source; its modern
assessment is [Tóth (2000)](/sources/toth-2000.md). Within the
[GLM framework](/methods/glm-divergence-cleaning.md) the projection is the
elliptic member of the cleaning family — the limit $\mathcal{D}(\psi) = 0$
of the generalized-Lagrange-multiplier coupling
([Dedner et al. (2002)](/sources/dedner-2002.md)).

## Properties, per [Tóth (2000)](/sources/toth-2000.md)

* **Accuracy is preserved:** the projection scheme is consistent and retains
  the base scheme's order of accuracy *even for discontinuous solutions* —
  proved in the paper against the folklore objection that projecting across
  shocks degrades the solution.
* **Tolerance-, not roundoff-level:** the constraint is enforced to the
  (iterative) Poisson solver's accuracy each time it is applied — a weaker
  guarantee than CT's algebraic invariant, but applied in the more natural
  cell-centered stencil $D_h^{\mathrm{c}}$, and it *removes* initial-condition
  divergence rather than merely preserving it
  ([exact discrete divergence](/properties/exact-discrete-divergence.md)).
* **Global, grid-flexible:** requires a global elliptic solve (CG-type
  iterative methods; parallelizable), and is the only scheme in Tóth's
  comparison applicable to unstructured grids.
* **Cheap in practice:** ≈6% CPU overhead in 2D relative to the base scheme;
  identical to the base scheme whenever $D_h^{\mathrm{c}} B_h^* = 0$ already.
* **Top-ranked:** among the most accurate and reliable schemes across the
  ten-problem comparison (Table IX).

# Citations

1. [Chorin (1968)](/sources/chorin-1968.md), eqs. (3)–(5), (20)–(22).
2. [Tóth (2000)](/sources/toth-2000.md), §5, §7, Table IX.
3. [Dedner et al. (2002)](/sources/dedner-2002.md), §2.
