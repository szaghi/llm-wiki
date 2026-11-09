---
type: Method
title: "Shock fitting on structured grids"
description: "Treating shocks as discontinuities with Rankine–Hugoniot jumps instead of capturing them: boundary and floating shock fitting tie the grid topology to the shock topology, while extrapolated shock fitting blanks the cells the shock crosses and exchanges data by Taylor extrapolation, recovering design-order convergence on unmodified structured grids."
status: established
aliases: [shock-fitting, structured extrapolated shock fitting, SESF, floating shock fitting, boundary shock fitting]
tags: [shock, structured-grid, compressible]
timestamp: 2026-11-08T21:07:00Z
---

# Shock fitting on structured grids

Shock capturing smears a shock over a few cells and its error drops the
global order of convergence near or below first order; **shock fitting**
represents the shock as a discontinuity whose two states obey the
Rankine–Hugoniot relations and whose speed follows from them
([Assonitis et al. 2022](/sources/assonitis-2022.md)).

Structured-grid shock fitting developed two forms from the 1960s:

- **boundary shock fitting**, where the shock is a boundary of the
  [boundary-fitted](/definitions/boundary-fitted-coordinate-system.md) grid —
  accurate but hard to extend to interacting shocks;
- **floating shock fitting**, where the shock moves across a fixed grid and
  special stencils are used next to it.

Both tie the grid topology to the shock topology and require geometric
operations whose cost and complexity grow with interactions.

## Extrapolated shock fitting

[Assonitis et al. (2022)](/sources/assonitis-2022.md) bring to structured
grids the unstructured discontinuity tracking that borrows from the shifted
boundary method: the shock, a chain of shock points carrying upstream and
downstream states, carves a hole in the grid by **blanking** the cells it
crosses — the capability overset-grid codes already have — and data pass
between the shock points and the hole boundary by truncated Taylor
extrapolation (cell gradients for second order). The shock points move with
the Rankine–Hugoniot speed. The flow solver runs as a black box needing only
cell blanking, the grid is never modified, and interacting discontinuities
and shock–wall interactions are handled. On a supersonic cylinder and on
regular and Mach reflections, the global convergence order is about two
(design) with fitting and slightly below one with capturing.

## Unstructured shock fitting near corners

[Muktieh & Assam (2026)](/sources/muktieh-2026.md) work with an open-source
unstructured shock-fitting code in which the shock is an internal boundary:
cells around it are removed, the region is remeshed locally (Delaunay
triangulation), the downstream state follows from the Rankine–Hugoniot
relations and the shock moves. They automate the setup (shock points
extracted from a shock-capturing solution, fitted initial shock lines, mesh
generation, configuration) with a released Python toolkit, and add special
points for shock initiation and reflection at geometric corners and a
revised regular-reflection point; the instabilities previously seen near
corners disappear on transonic airfoils, supersonic wedges and reflection
problems.

# Citations

- [Assonitis et al. (2022)](/sources/assonitis-2022.md) — introduction, algorithm, results, conclusions.
- [Muktieh & Assam (2026)](/sources/muktieh-2026.md) — abstract, §2–§3.
