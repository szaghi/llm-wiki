---
type: Source
title: "Dobrev, Knupp, Kolev, Mittal & Tomov (2019) — The target-matrix optimization paradigm for high-order meshes"
description: "Extension of target-matrix optimization to high-order isoparametric meshes: targets at every quadrature point, a variational objective, shape, size and alignment metrics with barrier categories, and a safeguarded Newton solver, implemented in MFEM."
resource: "doi:10.1137/18m1167206"
source_kind: paper
authors: [Dobrev V., Knupp P., Kolev T., Mittal K., Tomov V.]
year: 2019
venue: "SIAM J. Sci. Comput. 41(1):B50–B68"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2019_Crossref_SIAM_Journal_on_Scientific_Computing_Dobrev_The_Target-Matrix_Optimization_Paradigm_for_High-Order_Meshe.pdf"
tags: [mesh-optimization, target-matrix, high-order-mesh]
timestamp: 2026-11-08T20:47:00Z
---

# Summary

Dobrev et al. make [target-matrix optimization](/methods/target-matrix-optimization.md) work for high-order meshes, whose quality varies inside elements, by prescribing target Jacobians at quadrature points and minimizing a variational objective of algebraic quality metrics ([mesh quality metric](/definitions/mesh-quality-metric.md)).

# Version read

arXiv:1807.09807v1 (25 July 2018); metadata from the version of record, SIAM J. Sci. Comput. 41, B50–B68 (2019). §§1–4 and §6 read; §5 examples in outline.

# Key claims

1. Targets defined at every quadrature point control sub-element quality of high-order elements (§3.1). **Stated**
2. Shape, size, alignment and combined metrics follow from the factorization of the Jacobian; barrier metrics keep the mesh valid (§3). **Stated**
3. Under-sampling the element with too few quadrature points can invert elements of a fourth-order mesh (§3, Fig. 3.1). **Shown**
4. Newton's method with a line search rejecting inverting or strongly increasing steps solves the optimization robustly (§3.4). **Stated**

# Notation map

| Dobrev, Knupp, Kolev, Mittal & Tomov (2019) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $A$, $W$, $T$ | $\mathsf A$, $\mathsf W$, $\mathsf T$ |  |
| $\tau=\det T$ | $\det\mathsf T$ | page-local; $\tau$ is the registry relaxation time |
| $\mu_i$ | $\mu$ | quality metric |

# Reference list

35 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 3 (2026-11-08). This source is cited on:

- [Mesh quality metric](/definitions/mesh-quality-metric.md)
- [Target-matrix optimization (TMOP)](/methods/target-matrix-optimization.md)
