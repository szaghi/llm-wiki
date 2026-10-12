---
type: Source
title: "Jaber, Essel & Sullivan (2025) — GPU-native adaptive mesh refinement with application to lattice Boltzmann simulations"
description: "A single-GPU AMR in which mesh, adaptation and solver all stay on the device: a block forest of quadtrees/octrees stored as integer ID lists with explicit neighbor links (no space-filling curve), 2:1 balance, and a subcycled lattice-Boltzmann solver coupled across levels by two interpolated ghost layers and averaged interface cells without time interpolation; no conservation or divergence content."
resource: "doi:10.1016/j.cpc.2025.109543"
source_kind: paper
authors: [Jaber K., Essel E.E., Sullivan P.E.]
year: 2025
venue: "Comput. Phys. Commun. 311:109543"
local_file: "~/papers/mosaic/div-free-amr/2025-CPC-Jaber-101016jcpc2025109543.pdf"
tags: [amr, tree-amr, gpu, lattice-boltzmann]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

An AMR algorithm in which the mesh, its adaptation and the solver data
all live on one GPU, with no host round trips. Code: AGAL, open source.
* **Mesh.** A block forest of quadtrees and octrees ($4^d$-cell blocks,
  $r = 2$, 2:1 balance at all times), stored as per-level integer ID
  lists with explicit neighbor and neighbor-child links.
* **Solver.** A BGK lattice-Boltzmann solver for weakly compressible flow
  with recursive subcycling.
* **Level coupling.** Two layers of interpolated ghost distributions
  (linear or cubic) and averaged interface cells, with no temporal
  interpolation.
* **No constraint content.** The paper has no divergence constraint, no
  refluxing and no conservation claim across levels.

# Key claims

1. **Data structure** (§§3.1–3.2). Per-level ID sets plus a gap set of
   free slots, with index recycling and no compaction. Parent blocks keep
   their data. There is no Morton or other
   [space-filling curve](/definitions/space-filling-curve.md); SFC
   partitioning is future multi-GPU work (§6).
2. **Adaptation** (§3.3, Algs. 1–2). Eight steps built from Thrust
   primitives and custom kernels. 2:1 balance is enforced by cancelling
   refinement or reverting coarsening marks.
3. **Coarse–fine coupling** (§§3.4, 4.1).
   * Coarse to fine: two ghost layers, filled once per coarse step by
     linear or tensor-cubic interpolation of distributions rescaled after
     Dupuis & Chopard.
   * Fine to coarse: two interface layers averaged into their parents
     (eq. 19).
   * The two-layer band absorbs both fine substeps, so ghosts are never
     interpolated in time.
4. **No conservation guarantee** (§3.4). Mass-conservative alternatives
   are cited but not used. Mass drift across levels is not measured. The
   only interface check is a contour plot of continuous pressure (Fig. 27).
5. **Restriction order** (§3.4.3). A cubic fine-to-coarse restriction
   "compatible ... in order of accuracy" was unstable "even when the root
   grid was refined and the mesh adaptivity was disabled". The mean was
   kept.
6. **Accuracy** (§5.3, Table 7). On a square cylinder at Re = 100, cubic
   ghost fill matches the finest uniform drag coefficient, while linear
   fill "is seen to degrade accuracy".
7. **Performance** (§5.2, Tables 3–5).
   * Regridding takes under 2 % of runtime in 3D.
   * Peak throughput is 161, 1138 and 1753 million lattice updates per
     second on a GTX 970M, V100 and A100.
   * Block storage survives scattered indices, while cell storage slows
     2.6–5×.
   * Against a uniform 2048² grid, AMR is 4.2–9.6× faster.
8. **On ADAM.** The paper lists the 2023 ADAM GPU code among those whose
   mesh is "hosted and managed, in whole or part, on the CPU" (§1).

# Notation map

| Jaber et al. (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| level $L$, $\Delta x/2^L$ | $l$; $h$, $H$ | |
| coarse-to-fine interpolation | $\Gamma$ (from $P$) | linear or cubic; no order statement |
| averaging (eq. 19) | $R$ (mean) | |
| $N_c$ | $2^d$ | |
| $A$, $\alpha_{ijk}$ (cubic fit) | words | $A_h$ is the vector potential |
| $\omega$ (relaxation frequency and vorticity) | words | |
| $D$ (cylinder side) | words | collides with $D_h$ |

# Pages created or updated

* Updated [Block-structured AMR](/definitions/block-structured-amr.md) (GPU-resident forest; subcycling without time interpolation).
* Updated [Restriction-compatibility bound](/results/point-value-restriction-compatibility.md) (data points), [Refluxing](/methods/refluxing.md) (no flux register), [ADAM](/software/adam.md) (third-party description).
* Created [Space-filling curve](/definitions/space-filling-curve.md) (cited as the counterexample).

# Citations

1. `~/papers/mosaic/div-free-amr/2025-CPC-Jaber-101016jcpc2025109543.pdf`.
   * **Version.** arXiv:2308.08085v3 (25 February 2025), the author
     preprint (45 pages). It is not the typeset article.
   * **Identity.** doi:10.1016/j.cpc.2025.109543, checked on Crossref:
     Comput. Phys. Commun. 311:109543, June 2025.
   * **How it was read.** Text extraction, all sections. Eqs. 10–12 were
     checked on the page image.
   * **Printed typos.** Eq. 10 has $a_3 y$ for $a_3 xy$, and the printed
     $a_7$ of eq. 12 is wrong; neither is reproduced.
   * **Internal inconsistencies.** "1.34 % in A2", the cylinder domain
     height, and the inserted-block count.
   * **Reference list:** 96 entries; accents dropped by the PDF are
     restored where unambiguous.
