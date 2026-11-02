---
type: Definition
title: "Domain connectivity and overset grid assembly"
description: "The preprocessing that turns independent component grids into a usable overset grid: the domain connectivity information it produces (hole points, receptors, donors, weights), its phases, the algorithm families from the founding codes to partitioned, GPU and intersection-based assembly, and the measured costs of assembly for static and moving grids."
status: established
aliases: [overset grid assembly, OGA, grid assembly, overset assembly, domain connectivity information, DCI, domain connectivity function, DCF, oversetting process, connectivity, grid connectivity, overlapping grid connectivity]
tags: [domain-connectivity, hole-cutting, donor-search, moving-grid, parallel]
timestamp: 2026-11-02T15:27:00Z
---

# Domain connectivity and overset grid assembly

**Domain connectivity** is the information that couples the component grids of
an [overset grid](/definitions/overset-grid.md): which points are hole points
$\mathcal H_k$, which are receptor (fringe) points $\mathcal R_k$, and, for each
receptor, its donor grid $k'$, donor stencil $\mathcal S_{\mathbf i}$ and
interpolation weights $\alpha_{\mathbf j}$. **Overset grid assembly** is the
process that computes it. [Noack (2005)](/sources/noack-2005.md), §I, defines the
domain connectivity information (DCI) exactly as "which points are receptor
points along with their corresponding donor members and which are hole
points"; [Rogers et al. (2003)](/sources/rogers-2003.md) name three primary
operations — hole cutting, identification of interpolation points (hole-fringe
and outer-boundary points), identification of donor cells — and call a receptor
without a donor an [orphan](/definitions/orphan-point.md);
[Meakin & Suhs (1989)](/sources/meakin-1989.md) name the module the **Domain
Connectivity Function** (DCF).
[Chan (2009)](/sources/chan-2009.md), §7, defines domain connectivity as the
identification of hole points plus the search and storage of interpolation
stencils for the fringe points; [Roget & Sitaraman (2014)](/sources/roget-2014.md),
§2.1, call the process **overset grid assembly** (OGA) and state its task as
assigning every query point (node or cell centre) one of three exclusive
types, hole, field or receptor, with donor cells and weights for the
receptors, using no user input beyond the meshes, body tags and
boundary-condition locations; [Horne & Mahesh (2021)](/sources/horne-2021.md),
§2, name the parts of "overset assembly" communication patterns, cutting and
reconstruction-partner pairing.

## Output

The founding codes agree on the content of the output, not on its form.
PEGSUS writes two files, the composite grid and the interpolation data
([Benek et al. (1985)](/sources/benek-1985.md), p. 325); PEGASUS 5 writes the
interpolated points with their coefficients and donor cells and the blanked
points (Rogers et al. 2003); [Lee & Baeder (2003)](/sources/lee-2003.md), p. 1,
list the receptor points (indices, grid numbers) and donor cells (one corner's
indices, grid number, and the receptor's local coordinates $\mathbf s$ in the
cell); CMPGRD's output adds the mapping derivatives $\partial r_m/\partial x_n$
and the interpolation and discretization widths
([Chesshire & Henshaw (1990)](/sources/chesshire-1990.md), §4). The flow solver
reads the point classification as a mask
([point classification](/definitions/point-classification.md)) and applies the
interpolation at each step ([inter-grid
interpolation](/methods/inter-grid-interpolation.md)).

## Phases

Noack (2005), §§II–VI, orders assembly in four phases, which the other sources
share with variations:

1. **[Hole cutting](/methods/hole-cutting.md)** — mark points inside bodies or
   superseded by another grid as $\mathcal H_k$.
2. **Fringe identification** — mark the receptor layers around holes and on
   overlap (outer) boundaries ([fringe points](/definitions/fringe-point.md)).
3. **[Donor search](/methods/donor-search.md)** — locate, for each receptor, a
   donor cell in an overlapping grid and its local coordinates $\mathbf s$.
4. **Donor stencil and weights** — choose the stencil members and compute
   $\alpha_{\mathbf j}$.

