---
type: Method
title: "Wall-distance hole cutting"
description: "Point classification by a wall-distance criterion — each point is kept on the grid whose wall is nearest, the others become holes or receptors — as the basis of implicit hole cutting on unstructured grids, with the cost of the wall-distance computation as the bottleneck that parallel advancing-front and exact pre-classification methods attack."
status: established
aliases: [wall-distance-based implicit hole cutting, pre-classification overset grid assembly]
tags: [hole-cutting, domain-connectivity, unstructured, parallel]
timestamp: 2026-11-02T15:26:00Z
---

# Wall-distance hole cutting

In implicit hole cutting a point is kept as a discretization point on the grid that resolves it best and becomes a receptor or a hole elsewhere ([implicit hole cutting](/methods/implicit-hole-cutting.md)). A common "best" criterion in the later sources is wall distance $d_w$ (registry §8): near a body, the body's own grid should win.

## Cost of the wall distance

Computing $d_w$ for every point of every grid is the expensive step. [Xiao et al. (2023)](/sources/xiao-2023.md) accelerate it with a parallel advancing-front algorithm inside a parallel implicit-hole-cutting assembly for unstructured grids, with a bookkeeping alternating digital tree for the donor search ([donor search](/methods/donor-search.md), [parallel overset grid assembly](/methods/parallel-overset-grid-assembly.md)).

## Classification before the donor search

[Oh et al. (2024)](/sources/oh-2024.md) reverse the usual order of assembly: points are classified by the wall-distance criterion first, and the donor search runs only on the reduced set of query points. The wall distance is evaluated exactly against the discretized surface, which matters when bodies are very close; the cost is kept down by a bounded formulation and a conservative relation between cheap vertex-based distances and exact element-based distances, so the exact computation is done only where the bound cannot decide, with volumetric ray tracing and octree voxelization against "distance flooding" and load balancing in parallel. In all their tests the pre-classification assembly is faster than post-classification assembly without changing the donor search (alternating digital tree).

## Qualifications

- Hedayat et al. (2022) judge implicit hole cutting about an order of magnitude more expensive than explicit cutting for grids moved every step, without measurement ([Hedayat et al. 2022](/sources/hedayat-2022.md), §2.2.2); the wall-distance work above targets exactly that cost.

# Citations

- [Xiao et al. (2023)](/sources/xiao-2023.md) — Abstract, §2–§3.
- [Oh et al. (2024)](/sources/oh-2024.md) — Abstract, Conclusions.
- [Hedayat et al. (2022)](/sources/hedayat-2022.md) — §2.2.2.
