---
type: Benchmark
title: "Lid-driven cavity"
description: "The driven cavity on a background grid with an overlapping inner grid, used to check incompressible overset solvers against single-grid references: the square cavity at Re 1000 for an ADER scheme and a long two-lid Stokes cavity for a conservative pressure correction."
status: established
aliases: [driven cavity, two-sided lid-driven cavity]
tags: [benchmark, incompressible]
timestamp: 2026-11-02T15:27:00Z
---

# Lid-driven cavity

A cavity driven by a moving lid is a steady incompressible test used by both sources; with an overset inner grid placed in the cavity it checks that the coupling does not distort the recirculation.

- [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md): square cavity at $Re=1000$, $h=1/128$, foreground grid $(0.21,0.79)^2$ in the no-shift configuration; $\psi_{\max}=0.1171$ and vorticity $1.9721$ at $(0.4687,0.5625)$, against $0.1179$ and about $2.05$ in the references they compare with; stream function and vorticity are identical on both grids in the overlap (§5.2, Table 1) ([ADER schemes on overlapping grids](/methods/ader-on-overset-grids.md)).
- [Chandar & Sitaraman (2022)](/sources/chandar-2022.md): Stokes flow in a long cavity with two lids, compared with the analytical solution of Gaskell et al.; overset RBF interpolation with and without their global conservation correction takes 1198 and 1195 iterations against 821 on a single mesh; the streamlines depend slightly on where the flux-balance cell is placed (§3.8, Table 5, Figs. 32–34) ([conservative overset interface](/methods/conservative-overset-interface.md)).

- [Devlin et al. (2023)](/sources/devlin-2023.md): DFVF-overset results close to single-grid solutions with similar convergence toward a benchmark; on a relatively coarse grid a tertiary vortex is resolved that interpolation-based overset solutions miss (Abstract, §4) ([interpolation-free overset coupling](/methods/interpolation-free-overset-coupling.md)).

## Qualifications

- Chandar & Sitaraman (2022) describe the cavity as of height 5 and width 1 but print the mesh extents with $x$ and $y$ transposed (§3.8) *(compiler check, not in the sources)*.

# Citations

- [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) — §5.2, Table 1.
- [Chandar & Sitaraman (2022)](/sources/chandar-2022.md) — §3.8, Table 5.
- [Devlin et al. (2023)](/sources/devlin-2023.md) — Abstract, §4.
