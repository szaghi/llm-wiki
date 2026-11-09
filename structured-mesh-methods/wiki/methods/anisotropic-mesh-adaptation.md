---
type: Method
title: "Anisotropic mesh adaptation"
description: "Adapting the size, shape and orientation of elements to a metric tensor built from solution or geometry derivatives (Hessians, recovered gradients, edge-based error estimates), so that elements stretch along features; combined with node relocation and edge swapping it can turn an immersed level-set description into a body-fitted anisotropic mesh."
status: established
aliases: [metric-based adaptation, anisotropic remeshing, body-fitted anisotropic adaptation]
tags: [adaptation, anisotropic, metric-tensor, unstructured]
timestamp: 2026-11-08T20:46:00Z
---

# Anisotropic mesh adaptation

Anisotropic adaptation prescribes, at every point, a metric tensor
$\mathbb M$ ([notation](/notation.md)) whose eigenvectors and eigenvalues set
the directions and lengths of the desired edges, and remeshes so that edges
have unit length in that metric. It concentrates and stretches elements
along boundary layers, interfaces and shocks while keeping the node count
under control, as the [equidistribution principle](/definitions/equidistribution-principle.md)
does for structured grids.

## From an immersed geometry to a body-fitted mesh

[El Aouad, Larcher & Hachem (2022)](/sources/elaouad-2022.md) start from an
unstructured simplicial mesh in which a body is described by a level set.
First, a metric built from the level-set gradients (edge-based error
estimate with gradient recovery, stretching factors that keep the total
node count fixed) produces elements stretched along the interface — which
still crosses them. Second, a purely geometric step isolates the cut
elements, relocates the nodes closest to the interface onto it (an
r-adaptation by closest-point projection) and swaps the edges of the
remaining cut elements, preserving orientation. The result is a sharp,
anisotropic, body-fitted mesh with unchanged numbers of vertices and
elements; the order of the two steps matters. Two-dimensional cases with a
variational multiscale Navier–Stokes solver show the procedure.

# Citations

- [El Aouad, Larcher & Hachem (2022)](/sources/elaouad-2022.md) — method, test cases, conclusions.
