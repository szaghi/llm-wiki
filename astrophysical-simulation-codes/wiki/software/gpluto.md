---
type: Software
title: "gPLUTO"
description: "Complete C++ rewrite of the PLUTO MHD code that runs the whole time step on NVIDIA GPUs through OpenACC, described so far for ideal MHD on uniform Cartesian grids (SSP-RK3, WENOZ or parabolic reconstruction, HLLD, upwind constrained transport or GLM cleaning), with weak and strong scaling to 256–512 nodes and a GPU-frequency energy study."
status: established
aliases: [gPLUTO, PLUTO GPU, PLUTO on GPUs]
tags: [software, mhd, gpu, openacc, constrained-transport, divergence-cleaning, time-integration, riemann-solver, performance, scaling]
timestamp: 2026-10-12T00:00:00Z
---

# gPLUTO

gPLUTO is "a complete C++ rewrite of the legacy code"
[PLUTO](/software/pluto.md) that runs on NVIDIA GPUs through OpenACC
directives ([Rossazza et al. (2026)](/sources/rossazza-2026.md), abstract,
§1). The first paper covers only the classical ideal-MHD, uniform-mesh,
finite-volume path; adaptive mesh refinement, relativistic and non-ideal
physics, particles and non-Cartesian coordinates are deferred to a
forthcoming paper, and Lagrangian particles to a companion paper (§1, §5).

## Code

* Language C++, chosen for function templates, classes and polymorphism
  (§1). OpenACC was chosen as simpler and higher-level than CUDA, and for
  "interchangeability": the same source compiles and runs on CPUs with the
  directives ignored (§3.1). OpenMP for AMD systems is future work (§5).
* No repository URL, version or compiler is printed; the build flag
  `-gpu=managed` is named (§3.3).
* The legacy code's language is not stated.

## Equations and numerics

From [Rossazza et al. (2026)](/sources/rossazza-2026.md), §2:
* Ideal MHD in conservation form, $\partial_t u + \nabla\cdot\mathbf f(u) = s(u)$
  (eqs. 1–2), with $P^* = p + \tfrac12|\mathbf B|^2$ and
  $E = \frac{p}{\gamma-1} + \tfrac12\rho|\mathbf v|^2 + \tfrac12|\mathbf B|^2$
  (eq. 3); the pressure is recovered in closed form from $E$ (eq. 7).
* Finite-volume semi-discretization advanced by the SSP-RK3 method of lines
  (eq. 5), written here with the registry's $\mathcal L$:
  $$\begin{aligned}
  u^{*} &= u^n + \Delta t\,\mathcal L(u^n),\\
  u^{**} &= \tfrac14\left(3u^n + u^{*} + \Delta t\,\mathcal L(u^{*})\right),\\
  u^{n+1} &= \tfrac13\left(u^n + 2u^{**} + 2\Delta t\,\mathcal L(u^{**})\right).
  \end{aligned}$$
  This is the standard Shu–Osher form; the paper's eq. 5 prints the last
  stage without the factor 2 on the operator term, a misprint recorded on
  the Source page. The paper's operator already contains the factor
  $\Delta t$ (see the Source page). See
  [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md).
* Reconstruction of primitive variables (eq. 6): parabolic or WENOZ (§2.2).
  The generic upwind flux is the mean of the left and right physical
  fluxes minus half a dissipation matrix times the jump
  $u^+_{i+1/2} - u^-_{i+1/2}$ (eq. 8); all runs use HLLD (§4.1). See
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
* Divergence control: Powell's eight-wave method, divergence cleaning and
  constrained transport "in the more recent formulation by" Mignone & Del
  Zanna (2021) (§2.1). The weak-scaling runs use upwind CT (UCT-HLLD); the
  strong-scaling runs use [GLM cleaning](/methods/glm-divergence-cleaning.md)
  "because this algorithm requires less device memory than the constrained
  transport method", which allows a slightly larger grid; no memory
  figures are given (§4.1). See
  [constrained transport](/methods/constrained-transport.md).
* Uniform Cartesian mesh; no adaptive mesh refinement in this paper (§2.2).
  No CFL number is printed.

## GPU implementation

From [Rossazza et al. (2026)](/sources/rossazza-2026.md), §3; see
[GPU porting](/methods/gpu-porting.md):
* **Device residency.** "The entire computational workload is handled by
  the GPUs"; the CPU runs the operating system, manages system memory and
  does I/O, so no host–device transfers are needed during computation
  (§3.1).
* **Kernels.** `parallel loop collapse(3) present(...)` over the three cell
  indices; the inner loop over the conserved variables is sequential,
  because parallelizing it "usually tends to lower the performance"
  (Fig. 1, §3.2).
* **Memory.** CUDA Unified Memory (`-gpu=managed`) combined with explicit
  `enter data copyin` / `exit data delete` directives "to ensure correct
  deep copying of structured and nested data" (§3.3).
* **Data layout.** Pointer-to-pointer arrays were replaced by flat arrays
  wrapped in `Ary` classes that hide index arithmetic; the cell-centred
  arrays have the $x$ index fastest and the variable index slowest, so
  consecutive threads touch adjacent addresses (coalesced access).
  Directional sweep buffers are viewed as per-row 2D slices and reordered
  for the $y$ sweep to keep access coalesced (Fig. 2).
