---
type: Source
title: "Aftosmis, Berger & Murman (2004) — Applications of space-filling-curves to Cartesian methods for CFD"
description: "Extended abstract proposing Morton and Peano–Hilbert space-filling curves as one data structure for ordering, partitioning, multigrid coarsening and inter-mesh transfer on adapted Cartesian cut-cell meshes: one O(N log N) sort, then O(N) passes; Peano–Hilbert partitions carry 4% more communication faces than ideal, and the solver scales to about 430× on 512 CPUs."
resource: "doi:10.2514/6.2004-1232"
source_kind: paper
authors: [Aftosmis M.J., Berger M.J., Murman S.M.]
year: 2004
venue: "42nd AIAA Aerospace Sciences Meeting, AIAA Paper 2004-1232"
local_file: "~/papers/mosaic/div-free-amr/2004-AIAA-Aftosmis-10251462004-1232.pdf"
tags: [amr, tree-amr, partitioning, multigrid]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

On adaptively refined, cell-based Cartesian meshes with embedded
boundaries (the Cart3D lineage), one sort of the cells by
[space-filling-curve](/definitions/space-filling-curve.md) key yields
single-pass algorithms for cache ordering, domain decomposition,
multigrid coarsening and inter-mesh interpolation. The file read is the
extended abstract, not the final paper. It has no divergence-constraint
content, no coarse–fine transfer operators and no subcycling; the solver
is a steady multigrid Euler code.

# Key claims

1. **Orderings** (§2). Peano–Hilbert ("U-order") and Morton ("N-order"),
   with three properties: a mapping to one dimension, locality, and
   compactness, meaning the key needs only integer coordinates and the
   maximum level. The Morton key interleaves the coordinate bits.
2. **Adapted meshes** (§2). The finest cell defines a voxel, and integer
   indexing gives every cell a key. The $O(N\log N)$ sort dominates the
   cost, and everything else is local.
3. **Coarsening** (§3, Figs. 4–5). One pass agglomerates contiguous
   sibling runs into their parent; sets with a further-subdivided sibling
   are injected unchanged. Typical coarsening ratios exceed 7, and 4.5M
   cells reach 4500 after 4 coarsenings.
4. **Partitioning** (§4, eq. 1, Fig. 8).
   * Contiguous curve segments with cell weights (cut cells weigh 2.1),
     partitioned on the fly at read time. Repartitioning after adaptation
     moves data only at segment ends.
   * The ideal cubical bound is $F_c = 6(N_{\mathrm{cells}}/N_p)^{2/3}$
     faces. On 1.6M cells in 64 parts, Peano–Hilbert is 4 % above it.
     Morton is higher, about 9 % read from the bars; that value is not
     printed.
   * The cache hit rate is "about the same" as reverse Cuthill–McKee, with
     no numbers.
5. **Scaling** (§4.1, Figs. 9–11).
   * On a 4.4M-cell SSLV case, about 430× on 512 CPUs and about 120× on
     128 of an SGI Origin (600 MHz R14000).
   * 12–13× on 15 CPUs of a Pentium 4 gigabit cluster.
6. **Inter-mesh interpolation** (§5). It is $O(\max(M, N))$, and its
   algorithm is deferred to the final paper.

# Notation map

| Aftosmis et al. (2004) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $M(i)$, $H(i)$ (Morton and Hilbert indices) | $m(E)$ | $H$ collides with the coarse spacing |
| $U$ (one-dimensional index space) | words | |
| $(x_i, y_i, z_i)$ integer coordinates | words | |
| $F_c$, $N_{\mathrm{Cells}}$, $N_p$ | inline | |

# Pages created or updated

* Created [Space-filling curve](/definitions/space-filling-curve.md).
* Updated [Block-structured AMR](/definitions/block-structured-amr.md) (cell-based cut-cell tree variant).
* Updated [Notation registry](/notation.md): $m(E)$.

# Citations

1. `~/papers/mosaic/div-free-amr/2004-AIAA-Aftosmis-10251462004-1232.pdf`.
   * **Version.** The 6-page **extended abstract** (the cover reads "AIAA
     2004-Abstract", and its own page 9 is the submission note). The text
     defers several results to the final paper. Crossref lists 23
     references for the final paper; this file prints 32.
   * **Identity.** doi:10.2514/6.2004-1232, checked on Crossref: 42nd AIAA
     Aerospace Sciences Meeting, 5 January 2004, three authors.
   * **How it was read.** An OCR scan. Eq. 1 and the figures were read from
     the page images.
   * **Inconsistent print.**
     * The title block reuses AIAA 2000-0808.
     * The machine is an Origin 3000 in the text and a 3600 in the caption.
     * The cluster mesh is 1.8M or 1.6M cells.
     * "50 000 cells per subdomain" against the 25 000 shown.
   * **Reference list:** 32 entries; refs 12 and 24 are the same work,
     printed twice.
