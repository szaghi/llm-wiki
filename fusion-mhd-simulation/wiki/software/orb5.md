---
type: Software
title: "ORB5"
description: "Global nonlinear electromagnetic gyrokinetic particle-in-cell code with all species kinetic (bulk ions, electrons, energetic particles), δf markers pushed by RK4 and fields on cubic B-spline finite elements; in the NLED-AUG energetic-particle benchmark it gives growth rates 1.6–1.7× MEGA's, lower frequencies, upward chirping where the hybrid codes chirp down, and stronger edge transport."
status: established
aliases: [ORB5 code]
tags: [code, energetic-particles, alfven-eigenmode, particles, finite-elements, verification]
timestamp: 2026-10-16T23:30:00Z
---

# ORB5

ORB5 is a global, nonlinear, electromagnetic gyrokinetic particle-in-cell code
for the full Vlasov–Maxwell system in which bulk ions, energetic particles
(EPs) and electrons are all kinetic (Lanti 2020; [Vlad et al. (2025)](/sources/vlad-2025.md),
§5). It is not a hybrid code: the reference against which the
[hybrid kinetic-MHD](/methods/hybrid-kinetic-mhd.md) codes are compared in the
cited benchmarks treats the bulk plasma kinetically too.

## Model and numerics

From Vlad et al. (2025), §5:
* [δf](/methods/delta-f-method.md) markers for each species, pushed along the
  gyrocentre characteristics by fourth-order Runge–Kutta (see
  [particle pushers](/methods/particle-pushers.md)); collisions and sources
  are available but switched off in the benchmark.
* Straight-field-line coordinates (radial flux label, straight-field-line
  poloidal angle, toroidal angle).
* Quasi-neutrality and parallel Ampère's law discretized with finite elements,
  typically cubic B-splines.
* A field-aligned Fourier filter keeps only poloidal modes near $-nq$, and a
  mixed-variable pullback scheme addresses the cancellation problem.
* Resolution in the NLED-AUG benchmark: a $2000\times144\times48$ grid,
  $3\times10^7$ ion and EP markers and $1.2\times10^8$ electron markers;
  convergence is taken from an earlier study (Vannini 2022). Runs used
  Marconi, Piz Daint and GENCI; no GPU use is reported.

## Benchmarks

* **[NLED-AUG](/benchmarks/nled-aug-benchmark.md), linear** (Vlad et al. 2025,
  §5, Table 2): the same near-axis $m=2$
  [energetic particle mode](/definitions/energetic-particle-mode.md) as the
  hybrid codes, with $\gamma=348\,489$ s$^{-1}$ and $\omega/2\pi=127.09$ kHz
  (finite orbit width only) and $286\,400$ s$^{-1}$ and $145.24$ kHz (FLR),
  1.59× and 1.68× MEGA's growth rate. FLR lowers $\gamma$ and raises $\omega$
  in ORB5, while it lowers $\omega$ in MEGA (§4). In the earlier JOREK
  comparison ORB5's growth rate at the nominal gradient was about
  $3.5\times10^5$ s$^{-1}$ against about $1.7$–$2.1\times10^5$ for HYMAGYC,
  MEGA and JOREK, and its frequency about 127 kHz against 143–179 kHz
  ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §IV B, Fig. 9).
* **NLED-AUG, nonlinear** (Vlad et al. 2025, §5, §7, Figs. 10, 13–14): the
  EPM chirps **up** into the TAE gap, opposite to HYMAGYC and MEGA; a
  counter-rotating external TAE forms; the EPM expands strongly in radius and
  overlaps the TAE, which the authors relate to core-to-edge transport; the EP
  profile fills the core and drops at mid-radius, and edge transport is strong,
  as in XTOR-K. FOW-only runs transport markedly more than FLR runs.
* **[ITPA $n=6$ TAE](/benchmarks/itpa-tae-benchmark.md)**: ORB5 is among the
  FLR-including codes of the comparison (Bogaarts et al. 2022, §IV A, Fig. 3;
  [Liu et al. (2022)](/sources/liu-2022.md), §6.2, Fig. 5;
  [Liu et al. (2024)](/sources/liu-2024.md), §III C, Fig. 14).
* **[DIII-D RSAE](/benchmarks/diii-d-rsae-benchmark.md)**: ORB5 sits in the
  lower group of growth rates with GTC, GYRO, EUTERPE and M3D-C1-K (figure
  reading, Liu et al. 2022, §6.3, Fig. 7).
* **Linear ITG**: JOREK's full-orbit electrostatic model agrees with GENE, XGC
  and ORB5 ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §7.1).

## Limitations and benchmark spread

* The growth-rate gap to the hybrid codes and the opposite chirping direction
  are not explained. Vlad et al. (2025) (§5, §7) list fast-ion inertia, which
  fully gyrokinetic models keep and hybrid models drop and which matters at the
  high EP fraction of this case, and different particle boundary conditions,
  without quantifying either. In the earlier linear benchmark ORB5 also found
  a different most unstable mode for the on-axis EP profile, reconciled by
  scans that showed different thresholds, "likely" from different damping
  (§1).
* Chirping-direction and saturation spreads are recorded on the
  [NLED-AUG benchmark](/benchmarks/nled-aug-benchmark.md).

# Citations

1. [Vlad et al. (2025)](/sources/vlad-2025.md) — §1, §§4–5, §7, Table 2, Figs. 10, 13–14.
2. [Bogaarts et al. (2022)](/sources/bogaarts-2022.md) — §IV, Figs. 3, 9.
3. [Liu et al. (2022)](/sources/liu-2022.md) — §6.2–6.3, Figs. 5, 7.
4. [Liu et al. (2024)](/sources/liu-2024.md) — §III C, Fig. 14.
5. [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §7.1.
