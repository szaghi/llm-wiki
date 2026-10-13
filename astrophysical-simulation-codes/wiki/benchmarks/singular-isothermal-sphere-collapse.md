---
type: Benchmark
title: "Singular isothermal sphere collapse"
description: "Inside-out collapse of an isothermal sphere with an r^-2 density profile, whose Shu (1977) similarity solution gives a constant accretion rate; it tests sink-particle accretion and the gas flow around a sink, including a sink advected across the grid."
status: established
aliases: [Shu collapse, Shu (1977) collapse, SIS collapse, isothermal sphere collapse, inside-out collapse]
tags: [benchmark, self-gravity, verification, sink-particles]
timestamp: 2026-10-12T00:00:00Z
---

# Singular isothermal sphere collapse

**Set-up.** An isothermal sphere with density proportional to $r^{-2}$,
at or above the critical (hydrostatic) density, collapses from the inside
out. The Shu (1977) similarity solutions give the density and velocity
profiles and a constant central accretion rate, a constant times
$c_s^3/G$. With a [sink particle](/methods/sink-particles.md) at the centre
the test measures whether the sink accretes at the analytic rate and how
much it disturbs the surrounding flow.

**Runs.**
* [Krumholz et al. (2004)](/sources/krumholz-2004.md), §3.1, Figs. 1–2.
  $1\,M_\odot$ sphere of H+He gas, $c_s = 0.18$ km s$^{-1}$ (about 10 K),
  10% above the critical density, initialized from the analytic solution
  at $t = 1.3\times10^{12}$ s (expansion wave at $2.4\times10^{16}$ cm,
  8 cells), 64 cells per sphere radius, Bondi–Hoyle accretion with
  $r_{\mathrm{acc}} = 4h$. Three runs: sphere at rest, and advected across
  the grid at $0.5\,c_s$ and $2\,c_s$. Density and velocity errors are "a
  few percent" in cells adjacent to the accretion zone and about 1%
  further out; the accretion rate is within about 1% in all three runs
  after a transient shorter than the zone's sound-crossing time.
* [Federrath et al. (2010)](/sources/federrath-2010.md), §3.4,
  Figs. 10–11. $R = 5\times10^{16}$ cm,
  $\rho(R) = 3.82\times10^{-18}$ g cm$^{-3}$, $M = 3.02\,M_\odot$,
  $T = 10$ K ($c_s = 0.166$ km s$^{-1}$), overdensity parameter
  $4\pi G\rho(R)R^2/c_s^2 = 29.3$; FLASH with threshold accretion. The
  sink accretes about $1.5\times10^{-4}\,M_\odot$ yr$^{-1}$, nearly
  constant until about $2\times10^4$ yr and equal to the mass flux
  through shells; the density profile steepens from $r^{-2}$ to
  $r^{-1.5}$ with infall Mach numbers above 15. Re-integrating the Shu
  solutions to an overdensity parameter of 50, the authors obtain
  $1.45\times10^{-4}\,M_\odot$ yr$^{-1}$ at 29.3, "excellent agreement"
  (about 3% from the two rates; no error is printed).

**Variants.** Krumholz et al. start near the critical density and move
the sink through the grid; Federrath et al. use a strongly overdense
sphere at rest. The same static sphere (hydrodynamics off) serves
Federrath et al. as a gas-to-sink gravity test, with test sinks on
circular orbits whose velocities come out 1–2% below analytic (§3.2).

Neither run reports a resolution study.

# Citations

1. [Krumholz et al. (2004)](/sources/krumholz-2004.md), §3.1, Figs. 1–2
   (arXiv preprint v1).
2. [Federrath et al. (2010)](/sources/federrath-2010.md), §§3.2, 3.4,
   Figs. 5–6, 10–11 (arXiv v2).
