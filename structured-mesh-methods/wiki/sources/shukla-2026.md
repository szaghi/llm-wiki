---
type: Source
title: "Shukla, Hakim, Juno, Hammett & Francisquez (2026) — Constructing field-aligned coordinate systems for gyrokinetic simulations of tokamaks in X-point geometries"
description: "Multi-block field-aligned coordinates for tokamak X-point geometries in which blocks meet at the X-point and no geometric quantity or flux is evaluated at the singular points, for discontinuous Galerkin gyrokinetics."
resource: "doi:10.1017/s0022377826101779"
source_kind: paper
authors: [Shukla A., Hakim A., Juno J., Hammett G.W., Francisquez M.]
year: 2026
venue: "J. Plasma Phys. 92(3):E74"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2026_Crossref_Journal_of_Plasma_Physics_Shukla_Constructing_field-aligned_coordinate_systems_for_gyrokineti.pdf"
tags: [field-aligned, multi-block, plasma, discontinuous-galerkin]
timestamp: 2026-11-08T21:07:00Z
---

# Summary

Shukla et al. build field-aligned [boundary-fitted coordinates](/definitions/boundary-fitted-coordinate-system.md) that pass through magnetic X-points.

# Version read

arXiv:2510.21676v2 (2 November 2025); metadata from the version of record, J. Plasma Phys. 92, E74 (2026). Abstract, §§1–2 and Appendix A by structure read.

# Key claims

1. Field-aligned coordinates are singular at X- and O-points, where the Jacobian vanishes (§1–§2). **Stated**
2. A DG scheme with interior quadrature nodes never evaluates geometry or fluxes at the singular points, so blocks can meet at the X-point (§2). **Stated**
3. Consistency between blocks needs a common flux per face, independent of free-stream consistency (Appendix A). **Derived**

# Notation map

| Shukla, Hakim, Juno, Hammett & Francisquez (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $(\psi,\alpha,\theta)$ | field-aligned coordinates $\boldsymbol\xi$ |  |
| $J_c$ | $J$ |  |

# Reference list

55 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 6 (2026-11-08). This source is cited on:

- [Boundary-fitted coordinate system](/definitions/boundary-fitted-coordinate-system.md)
