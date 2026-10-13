---
type: Software
title: "AMReX and PeleC"
description: "AMReX is the block-structured AMR framework (C++/Fortran, MPI, OpenMP, GPUs, embedded-boundary geometry database, subcycling, refluxing) on which four sources of this corpus run cut-cell finite volume with flux or state redistribution and a fifth-order finite-difference WENO AMR; PeleC is its compressible reacting-flow code, second order with a predictor–corrector, run on piston-bowl engine geometries."
status: established
aliases: [AMReX, AMReX-Hydro, PeleC, Pele, CAMR, AMReX CNS solver]
tags: [software, amr, embedded-boundary, finite-volume, finite-difference, gpu]
timestamp: 2026-10-13T00:00:00Z
---

# AMReX and PeleC

The sources use AMReX as the host framework of the methods they present
and describe it only as far as those methods need. None of them measures
the framework itself.

## AMReX

**What the framework provides.** A publicly available framework for
massively parallel block-structured AMR applications with C++ and
Fortran interfaces. Listed features: flat MPI, OpenMP, hybrid
MPI/OpenMP or MPI/MPI parallelism, GPUs, logical tiling of grids,
coarsening, interpolation and ghost-cell filling between levels,
multigrid Poisson and Helmholtz solvers, subcycled time stepping, and
particles ([Natarajan et al. (2022)](/sources/natarajan-2022.md), §1).
Its basic data structure is a set of multi-dimensional arrays on
logically rectangular patches, distributed over MPI ranks, which
exchange data mostly by filling ghost (halo) cells
([Giuliani et al. (2022)](/sources/giuliani-2022.md), §4). The
multilevel step is the Berger–Colella one: coarse level first, fine
ghost cells filled from coarse data, finer levels subcycled, then
average-down and refluxing at synchronization
([Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §2.3;
[high-order AMR](/methods/high-order-amr.md)).

**Embedded-boundary geometry.** Cells are regular, cut or covered. The
geometry (cell type, volume fraction $\kappa_i$, face area fractions,
cell and face centroids, and the centroid, normal and area of the single
boundary face of a cut cell) is computed once and stored in a
distributed database, for every AMR level and for coarsened multigrid
levels. It is generated from an implicit function (positive in the
body, negative in the fluid), with library shapes, splines and
constructive solid geometry; an application can also supply its own.
Split, tunnel and multivalued cells are not supported
([Giuliani et al. (2022)](/sources/giuliani-2022.md), §§2.1–2.2;
[Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §2.1;
[cut-cell finite volume](/methods/cut-cell-finite-volume.md)).

**AMReX-Hydro and redistribution.** The open-source AMReX-Hydro modules
hold both [flux redistribution](/methods/flux-redistribution.md) and
[state redistribution](/methods/state-redistribution.md) (C++, 2D and
3D), used by the compressible and low-Mach codes. The 2022
implementation keeps coarse–fine boundaries off cut cells, so state
redistribution runs one level at a time, exactly as on a uniform grid;
neighbourhoods start from 3×3×3 blocks, and the preprocessing needs up to
three ghost cells per direction in the worst case. Where no
well-conditioned gradient can be built, the solver and the
redistribution drop to first order locally
([Giuliani et al. (2022)](/sources/giuliani-2022.md), §4). Barrio
Sanchez et al. lift the restriction with a re-redistribution register
merged with the reflux register
([Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §3.4).
The state-redistribution code runs on CPUs and GPUs
([Giuliani et al. (2022)](/sources/giuliani-2022.md), §6). No source
reports a GPU timing.

**Codes built on it in this corpus.**

| Code | Equations and scheme | Used by |
|---|---|---|
| CNS (AMReX's compressible example solver) | Navier–Stokes; second-order Godunov with van Leer-limited characteristic variables, RK2; flux redistribution; extended to moving bodies | [Natarajan et al. (2022)](/sources/natarajan-2022.md), §2 |
| CAMR | Euler; unsplit piecewise-linear Godunov with a two-shock Riemann solver, or method of lines with a predictor–corrector; weighted state redistribution | [Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §§4.1–4.3, App. C |
| PeleC | see below | [Giuliani et al. (2022)](/sources/giuliani-2022.md), §§5.1, 6.1; [Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §4.4 |
| IAMR, MFIX-Exa | incompressible and low-Mach (multiphase) flow with a nodal projection; state redistribution of the advective update only | [Giuliani et al. (2022)](/sources/giuliani-2022.md), §§5.2, 6.2 |
| A cell-centred FD-WENO AMR (the authors' own) | Euler; fifth-order characteristic FD-WENO-JS with a local Lax–Friedrichs splitting, subcycled SSP-RK3 | [Wang et al. (2025)](/sources/wang-2025.md), §§3–4 (preprint) |

**What each source ran.**
* *Moving bodies* ([Natarajan et al. (2022)](/sources/natarajan-2022.md),
  §§2–3). Every cut cell is refined to the finest level, so no
  coarse–fine boundary crosses the body; a Wong–Lele density sensor
  (threshold 0.005) tags the flow features in addition. Runs use 3–5
  levels, e.g. a $32^3$ base with two levels for a closed piston.
  The tests are on [cut-cell finite volume](/methods/cut-cell-finite-volume.md)
  and the cylinder and [Schardin](/benchmarks/schardin-problem.md)
  benchmarks.
* *Weighted state redistribution in 3D*
  ([Giuliani et al. (2022)](/sources/giuliani-2022.md), §§3.2, 6). 2D
  ramp and [supersonic vortex](/benchmarks/supersonic-vortex-annulus.md)
  tests, then PeleC on a piston bowl and MFIX-Exa on a circulating
  fluidized bed (2.5 cm mesh, smallest volume fraction
  $9.4\times10^{-6}$; cells below $10^{-6}$ treated as covered because of
  the linear solver).
* *Re-redistribution* ([Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md),
  §4). CAMR for the conservation test in a tilted channel, a
  [Sod](/benchmarks/sod-shock-tube.md) problem in a channel rotated 30°
  and the Mach 2.81
  [shock reflection from a cylinder](/benchmarks/shock-reflection-from-cylinder.md);
  PeleC for an engine (below).
* *Finite differences on AMReX* ([Wang et al. (2025)](/sources/wang-2025.md),
  §§4, 6; preprint). AMReX supplies grid nesting, dynamic regridding,
  ghost-cell filling and basic coarse–fine synchronization. The authors
  add WENO prolongation and restriction for ratios 2 and 4, stage-matched
  ghost values in time, refluxing of the Runge–Kutta stage fluxes, and
  the cell-centred storage that makes refluxing possible
  ([high-order AMR](/methods/high-order-amr.md)). AMReX's regrid
  interval `regrid_int` decides whether non-conservative interpolation
  shows: at 2 the hybrid and pure WENO interpolations agree on Sod; at 5
  (Sod) and 10 (Lax) pure WENO gives oscillations and a wrong shock speed
  (§6.3). The conclusions state that the code runs on CPUs and GPUs
  because AMReX does; no GPU run is reported.

## PeleC

PeleC is the compressible reacting-flow code of the Pele suite, built on
AMReX ([Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §4;
[Giuliani et al. (2022)](/sources/giuliani-2022.md), §6).

**Discretization** ([Giuliani et al. (2022)](/sources/giuliani-2022.md), §5.1).
* *Equations:* multi-species compressible Navier–Stokes with finite-rate
  chemistry and mixture-averaged species diffusion.
* *Space:* limited extrapolation of characteristic variables to face
  centres with a van Leer MUSCL limiter (a one-sided slope is zeroed if a
  covered cell is in its stencil); a two-shock approximate Riemann solver
  at face centroids, and a "normal Riemann solver" at the
  embedded-boundary face ([exact Riemann solver](/methods/exact-riemann-solver.md),
  where the two-shock approximation is described). Diffusive fluxes are
  centred and second order; at the wall a ray cast into the fluid gives a
  one-sided diffusive flux.
* *Time:* advection and diffusion explicit, reactions by a stiff ODE
  solver, coupled by a second-order predictor–corrector with an optional
  fixed-point iteration ("similar in spirit to spectral deferred
  corrections"); formal second order needs at least one iteration. State
  redistribution is applied after every advective–diffusive update. The
  time step obeys, in every cell, $(\max\vert\mathbf v\vert + c)\Delta t/h \le \tfrac13$
  with $h$ the smallest spacing, plus diffusive limits that in practice
  do not bind.

**Runs.**
* *Fuel injection into a piston bowl* ([Giuliani et al. (2022)](/sources/giuliani-2022.md),
  §6.1). Four methane jets into hot oxidizer, 21 species and 84
  reactions; base grid 128×128×48 (0.02 cm), two levels (0.005 cm), 11
  million cells on the finest level when the jets hit the walls; smallest
  volume fraction $10^{-6}$. State redistribution takes at most about 2 %
  of the run time. With flux redistribution the run is "not possible":
  mass fractions leave $[0, 1]$.
* *Compression-ignition engine* ([Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md),
  §4.4, Table 1). Dual-pulse n-dodecane injection into methane–air, 35
  species transported, reactions switched off, base grid 128×128×32 with
  one AMR level, run to 0.9 ms on 4 nodes of 36 Skylake cores (NREL
  Eagle). Adaptive refinement at the wall, made possible by
  re-redistribution, gives the flow of full wall refinement at 10.1 s
  per step against 44.0 at 0.45 ms, and 14.4 against 45.3 at 0.9 ms (3.2
  times faster). Keeping the wall one level coarser costs 10.4 and 10.0 s
  per step but diffuses the jets after they reach the wall.
  The production practice before this work was that coarser option;
  refining the whole wall to the finest of six levels is called
  computationally unfeasible.

**Later uses (batch 15).** *The multilevel step in the primary source*
([Berger & Colella (1989)](/sources/berger-1989.md), §§2–4). The
sequence above (coarse first, subcycled finer levels, average-down and
the flux correction at synchronization) is the paper's. Two precisions:
fine ghost cells are first copied from adjacent same-level grids, and
only the remainder is interpolated from coarser data, bilinearly in space
and linearly in time (§4); and the 1989 paper allows only even refinement
ratios, equal in space and time (§2). How AMReX itself fills ghost cells
is not stated by the sources of this page
([high-order AMR](/methods/high-order-amr.md)).

# Citations

1. [Giuliani et al. (2022)](/sources/giuliani-2022.md), §§2.1–2.2, 4, 5.1–5.2, 6 (arXiv v2).
2. [Natarajan et al. (2022)](/sources/natarajan-2022.md), §§1–3 (arXiv v1).
3. [Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §§2.1, 2.3, 3.4, 4, App. C (arXiv v1).
4. [Wang et al. (2025)](/sources/wang-2025.md), §§3–4, 6.3, 7 (arXiv preprint).
5. [Berger & Colella (1989)](/sources/berger-1989.md), §§2–4.
