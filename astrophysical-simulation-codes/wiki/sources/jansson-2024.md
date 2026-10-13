---
type: Source
title: "Jansson et al. (2024) — Neko: A modern, portable, and scalable framework for high-fidelity computational fluid dynamics"
description: "Presents Neko, an object-oriented Fortran 2008 matrix-free spectral-element framework for incompressible flow that reaches CPUs, vector engines, GPUs and FPGAs through backend-specific extensions of abstract Fortran types, matches Nek5000 and NekRS on a Cray XC40 and in a Taylor–Green DNS, and models its own strong-scaling limit with a roofline-plus-postal performance model; read as the 2021 arXiv preprint."
resource: "doi:10.1016/j.compfluid.2024.106243"
source_kind: paper
authors: [Jansson N., Karp M., Podobas A., Markidis S., Schlatter P.]
year: 2024
venue: "Comput. Fluids 275:106243"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2024-CompFluids-Jansson-101016jcompfluid2024106243.pdf"
tags: [software, gpu, performance-portability, performance, scaling, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

**The text read is the arXiv preprint 2107.01243v1 (2 July 2021), not the
Computers & Fluids article of 2024**, although the archive file is named after
the published DOI. The work is the same (same title and five authors), but
the published version is substantially revised (71 references against 65;
the preprint has no GPU scaling runs). Everything on this page and on
[Neko](/software/neko.md) is the preprint's content.

Neko is a portable, matrix-free, high-order spectral-element framework for
incompressible flow on hexahedral meshes, written in object-oriented Fortran
2008 on the numerical methods of Nek5000 (PN–PN splitting, BDF/extrapolation
IMEX, Schwarz-preconditioned Krylov solvers). Its portability device is not an
external layer (Kokkos, OCCA, OP2/OPS, DSLs, argued against in §2.1) but
application-specific abstract types whose deferred procedures are implemented
per backend (CPU, NEC SX-Aurora, GPU, FPGA) and selected at run time (§3.1). A
native gather–scatter overlaps MPI with local work (§3.2). On a Cray XC40 Neko
matches Nek5000 and NekRS in time per step on three strong-scaling cases and
matches the Taylor–Green DNS enstrophy within 0.25% (§7, §9). A roofline plus
postal performance model of the whole solver is validated within 5% on the
large case and used for projections (§8–§10). Merged into
[Neko](/software/neko.md), [GPU porting](/methods/gpu-porting.md),
[cell-update throughput](/definitions/cell-updates-per-second.md) and
[parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).

# Key claims

1. **Design** (§3, Table 1). Fortran 2008, object-oriented, dynamic memory,
   run-time polynomial degree, unified mesh format, multi-backend, "only
   standard library dependencies", variable precision, run-time solver choice,
   multi-compiler, native gather–scatter; contrasted with Nek5000 and NekRS.
2. **Usage** (§3). A generic binary driven by mesh and input deck, built on
   `libneko`; user callbacks through a build script; or direct use of the
   library.
3. **Abstraction layer** (§3.1, Listing 1, Fig. 1). Abstract `ax_t`, `gs_t`,
   `solver_t` with backend extensions (`ax_cpu_t`, `ax_sx_t`, `ax_gpu_t`, …),
   "all interchangable at runtime", instantiated once at the top of the solver
   stack to cut abstraction overhead; device allocation and transfers stay
   inside the derived type (§6).
4. **Programming-model position** (§1, §2.1). Abstraction libraries force
   deep integration and tie longevity to the library; offload does not fit
   native-mode accelerators; kernels may be tuned in DaCe and added back. An
   OpenACC Nek5000 port is called inflexible and NVIDIA-only.
5. **Matrix-free SEM** (§2, eqs. 4–10). Local stiffness operators combined
   through the gather–scatter, assembly matrices never formed.
6. **Overlapped gather–scatter** (§3.2, Algorithm 1). Receives posted first;
   shared values sent; local values gathered and scattered during
   communication; shared values scattered last. Non-injective ids in
   variable-length blocks; injective ids as contiguous sorted tuples for
   vector registers.
7. **Numerical method** (§4). PN–PN, BDF of order $k$ with $k$-th order
   extrapolation, pressure Poisson and per-component Helmholtz equations; CG
   with block-Jacobi for velocity; GMRES with two-level additive overlapping
   Schwarz for pressure, coarse problem by about 10 CG iterations; residual
   projection.
8. **Solver configuration** (§5, Table 2). Pressure Krylov / coarse solver /
   projection space: Neko GMRES / CG / 20; Nek5000 GMRES / XXT / 8; NekRS
   Flex-CG / HYPRE-AMG / 8; all BDF3, no dealiasing.
9. **Kernel portability** (§6, Fig. 2). The Poisson `ax_t` kernel on A100,
   MI100, SX-Aurora, Stratix 10 FPGA and one E5-2698v3 socket reaches "more
   than 10% of theoretical double precision peak performance" on most
   platforms (plotted only).
10. **Strong scaling** (§9, Fig. 6). Cray XC40, double precision, average
    wall time per step against cores: Neko ≈ Nek5000; NekRS "slightly worse"
    on the smallest case; no speed-up factor.
11. **SX-Aurora** (§9). About 4.3% of peak on 8 cores and 2.1% on 64 (Hemi);
    about 1.1% (pipe); about 4% for the Taylor–Green case on 512 cores; the
    coarse solve drops the average vector length below 100 of 256.
12. **Performance model** (§8, eqs. 12–15). Arithmetic time per kernel = the
    larger of flops over peak and mandatory memory operations over STREAM
    bandwidth; communication by a postal model for allreduce and
    gather–scatter, latencies sampled from more than 10,000 ping-pongs (XC40
    mean 2.6 µs, 99th percentile above 20 µs).
13. **Model validation** (§9.1, Fig. 7). Within 5% for the large Taylor–Green
    case below 2048 cores and above 128,000 points per core (effective 84
    against 90 GB/s triad); within 20% elsewhere; a factor 2 overestimate for
    the smallest case (cache-resident). For the SX-Aurora the model predicts
    about 5× faster than measured (Taylor–Green) and up to 10× (the smaller
    cases).
14. **Scaling limit** (§10). Reached where arithmetic and communication times
    are equal; the authors argue for work per process over bandwidth, not
    work per process, as the strong-scaling indicator.
15. **Projections** (§10, Fig. 8). A64FX about 12× faster; future machines up
    to 28.77×; model output, not measurements.

# Tests

* **Matrix-vector kernel** (§6, Fig. 2): ten quadrature points per direction,
  128–8192 elements, five platforms; compilers GNU 10.2.0/CUDA 11.1 (A100),
  CCE 11.0.2/ROCm 4.1.0 (MI100), Intel OpenCL SDK 20.2 (FPGA).
* **Taylor–Green vortex, Reynolds number 1600** (§7, eq. 11, Figs. 4–5): cube
  of side $2\pi$, periodic; $\Delta t = 5\times10^{-4}$, maximum Courant number
  0.20; $64^3$ elements of degree 7; reference $512^3$ dealiased
  pseudo-spectral DNS. All three SEM codes within 0.25% of the DNS enstrophy,
  mutually within $10^{-6}$ (Neko against Nek5000 of order $10^{-11}$); the
  plotted relative error peaks near $2\times10^{-3}$ around $t\approx17$.
* **Hemispherical roughness element** (§9): 2,042 elements, 10 points per
  direction, $\Delta t = 10^{-3}$; 1–4 XC40 nodes, 1–8 vector engines;
  scalability lost quickly in all codes.
* **Turbulent pipe flow**, friction Reynolds number 180 (§9): 36,480 elements,
  8 points per direction; all codes scale further; Nek5000 scales well "even
  for few elements per core in contrast to previously published results".
* **Taylor–Green vortex, Reynolds number 5000** (§9, Figs. 3, 6c, 7c):
  262,144 elements, 10 points per direction; up to 32,768 XC40 cores and 512
  vector-engine cores; NekRS does not fit below 1024 cores and diverged at
  16,384 (dashed); Nek5000 and Neko scale "down to ≈ 8 elements per PE".

No convergence-order test; verification is code-to-code and against DNS at
one resolution.

# Notation map

| Jansson et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$ (velocity) | $\mathbf v$ | **collision:** registry $u$ is the conserved state |
| $p$ | $p$ | kinematic pressure (incompressible) |
| $f$ (volume force) | words | **collision:** registry $f$ is the physical flux |
| $Re$, $Re_\delta$, $Re_\tau$ | words | Reynolds numbers |
| $\nu$ (kinematic viscosity) | words | **collision:** registry $\nu$ is the Courant number |
| CFL (0.20) | $\nu$ | |
| $dt$ | $\Delta t$ | |
| $n$ (time level) | $t^n$ | same |
| $N$ (polynomial degree) | words | **collision:** registry $N$ is cells per dimension |
| $E$ (number of elements) | words | **collision:** registry $E$ is the total energy density |
| $n = EN^3$, $n_p = E(N+1)^3$ | words | **collision** with the time level $n$ |
| $A$, $A^e$, $A_L$ | words (stiffness operators) | **collision:** registry $A(u)$ is the flux Jacobian |
| $Q$, $Q^T$ | words (scatter, gather) | also collides with the paper's $Q$ = loads + stores |
| $D$, $G^e$ | words | derivative and geometric-factor tensors |
| $b_j$, $a_j$, $k$ | words | BDF/extrapolation coefficients and order |
| $\omega$, $\mathcal E(\omega)$ | words (vorticity, enstrophy) | **collision:** registry $\boldsymbol{\mathcal E}$ is the EMF |
| $T$, $T_a$, $T_c$ | words | **collision:** registry $T$ is the temperature |
| $W$, $Q$ (flops, memory operations) | words | **collision:** registry $W$ is the Lorentz factor |
| $\pi$, $\beta$ | words (peak, memory bandwidth) | **collision:** $\beta^i$ is the shift |
| $\alpha^*$, $\beta^*$ | words (latency, inverse bandwidth) | |
| $P$ | words (number of processes) | avoids confusion with $p$, $P^*$ |
| $m$ | words (projection-space size) | **collision:** registry $m$ is the system size |

# Pages created or updated

* Created [Neko](/software/neko.md).
* Cited on [Porting compressible-flow codes to GPUs](/methods/gpu-porting.md),
  [Cell-update throughput](/definitions/cell-updates-per-second.md),
  [Parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2024-CompFluids-Jansson-101016jcompfluid2024106243.pdf`.
   * **Version.** arXiv preprint 2107.01243v1, submitted 2 July 2021, the
     only arXiv version; 13 pages, ACM conference template, no journal header.
     It is **not** the Computers & Fluids text. The preprint describes "a
     pre-release of Neko" (§5) and prints no repository URL; Nek5000 v19.0 and
     NekRS v20.1 (cloned 9 March 2021) were used for comparison.
   * **Identity.** doi:10.1016/j.compfluid.2024.106243, checked on Crossref:
     "Neko: A modern, portable, and scalable framework for high-fidelity
     computational fluid dynamics", Comput. Fluids 275, article 106243, issued
     May 2024; the same five authors; 71 references. Title and authors match
     the preprint's page 1.
   * **How it was read.** Text extraction; page 7 has no text layer and was
     read visually (Fig. 3 caption, end of §7, start of §8, Figs. 4–5); the
     §4 time-integration equations and eqs. 14–15 from rendered pages 5 and
     8; eq. 11 checked on page 6. Values of Figs. 2 and 6–8 are not stated in
     the text and are not reproduced.
   * **Recorded as printed.**
     - Eq. 11 (Taylor–Green initial condition): the second velocity component
       is printed $\sin(x)\cos(y)\cos(z)$, identical to the first; the
       standard field has $-\cos(x)\sin(y)\cos(z)$, and the printed one is not
       divergence-free.
     - §4: the extrapolated advection term appears with a $+$ sign on the
       right-hand side of the Helmholtz equation; the sign convention of the
       extrapolation coefficients is not stated.
     - The published version (71 references) was not read; any GPU scaling,
       newer features or revised numbers in it are absent here.
   * **Reference list:** 65 entries in the preprint (the published article
     has 71). [48] prints its author list garbled ("James W. Lottes Paul F.
     Fischer and Stefan G. Kerkemeier"), keyed `fischer-2008-b` after [17]
     `fischer-2008`; [58] prints the first author's surname only
     (Świrydowicz); [9] keyed `jacobs-2017`; same-author-year pairs
     `hoefler-2010`/`-b` and `tufo-1999`/`-b`. No DOIs printed; none added.
