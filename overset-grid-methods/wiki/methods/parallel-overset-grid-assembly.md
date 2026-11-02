---
type: Method
title: "Parallel and GPU overset grid assembly"
description: "How overset grid assembly is distributed: PEGASUS 5's coarse-grained master–worker MPI over grids and grid pairs, Roget and Sitaraman's assembly on the solver's own partitions with local data, query routing and adaptive load re-balancing (PUNDIT, HART-II scaling to 8192 cores), and Horne and Mahesh's GPU cutting and donor pairing by bounding volume hierarchies and GJK."
status: established
aliases: [parallel domain connectivity, parallel overset grid assembly, parallel OGA, GPU overset assembly, accelerated overset assembly, overset load balancing, load re-balance]
tags: [parallel, gpu, domain-connectivity, unstructured, rotorcraft]
timestamp: 2026-11-02T15:08:00Z
---

# Parallel and GPU overset grid assembly

[Domain connectivity](/definitions/domain-connectivity.md) on large overset
systems must run in parallel: the grids are too large for one process, the
flow solver is already distributed, and for
[moving grids](/methods/moving-overset-grid.md) the assembly is repeated every
step. Parallel assembly has to decide what is distributed (whole grids and grid
pairs, or the flow solver's partitions of every grid), how the receptor points
of one process meet the donor cells held by another, and how to balance a load
that depends on where grids overlap, not on how many cells a process holds. The
sources give three answers: coarse-grained task farming over grids and grid
pairs (PEGASUS 5), fine-grained assembly on the solver's partitions with
load re-balancing (PUNDIT), and on-node GPU acceleration of the geometric
kernels (Horne & Mahesh).

## Coarse-grained task farming (PEGASUS 5)

[Rogers et al. (2003)](/sources/rogers-2003.md), "Parallelization", Fig. 8,
parallelize [PEGASUS 5](/software/pegasus-5.md) with MPI as a master and
workers: the operations per grid or grid pair (surface projections for all
grid pairs, a tree build per grid, donor searches per grid pair, hole cutting
per grid, boundary-point identification per grid) are handed out by the master
as workers report completion, a dynamic load balancing. Ordering constraints
(all projections before all interpolations) create barrier-like idle phases,
and the final gather and write of all interpolation stencils is serial. A
52-grid case with 2429 operations runs just under 13 times faster on 15
processors (14 workers), with speedup saturating at about 14 beyond 16
processors; the Boeing 777 case (79 grids, 22.4 million points) reaches 33 on
48 SGI Origin processors, under 13 minutes. The parallel version always
reproduces the serial result (Conclusions). [Chan (2009)](/sources/chan-2009.md),
§7, records MPI parallelism as one of the three advances of the PEGASUS 5
re-engineering. [Noack (2005)](/sources/noack-2005.md) mentions a parallel
option of SUGGAR for hole cutting and donor search, unused in its runs.

The granularity is the grid: a run cannot use more workers than it has
grid-level operations at a time *(compiler check, not in the sources)*. Roget &
Sitaraman (2014), §1, count
"coarse-grain parallelism" (whole meshes on every process) and a partitioning
separate from the solver's, which needs replication or remapping of data, among
the limits of the existing assembly codes.

## Assembly on the solver's partitions (PUNDIT)

[Roget & Sitaraman (2014)](/sources/roget-2014.md) assemble overlapping
unstructured meshes, partitioned into mesh blocks by the flow solver itself
and distributed over many processes, using only per-process mesh data for the
non-Cartesian meshes, with no re-partitioning or replication (§1, §5). Their
code PUNDIT is the connectivity module of the Helios rotorcraft code. The six
steps (§2.2) are:

1. **hole profiling**: auxiliary Cartesian grids approximate each body's walls;
   only bounding boxes and integer tags are exchanged
   ([hole cutting](/methods/hole-cutting.md));
2. **query-point identification**: a point of a mesh block is sent as a query
   only to blocks of *other bodies* whose axis-aligned and oriented bounding
   boxes overlap its block, and only if it lies in the overlap of the two
   blocks' auxiliary grids (§3.2, Fig. 6); the receiving block keeps only the
   cells whose boxes overlap an oriented box around the received points (Fig. 8);
3. **mesh-block profiling**: cell neighbours and resolutions, an auxiliary grid
   per block and its *exact inverse map* (§3.3);
4. **donor search**: a line walk confined to one auxiliary cell, robust to the
   exits and re-entries of the search line through irregular partition
   boundaries, or an alternating digital tree (§3.4, §4;
   [donor search](/methods/donor-search.md));
5. **decision logic**: processes exchange accepted and rejected candidate
   donors and assign hole, field and receptor types by resolution (§3.5;
   [implicit hole cutting](/methods/implicit-hole-cutting.md));
6. **interpolation weights** (§3.6).

The query routing answers a failure of naive pairing: on the HART-II grids one
hollow fuselage block lies almost wholly inside the bounding box of all the
blade-1 blocks and would otherwise receive nearly every point of the 28 blocks
it may overlap (§3.2, Fig. 7; §5, Figs. 16–17).

**Load re-balancing** (§5). Partitioning at constant cells per partition gives
blocks of very different volumes; a large block overlapping many small ones
gets many queries, a block overlapping nothing (or only the Cartesian
background) none (Fig. 15). In page-local symbols, the load of each process is
its measured assembly time; with mean $\bar L$, the most loaded process
($L_{\max}$) repeatedly gives
$\Delta L=\min(L_{\max}-\bar L,\ \bar L-L_{\min})$ to the least loaded
($L_{\min}$), so that one of the two reaches the mean, until every process is
within 10% of $\bar L$. The resulting process-to-process table is turned into
block assignments assuming load proportional to query points: an overloaded
block is sliced along the longest extent of the oriented box of its query
points, at cuts set by cumulative query counts, and each slice is shipped with
its cells to an underloaded process by non-blocking MPI, the donor process
continuing its own work meanwhile (§5, Figs. 16–17). From the third assembly on,
the re-balance is *adaptive*: a process that measured load $L_{\mathrm m}$ and
had shipped work costing its helpers $L_{\mathrm s}=\sum_iL_i$ at the previous
assembly re-balances on the estimate $L_0=L_{\mathrm m}+L_{\mathrm s}$ of its
load without re-balance, which tracks moving and deforming grids; the overhead
of re-balancing is included in the measured loads. Re-balancing is implemented
only for the ADT search, because the line walk would need neighbour lists to be
shipped (§5, §7). The authors contrast it with the spatial decomposition
volumes of SUGGAR++, which re-partition parts of the grids so that queries and
donors share a process; PUNDIT keeps the solver partition and moves only
overloaded blocks, at the price of more communication at very large process
counts (§5).

**Measured scaling** (§6), on the HART-II rotor–fuselage configuration (four
blade meshes and one fuselage mesh, all near-body unstructured, no off-body
mesh; geometry of the HART II experiment, as cited) and a generic
wing–pylon–store configuration used only for static assembly
([store separation](/benchmarks/store-separation.md)):

| case | hardware | result |
|---|---|---|
| HART-II, 7 M nodes, 256 cores | 2.3 GHz AMD Opteron 6134 | assembly 1.3 s (7% of the time step) with the inverse-map walk, 2.6 s (14%) with the ADT; identical point-type counts; strong load imbalance in both (§6.1, Fig. 19) |
| same, ADT with re-balance | same | 2.1 s → 0.7 s after the first re-balance → 0.5 s after the first adaptive one; speedup at 256 cores 160 against 73 without (Figs. 20–21) |
| wing–pylon–store, 3 grids, 15 M cells, 64–512 cores | same | total time reduced by up to 80% (256 cores); speedup 213 against 117 at 256 cores, still well below linear (Fig. 23) |
| fine HART-II, 62 M nodes, 256–8192 cores | 2.6 GHz Intel Xeon E5-2670 | assembly time relative to the solver step: 12% → 3% at 256 cores, 136% → 21% at 8192 cores, the solver scaling almost ideally (Fig. 24) |

Speedups are computed from the total assembly time, re-balance overhead
included, assuming linear speedup from a serial run to the smallest process
count (§6.2). The authors call the scalability "far from ideal": the step that
identifies the data to transfer scales worst and tends to dominate, and the
imbalance of the query-identification step itself is not addressed; computing
the re-balance tables stays negligible up to 8192 cores (§6.2).

**TIOGA in a wind-farm stack.** [Sharma et al. (2021)](/sources/sharma-2021.md),
§1, assemble with TIOGA (cited to Roget & Sitaraman and to Brazell et al.),
an implicit-hole-cutting assembler, inside the ExaWind stack for blade-resolved
wind-farm simulations; they note that point-cloud interpolation stencils can
cross processor boundaries and add communication (§3.1.2), and they favour a
grid-by-grid (Schwarz) solve partly because it needs less MPI communication
than one global system (§3.2).

## GPU acceleration (Horne & Mahesh)

[Horne & Mahesh (2021)](/sources/horne-2021.md) port to GPUs the unstructured
overset method of their earlier work, which, as they recall, scaled to 492,000
CPU cores for 100,000 moving spheres (§1). The earlier timings showed cutting
and donor ("reconstruction-partner") pairing to be the two most expensive
assembly steps; the communication-pattern step is mostly MPI and stays on the
CPU (§2). Both steps reduce to one query, find every object of a set that
overlaps a given object, which real-time ray tracing and collision detection
answer with a **bounding volume hierarchy** (BVH) and an exact narrow-phase
test (§2):

- **Construction** (after Karras, as cited): each cell gets a Morton code by
  bit interleaving of its centroid coordinates, normalized by the partition
  size so that low float precision suffices; a radix sort orders the cells
  along this space-filling curve; each internal node covers a contiguous range
  of sorted cells split at the highest differing Morton bit, found by binary
  search in parallel; a bottom-up pass fills the bounding boxes, an atomic flag
  letting only the second thread to reach a node fill it. The tree has
  $2N_{\mathrm{obj}}-1$ nodes for $N_{\mathrm{obj}}$ cells (Fig. 4).
- **Query**: one GPU thread per query object, with its own stack of node
  pointers instead of recursion, descends only branches whose boxes overlap the
  query box; the leaf hits form the candidate pairs.
- **Narrow phase**: the Gilbert–Johnson–Keerthi (GJK) algorithm decides whether
  two convex polyhedra overlap by growing a simplex inside their Minkowski
  difference until it contains the origin or cannot; 3–5 iterations suffice
  for most tests, one thread per candidate pair. Box overlap alone is called
  unreliable for general unstructured cells.
- **Pipeline**: assign partitions and build communication patterns on the CPU;
  over-partition each partition into one piece per GPU of the node and build or
  update the BVHs; cut by explicit volumes (one thread per cell); fine-detail
  cut by BVH plus GJK against boundary faces; flood fill from the cut cells;
  pair receptors and donors by BVH plus GJK along the overset mesh edges and
  around cut regions ([hole cutting](/methods/hole-cutting.md)).
- **Reuse under motion**: with rigid motion of each partition the Morton order
  and tree topology are built once; afterwards only vertices and boxes are
  updated. Two empty trees per GPU are allocated at start-up and grown only
  when needed; the geometry is passed asynchronously as a "polyhedron soup".

On randomly arranged cuboid particles in a triply periodic box (100
configurations, about 40,000 cells per core, 4 nodes each with 4 NVIDIA V100
and a 24-core Xeon Gold 6126), the whole assembly runs about 15 times faster
than the CPU method, and the cutting and pairing kernels $O(10)$ to $O(100)$
times faster, the gain growing with the number of cells per core from 6,250 to
960,000 (§4.1, Figs. 10–11). The authors recall earlier GPU assemblies: a
gradient-search donor search of Chandar et al. (single GPU, static, one overset
mesh) and an ADT built on CPUs by Crabill et al. (16× on a K80 against four
cores) (§1).

## Parallel interpolation

Once assembled, the receptors must be filled across processes every step.
[Henshaw (2006)](/sources/henshaw-2006-b.md), §9.4, evaluates each
interpolation sum on the process that owns the donor stencil and ships the
sums to the owner of the receptors, so that at most one message passes between
any pair of processes ([inter-grid
interpolation](/methods/inter-grid-interpolation.md)).

## In-core assembly on solver partitions (Hedayat et al.)

[Hedayat et al. (2022)](/sources/hedayat-2022.md) partition every block over all processors as the flow solver prefers, so each processor cuts holes in its own partition; receptors are matched to processors by oriented bounding boxes, packed into one buffer per processor pair (worst-case messages $n\times P(m,2)$ instead of $C(n,2)\times P(m,2)$ for $n$ blocks on $m$ processors), searched by walking, and interpolated by a sparse PETSc matrix formed once per step (§2.2, Algorithms 2–3). Strong scaling on about 30 M points: assembly 5.1 s on 8 cores to 0.40 s on 140, then 0.58 s on 560 cores, about 7 % of the flow-solver time, limited by load imbalance; interpolation below 0.1 % (§4).

## Multiple solver instances (Li & Wang)

[Li & Wang (2022)](/sources/li-2022.md) give each component of an array its own instance of a single-solver code on an MPI intra-communicator and couple the instances by Roget & Sitaraman's assembly, run only on solver/process/block triples whose bounding boxes collide; against their dual-solver code this lowers assembly time, shrinks hole maps and scales better to 2880 processes (§3, §6). The off-body octree grid is refined so that background cells are not larger than the near-body cells they overlap ([AMR on overlapping grids](/methods/amr-on-overset-grids.md)).

## Qualifications

- Roget & Sitaraman print a "68% reduction" for 2.1 s → 0.7 s; the printed values
  give 67%, while 76% for 0.5 s agrees; the difference is consistent with rounding of
  the printed seconds *(compiler check, not in the sources)*.
- Horne & Mahesh state that the assembly comparison is not like-for-like: the CPU
  baseline uses other algorithms, and "a non-trivial portion of the speed-up is due to
  the new algorithms … rather than just through the use of GPUs" (§4.1). GJK is exact
  only for convex cells; the authors state that most cells are convex and describe no
  treatment of the others.
- PEGASUS 5's speedups and PUNDIT's are not comparable: the former distributes
  grid-level tasks of a structured preprocessor, the latter
  partitions of unstructured meshes inside a running solver *(compiler check, not
  in the sources)*.
- Chan (2009), §12, listed in 2008 the examination of load-balancing scaling and its
  effect on convergence, and a modular, fast, robust and automatic connectivity library
  for structured and unstructured grids, as open needs.

# Citations

- [Rogers et al. (2003)](/sources/rogers-2003.md) — "Parallelization", Fig. 8; Boeing 777 section; Conclusions.
- [Noack (2005)](/sources/noack-2005.md) — (parallel option of SUGGAR, unused in the reported runs).
- [Henshaw (2006)](/sources/henshaw-2006-b.md) — §9.4 (parallel interpolation).
- [Chan (2009)](/sources/chan-2009.md) — §7 (PEGASUS 5 MPI); §12 (open needs).
- [Roget & Sitaraman (2014)](/sources/roget-2014.md) — §1 (limits of existing codes); §2.2 (six steps); §3.2, Figs. 6–8; §3.3–3.6; §4; §5, Figs. 15–17 (load re-balance, SUGGAR++ comparison); §6, Figs. 19–24; §7.
- [Horne & Mahesh (2021)](/sources/horne-2021.md) — §1 (earlier GPU work, CPU scaling); §2, Figs. 3–6 (BVH, GJK, pipeline, reuse); §4.1, Figs. 10–11 (timings).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — §1 (TIOGA, ExaWind); §3.1.2; §3.2.
- [Hedayat et al. (2022)](/sources/hedayat-2022.md) — §2.2, §4, Algorithms 2–3.
- [Li & Wang (2022)](/sources/li-2022.md) — §2–§3, §6, Tables 2, 4.
