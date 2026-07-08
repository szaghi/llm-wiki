---
type: Source
title: "Lipnikov, Manzini & Shashkov (2014) — Mimetic finite difference method"
description: "The comprehensive 50-year review of mimetic discretization: consistency and stability conditions, families of schemes via non-unique inner products, degenerate cells and hanging nodes, higher order."
resource: "doi:10.1016/j.jcp.2013.07.031"
source_kind: paper
authors: [Lipnikov K., Manzini G., Shashkov M.]
year: 2014
venue: "J. Comput. Phys. 257:1163-1227"
local_file: "~/papers/mosaic/div-free-amr/2014-JCP-Lipnikov-101016jjcp201307031.pdf"
tags: [mimetic, review, polyhedral, consistency, stability, discrete-vector-analysis]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

"The first comprehensive review of the 50-year long history of the mimetic
methodology": design principles (mimic conservation, symmetry/positivity,
operator duality/self-adjointness, exact calculus identities), a
periodized history, systematic constructions of the discrete operators on
unstructured polygonal/polyhedral meshes, and the convergence theory —
much of it stated here in generalized polyhedral form. Extensions
demonstrated: higher-order approximations, discrete maximum principles,
saddle-point stability.

**Coverage of this ingestion (scoped):** abstract, §1 (design principles
and history) closely; construction/convergence sections at claim level.

# Key claims

1. **The two-condition architecture**: mimetic inner products are built to
   satisfy a *consistency* condition (S1: exactness on low-order
   polynomials) and a *stability* condition (S2: spectral equivalence) —
   and since these do not determine the product uniquely, MFD yields
   **families of schemes** on each mesh, with free parameters available
   for extra properties (monotonicity, maximum principles).
2. **Degenerate cells done right**: inner products valid for arbitrary
   polygons — 180° angles, zero-length edges, non-convex cells, **cells
   with hanging nodes** — via triangulation with eliminated temporary
   unknowns, depending *continuously* on cell shape; the technical basis
   for treating locally refined and non-matching meshes as ordinary
   polyhedral ones
   ([MFD convergence](/results/mfd-convergence.md)).
3. **Terminology consolidated**: *primary* mimetic operators (natural,
   from integral identities) vs *derived* (duals via inner products) —
   the [support-operator](/definitions/support-operator-method.md)
   pattern; the discrete exactness theorems (div = 0 iff curl) credited to
   the Hyman–Shashkov line as the systematic foundation.
4. **Lineage claim**: mimetic ideas span 50 years and multiple communities
   — the review positions MFD as the continuity of the Soviet-era
   difference-scheme school through modern polyhedral discretization.

# Notation map

| Lipnikov et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| primary / derived operators | $G_h, C_h, D_h$ / adjoint copies | SOM pattern |
| (S1), (S2) | consistency / stability conditions | on mimetic inner products |
| DVTC | discrete vector and tensor calculus | their umbrella term |

# Pages created or updated

* Updated [Support-operator method](/definitions/support-operator-method.md) (S1/S2 architecture; scheme families; degenerate-cell inner products).

# Citations

1. `~/papers/mosaic/div-free-amr/2014-JCP-Lipnikov-101016jjcp201307031.pdf` (doi:10.1016/j.jcp.2013.07.031) — scoped read: §1 closely; remainder at claim level.
