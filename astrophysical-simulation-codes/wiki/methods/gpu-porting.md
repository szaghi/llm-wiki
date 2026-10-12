---
type: Method
title: "Porting compressible-flow codes to GPUs"
description: "The design choices the GPU code papers document — programming model (CUDA, HIP, CUDA Fortran, OpenACC, Kokkos, framework or own backend abstraction), device-resident versus host-resident data, array layout for coalescing, register pressure and kernel fusion, host–device transfers, GPU-aware MPI and compute–communication overlap, and where AMR bookkeeping runs — with the measured consequences each source reports."
status: established
aliases: [GPU port, GPU acceleration, device-resident execution, GPU offload, performance portability]
tags: [gpu, performance-portability, kokkos, cuda, openacc, performance, scaling, amr]
timestamp: 2026-10-12T00:00:00Z
---

# Porting compressible-flow codes to GPUs

A GPU port of a finite-volume or finite-difference compressible solver has to
decide how the kernels are written, where the data live, how arrays are laid
out, how much each kernel does, how ghost data move between devices, and where
the mesh bookkeeping runs. The sources below document these decisions for ten
codes. Comparisons of throughput across codes are not like-for-like unless
hardware, precision, scheme and normalization agree; see
[cell-update throughput](/definitions/cell-updates-per-second.md) and
[parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).

## Programming model

| Code | Model | Stated reason or consequence |
|---|---|---|
| [GAMER](/software/gamer.md) | CUDA | CUDA thread blocks and streams ([Zhang et al. (2018)](/sources/zhang-2018.md), §4) |
| [Enzo](/software/enzo.md) | CUDA C/C++ port of PPM and the Dedner MHD solver | fields copied to and from the device around each solver call ([Bryan et al. (2014)](/sources/bryan-2014.md), §12.3) |
| [Cholla](/software/cholla.md) | C++/CUDA; a macro header `gpu.hpp` maps CUDA calls to HIP at compile time | one CUDA-written code base for NVIDIA and AMD ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §2.3.2) |
| [STREAmS](/software/streams.md) | CUDA Fortran `!$cuf` automatic kernels plus explicit kernels | directives, CUDA, OpenCL and HIP were weighed; `cuf` kernels keep "the large majority of the code" unaltered ([Bernardini et al. (2021)](/sources/bernardini-2021.md), §4.1) |
| [ADAM](/software/adam.md) | CUDA Fortran `cuf` kernels, some explicit kernels; other back-ends "under development" | code split by dependence on equation and on back-end, to avoid one implementation per equation per back-end ([Zaghi et al. (2023)](/sources/zaghi-2023.md), §2.1–§2.2) |
| [gPLUTO](/software/gpluto.md) | OpenACC directives in a C++ rewrite | simpler than CUDA; the same source runs on CPUs with the directives ignored; OpenMP planned for AMD ([Rossazza et al. (2026)](/sources/rossazza-2026.md), §3.1, §5) |
| [AthenaK](/software/athenak.md) | Kokkos | instructions "effectively translated into the native programming environment" of each target; CPUs, NVIDIA, AMD and ARM from one source ([Stone et al. (2026)](/sources/stone-2026.md), §1–§2) |
| [IDEFIX](/software/idefix.md) | Kokkos, bundled as a git submodule | without an accelerator the device code compiles as host code "with very little overhead"; arrays follow K-Athena ([Lesur et al. (2023)](/sources/lesur-2023.md), §3.1) |
| [Quokka](/software/quokka.md) | AMReX (NVIDIA GPUs, `nvcc`) | the paper states no programming model beyond AMReX ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.1.9, §4.1) |
| [GRaM-X](/software/gram-x.md) | AMReX lambda kernels through the CarpetX driver; CUDA, HIP and SYCL back-ends | the framework, not the physics code, owns the back-end ([Shankar et al. (2023)](/sources/shankar-2023.md), §III) |
| [Neko](/software/neko.md) | own abstract Fortran types with one extension per backend (CPU, SX-Aurora, GPU, FPGA), chosen at run time | argues that Kokkos, OCCA, OP2 and OPS force deep integration and tie longevity to the library, and that offload does not fit native-mode accelerators ([Jansson et al. (2024)](/sources/jansson-2024.md), §2.1, §3.1) |