* **Templates.** Kernels whose indexing depends on the sweep direction,
  including the Riemann solver, are templated on the direction so that small
  local arrays live in registers (Fig. 3).
* **MPI.** Legacy PLUTO's ArrayLib exchange is replaced by plain buffers
  and non-blocking point-to-point messages with up to 8 (2D) or 26 (3D,
  diagonals included) neighbours. Send buffers are packed on the device by
  two kernels on separate `async` queues, receives are unpacked likewise,
  and buffers are allocated in device memory with `acc_malloc` (Fig. 4,
  §3.4). Whether the MPI library is CUDA-aware is not stated.

## Performance

From [Rossazza et al. (2026)](/sources/rossazza-2026.md), §4, all FP64,
HLLD + WENOZ + SSP-RK3; metrics as in
[cell-update throughput](/definitions/cell-updates-per-second.md) and
[parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).
Machines (Table 1): MareNostrum 5 ACC (4 NVIDIA Hopper GPUs of 64 GB per
node), Leonardo Booster (4 A100 per node), MeluXina (4 A100 of 40 GB per
node), Leonardo DCGP (CPU, 112 Xeon 8480+ cores per node).
* **Weak scaling, 3D Orszag–Tang, upwind CT** (§4.1, Fig. 5, Table 2).
  Per-node grids $704\times704\times352$ (Booster, MareNostrum 5),
  $704\times704\times350$ (DCGP), $512^3$ (MeluXina). Efficiency is the
  wall-clock time on one node over that on the larger node count: MareNostrum 5 above
  95 % at 256 nodes; Leonardo Booster 88 % at 512 nodes (2048 GPUs);
  MeluXina 91 % at 32 nodes; Leonardo DCGP above 95 % to 64 nodes and 84 %
  at 128 nodes, unexplained by the authors.
* **Throughput** (Fig. 6), in cells updated per second per node; no values
  are printed. Read from the log-scale figure: about $1.5\times10^8$
  (MareNostrum 5), about $1.1\times10^8$ (Leonardo Booster, MeluXina), about
  $1.2\times10^7$ (Leonardo DCGP), roughly flat to 512 nodes.
* **GPU node against CPU node** (Table 3), Leonardo, Orszag–Tang weak
  scaling: 312–335 s on 4 A100 against 2885–3430.8 s on 112 CPU cores, at
  nearly equal cells per node; acceleration 9.24 (1 node), 9.12, 9.14, 8.98,
  9.11, 9.14, 9.02 and 10.24 (128 nodes), summarized as "a factor ≈ 9
  acceleration (per node usage)" (§5). The baseline is node against node,
  not normalized by cost or power; the CPU build (compiler, vectorization,
  whether it is the same source without OpenACC) is not stated; the 10.24
  reflects the CPU efficiency drop at 128 nodes.
* **Strong scaling, 3D Orszag–Tang, GLM** (§4.1, Fig. 7, Table 4). Six
  groups of four runs, each spanning an 8-fold increase in nodes from a base
  grid that nearly fills GPU memory ($832\times832\times416$ on 1 node to
  $3328\times1664\times1664$ on 32 nodes). Efficiency is the measured
  speed-up over the ideal. Mean at the largest node count of each group:
  0.90 (MareNostrum 5), 0.89 (Leonardo). Worst entries: 0.77 at 256 nodes
  and 0.83 at 16 nodes (MareNostrum 5), 0.86 at 32 nodes (Leonardo).
* **3D circularly polarized Alfvén wave** (§4.2, Figs. 8–9, Table 5),
  Leonardo Booster and MareNostrum 5 only. Weak scaling with CT: 0.97 at
  256 nodes (1024 GPUs) on Leonardo, 0.95 on MareNostrum 5. Strong scaling
  with GLM: the text gives average efficiencies 0.97 (Leonardo) and 0.93
  (MareNostrum 5), which Table 5 does not reproduce under the Table 4 rule
  (see the Source page); MareNostrum 5 loses most at the last doubling of
  each group (0.77–0.87).
* **Energy** (§4.3, Table 6, Figs. 10–12). Karolina GPU nodes (2 AMD EPYC
  7763, 8 A100-SXM4), GPU power from NVML, CPU power from RAPL, the rest of
  the node modelled (static 1120 W). Lowering the SM clock from 1410 to
  990 MHz, or strong scaling from 1 to 32 nodes, cuts GPU power per node from
  2.0 to 1.2 kW, and both together to 0.8 kW. Accepting at most about 6 %
  longer runtime, the energy saving is up to 8 % (Orszag–Tang, 1290 MHz) and
  11 % (Alfvén wave, 1230 MHz). The largest savings, at 1050–1110 MHz, are
  not at the lowest clock, because static power times the longer runtime
  dominates; savings shrink with node count. Energy efficiency is defined
  as FLOPS per watt, but no FLOP counts are reported.

## Verification

None. The paper runs the [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
(a 3D variant) and the
[circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
only as scaling workloads: no solution plots, error norms, convergence
orders or $\nabla\cdot\mathbf B$ diagnostics are shown, although §1 claims
the tests highlight "the code's effectiveness in reproducing them"
([Rossazza et al. (2026)](/sources/rossazza-2026.md), §1, §4).

# Citations

1. [Rossazza et al. (2026)](/sources/rossazza-2026.md), §§1–5, Tables 1–6, Figs. 1–12 (arXiv v1).
