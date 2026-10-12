---
type: Source
title: "Zaghi, Salvadore, Di Mascio & Rossi (2023) — Efficient GPU parallelization of adaptive mesh refinement technique for high-order compressible solver with immersed boundary"
description: "The published description of the ADAM block-octree AMR library at its 2023 state: identical Cartesian blocks, 2:1 balance, a Morton-keyed CPU hash map, a GPU-resident field with CUDA Fortran, second-order ghost interpolation and one global time step, with a WENO compressible Navier–Stokes application scaled to 256 V100 GPUs; no divergence-constraint content."
resource: "doi:10.1016/j.compfluid.2023.106040"
source_kind: paper
authors: [Zaghi S., Salvadore F., Di Mascio A., Rossi G.]
year: 2023
venue: "Comput. Fluids 266:106040"
local_file: "~/papers/mosaic/div-free-amr/2023-CompFluids-Zaghi-101016jcompfluid2023106040.pdf"
tags: [amr, tree-amr, gpu, production-code]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper presents ADAM, a Fortran 2003 object-oriented library for
block-based octree AMR, and NASTO, a compressible Navier–Stokes
application built on it. It treats the compressible equations only: no
MHD, no Maxwell, no divergence constraint. It is ingested as the
peer-reviewed record of the AMR infrastructure behind
[ADAM](/software/adam.md). Up to that page's date, that record rested only
on the author's own documentation.

# Key claims

1. **Octree of blocks** (§2.2). A single root block covers the domain.
   Blocks are identical Cartesian blocks of cell-centred cells with 26
   ghost regions, split 8 ways ($r = 2$). The number of ghost layers is
   not stated.
2. **Tree storage** (§2.2, Fig. 2). The tree is a hash map keyed by a
   64-bit "Morton index" that linearizes level and block coordinates. It
   is replicated on every MPI rank, not decomposed, and updated serially.
   Load balancing follows Morton curves ([space-filling curve](/definitions/space-filling-curve.md)).
3. **2:1 balance** (§2.2). "The AMR level between two contiguous blocks
   must differ by at most one". A hysteresis on the split and recompose
   thresholds prevents flip-flop.
4. **GPU strategy** (§§2.2, 3.2, 4).
   * The back-end is CUDA Fortran (mostly `!$cuf` kernels) with
     CUDA-aware MPI, one GPU per rank.
   * The field stays on the device, with the block index fastest-varying.
     Copies happen only at I/O and AMR updates.
   * OpenMP and OpenACC back-ends are future work.
5. **Interfaces.** Ghost cells across level jumps use "second-order
   interpolations". The stencil, the refine and coarsen operators, and
   any refluxing are not specified. A single global time step is taken
   from the smallest cell (eq. 9), so there is no subcycling. Ghosts are
   refreshed at every Runge–Kutta stage (§3.1.1).
6. **Discretization** (§3.1).
   * WENO finite differences in conservative form, with Lax–Friedrichs
     flux splitting, and SSP-RK3.
   * The WENO order of the main test is not stated; WENO3 for the
     appendix vortex.
   * A signed-distance immersed boundary, extrapolated by pseudo-time
     marching (eq. 10).
7. **Performance** (§3.2, Table 1). V100 GPUs on Marconi100.
   * **Strong scaling** (3.6M cells) is superlinear to 8 GPUs, about 89 %
     efficient at 16 and below 60 % at 32. The method is efficient above
     about 250 000 cells per GPU.
   * **Wider resolution ratios** grow the grind time less than 3× for a
     32× range.
   * **The serial AMR update dominates**, reaching 527.97 s per update at
     684 258 blocks.

**Tests.**
* A Mach 2.89 shock diffracting over a sphere, up to 350M cells on 256
  GPUs, in qualitative agreement with Bryson & Gross.
* An isentropic vortex for the AMR jumps (visual check only).

# Notation map

| Zaghi et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| refinement into 8 siblings | $r = 2$ | |
| AMR level | $l$ | |
| ghost interpolation at level jumps | $\Gamma$ | "second-order", stencil not given |
| refinement and coarsening "by interpolation" | $P$, $R$ | operators not given |
| $h(x)$ (numerical flux, eq. 5) | words | collides with $h$, the grid spacing |
| $R$ (gas constant), $R(\cdot)$ (residual) | words | collide with the restriction $R$ |
| $R_\delta = \delta_C/\delta_F$ | words (coarsest-to-finest spacing ratio) | not the per-level ratio $r$ |

# Pages created or updated

* Updated [ADAM](/software/adam.md): published-record section.
* Created [Space-filling curve](/definitions/space-filling-curve.md).
* Updated [Block-structured AMR](/definitions/block-structured-amr.md) and [Refluxing](/methods/refluxing.md).
* Updated [Notation registry](/notation.md): $l$, $r$.

# Citations

1. `~/papers/mosaic/div-free-amr/2023-CompFluids-Zaghi-101016jcompfluid2023106040.pdf`.
   * **Version.** The published Elsevier version (open access), from the
     University of L'Aquila repository.
   * **Identity.** doi:10.1016/j.compfluid.2023.106040, checked on
     Crossref: Comput. Fluids 266:106040, November 2023.
   * **How it was read.** Text extraction, all sections.
   * **Defects in the paper.** Figure grid labels do not match Table 1 run
     numbers.
   * **Reference list:** 70 entries.