Roget & Sitaraman (2014), §2.2, give a six-step pipeline for partitioned
meshes: hole profiling, query-point identification, mesh-block profiling,
donor search, decision logic (the only step that needs processor-to-processor
exchange of candidate donors), interpolation weights
([parallel and GPU overset grid assembly](/methods/parallel-overset-grid-assembly.md)).
Unlike Noack's order, the hole decision there comes *after* the donor search,
because a point is a hole point only if it finds no donor in the body's own
mesh ([hole cutting](/methods/hole-cutting.md)).

Automated codes add donor selection among several candidates and
[overlap optimization](/methods/overlap-optimization.md) (Rogers et al. 2003),
and projection of overlapping viscous surface grids before the donor search
([PEGASUS 5](/software/pegasus-5.md)).

## Algorithm families in the founding papers

- **Hierarchy-driven explicit cutting** (Benek et al. 1983, 1985;
  [PEGASUS / PEGSUS](/software/pegasus.md)): a strict
  [grid hierarchy](/definitions/grid-hierarchy.md) fixes who cuts whom and
  restricts the donor search to parent–child pairs; holes are bounded by a
  constant-index surface $\mathcal C$ of the embedded grid.
- **Priority-ordered classification** (Chesshire & Henshaw 1990, §3.2;
  [CMPGRD](/software/cmpgrd.md)): every point is assigned a status by a
  six-step iteration to a fixed point over a signed flag; exterior points are
  seeded next to physical boundaries and grow; unneeded interpolation points
  are deleted and interpolation points that can be discretized are converted;
  the authors estimate the cost at $O(n_g^2N_{\mathrm{pts}})$ operations.
- **Boundary-condition-driven automation** (Rogers et al. 2003; PEGASUS 5): the
  solid-wall boundary conditions of the flow-solver input define the hole
  cutters, a Cartesian hole map with a line-of-sight test cuts the holes,
  every point of every grid is searched against all $n_g(n_g-1)$ ordered grid
  pairs, a cell-difference parameter chooses among donors, and overlap
  optimization keeps the finest points.
- **Cell selection** (Lee & Baeder 2003;
  [implicit hole cutting](/methods/implicit-hole-cutting.md)): the two-step
  "cut, then search" procedure is replaced by a donor search for every point,
  keeping the smallest-volume cell; holes appear as a by-product, and no
  hierarchy, priority, hole optimization or tree data structure is used.
  Roget & Sitaraman (2014), §3.5, choose field and receptor points by the same
  resolution (cell-volume) comparison on unstructured meshes; TIOGA, as used by
  [Sharma et al. (2021)](/sources/sharma-2021.md), §1 and Fig. 4, cuts holes
  implicitly with mandatory fringe layers counted in cells from each outer
  boundary ([implicit hole cutting](/methods/implicit-hole-cutting.md)).
- **Tree-based cutting of general grids** (Noack 2005;
  [SUGGAR](/software/suggar.md)): octree or binary-tree Cartesian
  approximations of each body's cutting surface, a body hierarchy in which
  "siblings cut each other", node- and cell-centred fringe rules, and a
  neighbour-walk donor search through general polyhedra.
- **Partitioned, local-data assembly** (Roget & Sitaraman 2014; PUNDIT): every
  mesh partition profiles its own cells on auxiliary Cartesian grids, query
  points are routed between processes by bounding-box overlap, holes come from
  a wall-approximating auxiliary grid plus the donor search, and overloaded
  partitions are sliced and shipped at run time.
- **GPU collision-detection assembly** (Horne & Mahesh 2021): cutting and donor
  pairing reduce to one query, find all objects of a set that overlap a given
  object, answered by a linear bounding volume hierarchy and the GJK
  convex-overlap test on GPUs.
- **Geometric intersection without holes** ([Picard et al.
  (2021)](/sources/picard-2021.md), §3.2.2): two layers of receptor cells are
  marked on each grid from the patch boundary, and their geometric
  intersections with the other grid's cells (volumes and barycentres) are
  computed once; no cell is blanked.

