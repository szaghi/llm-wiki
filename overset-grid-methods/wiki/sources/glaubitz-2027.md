---
type: Source
title: "Glaubitz et al. (2027) — Towards provable energy-stable overset grid methods using sub-cell summation-by-parts operators"
description: "Develops a discrete counterpart of the well-posedness analysis of overset problems by introducing sub-cell summation-by-parts operators, which mimic integration by parts on parts of a cell, and uses them to build provably conservative and energy-stable overset methods for fixed one-dimensional overset domains."
resource: "doi:10.1016/j.jcp.2026.115347"
source_kind: paper
authors: [Glaubitz J., Lampert J., Winters A.R., Nordström J.]
year: 2027
venue: "J. Comput. Phys. 568:115347"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2027_Crossref_Journal_of_Computational_Physics_Glaubitz_Towards_provable_energy-stable_overset_grid_methods_using_su.pdf"
tags: [sbp-sat, stability, energy-method, conservation]
timestamp: 2026-11-02T15:51:00Z
---

# Summary

Overset grid methods work robustly in practice, but general stability proofs are lacking. Glaubitz et al. develop a discrete counterpart to the continuous well-posedness analysis of [Kopriva et al. (2022)](/sources/kopriva-2022.md): they introduce sub-cell summation-by-parts (SBP) operators — discrete derivative operators that mimic integration by parts on a sub-cell level, i.e. on the part of a cell that lies in the overlap — and use them to construct provably conservative and energy-stable overset grid methods for fixed one-dimensional overset domains that do not change in time or under refinement ([well-posedness and energy stability of overset problems](/results/overset-well-posedness.md), [high-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md)). Code is public.

# Version read

arXiv preprint 2509.21442v2 (8 September 2026), 34 pages; the 2027 issue was published online in 2026. Read in a targeted way (abstract, introduction, section structure, main results and conclusions closely; derivations and remaining results skimmed): from chunk 4 on, the bundle is compiled in the main session without reader subagents, by the owner's instruction. Claims below are limited to what was read closely.

# Key claims

1. Although overset grid methods are robust in extensive practical use, general stability proofs are not available (Abstract, §1). **Stated**
2. The work develops a discrete counterpart to the well-posedness analysis of Kopriva, Gassner and Nordström for continuous overset initial-boundary value problems (Abstract). **Stated**
3. Sub-cell SBP operators are introduced: discrete derivative operators that mimic integration by parts at a sub-cell level (Abstract, §3). **Derived**
4. With the sub-cell SBP property, provably conservative and energy-stable overset methods are built for fixed one-dimensional overset domains that do not change with time or under refinement (Abstract). **Proved**
5. The authors present the result as a step toward energy-method stability proofs for overset grid methods in general (Abstract). **Stated**

# Printed slips

None recorded (targeted reading).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| SBP norm and derivative matrices | $\mathsf H$, $\mathsf D=\mathsf H^{-1}\mathsf Q$ | registry §8, in use |
| SAT penalties | $\Sigma$ | registry §8 |
| sub-cell SBP operator | SBP property restricted to part of a cell | page-local |

# Reference list

81 references, merged complete into the [bibliography](/bibliography.md) with `citedby` glaubitz-2027, from the Crossref deposited reference list (DOIs resolved on Crossref); Kopriva et al.'s part II (`kopriva-2022-b`) is distinct from the ingested part I. [Kopriva et al. (2025)](/sources/kopriva-2025.md) is cited.

# Pages created or updated

Chunk 6 (2026-11-02). This source is cited on:

- [Conservative overset interface](/methods/conservative-overset-interface.md)
- [High-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md)
- [Well-posedness and energy stability of overset problems](/results/overset-well-posedness.md)
