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

**Corpus:** 10 of the 56 archived papers ingested in 1 chunk. Chunk 1 holds
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
mesh quality metrics.

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
   (discrete metric identities) and the
   [geometric conservation law](/properties/geometric-conservation-law.md)
   (moving grids); the [truncation error the grid adds](/results/grid-induced-truncation-error.md).
5. **Measuring the grid.**
   [Mesh quality metrics](/definitions/mesh-quality-metric.md).

## Catalogs

- [Definitions](/definitions/index.md)
- [Methods](/methods/index.md)
- [Results](/results/index.md)
- [Properties](/properties/index.md)
- [Sources](/sources/index.md)
- [Bibliography](/bibliography.md) — every work cited by an ingested source.