[Athena++](/software/athena-plus-plus.md) reaches GPUs only through its
Kokkos port K-Athena ([Stone et al. (2020)](/sources/stone-2020.md), §1,
§3.6.2); AthenaK is the from-scratch Kokkos version of the same framework, in
which "very little of the overall design was changed"
([Stone et al. (2026)](/sources/stone-2026.md), §2). AthenaK drops curvilinear
coordinates partly because virtual functions and polymorphism "are not
supported by the compilers currently available on many GPUs" (§2).

## Where the data live

Two designs appear.

**Host-resident, streamed.** [GAMER](/software/gamer.md) keeps all data in
host memory and sends "a small number of patch groups (typically a few
hundreds)" to the GPU at a time, overlapping transfers and kernels with CUDA
streams and running the gather/scatter and AMR work on OpenMP threads
concurrently ([Zhang et al. (2018)](/sources/zhang-2018.md), §4). Enzo's CUDA
port copies fields to and from the device around each solver call
([Bryan et al. (2014)](/sources/bryan-2014.md), §12.3). The older Cholla used an
"extreme version of the 'offload' model", copying the conserved arrays to and
from the GPU every step ([Caddy & Schneider (2024)](/sources/caddy-2024.md),
§2.3.1).

**Device-resident.** Every other GPU code here keeps the solution on the
device and moves it to the host only for output, initial conditions or mesh
changes (Quokka does not state its policy,
[Wibking & Krumholz (2022)](/sources/wibking-2022.md), §4.1):
* STREAmS copies host to device once before time marching and back at the end
  ([Bernardini et al. (2021)](/sources/bernardini-2021.md), §4.1).
* The new Cholla keeps all data on the GPU, with only initial conditions and
  file I/O on the CPU; HDF5 cannot write from GPU memory. No timing of the
  old against the new model is given beyond "considerable speedup"
  ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §2.3.1, §5).
* IDEFIX runs the whole algorithm "exclusively on the device"; the host does
  I/O, initial conditions and exception handling, with host mirrors for
  these ([Lesur et al. (2023)](/sources/lesur-2023.md), §3.1).
* AthenaK data are "always stored on the device, and is never moved to the
  host except for outputs"; the device-to-host copy "enables asynchronous
  outputs" ([Stone et al. (2026)](/sources/stone-2026.md), §2).
* In gPLUTO "the entire computational workload is handled by the GPUs" and no
  host–device transfers occur during computation
  ([Rossazza et al. (2026)](/sources/rossazza-2026.md), §3.1).
* In GRaM-X "all data are stored on the accelerator's built-in memory at all
  times", moved only for I/O, so every routine, including wave extraction,
  must run on the device ([Shankar et al. (2023)](/sources/shankar-2023.md),
  §III, §III C).
* In ADAM the compute phase runs on the GPU; CPU–GPU copies, with
  transposition, occur only at I/O and AMR updates
  ([Zaghi et al. (2023)](/sources/zaghi-2023.md), §2.2).

**Unified (managed) memory.** gPLUTO combines CUDA Unified Memory
(`-gpu=managed`) with explicit `enter data`/`exit data` directives for deep
copies of nested structures, leaving most movement to the driver
([Rossazza et al. (2026)](/sources/rossazza-2026.md), §3.3). GRaM-X places
its tabulated nuclear equation of state in unified memory, accessible from
host and device ([Shankar et al. (2023)](/sources/shankar-2023.md), §II C).
STREAmS rejects managed memory because the prefetch hints it needs (as in the
CaNS code) "reduce the readability"
([Bernardini et al. (2021)](/sources/bernardini-2021.md), §4.1).

