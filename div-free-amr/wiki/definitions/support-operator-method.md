---
type: Definition
title: "Support-operator method (mimetic discretization)"
description: "Discretize one prime operator to satisfy its integral identity exactly; define the remaining operators as its adjoints in discrete inner products."
status: established
aliases: [SOM, mimetic finite differences]
tags: [mimetic, support-operator, adjoint, discrete-vector-analysis]
timestamp: 2026-07-08T00:00:00Z
---

# Support-operator method (mimetic discretization)

The construction discipline of mimetic finite differences
([Hyman & Shashkov (1997)](/sources/hyman-shashkov-1997.md)): choose one
first-order operator as the **prime** operator and discretize it so a
discrete integral identity holds *exactly* — e.g. $D_h$ from the discrete
Gauss theorem, $C_h$ from the discrete Stokes theorem. Then define the
**derived** operators as adjoints in the chosen discrete inner products,
e.g.
$$G_h := -\,D_h^{*},$$
so that the discrete integration-by-parts identity
$(D_h \vec A, \varphi)_{V_h^3} + (\vec A, G_h \varphi)_{V_h^2} = \text{boundary terms}$
holds by construction rather than by verification.

Why the adjoint step is unavoidable: the *natural* operators alone have
mismatched domains and ranges
($G_h: V_h^0 \to V_h^1$ but $D_h: V_h^2 \to V_h^3$,
[notation](/notation.md)) — compound operators like
$\operatorname{div}\operatorname{grad}$, $\operatorname{grad}\operatorname{div}$,
$\operatorname{curl}\operatorname{curl}$ cannot be formed from them.
The adjoints supply the complementary-collocation copies, and they inherit
discrete analogs of the same vector-analysis theorems.

What the method buys, per the source: operators valid on nonuniform,
nonorthogonal, nonsmooth logically-rectangular (and unstructured) grids;
integral identities exact by construction, which is the substrate for
energy estimates, convergence and stability proofs, and constraint
preservation — the finite-difference sibling of
[SBP](/definitions/summation-by-parts.md)'s
mimic-integration-by-parts discipline, with the
[discrete exactness theorems](/results/discrete-exactness-theorems.md) as
its structural payoff.

The method's promises were later made rigorous: on general polyhedral
meshes (nonconvex and degenerate elements included), the mixed-form
mimetic discretization is provably stable with optimal convergence for
both variables —
[MFD convergence](/results/mfd-convergence.md)
([Brezzi, Lipnikov & Shashkov (2005)](/sources/brezzi-lipnikov-shashkov-2005.md)),
with the design criteria (conservation, adjointness, null spaces) serving
as the proof's hypotheses.

The mature form ([Lipnikov et al. (2014)](/sources/lipnikov-2014.md)):
mimetic inner products satisfy a *consistency* condition (S1) and a
*stability* condition (S2), which determine them only up to parameters —
so MFD produces **families of schemes** per mesh, with the freedom spent
on extra properties (maximum principles, monotonicity). Inner products
exist for arbitrarily degenerate polygons — including **hanging-node
cells** — and depend continuously on cell shape, which is what lets local
refinement be absorbed into the polyhedral class rather than treated as
an interface exception.

# Citations

1. [Hyman & Shashkov (1997)](/sources/hyman-shashkov-1997.md), §1, conclusions.
2. [Brezzi, Lipnikov & Shashkov (2005)](/sources/brezzi-lipnikov-shashkov-2005.md), §§4–5.
3. [Lipnikov, Manzini & Shashkov (2014)](/sources/lipnikov-2014.md), §§1–2.
