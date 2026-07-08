---
type: Source
title: "Balsara (2001) — Divergence-free adaptive mesh refinement for magnetohydrodynamics"
description: "Second-order divergence-free evolution on block-structured AMR: divergence-free reconstruction, prolongation, area-weighted restriction, and electric-field correction under subcycling."
resource: "doi:10.1006/jcph.2001.6917"
source_kind: paper
authors: [Balsara D.S.]
year: 2001
venue: "J. Comput. Phys. 174:614-648"
local_file: "~/papers/mosaic/div-free-amr/2001-JCP-Balsara-101006jcph20016917.pdf"
tags: [amr, constrained-transport, divergence-free-reconstruction, prolongation, restriction, subcycling]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The founding paper of **divergence-free block-structured AMR-MHD**: a
complete second-order scheme keeping the staggered face-field invariant
$D_h^{\mathrm{f}} B_h = 0$ exact across a
[Berger–Colella hierarchy](/definitions/block-structured-amr.md) with
subcycled time steps. Four components, each the magnetic analog of a
Berger–Colella fluid ingredient: (i) **divergence-free TVD reconstruction**
(limited quadratic polynomials, divergence-free at every point of the zone);
(ii) **divergence-free prolongation** — a minimal extension of the
reconstruction, instantiating $P_D$
([operator page](/operators/divergence-free-prolongation.md)); (iii)
**area-weighted restriction** of face fields (the analog of volume-weighted
restriction of cell quantities); (iv) the **electric-field correction step**
at fine–coarse interfaces
([method page](/methods/electric-field-correction.md)) — the analog of
[refluxing](/methods/refluxing.md) — restoring divergence-free consistency
after subcycled fine steps. Implemented in the RIEMANN framework; validated
on 3D AMR-MHD problems with strong magnetosonic shocks.

# Key claims

1. **Reconstruction** (§III): fit limited linear profiles on each face
   (minmod slopes of face fields), then a zone-interior quadratic vector
   polynomial with $a_{yy} = b_{xx} = 0$ and coefficients constrained by
   the *continuous* divergence-free condition
   ($a_x + b_y = 0$, $2a_{xx} + b_{xy} = 0$, $a_{xy} + 2b_{yy} = 0$ in 2D);
   the reconstructed field is divergence-free at **all points of the
   zone**, and the construction reduces to standard TVD reconstruction in
   1D. Second source for
   [divergence-free reconstruction](/methods/divergence-free-reconstruction.md).
2. **Prolongation = area-weighted evaluation of the reconstruction** (§IV):
   integrating the polynomials over fine-zone faces gives face averages
   that are divergence-free in the fine discrete sense to machine
   precision; being an integral formulation, it extends to any integer
   refinement ratio (recursively for 4, 8), any orthogonal geometry, and
   triangular/tetrahedral meshes.
3. **Nesting claim against zone-centered formulations** (§III intro): the
   divergence-free property survives transfer between levels because the
   staggered control volumes at finer levels nest inside coarse ones; "the
   zone-centered formulation of Tóth does not satisfy this property" —
   recorded under `Contradictions` at
   [CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md).
4. **Restriction alone breaks consistency under subcycling** (§V): after
   two fine steps, replacing the coarse face field by the four-fine-face
   average (5.4) disagrees with the coarse update (5.1), leaving nonzero
   divergence in abutting coarse zones — hence the electric-field
   correction: coarse edge EMFs are replaced by the time-averaged sums of
   fine edge EMFs, restoring EMF consistency exactly as flux correction
   restores flux consistency.
5. **Scope**: second-order accurate; ideal MHD here, with the implicit
   resistive extension sketched (§II) and flagged for iterative solvers on
   the same restriction/prolongation machinery.

# Notation map

| Balsara | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $B^{\pm}_x = B_{x,i\pm1/2,j,k}$ etc. | $B_h$, face-collocated | capital = coarse, lower-case $b$ = fine in §V |
| $E_{x,y,z}$ on edges | $E_h \in V_h^1$ | eq. (2.8) update = $\partial_t B_h = -C_h E_h$ |
| area-weighted prolongation (4.19) | $P_D$ | divergence-free by construction |
| four-face average (5.4) | $R$ on face data | area-weighted restriction |
| electric-field correction (5.6–5.7) | EMF synchronization | analog of refluxing for $V_h^1$ data |

# Pages created or updated

* Created [Divergence-free prolongation $P_D$](/operators/divergence-free-prolongation.md).
* Created [Electric-field correction](/methods/electric-field-correction.md).
* Updated [Divergence-free reconstruction](/methods/divergence-free-reconstruction.md) (second source; TVD-limited construction).
* Updated [CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md) (`Contradictions`: AMR nesting claim).
* Updated [Refluxing](/methods/refluxing.md) (cross-link to its face-field analog).

# Citations

1. `~/papers/mosaic/div-free-amr/2001-JCP-Balsara-101006jcph20016917.pdf` (doi:10.1006/jcph.2001.6917) — text extraction, pp. 614–648.
