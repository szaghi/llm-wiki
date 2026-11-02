---
type: Source
title: "Kopriva et al. (2025) — Energy bounds for discontinuous Galerkin spectral element approximations of well-posed overset grid problems for hyperbolic systems"
description: "Shows that a DG spectral element approximation of the well-posed overset problem for hyperbolic systems is energy bounded only for fixed order, mesh and time: without dissipation the overlap coupling admits positive eigenvalues; upwind fluxes stabilize it in one dimension, and a new penalty applying dissipation at points in the overlap adds more."
resource: "doi:10.1016/j.jcp.2024.113508"
source_kind: paper
authors: [Kopriva D.A., Winters A.R., Nordström J.]
year: 2025
venue: "J. Comput. Phys. 520:113508"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2025_Crossref_Journal_of_Computational_Physics_Kopriva_Energy_bounds_for_discontinuous_Galerkin_spectral_element_ap.pdf"
tags: [dg, stability, energy-method, sbp-sat]
timestamp: 2026-11-02T15:40:00Z
---

# Summary

The discrete sequel to [Kopriva et al. (2022)](/sources/kopriva-2022.md). Even though the discontinuous Galerkin spectral element method (DGSEM) is stable for hyperbolic boundary-value problems and the overset problem is well posed in an appropriate norm, the energy of the DGSEM approximation of the overset problem is bounded by data only for fixed polynomial order, mesh and time. Without dissipation the coupling of overlapping domains admits positive eigenvalues of the semi-discrete system. Upwind numerical fluxes stabilize the coupling in one dimension, and a new penalty applying dissipation at arbitrary points in the overlap, depending only on the difference between the two solutions, adds more; 1-D experiments show spectral convergence with sufficient dissipation ([well-posedness and energy stability](/results/overset-well-posedness.md), [DG on overlapping grids](/methods/discontinuous-galerkin-on-overset-grids.md)).

# Version read

arXiv preprint 2405.04668v2, 33 pages. Read in a targeted way (abstract, introduction, section structure, main results and conclusions closely; derivations and remaining results skimmed): from chunk 4 on, the bundle is compiled in the main session without reader subagents, by the owner's instruction. Claims below are limited to what was read closely.

# Key claims

1. Although the DGSEM is stable for hyperbolic boundary-value problems and the overset problem is well posed in an appropriate norm, the energy of the DGSEM approximation of the overset problem is bounded by data only for fixed polynomial order, mesh and time (Abstract). **Proved**
2. In the absence of dissipation, coupling the overlapping domains is destabilizing: the system integrated in time can have eigenvalues with positive real part (Abstract). **Shown**
3. In one space dimension the coupling is stabilized by the upwind numerical flux (Abstract). **Derived**
4. A new penalty method applies dissipation at arbitrary points within the overlap, depending only on the difference between the solutions (Abstract). **Derived**
5. One-dimensional experiments implement the well-posed penalty formulation and show spectral convergence when sufficient dissipation is applied (Abstract). **Shown**

# Printed slips

None recorded (targeted reading).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| DGSEM | DG spectral element method, polynomial degree $N$ | registry §8 |
| penalty in the overlap | point penalties $\Sigma^m$ | as on the well-posedness page |

# Reference list

15 references, merged complete into the [bibliography](/bibliography.md) with `citedby` kopriva-2025, from the Crossref deposited reference list. [Kopriva et al. (2022)](/sources/kopriva-2022.md) is cited.

# Pages created or updated

Chunk 5 (2026-11-02). This source is cited on:

- [Discontinuous Galerkin methods on overlapping grids](/methods/discontinuous-galerkin-on-overset-grids.md)
- [Well-posedness and energy stability of overset problems](/results/overset-well-posedness.md)
