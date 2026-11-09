---
type: Source
title: "Nonomura, Iizuka & Fujii (2010) — Freestream and vortex preservation properties of high-order WENO and WCNS on curvilinear grids"
description: "Comparison of WENO and weighted compact nonlinear schemes on curvilinear grids: finite-difference WENO in generalized coordinates cannot preserve the free stream, while WCNS with conservative metrics differenced like the fluxes preserves it and resolves vortices better."
resource: "doi:10.1016/j.compfluid.2009.08.005"
source_kind: paper
authors: [Nonomura T., Iizuka N., Fujii K.]
year: 2010
venue: "Comput. Fluids 39(2):197–214"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2010_Crossref_Computers_amp_Fluids_Nonomura_Freestream_and_vortex_preservation_properties_of_high-order.pdf"
tags: [free-stream-preservation, weno, wcns, high-order]
timestamp: 2026-11-08T20:38:00Z
---

# Summary

Nonomura, Iizuka and Fujii explain why the Visbal–Gaitonde technique applies to the weighted compact nonlinear scheme but not to WENO in generalized coordinates, and compare free-stream and vortex preservation of four implementations ([conservative metric evaluation](/methods/conservative-metric-evaluation.md)).

# Version read

Version of record, Comput. Fluids 39, 197–214 (2010). Formulations and conclusion read; tests in outline.

# Key claims

1. WENO interpolates fluxes containing metrics, so metrics alter its nonlinear weights, and the metrics cannot be split into upwind parts; WENO in generalized coordinates does not preserve the free stream (formulations). **Derived**
2. WCNS with the Visbal–Gaitonde technique preserves the free stream and the vortex better than WENO on all grids tested (conclusion). **Shown**
3. WENO in Cartesian form preserves the free stream but costs about three times as much (abstract, conclusion). **Shown**

# Notation map

| Nonomura, Iizuka & Fujii (2010) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tilde E$ | $\hat{\mathbf f}^1$ | contravariant flux |

# Reference list

20 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 2 (2026-11-08). This source is cited on:

- [Conservative metric evaluation](/methods/conservative-metric-evaluation.md)
- [Grid-induced truncation error](/results/grid-induced-truncation-error.md)
