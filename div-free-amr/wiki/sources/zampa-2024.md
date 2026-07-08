---
type: Source
title: "Zampa (2024) — Structure-preserving finite element and finite volume methods for nonlinear and time-dependent PDEs (PhD thesis, Trento)"
description: "The 2024 frontier: two exactly divergence-free hybrid schemes for visco-resistive MHD on unstructured mixed-element grids, one well-balanced, plus asymptotic-preserving low-Mach and multisymplectic compatible FE."
resource: "PhD thesis, University of Trento (supervisor M. Dumbser), December 2024"
source_kind: thesis
authors: [Zampa E.]
year: 2024
venue: "Doctoral School in Mathematics, University of Trento"
local_file: "~/papers/mosaic/div-free-amr/2024-Thesis-Zampa-Trento-StructurePreserving.pdf"
tags: [structure-preserving, divergence-constraint, hybrid, unstructured, well-balancing, multisymplectic, mhd]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The corpus's most recent synthesis (Trento, Dumbser school; collaborations
with Hiptmair, Abgrall, Stern): structure preservation treated as a
*panorama* — gauge invariance, (multi)symplecticity, involutions/
constraints, asymptotic preservation, maximum principles, well-balancing —
with geometry as the unifying tool. The MHD core (Ch. 4): **two exactly
divergence-free methods for viscous and resistive incompressible MHD**,
one of them also **well-balanced on unstructured mixed-element grids**
(quads+triangles in 2D; tets, hexes, pyramids in 3D) — divergence-free
evolution of face-normal $B$ components, constrained $L^2$ projection,
with [GLM cleaning](/methods/glm-divergence-cleaning.md) as an auxiliary
stage. Also: an asymptotic-preserving weakly compressible method that
**converges to an exactly divergence-free incompressible scheme in the
low-Mach limit** (quadratic in Mach, verified), hybridized so only SPD
systems are solved; and compatible FE for Hamiltonian PDEs via the
Hodge–Dirac operator with local multisymplecticity criteria.

**Coverage of this ingestion (scoped):** front matter, abstract,
introduction/TOC, and the Chapter 4 divergence machinery at claim level;
Chapters 2–3, 5 at abstract level.

# Key claims

1. **Exactness + well-balancing + unstructured mixed elements coexist**
   (2024): the face-based divergence-free evolution with constrained
   projection runs to machine precision on mixed-element grids —
   extending the exact-invariant family well beyond tensor-product meshes;
   verified through field-loop advection, Orszag–Tang, lid-driven MHD
   cavity, and Grad–Shafranov tokamak equilibria.
2. **The involution as one property among many**: the thesis's framing
   treats the divergence constraint alongside symplecticity, AP, and
   well-balancing — "conserving everything" as the design goal, with
   trade-offs made explicit rather than one invariant privileged.
3. **Hybridization as the solver strategy** (cf.
   [Kozdon et al. (2021)](/sources/kozdon-2021.md)): SPD systems only,
   in the FE/FV hybrid setting.
4. **Scope relative to this bundle's question**: semi-implicit hybrid
   FV/FE with facet DOFs on conforming unstructured meshes — high-order
   collocated FD and 2:1 AMR interfaces remain outside even this newest
   synthesis.

# Notation map

| Zampa | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| face-normal $B$ DOFs, constrained $L^2$ projection | $B_h \in V_h^2$ with $D_h^{\mathrm{f}}$-exact update | hybrid FV/FE |
| Hodge–Dirac operator | $d + \delta$ composite | multisymplectic machinery |

# Pages created or updated

* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md) (2024 frontier note).

# Citations

1. `~/papers/mosaic/div-free-amr/2024-Thesis-Zampa-Trento-StructurePreserving.pdf` — scoped read: front matter, abstract, Ch. 1 framing, Ch. 4 divergence machinery at claim level.
