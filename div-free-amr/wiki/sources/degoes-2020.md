---
type: Source
title: "de Goes, Butts & Desbrun (2020) — Discrete differential operators on polygonal meshes"
description: "Graphics-production consolidation: a linear-precise mimetic gradient on arbitrary (non-planar, non-convex) polygons bootstraps a full operator family, VEM-style with MFD stabilization."
resource: "doi:10.1145/3386569.3392389"
source_kind: paper
authors: [de Goes F., Butts A., Desbrun M.]
year: 2020
venue: "ACM Trans. Graph. 39(4):110"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2020-ACM-TOG-deGoes-10114533865693392389.pdf"
tags: [mimetic, polygonal, discrete-calculus, graphics, virtual-element]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The structure-preserving toolkit deployed in production graphics (Pixar):
a **novel mimetic discretization of the gradient, linear-precise on
arbitrary polygons** — including non-planar and non-convex faces — from
which a family of first- and second-order operators (Laplacian, covariant
derivative, shape operator) is bootstrapped "by mimicking key structural
properties of their continuous counterparts," drawing on the Virtual
Element Method with MFD-based inner-product stabilization
(explicitly the [Brezzi et al. (2005)](/sources/brezzi-lipnikov-shashkov-2005.md)
technique). The operators drop into existing geometry-processing
algorithms (editing, parameterization, vector-field design) on polygonal
surfaces.

# Key claims

1. **The mimetic pipeline's industrial reach**: the same
   consistency-plus-stabilization construction proved for polyhedral
   diffusion reappears, unchanged in structure, as the numerical layer of
   feature-film asset tooling — evidence for the framework's portability
   across domains far from its origins.
2. **Non-planar polygons handled**: extending VEM-style operators beyond
   flat faces — surface meshes as they exist in practice, not as theory
   prefers them.

# Notation map

| de Goes et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| discrete forms / directional fields | cochain data on surface complexes | DEC lineage |
| mimetic gradient, VEM stabilization | consistency (S1) + stability (S2) pattern | MFD-inherited |

# Pages created or updated

* Updated [Discrete exterior calculus (DEC)](/definitions/discrete-exterior-calculus.md) (industrial deployment note).

# Citations

1. `~/papers/mosaic/div-free-amr/2020-ACM-TOG-deGoes-10114533865693392389.pdf` (doi:10.1145/3386569.3392389) — text extraction, 14 pp.
