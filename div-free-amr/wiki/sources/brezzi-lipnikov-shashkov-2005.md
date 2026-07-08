---
type: Source
title: "Brezzi, Lipnikov & Shashkov (2005) — Convergence of the mimetic finite difference method for diffusion problems on polyhedral meshes"
description: "First rigorous stability and optimal-convergence proof for mimetic FD on general polyhedral meshes, covering locally refined and nonmatching meshes as degenerate polyhedra."
resource: "doi:10.1137/040613950"
source_kind: paper
authors: [Brezzi F., Lipnikov K., Shashkov M.]
year: 2005
venue: "SIAM J. Numer. Anal. 43(5):1872-1896"
local_file: "~/papers/mosaic/div-free-amr/2005-SINUM-Brezzi-101137040613950.pdf"
tags: [mimetic, convergence, polyhedral, stability, diffusion, mixed-form]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Supplies what the mimetic program had lacked: a **rigorous stability and
convergence theory**. For linear stationary diffusion in mixed first-order
form (flux + scalar), the mimetic finite difference method on unstructured
**polyhedral** meshes is proved stable with *optimal convergence rates for
both the scalar and vector variables*
([Result page](/results/mfd-convergence.md)) — by a novel direct technique
rather than the earlier detour through equivalence with mixed finite
elements. The mimetic design criteria are stated crisply: mimic the Gauss
theorem (local conservation), the gradient–divergence adjoint symmetry
(symmetry/positivity of the discrete operator), and the null spaces of the
operators (stability).

# Key claims

1. **Optimal rates on polyhedra**: under shape assumptions permissive
   enough to "cover the majority of meshes used in applications"
   (tetrahedra, pyramids, hexahedra, degenerate and nonconvex polyhedra),
   the mixed-form MFD converges at the optimal rates for both variables;
   the "lift property" is the key technical tool.
2. **AMR enters as degenerate polyhedra**: locally refined meshes "may be
   considered as … conformal polyhedral mesh[es] with degenerate elements
   (for instance, when the angle between two faces is 180°)," and the same
   for nonmatching meshes — so a polyhedral-capable discretization
   *eliminates the conformity pressure* that forces abundant red–green
   refinement. A 2:1 hanging-node interface is, in this reading, not an
   exception to be patched but an ordinary (degenerate) element.
3. **Design criteria as theorems' hypotheses**: conservation, adjointness,
   and null-space structure — the
   [support-operator](/definitions/support-operator-method.md) commitments
   — are exactly the properties the stability and convergence proofs
   consume.

# Notation map

| Brezzi–Lipnikov–Shashkov | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $F$ (velocity/flux), $p$ (pressure) | face DOFs in $V_h^2$, cell DOFs in $V_h^3$ | mixed form |
| $\mathcal{DIV}$, discrete flux operator | $D_h$ and $-D_h^{*}$ pair | prime + adjoint-derived |
| degenerate polyhedron (180° faces) | hanging-node/2:1 interface cell | their reading of local refinement |

# Pages created or updated

* Created [MFD convergence on polyhedral meshes](/results/mfd-convergence.md).
* Updated [Support-operator method](/definitions/support-operator-method.md) (convergence theory; polyhedral scope).

# Citations

1. `~/papers/mosaic/div-free-amr/2005-SINUM-Brezzi-101137040613950.pdf` (doi:10.1137/040613950) — text extraction, pp. 1872–1896.
