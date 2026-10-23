---
type: Benchmark
title: "Supersonic flow in a diamond-wedge channel"
description: "Steady Mach 2 Euler flow through a channel containing a diamond-shaped wedge, whose solution is a network of oblique shocks reflecting from the walls and intersecting, expansion fans and slip lines; used to show that implicit shock-tracking methods fit discontinuity surfaces of non-trivial topology on coarse meshes."
status: established
aliases: [diamond wedge in a channel, Mach 2 diamond, diamond airfoil in a tunnel, supersonic diamond]
tags: [benchmark, shock-tracking, dg]
timestamp: 2026-10-22T16:24:00Z
---

# Supersonic flow in a diamond-wedge channel

A uniform Mach 2 stream enters a channel with slip walls that contains a
symmetric diamond-shaped body. Oblique shocks form at the leading edge,
reflect from the channel walls and cross each other; expansion fans
leave the shoulders of the diamond, and a second shock system with a
slip line forms at the trailing edge. The steady solution therefore has
discontinuity surfaces that reflect, intersect and curve, with triple
points where they meet. For shock capturing this is a resolution test;
the sources here use it to show that an
[implicit shock-tracking](/methods/implicit-shock-tracking.md) method can
align mesh faces with every such surface on a coarse mesh, which
requires the method to handle a discontinuity topology it is not told
in advance.

## Runs in the sources

| Source | Method | Mesh | Result |
|---|---|---|---|
| [Luo et al. (2021)](/sources/luo-2021.md) §IV (second "D.") | moving DG with interface conservation enforcement, MDG(P1), started from a DG(P0) solution | 500 elements, 284 points, 66 boundary faces | shock reflection, shock–shock interaction and the expansion fan "well resolved" (Fig. 27) |
| [Huang & Zahr (2022)](/sources/huang-2022.md) §6.4.2 | high-order implicit shock tracking (HOIST), $p=q=2$, DistMesh initial mesh | 220 triangles, 201 after 19 element removals | all shocks and four generalized triple points tracked; the slip line from the trailing-edge triple point at $(3.16,0.26)$ not tracked on this coarse mesh (Fig. 30, Remark 23) |

Both use the steady Euler equations with slip walls and supersonic
inflow and outflow. Neither prints the channel or diamond dimensions in
its text; Huang & Zahr's figure axes are the only geometric information,
and Luo et al. give only the mesh counts. The two runs can therefore not
be checked against each other beyond the qualitative wave pattern.

The two methods differ in what defines the converged discontinuity:
Luo et al. enforce the interface condition with a central interior flux
and no Riemann solver, Huang & Zahr keep an upwind DG residual as the
constraint and use the central flux only in an enriched residual (see
[implicit shock tracking](/methods/implicit-shock-tracking.md)).
Huang & Zahr state that a shock-capturing method would need many more
elements near all discontinuity surfaces and triple points of this
problem; no capturing run is shown for comparison. Their solver
parameters for the case are listed in Table A.4.

## Qualifications

- Both sources judge the result by plots of the converged mesh and
  solution; no error measure is given, and no exact or reference
  solution is printed.
- The slip line is not fitted by Huang & Zahr's coarse mesh, so their
  solution is captured, not tracked, there.
- Luo et al. are read as an author manuscript and Huang & Zahr as arXiv
  v2, not the versions of record.

# Citations

- [Luo et al. (2021)](/sources/luo-2021.md) — §IV (second "D."), Fig. 27 (author manuscript).
- [Huang & Zahr (2022)](/sources/huang-2022.md) — §6.4.2, Remark 23, Fig. 30, Table A.4 (arXiv v2).
