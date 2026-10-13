---
type: Source
title: "Hirani (2003) — Discrete exterior calculus (PhD thesis, Caltech)"
description: "The thesis form of DEC: discrete-first development (not truncation of smooth calculus), circumcentric duals, and the proliferation of primal/dual operator variants unique to the discrete theory."
resource: "https://thesis.library.caltech.edu/ (CaltechTHESIS; PhD thesis, 2003)"
source_kind: thesis
authors: [Hirani A.N.]
year: 2003
venue: "PhD thesis, California Institute of Technology"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2003-PhDThesis-Hirani-Caltech-DEC.pdf"
tags: [dec, differential-forms, simplicial, dual-grid, thesis]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The thesis underlying
[Desbrun, Hirani, Leok & Marsden (2005)](/sources/desbrun-hirani-2005.md);
the two documents share the core of
[DEC](/definitions/discrete-exterior-calculus.md) (forms as cochains,
circumcentric duals, vector fields, flat/sharp, wedge, Lie derivative),
and this ingestion compiles only what the thesis adds or states more
explicitly than the paper.

**Coverage of this ingestion (scoped):** front matter and abstract read;
body treated as superseded by the 2005 paper except for the
thesis-distinctive points below.

Identifier note: no DOI could be **verified** for this thesis (DataCite
and Crossref queries returned no matching record); the resource field
points to the CaltechTHESIS repository, the canonical archive, rather
than risking a fabricated DOI.

# Key claims

1. **Methodological fork stated explicitly**: two routes to a discrete
   calculus — treat the mesh as approximating a smooth manifold and
   *truncate* the smooth operators, or take the discrete mesh "as the only
   given thing" and build the whole calculus from combinatorial and
   geometric operations, interpolating objects but never the mesh. DEC
   takes the second route — the cleanest statement in the corpus of the
   discrete-first design philosophy.
2. **Operator proliferation is intrinsic**: with primal and dual complexes
   in play, operators multiply into primal–primal, primal–dual (etc.)
   versions — "of course unique to the discrete side"; the continuous
   theory's single operator corresponds to a family discretely, and
   choosing among them is part of scheme design.
3. **Staggered-mesh kinship acknowledged**: "the use of duals is
   reminiscent of the use of staggered meshes in computational mechanics";
   derived formulas repeatedly coincide with existing ones in the
   literature — DEC as the systematization of practices this bundle
   traces to [MAC](/methods/mac-method.md) and
   [Yee](/methods/yee-scheme.md).
4. **General tensors** not developed, only sketched — a recorded boundary
   of the theory.

# Notation map

| Hirani | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| as in [Desbrun et al. (2005)](/sources/desbrun-hirani-2005.md) | see that notation map | thesis and paper share notation |

# Pages created or updated

* Updated [Discrete exterior calculus (DEC)](/definitions/discrete-exterior-calculus.md) (discrete-first philosophy; operator proliferation).

# Citations

1. `~/papers/mosaic/div-free-amr/2003-PhDThesis-Hirani-Caltech-DEC.pdf` — scoped read: front matter/abstract; body deferred to the 2005 paper.
