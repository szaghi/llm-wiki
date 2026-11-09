---
type: Definition
title: "Boundary-fitted coordinate system"
description: "A structured (curvilinear) grid viewed as a one-to-one mapping from a rectangular computational domain onto the physical domain, with coordinate lines coincident with every boundary; the equations are transformed so that all computation runs on a uniform square mesh, and the generation methods divide into conformal, orthogonal, algebraic (interpolation), elliptic, hyperbolic and variational families."
status: established
aliases: [body-fitted coordinates, boundary-conforming coordinates, curvilinear grid, structured grid, natural coordinate system]
tags: [structured-grid, curvilinear-grid, grid-generation, classification]
timestamp: 2026-11-08T21:07:00Z
---

# Boundary-fitted coordinate system

A **boundary-fitted coordinate system** is a curvilinear coordinate system
$\boldsymbol\xi$ on the physical domain $\Omega$ whose coordinate lines
(surfaces in 3-D) coincide with all boundaries. It is equivalently a
one-to-one mapping $\mathbf x(\boldsymbol\xi)$ from a rectangular
computational domain $\hat\Omega$ onto $\Omega$; a structured grid is the
image of a uniform lattice of $\hat\Omega$, so each point $\mathbf x_{\mathbf i}$
is identified by its index $\mathbf i$ and knows its neighbours
([Gordon & Hall 1973](/sources/gordon-1973.md);
[Thompson, Warsi & Mastin 1982](/sources/thompson-1982.md)).

## Why it is used

The partial differential equations are transformed analytically so that
$\boldsymbol\xi$ becomes the independent variable; every computation then
runs on a fixed square mesh in $\hat\Omega$, boundary conditions are imposed
at grid points without interpolation, and moving boundaries are handled on
the same fixed computational mesh
([Thompson, Thames & Mastin 1974](/sources/thompson-1974.md)). Thompson et al.
call the result a trade: simple equations with complex boundaries are
exchanged for complex equations with simple boundaries. The coordinate
lines can be concentrated where gradients are large, statically or by
coupling to the solution
([Thompson et al. 1982](/sources/thompson-1982.md)).

## Geometric meaning of the metric

With the covariant base vectors $\mathbf a_i$ and the metric tensor
$g_{ij}=\mathbf a_i\cdot\mathbf a_j$ ([notation](/notation.md)), $g_{ij}$
($i\ne j$) is proportional to the cosine of the angle between two coordinate
lines and vanishes for an orthogonal grid, $\sqrt{g_{ii}}$ is proportional to
arc length along the $\xi^i$ line, $J=\sqrt{\det g_{ij}}$ is the cell volume,
and $\sqrt{g_{ii}/g_{jj}}$ the cell aspect ratio; arc length along any curve
is $ds^2=g_{ij}\,d\xi^i d\xi^j$
([Thompson et al. 1982](/sources/thompson-1982.md), Section B). Orthogonality
is not required: a nonorthogonal system only means the equations must be
transformed in full rather than through the scale factors of orthogonal
coordinates, and orthogonality is incompatible with an arbitrary point
distribution on the boundary
([Thompson et al. 1974](/sources/thompson-1974.md)).

## Families of generation methods

The review of Thompson, Warsi and Mastin (1982) classifies the methods as:

- **conformal mapping** — elementary complex transformations, series,
  Schwarz–Christoffel, integral equations; orthogonal, but solving a Laplace
  problem;
- **orthogonal and nearly orthogonal** systems, by elliptic or hyperbolic
  equations or by orthogonal trajectories;
- **algebraic** generation by interpolation among the boundaries —
  [transfinite interpolation](/methods/transfinite-interpolation.md);
- **elliptic** generators —
  [elliptic grid generation](/methods/elliptic-grid-generation.md);
- **hyperbolic** generators, marched from a boundary —
  [hyperbolic grid generation](/methods/hyperbolic-grid-generation.md);
- **variational** generators, which minimize integral measures of mesh
  properties ([variational grid generation](/methods/variational-grid-generation.md)).

