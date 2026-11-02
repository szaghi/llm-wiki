---
type: Source
title: "Roget & Sitaraman (2014) — Robust and efficient overset grid assembly for partitioned unstructured meshes"
description: "Fully automated parallel overset grid assembly on solver-partitioned unstructured meshes using only local data: automatic hole cutting from Cartesian wall approximations, resolution-based field/receptor selection, a line-walk donor search made robust by an exact inverse map, an alternating-digital-tree alternative and adaptive load re-balancing, implemented in PUNDIT."
resource: "doi:10.1016/j.jcp.2013.12.021"
source_kind: paper
authors: [Roget B., Sitaraman J.]
year: 2014
venue: "J. Comput. Phys. 260:1-24"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2014_Crossref_Journal_of_Computational_Physics_Roget_Robust_and_efficient_overset_grid_assembly_for_partitioned_u.pdf"
tags: [domain-connectivity, hole-cutting, donor-search, unstructured, parallel]
timestamp: 2026-11-02T11:43:00Z
---

# Summary

Roget and Sitaraman present a fully automated, parallel overset grid assembly
([domain connectivity](/definitions/domain-connectivity.md)) for overlapping unstructured meshes.
The meshes stay partitioned into mesh-blocks exactly as the flow solver distributes them, and only
per-process data are used. Every query point (node or cell centre) becomes a hole, field or receptor
point ([point classification](/definitions/point-classification.md)); receptors receive donor cells
and tri-linear [interpolation](/methods/inter-grid-interpolation.md) weights. The method runs in six
steps: hole profiling, query-point identification, mesh-block profiling, donor search, decision logic
and interpolation.

- **[Hole cutting](/methods/hole-cutting.md)** approximates each body's wall by a Cartesian grid of
  sub-blocks, refined until no sub-block touches both a wall face and an outer-boundary face, with
  interior sub-blocks found by an external scan-line flood fill. A point in a hole sub-block of
  another body that finds no donor in that body's mesh is a hole point. The authors call this
  "exact".
- **Field or receptor** is decided by comparing the cell volume of a point with that of its
  candidate donors, so overlap is minimal: an [implicit hole cutting](/methods/implicit-hole-cutting.md)
  criterion (see also [overlap optimization](/methods/overlap-optimization.md)). Mandatory
  [receptors](/definitions/fringe-point.md) surround holes and outer boundaries. An
  [orphan](/definitions/orphan-point.md) arises only in pathological conflicts over low-quality
  donors.
- **[Donor search](/methods/donor-search.md)** is a line walk. Irregular partition boundaries break
  the classical walk, so each mesh-block gets an auxiliary Cartesian grid with an exact inverse map
  that provides a start point inside both a sub-block and a cell. An alternating digital tree (Bonet
  and Peraire) is kept for verification.
- **[Parallel assembly](/methods/parallel-overset-grid-assembly.md)**: bounding boxes and coarse
  auxiliary grids limit the query points, and an adaptive load re-balance slices overloaded
  mesh-blocks and ships them to underloaded processors.

The implementation is PUNDIT, the connectivity module of Helios. It is set beside
[PEGASUS 5](/software/pegasus-5.md) and [SUGGAR](/software/suggar.md)'s spatial decomposition volumes.
The tests report timings only: the HART-II rotor–fuselage (7 million and 62 million nodes) and a
[wing–pylon–store](/benchmarks/store-separation.md) configuration, the latter static, used only for
scaling. Assembly is needed at every step of [moving-grid](/methods/moving-overset-grid.md)
simulations. The paper gives no flow-solution accuracy.

# Version read

The Elsevier version of record (J. Comput. Phys. 260:1–24, received 29 April 2013, online
13 December 2013), 24 pages, all read; Eqs. (1)–(6) were checked visually. Page 1 matches the
Crossref card.

# Key claims

1. Assembly gives every query point one of three exclusive types, hole ($\mathcal H_k$), field
   ($\mathcal D_k$) or receptor ($\mathcal R_k$), with donor cells and weights $\alpha_{\mathbf j}$
   for receptors, and needs no user input beyond the partitioned meshes, body tags and
   boundary-condition locations. (§1, §2.1) **Stated**
2. Non-Cartesian meshes use only local (per-process) information and no global mesh data; the
   solver's partitioning is used as is, without re-partitioning or replication. (§1, §5) **Stated**
3. The classical line-walk donor search is not robust on partitioned unstructured meshes, because
   the search line can leave and re-enter a partition several times through its irregular boundary.
   (§1, Fig. 1) **Stated** (illustrated)
4. The hole cutting is "exact": the approximate sub-block wall representation combined with the
   donor search tags all, and only, points inside walls, provided no hole sub-block overlaps an
   outer-boundary face. (§3.1) **Derived** (logical argument)
5. The hole auxiliary grid is subdivided until no sub-block overlaps both a wall face and an
   outer-boundary face (bounding-box tests only), with a 1% margin on the enclosing box. (§3.1)
   **Stated**
