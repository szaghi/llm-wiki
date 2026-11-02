---
type: Source
title: "Delcour et al. (2022) — Investigating the influence of compressibility on the second-mode flutter of a cantilevered cylinder in axial flow"
description: "Validates a partitioned fluid–structure interaction framework with a Chimera mesh for a flexible cantilevered cylinder in confined axial flow against water experiments, then shows that air compressibility at inlet Mach numbers 0.66 and 0.72 accelerates second-mode flutter and changes its mode shape."
resource: "doi:10.1016/j.jfluidstructs.2021.103469"
source_kind: paper
authors: [Delcour L., Bral A., Van Langenhove L., Degroote J.]
year: 2022
venue: "J. Fluids Struct. 109:103469"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2022_Crossref_Journal_of_Fluids_and_Structures_Delcour_Investigating_the_influence_of_compressibility_on_the_second.pdf"
tags: [fsi, moving-grid, compressible, overset-grid]
timestamp: 2026-11-02T15:04:00Z
---

# Summary

A partitioned [fluid–structure interaction](/methods/fluid-structure-interaction-on-overset-grids.md) framework (in-house coupling code Tango with IQN-ILS quasi-Newton acceleration, Abaqus beam model, ANSYS Fluent with $k$-$\omega$ SST) simulates a flexible clamped-free cylinder in confined axial flow, motivated by air-jet weaving. Large cylinder motion is handled by a Chimera mesh: a fixed hexahedral background mesh of the channel and a body-fitted component mesh whose outer boundary deforms freely with the cylinder, moved as a fictitious linear-elastic solid ([moving overset grids](/methods/moving-overset-grid.md)). Water experiments (buckling and second-mode flutter) are reproduced; air simulations at constant dimensionless velocity show that compressibility at inlet Mach 0.66 and 0.72 accelerates the instability, changes the mode shape and lengthens the wall contact, with local supersonic pockets and shocks. The overset method is used, not developed: no hole-cutting, donor-search or interpolation detail is given.

# Version read

Anonymised author manuscript (Word-generated PDF, no authors on page 1), 23 pages, all read. The title matches the Crossref record; authors are taken from Crossref.

# Key claims

1. The Chimera technique combines body-fitted boundary-layer resolution with tolerance of large displacements, unlike immersed-boundary methods (poor boundary layers) and single deforming meshes (mesh degradation) (§1, §3.3). **Stated**
2. The component mesh (about 600 000 cells) is moved as a linear-elastic solid with Poisson ratio 0, its outer overset boundary free; the background mesh has 1.24 M cells (1.65 M with wall refinement) (§3.3). **Stated**
3. Water validation: first-mode buckling at 1.5 m/s, second-mode buckling at 3.3 m/s and second-mode flutter at 4.32 m/s are reproduced; simulated flutter frequency about 4.1 Hz against about 3.5 Hz measured (§4.1). **Shown**
4. Air at inlet Mach 0.21: compressibility delays the growth but leaves the final regime unchanged; at 0.66 and 0.72 it accelerates the instability, changes the mode shape and lengthens the line contact with the wall (about 6 cm and 17 cm) (§4.2). **Shown**
5. Local supersonic pockets terminated by shocks appear (maximum Mach 1.2 at 260 m/s) although the inlet is subsonic; motions start planar and become orbital (§4.2). **Shown**
6. Time-step and mesh refinement checks are reported for the 260 m/s compressible case (§4.2). **Shown**

# Printed slips

- The dimensionless velocity at 4.32 m/s is printed 6.3 in Table 2 and 6.43 in §4.1.3; the inlet Mach number at 260 m/s is printed 0.72 in Table 2 and 0.71 in §4.2.4.
- "Streamline factor" (§1) and "shape factor" (§2) name the same quantity; §3.3 prints "user" for "used".
- References: ref. 26 "partioned"; ref. 27 volume 0.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| overset interface | outer boundary of the component grid | moves with the deforming component mesh |
| component, background mesh | $G_k$ of higher, lower priority | |

# Reference list

27 printed references, numbered, no DOIs printed, merged complete into the [bibliography](/bibliography.md) with `citedby` delcour-2022. No printed duplicates.

# Pages created or updated

Chunk 3 (2026-11-02). This source is cited on:

- [Fluid–structure interaction on overlapping grids](/methods/fluid-structure-interaction-on-overset-grids.md)
- [Hole cutting](/methods/hole-cutting.md)
- [Immersed boundaries on overlapping grids](/methods/immersed-boundary-on-overset-grids.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Moving overset grids](/methods/moving-overset-grid.md)
- [Shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md)
