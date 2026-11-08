---
type: Source
title: "Agrawal, Kulachenko, Scapin, Tammisola & Brandt (2024) — An efficient isogeometric/finite-difference immersed boundary method for the fluid–structure interactions of slender flexible structures"
description: "Partitioned fluid–structure interaction of slender flexible rods: geometrically exact Cosserat rods in isogeometric analysis coupled by direct forcing to a staggered finite-difference flow solver, with Lagrangian markers generated in the spline parameter space independently of the structural mesh."
resource: "doi:10.1016/j.cma.2023.116495"
source_kind: paper
authors: [Agrawal V., Kulachenko A., Scapin N., Tammisola O., Brandt L.]
year: 2024
venue: "Comput. Methods Appl. Mech. Eng. 418:116495"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2024_Crossref_Computer_Methods_in_Applied_Mechanics_and_Engineering_Agrawal_An_efficient_isogeometricfinite-difference_immersed_boundary.pdf"
tags: [fluid-structure-interaction, direct-forcing, isogeometric, slender-structure]
timestamp: 2026-11-08T18:35:00Z
---

# Summary

Agrawal et al. couple a geometrically exact Cosserat rod model discretized by isogeometric analysis to an incompressible finite-difference solver on a staggered Cartesian grid through [direct forcing](/methods/direct-forcing.md). The structural resolution is decoupled from the fluid grid: Lagrangian markers are placed uniformly in the NURBS parameter space at about the fluid grid spacing and [spreading and interpolation](/operators/spreading-and-interpolation.md) act on them. The scheme targets many-filament [fluid–structure coupling](/methods/fluid-structure-coupling.md) at low cost.

# Version read

Accepted manuscript from the Politecnico di Torino repository; metadata from the version of record, Comput. Methods Appl. Mech. Eng. 418, 116495 (2024). §§1–3 read, validations in outline.

# Key claims

1. Uniform Lagrangian markers generated dynamically in the NURBS parameter space decouple the structural discretization from the Eulerian grid (§2–§3). **Stated**
2. Selective reduced integration removes shear locking in the rod elements (§2). **Stated**
3. Explicit partitioned coupling is used for efficiency with many structures; strong iterative coupling is judged too costly (§3). **Stated**
4. The scheme reproduces a 2D flexible filament in uniform flow and a 3D array of filaments in pulsating channel flow (validation). **Shown**

# Notation map

| Agrawal, Kulachenko, Scapin, Tammisola & Brandt (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| NURBS parameter $\xi$ | curve parameter of the structure | page-local |
| Lagrangian markers | $\mathbf X_\ell$ |  |

# Reference list

104 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 5 (2026-11-08). This source is cited on:

- [Fluid–structure coupling in immersed boundary methods](/methods/fluid-structure-coupling.md)
