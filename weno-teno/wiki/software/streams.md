---
type: Software
title: "STREAmS"
description: "STREAmS is a GPLv3 Fortran and CUDA finite-difference solver for direct numerical simulation of compressible wall turbulence; version 2.0 rewrites it with an object-oriented design separating physics from back-end and adds KEEP split-form convective schemes, a WENO-Z shock-capturing flux, recycling inflow and thermally perfect gases."
status: established
aliases: [STREAmS-2.0, Supersonic turbulent accelerated Navier-Stokes solver]
tags: [software, gpu, finite-difference, kinetic-energy-preserving, weno, turbulence]
timestamp: 2026-10-22T19:46:00Z
---

# STREAmS

STREAmS ("Supersonic turbulent accelerated Navier-Stokes solver") is a
high-order finite-difference solver of the compressible Navier–Stokes
equations in Cartesian coordinates for direct numerical simulation of
compressible, mainly wall-bounded, turbulent flows, with NVIDIA-GPU
(CUDA) and CPU back-ends. The bundle's account is
[Bernardini et al. (2023)](/sources/bernardini-2023.md), the two-page
Computer Physics Communications announcement of version 2.0, which
supersedes version 1 (Bernardini et al., CPC 2021, not ingested). The
announcement prints no equation, test or performance figure; everything
below is stated, not shown, in it.

## What the code solves

- The compressible Navier–Stokes equations for a thermally perfect gas
  in Cartesian coordinates, discretized by "high order finite difference
  approximations with hybrid low-dissipative/shock-capturing
  capabilities" and advanced by a Runge–Kutta scheme whose order and
  stages are not given (Solution method; see
  [conservative finite-difference schemes](/definitions/conservative-finite-difference-scheme.md)).
- Supported configurations: [turbulent channel flow](/benchmarks/turbulent-channel-flow.md),
  laminar and [turbulent boundary layers](/benchmarks/supersonic-turbulent-boundary-layer.md),
  and shock-wave/boundary-layer interaction (Nature of problem).
- Licence GPLv3; languages Fortran and CUDA; public repository on GitHub
  and a CPC Library archive (program summary).

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
- The announcement contains no validation, accuracy or performance data;
  those are in version 1's paper and in later releases, none of which is
  ingested.

# Citations

- [Bernardini et al. (2023)](/sources/bernardini-2023.md) — abstract; program summary; Summary of revisions, items 1–6.
- [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) — §1; §4.2.3.
- [Zaghi et al. (2023)](/sources/zaghi-2023.md) — §2.1.
