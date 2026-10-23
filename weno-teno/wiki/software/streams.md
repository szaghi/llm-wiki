---
type: Software
title: "STREAmS"
description: "STREAmS is a GPLv3 finite-difference solver for direct numerical simulation of compressible wall turbulence; version 2.0 adds an object-oriented physics/back-end split, KEEP split-form convective schemes, WENO-Z shock capturing and thermally perfect gases, and version 2.1 adds 2D-extruded curvilinear grids, OpenMP, HIP and OpenMP-offload back-ends and in situ visualization."
status: established
aliases: [STREAmS-2.0, STREAmS-2.1, Supersonic turbulent accelerated Navier-Stokes solver]
tags: [software, gpu, finite-difference, kinetic-energy-preserving, weno, turbulence]
timestamp: 2026-10-23T15:06:00Z
---

# STREAmS

STREAmS ("Supersonic turbulent accelerated Navier-Stokes solver") is a
high-order finite-difference solver of the compressible Navier–Stokes
equations for direct numerical simulation of compressible, mainly
wall-bounded, turbulent flows, with GPU and CPU back-ends. The bundle's
account is two two-page Computer Physics Communications announcements:
[Bernardini et al. (2023)](/sources/bernardini-2023.md), of version 2.0,
which supersedes version 1 (Bernardini et al., CPC 2021, not ingested),
and [Salvadore et al. (2025)](/sources/salvadore-2025.md), of version
2.1, which supersedes version 2.0. Neither announcement prints an
equation, test or performance figure; everything below is stated, not
shown, in them.

## What the code solves

- The compressible Navier–Stokes equations for a thermally perfect gas
  in Cartesian coordinates, discretized by "high order finite difference
  approximations with hybrid low-dissipative/shock-capturing
  capabilities" and advanced by a Runge–Kutta scheme whose order and
  stages the 2.0 announcement does not give (Solution method; see
  [conservative finite-difference schemes](/definitions/conservative-finite-difference-scheme.md)).
  The 2.1 announcement repeats the spatial phrase and names the time
  stepper "a third-order, low-storage Runge–Kutta scheme", without
  naming the scheme or calling it strong-stability preserving; it extends
  the geometry to "Cartesian or 2D-extruded curvilinear coordinates"
  (Salvadore et al. 2025, Solution method, Nature of problem).
- Supported configurations: [turbulent channel flow](/benchmarks/turbulent-channel-flow.md),
  laminar and [turbulent boundary layers](/benchmarks/supersonic-turbulent-boundary-layer.md),
  and shock-wave/boundary-layer interaction (Nature of problem); the 2.1
  announcement lists planar or circular channel flow, the boundary
  layer, shock-wave/boundary-layer interaction and airfoil flow
  (Salvadore et al. 2025, Nature of problem).
- Licence GPLv3; languages Fortran and CUDA (2.0), Fortran, CUDA and HIP
  (2.1); public repository on GitHub (STREAmS-CFD/STREAmS-2 for 2.1) and
  a CPC Library archive (program summaries).

## Changes in version 2.0

1. **Object-oriented structure.** The code is rewritten with Fortran
   derived types holding the variables and type-bound procedures, which
   separate the physics equations from the computing back-end: new
   back-ends and new equations can be added in the same structure, and
   code independent of the physics, of the back-end or of both is reused,
   while the "layer of computing procedures" stays lean enough to be
   optimized for each back-end (Summary of revisions, item 1).
2. **Input** in the `.ini` format (item 2).
3. **Convective schemes.** For smooth regions, the family of kinetic
   energy and entropy preserving (KEEP) schemes of Tamaki, Kuya & Kawai
   (2022), called "stable, non-dissipative and accurate"; for the
   shock-capturing flux, the [WENO-Z](/methods/weno-z.md) scheme of
   Borges et al. (2008) (item 3). The hybrid switch between the two is
   inherited from version 1 and not described in the announcement. See
   [split convective forms](/methods/split-convective-forms.md),
   [kinetic energy preservation](/properties/kinetic-energy-preservation.md)
   and [hybrid central-WENO schemes](/methods/hybrid-weno.md).
