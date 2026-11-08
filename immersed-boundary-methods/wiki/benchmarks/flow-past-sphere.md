---
type: Benchmark
title: "Flow past a sphere"
description: "Three-dimensional and axisymmetric flow around a sphere at Re of order 100–1000, used to test whether an immersed boundary on a non-conforming grid captures separation from a smooth surface, through the recirculation length, surface pressure and wake regimes."
status: established
aliases: [sphere wake, sphere]
tags: [benchmark, incompressible, separation, three-dimensional, validation]
timestamp: 2026-11-08T17:31:00Z
---

# Flow past a sphere

A sphere of diameter $D$ in a uniform stream, $Re=U_\infty D/\nu$. Unlike a
sharp-edged body, the separation point is set by viscous processes on a
smooth surface, which makes the sphere a demanding test of how an immersed
boundary represents the wall ([Fadlun et al. 2000](/sources/fadlun-2000.md), §3.2).

## Uses in the founding sources

- [Fadlun et al. (2000)](/sources/fadlun-2000.md), §3.2: [direct forcing](/methods/direct-forcing.md)
  with linear reconstruction on a stretched cylindrical grid, axisymmetric
  for $Re=100$–$1000$ and three-dimensional; the recirculation length and the
  surface pressure agree with body-fitted axisymmetric computations
  (Fadlun et al.'s refs. [16], [18]), for example a recirculation length
  $\ell/D=2.4$ at $Re=1000$ against $2.5$; outer boundary at 4 diameters and the sphere 3 diameters
  downstream of the inflow were found sufficient.
- [Kim et al. (2001)](/sources/kim-2001.md), §3.3: direct forcing with mass
  source, results in agreement with previous numerical and experimental data.

# Citations

- [Fadlun et al. (2000)](/sources/fadlun-2000.md) — §3.2.
- [Kim et al. (2001)](/sources/kim-2001.md) — §3.3.
