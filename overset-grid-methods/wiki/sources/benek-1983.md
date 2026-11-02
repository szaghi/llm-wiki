---
type: Source
title: "Benek et al. (1983) — A flexible grid embedding technique with application to the Euler equations"
description: "Founding paper of the Chimera method: independently generated body-fitted grids overset on one another in a level hierarchy, holes cut by level curves of embedded grids, an IBLANK mask in the implicit solver, linear Taylor interpolation at grid boundaries, the PEGASUS and XMERA codes, and 2-D Euler tests on a cylinder and the SKF 1.1 airfoil."
resource: "doi:10.2514/6.1983-1944"
source_kind: paper
authors: [Benek J.A., Steger J.L., Dougherty F.C.]
year: 1983
venue: "AIAA 6th Computational Fluid Dynamics Conference, Danvers, AIAA Paper 83-1944, pp. 373-382"
local_file: "/home/stefano/papers/mosaic/overset-chimera/1983_Crossref_6th_Computational_Fluid_Dynamics_Conference_Danvers_BENEK_A_flexible_grid_embedding_technique_with_application_to_the.pdf"
tags: [overset-grid, chimera, hole-cutting, interpolation, domain-connectivity, compressible]
timestamp: 2026-11-02T11:29:00Z
---

# Summary

Benek, Steger and Dougherty name and describe the **Chimera** method, the
origin of the [overset grid](/definitions/overset-grid.md) approach. Grid
patching joins subdomain grids along common boundaries
([patched grids](/definitions/patched-grid.md)). Chimera grid embedding
instead lets independently generated, simple body-fitted grids overlap. The
grids communicate by interpolating the flow variables at their boundaries,
and in principle each grid can carry its own flow model. The paper covers
three aspects of embedding: decomposition into subdomains, a
[grid hierarchy](/definitions/grid-hierarchy.md), and intergrid
communication.

The grids are arranged in levels $\ell(k)$. In the restricted tree used here,
each embedded grid lies inside a single grid of the level above, and grids of
the same level are disjoint. An embedded grid that contains a body cuts a
hole in its parent ([hole cutting](/methods/hole-cutting.md)). The hole
boundary $\mathcal C$ is a level curve of the embedded grid. Parent points
inside $\mathcal C$ are found by one of two point-in-curve tests. Their
neighbours outside $\mathcal C$ become hole-boundary points, the
[fringe points](/definitions/fringe-point.md) of later usage, and receive
values interpolated from the embedded grid. The outer boundary of each
embedded grid is interpolated from its parent. Donors are found by a
closest-point search and then a nearest-neighbour walk
([donor search](/methods/donor-search.md)). The
[inter-grid interpolation](/methods/inter-grid-interpolation.md) is a linear
Taylor formula, which is not conservative. A per-grid IBLANK array
([point classification](/definitions/point-classification.md)) multiplies
the rows of the Beam–Warming implicit system, so hole rows become identity
rows. Two codes carry out the method: PEGASUS ([PEGSUS and PEGASUS 4](/software/pegasus.md))
combines the grids and computes the hole and interpolation data, which is
the task later called [domain connectivity](/definitions/domain-connectivity.md),
and XMERA solves the flow through the hierarchy.

