---
type: Software
title: "STREAmS (GPU finite-difference DNS solver for compressible wall turbulence)"
description: "Cartesian finite-difference DNS solver for the compressible Navier–Stokes equations, hybridizing an energy-preserving central flux with Lax–Friedrichs flux-vector-split WENO under a Ducros shock sensor, with low-storage RK3, kept in one Fortran source for CPUs and multi-GPU runs through CUDA Fortran kernels, device-resident data and optional compute–communication overlap."
status: established
aliases: [STREAmS, Supersonic TuRbulEnt Accelerated navier-Stokes Solver]
tags: [software, hydro, gpu, cuda, performance, scaling, time-integration, verification]
timestamp: 2026-10-12T00:00:00Z
---

# STREAmS

STREAmS (Supersonic TuRbulEnt Accelerated navier–Stokes Solver) is a
direct-numerical-simulation code for compressible wall-bounded turbulence on
Cartesian grids, presented by [Bernardini et al. (2021)](/sources/bernardini-2021.md).
It is not an astrophysical code; it belongs to the bundle as a GPU
compressible-flow solver whose porting, data-layout and scaling choices are
documented in detail. All claims below come from that one paper.

## Code

* Fortran ("mostly using Fortran 90 features"), CUDA Fortran and MPI;
  licence GPLv3; repository `https://github.com/matteobernardini/STREAmS`,
  CPC Library and Code Ocean archives (Program summary, §4.1). No version
  number is printed; §5 says "a baseline version of the solver" is released.
* Target flows: supersonic plane channel, spatially developing
  zero-pressure-gradient boundary layer, and oblique shock-wave/turbulent
  boundary-layer interaction (§1, §3).

## Equations

Compressible Navier–Stokes equations of a perfect, heat-conducting gas
(§2, eqs. 1–3): viscosity from Sutherland's law, conductivity from a
constant Prandtl number 0.72. In channel flow a body force keeps the mass-flow
rate discretely constant and its power is added to the energy equation. No
MHD, gravity, radiation or relativity.

## Spatial discretization

From [Bernardini et al. (2021)](/sources/bernardini-2021.md), §2.1:
* **Central flux.** Convective terms are written in locally conservative
  form, so that the derivative at node $i$ is a difference of numerical
  fluxes at $x_{i\pm1/2}$ (eq. 5). The numerical flux is the split-form
  energy-preserving flux of Pirozzoli (2010), a sum over stencil offsets of
  three-factor averages of density, velocity and the transported quantity
  (eqs. 6–7). It conserves total kinetic energy discretely "in the limit
  case of inviscid incompressible flow"; its order is user-selectable from
  second to eighth.
* **Shock capturing.** Lax–Friedrichs flux-vector splitting, with the
  positive and negative characteristic fluxes reconstructed at interfaces by
  WENO, order selectable from first to seventh. This is a finite-difference
  flux splitting, not an interface Riemann solver on reconstructed states
  (compare the Rusanov/Lax–Friedrichs entry of
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)).
  The locally conservative form "allows straightforward hybridization" of the
  two fluxes.
* **Shock sensor.** A modified Ducros sensor, a ratio of the negative
  velocity divergence to a norm of divergence, vorticity and a reference
  term built from fixed velocity and length scales, clipped to $[0,1]$
  (eq. 8). The reference term is printed in a form that is not
  dimensionally consistent with the other two; see the
  [Source page](/sources/bernardini-2021.md). The switching threshold is
  given only for the channel test, 0.05 (§3.1).
* **Viscous terms** in Laplacian form to avoid odd–even decoupling, central
  differences up to eighth order (eq. 9).
* **Wall-normal staggering** (§3.1): the wall lies on an intermediate node
  where convective fluxes vanish, giving exact conservation of total mass and
  doubling "the maximum allowed time step".

## Time integration

Method of lines with the three-stage, third-order low-storage Runge–Kutta
scheme of Spalart, Moser & Rogers (1991) (§2.2, eqs. 10–11). The coefficients
are printed as $(0, 17/60, -5/12)$ and $(8/15, 5/12, 3/4)$; the reader notes
that the standard scheme has $-17/60$ in the first set and that the printed
weights do not sum to one, an unverified sign slip recorded on the
[Source page](/sources/bernardini-2021.md). The time-step analysis (eqs.
12–14, Fig. 2) gives the inviscid limits in wall units at unit Courant number
($\nu = 1$) and concludes that the compressible explicit step is always more
restrictive than the incompressible one, by "easily exceeding an order of
magnitude" at low Mach number. See
[unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md) for the
method-of-lines family.

## Mesh

One structured Cartesian mesh, uniform in the streamwise and spanwise
directions and stretched in the wall-normal one (error-function or sinh
mapping); **no mesh refinement**. MPI uses a 2D pencil decomposition in the
streamwise and spanwise directions (§3, §4.1).

## GPU design

From [Bernardini et al. (2021)](/sources/bernardini-2021.md), §4; see
[GPU porting](/methods/gpu-porting.md):
* **Programming model** (§4.1). The authors weighed directives (OpenACC,
  OpenMP), CUDA and CUDA Fortran, and portable options (OpenCL, HIP), and
  chose CUDA Fortran `!$cuf kernel do(3)` automatic kernels so that "the
  large majority of the code" stays unaltered; GPU-only parts sit in
  `#ifdef USE_CUDA` blocks.
