---
type: Source
title: "Zhang et al. (2019) — AMReX: a framework for block-structured adaptive mesh refinement"
description: "Four-page software paper for AMReX, the BoxLib successor: cell, face and node data, optional subcycling with unspecified multilevel synchronization, embedded boundaries, particles, geometric multigrid and BiCGStab, MPI+X and MPI+CUDA+X; no algorithms, tests or numbers, and no divergence content."
resource: "doi:10.21105/joss.01370"
source_kind: paper
authors: [Zhang W., Almgren A., Beckner V., Bell J., Blaschke J., Chan C., Day M., Friesen B., Gott K., Graves D., Katz M.P., Myers A., Nguyen T., Nonaka A., Rosso M., Williams S., Zingale M.]
year: 2019
venue: "J. Open Source Softw. 4:1370"
local_file: "~/papers/mosaic/div-free-amr/2019-JOSS-Zhang-1021105joss01370.pdf"
tags: [amr, block-structured, framework, gpu]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The citable record of [AMReX](/software/amrex.md), a C++ framework for
block-structured AMR descended from BoxLib. It lists capabilities only,
with no equations, figures, tests or performance numbers. The words
"projection", "refluxing", "flux register" and "divergence" do not appear.

# Key claims

1. **Scope and lineage** (Summary, p. 1). A framework for
   block-structured AMR "with complex boundary conditions on current and
   emerging architectures". It traces back to BoxLib.
2. **Advance** (p. 1). Strategies range "from level-by-level approaches
   (with or without subcycling in time) with multilevel synchronization
   to full-hierarchy approaches". No mechanism is named.
3. **Data** (p. 2). Fields on cell centres, faces or nodes. 1D Cartesian
   or spherical, 2D Cartesian or cylindrical, 3D Cartesian. Particle
   containers.
4. **Embedded boundaries** (p. 2). Cut cells with apertures, normals and
   volume fractions; no small-cell treatment is described.
5. **Parallelism** (p. 2). MPI+X (OpenMP tiling) and MPI+CUDA+X, with CUDA
   the only back-end of AMReX itself in 2019. Ghost filling is
   asynchronous, "including interpolation of data in space and time"
   (order not stated). There is a task-graph runtime and fork-join over MPI
   subgroups.
6. **Linear solvers** (p. 3). Geometric multigrid and BiCGStab, and
   hypre and PETSc interfaces, on regular and cut-cell data. Whether the
   multigrid is composite across levels is not stated.

# Notation map

| Zhang et al. (2019) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| ghost filling with interpolation in space and time | $\Gamma$ | order not stated |
| cell, face and node data | storage locations only | no form-degree semantics |
| level, hierarchy | $l$, $\Omega_h$ | $r$ not stated |

# Pages created or updated

* Created [AMReX](/software/amrex.md).
* Updated [Block-structured AMR](/definitions/block-structured-amr.md) (subcycling as a choice) and [Refluxing](/methods/refluxing.md) (no flux register named).

# Citations

1. `~/papers/mosaic/div-free-amr/2019-JOSS-Zhang-1021105joss01370.pdf`.
   * **Version.** The published JOSS PDF, 4 pages.
   * **Identity.** doi:10.21105/joss.01370, checked on Crossref:
     J. Open Source Softw. 4(37):1370, 12 May 2019, 17 authors.
   * **How it was read.** Text extraction, all of it.
   * **A citation slip.** The paper cites hypre to the PETSc reference.
   * **Reference list:** 17 entries. Four undated web pages take the
     citing year.
