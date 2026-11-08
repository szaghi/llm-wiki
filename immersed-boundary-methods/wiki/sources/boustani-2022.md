---
type: Source
title: "Boustani, Barad, Kiris & Brehm (2022) — An immersed interface methodology for simulating supersonic spacecraft parachutes with fluid–structure interaction"
description: "Higher-order immersed interface method on adaptive Cartesian grids, extended to membranes thinner than a cell and to fabric porosity imposed as a Darcy–Forchheimer jump condition, loosely coupled to a shell solver with contact, applied to supersonic disk-gap-band parachute inflation."
resource: "doi:10.1016/j.jfluidstructs.2022.103742"
source_kind: paper
authors: [Boustani J., Barad M.F., Kiris C.C., Brehm C.]
year: 2022
venue: "J. Fluids Struct. 114:103742"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2022_Crossref_Journal_of_Fluids_and_Structures_Boustani_An_immersed_interface_methodology_for_simulating_supersonic.pdf"
tags: [immersed-interface, fluid-structure-interaction, compressible, thin-structure, porosity]
timestamp: 2026-11-08T18:24:00Z
---

# Summary

Boustani, Barad, Kiris and Brehm extend NASA's LAVA [immersed interface method](/methods/immersed-interface-method.md) to thin, deforming, porous parachute fabric: in–out tests by ray casting, irregular points per grid direction and weighted least-squares stencils built on the correct side of the sheet handle membranes thinner than a grid cell, and porosity enters as a Darcy–Forchheimer jump condition. A loosely coupled shell solver with contact completes the [fluid–structure coupling](/methods/fluid-structure-coupling.md).

# Version read

Version of record, J. Fluids Struct. 114, 103742 (2022). §§1–4 read, §5 for results. Title and authors match Crossref.

# Key claims

1. Supersonic parachute failures in the LDSD tests motivate simulating inflation at flight conditions (§1). **Stated**
2. Thin geometries are detected by ray–triangle intersection; stencils are restricted to the same side of the sheet by graph walking, handling self-contact (§3). **Stated**
3. Fabric porosity is a Darcy–Forchheimer jump condition across the interface, with permeability and inertial coefficients fitted to broadcloth data (§3). **Derived**
4. Loose coupling with a shell solver (MITC elements, penalty contact) advances at the flow CFL step; contact scales to 640 cores (§4). **Stated**
5. Opening loads and inflation times of sub-scale disk-gap-band parachutes agree with wind-tunnel data and an empirical load model across Mach numbers (§5). **Shown**

# Notation map

| Boustani, Barad, Kiris & Brehm (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $K_p$, $\beta$ | Darcy permeability, Forchheimer coefficient | page-local |
| GLIP | grid-line intersection point |  |

# Reference list

71 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 4 (2026-11-08). This source is cited on:

- [Fluid–structure coupling in immersed boundary methods](/methods/fluid-structure-coupling.md)
- [Immersed interface method](/methods/immersed-interface-method.md)
