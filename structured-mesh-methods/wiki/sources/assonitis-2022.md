---
type: Source
title: "Assonitis, Paciorri, Ciallella, Ricchiuto & Bonfiglioli (2022) — Extrapolated shock fitting for two-dimensional flows on structured grids"
description: "Structured extrapolated shock fitting: the fitted shock blanks the cells it crosses and exchanges data with the surrounding flow by Taylor extrapolation, decoupling shock and grid topology and recovering second-order convergence."
resource: "doi:10.2514/1.j061893"
source_kind: paper
authors: [Assonitis A., Paciorri R., Ciallella M., Ricchiuto M., Bonfiglioli A.]
year: 2022
venue: "AIAA J. 60(11):6301–6312"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2022_Crossref_AIAA_Journal_Assonitis_Extrapolated_Shock_Fitting_for_Two-Dimensional_Flows_on_Stru.pdf"
tags: [shock-fitting, structured-grid, compressible]
timestamp: 2026-11-08T20:47:00Z
---

# Summary

Assonitis et al. bring extrapolated discontinuity tracking to structured grids ([shock fitting](/methods/shock-fitting.md)): shocks float on an unchanged grid, the cells they cross are blanked, and data are extrapolated across them.

# Version read

HAL deposit hal-03887410 of the published article (AIAA layout); metadata from the version of record, AIAA J. 60, 6301–6312 (2022). Introduction, algorithm and conclusions read; results in outline.

# Key claims

1. Boundary and floating shock fitting tie grid topology to shock topology (introduction). **Stated**
2. Cell blanking plus Taylor extrapolation lets a structured solver run as a black box under shock fitting (algorithm). **Stated**
3. Fitting converges at about second order where capturing falls slightly below first order (results). **Shown**

# Notation map

| Assonitis, Paciorri, Ciallella, Ricchiuto & Bonfiglioli (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| S-F, S-C | shock fitting, shock capturing |  |

# Reference list

47 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 3 (2026-11-08). This source is cited on:

- [Shock fitting on structured grids](/methods/shock-fitting.md)
