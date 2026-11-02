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

**Corpus:** chunk 1 of the archive ingested: the founding papers of
1983–2005. [Benek et al. (1983)](/sources/benek-1983.md) and
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
bodies and unstructured grids in SUGGAR.

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
   valid assemblies.
3. **Coupling and accuracy.** [Inter-grid interpolation](/methods/inter-grid-interpolation.md),
   [explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md),
   the [interpolation order and overlap requirements](/results/interpolation-order-requirement.md),
   and the [conservative overset interface](/methods/conservative-overset-interface.md).
4. **Motion and physics.** [Moving overset grids](/methods/moving-overset-grid.md),
   [incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md),
   verified with [twilight-zone flow](/methods/twilight-zone-flow.md);
   the [Yin–Yang grid](/definitions/yin-yang-grid.md) for spherical shells.
5. **Codes and test cases.** [PEGASUS](/software/pegasus.md),
   [PEGASUS 5](/software/pegasus-5.md), [DCF3D](/software/dcf3d.md),
   [CMPGRD](/software/cmpgrd.md), [SUGGAR](/software/suggar.md);
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
