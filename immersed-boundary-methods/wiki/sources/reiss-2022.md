---
type: Source
title: "Reiss (2022) — Pressure-tight and non-stiff volume penalization for compressible flows"
description: "Compressible volume penalization by a reduced volume fraction that scales mass, momentum and energy and keeps the speed of sound, making bodies pressure-tight without stiffness, with slip, no-slip and adiabatic walls, mass and energy conservation and the skew-symmetry of the interior scheme."
resource: "doi:10.1007/s10915-021-01747-x"
source_kind: paper
authors: [Reiss J.]
year: 2022
venue: "J. Sci. Comput. 90(3):86"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2022_Crossref_Journal_of_Scientific_Computing_Reiss_Pressure-Tight_and_Non-stiff_Volume_Penalization_for_Compres.pdf"
tags: [penalization, compressible, conservation, skew-symmetric]
timestamp: 2026-11-08T18:24:00Z
---

# Summary

Reiss replaces the velocity penalty of compressible Brinkman penalization, which becomes stiff when it must contain large pressure differences, by a reduced volume fraction in the body that scales all conserved quantities and leaves the sound speed unchanged ([volume penalization](/methods/volume-penalization.md)). Bodies become pressure-tight without stiffness; mass and energy are conserved ([discrete conservation](/properties/discrete-conservation.md)).

# Version read

arXiv:2103.08144v2 (November 2021), the preprint of the published paper (subtitle "An immersed boundary method with good conservation properties"). §§1–3 read in full, §4 for results. Title and author match Crossref.

# Key claims

1. Brinkman penalization becomes numerically stiff when high pressure gradients must be balanced (Abstract, §1). **Stated**
2. Scaling mass, momentum and energy by a volume fraction with a non-conservative pressure term keeps the sound speed and CFL condition (§2). **Derived**
3. Reducing the volume fraction by six to eight orders of magnitude makes fluxes vanish in the body; a Darcy friction adds no-slip at the explicit time-step limit (§2–§3). **Stated**
4. Mass and energy are conserved in the whole domain, approximately in the fluid; momentum is not, since bodies exchange momentum (§2). **Derived**
5. The skew-symmetry of the energy-conserving interior scheme is kept (§3). **Derived**
6. Acoustic reflections, a cylinder, a supersonic wedge and a confined blast wave are computed with good conservation (§4). **Shown**

# Notation map

| Reiss (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi$ (reduced volume) | $\phi_v$ | $\phi$ is the level set |
| Darcy coefficient | $\eta^{-1}$-type friction |  |

# Reference list

61 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 4 (2026-11-08). This source is cited on:

- [Shock–obstacle interaction](/benchmarks/shock-obstacle-interaction.md)
- [Volume penalization (Brinkman penalization)](/methods/volume-penalization.md)
- [Discrete conservation](/properties/discrete-conservation.md)
