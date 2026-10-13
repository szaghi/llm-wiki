---
type: Benchmark
title: "Supersonic flow past a circular cylinder (Cartesian embedded boundary)"
description: "Mach 3 flow past a unit cylinder computed on a Cartesian grid that does not fit the body, run to a steady bow shock; the standard robustness test of inverse Lax–Wendroff wall treatments for finite-difference WENO."
status: established
aliases: [Mach 3 cylinder, bow shock around a cylinder, supersonic cylinder]
tags: [benchmark, euler, 2d, boundary-treatment, cartesian-grid, steady]
timestamp: 2026-10-12T00:00:00Z
---

# Supersonic flow past a circular cylinder

**Set-up.** A Mach 3 stream meets a cylinder of unit radius on a
Cartesian grid that the body cuts at arbitrary distances, and the run
continues until a steady bow shock forms. The wall condition is imposed
through the ghost points by [inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md),
with WENO-type [extrapolation](/methods/weighted-extrapolation.md) near the
shock. Details differ between papers:
* Upper half by symmetry, reflecting at $y = 0$, far-field data at
  $x = -3$ and constant extrapolation at $y = 6$ and $x = 0$. The initial
  state is made compatible with the wall: $(\rho, p, v_x, v_y) = (1.4, 1, \sqrt{x^2+y^2} - 1, 0)$
  for $1 < \sqrt{x^2+y^2} \le 2$ and $(1.4, 1, 3, 0)$ elsewhere
  ([Ding, Shu & Zhang (2020)](/sources/ding-2020.md), Example 10, eq. 2.53).
* The full domain $(-3, 9)\times(-6, 6)$, run to $t = 40$, with the
  solution steady in $(-3, 0)\times(-6, 6)$
  ([Lu et al. (2021)](/sources/lu-2021.md), Example 3.11).
* Viscous, with an isothermal no-slip wall
  ([Lu et al. (2016)](/sources/lu-2016.md), §3).

**Results.**
* Fifth-order SILW with WENO extrapolation on $h = 1/40$ and $1/80$
  captures the bow shock (pressure contours from 2 to 15). The
  exactly conservative boundary fluxes give the same picture as plain
  SILW ([Ding, Shu & Zhang (2020)](/sources/ding-2020.md), Figs. 2.14–2.15).
* The flux-based ILW, with the solid wall imposed as zero normal mass
  flux, captures it stably on $h = 1/40$ and $1/80$
  ([Lu et al. (2021)](/sources/lu-2021.md), Fig. 8).
* Third-order convection–diffusion ILW with an isothermal no-slip wall
  captures it on a Cartesian grid ([Lu et al. (2016)](/sources/lu-2016.md), §3).

All results are qualitative contour plots; no paper reports a
quantitative measure such as the shock stand-off distance.

**Not to be confused with** the Mach 20 cylinder on a body-fitted grid
used to provoke the carbuncle ([hypersonic blunt-body test](/benchmarks/hypersonic-blunt-body.md);
[Simon & Mandal (2019)](/sources/simon-2019.md), §9.4).

# Citations

1. [Ding, Shu & Zhang (2020)](/sources/ding-2020.md), Example 10.
2. [Lu et al. (2021)](/sources/lu-2021.md), Example 3.11.
3. [Lu et al. (2016)](/sources/lu-2016.md), §3.
4. [Simon & Mandal (2019)](/sources/simon-2019.md), §9.4.
