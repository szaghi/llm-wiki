---
type: Benchmark
title: "Flow past a sphere"
description: "Three-dimensional and axisymmetric flow around a sphere at Re of order 100–1000, used to test whether an immersed boundary on a non-conforming grid captures separation from a smooth surface, through the recirculation length, surface pressure and wake regimes."
status: established
aliases: [sphere wake, sphere]
tags: [benchmark, incompressible, separation, three-dimensional, validation]
timestamp: 2026-11-08T18:08:00Z
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

## Later uses

- [Mittal et al. (2008)](/sources/mittal-2008.md), §3: [ghost cell](/methods/ghost-cell-method.md),
  stationary sphere $Re=100$–$350$ on a $16d\times15d\times15d$ domain, with the
  steady axisymmetric, steady non-axisymmetric and unsteady regimes, compared
  with Johnson and Patel and Marella et al.; suddenly accelerated sphere.
- [Uhlmann (2005)](/sources/uhlmann-2005.md), §5: a single sphere settling
  under gravity, then the sedimentation of 1000 spheres.
- [Mittal & Iaccarino (2005)](/sources/mittal-2005.md) cite LES of a sphere at
  $Re=3700$ and $10^4$ (Yun et al.) with Kim et al.'s forcing and mass source.

# Citations

- [Fadlun et al. (2000)](/sources/fadlun-2000.md) — §3.2.
- [Kim et al. (2001)](/sources/kim-2001.md) — §3.3.
- [Mittal & Iaccarino (2005)](/sources/mittal-2005.md) — applications.
- [Uhlmann (2005)](/sources/uhlmann-2005.md) — §5.
- [Mittal et al. (2008)](/sources/mittal-2008.md) — §3.
