---
type: Method
title: "High-order immersed boundary treatments for compressible flow"
description: "Boundary treatments that keep third- or higher-order accuracy at an immersed boundary for compressible flows with shocks: inverse Lax–Wendroff ghost values, high-order polynomial weighted-least-squares ghost values with or without image points, ghost values from discontinuous Galerkin polynomials, summation-by-parts embedded boundaries, and hybrid compact–WENO interiors; what each needs and the orders reported."
status: established
aliases: [high-order IB, high-order ghost-cell method, high-order embedded boundary]
tags: [high-order, ghost-cell, compressible, shock, sharp-interface]
timestamp: 2026-11-08T18:32:00Z
---

# High-order immersed boundary treatments for compressible flow

Second-order [ghost-cell methods](/methods/ghost-cell-method.md) interpolate
at an image point and extrapolate linearly along the normal; with a high-order
interior scheme that linear step caps the accuracy at the boundary. [Turner et al. (2024)](/sources/turner-2024.md),
§1, note that ghost-cell image-point methods with linear interpolation or
extrapolation, inverse-distance weighting or least squares with linear
extrapolation "do not produce a truly high-order approximation of the
immersed boundary". The sources pursue several routes.

| route | idea | interior scheme | order reported | source |
|---|---|---|---|---|
| inverse Lax–Wendroff | normal derivatives from the PDE and boundary data, Taylor-expanded ghost values | fifth-order WENO | 5 | [Tan & Shu (2010)](/sources/tan-2010.md) ([ILW](/methods/inverse-lax-wendroff.md)) |
| simplified ILW with auxiliary points | fewer ILW terms, interpolation to auxiliary points then extrapolation | third/fifth-order WENO | 3, 5 | [Liu et al. (2024)](/sources/liu-2024.md) |
| polynomial WLS ghost values | Taylor polynomial fitted by weighted least squares through the ghost point, fluid points and the boundary condition; ghost value read off directly, no linear extrapolation | compact differences with filters and hyperviscosity | $\ge3$, also supersonic | [Turner et al. (2024)](/sources/turner-2024.md) |
| no image point | constrained weighted least squares with the boundary condition at the grid-line intersection | upwind compact scheme | 3 | [Huang et al. (2024)](/sources/huang-2024.md) |
| DG polynomial at the image point | image-point value from the DG polynomial of its cell, no wide stencil | DG/direct DG on adaptive octree grids | DG order in smooth regions | [Qi et al. (2024)](/sources/qi-2024.md) |
| SBP embedded boundary | conservative, energy-stable boundary closures on cut grid lines | centred, up to sixth order | 4 globally | [Sharan et al. (2022)](/sources/sharan-2022.md) |
| hybrid compact–WENO | compact in smooth regions, WENO at shocks; bilinear image-point ghost values | fifth-order compact–WENO | — (accuracy and cost compared with WENO) | [Marashi & Hejranfar (2025)](/sources/marashi-2025.md) |

## Notes on the routes

- Turner et al. (2024, §2) replace the cosine weights of Seo and Mittal's
  low-Mach version by weights concentrated near the origin, which they find
  more stable for nonlinear high-speed problems, and treat zero-thickness
  membranes with boundary cells on both sides.
- Huang et al. (2024, §2) avoid image points because finding them near complex
  boundaries or in narrow gaps costs extra computation; one layer of ghost
  points suffices for global third order.
- Liu et al. (2024) show by eigenvalue analysis that the original simplified
  ILW is stable at the periodic CFL number for any cut fraction only at third
  order; placing auxiliary points (parameter $\alpha$) restores stability at
  higher order with fewer ILW terms.
- Marashi and Hejranfar (2025) report the hybrid compact–WENO scheme about 2.9
  times faster than WENO in one test, with somewhat more oscillation at shocks.

Shock problems used across the routes are collected on
[shock–obstacle interaction](/benchmarks/shock-obstacle-interaction.md).

# Citations

- [Tan & Shu (2010)](/sources/tan-2010.md) — §2–§3.
- [Sharan et al. (2022)](/sources/sharan-2022.md) — SBP embedded-boundary closures and global order (§4).
- [Liu et al. (2024)](/sources/liu-2024.md) — §1–§4.
- [Turner et al. (2024)](/sources/turner-2024.md) — §1–§4.
- [Huang et al. (2024)](/sources/huang-2024.md) — §1–§3.
- [Qi et al. (2024)](/sources/qi-2024.md) — §2–§4.
- [Marashi & Hejranfar (2025)](/sources/marashi-2025.md) — §2–§4.
