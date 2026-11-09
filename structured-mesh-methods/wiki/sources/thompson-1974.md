---
type: Source
title: "Thompson, Thames & Mastin (1974) — Automatic numerical generation of body-fitted curvilinear coordinate system for field containing any number of arbitrarily shaped two-dimensional bodies"
description: "Elliptic generation of body-fitted coordinates for multiply connected regions with any number of bodies: coordinates as solutions of Laplace or Poisson equations with Dirichlet data, inverted onto a rectangular computational domain, with control functions for line spacing."
resource: "doi:10.1016/0021-9991(74)90114-4"
source_kind: paper
authors: [Thompson J.F., Thames F.C., Mastin C.W.]
year: 1974
venue: "J. Comput. Phys. 15(3):299–319"
local_file: "/home/stefano/papers/mosaic/structured-mesh/1974_Crossref_Journal_of_Computational_Physics_Thompson_Automatic_numerical_generation_of_body-fitted_curvilinear_co.pdf"
tags: [elliptic-generation, multiply-connected, control-functions]
timestamp: 2026-11-08T20:27:00Z
---

# Summary

Thompson, Thames and Mastin generate a [boundary-fitted coordinate system](/definitions/boundary-fitted-coordinate-system.md) for a region with any number of arbitrarily shaped bodies: one coordinate is constant on each contour, branch cuts map to the sides of the rectangular computational domain, and the inverted Laplace or Poisson system is solved for the physical coordinates ([elliptic grid generation](/methods/elliptic-grid-generation.md)). Potential flow about airfoils validates the coordinates.

# Version read

Version of record (scan with text layer; parts of the OCR garbled), J. Comput. Phys. 15, 299–319 (1974). Introduction, transformation and spacing-control sections read; potential-flow results in outline. Authors corrected from page 1 (Crossref gives C. Mastin).

# Key claims

1. Boundary-coincident coordinate lines let boundary conditions be imposed without interpolation, where it is most damaging (introduction). **Stated**
2. Laplace equations in the physical plane, inverted, give a quasilinear elliptic system on a rectangular field for multiply connected regions (transformation section). **Derived**
3. Control terms $\nabla^2\xi^i=P^i$ with positive $P^i$ attract coordinate lines to a contour; solution-dependent $P^i$ are proposed for adaptive coordinates (spacing-control section). **Stated**
4. Stream-function solutions of lifting and nonlifting potential flow about Joukowski and Kármán–Trefftz airfoils agree with the analytic ones (results). **Shown**

# Notation map

| Thompson, Thames & Mastin (1974) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\alpha,\beta,\gamma$ | $g_{22}$, $g_{12}$, $g_{11}$ |  |
| $P$, $Q$ | $P$, $Q$ | control functions |
| natural coordinate system | boundary-fitted coordinate system |  |

# Reference list

6 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list (the printed list has the same 6).

# Pages created or updated

Chunk 1 (2026-11-08). This source is cited on:

- [Boundary-fitted coordinate system](/definitions/boundary-fitted-coordinate-system.md)
- [Elliptic grid generation](/methods/elliptic-grid-generation.md)
- [Hyperbolic grid generation](/methods/hyperbolic-grid-generation.md)
