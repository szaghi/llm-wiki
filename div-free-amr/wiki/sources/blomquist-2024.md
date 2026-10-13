---
type: Source
title: "Blomquist, West, Binswanger & Theillard (2024) — Stable nodal projection method on octree grids"
description: "Node-collocated incompressible projection on non-graded quad/octrees: not a true projection, but an iteration whose limit is the exact one, contracting on uniform grids via the staggered complex, with stability on adaptive grids set by the divergence's hanging-node ghost rule."
resource: "doi:10.1016/j.jcp.2023.112695"
source_kind: paper
authors: [Blomquist M., West S.R., Binswanger A.L., Theillard M.]
year: 2024
venue: "J. Comput. Phys. 499:112695"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2024-JCP-Blomquist-101016jjcp2023112695.pdf"
tags: [projection, incompressible, octree, amr, collocated, hanging-nodes]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper builds an incompressible Navier–Stokes solver with every
variable stored at the nodes of a non-graded quadtree or octree. It uses:
* sharp level-set boundaries with hybrid finite-volume/finite-difference
  treatment;
* semi-Lagrangian BDF2 with implicit viscosity;
* a nodal projection.

The supra-convergent Min–Gibou gradient and Laplacian are combined with a
deliberately first-order central divergence. Hanging nodes at T-junctions
are filled with ghost values.

The paper's central result is about the projection. It is merged into the
[projection method](/methods/projection-method.md) and the
[AMR projection method](/methods/amr-projection-method.md).

# Key claims

1. **Not a projection, but its limit is** (§3.1). The nodal Laplacian is
   not the nodal divergence of the nodal gradient, so the operator is not
   idempotent and one pass leaves residual divergence. Divergence-free
   fields are fixed by it. The eigenvalue-1 eigenspace is exactly the
   incompressible space, given a Dirichlet condition somewhere. If the
   iterated operator converges, its limit is the canonical projection.
2. **Uniform periodic grids: a contraction** (§3.2). The nodal divergence
   and gradient are the staggered operators composed with linear
   interpolations between nodes and edges, which are transposes of each
   other. The nodal Laplacian equals the staggered one, and averaging has
   norm at most one, so the operator contracts. The spectrum lies in
   $[0, 1]$; with no-slip walls a zero eigenvalue appears for the wall
   modes.
3. **Adaptive grids: a sufficient condition** (§3.3). Ghosted node and
   edge sets give the same staggered factorization. Convergence of the
   iteration follows if a spectral radius built from the interpolations is
   below 1. This needs only that the staggered Laplacian be the divergence
   of the gradient, not that the two operators are negative transposes.
   * The divergence's ghost-value rule is the only free ingredient.
   * Using the gradient's third-order ghost rule for the divergence is
     unstable. Quadratic, linear, ENO and WENO rules are stable.
   * An unstable interpolation can still give a convergent iteration.
   * The condition is not proved for the rule used, and boundaries are
     outside the analysis.
4. **Verification** (§§3.4, 4.2). Iterated projection on a randomly refined
   quadtree (240 splits) is stable and second-order. The iteration
   converges for Neumann, Dirichlet and mixed walls, with or without an
   interface. On an analytic vortex, velocity and potential converge at
   second order. One pass is enough for second order; the default is up to
   5 passes at tolerance $10^{-3}$, and 1 to 3 are typically used. The
   $L^\infty$ velocity error is lower than that of the authors' earlier
   MAC-octree solver.
5. **Applications** (§5). Driven cavity at $Re = 1000$; an oscillating
   cylinder matching experiment at CFL up to 10; flow past a disk and a
   sphere, where an improved departure-point reconstruction reduces the
   high-CFL drag and lift error; and flow at $Re = 1.87\cdot10^7$ past a
   sculpture, at about 560 s per step on 40 cores with about 3.3 million
   nodes.

# Notation map

| Blomquist et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathcal D$, $\mathcal G$ (staggered) | $D_h$, $G_h$ on node–edge data | staggered divergence and gradient |
| $\mathcal D_N$, $\mathcal G_N$, $\mathcal L_N$ (nodal) | node-collocated divergence, gradient, Laplacian | the divergence is first order on adaptive grids |
| $\mathcal P_N = \mathcal I - \mathcal G_N\mathcal L_N^{-1}\mathcal D_N$ | iterated collocated projection | not idempotent |
| $\phi$ (Hodge variable) | projection potential | |
| $\mathcal I^{\tilde N}_N$ (ghost interpolation) | hanging-node ghost rule | decides stability |
| velocity $\mathbf u$ | incompressible analog of $B_h$ | |

# Pages created or updated

* Updated [Projection method](/methods/projection-method.md): the iterated collocated projection and its exact limit, with a compiler reading on the compact-stencil variant.
* Updated [AMR projection method](/methods/amr-projection-method.md): the tree-based collocated variant, where the hanging-node divergence rule decides stability.

# Citations

1. `~/papers/mosaic/div-free-amr/2024-JCP-Blomquist-101016jjcp2023112695.pdf` (doi:10.1016/j.jcp.2023.112695): text extraction, all pages including the reference list (74 entries). The proofs of §§3.2–3.3 were read in outline; operator symbols are transcribed from the extracted text, where some glyphs are lost. Figures were read from their captions only.
