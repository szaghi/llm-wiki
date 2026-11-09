---
okf_version: "0.1"
---

# structured-mesh-methods — Knowledge Bundle

Structured and curvilinear mesh methods, as collected in a structured-mesh
bibliography of 1966–2026: how boundary-fitted coordinate systems and
curvilinear meshes are generated (algebraically, from elliptic, hyperbolic
or variational equations), adapted and moved, measured and optimized, and
how the discretization on them must treat metric terms to stay accurate and
to preserve a uniform flow.

**Start here:** the [Notation registry](/notation.md), which is normative for
every page ($\mathbf x$ physical and $\boldsymbol\xi=(\xi,\eta,\zeta)$
curvilinear coordinates, $\mathsf A=\partial\mathbf x/\partial\boldsymbol\xi$ and
$J=\det\mathsf A$, base vectors $\mathbf a_i$ and $\mathbf a^i$, the metric tensor
$g_{ij}$, the metric terms $J\mathbf a^i$, the grid velocity $\dot{\mathbf x}$,
control functions $P^i$, the monitor function $M$, the target Jacobian
$\mathsf W$ and $\mathsf T=\mathsf A\mathsf W^{-1}$), and the [update log](/log.md).

**Corpus:** 38 of the 56 archived papers ingested in 4 chunks (two archive files are not the papers their names announce; see the issues digest). Chunk 1 holds
the founding papers of 1966–2001: [Winslow (1966)](/sources/winslow-1966.md)
builds meshes from inverted Laplace equations;
[Gordon & Hall (1973)](/sources/gordon-1973.md) introduce transfinite
interpolation; [Thompson, Thames & Mastin (1974)](/sources/thompson-1974.md)
generate body-fitted coordinates for any number of bodies;
[Thomas & Lombard (1979)](/sources/thomas-1979.md) formulate the geometric
conservation law; [Steger & Sorenson (1979)](/sources/steger-1979.md) cluster
points automatically at a boundary; [Steger & Chaussee (1980)](/sources/steger-1980.md)
generate grids by hyperbolic marching;
[Brackbill & Saltzman (1982)](/sources/brackbill-1982.md) adapt meshes
variationally; the review of [Thompson, Warsi & Mastin (1982)](/sources/thompson-1982.md)
fixes the classification and the error analysis;
[Huang, Ren & Russell (1994)](/sources/huang-1994.md) derive moving mesh
PDEs; and [Knupp (2001)](/sources/knupp-2001.md) gives an algebraic theory of
mesh quality metrics. Chunk 2 (2002–2019) turns to the discretization on
curvilinear meshes and to curved high-order meshes: high-order compact
schemes on curvilinear and deforming meshes ([Visbal & Gaitonde 2002](/sources/visbal-2002.md)),
metric identities for spectral elements ([Kopriva 2006](/sources/kopriva-2006.md)),
free-stream preservation of WENO and weighted compact schemes
([Nonomura et al. 2010](/sources/nonomura-2010.md), [Deng et al. 2011](/sources/deng-2011.md),
[Deng et al. 2013](/sources/deng-2013.md), [Zhu & Hu 2019](/sources/zhu-2019.md)),
moving meshes for conservation laws ([Tang & Tang 2003](/sources/tang-2003.md)),
and the curving, validation and untangling of high-order meshes
([Xie et al. 2013](/sources/xie-2013.md), [Johnen et al. 2013](/sources/johnen-2013.md),
[Toulorge et al. 2013](/sources/toulorge-2013.md)).
Chunk 3 (2019–2022) brings target-matrix mesh optimization for high-order
and ALE meshes with hr-adaptivity ([Dobrev et al. 2019](/sources/dobrev-2019.md),
[2020](/sources/dobrev-2020.md), [2022](/sources/dobrev-2022.md)),
free-stream preserving WENO for MHD ([Yu et al. 2020](/sources/yu-2020.md)),
stable flux reconstruction on curved elements ([Cicchino et al. 2022](/sources/cicchino-2022.md)),
Lagrangian MHD on curvilinear elements ([Nikl et al. 2022](/sources/nikl-2022.md)),
shock fitting on structured grids ([Assonitis et al. 2022](/sources/assonitis-2022.md)),
anisotropic body-fitted adaptation ([El Aouad et al. 2022](/sources/elaouad-2022.md))
and neural-network grid generation ([Chen et al. 2022](/sources/chen-2022.md)).
Chunk 4 (2022–2024) adds further free-stream preserving upwind and WENO
schemes ([Han et al. 2022](/sources/han-2022.md), [Su et al. 2023](/sources/su-2023.md),
[Su et al. 2023b](/sources/su-2023-b.md)), mesh morphing to implicit
geometries and GPU mesh optimization ([Barrera et al. 2023](/sources/barrera-2023.md),
[Camier et al. 2023](/sources/camier-2023.md)), exact correction and cavity
remeshing of curved meshes ([Rochery & Loseille 2023](/sources/rochery-2023.md)),
the open-source generator NekMesh ([Green et al. 2024](/sources/green-2024.md)),
mapped-mesh AMR for detonations ([Peng & Deiterding 2023](/sources/peng-2023.md))
and a neural generator trained with coarse-mesh data ([Chen et al. 2023](/sources/chen-2023.md)).

