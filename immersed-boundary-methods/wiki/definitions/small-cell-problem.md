---
type: Definition
title: "Small-cell problem"
description: "The stability defect of explicit cut-cell (embedded-boundary) finite-volume schemes: a cell clipped by the boundary can have an arbitrarily small volume fraction, so a conservative update with a time step set by the full cells is unstable; the remedies are cell merging, redistribution, large-time-step and rotated schemes, and smaller local time steps."
status: established
aliases: [small cell problem, arbitrarily small cells, cut-cell stability]
tags: [cut-cell, embedded-boundary, stability, conservation]
timestamp: 2026-11-08T17:31:00Z
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

# Citations

- [Pember et al. (1995)](/sources/pember-1995.md) — §1, §2.6.
- [Ye et al. (1999)](/sources/ye-1999.md) — §2 (inclusion of immersed boundaries; pressure solver).
