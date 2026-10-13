---
type: Source
title: "Stone, Tomida, White & Felker (2020) — The Athena++ adaptive mesh refinement framework: design and magnetohydrodynamic solvers"
description: "Modern CT-AMR production framework: mesh abstracted from physics with face/edge data first-class, line-weighted EMF matching at interfaces, and bitwise EMF consistency enforced even on same-level shared edges."
resource: "doi:10.3847/1538-4365/ab929b"
source_kind: paper
authors: [Stone J.M., Tomida K., White C.J., Felker K.G.]
year: 2020
venue: "Astrophys. J. Suppl. Ser. 249:4"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2020-ApJS-Stone-1038471538-4365ab929b.pdf"
tags: [constrained-transport, amr, production-code, mhd, relativistic, task-parallelism]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The Athena++ framework: the mesh **abstracted from the physics**, with
cell-centered, face-centered, and edge-centered discretizations as
first-class citizens (generic communication classes for each) — the
infrastructure-level acknowledgment that MHD's staggered data is not an
afterthought. Block-based AMR on a binary/quad/octree of equal-sized
MeshBlocks, task-list dynamic execution (>80% parallel efficiency on
half a million threads), curvilinear coordinates, nonrelativistic and
relativistic MHD with [CT](/methods/constrained-transport.md).

# Key claims

1. **Line-weighted EMF matching at level interfaces**: coarse EMFs on
   shared edges are replaced by
   $e_{\mathrm{coarse}}\Delta l_{\mathrm{coarse}} = \sum e_{\mathrm{fine}}\Delta l_{\mathrm{fine}}$
   — otherwise face fluxes become inconsistent "and the resulting
   divergence error can grow and cause unphysical dynamics"
   ([electric-field correction](/methods/electric-field-correction.md)
   in Athena++ form).
2. **Determinism is part of the invariant**: even on shared edges *at the
   same refinement level*, EMFs computed by different MeshBlocks can
   differ — from prolongation arrangement, "nondeterministic ordering of
   the MPI communications, and round-off error" — so *both* fine and
   coarse shared-edge EMFs are explicitly averaged/corrected to be
   identical. An algebraic invariant held to machine precision is only as
   good as the bitwise agreement of its shared inputs.
3. **Unsplit at every substep**: preserving the constraint requires
   dimensionally unsplit integration *at each substep*; Athena++ drops
   CTU (characteristic projection intractable for relativistic MHD) in
   favor of VL2 and SSP/low-storage RK integrators — trading Athena's
   most accurate integrator for physics generality.

# Notation map

| Athena++ | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| face-centered $B$, edge-centered EMFs | $B_h \in V_h^2$, $E_h \in V_h^1$ | first-class mesh data kinds |
| eq. (1) line-weighted matching | EMF correction, metric-weighted | curvilinear-ready |
| eq. (2) volume-weighted restriction | $R$ on cell data | standard |

# Pages created or updated

* Updated [Electric-field correction](/methods/electric-field-correction.md) (line-weighted form; same-level determinism requirement).

# Citations

1. `~/papers/mosaic/div-free-amr/2020-ApJS-Stone-1038471538-4365ab929b.pdf` (doi:10.3847/1538-4365/ab929b) — text extraction, 40 pp.
