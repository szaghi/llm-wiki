---
type: Source
title: "Rogers et al. (2003) — PEGASUS 5: an automated preprocessor for overset-grid computational fluid dynamics"
description: "Describes PEGASUS 5, a rewrite of the PEGASUS connectivity code that automates overset assembly with boundary-condition-driven input, Cartesian hole-map hole cutting, exhaustive tree-and-stencil-jumping donor search, a cell-difference donor criterion, overlap optimization, surface projection and MPI parallelism, cutting the Boeing 777 connectivity work from 32 to 3 days."
resource: "doi:10.2514/2.2070"
source_kind: paper
authors: [Rogers S.E., Suhs N.E., Dietz W.E.]
year: 2003
venue: "AIAA J. 41:1037-1045"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2003_Crossref_AIAA_Journal_Rogers_PEGASUS_5_An_Automated_Preprocessor_for_Overset-Grid_Computa.pdf"
tags: [domain-connectivity, hole-cutting, donor-search, software]
timestamp: 2026-11-02T11:26:00Z
---

# Summary

The paper describes [PEGASUS 5](/software/pegasus-5.md), a from-scratch Fortran 90 rewrite of the
[PEGASUS](/software/pegasus.md) [domain connectivity](/definitions/domain-connectivity.md)
preprocessor for structured [overset grids](/definitions/overset-grid.md). It produces the hole
points, the receptor (hole-fringe and outer-boundary) points, their donor cells and the
interpolation coefficients for flow solvers such as OVERFLOW. The motivation is automation: a
153-mesh, 33-million-point high-lift case had needed over 17,000 lines of PEGASUS 4 input and
weeks of expert work.

The components are:

- the flow-solver boundary conditions as input, which fix the hole-cutting surfaces and the outer
  boundaries;
- automatic [hole cutting](/methods/hole-cutting.md) by a Cartesian hole map, painted inward from
  its corners, with a line-of-sight test for points in elements that the surface crosses;
- an exhaustive [donor search](/methods/donor-search.md) over all $n_g(n_g-1)$ ordered grid pairs
  and all points, with bounding boxes, an alternating digital tree and stencil jumping;
- donor selection by a new cell-difference parameter (CDP), replacing the user's priority lists;
- automatic [overlap optimization](/methods/overlap-optimization.md), which keeps the finest points
  and interpolates the coarser ones;
- projection of overlapping viscous surface grids, a restart that redoes only what changed, and
  master–worker MPI parallelism.

The [point classification](/definitions/point-classification.md), the fringe level $n_f$ of
[fringe points](/definitions/fringe-point.md) and [orphan points](/definitions/orphan-point.md)
are defined on the way, and the history of PEGASUS 1–4 is summarized. Two demonstrations follow:
the 30P30N three-element airfoil (a [multi-element airfoil](/benchmarks/multi-element-airfoil.md)
case; 7 zones, 65 s on one processor) and a Boeing 777-200 in landing configuration (79 meshes,
22.4 million points). OVERFLOW solutions on PEGASUS 4 and PEGASUS 5 connectivity agree with each
other and with experiment. For the 777, labor fell from 32 days to 3, orphans from about 5600 to
about 1200, and the speedup reached 33 on 48 processors. There is no accuracy analysis of the
interpolation or of the CDP.

# Version read

The AIAA Journal version of record (Vol. 41, No. 6, June 2003, pp. 1037–1045), 9 pages, with the
AIAA download stamp of 2015. The text layer is clean except for the CDP equation (p. 1040), which
was read visually. Page 1 matches the Crossref record (title, authors and order). The paper was
presented as AIAA Paper 2002-3186 (32nd Fluid Dynamics Conference, June 2002). That conference
version, with first author Suhs, is a separate record (`suhs-2002` in the bibliography) and is not
this journal paper. Locators are the paper's section headings and page numbers.

# Key claims

1. PEGASUS 5 is new code written from scratch in Fortran 90 (dynamic memory, pointers), whereas
   earlier versions borrowed heavily from their predecessors. (Introduction) **Stated**
2. A PEGASUS 4 high-lift case with 153 meshes and 33 million points needed over 17,000 lines of
   input and many weeks of expert work. (Motivation) **Stated**
3. Connectivity has three operations: hole cutting, identification of the receptors $\mathcal R_k$
   (hole-fringe and outer-boundary points), and identification of donor cells. A receptor without a
   suitable donor is an orphan, $\mathcal O_k$. Orphans should be eliminated; a few in a noncritical
   region have negligible effect, and some flow solvers update them by averaging. (Automation of
   the Oversetting Process) **Stated**
4. A hole-fringe point is any point with a hole point as neighbour. Outer-boundary points are the
   minimum/maximum index surfaces that have no flow-solver boundary condition. (same; Outer-Boundary
   Specification) **Stated**
