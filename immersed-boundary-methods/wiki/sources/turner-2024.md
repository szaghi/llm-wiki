---
type: Source
title: "Turner, Seo & Mittal (2024) — A high-order sharp-interface immersed boundary solver for high-speed flows"
description: "A ghost-cell immersed boundary method for compressible flow with shocks whose ghost values come directly from a high-order Taylor polynomial fitted by weighted least squares, in a compact finite-difference solver with hyperviscosity; third order or higher kept in supersonic tests."
resource: "doi:10.1016/j.jcp.2023.112748"
source_kind: paper
authors: [Turner J.M., Seo J.H., Mittal R.]
year: 2024
venue: "J. Comput. Phys. 500:112748"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2024_Crossref_Journal_of_Computational_Physics_Turner_A_high-order_sharp-interface_immersed_boundary_solver_for_hi.pdf"
tags: [ghost-cell, high-order, compressible, shock, membrane]
timestamp: 2026-11-08T18:35:00Z
---

# Summary

Turner, Seo and Mittal extend Seo and Mittal's high-order [ghost-cell method](/methods/ghost-cell-method.md) to the fully compressible Navier–Stokes equations with shock–boundary interaction in the ViCAS3D solver (compact differences, filters, hyperviscosity). Ghost values are read off a Taylor polynomial fitted by weighted least squares through fluid points and the boundary condition, without a linear extrapolation step, with new weights for stability; zero-thickness membranes use boundary cells on both sides ([high-order immersed boundary treatments](/methods/high-order-immersed-boundary.md)).

# Version read

Version of record, J. Comput. Phys. 500, 112748 (2024). §§1–2 read, §§3–4 tests in outline.

# Key claims

1. Image-point ghost-cell methods with linear interpolation or extrapolation do not give a truly high-order boundary approximation (§1). **Stated**
2. Ghost values from a weighted-least-squares Taylor polynomial including the boundary condition give user-selectable order; weights concentrated near the origin are more stable than cosine weights for nonlinear high-speed flow (§2). **Stated**
3. At $M=0.5$, $Re=40$ compressibility lengthens the cylinder recirculation, in agreement with body-fitted DNS (§3). **Shown**
4. Third-order or higher accuracy is maintained even for supersonic conditions (§3–§4). **Shown**

# Notation map

| Turner, Seo & Mittal (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $c_{ijk}$ | Taylor coefficients of the fit | page-local |
| $V$, $W$ | Vandermonde and weight matrices | page-local |

# Reference list

50 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 5 (2026-11-08). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Shock–obstacle interaction](/benchmarks/shock-obstacle-interaction.md)
- [Ghost-cell immersed boundary method](/methods/ghost-cell-method.md)
- [High-order immersed boundary treatments for compressible flow](/methods/high-order-immersed-boundary.md)
