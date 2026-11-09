---
type: Source
title: "Gordon & Hall (1973) — Construction of curvilinear co-ordinate systems and applications to mesh generation"
description: "Mesh generation as the construction of univalent maps of the unit square onto the domain by transfinite (blending-function) interpolation: Boolean sums of univariate projectors that match the boundary everywhere, with the Coons patch and isoparametric maps as special cases."
resource: "doi:10.1002/nme.1620070405"
source_kind: paper
authors: [Gordon W.J., Hall C.A.]
year: 1973
venue: "Int. J. Numer. Methods Eng. 7(4):461–477"
local_file: "/home/stefano/papers/mosaic/structured-mesh/1973_Crossref_International_Journal_for_Numerical_Methods_in_Engineering_Gordon_Construction_of_curvilinear_coordinate_systems_and_applicati.pdf"
tags: [transfinite-interpolation, algebraic-generation, grid-generation]
timestamp: 2026-11-08T20:27:00Z
---

# Summary

Gordon and Hall bring blending-function interpolation from computer-aided design to finite element mesh generation: a univalent map of the unit square (cube) onto the domain induces curvilinear coordinates, and [transfinite interpolation](/methods/transfinite-interpolation.md) — Boolean sums of univariate projectors — builds the map from the boundary curves alone. They discuss univalence and show a boundary reparametrization that removes fold-over.

# Version read

Version of record, Int. J. Numer. Methods Eng. 7, 461–477 (1973). Read in full except the shell example (skimmed).

# Key claims

1. A one-to-one map of the unit square onto the region is equivalent to a curvilinear coordinate system on it (mapping section). **Stated**
2. The Boolean sum $\mathcal P_\xi\oplus\mathcal P_\eta$ interpolates the primitive map on the whole boundary; the bilinear case is the Coons patch and isoparametric maps are special cases (transfinite interpolation section). **Derived**
3. Univalence is not guaranteed; poor boundary parametrizations fold the map ('overspill') and reparametrization can restore univalence (univalency section). **Shown**

# Notation map

| Gordon & Hall (1973) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $(s,t)$ | $(\xi,\eta)$ | parameters |
| $\mathcal P_s$, $\mathcal P_t$, $\mathcal P_s\oplus\mathcal P_t$ | $\mathcal P_\xi$, $\mathcal P_\eta$, $\mathcal P_\xi\oplus\mathcal P_\eta$ |  |
| $\phi_i$, $\psi_j$ | $\varphi_m$ | blending functions |

# Reference list

15 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 1 (2026-11-08). This source is cited on:

- [Boundary-fitted coordinate system](/definitions/boundary-fitted-coordinate-system.md)
- [Transfinite interpolation](/methods/transfinite-interpolation.md)
