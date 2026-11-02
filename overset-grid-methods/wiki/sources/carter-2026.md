---
type: Source
title: "Carter et al. (2026) — A fourth-order accurate single-step Lax–Wendroff-type scheme for Maxwell's equations on overlapping grids"
description: "A single-step fourth-order Lax–Wendroff-type scheme for Maxwell's equations on overlapping grids, from a Taylor expansion in time with five-point finite differences, stable up to CFL one on periodic grids and robust on overlapping grids, exactly divergence preserving on Cartesian grids, with fourth-order convergence on periodic and perfect-conductor problems."
resource: "doi:10.1016/j.jcp.2026.115322"
source_kind: paper
authors: [Carter J., Sturdevant B.J., Banks J.W., Shephard M.S., Bloomfield M.O.]
year: 2026
venue: "J. Comput. Phys. 567:115322"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2026_Crossref_Journal_of_Computational_Physics_Carter_A_fourth-order_accurate_single-step_Lax-Wendroff-type_scheme.pdf"
tags: [maxwell, finite-difference, high-order, stability]
timestamp: 2026-11-02T15:41:00Z
---

# Summary

A fourth-order, single-step method for the homogeneous isotropic Maxwell equations on overlapping grids in complex geometries: a Taylor expansion in time (Lax–Wendroff type) combined with five-point-wide finite differences in space. A von Neumann analysis on a uniform periodic grid gives stability up to CFL one, and the scheme is robustly stable on challenging overlapping-grid configurations at comparable CFL limits; on Cartesian grids it preserves the discrete divergence exactly. Fourth-order convergence is verified on overlapping grids with periodic and perfect-electrical-conductor boundaries ([Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md), [high-order discretizations](/methods/high-order-overset-discretization.md)).

# Version read

Version of record (Elsevier), 27 pages. Read in a targeted way (abstract, introduction, section structure, main results and conclusions closely; derivations and remaining results skimmed): from chunk 4 on, the bundle is compiled in the main session without reader subagents, by the owner's instruction. Claims below are limited to what was read closely.

# Key claims

1. The scheme is single step, Lax–Wendroff type, from a Taylor expansion in time with five-point-wide finite differences in space, fourth order in space and time (Abstract). **Derived**
2. A von Neumann analysis on a uniform periodic grid shows stability for CFL numbers up to one; on challenging overlapping grids the method is robustly stable with comparable CFL limits (Abstract). **Derived** / **Shown**
3. On Cartesian grids the discrete divergence-free constraint is preserved exactly (Abstract). **Derived**
4. Fourth-order convergence is verified on several overlapping-grid configurations with periodic and perfect-electrical-conductor boundaries (Abstract). **Shown**

# Printed slips

None recorded (targeted reading).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| CFL number | time step relative to the stability bound | |

# Reference list

25 references, merged complete into the [bibliography](/bibliography.md) with `citedby` carter-2026, from the Crossref deposited reference list; Yee (1966), printed under a variant author string, is `yee-1966`.

# Pages created or updated

Chunk 5 (2026-11-02). This source is cited on:

- [High-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md)
- [Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md)