4. **Inflow.** A recycling/rescaling inflow for spatially developing
   compressible turbulent boundary layers (after Pirozzoli, Bernardini &
   Grasso 2010) and a laminar inflow from the compressible Blasius
   solution (item 4).
5. **Thermodynamics.** Variable specific heats given by user-specified
   polynomials of temperature (NASA Glenn coefficients) (item 5).
6. **Grid stretching** that blends uniform near-wall spacing with
   uniform resolution in Kolmogorov units in the outer layer, after
   Pirozzoli & Orlandi (2021), stated to give accuracy "with higher
   computational efficiency" (item 6).

## Changes in version 2.1

Salvadore et al. (2025, Summary of revisions) announce three changes:

1. **Curvilinear grids.** STREAmS-2 is merged with the curvilinear
   solver FLEW (Soldati, Ceci & Pirozzoli 2024, not ingested): a
   generalized curvilinear coordinate system along two axes, whose
   surface coordinates need not be orthogonal, with the third axis normal
   to the surface, i.e. two-dimensional grids extruded in the third
   direction. No metric terms or transformed equations are printed.
   Three curvilinear cases are stated to be "supported and validated":
   a circular arc channel, a curved boundary layer (e.g. a compression
   ramp) and an airfoil on a C-mesh; no validation is shown.
2. **Back-ends.** Besides the original CUDA Fortran and pure MPI
   paradigms, an OpenMP back-end for CPUs, a HIP back-end for AMD GPUs
   and an OpenMP-offload back-end, tested on Intel GPUs and "potentially
   suitable for different kinds of accelerators", stated to be
   "thoroughly benchmarked" in other papers; no figure is printed.
3. **In situ visualization.** A layer connected to ParaView Catalyst2,
   with predefined extraction procedures (swirling strength is named)
   and a dedicated input-file section, so that visualizations of very
   large grids need no full-field output.

The convective schemes of 2.0 (KEEP, WENO-Z) are neither restated nor
replaced in the 2.1 announcement, which describes the spatial
discretization only by the "hybrid low-dissipative/shock-capturing"
phrase.

## Positioning in the bundle

[De Vanna et al. (2023b)](/sources/devanna-2023-b.md), presenting
[URANOS](/software/uranos.md), list STREAmS among the codes (with AFiD,
CaNS, OpenSBLI, PyFR and ZEFR) that they characterize as incompressible,
DNS-only or vendor-specific (CUDA), and place their own GPU weak scaling "in line with"
those of AFiD, CaNS and STREAmS (§1, §4.2.3).
[Zaghi et al. (2023)](/sources/zaghi-2023.md), presenting
[ADAM](/software/adam.md), group STREAmS with PyFR and Nek5000 as
GPU-performant codes of "limited algorithmic flexibility" (§2.1).
Both are characterizations by other code authors, not measurements of
STREAmS.

## Qualifications

- "Entropy preserving" in KEEP is Tamaki et al.'s term; the announcement
  makes no [entropy-stability](/properties/entropy-stability.md) claim,
  and gives no split form.
- Neither announcement contains validation, accuracy or performance
  data; those are in version 1's paper and in the papers the 2.1
  announcement cites for its back-ends and cases, none of which is
  ingested.

# Citations

- [Bernardini et al. (2023)](/sources/bernardini-2023.md) — abstract; program summary; Summary of revisions, items 1–6.
- [Salvadore et al. (2025)](/sources/salvadore-2025.md) — abstract; program summary (Nature of problem, Solution method); Summary of revisions, items 1–3.
- [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) — §1; §4.2.3.
- [Zaghi et al. (2023)](/sources/zaghi-2023.md) — §2.1.
