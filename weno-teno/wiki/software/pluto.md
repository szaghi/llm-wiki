---
type: Software
title: "PLUTO"
description: "PLUTO is the astrophysical finite-volume code of Mignone et al. that hosts the fourth-order pointwise constrained-transport schemes of the bundle for ideal classical and relativistic MHD and for resistive relativistic MHD, serves as data structure and MPI layer for moving-mesh and entropy-stable schemes, and is the design reference and comparison code of IDEFIX."
status: established
aliases: [PLUTO code, PLUTO astrophysical code]
tags: [software, mhd, relativistic, finite-volume]
timestamp: 2026-10-23T15:06:00Z
---

# PLUTO

PLUTO is the astrophysical code of Mignone et al. (2007, 2012), cited by
[Mignone et al. (2024)](/sources/mignone-2024.md) as the code in which
"all computations have been carried out" and the fourth-order resistive
method "has been implemented" (§4). No ingested source describes PLUTO
itself; the bundle knows it through the schemes built in it, the codes
that reuse its parts and the code that rewrites its design. What follows
is therefore a record of uses, not a description of the code.

## Schemes implemented in PLUTO

- **Fourth-order finite volumes for classical and relativistic MHD.**
  [Berta et al. (2024)](/sources/berta-2024.md) implement in PLUTO a
  fourth-order [constrained-transport](/methods/constrained-transport.md)
  scheme for ideal MHD and special relativistic MHD on Cartesian grids:
  cell averages converted to point values by
  [Laplacian corrections](/operators/cell-average-point-value-conversion.md),
  pointwise WENO-Z, MP5 or WENO3 reconstruction, one Riemann problem per
  face with the [HLL family](/methods/hll-riemann-solvers.md) or Roe, and
  upwind constrained-transport edge fields (§3–§4).
- **Fourth-order finite volumes for resistive relativistic MHD.** Mignone
  et al. (2024), who call Berta et al. "Paper II", extend it to resistive
  relativistic MHD with a stiff Ohm's-law source integrated by
  [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) schemes, explicit stages
  on cell averages and the implicit stage on point values; the scheme needs
  three ghost zones and two boundary calls per stage, "a more compact
  stencil when compared to its previous version (Paper II)" (§3.10, §5;
  [relativistic hydrodynamics and MHD](/definitions/relativistic-hydrodynamics.md)).
  Its runs use Courant number 0.4 in 2D and 0.3 in 3D (§4).

## PLUTO as data structure and parallel layer

- [Li, Duan & Tang (2022c)](/sources/li-2022-c.md) parallelize their
  entropy-conservative moving-mesh scheme for the
  [multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
  with the MPI parts of PLUTO, on CPU nodes with two Intel Xeon E5-2697A V4.
- [Duan & Tang (2022)](/sources/duan-2022.md) run their entropy-stable
  adaptive-moving-mesh schemes for relativistic MHD "on the PLUTO data
  structure" with MPI, on the same kind of nodes.

## PLUTO as design reference: IDEFIX

[Lesur et al. (2023)](/sources/lesur-2023.md) write
[IDEFIX](/software/idefix.md) as a deliberate rewrite of the PLUTO design
(reconstruct–solve–average, a PLUTO-compatible interface) for GPUs, and
state two algorithmic differences (§2.2–2.3, §2.7):

- IDEFIX puts the pressure in the momentum flux, solved by the Riemann
  solver, where PLUTO treats it as a source term, which creates additional
  pressure source terms in curvilinear geometry; the two codes' results
  "are expected to differ, even if the same algorithm combination is
  chosen";
- IDEFIX's time step combines hyperbolic and parabolic limits pointwise
  without PLUTO's dimension factor in the Courant number, and "can be
  somewhat larger".

They use PLUTO 4.3 with the Roe solver on 8000 points as the reference
for the [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md), and state
CPU performance and scaling "close to PLUTO 4.4" (§4.2, §5).

## Benchmarks run in PLUTO

Mignone et al. (2024, §4): a two-dimensional telegraph-equation test, a
stationary charged vortex ([magnetized vortex](/benchmarks/magnetized-vortex.md)),
a resistive relativistic rotor and a 3D blast wave
([MHD blast wave](/benchmarks/mhd-blast-wave.md)), the ideal
[tearing mode](/benchmarks/tearing-mode-instability.md) and a 3D relativistic
[Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md).
Berta et al. (2024, §5): rotated shock tubes, vortices, the
[circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md),
[field-loop advection](/benchmarks/field-loop-advection.md), the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), blast waves and
the [shock–cloud interaction](/benchmarks/mhd-shock-cloud-interaction.md).

## Qualifications

- PLUTO's own algorithms (its default reconstructions, Riemann solvers,
  time steppers, mesh and geometry support) are not documented by any
  ingested source; the statements above concern the schemes the sources
  add to it or the differences other authors state.
- The two PLUTO papers (Mignone et al. 2007, 2012) are cited works, not
  ingested.

# Citations

- [Mignone et al. (2024)](/sources/mignone-2024.md) — §1; §3.10; §4; §5.
- [Berta et al. (2024)](/sources/berta-2024.md) — arXiv v4: §3–§5.
- [Lesur et al. (2023)](/sources/lesur-2023.md) — arXiv v1: §2.2–2.3, §2.7, §4.2 (Fig. 6), §5.
- [Li, Duan & Tang (2022c)](/sources/li-2022-c.md) — §5.
- [Duan & Tang (2022)](/sources/duan-2022.md) — arXiv v1: §6.
