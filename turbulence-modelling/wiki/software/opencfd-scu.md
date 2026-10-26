---
type: Software
title: "OpenCFD-SCU"
description: "OpenCFD-SCU is an open-source CUDA-C/HIP finite-difference code for DNS of compressible wall-bounded turbulence, ported from the CPU code OpenCFD-SC; this page records its numerics, parallel and GPU design, reported performance and its 31-billion-point compression-ramp DNS."
status: established
aliases: [OpenCFD-SC, OpenCFD SCU]
tags: [software, dns, gpu, compressible, boundary-layer]
timestamp: 2026-10-26T05:06:00Z
---

# OpenCFD-SCU

**OpenCFD-SCU** is an open-source finite-difference solver for
[direct numerical simulation](/definitions/direct-numerical-simulation.md)
of compressible wall-bounded turbulence on graphics processing units,
presented by [Dang et al. (2022)](/sources/dang-2022.md). It was ported from
the Fortran CPU code OpenCFD-SC (written by Li) to CUDA-C, and translated to
HIP with AMD's HIPIFY so that the same source runs on NVIDIA and AMD GPUs;
CUDA Fortran was abandoned because HIPIFY does not handle it, and API calls
without an exact HIP counterpart are avoided (§4.1). It computes in double
precision, the GPU doing essentially all floating-point work and the CPU
only control and communication (§3). The version read is an author
manuscript titled "Part 1"; the companion "Part 2" it cites is not in its
reference list.

## Numerics

As described by Dang et al. (2022, §2):

- Three-dimensional compressible Navier–Stokes equations in curvilinear
  coordinates on a single-block grid, non-dimensionalized by reference
  length, velocity, density and temperature; Sutherland viscosity; typically
  $\gamma=1.4$, $Pr=0.7$.
- Convective terms: Steger–Warming flux-vector splitting, optional
  characteristic-variable reconstruction, and a library of upwind schemes
  (second-order NND, fifth- and seventh-order WENO, sixth-order OMP6,
  seventh-order WENO-SYMBO, seventh-order linear upwind), plus a hybrid of
  the last three switched by a modified Jameson pressure sensor; the schemes
  and the hybrid are on [WENO and hybrid schemes](/methods/weno-scheme.md).
  Near non-periodic boundaries fifth-order WENO with outside sub-stencils
  given zero weight.
- Viscous terms: sixth- or eighth-order central differences, reduced to
  second-, fourth- and sixth-order central and a one-sided second-order
  closure towards non-periodic boundaries.
- Time: three-stage third-order Runge–Kutta.

## Parallel and GPU design

- **Decomposition.** Three-dimensional MPI decomposition with a halo of four
  points (the widest scheme is seventh order); each subdomain is split into
  an interior and an outer zone so that interior computation overlaps the
  halo exchange on four CUDA streams (inviscid and viscous terms, interior
  and outer). Halo data travel GPU→CPU→MPI→CPU→GPU (no GPU-direct), in packed
  buffers and pinned host memory; four streams cut one Runge–Kutta step from
  291 ms to 265 ms (§3.2–3.3, §4.3.5–4.3.6, Fig. 15).
- **I/O.** MPI-IO with per-line collective reads; a field of "tens of
  billions" of points is read "in just ten minutes" (§3.4).
- **Kernels.** One thread per grid point in $8\times8\times8$ or
  $8\times8\times4$ blocks (the AMD warp has 64 threads); coalesced, aligned
  access; warp shuffle of neighbouring fluxes (double precision shuffled as
  two halves, which the MI60 requires) with redundant computation at block
  edges instead of inter-block exchange; shared-memory transposes for the
  $y$ and $z$ directions; atomic adds to merge contributions computed on
  different streams; fused kernels and division hoisting. The inviscid upwind
  difference takes 70% of the run time and the code is memory-bound
  (§4.2–4.3, Figs. 10, 12, 14). Kernel performance "is more than doubled"
  by the optimizations (§4).

## Reported performance

