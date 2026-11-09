---
type: Source
title: "Winslow (1966) — Numerical solution of the quasilinear Poisson equation in a nonuniform triangle mesh"
description: "Finite-volume (Ritz-equivalent) solution of the quasilinear Poisson equation on a topologically regular triangle mesh by over-relaxation, with an appendix that builds the mesh by solving inverted Laplace equations — the origin of elliptic grid generation."
resource: "doi:10.1016/0021-9991(66)90001-5"
source_kind: paper
authors: [Winslow A.M.]
year: 1966
venue: "J. Comput. Phys. 1(2):149–172"
local_file: "/home/stefano/papers/mosaic/structured-mesh/1966_Crossref_Journal_of_Computational_Physics_Winslow_Numerical_solution_of_the_quasilinear_poisson_equation_in_a.pdf"
tags: [elliptic-generation, finite-volume, triangle-mesh]
timestamp: 2026-11-08T20:27:00Z
---

# Summary

Winslow solves the quasilinear Poisson equation of nonlinear magnetostatics on a topologically regular, nonuniform triangle mesh, with coupling coefficients obtained equally from Gauss's theorem on 12-sided secondary cells and from a Ritz minimization with linear functions. His appendix constructs the mesh by treating mesh lines as equipotentials of Laplace equations in the physical plane, inverted into a quasilinear elliptic system for the coordinates — the start of [elliptic grid generation](/methods/elliptic-grid-generation.md).

# Version read

Version of record (scan with text layer), J. Comput. Phys. 1, 149–172 (1966). Main sections and the Appendix read in full; magnetostatic results skimmed.

# Key claims

1. The same difference equations follow from Gauss's theorem on secondary cells and from a Ritz minimization with piecewise-linear functions (derivations). **Derived**
2. Mesh lines as equipotentials of $\nabla^2\xi=\nabla^2\eta=0$ give a smooth mesh; inverted, $g_{22}\mathbf x_{\xi\xi}-2g_{12}\mathbf x_{\xi\eta}+g_{11}\mathbf x_{\eta\eta}=0$ is solved by over-relaxation (Appendix). **Derived**
3. Laplace equations in the computational variables (neighbour averaging) crowd lines or push them outside near concave boundaries; the inverted form does not (Appendix). **Stated**

# Notation map

| Winslow (1966) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\alpha,\beta,\gamma$ | $g_{22}$, $g_{12}$, $g_{11}$ |  |
| $(x,y)$ of the mesh lines | $(\xi,\eta)$ | curvilinear coordinates |
| $\lambda$, $S$ | page-local | coefficient and source of the solved equation |

# Reference list

25 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 1 (2026-11-08). This source is cited on:

- [Elliptic grid generation](/methods/elliptic-grid-generation.md)
