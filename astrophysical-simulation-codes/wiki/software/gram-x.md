---
type: Software
title: "GRaM-X"
description: "GPU-accelerated dynamical-spacetime GRMHD code for the Einstein Toolkit: Z4c spacetime on vertices and Valencia GRMHD on cells, TVD or WENO5 reconstruction with HLLE fluxes, a 3D Newton–Raphson / Newman / temperature-bisection primitive-recovery chain, tabulated nuclear EOS in unified memory, and block-structured AMR without subcycling through the CarpetX driver on AMReX, with all data kept on the GPU."
status: established
aliases: [GRaM-X, General Relativistic accelerated Magnetohydrodynamics on AMReX, CarpetX]
tags: [software, mhd, relativity, gpu, amr, primitive-recovery, equation-of-state, riemann-solver, time-integration, performance, scaling, verification, cuda]
timestamp: 2026-10-12T00:00:00Z
---

# GRaM-X

GRaM-X (General Relativistic accelerated Magnetohydrodynamics on AMReX) is
a dynamical-spacetime general-relativistic MHD code for the Einstein
Toolkit. It is a redesign of GRHydro written "from scratch in C++", with
reconstruction and Riemann solver "adapted from" GRHydro, and runs on CPUs
and GPUs through the Cactus driver CarpetX, which delegates block-structured
AMR, GPU kernel launches, MPI and OpenMP to AMReX
([Shankar et al. (2023)](/sources/shankar-2023.md), abstract, §I, §III,
§VI).

## Code

* An Einstein Toolkit thorn on the Cactus framework (flesh plus thorns,
  scheduling by a domain-specific language) with the driver CarpetX,
  developed over "the past 3 years" (§III). No repository URL, version
  number or licence is printed.
* I/O through Silo (3D output for VisIt) and openPMD with an ADIOS2
  back end for checkpoints, stated to be "more efficient than AMReX's built
  in BoxLib output" (§III).
* GPU back ends through AMReX: CUDA, HIP/ROC and DPC++/SYCL; the CPU path
  uses the NSIMD library for SIMD vectorization (§III). A runtime-switchable
  data-validity tracker exists for debugging and is off in production
  (§III).

## Equations

From [Shankar et al. (2023)](/sources/shankar-2023.md), §II A–B (eqs. 1–13).
* **Spacetime**: the Einstein equations in the Z4c formulation, finite
  differences on vertex-centred data, with 1+log slicing and a
  Γ-driver shift; constraint-damping parameters 0.02 and 0.0 (§II A).
  Other thorns see only the ADM variables: $\gamma_{ij}$, extrinsic
  curvature, $\alpha_{\mathrm L}$, $\beta^i$ and their time derivatives.
* **Fluid**: ideal GRMHD in the Valencia flux-conservative form
  $\partial_t u + \nabla\cdot\mathbf f(u) = s(u)$, finite volume on
  cell-centred data, with conserved $D$, $S_i$, $\tau$ and the field
  $\mathbf B$ densitized by the square root of the determinant of
  $\gamma_{ij}$ (eqs. 6–12). The sources contain the stress–energy tensor
  contracted with metric derivatives and Christoffel symbols (eq. 13).
* **Coupling**: the stress–energy tensor needs fluid values at vertices,
  obtained by a fourth-order symmetric 3D interpolation of the cell
  averages; the metric at cell faces is linearly interpolated from vertices
  (§II B, §II C). Second-order interpolation (averaging) gave "even larger,
  unacceptable amplitudes of oscillations" in the star test (§IV D).

## Solvers

From [Shankar et al. (2023)](/sources/shankar-2023.md), §II C.
* **Method of lines**: the right-hand side is primitive recovery, then
  reconstruction, then the Riemann solver, then flux divergence plus
  sources; RK2 or RK4 shared by spacetime and fluid (see
  [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md)).
* **Reconstruction**: TVD minmod, "2nd-order accurate in regions of smooth,
  monotonic flows but reduces to first order" at extrema and shocks, or
  WENO5, the planned production choice; selectable at run time.
* **Riemann solver**: HLLE only (see
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)).
  Roe and Marquina are planned, on the asserted ground that "methods which
  are compute intensive but not memory intensive add little extra cost on
  GPUs" (not measured).
* **Primitive recovery**: a 3D Newton–Raphson in $W$, $\rho h_{\mathrm{rel}}W^2$
  and $T$; on non-convergence the Newman & Hamlin one-dimensional
  iteration; as last resort bisection in temperature, "guaranteed to
  converge ... but much more expensive". Listed failure modes:
  non-convergence, negative density or pressure, speed above $c$, and
  leaving the table bounds in $\rho$, $T$, $Y_{\mathrm e}$. See
  [primitive-variable recovery](/methods/primitive-variable-recovery.md).
* **Equations of state**: polytropic, $\gamma$-law, and a tabulated nuclear
  EOS with 19 quantities in $(\rho, T, Y_{\mathrm e})$ in the
  stellarcollapse.org format; the table is loaded into CUDA unified memory,
  accessible from host and device.