5. The Cartesian hole map with a line-of-sight test does not use surface normals and so tolerates
   surface discontinuities, but it needs an air-tight solid boundary. The surface-normal hole
   cutting of earlier versions needed many special cases. (Hole Cutting; Figs. 2–3) **Stated**
6. There are $n_g(n_g-1)$ ordered donor/receptor grid pairs, so the work grows as $n_g^2$.
   PEGASUS 5 searches every candidate donor cell of every grid for every point. (Boundary Point
   Interpolation) **Stated**
7. Stencil jumping inverts trilinear interpolation ($q=2$ per direction) by Newton iteration,
   typically in 3–5 inversions and 2–3 jumps when the starting cell is close and the grid smooth.
   A jump is limited to 5 cells per direction, and jumps across C-grid cuts and periodic O-grid
   boundaries are handled. (same) **Stated**
8. Stencil jumping and its variants are "the most commonly used approaches for finding donor
   cells", also called "gradient search" and "stencil walking"; walking moves one cell at a time,
   jumping several. (same) **Stated**
9. Accuracy degrades when donor and receptor cells differ much in size. Among several candidate
   donors, the CDP picks the one closest in size and orientation. (Cell Difference Parameter)
   **Stated**
10. The overlap optimization is "unique" compared with other automatic attempts (refs. 17, 20),
    needs no user interaction, and keeps the finest points while the coarser ones are interpolated.
    In the 1-D example the uniformly coarser mesh keeps no field points in the overlap. (Overlap
    Optimization; Figs. 4–5) **Shown** (schematic)
11. Curved surfaces discretized linearly make two viscous-interpolation failures: orphans near the
    wall on concave surfaces, and on convex surfaces donors far from the wall, which give large
    near-wall velocities. Projecting the receptor surface grid onto the donor surface, for the
    interpolation only, corrects both. (Projection for Viscous Grids; Figs. 6–7) **Stated**
12. The restart repeats only the operations that depend on modified input, and finds them
    automatically. (Restarting) **Stated**
13. A 52-mesh case with 2429 operations runs just under 13 times faster on 15 processors
    (14 workers) than on one. The speedup asymptotes at about 14 beyond 16 processors; the final
    gather and write of the stencils is serial. (Parallelization; Fig. 8) **Shown**
14. The parallel version always reproduces the serial result. (Conclusions) **Stated**
15. 30P30N airfoil: PEGASUS 5 runs in 65 s on one SGI R10K 250 MHz processor. The only input
    changes are a global OFFSET of 2 and an OFFSET of 5 for both box grids. (Multi-Element Airfoil)
    **Shown**
16. 30P30N at $M_\infty=0.2$, $Re=9\times10^6$, $\alpha=8.1^\circ$: the $C_p$ distributions on the
    PEGASUS 4 and PEGASUS 5 grid systems are indistinguishable, and both suction peaks exceed the
    experiment. (Fig. 10) **Shown**
17. The Cartesian hole map usually lacks the resolution for a very thin trailing edge, so the hole
    in the wing grid comes too close to the slat trailing edge. OFFSET fixes it, and overlap
    optimization enlarges the effective hole. (Fig. 9) **Shown**
18. Boeing 777-200: 79 meshes, 22.4 million points. The first run takes 40 min on 16 SGI Origin
    processors (just over 9 CPU hours, $85\,\%$ efficiency). (Boeing 777 section) **Shown**
19. The 777 needed eight automatic hole cutters, an OFFSET of 1 or 2 on nearly half the meshes, a
    $50\,\%$ larger maximum projection distance and manual unblanking in two regions. (same)
    **Shown**
20. The final 777 grid system has just under 1200 orphans, against just under 5600 with
    PEGASUS 4. The labor was 3 days against 32. (same) **Shown**
21. On 48 SGI Origin processors the speedup is 33 and the 777 grids are processed in under 13 min.
    (same; Conclusions) **Shown**
22. 777 at $M_\infty=0.2$, $Re=5.8\times10^6$ (mean aerodynamic chord): the PEGASUS 5 lift curve
    matches the PEGASUS 4 one, agrees with experiment for $\alpha\le12^\circ$ and lies within
    $1.5\,\%$ of experiment at approach conditions. Maximum lift is not predicted. (Fig. 12)
    **Shown**
23. Averaged over the two cases, the time splits into projection $10\,\%$, interpolation about
    $50\,\%$, hole cutting about $30\,\%$ and overlap optimization about $5\,\%$. (Performance)
    **Shown**
24. A typical 3-D problem blanks about 5–15 % of the points, at 100–200 blanked points per CPU
    second on an SGI R10K 250 MHz. (Performance) **Shown**
25. The search finds on average 2–3 donor cells per point, at about 10,000 donor cells per CPU
    second, and about $5\,\%$ of the donors found are kept. (Performance) **Shown**
