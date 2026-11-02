---
okf_version: "0.1"
---

# overset-grid-methods — Knowledge Bundle

Overset (Chimera, composite overlapping) grid methods, as collected in an
overset-grid bibliography of 1983–2027: component grids that overlap
instead of abutting, the assembly that connects them (hole cutting, donor
search, fringe and orphan points, overlap optimization), the inter-grid
interpolation that couples them and its accuracy, conservation and
stability, moving overset grids, and the codes that implement them.

**Start here:** the [Notation registry](/notation.md), which is normative for
every page ($G_k$ the component grids of the composite grid $\mathcal G$,
$\mathbf x=\mathbf d_k(\mathbf r)$ their mappings from the unit cube,
$\iota_k$ the point mask with $1$ on discretization points, $0$ on holes and
$-k'$ on receptors with donor grid $k'$, $q$ the interpolation width, $d$
the overlap width, $p$ the discretization order), and the
[update log](/log.md).

**Corpus:** all 51 papers of the archive ingested in 6 chunks. Chunk 1
holds the founding papers of 1983–2005:
[Benek et al. (1983)](/sources/benek-1983.md) and
[Benek et al. (1985)](/sources/benek-1985.md) introduce the Chimera
grid-embedding technique in two and three dimensions;
[Meakin & Suhs (1989)](/sources/meakin-1989.md) make it move;
[Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) give composite
overlapping grids their formal definition, assembly algorithm and
interpolation-accuracy theory, and [Henshaw (1994)](/sources/henshaw-1994.md)
builds a fourth-order incompressible solver on them;
[Wang (1995)](/sources/wang-1995.md) makes the overset interface
conservative; [Lee & Baeder (2003)](/sources/lee-2003.md) introduce implicit
hole cutting; [Rogers et al. (2003)](/sources/rogers-2003.md) automate
assembly in PEGASUS 5; [Kageyama & Sato (2004)](/sources/kageyama-2004.md)
cover the sphere with two overlapping grids; and
[Noack (2005)](/sources/noack-2005.md) generalizes assembly to moving
bodies and unstructured grids in SUGGAR. The later chunks bring high-order
and Maxwell solvers on composite grids, parallel and GPU assembly, the
energy theory of the overset problem
([Kopriva et al. 2022](/sources/kopriva-2022.md),
[Glaubitz et al. 2027](/sources/glaubitz-2027.md)), immersed boundaries,
multiphase and fluid–structure applications. Chunks 4–6 were read in a
targeted way (see their Source pages).

## Reading guide

1. **What an overset grid is.** [Overset (Chimera) grid](/definitions/overset-grid.md)
   is the hub; [composite overlapping grid](/definitions/composite-overlapping-grid.md)
   is its formal definition; [patched (zonal) grids](/definitions/patched-grid.md)
   are the abutting alternative it is defined against;
   [grid hierarchy and priority](/definitions/grid-hierarchy.md) orders the
   components.
2. **Assembly.** [Domain connectivity](/definitions/domain-connectivity.md)
   is the problem; [point classification](/definitions/point-classification.md)
   is its output; [hole cutting](/methods/hole-cutting.md) and
   [implicit hole cutting](/methods/implicit-hole-cutting.md) remove points,
   [donor search](/methods/donor-search.md) finds interpolation stencils for
   [fringe points](/definitions/fringe-point.md), and
   [orphan points](/definitions/orphan-point.md) are where it fails;
   [overlap optimization](/methods/overlap-optimization.md) chooses among
   valid assemblies; [wall-distance hole cutting](/methods/wall-distance-hole-cutting.md)
   and [parallel and GPU assembly](/methods/parallel-overset-grid-assembly.md)
   make it fast; [exposed points](/definitions/exposed-point.md) appear when
   grids move.
3. **Coupling and accuracy.** [Inter-grid interpolation](/methods/inter-grid-interpolation.md),
   [explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md),
   the [interpolation order and overlap requirements](/results/interpolation-order-requirement.md),
   the [conservative overset interface](/methods/conservative-overset-interface.md),
   [interpolation-free coupling](/methods/interpolation-free-overset-coupling.md)
   and [nonlinear and optimized interpolation](/methods/nonlinear-inter-grid-interpolation.md);
   the theory is [well-posedness and energy stability](/results/overset-well-posedness.md).
4. **Discretizations on overlapping grids.** [High-order discretizations](/methods/high-order-overset-discretization.md),
   [discontinuous Galerkin](/methods/discontinuous-galerkin-on-overset-grids.md),
   [ADER](/methods/ader-on-overset-grids.md), [upwind schemes for wave equations](/methods/upwind-wave-equation-overset.md),
   [implicit–explicit time stepping](/methods/imex-time-stepping-on-overset-grids.md),
   [shock capturing](/methods/shock-capturing-on-overset-grids.md),
   [adaptive refinement](/methods/amr-on-overset-grids.md).
5. **Motion and physics.** [Moving overset grids](/methods/moving-overset-grid.md),
   [incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md),
   [immersed boundaries](/methods/immersed-boundary-on-overset-grids.md),
   [multiphase flow](/methods/multiphase-flow-on-overset-grids.md),
   [fluid–structure interaction](/methods/fluid-structure-interaction-on-overset-grids.md),
   [Maxwell's equations](/methods/maxwell-equations-on-overset-grids.md),
   verified with [twilight-zone flow](/methods/twilight-zone-flow.md);
   the [Yin–Yang grid](/definitions/yin-yang-grid.md) for spherical shells.
6. **Codes and test cases.** [PEGASUS](/software/pegasus.md),
   [PEGASUS 5](/software/pegasus-5.md), [DCF3D](/software/dcf3d.md),
   [CMPGRD](/software/cmpgrd.md), [Overture](/software/overture.md),
   [OVERFLOW](/software/overflow.md), [SUGGAR](/software/suggar.md),
   [OpenFOAM](/software/openfoam.md); [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md),
   [isentropic vortex](/benchmarks/isentropic-vortex.md),
   [lid-driven cavity](/benchmarks/lid-driven-cavity.md),
   [flow past a sphere](/benchmarks/flow-past-sphere.md),
   [shock–cylinder interaction](/benchmarks/shock-cylinder-interaction.md),
   [store separation](/benchmarks/store-separation.md),
   [multi-element airfoils](/benchmarks/multi-element-airfoil.md),
   [flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md).

## Catalog

- [Definitions](/definitions/index.md) — precise domain terms.
- [Methods](/methods/index.md) — algorithms and schemes.
- [Results](/results/index.md) — theorems and proved properties.
- [Software](/software/index.md) — codes embodying the methods.
- [Benchmarks](/benchmarks/index.md) — standard test problems.
- [Sources](/sources/index.md) — one page per ingested source.
- [Bibliography](/bibliography.md) — every work cited by the ingested sources.
