---
type: Source
title: "Noack (2005) — SUGGAR: a general capability for moving body overset grid assembly"
description: "Describes SUGGAR, a stand-alone overset assembler for structured, unstructured and polyhedral grids and for node- or cell-centred solvers, with binary-tree hole cutting, a body hierarchy, cell-centred fringe and donor-weight rules, polyhedral neighbour-walk donor search and moving-body coupling through named pipes."
resource: "doi:10.2514/6.2005-5117"
source_kind: paper
authors: [Noack R.W.]
year: 2005
venue: "17th AIAA Computational Fluid Dynamics Conference, Toronto, AIAA Paper 2005-5117"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2005_Crossref_17th_AIAA_Computational_Fluid_Dynamics_Conference_Noack_SUGGAR_A_General_Capability_for_Moving_Body_Overset_Grid_Ass.pdf"
tags: [domain-connectivity, hole-cutting, donor-search, moving-grid, unstructured]
timestamp: 2026-11-02T11:28:00Z
---

# Summary

Noack describes [SUGGAR](/software/suggar.md) (Structured, Unstructured, and Generalized overset
Grid AssembleR), a stand-alone [domain connectivity](/definitions/domain-connectivity.md) code for
[moving-body](/methods/moving-overset-grid.md) simulations. It assembles
[overset grids](/definitions/overset-grid.md) made of structured, unstructured (prism and
tetrahedral) and general polyhedral grids, for node-centred and cell-centred flow solvers. Earlier
papers covered octree hole cutting and node-centred assembly. This paper adds:

- **[hole cutting](/methods/hole-cutting.md)** with a binary tree, split in one direction at a time
  with a cyclic choice of direction, which needs fewer nodes than an octree where surfaces align
  with the Cartesian axes (Table 1);
- a body [hierarchy](/definitions/grid-hierarchy.md) with the rule "siblings cut each other";
- [fringe](/definitions/fringe-point.md) marking for cell-centred solvers, neighbour-based for
  least-squares reconstruction and node-based for Taylor-series reconstruction, with INNER and
  OUTER fringes of levels 1 and 2;
- a [donor search](/methods/donor-search.md) for general polyhedra by a neighbour walk with "thick"
  approximate face planes;
- cell-centred donor stencils (donor cell plus face neighbours) for
  [inter-grid interpolation](/methods/inter-grid-interpolation.md), with zeroth-order, Laplacian
  (USM3D), unweighted least-squares (HYB3D) and planned Delaunay-dual weights;
- moving-body support: search trees built once in each body frame, absolute hierarchical
  transforms, and synchronization with a motion controller and the flow solver through Unix named
  pipes.

The companion library DiRTlib handles the solver side. The paper also places SUGGAR beside
[PEGASUS](/software/pegasus.md) and [PEGASUS 5](/software/pegasus-5.md). Its hole/fringe/field
labels enter [point classification](/definitions/point-classification.md); it describes no
treatment of [orphan points](/definitions/orphan-point.md). Two demonstrations report timings and memory but
neither flow solutions nor accuracy. The first is a
[wing–pylon–store separation](/benchmarks/store-separation.md) case with prescribed motion on
structured grids (3.64 million points). The second is a C130 cargo air drop mixing 2 unstructured
and 15 structured grids (4.85 million points, 10.7 million cells).

# Version read

The AIAA typeset conference paper (version of record, AIAA Paper 2005-5117), 21 pages: text and
references on pp. 1–14, figures and tables on pp. 15–21. Text extraction is clean; page 8 was
checked visually. Page 1 prints "Ralph W. Noack" (Crossref "Noack, Ralph") and the title with
"a General" (Crossref "A General"); same work. The conference line under the page-1 banner prints
"June 6-9 2006" against the banner's 2005 (see Printed slips). The paper uses section numbers I–IX,
which locate the claims below.

# Key claims

1. Overset grid assembly provides the domain connectivity information: the receptor (fringe)
   points $\mathcal R_k$ with their donor members and weights, and the hole points $\mathcal H_k$.
   (§I) **Stated**
2. Hole cutting must be efficient because a moving-body simulation repeats the assembly at every
   time step. (§II, §VII) **Stated**
3. An approximate Cartesian geometry is adequate for hole cutting, since cutting a hole larger than
   the body is often advisable, for instance to keep coarse background receptors away from a
   resolved boundary layer. Small gaps need finer resolution to cut as few points as possible,
   hence variable resolution. (§II) **Stated**
4. Octrees refine isotropically and so over-refine in some directions (a slat gap is small
   chordwise but large spanwise). The binary tree splits in one direction. (§II) **Stated**
5. Nodes needed to refine to a surface (Table 1): for $x=0.8$, 13 (binary), 253 (quadtree) and
   10921 (octree); for $x+y=1$, 835, 709 and 31753; for $x+y+z=1$, 27265 (binary) and 21793
   (octree). The binary tree saves much memory where surfaces align with the axes and costs a small
   penalty otherwise. (§II, Table 1, Figs. 1–2) **Shown**
