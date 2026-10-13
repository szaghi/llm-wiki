---
type: Software
title: "Cholla (GPU-native astrophysical MHD code)"
description: "GPU-native finite-volume code on a static uniform Cartesian mesh, in C++ with CUDA or HIP, whose MHD extension runs the VL+CT integrator with HLLD fluxes, characteristic PLM or PPM and Gardiner–Stone constrained transport entirely in GPU memory and weak-scales to 74,088 MI250X GCDs of Frontier, and whose cosmology extension adds super-comoving coordinates, FFT self-gravity, particle-mesh dark matter, a dual-energy formalism and Grackle chemistry on the host."
status: established
aliases: [Cholla, Cholla-MHD]
tags: [software, mhd, hydro, gpu, cuda, constrained-transport, unsplit, riemann-solver, performance, scaling, verification, cosmology, self-gravity, dual-energy]
timestamp: 2026-10-12T00:00:00Z
---

# Cholla

Cholla is a GPU-native, finite-volume astrophysical code on a static
Cartesian mesh, written in C++ and CUDA (Schneider & Robertson 2015).
[Caddy & Schneider (2024)](/sources/caddy-2024.md) add ideal MHD
("Cholla-MHD") and describe the GPU design, the verification suite and the
testing infrastructure of the current code.

## Code

* Repository `https://github.com/cholla-hydro/cholla` (§5). The version used
  is archived on Zenodo as "bcaddy/cholla: Caddy & Schneider 2024, v3.x"
  (doi:10.5281/zenodo.10927183, reference list); no release number beyond
  this is printed.
* One code base written in CUDA. A header of preprocessor macros
  (`gpu.hpp`) maps the CUDA calls to HIP at compile time, and the user
  builds with `nvcc` or `hipcc` (§2.3.2).
* Physics modules are compile-time switches, so there is "no single binary
  file that contains all of Cholla" (§4.3).

## Equations

Ideal MHD in conservative form with magnetic permeability 1 (§2.1,
eqs. 1–10): total pressure $P^* = p + \tfrac12|\mathbf B|^2$, total energy
$E = \rho e + \tfrac12\rho|\mathbf v|^2 + \tfrac12|\mathbf B|^2$ and the
ideal-gas law $p = (\gamma-1)\rho e$. Only an ideal equation of state is
stated. Other physics (chemistry, radiation transport, …) is applied after
the MHD step in a "first order operator-split fashion" (§2.2, step 10).

## Solvers

* **Integrator: VL+CT** of Stone & Gardiner (2009), now Cholla's default,
  replacing CTU because it is "more robust than the CTU algorithm described
  in Schneider & Robertson (2015)"; the paper calls it "very similar in
  structure to the MUSCL-Hancock integrator" (§2.2). The step: time step;
  piecewise-constant (PCM) interface states; HLLD; edge EMFs; half-step
  update of $u$ and the face field; PLM or PPM reconstruction at the half
  step; HLLD; edge EMFs; full update; then the operator-split physics and
  the MPI ghost exchange (§2.2, steps 1–10). See
  [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md).
* **Time step** (§2.2.1, eq. 11):
  $\Delta t = \nu\min\left(\frac{h}{|v_x|+c_f},\frac{h}{|v_y|+c_f},\frac{h}{|v_z|+c_f}\right)$
  over all cells, uniform across the grid (the paper allows a different
  cell size per direction). The paper requires $\nu \le 0.5$ and calls the
  method "formally accurate" at $\nu = 0.5$, "though that is an estimate";
  in practice it is **not stable at 0.5 but stable at 0.4**, and runs
  typically use $\nu = 0.3$ "to improve the accuracy of the operator
  splitting" (footnote 4). Recorded as printed: eq. 11 uses one $c_f$ for
  all three directions, and eq. 12 for $c_f$ contains only the
  $x$-component of $\mathbf B$.
* **Reconstruction** (§2.2.2, §2.2.6). The PCM predictor is "too diffusive
  to be used on its own in both reconstruction steps" but "excellent for
  debugging". PLM forms left, right, centred and van Leer differences of
  the primitive variables, projects them onto characteristic variables with
  the eigenvectors of [Stone et al. (2008)](/sources/stone-2008.md), and
  limits them with the LeVeque (2002) limiter (eqs. 23–28); limiting in
  primitive variables is an option. PPM follows Felker & Stone (2018); in
  this integrator it is "formally second order" and "does not improve the
  overall order of convergence".
