---
type: Source
title: "Giuliani et al. (2022b) — A weighted state redistribution algorithm for embedded boundary grids"
description: "Extends state redistribution to three dimensions, introduces a weighted, less dissipative version that activates smoothly as the cut-cell volume fraction decreases, applies it to advective, diffusive and reactive updates in compressible and incompressible flow, and describes its implementation in AMReX-based exascale codes."
resource: "doi:10.1016/j.jcp.2022.111305"
source_kind: paper
authors: [Giuliani A., Almgren A.S., Bell J.B., Berger M.J., Henry de Frahan M.T., Rangarajan D.]
year: 2022
venue: "J. Comput. Phys. 464:111305"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2022_Crossref_Journal_of_Computational_Physics_Giuliani_A_weighted_state_redistribution_algorithm_for_embedded_bound.pdf"
tags: [state-redistribution, cut-cell, small-cell, amr, reacting-flow, gpu]
timestamp: 2026-11-08T18:12:00Z
---

# Summary

Giuliani, Almgren, Bell, Berger, Henry de Frahan and Rangarajan extend
[state redistribution](/methods/state-redistribution.md) to three dimensions,
replace its sharp volume-fraction threshold by weights that switch on smoothly
and dissipate less, apply it to diffusive and reactive updates and to
incompressible flow, and implement it in AMReX-Hydro and several exascale
codes. Of the two 2022 papers of this first author in the archive, this one
appeared second (the SIAM J. Sci. Comput. paper is giuliani-2022).

# Version read

arXiv:2112.12360v2 (May 2022), the preprint of the published paper; title and
authors match Crossref. §§1–3 read in full, §§4–6 for results and
implementation.

# Key claims

1. The extension of SRD to 3-D is straightforward; design changes handle complex 3-D cut geometries (growing least-squares stencils, first-order fallback) (§2). **Stated**
2. The original SRD switches abruptly at the volume-fraction threshold: a wall shift of $10^{-7}\Delta y$ can trigger an $O(1)$ change; the weighted version activates smoothly (§3, ramp advection tests). **Shown**
3. Weights $\alpha$ (own cell) and $\beta$ (neighbours) define a conservative weighted scheme that generalizes to other weightings, e.g. for monotonicity (§3). **Derived**
4. Normal merging is less diffusive than central merging (10–15 % lower errors); weighted SRD cuts errors by a factor 2–3 on coarse grids for a supersonic vortex in a quarter annulus (§3). **Shown**
5. SRD stabilizes updates with advective, diffusive and reactive terms, for compressible and low-Mach or incompressible flow (§4–§5). **Shown**
6. SRD runs in AMReX-Hydro, IAMR, the Pele codes and MFIX-Exa with domain decomposition and hybrid parallelism, at a negligible share of the total cost (§6). **Stated**

# Notation map

| Giuliani et al. (2022b) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $V_{i,j,k}$, $\hat V$, $N_{i,j,k}$, $W_{i,j,k}$ | cell and neighbourhood volumes, overlap count, containing neighbourhoods | |
| $\alpha_{i,j,k}$, $\beta_{i,j,k}$ | SRD weights, page-local | $\alpha$, $\beta$ have other registry roles |
| volume fraction | $\kappa$ | |

# Reference list

18 references, merged complete into the [bibliography](/bibliography.md)
from the Crossref deposited list.

# Pages created or updated

Chunk 3 (2026-11-08), list updated in chunk 4 (2026-11-08). This source is cited on:

- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [State redistribution](/methods/state-redistribution.md)