**Device memory as the binding limit.** Cholla stores only conserved
variables and recomputes primitives and the cell-centred field when needed,
because "Cholla is generally limited instead by GPU memory"; about $500^3$
cells fit on one 80 GB A100 and about $459^3$ on one MI250X GCD
([Caddy & Schneider (2024)](/sources/caddy-2024.md), §1, §2.3.1). gPLUTO
switches from constrained transport to
[GLM cleaning](/methods/glm-divergence-cleaning.md) in strong scaling because
GLM "requires less device memory", allowing a larger grid (no numbers)
([Rossazza et al. (2026)](/sources/rossazza-2026.md), §4.1). ADAM allocates
its device field "generally" to occupy the entire GPU memory
([Zaghi et al. (2023)](/sources/zaghi-2023.md), §2.2).

## Array layout and coalescing

* **STREAmS**, one V100, channel flow on $360\times240\times360$ points:
  moving the variable index from fastest to slowest (AoS to SoA) alone slowed
  the streamwise flux kernel from 76 to 330 ms, but together with transposed
  copies for that direction, precomputed primitives (fewer accesses and
  divisions, no register spilling) and reordered MPI buffers it cut the total
  from 656 to 297 ms, a factor 2.2; global-load efficiency rose from 25–30%
  to 54–90% and store efficiency from 25% to 90–100% (Tables 1–2)
  ([Bernardini et al. (2021)](/sources/bernardini-2021.md), §4.2).
* **gPLUTO** replaces pointer-to-pointer arrays by flat arrays wrapped in
  `Ary` classes with order $(i,j,k,\text{variable})$, $i$ fastest, so that
  consecutive threads touch adjacent addresses; sweep buffers are viewed as
  per-$(j,k)$ slices and reordered for the $y$ sweep to stay coalesced. Each
  kernel collapses the three spatial loops and runs the loop over variables
  sequentially, because parallelizing it "usually tends to lower the
  performance" ([Rossazza et al. (2026)](/sources/rossazza-2026.md), §3.2–§3.3).
* **ADAM** transposes its device field so that the block index is the
  contiguous one, "to maximize access data coalescing for contiguous CUDA
  threads" ([Zaghi et al. (2023)](/sources/zaghi-2023.md), §2.2).
* **AthenaK** stores each physics module's variables as Kokkos Views with one
  more dimension than space, the extra index running over MeshBlocks
  ([Stone et al. (2026)](/sources/stone-2026.md), §2). IDEFIX wraps
  `Kokkos::View`; neither paper discusses AoS against SoA
  ([Lesur et al. (2023)](/sources/lesur-2023.md), §3.1).

## Kernel granularity and register pressure

* **Launch count.** AthenaK packs all MeshBlocks of a device into one
  MeshBlockPack so that one kernel launch covers them, which "greatly
  enhances performance when there are a large number of small MeshBlocks"
  ([Stone et al. (2026)](/sources/stone-2026.md), §2). GAMER groups eight
  patches into one CUDA thread block to cut ghost-zone overhead
  ([Zhang et al. (2018)](/sources/zhang-2018.md), §4).
* **Templating against spills.** AthenaK templates some options (e.g. Riemann
  solvers) because "the number of registers is extremely limited on many
  GPUs" ([Stone et al. (2026)](/sources/stone-2026.md), §2). gPLUTO templates
  direction-dependent kernels on the sweep direction so that a small local
  array fits in registers ([Rossazza et al. (2026)](/sources/rossazza-2026.md),
  §3.3). GRaM-X attributes a 4× drop from static to dynamical spacetime to
  register spills in the spacetime solver
  ([Shankar et al. (2023)](/sources/shankar-2023.md), §V A).
* **Kernel fusion cuts both ways.** Fusing piecewise-constant reconstruction
  into the Riemann kernel improved Cholla's runtime by about 10%; fusing
  characteristic PLM into it slowed the code by about 10–15% through higher
  register use and lower occupancy, an outcome that "depends on compiler
  optimizations" ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §2.3.1).
