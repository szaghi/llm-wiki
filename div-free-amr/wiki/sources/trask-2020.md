---
type: Source
title: "Trask, Bochev & Perego (2020) — A conservative, consistent, and scalable meshfree mimetic method"
description: "Meshfree mimetic divergence on point clouds: virtual faces built from GMLS or graph-Laplacian moments satisfy a discrete divergence theorem and local conservation without any mesh."
resource: "doi:10.1016/j.jcp.2019.109187"
source_kind: paper
authors: [Trask N., Bochev P., Perego M.]
year: 2020
venue: "J. Comput. Phys. 409:109187"
local_file: "~/papers/mosaic/div-free-amr/2020-JCP-Trask-101016jjcp2019109187.pdf"
tags: [mimetic, meshfree, conservation, gmls, divergence-constraint]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The outer frontier of the mimetic program: "mimetic methods discretize
divergence by restricting the Gauss theorem to mesh cells. Because point
clouds lack such geometric entities, construction of a compatible meshfree
divergence remains a challenge." The **meshfree mimetic divergence (MMD)**
answers it by *constructing the missing geometry algebraically*: a virtual
primal–dual mesh whose **virtual face moments** contract with GMLS field
moments to give an operator satisfying a **discrete divergence theorem and
local conservation**, first-order accurate. Two instantiations: with a
low-quality background mesh (GMLS face moments), or fully meshfree (face
moments from weighted graph-Laplacian equations) — "trad[ing] an expensive
mesh generation problem for a scalable algebraic one, without sacrificing
compatibility with the divergence operator." Demonstrated as a virtual
finite-volume scheme for conservation laws on point clouds.

# Key claims

1. **Structure without geometry**: the Gauss-theorem structure is imposed
   as an algebraic constraint on virtual faces rather than inherited from
   mesh entities — evidence that the mimetic invariants attach to the
   *operator relations*, not to the mesh, sharpening the
   formulation-over-discretization theme
   ([secondary conservation](/properties/secondary-conservation.md)).
2. **Compatibility survives the meshfree limit** at first order — the
   price of abandoning mesh entities is accuracy order, not conservation
   or the divergence theorem.
3. **Degenerate-mesh remediation**: the background-mesh instantiation
   targets exactly the regime where mesh-based mimetic schemes lose
   robustness — a fallback layer below the polyhedral generality of MFD.

# Notation map

| Trask et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| MMD operator | $D_h$ on virtual faces | discrete Gauss theorem by construction |
| virtual face moments | algebraic surrogates for $V_h^2$ DOFs | GMLS or graph-Laplacian |

# Pages created or updated

* Updated [Support-operator method](/definitions/support-operator-method.md) (meshfree frontier: virtual faces).

# Citations

1. `~/papers/mosaic/div-free-amr/2020-JCP-Trask-101016jjcp2019109187.pdf` (doi:10.1016/j.jcp.2019.109187) — text extraction, 28 pp. **DOI corrected 2026-10-08 (DOI audit).** The DOI recorded earlier, 10.1016/j.jcp.2020.109187, does not resolve on Crossref; the registered DOI, verified by title and authors, is 10.1016/j.jcp.2019.109187. The archive file was renamed on 2026-10-08 to embed the correct DOI.
