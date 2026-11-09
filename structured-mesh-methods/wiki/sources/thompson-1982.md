---
type: Source
title: "Thompson, Warsi & Mastin (1982) — Boundary-fitted coordinate systems for numerical solution of partial differential equations — A review"
description: "Comprehensive review of boundary-fitted coordinate generation (conformal, orthogonal, algebraic, elliptic, hyperbolic), line control, adaptive and time-dependent systems, grid-induced truncation error and geometrically conservative forms."
resource: "doi:10.1016/0021-9991(82)90066-3"
source_kind: paper
authors: [Thompson J.F., Warsi Z.U.A., Mastin C.W.]
year: 1982
venue: "J. Comput. Phys. 47(1):1–108"
local_file: "/home/stefano/papers/mosaic/structured-mesh/1982_Crossref_Journal_of_Computational_Physics_Thompson_Boundary-fitted_coordinate_systems_for_numerical_solution_of.pdf"
tags: [review, grid-generation, truncation-error, metric-identities]
timestamp: 2026-11-08T20:27:00Z
---

# Summary

Thompson, Warsi and Mastin review the generation of [boundary-fitted coordinate systems](/definitions/boundary-fitted-coordinate-system.md) by family, with the tensor framework, line-spacing control, adaptive and moving systems, the [truncation error the grid adds](/results/grid-induced-truncation-error.md) and the conservative forms that make discrete [metric identities](/properties/free-stream-preservation.md) hold.

# Version read

Version of record (scan with text layer), J. Comput. Phys. 47, 1–108 (1982). Scoped reading: Sections A, B, O and P read; C–N and Q by structure and keyword. Third author's name corrected from page 1 (Crossref gives Wayne Mastin C.).

# Key claims

1. The metric components measure angle ($g_{12}$), arc length ($\sqrt{g_{ii}}$), cell volume ($J$) and aspect ratio (Section B). **Stated**
2. A central difference on a stretched grid is truly second order only if $x_{\xi\xi}=O(x_\xi^2)$; nonorthogonality adds a $\cot\theta$ term and departures up to $45^\circ$ are tolerable (Section O). **Derived**
3. Conservative derivative forms with numerically differenced metrics vanish for constant data; analytic metrics leave spurious source terms (Section P). **Derived**

# Notation map

| Thompson, Warsi & Mastin (1982) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\sqrt g$ | $J$ |  |
| $g_{ij}$ | $g_{ij}$ |  |
| $\alpha,\beta,\gamma$ | $g_{22}$, $g_{12}$, $g_{11}$ |  |

# Reference list

346 references in the Crossref deposited list, merged complete into the [bibliography](/bibliography.md); the reference extraction covers the whole list although the reading is scoped.

# Pages created or updated

Chunk 1 (2026-11-08). This source is cited on:

- [Boundary-fitted coordinate system](/definitions/boundary-fitted-coordinate-system.md)
- [Elliptic grid generation](/methods/elliptic-grid-generation.md)
- [Hyperbolic grid generation](/methods/hyperbolic-grid-generation.md)
- [Transfinite interpolation](/methods/transfinite-interpolation.md)
- [Free-stream preservation](/properties/free-stream-preservation.md)
- [Geometric conservation law](/properties/geometric-conservation-law.md)
- [Grid-induced truncation error](/results/grid-induced-truncation-error.md)
