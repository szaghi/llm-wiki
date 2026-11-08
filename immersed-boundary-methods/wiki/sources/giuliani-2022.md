---
type: Source
title: "Giuliani (2022) — A two-dimensional stabilized discontinuous Galerkin method on curvilinear embedded boundary grids"
description: "State redistribution for high-order discontinuous Galerkin methods on 2-D curvilinear cut-cell grids: neighbourhood projections in an overlap-weighted inner product give a conservative, p-exact stabilization at the background time step, with order p+1 in L1 and robustness for shocks."
resource: "doi:10.1137/21m1396277"
source_kind: paper
authors: [Giuliani A.]
year: 2022
venue: "SIAM J. Sci. Comput. 44(1):A389-A415"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2022_Crossref_SIAM_Journal_on_Scientific_Computing_Giuliani_A_Two-Dimensional_Stabilized_Discontinuous_Galerkin_Method_o.pdf"
tags: [state-redistribution, discontinuous-galerkin, cut-cell, small-cell, high-order]
timestamp: 2026-11-08T18:24:00Z
---

# Summary

Giuliani extends [state redistribution](/methods/state-redistribution.md) to discontinuous Galerkin methods on curvilinear embedded-boundary grids: after each explicit stage the solution is projected onto polynomials on merging neighbourhoods and back, which removes the [small-cell problem](/definitions/small-cell-problem.md) while keeping conservation and polynomial exactness. Of the two 2022 papers by this author in the archive, this one appeared first.

# Version read

arXiv:2102.01857v2 (December 2021), the preprint of the published paper. §§1–5 read, §6 for results. Title and author match Crossref.

# Key claims

1. Explicit DG on cut cells needs a time step proportional to the smallest cell; SRD restores a step proportional to background cells, $\Delta t=h/(a(2p+1))$ (§1, §3). **Stated**
2. Neighbourhood bases orthonormal in an overlap-weighted $L^2$ product make the postprocessing conservative and exact for degree-$p$ polynomials (§3–§4). **Derived**
3. Smooth problems converge at $p+1$ in $L^1$ and between $p$ and $p+1$ in $L^\infty$, with volume fractions down to $10^{-9}$ (§6). **Shown**
4. Curved cut cells matter: DG with linear geometry is not second order at the boundary; with curved geometry it is about ten times more accurate than a rotated-grid $h$-box method (§6). **Shown**
5. A Mach 10 double Mach reflection is computed robustly (§6). **Shown**

# Notation map

| Giuliani (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $K_i$, $\hat K_i$, $N_i$ | cell, merging neighbourhood, overlap count | as in the registry |
| $p$ | polynomial degree |  |

# Reference list

51 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 4 (2026-11-08). This source is cited on:

- [Shock–obstacle interaction](/benchmarks/shock-obstacle-interaction.md)
- [Small-cell problem](/definitions/small-cell-problem.md)
- [State redistribution](/methods/state-redistribution.md)
