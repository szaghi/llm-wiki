---
type: Source
title: "Bergmann et al. (2022a) — Second order ADER scheme for unsteady advection–diffusion on moving overset grids with a compact transmission condition"
description: "A space–time finite-volume scheme of ADER type for advection–diffusion on moving Chimera grids, with interpolation polynomials on arbitrarily intersecting space–time cells at block boundaries, a mesh-free predictor and finite-volume corrector, and a space–time local Lax–Friedrichs speed, second order in space and time."
resource: "doi:10.1137/21m1393911"
source_kind: paper
authors: [Bergmann M., Carlino M.G., Iollo A.]
year: 2022
venue: "SIAM J. Sci. Comput. 44:A524-A553"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2022_Crossref_SIAM_Journal_on_Scientific_Computing_Bergmann_Second_Order_ADER_Scheme_for_Unsteady_Advection-Diffusion_on.pdf"
tags: [ader, moving-grid, finite-volume, high-order]
timestamp: 2026-11-02T15:24:00Z
---

# Summary

The advection–diffusion predecessor of [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md): a space–time finite-volume scheme of ADER type on moving Chimera grids. Instead of time-dependent spatial transmission conditions between relatively moving blocks, interpolation polynomials are defined on arbitrarily intersecting space–time cells at the block boundaries, giving a compact stencil for the overlap; a mesh-free finite-element predictor and a finite-volume corrector represent the solution, and a space–time local Lax–Friedrichs stabilization speed accounts for advection and diffusion together. See [ADER schemes on overlapping grids](/methods/ader-on-overset-grids.md) and [moving overset grids](/methods/moving-overset-grid.md).

# Version read

HAL deposit hal-03615757 (author version of the SIAM paper), 28 pages. Read in a targeted way (abstract, introduction, section structure, main results and conclusions closely; derivations and remaining results skimmed): from chunk 4 on, the bundle is compiled in the main session without reader subagents, by the owner's instruction. Claims below are limited to what was read closely.

# Key claims

1. The equations are discretized on a space–time slab; transmission between relatively moving blocks uses interpolation polynomials on arbitrarily intersecting space–time cells at the block boundaries, giving a compact discretization stencil in the overlap (Abstract, §1). **Stated**
2. A mesh-free finite-element predictor and a finite-volume corrector represent the solution (Abstract). **Stated**
3. A new space–time local Lax–Friedrichs stabilization speed accounts for both the advective and the diffusive character of the equation (Abstract). **Stated**
4. On linear and nonlinear test problems, moving background and foreground meshes introduce no spurious perturbation and the scheme reaches second order in space and time uniformly (Abstract, numerical section). **Shown**
5. Several foreground meshes, possibly overlapping each other and moving independently, can be used (Abstract). **Shown**

# Printed slips

None recorded (targeted reading).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| foreground, background mesh | $G_k$ of higher, lower priority | |
| space–time cell | cell of the space–time slab | |

# Reference list

36 references, merged complete into the [bibliography](/bibliography.md) with `citedby` bergmann-2022, from the Crossref deposited reference list (DOIs resolved on Crossref). No printed duplicates detected.

# Pages created or updated

Chunk 4 (2026-11-02). This source is cited on:

- [ADER schemes on overlapping grids](/methods/ader-on-overset-grids.md)
