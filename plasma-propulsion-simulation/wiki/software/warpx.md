---
type: Software
title: "WarpX"
description: "Open-source GPU-native particle-in-cell code from the US DOE Exascale Computing Project, applied with Python callbacks to the axial–azimuthal Hall-thruster benchmark, where one H100 completes the 20 µs case in 1.81 days and its multigrid electrostatic solver limits multi-GPU scaling."
status: established
aliases: [WarpX PIC code]
tags: [software, pic, gpu, hall-thruster, computational-performance, benchmark]
timestamp: 2026-10-14T00:00:00Z
---

# WarpX

WarpX is an open-source particle-in-cell code developed under the US
Department of Energy Exascale Computing Project, written for GPUs, with a
Python interface; the paper states no implementation language or
underlying mesh library ([Marks & Gorodetsky (2025)](/sources/marks-2025.md),
Methods, Data availability). Versions 24.05 to 25.02 were used
(repository `https://github.com/BLAST-WarpX/warpx`); the Hall-thruster
scripts are at `https://github.com/archermarx/warpx-hall`.

## Algorithms used for Hall-thruster runs

All from [Marks & Gorodetsky (2025)](/sources/marks-2025.md), Methods.
* **Model.** Fully kinetic, explicit, electrostatic
  [PIC](/methods/pic-mcc.md); electrons and singly charged ions as
  macroparticles; no neutrals and no collisions in the benchmark runs.
* **Field solve.** Geometric multigrid Poisson solver, warm-started from the
  previous step, relative tolerance $10^{-2}$–$10^{-6}$ (baseline
  $10^{-5}$), in double precision.
* **Gather and push.** Energy-conserving gather (Lewis 1970) on a staggered
  grid, linear shape functions, relativistic Boris push
  (see [particle pushers](/methods/particle-pushers.md)), fused into one GPU
  kernel; particles in single precision.
* **Semi-implicit option.** The electrostatic semi-implicit scheme of
  Barnes, implemented in WarpX by Groenewald et al.
  (see [implicit and energy-conserving PIC](/methods/implicit-and-energy-conserving-pic.md)).
* **Particle management.** Sorting every 5–1000 steps (cost about 80% of a
  push) and leveling-thinning resampling.
* **Thruster-specific extensions as Python callbacks.** Ionization-source
  injection of electron–ion pairs with stochastic rounding of the injected
  count; cathode re-injection of the electron deficit (ions minus electrons
  crossing the anode plane) at the cathode plane, via WarpX's boundary
  scraping diagnostics; and an after-solve correction that subtracts a
  linear ramp so that the azimuthally averaged potential at the cathode
  plane is zero. The Python extensions take 0.6–1.9% of the run time
  (Table 4).
* **Hardware.** One Nvidia H100 (80 GB) for all runs but one on a V100; MPI
  with one rank per GPU for multi-GPU tests.

## Results

From [Marks & Gorodetsky (2025)](/sources/marks-2025.md), expanding the
authors' IEPC 2024 paper:
* [Axial–azimuthal benchmark](/benchmarks/axial-azimuthal-pic-benchmark.md):
  1.81 days on an H100 and 3.81 days on a V100 for Case 2; 2.86 and 5.06
  days on the H100 for Cases 1 and 3; 1.52 days for an optimized explicit
  configuration; profiles within the band of the 2019 codes (Fig. 3).
* Semi-implicit coarsening by 2×, 4× and 8× in 11.5, 4 and 2 h.
* Strong scaling of the multigrid electrostatic solver is limited by MPI
  communication (up to 95% of wall time at 32 GPUs), while particle routines
  and the electromagnetic solver scale "excellently", consistent with Myers
  et al. (2021) (see [GPU acceleration](/methods/gpu-acceleration-of-pic.md)).

# Citations

1. [Marks & Gorodetsky (2025)](/sources/marks-2025.md) — Methods, Results (Tables 4–5, Figs. 3–4, 15), Data availability.
