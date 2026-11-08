---
type: Source
title: "Collins, Lozinski & Scovazzi (2023) — A penalty-free Shifted Boundary Method of arbitrary order"
description: "Penalty-free shifted boundary method, inspired by the non-symmetric Nitsche method, with inf–sup stability and convergence for arbitrary-order elements, optimal observed rates for Poisson, and a one-order loss for elasticity with Neumann conditions."
resource: "doi:10.1016/j.cma.2023.116301"
source_kind: paper
authors: [Collins J.H., Lozinski A., Scovazzi G.]
year: 2023
venue: "Comput. Methods Appl. Mech. Eng. 417:116301"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2023_Crossref_Computer_Methods_in_Applied_Mechanics_and_Engineering_Collins_A_penalty-free_Shifted_Boundary_Method_of_arbitrary_order.pdf"
tags: [shifted-boundary, finite-element, nitsche, high-order]
timestamp: 2026-11-08T18:24:00Z
---

# Summary

Collins, Lozinski and Scovazzi remove the penalty from the [shifted boundary method](/methods/shifted-boundary-method.md) with a non-symmetric Nitsche-type formulation, prove stability and convergence for any polynomial order, and verify optimal rates numerically.

# Version read

Preprint layout of the published paper (no journal header). §§1–3 read in full, §§4–5 for results. Title and authors match Crossref.

# Key claims

1. The penalty-free SBM is inspired by the non-symmetric Nitsche method and needs no penalty parameter (§1–§2). **Stated**
2. Stability follows from an inf–sup estimate; the energy error is $O(h^k)$ for degree $k$ (§3, Theorem 1). **Proved**
3. The duality $L^2$ estimate is half an order suboptimal, optimal under an extra mesh assumption (Theorem 2), while computations show $k+1$ (§3, §5). **Proved**/**Shown**
4. For linear elasticity with Neumann conditions the method loses one order because stresses are extrapolated at one order less (§4). **Shown**
5. Poisson tests with polynomial orders 1–5 give optimal $L^2$ and $H^1$ rates, robust to domain rotation (§5). **Shown**

# Notation map

| Collins, Lozinski & Scovazzi (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\delta$, $\mathbf M_h$ | distance vector $\mathbf d$, map $\mathcal M$ | $\delta$ is the Dirac delta in the registry |
| $k$ | polynomial degree |  |

# Reference list

60 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 4 (2026-11-08). This source is cited on:

- [Shifted boundary method](/methods/shifted-boundary-method.md)
