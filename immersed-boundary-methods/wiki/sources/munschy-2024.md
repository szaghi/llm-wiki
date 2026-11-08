---
type: Source
title: "Munschy, Bourne, Dif-Pradalier, Donnel, Ghendrih, Grandgirard & Sarazin (2024) — Kinetic plasma-wall interaction using immersed boundary conditions"
description: "Kinetic 1D-1V plasma–wall (sheath) computations with the wall imposed by penalization as an immersed boundary condition, recovering kinetic sheath physics and larger heat transmission factors than usually predicted."
resource: "doi:10.1088/1741-4326/ad346c"
source_kind: paper
authors: [Munschy Y., Bourne E., Dif-Pradalier G., Donnel P., Ghendrih P., Grandgirard V., Sarazin Y.]
year: 2024
venue: "Nucl. Fusion 64(5):056027"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2024_Crossref_Nuclear_Fusion_Munschy_Kinetic_plasma-wall_interaction_using_immersed_boundary_cond.pdf"
tags: [volume-penalization, plasma, kinetic, sheath]
timestamp: 2026-11-08T18:35:00Z
---

# Summary

Munschy et al. carry [volume penalization](/methods/volume-penalization.md) from fluid plasma models to a kinetic Vlasov–Poisson setting: a mask marks the wall, where particle sinks and thermalization act, in a semi-Lagrangian solver close to a gyrokinetic code. Two variants, with and without current inside the material, both recover the kinetic sheath; non-Maxwellian distributions set the potential drop, and the heat transmission factors exceed the usual predictions.

# Version read

Version of record (open access), Nucl. Fusion 64, 056027 (2024). Abstract, §§1–2 and conclusions read; sheath results skimmed.

# Key claims

1. Gyrokinetic edge codes cannot resolve the Debye sheath, motivating immersed (penalized) wall conditions (§1). **Stated**
2. Penalized walls with or without current in the material both recover the essential kinetic sheath physics (§2, conclusions). **Shown**
3. Ion and electron heat transmission factors are 60 % and 35 % larger than usually predicted (abstract, conclusions). **Shown**

# Notation map

| Munschy, Bourne, Dif-Pradalier, Donnel, Ghendrih, Grandgirard & Sarazin (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| mask function | $\chi_s$ |  |

# Reference list

49 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 5 (2026-11-08). This source is cited on:

- [Volume penalization (Brinkman penalization)](/methods/volume-penalization.md)
