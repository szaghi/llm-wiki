---
type: Benchmark
title: "Hydrostatic white dwarf"
description: "A self-gravitating white dwarf with a realistic (Helmholtz) equation of state mapped from a 1D hydrostatic model onto a 3D Cartesian grid and evolved to see how well equilibrium is kept: spurious velocities, convergence, long-time expansion and the effect of bulk motion across the grid."
status: established
aliases: [stationary star, hydrostatic star, white dwarf in hydrostatic equilibrium, moving star test]
tags: [benchmark, self-gravity, hydro, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Hydrostatic white dwarf

**Set-up.** A white dwarf in hydrostatic equilibrium is integrated in 1D,
mapped onto a 3D Cartesian grid with Poisson self-gravity, and evolved
with nothing to drive it. Any velocity is an error of the discrete
balance between pressure gradient and gravity, made worse at the steep
stellar surface. Both runs use [CASTRO](/software/castro.md) with the
Helmholtz equation of state (see
[general equations of state](/methods/general-equation-of-state.md)).

**Runs.**
* *One second, uniform grids* ([Almgren et al. (2010)](/sources/almgren-2010.md),
  §8.4, eqs. 48–49, Figs. 10–11). Near-Chandrasekhar C/O white dwarf,
  central density $2.6\times10^9$ g cm$^{-3}$, central temperature
  $6\times10^8$ K, carbon and oxygen mass fractions 0.3 and 0.7,
  isentropic integration made isothermal below $10^7$ K. Domain
  $(5\times10^8\ \mathrm{cm})^3$ at $192^3$, $384^3$ and $768^3$ without
  refinement, Courant number 0.9, an outer sponge, monopole or Poisson
  gravity, run to 1 s (more than two sound-crossing times). The peak
  spurious velocity is below 1% of the central sound speed (about
  $9.4\times10^8$ cm s$^{-1}$) at the finest grid, and the maximum norm of
  the velocity inside $1.8\times10^8$ cm shows "clear second order
  convergence". The finest Poisson run has a larger peak velocity, from
  the stellar edge.
* *200 seconds, AMR* ([Katz et al. (2016)](/sources/katz-2016.md),
  §§3.1, 4.1, Figs. 4–5). A $0.9\,M_\odot$ white dwarf from an isothermal
  1D model (6.25 km spacing, mapped with 4 sub-zones per direction), at
  effective resolutions 256, 512 and 1024 with refined levels covering the
  star; radius measured as the volume with density above $10^3$ g
  cm$^{-3}$. The star expands to an equilibrium larger than the 1D model,
  less so at higher resolution; it is approximately in equilibrium only
  with a factor-4 refined level on the $256^3$ grid, and even then shows a
  late uptick. The final kinetic energy is **not** lower at the highest
  resolution than at the lower ones.
* *Moving star* ([Katz et al. (2016)](/sources/katz-2016.md), §4.3.2,
  Fig. 10). The same star with a bulk velocity of
  $2.56\times10^8$ cm s$^{-1}$, a domain four times larger and one more
  refined level to keep the effective resolution, the multipole origin
  following the star. It expands to nearly twice its radius at the lowest
  resolution and keeps growing at all resolutions by 200 s, "much worse at
  maintaining hydrostatic equilibrium" than the star at rest.

**Variants and reading.** The two papers differ in duration (1 s against
200 s), diagnostic (velocity norm against stellar radius and kinetic
energy), stellar model and mesh. Katz et al.'s result qualifies, without
contradicting, the second-order convergence of Almgren et al.: it holds
for the velocity over about two sound-crossing times, not for the
long-time equilibrium. Polytropic stars are covered by the
[self-gravitating polytrope](/benchmarks/self-gravitating-polytrope.md).

# Citations

1. [Almgren et al. (2010)](/sources/almgren-2010.md), §8.4, eqs. 48–49,
   Figs. 10–11 (arXiv v1).
2. [Katz et al. (2016)](/sources/katz-2016.md), §§3.1, 4.1, 4.3.2,
   Figs. 4–5, 10 (arXiv v2).
