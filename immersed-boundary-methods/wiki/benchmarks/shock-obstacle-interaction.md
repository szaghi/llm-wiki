---
type: Benchmark
title: "Shock–obstacle interaction"
description: "Compressible inviscid test problems in which a shock meets a solid body that is not aligned with the grid — shock reflection from a wedge or ramp (including double Mach reflection), supersonic flow past a wedge, prism or cylinder with an attached or bow shock, and moving shocks diffracting around a prism (Schardin's problem) or a cylinder — used to test immersed and embedded boundaries under strong discontinuities."
status: established
aliases: [shock reflection off a ramp, double Mach reflection, Schardin's problem, shock–cylinder interaction, supersonic flow past a cylinder]
tags: [benchmark, compressible, shock, cut-cell, ghost-cell]
timestamp: 2026-11-08T18:08:00Z
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

# Citations

- [Pember et al. (1995)](/sources/pember-1995.md) — §4.
- [Colella et al. (2006)](/sources/colella-2006.md) — results section.
- [Tan & Shu (2010)](/sources/tan-2010.md) — §3.
- [Chaudhuri et al. (2011)](/sources/chaudhuri-2011.md) — §3, §4.
