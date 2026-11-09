---
type: Method
title: "High-order mesh curving"
description: "A posteriori generation of curved high-order meshes: a straight-sided mesh is generated first, its boundary entities are curved onto the CAD geometry, and the interior is deformed — by a linear elasticity analogy with the boundary displacements as loads, or by optimization of node positions with log-barriers on the element distortion that untangles invalid elements locally."
status: established
aliases: [a posteriori curving, curved mesh generation, mesh untangling, elastic analogy, high-order mesh optimization]
tags: [high-order-mesh, curving, untangling, optimization]
timestamp: 2026-11-08T20:37:00Z
---

# High-order mesh curving

High-order discretizations need curved elements to represent curved
boundaries; without curved mesh generators their benefits are lost
([Xie et al. 2013](/sources/xie-2013.md)). Methods are **direct**, building
the curved mesh from the CAD model, or **a posteriori**, curving a mesh of
straight-sided elements; the latter are preferred because they reuse mature
linear meshers. Curving only the boundary entities often produces invalid
elements near high curvature ([validity](/definitions/high-order-mesh-validity.md)),
which local operations (swaps, deletions, node relocation) or remeshing try
to repair.

## Elastic analogy

[Xie et al. (2013)](/sources/xie-2013.md) treat the straight-sided mesh as an
undeformed elastic body. High-order nodes (Fekete points) are placed on the
curved boundary through the NURBS parameter space; their displacement onto
the true surface is the Dirichlet load of a high-order finite element
solution of linear elasticity, which moves the interior nodes. Any element
type and hybrid meshes are handled; anisotropic boundary-layer meshes are
curved layer by layer. The quality depends strongly on Poisson's ratio and
not on Young's modulus; $\nu=0.4$ maximizes the minimum distortion and keeps
the linear system well conditioned, and quality improves toward the
incompressible limit. Wing–body meshes with stretching above 200 are
produced.

## Optimization with moving barriers

[Toulorge et al. (2013)](/sources/toulorge-2013.md) untangle a possibly
invalid curved mesh by unconstrained optimization of the node positions: the
objective combines the distance of the high-order nodes from their
straight-sided positions with a log-barrier that keeps the distortion
$\mathcal D$ (bounded through Bézier expansions) above a threshold. For a
tangled mesh the barrier starts below the current minimum and is moved
step by step into the valid range; a further term bounds the largest
Jacobian in boundary layers. Optimization is local, in non-overlapping
groups of a few layers of elements around each invalid element with fixed
outer vertices, and boundary nodes may slide on the CAD geometry.

They also show that validity is not enough: curved elements reduce the
stable explicit time step, and three triangles with equal area and equal
constant $J$ can have different stable steps. A barrier on the smallest
eigenvalue of the element metric tensor recovers larger stable steps for
discontinuous Galerkin shallow-water computations.

# Citations

- [Xie et al. (2013)](/sources/xie-2013.md) — §1–§4, §6.
- [Toulorge et al. (2013)](/sources/toulorge-2013.md) — §1–§4, §6–§7.
