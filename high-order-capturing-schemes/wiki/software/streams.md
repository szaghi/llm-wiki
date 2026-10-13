---
type: Software
title: "STREAmS (compressible wall-turbulence DNS on GPUs)"
description: "Open-source Fortran/CUDA Fortran finite-difference DNS code for supersonic and hypersonic channel, boundary-layer and shock/boundary-layer flows: a kinetic-energy-preserving central flux of order 2–8, switched by a Ducros-type sensor to characteristic WENO of order 1–7, low-storage RK3, and GPU porting at 97% weak-scaling efficiency on 1024 GPUs."
status: established
aliases: [STREAmS, Supersonic TuRbulEnt Accelerated navier-Stokes Solver]
tags: [software, finite-difference, weno, hybrid, turbulence, gpu]
timestamp: 2026-10-13T00:00:00Z
---

# STREAmS

**Identity** ([Bernardini et al. (2021)](/sources/bernardini-2021.md),
program summary). STREAmS (Supersonic TuRbulEnt Accelerated navier–Stokes
Solver) was developed at Sapienza University of Rome, TU Delft and
CINECA. It is written in Fortran 90 and CUDA Fortran with MPI, under the
GPLv3 licence, and published at github.com/matteobernardini/STREAmS. It
covers three Cartesian wall-bounded flows: plane channel, zero-pressure-gradient
boundary layer, and oblique shock/boundary-layer interaction.

**Numerics** (§2).
* *Locally conservative finite differences*
  ([conservative finite difference](/methods/conservative-finite-difference.md)).
  Smooth regions use a central, kinetic-energy-preserving split flux,
  recast in conservative form, of even order 2 to 8. It conserves total
  kinetic energy discretely in the inviscid incompressible limit (eqs. 6–7).
* *Hybridization.* Because the flux is local, any interface can switch to
  Lax–Friedrichs flux-vector splitting with WENO of order 1 to 7 on the
  characteristic fluxes ([WENO](/methods/weno.md)). The switch is a Ducros-type
  sensor that flags only compressions, regularized by fixed flow scales
  (eq. 8). The threshold is 0.05 in the channel runs. The paper does not
  say how the sensor value maps to interfaces, nor whether the splitting
  speed is global or local ([hybrid compact-WENO](/methods/hybrid-compact-weno.md)).
* *Viscous terms* in Laplacian form, central to eighth order (eq. 9).
* *Time:* the three-stage low-storage RK3 of Spalart, Moser and Rogers.
  One of its coefficients is negative, so it is not SSP
  ([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).
* *Wall:* the wall-normal mesh is staggered so that the wall falls on an
  interface, where the convective flux vanishes. This gives exact mass
  conservation and doubles the allowed time step (§3.1).

**Evidence** (§3). On a Mach 1.5 channel, fourth- and sixth-order central
schemes and the hybrid at threshold 0.05 agree with a reference DNS. Full
WENO3 and WENO5 damp the turbulence statistics, which the authors call a
clear symptom of excessive numerical dissipation (Fig. 5;
[bandwidth-optimized WENO](/methods/bandwidth-optimized-weno.md)). The
hybrid reproduces a Mach 5.86 boundary layer and the Mach 2.28
shock/boundary-layer experiment of Dupont et al.

**GPU implementation** (§4).
* Every array has a host and a device copy. Without CUDA, `move_alloc`
  hands the host array to the device name, so one source runs on both.
  Loops are `!$cuf kernel` automatic kernels, and the convective fluxes
  are explicit kernels.
* On one V100 the code is memory-bound. Layout changes, a transposed
  copy for $x$-fluxes, precomputed primitive variables (which remove
  register spilling) and coalesced MPI buffers cut the time per step from
  656 ms to 297 ms, a factor 2.2 (Tables 1–2).
* With 2D pencil decomposition and CUDA-aware or host-staged MPI
  overlapping communication, weak scaling is about 97% efficient on 1024
  GPUs. Strong scaling is above 90% on 8 GPUs and 70% on 16, with an
  optimum near 0.5 million points per GPU.
* At equal accuracy on a channel at $\mathrm{Re}_\tau = 180$, it is about
  10 times faster and needs about 21 times less memory than the
  flux-reconstruction GPU code ZEFR (Table 3). These are the code
  authors' figures.

# Citations

1. [Bernardini et al. (2021)](/sources/bernardini-2021.md), §§2–4, Tables 1–3.
