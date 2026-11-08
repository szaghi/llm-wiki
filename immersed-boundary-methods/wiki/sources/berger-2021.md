---
type: Source
title: "Berger & Giuliani (2021) — A state redistribution algorithm for finite volume schemes on cut cell meshes"
description: "Introduces state redistribution, a postprocessing stabilization for explicit finite volumes on cut-cell meshes that merges small cells into possibly overlapping neighbourhoods and recombines overlap-weighted neighbourhood averages and gradients, conservative and linearity preserving, with second-order results for smooth and shocked gas dynamics."
resource: "doi:10.1016/j.jcp.2020.109820"
source_kind: paper
authors: [Berger M., Giuliani A.]
year: 2021
venue: "J. Comput. Phys. 428:109820"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2021_Crossref_Journal_of_Computational_Physics_Berger_A_state_redistribution_algorithm_for_finite_volume_schemes_o.pdf"
tags: [state-redistribution, cut-cell, small-cell, conservation, compressible]
timestamp: 2026-11-08T18:12:00Z
---

# Summary

Berger and Giuliani propose [state redistribution](/methods/state-redistribution.md)
for the [small-cell problem](/definitions/small-cell-problem.md) of cut-cell
finite volumes: an unstable update with the full-cell time step is followed by
a postprocessing that merges small cells into overlapping neighbourhoods,
weighted by overlap counts so that conservation holds, and recombines
neighbourhood reconstructions. Unlike [flux redistribution](/methods/redistribution.md)
it is linearity preserving, hence second order at the cut cells.

# Version read

arXiv:2005.05734v1 (May 2020), the preprint of the published paper; title and
authors match Crossref. §§1–4 read in full, §5 for results and §6.

# Key claims

1. Flux redistribution is simple and used in 3-D but first order at cut cells and not linearity preserving; cell merging lacks robust general 3-D implementations; $h$-box methods are second order but not extended to 3-D (§1). **Stated**
2. Naive cell merging with overlapping neighbourhoods is not conservative (§2, 1-D example). **Shown**
3. Weighting each cell by the inverse of its overlap count makes overlapping merging conservative (§2, §4). **Proved**
4. Neighbourhoods grow until their volume exceeds a threshold (half a full cell); large cells are their own neighbourhoods (§2). **Stated**
5. The second-order version, with limited least-squares gradients on neighbourhoods, preserves linear functions (§4). **Proved**
6. The postprocessed weights stay bounded as the small-cell fraction vanishes, but the scheme is not monotone for very small cells, as flux redistribution is not (§2). **Derived**
7. Applied to MUSCL and a method-of-lines base scheme, SRD keeps second order for smooth problems and captures shocks without oscillations (§5–§6). **Shown**

# Notation map

| Berger & Giuliani (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $\hat Q$ | $\mathbf q$, $\hat{\mathbf q}$ | cell and neighbourhood states |
| $V_i$, $N_i$, $M_i$ | $V_{\mathbf k}=\kappa_{\mathbf k}h^d$, overlap count, neighbourhood | |
| $\alpha$ (small-cell fraction, 1-D) | $\kappa$ | |
| $\eta_{i,j}$ (FRD fraction) | $\kappa$ | |

# Reference list

24 references, merged complete into the [bibliography](/bibliography.md)
from the Crossref deposited list.

# Pages created or updated

Chunk 3 (2026-11-08), list updated in chunk 4 (2026-11-08). This source is cited on:

- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Small-cell problem](/definitions/small-cell-problem.md)
- [Flux redistribution for cut cells](/methods/redistribution.md)
- [State redistribution](/methods/state-redistribution.md)
- [Discrete conservation](/properties/discrete-conservation.md)
