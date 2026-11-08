---
type: Source
title: "Okafor, Seshadri, Roy & Udaykumar (2026) — High-order Eulerian sharp interface numerical techniques for micro- to macro-scale simulation of shocked energetic materials"
description: "Fifth-order WENO-Z with narrow-band level sets and an HLLC Riemann-based ghost fluid method for shocked elastoplastic and reactive multi-material flows, from pore collapse to shock-to-detonation transition."
resource: "doi:10.1007/s00193-026-01270-8"
source_kind: paper
authors: [Okafor C., Seshadri P.K., Roy S., Udaykumar H.S.]
year: 2026
venue: "Shock Waves 36(2):18"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2026_Crossref_Shock_Waves_Okafor_High-order_Eulerian_sharp_interface_numerical_techniques_for.pdf"
tags: [ghost-fluid, level-set, high-order, shock, multimaterial]
timestamp: 2026-11-08T18:44:00Z
---

# Summary

Okafor et al. combine fifth-order WENO-Z, narrow-band level sets and a Riemann-based [ghost fluid method](/methods/ghost-fluid-method.md) (reflection across the interface, least-squares interpolation, HLLC along the normal) for shocked energetic materials, and review the GFM variants. They show that the high-order scheme costs little more per grid point and changes meso-scale sensitivity predictions.

# Version read

Version of record (open access), Shock Waves 36, 18 (2026). §1 (with the GFM review), §3 and §5 read; §4 by structure.

# Key claims

1. The original ghost fluid method gives at most first-order interfacial treatment; Riemann-based variants are more accurate and robust but costlier (§1.2). **Stated**
2. Ghost states come from an HLLC Riemann problem along the normal between the reflected-point state (least squares) and the interfacial state (§3.3). **Stated**
3. Fifth-order WENO adds negligible cost per grid point, and coarser meshes then lower the total cost (§5). **Shown**
4. Higher accuracy changes the meso-scale energy localization rates used as macro-scale closures (§4.3, §5). **Shown**

# Notation map

| Okafor, Seshadri, Roy & Udaykumar (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\varphi$ | $\phi$ | level set |
| $X_P=X_{IG}+2|\varphi_{IG}|\,n$ | reflected point | page-local |

# Reference list

135 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 6 (2026-11-08). This source is cited on:

- [Ghost fluid method](/methods/ghost-fluid-method.md)