6. An external scan-line flood fill, seeded from an added outer layer of "out" sub-blocks, avoids
   the seed-selection and disconnected-hole problems of internal flood fills; even a singly connected
   wall can give a multiply connected hole. (§3.1, Fig. 4) **Stated**
7. Ray-tracing hole cutting needs the whole body boundary, while this method needs only the wall
   sub-blocks. (§3.1) **Stated**
8. The number of sub-blocks per mesh-block follows the empirical rule
   $N_{\mathrm{SB}}=0.1\,N_{\mathrm{q}}^{0.4}N_{\mathrm c}^{0.6}$ ($N_{\mathrm q}$ query points,
   $N_{\mathrm c}$ cells), fitted by minimizing profiling and search time on a simple case. (Eq. (3),
   §3.3) **Shown** (fit; data not shown)
9. The exact inverse map is "exact": a sub-block with an empty cell list does not overlap the
   mesh-block, so a query point in it has no donor there. (§3.3) **Derived**
10. A cell overlaps a sub-block iff a cell vertex lies inside the sub-block, a cell edge crosses a
    sub-block face, a cell face crosses a sub-block edge, or the sub-block lies entirely inside the
    cell. (§3.3, Fig. 9) **Stated** (geometric argument)
11. Starting the walk from a cell point keeps the whole search line inside one sub-block, which is
    faster and confines special cases; the approximate inverse maps used before, in the earlier
    PUNDIT included, "can create severe robustness issues at boundaries of partitioned mesh-blocks".
    (§3.3) **Stated**
12. When the walk reaches a boundary face, all boundary faces of the sub-block are tested; for the
    closest new intersection (cell $c$, face $f$), a positive product of the search-line vector with
    the outward normal $\mathbf n_f$ means the query point lies outside the mesh-block, a negative one
    means re-entry, and the walk resumes from $c$. (§3.4, Fig. 10) **Stated**
13. Quadrilateral faces are split into two triangles along the diagonal through the lowest-index
    vertex; near-edge crossings are nudged towards the face centre to avoid infinite loops. (§3.4)
    **Stated**
14. If the weights of the found donor are out of tolerance (for instance in concave cells), all
    neighbour cells are tested; otherwise there is no donor. (§3.4) **Stated**
15. Decision order: hole points first; then mandatory receptors (outer-boundary nodes of near-body
    meshes and neighbours of hole points, to a stencil-dependent depth); then each remaining point is
    a field point if its resolution is finer than all its candidate donors, otherwise a receptor of
    the finest donor. (§3.5, Fig. 12) **Stated**
16. A donor cell whose vertices or centre are receptors has them turned into field points, unless
    they are mandatory receptors, in which case the receptor it serves becomes a field point; in
    pathological cases a mandatory receptor turns into a field point and an orphan $\mathcal O_k$
    results, the symptom of a poorly designed grid system (very thin overlap or mismatched cell sizes).
    (§3.5) **Stated**
17. Interpolation uses tri-linear basis functions on tetrahedra, prisms, pyramids and hexahedra; the
    weights come from Newton–Raphson iteration, which reaches machine precision in 3–4 iterations.
    (§3.6) **Stated**
18. The alternating digital tree searches the 6-D box of Eq. (6) (after Bonet and Peraire); it is
    "inherently less susceptible to robustness issues" than the line walk but costlier. (§4)
    **Stated**
19. HART-II (5 near-body unstructured meshes, $7\times10^6$ nodes, 256 processors): assembly takes
    1.3 s (7% of a time step) with the exact inverse map and 2.6 s (14%) with the tree, with identical
    connectivity (same count of each point type); hole profiling is negligible, and both show strong
    load imbalance. (§6.1, Fig. 19) **Shown**
20. Load re-balancing on HART-II cuts assembly time from 2.1 s to 0.7 s ("68% reduction") and then
    to 0.5 s after one adaptive iteration ("76% reduction"). (§6.2, Fig. 20) **Shown**
21. HART-II speed-up at 256 processors is 160 with re-balancing against 73 without (speed-up
    assuming linear scaling from serial to the smallest run, overhead included). (§6.2, Fig. 21)
    **Shown**
22. Wing–pylon–store (3 unstructured grids, $15\times10^6$ cells, 64–512 processors): total time
    falls by up to 80%; speed-up at 256 processors is 213 against 117, still well below linear. (§6.2,
    Fig. 23) **Shown**
23. Fine HART-II ($62\times10^6$ nodes, 256–8192 processors): the ratio of assembly to solver time
    falls from 12% to 3% at 256 processors and from 136% to 21% at 8192. (§6.2, Fig. 24) **Shown**
24. Identifying the data to transfer is the least scalable re-balance sub-task and tends to dominate;
    computing the re-balance matrices stays negligible up to 8192 processors; a load-balancing scheme
    that avoids the initial query-point imbalance is needed. (§6.2) **Shown** / **Stated**
25. Load re-balancing is implemented only with the tree search, since the exact inverse map would
    need extra data (cell neighbours) to be shipped. (§5, §7) **Stated**
26. The method is general, robust ("no undesirable point is generated"), fully automated and
    modular. (§7) **Stated**