* **Stack temporaries.** STREAmS writes explicit CUDA kernels for the Euler
  fluxes because the CPU routine's large temporaries would go to the kernel
  stack, so CPU and GPU flux code differ
  ([Bernardini et al. (2021)](/sources/bernardini-2021.md), §4.2).
* **Reductions.** Cholla computes the global time-step reduction on the GPU
  with an integer-encoded `atomicMax` (CUDA has no floating-point one),
  "slightly faster" than its former hybrid GPU+CPU reduction and much better
  at large element counts ([Caddy & Schneider (2024)](/sources/caddy-2024.md),
  §2.3.3).

## Inter-device communication

* **Device-side packing.** IDEFIX, AthenaK and gPLUTO pack and unpack ghost
  buffers in device kernels
  ([Lesur et al. (2023)](/sources/lesur-2023.md), §3.4;
  [Stone et al. (2026)](/sources/stone-2026.md), §2;
  [Rossazza et al. (2026)](/sources/rossazza-2026.md), §3.4); Cholla sends
  MPI messages directly from GPU buffers
  ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §2.3.1). IDEFIX credits
  device-side packing, "probably", for scaling slightly better than PLUTO
  beyond 10,000 CPU cores ([Lesur et al. (2023)](/sources/lesur-2023.md), §5).
* **GPU-aware MPI** is stated by STREAmS (optional, chosen at compile time),
  IDEFIX, Cholla and ADAM
  ([Bernardini et al. (2021)](/sources/bernardini-2021.md), §4.3;
  [Lesur et al. (2023)](/sources/lesur-2023.md), §3.4;
  [Caddy & Schneider (2024)](/sources/caddy-2024.md), §2.3.1;
  [Zaghi et al. (2023)](/sources/zaghi-2023.md), §2.2). AthenaK and gPLUTO
  send device-memory buffers but do not state whether the MPI is GPU-aware
  ([Stone et al. (2026)](/sources/stone-2026.md), §2;
  [Rossazza et al. (2026)](/sources/rossazza-2026.md), §3.4). In Quokka
  CUDA-aware MPI "did not improve performance"
  ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §4.1).
* **Exchange pattern.** IDEFIX exchanges dimension by dimension ($x$, then
  $y$, then $z$) with persistent communications, measured "generally faster,
  especially on NVidia GPUs" than a simultaneous 26-neighbour exchange, but
  unsuitable for AMR ([Lesur et al. (2023)](/sources/lesur-2023.md), §3.4).
  gPLUTO exchanges with up to 26 neighbours in 3D using `async` queues for
  packing and unpacking ([Rossazza et al. (2026)](/sources/rossazza-2026.md),
  §3.4). AthenaK's message count is proportional to the MeshBlocks in a
  rank's pack ([Stone et al. (2026)](/sources/stone-2026.md), §2).
* **Overlap.** STREAmS computes interior fluxes while ghost nodes travel and
  then the boundary fluxes; with it, weak scaling on 1024 V100s stays at about
  97%, visibly above the synchronous variant; in strong scaling the gain is
  "visible, but not remarkable" ([Bernardini et al. (2021)](/sources/bernardini-2021.md),
  §4.3). Neko overlaps its gather–scatter with local work
  ([Jansson et al. (2024)](/sources/jansson-2024.md), §3.2). GRaM-X has no
  overlap yet — a kernel starts only after all ghost zones of the previous
  one are filled — and attributes its 40–50% weak-scaling efficiency to
  ghost-zone communication ([Shankar et al. (2023)](/sources/shankar-2023.md),
  §III C, §V B). Quokka estimates that perfect overlap would raise its 1→4
  GPU efficiency above 99% (hydro) and 96% (radiation hydrodynamics), where
  ghost filling takes 42% and 53% of the 4-GPU wall time
  ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §4.1, Table 4).
  GAMER proposes overlapping MPI with CPU/GPU work as the fix for its
  efficiency loss at 512 nodes and more
  ([Zhang et al. (2018)](/sources/zhang-2018.md), §6).

