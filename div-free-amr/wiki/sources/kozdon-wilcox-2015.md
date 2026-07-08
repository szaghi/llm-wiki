---
type: Source
title: "Kozdon & Wilcox (2015) — Stable coupling of nonconforming, high-order finite difference methods"
description: "Couples nonconforming SBP blocks through H-compatible projections onto an interface glue space of piecewise polynomials, with provable energy stability including SBP-DG coupling."
resource: "doi:10.1137/15M1022823"
source_kind: paper
authors: [Kozdon J.E., Wilcox L.C.]
year: 2015
venue: "SIAM J. Sci. Comput. 38(2), arXiv:1410.5746"
local_file: "~/papers/mosaic/div-free-amr/2015-SISC-Kozdon-10113715M1022823.pdf"
tags: [sbp, sat, nonconforming, projection, glue-space, dg-coupling, interface-conditions]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Generalizes nonconforming SBP coupling from grid-to-grid interpolation to
**projection through a glue space**: each block's interface trace is
projected onto a space of discontinuous piecewise polynomials living on the
interface, with projection operators built to be **compatible with the SBP
energy norm** (in the $L_2(\Gamma)$ sense). Because each side talks only to
the glue space, operators are constructed *once per SBP operator*,
independent of what sits across the interface — enabling provably
energy-stable couplings for curved nonconforming interfaces, non-matching
block corners (T-intersections), and even **SBP-to-discontinuous-Galerkin**
hybrid meshes. Energy stability is proven for the 2D linear wave equation;
verified by eigenvalue analysis and curved-mesh simulations. The authors
state explicitly that accommodating nonconforming grids "enables the
development of adaptive mesh refinement codes using high-order, SBP finite
difference methods."

# Key claims

1. **Glue-space architecture**: interface coupling factors through a
   piecewise-polynomial intermediary; SATs are written against glue-space
   data. One-sided construction decouples the two sides — the reusability
   the direct $I_{C2F}/I_{F2C}$ pairs lack
   ([SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md)).
2. **H-compatibility replaces pairwise adjointness**: each projection is
   compatible with its own block's $\mathsf{H}$-norm
   ([notation](/notation.md)); the energy estimate telescopes through the
   glue space.
3. **Lineage recorded**: Mattsson–Carpenter's operators required matching
   block corners; Nissen et al. removed that at fixed refinement ratio
   (corpus paper, pending ingestion); this work removes the geometric
   constraints and adds method-heterogeneous (SBP–DG) coupling. The
   SBP property alone is insufficient — SBP-preserving *closures* remain
   necessary.
4. **Scope**: linear symmetric hyperbolic systems (wave equation proved);
   projections are equation-independent; extension claimed straightforward
   by standard techniques.

# Notation map

| Kozdon & Wilcox | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $D = H^{-1}Q$, $Q + Q^T = B$ | $\mathsf{D}_1 = \mathsf{H}^{-1}\mathsf{Q}$ | |
| glue grid / glue space | — | interface intermediary; named inline |
| projection operators to/from glue | generalization of $I_{C2F}, I_{F2C}$ | H-compatible per block |

# Pages created or updated

* Updated [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md) (glue-space generalization).

# Citations

1. `~/papers/mosaic/div-free-amr/2015-SISC-Kozdon-10113715M1022823.pdf` (doi:10.1137/15M1022823, arXiv:1410.5746) — text extraction, 30 pp.
