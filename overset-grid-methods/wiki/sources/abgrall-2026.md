---
type: Source
title: "Abgrall et al. (2026) — Dual formulation finite-volume methods on overlapping meshes for hyperbolic systems of conservation laws"
description: "Second-order schemes for hyperbolic conservation laws that evolve the conservative and a primitive (nonconservative) formulation on two overlapping staggered finite-volume meshes, the primitive solution supplying simple fluxes for the conservative one, with a post-processing that ensures nonlinear stability and a conservative coupling of the two sets of variables."
resource: "doi:10.1016/j.compfluid.2025.106952"
source_kind: paper
authors: [Abgrall R., Chertock A., Kurganov A., Micalizzi L.]
year: 2026
venue: "Comput. Fluids 307:106952"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2026_Crossref_Computers_amp_Fluids_Abgrall_Dual_formulation_finite-volume_methods_on_overlapping_meshes.pdf"
tags: [finite-volume, conservation, shock-capturing]
timestamp: 2026-11-02T15:41:00Z
---

# Summary

"Overlapping meshes" here are two staggered finite-volume meshes of one discretization, not overset component grids. Abgrall et al. evolve cell averages of the conservative variables on one mesh and of primitive variables (a formulation with nonconservative products, discretized by a path-conservative central-upwind scheme) on the other; the primitive solution supplies very simple numerical fluxes for the conservative system, and a post-processing ensures nonlinear stability and a conservative coupling of the two sets. The bundle holds it as the archive's example of overlap used inside a single discretization ([overset grid](/definitions/overset-grid.md), [conservative overset interface](/methods/conservative-overset-interface.md)).

# Version read

Version of record (Elsevier), 13 pages. Read in a targeted way (abstract, introduction, section structure, main results and conclusions closely; derivations and remaining results skimmed): from chunk 4 on, the bundle is compiled in the main session without reader subagents, by the owner's instruction. Claims below are limited to what was read closely.

# Key claims

1. Two formulations of a hyperbolic system — conservative, and primitive with nonconservative products — are discretized on overlapping staggered meshes with two different finite-volume schemes (Abstract). **Stated**
2. The nonconservative system is discretized by a path-conservative central-upwind scheme, and its solution evaluates simple numerical fluxes for the conservative system (Abstract). **Stated**
3. A post-processing ensures nonlinear stability and a conservative coupling between the two sets of variables (Abstract). **Stated**
4. Second-order schemes for one- and two-dimensional systems are tested numerically (Abstract). **Shown**

# Printed slips

None recorded (targeted reading).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| overlapping staggered meshes | two meshes of one discretization (not overset component grids) | |

# Reference list

52 references, merged complete into the [bibliography](/bibliography.md) with `citedby` abgrall-2026, from the Crossref deposited reference list; Shu & Osher part II is `shu-1989`, distinct from part I.

# Pages created or updated

Chunk 5 (2026-11-02). This source is cited on:

- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Conservative overset interface](/methods/conservative-overset-interface.md)
