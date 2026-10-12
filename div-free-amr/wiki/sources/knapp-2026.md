---
type: Source
title: "Knapp, Holke, Spenke, Burstedde & Dreyer (2026) — A Morton-type space-filling curve for pyramid subdivision and hybrid adaptive mesh refinement"
description: "Preprint adding pyramids to t8code's forest-of-trees AMR: a pyramid refines into 6 pyramids and 4 tetrahedra so that the split commutes with cubic refinement, a Morton-type index over (anchor, level, type) proved to be a space-filling-curve index, element and forest algorithms, and near-ideal scaling to 2^15–2^17 processes; no divergence content."
resource: "arXiv:2602.20887"
source_kind: paper
authors: [Knapp D., Holke J.A., Spenke T., Burstedde C., Dreyer L.]
year: 2026
venue: "arXiv:2602.20887 (preprint, v3)"
local_file: "~/papers/mosaic/div-free-amr/2026-arXiv-Knapp-1048550arXiv260220887.pdf"
tags: [amr, tree-amr, partitioning, hybrid-mesh]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper makes the pyramid a fully supported element of t8code's
forest-of-trees AMR. Hybrid 3D meshes need it to bridge tetrahedral and
hexahedral regions without hanging edges. It is pure mesh infrastructure:
a refinement rule, a [space-filling curve](/definitions/space-filling-curve.md),
element connectivity, partitioning and ghost layers. It has no PDE
solver, no coarse–fine transfer operators, no 2:1 balance and no
divergence content.

# Key claims

1. **Refinement rule** (§3, Tables 3.1–3.2). A pyramid splits into 6
   pyramids and 4 tetrahedra, chosen so that pyramidal refinement commutes
   with cubic refinement. Tetrahedra then refine by Bey's rule. A
   uniformly refined tree has $2\cdot8^l - 6^l$ elements at level $l$
   (eq. 5.1).
2. **Element identity** (§3). The anchor of the enclosing sub-cube, the
   level and a type in 0–7 (0–5 for tetrahedra, 6–7 for pyramids).
3. **The SFC index** (Defs. 3.2–3.4, Thm 3.5, Prop. 3.6). The pyramid
   index interleaves the anchor bits with the bits of the type history. It
   satisfies the three SFC-index axioms (injective per level, monotone
   under refinement, local), proved by embedding it in a 6D Morton index.
4. **Algorithms** (§4).
   * The parent of a tetrahedron needs a stored field, the level of its
     first tetrahedral ancestor.
   * A level-linear test decides whether a tetrahedron touches a pyramid
     (Thm 4.2).
   * Inter-tree neighbors are found by collapsing to the root face.
5. **Partitioning for creating a forest** (§5, Alg. 5.1). Uniform bounds on
   multi-shape forests, with one responsible process counting each shared
   tree once.
6. **Performance** (§§6–7).
   * Adapt and Partition scale near-ideally for every element shape up to
     $2^{15}$ processes on CARA, with up to 75e9 elements. Pyramids are
     somewhat costlier and hexahedra fastest.
   * A hybrid airplane mesh on $2^{14}$–$2^{17}$ processes of CARO runs in
     250.262 s down to 49.942 s, with Adapt taking 72–90 % of it.

# Notation map

| Knapp et al. (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $m_P$, $m_{\mathcal Q}$ (SFC indices) | $m(E)$ | |
| $l$, $\ell$, $\mathcal L$ | $l$; maximum level (words) | the paper uses both $l$ and $\ell$ |
| $P$ (element; process count) | words | collides with the prolongation $P$ |
| $I$ (generic SFC index) | $m(E)$ | collides with the identity in $RP = I$ |
| $\mathcal P$, $\mathcal Q$ | words | collides with $\mathcal P_r\Lambda^k$ |

# Pages created or updated

* Created [Space-filling curve](/definitions/space-filling-curve.md).
* Updated [Block-structured AMR](/definitions/block-structured-amr.md) (forest of element trees on hybrid meshes).
* Updated [Notation registry](/notation.md): $m(E)$, $l$.

# Citations

1. `~/papers/mosaic/div-free-amr/2026-arXiv-Knapp-1048550arXiv260220887.pdf`.
   * **Version.** arXiv:2602.20887v3 (22 May 2026), 35 pages. The
     bibliography is printed twice.
   * **No published version.** None was found on Crossref (by title and
     author, checked 2026-10-12). The arXiv DOI is a DataCite record.
   * **How it was read.** Text extraction, all sections. Eq. 3.4 and
     Alg. 5.1 were read from the page images.
   * **Defects in the preprint.**
     * "Theorem 4.1" is cited where Thm 4.3 is meant.
     * The supplement header omits Dreyer.
     * The prism ghost time in Table SM2.2 is off by a factor of 10.
   * **Reference list:** 50 entries. Ref. 1 misprints Fehling & Bangerth
     (ACM TOMS 49); ref. 37 carries the DOI of ref. 49, and that DOI was
     omitted.
