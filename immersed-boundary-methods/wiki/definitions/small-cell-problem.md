---
type: Definition
title: "Small-cell problem"
description: "The stability defect of explicit cut-cell (embedded-boundary) finite-volume schemes: a cell clipped by the boundary can have an arbitrarily small volume fraction, so a conservative update with a time step set by the full cells is unstable; the remedies are cell merging, redistribution, large-time-step and rotated schemes, and smaller local time steps."
status: established
aliases: [small cell problem, arbitrarily small cells, cut-cell stability]
tags: [cut-cell, embedded-boundary, stability, conservation]
timestamp: 2026-11-08T18:43:00Z
---

# Small-cell problem

In a [cut-cell method](/methods/cut-cell-method.md) the boundary $\Gamma$
clips Cartesian cells into irregular control volumes whose volume fraction
$\kappa_{\mathbf i}$ can be arbitrarily close to zero. A conservative
finite-volume update divides the net flux by the cell volume
$\kappa_{\mathbf i}h^d$, so an explicit scheme stable for full cells under a
CFL condition on $h$ is unstable in a cell with small $\kappa$ unless $\Delta t$
shrinks with $\kappa$. Because $\kappa$ is set by the geometry, not by the
user, the admissible $\Delta t$ for the whole computation could become
arbitrarily small. Pember et al. (1995, §1) state the design problem as
maintaining "accuracy, stability, and conservation in the irregular cells …
while using a time step restricted by CFL considerations using the regular cell
size alone".

## Remedies named in the founding papers

| remedy | idea | where |
|---|---|---|
| cell merging | absorb a small cut cell into a neighbour so every control volume is large | Ye et al. (1999, §2): cut pieces whose centre lies in the body are absorbed into neighbours, giving trapezoidal cells; Pember et al. (1995, §1) cite Chiang et al., Bayyuk et al. and Quirk; Coirier and Powell found merging more efficient than local time stepping |
| redistribution | take a stable non-conservative update in the cut cell and give the conservation deficit to its neighbours | [redistribution](/methods/redistribution.md), Pember et al. (1995, §2.6), after Chern and Colella |
| large-time-step / rotated schemes | let waves cross small cells in one step (LeVeque), or difference along a rotated stencil (Berger and LeVeque) | cited by Pember et al. (1995, §1): globally second order, between first and second order at the boundary |
| smaller local time steps | advance small cells with their own $\Delta t$ | cited by Pember et al. (1995, §1) from Coirier and Powell |

Implicit cut-cell schemes for incompressible flow face the same geometry as a
conditioning problem instead: the irregular cells destroy the diagonal
dominance of the pressure operator and slow the iterative solver
([Ye et al. 1999](/sources/ye-1999.md), §2).

## Quantified, and its counterparts

[Colella et al. (2006)](/sources/colella-2006.md), §2, state the constraint
of an explicit conservative update as $\Delta t=O\big(h\,\kappa_{\max}^{1/D}/v_{\max}\big)$, with
$D$ the dimension and $v_{\max}$ the maximum wave speed, and list merging,
special stencils (h-box) and algebraic redistribution as the cures.
[Ghias et al. (2007)](/sources/ghias-2007.md), §1, note that the problem
combines arbitrarily small cells with high inviscid velocities in them, and
that a [ghost-cell method](/methods/ghost-cell-method.md) avoids it because
cell sizes are not changed by the boundary. In finite elements the same
geometry makes the system matrix ill conditioned and the Nitsche formulation
unstable when a cut element barely intersects the domain; [CutFEM](/methods/cutfem.md)
removes it with a ghost penalty ([Burman et al. 2015](/sources/burman-2015.md), §3).

## Later remedies

[State redistribution](/methods/state-redistribution.md) postprocesses the
states of an unstable full-time-step update through overlapping merged
neighbourhoods and is second order at the cut cells, where
[flux redistribution](/methods/redistribution.md) is first order
([Berger & Giuliani 2021](/sources/berger-2021.md), §1). The
[shifted boundary method](/methods/shifted-boundary-method.md) avoids cut cells
altogether by moving the boundary condition to a surrogate boundary of whole
elements ([Main & Scovazzi 2018](/sources/main-2018.md), §1), which they
contrast with the costs of cut-element quadrature and ghost penalties.

## In immersed finite elements: stability versus conditioning

[de Prenter et al. (2023)](/sources/deprenter-2023.md) separate two effects
of small cut elements in unfitted finite elements. **Stability**: the Nitsche
parameter needed for coercivity grows without bound as a cut element thins,
weakening the bound of the operator norm and producing large gradients.
**Conditioning**: the equivalence between the coefficient norm and the
operator norm weakens, eigenvalues approach zero, and the condition number
grows as an inverse power of the smallest volume fraction that increases with
the polynomial order (the shape of the cut matters less). Their remedies are
(additive) Schwarz preconditioning, aggregation of badly cut elements onto
interior ones (AgFEM) and the ghost penalty of [CutFEM](/methods/cutfem.md),
which they analyse in a unified way; boundary formulations that avoid Nitsche's
penalty, such as the [shifted boundary method](/methods/shifted-boundary-method.md),
sidestep the stability problem at other costs.

For cut-cell discontinuous Galerkin schemes, [Giuliani (2022)](/sources/giuliani-2022.md)
extends [state redistribution](/methods/state-redistribution.md); for
dimensionally split high-order finite differences, [Sharan et al. (2022)](/sources/sharan-2022.md)
build boundary stencils that are stable at CFL 0.5 for any cut distance; and
[Xie et al. (2022)](/sources/xie-2022.md) avoid the problem with implicit time
stepping.

## Two further remedies

[Taylor, Wilcox & Chan (2025)](/sources/taylor-2025.md), §1.1, survey the
remedies by family: implicit or explicit–implicit time stepping and
subcycling; penalties built into the discretization (jump penalization, the
domain-of-dependence method); flux-based fixes (h-box methods, flux
redistribution); cell merging and cell linking; and
[state redistribution](/methods/state-redistribution.md).
[Jones, McNally & Reynolds (2026)](/sources/jones-2026.md) use the
Forrer–Jeltsch cut-cell scheme, which computes every flux on the full
Cartesian faces and does not treat a cut cell as smaller than its full
volume: the time step is not restricted, at the cost of local conservation
errors in the boundary cells.

# Citations

- [Pember et al. (1995)](/sources/pember-1995.md) — §1, §2.6.
- [Ye et al. (1999)](/sources/ye-1999.md) — §2 (inclusion of immersed boundaries; pressure solver).
- [Colella et al. (2006)](/sources/colella-2006.md) — §2.
- [Ghias et al. (2007)](/sources/ghias-2007.md) — §1.
- [Burman et al. (2015)](/sources/burman-2015.md) — §3.
- [Main & Scovazzi (2018)](/sources/main-2018.md) — §1.
- [Berger & Giuliani (2021)](/sources/berger-2021.md) — §1.
- [Sharan et al. (2022)](/sources/sharan-2022.md) — §3–§5.
- [Xie et al. (2022)](/sources/xie-2022.md) — §1.
- [Giuliani (2022)](/sources/giuliani-2022.md) — §1.
- [de Prenter et al. (2023)](/sources/deprenter-2023.md) — §2–§4.
- [Taylor, Wilcox & Chan (2025)](/sources/taylor-2025.md) — §1.1.
- [Jones, McNally & Reynolds (2026)](/sources/jones-2026.md) — §1, §3.
