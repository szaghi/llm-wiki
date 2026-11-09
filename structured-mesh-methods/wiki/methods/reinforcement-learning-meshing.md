---
type: Method
title: "Reinforcement-learning mesh generation and adaptation"
description: "Mesh decisions learned by reinforcement learning: multi-agent policies that refine and derefine elements in anticipation of future solution states, and agents that choose structured-mesh parameters for new configurations so that one simulation is grid-converged at a target cost."
status: established
aliases: [DynAMO, anticipatory mesh refinement, deep reinforcement learning meshing, multi-agent reinforcement learning AMR]
tags: [machine-learning, adaptation, grid-generation, reinforcement-learning]
timestamp: 2026-11-08T21:07:00Z
---

# Reinforcement-learning mesh generation and adaptation

Two sources use reinforcement learning to make mesh decisions that
conventional methods take from instantaneous indicators or from repeated
trial simulations.

## Anticipatory refinement

Adaptive refinement for time-dependent problems usually marks elements with
an instantaneous error indicator, so an adapted mesh soon becomes
suboptimal and must be re-adapted often. [Dzanic et al. (2024)](/sources/dzanic-2024.md)
pose dynamic mesh optimization as a decentralized partially observable
Markov decision process: each element is an agent that observes local
information and refines or derefines; observations and rewards are built to
be independent of problem scale and resolution, to exploit the finite
domain of influence of hyperbolic problems over a remesh interval, and to
let the user set error and cost targets at evaluation. The trained policies
anticipate how the solution will move, so meshes stay accurate longer. With
discontinuous Galerkin refinement in mesh size and in polynomial degree for linear advection and the
compressible Euler equations they outperform threshold-based strategies and
generalize to other mesh sizes, remesh intervals, simulation times and
initial conditions.

## Structured-mesh parameters without iteration

Structured meshes for turbomachinery passages depend on parameters
(spacings, growth ratios) that engineers tune by repeated simulation.
[Kim, Chae & You (2025)](/sources/kim-2025.md) train a generator by deep
multi-agent reinforcement learning — 256 agents building meshes and running
simulations on random configurations in parallel — first for shape
parameters, rewarded by geometric quality (ratio of Jacobian determinants,
skewness; [mesh quality metric](/definitions/mesh-quality-metric.md)), then for
resolution parameters, rewarded by accuracy and cost from the flow
solution. The trained generator gives meshes whose single simulation is
grid-converged at the desired cost for new turbine, compressor and impulse
blades, matching conventional iterative optimization.

Related learned generators that solve for the mesh itself are on
[neural-network mesh generation](/methods/neural-network-mesh-generation.md).

## Survey

[Owen et al. (2026)](/sources/owen-2026.md) survey AI along the CAD-to-mesh
pipeline. For structured meshing they note that the hardest step — finding
a valid block decomposition, which is then filled by transfinite
interpolation or pave-and-sweep — is still left to experts; reinforcement
learning decomposes simple 2-D shapes reliably and 3-D ones less
consistently, and learned frame fields guide field-aligned quadrangulation.
AI is presented as complementing, not replacing, established algorithms.

# Citations

- [Dzanic et al. (2024)](/sources/dzanic-2024.md) — abstract, §1, §3.
- [Kim, Chae & You (2025)](/sources/kim-2025.md) — abstract, §1, method.
- [Owen et al. (2026)](/sources/owen-2026.md) — §8, §13.