Line spacing is controlled by terms in the generating equations or by
subsequent one-dimensional stretching functions; grids may be patched from
subregions; and adaptive or time-dependent systems follow the solution or
moving boundaries
([moving mesh PDEs](/methods/moving-mesh-pde.md),
[equidistribution principle](/definitions/equidistribution-principle.md)).

## Accuracy and conservation

The grid enters the solution error through the stretching and skewness of
the coordinate lines ([grid-induced truncation error](/results/grid-induced-truncation-error.md))
and through the discrete metric terms, which must satisfy the metric
identities and, on moving grids, the geometric conservation law
([free-stream preservation](/properties/free-stream-preservation.md),
[geometric conservation law](/properties/geometric-conservation-law.md)).
Element shape, size and validity are measured by
[mesh quality metrics](/definitions/mesh-quality-metric.md).

## Unstructured curvilinear meshes

The same mapping view applies element by element to high-order curved
meshes, where each element is the image of a reference element by a
polynomial map whose positivity must be checked
([validity](/definitions/high-order-mesh-validity.md)) and which is usually
obtained by curving a straight-sided mesh
([high-order mesh curving](/methods/high-order-mesh-curving.md);
[Xie et al. 2013](/sources/xie-2013.md)).

## Curvilinear meshes in Lagrangian methods

High-order curvilinear finite elements let a Lagrangian mesh follow
strongly deforming flow longer without tangling or imprinting on the
solution: [Nikl, Kuchařík & Weber (2022)](/sources/nikl-2022.md) build
conservative high-order Lagrangian resistive MHD on such meshes, with
continuous kinematic and discontinuous thermodynamic spaces and a magnetic
field on spaces of the de Rham complex whose Piola maps keep the magnetic
flux invariant, so that mass, momentum, magnetic flux and energy are
conserved and the field stays divergence free. Mesh optimization for the
arbitrary Lagrangian–Eulerian variant is on
[target-matrix optimization](/methods/target-matrix-optimization.md).

## Block-structured refinement of mapped meshes

[Peng & Deiterding (2023)](/sources/peng-2023.md) run a block-structured
adaptive finite-volume framework on structured curvilinear meshes by
mapping its Cartesian index space onto the physical mesh: Riemann solvers
work in face-aligned frames through rotation matrices, restriction and
prolongation are weighted by the unequal volumes of mapped cells, and a
coarse–fine flux correction keeps the scheme conservative; detonations in
a pipe bend and a round tube are computed.

## Field-aligned coordinates through X-points

Coordinates aligned with a magnetic field exploit the anisotropy of tokamak
turbulence but are singular where the poloidal field vanishes (X- and
O-points, $J=0$). [Shukla et al. (2026)](/sources/shukla-2026.md) build a
multi-block field-aligned grid whose blocks conform to the separatrix and
meet at the X-point with no gap, and never evaluate geometric quantities or
fluxes at the singular points, because their discontinuous Galerkin scheme
uses quadrature nodes interior to cells and faces; between blocks with
different mappings, a common flux per face keeps the scheme consistent.
For high-order ALE MHD on curvilinear meshes,
[Mao & Xi (2026)](/sources/mao-2026.md) smooth the moving mesh by solving
$-\epsilon\nabla^2\mathbf x_{\mathrm{new}}+\mathbf x_{\mathrm{new}}=\mathbf x_{\mathrm{old}}$
with fixed boundary nodes ($\epsilon\approx10^{-4}$), triggered by quality
indicators, before structure-preserving remapping.

# Citations

- [Gordon & Hall (1973)](/sources/gordon-1973.md) — mapping view of curvilinear coordinates.
- [Thompson, Thames & Mastin (1974)](/sources/thompson-1974.md) — introduction and transformation.
- [Thompson, Warsi & Mastin (1982)](/sources/thompson-1982.md) — Sections A–B, classification C–Q.
- [Xie et al. (2013)](/sources/xie-2013.md) — §1.
- [Nikl, Kuchařík & Weber (2022)](/sources/nikl-2022.md) — abstract, §3, conclusions.
- [Peng & Deiterding (2023)](/sources/peng-2023.md) — §2.
- [Shukla et al. (2026)](/sources/shukla-2026.md) — §1–§2, Appendix A.
- [Mao & Xi (2026)](/sources/mao-2026.md) — §3.3.