6. Bodies form a tree in which siblings cut each other. Container bodies without grids build the
   hierarchy, and a body cuts all grids of its sibling's descendants. (§II, Figs. 3–4) **Stated**
7. Binary-tree refinement: each facet's bounding-box spans are enlarged by $\delta_{\min}=D/1000$,
   $D$ the box diagonal. A node is split in a direction where its span exceeds the enlarged facet
   span, chosen cyclically $x\to y\to z$ starting after the parent's split direction. (§III)
   **Stated**
8. Without the cyclic choice, the first facet would drive excessive refinement in one direction and
   spoil the refinement for other facets. (§III) **Stated**
9. The fringe depth depends on the solver: a least-squares gradient (Cobalt, HYB3D) needs the field
   cell and two fringe layers of cells, while a Taylor-series reconstruction (USM3D) needs node
   values on the first fringe layer, averaged from all cells around each node, so it needs a wider
   fringe. (§IV, Fig. 5) **Stated**
10. The node-based cell-centred fringe marking needs more overlap than the neighbour-based one.
    (§IV) **Stated**
11. Barycentric or parametric coordinates do not exist for general polyhedral cells. The donor
    search is a neighbour walk started from a cell found in a separate octree refined to the size of
    the solid-boundary faces. (§V) **Stated**
12. A cell-centred donor stencil is the donor cell plus its face neighbours, roughly twice the
    extent of a node-centred one (Fig. 8). Its member count drops at boundaries, worst for a
    tetrahedron in a mesh corner with all faces but one on the boundary, and this can hurt accuracy.
    (§VI) **Stated**
13. The weights $\alpha_{\mathbf j}$ are linear and normalized to $\sum_{\mathbf j}\alpha_{\mathbf j}=1$.
    The options are zeroth order (weight 1 on the donor cell), the USM3D Laplacian weights
    (optionally clipped to $[0,2]$ before normalizing, falling back to zeroth order if all vanish)
    and HYB3D unweighted least squares. (§VI) **Stated**
14. Least-squares weights degenerate (reduced dimensionality) when the donor cell and its neighbours
    share a boundary face aligned with a Cartesian direction. (§VI, Fig. 9) **Stated**
15. Least-squares interpolation was found to be non-monotone with respect to the donor values in
    HYB3D and USM3D results. This depends on the solution and must be handled in the solver or in
    DiRTlib. (§VI) **Stated** (no data shown)
16. A planned option tetrahedralizes (Delaunay) the centres of the donor cell and of the cells that
    share a node with it, and uses barycentric weights on the dual tetrahedron that contains the
    receptor. (§VI) **Stated** (future work)
17. The hole-cutting and donor-search trees are built once, in each moving body's untransformed
    frame. Grids are never moved; transforms are absolute in time and hierarchical (child relative
    to parent). (§VII) **Stated**
18. A query point is transformed from its local frame to the global frame and then to the target
    body's frame, so every search runs in the target's coordinates. (§VII) **Stated**
19. SUGGAR runs as a separate process, synchronized with a motion controller and the flow solver
    through blocking Unix FIFOs. All processes must run on one shared-memory machine, and only one
    parallel solver process can talk to a FIFO. (§VII, Fig. 10) **Stated**
20. Wing–pylon–store on a 2.6 GHz Pentium 4 with 3 GB: setup about 6 s grid reading, 261 s binary
    trees and 16 s donor-search octree, 283 s in all; per step about 15 s hole cutting, 39 s donor
    search and 10 s output; peak memory about 1.0 GB. (§VIII, Table 2) **Shown**
21. C130 / parachute / cargo: setup about 256 s reading and orienting the unstructured cells, 14 s
    binary tree and 79 s donor octree (printed total 335 s); per step about 81 s hole cutting, 53 s
    donor search and 71 s ASCII output; peak memory about 1.8 GB. A parallel option exists but was
    not used. (§VIII, Table 3) **Shown**
22. SUGGAR can combine structured and unstructured grids into one unstructured overset grid,
    written as a single general polyhedral grid. (§VIII) **Stated**
23. PEGASUS 5 "has not been applied to moving body problems". (§I) **Stated**

# Printed slips

- **Table 2 totals.** The 25 printed rows sum to 3,108,363 points and 2,899,400 cells, while the
  "Totals" row prints "26 structured, 3639804, 3411400". The differences are exactly
  $531441=81^3$ points and $512000=80^3$ cells, i.e. one $81\times81\times81$ grid missing from
  the rows, which matches the count 26 against 25 rows. The paper does not say which grid it is.
  Table 3's totals equal the sums of its rows *(compiler check, not in the sources)*.
- **C130 setup time (§VIII):** "approximately 256 seconds ... approximately 14 seconds ... and 79
  seconds ... for a total setup time of 335 seconds"; $256+14+79=349$ s. The wing–pylon–store total
  ($6+261+16=283$ s) is consistent *(compiler check, not in the sources)*.
