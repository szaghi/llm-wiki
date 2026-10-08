---
type: Benchmark
title: "Shock–vortex interaction"
description: "A small isentropic vortex convected through a stationary Mach 1.1 shock: tests capture of weak acoustic and vortical structure crossing a shock, grid-aligned or oblique."
status: established
aliases: [shock vortex interaction, Pao-Salas problem]
tags: [benchmark, euler, 2d, acoustics]
timestamp: 2026-10-08T00:00:00Z
---

# Shock–vortex interaction

**Set-up** (Pao & Salas). A stationary Mach 1.1 shock, a vortex
superposed on the upstream flow as perturbations of velocity,
temperature $T = p/\rho$ and entropy, with strength $0.3$, critical
radius $r_c = 0.05$ and decay parameter $0.204$, centred at
$(0.25, 0.5)$ for a shock at $x = 0.5$ on $[0, 2]\times[0, 1]$
([Jiang & Shu (1996)](/sources/jiang-1996.md), §8.3 Example 5).

**Results.**
* On a $251\times 100$ grid refined around the shock, WENO-LF-5-PS,
  WENO-LF-5 and ENO-LF-4 give about the same resolution, the WENO schemes
  with less noise; the pressure–entropy weights work here because the
  reflective top and bottom boundaries do not matter
  ([Jiang & Shu (1996)](/sources/jiang-1996.md)).
* [Balsara & Shu (2000)](/sources/balsara-2000.md) (§VII.c) rotate the
  problem: shock normal and mean flow at 45° to the grid on
  $[0, 1.5]^2$, $150\times 150$. $r = 5$ MPWENO keeps the vortex circular
  and the shock intact through the interaction; dimensionally split PPM
  with Lapidus viscosity shows strong corruption of density as the core
  and then the wave front cross the shock. They conclude that tests
  should not be aligned with the grid.

# Citations

1. [Jiang & Shu (1996)](/sources/jiang-1996.md), §8.3 Example 5.
2. [Balsara & Shu (2000)](/sources/balsara-2000.md), §VII.c.