The 2-D Euler tests are a [circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
at $M_\infty=0.25$ and $0.5$, the SKF 1.1 airfoil at $M_\infty=0.76$, and
the SKF 1.1 with a maneuver flap, a three-level
[multi-element airfoil](/benchmarks/multi-element-airfoil.md). Where a shock
crosses an overlap boundary the solution shows mismatch. The authors
tentatively blame the non-conservative interpolation, and this is the first
motivation recorded for a
[conservative overset interface](/methods/conservative-overset-interface.md).

# Version read

Version of record: a scan of the AIAA conference proceedings, pp. 373–382,
AIAA Paper 83-1944, with the handwritten accession stamp "A83-39391" on page
1. The PDF is image-only with an OCR layer. All 10 pages were read visually,
including every equation and figure caption. The page-1 title and authors
(J. A. Benek, J. L. Steger, F. C. Dougherty) match Crossref. The paper
prints no DOI. Locators are proceedings page numbers.

# Key claims

Registry notation: the source's grid $G_{\ell,i}$ is a component grid $G_k$
of level $\ell(k)=\ell$; its level curve $C$ is the hole-cutting surface
$\mathcal C$; its IBLANK is the 0/1 mask $i_b$, translated to $\iota$. The
source's "first-order accurate" Taylor formula is linear interpolation
(second order in the registry's sense; see the Notation map).

1. Methods that reduce grid-generation effort fall into three groups: grid patching, grid embedding and grid adapting. Patched grids join along common boundaries; embedded grids overlap, "with various constraints imposed upon the amount of overlap and the coincidence of points among grids" (Introduction, p. 373). **Stated**
2. The "flexible solution concept" divides the domain into regions of simpler geometry, a simpler flow model, or both. Because of this structural diversity it is named a **chimera** method; for example, Navier–Stokes on the element grids of a multi-element airfoil and Euler or potential flow on the background grid (p. 374, Fig. 1). **Stated**
3. The grids form a hierarchy of levels, representable as a graph. The general structure lets a grid link to several grids of the level above. The paper uses a tree: each grid of level $\ell$ lies wholly inside one grid of level $\ell-1$, and grids of the same level are disjoint (p. 374, Figs. 2–3). **Stated**
4. Boundary data of an embedded grid are interpolated from another grid with the "first-order accurate" Taylor series $u^k_{\mathbf i}=u^{k'}_{\mathbf j_0}+(\partial_xu)^{k'}_{\mathbf j_0}\,\Delta x+(\partial_yu)^{k'}_{\mathbf j_0}\,\Delta y$, where $\mathbf j_0$ is the donor point found by the search and $(\Delta x,\Delta y)$ is the receptor's offset from it (Eq. 1, p. 374). The stencil that gives the derivatives is not stated. **Stated**
5. This interpolation does not keep the conservation form, which may harm the solution where differences are taken across shocks (p. 374). **Stated**; claim 17 supports it. **Shown**
6. An embedded grid $G_{k'}$ that contains a body is treated as a hole in its parent $G_k$. This removes the parent points inside the body and those inside a grid embedded in $G_{k'}$, which would violate the hierarchy (Holes, p. 374). **Stated**
7. When the embedded grid is the only one of its level and the parent is an O-mesh wrapped around it, hole cutting reduces to dropping the parent points inside an azimuthal level line (p. 374). **Stated**
8. The hole boundary in $G_k$ is a level curve $\mathcal C$ of the embedded grid. Two searches find the points of $G_k$ inside $\mathcal C$ (p. 375, Figs. 4–6). **Stated**
9. The first search, a radius test, is "not particularly efficient", but such searches take "a miniscule amount of the total computational time" (p. 375). **Stated**
10. The second search, the sign of the outward normal at the closest point of $\mathcal C$ dotted with the vector to the tested point, "shows more promise of generalization to three dimensions" (p. 375). **Stated**
11. Points of $G_k$ that lie outside $\mathcal C$ and are nearest neighbours of hole points form the hole boundary. They are flagged and receive values interpolated from the embedded grid (p. 375, Fig. 7c). **Stated**
12. Donor location: for a boundary point of the embedded grid, the closest point of $G_k$ is found by search, and later points by a "nearest neighbor" procedure (p. 375, Fig. 7b). **Stated**
13. Overlap constraint: every point of the difference approximation used in the interpolation must exist on the donor grid. On heuristic grounds the overlap must also be wide enough that the boundaries forming it have little influence on the solution where interpolation occurs (Overlap, p. 375). **Stated**
14. In the implicit solver, the off-diagonal couplings of hole rows and the couplings of their neighbours to them are zeroed, the hole diagonals are set to the identity and the right side to the specified values. In practice each row is multiplied by IBLANK (0 in a hole, 1 otherwise), with unit diagonal on zeroed rows (Eqs. 2–3, p. 375). **Derived**
15. Cylinder at $M_\infty=0.25$: the two-level chimera solution and a single-grid Euler solution on a $90\times70$ polar grid are "indistinguishable", and both agree with a Prandtl–Glauert-corrected potential solution (p. 376, Fig. 9). **Shown**
16. Cylinder at $M_\infty=0.5$: the vortex phenomenon described by Salas appears, with asymmetric shedding, and the vortices "appear to experience no difficulty crossing between grids" (p. 376, Fig. 10). **Shown**
17. SKF 1.1 at $M_\infty=0.76$, $\alpha=2.5^\circ$: single-grid and two-grid Euler solutions disagree in the expansion before the shock, and the Mach contours show "hash" where the shock meets the grid boundary. This "indicates that the nonconservative interpolations are likely to be at fault", though the matter is "still under study" (pp. 376–377, Figs. 13–14). **Shown** (attribution **Stated**)
18. Both SKF 1.1 solutions ran at Courant number 10, defined by the smallest cell volume, so the chimera time steps differed between grids by a factor of 50 (p. 376). **Stated**
19. The chimera solution converged 3 times faster than the single-grid solution (p. 376). **Stated** (no convergence history shown)
20. The full-potential solution places the shock farthest aft and the Euler solution forward of it; viscous effects would move it toward the data (p. 377, Fig. 13). **Shown**
21. Maneuver flap, three levels, $M_\infty=0.6$ and $0.7$: agreement with experiment is better at $0.6$; the suction peaks are overpredicted, and at $0.7$ the shock is too far aft (p. 377, Figs. 17–18). **Shown**
22. Mach contours pass smoothly through grid boundaries, except at $M_\infty=0.7$ where the shock at the grid boundary causes trouble; "improved interpolation procedures are being examined" (p. 377, Figs. 19–20). **Shown**
23. The flow algorithm is "hidden" from the PEGASUS/XMERA management functions, so almost any solver can be substituted with little code change (Computer Codes, p. 376). **Stated**
24. Explicit boundary conditions (Steger; Pulliam and Steger) give a convenient way to impose the right boundary conditions on the various grids with minimal code changes (p. 374). **Stated**
25. The single SKF 1.1 O-mesh has 105 azimuthal and 70 radial points; its trailing-edge cut overlaps "two points on each side", which "reduces the effective number of azimuthal points to 100", consistent with five shared points (the cut line and two on each side) and with the "5 point overlap at the cut" of the chimera meshes $G_{11}$ ($105\times28$) and $G_{21}$ ($105\times46$) *(compiler check, not in the sources)* (p. 376, Figs. 11–12). **Stated**

# Printed slips

- Fig. 13 legend: "XMERA { G11 105 x 28 O-Mesh, G12 105 x 46 O-Mesh }". The text (p. 376) and Figs. 12, 15, 17 and 18 call the airfoil mesh $G_{21}$ (level 2); under the paper's own indexing, $G_{12}$ would be a second level-1 grid.
- Ref. 20 is printed with an incomplete paper number, "AIAA Paper 81-10XX".
- Fig. 2 caption: "Hierarchical structure at embedded grids", as printed ("at" for "of").
- Fig. 5 prints the radius-test formula followed by "$< r$". That is the *outside* condition of the text ("if $r\le r_c$, the point is taken to be within C"), drawn for a point beyond $\mathcal C$. This is not an error, but the figure's inequality is easily misread as the inside test.

# Notation map

| Benek et al. (1983) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $G_{\ell,i}$ ($G_{11}$, $G_{21}$, …) | $G_k$ with level $\ell(k)=\ell$ | two-index name replaced by one grid index; Fig. 1 uses $G_1,\dots,G_4$ |
| $\ell$ (level, 1 = background) | $\ell(k)$ | embedded grids have larger $\ell$ |
| $G_{\ell+1,j}$ in $G_{\ell,i}$ | embedded grid $G_{k'}$ in parent $G_k$ | in the hole-boundary interpolation $G_{k'}$ is the donor |
| $Q_B$, $Q_0$ | $u^k_{\mathbf i}$ (receptor value), $u^{k'}_{\mathbf j_0}$ (donor value) | Eq. 1; $\mathbf j_0$ registered in [notation](/notation.md) §9 |
| $Q_x$, $Q_y$ | $\partial_xu$, $\partial_yu$ at the donor point | stencil not stated |
| $\Delta x$, $\Delta y$ ("interpolation coefficients") | $(\Delta x,\Delta y)=\mathbf x^k_{\mathbf i}-\mathbf x^{k'}_{\mathbf j_0}$, receptor offset from the donor point | stored in place of the weights $\alpha_{\mathbf j}$ |
| "first-order accurate" (Eq. 1) | linear interpolation, error $O(h^2)$: second order | **order naming differs**: the registry names the error exponent; the formula is exact for linear fields *(compiler check, not in the sources)* |
| $C$ (level curve) | $\mathcal C$ | hole-cutting surface |
| $O$, $r$, $r_{\max}$, $r_c$, $\vec r^{\,\pm}$, $\theta^\pm$ | page-local (radius test) | Fig. 5 |
| $P$, $P_c$, $\vec R_p$, $\vec N$ | page-local (normal test) | $\vec N$ outward, as in the registry |
| $d=\vec N\cdot\vec R_p$ | page-local | **collision**: registry $d$ is the overlap distance |
| IBLANK (0 hole, 1 otherwise) | $i_b$, translated to $\iota$: 0 on $\mathcal H_k$ | hole-boundary and outer-boundary receptors keep IBLANK = 1 and are held in lists; $\iota$ marks them $-k'$ |
| hole points / hole-boundary points / field points | $\mathcal H_k$ / $\mathcal R_k$ / $\mathcal D_k$ | outer-boundary points of embedded grids are also in $\mathcal R_k$ |
| $A$, $\phi$, $F$, $a_{ij}$, $f_3,f_4,f_5$ | page-local (implicit system) | Eqs. 2–3 |
| $M_\infty$, $\alpha$, $C_p$ | $M_\infty$, $\alpha$, $C_p$ | agree |
| $\beta$ (flap deflection) | page-local | |

# Reference list

The paper prints 23 numbered references (superscript style). The list is
merged complete into the [bibliography](/bibliography.md), with `citedby`
including this slug. Ref. 2 is an edited proceedings volume (Thompson, ed.)
and Refs. 3, 9, 10 and 11 are chapters of it. Ref. 13 (Steger, Dougherty and
Benek, "A Chimera Grid Scheme", ASME 1983) is the companion paper that gives
the details of the nearest-neighbour search and the two hole searches.
Ref. 20 has an incomplete AIAA paper number ("81-10XX"). No DOIs are
printed. There are no printed duplicates.

# Pages created or updated

Chunk 1 (2026-11-02). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Multi-element airfoils](/benchmarks/multi-element-airfoil.md)
- [Domain connectivity and overset grid assembly](/definitions/domain-connectivity.md)
- [Explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md)
- [Fringe (receptor) points and overlap width](/definitions/fringe-point.md)
- [Grid hierarchy and priority](/definitions/grid-hierarchy.md)
- [Orphan points](/definitions/orphan-point.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Patched (zonal) grids](/definitions/patched-grid.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [Conservative overset interface](/methods/conservative-overset-interface.md)
- [Donor search](/methods/donor-search.md)
- [Hole cutting](/methods/hole-cutting.md)
- [Implicit hole cutting](/methods/implicit-hole-cutting.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Overlap optimization](/methods/overlap-optimization.md)
- [Interpolation order and overlap requirements](/results/interpolation-order-requirement.md)
- [PEGASUS (PEGSUS) versions 1–4](/software/pegasus.md)