26. A complex 3-D problem needs about one labor day with PEGASUS 5 against 10–20 with PEGASUS 4,
    at least an order of magnitude less. (Performance) **Stated**
27. Automatic hole cutting still fails in two ways: (a) it misses hole points inside very thin
    bodies, fixed by OFFSET or a finer hole map; (b) it cuts improper holes at curved surfaces that
    overlapping surface meshes define ambiguously, fixed by naming a grid subset where no hole may
    be cut. (777 section; Conclusions) **Shown** / **Stated**

# Printed slips

- **CDP (p. 1040).** Printed:
  $\mathrm{CDP}=\sum_{j=1}^{3}\frac{(X_j)_{DB}\times V_B-(X_j)_{DI}\times V_I}{(X_j)_{DB}\times V_B}$,
  followed by "Values for the cell difference parameter will vary from 0 (the best) to very large
  values." Each term equals $1-(X_j)_{DI}V_I/\big((X_j)_{DB}V_B\big)$ with positive factors, so it is
  below 1, CDP is below 3, and CDP is negative whenever the donor cell is larger than the receptor
  cell *(compiler check, not in the sources)*. The formula as printed does not have the stated range,
  and the rule "smallest CDP kept" would then favour the largest donor. The paper does not show
  which form was intended.
- **Abstract vs body:** the abstract gives a speedup "up to a factor of 30 for very large
  problems"; the body gives 33 on 48 processors and the conclusions "over a factor of 33".
- Typographical: "negligable" (p. 1038), "acutally" (p. 1043), "less that that required"
  (p. 1044). The setup script name is printed "peg setup".

# Notation map

| Rogers et al. (2003) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $N$ (number of grids) | $n_g$ | **$N$ is reserved for the polynomial degree in the registry**; pairs $n_g(n_g-1)$ |
| field point | $\mathcal D_k$ | |
| hole point (blanked) | $\mathcal H_k$ | no iblank value convention printed |
| hole-fringe point, outer-boundary point, interpolation / recipient / boundary point | $\mathcal R_k$ | "boundary cell" in the CDP is the receptor's cell |
| orphan | $\mathcal O_k$ | |
| donor cell, "interpolation cell" | central cell of $\mathcal S_{\mathbf i}$ | trilinear: $q=2$ per direction, 8 donor points |
| fringe level | $n_f$ | Fig. 1 shows $n_f=2$ |
| OFFSET | hole enlargement by OFFSET cells | input variable, default 0 |
| fringe / outside / inside element | Cartesian hole-map element cut by the surface / exterior / interior | hole-map elements, not grid points; **"fringe element" is not a fringe point** |
| CDP, $(X_j)_{DB}$, $(X_j)_{DI}$, $V_B$, $V_I$ | page-local, kept | $V_B$, $V_I$ are bounding-box volumes, not the cell volumes $\lvert V_c\rvert$ |
| computational indices in $[0,1]$ relative to the donor cell | $\mathbf s$ | |
| $x,y,z$ | $\mathbf x$ | |
| $NP$ | number of MPI processes | page-local |
| $M$, Re, $\alpha$ | $M_\infty$, $Re$, $\alpha$ | agree |

# Reference list

24 printed references, numbered in AIAA superscript style. All 24 are merged complete into the
[bibliography](/bibliography.md) with `citedby` rogers-2003; AIAA papers printed without a
conference name are entered as technical reports with the AIAA paper number. Ref. 4 is printed
"AIAA 95-1680" (without "Paper") and kept as printed; refs. 13–14 print "PEGSUS 3.0/4.0 Users
Manual" as titled. The AEDC report AEDC-TR-85-64 is keyed `benek-1985-b`, distinct from the
conference paper benek-1985. There are no printed duplicates or unparseable items.

# Pages created or updated

Chunk 1 (2026-11-02). This source is cited on:

- [Multi-element airfoils](/benchmarks/multi-element-airfoil.md)
- [Domain connectivity and overset grid assembly](/definitions/domain-connectivity.md)
- [Fringe (receptor) points and overlap width](/definitions/fringe-point.md)
- [Grid hierarchy and priority](/definitions/grid-hierarchy.md)
- [Orphan points](/definitions/orphan-point.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [Donor search](/methods/donor-search.md)
- [Hole cutting](/methods/hole-cutting.md)
- [Implicit hole cutting](/methods/implicit-hole-cutting.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Moving overset grids](/methods/moving-overset-grid.md)
- [Overlap optimization](/methods/overlap-optimization.md)
- [Interpolation order and overlap requirements](/results/interpolation-order-requirement.md)
- [DCF and DCF3D (Meakin's domain connectivity function and code)](/software/dcf3d.md)
- [PEGASUS 5](/software/pegasus-5.md)
- [PEGASUS (PEGSUS) versions 1–4](/software/pegasus.md)
