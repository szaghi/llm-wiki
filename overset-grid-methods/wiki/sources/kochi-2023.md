---
type: Source
title: "Kochi & Ramakrishna (2023) — Shock capturing using discontinuous Galerkin method and overset grids"
description: "Confines shock capturing to a refined structured overset grid aligned with the shock, built from the troubled-cell data of a coarse discontinuous Galerkin solution, and reruns the solver with the high-resolution flux and limiter only on that grid, giving sharp grid-aligned shocks for ramps, reflections, a cylinder bow shock and a Mach reflection."
resource: "doi:10.1016/j.jcp.2023.112230"
source_kind: paper
authors: [Kochi S.R.S.P., Ramakrishna M.]
year: 2023
venue: "J. Comput. Phys. 488:112230"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2023_Crossref_Journal_of_Computational_Physics_Kochi_Shock_capturing_using_discontinuous_Galerkin_method_and_over.pdf"
tags: [dg, shock-capturing, overset-grid, compressible]
timestamp: 2026-11-02T15:25:00Z
---

# Summary

A shock-fitting-like use of overset grids for a discontinuous Galerkin Euler solver: a coarse-grid DG solution flags troubled cells; a refined, structured overset grid aligned with the approximate shock location and enclosing those cells is built (with a manual component); the solver is rerun from the coarse solution with the high-resolution flux and limiter applied only on the overset grid. Shocks then lie along a grid line with very small thickness. Builds on the authors' DG overset coupling ([Kochi & Ramakrishna 2022](/sources/kochi-2022.md); [DG on overlapping grids](/methods/discontinuous-galerkin-on-overset-grids.md), [shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md)).

# Version read

Version of record (Elsevier), 28 pages. Read in a targeted way (abstract, introduction, section structure, main results and conclusions closely; derivations and remaining results skimmed): from chunk 4 on, the bundle is compiled in the main session without reader subagents, by the owner's instruction. Claims below are limited to what was read closely.

# Key claims

1. Troubled-cell data from a coarse-grid DG solution locate the shock; a refined structured overset grid aligned to it and enclosing the troubled cells is constructed, partly by hand (Abstract, Conclusions). **Stated**
2. The solver is rerun from the coarse solution with the high-resolution flux and the limiter only on the overset grid, so standard shock capturing acts only where needed (Conclusions). **Stated**
3. The shock is captured along a grid line with a very small non-dimensional thickness, which decreases with the order; an overset grid refined but not aligned with the shock does better than the coarse grid but worse than the aligned one (Conclusions). **Shown**
4. Tests: supersonic ramp, shock reflection off a flat plate, supersonic flow over a [circular cylinder](/benchmarks/flow-past-circular-cylinder.md) (shock stand-off validated against an analytical method) and a simple Mach reflection; preliminary moving straight shocks (Abstract). **Shown**

# Printed slips

None recorded (targeted reading).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| troubled cell | cell flagged by the shock indicator | |
| overset grid aligned to the shock | refined component $G_k$ of higher priority | |

# Reference list

33 references, merged complete into the [bibliography](/bibliography.md) with `citedby` kochi-2023, from the Crossref deposited reference list; three empty deposited records (refs. [11], [24], [26]) completed from the printed list (`tramel-2009`, `crabill-2016`, `kim-1998`). Benek et al. (1983) is cited as `benek-1983`.

# Pages created or updated

Chunk 4 (2026-11-02). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Discontinuous Galerkin methods on overlapping grids](/methods/discontinuous-galerkin-on-overset-grids.md)
- [Shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md)
