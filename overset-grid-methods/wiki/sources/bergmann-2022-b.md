---
type: Source
title: "Bergmann et al. (2022b) — ADER scheme for incompressible Navier–Stokes equations on overset grids with a compact transmission condition"
description: "Extends a second-order ADER-type space–time finite-volume scheme on moving overset grids to the two-dimensional incompressible Navier–Stokes equations, with a compact hybrid stencil that couples the grids through fluxes rather than fringe interpolation, verified on cavity, cylinder and sedimentation problems."
resource: "doi:10.1016/j.jcp.2022.111414"
source_kind: paper
authors: [Bergmann M., Carlino M.G., Iollo A., Telib H.]
year: 2022
venue: "J. Comput. Phys. 467:111414"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2022_Crossref_Journal_of_Computational_Physics_Bergmann_ADER_scheme_for_incompressible_Navier-Stokes_equations_on_ov.pdf"
tags: [incompressible, ader, moving-grid, finite-volume, conservation]
timestamp: 2026-11-02T15:03:00Z
---

# Summary

Bergmann et al. extend their second-order ADER-type space–time finite-volume scheme for advection–diffusion on moving overset grids to incompressible flow, with a Chorin–Temam projection on collocated variables. The two grids are coupled by a **compact transmission condition**: a hybrid stencil built from the first layer of cells around each fringe cell, taking cells of the other grid where its own grid has none, so that information crosses the overlap through finite-volume fluxes instead of [fringe interpolation](/methods/inter-grid-interpolation.md); interpolation is needed only when a hole cell becomes active. It is the subject of [ADER schemes on overlapping grids](/methods/ader-on-overset-grids.md). Tests: [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) on a rotating grid, [lid-driven cavity](/benchmarks/lid-driven-cavity.md), steady, impulsively started and stopped [cylinders](/benchmarks/flow-past-circular-cylinder.md), and a sedimenting cylinder handled with a penalization term ([incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md), [immersed boundaries](/methods/immersed-boundary-on-overset-grids.md)).

# Version read

Version of record (Elsevier typeset), 27 pages, all read. Page 1 matches the Crossref record.

# Key claims

1. The scheme is second order in space and time for velocity and pressure: $L^2$ rates about 2 on the Taylor–Green vortex with a rotating perturbed foreground grid; the $L^\infty$ error shows no definite rate, which the authors attribute to a small number of cell centres (§5.1, Fig. 8). **Shown**
2. Fringe cells exchange no interpolated data: the predictor is local and the corrector's hybrid stencil makes the fluxes carry information between grids; interpolation is needed only when a hole cell becomes active (§1, §4.1.2, §4.4). **Stated**
3. The hybrid stencil uses the first layer of surrounding cells, completed with cells of the other grid (Algorithm 1); the algorithm may fail for widely different spacings, for which remedies are suggested but not tested (§2.1). **Stated**
4. Hole cutting: background cells whose centres lie inside the surface of the foreground cells $n=5$ layers from its outer boundary are inactive (§2, §2.1). **Stated**
5. In the no-shift configuration on uniform Cartesian grids (Definition 4.1) the fringe scheme reduces to the interior diamond formula, so fluxes are conservative in that limit; the text says this can be proved, and no proof is printed (§4.2.2). **Stated**
6. Conservative overset interpolations are called less attractive because cumbersome in 3-D and, even when globally conservative, not locally conservative (§1). **Stated**
7. Lid-driven cavity at $Re=1000$ ($h=1/128$): $\psi_{\max}=0.1171$ against 0.1179 in the references (Table 1). **Shown**
8. Cylinder at $Re=200$: $C_D=1.3430$, $St=0.1979$, within the literature ranges (Table 3); impulsively started and stopped cylinders at $Re=40$, 200, 550 agree with references (Figs. 13–17). **Shown**
9. At equal accuracy the overset grid uses about $10^4$ cells against $10^5$–$10^6$ degrees of freedom in the compared studies; the sedimenting cylinder uses 9267 cells (§5.3.3, §6). **Shown**
10. The authors state that they solve the incompressible Navier–Stokes equations with an ADER-type scheme for the first time (§7). **Stated**

# Printed slips

- The Taylor–Green pressure is printed with $\sin2y$; the printed velocity field requires $\cos2y$ *(compiler check, not in the sources)*.
- Eq. (42) prints the $\partial_{xx}$ term twice (the second should be $\partial_{yy}$); Eq. (40) prints the mixed third-order coefficients as $1/4$ where the Taylor coefficient is $1/2$; Eqs. (35)–(36) carry the opposite sign to Eqs. (10), (39), (49); Eq. (48) states a $10\times10$ identity acting on a longer vector.
- The extended domain $(0,2)\times(-1,2)$ does not contain the cylinder's initial position $(1,4)$.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| foreground, background grid | $G_k$ of higher, lower priority | |
| fringe cell | receptor | coupled through fluxes, not interpolated |
| no-shift configuration | coincident cell faces of the two grids at the overlap | Definition 4.1 |
| $\varepsilon$ | relaxation parameter of the space–time predictor | page-local on the ADER page |

# Reference list

71 printed references, numbered, merged complete into the [bibliography](/bibliography.md) with `citedby` bergmann-2022-b. Ref. [36], the advection–diffusion paper, is `bergmann-2022` (SIAM J. Sci. Comput.), a later chunk of this bundle. Two Starius 1977 papers are keyed by publication order; Volkov's translation is merged into `volkov-1968`. No printed duplicates.

# Pages created or updated

Chunk 3 (2026-11-02). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Lid-driven cavity](/benchmarks/lid-driven-cavity.md)
- [Taylor–Green vortex (two-dimensional exact decaying solution)](/benchmarks/taylor-green-vortex.md)
- [Fringe (receptor) points and overlap width](/definitions/fringe-point.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [ADER schemes on overlapping grids](/methods/ader-on-overset-grids.md)
- [Conservative overset interface](/methods/conservative-overset-interface.md)
- [Fluid–structure interaction on overlapping grids](/methods/fluid-structure-interaction-on-overset-grids.md)
- [High-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md)
- [Hole cutting](/methods/hole-cutting.md)
- [Immersed boundaries on overlapping grids](/methods/immersed-boundary-on-overset-grids.md)
- [Incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Interpolation-free overset coupling](/methods/interpolation-free-overset-coupling.md)
- [Moving overset grids](/methods/moving-overset-grid.md)