* **Divergence of $\mathbf B$**: AMReX supports cell-, face-, edge- and
  vertex-centred data (one extra point per staggered direction, Fig. 1);
  placing the vector potential on edges keeps $\nabla\cdot\mathbf B$ zero to
  round-off, "in particular near mesh refinement interfaces" (§III B). The
  [constrained transport](/methods/constrained-transport.md) or
  vector-potential algorithm itself (EMF construction, gauge, prolongation)
  is not described, and no divergence measurement is reported. The 1D tests
  run without it; the 2D and 3D tests use it (§IV).

## Adaptive mesh refinement

From [Shankar et al. (2023)](/sources/shankar-2023.md), §III A, §III C; see
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* CarpetX implements Berger–Oliger block-structured AMR over AMReX:
  $r_{\mathrm{ref}} = 2$, proper nesting, ghost zones of a fine level filled
  by prolongation from the coarser level, restriction of covered coarse
  data. Refined regions are made of blocks of run-time size; "typical block
  size would be 8 × 8 × 8 cells" ($N_{\mathrm b} = 8$).
* AMReX's inter-level operators were extended to higher-order templated
  stencils for vertex-centred (spacetime) and conservative cell-centred
  (fluid) data (§III).
* **No subcycling**: one $\Delta t$ on all levels, "for simplicity" and
  because it "increases parallel scalability ... since all refinement levels
  can be evolved simultaneously. Subcycling in time necessarily serializes
  evolving different refinement levels" (§III A). Asserted: every
  performance run is unigrid.
* **Conservation across levels**: face fluxes are synchronized, fine fluxes
  restricted to coarse faces; "As we are using a global time step,
  so-called refluxing is not necessary" (§III C).

## GPU design and parallelism

From [Shankar et al. (2023)](/sources/shankar-2023.md), §III C, §V B; see
[porting compressible-flow codes to GPUs](/methods/gpu-porting.md).
* **Device residency**: "all data are stored on the accelerator's built-in
  memory at all times, and are moved from and to the CPU memory only for
  I/O", so every routine runs on the device; "All of CarpetX's basic
  operations are fully GPU enabled", including gravitational-wave
  extraction (§III). Loop kernels are AMReX lambda launches scheduled as
  tasks, with a barrier before synchronization or I/O. This is the opposite
  of [GAMER](/software/gamer.md)'s host-resident design.
* **CPU threading**: OpenMP tiles, an efficient tile being e.g.
  1000 × 4 × 4 (long in $x$ for cache lines, short in $y$, $z$ because of
  the many variables), scheduled as OpenMP tasks (§III C).
* **MPI** ghost exchange via AMReX. The next kernel starts only after all
  ghost zones of the previous kernel are filled: no compute–communication
  overlap yet, stated as a current limitation (§V B).

## Performance

From [Shankar et al. (2023)](/sources/shankar-2023.md), §V. Metric: zone-cycles
per second, (iterations × cells)/(wall time), per GPU by dividing by the GPU
count; one zone-cycle "includes all intermediate steps for RK2/RK4" (see
[cell-update throughput](/definitions/cell-updates-per-second.md)).
Unigrid, periodic, WENO5, $n_{\mathrm g} = 3$, no output, initial-data time
excluded. Precision is not stated; double precision is only implied by the
argument from FP64 peaks. Set-ups: A = static spacetime, ideal gas, RK2;
B = static spacetime, tabulated EOS, RK4; C = dynamical spacetime, tabulated
EOS, RK4.

* **One GPU** (§V A). NVIDIA V100 (Summit): A $0.44\times10^8$ ($152^3$) and
  $0.47\times10^8$ ($240^3$); B $0.24\times10^8$ and $0.26\times10^8$; C
  $0.062\times10^8$ at $168^3$, the memory maximum (expected about
  $0.1\times10^8$ after optimization). NVIDIA RTX A6000: A $0.090\times10^8$,
  B $0.045\times10^8$, C $0.020\times10^8$. A to B costs about 1.8× (two
  changes at once: tabulated EOS and twice the RK stages); B to C about 4×,
  with register spills in the spacetime solver. The A6000 is 3–6× slower
  than the V100, explained by FP64 peaks of 1.25 against 7.8 TFlop/s.
  Same-code, device-to-device comparison only.
* **H-AMR comparison** (§V A). H-AMR is quoted at "∼ 0.85 × 10⁸
  zone-cycles/s for a similar physics setup" on one Summit V100 and called
  "comparable", although it is about 1.8× GRaM-X's best figure; H-AMR's
  set-up is not specified.
