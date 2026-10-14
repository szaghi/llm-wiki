---
type: Method
title: "GPU acceleration of particle codes"
description: "Running particle-in-cell codes for plasma thrusters on GPUs: particle sorting or atomic deposition, active-particle compaction, memory-bound particle kernels, and the field solver as the strong-scaling bottleneck, with measured timings from a MATLAB/CUDA heavy-species code and from WarpX on the axial–azimuthal benchmark."
status: established
aliases: [GPU PIC, GPU-accelerated PIC, CUDA PIC]
tags: [gpu, pic, performance, numerics, hall-thruster]
timestamp: 2026-10-14T00:00:00Z
---

# GPU acceleration of particle codes

Fully kinetic thruster simulation is costly: [Taccogna et al. (2023)](/sources/taccogna-2023.md),
Sec. V B a, estimate that a 3D SPT-100 channel at $n=10^{18}$ m⁻³ and
$T_e\sim10$ eV ($\lambda_D\approx20$ µm) would need about 10 billion
cells, "hundreds of billions of particles" and about 10 TB of memory. GPUs
are one of the routes to that scale, alongside the algorithmic ones
([implicit PIC](/methods/implicit-and-energy-conserving-pic.md),
[reduced-order PIC](/methods/reduced-order-pic.md)).

## Implementation strategies

* **Deposition.** GPU PIC codes follow two strategies: particle sorting or
  atomic additions ([Taccogna et al. (2023)](/sources/taccogna-2023.md),
  Sec. V B). On CPUs, OpenMP race conditions are handled by reductions or
  atomics, and particle sorting improves cache use (Sec. V B).
