---
type: Source
title: "Bonelle & Ern (2014) — Analysis of compatible discrete operator schemes for elliptic problems on polyhedral meshes"
description: "CDO schemes analyzed: topological laws exact, all error in the discrete Hodge operator, whose two design properties yield optimal energy error estimates on polyhedral meshes."
resource: "doi:10.1051/m2an/2013104"
source_kind: paper
authors: [Bonelle J., Ern A.]
year: 2014
venue: "ESAIM: M2AN 48:553-581"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2014-ESAIM-M2AN-Bonelle-101051m2an2013104.pdf"
tags: [mimetic, hodge, polyhedral, error-analysis, dual-grid, elliptic]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The numerical-analysis maturation of the topology/metric split: **compatible
discrete operator (CDO)** schemes for elliptic problems on polyhedral
meshes localize DOFs by the physical nature of each field, keep topological
laws exact via structure-preserving gradient/divergence, and concentrate
*all* approximation in the **discrete Hodge operator** (sparse, SPD,
assembled cellwise) linking primal to dual quantities. The analysis
identifies **two design properties of the local Hodge operators** that
yield optimal discrete energy error estimates — plus discrete
Sobolev-embedding counterparts for the discrete gradient, an optimal
$L_2$ potential estimate for the barycentric-dual construction, and
explicit links to FE, FV, and mimetic FD.

# Key claims

1. **Error lives only in the closure**: "the only source of error in the
   scheme stems from the discretization of the closure relation" — the
   analysis-grade form of the
   [FIT](/methods/finite-integration-technique.md) observation, now with
   theorems attached: two local Hodge design properties ⟹ optimal energy
   error.
2. **Orientation as the organizing concept**: discrete differential
   operators act between entities of the *same* orientation type
   (inner/inner or outer/outer); the Hodge operator alone crosses
   orientation — which is *why* a dual mesh exists, pairing inner-oriented
   primal edges with outer-oriented dual faces. Primal and dual are not
   symmetric: only the primal mesh is user-visible.
3. **Two placements, one analysis**: vertex-based and cell-based potential
   DOFs both covered; scheme relations to nonconforming FE, FV, and MFD
   made explicit — the frameworks differ in Hodge construction, not
   structure.

# Notation map

| Bonelle & Ern | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| topological laws / closure relations | exact incidence structure / Hodge matrices | FIT split, analyzed |
| discrete Hodge operator | metric/material matrices | SPD, cellwise |
| inner/outer orientation | primal/dual pairing rationale | |

# Pages created or updated

* Updated [Finite integration technique](/methods/finite-integration-technique.md) (CDO as the analysis-grade descendant; two Hodge design properties).

# Citations

1. `~/papers/mosaic/div-free-amr/2014-ESAIM-M2AN-Bonelle-101051m2an2013104.pdf` (doi:10.1051/m2an/2013104) — text extraction, pp. 553–581.
