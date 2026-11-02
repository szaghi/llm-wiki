---
type: Source
title: "Benek et al. (1985) — A 3-D chimera grid embedding technique"
description: "Extends the Chimera grid-embedding scheme to three dimensions: a strict embedding hierarchy, hole cutting by a level surface with a radius-plus-normal test, one fringe layer, trilinear inter-grid interpolation, the PEGSUS connectivity code and the XMER3D implicit Euler solver, shown on transonic wing–body, wing–body–tail and three-ellipsoid configurations."
resource: "doi:10.2514/6.1985-1523"
source_kind: paper
authors: [Benek J.A., Buning P.G., Steger J.L.]
year: 1985
venue: "AIAA 7th Computational Physics Conference, Cincinnati, AIAA Paper 85-1523, pp. 322-331"
local_file: "/home/stefano/papers/mosaic/overset-chimera/1985_Crossref_7th_Computational_Physics_Conference_BENEK_A_3-D_chimera_grid_embedding_technique.pdf"
tags: [overset-grid, chimera, hole-cutting, interpolation, domain-connectivity, compressible]
timestamp: 2026-11-02T11:29:00Z
---

# Summary

Benek, Buning and Steger extend the two-dimensional Chimera scheme of 1983
to three dimensions ([overset grid](/definitions/overset-grid.md)). The domain is split into overlapping subdomains, each covered by an
independently generated boundary-conforming grid. Grids communicate only
through their boundaries, whose values are interpolated from the grid that
contains them. PEGSUS writes the result, a
[composite mesh](/definitions/composite-overlapping-grid.md), together with
its interpolation data. The grids form a strict embedding
[hierarchy](/definitions/grid-hierarchy.md): each grid of level $\ell$ lies
inside one grid of level $\ell-1$, and grids of the same level are disjoint.
The hierarchy restricts the [donor search](/methods/donor-search.md) to
parent–child pairs.

Where an embedded grid overlaps its parent, a hole is cut
([hole cutting](/methods/hole-cutting.md)). A level surface $\mathcal C$ of
the embedded grid is the initial hole boundary. Parent points inside it are
found by a bounding-radius test followed by the sign of the outward normal at
the closest point of $\mathcal C$, and are blanked in IBLANK
([point classification](/definitions/point-classification.md)). A single
layer of [fringe points](/definitions/fringe-point.md) is then found:
non-hole points that have a hole point among their nearest neighbours. They
receive values by trilinear interpolation from the embedded grid. The paper
argues for trilinear
[inter-grid interpolation](/methods/inter-grid-interpolation.md) over the
Taylor formula of 1983, and declines Berger's
[conservative interface](/methods/conservative-overset-interface.md) because
its stencils would be irregular in 3-D.

PEGSUS, the [connectivity](/definitions/domain-connectivity.md) code
([PEGSUS and PEGASUS 4](/software/pegasus.md)), produces the composite grid
and the interpolation data. XMER3D solves the Euler equations with a
modified Pulliam–Steger implicit approximate-factorization algorithm. The
modifications are an IBLANK-masked tridiagonal solve, explicit
dissipation weighted by the metrics, and a local time step. All grids are
static ([moving overset grids](/methods/moving-overset-grid.md) come later in
the corpus). The
transonic tests are an AEDC wing–body (3 grids, 65,813 points) at three
Mach numbers, the same body with a horizontal tail (4 grids, 157,540
points), and three ellipsoids (3 grids, 57,750 points). The paper judges the
agreement with wind-tunnel data qualitatively and gives no convergence or
error study.

# Version read

Version of record: a scanned AIAA reprint, AIAA Paper 85-1523, proceedings
pp. 322–331 (10 pages), with the accession stamp "A85-40955". The OCR layer
is letter-spaced and interleaves the columns, so the whole paper was read
visually and the equations were checked at 220 dpi. The page-1 title and
authors match Crossref. The paper prints the code name as **PEGSUS**; later
papers write PEGASUS. No DOI is printed. Locators are proceedings page
numbers.

# Key claims