- **Node-based fringe marking (§IV):** step 5 marks a cell INNER FRINGE 2 "if it has a node marked
  as INNER FRINGE 1", but no printed step marks INNER FRINGE 1 (steps 1–4 produce only OUT and OUTER
  FRINGE 1). Step 3 also prints "is it has" for "if it has".
- **Page 1:** the conference line prints "June 6-9 2006"; the banner and the paper number give
  2005.
- §VIII prints "Table 3 provides details on the system of grids." twice in one paragraph.
- **References:** refs. 4 and 13 both print "AIAA Paper 91-1586-CP", although ref. 4 is dated 1995
  (6th International Symposium, Lake Tahoe) and ref. 13 is the 1991 10th AIAA CFD Conference.
  Ref. 9 prints "Paper 97-2040, AIAA, 2000". Ref. 10 prints pages "643–65". Ref. 27 prints "AIAA
  Journal, Vol. 37, No. 12, 2000" while ref. 6 prints "Vol. 38, No. 11, 2000". Ref. 4 prints
  "Internationsl"; ref. 7 and §I print "PEGSUS 4.0" and "Pegsus4".

# Notation map

| Noack (2005) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| FIELD | $\mathcal D_k$ | points or cells the solver updates |
| hole, OUT | $\mathcal H_k$ | no iblank integers given |
| fringe, receptor, intergrid boundary point | $\mathcal R_k$ | synonyms in the paper |
| INNER FRINGE 1/2, OUTER FRINGE 1/2 | $\mathcal R_k$ with fringe level $n_f\in\{1,2\}$, at holes / at overlap boundaries | level 1 nearest the hole or boundary |
| donor cell, donor members | donor cell, $\mathcal S_{\mathbf i}$ | cell-centred: donor plus face neighbours, not a $q^{n_d}$ block |
| weights | $\alpha_{\mathbf j}$ | $\sum\alpha_{\mathbf j}=1$ |
| C, F1, F2 (Fig. 5) | field cell, first and second fringe cells | page-local |
| D, N (Fig. 9) | donor cell and its neighbours | **$D$ is also the facet diagonal in §III**; **$N$ is reserved for the polynomial degree** |
| $\delta x$, $\delta y$, $\delta z$, $D$, $\delta_{\min}=D/1000$ | facet bounding-box spans, diagonal, span enlargement | page-local; **$\delta$ is the Yin–Yang buffer angle in the registry**, used only on Yin–Yang pages |
| $h_x$, $h_y$, $h_z$ | tree-node spans | page-local; not grid spacings $h_k$ |
| $\vec N$, $\vec p$, $\epsilon$, $\vec r_i$ | $\bar{\mathbf n}_f$, $\mathbf p_f$, $\epsilon_f$, $\mathbf x_i$: averaged face normal, reference face point, face thickness, face vertices | page-local symbols of [donor search](/methods/donor-search.md); **$\vec p$ is not the pressure** |
| DCI | domain connectivity information | |
| hole-cutting octree / binary tree, donor-search octree | Cartesian approximations of the cutting surface $\mathcal C$; start-cell tree | |

# Reference list

27 printed references, numbered (AIAA superscript style). All 27 are merged complete into the
[bibliography](/bibliography.md) with `citedby` noack-2005. Ref. 20, the companion DiRTlib paper
(AIAA Paper 2005-5116) by the same author and year, is keyed `noack-2005-b`, because the plain key
is this source. AIAA papers printed only as "Paper NN-NNNN, AIAA, year" are entered as technical
reports. Refs. 4 and 13 print the same paper number (see Printed slips) but are different works by
their venues and dates, and are kept as two entries.

# Pages created or updated

Chunk 1 (2026-11-02), cited further in chunk 2. This source is cited on:

- [Wing–pylon–store separation and related moving-body cases](/benchmarks/store-separation.md)
- [Domain connectivity and overset grid assembly](/definitions/domain-connectivity.md)
- [Fringe (receptor) points and overlap width](/definitions/fringe-point.md)
- [Grid hierarchy and priority](/definitions/grid-hierarchy.md)
- [Orphan points](/definitions/orphan-point.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [Donor search](/methods/donor-search.md)
- [Fluid–structure interaction on overlapping grids](/methods/fluid-structure-interaction-on-overset-grids.md)
- [Hole cutting](/methods/hole-cutting.md)
- [Implicit hole cutting](/methods/implicit-hole-cutting.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Moving overset grids](/methods/moving-overset-grid.md)
- [Overlap optimization](/methods/overlap-optimization.md)
- [Parallel and GPU overset grid assembly](/methods/parallel-overset-grid-assembly.md)
- [DCF and DCF3D (Meakin's domain connectivity function and code)](/software/dcf3d.md)
- [Overture (and its grid generator Ogen)](/software/overture.md)
- [PEGASUS 5](/software/pegasus-5.md)
- [PEGASUS (PEGSUS) versions 1–4](/software/pegasus.md)
- [SUGGAR](/software/suggar.md)
