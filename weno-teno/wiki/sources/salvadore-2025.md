---
type: Source
title: "Salvadore et al. (2025) — STREAmS-2.1: Supersonic turbulent accelerated Navier-Stokes solver version 2.1"
description: "Two-page new-version announcement of the STREAmS compressible-wall-turbulence DNS code: version 2.1 merges the curvilinear solver FLEW (2D-extruded generalized curvilinear grids), adds OpenMP, HIP and OpenMP-offload back-ends to CUDA Fortran and MPI, and integrates Catalyst2 in situ visualization."
resource: "doi:10.1016/j.cpc.2025.109652"
source_kind: paper
authors: [Salvadore F., Soldati G., Ceci A., Rossi G., Memmolo A., Della Posta G., Modesti D., Sathyanarayana S., Bernardini M., Pirozzoli S.]
year: 2025
venue: "Comput. Phys. Commun. 314:109652"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_Computer_Physics_Communications_Salvadore_STREAmS-21_Supersonic_turbulent_accelerated_Navier-Stokes_so.pdf"
tags: [software, gpu, finite-difference, turbulence]
timestamp: 2026-10-23T14:54:00Z
---

# Summary

Salvadore et al. (2025) announce version 2.1 of [STREAmS](/software/streams.md), a
GPU-accelerated high-order finite-difference solver of the compressible
Navier–Stokes equations for direct numerical simulation of supersonic wall
turbulence. The release supersedes STREAmS-2.0 (Bernardini et al. 2023) and makes
three changes.

First, STREAmS-2 is merged with the curvilinear solver FLEW (Soldati, Ceci &
Pirozzoli 2024). This gives generalized curvilinear coordinates along two axes,
whose surface coordinates need not be orthogonal, with the third axis normal to the
surface ("2D-extruded curvilinear coordinates"). Three curvilinear cases are stated
to be supported and validated: a circular-arc channel, a curved boundary layer
such as a compression ramp, and an airfoil on a C-mesh.

Second, OpenMP for CPUs, HIP for AMD GPUs and OpenMP offload (tested on Intel GPUs)
are added to the original CUDA Fortran and pure-MPI back-ends.

Third, an in situ visualization layer based on Catalyst2 extracts predefined flow
quantities, such as the swirling strength, without heavy I/O on large grids.

The solution method is described in one line: high-order finite differences "with
hybrid low-dissipative/shock-capturing capabilities" and a third-order low-storage
Runge–Kutta scheme, for a thermally perfect gas. The supported canonical
configurations are planar or circular [channel flow](/benchmarks/turbulent-channel-flow.md),
the [boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md),
shock-wave/boundary-layer interaction and airfoil flow. The paper prints no
equations, results, benchmarks or performance numbers; every claim points to the
cited works.

# Version read

The archive file is the version of record (Elsevier, open access CC BY), a two-page
CPC "New Version Announcement" with a program summary, received 9 April 2025 and
available online 5 May 2025; both pages read. Page 1 matches the Crossref record
for the title, the ten authors in order, the venue and the DOI. The program summary
gives the CPC Library link doi:10.17632/hdcgjpzr3y.3, the repository
github.com/STREAmS-CFD/STREAmS-2, the GPLv3 licence and the languages "Fortran,
CUDA, HIP".

# Key claims

The source prints no mathematics; no page-local notation is needed.

1. STREAmS-2.1 updates STREAmS-2.0 (Comput. Phys. Commun. 285 (2023) 108644) and supersedes it (Abstract; program summary). **Stated**
2. STREAmS-2.1 merges the features of the curvilinear solver FLEW (Abstract; Summary of revisions, item 1). **Stated**
3. The curvilinear capability is a generalized curvilinear coordinate system along two axes, with surface coordinates "non necessarily orthogonal" and the third axis normal to the surface; the Nature of problem calls it "Cartesian or 2D-extruded curvilinear coordinates" (Summary of revisions, item 1). **Stated**
4. Three canonical curvilinear cases are "supported and validated using the present version": the circular-arc channel (cf. Moser & Moin 1987), the curved boundary layer, e.g. a compression ramp (cf. Wu & Martin 2007), and an airfoil on a C-mesh topology (cf. Quadrio et al. 2022) (Summary of revisions, item 1). No validation results are shown. **Stated**
5. The new back-ends, "which have been thoroughly benchmarked", are available alongside the original CUDA Fortran and pure-MPI paradigms (Summary of revisions, item 2). No benchmark data are printed. **Stated**
6. The OpenMP back-end targets CPUs, the HIP back-end AMD GPUs (Sathyanarayana et al. 2025), and the OpenMP-offload back-end, tested on Intel GPUs (Salvadore et al. 2024), is "potentially suitable for different kinds of accelerators" (Abstract; Summary of revisions, item 2). **Stated**
7. In situ visualization is a layer connected to Catalyst2, with predefined procedures to extract flow quantities (e.g. the swirling strength of turbulent structures) and a dedicated input-file section; it lets users extract visualizations from huge data sets without excessive I/O (Abstract; Summary of revisions, item 3). **Stated**
8. The code solves the compressible Navier–Stokes equations for a thermally perfect gas in Cartesian or 2D-extruded curvilinear coordinates (Nature of problem). **Stated**
9. The solver targets DNS of compressible supersonic turbulent boundary layers; the canonical configurations include planar or circular channel flow, the boundary layer, shock-wave/boundary-layer interaction and airfoil flow (Nature of problem). **Stated**
10. The equations are discretized by high-order finite differences with hybrid low-dissipative/shock-capturing capabilities (Solution method); the central scheme, the shock-capturing scheme and the sensor are not named. **Stated**
11. Time advancement uses a third-order, low-storage Runge–Kutta scheme (Solution method); the scheme is not named. **Stated**
12. Languages Fortran, CUDA and HIP; GPLv3 licence; developer repository github.com/STREAmS-CFD/STREAmS-2 (program summary). **Stated**

# Printed slips

- "non necessarily orthogonal" (Summary of revisions, item 1) for "not necessarily orthogonal".
- The repository link is broken across a line as "https://github.com/STREAmS-CFD/STREAmS-" / "2".
- Ref. [1] prints "a highfidelity accelerated solver"; ref. [4] prints the first page only; ref. [6] prints no page or article number beyond "942 (May 2022)".

# Notation map

The source prints no mathematical symbols, so there is nothing to translate. Its
"high-order" refers to the finite differences, formally and without a stated
order, and "third-order" to the low-storage Runge–Kutta scheme.

| Salvadore et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| (none) | — | no equations in the source |

# Reference list

The paper prints 9 references, numbered [1]–[9]. The list is merged complete into
the [bibliography](/bibliography.md), with `citedby` including `salvadore-2025`.
Ref. [3] is the ingested source Bernardini et al. (2023), STREAmS-2.0. Ref. [7]
prints "S. Sathyanarayana, et al."; ref. [2] (FLEW) is printed in online-first form
with a date and DOI but no volume or pages; ref. [1] prints no DOI. No item is
unparseable.

# Pages created or updated

Chunk 9 (2026-10-23), cited further in chunks 10–11 (2026-10-23/24). This source is cited on:

* [STREAmS](/software/streams.md)