Registry notation: the source's $G_{\ell,i}$ is $G_k$ with level
$\ell(k)$; its level surface $C$ is $\mathcal C$; IBLANK is the 0/1 mask
$i_b$, translated to $\iota$; its donor-cell coordinates
$(\bar\xi,\bar\eta,\bar\zeta)$ are $\mathbf s$; its $\vec Q$ is
$\hat{\mathbf q}=\mathbf q/J$; its local time step $h$ is written
$\Delta t_{\mathrm{loc}}$ here, since $h$ is a spacing in the registry.

1. Grid-generation approaches for complex geometry fall into three groups: grid patching (disjoint subdomains with common boundaries), grid embedding (a common overlap region instead of common boundaries), and grid adapting (Introduction, p. 322). **Stated**
2. The name *chimera* reflects that each component can have a boundary-conforming grid, selective refinement and, in principle, its own flow model. The present implementation solves the Euler equations on every grid (pp. 322–323). **Stated**
3. Removing the region of a grid that contains an embedded grid (the hole) simplifies communication, which then passes only through grid boundaries (Implementation, p. 323). **Stated**
4. The procedure is split into two codes. PEGSUS takes the grids and the embedding hierarchy and outputs the composite mesh and the interpolation data. XMER3D takes this output and the flow specification and solves the flow (p. 323). **Stated**
5. The grids form a hierarchy: each grid of level $\ell$ lies wholly inside one grid of level $\ell-1$, and grids of level $\ell$ are disjoint. The hierarchy is the graph of communication lines, and its main advantage is that it limits the donor search (p. 323, Fig. 1). **Stated**
6. Only the boundary of each embedded grid is updated by interpolation. Parent points inside a subregion of the embedded grid are excluded, which avoids interpolating every common point and also removes parent points inside solid bodies. The only requirement is enough overlap to interpolate the outer boundary of the embedded grid from its parent (Hole Generation, p. 323, Fig. 2). **Stated**
7. Hole cutting (stated in 2-D): build outward normals on $\mathcal C$; choose an origin $P_o$ inside $\mathcal C$ and set $R_{\max}$ to the largest distance from $P_o$ to $\mathcal C$. A point $P$ with $\lvert\vec r\rvert<R_{\max}$ is tested with $\vec N\cdot\vec R_p$, where $\vec N$ is the unit outward normal at the point $P_c$ of $\mathcal C$ closest to $P$ and $\vec R_p$ is the vector from $P_c$ to $P$. If $\vec N\cdot\vec R_p<0$, $P$ is a hole point and its IBLANK is set from 1 to 0 (p. 324, Fig. 3). **Stated** (no proof of correctness)
8. A point with IBLANK = 1 that has a hole point among its nearest neighbours is a fringe point. Fringe indices are added to the list of points needing interpolated data and, to simplify XMER3D, also to the hole list (IBLANK set to 0) (p. 324, Fig. 4). **Stated**
9. Earlier experience (ref. 11, Benek et al. 1983) showed that concern about interpolation across shocks was warranted when the Taylor series was used (Interpolation, p. 324). **Stated** (cited)
10. Mastin (ref. 19) showed that in 2-D bilinear interpolation beats the Taylor series when higher derivatives are unimportant, and simple experiments on a rectangular mesh containing a discontinuity (ref. 20, private communication) agree (p. 324). **Stated** (cited)
11. Berger's conservative interface (ref. 18), which generalizes Rai's patched-grid method to overlapping 2-D grids, gives irregular stencils, expected to be "even more irregular" in 3-D, so it is not used (p. 324). **Stated**
12. Trilinear interpolation $\phi=a_1+a_2s_1+a_3s_2+a_4s_3+a_5s_1s_2+a_6s_1s_3+a_7s_2s_3+a_8s_1s_2s_3$, with $0<s_m<1$ and $a_1,\dots,a_8$ fixed by the 8 values of the donor cell ($q=2$), is used for its compact stencil. Care is needed to keep the receptor inside the donor cell, and "trouble may be encountered with shock–grid boundary interactions" (p. 324). **Stated**
13. In XMER3D the holes are accommodated in "the standard tri-diagonal algorithm" by partitioning the coefficient matrices as in ref. 11. This amounts to multiplying each point's difference equation by its IBLANK and replacing the diagonal of hole points with the identity (p. 325). **Stated**
14. The explicit dissipation $\epsilon J^{-1}[(\nabla\Delta)^2_\xi+(\nabla\Delta)^2_\eta+(\nabla\Delta)^2_\zeta]J\hat{\mathbf q}$ is replaced by $\epsilon J^{-1}[\psi_\xi(\nabla\Delta)^2_\xi+\psi_\eta(\nabla\Delta)^2_\eta+\psi_\zeta(\nabla\Delta)^2_\zeta]J\hat{\mathbf q}$ with $\psi_\xi=\lvert\xi_x\rvert+\lvert\xi_y\rvert+\lvert\xi_z\rvert$ and likewise for $\eta$, $\zeta$. This approximates the flux-Jacobian eigenvalues without square roots, and a similar second-order term keeps the block-tridiagonal structure (p. 325). **Stated**
15. A local time step $\Delta t_{\mathrm{loc}}=\Delta t_{\lim}/(1+\sqrt J)$ (suggested by Pulliam) is used in the hope that it speeds convergence on embedded grids as it does on single grids; "the extent to which this is true has not been thoroughly investigated" (p. 325). **Stated**
16. The wing–body composite has 3 grids and 65,813 points: outer $47\times21\times20$, fuselage $47\times25\times25$, wing $66\times23\times11$. The fuselage grid's outer boundary overlaps the outer grid's inner boundary by 2.5 radii (Grids, p. 326). **Stated**
17. The wing grid has a 5-point overlap in $\xi$ at the trailing-edge cut "to eliminate the requirement for a periodic solution", and 15 $\eta$ points on the wing (p. 326). **Stated**
18. The wing cuts a hole in the fuselage grid, and the values on the hole surface are interpolated trilinearly from the wing grid (p. 326, Fig. 10). **Shown**
19. At $M_\infty=0.6$, $\alpha=0^\circ$ the computed $C_p$ agrees with the Lockheed CFWT data in an "encouraging" way, "particularly near the wing tip", although the tip is not modelled (p. 326, Fig. 11). **Shown**
20. At $M_\infty=0.75$, $\alpha=4^\circ$ the agreement with AEDC Tunnel 4T and Lockheed CFWT data is again "encouraging" (p. 327, Fig. 12). **Shown**
21. At $M_\infty=0.9$, $\alpha=2^\circ$ the agreement "looks acceptable", and is "surprisingly good" near the tip. The shock is smeared for lack of clustering (p. 328, Figs. 13–14). **Shown**
22. Mach contours on the outer surface of the wing grid, interpolated from the fuselage grid, are smooth: "the interaction between the grids results in a smooth set of contours" (p. 328, Fig. 16). **Shown**
23. The wing–body–tail composite has 4 grids and 157,540 points (outer $74\times25\times20$, fuselage $74\times35\times30$, wing $66\times28\times15$, tail $56\times18\times15$). On large grids "the major effect appears to be an expected increase in computing time" (p. 329). **Stated**
24. At $M_\infty=0.9$, $\alpha=2^\circ$ the wing–body and wing–body–tail solutions differ. The authors attribute this to resolution and to convergence level: 3 orders of residual reduction against 4 (p. 329, Figs. 13, 17). **Shown**/**Stated**
25. For three ellipsoids (57,750 points) at $M_\infty=0.8$, $\alpha=-2^\circ$ the Mach contours between the bodies are symmetric, "which implies that any asymmetries contained in the construction of the composite mesh have not affected the solution" (p. 330, Figs. 18–19). **Shown**
26. Conclusion: the chimera method has been extended to 3-D. Comparison with experiment indicates its general accuracy and shows that XMER3D needs viscous terms (p. 330). **Stated**

# Printed slips

- Fuselage contour (p. 325), printed: $y=\sqrt{(0.427-X)X}$ for $0\le X\le2.42$; $y=0.162-0.286X-0.024X^2$ for $2.42<X<4.11$; $y=1.0$ for $4.11<X$. As printed, the first branch is imaginary for $0.427<X\le2.42$, and the second is negative on its whole interval (at $X=4.11$ it gives $-1.42$, not the cylinder value $1.0$) *(compiler check, not in the sources)*. The scan is clear, so the misprint is in the original, and the true contour cannot be recovered from the paper.
- Fig. 5: the hierarchy boxes read "OUTER GRID FIG. 6", "FUSELAGE GRID FIG. 7", "WING GRID FIG. 8". The captions put these grids in Figs. 7, 8 and 9; Fig. 6 is the configuration sketch.
- Modified dissipation (p. 325), printed "$\dots+\psi_\zeta(\nabla\Delta)^2_\zeta[J\vec Q$": the closing bracket is printed as "[".
- p. 323: "embedded grids occupy a lower level of the hierarchy than the grids which envelop it", but in the next rule "grids on level $\ell$ are completely contained within a single grid on the next lower level $\ell-1$". "Lower" is used in both senses; Fig. 1 settles that embedded grids have larger $\ell$.
- Reference list: ref. 10 is dated "ASME FED-Vol. 5, June 1985", while refs. 4 and 14 date the same volume (*Advances in Grid Generation*) June 1983.

# Notation map

| Benek et al. (1985) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $G_{\ell,i}$ ($G_{1,1}$, $G_{21}$, …) | $G_k$ with level $\ell(k)$ | larger $\ell$ = embedded grid |
| $G_{\ell+1,j}\subset G_{\ell,i}$ | embedded $G_{k'}$ inside parent $G_k$ | set-inclusion signs between grids are used loosely in the text |
| $C$ (level surface) | $\mathcal C$ | |
| $P_o$, $R_{\max}$, $\vec r$, $P$, $P_c$ | page-local | hole-cutting test |
| $\vec N$, $\vec R_p$ | page-local | $\vec N$ unit outward, as in the registry |
| IBLANK (1 computed; 0 hole **and** fringe) | $i_b$, translated to $\iota$ | **convention clash**: fringe points are IBLANK = 0 here, $\iota=-k'$ in the registry; they are known as receptors only from the interpolation list |
| hole point / fringe point / computed point | $\mathcal H_k$ / $\mathcal R_k$ / $\mathcal D_k$ | fringe width $n_f=1$ |
| $\bar\xi,\bar\eta,\bar\zeta$ | $\mathbf s=(s_1,s_2,s_3)$ | local coordinates in the donor cell |
| $\phi$, $a_1,\dots,a_8$ | page-local | trilinear interpolant, width $q=2$ |
| $\xi,\eta,\zeta$; $\xi_x,\dots$ | $\boldsymbol\xi$; $\xi_x,\dots$ | agree |
| $J$ | $J$ | Pulliam–Steger convention: the paper writes $\vec Q=[\dots]/J$ |
| $\vec Q=[\rho,\rho u,\rho v,\rho w,e]/J$ | $\hat{\mathbf q}$ | total energy $e$ is $E$ |
| $\epsilon$, $(\nabla\Delta)^2_\xi$, $\psi_\xi$ | page-local | fourth-difference dissipation and its metric weights |
| $h=\Delta t_{\lim}/(1+\sqrt J)$ | $\Delta t_{\mathrm{loc}}$ | **collision**: registry $h$ is a spacing |
| $\eta=0.4,0.6,0.9$ (figures) | spanwise station fraction | **collision** with the coordinate $\eta$ |
| $M$, $\alpha$, $C_p$ | $M_\infty$, $\alpha$, $C_p$ | |

# Reference list

The paper prints 26 numbered references (superscript style, in order of
first citation). All are merged complete into the
[bibliography](/bibliography.md), with `citedby` including this slug. Ref. 1
(NASA CP-2166, 1980) has no author. Refs. 3 and 4 are edited volumes. Ref. 20
is a private communication. Ref. 10 (Steger, Dougherty and Benek, ASME
FED-Vol. 5) is printed with the year 1985, against 1983 for the same volume
in refs. 4 and 14. It is merged under the 1983 key as the same chapter, a
re-keying the human should confirm. Names are kept as printed
("Parthasavathy", "Sorenson R.I.", "Chausee"). No DOIs are printed.

# Pages created or updated

Chunk 1 (2026-11-02). This source is cited on:

- [Composite overlapping grid](/definitions/composite-overlapping-grid.md)
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
- [Moving overset grids](/methods/moving-overset-grid.md)
- [Overlap optimization](/methods/overlap-optimization.md)
- [Interpolation order and overlap requirements](/results/interpolation-order-requirement.md)
- [PEGASUS (PEGSUS) versions 1–4](/software/pegasus.md)
