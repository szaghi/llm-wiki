---
type: Source
title: "Devlin et al. (2023) — Direct Flux via Virtual Faces (DFVF-overset): interpolation-free, conservative overset grids"
description: "A conservative overset scheme that generalizes the finite-volume method to overlapping cells: cell volumes are shared through a normalized top-hat weight function, fluxes pass between overlapping cells through virtual faces of defined area, and no interpolation or assembly is needed; implemented for OpenFOAM and tested on diffusion, cavity and volume-of-fluid cases."
resource: "doi:10.1016/j.compfluid.2023.106072"
source_kind: paper
authors: [Devlin J., Chandar D., Quinlan N.J.]
year: 2023
venue: "Comput. Fluids 267:106072"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2023_Crossref_Computers_amp_Fluids_Devlin_Direct_Flux_via_Virtual_Faces_DFVF-overset_Interpolation-fre.pdf"
tags: [conservation, finite-volume, multiphase, interpolation, software]
timestamp: 2026-11-02T15:24:00Z
---

# Summary

DFVF-overset carries over to overset grids a general finite-volume form first derived for a meshless method that supports overlapping cells. Cell volume is distributed by a characteristic top-hat weight function normalized to a partition of unity, so overlapping cells share volume and intercell areas emerge; fluxes pass between overlapping cells through virtual faces of rigorously defined area. The scheme is conservative by construction and needs no interpolation, no overset grid assembly and no external overset library ([interpolation-free overset coupling](/methods/interpolation-free-overset-coupling.md), [conservative overset interface](/methods/conservative-overset-interface.md)). Implemented as an [OpenFOAM](/software/openfoam.md) preprocessor (foam-extend 4.1), it is tested on 1-D diffusion, the [lid-driven cavity](/benchmarks/lid-driven-cavity.md) and volume-of-fluid cases ([multiphase flow](/methods/multiphase-flow-on-overset-grids.md)).

# Version read

Version of record (Elsevier), 15 pages. Read in a targeted way (abstract, introduction, section structure, main results and conclusions closely; derivations and remaining results skimmed): from chunk 4 on, the bundle is compiled in the main session without reader subagents, by the owner's instruction. Claims below are limited to what was read closely.

# Key claims

1. Fluxes between overlapping cells pass through virtual faces with rigorously defined area; exact conservation is retained and no interpolation between the component grids is required (Abstract, §2). **Stated**
2. The scheme lets existing finite-volume solvers run on overset grids monolithically, without interpolation, overset grid assembly or external overset libraries (Conclusions). **Stated**
3. 1-D diffusion: second-order convergence to the analytical solution (Abstract, §4). **Shown**
4. Lid-driven cavity: results close to single-grid solutions with similar convergence to a benchmark; on a coarse grid a tertiary vortex is resolved that interpolation-based overset solutions miss (Abstract, §4). **Shown**
5. Static and dynamic volume-of-fluid cases: conventional overset schemes lose liquid mass, DFVF-overset conserves it strictly and agrees with single-grid solutions; the pressure field is smooth where interpolated overset shows a discontinuity between grids (Abstract, §4, Conclusions). **Shown**

# Printed slips

None recorded (targeted reading).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| virtual face | intercell area between overlapping cells | |
| top-hat weight function | volume-sharing weight, normalized to a partition of unity | page-local |

# Reference list

56 references, merged complete into the [bibliography](/bibliography.md) with `citedby` devlin-2023, from the Crossref deposited reference list; three entries with no year printed take the citing year. Ref. [6] prints the Helios paper (AIAA 2010-1230) with the authors reordered and is merged into `sankaran-2010`. [Chandar & Sitaraman (2022)](/sources/chandar-2022.md) is cited.

# Pages created or updated

Chunk 4 (2026-11-02). This source is cited on:

- [Lid-driven cavity](/benchmarks/lid-driven-cavity.md)
- [Conservative overset interface](/methods/conservative-overset-interface.md)
- [Interpolation-free overset coupling](/methods/interpolation-free-overset-coupling.md)
- [Multiphase flow on overlapping grids](/methods/multiphase-flow-on-overset-grids.md)
- [OpenFOAM (overset)](/software/openfoam.md)
