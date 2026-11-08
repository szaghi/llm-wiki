---
type: Benchmark
title: "Shock–obstacle interaction"
description: "Compressible inviscid test problems in which a shock meets a solid body that is not aligned with the grid — shock reflection from a wedge or ramp (including double Mach reflection), supersonic flow past a wedge, prism or cylinder with an attached or bow shock, and moving shocks diffracting around a prism (Schardin's problem) or a cylinder — used to test immersed and embedded boundaries under strong discontinuities."
status: established
aliases: [shock reflection off a ramp, double Mach reflection, Schardin's problem, shock–cylinder interaction, supersonic flow past a cylinder]
tags: [benchmark, compressible, shock, cut-cell, ghost-cell]
timestamp: 2026-11-08T18:43:00Z
---

# Shock–obstacle interaction

Strong shocks hitting a body whose surface cuts the grid test whether an
immersed or embedded boundary is robust (no spurious waves, correct
reflection angles) and accurate (shock positions, triple-point trajectories,
surface pressure). Exact or theoretical references exist for oblique shocks
($\theta$–$\beta$–$M$ relation) and bow-shock stand-off distances.

## Uses in the sources

| source | method | problem | reported |
|---|---|---|---|
| [Pember et al. (1995)](/sources/pember-1995.md) | [cut cell](/methods/cut-cell-method.md) with [redistribution](/methods/redistribution.md) | shock reflection on a ramp, ramp represented as reflecting wall and as cut cells; Mach 10 flow past a $30^\circ$ ramp | about first-order $L^1$ convergence (shocks); slightly larger errors near the Mach stem with cut cells |
| [Colella et al. (2006)](/sources/colella-2006.md) | cut cell, formally consistent, hybrid with redistribution | shock reflection from a ramp (double-Mach configuration) | robust with large-amplitude discontinuities crossing the boundary |
| [Tan & Shu (2010)](/sources/tan-2010.md) | [inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md), fifth-order WENO | double Mach reflection with the $30^\circ$ wedge not aligned with the grid; supersonic flow past a cylinder | comparable to the grid-aligned computation |
| [Chaudhuri et al. (2011)](/sources/chaudhuri-2011.md) | [ghost cell](/methods/ghost-cell-method.md), fifth-order WENO | $M=3.5$ past a $20^\circ$ prism and a cylinder; moving shocks: Schardin's problem, $M_s=2.81$ shock on a cylinder | oblique-shock angle $34.5^\circ$ against $34.58^\circ$ theory; bow-shock angles and stand-off converge to theory with refinement; triple points and vortex trajectories match experiments of Chang and Chang |

## Uses in chunk 3

- [Natarajan et al. (2022)](/sources/natarajan-2022.md): moving embedded
  boundaries with adaptive refinement — shock–cylinder, shock–wedge and
  shock–cone interactions and a pitching NACA 0012 airfoil.
- [Ni et al. (2022)](/sources/ni-2022.md): shock diffraction around a cylinder
  with regular-to-Mach reflection and triple-point trajectories, a
  shock-deformed flexible panel and the detonation-driven fragmentation of a
  steel shell.

## Uses in chunk 4

- [Giuliani (2022)](/sources/giuliani-2022.md): Mach 10 double Mach reflection
  with DG and state redistribution on a cut-cell grid.
- [Reiss (2022)](/sources/reiss-2022.md): supersonic flow along a wedge and a
  confined blast wave with volume-fraction penalization.
- [Ménez et al. (2023)](/sources/menez-2023.md): shock reflection on a wall,
  supersonic wedge and supersonic sphere (drag, recirculation, separation,
  stand-off, Nusselt number) with penalization and continuous forcing.

## Uses in chunk 5

- [Turner et al. (2024)](/sources/turner-2024.md): supersonic cylinders and
  spheres with bow shocks, third-order IB.
- [Qi et al. (2024)](/sources/qi-2024.md): transonic sphere, airfoils and the
  ONERA M6 wing with DG on adaptive grids.
- [Marashi & Hejranfar (2025)](/sources/marashi-2025.md): double Mach
  reflection, supersonic flow over a half cylinder and two cylinders, and a shock
  hitting an array of cylinders.

## Uses in chunk 6

- [Yang, Bi & Jiang (2026)](/sources/yang-2026.md): double Mach reflection,
  shock–cylinder, supersonic cylinder, a supersonic wedge ($M=2$, $20^\circ$)
  checked against oblique-shock theory, and shock interaction with several
  cylinders.
- [Zeng, Song & Scovazzi (2025)](/sources/zeng-2025.md): double Mach reflection
  with the wedge immersed in a grid not aligned with the ramp.

# Citations

- [Pember et al. (1995)](/sources/pember-1995.md) — §4.
- [Colella et al. (2006)](/sources/colella-2006.md) — results section.
- [Tan & Shu (2010)](/sources/tan-2010.md) — §3.
- [Chaudhuri et al. (2011)](/sources/chaudhuri-2011.md) — §3, §4.
- [Natarajan et al. (2022)](/sources/natarajan-2022.md) — §3.
- [Ni et al. (2022)](/sources/ni-2022.md) — §6.
- [Reiss (2022)](/sources/reiss-2022.md) — §4.
- [Giuliani (2022)](/sources/giuliani-2022.md) — §6.
- [Ménez et al. (2023)](/sources/menez-2023.md) — §4.
- [Turner et al. (2024)](/sources/turner-2024.md) — §3–§4.
- [Qi et al. (2024)](/sources/qi-2024.md) — §4.
- [Marashi & Hejranfar (2025)](/sources/marashi-2025.md) — §4.
- [Yang, Bi & Jiang (2026)](/sources/yang-2026.md) — §4.3–§4.7.
- [Zeng, Song & Scovazzi (2025)](/sources/zeng-2025.md) — §4.6.
