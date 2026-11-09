---
type: Source
title: "Dobrev, Knupp, Kolev, Mittal & Tomov (2022) — hr-Adaptivity for nonconforming high-order meshes with the target matrix optimization paradigm"
description: "hr-adaptivity combining target-matrix node optimization with nonconforming isotropic and anisotropic refinement chosen by TMOP quality estimators, meeting size and aspect-ratio targets with fewer degrees of freedom."
resource: "doi:10.1007/s00366-021-01407-6"
source_kind: paper
authors: [Dobrev V., Knupp P., Kolev T., Mittal K., Tomov V.]
year: 2022
venue: "Eng. Comput. 38(4):3721–3737"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2021_Crossref_Engineering_with_Computers_Dobrev_hr-Adaptivity_for_nonconforming_high-order_meshes_with_the_t.pdf"
tags: [mesh-optimization, target-matrix, hr-adaptivity, amr]
timestamp: 2026-11-08T20:47:00Z
---

# Summary

Dobrev et al. augment [target-matrix optimization](/methods/target-matrix-optimization.md) with nonconforming refinement to overcome the fixed topology of r-adaptivity.

# Version read

arXiv:2010.02166v1 (5 October 2020); metadata from the version of record, Eng. Comput. 38, 3721–3737 (2022; online 2021). Method sections and conclusions read; examples in outline.

# Key claims

1. r-adaptivity is limited by the mesh topology and cannot always meet size and aspect-ratio targets (introduction). **Stated**
2. TMOP-based estimators choose anisotropic refinement for aspect-ratio targets and isotropic refinement for size targets (method). **Stated**
3. hr-adaptivity reaches a given accuracy with significantly fewer degrees of freedom than r- or h-adaptivity (results). **Shown**

# Notation map

| Dobrev, Knupp, Kolev, Mittal & Tomov (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\gamma$ | refinement type | page-local |

# Reference list

39 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 3 (2026-11-08). This source is cited on:

- [Moving mesh partial differential equations](/methods/moving-mesh-pde.md)
- [Target-matrix optimization (TMOP)](/methods/target-matrix-optimization.md)
