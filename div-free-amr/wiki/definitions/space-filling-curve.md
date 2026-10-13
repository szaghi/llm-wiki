---
type: Definition
title: "Space-filling curve (Morton and Peano–Hilbert ordering)"
description: "A one-dimensional index over the cells, blocks or elements of a refinement tree, computed from integer coordinates and level alone, that is injective, monotone under refinement and local; AMR codes use it to order data, cut the mesh into partitions and coarsen it for multigrid."
status: established
aliases: [SFC, Morton order, Z-order, N-order, Peano–Hilbert order, U-order]
tags: [amr, tree-amr, partitioning]
timestamp: 2026-10-13T00:00:00Z
---

# Space-filling curve

**Definition.** A space-filling-curve (SFC) index assigns each element
$E$ of a refinement tree an integer $m(E)$. Knapp et al., after Holke,
state three axioms:
1. $m$ is injective on each level;
2. it is monotone under refinement: $m(E) \le m(E')$ for every
   descendant $E'$;
3. it is local: the descendants of $E$ fall between $m(E)$ and the index
   of the next element that is not a descendant.

Sorting the leaves by $m$ gives a consecutive leaf order. A partition is
then a set of contiguous segments of that order
([Knapp et al. (2026)](/sources/knapp-2026.md), §2, Def. 3.4).

**Morton (Z- or N-order).** The index interleaves the bits of the integer
coordinates. With $b$-bit coordinates $(x, y, z)$ it is the $3b$-bit word
formed bit by bit, $x^1 y^1 z^1\, x^2 y^2 z^2 \dots$. It is computable
from a cell's coordinates and the maximum level alone ("compactness"),
with no connectivity matrix.
* **Peano–Hilbert (U-order)** has the stronger locality: consecutive cells
  along the curve are face neighbors. Its key construction is cited, not
  given ([Aftosmis, Berger & Murman (2004)](/sources/aftosmis-berger-murman-2004.md), §2).
* **The Morton index is an SFC index in any dimension.** Knapp et al.
  extend it to hybrid meshes. An element is identified by the anchor of
  its enclosing sub-cube, its level and a type: 0–5 for tetrahedra, 6–7
  for pyramids. The index interleaves the anchor bits with the bits of the
  type history. They prove it is an SFC index by embedding it in a 6D
  Morton index ([Knapp et al. (2026)](/sources/knapp-2026.md), Thm 3.5,
  Prop. 3.6).

**Uses in AMR**
* **Partitioning.** Cutting the curve into equal-weight segments
  partitions the mesh, and it can be done on the fly at read time for
  any number of parts.
  * Refinement only inserts or removes entries of the order, so
    repartitioning moves data only at segment ends.
  * On a 1.6M-cell adapted mesh in 64 parts, Peano–Hilbert partitions
    carry 4 % more communication faces than an ideal cubical partition,
    $6\,(N_{\mathrm{cells}}/N_{\mathrm{parts}})^{2/3}$. Morton is somewhat
    worse.
  * Cache hit rates are "about the same" as reverse Cuthill–McKee
    ordering, though no numbers are given
    ([Aftosmis, Berger & Murman (2004)](/sources/aftosmis-berger-murman-2004.md), §4).
* **Multigrid coarsening.** After one $O(N\log N)$ sort, one $O(N)$ pass
  agglomerates contiguous runs of siblings into their parent. The authors
  state that coarsening ratios "typically exceed 7" for realistically
  complex problems (not quantified); their example, 4.5M cells reaching
  4500 after four coarsenings, averages about 5.6 per level ([Aftosmis, Berger & Murman (2004)](/sources/aftosmis-berger-murman-2004.md), §3).
* **Block ordering and load balance.**
  * ADAM keys its block octree with a Morton-type index and balances load
    along Morton curves ([Zaghi et al. (2023)](/sources/zaghi-2023.md), §2.2).
  * CASTRO switches between a knapsack heuristic and a Morton-ordered
    distribution of grids ([Almgren et al. (2010)](/sources/almgren-2010.md), §7.1).
  * t8code's partition "follows without additional efforts" from the curve.
    The forest-level operations keep near-ideal scaling up to $2^{15}$
    processes, and a hybrid airplane mesh runs on up to $2^{17}$
    ([Knapp et al. (2026)](/sources/knapp-2026.md), §§1.1, 6–7).
* **Not every tree code uses one.** A GPU-resident AMR stores its forest
  as integer ID lists with explicit neighbor links, and names SFC
  partitioning only as future multi-GPU work
  ([Jaber, Essel & Sullivan (2025)](/sources/jaber-essel-sullivan-2025.md), §§3.1, 6).

**Bearing on this bundle.** An SFC fixes data order and ownership. It
does not touch the interface operators ($\Gamma$, $R$, $P$) or any
divergence constraint, and none of these sources connects the two. See
[block-structured AMR](/definitions/block-structured-amr.md) for the
tree-based variants.

# Citations

1. [Knapp et al. (2026)](/sources/knapp-2026.md), §§1–3, 6–7 (arXiv preprint).
2. [Aftosmis, Berger & Murman (2004)](/sources/aftosmis-berger-murman-2004.md), §§2–4 (extended abstract).
3. [Zaghi et al. (2023)](/sources/zaghi-2023.md), §2.2.
4. [Almgren et al. (2010)](/sources/almgren-2010.md), §7.1.
5. [Jaber, Essel & Sullivan (2025)](/sources/jaber-essel-sullivan-2025.md), §§3.1, 6.
