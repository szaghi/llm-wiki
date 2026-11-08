---
type: Source
title: "Ménez, Parnaudeau, Beringhier & Goncalves da Silva (2023) — Assessment of volume penalization and immersed boundary methods for compressible flows with various thermal boundary conditions"
description: "Compares a continuous-forcing immersed boundary method with compressible volume penalization for isothermal and adiabatic obstacles, derives an implicit adiabatic penalization using ghost cells, finds both first order, penalization far cheaper, and proposes a porosity model that cuts the cost of shock reflection 36-fold."
resource: "doi:10.1016/j.jcp.2023.112465"
source_kind: paper
authors: [Ménez L., Parnaudeau P., Beringhier M., Goncalves Da Silva E.]
year: 2023
venue: "J. Comput. Phys. 493:112465"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2023_Crossref_Journal_of_Computational_Physics_Ménez_Assessment_of_volume_penalization_and_immersed_boundary_meth.pdf"
tags: [penalization, compressible, heat-transfer, ghost-cell, shock]
timestamp: 2026-11-08T18:24:00Z
---

# Summary

Ménez, Parnaudeau, Beringhier and Goncalves da Silva compare a continuous-forcing immersed boundary method with [volume penalization](/methods/volume-penalization.md) for compressible flows with isothermal and adiabatic bodies. Both are first order in space ([first-order accuracy of regularized-delta forcing](/results/first-order-accuracy-of-regularized-delta-forcing.md)); penalization is much cheaper, and an adiabatic condition borrows [ghost cells](/methods/ghost-cell-method.md).

# Version read

HAL accepted manuscript of the published paper. Methods read in full, results for conclusions. Title and authors match Crossref.

# Key claims

1. In compressible penalization the porosity in the continuity equation governs wave reflection and its decrease raises the spectral radius, restricting the time step (§2). **Derived**
2. An adiabatic penalization with an implicit source uses ghost cells and two image points to impose a zero normal temperature gradient to second order (§3). **Derived**
3. Both methods are first order in space for isothermal and adiabatic bodies (§4; conclusions). **Shown**
4. Continuous forcing fails downstream of a supersonic wedge because of artificial interior flow, and costs much more than penalization (§4; conclusions). **Shown**
5. A new porosity model reproduces shock reflection at the accuracy of $\phi_p=0.01$ with the cost divided by 36 (§4). **Shown**
6. A supersonic isothermal sphere agrees with Nagata et al. and Riahi et al. for drag, recirculation, separation, stand-off and Nusselt number (§4). **Shown**

# Notation map

| Ménez, Parnaudeau, Beringhier & Goncalves da Silva (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi$ (porosity) | $\phi_p$ | $\phi$ is the level set |
| $\eta$ | $\eta$ | agree |
| $\chi$ | $\chi_s$ |  |

# Reference list

64 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 4 (2026-11-08). This source is cited on:

- [Flow past a sphere](/benchmarks/flow-past-sphere.md)
- [Shock–obstacle interaction](/benchmarks/shock-obstacle-interaction.md)
- [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md)
- [Ghost-cell immersed boundary method](/methods/ghost-cell-method.md)
- [Volume penalization (Brinkman penalization)](/methods/volume-penalization.md)
- [First-order accuracy of regularized-delta forcing at interfaces](/results/first-order-accuracy-of-regularized-delta-forcing.md)
