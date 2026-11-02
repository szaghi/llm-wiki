---
type: Source
title: "Carlino & Boscheri (2024) — Arbitrary-Lagrangian-Eulerian finite volume IMEX schemes for the incompressible Navier–Stokes equations on evolving Chimera meshes"
description: "A second-order finite-volume semi-implicit IMEX Runge–Kutta scheme with an incremental projection for incompressible flow on evolving Chimera meshes, the mesh motion encoded in the numerical flux, a time step limited only by the relative fluid velocity, and compact fringe-to-field transmission by extrapolation on a minimal stencil."
resource: "doi:10.1016/j.jcp.2024.112764"
source_kind: paper
authors: [Carlino M.G., Boscheri W.]
year: 2024
venue: "J. Comput. Phys. 501:112764"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2024_Crossref_Journal_of_Computational_Physics_Carlino_Arbitrary-Lagrangian-Eulerian_finite_volume_IMEX_schemes_for.pdf"
tags: [incompressible, finite-volume, moving-grid, imex]
timestamp: 2026-11-02T15:25:00Z
---

# Summary

Carlino & Boscheri solve incompressible flow on moving Chimera meshes with semi-implicit IMEX Runge–Kutta time stepping: explicit and implicit terms are separated by a flux splitting, the velocity of the moving frame is encoded in the nonlinear flux by integration on moving cells (an arbitrary-Lagrangian–Eulerian finite volume), viscous terms are implicit so the CFL condition involves only the fluid velocity relative to the frame, and an incremental fractional-step projection enforces the divergence-free constraint. Fringe cells follow the donor/receptor paradigm with a compact transmission: extrapolation of available data on a minimal stencil of the other block around each fringe-cell centre ([IMEX time stepping on overlapping grids](/methods/imex-time-stepping-on-overset-grids.md), [incompressible flow](/methods/incompressible-flow-on-overset-grids.md), [moving overset grids](/methods/moving-overset-grid.md)).

# Version read

arXiv preprint 2308.02686v1 (4 August 2023), 32 pages. Read in a targeted way (abstract, introduction, section structure, main results and conclusions closely; derivations and remaining results skimmed): from chunk 4 on, the bundle is compiled in the main session without reader subagents, by the owner's instruction. Claims below are limited to what was read closely.

# Key claims

1. A semi-implicit IMEX finite-volume scheme separates explicit and implicit terms to handle slow and fast scales; second order in time is obtained with semi-implicit IMEX Runge–Kutta schemes combined with a fractional-step projection (Abstract, Conclusions). **Stated**
2. The velocity of the evolving Chimera mesh is encoded in the nonlinear flux through integration on moving cells (Abstract). **Stated**
3. With implicit viscous terms the maximum admissible time step depends only on the fluid velocity relative to the frame, not on the viscous eigenvalues (Abstract). **Stated**
4. Fringe cells use the donor/receptor paradigm with a compact continuous transmission: extrapolation of available data in the minimal stencil of the other block around the fringe-cell centre (Conclusions). **Stated**
5. Second-order accuracy and moving-body applications are shown numerically (Conclusions, numerical section). **Shown**

# Printed slips

None recorded (targeted reading).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| fringe cell, field cell | receptor, discretization point | |
| ALE | arbitrary-Lagrangian–Eulerian | grid velocity $\mathbf u_g$ |

# Reference list

94 references, merged complete into the [bibliography](/bibliography.md) with `citedby` carlino-2024, from the Crossref deposited reference list. [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) and [Bergmann et al. (2022a)](/sources/bergmann-2022.md) are cited.

# Pages created or updated

Chunk 4 (2026-11-02). This source is cited on:

- [ADER schemes on overlapping grids](/methods/ader-on-overset-grids.md)
- [Implicit–explicit time stepping on overlapping grids](/methods/imex-time-stepping-on-overset-grids.md)
- [Incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md)
- [Moving overset grids](/methods/moving-overset-grid.md)