Lee & Baeder (2003), pp. 2–3, describe the common two-step procedure of DCF3D,
Overture, PEGASUS, BEGGAR, ChalMesh/Xcog and FASTRAN as: cut holes into a mask
array, extract the list of inter-grid boundary points (outer-boundary and
hole-fringe points), then search donors for that list; they identify the mask
as the main difficulty.

## Assembly as a separate code or inside the solver

PEGASUS and SUGGAR are stand-alone preprocessors; the flow-solution algorithm
is "hidden" from PEGASUS/XMERA management so almost any solver can be
substituted (Benek et al. 1983, p. 376). Noack (2005), §I, contrasts codes where
assembly is integral to the solver (BEGGAR, DCF3D); Lee & Baeder (2003) say
their implicit hole cutting can be integrated in the flow solver or run
stand-alone, and that the solver then needs only one more array dimension
(`P(i,j,k)` → `P(i,j,k,ngrid)`, p. 3).

## Static and moving grids

For a static configuration assembly runs once and is cheap relative to a
converged solution, especially when one grid system serves many flow
conditions (Meakin & Suhs 1989, §II). For bodies in relative motion it runs
every time step, coupled cyclically with the flow solver (which needs the mask
and interpolation data) and the body dynamics (which needs the loads and
supplies the positions) (Meakin & Suhs 1989, §II; Noack 2005, §VII); see
[moving overset grids](/methods/moving-overset-grid.md). Meakin & Suhs limit
the level-$(n+1)$ hole search to the points on either side of the level-$n$ hole
boundaries; Noack builds the hole-cutting and donor-search trees once in each
body's own frame and transforms query points instead of grids, and couples
SUGGAR, the flow solver and a motion controller through blocking Unix FIFOs.
Noack (2005), §I, states that PEGASUS 5 "has not been applied to moving body
problems".

[Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md), §3.1 and Fig. 6, call
Ogen once per step on the *predicted* grid positions: only grids affected by
the motion are reconsidered, the previous classification is the initial
guess, invalidated receptors get a local search for new donors, and the full
algorithm is the fallback when the local search fails; connectivity is not
recomputed after the corrector of the rigid-body integrator, since the
predicted positions are already second-order accurate (§3.4). Points that the
motion uncovers get values at the old time by interpolation ([exposed
points](/definitions/exposed-point.md)). Banks et al. (2016), §4.1, regenerate
the deforming interface grids and then the connectivity ("cut holes, determine
interpolation points") with Ogen at every step;
[Wang et al. (2021)](/sources/wang-2021.md), §III A, recompute interpolation
coefficients at every 1° rotation step of a propeller grid. Horne & Mahesh
(2021), §2, exploit rigid motion of each mesh partition: the space-filling
ordering and tree topology of the bounding volume hierarchy are built once and
only the bounding boxes are updated. Roget & Sitaraman (2014), §3.3, compute
cell neighbours once and recompute cell resolutions only for elastically
deforming meshes. Picard et al. (2021) detect the receptor cells once, the
patch being fixed.

## Measured cost

| Source | Case | Hardware | Cost |
|---|---|---|---|
| Meakin & Suhs (1989), Table 1 | wing/store, 2 grids, 243,906 points | NAS CRAY-2 | connectivity/flow-solver CPU time per iteration: PEGASUS 1.96, restricted DCF 0.64 |
| Meakin & Suhs (1989), Table 1 | Shuttle SRB separation, 3 grids, 357,330 points | NAS CRAY-2 | same ratio: PEGASUS 5.27, restricted DCF 2.02 |
| Chesshire & Henshaw (1990), §6.4, §6.5 | cylinder in channel, three resolutions; two-flap airfoil | IBM 3090VF | 1.6, 3.1, 7.2 s; 9.3 s |
| Lee & Baeder (2003), Example | quad tilt rotor half model, 39 grids, ≈2.5 M points | Alpha 21264, 667 MHz | ≈45 s; linear instead of cubic interpolation saves ≈20–25% |
| Rogers et al. (2003) | 30P30N airfoil, 7 zones, 313,000 points | one SGI R10K, 250 MHz | 65 s |
| Rogers et al. (2003) | Boeing 777-200, 79 grids, 22.4 M points | SGI Origin, 16 / 48 processors | 40 min (just over 9 CPU h, 85% efficiency) / under 13 min (speedup 33) |
| Noack (2005), Table 2 | wing/pylon/store, structured, 3.64 M points | Pentium 4, 2.6 GHz | setup 283 s; per step ≈15 s holes + 39 s donors + 10 s output |
| Noack (2005), Table 3 | C130 + parachute + cargo, 2 unstructured + 15 structured, 4.85 M points | same | per step ≈81 s holes + 53 s donors + 71 s output |
| Henshaw & Schwendeman (2006), Table 6 | shock-driven cylinder, moving composite grid, no AMR / one AMR level | 2.2 GHz Xeon desktop | moving-grid generation 0.66 s of 17.8 s per step (3.7%) / 0.164 s of 3.81 s (4.3%); exposed points 0.13% / 0.17% |
| Roget & Sitaraman (2014), §6.1 | HART-II rotor–fuselage, 5 unstructured meshes, 7 M nodes | 256 cores, 2.3 GHz AMD Opteron 6134 | assembly 1.3 s (7% of the time step) with the exact inverse map, 2.6 s (14%) with the ADT; identical point-type counts |
| Roget & Sitaraman (2014), §6.2 | same, ADT with load re-balance | same | 2.1 s → 0.7 s → 0.5 s |
| Roget & Sitaraman (2014), §6.2 | fine HART-II, 62 M nodes | up to 8192 cores, 2.6 GHz Xeon E5-2670 | assembly/solver time 136% without, 21% with re-balance at 8192 cores |
| Horne & Mahesh (2021), §4.1 | random cuboid particles, ≈40,000 cells per core, 100 configurations | 4 nodes × (4 V100 + 24-core Xeon Gold 6126) | overall assembly ≈15× faster than the CPU method; cutting and pairing kernels $O(10)$–$O(100)$× |

Rogers et al. (2003) split PEGASUS 5's time, averaged over their two cases, as
interpolation ≈50%, hole cutting ≈30%, projection 10%, overlap optimization
≈5%; a typical 3-D case blanks 5–15% of the points, at 100–200 blanked points
per CPU second, and finds 2–3 donor cells per point at ≈10,000 donor cells per
CPU second, of which ≈5% are kept. The labour cost dominated before
automation: PEGASUS 4 needed over 17,000 lines of input for a 153-grid,
33-million-point high-lift case, and the 777 connectivity took 32 labour days
with PEGASUS 4 against 3 with PEGASUS 5. Meakin & Suhs (1989) attribute the
remaining DCF cost to problem-dependent configurations and to DCF routines
that do not vectorize; in static PEGASUS runs, hole definition is typically
the most expensive task (§II).

Chesshire & Henshaw's $O(n_g^2N_{\mathrm{pts}})$ estimate and Rogers et al.'s
$n_g(n_g-1)$ grid pairs both grow quadratically in the number of grids
*(compiler check, not in the sources)*; Rogers et al. answer it with bounding-box rejection of non-intersecting
pairs and Lee & Baeder with a symmetric overlap matrix built from boundary
points first ([donor search](/methods/donor-search.md)).

## Parallel assembly

The algorithms, measurements and limits of parallel and GPU assembly are
collected on [parallel and GPU overset grid
assembly](/methods/parallel-overset-grid-assembly.md); the founding
measurements are kept here.

PEGASUS 5 distributes per-grid and per-grid-pair operations (projections,
tree builds, donor searches, hole cutting, boundary-point identification) from
an MPI master to workers with dynamic load balancing; the final gather of all
stencils is serial, and speedup saturates (a 52-grid case with 2429 operations:
just under 13 on 15 processors, asymptote ≈14 beyond ≈16 processors; the 777:
33 on 48 processors) (Rogers et al. 2003, Parallelization, Fig. 8). The parallel
version always reproduces the serial result (Conclusions). SUGGAR has a parallel
option for hole cutting and donor search that Noack (2005) did not use in the
reported runs. Chan (2009), §12, lists a modular, fast, robust and automatic
connectivity library for structured and unstructured grids, and the study of
load-balancing scaling, among the open needs of 2008, and states (§7) that no
approach yet satisfied "the combined requirements of full automation,
robustness, and speed".

## Assembly coupled to the solver

In two 2022 solvers assembly is coupled directly to the flow solver: [Hedayat et al. (2022)](/sources/hedayat-2022.md) replace a file-based sequential assembly by an in-core parallel one inside the solver and report assembly at about 7 % of the flow-solver time on 560 cores (§4); [Li & Wang (2022)](/sources/li-2022.md) run assembly between solver instances, restricted to overlapping process pairs (§3). Li & Wang reuse the pipeline of Roget & Sitaraman, Hedayat et al. explicit hole cutting; both are described on [parallel overset grid assembly](/methods/parallel-overset-grid-assembly.md).

## Classification before the donor search

[Oh et al. (2024)](/sources/oh-2024.md) invert the usual order of assembly — point classification by exact wall distance first, donor search on the remaining query points after — and report faster assembly than post-classification in all tests ([wall-distance hole cutting](/methods/wall-distance-hole-cutting.md)).

## Qualifications

- Rogers et al. (2003) print a speedup "up to a factor of 30 for very large"
  problems in the abstract, and "a factor of 33" (body) / "over a factor of 33"
  (Conclusions) for the 777 run on 48 processors.
- Noack (2005), §VIII, prints a C130 setup total of 335 s for components of
  256, 14 and 79 s, which sum to 349 s *(compiler check, not in the sources)*.
  Its Table 2 totals (26 structured grids, 3,639,804 points, 3,411,400 cells)
  exceed the sums of the 25 listed rows (3,108,363 points, 2,899,400 cells) by
  531,441 $=81^3$ points and 512,000 $=80^3$ cells, the size of one
  $81\times81\times81$ grid not listed *(compiler check, not in the sources)*.

# Citations

- [Benek et al. (1983)](/sources/benek-1983.md) — p. 376 (PEGASUS/XMERA roles, solver hidden from management).
- [Benek et al. (1985)](/sources/benek-1985.md) — pp. 323–325 (PEGSUS input, hierarchy-restricted search, two output files).
- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §II (DCF, cyclic ADF/BDF/DCF coupling, restricted search, Table 1).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §3.2, pp. 14–21 (composite grid algorithm, cost estimate); §4 (output); §6.4–6.5 (construction times).
- [Lee & Baeder (2003)](/sources/lee-2003.md) — pp. 1–3 (output, existing two-step procedure, solver integration); Example, p. 12 (timing).
- [Rogers et al. (2003)](/sources/rogers-2003.md) — "Automation of the Oversetting Process", "Boundary Point Interpolation", "Parallelization", "Performance", Boeing 777 section, Conclusions.
- [Noack (2005)](/sources/noack-2005.md) — §I (DCI definition, codes); §§II–VII (phases, moving bodies, FIFOs); §VIII, Tables 2–3 (timings).
- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) — §3.1, §3.4, Fig. 6 (Ogen update per step); Table 6.
- [Chan (2009)](/sources/chan-2009.md) — §7 (definition, state of the art); §12 (needs).
- [Roget & Sitaraman (2014)](/sources/roget-2014.md) — §2.1–2.2 (OGA, point types, six steps); §3.3; §6.1–6.2 (timings).
- [Banks et al. (2016)](/sources/banks-2016.md) — §4.1 (connectivity regenerated each step).
- [Picard et al. (2021)](/sources/picard-2021.md) — §3.2.2 (intersection-based receptor marking, done once).
- [Horne & Mahesh (2021)](/sources/horne-2021.md) — §2 (overset assembly, BVH reuse); §4.1 (GPU timings).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — §1, Fig. 4 (TIOGA assembly).
- [Wang et al. (2021)](/sources/wang-2021.md) — §III A (coefficients recomputed each rotation step).
- [Hedayat et al. (2022)](/sources/hedayat-2022.md) — §2.2, §4.
- [Li & Wang (2022)](/sources/li-2022.md) — §3.
- [Oh et al. (2024)](/sources/oh-2024.md) — Abstract, Conclusions.
