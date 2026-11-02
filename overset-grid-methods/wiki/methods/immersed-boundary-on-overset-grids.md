---
type: Method
title: "Immersed boundaries on overlapping grids"
description: "Combining immersed-boundary methods with overset grids: a body-attached refined grid carries the immersed boundary over a coarse background, so local resolution follows a moving body; the sources differ in what moves, how data are transferred and how mass is conserved."
status: established
aliases: [overset immersed boundary method, overset-CURVIB, overset BC-enforced IBM]
tags: [immersed-boundary, moving-grid, incompressible, fsi]
timestamp: 2026-11-02T15:06:00Z
---

# Immersed boundaries on overlapping grids

An immersed-boundary method represents a body on a grid that does not conform to it, which needs fine uniform resolution wherever the body may go. Attaching a refined component grid $G_k$ to the body and overlapping it with a coarse background lets the resolution travel with the body: the immersed boundary lives on the component grid, and [inter-grid interpolation](/methods/inter-grid-interpolation.md) couples it to the background as on any [overset grid](/definitions/overset-grid.md).

## Variants

| source | immersed boundary | what the component grid does | transfer | conservation |
|---|---|---|---|---|
| [Hedayat et al. (2022)](/sources/hedayat-2022.md) | sharp-interface curvilinear (CURVIB) | body-fitted curvilinear grids that move with the bodies, solved in a non-inertial frame | trilinear, applied as a sparse matrix | flux correction over each blanked region and overset interface (§2.4.1) |
| [Zhao et al. (2022)](/sources/zhao-2022.md) | diffused-interface, boundary-condition-enforced | refined Cartesian grid that only translates with the centre of mass; rotation and deformation carried by the Lagrangian points | single nearest donor, gradient-based linear reconstruction | not discussed |
| [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) | penalization of the domain left by the foreground grid | rigid foreground grid moving with the body | fluxes through a compact hybrid stencil, no fringe interpolation | conservative in the no-shift limit |

- Hedayat et al. (2022) extend a fixed-grid overset-CURVIB solver to moving grids with a parallel in-core assembly ([parallel overset grid assembly](/methods/parallel-overset-grid-assembly.md)); when an overset interface crosses an immersed body they blank the region around the body in the other grid rather than give solid nodes approximate velocities (§2.4, Fig. 11).
- Zhao et al. (2022) keep the overset grid Cartesian and unrotated so it is never regenerated; two acceptor layers on each grid exchange data, and the inactive background cells around the body are [holes](/methods/hole-cutting.md) (§II).
- Bergmann et al. (2022b) handle a sedimenting cylinder whose foreground grid leaves the physical domain with a penalization term that does not alter the space–time fluxes ([ADER schemes on overlapping grids](/methods/ader-on-overset-grids.md), §6).

## Reported gains

Hedayat et al. (2022) need about 29 M nodes for four self-propelled fish against at least 470 M for a single grid of similar resolution (§3.5). Zhao et al. (2022) report 31–94 % fewer cells and 26–92 % less CPU time than their single-mesh method on four tests (§III). Bergmann et al. (2022b) use 9267 cells for a sedimenting cylinder against $10^5$–$10^6$ in compared studies (§6).

## Qualifications

- Zhao et al. (2022) argue second order for their single-donor reconstruction by a Taylor expansion only; no convergence study of the transfer is shown (§II C).
- Hedayat et al. (2022) state that implicit hole cutting costs about an order of magnitude more than explicit hole cutting, without a measurement (§2.2.2).
- Delcour et al. (2022) contrast Chimera meshes with immersed-boundary methods, which they find poor in boundary layers ([Delcour et al. 2022](/sources/delcour-2022.md), §1).

# Citations

- [Hedayat et al. (2022)](/sources/hedayat-2022.md) — §2.1–2.4, §3, §4.
- [Zhao et al. (2022)](/sources/zhao-2022.md) — §II, §III.
- [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) — §6.
- [Delcour et al. (2022)](/sources/delcour-2022.md) — §1.
