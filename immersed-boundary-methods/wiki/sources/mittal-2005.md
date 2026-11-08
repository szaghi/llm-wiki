---
type: Source
title: "Mittal & Iaccarino (2005) — Immersed boundary methods"
description: "Annual Review of Fluid Mechanics survey that defines immersed boundary methods broadly, formalizes the split into continuous and discrete forcing, compares feedback, penalization, direct-forcing, ghost-cell and cut-cell approaches for rigid bodies, discusses grid-size scaling with Reynolds number and the fresh-cell problem of moving sharp boundaries, and reviews applications."
resource: "doi:10.1146/annurev.fluid.37.061903.175743"
source_kind: paper
authors: [Mittal R., Iaccarino G.]
year: 2005
venue: "Annu. Rev. Fluid Mech. 37:239-261"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2005_Crossref_Annual_Review_of_Fluid_Mechanics_Mittal_IMMERSED_BOUNDARY_METHODS.pdf"
tags: [review, immersed-boundary, classification, ghost-cell, cut-cell, moving-boundary]
timestamp: 2026-11-08T18:08:00Z
---

# Summary

Mittal and Iaccarino use "immersed boundary method" for every method that
simulates viscous flow with immersed boundaries on non-conforming grids,
including the Cartesian grid methods of the inviscid literature
([immersed boundary method](/definitions/immersed-boundary-method.md)). They
formalize the dichotomy between continuous forcing (added to the continuous
equations) and discrete forcing (a modified discrete operator), review
Peskin's method, spring tethers, [feedback forcing](/methods/feedback-forcing.md)
and [penalization](/methods/volume-penalization.md) for rigid bodies,
[direct forcing](/methods/direct-forcing.md), [ghost-cell](/methods/ghost-cell-method.md)
and [cut-cell](/methods/cut-cell-method.md) methods, introduce the
tracking-versus-representation view of [sharp and diffuse interfaces](/definitions/sharp-and-diffuse-interface.md),
and name the [fresh-cell problem](/definitions/fresh-cell-problem.md) of
moving sharp boundaries.

# Version read

Version of record (Annual Reviews download), Annu. Rev. Fluid Mech. 37,
239–261 (2005), 24 pages. Read in full; applications skimmed. The text layer
drops the section headings, so claims are located by topic. Page-1 title
and authors match Crossref.

# Key claims

1. Imposing boundary conditions on the immersed boundary "is the key factor in developing an IB algorithm" and "what distinguishes one IB method from another" (imposition of boundary conditions). **Stated**
2. Continuous forcing $\mathcal L(\mathbf U)=\mathbf f_b$ is discretization independent; discrete forcing $[L']\{\mathbf U\}=\{\mathbf r\}$ is equivalent to $\{\mathbf f'_b\}=\{\mathbf r\}+[L]\{\mathbf U\}-[L']\{\mathbf U\}$ and gives direct control of accuracy, stability and conservation (same). **Derived**
3. A Cartesian grid grows like $(L/\delta)^2$ relative to a body-conformal one: $Re^{1}$ in 2-D and $Re^{1.5}$ in 3-D for laminar boundary layers, partly offset by points inside the body and cheaper solvers (introduction). **Derived**
4. Elastic constitutive laws are not well posed in the rigid limit; spring tethers are stiff for large stiffness and spuriously elastic for small (continuous forcing, rigid boundaries). **Stated**
5. Brinkman penalization is feedback forcing with $\alpha_f=0$ and $\beta_f=-\mu/K$ (same). **Derived**
6. Continuous forcing for rigid bodies smooths the boundary, introduces parameters that affect accuracy and stability, and requires solving inside the body (same). **Stated**
7. Direct forcing (Mohd-Yusof; Verzicco et al.) removes parameters and stability constraints but its forcing still extends into the fluid through the distribution function (discrete forcing). **Stated**
8. Ghost cells are solid cells with at least one fluid neighbour; linear reconstruction suffices when the first grid point is in the viscous sublayer, higher order is needed at marginal resolution (same). **Stated**
9. Strict local and global conservation can only be guaranteed by a finite-volume (cut-cell) approach, which is locally and globally second order, but its 3-D extension is nontrivial (same). **Stated**
10. Discrete forcing gives a sharp boundary, no extra stability constraint and decoupled solid nodes, but moving boundaries are harder and a pressure boundary condition is usually required (same). **Stated**
11. Sharp methods meet "freshly-cleared" cells without time history; merging or interpolation handles them; continuous forcing does not have the problem (moving boundaries). **Stated**
12. Applications: clapping filaments with Peskin's method, a ghost-cell RANS simulation of a pickup truck at $Re=3\times10^5$ (2–30 M cells, 30 % inside the body, grid from CAD in under 20 min), LES of a sphere at $Re=3700$ and $10^4$ (applications). **Stated** (cited)

# Notation map

| Mittal & Iaccarino (2005) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Omega_b$, $\Gamma_b$, $\Omega_f$ | $\Omega_s$, $\Gamma$, $\Omega_f$ | |
| $\mathbf f_b=(\mathbf f_m,f_p)$ | $\mathbf f_b$ (page-local forcing of the full system) | |
| $d$ (distribution function) | $\delta_h$ | |
| $\kappa$ (spring constant) | $k_s$ | registry $\kappa$ is the volume fraction |
| $\alpha$, $\beta$ | $\alpha_f$, $\beta_f$ | |
| $K$ (permeability) | $K$, related to $\eta$ | |
| $\mathbf X_k$, $\mathbf F_k$ | $\mathbf X_\ell$, $\mathbf F_\ell$ | |

# Reference list

The review prints a "Literature Cited" list; all 61 entries of the Crossref
deposit are merged complete into the [bibliography](/bibliography.md).

# Pages created or updated

Chunk 2 (2026-11-08), list updated in chunk 4 (2026-11-08). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Flow past a sphere](/benchmarks/flow-past-sphere.md)
- [Fresh-cell problem](/definitions/fresh-cell-problem.md)
- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md)
- [Classical (Peskin) immersed boundary method](/methods/classical-immersed-boundary-method.md)
- [Cut-cell (embedded-boundary) finite-volume method](/methods/cut-cell-method.md)
- [Direct (discrete-time) forcing](/methods/direct-forcing.md)
- [Feedback forcing](/methods/feedback-forcing.md)
- [Ghost-cell immersed boundary method](/methods/ghost-cell-method.md)
- [Volume penalization (Brinkman penalization)](/methods/volume-penalization.md)
- [Regularized delta function $\delta_h$](/operators/regularized-delta-function.md)
- [Discrete conservation](/properties/discrete-conservation.md)