* **Riemann solver**: HLLD, "implemented … exactly as described in Miyoshi
  & Kusano (2005)" (§2.2.3). The normal field at a face is the face value
  and is not reconstructed; the transverse field is reconstructed from the
  cell-centred average. Table 1 maps the magnetic components of the HLLD
  flux to face-centred electric fields per sweep direction. No other MHD
  solver is described. See
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
* **[Constrained transport](/methods/constrained-transport.md)** (§2.2.4,
  eqs. 13–18, Fig. 1, "based on Figure 5 of Stone et al. 2008"). Face-centred
  $\mathbf B$; the cell-centred field is the arithmetic mean of the two face
  values (eq. 13). Edge EMFs are the mean of the four adjacent face EMFs
  plus gradient terms formed against a cell-centre reference
  $\boldsymbol{\mathcal E} = -\mathbf v\times\mathbf B$ and upwinded by the
  sign of the face-normal velocity, with the mean of both sides otherwise
  (eqs. 15–18). The code advances $\mathbf B$ with the electric field, not
  the magnetic flux with the EMF; the paper says the two differ only by
  factors of unit length. CT was chosen "due to its overall accuracy,
  because the algorithm pairs well with static structured grids, and
  because the computational efficiency of GPUs is a good match to the
  algebraic complexity of CT" (§1).
* **Global time-step reduction** (§2.2.1, §2.3.3): on the GPU, then an MPI
  all-reduce. The last reduction level uses atomics; CUDA has no
  floating-point `atomicMax`, so an integer-encoded `atomicMax` taken from
  RAPIDS cuML is used. It is "slightly faster" than the earlier hybrid
  GPU+CPU reduction and "performs dramatically better as the number of
  elements increases".

## Mesh

Static, uniform Cartesian mesh with one global time step; no mesh
refinement (§2.2.1). Capacity: about $500^3$ cells on one 80 GB A100 and
about $459^3$ on one MI250X GCD; $19{,}278^3 \approx 7.2\times10^{12}$ cells
on Frontier (§1, abstract).

## GPU design and parallelism

From [Caddy & Schneider (2024)](/sources/caddy-2024.md), §2.3; see
[GPU porting](/methods/gpu-porting.md):
* **Device residency.** Older Cholla used an "extreme version of the
  'offload' model": conserved arrays lived in CPU memory and were copied to
  and from the GPU every step. The current code keeps all data on the GPU;
  MPI exchanges go directly from GPU buffers; only initial conditions and
  file I/O stay on the CPU, because HDF5 cannot write directly from GPU
  memory (footnote 5). The gain is described only as a "considerable
  speedup" (§5), with no timing of the old model.
* **Memory before arithmetic.** Cholla is "generally limited instead by GPU
  memory" (§2.3.1). Only the conserved variables are stored, which saves a
  second full grid of primitives and memory bandwidth; the cell-centred
  field is recomputed whenever needed (§2.2.1, §2.3.1).
* **Kernel fusion.** Fusing PCM reconstruction into the Riemann kernel
  gave about 10 % lower total runtime; fusing PLM with characteristic
  limiting into it **slowed the code by about 10–15 %**, because higher
  register use lowered occupancy. The outcome "depends on compiler
  optimizations which can vary between platforms" (§2.3.1).

## Performance