* **Directive and kernel models.** The PPPL code LTP-PIC uses OpenACC; the
  RUB implicit code ECCOPIC2S-M uses CUDA; VORPAL and the octree PIC-DSMC
  code CHAOS (MPI-CUDA) are named as GPU codes
  ([Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. V B, codes list).
* **Active-particle compaction.** [Gallo et al. (2021)](/sources/gallo-2021.md),
  §2.6, Fig. 3, keep separate ion and neutral lists with an active flag and
  sort them every step so that the active particles are contiguous; kernels
  then act only on active particles, which avoids thread divergence and
  uncoalesced memory access. The code is MATLAB with GPUArrays; only the
  field-interpolation routine is a hand-written CUDA kernel. Single GPU, no
  MPI; hardware not stated.
* **Kernel fusion and precision.** [WarpX](/software/warpx.md) fuses field
  gather and particle push into one GPU kernel, solves the field in double
  precision and pushes particles in single precision
  ([Marks & Gorodetsky (2025)](/sources/marks-2025.md), Methods). WarpX
  does not use reduced-precision or tensor-core arithmetic ("Role of GPU
  hardware").

## Measured performance

* **Heavy-species hybrid code** ([Gallo et al. (2021)](/sources/gallo-2021.md),
  §4.3, Table 2). SPT-100-like channel, ions and neutrals as particles,
  electrons prescribed; times in minutes:

  | Routine | multicore CPU | GPU | time saved |
  |---|---|---|---|
  | total | 101.2 | 55.75 | 44.91% |
  | RK4 push | 43.65 | 23.18 | 46.89% |
  | cubic bi-spline interpolation | 40.22 | 19.80 | 50.77% |
  | neutral motion | 7.31 | 3.45 | 52.80% |

  The total corresponds to a speed-up of 1.82 (101.2/55.75); the text calls
  it "around 2". A fully sequential for-loop version "required 1.5 h to
  perform a single timestep".
* **Fully kinetic explicit PIC** on the
  [axial–azimuthal benchmark](/benchmarks/axial-azimuthal-pic-benchmark.md)
  ([Marks & Gorodetsky (2025)](/sources/marks-2025.md), Results, Table 4):
  20 µs in 1.81 days on one Nvidia H100 and 3.81 days on one V100 (75
  initial particles per cell), against 2.5 days on 112 CPUs for the fastest
  2019 participant. The authors infer that both code architecture (the V100
  run beats all but two 2019 codes) and hardware (the H100 is nearly 2×
  faster than the V100 with no algorithm change) contribute. At 75, 150 and
  300 initial particles per cell, gather-and-push takes 48.81%, 63.79% and
  73.11% of the run time, the field solve 40.86%, 24.21% and 16.63%.
* **Roofline** (Fig. 4b). On the H100, the gather-and-push and charge
  deposition kernels are memory-bound (DRAM and L2 bandwidth); the field
  solver is well below the memory-streaming limit, possibly because the
  problem is small ([Marks & Gorodetsky (2025)](/sources/marks-2025.md)).
* **Tuning** (Table 5). Loosening the multigrid relative tolerance from
  $10^{-5}$ to $10^{-3}$ saves about 13% (1.81 → 1.59 days) with results
  within PIC noise; sorting every 5–100 steps instead of 500 saves at most
  about 1 h; sorting costs about 80% of a particle push; the optimized
  explicit run takes 1.52 days. Resampling saves up to 25% but heats
  electrons (see [implicit and energy-conserving PIC](/methods/implicit-and-energy-conserving-pic.md),
  "Particle resampling").
* **Small-problem overhead.** A semi-implicit run with 8× less work ran only
  about 3.5× faster, which the authors attribute to fixed GPU overhead
  ([Marks & Gorodetsky (2025)](/sources/marks-2025.md), "Semi-implicit
  solver").
* **Earlier GPU benchmark participant.** The implicit CUDA code ECCOPIC2S-M
  ran the axial–azimuthal benchmark at the explicit codes' $\Delta t$ and
  $\Delta x$, which the benchmark imposed, so the GPU showed no benefit
  there; in the radial–azimuthal benchmark an explicit GPU version
  performed "comparable to the best CPU-based code"
  ([Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. V B).
  [Marks & Gorodetsky (2025)](/sources/marks-2025.md), Results, report that
  the only GPU code of the 2019 effort needed 9 days for Case 2 on an Nvidia
  A100 with an implicit pusher, "not directly comparable" to their run (the
  A100 postdates the 2019 publication; see the Source page).

## The field solver as the bottleneck

* [Adamovich et al. (2017)](/sources/adamovich-2017.md), §17, list GPUs
  among the advances in plasma HPC but state that "implementation of
  Poisson's equation, due to its nonlocal nature, makes it still a major
  challenge to code parallelization".
* [Marks & Gorodetsky (2025)](/sources/marks-2025.md), "Scaling analysis",
  Fig. 15, Tables 2–3, measure this in WarpX: in a 3D uniform-plasma
  strong-scaling test on up to 32 H100s, the largest workload that fits one
  GPU (1024×512×512 cells) reaches a speed-up of only 1.75, and the MPI
  communication fraction of the multigrid electrostatic solver rises to 95%
  at 32 GPUs. Particle routines and the electromagnetic solver scale
  "excellently". The authors attribute the inefficiency to the multigrid
  smoothing communication at every level, and note that the result is
  cluster-specific.
* By contrast, CHAOS (Jambunathan & Levin 2018) is reported to obtain good
  strong scaling up to 128 GPUs with a GPU conjugate-gradient Poisson solver
  ([Marks & Gorodetsky (2025)](/sources/marks-2025.md), "Scaling analysis",
  attributed).
* On CPUs, MPI domain decomposition (2, 8 or 26 neighbours in 1D, 2D, 3D)
  is reported to reach speed-ups of order 1000
  ([Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. V B).

## Remaining cost

[Marks & Gorodetsky (2025)](/sources/marks-2025.md), "Kinetic simulations
in an engineering context", estimate that runs with real ionization must
cover the ~10 kHz [breathing mode](/definitions/breathing-mode.md), about
1 ms or 50 times the benchmark duration, and that whole-device kinetic runs
"may still require wall times measuring in the months".

## Contradictions

* **First GPU PIC simulation of a plasma thruster.** Status: Open,
  recommended for closure by the human.
  [Gallo et al. (2021)](/sources/gallo-2021.md), §2.6, state, citing a
  single review (Kahnfeld et al. 2019), that their approach "is the very
  first one to exploit GPU computing for a PIC application in plasma
  thrusters". Two earlier GPU particle codes stand against it.
  (i) [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. V B, state
  that CUDA was employed in the implicit energy-conserving ECCOPIC2S-M code
  used by the RUB team in the Hall-thruster benchmark of their ref. 84,
  which is Charoy et al. (2019), the
  [axial–azimuthal benchmark](/benchmarks/axial-azimuthal-pic-benchmark.md);
  [Marks & Gorodetsky (2025)](/sources/marks-2025.md), Results, also report
  one GPU code in that 2019 effort. Their hardware detail (a 9-day run on
  an A100, released after the 2019 publication) leaves the date of that
  timing open, not the code's GPU participation in the benchmark.
  (ii) CHAOS (Jambunathan & Levin 2018), an MPI-CUDA octree PIC-DSMC code
  for thruster plumes, is cited by Taccogna et al. (2023, ref. 290) and by Marks &
  Gorodetsky (2025, ref. 13); it predates the 2021 claim. On this evidence
  the priority claim does not hold as stated; the sources do not print the
  dates of the GPU runs themselves, so the entry stays Open until the human
  closes it (or Charoy et al. 2019 is ingested).

# Citations

1. [Taccogna et al. (2023)](/sources/taccogna-2023.md) — Sec. V B, Sec. V B a, codes list.
2. [Gallo et al. (2021)](/sources/gallo-2021.md) — §2.6 (Fig. 3), §4.3 (Table 2).
3. [Marks & Gorodetsky (2025)](/sources/marks-2025.md) — Methods; Results (Tables 4–5, Figs. 4, 15); "Role of GPU hardware"; "Scaling analysis"; "Kinetic simulations in an engineering context".
4. [Adamovich et al. (2017)](/sources/adamovich-2017.md) — §17.