* **Memory** (§4.1). Each array exists twice, a baseline array and a compute
  array that gets the device attribute only in GPU builds. The host-to-device
  copy happens once before time marching and the reverse copy at the end; in
  CPU builds `move_alloc` replaces the copy. The solution is therefore
  device-resident for the whole run. The authors contrast this with AFiD
  (module aliasing of host/device duplicates) and CaNS (CUDA managed memory,
  whose prefetch hints "reduce the readability").
* **Explicit kernels** (§4.2). The CPU convective-flux routine uses large
  temporaries that would go to the kernel stack, so the Euler fluxes use
  explicit CUDA kernels on the GPU; the CPU and GPU flux implementations
  differ.
* **Memory-access optimization** (§4.2, Tables 1–2; one V100, channel flow,
  energy-conserving flux, $360\times240\times360$). Profiling shows the code
  memory-bound with low arithmetic intensity. Five steps: (A) baseline;
  (B) array order changed from variable-fastest to variable-slowest (AoS to
  SoA) for coalescing; (C) transposed copies for the streamwise convective
  kernels; (D) precomputed primitive variables, which cut memory accesses and
  divisions and avoid register spilling; (E) reordered MPI buffers. Total
  time (Table 1) 656 → 1396 → 515 → 311 → 297 ms, an overall factor 2.2. Step
  B alone slows the streamwise Euler kernel from 76 to 330 ms but enables
  step C. Global-memory load efficiency rises from 25–30% to 54–90%, store
  efficiency from 25% to 90–100%.
* **Communication** (§4.3, Fig. 12). One MPI process per GPU; host-staged or
  CUDA-aware MPI chosen at compile time. An optional asynchronous mode
  computes interior fluxes while ghost nodes are exchanged, then boundary
  fluxes; without CUDA-aware MPI it uses `cudaMemcpyAsync` in a separate
  CUDA stream.

## Performance

Precision (FP32 or FP64) is not stated anywhere in the paper.
* **Hardware generations** (§4.2, Fig. 11; $360\times240\times360$,
  energy-conserving flux; elapsed time per step): Broadwell node (36 cores)
  2.87 s; K40 GPU 2.42 s; P100 0.66 s; Skylake node (48 cores) 1.68 s; V100
  0.3 s. The comparison is a whole CPU node against a single GPU card,
  without cost or power normalization; the authors say a fair comparison
  needs power metrics, "beyond our objectives".
* **Weak scaling** (§4.3, Fig. 13; Marconi100, IBM Power9 nodes with 4 V100
  and NVLink; $360\times240\times360$ points per GPU, sixth-order
  energy-conserving flux): asynchronous efficiency "about 97% on 1024 GPUs"
  ("exceeding 97%" in the abstract); the synchronous variant degrades
  visibly. See [parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).
* **Strong scaling** ($512\times230\times360$ points in total): efficiency
  above 90% at 8 GPUs, 70% at 16; the asynchronous gain is "visible, but not
  remarkable". The stated optimum of "about 500,000" points per GPU matches
  the figure's upper axis, which is a factor 10 off the stated mesh, so it is
  not reliable.
* **Accuracy-matched comparison with ZEFR** (§4.4, Table 3; channel at
  friction Reynolds number 180, bulk Mach 0.2; single GPU, model not
  stated). At equal error (STREAmS fourth order on mesh M4, errors at most
  3%; the flux-reconstruction code ZEFR needs M6, three times the degrees of
  freedom), STREAmS costs 9.6 against 28.3 ns per point per iteration and 350
  against 2060 bytes per point; accuracy-equivalent time 88 against 880
  (about 10×) and memory 3.2 against 64.1 (units not printed). See
  [cell-update throughput](/definitions/cell-updates-per-second.md).

## Verification

All tests are DNS of wall turbulence compared graphically with reference
DNS or experiment; there is no shock-tube or convergence-order test
([Bernardini et al. (2021)](/sources/bernardini-2021.md), §3):
* Supersonic channel, bulk Mach 1.5, friction Reynolds number 502,
  $1032\times256\times512$: "excellent agreement" with earlier DNS; fourth-
  and sixth-order central runs and the hybrid run (sixth-order central with
  fifth-order WENO, sensor threshold 0.05) are indistinguishable because the
  sensor is "seldom activated"; full WENO3 and WENO5 show "excessive numerical
  dissipation" (Figs. 3–5).
* Supersonic boundary layer at Mach 2 ($4096\times256\times512$) and
  hypersonic boundary layer at Mach 5.86 ($2048\times384\times800$),
  agreeing with incompressible and hypersonic DNS (Figs. 6–8).
* Shock-wave/boundary-layer interaction at Mach 2.28 with an 8° shock
  generator ($4096\times384\times288$), wall pressure and streamwise
  fluctuations in "excellent"/"very good" agreement with the experiment of
  Dupont et al. (2006) (Figs. 9–10).

## Limitations stated or evident

* No mesh refinement, single-block Cartesian geometry (§3–§4).
* Only CUDA Fortran for GPUs, NVIDIA-specific by design (§4.1).
* Precision and the ZEFR-run GPU model are not stated; several figure
  values are read from plots only.

# Citations

1. [Bernardini et al. (2021)](/sources/bernardini-2021.md), Program summary,
   §§1–5, eqs. 1–15, Tables 1–3, Figs. 2–14 (published version).