## Reading guide

1. **What a structured grid is.**
   [Boundary-fitted coordinate system](/definitions/boundary-fitted-coordinate-system.md)
   is the hub: the mapping view, the geometric meaning of the metric, and the
   families of generators.
2. **Generating the grid.**
   [Transfinite interpolation](/methods/transfinite-interpolation.md)
   (algebraic, explicit, not always valid),
   [elliptic grid generation](/methods/elliptic-grid-generation.md)
   (smooth, with control functions and boundary clustering),
   [hyperbolic grid generation](/methods/hyperbolic-grid-generation.md)
   (marched from a body), and
   [variational grid generation](/methods/variational-grid-generation.md)
   (minimizing measures of smoothness, orthogonality and volume).
3. **Adapting and moving the grid.**
   The [equidistribution principle](/definitions/equidistribution-principle.md)
   and the [moving mesh PDEs](/methods/moving-mesh-pde.md) built on it.
4. **Discretizing on the grid.**
   [Free-stream preservation](/properties/free-stream-preservation.md)
   (discrete metric identities), achieved by
   [conservative metric evaluation](/methods/conservative-metric-evaluation.md),
   and the [geometric conservation law](/properties/geometric-conservation-law.md)
   (moving grids); the [truncation error the grid adds](/results/grid-induced-truncation-error.md).
5. **Measuring the grid.**
   [Mesh quality metrics](/definitions/mesh-quality-metric.md) and the
   [validity of high-order curvilinear elements](/definitions/high-order-mesh-validity.md).
6. **Curved high-order meshes.**
   [High-order mesh curving](/methods/high-order-mesh-curving.md):
   elastic analogy and untangling by optimization.
7. **Optimizing and adapting meshes.**
   [Target-matrix optimization](/methods/target-matrix-optimization.md)
   (node movement toward targets, hr-adaptivity) and
   [anisotropic mesh adaptation](/methods/anisotropic-mesh-adaptation.md).
8. **Applications and new tools.**
   [Shock fitting on structured grids](/methods/shock-fitting.md) and
   [neural-network mesh generation](/methods/neural-network-mesh-generation.md).
9. **Software.** [NekMesh](/software/nekmesh.md), an open-source high-order
   mesh generator.

## Catalogs

- [Definitions](/definitions/index.md)
- [Methods](/methods/index.md)
- [Results](/results/index.md)
- [Properties](/properties/index.md)
- [Software](/software/index.md)
- [Sources](/sources/index.md)
- [Bibliography](/bibliography.md) — every work cited by an ingested source.
