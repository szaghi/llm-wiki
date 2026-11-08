---
type: Source
title: "Atallah, Canuto & Scovazzi (2022) — The high-order Shifted Boundary Method and its analysis"
description: "High-order shifted boundary method: Taylor expansions of order m shift Dirichlet data from the true to a piecewise-linear surrogate boundary in a Nitsche formulation, with coercivity, inf–sup and optimal H1 and L2 error estimates for Poisson and Stokes, and optimal rates without high-order body-fitted meshes or cut-cell quadrature."
resource: "doi:10.1016/j.cma.2022.114885"
source_kind: paper
authors: [Atallah N.M., Canuto C., Scovazzi G.]
year: 2022
venue: "Comput. Methods Appl. Mech. Eng. 394:114885"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2022_Crossref_Computer_Methods_in_Applied_Mechanics_and_Engineering_Atallah_The_high-order_Shifted_Boundary_Method_and_its_analysis.pdf"
tags: [shifted-boundary, high-order, finite-element, nitsche, analysis]
timestamp: 2026-11-08T18:12:00Z
---

# Summary

Atallah, Canuto and Scovazzi extend the [shifted boundary method](/methods/shifted-boundary-method.md)
to arbitrary polynomial order: Taylor expansions of order $m$ shift the
boundary data to the surrogate boundary, which may stay piecewise linear, and
the method keeps optimal convergence. They prove coercivity, an inf–sup
condition for Stokes and optimal $H^1$ and $L^2$ estimates.

# Version read

Accepted manuscript from the Politecnico di Torino repository (CC-BY-NC-ND),
with the published citation printed on its cover page. §§1–5 read in full;
the error estimates and numerical results read for their statements. Title
and authors match Crossref.

# Key claims

1. Optimal accuracy holds for any order of the finite-element spaces although the surrogate boundary is piecewise linear, bypassing high-order body-fitted meshes and cut-cell data structures (Abstract, §1). **Stated**/**Proved**
2. Geometry representations need not be watertight at scales finer than the grid (§1). **Stated**
3. The Nitsche penalty is paired with the first-order shift operator to enable an Aubin–Nitsche $L^2$ estimate (§3). **Derived**
4. Coercivity (Poisson) and a uniform inf–sup condition (Stokes, stabilized equal order or Taylor–Hood) hold under an assumption on the distance between surrogate and true boundary (§5). **Proved**
5. Bramble, Dupont and Thomée's boundary approximation is impractical with corners; Bramble and King require a distance $O(h^2)$, nearly body-fitting (§1). **Stated**
6. The primal Stokes formulation loses one order relative to the mixed one (§2, remark). **Stated**

# Notation map

| Atallah et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tilde\Omega_h$, $\tilde\Gamma_h$, $\mathbf M_h$, $\mathbf d$ | surrogate domain and boundary, map, distance vector | as on the method page |
| $S^m_h$ | $S^m_h$ | Taylor shift operator of order $m$ |
| $\gamma$, $\delta$ | Nitsche and pressure-stabilization parameters, page-local | $\delta$ is the Dirac delta in the registry |
| $m$ | polynomial degree | |

# Reference list

61 references, merged complete into the [bibliography](/bibliography.md)
from the Crossref deposited list.

# Pages created or updated

Chunk 3 (2026-11-08), list updated in chunk 4 (2026-11-08). This source is cited on:

- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Shifted boundary method](/methods/shifted-boundary-method.md)
