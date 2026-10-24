---
type: Source
title: "Bernardini et al. (2023) — STREAmS-2.0: Supersonic turbulent accelerated Navier-Stokes solver version 2.0"
description: "Two-page CPC new-version announcement of STREAmS-2.0, a GPU (CUDA) and CPU finite-difference DNS code for compressible wall turbulence: object-oriented Fortran rewrite, KEEP split convective schemes with WENO-Z shock capturing, new inflow conditions, thermally perfect gas and grid stretching."
resource: "doi:10.1016/j.cpc.2022.108644"
source_kind: paper
authors: [Bernardini M., Modesti D., Salvadore F., Sathyanarayana S., Della Posta G., Pirozzoli S.]
year: 2023
venue: "Comput. Phys. Commun. 285:108644"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Computer_Physics_Communications_Bernardini_STREAmS-20_Supersonic_turbulent_accelerated_Navier-Stokes_so.pdf"
tags: [software, gpu, finite-difference, turbulence, kinetic-energy-preserving, weno]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

A CPC "New version announcement" of [STREAmS](/software/streams.md), a
GPU-accelerated finite-difference solver for direct numerical simulation of
compressible, mainly wall-bounded, turbulent flows. The document is a program
summary. It prints no equations, figures, tables, tests or performance data, so
every claim on this page is **Stated**. The scheme details live in the cited
version-1 paper (Bernardini et al. 2021, CPC 263:107906) and in Tamaki, Kuya and
Kawai (2022).

Version 2.0 supersedes version 1 with these changes:

- an object-oriented rewrite in which Fortran derived types and type-bound
  procedures separate the physics equations from the computing back-end
  (NVIDIA GPU via CUDA, and CPU);
- `.ini` input;
- a family of kinetic-energy- and entropy-preserving (KEEP)
  [split convective forms](/methods/split-convective-forms.md) for the convective
  terms in smooth regions, called "stable, non-dissipative and accurate". The
  announcement links them to [kinetic energy preservation](/properties/kinetic-energy-preservation.md)
  after Tamaki et al. and makes no claim of entropy stability;
- [WENO-Z](/methods/weno-z.md) of Borges et al. as the shock-capturing flux;
- a recycling/rescaling turbulent inflow and a compressible-Blasius laminar
  inflow;
- a thermally perfect gas with polynomial specific heats (NASA Glenn
  coefficients);
- a grid stretching that blends uniform near-wall spacing with uniform
  resolution in Kolmogorov units.

The convective discretization is described only as "high-order finite
difference approximations with hybrid low-dissipative/shock-capturing
capabilities", that is, a [hybrid](/methods/hybrid-weno.md) central/WENO scheme.
The switch is not described. Time advancement is Runge–Kutta, with order not
stated. The supported configurations are turbulent channel flow, the laminar and
turbulent boundary layer, and shock-wave/boundary-layer interaction.

# Version read

Version of record (Elsevier typeset), 2 pages, both read. Text extraction is
clean. Page 1 matches Crossref (title, six authors, venue, DOI). The article was
received on 1 Dec 2022 and was online on 3 Jan 2023; the copyright line reads
2022, the issue is 2023. The program is available as CPC Library
doi:10.17632/hdcgjpzr3y.2 and at github.com/STREAmS-CFD/STREAmS-2 (GPLv3,
Fortran and CUDA).

# Key claims

1. STREAmS-2.0 supersedes STREAmS (CPC 263 (2021) 107906), for "New code structure and release of new features" (program summary). **Stated**
2. The solver is rewritten with an object-oriented design, Fortran derived types holding the variables and type-bound procedures, separating physics equations from back-end (abstract; revisions item 1). **Stated**
3. New back-ends and physics equations can be added within the same code structure, and code independent of physics, back-end or both is reused (item 1). **Stated**
4. The "layer of computing procedures maintains a lean structure that can be highly optimized with respect to the implemented back-end" (item 1). **Stated**
5. Back-ends are NVIDIA GPU and CPU, as in version 1; the languages are Fortran and CUDA (abstract; program summary). **Stated**
6. Input uses the `.ini` format (item 2). **Stated**
7. A family of KEEP schemes after Tamaki et al. [2] gives "stable, non-dissipative and accurate spatial discretization of the convective terms of the Navier–Stokes equations in smooth flow regions" (item 3). **Stated**
8. For the shock-capturing flux, "the improved low-dissipative WENO-Z scheme proposed by [3]" (Borges et al. 2008) is available (item 3). **Stated**
9. The spatial discretization is high-order finite differences with "hybrid low-dissipative/shock-capturing capabilities"; time advancement is Runge–Kutta, with order and number of stages not given (solution method). **Stated**
10. A recycling/rescaling inflow condition [4] is implemented for spatially developing compressible turbulent boundary layers (item 4). **Stated**
11. A laminar inflow from the solution of the compressible Blasius equation is available (item 4). **Stated**
12. The constitutive relations are generalized to thermally perfect gases, with specific heats given by user-specified polynomials of temperature [5] (item 5). **Stated**
13. A new grid-stretching function blends uniform near-wall spacing with uniform resolution in Kolmogorov units in the outer layer, "guaranteeing accuracy with higher computational efficiency" [6] (item 6). **Stated**
14. The code solves the compressible Navier–Stokes equations in Cartesian coordinates for DNS of compressible supersonic turbulent boundary layers. The supported configurations are the turbulent channel, the laminar and turbulent boundary layer, and shock-wave/boundary-layer interaction (nature of problem). **Stated**
15. The licence is GPLv3, with the public repository github.com/STREAmS-CFD/STREAmS-2 and CPC library DOI 10.17632/hdcgjpzr3y.2 (program summary). **Stated**

# Printed slips

None found.

# Notation map

The document prints no mathematical symbols.

| Bernardini et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| "high-order finite difference" | point values $u_i$, conservative fluxes $\hat f_{i+1/2}$ | [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md); reconstruction and splitting are not stated |
| KEEP | split convective form preserving $\kappa$ | after Tamaki et al. (2022); no form printed |
| WENO-Z | WENO-Z weights with $\tau_5$ | after Borges et al. (2008); no $\epsilon$, $q$ printed |

# Reference list

There are 6 printed references in numbered style ([1]–[6]), all inside the
program-summary block and all parsed. They are merged complete into the
[bibliography](/bibliography.md) with `citedby` `bernardini-2023`. Only ref. [3]
prints a DOI. Ref. [4] (Pirozzoli, Bernardini & Grasso 2010, J. Fluid Mech.
657:361–393) is a different work from the existing `pirozzoli-2010` (Pirozzoli
2010, J. Comput. Phys. 229:7180–7190) and is entered as `pirozzoli-2010-b`. Ref. [5] (NASA/TP 211556) and ref. [3] (Borges et al.)
match existing entries. No printed duplicates were found.

# Pages created or updated

Chunk 5 (2026-10-22), cited further in chunks 6–11 (2026-10-23/24). This source is cited on:

* [STREAmS](/software/streams.md)
