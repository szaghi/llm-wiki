---
type: Source
title: "Thomas & Lombard (1979) — Geometric conservation law and its application to flow computations on moving grids"
description: "Formulates the geometric conservation law for the volume element under time-dependent mappings and solves it with the flow scheme's own difference operators, so the Jacobian is consistent with the scheme and uniform flow is preserved on moving grids."
resource: "doi:10.2514/3.61273"
source_kind: paper
authors: [Thomas P.D., Lombard C.K.]
year: 1979
venue: "AIAA J. 17(10):1030–1037"
local_file: "/home/stefano/papers/mosaic/structured-mesh/1979_Crossref_AIAA_Journal_Thomas_Geometric_Conservation_Law_and_Its_Application_to_Flow_Compu.pdf"
tags: [gcl, moving-mesh, free-stream-preservation, finite-difference]
timestamp: 2026-11-08T20:27:00Z
---

# Summary

Thomas and Lombard introduce the [geometric conservation law](/properties/geometric-conservation-law.md): the volume element of a moving boundary-conforming grid obeys a conservation law that finite-volume cells satisfy by construction but that finite-difference schemes must solve, with the same operators, to keep the Jacobian consistent. They also show that conservatively written metric terms make central differences [preserve the free stream](/properties/free-stream-preservation.md).

# Version read

Version of record (scan with text layer), AIAA J. 17, 1030–1037 (1979). Method sections read in full; results in outline.

# Key claims

1. Finite-volume schemes satisfy an integral geometric conservation law implicitly; finite-difference schemes must solve its differential form for the Jacobian (introduction). **Derived**
2. Using the same difference scheme for the GCL and the flow equations gives a self-consistent volume element, equivalent to finite volumes at interior points (modified finite-volume method). **Derived**
3. Uniform flow is preserved on a moving grid only if the discrete GCL holds; conservative metric forms make the spatial metric-identity terms vanish with central differences (uniform-flow analysis). **Derived**
4. Implicit unsteady Navier–Stokes and explicit steady supersonic computations on moving grids (applications). **Shown**

# Notation map

| Thomas & Lombard (1979) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $J$ | $J$ |  |
| $\xi_t$, $\eta_t$, $\zeta_t$ | $\xi^i_t$ | time metric terms |
| $W_s$ | $\dot{\mathbf x}$ | boundary or grid velocity |
| $\tau$ | $t$ at fixed $\boldsymbol\xi$ |  |

# Reference list

20 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 1 (2026-11-08). This source is cited on:

- [Free-stream preservation](/properties/free-stream-preservation.md)
- [Geometric conservation law](/properties/geometric-conservation-law.md)