From [Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.2, Figs. 13–14;
metrics as in [cell-update throughput](/definitions/cell-updates-per-second.md)
and [parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).
* **Weak scaling** on Frontier (AMD MI250X; one GCD per MPI rank, "each GCD
  [is] a single GPU"), 3D slow magnetosonic wave, double precision,
  $459^3$ cells per GCD, PLM with characteristic limiting, 100 steps, time
  per step averaged without set-up and tear-down; 1 to 74,088 GCDs
  ($19{,}278^3$ cells). The printed numbers disagree:
  * §3.2 text: $2.36\times10^8$ cell updates per second on one GCD;
    $1.89\times10^8$ per GCD at 74,088 GCDs; total $1.40\times10^{13}$;
    efficiency 82.2 %.
  * Fig. 13 caption: $2.04\times10^8$ and $1.67\times10^8$; total
    $1.24\times10^{13}$; efficiency 82.2 %.
  * §5: efficiency "80 %", total "14.0 trillion".
  The ratios are $1.89/2.36 = 0.80$ and $1.67/2.04 = 0.82$; the plotted
  times (about 71 ms per $256^3$-normalized step at one GCD, about 88 ms at
  74,088) support the text values and about 80 %. The integrator time is
  nearly flat; MPI time "stabilizes at around 15ms" in the text, while the
  plot shows about 7–8 ms over $10^3$–$4\times10^4$ GCDs, rising to about
  15 ms only at full machine size; single-rank boundary copies take about
  0.6 % of the runtime. The residual loss is attributed to GPU-to-GPU
  runtime variance.
* **Strong scaling**, same problem with $459^3$ cells in total, one wave
  period (about 6100 steps): near-ideal to 32 GPUs (80 % efficiency),
  67.2 % at 64 GPUs ($115^3$ cells per GPU), not below 50 % until 256 GPUs,
  plateau at about 512 GPUs ($58^3$ per GPU) (Fig. 14). Recorded as
  printed: the text's "at most a ≈ 55% drop in efficiency" at
  $128^3$–$256^3$ cells per GPU is a loose bound; the measured 67.2 % at
  $115^3$ is a smaller drop.
* **NVIDIA GPUs**: about $2.59\times10^8$ cell updates per GPU-second on an
  A100 and $1.6\times10^8$ on a V100, with HLLD and second-order
  reconstruction (abstract, §3.2). Precision and problem size are not
  stated for these numbers.
* **Baselines.** No CPU baseline and no speed-up factor are claimed. The
  only comparison is "comparable to other similar optimized GPU codes (see
  e.g. Figures 9 and 10 in Grete et al. (2023))"; footnote 8 notes those are
  per node and for hydrodynamics, so it is not a like-for-like comparison.

## Testing and continuous integration

From [Caddy & Schneider (2024)](/sources/caddy-2024.md), §4:
* GoogleTest for unit, integration and system tests, including "death
  tests". Floating-point values match if either the absolute difference is
  below $10^{-14}$ or they are within 4 ULP; the $10^{-14}$ threshold was set
  because Sod results differ by about $5\times10^{-15}$ across hardware and
  compilers (§4.2.1).
* System tests compare with fiducial data cell by cell, or by the L2 norm
  of per-variable L1 norms for the MHD blast wave and the field loop, where
  the cell-by-cell check is fragile across systems (§4.2.2).
* On each pull request, GitHub Actions checks formatting and builds every
  HIP/AMD configuration in a container; a Jenkins matrix on local hardware
  builds and tests the CUDA/NVIDIA configurations and runs static analysers.
  **Only the CUDA builds are tested; the HIP builds are only compiled**
  (§4.3).

## Verification

All 3D, and all also in the automated test suite
([Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.1). The CFL number
of the accuracy tests is not stated.
* [Linear wave convergence](/benchmarks/linear-wave-convergence.md):
  grid-aligned waves on $N\times16\times16$ cells, $N = 16$ to 512; second
  order for slow, fast, Alfvén and entropy waves; PPM errors about an order
  of magnitude below PLM at equal $N$, at unchanged order (§3.1.1, Fig. 2).
* [Circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md):
  second order for travelling and standing waves; no gain of PPM over PLM
  (§3.1.2, Fig. 3).
* [Field-loop advection](/benchmarks/field-loop-advection.md): a tilted
  spherical loop; magnetic-energy dissipation "improves at approximately
  first order", maximum divergence about $10^{-17}$–$10^{-15}$ throughout;
  PPM gave spurious oscillations along the advection direction, so Fig. 5
  uses PLM (§3.1.3, Figs. 4–5).
* MHD Riemann problems on $512\times16\times16$ cells, run along all three
  axes in both orientations with "identical results": the
  [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md), Dai & Woodward
  (Ryu & Jones 2a), Ryu & Jones 1a and 4d, and the Einfeldt strong
  rarefaction (§3.1.4, Table 2, Figs. 6–10). Brio–Wu with PPM oscillates
  whether limiting is primitive or characteristic, and does not with PLM;
  the Felker & Stone (2018) PPM "significantly reduces oscillations"
  compared with the PPM of Stone et al. (2008). The Einfeldt case shows "no
  spurious oscillations or unphysical negative values". Results are shown
  visually only.
* [MHD blast wave](/benchmarks/mhd-blast-wave.md): $200\times300\times200$,
  plasma beta 0.2, smooth and symmetric; "Like Stone & Gardiner (2009), we
  find instabilities if β is decreased by a factor of 10" (§3.1.5, Fig. 11).
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md): $192^3$,
  qualitative comparison with Stone et al. (2008), Fig. 22; used as a
  regression test (§3.1.6, Fig. 12).

The Brio–Wu oscillations qualify, rather than contradict, the
[Athena++](/software/athena-plus-plus.md) result that characteristic
reconstruction removes them
([Stone et al. (2020)](/sources/stone-2020.md), §3.3.3): Cholla pairs PPM
with the VL+CT integrator, Athena++ with its method-of-lines integrators.

## Assessments in other sources

* The [AthenaK](/software/athenak.md) paper states that its single-GPU
  performance is "comparable to, or better than" Cholla-MHD and AthenaPK
  ([Stone et al. (2026)](/sources/stone-2026.md), §5.1); the AthenaK
  solver options and precision of that measurement are not stated.

## Later uses (batch 4)

### Cosmology extension

[Villasenor et al. (2021)](/sources/villasenor-2021.md) extend Cholla to
cosmological hydrodynamics plus N-body, "by engineering gas self-gravity,
a Fourier-space Poisson solver, a particle integrator, a comoving
coordinate scheme, and a coupling to the GRACKLE heating and cooling
library" (§1, §2, §7). The hydro solver of that version is the Godunov
finite-volume update with PPM reconstruction (Colella & Woodward 1984),
which the paper calls "third-order accurate in space and second-order
accurate in time" (§2.2, eq. 12); the integrator and the Riemann solver
are not named (details deferred to Schneider & Robertson 2015). This
qualifies, and does not contradict, the "formally second order" PPM
statement above: Villasenor et al. describe the reconstruction's spatial
order, with no measured convergence order, in a version that predates
VL+CT as default.
* **Super-comoving coordinates** (§2.1.2, eqs. 7–11), after Martel &
  Shapiro (1998), as used in Ramses by Teyssier (2002). With rescaled
  time, velocity, energies, pressure and potential, the adiabatic
  equations for $\gamma = 5/3$ take the form of the non-expanding
  equations, which "allows the extension of the hydrodynamics solver to
  an expanding frame system without any significant changes to the
  original solver". The evolved state adds the internal energy to
  density, momentum and total energy (eq. 12).
* **[Dual energy](/methods/dual-energy-formalism.md)** (§2.3, eq. 13): an
  Enzo-like single-threshold switch with threshold 0.035; see that page.
* **Gravity** (§2.4, eqs. 16–22): FFT Poisson solver (PFFT library) with
  the Green's function of the second-order discrete Laplacian and a
  fourth-order potential gradient; see
  [particle-mesh N-body](/methods/particle-mesh-gravity.md). The gravity
  sources are added after the hydro update, time-centred,
  $$\begin{aligned}
  (\rho\mathbf v)^{n+1}_i &= (\rho\mathbf v)^{*}_i + \tfrac12\Delta t^n\left(\rho^n_i + \rho^{n+1}_i\right)\mathbf g^{n+1/2}_i,\\
  E^{n+1}_i &= E^{*}_i + \tfrac12\Delta t^n\left[(\rho\mathbf v)^n_i + (\rho\mathbf v)^{*}_i\right]\cdot\mathbf g^{n+1/2}_i,
  \end{aligned}$$
  with $^{*}$ the post-hydro state, all in super-comoving variables
  (eqs. 20–21). The half-step potential is linearly extrapolated,
  $\Phi^n + \frac{\Delta t^n}{2\Delta t^{n-1}}(\Phi^n - \Phi^{n-1})$, times
  a scale-factor conversion (eq. 22). This is a source-form energy
  coupling, not the flux form of
  [conservative self-gravity](/methods/conservative-self-gravity.md).
* **Dark matter** (§2.5): CIC deposit and interpolation, kick–drift–kick
  (eqs. 23–28); see [particle-mesh N-body](/methods/particle-mesh-gravity.md).
* **Chemistry and cooling**: [Grackle](/software/grackle.md), called at
  the end of each step after the hydro update and the gravity sources,
  after which $E$ is reset from the updated internal energy (§2.6–2.7,
  eqs. 29–30); H and He ionization states are advected as passive scalars
  in the hydro update.
* **Time step** (§2.8, eqs. 33–35): the global minimum of a gas limit
  (scale factor times $h$ over $|v|+c_s$ per direction, Courant number
  0.3 by default, agreeing with the $\nu = 0.3$ above), a particle limit
  (coefficient 0.3) and an expansion limit (scale factor changing by
  1 %).
* **Small-step cell fix** (§2.8). Where a cell's gas time step falls below
  1/50 of the particle step, its density, momentum, total and internal
  energy are replaced by the average of its six nearest neighbours. This
  is not conservative. It happens "less than a dozen times per
  simulation" in the high-resolution runs; its effect is asserted, not
  tested, to be insignificant.
* The mesh is uniform, with one global time step (§1, §2.8), agreeing with
  the Mesh section above. The paper argues that a uniform grid samples
  the low-density, volume-filling intergalactic gas better than AMR or
  SPH at equal cost, "making the use of AMR unnecessary and inefficient";
  this is argued, not measured (§1).

### Host/device split (2021 version)

Only the hydro solver, including the advection of the ionization
species, runs on the GPUs; the FFT Poisson solver, the particle
integrator and the chemistry solver run on the host CPUs (§2.9). At
submission "an entirely GPU based distributed FFT solver has been
recently integrated into Cholla", and moving the particles and the H+He
network to the GPU was in progress. Grackle "is the slowest step in our
implementation" (§2.9), consuming "about half of the computational time"
(§4). This dates a hybrid stage between the offload model and the fully
GPU-resident design described above; see
[GPU porting](/methods/gpu-porting.md).

### Verification and performance (cosmology)

From [Villasenor et al. (2021)](/sources/villasenor-2021.md), §3, §4,
App. A:
* [Zel'dovich pancake](/benchmarks/zeldovich-pancake.md) against
  [Enzo](/software/enzo.md), 256 cells (§3.1, Fig. 1).
* Dark-matter-only matter power spectra ($256^3$ particles and cells)
  against Nyx, Ramses and Enzo: sub-per-cent once each code's gradient
  stencil and Green's function is matched (§3.2, Fig. 2).
* Adiabatic gas power spectra: against Ramses (Cholla run with the Ramses
  dual-energy condition) about 1 % or less at large scales and up to
  about 7 % at small scales for redshift below 1; against Enzo below 1 %
  at large and below 15 % at small scales (§3.3, Figs. 3–4). The authors
  state that small-scale gas power is "highly sensible [sic] to the
  numerical implementation of the hydrodynamics solver" and that they
  know of no robust code comparison of it.
* A mean-cosmic-temperature test of the dual-energy switch (§3.4); a
  chemistry plus UV-background run against Enzo with fitted
  intergalactic temperature–density relations agreeing within 1 % (§3.5).
* Resolution study at $512^3$, $1024^3$ and $2048^3$ cells and particles:
  the two finer runs "agree well"; no convergence rate is given (App. A,
  Fig. 17).
* **Performance** (§4): each $2048^3$ production run took 512 Summit
  GPUs for about 11 hours (about 1000 node-hours). No cell-update rate,
  precision or scaling study is printed.

# Citations

1. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §§1–5, Tables 1–2, Figs. 1–14 (arXiv v2).
2. [Stone et al. (2008)](/sources/stone-2008.md) (eigenvectors and comparison figures, as cited by Caddy & Schneider).
3. [Stone et al. (2020)](/sources/stone-2020.md), §3.3.3.
4. [Stone et al. (2026)](/sources/stone-2026.md), §5.1 (arXiv v1).
5. [Villasenor et al. (2021)](/sources/villasenor-2021.md), §§1–4, eqs. 7–35, App. A (arXiv v2).
