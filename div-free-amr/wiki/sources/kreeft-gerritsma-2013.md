---
type: Source
title: "Kreeft & Gerritsma (2013) — Mixed mimetic spectral element method for Stokes flow: a pointwise divergence-free solution"
description: "Arbitrary-order mimetic spectral elements on curvilinear quads/hexes: the projection commutes with the exterior derivative, so div/curl/grad are discretized exactly and Stokes solutions are pointwise divergence-free."
resource: "doi:10.1016/j.jcp.2012.10.043"
source_kind: paper
authors: [Kreeft J., Gerritsma M.]
year: 2013
venue: "J. Comput. Phys. 240:284-309"
local_file: "~/papers/mosaic/div-free-amr/2013-JCP-Kreeft-101016jjcp201212028.pdf"
tags: [mimetic, spectral-elements, high-order, divergence-constraint, stokes, curvilinear]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The mixed mimetic spectral element method (MMSEM,
[method page](/methods/mimetic-spectral-elements.md)) applied to Stokes
flow in vorticity–velocity–pressure form: **arbitrary-order** elements on
curvilinear quadrilaterals/hexahedra, built from the mimetic operator
triple — reduction $\mathcal{R}$ (integration onto $k$-cells),
reconstruction $\mathcal{I}$ (mimetic spectral interpolation/histopolation
functions), projection $\pi = \mathcal{I}\circ\mathcal{R}$ — with the
decisive property that **the projection commutes with the exterior
derivative**. Hence grad, curl, div "are discretized exactly," the LBB
condition is satisfied, convergence is optimal for all admissible boundary
conditions, and the velocity is **pointwise divergence-free for all mesh
sizes**.

# Key claims

1. **High order and exactness coexist**: the commuting projection carries
   the constraint to arbitrary polynomial order — the corpus's clearest
   constructive demonstration that "high-order" and "exact algebraic
   invariant" are jointly achievable, in the FE/spectral family on
   conforming curvilinear meshes.
2. **The alternatives fail on exactly this axis**: Galerkin spectral
   elements (velocity/pressure degree offset) are only *weakly*
   divergence-free — the divergence converges to zero but never is zero;
   least-squares spectral elements circumvent LBB but conserve mass
   poorly.
3. **Framework, not basis, does the work**: the authors note compatible
   B-splines or other mimetic bases slot into the same framework — the
   commuting-diagram structure, not the particular interpolant, is the
   active ingredient (cf.
   [FEEC](/definitions/finite-element-exterior-calculus.md),
   [DEC](/definitions/discrete-exterior-calculus.md) as sibling
   frameworks, acknowledged as such).
4. **Scope**: Stokes (elliptic); conforming meshes; no
   AMR/nonconforming-interface claim — the 2:1 question is untouched
   here.

# Notation map

| Kreeft & Gerritsma | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $k$-forms / $k$-cochains | $V_h^k$ | spectral-degree DOFs on $k$-cells |
| $\mathcal{R}, \mathcal{I}, \pi$ | reduction / reconstruction / projection | $\pi d = d \pi$ |
| exterior derivative $d$ | $G_h, C_h, D_h$ by degree | exact under projection |

# Pages created or updated

* Created [Mimetic spectral elements](/methods/mimetic-spectral-elements.md).

# Citations

1. `~/papers/mosaic/div-free-amr/2013-JCP-Kreeft-101016jjcp201212028.pdf` (doi:10.1016/j.jcp.2012.10.043) — text extraction, pp. 284–309. **DOI corrected 2026-10-08 (DOI audit).** The DOI recorded earlier, 10.1016/j.jcp.2012.12.028, resolves on Crossref to a Multi Level Multi Domain particle-in-cell paper by Innocenti et al.; the correct DOI, verified on Crossref by title, authors and pages, is 10.1016/j.jcp.2012.10.043. The archive filename still embeds the old DOI.