## Mesh refinement on GPUs

See [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* **Tree on the host, fields on the device.** AthenaK creates, stores and
  refines the tree on the host, with Kokkos DualViews for data needed on both
  sides, while prolongation, restriction and ghost loading run "all at once
  inside parallel kernels" ([Stone et al. (2026)](/sources/stone-2026.md),
  §2). ADAM keeps the octree in a serial hash map replicated on all
  processes, precomputes neighbour arrays so that the compute core shows "no
  evidence that this is AMR code", and refines on the CPU after copying the
  field back ([Zaghi et al. (2023)](/sources/zaghi-2023.md), §2.2). GAMER runs
  all AMR operations on the CPU, concurrently with the GPU
  ([Zhang et al. (2018)](/sources/zhang-2018.md), §4). In GRaM-X "all of
  CarpetX's basic operations are fully GPU enabled"
  ([Shankar et al. (2023)](/sources/shankar-2023.md), §III).
* **Measured AMR cost.** AthenaK, 2D MHD blast on one A100: about 20%
  throughput overhead (181 → 141 million cell updates per second), wall time
  18% of the uniform run ([Stone et al. (2026)](/sources/stone-2026.md), §5.1,
  Fig. 20). Quokka: single-node AMR per-GPU throughput about 50% below the
  uniform grid ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §4.2).
  ADAM: the serial AMR update grows from 0.74 s (1562 blocks) to 527.97 s
  (684,258 blocks) and dominates at high block counts
  ([Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.2, Table 1).
* **Time stepping.** GRaM-X uses one global step because subcycling
  "necessarily serializes evolving different refinement levels" (asserted,
  not measured) ([Shankar et al. (2023)](/sources/shankar-2023.md), §III A);
  Quokka subcycles and names sequential level-by-level stepping as one cause
  of its AMR efficiency loss ([Wibking & Krumholz (2022)](/sources/wibking-2022.md),
  §4.2). Cholla, STREAmS and IDEFIX have no mesh refinement
  ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §1;
  [Bernardini et al. (2021)](/sources/bernardini-2021.md), §3;
  [Lesur et al. (2023)](/sources/lesur-2023.md), §2.6).

## Load per device

Every GPU source finds that a device needs a large local problem:
* AthenaK on one A100, same total grid: 614, 413, 242 and 126 million cell
  updates per second for MeshBlocks of $128^3$, $64^3$, $32^3$ and $16^3$;
  "Running small problems on GPUs is not an effective use of resources"
  ([Stone et al. (2026)](/sources/stone-2026.md), §5.1). On CPUs Athena++
  recommends $8^3$–$16^3$ blocks with AMR
  ([Stone et al. (2020)](/sources/stone-2020.md), §3.6.5); neither paper
  compares the two regimes.
* IDEFIX: GPUs pay off "only for subdomains larger than $64^3$"; performance
  drops substantially below $64^3$ per GPU
  ([Lesur et al. (2023)](/sources/lesur-2023.md), §5).
* Quokka: keep at least $256^3$ cells per GPU per level
  ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §4.2).
* GRaM-X: below about $120^3$ cells per GPU "very inefficient", about $160^3$ a
  good compromise ([Shankar et al. (2023)](/sources/shankar-2023.md), §V C).
* ADAM: efficient above about 250,000 cells per GPU; blocks of $16^3$ cells
  are cheaper per cell than $8^3$ ([Zaghi et al. (2023)](/sources/zaghi-2023.md),
  §3.2).
* Cholla strong scaling plateaus at about 512 GPUs, $58^3$ cells per GPU
  ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.2).

## GPU against CPU