* **Weak scaling** (§V B, Table II, Fig. 7). Summit, 6 V100 per node, 1 to
  2304 nodes (13,824 GPUs). Efficiency is relative to **one node** (6 GPUs),
  not one GPU (see [parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md)):

  | nodes | set-up B, $240^3$ per GPU: zone-cycles/s per GPU | eff. | set-up C, $168^3$ per GPU: zone-cycles/s per GPU | eff. |
  |---|---|---|---|---|
  | 1 | $0.154\times10^8$ | 1.00 | $0.0412\times10^8$ | 1.00 |
  | 36 | $0.066\times10^8$ | 0.43 | $0.0205\times10^8$ | 0.50 |
  | 288 | $0.064\times10^8$ | 0.42 | $0.0207\times10^8$ | 0.50 |
  | 972 | $0.060\times10^8$ | 0.39 | $0.0204\times10^8$ | 0.50 |
  | 2304 | $0.063\times10^8$ | 0.40 | $0.0203\times10^8$ | 0.49 |

  The drop happens between 1 and 36 nodes and is flat after. The one-node
  per-GPU rate of set-up B is already below the single-GPU
  $0.26\times10^8$. The loss is attributed to ghost-zone communication
  "limited by communication bandwidth (not latency)" (asserted, no bandwidth
  measurement). An elongated $1{,}399{,}680\times240\times240$ grid on 972
  nodes reaches about 98%.
* **Strong scaling** (§V C, Table III, Fig. 8). Set-up B,
  $1440\times960\times480$ cells, 8 to 1000 nodes: per-GPU rate
  $0.084\times10^8$ at $240^3$ cells per GPU (efficiency 1.00, baseline 8
  nodes), 0.57 at $160^3$, 0.44 at $120^3$, 0.35 at $96^3$, 0.19 at $48^3$
  (total $93.46\times10^8$ zone-cycles/s on 6000 GPUs). Below about $120^3$
  cells per GPU is "very inefficient"; about $160^3$ is recommended for
  set-up B. Hours and GPU-hours per $10^5$ iterations in Table III are
  extrapolated from the benchmarks; the drop is attributed to under-occupied
  GPU threads (asserted).
* **Unsupported claim** (§VI). GRaM-X is said to run "at a speed 10 times
  faster and computational cost 30 times lesser compared to traditional
  CPU-based codes"; no CPU measurement, CPU code or CPU hardware appears in
  the paper.

## Verification

From [Shankar et al. (2023)](/sources/shankar-2023.md), §IV. All runs on
GPU; static-spacetime tests are compared visually, without error norms.
* **Balsara relativistic MHD shock tubes 1–5** (§IV A, Table I,
  Figs. 2–3). 1600 cells ($h = 1/1600$, grid $1600\times8\times8$), no AMR,
  no CT, RK4, $\nu = \Delta t/h = 0.8$, TVD minmod, HLLE; $\gamma = 2$
  (test 1) and $5/3$; exact solutions of Giacomazzo & Rezzolla. Test 1
  captures all five waves; test 4 ($W\approx22.37$) deviates at the centre
  "on the same level as" other codes; test 3 (pressure ratio $10^4$) shows
  "a considerable undershoot" at the right-moving fast shock, said to be
  largely removed by WENO (not shown). Table I lists the specific internal
  energy, not the pressure.
* **Cylindrical explosion** (§IV B, Fig. 4). The weak-field Komissarov case
  via GRHydro: $\mathbf B = (0.1, 0, 0)$, ambient $p = 3\times10^{-5}$,
  $\gamma = 4/3$, $200^2$ cells, CT, TVD, HLLE, RK4, $\nu = 0.25$, $t = 4$.
  A relativistic variant of the [MHD blast wave](/benchmarks/mhd-blast-wave.md).
* **[Relativistic magnetic rotor](/benchmarks/relativistic-magnetic-rotor.md)**
  (§IV C, Fig. 5). $400^2$ cells, CT, TVD, HLLE, RK4, $\nu = 0.25$,
  $t = 0.4$; maximum $W$ falls from about 10 to about 1.85.
* **Magnetized TOV star in dynamical spacetime** (§IV D, Fig. 6).
  Polytrope with $\gamma = 2$, mass $1.4\,M_\odot$; four AMR runs with
  finest $h$ = 1, 0.5, 0.25, 0.125 (geometric units of solar mass); WENO5,
  HLLE, RK4, $\nu = 0.25$ on the finest grid, CT, Z4c; to 8 ms.
  Central-density oscillations decrease with resolution with "convergence
  order of ∼ 2" (read from successive differences); the spectrum of the
  finest run matches the perturbative F, H1 and H2 modes, H3 "slightly
  shifted". The oscillation amplitude is larger than with GRHydro and BSSN,
  attributed to the interpolated stress–energy tensor.

## Limitations stated

M1 neutrino transport and other Riemann solvers are planned only (§VI).
Compute–communication overlap is absent (§V B). Optimization of set-up C
is pending (§V A).

# Citations

1. [Shankar et al. (2023)](/sources/shankar-2023.md), §§I–VI, eqs. 1–15,
   Tables I–III, Figs. 1–8 (arXiv v2).