# Printed slips

- **§1 organization paragraph:** "in the first section, the terminology … is defined … In the second
  and third sections, the two proposed methods are described … The fourth section describes the
  adaptive load re-balance algorithm"; the sections are §2–§5, so each ordinal is one short.
- **§3.4:** "If an intersection exits (on face F)", for "exists".
- **§6.2:** "the total time decreases from 2.1 sec to 0.7 sec (68% reduction)"; the printed times give
  $1-0.7/2.1=67\%$, while the "76%" for 0.5 s agrees *(compiler check, not in the sources)*.
- **§5:** $L_0$ denotes both the overloaded processor's estimate $L_m+L_s$ and the assistant's directly
  measured original load (both "load without re-balance").
- **Ref. [11]** prints the authors as "L. David, W.D.H. Brown, D.J. Quinlan": the Overture paper of
  Brown, Henshaw and Quinlan (1999); ref. [14] prints "J. Phys. Conf. Ser. 125 (1) (2013)" with no
  pages.

# Notation map

| Roget & Sitaraman (2014) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| OGA (overset grid assembly), grid connectivity | domain connectivity | |
| hole point (blanked-out) | $\mathcal H_k$ | no mask values printed |
| field point (active, solver point) | $\mathcal D_k$ | |
| receptor point (interpolation, fringe point) | $\mathcal R_k$ | |
| mandatory receptor | receptor forced by stencil depth at outer boundaries and holes | depth not quantified; cf. $n_f$ |
| orphan point | $\mathcal O_k$ | mandatory receptor without donor |
| query point $P$ | candidate receptor $\mathbf x^k_{\mathbf i}$ | node or cell centre |
| (candidate) donor cell | donor cell of $\mathcal S_{\mathbf i}$ | finest resolution wins |
| resolution | cell volume $\lvert V_c\rvert$; nodal: average of adjacent cells | smaller is finer |
| interpolation weights (tri-linear) | $\alpha_{\mathbf j}$, $q=2$ | |
| MB$_i$, $B_i$, $P_i$ | mesh-block (partition), body, processor | page-local; **$P$ is both a query point and a processor in the paper** |
| AG, sub-block, AABB, OBB | auxiliary Cartesian grid and its cells, axis-aligned and oriented bounding boxes | page-local |
| EIM, AIM, cell point | exact and approximate inverse maps, walk start point | page-local |
| ADT | alternating digital tree | |
| $N_{SB}$, $N_p$, $N_c$ | $N_{\mathrm{SB}}$, $N_{\mathrm q}$, $N_{\mathrm c}$ | **$N_p$ renamed: $p$ is the order of accuracy in the registry** |
| $N_x$, $N_y$, $N_z$, $dx$, $dy$, $dz$, $i,j,k$ | sub-block counts, sizes, indices | page-local; **$k$ (also the re-entry cell) is the grid index in the registry** |
| $C_{min}$, $C_{max}$, $(x_l,y_l,z_l)$, $(x_u,y_u,z_u)$ | box corners | page-local |
| $F$, $F_c$, $n$, $k$ (§3.4) | face $f$, re-entry face, neighbour cell, re-entry cell $c$ | |
| $L_A$, $L_{max}$, $L_{min}$, $\Delta L$, $L_m$, $L_s$, $L_i$, $L_0$ | processor loads in seconds | page-local |

# Reference list

20 printed references, numbered [1]–[20], all merged complete into the
[bibliography](/bibliography.md) with `citedby` roget-2014. Ref. [11], printed with garbled authors
(see Printed slips), is the existing entry `brown-1999` (AIAA Paper 99-3130, confirmed on Crossref).
Ref. [18] is Bonet and Peraire's alternating digital tree (`bonet-1991`), ref. [6] the earlier PUNDIT
paper (`sitaraman-2010`), ref. [3] [Rogers et al. (2003)](/sources/rogers-2003.md) and ref. [2]
Steger and Benek (`steger-1987`). Ref. [14] prints no pages. No printed duplicates.

# Pages created or updated

Chunk 2 (2026-11-02). This source is cited on:

- [Wing–pylon–store separation and related moving-body cases](/benchmarks/store-separation.md)
- [Domain connectivity and overset grid assembly](/definitions/domain-connectivity.md)
- [Explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md)
- [Fringe (receptor) points and overlap width](/definitions/fringe-point.md)
- [Orphan points](/definitions/orphan-point.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [Donor search](/methods/donor-search.md)
- [Hole cutting](/methods/hole-cutting.md)
- [Implicit hole cutting](/methods/implicit-hole-cutting.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Moving overset grids](/methods/moving-overset-grid.md)
- [Overlap optimization](/methods/overlap-optimization.md)
- [Parallel and GPU overset grid assembly](/methods/parallel-overset-grid-assembly.md)
- [OVERFLOW (OVERFLOW-D, OVERFLOW 2)](/software/overflow.md)
- [Overture (and its grid generator Ogen)](/software/overture.md)
- [PEGASUS 5](/software/pegasus-5.md)
- [SUGGAR](/software/suggar.md)