The sources' speed-ups use different baselines:
* **Node against node**: IDEFIX, a 4-V100 node 19.3× and a 4-MI250X node
  49.6× a 2-socket Cascade Lake node (double precision, 3D Orszag–Tang,
  different sub-domain sizes per worker) ([Lesur et al. (2023)](/sources/lesur-2023.md),
  §5, Table 4); gPLUTO, 4 A100 against two 56-core Xeon 8480+, about 9×
  at near-equal load (double precision) ([Rossazza et al. (2026)](/sources/rossazza-2026.md),
  Table 3); Enzo, one K20 node about 5× its 16 CPU cores
  ([Bryan et al. (2014)](/sources/bryan-2014.md), §12.3).
* **One GPU against one CPU node**: STREAmS, V100 0.3 s against a 48-core
  Skylake node 1.68 s per step, without cost or power normalization
  ([Bernardini et al. (2021)](/sources/bernardini-2021.md), §4.2); K-Athena
  on a Volta about 5× one 20-core Skylake
  ([Stone et al. (2020)](/sources/stone-2020.md), §3.6.2).
* **Unsupported**: GRaM-X's "10 times faster and computational cost 30
  times lesser compared to traditional CPU-based codes" has no CPU
  measurement in the paper ([Shankar et al. (2023)](/sources/shankar-2023.md),
  §VI).
* **Energy**: IDEFIX, from thermal design power, about $3\times10^{10}$ cells
  per kWh on CPUs and up to $1.8\times10^{11}$ on MI250X nodes, "up to 6
  times" better, at $256^3$ per GPU only ([Lesur et al. (2023)](/sources/lesur-2023.md),
  §5). gPLUTO lowers the GPU clock to save 8% (Orszag–Tang) and 11%
  (Alfvén wave) energy for at most about 6% longer runtime on 8-A100 nodes
  ([Rossazza et al. (2026)](/sources/rossazza-2026.md), §4.3).

## Correctness on GPUs

* Quokka needed `nvcc` `fmad=false` plus symmetric flux summation to keep the
  Liska–Wendroff implosion exactly symmetric, because fused multiply–add
  contraction breaks source-level symmetry
  ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.1.9).
* Cholla's test suite accepts a floating-point difference below $10^{-14}$
  absolute or within 4 ULP, since Sod results differ by about
  $5\times10^{-15}$ across hardware and compilers; its CI tests only the CUDA
  builds and merely compiles the HIP builds
  ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §4.2–§4.3).

# Citations

1. [Bernardini et al. (2021)](/sources/bernardini-2021.md), §§4.1–4.4,
   Tables 1–2, Figs. 11–13.
2. [Jansson et al. (2024)](/sources/jansson-2024.md), §§2.1, 3.1–3.2, 6
   (arXiv preprint 2021).
3. [Lesur et al. (2023)](/sources/lesur-2023.md), §§2.6, 3.1, 3.4, 5,
   Table 4.
4. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §§1, 2.3.1–2.3.3,
   3.2, 4.2–4.3, 5.
5. [Stone et al. (2026)](/sources/stone-2026.md), §§1–2, 5.1, Fig. 20
   (arXiv v1).
6. [Rossazza et al. (2026)](/sources/rossazza-2026.md), §§3.1–3.4, 4.1,
   4.3, 5, Table 3 (arXiv v1).
7. [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §§3.1.9, 4.1–4.2,
   Table 4 (arXiv v2).
8. [Shankar et al. (2023)](/sources/shankar-2023.md), §§II C, III, III A,
   III C, V A–V C, VI (arXiv v2).
9. [Zaghi et al. (2023)](/sources/zaghi-2023.md), §§2.1–2.2, 3.2, Table 1.
10. [Zhang, Schive & Chiueh (2018)](/sources/zhang-2018.md), §§4, 6.
11. [Bryan et al. (2014)](/sources/bryan-2014.md), §12.3.
12. [Stone et al. (2020)](/sources/stone-2020.md), §§1, 3.6.2, 3.6.5.
