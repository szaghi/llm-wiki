---
type: Software
title: "Neko (portable spectral-element framework for incompressible flow)"
description: "Object-oriented Fortran 2008 matrix-free spectral-element framework for incompressible flow, built on the numerical methods of Nek5000, that reaches CPUs, vector engines, GPUs and FPGAs through backend-specific extensions of abstract Fortran types instead of an external portability library; described here from the 2021 preprint."
status: established
aliases: [Neko, libneko]
tags: [software, gpu, performance-portability, performance, scaling, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Neko

Neko is a high-order spectral-element (SEM) framework for incompressible
flow on hexahedral meshes, presented by
[Jansson et al. (2024)](/sources/jansson-2024.md). **Everything on this page
comes from the 2021 arXiv preprint (arXiv:2107.01243v1)**; the published
Computers & Fluids version (2024) was not read; Crossref records 71
references for it against 65 printed in the preprint, and the preprint has no
GPU scaling runs. The preprint describes "a pre-release of Neko" (§5) and prints
no repository URL.

Neko is incompressible and has no shock capturing, Riemann solver, mesh
refinement or astrophysical physics. It is in the bundle as a
performance-portable framework whose portability design is an explicit
alternative to Kokkos-type layers.

## Design

From [Jansson et al. (2024)](/sources/jansson-2024.md), §3 and Table 1:
* Object-oriented Fortran 2008, dynamic memory, polynomial degree chosen at
  run time, a unified mesh format, variable precision support, run-time
  choice of solvers, "only standard library dependencies", support for
  several compilers, and a native gather–scatter. Table 1 contrasts this with
  Nek5000 (Fortran 77, static memory) and NekRS (OCCA with just-in-time
  compilation, gslib, no variable precision).
* **Usage**: a generic solver binary driven by a mesh and an input deck (no
  recompilation per case), built on the library `libneko`; user callbacks
  through a build script; or direct use of `libneko` to write another SEM
  solver (§3).
* **Abstraction layer** (§3.1, Listing 1, Fig. 1). Abstract types wrap
  large compute kernels: `ax_t` (action of the stiffness matrix), `gs_t`
  (gather–scatter), `solver_t` (time step). Each backend is an extended
  derived type (`ax_cpu_t`, `ax_sx_t`, `ax_gpu_t`, and likewise for `gs_t`),
  "all interchangable at runtime", covering both native execution (NEC
  SX-Aurora vector engine) and offload (GPU, FPGA). The types are
  instantiated once at the top of the solver stack, "thus reducing overhead
  costs associated with the abstraction layer". All platform-specific code,
  including device allocation and host–device transfers, lives inside the
  derived type (§6).
* **Position on portability libraries** (§1, §2.1). The authors argue that
  Kokkos, OCCA, OP2 and OPS force deep integration, specific data types or
  mixed-language code and tie the code's longevity to the library, and that
  the offload model does not fit native-mode accelerators. Kernels may be
  tuned in a framework such as DaCe and then added back, removing the
  dependency. An OpenACC port of Nek5000 is called inflexible and catering
  only to NVIDIA GPUs. See [GPU porting](/methods/gpu-porting.md).

## Numerical method

From [Jansson et al. (2024)](/sources/jansson-2024.md), §2 and §4, in words
(the SEM symbols are not in the bundle's registry):
* Matrix-free SEM on hexahedra with tensor-product Gauss–Lobatto–Legendre
  Lagrange bases; the global operator is applied as the gather–scatter of a
  block-diagonal unassembled element operator, never forming the assembly
  matrices (eqs. 4–10).
* Incompressible Navier–Stokes in the PN–PN splitting formulation, with
  backward differentiation of order $k$ for the implicit terms and $k$-th
  order extrapolation of advection and forcing, giving a pressure Poisson
  equation and one Helmholtz equation per velocity component (§4; the
  printed signs are recorded on the [Source page](/sources/jansson-2024.md)).
* Velocity: conjugate gradients with block-Jacobi preconditioning. Pressure:
  GMRES with a two-level additive overlapping Schwarz preconditioner, a
  coarse problem on linear elements solved approximately with about 10 CG
  iterations, and residual projection onto previous solutions (projection
  space 20, Table 2).
* **Overlapped gather–scatter** (§3.2, Algorithm 1). Elements are split into
  local and shared; receives are posted first, shared values gathered and
  sent, local values gathered and scattered during communication, and shared
  values scattered last. Shared global ids are split into non-injective
  (corners, edges) and injective (face and edge interiors) sets, the latter
  as contiguous sorted tuples suited to wide vector registers.

## Performance and portability

Hardware and baselines are as printed; see
[parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).
* **Kernel portability** (§6, Fig. 2). The Poisson `ax_t` kernel (ten
  quadrature points per direction, 128–8192 elements) runs on an NVIDIA A100
  (GNU 10.2.0, CUDA 11.1), an AMD MI100 (CCE 11.0.2, ROCm 4.1.0), a NEC
  SX-Aurora (native), an Intel Stratix 10 FPGA and one 16-core Intel
  E5-2698v3 socket, reaching "more than 10% of theoretical double precision
  peak performance" on most platforms. Values are only plotted. This is a
  kernel benchmark; the preprint has no whole-solver GPU run.
* **Strong scaling against Nek5000 and NekRS** (§9, Fig. 6). Cray XC40 (two
  16-core E5-2698v3 per node), double precision, average wall time per step
  against cores, each code with its own solver options (Table 2). Neko
  matches Nek5000 on CPUs; NekRS is "slightly worse" on the smallest case. No
  speed-up factor is given. Cases: a hemispherical roughness element (2,042
  elements), turbulent pipe flow at friction Reynolds number 180 (36,480
  elements) and a Taylor–Green vortex at Reynolds number 5000 (262,144
  elements, up to 32,768 cores, scaling "down to ≈ 8 elements per PE" for
  Nek5000 and Neko).
* **SX-Aurora** (§9): about 4.3% of peak on 8 cores and 2.1% on 64 for the
  smallest case, about 4% of peak for the Taylor–Green case on the whole
  64-engine machine (512 cores). The coarse-grid solve drops the average
  vector length below 100 of 256.
* **Performance model** (§8, eqs. 12–15). Time per step is modelled as an
  arithmetic part, a roofline per kernel (the larger of flops over peak and
  mandatory memory traffic over STREAM-triad bandwidth), plus a
  communication part from a latency–bandwidth (postal) model for
  `MPI_Allreduce` and gather–scatter, with latencies sampled from more than
  10,000 measured ping-pongs. On the XC40 the model is within 5% for the
  large Taylor–Green case at more than 128,000 points per core (effective
  bandwidth 84 against 90 GB/s triad), within 20% elsewhere, and overestimates the time
  by a factor 2 for the smallest case, whose working set fits in cache (§9.1,
  Fig. 7).
* **Strong-scaling limit** (§10). The limit is reached where arithmetic and
  communication time are equal, the latter dominated by allreduce latency
  because CG is the coarse solver; the authors argue that the relevant
  strong-scaling indicator is the work per process divided by the memory
  bandwidth, not the work per process alone. Projections to A64FX and future
  machines (about 12× to 28.77× faster) are model output, not measurements
  (§10, Fig. 8).

## Verification

* Taylor–Green vortex at Reynolds number 1600 (§7, Figs. 4–5): $64^3$
  elements of degree 7, $\Delta t = 5\times10^{-4}$, maximum Courant number
  $\nu = 0.20$; enstrophy against a $512^3$ dealiased pseudo-spectral DNS.
  Neko, Nek5000 and NekRS are all within 0.25% of the DNS enstrophy and agree
  with each other to $10^{-6}$ (Neko against Nek5000: of order $10^{-11}$).
  The printed initial condition has a typo (the second velocity component
  equals the first), recorded on the [Source page](/sources/jansson-2024.md).
* No convergence-order study; verification is code-to-code and against DNS
  at one resolution.

# Citations

1. [Jansson et al. (2024)](/sources/jansson-2024.md), §§1–10, eqs. 4–15,
   Tables 1–2, Listing 1, Algorithm 1, Figs. 1–8 (arXiv:2107.01243v1, 2021
   preprint of the Computers & Fluids article).