| Quantity | Value | Locator |
|---|---|---|
| CPU/GPU consistency | flat plate, $250\times240\times90$ points, 1000 steps, output to nine decimals: 56 of 5.4 million lines differ, by sign only | §5.1 |
| Speed-up over OpenCFD-SC | "more than 200", "200–500 times" at the same number of MPI processes | Abstract, §5, Fig. 19 |
| GPU against CPU count | 512 GPUs at 0.1387 s/step faster than 131,712 CPU processes at 0.39 s/step | §5.2, Table 5 |
| Weak scaling | $280^3$ points per GPU, 1 to 24,576 GPUs (more than 500 billion points), 98.7% efficiency | §5.3, Fig. 20 |
| Strong scaling | "60% parallel efficiency" over a 16-fold increase (128 to 2048 processes, 0.5174 to 0.0627 s/step) | §5, Table 5 |
| Throughput | 705.4 GFLOPS per GPU estimated from hand operation counts; 17.1 PFLOPS at full scale, 11.4% of peak | §5.4, Table 6, Fig. 21 |
| Single GPU, $200^3$ | V100 4.702 s, RTX 3090 4.038 s, A100 3.036 s, MI60 0.315 s per step | §5.5, Table 7 |

The authors attribute the tenfold lead of the AMD MI60 over the A100 to
optimizations targeted at the AMD warp and shared memory (§5.5). The
speed-up figures are taken at equal MPI process count, and the code runs
one process per GPU (§5.3), so they compare one GPU with one CPU process.
The conclusion that the code "saves up to 90% of the computational cost"
(§7) is stated without a cost computation.

## Validation and application

The test case is the Mach 2.9, 24° compression ramp of Wu & Martín and the
Bookey et al. experiment (see [shock/turbulent-boundary-layer
interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).
On $16100\times240\times200$ points, with WENO-SYMBO and eighth-order
viscous terms and an inflow made turbulent by wall blowing and suction
instead of recycling, the mean wall pressure and the van Driest-transformed
mean velocity agree with the DNS of Martín et al. and the experiment (§5.1,
Figs. 16–18). A wide-span run on $16250\times240\times8000$ points (31.2
billion), more than 29 boundary-layer thicknesses wide, with
$\Delta x^+=1.2$, $\Delta y^+=0.41$, $\Delta z^+=1.2$ at the reference
station 35 mm upstream of the corner, shows Taylor–Görtler vortices behind
the separation shock (§6.1, Figs. 22–25; qualitative).

## Qualifications

Printed inconsistencies in the version read (author manuscript):

- The GPU count is printed 24,567 in §1 and §5.4 and 24,576 elsewhere.
- Table 6 prints a total of $5.5726\times10^{12}$ operations; its rows sum to
  $5.5726\times10^{11}$, and the printed 705.4 GFLOPS corresponds to
  $5.5726\times10^{11}$ operations in 0.79 s, not to the printed 792 ms
  (which gives 703.6 GFLOPS) *(compiler check, not in the sources)*.
- The weak-scaling times printed in §5.3, 0.791 s/step on one GPU and 0.78
  s/step on 24,576, would give an efficiency above one, not 98.7%; Table 5
  gives a strong-scaling efficiency of $0.5174/(16\times0.0627)\approx52\%$,
  not 60% *(compiler check, not in the sources)*.
- Table 5 has no process count common to the CPU and GPU codes, so the
  "same number of MPI processes" speed-up cannot be read from it; Fig. 19
  uses the smallest CPU run as base.
- The MI60 is printed "M160" in several places; Eq. (12) prints
  $\partial T/\partial x$ in all three heat-flux terms; Eq. (13) prints the
  off-diagonal stress with $\partial u_j/\partial x_j$ in place of
  $\partial u_i/\partial x_j$; Eq. (15) and Eq. (16) give one symbol $C$ two
  meanings (Sutherland constant and non-dimensional sound speed).

# Citations

- [Dang et al. (2022)](/sources/dang-2022.md) — §1; §2, Eqs. (1)–(45) (equations and numerics); §3–§4, Figs. 3–15 (parallel and GPU design); §5, Tables 5–7, Figs. 16–21 (validation, performance); §6.1, Figs. 22–25 (wide-span ramp); §7.
